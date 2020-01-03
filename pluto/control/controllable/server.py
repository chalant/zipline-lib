import threading
import signal
from abc import ABC, abstractmethod
from concurrent import futures
import queue

import grpc

from google.protobuf import empty_pb2 as emp

from pluto.coms.utils import conversions
from pluto.trading_calendars import calendar_utils as cu
from pluto.coms.utils import conversions as crv
from pluto.control.controllable import states as st
from pluto.control.controllable import simulation_controllable as sc
from pluto.control.controllable import commands

from protos import controllable_pb2
from protos import calendar_pb2
from protos.clock_pb2 import (
    SESSION_START,
    SESSION_END,
    BAR,
    MINUTE_END,
    TRADE_END,
    BEFORE_TRADING_START
)

import click

from protos import controllable_pb2_grpc as cbl_rpc

class FrequencyFilter(ABC):
    @abstractmethod
    def filter(self, evt_exc_pairs):
        raise NotImplementedError

class DayFilter(FrequencyFilter):
    def filter(self, evt_exc_pairs):
        exchanges = []
        for evt, exc in evt_exc_pairs:
            if evt == TRADE_END:
                exchanges.append(exc)
        return exchanges

class MinuteFilter(FrequencyFilter):
    def filter(self, evt_exc_pairs):
        exchanges = []
        for evt, exc in evt_exc_pairs:
            if evt == TRADE_END or evt == BAR:
                exchanges.append(exc)
        return exchanges

class ControllableService(cbl_rpc.ControllableServicer):
    #todo: we need to queue requests from the controller until the controllable is ready
    # to execute them...
    def __init__(self, controller_url):
        self._calendar = None
        self._controller = None
        self._ctl_url = controller_url

        self._session = None

        self._stop = False
        self._start_flag = False
        self._session_start = False
        self._started = False

        self._bfs_flag = False
        self._frequency_filter = None

        self._exchanges = None
        self._num_exchanges = None

        self._session_end = []

        self._out_session = st.OutSession(self)
        self._active = st.Active(self)
        self._in_session = st.InSession(self)
        self._bfs = st.BFS(self)
        self._idle = idle = st.Idle(self)

        self._state = idle

        #used for queueing commands
        self._queue = queue.Queue()
        self._thread = None

    #todo need to use an interceptor to check for tokens etc.
    def _with_metadata(self, rpc, params):
        '''If we're not registered, an RpcError will be raised. Registration is handled
        externally.'''
        return rpc(params, metadata=(('Token', self._token)))

    @property
    def out_session(self):
        return self._out_session

    @property
    def active(self):
        return self._active

    @property
    def in_session(self):
        return self._in_session

    @property
    def bfs(self):
        return self._bfs

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def exchanges(self):
        return self._exchanges

    def stop(self):
        pass

    def Initialize(self, request_iterator, context):
        b = b''
        for bytes_ in request_iterator:
            b += bytes_

        params = controllable_pb2.InitParams()
        params.ParseFromString(b)

        id_ = params.id #the id of the controllable => will be used in performance updates
        exchanges = params.exchanges
        platform = params.platform
        capital = params.capital
        max_leverage = params.max_leverage
        calendar = params.calendar #todo: instanciate the calendar from the message
        strategy = params.strategy
        data_frequency = params.data_frequency
        start_dt = params.start
        end_dt = params.end

        if data_frequency ==  'day':
            self._frequency_filter = DayFilter()
        elif data_frequency == 'minute':
            self._frequency_filter = MinuteFilter()

        self._exchanges = exchanges
        self._num_exchanges = len(exchanges)

        mode = params.mode

        controllable = get_controllable(params.mode)
        if controllable:
            self._controllable = controllable
            controllable.initialize(
                start_dt,
                end_dt,
                calendar,
                strategy,
                capital,
                max_leverage,
                data_frequency,
                mode,
                platform)
            self._state = self._out_session
            #run the thread
            self._thread = thread = threading.Thread(self._run())
            thread.start()
        else:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Mode {} doesn't exist".format(mode))

        return emp.Empty()

    def Stop(self, request, context):
        #todo needs to liquidate positions and wipe the state.
        self._stop = True
        return emp.Empty()

    def UpdateParameters(self, request, context):
        self._controllable.update_parameters(request)
        return emp.Empty()

    def UpdateAccount(self, request_iterator, context):
        self._controllable.update_account(request_iterator)
        return emp.Empty()

    def UpdateBroker(self, request_iterator, context):
        pass


    def UpdateDataBundle(self, request_iterator, context):
        self._controllable.ingest_data(request_iterator)
        return emp.Empty()

    def ClockUpdate(self, request, context):
        '''Note: an update call might arrive while the step is executing..., so
        we must queue the update message... => the step must be a thread that pulls data
        from the queue...
        '''

        #todo: in daily mode, we should simulate the slippage on the current bar,
        # after placing orders.
        # NOTE: use FixedBasisPointsSlippage for slippage simulation.

        self._queue.put(
            commands.ClockUpdate(
                self._controller,
                self._controllable,
                self._frequency_filter,
                self._state,
                request)
        )

        return emp.Empty()

    def _update(self, dt, event, calendar, broker_state):
        raise NotImplementedError

    def _run(self):
        queue = self._queue
        while not self._stop:
            self._execute(queue.get())

    def _execute(self, command):
        command()

    def UpdateCalendar(self, request_iterator, context):
        b = b''
        for bytes_ in request_iterator:
            b += bytes_

        calendar = calendar_pb2.Calendar()
        calendar.ParseFromString(b)
        self._calendar = self._update_calendar(
            conversions.to_datetime(calendar.start).tz_localize('UTC').normalize(),
            conversions.to_datetime(calendar.end).tz_localize('UTC').normalize(),
            calendar)
        return emp.Empty()

    def _update_calendar(self, start_dt, end_dt, proto_calendar):
        return cu.TradingCalendar(start_dt, end_dt, proto_calendar)

class Server(object):
    def __init__(self):
        self._event = threading.Event()
        self._server = grpc.server(futures.ThreadPoolExecutor(10))

    def start(self, url, controllable):
        server = self._server
        server.add_insecure_port(url)
        cbl_rpc.add_ControllableServicer_to_server(controllable, server)
        server.start()
        self._event.wait()
        controllable.stop()
        server.stop()

    def stop(self):
        self._event.set()

_SERVER = Server()

def get_controllable(mode):
    '''

    Parameters
    ----------
    mode: str

    Returns
    -------
    pluto.control.controllable.controllable.Controllable
    '''
    if mode == 'simulation':
        return sc.SimulationControllable()
    elif mode == 'live':
        return
    else:
        return

def termination_handler(signum, frame):
    _SERVER.stop()

def interruption_handler(signum, frame):
    _SERVER.stop()

signal.signal(signal.SIGINT, interruption_handler)
signal.signal(signal.SIGTERM, termination_handler)

@click.group()
def cli():
    pass

#todo: when launching, we need to check if a previous state exists...
# if it does, we need to request all events that occurred starting from the latest checkpoint
# if we haven't reached the last bar, we can continue execution (execute on the next bar).
# If the session ended send performance packet etc. Any events between last checkpoint and now
# that doesn't involve placing trades (session_end, minute_end, session_start) can be executed.
# bar events will be executed on the next call after launch. When "replaying" the events, we
# should not make any call-back to the controller or place any trades. We "replay" so that we can
# synchronize variables (calendars, session_index etc.) => We need a "recovery" state or something
# after that, we can resume to normal execution (in-session etc.)
# all this logic must be done when launching the script.
@cli.command()
@click.argument('framework_url')
@cli.argument('controllable_url')
def start(framework_url, controllable_url):
    service = ControllableService(framework_url)
    #todo: check if we have a state file.

    #run forever or until an exception occurs, in which case, send back a report to the controller
    #or write to a log file. If the strategy crashes internally, there might be some bug that
    #need reviewing
    try:
        _SERVER.start(
            controllable_url,
            service)
    except Exception:
        #todo: store the state and send back a report to the controller.
        state = service.get_state()

    #if the script crashes for external reasons  it will restart and resume from its previous state.


if __name__ == '__main__':
    cli()

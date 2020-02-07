from pluto.control.modes import mode
from pluto.control.events_log import events_log

class LiveControlMode(mode.ControlMode):
    def __init__(self, framework_url):
        super(LiveControlMode, self).__init__(framework_url)

    def _create_process(self, session_id, framework_url):
        #todo:
        # we can terminate the pod (kubectl delete pod) or through api:
        # /api/v1/namespaces/{namespace}/pods/{name}
        # when deploying a pod, we should give it a unique name that we can use to make
        # delete, exec calls, etc. => The pods shall be named by session_id
        # controllables are made such that they can be restarted when they fail, and resume
        # from where they left-off
        # we will need a "service" to be able to call the pod, since it might restart, it will
        # get a new ip address, so we need a service. or we could find the node using its name,
        # then get its cluster-ip => this is the preferred approach PROBLEM: we might need to do
        # this on each iteration... at least we have more control over the "refresh" frequency
        return

    def _broker_update(self, dt, evt, event_writer, broker, processes):
        '''

        Parameters
        ----------
        dt
        evt
        event_writer: pluto.control.events_log.events_log._EventsLogWriter
        broker: pluto.broker.broker.Broker
        processes: typing.Iterable[pluto.control.modes.processes.process_factory.ProcessFactory]

        '''
        # called before clock update by the loop

        # the broker_state is an object of type message
        broker_state = self._broker.update(dt, evt)
        # todo: update all processes accounts with broker data...
        # todo: this isn't done in simulation mode...
        for process in processes:
            process.account_update(broker_state)
        event_writer.write_event('broker', broker_state)

    def _create_event_writer(self):
        return events_log.writer('live')


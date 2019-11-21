import secrets

from concurrent import futures

import grpc

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

from protos import interface_pb2 as itf_msg
from protos import interface_pb2_grpc as itf_rpc

from contrib.interface import editor
from contrib.interface.utils import grpc_interceptors as interceptors
from contrib.interface import monitor, credentials
from contrib.interface.utils import db_utils as utils, security


class Account(itf_rpc.GatewayServicer):
    def __init__(self, credentials, directory):
        '''

        Parameters
        ----------
        credentials: contrib.control.interface.credentials.Credentials
                    the initial credentials
        directory: contrib.interface.directory.Directory
        '''

        self._credentials = credentials
        self._directory = drt = directory

        self._editor = edt = editor.Editor(drt)
        self._monitor = mtr = monitor.Monitor(drt)


        self._logged_in = False

        self._authenticity = ath = interceptors.get_interceptors('authenticity')
        self._availability = avl = interceptors.get_interceptors('availability')

        self._server = server = grpc.server(
            futures.ThreadPoolExecutor(),
            interceptors=(ath + avl))

        itf_rpc.add_EditorServicer_to_server(edt, server)
        itf_rpc.add_MonitorServicer_to_server(mtr, server)

    def Login(self, request, context):
        #todo: logout after some inactivity
        # create a thread that logs out the client after a timeout is reached
        # we need to reset the timeout each time the authenticated client performs an action
        #for now, the service only accepts one client at a time.
        #for multiple clients we would need another structure (sessions)
        if not self._logged_in:
            try:
                self._check_credentials(request.username, request.password)
                token = self._create_token()  # a new token is created each successful login.

                for validator in self._authenticity:
                    validator.token = token
                self._logged_in = True
                return itf_msg.LoginResponse(token=token)
            except ValueError:
                context.abort(grpc.StatusCode.UNAUTHENTICATED)
        else:
            return itf_msg.LoginResponse()


    def Logout(self, request, context):
        self._logout()

    def _logout(self):
        #remove tokens
        for interceptor in self._authenticity:
            interceptor.token = None

        #set availability to false
        for interceptor in self._availability:
            interceptor.available = False

        self._logged_in = False

    def start(self, port, address='localhost:'):
        self._server.start(address+port)

    def stop(self, grace=0):
        self._logout()
        self._server.stop(grace)

    def _check_credentials(self, username, password):
        with credentials.read() as r:
            crd = r.query(credentials.Credentials)\
                .filter_by(username=username).one()
            if crd:
                salt = crd.salt
                hash_ = crd.hash_
                if hash_ != security.get_hash(salt, password):
                    raise ValueError('Not signed in')
            else:
                raise ValueError('Not signed in')

    def _create_token(self):
        return secrets.token_hex()
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protos import controller_pb2 as protos_dot_controller__pb2
from protos import data_bundle_pb2 as protos_dot_data__bundle__pb2
from protos import data_pb2 as protos_dot_data__pb2
from protos import dev_pb2 as protos_dot_dev__pb2


class DevStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetSession = channel.stream_stream(
        '/Dev/GetSession',
        request_serializer=protos_dot_dev__pb2.StrategyRequest.SerializeToString,
        response_deserializer=protos_dot_data__pb2.Data.FromString,
        )
    self.Deploy = channel.unary_unary(
        '/Dev/Deploy',
        request_serializer=protos_dot_dev__pb2.DeploymentRequest.SerializeToString,
        response_deserializer=protos_dot_dev__pb2.DeploymentReply.FromString,
        )
    self.New = channel.stream_stream(
        '/Dev/New',
        request_serializer=protos_dot_data__bundle__pb2.CompoundDomainDef.SerializeToString,
        response_deserializer=protos_dot_data__pb2.Data.FromString,
        )
    self.Modify = channel.stream_stream(
        '/Dev/Modify',
        request_serializer=protos_dot_data__bundle__pb2.CompoundDomainDef.SerializeToString,
        response_deserializer=protos_dot_data__pb2.Data.FromString,
        )
    self.Push = channel.stream_unary(
        '/Dev/Push',
        request_serializer=protos_dot_data__pb2.Data.SerializeToString,
        response_deserializer=protos_dot_dev__pb2.DeploymentReply.FromString,
        )
    self.DeploymentStatus = channel.unary_stream(
        '/Dev/DeploymentStatus',
        request_serializer=protos_dot_dev__pb2.DeploymentStatusRequest.SerializeToString,
        response_deserializer=protos_dot_dev__pb2.DeploymentStatusReply.FromString,
        )
    self.MountBroker = channel.unary_unary(
        '/Dev/MountBroker',
        request_serializer=protos_dot_dev__pb2.BrokerID.SerializeToString,
        response_deserializer=protos_dot_dev__pb2.MountStatus.FromString,
        )
    self.List = channel.unary_stream(
        '/Dev/List',
        request_serializer=protos_dot_dev__pb2.ListRequest.SerializeToString,
        response_deserializer=protos_dot_data__pb2.Data.FromString,
        )
    self.Domains = channel.unary_stream(
        '/Dev/Domains',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=protos_dot_data__pb2.Data.FromString,
        )
    self.GetController = channel.unary_unary(
        '/Dev/GetController',
        request_serializer=protos_dot_controller__pb2.ControllerRequest.SerializeToString,
        response_deserializer=protos_dot_controller__pb2.ControllerReply.FromString,
        )


class DevServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetSession(self, request_iterator, context):
    """
    The environment is stored for the lifetime of the application.
    A strategy returned by GetStrategy cannot be modified. (It can only be ran or stopped)
    A strategy returned by ModifyStrategy returns a simulation environment. It can optionally
    be stopped if it is running in a paper env or live env.)
    This service stores timestamped version of each strategy, so that we could roll-back,
    to a previous version of an implementation.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Deploy(self, request, context):
    """request a strategy deployment in a new environment (depending on the environment,
    some external actor might need to confirm (admin, user with the right credentials...))
    deploys a specific session.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def New(self, request_iterator, context):
    """the client also sends a name as metadata...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Modify(self, request_iterator, context):
    """adds a new version to the list of strategies
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Push(self, request_iterator, context):
    """pushes one or more strategies to the the hub...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeploymentStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MountBroker(self, request, context):
    """mounts a broker to be used by the controllers. The broker is a service that must
    implement a certain interface... Note this method cannot be called by any user.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """get a list of the strategies on the current branch
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Domains(self, request, context):
    """returns a list of compound domain def.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetController(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DevServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetSession': grpc.stream_stream_rpc_method_handler(
          servicer.GetSession,
          request_deserializer=protos_dot_dev__pb2.StrategyRequest.FromString,
          response_serializer=protos_dot_data__pb2.Data.SerializeToString,
      ),
      'Deploy': grpc.unary_unary_rpc_method_handler(
          servicer.Deploy,
          request_deserializer=protos_dot_dev__pb2.DeploymentRequest.FromString,
          response_serializer=protos_dot_dev__pb2.DeploymentReply.SerializeToString,
      ),
      'New': grpc.stream_stream_rpc_method_handler(
          servicer.New,
          request_deserializer=protos_dot_data__bundle__pb2.CompoundDomainDef.FromString,
          response_serializer=protos_dot_data__pb2.Data.SerializeToString,
      ),
      'Modify': grpc.stream_stream_rpc_method_handler(
          servicer.Modify,
          request_deserializer=protos_dot_data__bundle__pb2.CompoundDomainDef.FromString,
          response_serializer=protos_dot_data__pb2.Data.SerializeToString,
      ),
      'Push': grpc.stream_unary_rpc_method_handler(
          servicer.Push,
          request_deserializer=protos_dot_data__pb2.Data.FromString,
          response_serializer=protos_dot_dev__pb2.DeploymentReply.SerializeToString,
      ),
      'DeploymentStatus': grpc.unary_stream_rpc_method_handler(
          servicer.DeploymentStatus,
          request_deserializer=protos_dot_dev__pb2.DeploymentStatusRequest.FromString,
          response_serializer=protos_dot_dev__pb2.DeploymentStatusReply.SerializeToString,
      ),
      'MountBroker': grpc.unary_unary_rpc_method_handler(
          servicer.MountBroker,
          request_deserializer=protos_dot_dev__pb2.BrokerID.FromString,
          response_serializer=protos_dot_dev__pb2.MountStatus.SerializeToString,
      ),
      'List': grpc.unary_stream_rpc_method_handler(
          servicer.List,
          request_deserializer=protos_dot_dev__pb2.ListRequest.FromString,
          response_serializer=protos_dot_data__pb2.Data.SerializeToString,
      ),
      'Domains': grpc.unary_stream_rpc_method_handler(
          servicer.Domains,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=protos_dot_data__pb2.Data.SerializeToString,
      ),
      'GetController': grpc.unary_unary_rpc_method_handler(
          servicer.GetController,
          request_deserializer=protos_dot_controller__pb2.ControllerRequest.FromString,
          response_serializer=protos_dot_controller__pb2.ControllerReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Dev', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

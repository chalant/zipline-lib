# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from contrib.coms.protos import data_bundle_pb2 as contrib_dot_coms_dot_protos_dot_data__bundle__pb2
from contrib.control import controller_pb2 as contrib_dot_control_dot_controller__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ControllerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Deploy = channel.stream_stream(
        '/Controller/Deploy',
        request_serializer=contrib_dot_control_dot_controller__pb2.Strategy.SerializeToString,
        response_deserializer=contrib_dot_control_dot_controller__pb2.DeploymentStatus.FromString,
        )
    self.PerformancePacketUpdate = channel.unary_unary(
        '/Controller/PerformancePacketUpdate',
        request_serializer=contrib_dot_control_dot_controller__pb2.PerformancePacket.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Stop = channel.unary_unary(
        '/Controller/Stop',
        request_serializer=contrib_dot_control_dot_controller__pb2.StopParams.SerializeToString,
        response_deserializer=contrib_dot_control_dot_controller__pb2.StopStatus.FromString,
        )
    self.Run = channel.unary_unary(
        '/Controller/Run',
        request_serializer=contrib_dot_control_dot_controller__pb2.RunParams.SerializeToString,
        response_deserializer=contrib_dot_control_dot_controller__pb2.Status.FromString,
        )
    self.Watch = channel.unary_stream(
        '/Controller/Watch',
        request_serializer=contrib_dot_control_dot_controller__pb2.ID.SerializeToString,
        response_deserializer=contrib_dot_control_dot_controller__pb2.PerformancePacket.FromString,
        )
    self.GetStrategy = channel.unary_stream(
        '/Controller/GetStrategy',
        request_serializer=contrib_dot_control_dot_controller__pb2.ID.SerializeToString,
        response_deserializer=contrib_dot_control_dot_controller__pb2.Strategy.FromString,
        )
    self.GetEnvironment = channel.unary_stream(
        '/Controller/GetEnvironment',
        request_serializer=contrib_dot_coms_dot_protos_dot_data__bundle__pb2.Domain.SerializeToString,
        response_deserializer=contrib_dot_control_dot_controller__pb2.Environment.FromString,
        )
    self.GetStrategyList = channel.unary_stream(
        '/Controller/GetStrategyList',
        request_serializer=contrib_dot_control_dot_controller__pb2.Filter.SerializeToString,
        response_deserializer=contrib_dot_control_dot_controller__pb2.Strategy.FromString,
        )
    self.UpdateLevCap = channel.unary_unary(
        '/Controller/UpdateLevCap',
        request_serializer=contrib_dot_control_dot_controller__pb2.LevCap.SerializeToString,
        response_deserializer=contrib_dot_control_dot_controller__pb2.CapitalAssignmentStatus.FromString,
        )


class ControllerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Deploy(self, request_iterator, context):
    """deploys a strategy
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PerformancePacketUpdate(self, request, context):
    """This method is a callback for controllables: each controllable sends back a performance
    packet to the controller
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Stop(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Run(self, request, context):
    """runs a strategy with initial parameters
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Watch(self, request, context):
    """we can watch the performance of the strategy in real-time...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStrategy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEnvironment(self, request, context):
    """retrieve the environment on which the strategy will be developed
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStrategyList(self, request, context):
    """returns a list of deployed strategies
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateLevCap(self, request, context):
    """dynamically updates capital and/or leverage of a running strategy
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ControllerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Deploy': grpc.stream_stream_rpc_method_handler(
          servicer.Deploy,
          request_deserializer=contrib_dot_control_dot_controller__pb2.Strategy.FromString,
          response_serializer=contrib_dot_control_dot_controller__pb2.DeploymentStatus.SerializeToString,
      ),
      'PerformancePacketUpdate': grpc.unary_unary_rpc_method_handler(
          servicer.PerformancePacketUpdate,
          request_deserializer=contrib_dot_control_dot_controller__pb2.PerformancePacket.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Stop': grpc.unary_unary_rpc_method_handler(
          servicer.Stop,
          request_deserializer=contrib_dot_control_dot_controller__pb2.StopParams.FromString,
          response_serializer=contrib_dot_control_dot_controller__pb2.StopStatus.SerializeToString,
      ),
      'Run': grpc.unary_unary_rpc_method_handler(
          servicer.Run,
          request_deserializer=contrib_dot_control_dot_controller__pb2.RunParams.FromString,
          response_serializer=contrib_dot_control_dot_controller__pb2.Status.SerializeToString,
      ),
      'Watch': grpc.unary_stream_rpc_method_handler(
          servicer.Watch,
          request_deserializer=contrib_dot_control_dot_controller__pb2.ID.FromString,
          response_serializer=contrib_dot_control_dot_controller__pb2.PerformancePacket.SerializeToString,
      ),
      'GetStrategy': grpc.unary_stream_rpc_method_handler(
          servicer.GetStrategy,
          request_deserializer=contrib_dot_control_dot_controller__pb2.ID.FromString,
          response_serializer=contrib_dot_control_dot_controller__pb2.Strategy.SerializeToString,
      ),
      'GetEnvironment': grpc.unary_stream_rpc_method_handler(
          servicer.GetEnvironment,
          request_deserializer=contrib_dot_coms_dot_protos_dot_data__bundle__pb2.Domain.FromString,
          response_serializer=contrib_dot_control_dot_controller__pb2.Environment.SerializeToString,
      ),
      'GetStrategyList': grpc.unary_stream_rpc_method_handler(
          servicer.GetStrategyList,
          request_deserializer=contrib_dot_control_dot_controller__pb2.Filter.FromString,
          response_serializer=contrib_dot_control_dot_controller__pb2.Strategy.SerializeToString,
      ),
      'UpdateLevCap': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateLevCap,
          request_deserializer=contrib_dot_control_dot_controller__pb2.LevCap.FromString,
          response_serializer=contrib_dot_control_dot_controller__pb2.CapitalAssignmentStatus.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Controller', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

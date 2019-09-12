# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from contrib.control import clock_pb2 as contrib_dot_control_dot_clock__pb2
from contrib.control import controller_pb2 as contrib_dot_control_dot_controller__pb2
from contrib.control import data_pb2 as contrib_dot_control_dot_data__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ControllerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.PerformancePacketUpdate = channel.stream_unary(
        '/Controller/PerformancePacketUpdate',
        request_serializer=contrib_dot_control_dot_data__pb2.Data.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Stop = channel.unary_unary(
        '/Controller/Stop',
        request_serializer=contrib_dot_control_dot_controller__pb2.StopParams.SerializeToString,
        response_deserializer=contrib_dot_control_dot_controller__pb2.StopStatus.FromString,
        )
    self.Run = channel.stream_unary(
        '/Controller/Run',
        request_serializer=contrib_dot_control_dot_controller__pb2.RunParams.SerializeToString,
        response_deserializer=contrib_dot_control_dot_controller__pb2.Status.FromString,
        )
    self.UpdateLevCap = channel.unary_unary(
        '/Controller/UpdateLevCap',
        request_serializer=contrib_dot_control_dot_controller__pb2.LevCap.SerializeToString,
        response_deserializer=contrib_dot_control_dot_controller__pb2.CapitalAssignmentStatus.FromString,
        )
    self.ClockUpdate = channel.unary_unary(
        '/Controller/ClockUpdate',
        request_serializer=contrib_dot_control_dot_clock__pb2.ClockEvent.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class ControllerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def PerformancePacketUpdate(self, request_iterator, context):
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

  def Run(self, request_iterator, context):
    """runs a strategy with initial parameters
    this will pull the strategy from the store and run it.
    can run multiple strategies at the same time...
    we can watch the performance of the strategy in real-time...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateLevCap(self, request, context):
    """rpc Watch (StrategyID) returns (stream Data);

    dynamically updates capital and/or leverage of a running strategy
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ClockUpdate(self, request, context):
    """TODO: should be able to check for available domains.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ControllerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'PerformancePacketUpdate': grpc.stream_unary_rpc_method_handler(
          servicer.PerformancePacketUpdate,
          request_deserializer=contrib_dot_control_dot_data__pb2.Data.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Stop': grpc.unary_unary_rpc_method_handler(
          servicer.Stop,
          request_deserializer=contrib_dot_control_dot_controller__pb2.StopParams.FromString,
          response_serializer=contrib_dot_control_dot_controller__pb2.StopStatus.SerializeToString,
      ),
      'Run': grpc.stream_unary_rpc_method_handler(
          servicer.Run,
          request_deserializer=contrib_dot_control_dot_controller__pb2.RunParams.FromString,
          response_serializer=contrib_dot_control_dot_controller__pb2.Status.SerializeToString,
      ),
      'UpdateLevCap': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateLevCap,
          request_deserializer=contrib_dot_control_dot_controller__pb2.LevCap.FromString,
          response_serializer=contrib_dot_control_dot_controller__pb2.CapitalAssignmentStatus.SerializeToString,
      ),
      'ClockUpdate': grpc.unary_unary_rpc_method_handler(
          servicer.ClockUpdate,
          request_deserializer=contrib_dot_control_dot_clock__pb2.ClockEvent.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Controller', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
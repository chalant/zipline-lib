# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from protos import broker_pb2 as contrib_dot_coms_dot_protos_dot_broker__pb2
from protos import controller_service_pb2 as contrib_dot_coms_dot_protos_dot_controller__service__pb2
from protos import data_bundle_pb2 as contrib_dot_coms_dot_protos_dot_data__bundle__pb2
from contrib.control.clock_utils import clock_pb2 as contrib_dot_control_dot_clock_dot_clock__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ControllableStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ReceiveDataBundle = channel.unary_unary(
        '/Controllable/ReceiveDataBundle',
        request_serializer=contrib_dot_coms_dot_protos_dot_data__bundle__pb2.Bundle.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ClockUpdate = channel.unary_unary(
        '/Controllable/ClockUpdate',
        request_serializer=contrib_dot_control_dot_clock_dot_clock__pb2.ClockEvent.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.UpdateParameters = channel.unary_unary(
        '/Controllable/UpdateParameters',
        request_serializer=contrib_dot_coms_dot_protos_dot_controller__service__pb2.ParametersUpdateMessage.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Initialize = channel.unary_unary(
        '/Controllable/Initialize',
        request_serializer=contrib_dot_coms_dot_protos_dot_controller__service__pb2.InitialParameters.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.UpdateBroker = channel.unary_unary(
        '/Controllable/UpdateBroker',
        request_serializer=contrib_dot_coms_dot_protos_dot_broker__pb2.BrokerState.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.UpdateCalendar = channel.unary_unary(
        '/Controllable/UpdateCalendar',
        request_serializer=contrib_dot_control_dot_clock_dot_clock__pb2.CalendarMetadata.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class ControllableServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ReceiveDataBundle(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ClockUpdate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateParameters(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Initialize(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateBroker(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateCalendar(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ControllableServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ReceiveDataBundle': grpc.unary_unary_rpc_method_handler(
          servicer.ReceiveDataBundle,
          request_deserializer=contrib_dot_coms_dot_protos_dot_data__bundle__pb2.Bundle.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ClockUpdate': grpc.unary_unary_rpc_method_handler(
          servicer.ClockUpdate,
          request_deserializer=contrib_dot_control_dot_clock_dot_clock__pb2.ClockEvent.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'UpdateParameters': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateParameters,
          request_deserializer=contrib_dot_coms_dot_protos_dot_controller__service__pb2.ParametersUpdateMessage.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Initialize': grpc.unary_unary_rpc_method_handler(
          servicer.Initialize,
          request_deserializer=contrib_dot_coms_dot_protos_dot_controller__service__pb2.InitialParameters.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'UpdateBroker': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateBroker,
          request_deserializer=contrib_dot_coms_dot_protos_dot_broker__pb2.BrokerState.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'UpdateCalendar': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateCalendar,
          request_deserializer=contrib_dot_control_dot_clock_dot_clock__pb2.CalendarMetadata.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Controllable', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

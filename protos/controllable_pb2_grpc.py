# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protos import controller_pb2 as protos_dot_controller__pb2
from protos import data_pb2 as protos_dot_data__pb2


class ControllableStub(object):
  """TODO: State: bytes...

  A service to be controller by a controller service
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.UpdateDataBundle = channel.stream_unary(
        '/Controllable/UpdateDataBundle',
        request_serializer=protos_dot_data__pb2.Data.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.UpdateParameters = channel.unary_unary(
        '/Controllable/UpdateParameters',
        request_serializer=protos_dot_controller__pb2.ParametersUpdateMessage.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Initialize = channel.stream_unary(
        '/Controllable/Initialize',
        request_serializer=protos_dot_data__pb2.Data.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Update = channel.stream_stream(
        '/Controllable/Update',
        request_serializer=protos_dot_data__pb2.Data.SerializeToString,
        response_deserializer=protos_dot_data__pb2.Data.FromString,
        )
    self.UpdateCalendar = channel.stream_unary(
        '/Controllable/UpdateCalendar',
        request_serializer=protos_dot_data__pb2.Data.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Stop = channel.unary_stream(
        '/Controllable/Stop',
        request_serializer=protos_dot_controller__pb2.StopParams.SerializeToString,
        response_deserializer=protos_dot_data__pb2.Data.FromString,
        )


class ControllableServicer(object):
  """TODO: State: bytes...

  A service to be controller by a controller service
  """

  def UpdateDataBundle(self, request_iterator, context):
    """the controller calls this method to send a data bundle to the controllable
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateParameters(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Initialize(self, request_iterator, context):
    """called to initialize the controllable
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request_iterator, context):
    """TODO: should return the state of the strategy run session at each update...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateCalendar(self, request_iterator, context):
    """receives periodic calendar updates
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Stop(self, request, context):
    """TODO: should return the state of the controllable after it stopped...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ControllableServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'UpdateDataBundle': grpc.stream_unary_rpc_method_handler(
          servicer.UpdateDataBundle,
          request_deserializer=protos_dot_data__pb2.Data.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'UpdateParameters': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateParameters,
          request_deserializer=protos_dot_controller__pb2.ParametersUpdateMessage.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Initialize': grpc.stream_unary_rpc_method_handler(
          servicer.Initialize,
          request_deserializer=protos_dot_data__pb2.Data.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Update': grpc.stream_stream_rpc_method_handler(
          servicer.Update,
          request_deserializer=protos_dot_data__pb2.Data.FromString,
          response_serializer=protos_dot_data__pb2.Data.SerializeToString,
      ),
      'UpdateCalendar': grpc.stream_unary_rpc_method_handler(
          servicer.UpdateCalendar,
          request_deserializer=protos_dot_data__pb2.Data.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Stop': grpc.unary_stream_rpc_method_handler(
          servicer.Stop,
          request_deserializer=protos_dot_controller__pb2.StopParams.FromString,
          response_serializer=protos_dot_data__pb2.Data.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Controllable', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

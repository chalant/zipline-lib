# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/controllable.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from protos import broker_pb2 as protos_dot_broker__pb2
from protos import controller_pb2 as protos_dot_controller__pb2
from protos import clock_pb2 as protos_dot_clock__pb2
from protos import data_pb2 as protos_dot_data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/controllable.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19protos/controllable.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x13protos/broker.proto\x1a\x17protos/controller.proto\x1a\x12protos/clock.proto\x1a\x11protos/data.proto\"\xf0\x01\n\nInitParams\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08strategy\x18\x02 \x01(\x0c\x12\x0f\n\x07\x63\x61pital\x18\x03 \x01(\x02\x12\x14\n\x0cmax_leverage\x18\x04 \x01(\x02\x12\x16\n\x0e\x64\x61ta_frequency\x18\x05 \x01(\t\x12\x10\n\x08universe\x18\x06 \x01(\t\x12\x11\n\tlook_back\x18\x07 \x01(\x05\x12)\n\x05start\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x03\x65nd\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04mode\x18\n \x01(\t\"}\n\rUpdateRequest\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x19\n\x05\x65vent\x18\x02 \x01(\x0e\x32\n.EventType\x12\"\n\x0c\x62roker_state\x18\x03 \x01(\x0b\x32\x0c.BrokerState\"\r\n\x0bUpdateReply\"\xaf\x02\n\x11\x43ontrollableState\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x15\n\rsession_state\x18\x02 \x01(\t\x12\x0f\n\x07\x63\x61pital\x18\x03 \x01(\t\x12\x10\n\x08universe\x18\x04 \x01(\t\x12\x11\n\tlook_back\x18\x05 \x01(\x05\x12\x16\n\x0e\x64\x61ta_frequency\x18\x06 \x01(\t\x12)\n\x05start\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x03\x65nd\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ncheckpoint\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1d\n\x15metrics_tracker_state\x18\n \x01(\x0c\x32\x99\x02\n\x0c\x43ontrollable\x12\x44\n\x10UpdateParameters\x12\x18.ParametersUpdateRequest\x1a\x16.google.protobuf.Empty\x12.\n\nInitialize\x12\x06.Chunk\x1a\x16.google.protobuf.Empty(\x01\x12\x32\n\x0b\x43lockUpdate\x12\x0b.ClockEvent\x1a\x16.google.protobuf.Empty\x12\x31\n\rUpdateAccount\x12\x06.Chunk\x1a\x16.google.protobuf.Empty(\x01\x12,\n\x04Stop\x12\x0c.StopRequest\x1a\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,protos_dot_broker__pb2.DESCRIPTOR,protos_dot_controller__pb2.DESCRIPTOR,protos_dot_clock__pb2.DESCRIPTOR,protos_dot_data__pb2.DESCRIPTOR,])




_INITPARAMS = _descriptor.Descriptor(
  name='InitParams',
  full_name='InitParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='InitParams.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strategy', full_name='InitParams.strategy', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capital', full_name='InitParams.capital', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_leverage', full_name='InitParams.max_leverage', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_frequency', full_name='InitParams.data_frequency', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='universe', full_name='InitParams.universe', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='look_back', full_name='InitParams.look_back', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='InitParams.start', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='InitParams.end', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='InitParams.mode', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=177,
  serialized_end=417,
)


_UPDATEREQUEST = _descriptor.Descriptor(
  name='UpdateRequest',
  full_name='UpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='UpdateRequest.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event', full_name='UpdateRequest.event', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='broker_state', full_name='UpdateRequest.broker_state', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=419,
  serialized_end=544,
)


_UPDATEREPLY = _descriptor.Descriptor(
  name='UpdateReply',
  full_name='UpdateReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=546,
  serialized_end=559,
)


_CONTROLLABLESTATE = _descriptor.Descriptor(
  name='ControllableState',
  full_name='ControllableState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='ControllableState.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_state', full_name='ControllableState.session_state', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capital', full_name='ControllableState.capital', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='universe', full_name='ControllableState.universe', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='look_back', full_name='ControllableState.look_back', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_frequency', full_name='ControllableState.data_frequency', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='ControllableState.start', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='ControllableState.end', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkpoint', full_name='ControllableState.checkpoint', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metrics_tracker_state', full_name='ControllableState.metrics_tracker_state', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=562,
  serialized_end=865,
)

_INITPARAMS.fields_by_name['start'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_INITPARAMS.fields_by_name['end'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_UPDATEREQUEST.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_UPDATEREQUEST.fields_by_name['event'].enum_type = protos_dot_clock__pb2._EVENTTYPE
_UPDATEREQUEST.fields_by_name['broker_state'].message_type = protos_dot_broker__pb2._BROKERSTATE
_CONTROLLABLESTATE.fields_by_name['start'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CONTROLLABLESTATE.fields_by_name['end'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CONTROLLABLESTATE.fields_by_name['checkpoint'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['InitParams'] = _INITPARAMS
DESCRIPTOR.message_types_by_name['UpdateRequest'] = _UPDATEREQUEST
DESCRIPTOR.message_types_by_name['UpdateReply'] = _UPDATEREPLY
DESCRIPTOR.message_types_by_name['ControllableState'] = _CONTROLLABLESTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InitParams = _reflection.GeneratedProtocolMessageType('InitParams', (_message.Message,), dict(
  DESCRIPTOR = _INITPARAMS,
  __module__ = 'protos.controllable_pb2'
  # @@protoc_insertion_point(class_scope:InitParams)
  ))
_sym_db.RegisterMessage(InitParams)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEREQUEST,
  __module__ = 'protos.controllable_pb2'
  # @@protoc_insertion_point(class_scope:UpdateRequest)
  ))
_sym_db.RegisterMessage(UpdateRequest)

UpdateReply = _reflection.GeneratedProtocolMessageType('UpdateReply', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEREPLY,
  __module__ = 'protos.controllable_pb2'
  # @@protoc_insertion_point(class_scope:UpdateReply)
  ))
_sym_db.RegisterMessage(UpdateReply)

ControllableState = _reflection.GeneratedProtocolMessageType('ControllableState', (_message.Message,), dict(
  DESCRIPTOR = _CONTROLLABLESTATE,
  __module__ = 'protos.controllable_pb2'
  # @@protoc_insertion_point(class_scope:ControllableState)
  ))
_sym_db.RegisterMessage(ControllableState)



_CONTROLLABLE = _descriptor.ServiceDescriptor(
  name='Controllable',
  full_name='Controllable',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=868,
  serialized_end=1149,
  methods=[
  _descriptor.MethodDescriptor(
    name='UpdateParameters',
    full_name='Controllable.UpdateParameters',
    index=0,
    containing_service=None,
    input_type=protos_dot_controller__pb2._PARAMETERSUPDATEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Initialize',
    full_name='Controllable.Initialize',
    index=1,
    containing_service=None,
    input_type=protos_dot_data__pb2._CHUNK,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ClockUpdate',
    full_name='Controllable.ClockUpdate',
    index=2,
    containing_service=None,
    input_type=protos_dot_clock__pb2._CLOCKEVENT,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateAccount',
    full_name='Controllable.UpdateAccount',
    index=3,
    containing_service=None,
    input_type=protos_dot_data__pb2._CHUNK,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Stop',
    full_name='Controllable.Stop',
    index=4,
    containing_service=None,
    input_type=protos_dot_controller__pb2._STOPREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTROLLABLE)

DESCRIPTOR.services_by_name['Controllable'] = _CONTROLLABLE

# @@protoc_insertion_point(module_scope)

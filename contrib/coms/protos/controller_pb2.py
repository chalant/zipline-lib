# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contrib/coms/protos/controller.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='contrib/coms/protos/controller.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n$contrib/coms/protos/controller.proto\"%\n\x08Identity\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\"2\n\rRegisterReply\"!\n\x06STATUS\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x32\x35\n\nController\x12\'\n\x08Register\x12\t.Identity\x1a\x0e.RegisterReply\"\x00\x62\x06proto3')
)



_REGISTERREPLY_STATUS = _descriptor.EnumDescriptor(
  name='STATUS',
  full_name='RegisterReply.STATUS',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=96,
  serialized_end=129,
)
_sym_db.RegisterEnumDescriptor(_REGISTERREPLY_STATUS)


_IDENTITY = _descriptor.Descriptor(
  name='Identity',
  full_name='Identity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Identity.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='Identity.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=40,
  serialized_end=77,
)


_REGISTERREPLY = _descriptor.Descriptor(
  name='RegisterReply',
  full_name='RegisterReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REGISTERREPLY_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=129,
)

_REGISTERREPLY_STATUS.containing_type = _REGISTERREPLY
DESCRIPTOR.message_types_by_name['Identity'] = _IDENTITY
DESCRIPTOR.message_types_by_name['RegisterReply'] = _REGISTERREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Identity = _reflection.GeneratedProtocolMessageType('Identity', (_message.Message,), dict(
  DESCRIPTOR = _IDENTITY,
  __module__ = 'contrib.coms.protos.controller_pb2'
  # @@protoc_insertion_point(class_scope:Identity)
  ))
_sym_db.RegisterMessage(Identity)

RegisterReply = _reflection.GeneratedProtocolMessageType('RegisterReply', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERREPLY,
  __module__ = 'contrib.coms.protos.controller_pb2'
  # @@protoc_insertion_point(class_scope:RegisterReply)
  ))
_sym_db.RegisterMessage(RegisterReply)



_CONTROLLER = _descriptor.ServiceDescriptor(
  name='Controller',
  full_name='Controller',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=131,
  serialized_end=184,
  methods=[
  _descriptor.MethodDescriptor(
    name='Register',
    full_name='Controller.Register',
    index=0,
    containing_service=None,
    input_type=_IDENTITY,
    output_type=_REGISTERREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTROLLER)

DESCRIPTOR.services_by_name['Controller'] = _CONTROLLER

# @@protoc_insertion_point(module_scope)
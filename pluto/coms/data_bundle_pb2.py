# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data_bundle.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='data_bundle.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11\x64\x61ta_bundle.proto\"0\n\x11\x43ompoundDomainDef\x12\x1b\n\x07\x64omains\x18\x01 \x03(\x0b\x32\n.DomainDef\"7\n\tDomainDef\x12\n\n\x02op\x18\x01 \x01(\t\x12\x1e\n\x06\x64omain\x18\x02 \x01(\x0b\x32\x0e.UnitDomainDef\"D\n\rUnitDomainDef\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nasset_type\x18\x02 \x01(\t\x12\x11\n\tdata_type\x18\x03 \x01(\t\"4\n\rAssetMetadata\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x15\n\rcalendar_name\x18\x02 \x01(\t\"\x10\n\x0e\x42undleMetadata\"\x16\n\x06\x42undle\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x62\x06proto3')
)




_COMPOUNDDOMAINDEF = _descriptor.Descriptor(
  name='CompoundDomainDef',
  full_name='CompoundDomainDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='domains', full_name='CompoundDomainDef.domains', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=21,
  serialized_end=69,
)


_DOMAINDEF = _descriptor.Descriptor(
  name='DomainDef',
  full_name='DomainDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='op', full_name='DomainDef.op', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='DomainDef.domain', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=71,
  serialized_end=126,
)


_UNITDOMAINDEF = _descriptor.Descriptor(
  name='UnitDomainDef',
  full_name='UnitDomainDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='UnitDomainDef.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset_type', full_name='UnitDomainDef.asset_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='UnitDomainDef.data_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=128,
  serialized_end=196,
)


_ASSETMETADATA = _descriptor.Descriptor(
  name='AssetMetadata',
  full_name='AssetMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='AssetMetadata.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='calendar_name', full_name='AssetMetadata.calendar_name', index=1,
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
  serialized_start=198,
  serialized_end=250,
)


_BUNDLEMETADATA = _descriptor.Descriptor(
  name='BundleMetadata',
  full_name='BundleMetadata',
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
  serialized_start=252,
  serialized_end=268,
)


_BUNDLE = _descriptor.Descriptor(
  name='Bundle',
  full_name='Bundle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='Bundle.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
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
  serialized_start=270,
  serialized_end=292,
)

_COMPOUNDDOMAINDEF.fields_by_name['domains'].message_type = _DOMAINDEF
_DOMAINDEF.fields_by_name['domain'].message_type = _UNITDOMAINDEF
DESCRIPTOR.message_types_by_name['CompoundDomainDef'] = _COMPOUNDDOMAINDEF
DESCRIPTOR.message_types_by_name['DomainDef'] = _DOMAINDEF
DESCRIPTOR.message_types_by_name['UnitDomainDef'] = _UNITDOMAINDEF
DESCRIPTOR.message_types_by_name['AssetMetadata'] = _ASSETMETADATA
DESCRIPTOR.message_types_by_name['BundleMetadata'] = _BUNDLEMETADATA
DESCRIPTOR.message_types_by_name['Bundle'] = _BUNDLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CompoundDomainDef = _reflection.GeneratedProtocolMessageType('CompoundDomainDef', (_message.Message,), dict(
  DESCRIPTOR = _COMPOUNDDOMAINDEF,
  __module__ = 'data_bundle_pb2'
  # @@protoc_insertion_point(class_scope:CompoundDomainDef)
  ))
_sym_db.RegisterMessage(CompoundDomainDef)

DomainDef = _reflection.GeneratedProtocolMessageType('DomainDef', (_message.Message,), dict(
  DESCRIPTOR = _DOMAINDEF,
  __module__ = 'data_bundle_pb2'
  # @@protoc_insertion_point(class_scope:DomainDef)
  ))
_sym_db.RegisterMessage(DomainDef)

UnitDomainDef = _reflection.GeneratedProtocolMessageType('UnitDomainDef', (_message.Message,), dict(
  DESCRIPTOR = _UNITDOMAINDEF,
  __module__ = 'data_bundle_pb2'
  # @@protoc_insertion_point(class_scope:UnitDomainDef)
  ))
_sym_db.RegisterMessage(UnitDomainDef)

AssetMetadata = _reflection.GeneratedProtocolMessageType('AssetMetadata', (_message.Message,), dict(
  DESCRIPTOR = _ASSETMETADATA,
  __module__ = 'data_bundle_pb2'
  # @@protoc_insertion_point(class_scope:AssetMetadata)
  ))
_sym_db.RegisterMessage(AssetMetadata)

BundleMetadata = _reflection.GeneratedProtocolMessageType('BundleMetadata', (_message.Message,), dict(
  DESCRIPTOR = _BUNDLEMETADATA,
  __module__ = 'data_bundle_pb2'
  # @@protoc_insertion_point(class_scope:BundleMetadata)
  ))
_sym_db.RegisterMessage(BundleMetadata)

Bundle = _reflection.GeneratedProtocolMessageType('Bundle', (_message.Message,), dict(
  DESCRIPTOR = _BUNDLE,
  __module__ = 'data_bundle_pb2'
  # @@protoc_insertion_point(class_scope:Bundle)
  ))
_sym_db.RegisterMessage(Bundle)


# @@protoc_insertion_point(module_scope)
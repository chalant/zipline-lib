# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/controller.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from protos import metrics_pb2 as protos_dot_metrics__pb2
from protos import clock_pb2 as protos_dot_clock__pb2
from protos import data_pb2 as protos_dot_data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/controller.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17protos/controller.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14protos/metrics.proto\x1a\x12protos/clock.proto\x1a\x11protos/data.proto\"0\n\x06Status\x12&\n\x0esession_status\x18\x01 \x01(\x0e\x32\x0e.SessionStatus\":\n\rCapitalUpdate\x12\x15\n\rcapital_ratio\x18\x01 \x01(\x02\x12\x12\n\nsession_id\x18\x02 \x01(\t\"=\n\x11MaxLeverageUpdate\x12\x14\n\x0cmax_leverage\x18\x01 \x01(\x02\x12\x12\n\nsession_id\x18\x02 \x01(\t\"I\n\x06LevCap\x12\x15\n\rcapital_ratio\x18\x01 \x01(\x02\x12\x14\n\x0cmax_leverage\x18\x02 \x01(\x02\x12\x12\n\nsession_id\x18\x03 \x01(\t\"\x19\n\x17\x43\x61pitalAssignmentStatus\"\x92\x01\n\x12\x44\x65limitedRunParams\x12\x1e\n\nrun_params\x18\x01 \x03(\x0b\x32\n.RunParams\x12.\n\nstart_date\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_date\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xac\x01\n\tRunParams\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x15\n\rcapital_ratio\x18\x02 \x01(\x02\x12\x14\n\x0cmax_leverage\x18\x03 \x01(\x02\x12!\n\remission_rate\x18\x04 \x01(\x0e\x32\n.Frequency\x12\x17\n\x0f\x62\x65nchmark_asset\x18\x05 \x01(\t\x12\"\n\x0e\x64\x61ta_frequency\x18\x06 \x01(\x0e\x32\n.Frequency\"\x1f\n\nStopParams\x12\x11\n\tliquidate\x18\x01 \x01(\x08\"\x0c\n\nStopStatus\"2\n\x0bPerformance\x12#\n\x07packets\x18\x01 \x03(\x0b\x32\x12.PerformancePacket\"\xd8\x01\n\x11PerformancePacket\x12+\n\x0f\x63umulative_perf\x18\x01 \x01(\x0b\x32\x12.CumulativeMetrics\x12&\n\ndaily_perf\x18\x02 \x01(\x0b\x32\x12.PeriodPerformance\x12)\n\rminutely_perf\x18\x03 \x01(\x0b\x32\x12.PeriodPerformance\x12\x37\n\x17\x63umulative_risk_metrics\x18\x04 \x01(\x0b\x32\x16.CumulativeRiskMetrics\x12\n\n\x02id\x18\x05 \x01(\t\"x\n\x11PeriodPerformance\x12.\n\x12\x63umulative_metrics\x18\x01 \x01(\x0b\x32\x12.CumulativeMetrics\x12\x33\n\x15period_common_metrics\x18\x02 \x01(\x0b\x32\x14.PeriodCommonMetrics\"p\n\x17ParametersUpdateRequest\x12*\n\x10\x63ontroller_event\x18\x01 \x01(\x0e\x32\x10.ControllerEvent\x12\x0f\n\x07\x63\x61pital\x18\x02 \x01(\x02\x12\x18\n\x10maximum_leverage\x18\x03 \x01(\x02*/\n\rSessionStatus\x12\r\n\tCOMPLETED\x10\x00\x12\x0f\n\x0bINTERRUPTED\x10\x01*M\n\x0f\x43ontrollerEvent\x12\x12\n\x0e\x43\x41PITAL_CHANGE\x10\x00\x12\x13\n\x0fLEVERAGE_CHANGE\x10\x01\x12\x11\n\rBROKER_UPDATE\x10\x02\x32\xeb\x02\n\nController\x12:\n\x17PerformancePacketUpdate\x12\x05.Data\x1a\x16.google.protobuf.Empty(\x01\x12 \n\x04Stop\x12\x0b.StopParams\x1a\x0b.StopStatus\x12;\n\tLiquidate\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12\x33\n\x0cUpdateLevCap\x12\x07.LevCap\x1a\x18.CapitalAssignmentStatus(\x01\x12\x32\n\x0b\x43lockUpdate\x12\x0b.ClockEvent\x1a\x16.google.protobuf.Empty\x12)\n\x06\x44\x65ploy\x12\x05.Data\x1a\x16.google.protobuf.Empty(\x01\x12.\n\x0bUpdateGraph\x12\x05.Data\x1a\x16.google.protobuf.Empty(\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,protos_dot_metrics__pb2.DESCRIPTOR,protos_dot_clock__pb2.DESCRIPTOR,protos_dot_data__pb2.DESCRIPTOR,])

_SESSIONSTATUS = _descriptor.EnumDescriptor(
  name='SessionStatus',
  full_name='SessionStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERRUPTED', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1303,
  serialized_end=1350,
)
_sym_db.RegisterEnumDescriptor(_SESSIONSTATUS)

SessionStatus = enum_type_wrapper.EnumTypeWrapper(_SESSIONSTATUS)
_CONTROLLEREVENT = _descriptor.EnumDescriptor(
  name='ControllerEvent',
  full_name='ControllerEvent',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CAPITAL_CHANGE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEVERAGE_CHANGE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BROKER_UPDATE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1352,
  serialized_end=1429,
)
_sym_db.RegisterEnumDescriptor(_CONTROLLEREVENT)

ControllerEvent = enum_type_wrapper.EnumTypeWrapper(_CONTROLLEREVENT)
COMPLETED = 0
INTERRUPTED = 1
CAPITAL_CHANGE = 0
LEVERAGE_CHANGE = 1
BROKER_UPDATE = 2



_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_status', full_name='Status.session_status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=150,
  serialized_end=198,
)


_CAPITALUPDATE = _descriptor.Descriptor(
  name='CapitalUpdate',
  full_name='CapitalUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='capital_ratio', full_name='CapitalUpdate.capital_ratio', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='CapitalUpdate.session_id', index=1,
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
  serialized_start=200,
  serialized_end=258,
)


_MAXLEVERAGEUPDATE = _descriptor.Descriptor(
  name='MaxLeverageUpdate',
  full_name='MaxLeverageUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_leverage', full_name='MaxLeverageUpdate.max_leverage', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='MaxLeverageUpdate.session_id', index=1,
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
  serialized_start=260,
  serialized_end=321,
)


_LEVCAP = _descriptor.Descriptor(
  name='LevCap',
  full_name='LevCap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='capital_ratio', full_name='LevCap.capital_ratio', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_leverage', full_name='LevCap.max_leverage', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='LevCap.session_id', index=2,
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
  serialized_start=323,
  serialized_end=396,
)


_CAPITALASSIGNMENTSTATUS = _descriptor.Descriptor(
  name='CapitalAssignmentStatus',
  full_name='CapitalAssignmentStatus',
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
  serialized_start=398,
  serialized_end=423,
)


_DELIMITEDRUNPARAMS = _descriptor.Descriptor(
  name='DelimitedRunParams',
  full_name='DelimitedRunParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='run_params', full_name='DelimitedRunParams.run_params', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='DelimitedRunParams.start_date', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_date', full_name='DelimitedRunParams.end_date', index=2,
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
  serialized_start=426,
  serialized_end=572,
)


_RUNPARAMS = _descriptor.Descriptor(
  name='RunParams',
  full_name='RunParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='RunParams.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capital_ratio', full_name='RunParams.capital_ratio', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_leverage', full_name='RunParams.max_leverage', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='emission_rate', full_name='RunParams.emission_rate', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='benchmark_asset', full_name='RunParams.benchmark_asset', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_frequency', full_name='RunParams.data_frequency', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=575,
  serialized_end=747,
)


_STOPPARAMS = _descriptor.Descriptor(
  name='StopParams',
  full_name='StopParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='liquidate', full_name='StopParams.liquidate', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=749,
  serialized_end=780,
)


_STOPSTATUS = _descriptor.Descriptor(
  name='StopStatus',
  full_name='StopStatus',
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
  serialized_start=782,
  serialized_end=794,
)


_PERFORMANCE = _descriptor.Descriptor(
  name='Performance',
  full_name='Performance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packets', full_name='Performance.packets', index=0,
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
  serialized_start=796,
  serialized_end=846,
)


_PERFORMANCEPACKET = _descriptor.Descriptor(
  name='PerformancePacket',
  full_name='PerformancePacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cumulative_perf', full_name='PerformancePacket.cumulative_perf', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='daily_perf', full_name='PerformancePacket.daily_perf', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minutely_perf', full_name='PerformancePacket.minutely_perf', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cumulative_risk_metrics', full_name='PerformancePacket.cumulative_risk_metrics', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='PerformancePacket.id', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=849,
  serialized_end=1065,
)


_PERIODPERFORMANCE = _descriptor.Descriptor(
  name='PeriodPerformance',
  full_name='PeriodPerformance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cumulative_metrics', full_name='PeriodPerformance.cumulative_metrics', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period_common_metrics', full_name='PeriodPerformance.period_common_metrics', index=1,
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
  serialized_start=1067,
  serialized_end=1187,
)


_PARAMETERSUPDATEREQUEST = _descriptor.Descriptor(
  name='ParametersUpdateRequest',
  full_name='ParametersUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='controller_event', full_name='ParametersUpdateRequest.controller_event', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capital', full_name='ParametersUpdateRequest.capital', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maximum_leverage', full_name='ParametersUpdateRequest.maximum_leverage', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=1189,
  serialized_end=1301,
)

_STATUS.fields_by_name['session_status'].enum_type = _SESSIONSTATUS
_DELIMITEDRUNPARAMS.fields_by_name['run_params'].message_type = _RUNPARAMS
_DELIMITEDRUNPARAMS.fields_by_name['start_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DELIMITEDRUNPARAMS.fields_by_name['end_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_RUNPARAMS.fields_by_name['emission_rate'].enum_type = protos_dot_clock__pb2._FREQUENCY
_RUNPARAMS.fields_by_name['data_frequency'].enum_type = protos_dot_clock__pb2._FREQUENCY
_PERFORMANCE.fields_by_name['packets'].message_type = _PERFORMANCEPACKET
_PERFORMANCEPACKET.fields_by_name['cumulative_perf'].message_type = protos_dot_metrics__pb2._CUMULATIVEMETRICS
_PERFORMANCEPACKET.fields_by_name['daily_perf'].message_type = _PERIODPERFORMANCE
_PERFORMANCEPACKET.fields_by_name['minutely_perf'].message_type = _PERIODPERFORMANCE
_PERFORMANCEPACKET.fields_by_name['cumulative_risk_metrics'].message_type = protos_dot_metrics__pb2._CUMULATIVERISKMETRICS
_PERIODPERFORMANCE.fields_by_name['cumulative_metrics'].message_type = protos_dot_metrics__pb2._CUMULATIVEMETRICS
_PERIODPERFORMANCE.fields_by_name['period_common_metrics'].message_type = protos_dot_metrics__pb2._PERIODCOMMONMETRICS
_PARAMETERSUPDATEREQUEST.fields_by_name['controller_event'].enum_type = _CONTROLLEREVENT
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['CapitalUpdate'] = _CAPITALUPDATE
DESCRIPTOR.message_types_by_name['MaxLeverageUpdate'] = _MAXLEVERAGEUPDATE
DESCRIPTOR.message_types_by_name['LevCap'] = _LEVCAP
DESCRIPTOR.message_types_by_name['CapitalAssignmentStatus'] = _CAPITALASSIGNMENTSTATUS
DESCRIPTOR.message_types_by_name['DelimitedRunParams'] = _DELIMITEDRUNPARAMS
DESCRIPTOR.message_types_by_name['RunParams'] = _RUNPARAMS
DESCRIPTOR.message_types_by_name['StopParams'] = _STOPPARAMS
DESCRIPTOR.message_types_by_name['StopStatus'] = _STOPSTATUS
DESCRIPTOR.message_types_by_name['Performance'] = _PERFORMANCE
DESCRIPTOR.message_types_by_name['PerformancePacket'] = _PERFORMANCEPACKET
DESCRIPTOR.message_types_by_name['PeriodPerformance'] = _PERIODPERFORMANCE
DESCRIPTOR.message_types_by_name['ParametersUpdateRequest'] = _PARAMETERSUPDATEREQUEST
DESCRIPTOR.enum_types_by_name['SessionStatus'] = _SESSIONSTATUS
DESCRIPTOR.enum_types_by_name['ControllerEvent'] = _CONTROLLEREVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), dict(
  DESCRIPTOR = _STATUS,
  __module__ = 'protos.controller_pb2'
  # @@protoc_insertion_point(class_scope:Status)
  ))
_sym_db.RegisterMessage(Status)

CapitalUpdate = _reflection.GeneratedProtocolMessageType('CapitalUpdate', (_message.Message,), dict(
  DESCRIPTOR = _CAPITALUPDATE,
  __module__ = 'protos.controller_pb2'
  # @@protoc_insertion_point(class_scope:CapitalUpdate)
  ))
_sym_db.RegisterMessage(CapitalUpdate)

MaxLeverageUpdate = _reflection.GeneratedProtocolMessageType('MaxLeverageUpdate', (_message.Message,), dict(
  DESCRIPTOR = _MAXLEVERAGEUPDATE,
  __module__ = 'protos.controller_pb2'
  # @@protoc_insertion_point(class_scope:MaxLeverageUpdate)
  ))
_sym_db.RegisterMessage(MaxLeverageUpdate)

LevCap = _reflection.GeneratedProtocolMessageType('LevCap', (_message.Message,), dict(
  DESCRIPTOR = _LEVCAP,
  __module__ = 'protos.controller_pb2'
  # @@protoc_insertion_point(class_scope:LevCap)
  ))
_sym_db.RegisterMessage(LevCap)

CapitalAssignmentStatus = _reflection.GeneratedProtocolMessageType('CapitalAssignmentStatus', (_message.Message,), dict(
  DESCRIPTOR = _CAPITALASSIGNMENTSTATUS,
  __module__ = 'protos.controller_pb2'
  # @@protoc_insertion_point(class_scope:CapitalAssignmentStatus)
  ))
_sym_db.RegisterMessage(CapitalAssignmentStatus)

DelimitedRunParams = _reflection.GeneratedProtocolMessageType('DelimitedRunParams', (_message.Message,), dict(
  DESCRIPTOR = _DELIMITEDRUNPARAMS,
  __module__ = 'protos.controller_pb2'
  # @@protoc_insertion_point(class_scope:DelimitedRunParams)
  ))
_sym_db.RegisterMessage(DelimitedRunParams)

RunParams = _reflection.GeneratedProtocolMessageType('RunParams', (_message.Message,), dict(
  DESCRIPTOR = _RUNPARAMS,
  __module__ = 'protos.controller_pb2'
  # @@protoc_insertion_point(class_scope:RunParams)
  ))
_sym_db.RegisterMessage(RunParams)

StopParams = _reflection.GeneratedProtocolMessageType('StopParams', (_message.Message,), dict(
  DESCRIPTOR = _STOPPARAMS,
  __module__ = 'protos.controller_pb2'
  # @@protoc_insertion_point(class_scope:StopParams)
  ))
_sym_db.RegisterMessage(StopParams)

StopStatus = _reflection.GeneratedProtocolMessageType('StopStatus', (_message.Message,), dict(
  DESCRIPTOR = _STOPSTATUS,
  __module__ = 'protos.controller_pb2'
  # @@protoc_insertion_point(class_scope:StopStatus)
  ))
_sym_db.RegisterMessage(StopStatus)

Performance = _reflection.GeneratedProtocolMessageType('Performance', (_message.Message,), dict(
  DESCRIPTOR = _PERFORMANCE,
  __module__ = 'protos.controller_pb2'
  # @@protoc_insertion_point(class_scope:Performance)
  ))
_sym_db.RegisterMessage(Performance)

PerformancePacket = _reflection.GeneratedProtocolMessageType('PerformancePacket', (_message.Message,), dict(
  DESCRIPTOR = _PERFORMANCEPACKET,
  __module__ = 'protos.controller_pb2'
  # @@protoc_insertion_point(class_scope:PerformancePacket)
  ))
_sym_db.RegisterMessage(PerformancePacket)

PeriodPerformance = _reflection.GeneratedProtocolMessageType('PeriodPerformance', (_message.Message,), dict(
  DESCRIPTOR = _PERIODPERFORMANCE,
  __module__ = 'protos.controller_pb2'
  # @@protoc_insertion_point(class_scope:PeriodPerformance)
  ))
_sym_db.RegisterMessage(PeriodPerformance)

ParametersUpdateRequest = _reflection.GeneratedProtocolMessageType('ParametersUpdateRequest', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERSUPDATEREQUEST,
  __module__ = 'protos.controller_pb2'
  # @@protoc_insertion_point(class_scope:ParametersUpdateRequest)
  ))
_sym_db.RegisterMessage(ParametersUpdateRequest)



_CONTROLLER = _descriptor.ServiceDescriptor(
  name='Controller',
  full_name='Controller',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1432,
  serialized_end=1795,
  methods=[
  _descriptor.MethodDescriptor(
    name='PerformancePacketUpdate',
    full_name='Controller.PerformancePacketUpdate',
    index=0,
    containing_service=None,
    input_type=protos_dot_data__pb2._DATA,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Stop',
    full_name='Controller.Stop',
    index=1,
    containing_service=None,
    input_type=_STOPPARAMS,
    output_type=_STOPSTATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Liquidate',
    full_name='Controller.Liquidate',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateLevCap',
    full_name='Controller.UpdateLevCap',
    index=3,
    containing_service=None,
    input_type=_LEVCAP,
    output_type=_CAPITALASSIGNMENTSTATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ClockUpdate',
    full_name='Controller.ClockUpdate',
    index=4,
    containing_service=None,
    input_type=protos_dot_clock__pb2._CLOCKEVENT,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Deploy',
    full_name='Controller.Deploy',
    index=5,
    containing_service=None,
    input_type=protos_dot_data__pb2._DATA,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateGraph',
    full_name='Controller.UpdateGraph',
    index=6,
    containing_service=None,
    input_type=protos_dot_data__pb2._DATA,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTROLLER)

DESCRIPTOR.services_by_name['Controller'] = _CONTROLLER

# @@protoc_insertion_point(module_scope)
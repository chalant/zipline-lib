# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contrib/control/controller.proto

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
from contrib.coms.protos import metrics_pb2 as contrib_dot_coms_dot_protos_dot_metrics__pb2
from contrib.coms.protos import data_bundle_pb2 as contrib_dot_coms_dot_protos_dot_data__bundle__pb2
from contrib.control import clock_pb2 as contrib_dot_control_dot_clock__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='contrib/control/controller.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n contrib/control/controller.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a!contrib/coms/protos/metrics.proto\x1a%contrib/coms/protos/data_bundle.proto\x1a\x1b\x63ontrib/control/clock.proto\";\n\x18InitializationParameters\x12\x10\n\x08strategy\x18\x01 \x01(\x0c\x12\r\n\x05state\x18\x02 \x01(\x0c\"\x1d\n\x0cSessionState\x12\r\n\x05state\x18\x01 \x01(\x0c\"$\n\x10\x44\x65ploymentStatus\x12\x10\n\x08strategy\x18\x01 \x01(\x0c\"1\n\x06Status\x12\x1b\n\x06status\x18\x01 \x01(\x0e\x32\x0b.StatusEnum\x12\n\n\x02id\x18\x02 \x01(\t\";\n\x06LevCap\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x63\x61pital\x18\x02 \x01(\x02\x12\x14\n\x0cmax_leverage\x18\x03 \x01(\x02\"\x19\n\x17\x43\x61pitalAssignmentStatus\"\"\n\x0b\x45nvironment\x12\x13\n\x0b\x65nvironment\x18\x01 \x01(\x0c\"\x1a\n\x08Strategy\x12\x0e\n\x06script\x18\x01 \x01(\x0c\"%\n\x06\x46ilter\x12\x1b\n\x06status\x18\x01 \x01(\x0e\x32\x0b.StatusEnum\"\x9e\x01\n\tRunParams\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x63\x61pital\x18\x02 \x01(\x03\x12\x14\n\x0cmax_leverage\x18\x03 \x01(\x02\x12!\n\remission_rate\x18\x04 \x01(\x0e\x32\n.Frequency\x12\x17\n\x0f\x62\x65nchmark_asset\x18\x05 \x01(\t\x12\"\n\x0e\x64\x61ta_frequency\x18\x06 \x01(\x0e\x32\n.Frequency\"+\n\nStopParams\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tliquidate\x18\x02 \x01(\x08\"\x0c\n\nStopStatus\"\x10\n\x02ID\x12\n\n\x02id\x18\x01 \x01(\t\"\xcc\x01\n\x11PerformancePacket\x12+\n\x0f\x63umulative_perf\x18\x01 \x01(\x0b\x32\x12.CumulativeMetrics\x12&\n\ndaily_perf\x18\x02 \x01(\x0b\x32\x12.PeriodPerformance\x12)\n\rminutely_perf\x18\x03 \x01(\x0b\x32\x12.PeriodPerformance\x12\x37\n\x17\x63umulative_risk_metrics\x18\x04 \x01(\x0b\x32\x16.CumulativeRiskMetrics\"x\n\x11PeriodPerformance\x12.\n\x12\x63umulative_metrics\x18\x01 \x01(\x0b\x32\x12.CumulativeMetrics\x12\x33\n\x15period_common_metrics\x18\x02 \x01(\x0b\x32\x14.PeriodCommonMetrics\"p\n\x17ParametersUpdateMessage\x12*\n\x10\x63ontroller_event\x18\x01 \x01(\x0e\x32\x10.ControllerEvent\x12\x0f\n\x07\x63\x61pital\x18\x02 \x01(\x02\x12\x18\n\x10maximum_leverage\x18\x03 \x01(\x02*&\n\nStatusEnum\x12\x0b\n\x07Running\x10\x00\x12\x0b\n\x07Pending\x10\x01*M\n\x0f\x43ontrollerEvent\x12\x12\n\x0e\x43\x41PITAL_CHANGE\x10\x00\x12\x13\n\x0fLEVERAGE_CHANGE\x10\x01\x12\x11\n\rBROKER_UPDATE\x10\x02\x32\x89\x03\n\nController\x12*\n\x06\x44\x65ploy\x12\t.Strategy\x1a\x11.DeploymentStatus(\x01\x30\x01\x12\x45\n\x17PerformancePacketUpdate\x12\x12.PerformancePacket\x1a\x16.google.protobuf.Empty\x12 \n\x04Stop\x12\x0b.StopParams\x1a\x0b.StopStatus\x12\x1a\n\x03Run\x12\n.RunParams\x1a\x07.Status\x12\"\n\x05Watch\x12\x03.ID\x1a\x12.PerformancePacket0\x01\x12\x1f\n\x0bGetStrategy\x12\x03.ID\x1a\t.Strategy0\x01\x12)\n\x0eGetEnvironment\x12\x07.Domain\x1a\x0c.Environment0\x01\x12\'\n\x0fGetStrategyList\x12\x07.Filter\x1a\t.Strategy0\x01\x12\x31\n\x0cUpdateLevCap\x12\x07.LevCap\x1a\x18.CapitalAssignmentStatusb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,contrib_dot_coms_dot_protos_dot_metrics__pb2.DESCRIPTOR,contrib_dot_coms_dot_protos_dot_data__bundle__pb2.DESCRIPTOR,contrib_dot_control_dot_clock__pb2.DESCRIPTOR,])

_STATUSENUM = _descriptor.EnumDescriptor(
  name='StatusEnum',
  full_name='StatusEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Running', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Pending', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1221,
  serialized_end=1259,
)
_sym_db.RegisterEnumDescriptor(_STATUSENUM)

StatusEnum = enum_type_wrapper.EnumTypeWrapper(_STATUSENUM)
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
  serialized_start=1261,
  serialized_end=1338,
)
_sym_db.RegisterEnumDescriptor(_CONTROLLEREVENT)

ControllerEvent = enum_type_wrapper.EnumTypeWrapper(_CONTROLLEREVENT)
Running = 0
Pending = 1
CAPITAL_CHANGE = 0
LEVERAGE_CHANGE = 1
BROKER_UPDATE = 2



_INITIALIZATIONPARAMETERS = _descriptor.Descriptor(
  name='InitializationParameters',
  full_name='InitializationParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='strategy', full_name='InitializationParameters.strategy', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='InitializationParameters.state', index=1,
      number=2, type=12, cpp_type=9, label=1,
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
  serialized_start=168,
  serialized_end=227,
)


_SESSIONSTATE = _descriptor.Descriptor(
  name='SessionState',
  full_name='SessionState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='SessionState.state', index=0,
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
  serialized_start=229,
  serialized_end=258,
)


_DEPLOYMENTSTATUS = _descriptor.Descriptor(
  name='DeploymentStatus',
  full_name='DeploymentStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='strategy', full_name='DeploymentStatus.strategy', index=0,
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
  serialized_start=260,
  serialized_end=296,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='Status.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='Status.id', index=1,
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
  serialized_start=298,
  serialized_end=347,
)


_LEVCAP = _descriptor.Descriptor(
  name='LevCap',
  full_name='LevCap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='LevCap.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capital', full_name='LevCap.capital', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_leverage', full_name='LevCap.max_leverage', index=2,
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
  serialized_start=349,
  serialized_end=408,
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
  serialized_start=410,
  serialized_end=435,
)


_ENVIRONMENT = _descriptor.Descriptor(
  name='Environment',
  full_name='Environment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='environment', full_name='Environment.environment', index=0,
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
  serialized_start=437,
  serialized_end=471,
)


_STRATEGY = _descriptor.Descriptor(
  name='Strategy',
  full_name='Strategy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='script', full_name='Strategy.script', index=0,
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
  serialized_start=473,
  serialized_end=499,
)


_FILTER = _descriptor.Descriptor(
  name='Filter',
  full_name='Filter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='Filter.status', index=0,
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
  serialized_start=501,
  serialized_end=538,
)


_RUNPARAMS = _descriptor.Descriptor(
  name='RunParams',
  full_name='RunParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='RunParams.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capital', full_name='RunParams.capital', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=541,
  serialized_end=699,
)


_STOPPARAMS = _descriptor.Descriptor(
  name='StopParams',
  full_name='StopParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='StopParams.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='liquidate', full_name='StopParams.liquidate', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=701,
  serialized_end=744,
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
  serialized_start=746,
  serialized_end=758,
)


_ID = _descriptor.Descriptor(
  name='ID',
  full_name='ID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ID.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=760,
  serialized_end=776,
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
  serialized_start=779,
  serialized_end=983,
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
  serialized_start=985,
  serialized_end=1105,
)


_PARAMETERSUPDATEMESSAGE = _descriptor.Descriptor(
  name='ParametersUpdateMessage',
  full_name='ParametersUpdateMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='controller_event', full_name='ParametersUpdateMessage.controller_event', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capital', full_name='ParametersUpdateMessage.capital', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maximum_leverage', full_name='ParametersUpdateMessage.maximum_leverage', index=2,
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
  serialized_start=1107,
  serialized_end=1219,
)

_STATUS.fields_by_name['status'].enum_type = _STATUSENUM
_FILTER.fields_by_name['status'].enum_type = _STATUSENUM
_RUNPARAMS.fields_by_name['emission_rate'].enum_type = contrib_dot_control_dot_clock__pb2._FREQUENCY
_RUNPARAMS.fields_by_name['data_frequency'].enum_type = contrib_dot_control_dot_clock__pb2._FREQUENCY
_PERFORMANCEPACKET.fields_by_name['cumulative_perf'].message_type = contrib_dot_coms_dot_protos_dot_metrics__pb2._CUMULATIVEMETRICS
_PERFORMANCEPACKET.fields_by_name['daily_perf'].message_type = _PERIODPERFORMANCE
_PERFORMANCEPACKET.fields_by_name['minutely_perf'].message_type = _PERIODPERFORMANCE
_PERFORMANCEPACKET.fields_by_name['cumulative_risk_metrics'].message_type = contrib_dot_coms_dot_protos_dot_metrics__pb2._CUMULATIVERISKMETRICS
_PERIODPERFORMANCE.fields_by_name['cumulative_metrics'].message_type = contrib_dot_coms_dot_protos_dot_metrics__pb2._CUMULATIVEMETRICS
_PERIODPERFORMANCE.fields_by_name['period_common_metrics'].message_type = contrib_dot_coms_dot_protos_dot_metrics__pb2._PERIODCOMMONMETRICS
_PARAMETERSUPDATEMESSAGE.fields_by_name['controller_event'].enum_type = _CONTROLLEREVENT
DESCRIPTOR.message_types_by_name['InitializationParameters'] = _INITIALIZATIONPARAMETERS
DESCRIPTOR.message_types_by_name['SessionState'] = _SESSIONSTATE
DESCRIPTOR.message_types_by_name['DeploymentStatus'] = _DEPLOYMENTSTATUS
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['LevCap'] = _LEVCAP
DESCRIPTOR.message_types_by_name['CapitalAssignmentStatus'] = _CAPITALASSIGNMENTSTATUS
DESCRIPTOR.message_types_by_name['Environment'] = _ENVIRONMENT
DESCRIPTOR.message_types_by_name['Strategy'] = _STRATEGY
DESCRIPTOR.message_types_by_name['Filter'] = _FILTER
DESCRIPTOR.message_types_by_name['RunParams'] = _RUNPARAMS
DESCRIPTOR.message_types_by_name['StopParams'] = _STOPPARAMS
DESCRIPTOR.message_types_by_name['StopStatus'] = _STOPSTATUS
DESCRIPTOR.message_types_by_name['ID'] = _ID
DESCRIPTOR.message_types_by_name['PerformancePacket'] = _PERFORMANCEPACKET
DESCRIPTOR.message_types_by_name['PeriodPerformance'] = _PERIODPERFORMANCE
DESCRIPTOR.message_types_by_name['ParametersUpdateMessage'] = _PARAMETERSUPDATEMESSAGE
DESCRIPTOR.enum_types_by_name['StatusEnum'] = _STATUSENUM
DESCRIPTOR.enum_types_by_name['ControllerEvent'] = _CONTROLLEREVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InitializationParameters = _reflection.GeneratedProtocolMessageType('InitializationParameters', (_message.Message,), dict(
  DESCRIPTOR = _INITIALIZATIONPARAMETERS,
  __module__ = 'contrib.control.controller_pb2'
  # @@protoc_insertion_point(class_scope:InitializationParameters)
  ))
_sym_db.RegisterMessage(InitializationParameters)

SessionState = _reflection.GeneratedProtocolMessageType('SessionState', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONSTATE,
  __module__ = 'contrib.control.controller_pb2'
  # @@protoc_insertion_point(class_scope:SessionState)
  ))
_sym_db.RegisterMessage(SessionState)

DeploymentStatus = _reflection.GeneratedProtocolMessageType('DeploymentStatus', (_message.Message,), dict(
  DESCRIPTOR = _DEPLOYMENTSTATUS,
  __module__ = 'contrib.control.controller_pb2'
  # @@protoc_insertion_point(class_scope:DeploymentStatus)
  ))
_sym_db.RegisterMessage(DeploymentStatus)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), dict(
  DESCRIPTOR = _STATUS,
  __module__ = 'contrib.control.controller_pb2'
  # @@protoc_insertion_point(class_scope:Status)
  ))
_sym_db.RegisterMessage(Status)

LevCap = _reflection.GeneratedProtocolMessageType('LevCap', (_message.Message,), dict(
  DESCRIPTOR = _LEVCAP,
  __module__ = 'contrib.control.controller_pb2'
  # @@protoc_insertion_point(class_scope:LevCap)
  ))
_sym_db.RegisterMessage(LevCap)

CapitalAssignmentStatus = _reflection.GeneratedProtocolMessageType('CapitalAssignmentStatus', (_message.Message,), dict(
  DESCRIPTOR = _CAPITALASSIGNMENTSTATUS,
  __module__ = 'contrib.control.controller_pb2'
  # @@protoc_insertion_point(class_scope:CapitalAssignmentStatus)
  ))
_sym_db.RegisterMessage(CapitalAssignmentStatus)

Environment = _reflection.GeneratedProtocolMessageType('Environment', (_message.Message,), dict(
  DESCRIPTOR = _ENVIRONMENT,
  __module__ = 'contrib.control.controller_pb2'
  # @@protoc_insertion_point(class_scope:Environment)
  ))
_sym_db.RegisterMessage(Environment)

Strategy = _reflection.GeneratedProtocolMessageType('Strategy', (_message.Message,), dict(
  DESCRIPTOR = _STRATEGY,
  __module__ = 'contrib.control.controller_pb2'
  # @@protoc_insertion_point(class_scope:Strategy)
  ))
_sym_db.RegisterMessage(Strategy)

Filter = _reflection.GeneratedProtocolMessageType('Filter', (_message.Message,), dict(
  DESCRIPTOR = _FILTER,
  __module__ = 'contrib.control.controller_pb2'
  # @@protoc_insertion_point(class_scope:Filter)
  ))
_sym_db.RegisterMessage(Filter)

RunParams = _reflection.GeneratedProtocolMessageType('RunParams', (_message.Message,), dict(
  DESCRIPTOR = _RUNPARAMS,
  __module__ = 'contrib.control.controller_pb2'
  # @@protoc_insertion_point(class_scope:RunParams)
  ))
_sym_db.RegisterMessage(RunParams)

StopParams = _reflection.GeneratedProtocolMessageType('StopParams', (_message.Message,), dict(
  DESCRIPTOR = _STOPPARAMS,
  __module__ = 'contrib.control.controller_pb2'
  # @@protoc_insertion_point(class_scope:StopParams)
  ))
_sym_db.RegisterMessage(StopParams)

StopStatus = _reflection.GeneratedProtocolMessageType('StopStatus', (_message.Message,), dict(
  DESCRIPTOR = _STOPSTATUS,
  __module__ = 'contrib.control.controller_pb2'
  # @@protoc_insertion_point(class_scope:StopStatus)
  ))
_sym_db.RegisterMessage(StopStatus)

ID = _reflection.GeneratedProtocolMessageType('ID', (_message.Message,), dict(
  DESCRIPTOR = _ID,
  __module__ = 'contrib.control.controller_pb2'
  # @@protoc_insertion_point(class_scope:ID)
  ))
_sym_db.RegisterMessage(ID)

PerformancePacket = _reflection.GeneratedProtocolMessageType('PerformancePacket', (_message.Message,), dict(
  DESCRIPTOR = _PERFORMANCEPACKET,
  __module__ = 'contrib.control.controller_pb2'
  # @@protoc_insertion_point(class_scope:PerformancePacket)
  ))
_sym_db.RegisterMessage(PerformancePacket)

PeriodPerformance = _reflection.GeneratedProtocolMessageType('PeriodPerformance', (_message.Message,), dict(
  DESCRIPTOR = _PERIODPERFORMANCE,
  __module__ = 'contrib.control.controller_pb2'
  # @@protoc_insertion_point(class_scope:PeriodPerformance)
  ))
_sym_db.RegisterMessage(PeriodPerformance)

ParametersUpdateMessage = _reflection.GeneratedProtocolMessageType('ParametersUpdateMessage', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERSUPDATEMESSAGE,
  __module__ = 'contrib.control.controller_pb2'
  # @@protoc_insertion_point(class_scope:ParametersUpdateMessage)
  ))
_sym_db.RegisterMessage(ParametersUpdateMessage)



_CONTROLLER = _descriptor.ServiceDescriptor(
  name='Controller',
  full_name='Controller',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1341,
  serialized_end=1734,
  methods=[
  _descriptor.MethodDescriptor(
    name='Deploy',
    full_name='Controller.Deploy',
    index=0,
    containing_service=None,
    input_type=_STRATEGY,
    output_type=_DEPLOYMENTSTATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PerformancePacketUpdate',
    full_name='Controller.PerformancePacketUpdate',
    index=1,
    containing_service=None,
    input_type=_PERFORMANCEPACKET,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Stop',
    full_name='Controller.Stop',
    index=2,
    containing_service=None,
    input_type=_STOPPARAMS,
    output_type=_STOPSTATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Run',
    full_name='Controller.Run',
    index=3,
    containing_service=None,
    input_type=_RUNPARAMS,
    output_type=_STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Watch',
    full_name='Controller.Watch',
    index=4,
    containing_service=None,
    input_type=_ID,
    output_type=_PERFORMANCEPACKET,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetStrategy',
    full_name='Controller.GetStrategy',
    index=5,
    containing_service=None,
    input_type=_ID,
    output_type=_STRATEGY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetEnvironment',
    full_name='Controller.GetEnvironment',
    index=6,
    containing_service=None,
    input_type=contrib_dot_coms_dot_protos_dot_data__bundle__pb2._DOMAIN,
    output_type=_ENVIRONMENT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetStrategyList',
    full_name='Controller.GetStrategyList',
    index=7,
    containing_service=None,
    input_type=_FILTER,
    output_type=_STRATEGY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateLevCap',
    full_name='Controller.UpdateLevCap',
    index=8,
    containing_service=None,
    input_type=_LEVCAP,
    output_type=_CAPITALASSIGNMENTSTATUS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTROLLER)

DESCRIPTOR.services_by_name['Controller'] = _CONTROLLER

# @@protoc_insertion_point(module_scope)

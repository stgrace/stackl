# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agent.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='agent.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0b\x61gent.proto\"\xa1\x01\n\nInvocation\x12\r\n\x05image\x18\x01 \x01(\t\x12\x1d\n\x15infrastructure_target\x18\x02 \x01(\t\x12\x16\n\x0estack_instance\x18\x03 \x01(\t\x12\x0f\n\x07service\x18\x04 \x01(\t\x12\x1e\n\x16\x66unctional_requirement\x18\x05 \x01(\t\x12\x0c\n\x04tool\x18\x06 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x07 \x01(\t\"#\n\x10\x43onnectionResult\x12\x0f\n\x07success\x18\x01 \x01(\x08\"/\n\rAgentMetadata\x12\x10\n\x08selector\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x8b\x01\n\x10\x41utomationResult\x12\x16\n\x0estack_instance\x18\x01 \x01(\t\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x1e\n\x16\x66unctional_requirement\x18\x03 \x01(\t\x12\x17\n\x06status\x18\x04 \x01(\x0e\x32\x07.Status\x12\x15\n\rerror_message\x18\x05 \x01(\t*\x1f\n\x06Status\x12\t\n\x05READY\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x32\xa4\x01\n\x0bStacklAgent\x12\x34\n\rRegisterAgent\x12\x0e.AgentMetadata\x1a\x11.ConnectionResult\"\x00\x12)\n\x06GetJob\x12\x0e.AgentMetadata\x1a\x0b.Invocation\"\x00\x30\x01\x12\x34\n\x0cReportResult\x12\x11.AutomationResult\x1a\x11.ConnectionResultb\x06proto3')
)

_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='READY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=407,
  serialized_end=438,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
READY = 0
FAILED = 1



_INVOCATION = _descriptor.Descriptor(
  name='Invocation',
  full_name='Invocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='Invocation.image', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='infrastructure_target', full_name='Invocation.infrastructure_target', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stack_instance', full_name='Invocation.stack_instance', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service', full_name='Invocation.service', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='functional_requirement', full_name='Invocation.functional_requirement', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tool', full_name='Invocation.tool', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='Invocation.action', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=16,
  serialized_end=177,
)


_CONNECTIONRESULT = _descriptor.Descriptor(
  name='ConnectionResult',
  full_name='ConnectionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='ConnectionResult.success', index=0,
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
  serialized_start=179,
  serialized_end=214,
)


_AGENTMETADATA = _descriptor.Descriptor(
  name='AgentMetadata',
  full_name='AgentMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='selector', full_name='AgentMetadata.selector', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='AgentMetadata.name', index=1,
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
  serialized_start=216,
  serialized_end=263,
)


_AUTOMATIONRESULT = _descriptor.Descriptor(
  name='AutomationResult',
  full_name='AutomationResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stack_instance', full_name='AutomationResult.stack_instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service', full_name='AutomationResult.service', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='functional_requirement', full_name='AutomationResult.functional_requirement', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='AutomationResult.status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='AutomationResult.error_message', index=4,
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
  serialized_start=266,
  serialized_end=405,
)

_AUTOMATIONRESULT.fields_by_name['status'].enum_type = _STATUS
DESCRIPTOR.message_types_by_name['Invocation'] = _INVOCATION
DESCRIPTOR.message_types_by_name['ConnectionResult'] = _CONNECTIONRESULT
DESCRIPTOR.message_types_by_name['AgentMetadata'] = _AGENTMETADATA
DESCRIPTOR.message_types_by_name['AutomationResult'] = _AUTOMATIONRESULT
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Invocation = _reflection.GeneratedProtocolMessageType('Invocation', (_message.Message,), {
  'DESCRIPTOR' : _INVOCATION,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:Invocation)
  })
_sym_db.RegisterMessage(Invocation)

ConnectionResult = _reflection.GeneratedProtocolMessageType('ConnectionResult', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONRESULT,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:ConnectionResult)
  })
_sym_db.RegisterMessage(ConnectionResult)

AgentMetadata = _reflection.GeneratedProtocolMessageType('AgentMetadata', (_message.Message,), {
  'DESCRIPTOR' : _AGENTMETADATA,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:AgentMetadata)
  })
_sym_db.RegisterMessage(AgentMetadata)

AutomationResult = _reflection.GeneratedProtocolMessageType('AutomationResult', (_message.Message,), {
  'DESCRIPTOR' : _AUTOMATIONRESULT,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:AutomationResult)
  })
_sym_db.RegisterMessage(AutomationResult)



_STACKLAGENT = _descriptor.ServiceDescriptor(
  name='StacklAgent',
  full_name='StacklAgent',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=441,
  serialized_end=605,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterAgent',
    full_name='StacklAgent.RegisterAgent',
    index=0,
    containing_service=None,
    input_type=_AGENTMETADATA,
    output_type=_CONNECTIONRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetJob',
    full_name='StacklAgent.GetJob',
    index=1,
    containing_service=None,
    input_type=_AGENTMETADATA,
    output_type=_INVOCATION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReportResult',
    full_name='StacklAgent.ReportResult',
    index=2,
    containing_service=None,
    input_type=_AUTOMATIONRESULT,
    output_type=_CONNECTIONRESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STACKLAGENT)

DESCRIPTOR.services_by_name['StacklAgent'] = _STACKLAGENT

# @@protoc_insertion_point(module_scope)

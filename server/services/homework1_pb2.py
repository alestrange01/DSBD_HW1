# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/homework1.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'services/homework1.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18services/homework1.proto\x12\thomework1\"\r\n\x0bNoneRequest\"A\n\x0fRegisterRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05share\x18\x03 \x01(\t\"/\n\x0cLoginRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"-\n\rUpdateRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\r\n\x05share\x18\x02 \x01(\t\"\x1e\n\rDeleteRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"\x18\n\x0bMeanRequest\x12\t\n\x01n\x18\x01 \x01(\t\"=\n\x05Reply\x12\x12\n\nstatusCode\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t2\xa6\x03\n\rServerService\x12:\n\x08Register\x12\x1a.homework1.RegisterRequest\x1a\x10.homework1.Reply\"\x00\x12\x34\n\x05Login\x12\x17.homework1.LoginRequest\x1a\x10.homework1.Reply\"\x00\x12\x36\n\x06Update\x12\x18.homework1.UpdateRequest\x1a\x10.homework1.Reply\"\x00\x12\x36\n\x06\x44\x65lete\x12\x18.homework1.DeleteRequest\x1a\x10.homework1.Reply\"\x00\x12;\n\rGetValueShare\x12\x16.homework1.NoneRequest\x1a\x10.homework1.Reply\"\x00\x12:\n\x0cGetMeanShare\x12\x16.homework1.MeanRequest\x1a\x10.homework1.Reply\"\x00\x12:\n\x0cViewAllUsers\x12\x16.homework1.NoneRequest\x1a\x10.homework1.Reply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.homework1_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_NONEREQUEST']._serialized_start=39
  _globals['_NONEREQUEST']._serialized_end=52
  _globals['_REGISTERREQUEST']._serialized_start=54
  _globals['_REGISTERREQUEST']._serialized_end=119
  _globals['_LOGINREQUEST']._serialized_start=121
  _globals['_LOGINREQUEST']._serialized_end=168
  _globals['_UPDATEREQUEST']._serialized_start=170
  _globals['_UPDATEREQUEST']._serialized_end=215
  _globals['_DELETEREQUEST']._serialized_start=217
  _globals['_DELETEREQUEST']._serialized_end=247
  _globals['_MEANREQUEST']._serialized_start=249
  _globals['_MEANREQUEST']._serialized_end=273
  _globals['_REPLY']._serialized_start=275
  _globals['_REPLY']._serialized_end=336
  _globals['_SERVERSERVICE']._serialized_start=339
  _globals['_SERVERSERVICE']._serialized_end=761
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: param_server/param_server.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fparam_server/param_server.proto\x12\x17mavsdk.rpc.param_server\x1a\x14mavsdk_options.proto\"9\n\x17RetrieveParamIntRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"r\n\x18RetrieveParamIntResponse\x12G\n\x13param_server_result\x18\x01 \x01(\x0b\x32*.mavsdk.rpc.param_server.ParamServerResult\x12\r\n\x05value\x18\x02 \x01(\x05\"G\n\x16ProvideParamIntRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x05\"b\n\x17ProvideParamIntResponse\x12G\n\x13param_server_result\x18\x01 \x01(\x0b\x32*.mavsdk.rpc.param_server.ParamServerResult\";\n\x19RetrieveParamFloatRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"t\n\x1aRetrieveParamFloatResponse\x12G\n\x13param_server_result\x18\x01 \x01(\x0b\x32*.mavsdk.rpc.param_server.ParamServerResult\x12\r\n\x05value\x18\x02 \x01(\x02\"I\n\x18ProvideParamFloatRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x02\"d\n\x19ProvideParamFloatResponse\x12G\n\x13param_server_result\x18\x01 \x01(\x0b\x32*.mavsdk.rpc.param_server.ParamServerResult\"<\n\x1aRetrieveParamCustomRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"u\n\x1bRetrieveParamCustomResponse\x12G\n\x13param_server_result\x18\x01 \x01(\x0b\x32*.mavsdk.rpc.param_server.ParamServerResult\x12\r\n\x05value\x18\x02 \x01(\t\"J\n\x19ProvideParamCustomRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"e\n\x1aProvideParamCustomResponse\x12G\n\x13param_server_result\x18\x01 \x01(\x0b\x32*.mavsdk.rpc.param_server.ParamServerResult\",\n\x18RetrieveAllParamsRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"O\n\x19RetrieveAllParamsResponse\x12\x32\n\x06params\x18\x01 \x01(\x0b\x32\".mavsdk.rpc.param_server.AllParams\"\'\n\x08IntParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05\")\n\nFloatParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\"*\n\x0b\x43ustomParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xba\x01\n\tAllParams\x12\x35\n\nint_params\x18\x01 \x03(\x0b\x32!.mavsdk.rpc.param_server.IntParam\x12\x39\n\x0c\x66loat_params\x18\x02 \x03(\x0b\x32#.mavsdk.rpc.param_server.FloatParam\x12;\n\rcustom_params\x18\x03 \x03(\x0b\x32$.mavsdk.rpc.param_server.CustomParam\"\xa1\x02\n\x11ParamServerResult\x12\x41\n\x06result\x18\x01 \x01(\x0e\x32\x31.mavsdk.rpc.param_server.ParamServerResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\xb4\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NOT_FOUND\x10\x02\x12\x15\n\x11RESULT_WRONG_TYPE\x10\x03\x12\x1e\n\x1aRESULT_PARAM_NAME_TOO_LONG\x10\x04\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x05\x12\x1f\n\x1bRESULT_PARAM_VALUE_TOO_LONG\x10\x06\x32\xaa\x07\n\x12ParamServerService\x12}\n\x10RetrieveParamInt\x12\x30.mavsdk.rpc.param_server.RetrieveParamIntRequest\x1a\x31.mavsdk.rpc.param_server.RetrieveParamIntResponse\"\x04\x80\xb5\x18\x01\x12z\n\x0fProvideParamInt\x12/.mavsdk.rpc.param_server.ProvideParamIntRequest\x1a\x30.mavsdk.rpc.param_server.ProvideParamIntResponse\"\x04\x80\xb5\x18\x01\x12\x83\x01\n\x12RetrieveParamFloat\x12\x32.mavsdk.rpc.param_server.RetrieveParamFloatRequest\x1a\x33.mavsdk.rpc.param_server.RetrieveParamFloatResponse\"\x04\x80\xb5\x18\x01\x12\x80\x01\n\x11ProvideParamFloat\x12\x31.mavsdk.rpc.param_server.ProvideParamFloatRequest\x1a\x32.mavsdk.rpc.param_server.ProvideParamFloatResponse\"\x04\x80\xb5\x18\x01\x12\x86\x01\n\x13RetrieveParamCustom\x12\x33.mavsdk.rpc.param_server.RetrieveParamCustomRequest\x1a\x34.mavsdk.rpc.param_server.RetrieveParamCustomResponse\"\x04\x80\xb5\x18\x01\x12\x83\x01\n\x12ProvideParamCustom\x12\x32.mavsdk.rpc.param_server.ProvideParamCustomRequest\x1a\x33.mavsdk.rpc.param_server.ProvideParamCustomResponse\"\x04\x80\xb5\x18\x01\x12\x80\x01\n\x11RetrieveAllParams\x12\x31.mavsdk.rpc.param_server.RetrieveAllParamsRequest\x1a\x32.mavsdk.rpc.param_server.RetrieveAllParamsResponse\"\x04\x80\xb5\x18\x01\x42*\n\x16io.mavsdk.param_serverB\x10ParamServerProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'param_server.param_server_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026io.mavsdk.param_serverB\020ParamServerProto'
  _PARAMSERVERSERVICE.methods_by_name['RetrieveParamInt']._options = None
  _PARAMSERVERSERVICE.methods_by_name['RetrieveParamInt']._serialized_options = b'\200\265\030\001'
  _PARAMSERVERSERVICE.methods_by_name['ProvideParamInt']._options = None
  _PARAMSERVERSERVICE.methods_by_name['ProvideParamInt']._serialized_options = b'\200\265\030\001'
  _PARAMSERVERSERVICE.methods_by_name['RetrieveParamFloat']._options = None
  _PARAMSERVERSERVICE.methods_by_name['RetrieveParamFloat']._serialized_options = b'\200\265\030\001'
  _PARAMSERVERSERVICE.methods_by_name['ProvideParamFloat']._options = None
  _PARAMSERVERSERVICE.methods_by_name['ProvideParamFloat']._serialized_options = b'\200\265\030\001'
  _PARAMSERVERSERVICE.methods_by_name['RetrieveParamCustom']._options = None
  _PARAMSERVERSERVICE.methods_by_name['RetrieveParamCustom']._serialized_options = b'\200\265\030\001'
  _PARAMSERVERSERVICE.methods_by_name['ProvideParamCustom']._options = None
  _PARAMSERVERSERVICE.methods_by_name['ProvideParamCustom']._serialized_options = b'\200\265\030\001'
  _PARAMSERVERSERVICE.methods_by_name['RetrieveAllParams']._options = None
  _PARAMSERVERSERVICE.methods_by_name['RetrieveAllParams']._serialized_options = b'\200\265\030\001'
  _globals['_RETRIEVEPARAMINTREQUEST']._serialized_start=82
  _globals['_RETRIEVEPARAMINTREQUEST']._serialized_end=139
  _globals['_RETRIEVEPARAMINTRESPONSE']._serialized_start=141
  _globals['_RETRIEVEPARAMINTRESPONSE']._serialized_end=255
  _globals['_PROVIDEPARAMINTREQUEST']._serialized_start=257
  _globals['_PROVIDEPARAMINTREQUEST']._serialized_end=328
  _globals['_PROVIDEPARAMINTRESPONSE']._serialized_start=330
  _globals['_PROVIDEPARAMINTRESPONSE']._serialized_end=428
  _globals['_RETRIEVEPARAMFLOATREQUEST']._serialized_start=430
  _globals['_RETRIEVEPARAMFLOATREQUEST']._serialized_end=489
  _globals['_RETRIEVEPARAMFLOATRESPONSE']._serialized_start=491
  _globals['_RETRIEVEPARAMFLOATRESPONSE']._serialized_end=607
  _globals['_PROVIDEPARAMFLOATREQUEST']._serialized_start=609
  _globals['_PROVIDEPARAMFLOATREQUEST']._serialized_end=682
  _globals['_PROVIDEPARAMFLOATRESPONSE']._serialized_start=684
  _globals['_PROVIDEPARAMFLOATRESPONSE']._serialized_end=784
  _globals['_RETRIEVEPARAMCUSTOMREQUEST']._serialized_start=786
  _globals['_RETRIEVEPARAMCUSTOMREQUEST']._serialized_end=846
  _globals['_RETRIEVEPARAMCUSTOMRESPONSE']._serialized_start=848
  _globals['_RETRIEVEPARAMCUSTOMRESPONSE']._serialized_end=965
  _globals['_PROVIDEPARAMCUSTOMREQUEST']._serialized_start=967
  _globals['_PROVIDEPARAMCUSTOMREQUEST']._serialized_end=1041
  _globals['_PROVIDEPARAMCUSTOMRESPONSE']._serialized_start=1043
  _globals['_PROVIDEPARAMCUSTOMRESPONSE']._serialized_end=1144
  _globals['_RETRIEVEALLPARAMSREQUEST']._serialized_start=1146
  _globals['_RETRIEVEALLPARAMSREQUEST']._serialized_end=1190
  _globals['_RETRIEVEALLPARAMSRESPONSE']._serialized_start=1192
  _globals['_RETRIEVEALLPARAMSRESPONSE']._serialized_end=1271
  _globals['_INTPARAM']._serialized_start=1273
  _globals['_INTPARAM']._serialized_end=1312
  _globals['_FLOATPARAM']._serialized_start=1314
  _globals['_FLOATPARAM']._serialized_end=1355
  _globals['_CUSTOMPARAM']._serialized_start=1357
  _globals['_CUSTOMPARAM']._serialized_end=1399
  _globals['_ALLPARAMS']._serialized_start=1402
  _globals['_ALLPARAMS']._serialized_end=1588
  _globals['_PARAMSERVERRESULT']._serialized_start=1591
  _globals['_PARAMSERVERRESULT']._serialized_end=1880
  _globals['_PARAMSERVERRESULT_RESULT']._serialized_start=1700
  _globals['_PARAMSERVERRESULT_RESULT']._serialized_end=1880
  _globals['_PARAMSERVERSERVICE']._serialized_start=1883
  _globals['_PARAMSERVERSERVICE']._serialized_end=2821
# @@protoc_insertion_point(module_scope)

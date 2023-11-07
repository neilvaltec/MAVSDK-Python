# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: component_information/component_information.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1component_information/component_information.proto\x12 mavsdk.rpc.component_information\x1a\x14mavsdk_options.proto\"\xc7\x01\n\nFloatParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x11short_description\x18\x02 \x01(\t\x12\x18\n\x10long_description\x18\x03 \x01(\t\x12\x0c\n\x04unit\x18\x04 \x01(\t\x12\x16\n\x0e\x64\x65\x63imal_places\x18\x05 \x01(\x05\x12\x13\n\x0bstart_value\x18\x06 \x01(\x02\x12\x15\n\rdefault_value\x18\x07 \x01(\x02\x12\x11\n\tmin_value\x18\x08 \x01(\x02\x12\x11\n\tmax_value\x18\t \x01(\x02\",\n\x18\x41\x63\x63\x65ssFloatParamsRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"\xbd\x01\n\x19\x41\x63\x63\x65ssFloatParamsResponse\x12\x62\n\x1c\x63omponent_information_result\x18\x01 \x01(\x0b\x32<.mavsdk.rpc.component_information.ComponentInformationResult\x12<\n\x06params\x18\x02 \x03(\x0b\x32,.mavsdk.rpc.component_information.FloatParam\"/\n\x10\x46loatParamUpdate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\".\n\x1aSubscribeFloatParamRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"^\n\x12\x46loatParamResponse\x12H\n\x0cparam_update\x18\x01 \x01(\x0b\x32\x32.mavsdk.rpc.component_information.FloatParamUpdate\"\xcd\x01\n\x1a\x43omponentInformationResult\x12S\n\x06result\x18\x01 \x01(\x0e\x32\x43.mavsdk.rpc.component_information.ComponentInformationResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"F\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x03\x32\xc6\x02\n\x1b\x43omponentInformationService\x12\x92\x01\n\x11\x41\x63\x63\x65ssFloatParams\x12:.mavsdk.rpc.component_information.AccessFloatParamsRequest\x1a;.mavsdk.rpc.component_information.AccessFloatParamsResponse\"\x04\x80\xb5\x18\x01\x12\x91\x01\n\x13SubscribeFloatParam\x12<.mavsdk.rpc.component_information.SubscribeFloatParamRequest\x1a\x34.mavsdk.rpc.component_information.FloatParamResponse\"\x04\x80\xb5\x18\x00\x30\x01\x42<\n\x1fio.mavsdk.component_informationB\x19\x43omponentInformationProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component_information.component_information_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037io.mavsdk.component_informationB\031ComponentInformationProto'
  _COMPONENTINFORMATIONSERVICE.methods_by_name['AccessFloatParams']._options = None
  _COMPONENTINFORMATIONSERVICE.methods_by_name['AccessFloatParams']._serialized_options = b'\200\265\030\001'
  _COMPONENTINFORMATIONSERVICE.methods_by_name['SubscribeFloatParam']._options = None
  _COMPONENTINFORMATIONSERVICE.methods_by_name['SubscribeFloatParam']._serialized_options = b'\200\265\030\000'
  _globals['_FLOATPARAM']._serialized_start=110
  _globals['_FLOATPARAM']._serialized_end=309
  _globals['_ACCESSFLOATPARAMSREQUEST']._serialized_start=311
  _globals['_ACCESSFLOATPARAMSREQUEST']._serialized_end=355
  _globals['_ACCESSFLOATPARAMSRESPONSE']._serialized_start=358
  _globals['_ACCESSFLOATPARAMSRESPONSE']._serialized_end=547
  _globals['_FLOATPARAMUPDATE']._serialized_start=549
  _globals['_FLOATPARAMUPDATE']._serialized_end=596
  _globals['_SUBSCRIBEFLOATPARAMREQUEST']._serialized_start=598
  _globals['_SUBSCRIBEFLOATPARAMREQUEST']._serialized_end=644
  _globals['_FLOATPARAMRESPONSE']._serialized_start=646
  _globals['_FLOATPARAMRESPONSE']._serialized_end=740
  _globals['_COMPONENTINFORMATIONRESULT']._serialized_start=743
  _globals['_COMPONENTINFORMATIONRESULT']._serialized_end=948
  _globals['_COMPONENTINFORMATIONRESULT_RESULT']._serialized_start=878
  _globals['_COMPONENTINFORMATIONRESULT_RESULT']._serialized_end=948
  _globals['_COMPONENTINFORMATIONSERVICE']._serialized_start=951
  _globals['_COMPONENTINFORMATIONSERVICE']._serialized_end=1277
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transponder/transponder.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dtransponder/transponder.proto\x12\x16mavsdk.rpc.transponder\"/\n\x1bSubscribeTransponderRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"O\n\x13TransponderResponse\x12\x38\n\x0btransponder\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.transponder.AdsbVehicle\">\n\x19SetRateTransponderRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12\x0f\n\x07rate_hz\x18\x02 \x01(\x01\"c\n\x1aSetRateTransponderResponse\x12\x45\n\x12transponder_result\x18\x01 \x01(\x0b\x32).mavsdk.rpc.transponder.TransponderResult\"\xb3\x02\n\x0b\x41\x64sbVehicle\x12\x14\n\x0cicao_address\x18\x01 \x01(\r\x12\x14\n\x0clatitude_deg\x18\x02 \x01(\x01\x12\x15\n\rlongitude_deg\x18\x03 \x01(\x01\x12\x1b\n\x13\x61\x62solute_altitude_m\x18\x05 \x01(\x02\x12\x13\n\x0bheading_deg\x18\x06 \x01(\x02\x12\x1f\n\x17horizontal_velocity_m_s\x18\x07 \x01(\x02\x12\x1d\n\x15vertical_velocity_m_s\x18\x08 \x01(\x02\x12\x10\n\x08\x63\x61llsign\x18\t \x01(\t\x12=\n\x0c\x65mitter_type\x18\n \x01(\x0e\x32\'.mavsdk.rpc.transponder.AdsbEmitterType\x12\x0e\n\x06squawk\x18\r \x01(\r\x12\x0e\n\x06tslc_s\x18\x0e \x01(\r\"\x8f\x02\n\x11TransponderResult\x12@\n\x06result\x18\x01 \x01(\x0e\x32\x30.mavsdk.rpc.transponder.TransponderResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\xa3\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x02\x12\x1b\n\x17RESULT_CONNECTION_ERROR\x10\x03\x12\x0f\n\x0bRESULT_BUSY\x10\x04\x12\x19\n\x15RESULT_COMMAND_DENIED\x10\x05\x12\x12\n\x0eRESULT_TIMEOUT\x10\x06*\xad\x05\n\x0f\x41\x64sbEmitterType\x12\x1d\n\x19\x41\x44SB_EMITTER_TYPE_NO_INFO\x10\x00\x12\x1b\n\x17\x41\x44SB_EMITTER_TYPE_LIGHT\x10\x01\x12\x1b\n\x17\x41\x44SB_EMITTER_TYPE_SMALL\x10\x02\x12\x1b\n\x17\x41\x44SB_EMITTER_TYPE_LARGE\x10\x03\x12\'\n#ADSB_EMITTER_TYPE_HIGH_VORTEX_LARGE\x10\x04\x12\x1b\n\x17\x41\x44SB_EMITTER_TYPE_HEAVY\x10\x05\x12\"\n\x1e\x41\x44SB_EMITTER_TYPE_HIGHLY_MANUV\x10\x06\x12\x1f\n\x1b\x41\x44SB_EMITTER_TYPE_ROTOCRAFT\x10\x07\x12 \n\x1c\x41\x44SB_EMITTER_TYPE_UNASSIGNED\x10\x08\x12\x1c\n\x18\x41\x44SB_EMITTER_TYPE_GLIDER\x10\t\x12!\n\x1d\x41\x44SB_EMITTER_TYPE_LIGHTER_AIR\x10\n\x12\x1f\n\x1b\x41\x44SB_EMITTER_TYPE_PARACHUTE\x10\x0b\x12!\n\x1d\x41\x44SB_EMITTER_TYPE_ULTRA_LIGHT\x10\x0c\x12!\n\x1d\x41\x44SB_EMITTER_TYPE_UNASSIGNED2\x10\r\x12\x19\n\x15\x41\x44SB_EMITTER_TYPE_UAV\x10\x0e\x12\x1b\n\x17\x41\x44SB_EMITTER_TYPE_SPACE\x10\x0f\x12!\n\x1d\x41\x44SB_EMITTER_TYPE_UNASSGINED3\x10\x10\x12\'\n#ADSB_EMITTER_TYPE_EMERGENCY_SURFACE\x10\x11\x12%\n!ADSB_EMITTER_TYPE_SERVICE_SURFACE\x10\x12\x12$\n ADSB_EMITTER_TYPE_POINT_OBSTACLE\x10\x13\x32\x91\x02\n\x12TransponderService\x12|\n\x14SubscribeTransponder\x12\x33.mavsdk.rpc.transponder.SubscribeTransponderRequest\x1a+.mavsdk.rpc.transponder.TransponderResponse\"\x00\x30\x01\x12}\n\x12SetRateTransponder\x12\x31.mavsdk.rpc.transponder.SetRateTransponderRequest\x1a\x32.mavsdk.rpc.transponder.SetRateTransponderResponse\"\x00\x42)\n\x15io.mavsdk.transponderB\x10TransponderProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transponder.transponder_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025io.mavsdk.transponderB\020TransponderProto'
  _globals['_ADSBEMITTERTYPE']._serialized_start=937
  _globals['_ADSBEMITTERTYPE']._serialized_end=1622
  _globals['_SUBSCRIBETRANSPONDERREQUEST']._serialized_start=57
  _globals['_SUBSCRIBETRANSPONDERREQUEST']._serialized_end=104
  _globals['_TRANSPONDERRESPONSE']._serialized_start=106
  _globals['_TRANSPONDERRESPONSE']._serialized_end=185
  _globals['_SETRATETRANSPONDERREQUEST']._serialized_start=187
  _globals['_SETRATETRANSPONDERREQUEST']._serialized_end=249
  _globals['_SETRATETRANSPONDERRESPONSE']._serialized_start=251
  _globals['_SETRATETRANSPONDERRESPONSE']._serialized_end=350
  _globals['_ADSBVEHICLE']._serialized_start=353
  _globals['_ADSBVEHICLE']._serialized_end=660
  _globals['_TRANSPONDERRESULT']._serialized_start=663
  _globals['_TRANSPONDERRESULT']._serialized_end=934
  _globals['_TRANSPONDERRESULT_RESULT']._serialized_start=771
  _globals['_TRANSPONDERRESULT_RESULT']._serialized_end=934
  _globals['_TRANSPONDERSERVICE']._serialized_start=1625
  _globals['_TRANSPONDERSERVICE']._serialized_end=1898
# @@protoc_insertion_point(module_scope)

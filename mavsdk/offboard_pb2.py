# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: offboard/offboard.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17offboard/offboard.proto\x12\x13mavsdk.rpc.offboard\x1a\x14mavsdk_options.proto\" \n\x0cStartRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"M\n\rStartResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"\x1f\n\x0bStopRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"L\n\x0cStopResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"#\n\x0fIsActiveRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"%\n\x10IsActiveResponse\x12\x11\n\tis_active\x18\x01 \x01(\x08\"W\n\x12SetAttitudeRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12/\n\x08\x61ttitude\x18\x02 \x01(\x0b\x32\x1d.mavsdk.rpc.offboard.Attitude\"S\n\x13SetAttitudeResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"m\n\x19SetActuatorControlRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12>\n\x10\x61\x63tuator_control\x18\x02 \x01(\x0b\x32$.mavsdk.rpc.offboard.ActuatorControl\"Z\n\x1aSetActuatorControlResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"d\n\x16SetAttitudeRateRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12\x38\n\rattitude_rate\x18\x02 \x01(\x0b\x32!.mavsdk.rpc.offboard.AttitudeRate\"W\n\x17SetAttitudeRateResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"h\n\x15SetPositionNedRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12=\n\x10position_ned_yaw\x18\x02 \x01(\x0b\x32#.mavsdk.rpc.offboard.PositionNedYaw\"V\n\x16SetPositionNedResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"q\n\x18SetPositionGlobalRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12\x43\n\x13position_global_yaw\x18\x02 \x01(\x0b\x32&.mavsdk.rpc.offboard.PositionGlobalYaw\"Y\n\x19SetPositionGlobalResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"u\n\x16SetVelocityBodyRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12I\n\x16velocity_body_yawspeed\x18\x02 \x01(\x0b\x32).mavsdk.rpc.offboard.VelocityBodyYawspeed\"W\n\x17SetVelocityBodyResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"h\n\x15SetVelocityNedRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12=\n\x10velocity_ned_yaw\x18\x02 \x01(\x0b\x32#.mavsdk.rpc.offboard.VelocityNedYaw\"V\n\x16SetVelocityNedResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"\xaf\x01\n\x1dSetPositionVelocityNedRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12=\n\x10position_ned_yaw\x18\x02 \x01(\x0b\x32#.mavsdk.rpc.offboard.PositionNedYaw\x12=\n\x10velocity_ned_yaw\x18\x03 \x01(\x0b\x32#.mavsdk.rpc.offboard.VelocityNedYaw\"^\n\x1eSetPositionVelocityNedResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"m\n\x19SetAccelerationNedRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12>\n\x10\x61\x63\x63\x65leration_ned\x18\x02 \x01(\x0b\x32$.mavsdk.rpc.offboard.AccelerationNed\"Z\n\x1aSetAccelerationNedResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"V\n\x08\x41ttitude\x12\x10\n\x08roll_deg\x18\x01 \x01(\x02\x12\x11\n\tpitch_deg\x18\x02 \x01(\x02\x12\x0f\n\x07yaw_deg\x18\x03 \x01(\x02\x12\x14\n\x0cthrust_value\x18\x04 \x01(\x02\"(\n\x14\x41\x63tuatorControlGroup\x12\x10\n\x08\x63ontrols\x18\x01 \x03(\x02\"L\n\x0f\x41\x63tuatorControl\x12\x39\n\x06groups\x18\x01 \x03(\x0b\x32).mavsdk.rpc.offboard.ActuatorControlGroup\"`\n\x0c\x41ttitudeRate\x12\x12\n\nroll_deg_s\x18\x01 \x01(\x02\x12\x13\n\x0bpitch_deg_s\x18\x02 \x01(\x02\x12\x11\n\tyaw_deg_s\x18\x03 \x01(\x02\x12\x14\n\x0cthrust_value\x18\x04 \x01(\x02\"R\n\x0ePositionNedYaw\x12\x0f\n\x07north_m\x18\x01 \x01(\x02\x12\x0e\n\x06\x65\x61st_m\x18\x02 \x01(\x02\x12\x0e\n\x06\x64own_m\x18\x03 \x01(\x02\x12\x0f\n\x07yaw_deg\x18\x04 \x01(\x02\"\xfc\x01\n\x11PositionGlobalYaw\x12\x0f\n\x07lat_deg\x18\x01 \x01(\x01\x12\x0f\n\x07lon_deg\x18\x02 \x01(\x01\x12\r\n\x05\x61lt_m\x18\x03 \x01(\x02\x12\x0f\n\x07yaw_deg\x18\x04 \x01(\x02\x12J\n\raltitude_type\x18\x05 \x01(\x0e\x32\x33.mavsdk.rpc.offboard.PositionGlobalYaw.AltitudeType\"Y\n\x0c\x41ltitudeType\x12\x1a\n\x16\x41LTITUDE_TYPE_REL_HOME\x10\x00\x12\x16\n\x12\x41LTITUDE_TYPE_AMSL\x10\x01\x12\x15\n\x11\x41LTITUDE_TYPE_AGL\x10\x02\"h\n\x14VelocityBodyYawspeed\x12\x13\n\x0b\x66orward_m_s\x18\x01 \x01(\x02\x12\x11\n\tright_m_s\x18\x02 \x01(\x02\x12\x10\n\x08\x64own_m_s\x18\x03 \x01(\x02\x12\x16\n\x0eyawspeed_deg_s\x18\x04 \x01(\x02\"X\n\x0eVelocityNedYaw\x12\x11\n\tnorth_m_s\x18\x01 \x01(\x02\x12\x10\n\x08\x65\x61st_m_s\x18\x02 \x01(\x02\x12\x10\n\x08\x64own_m_s\x18\x03 \x01(\x02\x12\x0f\n\x07yaw_deg\x18\x04 \x01(\x02\"K\n\x0f\x41\x63\x63\x65lerationNed\x12\x12\n\nnorth_m_s2\x18\x01 \x01(\x02\x12\x11\n\teast_m_s2\x18\x02 \x01(\x02\x12\x11\n\tdown_m_s2\x18\x03 \x01(\x02\"\xa2\x02\n\x0eOffboardResult\x12:\n\x06result\x18\x01 \x01(\x0e\x32*.mavsdk.rpc.offboard.OffboardResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\xbf\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x02\x12\x1b\n\x17RESULT_CONNECTION_ERROR\x10\x03\x12\x0f\n\x0bRESULT_BUSY\x10\x04\x12\x19\n\x15RESULT_COMMAND_DENIED\x10\x05\x12\x12\n\x0eRESULT_TIMEOUT\x10\x06\x12\x1a\n\x16RESULT_NO_SETPOINT_SET\x10\x07\x32\xc1\n\n\x0fOffboardService\x12P\n\x05Start\x12!.mavsdk.rpc.offboard.StartRequest\x1a\".mavsdk.rpc.offboard.StartResponse\"\x00\x12M\n\x04Stop\x12 .mavsdk.rpc.offboard.StopRequest\x1a!.mavsdk.rpc.offboard.StopResponse\"\x00\x12]\n\x08IsActive\x12$.mavsdk.rpc.offboard.IsActiveRequest\x1a%.mavsdk.rpc.offboard.IsActiveResponse\"\x04\x80\xb5\x18\x01\x12\x66\n\x0bSetAttitude\x12\'.mavsdk.rpc.offboard.SetAttitudeRequest\x1a(.mavsdk.rpc.offboard.SetAttitudeResponse\"\x04\x80\xb5\x18\x01\x12{\n\x12SetActuatorControl\x12..mavsdk.rpc.offboard.SetActuatorControlRequest\x1a/.mavsdk.rpc.offboard.SetActuatorControlResponse\"\x04\x80\xb5\x18\x01\x12r\n\x0fSetAttitudeRate\x12+.mavsdk.rpc.offboard.SetAttitudeRateRequest\x1a,.mavsdk.rpc.offboard.SetAttitudeRateResponse\"\x04\x80\xb5\x18\x01\x12o\n\x0eSetPositionNed\x12*.mavsdk.rpc.offboard.SetPositionNedRequest\x1a+.mavsdk.rpc.offboard.SetPositionNedResponse\"\x04\x80\xb5\x18\x01\x12x\n\x11SetPositionGlobal\x12-.mavsdk.rpc.offboard.SetPositionGlobalRequest\x1a..mavsdk.rpc.offboard.SetPositionGlobalResponse\"\x04\x80\xb5\x18\x01\x12r\n\x0fSetVelocityBody\x12+.mavsdk.rpc.offboard.SetVelocityBodyRequest\x1a,.mavsdk.rpc.offboard.SetVelocityBodyResponse\"\x04\x80\xb5\x18\x01\x12o\n\x0eSetVelocityNed\x12*.mavsdk.rpc.offboard.SetVelocityNedRequest\x1a+.mavsdk.rpc.offboard.SetVelocityNedResponse\"\x04\x80\xb5\x18\x01\x12\x87\x01\n\x16SetPositionVelocityNed\x12\x32.mavsdk.rpc.offboard.SetPositionVelocityNedRequest\x1a\x33.mavsdk.rpc.offboard.SetPositionVelocityNedResponse\"\x04\x80\xb5\x18\x01\x12{\n\x12SetAccelerationNed\x12..mavsdk.rpc.offboard.SetAccelerationNedRequest\x1a/.mavsdk.rpc.offboard.SetAccelerationNedResponse\"\x04\x80\xb5\x18\x01\x42#\n\x12io.mavsdk.offboardB\rOffboardProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'offboard.offboard_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022io.mavsdk.offboardB\rOffboardProto'
  _OFFBOARDSERVICE.methods_by_name['IsActive']._options = None
  _OFFBOARDSERVICE.methods_by_name['IsActive']._serialized_options = b'\200\265\030\001'
  _OFFBOARDSERVICE.methods_by_name['SetAttitude']._options = None
  _OFFBOARDSERVICE.methods_by_name['SetAttitude']._serialized_options = b'\200\265\030\001'
  _OFFBOARDSERVICE.methods_by_name['SetActuatorControl']._options = None
  _OFFBOARDSERVICE.methods_by_name['SetActuatorControl']._serialized_options = b'\200\265\030\001'
  _OFFBOARDSERVICE.methods_by_name['SetAttitudeRate']._options = None
  _OFFBOARDSERVICE.methods_by_name['SetAttitudeRate']._serialized_options = b'\200\265\030\001'
  _OFFBOARDSERVICE.methods_by_name['SetPositionNed']._options = None
  _OFFBOARDSERVICE.methods_by_name['SetPositionNed']._serialized_options = b'\200\265\030\001'
  _OFFBOARDSERVICE.methods_by_name['SetPositionGlobal']._options = None
  _OFFBOARDSERVICE.methods_by_name['SetPositionGlobal']._serialized_options = b'\200\265\030\001'
  _OFFBOARDSERVICE.methods_by_name['SetVelocityBody']._options = None
  _OFFBOARDSERVICE.methods_by_name['SetVelocityBody']._serialized_options = b'\200\265\030\001'
  _OFFBOARDSERVICE.methods_by_name['SetVelocityNed']._options = None
  _OFFBOARDSERVICE.methods_by_name['SetVelocityNed']._serialized_options = b'\200\265\030\001'
  _OFFBOARDSERVICE.methods_by_name['SetPositionVelocityNed']._options = None
  _OFFBOARDSERVICE.methods_by_name['SetPositionVelocityNed']._serialized_options = b'\200\265\030\001'
  _OFFBOARDSERVICE.methods_by_name['SetAccelerationNed']._options = None
  _OFFBOARDSERVICE.methods_by_name['SetAccelerationNed']._serialized_options = b'\200\265\030\001'
  _globals['_STARTREQUEST']._serialized_start=70
  _globals['_STARTREQUEST']._serialized_end=102
  _globals['_STARTRESPONSE']._serialized_start=104
  _globals['_STARTRESPONSE']._serialized_end=181
  _globals['_STOPREQUEST']._serialized_start=183
  _globals['_STOPREQUEST']._serialized_end=214
  _globals['_STOPRESPONSE']._serialized_start=216
  _globals['_STOPRESPONSE']._serialized_end=292
  _globals['_ISACTIVEREQUEST']._serialized_start=294
  _globals['_ISACTIVEREQUEST']._serialized_end=329
  _globals['_ISACTIVERESPONSE']._serialized_start=331
  _globals['_ISACTIVERESPONSE']._serialized_end=368
  _globals['_SETATTITUDEREQUEST']._serialized_start=370
  _globals['_SETATTITUDEREQUEST']._serialized_end=457
  _globals['_SETATTITUDERESPONSE']._serialized_start=459
  _globals['_SETATTITUDERESPONSE']._serialized_end=542
  _globals['_SETACTUATORCONTROLREQUEST']._serialized_start=544
  _globals['_SETACTUATORCONTROLREQUEST']._serialized_end=653
  _globals['_SETACTUATORCONTROLRESPONSE']._serialized_start=655
  _globals['_SETACTUATORCONTROLRESPONSE']._serialized_end=745
  _globals['_SETATTITUDERATEREQUEST']._serialized_start=747
  _globals['_SETATTITUDERATEREQUEST']._serialized_end=847
  _globals['_SETATTITUDERATERESPONSE']._serialized_start=849
  _globals['_SETATTITUDERATERESPONSE']._serialized_end=936
  _globals['_SETPOSITIONNEDREQUEST']._serialized_start=938
  _globals['_SETPOSITIONNEDREQUEST']._serialized_end=1042
  _globals['_SETPOSITIONNEDRESPONSE']._serialized_start=1044
  _globals['_SETPOSITIONNEDRESPONSE']._serialized_end=1130
  _globals['_SETPOSITIONGLOBALREQUEST']._serialized_start=1132
  _globals['_SETPOSITIONGLOBALREQUEST']._serialized_end=1245
  _globals['_SETPOSITIONGLOBALRESPONSE']._serialized_start=1247
  _globals['_SETPOSITIONGLOBALRESPONSE']._serialized_end=1336
  _globals['_SETVELOCITYBODYREQUEST']._serialized_start=1338
  _globals['_SETVELOCITYBODYREQUEST']._serialized_end=1455
  _globals['_SETVELOCITYBODYRESPONSE']._serialized_start=1457
  _globals['_SETVELOCITYBODYRESPONSE']._serialized_end=1544
  _globals['_SETVELOCITYNEDREQUEST']._serialized_start=1546
  _globals['_SETVELOCITYNEDREQUEST']._serialized_end=1650
  _globals['_SETVELOCITYNEDRESPONSE']._serialized_start=1652
  _globals['_SETVELOCITYNEDRESPONSE']._serialized_end=1738
  _globals['_SETPOSITIONVELOCITYNEDREQUEST']._serialized_start=1741
  _globals['_SETPOSITIONVELOCITYNEDREQUEST']._serialized_end=1916
  _globals['_SETPOSITIONVELOCITYNEDRESPONSE']._serialized_start=1918
  _globals['_SETPOSITIONVELOCITYNEDRESPONSE']._serialized_end=2012
  _globals['_SETACCELERATIONNEDREQUEST']._serialized_start=2014
  _globals['_SETACCELERATIONNEDREQUEST']._serialized_end=2123
  _globals['_SETACCELERATIONNEDRESPONSE']._serialized_start=2125
  _globals['_SETACCELERATIONNEDRESPONSE']._serialized_end=2215
  _globals['_ATTITUDE']._serialized_start=2217
  _globals['_ATTITUDE']._serialized_end=2303
  _globals['_ACTUATORCONTROLGROUP']._serialized_start=2305
  _globals['_ACTUATORCONTROLGROUP']._serialized_end=2345
  _globals['_ACTUATORCONTROL']._serialized_start=2347
  _globals['_ACTUATORCONTROL']._serialized_end=2423
  _globals['_ATTITUDERATE']._serialized_start=2425
  _globals['_ATTITUDERATE']._serialized_end=2521
  _globals['_POSITIONNEDYAW']._serialized_start=2523
  _globals['_POSITIONNEDYAW']._serialized_end=2605
  _globals['_POSITIONGLOBALYAW']._serialized_start=2608
  _globals['_POSITIONGLOBALYAW']._serialized_end=2860
  _globals['_POSITIONGLOBALYAW_ALTITUDETYPE']._serialized_start=2771
  _globals['_POSITIONGLOBALYAW_ALTITUDETYPE']._serialized_end=2860
  _globals['_VELOCITYBODYYAWSPEED']._serialized_start=2862
  _globals['_VELOCITYBODYYAWSPEED']._serialized_end=2966
  _globals['_VELOCITYNEDYAW']._serialized_start=2968
  _globals['_VELOCITYNEDYAW']._serialized_end=3056
  _globals['_ACCELERATIONNED']._serialized_start=3058
  _globals['_ACCELERATIONNED']._serialized_end=3133
  _globals['_OFFBOARDRESULT']._serialized_start=3136
  _globals['_OFFBOARDRESULT']._serialized_end=3426
  _globals['_OFFBOARDRESULT_RESULT']._serialized_start=3235
  _globals['_OFFBOARDRESULT_RESULT']._serialized_end=3426
  _globals['_OFFBOARDSERVICE']._serialized_start=3429
  _globals['_OFFBOARDSERVICE']._serialized_end=4774
# @@protoc_insertion_point(module_scope)

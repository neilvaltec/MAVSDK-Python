# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: camera/camera.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x63\x61mera/camera.proto\x12\x11mavsdk.rpc.camera\x1a\x14mavsdk_options.proto\"\"\n\x0ePrepareRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"I\n\x0fPrepareResponse\x12\x36\n\rcamera_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.camera.CameraResult\"$\n\x10TakePhotoRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"K\n\x11TakePhotoResponse\x12\x36\n\rcamera_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.camera.CameraResult\"A\n\x19StartPhotoIntervalRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12\x12\n\ninterval_s\x18\x02 \x01(\x02\"T\n\x1aStartPhotoIntervalResponse\x12\x36\n\rcamera_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.camera.CameraResult\",\n\x18StopPhotoIntervalRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"S\n\x19StopPhotoIntervalResponse\x12\x36\n\rcamera_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.camera.CameraResult\"%\n\x11StartVideoRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"L\n\x12StartVideoResponse\x12\x36\n\rcamera_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.camera.CameraResult\"$\n\x10StopVideoRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"K\n\x11StopVideoResponse\x12\x36\n\rcamera_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.camera.CameraResult\".\n\x1aStartVideoStreamingRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"U\n\x1bStartVideoStreamingResponse\x12\x36\n\rcamera_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.camera.CameraResult\"-\n\x19StopVideoStreamingRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"T\n\x1aStopVideoStreamingResponse\x12\x36\n\rcamera_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.camera.CameraResult\"I\n\x0eSetModeRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12%\n\x04mode\x18\x02 \x01(\x0e\x32\x17.mavsdk.rpc.camera.Mode\"I\n\x0fSetModeResponse\x12\x36\n\rcamera_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.camera.CameraResult\"[\n\x11ListPhotosRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12\x34\n\x0cphotos_range\x18\x02 \x01(\x0e\x32\x1e.mavsdk.rpc.camera.PhotosRange\"\x83\x01\n\x12ListPhotosResponse\x12\x36\n\rcamera_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.camera.CameraResult\x12\x35\n\rcapture_infos\x18\x02 \x03(\x0b\x32\x1e.mavsdk.rpc.camera.CaptureInfo\"/\n\x1bSubscribeInformationRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"J\n\x13InformationResponse\x12\x33\n\x0binformation\x18\x01 \x01(\x0b\x32\x1e.mavsdk.rpc.camera.Information\"(\n\x14SubscribeModeRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"5\n\x0cModeResponse\x12%\n\x04mode\x18\x01 \x01(\x0e\x32\x17.mavsdk.rpc.camera.Mode\"3\n\x1fSubscribeVideoStreamInfoRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"X\n\x17VideoStreamInfoResponse\x12=\n\x11video_stream_info\x18\x01 \x01(\x0b\x32\".mavsdk.rpc.camera.VideoStreamInfo\"/\n\x1bSubscribeCaptureInfoRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"K\n\x13\x43\x61ptureInfoResponse\x12\x34\n\x0c\x63\x61pture_info\x18\x01 \x01(\x0b\x32\x1e.mavsdk.rpc.camera.CaptureInfo\"*\n\x16SubscribeStatusRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"B\n\x0eStatusResponse\x12\x30\n\rcamera_status\x18\x01 \x01(\x0b\x32\x19.mavsdk.rpc.camera.Status\"3\n\x1fSubscribeCurrentSettingsRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"O\n\x17\x43urrentSettingsResponse\x12\x34\n\x10\x63urrent_settings\x18\x01 \x03(\x0b\x32\x1a.mavsdk.rpc.camera.Setting\":\n&SubscribePossibleSettingOptionsRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"\\\n\x1ePossibleSettingOptionsResponse\x12:\n\x0fsetting_options\x18\x01 \x03(\x0b\x32!.mavsdk.rpc.camera.SettingOptions\"R\n\x11SetSettingRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12+\n\x07setting\x18\x02 \x01(\x0b\x32\x1a.mavsdk.rpc.camera.Setting\"L\n\x12SetSettingResponse\x12\x36\n\rcamera_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.camera.CameraResult\"R\n\x11GetSettingRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12+\n\x07setting\x18\x02 \x01(\x0b\x32\x1a.mavsdk.rpc.camera.Setting\"y\n\x12GetSettingResponse\x12\x36\n\rcamera_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.camera.CameraResult\x12+\n\x07setting\x18\x02 \x01(\x0b\x32\x1a.mavsdk.rpc.camera.Setting\"(\n\x14\x46ormatStorageRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\"O\n\x15\x46ormatStorageResponse\x12\x36\n\rcamera_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.camera.CameraResult\"N\n\x14SelectCameraResponse\x12\x36\n\rcamera_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.camera.CameraResult\":\n\x13SelectCameraRequest\x12\x10\n\x08\x64rone_id\x18\x01 \x01(\x05\x12\x11\n\tcamera_id\x18\x02 \x01(\x05\"\xa0\x02\n\x0c\x43\x61meraResult\x12\x36\n\x06result\x18\x01 \x01(\x0e\x32&.mavsdk.rpc.camera.CameraResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\xc3\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x16\n\x12RESULT_IN_PROGRESS\x10\x02\x12\x0f\n\x0bRESULT_BUSY\x10\x03\x12\x11\n\rRESULT_DENIED\x10\x04\x12\x10\n\x0cRESULT_ERROR\x10\x05\x12\x12\n\x0eRESULT_TIMEOUT\x10\x06\x12\x19\n\x15RESULT_WRONG_ARGUMENT\x10\x07\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x08\"q\n\x08Position\x12\x14\n\x0clatitude_deg\x18\x01 \x01(\x01\x12\x15\n\rlongitude_deg\x18\x02 \x01(\x01\x12\x1b\n\x13\x61\x62solute_altitude_m\x18\x03 \x01(\x02\x12\x1b\n\x13relative_altitude_m\x18\x04 \x01(\x02\"8\n\nQuaternion\x12\t\n\x01w\x18\x01 \x01(\x02\x12\t\n\x01x\x18\x02 \x01(\x02\x12\t\n\x01y\x18\x03 \x01(\x02\x12\t\n\x01z\x18\x04 \x01(\x02\"B\n\nEulerAngle\x12\x10\n\x08roll_deg\x18\x01 \x01(\x02\x12\x11\n\tpitch_deg\x18\x02 \x01(\x02\x12\x0f\n\x07yaw_deg\x18\x03 \x01(\x02\"\xff\x01\n\x0b\x43\x61ptureInfo\x12-\n\x08position\x18\x01 \x01(\x0b\x32\x1b.mavsdk.rpc.camera.Position\x12:\n\x13\x61ttitude_quaternion\x18\x02 \x01(\x0b\x32\x1d.mavsdk.rpc.camera.Quaternion\x12;\n\x14\x61ttitude_euler_angle\x18\x03 \x01(\x0b\x32\x1d.mavsdk.rpc.camera.EulerAngle\x12\x13\n\x0btime_utc_us\x18\x04 \x01(\x04\x12\x12\n\nis_success\x18\x05 \x01(\x08\x12\r\n\x05index\x18\x06 \x01(\x05\x12\x10\n\x08\x66ile_url\x18\x07 \x01(\t\"\xc5\x01\n\x13VideoStreamSettings\x12\x15\n\rframe_rate_hz\x18\x01 \x01(\x02\x12!\n\x19horizontal_resolution_pix\x18\x02 \x01(\r\x12\x1f\n\x17vertical_resolution_pix\x18\x03 \x01(\r\x12\x14\n\x0c\x62it_rate_b_s\x18\x04 \x01(\r\x12\x14\n\x0crotation_deg\x18\x05 \x01(\r\x12\x0b\n\x03uri\x18\x06 \x01(\t\x12\x1a\n\x12horizontal_fov_deg\x18\x07 \x01(\x02\"\xc2\x03\n\x0fVideoStreamInfo\x12\x38\n\x08settings\x18\x01 \x01(\x0b\x32&.mavsdk.rpc.camera.VideoStreamSettings\x12\x44\n\x06status\x18\x02 \x01(\x0e\x32\x34.mavsdk.rpc.camera.VideoStreamInfo.VideoStreamStatus\x12H\n\x08spectrum\x18\x03 \x01(\x0e\x32\x36.mavsdk.rpc.camera.VideoStreamInfo.VideoStreamSpectrum\"]\n\x11VideoStreamStatus\x12#\n\x1fVIDEO_STREAM_STATUS_NOT_RUNNING\x10\x00\x12#\n\x1fVIDEO_STREAM_STATUS_IN_PROGRESS\x10\x01\"\x85\x01\n\x13VideoStreamSpectrum\x12!\n\x1dVIDEO_STREAM_SPECTRUM_UNKNOWN\x10\x00\x12\'\n#VIDEO_STREAM_SPECTRUM_VISIBLE_LIGHT\x10\x01\x12\"\n\x1eVIDEO_STREAM_SPECTRUM_INFRARED\x10\x02\"\x87\x05\n\x06Status\x12\x10\n\x08video_on\x18\x01 \x01(\x08\x12\x19\n\x11photo_interval_on\x18\x02 \x01(\x08\x12\x18\n\x10used_storage_mib\x18\x03 \x01(\x02\x12\x1d\n\x15\x61vailable_storage_mib\x18\x04 \x01(\x02\x12\x19\n\x11total_storage_mib\x18\x05 \x01(\x02\x12\x18\n\x10recording_time_s\x18\x06 \x01(\x02\x12\x19\n\x11media_folder_name\x18\x07 \x01(\t\x12?\n\x0estorage_status\x18\x08 \x01(\x0e\x32\'.mavsdk.rpc.camera.Status.StorageStatus\x12\x12\n\nstorage_id\x18\t \x01(\r\x12;\n\x0cstorage_type\x18\n \x01(\x0e\x32%.mavsdk.rpc.camera.Status.StorageType\"\x91\x01\n\rStorageStatus\x12 \n\x1cSTORAGE_STATUS_NOT_AVAILABLE\x10\x00\x12\x1e\n\x1aSTORAGE_STATUS_UNFORMATTED\x10\x01\x12\x1c\n\x18STORAGE_STATUS_FORMATTED\x10\x02\x12 \n\x1cSTORAGE_STATUS_NOT_SUPPORTED\x10\x03\"\xa0\x01\n\x0bStorageType\x12\x18\n\x14STORAGE_TYPE_UNKNOWN\x10\x00\x12\x1a\n\x16STORAGE_TYPE_USB_STICK\x10\x01\x12\x13\n\x0fSTORAGE_TYPE_SD\x10\x02\x12\x18\n\x14STORAGE_TYPE_MICROSD\x10\x03\x12\x13\n\x0fSTORAGE_TYPE_HD\x10\x07\x12\x17\n\x12STORAGE_TYPE_OTHER\x10\xfe\x01\"7\n\x06Option\x12\x11\n\toption_id\x18\x01 \x01(\t\x12\x1a\n\x12option_description\x18\x02 \x01(\t\"w\n\x07Setting\x12\x12\n\nsetting_id\x18\x01 \x01(\t\x12\x1b\n\x13setting_description\x18\x02 \x01(\t\x12)\n\x06option\x18\x03 \x01(\x0b\x32\x19.mavsdk.rpc.camera.Option\x12\x10\n\x08is_range\x18\x04 \x01(\x08\"\x7f\n\x0eSettingOptions\x12\x12\n\nsetting_id\x18\x01 \x01(\t\x12\x1b\n\x13setting_description\x18\x02 \x01(\t\x12*\n\x07options\x18\x03 \x03(\x0b\x32\x19.mavsdk.rpc.camera.Option\x12\x10\n\x08is_range\x18\x04 \x01(\x08\"\xd5\x01\n\x0bInformation\x12\x13\n\x0bvendor_name\x18\x01 \x01(\t\x12\x12\n\nmodel_name\x18\x02 \x01(\t\x12\x17\n\x0f\x66ocal_length_mm\x18\x03 \x01(\x02\x12!\n\x19horizontal_sensor_size_mm\x18\x04 \x01(\x02\x12\x1f\n\x17vertical_sensor_size_mm\x18\x05 \x01(\x02\x12 \n\x18horizontal_resolution_px\x18\x06 \x01(\r\x12\x1e\n\x16vertical_resolution_px\x18\x07 \x01(\r*8\n\x04Mode\x12\x10\n\x0cMODE_UNKNOWN\x10\x00\x12\x0e\n\nMODE_PHOTO\x10\x01\x12\x0e\n\nMODE_VIDEO\x10\x02*F\n\x0bPhotosRange\x12\x14\n\x10PHOTOS_RANGE_ALL\x10\x00\x12!\n\x1dPHOTOS_RANGE_SINCE_CONNECTION\x10\x01\x32\xd3\x11\n\rCameraService\x12R\n\x07Prepare\x12!.mavsdk.rpc.camera.PrepareRequest\x1a\".mavsdk.rpc.camera.PrepareResponse\"\x00\x12X\n\tTakePhoto\x12#.mavsdk.rpc.camera.TakePhotoRequest\x1a$.mavsdk.rpc.camera.TakePhotoResponse\"\x00\x12s\n\x12StartPhotoInterval\x12,.mavsdk.rpc.camera.StartPhotoIntervalRequest\x1a-.mavsdk.rpc.camera.StartPhotoIntervalResponse\"\x00\x12p\n\x11StopPhotoInterval\x12+.mavsdk.rpc.camera.StopPhotoIntervalRequest\x1a,.mavsdk.rpc.camera.StopPhotoIntervalResponse\"\x00\x12[\n\nStartVideo\x12$.mavsdk.rpc.camera.StartVideoRequest\x1a%.mavsdk.rpc.camera.StartVideoResponse\"\x00\x12X\n\tStopVideo\x12#.mavsdk.rpc.camera.StopVideoRequest\x1a$.mavsdk.rpc.camera.StopVideoResponse\"\x00\x12z\n\x13StartVideoStreaming\x12-.mavsdk.rpc.camera.StartVideoStreamingRequest\x1a..mavsdk.rpc.camera.StartVideoStreamingResponse\"\x04\x80\xb5\x18\x01\x12w\n\x12StopVideoStreaming\x12,.mavsdk.rpc.camera.StopVideoStreamingRequest\x1a-.mavsdk.rpc.camera.StopVideoStreamingResponse\"\x04\x80\xb5\x18\x01\x12R\n\x07SetMode\x12!.mavsdk.rpc.camera.SetModeRequest\x1a\".mavsdk.rpc.camera.SetModeResponse\"\x00\x12[\n\nListPhotos\x12$.mavsdk.rpc.camera.ListPhotosRequest\x1a%.mavsdk.rpc.camera.ListPhotosResponse\"\x00\x12]\n\rSubscribeMode\x12\'.mavsdk.rpc.camera.SubscribeModeRequest\x1a\x1f.mavsdk.rpc.camera.ModeResponse\"\x00\x30\x01\x12r\n\x14SubscribeInformation\x12..mavsdk.rpc.camera.SubscribeInformationRequest\x1a&.mavsdk.rpc.camera.InformationResponse\"\x00\x30\x01\x12~\n\x18SubscribeVideoStreamInfo\x12\x32.mavsdk.rpc.camera.SubscribeVideoStreamInfoRequest\x1a*.mavsdk.rpc.camera.VideoStreamInfoResponse\"\x00\x30\x01\x12v\n\x14SubscribeCaptureInfo\x12..mavsdk.rpc.camera.SubscribeCaptureInfoRequest\x1a&.mavsdk.rpc.camera.CaptureInfoResponse\"\x04\x80\xb5\x18\x00\x30\x01\x12\x63\n\x0fSubscribeStatus\x12).mavsdk.rpc.camera.SubscribeStatusRequest\x1a!.mavsdk.rpc.camera.StatusResponse\"\x00\x30\x01\x12\x82\x01\n\x18SubscribeCurrentSettings\x12\x32.mavsdk.rpc.camera.SubscribeCurrentSettingsRequest\x1a*.mavsdk.rpc.camera.CurrentSettingsResponse\"\x04\x80\xb5\x18\x00\x30\x01\x12\x93\x01\n\x1fSubscribePossibleSettingOptions\x12\x39.mavsdk.rpc.camera.SubscribePossibleSettingOptionsRequest\x1a\x31.mavsdk.rpc.camera.PossibleSettingOptionsResponse\"\x00\x30\x01\x12[\n\nSetSetting\x12$.mavsdk.rpc.camera.SetSettingRequest\x1a%.mavsdk.rpc.camera.SetSettingResponse\"\x00\x12[\n\nGetSetting\x12$.mavsdk.rpc.camera.GetSettingRequest\x1a%.mavsdk.rpc.camera.GetSettingResponse\"\x00\x12\x64\n\rFormatStorage\x12\'.mavsdk.rpc.camera.FormatStorageRequest\x1a(.mavsdk.rpc.camera.FormatStorageResponse\"\x00\x12\x65\n\x0cSelectCamera\x12&.mavsdk.rpc.camera.SelectCameraRequest\x1a\'.mavsdk.rpc.camera.SelectCameraResponse\"\x04\x80\xb5\x18\x01\x42\x1f\n\x10io.mavsdk.cameraB\x0b\x43\x61meraProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'camera.camera_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020io.mavsdk.cameraB\013CameraProto'
  _CAMERASERVICE.methods_by_name['StartVideoStreaming']._options = None
  _CAMERASERVICE.methods_by_name['StartVideoStreaming']._serialized_options = b'\200\265\030\001'
  _CAMERASERVICE.methods_by_name['StopVideoStreaming']._options = None
  _CAMERASERVICE.methods_by_name['StopVideoStreaming']._serialized_options = b'\200\265\030\001'
  _CAMERASERVICE.methods_by_name['SubscribeCaptureInfo']._options = None
  _CAMERASERVICE.methods_by_name['SubscribeCaptureInfo']._serialized_options = b'\200\265\030\000'
  _CAMERASERVICE.methods_by_name['SubscribeCurrentSettings']._options = None
  _CAMERASERVICE.methods_by_name['SubscribeCurrentSettings']._serialized_options = b'\200\265\030\000'
  _CAMERASERVICE.methods_by_name['SelectCamera']._options = None
  _CAMERASERVICE.methods_by_name['SelectCamera']._serialized_options = b'\200\265\030\001'
  _globals['_MODE']._serialized_start=5590
  _globals['_MODE']._serialized_end=5646
  _globals['_PHOTOSRANGE']._serialized_start=5648
  _globals['_PHOTOSRANGE']._serialized_end=5718
  _globals['_PREPAREREQUEST']._serialized_start=64
  _globals['_PREPAREREQUEST']._serialized_end=98
  _globals['_PREPARERESPONSE']._serialized_start=100
  _globals['_PREPARERESPONSE']._serialized_end=173
  _globals['_TAKEPHOTOREQUEST']._serialized_start=175
  _globals['_TAKEPHOTOREQUEST']._serialized_end=211
  _globals['_TAKEPHOTORESPONSE']._serialized_start=213
  _globals['_TAKEPHOTORESPONSE']._serialized_end=288
  _globals['_STARTPHOTOINTERVALREQUEST']._serialized_start=290
  _globals['_STARTPHOTOINTERVALREQUEST']._serialized_end=355
  _globals['_STARTPHOTOINTERVALRESPONSE']._serialized_start=357
  _globals['_STARTPHOTOINTERVALRESPONSE']._serialized_end=441
  _globals['_STOPPHOTOINTERVALREQUEST']._serialized_start=443
  _globals['_STOPPHOTOINTERVALREQUEST']._serialized_end=487
  _globals['_STOPPHOTOINTERVALRESPONSE']._serialized_start=489
  _globals['_STOPPHOTOINTERVALRESPONSE']._serialized_end=572
  _globals['_STARTVIDEOREQUEST']._serialized_start=574
  _globals['_STARTVIDEOREQUEST']._serialized_end=611
  _globals['_STARTVIDEORESPONSE']._serialized_start=613
  _globals['_STARTVIDEORESPONSE']._serialized_end=689
  _globals['_STOPVIDEOREQUEST']._serialized_start=691
  _globals['_STOPVIDEOREQUEST']._serialized_end=727
  _globals['_STOPVIDEORESPONSE']._serialized_start=729
  _globals['_STOPVIDEORESPONSE']._serialized_end=804
  _globals['_STARTVIDEOSTREAMINGREQUEST']._serialized_start=806
  _globals['_STARTVIDEOSTREAMINGREQUEST']._serialized_end=852
  _globals['_STARTVIDEOSTREAMINGRESPONSE']._serialized_start=854
  _globals['_STARTVIDEOSTREAMINGRESPONSE']._serialized_end=939
  _globals['_STOPVIDEOSTREAMINGREQUEST']._serialized_start=941
  _globals['_STOPVIDEOSTREAMINGREQUEST']._serialized_end=986
  _globals['_STOPVIDEOSTREAMINGRESPONSE']._serialized_start=988
  _globals['_STOPVIDEOSTREAMINGRESPONSE']._serialized_end=1072
  _globals['_SETMODEREQUEST']._serialized_start=1074
  _globals['_SETMODEREQUEST']._serialized_end=1147
  _globals['_SETMODERESPONSE']._serialized_start=1149
  _globals['_SETMODERESPONSE']._serialized_end=1222
  _globals['_LISTPHOTOSREQUEST']._serialized_start=1224
  _globals['_LISTPHOTOSREQUEST']._serialized_end=1315
  _globals['_LISTPHOTOSRESPONSE']._serialized_start=1318
  _globals['_LISTPHOTOSRESPONSE']._serialized_end=1449
  _globals['_SUBSCRIBEINFORMATIONREQUEST']._serialized_start=1451
  _globals['_SUBSCRIBEINFORMATIONREQUEST']._serialized_end=1498
  _globals['_INFORMATIONRESPONSE']._serialized_start=1500
  _globals['_INFORMATIONRESPONSE']._serialized_end=1574
  _globals['_SUBSCRIBEMODEREQUEST']._serialized_start=1576
  _globals['_SUBSCRIBEMODEREQUEST']._serialized_end=1616
  _globals['_MODERESPONSE']._serialized_start=1618
  _globals['_MODERESPONSE']._serialized_end=1671
  _globals['_SUBSCRIBEVIDEOSTREAMINFOREQUEST']._serialized_start=1673
  _globals['_SUBSCRIBEVIDEOSTREAMINFOREQUEST']._serialized_end=1724
  _globals['_VIDEOSTREAMINFORESPONSE']._serialized_start=1726
  _globals['_VIDEOSTREAMINFORESPONSE']._serialized_end=1814
  _globals['_SUBSCRIBECAPTUREINFOREQUEST']._serialized_start=1816
  _globals['_SUBSCRIBECAPTUREINFOREQUEST']._serialized_end=1863
  _globals['_CAPTUREINFORESPONSE']._serialized_start=1865
  _globals['_CAPTUREINFORESPONSE']._serialized_end=1940
  _globals['_SUBSCRIBESTATUSREQUEST']._serialized_start=1942
  _globals['_SUBSCRIBESTATUSREQUEST']._serialized_end=1984
  _globals['_STATUSRESPONSE']._serialized_start=1986
  _globals['_STATUSRESPONSE']._serialized_end=2052
  _globals['_SUBSCRIBECURRENTSETTINGSREQUEST']._serialized_start=2054
  _globals['_SUBSCRIBECURRENTSETTINGSREQUEST']._serialized_end=2105
  _globals['_CURRENTSETTINGSRESPONSE']._serialized_start=2107
  _globals['_CURRENTSETTINGSRESPONSE']._serialized_end=2186
  _globals['_SUBSCRIBEPOSSIBLESETTINGOPTIONSREQUEST']._serialized_start=2188
  _globals['_SUBSCRIBEPOSSIBLESETTINGOPTIONSREQUEST']._serialized_end=2246
  _globals['_POSSIBLESETTINGOPTIONSRESPONSE']._serialized_start=2248
  _globals['_POSSIBLESETTINGOPTIONSRESPONSE']._serialized_end=2340
  _globals['_SETSETTINGREQUEST']._serialized_start=2342
  _globals['_SETSETTINGREQUEST']._serialized_end=2424
  _globals['_SETSETTINGRESPONSE']._serialized_start=2426
  _globals['_SETSETTINGRESPONSE']._serialized_end=2502
  _globals['_GETSETTINGREQUEST']._serialized_start=2504
  _globals['_GETSETTINGREQUEST']._serialized_end=2586
  _globals['_GETSETTINGRESPONSE']._serialized_start=2588
  _globals['_GETSETTINGRESPONSE']._serialized_end=2709
  _globals['_FORMATSTORAGEREQUEST']._serialized_start=2711
  _globals['_FORMATSTORAGEREQUEST']._serialized_end=2751
  _globals['_FORMATSTORAGERESPONSE']._serialized_start=2753
  _globals['_FORMATSTORAGERESPONSE']._serialized_end=2832
  _globals['_SELECTCAMERARESPONSE']._serialized_start=2834
  _globals['_SELECTCAMERARESPONSE']._serialized_end=2912
  _globals['_SELECTCAMERAREQUEST']._serialized_start=2914
  _globals['_SELECTCAMERAREQUEST']._serialized_end=2972
  _globals['_CAMERARESULT']._serialized_start=2975
  _globals['_CAMERARESULT']._serialized_end=3263
  _globals['_CAMERARESULT_RESULT']._serialized_start=3068
  _globals['_CAMERARESULT_RESULT']._serialized_end=3263
  _globals['_POSITION']._serialized_start=3265
  _globals['_POSITION']._serialized_end=3378
  _globals['_QUATERNION']._serialized_start=3380
  _globals['_QUATERNION']._serialized_end=3436
  _globals['_EULERANGLE']._serialized_start=3438
  _globals['_EULERANGLE']._serialized_end=3504
  _globals['_CAPTUREINFO']._serialized_start=3507
  _globals['_CAPTUREINFO']._serialized_end=3762
  _globals['_VIDEOSTREAMSETTINGS']._serialized_start=3765
  _globals['_VIDEOSTREAMSETTINGS']._serialized_end=3962
  _globals['_VIDEOSTREAMINFO']._serialized_start=3965
  _globals['_VIDEOSTREAMINFO']._serialized_end=4415
  _globals['_VIDEOSTREAMINFO_VIDEOSTREAMSTATUS']._serialized_start=4186
  _globals['_VIDEOSTREAMINFO_VIDEOSTREAMSTATUS']._serialized_end=4279
  _globals['_VIDEOSTREAMINFO_VIDEOSTREAMSPECTRUM']._serialized_start=4282
  _globals['_VIDEOSTREAMINFO_VIDEOSTREAMSPECTRUM']._serialized_end=4415
  _globals['_STATUS']._serialized_start=4418
  _globals['_STATUS']._serialized_end=5065
  _globals['_STATUS_STORAGESTATUS']._serialized_start=4757
  _globals['_STATUS_STORAGESTATUS']._serialized_end=4902
  _globals['_STATUS_STORAGETYPE']._serialized_start=4905
  _globals['_STATUS_STORAGETYPE']._serialized_end=5065
  _globals['_OPTION']._serialized_start=5067
  _globals['_OPTION']._serialized_end=5122
  _globals['_SETTING']._serialized_start=5124
  _globals['_SETTING']._serialized_end=5243
  _globals['_SETTINGOPTIONS']._serialized_start=5245
  _globals['_SETTINGOPTIONS']._serialized_end=5372
  _globals['_INFORMATION']._serialized_start=5375
  _globals['_INFORMATION']._serialized_end=5588
  _globals['_CAMERASERVICE']._serialized_start=5721
  _globals['_CAMERASERVICE']._serialized_end=7980
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/game/gamegmtemplates/game_gm_templates_action.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/game/gamegmtemplates/game_gm_templates_action.proto',
  package='pogoprotos.networking.game.gamegmtemplates',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nIpogoprotos/networking/game/gamegmtemplates/game_gm_templates_action.proto\x12*pogoprotos.networking.game.gamegmtemplates*c\n\x15GameGmTemplatesAction\x12$\n UNKNOWN_GAME_GM_TEMPLATES_ACTION\x10\x00\x12$\n\x1e\x44OWNLOAD_GAME_MASTER_TEMPLATES\x10\xa0\xe0\x14\x62\x06proto3'
)

_GAMEGMTEMPLATESACTION = _descriptor.EnumDescriptor(
  name='GameGmTemplatesAction',
  full_name='pogoprotos.networking.game.gamegmtemplates.GameGmTemplatesAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_GAME_GM_TEMPLATES_ACTION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWNLOAD_GAME_MASTER_TEMPLATES', index=1, number=340000,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=121,
  serialized_end=220,
)
_sym_db.RegisterEnumDescriptor(_GAMEGMTEMPLATESACTION)

GameGmTemplatesAction = enum_type_wrapper.EnumTypeWrapper(_GAMEGMTEMPLATESACTION)
UNKNOWN_GAME_GM_TEMPLATES_ACTION = 0
DOWNLOAD_GAME_MASTER_TEMPLATES = 340000


DESCRIPTOR.enum_types_by_name['GameGmTemplatesAction'] = _GAMEGMTEMPLATESACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
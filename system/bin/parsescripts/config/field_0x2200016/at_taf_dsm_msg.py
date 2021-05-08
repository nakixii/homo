#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   at taf dsm msg
modify  record  :   2019-05-25 create file
"""

at_taf_dsm_msg_enum_table = {
  0x0000 : "MN_CALLBACK_CS_CALL",
  0x0001 : "MN_CALLBACK_PS_CALL",
  0x0002 : "MN_CALLBACK_MSG",
  0x0003 : "MN_CALLBACK_SS",
  0x0004 : "MN_CALLBACK_PHONE",
  0x0005 : "MN_CALLBACK_DATA_IND",
  0x0006 : "MN_CALLBACK_DATA_STATUS",
  0x0007 : "MN_CALLBACK_DATA_FLOW",
  0x0008 : "MN_CALLBACK_SET",
  0x0009 : "MN_CALLBACK_QRY",
  0x0010 : "MN_CALLBACK_PHONE_BOOK",
  0x0011 : "MN_CALLBACK_STK",
  0x0012 : "MN_CALLBACK_CMD_CNF",
  0x0013 : "MN_CALLBACK_CHANNEL_STATUS",
  0x0014 : "MN_CALLBACK_PIH",
  0x0015 : "MN_CALLBACK_VOICE_CONTROL",
  0x0016 : "MN_CALLBACK_LOG_PRINT",
  0x0017 : "MN_CALLBACK_IFACE",
  0x0018 : "MN_CALLBACK_MAX",
  0x04f1 : "ID_DSM_NDIS_IFACE_UP_IND",
  0x04f2 : "ID_DSM_NDIS_IFACE_DOWN_IND",
  0x04f3 : "ID_DSM_NDIS_CONFIG_IPV6_DNS_IND",
}

def get_at_taf_dsm_msg_str( MsgId):
    for MsgIdIndex in at_taf_dsm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return at_taf_dsm_msg_enum_table[MsgIdIndex]

    return "none"
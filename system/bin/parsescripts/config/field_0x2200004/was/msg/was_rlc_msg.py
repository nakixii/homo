#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list RrcRlcInterface.h
modify  record  :   2016-01-07 create file
"""

was_rlc_msg_enum_table = {
0x0000 : "ID_RRC_RLC_AM_DATA_REQ",
0x0001 : "ID_RLC_RRC_AM_DATA_CNF",
0x0002 : "ID_RRC_RLC_UM_DATA_REQ",
0x0003 : "ID_RLC_RRC_AM_DATA_IND",
0x0004 : "ID_RRC_RLC_TM_DATA_REQ",
0x0005 : "ID_RLC_RRC_UM_DATA_IND",
0x0006 : "ID_RRC_RLC_AM_CONFIG_REQ",
0x0007 : "ID_RLC_RRC_TM_DATA_IND",
0x0008 : "ID_RRC_RLC_UM_CONFIG_REQ",
0x0009 : "ID_RLC_RRC_CONFIG_CNF",
0x000a : "ID_RRC_RLC_TM_CONFIG_REQ",
0x000b : "ID_RLC_RRC_RELEASE_CNF",
0x000c : "ID_RRC_RLC_RELEASE_REQ",
0x000d : "ID_RLC_RRC_SUSPEND_CNF",
0x000e : "ID_RRC_RLC_SUSPEND_REQ",
0x000f : "ID_RLC_RRC_RESUME_CNF",
0x0010 : "ID_RRC_RLC_RESUME_REQ",
0x0011 : "ID_RLC_RRC_STOP_CNF",
0x0012 : "ID_RRC_RLC_STOP_REQ",
0x0013 : "ID_RLC_RRC_CONTINUE_CNF",
0x0014 : "ID_RRC_RLC_CONTINUE_REQ",
0x0015 : "ID_RLC_RRC_STATUS_IND",
0x0016 : "ID_RRC_RLC_MODE_CHANGE_REQ",
0x0017 : "ID_RLC_RRC_ULDATA_TX_IND",
0x0018 : "ID_RRC_RLC_CIPHER_CONFIG_REQ",
0x0019 : "ID_RLC_RRC_MODE_CHANGE_CNF",
0x001b : "ID_RLC_RRC_CIPHER_CONFIG_CNF",
0x001d : "ID_RLC_RRC_CIPHERING_ACTIVE_IND",
}

def get_was_rlc_msg_str( MsgId):
    for MsgIdIndex in was_rlc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return was_rlc_msg_enum_table[MsgIdIndex]

    return "none"
#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list gas lapdm msg
modify  record  :   2018-03-27 create file
"""

gas_lapdm_msg_enum_table = {
0x0001 : "ID_DL_EST_REQ",
0x0002 : "ID_DL_EST_IND",
0x0003 : "ID_DL_EST_CNF",
0x0004 : "ID_DL_REL_REQ",
0x0005 : "ID_DL_REL_IND",
0x0006 : "ID_DL_REL_CNF",
0x0007 : "ID_DL_SUSPEND_REQ",
0x0007 : "ID_DL_SUSPEND_CNF",
0x0009 : "ID_DL_RESUME_REQ",
0x000A : "ID_DL_RESUME_CNF",
0x000B : "ID_DL_RECONN_REQ",
0x000C : "ID_DL_RECONN_CNF",
0x000D : "ID_DL_DATA_REQ",
0x000E : "ID_DL_DATA_IND",
0x000F : "ID_DL_UNITDATA_REQ",
0x0010 : "ID_DL_UNITDATA_IND",
0x0011 : "ID_MDL_REL_REQ",
0x0012 : "ID_MDL_ERR_IND",
0x0013 : "ID_DL_NACK_DATA_REQ",
0x0014 : "ID_DL_NACK_DATA_CNF",
0x0015 : "ID_DL_INFO_REQ",
0x0016 : "ID_DL_I_RETX_NOTIFY",
}

def get_gas_lapdm_msg_str( MsgId):
    for MsgIdIndex in gas_lapdm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return gas_lapdm_msg_enum_table[MsgIdIndex]

    return "none"
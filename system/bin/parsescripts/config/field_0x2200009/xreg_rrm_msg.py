#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list xreg rrm msg
modify  record  :   2016-04-27 create file
"""

xreg_rrm_msg_enum_table = {
0x0001 : "ID_PS_RRM_RADIO_RESOURCE_APPLY_REQ",
0x0002 : "ID_RRM_PS_RADIO_RESOURCE_APPLY_CNF",
0x0003 : "ID_PS_RRM_RADIO_RESOURCE_RELEASE_IND",
0x0004 : "ID_RRM_PS_RADIO_RESOURCE_OCCUPY_REQ",
0x0005 : "ID_PS_RRM_RADIO_RESOURCE_OCCUPY_CNF",
0x0006 : "ID_PS_RRM_PROTECT_PS_IND",
0x0007 : "ID_PS_RRM_DEPROTECT_PS_IND",
0x0008 : "ID_PS_RRM_REGISTER_IND",
0x0009 : "ID_PS_RRM_DEREGISTER_IND",
0x000A : "ID_PS_RRM_PS_STATUS_IND",
0x000B : "ID_PS_RRM_PS_ERROR_IND",
0x000C : "ID_PS_RRM_ABNORMAL_STATUS_IND",
0x000D : "ID_PS_RRM_PROTECT_SIGNAL_IND",
0x000E : "ID_PS_RRM_DEPROTECT_SIGNAL_IND",
}

def get_xreg_rrm_msg_str( MsgId):
    for MsgIdIndex in xreg_rrm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return xreg_rrm_msg_enum_table[MsgIdIndex]

    return "none"
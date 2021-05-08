#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list gas rrm msg
modify  record  :   2016-01-07 create file
"""

gas_rrm_msg_enum_table = {
0x0001 : "PS_RRM_RADIO_RESOURCE_APPLY_REQ",
0x0002 : "RRM_PS_RADIO_RESOURCE_APPLY_CNF",
0x0003 : "PS_RRM_RADIO_RESOURCE_RELEASE_IND",
0x0004 : "RRM_PS_RADIO_RESOURCE_OCCUPY_REQ",
0x0005 : "PS_RRM_RADIO_RESOURCE_OCCUPY_CNF",
0x000d : "PS_RRM_PROTECT_SIGNAL_IND",
0x000e : "PS_RRM_DEPROTECT_SIGNAL_IND",
0x000f : "RRM_PS_USED_TASK_STATUS_IND",
}

def get_gas_rrm_msg_str( MsgId):
    for MsgIdIndex in gas_rrm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return gas_rrm_msg_enum_table[MsgIdIndex]

    return "none"
#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list gas taf msg
modify  record  :   2016-01-07 create file
"""

gas_taf_msg_enum_table = {
0x0003 : "GAS_CBS_DATA_IND",
0x0004 : "CBS_GAS_CFG_REQ",
0x0007 : "GAS_CBS_CFG_CNF",
0x000D : "RR_CBS_GS_STATUS_CHANGE_IND",
}

def get_gas_taf_msg_str( MsgId):
    for MsgIdIndex in gas_taf_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return gas_taf_msg_enum_table[MsgIdIndex]

    return "none"
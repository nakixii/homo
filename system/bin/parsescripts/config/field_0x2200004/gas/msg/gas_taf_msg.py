#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list gas taf msg
modify  record  :   2016-01-07 create file
"""

gas_taf_msg_enum_table = {
0x0001 : "ID_BMC_CBS_DATA_IND",
0x0002 : "ID_CBS_BMC_CFG_REQ",
0x0003 : "ID_GAS_CBS_DATA_IND",
0x0004 : "ID_CBS_GAS_CFG_REQ",
0x0005 : "ID_BMC_CBS_CFG_CNF",
0x0007 : "ID_GAS_CBS_CFG_CNF",
0x0009 : "ID_RR_CBS_ETWS_PRIMARY_NOTIFY_IND",
0x000B : "ID_LRRC_CBS_DATA_IND",
0x000D : "ID_RR_CBS_GS_STATUS_CHANGE_IND",
}

def get_gas_taf_msg_str( MsgId):
    for MsgIdIndex in gas_taf_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return gas_taf_msg_enum_table[MsgIdIndex]

    return "none"
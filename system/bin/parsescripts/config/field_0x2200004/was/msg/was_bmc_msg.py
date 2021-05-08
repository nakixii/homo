#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list RrcBmcInterface.h
modify  record  :   2016-01-07 create file
"""

was_bmc_msg_enum_table = {
0x0001 : "ID_BMC_RRC_RX_IND",
0x0002 : "ID_RRC_BMC_STATUS_CHANGE_IND",
}

def get_was_bmc_msg_str( MsgId):
    for MsgIdIndex in was_bmc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return was_bmc_msg_enum_table[MsgIdIndex]

    return "none"
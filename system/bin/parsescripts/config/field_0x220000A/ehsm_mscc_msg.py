#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list ehsm mscc msg
modify  record  :   2016-08-12 create file
"""

ehsm_mscc_msg_enum_table = {
0x5000 : "ID_MSCC_EHSM_DETACH_REQ",
0x5001 : "ID_EHSM_MSCC_DETACH_CNF",
}

def get_ehsm_mscc_msg_str( MsgId):
    for MsgIdIndex in ehsm_mscc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return ehsm_mscc_msg_enum_table[MsgIdIndex]

    return "none"
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list at stk msg
modify  record  :   2019-02-25 create file
"""

at_oam_msg_enum_table = {
0x0001 : "STK_AT_DATAPRINT_CNF",
0x0002 : "STK_AT_EVENT_CNF",
0x0003 : "PIH_AT_EVENT_CNF",
0x0004 : "PB_AT_EVENT_CNF",
0x0005 : "EMAT_AT_EVENT_CNF",
}

def get_at_oam_msg_str( MsgId):
    for MsgIdIndex in at_oam_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return at_oam_msg_enum_table[MsgIdIndex]

    return "none"
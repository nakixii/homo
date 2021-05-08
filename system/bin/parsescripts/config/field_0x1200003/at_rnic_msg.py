#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list at rnic msg
modify  record  :   2019-05-25 create file
"""

at_rnic_msg_enum_table = {
0x0002 : "ID_AT_RNIC_DIAL_MODE_REQ",
0x000B : "ID_AT_RNIC_USB_TETHER_INFO_IND",
0x1003 : "ID_RNIC_AT_DIAL_MODE_CNF",
}

def get_at_rnic_msg_str( MsgId):
    for MsgIdIndex in at_rnic_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return at_rnic_msg_enum_table[MsgIdIndex]

    return "none"
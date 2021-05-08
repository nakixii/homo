#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list at ndis msg
modify  record  :   2016-01-22 create file
"""

at_ndis_msg_enum_table = {
0x0001 : "ID_AT_NDIS_PDNINFO_CFG_REQ",
0x0021 : "ID_AT_NDIS_PDNINFO_CFG_CNF",
0x0002 : "ID_AT_NDIS_PDNINFO_REL_REQ",
0x0022 : "ID_AT_NDIS_PDNINFO_REL_CNF",
0x0101 : "ID_AT_NDIS_IFACE_UP_CONFIG_IND",
0x0102 : "ID_AT_NDIS_IFACE_DOWN_CONFIG_IND",
}

def get_at_ndis_msg_str( MsgId):
    for MsgIdIndex in at_ndis_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return at_ndis_msg_enum_table[MsgIdIndex]

    return "none"
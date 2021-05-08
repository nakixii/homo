#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list hsd ehsm msg
modify  record  :   2016-04-27 create file
"""

hsd_ehsm_msg_enum_table = {
0x0000 : "ID_HSD_EHSM_START_REQ",
0x0001 : "ID_EHSM_HSD_START_CNF",
0x0002 : "ID_HSD_EHSM_POWER_OFF_REQ",
0x0003 : "ID_EHSM_HSD_POWER_OFF_CNF",
0x0004 : "ID_HSD_EHSM_POWER_SAVE_REQ",
0x0005 : "ID_EHSM_HSD_POWER_SAVE_CNF",
}

def get_hsd_ehsm_msg_str( MsgId):
    for MsgIdIndex in hsd_ehsm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return hsd_ehsm_msg_enum_table[MsgIdIndex]

    return "none"
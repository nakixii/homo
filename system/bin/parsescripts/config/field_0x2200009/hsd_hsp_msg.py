#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list hsd hsp msg
modify  record  :   2016-04-27 create file
"""

hsd_hsp_msg_enum_table = {
0x9100 : "ID_CAS_CNAS_HRPD_OHM_NOT_CURRENT_IND",
0x9101 : "ID_CAS_CNAS_HRPD_OVERHEAD_MSG_IND",
}

def get_hsd_hsp_msg_str( MsgId):
    for MsgIdIndex in hsd_hsp_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return hsd_hsp_msg_enum_table[MsgIdIndex]

    return "none"
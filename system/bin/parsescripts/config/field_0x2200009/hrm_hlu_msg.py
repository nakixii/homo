#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list hrm hlu msg
modify  record  :   2016-04-27 create file
"""

hrm_hlu_msg_enum_table = {
0x0000 : "ID_HRM_HLU_DATA_IND",
0x0001 : "ID_HLU_HRM_DATA_REQ",
0x0002 : "ID_HRM_HLU_DATA_CNF",
0x0003 : "ID_HLU_HRM_DATA_CANCEL_NTF",
}

def get_hrm_hlu_msg_str( MsgId):
    for MsgIdIndex in hrm_hlu_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return hrm_hlu_msg_enum_table[MsgIdIndex]

    return "none"
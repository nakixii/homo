#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list ehsm esm msg
modify  record  :   2016-04-27 create file
"""

ehsm_esm_msg_enum_table = {
0x0000 : "ID_EHSM_ESM_CLEAR_ALL_BEARER_NOTIFY",
0x0001 : "ID_EHSM_ESM_SYNC_PDN_INFO_IND",
0x1000 : "ID_ESM_EHSM_CLEAR_ALL_BEARER_NOTIFY",
0x1001 : "ID_ESM_EHSM_SYNC_PDN_INFO_IND",
}

def get_ehsm_esm_msg_str( MsgId):
    for MsgIdIndex in ehsm_esm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return ehsm_esm_msg_enum_table[MsgIdIndex]

    return "none"
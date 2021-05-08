#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list ehsm ehsm msg
modify  record  :   2016-04-27 create file
"""

ehsm_ehsm_msg_enum_table = {
0x0000 : "ID_CNAS_EHSM_EHSM_ATTACH_REQ",
0x0001 : "ID_CNAS_EHSM_EHSM_ACTIVATING_RSLT_CNF",
0x0002 : "ID_CNAS_EHSM_EHSM_DEACTIVATING_RSLT_CNF",
0x0003 : "ID_CNAS_EHSM_EHSM_PDN_RE_ESTABLISH_REQ",
0x0004 : "ID_CNAS_EHSM_EHSM_ABORT_REQ",
0x0005 : "ID_CNAS_EHSM_EHSM_LOCAL_DETACH_ALL_REQ",
}

def get_ehsm_ehsm_msg_str( MsgId):
    for MsgIdIndex in ehsm_ehsm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return ehsm_ehsm_msg_enum_table[MsgIdIndex]

    return "none"
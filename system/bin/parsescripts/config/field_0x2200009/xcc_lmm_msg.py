#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list xcc lmm msg
modify  record  :   2016-04-27 create file
"""

xcc_lmm_msg_enum_table = {
0x0000 : "ID_XCC_LMM_CALL_START_NTF",
0x0001 : "ID_XCC_LMM_CALL_END_NTF",
0x0002 : "ID_LMM_XCC_ESR_END_IND",
}

def get_xcc_lmm_msg_str( MsgId):
    for MsgIdIndex in xcc_lmm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return xcc_lmm_msg_enum_table[MsgIdIndex]

    return "none"
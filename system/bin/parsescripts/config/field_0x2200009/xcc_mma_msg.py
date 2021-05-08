#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list xcc mma msg
modify  record  :   2016-04-27 create file
"""

xcc_mma_msg_enum_table = {
0x0000 : "ID_XCC_MMA_1X_CALL_STATE_IND",
}

def get_xcc_mma_msg_str( MsgId):
    for MsgIdIndex in xcc_mma_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return xcc_mma_msg_enum_table[MsgIdIndex]

    return "none"
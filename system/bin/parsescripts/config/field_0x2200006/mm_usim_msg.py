#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list mm usim msg
modify  record  :   2016-02-01 create file
"""

mm_usim_msg_enum_table = {
4 : "USIMM_AUTHENTICATION_CNF",
6 : "USIMM_UPDATEFILE_CNF",
}

def get_mm_usim_msg_str( MsgId):
    for MsgIdIndex in mm_usim_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return mm_usim_msg_enum_table[MsgIdIndex]

    return "none"
#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list xreg taf msg
modify  record  :   2016-04-27 create file
"""

xreg_taf_msg_enum_table = {
0x3000 : "ID_XREG_APS_REG_BEGIN_IND",
}

def get_xreg_taf_msg_str( MsgId):
    for MsgIdIndex in xreg_taf_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return xreg_taf_msg_enum_table[MsgIdIndex]

    return "none"
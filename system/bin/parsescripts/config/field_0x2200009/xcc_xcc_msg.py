#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list xcc xcc msg
modify  record  :   2016-04-27 create file
"""

xcc_xcc_msg_enum_table = {
0x0000 : "ID_CNAS_XCC_XCC_ABORT_REQ",
0x0001 : "ID_CNAS_XCC_XCC_MO_CALLING_RSLT_CNF",
0x0002 : "ID_CNAS_XCC_XCC_MT_CALLING_RSLT_CNF",
0x0003 : "ID_CNAS_XCC_XCC_POWER_DOWN_IND",
0x0004 : "ID_CNAS_XCC_XCC_NDSS_REDIAL_IND",
0x0005 : "ID_CNAS_XCC_XCC_CALL_STATE_IND",
}

def get_xcc_xcc_msg_str( MsgId):
    for MsgIdIndex in xcc_xcc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return xcc_xcc_msg_enum_table[MsgIdIndex]

    return "none"
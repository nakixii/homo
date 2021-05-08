#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list xcc xpds msg
modify  record  :   2016-04-27 create file
"""

xcc_xpds_msg_enum_table = {
0x3000 : "ID_XPDS_XCC_ORIG_AGPS_CALL_REQ",
0x3001 : "ID_XCC_XPDS_ORIG_AGPS_CALL_CNF",
0x3002 : "ID_XPDS_XCC_END_AGPS_CALL_REQ",
0x3003 : "ID_XCC_XPDS_END_AGPS_CALL_CNF",
0x3004 : "ID_XCC_XPDS_INCOMING_CALL_IND",
0x3005 : "ID_XCC_XPDS_CALL_CONN_IND",
0x3006 : "ID_XPDS_XCC_ANSWER_CALL_REQ",
0x3007 : "ID_XCC_XPDS_ANSWER_CALL_CNF",
0x3008 : "ID_XCC_XPDS_SERVICE_CONNECT_IND",
}

def get_xcc_xpds_msg_str( MsgId):
    for MsgIdIndex in xcc_xpds_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return xcc_xpds_msg_enum_table[MsgIdIndex]

    return "none"
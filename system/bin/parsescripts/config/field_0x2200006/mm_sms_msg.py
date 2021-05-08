#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list mm sms msg
modify  record  :   2016-02-01 create file
"""

mm_sms_msg_enum_table = {
1 : "MMSMS_EST_REQ",
3 : "MMSMS_REL_REQ",
5 : "MMSMS_ABORT_REQ",
7 : "MMSMS_DATA_REQ",
9 : "MMSMS_BEGIN_SESSION_NOTIFY",
11 : "MMSMS_END_SESSION_NOTIFY",
0 : "MMSMS_EST_CNF",
2 : "MMSMS_EST_IND",
4 : "MMSMS_REL_IND",
6 : "MMSMS_DATA_IND",
8 : "MMSMS_ERR_IND",
10 : "MMSMS_REG_STATE_IND",
12 : "MMSMS_NACK_DATA_IND",
14 : "MMSMS_RADIO_RESOURCE_CHECK_IND",
}

def get_mm_sms_msg_str( MsgId):
    for MsgIdIndex in mm_sms_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return mm_sms_msg_enum_table[MsgIdIndex]

    return "none"
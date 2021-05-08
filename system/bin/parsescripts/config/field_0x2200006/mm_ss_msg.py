#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list mm ss msg
modify  record  :   2016-02-01 create file
"""

mm_ss_msg_enum_table = {
0 : "MMSS_EST_REQ",
1 : "MMSS_EST_CNF",
2 : "MMSS_DATA_REQ",
3 : "MMSS_EST_IND",
4 : "MMSS_REL_REQ",
5 : "MMSS_DATA_IND",
6 : "MMSS_ABORT_REQ",
7 : "MMSS_REL_IND",
8 : "MMSS_BEGIN_SESSION_NOTIFY",
9 : "MMSS_RADIO_RESOURCE_CHECK_IND",
10 : "MMSS_END_SESSION_NOTIFY",
12 : "MMSS_SS_STATUS_NOTIFY",
}

def get_mm_ss_msg_str( MsgId):
    for MsgIdIndex in mm_ss_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return mm_ss_msg_enum_table[MsgIdIndex]

    return "none"
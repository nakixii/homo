#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list mm cc msg
modify  record  :   2016-02-01 create file
"""

mm_cc_msg_enum_table = {
0 : "MMCC_EST_REQ",
1 : "MMCC_EST_CNF",
2 : "MMCC_REL_REQ",
3 : "MMCC_EST_IND",
4 : "MMCC_ABORT_REQ",
5 : "MMCC_REL_IND",
6 : "MMCC_DATA_REQ",
7 : "MMCC_DATA_IND",
8 : "MMCC_UNIT_DATA_REQ",
9 : "MMCC_UNIT_DATA_IND",
10 : "MMCC_REEST_REQ",
11 : "MMCC_REEST_CNF",
12 : "MMCC_PROMPT_REJ",
13 : "MMCC_SYNC_IND",
14 : "MMCC_START_CC",
15 : "MMCC_ERR_IND",
16 : "MMCC_SRVCC_CALL_INFO_NOTIFY",
17 : "MMCC_PROMPT_IND",
18 : "MMCC_BEGIN_SESSION_NOTIFY",
19 : "MMCC_EMC_NUM_LST_IND",
20 : "MMCC_END_SESSION_NOTIFY",
21 : "MMCC_SRVCC_STATUS_IND",
22 : "MMCC_CALL_STATUS_NTY",
23 : "MMCC_GET_CALL_INFO_REQ",
24 : "MMCC_GET_CALL_INFO_CNF",
25 : "MMCC_RRC_CONN_REL_IND",
26 : "MMCC_CALL_DISC_CAUSE_NTY",
27 : "MMCC_READO_RESOURCE_CHECK_IND",
28 : "MMCC_IMS_CALL_INFO_NTY",
29 : "MMCC_CLOSE_HIFI_REQ",
30 : "MMCC_CLOSE_HIFI_CNF",
31 : "MMCC_NAS_INFO_NOTIFY",
}

def get_mm_cc_msg_str( MsgId):
    for MsgIdIndex in mm_cc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return mm_cc_msg_enum_table[MsgIdIndex]

    return "none"
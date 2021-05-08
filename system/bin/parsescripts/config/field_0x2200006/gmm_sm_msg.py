#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list gmm sm msg
modify  record  :   2016-02-01 create file
"""

gmm_sm_msg_enum_table = {
0 : "GMMSM_ESTABLISH_REQ",
2 : "GMMSM_DATA_REQ",
8 : "GMMSM_PDP_DEACTIVATED_IND",
0x0A : "GMMSM_PDP_MODIFY_IND",
14 : "GMMSM_BEGIN_SESSION_NOTIFY",
16 : "GMMSM_END_SESSION_NOTIFY",
1 : "GMMSM_ESTABLISH_CNF",
3 : "GMMSM_DATA_IND",
5 : "GMMSM_STATUS_IND",
7 : "GMMSM_SERVICE_REJ",
9 : "GMMSM_SYS_INFO_IND",
11 : "GMMSM_REL_IND",
4 : "GMMSM_PDP_STATUS_IND",
12 : "GMMSM_ABORT_REQ",
13 : "GMMSM_SIG_CONN_IND",
15 : "GMMSM_RADIO_RESOURCE_CHECK_IND",
}

def get_gmm_sm_msg_str( MsgId):
    for MsgIdIndex in gmm_sm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return gmm_sm_msg_enum_table[MsgIdIndex]

    return "none"
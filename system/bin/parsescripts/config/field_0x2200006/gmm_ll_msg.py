#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list gmm ll msg
modify  record  :   2016-02-01 create file
"""

gmm_ll_msg_enum_table = {
0x0001 : "ID_LL_GMM_ASSIGN_REQ",
0x0002 : "ID_LL_GMM_TRIGGER_REQ",
0x0003 : "ID_LL_GMM_SUSPEND_REQ",
0x0004 : "ID_LL_GMM_RESUME_REQ",
0x0005 : "ID_LL_GMM_STATUS_IND",
0x0006 : "ID_LL_GMM_ABORT_REQ",
0x0015 : "ID_LL_UNITDATA_REQ",
0x0016 : "ID_LL_UNITDATA_IND",
0x0017 : "ID_LL_UNITDATA_CNF",
0x0020 : "ID_LL_DATA_INFORM",
}

def get_gmm_ll_msg_str( MsgId):
    for MsgIdIndex in gmm_ll_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return gmm_ll_msg_enum_table[MsgIdIndex]

    return "none"
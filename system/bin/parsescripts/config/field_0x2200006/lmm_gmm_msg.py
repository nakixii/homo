#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list lmm gmm msg
modify  record  :   2016-02-01 create file
"""

lmm_gmm_msg_enum_table = {
0x11F1 : "ID_GMM_LMM_RESEL_SECU_INFO_REQ",
0x11F2 : "ID_GMM_LMM_HO_SECU_INFO_REQ",
0x11F3 : "ID_GMM_LMM_INFO_CHANGE_NOTIFY_REQ",
0x11F4 : "ID_GMM_LMM_TIMER_STATE_NOTIFY",
0x11F5 : "ID_GMM_LMM_BEGIN_SESSION_NOTIFY",
0x11F6 : "ID_GMM_LMM_END_SESSION_NOTIFY",
0x11D1 : "ID_LMM_GMM_RESEL_SECU_INFO_CNF",
0x11D2 : "ID_LMM_GMM_HO_SECU_INFO_CNF",
0x11D3 : "ID_LMM_GMM_INFO_CHANGE_NOTIFY",
}

def get_lmm_gmm_msg_str( MsgId):
    for MsgIdIndex in lmm_gmm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return lmm_gmm_msg_enum_table[MsgIdIndex]

    return "none"
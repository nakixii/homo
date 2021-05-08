#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list lmm mm msg
modify  record  :   2016-02-01 create file
"""

lmm_mm_msg_enum_table = {
0x1BB6 : "ID_MM_LMM_CSFB_SERVICE_START_NOTIFY",
0x1BB7 : "ID_MM_LMM_CSFB_SERVICE_ABORT_NOTIFY",
0x1BB8 : "ID_MM_LMM_HO_SECU_INFO_REQ",
0x1BB9 : "ID_MM_LMM_SRVCC_STATUS_NOTIFY",
0x1BBA : "ID_MM_LMM_BEGIN_SESSION_NOTIFY",
0x1BBB : "ID_MM_LMM_END_SESSION_NOTIFY",
0x1BD6 : "ID_LMM_MM_COMBINED_START_NOTIFY_REQ",
0x1BD7 : "ID_LMM_MM_CSFB_SERVICE_END_IND",
0x1BD8 : "ID_LMM_MM_CSFB_SERVICE_PAGING_IND",
0x1BD9 : "ID_LMM_MM_INFO_CHANGE_NOTIFY",
0x1BDA : "ID_LMM_MM_HO_SECU_INFO_CNF",
}

def get_lmm_mm_msg_str( MsgId):
    for MsgIdIndex in lmm_mm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return lmm_mm_msg_enum_table[MsgIdIndex]

    return "none"
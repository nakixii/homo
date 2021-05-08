#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list hsm hlu msg
modify  record  :   2016-04-27 create file
"""

hsm_hlu_msg_enum_table = {
0x0001 : "ID_HSM_HLU_1X_TO_HRPD_HANDOFF_REQ",
0x0002 : "ID_HLU_HSM_1X_TO_HRPD_HANDOFF_CNF",
0x0003 : "ID_HSM_HLU_SESSION_CHANGED_IND",
0x0004 : "ID_HLU_HSM_LOC_CHANGED_IND",
}

def get_hsm_hlu_msg_str( MsgId):
    for MsgIdIndex in hsm_hlu_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return hsm_hlu_msg_enum_table[MsgIdIndex]

    return "none"
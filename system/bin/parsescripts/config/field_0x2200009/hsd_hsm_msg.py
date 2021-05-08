#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list hsd hsm msg
modify  record  :   2016-04-27 create file
"""

hsd_hsm_msg_enum_table = {
0x0000 : "ID_HSD_HSM_START_REQ",
0x0001 : "ID_HSM_HSD_START_CNF",
0x0002 : "ID_HSD_HSM_POWEROFF_REQ",
0x0003 : "ID_HSM_HSD_POWEROFF_CNF",
0x0004 : "ID_HSD_HSM_POWER_SAVE_REQ",
0x0005 : "ID_HSM_HSD_POWER_SAVE_CNF",
0x0006 : "ID_HSD_HSM_SYSTEM_ACQUIRED_IND",
0x0007 : "ID_HSD_HSM_OVERHEAD_MSG_IND",
0x0008 : "ID_HSD_HSM_OHM_NOT_CURRENT_IND",
0x0009 : "ID_HSM_HSD_SESSION_NEG_RESULT_IND",
0x000A : "ID_HSM_HSD_SESSION_OPEN_OR_NEG_END_IND",
0x000B : "ID_HSM_HSD_SESSION_OPEN_OR_NEG_START_IND",
0x000C : "ID_HSM_HSD_CAS_STATUS_IND",
0x000D : "ID_HSM_HSD_CONN_OPEN_IND",
0x000E : "ID_HSD_HSM_SUSPEND_IND",
0x000F : "ID_HSD_HSM_RESUME_IND",
0x0010 : "ID_HSD_HSM_IRAT_FROM_LTE_IND",
0x0011 : "ID_HSD_HSM_IRAT_TO_LTE_IND",
0x0012 : "ID_HSD_HSM_PILOT_SEARCH_FAIL_NTF",
}

def get_hsd_hsm_msg_str( MsgId):
    for MsgIdIndex in hsd_hsm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return hsd_hsm_msg_enum_table[MsgIdIndex]

    return "none"
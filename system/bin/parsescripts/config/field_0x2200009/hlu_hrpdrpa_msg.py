#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list hlu hrpdrpa msg
modify  record  :   2016-04-27 create file
"""

hlu_hrpdrpa_msg_enum_table = {
0x3880 : "ID_CTTF_CNAS_HRPD_PA_COMMITTED_IND",
0x3881 : "ID_CTTF_CNAS_HRPD_PA_ACCESS_AUTH_STATUS_IND",
0x3882 : "ID_CNAS_CTTF_HRPD_PA_SESSION_CLOSED_IND",
}

def get_hlu_hrpdrpa_msg_str( MsgId):
    for MsgIdIndex in hlu_hrpdrpa_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return hlu_hrpdrpa_msg_enum_table[MsgIdIndex]

    return "none"
#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list hsm hsm msg
modify  record  :   2016-04-27 create file
"""

hsm_hsm_msg_enum_table = {
0x0000 : "ID_CNAS_HSM_HSM_UATI_REQ",
0x0001 : "ID_CNAS_HSM_HSM_SESSION_ACTIVE_REQ",
0x0002 : "ID_CNAS_HSM_HSM_SESSION_DEACTIVE_REQ",
0x0003 : "ID_CNAS_HSM_HSM_UATI_REQUEST_RESULT_IND",
0x0004 : "ID_CNAS_HSM_HSM_SESSION_ACTIVE_RESULT_IND",
0x0005 : "ID_CNAS_HSM_HSM_SESSION_DEACTIVE_RESULT_IND",
0x0006 : "ID_CNAS_HSM_HSM_SWITCH_ON_REQ",
0x0007 : "ID_CNAS_HSM_HSM_SWITCH_ON_RESULT_IND",
0x0008 : "ID_CNAS_HSM_HSM_SESSION_CLOSE_IND",
0x0009 : "ID_CNAS_HSM_HSM_CONN_MNMT_REQ",
0x000A : "ID_CNAS_HSM_HSM_CONN_MNMT_RESULT_IND",
0x000B : "ID_CNAS_HSM_HSM_HRPD_PA_RAT_MODE_NTF",
}

def get_hsm_hsm_msg_str( MsgId):
    for MsgIdIndex in hsm_hsm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return hsm_hsm_msg_enum_table[MsgIdIndex]

    return "none"
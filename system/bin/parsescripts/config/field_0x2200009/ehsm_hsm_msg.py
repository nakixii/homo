#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list ehsm hsm msg
modify  record  :   2016-04-27 create file
"""

ehsm_hsm_msg_enum_table = {
0x0000 : "ID_EHSM_HSM_CONN_EST_REQ",
0x0001 : "ID_HSM_EHSM_CONN_EST_CNF",
0x0002 : "ID_EHSM_HSM_DISC_REQ",
0x0003 : "ID_HSM_EHSM_DISC_CNF",
0x0004 : "ID_HSM_EHSM_DISC_IND",
0x0005 : "ID_HSM_EHSM_IRAT_LTE_IND",
0x0006 : "ID_HSM_EHSM_SESSION_INFO_IND",
0x0007 : "ID_EHSM_HSM_EHRPD_NOT_AVAILABLE_IND",
0x0008 : "ID_HSM_EHSM_SUSPEND_IND",
0x0009 : "ID_EHSM_HSM_LTE_REG_SUCCESS_IND",
0x000A : "ID_HSM_EHSM_CONNECT_IND",
}

def get_ehsm_hsm_msg_str( MsgId):
    for MsgIdIndex in ehsm_hsm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return ehsm_hsm_msg_enum_table[MsgIdIndex]

    return "none"
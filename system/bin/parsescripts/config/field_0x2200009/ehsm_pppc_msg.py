#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list ehsm pppc msg
modify  record  :   2016-04-27 create file
"""

ehsm_pppc_msg_enum_table = {
0x0000 : "ID_CNAS_CTTF_EHRPD_ATTACH_REQ",
0x0001 : "ID_CTTF_CNAS_EHRPD_ATTACH_CNF",
0x0002 : "ID_CNAS_CTTF_EHRPD_DETACH_REQ",
0x0003 : "ID_CTTF_CNAS_EHRPD_DETACH_CNF",
0x0004 : "ID_CTTF_CNAS_EHRPD_DETACH_IND",
0x0005 : "ID_CNAS_CTTF_EHRPD_PDN_CONN_REQ",
0x0006 : "ID_CTTF_CNAS_EHRPD_PDN_CONN_CNF",
0x0007 : "ID_CNAS_CTTF_EHRPD_PDN_DISC_REQ",
0x0008 : "ID_CTTF_CNAS_EHRPD_PDN_DISC_CNF",
0x0009 : "ID_CTTF_CNAS_EHRPD_PDN_DISC_IND",
0x000A : "ID_CNAS_CTTF_EHRPD_PDN_LOC_DISC_IND",
0x000B : "ID_CNAS_CTTF_EHRPD_LOC_DETACH_IND",
0x000C : "ID_CNAS_CTTF_EHRPD_LINK_STATUS_NTF",
0x000D : "ID_CTTF_CNAS_EHRPD_RECONN_IND",
0x000E : "ID_CTTF_CNAS_EHRPD_MODIFY_IND",
}

def get_ehsm_pppc_msg_str( MsgId):
    for MsgIdIndex in ehsm_pppc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return ehsm_pppc_msg_enum_table[MsgIdIndex]

    return "none"
#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list hsm hrm msg
modify  record  :   2016-04-27 create file
"""

hsm_hrm_msg_enum_table = {
0x0000 : "ID_HSM_HRM_SESSION_BEGIN_NTF",
0x0001 : "ID_HSM_HRM_SESSION_END_NTF",
0x0002 : "ID_HRM_HSM_DATA_IND",
0x0003 : "ID_HSM_HRM_DATA_REQ",
0x0004 : "ID_HRM_HSM_DATA_CNF",
0x0005 : "ID_HRM_HSM_UATI_CMPL_SND_IND",
0x0006 : "ID_HSM_HRM_DATA_CANCEL_NTF",
}

def get_hsm_hrm_msg_str( MsgId):
    for MsgIdIndex in hsm_hrm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return hsm_hrm_msg_enum_table[MsgIdIndex]

    return "none"
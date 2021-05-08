#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list hsd hrup msg
modify  record  :   2016-04-27 create file
"""

hsd_hrup_msg_enum_table = {
0x8100 : "ID_CAS_CNAS_HRPD_IDLE_HO_IND",
0x8101 : "ID_CNAS_CAS_HRPD_SET_SIGNAL_QUALITY_REQ",
0x8102 : "ID_CAS_CNAS_HRPD_SET_SIGNAL_QUALITY_CNF",
0x8103 : "ID_CAS_CNAS_HRPD_SIGNAL_QUALITY_IND",
0x8104 : "ID_CAS_CNAS_HRPD_DATA_SERVICE_AVAILBLE_IND",
}

def get_hsd_hrup_msg_str( MsgId):
    for MsgIdIndex in hsd_hrup_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return hsd_hrup_msg_enum_table[MsgIdIndex]

    return "none"
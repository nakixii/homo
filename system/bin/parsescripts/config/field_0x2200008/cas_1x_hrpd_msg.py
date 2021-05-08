#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list cas 1x/hrpd inter msg
modify  record  :   2016-03-09 create file
"""

cas_1x_hrpd_msg_enum_table = {
    0x0000 : "ID_CAS_HRPD_1X_PGSLOT_IND",
    0x0001 : "ID_CAS_HRPD_1X_NORMAL_CAMP_STATUS_IND",
    0x0002 : "ID_CAS_HRPD_1X_SLOT_MODE_INFO_IND",
}

def get_cas_1x_hrpd_msg_str(MsgId):
    for MsgIdIndex in cas_1x_hrpd_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return cas_1x_hrpd_msg_enum_table[MsgIdIndex]

    return "unknown"
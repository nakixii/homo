#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list cproc apm msg
modify  record  :   2016-03-10 create file
"""

cproc_apm_msg_enum_table = {
    0x0000 :     "ID_APM_CPROC_1X_NONPROTOCOL_START_REQ",
    0x0001 :     "ID_APM_CPROC_1X_NONPROTOCOL_STOP_REQ",
    0x0002 :     "ID_APM_CPROC_1X_SAR_CTRL_REQ",
    0x0003 :     "ID_CPROC_APM_1X_WORK_MODE_IND",
    0x0004 :     "ID_APM_CPROC_1X_ACTIVE_REQ",
    0x0005 :     "ID_CPROC_APM_1X_ACTIVE_IND",
    0x0006 :     "ID_APM_CPROC_1X_RAT_CAP_UPDATE_REQ",
    0x0007 :     "ID_CPROC_APM_1X_RAT_CAP_UPDATE_CNF",
    0xF000 :     "ID_APM_CPROC_HRPD_ACTIVE_REQ",
    0xF001 :     "ID_CPROC_APM_HRPD_ACTIVE_CNF",
    0xF002 :     "ID_APM_CPROC_HRPD_NONPROTOCOL_START_REQ",
    0xF003 :     "ID_APM_CPROC_HRPD_NONPROTOCOL_STOP_REQ",
    0xF004 :     "ID_APM_CPROC_HRPD_SAR_CTRL_REQ",
    0xF005 :     "ID_CPROC_APM_HRPD_WORK_MODE_IND",
    0xF006 :     "ID_APM_CPROC_HRPD_RAT_CAP_UPDATE_REQ",
    0xF007 :     "ID_CPROC_APM_HRPD_RAT_CAP_UPDATE_CNF",
}

def get_cproc_apm_msg_str( MsgId, usVersion ):
    for MsgIdIndex in cproc_apm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return cproc_apm_msg_enum_table[MsgIdIndex]

    return "unknown"

#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list cproc other msg
modify  record  :   2016-03-30 create file
"""

cproc_other_msg_enum_table = {
    0xB003 :     "ID_CPROC_HRPD_DCXO_SCHEDULE_DCXO_REQ",
    0xB004 :     "ID_CPROC_1X_DCXO_SCHEDULE_DCXO_REQ",
    0x9001 :     "ID_OM_ERR_LOG_CTRL_IND",
    0x9002 :     "ID_OM_ERR_LOG_REPORT_REQ",
    0x9003 :     "ID_OM_ERR_LOG_REPORT_CNF",
    0x9004 :     "ID_OM_FTM_CTRL_IND",
    0x9005 :     "ID_OM_FTM_REPORT_IND",
    0x9006 :     "ID_OM_FTM_REQUIRE_IND",
    0x9007 :     "ID_OM_FTM_REQUIRE_CNF",
    0x9009 :     "ID_OM_FAULT_ERR_LOG_IND",
    0x900A :     "ID_OM_ALARM_ERR_LOG_IND",
    0x9010 :     "ID_OM_INFO_CLT_REPORT_REQ",
    0x9011 :     "ID_OM_INFO_CLT_REPORT_CNF",
    0xFEFF :     "ID_CPROC_UPHY_CSDR_SET_MODE_INFO",
    0xDE01 :     "ID_CPROC_CODEC_1X_VOICE_QUALITY_IND",
}

def get_cproc_other_msg_str(MsgId, usVersion):
    for MsgIdIndex in cproc_other_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return cproc_other_msg_enum_table[MsgIdIndex]

    return "unknown"


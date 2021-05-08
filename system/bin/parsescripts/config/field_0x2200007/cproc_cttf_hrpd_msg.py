#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list cproc cttf hrpd msg
modify  record  :   2016-03-10 create file
"""

cproc_cttf_hrpd_msg_enum_table = {
    0x4300 : "ID_CTTF_CPROC_HRPD_AC_CONFIG_REQ",
    0x4301 : "ID_CPROC_CTTF_HRPD_AC_CONFIG_CNF",
    0x4302 : "ID_CPROC_CTTF_HRPD_AC_PROBE_IND",
    0x4303 : "ID_CTTF_CPROC_HRPD_AC_RELEASE_REQ",
    0x4304 : "ID_CPROC_CTTF_HRPD_AC_RELEASE_CNF",
    0x4305 : "ID_CPROC_CTTF_HRPD_AC_ERROR_IND",
    0x4306 : "ID_CTTF_CPROC_HRPD_TCH_CONFIG_REQ",
    0x4307 : "ID_CPROC_CTTF_HRPD_TCH_CONFIG_CNF",
    0x4308 : "ID_CTTF_CPROC_HRPD_TCH_RECONFIG_REQ",
    0x4309 : "ID_CPROC_CTTF_HRPD_TCH_RECONFIG_CNF",
    0x430A : "ID_CTTF_CPROC_HRPD_DRC_MODE_REQ",
    0x430B : "ID_CPROC_CTTF_HRPD_DRC_MODE_CNF",
    0x430C : "ID_CTTF_CPROC_HRPD_TCH_RELEASE_REQ",
    0x430D : "ID_CPROC_CTTF_HRPD_TCH_RELEASE_CNF",
    0x430E : "ID_CPROC_CTTF_HRPD_SUSPENDED_IND",
    0x430F : "ID_CTTF_CPROC_HRPD_SUSPENDED_RSP",
    0x4310 : "ID_CPROC_CTTF_HRPD_RESUMED_IND",
    0x4311 : "ID_CTTF_CPROC_HRPD_RESUMED_RSP",
    0x4312 : "ID_CTTF_CPROC_HRPD_TCH_SUSPEND_REQ",
    0x4313 : "ID_CTTF_CPROC_HRPD_APM_START_UPDATE_IND",
    0x4314 : "ID_CTTF_CPROC_HRPD_APM_STOP_UPDATE_IND",
}

def get_cproc_cttf_hrpd_msg_str(MsgId, usVersion):
    for MsgIdIndex in cproc_cttf_hrpd_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return cproc_cttf_hrpd_msg_enum_table[MsgIdIndex]

    return "unknown"

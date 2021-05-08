#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list cproc hrpd internal msg
modify  record  :   2016-03-10 create file
                            2016-11-09 update 
"""

cproc_hrpd_internal_msg_enum_table_0000 = {
    0x4500  : "ID_CPROC_CM_SM_HRPD_MEAS_MODE_REQ",
    0x4501  : "ID_CPROC_CM_SM_HRPD_RESET_REQ",
    0x4502  : "ID_CPROC_SM_CM_HRPD_RESET_CNF",
    0x4503  : "ID_CPROC_CM_SM_HRPD_PILOT_SEARCH_REQ",
    0x4504  : "ID_CPROC_SM_CM_HRPD_PILOT_SEARCH_IND",
    0x4505  : "ID_CPROC_CM_SM_HRPD_PILOT_SEARCH_STOP_REQ",
    0x4506  : "ID_CPROC_SM_CM_HRPD_PILOT_SEARCH_STOP_CNF",
    0x4507  : "ID_CPROC_CM_SM_HRPD_GAP_CFG_RSP",
    0x4508  : "ID_CPROC_CM_SM_HRPD_GAP_RSP",
    0x4509  : "ID_CPROC_SM_CM_HRPD_GAP_IND",
    0x450A  : "ID_CPROC_CM_SM_HRPD_MPS_REQ",
    0x450B  : "ID_CPROC_SM_CM_HRPD_MPS_CNF",
    0x450C  : "ID_CPROC_SM_CM_HRPD_MPS_IND",
    0x450D  : "ID_CPROC_CM_SM_HRPD_MPS_SUSPEND_REQ",
    0x450E  : "ID_CPROC_SM_CM_HRPD_MPS_SUSPEND_CNF",
    0x450F  : "ID_CPROC_CM_SM_HRPD_MPS_RESUME_REQ",
    0x4510  : "ID_CPROC_SM_CM_HRPD_MPS_RESUME_CNF",
    0x4511  : "ID_CPROC_CM_SM_HRPD_MPS_STOP_REQ",
    0x4512  : "ID_CPROC_SM_CM_HRPD_MPS_STOP_CNF",
    0x4513  : "ID_CPROC_CM_SM_HRPD_MEAS_REQ",
    0x4514  : "ID_CPROC_CM_SM_HRPD_MEAS_STOP_REQ",
    0x4515  : "ID_CPROC_SM_CM_HRPD_MEAS_STOP_CNF",
    0x4516  : "ID_CPROC_SM_CM_HRPD_MEAS_BUF_FILLED_IND",
    0x4517  : "ID_CPROC_SM_CM_HRPD_ERROR_IND",
    0x4518  : "ID_CPROC_CM_SM_HRPD_MPS_RESET_REQ",
    0x4519  : "ID_CPROC_SM_CM_HRPD_MPS_RESET_CNF",
}

cproc_hrpd_internal_msg_enum_table_0100 = {
    0x4500  : "ID_CPROC_CM_SM_HRPD_MEAS_MODE_REQ",
    0x4501  : "ID_CPROC_CM_SM_HRPD_RESET_REQ",
    0x4502  : "ID_CPROC_SM_CM_HRPD_RESET_CNF",
    0x4503  : "ID_CPROC_CM_SM_HRPD_PILOT_SEARCH_REQ",
    0x4504  : "ID_CPROC_SM_CM_HRPD_PILOT_SEARCH_IND",
    0x4505  : "ID_CPROC_CM_SM_HRPD_PILOT_SEARCH_STOP_REQ",
    0x4506  : "ID_CPROC_SM_CM_HRPD_PILOT_SEARCH_STOP_CNF",
    0x4507  : "ID_CPROC_CM_SM_HRPD_PILOT_SEARCH_SUSPEND_REQ",
    0x4508  : "ID_CPROC_SM_CM_HRPD_PILOT_SEARCH_SUSPEND_CNF",
    0x4509  : "ID_CPROC_CM_SM_HRPD_PILOT_SEARCH_RESUME_REQ",
    0x450A  : "ID_CPROC_CM_SM_HRPD_GAP_CFG_RSP",
    0x450B  : "ID_CPROC_CM_SM_HRPD_GAP_RSP",
    0x450C  : "ID_CPROC_SM_CM_HRPD_GAP_IND",
    0x450D  : "ID_CPROC_CM_SM_HRPD_MPS_REQ",
    0x450E  : "ID_CPROC_SM_CM_HRPD_MPS_CNF",
    0x450F  : "ID_CPROC_SM_CM_HRPD_MPS_IND",
    0x4510  : "ID_CPROC_CM_SM_HRPD_MPS_SUSPEND_REQ",
    0x4511  : "ID_CPROC_SM_CM_HRPD_MPS_SUSPEND_CNF",
    0x4512  : "ID_CPROC_CM_SM_HRPD_MPS_RESUME_REQ",
    0x4513  : "ID_CPROC_SM_CM_HRPD_MPS_RESUME_CNF",
    0x4514  : "ID_CPROC_CM_SM_HRPD_MPS_STOP_REQ",
    0x4515  : "ID_CPROC_SM_CM_HRPD_MPS_STOP_CNF",
    0x4516  : "ID_CPROC_CM_SM_HRPD_MEAS_REQ",
    0x4517  : "ID_CPROC_CM_SM_HRPD_MEAS_STOP_REQ",
    0x4518  : "ID_CPROC_SM_CM_HRPD_MEAS_STOP_CNF",
    0x4519  : "ID_CPROC_SM_CM_HRPD_MEAS_BUF_FILLED_IND",
    0x451A  : "ID_CPROC_SM_CM_HRPD_ERROR_IND",
    0x451B  : "ID_CPROC_CM_SM_HRPD_MPS_RESET_REQ",
    0x451C  : "ID_CPROC_SM_CM_HRPD_MPS_RESET_CNF",
    0x451D  : "ID_CPROC_SM_CM_HRPD_NEW_BUF_IND",
    0x451E  : "ID_CPROC_CM_SM_HRPD_NEW_BUF_RSP",
}

cproc_hrpd_internal_msg_enum_table_0101 = {
    0x4500  : "ID_CPROC_CM_SM_HRPD_MEAS_MODE_REQ",
    0x4501  : "ID_CPROC_CM_SM_HRPD_RESET_REQ",
    0x4502  : "ID_CPROC_SM_CM_HRPD_RESET_CNF",
    0x4503  : "ID_CPROC_CM_SM_HRPD_PILOT_SEARCH_REQ",
    0x4504  : "ID_CPROC_SM_CM_HRPD_PILOT_SEARCH_IND",
    0x4505  : "ID_CPROC_CM_SM_HRPD_PILOT_SEARCH_STOP_REQ",
    0x4506  : "ID_CPROC_SM_CM_HRPD_PILOT_SEARCH_STOP_CNF",
    0x4507  : "ID_CPROC_CM_SM_HRPD_PILOT_SEARCH_SUSPEND_REQ",
    0x4508  : "ID_CPROC_SM_CM_HRPD_PILOT_SEARCH_SUSPEND_CNF",
    0x4509  : "ID_CPROC_CM_SM_HRPD_PILOT_SEARCH_RESUME_REQ",
    0x450A  : "ID_CPROC_SM_CM_HRPD_PS_BUF_FINISH_IND",
    0x450B  : "ID_CPROC_SM_CM_HRPD_RF_IND",
    0x450C  : "ID_CPROC_CM_SM_HRPD_RF_RSP",
    0x450D  : "ID_CPROC_CM_SM_HRPD_GAP_CFG_RSP",
    0x450E  : "ID_CPROC_CM_SM_HRPD_GAP_RSP",
    0x450F  : "ID_CPROC_SM_CM_HRPD_GAP_IND",
    0x4510  : "ID_CPROC_CM_SM_HRPD_MPS_REQ",
    0x4511  : "ID_CPROC_SM_CM_HRPD_MPS_CNF",
    0x4512  : "ID_CPROC_SM_CM_HRPD_MPS_IND",
    0x4513  : "ID_CPROC_CM_SM_HRPD_MPS_SUSPEND_REQ",
    0x4514  : "ID_CPROC_SM_CM_HRPD_MPS_SUSPEND_CNF",
    0x4515  : "ID_CPROC_CM_SM_HRPD_MPS_RESUME_REQ",
    0x4516  : "ID_CPROC_SM_CM_HRPD_MPS_RESUME_CNF",
    0x4517  : "ID_CPROC_CM_SM_HRPD_MPS_STOP_REQ",
    0x4518  : "ID_CPROC_SM_CM_HRPD_MPS_STOP_CNF",
    0x4519  : "ID_CPROC_CM_SM_HRPD_MEAS_REQ",
    0x451A  : "ID_CPROC_CM_SM_HRPD_MEAS_STOP_REQ",
    0x451B  : "ID_CPROC_SM_CM_HRPD_MEAS_STOP_CNF",
    0x451C  : "ID_CPROC_SM_CM_HRPD_MEAS_BUF_FILLED_IND",
    0x451D  : "ID_CPROC_SM_CM_HRPD_ERROR_IND",
    0x451E  : "ID_CPROC_CM_SM_HRPD_MPS_RESET_REQ",
    0x451F  : "ID_CPROC_SM_CM_HRPD_MPS_RESET_CNF",
    0x4520  : "ID_CPROC_SM_CM_HRPD_NEW_BUF_IND",
    0x4521  : "ID_CPROC_CM_SM_HRPD_NEW_BUF_RSP",
}

def get_cproc_hrpd_internal_msg_str(MsgId, usVersion):
    if (usVersion == 0x0000):
        for MsgIdIndex in cproc_hrpd_internal_msg_enum_table_0000.keys():
            if MsgIdIndex == MsgId:
                return cproc_hrpd_internal_msg_enum_table_0000[MsgIdIndex]
        return "unknown"
    elif (usVersion == 0x0100 or usVersion == 0x0103):
        for MsgIdIndex in cproc_hrpd_internal_msg_enum_table_0100.keys():
            if MsgIdIndex == MsgId:
                return cproc_hrpd_internal_msg_enum_table_0100[MsgIdIndex]
        return "unknown"
    elif (usVersion == 0x0101):
        for MsgIdIndex in cproc_hrpd_internal_msg_enum_table_0101.keys():
            if MsgIdIndex == MsgId:
                return cproc_hrpd_internal_msg_enum_table_0101[MsgIdIndex]
        return "unknown"
    elif (usVersion == 0x0102):
        for MsgIdIndex in cproc_hrpd_internal_msg_enum_table_0101.keys():
            if MsgIdIndex == MsgId:
                return cproc_hrpd_internal_msg_enum_table_0101[MsgIdIndex]
        return "unknown"
    else:
        return "unknown"


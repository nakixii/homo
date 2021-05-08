#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list gas l2 msg
modify  record  :   2016-01-07 create file
"""

GAS_GRM_MSG_ENUM_TABLE = {
    0x0001: "CGRM_UL_SETUP_REQ",
    0x0002: "CGRM_UL_SETUP_CNF",
    0x0003: "CGRM_DL_SETUP_REQ",
    0x0004: "CGRM_DL_SETUP_CNF",
    0x0005: "CGRM_UL_CHANGE_REQ",
    0x0006: "CGRM_UL_CHANGE_CNF",
    0x0007: "CGRM_DL_CHANGE_REQ",
    0x0008: "CGRM_DL_CHANGE_CNF",
    0x0009: "CGRM_SUSPEND_REQ",
    0x000A: "CGRM_SUSPEND_CNF",
    0x000B: "CGRM_RESUME_REQ",
    0x000C: "CGRM_RESUME_CNF",
    0x000D: "CGRM_UL_RELEASE_REQ",
    0x000E: "CGRM_UL_RELEASE_CNF",
    0x000F: "CGRM_DL_RELEASE_REQ",
    0x0010: "CGRM_DL_RELEASE_CNF",
    0x0016: "CGRM_MSGDATA_IND",
    0x0031: "CGRM_UL_CLEAR_DATA_REQ",
    0x0032: "CGRM_UL_CLEAR_DATA_CNF",
    0x0036: "CGRM_GPRS_UL_ACK",
    0x0037: "CGRM_UL_RESOURCE_IND",
    0x0038: "CGRM_STATUS_IND",
    0x0039: "CGRM_UL_ACQUIRE_IND",
    0x0040: "CGRM_CTRL_MSG_RRBP_REQ",
    0x0041: "CGRM_RRBP_SEND_IND",
    0x0042: "CGRM_EGPRS_UL_ACK",
    0x0043: "CGRM_INFO_UPDATE_REQ",
    0x0044: "CGRM_INFO_UPDATE_CNF",
    0x0045: "CGRM_TLLI_UPDATE_REQ",
    0x0046: "CGRM_TLLI_UPDATE_CNF",
    0x0047: "CGRM_STOP_TX_REQ",
    0x0048: "CGRM_INIT_TX_REQ",
    0x0050: "GRM_TRACE_GRPS_RRBP_IND",
    0x0051: "GRM_TRACE_EGRPS_RRBP_IND",
    0x0053: "CGRM_TEST_MODE_START_IND",
    0x0054: "CGRM_TEST_MODE_STOP_IND",
    0x0055: "CGRM_GRR_TBF_EST_FAIL_IND",
    0x0056: "CGRM_GRR_DRX_PARA_IND",
    0x0057: "CGRM_UL_SERVICE_IND",
}


def get_gas_grm_msg_str(msg_id):
    for msg_id_index in GAS_GRM_MSG_ENUM_TABLE.keys():
        if msg_id_index == msg_id:
            return GAS_GRM_MSG_ENUM_TABLE[msg_id_index]

    return "none"

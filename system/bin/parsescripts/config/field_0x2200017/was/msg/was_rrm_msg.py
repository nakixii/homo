#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list PsRrmInterface.h
author          :   hudong 00377722
modify  record  :   2018-03-27 create file
"""

WAS_RRM_MSG_ENUM_TABLE = {
    0x0001: "ID_PS_RRM_RADIO_RESOURCE_APPLY_REQ",
    0x0002: "ID_RRM_PS_RADIO_RESOURCE_APPLY_CNF",
    0x0003: "ID_PS_RRM_RADIO_RESOURCE_RELEASE_IND",
    0x0004: "ID_RRM_PS_RADIO_RESOURCE_OCCUPY_REQ",
    0x0005: "ID_PS_RRM_RADIO_RESOURCE_OCCUPY_CNF",
    0x0006: "ID_PS_RRM_PROTECT_PS_IND",
    0x0007: "ID_PS_RRM_DEPROTECT_PS_IND",
    0x0008: "ID_PS_RRM_REGISTER_PS_IND",
    0x0009: "ID_PS_RRM_DEREGISTER_PS_IND",
    0x000a: "ID_RRM_PS_STATUS_IND",
    0x000b: "ID_RRM_PS_ERROR_IND",
    0x000c: "ID_RRM_PS_ABNORMAL_STATUS_IND",
    0x000d: "ID_PS_RRM_PROTECT_SIGNAL_IND",
    0x000e: "ID_PS_RRM_DEPROTECT_SIGNAL_IND",
    0x000f: "ID_RRM_PS_USED_TASK_STATUS_IND",
    0x0010: "ID_PS_RRM_RAT_COMBINED_MODE_IND",
    0x0013: "ID_RRM_PS_RADIO_RESOURCE_CHECK_IND",
}


def get_was_rrm_msg_str(msg_id):
    for msg_id_index in WAS_RRM_MSG_ENUM_TABLE.keys():
        if msg_id_index == msg_id:
            return WAS_RRM_MSG_ENUM_TABLE[msg_id_index]

    return "none"

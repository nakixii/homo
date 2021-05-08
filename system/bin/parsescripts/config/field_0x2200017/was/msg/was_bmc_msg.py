#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list RrcBmcInterface.h
author          :   sunbing 00184266
modify  record  :   2016-01-07 create file
"""

WAS_BMC_MSG_ENUM_TABLE = {
    0x0001: "ID_BMC_RRC_RX_IND",
    0x0002: "ID_RRC_BMC_STATUS_CHANGE_IND",
}


def get_was_bmc_msg_str(msg_id):
    for msg_id_index in WAS_BMC_MSG_ENUM_TABLE.keys():
        if msg_id_index == msg_id:
            return WAS_BMC_MSG_ENUM_TABLE[msg_id_index]

    return "none"

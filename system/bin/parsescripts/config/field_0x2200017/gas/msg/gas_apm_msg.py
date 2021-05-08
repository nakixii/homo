#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list gas css msg
author          :   sunbing 00184266
modify  record  :   2016-01-07 create file
"""

GAS_APM_MSG_ENUM_TABLE = {
    0x8740: "MPH_AS_ACTIVE_DSDS_STATUS_IND",
}


def get_gas_apm_msg_str(msg_id):
    for msg_id_index in GAS_APM_MSG_ENUM_TABLE.keys():
        if msg_id_index == msg_id:
            return GAS_APM_MSG_ENUM_TABLE[msg_id_index]

    return "none"

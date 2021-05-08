#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list pid
author          :   sunbing 00184266
modify  record  :   2016-01-07 create file
"""

GAS_SIM_ENUM_TABLE = {
    6: "USIMM_UPDATEFILE_REQ",
    7: "USIMM_READFILE_REQ",
}

SIM_GAS_ENUM_TABLE = {
    6: "USIMM_UPDATEFILE_CNF",
    7: "USIMM_READFILE_CNF",
}


def get_gas_sim_str(msg_id):
    for msg_id_index in GAS_SIM_ENUM_TABLE.keys():
        if msg_id_index == msg_id:
            return GAS_SIM_ENUM_TABLE[msg_id_index]

    return "none"


def get_sim_gas_str(msg_id):
    for msg_id_index in SIM_GAS_ENUM_TABLE.keys():
        if msg_id_index == msg_id:
            return SIM_GAS_ENUM_TABLE[msg_id_index]

    return "none"

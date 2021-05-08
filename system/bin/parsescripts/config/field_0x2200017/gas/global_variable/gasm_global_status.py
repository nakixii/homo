#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list gasm global status
author          :   sunbing 00184266
modify  record  :   2016-01-09 create file
"""

import struct
import string

MACRO_GPHY_MASTER_MODE_BUTT_INDEX = 0x5
MACRO_SIM_STATUS_BUTT_INDEX = 0x3
MACRO_RAT_PRIO_BUTT_INDEX = 0x4

GASM_GPHY_MASTER_MODE_ENUM_TABLE = {
    0x0: "GAS_MASTER_MODE_NONE",
    0x1: "GAS_MASTER_MODE_GSM",
    0x2: "GAS_MASTER_MODE_WCDMA",
    0x3: "GAS_MASTER_MODE_TDSCDMA",
    0x4: "GAS_MASTER_MODE_LTE",
    0x5: "GAS_MASTER_MODE_BUTT",
}

GASM_SIM_STATUS_ENUM_TABLE = {
    0x0: "RRC_NAS_UICC_ABSENT",
    0x1: "RRC_NAS_USIM_PRESENT",
    0x2: "RRC_NAS_SIM_PRESET",
    0x3: "RRC_NAS_SIM_STATUS_BUTT",
}

GASM_RAT_PRIO_ENUM_TABLE = {
    0x0: "RRMM_RAT_PRIO_NULL",
    0x1: "RRMM_RAT_PRIO_LOW",
    0x2: "RRMM_RAT_PRIO_MIDDLE",
    0x3: "RRMM_RAT_PRIO_HIGH",
    0x4: "RRMM_RAT_PRIO_BUTT",
}


def get_gas_gphy_master_mode(gphy_master_mode):
    for index in GASM_GPHY_MASTER_MODE_ENUM_TABLE.keys():
        if index == gphy_master_mode:
            return GASM_GPHY_MASTER_MODE_ENUM_TABLE[index]

    return GASM_GPHY_MASTER_MODE_ENUM_TABLE[MACRO_GPHY_MASTER_MODE_BUTT_INDEX]


def get_gas_sim_status(sim_status):
    for index in GASM_SIM_STATUS_ENUM_TABLE.keys():
        if index == sim_status:
            return GASM_SIM_STATUS_ENUM_TABLE[index]

    return GASM_SIM_STATUS_ENUM_TABLE[MACRO_SIM_STATUS_BUTT_INDEX]


def get_gas_rat_prio(rat_prio):
    for index in GASM_RAT_PRIO_ENUM_TABLE.keys():
        if index == rat_prio:
            return GASM_RAT_PRIO_ENUM_TABLE[index]

    return GASM_SIM_STATUS_ENUM_TABLE[MACRO_RAT_PRIO_BUTT_INDEX]


def anls_modem_x_gasm_glob_sta(instream, file_offset, outstream):
    instream.seek(file_offset)

    (time_stamp,) = struct.unpack('I', instream.read(4))
    str_time_stamp = '%x' % time_stamp
    outstream.writelines(
        ["%-15s0x%-7s\n" % ("time_stamp :", str_time_stamp.upper())])

    (tick,) = struct.unpack('I', instream.read(4))
    str_tick = '%x' % tick
    outstream.writelines(["%-15s0x%-7s\n" % ("tick :", str_tick.upper())])

    (gphy_master_mode,) = struct.unpack('>B', instream.read(1))
    str_gphy_master_mode = get_gas_gphy_master_mode(gphy_master_mode)
    str_gphy_master_mode = '%s(0x%x)' % (
        str_gphy_master_mode, gphy_master_mode)
    outstream.writelines(
        ["%-15s%-7s\n" % ("gphy_master_mode :", str_gphy_master_mode)])

    (gasm_space,) = struct.unpack('>B', instream.read(1))
    (gasm_space,) = struct.unpack('>B', instream.read(1))
    (gasm_space,) = struct.unpack('>B', instream.read(1))
    (gasm_space,) = struct.unpack('>B', instream.read(1))
    (gasm_space,) = struct.unpack('>B', instream.read(1))
    (gasm_space,) = struct.unpack('>B', instream.read(1))
    (gasm_space,) = struct.unpack('>B', instream.read(1))

    (sim_status,) = struct.unpack('I', instream.read(4))
    str_sim_status = get_gas_sim_status(sim_status)
    str_sim_status = '%s(0x%x)' % (str_sim_status, sim_status)
    outstream.writelines(["%-15s%-7s\n" % ("ulSimStatue :", str_sim_status)])

    (gsm_prio,) = struct.unpack('>B', instream.read(1))
    str_gsm_prio = get_gas_rat_prio(gsm_prio)
    str_gsm_prio = '%s(0x%x)' % (str_gsm_prio, gsm_prio)
    outstream.writelines(["%-15s%-7s\n" % ("gsm_prio :", str_gsm_prio)])

    (utran_prio,) = struct.unpack('>B', instream.read(1))
    str_utran_prio = get_gas_rat_prio(utran_prio)
    str_utran_prio = '%s(0x%x)' % (str_utran_prio, utran_prio)
    outstream.writelines(["%-15s%-7s\n" % ("utran_prio :", str_utran_prio)])

    (lte_prio,) = struct.unpack('>B', instream.read(1))
    str_lte_prio = get_gas_rat_prio(lte_prio)
    str_lte_prio = '%s(0x%x)' % (str_lte_prio, lte_prio)
    outstream.writelines(["%-15s%-7s\n" % ("lte_prio :", str_lte_prio)])

    (gasm_space,) = struct.unpack('>B', instream.read(1))
    (gasm_space,) = struct.unpack('>B', instream.read(1))
    (gasm_space,) = struct.unpack('>B', instream.read(1))
    (gasm_space,) = struct.unpack('>B', instream.read(1))
    (gasm_space,) = struct.unpack('>B', instream.read(1))

#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list gcomm global status
author          :   sunbing 00184266
modify  record  :   2016-01-07 create file
"""

import struct
import string

MACRO_GCOMM_FSM_L2_FDD_MEAS_INDEX = 0x3
MACRO_GCOMM_FSM_L2_TDD_MEAS_INDEX = 0x2

MACRO_GCOMM_FSM_L2_STATUS_BUTT_INDEX = 0xFF

GAS_GCOMM_L1_STATE_ENUM_TABLE = {
    0x01: "GAS_GCOMM_INACTIVE_STAT",
    0x02: "GAS_GCOMM_GSM_IDLE_MEAS_STAT",
    0x03: "GAS_GCOMM_GSM_DEDICATED_MEAS_STAT",
    0x04: "GAS_GCOMM_GPRS_RESEL_MEAS_STAT",
    0x05: "GAS_GCOMM_GPRS_NC_MEAS_STAT",
    0x06: "GAS_GCOMM_STAT_BUTT",
}

GAS_GCOMM_L2_STATE_ENUM_TABLE = {
    0x21: "GAS_GCOMM_L2_STATE_LTE_IDLE_MEAS_WAIT_LRRC_MEAS_CNF",
    0x22: "GAS_GCOMM_L2_STATE_LTE_IDLE_MEAS_WAIT_GPHY_MEAS_CNF",
    0x23: "GAS_GCOMM_L2_STATE_LTE_IDLE_MEAS_WAIT_LRRC_MEAS_IND",
    0x24: "GAS_GCOMM_L2_STATE_LTE_IDLE_MEAS_WAIT_MEAS_PT_EXP",
    0x25: "GAS_GCOMM_L2_STATE_LTE_IDLE_MEAS_WAIT_GPHY_STOP_MEAS_CNF",
    0x26: "GAS_GCOMM_L2_STATE_LTE_IDLE_MEAS_WAIT_LRRC_STOP_MEAS_CNF",
    0x31: "GAS_GCOMM_L2_STATE_LTE_CONNECT_MEAS_WAIT_LRRC_MEAS_CNF",
    0x32: "GAS_GCOMM_L2_STATE_LTE_CONNECT_MEAS_WAIT_GPHY_MEAS_CNF",
    0x33: "GAS_GCOMM_L2_STATE_LTE_CONNECT_MEAS_WAIT_LRRC_MEAS_IND",
    0x34: "GAS_GCOMM_L2_STATE_LTE_CONNECT_MEAS_WAIT_MEAS_PT_EXP",
    0x35: "GAS_GCOMM_L2_STATE_LTE_CONNECT_MEAS_WAIT_GPHY_STOP_MEAS_CNF",
    0x36: "GAS_GCOMM_L2_STATE_LTE_CONNECT_MEAS_WAIT_LRRC_STOP_MEAS_CNF",
    0xFE: "GAS_GCOMM_L2_STATE_INIT",
    0xFF: "GAS_GCOMM_L2_STATE_NULL",
}

GAS_GCOMM_L2_FDD_MEAS_STATE_ENUM_TABLE = {
    0x1: "GAS_GCOMM_L2_STATE_FDD_MEAS_STARTUP_WRRC",
    0x2: "GAS_GCOMM_L2_STATE_FDD_MEAS_STARTUP_GPHY",
    0x3: "GAS_GCOMM_L2_STATE_FDD_MEAS_WAIT_WRRC_MEAS_IND",
    0x4: "GAS_GCOMM_L2_STATE_FDD_MEAS_READY_TO_RELEASE",
    0x5: "GAS_GCOMM_L2_STATE_FDD_MEAS_RELEASE_GPHY",
    0x6: "GAS_GCOMM_L2_STATE_FDD_MEAS_RELEASE_WRRC",
}

GAS_GCOMM_L2_TDS_MEAS_STATE_ENUM_TABLE = {
    0x1: "GAS_GCOMM_L2_STATE_TDS_MEAS_STARTUP_TRRC",
    0x2: "GAS_GCOMM_L2_STATE_TDS_MEAS_STARTUP_GPHY",
    0x3: "GAS_GCOMM_L2_STATE_TDS_MEAS_WAIT_TRRC_MEAS_IND",
    0x4: "GAS_GCOMM_L2_STATE_TDS_MEAS_READY_TO_RELEASE",
    0x5: "GAS_GCOMM_L2_STATE_TDS_MEAS_RELEASE_GPHY",
    0x6: "GAS_GCOMM_L2_STATE_TDS_MEAS_RELEASE_TRRC",
}

GAS_GCOMM_L2_FSM_ENUM_TABLE = {
    0x0: "GAS_GCOMM_FSM_IDLE_LTE_MEASURE",
    0x1: "GAS_GCOMM_FSM_CONNECT_LTE_MEASURE",
    0x2: "GAS_GCOMM_FSM_TDS_MEASURE",
    0x3: "GAS_GCOMM_FSM_FDD_MEASURE",
    0x4: "GAS_GCOMM_FSM_BUTT",
}

GAS_GCOMM_STOP_MEAS_MANNER_ENUM_TABLE = {
    0x0: "GAS_GCOMM_STOP_MEAS_MANNER_NEED_NO_STOP_CNF",
    0x1: "GAS_GCOMM_STOP_MEAS_MANNER_NEED_STOP_CNF",
    0x2: "GAS_GCOMM_STOP_MEAS_MANNER_BUTT",
}


def get_gcomm_l1_state(state):
    for index in GAS_GCOMM_L1_STATE_ENUM_TABLE.keys():
        if index == state:
            return GAS_GCOMM_L1_STATE_ENUM_TABLE[index]

    return "none"


def get_gcomm_l2_fsm(fsm):
    for index in GAS_GCOMM_L2_FSM_ENUM_TABLE.keys():
        if index == fsm:
            return GAS_GCOMM_L2_FSM_ENUM_TABLE[index]

    return "none"


def get_gcomm_l2_interrupt_type(interrupt_type):
    for index in GAS_GCOMM_STOP_MEAS_MANNER_ENUM_TABLE.keys():
        if index == interrupt_type:
            return GAS_GCOMM_STOP_MEAS_MANNER_ENUM_TABLE[index]

    return "none"


def get_gcomm_l2_state(fsm, state):
    if MACRO_GCOMM_FSM_L2_FDD_MEAS_INDEX == fsm:
        for index in GAS_GCOMM_L2_FDD_MEAS_STATE_ENUM_TABLE.keys():
            if index == state:
                return GAS_GCOMM_L2_FDD_MEAS_STATE_ENUM_TABLE[index]
    elif MACRO_GCOMM_FSM_L2_TDD_MEAS_INDEX == fsm:
        for index in GAS_GCOMM_L2_TDS_MEAS_STATE_ENUM_TABLE.keys():
            if index == state:
                return GAS_GCOMM_L2_TDS_MEAS_STATE_ENUM_TABLE[index]
    else:
        for index in GAS_GCOMM_L2_STATE_ENUM_TABLE.keys():
            if index == state:
                return GAS_GCOMM_L2_STATE_ENUM_TABLE[index]

    return GAS_GCOMM_L2_STATE_ENUM_TABLE[MACRO_GCOMM_FSM_L2_STATUS_BUTT_INDEX]


def anls_modem_x_gcomm_glob_sta(instream, file_offset, outstream, vers_no):
    instream.seek(file_offset)

    if vers_no < 3:
        (gcomm_sta,) = struct.unpack('I', instream.read(4))
        str_gcomm_sta = get_gcomm_l1_state(gcomm_sta)
        str_gcomm_sta = '%s(0x%x)' % (str_gcomm_sta, gcomm_sta)
        outstream.writelines(["%-15s%-7s\n" % ("gcomm_sta :", str_gcomm_sta)])

        (gcomm_l2_sta,) = struct.unpack('H', instream.read(2))

        (gcomm_fsm_l2_id,) = struct.unpack('H', instream.read(2))
        str_gcomm_fsm_l2_id = get_gcomm_l2_fsm(gcomm_fsm_l2_id)
        str_gcomm_fsm_l2_id = '%s(0x%x)' % (
            str_gcomm_fsm_l2_id, gcomm_fsm_l2_id)

        str_gcomm_l2_sta = get_gcomm_l2_state(gcomm_fsm_l2_id, gcomm_l2_sta)
        str_gcomm_l2_sta = '%s(0x%x)' % (str_gcomm_l2_sta, gcomm_l2_sta)

        outstream.writelines(
            ["%-15s%-7s\n" % ("gcomm_l2_sta :", str_gcomm_l2_sta)])
        outstream.writelines(
            ["%-15s%-7s\n" % ("gcomm_fsm_l2_id :", str_gcomm_fsm_l2_id)])

        (gcomm_entry_msg_event_type,) = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s0x%-7x\n" % (
            "gcomm_entry_msg_event_type :", gcomm_entry_msg_event_type)])

        (gcomm_l2_interrupt_type,) = struct.unpack('>B', instream.read(1))
        str_gcomm_l2_interrupt_type = get_gcomm_l2_interrupt_type(
            gcomm_l2_interrupt_type)
        str_gcomm_l2_interrupt_type = '%s(0x%x)' % (
            str_gcomm_l2_interrupt_type, gcomm_l2_interrupt_type)
        outstream.writelines(["%-15s%-7s\n" % (
            "gcomm_l2_interrupt_type :", str_gcomm_l2_interrupt_type)])

        (gcomc_space,) = struct.unpack('>B', instream.read(1))
        (gcomc_space,) = struct.unpack('>B', instream.read(1))
        (gcomc_space,) = struct.unpack('>B', instream.read(1))
        (gcomc_space,) = struct.unpack('>B', instream.read(1))
        (gcomc_space,) = struct.unpack('>B', instream.read(1))

        (gcomm_cached_counter,) = struct.unpack('>B', instream.read(1))
        outstream.writelines(["%-15s0x%-7x\n" % (
            "gcomm_cached_counter :", gcomm_cached_counter)])

        (gcomm_cached_cur_msg_index,) = struct.unpack('>B', instream.read(1))
        outstream.writelines(["%-15s0x%-7x\n" % (
            "gcomm_cached_cur_msg_index :", gcomm_cached_cur_msg_index)])

        (gcomm_cached_event_type,) = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s0x%-7x\n" % (
            "aul_gcomc_msg_queue_event_type[0] :", gcomm_cached_event_type)])

        (gcomm_cached_event_type,) = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s0x%-7x\n" % (
            "aul_gcomc_msg_queue_event_type[1] :", gcomm_cached_event_type)])

        (gcomm_cached_event_type,) = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s0x%-7x\n" % (
            "aul_gcomc_msg_queue_event_type[2] :", gcomm_cached_event_type)])

        (gcomm_cached_event_type,) = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s0x%-7x\n" % (
            "aul_gcomc_msg_queue_event_type[3] :", gcomm_cached_event_type)])

        (gcomm_cached_event_type,) = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s0x%-7x\n" % (
            "aul_gcomc_msg_queue_event_type[4] :", gcomm_cached_event_type)])

    else:
        (gcomm_sta,) = struct.unpack('I', instream.read(4))
        str_gcomm_sta = get_gcomm_l1_state(gcomm_sta)
        str_gcomm_sta = '%s(0x%x)' % (str_gcomm_sta, gcomm_sta)
        outstream.writelines(["%-15s%-7s\n" % ("gcomm_sta :", str_gcomm_sta)])

        (gcomm_l2_sta,) = struct.unpack('H', instream.read(2))

        (gcomm_fsm_l2_id,) = struct.unpack('H', instream.read(2))
        str_gcomm_fsm_l2_id = get_gcomm_l2_fsm(gcomm_fsm_l2_id)
        str_gcomm_fsm_l2_id = '%s(0x%x)' % (
            str_gcomm_fsm_l2_id, gcomm_fsm_l2_id)

        str_gcomm_l2_sta = get_gcomm_l2_state(gcomm_fsm_l2_id, gcomm_l2_sta)
        str_gcomm_l2_sta = '%s(0x%x)' % (str_gcomm_l2_sta, gcomm_l2_sta)

        outstream.writelines(
            ["%-15s%-7s\n" % ("gcomm_l2_sta :", str_gcomm_l2_sta)])
        outstream.writelines(
            ["%-15s%-7s\n" % ("gcomm_fsm_l2_id :", str_gcomm_fsm_l2_id)])

        (gcomm_l2_entry_msg_event_type,) = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s0x%-7x\n" % (
            "gcomm_l2_entry_msg_event_type :", gcomm_l2_entry_msg_event_type)])

        (gcomm_l2_interrupt_type,) = struct.unpack('>B', instream.read(1))
        str_gcomm_l2_interrupt_type = get_gcomm_l2_interrupt_type(
            gcomm_l2_interrupt_type)
        str_gcomm_l2_interrupt_type = '%s(0x%x)' % (
            str_gcomm_l2_interrupt_type, gcomm_l2_interrupt_type)
        outstream.writelines(["%-15s%-7s\n" % (
            "gcomm_l2_interrupt_type :", str_gcomm_l2_interrupt_type)])

        (gcomc_space,) = struct.unpack('>B', instream.read(1))
        (gcomc_space,) = struct.unpack('>B', instream.read(1))
        (gcomc_space,) = struct.unpack('>B', instream.read(1))
        (gcomc_space,) = struct.unpack('>B', instream.read(1))
        (gcomc_space,) = struct.unpack('>B', instream.read(1))

        (gcomm_l3_sta,) = struct.unpack('H', instream.read(2))

        (gcomm_fsm_l3_id,) = struct.unpack('H', instream.read(2))
        str_gcomm_fsm_l3_id = get_gcomm_l2_fsm(gcomm_fsm_l3_id)
        str_gcomm_fsm_l3_id = '%s(0x%x)' % (
            str_gcomm_fsm_l3_id, gcomm_fsm_l3_id)

        str_gcomm_l3_sta = get_gcomm_l2_state(gcomm_fsm_l3_id, gcomm_l3_sta)
        str_gcomm_l3_sta = '%s(0x%x)' % (str_gcomm_l3_sta, gcomm_l3_sta)

        outstream.writelines(
            ["%-15s%-7s\n" % ("gcomm_l3_sta :", str_gcomm_l3_sta)])
        outstream.writelines(
            ["%-15s%-7s\n" % ("gcomm_fsm_l3_id :", str_gcomm_fsm_l3_id)])

        (gcomc_space,) = struct.unpack('>B', instream.read(1))
        (gcomc_space,) = struct.unpack('>B', instream.read(1))

        (gcomm_l3_entry_msg_event_type,) = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s0x%-7x\n" % (
            "gcomm_l3_entry_msg_event_type :", gcomm_l3_entry_msg_event_type)])

        (gcomm_l3_interrupt_type,) = struct.unpack('>B', instream.read(1))
        str_gcomm_l3_interrupt_type = get_gcomm_l2_interrupt_type(
            gcomm_l3_interrupt_type)
        str_gcomm_l3_interrupt_type = '%s(0x%x)' % (
            str_gcomm_l3_interrupt_type, gcomm_l3_interrupt_type)
        outstream.writelines(["%-15s%-7s\n" % (
            "gcomm_l3_interrupt_type :", str_gcomm_l3_interrupt_type)])

        (gcomc_space,) = struct.unpack('>B', instream.read(1))
        (gcomc_space,) = struct.unpack('>B', instream.read(1))
        (gcomc_space,) = struct.unpack('>B', instream.read(1))
        (gcomc_space,) = struct.unpack('>B', instream.read(1))
        (gcomc_space,) = struct.unpack('>B', instream.read(1))

        (gcomm_l2_cached_counter,) = struct.unpack('>B', instream.read(1))
        outstream.writelines(["%-15s0x%-7x\n" % (
            "gcomm_cached_counter :", gcomm_l2_cached_counter)])

        (gcomm_l2_cached_cur_msg_index,) = struct.unpack(
            '>B', instream.read(1))
        outstream.writelines(["%-15s0x%-7x\n" % (
            "gcomm_l2_cached_cur_msg_index :", gcomm_l2_cached_cur_msg_index)])

        (gcomm_l2_cached_event_type,) = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s0x%-7x\n" % (
            "aul_gcomc_msg_queue_event_type[0] :",
            gcomm_l2_cached_event_type)])

        (gcomm_l2_cached_event_type,) = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s0x%-7x\n" % (
            "aul_gcomc_msg_queue_event_type[1] :",
            gcomm_l2_cached_event_type)])

        (gcomm_l2_cached_event_type,) = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s0x%-7x\n" % (
            "aul_gcomc_msg_queue_event_type[2] :",
            gcomm_l2_cached_event_type)])

        (gcomm_l3_cached_counter,) = struct.unpack('>B', instream.read(1))
        outstream.writelines(["%-15s0x%-7x\n" % (
            "gcomm_cached_counter :", gcomm_l3_cached_counter)])

        (gcomm_l3_cached_cur_msg_index,) = struct.unpack(
            '>B', instream.read(1))
        outstream.writelines(["%-15s0x%-7x\n" % (
            "gcomm_l3_cached_cur_msg_index :", gcomm_l3_cached_cur_msg_index)])

        (gcomc_space,) = struct.unpack('>B', instream.read(1))
        (gcomc_space,) = struct.unpack('>B', instream.read(1))

        (gcomm_l3_cached_event_type,) = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s0x%-7x\n" % (
            "aul_gcomc_msg_queue_event_type[0] :",
            gcomm_l3_cached_event_type)])

        (gcomm_l3_cached_event_type,) = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s0x%-7x\n" % (
            "aul_gcomc_msg_queue_event_type[1] :",
            gcomm_l3_cached_event_type)])

        (gcomm_l3_cached_event_type,) = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s0x%-7x\n" % (
            "aul_gcomc_msg_queue_event_type[2] :",
            gcomm_l3_cached_event_type)])

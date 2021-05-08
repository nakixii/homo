#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2029. All rights reserved.
description     :   analysis was dump bin
author          :   gaoyue 00563542
modify  record  :   2020-04-18 create file
"""

import struct
import os
import sys
import string
from gas.analyse_gas_global import get_gcomm_global_status_lenth
from gas.analyse_gas_global import MACRO_GAS_GASM_GLOBAL_STATUS_LENGTH
from gas.analyse_gas_global import MACRO_GAS_GCOMC_GLOBAL_STATUS_LENGTH
from gas.analyse_gas_global import MACRO_GAS_GCOMSI_GLOBAL_STATUS_LENGTH
from gas.analyse_gas_global import MACRO_GAS_RR_GLOBAL_STATUS_LENGTH
from gas.analyse_gas_global import MACRO_GAS_GRR_GLOBAL_STATUS_LENGTH
from gas.analyse_gas_msg import get_gas_gphy_msg_str
from gas.analyse_gas_msg import get_gas_timer_msg_str
from gas.analyse_gas_msg import get_gas_nas_msg_str
from gas.analyse_gas_msg import get_gas_was_msg_str
from gas.analyse_gas_msg import get_gas_rrm_msg_str
from gas.analyse_gas_msg import get_gas_trrc_msg_str
from gas.analyse_gas_msg import get_gas_lrrc_msg_str
from gas.analyse_gas_msg import get_gas_css_msg_str
from gas.analyse_gas_msg import get_gas_mta_msg_str
from gas.analyse_gas_msg import get_gas_mtc_msg_str
from gas.analyse_gas_msg import get_gas_taf_msg_str
from gas.analyse_gas_msg import get_gas_grm_msg_str
from gas.analyse_gas_msg import get_gas_sim_str
from gas.analyse_gas_msg import get_sim_gas_str
from gas.analyse_gas_msg import get_gas_om_msg_str
from gas.analyse_gas_msg import get_gas_apm_msg_str
from gas.analyse_gas_msg import get_gas_lapdm_msg_str
from was.analyse_was_msg import get_was_wphy_msg_str
from was.analyse_was_msg import get_was_timer_msg_str
from was.analyse_was_msg import get_was_mac_msg_str
from was.analyse_was_msg import get_was_pdcp_msg_str
from was.analyse_was_msg import get_was_rlc_msg_str
from was.analyse_was_msg import get_was_om_msg_str
from was.analyse_was_msg import get_was_lrrc_msg_str
from was.analyse_was_msg import get_was_bmc_msg_str
from was.analyse_was_msg import get_was_rrm_msg_str
from was.analyse_was_msg import get_guas_mta_msg_str
from was.analyse_was_msg import get_guas_bastet_msg_str
from was_pid import guas_get_modem0_pid_str
from was_pid import guas_get_modem1_pid_str
from vers_ctrl import guas_get_version_no
from vers_ctrl import MACRO_VERSION_NO_0
from vers_ctrl import MACRO_VERSION_NO_1
from vers_ctrl import MACRO_VERSION_NO_2
from vers_ctrl import MACRO_VERSION_NO_3
from vers_ctrl import MACRO_VERSION_NO_4

SEPA_START = "\n" + 25 * "*"
SEPA_END = "*" * 25 + "\n"

MACRO_WAS_DEBUG_VERSION_LENGTH = 8
MACRO_GAS_DEBUG_VERSION_LENGTH = 8
MACRO_GAS_MNTN_REC_MSG_INFO_MAX_CNT = 120
MACRO_GAS_MNTN_REC_MSG_INFO_SIZE = 8
MACRO_GAS_MNTN_REC_NAS_MSG_INFO_MAX_CNT = 60

MACRO_WAS_SAVE_EXC_MSG_INFO_SIZE = 8
MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT = 160
MACRO_WAS_MNTN_REC_NAS_MSG_INFO_MAX_CNT = 60
MACRO_WAS_SAVE_FSM_IN_STACK_MAX_NUM = 3
MACRO_WAS_SAVE_MSG_IN_QUEUE_MAX_NUM = 10

MACRO_MODEM0_ADDR_LENGTH = 2048
MACRO_MODEM1_ADDR_LENGTH = 2048

'''
def guas_vers_ctrl(vers_no, outstream):
    global MACRO_GAS_DEBUG_MSG_LIST_LENGTH
    global MACRO_GAS_MODEM0_DUMP_INFO_LENGTH
    global MACRO_GAS_GCOMM_GLOBAL_STATUS_LENGTH

    if MACRO_VERSION_NO_0 == vers_no:
        MACRO_GAS_DEBUG_MSG_LIST_LENGTH = 8 + \
            MACRO_GAS_MNTN_REC_MSG_INFO_SIZE * \
            MACRO_GAS_MNTN_REC_MSG_INFO_MAX_CNT
    elif MACRO_VERSION_NO_1 == vers_no or MACRO_VERSION_NO_2 == vers_no:
        MACRO_GAS_DEBUG_MSG_LIST_LENGTH = 8 + \
            MACRO_GAS_MNTN_REC_MSG_INFO_SIZE * \
            MACRO_GAS_MNTN_REC_MSG_INFO_MAX_CNT + 4 + \
            MACRO_GAS_MNTN_REC_MSG_INFO_SIZE * \
            MACRO_GAS_MNTN_REC_NAS_MSG_INFO_MAX_CNT
    elif MACRO_VERSION_NO_3 == vers_no:
        MACRO_GAS_DEBUG_MSG_LIST_LENGTH = 8 + \
            MACRO_GAS_MNTN_REC_MSG_INFO_SIZE * \
            MACRO_GAS_MNTN_REC_MSG_INFO_MAX_CNT + 4 + \
            MACRO_GAS_MNTN_REC_MSG_INFO_SIZE * \
            MACRO_GAS_MNTN_REC_NAS_MSG_INFO_MAX_CNT
    elif MACRO_VERSION_NO_4 == vers_no:
        MACRO_GAS_DEBUG_MSG_LIST_LENGTH = 8 + \
            MACRO_GAS_MNTN_REC_MSG_INFO_SIZE * \
            MACRO_GAS_MNTN_REC_MSG_INFO_MAX_CNT + 4 + \
            MACRO_GAS_MNTN_REC_MSG_INFO_SIZE * \
            MACRO_GAS_MNTN_REC_NAS_MSG_INFO_MAX_CNT

    MACRO_GAS_GCOMM_GLOBAL_STATUS_LENGTH = get_gcomm_global_status_lenth(
        vers_no)

    MACRO_GAS_MODEM0_DUMP_INFO_LENGTH = MACRO_GAS_DEBUG_MSG_LIST_LENGTH + \
        MACRO_GAS_GASM_GLOBAL_STATUS_LENGTH + \
        MACRO_GAS_GCOMC_GLOBAL_STATUS_LENGTH + \
        MACRO_GAS_GCOMSI_GLOBAL_STATUS_LENGTH + \
        MACRO_GAS_GCOMM_GLOBAL_STATUS_LENGTH + \
        MACRO_GAS_RR_GLOBAL_STATUS_LENGTH + \
        MACRO_GAS_GRR_GLOBAL_STATUS_LENGTH
'''


def analysis_was_debug_version(instream, file_offset, outstream):
    instream.seek(file_offset)

    (version_name_0,) = struct.unpack('>B', instream.read(1))
    (version_name_1,) = struct.unpack('>B', instream.read(1))
    (version_name_2,) = struct.unpack('>B', instream.read(1))
    (version_name_3,) = struct.unpack('>B', instream.read(1))
    (version_space,) = struct.unpack('>B', instream.read(1))
    (version_no_0,) = struct.unpack('>B', instream.read(1))
    (version_no_1,) = struct.unpack('>B', instream.read(1))
    (version_end,) = struct.unpack('>B', instream.read(1))

    version_name = "%s%s%s%s" % (
        chr(version_name_0), chr(version_name_1), chr(version_name_2),
        chr(version_name_3))
    version_no = "%s%s" % (chr(version_no_0), chr(version_no_1))

    outstream.writelines(["%-15s%-7s\n" % ("Version Name:", version_name)])
    outstream.writelines(["%-15s%-7s\n" % ("Version No.:", version_no)])

    vers_no = guas_get_version_no(version_name, version_no)

    return vers_no


def get_gas_msg_str(pid1, pid2, msg_id):
    if 'gphy' == pid1.lower() or 'gphy' == pid2.lower():
        return get_gas_gphy_msg_str(msg_id)
    elif 'i1_gphy' == pid1.lower() or 'i1_gphy' == pid2.lower():
        return get_gas_gphy_msg_str(msg_id)
    elif 'timer' == pid1.lower() or 'timer' == pid2.lower():
        return get_gas_timer_msg_str(msg_id)
    elif 'mmc' == pid1.lower() or 'mmc' == pid2.lower():
        return get_gas_nas_msg_str(msg_id)
    elif 'i1_mmc' == pid1.lower() or 'i1_mmc' == pid2.lower():
        return get_gas_nas_msg_str(msg_id)
    elif 'mm' == pid1.lower() or 'mm' == pid2.lower():
        return get_gas_nas_msg_str(msg_id)
    elif 'i1_mm' == pid1.lower() or 'i1_mm' == pid2.lower():
        return get_gas_nas_msg_str(msg_id)
    elif 'gmm' == pid1.lower() or 'gmm' == pid2.lower():
        return get_gas_nas_msg_str(msg_id)
    elif 'i1_gmm' == pid1.lower() or 'i1_gmm' == pid2.lower():
        return get_gas_nas_msg_str(msg_id)
    elif 'wcom' == pid1.lower() or 'wcom' == pid2.lower():
        return get_gas_was_msg_str(msg_id)
    elif 'i1_wcom' == pid1.lower() or 'i1_wcom' == pid2.lower():
        return get_gas_was_msg_str(msg_id)
    elif 'wrr' == pid1.lower() or 'wrr' == pid2.lower():
        return get_gas_was_msg_str(msg_id)
    elif 'i1_wrr' == pid1.lower() or 'i1_wrr' == pid2.lower():
        return get_gas_was_msg_str(msg_id)
    elif 'rrm' == pid1.lower() or 'rrm' == pid2.lower():
        return get_gas_rrm_msg_str(msg_id)
    elif 'trrc' == pid1.lower() or 'trrc' == pid2.lower():
        return get_gas_trrc_msg_str(msg_id)
    elif 'errc' == pid1.lower() or 'errc' == pid2.lower():
        return get_gas_lrrc_msg_str(msg_id)
    elif 'i1_errc' == pid1.lower() or 'i1_errc' == pid2.lower():
        return get_gas_lrrc_msg_str(msg_id)
    elif 'ermm' == pid1.lower() or 'ermm' == pid2.lower():
        return get_gas_lrrc_msg_str(msg_id)
    elif 'i1_ermm' == pid1.lower() or 'i1_ermm' == pid2.lower():
        return get_gas_lrrc_msg_str(msg_id)
    elif 'css' == pid1.lower() or 'css' == pid2.lower():
        return get_gas_css_msg_str(msg_id)
    elif 'mta' == pid1.lower() or 'mta' == pid2.lower():
        return get_gas_mta_msg_str(msg_id)
    elif 'mtc' == pid1.lower() or 'mtc' == pid2.lower():
        return get_gas_mtc_msg_str(msg_id)
    elif 'taf' == pid1.lower() or 'taf' == pid2.lower():
        return get_gas_taf_msg_str(msg_id)
    elif 'i1_taf' == pid1.lower() or 'i1_taf' == pid2.lower():
        return get_gas_taf_msg_str(msg_id)
    elif 'grm' == pid1.lower() or 'grm' == pid2.lower():
        return get_gas_grm_msg_str(msg_id)
    elif 'i1_grm' == pid1.lower() or 'i1_grm' == pid2.lower():
        return get_gas_grm_msg_str(msg_id)
    elif 'usim' == pid1.lower():
        return get_sim_gas_str(msg_id)
    elif 'usim' == pid2.lower():
        return get_gas_sim_str(msg_id)
    elif 'i1_usim' == pid1.lower():
        return get_sim_gas_str(msg_id)
    elif 'i1_usim' == pid2.lower():
        return get_gas_sim_str(msg_id)
    elif 'msp_pid' == pid1.lower() or 'msp_pid' == pid2.lower():
        return get_gas_om_msg_str(msg_id)
    elif 'apm' == pid2.lower():
        return get_gas_apm_msg_str(msg_id)
    elif 'lapdm' == pid1.lower() or 'lapdm' == pid2.lower():
        return get_gas_lapdm_msg_str(msg_id)
    elif 'ii_lapdm' == pid1.lower() or 'i1_lapdm' == pid2.lower():
        return get_gas_lapdm_msg_str(msg_id)
    elif 'i1_mta' == pid1.lower() or 'i1_mta' == pid2.lower():
        return get_gas_mta_msg_str(msg_id)
    else:
        return 'none'


'''
def anls_gas_mntn_per_rec_msg_info(instream, file_local_offset, outstream,
                                   modem_no):
    instream.seek(file_local_offset)

    (tick,) = struct.unpack('H', instream.read(2))
    (msg_id,) = struct.unpack('H', instream.read(2))
    (send_pid,) = struct.unpack('H', instream.read(2))
    (rcv_pid,) = struct.unpack('H', instream.read(2))

    if 0 == modem_no:
        str_send_pid = guas_get_modem0_pid_str(send_pid)
        str_rcv_pid = guas_get_modem0_pid_str(rcv_pid)
    elif 1 == modem_no:
        str_send_pid = guas_get_modem1_pid_str(send_pid)
        str_rcv_pid = guas_get_modem1_pid_str(rcv_pid)
    else:
        str_send_pid = guas_get_modem0_pid_str(send_pid)
        str_rcv_pid = guas_get_modem0_pid_str(rcv_pid)

    str_msg_id = get_gas_msg_str(str_send_pid, str_rcv_pid, msg_id)

    str_send_pid = '%s(0x%x)' % (str_send_pid, send_pid)
    str_rcv_pid = '%s(0x%x)' % (str_rcv_pid, rcv_pid)
    str_msg_id = '%s(0x%x)' % (str_msg_id, msg_id)
    str_tick = '%x' % tick

    outstream.writelines(
        ["%-15s%-15s%-60s0x%-10s\n" % (
        str_send_pid, str_rcv_pid, str_msg_id, str_tick.upper())])


def get_gas_mntn_rec_msg_cnt(instream, file_offset, msg_index, default_cnt):
    file_offset = file_offset + msg_index * MACRO_GAS_MNTN_REC_MSG_INFO_SIZE
    instream.seek(file_offset)

    (tick,) = struct.unpack('H', instream.read(2))
    (msg_id,) = struct.unpack('H', instream.read(2))
    (send_pid,) = struct.unpack('H', instream.read(2))
    (rcv_pid,) = struct.unpack('H', instream.read(2))

    if 0 == tick and 0 == msg_id and 0 == send_pid and 0 == rcv_pid:
        return msg_index
    else:
        return default_cnt


def analysis_gas_mntn_rec_msg_info(instream, file_offset, outstream, msg_index,
                                   modem_no):
    looper = 0
    instream.seek(file_offset)

    msg_cnt = get_gas_mntn_rec_msg_cnt(instream, file_offset, msg_index,
                                       MACRO_GAS_MNTN_REC_MSG_INFO_MAX_CNT)
    if msg_index == msg_cnt:
        start_index = 0
    else:
        start_index = msg_index

    while looper < msg_cnt:
        looper_index = (
            looper + start_index) % MACRO_GAS_MNTN_REC_MSG_INFO_MAX_CNT
        file_local_offset = file_offset + \
            looper_index * MACRO_GAS_MNTN_REC_MSG_INFO_SIZE
        anls_gas_mntn_per_rec_msg_info(instream, file_local_offset,
                                       outstream, modem_no)
        looper = looper + 1


def analysis_gas_modem_x_msg_list(instream, file_offset, outstream, modem_no):
    instream.seek(file_offset)

    (last_tick,) = struct.unpack('I', instream.read(4))
    str_last_tick = '%x' % last_tick
    outstream.writelines(
        ["%-15s0x%-7s\n" % ("last_tick:", str_last_tick.upper())])

    (msg_index,) = struct.unpack('I', instream.read(4))
    str_msg_index = '%x' % msg_index
    outstream.writelines(
        ["%-15s%d(0x%s)\n" % ("msg_index:", msg_index, str_msg_index.upper())])

    outstream.writelines(["%-15s%-15s%-60s%-10s\n" % (
        "send_pid", "receive_pid", "msg_id", "tick")])
    file_offset = file_offset + 8
    analysis_gas_mntn_rec_msg_info(instream, file_offset, outstream, msg_index,
                                   modem_no)


def anls_gas_mntn_rec_nas_msg_info(instream, file_offset, outstream,
                                   msg_index, modem_no):
    looper = 0
    instream.seek(file_offset)

    msg_cnt = get_gas_mntn_rec_msg_cnt(instream, file_offset, msg_index,
        MACRO_GAS_MNTN_REC_NAS_MSG_INFO_MAX_CNT)

    if msg_index == msg_cnt:
        start_index = 0
    else:
        start_index = msg_index

    while looper < msg_cnt:
        looper_index = (
            looper + start_index) % MACRO_GAS_MNTN_REC_NAS_MSG_INFO_MAX_CNT
        file_local_offset = file_offset + \
            looper_index * MACRO_GAS_MNTN_REC_MSG_INFO_SIZE
        anls_gas_mntn_per_rec_msg_info(instream, file_local_offset,
                                       outstream, modem_no)
        looper = looper + 1


def anls_gas_modem_x_nas_msg_list(instream, file_offset, outstream, modem_no):
    instream.seek(file_offset)

    (nas_msg_index,) = struct.unpack('I', instream.read(4))
    str_nas_msg_index = '%x' % nas_msg_index
    outstream.writelines(
        ["%-15s0x%-7s\n" % ("nas_msg_index:", str_nas_msg_index.upper())])

    outstream.writelines(["%-15s%-15s%-60s%-10s\n" % (
        "send_pid", "receive_pid", "msg_id", "tick")])
    file_offset = file_offset + 4
    anls_gas_mntn_rec_nas_msg_info(instream, file_offset, outstream,
                                   nas_msg_index, modem_no)
'''


def get_was_send_msg_str(msg_id):
    match = 0
    gas_msg = get_gas_was_msg_str(msg_id)
    wphy_msg = get_was_wphy_msg_str(msg_id)
    pdcp_msg = get_was_pdcp_msg_str(msg_id)
    rlc_msg = get_was_rlc_msg_str(msg_id)
    mac_msg = get_was_mac_msg_str(msg_id)
    msp_msg = get_was_om_msg_str(msg_id)
    lrrc_msg = get_was_lrrc_msg_str(msg_id)
    nas_msg = get_gas_nas_msg_str(msg_id)
    bmc_msg = get_was_bmc_msg_str(msg_id)

    if 'none' != gas_msg:
        match = match + 1

    if 'none' != wphy_msg:
        match = match + 1

    if 'none' != pdcp_msg:
        match = match + 1

    if 'none' != rlc_msg:
        match = match + 1

    if 'none' != mac_msg:
        match = match + 1

    if 'none' != msp_msg:
        match = match + 1

    if 'none' != lrrc_msg:
        match = match + 1

    if 'none' != nas_msg:
        match = match + 1

    if 'none' != bmc_msg:
        match = match + 1

    if 1 != match:
        return 'More than one Msg'

    if 'none' != gas_msg:
        return gas_msg

    if 'none' != wphy_msg:
        return wphy_msg

    if 'none' != pdcp_msg:
        return pdcp_msg

    if 'none' != rlc_msg:
        return rlc_msg

    if 'none' != mac_msg:
        return mac_msg

    if 'none' != msp_msg:
        return msp_msg

    if 'none' != lrrc_msg:
        return lrrc_msg

    if 'none' != nas_msg:
        return nas_msg

    if 'none' != bmc_msg:
        return bmc_msg


def get_was_msg_str_vers0(send_pid, msg_id):
    if 'wcom' == send_pid.lower() or 'wrr' == send_pid.lower():
        return get_was_send_msg_str(msg_id)
    elif 'gas' == send_pid.lower():
        return get_gas_was_msg_str(msg_id)
    elif 'wphy' == send_pid.lower():
        return get_was_wphy_msg_str(msg_id)
    elif 'timer' == send_pid.lower():
        return get_was_timer_msg_str(msg_id)
    elif 'pdcp' == send_pid.lower():
        return get_was_pdcp_msg_str(msg_id)
    elif 'rlc' == send_pid.lower():
        return get_was_rlc_msg_str(msg_id)
    elif 'mac' == send_pid.lower():
        return get_was_mac_msg_str(msg_id)
    elif 'msp_pid' == send_pid.lower():
        return get_was_om_msg_str(msg_id)
    elif 'errc' == send_pid.lower() or 'ermm' == send_pid.lower():
        return get_was_lrrc_msg_str(msg_id)
    elif 'mmc' == send_pid.lower():
        return get_gas_nas_msg_str(msg_id)
    elif 'mm' == send_pid.lower():
        return get_gas_nas_msg_str(msg_id)
    elif 'gmm' == send_pid.lower():
        return get_gas_nas_msg_str(msg_id)
    elif 'bmc' == send_pid.lower():
        return get_was_bmc_msg_str(msg_id)
    else:
        return "none"


def get_was_msg_str_vers1(pid1, pid2, msg_id):
    if 'gas' == pid1.lower() or 'gas' == pid2.lower():
        return get_gas_was_msg_str(msg_id)
    if 'i1_gas' == pid1.lower() or 'i1_gas' == pid2.lower():
        return get_gas_was_msg_str(msg_id)
    elif 'wphy' == pid1.lower() or 'wphy' == pid2.lower():
        return get_was_wphy_msg_str(msg_id)
    elif 'i1_wphy' == pid1.lower() or 'i1_wphy' == pid2.lower():
        return get_was_wphy_msg_str(msg_id)
    elif 'timer' == pid1.lower() or 'timer' == pid2.lower():
        return get_was_timer_msg_str(msg_id)
    elif 'pdcp' == pid1.lower() or 'pdcp' == pid2.lower():
        return get_was_pdcp_msg_str(msg_id)
    elif 'i1_pdcp' == pid1.lower() or 'i1_pdcp' == pid2.lower():
        return get_was_pdcp_msg_str(msg_id)
    elif 'rlc' == pid1.lower() or 'rlc' == pid2.lower():
        return get_was_rlc_msg_str(msg_id)
    elif 'i1_rlc' == pid1.lower() or 'i1_rlc' == pid2.lower():
        return get_was_rlc_msg_str(msg_id)
    elif 'mac' == pid1.lower() or 'mac' == pid2.lower():
        return get_was_mac_msg_str(msg_id)
    elif 'i1_mac' == pid1.lower() or 'i1_mac' == pid2.lower():
        return get_was_mac_msg_str(msg_id)
    elif 'msp_pid' == pid1.lower() or 'msp_pid' == pid2.lower():
        return get_was_om_msg_str(msg_id)
    elif 'errc' == pid1.lower() or 'errc' == pid2.lower():
        return get_was_lrrc_msg_str(msg_id)
    elif 'i1_errc' == pid1.lower() or 'i1_errc' == pid2.lower():
        return get_was_lrrc_msg_str(msg_id)
    elif 'ermm' == pid1.lower() or 'ermm' == pid2.lower():
        return get_was_lrrc_msg_str(msg_id)
    elif 'i1_ermm' == pid1.lower() or 'i1_ermm' == pid2.lower():
        return get_was_lrrc_msg_str(msg_id)
    elif 'mmc' == pid1.lower() or 'mmc' == pid2.lower():
        return get_gas_nas_msg_str(msg_id)
    elif 'i1_mmc' == pid1.lower() or 'i1_mmc' == pid2.lower():
        return get_gas_nas_msg_str(msg_id)
    elif 'mm' == pid1.lower() or 'mm' == pid2.lower():
        return get_gas_nas_msg_str(msg_id)
    elif 'i1_mm' == pid1.lower() or 'i1_mm' == pid2.lower():
        return get_gas_nas_msg_str(msg_id)
    elif 'gmm' == pid1.lower() or 'gmm' == pid2.lower():
        return get_gas_nas_msg_str(msg_id)
    elif 'i1_gmm' == pid1.lower() or 'i1_gmm' == pid2.lower():
        return get_gas_nas_msg_str(msg_id)
    elif 'rabm' == pid1.lower() or 'rabm' == pid2.lower():
        return get_gas_nas_msg_str(msg_id)
    elif 'i1_rabm' == pid1.lower() or 'i1_rabm' == pid2.lower():
        return get_gas_nas_msg_str(msg_id)
    elif 'bmc' == pid1.lower() or 'bmc' == pid2.lower():
        return get_was_bmc_msg_str(msg_id)
    elif 'i1_bmc' == pid1.lower() or 'i1_bmc' == pid2.lower():
        return get_was_bmc_msg_str(msg_id)
    elif 'rrm' == pid1.lower() or 'rrm' == pid2.lower():
        return get_was_rrm_msg_str(msg_id)
    elif 'css' == pid1.lower() or 'css' == pid2.lower():
        return get_gas_css_msg_str(msg_id)
    elif 'mtc' == pid1.lower() or 'mtc' == pid2.lower():
        return get_gas_mtc_msg_str(msg_id)
    elif 'taf' == pid1.lower() or 'taf' == pid2.lower():
        return get_gas_taf_msg_str(msg_id)
    elif 'i1_taf' == pid1.lower() or 'i1_taf' == pid2.lower():
        return get_gas_taf_msg_str(msg_id)
    elif 'mta' == pid1.lower() or 'mta' == pid2.lower():
        return get_guas_mta_msg_str(msg_id)
    elif 'i1_mta' == pid1.lower() or 'i1_mta' == pid2.lower():
        return get_guas_mta_msg_str(msg_id)
    elif 'bastet' == pid1.lower() or 'bastet' == pid2.lower():
        return get_guas_bastet_msg_str(msg_id)
    else:
        return 'none'


def anls_was_per_save_exc_msg_ver0(instream, file_local_offset, outstream):
    instream.seek(file_local_offset)

    (time_stamp,) = struct.unpack('I', instream.read(4))
    (send_pid,) = struct.unpack('H', instream.read(2))
    (msg_id,) = struct.unpack('H', instream.read(2))

    str_send_pid = guas_get_modem0_pid_str(send_pid)
    str_msg_id = get_was_msg_str_vers0(send_pid, msg_id)

    str_send_pid = '%s(0x%x)' % (str_send_pid, send_pid)
    str_msg_id = '%s(0x%x)' % (str_msg_id, msg_id)

    outstream.writelines(
        ["%-20s%-60s0x%-27x\n" % (str_send_pid, str_msg_id, time_stamp)])


def anls_was_per_save_exc_msg_ver1(instream, file_local_offset, outstream,
                                   version):
    instream.seek(file_local_offset)

    (time_stamp,) = struct.unpack('H', instream.read(2))
    (msg_id,) = struct.unpack('H', instream.read(2))
    (send_pid,) = struct.unpack('H', instream.read(2))
    (rcv_pid,) = struct.unpack('H', instream.read(2))

    if 0 == version:
        str_send_pid = guas_get_modem0_pid_str(send_pid)
        str_rcv_pid = guas_get_modem0_pid_str(rcv_pid)
    elif 1 == version:
        str_send_pid = guas_get_modem1_pid_str(send_pid)
        str_rcv_pid = guas_get_modem1_pid_str(rcv_pid)
    else:
        str_send_pid = guas_get_modem0_pid_str(send_pid)
        str_rcv_pid = guas_get_modem0_pid_str(rcv_pid)

    str_msg_id = get_was_msg_str_vers1(str_send_pid, str_rcv_pid, msg_id)

    str_send_pid = '%s(0x%x)' % (str_send_pid, send_pid)
    str_rcv_pid = '%s(0x%x)' % (str_rcv_pid, rcv_pid)
    str_msg_id = '%s(0x%x)' % (str_msg_id, msg_id)
    str_tick = '%x' % time_stamp

    outstream.writelines(["%-20s%-15s%-60s0x%-10s\n" % (
        str_send_pid, str_rcv_pid, str_msg_id, str_tick.upper())])


def anls_was_save_exc_msg_vers_01(instream, file_offset, outstream,
                                  handled_msg_num):
    looper = 0

    outstream.writelines(
        ["%-20s%-60s%-27s\n" % ("send_pid", "msg_id", "time_stamp")])

    while looper < MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT:
        looper_index = (
            looper + handled_msg_num) % MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT
        file_local_offset = file_offset + \
            looper_index * MACRO_WAS_SAVE_EXC_MSG_INFO_SIZE
        anls_was_per_save_exc_msg_ver0(instream, file_local_offset, outstream)
        looper = looper + 1


def anls_was_save_exc_msg_vers_02(instream, file_offset, outstream,
                                  handled_msg_num, version):
    looper = 0

    outstream.writelines(["%-20s%-15s%-60s%-10s\n" % (
        "send_pid", "receive_pid", "msg_id", "tick")])

    while looper < MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT:
        looper_index = (
            looper + handled_msg_num) % MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT
        file_local_offset = file_offset + \
            looper_index * MACRO_WAS_SAVE_EXC_MSG_INFO_SIZE
        anls_was_per_save_exc_msg_ver1(
            instream, file_local_offset, outstream, version)
        looper = looper + 1


def anls_was_save_nas_msg_vers_02(instream, file_offset, outstream,
                                  handled_msg_num, version):
    looper = 0

    outstream.writelines(["%-20s%-15s%-60s%-10s\n" % (
        "send_pid", "receive_pid", "msg_id", "tick")])

    while looper < MACRO_WAS_MNTN_REC_NAS_MSG_INFO_MAX_CNT:
        looper_index = (
            looper + handled_msg_num) % MACRO_WAS_MNTN_REC_NAS_MSG_INFO_MAX_CNT
        file_local_offset = file_offset + \
            looper_index * MACRO_WAS_SAVE_EXC_MSG_INFO_SIZE
        anls_was_per_save_exc_msg_ver1(
            instream, file_local_offset, outstream, version)
        looper = looper + 1


def anls_was_mntn_save_msgid_queue(instream, file_offset, outstream,
                                   msg_id_in_queue_num):
    looper = 0

    outstream.writelines(["%-17s\n" % ("aul_msg_id_in_queue[10] := {")])

    while looper < MACRO_WAS_SAVE_MSG_IN_QUEUE_MAX_NUM:
        looper_index = (
            looper + msg_id_in_queue_num) % MACRO_WAS_SAVE_MSG_IN_QUEUE_MAX_NUM
        file_local_offset = file_offset + looper_index
        instream.seek(file_local_offset)

        (msg_id_in_queue,) = struct.unpack('I', instream.read(4))
        outstream.writelines(["0x%-17x" % (msg_id_in_queue)])

        if 3 == looper % 4:
            outstream.writelines("\n")

        looper = looper + 1

    outstream.writelines(["%s\n" % ("}")])


def anls_was_mntn_save_fsm_state(instream, file_offset, outstream):
    looper = 0

    outstream.writelines(
        ["%-20s%-15s%-60s\n" % ("fsm_id", "main_state", "sub_state")])

    while looper < MACRO_WAS_SAVE_FSM_IN_STACK_MAX_NUM:
        file_local_offset = file_offset + \
            looper * MACRO_WAS_SAVE_EXC_MSG_INFO_SIZE
        instream.seek(file_local_offset)
        (fsm_id,) = struct.unpack('H', instream.read(2))
        (main_state,) = struct.unpack('H', instream.read(2))
        (sub_state,) = struct.unpack('H', instream.read(2))
        outstream.writelines(
            ["%-20s%-15s%-60s\n" % (fsm_id, main_state, sub_state)])
        looper = looper + 1


def anls_was_modem0_dump_vers_01(instream, file_offset, outstream):
    outstream.writelines(
        SEPA_START + " modem0 was debug msg list vers 01 " + SEPA_END)

    instream.seek(file_offset + \
        MACRO_WAS_SAVE_EXC_MSG_INFO_SIZE * MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT)

    (handled_msg_num,) = struct.unpack('I', instream.read(4))
    outstream.writelines(
        ["%-15s0x%-7x\n" % ("handled_msg_num :", handled_msg_num)])

    anls_was_save_exc_msg_vers_01(instream, file_offset, outstream,
                                  handled_msg_num)

    outstream.writelines("\n")

    instream.seek(
        file_offset + MACRO_WAS_SAVE_EXC_MSG_INFO_SIZE * \
        MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT + 4 + \
        4 * MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT)

    (msg_id_in_queue_num,) = struct.unpack('I', instream.read(4))
    outstream.writelines(
        ["%-15s%-7x\n" % ("msg_id_in_queue_num :", msg_id_in_queue_num)])

    file_offset = file_offset + MACRO_WAS_SAVE_EXC_MSG_INFO_SIZE * \
        MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT + 4

    anls_was_mntn_save_msgid_queue(instream, file_offset, outstream,
                                   msg_id_in_queue_num)


def anls_was_modem0_dump_vers_02(instream, file_offset, outstream, version):
    outstream.writelines(
        SEPA_START + " modem%d was debug msg list vers 02 " % version + \
        SEPA_END)

    instream.seek(file_offset)
    # ##HandledMsg
    (handled_msg_num,) = struct.unpack('I', instream.read(4))

    outstream.writelines(
        ["%-15s0x%-7x\n" % ("handled_msg_index :",
        handled_msg_num % MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT)])

    file_offset = file_offset + 4

    anls_was_save_exc_msg_vers_02(
        instream, file_offset, outstream, handled_msg_num, version)

    outstream.writelines("\n")

    file_offset = file_offset + \
        MACRO_WAS_SAVE_EXC_MSG_INFO_SIZE * MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT

    instream.seek(file_offset)

    # ##HandledNasMsg
    (handled_nas_msg_num,) = struct.unpack('I', instream.read(4))
    outstream.writelines(
        ["%-15s0x%-7x\n" % ("handled_nas_msg_index :",
        handled_nas_msg_num % MACRO_WAS_MNTN_REC_NAS_MSG_INFO_MAX_CNT)])

    file_offset = file_offset + 4

    anls_was_save_nas_msg_vers_02(instream, file_offset, outstream,
                                  handled_nas_msg_num, version)

    outstream.writelines("\n")

    file_offset = file_offset + MACRO_WAS_SAVE_EXC_MSG_INFO_SIZE * \
        MACRO_WAS_MNTN_REC_NAS_MSG_INFO_MAX_CNT

    instream.seek(file_offset)

    # ##unhandledMsg
    (msg_id_in_queue_num,) = struct.unpack('I', instream.read(4))
    outstream.writelines(
        ["%-15s%-7x\n" % ("msg_id_in_queue_index :",
        msg_id_in_queue_num % MACRO_WAS_SAVE_MSG_IN_QUEUE_MAX_NUM)])

    file_offset = file_offset + 4

    anls_was_mntn_save_msgid_queue(instream, file_offset, outstream,
                                   msg_id_in_queue_num)
    outstream.writelines("\n")

    file_offset = file_offset + 4 * MACRO_WAS_SAVE_MSG_IN_QUEUE_MAX_NUM

    instream.seek(file_offset)

    # ##was wrr fsm state
    outstream.writelines(
        SEPA_START + " modem%d was wrr fsm " % version + SEPA_END)
    anls_was_mntn_save_fsm_state(instream, file_offset, outstream)

    outstream.writelines("\n")

    file_offset = file_offset + \
        MACRO_WAS_SAVE_EXC_MSG_INFO_SIZE * MACRO_WAS_SAVE_FSM_IN_STACK_MAX_NUM

    instream.seek(file_offset)
    # ##was sib fsm state
    outstream.writelines(
        SEPA_START + " modem%d was sib fsm " % version + SEPA_END)
    anls_was_mntn_save_fsm_state(instream, file_offset, outstream)

    outstream.writelines("\n")

    file_offset = file_offset + \
        MACRO_WAS_SAVE_EXC_MSG_INFO_SIZE * MACRO_WAS_SAVE_FSM_IN_STACK_MAX_NUM

    instream.seek(file_offset)
    # ##was csel fsm state
    outstream.writelines(
        SEPA_START + " modem%d was csel fsm " % version + SEPA_END)
    anls_was_mntn_save_fsm_state(instream, file_offset, outstream)

    outstream.writelines("\n")

    file_offset = file_offset + \
        MACRO_WAS_SAVE_EXC_MSG_INFO_SIZE * MACRO_WAS_SAVE_FSM_IN_STACK_MAX_NUM

    instream.seek(file_offset)
    # ##was rb fsm state
    outstream.writelines(
        SEPA_START + " modem%d was rm fsm " % version + SEPA_END)
    anls_was_mntn_save_fsm_state(instream, file_offset, outstream)

    outstream.writelines("\n")

    file_offset = file_offset + \
        MACRO_WAS_SAVE_EXC_MSG_INFO_SIZE * MACRO_WAS_SAVE_FSM_IN_STACK_MAX_NUM

    instream.seek(file_offset)

    # ##was bg fsm state
    outstream.writelines(
        SEPA_START + " modem%d was bg fsm " % version + SEPA_END)
    anls_was_mntn_save_fsm_state(instream, file_offset, outstream)

    outstream.writelines("\n")


def analysis_gas_modem_x_dump_info(instream, file_offset, outstream, version,
                                   modem_no):
    # ##### analysis gas debug msg list ########
    outstream.writelines(
        [SEPA_START + " modem%d gas debug msg list " % modem_no + SEPA_END])
    file_offset = file_offset + MACRO_GAS_DEBUG_VERSION_LENGTH
    analysis_gas_modem_x_msg_list(instream, file_offset, outstream, modem_no)

    outstream.writelines(
        [SEPA_START + " modem%d gas nas msg list " % modem_no + SEPA_END])
    file_offset1 = file_offset + 8 + \
        MACRO_GAS_MNTN_REC_MSG_INFO_SIZE * MACRO_GAS_MNTN_REC_MSG_INFO_MAX_CNT
    anls_gas_modem_x_nas_msg_list(instream, file_offset1, outstream, modem_no)

    # ##### analysis gasm global status ########
    outstream.writelines(
        [SEPA_START + " modem%d GASM global status " % modem_no + SEPA_END])
    file_offset = file_offset + MACRO_GAS_DEBUG_MSG_LIST_LENGTH
    anls_modem_x_gasm_glob_sta(instream, file_offset, outstream)

    # ##### analysis gcomc global status #######
    outstream.writelines(
        [SEPA_START + " modem%d GCOMC global status " % modem_no + SEPA_END])
    file_offset = file_offset + MACRO_GAS_GASM_GLOBAL_STATUS_LENGTH
    anls_modem_x_gcomc_glob_sta(instream, file_offset, outstream)

    # ##### analysis gcomsi global status ######
    outstream.writelines(
        [SEPA_START + " modem%d GCOMSI global status " % modem_no + SEPA_END])
    file_offset = file_offset + MACRO_GAS_GCOMC_GLOBAL_STATUS_LENGTH
    anls_modem_x_gcomsi_glob_sta(instream, file_offset, outstream)

    # ##### analysis gcomm global status #######
    outstream.writelines(
        [SEPA_START + " modem%d GCOMM global status " % modem_no + SEPA_END])
    file_offset = file_offset + MACRO_GAS_GCOMSI_GLOBAL_STATUS_LENGTH
    anls_modem_x_gcomm_glob_sta(instream, file_offset, outstream, version)

    # ##### analysis rr global status ##########
    outstream.writelines(
        [SEPA_START + " modem%d RR global status " % modem_no + SEPA_END])
    file_offset = file_offset + MACRO_GAS_GCOMM_GLOBAL_STATUS_LENGTH
    anls_modem_x_rr_glob_sta(instream, file_offset, outstream)

    # ##### analysis grr global status #########
    outstream.writelines(
        [SEPA_START + " modem%d GRR global status " % modem_no + SEPA_END])
    file_offset = file_offset + MACRO_GAS_RR_GLOBAL_STATUS_LENGTH
    anls_modem_x_grr_glob_sta(instream, file_offset, outstream)


def analysis_was_dump_info(infile, offset, outfile):
    instream = infile
    outstream = outfile
    file_offset = eval(offset)

    # ##### analysis guas debug version ########
    vers_no = analysis_was_debug_version(instream, file_offset, outstream)

    # ### gas modem0 #########

    # #### was modem0 #########
    file_offset = eval(offset) + MACRO_WAS_DEBUG_VERSION_LENGTH
    anls_was_modem0_dump_vers_02(instream, file_offset, outstream, 0)

    if MACRO_VERSION_NO_4 > vers_no:
        # #### gas modem1 #########

        # #### was modem1 #########
        modem1_was_offset = eval(
            offset) + MACRO_MODEM0_ADDR_LENGTH + MACRO_WAS_DEBUG_VERSION_LENGTH
        anls_was_modem0_dump_vers_02(instream, modem1_was_offset, outstream, 1)

        # #### gas modem2 #########

    return True


###############################################################################
def entry_0x2200017(infile, field, offset, length, version, mode, outfile):
    # #######check parameter start#############
    if not field == '0x2200017':
        print("hidis field is %s." % (field))
        print("current field is 0x2200017.")
        return error['ERR_CHECK_FIELD']
    elif not version == '0x0000':
        print("hidis version is %s." % (version))
        print("current version is 0x0000.")
        return error['ERR_CHECK_VERSION']
    elif not length == '0x1000' or length == '0x800':
        print("hids length is %s." % (length))
        print("current length is 0x4000.")
        return error['ERR_CHECK_LEN']
    # #######check parameter end##############
    ret = analysis_was_dump_info(infile, offset, outfile)

    return 0

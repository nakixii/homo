#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
filename        :   analysis_guas_dump_bin.py
author          :   sunbing 00184266
description     :   analysis guas dump bin
modify  record  :   2016-01-07 create file
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
from gas.analyse_gas_global import analysis_modemX_gasm_global_status
from gas.analyse_gas_global import analysis_modemX_gcomc_global_status
from gas.analyse_gas_global import analysis_modemX_gcomm_global_status
from gas.analyse_gas_global import analysis_modemX_gcomsi_global_status
from gas.analyse_gas_global import analysis_modemX_grr_global_status
from gas.analyse_gas_global import analysis_modemX_rr_global_status
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
from gas_pid import guas_get_modem0_pid_str
from gas_pid import guas_get_modem1_pid_str
from vers_ctrl import analysis_guas_debug_version
from vers_ctrl import MACRO_GAS_DEBUG_VERSION_LENGTH
from vers_ctrl import MACRO_VERSION_NO_0
from vers_ctrl import MACRO_VERSION_NO_1
from vers_ctrl import MACRO_VERSION_NO_2
from vers_ctrl import MACRO_VERSION_NO_3
from vers_ctrl import MACRO_VERSION_NO_4

SEPA_START = "\n" + 25 * "*"
SEPA_END = "*" * 25 + "\n"

MACRO_GAS_MNTN_REC_MSG_INFO_MAX_CNT = 120
MACRO_GAS_MNTN_REC_MSG_INFO_SIZE = 8
MACRO_GAS_MNTN_REC_NAS_MSG_INFO_MAX_CNT = 60

MACRO_MODEM0_ADDR_LENGTH = 2048
MACRO_MODEM1_ADDR_LENGTH = 2048
MACRO_GAS_DEBUG_MSG_LIST_LENGTH = 968


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

    outstream.writelines(["%-15s%-15s%-60s0x%-10s\n" % (
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


def analysis_gas_mntn_rec_msg_info(instream, file_offset, outstream,
                                   msg_index, modem_no):
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
    analysis_gas_mntn_rec_msg_info(instream, file_offset, outstream,
                                   msg_index, modem_no)


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
    analysis_modemX_gasm_global_status(instream, file_offset, outstream)

    # ##### analysis gcomc global status #######
    outstream.writelines(
        [SEPA_START + " modem%d GCOMC global status " % modem_no + SEPA_END])
    file_offset = file_offset + MACRO_GAS_GASM_GLOBAL_STATUS_LENGTH
    analysis_modemX_gcomc_global_status(instream, file_offset, outstream)

    # ##### analysis gcomsi global status ######
    outstream.writelines(
        [SEPA_START + " modem%d GCOMSI global status " % modem_no + SEPA_END])
    file_offset = file_offset + MACRO_GAS_GCOMC_GLOBAL_STATUS_LENGTH
    analysis_modemX_gcomsi_global_status(instream, file_offset, outstream)

    # ##### analysis gcomm global status #######
    outstream.writelines(
        [SEPA_START + " modem%d GCOMM global status " % modem_no + SEPA_END])
    file_offset = file_offset + MACRO_GAS_GCOMSI_GLOBAL_STATUS_LENGTH
    analysis_modemX_gcomm_global_status(instream, file_offset, outstream,
                                        version)

    # ##### analysis rr global status ##########
    outstream.writelines(
        [SEPA_START + " modem%d RR global status " % modem_no + SEPA_END])
    file_offset = file_offset + MACRO_GAS_GCOMM_GLOBAL_STATUS_LENGTH
    analysis_modemX_rr_global_status(instream, file_offset, outstream)

    # ##### analysis grr global status #########
    outstream.writelines(
        [SEPA_START + " modem%d GRR global status " % modem_no + SEPA_END])
    file_offset = file_offset + MACRO_GAS_RR_GLOBAL_STATUS_LENGTH
    analysis_modemX_grr_global_status(instream, file_offset, outstream)


def analysis_gas_dump_info(infile, offset, outfile, vers_no):
    instream = infile
    outstream = outfile

    # ##### analysis guas debug info ########
    guas_vers_ctrl(vers_no, outstream)
    # ### gas modem0 #########
    file_offset = eval(offset)
    analysis_gas_modem_x_dump_info(instream, file_offset, outstream,
                                   vers_no, 0)

    if MACRO_VERSION_NO_4 > vers_no:
        # #### gas modem1 #########
        file_offset = eval(offset) + MACRO_MODEM0_ADDR_LENGTH
        analysis_gas_modem_x_dump_info(instream, file_offset, outstream,
                                       vers_no, 1)

        # #### gas modem2 #########
        file_offset = file_offset + MACRO_MODEM1_ADDR_LENGTH
        analysis_gas_modem_x_dump_info(instream, file_offset, outstream,
                                       vers_no, 2)

    return True

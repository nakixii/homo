#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list gcomsi global status
modify  record  :   2016-01-09 create file
"""

import struct
import string

MACRO_GCOMSI_L2_NCELL_PARALLEL_SEARCH_STATE_BUTT_INDEX      = 3
MACRO_GCOMSI_L2_INACTIVE_SCELL_BCCH_STATE_BUTT_INDEX        = 5
MACRO_GCOMSI_L2_INACTIVE_PARALLEL_SEARCH_STATE_BUTT_INDEX   = 3

MACRO_GCOMSI_FSM_L2_INACTIVE_SCELL_BCCH_INDEX               = 0x29
MACRO_GCOMSI_FSM_L2_INACTIVE_PARALLEL_SEARCH_INDEX          = 0x2A
MACRO_GCOMSI_FSM_L2_NCELL_PARALLEL_SEARCH_INDEX             = 0x2B

gas_gcomsi_l1_state_enum_table = {
0x00 : "GAS_GCOMSI_STATE_SCELL_INACTIVE",
0x01 : "GAS_GCOMSI_STATE_SCELL_BCCH",
0x02 : "GAS_GCOMSI_STATE_SCELL_PBCCH",
0x03 : "GAS_GCOMSI_STATE_SCELL_NORMAL",
0x04 : "GAS_GCOMSI_STATE_SCELL_DEDICATE",
0xFE : "GAS_GCOMSI_STATE_INIT",
0xFF : "GAS_GCOMSI_STATE_NULL",
}

gas_gcomsi_l2_fsm_enum_table = {
0x20 : "GAS_GCOMSI_FSM_L2_SCELL_GSM_PERIOD",
0x21 : "GAS_GCOMSI_FSM_L2_SCELL_GPRS_PERIOD",
0x22 : "GAS_GCOMSI_FSM_L2_NCELL_BCCH_PERIOD",
0x23 : "GAS_GCOMSI_FSM_L2_NCELL_BCCH",
0x24 : "GAS_GCOMSI_FSM_L2_SCELL_PACKET_SI_STATUS",
0x25 : "GAS_GCOMSI_FSM_L2_SCELL_BCCH_ENH_RECEIVE",
0x26 : "GAS_GCOMSI_FSM_L2_SCELL_NORMAL_BG_NCELL_BCCH",
0x27 : "GAS_GCOMSI_FSM_L2_INACTIVE_BG_NCELL_BCCH",
0x28 : "GAS_GCOMSI_FSM_L2_INACTIVE_SEARCH_BCCH",
0x29 : "GAS_GCOMSI_FSM_L2_INACTIVE_SCELL_BCCH",
0x2A : "GAS_GCOMSI_FSM_L2_INACTIVE_PARALLEL_SEARCH",
0x2B : "GAS_GCOMSI_FSM_L2_NCELL_PARALLEL_SEARCH",
0xFF : "GAS_GCOMSI_FSM_L2_NULL",
}

gas_gcomsi_l2_state_enum_table = {
0xFE  : "GAS_GCOMSI_STATE_INIT",
0xFF  : "GAS_GCOMSI_STATE_NULL",
0x200 : "GAS_GCOMSI_STATE_L2_SCELL_GSM_PERIOD_READING_BCCH",
0x210 : "GAS_GCOMSI_STATE_L2_SCELL_GPRS_PERIOD_READING_BCCH",
0x211 : "GAS_GCOMSI_STATE_L2_SCELL_GPRS_PERIOD_READING_PBCCH",
0x212 : "GAS_GCOMSI_STATE_L2_SCELL_GPRS_PERIOD_RCVPSI13_INTRANSFER",
0x213 : "GAS_GCOMSI_STATE_L2_SCELL_GPRS_PERIOD_RCVPSI1_INTRANSFER",
0x214 : "GAS_GCOMSI_STATE_L2_SCELL_GPRS_PERIOD_WAITTING_READ_PBCCH",
0x220 : "GAS_GCOMSI_STATE_L2_NCELL_BCCH_PERIOD_READING_BCCH",
0x221 : "GAS_GCOMSI_STATE_L2_NCELL_BCCH_PERIOD_START_GPHY",
0x222 : "GAS_GCOMSI_STATE_L2_NCELL_BCCH_PERIOD_STOP_GPHY",
0x230 : "GAS_GCOMSI_STATE_L2_NCELL_BCCH_READING_BCCH",
0x231 : "GAS_GCOMSI_STATE_L2_NCELL_BCCH_READING_PBCCH",
0x232 : "GAS_GCOMSI_STATE_L2_NCELL_BCCH_BCCH_SYNC",
0x240 : "GAS_GCOMSI_STATE_L2_SCELL_PACKET_SI_STATUS_SEND_MSG",
0x241 : "GAS_GCOMSI_STATE_L2_SCELL_PACKET_SI_STATUS_SCV_PSCD",
0x260 : "GAS_GCOMSI_STATE_L2_SCELL_NORMAL_BG_NCELL_BCCH_SYNC",
0x261 : "GAS_GCOMSI_STATE_L2_SCELL_NORMAL_BG_NCELL_BCCH_READING_BCCH",
0x270 : "GAS_GCOMSI_STATE_L2_INACTIVE_BG_NCELL_BCCH_SYNC",
0x271 : "GAS_GCOMSI_STATE_L2_INACTIVE_BG_NCELL_BCCH_READING_BCCH",
0x272 : "GAS_GCOMSI_STATE_L2_INACTIVE_BG_NCELL_BCCH_SYNC_ABNORMAL",
0x273 : "GAS_GCOMSI_STATE_L2_INACTIVE_BG_NCELL_BCCH_STOP_READING_BCCH",
0x274 : "GAS_GCOMSI_STATE_L2_INACTIVE_BG_NCELL_BCCH_SYNC_INTERRUPTED",
0x275 : "GAS_GCOMSI_STATE_L2_INACTIVE_BG_NCELL_BCCH_READING_BCCH_INTERRUPTED",
}

gas_gcomsi_l2_ncell_parallel_search_state_enum_table = {
0x0 : "GAS_GCOMSI_STATE_L2_NCELL_PARALLEL_SEARCH_START_GPHY",
0x1 : "GAS_GCOMSI_STATE_L2_NCELL_PARALLEL_SEARCH_BCCH_READING",
0x2 : "GAS_GCOMSI_STATE_L2_NCELL_PARALLEL_SEARCH_STOP_GPHY",
0x3 : "GAS_GCOMSI_STATE_L2_NCELL_PARALLEL_SEARCH_BUTT",
}

gas_gcomsi_l2_inactive_scell_bcch_state_enum_table = {
0x0 : "GAS_GCOMSI_STATE_L2_INACTIVE_SCELL_BCCH_WAIT_BSIC_SI,",
0x1 : "GAS_GCOMSI_STATE_L2_INACTIVE_SCELL_BCCH_WAIT_RSP_BY_ACTIVE_READ",
0x2 : "GAS_GCOMSI_STATE_L2_INACTIVE_SCELL_BCCH_WAIT_RSP_BY_NACC",
0x3 : "GAS_GCOMSI_STATE_L2_INACTIVE_SCELL_BCCH_WAIT_FULL_ESSENTIAL_SI",
0x4 : "GAS_GCOMSI_STATE_L2_INACTIVE_SCELL_BCCH_WAIT_FULL_ESSENTIAL_PSI",
0x5 : "GAS_GCOMSI_STATE_L2_INACTIVE_SCELL_BCCH_BUTT",
}

gas_gcomsi_l2_inactive_parallel_search_state_enum_table = {
0x0 : "GAS_GCOMSI_STATE_L2_INACTIVE_PARALLEL_SEARCH_START_GPHY",
0x1 : "GAS_GCOMSI_STATE_L2_INACTIVE_PARALLEL_SEARCH_BCCH_READING",
0x2 : "GAS_GCOMSI_STATE_L2_INACTIVE_PARALLEL_SEARCH_STOP_GPHY",
0x3 : "GAS_GCOMSI_STATE_L2_INACTIVE_PARALLEL_SEARCH_BUTT"
}

def get_gcomsi_l1_state( ulState):
    for index in gas_gcomsi_l1_state_enum_table.keys():
        if index == ulState:
            return gas_gcomsi_l1_state_enum_table[index]

    return "none"

def get_gcomsi_l2_fsm( ulFsm):
    for index in gas_gcomsi_l2_fsm_enum_table.keys():
        if index == ulFsm:
            return gas_gcomsi_l2_fsm_enum_table[index]

    return "none"

def get_gcomsi_l2_state( ulFsm, ulState):
    if ( MACRO_GCOMSI_FSM_L2_INACTIVE_SCELL_BCCH_INDEX == ulFsm):
        for index in gas_gcomsi_l2_inactive_scell_bcch_state_enum_table.keys():
            if index == ulState:
                return gas_gcomsi_l2_inactive_scell_bcch_state_enum_table[index]

        return gas_gcomsi_l2_inactive_scell_bcch_state_enum_table[MACRO_GCOMSI_L2_INACTIVE_SCELL_BCCH_STATE_BUTT_INDEX]
    elif ( MACRO_GCOMSI_FSM_L2_INACTIVE_PARALLEL_SEARCH_INDEX == ulFsm):
        for index in gas_gcomsi_l2_inactive_parallel_search_state_enum_table.keys():
            if index == ulState:
                return gas_gcomsi_l2_inactive_parallel_search_state_enum_table[index]

        return gas_gcomsi_l2_inactive_parallel_search_state_enum_table[MACRO_GCOMSI_L2_INACTIVE_PARALLEL_SEARCH_STATE_BUTT_INDEX]
    elif ( MACRO_GCOMSI_FSM_L2_NCELL_PARALLEL_SEARCH_INDEX == ulFsm):
        for index in gas_gcomsi_l2_ncell_parallel_search_state_enum_table.keys():
            if index == ulState:
                return gas_gcomsi_l2_ncell_parallel_search_state_enum_table[index]

        return gas_gcomsi_l2_ncell_parallel_search_state_enum_table[MACRO_GCOMSI_L2_NCELL_PARALLEL_SEARCH_STATE_BUTT_INDEX]
    else:
        for index in gas_gcomsi_l2_fsm_enum_table.keys():
            if index == ulFsm:
                return gas_gcomsi_l2_fsm_enum_table[index]

    return "none"

def analysis_modemX_gcomsi_global_status( instream, fileOffset, outstream):
        instream.seek(fileOffset)

        (ulGcomsiCurrFsmL1Sta,) = struct.unpack('I', instream.read(4))
        stGcomsiCurrFsmL1Sta    = get_gcomsi_l1_state(ulGcomsiCurrFsmL1Sta)
        stGcomsiCurrFsmL1Sta    = '%s(0x%x)' % ( stGcomsiCurrFsmL1Sta, ulGcomsiCurrFsmL1Sta)
        outstream.writelines(["%-15s%-7s\n" % ("ulGcomsiCurrFsmL1Sta :", stGcomsiCurrFsmL1Sta)])

        (ulGcomsiCurrFsmL2,) = struct.unpack('I', instream.read(4))
        stGcomsiCurrFsmL2    = get_gcomsi_l2_fsm(ulGcomsiCurrFsmL2)
        stGcomsiCurrFsmL2    = '%s(0x%x)' % ( stGcomsiCurrFsmL2, ulGcomsiCurrFsmL2)
        outstream.writelines(["%-15s%-7s\n" % ("ulGcomsiCurrFsmL2 :", stGcomsiCurrFsmL2)])

        (ulGcomsiCurrFsmL2Sta,) = struct.unpack('I', instream.read(4))
        stGcomsiCurrFsmL2Sta    = get_gcomsi_l2_state( ulGcomsiCurrFsmL2, ulGcomsiCurrFsmL2Sta)
        stGcomsiCurrFsmL2Sta    = '%s(0x%x)' % ( stGcomsiCurrFsmL2Sta, ulGcomsiCurrFsmL2Sta)
        outstream.writelines(["%-15s%-7s\n" % ("ulGcomsiCurrFsmL2Sta :", stGcomsiCurrFsmL2Sta)])

        (ulGcomsiInitFsmL2MsgType,) = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s0x%-7x\n" % ("ulGcomsiInitFsmL2MsgType :", ulGcomsiInitFsmL2MsgType)])

        (ulGcomsiStopFsmL2Level,) = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s0x%-7x\n" % ("ulGcomsiStopFsmL2Level :", ulGcomsiStopFsmL2Level)])

        (ucGcomsiCachedExistMsgFlag,)     = struct.unpack('>B', instream.read(1))
        outstream.writelines(["%-15s0x%-7x\n" % ("ucGcomsiCachedExistMsgFlag :", ucGcomsiCachedExistMsgFlag)])

        (gcomc_space,)   = struct.unpack('>B', instream.read(1))
        (gcomc_space,)   = struct.unpack('>B', instream.read(1))
        (gcomc_space,)   = struct.unpack('>B', instream.read(1))

        (ulGcomsiCachedMsgEventType,)     = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s0x%-7x\n" % ("ulGcomsiCachedMsgEventType :", ulGcomsiCachedMsgEventType)])
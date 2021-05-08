#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list rr global status
modify  record  :   2016-01-09 create file
"""

import struct
import string

gas_rr_main_state_enum_table = {
0x0 : "GAS_RR_MAINSTATE_IDLE",
0x1 : "GAS_RR_MAINSTATE_DEDICATED",
0x2 : "GAS_RR_MAINSTATE_UNSTABLE",
}

gas_rr_sub_state_enum_table = {
0x0F : "GAS_RR_SUBSTATE_ESP_SAP3",
0x10 : "GAS_RR_SUBSTATE_ACCESSING",
0x11 : "GAS_RR_SUBSTATE_TERMINATING",
0x12 : "GAS_RR_SUBSTATE_ACCESS_FAILURE",
0x13 : "GAS_RR_SUBSTATE_APPLY_ACCESSING",
0x14 : "GAS_RR_SUBSTATE_ASSIGN_CMD_FAILURE",
0x15 : "GAS_RR_SUBSTATE_INTRA_HANDOVER_PHY_STEP1",
0x16 : "GAS_RR_SUBSTATE_INTRA_HANDOVER_PHY_STEP2",
0x17 : "GAS_RR_SUBSTATE_INTRA_HANDOVER_PHY",
0x18 : "GAS_RR_SUBSTATE_SET_MASTER_MODE",
0x19 : "GAS_RR_SUBSTATE_ROLLBACK_SET_SLAVE_MODE",
0x1A : "GAS_RR_SUBSTATE_INTER_HANDOVER_FAILURE",
0x1B : "GAS_RR_SUBSTATE_NAS_SUSPEND",
0x1C : "GAS_RR_SUBSTATE_NAS_RESUME",
0x1D : "GAS_RR_SUBSTATE_WAIT_DL_NACK_DATA",
0x1E : "GAS_RR_SUBSTATE_WAIT_RF_RES_CNF",
0x30 : "GAS_RR_SUBSTATE_RECONSTRUCT_PHY",
0x31 : "GAS_RR_SUBSTATE_RECONSTRUCT_DL",
0x32 : "GAS_RR_SUBSTATE_RECONSTRUCT_FAILUER",
0x33 : "GAS_RR_SUBSTATE_RECONSTRUCT_FAIL_RESUMING_NAS",
0x34 : "GAS_RR_SUBSTATE_RECONSTRUCT_SUCCESS_RESUMING_NAS",
0x70 : "GAS_RR_SUBSTATE_PHY_ACTIVATING",
0x71 : "GAS_RR_SUBSTATE_PHY_DEACTIVATING",
0x72 : "GAS_RR_SUBSTATE_PHY_CIPHER",
0x73 : "GAS_RR_SUBSTATE_PHY_CHMODE",
0x74 : "GAS_RR_SUBSTATE_PHY_FREQ_REDEF",
0x75 : "GAS_RR_SUBSTATE_PHY_ABNORMAL",
0x76 : "GAS_RR_SUBSTATE_PHY_BHO_FB_SB",
0x77 : "GAS_RR_SUBSTATE_PHY_STOP_BHO_FB_SB",
0x78 : "GAS_RR_SUBSTATE_PHY_REL_ALL",
0x79 : "GAS_RR_SUBSTATE_SET_SLAVE_MODE",
0x7A : "GAS_RR_SUBSTATE_ROLLBACK_SET_MASTER_MODE",
0x7B : "GAS_RR_SUBSTATE_STOP_PHY_DEACTIVATING",
0x7C : "GAS_RR_SUBSTATE_STOP_PHY_REL_ALL",
0x7D : "GAS_RR_SUBSTATE_STOP_SET_SLAVE_MODE",
0x7E : "GAS_RR_SUBSTATE_WAIT_HO_STOP_CNF",
0x80 : "GAS_RR_SUBSTATE_DL_EST",
0x81 : "GAS_RR_SUBSTATE_DL_SUSP",
0x82 : "GAS_RR_SUBSTATE_DL_RESUME",
0x83 : "GAS_RR_SUBSTATE_DL_RECONN",
0x84 : "GAS_RR_SUBSTATE_DL_REL",
0x85 : "GAS_RR_SUBSTATE_DL_ABNORMAL",
0x86 : "GAS_RR_SUBSTATE_INTER_HANDOVER",
0x90 : "GAS_RR_SUBSTATE_GASM_ACTIVATING",
0xFE : "GAS_RR_SUBSTATE_FSM_INIT",
0xFF : "GAS_RR_SUBSTATE_FSM_NULL",
}

def get_rr_main_state( ucRrCurMainState):
    for index in gas_rr_main_state_enum_table.keys():
        if index == ucRrCurMainState:
            return gas_rr_main_state_enum_table[index]

    return "none"

def get_rr_sub_state( ucRrSubState):
    for index in gas_rr_sub_state_enum_table.keys():
        if index == ucRrSubState:
            return gas_rr_sub_state_enum_table[index]

    return "none"

def analysis_modemX_rr_global_status( instream, fileOffset, outstream):
        instream.seek(fileOffset)

        (ucRrCurMainState,)     = struct.unpack('>B', instream.read(1))
        stRrCurMainState        = get_rr_main_state(ucRrCurMainState)
        stRrCurMainState        = '%s(0x%x)' % ( stRrCurMainState, ucRrCurMainState)
        outstream.writelines(["%-15s%-7s\n" % ("ucRrCurMainState :", stRrCurMainState)])

        (ucRrCurSubState,)      = struct.unpack('>B', instream.read(1))
        stRrCurSubState         = get_rr_sub_state(ucRrCurSubState)
        stRrCurSubState         = '%s(0x%x)' % ( stRrCurSubState, ucRrCurSubState)
        outstream.writelines(["%-15s%-7s\n" % ("ucRrCurSubState :", stRrCurSubState)])

        (gcomc_space,)   = struct.unpack('>B', instream.read(1))
        (gcomc_space,)   = struct.unpack('>B', instream.read(1))

        (ulRrCachedEventType,) = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s0x%-7x\n" % ("ulRrCachedEventType :", ulRrCachedEventType)])
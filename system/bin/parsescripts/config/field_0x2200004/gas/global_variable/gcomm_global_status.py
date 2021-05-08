#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list gcomm global status
modify  record  :   2016-01-07 create file
"""

import struct
import string

MACRO_GCOMM_FSM_L2_FDD_MEAS_INDEX               = 0x3
MACRO_GCOMM_FSM_L2_TDD_MEAS_INDEX               = 0x2

MACRO_GCOMM_FSM_L2_STATUS_BUTT_INDEX            = 0xFF

gas_gcomm_l1_state_enum_table = {
0x01 : "GAS_GCOMM_INACTIVE_STAT",
0x02 : "GAS_GCOMM_GSM_IDLE_MEAS_STAT",
0x03 : "GAS_GCOMM_GSM_DEDICATED_MEAS_STAT",
0x04 : "GAS_GCOMM_GPRS_RESEL_MEAS_STAT",
0x05 : "GAS_GCOMM_GPRS_NC_MEAS_STAT",
0x06 : "GAS_GCOMM_STAT_BUTT",
}

gas_gcomm_l2_state_enum_table = {
0x21 : "GAS_GCOMM_L2_STATE_LTE_IDLE_MEAS_WAIT_LRRC_MEAS_CNF",
0x22 : "GAS_GCOMM_L2_STATE_LTE_IDLE_MEAS_WAIT_GPHY_MEAS_CNF",
0x23 : "GAS_GCOMM_L2_STATE_LTE_IDLE_MEAS_WAIT_LRRC_MEAS_IND",
0x24 : "GAS_GCOMM_L2_STATE_LTE_IDLE_MEAS_WAIT_MEAS_PT_EXP",
0x25 : "GAS_GCOMM_L2_STATE_LTE_IDLE_MEAS_WAIT_GPHY_STOP_MEAS_CNF",
0x26 : "GAS_GCOMM_L2_STATE_LTE_IDLE_MEAS_WAIT_LRRC_STOP_MEAS_CNF",
0x31 : "GAS_GCOMM_L2_STATE_LTE_CONNECT_MEAS_WAIT_LRRC_MEAS_CNF",
0x32 : "GAS_GCOMM_L2_STATE_LTE_CONNECT_MEAS_WAIT_GPHY_MEAS_CNF",
0x33 : "GAS_GCOMM_L2_STATE_LTE_CONNECT_MEAS_WAIT_LRRC_MEAS_IND",
0x34 : "GAS_GCOMM_L2_STATE_LTE_CONNECT_MEAS_WAIT_MEAS_PT_EXP",
0x35 : "GAS_GCOMM_L2_STATE_LTE_CONNECT_MEAS_WAIT_GPHY_STOP_MEAS_CNF",
0x36 : "GAS_GCOMM_L2_STATE_LTE_CONNECT_MEAS_WAIT_LRRC_STOP_MEAS_CNF",
0xFE : "GAS_GCOMM_L2_STATE_INIT",
0xFF : "GAS_GCOMM_L2_STATE_NULL",
}

gas_gcomm_l2_fdd_meas_state_enum_table = {
0x1 : "GAS_GCOMM_L2_STATE_FDD_MEAS_STARTUP_WRRC",
0x2 : "GAS_GCOMM_L2_STATE_FDD_MEAS_STARTUP_GPHY",
0x3 : "GAS_GCOMM_L2_STATE_FDD_MEAS_WAIT_WRRC_MEAS_IND",
0x4 : "GAS_GCOMM_L2_STATE_FDD_MEAS_READY_TO_RELEASE",
0x5 : "GAS_GCOMM_L2_STATE_FDD_MEAS_RELEASE_GPHY",
0x6 : "GAS_GCOMM_L2_STATE_FDD_MEAS_RELEASE_WRRC",
}

gas_gcomm_l2_tds_meas_state_enum_table = {
0x1 : "GAS_GCOMM_L2_STATE_TDS_MEAS_STARTUP_TRRC",
0x2 : "GAS_GCOMM_L2_STATE_TDS_MEAS_STARTUP_GPHY",
0x3 : "GAS_GCOMM_L2_STATE_TDS_MEAS_WAIT_TRRC_MEAS_IND",
0x4 : "GAS_GCOMM_L2_STATE_TDS_MEAS_READY_TO_RELEASE",
0x5 : "GAS_GCOMM_L2_STATE_TDS_MEAS_RELEASE_GPHY",
0x6 : "GAS_GCOMM_L2_STATE_TDS_MEAS_RELEASE_TRRC",
}

gas_gcomm_l2_fsm_enum_table = {
0x0 : "GAS_GCOMM_FSM_IDLE_LTE_MEASURE",
0x1 : "GAS_GCOMM_FSM_CONNECT_LTE_MEASURE",
0x2 : "GAS_GCOMM_FSM_TDS_MEASURE",
0x3 : "GAS_GCOMM_FSM_FDD_MEASURE",
0x4 : "GAS_GCOMM_FSM_BUTT",
}

gas_gcomm_stop_meas_manner_enum_table = {
0x0 : "GAS_GCOMM_STOP_MEAS_MANNER_NEED_NO_STOP_CNF",
0x1 : "GAS_GCOMM_STOP_MEAS_MANNER_NEED_STOP_CNF",
0x2 : "GAS_GCOMM_STOP_MEAS_MANNER_BUTT",
}

def get_gcomm_l1_state( ulState):
    for index in gas_gcomm_l1_state_enum_table.keys():
        if index == ulState:
            return gas_gcomm_l1_state_enum_table[index]

    return "none"

def get_gcomm_l2_fsm( ulFsm):
    for index in gas_gcomm_l2_fsm_enum_table.keys():
        if index == ulFsm:
            return gas_gcomm_l2_fsm_enum_table[index]

    return "none"

def get_gcomm_l2_interrupt_type( enInterruptType):
    for index in gas_gcomm_stop_meas_manner_enum_table.keys():
        if index == enInterruptType:
            return gas_gcomm_stop_meas_manner_enum_table[index]

    return "none"

def get_gcomm_l2_state( ulFsm, ulState):
    if ( MACRO_GCOMM_FSM_L2_FDD_MEAS_INDEX == ulFsm):
        for index in gas_gcomm_l2_fdd_meas_state_enum_table.keys():
            if index == ulState:
                return gas_gcomm_l2_fdd_meas_state_enum_table[index]
    elif ( MACRO_GCOMM_FSM_L2_TDD_MEAS_INDEX == ulFsm):
        for index in gas_gcomm_l2_tds_meas_state_enum_table.keys():
            if index == ulState:
                return gas_gcomm_l2_tds_meas_state_enum_table[index]
    else:
        for index in gas_gcomm_l2_state_enum_table.keys():
            if index == ulState:
                return gas_gcomm_l2_state_enum_table[index]

    return gas_gcomm_l2_state_enum_table[MACRO_GCOMM_FSM_L2_STATUS_BUTT_INDEX]

def analysis_modemX_gcomm_global_status( instream, fileOffset, outstream, vers_no):
        instream.seek(fileOffset)

        if ( vers_no < 3):
            (enGcommSta,) = struct.unpack('I', instream.read(4))
            strGcommSta   = get_gcomm_l1_state(enGcommSta)
            strGcommSta   = '%s(0x%x)' % ( strGcommSta, enGcommSta)
            outstream.writelines(["%-15s%-7s\n" % ("enGcommSta :", strGcommSta)])

            (usGcommL2Sta,) = struct.unpack('H', instream.read(2))

            (enGcommFsmL2Id,) = struct.unpack('H', instream.read(2))
            strGcommFsmL2Id   = get_gcomm_l2_fsm(enGcommFsmL2Id)
            strGcommFsmL2Id   = '%s(0x%x)' % ( strGcommFsmL2Id, enGcommFsmL2Id)

            strGcommL2Sta   = get_gcomm_l2_state( enGcommFsmL2Id, usGcommL2Sta)
            strGcommL2Sta   = '%s(0x%x)' % ( strGcommL2Sta, usGcommL2Sta)

            outstream.writelines(["%-15s%-7s\n" % ("usGcommL2Sta :", strGcommL2Sta)])
            outstream.writelines(["%-15s%-7s\n" % ("enGcommFsmL2Id :", strGcommFsmL2Id)])

            (ulGcommEntryMsgEventType,) = struct.unpack('I', instream.read(4))
            outstream.writelines(["%-15s0x%-7x\n" % ("ulGcommEntryMsgEventType :", ulGcommEntryMsgEventType)])

            (enGcommL2InterruptType,) = struct.unpack('>B', instream.read(1))
            strGcommL2InterruptType   = get_gcomm_l2_interrupt_type(enGcommL2InterruptType)
            strGcommL2InterruptType   = '%s(0x%x)' % ( strGcommL2InterruptType, enGcommL2InterruptType)
            outstream.writelines(["%-15s%-7s\n" % ("enGcommL2InterruptType :", strGcommL2InterruptType)])

            (gcomc_space,)   = struct.unpack('>B', instream.read(1))
            (gcomc_space,)   = struct.unpack('>B', instream.read(1))
            (gcomc_space,)   = struct.unpack('>B', instream.read(1))
            (gcomc_space,)   = struct.unpack('>B', instream.read(1))
            (gcomc_space,)   = struct.unpack('>B', instream.read(1))

            (ucGcommCachedCounter,) = struct.unpack('>B', instream.read(1))
            outstream.writelines(["%-15s0x%-7x\n" % ("ucGcommCachedCounter :", ucGcommCachedCounter)])

            (ucGcommCachedCurMsgIndex,) = struct.unpack('>B', instream.read(1))
            outstream.writelines(["%-15s0x%-7x\n" % ("ucGcommCachedCurMsgIndex :", ucGcommCachedCurMsgIndex)])

            (ulGcommCachedEventType,) = struct.unpack('I', instream.read(4))
            outstream.writelines(["%-15s0x%-7x\n" % ("aulGcomcMsgQueueEventType[0] :", ulGcommCachedEventType)])

            (ulGcommCachedEventType,) = struct.unpack('I', instream.read(4))
            outstream.writelines(["%-15s0x%-7x\n" % ("aulGcomcMsgQueueEventType[1] :", ulGcommCachedEventType)])

            (ulGcommCachedEventType,) = struct.unpack('I', instream.read(4))
            outstream.writelines(["%-15s0x%-7x\n" % ("aulGcomcMsgQueueEventType[2] :", ulGcommCachedEventType)])

            (ulGcommCachedEventType,) = struct.unpack('I', instream.read(4))
            outstream.writelines(["%-15s0x%-7x\n" % ("aulGcomcMsgQueueEventType[3] :", ulGcommCachedEventType)])

            (ulGcommCachedEventType,) = struct.unpack('I', instream.read(4))
            outstream.writelines(["%-15s0x%-7x\n" % ("aulGcomcMsgQueueEventType[4] :", ulGcommCachedEventType)])

        else:
            (enGcommSta,) = struct.unpack('I', instream.read(4))
            strGcommSta   = get_gcomm_l1_state(enGcommSta)
            strGcommSta   = '%s(0x%x)' % ( strGcommSta, enGcommSta)
            outstream.writelines(["%-15s%-7s\n" % ("enGcommSta :", strGcommSta)])

            (usGcommL2Sta,) = struct.unpack('H', instream.read(2))

            (enGcommFsmL2Id,) = struct.unpack('H', instream.read(2))
            strGcommFsmL2Id   = get_gcomm_l2_fsm(enGcommFsmL2Id)
            strGcommFsmL2Id   = '%s(0x%x)' % ( strGcommFsmL2Id, enGcommFsmL2Id)

            strGcommL2Sta   = get_gcomm_l2_state( enGcommFsmL2Id, usGcommL2Sta)
            strGcommL2Sta   = '%s(0x%x)' % ( strGcommL2Sta, usGcommL2Sta)

            outstream.writelines(["%-15s%-7s\n" % ("usGcommL2Sta :", strGcommL2Sta)])
            outstream.writelines(["%-15s%-7s\n" % ("enGcommFsmL2Id :", strGcommFsmL2Id)])

            (ulGcommL2EntryMsgEventType,) = struct.unpack('I', instream.read(4))
            outstream.writelines(["%-15s0x%-7x\n" % ("ulGcommEntryMsgEventType :", ulGcommL2EntryMsgEventType)])

            (enGcommL2InterruptType,) = struct.unpack('>B', instream.read(1))
            strGcommL2InterruptType   = get_gcomm_l2_interrupt_type(enGcommL2InterruptType)
            strGcommL2InterruptType   = '%s(0x%x)' % ( strGcommL2InterruptType, enGcommL2InterruptType)
            outstream.writelines(["%-15s%-7s\n" % ("enGcommL2InterruptType :", strGcommL2InterruptType)])

            (gcomc_space,)   = struct.unpack('>B', instream.read(1))
            (gcomc_space,)   = struct.unpack('>B', instream.read(1))
            (gcomc_space,)   = struct.unpack('>B', instream.read(1))
            (gcomc_space,)   = struct.unpack('>B', instream.read(1))
            (gcomc_space,)   = struct.unpack('>B', instream.read(1))

            (usGcommL3Sta,) = struct.unpack('H', instream.read(2))

            (enGcommFsmL3Id,) = struct.unpack('H', instream.read(2))
            strGcommFsmL3Id   = get_gcomm_l2_fsm(enGcommFsmL3Id)
            strGcommFsmL3Id   = '%s(0x%x)' % ( strGcommFsmL3Id, enGcommFsmL3Id)

            strGcommL3Sta   = get_gcomm_l2_state( enGcommFsmL3Id, usGcommL3Sta)
            strGcommL3Sta   = '%s(0x%x)' % ( strGcommL3Sta, usGcommL3Sta)

            outstream.writelines(["%-15s%-7s\n" % ("usGcommL3Sta :", strGcommL3Sta)])
            outstream.writelines(["%-15s%-7s\n" % ("enGcommFsmL3Id :", strGcommFsmL3Id)])

            (gcomc_space,)   = struct.unpack('>B', instream.read(1))
            (gcomc_space,)   = struct.unpack('>B', instream.read(1))

            (ulGcommL3EntryMsgEventType,) = struct.unpack('I', instream.read(4))
            outstream.writelines(["%-15s0x%-7x\n" % ("ulGcommEntryMsgEventType :", ulGcommL3EntryMsgEventType)])

            (enGcommL3InterruptType,) = struct.unpack('>B', instream.read(1))
            strGcommL3InterruptType   = get_gcomm_l2_interrupt_type(enGcommL3InterruptType)
            strGcommL3InterruptType   = '%s(0x%x)' % ( strGcommL3InterruptType, enGcommL3InterruptType)
            outstream.writelines(["%-15s%-7s\n" % ("enGcommL2InterruptType :", strGcommL3InterruptType)])

            (gcomc_space,)   = struct.unpack('>B', instream.read(1))
            (gcomc_space,)   = struct.unpack('>B', instream.read(1))
            (gcomc_space,)   = struct.unpack('>B', instream.read(1))
            (gcomc_space,)   = struct.unpack('>B', instream.read(1))
            (gcomc_space,)   = struct.unpack('>B', instream.read(1))

            (ucGcommL2CachedCounter,) = struct.unpack('>B', instream.read(1))
            outstream.writelines(["%-15s0x%-7x\n" % ("ucGcommCachedCounter :", ucGcommL2CachedCounter)])

            (ucGcommL2CachedCurMsgIndex,) = struct.unpack('>B', instream.read(1))
            outstream.writelines(["%-15s0x%-7x\n" % ("ucGcommCachedCurMsgIndex :", ucGcommL2CachedCurMsgIndex)])

            (ulGcommL2CachedEventType,) = struct.unpack('I', instream.read(4))
            outstream.writelines(["%-15s0x%-7x\n" % ("aulGcomcMsgQueueEventType[0] :", ulGcommL2CachedEventType)])

            (ulGcommL2CachedEventType,) = struct.unpack('I', instream.read(4))
            outstream.writelines(["%-15s0x%-7x\n" % ("aulGcomcMsgQueueEventType[1] :", ulGcommL2CachedEventType)])

            (ulGcommL2CachedEventType,) = struct.unpack('I', instream.read(4))
            outstream.writelines(["%-15s0x%-7x\n" % ("aulGcomcMsgQueueEventType[2] :", ulGcommL2CachedEventType)])

            (ucGcommL3CachedCounter,) = struct.unpack('>B', instream.read(1))
            outstream.writelines(["%-15s0x%-7x\n" % ("ucGcommCachedCounter :", ucGcommL3CachedCounter)])

            (ucGcommL3CachedCurMsgIndex,) = struct.unpack('>B', instream.read(1))
            outstream.writelines(["%-15s0x%-7x\n" % ("ucGcommCachedCurMsgIndex :", ucGcommL3CachedCurMsgIndex)])

            (gcomc_space,)   = struct.unpack('>B', instream.read(1))
            (gcomc_space,)   = struct.unpack('>B', instream.read(1))

            (ulGcommL3CachedEventType,) = struct.unpack('I', instream.read(4))
            outstream.writelines(["%-15s0x%-7x\n" % ("aulGcomcMsgQueueEventType[0] :", ulGcommL3CachedEventType)])

            (ulGcommL3CachedEventType,) = struct.unpack('I', instream.read(4))
            outstream.writelines(["%-15s0x%-7x\n" % ("aulGcomcMsgQueueEventType[1] :", ulGcommL3CachedEventType)])

            (ulGcommL3CachedEventType,) = struct.unpack('I', instream.read(4))
            outstream.writelines(["%-15s0x%-7x\n" % ("aulGcomcMsgQueueEventType[2] :", ulGcommL3CachedEventType)])

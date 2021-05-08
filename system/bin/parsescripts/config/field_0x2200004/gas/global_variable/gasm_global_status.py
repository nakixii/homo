#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list gasm global status
modify  record  :   2016-01-09 create file
"""

import struct
import string

MACRO_GPHY_MASTER_MODE_BUTT_INDEX   = 0x5
MACRO_SIM_STATUS_BUTT_INDEX         = 0x3
MACRO_RAT_PRIO_BUTT_INDEX           = 0x4

gasm_gphy_master_mode_enum_table = {
0x0 : "GAS_MASTER_MODE_NONE",
0x1 : "GAS_MASTER_MODE_GSM",
0x2 : "GAS_MASTER_MODE_WCDMA",
0x3 : "GAS_MASTER_MODE_TDSCDMA",
0x4 : "GAS_MASTER_MODE_LTE",
0x5 : "GAS_MASTER_MODE_BUTT",
}

gasm_sim_status_enum_table = {
0x0 : "RRC_NAS_UICC_ABSENT",
0x1 : "RRC_NAS_USIM_PRESENT",
0x2 : "RRC_NAS_SIM_PRESET",
0x3 : "RRC_NAS_SIM_STATUS_BUTT",
}

gasm_rat_prio_enum_table = {
0x0 : "RRMM_RAT_PRIO_NULL",
0x1 : "RRMM_RAT_PRIO_LOW",
0x2 : "RRMM_RAT_PRIO_MIDDLE",
0x3 : "RRMM_RAT_PRIO_HIGH",
0x4 : "RRMM_RAT_PRIO_BUTT",
}

def get_gas_gphy_master_mode( enGphyMasterMode):
    for index in gasm_gphy_master_mode_enum_table.keys():
        if index == enGphyMasterMode:
            return gasm_gphy_master_mode_enum_table[index]

    return gasm_gphy_master_mode_enum_table[MACRO_GPHY_MASTER_MODE_BUTT_INDEX]

def get_gas_sim_status( ulSimStatus):
    for index in gasm_sim_status_enum_table.keys():
        if index == ulSimStatus:
            return gasm_sim_status_enum_table[index]

    return gasm_sim_status_enum_table[MACRO_SIM_STATUS_BUTT_INDEX]

def get_gas_rat_prio( enRatPrio):
    for index in gasm_rat_prio_enum_table.keys():
        if index == enRatPrio:
            return gasm_rat_prio_enum_table[index]

    return gasm_sim_status_enum_table[MACRO_RAT_PRIO_BUTT_INDEX]

def analysis_modemX_gasm_global_status( instream, fileOffset, outstream):
        instream.seek(fileOffset)

        (ulTimeStamp,)  = struct.unpack('I', instream.read(4))
        strTimeStamp    = '%x'% ulTimeStamp
        outstream.writelines(["%-15s0x%-7s\n" % ("ulTimeStamp :", strTimeStamp.upper())])

        (ulTick,)  = struct.unpack('I', instream.read(4))
        strTick    = '%x'% ulTick
        outstream.writelines(["%-15s0x%-7s\n" % ("ulTick :", strTick.upper())])

        (enGphyMasterMode,)     = struct.unpack('>B', instream.read(1))
        strGphyMasterMode       = get_gas_gphy_master_mode(enGphyMasterMode)
        strGphyMasterMode       = '%s(0x%x)' % ( strGphyMasterMode, enGphyMasterMode)
        outstream.writelines(["%-15s%-7s\n" % ("enGphyMasterMode :", strGphyMasterMode)])

        (gasm_space,)   = struct.unpack('>B', instream.read(1))
        (gasm_space,)   = struct.unpack('>B', instream.read(1))
        (gasm_space,)   = struct.unpack('>B', instream.read(1))
        (gasm_space,)   = struct.unpack('>B', instream.read(1))
        (gasm_space,)   = struct.unpack('>B', instream.read(1))
        (gasm_space,)   = struct.unpack('>B', instream.read(1))
        (gasm_space,)   = struct.unpack('>B', instream.read(1))

        (ulSimStatus,)  = struct.unpack('I', instream.read(4))
        strSimStatus    = get_gas_sim_status( ulSimStatus)
        strSimStatus    = '%s(0x%x)' % ( strSimStatus, ulSimStatus)
        outstream.writelines(["%-15s%-7s\n" % ("ulSimStatue :", strSimStatus)])

        (enGsmPrio,)    = struct.unpack('>B', instream.read(1))
        strGsmPrio      = get_gas_rat_prio( enGsmPrio)
        strGsmPrio      = '%s(0x%x)' % ( strGsmPrio, enGsmPrio)
        outstream.writelines(["%-15s%-7s\n" % ("enGsmPrio :", strGsmPrio)])

        (enUtranPrio,)  = struct.unpack('>B', instream.read(1))
        strUtranPrio    = get_gas_rat_prio( enUtranPrio)
        strUtranPrio    = '%s(0x%x)' % ( strUtranPrio, enUtranPrio)
        outstream.writelines(["%-15s%-7s\n" % ("enUtranPrio :", strUtranPrio)])

        (enLtePrio,)    = struct.unpack('>B', instream.read(1))
        strLtePrio      = get_gas_rat_prio( enLtePrio)
        strLtePrio      = '%s(0x%x)' % ( strLtePrio, enLtePrio)
        outstream.writelines(["%-15s%-7s\n" % ("enLtePrio :", strLtePrio)])

        (gasm_space,)   = struct.unpack('>B', instream.read(1))
        (gasm_space,)   = struct.unpack('>B', instream.read(1))
        (gasm_space,)   = struct.unpack('>B', instream.read(1))
        (gasm_space,)   = struct.unpack('>B', instream.read(1))
        (gasm_space,)   = struct.unpack('>B', instream.read(1))
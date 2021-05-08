#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (C) Huawei Technologies Co., Ltd. 2010-2018. All rights reserved.

import struct
import os
import sys
import string
from config import *

global g_StampEnumTable
global g_lastStampEnum
global g_lastStateStamp
global g_StampPrint2FileMark
#global myDdrOffset
global g_StampOffset
global g_IsTheFirst
global g_CountEnumTable
global g_CountStateMaxIndex
global g_FileOffset
global g_CpmState
global g_SleepFlag
global g_CpmWakeLock
global g_PhyState
g_StampEnumTable = {
        0: ("NRCPM_SLEEP_REQISR_0",         "Receive phy sleep req msg"),
        1: ("NRCPM_SLEEP_REQISR_1",         "Finish phy sleep req msg proc"),
        2: ("NRCPM_SLEEP_REQ_0",            "Receive Dsp sleep req"),
        3: ("NRCPM_SLEEP_REQ_1",            "allow Dsp sleep req"),
        4: ("NRCPM_FORBID_SLEEP_0",         "l2 don't allow Dsp sleep req"),
        5: ("NRCPM_FORBID_SLEEP_1",         "Don't allow Dsp sleep req"),
        6: ("NRCPM_FORBID_SLEEP_2",         "Measure flag is ture,don't allow Dsp sleep"),
        7: ("NRCPM_FORBID_SLEEP_3",         "Wake_lock flag is ture,don't allow Dsp sleep"),
        8: ("NRCPM_FORBID_SLEEP_4",         "eicc busy don't allow Dsp sleep"),
        9: ("NRCPM_SLEEP_CANCELISR_0",      "Receive phy sleep cancel msg"),
        10:("NRCPM_SLEEP_CANCELISR_1",      "Finish phy sleep cancel msg proc"),
        11:("NRCPM_SLEEP_CANCEL_0",         "cancel dsp sleep req start"),
        12:("NRCPM_SLEEP_CANCEL_1",         "cancel dsp sleep req end"),
        13:("NRCPM_DSPHALTISR_0",           "Receive Dsp halt msg"),
        14:("NRCPM_DSPHALTISR_1",           "Finish Halt_msg proc"),
        15:("NRCPM_HWPOWERDOWN_0",          "Enter sleep proc, Callback allow dsp sleep"),
        16:("NRCPM_HWPOWERDOWN_1",          "Get if l2 allow dsp sleep"),
        17:("NRCPM_HWPOWERDOWN_2",          "Get measure_flag and wake_lock_flag"),
        18:("NRCPM_HWPOWERDOWN_3",          "Callback suspend early"),
        19:("NRCPM_HWPOWERDOWN_4",          "rf power off"),
        20:("NRCPM_HWPOWERDOWN_5",          "abb power off"),
        21:("NRCPM_HWPOWERDOWN_6",          "bbp power off"),
        22:("NRCPM_HWPOWERDOWN_7",          "Callback suspend"),
        23:("NRCPM_HWPOWERDOWN_8",          "Dsp_core wake_unlcok"),
        24:("NRCPM_HWPOWERDOWN_9",          "ccpu core wake unlock"),
        25:("NRCPM_HWPOWERDOWN_10",         "Finish sleep proc"),
        26:("NRCPM_HWPOWERDOWN_11",         "NULL"),
        27:("NRCPM_HWPOWERDOWN_12",         "NULL"),
        28:("NRCPM_HALT_NEED_NOT_DEAL_0",   "l2 don't allow Dsp sleep"),
        29:("NRCPM_HALT_NEED_NOT_DEAL_1",   "Don't allow Dsp sleep req"),
        30:("NRCPM_HALT_NEED_NOT_DEAL_2",   "Measure flag is ture,don't allow Dsp sleep"),
        31:("NRCPM_HALT_NEED_NOT_DEAL_3",   "Wake_lock flag is true;Send DSP wakeup msg"),
        32:("NRCPM_AWAKEISR_0",             "Receive awake IPC"),
        33:("NRCPM_AWAKEISR_1",             "Finish Awake_Isr proc"),
        34:("Start to awake",               "Callback resume_early"),
        35:("NRCPM_HWPOWERUP_1",            "Dsp_core wake_lock"),
        36:("NRCPM_HWPOWERUP_2",            "rf power on"),
        37:("NRCPM_HWPOWERUP_3",            "rf clk enable"),
        38:("NRCPM_HWPOWERUP_4",            "rf rstn"),
        39:("NRCPM_HWPOWERUP_5",            "bbp power on"),
        40:("NRCPM_HWPOWERUP_6",            "......"),
        41:("NRCPM_HWPOWERUP_7",            "Callback resume"),
        42:("NRCPM_HWPOWERUP_8",            "Send DSP wakeup eicc"),
        43:("NRCPM_HWPOWERUP_9",            "Finish awake proc"),
        44:("NRCPM_HWPOWERUP_10",           "NULL"),
        45:("NRCPM_HWPOWERUP_11",           "NULL"),
        46:("NRCPM_RESUMEISR_0",            "Receive Dsp resume msg"),
        47:("NRCPM_RESUMEISR_1",            "Finish Resume_Isr proc"),
        48:("NRCPM_RESUME_0",               "Check has_force_awake flag"),
        49:("NRCPM_RESUME_1",               "Clear has_force_awake flag;Wakeup sem up"),
        50:("NRCPM_RESUME_2",               "Callback complete"),
        51:("NRCPM_RESUME_3",               "Finish resume proc"),
        52:("NRCPM_RESUME_4",               "allow phy sleep"),
        0x5a5a5a5a:("Start to sleep",       "Start to sleep")
}
g_lastStampEnum = 0
g_lastStateStamp = 0
myDdrOffset = 0
g_StampOffset = 0
g_IsTheFirst = 1
#keep enum not change
g_CountEnumTable = {
    0:  "NRCPM_SLEEP_REQ",
    1:  "DSP Halt Int",
    2:  "DSP WakeUp Int",             
    3:  "DSP Resume Msg",
    4:  "DSP SuspendEarly Fail",       
    5:  "DSP Measure Flag",       
    6:  "DSP WakeLock Halt Not Deal",         
    7:  "DSP Deep Sleep",          
    8:  "DSP Snooze",
    9:  "DSP SleepType Error",         
    10: "DSP Store TCM Fail",
    11: "DSP WakeUp SemUp",       
    12: "DSP Restore TCM Fail",  
    13: "Force Awake API",
    14: "CPM Task Start",    
    15: "CPM Task End",    
    16: "DSP MstWakeSlvReq Int",           
    17: "Master Wake GSM",     
    18: "Master Wake WCDMA",
    19: "Master Wake LTE",
    20: "Master Wake TDS",         
    21: "Master Wake CDMA_1X",      
    22: "Master Wake CDMA_HRPD",
    23: "Master Wake NR",
    24: "DSP Deep Sleep TCM Retention",
    25: "DRX_State_BUTT"
}
g_CountStateMaxIndex = 25
g_FileOffset = 0

#######################################################################################
def ReadBinStampHead(inobj):
        global myDdrOffset
        global g_CpmState
        global g_SleepFlag
        global g_CpmWakeLock
        global g_PhyState
        inobj.seek(myDdrOffset)
        (g_CpmState, ) = struct.unpack('I', inobj.read(4))
        (g_SleepFlag, ) = struct.unpack('I', inobj.read(4))
        (g_CpmWakeLock, ) = struct.unpack('I', inobj.read(4))
        (g_PhyState, ) = struct.unpack('I', inobj.read(4))
        (queueMaxNum, ) = struct.unpack('I', inobj.read(4))
        (queueFront, ) = struct.unpack("I", inobj.read(4))
        (queueRear, ) = struct.unpack("I", inobj.read(4))
        (queueNum, ) = struct.unpack("I", inobj.read(4))
        print('maxNum %d, rear %d, num %d.\n' %(queueMaxNum, queueRear, queueNum))
        return {'maxNum':queueMaxNum, 'front':queueFront, 'rear':queueRear, 'num':queueNum}
def StampFindTableIndex(state):
        mark = 0
        for tableIndex in g_StampEnumTable.keys():
                if tableIndex == state:
                        mark = 1
                        break
        if mark == 1:
                return tableIndex
        else:
                return -1
def StampPrint2File(outobj, slice, state):
        global g_lastStampEnum
        global g_lastStateStamp
        global g_IsTheFirst
        stateIndex = 0
        workIndex = 1
        if g_IsTheFirst != 1:
                outobj.writelines(['0x%-10x%-50s\n' % (slice - g_lastStateStamp, g_StampEnumTable[g_lastStampEnum][workIndex])])
        tableIndex = StampFindTableIndex(state)
        if tableIndex == -1:
                print("stamp table index find fail state = %d", state)
                return
        outobj.writelines(['0x%-10x%-30s' % (slice, g_StampEnumTable[tableIndex][stateIndex])])
        g_lastStampEnum = tableIndex
        g_lastStateStamp = slice
        g_IsTheFirst = 0
def PrintStamp(inobj, outobj):
        global myDdrOffset
        queueHead = ReadBinStampHead(inobj)
        if queueHead['maxNum'] > queueHead['num']:
                storeNum = queueHead['num']
        else:
                storeNum = queueHead['maxNum']
        outobj.writelines(["%-15s%-27s%-12s%-10s\n" % ("TimeStamp", "State","Slice", "Work")])
        hasReadNum = 0
        g_StampOffset = queueHead['front']
        QueueDataOffset = 32
        inobj.seek(g_StampOffset * 8 + QueueDataOffset + myDdrOffset)

        while hasReadNum < storeNum:
                if g_StampOffset == 0:
                        inobj.seek(g_StampOffset * 8 + QueueDataOffset + myDdrOffset)
                (slice, ) = struct.unpack('I', inobj.read(4))
                (state, ) = struct.unpack('I', inobj.read(4))
                StampPrint2File(outobj, slice, state)
                hasReadNum = hasReadNum  + 1
                g_StampOffset = (g_StampOffset + 1)%queueHead['maxNum']
        #move the pointer to countOffset
        countOffset = queueHead['maxNum'] * 8  + QueueDataOffset
        inobj.seek(countOffset + myDdrOffset)
        return 0
######################################################################################
def CountFindTableIndex(stateIndex):
        mark = 0
        for tableIndex in g_CountEnumTable.keys():
                if tableIndex == stateIndex:
                          mark = 1
                          break
        if mark == 1:
                return tableIndex
        else:
                return -1
                          
def CountPrint2File(outobj, stateIndex, count, slice):
        tableIndex = CountFindTableIndex(stateIndex)
        if tableIndex == -1:
                print("Count find table index fail stateIndex = %d", stateIndex)
                return
        outobj.writelines("%-30s :Count 0x%-08x, Slice 0x%-08x\n" % (g_CountEnumTable[tableIndex], count, slice))
def printCount(inobj, outobj):
        global g_CpmState
        global g_SleepFlag
        global g_CpmWakeLock
        global g_PhyState
        stateIndex = 0
        outobj.writelines("\n===============================================================================\n")
        outobj.writelines("CPM State     =  0x%-08x\n" % (g_CpmState))
        outobj.writelines("Sleep Flag    =  0x%-08x\n" % (g_SleepFlag))
        outobj.writelines("CPM Wake Lock =  0x%-08x\n" % (g_CpmWakeLock))
        outobj.writelines("DSP State     =  0x%-08x\n" % (g_PhyState))
        while stateIndex < g_CountStateMaxIndex:
                (count, ) = struct.unpack("I", inobj.read(4))
                (slice, ) = struct.unpack("I", inobj.read(4))
                CountPrint2File(outobj, stateIndex, count, slice)
                stateIndex = stateIndex +1
def ExpaseMspSleep(infile, field, offset, len, version, mode, outfile):
        global myDdrOffset
        myDdrOffset = eval(offset)
        inobj = infile
        outobj = outfile
        ret = PrintStamp(inobj, outobj)
        print('PrintStamp OK')
        ret = printCount(inobj, outobj)
        return ret
########################################################################################
def entry_0x7000099(infile, field, offset, len, version, mode, outfile):
        ########check parameter start#############
        if not field == '0x7000099':
            print('hidis field is ', field)
            print('current field is', '0x7000099')
            return error['ERR_CHECK_FIELD']
        elif not version == '0x0000':
            print('hidis version is ', version)
            print('current version is ', '0x0000')
            return error['ERR_CHECK_VERSION']
        elif not len == '0x1000':
            print('hids len is ', len)
            print('current len is ', '0x1000')
            return error['ERR_CHECK_LEN']
        #########check parameter end##############
        outfile.writelines("============NR CPMNR0============\n")
        ret = ExpaseMspSleep(infile, field, offset, len, version, mode, outfile)
        return 0


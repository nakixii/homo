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
        0: ("CPM_DSPHALTISR_0",             "Receive Dsp halt IPC"),
        1: ("CPM_DSPHALTISR_1",             "Finish Halt_Isr proc"),
        2: ("CPM_HWPOWERDOWN_0",            "Enter sleep proc,read sleep_type,stop dsp core"),
        3: ("CPM_HWPOWERDOWN_1",            "Check has_force_awake flag"),
        4: ("CPM_HWPOWERDOWN_2",            "Check sleep_type"),
        5: ("CPM_HWPOWERDOWN_3",            "Enter deep_sleep proc,store dsp image"),
        6: ("CPM_HWPOWERDOWN_4",            "Store dsp image ok"),
        7: ("CPM_HWPOWERDOWN_5",            "Dsp power down"),
        8: ("CPM_HWPOWERDOWN_6",            "Enter snooze proc"),
        9: ("CPM_HWPOWERDOWN_7",            "Sleep type error"),
        10:("CPM_HWPOWERDOWN_8",            "Store bbp voltage and dsp pll"),
        11:("CPM_HWPOWERDOWN_9",            "Callback suspend"),
        12:("CPM_HWPOWERDOWN_10",           "DDR_FREQ update 0"),
        13:("CPM_HWPOWERDOWN_11",           "Ccore wake_unlock"),
        14:("CPM_HWPOWERDOWN_12",           "Finish sleep proc"),
        15:("CPM_HALT_NEED_NOT_DEAL_0",     "Wake_lock flag is true;Reset dsp core"),
        16:("CPM_HALT_NEED_NOT_DEAL_1",     "NULL"),
        17:("CPM_HALT_NEED_NOT_DEAL_2",     "NULL"),
        18:("CPM_AWAKEISR_0",               "NULL"),
        19:("CPM_AWAKEISR_1",               "NULL"),
        20:("Start to awake",               "Callback resume_early"),
        21:("CPM_HWPOWERUP_1",              "Restore bbp voltage and dsp pll"),
        22:("CPM_HWPOWERUP_2",              "Read sleep_type"),
        23:("CPM_HWPOWERUP_3",              "Enter DeepSleep wakeup proc,DDR_FREQ update to 240MHz"),
        24:("CPM_HWPOWERUP_4",  			"Dsp power on"),
        25:("CPM_HWPOWERUP_5",              "Restore dsp image"),
        26:("CPM_HWPOWERUP_6",              "Restore dsp image ok"),
        27:("CPM_HWPOWERUP_7",              "Enter snooze wakeup proc,DDR_FREQ update to 120MHz"),
        28:("CPM_HWPOWERUP_8",              "Dsp clk enable and unreset core"),
        29:("CPM_HWPOWERUP_9",              "Sleep type error"),
        30:("CPM_HWPOWERUP_10",             "Callback resume; Run dsp core"),
        31:("CPM_HWPOWERUP_11",             "Finish awake proc"),
        32:("CPM_RESUMEISR_0",              "Receive Dsp resume IPC"),
        33:("CPM_RESUMEISR_1",              "Finish Resume_Isr proc"),
        34:("CPM_RESUME_0",                 "DDR_FREQ update to 120MHz"),
        35:("CPM_RESUME_1",                 "Callback complete"),
        36:("CPM_RESUME_2",                 "Check has_force_awake flag"),
        37:("CPM_RESUME_3",                 "Clear has_force_awake flag;Wakeup sem up"),
        38:("CPM_RESUME_4",                 "Finish resume proc"),
        0x5a5a5a5a:("Start to sleep",       "Start to sleep")
}
g_lastStampEnum = 0
g_lastStateStamp = 0
myDdrOffset = 0
g_StampOffset = 0
g_IsTheFirst = 1
#keep enum not change
g_CountEnumTable = {
	0:	"DSP Halt Int",               
	1:	"DSP WakeUp Int",             
	2:	"DSP Resume Int",
	3:	"DSP SuspendEarly Fail",       
	4:	"DSP Measure Flag",       
	5:	"DSP WakeLock Halt Not Deal",         
	6:	"DSP Deep Sleep",          
	7:	"DSP Snooze",
	8:	"DSP SleepType Error",         
	9:	"DSP Store TCM Fail",
	10:	"DSP WakeUp SemUp",       
	11:	"DSP Restore TCM Fail",  
	12:     "Force Awake API",
	13:	"CPM Task Start",    
	14:	"CPM Task End",    
	15:	"DSP MstWakeSlvReq Int",           
	16:	"Master Wake GSM",     
	17:	"Master Wake WCDMA",
	18: "Master Wake LTE",
	19:	"Master Wake TDS",         
	20:	"Master Wake CDMA_1X",      
	21:	"Master Wake CDMA_HRPD",
	22: "DSP Deep Sleep TCM Retention",
	23: "DRX_State_BUTT"
}
g_CountStateMaxIndex = 23
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
        print({'maxNum':queueMaxNum, 'rear':queueRear, 'num':queueNum})
        return {'maxNum':queueMaxNum, 'front':queueFront, 'rear':queueRear, 'num':queueNum}
def StampFindTableIndex(state):
        mark = 0
        for tableIndex in list(g_StampEnumTable.keys()):
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
        for tableIndex in list(g_CountEnumTable.keys()):
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
def entry_0x2000089(infile, field, offset, len, version, mode, outfile):
        ########check parameter start#############
        if not field == '0x2000089':
            print('hidis field is ', field)
            print('current field is', '0x2000089')
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
        ret = ExpaseMspSleep(infile, field, offset, len, version, mode, outfile)
        return 0


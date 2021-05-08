#!/usr/bin/env python3
# coding=utf-8
# Copyright (C) Huawei Technologies Co., Ltd. 2010-2018. All rights reserved.

import struct
import os
import sys
import string
from config import *

global g_StampEnumTable
global g_lastStampEnum
global g_lastStateStamp
global g_lastOtherInfo
global g_StampPrint2FileMark
#global myDdrOffset
global g_StampOffset
global g_IsTheFirst
global g_CountStateMaxIndex
global g_FileOffset

g_StampEnumTable = {
        1: ("NV_DEBUG_WRITEEX_START",               "write nv start, nvid"),
        2: ("NV_DEBUG_WRITEEX_GET_IPC_START",       "for check crc,start to get ipc sem"),
        3: ("NV_DEBUG_WRITEEX_GET_IPC_END",         "get ipc sem end"),
        4: ("NV_DEBUG_WRITEEX_GIVE_IPC",            "check crc end, release ipc sem"),
        5: ("NV_DEBUG_WRITEEX_MEM_START",           "write to mem start"),
        6: ("NV_DEBUG_WRITEEX_FILE_START",          "write to file start"),
        7: ("NV_DEBUG_FLUSH_START",                 "flush nv list start"),
        8: ("NV_DEBUG_FLUSH_END",                   "flush nv list end"),
        9: ("NV_DEBUG_REQ_FLUSH_START",             "req flush nv list start"),
        10:("NV_DEBUG_REQ_FLUSH_END",               "req flush nv list end"),
        11:("NV_DEBUG_FLUSHEX_START",               "flush nv to file start"),
        12:("NV_DEBUG_FLUSHEX_OPEN_START",          "open nv file start"),
        13:("NV_DEBUG_FLUSHEX_OPEN_END",            "open nv file end"),
        14:("NV_DEBUG_FLUSHEX_GET_PROTECT_SEM_START",       "before write to file get ipc and sem start"),
        15:("NV_DEBUG_FLUSHEX_GET_PROTECT_SEM_END",         "before write to file get ipc and sem end"),
        16:("NV_DEBUG_FLUSHEX_GIVE_IPC",            "write to file release ipc"),
        17:("NV_DEBUG_FLUSHEX_GIVE_SEM",            "release sem"),
        18:("NV_DEBUG_FLUSHEX_WRITE_FILE_START",    "write to nv.bin start"),
        19:("NV_DEBUG_FLUSHEX_WRITE_FILE_END",      "write to nv.bin end"),
        20:("NV_DEBUG_WRITEEX_END",                 "write nv end, nvid"),
        21:("NV_DEBUG_RECEIVE_ICC",                 "receive icc msg from acore"),
        22:("NV_DEBUG_SEND_ICC",  			        "send icc msg to acore, msgtype"),
        23:("NV_DEBUG_READ_ICC",                    "read icc from ccore, msgtype"),
        24:("NV_DEBUG_REQ_ASYNC_WRITE",             "send async write nv msg"),
        25:("NV_DEBUG_REQ_REMOTE_WRITE",            "read icc from ccore")
}
g_IccMsgTable = {
        64:("NV_ICC_REQ_SYS",               "ccore request to acore to wirte nv to sys area"),
        65:("NV_ICC_REQ_INSTANT_FLUSH",     "ccore request to acore to flush nv to flash with cnf"),
        66:("NV_ICC_REQ_CCORE_DELAY_FLUSH", "ccore request to acore to write nv to flash with no cnf"),
        67:("NV_REQ_ACORE_DELAY_FLUSH",     "ccore request to acore to write nv to flash with "),
        68:("NV_ICC_RESUME_ITEM",           "ccore request to acore to resume nv because the nv crc is error"),
        127:("NV_ICC_CNF",                  "acore cnf to ccore"),
        255:("NV_ICC_RESUME",               "ccore request to acore to resume all nv bin to ddr")
}
g_IccMsgNum = 7
g_lastStampEnum = 0
g_lastStateStamp = 0
myDdrOffset = 0
g_StampOffset = 0
g_IsTheFirst = 1
g_CountStateMaxIndex = 31
g_FileOffset = 0
#######################################################################################
def ReadBinStampHead(inobj):
        global myDdrOffset
        inobj.seek(myDdrOffset)
        (queueMaxNum, ) = struct.unpack('I', inobj.read(4))
        (queueFront, ) = struct.unpack("I", inobj.read(4))
        (queueRear, ) = struct.unpack("I", inobj.read(4))
        (queueNum, ) = struct.unpack("I", inobj.read(4))
        print({'maxNum':queueMaxNum, 'front':queueFront, 'rear':queueRear, 'num':queueNum})
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
def StampPrint2File(outobj, slice, state, otherinfo):
        global g_lastStampEnum
        global g_lastStateStamp
        global g_IsTheFirst
        global g_lastOtherInfo
        stateIndex = 0
        workIndex = 1
        if g_IsTheFirst != 1 or g_IsTheFirst == 2:
                outobj.writelines(['0x%-10x%-10s : 0x%x\n' % (slice - g_lastStateStamp, g_StampEnumTable[g_lastStampEnum][workIndex], g_lastOtherInfo)])
                if g_IsTheFirst == 2:
                    print("end")
                    return
        tableIndex = StampFindTableIndex(state)
        if tableIndex == -1:
                print("stamp table index find fail state = %d", state)
                return
        outobj.writelines(['0x%-10x%-30s' % (slice, g_StampEnumTable[tableIndex][stateIndex])])
        g_lastStampEnum = tableIndex
        g_lastStateStamp = slice
        g_lastOtherInfo = otherinfo
        g_IsTheFirst = 0
        
def PrintStamp(inobj, outobj):
        global myDdrOffset
        global g_IsTheFirst
        queueHead = ReadBinStampHead(inobj)
        #prepare to parse data
        outobj.writelines(["%-15s%-27s%-12s%-10s\n" % ("TimeStamp", "State","Slice", "Work")])
        hasReadNum = 0
        g_StampOffset = queueHead['front']
        #queue real data offset#
        QueueDataOffset = 16
        #queue is not loop
        if queueHead['maxNum'] > queueHead['num']:
                storeNum = queueHead['num']
 
        else:
                storeNum = queueHead['maxNum']
        while hasReadNum < storeNum:
                inobj.seek( myDdrOffset + QueueDataOffset + g_StampOffset * 8)
                (state, ) = struct.unpack('H', inobj.read(2))
                #other info is nvid or icc msg type#
                (otherinfo, ) = struct.unpack('H', inobj.read(2))
                (slice, ) = struct.unpack('I', inobj.read(4))
                StampPrint2File(outobj, slice, state, otherinfo)
                hasReadNum = hasReadNum  + 1
                g_StampOffset = (g_StampOffset + 1)%queueHead['maxNum']
        g_IsTheFirst = 2
        StampPrint2File(outobj, 0, 0, 0)
        return 0
def PrintHelpInfo(outobj):
        outobj.writelines("\n********************************icc msg help info start***************************************\n")
        outobj.writelines(["%-15s%-30s%-12s\n" % ("msg id", "Enum", "Work")])
        iccMsgTableIndex = 0
        iccMsgEnumIndex = 0
        iccMsgWorkIndex = 1
        for iccMsgIndex in list(g_IccMsgTable.keys()):
            outobj.writelines(["0x%-12x%-30s%-12s\n" % (iccMsgIndex, g_IccMsgTable[iccMsgIndex][iccMsgEnumIndex],  g_IccMsgTable[iccMsgIndex][iccMsgWorkIndex])])
            iccMsgTableIndex = iccMsgTableIndex + 1
        outobj.writelines("********************************icc msg help info end***************************************\n")
######################################################################################
def ExpaseNV(infile, field, offset, len, version, mode, outfile):
        global myDdrOffset
        myDdrOffset = eval(offset)
        inobj = infile
        outobj = outfile
        ret = PrintStamp(inobj, outobj)
        print('PrintStamp OK')
        PrintHelpInfo(outobj)
        return ret
########################################################################################
def entry_0x1100009(infile, field, offset, len, version, mode, outfile):
        ########check parameter start#############
        if not field == '0x1100009':
            print(('hidis field is ', field))
            print(('current field is', '0x1100009'))
            return error['ERR_CHECK_FIELD']
        elif not version == '0x0000':
            print(('hidis version is ', version))
            print(('current version is ', '0x0000'))
            return error['ERR_CHECK_VERSION']
        elif not len == '0x1000':
            print(('hids len is ', len))
            print(('current len is ', '0x1000'))
            return error['ERR_CHECK_LEN']
        #########check parameter end##############
        ret = ExpaseNV(infile, field, offset, len, version, mode, outfile)
        return 0


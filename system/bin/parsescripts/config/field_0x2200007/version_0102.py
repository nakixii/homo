#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   analysis cproc dump bin
modify  record  :   2016-03-10 create file
"""

import struct
import os
import sys
import string
from cproc_parse_lib import *

MACRO_CPROC_MNTN_MAX_HANDLED_MSG_SAVE_NUM                 = 120
MACRO_CPROC_1X_MNTN_LOG_HANDLED_MSG_SAVE_INFO_SIZE   = 8
MACRO_CPROC_1X_MNTN_INT_SPEND_TIME_INFO_SIZE                 = 96
MACRO_CPROC_HRPD_MNTN_MAX_WAIT_LIST_NUM                       = 16
MACRO_CPROC_MNTN_MAX_DYNAMIC_ERROR_MSG_NUM                = 50
MACRO_CPROC_MNTN_FSM_ERROR_INFO_SIZE                               = 20
MACRO_CPROC_MNTN_MAX_FSM_SAVE_NUM                                  = 120
MACRO_CPROC_MNTN_MAX_FSM_REG_KILL_INFO_NUM                   = 50
MACRO_CPROC_MNTN_MAX_FSM_ESS_EVENT_NUM                         = 30
MACRO_CPROC_MNTN_MAX_DYNAMIC_ERROR_MSG_NUM                 = 50

"""
 -------------------------------------------
|  Field version            4 bytes
 -------------------------------------------
|  1x Handled msg index     4 bytes
|  1x Last msg timeslice    4 bytes
|  1x Handled msg array     8 bytes * 120
 -------------------------------------------
|  hrpd Handled msg index   4 bytes
|  hrpd Last msg timeslice  4 bytes
|  hrpd Handled msg array   8 bytes * 120
 -------------------------------------------
|  RM Handled msg index     4 bytes
|  RM Last msg timeslice    4 bytes
|  RM Handled msg array     8 bytes * 120
 -------------------------------------------
|  ErrorInd flag            4 bytes
 -------------------------------------------
|  hrpd Handled msg index   4 bytes
|  hrpd Last msg timeslice  4 bytes
|  hrpd Handled msg array   8 bytes * 120
 -------------------------------------------
|  Wait List                4 bytes * 16
 -------------------------------------------
|  Interrupt spend time     96 bytes
 -------------------------------------------
|  hrpd FSM current index   4 bytes
|  hrpd FSM last timeslice  4 bytes
|  hrpd FSM state array     4 bytes * 120
 -------------------------------------------
|  Fsm error                20 bytes
 -------------------------------------------
|  Fsm kill info            1204 bytes
 -------------------------------------------
|  Dynamic error number    4 bytes
|  1x msg array               8 bytes * 50
|  hrpd msg array            8 bytes * 50
 -------------------------------------------
"""

def analysis_cproc_dump_info_0102( infile, offset, outfile, version):
        instream = infile
        outstream  = outfile
        #fileOffset = eval(offset)
        fileOffset = offset
        
        outstream.writelines(["\n======================================================================================\n"])
        outstream.writelines(["CPROC DUMP ANALYSIS @20161201, Field version: %d.%d\n" % (version>>8, version&0xff)])
        outstream.writelines(["======================================================================================\n"])
        #outstream.writelines(["Output to txt file: c:\\modem_dump_cproc.txt\n\n\n"])
        #save2file.writelines(["======================================================================================\n"])
        #save2file.writelines(["CPROC DUMP ANALYSIS @20161121, Field version: %d.%d\n" % (version>>8, version&0xff)])
        #save2file.writelines(["======================================================================================\n"])
        #save2file.writelines(["Output to txt file: c:\\modem_dump_cproc.txt\n\n\n"])
        
        ######## analysis cproc 1x handled msg #########
        instream.seek(fileOffset) 
        (ulHandledMsgIndex,)  = struct.unpack('I', instream.read(4))
        (ulLastMsgTimeSlice,) = struct.unpack('I', instream.read(4))
        strTemp               = 'Last message timeslice: 0x%08X '% (ulLastMsgTimeSlice)
        
        fileOffset = fileOffset + 8
        outstream.writelines(["(1) CPROC 1X handled message list\n"])
        outstream.writelines(["======================================================================================\n"])
        #save2file.writelines(["(1) CPROC 1X handled message list\n"])
        #save2file.writelines(["======================================================================================\n"])
        outstream.writelines(["%-15s\n\n" % (strTemp)])
        #save2file.writelines(["%-15s\n\n" % (strTemp)])
        analysis_cproc_handled_msg_list_dump_info( instream, fileOffset, outstream, ulHandledMsgIndex, version)


        ######## analysis cproc hrpd handled msg #########
        fileOffset = fileOffset + MACRO_CPROC_1X_MNTN_LOG_HANDLED_MSG_SAVE_INFO_SIZE * MACRO_CPROC_MNTN_MAX_HANDLED_MSG_SAVE_NUM
        
        instream.seek(fileOffset) 
        (ulHandledMsgIndex,)  = struct.unpack('I', instream.read(4))
        (ulLastMsgTimeSlice,) = struct.unpack('I', instream.read(4))
        strTemp               = 'Last message timeslice: 0x%08X '% (ulLastMsgTimeSlice)

        fileOffset = fileOffset + 8
        outstream.writelines(["\n\n(2) CPROC HRPD handled message list\n"])
        outstream.writelines(["======================================================================================\n"])
        #save2file.writelines(["\n\n(2) CPROC HRPD handled message list\n"])
        #save2file.writelines(["======================================================================================\n"])
        outstream.writelines(["%-15s\n\n" % (strTemp)])
        #save2file.writelines(["%-15s\n\n" % (strTemp)])
        analysis_cproc_handled_msg_list_dump_info( instream, fileOffset, outstream, ulHandledMsgIndex, version)


        ######## analysis cproc rm handled msg #########
        fileOffset = fileOffset + MACRO_CPROC_1X_MNTN_LOG_HANDLED_MSG_SAVE_INFO_SIZE * MACRO_CPROC_MNTN_MAX_HANDLED_MSG_SAVE_NUM

        instream.seek(fileOffset) 
        (ulHandledMsgIndex,)  = struct.unpack('I', instream.read(4))
        (ulLastMsgTimeSlice,) = struct.unpack('I', instream.read(4))
        strTemp               = 'Last message timeslice: 0x%08X '% (ulLastMsgTimeSlice)

        fileOffset = fileOffset + 8
        outstream.writelines(["\n\n(3) CPROC RM handled message list\n"])
        outstream.writelines(["======================================================================================\n"])
        #save2file.writelines(["\n\n(3) CPROC RM handled message list\n"])
        #save2file.writelines(["======================================================================================\n"])
        outstream.writelines(["%-15s\n\n" % (strTemp)])
        #save2file.writelines(["%-15s\n\n" % (strTemp)])
        analysis_cproc_handled_msg_list_dump_info( instream, fileOffset, outstream, ulHandledMsgIndex, version)
        

        ######## analysis cproc hrpd extern handled msg #########
        fileOffset = fileOffset + MACRO_CPROC_1X_MNTN_LOG_HANDLED_MSG_SAVE_INFO_SIZE * MACRO_CPROC_MNTN_MAX_HANDLED_MSG_SAVE_NUM

        instream.seek(fileOffset)
        (ulErrorIndFlag,)     = struct.unpack('I', instream.read(4))
        (ulHandledMsgIndex,)  = struct.unpack('I', instream.read(4))
        (ulLastMsgTimeSlice,) = struct.unpack('I', instream.read(4))
        strTemp               = 'Last message timeslice: 0x%08X '% (ulLastMsgTimeSlice)

        fileOffset = fileOffset + 12
        outstream.writelines(["\n\n(4) CPROC HRPD Extern handled message list\n"])
        outstream.writelines(["======================================================================================\n"])
        #save2file.writelines(["\n\n(4) CPROC HRPD Extern handled message list\n"])
        #save2file.writelines(["======================================================================================\n"])

        if (ulLastMsgTimeSlice == 0):
            outstream.writelines(["no record\n"])
            #save2file.writelines(["no record\n"])
        else:
            outstream.writelines(["%-15s\n\n" % (strTemp)])
            #save2file.writelines(["%-15s\n\n" % (strTemp)])
            analysis_cproc_handled_msg_list_dump_info( instream, fileOffset, outstream, ulHandledMsgIndex, version)
        
		
        ######## analysis cproc hrpd waitlist #########
        ulWaitListLoop   = 0
        fileOffset = fileOffset + MACRO_CPROC_1X_MNTN_LOG_HANDLED_MSG_SAVE_INFO_SIZE * MACRO_CPROC_MNTN_MAX_HANDLED_MSG_SAVE_NUM

        outstream.writelines(["\n\n(5) CPROC HRPD FSM waitlist info\n"])
        outstream.writelines(["======================================================================================\n"])
        #save2file.writelines(["\n\n(5) CPROC HRPD FSM waitlist info\n"])
        #save2file.writelines(["======================================================================================\n"])
        
        outstream.writelines(["%-50s%-50s\n" % ("FsmId/ExceptionId", "usWaitList")])
        #save2file.writelines(["%-50s%-50s\n" % ("FsmId/ExceptionId", "usWaitList")])
        
        while ulWaitListLoop < MACRO_CPROC_HRPD_MNTN_MAX_WAIT_LIST_NUM:
                fileLocalOffset = fileOffset + ulWaitListLoop * 4
                analysis_cproc_hrpd_mntn_per_fsm_waitlist_info(instream, fileLocalOffset, outstream)
                ulWaitListLoop = ulWaitListLoop + 1
        
        
        ######## analysis int spend time info #########
        ulIntSpendTimeLoop = 0
        fileOffset = fileOffset + MACRO_CPROC_HRPD_MNTN_MAX_WAIT_LIST_NUM * 4
        
        instream.seek(fileOffset)
        (ulIntStartTime,)               = struct.unpack('I', instream.read(4))
        (ulStartCallbackLoopTime,)  = struct.unpack('I', instream.read(4))
        (ulIntEndTime,)                 = struct.unpack('I', instream.read(4))
        (ulCallbackNum,)               = struct.unpack('I', instream.read(4))

        outstream.writelines(["\n\n(6) CPROC interrupt spend time info\n"])
        outstream.writelines(["======================================================================================\n"])
        #save2file.writelines(["\n\n(6) CPROC interrupt spend time info\n"])
        #save2file.writelines(["======================================================================================\n"])
        
        outstream.writelines(["ulIntStartTime: 0x%08X\nulStartCallbackLoopTime: 0x%08X\nulIntEndTime: 0x%08X\nulCallbackNum: 0x%08X\n" % (ulIntStartTime, ulStartCallbackLoopTime, ulIntEndTime, ulCallbackNum)])
        #save2file.writelines(["ulIntStartTime: 0x%08X\nulStartCallbackLoopTime: 0x%08X\nulIntEndTime: 0x%08X\nulCallbackNum: 0x%08X\n" % (ulIntStartTime, ulStartCallbackLoopTime, ulIntEndTime, ulCallbackNum)])
        
        outstream.writelines(["%-22s" % ("aulCallbackSpendTime: ")])
        #save2file.writelines(["%-22s" % ("aulCallbackSpendTime: ")])

        while ulIntSpendTimeLoop < 10:
                (ulCallbackSpendTime,) = struct.unpack('I', instream.read(4))
                outstream.writelines(["0x%08X  " % (ulCallbackSpendTime)])
                #save2file.writelines(["%08X  " % (ulCallbackSpendTime)])
                ulIntSpendTimeLoop = ulIntSpendTimeLoop + 1

        outstream.writelines(["\n"])
        #save2file.writelines(["\n"])

        outstream.writelines(["%-22s" % ("aulCallback: ")])
        #save2file.writelines(["%-22s" % ("aulCallback: ")])

        ulIntSpendTimeLoop = 0

        while ulIntSpendTimeLoop < 10:
                (ulCallbackSpendTime,) = struct.unpack('I', instream.read(4))
                outstream.writelines(["0x%08X  " % (ulCallbackSpendTime)])
                #save2file.writelines(["%08X  " % (ulCallbackSpendTime)])
                ulIntSpendTimeLoop = ulIntSpendTimeLoop + 1
        
        
        ######## analysis cproc hrpd fsm #########
        fileOffset = fileOffset + MACRO_CPROC_1X_MNTN_INT_SPEND_TIME_INFO_SIZE

        instream.seek(fileOffset)
        (ulHandledMsgIndex,)  = struct.unpack('I', instream.read(4))
        (ulLastMsgTimeSlice,) = struct.unpack('I', instream.read(4))
        strTemp               = 'Last record timeslice: 0x%08X '% (ulLastMsgTimeSlice)

        fileOffset = fileOffset + 8
        outstream.writelines(["\n\n\n(7) CPROC HRPD state machine\n"])
        outstream.writelines(["======================================================================================\n"])
        #save2file.writelines(["\n\n\n(7) CPROC HRPD state machine\n"])
        #save2file.writelines(["======================================================================================\n"])
        outstream.writelines(["%-15s\n\n" % (strTemp)])
        #save2file.writelines(["%-15s\n\n" % (strTemp)])
        analysis_cproc_fsm_list_dump_info(instream, fileOffset, outstream, ulHandledMsgIndex, version)


        ######## analysis FSM error info #########
        fileOffset = fileOffset + MACRO_CPROC_MNTN_MAX_FSM_SAVE_NUM * 4
        
        instream.seek(fileOffset)
        (ulErrorCode,)                   = struct.unpack('I', instream.read(4))
        (ulLastEvent,)                  = struct.unpack('I', instream.read(4))
        (ulLastMessage,)              = struct.unpack('I', instream.read(4))
        (pWorld,)                        = struct.unpack('I', instream.read(4))
        (ulContextSize,)               = struct.unpack('I', instream.read(4))
        
        outstream.writelines(["\n\n(8) CPROC FSM error info\n"])
        outstream.writelines(["======================================================================================\n"])
        #save2file.writelines(["\n\n(8) CPROC FSM error info\n"])
        #save2file.writelines(["======================================================================================\n"])
        if (ulErrorCode == 0):
            outstream.writelines(["no record\n"])
            #save2file.writelines(["no record\n"])
        else:
            outstream.writelines(["ErrorCode: 0x%08X\nLastEvent: 0x%08X\nLastMessage: 0x%08X\npWorld: 0x%08X\nContextSize: 0x%08X\n" % (ulErrorCode, ulLastEvent, ulLastMessage, pWorld, ulContextSize)])
            #save2file.writelines(["ErrorCode: 0x%08X\nLastEvent: 0x%08X\nLastMessage: 0x%08X\npWorld: 0x%08X\nContextSize: 0x%08X\n" % (ulErrorCode, ulLastEvent, ulLastMessage, pWorld, ulContextSize)])


        ######## analysis FSM register and kill info #########
        ulFsmRegKillLoop = 0
        fileOffset = fileOffset + MACRO_CPROC_MNTN_FSM_ERROR_INFO_SIZE
        fileTmpOffset = fileOffset + (12 * MACRO_CPROC_MNTN_MAX_FSM_REG_KILL_INFO_NUM) * 2

        instream.seek(fileTmpOffset)
        (usFsmRegisterIdx,)  = struct.unpack('H', instream.read(2))
        (usFsmKillIdx,)         = struct.unpack('H', instream.read(2))

        outstream.writelines(["\n\n(9) CPROC FSM register and kill info\n"])
        outstream.writelines(["======================================================================================\n"])
        #save2file.writelines(["\n\n(9) CPROC FSM register and kill info\n"])
        #save2file.writelines(["======================================================================================\n"]) 
        
        outstream.writelines(["usFsmRegisterIdx: %d,  usFsmKillIdx: %d\n\n" % (usFsmRegisterIdx, usFsmKillIdx)])
        #save2file.writelines(["usFsmRegisterIdx: %d,  usFsmKillIdx: %d\n\n" % (usFsmRegisterIdx, usFsmKillIdx)])

        outstream.writelines(["|<---------------------- FSM register info ---------------------->|                 |<------------------------ FSM kill info ------------------------->|\n"])
        #save2file.writelines(["|<---------------------- FSM register info ---------------------->|                 |<------------------------ FSM kill info ------------------------->|\n"])
        outstream.writelines(["%-15s%-40s%-30s%-15s%-40s%-25s\n" % ("ulTimeStamp", "ulFsmId", "ulFsmPointer", "ulTimeStamp", "ulFsmId", "ulFsmPointer")])
        #save2file.writelines(["%-15s%-40s%-30s%-15s%-40s%-25s\n" % ("ulTimeStamp", "ulFsmId", "ulFsmPointer", "ulTimeStamp", "ulFsmId", "ulFsmPointer")])
        
        while ulFsmRegKillLoop < MACRO_CPROC_MNTN_MAX_FSM_REG_KILL_INFO_NUM:
                fileLocalOffset = fileOffset + ulFsmRegKillLoop * 12
                analysis_cproc_hrpd_mntn_fsm_reg_kill_info(instream, fileLocalOffset, outstream)
                ulFsmRegKillLoop = ulFsmRegKillLoop + 1
       

        ######## analysis FSM ess event #########
        ulLooper    = 0
        ulSplotCnt = 0
        fileOffset = fileOffset + (12 * MACRO_CPROC_MNTN_MAX_FSM_REG_KILL_INFO_NUM) * 2 + 4

        instream.seek(fileOffset)
        (ulEssEventCurIndex,)       = struct.unpack('I', instream.read(4))
        (ulLastEssEventTimeSlice,) = struct.unpack('I', instream.read(4))
        strTemp = 'Last ess event timeslice: 0x%08X' % (ulLastEssEventTimeSlice)
        
        fileOffset = fileOffset + 8
        
        outstream.writelines(["\n\n(10) CPROC HRPD ESS event\n"])
        outstream.writelines(["======================================================================================\n"])
        #save2file.writelines(["\n\n(10) CPROC HRPD ESS event\n"])
        #save2file.writelines(["======================================================================================\n"])
        outstream.writelines(["%s\n" % (strTemp)])
        #save2file.writelines(["%s\n" % (strTemp)])
        
        outstream.writelines(["Hex format: timestamp(ess event)\n\n"])
        #save2file.writelines(["Hex format: timestamp(ess event)\n\n"])

        ulLooper = ulEssEventCurIndex
        
        while ulLooper < (MACRO_CPROC_MNTN_MAX_FSM_ESS_EVENT_NUM + ulEssEventCurIndex):
                ulLooperIndex = ulLooper % MACRO_CPROC_MNTN_MAX_FSM_ESS_EVENT_NUM
                fileLocalOffset = fileOffset + ulLooperIndex * 8
                
                #analysis_cproc_mntn_each_ess_event_info(instream, fileLocalOffset, outstream, save2file, version)
                instream.seek(fileLocalOffset)

                (ulTimeStamp,)   = struct.unpack('I', instream.read(4))
                (ulEssEvent,)     = struct.unpack('I', instream.read(4))
                
                if (ulEssEvent > 0):
                    strEssEvent = '0x%08X(Event:%08X)' % (ulTimeStamp, ulEssEvent)
                    outstream.writelines(["%s " % (strEssEvent)])
                    #save2file.writelines(["%s " % (strEssEvent)])
                    ulSplotCnt = ulSplotCnt + 1
                
                ulLooper = ulLooper + 1
                
                if ((ulSplotCnt > 0) and (ulSplotCnt % 5 == 0)):
                    outstream.writelines(["\n"])
                    #save2file.writelines(["\n"])

        if ((ulSplotCnt > 0) and (ulSplotCnt % 5 > 0)):
                outstream.writelines(["\n"])
                #save2file.writelines(["\n"])
        

        ######## analysis hrpd dynamic error msg info #########
        fileOffset = fileOffset + MACRO_CPROC_MNTN_MAX_FSM_ESS_EVENT_NUM * 8
        
        instream.seek(fileOffset) 
        (ulTotalDynamicErrorNum,)  = struct.unpack('I', instream.read(4))

        fileOffset = fileOffset + 4
        
        outstream.writelines(["\n\n(11) CPROC HRPD Dynamic Error message list\n"])
        outstream.writelines(["======================================================================================\n"])
        #save2file.writelines(["\n\n(11) CPROC HRPD Dynamic Error message list\n"])
        #save2file.writelines(["======================================================================================\n"])

        if (ulTotalDynamicErrorNum == 0):
            outstream.writelines(["no record"])
            #save2file.writelines(["no record"])
        else:
            outstream.writelines(["ulTotalDynamicErrorNum: %d\n\n" % (ulTotalDynamicErrorNum)])
            #save2file.writelines(["ulTotalDynamicErrorNum: %d\n\n" % (ulTotalDynamicErrorNum)])

            outstream.writelines(["|<----------------------------------------------- cproc 1x -------------------------------------------->|\n"])
            #save2file.writelines(["|<----------------------------------------------- cproc 1x -------------------------------------------->|\n"])
            analysis_cproc_dynamic_error_msg_list_info( instream, fileOffset, outstream, version)

            outstream.writelines(["\n"])
            #save2file.writelines(["\n"])

            outstream.writelines(["|<---------------------------------------------- cproc hrpd ------------------------------------------->|\n"])
            #save2file.writelines(["|<---------------------------------------------- cproc hrpd ------------------------------------------->|\n"])
            
            fileOffset = fileOffset + MACRO_CPROC_MNTN_MAX_DYNAMIC_ERROR_MSG_NUM * MACRO_CPROC_1X_MNTN_LOG_HANDLED_MSG_SAVE_INFO_SIZE
            analysis_cproc_dynamic_error_msg_list_info( instream, fileOffset, outstream, version)

        outstream.writelines(["\n\n---------- The end ----------"])
        #save2file.writelines(["\n\n---------- The end ----------"])
        	
        return True
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
"""

def analysis_cproc_dump_info_0100( infile, offset, outfile, version):
        instream = infile
        outstream  = outfile
        #fileOffset = eval(offset)
        fileOffset = offset

        outstream.writelines(["\n======================================================================================\n"])
        outstream.writelines(["CPROC DUMP ANALYSIS @20160311, Field version: %d.%d\n" % (version>>8, version&0xff)])
        outstream.writelines(["======================================================================================\n\n"])
        #outstream.writelines(["Output to txt file: c:\\modem_dump_cproc.txt\n\n"])
        #save2file.writelines(["======================================================================================\n"])
        #save2file.writelines(["CPROC DUMP ANALYSIS @20160311, Field version: %d.%d\n" % (version>>8, version&0xff)])
        #save2file.writelines(["======================================================================================\n\n"])
        #save2file.writelines(["Output to txt file: c:\\modem_dump_cproc.txt\n\n"])
        
        ######## analysis cproc 1x handled msg #########
        instream.seek(fileOffset) 
        (ulHandledMsgIndex,)  = struct.unpack('I', instream.read(4))
        (ulLastMsgTimeSlice,) = struct.unpack('I', instream.read(4))
        strTemp               = 'cproc 1x last msg timeslice: 0x%08X '% (ulLastMsgTimeSlice)
        outstream.writelines(["%-15s\n" % (strTemp)])
        #save2file.writelines(["%-15s\n" % (strTemp)])
        
        fileOffset = fileOffset + 8  
        outstream.writelines(["\n**************************** 1X: analysis cproc handled msg begin *******************************\n\n"])
        #save2file.writelines(["\n**************************** 1X: analysis cproc handled msg begin *******************************\n\n"])
        analysis_cproc_handled_msg_list_dump_info( instream, fileOffset, outstream, ulHandledMsgIndex, version)
        outstream.writelines(["\n**************************** 1X: analysis cproc handled msg end *******************************\n\n\n"])
        #save2file.writelines(["\n**************************** 1X: analysis cproc handled msg end *******************************\n\n\n"])


        ######## analysis cproc hrpd handled msg #########
        fileOffset = fileOffset + MACRO_CPROC_1X_MNTN_LOG_HANDLED_MSG_SAVE_INFO_SIZE * MACRO_CPROC_MNTN_MAX_HANDLED_MSG_SAVE_NUM
        
        instream.seek(fileOffset) 
        (ulHandledMsgIndex,)  = struct.unpack('I', instream.read(4))
        (ulLastMsgTimeSlice,) = struct.unpack('I', instream.read(4))
        strTemp               = 'cproc hrpd last msg timeslice: 0x%08X '% (ulLastMsgTimeSlice)
        outstream.writelines(["%-15s\n" % (strTemp)])
        #save2file.writelines(["%-15s\n" % (strTemp)])

        fileOffset = fileOffset + 8
        outstream.writelines(["\n**************************** HRPD: analysis cproc handled msg begin *******************************\n\n"])
        #save2file.writelines(["\n**************************** HRPD: analysis cproc handled msg begin *******************************\n\n"])
        analysis_cproc_handled_msg_list_dump_info( instream, fileOffset, outstream, ulHandledMsgIndex, version)
        outstream.writelines(["\n**************************** HRPD: analysis cproc handled msg end *******************************\n\n\n"])
        #save2file.writelines(["\n**************************** HRPD: analysis cproc handled msg end *******************************\n\n\n"])


        ######## analysis cproc rm handled msg #########
        fileOffset = fileOffset + MACRO_CPROC_1X_MNTN_LOG_HANDLED_MSG_SAVE_INFO_SIZE * MACRO_CPROC_MNTN_MAX_HANDLED_MSG_SAVE_NUM

        instream.seek(fileOffset) 
        (ulHandledMsgIndex,)  = struct.unpack('I', instream.read(4))
        (ulLastMsgTimeSlice,) = struct.unpack('I', instream.read(4))
        strTemp               = 'cproc rm last msg timeslice: 0x%08X '% (ulLastMsgTimeSlice)
        outstream.writelines(["%-15s\n" % (strTemp)])
        #save2file.writelines(["%-15s\n" % (strTemp)])

        fileOffset = fileOffset + 8
        outstream.writelines(["\n**************************** RM: analysis cproc handled msg begin *******************************\n\n"])
        #save2file.writelines(["\n**************************** RM: analysis cproc handled msg begin *******************************\n\n"])
        analysis_cproc_handled_msg_list_dump_info( instream, fileOffset, outstream, ulHandledMsgIndex, version)
        outstream.writelines(["\n**************************** RM: analysis cproc handled msg end *******************************\n\n\n"])
        #save2file.writelines(["\n**************************** RM: analysis cproc handled msg end *******************************\n\n\n"])

		######## analysis cproc hrpd extern handled msg #########
        fileOffset = fileOffset + MACRO_CPROC_1X_MNTN_LOG_HANDLED_MSG_SAVE_INFO_SIZE * MACRO_CPROC_MNTN_MAX_HANDLED_MSG_SAVE_NUM

        instream.seek(fileOffset)
        (ulErrorIndFlag,)     = struct.unpack('I', instream.read(4))
        (ulHandledMsgIndex,)  = struct.unpack('I', instream.read(4))
        (ulLastMsgTimeSlice,) = struct.unpack('I', instream.read(4))
        strTemp               = 'cproc hrpd extern last msg timeslice: 0x%08X '% (ulLastMsgTimeSlice)
        outstream.writelines(["%-15s\n" % (strTemp)])
        #save2file.writelines(["%-15s\n" % (strTemp)])

        fileOffset = fileOffset + 12
        outstream.writelines(["\n**************************** HRPD EXTERN: analysis cproc handled msg begin *******************************\n\n"])
        #save2file.writelines(["\n**************************** HRPD EXTERN: analysis cproc handled msg begin *******************************\n\n"])
        analysis_cproc_handled_msg_list_dump_info( instream, fileOffset, outstream, ulHandledMsgIndex, version)
        outstream.writelines(["\n**************************** HRPD EXTERN: analysis cproc handled msg end *******************************\n\n\n"])
        #save2file.writelines(["\n**************************** HRPD EXTERN: analysis cproc handled msg end *******************************\n\n\n"])
		
        ######## analysis cproc hrpd waitlist #########
        ulWaitListLoop   = 0
        fileOffset = fileOffset + MACRO_CPROC_1X_MNTN_LOG_HANDLED_MSG_SAVE_INFO_SIZE * MACRO_CPROC_MNTN_MAX_HANDLED_MSG_SAVE_NUM

        outstream.writelines(["\n**************************** HRPD FSM WAIT_LIST: analysis begin *******************************\n\n"])
        #save2file.writelines(["\n**************************** HRPD FSM WAIT_LIST: analysis begin *******************************\n\n"])
        
        outstream.writelines(["%-50s%-50s\n" % ("FsmId/ExceptionId", "usWaitList")])
        #save2file.writelines(["%-50s%-50s\n" % ("FsmId/ExceptionId", "usWaitList")])
        
        while ulWaitListLoop < MACRO_CPROC_HRPD_MNTN_MAX_WAIT_LIST_NUM:
                fileLocalOffset = fileOffset + ulWaitListLoop * 4
                analysis_cproc_hrpd_mntn_per_fsm_waitlist_info(instream, fileLocalOffset, outstream)
                ulWaitListLoop = ulWaitListLoop + 1
        
        outstream.writelines(["\n**************************** HRPD FSM WAIT_LIST: analysis end *******************************\n\n\n"])
        #save2file.writelines(["\n**************************** HRPD FSM WAIT_LIST: analysis end *******************************\n\n\n"])
        
		######## analysis cproc hrpd fsm #########
        fileOffset = fileOffset + MACRO_CPROC_HRPD_MNTN_MAX_WAIT_LIST_NUM * 4 + MACRO_CPROC_1X_MNTN_INT_SPEND_TIME_INFO_SIZE

        instream.seek(fileOffset)
        (ulHandledMsgIndex,)  = struct.unpack('I', instream.read(4))
        (ulLastMsgTimeSlice,) = struct.unpack('I', instream.read(4))
        strTemp               = 'cproc hrpd last fsm record timeslice: 0x%08X '% (ulLastMsgTimeSlice)
        outstream.writelines(["%-15s\n" % (strTemp)])
        #save2file.writelines(["%-15s\n" % (strTemp)])

        fileOffset = fileOffset + 8
        outstream.writelines(["\n**************************** HRPD FSM: analysis cproc state machine begin *******************************\n\n"])
        #save2file.writelines(["\n**************************** HRPD FSM: analysis cproc state machine begin *******************************\n\n"])
        analysis_cproc_fsm_list_dump_info(instream, fileOffset, outstream, ulHandledMsgIndex, version)
        outstream.writelines(["\n**************************** HRPD FSM: analysis cproc state machine end *******************************"])
        #save2file.writelines(["\n**************************** HRPD FSM: analysis cproc state machine end *******************************"])
		
        return True
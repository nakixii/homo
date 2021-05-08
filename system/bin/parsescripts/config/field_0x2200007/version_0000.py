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

def analysis_cproc_dump_info_0000( infile, offset, outfile, version):
        instream = infile
        outstream  = outfile
        #fileOffset = eval(offset)
        fileOffset = offset

        outstream.writelines(["\n***********************************************************\n"])
        outstream.writelines(["******** CPROC DUMP ANALYSIS by CAS Team 20160311 *********\n"])
        outstream.writelines(["***********************************************************\n\n"])
        #outstream.writelines(["Output to txt file: c:\\modem_dump_cproc.txt\n\n"])

        #save2file.writelines(["***********************************************************\n"])
        #save2file.writelines(["******** CPROC DUMP ANALYSIS by CAS Team 20160311 *********\n"])
        #save2file.writelines(["***********************************************************\n\n"])
        
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
		
		######## analysis cproc hrpd fsm #########
        fileOffset = fileOffset + MACRO_CPROC_1X_MNTN_LOG_HANDLED_MSG_SAVE_INFO_SIZE * MACRO_CPROC_MNTN_MAX_HANDLED_MSG_SAVE_NUM + MACRO_CPROC_1X_MNTN_INT_SPEND_TIME_INFO_SIZE

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
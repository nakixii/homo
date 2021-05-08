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
from cproc_pid import *
from cproc_cas_1x_msg import *
from cproc_cas_hrpd_msg import *
from cproc_1x_internal_msg import *
from cproc_apm_msg import *
from cproc_cbt_msg import *
from cproc_csdr_1x_msg import *
from cproc_csdr_hrpd_msg import *
from cproc_cttf_hrpd_msg import *
from cproc_hrpd_internal_msg import *
from cproc_rm_msg import *
from cproc_tas_msg import *
from cproc_hrpd_fsm import *
from cproc_other_msg import *

MACRO_CPROC_MNTN_MAX_HANDLED_MSG_SAVE_NUM                 = 120
MACRO_CPROC_1X_MNTN_LOG_HANDLED_MSG_SAVE_INFO_SIZE   = 8
MACRO_CPROC_1X_MNTN_INT_SPEND_TIME_INFO_SIZE                 = 96
MACRO_CPROC_MNTN_MAX_FSM_REG_KILL_INFO_NUM                  = 50
MACRO_CPROC_MNTN_MAX_DYNAMIC_ERROR_MSG_NUM                = 50
 
def cproc_get_msg_str( pid1, pid2, usMsgId, outstream, version):
        if ( (pid1.upper() in ['1XCTAS']) or (pid2.upper() in ['1XCTAS'])):
                return get_cproc_tas_msg_str(usMsgId, version)

        elif ( (pid1.upper() in ['OM']) or (pid2.upper() in ['OM'])):
                return get_cproc_other_msg_str(usMsgId, version)
				
        elif ( (pid1.upper() in ['CPROC_1XDSP']) and (pid2.upper() in ['DSP_PROCSTUB', 'CSDR_1XCM', 'CSDR_1XSM'])):
                return get_cproc_csdr_1x_msg_str(usMsgId, version)

        elif ( (pid2.upper() in ['CPROC_1XDSP']) and (pid1.upper() in ['DSP_PROCSTUB', 'CSDR_1XCM', 'CSDR_1XSM'])):
                return get_cproc_csdr_1x_msg_str(usMsgId, version)

        elif ( (pid1.upper() in ['CPROC_1XCM', 'CPROC_1XSM']) and (pid2.upper() in ['1XCASM', '1XCSRCH', '1XCMEAS'])):
                return get_cas_cproc_1x_msg_str(usMsgId, version) 
                 
        elif ( (pid2.upper() in ['CPROC_1XCM', 'CPROC_1XSM']) and (pid1.upper() in ['1XCASM', '1XCSRCH', '1XCMEAS'])):
                return get_cas_cproc_1x_msg_str(usMsgId, version) 

        elif ( (pid1.upper() in ['HRPD_CM', 'HRPD_SM']) and (pid2.upper() in ['HALMP', 'HSP', 'HRUP', 'HSCP'])):
                return get_cas_cproc_hrpd_msg_str(usMsgId, version) 

        elif ( (pid2.upper() in ['HRPD_CM', 'HRPD_SM']) and (pid1.upper() in ['HALMP', 'HSP', 'HRUP', 'HSCP'])):
                return get_cas_cproc_hrpd_msg_str(usMsgId, version)

        elif ( (pid1.upper() in ['CPROC_RM']) or (pid2.upper() in ['CPROC_RM'])):
                return get_cproc_rm_msg_str(usMsgId, version)

        elif ( (pid1.upper() in ['HRPDRMAC']) or (pid2.upper() in ['HRPDRMAC'])):
                return get_cproc_cttf_hrpd_msg_str(usMsgId, version)

        elif ( (pid1.upper() in ['CBT']) or (pid2.upper() in ['CBT'])):
                return get_cproc_cbt_msg_str(usMsgId, version)

        elif ( (pid1.upper() in ['CPROC_1XCM', 'CPROC_1XSM']) and (pid2.upper() in ['DSP_PROCSTUB', 'CSDR_1XCM', 'CSDR_1XSM'])):
                return get_cproc_csdr_1x_msg_str(usMsgId, version)

        elif ( (pid2.upper() in ['CPROC_1XCM', 'CPROC_1XSM']) and (pid1.upper() in ['DSP_PROCSTUB', 'CSDR_1XCM', 'CSDR_1XSM'])):
                return get_cproc_csdr_1x_msg_str(usMsgId, version)
        
        elif ( (pid1.upper() in ['HRPD_CM', 'HRPD_SM']) and (pid2.upper() in ['DSP_PROCSTUB', 'CSDR_HRPDCM', 'CSDR_HRPDSM'])):
                return get_cproc_csdr_hrpd_msg_str(usMsgId, version) 

        elif ( (pid2.upper() in ['HRPD_CM', 'HRPD_SM']) and (pid1.upper() in ['DSP_PROCSTUB', 'CSDR_HRPDCM', 'CSDR_HRPDSM'])):
                return get_cproc_csdr_hrpd_msg_str(usMsgId, version)

        elif ( (pid1.upper() in ['CPROC_1XCM', 'CPROC_1XSM']) and (pid2.upper() in ['CPROC_1XCM', 'CPROC_1XSM'])):
                return get_cproc_1x_internal_msg_str(usMsgId, version)

        elif ( (pid1.upper() in ['HRPD_CM', 'HRPD_SM']) and (pid2.upper() in ['HRPD_CM', 'HRPD_SM'])):
                return get_cproc_hrpd_internal_msg_str(usMsgId, version)

        elif ( (pid1.upper() in ['CPROC_1XCM']) and (pid2.upper() in ['CPROC_1XCM'])):
                return get_cproc_1x_internal_msg_str(usMsgId, version)

        elif ( (pid1.upper() in ['CPROC_1XSM']) and (pid2.upper() in ['CPROC_1XSM'])):
                return get_cproc_1x_internal_msg_str(usMsgId, version)
				
        elif ( (pid1.upper() in ['APM']) and (pid2.upper() in ['HRPD_CM', 'CPROC_1XCM'])):
                return get_cproc_apm_msg_str(usMsgId, version)
				
        elif ( (pid2.upper() in ['APM']) and (pid1.upper() in ['HRPD_CM', 'CPROC_1XCM'])):
                return get_cproc_apm_msg_str(usMsgId, version)
				
        elif ( (pid1.upper() in ['CPROC_1XCM']) and (pid2.upper() in ['CPROC_1XDSP'])):
                return get_cproc_1x_internal_msg_str(usMsgId, version)
				
        elif ( (pid2.upper() in ['CPROC_1XCM']) and (pid1.upper() in ['CPROC_1XDSP'])):
                return get_cproc_1x_internal_msg_str(usMsgId, version)
				
        elif ( (pid1.upper() in ['HRPD_CM']) and (pid2.upper() in ['RCM'])):
                return get_cproc_tas_msg_str(usMsgId, version)
		
        elif ( (pid1.upper() in ['HRPD_CM']) and (pid2.upper() in ['IDLE'])):
                return get_cproc_other_msg_str(usMsgId, version);
				
        elif ( (pid1.upper() in ['SHPA']) or (pid2.upper() in ['CPROC_1XCM'])):
                return get_cproc_cbt_msg_str(usMsgId, version)
        
        elif ( (pid2.upper() in ['SHPA']) or (pid1.upper() in ['CPROC_1XCM'])):
                return get_cproc_cbt_msg_str(usMsgId, version)
		
        elif ( (pid1.upper() in ['RCM']) or (pid2.upper() in ['RCM'])):
                return get_cproc_rm_msg_str(usMsgId, version)
		
        else:
                return get_cproc_other_msg_str(usMsgId, version);


def analysis_cproc_mntn_each_msg_info(instream, fileLocalOffset, outstream, version):
        instream.seek(fileLocalOffset)

        if (version == 0x0102 or version == 0x0103):
            (MsgId,)          = struct.unpack('H', instream.read(2))
            (SendPid,)        = struct.unpack('B', instream.read(1)) 
            (RcvPid,)         = struct.unpack('B', instream.read(1)) 
            (TimeStamp,)   = struct.unpack('I', instream.read(4))
        else:
            (TimeStamp,)      = struct.unpack('H', instream.read(2))
            (MsgId,)          = struct.unpack('H', instream.read(2))
            (SendPid,)        = struct.unpack('H', instream.read(2))
            (RcvPid,)         = struct.unpack('H', instream.read(2))
       
        if (SendPid == 0 or RcvPid == 0 or MsgId == 0):
            return True

        strSendPid      = cproc_get_pid_str(SendPid, outstream)
        strRcvPid       = cproc_get_pid_str(RcvPid, outstream)
        strMsgId        = cproc_get_msg_str(strSendPid, strRcvPid, MsgId, outstream, version)

        if (strMsgId.upper() in ['UNKNOWN']):
            strMsgId = get_cproc_other_msg_str(MsgId, version);
        
        strSendPid      = '%s(0x%02X)' % (strSendPid, SendPid)
        strRcvPid       = '%s(0x%02X)' % (strRcvPid, RcvPid)
        strMsgId        = '%s(0x%04X)' % (strMsgId, MsgId)
        strTimeStamp    = '%08X'% TimeStamp
        
        outstream.writelines(["0x%-13s%-25s%-25s%-60s\n" % (strTimeStamp.upper(), strSendPid, strRcvPid, strMsgId)])
        #save2file.writelines(["%-15s%-25s%-25s%-60s\n" % (strTimeStamp.upper(), strSendPid, strRcvPid, strMsgId)])
        

def analysis_cproc_handled_msg_list_dump_info( instream, fileOffset, outstream, ulCurMsgIndex, version):
        ulLooper        = ulCurMsgIndex
        
        #outstream.writelines(["Current msg index: %d\n" % (ulCurMsgIndex)])
        
        outstream.writelines(["%-15s%-25s%-25s%-60s\n" % ("usTimeStamp", "usSendPid", "usReceivePid","usMsgId")])
        #save2file.writelines(["%-15s%-25s%-25s%-60s\n" % ("usTimeStamp", "usSendPid", "usReceivePid","usMsgId")])
        
        while ulLooper < (MACRO_CPROC_MNTN_MAX_HANDLED_MSG_SAVE_NUM + ulCurMsgIndex):
                ulLooperIndex = ulLooper % MACRO_CPROC_MNTN_MAX_HANDLED_MSG_SAVE_NUM
                fileLocalOffset = fileOffset + ulLooperIndex * MACRO_CPROC_1X_MNTN_LOG_HANDLED_MSG_SAVE_INFO_SIZE
                analysis_cproc_mntn_each_msg_info(instream, fileLocalOffset, outstream, version)
                ulLooper = ulLooper + 1

        return True

def analysis_cproc_mntn_per_fsm_info(instream, fileLocalOffset, outstream, version):
        instream.seek(fileLocalOffset)
	
        (ucTimestamp,)      = struct.unpack('B', instream.read(1))    
        (ucFsmId,)          = struct.unpack('B', instream.read(1))
        (ucCurState,)       = struct.unpack('B', instream.read(1))
        (ucNewState,)       = struct.unpack('B', instream.read(1))
		
        #outstream.writelines(["%02x-%02x-%02x-%02x\n" % (ucTimestamp, ucFsmId, ucCurState, ucNewState)])
        
        if (ucFsmId == 0):
            return True

        strTimestamp    = '0x%02X'% (ucTimestamp)
        strFsmId        = get_cproc_hrpd_fsm_str(ucFsmId)
        #strCurState     = '%s(0x%X)'% ("none", ucCurState)
        #strNewState     = '%s(0x%X)'% ("none", ucNewState)
        strCurState     = '%s(0x%X)'% (get_cproc_hrpd_fsm_state_str(strFsmId, ucCurState, version), ucCurState)
        strNewState     = '%s(0x%X)'% (get_cproc_hrpd_fsm_state_str(strFsmId, ucNewState, version), ucNewState)
        strFsmId      = '%s(0x%04X)'% (strFsmId, ucFsmId)
		
        outstream.writelines(["%-15s%-50s%-35s%-35s\n" % (strTimestamp, strFsmId, strCurState, strNewState)])
        #save2file.writelines(["%-15s%-50s%-35s%-35s\n" % (strTimestamp, strFsmId, strCurState, strNewState)])
		
		
def analysis_cproc_fsm_list_dump_info( instream, fileOffset, outstream, ulCurMsgIndex, version):
        ulLooper        = ulCurMsgIndex

        #outstream.writelines(["Current msg index: 0x%04X\n" % (fileOffset)])
        
        outstream.writelines(["%-15s%-50s%-35s%-35s\n" % ("ucTimeStamp", "ucFsmId", "ucCurrentState", "ucNewState")])
        #save2file.writelines(["%-15s%-50s%-35s%-35s\n" % ("ucTimeStamp", "ucFsmId", "ucCurrentState", "ucNewState")])
        
        while ulLooper < (MACRO_CPROC_MNTN_MAX_HANDLED_MSG_SAVE_NUM + ulCurMsgIndex):
                ulLooperIndex = ulLooper % MACRO_CPROC_MNTN_MAX_HANDLED_MSG_SAVE_NUM
                fileLocalOffset = fileOffset + ulLooperIndex * 4
                #outstream.writelines(["Current msg index: %04X\n" % (fileLocalOffset)])
                analysis_cproc_mntn_per_fsm_info(instream, fileLocalOffset, outstream, version)
                ulLooper = ulLooper + 1

        return True

        
def analysis_cproc_hrpd_mntn_per_fsm_waitlist_info(instream, fileLocalOffset, outstream):
        instream.seek(fileLocalOffset)
	
        (usId,)         = struct.unpack('H', instream.read(2))
        (usWaitList,)   = struct.unpack('H', instream.read(2))
		
        #outstream.writelines(["%04x-%04x\n" % (usId, usWaitList)])
        
        if (usId == 0):
            return True

        strId           = get_cproc_hrpd_fsm_str(usId)
        strWaitList     = '0x%04X'% (usWaitList)
		
        outstream.writelines(["%-50s%-50s\n" % (strId, strWaitList)])
        #save2file.writelines(["%-50s%-50s\n" % (strId, strWaitList)])

def analysis_cproc_hrpd_mntn_fsm_reg_kill_info(instream, fileLocalOffset, outstream):
        instream.seek(fileLocalOffset)
        (ulTimeStamp,)         = struct.unpack('I', instream.read(4))
        (ulFsmId,)                = struct.unpack('I', instream.read(4))
        (ulFsmPointer,)         = struct.unpack('I', instream.read(4))

        instream.seek(fileLocalOffset + 12 * MACRO_CPROC_MNTN_MAX_FSM_REG_KILL_INFO_NUM)
        (ulTimeStamp2,)         = struct.unpack('I', instream.read(4))
        (ulFsmId2,)                = struct.unpack('I', instream.read(4))
        (ulFsmPointer2,)         = struct.unpack('I', instream.read(4))

        strTimeStamp    = '0x%08x' % ulTimeStamp
        #strFsmId           = '%08x' % ulFsmId
        #child fsm mask is 0x10000
        strFsmId          = '%s(0x%x)' % (get_cproc_hrpd_fsm_str(ulFsmId & 0xffff), ulFsmId)
        strFsmPointer    = '0x%08x' % ulFsmPointer

        strTimeStamp2    = '0x%08x' % ulTimeStamp2
        #strFsmId2           = '%08x' % ulFsmId2
        strFsmId2          = '%s(0x%x)' % (get_cproc_hrpd_fsm_str(ulFsmId2 & 0xff), ulFsmId2)
        strFsmPointer2    = '0x%08x' % ulFsmPointer2        
        
        outstream.writelines(["%-15s%-40s%-30s%-15s%-40s%-25s\n" % (strTimeStamp, strFsmId, strFsmPointer, strTimeStamp2, strFsmId2, strFsmPointer2)])
        #save2file.writelines(["%-15s%-40s%-30s%-15s%-40s%-25s\n" % (strTimeStamp.upper(), strFsmId, strFsmPointer.upper(), strTimeStamp2.upper(), strFsmId2, strFsmPointer2.upper())])

def analysis_cproc_mntn_each_ess_event_info(instream, fileLocalOffset, outstream, version):
        instream.seek(fileLocalOffset)

        (ulTimeStamp,)   = struct.unpack('I', instream.read(4))
        (ulEssEvent,)     = struct.unpack('I', instream.read(4))
        
        if (ulEssEvent == 0):
            return True

        strEssEvent = '0x%08X(Event:%08X)' % (ulTimeStamp, ulEssEvent)
        
        outstream.writelines(["%s " % (strEssEvent)])
        #save2file.writelines(["%s " % (strEssEvent)])

def analysis_cproc_dynamic_error_msg_list_info( instream, fileOffset, outstream, version):
        ulLooper     = 0
        ulMsgIndex  = (MACRO_CPROC_MNTN_MAX_DYNAMIC_ERROR_MSG_NUM - 1)
        
        outstream.writelines(["%-15s%-25s%-25s%-60s\n" % ("TimeStamp", "SendPid", "ReceivePid","MsgId")])
        #save2file.writelines(["%-15s%-25s%-25s%-60s\n" % ("TimeStamp", "SendPid", "ReceivePid","MsgId")])
        
        while ulLooper < MACRO_CPROC_MNTN_MAX_DYNAMIC_ERROR_MSG_NUM:
                fileLocalOffset = fileOffset + ulMsgIndex * MACRO_CPROC_1X_MNTN_LOG_HANDLED_MSG_SAVE_INFO_SIZE
                analysis_cproc_mntn_each_msg_info(instream, fileLocalOffset, outstream, version)
                ulMsgIndex = ulMsgIndex - 1
                ulLooper = ulLooper + 1

        return True

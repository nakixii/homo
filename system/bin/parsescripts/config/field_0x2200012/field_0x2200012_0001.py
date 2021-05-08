#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   analysis taf dump bin
modify  record  :   2019-05-13 create file
"""

import struct
import os
import sys
import string
from dsm_pid import *
from dsm_fsm_id import *
from ads_dsm_msg import *
from taf_dsm_msg import *
from cds_dsm_msg import *
from at_dsm_msg import *
from imsa_dsm_msg import *
from dsm_internal_msg import *

MACRO_NAS_EXC_LOG_LENGTH_MODEM           = 0x1800
MACRO_TAF_DSM_MAX_LOG_EVENT_STATE_NUM    = 20
MACRO_TAF_DSM_MNTN_LOG_MSG_INFO_SIZE     = 24
MACRO_TAF_DSM_MAX_GROUP_DUMP_NUM         = 16
MACRO_TAF_DSM_MAX_GROUP_DUMP_INFO_SIZE   = 12
MACRO_TAF_DSM_MAX_PDN_DUMP_NUM              = 32
MACRO_TAF_DSM_MAX_PDN_DUMP_INFO_SIZE     = 12
MACRO_TAF_DSM_MAX_BEARER_DUMP_NUM         = 32
MACRO_TAF_DSM_MAX_BEARER_DUMP_INFO_SIZE  = 28 
MACRO_TAF_DSM_MAX_SAVE_DUMP_INFO_SIZE    = 1480
MACRO_TAF_XSMS_MAX_TIMER_DUMP_NUM        = 64
MACRO_TAF_XSMS_MAX_TIMER_ID_NUM          = 33

GLOBAL_Offset = 0
modem_index   = 0
g_offset      = 0

def get_dsm_msgid_str( pid1, pid2, usMsgId):
        if ( 'dsm' == pid1.lower() and 'at' == pid2.lower()):
                return get_at_dsm_msg_str(usMsgId)
        elif ( 'i1_dsm' == pid1.lower() and 'at' == pid2.lower()):
                return get_at_dsm_msg_str(usMsgId)      
        elif ( 'i2_dsm' == pid1.lower() and 'at' == pid2.lower()):
                return get_at_dsm_msg_str(usMsgId)
        elif ( 'at' == pid1.lower() and 'dsm' == pid2.lower()):
                return get_at_dsm_msg_str(usMsgId)
        elif ( 'at' == pid1.lower() and 'i1_dsm' == pid2.lower()):
              return get_at_dsm_msg_str(usMsgId)
        elif ( 'at' == pid1.lower() and 'i2_dsm' == pid2.lower()):
              return get_at_dsm_msg_str(usMsgId)            
            
        elif ( 'dsm' == pid1.lower() and 'imsa' == pid2.lower()):
                return get_imsa_dsm_msg_str(usMsgId)
        elif ( 'i1_dsm' == pid1.lower() and 'i1_imsa' == pid2.lower()):
                return get_imsa_dsm_msg_str(usMsgId)      
        elif ( 'i2_dsm' == pid1.lower() and 'i2_imsa' == pid2.lower()):
                return get_imsa_dsm_msg_str(usMsgId)
        elif ( 'imsa' == pid1.lower() and 'dsm' == pid2.lower()):
                return get_imsa_dsm_msg_str(usMsgId)
        elif ( 'i1_imsa' == pid1.lower() and 'i1_dsm' == pid2.lower()):
              return get_imsa_dsm_msg_str(usMsgId)
        elif ( 'i2_imsa' == pid1.lower() and 'i2_dsm' == pid2.lower()):
              return get_imsa_dsm_msg_str(usMsgId)
              
        elif ( 'dsm' == pid1.lower() and 'ads' == pid2.lower()):
                return get_ads_dsm_msg_str(usMsgId)
        elif ( 'i1_dsm' == pid1.lower() and 'ads' == pid2.lower()):
                return get_ads_dsm_msg_str(usMsgId)      
        elif ( 'i2_dsm' == pid1.lower() and 'ads' == pid2.lower()):
                return get_ads_dsm_msg_str(usMsgId)
        
        elif ( 'dsm' == pid1.lower() and 'cds' == pid2.lower()):
                return get_cds_dsm_msg_str(usMsgId)
        elif ( 'i1_dsm' == pid1.lower() and 'cds' == pid2.lower()):
                return get_cds_dsm_msg_str(usMsgId)      
        elif ( 'i2_dsm' == pid1.lower() and 'cds' == pid2.lower()):
                return get_cds_dsm_msg_str(usMsgId)
        
        elif ( 'dsm' == pid1.lower() and 'dsm' == pid2.lower()):
                return get_dsm_inter_msg_str(usMsgId)
        elif ( 'i1_dsm' == pid1.lower() and 'i1_dsm' == pid2.lower()):
                return get_dsm_inter_msg_str(usMsgId)      
        elif ( 'i2_dsm' == pid1.lower() and 'i2_dsm' == pid2.lower()):
                return get_dsm_inter_msg_str(usMsgId)
        
        elif ( 'dsm' == pid1.lower() and 'taf' == pid2.lower()):
                return get_taf_dsm_msg_str(usMsgId)
        elif ( 'taf' == pid1.lower() and 'dsm' == pid2.lower()):
                return get_taf_dsm_msg_str(usMsgId)
        elif ( 'i1_dsm' == pid1.lower() and 'i1_taf' == pid2.lower()):
                return get_taf_dsm_msg_str(usMsgId)      
        elif ( 'i1_taf' == pid1.lower() and 'i1_dsm' == pid2.lower()):
                return get_taf_dsm_msg_str(usMsgId)
        elif ( 'i2_dsm' == pid1.lower() and 'i2_taf' == pid2.lower()):
                return get_taf_dsm_msg_str(usMsgId)      
        elif ( 'i2_taf' == pid1.lower() and 'i2_dsm' == pid2.lower()):
                return get_taf_dsm_msg_str(usMsgId)
                
        else:
                return 'none'

def analysis_dsm_mntn_per_rec_msg_info( instream, fileLocalOffset, outstream, ulLooper):
        instream.seek(fileLocalOffset)

        (ulReceiveTime,) = struct.unpack('I', instream.read(4))
        (ulExitTime,)    = struct.unpack('I', instream.read(4))

        (usSendPid,)     = struct.unpack('I', instream.read(4))
        (usRcvPid,)      = struct.unpack('I', instream.read(4))

        (usMsgId,)       = struct.unpack('I', instream.read(4))
        (ucMainFsmId,)   = struct.unpack('B', instream.read(1))
        (ucMainState,)   = struct.unpack('B', instream.read(1))
        (ucSubFsmId,)    = struct.unpack('B', instream.read(1))
        (ucSubState,)    = struct.unpack('B', instream.read(1))

        strSendPid       = taf_dsm_get_pid_str(usSendPid)
        strRcvPid        = taf_dsm_get_pid_str(usRcvPid)
        strMsgId         = get_dsm_msgid_str(strSendPid, strRcvPid, usMsgId)
        
        strSendPid       = '%s(0x%x)' % ( strSendPid, usSendPid)
        strRcvPid        = '%s(0x%x)' % ( strRcvPid, usRcvPid)
        strMsgId         = '%s(0x%x)' % ( strMsgId, usMsgId)
        strReceiveTime   = '0x%x'% ulReceiveTime
        strExitTime      = '0x%x'% ulExitTime

        strMainFsmId     = '0x%x' % ucMainFsmId 
        
        strDsmState      = taf_dsm_get_fsm_state_str(ucMainState)
        strDsmState      = '%s(0x%x)' % ( strDsmState, ucMainState)  
        strSubFsmId      = '0x%x' % ucSubFsmId
        strSubState      = '0x%x' % ucSubState
  
        #outstream.writelines(["\n**************************** (-.^): *******************************\n"])
        outstream.writelines(["%-10s%-15s%-15s%-15s%-15s%-55s%-20s%-20s%-20s%-20s\n" % (ulLooper, strReceiveTime.upper(), strExitTime.upper(), strSendPid, strRcvPid, strMsgId, strMainFsmId, strDsmState, strSubFsmId, strSubState)])  
       
       
def analysis_dsm_mntn_per_group_info( instream, outstream, ulLooper):

        (ucDsmGroupInst,)   = struct.unpack('B', instream.read(1))
        (ucUserPdpType,)    = struct.unpack('B', instream.read(1))
        (ucRmNetId,)        = struct.unpack('B', instream.read(1))
        (enCurrIpv4State,)  = struct.unpack('B', instream.read(1))
        (enCurrIpv6State,)  = struct.unpack('B', instream.read(1))
        (enCurrNonIpState,) = struct.unpack('B', instream.read(1))
        (enPastIpv4State,)  = struct.unpack('B', instream.read(1))
        (enPastIpv6State,)  = struct.unpack('B', instream.read(1))
        (enPastNonIpState,) = struct.unpack('B', instream.read(1))
        (ucReserve,)        = struct.unpack('B', instream.read(1))
        (ucReserve,)        = struct.unpack('B', instream.read(1))
        (ucReserve,)        = struct.unpack('B', instream.read(1))
        
        strDsmGroupInst       = '0x%x' % ucDsmGroupInst
        strUserPdpType        = '0x%x' % ucUserPdpType
        strRmNetId            = '0x%x' % ucRmNetId
        strCurrIpv4State      = '0x%x' % enCurrIpv4State
        strCurrIpv6State      = '0x%x' % enCurrIpv6State
        strCurrNonIpState     = '0x%x' % enCurrNonIpState
        strPastIpv4State      = '0x%x' % enPastIpv4State
        strPastIpv6State      = '0x%x' % enPastIpv6State
        strPastNonIpState     = '0x%x' % enPastNonIpState
  
        #outstream.writelines(["\n**************************** (-.^): *******************************\n"])
        outstream.writelines(["%-10s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s\n" % (ulLooper, strDsmGroupInst, strUserPdpType, strRmNetId, strCurrIpv4State, strCurrIpv6State, strCurrNonIpState, strPastIpv4State, strPastIpv6State, strPastNonIpState)])  
          

def analysis_dsm_mntn_per_pdn_info( instream, outstream, ulLooper):

        (ucDsmPdnInst,)       = struct.unpack('B', instream.read(1))
        (ucPduSessionId,)     = struct.unpack('B', instream.read(1))
        (ucState,)            = struct.unpack('B', instream.read(1))
        (ucRequestType,)      = struct.unpack('B', instream.read(1))
        (ucAccessType,)       = struct.unpack('B', instream.read(1))
        (ucCnRatType,)        = struct.unpack('B', instream.read(1))
        (ucReserve,)          = struct.unpack('B', instream.read(1))
        (ucReserve,)          = struct.unpack('B', instream.read(1))

        strDsmPdnInst         = '0x%x' % ucDsmPdnInst
        strPduSessionId       = '0x%x' % ucPduSessionId
        strState              = '0x%x' % ucState
        strRequestType        = '0x%x' % ucRequestType
        strAccessType         = '0x%x' % ucAccessType
        strCnRatType          = '0x%x' % ucCnRatType

        #outstream.writelines(["\n**************************** (-.^): *******************************\n"])
        outstream.writelines(["%-10s%-20s%-20s%-20s%-20s%-20s%-20s%\n" % \
(ulLooper, strDsmPdnInst, strPduSessionId, strState, strRequestType, \
strAccessType, strCnRatType)])

def analysis_dsm_mntn_per_bearer_info( instream, outstream, ulLooper):

        (ucDsmPdnInst,)       = struct.unpack('B', instream.read(1))
        (ucDsmBearerInst,)    = struct.unpack('B', instream.read(1))
        (ucPsCallId,)         = struct.unpack('B', instream.read(1))
        (ucBearerId,)         = struct.unpack('B', instream.read(1))
        (ucQfi,)              = struct.unpack('B', instream.read(1))
        (ucBearerType,)       = struct.unpack('B', instream.read(1))
        (ucBearerStatus,)     = struct.unpack('B', instream.read(1))
        (ucReserve,)          = struct.unpack('B', instream.read(1))
        (ucCurrCid,)          = struct.unpack('B', instream.read(1))
        (ucGroupInst1,)       = struct.unpack('B', instream.read(1))
        (ucGroupInst2,)       = struct.unpack('B', instream.read(1))
        (ucReserve,)          = struct.unpack('B', instream.read(1))
        (ulModuleId1,)        = struct.unpack('I', instream.read(4))
        (ulModuleId2,)        = struct.unpack('I', instream.read(4))
        (usClientId1,)        = struct.unpack('H', instream.read(2))
        (usClientId2,)        = struct.unpack('H', instream.read(2))
        (ulBitCidMask,)       = struct.unpack('I', instream.read(4))
        
        strDsmPdnInst         = '0x%x' % ucDsmPdnInst
        strDsmBearerInst      = '0x%x' % ucDsmBearerInst
        strPsCallId           = '0x%x' % ucPsCallId
        strBearerId           = '0x%x' % ucBearerId
        strQfi                = '0x%x' % ucQfi
        strBearerType         = '0x%x' % ucBearerType
        strBearerStatus       = '0x%x' % ucBearerStatus
        strCurrCid            = '0x%x' % ucCurrCid
        strGroupInst1         = '0x%x' % ucGroupInst1
        strGroupInst2         = '0x%x' % ucGroupInst2
        strModuleId1          = '0x%x' % ulModuleId1
        strModuleId2          = '0x%x' % ulModuleId2
        strClientId1          = '0x%x' % usClientId1
        strClientId2          = '0x%x' % usClientId2
        strBitCidMask         = '0x%x' % ulBitCidMask
  
        #outstream.writelines(["\n**************************** (-.^): *******************************\n"])
        outstream.writelines(["%-10s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s\n" % (ulLooper, strDsmPdnInst, strDsmBearerInst, strPsCallId, strBearerId, strQfi, strBearerType, strBearerStatus, strCurrCid, strGroupInst1, strGroupInst2, strModuleId1, strModuleId2, strClientId1, strClientId2, strBitCidMask)])  


def analysis_taf_mntn_log_dsm_dump_info( instream, outstream):
        ulLooper = 0
        fileOffset = 0
        
        outstream.writelines(["%-10s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s\n" % ("index","ucDsmGroupInst", "ucUserPdpType", "ucRmNetId", "enCurrIpv4State", "enCurrIpv6State", "enCurrNonIpState", "enPastIpv4State", "enPastIpv6State", "enPastNonIpState")])
        while ulLooper < MACRO_TAF_DSM_MAX_GROUP_DUMP_NUM:
            analysis_dsm_mntn_per_group_info( instream, outstream, ulLooper)
            ulLooper = ulLooper + 1

        ulLooper = 0
        outstream.writelines(["%-10s%-20s%-20s%-20s%-20s%-20s%-20s%\n" % \
("index", "ucDsmPdnInst", "ucPduSessionId", "ucState", "ucRequestType", \
"ucAccessType", "ucCnRatType")])

        while ulLooper < MACRO_TAF_DSM_MAX_PDN_DUMP_NUM:
            analysis_dsm_mntn_per_pdn_info( instream, outstream, ulLooper)
            ulLooper = ulLooper + 1
        
        ulLooper = 0
        outstream.writelines(["%-10s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s\n" % ("index","DsmPdnInst","DsmBearerInst","PsCallId","BearerId","Qfi","BearerType","BearerStatus","CurrCid","GroupInst1","GroupInst2","ModuleId1","ModuleId2","ClientId1","ClientId2","BitCidMask")])
        while ulLooper < MACRO_TAF_DSM_MAX_BEARER_DUMP_NUM:
            analysis_dsm_mntn_per_bearer_info( instream, outstream, ulLooper)
            ulLooper = ulLooper + 1
            
        outstream.writelines(["\nDsmGroupEntityCtxNum:%d\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["\nDsmPdnEntityCtxNum:%d\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["\nDsmBearerEntityCtxNum:%d\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)        = struct.unpack('B', instream.read(1))    
        
def analysis_taf_mntn_log_xsms_dump_info( instream, outstream):
        ulLooper = 0
 
        outstream.writelines(["\nxsmsTimerIndex:%d\n" % struct.unpack('I', instream.read(4))])

        outstream.writelines(["%-10s%-10s\n" % ("index","xsmsTimerTrace")])
        while ulLooper < MACRO_TAF_XSMS_MAX_TIMER_DUMP_NUM:
            (xsmsTimerTrace,)       = struct.unpack('B', instream.read(1))
            strxsmsTimerTrace         = '0x%x' % xsmsTimerTrace
            outstream.writelines(["%-10d%-10s\n" % (ulLooper, strxsmsTimerTrace)])
            ulLooper = ulLooper + 1

        ulLooper = 0        
        outstream.writelines(["%-10s%-20s\n" % ("index","startXsmsTimer")])
        while ulLooper < MACRO_TAF_XSMS_MAX_TIMER_ID_NUM:
            (startXsmsTimer,)       = struct.unpack('I', instream.read(4))
            strstartXsmsTimer         = '0x%x' % startXsmsTimer
            outstream.writelines(["%-10d%-10s\n" % (ulLooper, strstartXsmsTimer)])
            ulLooper = ulLooper + 1

        ulLooper = 0        
        outstream.writelines(["%-10s%-20s\n" % ("index","stopXsmsTimer")])
        while ulLooper < MACRO_TAF_XSMS_MAX_TIMER_ID_NUM:
            (stopXsmsTimer,)       = struct.unpack('I', instream.read(4))
            strstopXsmsTimer         = '0x%x' % stopXsmsTimer
            outstream.writelines(["%-10d%-10s\n" % (ulLooper,strstopXsmsTimer)])
            ulLooper = ulLooper + 1

def analysis_dsm_modem0_dump_info( instream, fileOffset, outstream):
        ulLooper = 0
        ulEndTick = 0
        ulbeginTick = 0

        outstream.writelines(["\nLatestIndex:0x%x\n" % struct.unpack('I', instream.read(4))])
        fileOffset = fileOffset + 4
        
        outstream.writelines(["%-10s%-15s%-15s%-15s%-15s%-55s%-20s%-20s%-20s%-20s\n" % ("index","ulReceiveTime", "ulExitTime", "ulSendPid", "ulReceivePid", "usMsgId", "ucMainFsmId", "ucMainState", "ucSubFsmId", "ucSubState")])
        while ulLooper < MACRO_TAF_DSM_MAX_LOG_EVENT_STATE_NUM:
            fileLocalOffset = fileOffset + ulLooper * MACRO_TAF_DSM_MNTN_LOG_MSG_INFO_SIZE
            analysis_dsm_mntn_per_rec_msg_info( instream, fileLocalOffset, outstream, ulLooper)
            ulLooper = ulLooper + 1
        
        instream.seek(fileOffset + MACRO_TAF_DSM_MAX_LOG_EVENT_STATE_NUM * MACRO_TAF_DSM_MNTN_LOG_MSG_INFO_SIZE)
        
        outstream.writelines(["\nulDsmInfoStart:%d\n" % struct.unpack('I', instream.read(4))])
        
        analysis_taf_mntn_log_dsm_dump_info(instream, outstream)
        
        instream.seek(fileOffset + MACRO_TAF_DSM_MAX_LOG_EVENT_STATE_NUM * MACRO_TAF_DSM_MNTN_LOG_MSG_INFO_SIZE + MACRO_TAF_DSM_MAX_SAVE_DUMP_INFO_SIZE)
        
        outstream.writelines(["\nxsmsInfoStart:%d\n" % struct.unpack('I', instream.read(4))])
        
        analysis_taf_mntn_log_xsms_dump_info(instream, outstream)

        instream.seek(fileOffset + MACRO_TAF_DSM_MAX_LOG_EVENT_STATE_NUM * MACRO_TAF_DSM_MNTN_LOG_MSG_INFO_SIZE + MACRO_TAF_DSM_MAX_SAVE_DUMP_INFO_SIZE)
        
        global modem_index
        if modem_index == 2:
           return

#       2857740885 = 0xaa55aa55 find end tick
        while ulEndTick != 2857740885:
            (ulEndTick,)       = struct.unpack('I', instream.read(4))
        print ("Dsm End tag is %s" % (ulEndTick))


#       2857740885 = 0xaa55aa55 find Begin tick
#        while ulbeginTick != 2857740885:
#                (ulbeginTick,)       = struct.unpack('I', instream.read(4))
#        print ("Dsm begin tag is %s" % (ulbeginTick))

        global GLOBAL_Offset
        GLOBAL_Offset = g_offset + MACRO_NAS_EXC_LOG_LENGTH_MODEM * (modem_index + 1)
        print ("GLOBAL_Offset is %s" % (GLOBAL_Offset))


def analysis_dsm_modemX_event_state_list_dump_info( instream, fileOffset, outstream):   
        
        #outstream.writelines(["\n**************************** analysis_dsm_modemX_event_state_list_dump_info enter! %d*******************************\n" % (fileOffset)])
        instream.seek(fileOffset)
        (ulBeginTick,)       = struct.unpack('I', instream.read(4))
        strBeginTick         = '0x0x%x'% ulBeginTick
        print ("Begin tag is %s" % (strBeginTick))

        outstream.writelines(["strModemLogBeginFlg         %-15s\n" % ( strBeginTick )])
        
        fileOffset = fileOffset + 4
        
        #outstream.writelines(["\n**************************** analysis_dsm_modemX_event_state_list_dump_info enter! %d*******************************\n" % (fileOffset)])
        
        ##### dsm modem0 #########  
        analysis_dsm_modem0_dump_info(instream, fileOffset, outstream)

        return True

def analysis_dsm_dump_info( infile, offset, outfile):
        instream = infile
        outstream  = outfile
        fileOffset = eval(offset)
        
        global g_offset
        g_offset = fileOffset
        
        ##### dsm modem0 PARSE EVENT STATE #########   
        outstream.writelines(["\n**************************** modem0:analysis_dsm_dump_info begin!*******************************\n"])             
        global modem_index
        modem_index = 0
        analysis_dsm_modemX_event_state_list_dump_info( instream, fileOffset, outstream )
        outstream.writelines(["\n**************************** modem0:analysis_dsm_dump_info end!*******************************\n"])       
        

        ##### dsm modem1 PARSE EVENT STATE #########                
        outstream.writelines(["\n**************************** modem1:analysis_dsm_dump_info begin!*******************************\n"])
#        fileOffset = fileOffset + MACRO_MODEM0_ADDR_LENGTH        
#        print ("Old fileOffset is %" % (fileOffset))
        global GLOBAL_Offset
        fileOffset = GLOBAL_Offset
        print ("fileOffset is %s" % (fileOffset))
#       global modem_index
        modem_index = 1
        analysis_dsm_modemX_event_state_list_dump_info( instream, fileOffset, outstream )
        outstream.writelines(["\n**************************** modem1:analysis_dsm_dump_info end!*******************************\n"])    

        ##### dsm modem2 PARSE EVENT STATE #########                
        outstream.writelines(["\n**************************** modem2:analysis_dsm_dump_info begin!*******************************\n"])
#        fileOffset = fileOffset + MACRO_MODEM1_ADDR_LENGTH        
#        global GLOBAL_Offset
        fileOffset = GLOBAL_Offset
#        global modem_index
        modem_index = 2
        analysis_dsm_modemX_event_state_list_dump_info( instream, fileOffset, outstream )
        outstream.writelines(["\n**************************** modem2:analysis_dsm_dump_info end!*******************************\n"]) 
        
        return True

########################################################################################
def entry_0x2200012(infile, field, offset, len, version, mode, outfile):     
        ########check parameter start#############      
        if not field == '0x2200012':
            print ("hidis field is %s" % (field))
            print ("current field is 0x2200012")
            return error['ERR_CHECK_FIELD']
        elif not version == '0x0001':
            print ("hidis version is %s" % (version))
            print ("current version is 0x0001")
            return error['ERR_CHECK_VERSION']
        print ("Offset is %s" % (offset))
        #########check parameter end##############
        ret = analysis_dsm_dump_info( infile, offset, outfile)

        return 0


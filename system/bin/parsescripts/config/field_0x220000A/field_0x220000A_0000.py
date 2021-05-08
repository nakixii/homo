#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   analysis mscc dump bin
modify  record  :   2016-01-27 create file
"""

import struct
import os
import sys
import string
from mscc_pid import *
from fsm_id import *
from mmc_mscc_msg import *
from mma_mscc_msg import *
from xsd_mscc_msg import *
from hsd_mscc_msg import *
from imsa_mscc_msg import *
from timer_mscc_msg import *
from usim_mscc_msg import *
from mscc_mscc_msg import *
from regm_mscc_msg import *

#MACRO_MODEM0_ADDR_LENGTH                = 4096
#MACRO_MODEM1_ADDR_LENGTH                = 4096
MACRO_NAS_MSCC_MAX_LOG_EVENT_STATE_NUM  = 200
MACRO_NAS_MSCC_MNTN_LOG_MSG_INFO_SIZE   = 16

GLOBAL_Offset = 0
modem_index   = 0

def analysis_array_data_one_byte(instream, outstream, ulIndex):
        ulLooper        = 0

        while ulLooper < ulIndex:
            outstream.writelines(["%02X" % struct.unpack('B', instream.read(1))])
            ulLooper = ulLooper + 1
            
        outstream.writelines(["\n"])

def analysis_array_data_four_byte(instream, outstream, ulIndex):
        ulLooper        = 0

        while ulLooper < ulIndex:
            outstream.writelines(["%X " % struct.unpack('I', instream.read(4))])
            ulLooper = ulLooper + 1
        
        outstream.writelines(["\n"])

def get_mscc_msgid_str( pid1, pid2, usMsgId):
        if ( 'mscc' == pid1.lower() and 'mmc' == pid2.lower()):
                return get_mmc_mscc_msg_str(usMsgId)
        elif ( 'i1_mscc' == pid1.lower() and 'i1_mmc' == pid2.lower()):
                return get_mmc_mscc_msg_str(usMsgId)      
        elif ( 'i2_mscc' == pid1.lower() and 'i2_mmc' == pid2.lower()):
                return get_mmc_mscc_msg_str(usMsgId)
        elif ( 'mmc' == pid1.lower() and 'mscc' == pid2.lower()):
                return get_mmc_mscc_msg_str(usMsgId)
        elif ( 'i1_mmc' == pid1.lower() and 'i1_mscc' == pid2.lower()):
              return get_mmc_mscc_msg_str(usMsgId)
        elif ( 'i2_mmc' == pid1.lower() and 'i2_mscc' == pid2.lower()):
              return get_mmc_mscc_msg_str(usMsgId)            
        elif ( 'i2_mscc' == pid1.lower() and 'i2_mmc' == pid2.lower()):
                return get_mmc_mscc_msg_str(usMsgId) 

        elif ( 'mscc' == pid1.lower() and 'mma' == pid2.lower()):
                return get_mma_mscc_msg_str(usMsgId)  
        elif ( 'i1_mscc' == pid1.lower() and 'i1_mma' == pid2.lower()):
                return get_mma_mscc_msg_str(usMsgId)    
        elif ( 'i2_mscc' == pid1.lower() and 'i2_mma' == pid2.lower()):
                return get_mma_mscc_msg_str(usMsgId)  
        elif ( 'mma' == pid1.lower() and 'mscc' == pid2.lower()):
                return get_mma_mscc_msg_str(usMsgId) 
        elif ( 'i1_mma' == pid1.lower() and 'i1_mscc' == pid2.lower()):
                return get_mma_mscc_msg_str(usMsgId)  
        elif ( 'i2_mma' == pid1.lower() and 'i2_mscc' == pid2.lower()):
                return get_mma_mscc_msg_str(usMsgId)

        elif ( 'xsd' == pid1.lower() and 'mscc' == pid2.lower()):
                return get_xsd_mscc_msg_str(usMsgId)
        elif ( 'mscc' == pid1.lower() and 'xsd' == pid2.lower()):
                return get_xsd_mscc_msg_str(usMsgId)
        elif ( 'xsd' == pid1.lower() and 'i1_mscc' == pid2.lower()):
                return get_xsd_mscc_msg_str(usMsgId)
        elif ( 'i1_mscc' == pid1.lower() and 'xsd' == pid2.lower()):
                return get_xsd_mscc_msg_str(usMsgId)    
        elif ( 'xsd' == pid1.lower() and 'i2_mscc' == pid2.lower()):
                return get_xsd_mscc_msg_str(usMsgId)
        elif ( 'i2_mscc' == pid1.lower() and 'xsd' == pid2.lower()):
                return get_xsd_mscc_msg_str(usMsgId)

        elif ( 'hsd' == pid1.lower() and 'mscc' == pid2.lower()):
                return get_hsd_mscc_msg_str(usMsgId)
        elif ( 'mscc' == pid1.lower() and 'hsd' == pid2.lower()):
                return get_hsd_mscc_msg_str(usMsgId)    
        elif ( 'hsd' == pid1.lower() and 'i1_mscc' == pid2.lower()):
                return get_hsd_mscc_msg_str(usMsgId)
        elif ( 'i1_mscc' == pid1.lower() and 'hsd' == pid2.lower()):
                return get_hsd_mscc_msg_str(usMsgId)    
        elif ( 'hsd' == pid1.lower() and 'i2_mscc' == pid2.lower()):
                return get_hsd_mscc_msg_str(usMsgId)
        elif ( 'i2_mscc' == pid1.lower() and 'hsd' == pid2.lower()):
                return get_hsd_mscc_msg_str(usMsgId)

        elif ( 'imsa' == pid1.lower() and 'mscc' == pid2.lower()):
                return get_imsa_mscc_msg_str(usMsgId)
        elif ( 'mscc' == pid1.lower() and 'imsa' == pid2.lower()):
                return get_imsa_mscc_msg_str(usMsgId)   
        elif ( 'i1_imsa' == pid1.lower() and 'i1_mscc' == pid2.lower()):
                return get_imsa_mscc_msg_str(usMsgId)
        elif ( 'i1_mscc' == pid1.lower() and 'i1_imsa' == pid2.lower()):
                return get_imsa_mscc_msg_str(usMsgId)   
        elif ( 'imsa' == pid1.lower() and 'i2_mscc' == pid2.lower()):
                return get_imsa_mscc_msg_str(usMsgId)
        elif ( 'i2_mscc' == pid1.lower() and 'imsa' == pid2.lower()):
                return get_imsa_mscc_msg_str(usMsgId)

        elif ( 'timer' == pid1.lower() and 'mscc' == pid2.lower()):
                return get_timer_mscc_msg_str(usMsgId)
        elif ( 'mscc' == pid1.lower() and 'timer' == pid2.lower()):
                return get_timer_mscc_msg_str(usMsgId)  
        elif ( 'timer' == pid1.lower() and 'i1_mscc' == pid2.lower()):
                return get_timer_mscc_msg_str(usMsgId)
        elif ( 'i1_mscc' == pid1.lower() and 'timer' == pid2.lower()):
                return get_timer_mscc_msg_str(usMsgId)  
        elif ( 'timer' == pid1.lower() and 'i2_mscc' == pid2.lower()):
                return get_timer_mscc_msg_str(usMsgId)
        elif ( 'i2_mscc' == pid1.lower() and 'timer' == pid2.lower()):
                return get_timer_mscc_msg_str(usMsgId)

        elif ( 'usim' == pid1.lower() and 'mscc' == pid2.lower()):
                return get_usim_mscc_msg_str(usMsgId)
        elif ( 'mscc' == pid1.lower() and 'usim' == pid2.lower()):
                return get_usim_mscc_msg_str(usMsgId)   
        elif ( 'usim' == pid1.lower() and 'i1_mscc' == pid2.lower()):
                return get_usim_mscc_msg_str(usMsgId)
        elif ( 'i1_mscc' == pid1.lower() and 'usim' == pid2.lower()):
                return get_usim_mscc_msg_str(usMsgId)   
        elif ( 'usim' == pid1.lower() and 'i2_mscc' == pid2.lower()):
                return get_usim_mscc_msg_str(usMsgId)
        elif ( 'i2_mscc' == pid1.lower() and 'usim' == pid2.lower()):
                return get_usim_mscc_msg_str(usMsgId)
        elif ( 'mscc' == pid1.lower() and 'mscc' == pid2.lower()):
                return get_mscc_mscc_msg_str(usMsgId)
        elif ( 'i1_mscc' == pid1.lower() and 'i1_mscc' == pid2.lower()):
                return get_mscc_mscc_msg_str(usMsgId)
        elif ( 'i2_mscc' == pid1.lower() and 'i2_mscc' == pid2.lower()):
                return get_mscc_mscc_msg_str(usMsgId)
        elif ( 'mscc' == pid1.lower() and 'regm' == pid2.lower()):
                return get_regm_mscc_msg_str(usMsgId)
        elif ( 'i1_mscc' == pid1.lower() and 'i1_regm' == pid2.lower()):
                return get_regm_mscc_msg_str(usMsgId)
        elif ( 'i2_mscc' == pid1.lower() and 'i2_regm' == pid2.lower()):
                return get_regm_mscc_msg_str(usMsgId)
        elif ( 'regm' == pid1.lower() and 'mscc' == pid2.lower()):
                return get_regm_mscc_msg_str(usMsgId)
        elif ( 'i1_regm' == pid1.lower() and 'i1_mscc' == pid2.lower()):
                return get_regm_mscc_msg_str(usMsgId)
        elif ( 'i2_regm' == pid1.lower() and 'i2_mscc' == pid2.lower()):
                return get_regm_mscc_msg_str(usMsgId)
        else:
                return 'none'

def analysis_mscc_mntn_per_rec_msg_info( instream, fileLocalOffset, outstream, ulLooper):
        instream.seek(fileLocalOffset)

        (ulReceiveTime,) = struct.unpack('I', instream.read(4))
        (ulExitTime,)    = struct.unpack('I', instream.read(4))

        (usSendPid,)     = struct.unpack('H', instream.read(2))
        (usRcvPid,)      = struct.unpack('H', instream.read(2))

        (usMsgId,)       = struct.unpack('H', instream.read(2))
        (ucMsccFsmId,)   = struct.unpack('B', instream.read(1))
        (ucMsccState,)   = struct.unpack('B', instream.read(1))
        
        #outstream.writelines(["\n*** (^_^): %-10d%-10d%-10d%-10d%-10d%-10d%-10d*******************************\n" % (ulReceiveTime, ulExitTime, usSendPid, usRcvPid, usMsgId, ucMsccFsmId, ucMsccState)])

        strSendPid       = nas_mscc_get_pid_str(usSendPid)
        strRcvPid        = nas_mscc_get_pid_str(usRcvPid)
        strMsgId         = get_mscc_msgid_str(strSendPid, strRcvPid, usMsgId)      
        strMsccFsmId     = nas_mscc_get_fsmid_str(ucMsccFsmId)
 
        strSendPid       = '%s(0x%x)' % ( strSendPid, usSendPid)
        strRcvPid        = '%s(0x%x)' % ( strRcvPid, usRcvPid)
        strMsgId         = '%s(0x%x)' % ( strMsgId, usMsgId)
        strReceiveTime   = '%x'% ulReceiveTime
        strExitTime      = '%x'% ulExitTime

        strMsccFsmId     = '%s(0x%x)' % ( strMsccFsmId, ucMsccFsmId)       
 
        strMsccState     = '%x' % ucMsccState
  
        #outstream.writelines(["\n**************************** (-.^): *******************************\n"])
        outstream.writelines(["%-10s%-15s%-15s%-15s%-15s%-55s%-20s%-20s\n" % (ulLooper, strReceiveTime.upper(), strExitTime.upper(), strSendPid, strRcvPid, strMsgId, strMsccFsmId, strMsccState)])  

def analysis_gunas_mntn_log_SimStatus_info( instream, outstream):
        outstream.writelines(["UsimStatus:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CsimStatus:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SimCsRegStatus:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SimPsRegStatus:%X\n" % struct.unpack('B', instream.read(1))])

def analysis_gunas_mntn_log_MsCfgInfo_info( instream, outstream):
        outstream.writelines(["CustomCfgInfo_PlatformRatCap_RatNum:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["CustomCfgInfo_PlatformRatCap_RatList:"])
        analysis_array_data_four_byte(instream, outstream, 7)
        
        outstream.writelines(["CustomCfgInfo_ImsCfgInfo_ImsRatSupport_WifiImsSupport:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_ImsCfgInfo_ImsRatSupport_LteImsSupport:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_ImsCfgInfo_ImsRatSupport_UtranImsSupport:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_ImsCfgInfo_ImsRatSupport_GsmImsSupport:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_ImsCfgInfo_ImsRatSupport_WifiEmsSupport:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_ImsCfgInfo_ImsRatSupport_LteEmsSupport:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_ImsCfgInfo_ImsRatSupport_RoamingImsSupport:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_ImsCfgInfo_ImsRatSupport_ImsSupport:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_ImsCfgInfo_VoiceDomain:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CustomCfgInfo_ImsCfgInfo_WaitImsVoiceAvailTimerLen:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CustomCfgInfo_ImsCfgInfo_ClImsSupportFlg:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CustomCfgInfo_ImsCfgInfo_ClVolteMode:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssSysAcqCfg_ReAcqLteOnHrpdSyncIndFlag:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssSysAcqCfg_Is1XLocInfoPrefThanLte:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_AvailableTimerLengthFirstSearch:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_AvailableTimerCountFirstSearch:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_AvailableTimerLengthDeepSearch:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_ScanTimerLen:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_SleepTimerLen:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_CLSysAcqWaitHsdCnfTimerLen:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_CLCLOosTimerMaxExpiredTimes:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_BsrCtrlDoEnterIdleRstLen:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_BsrTimerCtrl_BsrTimerActivateFlag:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_BsrTimerCtrl_BsrPhaseNum:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_BsrTimerCtrl_HrpdConnBsrActiveFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_BsrTimerCtrl_EhrpdConnBsrActiveFlg:%X\n" % struct.unpack('B', instream.read(1))])     
        ulLooper        = 0
        while ulLooper < 2:
            outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_BsrTimerCtrl_BsrTimerInfo%d:\n" % ulLooper])
            outstream.writelines(["MaxHistorySrchTimes:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["MaxPrefBandSrchTimes:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["BsrTimersMaxExpiredTimes:%X\n" % struct.unpack('B', instream.read(1))])
            (ucReserve,)           = struct.unpack('B', instream.read(1))
            outstream.writelines(["ucReserve:%X\n" % ucReserve])
            outstream.writelines(["BsrTimerLenWithNoMatchedMsplRec:%X\n" % struct.unpack('I', instream.read(4))])
            outstream.writelines(["BsrTimerLen:%X\n" % struct.unpack('I', instream.read(4))])
            ulLooper = ulLooper + 1         
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_BsrTimerCtrl_HistoryActiveFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssLastLocInfo_IsLocInfoUsedInSwitchOn:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssLastLocInfo_SysAcqMode:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssLastLocInfo_Cdma1XActiveFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssLastLocInfo_LteActiveFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssLastLocInfo_1xLocationInfo_Mcc:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssLastLocInfo_1xLocationInfo_Mnc:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssLastLocInfo_1xLocationInfo_Sid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssLastLocInfo_1xLocationInfo_Nid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssLastLocInfo_1xLocationInfo_1xPrioClass:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssLastLocInfo_1xLocationInfo_AIPrioClass:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssLastLocInfo_LteLocationInfo_Mcc:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssLastLocInfo_LteLocationInfo_Mnc:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CustomCfgInfo_MmssNvimCfgInfo_MmssLastLocInfo_LteLocationInfo_PrioClass:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["CustomCfgInfo_1xSrcClSysAcqStrategy_ClSysAcqCtrlInfo_1xBsrLteActiveFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_1xSrcClSysAcqStrategy_ClSysAcqCtrlInfo_1xBsrLteTimerFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_1xSrcClSysAcqStrategy_ClSysAcqCtrlInfo_Srlte1xBsrLteEnableFlag:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["CustomCfgInfo_1xSrcClSysAcqStrategy_PhaseOnePatternCfg_TotalTimeLen:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CustomCfgInfo_1xSrcClSysAcqStrategy_PhaseOnePatternCfg_SleepTimeLen:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CustomCfgInfo_1xSrcClSysAcqStrategy_PhaseOnePatternCfg_LteHistorySrchNum:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_1xSrcClSysAcqStrategy_PhaseOnePatternCfg_LteFullBandSrchNum:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_1xSrcClSysAcqStrategy_PhaseOnePatternCfg_LtePrefBandSrchNum:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["CustomCfgInfo_1xSrcClSysAcqStrategy_PhaseTwoPatternCfg_TotalTimeLen:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CustomCfgInfo_1xSrcClSysAcqStrategy_PhaseTwoPatternCfg_SleepTimeLen:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CustomCfgInfo_1xSrcClSysAcqStrategy_PhaseTwoPatternCfg_LteHistorySrchNum:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_1xSrcClSysAcqStrategy_PhaseTwoPatternCfg_LteFullBandSrchNum:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_1xSrcClSysAcqStrategy_PhaseTwoPatternCfg_LtePrefBandSrchNum:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["CustomCfgInfo_ClSysAcqDsdsStrategy_ReAcqLteWithNoRfEnable:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_ClSysAcqDsdsStrategy_ReAcqLteWithNoRfScene:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CustomCfgInfo_ClSysAcqDsdsStrategy_ReAcqLteWithNoRfDelayTime:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["CustomCfgInfo_TestConfig_NoCardModeCfgFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["CustomCfgInfo_ClSysAcqTypeCtrlCfg_HistoryActFlg:"])
        analysis_array_data_one_byte(instream, outstream, 40)
        outstream.writelines(["CustomCfgInfo_ClSysAcqTypeCtrlCfg_PrefBandActFlg:"])
        analysis_array_data_one_byte(instream, outstream, 40)
        
        outstream.writelines(["CustomCfgInfo_CdmaModemInfo_CurrCdmaModemId:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CustomCfgInfo_CdmaModemInfo_LastCdmaModemId:%X\n" % struct.unpack('H', instream.read(2))])
        
        outstream.writelines(["CustomCfgInfo_CdmaClSwitchOnOptCfg_IsCdmaSwitchOnAsyncReadCard:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["CustomCfgInfo_AiModemCfg_ActFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["MsSysCfgInfo_RatPrio_RatNum:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MsSysCfgInfo_RatPrio_RatPrio:"])
        analysis_array_data_one_byte(instream, outstream, 3)
        outstream.writelines(["MsSysCfgInfo_CdmaVolteRecovRatPrio_RatNum:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MsSysCfgInfo_CdmaVolteRecovRatPrio_RatPrio:"])
        analysis_array_data_one_byte(instream, outstream, 3)
        outstream.writelines(["MsSysCfgInfo_RoamCapability:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MsSysCfgInfo_LteCapChangeFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["MsSysCfgInfo_LteCapSta:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["MsSysCfgInfo_DisableReason:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["MsSysCfgInfo_Band_WcdmaBand:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["MsSysCfgInfo_Band_GsmBand:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["MsSysCfgInfo_Band_LteBand:"])
        analysis_array_data_four_byte(instream, outstream, 8)
        outstream.writelines(["MsSysCfgInfo_Band_CdmaBand:%X\n" % struct.unpack('I', instream.read(4))])

def analysis_gunas_mntn_log_NwInfo_info( instream, outstream):
        outstream.writelines(["LteNwCapInfo_NwImsVoCap:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["LteNwCapInfo_NwBsCap:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["LteNwCapInfo_LteCsCap:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["GuNwCapInfo_NwImsVoCap:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["GuNwCapInfo_NwBsCap:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["GuNwCapInfo_LteCsCap:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["SysInfo_3GppSysInfo_CampOnFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3GppSysInfo_SysMode:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3GppSysInfo_LmmAccessType:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3GppSysInfo_PrioClass:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3GppSysInfo_CellId:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SysInfo_3GppSysInfo_PlmnId_Mcc:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SysInfo_3GppSysInfo_PlmnId_Mnc:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SysInfo_3GppSysInfo_Lac:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SysInfo_3GppSysInfo_Rac:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3GppSysInfo_RoamFlag:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3GppSysInfo_InterRoamFlag:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_CampOnFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_BandClass:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_Freq:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_Sid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_Nid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_ServiceStatus:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RoamingInd:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_PrevInUse:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_Pzid:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_1xPriClass:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_AIPriClass:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfoIncl:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_BaseStationInfoIncl:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_ServiceInfoIncl:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_RegZone:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_RegZoneNum:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_ZoneTimer:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_MultiSidFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_MultiNidFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_RegDistance:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_RegPeriod:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_HomeReg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_SidRoamReg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_NidRoamReg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_PowerUpReg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_PowerDownReg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_ParameterReg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_BaseStationInfo_BaseId:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_BaseStationInfo_BaseClass:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_BaseStationInfo_BaseLatitude:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_BaseStationInfo_BaseLongiitude:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_ServiceInfo_MaxAltSo:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_ServiceInfo_SDBSupported:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_ServiceInfo_MoQos:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_ServiceInfo_ConcurrentSupported:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_ServiceInfo_MoPosSupported:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_ServiceInfo_ImsiI1_I2:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_ServiceInfo_Mcc:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_ServiceInfo_Mnc:%X\n" % struct.unpack('H', instream.read(2))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_1xOosCause:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_QpchSupportFlag:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["SysInfo_3Gpp2SysInfo_HrpdSysInfo_CampOnFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_HrpdSysInfo_HrpdPrioClass:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_HrpdSysInfo_AIPrioClass:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_HrpdSysInfo_SubNetMask:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_HrpdSysInfo_Mcc:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_HrpdSysInfo_SectorId:"])
        analysis_array_data_one_byte(instream, outstream, 16)
        
        outstream.writelines(["ServiceStatusInfo_1xServiceStatus:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ServiceStatusInfo_HrpdServiceStatus:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ServiceStatusInfo_3gppPsServiceStatus:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ServiceStatusInfo_3gppCsServiceStatus:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ServiceStatusInfo_EccSrvFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ServiceStatusInfo_IsInCsSrvConn:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["ConnStatusInfo_HrpdConnExistFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ConnStatusInfo_LteEpsConnExistFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["ImsDomainInfo_ImsVoiceCap:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsDomainInfo_RcvServiceChangeIndFlag:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsDomainInfo_ImsEmcBearerState:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsDomainInfo_ImsNormalMediaBearerState:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsDomainInfo_ImsCallxistFlag:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["SendToImsaInfo_RoamFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["SendToImsaInfo_PsRegCnRslt:%X\n" % struct.unpack('I', instream.read(4))])
        
        outstream.writelines(["LastSysInfo_LastCampOnLTEOrDoRat:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])

def analysis_gunas_mntn_log_PowerSaveCtrl_info( instream, outstream):
        outstream.writelines(["1xActiveFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["HrpdActiveFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["3gppActiveFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PowerSaveReplyFlg:%X\n" % struct.unpack('B', instream.read(1))])

def analysis_gunas_mntn_log_SysAcqCtrl_info( instream, outstream):
        outstream.writelines(["NoCardInitSearchLoc_InitSearchGulLoc_Plmn_Mcc:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["NoCardInitSearchLoc_InitSearchGulLoc_Plmn_Mnc:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["NoCardInitSearchLoc_InitSearchGulLoc_Lac:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["NoCardInitSearchLoc_InitSearchGulLoc_Rat:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["NoCardInitSearchLoc_InitSearchCdmaLoc_Sid:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["NoCardInitSearchLoc_InitSearchCdmaLoc_Nid:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["NoCardInitSearchLoc_InitSearchCdmaLoc_Mcc:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["NoCardInitSearchLoc_InitSearchWaitType:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["NoCardInitSearchLoc_IsLocInfoUsed:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["AllowSrchLteFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["LteSysPriClass:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["Cur1XServiceSysAcqPhaseNum:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MoCallConnecting:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CallBackEnableFlg:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["IsEmcCallExist:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["VolteEmcSrvAcqExistFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ClOosTimerExpiredCount:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SrvAcqFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["IsAllowEmcCallInforeign:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["EmcCallBackDelayFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["LteOos1xActDelayTimer:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["EpsAttachAllow:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["PrioSrchLastRatFlag:%X\n" % struct.unpack('I', instream.read(4))])
        
        outstream.writelines(["EplmnListInClMode_EquPlmnNum:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        ulLooper        = 0
        while ulLooper < 16:
            outstream.writelines(["EplmnListInClMode_EquPlmnAddr%d:" % ulLooper])
            outstream.writelines(["Mcc :%X " % struct.unpack('I', instream.read(4))])
            outstream.writelines(["Mnc :%X\n" % struct.unpack('I', instream.read(4))])
            ulLooper = ulLooper + 1
            
        outstream.writelines(["ClEnhanceVoltePingPongStrategy_DisableLteTimerLen:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["ClEnhanceVoltePingPongStrategy_SwitchCtrlTimerLen:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["ClEnhanceVoltePingPongStrategy_MaxPingPongNum:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["ClNormalVoltePingPongInfo_CurrSwitchNum:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["ClNormalVoltePingPongInfo_SwitchBeginSlice:"])
        analysis_array_data_four_byte(instream, outstream, 10)
        outstream.writelines(["ClNormalVoltePingPongInfo_LteStatus:%X\n" % struct.unpack('I', instream.read(4))])
            
def analysis_mscc_modem0_dump_info( instream, fileOffset, outstream, ulMsgIndex):
        ulLooper = 0
        instreamtemp = instream
        ulEndTick = 0
        ulbeginTick = 0

        outstream.writelines(["%-10s%-15s%-15s%-15s%-15s%-55s%-20s%-20s\n" % ("index","ulReceiveTime", "ulExitTime", "usSendPid", "usReceivePid", "usMsgId", "ucMsccFsmId", "ucMsccState")])
        while ulLooper < MACRO_NAS_MSCC_MAX_LOG_EVENT_STATE_NUM:
                ulLooperIndex = ( ulLooper + ulMsgIndex) % MACRO_NAS_MSCC_MAX_LOG_EVENT_STATE_NUM
                fileLocalOffset = fileOffset + ulLooperIndex * MACRO_NAS_MSCC_MNTN_LOG_MSG_INFO_SIZE
                analysis_mscc_mntn_per_rec_msg_info( instream, fileLocalOffset, outstream, (ulLooper))
                ulLooper = ulLooper + 1
                
        outstream.writelines(["\nLatestIndex:%d\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["\n%-15s\n" % ("SimStatus:")])
        analysis_gunas_mntn_log_SimStatus_info( instream, outstream)
        
        outstream.writelines(["\nIsCardChanged:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["\n%-15s\n" % ("MsCfgInfo:")])
        analysis_gunas_mntn_log_MsCfgInfo_info( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("NwInfo:")])
        analysis_gunas_mntn_log_NwInfo_info( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("PowerSaveCtrl:")])
        analysis_gunas_mntn_log_PowerSaveCtrl_info( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("SysAcqCtrl:")])
        analysis_gunas_mntn_log_SysAcqCtrl_info( instream, outstream)

        instream.seek(fileOffset + MACRO_NAS_MSCC_MAX_LOG_EVENT_STATE_NUM * MACRO_NAS_MSCC_MNTN_LOG_MSG_INFO_SIZE)
        
        global modem_index
        if modem_index == 2:
                return

#       2857740885 = 0xaa55aa55 find end tick
        while ulEndTick != 2857740885:
                (ulEndTick,)       = struct.unpack('I', instream.read(4))
        print ("Mscc End tag is %s" % (ulEndTick))



#       2857740885 = 0xaa55aa55 find Begin tick
        while ulbeginTick != 2857740885:
                (ulbeginTick,)       = struct.unpack('I', instream.read(4))
        print ("Mscc begin tag is %s" % (ulbeginTick))

        global GLOBAL_Offset
        GLOBAL_Offset = instream.tell()
        print ("GLOBAL_Offset is %s" % (GLOBAL_Offset))


def analysis_mscc_modemX_event_state_list_dump_info( instream, fileOffset, outstream):   
        ulLooperTest = 0
        
        #outstream.writelines(["\n**************************** analysis_mscc_modemX_event_state_list_dump_info enter! %d*******************************\n" % (fileOffset)])
        instream.seek(fileOffset)
        (ulBeginTick,)       = struct.unpack('I', instream.read(4))
        strBeginTick         = '0x%x'% ulBeginTick
        print ("Begin tag is %s" % (strBeginTick))

        #outstream.writelines(["strModem0LogBeginFlg         %-15s\n" % ( strBeginTick )])
        
        fileOffset = fileOffset + 4
        
        #outstream.writelines(["\n**************************** analysis_mscc_modemX_event_state_list_dump_info enter! %d*******************************\n" % (fileOffset)])
        
        ##### mscc modem0 #########  
        analysis_mscc_modem0_dump_info(instream, fileOffset, outstream, ulLooperTest)

        return True

def analysis_mscc_dump_info( infile, offset, outfile):
        instream = infile
        outstream  = outfile
        fileOffset = eval(offset)
           
        ##### mscc modem0 PARSE EVENT STATE #########   
        outstream.writelines(["\n**************************** modem0:analysis_mscc_dump_info begin!*******************************\n"])             
        global modem_index
        modem_index = 0
        analysis_mscc_modemX_event_state_list_dump_info( instream, fileOffset, outstream )
        outstream.writelines(["\n**************************** modem0:analysis_mscc_dump_info end!*******************************\n"])       
        

        ##### mscc modem1 PARSE EVENT STATE #########                
        outstream.writelines(["\n**************************** modem1:analysis_mscc_dump_info begin!*******************************\n"])
#        fileOffset = fileOffset + MACRO_MODEM0_ADDR_LENGTH        
#        print ("Old fileOffset is %" % (fileOffset))
        global GLOBAL_Offset
        fileOffset = GLOBAL_Offset - 4
        print ("fileOffset is %s" % (fileOffset))
#       global modem_index
        modem_index = 1
        analysis_mscc_modemX_event_state_list_dump_info( instream, fileOffset, outstream )
        outstream.writelines(["\n**************************** modem1:analysis_mscc_dump_info end!*******************************\n"])    

        ##### mscc modem2 PARSE EVENT STATE #########                
        outstream.writelines(["\n**************************** modem2:analysis_mscc_dump_info begin!*******************************\n"])
#        fileOffset = fileOffset + MACRO_MODEM1_ADDR_LENGTH        
#        global GLOBAL_Offset
        fileOffset = GLOBAL_Offset - 4
#        global modem_index
        modem_index = 2
        analysis_mscc_modemX_event_state_list_dump_info( instream, fileOffset, outstream )
        outstream.writelines(["\n**************************** modem2:analysis_mscc_dump_info end!*******************************\n"]) 
        
        return True

########################################################################################
def entry_0x220000A(infile, field, offset, len, version, mode, outfile):     
        ########check parameter start#############      
        if not field == '0x220000A':
            print ("hidis field is %s" % (field))
            print ("current field is 0x220000A")
            return error['ERR_CHECK_FIELD']
        elif not version == '0x0000':
            print ("hidis version is %s" % (version))
            print ("current version is 0x0000")
            return error['ERR_CHECK_VERSION']
        print ("Offset is %s" % (offset))
        #########check parameter end##############
        ret = analysis_mscc_dump_info( infile, offset, outfile)

        return 0


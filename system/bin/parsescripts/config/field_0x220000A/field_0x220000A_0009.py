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
MACRO_NAS_EXC_LOG_LENGTH_MODEM          = 4096

GLOBAL_Offset = 0
modem_index   = 0
g_offset = 0

def analysis_array_data_one_byte(instream, outstream, ulIndex):
        ulLooper        = 0

        while ulLooper < ulIndex:
            outstream.writelines(["%02X" % struct.unpack('B', instream.read(1))])
            ulLooper = ulLooper + 1
        outstream.writelines(["\n"])

def analysis_array_data_four_byte(instream, outstream, ulIndex):
        ulLooper        = 0

        while ulLooper < ulIndex:
            outstream.writelines(["0x%X " % struct.unpack('I', instream.read(4))])
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
        strReceiveTime   = '0x%x'% ulReceiveTime
        strExitTime      = '0x%x'% ulExitTime

        strMsccFsmId     = '%s(0x%x)' % ( strMsccFsmId, ucMsccFsmId)

        strMsccState     = '0x%x' % ucMsccState

        #outstream.writelines(["\n**************************** (-.^): *******************************\n"])
        outstream.writelines(["%-10s%-15s%-15s%-15s%-15s%-55s%-20s%-20s\n" % (ulLooper, strReceiveTime.upper(), strExitTime.upper(), strSendPid, strRcvPid, strMsgId, strMsccFsmId, strMsccState)])

def analysis_gunas_mntn_log_SimStatus_info( instream, outstream):
        outstream.writelines(["UsimStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CsimStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SimCsRegStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SimPsRegStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["\nIsCardChanged:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])

def analysis_gunas_mntn_log_CustomCfgInfo_info( instream, outstream):
        outstream.writelines(["MmssNvimCfgInfo_MmssSysAcqCfg_ReAcqLteOnHrpdSyncIndFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MmssNvimCfgInfo_MmssSysAcqCfg_Is1XLocInfoPrefThanLte:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_ScanTimerLen:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_SleepTimerLen:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_CLSysAcqWaitHsdCnfTimerLen:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_CLCLOosTimerMaxExpiredTimes:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_AvailableTimerLengthFirstSearch:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_AvailableTimerCountFirstSearch:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_AvailableTimerLengthDeepSearch:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_BsrCtrlDoEnterIdleRstLen:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_BsrTimerCtrl_BsrTimerActivateFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_BsrTimerCtrl_BsrPhaseNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_BsrTimerCtrl_HrpdConnBsrActiveFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_BsrTimerCtrl_EhrpdConnBsrActiveFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        ulLooper        = 0
        while ulLooper < 2:
            outstream.writelines(["MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_BsrTimerCtrl_BsrTimerInfo%d:\n" % ulLooper])
            outstream.writelines(["MaxHistorySrchTimes:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["MaxPrefBandSrchTimes:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["BsrTimersMaxExpiredTimes:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["BsrTimerLenWithNoMatchedMsplRec:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["BsrTimerLen:0x%X\n" % struct.unpack('B', instream.read(1))])
            (ucReserve,)           = struct.unpack('B', instream.read(1))
            outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
            (ucReserve,)           = struct.unpack('B', instream.read(1))
            outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
            (ucReserve,)           = struct.unpack('B', instream.read(1))
            outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
            ulLooper = ulLooper + 1
        outstream.writelines(["MmssNvimCfgInfo_MmssSysAcqCfg_SysAcqTimerCfg_BsrTimerCtrl_HistoryActiveFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])

        outstream.writelines(["MmssNvimCfgInfo_MmssLastLocInfo_IsLocInfoUsedInSwitchOn:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MmssNvimCfgInfo_MmssLastLocInfo_SysAcqMode:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MmssNvimCfgInfo_MmssLastLocInfo_Cdma1XActiveFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MmssNvimCfgInfo_MmssLastLocInfo_Sys3gppActiveFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MmssNvimCfgInfo_MmssLastLocInfo_Sys1xLocationInfo_Mcc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["MmssNvimCfgInfo_MmssLastLocInfo_Sys1xLocationInfo_Mnc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["MmssNvimCfgInfo_MmssLastLocInfo_Sys1xLocationInfo_Sid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["MmssNvimCfgInfo_MmssLastLocInfo_Sys1xLocationInfo_Nid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["MmssNvimCfgInfo_MmssLastLocInfo_Sys1xLocationInfo_Sys1xPrioClass:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MmssNvimCfgInfo_MmssLastLocInfo_Sys1xLocationInfo_AIPrioClass:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["MmssNvimCfgInfo_MmssLastLocInfo_Sys3gppLocationInfo_Mcc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["MmssNvimCfgInfo_MmssLastLocInfo_Sys3gppLocationInfo_Mnc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["MmssNvimCfgInfo_MmssLastLocInfo_Sys3gppLocationInfo_PrioClass:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])

        outstream.writelines(["ClSysAcqTypeCtrlCfg_HistoryActFlg:0x"])
        analysis_array_data_one_byte(instream, outstream, 40)
        outstream.writelines(["ClSysAcqTypeCtrlCfg_PrefBandActFlg:0x"])
        analysis_array_data_one_byte(instream, outstream, 40)

        outstream.writelines(["ImsCfgInfo_WaitImsVoiceAvailTimerLen:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsCfgInfo_ClImsSupportFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsCfgInfo_VoiceDomain:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsCfgInfo_ClVolteMode:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsCfgInfo_ImsRatSupport_WifiImsSupport:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsCfgInfo_ImsRatSupport_LteImsSupport:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsCfgInfo_ImsRatSupport_UtranImsSupport:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsCfgInfo_ImsRatSupport_GsmImsSupport:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsCfgInfo_ImsRatSupport_WifiEmsSupport:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsCfgInfo_ImsRatSupport_LteEmsSupport:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsCfgInfo_ImsRatSupport_RoamingImsSupport:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsCfgInfo_ImsRatSupport_ImsSupport:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsCfgInfo_ImsRatSupport_NrImsSupport:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsCfgInfo_ImsRatSupport_NrEmsSupport:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsCfgInfo_ImsRatSupport_NrEmfbSupport:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["ImsCfgInfo_ImsRatSupport_SerialRegIn1xAndNrFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsCfgInfo_ImsRatSupport_Sys1xCoexistWithNrFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsCfgInfo_ImsRatSupport_NrWaitImsVoiceAvailTimerLen:%X\n" % struct.unpack('H', instream.read(2))])

        outstream.writelines(["PlatformRatCap_RatNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PlatformRatCap_RatList:"])
        analysis_array_data_one_byte(instream, outstream, 7)

        outstream.writelines(["ClSysAcqDsdsStrategy_ReAcqLteWithNoRfEnable:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ClSysAcqDsdsStrategy_ReAcqLteWithNoRfScene:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ClSysAcqDsdsStrategy_ReAcqLteWithNoRfDelayTime:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])

        outstream.writelines(["Sys1xSrcClSysAcqStrategy_ClSysAcqCtrlInfo_Sys1xBsrLteActiveFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["Sys1xSrcClSysAcqStrategy_ClSysAcqCtrlInfo_Sys1xBsrLteTimerLen:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["Sys1xSrcClSysAcqStrategy_ClSysAcqCtrlInfo_Srlte1xBsrLteEnableFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["Sys1xSrcClSysAcqStrategy_PhaseOnePatternCfg_TotalTimeLen:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["Sys1xSrcClSysAcqStrategy_PhaseOnePatternCfg_SleepTimeLen:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["Sys1xSrcClSysAcqStrategy_PhaseOnePatternCfg_LteHistorySrchNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["Sys1xSrcClSysAcqStrategy_PhaseOnePatternCfg_LteFullBandSrchNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["Sys1xSrcClSysAcqStrategy_PhaseOnePatternCfg_LtePrefBandSrchNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["Sys1xSrcClSysAcqStrategy_PhaseTwoPatternCfg_TotalTimeLen:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["Sys1xSrcClSysAcqStrategy_PhaseTwoPatternCfg_SleepTimeLen:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["Sys1xSrcClSysAcqStrategy_PhaseTwoPatternCfg_LteHistorySrchNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["Sys1xSrcClSysAcqStrategy_PhaseTwoPatternCfg_LteFullBandSrchNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["Sys1xSrcClSysAcqStrategy_PhaseTwoPatternCfg_LtePrefBandSrchNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])

        outstream.writelines(["CdmaModemInfo_CurrCdmaModemId:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CdmaModemInfo_LastCdmaModemId:0x%X\n" % struct.unpack('H', instream.read(2))])

        outstream.writelines(["AiModemActFlgCfg:0x%X\n" % struct.unpack('B', instream.read(1))])

        outstream.writelines(["TestNoCardModeFlgCfg:0x%X\n" % struct.unpack('B', instream.read(1))])

        outstream.writelines(["MultiModeEmcSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])

        outstream.writelines(["IsCdmaSwitchOnAsyncReadCard:0x%X\n" % struct.unpack('B', instream.read(1))])

def analysis_gunas_mntn_log_MsSysCfgInfo_info( instream, outstream):
        outstream.writelines(["RatPrio_RatNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["RatPrio_RatPrio:0x"])
        analysis_array_data_one_byte(instream, outstream, 7)
        outstream.writelines(["CdmaVolteRecovRatPrio_RatNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CdmaVolteRecovRatPrio_RatPrio:0x"])
        analysis_array_data_one_byte(instream, outstream, 7)
        outstream.writelines(["RoamCapability:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["LteCapChangeFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NrRatChangeFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["LteCapSta:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["DisableLReason:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NrCapSta:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["DisableNrReason:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["Band_WcdmaBand:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["Band_GsmBand:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["Band_LteBand:"])
        analysis_array_data_four_byte(instream, outstream, 8)
        outstream.writelines(["Band_CdmaBand:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["Band_NrBand:"])
        analysis_array_data_four_byte(instream, outstream, 32)
        outstream.writelines(["NrOptionCfg_NrSaSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NrOptionCfg_NrDcMode:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NrOptionCfg_Nr5gcAccessMode:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NrOptionCfg_Nr5gcNon3gppAccessMode:0x%X\n" % struct.unpack('B', instream.read(1))])

def analysis_gunas_mntn_log_NwInfo_info( instream, outstream):
        outstream.writelines(["NrLteN26Ind:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["LastSysInfoCampOnRat:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])

        outstream.writelines(["ConnStatusInfo_HrpdConnExistFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ConnStatusInfo_LteEpsConnExistFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])

        outstream.writelines(["GuCapInfo_NwImsVoCap:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["GuCapInfo_NwEmcBsCap:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])

        outstream.writelines(["LteCapInfo_NwImsVoCap:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["LteCapInfo_NwEmcBsCap:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["LteCapInfo_LteCsCap:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])

        outstream.writelines(["SysInfo_3GppSysInfo_Lac:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SysInfo_3GppSysInfo_Rac:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3GppSysInfo_RoamFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3GppSysInfo_InterRoamFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3GppSysInfo_imsEmcNotSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3GppSysInfo_supportImsECallFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3GppSysInfo_CampOnFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3GppSysInfo_SysMode:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3GppSysInfo_NrLteAccessType:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3GppSysInfo_PrioClass:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["SysInfo_3GppSysInfo_CellId_CellIdLowBit:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SysInfo_3GppSysInfo_CellId_CellIdHighBit:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SysInfo_3GppSysInfo_PlmnId_Mcc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SysInfo_3GppSysInfo_PlmnId_Mnc:0x%X\n" % struct.unpack('I', instream.read(4))])

        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_CampOnFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_BandClass:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_Freq:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_Sid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_Nid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RoamingInd:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_PrevInUse:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_Pzid:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfoIncl:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_BaseStationInfoIncl:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_ServiceInfoIncl:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_QpchSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_Pif1xPriClass:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_PifAIPriClass:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_1xOosCause:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_ServiceStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_RegZone:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_RegZoneNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_ZoneTimer:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_MultiSidFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_MultiNidFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_RegDistance:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_RegPeriod:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_HomeReg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_SidRoamReg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_NidRoamReg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_PowerUpReg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_PowerDownReg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_RegInfo_ParameterReg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_BaseStationInfo_BaseId:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_BaseStationInfo_BaseClass:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_BaseStationInfo_BaseLatitude:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_BaseStationInfo_BaseLongiitude:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_ServiceInfo_MaxAltSo:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_ServiceInfo_SDBSupported:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_ServiceInfo_MoQos:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_ServiceInfo_ConcurrentSupported:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_ServiceInfo_MoPosSupported:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_ServiceInfo_UsImsiI1_I2:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_ServiceInfo_Mcc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_1xSysInfo_1xSysSrvInfo_ServiceInfo_Mnc:0x%X\n" % struct.unpack('I', instream.read(4))])

        outstream.writelines(["SysInfo_3Gpp2SysInfo_HrpdSysInfo_CampOnFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_HrpdSysInfo_HrpdPrioClass:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_HrpdSysInfo_AIPrioClass:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_HrpdSysInfo_SubNetMask:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_HrpdSysInfo_Mcc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SysInfo_3Gpp2SysInfo_HrpdSysInfo_SectorId:0x"])
        analysis_array_data_one_byte(instream, outstream, 16)

        outstream.writelines(["ImsDomainInfo_ImsVoiceCap:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsDomainInfo_RcvServiceChangeIndFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsDomainInfo_ImsEmcBearerState:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsDomainInfo_ImsNormalMediaBearerState:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsDomainInfo_ImsCallxistFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsDomainInfo_ImsSignalQuality:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])

        outstream.writelines(["NrCapInfo_SmsOverNasAllowed:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NrCapInfo_EmsInd:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NrCapInfo_EmsFallBackInd:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NrCapInfo_VoPsInd:0x%X\n" % struct.unpack('B', instream.read(1))])

        outstream.writelines(["ServiceStatusInfo_1xServiceStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ServiceStatusInfo_HrpdServiceStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ServiceStatusInfo_3gppPsServiceStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ServiceStatusInfo_3gppCsServiceStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ServiceStatusInfo_EccSrvFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ServiceStatusInfo_IsInCsSrvConn:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])

        outstream.writelines(["SendToImsaInfo_RoamFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["SendToImsaInfo_PsRegCnRslt:0x%X\n" % struct.unpack('I', instream.read(4))])

def analysis_gunas_mntn_log_PowerSaveCtrl_info( instream, outstream):
        outstream.writelines(["1xActiveFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["HrpdActiveFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["3gppActiveFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PowerSaveReplyFlg:0x%X\n" % struct.unpack('B', instream.read(1))])

def analysis_gunas_mntn_log_SysAcqCtrl_info( instream, outstream):
        outstream.writelines(["AllowSrch3gppFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MoCallConnecting:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["IsEmcCallExist:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["VolteEmcSrvAcqExistFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ClOosTimerExpiredCount:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SrvAcqFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["IsAllowEmcCallInforeign:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["EmcCallBackDelayFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SuspendNrWhenPowerSave1x:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsAttachAllow:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PrioSrchLastRatFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["3gppSysPriClass:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["Cur1XServiceSysAcqPhaseNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["EmcSrvTypeForMmc:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["unavail3gppReason :0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CallBackEnableFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["DelayAct1xTimeInfo_delayAct1xTimeWithNrNotSpt:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["DelayAct1xTimeInfo_delayAct1xTimeWithNrSpt:0x%X\n" % struct.unpack('I', instream.read(4))])

        outstream.writelines(["EplmnListInClMode_EquPlmnNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        ulLooper        = 0
        while ulLooper < 16:
            outstream.writelines(["EplmnListInClMode_EquPlmnAddr%d:" % ulLooper])
            outstream.writelines(["Mcc :0x%X " % struct.unpack('I', instream.read(4))])
            outstream.writelines(["Mnc :0x%X\n" % struct.unpack('I', instream.read(4))])
            ulLooper = ulLooper + 1

        outstream.writelines(["MsccEndTag :0x%X\n" % struct.unpack('I', instream.read(4))])
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
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])

        outstream.writelines(["\n%-15s\n" % ("SimStatus:")])
        analysis_gunas_mntn_log_SimStatus_info( instream, outstream)

        outstream.writelines(["\n%-15s\n" % ("CustomCfgInfo:")])
        analysis_gunas_mntn_log_CustomCfgInfo_info( instream, outstream)

        outstream.writelines(["\n%-15s\n" % ("MsCfgInfo:")])
        analysis_gunas_mntn_log_MsSysCfgInfo_info( instream, outstream)

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
#        while ulbeginTick != 2857740885:
#                (ulbeginTick,)       = struct.unpack('I', instream.read(4))
#        print ("Mscc begin tag is %s" % (ulbeginTick))

        global GLOBAL_Offset
        GLOBAL_Offset = g_offset + MACRO_NAS_EXC_LOG_LENGTH_MODEM * (modem_index + 1)
#        GLOBAL_Offset = instream.tell()
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

        global g_offset
        g_offset = eval(offset)

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
        fileOffset = GLOBAL_Offset
        print ("fileOffset is %s" % (fileOffset))
#       global modem_index
        modem_index = 1
        analysis_mscc_modemX_event_state_list_dump_info( instream, fileOffset, outstream )
        outstream.writelines(["\n**************************** modem1:analysis_mscc_dump_info end!*******************************\n"])

        ##### mscc modem2 PARSE EVENT STATE #########
        outstream.writelines(["\n**************************** modem2:analysis_mscc_dump_info begin!*******************************\n"])
#        fileOffset = fileOffset + MACRO_MODEM1_ADDR_LENGTH
#        global GLOBAL_Offset
        fileOffset = GLOBAL_Offset
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
        elif not version == '0x0009':
            print ("hidis version is %s" % (version))
            print ("current version is 0x0009")
            return error['ERR_CHECK_VERSION']
        print ("Offset is %s" % (offset))
        #########check parameter end##############
        ret = analysis_mscc_dump_info( infile, offset, outfile)

        return 0


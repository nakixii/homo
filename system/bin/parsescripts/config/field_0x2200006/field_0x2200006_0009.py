#!/usr/bin/env python3
"""
Copyright 漏 Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   analysis guas dump bin
modify  record  :   2016-01-22 create file
"""

import struct
import os
import sys
import string
from nas_pid import *
from mmc_mscc_msg import *
from nas_lmm_msg import *
from gas_nas_msg import *
from gas_mta_msg import *
from gas_mtc_msg import *
from gas_taf_msg import *
from mmc_rrm_msg import *
from mmc_css_msg import *
from mmc_regm_msg import *
from gmm_sm_msg import *
from regm_mscc_msg import *
from mmc_usim_msg import *
from mm_usim_msg import *
from gmm_usim_msg import *
from gmm_ll_msg import *
from mmc_nrmm_msg import *
from regm_nrmm_msg import *

MACRO_MODEM0_ADDR_LENGTH                = 3072
MACRO_MODEM1_ADDR_LENGTH                = 3072
MACRO_NAS_MML_MAX_LOG_EVENT_STATE_NUM   = 100
MACRO_NAS_MNTN_LOG_MSG_INFO_SIZE        = 16
MACRO_NAS_MNTN_LOG_MSG_INFO_SIZE_HIONE  = 20
MACRO_NAS_EXC_LOG_LENGTH_MODEM          = 4096

GLOBAL_Offset = 0
modem_index   = 0
Global_Version = 0
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
        
def get_nas_as_msg_str( pid1, pid2, usMsgName):
        if ( 'mscc' == pid1.lower() and 'mmc' == pid2.lower()):
                return get_mmc_mscc_msg_str(usMsgName)
        elif ( 'i1_mscc' == pid1.lower() and 'i1_mmc' == pid2.lower()):
                return get_mmc_mscc_msg_str(usMsgName)
        elif ( 'i2_mscc' == pid1.lower() and 'i2_mmc' == pid2.lower()):
                return get_mmc_mscc_msg_str(usMsgName)
        elif ( 'mmc' == pid1.lower() and 'rrm' == pid2.lower()):
                return get_mmc_rrm_msg_str(usMsgName) 
        elif ( 'rrm' == pid1.lower() and 'mmc' == pid2.lower()):
                return get_mmc_rrm_msg_str(usMsgName)
        elif ( 'mmc' == pid1.lower() and 'regm' == pid2.lower()):
                return get_mmc_regm_msg_str(usMsgName)
        elif ( 'sm' == pid1.lower() and 'gmm' == pid2.lower()):
                return get_gmm_sm_msg_str(usMsgName)
        elif ( 'i1_sm' == pid1.lower() and 'i1_gmm' == pid2.lower()):
                return get_gmm_sm_msg_str(usMsgName)
        elif ( 'i2_sm' == pid1.lower() and 'i2_gmm' == pid2.lower()):
                return get_gmm_sm_msg_str(usMsgName)              
        elif ( 'regm' == pid1.lower() and 'mmc' == pid2.lower()):
                return get_mmc_regm_msg_str(usMsgName)
        elif ( 'i1_mmc' == pid1.lower() and 'i1_regm' == pid2.lower()):
                return get_mmc_regm_msg_str(usMsgName) 
        elif ( 'i1_regm' == pid1.lower() and 'i1_mmc' == pid2.lower()):
                return get_mmc_regm_msg_str(usMsgName)
        elif ( 'i2_mmc' == pid1.lower() and 'i2_regm' == pid2.lower()):
                return get_mmc_regm_msg_str(usMsgName) 
        elif ( 'i2_regm' == pid1.lower() and 'i2_mmc' == pid2.lower()):
                return get_mmc_regm_msg_str(usMsgName)
        elif ( 'mscc' == pid1.lower() and 'regm' == pid2.lower()):
                return get_regm_mscc_msg_str(usMsgName)
        elif ( 'i1_mscc' == pid1.lower() and 'i1_regm' == pid2.lower()):
                return get_regm_mscc_msg_str(usMsgName)
        elif ( 'i2_mscc' == pid1.lower() and 'i2_regm' == pid2.lower()):
                return get_regm_mscc_msg_str(usMsgName)
        elif ( 'regm' == pid1.lower() and 'mscc' == pid2.lower()):
                return get_regm_mscc_msg_str(usMsgName)
        elif ( 'i1_regm' == pid1.lower() and 'i1_mscc' == pid2.lower()):
                return get_regm_mscc_msg_str(usMsgName)
        elif ( 'i2_regm' == pid1.lower() and 'i2_mscc' == pid2.lower()):
                return get_regm_mscc_msg_str(usMsgName) 
        elif ( 'usim' == pid1.lower() and 'gmm' == pid2.lower()):
                return get_gmm_usim_msg_str(usMsgName)
        elif ( 'i1_usim' == pid1.lower() and 'i1_gmm' == pid2.lower()):
                return get_gmm_usim_msg_str(usMsgName)
        elif ( 'i2_usim' == pid1.lower() and 'i2_gmm' == pid2.lower()):
                return get_gmm_usim_msg_str(usMsgName)
        elif ( 'usim' == pid1.lower() and 'mmc' == pid2.lower()):
                return get_mmc_usim_msg_str(usMsgName)
        elif ( 'i1_usim' == pid1.lower() and 'i1_mmc' == pid2.lower()):
                return get_mmc_usim_msg_str(usMsgName)
        elif ( 'i2_usim' == pid1.lower() and 'i2_mmc' == pid2.lower()):
                return get_mmc_usim_msg_str(usMsgName)
        elif ( 'usim' == pid1.lower() and 'mm' == pid2.lower()):
                return get_mm_usim_msg_str(usMsgName)
        elif ( 'i1_usim' == pid1.lower() and 'i1_mm' == pid2.lower()):
                return get_mm_usim_msg_str(usMsgName)
        elif ( 'i2_usim' == pid1.lower() and 'i2_mm' == pid2.lower()):
                return get_mm_usim_msg_str(usMsgName)
        elif ( 'll' == pid1.lower() and 'gmm' == pid2.lower()):
                return get_gmm_ll_msg_str(usMsgName)
        elif ( 'i1_ll' == pid1.lower() and 'i1_gmm' == pid2.lower()):
                return get_gmm_ll_msg_str(usMsgName)
        elif ( 'i2_ll' == pid1.lower() and 'i2_gmm' == pid2.lower()):
                return get_gmm_ll_msg_str(usMsgName)
        elif ( 'lmm' == pid1.lower() or 'lmm' == pid2.lower()):                
                return get_lmm_nas_msg_str(usMsgName)
        elif ( 'i1_lmm' == pid1.lower() or 'i1_lmm' == pid2.lower()):                
                return get_lmm_nas_msg_str(usMsgName)
        elif ( 'css' == pid1.lower() or 'css' == pid2.lower()):
                return get_mmc_css_msg_str(usMsgName)
        elif ( 'nrmm' == pid1.lower() and 'mmc' == pid2.lower()):
                return get_mmc_nrmm_msg_str(usMsgName)
        elif ( 'mmc' == pid1.lower() and 'nrmm' == pid2.lower()):    # nrmm的pid值大于u16在记录dump时会产生截断，截断值是0x0005，相当于是I1_XSMS，临时使用，待后续解决
                return get_mmc_nrmm_msg_str(usMsgName)
        elif ( 'nrmm' == pid1.lower() and 'regm' == pid2.lower()):   # nrmm的pid值大于u16在记录dump时会产生截断，截断值是0x0005，相当于是I1_XSMS，临时使用，待后续解决
                return get_regm_nrmm_msg_str(usMsgName)
        elif ( 'regm' == pid1.lower() and 'nrmm' == pid2.lower()):   # nrmm的pid值大于u16在记录dump时会产生截断，截断值是0x0005，相当于是I1_XSMS，临时使用，待后续解决
                return get_regm_nrmm_msg_str(usMsgName)
        elif ( 'nrmm' == pid1.lower() and 'regm' == pid2.lower()):   # nrmm的pid值大于u16在记录dump时会产生截断，截断值是0x0005，相当于是I1_XSMS，临时使用，待后续解决
                return get_regm_nrmm_msg_str(usMsgName)		
        elif ( 'mmc' == pid1.lower() or 'mmc' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgName)
        elif ( 'i1_mmc' == pid1.lower() or 'i1_mmc' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgName)
        elif ( 'i2_mmc' == pid1.lower() or 'i2_mmc' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgName)
        elif ( 'mm' == pid1.lower() or 'mm' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgName)
        elif ( 'i1_mm' == pid1.lower() or 'i1_mm' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgName)
        elif ( 'i2_mm' == pid1.lower() or 'i2_mm' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgName)
        elif ( 'gmm' == pid1.lower() or 'gmm' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgName)
        elif ( 'i1_gmm' == pid1.lower() or 'i1_gmm' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgName)
        elif ( 'i2_gmm' == pid1.lower() or 'i2_gmm' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgName)
        elif ( 'taf' == pid1.lower() or 'taf' == pid2.lower()):
                return get_gas_taf_msg_str(usMsgName)
        elif ( 'i1_taf' == pid1.lower() or 'i1_taf' == pid2.lower()):
                return get_gas_taf_msg_str(usMsgName)
        elif ( 'i2_taf' == pid1.lower() or 'i2_taf' == pid2.lower()):
                return get_gas_taf_msg_str(usMsgName)
        else:
                return 'none'

def analysis_gunas_mntn_per_rec_msg_info( instream, fileLocalOffset, outstream):
        instream.seek(fileLocalOffset)

        (receiveTime,)           = struct.unpack('I', instream.read(4))
        (sendPid,)        = struct.unpack('H', instream.read(2))
        (receivePid,)         = struct.unpack('H', instream.read(2))

        (usMsgName,)          = struct.unpack('H', instream.read(2))
        (mmcFsmId,)       = struct.unpack('B', instream.read(1))
        (mmcState,)       = struct.unpack('B', instream.read(1))

        (gmmState,)       = struct.unpack('B', instream.read(1))
        (mmState,)        = struct.unpack('B', instream.read(1))
        (regmFsmId,) = struct.unpack('B', instream.read(1))
        (regmState,) = struct.unpack('B', instream.read(1))
        (utranCtrlFsmId,) = struct.unpack('B', instream.read(1))
        (utranCtrlState,) = struct.unpack('B', instream.read(1))
        (ucReserve1,)       = struct.unpack('B', instream.read(1))
        (ucReserve2,)       = struct.unpack('B', instream.read(1))

        strSendPid      = guas_get_pid_str(sendPid)
        strRcvPid       = guas_get_pid_str(receivePid)
        strMsgId        = get_nas_as_msg_str( strSendPid, strRcvPid, usMsgName)

        strSendPid      = '%s(0x%x)' % ( strSendPid, sendPid)
        strRcvPid       = '%s(0x%x)' % ( strRcvPid, receivePid)
        strMsgId        = '%s(0x%x)' % ( strMsgId, usMsgName)
        strTick         = '0x%x'% receiveTime
        
        #outstream.writelines(["%-15s0x%-7s\n" % ("ulLastTick:", strTick.upper())])

        strMmcFsmId     = '%x'% mmcFsmId        
        #outstream.writelines(["%-15s0x%-7s\n" % ("strMmcFsmId:", strMmcFsmId.upper())])
        
        strMmcState     = '%x'% mmcState
        
        strGmmcState    = '%x'% gmmState
        #outstream.writelines(["%-15s0x%-7s\n" % ("strGmmcState:", strGmmcState.upper())])
        
        strMmState      = '%x'% mmState
        #outstream.writelines(["%-15s0x%-7s\n" % ("strMmState:", strMmState.upper())])
        strRegmFsmId      = '%x'% regmFsmId
        strRegmState      = '%x'% regmState

        strUtranCtrlFsmId      = '%x'% utranCtrlFsmId
        #outstream.writelines(["%-15s0x%-7s\n" % ("strUtranCtrlFsmId:", strUtranCtrlFsmId.upper())])
        strUtranCtrlStat      = '%x'% utranCtrlState
        #outstream.writelines(["%-15s0x%-7s\n" % ("strUtranCtrlStat:", strUtranCtrlStat.upper())])
        
        outstream.writelines(["%-10s%-15s%-15s%-60s0x%-10s0x%-10s0x%-10s0x%-10s0x%-10s0x%-10s0x%-10s0x%-10s\n" % (strTick.upper(), strSendPid, strRcvPid, strMsgId, strMmcFsmId,strMmcState,strGmmcState,strMmState,strRegmFsmId,strRegmState,strUtranCtrlFsmId,strUtranCtrlStat)])


def analysis_gunas_mntn_per_rec_msg_info_version0x02( instream, fileLocalOffset, outstream, ulLooper):
        instream.seek(fileLocalOffset)

        (receiveTime,)           = struct.unpack('I', instream.read(4))
        (sendPid,)        = struct.unpack('H', instream.read(2))
        (receivePid,)         = struct.unpack('H', instream.read(2))

        (usMsgName,)          = struct.unpack('H', instream.read(2))
        (mmcFsmId,)       = struct.unpack('B', instream.read(1))
        (mmcState,)       = struct.unpack('B', instream.read(1))

        (gmmState,)       = struct.unpack('B', instream.read(1))
        (mmState,)        = struct.unpack('B', instream.read(1))
        (regmFsmId,)      = struct.unpack('B', instream.read(1))
        (regmState,)      = struct.unpack('B', instream.read(1))
        (utranCtrlFsmId,) = struct.unpack('B', instream.read(1))
        (utranCtrlState,) = struct.unpack('B', instream.read(1))
        (ucReserve1,)       = struct.unpack('B', instream.read(1))
        (ucReserve2,)       = struct.unpack('B', instream.read(1))

        strSendPid      = guas_get_pid_str(sendPid)
        strRcvPid       = guas_get_pid_str(receivePid)
        strMsgId        = get_nas_as_msg_str( strSendPid, strRcvPid, usMsgName)

        strSendPid      = '%s(0x%x)' % ( strSendPid, sendPid)
        strRcvPid       = '%s(0x%x)' % ( strRcvPid, receivePid)
        strMsgId        = '%s(0x%x)' % ( strMsgId, usMsgName)
        strTick         = '0x%x'% receiveTime
        
        #outstream.writelines(["%-15s0x%-7s\n" % ("ulLastTick:", strTick.upper())])

        strMmcFsmId     = '%x'% mmcFsmId        
        #outstream.writelines(["%-15s0x%-7s\n" % ("strMmcFsmId:", strMmcFsmId.upper())])
        
        strMmcState     = '%x'% mmcState
        
        strGmmcState    = '%x'% gmmState
        #outstream.writelines(["%-15s0x%-7s\n" % ("strGmmcState:", strGmmcState.upper())])
        
        strMmState      = '%x'% mmState
        #outstream.writelines(["%-15s0x%-7s\n" % ("strMmState:", strMmState.upper())])
        strRegmFsmId      = '%x'% regmFsmId
        strRegmState      = '%x'% regmState
        #outstream.writelines(["%-15s0x%-7s\n" % ("strRegmState:", strRegmState.upper())])
        
        strUtranCtrlFsmId      = '%x'% utranCtrlFsmId
        #outstream.writelines(["%-15s0x%-7s\n" % ("strUtranCtrlFsmId:", strUtranCtrlFsmId.upper())])
        strUtranCtrlStat      = '%x'% utranCtrlState
        #outstream.writelines(["%-15s0x%-7s\n" % ("strUtranCtrlStat:", strUtranCtrlStat.upper())])
        
        outstream.writelines(["%-10s%-10s%-15s%-15s%-50s0x%-10s0x%-10s0x%-10s0x%-10s0x%-10s0x%-10s0x%-10s0x%-10s\n" % (ulLooper, strTick.upper(), strSendPid, strRcvPid, strMsgId, strMmcFsmId,strMmcState,strGmmcState,strMmState,strRegmFsmId,strRegmState,strUtranCtrlFsmId,strUtranCtrlStat)])

def analysis_gunas_mntn_log_event_state_other_info_version0x02( instream, outstream):
        (exitTime,)             = struct.unpack('I', instream.read(4))
        (latestIndex,)          = struct.unpack('B', instream.read(1))
        (reserve,)           = struct.unpack('B', instream.read(1))
        (reserve,)           = struct.unpack('B', instream.read(1))
        (reserve,)           = struct.unpack('B', instream.read(1))
        strexitTime             = '0x%X'% exitTime
        strlatestIndex          = '%d'% (latestIndex + 1)
        outstream.writelines(["%-15s%-15s\n" % (strexitTime, strlatestIndex)])

def analysis_gunas_mntn_log_sim_status_info_version0x02( instream, outstream):
        (simPresentStatus,)             = struct.unpack('B', instream.read(1))
        (simType,)                      = struct.unpack('B', instream.read(1))
        (simCsRegStatus,)               = struct.unpack('B', instream.read(1))
        (simPsRegStatus,)               = struct.unpack('B', instream.read(1))
        (psUpdateStatus,)               = struct.unpack('B', instream.read(1))
        (csUpdateStatus,)               = struct.unpack('B', instream.read(1))
        (imsiRefreshStatus,)            = struct.unpack('B', instream.read(1))
        (reserve,)                    = struct.unpack('B', instream.read(1)) 
        (usimRefreshInfo_usimRefreshFlag,)      = struct.unpack('I', instream.read(4))
        (usimRefreshInfo_refreshType,)          = struct.unpack('I', instream.read(4))
        
        strsimPresentStatus             = '0x%X'% simPresentStatus
        strsimType                      = '0x%X'% simType
        strsimCsRegStatus               = '0x%X'% simCsRegStatus
        strsimPsRegStatus               = '0x%X'% simPsRegStatus
        strpsUpdateStatus               = '0x%X'% psUpdateStatus
        strcsUpdateStatus               = '0x%X'% csUpdateStatus
        strimsiRefreshStatus            = '0x%X'% imsiRefreshStatus
        strusimRefreshInfo_usimRefreshFlag      = '0x%X'% usimRefreshInfo_usimRefreshFlag
        strusimRefreshInfo_refreshType          = '0x%X'% usimRefreshInfo_refreshType
        
        outstream.writelines(["simPresentStatus:%-15s\n" % (strsimPresentStatus)])
        outstream.writelines(["simType:%-15s\n" % (strsimType)])
        outstream.writelines(["simCsRegStatus:%-15s\n" % (strsimCsRegStatus)])
        outstream.writelines(["simPsRegStatus:%-15s\n" % (strsimPsRegStatus)])
        outstream.writelines(["psUpdateStatus:%-15s\n" % (strpsUpdateStatus)])
        outstream.writelines(["csUpdateStatus:%-15s\n" % (strcsUpdateStatus)])
        outstream.writelines(["imsiRefreshStatus:%-15s\n" % (strimsiRefreshStatus)])
        outstream.writelines(["ucReserve1:0x%X\n" % (reserve)])
        outstream.writelines(["usimRefreshInfo_usimRefreshFlag.:%-15s\n" % (strusimRefreshInfo_usimRefreshFlag)])
        outstream.writelines(["usimRefreshInfo_refreshType.:%-15s\n" % (strusimRefreshInfo_refreshType)])

def analysis_gunas_mntn_log_ms_identity_info_version0x02( instream, outstream):
        outstream.writelines(["Imsi:0x"])
        analysis_array_data_one_byte(instream, outstream, 9)
        outstream.writelines(["PtmsiSignature:0x"])
        analysis_array_data_one_byte(instream, outstream, 3)
        outstream.writelines(["Ptmsi:0x"])
        analysis_array_data_one_byte(instream, outstream, 4)
        outstream.writelines(["Tmsi:0x"])
        analysis_array_data_one_byte(instream, outstream, 4)
        
        (ueOperMode,)           = struct.unpack('B', instream.read(1))
        strueOperMode           = '0x%X'% ueOperMode
        outstream.writelines(["ueOperMode:%-15s\n" % (strueOperMode)])
        
        (reserve1,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve1:0x%X\n" % (reserve1)])

        (ueIdMask,)           = struct.unpack('B', instream.read(1))
        strueIdMask           = '0x%X'% ueIdMask
        outstream.writelines(["ueIdMask:%-15s\n" % (strueIdMask)])
        
        (lteGutiValid,)           = struct.unpack('B', instream.read(1))
        strueGutiValid           = '0x%X'% lteGutiValid
        outstream.writelines(["lteGutiValid:%-15s\n" % (strueGutiValid)])

        outstream.writelines(["Lai:0x"])
        analysis_array_data_one_byte(instream, outstream, 6)
        outstream.writelines(["Rai:0x"])
        analysis_array_data_one_byte(instream, outstream, 6)
        
        (simLockedFlg,)           = struct.unpack('B', instream.read(1))
        strsimLockedFlg           = '0x%X'% simLockedFlg
        outstream.writelines(["simLockedFlg:%-15s\n" % (strsimLockedFlg)])
        
        (usimRptImsiValidFlg,)  = struct.unpack('B', instream.read(1))
        strusimRptImsiValidFlg  = '0x%X'% usimRptImsiValidFlg
        outstream.writelines(["usimRptImsiValidFlg:%-15s\n" % (strusimRptImsiValidFlg)])
        
        outstream.writelines(["UsimRptImsi:0x"])
        analysis_array_data_one_byte(instream, outstream, 9)
        
        (reserve4,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve1:0x%X\n" % (reserve4)])

def analysis_gunas_mntn_log_ps_security_info_version0x02( instream, outstream):
        (cKSN,)                 = struct.unpack('B', instream.read(1))
        strcKSN                 = '0x%X'% cKSN
        outstream.writelines(["cKSN:%-15s\n" % (strcKSN)])
        
        (reserve1,)           = struct.unpack('B', instream.read(1))
        (reserve2,)           = struct.unpack('B', instream.read(1))
        (reserve3,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve1:0x%X\n" % (reserve1)])
        outstream.writelines(["ucReserve1:0x%X\n" % (reserve2)])
        outstream.writelines(["ucReserve1:0x%X\n" % (reserve3)])        
        
def analysis_gunas_mntn_log_cs_security_info_version0x02( instream, outstream):
        (cKSN,)                 = struct.unpack('B', instream.read(1))
        strcKSN                 = '0x%X'% cKSN
        outstream.writelines(["cKSN:%-15s\n" % (strcKSN)])
        
        (reserve1,)           = struct.unpack('B', instream.read(1))
        (reserve2,)           = struct.unpack('B', instream.read(1))
        (reserve3,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve1:0x%X\n" % (reserve1)])
        outstream.writelines(["ucReserve1:0x%X\n" % (reserve2)])
        outstream.writelines(["ucReserve1:0x%X\n" % (reserve3)])  
        
def analysis_gunas_mntn_log_sim_native_content_info_version0x02( instream, outstream):
        outstream.writelines(["CsLociInfoFile:0x"])
        analysis_array_data_one_byte(instream, outstream, 11)
        outstream.writelines(["PsLociInfoFile:0x"])
        analysis_array_data_one_byte(instream, outstream, 14)
        outstream.writelines(["HplmnPeriFile:0x"])
        analysis_array_data_one_byte(instream, outstream, 1)
        
        (resverd1,)           = struct.unpack('B', instream.read(1))
        (resverd2,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve1:0x%X\n" % (resverd1)])
        outstream.writelines(["ucReserve1:0x%X\n" % (resverd2)])

def analysis_gunas_mntn_log_Ms3GppRel_info_version0x02( instream, outstream):
        #(msGsmRel,)             = struct.unpack('B', instream.read(1))
        #strmsGsmRel             = '%X'% msGsmRel
        outstream.writelines(["msGsmRel:0x%X\n" % struct.unpack('B', instream.read(1))])
        
        (msWcdmaRel,)           = struct.unpack('B', instream.read(1))
        strmsWcdmaRel           = '0x%X'% msWcdmaRel
        outstream.writelines(["msWcdmaRel:%-15s\n" % (strmsWcdmaRel)])
        
        (msSgsnRel,)            = struct.unpack('B', instream.read(1))
        strmsSgsnRel            = '0x%X'% msSgsnRel
        outstream.writelines(["msSgsnRel:%-15s\n" % (strmsSgsnRel)])
        
        (msMscRel,)             = struct.unpack('B', instream.read(1))
        strmsMscRel             = '0x%X'% msMscRel
        outstream.writelines(["msMscRel:%-15s\n" % (strmsMscRel)])
        
        (lteNasRelease,)        = struct.unpack('B', instream.read(1))
        strlteNasRelease        = '0x%X'% lteNasRelease
        outstream.writelines(["lteNasRelease:%-15s\n" % (strlteNasRelease)])
        
        (resverd1,)           = struct.unpack('B', instream.read(1))
        (resverd2,)           = struct.unpack('B', instream.read(1))
        (resverd3,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve1:0x%X\n" % (resverd1)])
        outstream.writelines(["ucReserve1:0x%X\n" % (resverd2)])
        outstream.writelines(["ucReserve1:0x%X\n" % (resverd3)])

def analysis_gunas_mntn_log_MsCapability_info_version0x02( instream, outstream): 
        (Classmark1,)           = struct.unpack('B', instream.read(1))
        strClassmark1           = '0x%X'% Classmark1
        outstream.writelines(["Classmark1:%-15s\n" % (strClassmark1)]) 
        outstream.writelines(["Classmark2:0x"])
        analysis_array_data_one_byte(instream, outstream, 4)
        outstream.writelines(["FddClassmark3:0x"])
        analysis_array_data_one_byte(instream, outstream, 33)
        outstream.writelines(["TddClassmark3:0x"])
        analysis_array_data_one_byte(instream, outstream, 33)
        struct.unpack('B', instream.read(1))
        
        (MsNetworkCapability_NetworkCapabilityLen,)     = struct.unpack('B', instream.read(1))
        strMsNetworkCapability_NetworkCapabilityLen     = '0x%X'% MsNetworkCapability_NetworkCapabilityLen
        outstream.writelines(["MsNetworkCapability_NetworkCapabilityLen:%-15s\n" % (strMsNetworkCapability_NetworkCapabilityLen)])
        outstream.writelines(["MsNetworkCapability_NetworkCapability:0x"])
        analysis_array_data_one_byte(instream, outstream, 9)
        (MsNetworkCapability_A5SupportCtrl,)     = struct.unpack('H', instream.read(2))
        strMsNetworkCapability_A5SupportCtrl     = '0x%X'% MsNetworkCapability_A5SupportCtrl
        outstream.writelines(["MsNetworkCapability_A5SupportCtrl:%-15s\n" % (strMsNetworkCapability_A5SupportCtrl)])
        (MsNetworkCapability_GeaSupportCtrl,)    = struct.unpack('B', instream.read(1))
        strMsNetworkCapability_GeaSupportCtrl    = '0x%X'% MsNetworkCapability_GeaSupportCtrl
        outstream.writelines(["MsNetworkCapability_GeaSupportCtrl:%-15s\n" % (strMsNetworkCapability_GeaSupportCtrl)])
        (ucReserve1,)           = struct.unpack('B', instream.read(1))
        (ucReserve2,)           = struct.unpack('B', instream.read(1))
        (ucReserve3,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve1:0x%X\n" % (ucReserve1)])
        outstream.writelines(["ucReserve1:0x%X\n" % (ucReserve2)])
        outstream.writelines(["ucReserve1:0x%X\n" % (ucReserve3)])

        outstream.writelines(["Imeisv:0x"])
        analysis_array_data_one_byte(instream, outstream, 16)
        outstream.writelines(["Imei:0x"])
        analysis_array_data_one_byte(instream, outstream, 16)
        
        (UeNetworkCapbility_UeNetCapLen,)     = struct.unpack('B', instream.read(1))
        strUeNetworkCapbility_UeNetCapLen     = '0x%X'% UeNetworkCapbility_UeNetCapLen
        outstream.writelines(["UeNetworkCapbility_UeNetCapLen:%-15s\n" % (strUeNetworkCapbility_UeNetCapLen)])
        outstream.writelines(["UeNetworkCapbility_UeNetCap:0x"])
        analysis_array_data_one_byte(instream, outstream, 13)
        (ucReserve4,)           = struct.unpack('B', instream.read(1))    
        (ucReserve5,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve1:0x%X\n" % (ucReserve4)])
        outstream.writelines(["ucReserve1:0x%X\n" % (ucReserve5)])

        (PlatformRatCap_RatNum,)     = struct.unpack('B', instream.read(1))
        strPlatformRatCap_RatNum     = '0x%X'% PlatformRatCap_RatNum
        outstream.writelines(["PlatformRatCap_RatNum:%-15s\n" % (strPlatformRatCap_RatNum)])
        outstream.writelines(["PlatformRatCap_RatPrio:0x"])
        analysis_array_data_one_byte(instream, outstream, 7)
   
        (PlatformBandCap_GsmCapability,)     = struct.unpack('I', instream.read(4))
        strPlatformBandCap_GsmCapability     = '0x%X'% PlatformBandCap_GsmCapability
        outstream.writelines(["PlatformBandCap_GsmCapability:%-15s\n" % (strPlatformBandCap_GsmCapability)])
        
        (MsNotifyNwCapInfo_NotifyNwCsPrioRatList_RatNum,)     = struct.unpack('B', instream.read(1))
        strMsNotifyNwCapInfo_NotifyNwCsPrioRatList_RatNum     = '0x%X'% MsNotifyNwCapInfo_NotifyNwCsPrioRatList_RatNum
        outstream.writelines(["MsNotifyNwCapInfo_NotifyNwCsPrioRatList_RatNum:%-15s\n" % (strMsNotifyNwCapInfo_NotifyNwCsPrioRatList_RatNum)])
        outstream.writelines(["MsNotifyNwCapInfo_NotifyNwCsPrioRatList_RatPrio:0x"])
        analysis_array_data_one_byte(instream, outstream, 7)
        (MsNotifyNwCapInfo_NotifyNwPsPrioRatList_RatNum,)     = struct.unpack('B', instream.read(1))
        strMsNotifyNwCapInfo_NotifyNwPsPrioRatList_RatNum     = '0x%X'% MsNotifyNwCapInfo_NotifyNwPsPrioRatList_RatNum
        outstream.writelines(["MsNotifyNwCapInfo_NotifyNwPsPrioRatList_RatNum:%-15s\n" % (strMsNotifyNwCapInfo_NotifyNwPsPrioRatList_RatNum)])
        outstream.writelines(["MsNotifyNwCapInfo_NotifyNwPsPrioRatList_RatPrio:0x"])
        analysis_array_data_one_byte(instream, outstream, 7)
        (MsNotifyNwCapInfo_NotifyNwEndcCap,)     = struct.unpack('B', instream.read(1))
        strMsNotifyNwCapInfo_NotifyNwEndcCap     = '0x%X'% MsNotifyNwCapInfo_NotifyNwEndcCap
        outstream.writelines(["MsNotifyNwCapInfo_NotifyNwEndcCap:%-15s\n" % (strMsNotifyNwCapInfo_NotifyNwEndcCap)])
        (ucReserve1,)           = struct.unpack('B', instream.read(1))  
        outstream.writelines(["ucReserve1:0x%X\n" % (ucReserve1)])
        (ucReserve2,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve2:0x%X\n" % (ucReserve2)])
        (ucReserve3,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve3:0x%X\n" % (ucReserve3)])
        
        (CardType,)     = struct.unpack('B', instream.read(1))
        strCardType     = '0x%X'% CardType
        outstream.writelines(["CardType:%-15s\n" % (strCardType)])
        (CdmaCapa,)     = struct.unpack('B', instream.read(1))
        strCdmaCapa     = '0x%X'% CdmaCapa
        outstream.writelines(["CdmaCapa:%-15s\n" % (strCdmaCapa)])
        
        (ucReserve4,)           = struct.unpack('B', instream.read(1))  
        outstream.writelines(["ucReserve4:0x%X\n" % (ucReserve4)])
        (ucReserve5,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve5:0x%X\n" % (ucReserve5)])

def analysis_gunas_mntn_log_MsSysCfgInfo_info_version0x02( instream, outstream):
        outstream.writelines(["LteCsServiceCfg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["LteUeUsageSetting:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["nrSupportVoiceCentricFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["VoiceDomainPreference:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MsMode:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsAutoAttachFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["serialRegIn1xAndNrFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["sys1xCoexistWithNrFlg:0x%X\n" % struct.unpack('B', instream.read(1))])

        outstream.writelines(["MsBand_WcdmaBand_Band:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["MsBand_GsmBand_Band:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["MsBand_LteBand:"])
        analysis_array_data_four_byte(instream, outstream, 8)
        outstream.writelines(["MsBand_CdmaBand_Band:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["MsBand_nrBand:"])
        analysis_array_data_four_byte(instream, outstream, 32)

        outstream.writelines(["PrioRatList_RatNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PrioRatList_RatPrio:0x"])
        analysis_array_data_one_byte(instream, outstream, 7)
        (ucReserve1,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve1:0x%X\n" % ucReserve1])
        
        outstream.writelines(["3GPP2RatList_RatNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["3GPP2RatList_RatPrio:0x"])
        analysis_array_data_one_byte(instream, outstream, 2)
        (ucReserve2,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve2:0x%X\n" % ucReserve2])

        outstream.writelines(["ImsConfig_ImsRatSupport_WifiImsSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsConfig_ImsRatSupport_LteImsSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsConfig_ImsRatSupport_UtranImsSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsConfig_ImsRatSupport_GsmImsSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsConfig_ImsRatSupport_WifiEmsSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsConfig_ImsRatSupport_LteEmsSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsConfig_ImsRatSupport_RoamingImsSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsConfig_ImsRatSupport_ImsSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsConfig_ImsRatSupport_nrImsSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsConfig_ImsRatSupport_nrEmsSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve3,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve2:0x%X\n" % ucReserve3])
        (ucReserve4,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve2:0x%X\n" % ucReserve4])
        outstream.writelines(["ImsConfig_ImsCapability_VoiceCallOnLteSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsConfig_ImsCapability_VideoCallOnLteSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsConfig_ImsCapability_SmsOnLteSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsConfig_ImsCapability_VoiceCallOnWifiSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsConfig_ImsCapability_VideoCallOnWifiSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsConfig_ImsCapability_SmsOnWifiSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsConfig_ImsCapability_SmsOnUtranSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsConfig_ImsCapability_SmsOnGsmSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsConfig_ImsCapability_UssdOnImsSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsConfig_ImsCapability_voiceCallOnNrSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsConfig_ImsCapability_videoCallOnNrSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsConfig_ImsCapability_smsOnNrSupportFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        
        outstream.writelines(["DelayedCsfbLauFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SyscfgTriHighRatSrchFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["updateEfLociFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve5,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve8:0x%X\n" % ucReserve5])
        
        outstream.writelines(["SysCfgInfo_DoingSysCfgFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve9,)           = struct.unpack('B', instream.read(1))   
        (ucReserve10,)           = struct.unpack('B', instream.read(1))
        (ucReserve11,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve9:0x%X\n" % ucReserve9])  
        outstream.writelines(["ucReserve10:0x%X\n" % ucReserve10])
        outstream.writelines(["ucReserve11:0x%X\n" % ucReserve11])
        
        outstream.writelines(["DisableLteStaInfo_LteCapabilitystatus:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["DisableLteStaInfo_DisableLteReason:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["DisableLteStaInfo_DisableLteRoamFlg:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["DisableLteStaInfo_DisableLteEmcFlg:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["DisableLteStaInfo_DisableLte3396RunningFlg:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["DisableLteStaInfo_DisableLtePdpRejFlg:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["DisableLteStaInfo_DisableLteDcmCustomFlg:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["DisableLteStaInfo_DisableLteBackoffTimerRunningFlg:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["DisableLteStaInfo_T3396DisableLteByPlmn:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["DisableLteStaInfo_DisableLteDcmDataOffFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve12,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve12:0x%X\n" % ucReserve12])
        (ucReserve13,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve12:0x%X\n" % ucReserve13])

        outstream.writelines(["DisableNrStaInfo_NrCapabilityStatus:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["DisableNrStaInfo_DisableNrReason:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["DisableNrStaInfo_DisableNrRoamFlg:0x%X\n" % struct.unpack('I', instream.read(4))])

        outstream.writelines(["DataSwitchInfo_DataSwitch:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["DataSwitchInfo_DataRoamSwitch:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve14,)           = struct.unpack('B', instream.read(1))
        (ucReserve15,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve14:0x%X\n" % ucReserve14])
        outstream.writelines(["ucReserve15:0x%X\n" % ucReserve15])
        outstream.writelines(["DcmDataOffCtrlFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve16,)           = struct.unpack('B', instream.read(1))   
        (ucReserve17,)           = struct.unpack('B', instream.read(1))
        (ucReserve18,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve16:0x%X\n" % ucReserve16])
        outstream.writelines(["ucReserve17:0x%X\n" % ucReserve17])
        outstream.writelines(["ucReserve18:0x%X\n" % ucReserve18])
        
def analysis_gunas_mntn_log_CampPlmnInfo_info_version0x02( instream, outstream):
        outstream.writelines(["NetRatType:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NetWorkMode:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysSubMode:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
        outstream.writelines(["Lai_PlmnId_Mcc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["Lai_PlmnId_Mnc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["Lai_PlmnId_Lac:0x"])
        analysis_array_data_one_byte(instream, outstream, 2)
        outstream.writelines(["Lai_PlmnId_CampPlmnNetRat:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["Lai_PlmnId_Rac:0x%X\n" % struct.unpack('B', instream.read(1))])
        
        outstream.writelines(["OldLai_PlmnId_Mcc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["OldLai_PlmnId_Mnc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["OldLai_PlmnId_Lac:0x"])
        analysis_array_data_one_byte(instream, outstream, 2)
        outstream.writelines(["OldLai_PlmnId_CampPlmnNetRat:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OldLai_PlmnId_Rac:0x%X\n" % struct.unpack('B', instream.read(1))])
        
        outstream.writelines(["CampCellInfo_Arfcn:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CampCellInfo_CellNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CampCellInfo_RssiNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])  
        
        ulLooper        = 0
        while ulLooper < 8:
            outstream.writelines(["\nCampCellInfo_CellInfo%d:\n" % ulLooper])
            outstream.writelines(["CellId_CellIdLowBit:0x%X\n" % struct.unpack('I', instream.read(4))])
            outstream.writelines(["CellId_CellIdHighBit:0x%X\n" % struct.unpack('I', instream.read(4))])
            outstream.writelines(["CellRssi:0x%X\n" % struct.unpack('H', instream.read(2))])
            outstream.writelines(["CellRscp:0x%X\n" % struct.unpack('H', instream.read(2))])
            outstream.writelines(["CellType:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["SupportEmcFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
            (ucReserve,)           = struct.unpack('B', instream.read(1))
            outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
            (ucReserve,)           = struct.unpack('B', instream.read(1))
            outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
            ulLooper = ulLooper + 1
            
        ulLooper        = 0
        while ulLooper < 8:
            outstream.writelines(["\nCampCellInfo_RssiInfo%d:\n" % ulLooper])
            outstream.writelines(["RssiLevel:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["ChannalQual:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Ecno:0x%X\n" % struct.unpack('B', instream.read(1))])
            (ucReserve,)           = struct.unpack('B', instream.read(1))
            outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
            outstream.writelines(["RssiValue:0x%X\n" % struct.unpack('H', instream.read(2))])
            outstream.writelines(["RscpValue:0x%X\n" % struct.unpack('H', instream.read(2))])
            ulLooper = ulLooper + 1
            
        outstream.writelines(["CampCellInfo_CellDlFreq:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CampCellInfo_CellUlFreq:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CampCellInfo_UeRfPower:0x%X\n" % struct.unpack('H', instream.read(2))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
        outstream.writelines(["OperatorNameInfo_OperatorPlmnId_Mcc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["OperatorNameInfo_OperatorPlmnId_Mnc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["OperatorNameInfo_OperatorNameShort:0x"])
        analysis_array_data_one_byte(instream, outstream, 100)
        outstream.writelines(["OperatorNameInfo_OperatorNameLong:0x"])
        analysis_array_data_one_byte(instream, outstream, 100)
        
        outstream.writelines(["RrcNcellInfo_UtranNcellExist:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["RrcNcellInfo_LteNcellExist:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
        outstream.writelines(["CsgId:0x%X\n" % struct.unpack('I', instream.read(4))])
        
        outstream.writelines(["CsgIdHomeNodeBName_NameLen:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CsgIdHomeNodeBName_NameIndication:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["CsgIdHomeNodeBName_Name:0x"])
        analysis_array_data_one_byte(instream, outstream, 48)
        
        outstream.writelines(["Rac:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["LmmAccessType:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["HomeNodebNameIndication:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["nrTai_plmnId_ulMcc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["nrTai_plmnId_ulMNc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["nrTai_tac_tac:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["nrTai_tac_tacCont:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["nrTai_tac_tacCont1:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
def analysis_gunas_mntn_log_CsDomainInfo_info_version0x02( instream, outstream):
        outstream.writelines(["CsSupportFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["AttFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CsAttachAllow:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CsRegStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        
        outstream.writelines(["CsAcRestriction_PagingRsp:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CsAcRestriction_Register:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CsAcRestriction_NormalService:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CsAcRestriction_EmergencyService:0x%X\n" % struct.unpack('B', instream.read(1))])
        
        outstream.writelines(["T3212Len:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CsDrxLen:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CsRegisterBarToUnBarFlag:0x%X\n" % struct.unpack('I', instream.read(4))])
        
        outstream.writelines(["LastSuccLai_PlmnId_Mcc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["LastSuccLai_PlmnId_Mnc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["LastSuccLai_Lac:0x"])
        analysis_array_data_one_byte(instream, outstream, 2)
        outstream.writelines(["LastSuccLai_CampPlmnNetRat:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["LastSuccLai_Rac:0x%X\n" % struct.unpack('B', instream.read(1))])
        
        outstream.writelines(["CmSrvStatus_MoCallStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CmSrvStatus_MoSsStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CmSrvStatus_MoLcsStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CmSrvStatus_MtCsfbPagingTimerStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CmSrvStatus_CellNotSupportCsmoFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CmSrvStatus_DelayNetworkSerchTimerStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CmSrvStatus_EnableCsfbMtFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CmSrvStatus_LastRedialTransActionFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CmSrvStatus_CsfbEsrFailToGuPhaseInfo_TriggerPlmnSrchFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CmSrvStatus_CsfbEsrFailToGuPhaseInfo_ToGuPhase:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["CmSrvStatus_CcReestFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CmSrvStatus_IsCsfbMtFailTimerRunning:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
        outstream.writelines(["CsDamNoSearchFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["CsSrvStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        
        outstream.writelines(["LaiInfoInAcceptMsg_PlmnId_Mcc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["LaiInfoInAcceptMsg_PlmnId_Mnc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["LaiInfoInAcceptMsg_Lac:0x"])
        analysis_array_data_one_byte(instream, outstream, 2)
        outstream.writelines(["LaiInfoInAcceptMsg_CampPlmnNetRat:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["LaiInfoInAcceptMsg_Rac:0x%X\n" % struct.unpack('B', instream.read(1))])

        outstream.writelines(["lastLteSuccLai_PlmnId_Mcc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["lastLteSuccLai_PlmnId_Mnc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["lastLteSuccLai_Lac:0x"])
        analysis_array_data_one_byte(instream, outstream, 2)
        outstream.writelines(["lastLteSuccLai_CampPlmnNetRat:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["lastLteSuccLai_Rac:0x%X\n" % struct.unpack('B', instream.read(1))])

def analysis_gunas_mntn_log_PsDomainInfo_info_version0x02( instream, outstream):
        outstream.writelines(["PsSupportFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsAttachAllow:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsRegStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsSrvStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        
        outstream.writelines(["PsAcRestriction_PagingRsp:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsAcRestriction_Register:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsAcRestriction_NormalService:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsAcRestriction_EmergencyService:0x%X\n" % struct.unpack('B', instream.read(1))])
        
        outstream.writelines(["PsRegisterBarToUnBarFlag:0x%X\n" % struct.unpack('I', instream.read(4))])
        
        outstream.writelines(["LastSuccRai_Lai_PlmnId_Mcc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["LastSuccRai_Lai_PlmnId_Mnc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["LastSuccRai_Lai_Lac:0x"])
        analysis_array_data_one_byte(instream, outstream, 2)
        outstream.writelines(["LastSuccRai_Lai_CampPlmnNetRat:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["LastSuccRai_Lai_Rac:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["LastSuccRai_Rac:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
        outstream.writelines(["PsDomainDrxPara_SplitPgCycleCode:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsDomainDrxPara_UeUtranPsDrxLen:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsDomainDrxPara_UeEutranPsDrxLen:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsDomainDrxPara_WSysInfoDrxLen:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsDomainDrxPara_LSysInfoDrxLen:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsDomainDrxPara_SplitOnCcch:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsDomainDrxPara_NonDrxTimer:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsDomainDrxPara_PsRegisterContainDrx:0x%X\n" % struct.unpack('B', instream.read(1))])
        
        outstream.writelines(["NwImsVoCap:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsDamNoSearchFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsLocalDetachFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
        outstream.writelines(["GmmProcInfo_Type:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["GmmProcInfo_Flag:0x%X\n" % struct.unpack('H', instream.read(2))])
        
        outstream.writelines(["SmProcFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["GprsSupportChgFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsHandoverTimerStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["psSceneServiceState:0x%X\n" % struct.unpack('B', instream.read(1))])
        
        outstream.writelines(["PsRelCause:0x%X\n" % struct.unpack('I', instream.read(4))])
        
        outstream.writelines(["raiInfoInAcceptMsg_lai_plmnId_Mcc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["raiInfoInAcceptMsg_lai_plmnId_Mnc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["raiInfoInAcceptMsg_lai_Lac:0x"])
        analysis_array_data_one_byte(instream, outstream, 2)
        outstream.writelines(["raiInfoInAcceptMsg_lai_CampPlmnNetRat:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["raiInfoInAcceptMsg_lai_Rac:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["raiInfoInAcceptMsg_Rac:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
        outstream.writelines(["NrRegInfo_LastNrRegTai_PlmnId_ulMcc:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NrRegInfo_LastNrRegTai_PlmnId_ulMnc:0x%X\n" % struct.unpack('B', instream.read(1))])
        
        outstream.writelines(["NrRegInfo_LastNrRegTai_Tac_Tac:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NrRegInfo_LastNrRegTai_Tac_TacCont:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NrRegInfo_LastNrRegTai_Tac_TacCont1:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])

        outstream.writelines(["NrRegInfo_NrGutiInfo_ValidFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["NrRegInfo_NrGutiInfo_Guti_PlmnId_PlmnId:0x"])
        analysis_array_data_one_byte(instream, outstream, 3)
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["NrRegInfo_NrGutiInfo_Guti_AmfSetId:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["NrRegInfo_NrGutiInfo_Guti_AmfRegionId:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NrRegInfo_NrGutiInfo_Guti_AmfPointer:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NrRegInfo_NrGutiInfo_Guti_Tmsi:0x%X\n" % struct.unpack('I', instream.read(4))])

        outstream.writelines(["NrRegInfo_NrRegState:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])

        outstream.writelines(["lteGutiInfo_validFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])

        outstream.writelines(["lteGutiInfo_guti_plmnId_plmnId:0x"])
        analysis_array_data_one_byte(instream, outstream, 3)
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))

        outstream.writelines(["lteGutiInfo_guti_mmeGroupId:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["lteGutiInfo_guti_mmeCode:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["lteGutiInfo_guti_mTmsi:0x%X\n" % struct.unpack('I', instream.read(4))])

def analysis_gunas_mntn_log_BandInfo_info_version0x02( instream, outstream):
        outstream.writelines(["WcdmaBand_Band:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["GsmBand_Band:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["LteBand_LteBand:"])
        analysis_array_data_four_byte(instream, outstream, 8)
        outstream.writelines(["CdmaBand_Band:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["nrBand_Band:"])
        analysis_array_data_four_byte(instream, outstream, 32)

def analysis_gunas_mntn_log_Network3GppRel_info_version0x02( instream, outstream):
        outstream.writelines(["NetMscRel:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NetSgsnRel:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["rel99Count:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["rel98Count:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["sgSnRel98Count:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["sgSnRel99Count:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["sgSnRel98Auth2GCount:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["sgSnRel99Auth2GCount:0x%X\n" % struct.unpack('B', instream.read(1))])

def analysis_gunas_mntn_log_ConnStatus_info_version0x02( instream, outstream):
        outstream.writelines(["CsSigConnStatusFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsSigConnStatusFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsTbfStatusFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["RrcStatusFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CsServiceConnStatusFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CsServiceBufferFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsServiceBufferFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PdpStatusFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["EpsSigConnStatusFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["EpsServiceConnStatusFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["EmergencyServiceFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PsTcServiceFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["EmcPdpStatusFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CsfbServiceStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SrvccCallFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["nrConnStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])

def analysis_gunas_mntn_log_EpsDomainInfo_info_version0x02( instream, outstream):
        outstream.writelines(["T3412Status:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["T3423Status:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["T3402Status:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["T3346Status:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["nwEmcBS:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["AdditionUpdateRsltInfo:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["EpsRegStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["IsRelCauseCsfbHighPrio:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["EpsEmcAttachFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NwImsVoCap:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["T3402Len:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["S1ModeLowLayerFailureFlag:0x%X\n" % struct.unpack('I', instream.read(4))])

def analysis_gunas_mntn_log_PsBearerContext_info_version0x02( instream, outstream):
        ulLooper        = 0

        while ulLooper < 11:
            outstream.writelines(["\nPsBearerContext%d:\n" % ulLooper])
            outstream.writelines(["PsBearerState:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PsBearerIsrFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PsActPending:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PsDeactPending:0x%X\n" % struct.unpack('B', instream.read(1))])
            ulLooper = ulLooper + 1

def analysis_gunas_mntn_log_ImsDomainInfo_info_version0x02( instream, outstream):
        outstream.writelines(["ImsVoiceAvail:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsNormalRegSta:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsNormalCallExistFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["imsVoiceCallExistFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["imsVideoCallExistFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["PersistentBearerState:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsEmcCallExistFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsRegDomain:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsSmsExistFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsSsExistFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsUnavailableType:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ImsEmcDomain:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["ImsCurPlmnId_Mcc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["ImsCurPlmnId_Mnc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["ImsRegResult:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SipStatusCode:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["IsPermForbFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CurRatType:0x%X\n" % struct.unpack('B', instream.read(1))])
        
def analysis_gunas_mntn_log_NoRfInfo_info_version0x02( instream, outstream):
        outstream.writelines(["RfAvailFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["RatType:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
        outstream.writelines(["RrmResourceInfo_MmSndLuRegisterRrmResourceFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["RrmResourceInfo_GmmSndAttRegisterRrmResourceFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["RrmResourceInfo_GmmSndRauRegisterRrmResourceFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
        outstream.writelines(["NoRfCauseInfo_MmNoRfCauseFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NoRfCauseInfo_GmmNoRfCauseFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])

def analysis_gunas_mntn_log_OriginalRejCause_info_version0x02( instream, outstream):
        outstream.writelines(["OriginalRejCause:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["usPsOriginalRejectCause:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["usCsOriginalRejectCause:0x%X\n" % struct.unpack('H', instream.read(2))])

def analysis_gunas_modem0_dump_info( instream, fileOffset, outstream, ulMsgIndex):
        ulLooper        = 0
        ulEndTick       = 0
        ulbeginTick     = 0

        outstream.writelines(["%-10s%-15s%-15s%-60s%-10s%-10s%-10s%-10s%-10s%-10s\n" % ("receiveTime", "sendPid", "usReceivePid","ulMsgId", "mmcFsmId","ucState","gmmState","mmState","regmFsmId","regmState","utranCtrlFsmId","ucState")])
        while ulLooper < MACRO_NAS_MML_MAX_LOG_EVENT_STATE_NUM:
            ulLooperIndex = ( ulLooper + ulMsgIndex) % MACRO_NAS_MML_MAX_LOG_EVENT_STATE_NUM
            fileLocalOffset = fileOffset + ulLooperIndex * MACRO_NAS_MNTN_LOG_MSG_INFO_SIZE
            analysis_gunas_mntn_per_rec_msg_info( instream, fileLocalOffset, outstream)
            ulLooper = ulLooper + 1

        global modem_index
        if modem_index == 2:
                return
#       1437226410 = 0x55aa55aa find end tick
        while ulEndTick != 1437226410:
                (ulEndTick,)       = struct.unpack('I', instream.read(4))
        print ("Mscc End tag is %s" % (ulEndTick))

#       1437226410 = 0x55aa55aa find Begin tick
        while ulbeginTick != 1437226410:
                (ulbeginTick,)       = struct.unpack('I', instream.read(4))
        print ("Mscc begin tag is %s" % (ulbeginTick))

        global GLOBAL_Offset
        GLOBAL_Offset = instream.tell()
        print ("GLOBAL_Offset is %s" % (GLOBAL_Offset))


def analysis_gunas_modem0_dump_info_version0x02( instream, fileOffset, outstream, ulMsgIndex):
        ulLooper        = 0
        ulEndTick       = 0
        ulbeginTick     = 0


        outstream.writelines(["%-10s%-10s%-15s%-15s%-50s%-10s%-12s%-12s%-12s%-12s%-10s%-15s%-15s\n" % ("index", "Tick", "SendPid", "ReceivePid","ulMsgId", "MmcFsmId","MmcState","GmmState","MmState","RegmFsmId","RegmState","UtranCtrlFsmId","UtranCtrlState")])
        while ulLooper < MACRO_NAS_MML_MAX_LOG_EVENT_STATE_NUM:
            ulLooperIndex = ( ulLooper + ulMsgIndex) % MACRO_NAS_MML_MAX_LOG_EVENT_STATE_NUM
            fileLocalOffset = fileOffset + ulLooperIndex * MACRO_NAS_MNTN_LOG_MSG_INFO_SIZE_HIONE
            analysis_gunas_mntn_per_rec_msg_info_version0x02( instream, fileLocalOffset, outstream, (ulLooper + 1))
            ulLooper = ulLooper + 1
        
        outstream.writelines(["\n%-15s%-15s\n" % ("exitTime", "latestIndex")])
        analysis_gunas_mntn_log_event_state_other_info_version0x02( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("SimStatus:")])
        analysis_gunas_mntn_log_sim_status_info_version0x02( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("MsIdentity:")])
        analysis_gunas_mntn_log_ms_identity_info_version0x02( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("PsSecurity:")])
        analysis_gunas_mntn_log_ps_security_info_version0x02( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("CsSecurity:")])
        analysis_gunas_mntn_log_cs_security_info_version0x02( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("SimNativeContent:")])
        analysis_gunas_mntn_log_sim_native_content_info_version0x02( instream, outstream)
        
        (CallMode,)             = struct.unpack('B', instream.read(1))
        strCallMode             = '0x%X'% CallMode
        outstream.writelines(["\nCallMode:%-15s\n" % (strCallMode)])
        (ucReserve1,)           = struct.unpack('B', instream.read(1))
        (ucReserve2,)           = struct.unpack('B', instream.read(1))
        (ucReserve3,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve1:0x%X\n" % (ucReserve1)])
        outstream.writelines(["ucReserve1:0x%X\n" % (ucReserve2)])
        outstream.writelines(["ucReserve1:0x%X\n" % (ucReserve3)])
        
        outstream.writelines(["\n%-15s\n" % ("Ms3GppRel:")])
        analysis_gunas_mntn_log_Ms3GppRel_info_version0x02( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("MsCapability:")])
        analysis_gunas_mntn_log_MsCapability_info_version0x02( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("MsSysCfgInfo:")])
        analysis_gunas_mntn_log_MsSysCfgInfo_info_version0x02( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("CampPlmnInfo:")])
        analysis_gunas_mntn_log_CampPlmnInfo_info_version0x02( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("CsDomainInfo:")])
        analysis_gunas_mntn_log_CsDomainInfo_info_version0x02( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("PsDomainInfo:")])
        analysis_gunas_mntn_log_PsDomainInfo_info_version0x02( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("BandInfo:")])
        analysis_gunas_mntn_log_BandInfo_info_version0x02( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("Network3GppRel:")])
        analysis_gunas_mntn_log_Network3GppRel_info_version0x02( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("ConnStatus:")])
        analysis_gunas_mntn_log_ConnStatus_info_version0x02( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("EpsDomainInfo:")])
        analysis_gunas_mntn_log_EpsDomainInfo_info_version0x02( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("PsBearerContext:")])
        analysis_gunas_mntn_log_PsBearerContext_info_version0x02( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("ImsDomainInfo:")])
        analysis_gunas_mntn_log_ImsDomainInfo_info_version0x02( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("NoRfInfo:")])
        analysis_gunas_mntn_log_NoRfInfo_info_version0x02( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("OriginalRejCause:")])
        analysis_gunas_mntn_log_OriginalRejCause_info_version0x02( instream, outstream)
        
        
        instream.seek(fileOffset + MACRO_NAS_MML_MAX_LOG_EVENT_STATE_NUM * MACRO_NAS_MNTN_LOG_MSG_INFO_SIZE_HIONE)
        global modem_index
        if modem_index == 2:
                return
#       1437226410 = 0x55bb55bb find end tick
        while ulEndTick != 1438340539:
                (ulEndTick,) = struct.unpack('I', instream.read(4))
        print ("NAS End tag is %s" % (ulEndTick))

#       1437226410 = 0x55bb55bb find Begin tick
#        while ulbeginTick != 1438340539:
#                (ulbeginTick,) = struct.unpack('I', instream.read(4))
#        print ("NAS begin tag is %s" % (ulbeginTick))

        global GLOBAL_Offset
        GLOBAL_Offset = g_offset + MACRO_NAS_EXC_LOG_LENGTH_MODEM * (modem_index + 1)
#        GLOBAL_Offset = instream.tell()
        print ("GLOBAL_Offset is %s" % (GLOBAL_Offset))


def analysis_gunas_modemX_event_state_list_dump_info( instream, fileOffset, outstream):
        ulLooperTest = 0

        #outstream.writelines(["\n**************************** analysis_gunas_modemX_event_state_list_dump_info enter! %d*******************************\n" % (fileOffset)])
        instream.seek(fileOffset)
        (ulBeginTick,)       = struct.unpack('I', instream.read(4))
        strBeginTick         = '0x%x'% ulBeginTick
        print ("Begin tag is %s" % (strBeginTick))

        #outstream.writelines(["strModem0LogBeginFlg         %-15s\n" % ( strBeginTick )])
        
        fileOffset = fileOffset + 4
        
        #outstream.writelines(["\n**************************** analysis_gunas_modemX_event_state_list_dump_info enter! %d*******************************\n" % (fileOffset)])
        
        ##### gunas modem0 #########        
#       Old Version begin is 0x55aa55aa
        global Global_Version
        if ulBeginTick == 1437226410:
            Global_Version = 0x01
            analysis_gunas_modem0_dump_info(instream, fileOffset, outstream, ulLooperTest)

#       New Version begin is 0x55bb55bb
        if ulBeginTick == 1438340539:
            Global_Version = 0x02
            analysis_gunas_modem0_dump_info_version0x02(instream, fileOffset, outstream, ulLooperTest)

        return True

def analysis_gunas_dump_info( infile, offset, outfile):
        instream = infile
        outstream  = outfile
        fileOffset = eval(offset)

        global g_offset
        g_offset = eval(offset)
        
        #outstream.writelines(["\n**************************** WUMAI:GUNAS_DUMP_ANALYSIS_2016_01_22_VERSION_1.0 *******************************\n"])
        
        ##### gunas modem0 PARSE EVENT STATE #########   
        outstream.writelines(["\n**************************** modem0:analysis_gunas_dump_info begin!*******************************\n"])             
        global modem_index
        global GLOBAL_Offset
        modem_index = 0
        analysis_gunas_modemX_event_state_list_dump_info( instream, fileOffset, outstream )
        outstream.writelines(["\n**************************** modem0:analysis_gunas_dump_info end!*******************************\n"])       
        
        
        ##### gunas modem1 PARSE EVENT STATE #########                
        outstream.writelines(["\n**************************** modem1:analysis_gunas_dump_info begin!*******************************\n"])
#        fileOffset = fileOffset + MACRO_MODEM0_ADDR_LENGTH        
#        global GLOBAL_Offset
        fileOffset = GLOBAL_Offset
#        global modem_index
        modem_index = 1
        analysis_gunas_modemX_event_state_list_dump_info( instream, fileOffset, outstream )
        outstream.writelines(["\n**************************** modem1:analysis_gunas_dump_info end!*******************************\n"])               
        
        
        ##### gunas modem1 PARSE EVENT STATE #########                
        outstream.writelines(["\n**************************** modem2:analysis_gunas_dump_info begin!*******************************\n"])
#        fileOffset = fileOffset + MACRO_MODEM0_ADDR_LENGTH        
#        global GLOBAL_Offset
        fileOffset = GLOBAL_Offset
#        global modem_index
        modem_index = 2
        analysis_gunas_modemX_event_state_list_dump_info( instream, fileOffset, outstream )
        outstream.writelines(["\n**************************** modem2:analysis_gunas_dump_info end!*******************************\n"])
        return True


########################################################################################
def entry_0x2200006(infile, field, offset, len, version, mode, outfile):
        ########check parameter start#############
        if not field == '0x2200006':
            print ("hidis field is %s" % (field))
            print ("current field is 0x2200006")
            return error['ERR_CHECK_FIELD']
        elif not version == '0x0009':
            print ("hidis version is %s" % (version))
            print ("current version is 0x0009")
            return error['ERR_CHECK_VERSION']
        #########check parameter end##############
        ret = analysis_gunas_dump_info( infile, offset, outfile)

        #c = msvcrt.getch()
        return 0


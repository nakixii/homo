#!/usr/bin/env python
# coding: utf-8
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
        outstream.writelines(["%X" % struct.unpack('I', instream.read(4))])
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
            return ''

def analysis_gunas_mntn_per_rec_msg_inf( instream, fileLocalOffset, outstream):
    instream.seek(fileLocalOffset)

    (receiveTime,)           = struct.unpack('I', instream.read(4))
    (sendPid,)        = struct.unpack('H', instream.read(2))
    (receivePid,)         = struct.unpack('H', instream.read(2))

    (usMsgName,)          = struct.unpack('H', instream.read(2))
    (mmcFsmId,)       = struct.unpack('B', instream.read(1))
    (mmcSta,)       = struct.unpack('B', instream.read(1))

    (gmmSta,)       = struct.unpack('B', instream.read(1))
    (mmSta,)        = struct.unpack('B', instream.read(1))
    (regmFsmId,) = struct.unpack('B', instream.read(1))
    (regmSta,) = struct.unpack('B', instream.read(1))
    (utranCtrlFsmId,) = struct.unpack('B', instream.read(1))
    (utranCtrlSta,) = struct.unpack('B', instream.read(1))
    (ucrsv1,)       = struct.unpack('B', instream.read(1))
    (ucrsv2,)       = struct.unpack('B', instream.read(1))

    strSendPid      = guas_get_pid_str(sendPid)
    strRcvPid       = guas_get_pid_str(receivePid)
    strMsgId        = get_nas_as_msg_str( strSendPid, strRcvPid, usMsgName)

    strSendPid      = '%s(%x)' % ( strSendPid, sendPid)
    strRcvPid       = '%s(%x)' % ( strRcvPid, receivePid)
    strMsgId        = '%s(%x)' % ( strMsgId, usMsgName)
    strTick         = '%x'% receiveTime

    #outstream.writelines(["%s0x%-7s\n" % ("ulLastTick:", strTick.upper())])

    strMmcFsmId     = '%x'% mmcFsmId
    #outstream.writelines(["%s0x%-7s\n" % ("strMmcFsmId:", strMmcFsmId.upper())])

    strMmcSta     = '%x'% mmcSta

    strGmmcSta    = '%x'% gmmSta
    #outstream.writelines(["%s0x%-7s\n" % ("strGmmcSta:", strGmmcSta.upper())])

    strMmSta      = '%x'% mmSta
    #outstream.writelines(["%s0x%-7s\n" % ("strMmSta:", strMmSta.upper())])
    strRegmFsmId      = '%x'% regmFsmId
    strRegmSta      = '%x'% regmSta

    strUtranCtrlFsmId      = '%x'% utranCtrlFsmId
    #outstream.writelines(["%s0x%-7s\n" % ("strUtranCtrlFsmId:", strUtranCtrlFsmId.upper())])
    strUtranCtrlStat      = '%x'% utranCtrlSta
    #outstream.writelines(["%s0x%-7s\n" % ("strUtranCtrlStat:", strUtranCtrlStat.upper())])

    outstream.writelines(["%s %s %s %s %s %s %s %s %s %s %s %s\n" % (strTick.upper(), strSendPid, strRcvPid, strMsgId, strMmcFsmId,strMmcSta,strGmmcSta,strMmSta,strRegmFsmId,strRegmSta,strUtranCtrlFsmId,strUtranCtrlStat)])


def analysis_gunas_mntn_per_rec_msg_inf_version0x02( instream, fileLocalOffset, outstream, ulLooper):
    instream.seek(fileLocalOffset)

    (receiveTime,)           = struct.unpack('I', instream.read(4))
    (sendPid,)        = struct.unpack('H', instream.read(2))
    (receivePid,)         = struct.unpack('H', instream.read(2))

    (usMsgName,)          = struct.unpack('H', instream.read(2))
    (mmcFsmId,)       = struct.unpack('B', instream.read(1))
    (mmcSta,)       = struct.unpack('B', instream.read(1))

    (gmmSta,)       = struct.unpack('B', instream.read(1))
    (mmSta,)        = struct.unpack('B', instream.read(1))
    (regmFsmId,)      = struct.unpack('B', instream.read(1))
    (regmSta,)      = struct.unpack('B', instream.read(1))
    (utranCtrlFsmId,) = struct.unpack('B', instream.read(1))
    (utranCtrlSta,) = struct.unpack('B', instream.read(1))
    (ucrsv1,)       = struct.unpack('B', instream.read(1))
    (ucrsv2,)       = struct.unpack('B', instream.read(1))

    strSendPid      = guas_get_pid_str(sendPid)
    strRcvPid       = guas_get_pid_str(receivePid)
    strMsgId        = get_nas_as_msg_str( strSendPid, strRcvPid, usMsgName)

    strSendPid      = '%s(%x)' % ( strSendPid, sendPid)
    strRcvPid       = '%s(%x)' % ( strRcvPid, receivePid)
    strMsgId        = '%s(%x)' % ( strMsgId, usMsgName)
    strTick         = '%x'% receiveTime

    #outstream.writelines(["%s0x%-7s\n" % ("ulLastTick:", strTick.upper())])

    strMmcFsmId     = '%x'% mmcFsmId
    #outstream.writelines(["%s0x%-7s\n" % ("strMmcFsmId:", strMmcFsmId.upper())])

    strMmcSta     = '%x'% mmcSta

    strGmmcSta    = '%x'% gmmSta
    #outstream.writelines(["%s0x%-7s\n" % ("strGmmcSta:", strGmmcSta.upper())])

    strMmSta      = '%x'% mmSta
    #outstream.writelines(["%s0x%-7s\n" % ("strMmSta:", strMmSta.upper())])
    strRegmFsmId      = '%x'% regmFsmId
    strRegmSta      = '%x'% regmSta
    #outstream.writelines(["%s0x%-7s\n" % ("strRegmSta:", strRegmSta.upper())])

    strUtranCtrlFsmId      = '%x'% utranCtrlFsmId
    #outstream.writelines(["%s0x%-7s\n" % ("strUtranCtrlFsmId:", strUtranCtrlFsmId.upper())])
    strUtranCtrlStat      = '%x'% utranCtrlSta
    #outstream.writelines(["%s0x%-7s\n" % ("strUtranCtrlStat:", strUtranCtrlStat.upper())])

    outstream.writelines(["%s %s %s %s %s %s %s %s %s %s %s %s %s\n" % (ulLooper, strTick.upper(), strSendPid, strRcvPid, strMsgId, strMmcFsmId,strMmcSta,strGmmcSta,strMmSta,strRegmFsmId,strRegmSta,strUtranCtrlFsmId,strUtranCtrlStat)])

def analysis_gunas_mntn_log_event_state_other_inf_version0x02( instream, outstream):
    (exitTime,)             = struct.unpack('I', instream.read(4))
    (latestIndex,)          = struct.unpack('B', instream.read(1))
    (rsv,)           = struct.unpack('B', instream.read(1))
    (rsv,)           = struct.unpack('B', instream.read(1))
    (rsv,)           = struct.unpack('B', instream.read(1))
    strexitTime             = '%X'% exitTime
    strlatestIndex          = '%d'% (latestIndex + 1)
    outstream.writelines(["%s%s\n" % (strexitTime, strlatestIndex)])

def analysis_gunas_mntn_log_sim_sta_inf_version0x02( instream, outstream):
    (simPresSta,)             = struct.unpack('B', instream.read(1))
    (simTyp,)                      = struct.unpack('B', instream.read(1))
    (simCsRegSta,)               = struct.unpack('B', instream.read(1))
    (simPsRegSta,)               = struct.unpack('B', instream.read(1))
    (psUpdSta,)               = struct.unpack('B', instream.read(1))
    (csUpdSta,)               = struct.unpack('B', instream.read(1))
    (imsiRfreSta,)            = struct.unpack('B', instream.read(1))
    (rsv,)                    = struct.unpack('B', instream.read(1))
    (usimRfreinf_usimRfreFlg,)      = struct.unpack('I', instream.read(4))
    (usimRfreinf_RfreTyp,)          = struct.unpack('I', instream.read(4))

    strsimPresSta             = '%X'% simPresSta
    strsimTyp                      = '%X'% simTyp
    strsimCsRegSta               = '%X'% simCsRegSta
    strsimPsRegSta               = '%X'% simPsRegSta
    strpsUpdSta               = '%X'% psUpdSta
    strcsUpdSta               = '%X'% csUpdSta
    strimsiRfreSta            = '%X'% imsiRfreSta
    strusimRfreinf_usimRfreFlg      = '%X'% usimRfreinf_usimRfreFlg
    strusimRfreinf_RfreTyp          = '%X'% usimRfreinf_RfreTyp

    outstream.writelines(["simPresSta:%s\n" % (strsimPresSta)])
    outstream.writelines(["simTyp:%s\n" % (strsimTyp)])
    outstream.writelines(["simCsRegSta:%s\n" % (strsimCsRegSta)])
    outstream.writelines(["simPsRegSta:%s\n" % (strsimPsRegSta)])
    outstream.writelines(["psUpdSta:%s\n" % (strpsUpdSta)])
    outstream.writelines(["csUpdSta:%s\n" % (strcsUpdSta)])
    outstream.writelines(["imsiRfreSta:%s\n" % (strimsiRfreSta)])
    outstream.writelines(["ucrsv1:%X\n" % (rsv)])
    outstream.writelines(["usimRfreInfUsimRfreFlg.:%s\n" % (strusimRfreinf_usimRfreFlg)])
    outstream.writelines(["usimRfreInfRfreTyp.:%s\n" % (strusimRfreinf_RfreTyp)])

def analysis_gunas_mntn_log_ms_identity_inf_version0x02( instream, outstream):
    outstream.writelines(["imsi:"])
    analysis_array_data_one_byte(instream, outstream, 9)
    outstream.writelines(["ptmsiSignature:"])
    analysis_array_data_one_byte(instream, outstream, 3)
    outstream.writelines(["ptmsi:"])
    analysis_array_data_one_byte(instream, outstream, 4)
    outstream.writelines(["tmsi:"])
    analysis_array_data_one_byte(instream, outstream, 4)

    (ueOperMode,)           = struct.unpack('B', instream.read(1))
    strueOperMode           = '%X'% ueOperMode
    outstream.writelines(["ueOperMode:%s\n" % (strueOperMode)])

    (rsv1,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv1:%X\n" % (rsv1)])

    (ueIdMask,)           = struct.unpack('B', instream.read(1))
    strueIdMask           = '%X'% ueIdMask
    outstream.writelines(["ueIdMask:%s\n" % (strueIdMask)])

    (lteGutiValid,)           = struct.unpack('B', instream.read(1))
    strueGutiValid           = '%X'% lteGutiValid
    outstream.writelines(["lteGutiValid:%s\n" % (strueGutiValid)])

    outstream.writelines(["lai:"])
    analysis_array_data_one_byte(instream, outstream, 6)
    outstream.writelines(["rai:"])
    analysis_array_data_one_byte(instream, outstream, 6)

    (simLockedFlg,)           = struct.unpack('B', instream.read(1))
    strsimLockedFlg           = '%X'% simLockedFlg
    outstream.writelines(["simLockedFlg:%s\n" % (strsimLockedFlg)])

    (usimRptImsiValidFlg,)  = struct.unpack('B', instream.read(1))
    strusimRptImsiValidFlg  = '%X'% usimRptImsiValidFlg
    outstream.writelines(["usimRptImsiValidFlg:%s\n" % (strusimRptImsiValidFlg)])

    outstream.writelines(["usimRptImsi:"])
    analysis_array_data_one_byte(instream, outstream, 9)

    (rsv4,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv1:%X\n" % (rsv4)])

def analysis_gunas_mntn_log_ps_security_inf_version0x02( instream, outstream):
    (cKSN,)                 = struct.unpack('B', instream.read(1))
    strcKSN                 = '%X'% cKSN
    outstream.writelines(["cKSN:%s\n" % (strcKSN)])

    (rsv1,)           = struct.unpack('B', instream.read(1))
    (rsv2,)           = struct.unpack('B', instream.read(1))
    (rsv3,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv1:%X\n" % (rsv1)])
    outstream.writelines(["ucrsv1:%X\n" % (rsv2)])
    outstream.writelines(["ucrsv1:%X\n" % (rsv3)])

def analysis_gunas_mntn_log_cs_security_inf_version0x02( instream, outstream):
    (cKSN,)                 = struct.unpack('B', instream.read(1))
    strcKSN                 = '%X'% cKSN
    outstream.writelines(["cKSN:%s\n" % (strcKSN)])

    (rsv1,)           = struct.unpack('B', instream.read(1))
    (rsv2,)           = struct.unpack('B', instream.read(1))
    (rsv3,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv1:%X\n" % (rsv1)])
    outstream.writelines(["ucrsv1:%X\n" % (rsv2)])
    outstream.writelines(["ucrsv1:%X\n" % (rsv3)])

def analysis_gunas_mntn_log_sim_native_content_inf_version0x02( instream, outstream):
    outstream.writelines(["csLociInfFile:"])
    analysis_array_data_one_byte(instream, outstream, 11)
    outstream.writelines(["psLociInfFile:"])
    analysis_array_data_one_byte(instream, outstream, 14)
    outstream.writelines(["hplmnPeriFile:"])
    analysis_array_data_one_byte(instream, outstream, 1)

    (resverd1,)           = struct.unpack('B', instream.read(1))
    (resverd2,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv1:%X\n" % (resverd1)])
    outstream.writelines(["ucrsv1:%X\n" % (resverd2)])

def analysis_gunas_mntn_log_Ms3GppRel_inf_version0x02( instream, outstream):
    #(msGsmRel,)             = struct.unpack('B', instream.read(1))
    #strmsGsmRel             = '%X'% msGsmRel
    outstream.writelines(["msGsmRel:%X\n" % struct.unpack('B', instream.read(1))])

    (msWcdmaRel,)           = struct.unpack('B', instream.read(1))
    strmsWcdmaRel           = '%X'% msWcdmaRel
    outstream.writelines(["msWcdmaRel:%s\n" % (strmsWcdmaRel)])

    (msSgsnRel,)            = struct.unpack('B', instream.read(1))
    strmsSgsnRel            = '%X'% msSgsnRel
    outstream.writelines(["msSgsnRel:%s\n" % (strmsSgsnRel)])

    (msMscRel,)             = struct.unpack('B', instream.read(1))
    strmsMscRel             = '%X'% msMscRel
    outstream.writelines(["msMscRel:%s\n" % (strmsMscRel)])

    (lteNasRel,)        = struct.unpack('B', instream.read(1))
    strlteNasRel        = '%X'% lteNasRel
    outstream.writelines(["lteNasRel:%s\n" % (strlteNasRel)])

    (resverd1,)           = struct.unpack('B', instream.read(1))
    (resverd2,)           = struct.unpack('B', instream.read(1))
    (resverd3,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv1:%X\n" % (resverd1)])
    outstream.writelines(["ucrsv1:%X\n" % (resverd2)])
    outstream.writelines(["ucrsv1:%X\n" % (resverd3)])

def analysis_gunas_mntn_log_MsCap_inf_version0x02( instream, outstream):
    (Classmark1,)           = struct.unpack('B', instream.read(1))
    strClassmark1           = '%X'% Classmark1
    outstream.writelines(["classmark1:%s\n" % (strClassmark1)])
    outstream.writelines(["classmark2:"])
    analysis_array_data_one_byte(instream, outstream, 4)
    outstream.writelines(["fddClassmark3:"])
    analysis_array_data_one_byte(instream, outstream, 33)
    outstream.writelines(["tddClassmark3:"])
    analysis_array_data_one_byte(instream, outstream, 33)
    struct.unpack('B', instream.read(1))

    (MsNetCap_NetCapLen,)     = struct.unpack('B', instream.read(1))
    strMsNetCap_NetCapLen     = '%X'% MsNetCap_NetCapLen
    outstream.writelines(["msNetCapNetCapLen:%s\n" % (strMsNetCap_NetCapLen)])
    outstream.writelines(["msNetCapNetCap:"])
    analysis_array_data_one_byte(instream, outstream, 9)
    (MsNetCap_A5SptCtrl,)     = struct.unpack('H', instream.read(2))
    strMsNetCap_A5SptCtrl     = '%X'% MsNetCap_A5SptCtrl
    outstream.writelines(["msNetCapA5SptCtrl:%s\n" % (strMsNetCap_A5SptCtrl)])
    (MsNetCap_GeaSptCtrl,)    = struct.unpack('B', instream.read(1))
    strMsNetCap_GeaSptCtrl    = '%X'% MsNetCap_GeaSptCtrl
    outstream.writelines(["msNetCapGeaSptCtrl:%s\n" % (strMsNetCap_GeaSptCtrl)])
    (ucrsv1,)           = struct.unpack('B', instream.read(1))
    (ucrsv2,)           = struct.unpack('B', instream.read(1))
    (ucrsv3,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv1:%X\n" % (ucrsv1)])
    outstream.writelines(["ucrsv1:%X\n" % (ucrsv2)])
    outstream.writelines(["ucrsv1:%X\n" % (ucrsv3)])

    outstream.writelines(["imeisv:"])
    analysis_array_data_one_byte(instream, outstream, 16)
    outstream.writelines(["imei:"])
    analysis_array_data_one_byte(instream, outstream, 16)

    (UeNetCap_UeNetCapLen,)     = struct.unpack('B', instream.read(1))
    strUeNetCap_UeNetCapLen     = '%X'% UeNetCap_UeNetCapLen
    outstream.writelines(["ueNetCapUeNetCapLen:%s\n" % (strUeNetCap_UeNetCapLen)])
    outstream.writelines(["ueNetCapUeNetCap:"])
    analysis_array_data_one_byte(instream, outstream, 13)
    (ucrsv4,)           = struct.unpack('B', instream.read(1))
    (ucrsv5,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv1:%X\n" % (ucrsv4)])
    outstream.writelines(["ucrsv1:%X\n" % (ucrsv5)])

    (PlatformRatCap_RatNum,)     = struct.unpack('B', instream.read(1))
    strPlatformRatCap_RatNum     = '%X'% PlatformRatCap_RatNum
    outstream.writelines(["platformRatCapRatNum:%s\n" % (strPlatformRatCap_RatNum)])
    outstream.writelines(["platformRatCapRatPrio:"])
    analysis_array_data_one_byte(instream, outstream, 7)

    (PlatformBandCap_GsmCap,)     = struct.unpack('I', instream.read(4))
    strPlatformBandCap_GsmCap     = '%X'% PlatformBandCap_GsmCap
    outstream.writelines(["platformBandCapGsmCap:%s\n" % (strPlatformBandCap_GsmCap)])

    (MsNtfyNwCapInf_NtfyNwCsPrioRatList_RatNum,)     = struct.unpack('B', instream.read(1))
    strMsNtfyNwCapInf_NtfyNwCsPrioRatList_RatNum     = '%X'% MsNtfyNwCapInf_NtfyNwCsPrioRatList_RatNum
    outstream.writelines(["msNtfyNwCapInfNtfyNwCsPrioRatListRatNum:%s\n" % (strMsNtfyNwCapInf_NtfyNwCsPrioRatList_RatNum)])
    outstream.writelines(["msNtfyNwCapInfNtfyNwCsPrioRatListRatPrio:"])
    analysis_array_data_one_byte(instream, outstream, 7)
    (MsNtfyNwCapInf_NtfyNwPsPrioRatList_RatNum,)     = struct.unpack('B', instream.read(1))
    strMsNtfyNwCapInf_NtfyNwPsPrioRatList_RatNum     = '%X'% MsNtfyNwCapInf_NtfyNwPsPrioRatList_RatNum
    outstream.writelines(["msNtfyNwCapInfNtfyNwPsPrioRatListRatNum:%s\n" % (strMsNtfyNwCapInf_NtfyNwPsPrioRatList_RatNum)])
    outstream.writelines(["msNtfyNwCapInfNtfyNwPsPrioRatListRatPrio:"])
    analysis_array_data_one_byte(instream, outstream, 7)
    (MsNtfyNwCapInf_NtfyNwEndcCap,)     = struct.unpack('B', instream.read(1))
    strMsNtfyNwCapInf_NtfyNwEndcCap     = '%X'% MsNtfyNwCapInf_NtfyNwEndcCap
    outstream.writelines(["msNtfyNwCapInfNtfyNwEndcCap:%s\n" % (strMsNtfyNwCapInf_NtfyNwEndcCap)])
    (ucrsv1,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv1:%X\n" % (ucrsv1)])
    (ucrsv2,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv2:%X\n" % (ucrsv2)])
    (ucrsv3,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv3:%X\n" % (ucrsv3)])

    (CardTyp,)     = struct.unpack('B', instream.read(1))
    strCardTyp     = '%X'% CardTyp
    outstream.writelines(["cardTyp:%s\n" % (strCardTyp)])
    (CdmaCapa,)     = struct.unpack('B', instream.read(1))
    strCdmaCapa     = '%X'% CdmaCapa
    outstream.writelines(["cdmaCapa:%s\n" % (strCdmaCapa)])

    (ucrsv4,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv4:%X\n" % (ucrsv4)])
    (ucrsv5,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv5:%X\n" % (ucrsv5)])

def analysis_gunas_mntn_log_MsSysCfgInf_inf_version0x02( instream, outstream):
    outstream.writelines(["lteCsSrvCfg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["lteUeUsageSetting:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["nrSptVoiceCentricFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["voiceDomainPref:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["msMode:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psAutoAttFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["serialRegIn1xAndNrFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["sys1xCoexistWithNrFlg:%X\n" % struct.unpack('B', instream.read(1))])

    outstream.writelines(["msBandWcdmaBandBand:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["msBandGsmBandBand:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["msBandLteBand:"])
    analysis_array_data_four_byte(instream, outstream, 8)
    outstream.writelines(["msBandCdmaBandBand:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["msBandNrBand:"])
    analysis_array_data_four_byte(instream, outstream, 32)

    outstream.writelines(["prioRatListRatNum:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["prioRatListRatPrio:"])
    analysis_array_data_one_byte(instream, outstream, 7)

    outstream.writelines(["3GPP2RatListRatNum:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["3GPP2RatListRatPrio:"])
    analysis_array_data_one_byte(instream, outstream, 2)
    (ucrsv2,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv2:%X\n" % ucrsv2])

    outstream.writelines(["imsCfgImsRatSptWifiImsSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsCfgImsRatSptLteImsSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsCfgImsRatSptUtranImsSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsCfgImsRatSptGsmImsSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsCfgImsRatSptWifiEmsSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsCfgImsRatSptLteEmsSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsCfgImsRatSptRoamingImsSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsCfgImsRatSptImsSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsCfgImsRatSptNrImsSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsCfgImsRatSptNrEmsSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv3,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv2:%X\n" % ucrsv3])
    (ucrsv4,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv2:%X\n" % ucrsv4])
    outstream.writelines(["imsCfgImsCapVoiceCallOnLteSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsCfgImsCapVideoCallOnLteSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsCfgImsCapSmsOnLteSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsCfgImsCapVoiceCallOnWifiSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsCfgImsCapVideoCallOnWifiSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsCfgImsCapSmsOnWifiSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsCfgImsCapSmsOnUtranSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsCfgImsCapSmsOnGsmSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsCfgImsCapUssdOnImsSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsCfgImsCapVoiceCallOnNrSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsCfgImsCapVideoCallOnNrSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsCfgImsCapSmsOnNrSptFlg:%X\n" % struct.unpack('B', instream.read(1))])

    outstream.writelines(["delayedCsfbLauFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["syscfgTriHighRatSrchFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["updEfLociFlg:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv5,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv8:%X\n" % ucrsv5])

    outstream.writelines(["sysCfgInfDoingSysCfgFlg:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv9,)           = struct.unpack('B', instream.read(1))
    (ucrsv10,)           = struct.unpack('B', instream.read(1))
    (ucrsv11,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv9:%X\n" % ucrsv9])
    outstream.writelines(["ucrsv10:%X\n" % ucrsv10])
    outstream.writelines(["ucrsv11:%X\n" % ucrsv11])

    outstream.writelines(["dsbLteStaInfLteCapSta:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["dsbLteStaInfDsbLteRsn:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["dsbLteStaInfDsbLteRoamFlg:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["dsbLteStaInfDsbLteEmcFlg:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["dsbLteStaInfDsbLte3396RunningFlg:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["dsbLteStaInfDsbLtePdpRejFlg:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["dsbLteStaInfDsbLteDcmCustomFlg:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["dsbLteStaInfDsbLteBackoffTimerRunningFlg:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["dsbLteStaInfT3396DsbLteByPlmn:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["dsbLteStaInfDsbLteDcmDataOffFlg:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv12,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv12:%X\n" % ucrsv12])
    (ucrsv13,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv12:%X\n" % ucrsv13])

    outstream.writelines(["dsbNrStaInfNrCapSta:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["dsbNrStaInfDsbNrRsn:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["dsbNrStaInfDsbNrRoamFlg:%X\n" % struct.unpack('I', instream.read(4))])

    outstream.writelines(["dataSwitchInfDataSwitch:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["dataSwitchInfDataRoamSwitch:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv14,)           = struct.unpack('B', instream.read(1))
    (ucrsv15,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv14:%X\n" % ucrsv14])
    outstream.writelines(["ucrsv15:%X\n" % ucrsv15])
    outstream.writelines(["dcmDataOffCtrlFlg:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv16,)           = struct.unpack('B', instream.read(1))
    (ucrsv17,)           = struct.unpack('B', instream.read(1))
    (ucrsv18,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv16:%X\n" % ucrsv16])
    outstream.writelines(["ucrsv17:%X\n" % ucrsv17])
    outstream.writelines(["ucrsv18:%X\n" % ucrsv18])

def analysis_gunas_mntn_log_CampPlmninf_inf_version0x02( instream, outstream):
    outstream.writelines(["netRatTyp:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["netMode:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["sysSubMode:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["tempCampStat:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["cnTyp:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])

    outstream.writelines(["laiPlmnIdMcc:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["laiPlmnIdMnc:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["laiPlmnIdLac:"])
    analysis_array_data_one_byte(instream, outstream, 2)
    outstream.writelines(["laiPlmnIdCampPlmnNetRat:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["laiCampCnTyp:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["laiPlmnIdRac:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])

    outstream.writelines(["oldLaiPlmnIdMcc:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["oldLaiPlmnIdMnc:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["oldLaiPlmnIdLac:"])
    analysis_array_data_one_byte(instream, outstream, 2)
    outstream.writelines(["oldLaiPlmnIdCampPlmnNetRat:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["oldLaiCampCnTyp:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["oldLaiPlmnIdRac:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])

    outstream.writelines(["campCellInfArfcn:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["campCellInfCellNum:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["campCellInfRssiNum:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])

    ulLooper        = 0
    while ulLooper < 8:
        outstream.writelines(["\nCampCellInfCellInf%d:\n" % ulLooper])
        outstream.writelines(["cellIdCellIdLowBit:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["cellIdCellIdHighBit:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["cellRssi:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["cellRscp:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["cellTyp:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["sptEmcFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucrsv,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucrsv:%X\n" % ucrsv])
        (ucrsv,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucrsv:%X\n" % ucrsv])
        ulLooper = ulLooper + 1

    ulLooper        = 0
    while ulLooper < 8:
        outstream.writelines(["\nCampCellInfRssiInf%d:\n" % ulLooper])
        outstream.writelines(["rssiLevel:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["channalQual:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ecno:%X\n" % struct.unpack('B', instream.read(1))])
        (ucrsv,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucrsv:%X\n" % ucrsv])
        outstream.writelines(["rssiValue:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["rscpValue:%X\n" % struct.unpack('H', instream.read(2))])
        ulLooper = ulLooper + 1

    outstream.writelines(["campCellInfCellDlFreq:%X\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["campCellInfCellUlFreq:%X\n" % struct.unpack('H', instream.read(2))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])

    outstream.writelines(["optrNameInfOptrPlmnIdMcc:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["optrNameInfOptrPlmnIdMnc:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["optrNameInfOptrNameShort:"])
    analysis_array_data_one_byte(instream, outstream, 100)
    outstream.writelines(["optrNameInfOptrNameLong:"])
    analysis_array_data_one_byte(instream, outstream, 100)

    outstream.writelines(["csgId:%X\n" % struct.unpack('I', instream.read(4))])

    outstream.writelines(["csgIdHomeNodeBNameNameLen:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["csgIdHomeNodeBNameNameInd:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    outstream.writelines(["csgIdHomeNodeBNameName:"])
    analysis_array_data_one_byte(instream, outstream, 48)

    outstream.writelines(["ucRac:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["nrLmmAccessTyp:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["homeNodebNameInd:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])

    outstream.writelines(["nrTaiPlmnIdUlMcc:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["nrTaiPlmnIdUlMNc:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["nrTaiTacTac:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["nrTaiTacTacCont:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["nrTaiTacTacCont1:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])

def analysis_gunas_mntn_log_CsDomaininf_inf_version0x02( instream, outstream):
    outstream.writelines(["csSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["attFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["csAttAllow:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["csRegSta:%X\n" % struct.unpack('B', instream.read(1))])

    outstream.writelines(["csAcRstrPagingRsp:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["csAcRstrReg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["csAcRstrNormSrv:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["csAcRstrEmergencySrv:%X\n" % struct.unpack('B', instream.read(1))])

    outstream.writelines(["t3212Len:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["csDrxLen:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["csRegBarToUnBarFlg:%X\n" % struct.unpack('I', instream.read(4))])

    outstream.writelines(["lastSuccLaiPlmnIdMcc:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["lastSuccLaiPlmnIdMnc:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["lastSuccLaiLac:"])
    analysis_array_data_one_byte(instream, outstream, 2)
    outstream.writelines(["lastSuccLaiCampPlmnNetRat:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["lastSuccLaiCampCnTyp:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["lastSuccLaiRac:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])

    outstream.writelines(["cmSrvStaMoCallSta:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["cmSrvStaMoSsSta:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["cmSrvStaMoLcsSta:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["cmSrvStaMtCsfbPagingTimerSta:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["cmSrvStaCellNotSptCsmoFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["cmSrvStaDelayNetSrchTimerSta:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["cmSrvStaEnableCsfbMtFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["cmSrvStaLastRedialTransActionFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["cmSrvStaCsfbEsrFailToGuPhaseInfTriggerPlmnSrchFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["cmSrvStaCsfbEsrFailToGuPhaseInfToGuPhase:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    outstream.writelines(["cmSrvStaCcReestFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["cmSrvStaIsCsfbMtFailTimerRunning:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])

    outstream.writelines(["csDamNoSrchFlg:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    outstream.writelines(["csSrvSta:%X\n" % struct.unpack('B', instream.read(1))])

    outstream.writelines(["laiInfInAcptMsgPlmnIdMcc:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["laiInfInAcptMsgPlmnIdMnc:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["laiInfInAcptMsgLac:"])
    analysis_array_data_one_byte(instream, outstream, 2)
    outstream.writelines(["laiInfInAcptMsgCampPlmnNetRat:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["laiInfInAcptMsgCampCnTyp:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["laiInfInAcptMsgRac:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])

    outstream.writelines(["lastLteSuccLaiPlmnIdMcc:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["lastLteSuccLaiPlmnIdMnc:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["lastLteSuccLaiLac:"])
    analysis_array_data_one_byte(instream, outstream, 2)
    outstream.writelines(["lastLteSuccLaiCampPlmnNetRat:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["lastLteSuccLaiCampCnTyp:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["lastLteSuccLaiRac:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])

def analysis_gunas_mntn_log_PsDomaininf_inf_version0x02( instream, outstream):
    outstream.writelines(["psSptFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psAttAllow:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psRegSta:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psSrvSta:%X\n" % struct.unpack('B', instream.read(1))])

    outstream.writelines(["psAcRstrPagingRsp:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psAcRstrReg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psAcRstrNormSrv:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psAcRstrEmergencySrv:%X\n" % struct.unpack('B', instream.read(1))])

    outstream.writelines(["psRegBarToUnBarFlg:%X\n" % struct.unpack('I', instream.read(4))])

    outstream.writelines(["lastSuccRaiLaiPlmnIdMcc:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["lastSuccRaiLaiPlmnIdMnc:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["lastSuccRaiLaiLac:"])
    analysis_array_data_one_byte(instream, outstream, 2)
    outstream.writelines(["lastSuccRaiLaiCampPlmnNetRat:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["lastSuccRaiLaiCampCnTyp:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["lastSuccRaiLaiRac:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    outstream.writelines(["lastSuccRaiRac:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])

    outstream.writelines(["psDomainDrxParaSplitPgCycleCode:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psDomainDrxParaUeUtranPsDrxLen:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psDomainDrxParaUeEutranPsDrxLen:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psDomainDrxParaWSysInfDrxLen:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psDomainDrxParaLSysInfDrxLen:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psDomainDrxParaSplitOnCcch:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psDomainDrxParaNonDrxTimer:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psDomainDrxParaPsRegContainDrx:%X\n" % struct.unpack('B', instream.read(1))])

    outstream.writelines(["nwImsVoCap:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psDamNoSrchFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psLocalDetachFlg:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])

    outstream.writelines(["gmmProcInfTyp:%X\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["gmmProcInfFlg:%X\n" % struct.unpack('H', instream.read(2))])

    outstream.writelines(["smProcFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["gprsSptChgFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psHandoverTimerSta:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psSceneSrvSta:%X\n" % struct.unpack('B', instream.read(1))])

    outstream.writelines(["psRelCause:%X\n" % struct.unpack('I', instream.read(4))])

    outstream.writelines(["raiInfInAcptMsgLaiPlmnIdMcc:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["raiInfInAcptMsgLaiPlmnIdMnc:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["raiInfInAcptMsgLaiLac:"])
    analysis_array_data_one_byte(instream, outstream, 2)
    outstream.writelines(["raiInfInAcptMsgLaiCampPlmnNetRat:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["raiInfInAcptMsgLaiCampCnTyp:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["raiInfInAcptMsgLaiRac:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])

    outstream.writelines(["raiInfInAcptMsgRac:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])

    outstream.writelines(["nrRegInfLastNrRegTaiPlmnIdUlMcc:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["nrRegInfLastNrRegTaiPlmnIdUlMnc:%X\n" % struct.unpack('I', instream.read(4))])

    outstream.writelines(["nrRegInfLastNrRegTaiTacTac:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["nrRegInfLastNrRegTaiTacTacCont:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["nrRegInfLastNrRegTaiTacTacCont1:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])

    outstream.writelines(["nrRegInfNrGutiInfValidFlg:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    outstream.writelines(["nrRegInfNrGutiInfGutiPlmnIdPlmnId:"])
    analysis_array_data_one_byte(instream, outstream, 3)
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    outstream.writelines(["nrRegInfNrGutiInfGutiAmfSetId:%X\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["nrRegInfNrGutiInfGutiAmfRegionId:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["nrRegInfNrGutiInfGutiAmfPointer:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["nrRegInfNrGutiInfGutiTmsi:%X\n" % struct.unpack('I', instream.read(4))])

    outstream.writelines(["nrRegInfNrRegSta:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])

    outstream.writelines(["lteGutiInfValidFlg:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])

    outstream.writelines(["lteGutiInfGutiPlmnIdPlmnId:"])
    analysis_array_data_one_byte(instream, outstream, 3)
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))

    outstream.writelines(["lteGutiInfGutiMmeGroupId:%X\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["lteGutiInfGutiMmeCode:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["lteGutiInfGutiMTmsi:%X\n" % struct.unpack('I', instream.read(4))])

def analysis_gunas_mntn_log_Bandinf_inf_version0x02( instream, outstream):
    outstream.writelines(["wcdmaBandBand:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["gsmBandBand:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["lteBandLteBand:"])
    analysis_array_data_four_byte(instream, outstream, 8)
    outstream.writelines(["cdmaBandBand:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["nrBandBand:"])
    analysis_array_data_four_byte(instream, outstream, 32)

def analysis_gunas_mntn_log_Net3GppRel_inf_version0x02( instream, outstream):
    outstream.writelines(["netMscRel:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["netSgsnRel:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["rel99Cnt:%X\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["rel98Cnt:%X\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["sgSnRel98Cnt:%X\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["sgSnRel99Cnt:%X\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["sgSnRel98Auth2GCnt:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["sgSnRel99Auth2GCnt:%X\n" % struct.unpack('B', instream.read(1))])

def analysis_gunas_mntn_log_ConnSta_inf_version0x02( instream, outstream):
    outstream.writelines(["csSigConnStaFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psSigConnStaFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psTbfStaFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["rrcStaFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["csSrvConnStaFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["csSrvBufferFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psSrvBufferFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["pdpStaFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["epsSigConnStaFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["epsSrvConnStaFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["emergencySrvFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["psTcSrvFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["emcPdpStaFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["csfbSrvSta:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["srvccCallFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["nrConnSta:%X\n" % struct.unpack('B', instream.read(1))])

def analysis_gunas_mntn_log_EpsDomaininf_inf_version0x02( instream, outstream):
    outstream.writelines(["t3412Sta:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["t3423Sta:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["t3402Sta:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["t3346Sta:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    outstream.writelines(["nwEmcBS:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["additionUpdRsltInf:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["epsRegSta:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["isRelCauseCsfbHighPrio:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["epsEmcAttFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["nwImsVoCap:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["t3402Len:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["s1ModeLowLayerFailFlg:%X\n" % struct.unpack('I', instream.read(4))])

def analysis_gunas_mntn_log_PsBearerContext_inf_version0x02( instream, outstream):
    ulLooper        = 0

    while ulLooper < 11:
        outstream.writelines(["\nPsBearerContext%d:\n" % ulLooper])
        outstream.writelines(["psBearerSta:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["psBearerIsrFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["psActPending:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["psDeactPending:%X\n" % struct.unpack('B', instream.read(1))])
        ulLooper = ulLooper + 1

def analysis_gunas_mntn_log_ImsDomaininf_inf_version0x02( instream, outstream):
    outstream.writelines(["imsVoiceAvail:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsNormRegSta:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsNormCallExistFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsVoiceCallExistFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsVideoCallExistFlg:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    outstream.writelines(["persistentBearerSta:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsEmcCallExistFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsRegDomain:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsSmsExistFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsSsExistFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsUnavailableTyp:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["imsEmcDomain:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    outstream.writelines(["imsCurPlmnIdMcc:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["imsCurPlmnIdMnc:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["imsRegResult:%X\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["sipStaCode:%X\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["isPermForbFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["curRatTyp:%X\n" % struct.unpack('B', instream.read(1))])

def analysis_gunas_mntn_log_NoRfinf_inf_version0x02( instream, outstream):
    outstream.writelines(["rfAvailFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["ratTyp:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])

    outstream.writelines(["rrmResInfMmSndLuRegRrmResFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["rrmResInfGmmSndAttRegRrmResFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["rrmResInfGmmSndRauRegRrmResFlg:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])

    outstream.writelines(["noRfCauseInfMmNoRfCauseFlg:%X\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["noRfCauseInfGmmNoRfCauseFlg:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])

def analysis_gunas_mntn_log_OrigRejCause_inf_version0x02( instream, outstream):
    outstream.writelines(["origRejCause:%X\n" % struct.unpack('B', instream.read(1))])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    (ucrsv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv:%X\n" % ucrsv])
    outstream.writelines(["usPsOrigRejCause:%X\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["usCsOrigRejCause:%X\n" % struct.unpack('H', instream.read(2))])

def analysis_gunas_modem0_dump_inf( instream, fileOffset, outstream, ulMsgIndex):
    ulLooper        = 0
    ulEndTick       = 0
    ulbeginTick     = 0

    outstream.writelines(["%s %s %s %s %s %s %s %s %s %s\n" % ("receiveTime", "sendPid", "usReceivePid","ulMsgId", "mmcFsmId","ucState","gmmState","mmState","regmFsmId","regmState","utranCtrlFsmId","ucState")])
    while ulLooper < MACRO_NAS_MML_MAX_LOG_EVENT_STATE_NUM:
        ulLooperIndex = ( ulLooper + ulMsgIndex) % MACRO_NAS_MML_MAX_LOG_EVENT_STATE_NUM
        fileLocalOffset = fileOffset + ulLooperIndex * MACRO_NAS_MNTN_LOG_MSG_INFO_SIZE
        analysis_gunas_mntn_per_rec_msg_inf( instream, fileLocalOffset, outstream)
        ulLooper = ulLooper + 1

    global modem_index
    if modem_index == 2:
            return
#       1437226410 = 0x55aa55aa find end tick
    while ulEndTick != 1437226410:
            (ulEndTick,)       = struct.unpack('I', instream.read(4))
    print ("mscc End tag is %s" % (ulEndTick))

#       1437226410 = 0x55aa55aa find Begin tick
    while ulbeginTick != 1437226410:
            (ulbeginTick,)       = struct.unpack('I', instream.read(4))
    print ("mscc begin tag is %s" % (ulbeginTick))

    global GLOBAL_Offset
    GLOBAL_Offset = instream.tell()
    print ("gLOBALOffset is %s" % (GLOBAL_Offset))


def analysis_gunas_modem0_dump_inf_version0x02( instream, fileOffset, outstream, ulMsgIndex):
    ulLooper        = 0
    ulEndTick       = 0
    ulbeginTick     = 0


    outstream.writelines(["%s %s %s %s %s %s %s %s %s %s %s %s %s\n" % ("index", "Tick", "SendPid", "ReceivePid","ulMsgId", "MmcFsmId","MmcState","GmmState","MmState","RegmFsmId","RegmState","UtranCtrlFsmId","UtranCtrlState")])
    while ulLooper < MACRO_NAS_MML_MAX_LOG_EVENT_STATE_NUM:
        ulLooperIndex = ( ulLooper + ulMsgIndex) % MACRO_NAS_MML_MAX_LOG_EVENT_STATE_NUM
        fileLocalOffset = fileOffset + ulLooperIndex * MACRO_NAS_MNTN_LOG_MSG_INFO_SIZE_HIONE
        analysis_gunas_mntn_per_rec_msg_inf_version0x02( instream, fileLocalOffset, outstream, (ulLooper + 1))
        ulLooper = ulLooper + 1

    outstream.writelines(["\n%s%s\n" % ("exitTime", "latestIndex")])
    analysis_gunas_mntn_log_event_state_other_inf_version0x02( instream, outstream)

    outstream.writelines(["\n%s\n" % ("SimSta:")])
    analysis_gunas_mntn_log_sim_sta_inf_version0x02( instream, outstream)

    outstream.writelines(["\n%s\n" % ("MsIdentity:")])
    analysis_gunas_mntn_log_ms_identity_inf_version0x02( instream, outstream)

    outstream.writelines(["\n%s\n" % ("PsSecurity:")])
    analysis_gunas_mntn_log_ps_security_inf_version0x02( instream, outstream)

    outstream.writelines(["\n%s\n" % ("CsSecurity:")])
    analysis_gunas_mntn_log_cs_security_inf_version0x02( instream, outstream)

    outstream.writelines(["\n%s\n" % ("SimNativeContent:")])
    analysis_gunas_mntn_log_sim_native_content_inf_version0x02( instream, outstream)

    (CallMode,)             = struct.unpack('B', instream.read(1))
    strCallMode             = '%X'% CallMode
    outstream.writelines(["\nCallMode:%s\n" % (strCallMode)])
    (ucrsv1,)           = struct.unpack('B', instream.read(1))
    (ucrsv2,)           = struct.unpack('B', instream.read(1))
    (ucrsv3,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["ucrsv1:%X\n" % (ucrsv1)])
    outstream.writelines(["ucrsv1:%X\n" % (ucrsv2)])
    outstream.writelines(["ucrsv1:%X\n" % (ucrsv3)])

    outstream.writelines(["\n%s\n" % ("Ms3GppRel:")])
    analysis_gunas_mntn_log_Ms3GppRel_inf_version0x02( instream, outstream)

    outstream.writelines(["\n%s\n" % ("MsCap:")])
    analysis_gunas_mntn_log_MsCap_inf_version0x02( instream, outstream)

    outstream.writelines(["\n%s\n" % ("MsSysCfgInf:")])
    analysis_gunas_mntn_log_MsSysCfgInf_inf_version0x02( instream, outstream)

    outstream.writelines(["\n%s\n" % ("CampPlmnInf:")])
    analysis_gunas_mntn_log_CampPlmninf_inf_version0x02( instream, outstream)

    outstream.writelines(["\n%s\n" % ("CsDomainInf:")])
    analysis_gunas_mntn_log_CsDomaininf_inf_version0x02( instream, outstream)

    outstream.writelines(["\n%s\n" % ("PsDomaininf:")])
    analysis_gunas_mntn_log_PsDomaininf_inf_version0x02( instream, outstream)

    outstream.writelines(["\n%s\n" % ("BandInf:")])
    analysis_gunas_mntn_log_Bandinf_inf_version0x02( instream, outstream)

    outstream.writelines(["\n%s\n" % ("Net3GppRel:")])
    analysis_gunas_mntn_log_Net3GppRel_inf_version0x02( instream, outstream)

    outstream.writelines(["\n%s\n" % ("ConnSta:")])
    analysis_gunas_mntn_log_ConnSta_inf_version0x02( instream, outstream)

    outstream.writelines(["\n%s\n" % ("EpsDomainInf:")])
    analysis_gunas_mntn_log_EpsDomaininf_inf_version0x02( instream, outstream)

    outstream.writelines(["\n%s\n" % ("PsBearerContext:")])
    analysis_gunas_mntn_log_PsBearerContext_inf_version0x02( instream, outstream)

    outstream.writelines(["\n%s\n" % ("ImsDomainInf:")])
    analysis_gunas_mntn_log_ImsDomaininf_inf_version0x02( instream, outstream)

    outstream.writelines(["\n%s\n" % ("NoRfInf:")])
    analysis_gunas_mntn_log_NoRfinf_inf_version0x02( instream, outstream)

    outstream.writelines(["\n%s\n" % ("OrigRejCause:")])
    analysis_gunas_mntn_log_OrigRejCause_inf_version0x02( instream, outstream)


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


def analysis_gunas_modemX_event_state_list_dump_inf( instream, fileOffset, outstream):
    ulLooperTest = 0

    #outstream.writelines(["\n analysisGunasModemXEventStateListDumpinf enter! %d\n" % (fileOffset)])
    instream.seek(fileOffset)
    (ulBeginTick,)       = struct.unpack('I', instream.read(4))
    strBeginTick         = '%x'% ulBeginTick
    print ("begin tag is %s" % (strBeginTick))

    #outstream.writelines(["strModem0LogBeginflg         %s\n" % ( strBeginTick )])

    fileOffset = fileOffset + 4

    #outstream.writelines(["\n analysisGunasModemXEventStateListDumpinf enter! %d\n" % (fileOffset)])

    # gunas modem0 #
#       Old Version begin is 0x55aa55aa
    global Global_Version
    if ulBeginTick == 1437226410:
        Global_Version = 0x01
        analysis_gunas_modem0_dump_inf(instream, fileOffset, outstream, ulLooperTest)

#       New Version begin is 0x55bb55bb
    if ulBeginTick == 1438340539:
        Global_Version = 0x02
        analysis_gunas_modem0_dump_inf_version0x02(instream, fileOffset, outstream, ulLooperTest)

    return True

def analysis_gunas_dump_info( infile, offset, outfile):
    instream = infile
    outstream  = outfile
    fileOffset = eval(offset)

    global g_offset
    g_offset = eval(offset)

    #outstream.writelines(["\n WUMAI:GUNASDUMPANALYSIS20160122VERSION1.0 \n"])

    # gunas modem0 PARSE EVENT STATE #
    outstream.writelines(["\n modem0:analysisGunasDumpinf begin!\n"])
    global modem_index
    global GLOBAL_Offset
    modem_index = 0
    analysis_gunas_modemX_event_state_list_dump_inf( instream, fileOffset, outstream )
    outstream.writelines(["\n modem0:analysisGunasDumpinf end!\n"])


    # gunas modem1 PARSE EVENT STATE #
    outstream.writelines(["\n modem1:analysisGunasDumpinf begin!\n"])
#        fileOffset = fileOffset + MACRO_MODEM0_ADDR_LENGTH
#        global GLOBAL_Offset
    fileOffset = GLOBAL_Offset
#        global modem_index
    modem_index = 1
    analysis_gunas_modemX_event_state_list_dump_inf( instream, fileOffset, outstream )
    outstream.writelines(["\n modem1:analysisGunasDumpinf end!\n"])


    # gunas modem1 PARSE EVENT STATE #
    outstream.writelines(["\n modem2:analysisGunasDumpinf begin!\n"])
#        fileOffset = fileOffset + MACRO_MODEM0_ADDR_LENGTH
#        global GLOBAL_Offset
    fileOffset = GLOBAL_Offset
#        global modem_index
    modem_index = 2
    analysis_gunas_modemX_event_state_list_dump_inf( instream, fileOffset, outstream )
    outstream.writelines(["\n modem2:analysisGunasDumpinf end!\n"])
    return True


########################################################################################
def entry_0x2200006(infile, field, offset, len, version, mode, outfile):
    ########check parameter start#############
    if not field == '0x2200006':
        print ("hidis field is %s" % (field))
        print ("current field is 0x2200006")
        return error['ERR_CHECK_FIELD']
    elif not version == '0x000b':
        print ("hidis version is %s" % (version))
        print ("current version is 0x000b")
        return error['ERR_CHECK_VERSION']
    #check parameter end #
    ret = analysis_gunas_dump_info( infile, offset, outfile)

    #c = msvcrt.getch()
    return 0


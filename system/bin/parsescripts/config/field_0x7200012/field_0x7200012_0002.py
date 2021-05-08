#!/usr/bin/env python
# coding: utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   analysis mscc dump bin
author          :   z00382546
modify  record  :   2019-05-14 create file
"""

import struct
import os
import sys
import string
from nrnas_pid import *
from nrnas_msg import *

MACRO_NRNAS_MAX_LOG_NRMM_MSG_STATE_NUM = 70
MACRO_NRNAS_MAX_LOG_NRCM_MSG_STATE_NUM  = 70
MACRO_NRNAS_MAX_LOG_NREAP_MSG_STATE_NUM = 70
MACRO_NAS_NRMM_MAX_EPLMN_NUM = 16
MACRO_NAS_NRSM_MAX_PDU_SESSION_CTX_CO_EXIST_NUM = 6
MACRO_NRNAS_EAP_MAX_ENTITY_NUM = 8

def analysis_nrmm_mntn_save_exc_cm_fsm_ctx(instream, fileOffset, outstream):
    instream.seek(fileOffset)

    outstream.writelines(["\nCM FSM CTX\n"])
    outstream.writelines(["mdoem id:%d\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["access type id:%d\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["CmSuspended:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["RegStatus:%d (0:Reg 1:Dereg)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["IsCmPowerOn:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["AbortSrvFlag:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["IsSrSentInConn:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["SrvType:%d (0:Sign 1:Data 2:mt service 3:emc 4:emc fallback 5:high prior access)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["SrvAttemptCnt:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Upu Ack:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])


def analysis_nrmm_mntn_save_exc_reg_fsm_ctx(instream, fileOffset, outstream):
    instream.seek(fileOffset)

    outstream.writelines(["\nREG FSM CTX\n"])
    outstream.writelines(["mdoem id:%d\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["access type id:%d\n" % struct.unpack('H', instream.read(2))])
    fileOffset = fileOffset + 4
    #NRNAS_NRMM_MNTN_SAVE_EXC_REG_CTRL_INFO_STRU Begin
    outstream.writelines(["\nReg Type:%d (1:initial 2:mobility 3:periodic 4:5GS EMC)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["PeriodicRegDelayFlag:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["RegAttemptCnt:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["IsRegInitInIdleMode:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["FollowOnFlag:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["UplinkDataStatusSetFlag:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    #NRNAS_NRMM_MNTN_SAVE_EXC_REG_CTRL_INFO_STRU END

    fileOffset = fileOffset + 8
    instream.seek(fileOffset)
    #NRNAS_NRMM_MNTN_SAVE_EXC_DEREG_CTRL_INFO_STRU Begin
    outstream.writelines(["\nDereg Type:%d (0:dereg 1:power off)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["DeregAttemptCnt:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["TaiChgInDereg:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    #NRNAS_NRMM_MNTN_SAVE_EXC_DEREG_CTRL_INFO_STRU END

    fileOffset = fileOffset + 4
    instream.seek(fileOffset)
    #NRNAS_NRMM_MNTN_SAVE_EXC_REGM_RELATED_INFO_STRU Begin
    outstream.writelines(["\nUserRegReqFlag:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["UserDeregReqFlag:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    #NRNAS_NRMM_MNTN_SAVE_EXC_REGM_RELATED_INFO_STRU END

    fileOffset = fileOffset + 4
    instream.seek(fileOffset)
    #NRNAS_NRMM_MNTN_SAVE_EXC_INTERSYS_INFO_STRU Begin
    outstream.writelines(["\nIsRatSuspended:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["InterSysResumeType:%d (0:RESEL 1:HO 2:REDIR 3:RESEL REVERVER 4:REDIR REVERSE 5:HO REVERSE)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    #NRNAS_NRMM_MNTN_SAVE_EXC_INTERSYS_INFO_STRU END


def analysis_nrmm_mntn_save_exc_access_type_inist_ctx(instream, fileOffset, outstream):
    instream.seek(fileOffset)
    #NRNAS_NRMM_MNTN_SAVE_EXC_UE_INFO_CTX_STRU Begin
    #NRNAS_MNTN_SAVE_EXC_MMC_NRMM_RAT_PRIO_STRU Begin
    outstream.writelines(["\nRat Nnm:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["0:GSM 1:WCDMA 2:LTE 3:CDMA1X 4:HRPD 5:NR\n"])
    count = 0
    while count < 6:
            outstream.writelines(["Rat:%d\n" % struct.unpack('B', instream.read(1))])
            count = count + 1
    #NRNAS_MNTN_SAVE_EXC_MMC_NRMM_RAT_PRIO_STRU End

    #NRNAS_NRMM_MNTN_SAVE_EXC_SEC_INFO_STRU Begin
    outstream.writelines(["\nSec Disable:%d (1:support palin text and null algo 2:not support)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv1:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv2:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv3:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["5gEaAlgBitMap:0x%x\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["5gIaAlgBitMap:0x%x\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["EeaAlgBitMap:0x%x\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["EiaAlgBitMap:0x%x\n" % struct.unpack('B', instream.read(1))])
    #NRNAS_NRMM_MNTN_SAVE_EXC_SEC_INFO_STRU End

    #NRNAS_NRMM_MNTN_SAVE_EXC_DISABLE_LTE_INFO_STRU Begin
    outstream.writelines(["\nDisable Lte:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv1:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv2:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv3:%d\n" % struct.unpack('B', instream.read(1))])
    #NRNAS_NRMM_MNTN_SAVE_EXC_DISABLE_LTE_INFO_STRU End

    #NRNAS_NRMM_MNTN_SAVE_EXC_5GMM_CAP_CFG_INFO_STRU Begin
    outstream.writelines(["\nSms Over Nas:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Mico Mode:%d (1:active 0:inactive)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    #NRNAS_NRMM_MNTN_SAVE_EXC_5GMM_CAP_CFG_INFO_STRU End

    #NRNAS_NRMM_MNTN_SAVE_EXC_CUSTON_CFG_INFO_STRU Begin
    outstream.writelines(["\nInit Reg with follow on:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["AllowAreaUpdateForbTaiListFlag:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["ucDrxValue:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["RelPsSignalConFlg:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["RelPsSignalConAbnormalScene:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["T3540Len:%d\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["T3540LenAbnormalScene:%d\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["DataReqRetryCfg-Enable:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["DataReqRetryCfg-Times:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    #NRNAS_NRMM_MNTN_SAVE_EXC_CUSTON_CFG_INFO_STRU End

    outstream.writelines(["\nDual Reg Supported:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Last Reg Sys Mode:%d (0:N1 Mode 1:S1 Mode 2:Iu or A/Gb Mode)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    #NRNAS_NRMM_MNTN_SAVE_EXC_UE_INFO_CTX_STRU End

    fileOffset = fileOffset + 48
    instream.seek(fileOffset)
    #NRNAS_NRMM_MNTN_SAVE_EXC_REG_INFO_CTX_STRU Begin
    #NRNAS_NRMM_MNTN_SAVE_EXC_5GS_NW_FEATURE_STRU Begin
    outstream.writelines(["\n5GS nw feature-Len:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Cap Byte:0x%x (0:ImsVoPs-3GPP 1:ImsVoPs-Non3GPP 2:Emc-3GPP 3:Emc-Non3GPP 4:EMF-NR 5:EMF-LTE 6:IWKN26 7:MPSI)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Cap Byte:0x%x (0:EMCN3 1:MSCI 2-7:spare)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    #NRNAS_NRMM_MNTN_SAVE_EXC_5GS_NW_FEATURE_STRU End

    #NRNAS_NRMM_MNTN_SAVE_EXC_PLMN_LIST_STRU Begin
    outstream.writelines(["\nEPLMN Num:%d\n" % struct.unpack('I', instream.read(4))])
    count = 0
    while count < MACRO_NAS_NRMM_MAX_EPLMN_NUM:
            outstream.writelines(["Plmn%d:" % (count)])
            outstream.writelines(["0x%x " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["0x%x " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["0x%x " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
            count = count + 1
    #NRNAS_NRMM_MNTN_SAVE_EXC_PLMN_LIST_STRU End

    #NRNAS_NRMM_MNTN_SAVE_EXC_MICO_INDICATION_STRU Begin
    outstream.writelines(["\nMico Indication:\n"])
    outstream.writelines(["Cap Byte:0x%x (0:Raai 1-7:spare)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    #NRNAS_NRMM_MNTN_SAVE_EXC_MICO_INDICATION_STRU End

    #NRNAS_NRMM_MNTN_SAVE_EXC_T3502_CTRL_STRU Begin
    outstream.writelines(["\nT3502 Ctrl:\n"])
    outstream.writelines(["\nPLMN Num:%d\n" % struct.unpack('I', instream.read(4))])
    count = 0
    while count < MACRO_NAS_NRMM_MAX_EPLMN_NUM:
            outstream.writelines(["Plmn%d:" % (count)])
            outstream.writelines(["0x%x " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["0x%x " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["0x%x " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
            count = count + 1
    outstream.writelines(["IsT3502RcvRegRej:%d\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["T3502TimerLen:%d (0:deactive)\n" % struct.unpack('I', instream.read(4))])
    #NRNAS_NRMM_MNTN_SAVE_EXC_T3502_CTRL_STRU End

    outstream.writelines(["\nsms allowed:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])

    outstream.writelines(["\nT3512TiLen:%d\n" % struct.unpack('I', instream.read(4))])
    #NRNAS_NRMM_MNTN_SAVE_EXC_REG_INFO_CTX_STRU End

    fileOffset = fileOffset + 160
    instream.seek(fileOffset)
    #NRNAS_NRMM_MNTN_SAVE_EXC_SRV_INFO_CTX_STRU Begin
    #NAS_NRMM_MNTN_SAVE_EXC_NRSM_BUFF_MSG_INFO_STRU Begin
    outstream.writelines(["\nNrsm Msg Buffer Num:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["IsNrsmEstReqBuffered:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    #NAS_NRMM_MNTN_SAVE_EXC_NRSM_BUFF_MSG_INFO_STRU End

    #NAS_NRMM_MNTN_SAVE_EXC_IMS_SRV_RESULT_INFO_STRU Begin
    outstream.writelines(["\nIms Info:\n"])
    outstream.writelines(["IsImsaEmfbPending:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["ReqPduNum:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["ProcessedReqPduNum:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    count = 0
    while count < 3:
            outstream.writelines(["ims srv rslt%d:" % (count)])
            outstream.writelines(["Pdu Session Id:%d " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Rslt:%d " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Rsv:0x%x" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
            count = count + 1
    #NAS_NRMM_MNTN_SAVE_EXC_IMS_SRV_RESULT_INFO_STRU End

    #NAS_NRMM_MNTN_SAVE_EXC_SMS_INFO_STRU Begin
    outstream.writelines(["\nSmsOverNasEstReqFlg:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["SmsOverNasEventFlg:0x%x (bit0;Mo sms  bit1:Mt Sms)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    #NAS_NRMM_MNTN_SAVE_EXC_SMS_INFO_STRU End
    #NRNAS_NRMM_MNTN_SAVE_EXC_SRV_INFO_CTX_STRU End

    fileOffset = fileOffset + 24
    instream.seek(fileOffset)
    #NRNAS_NRMM_MNTN_SAVE_EXC_MAIN_CTRL_CTX_STRU Begin
    outstream.writelines(["\nMain Ctrl:\n"])
    outstream.writelines(["OpId:%d\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["Air Msg Type:0x%x (0x00:NULL 0x01:REG REQ 0x02:CONF UPDATE CMPL 0x04:DEREG REQ 0x08:REG CMPL 0x10:DEREG ACC)\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["Ooc Flag:0x%x\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    #NRNAS_NRMM_MNTN_SAVE_EXC_MAIN_CTRL_CTX_STRU End

    fileOffset = fileOffset + 8
    instream.seek(fileOffset)
    #NRNAS_NRMM_MNTN_SAVE_EXC_CONN_INFO_CTX_STRU Begin
    outstream.writelines(["\nConnection Mode:%d (0:IDLE 1:CONNECTED 2:CONNECTED WITH RRC INACTIVE 3:ESTING 4:RELEASING)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["CurDataCnfRetryTimes:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    #NRNAS_NRMM_MNTN_SAVE_EXC_CONN_INFO_CTX_STRU End

    fileOffset = fileOffset + 4
    instream.seek(fileOffset)
    #NRNAS_NRMM_MNTN_SAVE_EXC_NWS_INFO_CTX_STRU Begin
    outstream.writelines(["\nManualSearchFlag:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    #NRNAS_NRMM_MNTN_SAVE_EXC_NWS_INFO_CTX_STRU End

    fileOffset = fileOffset + 4
    instream.seek(fileOffset)
    #NAS_NRMM_MntnSaveUpuInfo Begin
    outstream.writelines(["upuAck:0x%x\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["upuReg:0x%x\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    #NAS_NRMM_MntnSaveUpuInfo End

    fileOffset = fileOffset + 4
    instream.seek(fileOffset)
    #NAS_NRMM_MntnAsCtrlInfo Begin
    outstream.writelines(["asType:0x%x\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv:0x%x\n" % struct.unpack('B', instream.read(1))])
    #NAS_NRMM_MntnAsCtrlInfo End

    #NRNAS_NRMM_MNTN_SAVE_EXC_TIMER_INFO_CTX_STRU Begin
    outstream.writelines(["\nRuning Timer:\n"])
    count = 0
    while count < 10:
            outstream.writelines(["Timer%d:\n" % (count)])
            outstream.writelines(["HTimer:0x%x\n" % struct.unpack('I', instream.read(4))])
            outstream.writelines(["Timer Id:0x%x\n" % struct.unpack('I', instream.read(4))])
            outstream.writelines(["Timer Para:0x%x\n" % struct.unpack('I', instream.read(4))])
            outstream.writelines(["Timer Status:0x%x (0:Stop 1:Runing)\n" % struct.unpack('I', instream.read(4))])
            count = count + 1
    #NRNAS_NRMM_MNTN_SAVE_EXC_TIMER_INFO_CTX_STRU End


def analysis_nrmm_mntn_save_exc_log(instream, fileOffset, outstream):
    instream.seek(fileOffset)

    (startTag,)      = struct.unpack('I', instream.read(4))
    startTagStr      = '0x%x' % startTag
    print("Nrmm Begin tag is %s\n" % (startTagStr))
    fileOffset = fileOffset + 4

    outstream.writelines(["--Nrmm Mntn Dump Begin--\n"])
    #NRNAS_NRMM_MNTN_SAVE_EXC_MULTI_ACCESS_SHARE_CTX_STRU Begin
    outstream.writelines(["\nUsim State:%d (0:valid 1:invalid)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv1:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv2:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv3:%d\n" % struct.unpack('B', instream.read(1))])
    fileOffset = fileOffset + 4
    #NRNAS_NRMM_MNTN_SAVE_EXC_MULTI_ACCESS_SHARE_CTX_STRU End

    #NRNAS_NRMM_MNTN_SAVE_EXC_ACCESS_TYPE_INIST_CTX_STRU Begin
    #暂时只支持3GPP
    analysis_nrmm_mntn_save_exc_access_type_inist_ctx(instream, fileOffset, outstream)
    fileOffset = fileOffset + 408*1
    #NRNAS_NRMM_MNTN_SAVE_EXC_ACCESS_TYPE_INIST_CTX_STRU End

    #NRNAS_NRMM_MNTN_SAVE_EXC_REG_FSM_CTX_STRU Begin
    #暂时只支持GPP
    analysis_nrmm_mntn_save_exc_reg_fsm_ctx(instream, fileOffset, outstream)
    fileOffset = fileOffset + 24*1
    #NRNAS_NRMM_MNTN_SAVE_EXC_REG_FSM_CTX_STRU End

    #NRNAS_NRMM_MNTN_SAVE_EXC_CM_FSM_CTX_STRU Begin
    #暂时只支持GPP
    analysis_nrmm_mntn_save_exc_cm_fsm_ctx(instream, fileOffset, outstream)
    fileOffset = fileOffset + 16*1
    #NRNAS_NRMM_MNTN_SAVE_EXC_CM_FSM_CTX_STRU End

    outstream.writelines(["--Nrmm Mntn Dump End--\n"])


def analysis_nrsm_mntn_save_exc_pdu_session_ctx_log(instream, fileLocalOffset, outstream, ulLooper):
    instream.seek(fileLocalOffset)
    outstream.writelines(["Pdu Session Used Flag:%d\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["Pdu Session State:%d (0:inactive 1:active pending 2:active 3:inactive pending 4:modify pending 5:suspend 6: resume pending)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv1:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv2:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv3:%d\n" % struct.unpack('B', instream.read(1))])

    #NRNAS_NRSM_MNTN_SAVE_EXC_STATE_INFO_STRU Begin
    outstream.writelines(["Cap Byte:0x%x (0:ssc mode 1:snssai 2:old pdu session id 3:Pcscf Discovery 4:im cm signal flg 5:max support pf num 7-31:spare)\n" % struct.unpack('I', instream.read(4))])

    outstream.writelines(["PsCallId:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Cid:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Pti:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["pdu session id:%d (0~15)\n" % struct.unpack('B', instream.read(1))])

    outstream.writelines(["old pdu session id:%d (0~15)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["pdu session type:%d (1:IPV4 2:IPV6 3:IPV4V6 4:UNSTRUCT 5:ETHERNET)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["ssc mode:%d (1:ssc mode 1 2:ssc mode 2 3:ssc mode 3)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["pdu session request type:%d (1:initial 2:handover)\n" % struct.unpack('B', instream.read(1))])

    outstream.writelines(["Emergency ind:%d (0:not emc 1:emc)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Pcscf Discovery:%d (0:not influenced 1:through nas sig 2:through dhcp)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Ims Cn Signal Flg:%d (0:not while ims cn sig only 1:while ims cn sig only)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["always on ind:%d (0:not always on ind 1:always on ind)\n" % struct.unpack('B', instream.read(1))])

    outstream.writelines(["Max Support Pf Num:%d\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["Mtu For Ims Dnn Flag:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Mtu For other Dnn Flag:%d\n" % struct.unpack('B', instream.read(1))])

    outstream.writelines(["acc type:%d (0:3gpp)\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["opid:0x%x\n" % struct.unpack('H', instream.read(2))])

    outstream.writelines(["reflect qos ind:%d (0:not support 1:support)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["multi home ind:%d (0:not support 1:support)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv1:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Rsv2:%d\n" % struct.unpack('B', instream.read(1))])
    #NRNAS_NRSM_MNTN_SAVE_EXC_STATE_INFO_STRU End

def analysis_nrsm_mntn_save_exc_log(instream, fileOffset, outstream):
    instream.seek(fileOffset)

    ulLooper        = 0

    (startTag,)      = struct.unpack('I', instream.read(4))
    startTagStr      = '0x%x' % startTag
    print("Nrsm Begin tag is %s\n" % (startTagStr))
    fileOffset = fileOffset + 4
    outstream.writelines(["--Nrsm Mntn Dump Begin--\n"])
    #NRNAS_NRSM_MNTN_SAVE_EXC_PDU_SESSION_CTX_STRU Begin
    #NRNAS_NRSM_MNTN_SAVE_EXC_PDU_SESSION_CTX_STRU的大小为36
    while ulLooper < MACRO_NAS_NRSM_MAX_PDU_SESSION_CTX_CO_EXIST_NUM:
        outstream.writelines(["\npdu session ctx index: %d\n" % ulLooper])
        analysis_nrsm_mntn_save_exc_pdu_session_ctx_log(instream, 36*ulLooper+fileOffset, outstream, ulLooper)
        ulLooper = ulLooper + 1
    #NRNAS_NRSM_MNTN_SAVE_EXC_PDU_SESSION_CTX_STRU End
    fileOffset = fileOffset + 216

    outstream.writelines(["opid:0x%x\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["cur max pti:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["start ind flg:%d (0:null 1:3gpp 2:no 3gpp)\n" % struct.unpack('B', instream.read(1))])

    outstream.writelines(["nr reg status:%d (0:normal reg 1:emc reg 2:dereg)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["IWKN26:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["old IWKN26:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["nr Active Flag(0:suspend 1:active):%d\n" % struct.unpack('B', instream.read(1))])

    #NRNAS_MNTN_SAVE_EXC_PS_NR_PLMN_ID_STRU Begin
    outstream.writelines(["\n%-15s\n" % ("NrPlmnInfo:")])
    (plmn,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["plmn:0x%X\n" % plmn])
    (plmn,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["plmn:0x%X\n" % plmn])
    (plmn,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["plmn:0x%X\n" % plmn])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    #NRNAS_MNTN_SAVE_EXC_PS_NR_PLMN_ID_STRU End

    outstream.writelines(["--Nrsm Mntn Dump End--\n"])

def analysis_nreap_mntn_save_exc_eap_entity_ctx_log(instream, fileLocalOffset, outstream, ulLooper):
    instream.seek(fileLocalOffset)
    outstream.writelines(["eap entity Used Flag:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["eap entity id:%d (0-1:NRMM 2-16:NRSM)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Auth cnf Flag:%d (0:null 1:wait auth cnf flg)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Resv:%d\n" % struct.unpack('B', instream.read(1))])

    outstream.writelines(["Auth Req Pid:0x%X\n" % struct.unpack('I', instream.read(4))])

    #NRNAS_NREAP_MNTN_SAVE_EXC_AKA_DATA_INFO_STRU Begin
    outstream.writelines(["\n%-15s\n" % ("aka data info:")])
    outstream.writelines(["Eap Method:%d (0:aka 1:aka prime)\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["Eap aka state:%d (0:continue 1:result success 2:success 3:failure)\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["Reauth:%d (0:full-auth 1:re-auth)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["KdfNegotiation:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["NumNotification:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["NumIdReq:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["PrevId:%d\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["ResultInd:%d\n" % struct.unpack('B', instream.read(1))])
    (Reserved,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["Reserved:0x%X\n" % Reserved])
    (Reserved,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["Reserved:0x%X\n" % Reserved])
    (Reserved,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["Reserved:0x%X\n" % Reserved])
    outstream.writelines(["CounterTooSmall:%d\n" % struct.unpack('H', instream.read(2))])
    #NRNAS_NREAP_MNTN_SAVE_EXC_AKA_DATA_INFO_STRU End

    #NRNAS_NREAP_MNTN_SAVE_EXC_CTRL_INFO_STRU Begin
    outstream.writelines(["\n%-15s\n" % ("eap ctrl info:")])
    outstream.writelines(["EapLastReqID:%d\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["Req Method:%d (1:identity 2:notify 3:NAK 23:AKA 50:AKA PRIME 254:EXPAND NAK)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Request ID:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["select Method:%d (1:identity 2:notify 3:NAK 23:AKA 50:AKA PRIME 254:EXPAND NAK)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Inter Type:%d (0:AKA 1:AKA PRIME)\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Eap Peer State:%d (0:idle 1:authenticating 2:notifying 3:closing 4:closed)\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["Local Result:%d\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["Remote Result:%d\n" % struct.unpack('I', instream.read(4))])
    outstream.writelines(["Resp Pkt Len:%d\n" % struct.unpack('H', instream.read(2))])
    outstream.writelines(["Last Rsp Use able:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["Reserve:%d\n" % struct.unpack('B', instream.read(1))])
    #NRNAS_NREAP_MNTN_SAVE_EXC_CTRL_INFO_STRU End

def analysis_nreap_mntn_save_exc_log(instream, fileOffset, outstream):
    instream.seek(fileOffset)

    ulLooper        = 0

    (startTag,)      = struct.unpack('I', instream.read(4))
    startTagStr      = '0x%x' % startTag
    print("Nreap Begin tag is %s\n" % (startTagStr))
    outstream.writelines(["--Nreap Mntn Dump Begin--\n"])
    fileOffset = fileOffset + 4
    #NRNAS_NREAP_MNTN_SAVE_EXC_ENTITY_CTX_STRU Begin
    #NRNAS_NREAP_MNTN_SAVE_EXC_ENTITY_CTX_STRU的大小为44
    while ulLooper < MACRO_NRNAS_EAP_MAX_ENTITY_NUM:
        outstream.writelines(["\nEAP entity ctx index: %d\n" % ulLooper])
        analysis_nreap_mntn_save_exc_eap_entity_ctx_log(instream, 44*ulLooper+fileOffset, outstream, ulLooper)
        ulLooper = ulLooper + 1
    #NRNAS_NREAP_MNTN_SAVE_EXC_ENTITY_CTX_STRU End

    #NRNAS_MNTN_SAVE_EXC_PS_NR_PLMN_ID_STRU Begin
    outstream.writelines(["\n%-15s\n" % ("NrPlmnInfo:")])
    (plmn,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["plmn:0x%X\n" % plmn])
    (plmn,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["plmn:0x%X\n" % plmn])
    (plmn,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["plmn:0x%X\n" % plmn])
    outstream.writelines(["Rsv:%d\n" % struct.unpack('B', instream.read(1))])
    #NRNAS_MNTN_SAVE_EXC_PS_NR_PLMN_ID_STRU End

    outstream.writelines(["Cur Eap Entity Idx:%d\n" % struct.unpack('B', instream.read(1))])
    outstream.writelines(["usim status:%d (0:valid 1:invalid)\n" % struct.unpack('B', instream.read(1))])
    (Resv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["Resv:0x%X\n" % Resv])
    (Resv,)           = struct.unpack('B', instream.read(1))
    outstream.writelines(["Resv:0x%X\n" % Resv])

    outstream.writelines(["--Nreap Mntn Dump End--\n"])

def analysis_nrnas_msg_state_stru(instream, fileLocalOffset, outstream, ulLooper):
    instream.seek(fileLocalOffset)

    (ulReceiveTime,) = struct.unpack('I', instream.read(4))
    (ulExitTime,)    = struct.unpack('I', instream.read(4))

    (usSendPid,)     = struct.unpack('I', instream.read(4))
    (usRcvPid,)      = struct.unpack('I', instream.read(4))

    (usMsgId,)       = struct.unpack('H', instream.read(2))
    (ucFsmId,)   = struct.unpack('B', instream.read(1))
    (ucState,)   = struct.unpack('B', instream.read(1))

    strSendPid       = nrnas_get_pid_str(usSendPid)
    strRcvPid        = nrnas_get_pid_str(usRcvPid)
    strMsgId         = nrnas_get_msgid_str(strSendPid, strRcvPid, usMsgId)

    strSendPid       = '%s(0x%x)' % (strSendPid, usSendPid)
    strRcvPid        = '%s(0x%x)' % (strRcvPid, usRcvPid)
    strMsgId         = '%s(0x%x)' % (strMsgId, usMsgId)
    strReceiveTime   = '%x' % ulReceiveTime
    strExitTime      = '%x' % ulExitTime

    strFsmId     = '0x%x' % (ucFsmId)

    strState     = '0x%x' % ucState

    #outstream.writelines(["\n**************************** (-.^): *******************************\n"])
    outstream.writelines(["%-10s%-15s%-15s%-15s%-15s%-55s%-20s%-20s\n" % (ulLooper, strReceiveTime.upper(), strExitTime.upper(), strSendPid, strRcvPid, strMsgId, strFsmId, strState)])

def analysis_nrmm_state_modem0_dump_info(instream, fileOffset, outstream):
    count = 0
    outstream.writelines(["%-10s%-15s%-15s%-15s%-15s%-55s%-20s%-20s\n" % ("index", "ulReceiveTime", "ulExitTime", "usSendPid", "usReceivePid", "usMsgId", "ucMsccFsmId", "ucMsccState")])

    #NRNAS_MSG_STATE_STRU的大小为20
    #输出70条NRNAS_MSG_STATE_STRU
    while count < MACRO_NRNAS_MAX_LOG_NRMM_MSG_STATE_NUM:
            analysis_nrnas_msg_state_stru(instream, 20*count+fileOffset, outstream, count)
            count = count + 1

    #NRNAS_LOG_NRMM_MSG_STATE_STRU中的ulLatestIndex
    outstream.writelines(["\nLatestIndex:%d\n" % struct.unpack('I', instream.read(4))])

def analysis_nrcm_state_modem0_dump_info(instream, fileOffset, outstream):
    count = 0
    outstream.writelines(["%-10s%-15s%-15s%-15s%-15s%-55s%-20s%-20s\n" % ("index", "ulReceiveTime", "ulExitTime", "usSendPid", "usReceivePid", "usMsgId", "ucMsccFsmId", "ucMsccState")])

    #NRNAS_MSG_STATE_STRU的大小为20
    #输出70条NRNAS_MSG_STATE_STRU
    while count < MACRO_NRNAS_MAX_LOG_NRCM_MSG_STATE_NUM:
            analysis_nrnas_msg_state_stru(instream, 20*count+fileOffset, outstream, count)
            count = count + 1

    #NRNAS_LOG_NRMM_MSG_STATE_STRU中的ulLatestIndex
    outstream.writelines(["\nLatestIndex:%d\n" % struct.unpack('I', instream.read(4))])

def analysis_nreap_state_modem0_dump_info(instream, fileOffset, outstream):
    count = 0
    outstream.writelines(["%-10s%-15s%-15s%-15s%-15s%-55s%-20s%-20s\n" % ("index", "ulReceiveTime", "ulExitTime", "usSendPid", "usReceivePid", "usMsgId", "ucMsccFsmId", "ucMsccState")])

    #NRNAS_MSG_STATE_STRU的大小为20
    #输出70条NRNAS_MSG_STATE_STRU
    while count < MACRO_NRNAS_MAX_LOG_NREAP_MSG_STATE_NUM:
            analysis_nrnas_msg_state_stru(instream, 20*count+fileOffset, outstream, count)
            count = count + 1

    #NRNAS_LOG_NRMM_MSG_STATE_STRU中的ulLatestIndex
    outstream.writelines(["\nLatestIndex:%d\n" % struct.unpack('I', instream.read(4))])

def analysis_nrnas_modem0_dump_info(instream, fileOffset, outstream):

    ########################### 解析NRNAS MSG STATE--BEGIN ############################
    #解析NRMM MSG STATE
    analysis_nrmm_state_modem0_dump_info(instream, fileOffset, outstream)
    fileOffset = fileOffset + 20*MACRO_NRNAS_MAX_LOG_NRMM_MSG_STATE_NUM + 4

    #解析NRCM MSG STATE
    analysis_nrcm_state_modem0_dump_info(instream, fileOffset, outstream)
    fileOffset = fileOffset + 20*MACRO_NRNAS_MAX_LOG_NRCM_MSG_STATE_NUM + 4

    #解析NREAP MSG STATE
    analysis_nreap_state_modem0_dump_info(instream, fileOffset, outstream)
    fileOffset = fileOffset + 20*MACRO_NRNAS_MAX_LOG_NREAP_MSG_STATE_NUM + 4
    ########################### 解析NRNAS MSG STATE--END ############################

    #NRNAS_NRSM_MNTN_SAVE_EXC_LOG_STRU
    analysis_nrsm_mntn_save_exc_log(instream, fileOffset, outstream)
    fileOffset = fileOffset + 232

    #NRNAS_NREAP_MNTN_SAVE_EXC_LOG_STRU
    analysis_nreap_mntn_save_exc_log(instream, fileOffset, outstream)
    fileOffset = fileOffset + 364

    ########################### 解析NRNAS_NRMM_MNTN_SAVE_EXC_LOG_STRU--BEGIN ############################
    analysis_nrmm_mntn_save_exc_log(instream, fileOffset, outstream)
    fileOffset = fileOffset + 456
    ########################### 解析NRNAS_NRMM_MNTN_SAVE_EXC_LOG_STRU--END ############################
    instream.seek(fileOffset)
    (endTick,)       = struct.unpack('I', instream.read(4))
    endTickStr         = '0x%x' % endTick
    print("End tag is %s" % (endTickStr))

def analysis_nrnas_event_state_list_dump_info(instream, fileOffset, outstream):

    #outstream.writelines(["\n**************************** analysis_nrnas_event_state_list_dump_info enter! %d*******************************\n" % (fileOffset)])
    instream.seek(fileOffset)
    (ulBeginTick,)       = struct.unpack('I', instream.read(4))
    strBeginTick         = '0x%x' % ulBeginTick
    print("Begin tag is %s" % (strBeginTick))

    #outstream.writelines(["strModem0LogBeginFlg         %-15s\n" % (strBeginTick )])

    fileOffset = fileOffset + 4

    #outstream.writelines(["\n**************************** analysis_nrnas_event_state_list_dump_info enter! %d*******************************\n" % (fileOffset)])

    analysis_nrnas_modem0_dump_info(instream, fileOffset, outstream)

    return True

def analysis_nrnas_dump_info(infile, offset, outfile):
    instream = infile
    outstream  = outfile
    fileOffset = eval(offset)

    ##### nrnas PARSE EVENT STATE #########
    outstream.writelines(["\n**************************** modem0:analysis_nrnas_dump_info begin!*******************************\n"])
    analysis_nrnas_event_state_list_dump_info(instream, fileOffset, outstream)
    outstream.writelines(["\n**************************** modem0:analysis_nrnas_dump_info end!*******************************\n"])

    return True

########################################################################################
def entry_0x7200012(infile, field, offset, len, version, mode, outfile):
    ########check parameter start#############
    if not field == '0x7200012':
        print("hidis field is %s" % (field))
        print("current field is 0x7200012")
        return error['ERR_CHECK_FIELD']
    elif not version == '0x0002':
        print("hidis version is %s" % (version))
        print("current version is 0x0001")
        return error['ERR_CHECK_VERSION']
    print("Offset is %s" % (offset))
    #########check parameter end##############
    ret = analysis_nrnas_dump_info(infile, offset, outfile)

    return 0

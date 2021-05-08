#!/usr/bin/env python3
# coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2016 - 2019 Hisilicon Technoligies Co., Ltd.
# * Filename      field_0x2200002_0000.py
# * Description   tlps dump
# * Version       1.0
# * Data          2018-03-22 create file
#***********************************************************************
import struct
import os
import sys
import string

from pid_msg import *
from lnas_state import *
from lrrc_state import *
from trrc_state import *

TLPS_EXC_HPA_SEND_FAIL_MSG_NUM = 8
LHPA_DATA_ABORT_MSG_STRU_SIZE  = 16

NAS_LMM_PARA_FSM_BUTT = 2

RRC_PARA_FSM_BUTT = 5
LRRC_LNAS_RAT_TYPE_BUTT = 5

TLPS_EXC_MAX_SAVE_MSG_NUM = 200

LNAS_EXC_MAX_SAVE_MSG_NUM = 50
def analysis_lnas_msg_state_info( instream, fileOffset, outstream):
        ulLooper = 0
        strSendPid = 'nonPid'
        strRcvPid  = 'nonPid'
        strMsgid   = 'UnKnowId'
        strMs      = 'UnKnowState'
        strSs      = 'UnKnowState'
        
        instream.seek(fileOffset)
        outstream.writelines(["%-15s%-20s%-20s%-15s%-55s%-40s%-70s\n" % ("TimeStamp", "SendPid", "RcvPid", "Aug", "MsgId", "EMM MS", "EMM SS")])
        
        while ulLooper < (LNAS_EXC_MAX_SAVE_MSG_NUM):
                instream.seek(fileOffset + 20*(LNAS_EXC_MAX_SAVE_MSG_NUM - 1 - ulLooper))
                (ulTimeStamp,)      = struct.unpack('I', instream.read(4))
                (ulRcvPid,)         = struct.unpack('H', instream.read(2))
                (ulSendPid,)        = struct.unpack('H', instream.read(2))                
                (ulMsgId,)          = struct.unpack('I', instream.read(4))
                (ulAug,)            = struct.unpack('I', instream.read(4))
                (enMs,)             = struct.unpack('H', instream.read(2))
                (enSs,)             = struct.unpack('H', instream.read(2))
                
                strSendPid = Tlps_Get_Pid_Str(ulSendPid)
                strRcvPid  = Tlps_Get_Pid_Str(ulRcvPid)
                strMsgid   = Tlps_Get_MsgId_Str(strSendPid, strRcvPid,ulMsgId)
                strMs      = Tlps_Get_Lnas_MainState_Str(enMs)
                strSs      = Tlps_Get_Lnas_SubState_Str(enSs)
                
                strTimeStamp_Merge   = '0x%08x'% ulTimeStamp
                strSendPid_Merge     = '%s(0x%x)' % ( strSendPid, ulSendPid)
                strRcvPid_Merge      = '%s(0x%x)' % ( strRcvPid, ulRcvPid)
                strAug_Merge         = '0x%08x' % ulAug
                strMsgId_Merge       = '%s(0x%x)' % ( strMsgid, ulMsgId)
                strMs_Merge          = '%s(0x%x)' % ( strMs, enMs)
                strSs_Merge          = '%s(0x%x)' % ( strSs, enSs)
                
                outstream.writelines(["%-15s%-20s%-20s%-15s%-55s%-40s%-70s\n" % (strTimeStamp_Merge, strSendPid_Merge, strRcvPid_Merge, strAug_Merge, strMsgId_Merge, strMs_Merge, strSs_Merge)])
                ulLooper = ulLooper + 1
        
        return True

def analysis_tlps_msg_info( instream, fileOffset, outstream):
        ulLooper = 0
        strSendPid = 'nonPid'
        strRcvPid  = 'nonPid'
        strMsgid   = 'UnKnowId'

        instream.seek(fileOffset)
        outstream.writelines(["%-15s%-20s%-20s%-15s%-70s\n" % ("TimeStamp", "SendPid", "RcvPid", "Aug","MsgId")])
        
        while ulLooper < (TLPS_EXC_MAX_SAVE_MSG_NUM):
                instream.seek(fileOffset + 16*(TLPS_EXC_MAX_SAVE_MSG_NUM - 1 - ulLooper))
                (ulTimeStamp,)      = struct.unpack('I', instream.read(4))
                (ulRcvPid,)         = struct.unpack('H', instream.read(2))
                (ulSendPid,)        = struct.unpack('H', instream.read(2))                
                (ulMsgId,)          = struct.unpack('I', instream.read(4))
                (ulAug,)            = struct.unpack('I', instream.read(4))
                
                strSendPid = Tlps_Get_Pid_Str(ulSendPid)
                strRcvPid  = Tlps_Get_Pid_Str(ulRcvPid)
                strMsgid   = Tlps_Get_MsgId_Str(strSendPid, strRcvPid,ulMsgId)
                
                if 0xbd00 == ulMsgId:
                    timerid = 0x0000ffff & ulAug
                    strMsgid = Tlps_Get_Lrrc_StaTiId_Str(timerid)
                    
                strTimeStamp_Merge   = '0x%08x'% ulTimeStamp
                strSendPid_Merge     = '%s(0x%x)' % ( strSendPid, ulSendPid)
                strRcvPid_Merge      = '%s(0x%x)' % ( strRcvPid, ulRcvPid)
                strAug_Merge         = '0x%08x' % ulAug
                strMsgId_Merge       = '%s(0x%x)' % ( strMsgid, ulMsgId)
                
                outstream.writelines(["%-15s%-20s%-20s%-15s%-70s\n" % (strTimeStamp_Merge, strSendPid_Merge, strRcvPid_Merge, strAug_Merge, strMsgId_Merge)])
                ulLooper = ulLooper + 1
        
        return True

def analysis_trrc_state_info( instream, fileOffset, outstream):
        instream.seek(fileOffset)
        
        (enFlowCtrlFlag,)       = struct.unpack('I', instream.read(4))
        (enTrrcSubState,)       = struct.unpack('I', instream.read(4))
        (enTrrcState,)          = struct.unpack('B', instream.read(1))
        (enUtranMode,)          = struct.unpack('B', instream.read(1))
        (enTmacPreState,)       = struct.unpack('B', instream.read(1))
        (enTmacStartState,)     = struct.unpack('B', instream.read(1)) 
               
        strFlowCtrlFlag         = Trrc_Get_Flow_Ctrl_Flag_Str(enFlowCtrlFlag)
        strTrrcSubState         = Trrc_Get_Sub_State_Str(enTrrcSubState)
        strTrrcState            = Trrc_Get_Tds_State_Str(enTrrcState)
        strUtranMode            = Trrc_Get_Utran_Mode_Str(enUtranMode)
        
        outstream.writelines(["TRRC Flow  CtrlFlg[0x%x]: %s\n" % (enFlowCtrlFlag, strFlowCtrlFlag)])
        outstream.writelines(["TRRC    Sub  State[0x%x]: %s\n" % (enTrrcSubState, strTrrcSubState)])
        outstream.writelines(["TRRC Current State[0x%x]: %s\n" % (enTrrcState, strTrrcState)])
        outstream.writelines(["UTAN MODE[0x%x]: %s\n" % (enUtranMode, strUtranMode)])
        outstream.writelines(["TRRC TmacPreState: 0x%x\n" % (enTmacPreState)])
        outstream.writelines(["TRRC TmacStartState: 0x%x\n" % (enTmacStartState)])
        
        return True

def analysis_lrrc_state_info( instream, fileOffset, outstream):
        ulLooper = 0
        instream.seek(fileOffset)
        
        strFsmId        = 'unkown'
        strMainState    = 'unkown'
        strSubState     = 'unkown'
        strStaTiId      = 'unkown'
        
        strRrcConnState = 'unkown'
        strLteState     = 'unkown'
        strRrcFlowCtrlFlg = 'unkown'
        while ulLooper < (RRC_PARA_FSM_BUTT):
                (enFsmId,)      = struct.unpack('H', instream.read(2))
                (enMainState,)  = struct.unpack('H', instream.read(2))
                (enSubState,)   = struct.unpack('H', instream.read(2))
                (enStaTiId,)    = struct.unpack('H', instream.read(2))
                
                strFsmId       = Tlps_Get_Lrrc_FsmId_Str(enFsmId)
                strMainState   = Tlps_Get_Lrrc_MainState_Str(enMainState)
                strSubState    = Tlps_Get_Lrrc_SubState_Str(enSubState)
                strStaTiId     = Tlps_Get_Lrrc_StaTiId_Str(enStaTiId)
                
                strFsmId_Merge      = 'FSM[0x%x]:%s'% ( enFsmId, strFsmId)
                strMainState_Merge  = 'MS[0x%x]:%s'% ( enMainState, strMainState)
                strSubState_Merge   = 'SS[0x%x]:%s'% ( enSubState, strSubState)
                strStaTiId_Merge    = 'StateTi[0x%x]:%s'% ( enStaTiId, strStaTiId)
                
                outstream.writelines(["%-35s%-58s%-58s%-80s\n" % (strFsmId_Merge, strMainState_Merge, strSubState_Merge, strStaTiId_Merge)])
                ulLooper = ulLooper + 1
        (enRrcFlowCtrlFlg,)      = struct.unpack('i', instream.read(4))
        strRrcFlowCtrlFlg       = Tlps_Get_Lrrc_FlowCtrlFlg_Str(enRrcFlowCtrlFlg)
        outstream.writelines(["FLOW CTRL FLAG[0x%x]: %s\n" % (enRrcFlowCtrlFlg, strRrcFlowCtrlFlg)])
        
        (enGsm_Prio,)      = struct.unpack('B', instream.read(1))
        (enUtran_Prio,)    = struct.unpack('B', instream.read(1))
        (enLte_Prio,)      = struct.unpack('B', instream.read(1))
        (en1X_Prio,)       = struct.unpack('B', instream.read(1))
        (enHrpd_Prio,)     = struct.unpack('B', instream.read(1))
        
        strRatPrio = Lrrc_get_rat_prio_Str(enGsm_Prio)
        outstream.writelines(["Gsm    Prio[0x%x]: %s\n" % (enGsm_Prio, strRatPrio)])
        strRatPrio = Lrrc_get_rat_prio_Str(enUtran_Prio)
        outstream.writelines(["Utran  Prio[0x%x]: %s\n" % (enUtran_Prio, strRatPrio)])
        strRatPrio = Lrrc_get_rat_prio_Str(enLte_Prio)
        outstream.writelines(["LTE    Prio[0x%x]: %s\n" % (enLte_Prio, strRatPrio)])
        strRatPrio = Lrrc_get_rat_prio_Str(en1X_Prio)
        outstream.writelines(["CDMA1X Prio[0x%x]: %s\n" % (en1X_Prio, strRatPrio)])
        strRatPrio = Lrrc_get_rat_prio_Str(enHrpd_Prio)
        outstream.writelines(["HRPD   Prio[0x%x]: %s\n" % (enHrpd_Prio, strRatPrio)])
        
        (enAS_rel,)          = struct.unpack('B', instream.read(1))
        (enConnState,)       = struct.unpack('B', instream.read(1))
        (Rsv,)               = struct.unpack('B', instream.read(1))
        strAS_rel    = Lrrc_get_as_release_Str(enAS_rel)
        strConnState = Lrrc_get_protocal_state_Str(enConnState)
        outstream.writelines(["LRRC Release[0x%x]: %s\n" % (enAS_rel, strAS_rel)])
        outstream.writelines(["LRRC PROTOCAL STATE[0x%x]: %s\n" % (enConnState, strConnState)])
        
        (enUtranMode,)      = struct.unpack('i', instream.read(4))
        strUtranMode  = Lrrc_get_utran_mode_Str(enUtranMode)
        outstream.writelines(["UE MODE[0x%x]: %s\n" % (enUtranMode, strUtranMode)])
        
        return True

def analysis_lnas_state_info( instream, fileOffset, outstream):
        ulLooper = 0
        instream.seek(fileOffset)
        
        strFsmId        = 'unkown'
        strMainState    = 'unkown'
        strSubState     = 'unkown'
        strStaTiId      = 'unkown'
        strRrcConnState = 'unkown'
        strLteState     = 'unkown'
        while ulLooper < (NAS_LMM_PARA_FSM_BUTT):
                (enFsmId,)      = struct.unpack('H', instream.read(2))
                (enMainState,)  = struct.unpack('H', instream.read(2))
                (enSubState,)   = struct.unpack('H', instream.read(2))
                (enStaTiId,)    = struct.unpack('H', instream.read(2))
                
                strFsmId       = Tlps_Get_Lnas_FsmId_Str(enFsmId)
                strMainState   = Tlps_Get_Lnas_MainState_Str(enMainState)
                strSubState    = Tlps_Get_Lnas_SubState_Str(enSubState)
                strStaTiId     = Tlps_Get_Lnas_StaTiId_Str(enStaTiId)
                
                strFsmId_Merge      = '[0x%x]: %s'% ( enFsmId, strFsmId)
                strMainState_Merge  = 'MS[0x%x]: %s'% ( enMainState, strMainState)
                strSubState_Merge   = 'SS[0x%x]: %s'% ( enSubState, strSubState)
                strStaTiId_Merge    = 'StateTi[0x%x]: %s'% ( enStaTiId, strStaTiId)
                
                outstream.writelines(["%-20s%-40s%-50s%-70s\n" % (strFsmId_Merge, strMainState_Merge, strSubState_Merge, strStaTiId_Merge)])
                ulLooper = ulLooper + 1
        (enRrcConnState,)      = struct.unpack('I', instream.read(4))
        (enLteState,)          = struct.unpack('I', instream.read(4))
        enRrcConnState = 0x000000FF & enRrcConnState
        strRrcConnState = Tlps_Get_Lnas_RrcConnState_Str(enRrcConnState)
        strLteState     = Tlps_Get_Lnas_LteState_Str(enLteState)
        outstream.writelines(["CONN STATE[0x%x]: %s\n" % (enRrcConnState, strRrcConnState)])
        outstream.writelines(["LTE  STATE[0x%x]: %s\n" % (enLteState, strLteState)])
        
        return True

def analysis_mbx_write_fail_msg_info( instream, fileOffset, outstream):
        ulLooper = 0
        strSendPid = 'nonPid'
        strMsgid = 'UnKnowId'
        strRcvPid = 'PS_HPA'
        fileOffset = fileOffset + 4
        instream.seek(fileOffset)
        outstream.writelines(["%-15s%-20s%-20s%-70s\n" % ("TimeStamp", "SendPid", "Opid", "MsgId")])
        
        while ulLooper < (TLPS_EXC_HPA_SEND_FAIL_MSG_NUM):
                (ulTimeStamp,)      = struct.unpack('I', instream.read(4))
                (ulSendPid,)        = struct.unpack('I', instream.read(4))
                (ulOpid,)           = struct.unpack('I', instream.read(4))
                (ulMsgId,)          = struct.unpack('I', instream.read(4))
                
                strSendPid = Tlps_Get_Pid_Str(ulSendPid)
                strMsgid   = Tlps_Get_MsgId_Str(strSendPid, strRcvPid,ulMsgId)
                
                strTimeStamp_Merge   = '0x%08x'% ulTimeStamp
                strSendPid_Merge     = '%s(0x%x)' % ( strSendPid, ulSendPid)
                strOpid_Merge        = '0x%08x' % ulOpid
                strMsgId_Merge       = '%s(0x%x)' % ( strMsgid, ulMsgId)
                
                outstream.writelines(["%-15s%-20s%-20s%-70s\n" % (strTimeStamp_Merge, strSendPid_Merge, strOpid_Merge, strMsgId_Merge)])
                ulLooper = ulLooper + 1
        
        return True

def analysis_tlps_dump_info( infile, offset, outfile):
        instream = infile
        outstream  = outfile
        fileOffset = eval(offset)
        
        outstream.writelines(["************************************************************\n"])
        outstream.writelines(["******** TLPS_DUMP_ANALYSIS_2018_03_22_VERSION_1.0 *********\n"])
        outstream.writelines(["************************************************************\n\n"])
        
        fileOffset = fileOffset + 32
        outstream.writelines(["************************************ WRITE MBX FAIL MSG *************************************\n"])
        analysis_mbx_write_fail_msg_info(infile, fileOffset, outfile)
        fileOffset = fileOffset + 4 + TLPS_EXC_HPA_SEND_FAIL_MSG_NUM*LHPA_DATA_ABORT_MSG_STRU_SIZE
        outstream.writelines(["\n"])
        
        outstream.writelines(["************************************ LNAS STATE INFO ***************************************\n"])
        analysis_lnas_state_info(infile, fileOffset, outfile)
        fileOffset = fileOffset + 24
        outstream.writelines(["\n"])
        
        outstream.writelines(["************************************ LRRC STATE INFO ***************************************\n"])
        analysis_lrrc_state_info(infile, fileOffset, outfile)
        fileOffset = fileOffset + 56
        outstream.writelines(["\n"])
        
        outstream.writelines(["************************************ TRRC STATE INFO ***************************************\n"])
        analysis_trrc_state_info(infile, fileOffset, outfile)
        fileOffset = fileOffset + 12
        outstream.writelines(["\n"])
        
        outstream.writelines(["************************************  TLPS MSG INFO ***************************************\n"])
        analysis_tlps_msg_info(infile, fileOffset, outfile)
        fileOffset = fileOffset + TLPS_EXC_MAX_SAVE_MSG_NUM*16
        outstream.writelines(["\n"])
        
        outstream.writelines(["************************************  LNAS MSG&STATE INFO **********************************\n"])
        analysis_lnas_msg_state_info(infile, fileOffset, outfile)
        fileOffset = fileOffset + LNAS_EXC_MAX_SAVE_MSG_NUM*20
        outstream.writelines(["************************************  TLPS ANALYSIS END  **********************************\n"])
        
        outstream.writelines(["\n"])
        outstream.writelines(["************************************************************\n"])
        outstream.writelines(["******** TLPS_DUMP_ANALYSIS_2018_03_22_VERSION_1.0 *********\n"])
        outstream.writelines(["************************************************************\n\n"])
        return True


########################################################################################
def entry_0x2200002(infile, field, offset, len, version, mode, outfile):

        ########check parameter start#############
        if not field == '0x2200002':
            #print 'hidis field is ', field
            #print 'current field is', '0x2200002'
            return error['ERR_CHECK_FIELD']
        elif not len == '0x2800':
            #print 'hids len is ', len
            #print 'current len is ', '0x2800'
            return error['ERR_CHECK_LEN']
        #########check parameter end##############

        ret = analysis_tlps_dump_info( infile, offset, outfile)

        return 0


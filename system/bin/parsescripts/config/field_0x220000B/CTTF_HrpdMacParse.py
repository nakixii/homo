#!/usr/bin/env python3
# coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2016 - 2019 Hisilicon Technoligies Co., Ltd.
# * Filename      CTTF_HrpdMacParse.py
# * Description   parse Hrpd Mac Dump Info
# * Version       1.0
# * Data          2016-07-07 create file
#***********************************************************************
import struct
from pid import CTTF_GetPidStr
from msgId import CTTF_GetMsgIdStr

CTTF_HRPD_MAC_MNTN_DUMP_MAX_SAVE_STATE_NUM  = 5
CTTF_HRPD_MAC_MNTN_DUMP_MAX_SAVE_MSG_NUM    = 50

def CTTF_HRPD_MAC_GetStateStr(ucState, type):
    state_table = {
        'AcMacStateCtx' : {
            0 : 'NULL',
            1 : 'RUN'
        },
        'AcMacSubStateCtx' : {
            0 : 'NULL',
            1 : 'PERSIST',
            2 : 'TX_SETUP',
            3 : 'TX_PRE',
            4 : 'TX_DATA',
            5 : 'TX_DONE',
            6 : 'BKOFF',
            7 : 'MAXSEQ',
            8 : 'TX_END'
        }
    }
    if type in state_table and ucState in state_table[type]:
        strState = state_table[type][ucState]
    else:
        strState = str(ucState)
    return strState
        
def CTTF_HRPD_MAC_ParseStateInfo(infile, type):
    #############################################################################################################
    #   CTTF_HRPD_MAC_MNTN_DUMP_STATE_INFO_STRU结构
    #   VOS_UINT16          usTimeStamp
    #   VOS_UINT8           ucOldState
    #   VOS_UINT8           ucNewState
    #############################################################################################################
    usTimeStamp, ucOldState, ucNewState = struct.unpack('H2B', infile.read(4))
    strOldState = CTTF_HRPD_MAC_GetStateStr(ucOldState, type)
    strNewState = CTTF_HRPD_MAC_GetStateStr(ucNewState, type)
    return usTimeStamp, strOldState, strNewState
    
def CTTF_HRPD_MAC_ParseStateCtx(infile, outfile, type):
    #############################################################################################################
    #   CTTF_HRPD_MAC_MNTN_DUMP_STATE_CONTEXT_STRU结构
    #   VOS_UINT8                   ucHeadIndex
    #   VOS_UINT8                   ucTailIndex
    #   VOS_UINT16                  usReserved
    #   CTTF_HRPD_MAC_MNTN_DUMP_STATE_INFO_STRU astStateInfo[CTTF_HRPD_MAC_MNTN_DUMP_MAX_SAVE_STATE_NUM]
    #############################################################################################################
    outfile.write('------------------------------------%s Start------------------------------------------\n' % type)
    ucHeadIndex, ucTailIndex, _ = struct.unpack('2BH', infile.read(4))
    astStateInfo = []
    for i in range(CTTF_HRPD_MAC_MNTN_DUMP_MAX_SAVE_STATE_NUM):
        stateInfo = CTTF_HRPD_MAC_ParseStateInfo(infile, type)
        astStateInfo.append(stateInfo)
    out_str = '%-9s     %8s--->%-8s  \n' % ('TimeStamp', 'OldState', 'NewState')
    outfile.write(out_str)    
    for i in range((ucHeadIndex - 1)%CTTF_HRPD_MAC_MNTN_DUMP_MAX_SAVE_STATE_NUM, CTTF_HRPD_MAC_MNTN_DUMP_MAX_SAVE_STATE_NUM):
        out_str = '%05d         %8s--->%-8s \n' % (astStateInfo[i])
        outfile.write(out_str)
    for i in range(ucTailIndex):
        out_str = '%05d         %8s--->%-8s \n' % (astStateInfo[i])
        outfile.write(out_str)
    outfile.write('------------------------------------%s End--------------------------------------------\n\n' % type)    

def CTTF_HRPD_MAC_ParseMsgInfo(infile):
    #############################################################################################################
    #   CTTF_HRPD_MAC_MNTN_DUMP_MSG_INFO_STRU结构
    #   VOS_UINT16          usTimeStamp
    #   VOS_UINT16          usMsgId
    #   VOS_UINT8           ucSendPid
    #   VOS_UINT8           ucRcvPid
    #   VOS_UINT16          usFlag
    #############################################################################################################
    usTimeStamp, usMsgId, ucSendPid, ucRcvPid, usFlag = struct.unpack('2H2BH', infile.read(8))
    strSendPid  = CTTF_GetPidStr(ucSendPid)
    strRcvPid   = CTTF_GetPidStr(ucRcvPid)
    strMsgId    = CTTF_GetMsgIdStr(usMsgId)
    return usTimeStamp, strMsgId, strSendPid, strRcvPid, usFlag
    
def CTTF_HRPD_MAC_ParseMsgCtx(infile, outfile):
    #############################################################################################################
    #   CTTF_HRPD_MAC_MNTN_DUMP_MSG_CONTEXT_STRU
    #   VOS_UINT8                   ucHeadIndex
    #   VOS_UINT8                   ucTailIndex
    #   VOS_UINT16                  usReserved
    #   CTTF_HRPD_MAC_MNTN_DUMP_MSG_INFO_STRU astMsgInfo[CTTF_HRPD_MAC_MNTN_DUMP_MAX_SAVE_MSG_NUM]
    #############################################################################################################
    outfile.write('------------------------------------MAC Msg Info Start----------------------------------------------\n')
    ucHeadIndex, ucTailIndex, _ = struct.unpack('2BH', infile.read(4))
    astMsgInfo = []
    for i in range(CTTF_HRPD_MAC_MNTN_DUMP_MAX_SAVE_MSG_NUM):
        msgInfo = CTTF_HRPD_MAC_ParseMsgInfo(infile)
        astMsgInfo.append(msgInfo)
    out_str = '%-9s   %-50s   %-10s   %-10s %-5s  \n' % ('TimeStamp', 'msgId', 'sendPid', 'rcvPid', 'flag')
    outfile.write(out_str)
    for i in range((ucHeadIndex - 1)%CTTF_HRPD_MAC_MNTN_DUMP_MAX_SAVE_STATE_NUM, CTTF_HRPD_MAC_MNTN_DUMP_MAX_SAVE_STATE_NUM):
        out_str = '%05d       %-50s   %-10s   %-10s   %d \n' % (astMsgInfo[i])
        outfile.write(out_str)
    for i in range(ucTailIndex):
        out_str = '%05d       %-50s   %-10s   %-10s   %d \n' % (astMsgInfo[i])
        outfile.write(out_str)    
    outfile.write('------------------------------------MAC Msg Info End------------------------------------------------\n\n') 
    
def CTTF_HRPD_MAC_ParseDumpInfo(infile, outfile, usDataLen):
    if usDataLen != 500:
        outfile.write('please Update The HRPD MAC Parse Struct')
        return False
    #############################################################################################################
    #   HRPD MAC DUMP信息结构
    #   CTTF_HRPD_MAC_MNTN_DUMP_STATE_CONTEXT_STRU  stAcMacStateCtx
    #   CTTF_HRPD_MAC_MNTN_DUMP_STATE_CONTEXT_STRU  stAcMacSubStateCtx
    #   CTTF_HRPD_MAC_MNTN_DUMP_STATE_CONTEXT_STRU  stMacTxCtrlStateCtx
    #   CTTF_HRPD_MAC_MNTN_DUMP_STATE_CONTEXT_STRU  stMacMonitorCtrlStateCtx
    #   CTTF_HRPD_MAC_MNTN_DUMP_MSG_CONTEXT_STRU    stMacMsgCtx
    #############################################################################################################
    outfile.write('------------------------------------Hrpd Mac Dump Info Start----------------------------------------\n')
    CTTF_HRPD_MAC_ParseStateCtx(infile, outfile, 'AcMacStateCtx')
    CTTF_HRPD_MAC_ParseStateCtx(infile, outfile, 'AcMacSubStateCtx')
    CTTF_HRPD_MAC_ParseStateCtx(infile, outfile, 'MacTxCtrlStateCtx')
    CTTF_HRPD_MAC_ParseStateCtx(infile, outfile, 'MacMonitorCtrlStateCtx')
    CTTF_HRPD_MAC_ParseMsgCtx(infile, outfile)
    outfile.write('------------------------------------Hrpd Mac Dump Info End-------------------------------------------\n')
    
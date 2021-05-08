#!/usr/bin/env python3
# coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2016 - 2019 Hisilicon Technoligies Co., Ltd.
# * Filename      CTTF_1xLacParse.py
# * Description   parse 1x Lac Dump Info
# * Version       1.0
# * Data          2016-08-27 create file
#***********************************************************************
import struct

CTTF_1X_LAC_MNTN_DUMP_MAX_LINK_NUM = 12

def CTTF_1X_GetBoolStr(enFlag):
    state_table = {
            0 : 'FALSE',
            1 : 'TRUE',
    }
    if enFlag in state_table:
        strBool = state_table[enFlag]
    else:
        strBool = str(enFlag)
    return strBool

def CTTF_1X_LAC_GetCschEntStateStr(ucCschEntState):
    state_table = {
        0 : 'NULL',
        1 : 'EXIST',
    }
    if ucCschEntState in state_table:
        strCschEntState = state_table[ucCschEntState]
    else:
        strCschEntState = str(ucCschEntState)
    return strCschEntState

def CTTF_1X_LAC_ParseRLacCschInfo(infile, outfile):
    #############################################################################################################
    #   1X RLAC CSCH信息结构
    #   VOS_UINT8                                   ucRCschEntState
    #   VOS_UINT8                                   ucReserve
    #   VOS_UINT16                                  usPRevInUse
    #############################################################################################################
    ucRCschEntState, _, usPRevInUse = struct.unpack('2BH', infile.read(4))
    outfile.write('****************RLacCschInfo****************\n')
    strRCschEntState = CTTF_1X_LAC_GetCschEntStateStr(ucRCschEntState)
    out_str = 'RCschEntState : %s \n' % strRCschEntState
    outfile.write(out_str)
    out_str = 'PRevInUse : %d \n' % usPRevInUse
    outfile.write(out_str)

def CTTF_1X_LAC_ParseFLacCschInfo(infile, outfile):
    #############################################################################################################
    #   1X FLAC CSCH信息结构
    #   VOS_UINT8                                   ucFCschEntState
    #   PS_BOOL_ENUM_UINT8                          enSlotted
    #   VOS_UINT16                                  usPagingSlotCycle
    #############################################################################################################
    ucFCschEntState, enSlotted, usPagingSlotCycle = struct.unpack('2BH', infile.read(4))
    outfile.write('****************FLacCschInfo****************\n')
    strFCschEntState = CTTF_1X_LAC_GetCschEntStateStr(ucFCschEntState)
    out_str = 'FCschEntState : %s \n' % strFCschEntState
    outfile.write(out_str)
    strSlotted = CTTF_1X_GetBoolStr(enSlotted)
    out_str = 'Slotted : %s \n' % strSlotted
    outfile.write(out_str)
    strPagingSlotCycle = str(usPagingSlotCycle)
    out_str = 'PagingSlotCycle : %s \n' % strPagingSlotCycle
    outfile.write(out_str)

def CTTF_1X_LAC_GetDschStateStr(ucDschState):
    state_table = {
        0 : 'NULL',
        1 : 'READY',
        2 : 'TRANSMITTING',
    }
    if ucDschState in state_table:
        strDschState = state_table[ucDschState]
    else:
        strDschState = str(ucDschState)
    return strDschState

def CTTF_1X_LAC_ParseRLacDschInfo(infile, outfile):
    #############################################################################################################
    #   1X RLAC DSCH信息结构
    #   VOS_UINT16                                  usPRevInUse
    #   VOS_UINT8                                   ucRDschState
    #   VOS_UINT8                                   ucReserve
    #############################################################################################################
    usPRevInUse, ucRDschState, _ = struct.unpack('H2B', infile.read(4))
    outfile.write('****************RLacDschInfo****************\n')
    out_str = 'PRevInUse : %d \n' % usPRevInUse
    outfile.write(out_str)
    strRDschState = CTTF_1X_LAC_GetDschStateStr(ucRDschState)
    out_str = 'RDschState : %s \n' % strRDschState
    outfile.write(out_str)

def CTTF_1X_LAC_ParseFLacDschInfo(infile, outfile):
    #############################################################################################################
    #   1X FLAC DSCH信息结构
    #   VOS_UINT16                                  usPRevInUse
    #   PS_BOOL_ENUM_UINT8                          enAcquireTchMode
    #   PS_BOOL_ENUM_UINT8                          enRxState
    #############################################################################################################
    usPRevInUse, enAcquireTchMode, enRxState = struct.unpack('H2B', infile.read(4))
    outfile.write('****************FLacDschInfo****************\n')
    out_str = 'PRevInUse : %d \n' % usPRevInUse
    outfile.write(out_str)
    strAcquireTchMode = CTTF_1X_GetBoolStr(enAcquireTchMode)
    out_str = 'AcquireTchMode : %s \n' % strAcquireTchMode
    outfile.write(out_str)
    strRxState = CTTF_1X_GetBoolStr(enRxState)
    out_str = 'RxState : %s \n' % strRxState
    outfile.write(out_str)

def CTTF_1X_LAC_ParseLacLinkInfo(infile, outfile):
    link_lable = {
        0 : 'RCSCH_SDU_LINK',
        1 : 'FDSCH_ACK_LINK',
        2 : 'SDU_NODE_LINK',
        3 : 'AWAIT_ACK_LINK',
        4 : 'SAR_TX_NODE_LINK',
        5 : 'FREE_NODE_LINK',
        6 : 'SYNC_SEG_LINK',
        7 : 'PCH_SEG_LINK',
        8 : 'OTHER_MSG_LINK',
        9 : 'GPMUPM_MSG_LINK',
        10 : 'FCSCH_IND_LINK',
        11 : 'FDSCH_DUPL_LINK',
    }
    outfile.write('****************LacLinkInfo****************\n')
    for i in range(CTTF_1X_LAC_MNTN_DUMP_MAX_LINK_NUM):
        ulLinkCnt = struct.unpack('I', infile.read(4))[0]
        outfile.write('%-25s : %d \n' % (link_lable[i], ulLinkCnt))

def CTTF_1X_LAC_ParseDumpInfo(infile, outfile, usDataLen):
    if usDataLen != 64:
        outfile.write('please Update The 1X LAC Parse Struct')
        return False
    #############################################################################################################
    #   1X LAC DUMP信息结构
    #   CTTF_1X_MAC_MNTN_DUMP_RLAC_CSCH_INFO_STRU   stRLacCschInfo
    #   CTTF_1X_MAC_MNTN_DUMP_FLAC_CSCH_INFO_STRU   stFLacCschInfo
    #   CTTF_1X_MAC_MNTN_DUMP_RLAC_DSCH_INFO_STRU   stRLacDschInfo
    #   CTTF_1X_MAC_MNTN_DUMP_FLAC_DSCH_INFO_STRU   stFLacDschInfo
    #   CTTF_1X_MAC_MNTN_DUMP_LINK_STATUS_STRU      astLacLinkInfo[CTTF_1X_LAC_MNTN_DUMP_LINK_BUTT]
    #############################################################################################################
    outfile.write('------------------------------------1x Lac Dump Info Start----------------------------------------\n')
    CTTF_1X_LAC_ParseRLacCschInfo(infile, outfile)
    CTTF_1X_LAC_ParseFLacCschInfo(infile, outfile)
    CTTF_1X_LAC_ParseRLacDschInfo(infile, outfile)
    CTTF_1X_LAC_ParseFLacDschInfo(infile, outfile)
    CTTF_1X_LAC_ParseLacLinkInfo(infile, outfile)
    outfile.write('------------------------------------1x Lac Dump Info End-------------------------------------------\n')

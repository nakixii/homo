#!/usr/bin/env python3
# coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2016 - 2019 Hisilicon Technoligies Co., Ltd.
# * Filename      CTTF_1xMacParse.py
# * Description   parse 1x Mac Dump Info
# * Version       1.0
# * Data          2016-08-27 create file
#***********************************************************************
import struct

CTTF_1X_MAC_MNTN_DUMP_MAX_FDATA_IND_NUM = 3
CTTF_1X_MAC_MNTN_DUMP_MAX_LINK_NUM      = 9

def CTTF_1X_MAC_GetMacStateStr(usState):
    state_table = {
            0 : 'NULL',
            1 : 'COMMON',
            2 : 'DEDICATE',
    }

    if usState in state_table:
        strState = state_table[usState]
    else:
        strState = str(ucState)
    return strState

def CTTF_1X_MAC_GetChannelStateStr(ucState):
    state_table = {
            0 : 'NOT_EXIST',
            1 : 'WAIT_ACQUIRE',
            2 : 'ALIVE',
    }

    if ucState in state_table:
        strState = state_table[ucState]
    else:
        strState = str(ucState)
    return strState

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

def CTTF_1X_MAC_GetFrameQualityStr(usFrameQuality):
    state_table = {
            0 : 'GOOD',
            1 : 'INSUFFICIENT',
            2 : 'INSUFFICIENT_KNOWN_RATE',
    }
    if usFrameQuality in state_table:
        strFrameQuality = state_table[usFrameQuality]
    else:
        strFrameQuality = str(usFrameQuality)
    return strFrameQuality

def CTTF_1X_MAC_ParseRMacEntInfo(infile, outfile):
    #############################################################################################################
    #   1X RMAC 实体信息结构
    #   VOS_UINT16                              usRMacState
    #   VOS_UINT16                              usServiceOption
    #   PS_BOOL_ENUM_UINT8                      enFchFlag
    #   PS_BOOL_ENUM_UINT8                      enSchFlag
    #   VOS_UINT8                               ucFchState
    #   VOS_UINT8                               ucSchState
    #############################################################################################################
    usRMacState, usServiceOption, enFchFlag, enSchFlag, ucFchState, ucSchState = struct.unpack('2H4B', infile.read(8))
    outfile.write('****************RMacEntInfo****************\n')
    strRMacState = CTTF_1X_MAC_GetMacStateStr(usRMacState)
    out_str = 'RMacState : %s \n' % strRMacState
    outfile.write(out_str)
    strServiceOption = str(usServiceOption)
    out_str = 'ServiceOption : %s \n' % strServiceOption
    outfile.write(out_str)
    strFchFlag = CTTF_1X_GetBoolStr(enFchFlag)
    out_str = 'FchFlag : %s \n' % strFchFlag
    outfile.write(out_str)
    strSchFlag = CTTF_1X_GetBoolStr(enSchFlag)
    out_str = 'SchFlag : %s \n' % strSchFlag
    outfile.write(out_str)
    strFchState = CTTF_1X_MAC_GetChannelStateStr(ucFchState)
    out_str = 'FchState : %s \n' % strFchState
    outfile.write(out_str)
    strSchState = CTTF_1X_MAC_GetChannelStateStr(ucSchState)
    out_str = 'SchState : %s \n' % strSchState
    outfile.write(out_str)

def CTTF_1X_MAC_ParseFMacIdx(infile, outfile, type):
    #############################################################################################################
    #   1X FMAC 邮箱Idx结构
    #   VOS_UINT16                              usHeadIdx
    #   VOS_UINT16                              usTailIdx
    #############################################################################################################
    usHeadIdx, usTailIdx = struct.unpack('2H', infile.read(4))
    outfile.write('%s FBuff Idx: \n' % type)
    outfile.write('HeadIdx: %d \n' % usHeadIdx)
    outfile.write('TailIdx: %d \n' % usTailIdx)

def CTTF_1X_MAC_ParseFDataInd(infile):
    #############################################################################################################
    #   1X FMAC 邮箱Data结构
    #   VOS_UINT16                              usRcvedInd
    #   VOS_UINT16                              usFrameQuality
    #   VOS_UINT32                              ulDataAddr
    #############################################################################################################
    usRcvedInd, usFrameQuality, ulDataAddr = struct.unpack('2HI', infile.read(8))
    strRcvedInd = str(usRcvedInd)
    strFrameQuality = CTTF_1X_MAC_GetFrameQualityStr(usFrameQuality)
    strDataAddr = '%08x' % ulDataAddr
    return strRcvedInd, strFrameQuality, strDataAddr
    
def CTTF_1X_MAC_PrintFDataInd(infile, outfile):
    outfile.write('%-10s %-24s %-10s \n' % ('RcvedInd', 'FrameQuality', 'DataAddr'))
    for i in range(CTTF_1X_MAC_MNTN_DUMP_MAX_FDATA_IND_NUM):
        stFDataInfo = CTTF_1X_MAC_ParseFDataInd(infile)
        outfile.write('%-10s %-24s %-10s \n' % stFDataInfo)

def CTTF_1X_MAC_ParseFMacBufInfo(infile, outfile):
    #############################################################################################################
    #   1X FMAC 邮箱信息结构
    #   CTTF_1X_MAC_MNTN_DUMP_FBUFFER_IDX_STRU  stFchBuffCtrl
    #   CTTF_1X_MAC_MNTN_DUMP_FDATA_STRU        astFchDataInd[3]
    #   CTTF_1X_MAC_MNTN_DUMP_FBUFFER_IDX_STRU  stSchBuffCtrl
    #   CTTF_1X_MAC_MNTN_DUMP_FDATA_STRU        astSchDataInd[3]
    #############################################################################################################
    outfile.write('****************FMacBufInfo****************\n')
    CTTF_1X_MAC_ParseFMacIdx(infile, outfile, 'FCH')
    CTTF_1X_MAC_PrintFDataInd(infile, outfile)
    CTTF_1X_MAC_ParseFMacIdx(infile, outfile, 'SCH')
    CTTF_1X_MAC_PrintFDataInd(infile, outfile)

def CTTF_1X_MAC_ParseFMacEntInfo(infile, outfile):
    #############################################################################################################
    #   1X FMAC 实体信息结构
    #   VOS_UINT16                              usFMacState
    #   PS_BOOL_ENUM_UINT8                      enSchFlag
    #   VOS_UINT8                               ucSchState
    #############################################################################################################
    usFMacState, enSchFlag, ucSchState = struct.unpack('H2B', infile.read(4))
    outfile.write('****************FMacEntInfo****************\n')
    strFMacState = CTTF_1X_MAC_GetMacStateStr(usFMacState)
    out_str = 'FMacState : %s \n' % strFMacState
    outfile.write(out_str)
    strSchFlag = CTTF_1X_GetBoolStr(enSchFlag)
    out_str = 'SchFlag : %s \n' % strSchFlag
    outfile.write(out_str)
    strSchState = CTTF_1X_MAC_GetChannelStateStr(ucSchState)
    out_str = 'SchState : %s \n' % strSchState
    outfile.write(out_str)

def CTTF_1X_MAC_ParseMacLinkInfo(infile, outfile):
    link_lable = {
        0 : 'RMAC_CHAN_CTRL_LINK',
        1 : 'RMAC_FCH_STORE_LINK',
        2 : 'RMAC_SCH_STORE_LINK',
        3 : 'RMAC_FCH_RATE_LINK',
        4 : 'RMAC_SCH_RATE_LINK',
        5 : 'RMAC_SRVDAT_LINK',
        6 : 'FMAC_CHAN_CTRL_LINK',
        7 : 'FMAC_FCH_STORE_LINK',
        8 : 'FMAC_SCH_STORE_LINK',
    }
    outfile.write('****************MacLinkInfo****************\n')
    for i in range(CTTF_1X_MAC_MNTN_DUMP_MAX_LINK_NUM):
        ulLinkCnt = struct.unpack('I', infile.read(4))[0]
        outfile.write('%-25s : %d \n' % (link_lable[i], ulLinkCnt))

def CTTF_1X_MAC_ParseDumpInfo(infile, outfile, usDataLen):
    if usDataLen != 104:
        outfile.write('please Update The 1X MAC Parse Struct')
        return False
    #############################################################################################################
    #   1X MAC DUMP信息结构
    #   CTTF_1X_MAC_MNTN_DUMP_RMAC_ENT_STRU     stRMacEntInfo
    #   CTTF_1X_MAC_MNTN_DUMP_FBUFFER_STRU      stFMacBufInfo
    #   CTTF_1X_MAC_MNTN_DUMP_FMAC_ENT_STRU     stFMacEntInfo
    #   CTTF_1X_MAC_MNTN_DUMP_LINK_STATUS_STRU  astMacLinkInfo[CTTF_1X_MAC_MNTN_DUMP_LINK_BUTT]
    #############################################################################################################
    outfile.write('------------------------------------1x Mac Dump Info Start----------------------------------------\n')
    CTTF_1X_MAC_ParseRMacEntInfo(infile, outfile)
    CTTF_1X_MAC_ParseFMacBufInfo(infile, outfile)
    CTTF_1X_MAC_ParseFMacEntInfo(infile, outfile)
    CTTF_1X_MAC_ParseMacLinkInfo(infile, outfile)
    outfile.write('------------------------------------1x Mac Dump Info End-------------------------------------------\n')

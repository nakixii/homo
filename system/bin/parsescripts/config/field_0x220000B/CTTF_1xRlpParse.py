#!/usr/bin/env python3
# coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2016 - 2019 Hisilicon Technoligies Co., Ltd.
# * Filename      CTTF_1xRlpParse.py
# * Description   parse 1x Rlp Dump Info
# * Version       1.0
# * Data          2016-08-29 create file
#***********************************************************************
import struct

CTTF_1X_RLP_MNTN_DUMP_MAX_LINK_NUM = 13

def CTTF_1X_MAC_GetRSchStateStr(ucState):
    state_table = {
            0 : 'EXIST',
            1 : 'NOT_EXIST_DTX',
            2 : 'NOT_EXIST_LIFETIME',
            3 : 'NOT_EXIST_OTHER',
    }

    if ucState in state_table:
        strState = state_table[ucState]
    else:
        strState = str(ucState)
    return strState

def CTTF_1X_MAC_GetTxFrameTypeStr(ucTxFrameType):
    frame_table = {
        0 : 'BLANK',
        1 : 'IDLE',
        2 : 'FILL',
        3 : 'REXMIT',
        4 : 'SYNC',
        5 : 'NAK',
        6 : 'NEW DATA'
    }
    if ucTxFrameType in frame_table:
        strTxFrameType = frame_table[ucTxFrameType]
    else:
        strTxFrameType = str(ucTxFrameType)
    return strTxFrameType

def CTTF_1X_MAC_GetRxFrameTypeStr(ucRxFrameType):
    frame_table = {
        0 : 'NO_DATA',
        1 : 'NEW_DATA',
        2 : 'RETRANSM_DATA',
    }
    if ucRxFrameType in frame_table:
        strRxFrameType = frame_table[ucRxFrameType]
    else:
        strRxFrameType = str(ucRxFrameType)
    return strRxFrameType

def CTTF_1X_RLP_ParseFchFrameInfo(infile, outfile, type):
    #############################################################################################################
    #   1X RLP FCHFrame信息结构
    #   VOS_UINT8                               aucFchFrame[22]
    #   VOS_UINT16                              usFchBitSize
    #############################################################################################################
    outfile.write('%s Fch Data : \n' % type)
    for i in range(22):
        ucFchFrame = struct.unpack('B', infile.read(1))
        if ((i == 10) or (i == 21)):
            outfile.write('%02x \n' % ucFchFrame)
        else:
            outfile.write('%02x ' % ucFchFrame)
    usFchBitSize = struct.unpack('H', infile.read(2))
    out_str = 'FchBitSize : %d \n' % usFchBitSize
    outfile.write(out_str)

def CTTF_1X_RLP_ParseRRlpTxSchFrameInfo(infile, outfile):
    #############################################################################################################
    #   1X RLP RSCHFrame信息结构
    #   VOS_UINT16                              usLSeq
    #   VOS_UINT16                              usTxBitLen
    #   VOS_UINT8                               ucTxFrameType
    #   VOS_UINT8                               aucReserve[3]
    #############################################################################################################
    usLSeq, usTxBitLen, ucTxFrameType, _, _, _ = struct.unpack('2H4B', infile.read(8))
    strLSeq = str(usLSeq)
    strTxBitLen = str(usTxBitLen)
    strTxFrameType = CTTF_1X_MAC_GetTxFrameTypeStr(ucTxFrameType)
    out_str = '%-8s %-10s %-15s \n' % (strLSeq, strTxBitLen, strTxFrameType)
    outfile.write(out_str)
    
def CTTF_1X_RLP_ParseRRlpTxFrameInfo(infile, outfile):
    #############################################################################################################
    #   1X RLP TX信息结构
    #   CTTF_1X_RLP_MNTN_DUMP_FCH_FRAME_STRU    stTxFchFrame
    #   VOS_UINT32                              ulValidSchPdu
    #   CTTF_1X_RLP_MNTN_DUMP_RSCH_FRAME_STRU   astTxSchFrame[8]
    #############################################################################################################
    CTTF_1X_RLP_ParseFchFrameInfo(infile, outfile, 'Tx')
    ulValidSchPdu = struct.unpack('I', infile.read(4))
    out_str = 'ValidSchPdu : %d \n' % ulValidSchPdu
    outfile.write(out_str)
    outfile.write('%-8s %-10s %-15s \n' % ('LSeq', 'TxBitLen', 'TxFrameType'))
    for i in range(8):
        CTTF_1X_RLP_ParseRRlpTxSchFrameInfo(infile, outfile)

def CTTF_1X_RLP_ParseRRlpTxInfo(infile, outfile):
    #############################################################################################################
    #   1X RLP TX信息结构
    #   VOS_UINT32                              ulSduBo
    #   VOS_UINT16                              usL_Vs
    #   VOS_UINT8                               ucRSchStatus
    #   VOS_UINT8                               ucReserve
    #   CTTF_1X_RLP_MNTN_DUMP_TX_FRAME_STRU     stTxFrame
    #############################################################################################################
    ulSduBo, usL_Vs, ucRSchStatus, _ = struct.unpack('IH2B', infile.read(8))
    outfile.write('****************RRlpTxInfo****************\n')
    out_str = 'SduBo : %d \n' % ulSduBo
    outfile.write(out_str)
    out_str = 'L_Vs : %d \n' % usL_Vs
    outfile.write(out_str)
    strRSchStatus = CTTF_1X_MAC_GetRSchStateStr(ucRSchStatus)
    out_str = 'RSchStatus : %s \n' % strRSchStatus
    outfile.write(out_str)
    CTTF_1X_RLP_ParseRRlpTxFrameInfo(infile, outfile)

def CTTF_1X_RLP_ParseFRlpRxSchFrameInfo(infile, outfile):
    #############################################################################################################
    #   1X RLP FSCHFrame信息结构
    #   VOS_UINT8                               ucSeqHi
    #   VOS_UINT8                               ucSeq
    #   VOS_UINT8                               ucRxFrameType
    #   VOS_UINT8                               aucReserve[3]
    #   VOS_UINT16                              usRxBitLen
    #############################################################################################################
    ucSeqHi, ucSeq, ucRxFrameType, _, _, _, usRxBitLen = struct.unpack('6BH', infile.read(8))
    strSeqHi = str(ucSeqHi)
    strSeq = str(ucSeq)
    strRxFrameType = CTTF_1X_MAC_GetRxFrameTypeStr(ucRxFrameType)
    strRxBitLen = str(usRxBitLen)
    out_str = '%-5s %-5s %-5s %-15s \n' % (strSeqHi, strSeq, strRxBitLen, strRxFrameType)
    outfile.write(out_str)

def CTTF_1X_RLP_ParseFRlpRxFrameInfo(infile, outfile):
    #############################################################################################################
    #   1X RLP RX信息结构
    #   CTTF_1X_RLP_MNTN_DUMP_FCH_FRAME_STRU    stRxFchFrame
    #   VOS_UINT32                              ulValidSchPdu
    #   CTTF_1X_RLP_MNTN_DUMP_FSCH_FRAME_STRU   astRxSchFrame[8]
    #############################################################################################################
    CTTF_1X_RLP_ParseFchFrameInfo(infile, outfile, 'Rx')
    ulValidSchPdu = struct.unpack('I', infile.read(4))
    out_str = 'ValidSchPdu : %d \n' % ulValidSchPdu
    outfile.write(out_str)
    outfile.write('%-5s %-5s %-5s %-15s \n' % ('SeqHi', 'Seq', 'RxBitLen', 'RxFrameType'))
    for i in range(8):
        CTTF_1X_RLP_ParseFRlpRxSchFrameInfo(infile, outfile)

def CTTF_1X_RLP_ParseFRlpRxInfo(infile, outfile):
    #############################################################################################################
    #   1X RLP RX信息结构
    #   VOS_UINT16                              usL_Vn
    #   VOS_UINT16                              usL_Vr
    #   VOS_UINT16                              usL_Vnpeer
    #   VOS_UINT8                               ucReserve[2]
    #   CTTF_1X_RLP_MNTN_DUMP_RX_FRAME_STRU     stRxFrame
    #############################################################################################################
    usL_Vn, usL_Vr, usL_Vnpeer, _, _ = struct.unpack('3H2B', infile.read(8))
    outfile.write('****************FRlpRxInfo****************\n')
    out_str = 'L_Vn : %d \n' % usL_Vn
    outfile.write(out_str)
    out_str = 'L_Vr : %d \n' % usL_Vr
    outfile.write(out_str)
    out_str = 'L_Vnpeer : %d \n' % usL_Vnpeer
    outfile.write(out_str)
    CTTF_1X_RLP_ParseFRlpRxFrameInfo(infile, outfile)

def CTTF_1X_RLP_ParseRlpLinkInfo(infile, outfile):
    link_lable = {
        0 : 'SHAREQ_CONTROL_LINK',
        1 : 'SHAREQ_NAK_FROM_BS_LINK',
        2 : 'SHAREQ_NAK_TO_BS_LINK',
        3 : 'SDUQ_NOTRANS_PRI0_LINK',
        4 : 'SDUQ_NOTRANS_PRI1_LINK',
        5 : 'SDUQ_NOTRANS_PRI2_LINK',
        6 : 'SDUQ_NOTRANS_PRI3_LINK',
        7 : 'SDUQ_NOTRANS_PRI4_LINK',
        8 : 'SDUQ_TRANSMITTING_LINK',
        9 : 'SDU_BUFF_LINK',
        10 : 'REXMITQ_LINK',
        11 : 'NAKTOBS_MGMT_LINK',
        12 : 'RESEQUENCE_MGMT_LINK',
    }
    outfile.write('****************RlpLinkInfo****************\n')
    for i in range(CTTF_1X_RLP_MNTN_DUMP_MAX_LINK_NUM):
        ulLinkCnt = struct.unpack('I', infile.read(4))[0]
        outfile.write('%-25s : %d \n' % (link_lable[i], ulLinkCnt))

def CTTF_1X_RLP_ParseDumpInfo(infile, outfile, usDataLen):
    if usDataLen != 252:
        outfile.write('please Update The 1X RLP Parse Struct')
        return False
    #############################################################################################################
    #   1X RLP DUMP信息结构
    #   CTTF_1X_RLP_MNTN_DUMP_TX_STATUS_STRU    stRRlpTxInfo
    #   CTTF_1X_RLP_MNTN_DUMP_RX_STATUS_STRU    stFRlpRxInfo
    #   CTTF_1X_RLP_MNTN_DUMP_LINK_STATUS_STRU  astRlpLinkInfo[CTTF_1X_RLP_MNTN_DUMP_LINK_BUTT]
    #############################################################################################################
    outfile.write('------------------------------------1x Rlp Dump Info Start----------------------------------------\n')
    CTTF_1X_RLP_ParseRRlpTxInfo(infile, outfile)
    CTTF_1X_RLP_ParseFRlpRxInfo(infile, outfile)
    CTTF_1X_RLP_ParseRlpLinkInfo(infile, outfile)
    outfile.write('------------------------------------1x Rlp Dump Info End-------------------------------------------\n')

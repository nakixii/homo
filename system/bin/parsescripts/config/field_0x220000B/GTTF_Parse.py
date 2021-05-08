#!/usr/bin/env python3
# coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2018 - 2019 Hisilicon Technoligies Co., Ltd.
# * Filename      GTTF_Parse.py
# * Description   parse Gttf Dump Info
# * Version       1.0
# * Data          2018-01-4 create file
#***********************************************************************
import struct

GTTF_MNTN_GRM_RECORD_MAX_MSG = 20
GTTF_MNTN_GRM_RECORD_MAX_DL_DATA = 30
GTTF_MNTN_GRM_RECORD_MAX_SEND_GMM_DATA = 20

GTTF_MNTN_GRM_RECOED_MAX_DL_DATA_LEN = 14
GTTF_MNTN_LLC_RECOED_MAX_SEND_GMM_DATA_LEN = 4

gttf_pid_enum_table = {
    1   : "TIMER",
    148   : "TC",
    35  : "I1_TC",
    238   : "I2_TC",	
    130  : "GRM",
    24  : "I1_GRM",
    258  : "I2_GRM",
    128  : "GAS",
    28  : "I1_GAS",
    262  : "I2_GAS",
    131  : "LL",
    26  : "I1_LL",
    260  : "I2_LL",
    205  : "GPHY",
    44  : "I1_GPHY",
    263  : "I2_GPHY",
}


gttf_gas_grm_msg_enum_table = {
    0x1	    : 'ID_CGRM_UL_SETUP_REQ',
    0x3	    : 'ID_CGRM_DL_SETUP_REQ',
    0x5	    : 'ID_CGRM_UL_CHANGE_REQ',
    0x7	    : 'ID_CGRM_DL_CHANGE_REQ',
    0x9	    : 'ID_CGRM_SUSPEND_REQ',
    0xB	    : 'ID_CGRM_RESUME_REQ',
    0xD	    : 'ID_CGRM_UL_RELEASE_REQ',
    0xF	    : 'ID_CGRM_DL_RELEASE_REQ',
    0x31	: 'ID_CGRM_UL_CLEAR_DATA_REQ',
    0x36	: 'ID_CGRM_GPRS_UL_ACK',
    0x40	: 'ID_CGRM_CTRL_MSG_RRBP_REQ',
    0x42	: 'ID_CGRM_EGPRS_UL_ACK',
    0x43	: 'ID_CGRM_INFO_UPDATE_REQ',
    0x45	: 'ID_CGRM_TLLI_UPDATE_REQ',
    0x47	: 'ID_CGRM_STOP_TX_REQ',
    0x48	: 'ID_CGRM_INIT_TX_REQ',
    0x55	: 'ID_CGRM_GRR_TBF_EST_FAIL_IND',
    0x56	: 'ID_CGRM_GRR_DRX_PARA_IND',
}

gttf_gphy_grm_msg_enum_table = {
    0x7501	: 'ID_PHP_DL_START_TIME_IND',
    0x7502	: 'ID_PHP_PACKET_DATA_IND',
    0x7503	: 'ID_PHP_PACKET_SEND_IND',
    0x7505	: 'ID_PHP_RRBP_MSG_CNF',
    0x7506	: 'ID_PHP_UL_START_TIME_IND',
    0x7507	: 'ID_PHY_RRBP_FN_IND',
    0x7508	: 'ID_PHY_EGPRS_SRB_CNF',
}

gttf_ll_grm_msg_enum_table = {
    0x120	: 'ID_GRLC_DATA_REQ',
    0x121	: 'ID_GRLC_UNITDATA_REQ',
    0x1120	: 'ID_TRACE_GRLC_DATA_REQ',
    0x1121	: 'ID_TRACE_GRLC_UNITDATA_REQ',
    0x124	: 'ID_CGRLC_ABORT_REQ',
    0x125	: 'ID_CGRLC_SUSPEND_REQ',
    0x126	: 'ID_CGRLC_RESUME_REQ',
    0x127	: 'ID_CGRLC_CLEAR_LL_PDU_REQ',
    0x128	: 'ID_LL_TLLI_STATE_IND',
}

gttf_tc_grm_msg_enum_table = {
    0x3C	: 'ID_GRM_GTM_SETUP_REQ',
    0x3F	: 'ID_GRM_GTM_REL_RSP',
    0x4C	: 'ID_GRM_SRB_SETUP_REQ',
    0x4F	: 'ID_GRM_SRB_REL_RSP'
}


def Is_GasPid(pid):
    state_table = {
    128  : "GAS",
    28  : "I1_GAS",
    262  : "I2_GAS",
    }
    
    if pid in state_table:
        return True
    else:
        return False


def Is_GrmPid(pid):
    state_table = {
    130  : "GRM",
    24  : "I1_GRM",
    258  : "I2_GRM",
    }
    
    if pid in state_table:
        return True
    else:
        return False


def Is_GphyPid(pid):
    state_table = {
    205  : "GPHY",
    44  : "I1_GPHY",
    263  : "I2_GPHY",
    }
    
    if pid in state_table:
        return True
    else:
        return False


def Is_LlPid(pid):
    state_table = {
    131  : "LL",
    26  : "I1_LL",
    260  : "I2_LL",
    }
    
    if pid in state_table:
        return True
    else:
        return False


def Is_TcPid(pid):
    state_table = {
    148   : "TC",
    35  : "I1_TC",
    238   : "I2_TC",
    }
    
    if pid in state_table:
        return True
    else:
        return False
		
def Is_TimerPid(pid):
    if pid == 1:
        return True
    else:
        return False		

def getGasMsgId(msgid):
    if msgid in gttf_gas_grm_msg_enum_table:
        return gttf_gas_grm_msg_enum_table[msgid]
    else:
        return "none"
		
def getGphyMsgId(msgid):
    if msgid in gttf_gphy_grm_msg_enum_table:
        return gttf_gphy_grm_msg_enum_table[msgid]
    else:
        return "none"

def getLlMsgId(msgid):
    if msgid in gttf_ll_grm_msg_enum_table:
        return gttf_ll_grm_msg_enum_table[msgid]
    else:
        return "none"

def getTcMsgId(msgid):
    if msgid in gttf_tc_grm_msg_enum_table:
        return gttf_tc_grm_msg_enum_table[msgid]
    else:
        return "none"		

def TTF_GetMsgIdStr(ulsendPid,usMsgId):
    if Is_GasPid(ulsendPid):
        strMsgId = getGasMsgId(usMsgId)
    elif  Is_GphyPid(ulsendPid):
        strMsgId = getGphyMsgId(usMsgId)
    elif  Is_LlPid(ulsendPid):
        strMsgId = getLlMsgId(usMsgId)	
    elif  Is_TcPid(ulsendPid):
        strMsgId = getTcMsgId(usMsgId)	
    elif  Is_TimerPid(ulsendPid):
        strMsgId = 'Gttf_Timerout'		
    else:
        strMsgId = "none"
		
    return strMsgId

def TTF_GetPidStr(ucPid):
    if ucPid in gttf_pid_enum_table:
        strPid = gttf_pid_enum_table[ucPid]
    else:    
        strPid = "none"
    return strPid

def GTTF_GetULTbfState(ucUlTbfState):
    state_table = {
        0x01 : 'IDLE',
        0x02 : 'SETUP_WAIT',
        0x04 : 'ACTIVE',
        0x08 : 'CHANGE_WAIT',
        0x10 : 'SUSPEND',
        0x20 : 'STOP'
    }
    if ucUlTbfState in state_table:
        strUlTbfState = state_table[ucUlTbfState]
    else:
        strUlTbfState = str(ucUlTbfState)
    return strUlTbfState
	
def GTTF_GetULTbfMode(Tbfmode):
    state_table = {
        0 : 'NonExtend',
        1 : 'Extend'
    }
    if Tbfmode in state_table:
        strTbfmode = state_table[Tbfmode]
    else:
        strTbfmode = str(Tbfmode)
    return strTbfmode


def GTTF_GetULSuspendType(suspendtype):
    state_table = {
        0 : 'NULL',
        1 : 'USER_DATA',
		2 : 'ALL_DATA'
    }
    if suspendtype in state_table:
        strUlSuspendType = state_table[suspendtype]
    else:
        strUlSuspendType = str(suspendtype)
    return strUlSuspendType

   
def GTTF_GetDLTbfState(ucDlTbfState):
    state_table = {
        0x01 : 'IDLE',
        0x02 : 'ACTIVE',
        0x04 : 'SUSPEND'
    }
    if ucDlTbfState in state_table:
        strDlTbfState = state_table[ucDlTbfState]
    else:
        strDlTbfState = str(ucDlTbfState)
    return strDlTbfState
	
def GTTF_GetTbfMode(Tbfmode):
    state_table = {
        0 : 'GPRS',
        1 : 'EGPRS',
        2 : 'NULL'
    }
    if Tbfmode in state_table:
        strTbfmode = state_table[Tbfmode]
    else:
        strTbfmode = str(Tbfmode)
    return strTbfmode

def GTTF_ParseGrmInfo(infile, outfile):
    #############################################################################################################
    #   GrmInfo info
    #   /* ul tbf info */
    #   VOS_UINT8                                   ucUlState
    #   VOS_UINT8                                   enUlTbfmode
    #   VOS_UINT8                                   ucUlErrProcMask
    #   VOS_UINT8                                   enUlSuspendType
    #
    #   VOS_UINT16                                  usSduRcvQcnt
    #   VOS_UINT16                                  usSduWatiResQcnt
    #   VOS_UINT16                                  usSduSuspendQcnt
    #   VOS_UINT16                                  usSduTempQcnt
    #
    #   /* dl tbf info */
    #   VOS_UINT8                                   ucDlState
    #   VOS_UINT8                                   enDlTbfmode
    #   VOS_UINT8                                   ucDlErrProcMask
    #   VOS_UINT8                                   ucDLStateBeforeSuspend
    #############################################################################################################
	#usRMacState, usServiceOption, enFchFlag, enSchFlag, ucFchState, ucSchState = struct.unpack('2H4B', infile.read(8))
    ucUlState, enUlTbfmode, ucUlErrProcMask, enUlSuspendType = struct.unpack('4B', infile.read(4))
    outfile.write('****************UL TBF INFO ****************\n')
    strUlState = GTTF_GetULTbfState(ucUlState)
    out_str = 'UL_STATE:        %s \n' % strUlState
    outfile.write(out_str)
    
    strUlTbfmode = GTTF_GetULTbfMode(enUlTbfmode)
    out_str = 'UL_TBF_Mode:     %s \n' % strUlTbfmode
    outfile.write(out_str)  
    
    out_str = 'UlErrProcMask:   %d \n' % ucUlErrProcMask
    outfile.write(out_str)  
    
    strUlSuspendType = GTTF_GetULSuspendType(enUlSuspendType)
    out_str = 'UL_Suspend_Type: %s \n' % strUlSuspendType
    outfile.write(out_str)  
    
    usSduRcvQcnt, usSduWatiResQcnt, usSduSuspendQcnt, usSduTempQcnt = struct.unpack('4H', infile.read(2*4))
    out_str = 'usSduRcvQcnt:     %d \nusSduWatiResQcnt: %d\nusSduSuspendQcnt: %d\nusSduTempQcnt:    %d \n' % (usSduRcvQcnt, usSduWatiResQcnt, usSduSuspendQcnt, usSduTempQcnt)
    outfile.write(out_str)  
    
    ucDlState, enDlTbfmode, ucDlErrProcMask, ucDLStateBeforeSuspend = struct.unpack('4B', infile.read(4))
    outfile.write('\n****************DL TBF INFO ****************\n')
    strDlState = GTTF_GetDLTbfState(ucDlState)
    out_str = 'DL_STATE:                %s \n' % strDlState
    outfile.write(out_str)
    
    strDlTbfmode = GTTF_GetTbfMode(enDlTbfmode)
    out_str = 'DL_TBF_Mode:             %s \n' % strDlTbfmode
    outfile.write(out_str)  
    
    out_str = 'DlErrProcMask:           %d \n' % ucDlErrProcMask
    outfile.write(out_str)  
    
    strDLStateBeforeSuspend = GTTF_GetDLTbfState(ucDLStateBeforeSuspend)
    out_str = 'DL_STATE_BEFORE_SUSPEND: %s \n' % strDLStateBeforeSuspend
    outfile.write(out_str)
	
def GTTF_ParseGrmRecordMsg(infile):
    #############################################################################################################
    #   Grm Record msg struct
    #   VOS_UINT32                              usSenderPid
    #   VOS_UINT32                              usReeiverPid
    #   VOS_UINT16                              usTick
    #   VOS_UINT16                              usMsgId
    #############################################################################################################
    usSenderPid, usReciverPid, usTick,usMsgId = struct.unpack('2I2H', infile.read(12))
    strSenderPid = TTF_GetPidStr(usSenderPid)
    strReciverPid = TTF_GetPidStr(usReciverPid)
    StrMsgId = TTF_GetMsgIdStr(usSenderPid, usMsgId)
    return strSenderPid, strReciverPid, usTick, StrMsgId
	
def GTTF_ParseGrmOneDlData(infile,outfile):
    #############################################################################################################
    #   Grm Dl Data struct
    #   VOS_UINT16                              usTick
    #   VOS_UINT16                              usBsn
    #   VOS_UINT8                               ucDataLen
    #   VOS_UINT8                               ucRsv
    #   VOS_UINT8                               aucData[GTTF_MNTN_GRM_RECOED_MAX_DL_DATA_LEN]
    #############################################################################################################
    usTick, usBsn, ucDataLen, _, = struct.unpack('2H2B', infile.read(6))
    outfile.write('%-10s %-10s %-10s' % (usTick, usBsn, ucDataLen))
    
    for i in range(GTTF_MNTN_GRM_RECOED_MAX_DL_DATA_LEN):
        data = struct.unpack('B', infile.read(1))
        outfile.write('%02x ' % data)
    outfile.write('\n')
	
def GTTF_ParseLltoGmmOneDlData(infile,outfile):
    #############################################################################################################
    #   Ll to Gmm DlData struct
    #   VOS_UINT16                              usTick
    #   VOS_UINT16                              usDataLen
    #   VOS_UINT8                               aucData[GTTF_MNTN_LLC_RECOED_MAX_SEND_GMM_DATA_LEN]
    #############################################################################################################
    usTick, ucDataLen, = struct.unpack('2H', infile.read(4))
    outfile.write('%-12s %-12s' % (usTick, ucDataLen))
    
    aucData = struct.unpack('4B', infile.read(4))
    outfile.write(' %02x %02x %02x %02x\n' % aucData)

	
def GTTF_ParseGrmGetMsg(infile, outfile,index):	
    outfile.write('\n+++++++++++++++++ ParseGrmRecordMsg Start  +++++++++++++++++ \n')
    outfile.write('The start index: %d\n' % index)
    outfile.write('%-12s %-12s %-20s %-30s \n' % ('SenderPid', 'ReceiverPid', 'Tick', 'MsgId'))
    for i in range(GTTF_MNTN_GRM_RECORD_MAX_MSG):
        stOneRecordMsg = GTTF_ParseGrmRecordMsg(infile)
        outfile.write('%-12s %-12s %-20s %-30s \n' % stOneRecordMsg)
    outfile.write('+++++++++++++++++ ParseGrmRecordMsg End  +++++++++++++++++ \n')
	
def GTTF_ParseGrmDlData(infile, outfile,index):	
    outfile.write('\n+++++++++++++++++ ParseGrmDlData Start  +++++++++++++++++ \n')
    outfile.write('The start index: %d\n' % index)
    outfile.write('%-10s %-10s %-10s %-50s \n' % ('Tick', 'Bsn', 'Length', 'Data'))
    for i in range(GTTF_MNTN_GRM_RECORD_MAX_DL_DATA):
        stOneRecordMsg = GTTF_ParseGrmOneDlData(infile,outfile)
    outfile.write('+++++++++++++++++ ParseGrmDlData End  +++++++++++++++++ \n')
		
def GTTF_ParseLlToGmmData(infile, outfile,index):	
    outfile.write('\n+++++++++++++++++ ParseLlToGmmData Start  +++++++++++++++++ \n')
    outfile.write('The start index: %d\n' % index)
    outfile.write('%-12s %-12s %-20s \n' % ('Tick', 'Length', 'Data'))
    for i in range(GTTF_MNTN_GRM_RECORD_MAX_SEND_GMM_DATA):
        GTTF_ParseLltoGmmOneDlData(infile,outfile)
    outfile.write('+++++++++++++++++ ParseLlToGmmData End  +++++++++++++++++ \n')

def GTTF_ParseDumpInfo(infile, outfile, usDataLen):
    if usDataLen != 1020:
        outfile.write('GTTF_ParseDumpInfo struct len is %d\n' %usDataLen)
        return False
    #############################################################################################################
    #   GTTF DUMP info
    #   GRM_MNTN_GRM_INFO_RECORD                stGrmInfoRecord;
    #   VOS_UINT8                               ucGrmMsgIdx
    #   VOS_UINT8                               ucGrmDlDataIdx
    #   VOS_UINT8                               ucLLCDataIdx
    #   VOS_UINT8                               ucRsv
    #   GRM_MNTN_GRM_GET_MSG_RECORD             stGrmInfoRecord;
    #   GRM_MNTN_GRM_GET_DL_DATA_RECORD         stGrmInfoRecord;
    #   GRM_MNTN_LLC_TO_GMM_DL_DATA_RECORD      stGrmInfoRecord;
    #############################################################################################################
    outfile.write('------------------------------------Gttf I0 Dump Info Start----------------------------------------\n')
    GTTF_ParseGrmInfo(infile, outfile)
    ucGrmMsgIdx, ucGrmDlDataIdx,ucLLCDataIdx,_ = struct.unpack('4B', infile.read(4))
    GTTF_ParseGrmGetMsg(infile, outfile, ucGrmMsgIdx)
    GTTF_ParseGrmDlData(infile, outfile, ucGrmDlDataIdx)
    GTTF_ParseLlToGmmData(infile, outfile,ucLLCDataIdx)
    outfile.write('------------------------------------Gttf I0 Dump Info End-------------------------------------------\n')
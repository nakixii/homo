#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   analysis guas dump bin
modify  record  :   2016-01-22 create file
"""

import struct
import os
import sys
import string
from cas_pid import *
from cnas_cas_1x_msg import *
from cnas_cas_hrpd_msg import *
from cas_fsm import *
from cas_cproc_hrpd_msg import *
from cas_lte_hrpd_msg import *
from cas_cttf_hrpd_msg import *
from cas_cttf_1x_msg import *
from cas_cproc_1x_msg import *
from ps_rrm_msg       import *
from cas_1x_hrpd_msg import *
from cas_timer_msg import *
from cas_other_msg import *

MACRO_CAS_MNTN_MAX_HANDLED_MSG_SAVE_NUM              = 100
MACRO_CAS_MNTN_MAX_INQUEUE_MSG_SAVE_NUM              = 20
MACRO_CAS_1X_MNTN_LOG_HANDLED_MSG_SAVE_INFO_SIZE     = 16
MACRO_CAS_MNTN_LOG_INQUEUE_MSG_SAVE_INFO_SIZE        = 8
MACRO_CAS_HRPD_MNTN_LOG_HANDLED_MSG_SAVE_INFO_SIZE   = 20
MACRO_CAS_HRPD_MNTN_OTA_CODEC_MAX_LENGTH             = 300

def get_pid_file(): 
    dirname = ''
    path = sys.path[0] 
    if os.path.isdir(path): 
        dirname =  path
    elif os.path.isfile(path): 
        dirname = os.path.dirname(path) 

    field_dir = dirname + '\\field_0x2200008\\PidTable.xls'
    if not os.path.exists(field_dir):
        return ''
        
    return field_dir
        
def get_msg_file(): 
    dirname = ''
    path = sys.path[0] 
    if os.path.isdir(path): 
        dirname =  path
    elif os.path.isfile(path): 
        dirname = os.path.dirname(path) 

    field_dir = dirname + '\\field_0x2200008\\TraceTable.xls'
    if not os.path.exists(field_dir):
        return ''
        
    return field_dir

"""    
def cas_get_pid_str( pid, outstream):

    dirname = get_pid_file()
    #outstream.writelines(["%-15s\n" % (dirname)])

    try:    
        data  = xlrd.open_workbook(dirname)
        
        table = data.sheet_by_index(0)
        #outstream.writelines(["pid table nrows = %d\n" % (table.nrows)])
        for i in range(table.nrows):
            if pid == table.row_values(i)[1]:
                return table.row_values(i)[0]
    except:
        return "none"
"""

"""
def cas_get_msgstrbymsgid( Sendpid, Rcvpid, usMsgId, outstream):

    dirname = get_msg_file()
    #outstream.writelines(["%-15s\n" % (dirname)])

    try:     
        data  = xlrd.open_workbook(dirname)
        table = data.sheet_by_index(0)
        #outstream.writelines(["msg table nrows = %d\n" % (table.nrows)])
        for i in range(table.nrows):
            if (Sendpid == table.row_values(i)[0] and Rcvpid == Rcvpid.row_values(i)[1] and usMsgId == eval(Rcvpid.row_values(i)[2])):
                return table.row_values(i)[3]
    except:
        return "none"

def cas_get_msg_string_by_msgid( Sendpid, Rcvpid, usMsgId, outstream):

    dirname = get_msg_file()
    #outstream.writelines(["%-15s\n" % (dirname)])

    try:     
        data  = xlrd.open_workbook(dirname)
        table = data.sheet_by_index(0)
        #outstream.writelines(["msg table nrows = %d\n" % (table.nrows)])
        #outstream.writelines(["table.row_values(42)[0] = %s  table.row_values(42)[1] = %s  table.row_values(42)[2] = %s\n" % (table.row_values(42)[0], table.row_values(42)[1], table.row_values(42)[2])])

        #outstream.writelines(["type(Sendpid) = %s \n" % (type(Sendpid))])
        #outstream.writelines(["type(table.row_values(42)[0]) = %s \n" % (type(table.row_values(42)[0]))])       
        for i in range(table.nrows):
            if (Sendpid == table.row_values(i)[0]):
            #outstream.writelines(["Sendpid = %s table.row_values(42)[0] = %s\n" % (Sendpid, table.row_values(42)[0])]) 
                if Rcvpid == table.row_values(i)[1]:
                #outstream.writelines(["Rcvpid = %s table.row_values(42)[1] = %s\n" % (Rcvpid, table.row_values(42)[1])]) 
                    if  usMsgId == eval(table.row_values(i)[2]):
                    #outstream.writelines(["usMsgId = %s table.row_values(42)[2] = %s\n" % (usMsgId, table.row_values(42)[2])])
                        return table.row_values(i)[3]
    except:
        return "none"        
 """ 
 
def cas_get_msg_string_by_msgid( pid1, pid2, usMsgId, outstream):
        if ( (pid1.upper() in ['1XCASM', ]) and (pid2.upper() in ['XSD', 'XCC', 'XREG', 'XSMS', 'USIM'])):
                 return get_cnas_cas_1x_msg_str(usMsgId)

        elif ( (pid1.upper() in ['OM']) or (pid2.upper() in ['OM'])):
                return get_cas_other_msg_str(usMsgId)
				 
        elif ( (pid1.upper() in ['RRM']) and (pid2.upper() in ['1XCASM', 'HALMP'])):
                 return get_ps_rrm_msg_str(usMsgId) 
                 
        elif ( (pid2.upper() in ['RRM']) and (pid1.upper() in ['1XCASM', 'HALMP'])):
                 return get_ps_rrm_msg_str(usMsgId)
                 
        elif ( (pid2.upper() in ['1XCASM', ]) and (pid1.upper() in ['XSD', 'XCC', 'XREG', 'XSMS', 'USIM'])):
                 return get_cnas_cas_1x_msg_str(usMsgId)
        
        elif ( (pid1.upper() in ['HSD', 'HSM', 'EHSM', 'HLU']) and (pid2.upper() in ['HALMP', 'HSP', 'HRUP', 'HSCP'])):
                 return get_cnas_cas_hrpd_msg_str(usMsgId)

        elif ( (pid2.upper() in ['HSD', 'HSM', 'EHSM', 'HLU']) and (pid1.upper() in ['HALMP', 'HSP', 'HRUP', 'HSCP'])):
                 return get_cnas_cas_hrpd_msg_str(usMsgId) 

        elif ( (pid1.upper() in ['HRPD_CM', 'HRPD_SM']) and (pid2.upper() in ['HALMP', 'HSP', 'HRUP', 'HSCP'])):
                 return get_cas_cproc_hrpd_msg_str(usMsgId) 

        elif ( (pid2.upper() in ['HRPD_CM', 'HRPD_SM']) and (pid1.upper() in ['HALMP', 'HSP', 'HRUP', 'HSCP'])):
                 return get_cas_cproc_hrpd_msg_str(usMsgId) 

        elif ( (pid1.upper() in ['ERMM', 'ERRC']) and (pid2.upper() in ['HALMP', 'HSP', 'HRUP', 'HSCP'])):
                 return get_cas_lte_hrpd_msg_str(usMsgId) 

        elif ( (pid2.upper() in ['ERMM', 'ERRC']) and (pid1.upper() in ['HALMP', 'HSP', 'HRUP', 'HSCP'])):
                 return get_cas_lte_hrpd_msg_str(usMsgId) 

        elif ( (pid1.upper() in ['HRPDRMAC', 'HRPDSIG', 'HRPDRSLP', 'HRPDRSPS', 'HRPDRPA', 'RRM']) and (pid2.upper() in ['HALMP', 'HSP', 'HRUP', 'HSCP'])):
                 return get_cas_cttf_hrpd_msg_str(usMsgId) 

        elif ( (pid2.upper() in ['HRPDRMAC', 'HRPDSIG', 'HRPDRSLP', 'HRPDRSPS', 'HRPDRPA', 'RRM']) and (pid1.upper() in ['HALMP', 'HSP', 'HRUP', 'HSCP'])):
                 return get_cas_cttf_hrpd_msg_str(usMsgId) 

        elif ( (pid1.upper() in ['1XRLAC', '1XRMAC', '1XRRLP', '1XRTESTSO']) and (pid2.upper() in ['1XCASM'])):
                 return get_cas_cttf_1x_msg_str(usMsgId) 
                 
        elif ( (pid2.upper() in ['1XRLAC', '1XRMAC', '1XRRLP', '1XRTESTSO']) and (pid1.upper() in ['1XCASM'])):
                 return get_cas_cttf_1x_msg_str(usMsgId) 

        elif ( (pid1.upper() in ['CPROC_1XCM', 'CPROC_1XSM']) and (pid2.upper() in ['1XCASM', '1XCSRCH', '1XCMEAS'])):
                 return get_cas_cproc_1x_msg_str(usMsgId) 
                 
        elif ( (pid2.upper() in ['CPROC_1XCM', 'CPROC_1XSM']) and (pid1.upper() in ['1XCASM', '1XCSRCH', '1XCMEAS'])):
                 return get_cas_cproc_1x_msg_str(usMsgId)  

        elif ( (pid1.upper() in ['1XCASM', ]) and (pid2.upper() in ['HSP'])):
                 return get_cas_1x_hrpd_msg_str(usMsgId)
                 
        elif ( (pid1.upper() in ['TIMER']) and (pid2.upper() in ['HALMP', 'HSP', 'HRUP', 'HSCP'])):
                 return get_cas_hrpd_timer_msg_str(usMsgId)
                 
        elif ( (pid1.upper() in ['TIMER']) and (pid2.upper() in ['1XCMEAS', '1XCASM', '1XCSRCH'])):
                 return get_cas_1x_timer_msg_str(usMsgId)
                 
        else:
                 #outstream.writelines(["%-50s%-50s%-50d\n" % (pid1.upper(), pid2.upper(), usMsgId)])
                 return get_cas_other_msg_str(usMsgId)

def analysis_cas_1x_mntn_per_handled_msg_info( instream, fileLocalOffset, outstream):
        instream.seek(fileLocalOffset)

        (usTimeStamp,)      = struct.unpack('H', instream.read(2))
        (usSendPid,)        = struct.unpack('H', instream.read(2))
        (usRcvPid,)         = struct.unpack('H', instream.read(2))
        (usMsgId,)          = struct.unpack('H', instream.read(2))

        if (usSendPid == 0 or usRcvPid == 0 or usMsgId == 0):
            return True
            
        (ucFsmId0,)          = struct.unpack('B', instream.read(1))
        (ucMainState0,)      = struct.unpack('B', instream.read(1))
        (ucSubState0,)       = struct.unpack('B', instream.read(1))
        (ucReserved0,)       = struct.unpack('B', instream.read(1))
        
        (ucFsmId1,)          = struct.unpack('B', instream.read(1))
        (ucMainState1,)      = struct.unpack('B', instream.read(1))
        (ucSubState1,)       = struct.unpack('B', instream.read(1))
        (ucReserved1,)       = struct.unpack('B', instream.read(1))

        strSendPid      = cas_get_pid_str(usSendPid, outstream)
        strRcvPid       = cas_get_pid_str(usRcvPid, outstream)
        strMsgId        = cas_get_msg_string_by_msgid( strSendPid, strRcvPid, usMsgId, outstream)
        strSendPid      = '%s(0x%x)' % ( strSendPid, usSendPid)
        strRcvPid       = '%s(0x%x)' % ( strRcvPid, usRcvPid)
        strMsgId        = '%s(0x%x)' % ( strMsgId, usMsgId)
        strTimeStamp    = '%04x'% usTimeStamp
        

        strFsmId0       = cas_1x_get_fsm_id_str(ucFsmId0)
        strMainState0   = cas_1x_get_fsm_main_state_str(ucMainState0)
        strSubState0    = cas_1x_get_fsm_main_state_str(ucSubState0)        
        strFsmId0       = '%s(0x%x)'% (strFsmId0, ucFsmId0)        
        strMainState0   = '%s(0x%x)'% (strMainState0, ucMainState0)
        strSubState0    = '%s(0x%x)'% (strSubState0, ucSubState0)

        strFsmId1       = cas_1x_get_fsm_id_str(ucFsmId1)
        strMainState1   = cas_1x_get_fsm_main_state_str(ucMainState1)
        strSubState1    = cas_1x_get_fsm_substate_str(ucSubState1)
        strFsmId1       = '%s(0x%x)'% (strFsmId1, ucFsmId1)        
        strMainState1   = '%s(0x%x)'% (strMainState1, ucMainState1)
        strSubState1    = '%s(0x%x)'% (strSubState1, ucSubState1)
        
        outstream.writelines(["0x%-18s%-20s%-20s%-70s%-50s%-50s%-50s%-50s%-50s%-50s\n" % (strTimeStamp.upper(), strSendPid, strRcvPid, strMsgId, strFsmId0, strMainState0, strSubState0, strFsmId1, strMainState1, strSubState1)])
        #save2file.writelines(["%-20s%-20s%-20s%-70s%-50s%-50s%-50s%-50s%-50s%-50s\n" % (strTimeStamp.upper(), strSendPid, strRcvPid, strMsgId, strFsmId0, strMainState0, strSubState0, strFsmId1, strMainState1, strSubState1)])

def analysis_cas_mntn_per_inqueue_msg_info( instream, fileLocalOffset, outstream):
        instream.seek(fileLocalOffset)

        (usSendPid,)        = struct.unpack('H', instream.read(2))
        (usRcvPid,)         = struct.unpack('H', instream.read(2))
        (usMsgId,)          = struct.unpack('H', instream.read(2))
        (usReserved0,)      = struct.unpack('H', instream.read(2))

        if (usSendPid == 0 or usRcvPid == 0 or usMsgId == 0):
            return True
            
        strSendPid      = cas_get_pid_str(usSendPid, outstream)
        strRcvPid       = cas_get_pid_str(usRcvPid, outstream)
        strMsgId        = cas_get_msg_string_by_msgid(strSendPid, strRcvPid, usMsgId, outstream)

        strSendPid      = '%s(0x%x)' % ( strSendPid, usSendPid)
        strRcvPid       = '%s(0x%x)' % ( strRcvPid, usRcvPid)
        strMsgId        = '%s(0x%x)' % ( strMsgId, usMsgId)
                
        outstream.writelines(["%-20s%-20s%-60s\n" % (strSendPid, strRcvPid, strMsgId)])
        #save2file.writelines(["%-20s%-20s%-60s\n" % (strSendPid, strRcvPid, strMsgId)])


def analysis_cas_hrpd_mntn_per_handled_msg_info( instream, fileLocalOffset, outstream):
        instream.seek(fileLocalOffset)

        (usTimeStamp,)      = struct.unpack('H', instream.read(2))
        (usSendPid,)        = struct.unpack('H', instream.read(2))
        (usRcvPid,)         = struct.unpack('H', instream.read(2))
        (usMsgId,)          = struct.unpack('H', instream.read(2))

        if (usSendPid == 0 or usRcvPid == 0 or usMsgId == 0):
            return True
            
        (ucFsmId0,)          = struct.unpack('B', instream.read(1))
        (ucMainState0,)      = struct.unpack('B', instream.read(1))
        (ucSubState0,)       = struct.unpack('B', instream.read(1))
        (ucReserved0,)       = struct.unpack('B', instream.read(1))
        
        (ucFsmId1,)          = struct.unpack('B', instream.read(1))
        (ucMainState1,)      = struct.unpack('B', instream.read(1))
        (ucSubState1,)       = struct.unpack('B', instream.read(1))
        (ucReserved1,)       = struct.unpack('B', instream.read(1))

        (ucFsmId2,)          = struct.unpack('B', instream.read(1))
        (ucMainState2,)      = struct.unpack('B', instream.read(1))
        (ucSubState2,)       = struct.unpack('B', instream.read(1))
        (ucReserved2,)       = struct.unpack('B', instream.read(1))
        
        strSendPid      = cas_get_pid_str(usSendPid, outstream)
        strRcvPid       = cas_get_pid_str(usRcvPid, outstream)
        strMsgId        = cas_get_msg_string_by_msgid( strSendPid, strRcvPid, usMsgId, outstream)

        strSendPid      = '%s(0x%x)' % ( strSendPid, usSendPid)
        strRcvPid       = '%s(0x%x)' % ( strRcvPid, usRcvPid)
        strMsgId        = '%s(0x%x)' % ( strMsgId, usMsgId)
        strTimeStamp    = '%04x'% usTimeStamp

        strFsmId0       = cas_hrpd_get_fsm_id_str(ucFsmId0)
        strMainState0   = cas_hrpd_get_fsm_main_state_str(ucMainState0)
        strSubState0    = cas_hrpd_get_fsm_substate_str(ucSubState0)         
        strFsmId0       = '%s(0x%x)'% (strFsmId0, ucFsmId0)        
        strMainState0   = '%s(0x%x)'% (strMainState0, ucMainState0)
        strSubState0    = '%s(0x%x)'% (strSubState0, ucSubState0)

        strFsmId1       = cas_hrpd_get_fsm_id_str(ucFsmId1)
        strMainState1   = cas_hrpd_get_fsm_main_state_str(ucMainState1)
        strSubState1    = cas_hrpd_get_fsm_substate_str(ucSubState1) 
        strFsmId1       = '%s(0x%x)'% (strFsmId1, ucFsmId1)        
        strMainState1   = '%s(0x%x)'% (strMainState1, ucMainState1)
        strSubState1    = '%s(0x%x)'% (strSubState1, ucSubState1)

        strFsmId2       = cas_hrpd_get_fsm_id_str(ucFsmId2)
        strMainState2   = cas_hrpd_get_fsm_main_state_str(ucMainState2)
        strSubState2    = cas_hrpd_get_fsm_substate_str(ucSubState2) 
        strFsmId2       = '%s(0x%x)'% (strFsmId2, ucFsmId2)        
        strMainState2   = '%s(0x%x)'% (strMainState2, ucMainState2)
        strSubState2    = '%s(0x%x)'% (strSubState2, ucSubState2)
        
        outstream.writelines(["0x%-18s%-20s%-20s%-70s%-50s%-50s%-50s%-50s%-50s%-50s%-50s%-50s%-50s\n" % (strTimeStamp.upper(), strSendPid, strRcvPid, strMsgId, strFsmId0, strMainState0, strSubState0, strFsmId1, strMainState1, strSubState1, strFsmId2, strMainState2, strSubState2)])
        #save2file.writelines(["%-20s%-20s%-20s%-70s%-50s%-50s%-50s%-50s%-50s%-50s%-50s%-50s%-50s\n" % (strTimeStamp.upper(), strSendPid, strRcvPid, strMsgId, strFsmId0, strMainState0, strSubState0, strFsmId1, strMainState1, strSubState1, strFsmId2, strMainState2, strSubState2)])


def analysis_cas_1x_handled_msg_dump_info( instream, fileOffset, outstream, ulMsgIndex, ulFirstMsgIndex):
        ulLooper        = ulFirstMsgIndex
        
        outstream.writelines(["%-20s%-20s%-20s%-70s%-50s%-50s%-50s%-50s%-50s%-50s\n" % ("usTimeStamp", "usSendPid", "usReceivePid","usMsgId", "ucFsmId0","ucMainState0","ucSubState0","ucFsmId1","ucMainState1","ucSubState1")])
        #save2file.writelines(["%-20s%-20s%-20s%-70s%-50s%-50s%-50s%-50s%-50s%-50s\n" % ("usTimeStamp", "usSendPid", "usReceivePid","usMsgId", "ucFsmId0","ucMainState0","ucSubState0","ucFsmId1","ucMainState1","ucSubState1")])
        while ulLooper < (MACRO_CAS_MNTN_MAX_HANDLED_MSG_SAVE_NUM + ulFirstMsgIndex):
                ulLooperIndex = ( ulLooper + ulMsgIndex) % MACRO_CAS_MNTN_MAX_HANDLED_MSG_SAVE_NUM
                fileLocalOffset = fileOffset + ulLooperIndex * MACRO_CAS_1X_MNTN_LOG_HANDLED_MSG_SAVE_INFO_SIZE
                analysis_cas_1x_mntn_per_handled_msg_info( instream, fileLocalOffset, outstream)
                ulLooper = ulLooper + 1


def analysis_cas_inqueue_msg_dump_info( instream, fileOffset, outstream, ulMsgIndex):
        ulLooper        = 0
        
        outstream.writelines(["%-20s%-20s%-70s\n" % ("usSendPid", "usReceivePid","usMsgId")])
        while ulLooper < MACRO_CAS_MNTN_MAX_INQUEUE_MSG_SAVE_NUM:
                ulLooperIndex = ( ulLooper + ulMsgIndex) % MACRO_CAS_MNTN_MAX_INQUEUE_MSG_SAVE_NUM
                fileLocalOffset = fileOffset + ulLooperIndex * MACRO_CAS_MNTN_LOG_INQUEUE_MSG_SAVE_INFO_SIZE
                analysis_cas_mntn_per_inqueue_msg_info( instream, fileLocalOffset, outstream)
                ulLooper = ulLooper + 1


def analysis_cas_hrpd_handled_msg_dump_info( instream, fileOffset, outstream, ulMsgIndex, ulFirstMsgIndex):
        ulLooper        = ulFirstMsgIndex
        
        outstream.writelines(["%-20s%-20s%-20s%-70s%-50s%-50s%-50s%-50s%-50s%-50s%-50s%-50s%-50s\n" % ("usTimeStamp", "usSendPid", "usReceivePid","usMsgId", "ucFsmId0","ucMainState0","ucSubState0","ucFsmId1","ucMainState1","ucSubState1","ucFsmId2","ucMainState2","ucSubState2")])
        while ulLooper < (MACRO_CAS_MNTN_MAX_HANDLED_MSG_SAVE_NUM + ulFirstMsgIndex):
                ulLooperIndex = ( ulLooper + ulMsgIndex) % MACRO_CAS_MNTN_MAX_HANDLED_MSG_SAVE_NUM
                fileLocalOffset = fileOffset + ulLooperIndex * MACRO_CAS_HRPD_MNTN_LOG_HANDLED_MSG_SAVE_INFO_SIZE
                analysis_cas_hrpd_mntn_per_handled_msg_info( instream, fileLocalOffset, outstream)
                ulLooper = ulLooper + 1


def analysis_cas_1x_handled_msg_list_dump_info( instream, fileOffset, outstream, ulFirstMsgIndex):
        ulLooperTest = 0

        ##### gunas modem0 #########        
        analysis_cas_1x_handled_msg_dump_info(instream, fileOffset, outstream, ulLooperTest, ulFirstMsgIndex)

        return True        

def analysis_cas_inqueue_msg_list_dump_info( instream, fileOffset, outstream):
        ulLooperTest = 0
 
        ##### one cas 1x handled msg length is 16  #########        
        analysis_cas_inqueue_msg_dump_info(instream, fileOffset, outstream, ulLooperTest)

        return True

def analysis_cas_hrpd_handled_msg_list_dump_info( instream, fileOffset, outstream, ulFirstMsgIndex):
        ulLooperTest = 0

        ##### gunas modem0 #########        
        analysis_cas_hrpd_handled_msg_dump_info(instream, fileOffset, outstream, ulLooperTest, ulFirstMsgIndex)

        return True  

def analysis_cas_hrpd_per_ota_codec_dump_info( instream, fileLocalOffset, outstream):	
    ulLooper = 0
    ulSpace  = 0
	
    instream.seek(fileLocalOffset)

    (usTimeStamp,)      = struct.unpack('H', instream.read(2))
    (usProtocolType,)   = struct.unpack('H', instream.read(2))
    (usMsgBitLen,)      = struct.unpack('H', instream.read(2))
    (ucInstanceType,)   = struct.unpack('B', instream.read(1))
    (enIsFullMsg,)      = struct.unpack('B', instream.read(1))
   
    outstream.writelines(["usTimeStamp:    0x%04X\n" % (usTimeStamp)])
    outstream.writelines(["usProtocolType: %d\n" % (usProtocolType)])
    outstream.writelines(["usMsgBitLen:    %d\n" % (usMsgBitLen)])
    outstream.writelines(["ucInstanceType: %d\n" % (ucInstanceType)])
    outstream.writelines(["enIsFullMsg:    %d\n" % (enIsFullMsg)])
		
    while ulLooper < MACRO_CAS_HRPD_MNTN_OTA_CODEC_MAX_LENGTH:
        (ucData,) = struct.unpack('B', instream.read(1))
        #outstream.writelines(["%02X \n" % (ucData)])
        
        if ulLooper == 0:
            outstream.writelines(["0x%02X " % (ucData)])
		
        elif (ulLooper+1) % 16:
            outstream.writelines(["0x%02X " % (ucData)])
        else:
            outstream.writelines(["0x%02X\n" % (ucData)])
			
        ulLooper = ulLooper + 1

    outstream.writelines(["\n\n"])

def analysis_cas_hrpd_ota_codec_dump_info( instream, fileOffset, outstream):
    ulLooper = 0

    while ulLooper < 2:
        outstream.writelines(["------------ No.%d OTA codec ----------\n" % (ulLooper+1)])
        fileLocalOffset = fileOffset + ulLooper * (MACRO_CAS_HRPD_MNTN_OTA_CODEC_MAX_LENGTH + 8)
        analysis_cas_hrpd_per_ota_codec_dump_info( instream, fileLocalOffset, outstream)
        ulLooper = ulLooper + 1

def analysis_cas_dump_info( infile, offset, outfile):
        instream = infile
        outstream  = outfile
        fileOffset = eval(offset)
        
        #outstream.writelines(["\n**************************** WUMAI:CAS_DUMP_ANALYSIS_2016_03_05_VERSION_1.0 *******************************\n"])
        outstream.writelines(["\n***********************************************************\n"])
        outstream.writelines(["******** CAS DUMP ANALYSIS by CAS Team 20160311 *********\n"])
        outstream.writelines(["***********************************************************\n\n"])
        #outstream.writelines(["Output to txt file: c:\\modem_dump_cas.txt\n\n"])

        #save2file.writelines(["***********************************************************\n"])
        #save2file.writelines(["******** CAS DUMP ANALYSIS by CAS Team 20160311 *********\n"])
        #save2file.writelines(["***********************************************************\n\n"])
        
        ##### analysis cas handled msg #########  
        ##### XXXXXXXXXXXX #########
        instream.seek(fileOffset) 
        (ulRatFlag,)          = struct.unpack('I', instream.read(4))
        (ulHandledMsgIndex,)  = struct.unpack('I', instream.read(4))
        (ulLastMsgTimeSlice,) = struct.unpack('I', instream.read(4))
        strTemp               = 'Magic for 1x: 0x%08X, strLastMsgTimeSlice: 0x%08X '% (ulRatFlag, ulLastMsgTimeSlice)
        outstream.writelines(["%-15s\n" % (strTemp)])
        #save2file.writelines(["%-15s\n" % (strTemp)])
        
        fileOffset = fileOffset + 12  
        outstream.writelines(["\n**************************** 1X:analysis cas handled msg begin! *******************************\n"])
        #save2file.writelines(["\n**************************** 1X:analysis cas handled msg begin! *******************************\n"])
        analysis_cas_1x_handled_msg_list_dump_info( instream, fileOffset, outstream, ulHandledMsgIndex)
        outstream.writelines(["\n**************************** 1X:analysis_cas_dump_info end! *******************************\n"])
        #save2file.writelines(["\n**************************** 1X:analysis_cas_dump_info end! *******************************\n"])

        
        fileOffset = fileOffset + MACRO_CAS_1X_MNTN_LOG_HANDLED_MSG_SAVE_INFO_SIZE * MACRO_CAS_MNTN_MAX_HANDLED_MSG_SAVE_NUM

        instream.seek(fileOffset)
        (ulMsgIDInQueueIndex,)       = struct.unpack('I', instream.read(4))
        strMsgIDInQueueIndex         = '%x'% ulMsgIDInQueueIndex
        #outstream.writelines(["strMsgIDInQueueIndex         %-15s\n" % ( strMsgIDInQueueIndex )])
        fileOffset = fileOffset + 4
        
        outstream.writelines(["\n**************************** 1X:analysis cas inqueue msg begin! *******************************\n"])
        #save2file.writelines(["\n**************************** 1X:analysis cas inqueue msg begin! *******************************\n"])
        analysis_cas_inqueue_msg_list_dump_info( instream, fileOffset, outstream)
        outstream.writelines(["\n**************************** 1X:analysis cas inqueue msg end! *******************************\n\n\n"])
        #save2file.writelines(["\n**************************** 1X:analysis cas inqueue msg end! *******************************\n\n\n"])


        fileOffset = fileOffset + MACRO_CAS_MNTN_LOG_INQUEUE_MSG_SAVE_INFO_SIZE * MACRO_CAS_MNTN_MAX_INQUEUE_MSG_SAVE_NUM

        instream.seek(fileOffset)
        (ulRatFlag,)          = struct.unpack('I', instream.read(4))
        (ulHandledMsgIndex,)  = struct.unpack('I', instream.read(4))
        (ulLastMsgTimeSlice,) = struct.unpack('I', instream.read(4))
        strTemp               = 'Magic for hrpd: 0x%08X, strLastMsgTimeSlice: 0x%08X'% (ulRatFlag, ulLastMsgTimeSlice)
        outstream.writelines(["%-15s\n" % (strTemp)])
        #save2file.writelines(["%-15s\n" % (strTemp)])
        
        fileOffset = fileOffset + 12  
       
        outstream.writelines(["\n**************************** HRPD:analysis cas handled msg begin! *******************************\n"])
        #save2file.writelines(["\n**************************** HRPD:analysis cas handled msg begin! *******************************\n"])
        analysis_cas_hrpd_handled_msg_list_dump_info( instream, fileOffset, outstream, ulHandledMsgIndex)
        outstream.writelines(["\n**************************** HRPD:analysis cas handled msg end! *******************************\n"])
        #save2file.writelines(["\n**************************** HRPD:analysis cas handled msg end! *******************************\n"])


        fileOffset = fileOffset + MACRO_CAS_MNTN_MAX_HANDLED_MSG_SAVE_NUM * MACRO_CAS_HRPD_MNTN_LOG_HANDLED_MSG_SAVE_INFO_SIZE

        instream.seek(fileOffset)
        (ulMsgIDInQueueIndex,)       = struct.unpack('I', instream.read(4))
        strMsgIDInQueueIndex         = '%x'% ulMsgIDInQueueIndex
        #outstream.writelines(["strMsgIDInQueueIndex         %-15s\n" % ( strMsgIDInQueueIndex )])
        fileOffset = fileOffset + 4
        
        outstream.writelines(["\n**************************** HRPD:analysis cas inqueue msg begin! *******************************\n"])
        #save2file.writelines(["\n**************************** HRPD:analysis cas inqueue msg begin! *******************************\n"])
        analysis_cas_inqueue_msg_list_dump_info( instream, fileOffset, outstream)
        outstream.writelines(["\n**************************** HRPD:analysis cas inqueue msg end! *******************************\n"])
        #save2file.writelines(["\n**************************** HRPD:analysis cas inqueue msg end! *******************************\n"])

        # OTA Codec
        fileOffset = fileOffset + MACRO_CAS_MNTN_LOG_INQUEUE_MSG_SAVE_INFO_SIZE * MACRO_CAS_MNTN_MAX_INQUEUE_MSG_SAVE_NUM
		
        instream.seek(fileOffset)
        (ulOtaMsgIndex,)       = struct.unpack('I', instream.read(4))
        strOtaMsgIndex         = '%d' % ulOtaMsgIndex
        fileOffset = fileOffset + 4
        
        outstream.writelines(["\n**************************** HRPD: OTA Codec begin! *******************************\n"])
        #save2file.writelines(["\n**************************** HRPD: OTA Codec begin! *******************************\n"])
        outstream.writelines(["ulOtaMsgIndex: %s\n\n" % ( strOtaMsgIndex )])
        analysis_cas_hrpd_ota_codec_dump_info( instream, fileOffset, outstream)
        outstream.writelines(["\n**************************** HRPD: OTA Codec end! *******************************\n"])
        #save2file.writelines(["\n**************************** HRPD: OTA Codec end! *******************************\n"])
                    
        return True



########################################################################################
def entry_0x2200008(infile, field, offset, len, version, mode, outfile):
        outstream  = outfile

        ########check parameter start#############
        if not field == '0x2200008':
            print ("hidis field is %s." % (field) ) 
            print ("current field is 0x2200008.")
            return error['ERR_CHECK_FIELD']
        elif not version == '0x0000':
            print ("hidis version is %s." % (version) )
            print ("current version is 0x0000.")
            return error['ERR_CHECK_VERSION']
        elif not len == '0x2000':
            print ("hids len is %s." % (len) )
            print ("current len is 0x2000." )
            return error['ERR_CHECK_LEN']
        #########check parameter end##############
        ########outstream.writelines(%(infile, offset, outfile))
        ########outstream.writelines("123456789\n")

        
        ret = analysis_cas_dump_info( infile, offset, outfile)

        #gcas_get_pid_str( 5, outstream)

        #strtemp = get_ps_rrm_msg_str(0x2)
        #outstream.writelines(["strtemp = %s\n"  %(strtemp)])
        #c = msvcrt.getch()
        return 0


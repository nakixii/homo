#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   analysis cnas dump bin
modify  record  :   2018-04-25 create file
"""

import struct
import os
import sys
import string
from cnas_pid import *
from xsd_mscc_msg import *
from xsd_timer_msg import *
from xcc_timer_msg import *
from xreg_timer_msg import *
from ehsm_timer_msg import *
from hsm_timer_msg import *
from hsd_timer_msg import *
from cnas_cas_1x_msg import *
from cnas_cas_hrpd_msg import *
from xsd_xreg_msg import *
from xsd_xcc_msg import *
from xsd_xsd_msg import *
from xsd_taf_msg import *
from xcc_xcc_msg import *
from xcc_mma_msg import *
from xcc_taf_msg import *
from xcc_sms_msg import *
from xcc_lmm_msg import *
from xcc_xpds_msg import *
from xreg_taf_msg import *
from xreg_rrm_msg import *
from hsd_mscc_msg import *
from hsd_hsd_msg import *
from hsd_ehsm_msg import *
from hsd_hlu_msg import *
from hsd_hrm_msg import *
from hsd_hsm_msg import *
from hsd_hsp_msg import *
from hsd_hrup_msg import *
from ehsm_hsm_msg import *
from ehsm_ehsm_msg import *
from ehsm_esm_msg import *
from ehsm_taf_msg import *
from ehsm_pppc_msg import *
from hrm_hlu_msg import *
from hrm_hrpdsig_msg import *
from hsm_hlu_msg import *
from hsm_hrm_msg import *
from hsm_hsm_msg import *
from hsm_hrpdrmac_msg import *
from hlu_hrpdrpa_msg import *

MACRO_NAS_CNAS_MAX_LOG_EVENT_STATE_NUM  = 250
MACRO_NAS_CNAS_MNTN_LOG_MSG_INFO_SIZE   = 16
MACRO_CNAS_HSD_MAX_LOG_EVENT_STATE_NUM  = 100
MACRO_CNAS_HSD_MNTN_LOG_MSG_INFO_SIZE   = 12

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
        
def get_cnas_msgid_str( pid1, pid2, usMsgId):       
        if ( 'xsd' == pid1.lower() and 'mscc' == pid2.lower()):
                return get_xsd_mscc_msg_str(usMsgId)
        elif ( 'mscc' == pid1.lower() and 'xsd' == pid2.lower()):
                return get_xsd_mscc_msg_str(usMsgId)
        elif ( 'xsd' == pid1.lower() and 'i1_mscc' == pid2.lower()):
                return get_xsd_mscc_msg_str(usMsgId)
        elif ( 'i1_mscc' == pid1.lower() and 'xsd' == pid2.lower()):
                return get_xsd_mscc_msg_str(usMsgId)    
        elif ( 'xsd' == pid1.lower() and 'i2_mscc' == pid2.lower()):
                return get_xsd_mscc_msg_str(usMsgId)
        elif ( 'i2_mscc' == pid1.lower() and 'xsd' == pid2.lower()):
                return get_xsd_mscc_msg_str(usMsgId)
                
        elif ( '1xcasm' == pid2.lower()):
                return get_cnas_cas_1x_msg_str(usMsgId)
        elif ( '1xcasm' == pid1.lower()):
                return get_cnas_cas_1x_msg_str(usMsgId)
                
        elif ( 'halmp' == pid2.lower()):
                return get_cnas_cas_hrpd_msg_str(usMsgId)
        elif ( 'halmp' == pid1.lower()):
                return get_cnas_cas_hrpd_msg_str(usMsgId)
                
        elif ( 'xsd' == pid1.lower() and 'timer' == pid2.lower()):
                return get_xsd_timer_msg_str(usMsgId)   
        elif ( 'timer' == pid1.lower() and 'xsd' == pid2.lower()):
                return get_xsd_timer_msg_str(usMsgId)
                
        elif ( 'xcc' == pid1.lower() and 'timer' == pid2.lower()):
                return get_xcc_timer_msg_str(usMsgId)   
        elif ( 'timer' == pid1.lower() and 'xcc' == pid2.lower()):
                return get_xcc_timer_msg_str(usMsgId)
                
        elif ( 'xreg' == pid1.lower() and 'timer' == pid2.lower()):
                return get_xreg_timer_msg_str(usMsgId)  
        elif ( 'timer' == pid1.lower() and 'xreg' == pid2.lower()):
                return get_xreg_timer_msg_str(usMsgId)
                
        elif ( 'ehsm' == pid1.lower() and 'timer' == pid2.lower()):
                return get_ehsm_timer_msg_str(usMsgId)  
        elif ( 'timer' == pid1.lower() and 'ehsm' == pid2.lower()):
                return get_ehsm_timer_msg_str(usMsgId)
                
        elif ( 'hsm' == pid1.lower() and 'timer' == pid2.lower()):
                return get_hsm_timer_msg_str(usMsgId)   
        elif ( 'timer' == pid1.lower() and 'hsm' == pid2.lower()):
                return get_hsm_timer_msg_str(usMsgId)
                
        elif ( 'hsd' == pid1.lower() and 'timer' == pid2.lower()):
                return get_hsd_timer_msg_str(usMsgId)   
        elif ( 'timer' == pid1.lower() and 'hsd' == pid2.lower()):
                return get_hsd_timer_msg_str(usMsgId)
                
        elif ( 'xsd' == pid1.lower() and 'xreg' == pid2.lower()):
                return get_xsd_xreg_msg_str(usMsgId)
        elif ( 'xreg' == pid1.lower() and 'xsd' == pid2.lower()):
                return get_xsd_xreg_msg_str(usMsgId)
                
        elif ( 'xsd' == pid1.lower() and 'xcc' == pid2.lower()):
                return get_xsd_xcc_msg_str(usMsgId)
        elif ( 'xcc' == pid1.lower() and 'xsd' == pid2.lower()):
                return get_xsd_xcc_msg_str(usMsgId)
        
        elif ( 'xsd' == pid1.lower() and 'xsd' == pid2.lower()):
                return get_xsd_xsd_msg_str(usMsgId)
        elif ( 'xsd' == pid1.lower() and 'xsd' == pid2.lower()):
                return get_xsd_xsd_msg_str(usMsgId)
                
        elif ( 'xsd' == pid1.lower() and 'xsd' == pid2.lower()):
                return get_xsd_taf_msg_str(usMsgId)
        elif ( 'xsd' == pid1.lower() and 'xsd' == pid2.lower()):
                return get_xsd_taf_msg_str(usMsgId)
                
        elif ( 'xcc' == pid1.lower() and 'xcc' == pid2.lower()):
                return get_xcc_xcc_msg_str(usMsgId)
        elif ( 'xcc' == pid1.lower() and 'xcc' == pid2.lower()):
                return get_xcc_xcc_msg_str(usMsgId)
                
        elif ( 'xcc' == pid1.lower() and 'mma' == pid2.lower()):
                return get_xcc_mma_msg_str(usMsgId)
        elif ( 'mma' == pid1.lower() and 'xcc' == pid2.lower()):
                return get_xcc_mma_msg_str(usMsgId)
        elif ( 'xcc' == pid1.lower() and 'i1_mma' == pid2.lower()):
                return get_xcc_mma_msg_str(usMsgId)
        elif ( 'i1_mma' == pid1.lower() and 'xcc' == pid2.lower()):
                return get_xcc_mma_msg_str(usMsgId)
        elif ( 'xcc' == pid1.lower() and 'i2_mma' == pid2.lower()):
                return get_xcc_mma_msg_str(usMsgId)
        elif ( 'i2_mma' == pid1.lower() and 'xcc' == pid2.lower()):
                return get_xcc_mma_msg_str(usMsgId)
                
        elif ( 'xcc' == pid1.lower() and 'taf' == pid2.lower()):
                return get_xcc_taf_msg_str(usMsgId)
        elif ( 'taf' == pid1.lower() and 'xcc' == pid2.lower()):
                return get_xcc_taf_msg_str(usMsgId)
        elif ( 'xcc' == pid1.lower() and 'i1_taf' == pid2.lower()):
                return get_xcc_taf_msg_str(usMsgId)
        elif ( 'i1_taf' == pid1.lower() and 'xcc' == pid2.lower()):
                return get_xcc_taf_msg_str(usMsgId)
        elif ( 'xcc' == pid1.lower() and 'i2_taf' == pid2.lower()):
                return get_xcc_taf_msg_str(usMsgId)
        elif ( 'i2_taf' == pid1.lower() and 'xcc' == pid2.lower()):
                return get_xcc_taf_msg_str(usMsgId)
                
        elif ( 'xcc' == pid1.lower() and 'sms' == pid2.lower()):
                return get_xcc_sms_msg_str(usMsgId)
        elif ( 'sms' == pid1.lower() and 'xcc' == pid2.lower()):
                return get_xcc_sms_msg_str(usMsgId)
                
        elif ( 'xcc' == pid1.lower() and 'lmm' == pid2.lower()):
                return get_xcc_lmm_msg_str(usMsgId)
        elif ( 'lmm' == pid1.lower() and 'xcc' == pid2.lower()):
                return get_xcc_lmm_msg_str(usMsgId)
                
        elif ( 'xcc' == pid1.lower() and 'xpds' == pid2.lower()):
                return get_xcc_xpds_msg_str(usMsgId)
        elif ( 'xpds' == pid1.lower() and 'xcc' == pid2.lower()):
                return get_xcc_xpds_msg_str(usMsgId)
                
        elif ( 'xreg' == pid1.lower() and 'taf' == pid2.lower()):
                return get_xreg_taf_msg_str(usMsgId)
        elif ( 'taf' == pid1.lower() and 'xreg' == pid2.lower()):
                return get_xreg_taf_msg_str(usMsgId)
        elif ( 'xreg' == pid1.lower() and 'i1_taf' == pid2.lower()):
                return get_xreg_taf_msg_str(usMsgId)
        elif ( 'i1_taf' == pid1.lower() and 'xreg' == pid2.lower()):
                return get_xreg_taf_msg_str(usMsgId)
        elif ( 'xreg' == pid1.lower() and 'i2_taf' == pid2.lower()):
                return get_xreg_taf_msg_str(usMsgId)
        elif ( 'i2_taf' == pid1.lower() and 'xreg' == pid2.lower()):
                return get_xreg_taf_msg_str(usMsgId)

        elif ( 'xreg' == pid1.lower() and 'rrm' == pid2.lower()):
                return get_xreg_rrm_msg_str(usMsgId)
        elif ( 'rrm' == pid1.lower() and 'xreg' == pid2.lower()):
                return get_xreg_rrm_msg_str(usMsgId)
                
        elif ( 'hsd' == pid1.lower() and 'mscc' == pid2.lower()):
                return get_hsd_mscc_msg_str(usMsgId)
        elif ( 'mscc' == pid1.lower() and 'hsd' == pid2.lower()):
                return get_hsd_mscc_msg_str(usMsgId)    
        elif ( 'hsd' == pid1.lower() and 'i1_mscc' == pid2.lower()):
                return get_hsd_mscc_msg_str(usMsgId)
        elif ( 'i1_mscc' == pid1.lower() and 'hsd' == pid2.lower()):
                return get_hsd_mscc_msg_str(usMsgId)    
        elif ( 'hsd' == pid1.lower() and 'i2_mscc' == pid2.lower()):
                return get_hsd_mscc_msg_str(usMsgId)
        elif ( 'i2_mscc' == pid1.lower() and 'hsd' == pid2.lower()):
                return get_hsd_mscc_msg_str(usMsgId)    

        elif ( 'hsd' == pid1.lower() and 'hsd' == pid2.lower()):
                return get_hsd_hsd_msg_str(usMsgId)
        elif ( 'hsd' == pid1.lower() and 'hsd' == pid2.lower()):
                return get_hsd_hsd_msg_str(usMsgId)
                
        elif ( 'hsd' == pid1.lower() and 'ehsm' == pid2.lower()):
                return get_hsd_ehsm_msg_str(usMsgId)
        elif ( 'ehsm' == pid1.lower() and 'hsd' == pid2.lower()):
                return get_hsd_ehsm_msg_str(usMsgId)
                
        elif ( 'hsd' == pid1.lower() and 'hlu' == pid2.lower()):
                return get_hsd_hlu_msg_str(usMsgId)
        elif ( 'hlu' == pid1.lower() and 'hsd' == pid2.lower()):
                return get_hsd_hlu_msg_str(usMsgId)
                
        elif ( 'hsd' == pid1.lower() and 'hrm' == pid2.lower()):
                return get_hsd_hrm_msg_str(usMsgId)
        elif ( 'hrm' == pid1.lower() and 'hsd' == pid2.lower()):
                return get_hsd_hrm_msg_str(usMsgId)

        elif ( 'hsd' == pid1.lower() and 'hsm' == pid2.lower()):
                return get_hsd_hsm_msg_str(usMsgId)
        elif ( 'hsm' == pid1.lower() and 'hsd' == pid2.lower()):
                return get_hsd_hsm_msg_str(usMsgId)
                
        elif ( 'hsd' == pid1.lower() and 'hsp' == pid2.lower()):
                return get_hsd_hsp_msg_str(usMsgId)
        elif ( 'hsp' == pid1.lower() and 'hsd' == pid2.lower()):
                return get_hsd_hsp_msg_str(usMsgId)
                
        elif ( 'hsd' == pid1.lower() and 'hrup' == pid2.lower()):
                return get_hsd_hrup_msg_str(usMsgId)
        elif ( 'hrup' == pid1.lower() and 'hsd' == pid2.lower()):
                return get_hsd_hrup_msg_str(usMsgId)
                        
        elif ( 'ehsm' == pid1.lower() and 'hsm' == pid2.lower()):
                return get_ehsm_hsm_msg_str(usMsgId)
        elif ( 'hsm' == pid1.lower() and 'ehsm' == pid2.lower()):
                return get_ehsm_hsm_msg_str(usMsgId)

        elif ( 'ehsm' == pid1.lower() and 'ehsm' == pid2.lower()):
                return get_ehsm_ehsm_msg_str(usMsgId)
        elif ( 'ehsm' == pid1.lower() and 'ehsm' == pid2.lower()):
                return get_ehsm_ehsm_msg_str(usMsgId)
                
        elif ( 'ehsm' == pid1.lower() and 'esm' == pid2.lower()):
                return get_ehsm_esm_msg_str(usMsgId)
        elif ( 'esm' == pid1.lower() and 'ehsm' == pid2.lower()):
                return get_ehsm_esm_msg_str(usMsgId)
                
        elif ( 'ehsm' == pid1.lower() and 'taf' == pid2.lower()):
                return get_ehsm_taf_msg_str(usMsgId)
        elif ( 'taf' == pid1.lower() and 'ehsm' == pid2.lower()):
                return get_ehsm_taf_msg_str(usMsgId)
        elif ( 'ehsm' == pid1.lower() and 'i1_taf' == pid2.lower()):
                return get_ehsm_taf_msg_str(usMsgId)
        elif ( 'i1_taf' == pid1.lower() and 'ehsm' == pid2.lower()):
                return get_ehsm_taf_msg_str(usMsgId)
        elif ( 'ehsm' == pid1.lower() and 'i2_taf' == pid2.lower()):
                return get_ehsm_taf_msg_str(usMsgId)
        elif ( 'i2_taf' == pid1.lower() and 'ehsm' == pid2.lower()):
                return get_ehsm_taf_msg_str(usMsgId)
                
        elif ( 'ehsm' == pid1.lower() and 'pppc' == pid2.lower()):
                return get_ehsm_pppc_msg_str(usMsgId)
        elif ( 'pppc' == pid1.lower() and 'ehsm' == pid2.lower()):
                return get_ehsm_pppc_msg_str(usMsgId)
                
        elif ( 'hrm' == pid1.lower() and 'hlu' == pid2.lower()):
                return get_hrm_hlu_msg_str(usMsgId)
        elif ( 'hlu' == pid1.lower() and 'hrm' == pid2.lower()):
                return get_hrm_hlu_msg_str(usMsgId)
                
        elif ( 'hrm' == pid1.lower() and 'hrpdsig' == pid2.lower()):
                return get_hrm_hrpdsig_msg_str(usMsgId)
        elif ( 'hrpdsig' == pid1.lower() and 'hrm' == pid2.lower()):
                return get_hrm_hrpdsig_msg_str(usMsgId)
                
        elif ( 'hsm' == pid1.lower() and 'hlu' == pid2.lower()):
                return get_hsm_hlu_msg_str(usMsgId)
        elif ( 'hlu' == pid1.lower() and 'hsm' == pid2.lower()):
                return get_hsm_hlu_msg_str(usMsgId)
                
        elif ( 'hsm' == pid1.lower() and 'hrm' == pid2.lower()):
                return get_hsm_hrm_msg_str(usMsgId)
        elif ( 'hrm' == pid1.lower() and 'hsm' == pid2.lower()):
                return get_hsm_hrm_msg_str(usMsgId)
                
        elif ( 'hsm' == pid1.lower() and 'hsm' == pid2.lower()):
                return get_hsm_hsm_msg_str(usMsgId)
        elif ( 'hsm' == pid1.lower() and 'hsm' == pid2.lower()):
                return get_hsm_hsm_msg_str(usMsgId)

        elif ( 'hsm' == pid1.lower() and 'hrpdrmac' == pid2.lower()):
                return get_hsm_hrpdrmac_msg_str(usMsgId)
        elif ( 'hrpdrmac' == pid1.lower() and 'hsm' == pid2.lower()):
                return get_hsm_hrpdrmac_msg_str(usMsgId)
                
        elif ( 'hlu' == pid1.lower() and 'hrpdrpa' == pid2.lower()):
                return get_hlu_hrpdrpa_msg_str(usMsgId)
        elif ( 'hrpdrpa' == pid1.lower() and 'hlu' == pid2.lower()):
                return get_hlu_hrpdrpa_msg_str(usMsgId)

        else:
                return 'none'

def analysis_cnas_mntn_per_rec_msg_info( instream, fileLocalOffset, outstream, ulLooper):
        instream.seek(fileLocalOffset)

        #outstream.writelines(["\n**************************** *_* *******************************\n"])

        (ulReceiveTime,) = struct.unpack('I', instream.read(4))
        (ulExitTime,)    = struct.unpack('I', instream.read(4))

        (usSendPid,)     = struct.unpack('H', instream.read(2))
        (usRcvPid,)      = struct.unpack('H', instream.read(2))

        (usMsgId,)       = struct.unpack('H', instream.read(2))
        (ucCnasFsmId,)   = struct.unpack('B', instream.read(1))
        (ucCnasState,)   = struct.unpack('B', instream.read(1))

        #outstream.writelines(["\n*** (^_^): %-10d%-10d%-10d%-10d%-10d%-10d%-10d*******************************\n" % (ulReceiveTime, ulExitTime, usSendPid, usRcvPid, usMsgId, ucCnasFsmId, ucCnasState)])

        strSendPid       = cnas_get_pid_str(usSendPid)
        strRcvPid        = cnas_get_pid_str(usRcvPid)
        strMsgId         = get_cnas_msgid_str(strSendPid, strRcvPid, usMsgId)      
 
        strSendPid       = '%s(0x%x)' % ( strSendPid, usSendPid)
        strRcvPid        = '%s(0x%x)' % ( strRcvPid, usRcvPid)
        strMsgId         = '%s(0x%x)' % ( strMsgId, usMsgId)
        strReceiveTime   = '0x%x'% ulReceiveTime
        strExitTime      = '0x%x'% ulExitTime

        strCnasFsmId = '0x%x' % ucCnasFsmId
        strCnasState = '0x%x' % ucCnasState
   
        outstream.writelines(["%-10s%-15s%-15s%-15s%-15s%-55s%-20s%-20s\n" % (ulLooper, strReceiveTime.upper(), strExitTime.upper(), strSendPid, strRcvPid, strMsgId, strCnasFsmId, strCnasState)])     
        #outstream.writelines(["\n**************************** (-.^): *******************************\n"])

def analysis_cnas_per_dump_info( instream, fileOffset, outstream, ulMsgIndex):
        ulLooper = 0
              
        outstream.writelines(["%-10s%-15s%-15s%-15s%-15s%-55s%-20s%-20s\n" % ("index","ulReceiveTime", "ulExitTime", "usSendPid", "usReceivePid", "usMsgId", "ucCnasFsmId", "ucCnasState")])
        while ulLooper < MACRO_NAS_CNAS_MAX_LOG_EVENT_STATE_NUM:
            ulLooperIndex = ( ulLooper + ulMsgIndex) % MACRO_NAS_CNAS_MAX_LOG_EVENT_STATE_NUM
            fileLocalOffset = fileOffset + ulLooperIndex * MACRO_NAS_CNAS_MNTN_LOG_MSG_INFO_SIZE
            analysis_cnas_mntn_per_rec_msg_info( instream, fileLocalOffset, outstream, (ulLooper))
            ulLooper = ulLooper + 1

def analysis_cnas_mntn_log_CnasCcbMntnSaveExcLog_info( instream, outstream):
        outstream.writelines(["IsMtCallInRoamingAcc:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PowerOffCampOnCtrlFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["HrpdNetWorkSrchingFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PrlSrcType:0x%X\n" % struct.unpack('B', instream.read(1))])
        
        outstream.writelines(["NwInfo_ConcurrentSupported:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NwInfo_PRevInUse:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NwInfo_CasSta:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NwInfo_CasSubSta0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NwInfo_ProtocolRev:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NwInfo_1xRfAvailFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["NwInfo_1xSysInfo_Sid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["NwInfo_1xSysInfo_Nid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["NwInfo_1xSysInfo_BandClass:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["NwInfo_1xSysInfo_Channel:0x%X\n" % struct.unpack('H', instream.read(2))])
        
        outstream.writelines(["HomeSidNidList_SysNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["HomeSidNidList_HomeSidNidSrcType:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        ulLooper        = 0
        while ulLooper < 20:
            outstream.writelines(["HomeSidNidList_HomeSidNid%d:" % ulLooper])
            outstream.writelines(["Sid :0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Nid :0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Band :0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Reserve :0x%X\n" % struct.unpack('H', instream.read(2))])
            ulLooper = ulLooper + 1
            
        outstream.writelines(["ModemInfo_CurCdmaModeModemId:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["ModemInfo_PreCdmaModeModemId:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["ModemInfo_CurRealModemId:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["ModemInfo_CdmaModemIdIsKnown:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
        outstream.writelines(["CurrPsRatType:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["PrevPsRatType:0x%X\n" % struct.unpack('I', instream.read(4))])
        
        ulLooper        = 0
        while ulLooper < 5:
            outstream.writelines(["1xCallState%d:" % ulLooper])
            outstream.writelines(["1xCallState :0x%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["1xSoType :0x%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve :0x%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve :0x%X\n" % struct.unpack('B', instream.read(1))])
            ulLooper = ulLooper + 1
            
        outstream.writelines(["1xReturnCause:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["1xCallExistCount:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
        outstream.writelines(["OperLockSysWhiteList_Enable:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["OperLockSysWhiteList_WhiteSysNum:0x%X\n" % struct.unpack('H', instream.read(2))])
        ulLooper        = 0
        while ulLooper < 20:
            outstream.writelines(["OperLockSysWhiteList_SysInfo%d:" % ulLooper])
            outstream.writelines(["StartSid :0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["EndSid :0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Mcc :0x%X\n" % struct.unpack('I', instream.read(4))])
            ulLooper = ulLooper + 1
            
        outstream.writelines(["CTCCCustInfo_CustFreqList_EnableFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["CTCCCustInfo_CustFreqList_FreqNum:0x%X\n" % struct.unpack('H', instream.read(2))])
        ulLooper        = 0
        while ulLooper < 20:
            outstream.writelines(["CTCCCustInfo_CustFreqList_FreqList%d:" % ulLooper])
            outstream.writelines(["Channel :0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Reserve :0x%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve :0x%X\n" % struct.unpack('B', instream.read(1))])
            ulLooper = ulLooper + 1
            
        outstream.writelines(["CdmaStandardChan_PrimaryA:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CdmaStandardChan_PrimaryB:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CdmaStandardChan_SecondaryA:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CdmaStandardChan_SecondaryB:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["OhmFreq_BandClass:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["OhmFreq_Channel:0x%X\n" % struct.unpack('H', instream.read(2))])
        
        outstream.writelines(["CardInfo_CsimCardStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CardInfo_UsimCardStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CardInfo_IccId:0x"])
        analysis_array_data_one_byte(instream, outstream, 10)
        outstream.writelines(["CardInfo_UIMID_EFRUIMID:0x"])
        analysis_array_data_one_byte(instream, outstream, 8)
        outstream.writelines(["CardInfo_EsnMeidMe_EsnMeidType:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CardInfo_EsnMeidMe_data:0x"])
        analysis_array_data_one_byte(instream, outstream, 7)
        outstream.writelines(["CardInfo_HrpdAccessAuthInfo_AccessAuthAvailFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CardInfo_HrpdAccessAuthInfo_AccessAuthUserNameLen:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["CardInfo_HrpdAccessAuthInfo_AccessAuthUserName:0x"])
        analysis_array_data_one_byte(instream, outstream, 253)
        outstream.writelines(["CardInfo_PreImsi:0x"])
        analysis_array_data_one_byte(instream, outstream, 9)
        outstream.writelines(["CardInfo_Imsi:0x"])
        analysis_array_data_one_byte(instream, outstream, 9)
        outstream.writelines(["CardInfo_IsCardChanged:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CardInfo_IsSwitchOnAsyncReadCard:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CardInfo_1xReadCardStatusFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CardInfo_HrpdReadCardStatusFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
        outstream.writelines(["1xSrvInfo_CurSrvStatus:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["1xSrvInfo_1xActiveFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
        outstream.writelines(["MsSysCfg_RatNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["MsSysCfg_RatPrio:"])
        analysis_array_data_four_byte(instream, outstream, 4)

def analysis_cnas_mntn_log_CnasXsdMntnSaveExcLog_info( instream, outstream):
        outstream.writelines(["RedirInfo_Redirrection:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["RedirInfo_ReturnIfFail:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["RedirInfo_ExpectSid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["RedirInfo_ExpectNid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["RedirInfo_NdssInd:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["RedirInfo_ChanNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        ulLooper        = 0
        while ulLooper < 16:
            outstream.writelines(["RedirInfo_ChanInfo%d:" % ulLooper])
            outstream.writelines(["FreqChan_BandClass :0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["FreqChan_Channel :0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["ChanStatus :0x%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve :0x%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve :0x%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve :0x%X\n" % struct.unpack('B', instream.read(1))])
            ulLooper = ulLooper + 1
        outstream.writelines(["RedirInfo_OriginalSystem_Sid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["RedirInfo_OriginalSystem_Nid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["RedirInfo_OriginalSystem_Freq_BandClass:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["RedirInfo_OriginalSystem_Freq_Channel:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["RedirInfo_CurScanIndex:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["RedirInfo_IsEmcRedir:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
        outstream.writelines(["MntnAvoidFreqList_AvoidFreqNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        ulLooper        = 0
        while ulLooper < 3:
            outstream.writelines(["MntnAvoidFreqList_AvoidFreqInfo%d: " % ulLooper])
            outstream.writelines(["AvoidFlag:0x%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:0x%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:0x%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:0x%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["StartSlice:0x%X " % struct.unpack('I', instream.read(4))])
            outstream.writelines(["ExpiredSliceNum:0x%X " % struct.unpack('I', instream.read(4))])
            outstream.writelines(["AvoidFreq_BandClass:0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["AvoidFreq_Channel:0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["AvoidTimes:0x"])
            analysis_array_data_one_byte(instream, outstream, 13)
            struct.unpack('B', instream.read(1))
            struct.unpack('B', instream.read(1))
            struct.unpack('B', instream.read(1))
            ulLooper = ulLooper + 1
            
        outstream.writelines(["MruList_SysNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        ulLooper        = 0
        while ulLooper < 12:
            outstream.writelines(["MruList_System%d: " % ulLooper])
            outstream.writelines(["Sid:0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Nid:0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Freq_BandClass:0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Freq_Channel:0x%X\n" % struct.unpack('H', instream.read(2))])
            ulLooper = ulLooper + 1
            
        outstream.writelines(["ChanScanList_TotalNum:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["ChanScanList_CurScanIndex:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["ChanScanList_MaxScanChanSize:0x%X\n" % struct.unpack('H', instream.read(2))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["ChanScanList_IsNewScanListFlg:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["ChanScanList_pScanChanInfo:0x%X\n" % struct.unpack('I', instream.read(4))])
        
        outstream.writelines(["GeoListSrchInfo_GeoNum:0x%X\n" % struct.unpack('H', instream.read(2))])
        (Reserve,)           = struct.unpack('H', instream.read(2))
        outstream.writelines(["Reserve:0x%X\n" % Reserve])
        outstream.writelines(["GeoListSrchInfo_pGeoSrchInfo:0x%X\n" % struct.unpack('I', instream.read(4))])
        
        outstream.writelines(["CurCampedSysInfo_System_Sid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CurCampedSysInfo_System_Nid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CurCampedSysInfo_System_Freq_BandClass:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CurCampedSysInfo_System_Freq_Channel:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CurCampedSysInfo_Mcc:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CurCampedSysInfo_SrvStatus:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CurCampedSysInfo_ImsiI1_I2:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CurCampedSysInfo_RoamingInd:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CurCampedSysInfo_SysType:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CurCampedSysInfo_CampOnFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
        outstream.writelines(["CallRedialInfo_CallExistFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CallRedialInfo_OrigSysExistFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["CallRedialInfo_CallOrignalSys_Sid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CallRedialInfo_CallOrignalSys_Nid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CallRedialInfo_CallOrignalSys_Freq_BandClass:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CallRedialInfo_CallOrignalSys_Freq_Channel:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CallRedialInfo_CallRedialChanScanList_TotalNum:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CallRedialInfo_CallRedialChanScanList_CurScanIndex:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CallRedialInfo_CallRedialChanScanList_MaxScanChanSize:0x%X\n" % struct.unpack('H', instream.read(2))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["CallRedialInfo_CallRedialChanScanList_IsNewScanListFlag:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CallRedialInfo_CallRedialChanScanList_pstScanChanInfo:0x%X\n" % struct.unpack('I', instream.read(4))])
        
        outstream.writelines(["FreqLockPara_FreqLockMode:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["FreqLockPara_CdmaBandClass:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["FreqLockPara_Sid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["FreqLockPara_Nid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["FreqLockPara_CdmaFreq:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["FreqLockPara_CdmaPn:0x%X\n" % struct.unpack('H', instream.read(2))])
        
        outstream.writelines(["OocScheduleInfo_OocCtxInfo_WaitSearchFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OocScheduleInfo_OocCtxInfo_CurPhase:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OocScheduleInfo_OocCtxInfo_CurTimes:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["OocScheduleInfo_OocCtxInfo_FirstFourAcqArrivedFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OocScheduleInfo_OocCtxInfo_AttemptTimesInDoTraffic:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OocScheduleInfo_OocCtxInfo_SceneSetFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OocScheduleInfo_OocCtxInfo_TotalTimerExpiredFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OocScheduleInfo_OocCtxInfo_1xMru0TimerExpiredCount:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["OocScheduleInfo_OocCtxInfo_OocSearchScene:0x%X\n" % struct.unpack('I', instream.read(4))])
        (Reserve,)           = struct.unpack('H', instream.read(2))
        outstream.writelines(["Reserve:0x%X\n" % Reserve])
        outstream.writelines(["OocScheduleInfo_StrategyCfg_PhaseNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OocScheduleInfo_StrategyCfg_OocScanStrategy:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OocScheduleInfo_StrategyCfg_1xOocDoTchPhase1TimerLen:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OocScheduleInfo_StrategyCfg_1xOocDoTchPhase2TimerLen:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OocScheduleInfo_StrategyCfg_1xMru0TimerMaxExpiredTimes:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        ulLooper        = 0
        while ulLooper < 8:
            outstream.writelines(["OocScheduleInfo_StrategyCfg_PhaseCfgInfo%d: " % ulLooper])
            outstream.writelines(["TotalTimeLen:0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["SleepTimeLen:0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["SrchNum:0x%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:0x%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Mru0SearchTimerLen:0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["MinSleepTimerLen:0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Reserve:0x%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:0x%X\n" % struct.unpack('B', instream.read(1))])
            ulLooper = ulLooper + 1
            
        outstream.writelines(["EmcCallInfo_EmcState:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["EmcCallInfo_CallBackSrchCounter:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["EmcCallInfo_ExcludeSaveOhmFreqFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["EmcCallInfo_CallBackCfg_CallBackEnableFlg:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["EmcCallInfo_CallBackCfg_CallBackModeTimerLen:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["EmcCallInfo_CallOrignalSys_Sid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["EmcCallInfo_CallOrignalSys_Nid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["EmcCallInfo_CallOrignalSys_Freq_BandClass:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["EmcCallInfo_CallOrignalSys_Freq_Channel:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["EmcCallInfo_EmcCallRedialChanScanList_TotalNum:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["EmcCallInfo_EmcCallRedialChanScanList_CurScanIndex:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["EmcCallInfo_EmcCallRedialChanScanList_MaxScanChanSize:0x%X\n" % struct.unpack('H', instream.read(2))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["EmcCallInfo_EmcCallRedialChanScanList_IsNewScanListFlg:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["EmcCallInfo_EmcCallRedialChanScanList_pstScanChanInfo:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["EmcCallInfo_EmcRedialSysAcqCfg_RedialCount:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["EmcCallInfo_EmcRedialSysAcqCfg_RedialTimes:0x"])
        analysis_array_data_one_byte(instream, outstream, 12)
        outstream.writelines(["EmcCallInfo_EmcRedialSysAcqCfg_LastCampedSys_Sid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["EmcCallInfo_EmcRedialSysAcqCfg_LastCampedSys_Nid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["EmcCallInfo_EmcRedialSysAcqCfg_LastCampedSys_Freq_BandClass:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["EmcCallInfo_EmcRedialSysAcqCfg_LastCampedSys_Freq_Channel:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["EmcCallInfo_EmcRedialSysAcqCfg_EmcRedialMruList_SysNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        ulLooper        = 0
        while ulLooper < 12:
            outstream.writelines(["EmcCallInfo_EmcRedialSysAcqCfg_EmcRedialMruList_System%d: " % ulLooper])
            outstream.writelines(["Sid:0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Nid:0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Freq_BandClass:0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Freq_Channel:0x%X\n" % struct.unpack('H', instream.read(2))])
            ulLooper = ulLooper + 1
        outstream.writelines(["EmcCallInfo_EmcCallBackCfInfo_CfChannelNum:0x%X\n" % struct.unpack('H', instream.read(2))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        ulLooper        = 0
        while ulLooper < 3:
            outstream.writelines(["EmcCallInfo_EmcCallBackCfInfo_ChannelList%d: " % ulLooper])
            outstream.writelines(["BandClass:0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Channel:0x%X\n" % struct.unpack('H', instream.read(2))])
            ulLooper = ulLooper + 1
            
        outstream.writelines(["Cdma1xCustomPrefChan_EnableFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["Cdma1xCustomPrefChan_FreqNum:0x%X\n" % struct.unpack('H', instream.read(2))])
        ulLooper        = 0
        while ulLooper < 20:
            outstream.writelines(["Cdma1xCustomPrefChan_FreqList%d: " % ulLooper])
            outstream.writelines(["Channel:0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["BandClass:0x%X\n" % struct.unpack('H', instream.read(2))])
            ulLooper = ulLooper + 1
            
        outstream.writelines(["SrvAcqFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["TestConfig_ReadNvPrlDirectly:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["TestConfig_ReadDefaultPrl:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["TestConfig_NoCardModeCfgFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["TestConfig_IsMode1xAvailTimerLen:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["TestConfig_PrlCombinedFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["SysAcqNvimCfg_AddAvoidListCfg_IsNegSysAdd:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysAcqNvimCfg_AddAvoidListCfg_Reserve:0x"])
        analysis_array_data_one_byte(instream, outstream, 15)
        outstream.writelines(["SysAcqNvimCfg_NegPrefSysCmpCtrl_NegPrefSysCmpType:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysAcqNvimCfg_NegPrefSysCmpCtrl_Reserve:0x"])
        analysis_array_data_one_byte(instream, outstream, 15)

def analysis_cnas_mntn_log_CnasXccMntnSaveExcLog_info( instream, outstream):    
        outstream.writelines(["MainCtrlCtx_BufferMsgQueue_MsgNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        ulLooper        = 0
        while ulLooper < 5:
            outstream.writelines(["MainCtrlCtx_BufferMsgQueue_pastBufferMsg%d:" % ulLooper])
            outstream.writelines(["p is 0x%X\n" % struct.unpack('I', instream.read(4))])
            ulLooper = ulLooper + 1
        outstream.writelines(["MainCtrlCtx_SeqNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MainCtrlCtx_LastestCallIndex:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["MainCtrlCtx_EmcCallCtrl_WaitFlashMsgRspFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MainCtrlCtx_EmcCallCtrl_EmcCallId:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MainCtrlCtx_EmcCallCtrl_MtVoiceCallId:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MainCtrlCtx_EmcCallCtrl_FlashMsgSeqNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        ulLooper        = 0
        while ulLooper < 7:
            outstream.writelines(["astSridInfo%d: " % ulLooper])
            outstream.writelines(["IsUsed:0x%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Srid:0x%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["So:0x%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["ConnectId:0x%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:0x%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:0x%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:0x%X\n" % struct.unpack('B', instream.read(1))])
            ulLooper = ulLooper + 1
        outstream.writelines(["OrigCallIndexOrder_CallNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["OrigCallIndexOrder_CallIndex:0x"])
        analysis_array_data_one_byte(instream, outstream, 4)
        outstream.writelines(["CallNvimCfg_IsL3ErrReOrigCount:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CallNvimCfg_PrivacyMode:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CallNvimCfg_Reserve:"])
        analysis_array_data_one_byte(instream, outstream, 14)
        outstream.writelines(["CallNvimCfg_EccSrvCap:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CallNvimCfg_EccSrvStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["PagingRspSoCfg_NoDataSrvRspSo33Flg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["IsAlreadyNtfLmmCallStart:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
def analysis_cnas_mntn_log_CnasXregMntnSaveExcLog_info( instream, outstream):
        outstream.writelines(["CnasXregStateInfo_RegEnableFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_DistRegFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_RegisterFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_IsVerChange:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_IsTchHandoff:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_PowerSaveDeregFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_IsTiPowerOffEstCnfValid:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_NormalServiceFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_T57MState:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_RegTimerState:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_CurRegType:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_PowerOffDeregFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_CasState:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_BlkSys:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_BandClass:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CnasXregStateInfo_RegInitCount:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CnasXregStateInfo_RegCountMax:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CnasXregStateInfo_RemainderTimerLen:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CnasXregStateInfo_DistInfo_BaseLast:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CnasXregStateInfo_DistInfo_BaseLong:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CnasXregStateInfo_DistInfo_DistThrd:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CnasXregStateInfo_RegTypeMntn:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CnasXregStateInfo_RegResult:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CnasXregStateInfo_RegTypeNeeded:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
        outstream.writelines(["CnasXregSysMsgCont_Available:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_BandClass:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_Freq:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_Sid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_Nid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_PacketZoneId:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfoIncl:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_BaseStationInfoIncl:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_ServiceInfoIncl:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_MaxSlotCycleIndex:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_PRevInUse:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_RegZone:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_RegZoneNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_ZoneTimer:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_MultiSidFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_MultiNidFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_RegDistance:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_RegPeriod:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_HomeReg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_SidRoamReg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_NidRoamReg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_PowerUpReg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_PowerDownReg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_ParameterReg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_BaseStationInfo_BaseId:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_BaseStationInfo_BaseClass:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_BaseStationInfo_BaseLatitude:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_BaseStationInfo_BaseLongitude:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_ServiceInfo_MaxAltSo:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_ServiceInfo_SDBSupported:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_ServiceInfo_MoQos:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_ServiceInfo_ConcurrentSupported:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_ServiceInfo_MoPosSupported:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_ServiceInfo_ImsiI1_I2:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_ServiceInfo_Mcc:0x%X\n" % struct.unpack('I', instream.read(4))])

def analysis_cnas_mntn_log_CnasHsmMntnSaveExcLog_info( instream, outstream):
        outstream.writelines(["HrpdConnCtrlInfo_HrpdConvertedCasStatus:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["HrpdConnCtrlInfo_HrpdOriginalCasStatus:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["HrpdConnCtrlInfo_HsmCallId:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["HrpdConnCtrlInfo_ConnStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["HrpdConnCtrlInfo_IsFirstPdpActConnFlag:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionSeed:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionCtrlInfo_PublicData_TransmitATI_ATIType:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["SessionCtrlInfo_PublicData_TransmitATI_ATIValue:0x"])
        analysis_array_data_one_byte(instream, outstream, 4)
        outstream.writelines(["SessionCtrlInfo_PublicData_TransmitATI_AddrTimerLen:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionCtrlInfo_PublicData_ReceiveATIList_ATIRecordNum:0x%X\n" % struct.unpack('I', instream.read(4))])
        ulLooper        = 0
        while ulLooper < 5:
            outstream.writelines(["SessionCtrlInfo_PublicData_ReceiveATIList_ATIEntry%d:\n" % ulLooper])
            outstream.writelines(["ATIType:0x%X" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["ucReserve:0x%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["ucReserve:0x%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["ucReserve:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["ATIValue:0x"])
            analysis_array_data_one_byte(instream, outstream, 4)
            outstream.writelines(["AddrTimerLen:0x%X\n" % struct.unpack('I', instream.read(4))])
            ulLooper = ulLooper + 1
        outstream.writelines(["SessionCtrlInfo_PublicData_UATIInfo_CurUATI:0x"])
        analysis_array_data_one_byte(instream, outstream, 16)   
        outstream.writelines(["SessionCtrlInfo_PublicData_UATIInfo_OldUATI:0x"])
        analysis_array_data_one_byte(instream, outstream, 16)
        outstream.writelines(["SessionCtrlInfo_PublicData_UATIInfo_SubnetInc:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_UATIInfo_UATIColorCode:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_UATIInfo_UATISubnetMask:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_UATIInfo_OldUATILen:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_LocInfo_Longitude:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionCtrlInfo_PublicData_LocInfo_Latitude:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionActCtrlCtx_SessionActTriedCntConnFail:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionActCtrlCtx_SessionActTriedCntOtherFail:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionActCtrlCtx_SessionActMaxCntConnFail:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionActCtrlCtx_SessionActMaxCntOtherFail:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionActCtrlCtx_SessionActTimerLen:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionActCtrlCtx_ScpActFailProtType:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionActCtrlCtx_ScpActFailProtSubType:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionActCtrlCtx_ReqSessionTypeForRetry:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionActCtrlCtx_IsExplicitlyConnDenyFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["SessionCtrlInfo_PublicData_HrpdSysInfo_ColorCode:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_HrpdSysInfo_SubNetMask:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_HrpdSysInfo_OhmParameterUpToDate:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_HrpdSysInfo_SecondaryColorCodeCount:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_HrpdSysInfo_SectorId:0x"])
        analysis_array_data_one_byte(instream, outstream, 16)
        outstream.writelines(["SessionCtrlInfo_PublicData_HrpdSysInfo_SecondaryColorCode:0x"])
        analysis_array_data_one_byte(instream, outstream, 7)
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["SessionCtrlInfo_PublicData_HrpdSysInfo_Longitude:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionCtrlInfo_PublicData_HrpdSysInfo_Latitude:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionCtrlInfo_PublicData_UATIAssignMsgSeq:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_UATIReqTransId:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_IsFirstSysAcq:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_RcvOhmScene:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_IsSessionNegOngoing:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_IsScpActive:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_StartUatiReqAfterSectorIdChgFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_WaitUatiAssignTimerLenInfo_Setup:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_WaitUatiAssignTimerLenInfo_Open:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["SessionCtrlInfo_PublicData_LatestSessionDeactReason:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_PrevUatiForSessionRestore:0x"])
        analysis_array_data_one_byte(instream, outstream, 16)
        outstream.writelines(["SessionCtrlInfo_PublicData_NegoSessionType:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_ReqSessionType:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_CurSessionRelType:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_StoreEsnMeidRslt_IsStored:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_StoreEsnMeidRslt_IsChanged:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["SessionCtrlInfo_PublicData_Modem0CardStatusChgInfo_IsPreCardPresent:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_Modem0CardStatusChgInfo_IsCurCardPresent:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["SessionCtrlInfo_PublicData_Modem1CardStatusChgInfo_IsPreCardPresent:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_Modem1CardStatusChgInfo_IsCurCardPresent:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["SessionCtrlInfo_PublicData_Modem2CardStatusChgInfo_IsPreCardPresent:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_Modem2CardStatusChgInfo_IsCurCardPresent:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["SessionCtrlInfo_PublicData_LastHrpdUERevInfo_SuppOnlyDo0:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_LastHrpdUERevInfo_SuppDoaWithMfpa:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_LastHrpdUERevInfo_SuppDoaWithEmfpa:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_LastHrpdUERevInfo_SuppDoaEhrpd:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_UatiReqRetryTimesWhenUatiAssignTimerExpireInAmpOpen:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SendSessionCloseFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_ClearKATimerInConnOpenFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_RecoverEhrpdAvailFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_RecoverEhrpdCapAfterSessionCloseFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_CloseEhrpdCapAfterSyscfgNotSupportLteFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_EhrpdAvailFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_PriorUATAssignMsgSeq:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_PriorSessionSeed:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionCtrlInfo_PublicData_PseudorandomNumber:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionCtrlInfo_PublicData_PaAccessAuthCtrlInfo_Subnet:0x"])
        analysis_array_data_one_byte(instream, outstream, 16)
        outstream.writelines(["SessionCtrlInfo_PublicData_PaAccessAuthCtrlInfo_Count:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["SessionCtrlInfo_PublicData_SectorIdOfLastUatiReq:0x"])
        analysis_array_data_one_byte(instream, outstream, 16)
        
        outstream.writelines(["HrpdAmpNegAttibInfo_MaxNoMonitorDistance:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["HrpdAmpNegAttibInfo_HardwareSeparableFromSession:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["HrpdAmpNegAttibInfo_SupportGAUPMaxNoMonitorDistance:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["HrpdAmpNegAttibInfo_ReducedSubnetMaskOffset:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["HrpdAmpNegAttibInfo_SupportSecondaryColorCodes:0x%X\n" % struct.unpack('H', instream.read(2))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
        outstream.writelines(["KeepAliveCtrlCtx_ReferenceSysTick:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["KeepAliveCtrlCtx_KeepAliveReqTransId:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["KeepAliveCtrlCtx_ReceivedSysTime:0x"])
        analysis_array_data_four_byte(instream, outstream, 2)
        outstream.writelines(["KeepAliveCtrlCtx_KeepAliveTimerInfo_KeepAliveReqSndCount:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["KeepAliveCtrlCtx_KeepAliveTimerInfo_SysTickFwdTrafChan:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["KeepAliveCtrlCtx_KeepAliveTimerInfo_OldSysTickFwdTrafChan:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["KeepAliveCtrlCtx_KeepAliveTimerInfo_KeepAliveTimerLen:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["KeepAliveCtrlCtx_KeepAliveTimerInfo_TotalTimerRunCount:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["KeepAliveCtrlCtx_KeepAliveTimerInfo_TimerExpiredCount:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["KeepAliveCtrlCtx_SessionKeepAliveInfo_IsKeepAliveInfoValid:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["KeepAliveCtrlCtx_SessionKeepAliveInfo_TsmpClose:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["KeepAliveCtrlCtx_SessionKeepAliveInfo_TsmpCloseRemainTime:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["KeepAliveCtrlCtx_SessionKeepAliveInfo_PowerOffSysTime:0x"])
        analysis_array_data_four_byte(instream, outstream, 2)
        outstream.writelines(["MultiModeCtrlInfo_LteReqSuccFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["SnpDataReqCtrlInfo_HsmSnpDataReqOpId:0x%X\n" % struct.unpack('H', instream.read(2))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["SnpDataReqCtrlInfo_SaveSnpDataReqOpId_SessionCloseOpId:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SnpDataReqCtrlInfo_SaveSnpDataReqOpId_UatiReqOpId:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SnpDataReqCtrlInfo_SaveSnpDataReqOpId_UatiCmplOpId:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SnpDataReqCtrlInfo_SaveSnpDataReqOpId_KeepAliveReqOpId:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SnpDataReqCtrlInfo_SaveSnpDataReqOpId_KeepAliveRspOpId:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SnpDataReqCtrlInfo_SaveSnpDataReqOpId_HardWareIdRspOpId:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["LowPowerCtrlInfo_SlotVoteBox:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])

def analysis_cnas_mntn_log_CnasEHsmMntnSaveExcLog_info( instream, outstream):
        outstream.writelines(["EhrpdState:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionType:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["WorkMode:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["AirLinkExist:0x%X\n" % struct.unpack('I', instream.read(4))])
        
        ulLooper        = 0
        while ulLooper < 3:
            outstream.writelines(["\nLocalPdnBearInfo%d:\n" % ulLooper])
            outstream.writelines(["PdnId:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["InUsed:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Cid:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["IsPdnActive:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Epsbid:0x%X\n" % struct.unpack('I', instream.read(4))])
            outstream.writelines(["PdnAddr_PdnType:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PdnAddr_SynncToEsmIpv6Addr:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PdnAddr_Reserve:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PdnAddr_Reserve:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PdnAddr_Ipv4Addr:0x"])
            analysis_array_data_one_byte(instream, outstream, 4)
            outstream.writelines(["PdnAddr_Ipv6Addr:0x"])
            analysis_array_data_one_byte(instream, outstream, 16)
            outstream.writelines(["ApnLen:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Apn:0x"])
            analysis_array_data_one_byte(instream, outstream, 7)
            outstream.writelines(["AttachType:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PdnType:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Mtu:0x%X\n" % struct.unpack('H', instream.read(2))])
            outstream.writelines(["AuthType:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["RetryTotalCnt:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:0x%X\n" % struct.unpack('B', instream.read(1))])
            ulLooper = ulLooper + 1
            
        ulLooper        = 0
        while ulLooper < 3:
            outstream.writelines(["\nLtePdnBearInfo%d:\n" % ulLooper])
            outstream.writelines(["InUsed:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Cid:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PdnType:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Epsbid:0x%X\n" % struct.unpack('I', instream.read(4))])
            outstream.writelines(["PdnAddr_PdnType:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PdnAddr_SynncToEsmIpv6Addr:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PdnAddr_Reserve:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PdnAddr_Reserve:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PdnAddr_Ipv4Addr:0x"])
            analysis_array_data_one_byte(instream, outstream, 4)
            outstream.writelines(["PdnAddr_Ipv6Addr:0x"])
            analysis_array_data_one_byte(instream, outstream, 16)
            outstream.writelines(["ApnLen:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Apn:0x"])
            analysis_array_data_one_byte(instream, outstream, 7)
            ulLooper = ulLooper + 1
        
def analysis_cnas_event_state_list_dump_info( instream, fileOffset, outstream):   
        ulLooperTest = 0
        
        #outstream.writelines(["\n**************************** analysis_cnas_event_state_list_dump_info enter! %d*******************************\n" % (fileOffset)])
        instream.seek(fileOffset)
        (ulBeginTick,)       = struct.unpack('I', instream.read(4))
        strBeginTick         = '0x%x'% ulBeginTick

        #outstream.writelines(["strModemLogBeginFlg         %-15s\n" % ( strBeginTick )])
        
        fileOffset = fileOffset + 4
        
        #outstream.writelines(["\n**************************** analysis_cnas_event_state_list_dump_info enter! %d*******************************\n" % (fileOffset)])
        
        ##### cnas #########        
        analysis_cnas_per_dump_info(instream, fileOffset, outstream, ulLooperTest)
        
        outstream.writelines(["\nLatestIndex:%d\n" % struct.unpack('I', instream.read(4))])
        
        outstream.writelines(["\nCnasCcbInfoStart:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["\n%-15s\n" % ("CnasCcbMntnSaveExcLog:")])
        analysis_cnas_mntn_log_CnasCcbMntnSaveExcLog_info( instream, outstream)
        
        outstream.writelines(["\nCnasXsdInfoStart:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["\n%-15s\n" % ("CnasXsdMntnSaveExcLog:")])
        analysis_cnas_mntn_log_CnasXsdMntnSaveExcLog_info( instream, outstream)
        
        outstream.writelines(["\nCnasXccInfoStart:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["\n%-15s\n" % ("CnasXccMntnSaveExcLog:")])
        analysis_cnas_mntn_log_CnasXccMntnSaveExcLog_info( instream, outstream)
        
        outstream.writelines(["\nCnasXregInfoStart:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["\n%-15s\n" % ("CnasXregMntnSaveExcLog:")])
        analysis_cnas_mntn_log_CnasXregMntnSaveExcLog_info( instream, outstream)
        
        outstream.writelines(["\nCnasHsmInfoStart:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["\n%-15s\n" % ("CnasHsmMntnSaveExcLog:")])
        analysis_cnas_mntn_log_CnasHsmMntnSaveExcLog_info( instream, outstream)
        
        outstream.writelines(["\nCnasEHsmInfoStart:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["\n%-15s\n" % ("CnasEHsmMntnSaveExcLog:")])
        analysis_cnas_mntn_log_CnasEHsmMntnSaveExcLog_info( instream, outstream)
        
        #outstream.writelines(["\nCnasHsdInfoStart:0x%X\n" % struct.unpack('I', instream.read(4))])
        
        #outstream.writelines(["\n**************************** *_* *******************************\n"])     

        return True

def analysis_hsd_mntn_per_rec_msg_info( instream, fileLocalOffset, outstream, ulLooper):
        instream.seek(fileLocalOffset)

        #outstream.writelines(["\n**************************** *_* *******************************\n"])

        (ulReceiveTime,) = struct.unpack('I', instream.read(4))

        (usSendPid,)     = struct.unpack('H', instream.read(2))
        (usRcvPid,)      = struct.unpack('H', instream.read(2))

        (usMsgId,)       = struct.unpack('H', instream.read(2))
        (ucCnasFsmId,)   = struct.unpack('B', instream.read(1))
        (ucCnasState,)   = struct.unpack('B', instream.read(1))

        #outstream.writelines(["\n*** (^_^): %-10d%-10d%-10d%-10d%-10d%-10d%-10d*******************************\n" % (ulReceiveTime, ulExitTime, usSendPid, usRcvPid, usMsgId, ucCnasFsmId, ucCnasState)])

        strSendPid       = cnas_get_pid_str(usSendPid)
        strRcvPid        = cnas_get_pid_str(usRcvPid)
        strMsgId         = get_cnas_msgid_str(strSendPid, strRcvPid, usMsgId)      
 
        strSendPid       = '%s(0x%x)' % ( strSendPid, usSendPid)
        strRcvPid        = '%s(0x%x)' % ( strRcvPid, usRcvPid)
        strMsgId         = '%s(0x%x)' % ( strMsgId, usMsgId)
        strReceiveTime   = '0x%x'% ulReceiveTime

        strCnasFsmId = '0x%x' % ucCnasFsmId
        strCnasState = '0x%x' % ucCnasState
   
        outstream.writelines(["%-10s%-30s%-15s%-15s%-55s%-20s%-20s\n" % (ulLooper, strReceiveTime.upper(), strSendPid, strRcvPid, strMsgId, strCnasFsmId, strCnasState)])      
        #outstream.writelines(["\n**************************** (-.^): *******************************\n"])  
        
def analysis_hsd_per_dump_info( instream, fileOffset, outstream, ulMsgIndex):
        ulLooper = 0
              
        outstream.writelines(["%-10s%-30s%-15s%-15s%-55s%-20s%-20s\n" % ("index","ulReceiveTime","usSendPid", "usReceivePid", "usMsgId", "ucCnasFsmId", "ucCnasState")])
        while ulLooper < MACRO_CNAS_HSD_MAX_LOG_EVENT_STATE_NUM:
            ulLooperIndex = ( ulLooper + ulMsgIndex) % MACRO_CNAS_HSD_MAX_LOG_EVENT_STATE_NUM
            fileLocalOffset = fileOffset + ulLooperIndex * MACRO_CNAS_HSD_MNTN_LOG_MSG_INFO_SIZE
            analysis_hsd_mntn_per_rec_msg_info( instream, fileLocalOffset, outstream, ulLooper)
            ulLooper = ulLooper + 1

def analysis_cnas_mntn_log_MruList_info( instream, outstream):
        outstream.writelines(["CurrMruNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
        ulLooper        = 0
        while ulLooper < 12:
            outstream.writelines(["\nHrpdSys%d:\n" % ulLooper])
            outstream.writelines(["Subnet:0x"])
            analysis_array_data_one_byte(instream, outstream, 16)
            outstream.writelines(["SubnetMask:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Freq_BandClass:0x%X\n" % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Freq_Channel:0x%X\n" % struct.unpack('H', instream.read(2))])
            ulLooper = ulLooper + 1

def analysis_cnas_mntn_log_AvoidFreqList_info( instream, outstream):
        outstream.writelines(["AvoidItemUsedNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["CurrAvoidReason:0x%X\n" % struct.unpack('B', instream.read(1))])
        
        ulLooper        = 0
        while ulLooper < 3:
            outstream.writelines(["\nAvoidFreqInfo%d:\n" % ulLooper])
            outstream.writelines(["UsedFlg:0x%X\n" % struct.unpack('I', instream.read(4))])
            outstream.writelines(["AvoidReason:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["StartSlice:0x%X\n" % struct.unpack('I', instream.read(4))])
            outstream.writelines(["ExpiredSliceNum:0x%X\n" % struct.unpack('I', instream.read(4))])
            outstream.writelines(["AvoidFreq_BandClass:0x%X\n" % struct.unpack('H', instream.read(2))])
            outstream.writelines(["AvoidFreq_Channel:0x%X\n" % struct.unpack('H', instream.read(2))])
            ulLooper = ulLooper + 1

def analysis_cnas_mntn_log_Redirection_info( instream, outstream):
        outstream.writelines(["ChanNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
        ulLooper        = 0
        while ulLooper < 3:
            outstream.writelines(["\nChannel%d:\n" % ulLooper])
            outstream.writelines(["SystemType:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["BandClass:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Channel:0x%X\n" % struct.unpack('H', instream.read(2))])
            ulLooper = ulLooper + 1

def analysis_cnas_mntn_log_HighPriority_info( instream, outstream):
        outstream.writelines(["FreqNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        
        ulLooper        = 0
        while ulLooper < 16:
            outstream.writelines(["\nFreqInfo%d:\n" % ulLooper])
            outstream.writelines(["Freq_BandClass:0x%X\n" % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Freq_Channel:0x%X\n" % struct.unpack('H', instream.read(2))])
            outstream.writelines(["HrpdSysItem_AcqIndex:0x%X\n" % struct.unpack('H', instream.read(2))])
            outstream.writelines(["HrpdSysItem_SysIndex:0x%X\n" % struct.unpack('H', instream.read(2))])
            outstream.writelines(["HrpdSysItem_PrioLevel:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["HrpdSysItem_PrefNegSys:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["HrpdSysItem_Reserve:0x%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["HrpdSysItem_Reserve:0x%X\n" % struct.unpack('B', instream.read(1))])
            ulLooper = ulLooper + 1

def analysis_cnas_mntn_log_HrpdSysInfo_info( instream, outstream):
        outstream.writelines(["Status:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CampedHrpdSysInfo_Subnet:0x"])
        analysis_array_data_one_byte(instream, outstream, 16)
        outstream.writelines(["SubnetMask:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["Freq_BandClass:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["Freq_Channel:0x%X\n" % struct.unpack('H', instream.read(2))])

def analysis_cnas_mntn_log_OocScheduleInfo_info( instream, outstream):
        outstream.writelines(["OosCtxInfo_WaitSearchFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OosCtxInfo_CurrentPhase:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OosCtxInfo_CurrentTimes:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["OosCtxInfo_SceneSetFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OosCtxInfo_HrpdMru0TimerExpiredCount:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["OosCtxInfo_OocSearchScene:0x%X\n" % struct.unpack('I', instream.read(4))])
        
        outstream.writelines(["ConfigInfo_Mru0SearchTimerLen:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ConfigInfo_PhaseNum:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ConfigInfo_HrpdMru0TimerMaxExpiredTimes:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        ulLooper        = 0
        while ulLooper < 8:
            outstream.writelines(["\nConfigInfo_OocTimerInfo%d:\n" % ulLooper])
            outstream.writelines(["Times:0x%X\n" % struct.unpack('H', instream.read(2))])
            outstream.writelines(["TimerLen:0x%X\n" % struct.unpack('H', instream.read(2))])
            ulLooper = ulLooper + 1

def analysis_cnas_mntn_log_CasOhmHrpdSys_info( instream, outstream):
        outstream.writelines(["Subnet:"])
        analysis_array_data_one_byte(instream, outstream, 16)
        outstream.writelines(["SubnetMask:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["Freq_BandClass:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["Freq_Channel:0x%X\n" % struct.unpack('H', instream.read(2))])

def analysis_cnas_mntn_log_NetwkLostSysRec_info( instream, outstream):
        outstream.writelines(["HrpdSys_Subnet:0x"])
        analysis_array_data_one_byte(instream, outstream, 16)
        outstream.writelines(["HrpdSys_SubnetMask:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        outstream.writelines(["HrpdSys_Freq_BandClass:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["HrpdSys_Freq_Channel:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["LastRecSlice:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["NetwkLostCnt:0x%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:0x%X\n" % ucReserve])

def analysis_cnas_mntn_log_SyncFreq_info( instream, outstream):
        outstream.writelines(["BandClass:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["Channel:0x%X\n" % struct.unpack('H', instream.read(2))])

def analysis_cnas_mntn_log_SysAcqSrlteInfo_info( instream, outstream):
        outstream.writelines(["IsSysAcqNoRfTimerExpired:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["HrpdSysAcqNoRfProtectTimerLen:0x%X\n" % struct.unpack('I', instream.read(4))])

def analysis_cnas_mntn_log_HrpdMatched1xSysInfo_info( instream, outstream):
        outstream.writelines(["Status:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["1xSys_Sid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["1xSys_Nid:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["1xSys_Freq_BandClass:0x%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["1xSys_Freq_Channel:0x%X\n" % struct.unpack('H', instream.read(2))])
    
def analysis_cnas_mntn_log_SysAssistInfo_info( instream, outstream):
        outstream.writelines(["NoRfScene:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["ATStatus:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionNegStatus:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["HrpdRfAvailFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["Mru0RelateFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysCfgFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NoRf1XUeStatus:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["UeSupportedBand:0x%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["IsAbnormalLostFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionRlt:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["IsSyncFreqInSpmListFlg:0x%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["Reserve:0x%X\n" % struct.unpack('B', instream.read(1))])
    
def analysis_cnas_hsd_msg_info( instream, fileOffset, outstream):   
        ulLooperTest = 0
        
        instream.seek(fileOffset)
        (ulBeginTick,)       = struct.unpack('I', instream.read(4))

        strBeginTick         = '%x'% ulBeginTick

        while True:
            fileOffset = fileOffset + 4
            instream.seek(fileOffset)
            (ulBeginTick,)       = struct.unpack('I', instream.read(4))
            strBeginTick         = '%x'% ulBeginTick
            if strBeginTick == 'aa550006':
                break

        fileOffset = fileOffset + 4
        
        #outstream.writelines(["\n**************************** analysis_cnas_hsd_msg_info enter! %d*******************************\n" % (fileOffset)])
        
        ##### cnas #########        
        analysis_hsd_per_dump_info(instream, fileOffset, outstream, ulLooperTest)
        
        outstream.writelines(["\nLatestIndex:%d\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["ModeType:0x%X\n" % struct.unpack('I', instream.read(4))])
        
        outstream.writelines(["\n%-15s\n" % ("MruList:")])
        analysis_cnas_mntn_log_MruList_info( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("AvoidFreqList:")])
        analysis_cnas_mntn_log_AvoidFreqList_info( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("Redirection:")])
        analysis_cnas_mntn_log_Redirection_info( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("HighPriority:")])
        analysis_cnas_mntn_log_HighPriority_info( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("HrpdSysInfo:")])
        analysis_cnas_mntn_log_HrpdSysInfo_info( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("OocScheduleInfo:")])
        analysis_cnas_mntn_log_OocScheduleInfo_info( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("CasOhmHrpdSys:")])
        analysis_cnas_mntn_log_CasOhmHrpdSys_info( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("NetwkLostSysRec:")])
        analysis_cnas_mntn_log_NetwkLostSysRec_info( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("SyncFreq:")])
        analysis_cnas_mntn_log_SyncFreq_info( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("SysAcqSrlteInfo:")])
        analysis_cnas_mntn_log_SysAcqSrlteInfo_info( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("HrpdMatched1xSysInfo:")])
        analysis_cnas_mntn_log_HrpdMatched1xSysInfo_info( instream, outstream)
        
        outstream.writelines(["\n%-15s\n" % ("SysAssistInfo:")])
        analysis_cnas_mntn_log_SysAssistInfo_info( instream, outstream)
        
        #outstream.writelines(["\n**************************** *_* *******************************\n"])     

        return True 
    
def analysis_cnas_dump_info( infile, offset, outfile):
        instream = infile
        outstream  = outfile
        fileOffset = eval(offset)
           
        ##### cnas PARSE EVENT STATE #########   
        outstream.writelines(["\n**************************** analysis_cnas_dump_info begin!*******************************\n"])             
        analysis_cnas_event_state_list_dump_info( instream, fileOffset, outstream )
        outstream.writelines(["\n**************************** analysis_cnas_dump_info end!*******************************\n"])      

        outstream.writelines(["\n**************************** analysis_cnas_hsd_msg begin!*******************************\n"])
        outstream.writelines(["\nCnasHsdInfoStart:0x%X\n" % struct.unpack('I', instream.read(4))])
        analysis_cnas_hsd_msg_info( instream, fileOffset, outstream )
        outstream.writelines(["\n**************************** analysis_cnas_hsd_msg end!*******************************\n"])        
            
        return True

########################################################################################
def entry_0x2200009(infile, field, offset, len, version, mode, outfile):     
        ########check parameter start#############      
        if not field == '0x2200009':
            print ("hidis field is %s" % (field))
            print ("current field is 0x2200009")
            return error['ERR_CHECK_FIELD']
        elif not version == '0x0004':
            print ("hidis version is %s" % (version))
            print ("current version is 0x0004")
            return error['ERR_CHECK_VERSION']
        elif not len == '0x3000':
            print ("hids len is %s" % (len))
            print ("current len is 0x3000")
            return error['ERR_CHECK_LEN']
        #########check parameter end##############
        ret = analysis_cnas_dump_info( infile, offset, outfile)

        return 0


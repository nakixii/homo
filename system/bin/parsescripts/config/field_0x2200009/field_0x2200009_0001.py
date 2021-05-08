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
            outstream.writelines(["%X " % struct.unpack('I', instream.read(4))])
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
        strReceiveTime   = '%x'% ulReceiveTime
        strExitTime      = '%x'% ulExitTime

        strCnasFsmId = '%x' % ucCnasFsmId 
        strCnasState = '%x' % ucCnasState
   
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
        outstream.writelines(["IsMtCallInRoamingAcc:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PowerOffCampOnCtrlFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["HrpdNetWorkSrchingFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["PrlSrcType:%X\n" % struct.unpack('B', instream.read(1))])
        
        outstream.writelines(["NwInfo_ConcurrentSupported:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NwInfo_PRevInUse:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NwInfo_CasSta:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NwInfo_CasSubSta%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NwInfo_ProtocolRev:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NwInfo_1xRfAvailFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["NwInfo_1xSysInfo_Sid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["NwInfo_1xSysInfo_Nid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["NwInfo_1xSysInfo_BandClass:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["NwInfo_1xSysInfo_Channel:%X\n" % struct.unpack('H', instream.read(2))])
        
        outstream.writelines(["HomeSidNidList_SysNum:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["HomeSidNidList_HomeSidNidSrcType:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        ulLooper        = 0
        while ulLooper < 20:
            outstream.writelines(["HomeSidNidList_HomeSidNid%d:" % ulLooper])
            outstream.writelines(["Sid :%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Nid :%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Band :%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Reserve :%X\n" % struct.unpack('H', instream.read(2))])
            ulLooper = ulLooper + 1
            
        outstream.writelines(["ModemInfo_CurCdmaModeModemId:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["ModemInfo_PreCdmaModeModemId:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["ModemInfo_CdmaModemIdIsKnown:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["CurrPsRatType:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["PrevPsRatType:%X\n" % struct.unpack('I', instream.read(4))])
        
        ulLooper        = 0
        while ulLooper < 5:
            outstream.writelines(["1xCallState%d:" % ulLooper])
            outstream.writelines(["1xCallState :%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["1xSoType :%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve :%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve :%X\n" % struct.unpack('B', instream.read(1))])
            ulLooper = ulLooper + 1
            
        outstream.writelines(["1xReturnCause:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["1xCallExistCount:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["OperLockSysWhiteList_Enable:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["OperLockSysWhiteList_WhiteSysNum:%X\n" % struct.unpack('H', instream.read(2))])
        ulLooper        = 0
        while ulLooper < 20:
            outstream.writelines(["OperLockSysWhiteList_SysInfo%d:" % ulLooper])
            outstream.writelines(["StartSid :%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["EndSid :%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Mcc :%X\n" % struct.unpack('I', instream.read(4))])
            ulLooper = ulLooper + 1
            
        outstream.writelines(["CTCCCustInfo_CustFreqList_EnableFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["CTCCCustInfo_CustFreqList_FreqNum:%X\n" % struct.unpack('H', instream.read(2))])
        ulLooper        = 0
        while ulLooper < 20:
            outstream.writelines(["CTCCCustInfo_CustFreqList_FreqList%d:" % ulLooper])
            outstream.writelines(["Channel :%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Reserve :%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve :%X\n" % struct.unpack('B', instream.read(1))])
            ulLooper = ulLooper + 1
            
        outstream.writelines(["CdmaStandardChan_PrimaryA:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CdmaStandardChan_PrimaryB:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CdmaStandardChan_SecondaryA:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CdmaStandardChan_SecondaryB:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["OhmFreq_BandClass:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["OhmFreq_Channel:%X\n" % struct.unpack('H', instream.read(2))])
        
        outstream.writelines(["CardInfo_CsimCardStatus:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CardInfo_UsimCardStatus:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CardInfo_IccId:"])
        analysis_array_data_one_byte(instream, outstream, 10)
        outstream.writelines(["CardInfo_UIMID_EFRUIMID:"])
        analysis_array_data_one_byte(instream, outstream, 8)
        outstream.writelines(["CardInfo_EsnMeidMe_EsnMeidType:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CardInfo_EsnMeidMe_data:"])
        analysis_array_data_one_byte(instream, outstream, 7)
        outstream.writelines(["CardInfo_HrpdAccessAuthInfo_AccessAuthAvailFlag:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CardInfo_HrpdAccessAuthInfo_AccessAuthUserNameLen:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["CardInfo_HrpdAccessAuthInfo_AccessAuthUserName:"])
        analysis_array_data_one_byte(instream, outstream, 253)
        outstream.writelines(["CardInfo_PreImsi:"])
        analysis_array_data_one_byte(instream, outstream, 9)
        outstream.writelines(["CardInfo_Imsi:"])
        analysis_array_data_one_byte(instream, outstream, 9)
        outstream.writelines(["CardInfo_IsCardChanged:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CardInfo_IsSwitchOnAsyncReadCard:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CardInfo_1xReadCardStatusFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CardInfo_HrpdReadCardStatusFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["1xSrvInfo_CurSrvStatus:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["1xSrvInfo_1xActiveFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["MsSysCfg_RatNum:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["MsSysCfg_RatPrio:"])
        analysis_array_data_four_byte(instream, outstream, 3)

def analysis_cnas_mntn_log_CnasXsdMntnSaveExcLog_info( instream, outstream):
        outstream.writelines(["RedirInfo_Redirrection:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["RedirInfo_ReturnIfFail:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["RedirInfo_ExpectSid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["RedirInfo_ExpectNid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["RedirInfo_NdssInd:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["RedirInfo_ChanNum:%X\n" % struct.unpack('B', instream.read(1))])
        ulLooper        = 0
        while ulLooper < 16:
            outstream.writelines(["RedirInfo_ChanInfo%d:" % ulLooper])
            outstream.writelines(["FreqChan_BandClass :%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["FreqChan_Channel :%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["ChanStatus :%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve :%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve :%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve :%X\n" % struct.unpack('B', instream.read(1))])
            ulLooper = ulLooper + 1
        outstream.writelines(["RedirInfo_OriginalSystem_Sid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["RedirInfo_OriginalSystem_Nid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["RedirInfo_OriginalSystem_Freq_BandClass:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["RedirInfo_OriginalSystem_Freq_Channel:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["RedirInfo_CurScanIndex:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["RedirInfo_IsEmcRedir:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["MntnAvoidFreqList_AvoidFreqNum:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        ulLooper        = 0
        while ulLooper < 3:
            outstream.writelines(["MntnAvoidFreqList_AvoidFreqInfo%d: " % ulLooper])
            outstream.writelines(["AvoidFlag:%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["StartSlice:%X " % struct.unpack('I', instream.read(4))])
            outstream.writelines(["ExpiredSliceNum:%X " % struct.unpack('I', instream.read(4))])
            outstream.writelines(["AvoidFreq_BandClass:%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["AvoidFreq_Channel:%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["AvoidTimes:%X "])
            analysis_array_data_one_byte(instream, outstream, 13)
            struct.unpack('B', instream.read(1))
            struct.unpack('B', instream.read(1))
            struct.unpack('B', instream.read(1))
            ulLooper = ulLooper + 1
            
        outstream.writelines(["MruList_SysNum:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        ulLooper        = 0
        while ulLooper < 12:
            outstream.writelines(["MruList_System%d: " % ulLooper])
            outstream.writelines(["Sid:%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Nid:%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Freq_BandClass:%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Freq_Channel:%X\n" % struct.unpack('H', instream.read(2))])
            ulLooper = ulLooper + 1
            
        outstream.writelines(["ChanScanList_TotalNum:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["ChanScanList_CurScanIndex:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["ChanScanList_MaxScanChanSize:%X\n" % struct.unpack('H', instream.read(2))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["ChanScanList_IsNewScanListFlg:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["ChanScanList_pScanChanInfo:%X\n" % struct.unpack('I', instream.read(4))])
        
        outstream.writelines(["GeoListSrchInfo_GeoNum:%X\n" % struct.unpack('H', instream.read(2))])
        (Reserve,)           = struct.unpack('H', instream.read(2))
        outstream.writelines(["Reserve:%X\n" % Reserve])
        outstream.writelines(["GeoListSrchInfo_pGeoSrchInfo:%X\n" % struct.unpack('I', instream.read(4))])
        
        outstream.writelines(["CurCampedSysInfo_System_Sid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CurCampedSysInfo_System_Nid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CurCampedSysInfo_System_Freq_BandClass:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CurCampedSysInfo_System_Freq_Channel:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CurCampedSysInfo_Mcc:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CurCampedSysInfo_SrvStatus:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CurCampedSysInfo_ImsiI1_I2:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CurCampedSysInfo_RoamingInd:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CurCampedSysInfo_SysType:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CurCampedSysInfo_CampOnFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["CallRedialInfo_CallExistFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CallRedialInfo_OrigSysExistFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["CallRedialInfo_CallOrignalSys_Sid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CallRedialInfo_CallOrignalSys_Nid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CallRedialInfo_CallOrignalSys_Freq_BandClass:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CallRedialInfo_CallOrignalSys_Freq_Channel:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CallRedialInfo_CallRedialChanScanList_TotalNum:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CallRedialInfo_CallRedialChanScanList_CurScanIndex:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CallRedialInfo_CallRedialChanScanList_MaxScanChanSize:%X\n" % struct.unpack('H', instream.read(2))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["CallRedialInfo_CallRedialChanScanList_IsNewScanListFlag:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CallRedialInfo_CallRedialChanScanList_pstScanChanInfo:%X\n" % struct.unpack('I', instream.read(4))])
        
        outstream.writelines(["FreqLockPara_FreqLockMode:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["FreqLockPara_CdmaBandClass:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["FreqLockPara_Sid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["FreqLockPara_Nid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["FreqLockPara_CdmaFreq:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["FreqLockPara_CdmaPn:%X\n" % struct.unpack('H', instream.read(2))])
        
        outstream.writelines(["OocScheduleInfo_OocCtxInfo_WaitSearchFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OocScheduleInfo_OocCtxInfo_CurPhase:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OocScheduleInfo_OocCtxInfo_CurTimes:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["OocScheduleInfo_OocCtxInfo_FirstFourAcqArrivedFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OocScheduleInfo_OocCtxInfo_AttemptTimesInDoTraffic:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OocScheduleInfo_OocCtxInfo_SceneSetFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OocScheduleInfo_OocCtxInfo_TotalTimerExpiredFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OocScheduleInfo_OocCtxInfo_1xMru0TimerExpiredCount:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["OocScheduleInfo_OocCtxInfo_OocSearchScene:%X\n" % struct.unpack('I', instream.read(4))])
        (Reserve,)           = struct.unpack('H', instream.read(2))
        outstream.writelines(["Reserve:%X\n" % Reserve])
        outstream.writelines(["OocScheduleInfo_StrategyCfg_PhaseNum:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OocScheduleInfo_StrategyCfg_OocScanStrategy:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OocScheduleInfo_StrategyCfg_1xOocDoTchPhase1TimerLen:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OocScheduleInfo_StrategyCfg_1xOocDoTchPhase2TimerLen:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OocScheduleInfo_StrategyCfg_1xMru0TimerMaxExpiredTimes:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        ulLooper        = 0
        while ulLooper < 8:
            outstream.writelines(["OocScheduleInfo_StrategyCfg_PhaseCfgInfo%d: " % ulLooper])
            outstream.writelines(["TotalTimeLen:%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["SleepTimeLen:%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["SrchNum:%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Mru0SearchTimerLen:%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["MinSleepTimerLen:%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Reserve:%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:%X\n" % struct.unpack('B', instream.read(1))])
            ulLooper = ulLooper + 1
            
        outstream.writelines(["EmcCallInfo_EmcState:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["EmcCallInfo_CallBackSrchCounter:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["EmcCallInfo_ExcludeSaveOhmFreqFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["EmcCallInfo_CallBackCfg_CallBackEnableFlg:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["EmcCallInfo_CallBackCfg_CallBackModeTimerLen:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["EmcCallInfo_CallOrignalSys_Sid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["EmcCallInfo_CallOrignalSys_Nid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["EmcCallInfo_CallOrignalSys_Freq_BandClass:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["EmcCallInfo_CallOrignalSys_Freq_Channel:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["EmcCallInfo_EmcCallRedialChanScanList_TotalNum:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["EmcCallInfo_EmcCallRedialChanScanList_CurScanIndex:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["EmcCallInfo_EmcCallRedialChanScanList_MaxScanChanSize:%X\n" % struct.unpack('H', instream.read(2))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["EmcCallInfo_EmcCallRedialChanScanList_IsNewScanListFlg:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["EmcCallInfo_EmcCallRedialChanScanList_pstScanChanInfo:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["EmcCallInfo_EmcRedialSysAcqCfg_RedialCount:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["EmcCallInfo_EmcRedialSysAcqCfg_RedialTimes:"])
        analysis_array_data_one_byte(instream, outstream, 12)
        outstream.writelines(["EmcCallInfo_EmcRedialSysAcqCfg_LastCampedSys_Sid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["EmcCallInfo_EmcRedialSysAcqCfg_LastCampedSys_Nid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["EmcCallInfo_EmcRedialSysAcqCfg_LastCampedSys_Freq_BandClass:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["EmcCallInfo_EmcRedialSysAcqCfg_LastCampedSys_Freq_Channel:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["EmcCallInfo_EmcRedialSysAcqCfg_EmcRedialMruList_SysNum:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        ulLooper        = 0
        while ulLooper < 12:
            outstream.writelines(["EmcCallInfo_EmcRedialSysAcqCfg_EmcRedialMruList_System%d: " % ulLooper])
            outstream.writelines(["Sid:%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Nid:%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Freq_BandClass:%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Freq_Channel:%X\n" % struct.unpack('H', instream.read(2))])
            ulLooper = ulLooper + 1
        outstream.writelines(["EmcCallInfo_EmcCallBackCfInfo_CfChannelNum:%X\n" % struct.unpack('H', instream.read(2))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        ulLooper        = 0
        while ulLooper < 3:
            outstream.writelines(["EmcCallInfo_EmcCallBackCfInfo_ChannelList%d: " % ulLooper])
            outstream.writelines(["BandClass:%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Channel:%X\n" % struct.unpack('H', instream.read(2))])
            ulLooper = ulLooper + 1
            
        outstream.writelines(["Cdma1xCustomPrefChan_EnableFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["Cdma1xCustomPrefChan_FreqNum:%X\n" % struct.unpack('H', instream.read(2))])
        ulLooper        = 0
        while ulLooper < 20:
            outstream.writelines(["Cdma1xCustomPrefChan_FreqList%d: " % ulLooper])
            outstream.writelines(["Channel:%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["BandClass:%X\n" % struct.unpack('H', instream.read(2))])
            ulLooper = ulLooper + 1
            
        outstream.writelines(["SrvAcqFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["TestConfig_ReadNvPrlDirectly:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["TestConfig_ReadDefaultPrl:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["TestConfig_NoCardModeCfgFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["TestConfig_IsMode1xAvailTimerLen:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["TestConfig_PrlCombinedFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["SysAcqNvimCfg_AddAvoidListCfg_IsNegSysAdd:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysAcqNvimCfg_AddAvoidListCfg_Reserve:"])
        analysis_array_data_one_byte(instream, outstream, 15)
        outstream.writelines(["SysAcqNvimCfg_NegPrefSysCmpCtrl_NegPrefSysCmpType:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysAcqNvimCfg_NegPrefSysCmpCtrl_Reserve:"])
        analysis_array_data_one_byte(instream, outstream, 15)

def analysis_cnas_mntn_log_CnasXccMntnSaveExcLog_info( instream, outstream):    
        outstream.writelines(["MainCtrlCtx_BufferMsgQueue_MsgNum:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        ulLooper        = 0
        while ulLooper < 5:
            outstream.writelines(["MainCtrlCtx_BufferMsgQueue_pastBufferMsg%d:" % ulLooper])
            outstream.writelines(["p is %X\n" % struct.unpack('I', instream.read(4))])
            ulLooper = ulLooper + 1
        outstream.writelines(["MainCtrlCtx_SeqNum:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MainCtrlCtx_LastestCallIndex:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["MainCtrlCtx_EmcCallCtrl_WaitFlashMsgRspFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MainCtrlCtx_EmcCallCtrl_EmcCallId:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MainCtrlCtx_EmcCallCtrl_MtVoiceCallId:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["MainCtrlCtx_EmcCallCtrl_FlashMsgSeqNum:%X\n" % struct.unpack('B', instream.read(1))])
        ulLooper        = 0
        while ulLooper < 7:
            outstream.writelines(["astSridInfo%d: " % ulLooper])
            outstream.writelines(["IsUsed:%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Srid:%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["So:%X " % struct.unpack('H', instream.read(2))])
            outstream.writelines(["ConnectId:%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:%X\n" % struct.unpack('B', instream.read(1))])
            ulLooper = ulLooper + 1
        outstream.writelines(["OrigCallIndexOrder_CallNum:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["OrigCallIndexOrder_CallIndex:"])
        analysis_array_data_one_byte(instream, outstream, 4)
        outstream.writelines(["CallNvimCfg_IsL3ErrReOrigCount:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CallNvimCfg_PrivacyMode:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CallNvimCfg_Reserve:"])
        analysis_array_data_one_byte(instream, outstream, 14)
        outstream.writelines(["CallNvimCfg_EccSrvCap:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CallNvimCfg_EccSrvStatus:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["PagingRspSoCfg_NoDataSrvRspSo33Flg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["IsAlreadyNtfLmmCallStart:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
def analysis_cnas_mntn_log_CnasXregMntnSaveExcLog_info( instream, outstream):
        outstream.writelines(["CnasXregStateInfo_RegEnableFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_DistRegFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_RegisterFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_IsVerChange:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_IsTchHandoff:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_PowerSaveDeregFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["CnasXregStateInfo_T57MState:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_RegTimerState:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_CurRegType:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_PowerOffDeregFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_CasState:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_BlkSys:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregStateInfo_BandClass:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CnasXregStateInfo_RegInitCount:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CnasXregStateInfo_RegCountMax:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CnasXregStateInfo_RemainderTimerLen:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CnasXregStateInfo_DistInfo_BaseLast:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CnasXregStateInfo_DistInfo_BaseLong:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CnasXregStateInfo_DistInfo_DistThrd:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CnasXregStateInfo_RegTypeMntn:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CnasXregStateInfo_RegResult:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CnasXregStateInfo_RegTypeNeeded:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["CnasXregSysMsgCont_Available:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_BandClass:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_Freq:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_Sid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_Nid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_PacketZoneId:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfoIncl:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_BaseStationInfoIncl:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_ServiceInfoIncl:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_MaxSlotCycleIndex:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_PRevInUse:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_RegZone:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_RegZoneNum:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_ZoneTimer:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_MultiSidFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_MultiNidFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_RegDistance:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_RegPeriod:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_HomeReg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_SidRoamReg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_NidRoamReg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_PowerUpReg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_PowerDownReg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_RegInfo_ParameterReg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_BaseStationInfo_BaseId:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_BaseStationInfo_BaseClass:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_BaseStationInfo_BaseLatitude:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_BaseStationInfo_BaseLongitude:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_ServiceInfo_MaxAltSo:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_ServiceInfo_SDBSupported:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_ServiceInfo_MoQos:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_ServiceInfo_ConcurrentSupported:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_ServiceInfo_MoPosSupported:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_ServiceInfo_ImsiI1_I2:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["CnasXregSysMsgCont_SysInfo_ServiceInfo_Mcc:%X\n" % struct.unpack('I', instream.read(4))])

def analysis_cnas_mntn_log_CnasHsmMntnSaveExcLog_info( instream, outstream):
        outstream.writelines(["HrpdConnCtrlInfo_HrpdConvertedCasStatus:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["HrpdConnCtrlInfo_HrpdOriginalCasStatus:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["HrpdConnCtrlInfo_HsmCallId:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["HrpdConnCtrlInfo_ConnStatus:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["HrpdConnCtrlInfo_IsFirstPdpActConnFlag:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionSeed:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionCtrlInfo_PublicData_TransmitATI_ATIType:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["SessionCtrlInfo_PublicData_TransmitATI_ATIValue:"])
        analysis_array_data_one_byte(instream, outstream, 4)
        outstream.writelines(["SessionCtrlInfo_PublicData_TransmitATI_AddrTimerLen:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionCtrlInfo_PublicData_ReceiveATIList_ATIRecordNum:%X\n" % struct.unpack('I', instream.read(4))])
        ulLooper        = 0
        while ulLooper < 5:
            outstream.writelines(["SessionCtrlInfo_PublicData_ReceiveATIList_ATIEntry%d:\n" % ulLooper])
            outstream.writelines(["ATIType:%X" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["ucReserve:%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["ucReserve:%X " % struct.unpack('B', instream.read(1))])
            outstream.writelines(["ucReserve:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["ATIValue: "])
            analysis_array_data_one_byte(instream, outstream, 4)
            outstream.writelines(["AddrTimerLen:%X\n" % struct.unpack('I', instream.read(4))])
            ulLooper = ulLooper + 1
        outstream.writelines(["SessionCtrlInfo_PublicData_UATIInfo_CurUATI:"])
        analysis_array_data_one_byte(instream, outstream, 16)   
        outstream.writelines(["SessionCtrlInfo_PublicData_UATIInfo_OldUATI:"])
        analysis_array_data_one_byte(instream, outstream, 16)
        outstream.writelines(["SessionCtrlInfo_PublicData_UATIInfo_SubnetInc:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_UATIInfo_UATIColorCode:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_UATIInfo_UATISubnetMask:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_UATIInfo_OldUATILen:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_LocInfo_Longitude:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionCtrlInfo_PublicData_LocInfo_Latitude:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionActCtrlCtx_SessionActTriedCntConnFail:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionActCtrlCtx_SessionActTriedCntOtherFail:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionActCtrlCtx_SessionActMaxCntConnFail:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionActCtrlCtx_SessionActMaxCntOtherFail:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionActCtrlCtx_SessionActTimerLen:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionActCtrlCtx_ScpActFailProtType:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionActCtrlCtx_ScpActFailProtSubType:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionActCtrlCtx_ReqSessionTypeForRetry:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionActCtrlCtx_IsExplicitlyConnDenyFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["SessionCtrlInfo_PublicData_HrpdSysInfo_ColorCode:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_HrpdSysInfo_SubNetMask:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_HrpdSysInfo_OhmParameterUpToDate:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_HrpdSysInfo_SecondaryColorCodeCount:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_HrpdSysInfo_SectorId:"])
        analysis_array_data_one_byte(instream, outstream, 16)
        outstream.writelines(["SessionCtrlInfo_PublicData_HrpdSysInfo_SecondaryColorCode:"])
        analysis_array_data_one_byte(instream, outstream, 7)
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["SessionCtrlInfo_PublicData_HrpdSysInfo_Longitude:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionCtrlInfo_PublicData_HrpdSysInfo_Latitude:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionCtrlInfo_PublicData_UATIAssignMsgSeq:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_UATIReqTransId:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_IsFirstSysAcq:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_RcvOhmScene:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SessionStatus:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_IsSessionNegOngoing:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_IsScpActive:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_StartUatiReqAfterSectorIdChgFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_WaitUatiAssignTimerLenInfo_Setup:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_WaitUatiAssignTimerLenInfo_Open:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["SessionCtrlInfo_PublicData_LatestSessionDeactReason:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_PrevUatiForSessionRestore:"])
        analysis_array_data_one_byte(instream, outstream, 16)
        outstream.writelines(["SessionCtrlInfo_PublicData_NegoSessionType:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_ReqSessionType:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_CurSessionRelType:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_StoreEsnMeidRslt_IsStored:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_StoreEsnMeidRslt_IsChanged:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["SessionCtrlInfo_PublicData_Modem0CardStatusChgInfo_IsPreCardPresent:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_Modem0CardStatusChgInfo_IsCurCardPresent:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["SessionCtrlInfo_PublicData_Modem1CardStatusChgInfo_IsPreCardPresent:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_Modem1CardStatusChgInfo_IsCurCardPresent:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["SessionCtrlInfo_PublicData_Modem2CardStatusChgInfo_IsPreCardPresent:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_Modem2CardStatusChgInfo_IsCurCardPresent:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["SessionCtrlInfo_PublicData_LastHrpdUERevInfo_SuppOnlyDo0:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_LastHrpdUERevInfo_SuppDoaWithMfpa:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_LastHrpdUERevInfo_SuppDoaWithEmfpa:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_LastHrpdUERevInfo_SuppDoaEhrpd:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_UatiReqRetryTimesWhenUatiAssignTimerExpireInAmpOpen:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_SendSessionCloseFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_ClearKATimerInConnOpenFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_RecoverEhrpdAvailFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_RecoverEhrpdCapAfterSessionCloseFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_CloseEhrpdCapAfterSyscfgNotSupportLteFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_EhrpdAvailFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_PriorUATAssignMsgSeq:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionCtrlInfo_PublicData_PriorSessionSeed:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionCtrlInfo_PublicData_PseudorandomNumber:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionCtrlInfo_PublicData_PaAccessAuthCtrlInfo_Subnet: "])
        analysis_array_data_one_byte(instream, outstream, 16)
        outstream.writelines(["SessionCtrlInfo_PublicData_PaAccessAuthCtrlInfo_Count:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["SessionCtrlInfo_PublicData_SectorIdOfLastUatiReq: "])
        analysis_array_data_one_byte(instream, outstream, 16)
        
        outstream.writelines(["HrpdAmpNegAttibInfo_MaxNoMonitorDistance:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["HrpdAmpNegAttibInfo_HardwareSeparableFromSession:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["HrpdAmpNegAttibInfo_SupportGAUPMaxNoMonitorDistance:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["HrpdAmpNegAttibInfo_ReducedSubnetMaskOffset:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["HrpdAmpNegAttibInfo_SupportSecondaryColorCodes:%X\n" % struct.unpack('H', instream.read(2))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        outstream.writelines(["KeepAliveCtrlCtx_ReferenceSysTick:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["KeepAliveCtrlCtx_KeepAliveReqTransId:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["KeepAliveCtrlCtx_ReceivedSysTime: "])
        analysis_array_data_four_byte(instream, outstream, 2)
        outstream.writelines(["KeepAliveCtrlCtx_KeepAliveTimerInfo_KeepAliveReqSndCount:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["KeepAliveCtrlCtx_KeepAliveTimerInfo_SysTickFwdTrafChan:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["KeepAliveCtrlCtx_KeepAliveTimerInfo_OldSysTickFwdTrafChan:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["KeepAliveCtrlCtx_KeepAliveTimerInfo_KeepAliveTimerLen:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["KeepAliveCtrlCtx_KeepAliveTimerInfo_TotalTimerRunCount:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["KeepAliveCtrlCtx_KeepAliveTimerInfo_TimerExpiredCount:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["KeepAliveCtrlCtx_SessionKeepAliveInfo_IsKeepAliveInfoValid:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["KeepAliveCtrlCtx_SessionKeepAliveInfo_TsmpClose:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["KeepAliveCtrlCtx_SessionKeepAliveInfo_TsmpCloseRemainTime:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["KeepAliveCtrlCtx_SessionKeepAliveInfo_PowerOffSysTime: "])
        analysis_array_data_four_byte(instream, outstream, 2)
        outstream.writelines(["MultiModeCtrlInfo_LteReqSuccFlg:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["SnpDataReqCtrlInfo_HsmSnpDataReqOpId:%X\n" % struct.unpack('H', instream.read(2))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["SnpDataReqCtrlInfo_SaveSnpDataReqOpId_SessionCloseOpId:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SnpDataReqCtrlInfo_SaveSnpDataReqOpId_UatiReqOpId:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SnpDataReqCtrlInfo_SaveSnpDataReqOpId_UatiCmplOpId:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SnpDataReqCtrlInfo_SaveSnpDataReqOpId_KeepAliveReqOpId:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SnpDataReqCtrlInfo_SaveSnpDataReqOpId_KeepAliveRspOpId:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["SnpDataReqCtrlInfo_SaveSnpDataReqOpId_HardWareIdRspOpId:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["LowPowerCtrlInfo_SlotVoteBox:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])

def analysis_cnas_mntn_log_CnasEHsmMntnSaveExcLog_info( instream, outstream):
        outstream.writelines(["EhrpdState:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionType:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["WorkMode:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["AirLinkExist:%X\n" % struct.unpack('I', instream.read(4))])
        
        ulLooper        = 0
        while ulLooper < 3:
            outstream.writelines(["\nLocalPdnBearInfo%d:\n" % ulLooper])
            outstream.writelines(["PdnId:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["InUsed:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Cid:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["IsPdnActive:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Epsbid:%X\n" % struct.unpack('I', instream.read(4))])
            outstream.writelines(["PdnAddr_PdnType:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PdnAddr_SynncToEsmIpv6Addr:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PdnAddr_Reserve:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PdnAddr_Reserve:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PdnAddr_Ipv4Addr:"])
            analysis_array_data_one_byte(instream, outstream, 4)
            outstream.writelines(["PdnAddr_Ipv6Addr:"])
            analysis_array_data_one_byte(instream, outstream, 16)
            outstream.writelines(["ApnLen:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Apn:"])
            analysis_array_data_one_byte(instream, outstream, 7)
            outstream.writelines(["AttachType:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PdnType:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Mtu:%X\n" % struct.unpack('H', instream.read(2))])
            outstream.writelines(["AuthType:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["RetryTotalCnt:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:%X\n" % struct.unpack('B', instream.read(1))])
            ulLooper = ulLooper + 1
            
        ulLooper        = 0
        while ulLooper < 3:
            outstream.writelines(["\nLtePdnBearInfo%d:\n" % ulLooper])
            outstream.writelines(["InUsed:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Cid:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PdnType:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Epsbid:%X\n" % struct.unpack('I', instream.read(4))])
            outstream.writelines(["PdnAddr_PdnType:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PdnAddr_SynncToEsmIpv6Addr:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PdnAddr_Reserve:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PdnAddr_Reserve:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["PdnAddr_Ipv4Addr:"])
            analysis_array_data_one_byte(instream, outstream, 4)
            outstream.writelines(["PdnAddr_Ipv6Addr:"])
            analysis_array_data_one_byte(instream, outstream, 16)
            outstream.writelines(["ApnLen:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Apn:"])
            analysis_array_data_one_byte(instream, outstream, 7)
            ulLooper = ulLooper + 1
        
def analysis_cnas_event_state_list_dump_info( instream, fileOffset, outstream):   
        ulLooperTest = 0
        
        #outstream.writelines(["\n**************************** analysis_cnas_event_state_list_dump_info enter! %d*******************************\n" % (fileOffset)])
        instream.seek(fileOffset)
        (ulBeginTick,)       = struct.unpack('I', instream.read(4))
        strBeginTick         = '%x'% ulBeginTick

        #outstream.writelines(["strModemLogBeginFlg         %-15s\n" % ( strBeginTick )])
        
        fileOffset = fileOffset + 4
        
        #outstream.writelines(["\n**************************** analysis_cnas_event_state_list_dump_info enter! %d*******************************\n" % (fileOffset)])
        
        ##### cnas #########        
        analysis_cnas_per_dump_info(instream, fileOffset, outstream, ulLooperTest)
        
        outstream.writelines(["\nLatestIndex:%d\n" % struct.unpack('I', instream.read(4))])
        
        outstream.writelines(["\nCnasCcbInfoStart:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["\n%-15s\n" % ("CnasCcbMntnSaveExcLog:")])
        analysis_cnas_mntn_log_CnasCcbMntnSaveExcLog_info( instream, outstream)
        
        outstream.writelines(["\nCnasXsdInfoStart:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["\n%-15s\n" % ("CnasXsdMntnSaveExcLog:")])
        analysis_cnas_mntn_log_CnasXsdMntnSaveExcLog_info( instream, outstream)
        
        outstream.writelines(["\nCnasXccInfoStart:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["\n%-15s\n" % ("CnasXccMntnSaveExcLog:")])
        analysis_cnas_mntn_log_CnasXccMntnSaveExcLog_info( instream, outstream)
        
        outstream.writelines(["\nCnasXregInfoStart:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["\n%-15s\n" % ("CnasXregMntnSaveExcLog:")])
        analysis_cnas_mntn_log_CnasXregMntnSaveExcLog_info( instream, outstream)
        
        outstream.writelines(["\nCnasHsmInfoStart:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["\n%-15s\n" % ("CnasHsmMntnSaveExcLog:")])
        analysis_cnas_mntn_log_CnasHsmMntnSaveExcLog_info( instream, outstream)
        
        outstream.writelines(["\nCnasEHsmInfoStart:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["\n%-15s\n" % ("CnasEHsmMntnSaveExcLog:")])
        analysis_cnas_mntn_log_CnasEHsmMntnSaveExcLog_info( instream, outstream)
        
        #outstream.writelines(["\nCnasHsdInfoStart:%X\n" % struct.unpack('I', instream.read(4))])
        
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
        strReceiveTime   = '%x'% ulReceiveTime

        strCnasFsmId = '%x' % ucCnasFsmId 
        strCnasState = '%x' % ucCnasState
   
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
        outstream.writelines(["CurrMruNum:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        ulLooper        = 0
        while ulLooper < 12:
            outstream.writelines(["\nHrpdSys%d:\n" % ulLooper])
            outstream.writelines(["Subnet: "])
            analysis_array_data_one_byte(instream, outstream, 16)
            outstream.writelines(["SubnetMask:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Freq_BandClass:%X\n" % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Freq_Channel:%X\n" % struct.unpack('H', instream.read(2))])
            ulLooper = ulLooper + 1

def analysis_cnas_mntn_log_AvoidFreqList_info( instream, outstream):
        outstream.writelines(["AvoidItemUsedNum:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["CurrAvoidReason:%X\n" % struct.unpack('B', instream.read(1))])
        
        ulLooper        = 0
        while ulLooper < 3:
            outstream.writelines(["\nAvoidFreqInfo%d:\n" % ulLooper])
            outstream.writelines(["UsedFlg:%X\n" % struct.unpack('I', instream.read(4))])
            outstream.writelines(["AvoidReason:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Reserve:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["StartSlice:%X\n" % struct.unpack('I', instream.read(4))])
            outstream.writelines(["ExpiredSliceNum:%X\n" % struct.unpack('I', instream.read(4))])
            outstream.writelines(["AvoidFreq_BandClass:%X\n" % struct.unpack('H', instream.read(2))])
            outstream.writelines(["AvoidFreq_Channel:%X\n" % struct.unpack('H', instream.read(2))])
            ulLooper = ulLooper + 1

def analysis_cnas_mntn_log_Redirection_info( instream, outstream):
        outstream.writelines(["ChanNum:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        ulLooper        = 0
        while ulLooper < 3:
            outstream.writelines(["\nChannel%d:\n" % ulLooper])
            outstream.writelines(["SystemType:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["BandClass:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["Channel:%X\n" % struct.unpack('H', instream.read(2))])
            ulLooper = ulLooper + 1

def analysis_cnas_mntn_log_HighPriority_info( instream, outstream):
        outstream.writelines(["FreqNum:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        
        ulLooper        = 0
        while ulLooper < 16:
            outstream.writelines(["\nFreqInfo%d:\n" % ulLooper])
            outstream.writelines(["Freq_BandClass:%X\n" % struct.unpack('H', instream.read(2))])
            outstream.writelines(["Freq_Channel:%X\n" % struct.unpack('H', instream.read(2))])
            outstream.writelines(["HrpdSysItem_AcqIndex:%X\n" % struct.unpack('H', instream.read(2))])
            outstream.writelines(["HrpdSysItem_SysIndex:%X\n" % struct.unpack('H', instream.read(2))])
            outstream.writelines(["HrpdSysItem_PrioLevel:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["HrpdSysItem_PrefNegSys:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["HrpdSysItem_Reserve:%X\n" % struct.unpack('B', instream.read(1))])
            outstream.writelines(["HrpdSysItem_Reserve:%X\n" % struct.unpack('B', instream.read(1))])
            ulLooper = ulLooper + 1

def analysis_cnas_mntn_log_HrpdSysInfo_info( instream, outstream):
        outstream.writelines(["Status:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["CampedHrpdSysInfo_Subnet:"])
        analysis_array_data_one_byte(instream, outstream, 16)
        outstream.writelines(["SubnetMask:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["Freq_BandClass:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["Freq_Channel:%X\n" % struct.unpack('H', instream.read(2))])

def analysis_cnas_mntn_log_OocScheduleInfo_info( instream, outstream):
        outstream.writelines(["OosCtxInfo_WaitSearchFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OosCtxInfo_CurrentPhase:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OosCtxInfo_CurrentTimes:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["OosCtxInfo_SceneSetFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["OosCtxInfo_HrpdMru0TimerExpiredCount:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["OosCtxInfo_OocSearchScene:%X\n" % struct.unpack('I', instream.read(4))])
        
        outstream.writelines(["ConfigInfo_Mru0SearchTimerLen:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ConfigInfo_PhaseNum:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["ConfigInfo_HrpdMru0TimerMaxExpiredTimes:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        ulLooper        = 0
        while ulLooper < 8:
            outstream.writelines(["\nConfigInfo_OocTimerInfo%d:\n" % ulLooper])
            outstream.writelines(["Times:%X\n" % struct.unpack('H', instream.read(2))])
            outstream.writelines(["TimerLen:%X\n" % struct.unpack('H', instream.read(2))])
            ulLooper = ulLooper + 1

def analysis_cnas_mntn_log_CasOhmHrpdSys_info( instream, outstream):
        outstream.writelines(["Subnet:"])
        analysis_array_data_one_byte(instream, outstream, 16)
        outstream.writelines(["SubnetMask:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["Freq_BandClass:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["Freq_Channel:%X\n" % struct.unpack('H', instream.read(2))])

def analysis_cnas_mntn_log_NetwkLostSysRec_info( instream, outstream):
        outstream.writelines(["HrpdSys_Subnet:"])
        analysis_array_data_one_byte(instream, outstream, 16)
        outstream.writelines(["HrpdSys_SubnetMask:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        outstream.writelines(["HrpdSys_Freq_BandClass:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["HrpdSys_Freq_Channel:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["LastRecSlice:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["NetwkLostCnt:%X\n" % struct.unpack('B', instream.read(1))])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])
        (ucReserve,)           = struct.unpack('B', instream.read(1))
        outstream.writelines(["ucReserve:%X\n" % ucReserve])

def analysis_cnas_mntn_log_SyncFreq_info( instream, outstream):
        outstream.writelines(["BandClass:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["Channel:%X\n" % struct.unpack('H', instream.read(2))])

def analysis_cnas_mntn_log_SysAcqSrlteInfo_info( instream, outstream):
        outstream.writelines(["IsSysAcqNoRfTimerExpired:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["HrpdSysAcqNoRfProtectTimerLen:%X\n" % struct.unpack('I', instream.read(4))])

def analysis_cnas_mntn_log_HrpdMatched1xSysInfo_info( instream, outstream):
        outstream.writelines(["Status:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["1xSys_Sid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["1xSys_Nid:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["1xSys_Freq_BandClass:%X\n" % struct.unpack('H', instream.read(2))])
        outstream.writelines(["1xSys_Freq_Channel:%X\n" % struct.unpack('H', instream.read(2))])
    
def analysis_cnas_mntn_log_SysAssistInfo_info( instream, outstream):
        outstream.writelines(["NoRfScene:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["ATStatus:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["SessionNegStatus:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["HrpdRfAvailFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["Mru0RelateFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SysCfgFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["NoRf1XUeStatus:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["UeSupportedBand:%X\n" % struct.unpack('I', instream.read(4))])
        outstream.writelines(["IsAbnormalLostFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["SessionRlt:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["IsSyncFreqInSpmListFlg:%X\n" % struct.unpack('B', instream.read(1))])
        outstream.writelines(["Reserve:%X\n" % struct.unpack('B', instream.read(1))])
    
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
        outstream.writelines(["ModeType:%X\n" % struct.unpack('I', instream.read(4))])
        
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
        outstream.writelines(["\nCnasHsdInfoStart:%X\n" % struct.unpack('I', instream.read(4))])        
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
        elif not version == '0x0001':
            print ("hidis version is %s" % (version))
            print ("current version is 0x0001")
            return error['ERR_CHECK_VERSION']
        elif not len == '0x3000':
            print ("hids len is %s" % (len))
            print ("current len is 0x3000")
            return error['ERR_CHECK_LEN']
        #########check parameter end##############
        ret = analysis_cnas_dump_info( infile, offset, outfile)

        return 0


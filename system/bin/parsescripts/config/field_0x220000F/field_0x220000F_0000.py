#!/usr/bin/env python3
# coding=utf-8
"""
功能：analysis guphy dump bin
版权信息：华为技术有限公司，版权所有（C）2010-2019
修改记录：2016-01-22  创建
"""

import struct
import os
import sys
import string

from UPHY_ERR_CODE_ENUM import UPHY_GetErrCode
from PlatForm_Rat_Type import UPHY_GetRatType
from Rcm_RatMode import RCM_GetRatMode

from Uphy_Apm_Module import Uphy_Get_Apm_Module_Id
from Uphy_Apm_Module import Uphy_Get_Oam_Work_Mode
from Uphy_Apm_Module import Uphy_Get_Oam_Business_Type
from Uphy_Apm_Module import Uphy_Get_Bool_Business_Type

from Uphy_Operate_Func import UphySetModemModeStatus
from Uphy_Operate_Func import UphyIsModeExistBit

GLOBAL_MODEM_GU_ACTIVE_STATUS           = 0;

GLOBAL_MODEM0_G_ACTIVE_STATUS           = 0x0001
GLOBAL_MODEM0_U_ACTIVE_STATUS           = 0x0002
GLOBAL_MODEM1_G_ACTIVE_STATUS           = 0x0003
GLOBAL_MODEM1_U_ACTIVE_STATUS           = 0x0004
GLOBAL_MODEM2_G_ACTIVE_STATUS           = 0x0005

GLOBAL_UPHY_VOS_RATMODE_MAX_NUM         = 6
GLOBAL_UPHY_LOCK_CNT_NUM                = 2

MACRO_MODEM0_GPHY_EXISIT                = 2532

MACRO_MODEM0_ADDR_LENGTH                = 2532
MACRO_MODEM1_ADDR_LENGTH                = 2088
MACRO_MODEM2_ADDR_LENGTH                = 1232
MACRO_WPHY_INFO_LENGTH                  = 736
MACRO_GPHY_INFO_LENGTH                  = 792

UPHY_INIT_MODEM_MAX_NUM                 = 3

UPHY_SPIN_LOCKTYPE_MAX_NUM              = 8

UPHY_MNTN_PID_MSG_TRACE_NUM             = 32
UPHY_MNTN_PHY_MSG_TRACE_NUM             = 20

UPHY_DRX_MNTN_NUM                       = 4
UPHY_DRX_MNTN_ERR_NUM                   = 10

MACRO_NAS_MNTN_LOG_MSG_INFO_SIZE        = 16


def analysis_guphy_modem0_InitCtx_SpinLock_Info( instream, fileOffset, outstream ):

        global  GLOBAL_UPHY_LOCK_CNT_NUM
        
        UphySpinLockIdx       = 0

        while UphySpinLockIdx < UPHY_SPIN_LOCKTYPE_MAX_NUM:
                (enSpinLockId,)                 = struct.unpack('H', instream.read(2))
                strSpinLockId                   = '%x'% enSpinLockId
                outstream.writelines(["%-80s%-2s%-46s\n" % ("\nenSpinLockId:"," 0x",strSpinLockId)])

                (uhwRsv,)                       = struct.unpack('H', instream.read(2))
                strRsv                          = '%x'% uhwRsv

                (stSpinLockTask,)               = struct.unpack('I', instream.read(4))
                strSpinLockTask                  = '%x'% stSpinLockTask
                outstream.writelines(["%-80s%-2s%-46s\n" % ("stSpinLockTask:","0x",strSpinLockTask)])
                
                (uwLockLevel,)                  = struct.unpack('I', instream.read(4))
                strLockLevel                    = '%x'% uwLockLevel
                outstream.writelines(["%-80s%-2s%-46s\n" % ("uwLockLevel:","0x",strLockLevel)])
                
                lockContIdx = 0
                while lockContIdx < GLOBAL_UPHY_LOCK_CNT_NUM:
                        (uwLockCount,)                 = struct.unpack('I', instream.read(4))
                        strLockCount                   = '%x'% uwLockCount
                        outstream.writelines(["%-80s%-2s%-46s\n" % ( "auwLockCount:","0x",strLockCount)])
                        lockContIdx = lockContIdx + 1

                UphySpinLockIdx                 = UphySpinLockIdx + 1

def analysis_guphy_modem0_InitCtx_Platform_Info( instream, fileOffset, outstream ):
        ModemIdx           = 0

        global  GLOBAL_MODEM_GU_ACTIVE_STATUS

        while ModemIdx < UPHY_INIT_MODEM_MAX_NUM:
                PlatFormIdx        = 0

                strModemIdx          = '%x'% ModemIdx

                (uwReadNvResult,)       = struct.unpack('I', instream.read(4))
                strReadNvResult          = '%x'% uwReadNvResult
                outstream.writelines(["\nastPlatformInfo[%s]%-60s 0x%-60s\n" % ( strModemIdx,".uwReadNvResult:",strReadNvResult )])

                (uwReadNvSlice,)       = struct.unpack('I', instream.read(4))
                strReadNvSlice          = '%x'% uwReadNvSlice
                outstream.writelines(["astPlatformInfo[%s]%-60s 0x%-30s\n" % ( strModemIdx,".uwReadNvSlice:",strReadNvSlice )])

                (usRatNum,)       = struct.unpack('H', instream.read(2))
                strRatNum          = '%x'% usRatNum
                outstream.writelines(["astPlatformInfo[%s].stPlatform%-50s0x%-30s\n" % ( strModemIdx,".usRatNum:",strRatNum )])

                while PlatFormIdx < GLOBAL_UPHY_VOS_RATMODE_MAX_NUM:
                        strPlatFormIdx    = '%x'% PlatFormIdx

                        (enRatList,)      = struct.unpack('H', instream.read(2))
                        strRatList        = UPHY_GetRatType(enRatList, GLOBAL_UPHY_VOS_RATMODE_MAX_NUM)

                        #GLOBAL_MODEM_GU_ACTIVE_STATUS = UphySetModemModeStatus( strRatList,ModemIdx )

                        outstream.writelines(["astPlatformInfo[%s].stPlatform.enRatList[%s]:                                    %-30s\n" % ( strModemIdx,strPlatFormIdx,strRatList )])

                        PlatFormIdx       = PlatFormIdx + 1

                PlatFormIdx        = 0
                while PlatFormIdx < GLOBAL_UPHY_VOS_RATMODE_MAX_NUM:
                        strPlatFormIdx    = '%x'% PlatFormIdx
                        (uhwActiveResult,)      = struct.unpack('H', instream.read(2))
                        strActiveResult         = '%x'% uhwActiveResult
                        outstream.writelines(["astPlatformInfo[%s].auhwActiveResult[%s]:%-40s0x%-80s\n" % ( strModemIdx,strPlatFormIdx," ",strActiveResult )])

                        PlatFormIdx       = PlatFormIdx + 1

                (uhwRsv,)      = struct.unpack('H', instream.read(2))

                PlatFormIdx        = 0
                while PlatFormIdx < GLOBAL_UPHY_VOS_RATMODE_MAX_NUM:
                        strPlatFormIdx    = '%x'% PlatFormIdx
                        (uwActFinishSlice,)      = struct.unpack('I', instream.read(4))
                        strActFinishSlice         = '%x'% uwActFinishSlice
                        outstream.writelines(["astPlatformInfo[%s].uwActFinishSlice[%s]:%-40s0x%-80s\n" % ( strModemIdx,strPlatFormIdx,"",strActFinishSlice )])

                        PlatFormIdx       = PlatFormIdx + 1

                ModemIdx       = ModemIdx + 1

def analysis_guphy_modem0_RcmExc_Info( instream, fileOffset, outstream ):
        (rfPrepareTime,)         = struct.unpack('I', instream.read(4))
        strRfPrepareTime         = '%x'% rfPrepareTime
        outstream.writelines(["%-80s%-2s%-46s" % ("\nrfPrepareTime:"," 0x",strRfPrepareTime)])

        (rfExecuteTime,)         = struct.unpack('I', instream.read(4))
        strRfExecuteTime         = '%x'% rfExecuteTime
        outstream.writelines(["%-80s%-2s%-46s" % ("\nrfExecuteTime:"," 0x",strRfExecuteTime)])

        (rfRptMode,)             = struct.unpack('I', instream.read(4))
        strRatMode               = RCM_GetRatMode(rfRptMode)
        strRfRptMode             = '%x'% rfRptMode + '(' + strRatMode + ')'
        outstream.writelines(["%-80s%-2s%-46s" % ("\nrfRptMode:"," 0x",strRfRptMode)])

        (curSysTime,)            = struct.unpack('I', instream.read(4))
        strCurSysTime            = '%x'% curSysTime
        outstream.writelines(["%-80s%-2s%-46s" % ("\ncurSysTime:"," 0x",strCurSysTime)])

        (rfProcState,)           = struct.unpack('H', instream.read(2))
        strRfProcState           = '%x'% rfProcState
        outstream.writelines(["%-80s%-2s%-46s" % ("\nrfProcState:"," 0x",strRfProcState)])

        (rfPreemptState,)        = struct.unpack('H', instream.read(2))
        strRfPreemptState        = '%x'% rfPreemptState
        outstream.writelines(["%-80s%-2s%-46s" % ("\nrfPreemptState:"," 0x",strRfPreemptState)])

        (rfSuspendState,)        = struct.unpack('H', instream.read(2))
        strRfSuspendState        = '%x'% rfSuspendState
        outstream.writelines(["%-80s%-2s%-46s" % ("\nrrfSuspendState:"," 0x",strRfSuspendState)])

        (rficId,)                = struct.unpack('H', instream.read(2))
        strRficId                = '%x'% rficId
        outstream.writelines(["%-80s%-2s%-46s\n" % ("\nrficId:"," 0x",strRficId)])

def analysis_guphy_modem0_InitCtx_ModemAct_Info( instream, fileOffset, outstream):
        ulLooper        = 0

        outstream.writelines(["%-100s%-80s\n" % ("Modem", "ModemActFlag")])
        while ulLooper < UPHY_INIT_MODEM_MAX_NUM:
                (uwModemActFlag,)            = struct.unpack('I', instream.read(4))
                strModemActFlag              = Uphy_Get_Bool_Business_Type(uwModemActFlag)
                strLooper                    = '%x'% ulLooper
                outstream.writelines(["0x%-98s%-100s\n" % (strLooper,strModemActFlag)])
                ulLooper = ulLooper + 1

def analysis_guphy_modem0_InitCtx_Active_Status_Info( instream, fileOffset, outstream):
        global GLOBAL_UPHY_VOS_RATMODE_MAX_NUM
        ModemIdx        = 0

        outstream.writelines(["%-50s%-50s%-60s\n" % ("Modem", "RatMode", "ActiveStatus")])
        while ModemIdx < UPHY_INIT_MODEM_MAX_NUM:
                RatModIdx       = 0
                while RatModIdx < GLOBAL_UPHY_VOS_RATMODE_MAX_NUM:
                        (uwActStatus,)                  = struct.unpack('I', instream.read(4))
                        strActStatus                    = '%x'% uwActStatus
                        strModemIdx                     = '%x'% ModemIdx
                        strRatModIdx                    = UPHY_GetRatType(RatModIdx, GLOBAL_UPHY_VOS_RATMODE_MAX_NUM)
                        outstream.writelines(["0x%-48s%-50s0x%-75s\n" % (strModemIdx,strRatModIdx,strActStatus)])

                        RatModIdx       = RatModIdx + 1
                ModemIdx        = ModemIdx + 1

                outstream.writelines("\n")
                RatModIdx       = 0



def analysis_guphy_modem0_dump_comm_info( instream, fileOffset, outstream ):
        outstream.writelines(["\n***************************************************************************************************************\n"])
        outstream.writelines(["\n*                                         UPHY_APM_SAVE_EXC_COMM_INFO                                         *\n"])
        outstream.writelines(["\n***************************************************************************************************************\n"])
        outstream.writelines("\n")

        instream.seek(fileOffset)

        (uwRfVersion,)          = struct.unpack('I', instream.read(4))
        strRfVersion            =  '%x'% uwRfVersion
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwRfVersion",strRfVersion )])

        fileOffset = fileOffset + 4

        (uwAbbVersion,)         = struct.unpack('I', instream.read(4))
        strAbbVersion           =  '%x'% uwAbbVersion
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwAbbVersion",strAbbVersion )])

        fileOffset = fileOffset + 4

        outstream.writelines(["\n******************************************UPHY_COMM_CONTEXT_INFO******************************************\n"])

        (enUphyCommMuiltiModeModemState,)       = struct.unpack('I', instream.read(4))
        strUphyCommMuiltiModeModemState         = Uphy_Get_Bool_Business_Type(enUphyCommMuiltiModeModemState)
        outstream.writelines(["%-100s%-50s\n" % ( "enUphyCommMuiltiModeModemState",strUphyCommMuiltiModeModemState )])
        fileOffset = fileOffset + 4

        outstream.writelines(["\n******************************************UPHY_COMM_INIT_CONTEXT_INFO**************************************\n"])

        (uwFidInitSlice,)       =struct.unpack('I', instream.read(4))
        strFidInitSlice         = '%x'% uwFidInitSlice
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwFidInitSlice",strFidInitSlice )])
        fileOffset = fileOffset + 4

        (uwReadNvResult,)       = struct.unpack('I', instream.read(4))
        strReadNvResult           = '%x'% uwReadNvResult
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwReadNvResult",strReadNvResult )])
        fileOffset = fileOffset + 4

        (uhwPhyAutoInitFlg,)       = struct.unpack('I', instream.read(4))
        strPhyAutoInitFlg           = '%x'% uhwPhyAutoInitFlg
        outstream.writelines(["%-100s0x%-50s\n" % ( "uhwPhyAutoInitFlg",strPhyAutoInitFlg )])
        fileOffset = fileOffset + 4

        (uwReadNvSlice,)       = struct.unpack('I', instream.read(4))
        strReadNvSlice           = '%x'% uwReadNvSlice
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwReadNvSlice",strReadNvSlice )])
        fileOffset = fileOffset + 4

        (uwNasInitSlice,)       = struct.unpack('I', instream.read(4))
        strNasInitSlice         = '%x'% uwNasInitSlice
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwNasInitSlice",strNasInitSlice )])
        fileOffset = fileOffset + 4

        (enInitResult,)         = struct.unpack('I', instream.read(4))
        strInitResult           = UPHY_GetErrCode(enInitResult)
        outstream.writelines(["%-100s%-50s\n" % ( "enInitResult",strInitResult )])
        fileOffset = fileOffset + 4

        (uwInitFinishSlice,)    = struct.unpack('I', instream.read(4))
        strInitFinishSlice      = '%x'% uwInitFinishSlice
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwInitFinishSlice",strInitFinishSlice )])
        fileOffset = fileOffset + 4

        (uhwRcmNoticeIndFlag,)  = struct.unpack('H', instream.read(2))
        strRcmNoticeIndFlag     = '%x'% uhwRcmNoticeIndFlag
        outstream.writelines(["%-100s0x%-50s\n" % ( "uhwRcmNoticeIndFlag",strRcmNoticeIndFlag )])

        (uhwUphyCommInitFlag,)  = struct.unpack('H', instream.read(2))
        strUphyCommInitFlag     = '%x'% uhwUphyCommInitFlag
        outstream.writelines(["%-100s0x%-50s\n" % ( "uhwUphyCommInitFlag",strUphyCommInitFlag )])

        outstream.writelines(["\n********************************************auwModemActFlag[]********************************************\n"])

        analysis_guphy_modem0_InitCtx_ModemAct_Info( instream, fileOffset, outstream )
        fileOffset = fileOffset + 12

        outstream.writelines(["\n********************************************auwActiveStatus[]********************************************\n"])
        analysis_guphy_modem0_InitCtx_Active_Status_Info( instream, fileOffset, outstream )

        outstream.writelines(["\n********************************************astPlatformInfo[]********************************************\n"])
        analysis_guphy_modem0_InitCtx_Platform_Info( instream, fileOffset, outstream )

        outstream.writelines(["\n********************************************astSpinLockInfo[]********************************************\n"])
        try:
                analysis_guphy_modem0_InitCtx_SpinLock_Info( instream, fileOffset, outstream )
        except:
                import traceback
                outstream.writelines([traceback.format_exc()])

        outstream.writelines(["\n********************************************rcmExcInfo[]********************************************\n"])
        analysis_guphy_modem0_RcmExc_Info( instream, fileOffset, outstream )

def analysis_guphy_modemX_Apm_Module_Status_Info( instream, fileOffset, outstream ):
        (enPhyID,)              = struct.unpack('H', instream.read(2))
        strPhyID                =  Uphy_Get_Apm_Module_Id( enPhyID )
        outstream.writelines(["%-100s%-50s\n" % ( "enPhyID",strPhyID )])

        (uhwInit,)              = struct.unpack('H', instream.read(2))
        strInit                 =  '%x'% uhwInit
        outstream.writelines(["%-100s0x%-50s\n" % ( "uhwInit",strInit )])

        (enWorkMode,)           = struct.unpack('H', instream.read(2))
        strWorkMode             =  Uphy_Get_Oam_Work_Mode( enWorkMode )
        outstream.writelines(["%-100s%-50s\n" % ( "enWorkMode",strWorkMode )])

        (enBusinessType,)       = struct.unpack('H', instream.read(2))
        strBusinessType         =  Uphy_Get_Oam_Business_Type( enBusinessType )
        outstream.writelines(["%-100s%-50s\n" % ( "enBusinessType",strBusinessType )])

        (enMasterMode,)         = struct.unpack('I', instream.read(4))
        strMasterMode           = UPHY_GetRatType(enMasterMode, GLOBAL_UPHY_VOS_RATMODE_MAX_NUM)
        outstream.writelines(["%-100s%-50s\n" % ( "enMasterMode",strMasterMode )])

        (enSlaveMode,)         = struct.unpack('I', instream.read(4))
        strSlaveMode           = UPHY_GetRatType(enSlaveMode, GLOBAL_UPHY_VOS_RATMODE_MAX_NUM)
        outstream.writelines(["%-100s%-50s\n" % ( "enSlaveMode",strSlaveMode )])

def    analysis_guphy_modemX_wphy_master_drx_mntn_Info( instream, fileOffset, outstream ):

        (uwForbidSleepReason,)                    = struct.unpack('I', instream.read(4))
        strForbidSleepReason                      =  '%x'% uwForbidSleepReason
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwForbidSleepReason",strForbidSleepReason )])

        (uwSndSleepReqCnt,)                    = struct.unpack('I', instream.read(4))
        strSndSleepReqCnt                      =  '%x'% uwSndSleepReqCnt
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwSndSleepReqCnt",strSndSleepReqCnt )])

        (uwSndSleepReqSlice,)                    = struct.unpack('I', instream.read(4))
        strSndSleepReqSlice                      =  '%x'% uwSndSleepReqSlice
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwSndSleepReqSlice",strSndSleepReqSlice )])

        (uwDrxRcvSleepSlice,)                    = struct.unpack('I', instream.read(4))
        strDrxRcvSleepSlice                      =  '%x'% uwDrxRcvSleepSlice
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwDrxRcvSleepSlice",strDrxRcvSleepSlice )])

        (uwDrxSendSleepSlice,)                    = struct.unpack('I', instream.read(4))
        strDrxSendSleepSlice                      =  '%x'% uwDrxSendSleepSlice
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwDrxSendSleepSlice",strDrxRcvSleepSlice )])

        (uwDrxNeedWakeSlice,)                    = struct.unpack('I', instream.read(4))
        strDrxNeedWakeSlice                      =  '%x'% uwDrxNeedWakeSlice
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwDrxNeedWakeSlice",strDrxNeedWakeSlice )])

        (uwDrxRcvWakeSlice,)                    = struct.unpack('I', instream.read(4))
        strDrxRcvWakeSlice                      =  '%x'% uwDrxRcvWakeSlice
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwDrxRcvWakeSlice",strDrxRcvWakeSlice )])

        (uwDrxSendWakeSlice,)                    = struct.unpack('I', instream.read(4))
        strDrxRcvWakeSlice                      =  '%x'% uwDrxSendWakeSlice
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwDrxSendWakeSlice",strDrxRcvWakeSlice )])

        (uwRcvWakeMsgCnt,)                    = struct.unpack('I', instream.read(4))
        strRcvWakeMsgCnt                      =  '%x'% uwRcvWakeMsgCnt
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwRcvWakeMsgCnt",strRcvWakeMsgCnt )])

        (uwRcvWakeMsgSlice,)                    = struct.unpack('I', instream.read(4))
        strRcvWakeMsgSlice                      =  '%x'% uwRcvWakeMsgSlice
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwRcvWakeMsgSlice",strRcvWakeMsgSlice )])

        (uwDcStartSlice,)                    = struct.unpack('I', instream.read(4))
        strDcStartSlice                      =  '%x'% uwDcStartSlice
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwDcStartSlice",strDcStartSlice )])

        (uwDcEndSlice,)                    = struct.unpack('I', instream.read(4))
        strDcEndSlice                      =  '%x'% uwDcEndSlice
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwDcEndSlice",strDcEndSlice )])

        (uwMpstartslice,)                    = struct.unpack('I', instream.read(4))
        strMpstartslice                      =  '%x'% uwMpstartslice
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwMpstartslice",strMpstartslice )])

        (uwRcvMpSrchIntCnt,)                    = struct.unpack('I', instream.read(4))
        strRcvMpSrchIntCnt                      =  '%x'% uwRcvMpSrchIntCnt
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwRcvMpSrchIntCnt",strRcvMpSrchIntCnt )])

        (uwRcvMpSrchIntSlice,)                    = struct.unpack('I', instream.read(4))
        strRcvMpSrchIntSlice                      =  '%x'% uwRcvMpSrchIntSlice
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwRcvMpSrchIntSlice",strRcvMpSrchIntSlice )])

        (uwOpenSlotIntCnt,)                    = struct.unpack('I', instream.read(4))
        strOpenSlotIntCnt                      =  '%x'% uwOpenSlotIntCnt
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwOpenSlotIntCnt",strOpenSlotIntCnt )])

        (uwOpenSlotIntSlice,)                    = struct.unpack('I', instream.read(4))
        strOpenSlotIntSlice                      =  '%x'% uwOpenSlotIntSlice
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwOpenSlotIntSlice",strOpenSlotIntSlice )])

        (uwPichSetupSlice,)                    = struct.unpack('I', instream.read(4))
        strPichSetupSlice                      =  '%x'% uwPichSetupSlice
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwPichSetupSlice",strPichSetupSlice )])

        (uwPiIntSlice,)                    = struct.unpack('I', instream.read(4))
        strPiIntSlice                      =  '%x'% uwPiIntSlice
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwPiIntSlice",strPiIntSlice )])

        outstream.writelines(["\n******************************** stPiRealTime **********************\n"])
        (uhwSfn,)                       = struct.unpack('H', instream.read(2))
        strSfn                          =  '%x'% uhwSfn
        outstream.writelines(["%-100s0x%-50s\n" % ( "uhwSfn",strSfn )])

        (uhwCfn,)                       = struct.unpack('H', instream.read(2))
        strCfn                          =  '%x'% uhwCfn
        outstream.writelines(["%-100s0x%-50s\n" % ( "uhwCfn",strCfn )])

        (uhwSlot,)                       = struct.unpack('H', instream.read(2))
        strSlot                          =  '%x'% uhwSlot
        outstream.writelines(["%-100s0x%-50s\n" % ( "uhwSlot",strSlot )])

        (uhwChip,)                       = struct.unpack('H', instream.read(2))
        strChip                          =  '%x'% uhwChip
        outstream.writelines(["%-100s0x%-50s\n" % ( "uhwChip",strChip )])

        outstream.writelines(["\n******************************** stPichSetupTime **********************\n"])
        (uhwSfn,)                       = struct.unpack('H', instream.read(2))
        strSfn                          =  '%x'% uhwSfn
        outstream.writelines(["%-100s0x%-50s\n" % ( "uhwSfn",strSfn )])

        (uhwCfn,)                       = struct.unpack('H', instream.read(2))
        strCfn                          =  '%x'% uhwCfn
        outstream.writelines(["%-100s0x%-50s\n" % ( "uhwCfn",strCfn )])

        (uhwSlot,)                       = struct.unpack('H', instream.read(2))
        strSlot                          =  '%x'% uhwSlot
        outstream.writelines(["%-100s0x%-50s\n" % ( "uhwSlot",strSlot )])

        (uhwChip,)                       = struct.unpack('H', instream.read(2))
        strChip                          =  '%x'% uhwChip
        outstream.writelines(["%-100s0x%-50s\n" % ( "uhwChip",strChip )])

def    analysis_guphy_modemX_wphy_slave_drx_mntn_Info( instream, fileOffset, outstream ):

        (uwForbidSleepReason,)                    = struct.unpack('H', instream.read(2))
        strForbidSleepReason                      =  '%x'% uwForbidSleepReason
        outstream.writelines(["%-100s0x%-50s\n" % ( "uhwForbidSleepReason",strForbidSleepReason )])

        instream.read(2)

        (uwSndSleepReqCnt,)                    = struct.unpack('I', instream.read(4))
        strSndSleepReqCnt                      =  '%x'% uwSndSleepReqCnt
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwSndSleepReqCnt",strSndSleepReqCnt )])

        (uwSndSleepReqSlice,)                    = struct.unpack('I', instream.read(4))
        strSndSleepReqSlice                      =  '%x'% uwSndSleepReqSlice
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwSndSleepReqSlice",strSndSleepReqSlice )])

        (uwRcvWakeMsgCnt,)                    = struct.unpack('I', instream.read(4))
        strRcvWakeMsgCnt                      =  '%x'% uwRcvWakeMsgCnt
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwRcvWakeMsgCnt",strRcvWakeMsgCnt )])

        (uwRcvWakeMsgSlice,)                    = struct.unpack('I', instream.read(4))
        strRcvWakeMsgSlice                      =  '%x'% uwRcvWakeMsgSlice
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwRcvWakeMsgSlice",strRcvWakeMsgSlice )])

        (uwOpenSlotIntCnt,)                    = struct.unpack('I', instream.read(4))
        strOpenSlotIntCnt                      =  '%x'% uwOpenSlotIntCnt
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwOpenSlotIntCnt",strOpenSlotIntCnt )])

        (uwOpenSlotIntSlice,)                    = struct.unpack('I', instream.read(4))
        strOpenSlotIntSlice                      =  '%x'% uwOpenSlotIntSlice
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwOpenSlotIntSlice",strOpenSlotIntSlice )])

def    analysis_guphy_modemX_mntn_wphy_drx_mntn_Info( instream, fileOffset, outstream ):
        outstream.writelines(["\n********************UPHY_TOOL_WPHY_DRX_MNTN_INFO**********************\n"])
        analysis_guphy_modemX_wphy_master_drx_mntn_Info( instream, fileOffset, outstream )

        outstream.writelines(["\n********************UPHY_TOOL_UPHY_WDRX_MNTN_INFO**********************\n"])
        analysis_guphy_modemX_wphy_slave_drx_mntn_Info( instream, fileOffset, outstream )


def     analysis_guphy_modem0_dump_wphy_info( instream, fileOffset, outstream ):
        outstream.writelines(["\n***************************************************************************************************************\n"])
        outstream.writelines(["\n*                                         UPHY_APM_SAVE_EXC_WPHY_INFO                                         *\n"])
        outstream.writelines(["\n***************************************************************************************************************\n"])
        outstream.writelines("\n")
        instream.seek(fileOffset)

        (uhwSysState,)          = struct.unpack('H', instream.read(2))
        strSysState             =  '%x'% uhwSysState
        outstream.writelines(["%-100s0x%-50s\n" % ( "uhwSysState",strSysState )])

        (uhwDsdsFlag,)          = struct.unpack('H', instream.read(2))
        strDsdsFlag             =  '%x'% uhwDsdsFlag
        outstream.writelines(["%-100s0x%-50s\n" % ( "uhwDsdsFlag",strDsdsFlag )])

        fileOffset = fileOffset + 4

        (uhwTasEn,)             = struct.unpack('I', instream.read(4))
        strTasEn                =  '%x'% uhwTasEn
        outstream.writelines(["%-100s0x%-50s\n" % ( "uhwTasEn",strTasEn )])

        outstream.writelines(["\n******************************************UPHY_APM_MODULE_STATUS_INFO******************************************\n"])
        analysis_guphy_modemX_Apm_Module_Status_Info( instream, fileOffset, outstream )

        outstream.writelines(["\n******************************************UPHY_MNTN_PHY_MSG_TRACE_BUF_INFO*************************************\n"])
        analysis_guphy_modemX_Mntn_Phy_Msg_Buf_Info( instream, fileOffset, outstream )

       # outstream.writelines(["\n******************************UPHY_WPHY_DRX_MNTN_INFO*************************\n"])
       # analysis_guphy_modemX_mntn_wphy_drx_mntn_Info( instream, fileOffset, outstream )

def    analysis_guphy_modemX_Mntn_Phy_Msg_Info( instream, fileOffset, outstream ):
        PhyMsgTraceIdx        = 0

        outstream.writelines(["\n********************************astSendMsgList[20]**********************\n"])
        outstream.writelines(["%-50s%-60s%-80s\n" % ("PhyMsgTraceIdx","uwMsgId", "uwInSlice")])

        while PhyMsgTraceIdx < UPHY_MNTN_PHY_MSG_TRACE_NUM:
                (uwMsgId,)                      = struct.unpack('I', instream.read(4))
                strMsgId                        = '%x'% uwMsgId

                (uwInSlice,)                    = struct.unpack('I', instream.read(4))
                strInSlice                      = '%x'% uwInSlice

                strPhyMsgTraceIdx               = '%x'% PhyMsgTraceIdx

                outstream.writelines(["0x%-50s0x%-60s0x%-80s\n" % (strPhyMsgTraceIdx,strMsgId,strInSlice)])

                PhyMsgTraceIdx                  = PhyMsgTraceIdx + 1

def analysis_guphy_modemX_Mntn_Phy_Msg_Buf_Info( instream, fileOffset, outstream ):

        outstream.writelines(["\n******************************************UPHY_MNTN_PID_MSG_TRACE_BUF_INFO*************************************\n"])
        analysis_guphy_modemX_Mntn_Pid_Msg_Buf_Info( instream, fileOffset, outstream )

        outstream.writelines(["\n******************************************UPHY_MNTN_SND_RCV_MSG_TRACE_BUF_INFO**********************************\n"])
        (uhwSendMsgTraceIdx,)   = struct.unpack('H', instream.read(2))
        strSendMsgTraceIdx      = '%x'% uhwSendMsgTraceIdx
        outstream.writelines(["%-100s0x%-50s\n" % ( "uhwSendMsgTraceIdx",strSendMsgTraceIdx )])

        (uhwRcvMsgTraceIdx,)    = struct.unpack('H', instream.read(2))
        strRcvMsgTraceIdx       = '%x'% uhwRcvMsgTraceIdx
        outstream.writelines(["%-100s0x%-50s\n" % ( "uhwRcvMsgTraceIdx",strRcvMsgTraceIdx )])

        outstream.writelines(["\n******************************************astSendMsgList[20]***************************************************\n"])
        analysis_guphy_modemX_Mntn_Phy_Msg_Info( instream, fileOffset, outstream )

        outstream.writelines(["\n******************************************astRcvMsgList[20]***************************************************\n"])
        analysis_guphy_modemX_Mntn_Phy_Msg_Info( instream, fileOffset, outstream )



def analysis_guphy_modemX_Mntn_Pid_Msg_Buf_Info( instream, fileOffset, outstream ):
        PidMsgTraceIdx        = 0

        (uwTraceIdx,)              = struct.unpack('I', instream.read(4))
        strTraceIdx                =  '%x'% uwTraceIdx

        outstream.writelines(["%-100s0x%-50s\n" % ( "uwTraceIdx",strTraceIdx )])

        outstream.writelines(["\n********************************astPidTraceList[32]**********************\n"])
        outstream.writelines(["%-25s%-25s%-25s%-25s\n" % ("PidMsgTraceIdx","uwTraceId", "uwInSlice", "uwOutSlice")])
        while PidMsgTraceIdx < UPHY_MNTN_PID_MSG_TRACE_NUM:
                (uwTraceId,)                    = struct.unpack('I', instream.read(4))
                strTraceId                      = '%x'% uwTraceId

                (uwInSlice,)                    = struct.unpack('I', instream.read(4))
                strInSlice                      = '%x'% uwInSlice

                (uwOutSlice,)                   = struct.unpack('I', instream.read(4))
                strOutSlice                     = '%x'% uwOutSlice

                strPidMsgTraceIdx               = '%x'% PidMsgTraceIdx

                outstream.writelines(["0x%-25s0x%-20s0x%-25s0x%-20s\n" % (strPidMsgTraceIdx,strTraceId,strInSlice,strOutSlice)])

                PidMsgTraceIdx                  = PidMsgTraceIdx + 1

def analysis_guphy_modemX_Drx_Gphy_Master_Info( instream, fileOffset, outstream ):
        outstream.writelines(["\n********************************auwSlpStatusErrSlice[4]**********************\n"])
        (uwSlpStatusErrCnt,)                    = struct.unpack('I', instream.read(4))
        strSlpStatusErrCnt                      =  '%x'% uwSlpStatusErrCnt
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwSlpStatusErrCnt",uwSlpStatusErrCnt )])

        DrxMntnIdx        = 0
        while DrxMntnIdx < UPHY_DRX_MNTN_NUM:
                (uwSlpStatusErrSlice,)          = struct.unpack('I', instream.read(4))
                strSlpStatusErrSlice            = '%x'% uwSlpStatusErrSlice

                strDrxMntnIdx                   = '%x'% DrxMntnIdx

                outstream.writelines(["%-s%-s%-100s%-s%-s\n" % ( "auwSlpStatusErrSlice[",strDrxMntnIdx,"]: ","0x",strSlpStatusErrSlice)])

                DrxMntnIdx                      = DrxMntnIdx + 1

        outstream.writelines(["\n********************************auwCallBackSleepFailCnt[4]**********************\n"])
        (uwCallBackSleepFailCnt,)                    = struct.unpack('I', instream.read(4))
        strCallBackSleepFailCnt                      =  '%x'% uwCallBackSleepFailCnt
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwCallBackSleepFailCnt",uwCallBackSleepFailCnt )])

        DrxMntnIdx        = 0
        while DrxMntnIdx < UPHY_DRX_MNTN_NUM:
                (uwSlpStatusFailSlice,)          = struct.unpack('I', instream.read(4))
                strSlpStatusErrSlice            = '%x'% uwSlpStatusFailSlice

                strDrxMntnIdx                   = '%x'% DrxMntnIdx

                outstream.writelines(["%-s%-s%-90s%-s%-s\n" % ( "auwCallBackSleepFailCnt[",strDrxMntnIdx,"]: ","0x",strSlpStatusErrSlice)])

                DrxMntnIdx                      = DrxMntnIdx + 1

        outstream.writelines(["\n********************************auwSleepLenErrCnt[4]**********************\n"])
        (uwCallBackSleepErrCnt,)                = struct.unpack('I', instream.read(4))
        strCallBackSleepErrCnt                  =  '%x'% uwCallBackSleepErrCnt
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwCallBackSleepLenErr",strCallBackSleepErrCnt )])

        DrxMntnIdx        = 0
        while DrxMntnIdx < UPHY_DRX_MNTN_NUM:
                (uwCallBackSleepLenErrSlice,)             = struct.unpack('I', instream.read(4))
                strCallBackSleepLenErrSlice               = '%x'% uwCallBackSleepLenErrSlice

                strDrxMntnIdx                   = '%x'% DrxMntnIdx

                outstream.writelines(["%-s%-s%-90s%-s%-s\n" % ( "auwSleepLenErrCnt[",strDrxMntnIdx,"]: ","0x",strCallBackSleepLenErrSlice)])

                DrxMntnIdx                      = DrxMntnIdx + 1

        outstream.writelines(["\n********************************auwWakeLenErrCnt[4]**********************\n"])
        (uwWakeLenErrCnt,)                      = struct.unpack('I', instream.read(4))
        strWakeLenErrCnt                        =  '%x'% uwWakeLenErrCnt
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwWakeLenErrCnt",strWakeLenErrCnt )])

        DrxMntnIdx        = 0
        while DrxMntnIdx < UPHY_DRX_MNTN_NUM:
                (uwWakeLenErrSlice,)            = struct.unpack('I', instream.read(4))
                strWakeLenErrSlice              = '%x'% uwWakeLenErrSlice

                strDrxMntnIdx                   = '%x'% DrxMntnIdx

                outstream.writelines(["%-s%-s%-90s%-s%-s\n" % ( "auwRcvWakeLenErrCnt[",strDrxMntnIdx,"]: ","0x",strWakeLenErrSlice)])

                DrxMntnIdx                      = DrxMntnIdx + 1

        (uwProtectTimerLen,)                      = struct.unpack('I', instream.read(4))
        strProtectTimerLen                        =  '%x'% uwProtectTimerLen
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwProtectTimerLen",strProtectTimerLen )])

        (uwGaugePara,)                      = struct.unpack('I', instream.read(4))
        strGaugePara                        =  '%x'% uwGaugePara
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwGaugePara",strGaugePara )])

        (uwSleepLen,)                      = struct.unpack('I', instream.read(4))
        strSleepLen                        =  '%x'% uwSleepLen
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwSleepLen",strSleepLen )])

        (uwClockSwitchLen,)                      = struct.unpack('I', instream.read(4))
        strClockSwitchLen                        =  '%x'% uwClockSwitchLen
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwClockSwitchLen",strClockSwitchLen )])

        (uwCalSleepLen,)                      = struct.unpack('I', instream.read(4))
        strCalSleepLen                        =  '%x'% uwCalSleepLen
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwCalSleepLen",strCalSleepLen )])

        (uwCalClkSwitchLen,)                      = struct.unpack('I', instream.read(4))
        strCalClkSwitchLen                        =  '%x'% uwCalClkSwitchLen
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwCalClkSwitchLen",strCalClkSwitchLen )])

        (uwExptAwakeSlice,)                      = struct.unpack('I', instream.read(4))
        strExptAwakeSlice                        =  '%x'% uwExptAwakeSlice
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwExptAwakeSlice",strExptAwakeSlice )])

        (uwRegRdSleepLen,)                      = struct.unpack('I', instream.read(4))
        strRegRdSleepLen                        =  '%x'% uwRegRdSleepLen
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwRegRdSleepLen",strRegRdSleepLen )])

        (uwRegRdClkSwitchLen,)                  = struct.unpack('I', instream.read(4))
        strRegRdClkSwitchLen                    =  '%x'% uwRegRdClkSwitchLen
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwRegRdClkSwitchLen",strRegRdClkSwitchLen )])

        (uwRcvSleepCnt,)                        = struct.unpack('I', instream.read(4))
        strRcvSleepCnt                          =  '%x'% uwRcvSleepCnt
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwRcvSleepCnt",strRcvSleepCnt )])

        (uwSndSleepCnt,)                      = struct.unpack('I', instream.read(4))
        strSndSleepCnt                        =  '%x'% uwSndSleepCnt
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwSndSleepCnt",strSndSleepCnt )])

        (uwLastSleepSlice,)                      = struct.unpack('I', instream.read(4))
        strLastSleepSlice                        =  '%x'% uwLastSleepSlice
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwLastSleepSlice",strLastSleepSlice )])

        (uwRcvWakeCnt,)                         = struct.unpack('I', instream.read(4))
        strRcvWakeCnt                           =  '%x'% uwRcvWakeCnt
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwRcvWakeCnt",strRcvWakeCnt )])

        (uwSndWakeCnt,)                         = struct.unpack('I', instream.read(4))
        strSndWakeCnt                           =  '%x'% uwSndWakeCnt
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwSndWakeCnt",strSndWakeCnt )])

        (uwGphyTimerCnt,)                         = struct.unpack('I', instream.read(4))
        strGphyTimerCnt                           =  '%x'% uwGphyTimerCnt
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwGphyTimerCnt",strGphyTimerCnt )])

        (uwRegTxcoSwitch,)                         = struct.unpack('I', instream.read(4))
        strRegTxcoSwitch                           =  '%x'% uwRegTxcoSwitch
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwRegTxcoSwitch",strRegTxcoSwitch )])

        (uwGphyTimerSlice,)                         = struct.unpack('I', instream.read(4))
        strGphyTimerSlice                           =  '%x'% uwGphyTimerSlice
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwGphyTimerSlice",strGphyTimerSlice )])

        outstream.writelines(["\n********************************auwRcvSleepSlice[4]**********************\n"])
        DrxMntnIdx        = 0
        while DrxMntnIdx < UPHY_DRX_MNTN_NUM:
                (uwRcvSleepSlice,)              = struct.unpack('I', instream.read(4))
                strRcvSleepSlice              = '%x'% uwRcvSleepSlice

                strDrxMntnIdx                   = '%x'% DrxMntnIdx

                outstream.writelines(["%-s%-s%-90s%-s%-s\n" % ( "auwRcvSleepSlice[",strDrxMntnIdx,"]: ","0x",strRcvSleepSlice)])

                DrxMntnIdx                      = DrxMntnIdx + 1

        outstream.writelines(["\n********************************auwSndSleepSlice[4]**********************\n"])
        DrxMntnIdx        = 0
        while DrxMntnIdx < UPHY_DRX_MNTN_NUM:
                (uwSndSleepSlice,)              = struct.unpack('I', instream.read(4))
                strSndSleepSlice              = '%x'% uwSndSleepSlice

                strDrxMntnIdx                   = '%x'% DrxMntnIdx

                outstream.writelines(["%-s%-s%-90s%-s%-s\n" % ( "auwSndSleepSlice[",strDrxMntnIdx,"]: ","0x",strSndSleepSlice)])

                DrxMntnIdx                      = DrxMntnIdx + 1

        outstream.writelines(["\n********************************auwRcvWakeSlice[4]**********************\n"])
        DrxMntnIdx        = 0
        while DrxMntnIdx < UPHY_DRX_MNTN_NUM:
                (uwRcvWakeSlice,)               = struct.unpack('I', instream.read(4))
                strRcvWakeSlice                 = '%x'% uwRcvWakeSlice

                strDrxMntnIdx                   = '%x'% DrxMntnIdx

                outstream.writelines(["%-s%-s%-90s%-s%-s\n" % ( "auwRcvWakeSlice[",strDrxMntnIdx,"]: ","0x",strRcvWakeSlice)])

                DrxMntnIdx                      = DrxMntnIdx + 1

        outstream.writelines(["\n********************************auwSndWakeSlice[4]**********************\n"])
        DrxMntnIdx        = 0
        while DrxMntnIdx < UPHY_DRX_MNTN_NUM:
                (uwSndWakeSlice,)               = struct.unpack('I', instream.read(4))
                strSndWakeSlice                 = '%x'% uwSndWakeSlice

                strDrxMntnIdx                   = '%x'% DrxMntnIdx

                outstream.writelines(["%-s%-s%-90s%-s%-s\n" % ( "auwSndWakeSlice[",strDrxMntnIdx,"]: ","0x",strSndWakeSlice)])

                DrxMntnIdx                      = DrxMntnIdx + 1

        outstream.writelines(["\n********************************auwRcvWakeQb[4]**********************\n"])
        DrxMntnIdx        = 0
        while DrxMntnIdx < UPHY_DRX_MNTN_NUM:
                (uwRcvWakeQb,)                  = struct.unpack('I', instream.read(4))
                strRcvWakeQb                    = '%x'% uwRcvWakeQb

                strDrxMntnIdx                   = '%x'% DrxMntnIdx

                outstream.writelines(["%-s%-s%-90s%-s%-s\n" % ( "auwRcvWakeQb[",strDrxMntnIdx,"]: ","0x",strRcvWakeQb)])

                DrxMntnIdx                      = DrxMntnIdx + 1

        outstream.writelines(["\n********************************auwSndWakeQb[4]**********************\n"])
        DrxMntnIdx        = 0
        while DrxMntnIdx < UPHY_DRX_MNTN_NUM:
                (uwSndWakeQb,)                  = struct.unpack('I', instream.read(4))
                strSndWakeQb                    = '%x'% uwSndWakeQb

                strDrxMntnIdx                   = '%x'% DrxMntnIdx

                outstream.writelines(["%-s%-s%-90s%-s%-s\n" % ( "auwSndWakeQb[",strDrxMntnIdx,"]: ","0x",strSndWakeQb)])

                DrxMntnIdx                      = DrxMntnIdx + 1

        (uwGphyErrIndex,)                         = struct.unpack('I', instream.read(4))
        strGphyErrIndex                           =  '%x'% uwGphyErrIndex
        outstream.writelines(["%-112s0x%-50s\n" % ( "\nuwGphyErrIndex",strRegTxcoSwitch )])

        (uwGphyErrCnt,)                         = struct.unpack('I', instream.read(4))
        strGphyErrCnt                           =  '%x'% uwGphyErrCnt
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwGphyErrCnt",strGphyErrCnt )])

        outstream.writelines(["\n********************************auwGphyTimerErrSlice[10]**********************\n"])
        DrxMntnIdx        = 0
        while DrxMntnIdx < UPHY_DRX_MNTN_ERR_NUM:
                (uwGphyTimerErrSlice,)                  = struct.unpack('I', instream.read(4))
                strGphyTimerErrSlice                    = '%x'% uwGphyTimerErrSlice

                strDrxMntnIdx                   = '%x'% DrxMntnIdx

                outstream.writelines(["%-s%-s%-90s%-s%-s\n" % ( "auwGphyTimerErrSlice[",strDrxMntnIdx,"]: ","0x",strGphyTimerErrSlice)])

                DrxMntnIdx                      = DrxMntnIdx + 1


def analysis_guphy_modemX_Drx_Gphy_Slave_Info( instream, fileOffset, outstream ):

        (uwRcvSleepCnt,)                        = struct.unpack('I', instream.read(4))
        strRcvSleepCnt                          =  '%x'% uwRcvSleepCnt
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwRcvSleepCnt",strRcvSleepCnt )])

        outstream.writelines(["\n********************************auwRcvSleepSlice[4]**********************\n"])
        DrxMntnIdx        = 0
        while DrxMntnIdx < UPHY_DRX_MNTN_NUM:
                (uwRcvSleepSlice,)              = struct.unpack('I', instream.read(4))
                strRcvSleepSlice              = '%x'% uwRcvSleepSlice

                strDrxMntnIdx                   = '%x'% DrxMntnIdx

                outstream.writelines(["%-s%-s%-90s%-s%-s\n" % ( "auwRcvSleepSlice[",strDrxMntnIdx,"]: ","0x",strRcvSleepSlice)])

                DrxMntnIdx                      = DrxMntnIdx + 1

        outstream.writelines(["\n********************************auwSlpStatusErrSlice[4]**********************\n"])
        (uwSlpStatusErrCnt,)                    = struct.unpack('I', instream.read(4))
        strSlpStatusErrCnt                      =  '%x'% uwSlpStatusErrCnt
        outstream.writelines(["%-100s0x%-50s\n" % ( "uwSlpStatusErrCnt",uwSlpStatusErrCnt )])

        DrxMntnIdx        = 0
        while DrxMntnIdx < UPHY_DRX_MNTN_NUM:
                (uwSlpStatusErrSlice,)          = struct.unpack('I', instream.read(4))
                strSlpStatusErrSlice            = '%x'% uwSlpStatusErrSlice

                strDrxMntnIdx                   = '%x'% DrxMntnIdx

                outstream.writelines(["%-s%-s%-90s%-s%-s\n" % ( "auwSlpStatusErrSlice[",strDrxMntnIdx,"]: ","0x",strSlpStatusErrSlice)])

                DrxMntnIdx                      = DrxMntnIdx + 1

        outstream.writelines(["\n********************************auwCallBackSleepFailCnt[4]**********************\n"])
        (uwCallBackSleepFailCnt,)                    = struct.unpack('I', instream.read(4))
        strCallBackSleepFailCnt                      =  '%x'% uwCallBackSleepFailCnt
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwCallBackSleepFailCnt",uwCallBackSleepFailCnt )])

        DrxMntnIdx        = 0
        while DrxMntnIdx < UPHY_DRX_MNTN_NUM:
                (uwSlpStatusFailSlice,)          = struct.unpack('I', instream.read(4))
                strSlpStatusErrSlice            = '%x'% uwSlpStatusFailSlice

                strDrxMntnIdx                   = '%x'% DrxMntnIdx

                outstream.writelines(["%-s%-s%-90s%-s%-s\n" % ( "auwCallBackSleepFailCnt[",strDrxMntnIdx,"]: ","0x",strSlpStatusErrSlice)])

                DrxMntnIdx                      = DrxMntnIdx + 1

        outstream.writelines(["\n********************************auwSndSleepSlice[4]**********************\n"])
        (uwSndSleepCnt,)                      = struct.unpack('I', instream.read(4))
        strSndSleepCnt                        =  '%x'% uwSndSleepCnt
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwSndSleepCnt",strSndSleepCnt )])

        DrxMntnIdx        = 0
        while DrxMntnIdx < UPHY_DRX_MNTN_NUM:
                (uwSndSleepSlice,)              = struct.unpack('I', instream.read(4))
                strSndSleepSlice              = '%x'% uwSndSleepSlice

                strDrxMntnIdx                   = '%x'% DrxMntnIdx

                outstream.writelines(["%-s%-s%-90s%-s%-s\n" % ( "auwSndSleepSlice[",strDrxMntnIdx,"]: ","0x",strSndSleepSlice)])

                DrxMntnIdx                      = DrxMntnIdx + 1

        outstream.writelines(["\n********************************auwRcvWakeSlice[4]**********************\n"])
        (uwRcvWakeCnt,)                         = struct.unpack('I', instream.read(4))
        strRcvWakeCnt                           =  '%x'% uwRcvWakeCnt
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwRcvWakeCnt",strRcvWakeCnt )])

        DrxMntnIdx        = 0
        while DrxMntnIdx < UPHY_DRX_MNTN_NUM:
                (uwRcvWakeSlice,)               = struct.unpack('I', instream.read(4))
                strRcvWakeSlice                 = '%x'% uwRcvWakeSlice

                strDrxMntnIdx                   = '%x'% DrxMntnIdx

                outstream.writelines(["%-s%-s%-90s%-s%-s\n" % ( "auwRcvWakeSlice[",strDrxMntnIdx,"]: ","0x",strRcvWakeSlice)])

                DrxMntnIdx                      = DrxMntnIdx + 1

        outstream.writelines(["\n********************************auwWakeErrCnt[4]**********************\n"])
        (uwWakeLenErrCnt,)                      = struct.unpack('I', instream.read(4))
        strWakeLenErrCnt                        =  '%x'% uwWakeLenErrCnt
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwWakeErrCnt",strWakeLenErrCnt )])

        DrxMntnIdx        = 0
        while DrxMntnIdx < UPHY_DRX_MNTN_NUM:
                (uwWakeLenErrSlice,)            = struct.unpack('I', instream.read(4))
                strWakeLenErrSlice              = '%x'% uwWakeLenErrSlice

                strDrxMntnIdx                   = '%x'% DrxMntnIdx

                outstream.writelines(["%-s%-s%-90s%-s%-s\n" % ( "auwRcvWakeErrCnt[",strDrxMntnIdx,"]: ","0x",strWakeLenErrSlice)])

                DrxMntnIdx                      = DrxMntnIdx + 1

        outstream.writelines(["\n********************************auwSndWakeSlice[4]**********************\n"])
        (uwSndWakeCnt,)                         = struct.unpack('I', instream.read(4))
        strSndWakeCnt                           =  '%x'% uwSndWakeCnt
        outstream.writelines(["%-112s0x%-50s\n" % ( "uwSndWakeCnt",strSndWakeCnt )])

        DrxMntnIdx        = 0
        while DrxMntnIdx < UPHY_DRX_MNTN_NUM:
                (uwSndWakeSlice,)               = struct.unpack('I', instream.read(4))
                strSndWakeSlice                 = '%x'% uwSndWakeSlice

                strDrxMntnIdx                   = '%x'% DrxMntnIdx

                outstream.writelines(["%-s%-s%-90s%-s%-s\n" % ( "auwSndWakeSlice[",strDrxMntnIdx,"]: ","0x",strSndWakeSlice)])

                DrxMntnIdx                      = DrxMntnIdx + 1



def analysis_guphy_modem0_dump_gphy_info( instream, fileOffset, outstream ):
        outstream.writelines(["\n***************************************************************************************************************\n"])
        outstream.writelines(["\n*                                         UPHY_APM_SAVE_EXC_GPHY_INFO                                         *\n"])
        outstream.writelines(["\n***************************************************************************************************************\n"])
        outstream.writelines("\n")

        instream.seek(fileOffset)

        outstream.writelines(["\n************************UPHY_APM_MODULE_STATUS_INFO**********************\n"])
        analysis_guphy_modemX_Apm_Module_Status_Info( instream, fileOffset, outstream )

        outstream.writelines(["\n****************************UPHY_MNTN_PID_MSG_TRACE_BUF_INFO**********************\n"])
        outstream.writelines(["\n****************************stGphyMsgBuf**********************\n"])
        analysis_guphy_modemX_Mntn_Pid_Msg_Buf_Info( instream, fileOffset, outstream )

        outstream.writelines(["\n****************************UPHY_MNTN_PID_MSG_TRACE_BUF_INFO**********************\n"])
        outstream.writelines(["\n****************************stGphyIntMsgTrace**********************\n"])
        analysis_guphy_modemX_Mntn_Pid_Msg_Buf_Info( instream, fileOffset, outstream )

        #outstream.writelines(["\n****************************UPHY_DRX_GPHY_MASTER_MNTN_INFO**********************\n"])
        #analysis_guphy_modemX_Drx_Gphy_Master_Info( instream, fileOffset, outstream )

        #outstream.writelines(["\n****************************UPHY_DRX_GPHY_SLAVE_MNTN_INFO**********************\n"])
        #analysis_guphy_modemX_Drx_Gphy_Slave_Info( instream, fileOffset, outstream )

def analysis_guphy_modemX_event_state_list_dump_info( instream, fileOffset, outstream, type):
        #outstream.writelines(["\n**************************** analysis_guphy_modemX_event_state_list_dump_info enter! %d*******************************\n" % (fileOffset)])

        #outstream.writelines(["\n**************************** analysis_guphy_modemX_event_state_list_dump_info enter! %d*******************************\n" % (fileOffset)])
        
        ##### guphy modem0 #########
        if type == "Com_Info":
                try:
                        analysis_guphy_modem0_dump_comm_info(instream, fileOffset, outstream )
                except:
                        import traceback
                        outstream.writelines([traceback.format_exc()])

        elif type == "Wphy_Info":
                try:
                        analysis_guphy_modem0_dump_wphy_info(instream, fileOffset, outstream )
                except:
                        import traceback
                        outstream.writelines([traceback.format_exc()])

        elif type == "Gphy_Info":
                try:
                        analysis_guphy_modem0_dump_gphy_info(instream, fileOffset, outstream )
                except:
                        import traceback
                        outstream.writelines([traceback.format_exc()])

        return True

def analysis_guphy_dump_info( infile, offset, outfile):
        global  GLOBAL_UPHY_LOCK_CNT_NUM
        global  GLOBAL_UPHY_VOS_RATMODE_MAX_NUM

        phoenixEs = 19
        phoenixCs = 20
        orlando = 21
        b5000Es = 50
        b5000Cs = 51
        M536 = 52
        baltimore = 53
        denver = 54
        instream = infile
        outstream  = outfile
        fileOffset = eval(offset)
        
        #outstream.writelines(["\n**************************** WUMAI:GUPHY_DUMP_ANALYSIS_2016_01_22_VERSION_1.0 *******************************\n"])
        instream.seek(fileOffset)

        ##### guphy modem0 PARSE EVENT STATE #########   
        outstream.writelines(["\n****************************************** modem0:analysis_guphy_dump_info begin!*********************************************\n" ])
        (ulBeginTick,)       = struct.unpack('I', instream.read(4))
        strBeginTick         = '%x'% ulBeginTick

        outstream.writelines(["strModem0LogBeginFlg         0x%-15s\n" % ( strBeginTick )])

        fileOffset = fileOffset + 4
        
        VERSION = ulBeginTick & 0xfff
        CVERSION = (ulBeginTick & 0xf000)/0x1000
        if VERSION == b5000Es or VERSION == b5000Cs or VERSION == M536 or VERSION == baltimore:
            MACRO_COMM_INFO_LENGTH = 504 + 24 #24 is RcmExcInfo
            GLOBAL_UPHY_VOS_RATMODE_MAX_NUM = 7
            GLOBAL_UPHY_LOCK_CNT_NUM = 2
        elif VERSION == denver:
            MACRO_COMM_INFO_LENGTH = 504 + 24 - 32 #24 is RcmExcInfo
            GLOBAL_UPHY_VOS_RATMODE_MAX_NUM = 7
            GLOBAL_UPHY_LOCK_CNT_NUM = 1
        elif VERSION == orlando and CVERSION == 1: #orlandoC10fenzhi 
            MACRO_COMM_INFO_LENGTH = 500 
            GLOBAL_UPHY_VOS_RATMODE_MAX_NUM = 6
            GLOBAL_UPHY_LOCK_CNT_NUM = 1
        elif VERSION == orlando and CVERSION == 2: #orlandoC20fenzhi 
            MACRO_COMM_INFO_LENGTH = 444
            GLOBAL_UPHY_VOS_RATMODE_MAX_NUM = 6
            GLOBAL_UPHY_LOCK_CNT_NUM = 1
        elif VERSION == orlando and CVERSION == 3: #orlando_main
            MACRO_COMM_INFO_LENGTH = 460
            GLOBAL_UPHY_VOS_RATMODE_MAX_NUM = 6
            GLOBAL_UPHY_LOCK_CNT_NUM = 1
        elif (VERSION == phoenixCs or VERSION == phoenixEs) and CVERSION == 1: #phoenixC10fenzhi
            MACRO_COMM_INFO_LENGTH = 472
            GLOBAL_UPHY_VOS_RATMODE_MAX_NUM = 6
            GLOBAL_UPHY_LOCK_CNT_NUM = 2
        elif (VERSION == phoenixCs or VERSION == phoenixEs) and CVERSION == 2: #phoenixC20_main
            MACRO_COMM_INFO_LENGTH = 492
            GLOBAL_UPHY_VOS_RATMODE_MAX_NUM = 6
            GLOBAL_UPHY_LOCK_CNT_NUM = 2
        else: #之前的配置
            MACRO_COMM_INFO_LENGTH = 472
            GLOBAL_UPHY_VOS_RATMODE_MAX_NUM = 6
            GLOBAL_UPHY_LOCK_CNT_NUM = 2
                                    
        #outstream.writelines(["Com_Info1         %-15d\n" % ( fileOffset )])

        analysis_guphy_modemX_event_state_list_dump_info( instream, fileOffset, outstream, "Com_Info" )

        fileOffset = fileOffset + MACRO_COMM_INFO_LENGTH

        #outstream.writelines(["Wphy_Info1         %-15d\n" % ( fileOffset )])

        analysis_guphy_modemX_event_state_list_dump_info( instream, fileOffset, outstream, "Wphy_Info" )

        #outstream.writelines(["Wphy_Info2         %-15d\n" % ( fileOffset )])

        fileOffset = fileOffset + MACRO_WPHY_INFO_LENGTH

        #outstream.writelines(["Gphy_Info1         %-15d\n" % ( fileOffset )])

        analysis_guphy_modemX_event_state_list_dump_info( instream, fileOffset, outstream, "Gphy_Info" )

        #outstream.writelines(["Gphy_Info2         %-15d\n" % ( fileOffset )])

        fileOffset = fileOffset + MACRO_GPHY_INFO_LENGTH

        (ulEndTick,)       = struct.unpack('I', instream.read(4))
        strEndTick         = '%x'% ulEndTick

        fileOffset = fileOffset + 4
        outstream.writelines(["strModem0LogEndFlg         0x%-15s\n" % ( strEndTick )])

        outstream.writelines(["\n**************************** modem0:analysis_guphy_dump_info end!*******************************\n"])
        fileOffset = eval(offset) + MACRO_MODEM0_ADDR_LENGTH
        instream.seek(fileOffset)
        ##### guphy modem1 PARSE EVENT STATE #########                
        outstream.writelines(["\n**************************** modem1:analysis_guphy_dump_info begin!*******************************\n"])
        (ulBeginTick,)       = struct.unpack('I', instream.read(4))
        strBeginTick         = '%x'% ulBeginTick

        outstream.writelines(["strModem1LogBeginFlg         0x%-15s\n" % ( strBeginTick )])

        fileOffset = fileOffset + 4

        analysis_guphy_modemX_event_state_list_dump_info( instream, fileOffset, outstream, "Wphy_Info" )

        fileOffset = fileOffset + MACRO_WPHY_INFO_LENGTH

        analysis_guphy_modemX_event_state_list_dump_info( instream, fileOffset, outstream, "Gphy_Info" )

        fileOffset = fileOffset + MACRO_GPHY_INFO_LENGTH

        (ulEndTick,)       = struct.unpack('I', instream.read(4))
        strEndTick         = '%x'% ulEndTick

        outstream.writelines(["strModem1LogEndFlg         0x%-15s\n" % ( strEndTick )])
        fileOffset = fileOffset + 4

        outstream.writelines(["\n**************************** modem1:analysis_guphy_dump_info end!*******************************\n"])
        fileOffset = eval(offset) + MACRO_MODEM0_ADDR_LENGTH + MACRO_MODEM1_ADDR_LENGTH
        instream.seek(fileOffset)
        outstream.writelines(["\n**************************** modem2:analysis_guphy_dump_info begin!*******************************\n"])

        (ulBeginTick,)       = struct.unpack('I', instream.read(4))
        strBeginTick         = '%x'% ulBeginTick

        outstream.writelines(["strModem2LogBeginFlg         0x%-15s\n" % ( strBeginTick )])

        fileOffset = fileOffset + 4

        analysis_guphy_modemX_event_state_list_dump_info( instream, fileOffset, outstream, "Gphy_Info" )

        fileOffset = fileOffset + MACRO_MODEM1_ADDR_LENGTH - 4

        (ulEndTick,)       = struct.unpack('I', instream.read(4))
        strEndTick         = '%x'% ulEndTick

        outstream.writelines(["strModem2LogEndFlg         0x%-15s\n" % ( strEndTick )])

        fileOffset = fileOffset + 4
        outstream.writelines(["\n**************************** modem2:analysis_guphy_dump_info end!*******************************\n"])

        return True



########################################################################################
def entry_0x220000F(infile, field, offset, len, version, mode, outfile):
        ########check parameter start#############
        if not field == '0x220000F':
            print(('hidis field is ', field))
            outfile.writelines(["strModem1LogEndFlg         0x%-15s\n" % ( field )])
            print(('current field is', '0x220000F'))
            return error['ERR_CHECK_FIELD']
        elif not version == '0x0000':
            print(('hidis version is ', version))
            print(('current version is ', '0x0000'))
            outfile.writelines(["strModem1LogEndFlg         0x%-15s\n" % ( version )])
            return error['ERR_CHECK_VERSION']
        elif not len == '0x1770':
            print(('hids len is ', len))
            print(('current len is ', '0x1770'))
            outfile.writelines(["strModem1LogEndFlg         0x%-15s\n" % ( version )])
            return error['ERR_CHECK_LEN']
        #########check parameter end##############
        try:
                print("test")
                ret = analysis_guphy_dump_info( infile, offset, outfile)
        except:
                import traceback
                traceback.print_exc()
                #outfile.writelines([traceback.format_exc()])

        #c = msvcrt.getch()
        return 0


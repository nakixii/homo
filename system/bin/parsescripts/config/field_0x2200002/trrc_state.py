#!/usr/bin/env python3
# coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2016 - 2019 Hisilicon Technoligies Co., Ltd.
# * Filename      trrc_state.py
# * Description   tlps dump
# * Version       1.0
# * Data          2018-03-22 create file
#***********************************************************************
import string

trrc_flow_ctrl_flag_enum_table = {
    0  : "TRRC_FLOW_CTRL_TYPE_T2T_NORMAL",
    1  : "TRRC_FLOW_CTRL_TYPE_T2T_NORMAL_IDL_SYS_UPDATA",
    2  : "TRRC_FLOW_CTRL_TYPE_T2T_NORMAL_PCH_SYS_UPDATA",
    3  : "TRRC_FLOW_CTRL_TYPE_T2T_NORMAL_ENTER_PCH",
    4  : "TRRC_FLOW_CTRL_TYPE_T2T_NORMAL_ENTER_FCH",
    5  : "TRRC_FLOW_CTRL_TYPE_T2T_NORMAL_ENTER_DCH",
    6  : "TRRC_FLOW_CTRL_TYPE_T2T_RES_ENTER_FCH",
    7  : "TRRC_FLOW_CTRL_TYPE_T2T_NAS_SUSPEND",
    8  : "TRRC_FLOW_CTRL_TYPE_T2T_NORMAL_END",
    9  : "TRRC_FLOW_CTRL_TYPE_IRAT2T_START",
    10  : "TRRC_FLOW_CTRL_TYPE_G2T_START_RESEL",
    11  : "TRRC_FLOW_CTRL_TYPE_G2T_RESEL_FAIL",
    12  : "TRRC_FLOW_CTRL_TYPE_G2T_STOP_RESEL",
    13  : "TRRC_FLOW_CTRL_TYPE_L2T_START_RESEL",
    14  : "TRRC_FLOW_CTRL_TYPE_L2T_RESEL_FAIL",
    15  : "TRRC_FLOW_CTRL_TYPE_L2T_STOP_RESEL",
    16  : "TRRC_FLOW_CTRL_TYPE_G2T_START_CCO",
    17  : "TRRC_FLOW_CTRL_TYPE_G2T_CCO_FAIL",
    18  : "TRRC_FLOW_CTRL_TYPE_G2T_STOP_CCO",
    19  : "TRRC_FLOW_CTRL_TYPE_G2T_START_HO",
    20  : "TRRC_FLOW_CTRL_TYPE_G2T_HO_FAIL",
    21  : "TRRC_FLOW_CTRL_TYPE_G2T_STOP_HO",
    22  : "TRRC_FLOW_CTRL_TYPE_L2T_START_HO",
    23  : "TRRC_FLOW_CTRL_TYPE_L2T_HO_FAIL",
    24  : "TRRC_FLOW_CTRL_TYPE_L2T_STOP_HO",
    25  : "TRRC_FLOW_CTRL_TYPE_L2T_START_REDIR",
    26  : "TRRC_FLOW_CTRL_TYPE_L2T_REDIR_FAIL",
    27  : "TRRC_FLOW_CTRL_TYPE_L2T_STOP_REDIR",
    28  : "TRRC_FLOW_CTRL_TYPE_G2T_START_REDIR",
    29  : "TRRC_FLOW_CTRL_TYPE_G2T_REDIR_FAIL",
    30  : "TRRC_FLOW_CTRL_TYPE_G2T_STOP_REDIR",
    31  : "TRRC_FLOW_CTRL_TYPE_IRAT2T_END",
    32  : "TRRC_FLOW_CTRL_TYPE_T2IRAT_START",
    33  : "TRRC_FLOW_CTRL_TYPE_T2L_START",
    34  : "TRRC_FLOW_CTRL_TYPE_T2L_START_RESEL",
    35  : "TRRC_FLOW_CTRL_TYPE_T2L_RESEL_FAIL",
    36  : "TRRC_FLOW_CTRL_TYPE_T2L_START_HO",
    37  : "TRRC_FLOW_CTRL_TYPE_T2L_HO_FAIL",
    38  : "TRRC_FLOW_CTRL_TYPE_T2L_STOP_HO",
    39  : "TRRC_FLOW_CTRL_TYPE_T2L_REDIR",
    40  : "TRRC_FLOW_CTRL_TYPE_T2L_REDIR_FAIL",
    41  : "TRRC_FLOW_CTRL_TYPE_T2L_STOP_REDIR",
    42  : "TRRC_FLOW_CTRL_TYPE_T2L_END",
    43  : "TRRC_FLOW_CTRL_TYPE_T2G_START",
    44  : "TRRC_FLOW_CTRL_TYPE_T2G_START_RESEL",
    45  : "TRRC_FLOW_CTRL_TYPE_T2G_RESEL_FAIL",
    46  : "TRRC_FLOW_CTRL_TYPE_T2G_START_CCO",
    47  : "TRRC_FLOW_CTRL_TYPE_T2G_CCO_FAIL",
    48  : "TRRC_FLOW_CTRL_TYPE_T2G_START_HO",
    49  : "TRRC_FLOW_CTRL_TYPE_T2G_HO_FAIL",
    50  : "TRRC_FLOW_CTRL_TYPE_T2G_STOP_HO",
    51  : "TRRC_FLOW_CTRL_TYPE_T2G_REDIR",
    52  : "TRRC_FLOW_CTRL_TYPE_T2G_END",
    53  : "TRRC_FLOW_CTRL_TYPE_T2IRAT_END",
    54  : "TRRC_FLOW_CTRL_TYPE_G2T_MEAS",
    55  : "TRRC_FLOW_CTRL_TYPE_L2T_IDLE_MEAS",
    56  : "TRRC_FLOW_CTRL_TYPE_L2T_CONN_MEAS",
    57  : "TRRC_FLOW_CTRL_TYPE_L2T_RELALL",
    58  : "TRRC_FLOW_CTRL_TYPE_T2T_SYSCFG_SUSPEND",
    59  : "TRRC_FLOW_CTRL_TYPE_T2T_POWEROFF",
    60  : "TRRC_FLOW_CTRL_TYPE_T2T_CELL_SEARCH",
    61  : "TRRC_FLOW_CTRL_TYPE_T2T_OOC_STATUS_NOTIFY",
    62  : "TRRC_FLOW_CTRL_TYPE_NCELL_SPEC_VALID",
    63  : "TRRC_FLOW_CTRL_TYPE_PRIO_SPEC_VALID",
    64  : "TRRC_FLOW_CTRL_TYPE_PREF_BAND_VALID",
    65  : "TRRC_FLOW_CTRL_TYPE_T2T_STOP_PLMN_SEARCH",
    66  : "TRRC_FLOW_CTRL_TYPE_T2T_POWEROFF_INTER_RAT",
    67  : "TRRC_FLOW_CTRL_TYPE_BUTT",
}

trrc_substate_enum_table = {
    0  : "TRRC_STATE_NULL",
    1  : "TRRC_STATE_Sent_GunasSuspendInd_T2G_RESEL",
    2  : "TRRC_STATE_Sent_s_rrc_RR_L1_RSRC_REQ",
    3  : "TRRC_STATE_Sent_TmacBsicVerifyReq",
    4  : "TRRC_STATE_Sent_GunasSuspendInd_T2G_CCO",
    5  : "TRRC_STATE_Sent_GunasSuspendInd_T2G_HO",
    6  : "TRRC_STATE_Sent_GunasSuspendInd_T2G_HO_T2G_HO_R3",
    7  : "TRRC_STATE_Sent_OP_CMAC_INTER_RAT_REQ",
    8  : "TRRC_STATE_Sent_OP_RR_SET_INACTIVE_REQ",
    9  : "TRRC_STATE_Sent_SndTmacBsicVerifyReq_DCH",
    10  : "TRRC_STATE_Sent_GunasSuspendInd_T2G_RESEL_2",
    11  : "TRRC_STATE_Sent_GunasSuspendInd_T2L_RESEL",
    12  : "TRRC_STATE_Sent_CMAC_IDL_MEAS_REQ",
    13  : "TRRC_STATE_Sent_CMAC_FCH_CONFIG_REQ",
    14  : "TRRC_STATE_Sent_CMAC_DCH_MEAS_REQ",
    15  : "TRRC_STATE_Sent_CMAC_IDL_MEAS_REQ_2",
    16  : "TRRC_STATE_Sent_CMAC_DCH_MEAS_REQ_2",
    17  : "TRRC_STATE_Sent_CMAC_IDL_MEAS_REQ_3",
    18  : "TRRC_STATE_Sent_CMAC_DCH_MEAS_REQ_3",
    19  : "TRRC_STATE_Sent_GunasSuspendInd_T2L_HANDOVER",
    20  : "TRRC_STATE_Sent_GunasSuspendInd_T2L_REDIR",
    21  : "TRRC_STATE_Sent_GunasSuspendInd_T2L_REDIR_2",
    22  : "TRRC_STATE_Sent_RR_CELL_CHANGE_REQ_1",
    23  : "TRRC_STATE_Sent_T_IR_RR_RESEL_REQ_1",
    24  : "TRRC_STATE_Sent_T_IR_RR_RESEL_REQ_2",
    25  : "TRRC_STATE_Sent_RR_CELL_CHANGE_REQ_2",
    26  : "TRRC_STATE_Sent_SndGrrBsicVerifyReq",
    27  : "TRRC_STATE_Sent_SndGrrBsicVerifyReq_2",
    28  : "TRRC_STATE_Sent_ID_TRRC_GRR_CELL_RESEL_REQ",
    29  : "TRRC_STATE_Sent_ID_TRRC_GRR_GETUECAPINFO_REQ",
    30  : "TRRC_STATE_Sent_ID_TRRC_LRRC_GETUECAPINFO_REQ",
    31  : "TRRC_STATE_Sent_ID_TRRC_LRRC_CELL_RESEL_REQ",
    32  : "TRRC_STATE_Sent_SndLrrcRelAllReq",
    33  : "TRRC_STATE_Sent_SndGrrRelAllReq",
    34  : "TRRC_STATE_Sent_ID_TRRC_GRR_CELL_CHANGE_ORDER_REQ",
    35  : "TRRC_STATE_Sent_SndLrrcRedirReq",
    36  : "TRRC_STATE_Sent_SndLrrcConnMeasReq_1",
    37  : "TRRC_STATE_Sent_SndLrrcIdleMeasReq",
    38  : "TRRC_STATE_Sent_SndLrrcConnMeasReq_2",
    39  : "TRRC_STATE_Sent_ID_TRRC_GRR_MEASURE_REQ",
    40  : "TRRC_STATE_Sent_SndGrrBsicVerifyReq_3",
    41  : "TRRC_STATE_Sent_SndGrrBsicVerifyReq_4",
    42  : "TRRC_STATE_Sent_ID_TRRC_LRRC_HANDOVER_REQ",
    43  : "TRRC_STATE_Sent_ID_TRRC_GRR_HANDOVER_REQ",
    44  : "TRRC_STATE_TRRC_IRAT_ProcRejRedirFail",
    45  : "TRRC_STATE_BUTT",
}
Trrc_state_enum_table = {
    0  : "RRC_NUL",
    1  : "RRC_SEL",
    2  : "RRC_IDL",
    3  : "RRC_RES",
    4  : "RRC_ACC",
    5  : "RRC_FCH",
    6  : "RRC_DCH",
    7  : "RRC_PCH",
    8  : "RRC_WCA",
    9  : "RRC_REL",
    10  : "RRC_CNF",
    11  : "RRC_LIM",
    12  : "RRC_SNW",
    13  : "RRC_INACTIVE",
    14  : "RRC_PREDEF",
    15  : "RRC_PEND",
    16  : "RRC_RATHO",
    17  : "RRC_WAIT",
    18  : "RRC_POWEROFF",
}

Trrc_utran_mode_enum_table = {
    0 : "TRRC_CCB_UTRAN_MODE_WCDMA",
    1 : "TRRC_CCB_UTRAN_MODE_TDSCDMA",
    2 : "TRRC_CCB_UTRAN_MODE_BUTT",
}

def Trrc_Get_Flow_Ctrl_Flag_Str(state):
    for index in trrc_flow_ctrl_flag_enum_table.keys():
        if index == state:
            return trrc_flow_ctrl_flag_enum_table[index]

    return "unknown"

def Trrc_Get_Sub_State_Str(state):
    for index in trrc_substate_enum_table.keys():
        if index == state:
            return trrc_substate_enum_table[index]

    return "unknown"

def Trrc_Get_Tds_State_Str(state):
    for index in Trrc_state_enum_table.keys():
        if index == state:
            return Trrc_state_enum_table[index]

    return "unknown"

def Trrc_Get_Utran_Mode_Str(state):
    for index in Trrc_utran_mode_enum_table.keys():
        if index == state:
            return Trrc_utran_mode_enum_table[index]

    return "unknown"

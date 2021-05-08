#!/usr/bin/env python3
# coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2016 - 2019 Hisilicon Technoligies Co., Ltd.
# * Filename      lnas_state.py
# * Description   tlps dump
# * Version       1.0
# * Data          2018-03-22 create file
#***********************************************************************
import string

Lnas_fsm_id_enum_table = {

    2 : "FSM_ID_BUTT",
}

lnas_fsm_main_state_enum_table = {

    20 : "NAS_LMM_MAIN_STATE_BUTT",
}

lnas_fsm_substate_enum_table = {

    45  : "MM_SS_BUTT",
}

lnas_state_timer_enum_table = {
    0  : "TI_NAS_EMM_STATE_NO_TIMER",
    1  : "TI_NAS_EMM_STATE_T3440",
    2  : "TI_NAS_EMM_STATE_DEL_FORB_TA_PROID",
    3  : "TI_NAS_LMM_TIMER_WAIT_USIM_CNF",
    4  : "TI_NAS_LMM_TIMER_WAIT_USIM_READY_START",
    5  : "TI_NAS_EMM_STATE_MRRC_BOUNDARY_START",
    6  : "TI_NAS_EMM_MRRC_WAIT_RRC_CONN_CNF",
    7  : "TI_NAS_EMM_MRRC_WAIT_RRC_REL_CNF",
    8  : "TI_NAS_EMM_STATE_REG_BOUNDARY_START",
    9  : "TI_NAS_EMM_T3410",
    10  : "TI_NAS_EMM_WAIT_ESM_PDN_RSP",
    11  : "TI_NAS_EMM_WAIT_ESM_BEARER_CNF",
    12  : "TI_NAS_EMM_WAIT_RRC_DATA_CNF",
    13  : "TI_NAS_EMM_STATE_DEREG_BOUNDARY_START",
    14  : "TI_NAS_EMM_T3421",
    15  : "TI_NAS_EMM_STATE_TAU_BOUNDARY_START",
    16  : "TI_NAS_EMM_STATE_TAU_T3430",
    17  : "TI_NAS_EMM_STATE_SERVICE_BOUNDARY_START",
    18  : "TI_NAS_EMM_STATE_SERVICE_T3417",
    19  : "TI_NAS_EMM_STATE_SERVICE_T3417_EXT",
    20  : "TI_NAS_EMM_STATE_SERVICE_T3442",
    21  : "TI_NAS_EMM_STATE_PLMN_BOUNDARY_START",
    22  : "TI_NAS_EMM_WAIT_MMC_START_CNF_TIMER",
    23  : "TI_NAS_EMM_WAIT_RRC_START_CNF_TIMER",
    24  : "TI_NAS_EMM_WAIT_MMC_STOP_CNF_TIMER",
    25  : "TI_NAS_EMM_WAIT_RRC_STOP_CNF_TIMER",
    26  : "TI_NAS_EMM_STATE_AUTH_BOUNDARY_START",
    27  : "TI_NAS_EMM_T3418",
    28  : "TI_NAS_EMM_T3420",
    29  : "TI_NAS_EMM_RRCORI_WAIT_OTHER_SUSPEND_RSP_TIMER",
    30  : "TI_NAS_EMM_WAIT_SUSPEND_END_TIMER",
    31  : "TI_NAS_EMM_MMCORI_WAIT_OTHER_SUSPEND_RSP_TIMER",
    32  : "TI_NAS_EMM_SYSCFGORI_WAIT_OTHER_SUSPEND_RSP_TIMER",
    33  : "TI_NAS_EMM_RRCRSM_WAIT_OTHER_RESUME_RSP_TIMER",
    34  : "TI_NAS_EMM_WAIT_SYS_INFO_IND_TIMER",
    35  : "TI_NAS_EMM_SYSCFGRSM_WAIT_OTHER_RESUME_RSP_TIMER",
    36  : "TI_NAS_EMM_STATE_WAIT_SYSCFG_CNF_TIMER",
    37  : "TI_NAS_EMM_STATE_TI_BUTT",
    38  : "TI_NAS_EMMC_STATE_WAIT_PLMN_SRCH_CNF_TIMER",
    39  : "TI_NAS_EMMC_STATE_TI_BUTT",
    40  : "NAS_LMM_STATE_TI_BUTT",
}

Lnas_conn_state_enum_table = {
    0 : "NAS_EMM_CONN_IDLE",
    1 : "NAS_EMM_CONN_ESTING",
    2 : "NAS_EMM_CONN_SIG",
    3 : "NAS_EMM_CONN_DATA",
    4 : "NAS_EMM_CONN_RELEASING",
    5 : "NAS_EMM_CONN_WAIT_SYS_INFO",
    6 : "NAS_EMM_CONN_BUTT",
}

Lnas_lte_state_enum_table = {
    0 : "NAS_LMM_CUR_LTE_SUSPEND",
    1 : "NAS_LMM_CUR_LTE_ACTIVE",
    2 : "NAS_LMM_CUR_LTE_BUTT",
}
def Tlps_Get_Lnas_FsmId_Str(fsmid):
    for fsmid_index in Lnas_fsm_id_enum_table.keys():
        if fsmid_index == fsmid:
            return Lnas_fsm_id_enum_table[fsmid_index]

    return "unknown"

def Tlps_Get_Lnas_MainState_Str(state):
    for index in lnas_fsm_main_state_enum_table.keys():
        if index == state:
            return lnas_fsm_main_state_enum_table[index]

    return "unknown"

def Tlps_Get_Lnas_SubState_Str(state):
    for index in lnas_fsm_substate_enum_table.keys():
        if index == state:
            return lnas_fsm_substate_enum_table[index]

    return "unknown"

def Tlps_Get_Lnas_StaTiId_Str(timerid):
    for index in lnas_state_timer_enum_table.keys():
        if index == timerid:
            return lnas_state_timer_enum_table[index]

    return "unknown"

def Tlps_Get_Lnas_RrcConnState_Str(state):
    for index in Lnas_conn_state_enum_table.keys():
        if index == state:
            return Lnas_conn_state_enum_table[index]

    return "unknown"

def Tlps_Get_Lnas_LteState_Str(state):
    for index in Lnas_lte_state_enum_table.keys():
        if index == state:
            return Lnas_lte_state_enum_table[index]

    return "unknown"

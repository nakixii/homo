#!/usr/bin/env python3
# coding=utf-8
"""

功能；复位log分析脚本
版权信息：华为技术有限公司，版权所有(C) 2010-2019
修改记录：
        2019-11-08 尹鹏 创建内容
        2019-11-08 尹鹏 修改注释
"""
import string

#max num of parallel fsm is 6
NRRC_PARALLEL_FSM_BUTT = 6

LTE_NR_PROTOCOL_VER_ENUM_TABLE = {
    0x01: "LTE_NR_PROTOCOL_VER_V8",
    0x02: "LTE_NR_PROTOCOL_VER_V9",
    0x04: "LTE_NR_PROTOCOL_VER_V10",
    0x08: "LTE_NR_PROTOCOL_VER_V11",
    0x10: "LTE_NR_PROTOCOL_VER_V12",
    0x20: "LTE_NR_PROTOCOL_VER_V13",
    0x40: "LTE_NR_PROTOCOL_VER_V14",
    0x80: "LTE_NR_PROTOCOL_VER_V15",
}

NRRC_CCB_NET_DEPLOY_TYPE_ENUM = {
    0: "NRRC_CCB_NET_DEPLOY_TYPE_NONE",
    1: "NRRC_CCB_NET_DEPLOY_TYPE_SA",
    2: "NRRC_CCB_NET_DEPLOY_TYPE_ENDC",
    3: "NRRC_CCB_NET_DEPLOY_TYPE_NEDC",
}

NRRC_PTL_STATE_ENUM = {
    0: "NRRC_PTL_STATE_NULL",
    1: "NRRC_PTL_STATE_IDLE",
    2: "NRRC_PTL_STATE_CONN",
    3: "NRRC_PTL_STATE_INACTIVE",
}

NRRC_UE_STATE_ENUM = {
    0: "NRRC_UE_STATE_NULL",
    1: "NRRC_UE_STATE_DEACTIVE",
    2: "NRRC_UE_STATE_ACTIVE",
}

NRRC_MASTER_CTRL_FSM_ENUM = {
    0: "NRRC_MASTER_CTRL_FSM_IDLECTRL",
    1: "NRRC_MASTER_CTRL_FSM_CONNCTRL",
}

NRRC_UTRAN_MODE_ENUM = {
    0: "NRRC_UTRAN_MODE_WCDMA",
    1: "NRRC_UTRAN_MODE_TDSCDMA",
    2: "NRRC_UTRAN_MODE_NULL",
}

NRRC_UE_CAMPED_STATE_ENUM = {
    0: "NRRC_UE_CAMPED_STATE_NORMALLY",
    1: "NRRC_UE_CAMPED_STATE_ANY_CELL",
}

NRRC_POWER_STATUS_ENUM = {
    0: "NRRC_POWER_STATUS_NONE",
    1: "NRRC_POWER_STATUS_ON",
    2: "NRRC_POWER_STATUS_OFF",
}

NRRC_PARALLEL_FSM_ENUM = {
    0: "NRRC_PARALLEL_FSM_IDLECTRL",
    1: "NRRC_PARALLEL_FSM_CONNCTRL",
    2: "NRRC_PARALLEL_FSM_MEAS",
    3: "NRRC_PARALLEL_FSM_CSRCH",
    4: "NRRC_PARALLEL_FSM_SIB",
    5: "NRRC_PARALLEL_FSM_BGSCTRL",
    6: "NRRC_PARALLEL_FSM_ITFCM",
}


def get_nrrc_parallel_fsm_str(parallelfsm):
    for fsmid_index in NRRC_PARALLEL_FSM_ENUM.keys():
        if fsmid_index == parallelfsm:
            return NRRC_PARALLEL_FSM_ENUM[fsmid_index]

    return "LTE_NR_PROTOCOL_VER_BUTT"


def get_lte_nr_protocol_ver_str(protocolver):
    for fsmid_index in LTE_NR_PROTOCOL_VER_ENUM_TABLE.keys():
        if fsmid_index == protocolver:
            return LTE_NR_PROTOCOL_VER_ENUM_TABLE[fsmid_index]

    return "LTE_NR_PROTOCOL_VER_BUTT"


def get_nrrc_deploy_type_str(netdeploytype):
    for fsmid_index in NRRC_CCB_NET_DEPLOY_TYPE_ENUM.keys():
        if fsmid_index == netdeploytype:
            return NRRC_CCB_NET_DEPLOY_TYPE_ENUM[fsmid_index]

    return "NRRC_CCB_NET_DEPLOY_TYPE_BUTT"


def get_nrrc_ptl_state_str(ptlstate):
    for fsmid_index in NRRC_PTL_STATE_ENUM.keys():
        if fsmid_index == ptlstate:
            return NRRC_PTL_STATE_ENUM[fsmid_index]

    return "NRRC_PTL_STATE_BUTT"


def get_nrrc_ue_state_str(uestate):
    for fsmid_index in NRRC_UE_STATE_ENUM.keys():
        if fsmid_index == uestate:
            return NRRC_UE_STATE_ENUM[fsmid_index]

    return "NRRC_UE_STATE_BUTT"


def get_nrrc_master_ctrl_fsm_str(masterctrlfsm):
    for fsmid_index in NRRC_MASTER_CTRL_FSM_ENUM.keys():
        if fsmid_index == masterctrlfsm:
            return NRRC_MASTER_CTRL_FSM_ENUM[fsmid_index]

    return "NRRC_MASTER_CTRL_FSM_BUTT"


def get_nrrc_utran_mode_str(utranmode):
    for fsmid_index in NRRC_UTRAN_MODE_ENUM.keys():
        if fsmid_index == utranmode:
            return NRRC_UTRAN_MODE_ENUM[fsmid_index]

    return "NRRC_UTRAN_MODE_BUTT"


def get_nrrc_ue_camped_state_str(campstate):
    for fsmid_index in NRRC_UE_CAMPED_STATE_ENUM.keys():
        if fsmid_index == campstate:
            return NRRC_UE_CAMPED_STATE_ENUM[fsmid_index]

    return "NRRC_UE_CAMPED_STATE_ENUM_BUTT"


def get_nrrc_power_status_str(powerstate):
    for fsmid_index in NRRC_POWER_STATUS_ENUM.keys():
        if fsmid_index == powerstate:
            return NRRC_POWER_STATUS_ENUM[fsmid_index]

    return "NRRC_POWER_STATUS_ENUM_BUTT"

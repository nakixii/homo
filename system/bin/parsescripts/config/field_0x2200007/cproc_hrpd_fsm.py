#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list cproc hrpd fsm name
modify  record  :   2016-03-22 create file
"""

cproc_hrpd_fsm_enum_table = {
    0x0001 :     "CPROC_HRPD_CM_DRX_FSM",
    0x0002 :     "CPROC_HRPD_CM_PAGING_FSM",
    0x0003 :     "CPROC_HRPD_CM_TCH_FSM",
    0x0004 :     "CPROC_HRPD_CM_PILOT_SEARCH_FSM",
    0x0005 :     "CPROC_HRPD_SM_RESET_FSM",
    0x0006 :     "CPROC_HRPD_CM_RESET_FSM",
    0x0008 :     "CPROC_HRPD_CM_SLS_FSM",
    0x0009 :     "CPROC_HRPD_CM_POWER_ON_FSM",
    0x000A :     "CPROC_HRPD_SM_MPS_FSM",
    0x000B :     "CPROC_HRPD_CM_SUSPEND_FSM",
    0x000C :     "CPROC_HRPD_CM_AC_CH_FSM",
    0x000D :     "CPROC_HRPD_CM_TCH_HO_FSM",
    0x000E :     "CPROC_HRPD_CM_CC_CH_FSM",
    0x000F :     "CPROC_HRPD_CM_CC_FSM",
    0x0010 :     "CPROC_HRPD_CM_SET_MODE_FSM",
    0x0011 :     "CPROC_HRPD_CM_FSM",
    0x0012 :     "CPROC_HRPD_CM_AC_FSM",
    0x0013 :     "CPROC_RM_FSM",
    0x0014 :     "CPROC_RM_RAT_TOP_FSM",
    0x0015 :     "CPROC_RM_WAIT_PAGING_FSM",
    0x0016 :     "CPROC_RM_ASSIGNMENT_FSM",
    0x0017 :     "CPROC_HRPD_CM_DRX_IRAT_FSM",
    0x001A :     "CPROC_HRPD_SM_SLAVEMEASUREMENT_FSM",
    0x001B :     "CPROC_HRPD_CM_SLAVE_FSM",
    0x001E :     "CPROC_HRPD_CM_SVLTE_IRAT_FSM",
    0x0020 :     "CPROC_HRPD_SM_PS_FSM",
    0x0021 :     "CPROC_HRPD_SM_MEASUREMENT_FSM",
    0x0023 :     "CPROC_HRPD_CM_AGPS_FSM",
    0x0024 :     "CPROC_HRPD_CM_SYNC_TIME_CH_FSM",
    0x0025 :     "CTAS_FSM",
    0x0026 :     "CTAS_ACCESS_ON_FSM",
    0x0027 :     "CTAS_SLS_FSM",
    0x0028 :     "CTAS_TCH_ON_FSM",
    0x002A :     "CPROC_HRPD_CM_SYNC_TIME_FSM",
    0x003A :     "CPROC_HRPD_CM_LPHY_WAKEUP_FSM",
    0x0050 :     "CTAS_PROXY_FSM",
    0x0056 :     "CTAS_PS_FSM",
    0x0065 :     "CPROC_HRPD_SM_MEASMODE_FSM",
    0x0068 :     "CPROC_HRPD_CM_LTE_IRAT_FSM",
}

cproc_hrpd_cm_lphy_wakeup_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAKEUP_CNF_SUSP",
    0x0002 :     "WAIT_WAKEUP_CNF",
    0x0003 :     "RELEASING_SUSP",
    0x0004 :     "RELEASING",
    0x0005 :     "WAIT_WAKEUP_IND_SUSP",
    0x0006 :     "WAIT_WAKEUP_IND",
    0x0007 :     "TERMINATE",
    0x0008 :     "BUTT",
}

cproc_hrpd_cm_sync_time_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_RESOURCE",
    0x0002 :     "ALLOCATED",
    0x0003 :     "SUSPENDING",
    0x0004 :     "ENDING",
    0x0005 :     "RELEASING",
    0x0006 :     "TERMINATE",
    0x0007 :     "BUTT",
}

cproc_hrpd_cm_sync_time_ch_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "START_MPS",
    0x0002 :     "MPS",
    0x0003 :     "STOP",
    0x0004 :     "WAIT_CNF",
    0x0005 :     "RELEASE",
    0x0006 :     "TERMINATE",
    0x0007 :     "BUTT",
}

cproc_hrpd_cm_agps_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "NO_SYNC",
    0x0002 :     "WAIT_RESULT",
    0x0003 :     "TERMINATE",
    0x0004 :     "BUTT",
}

cproc_hrpd_sm_measurement_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "GAP_STOPPING",
    0x0002 :     "DRX_STOPPING",
    0x0003 :     "CC_MEAS_NOT_CFG",
    0x0004 :     "CONFIGURED",
    0x0005 :     "MEAS_NSF",
    0x0006 :     "MEAS_SF",
    0x0007 :     "MASTER_IDLE",
    0x0008 :     "STOPPING",
    0x0009 :     "TCH_MEAS_NOT_CFG",
    0x000A :     "DRX_MEAS_NOT_CFG",
    0x000B :     "DRX",
    0x000C :     "TERMINATE",
    0x000D :     "BUTT",
}

cproc_hrpd_sm_ps_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "SELECT_PN",
    0x0002 :     "SEARCHING",
    0x0003 :     "STOPPING",
    0x0004 :     "TERMINATE",
    0x0005 :     "BUTT",
}

cproc_hrpd_cm_svlte_irat_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_WAKEUP",
    0x0002 :     "SUSPENDED",
    0x0003 :     "WAIT_RESOURCE",
    0x0004 :     "LTE_MEAS_BSR",
    0x0005 :     "WAIT_MEAS",
    0x0006 :     "RESTART_MEAS",
    0x0007 :     "TERMINATE",
    0x0008 :     "BUTT",
}

cproc_hrpd_sm_measmode_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "SLAVE",
    0x0002 :     "MASTER",
    0x0003 :     "BUTT",
}

cproc_hrpd_cm_slave_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "CFG",
    0x0002 :     "MEAS_PS",
    0x0003 :     "MEAS_CC",
    0x0004 :     "MEAS_WAIT_GAP_IND",
    0x0005 :     "MEAS",
    0x0006 :     "MEAS_CFG",
    0x0007 :     "MEAS_NEW_GAP",
    0x0008 :     "PILOT_SEARCH",
    0x0009 :     "CC_MONITOR",
    0x000A :     "CFG_STOPPING",
    0x000B :     "TERMINATE",
    0x000C :     "BUTT",
}

cproc_hrpd_sm_slavemeasurement_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "GET_TIMING",
    0x0002 :     "WAIT_GAP_CFG",
    0x0003 :     "SEARCH_TIMING",
    0x0004 :     "MEAS_CFG",
    0x0005 :     "MEAS_GAP",
    0x0006 :     "RECFG",
    0x0007 :     "RECFG_GAP",
    0x0008 :     "STOPPING",
    0x0009 :     "TERMINATE",
    0x000A :     "BUTT",
}

cproc_hrpd_cm_drx_irat_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_LTE_MEAS",
    0x0002 :     "LTE_MEAS",
    0x0003 :     "WAIT_INT2",
    0x0004 :     "WAIT_LTE_BSR",
    0x0005 :     "LTE_BSR",
    0x0006 :     "DONE_WAIT_INT2",
    0x0007 :     "TERMINATE",
    0x0008 :     "BUTT",
}

cproc_hrpd_rm_assignment_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "SUSPENDING",
    0x0002 :     "RM_SUSPEND_PREEMPTED",
    0x0003 :     "RM_SUSPEND",
    0x0004 :     "SUSPENDED",
    0x0005 :     "WAIT_ASSIGN",
    0x0006 :     "ASSIGNED",
    0x0007 :     "ASSIGN_NEW",
    0x0008 :     "PENDING_RESUME",
    0x0009 :     "TERMINATE",
    0x000A :     "BUTT",
}

cproc_hrpd_rm_wait_paging_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_ASSIGN",
    0x0002 :     "WAIT_PAGING_APPLY",
    0x0003 :     "TERMINATE",
    0x0004 :     "BUTT",
}

cproc_hrpd_rm_rat_top_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_REL_CNF",
    0x0002 :     "WAIT_RELEASE_ALL",
    0x0003 :     "INIT",
    0x0004 :     "IDLE",
    0x0005 :     "WAIT_PAGING_ASSIGN",
    0x0006 :     "ASSIGNED",
    0x0007 :     "BUTT",
}

cproc_hrpd_rm_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "IDLE",
    0x0002 :     "ASSIGNED_1X",
    0x0003 :     "ASSIGNED_HRPD",
    0x0004 :     "BUTT",
}

cproc_hrpd_cm_ac_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "ACCESS",
    0x0002 :     "AC_STOPPING",
    0x0003 :     "AC_SUSPENDING",
    0x0004 :     "TERMINATE",
    0x0005 :     "BUTT",
}

cproc_hrpd_cm_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "POWER_ON",
    0x0002 :     "SET_MODE",
    0x0003 :     "MASTER_FREE",
    0x0004 :     "SIGNAL_LEVEL_SCAN",
    0x0005 :     "PILOT_SEARCH",
    0x0006 :     "CC_MONITOR",
    0x0007 :     "ACCESS",
    0x0008 :     "CONNECTED",
    0x0009 :     "IDLE_DRX",
    0x000A :     "SLAVE_FREE",
    0x000B :     "BUTT",
}

cproc_hrpd_cm_set_mode_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "SLAVE_KEEP_TIMING",
    0x0002 :     "SLAVE_KEEP_TIMING_WAIT_CONF",
    0x0003 :     "WAITING_CONFIRM",
    0x0004 :     "SLAVE_WAITING_CONFIRM",
    0x0005 :     "TERMINATE",
    0x0006 :     "BUTT",
}

cproc_hrpd_cm_cc_ch_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "START_QUICK_MPS_NO_TIME",
    0x0002 :     "START_MPS_NO_TIME",
    0x0003 :     "START_CC_NO_TIME",
    0x0004 :     "CC_NO_TIME",
    0x0005 :     "STOP_SET_TIME",
    0x0006 :     "SET_TIME",
    0x0007 :     "START_QUICK_MPS",
    0x0008 :     "START_MPS",
    0x0009 :     "START_CC",
    0x000A :     "CC",
    0x000B :     "HANDOFF",
    0x000C :     "REL_WAIT_MPS_CNF_NO_TIME",
    0x000D :     "REL_WAIT_CC_CNF_NO_TIME",
    0x000E :     "REL_STOPPING_NO_TIME",
    0x000F :     "REL_STOP_SET_TIME",
    0x0010 :     "REL_SET_TIME",
    0x0011 :     "REL_WAIT_MPS_CNF",
    0x0012 :     "REL_WAIT_CC_CNF",
    0x0013 :     "REL_STOPPING",
    0x0014 :     "DRX_STOPPING",
    0x0015 :     "RESET_MPS_SET_TIME",
    0x0016 :     "TERMINATE",
    0x0017 :     "BUTT",
}

cproc_hrpd_cm_cc_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "CC_MONITOR",
    0x0002 :     "CC_NO_ALLOC_NO_TIME",
    0x0003 :     "CC_NO_ALLOC",
    0x0004 :     "CC_SUSPENDING",
    0x0005 :     "NO_ALLOC_SET_TIME",
    0x0006 :     "ALLOC_SET_TIME",
    0x0007 :     "CC_STOPPING",
    0x0008 :     "TERMINATE",
    0x0009 :     "BUTT",
}

cproc_hrpd_cm_tch_ho_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "STOPPING",
    0x0002 :     "WAIT_RXON",
    0x0003 :     "RESUMING_MPS",
    0x0004 :     "RESUMING",
    0x0005 :     "SUSPENDED_STOP",
    0x0006 :     "TERMINATE",
    0x0007 :     "BUTT",
}

cproc_hrpd_cm_ac_ch_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "SUSPENDING",
    0x0002 :     "SUSP_WAIT_CNF",
    0x0003 :     "STOP_WAIT_CNF",
    0x0004 :     "WAIT_START_CNF",
    0x0005 :     "WAIT_START_IND",
    0x0006 :     "TRANSMITTING",
    0x0007 :     "STOPPING",
    0x0008 :     "REL_WAIT_CNF",
    0x0009 :     "REL_STOPPING",
    0x000A :     "TERMINATE",
    0x000B :     "BUTT",
}

cproc_hrpd_cm_suspend_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_TO_RESUME_STOPPING",
    0x0002 :     "WAIT_TO_RESUME",
    0x0003 :     "RF_REL_ALL_ALLOC",
    0x0004 :     "RESUMING_PEND_SUSP",
    0x0005 :     "SUSPENDING_MPS",
    0x0006 :     "SUSPENDING",
    0x0007 :     "STOP_MEAS",
    0x0008 :     "RESUMING",
    0x0009 :     "SUSPENDING_MPS_PEND_STOP",
    0x000A :     "SUSPENDING_PEND_STOP",
    0x000B :     "RESUMING_PEND_STOP",
    0x000C :     "RF_SUSPENDING_MPS",
    0x000D :     "RF_SUSP_STOPPING",
    0x000E :     "RF_SUSPENDING",
    0x000F :     "RF_SUSPENDED",
    0x0010 :     "RF_REL_ALL",
    0x0011 :     "RESUMING_MPS_PEND_STOP",
    0x0012 :     "RESUMING_MPS",
    0x0013 :     "TERMINATE",
    0x0014 :     "BUTT",
}

cproc_hrpd_sm_mps_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "QUICK_MPS_ONE_SHOT",
    0x0002 :     "QUICK_MPS",
    0x0003 :     "SUSPENDED",
    0x0004 :     "MPS",
    0x0005 :     "STOP_MPS",
    0x0006 :     "TERMINATE",
    0x0007 :     "BUTT",
}

cproc_hrpd_cm_power_on_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_CPROC_RM",
    0x0002 :     "WAITING_CNF",
    0x0003 :     "TERMINATE",
    0x0004 :     "BUTT",
}

cproc_hrpd_cm_sls_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "SLS_WAIT_REOURCE",
    0x0002 :     "SLS_WAIT_RXON",
    0x0003 :     "SCANNING",
    0x0004 :     "STOPPING",
    0x0005 :     "WAIT_SLS_IND",
    0x0006 :     "RELEASING",
    0x0007 :     "SUSPENDING_SLS",
    0x0008 :     "SUSPENDING_RADIO",
    0x0009 :     "SLAVE_WAIT_GAP",
    0x000A :     "TERMINATE",
    0x000B :     "BUTT",
}

cproc_hrpd_cm_reset_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAITING_CONFIRMS",
    0x0002 :     "WAITING_RM_INIT_CNF",
    0x0003 :     "TERMINATE",
    0x0004 :     "BUTT",
}

cproc_hrpd_sm_reset_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAITING_CONFIRM",
    0x0002 :     "TERMINATE",
    0x0003 :     "BUTT",
}

cproc_hrpd_cm_pilot_search_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "PS_WAIT_RESOURCE",
    0x0002 :     "WAIT_RXON",
    0x0003 :     "WAIT_PS_IND",
    0x0004 :     "NO_PILOT_FOUND",
    0x0005 :     "REL_ALL_WAIT_RXON",
    0x0006 :     "REL_ALL_WAIT_RXON_AFTER_GAP",
    0x0007 :     "REL_ALL_STOPPING",
    0x0008 :     "SUSPENDED",
    0x0009 :     "SLAVE_WAIT_GAP",
    0x000A :     "SLAVE_WAIT_GAP_STOPPING",
    0x000B :     "TERMINATE",
    0x000C :     "BUTT",
}

cproc_hrpd_cm_tch_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_SART_CNF",
    0x0002 :     "TCH",
    0x0003 :     "STOPPING",
    0x0004 :     "CC_MPS",
    0x0005 :     "SUSPENDED",
    0x0006 :     "HANDOFF",
    0x0007 :     "CC_SUSPENDING",
    0x0008 :     "REL_WAIT_CNF",
    0x0009 :     "REL_STOPPING",
    0x000A :     "TERMINATE",
    0x000B :     "BUTT",
}

cproc_hrpd_cm_paging_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "START_MPS",
    0x0002 :     "RX_FIRST_SLOT",
    0x0003 :     "MONITOR_CC",
    0x0004 :     "MEAS_BUFFER",
    0x0005 :     "STOPPING",
    0x0006 :     "STOPPING_NEW_REQ",
    0x0007 :     "TERMINATE",
    0x0008 :     "BUTT",
}

cproc_hrpd_cm_drx_state_enum_table_0000 = {
    0x0000 :     "INITIAL",
    0x0001 :     "LPHY_WAKEUP",
    0x0002 :     "ERLEASE",
    0x0003 :     "STOP_CC",
    0x0004 :     "REL_ACTIVITY",
    0x0005 :     "LTE_MEAS_BSR",
    0x0006 :     "SLEEP",
    0x0007 :     "PAGING",
    0x0008 :     "WAIT_RESOURCE_IND",
    0x0009 :     "SUSPENGING",
    0x000A :     "STOP_CC_NO_ALLOC",
    0x000B :     "WAIT_PAGING",
    0x000C :     "TIME_SYNC",
    0x000D :     "START_PAGING",
    0x000E :     "RELEASE_TIME_SYNC",
    0x000F :     "TERMINATE",
    0x0010 :     "BUTT",
}

cproc_hrpd_cm_lphy_wakeup_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_WAKEUP_CNF_SUSP",
    0x0002 :     "WAIT_WAKEUP_CNF",
    0x0003 :     "RELEASING_SUSP",
    0x0004 :     "RELEASING",
    0x0005 :     "WAIT_WAKEUP_IND_SUSP",
    0x0006 :     "WAIT_WAKEUP_IND",
    0x0007 :     "TERMINATE",
    0x0008 :     "BUTT",
}

cproc_hrpd_cm_sync_time_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_RESOURCE",
    0x0002 :     "ALLOCATED",
    0x0003 :     "SUSPENDING",
    0x0004 :     "ENDING",
    0x0005 :     "RELEASING",
    0x0006 :     "TERMINATE",
    0x0007 :     "BUTT",
}

cproc_hrpd_cm_sync_time_ch_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "START_MPS",
    0x0002 :     "MPS",
    0x0003 :     "STOP",
    0x0004 :     "WAIT_CNF",
    0x0005 :     "RELEASE",
    0x0006 :     "TERMINATE",
    0x0007 :     "BUTT",
}

cproc_hrpd_cm_agps_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "NO_SYNC",
    0x0002 :     "WAIT_RESULT",
    0x0003 :     "TERMINATE",
    0x0004 :     "BUTT",
}

cproc_hrpd_sm_measurement_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "GAP_STOPPING",
    0x0002 :     "DRX_STOPPING",
    0x0003 :     "CC_MEAS_NOT_CFG",
    0x0004 :     "CONFIGURED",
    0x0005 :     "MEAS_NSF",
    0x0006 :     "MEAS_SF",
    0x0007 :     "MASTER_IDLE",
    0x0008 :     "STOPPING",
    0x0009 :     "TCH_MEAS_NOT_CFG",
    0x000A :     "DRX_MEAS_NOT_CFG",
    0x000B :     "DRX",
    0x000C :     "TERMINATE",
    0x000D :     "BUTT",
}

cproc_hrpd_sm_ps_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "SELECT_PN",
    0x0002 :     "SELECT_PN_SUSPENDING",
    0x0003 :     "SEARCHING",
    0x0004 :     "SUSPENDING",
    0x0005 :     "STOPPING",
    0x0006 :     "TERMINATE",
    0x0007 :     "BUTT",
}

cproc_hrpd_cm_svlte_irat_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_RESOURCE",
    0x0002 :     "LTE_MEAS_BSR",
    0x0003 :     "WAIT_MEAS",
    0x0004 :     "TERMINATE",
    0x0005 :     "BUTT",
}

cproc_hrpd_sm_measmode_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "SLAVE",
    0x0002 :     "MASTER",
    0x0003 :     "BUTT",
}

cproc_hrpd_cm_slave_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "CFG",
    0x0002 :     "MEAS_PS",
    0x0003 :     "MEAS_CC",
    0x0004 :     "MEAS_WAIT_GAP_IND",
    0x0005 :     "MEAS",
    0x0006 :     "MEAS_CFG",
    0x0007 :     "MEAS_NEW_GAP",
    0x0008 :     "PILOT_SEARCH",
    0x0009 :     "CC_MONITOR",
    0x000A :     "CFG_STOPPING",
    0x000B :     "TERMINATE",
    0x000C :     "BUTT",
}

cproc_hrpd_sm_slavemeasurement_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "GET_TIMING",
    0x0002 :     "WAIT_GAP_CFG",
    0x0003 :     "SEARCH_TIMING",
    0x0004 :     "MEAS_CFG",
    0x0005 :     "MEAS_GAP",
    0x0006 :     "RECFG",
    0x0007 :     "RECFG_GAP",
    0x0008 :     "STOPPING",
    0x0009 :     "TERMINATE",
    0x000A :     "BUTT",
}

cproc_hrpd_cm_drx_irat_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_LTE_MEAS",
    0x0002 :     "LTE_MEAS",
    0x0003 :     "WAIT_INT2",
    0x0004 :     "WAIT_LTE_BSR",
    0x0005 :     "LTE_BSR",
    0x0006 :     "DONE_WAIT_INT2",
    0x0007 :     "TERMINATE",
    0x0008 :     "BUTT",
}

cproc_hrpd_rm_assignment_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "SUSPENDING",
    0x0002 :     "RM_SUSPEND_PREEMPTED",
    0x0003 :     "RM_SUSPEND",
    0x0004 :     "SUSPENDED",
    0x0005 :     "WAIT_ASSIGN",
    0x0006 :     "ASSIGNED",
    0x0007 :     "ASSIGN_NEW",
    0x0008 :     "PENDING_RESUME",
    0x0009 :     "TERMINATE",
    0x000A :     "BUTT",
}

cproc_hrpd_rm_wait_paging_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_ASSIGN",
    0x0002 :     "WAIT_PAGING_APPLY",
    0x0003 :     "TERMINATE",
    0x0004 :     "BUTT",
}

cproc_hrpd_rm_rat_top_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_REL_CNF",
    0x0002 :     "WAIT_RELEASE_ALL",
    0x0003 :     "INIT",
    0x0004 :     "IDLE",
    0x0005 :     "WAIT_PAGING_ASSIGN",
    0x0006 :     "ASSIGNED",
    0x0007 :     "BUTT",
}

cproc_hrpd_rm_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "IDLE",
    0x0002 :     "ASSIGNED_1X",
    0x0003 :     "ASSIGNED_HRPD",
    0x0004 :     "BUTT",
}

cproc_hrpd_cm_ac_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "ACCESS",
    0x0002 :     "AC_STOPPING",
    0x0003 :     "AC_SUSPENDING",
    0x0004 :     "TERMINATE",
    0x0005 :     "BUTT",
}

cproc_hrpd_cm_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "POWER_ON",
    0x0002 :     "SET_MODE",
    0x0003 :     "MASTER_FREE",
    0x0004 :     "PILOT_SEARCH",
    0x0005 :     "CC_MONITOR",
    0x0006 :     "ACCESS",
    0x0007 :     "CONNECTED",
    0x0008 :     "IDLE_DRX",
    0x0009 :     "SLAVE_FREE",
    0x000A :     "TERMINATE",    
    0x000B :     "BUTT",
}

cproc_hrpd_cm_set_mode_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "SLAVE_KEEP_TIMING",
    0x0002 :     "SLAVE_KEEP_TIMING_WAIT_CONF",
    0x0003 :     "WAITING_CONFIRM",
    0x0004 :     "SLAVE_WAITING_CONFIRM",
    0x0005 :     "TERMINATE",
    0x0006 :     "BUTT",
}

cproc_hrpd_cm_cc_ch_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "START_QUICK_MPS_NO_TIME",
    0x0002 :     "START_MPS_NO_TIME",
    0x0003 :     "START_CC_NO_TIME",
    0x0004 :     "CC_NO_TIME",
    0x0005 :     "STOP_SET_TIME",
    0x0006 :     "SET_TIME",
    0x0007 :     "START_QUICK_MPS",
    0x0008 :     "START_MPS",
    0x0009 :     "START_CC",
    0x000A :     "CC",
    0x000B :     "WAIT_ALLOCATION",
    0x000C :     "HANDOFF",
    0x000D :     "REL_WAIT_MPS_CNF_NO_TIME",
    0x000E :     "REL_WAIT_CC_CNF_NO_TIME",
    0x000F :     "REL_STOPPING_NO_TIME",
    0x0010 :     "REL_STOP_SET_TIME",
    0x0011 :     "REL_SET_TIME",
    0x0012 :     "REL_WAIT_MPS_CNF",
    0x0013 :     "REL_WAIT_CC_CNF",
    0x0014 :     "REL_STOPPING",
    0x0015 :     "DRX_STOPPING",
    0x0016 :     "RESET_MPS_SET_TIME",
    0x0017 :     "TERMINATE",
    0x0018 :     "BUTT",
}

cproc_hrpd_cm_cc_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "CC_MONITOR",
    0x0002 :     "CC_NO_ALLOC_NO_TIME",
    0x0003 :     "WAIT_INITAL_TX",
    0x0004 :     "WAIT_RX_OFF",
    0x0005 :     "CC_NO_ALLOC",
    0x0006 :     "CC_SUSPENDING",
    0x0007 :     "CC_WAIT_TX_ALLOC",
    0x0008 :     "NO_ALLOC_SET_TIME",
    0x0009 :     "ALLOC_SET_TIME",
    0x000A :     "CC_STOPPING",
    0x000B :     "TERMINATE",
    0x000C :     "BUTT",
}

cproc_hrpd_cm_tch_ho_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "STOPPING",
    0x0002 :     "WAIT_RXON",
    0x0003 :     "RESUMING_MPS",
    0x0004 :     "RESUMING",
    0x0005 :     "SUSPENDED_STOP",
    0x0006 :     "TERMINATE",
    0x0007 :     "BUTT",
}

cproc_hrpd_cm_ac_ch_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_RESUMED_RSP",
    0x0002 :     "SUSPENDING",
    0x0003 :     "SUSP_WAIT_CNF",
    0x0004 :     "STOP_WAIT_CNF",
    0x0005 :     "WAIT_START_CNF",
    0x0006 :     "WAIT_START_IND",
    0x0007 :     "TRANSMITTING",
    0x0008 :     "STOPPING",
    0x0009 :     "REL_RESUMED_RSP",
    0x000A :     "REL_WAIT_CNF",
    0x000B :     "REL_STOPPING",
    0x000C :     "TERMINATE",
    0x000D :     "BUTT",
}

cproc_hrpd_cm_suspend_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_TO_RESUME_STOPPING",
    0x0002 :     "WAIT_TO_RESUME",
    0x0003 :     "RF_REL_ALL_ALLOC",
    0x0004 :     "RESUMING_PEND_SUSP",
    0x0005 :     "SUSPENDING_MPS",
    0x0006 :     "SUSPENDING",
    0x0007 :     "STOP_MEAS",
    0x0008 :     "RESUMING",
    0x0009 :     "SUSPENDING_MPS_PEND_STOP",
    0x000A :     "SUSPENDING_PEND_STOP",
    0x000B :     "RESUMING_PEND_STOP",
    0x000C :     "RF_SUSPENDING_MPS",
    0x000D :     "RF_SUSP_STOPPING",
    0x000E :     "RF_SUSPENDING",
    0x000F :     "RF_SUSPENDED",
    0x0010 :     "RF_REL_ALL",
    0x0011 :     "RESUMING_MPS_PEND_STOP",
    0x0012 :     "RESUMING_MPS",
    0x0013 :     "TERMINATE",
    0x0014 :     "BUTT",
}

cproc_hrpd_sm_mps_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "QUICK_MPS_ONE_SHOT",
    0x0002 :     "QUICK_MPS",
    0x0003 :     "SUSPENDED",
    0x0004 :     "MPS",
    0x0005 :     "STOP_MPS",
    0x0006 :     "TERMINATE",
    0x0007 :     "BUTT",
}

cproc_hrpd_cm_power_on_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_CPROC_RM",
    0x0002 :     "WAITING_CNF",
    0x0003 :     "TERMINATE",
    0x0004 :     "BUTT",
}

cproc_hrpd_cm_sls_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "SLS_WAIT_REOURCE",
    0x0002 :     "SLS_WAIT_RXON",
    0x0003 :     "SCANNING",
    0x0004 :     "STOPPING",
    0x0005 :     "WAIT_SLS_IND",
    0x0006 :     "RELEASING",
    0x0007 :     "SUSPENDING_SLS",
    0x0008 :     "SUSPENDING_RADIO",
    0x0009 :     "SLAVE_WAIT_GAP",
    0x000A :     "TERMINATE",
    0x000B :     "BUTT",
}

cproc_hrpd_cm_reset_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAITING_CONFIRMS",
    0x0002 :     "WAITING_RM_INIT_CNF",
    0x0003 :     "TERMINATE",
    0x0004 :     "BUTT",
}

cproc_hrpd_sm_reset_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAITING_CONFIRM",
    0x0002 :     "TERMINATE",
    0x0003 :     "BUTT",
}

cproc_hrpd_cm_pilot_search_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "PS_WAIT_RESOURCE",
    0x0002 :     "WAIT_RXON",
    0x0003 :     "WAIT_PS_IND",
    0x0004 :     "NO_PILOT_FOUND",
    0x0005 :     "REL_ALL_WAIT_RXON",
    0x0006 :     "REL_ALL_WAIT_RXON_AFTER_GAP",
    0x0007 :     "REL_ALL_STOPPING",
    0x0008 :     "SUSPENDED",
    0x0009 :     "SUSPENDED_STOPPED",
    0x000A :     "SLAVE_WAIT_GAP",
    0x000B :     "SET_TIME",
    0x000C :     "TERMINATE",
    0x000D :     "BUTT",
}

cproc_hrpd_cm_tch_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_SART_CNF",
    0x0002 :     "TCH",
    0x0003 :     "STOPPING",
    0x0004 :     "CC_MPS",
    0x0005 :     "SUSPENDED",
    0x0006 :     "HANDOFF",
    0x0007 :     "CC_SUSPENDING",
    0x0008 :     "REL_WAIT_CNF",
    0x0009 :     "REL_STOPPING",
    0x000A :     "TERMINATE",
    0x000B :     "BUTT",
}

cproc_hrpd_cm_paging_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "START_MPS",
    0x0002 :     "RX_FIRST_SLOT",
    0x0003 :     "MONITOR_CC",
    0x0004 :     "MEAS_BUFFER",
    0x0005 :     "STOPPING",
    0x0006 :     "STOPPING_NEW_REQ",
    0x0007 :     "TERMINATE",
    0x0008 :     "BUTT",
}

cproc_hrpd_cm_drx_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_WAKEUP_IND",
    0x0002 :     "RELEASE",
    0x0003 :     "STOP_CC",
    0x0004 :     "REL_ACTIVITY",
    0x0005 :     "LTE_MEAS_BSR",
    0x0006 :     "SLEEP",
    0x0007 :     "PAGING",
    0x0008 :     "WAIT_RESOURCE_IND",
    0x0009 :     "SUSPENGING",
    0x000A :     "STOP_CC_NO_ALLOC",
    0x000B :     "WAIT_PAGING",
    0x000C :     "TIME_SYNC",
    0x000D :     "RELEASE_TIME_SYNC",
    0x000E :     "TERMINATE",
    0x000F :     "BUTT",
}

cproc_hrpd_cm_lte_irat_state_enum_table_0100 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_WAKEUP",
    0x0002 :     "SUSPENDED",
    0x0003 :     "LTE_MEAS_BSR",
    0x0004 :     "RESTART_MEAS",
    0x0005 :     "TERMINATE",
    0x0006 :     "BUTT",
}

cproc_hrpd_cm_lphy_wakeup_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_WAKEUP_CNF_SUSP",
    0x0002 :     "WAIT_WAKEUP_CNF",
    0x0003 :     "RELEASING_SUSP",
    0x0004 :     "RELEASING",
    0x0005 :     "WAIT_WAKEUP_IND_SUSP",
    0x0006 :     "WAIT_WAKEUP_IND",
    0x0007 :     "TERMINATE",
    0x0008 :     "BUTT",
}

cproc_hrpd_cm_sync_time_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_RESOURCE",
    0x0002 :     "ALLOCATED",
    0x0003 :     "SUSPENDING",
    0x0004 :     "ENDING",
    0x0005 :     "RELEASING",
    0x0006 :     "TERMINATE",
    0x0007 :     "BUTT",
}

cproc_hrpd_cm_sync_time_ch_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "START_MPS",
    0x0002 :     "STOP",
    0x0003 :     "RELEASE",
    0x0004 :     "TERMINATE",
    0x0005 :     "BUTT",
}

cproc_hrpd_cm_agps_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "NO_SYNC",
    0x0002 :     "WAIT_RESULT",
    0x0003 :     "TERMINATE",
    0x0004 :     "BUTT",
}

cproc_hrpd_sm_measurement_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "GAP_STOPPING",
    0x0002 :     "DRX_STOPPING",
    0x0003 :     "CC_MEAS_NOT_CFG",
    0x0004 :     "CONFIGURED",
    0x0005 :     "MEAS_NSF",
    0x0006 :     "MEAS_SF",
    0x0007 :     "MASTER_IDLE",
    0x0008 :     "STOPPING",
    0x0009 :     "TCH_MEAS_NOT_CFG",
    0x000A :     "DRX_MEAS_NOT_CFG",
    0x000B :     "DRX",
    0x000C :     "DRX_MEAS_STOPPED",
    0x000D :     "TERMINATE",
    0x000E :     "BUTT",
}

cproc_hrpd_sm_ps_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "REQUEST_RF",
    0x0002 :     "SELECT_PN",
    0x0003 :     "SELECT_PN_SUSPENDING",
    0x0004 :     "SEARCHING",
    0x0005 :     "SUSPENDING",
    0x0006 :     "STOPPING",
    0x0007 :     "QUICK_MPS",
    0x0008 :     "QUICK_MPS_SUSPENDING",
    0x0009 :     "TERMINATE",
    0x000A :     "BUTT",
}

cproc_hrpd_cm_svlte_irat_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_RESOURCE",
    0x0002 :     "LTE_MEAS_BSR",
    0x0003 :     "WAIT_MEAS",
    0x0004 :     "TERMINATE",
    0x0005 :     "BUTT",
}

cproc_hrpd_sm_measmode_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "SLAVE",
    0x0002 :     "MASTER",
    0x0003 :     "BUTT",
}

cproc_hrpd_cm_slave_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "CFG",
    0x0002 :     "MEAS_PS",
    0x0003 :     "MEAS_CC",
    0x0004 :     "MEAS_WAIT_GAP_IND",
    0x0005 :     "MEAS",
    0x0006 :     "MEAS_CFG",
    0x0007 :     "MEAS_NEW_GAP",
    0x0008 :     "PILOT_SEARCH",
    0x0009 :     "CC_MONITOR",
    0x000A :     "CFG_STOPPING",
    0x000B :     "TERMINATE",
    0x000C :     "BUTT",
}

cproc_hrpd_sm_slavemeasurement_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "GET_TIMING",
    0x0002 :     "WAIT_GAP_CFG",
    0x0003 :     "SEARCH_TIMING",
    0x0004 :     "MEAS_CFG",
    0x0005 :     "MEAS_GAP",
    0x0006 :     "RECFG",
    0x0007 :     "RECFG_GAP",
    0x0008 :     "STOPPING",
    0x0009 :     "TERMINATE",
    0x000A :     "BUTT",
}

cproc_hrpd_cm_drx_irat_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_LTE_MEAS",
    0x0002 :     "LTE_MEAS",
    0x0003 :     "WAIT_INT2",
    0x0004 :     "WAIT_LTE_BSR",
    0x0005 :     "LTE_BSR",
    0x0006 :     "DONE_WAIT_INT2",
    0x0007 :     "TERMINATE",
    0x0008 :     "BUTT",
}

cproc_hrpd_rm_assignment_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "SUSPENDING",
    0x0002 :     "RM_SUSPEND_PREEMPTED",
    0x0003 :     "RM_SUSPEND",
    0x0004 :     "SUSPENDED",
    0x0005 :     "WAIT_ASSIGN",
    0x0006 :     "ASSIGNED",
    0x0007 :     "ASSIGN_NEW",
    0x0008 :     "PENDING_RESUME",
    0x0009 :     "TERMINATE",
    0x000A :     "BUTT",
}

cproc_hrpd_rm_wait_paging_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_ASSIGN",
    0x0002 :     "WAIT_PAGING_APPLY",
    0x0003 :     "TERMINATE",
    0x0004 :     "BUTT",
}

cproc_hrpd_rm_rat_top_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_REL_CNF",
    0x0002 :     "WAIT_RELEASE_ALL",
    0x0003 :     "INIT",
    0x0004 :     "IDLE",
    0x0005 :     "WAIT_PAGING_ASSIGN",
    0x0006 :     "ASSIGNED",
    0x0007 :     "BUTT",
}

cproc_hrpd_rm_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "IDLE",
    0x0002 :     "ASSIGNED_1X",
    0x0003 :     "ASSIGNED_HRPD",
    0x0004 :     "ASSIGNED_CBT",
    0x0005 :     "BUTT",
}

cproc_hrpd_cm_ac_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "ACCESS",
    0x0002 :     "AC_STOPPING",
    0x0003 :     "AC_SUSPENDING",
    0x0004 :     "TERMINATE",
    0x0005 :     "BUTT",
}

cproc_hrpd_cm_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "POWER_ON",
    0x0002 :     "SET_MODE",
    0x0003 :     "MASTER_FREE",
    0x0004 :     "PILOT_SEARCH",
    0x0005 :     "CC_MONITOR",
    0x0006 :     "ACCESS",
    0x0007 :     "CONNECTED",
    0x0008 :     "IDLE_DRX",
    0x0009 :     "SLAVE_FREE",
    0x000A :     "TERMINATE",    
    0x000B :     "BUTT",
}

cproc_hrpd_cm_set_mode_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "SLAVE_KEEP_TIMING",
    0x0002 :     "SLAVE_KEEP_TIMING_WAIT_CONF",
    0x0003 :     "WAITING_CONFIRM",
    0x0004 :     "SLAVE_WAITING_CONFIRM",
    0x0005 :     "TERMINATE",
    0x0006 :     "BUTT",
}

cproc_hrpd_cm_cc_ch_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "START_QUICK_MPS_NO_TIME",
    0x0002 :     "START_MPS_NO_TIME",
    0x0003 :     "START_CC_NO_TIME",
    0x0004 :     "CC_NO_TIME",
    0x0005 :     "STOP_SET_TIME",
    0x0006 :     "SET_TIME",
    0x0007 :     "START_QUICK_MPS",
    0x0008 :     "START_MPS",
    0x0009 :     "START_CC",
    0x000A :     "CC",
    0x000B :     "WAIT_ALLOCATION",
    0x000C :     "HANDOFF",
    0x000D :     "REL_WAIT_CC_CNF_NO_TIME",
    0x000E :     "REL_STOPPING_NO_TIME",
    0x000F :     "REL_STOP_SET_TIME",
    0x0010 :     "REL_SET_TIME",
    0x0011 :     "REL_WAIT_MPS_CNF",
    0x0012 :     "REL_WAIT_CC_CNF",
    0x0013 :     "REL_STOPPING",
    0x0014 :     "DRX_STOPPING",
    0x0015 :     "RESET_MPS_SET_TIME",
    0x0016 :     "TERMINATE",
    0x0017 :     "BUTT",
}

cproc_hrpd_cm_cc_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "CC_MONITOR",
    0x0002 :     "CC_NO_ALLOC_NO_TIME",
    0x0003 :     "CC_WAIT_INITAL_TX",
    0x0004 :     "CC_WAIT_RX_OFF",
    0x0005 :     "CC_NO_ALLOC",
    0x0006 :     "CC_SUSPENDING",
    0x0007 :     "CC_WAIT_TX_ALLOC",
    0x0008 :     "CC_NO_ALLOC_SET_TIME",
    0x0009 :     "CC_STOP_SET_TIME",
    0x000A :     "CC_STOPPING",
    0x000B :     "TERMINATE",
    0x000C :     "BUTT",
}

cproc_hrpd_cm_tch_ho_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "STOPPING",
    0x0002 :     "WAIT_RXON",
    0x0003 :     "RESUMING_MPS",
    0x0004 :     "RESUMING",
    0x0005 :     "SUSPENDED_STOP",
    0x0006 :     "TERMINATE",
    0x0007 :     "BUTT",
}

cproc_hrpd_cm_ac_ch_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_RESUMED_RSP",
    0x0002 :     "SUSPENDING",
    0x0003 :     "SUSP_WAIT_CNF",
    0x0004 :     "STOP_WAIT_CNF",
    0x0005 :     "WAIT_START_CNF",
    0x0006 :     "WAIT_START_IND",
    0x0007 :     "TRANSMITTING",
    0x0008 :     "STOPPING",
    0x0009 :     "REL_RESUMED_RSP",
    0x000A :     "REL_WAIT_CNF",
    0x000B :     "REL_STOPPING",
    0x000C :     "TERMINATE",
    0x000D :     "BUTT",
}

cproc_hrpd_cm_suspend_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_TO_RESUME_STOPPING",
    0x0002 :     "WAIT_TO_RESUME",
    0x0003 :     "RF_REL_ALL_ALLOC",
    0x0004 :     "RESUMING_PEND_SUSP",
    0x0005 :     "SUSPENDING_MPS",
    0x0006 :     "SUSPENDING",
    0x0007 :     "STOP_MEAS",
    0x0008 :     "RESUMING",
    0x0009 :     "SUSPENDING_MPS_PEND_STOP",
    0x000A :     "SUSPENDING_PEND_STOP",
    0x000B :     "RESUMING_PEND_STOP",
    0x000C :     "RF_SUSPENDING_MPS",
    0x000D :     "RF_SUSP_STOPPING",
    0x000E :     "RF_SUSPENDING",
    0x000F :     "RF_SUSPENDED",
    0x0010 :     "RF_REL_ALL",
    0x0011 :     "RESUMING_MPS_PEND_STOP",
    0x0012 :     "RESUMING_MPS",
    0x0013 :     "TERMINATE",
    0x0014 :     "BUTT",
}

cproc_hrpd_sm_mps_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "QUICK_MPS_ONE_SHOT",
    0x0002 :     "QUICK_MPS",
    0x0003 :     "SUSPENDED",
    0x0004 :     "MPS",
    0x0005 :     "STOP_MPS",
    0x0006 :     "TERMINATE",
    0x0007 :     "BUTT",
}

cproc_hrpd_cm_power_on_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_CPROC_RM",
    0x0002 :     "WAITING_CNF",
    0x0003 :     "TERMINATE",
    0x0004 :     "BUTT",
}

cproc_hrpd_cm_sls_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "SLS_WAIT_REOURCE",
    0x0002 :     "SLS_WAIT_RXON",
    0x0003 :     "SCANNING",
    0x0004 :     "STOPPING",
    0x0005 :     "WAIT_SLS_IND",
    0x0006 :     "RELEASING",
    0x0007 :     "SUSPENDING_SLS",
    0x0008 :     "SUSPENDING_RADIO",
    0x0009 :     "SLAVE_WAIT_GAP",
    0x000A :     "TERMINATE",
    0x000B :     "BUTT",
}

cproc_hrpd_cm_reset_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAITING_CONFIRMS",
    0x0002 :     "WAITING_RM_INIT_CNF",
    0x0003 :     "TERMINATE",
    0x0004 :     "BUTT",
}

cproc_hrpd_sm_reset_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAITING_CONFIRM",
    0x0002 :     "TERMINATE",
    0x0003 :     "BUTT",
}

cproc_hrpd_cm_pilot_search_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "PS_WAIT_RESOURCE",
    0x0002 :     "WAIT_RXON",
    0x0003 :     "WAIT_PS_IND",
    0x0004 :     "WAIT_RXOFF_PS_IND",
    0x0005 :     "WAIT_PS_IND_NO_RF",
    0x0006 :     "WAIT_RESOURCE_PS_IND",
    0x0007 :     "WAIT_RESOURCE_RF_IND",
    0x0008 :     "NO_PILOT_FOUND",
    0x0009 :     "REL_ALL_WAIT_RXON",
    0x000A :     "REL_ALL_WAIT_RXON_AFTER_GAP",
    0x000B :     "REL_ALL_STOPPING",
    0x000C :     "SUSPENDED",
    0x000D :     "SUSPENDED_STOPPED",
    0x000E :     "SLAVE_WAIT_GAP",
    0x000F :     "SET_TIME",
    0x0010 :     "TERMINATE",
    0x0011 :     "BUTT",
}

cproc_hrpd_cm_tch_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_SART_CNF",
    0x0002 :     "TCH",
    0x0003 :     "STOPPING",
    0x0004 :     "CC_MPS",
    0x0005 :     "SUSPENDED",
    0x0006 :     "HANDOFF",
    0x0007 :     "CC_SUSPENDING",
    0x0008 :     "REL_WAIT_CNF",
    0x0009 :     "REL_STOPPING",
    0x000A :     "TERMINATE",
    0x000B :     "BUTT",
}

cproc_hrpd_cm_paging_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "START_MPS",
    0x0002 :     "RX_FIRST_SLOT",
    0x0003 :     "MONITOR_CC",
    0x0004 :     "MEAS_BUFFER",
    0x0005 :     "STOPPING",
    0x0006 :     "STOPPING_NEW_REQ",
    0x0007 :     "TERMINATE",
    0x0008 :     "BUTT",
}

cproc_hrpd_cm_drx_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_WAKEUP_IND",
    0x0002 :     "RELEASE",
    0x0003 :     "STOP_CC",
    0x0004 :     "REL_ACTIVITY",
    0x0005 :     "LTE_MEAS_BSR",
    0x0006 :     "SLEEP",
    0x0007 :     "PAGING",
    0x0008 :     "WAIT_RESOURCE_IND",
    0x0009 :     "SUSPENGING",
    0x000A :     "STOP_CC_NO_ALLOC",
    0x000B :     "WAIT_PAGING",
    0x000C :     "TIME_SYNC",
    0x000D :     "RELEASE_TIME_SYNC",
    0x000E :     "TERMINATE",
    0x000F :     "BUTT",
}

cproc_hrpd_cm_lte_irat_state_enum_table_0101 = {
    0x0000 :     "INITIAL",
    0x0001 :     "WAIT_WAKEUP",
    0x0002 :     "SUSPENDED",
    0x0003 :     "LTE_MEAS_BSR",
    0x0004 :     "RESTART_MEAS",
    0x0005 :     "TERMINATE",
    0x0006 :     "BUTT",
}

def get_cproc_hrpd_fsm_str(MsgId):
    for MsgIdIndex in cproc_hrpd_fsm_enum_table.keys():
        if MsgIdIndex == MsgId:
            return cproc_hrpd_fsm_enum_table[MsgIdIndex]

    return "unknown"

def get_cproc_hrpd_state_str(state_table, state):
    for MsgIdIndex in state_table.keys():
        if MsgIdIndex == state:
            return state_table[MsgIdIndex]

    return "unknown"
	
def get_cproc_hrpd_fsm_state_str_0000(strFsmId, ucCurState):

    if ( strFsmId.upper() in ['CPROC_HRPD_CM_DRX_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_drx_state_enum_table_0000, ucCurState)
    
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_PAGING_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_paging_state_enum_table_0000, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_TCH_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_tch_state_enum_table_0000, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_PILOT_SEARCH_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_pilot_search_state_enum_table_0000, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_HRPD_SM_RESET_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_sm_reset_state_enum_table_0000, ucCurState)
	
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_RESET_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_reset_state_enum_table_0000, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_SLS_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_sls_state_enum_table_0000, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_POWER_ON_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_power_on_state_enum_table_0000, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_HRPD_SM_MPS_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_sm_mps_state_enum_table_0000, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_SUSPEND_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_suspend_state_enum_table_0000, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_AC_CH_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_ac_ch_state_enum_table_0000, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_TCH_HO_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_tch_ho_state_enum_table_0000, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_CC_CH_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_cc_ch_state_enum_table_0000, ucCurState)
	
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_CC_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_cc_state_enum_table_0000, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_SET_MODE_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_set_mode_state_enum_table_0000, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_state_enum_table_0000, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_AC_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_ac_state_enum_table_0000, ucCurState)	
			
    elif ( strFsmId.upper() in ['CPROC_RM_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_rm_state_enum_table_0000, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_RM_RAT_TOP_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_rm_rat_top_state_enum_table_0000, ucCurState)
	
    elif ( strFsmId.upper() in ['CPROC_RM_WAIT_PAGING_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_rm_wait_paging_state_enum_table_0000, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_RM_ASSIGNMENT_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_rm_assignment_state_enum_table_0000, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_DRX_IRAT_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_drx_irat_state_enum_table_0000, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_HRPD_SM_SLAVEMEASUREMENT_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_sm_slavemeasurement_state_enum_table_0000, ucCurState)
	
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_SLAVE_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_slave_state_enum_table_0000, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_SM_MEASMODE_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_sm_measmode_state_enum_table_0000, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_SVLTE_IRAT_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_svlte_irat_state_enum_table_0000, ucCurState)
	
    elif ( strFsmId.upper() in ['CPROC_HRPD_SM_PS_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_sm_ps_state_enum_table_0000, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_SM_MEASUREMENT_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_sm_measurement_state_enum_table_0000, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_AGPS_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_agps_state_enum_table_0000, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_SYNC_TIME_CH_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_sync_time_ch_state_enum_table_0000, ucCurState)	

    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_SYNC_TIME_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_sync_time_state_enum_table_0000, ucCurState)
	
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_LPHY_WAKEUP_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_lphy_wakeup_state_enum_table_0000, ucCurState)
		
    else:
        return 'unknown'

def get_cproc_hrpd_fsm_state_str_0100(strFsmId, ucCurState):

    if ( strFsmId.upper() in ['CPROC_HRPD_CM_DRX_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_drx_state_enum_table_0100, ucCurState)
    
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_PAGING_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_paging_state_enum_table_0100, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_TCH_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_tch_state_enum_table_0100, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_PILOT_SEARCH_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_pilot_search_state_enum_table_0100, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_HRPD_SM_RESET_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_sm_reset_state_enum_table_0100, ucCurState)
	
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_RESET_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_reset_state_enum_table_0100, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_SLS_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_sls_state_enum_table_0100, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_POWER_ON_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_power_on_state_enum_table_0100, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_HRPD_SM_MPS_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_sm_mps_state_enum_table_0100, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_SUSPEND_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_suspend_state_enum_table_0100, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_AC_CH_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_ac_ch_state_enum_table_0100, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_TCH_HO_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_tch_ho_state_enum_table_0100, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_CC_CH_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_cc_ch_state_enum_table_0100, ucCurState)
	
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_CC_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_cc_state_enum_table_0100, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_SET_MODE_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_set_mode_state_enum_table_0100, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_state_enum_table_0100, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_AC_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_ac_state_enum_table_0100, ucCurState)	
			
    elif ( strFsmId.upper() in ['CPROC_RM_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_rm_state_enum_table_0100, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_RM_RAT_TOP_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_rm_rat_top_state_enum_table_0100, ucCurState)
	
    elif ( strFsmId.upper() in ['CPROC_RM_WAIT_PAGING_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_rm_wait_paging_state_enum_table_0100, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_RM_ASSIGNMENT_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_rm_assignment_state_enum_table_0100, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_DRX_IRAT_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_drx_irat_state_enum_table_0100, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_HRPD_SM_SLAVEMEASUREMENT_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_sm_slavemeasurement_state_enum_table_0100, ucCurState)
	
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_SLAVE_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_slave_state_enum_table_0100, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_SM_MEASMODE_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_sm_measmode_state_enum_table_0100, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_SVLTE_IRAT_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_svlte_irat_state_enum_table_0100, ucCurState)
	
    elif ( strFsmId.upper() in ['CPROC_HRPD_SM_PS_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_sm_ps_state_enum_table_0100, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_SM_MEASUREMENT_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_sm_measurement_state_enum_table_0100, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_AGPS_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_agps_state_enum_table_0100, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_SYNC_TIME_CH_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_sync_time_ch_state_enum_table_0100, ucCurState)	

    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_SYNC_TIME_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_sync_time_state_enum_table_0100, ucCurState)
	
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_LPHY_WAKEUP_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_lphy_wakeup_state_enum_table_0100, ucCurState)
        
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_LTE_IRAT_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_lte_irat_state_enum_table_0100, ucCurState)
		
    else:
        return 'unknown'

def get_cproc_hrpd_fsm_state_str_0101(strFsmId, ucCurState):

    if ( strFsmId.upper() in ['CPROC_HRPD_CM_DRX_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_drx_state_enum_table_0101, ucCurState)
    
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_PAGING_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_paging_state_enum_table_0101, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_TCH_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_tch_state_enum_table_0101, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_PILOT_SEARCH_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_pilot_search_state_enum_table_0101, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_HRPD_SM_RESET_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_sm_reset_state_enum_table_0101, ucCurState)
	
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_RESET_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_reset_state_enum_table_0101, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_SLS_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_sls_state_enum_table_0101, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_POWER_ON_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_power_on_state_enum_table_0101, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_HRPD_SM_MPS_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_sm_mps_state_enum_table_0101, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_SUSPEND_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_suspend_state_enum_table_0101, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_AC_CH_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_ac_ch_state_enum_table_0101, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_TCH_HO_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_tch_ho_state_enum_table_0101, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_CC_CH_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_cc_ch_state_enum_table_0101, ucCurState)
	
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_CC_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_cc_state_enum_table_0101, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_SET_MODE_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_set_mode_state_enum_table_0101, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_state_enum_table_0101, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_AC_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_ac_state_enum_table_0101, ucCurState)	
			
    elif ( strFsmId.upper() in ['CPROC_RM_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_rm_state_enum_table_0101, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_RM_RAT_TOP_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_rm_rat_top_state_enum_table_0101, ucCurState)
	
    elif ( strFsmId.upper() in ['CPROC_RM_WAIT_PAGING_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_rm_wait_paging_state_enum_table_0101, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_RM_ASSIGNMENT_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_rm_assignment_state_enum_table_0101, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_DRX_IRAT_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_drx_irat_state_enum_table_0101, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_HRPD_SM_SLAVEMEASUREMENT_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_sm_slavemeasurement_state_enum_table_0101, ucCurState)
	
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_SLAVE_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_slave_state_enum_table_0101, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_SM_MEASMODE_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_sm_measmode_state_enum_table_0101, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_SVLTE_IRAT_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_svlte_irat_state_enum_table_0101, ucCurState)
	
    elif ( strFsmId.upper() in ['CPROC_HRPD_SM_PS_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_sm_ps_state_enum_table_0101, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_SM_MEASUREMENT_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_sm_measurement_state_enum_table_0101, ucCurState)
		
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_AGPS_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_agps_state_enum_table_0101, ucCurState)

    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_SYNC_TIME_CH_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_sync_time_ch_state_enum_table_0101, ucCurState)	

    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_SYNC_TIME_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_sync_time_state_enum_table_0101, ucCurState)
	
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_LPHY_WAKEUP_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_lphy_wakeup_state_enum_table_0101, ucCurState)
        
    elif ( strFsmId.upper() in ['CPROC_HRPD_CM_LTE_IRAT_FSM'] ):
        return get_cproc_hrpd_state_str(cproc_hrpd_cm_lte_irat_state_enum_table_0101, ucCurState)
		
    else:
        return 'unknown'

def get_cproc_hrpd_fsm_state_str(strFsmId, ucCurState, usVersion):
    if (usVersion == 0x0000):
        return get_cproc_hrpd_fsm_state_str_0000(strFsmId, ucCurState)
    elif (usVersion == 0x0100 or usVersion == 0x0103):
        return get_cproc_hrpd_fsm_state_str_0100(strFsmId, ucCurState)
    elif (usVersion == 0x0101):
        return get_cproc_hrpd_fsm_state_str_0101(strFsmId, ucCurState)
    elif (usVersion == 0x0102):
        return get_cproc_hrpd_fsm_state_str_0101(strFsmId, ucCurState)
    else:
        return "unknown"


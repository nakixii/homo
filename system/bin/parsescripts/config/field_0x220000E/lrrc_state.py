#!/usr/bin/env python3
# coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2016 - 2019 Hisilicon Technoligies Co., Ltd.
# * Filename      lrrc_state.py
# * Description   tlps dump
# * Version       1.0
# * Data          2018-03-22 create file
#***********************************************************************
import string

Lrrc_fsm_id_enum_table = {

    19  : "RRC_FSM_BUTT",
}

lrrc_fsm_main_state_enum_table = {
    77  : "RRC_MS_ID_BUTT",
}

lrrc_fsm_substate_enum_table = {

    193  : "RRC_SS_ID_BUTT",
}

lrrc_state_timer_enum_table = {
    53248  : "TI_RRC_PTL_MAIN_BOUNDARY_START",
    53249  : "TI_RRC_PTL_T310",
    53250  : "TI_RRC_PTL_RRC_BOUNDARY_START",
    53251  : "TI_RRC_PTL_T300",
    53252  : "TI_RRC_PTL_T302",
    53253  : "TI_RRC_PTL_T303",
    53254  : "TI_RRC_PTL_T305",
    53255  : "TI_RRC_PTL_T306",
    53256  : "TI_RRC_PTL_T330",
    53257  : "TI_RRC_PTL_T330_DELAY",
    53258  : "TI_RRC_PTL_RLF_DELAY",
    53259  : "TI_RRC_RRC_WAIT_SIB_MP",
    53260  : "TI_RRC_RRC_CONN_REL_DELAY",
    53261  : "TI_RRC_PTL_REEST_BOUNDARY_START",
    53262  : "TI_RRC_PTL_REEST_T311",
    53263  : "TI_RRC_PTL_REEST_T301",
    53264  : "TI_RRC_PTL_RB_BOUNDARY_START",
    53265  : "TI_RRC_PTL_T304",
    53266  : "TI_RRC_PTL_CSELPC_BOUNDARY_START",
    53267  : "TI_RRC_PTL_CSEL_BOUNDARY_START",
    53268  : "TI_RRC_PTL_BSIC_VERIFY",
    53269  : "TI_RRC_PTL_CSEL_SUITABLE_CELL_DETECT",
    53270  : "TI_RRC_PTL_LOSTCOVERAGE",
    53271  : "TI_RRC_PTL_CAMPSTICK",
    53272  : "TI_RRC_PTL_T320",
    53273  : "TI_RRC_PTL_IDLE_NORMALHYST",
    53274  : "TI_RRC_PTL_RESELECTION",
    53275  : "TI_RRC_PTL_TBARRED",
    53276  : "TI_RRC_PTL_TFORBIDDEN",
    53277  : "TI_RRC_PTL_GERAN_TBARRED",
    53278  : "TI_RRC_PTL_GERAN_TFORBIDDEN",
    53279  : "TI_RRC_PTL_UTRAN_TBARRED",
    53280  : "TI_RRC_PTL_UTRAN_TFORBIDDEN",
    53281  : "TI_RRC_PTL_G2L_RESEL_PUNISH",
    53282  : "TI_RRC_PTL_W2L_REDIR_PUNISH",
    53283  : "TI_RRC_PTL_MBMS_MCCH_NOTIFY",
    53284  : "TI_RRC_PTL_RM_BOUNDARY_START",
    53285  : "TI_RRC_CMM_NC_EVT_TRIG",
    53286  : "TI_RRC_CMM_SC_EVT_TRIG",
    53287  : "TI_RRC_CMM_MOBILITY_NORMALHYST",
    53288  : "TI_RRC_CMM_PERIOD_RPT",
    53289  : "TI_RRC_PTL_T321",
    53290  : "TI_RRC_PTL_SIB_BOUNDARY_START",
    53291  : "TI_RRC_PTL_SIB_3HOUR_UPDATE",
    53292  : "TI_RRC_PAGING_VALID_TIMER",
    53293  : "TI_RRC_PTL_ASN1_BOUNDARY_START",
    53294  : "TI_RRC_PTL_MNTN_BOUNDARY_START",
    53295  : "TI_FAST_DORM_CFG_DELAY",
    53296  : "TI_IRAT_REDIR_SEARCH_TIMER",
    53297  : "TI_MTC_AREA_LOST_TIMER",
    53298  : "TI_MTCLOST_PS_TRANSFER_TIMER",
    53299  : "TI_MTCAVAILABLE_PS_TRANSFER_TIMER",
    53300  : "TI_RRC_DSDS_REL_PS_PAGING_TIMER",
    53301  : "TI_RRC_DSDS_NORF_LOST_COVERAGE",
    53302  : "TI_RRC_DSDS_SHORT_OCCUPY_RF_RECOVER",
    53303  : "TI_RRC_DSDS_DELAY_REL_REDIR_RF_RESOURCE_TIME",
    53304  : "TI_RRC_DSDS_OCCUPY_PROTECT_TIMER",
    53305  : "TI_RRC_PTL_T325",
    53306  : "TI_RRC_PTL_PWRPREF_IND_TIME",
    53307  : "TI_RRC_DAM_CELL_BAR_TIMER",
    53308  : "TI_RRC_PRINT_BUFFER_TIMER",
    53309  : "TI_RRC_CSFB_OPTIMIZE_PROTECT_TIMER",
    53310  : "TI_RRC_CHR_PUSH_NOTIFY_TIMER",
    53311  : "TI_RRC_CSG_CELL_BAR_TIMER",
    53312  : "TI_RRC_PTL_SIB_DSDS_UPDATE",
    53313  : "TI_RRC_PTL_CSG_IDLE_ASF",
    53314  : "TI_RRC_PTL_CSG_IDLE_ADD_MEASURE",
    53315  : "TI_LRRC_LCMM_CONN_ASF",
    53316  : "TI_LRRC_LCMM_PROXI_LEAVE",
    53317  : "TI_RRC_M_PAGING_VALID_TIMER",
    53318  : "TI_RRC_VOTLE_FAULT_TRIG_BYL2_AUTOAN_WAIT",
    53319  : "TI_RRC_VOTLE_FAULT_TRIG_BYL2_AUTOAN_RPT",
    53320  : "TI_RRC_INCREASE_CCPU_DDR_FREQ_TIMER",
    53321  : "TI_RRC_PTL_T307",
    53322  : "TI_RRC_PTL_T312",
    53323  : "TI_RRC_PTL_T313",
    53324  : "TI_RRC_PTL_T308",
    53325  : "TI_RRC_T300_CONN_EST_FAIL_TIMER",
    53326  : "TI_RRC_PTL_T360",
    53327  : "TI_RRC_REEST_RECOVER_PROTECT",
    53328  : "TI_RRC_CONN_REL_PROTECT",
    53329  : "TI_LRRC_IQI_MEAS_RPRT_IDLE",
    53330  : "TI_LRRC_IQI_MEAS_RPRT_CONN",
    53331  : "TI_RRC_DSDS_LTE_HO_RA_SIGNAL_PROTECT_TIMER",
    53332  : "TI_LRRC_SIB_GET_SIB1_PERIODED",
    53333  : "TI_RRC_PTL_JAM_DET_FAST_RPT_TIMER",
    53334  : "TI_DSDS_RRC_CONN_REL_REEST_RECOVER",
    53335  : "TI_LRRC_AUTO_BGS_RESEL_EVA_TIMER",
    53336  : "TI_RRC_PTL_BUTT",

    53504  : "TI_RRC_STATE_MAIN_BOUNDARY_START",
    53505  : "TI_RRC_STATE_RRC_BOUNDARY_START",
    53506  : "TI_RRC_CSELPC_CELL_RESEL_STOP_CNF",
    53507  : "TI_RRC_CSELPC_CELL_RESEL_START_CNF",
    53508  : "TI_RRC_RRC_WAIT_ITFL2_CFG_CNF",
    53509  : "TI_RRC_RRC_WAIT_ITFL2_REL_CNF",
    53510  : "TI_RRC_RRC_WAIT_ITFPHY_CFG_CNF",
    53511  : "TI_RRC_RRC_WAIT_ITFPHY_REL_CNF",
    53512  : "TI_RRC_RRC_WAIT_MAC_RA_CNF",
    53513  : "TI_RRC_RRC_WAIT_DATA_CNF",
    53514  : "TI_RRC_RRC_CSELPC_STATE_CHANGE_CNF",
    53515  : "TI_RRC_RRC_CMM_STATE_CHANGE_CNF",
    53516  : "TI_RRC_RRC_WAIT_DATA_CNF_OF_UL_TRANS",
    53517  : "TI_RRC_RRC_WAIT_RRC_CONN_EST_OR_REJECT",
    53518  : "TI_LRRC_LRRC_SS_WAIT_ITFL2_RESET_L2_CNF",
    53519  : "TI_LRRC_LRRC_WAIT_GURRC_UE_CAP_CNF",
    53520  : "TI_LRRC_LRRC_WAIT_LPHY_SET_WORK_MODE_CNF",
    53521  : "TI_LRRC_LRRC_WAIT_LCSELPC_CELL_SEARCH_CNF",
    53522  : "TI_LRRC_LRRC_WAIT_LMM_RESUME_RSP",
    53523  : "TI_LRRC_LRRC_WAIT_LMM_SUSPEND_RSP",
    53524  : "TI_LRRC_LRRC_WAIT_GURRC_CNF",
    53525  : "TI_LRRC_LRRC_WAIT_LOAD_WDSP_CNF",
    53526  : "TI_LRRC_LRRC_WAIT_GURRC_STOP_CNF",
    53527  : "TI_LRRC_LRRC_WAIT_GURRC_REL_ALL_CNF",
    53528  : "TI_LRRC_LRRC_WAIT_TRRC_UE_CAP_CNF",
    53529  : "TI_LRRC_LRRC_WAIT_TRRC_CNF",
    53530  : "TI_LRRC_LRRC_WAIT_TRRC_STOP_CNF",
    53531  : "TI_LRRC_LRRC_WAIT_TRRC_REL_ALL_CNF",
    53532  : "TI_RRC_STATE_REEST_BOUNDARY_START",
    53533  : "TI_RRC_REEST_WAIT_NAS_SUSPEND_RABM_RSP",
    53534  : "TI_RRC_REEST_WAIT_CMM_STATE_CHANGE_CNF",
    53535  : "TI_RRC_REEST_WAIT_ITFL2_CONFIG_L2_CNF",
    53536  : "TI_RRC_REEST_WAIT_ITFPHY_CONFIG_PHY_CNF",
    53537  : "TI_LRRC_LREEST_WAIT_GURRC_REL_ALL_CNF",
    53538  : "TI_LRRC_LREEST_WAIT_TRRC_REL_ALL_CNF",
    53539  : "TI_RRC_REEST_WAIT_CSELPC_STATE_CHANGE_CNF",
    53540  : "TI_RRC_REEST_WAIT_MAC_RA_CNF",
    53541  : "TI_RRC_REEST_WAIT_PDCP_DATA_CNF",
    53542  : "TI_RRC_REEST_CONN_REEST_T301",
    53543  : "TI_RRC_REEST_WAIT_RRC_CONN_REEST_OR_REJECT",
    53544  : "TI_RRC_REEST_WAIT_SMC_SECU_CONFIG_CNF",
    53545  : "TI_RRC_REEST_WAIT_DSDS_RADIO_RESOURCE_CNF",
    53546  : "TI_RRC_STATE_TI_RB_BOUNDARY_START",
    53547  : "TI_RRC_RB_WAIT_RABM_STATUS_RSP",
    53548  : "TI_RRC_RB_WAIT_CMM_HO_CNF",
    53549  : "TI_RRC_RB_WAIT_ITFPHY_CFG_CNF",
    53550  : "TI_RRC_RB_WAIT_PHY_SYNC_CNF",
    53551  : "TI_RRC_RB_WAIT_ITFL2_CFG_CNF",
    53552  : "TI_RRC_RB_WAIT_SMC_SECU_CFG_CNF",
    53553  : "TI_RRC_RB_WAIT_RABM_STATUS_CNF",
    53554  : "TI_RRC_RB_WAIT_CMM_MEAS_CTRL_CNF",
    53555  : "TI_RRC_RB_WAIT_PDCP_DATA_CNF",
    53556  : "TI_RRC_RB_WAIT_REL_NEW_RB_CNF",
    53557  : "TI_LRRC_LRB_WAIT_LPHY_SET_WORK_MODE_CNF",
    53558  : "TI_LRRC_LRB_WAIT_MM_SECU_PARA_RSP",
    53559  : "TI_LRRC_LRB_WAIT_MM_RESUME_RSP",
    53560  : "TI_LRRC_LRB_WAIT_GURRC_REL_ALL_CNF",
    53561  : "TI_RRC_STATE_CSELPC_BOUNDARY_START",
    53562  : "TI_RRC_CSELPC_WAIT_CONFIG_PHY_CNF",
    53563  : "TI_RRC_CSELPC_WAIT_PHY_CAMPED_CELL_CNF",
    53564  : "TI_RRC_CSELPC_WAIT_CONFIG_L2_CNF",
    53565  : "TI_RRC_CSELPC_WAIT_CSEL_SPEC_PLMN_SEARCH_CNF",
    53566  : "TI_RRC_CSELPC_WAIT_CSEL_PLMN_LIST_SEARCH_CNF",
    53567  : "TI_RRC_CSELPC_WAIT_CSEL_STOP_PLMN_LIST_CNF",
    53568  : "TI_RRC_CSELPC_WAIT_CSEL_CELL_SEARCH_CNF",
    53569  : "TI_RRC_CSELPC_WAIT_CELL_RESEL_STOP_REQ",
    53570  : "TI_RRC_CSELPC_WAIT_CELL_RESEL_START_REQ",
    53571  : "TI_RRC_CSELPC_WAIT_CSEL_RESEL_START_CNF",
    53572  : "TI_RRC_CSELPC_WAIT_CSEL_RESEL_STOP_CNF",
    53573  : "TI_RRC_CSELPC_WAIT_STATE_CHANGE_REQ",
    53574  : "TI_RRC_CSELPC_WAIT_CSEL_STATE_CHANGE_CNF",
    53575  : "TI_RRC_CSELPC_WAIT_SIB_UPDATE_SYSINFO_CNF",
    53576  : "TI_RRC_CSELPC_WAIT_SIB_REL_CNF",
    53577  : "TI_RRC_CSELPC_WAIT_CSEL_SYS_INFO_CHANGE_CNF",
    53578  : "TI_RRC_CSELPC_WAIT_CMM_SYSINFO_CHANGE_CNF",
    53579  : "TI_LRRC_LCSELPC_WAIT_LPHY_SET_WORK_MODE_CNF",
    53580  : "TI_LRRC_LCSELPC_SS_WAIT_MBMS_FLOW_CMP",
    53581  : "TI_LRRC_LCSELPC_SS_WAIT_MBMS_MCCH_CFG_CNF",
    53582  : "TI_LRRC_LCSELPC_SS_WAIT_MBMS_MCCH_MSG_IND",
    53583  : "TI_LRRC_LCSELPC_SS_WAIT_MBMS_MCCH_RECFG_CNF",
    53584  : "TI_LRRC_LCSELPC_SS_WAIT_MBMS_L2_CFG_CNF",
    53585  : "TI_LRRC_LCSELPC_SS_WAIT_MBMS_PHY_CFG_CNF",
    53586  : "TI_LRRC_LCSELPC_SS_WAIT_MBMS_L2_REL_CNF",
    53587  : "TI_LRRC_LCSELPC_SS_WAIT_MBMS_PHY_REL_CNF",
    53588  : "TI_RRC_STATE_SMC_BOUNDARY_START",
    53589  : "TI_RRC_SMC_WAIT_CNF",
    53590  : "TI_RRC_STATE_CSEL_BOUNDARY_START",
    53591  : "TI_RRC_CSEL_WAIT_PHY_IND",
    53592  : "TI_RRC_CSEL_WAIT_PHY_CNF",
    53593  : "TI_RRC_CSEL_WAIT_SIB_CNF",
    53594  : "TI_RRC_CSEL_WAIT_GU_MEAS_CNF",
    53595  : "TI_RRC_CSEL_WAIT_TDS_MEAS_CNF",
    53596  : "TI_LRRC_LCSEL_WAIT_WRRC_BSIC_VERIFY_CNF",
    53597  : "TI_LRRC_LCSEL_WAIT_LPHY_BSIC_VERIFY_CNF",
    53598  : "TI_LRRC_LCSELPC_WAIT_LCSELBG_CNF",
    53599  : "TI_LRRC_LCSEL_WAIT_LCSELPC_CNF",
    53600  : "TI_LRRC_LCSELBG_WAIT_GURRC_CNF",
    53601  : "TI_LRRC_LCSELBG_WAIT_GURRC_IND",
    53602  : "TI_RRC_CSEL_WAIT_RSSI_SORT_IND",
    53603  : "TI_RRC_CSEL_WAIT_BGSRESEL_PREWORK_IND",
    53604  : "TI_RRC_CSEL_WAIT_BGSRESEL_SIBACQIRE_CNF",
    53605  : "TI_RRC_SIB_WAIT_RL_SETUP_CNF",
    53606  : "TI_RRC_SIB_WAIT_MIB_IND",
    53607  : "TI_RRC_SIB_WAIT_RL_REL_CNF",
    53608  : "TI_RRC_SIB_WAIT_SIB1_IND",
    53609  : "TI_RRC_SIB_WAIT_PHY_CNF",
    53610  : "TI_RRC_SIB_WAIT_SIB_IND",
    53611  : "TI_RRC_STATE_CMM_BOUNDARY_START",
    53612  : "TI_RRC_CMM_WAIT_PHY_CNF",
    53613  : "TI_LRRC_LCMM_WAIT_WRRC_BSIC_VERIFY_CNF",
    53614  : "TI_LRRC_LCMM_WAIT_LPHY_BSIC_VERIFY_CNF",
    53615  : "TI_RRC_CMM_WAIT_GU_MEAS_CNF",
    53616  : "TI_RRC_CMM_WAIT_UTRA_TDD_MEAS_CNF",
    53617  : "TI_RRC_ITF_WAIT_CNF_ERRC",
    53618  : "TI_RRC_STATE_ASN1_BOUNDARY_START",
    53619  : "TI_RRC_STATE_FSM_PROTECT_ERRC",
    53620  : "TI_RRC_STATE_FSM_PROTECT_CSEL",
    53621  : "TI_RRC_STATE_FSM_PROTECT_CMM",
    53622  : "TI_RRC_STATE_FSM_PROTECT_SIB",
    53623  : "TI_RRC_STATE_FSM_PROTECT_CSELBG",
    53624  : "TI_LRRC_LCSELBG_PROTECT_SLAVE_SUSPEND",
    53625  : "TI_RRC_APP_RSSI_REPORT",
    53626  : "TI_LRRC_LRRC_WAIT_CDMA_CNF",
    53627  : "TI_LRRC_LRRC_WAIT_CDMA_STOP_CNF",
    53628  : "TI_LRRC_WAIT_RRM_RADIO_RESOURCE_CNF",
    53629  : "TI_RRC_PTL_CONNESTFAIL_DELAY",
    53630  : "TI_LRRC_LRRC_WAIT_CONN_TO_IDLE_CNF",
    53631  : "TI_RRC_CSELPC_WAIT_CONN_TO_IDLE_REQ",
    53632  : "TI_LRRC_LRRC_WAIT_CAS_REL_ALL_CNF",
    53633  : "TI_LRRC_LRRC_WAIT_CAS_RESEL_CNF",
    53634  : "TI_LRRC_LRRC_WAIT_CAS_REDIRECT_CNF",
    53635  : "TI_RRC_CSEL_WAIT_CDMA_HRPD_MEAS_CNF",
    53636  : "TI_RRC_CMM_WAIT_HRPD_MEAS_CNF",
    53637  : "TI_LRRC_LCSELPC_SS_WAIT_MBMS_PHY_ENABLE_CNF",
    53638  : "TI_LRRC_LCSELPC_SS_WAIT_MBMS_PHY_DISABLE_CNF",
    53639  : "TI_LRRC_LCSELPC_SS_WAIT_MBMS_NOTIFY_CFG_CNF",
    53640  : "TI_LRRC_LCSELPC_SS_WAIT_MBMS_PMCH_CFG_CNF",
    53641  : "TI_LRRC_LCSELPC_SS_WAIT_MBMS_PMCH_ACTIVE_CNF",
    53642  : "TI_LRRC_LCMM_WAIT_LPP_LPHY_OTDOA_CNF",
    53643  : "TI_LRRC_LRRC_WAIT_LPP_LCMM_OTDOA_CNF",
    53644  : "TI_RRC_CSEL_WAIT_CSS_CURR_GEO_RSP",
    53645  : "TI_LRRC_LCMM_WAIT_LPHY_MBSFN_MEAS_CNF",
    53646  : "TI_RRC_WAIT_PDCP_HCODE_PROC_RSP",
    53647  : "TI_RRC_ITF_WAIT_CNF_CMM",
    53648  : "TI_RRC_ITF_WAIT_CNF_CSEL",
    53649  : "TI_RRC_ITF_WAIT_CNF_SIB",
    53650  : "TI_RRC_ITF_WAIT_CNF_CSELBG",
    53651  : "TI_RRC_STATE_BUTT",
}

Lrrc_flow_ctrl_flag_enum_table = {
    0  : "LRRC_FLOW_CTRL_TYPE_L2L_NORMAL",
    1  : "LRRC_FLOW_CTRL_TYPE_G2L_START_RESEL",
    2  : "LRRC_FLOW_CTRL_TYPE_G2L_RESEL_FAIL",
    3  : "LRRC_FLOW_CTRL_TYPE_G2L_STOP_RESEL",
    4  : "LRRC_FLOW_CTRL_TYPE_G2L_START_REDIR",
    5  : "LRRC_FLOW_CTRL_TYPE_G2L_REDIR_FAIL",
    6  : "LRRC_FLOW_CTRL_TYPE_G2L_STOP_REDIR",
    7  : "LRRC_FLOW_CTRL_TYPE_G2L_START_CCO",
    8  : "LRRC_FLOW_CTRL_TYPE_G2L_CCO_FAIL",
    9  : "LRRC_FLOW_CTRL_TYPE_G2L_STOP_CCO",
    10  : "LRRC_FLOW_CTRL_TYPE_G2L_START_HO",
    11  : "LRRC_FLOW_CTRL_TYPE_G2L_HO_FAIL",
    12  : "LRRC_FLOW_CTRL_TYPE_G2L_STOP_HO",
    13  : "LRRC_FLOW_CTRL_TYPE_W2L_START_RESEL",
    14  : "LRRC_FLOW_CTRL_TYPE_W2L_RESEL_FAIL",
    15  : "LRRC_FLOW_CTRL_TYPE_W2L_STOP_RESEL",
    16  : "LRRC_FLOW_CTRL_TYPE_W2L_START_REDIR",
    17  : "LRRC_FLOW_CTRL_TYPE_W2L_REDIR_FAIL",
    18  : "LRRC_FLOW_CTRL_TYPE_W2L_STOP_REDIR",
    19  : "LRRC_FLOW_CTRL_TYPE_W2L_START_HO",
    20  : "LRRC_FLOW_CTRL_TYPE_W2L_HO_FAIL",
    21  : "LRRC_FLOW_CTRL_TYPE_W2L_STOP_HO",
    22  : "LRRC_FLOW_CTRL_TYPE_W2L_START_PLMN",
    23  : "LRRC_FLOW_CTRL_TYPE_W2L_DONE_PLMN",
    24  : "LRRC_FLOW_CTRL_TYPE_W2L_STOP_PLMN",
    25  : "LRRC_FLOW_CTRL_TYPE_L2G_START_RESEL",
    26  : "LRRC_FLOW_CTRL_TYPE_L2G_RESEL_FAIL",
    27  : "LRRC_FLOW_CTRL_TYPE_L2G_START_REDIR",
    28  : "LRRC_FLOW_CTRL_TYPE_L2G_REDIR_FAIL",
    29  : "LRRC_FLOW_CTRL_TYPE_L2G_START_CCO",
    30  : "LRRC_FLOW_CTRL_TYPE_L2G_CCO_FAIL",
    31  : "LRRC_FLOW_CTRL_TYPE_L2G_START_HO",
    32  : "LRRC_FLOW_CTRL_TYPE_L2G_HO_FAIL",
    33  : "LRRC_FLOW_CTRL_TYPE_L2W_START_RESEL",
    34  : "LRRC_FLOW_CTRL_TYPE_L2W_RESEL_FAIL",
    35  : "LRRC_FLOW_CTRL_TYPE_L2W_START_REDIR",
    36  : "LRRC_FLOW_CTRL_TYPE_L2W_REDIR_FAIL",
    37  : "LRRC_FLOW_CTRL_TYPE_L2W_START_HO",
    38  : "LRRC_FLOW_CTRL_TYPE_L2W_HO_FAIL",
    39  : "LRRC_FLOW_CTRL_TYPE_G2L_IDLE_MEAS",
    40  : "LRRC_FLOW_CTRL_TYPE_W2L_IDLE_MEAS",
    41  : "LRRC_FLOW_CTRL_TYPE_G2L_CONN_MEAS",
    42  : "LRRC_FLOW_CTRL_TYPE_W2L_CONN_MEAS",
    43  : "LRRC_FLOW_CTRL_TYPE_W2L_RELALL",
    44  : "LRRC_FLOW_CTRL_TYPE_L2W_START_CELL_SRCH",
    45  : "LRRC_FLOW_CTRL_TYPE_L2W_STOP_CELL_SRCH",
    46  : "LRRC_FLOW_CTRL_TYPE_L2G_START_CELL_SRCH",
    47  : "LRRC_FLOW_CTRL_TYPE_L2G_STOP_CELL_SRCH",
    48  : "LRRC_FLOW_CTRL_TYPE_T2L_RELALL",
    49  : "LRRC_FLOW_CTRL_TYPE_G2L_RELALL",
    50  : "LRRC_FLOW_CTRL_TYPE_L2T_START_REDIR",
    51  : "LRRC_FLOW_CTRL_TYPE_L2T_START_HO",
    52  : "LRRC_FLOW_CTRL_TYPE_L2T_START_RESEL",
    53  : "LRRC_FLOW_CTRL_TYPE_T2L_IDLE_MEAS",
    54  : "LRRC_FLOW_CTRL_TYPE_T2L_CONN_MEAS",
    55  : "LRRC_FLOW_CTRL_TYPE_C2L_IDLE_MEAS",
    56  : "LRRC_FLOW_CTRL_TYPE_L2C_START_RESEL",
    57  : "LRRC_FLOW_CTRL_TYPE_L2C_RESEL_FAIL",
    58  : "LRRC_FLOW_CTRL_TYPE_L2C_START_REDIR",
    59  : "LRRC_FLOW_CTRL_TYPE_L2C_REDIR_FAIL",
    60  : "LRRC_FLOW_CTRL_TYPE_C2L_START_RESEL",
    61  : "LRRC_FLOW_CTRL_TYPE_C2L_RESEL_FAIL",
    62  : "LRRC_FLOW_CTRL_TYPE_C2L_STOP_RESEL",
    63  : "LRRC_FLOW_CTRL_TYPE_C2L_RELALL",
    64  : "LRRC_FLOW_CTRL_TYPE_BUTT",
}

Lrrc_rat_prio_enum_table = {
    0 : "LRRC_LNAS_RAT_PRIO_NULL",
    1 : "LRRC_LNAS_RAT_PRIO_LOW",
    2 : "LRRC_LNAS_RAT_PRIO_MIDDLE",
    3 : "LRRC_LNAS_RAT_PRIO_HIGH",
    4 : "LRRC_LNAS_RAT_PRIO_BUTT",
}

Lrrc_as_release_enum_table = {
    0 : "RRC_REL_AS_REL8",
    1 : "RRC_REL_AS_REL9",
    2 : "RRC_REL_AS_REL10",
    3 : "RRC_REL_AS_REL11",
    4 : "RRC_REL_AS_REL12",
    5 : "RRC_REL_AS_REL13",
}

Lrrc_protocol_state_enum_table = {
    0 : "RRC_PROTOCOL_IDLE",
    1 : "RRC_PROTOCOL_CONNECTED",
    2 : "RRC_PROTOCOL_STATE_BUTT",
}

Lrrc_utran_mode_enum_table = {
    0 : "LRRC_GUL_MODE",
    1 : "LRRC_GTL_MODE",
    2 : "LRRC_MODE_NULL",
    3 : "LRRC_MODE_BUTT",
}
def Tlps_Get_Lrrc_FsmId_Str(fsmid):
    for fsmid_index in Lrrc_fsm_id_enum_table.keys():
        if fsmid_index == fsmid:
            return Lrrc_fsm_id_enum_table[fsmid_index]

    return "unknown"

def Tlps_Get_Lrrc_MainState_Str(state):
    for index in lrrc_fsm_main_state_enum_table.keys():
        if index == state:
            return lrrc_fsm_main_state_enum_table[index]

    return "unknown"

def Tlps_Get_Lrrc_SubState_Str(state):
    for index in lrrc_fsm_substate_enum_table.keys():
        if index == state:
            return lrrc_fsm_substate_enum_table[index]

    return "unknown"

def Tlps_Get_Lrrc_StaTiId_Str(timerid):
    for index in lrrc_state_timer_enum_table.keys():
        if index == timerid:
            return lrrc_state_timer_enum_table[index]

    return "unknown"

def Tlps_Get_Lrrc_FlowCtrlFlg_Str(state):
    for index in Lrrc_flow_ctrl_flag_enum_table.keys():
        if index == state:
            return Lrrc_flow_ctrl_flag_enum_table[index]

    return "unknown"

def Lrrc_get_rat_prio_Str(state):
    for index in Lrrc_rat_prio_enum_table.keys():
        if index == state:
            return Lrrc_rat_prio_enum_table[index]

    return "unknown"

def Lrrc_get_as_release_Str(state):
    for index in Lrrc_as_release_enum_table.keys():
        if index == state:
            return Lrrc_as_release_enum_table[index]

    return "unknown"

def Lrrc_get_protocal_state_Str(state):
    for index in Lrrc_protocol_state_enum_table.keys():
        if index == state:
            return Lrrc_protocol_state_enum_table[index]

    return "unknown"

def Lrrc_get_utran_mode_Str(state):
    for index in Lrrc_utran_mode_enum_table.keys():
        if index == state:
            return Lrrc_utran_mode_enum_table[index]

    return "unknown"
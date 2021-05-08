#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list mmc mscc msg
modify  record  :   2016-01-22 create file
"""

lmm_nas_msg_enum_table = {
#PS_MSG_ID_MMC_TO_LMM_BASE = 0x1130
0x1131 : "ID_MMC_LMM_START_REQ",
0x1132 : "ID_MMC_LMM_STOP_REQ",
0x1133 : "ID_MMC_LMM_PLMN_SRCH_REQ",
0x1134 : "ID_MMC_LMM_STOP_PLMN_SRCH_REQ",
0x1135 : "ID_MMC_LMM_EPLMN_NOTIFY_REQ",
0x1136 : "ID_MMC_LMM_CELL_SELECTION_CTRL_REQ",
0x1137 : "ID_MMC_LMM_ACTION_RESULT_REQ",
0x1138 : "ID_MMC_LMM_REL_REQ",
0x1139 : "ID_MMC_LMM_SUSPEND_REQ",
0x113A : "ID_MMC_LMM_CSFB_REQ",
0x113B : "ID_MMC_LMM_SYS_CFG_REQ",
0x113C : "ID_MMC_LMM_USIM_STATUS_REQ",
0x113D : "ID_MMC_LMM_ATTACH_REQ",
0x113E : "ID_MMC_LMM_DETACH_REQ",
0x113F : "ID_MMC_LMM_RESUME_NOTIFY",
0x1140 : "ID_MMC_LMM_SUSPEND_RSP",
0x1141 : "ID_MMC_LMM_DISABLE_LTE_NOTIFY",
0x1142 : "ID_MMC_LMM_ENABLE_LTE_NOTIFY",
0x1143 : "ID_MMC_LMM_USER_PLMN_END_NOTIFY",
0x1144 : "ID_MMC_LMM_UE_OOC_STATUS_NOTIFY",
0x1145 : "ID_MMC_LMM_WCDMA_SYS_INFO_IND",
0x1146 : "ID_MMC_LMM_GSM_SYS_INFO_IND",
0x1147 : "ID_MMC_LMM_BG_PLMN_SEARCH_REQ",
0x1148 : "ID_MMC_LMM_STOP_BG_PLMN_SEARCH_REQ",
0x1149 : "ID_MMC_LMM_UTRAN_MODE_REQ",
0x114A : "ID_MMC_LMM_SUSPEND_REL_REQ",
0x114B : "ID_MMC_LMM_LTE_SYS_INFO_IND",
0x114C : "ID_MMC_LMM_OTHER_MODEM_INFO_NOTIFY",
0x114D : "ID_MMC_LMM_IMS_VOICE_CAP_CHANGE_NOTIFY",
0x114E : "ID_MMC_LMM_BEGIN_SESSION_NOTIFY",
0x114F : "ID_MMC_LMM_END_SESSION_NOTIFY",
0x1150 : "ID_MMC_LMM_CELL_SIGN_REPORT_NOTIFY",
0x1151 : "ID_MMC_LMM_VOICE_DOMAIN_CHANGE_IND",
0x1153 : "ID_MMC_LMM_CS_CONN_STATUS_NOTIFY",
0x1154 : "ID_MMC_LMM_BG_SEARCH_HRPD_REQ",
0x1155 : "ID_MMC_LMM_STOP_BG_SEARCH_HRPD_REQ",
0x1156 : "ID_MMC_LMM_CSG_WHITE_LIST_NOTIFY",
0x1157 : "ID_MMC_LMM_CSG_LIST_SEARCH_REQ",
0x1158 : "ID_MMC_LMM_CSG_BG_SEARCH_REQ",
0x1159 : "ID_MMC_LMM_CL_INTERSYS_START_NTF",
0x115A : "ID_MMC_LMM_NOT_BACK_LTE_CHR_NOTIFY",
0x115B : "ID_MMC_LMM_IMMEDIATE_REPORT_CURR_CELL_SIGN_NOTIFY",
0x115C : "ID_MMC_LMM_ACDC_APP_NOTIFY",
0x115D : "ID_MMC_LMM_EFNASCONFIG_SIM_INFO_NOTIFY",
#PS_MSG_ID_LMM_TO_MMC_BASE = 0x10B0
0x10B1 : "ID_LMM_MMC_START_CNF",
0x10B2 : "ID_LMM_MMC_STOP_CNF",
0x10B3 : "ID_LMM_MMC_PLMN_SRCH_CNF",
0x10B4 : "ID_LMM_MMC_STOP_PLMN_SRCH_CNF",
0x10B5 : "ID_LMM_MMC_AREA_LOST_IND",
0x10B6 : "ID_LMM_MMC_SYS_INFO_IND",
0x10B7 : "ID_LMM_MMC_EMM_INFO_IND",
0x10B8 : "ID_LMM_MMC_ERR_IND",
0x10B9 : "ID_LMM_MMC_EPS_SERVICE_IND",
0x10BA : "ID_LMM_MMC_SUSPEND_IND",
0x10BB : "ID_LMM_MMC_SUSPEND_CNF",
0x10BC : "ID_LMM_MMC_RESUME_IND",
0x10BD : "ID_LMM_MMC_STATUS_IND",
0x10BE : "ID_LMM_MMC_SYS_CFG_CNF",
0x10BF : "ID_LMM_MMC_USIM_STATUS_CNF",
0x10C0 : "ID_LMM_MMC_ATTACH_CNF",
0x10C1 : "ID_LMM_MMC_ATTACH_IND",
0x10C2 : "ID_LMM_MMC_DETACH_CNF",
0x10C3 : "ID_LMM_MMC_DETACH_IND",
0x10C4 : "ID_LMM_MMC_TAU_RESULT_IND",
0x10C5 : "ID_LMM_MMC_SERVICE_RESULT_IND",
0x10C6 : "ID_LMM_MMC_TIN_TYPE_IND",
0x10C9 : "ID_LMM_MMC_TIMER_STATE_NOTIFY",
0x10CA : "ID_LMM_MMC_BG_PLMN_SEARCH_CNF",
0x10CB : "ID_LMM_MMC_STOP_BG_PLMN_SEARCH_CNF",
0x10CC : "ID_LMM_MMC_NOT_CAMP_ON_IND",
0x10CD : "ID_LMM_MMC_UTRAN_MODE_CNF",
0x10CE : "ID_LMM_MMC_SUSPEND_REL_CNF",
0x10CF : "ID_LMM_MMC_EMC_PDP_STATUS_NOTIFY",
0x10D0 : "ID_LMM_MMC_SUSPEND_INFO_CHANGE_NOTIFY",
0x10D1 : "ID_LMM_MMC_INFO_CHANGE_NOTIFY",
0x10D2 : "ID_LMM_MMC_SIM_AUTH_FAIL_IND",
0x10D3 : "ID_LMM_MMC_SEARCHED_PLMN_INFO_IND",
0x10D4 : "ID_LMM_MMC_CELL_SIGN_REPORT_IND",
0x10D5 : "ID_LMM_MMC_T3402_LEN_NOTIFY",
0x10D6 : "ID_LMM_MMC_EUTRAN_NOT_ALLOW_NOTIFY",
0x10D7 : "ID_LMM_MMC_BG_SEARCH_HRPD_CNF",
0x10D8 : "ID_LMM_MMC_STOP_BG_SEARCH_HRPD_CNF",
0x10D9 : "ID_LMM_MMC_CSG_LIST_SEARCH_CNF",
0x10DA : "ID_LMM_MMC_CSG_BG_SEARCH_CNF",
0x10DB : "ID_LMM_MMC_CSG_ID_HOME_NODEB_NAME_IND",
0x10DC : "ID_LMM_MMC_PLMN_STATUS_IND",
0x10DD : "ID_LMM_MMC_ANYCELL_SEARCH_NOTIFY",
0x10DE : "ID_LMM_MMC_RRM_RADIO_RESOURCE_CHECK_IND",
#PS_MSG_ID_MM_TO_LMM_BASE = 0x1BB5
0x1BB6 : "ID_MM_LMM_CSFB_SERVICE_START_NOTIFY",
0x1BB7 : "ID_MM_LMM_CSFB_SERVICE_ABORT_NOTIFY",
0x1BB8 : "ID_MM_LMM_HO_SECU_INFO_REQ",
0x1BB9 : "ID_MM_LMM_SRVCC_STATUS_NOTIFY",
0x1BBA : "ID_MM_LMM_BEGIN_SESSION_NOTIFY",
0x1BBB : "ID_MM_LMM_END_SESSION_NOTIFY",
0x1BBC : "ID_MM_LMM_CSFB_SERVICE_FAIL_NOTIFY",
0x1BBD : "ID_MM_LMM_TIMER_STATE_NOTIFY",
#PS_MS_ID_LMM_TO_MM_BASE = 0x1BD5
0x1BD6 : "ID_LMM_MM_COMBINED_START_NOTIFY_REQ",
0x1BD7 : "ID_LMM_MM_CSFB_SERVICE_END_IND",
0x1BD8 : "ID_LMM_MM_CSFB_SERVICE_PAGING_IND",
0x1BD9 : "ID_LMM_MM_INFO_CHANGE_NOTIFY",
0x1BDA : "ID_LMM_MM_HO_SECU_INFO_CNF",
0x1BDB : "ID_LMM_MM_RRM_RADIO_RESOURCE_CHECK_IND",
#PS_MSG_ID_GMM_TO_LMM_BASE = 0x11F0
0x11F1 : "ID_GMM_LMM_RESEL_SECU_INFO_REQ",
0x11F2 : "ID_GMM_LMM_HO_SECU_INFO_REQ",
0x11F3 : "ID_GMM_LMM_INFO_CHANGE_NOTIFY_REQ",
0x11F4 : "ID_GMM_LMM_TIMER_STATE_NOTIFY",
0x11F5 : "ID_GMM_LMM_BEGIN_SESSION_NOTIFY",
0x11F6 : "ID_GMM_LMM_END_SESSION_NOTIFY",
0x11F7 : "ID_GMM_LMM_RAU_NOTIFY",
0x11F8 : "ID_GMM_LMM_TIN_PTMSI_NOTIFY",
#PS_MSG_ID_LMM_TO_GMM_BASE = 0x11D0
0x11D1 : "ID_LMM_GMM_RESEL_SECU_INFO_CNF",
0x11D2 : "ID_LMM_GMM_HO_SECU_INFO_CNF",
0x11D3 : "ID_LMM_GMM_INFO_CHANGE_NOTIFY",
0x11D4 : "ID_LMM_GMM_TIN_GUTI_NOTIFY",
0x11D5 : "ID_LMM_GMM_RRM_RADIO_RESOURCE_CHECK_IND",
0x2696 : "ID_REGM_LMM_ACTION_RESULT_REQ",
0x2697 : "ID_REGM_LMM_REL_REQ",
0x2698 : "ID_REGM_LMM_ATTACH_REQ",
0x2699 : "ID_REGM_LMM_DETACH_REQ",
0x269A : "ID_REGM_LMM_IMS_VOICE_CAP_CHANGE_NOTIFY",
0x269B : "ID_REGM_LMM_CS_CONN_STATUS_NOTIFY",
0x2656 : "ID_LMM_REGM_EMM_INFO_IND",
0x2657 : "ID_LMM_REGM_CONN_STATUS_IND",
0x2658 : "ID_LMM_REGM_ATTACH_CNF",
0x2659 : "ID_LMM_REGM_ATTACH_IND",
0x265A : "ID_LMM_REGM_DETACH_CNF",
0x265B : "ID_LMM_REGM_DETACH_IND",
0x265C : "ID_LMM_REGM_TAU_RESULT_IND",
0x265D : "ID_LMM_REGM_SERVICE_RESULT_IND",
0x265E : "ID_LMM_REGM_TIMER_STATE_NOTIFY",
0x265F : "ID_LMM_REGM_INFO_CHANGE_NOTIFY",
0x2660: "ID_LMM_REGM_SIM_AUTH_FAIL_IND",
}

def get_lmm_nas_msg_str( MsgId):
    for MsgIdIndex in lmm_nas_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return lmm_nas_msg_enum_table[MsgIdIndex]

    return "none"
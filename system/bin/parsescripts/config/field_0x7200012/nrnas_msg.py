#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list nrnas msg
modify  record  :   2019-05-14 create file
"""

aps_nrsm_msg_enum_table = {
0x0000 : "ID_APS_NRSM_DEVICE_TRIGGER_RSP",
0x0001 : "ID_APS_NRSM_PDU_SESSION_EST_REQ",
0x0002 : "ID_APS_NRSM_PDU_SESSION_MODIFY_REQ",
0x0003 : "ID_APS_NRSM_PDU_SESSION_RELEASE_REQ",
0x0004 : "ID_APS_NRSM_PDU_SESSION_LOCAL_RELEASE_NTF",
0x0005 : "ID_APS_NRSM_PDU_SESSION_INFO_UPDATE_NTF",
0x0006 : "ID_APS_NRSM_GET_SDF_PARA_RSP",
0x0007 : "ID_APS_NRSM_PDU_SESSION_ABORT_NTF",

0x0100 : "ID_NRSM_APS_DEVICE_TRIGGER_IND",
0x0101 : "ID_NRSM_APS_PDU_SESSION_EST_CNF",
0x0102 : "ID_NRSM_APS_PDU_SESSION_MODIFY_CNF",
0x0103 : "ID_NRSM_APS_PDU_SESSION_MODIFY_IND",
0x0104 : "ID_NRSM_APS_PDU_SESSION_RELEASE_CNF",
0x0105 : "ID_NRSM_APS_PDU_SESSION_RELEASE_IND",
0x0106 : "ID_NRSM_APS_LTE_HANDOVER_TO_NR_IND",
0x0107 : "ID_NRSM_APS_PDU_SESSION_SSM3_REEST_IND",
0x0108 : "ID_NRSM_APS_PDU_SESSION_SSM2_INFO_UPDATE_IND",
0x0109 : "ID_NRSM_APS_GET_SDF_PARA_IND",
0x010A : "ID_NRSM_APS_CLEAR_ALL_PDU_SESSION_IND",
}

def get_aps_nrsm_msg_str( MsgId):
    for MsgIdIndex in aps_nrsm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return aps_nrsm_msg_enum_table[MsgIdIndex]

    return "none"

nrsm_nrmm_msg_enum_table = {
0x0001 : "ID_NRSM_NRMM_EST_REQ",
0x0002 : "ID_NRSM_NRMM_DATA_REQ",
0x0003 : "ID_NRSM_NRMM_PDU_ACTIVATE_INFO_UPDATE_NTF",
0x0004 : "ID_NRSM_NRMM_BEGIN_SESSION_NTF",
0x0005 : "ID_NRSM_NRMM_END_SESSION_NTF",
0x0006 : "ID_NRSM_NRMM_PDN_ACTIVATE_INFO_UPDATE_NTF",
0x0007 : "ID_NRSM_NRMM_ABORT_NTF",

0x0101 : "ID_NRMM_NRSM_EST_CNF",
0x0102 : "ID_NRMM_NRSM_EST_IND",
0x0103 : "ID_NRMM_NRSM_REL_IND",
0x0104 : "ID_NRMM_NRSM_DATA_CNF",
0x0105 : "ID_NRMM_NRSM_DATA_IND",
0x0106 : "ID_NRMM_NRSM_RESUME_IND",
0x0107 : "ID_NRMM_NRSM_SUSPEND_IND",
0x0108 : "ID_NRMM_NRSM_PDU_SESSION_ID_UPDATE_IND",
0x0109 : "ID_NRMM_NRSM_START_IND",
0x010A : "ID_NRMM_NRSM_POWER_OFF_IND",
0x010B : "ID_NRMM_NRSM_RADIO_RESOURCE_CHECK_IND",
0x010C : "ID_NRMM_NRSM_NR_SYS_INFO_IND",
0x010D : "ID_NRMM_NRSM_PROCOTOL_VERSION_IND",
}

def get_nrsm_nrmm_msg_str( MsgId):
    for MsgIdIndex in nrsm_nrmm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrsm_nrmm_msg_enum_table[MsgIdIndex]

    return "none"
    
nrsm_sm_msg_enum_table = {
0x0001 : "ID_SM_NRSM_SYNC_PDP_INFO_IND",
0x0002 : "ID_SM_NRSM_CLEAR_ALL_PDU_SESSION_INFO_IND",

0x1001 : "ID_NRSM_SM_SYNC_PDU_SESSION_INFO_IND",
0x1002 : "ID_NRSM_SM_CLEAR_ALL_PDU_SESSION_INFO_IND",
}

def get_nrsm_sm_msg_str( MsgId):
    for MsgIdIndex in nrsm_sm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrsm_sm_msg_enum_table[MsgIdIndex]

    return "none"
    
nrsm_ehsm_msg_enum_table = {
0x0001 : "ID_EHSM_NRSM_SYNC_PDN_INFO_IND",
0x0002 : "ID_EHSM_NRSM_CLEAR_ALL_PDU_SESSION_INFO_IND",

0x1001 : "ID_NRSM_EHSM_SYNC_PDU_SESSION_INFO_IND",
0x1002 : "ID_NRSM_EHSM_CLEAR_ALL_PDU_SESSION_INFO_IND",
}

def get_nrsm_ehsm_msg_str( MsgId):
    for MsgIdIndex in nrsm_ehsm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrsm_ehsm_msg_enum_table[MsgIdIndex]

    return "none"
    
nrsm_esm_msg_enum_table = {
0x0001 : "ID_ESM_NRSM_SYNC_PDN_INFO_IND",
0x0002 : "ID_ESM_NRSM_NR_HANDOVER_TO_LTE_IND",
0x0003 : "ID_ESM_NRSM_CLEAR_ALL_PDU_SESSION_INFO_IND",
0x0004 : "ID_ESM_NRSM_MAP_FAIL_QOS_FLOW_INFO_IND",

0x1001 : "ID_NRSM_ESM_SYNC_PDU_SESSION_INFO_IND",
0x1002 : "ID_NRSM_ESM_LTE_HANDOVER_TO_NR_IND",
0x1003 : "ID_NRSM_ESM_MAP_FAIL_EPS_BEAR_INFO_IND",
0x1004 : "ID_NRSM_ESM_CLEAR_ALL_PDU_SESSION_INFO_IND",
}

def get_nrsm_esm_msg_str( MsgId):
    for MsgIdIndex in nrsm_esm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrsm_esm_msg_enum_table[MsgIdIndex]

    return "none"
    
nrsm_rrm_msg_enum_table = {
0x0008 : "ID_PS_RRM_REGISTER_IND",
0x0009 : "ID_PS_RRM_DEREGISTER_IND",

0x000a : "ID_RRM_PS_STATUS_IND",
}

def get_nrsm_rrm_msg_str( MsgId):
    for MsgIdIndex in nrsm_rrm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrsm_rrm_msg_enum_table[MsgIdIndex]

    return "none"
    
nreap_nrsm_msg_enum_table = {
0x0001 : "ID_NRNAS_EAP_AUTH_DATA_IND",
0x0003 : "ID_NRNAS_EAP_CLEAR_RES_IND",
0x0005 : "ID_NRNAS_EAP_PLMN_ID_IND",
0x0007 : "ID_NRNAS_EAP_CONFIG_IND",
0x0009 : "ID_NRNAS_EAP_IDENTITY_QUERY_CNF",

0x0002 : "ID_NRNAS_EAP_AUTH_RSLT_NTF",
0x0004 : "ID_NRNAS_EAP_ENTITY_ID_STATE_NTF",
0x0006 : "ID_NRNAS_EAP_KAUSF_NTF",
0x0008 : "ID_NRNAS_EAP_IDENTITY_QUERY_REQ",
}

def get_nreap_nrsm_msg_str( MsgId):
    for MsgIdIndex in nreap_nrsm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nreap_nrsm_msg_enum_table[MsgIdIndex]

    return "none"
    
nreap_nrmm_msg_enum_table = {
0x0001 : "ID_NRNAS_EAP_AUTH_DATA_IND",
0x0003 : "ID_NRNAS_EAP_CLEAR_RES_IND",
0x0005 : "ID_NRNAS_EAP_PLMN_ID_IND",
0x0007 : "ID_NRNAS_EAP_CONFIG_IND",
0x0009 : "ID_NRNAS_EAP_IDENTITY_QUERY_CNF",

0x0002 : "ID_NRNAS_EAP_AUTH_RSLT_NTF",
0x0004 : "ID_NRNAS_EAP_ENTITY_ID_STATE_NTF",
0x0006 : "ID_NRNAS_EAP_KAUSF_NTF",
0x0008 : "ID_NRNAS_EAP_IDENTITY_QUERY_REQ",
}

def get_nreap_nrmm_msg_str( MsgId):
    for MsgIdIndex in nreap_nrmm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nreap_nrmm_msg_enum_table[MsgIdIndex]

    return "none"
    
nrsm_nrsm_msg_enum_table = {
0x0100 : "ID_NAS_NRSM_PDU_SESSION_ESTING_RSLT_CNF",
0x0101 : "ID_NAS_NRSM_PDU_SESSION_RELEASE_RSLT_CNF",
0x0102 : "ID_NAS_NRSM_PDU_SESSION_AUTHENTICATE_RSLT_CNF",
0x0103 : "ID_NAS_NRSM_PDU_SESSION_ACTIVE_REQ",
0x0104 : "ID_NAS_NRSM_INTERSYS_RESUME_RSLT_CNF",
0x0105 : "ID_NAS_NRSM_PDU_SESSION_MODIFY_RSLT_CNF",
0x0106 : "ID_NAS_NRSM_PDU_SESSION_MODIFY_REQ",
0x0107 : "ID_NAS_NRSM_PDU_SESSION_RELEASE_REQ",
0x6000 : "ID_NRNAS_MNTN_LOG_READ_NV_INFO_IND",
0x8000 : "NAS_NRSM_LOG_FSM_INFO_IND",
0x8001 : "NAS_NRSM_LOG_BUFFER_MSG_INFO_IND",
0x8002 : "NAS_NRSM_LOG_PDU_SESSION_FORBIDDEN_LIST_INFO_IND",
0x8003 : "NAS_NRSM_LOG_THROT_SUBSCRIPTION_INFO_IND",
0x8004 : "NAS_NRSM_LOG_FOLLOW_ON_INFO_IND",
0x8005 : "NAS_NRSM_LOG_AIR_MSG_RETRANSMIT_STATUS_INFO_IND",
0x8006 : "NAS_NRSM_LOG_APS_LTE_HANDOVER_TO_NR_IND",
0x8007 : "NAS_NRSM_LOG_ESM_SYNC_PDU_SESSION_INFO_IND",
0x8008 : "NAS_NRSM_LOG_ESM_LTE_HANDOVER_TO_NR_IND",
}

def get_nrsm_nrsm_msg_str( MsgId):
    for MsgIdIndex in nrsm_nrsm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrsm_nrsm_msg_enum_table[MsgIdIndex]

    return "none"
    
timer_nrsm_msg_enum_table = {
0x00 : "TI_NAS_NRSM_T3580",
0x01 : "TI_NAS_NRSM_T3581",
0x02 : "TI_NAS_NRSM_T3582",
0x100 : "TI_NAS_NRSM_WAIT_NRMM_DATA_CNF",
0x101 : "TI_NAS_NRSM_WAIT_APS_PDU_SESSION_INFO_UPDATE_NTF",
0x102 : "TI_NAS_NRSM_RETRANSMIT_INTERVAL",
0x103 : "TI_NAS_NRSM_PROTOCOL_COMPLEMENT",
0x104 : "TI_NAS_NRSM_WAIT_AUTH_COMPLETE",
0x105 : "TI_NAS_NRSM_WAIT_APS_SDF_PARA_RSP",
0x106 : "TI_NAS_NRSM_WAIT_NRMM_EST_CNF",
}

def get_timer_nrsm_msg_str( MsgId):
    for MsgIdIndex in timer_nrsm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return timer_nrsm_msg_enum_table[MsgIdIndex]

    return "none"
    
nreap_nreap_msg_enum_table = {
0x6000 : "ID_NRNAS_MNTN_LOG_READ_NV_INFO_IND",
0x9000 : "NRNAS_EAP_LOG_PEER_STATE_INFO_IND",
0x9001 : "NRNAS_EAP_LOG_AKA_STATE_INFO_IND",
}

def get_nreap_nreap_msg_str( MsgId):
    for MsgIdIndex in nreap_nreap_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nreap_nreap_msg_enum_table[MsgIdIndex]

    return "none"
    
timer_nreap_msg_enum_table = {
0x00 : "TI_NRNAS_EAP_WAIT_NW_AUTH_RSLT",
0x01 : "TI_NRNAS_EAP_WAIT_USIMM_AUTH_CNF",
}

def get_timer_nreap_msg_str( MsgId):
    for MsgIdIndex in timer_nreap_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return timer_nreap_msg_enum_table[MsgIdIndex]

    return "none"
    
nreap_usimm_msg_enum_table = {
0x04 : "USIMM_AUTHENTICATION_REQ",
0x04 : "USIMM_AUTHENTICATION_CNF",
}

def get_nreap_usimm_msg_str( MsgId):
    for MsgIdIndex in nreap_usimm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nreap_usimm_msg_enum_table[MsgIdIndex]

    return "none"

nrmm_mmc_msg_enum_table = {
0x01 : "ID_NRMM_MMC_START_CNF",
0x03 : "ID_NRMM_MMC_POWER_OFF_CNF",
0x05 : "ID_NRMM_MMC_SPEC_PLMN_SRCH_CNF",
0x07 : "ID_NRMM_MMC_STOP_PLMN_SRCH_CNF",
0x09 : "ID_NRMM_MMC_SUSPEND_CNF",
0x0B : "ID_NRMM_MMC_SYS_INFO_IND",
0x0D : "ID_NRMM_MMC_ANYCELL_PLMN_SRCH_CNF",
0x0F : "ID_NRMM_MMC_AREA_LOST_IND",
0x11 : "ID_NRMM_MMC_SYS_CFG_CNF",
0x13 : "ID_NRMM_MMC_SEARCHED_PLMN_INFO_IND",
0x15 : "ID_NRMM_MMC_SUSPEND_IND",
0x17 : "ID_NRMM_MMC_RESUME_IND",
0x19 : "ID_NRMM_MMC_CELL_SIGN_RPT_IND",
0x1B : "ID_NRMM_MMC_PLMN_LIST_SRCH_CNF",
0x1D : "ID_NRMM_MMC_RADIO_RESOURCE_CHECK_IND",
0x1F : "ID_NRMM_MMC_SOR_INFO_UPDATE_IND",
0x21 : "ID_NRMM_MMC_NET_SCAN_CNF",
0x23 : "ID_NRMM_MMC_NET_SCAN_STOP_CNF",


0x00 : "ID_MMC_NRMM_START_REQ",
0x02 : "ID_MMC_NRMM_POWER_OFF_REQ",
0x04 : "ID_MMC_NRMM_SPEC_PLMN_SRCH_REQ",
0x06 : "ID_MMC_NRMM_STOP_PLMN_SRCH_REQ",
0x08 : "ID_MMC_NRMM_SUSPEND_REQ",
0x0A : "ID_MMC_NRMM_NR_SYS_INFO_NTF",
0x0C : "ID_MMC_NRMM_EPLMN_CFG_NTF",
0x0E : "ID_MMC_NRMM_ANYCELL_PLMN_SRCH_REQ",
0x10 : "ID_MMC_NRMM_PARALLEL_SRCH_START_NTF",
0x12 : "ID_MMC_NRMM_PARALLEL_SRCH_END_NTF",
0x14 : "ID_MMC_NRMM_SYS_CFG_REQ",
0x16 : "ID_MMC_NRMM_DISABLE_LTE_NTF",
0x18 : "ID_MMC_NRMM_ENABLE_LTE_NTF",
0x1A : "ID_MMC_NRMM_CELL_SELECTION_CTRL_NTF",
0x1C : "ID_MMC_NRMM_OOC_STATE_NTF",
0x1E : "ID_MMC_NRMM_HPLMN_INFO_NTF",
0x20 : "ID_MMC_NRMM_USER_SPEC_PLMN_START_NTF",
0x22 : "ID_MMC_NRMM_USER_SPEC_PLMN_END_NTF",
0x24 : "ID_MMC_NRMM_DISABLE_NR_NTF",
0x26 : "ID_MMC_NRMM_ENABLE_NR_NTF",
0x28 : "ID_MMC_NRMM_SUSPEND_REL_NTF",
0x2A : "ID_MMC_NRMM_SUSPEND_RSP",
0x2C : "ID_MMC_NRMM_CELL_SIGN_RPT_NTF",
0x2E : "ID_MMC_NRMM_RESUME_NTF",
0x30 : "ID_MMC_NRMM_PLMN_LIST_SRCH_REQ",
0x32 : "ID_MMC_NRMM_BEGIN_SESSION_NTF",
0x34 : "ID_MMC_NRMM_END_SESSION_NTF",
0x36 : "ID_MMC_NRMM_NET_SCAN_REQ",
0x38 : "ID_MMC_NRMM_NET_SCAN_STOP_REQ"
}

def nrmm_mmc_msg_str( MsgId):
    for MsgIdIndex in nrmm_mmc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrmm_mmc_msg_enum_table[MsgIdIndex]

    return "none"
    
nrmm_regm_msg_enum_table = {
0x01 : "ID_NRMM_REGM_REG_RSLT_IND",
0x03 : "ID_NRMM_REGM_CONN_STATUS_IND",
0x05 : "ID_NRMM_REGM_DEREG_RSLT_IND",
0x07 : "ID_NRMM_REGM_REG_CNF",
0x09 : "ID_NRMM_REGM_DEREG_CNF",
0x0B : "ID_NRMM_REGM_SRV_REJ_IND",
0x0D : "ID_NRMM_REGM_MM_INFO_IND",
0x0F : "ID_NRMM_REGM_NSSAI_CHANGE_IND",
0x11 : "ID_NRMM_REGM_SMS_OVER_NAS_AVAIL_IND",

0x00 : "ID_REGM_NRMM_REG_REQ",
0x02 : "ID_REGM_NRMM_DEREG_REQ",
0x4 : "ID_REGM_NRMM_REL_CONN_NTF",
0x06 : "ID_REGM_NRMM_LMM_REG_INFO_NTF",
0x08 : "ID_REGM_NRMM_GU_REG_INFO_NTF"
}

def nrmm_regm_msg_str( MsgId):
    for MsgIdIndex in nrmm_regm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrmm_regm_msg_enum_table[MsgIdIndex]

    return "none"
    
nrmm_nrmm_msg_enum_table = {
0x00 : "ID_NRMM_INTER_PWR_REG_POWER_ON_NTF",
0x01 : "ID_NRMM_INTER_PWR_REG_POWER_OFF_REQ",
0x02 : "ID_NRMM_INTER_REG_PWR_POWER_OFF_CNF",
0x1000 : "ID_NRMM_INTER_NWS_REG_NETWORK_SEARCH_NTF",
0x1001 : "ID_NRMM_INTER_NWS_REG_CON_REL_REQ",
0x1002 : "ID_NRMM_INTER_REG_NWS_CON_REL_CNF",
0x1004 : "ID_NRMM_INTER_NWS_REG_CAP_CHANGE_NTF",
0x2000 : "ID_NRMM_INTER_REG_SEC_POWER_ON_NTF",
0x2001 : "ID_NRMM_INTER_REG_SEC_POWER_OFF_NTF",
0x2002 : "ID_NRMM_INTER_REG_SEC_DEREG_INITIATE_NTF",
0x2003 : "ID_NRMM_INTER_REG_SEC_REG_INITIATE_NTF",
0x2004 : "ID_NRMM_INTER_SEC_REG_CON_EST_CNF",
0x2005 : "ID_NRMM_INTER_REG_SEC_CON_REL_REQ",
0x2006 : "ID_NRMM_INTER_SEC_REG_CON_REL_IND",
0x2007 : "ID_NRMM_INTER_SEC_REG_REG_REINITIATE_IND",
0x2008 : "ID_NRMM_INTER_SEC_REG_AUTH_REJ_IND",
0x2009 : "ID_NRMM_INTER_SEC_REG_AUTH_FAILURE_IND",
0x200A : "ID_NRMM_INTER_SEC_REG_DATA_CNF",
0x200B : "ID_NRMM_INTER_SEC_REG_CON_EST_IND",
0x200C : "ID_NRMM_INTER_REG_SEC_SUSPEND_NTF",
0x200D : "ID_NRMM_INTER_REG_SEC_RESUME_NTF",
0x200E : "ID_NRMM_INTER_REG_SEC_LTE_NSC_NTF",
0x200F : "ID_NRMM_INTER_SEC_REG_STOP_T3540_IND",
0x2010 : "ID_NRMM_INTER_REG_SEC_DELETE_SEC_CTX_NTF",
0x2011 : "ID_NRMM_INTER_SEC_REG_FALLBACK_IND",
0x2012 : "ID_NRMM_INTER_REG_SEC_REG_COMPLETE_NTF",
0x3000 : "ID_NRMM_INTER_AMF_REG_REGISTRATION_ACCEPT",
0x3001 : "ID_NRMM_INTER_AMF_REG_REGISTRATION_REJECT",
0x3002 : "ID_NRMM_INTER_AMF_REG_DEREG_REQ",
0x3003 : "ID_NRMM_INTER_AMF_REG_DEREG_ACC",
0x3004 : "ID_NRMM_INTER_AMF_REG_CONFIG_UPDATE_COMMAND",
0x4000 : "ID_NRMM_INTER_AMF_SEC_IDENTITY_REQUEST",
0x4001 : "ID_NRMM_INTER_AMF_SEC_AUTHENTICATION_REQUEST",
0x4002 : "ID_NRMM_INTER_AMF_SEC_AUTHENTICATION_REJECT",
0x4003 : "ID_NRMM_INTER_AMF_SEC_SECURITY_MODE_COMMAND",
0x4004 : "ID_NRMM_INTER_AMF_SEC_AUTHENTICATION_RESULT",
0x5000 : "ID_NRMM_INTER_AMF_CM_SERVICE_ACCEPT",
0x5001 : "ID_NRMM_INTER_AMF_CM_SERVICE_REJECT",
0x5002 : "ID_NRMM_INTER_AMF_CM_DL_NAS_TRANSPORT",
0x6000 : "ID_NRMM_INTER_REG_CM_REG_IND",
0x6001 : "ID_NRMM_INTER_REG_CM_DEREG_IND",
0x6002 : "ID_NRMM_INTER_CM_REG_SRV_INIT_NTF",
0x6003 : "ID_NRMM_INTER_CM_REG_SRV_END_NTF",
0x6004 : "ID_NRMM_INTER_REG_CM_SRV_SUSPEND_IND",
0x6005 : "ID_NRMM_INTER_REG_CM_SRV_RESUME_IND",
0x6006 : "ID_NRMM_INTER_REG_CM_POWER_OFF_IND",
0x6007 : "ID_NRMM_INTER_REG_CM_POWER_ON_IND",
0x6008 : "ID_NRMM_INTER_REG_CM_SRV_ABORT_IND",
0x6009 : "ID_NRMM_INTER_REG_CM_RAT_SUSPEND_IND",
0x600A : "ID_NRMM_INTER_REG_CM_RAT_RESUME_IND",
0x600B : "ID_NRMM_INTER_CM_REG_REGISTRATION_NTF",
0x600C : "ID_NRMM_INTER_CM_REG_DRB_ACTIVE_NTF",
0x600D : "ID_NRMM_INTER_CM_REG_STOP_T3540_NTF",
0x600E : "ID_NRMM_INTER_REG_CM_PDU_STATUS_IND",
0x7000 : "ID_NRMM_INTER_CM_SEC_SRV_REQ_STATE_NTF",
0x7001 : "ID_NRMM_INTER_SEC_CM_CON_EST_CNF",
0x7002 : "ID_NRMM_INTER_SEC_CM_CON_REL_IND",
0x7003 : "ID_NRMM_INTER_SEC_CM_SRV_REINITIATE_IND",
0x7004 : "ID_NRMM_INTER_SEC_CM_DATA_CNF",
0x7005 : "ID_NRMM_INTER_SEC_CM_AUTH_REJ_IND",
0x7006 : "ID_NRMM_INTER_SEC_CM_AUTH_FAILURE_IND",
0x7007 : "ID_NRMM_INTER_SEC_CM_FALLBACK_IND",
0x8000 : "ID_NRMM_INTER_IW_REG_SUSPEND_NTF",
0x8001 : "ID_NRMM_INTER_IW_REG_RESUME_NTF",
0x8002 : "ID_NRMM_INTER_IW_REG_CON_REL_REQ",
0x8003 : "ID_NRMM_INTER_REG_IW_CON_REL_CNF",
0x9000 : "ID_NRMM_INTER_PWR_IW_POWER_OFF_NTF",
0xA000 : "NAS_NRMM_OM_LOG_REG_FSM_INFO_IND",
0xA001 : "NAS_NRMM_OM_LOG_CM_FSM_INFO_IND",
0xA002 : "NAS_NRMM_OM_LOG_IW_FSM_INFO_IND",
0xA003 : "NAS_NRMM_OM_LOG_NWS_FSM_INFO_IND",
0xA004 : "NAS_NRMM_OM_LOG_PWR_FSM_INFO_IND",
0xA005 : "NAS_NRMM_OM_LOG_SEC_FSM_INFO_IND",
0xA006 : "NAS_NRMM_OM_LOG_NAS_MSG_STREAMING_IND",
0xA007 : "NAS_NRMM_OM_LOG_ECIPHER_INFO_IND",
0xA008 : "NAS_NRMM_OM_LOG_NV_READ_INFO_IND",
0xA009 : "NAS_NRMM_OM_LOG_NV_WRITE_INFO_IND",
0xA00A : "NAS_NRMM_OM_LOG_AIR_ENCODE_IE_IND",
0xA00B : "NAS_NRMM_OM_LOG_ALLOWED_NSSAI_IND",
0xA00C : "NAS_NRMM_OM_LOG_CONFIGURED_NSSAI_IND",
0xA00D : "NAS_NRMM_OM_LOG_REJECTED_NSSAI_IND",
0xA00E : "NAS_NRMM_OM_LOG_AIR_DECODE_IE_IND",
0xA00F : "NAS_NRMM_OM_LOG_DL_NAS_CONTAINER_IND",
0xA010 : "NAS_NRMM_OM_LOG_SUCI_CIPHER_INFO_IND",
0xB000 : "ID_NRMM_INTER_REG_REG_SYS_INFO_NTF"
}

def nrmm_nrmm_msg_str( MsgId):
    for MsgIdIndex in nrmm_nrmm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrmm_nrmm_msg_enum_table[MsgIdIndex]

    return "none"
    
nrmm_timer_msg_enum_table = {
0x00 : "TI_NAS_NRMM_T3502",
0x01 : "TI_NAS_NRMM_T3510",
0x02 : "TI_NAS_NRMM_T3511",
0x03 : "TI_NAS_NRMM_T3512",
0x04 : "TI_NAS_NRMM_T3516",
0x05 : "TI_NAS_NRMM_T3517",
0x06 : "TI_NAS_NRMM_T3519",
0x07 : "TI_NAS_NRMM_T3520",
0x08 : "TI_NAS_NRMM_T3521",
0x09 : "TI_NAS_NRMM_T3540",
0x0a : "TI_NAS_NRMM_T3525",
0x0b : "TI_NAS_NRMM_POWER_OFF_PROTECT",
0x0c : "TI_NAS_NRMM_ERASE_FORBIDDEN_TAI_LIST",
0x1000 : "TI_NAS_NRMM_WAIT_AS_EST_CNF",
0x1001 : "TI_NAS_NRMM_WAIT_AS_POWER_ON_CNF",
0x1002 : "TI_NAS_NRMM_WAIT_AS_POWER_OFF_CNF",
0x1003 : "TI_NAS_NRMM_WAIT_AUTH_CNF",
0x1004 : "TI_NAS_NRMM_WAIT_SYS_INFO_NTF",
0x1005 : "TI_NAS_NRMM_WAIT_USIM_READ_CNF",
0x1006 : "TI_NAS_NRMM_USER_DEREG",
0x1007 : "TI_NAS_NRMM_WAIT_PAGING_RSP"
}

def nrmm_timer_msg_str( MsgId):
    for MsgIdIndex in nrmm_timer_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrmm_timer_msg_enum_table[MsgIdIndex]

    return "none"
    
nrmm_nrrc_msg_enum_table = {
0x00 : "ID_NRMM_NRRC_START_REQ",
0x02 : "ID_NRMM_NRRC_POWER_OFF_REQ",
0x04 : "ID_NRMM_NRRC_PARALLEL_PLMN_SRCH_START_NTF",
0x05 : "ID_NRMM_NRRC_PARALLEL_PLMN_SRCH_END_NTF",
0x06 : "ID_NRMM_NRRC_ANYCELL_PLMN_SRCH_REQ",
0x08 : "ID_NRMM_NRRC_SPEC_PLMN_SRCH_REQ",
0x0A : "ID_NRMM_NRRC_PLMN_LIST_SRCH_REQ",
0x0C : "ID_NRMM_NRRC_GEO_PLMN_SRCH_REQ",
0x0E : "ID_NRMM_NRRC_STOP_PLMN_SRCH_REQ",
0x10 : "ID_NRMM_NRRC_BG_PLMN_SRCH_REQ",
0x12 : "ID_NRMM_NRRC_STOP_BG_PLMN_SRCH_REQ",
0x14 : "ID_NRMM_NRRC_SUSPEND_REQ",
0x19 : "ID_NRMM_NRRC_CELL_SIGN_RPT_NTF",
0x1B : "ID_NRMM_NRRC_IMMEDIATE_RPT_CELL_SIGN_NTF",
0x1C : "ID_NRMM_NRRC_CELL_SELECTION_CTRL_NTF",
0x1D : "ID_NRMM_NRRC_OOC_STATE_NTF",
0x1F : "ID_NRMM_NRRC_SUSPEND_REL_NTF",
0x21 : "ID_NRMM_NRRC_UTRAN_MODE_REQ",
0x24 : "ID_NRMM_NRRC_SUSPEND_RSP",
0x26 : "ID_NRMM_NRRC_RESUME_RSP",
0x27 : "ID_NRMM_NRRC_DRX_INFO_NTF",
0x28 : "ID_NRMM_NRRC_EPLMN_CFG_NTF",
0x29 : "ID_NRMM_NRRC_USIM_STATUS_NTF",
0x2A : "ID_NRMM_NRRC_CLEAR_BUFF_NTF",
0x2B : "ID_NRMM_NRRC_DETACH_NTF",
0x2C : "ID_NRMM_NRRC_DISABLE_NR_NTF",
0x2D : "ID_NRMM_NRRC_SEC_PARA_NTF",
0x2F : "ID_NRMM_NRRC_SEC_PARA_RSP",
0x31 : "ID_NRMM_NRRC_EST_REQ",
0x33 : "ID_NRMM_NRRC_REL_REQ",
0x36 : "ID_NRMM_NRRC_DATA_REQ",
0x39 : "ID_NRMM_NRRC_SYS_CFG_REQ",
0x3D : "ID_NRMM_NRRC_SESSION_BEGIN_NTF",
0x3E : "ID_NRMM_NRRC_SESSION_END_NTF",
0x40 : "ID_NRMM_NRRC_DISABLE_LTE_NTF",
0x41 : "ID_NRMM_NRRC_ENABLE_LTE_NTF",
0x43 : "ID_NRMM_NRRC_HPLMN_INFO_NTF",
0x44 : "ID_NRMM_NRRC_FORB_TA_LIST_CHANGE_NTF",
0x45 : "ID_NRMM_NRRC_NG_5G_S_TMSI_CHANGE_NTF",
0x48 : "ID_NRMM_NRRC_NET_SCAN_REQ",
0x4A : "ID_NRMM_NRRC_NET_SCAN_STOP_REQ",
0x4C : "ID_NRMM_NRRC_ENABLE_NR_NTF",
0x4D : "ID_NRMM_NRRC_ACCESS_CLASS_NTF",
0x4F : "ID_NRMM_NRRC_RNA_UPDATE_RSP",
0x50 : "ID_NRMM_NRRC_CONNECT_RESUME_REQ",

0x00000001 : "ID_NRRC_NRMM_START_CNF",
0x00000003 : "ID_NRRC_NRMM_POWER_OFF_CNF",
0x00000007 : "ID_NRRC_NRMM_ANYCELL_PLMN_SRCH_CNF",
0x00000009 : "ID_NRRC_NRMM_SPEC_PLMN_SRCH_CNF",
0x0000000B : "ID_NRRC_NRMM_PLMN_LIST_SRCH_CNF",
0x0000000D : "ID_NRRC_NRMM_GEO_PLMN_SRCH_CNF",
0x0000000F : "ID_NRRC_NRMM_STOP_PLMN_SRCH_CNF",
0x00000011 : "ID_NRRC_NRMM_BG_PLMN_SRCH_CNF",
0x00000013 : "ID_NRRC_NRMM_STOP_BG_PLMN_SRCH_CNF",
0x00000015 : "ID_NRRC_NRMM_SUSPEND_CNF",
0x00000016 : "ID_NRRC_NRMM_SEARCHED_PLMN_INFO_IND",
0x00000017 : "ID_NRRC_NRMM_AREA_LOST_IND",
0x00000018 : "ID_NRRC_NRMM_SYS_INFO_IND",
0x0000001A : "ID_NRRC_NRMM_CELL_SIGN_REPORT_IND",
0x0000001E : "ID_NRRC_NRMM_PAGING_IND",
0x00000020 : "ID_NRRC_NRMM_SUSPEND_REL_CNF",
0x00000022 : "ID_NRRC_NRMM_UTRAN_MODE_CNF",
0x00000023 : "ID_NRRC_NRMM_SUSPEND_IND",
0x00000025 : "ID_NRRC_NRMM_RESUME_IND",
0x0000002E : "ID_NRRC_NRMM_SEC_PARA_IND",
0x0000002F : "ID_NRMM_NRRC_SEC_PARA_RSP",
0x00000030 : "ID_NRRC_NRMM_UE_CAP_CHANGE_IND",
0x00000032 : "ID_NRRC_NRMM_EST_CNF",
0x00000034 : "ID_NRRC_NRMM_REL_CNF",
0x00000035 : "ID_NRRC_NRMM_REL_IND",
0x00000037 : "ID_NRRC_NRMM_DATA_CNF",
0x00000038 : "ID_NRRC_NRMM_DATA_IND",
0x0000003A : "ID_NRRC_NRMM_SYS_CFG_CNF",
0x0000003B : "ID_NRRC_NRMM_ACCESS_GRANT_IND",
0x0000003C : "ID_NRRC_NRMM_INACTIVE_STATE_IND",
0x0000003F : "ID_NRRC_NRMM_FALLBACK_IND",
0x00000042 : "ID_NRRC_NRMM_HO_FAILURE_IND",
0x00000046 : "ID_NRRC_NRMM_RADIO_RESOURCE_CHECK_IND",
0x00000047 : "ID_NRRC_NRMM_RF_SHORT_OCCUPY_IND",
0x00000049 : "ID_NRRC_NRMM_NET_SCAN_CNF",
0x0000004B : "ID_NRRC_NRMM_NET_SCAN_STOP_CNF",
0x0000004E : "ID_NRRC_NRMM_RNA_UPDATE_IND",
0x00000051 : "ID_NRRC_NRMM_CONNECT_RESUME_CNF"
}

def nrmm_nrrc_msg_str( MsgId):
    for MsgIdIndex in nrmm_nrrc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrmm_nrrc_msg_enum_table[MsgIdIndex]

    return "none"

    
nrmm_sdap_msg_enum_table = {
0x00 : "ID_SDAP_NRMM_SRV_EST_REQ",
0x01 : "ID_NRMM_SDAP_SRV_EST_CNF",
0x02 : "ID_NRMM_SDAP_SRV_EST_NTF",
0x03 : "ID_SDAP_NRMM_PDU_SESSION_WITH_DRB_INFO_IND",
0x04 : "ID_SDAP_NRMM_SRV_RESUME_REQ",
0x05 : "ID_NRMM_SDAP_SRV_RESUME_CNF"
}

def nrmm_sdap_msg_str( MsgId):
    for MsgIdIndex in nrmm_sdap_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrmm_sdap_msg_enum_table[MsgIdIndex]

    return "none"

nrmm_usim_msg_enum_table = {
0x4 : "USIMM_AUTHENTICATION_REQ",
0x6 : "USIMM_UPDATEFILE_REQ",
0x7 : "USIMM_READFILE_REQ",
0x2000 : "NAS_LOG_USIMM_API_SET_FILE_REQ",
0x2001 : "NAS_LOG_USIMM_API_GET_FILE_REQ"
}

def nrmm_usim_msg_str( MsgId):
    for MsgIdIndex in nrmm_usim_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrmm_usim_msg_enum_table[MsgIdIndex]

    return "none"
    
nrmm_pcf_msg_enum_table = {
0x01 : "ID_PCF_NRMM_DATA_REQ",
0x02 : "ID_NRMM_PCF_DATA_CNF",
0x03 : "ID_NRMM_PCF_DATA_IND",
0x04 : "ID_NRMM_PCF_START_IND",
0x05 : "ID_NRMM_PCF_LADN_UPDATE_IND",
0x06 : "ID_NRMM_PCF_NSSAI_UPDATE_IND"
}

def nrmm_pcf_msg_str( MsgId):
    for MsgIdIndex in nrmm_pcf_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrmm_pcf_msg_enum_table[MsgIdIndex]

    return "none"
    
nrmm_imsa_msg_enum_table = {
0x00 : "ID_NRMM_IMSA_INITIAL_REG_BEGIN_IND",
0x01 : "ID_NRMM_IMSA_SRV_EST_CNF",
0x02 : "ID_NRMM_IMSA_EMFB_SR_CNF",
0x20 : "ID_IMSA_NRMM_SRV_EST_REQ",
0x21 : "ID_IMSA_NRMM_EMFB_SR_REQ"
}

def nrmm_imsa_msg_str( MsgId):
    for MsgIdIndex in nrmm_imsa_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrmm_imsa_msg_enum_table[MsgIdIndex]

    return "none"

nrmm_lmm_msg_enum_table = {
0x00 : "ID_NRMM_LMM_INTERSYS_LTE_INFO_REQ",
0x01 : "ID_LMM_NRMM_INTERSYS_LTE_INFO_CNF",
0x02 : "ID_LMM_NRMM_NR_SECU_PARA_INFO_REQ",
0x03 : "ID_NRMM_LMM_NR_SECU_PARA_INFO_CNF",
0x04 : "ID_NRMM_LMM_UPLINK_COUNT_UPDATE_NTF",
0x05 : "ID_LMM_NRMM_UPLINK_COUNT_UPDATE_NTF"
}

def nrmm_lmm_msg_str( MsgId):
    for MsgIdIndex in nrmm_lmm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrmm_lmm_msg_enum_table[MsgIdIndex]

    return "none"
    
nrmm_sms_msg_enum_table = {
0x01 : "ID_SMS_NRMM_EST_REQ",
0x02 : "ID_SMS_NRMM_DATA_REQ",
0x03 : "ID_SMS_NRMM_BEGIN_SESSION_NOTIFY",
0x04 : "ID_SMS_NRMM_END_SESSION_NOTIFY",

0x101 : "ID_NRMM_SMS_EST_CNF",
0x102 : "ID_NRMM_SMS_DATA_IND",
0x103 : "ID_NRMM_SMS_ERR_IND",
0x104 : "ID_NRMM_SMS_RADIO_RESOURCE_CHECK_IND"
}

def nrmm_sms_msg_str( MsgId):
    for MsgIdIndex in nrmm_sms_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrmm_sms_msg_enum_table[MsgIdIndex]

    return "none"
    
nrmm_mta_msg_enum_table = {
0x0801 : "ID_NRNAS_MTA_GET_NRMM_CHR_STATS_INFO_CNF",
0x0701 : "ID_MTA_NRNAS_GET_NRMM_CHR_STATS_INFO_REQ"
}

def nrmm_mta_msg_str( MsgId):
    for MsgIdIndex in nrmm_mta_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrmm_mta_msg_enum_table[MsgIdIndex]

    return "none"
    
nrmm_diag_app_msg_enum_table = {
20001 : "ID_OM_NAS_GET_NRMM_UE_INFO_REQ",
20002 : "ID_NAS_OM_GET_NRMM_UE_INFO_CNF",
20003 : "ID_NAS_OM_NRMM_UE_INFO_IND",
20004 : "ID_OM_NAS_GET_NRMM_NW_INFO_REQ",
20005 : "ID_NAS_OM_GET_NRMM_NW_INFO_CNF",
20006 : "ID_NAS_OM_NRMM_NW_INFO_IND"
}

def nrmm_diag_app_msg_str( MsgId):
    for MsgIdIndex in nrmm_diag_app_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrmm_diag_app_msg_enum_table[MsgIdIndex]

    return "none"
    
nrmm_mtc_msg_enum_table = {
0x0701 : "ID_NRMM_MTC_BEGIN_SESSION_NOTIFY",
0x0702 : "ID_NRMM_MTC_END_SESSION_NOTIFY"
}

def nrmm_mtc_msg_str( MsgId):
    for MsgIdIndex in nrmm_mtc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrmm_mtc_msg_enum_table[MsgIdIndex]

    return "none"
    
nrmm_chr_om_msg_enum_table = {
0x9003 : "ID_OM_ERR_LOG_REPORT_CNF",
0x9009 : "ID_OM_FAULT_ERR_LOG_IND"
}

def nrmm_chr_om_msg_str( MsgId):
    for MsgIdIndex in nrmm_chr_om_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrmm_chr_om_msg_enum_table[MsgIdIndex]

    return "none"
    
nrmm_mma_msg_enum_table = {
0x100 : "ID_NRMM_MMA_MLOG_EVENT_NTF"
}

def nrmm_mma_msg_str( MsgId):
    for MsgIdIndex in nrmm_mma_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrmm_mma_msg_enum_table[MsgIdIndex]

    return "none"
    
nrmm_rrm_msg_enum_table = {
0x0008 : "ID_PS_RRM_REGISTER_IND",
0x0009 : "ID_PS_RRM_DEREGISTER_IND"
}

def nrmm_rrm_msg_str( MsgId):
    for MsgIdIndex in nrmm_rrm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrmm_rrm_msg_enum_table[MsgIdIndex]

    return "none"
    
nrmm_tc_msg_enum_table = {
0x01 : "ID_NRMM_TC_DATA_IND"
}

def nrmm_tc_msg_str( MsgId):
    for MsgIdIndex in nrmm_tc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrmm_tc_msg_enum_table[MsgIdIndex]
    return "none"
            
nrmm_si_stk_msg_enum_table = {
0x1d : "ID_NAS_STK_NETWORK_REJECTION_EVENT"
}

def nrmm_si_stk_msg_str( MsgId):
    for MsgIdIndex in nrmm_si_stk_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return nrmm_si_stk_msg_enum_table[MsgIdIndex]

    return "none"
    
pcf_dsm_msg_enum_table = {
0x01 : "ID_PCF_DSM_URSP_UPDATE_IND",
0x02 : "ID_PCF_DSM_LADN_UPDATE_IND",
0x03 : "ID_PCF_DSM_NSSAI_UPDATE_IND",
0x04 : "ID_PCF_DSM_UE_POLICY_IND"
}

def pcf_dsm_msg_str( MsgId):
    for MsgIdIndex in pcf_dsm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return pcf_dsm_msg_enum_table[MsgIdIndex]

    return "none"

def nrnas_get_msgid_str(pid1, pid2, MsgId):
    if (( 'taf' == pid1.lower() and 'nrsm' == pid2.lower()) or ( 'nrsm' == pid1.lower() and 'taf' == pid2.lower())):
        return get_aps_nrsm_msg_str( MsgId)
    elif (( 'nrmm' == pid1.lower() and 'nrsm' == pid2.lower()) or ( 'nrsm' == pid1.lower() and 'nrmm' == pid2.lower())):
        return get_nrsm_nrmm_msg_str( MsgId)
    elif (( 'sm' == pid1.lower() and 'nrsm' == pid2.lower()) or ( 'nrsm' == pid1.lower() and 'sm' == pid2.lower())):
        return get_nrsm_sm_msg_str( MsgId)
    elif (( 'ehsm' == pid1.lower() and 'nrsm' == pid2.lower()) or ( 'nrsm' == pid1.lower() and 'ehsm' == pid2.lower())):
        return get_nrsm_ehsm_msg_str( MsgId)
    elif (( 'esm' == pid1.lower() and 'nrsm' == pid2.lower()) or ( 'nrsm' == pid1.lower() and 'esm' == pid2.lower())):
        return get_nrsm_esm_msg_str( MsgId)
    elif (( 'rrm' == pid1.lower() and 'nrsm' == pid2.lower()) or ( 'nrsm' == pid1.lower() and 'rrm' == pid2.lower())):
        return get_nrsm_rrm_msg_str( MsgId)
    elif (( 'nreap' == pid1.lower() and 'nrsm' == pid2.lower()) or ( 'nrsm' == pid1.lower() and 'nreap' == pid2.lower())):
        return get_nreap_nrsm_msg_str( MsgId)
    elif (( 'nreap' == pid1.lower() and 'nrmm' == pid2.lower()) or ( 'nrmm' == pid1.lower() and 'nreap' == pid2.lower())):
        return get_nreap_nrmm_msg_str( MsgId)
    elif (( 'nrsm' == pid1.lower() and 'nrsm' == pid2.lower()) or ( 'nrsm' == pid1.lower() and 'nrsm' == pid2.lower())):
        return get_nrsm_nrsm_msg_str( MsgId)
    elif (( 'timer' == pid1.lower() and 'nrsm' == pid2.lower()) or ( 'nrsm' == pid1.lower() and 'timer' == pid2.lower())):
        return get_timer_nrsm_msg_str( MsgId)
    elif (( 'nreap' == pid1.lower() and 'nreap' == pid2.lower()) or ( 'nreap' == pid1.lower() and 'nreap' == pid2.lower())):
        return get_nreap_nreap_msg_str( MsgId)
    elif (( 'timer' == pid1.lower() and 'nreap' == pid2.lower()) or ( 'nreap' == pid1.lower() and 'timer' == pid2.lower())):
        return get_timer_nreap_msg_str( MsgId)
    elif (( 'nreap' == pid1.lower() and 'usim' == pid2.lower()) or ( 'usim' == pid1.lower() and 'nreap' == pid2.lower())):
        return get_nreap_usimm_msg_str( MsgId)
    elif (( 'nreap' == pid1.lower() and 'i1_usim' == pid2.lower()) or ( 'i1_usim' == pid1.lower() and 'nreap' == pid2.lower())):
        return get_nreap_usimm_msg_str( MsgId)
    elif (( 'nreap' == pid1.lower() and 'i2_usim' == pid2.lower()) or ( 'i2_usim' == pid1.lower() and 'nreap' == pid2.lower())):
        return get_nreap_usimm_msg_str( MsgId)
    elif (( 'nrmm' == pid1.lower() and 'mmc' == pid2.lower()) or ( 'mmc' == pid1.lower() and 'nrmm' == pid2.lower())):
        return nrmm_mmc_msg_str( MsgId)
    elif (( 'nrmm' == pid1.lower() and 'regm' == pid2.lower()) or ( 'regm' == pid1.lower() and 'nrmm' == pid2.lower())):
        return nrmm_regm_msg_str( MsgId)
    elif (( 'imsa' == pid1.lower() and 'nrmm' == pid2.lower()) or ( 'nrmm' == pid1.lower() and 'imsa' == pid2.lower())):
        return nrmm_imsa_msg_str( MsgId)
    elif (( 'nrmm' == pid1.lower() and 'timer' == pid2.lower()) or ( 'timer' == pid1.lower() and 'nrmm' == pid2.lower())):
        return nrmm_timer_msg_str( MsgId)
    elif (( 'nrmm' == pid1.lower() and 'nrrc' == pid2.lower()) or ( 'nrrc' == pid1.lower() and 'nrmm' == pid2.lower())):
        return nrmm_nrrc_msg_str( MsgId)
    elif (( 'nrmm' == pid1.lower() and 'sdap_ul' == pid2.lower()) or ( 'sdap_ul' == pid1.lower() and 'nrmm' == pid2.lower())):
        return nrmm_sdap_msg_str( MsgId)
    elif (( 'usim' == pid1.lower() and 'nrmm' == pid2.lower()) or ( 'nrmm' == pid1.lower() and 'usim' == pid2.lower())):
        return nrmm_usim_msg_str( MsgId)
    elif (( 'i1_usim' == pid1.lower() and 'nrmm' == pid2.lower()) or ( 'nrmm' == pid1.lower() and 'i1_usim' == pid2.lower())):
        return nrmm_usim_msg_str( MsgId)
    elif (( 'i2_usim' == pid1.lower() and 'nrmm' == pid2.lower()) or ( 'nrmm' == pid1.lower() and 'i2_usim' == pid2.lower())):
        return nrmm_usim_msg_str( MsgId)
    elif (( 'pcf' == pid1.lower() and 'nrmm' == pid2.lower()) or ( 'nrmm' == pid1.lower() and 'pcf' == pid2.lower())):
        return nrmm_pcf_msg_str( MsgId)
    elif ( 'nrmm' == pid1.lower() and 'nrmm' == pid2.lower()):
        return nrmm_nrmm_msg_str( MsgId)
    elif (( 'lmm' == pid1.lower() and 'nrmm' == pid2.lower()) or ( 'nrmm' == pid1.lower() and 'lmm' == pid2.lower())):
        return nrmm_lmm_msg_str( MsgId)
    elif (( 'sms' == pid1.lower() and 'nrmm' == pid2.lower()) or ( 'nrmm' == pid1.lower() and 'sms' == pid2.lower())):
        return nrmm_sms_msg_str( MsgId)
    elif (( 'mta' == pid1.lower() and 'nrmm' == pid2.lower()) or ( 'nrmm' == pid1.lower() and 'mta' == pid2.lower())):
        return nrmm_mta_msg_str( MsgId)
    elif (( 'mtc' == pid1.lower() and 'nrmm' == pid2.lower()) or ( 'nrmm' == pid1.lower() and 'mtc' == pid2.lower())):
        return nrmm_mtc_msg_str( MsgId)
    elif (( 'mma' == pid1.lower() and 'nrmm' == pid2.lower()) or ( 'nrmm' == pid1.lower() and 'mma' == pid2.lower())):
        return nrmm_mma_msg_str( MsgId)
    elif (( 'rrm' == pid1.lower() and 'nrmm' == pid2.lower()) or ( 'nrmm' == pid1.lower() and 'rrm' == pid2.lower())):
        return nrmm_rrm_msg_str( MsgId)
    elif (( 'tc' == pid1.lower() and 'nrmm' == pid2.lower()) or ( 'nrmm' == pid1.lower() and 'tc' == pid2.lower())):
        return nrmm_tc_msg_str( MsgId)
    elif (( 'si_stk' == pid1.lower() and 'nrmm' == pid2.lower()) or ( 'nrmm' == pid1.lower() and 'si_stk' == pid2.lower())):
        return nrmm_si_stk_msg_str( MsgId)
    elif (( 'pcf' == pid1.lower() and 'dsm' == pid2.lower()) or ( 'dsm' == pid1.lower() and 'pcf' == pid2.lower())):
        return pcf_dsm_msg_str( MsgId)
    else:
        return 'none'
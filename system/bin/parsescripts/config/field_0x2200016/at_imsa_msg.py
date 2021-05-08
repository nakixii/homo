#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list at imsa msg
modify  record  :   2019-05-24 create file
"""

at_imsa_msg_enum_table = {
0x0001 : "ID_AT_IMSA_CIREG_SET_REQ",
0x0002 : "ID_AT_IMSA_CIREG_QRY_REQ",
0x0003 : "ID_AT_IMSA_CIREP_SET_REQ",
0x0004 : "ID_AT_IMSA_CIREP_QRY_REQ",
0x0005 : "ID_AT_IMSA_VOLTEIMPU_QRY_REQ",
0x0006 : "ID_AT_IMSA_IMS_REG_DOMAIN_QRY_REQ",
0x0007 : "ID_AT_IMSA_IMS_CTRL_MSG",
0x0008 : "ID_AT_IMSA_CALL_ENCRYPT_SET_REQ",
0x0009 : "ID_AT_IMSA_ROAMING_IMS_QRY_REQ",
0x000A : "ID_AT_IMSA_PCSCF_SET_REQ",
0x000B : "ID_AT_IMSA_PCSCF_QRY_REQ",
0x000C : "ID_AT_IMSA_DMDYN_SET_REQ",
0x000D : "ID_AT_IMSA_DMDYN_QRY_REQ",
0x000E : "ID_AT_IMSA_IMSTIMER_SET_REQ",
0x000F : "ID_AT_IMSA_IMSTIMER_QRY_REQ",
0x0010 : "ID_AT_IMSA_SMSPSI_SET_REQ",
0x0011 : "ID_AT_IMSA_SMSPSI_QRY_REQ",
0x0012 : "ID_AT_IMSA_DMUSER_QRY_REQ",
0x0013 : "ID_AT_IMSA_NICKNAME_SET_REQ",
0x0014 : "ID_AT_IMSA_NICKNAME_QRY_REQ",
0x0015 : "ID_AT_IMSA_BATTERYINFO_SET_REQ",
0x0016 : "ID_AT_IMSA_VOLTEREG_NTF",
0x0017 : "ID_AT_IMSA_CANCEL_ADD_VIDEO_REQ",
0x0018 : "ID_AT_IMSA_VOLTEIMPI_QRY_REQ",
0x0019 : "ID_AT_IMSA_VOLTEDOMAIN_QRY_REQ",
0x001A : "ID_AT_IMSA_REGERR_REPORT_SET_REQ",
0x001B : "ID_AT_IMSA_REGERR_REPORT_QRY_REQ",
0x001C : "ID_AT_IMSA_IMS_IP_CAP_SET_REQ",
0x001D : "ID_AT_IMSA_IMS_IP_CAP_QRY_REQ",
0x001E : "ID_AT_IMSA_IMS_SRV_STAT_RPT_SET_REQ",
0x001F : "ID_AT_IMSA_IMS_SRV_STAT_RPT_QRY_REQ",
0x0020 : "ID_AT_IMSA_IMS_SERVICE_STATUS_QRY_REQ",
0x0021 : "ID_AT_IMSA_EMERGENCY_AID_SET_REQ",
0x0022 : "ID_AT_IMSA_DM_RCS_CFG_SET_REQ",
0x0023 : "ID_AT_IMSA_USER_AGENT_CFG_SET_REQ",
0x0024 : "ID_AT_IMSA_VICECFG_SET_REQ",
0x0025 : "ID_AT_IMSA_VICECFG_QRY_REQ",
0x0026 : "ID_AT_IMSA_RTTCFG_SET_REQ",
0x0027 : "ID_AT_IMSA_RTT_MODIFY_SET_REQ",
0x0028 : "ID_AT_IMSA_TRANSPORT_TYPE_SET_REQ",
0x0029 : "ID_AT_IMSA_TRANSPORT_TYPE_QRY_REQ",
0x1001 : "ID_IMSA_AT_CIREG_SET_CNF",
0x1002 : "ID_IMSA_AT_CIREG_QRY_CNF",
0x1003 : "ID_IMSA_AT_CIREP_SET_CNF",
0x1004 : "ID_IMSA_AT_CIREP_QRY_CNF",
0x1005 : "ID_IMSA_AT_VOLTEIMPU_QRY_CNF",
0x1006 : "ID_IMSA_AT_CIREGU_IND",
0x1007 : "ID_IMSA_AT_CIREPH_IND",
0x1008 : "ID_IMSA_AT_CIREPI_IND",
0x1009 : "ID_IMSA_AT_VT_PDP_ACTIVATE_IND",
0x100A : "ID_IMSA_AT_VT_PDP_DEACTIVATE_IND",
0x100B : "ID_IMSA_AT_MT_STATES_IND",
0x100C : "ID_IMSA_AT_IMS_REG_DOMAIN_QRY_CNF",
0x100D : "ID_IMSA_AT_IMS_CTRL_MSG",
0x100E : "ID_IMSA_AT_CALL_ENCRYPT_SET_CNF",
0x100F : "ID_IMSA_AT_ROAMING_IMS_QRY_CNF",
0x1010 : "ID_IMSA_AT_IMS_RAT_HANDOVER_IND",
0x1011 : "ID_IMSA_AT_IMS_SRV_STATUS_UPDATE_IND",
0x1012 : "ID_IMSA_AT_PCSCF_SET_CNF",
0x1013 : "ID_IMSA_AT_PCSCF_QRY_CNF",
0x1014 : "ID_IMSA_AT_DMDYN_SET_CNF",
0x1015 : "ID_IMSA_AT_DMDYN_QRY_CNF",
0x1016 : "ID_IMSA_AT_DMCN_IND",
0x1017 : "ID_IMSA_AT_IMSTIMER_SET_CNF",
0x1018 : "ID_IMSA_AT_IMSTIMER_QRY_CNF",
0x1019 : "ID_IMSA_AT_SMSPSI_SET_CNF",
0x101A : "ID_IMSA_AT_SMSPSI_QRY_CNF",
0x101B : "ID_IMSA_AT_DMUSER_QRY_CNF",
0x101C : "ID_IMSA_AT_NICKNAME_SET_CNF",
0x101D : "ID_IMSA_AT_NICKNAME_QRY_CNF",
0x101E : "ID_IMSA_AT_REGFAIL_IND",
0x101F : "ID_IMSA_AT_BATTERYINFO_SET_CNF",
0x1020 : "ID_IMSA_AT_CANCEL_ADD_VIDEO_CNF",
0x1021 : "ID_IMSA_AT_VOLTEIMPI_QRY_CNF",
0x1022 : "ID_IMSA_AT_VOLTEDOMAIN_QRY_CNF",
0x1023 : "ID_IMSA_AT_REGERR_REPORT_SET_CNF",
0x1024 : "ID_IMSA_AT_REGERR_REPORT_QRY_CNF",
0x1025 : "ID_IMSA_AT_REGERR_REPORT_IND",
0x1026 : "ID_IMSA_AT_IMS_IP_CAP_SET_CNF",
0x1027 : "ID_IMSA_AT_IMS_IP_CAP_QRY_CNF",
0x1028 : "ID_IMSA_AT_EMC_PDN_ACTIVATE_IND",
0x1029 : "ID_IMSA_AT_EMC_PDN_DEACTIVATE_IND",
0x102A : "ID_IMSA_AT_IMS_SRV_STAT_RPT_SET_CNF",
0x102B : "ID_IMSA_AT_IMS_SRV_STAT_RPT_QRY_CNF",
0x102C : "ID_IMSA_AT_IMS_SERVICE_STATUS_QRY_CNF",
0x102D : "ID_IMSA_AT_EMERGENCY_AID_SET_CNF",
0x102E : "ID_IMSA_AT_CALL_ALT_SRV_IND",
0x102F : "ID_IMSA_AT_DM_RCS_CFG_SET_CNF",
0x1030 : "ID_IMSA_AT_USER_AGENT_CFG_SET_CNF",
0x1031 : "ID_IMSA_AT_IMPU_TYPE_IND",
0x1032 : "ID_IMSA_AT_VICECFG_SET_CNF",
0x1033 : "ID_IMSA_AT_VICECFG_QRY_CNF",
0x1034 : "ID_IMSA_AT_DIALOG_NOTIFY",
0x1035 : "ID_IMSA_AT_RTTCFG_SET_CNF",
0x1036 : "ID_IMSA_AT_RTT_MODIFY_SET_CNF",
0x1037 : "ID_IMSA_AT_RTT_EVENT_IND",
0x1038 : "ID_IMSA_AT_RTT_ERROR_IND",
0x1039 : "ID_IMSA_AT_TRANSPORT_TYPE_SET_CNF",
0x103A : "ID_IMSA_AT_TRANSPORT_TYPE_QRY_CNF",
}

def get_at_imsa_msg_str( MsgId):
    for MsgIdIndex in at_imsa_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return at_imsa_msg_enum_table[MsgIdIndex]

    return "none"
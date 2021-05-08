#!/usr/bin/env python3
# coding=utf-8
"""
功能：list pid list
版权信息：华为技术有限公司，版权所有（C）2010-2019
修改记录：2016-07-08  创建
"""

import string

Rrc_Phy_Msg_Id_enum_table = {
   0x1001 : "ID_RRC_PHY_RL_SETUP_REQ",
   0x1002 : "ID_RRC_PHY_RL_MODIFY_REQ",
   0x1003 : "ID_RRC_PHY_RL_RELEASE_REQ",
   0x1004 : "ID_RRC_PHY_POWER_CONTROL_REQ",
   0x1005 : "ID_RRC_PHY_TRCH_CONFIG_REQ",
   0x1006 : "UPHY_APM_CODEC_HR_ID",
   0x1007: "UPHY_APM_CODEC_HR_ID",
   0x1008: "UPHY_APM_CODEC_HR_ID",
   0x1009: "UPHY_APM_CODEC_HR_ID",
   0x1010: "UPHY_APM_CODEC_HR_ID",
   0x1011: "UPHY_APM_CODEC_HR_ID",
   0x1012: "UPHY_APM_CODEC_HR_ID",
   0x1013: "UPHY_APM_CODEC_HR_ID",
   0x1014: "UPHY_APM_CODEC_HR_ID",
   0x1015: "UPHY_APM_CODEC_HR_ID",
   0x1016: "UPHY_APM_CODEC_HR_ID",
   0x1017: "UPHY_APM_CODEC_HR_ID",
   0x1018: "UPHY_APM_CODEC_HR_ID",
   0x1019: "UPHY_APM_CODEC_HR_ID",
   0x1020: "UPHY_APM_CODEC_HR_ID",
   0x1021: "UPHY_APM_CODEC_HR_ID",
   0x1022: "UPHY_APM_CODEC_HR_ID",
   0x1023: "UPHY_APM_CODEC_HR_ID",
   0x1024: "UPHY_APM_CODEC_HR_ID",
   0x1025: "UPHY_APM_CODEC_HR_ID",
   0x1026: "UPHY_APM_CODEC_HR_ID",
   0x1027: "UPHY_APM_CODEC_HR_ID",
   0x1028: "UPHY_APM_CODEC_HR_ID",
   0x1029: "UPHY_APM_CODEC_HR_ID",
   0x1030: "UPHY_APM_CODEC_HR_ID",
   0x1031: "UPHY_APM_CODEC_HR_ID",
   0x1032: "UPHY_APM_CODEC_HR_ID",
   0x1033: "UPHY_APM_CODEC_HR_ID",
   0x1034: "UPHY_APM_CODEC_HR_ID",
   0x1035: "UPHY_APM_CODEC_HR_ID",
   0x1036: "UPHY_APM_CODEC_HR_ID",
   0x1037: "UPHY_APM_CODEC_HR_ID",

}


def Uphy_Get_Apm_Module_Id(ucIdx):
    if ucIdx in uphy_apm_module_id_enum_table:
        strRlt = uphy_apm_module_id_enum_table[ucIdx]
    else:
        strRlt = "UPHY_APM_MODULE_ID_BUTT"
    return strRlt
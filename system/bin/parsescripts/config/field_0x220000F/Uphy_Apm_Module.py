#!/usr/bin/env python3
# coding=utf-8
"""
功能：apm模块
版权信息：华为技术有限公司，版权所有（C）2010-2019
修改记录：2016-07-08  创建
"""

import string

uphy_apm_module_id_enum_table = {
    0   : "UPHY_APM_GSM_ID",
    1   : "UPHY_APM_WCDMA_ID",
    2  : "UPHY_APM_CODEC_AMR_ID",
    3  : "UPHY_APM_CODEC_EFR_ID",
    4  : "UPHY_APM_CODEC_FR_ID",
    5  : "UPHY_APM_CODEC_HR_ID",
}

uphy_oam_work_mode_enum_table = {
    0   : "UCOM_WORK_MODE_SIG",
    1   : "UCOM_WORK_MODE_NON_SIG",
}

uphy_oam_business_enum_table = {
    0   : "UCOM_OAM_BUSINESS_TYPE_NORMAL",
    1   : "UCOM_OAM_BUSINESS_TYPE_CT",
    2   : "UCOM_OAM_BUSINESS_TYPE_NO_SIG_BT",
    3   : "UCOM_OAM_BUSINESS_TYPE_SIG_BT",
}

uphy_bool_enum_table = {
    0   : "UPHY_FALSE",
    1   : "UPHY_TRUE",
}

def Uphy_Get_Apm_Module_Id(ucIdx):
    if ucIdx in uphy_apm_module_id_enum_table:
        strRlt = uphy_apm_module_id_enum_table[ucIdx]
    else:
        strRlt = "UPHY_APM_MODULE_ID_BUTT"
    return strRlt


def Uphy_Get_Oam_Work_Mode(ucIdx):
    if ucIdx in uphy_oam_work_mode_enum_table:
        strRlt = uphy_oam_work_mode_enum_table[ucIdx]
    else:
        strRlt = "UCOM_WORK_MODE_BUTT"
    return strRlt

def Uphy_Get_Oam_Business_Type(ucIdx):
    if ucIdx in uphy_oam_business_enum_table:
        strRlt = uphy_oam_business_enum_table[ucIdx]
    else:
        strRlt = "UCOM_OAM_BUSINESS_TYPE_BUTT"
    return strRlt

def Uphy_Get_Bool_Business_Type(ucIdx):
    if ucIdx in uphy_bool_enum_table:
        strRlt = uphy_bool_enum_table[ucIdx]
    else:
        strRlt = "UPHY_BUTT"
    return strRlt
#!/usr/bin/env python3
# coding=utf-8
"""
功能：获取制式类型
版权信息：华为技术有限公司，版权所有（C）2010-2019
修改记录：2016-07-08  创建
"""

import string

platform_rat_type_enum_table = {
    0   : "PLATFORM_RAT_GSM",
    1   : "PLATFORM_RAT_WCDMA",
    2  : "PLATFORM_RAT_LTE",
    3  : "PLATFORM_RAT_TDS",
    4  : "PLATFORM_RAT_1X",
    5  : "PLATFORM_RAT_HRPD",
    6  : "PLATFORM_RAT_NR",
}

def UPHY_GetRatType(ucIdx, maxRatNum):
    if ucIdx in platform_rat_type_enum_table and ucIdx < maxRatNum:
        strRlt = platform_rat_type_enum_table[ucIdx]
    else:
        strRlt = "PLATFORM_RAT_BUTT"
    return strRlt

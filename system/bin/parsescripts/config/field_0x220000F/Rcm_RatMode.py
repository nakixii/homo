#!/usr/bin/env python3
# coding=utf-8
"""
功能：获取RCM制式类型
版权信息：华为技术有限公司，版权所有（C）2020-2029
修改记录：2020-06-08 马辉  创建
"""

import string

rcm_rat_mode_enum_table = {
    0   : "RCM_G0",
    1   : "RCM_G1",
    2   : "RCM_G2",
    3   : "RCM_MODE_ID_BUTT",
    4   : "RCM_W0",
    5   : "RCM_W1",
    6   : "RCM_MODE_ID_BUTT",
    7   : "RCM_MODE_ID_BUTT",
    8   : "RCM_LTE0",
    9   : "RCM_LTE1",
    10   : "RCM_MODE_ID_BUTT",
    11   : "RCM_LTEV",
    12   : "RCM_MODE_ID_BUTT",
    13   : "RCM_MODE_ID_BUTT",
    14   : "RCM_MODE_ID_BUTT",
    15   : "RCM_MODE_ID_BUTT",
    16   : "RCM_MODE_ID_BUTT",
    17   : "RCM_MODE_ID_BUTT",
    18   : "RCM_MODE_ID_BUTT",
    19   : "RCM_1X",
    20   : "RCM_HRPD0",
    21   : "RCM_HRPD1",
    22   : "RCM_MODE_ID_BUTT",
    23   : "RCM_MODE_ID_BUTT",
    24   : "RCM_NR",
    25   : "RCM_MODE_ID_BUTT",
    26   : "RCM_MODE_ID_BUTT",
    27   : "RCM_MODE_ID_BUTT",
    28   : "RCM_MODE_ID_BUTT",
    29   : "RCM_MODE_ID_BUTT",
    30   : "RCM_MODE_ID_BUTT",
    31   : "RCM_MODE_ID_BUTT",
}

def RCM_GetRatMode(rptMode):
    strRlt = "RCM_MODE_ID_BUTT"
    for i in range(0,32) :
        if rptMode >> i & 1 == 1:
            strRlt = rcm_rat_mode_enum_table[i]
            break
    return strRlt

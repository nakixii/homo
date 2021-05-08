#!/usr/bin/env python3
# coding=utf-8
"""
功能：list pid list
版权信息：华为技术有限公司，版权所有（C）2010-2019
修改记录：2016-07-08  创建
"""
import string

cttf_pid_enum_table = {
    1   : "TIMER",
    49  : "CPROC_RM",
    50  : "1XRLAC",
    51  : "1XRMAC",
    52  : "1XRRLP",
    53  : "1XRTESTSO",
    54  : "1XFTESTSO",
    55  : "1XFLAC",
    56  : "1XFMAC",
    57  : "1XFRLP",
    58  : "HRPDRSLP",
    59  : "HRPDRPA",
    60  : "HRPDRSPS",
    61  : "HRPDRMAC",
    62  : "HRPDFSLP",
    63  : "HRPDFPA",
    64  : "HRPDFSPS",
    65  : "HRPDFMAC",
    66  : "HRPDSIG",
    67  : "PPPC",
    68  : "HRPD_CM",
    69  : "HRPD_SM",
    70  : "DSP_PROCSTUB",
    71  : "CPROC_1XCM",
    72  : "CPROC_1XSM",
    73  : "CPROC_1XDSP",
    74  : "PLUM",
    75  : "1XCASM",
    76  : "1XCMEAS",
    77  : "1XCSRCH",
    78  : "HALMP",
    79  : "HRUP",
    80  : "HSCP",
    81  : "HSP",
    82  : "XREG",
    83  : "XSD",
    84  : "XCC",
    85  : "HSD",
    86  : "HLU",
    87  : "HSM",
    88  : "EHSM",
    89  : "XSMS",
    90  : "XPDS",
    124 : "SHPA",
    101 : "USIM",
    201 : "APM",
    208 : "IDLE",
    225 : "RRM",
    228 : "RCM",
    249 : "1XCTAS",
    251 : "CBT",
}

def CTTF_GetPidStr(ucPid):
    if ucPid in cttf_pid_enum_table:
        strPid = cttf_pid_enum_table[ucPid]
    else:    
        strPid = "none"
    return strPid
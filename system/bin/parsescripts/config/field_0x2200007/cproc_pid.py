#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list pid list
modify  record  :   2016-03-10 create file
"""

import string

cproc_pid_enum_table = {
    1   : "TIMER",
    2   : "VOICE",
    4   : "CSDR_1XCM", #csdr -> cproc
    5   : "CSDR_1XSM", #csdr -> cproc
    6   : "CSDR_HRPDCM", #csdr -> cproc
    7   : "CSDR_HRPDSM", #csdr -> cproc
    28  : "OM",
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
    229 : "DSP_PID_STARTUP",
    249 : "1XCTAS",
    251 : "CBT",
    287 : "CSDR_1XCM", #cproc -> csdr
    288 : "CSDR_1XSM", #cproc -> csdr
    289 : "CSDR_HRPDCM", #cproc -> csdr
    290 : "CSDR_HRPDSM", #cproc -> csdr
}

def cproc_get_pid_str(pid, outstream):
    if (pid == 187 or pid == 188 or pid == 189 or pid == 190):
        pid = pid + 100
    
    for pidIndex in cproc_pid_enum_table.keys():
        if pidIndex == pid:
            return cproc_pid_enum_table[pidIndex]

    return "unknown"
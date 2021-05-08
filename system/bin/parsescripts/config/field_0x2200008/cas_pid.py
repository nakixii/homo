#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list pid
modify  record  :   2016-01-07 create file
"""

import string


cas_pid_enum_table = {
    1   : "TIMER",
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
    91  : "HRM",
    101 : "USIM",
    171 : "ERRC",
    172 : "ERMM",
    219 : "MTC",
    222 : "I0_IMSA",
    225 : "RRM",
    284 : "I1_IMSA",
}

def cas_get_pid_str(pid, outstream):
    
    for pidIndex in cas_pid_enum_table.keys():
        if pidIndex == pid:
            return cas_pid_enum_table[pidIndex]

    return "unknown"
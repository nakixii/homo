#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list pid
modify  record  :   2016-04-27 create file
"""

import string

cnas_pid_enum_table = {
     1:	"Timer",
     2:	"Gcomc",
     6: "I1_MSCC",
    20: "I1_Usim",
	24:	"I1_Grm",
	28:	"I1_Gas",
	29:	"I1_Mm",
	30:	"I1_Mmc",
	31:	"I1_Gmm",
	32:	"I1_MMA",
    33: "I1_CC",
    34: "I1_SS",
    40: "I1_Taf",
	44:	"I1_Gphy",
    47: "I1_Apm",
    48: "I1_Sleep",
    59: "HRPDRPA",
    61: "HRPDRMAC",
    66: "HRPDSIG",
    67: "PPPC",
    75: "1XCASM",
    78: "HALMP",
    79: "HRUP",
    80: "HSCP",
    81: "HSP",
    82: "XREG",
	83: "XSD",
	84: "XCC",
	85: "HSD",
	86: "HLU",
	87: "HSM",
	88: "EHSM",
    89: "XSMS",
    90: "XPDS",
    91: "HRM",
   101: "Usim",
   105: "OM",
   106: "NVIM",
   108: "DIAG",
   118: "MSCC",
   128:	"Gas",
   129:	"Lapdm",
   130: "Grm",
   133: "Wrr",
   134: "Wcom",
   140: "RABM",
   141: "Mmc",
   142: "Mm",
   143: "Gmm",
   144: "CC",
   145: "SM",
   146: "SMS",
   147: "SS",
   152: "Taf",
   157: "Mma",
   158: "Sleep",
   170: "Css",
   171: "Errc",
   172: "Ermm",
   173: "LMM",
   201: "Apm",
   203: "Wphy",
   205: "Gphy",
   209: "Mta",
   217: "Trrc",
   219: "Mtc",
   222: "IMSA",
   225: "Rrm",
   233: "I2_MMC",
   235: "I2_MMA",
   243: "I2_TAF",
   247: "I2_MSCC",
}

def cnas_get_pid_str( pid):
    for pidIndex in cnas_pid_enum_table.keys():
        if pidIndex == pid:
            return cnas_pid_enum_table[pidIndex]

    return "none"
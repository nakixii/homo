#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list pid
modify  record  :   2016-01-27 create file
"""

import string

taf_dsm_pid_enum_table = {
     1: "Timer",
    30: "I1_Mmc",
    32: "I1_MMA",
    40: "I1_Taf",
   105: "OM",
   106: "NVIM",
   108: "DIAG",
   125: "I1_ESM",
   141: "Mmc",
   152: "Taf",
   157: "Mma",
   174: "ESM",
   197: "CDS",
   222: "IMSA",
   233: "I2_MMC",
   235: "I2_MMA",
   243: "I2_TAF",
   284: "I1_IMSA",
   308: "DSM",
   309: "I1_DSM",
   310: "I2_DSM",
   65549: "AT",
   65551: "ADS_UL",
}

def taf_dsm_get_pid_str( pid):
    for pidIndex in taf_dsm_pid_enum_table.keys():
        if pidIndex == pid:
            return taf_dsm_pid_enum_table[pidIndex]

    return "none"
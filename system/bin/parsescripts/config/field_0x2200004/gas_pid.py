#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list pid
author          :   sunbing 00184266
modify  record  :   2016-01-07 create file
"""

import string

GAS_MODEM0_PID_TABLE = {
   1: "Timer",
   2: "Gcomc",
   28: "Msp_pid",
   101: "Usim",
   111: "Bastet",
   128: "Gas",
   129: "Lapdm",
   130: "Grm",
   133: "Wrr",
   134: "Wcom",
   136: "Bmc",
   137: "Pdcp",
   138: "Rlc",
   139: "Mac",
   140: "Rabm",
   141: "Mmc",
   142: "Mm",
   143: "Gmm",
   152: "Taf",
   158: "Sleep",
   170: "Css",
   171: "Errc",
   172: "Ermm",
   201: "Apm",
   203: "Wphy",
   205: "Gphy",
   209: "Mta",
   217: "Trrc",
   219: "Mtc",
   225: "Rrm",
   8192: "GPHY",
   8195: "WPHY",
}

GAS_MODEM1_PID_TABLE = {
    1: "Timer",
    11: "I1_WRR",
    12: "I1_WCOM",
    13: "I1_BMC",
    14: "I1_PDCP",
    15: "I1_RLC",
    16: "I1_MAC",
    17: "I1_RLCDL",
    18: "I1_MACDL",
    20: "I1_Usim",
    24: "I1_Grm",
    25: "I1_Lapdm",
    28: "I1_Gas",
    29: "I1_Mm",
    30: "I1_Mmc",
    31: "I1_Gmm",
    37: "I1_Rabm",
    40: "I1_Taf",
    43: "I1_Mta",
    44: "I1_Gphy",
    47: "I1_Apm",
    48: "I1_Sleep",
    109: "I1_Errc",
    111: "Bastet",
    122: "I1_Ermm",
    170: "Css",
    219: "Mtc",
    225: "Rrm",
    272: "I1_WPHY",
    8193: "GPHY",
    8196: "WPHY",
}


def guas_get_modem0_pid_str(pid):
    for pid_index in GAS_MODEM0_PID_TABLE.keys():
        if pid_index == pid:
            return GAS_MODEM0_PID_TABLE[pid_index]

    return "none"


def guas_get_modem1_pid_str(pid):
    for pid_index in GAS_MODEM1_PID_TABLE.keys():
        if pid_index == pid:
            return GAS_MODEM1_PID_TABLE[pid_index]

    return "none"
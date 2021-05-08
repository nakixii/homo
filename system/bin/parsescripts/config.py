#!/usr/bin/env python3
# coding=utf-8
# Copyright (C) Huawei Technologies Co., Ltd. 2010-2018. All rights reserved.

import os
import sys
import struct
import string

#entry_mntn config
#error number define
global error
global modeList
global errmodid
global mntnbase
global corenum
errmodid = 0
mntnbase = 0
error = {
    'ERR_SUCCESS'           :0x0,
    'ERR_NO_FIELD_SCRIPTS'  :0x1,
    'ERR_NO_VERSION_SCRIPTS':0x2,
    'ERR_OPEN_INFILE'       :0x3,
    'ERR_OPEN_OUTFILE'      :0x4,
    'ERR_CHECK_VERSION'     :0x5,
    'ERR_CHECK_LEN'         :0x6,
    'ERR_EXPARSE_DATA'      :0x7,
    'ERR_OTHER'             :0x8,
    'ERR_PARAMS_ERROR'      :0x9,
    'ERR_CHECK_FIELD'       :0xA
}
modeList = ('0' '1' 'm')

filedict = {"modem_dump.bin" : "modem_dump.txt", "lphy_dump.bin":"lphy_dump.txt", "nrphy_dump.bin":"nrphy_dump.txt", "rfdsp_dump.bin":"rfdsp_dump.txt", "pde.bin" : "pde.txt"}

modem_dump_txt = "modem_dump.txt"
modem_back = "modem_dump_backup.bin"
modem_print = "modem_kernel_print.txt"

exc_info = {
    'FAST_POWERUP':0x0,
    'POWERKEY_POWERUP':0x1,
    'VBUS_POWERUP':0x2,
    'ALARM_ON_POWERUP':0x3,
    'POWERHOLD_POWERUP':0x4,
    'POWERKEY_SHUTDOWN':0x5,
    'POWERHOLD_SHUTDOWN':0x6,
    'POWERKEY_10S_REBOOT':0x7,
    'RESETKEY_REBOOT':0x8,
    'SOFT_REBOOT':0x9,
    'PMU_EXCEPTION':0xa,
    'AP_S_WDT_TIMEOUT':0xc,
    'AP_S_EXC_PANIC':0xd,
    'AP_S_EXC_SFTRESET':0xe,
    'AP_S_EXC_PANIC_INT':0xf,
    'AP_S_DMSS_EXC':0x10,
    'LPM3_S_EXCEPTION':0x12,
    'LPM3_S_WDT_TIMEOUT':0x13,
    'TEEOS_S_WDT_TIMEOUT':0x15,
    'CP_S_MODEMAP':0x52,
    'CP_S_EXCEPTION':0x53,
    'CP_S_RESETFAIL':0x54,
    'CP_S_NORMALRESET':0x55,
    'CP_S_MODEMNOC':0x51,
    'CP_S_MODEMDMSS':0x50,
    'CP_S_RILD_EXCEPTION':0x56,
    'CP_S_3RD_EXCEPTION':0x57,
    'RDR_TEST_WDT_TIMEOUT':0x62,
    'RDR_TEST_PANIC':0x63,
    'RDR_TEST_DIE':0x64,
    'RDR_TEST_STACKOVERFLOW':0x65,
    'UNDEFINE':0x66,
}

core_info = {
    "CP"            :0x1,
    "MODEMAP"            :0x2,
}
core_order = {
    "CP"            :0x0,
    "MODEMAP"            :0x1,
}

def get_core_name(coreid):
    for core,index in core_info.items():
        if index==coreid:
            return core
    return "unknown"

def get_exc_tyep(exc_type):
    for e_type,index in exc_info.items():
        if index==exc_type:
            return e_type
    return "UNDEFINE"


def get_mntn_addr():
    return mntnbase

def get_core_num():
    return corenum


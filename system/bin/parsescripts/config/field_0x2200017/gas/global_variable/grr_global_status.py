#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list grr global status
author          :   sunbing 00184266
modify  record  :   2016-01-09 create file
"""

import struct
import string

GAS_GRR_L1_STA_ENUM_TABLE = {
    0x0: "GASGRR_L1_STA_IDLE",
    0x1: "GASGRR_L1_STA_ACCESS",
    0x2: "GASGRR_L1_STA_UNSTABLE",
    0x3: "GASGRR_L1_STA_ABNORMAL",
    0x4: "GASGRR_L1_STA_TRANSFER",
}

GAS_GRR_L2_STA_ENUM_TABLE = {
    0x0001: "GASGRR_L2_STA_RAND_IDLE",
    0x0002: "GASGRR_L2_STA_ACS_PERMIT",
    0x0004: "GASGRR_L2_STA_ACCESS",
    0x0008: "GASGRR_L2_STA_QUEUING",
    0x0010: "GASGRR_L2_STA_REJECT_PH1",
    0x0020: "GASGRR_L2_STA_REJECT_PH2",
    0x1001: "GASGRR_L2_STA_ACCESS_ACTIVE",
    0x1002: "GASGRR_L2_STA_ACCESS_ONEPHASECR",
    0x1003: "GASGRR_L2_STA_ACCESS_DEACTIVE",
    0x1004: "GASGRR_L2_STA_ACCESS_TWOPHASE",
    0x2001: "GASGRR_L2_STA_DOWNLINK_IDLE",
    0x2002: "GASGRR_L2_STA_DOWNLINK_ACTIVE",
    0x2004: "GASGRR_L2_STA_DOWNLINK_TBF",
    0x2008: "GASGRR_L2_STA_DOWNLINK_RELEASE",
    0x2010: "GASGRR_L2_STA_DOWNLINK_DEACTIVE",
    0x3001: "GASGRR_L2_STA_ABNORMAL_RELEASE",
    0x3002: "GASGRR_L2_STA_ABNORMAL_DEACTIVE_1",
    0x3004: "GASGRR_L2_STA_ABNORMAL_DEACTIVE_2",
    0x3008: "GASGRR_L2_STA_ABNORMAL_GET_SYSINFO",
}

GAS_GRR_L3_STA_ENUM_TABLE = {
    0x0001: "GASGRR_L3_STA_UPLINK_IDLE",
    0x0002: "GASGRR_L3_STA_UPLINK_ACCESS",
    0x0004: "GASGRR_L3_STA_UPLINK_REJECT",
    0x0008: "GASGRR_L3_STA_UPLINK_ACTIVE",
    0x0010: "GASGRR_L3_STA_UPLINK_TBF",
    0x0020: "GASGRR_L3_STA_UPLINK_RELEASE",
    0x0040: "GASGRR_L3_STA_UPLINK_DEACTIVE",
}


def get_grr_l1_sta(state):
    for index in GAS_GRR_L1_STA_ENUM_TABLE.keys():
        if index == state:
            return GAS_GRR_L1_STA_ENUM_TABLE[index]

    return "none"


def get_grr_l2_sta(state):
    for index in GAS_GRR_L2_STA_ENUM_TABLE.keys():
        if index == state:
            return GAS_GRR_L2_STA_ENUM_TABLE[index]

    return "none"


def get_grr_l3_sta(state):
    for index in GAS_GRR_L3_STA_ENUM_TABLE.keys():
        if index == state:
            return GAS_GRR_L3_STA_ENUM_TABLE[index]

    return "none"


def anls_modem_x_grr_glob_sta(instream, file_offset, outstream):
    instream.seek(file_offset)

    (grr_l1_sta,) = struct.unpack('H', instream.read(2))
    str_grr_l1_sta = get_grr_l1_sta(grr_l1_sta)
    str_grr_l1_sta = '%s(0x%x)' % (str_grr_l1_sta, grr_l1_sta)
    outstream.writelines(["%-15s%-7s\n" % ("grr_l1_sta :", str_grr_l1_sta)])

    (grr_l2_sta,) = struct.unpack('H', instream.read(2))
    str_grr_l2_sta = get_grr_l2_sta(grr_l2_sta)
    str_grr_l2_sta = '%s(0x%x)' % (str_grr_l2_sta, grr_l2_sta)
    outstream.writelines(["%-15s%-7s\n" % ("grr_l2_sta :", str_grr_l2_sta)])

    (grr_l3_sta,) = struct.unpack('H', instream.read(2))
    str_grr_l3_sta = get_grr_l3_sta(grr_l3_sta)
    str_grr_l3_sta = '%s(0x%x)' % (str_grr_l3_sta, grr_l3_sta)
    outstream.writelines(["%-15s%-7s\n" % ("grr_l3_sta :", str_grr_l3_sta)])

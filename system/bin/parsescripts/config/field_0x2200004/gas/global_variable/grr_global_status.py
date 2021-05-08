#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list grr global status
modify  record  :   2016-01-09 create file
"""

import struct
import string

gas_grr_l1_sta_enum_table = {
0x0 : "GASGRR_L1_STA_IDLE",
0x1 : "GASGRR_L1_STA_ACCESS",
0x2 : "GASGRR_L1_STA_UNSTABLE",
0x3 : "GASGRR_L1_STA_ABNORMAL",
0x4 : "GASGRR_L1_STA_TRANSFER",
}

gas_grr_l2_sta_enum_table = {
0x0001 : "GASGRR_L2_STA_RAND_IDLE",
0x0002 : "GASGRR_L2_STA_ACS_PERMIT",
0x0004 : "GASGRR_L2_STA_ACCESS",
0x0008 : "GASGRR_L2_STA_QUEUING",
0x0010 : "GASGRR_L2_STA_REJECT_PH1",
0x0020 : "GASGRR_L2_STA_REJECT_PH2",
0x1001 : "GASGRR_L2_STA_ACCESS_ACTIVE",
0x1002 : "GASGRR_L2_STA_ACCESS_ONEPHASECR",
0x1003 : "GASGRR_L2_STA_ACCESS_DEACTIVE",
0x1004 : "GASGRR_L2_STA_ACCESS_TWOPHASE",
0x2001 : "GASGRR_L2_STA_DOWNLINK_IDLE",
0x2002 : "GASGRR_L2_STA_DOWNLINK_ACTIVE",
0x2004 : "GASGRR_L2_STA_DOWNLINK_TBF",
0x2008 : "GASGRR_L2_STA_DOWNLINK_RELEASE",
0x2010 : "GASGRR_L2_STA_DOWNLINK_DEACTIVE",
0x3001 : "GASGRR_L2_STA_ABNORMAL_RELEASE",
0x3002 : "GASGRR_L2_STA_ABNORMAL_DEACTIVE_1",
0x3004 : "GASGRR_L2_STA_ABNORMAL_DEACTIVE_2",
0x3008 : "GASGRR_L2_STA_ABNORMAL_GET_SYSINFO",
}

gas_grr_l3_sta_enum_table = {
0x0001 : "GASGRR_L3_STA_UPLINK_IDLE",
0x0002 : "GASGRR_L3_STA_UPLINK_ACCESS",
0x0004 : "GASGRR_L3_STA_UPLINK_REJECT",
0x0008 : "GASGRR_L3_STA_UPLINK_ACTIVE",
0x0010 : "GASGRR_L3_STA_UPLINK_TBF",
0x0020 : "GASGRR_L3_STA_UPLINK_RELEASE",
0x0040 : "GASGRR_L3_STA_UPLINK_DEACTIVE",
}

def get_grr_l1_sta( usState):
    for index in gas_grr_l1_sta_enum_table.keys():
        if index == usState:
            return gas_grr_l1_sta_enum_table[index]

    return "none"

def get_grr_l2_sta( usState):
    for index in gas_grr_l2_sta_enum_table.keys():
        if index == usState:
            return gas_grr_l2_sta_enum_table[index]

    return "none"

def get_grr_l3_sta( usState):
    for index in gas_grr_l3_sta_enum_table.keys():
        if index == usState:
            return gas_grr_l3_sta_enum_table[index]

    return "none"

def analysis_modemX_grr_global_status( instream, fileOffset, outstream):
        instream.seek(fileOffset)

        (usGrrL1Sta,)     = struct.unpack('H', instream.read(2))
        stGrrL1Sta        = get_grr_l1_sta(usGrrL1Sta)
        stGrrL1Sta        = '%s(0x%x)' % ( stGrrL1Sta, usGrrL1Sta)
        outstream.writelines(["%-15s%-7s\n" % ("usGrrL1Sta :", stGrrL1Sta)])

        (usGrrL2Sta,)      = struct.unpack('H', instream.read(2))
        stGrrL2Sta         = get_grr_l2_sta(usGrrL2Sta)
        stGrrL2Sta         = '%s(0x%x)' % ( stGrrL2Sta, usGrrL2Sta)
        outstream.writelines(["%-15s%-7s\n" % ("usGrrL2Sta :", stGrrL2Sta)])

        (usGrrL3Sta,)      = struct.unpack('H', instream.read(2))
        stGrrL3Sta         = get_grr_l3_sta(usGrrL3Sta)
        stGrrL3Sta         = '%s(0x%x)' % ( stGrrL3Sta, usGrrL3Sta)
        outstream.writelines(["%-15s%-7s\n" % ("usGrrL3Sta :", stGrrL3Sta)])
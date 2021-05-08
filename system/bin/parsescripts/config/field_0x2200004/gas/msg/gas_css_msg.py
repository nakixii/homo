#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list gas css msg
modify  record  :   2016-01-07 create file
"""

gas_css_msg_enum_table = {
0x0 : "CSS_MULTI_BAND_SCAN_REQ",
0x1 : "CSS_STOP_BAND_SCAN_REQ",
0x2 : "CSS_CURR_GEO_IND",
0x3 : "CSS_AS_BAND_SACN_REQ",
0x4 : "CSS_AS_STOP_BAND_SACN_REQ",
0x5 : "CSS_MULTI_BAND_SCAN_CNF",
0x6 : "CSS_STOP_BAND_SCAN_CNF",
0x7 : "CSS_CURR_GEO_RSP",
0x8 : "CSS_AS_BAND_SACN_CNF",
0x9 : "CSS_AS_BAND_SACN_IND",
0xa : "CSS_AS_STOP_BAND_SACN_CNF",
0xb : "CSS_HISTORY_FREQ_IND",
0xc : "CSS_CURR_RPLMN_INFO_NOTIFY",
0xd : "CSS_CURR_TACLAC_INFO_IND",
0xe : "CSS_CURR_TACLAC_CLOUD_LINE_INFO_NOTIFY",
0xf : "CSS_MS_BAND_INFO_NOTIFY",
}

def get_gas_css_msg_str( MsgId):
    for MsgIdIndex in gas_css_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return gas_css_msg_enum_table[MsgIdIndex]

    return "none"
#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list ps css msg
modify  record  :   2016-12-13 create file
"""

ps_css_msg_enum_table = {
0x0000 : "ID_CSS_MULTI_BAND_SCAN_REQ",
0x0001 : "ID_CSS_STOP_BAND_SCAN_REQ",
0x0002 : "ID_CSS_CURR_GEO_IND",
0x0003 : "ID_CSS_AS_BAND_SCAN_REQ",
0x0004 : "ID_CSS_AS_STOP_BAND_SCAN_REQ",
0x0005 : "ID_CSS_MULTI_BAND_SCAN_CNF",
0x0006 : "ID_CSS_STOP_BAND_SCAN_CNF",
0x0007 : "ID_CSS_CURR_GEO_RSP",
0x0008 : "ID_CSS_AS_BAND_SCAN_CNF",
0x0009 : "ID_CSS_AS_BAND_SCAN_IND",
0x000A : "ID_CSS_AS_STOP_BAND_SCAN_CNF",
0x000B : "ID_CSS_HISTORY_FREQ_IND",
0x000C : "ID_CSS_CURR_RPLMN_INFO_NOFITY",
0x000D : "ID_CSS_CURR_TACLAC_INFO_IND",
0x000E : "ID_CSS_CURR_TACLAC_CLOUD_LINE_INFO_NOTIFY",
0x000F : "ID_CSS_MS_BAND_INFO_NOTIFY",
}

def get_ps_css_msg_str(MsgId):
    for MsgIdIndex in ps_css_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return ps_css_msg_enum_table[MsgIdIndex]

    return "none"
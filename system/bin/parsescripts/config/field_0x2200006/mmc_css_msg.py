#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list mmc css msg
modify  record  :   2018-04-20 create file
"""

mmc_css_msg_enum_table = {
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
0x000a : "ID_CSS_AS_STOP_BAND_SCAN_CNF",
0x000b : "ID_CSS_HISTORY_FREQ_IND",
0x000c : "ID_CSS_CURR_RPLMN_INFO_NOTIFY",
0x000d : "ID_CSS_CURR_TACLAC_INFO_IND",
0x000e : "ID_CSS_CURR_TACLAC_CLOUD_LINE_INFO_NOTIFY",
0x000f : "ID_CSS_SRCHED_PLMN_INFO_NOTIFY",
0x0010 : "ID_CSS_MS_BAND_INFO_NOTIFY",
}

def get_mmc_css_msg_str( MsgId):
    for MsgIdIndex in mmc_css_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return mmc_css_msg_enum_table[MsgIdIndex]

    return "none"
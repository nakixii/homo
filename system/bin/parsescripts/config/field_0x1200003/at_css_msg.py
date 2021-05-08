#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   at css msg
modify  record  :   2019-05-25 create file
"""

at_css_msg_enum_table = {
0x0001 : "ID_AT_CSS_MCC_INFO_SET_REQ",
0x0002 : "ID_AT_CSS_MCC_VERSION_INFO_REQ",
0x0003 : "ID_AT_CSS_BLACK_CELL_LIST_SET_REQ",
0x0004 : "ID_AT_CSS_BLACK_CELL_LIST_QUERY_REQ",
0x0005 : "ID_AT_CSS_LINE_INDEX_LIST_SET_REQ",
0x0006 : "ID_AT_CSS_LINE_DETAIL_SET_REQ",
0x0007 : "ID_AT_CSS_LINE_INDEX_LIST_QUERY_REQ",
0x0008 : "ID_AT_CSS_VZWMRUC_SET_REQ",
0x0009 : "ID_AT_CSS_VZWMRUE_SET_REQ",
0x000a : "ID_AT_CSS_VZWMRUE_QUERY_REQ",
0x1001 : "ID_CSS_AT_MCC_INFO_SET_CNF",
0x1002 : "ID_CSS_AT_MCC_VERSION_INFO_CNF",
0x1003 : "ID_CSS_AT_QUERY_MCC_INFO_NOTIFY",
0x1004 : "ID_CSS_AT_BLACK_CELL_LIST_SET_CNF",
0x1005 : "ID_CSS_AT_BLACK_CELL_LIST_QUERY_CNF",
0x1006 : "ID_CSS_AT_BLACK_CELL_MCC_NOTIFY",
0x1007 : "ID_CSS_AT_LINE_INDEX_LIST_SET_CNF",
0x1008 : "ID_CSS_AT_LINE_DETAIL_SET_CNF",
0x1009 : "ID_CSS_AT_LINE_INDEX_LIST_QUERY_CNF",
0x100a : "ID_CSS_AT_LINE_PLMN_NOTIFY",
0x100b : "ID_CSS_AT_LINE_INDEX_NOTIFY",
0x100c : "ID_CSS_AT_VZWMRUC_SET_CNF",
0x100d : "ID_CSS_AT_VZWMRUE_SET_CNF",
0x100e : "ID_CSS_AT_VZWMRUE_QUERY_CNF",
}

def get_at_css_msg_str( MsgId):
    for MsgIdIndex in at_css_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return at_css_msg_enum_table[MsgIdIndex]

    return "none"
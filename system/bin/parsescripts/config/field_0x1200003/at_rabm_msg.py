#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list at rabm msg
modify  record  :   2019-05-25 create file
"""

at_rabm_msg_enum_table = {
0x00 : "ID_AT_RABM_SET_FASTDORM_PARA_REQ",
0x01 : "ID_AT_RABM_QRY_FASTDORM_PARA_REQ",
0x02 : "ID_RABM_AT_SET_FASTDORM_PARA_CNF",
0x03 : "ID_RABM_AT_QRY_FASTDORM_PARA_CNF",
0x04 : "ID_AT_RABM_SET_RELEASE_RRC_REQ",
0x05 : "ID_RABM_AT_SET_RELEASE_RRC_CNF",
0x06 : "ID_AT_RABM_SET_VOICEPREFER_PARA_REQ",
0x07 : "ID_RABM_AT_SET_VOICEPREFER_PARA_CNF",
0x08 : "ID_AT_RABM_QRY_VOICEPREFER_PARA_REQ",
0x09 : "ID_RABM_AT_QRY_VOICEPREFER_PARA_CNF",
0x0a : "ID_RABM_AT_VOICEPREFER_STATUS_REPORT",
}

def get_at_rabm_msg_str( MsgId):
    for MsgIdIndex in at_rabm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return at_rabm_msg_enum_table[MsgIdIndex]

    return "none"
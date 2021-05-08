#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   at ppp msg
modify  record  :   2019-05-25 create file
"""

at_ppp_msg_enum_table = {
0x00 : "AT_PPP_RELEASE_IND_MSG",
0x01 : "AT_PPP_MODEM_MSC_IND_MSG",
0x02 : "AT_PPP_PROTOCOL_REL_IND_MSG",
}

def get_at_ppp_msg_str( MsgId):
    for MsgIdIndex in at_ppp_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return at_ppp_msg_enum_table[MsgIdIndex]

    return "none"
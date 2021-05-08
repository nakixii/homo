#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list ads dsm msg
modify  record  :   2019-05-12 create file
"""

ads_dsm_msg_enum_table = {
0x0001 : "ID_DSM_ADS_IFACE_CONFIG_IND",
}

def get_ads_dsm_msg_str( MsgId):
    for MsgIdIndex in ads_dsm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return ads_dsm_msg_enum_table[MsgIdIndex]

    return "none"
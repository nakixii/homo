#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list imsa mscc msg
modify  record  :   2016-01-27 create file
"""

imsa_mscc_msg_enum_table = {
0x00 : "ID_MSCC_IMSA_START_REQ",
0x01 : "ID_MSCC_IMSA_STOP_REQ",
0x02 : "ID_MSCC_IMSA_DEREG_REQ",
0x03 : "ID_MSCC_IMSA_SERVICE_CHANGE_IND",
0x04 : "ID_MSCC_IMSA_CAMP_INFO_CHANGE_IND",
0x05 : "ID_MSCC_IMSA_VOICE_DOMAIN_CHANGE_IND",
0x06 : "ID_MSCC_IMSA_IMS_DOMAIN_CFG_SET_REQ",
0x07 : "ID_MSCC_IMSA_ROAM_IMS_SUPPORT_SET_REQ",
0x08 : "ID_MSCC_IMSA_AREA_LOST_IND",
0x09 : "ID_MSCC_IMSA_REG_REQ",
0x40 : "ID_IMSA_MSCC_START_CNF",
0x41 : "ID_IMSA_MSCC_STOP_CNF",
0x42 : "ID_IMSA_MSCC_DEREG_CNF",
0x43 : "ID_IMSA_MSCC_IMS_VOICE_CAP_NOTIFY",
0x44 : "ID_IMSA_MSCC_IMS_DOMAIN_CFG_SET_CNF",
0x45 : "ID_IMSA_MSCC_ROAM_IMS_SUPPORT_SET_CNF",
0x46 : "ID_IMSA_MSCC_REG_CNF",
}

def get_imsa_mscc_msg_str( MsgId):
    for MsgIdIndex in imsa_mscc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return imsa_mscc_msg_enum_table[MsgIdIndex]

    return "none"
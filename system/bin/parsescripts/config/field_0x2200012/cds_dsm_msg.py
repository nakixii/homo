#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list cds dsm msg
modify  record  :   2019-05-12 create file
"""

imsa_cds_msg_enum_table = {
0x0001 : "ID_DSM_CDS_PDU_SESSION_INFO_CONFIG_IND",
0x0002 : "ID_DSM_CDS_IFACE_CONFIG_IND",
}

def get_cds_dsm_msg_str( MsgId):
    for MsgIdIndex in imsa_cds_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return imsa_cds_msg_enum_table[MsgIdIndex]

    return "none"
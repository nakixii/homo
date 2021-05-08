#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list xsd xcc msg
modify  record  :   2016-04-27 create file
"""

xsd_xcc_msg_enum_table = {
0x0000 : "ID_XSD_XCC_START_REQ",
0x0001 : "ID_XCC_XSD_START_CNF",
0x0002 : "ID_XSD_XCC_POWER_OFF_REQ",
0x0003 : "ID_XCC_XSD_POWER_OFF_CNF",
0x0004 : "ID_XCC_XSD_DEREGISTER_IND",
0x0005 : "ID_XSD_XCC_NDSS_RESULT_IND",
}

def get_xsd_xcc_msg_str( MsgId):
    for MsgIdIndex in xsd_xcc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return xsd_xcc_msg_enum_table[MsgIdIndex]

    return "none"
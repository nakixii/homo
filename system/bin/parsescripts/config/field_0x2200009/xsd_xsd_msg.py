#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list xsd xsd msg
modify  record  :   2016-04-27 create file
"""

xsd_xsd_msg_enum_table = {
0x0000 : "ID_CNAS_XSD_XSD_ABORT_REQ",
0x0001 : "ID_CNAS_XSD_XSD_SWITCH_ON_RSLT_CNF",
0x0002 : "ID_CNAS_XSD_XSD_BSR_RSLT_CNF",
0x0003 : "ID_CNAS_XSD_XSD_POWER_OFF_RSLT_CNF",
0x0004 : "ID_CNAS_XSD_XSD_REDIRECTION_IND",
0x0005 : "ID_CNAS_XSD_XSD_REDIRECTION_RSLT_CNF",
0x0006 : "ID_CNAS_XSD_XSD_SYSTEM_ACQUIRED_REQ",
0x0007 : "ID_CNAS_XSD_XSD_SYSTEM_ACQUIRED_RSLT_CNF",
}

def get_xsd_xsd_msg_str( MsgId):
    for MsgIdIndex in xsd_xsd_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return xsd_xsd_msg_enum_table[MsgIdIndex]

    return "none"
#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list xsd xreg msg
modify  record  :   2016-04-27 create file
"""

xsd_xreg_msg_enum_table = {
0x0000 : "ID_XSD_XREG_START_REQ",
0x0001 : "ID_XREG_XSD_START_CNF",
0x0002 : "ID_XSD_XREG_POWER_OFF_REQ",
0x0003 : "ID_XREG_XSD_POWER_OFF_CNF",
0x0004 : "ID_XSD_XREG_SYS_INFO_IND",
0x0005 : "ID_XSD_XREG_REDIRECTION_IND",
0x0006 : "ID_XSD_XREG_DEREGISTER_IND",
0x0007 : "ID_XSD_XREG_UE_STATE_IND",
0x0008 : "ID_XREG_XSD_REG_SUCCESS_IND",
0x0009 : "ID_XSD_XREG_NORMAL_SERVICE_IND",
}

def get_xsd_xreg_msg_str( MsgId):
    for MsgIdIndex in xsd_xreg_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return xsd_xreg_msg_enum_table[MsgIdIndex]

    return "none"
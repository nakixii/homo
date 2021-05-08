#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list hsd hsd msg
modify  record  :   2016-04-27 create file
"""

hsd_hsd_msg_enum_table = {
0x0000 : "ID_CNAS_HSD_HSD_ABORT_REQ",
0x0001 : "ID_CNAS_HSD_HSD_SWITCH_ON_RSLT_CNF",
0x0002 : "ID_CNAS_HSD_HSD_BSR_RSLT_CNF",
0x0003 : "ID_CNAS_HSD_HSD_POWER_OFF_RSLT_CNF",
0x0004 : "ID_CNAS_HSD_HSD_REDIRECTION_IND",
0x0005 : "ID_CNAS_HSD_HSD_REDIRECTION_RSLT_CNF",
0x0006 : "ID_CNAS_HSD_HSD_SYSTEM_ACQUIRED_REQ",
0x0007 : "ID_CNAS_HSD_HSD_SYSTEM_ACQUIRED_RSLT_CNF",
0x0008 : "ID_CNAS_HSD_HSD_POWER_SAVE_RSLT_CNF",
0x0009 : "ID_CNAS_HSD_HSD_INTER_SYS_RSLT_CNF",
0x000A : "ID_CNAS_HSD_HSD_BG_SRCH_RSLT_CNF",
0x1000 : "ID_CNAS_XSD_HSD_SYS_ACQ_RSLT_IND",
}

def get_hsd_hsd_msg_str( MsgId):
    for MsgIdIndex in hsd_hsd_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return hsd_hsd_msg_enum_table[MsgIdIndex]

    return "none"
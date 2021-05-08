#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list xreg timer msg
modify  record  :   2016-04-27 create file
"""

xreg_timer_msg_enum_table = {
0x00 : "TI_CNAS_XREG_TIMER_T57M",
0x01 : "TI_CNAS_XREG_TIMER_PERIOD_REG",
0x02 : "TI_CNAS_XREG_TIMER_ESTCNF_PT",
0x03 : "TI_CNAS_XREG_TIMER_PWROFF_ESTCNF_PT",
0x04 : "TI_CNAS_XREG_TIMER_ABORTCNF_PT",
0x05 : "TI_CNAS_XREG_TIMER_ZONELIST_PT",
0x06 : "TI_CNAS_XREG_TIMER_CARDFILE_CNF_PT",
}

def get_xreg_timer_msg_str( MsgId):
    for MsgIdIndex in xreg_timer_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return xreg_timer_msg_enum_table[MsgIdIndex]

    return "none"
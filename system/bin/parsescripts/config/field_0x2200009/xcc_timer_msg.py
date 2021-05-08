#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list xcc timer msg
modify  record  :   2016-04-27 create file
"""

xcc_timer_msg_enum_table = {
0x00 : "TI_CNAS_XCC_T52M",
0x01 : "TI_CNAS_XCC_T53M",
0x02 : "TI_CNAS_XCC_WAIT_APS_SUSPEND_RSP",
0x03 : "TI_CNAS_XCC_WAIT_AS_EST_CNF",
0x04 : "TI_CNAS_XCC_WAIT_AS_CALL_INIT_IND",
0x05 : "TI_CNAS_XCC_WAIT_CONN_L2_ACK",
0x06 : "TI_CNAS_XCC_WAIT_FOR_INCOMING_RSP",
0x07 : "TI_CNAS_XCC_PROTECT_POWER_DOWN_ENDING",
0x08 : "TI_CNAS_XCC_WAIT_FLASH_CNF_L2_ACK",
0x09 : "TI_CNAS_XCC_WAIT_BURST_DTMF_CNF_L2_ACK",
0x0A : "TI_CNAS_XCC_WAIT_EMERGENCY_CALL_FLASH_CNF_L2_ACK",
0x0B : "TI_CNAS_XCC_WAIT_CONT_DTMF_CNF_L2_ACK",
0x0C : "TI_CNAS_XCC_WAIT_ESR_END_IND",
}

def get_xcc_timer_msg_str( MsgId):
    for MsgIdIndex in xcc_timer_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return xcc_timer_msg_enum_table[MsgIdIndex]

    return "none"
#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list ehsm timer msg
modify  record  :   2016-04-27 create file
"""

ehsm_timer_msg_enum_table = {
0x00 : "TI_CNAS_EHSM_WAIT_HSM_CONN_EST_CNF",
0x01 : "TI_CNAS_EHSM_WAIT_CONN_RETRY_EST",
0x02 : "TI_CNAS_EHSM_WAIT_CTTF_PDN_SETUP_CNF",
0x03 : "TI_CNAS_EHSM_WAIT_RETRY_PDN_SETUP",
0x04 : "TI_CNAS_EHSM_WAIT_CTTF_PDN_DISC_CNF",
0x05 : "TI_CNAS_EHSM_WAIT_DETACH_CNF",
0x06 : "TI_CNAS_EHSM_WAIT_HSM_DISC_CNF",
0x07 : "TI_CNAS_EHSM_PROTECTING_POWER_OFF_PROCESS",
}

def get_ehsm_timer_msg_str( MsgId):
    for MsgIdIndex in ehsm_timer_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return ehsm_timer_msg_enum_table[MsgIdIndex]

    return "none"
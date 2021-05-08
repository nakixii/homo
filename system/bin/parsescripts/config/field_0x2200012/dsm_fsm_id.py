#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list fsm id
modify  record  :   2016-01-27 create file
"""

import string

taf_dsm_pdn_fsm_state_enum_table = {
0x00 : "INACTIVE",
0x01 : "WAIT_APS_ACTIVATE_CNF",
0x02 : "ACTIVE",
0x03 : "WAIT_APS_DEACTIVATE_CNF",
0x04 : "WAIT_APP_ANSWER_RSP",
}

def taf_dsm_get_fsm_state_str( fsmid):
    for FsmidIndex in taf_dsm_pdn_fsm_state_enum_table.keys():
        if FsmidIndex == fsmid:
            return taf_dsm_pdn_fsm_state_enum_table[FsmidIndex]

    return "none"
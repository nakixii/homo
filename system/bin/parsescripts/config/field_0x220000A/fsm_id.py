#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list fsm id
modify  record  :   2016-01-27 create file
"""

import string

nas_mscc_fsm_id_enum_table = {
0x00 : "L1_MAIN",
0x01 : "SWITCH_ON",
0x02 : "POWER_OFF",
0x03 : "SYS_ACQ",
0x04 : "BETTER_SYSTEM_RESELECTION",
0x05 : "SYSTEM_CONFIG",
0x06 : "CL_INTERSYS",
0x07 : "MODE_SELECTION",
}

def nas_mscc_get_fsmid_str( fsmid):
    for FsmidIndex in nas_mscc_fsm_id_enum_table.keys():
        if FsmidIndex == fsmid:
            return nas_mscc_fsm_id_enum_table[FsmidIndex]

    return "none"
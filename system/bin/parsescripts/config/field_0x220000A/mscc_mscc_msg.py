#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list imsa mscc msg
modify  record  :   2018-04-20 create file
"""

mscc_mscc_msg_enum_table = {
0x7000 : "ID_NAS_MSCC_MSCC_SWITCH_ON_RSLT_CNF",
0x7001 : "ID_NAS_MSCC_MSCC_POWER_OFF_RSLT_CNF",
0x7002 : "ID_NAS_MSCC_MSCC_SYS_ACQ_REQ",
0x7003 : "ID_NAS_MSCC_MSCC_SYS_ACQ_RSLT_CNF",
0x7004 : "ID_NAS_MSCC_MSCC_ABORT_FSM_REQ",
0x7005 : "ID_NAS_MSCC_MSCC_BSR_RSLT_CNF",
0x7006 : "ID_NAS_MSCC_MSCC_SYS_CFG_RSLT_CNF",
0x7007 : "ID_NAS_MSCC_MSCC_CL_INTERSYS_RSLT_CNF",
0x7008 : "ID_NAS_MSCC_MSCC_POWER_SAVE_REQ",
0x7009 : "ID_NAS_MSCC_MSCC_SWITCH_ON_REQ",
0x700A : "ID_NAS_MSCC_MSCC_MODE_SELECTION_REQ",
0x700B : "ID_NAS_MSCC_MSCC_MODE_SELECTION_RSLT_CNF",
0x700C : "ID_NAS_MSCC_MSCC_INTER_BSR_REQ",
0x700D : "ID_NAS_MSCC_MSCC_SYS_CFG_SET_REQ",
0x700E : "ID_NAS_MSCC_MSCC_PID_INIT_IND",
}

def get_mscc_mscc_msg_str( MsgId):
    for MsgIdIndex in mscc_mscc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return mscc_mscc_msg_enum_table[MsgIdIndex]

    return "none"
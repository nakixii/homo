#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list ehsm taf msg
modify  record  :   2016-04-27 create file
"""

ehsm_taf_msg_enum_table = {
0x0000 : "ID_APS_EHSM_PDN_ACTIVATE_REQ",
0x0001 : "ID_EHSM_APS_PDN_ACTIVATE_CNF",
0x0002 : "ID_EHSM_APS_PDN_ACTIVATE_IND",
0x0003 : "ID_APS_EHSM_PDN_DEACTIVATE_REQ",
0x0004 : "ID_EHSM_APS_PDN_DEACTIVATE_CNF",
0x0005 : "ID_EHSM_APS_PDN_DEACTIVATE_IND",
0x0006 : "ID_EHSM_APS_LTE_HANDOVER_TO_EHRPD_IND",
0x0007 : "ID_APS_EHSM_RECONN_REQ",
0x0008 : "ID_EHSM_APS_RECONN_CNF",
0x0009 : "ID_APS_EHSM_PS_RAT_TYPE_NOTIFY",
0x000A : "ID_APS_EHSM_PDN_CONTEXT_INFO_NOTIFY",
0x000B : "ID_APS_EHSM_LOC_DETACH_NOTIFY",
0x000C : "ID_APS_EHSM_LOC_DEACTIVATE_NOTIFY",
0x000D : "ID_APS_EHSM_DISC_NOTIFY",
0x000E : "ID_APS_EHSM_PDN_ATTACH_REQ",
0x000F : "ID_EHSM_APS_PDN_ATTACH_CNF",
0x0010 : "ID_EHSM_APS_PDN_INFO_CHANGE_IND",
}

def get_ehsm_taf_msg_str( MsgId):
    for MsgIdIndex in ehsm_taf_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return ehsm_taf_msg_enum_table[MsgIdIndex]

    return "none"
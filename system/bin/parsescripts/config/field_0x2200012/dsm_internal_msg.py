#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list dsm internal msg
modify  record  :   2019-05-12 create file
"""

dsm_inter_msg_enum_table = {
0x0801 : "ID_EVT_TAF_PS_CALL_PDP_ACTIVATE_CNF",
0x0802 : "ID_EVT_TAF_PS_CALL_PDP_ACTIVATE_REJ",
0x0803 : "ID_EVT_TAF_PS_CALL_PDP_ACTIVATE_IND",
0x0808 : "ID_EVT_TAF_PS_CALL_PDP_DEACTIVATE_CNF",
0x0809 : "ID_EVT_TAF_PS_CALL_PDP_DEACTIVATE_IND",
0x080B : "ID_EVT_TAF_PS_CALL_PDP_IPV6_INFO_IND",
0x080C : "ID_EVT_TAF_PS_CALL_PDP_RABID_CHANGE_IND",
0x080D : "ID_EVT_TAF_PS_CALL_HANDOVER_RESULT_NTF",
0x0831 : "ID_EVT_TAF_PS_CALL_ORIG_CNF",
0x0832 : "ID_EVT_TAF_PS_CALL_END_CNF",
}

def get_dsm_inter_msg_str( MsgId):
    for MsgIdIndex in dsm_inter_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return dsm_inter_msg_enum_table[MsgIdIndex]

    return "none"
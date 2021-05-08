#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list imsa dsm msg
modify  record  :   2019-05-12 create file
"""

imsa_dsm_msg_enum_table = {
0x0801 : "ID_EVT_TAF_PS_CALL_PDP_ACTIVATE_CNF",
0x0802 : "ID_EVT_TAF_PS_CALL_PDP_ACTIVATE_REJ",
0x0803 : "ID_EVT_TAF_PS_CALL_PDP_ACTIVATE_IND",
0x0804 : "ID_EVT_TAF_PS_CALL_PDP_MANAGE_IND",
0x0805 : "ID_EVT_TAF_PS_CALL_PDP_MODIFY_CNF",
0x0806 : "ID_EVT_TAF_PS_CALL_PDP_MODIFY_REJ",
0x0807 : "ID_EVT_TAF_PS_CALL_PDP_MODIFY_IND",
0x0808 : "ID_EVT_TAF_PS_CALL_PDP_DEACTIVATE_CNF",
0x0809 : "ID_EVT_TAF_PS_CALL_PDP_DEACTIVATE_IND",
0x080A : "ID_EVT_TAF_PS_CALL_PDP_DISCONNECT_IND",
0x080B : "ID_EVT_TAF_PS_CALL_PDP_IPV6_INFO_IND",
0x0831 : "ID_EVT_TAF_PS_CALL_ORIG_CNF",
0x0832 : "ID_EVT_TAF_PS_CALL_END_CNF",
0x0833 : "ID_EVT_TAF_PS_CALL_MODIFY_CNF",
0x0834 : "ID_EVT_TAF_PS_CALL_ANSWER_CNF",
0x0835 : "ID_EVT_TAF_PS_CALL_HANGUP_CNF",
}

def get_imsa_dsm_msg_str( MsgId):
    for MsgIdIndex in imsa_dsm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return imsa_dsm_msg_enum_table[MsgIdIndex]

    return "none"
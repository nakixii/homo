#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list regm nrmm msg
modify  record  :   2019-04-28 create file
"""

regm_nrmm_msg_enum_table = {
#regm->nrmm
0x00 : "ID_REGM_NRMM_REG_REQ",
0x02 : "ID_REGM_NRMM_DEREG_REQ",
0x04 : "ID_REGM_NRMM_REL_CONN_NTF",
0x06 : "ID_REGM_NRMM_LMM_REG_INFO_NTF",
0x08 : "ID_REGM_NRMM_GU_REG_INFO_NTF",
0x0A : "ID_REGM_NRMM_SRV_INFO_NTF",
0x0C : "ID_REGM_NRMM_EHRPD_PS_CALL_CHANGE_NTF",
#nrmm->regm
0x01 : "ID_NRMM_REGM_REG_RSLT_IND",
0x03 : "ID_NRMM_REGM_CONN_STATUS_IND",
0x05 : "ID_NRMM_REGM_DEREG_RSLT_IND",
0x07 : "ID_NRMM_REGM_REG_CNF",
0x09 : "ID_NRMM_REGM_DEREG_CNF",
0x0B : "ID_NRMM_REGM_SRV_REJ_IND",
0x0D : "ID_NRMM_REGM_MM_INFO_IND",
0x0F : "ID_NRMM_REGM_NSSAI_CHANGE_IND",
0x11 : "ID_NRMM_REGM_SMS_OVER_NAS_AVAIL_IND",
}

def get_regm_nrmm_msg_str( MsgId):
    for MsgIdIndex in regm_nrmm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return regm_nrmm_msg_enum_table[MsgIdIndex]

    return "none"
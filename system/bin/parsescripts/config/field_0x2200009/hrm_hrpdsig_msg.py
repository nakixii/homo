#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list hrm hrpdsig msg
modify  record  :   2016-04-27 create file
"""

hrm_hrpdsig_msg_enum_table = {
0x3500 : "ID_CTTF_CNAS_HRPD_SNP_DATA_CNF",
0x3501 : "ID_CNAS_CTTF_HRPD_SNP_DATA_REQ",
0x3502 : "ID_CTTF_CNAS_HRPD_SNP_DATA_IND",
0x3503 : "ID_NAS_CTTF_HRPD_SNP_DATA_CANCEL_REQ",
}

def get_hrm_hrpdsig_msg_str( MsgId):
    for MsgIdIndex in hrm_hrpdsig_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return hrm_hrpdsig_msg_enum_table[MsgIdIndex]

    return "none"
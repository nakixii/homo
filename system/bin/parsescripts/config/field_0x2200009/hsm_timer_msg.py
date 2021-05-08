#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list hsm timer msg
modify  record  :   2016-04-27 create file
"""

hsm_timer_msg_enum_table = {
0x00 : "TI_CNAS_HSM_WAIT_SCP_ACTIVE_CNF",
0x01 : "TI_CNAS_HSM_UATI_REQUEST_WAIT_SNP_DATA_CNF",
0x02 : "TI_CNAS_HSM_SESSION_CLOSE_WAIT_SNP_DATA_CNF",
0x03 : "TI_CNAS_HSM_UATI_COMPLETE_WAIT_SNP_DATA_CNF",
0x04 : "TI_CNAS_HSM_MO_KEEP_ALIVE_WAIT_SNP_DATA_CNF",
0x05 : "TI_CNAS_HSM_MT_KEEP_ALIVE_WAIT_SNP_DATA_CNF",
0x06 : "TI_CNAS_HSM_HARDWARE_ID_RSP_WAIT_SNP_DATA_CNF",
0x07 : "TI_CNAS_HSM_WAIT_UATI_ASSIGN",
0x08 : "TI_CNAS_HSM_ADDRESS_TIMER",
0x09 : "TI_CNAS_HSM_KEEP_ALIVE_TIMER",
0x0A : "TI_CNAS_HSM_WAIT_HRPD_CONN_CLOSE_IND",
0x0B : "TI_CNAS_HSM_WAIT_HRPD_CONN_OPEN_IND",
0x0C : "TI_CNAS_HSM_WAIT_SCP_DEACTIVE_CNF",
0x0D : "TI_CNAS_HSM_UATI_AND_SESSION_ACT_PROTECT_TIMER",
0x0E : "TI_CNAS_HSM_WAIT_PA_RAT_MODE_NTF",
0x0F : "TI_CNAS_HSM_WAIT_CARD_READ_CNF",
0x10 : "TI_CNAS_HSM_WAIT_KEEP_ALIVE_RSP",
0x11 : "TI_CNAS_HSM_WAIT_UATI_CMPL_SND_IND",
}

def get_hsm_timer_msg_str( MsgId):
    for MsgIdIndex in hsm_timer_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return hsm_timer_msg_enum_table[MsgIdIndex]

    return "none"
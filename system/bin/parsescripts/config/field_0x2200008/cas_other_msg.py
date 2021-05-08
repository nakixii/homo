#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list cas other msg
modify  record  :   2016-05-23 create file
"""

cas_other_msg_enum_table = {
    0x9001 :     "ID_OM_ERR_LOG_CTRL_IND",
	0x9002 :     "ID_OM_ERR_LOG_REPORT_REQ",
	0x9003 :     "ID_OM_ERR_LOG_REPORT_CNF",
	0x9009 :     "ID_OM_FAULT_ERR_LOG_IND",
    
	0x0000 :     "ID_CAS_RFUSER_HRPD_RESOURCE_APPLY_CNF",
	0x0001 :     "ID_CAS_RFUSER_HRPD_RESOURCE_OCCUPY_IND",
	0x0002 :     "ID_CAS_RFUSER_HRPD_RESOURCE_RESET_IND",
    0x0003 :     "ID_RFUSER_CAS_HRPD_RESOURCE_APPLY_REQ",	
    0x0004 :     "ID_RFUSER_CAS_HRPD_RESOURCE_REL_NTF",
    0x0005 :     "ID_RFUSER_CAS_HRPD_RESOURCE_OCCUPY_RSP",
    0x0006 :     "ID_CAS_RFUSER_HRPD_RESOURCE_CHECK_IND",
    0x2595 :     "ID_IMSA_CAS_1X_QUALITY_CFG_REQ",
    0x25b5 :     "ID_CAS_IMSA_1X_QUALITY_CFG_CNF",
    0x25b5 :     "ID_CAS_IMSA_1X_STATE_IND",

    0x000E :     "ID_RRC_MTC_USING_FREQ_IND",
    0x0016 :     "ID_RRC_MTC_CAS_1X_TCH_ACTIVE_SET_UPDATE_NTF",
}

def get_cas_other_msg_str(MsgId):
    for MsgIdIndex in cas_other_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return cas_other_msg_enum_table[MsgIdIndex]

    return "unknown"
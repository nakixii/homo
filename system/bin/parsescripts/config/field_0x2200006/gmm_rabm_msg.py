#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list gmm rabm msg
modify  record  :   2016-02-01 create file
"""

gmm_rabm_msg_enum_table = {
0x0000 : "ID_RABM_GMM_REESTABLISH_REQ",
0x0001 : "ID_RABM_GMM_RAB_REL_IND",
0x0002 : "ID_RABM_GMM_ROUTING_AREA_UPDATE_RSP",
0x0003 : "ID_RABM_GMM_MML_PROC_STATUS_QRY_REQ",
0x0004 : "ID_RABM_GMM_RAB_SETUP_IND",
0x1000 : "ID_GMM_RABM_REESTABLISH_CNF",
0x1001 : "ID_GMM_RABM_SYS_SRV_CHG_IND",
0x1002 : "ID_GMM_RABM_ROUTING_AREA_UPDATE_IND",
0x1003 : "ID_GMM_RABM_MML_PROC_STATUS_QRY_CNF",
}

def get_gmm_rabm_msg_str( MsgId):
    for MsgIdIndex in gmm_rabm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return gmm_rabm_msg_enum_table[MsgIdIndex]

    return "none"
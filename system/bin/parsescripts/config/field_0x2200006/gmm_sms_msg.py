#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list gmm sms msg
modify  record  :   2016-02-01 create file
"""

gmm_sms_msg_enum_table = {
1 : "PMMSMS_EST_REQ",
5 : "PMMSMS_UNITDATA_REQ",
7 : "PMMSMS_REL_REQ",
9 : "GMMSMS_BEGIN_SESSION_NOTIFY",
0 : "GMMSMS_REG_STATE_IND",
2 : "PMMSMS_EST_CNF",
4 : "PMMSMS_UNITDATA_IND",
6 : "PMMSMS_ERROR_IND",
8 : "GMMSMS_SERVICE_STATUS_IND",
10 : "GMMSMS_END_SESSION_NOTIFY",
12 : "GMMSMS_RADIO_RESOURCE_CHECK_IND",
}

def get_gmm_sms_msg_str( MsgId):
    for MsgIdIndex in gmm_sms_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return gmm_sms_msg_enum_table[MsgIdIndex]

    return "none"
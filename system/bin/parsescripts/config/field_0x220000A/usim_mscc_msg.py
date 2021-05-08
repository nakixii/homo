#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list usim mscc msg
modify  record  :   2016-04-27 create file
"""

usim_mscc_msg_enum_table = {
0 : "USIMM_ACTIVECARD_CNF",
1 : "USIMM_INITCONTINUE_CNF",
2 : "USIMM_PROTECTRESET_CNF",
3 : "USIMM_DEACTIVECARD_CNF",
4 : "USIMM_AUTHENTICATION_CNF",
5 : "USIMM_PINHANDLE_CNF",
6 : "USIMM_UPDATEFILE_CNF",
7 : "USIMM_READFILE_CNF",
8 : "USIMM_QUERYFILE_CNF",
9 : "USIMM_STATUSCMD_CNF",
10 : "USIMM_SEARCHFILE_CNF",
11 : "USIMM_FBDNPROCESS_CNF",
12 : "USIMM_OPENCHANNEL_CNF",
13 : "USIMM_CLOSECHANNEL_CNF",
14 : "USIMM_SENDTPDUDATA_CNF",
15 : "USIMM_BSCHALLENGE_CNF",
16 : "USIMM_GENERATE_KEYVPM_CNF",
17 : "USIMM_MANAGESSD_CNF",
18 : "USIMM_STKTERMINALRSP_CNF",
19 : "USIMM_STKREFRESH_CNF",
20 : "USIMM_STKENVELOPE_CNF",
21: "USIMM_RACCESS_CNF",
22 : "USIMM_SETMUTILFILE_CNF",
100 : "USIMM_CARDSTATUS_IND",
101 : "USIMM_STKREFRESH_IND",
102 : "USIMM_STKDATA_IND",
103 : "USIMM_ECCNUMBER_IND",
104: "USIMM_VSIM_RDH_IND",
105 : "USIMM_HOTINOUT_IND",
}

def get_usim_mscc_msg_str( MsgId):
    for MsgIdIndex in usim_mscc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return usim_mscc_msg_enum_table[MsgIdIndex]

    return "none"
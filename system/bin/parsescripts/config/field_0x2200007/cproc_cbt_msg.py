#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list cproc cbt msg
modify  record  :   2016-03-10 create file
"""

cproc_cbt_msg_enum_table = {
    0x2000 :     "ID_CBT_CPROC_LONG_CODE_CFG_REQ",                                                      
    0x2001 :     "ID_CPROC_CBT_1X_LONG_CODE_CFG_CNF",                                                   
    0x2002 :     "ID_CBT_CPROC_1X_REL_ALL_REQ",                                                         
    0x2003 :     "ID_CPROC_CBT_1X_REL_ALL_CNF",                                                         
    0x2008 :     "ID_CBT_CPROC_1X_SET_WORK_MODE_REQ",                                                   
    0x2009 :     "ID_CPROC_CBT_1X_SET_WORK_MODE_CNF",                                                                                        
    0x2040 :     "ID_CBT_CPROC_1X_SIGNAL_LEVEL_REQ",                                      
    0x2041 :     "ID_CPROC_CBT_1X_SIGNAL_LEVEL_CNF",                                                                    
    0x204E :     "ID_CBT_CPROC_1X_PILOT_SEARCH_REQ",                                      
    0x204F :     "ID_CPROC_CBT_1X_PILOT_SEARCH_IND",                                                                      
    0x2051 :     "ID_CPROC_CBT_1X_ACTION_IND",                                          
    0x2059 :     "ID_CBT_CPROC_1X_TCH_CONFIG_REQ",                                        
    0x205A :     "ID_CPROC_CBT_1X_TCH_CONFIG_CNF",                                                                       
    0x2063 :     "ID_CPROC_CBT_1X_SET_TIMING_CNF",                                        
    0x2064 :     "ID_CBT_CPROC_1X_SET_TIMING_REQ",    
    0x2065 :     "ID_CBT_CPROC_1X_PWRCTRL_CONFIG_REQ",                                    
    0x2066 :     "ID_CPROC_CBT_1X_PWRCTRL_CONFIG_CNF",    
    0x2FF0 :     "ID_CBT_CPROC_1X_SET_POWER_REQ",
    0x2FF1 :     "ID_CPROC_CBT_1X_SET_POWER_CNF",
    0x2FF3 :     "ID_CSDR_CCBT_1X_DDR_RAM_BASE_ADDR_IND",
    0xD242 :     "ID_OAM_PHY_SET_WORK_MODE_REQ",
    0x2D42 :     "ID_PHY_OAM_SET_WORK_MODE_CNF",
    0x0059 :     "ID_CPROC_CBT_1X_FER_MEAS_REPORT_IND",
}

def get_cproc_cbt_msg_str( MsgId, usVersion):
    for MsgIdIndex in cproc_cbt_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return cproc_cbt_msg_enum_table[MsgIdIndex]

    return "unknown"

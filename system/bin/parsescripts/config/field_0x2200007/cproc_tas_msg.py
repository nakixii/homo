#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list cproc ctas msg
modify  record  :   2016-03-10 create file
"""

cproc_tas_msg_enum_table = {
    0x23A0 :     "ID_CPROC_CTAS_MEAS_REQ",                                                      
    0x23A1 :     "ID_CPROC_CTAS_SIGNAL_LEVEL_REQ",                                                   
    0x23A2 :     "ID_CPROC_CTAS_SIGNAL_LEVEL_RESULT_RSP",                                                         
    0x23A3 :     "ID_CPROC_CTAS_STATE_REQ",                                                         
    0x23A4 :     "ID_CPROC_CTAS_WORK_MODE_REQ",                                                   
    0x23A5 :     "ID_CTAS_CPROC_SIGNAL_LEVEL_IND",                                                                                        
    0x23A6 :     "ID_CTAS_CPROC_SIGNAL_LEVEL_RESULT_IND",                                      
    0x23A7 :     "ID_CPROC_CTAS_RELEASE_ALL_REQ",                                                                    
    0x23A8 :     "ID_CTAS_CPROC_RELEASE_ALL_CNF",                                      
    0x23A9 :     "ID_CPROC_CTAS_PILOT_SEARCH_REQ",                                                                      
    0x23AA :     "ID_CPROC_CTAS_PILOT_SEARCH_DONE_REQ",                                          
    0x23AB :     "ID_CPROC_CTAS_PILOT_SEARCH_FAIL_REQ",                                        
    0x23AC :     "ID_CTAS_CPROC_PILOT_SEARCH_COMPLETE_IND",                                                                       
    0x23AD :     "ID_CTAS_CPROC_PILOT_SEARCH_RESTART_IND",                                        
    0x23AE :     "ID_CPROC_CTAS_ANTENNA_STATUS_NTF",
    0x23AF :     "ID_CPROC_1X_CTAS_SLOTTED_FIRST_CONTINUS_MPS_NTF",
    0x23B0 :     "ID_CPROC_1X_CTAS_WAKEUP_IND",
    0x23B1 :     "ID_CPROC_1X_CTAS_ANT_LOCK_IND",
    0x23B2 :     "ID_CPROC_1X_CTAS_ANT_UNLOCK_IND",
    0x180E :     "ID_PHY_RCM_START_TAS_CNF",
    0x180F :     "ID_PHY_RCM_STOP_TAS_CNF",
    0x1810 :     "ID_PHY_RCM_SET_DPDT_CNF",
    0x1811 :     "ID_PHY_RCM_TX_BLANKING_IND",
    0x1812 :     "ID_PHY_RCM_RATMODE_IND",
    0x1814 :     "ID_PHY_RCM_ACCESS_STATE_IND",
    0x1815 :     "ID_PHY_RCM_SEARCHING_STATE_IND",
    0x1816 :     "ID_PHY_RCM_SIGNAL_STATE_IND",
    0x1817 :     "ID_PHY_RCM_IDLE_HAPPY_IND",
    0x181A :     "ID_PHY_RCM_SEARCHING_STATE_REQ",
    0x188E :     "ID_RCM_PHY_START_TAS_REQ",
    0x188F :     "ID_RCM_PHY_STOP_TAS_REQ",    
    0x1890 :     "ID_RCM_PHY_SET_DPDT_REQ",
    0x1891 :     "ID_RCM_PHY_TX_BLANKING_IND",
    0x1893 :     "ID_RCM_PHY_SEARCHING_STATE_CNF",
    0x1894 :     "ID_RCM_PHY_AGENT_SET_DPDT_REQ",
    0x1895 :     "ID_RCM_PHY_VOICE_CALL_STATE_IND",
    0x00E0 :     "ID_CTAS_CSDR_1X_SET_DPDT_REQ",
    0x00E1 :     "ID_CSDR_CTAS_1X_SET_DPDT_CNF",
    0x00E2 :     "ID_CTAS_CSDR_1X_TAS_START_REQ",
    0x00E3 :     "ID_CSDR_CTAS_1X_TAS_START_CNF",
    0x00E4 :     "ID_CSDR_CTAS_1X_TX_BLANKING_IND",
    0x00E5 :     "ID_CTAS_CSDR_1X_TX_BLANKING_IND",
    0x00E6 :     "ID_CTAS_CSDR_1X_TAS_AUTH_STATUS_IND",
}

def get_cproc_tas_msg_str(MsgId, usVersion):
    for MsgIdIndex in cproc_tas_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return cproc_tas_msg_enum_table[MsgIdIndex]

    return "unknown"

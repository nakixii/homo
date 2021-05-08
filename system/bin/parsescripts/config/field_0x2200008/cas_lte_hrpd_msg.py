#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list gas mtc msg
modify  record  :   2016-01-07 create file
"""

cas_lte_hrpd_msg_enum_table = {
    0x0000 :     "ID_CAS_LRRC_HRPD_IDLE_MEAS_REQ",      
    0x0001 :     "ID_LRRC_CAS_HRPD_IDLE_MEAS_CNF",      
    0x0002 :     "ID_LRRC_CAS_HRPD_IDLE_MEAS_IND",      
    0x0003 :     "ID_CAS_LRRC_HRPD_IDLE_RESEL_REQ",     
    0x0004 :     "ID_LRRC_CAS_HRPD_IDLE_RESEL_CNF",     
    0x0005 :     "ID_CAS_LRRC_HRPD_IDLE_RESEL_STOP_REQ",
    0x0006 :     "ID_LRRC_CAS_HRPD_IDLE_RESEL_STOP_CNF",
    0x0007 :     "ID_CAS_LRRC_HRPD_BSR_REQ",            
    0x0008 :     "ID_LRRC_CAS_HRPD_BSR_CNF",            
    0x0009 :     "ID_LRRC_CAS_HRPD_BSR_IND",            
    0x000A :     "ID_CAS_LRRC_HRPD_BSR_STOP_REQ",       
    0x000B :     "ID_LRRC_CAS_HRPD_BSR_STOP_CNF",       
    0x000C :     "ID_CAS_LRRC_HRPD_REL_ALL_REQ",        
    0x000D :     "ID_LRRC_CAS_HRPD_REL_ALL_CNF",        
    0x000E :     "ID_LRRC_CAS_HRPD_REL_ALL_REQ",        
    0x000F :     "ID_CAS_LRRC_HRPD_REL_ALL_CNF",        
    0x0010 :     "ID_LRRC_CAS_HRPD_IDLE_MEAS_REQ",      
    0x0011 :     "ID_CAS_LRRC_HRPD_IDLE_MEAS_CNF",      
    0x0012 :     "ID_CAS_LRRC_HRPD_IDLE_MEAS_IND",      
    0x0013 :     "ID_LRRC_CAS_HRPD_CONNECTED_MEAS_REQ", 
    0x0014 :     "ID_CAS_LRRC_HRPD_CONNECTED_MEAS_CNF", 
    0x0015 :     "ID_CAS_LRRC_HRPD_CONNECTED_MEAS_IND", 
    0x0016 :     "ID_LRRC_CAS_HRPD_IDLE_RESEL_REQ",     
    0x0017 :     "ID_CAS_LRRC_HRPD_IDLE_RESEL_CNF",     
    0x0018 :     "ID_LRRC_CAS_HRPD_RESEL_STOP_REQ",     
    0x0019 :     "ID_CAS_LRRC_HRPD_RESEL_STOP_CNF",     
    0x001A :     "ID_LRRC_CAS_HRPD_REDIRECT_REQ",       
    0x001B :     "ID_CAS_LRRC_HRPD_REDIRECT_CNF",       
    0x001C :     "ID_LRRC_CAS_HRPD_REDIRECT_STOP_REQ",  
    0x001D :     "ID_CAS_LRRC_HRPD_REDIRECT_STOP_CNF",  
    0x001E :     "ID_LRRC_CAS_HRPD_BSR_REQ",            
    0x001F :     "ID_CAS_LRRC_HRPD_BSR_CNF",            
    0x0020 :     "ID_CAS_LRRC_HRPD_BSR_IND",            
    0x0021 :     "ID_LRRC_CAS_HRPD_BSR_STOP_REQ",         
    0x0022 :     "ID_CAS_LRRC_HRPD_BSR_STOP_CNF",       
    0x0023 :     "ID_LRRC_CAS_HRPD_BSR_SUSPEND_REQ",    
    0x0024 :     "ID_CAS_LRRC_HRPD_BSR_SUSPEND_CNF",    
    0x0025 :     "ID_LRRC_CAS_HRPD_BSR_RESUME_REQ",     
    0x0026 :     "ID_CAS_LRRC_HRPD_BSR_RESUME_CNF", 
}

def get_cas_lte_hrpd_msg_str( MsgId):
    for MsgIdIndex in cas_lte_hrpd_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return cas_lte_hrpd_msg_enum_table[MsgIdIndex]

    return "unknown"
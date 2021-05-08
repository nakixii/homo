#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list gas mta msg
modify  record  :   2016-01-07 create file
"""

cas_cproc_hrpd_msg_enum_table = {   
    0x4200 :     "ID_CAS_CPROC_HRPD_RESET_REQ",                
    0x4201 :     "ID_CPROC_CAS_HRPD_RESET_CNF",                
    0x4202 :     "ID_CAS_CPROC_HRPD_SET_MODE_REQ",             
    0x4203 :     "ID_CPROC_CAS_HRPD_SET_MODE_CNF",             
    0x4204 :     "ID_CPROC_CAS_HRPD_WAKEUP_IND",               
    0x4205 :     "ID_CPROC_CAS_HRPD_SLEEP_IND",                
    0x4206 :     "ID_CAS_CPROC_HRPD_CC_CONFIG_REQ",            
    0x4207 :     "ID_CPROC_CAS_HRPD_CC_CONFIG_CNF",            
    0x4208 :     "ID_CPROC_CAS_HRPD_ACTIVE_CELL_IND",          
    0x4209 :     "ID_CAS_CPROC_HRPD_SEARCH_PILOT_REQ",         
    0x420A :     "ID_CPROC_CAS_HRPD_SEARCH_PILOT_IND",         
    0x420B :     "ID_CAS_CPROC_HRPD_SEARCH_PILOT_STOP_REQ",    
    0x420C :     "ID_CPROC_CAS_HRPD_SEARCH_PILOT_STOP_CNF",    
    0x420D :     "ID_CAS_CPROC_HRPD_SYSTIME_UPDATE_REQ",       
    0x420E :     "ID_CPROC_CAS_HRPD_SYSTIME_UPDATE_IND",       
    0x420F :     "ID_CPROC_CAS_HRPD_ERROR_IND",                
    0x4210 :     "ID_CPROC_CAS_HRPD_NO_RF_IND",                
    0x4211 :     "ID_CPROC_CAS_HRPD_RF_IND",                   
    0x4212 :     "ID_CAS_CPROC_HRPD_LTE_MEAS_REQ",             
    0x4213 :     "ID_CPROC_CAS_HRPD_LTE_MEAS_CNF",             
    0x4214 :     "ID_CAS_CPROC_HRPD_STOP_LTE_MEAS_REQ",        
    0x4215 :     "ID_CPROC_CAS_HRPD_STOP_LTE_MEAS_CNF",        
    0x4216 :     "ID_CAS_CPROC_HRPD_LTE_BSR_REQ",             
    0x4217 :     "ID_CPROC_CAS_HRPD_LTE_BSR_CNF",              
    0x4218 :     "ID_CAS_CPROC_HRPD_STOP_LTE_BSR_REQ",        
    0x4219 :     "ID_CPROC_CAS_HRPD_STOP_LTE_BSR_CNF",         
    0x421A :     "ID_CAS_CPROC_HRPD_READ_LTE_NL_REQ",          
    0x421B :     "ID_CPROC_CAS_HRPD_READ_LTE_NL_CNF",          
    0x421C :     "ID_CAS_CPROC_HRPD_STOP_LTE_NL_REQ",          
    0x421D :     "ID_CPROC_CAS_HRPD_STOP_LTE_NL_CNF",          
    0x421E :     "ID_CAS_CPROC_HRPD_REL_ALL_REQ",              
    0x421F :     "ID_CPROC_CAS_HRPD_REL_ALL_CNF",                
    0x4220 :     "ID_CAS_CPROC_HRPD_SEARCH_PILOT_SUSPEND_REQ", 
    0x4221 :     "ID_CPROC_CAS_HRPD_SEARCH_PILOT_SUSPEND_CNF", 
    0x4222 :     "ID_CAS_CPROC_HRPD_SEARCH_PILOT_RESUME_REQ",  
    0x4223 :     "ID_CPROC_CAS_HRPD_SEARCH_PILOT_RESUME_CNF",  
    0x4224 :     "ID_CAS_CPROC_HRPD_CC_STOP_REQ",              
    0x4225 :     "ID_CPROC_CAS_HRPD_CC_STOP_CNF",              
    0x4226 :     "ID_CAS_CPROC_HRPD_TIME_SYNC_REQ",            
    0x4227 :     "ID_CPROC_CAS_HRPD_TIME_SYNC_IND",            
    0x4228 :     "ID_CAS_CPROC_HRPD_CONNECTION_STATUS_REQ",    
    0x4229 :     "ID_CAS_CPROC_HRPD_TCH_FLOW_STATUS_REQ", 
    0x422A :     "ID_CAS_CPROC_HRPD_OHM_NOT_CURRENT_IND",
    0x422B :     "ID_CAS_CPROC_HRPD_OHM_CURRENT_IND",	
    0x4600 :     "ID_CAS_CPROC_HRPD_MEAS_PILOTSET_REQ",        
    0x4601 :     "ID_CPROC_CAS_HRPD_MEAS_PILOTSET_CNF",        
    0x4602 :     "ID_CPROC_CAS_HRPD_MEAS_PILOTSET_IND",    
}

def get_cas_cproc_hrpd_msg_str( MsgId):
    for MsgIdIndex in cas_cproc_hrpd_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return cas_cproc_hrpd_msg_enum_table[MsgIdIndex]

    return "unknown"
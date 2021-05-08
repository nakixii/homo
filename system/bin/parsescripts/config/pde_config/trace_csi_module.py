#!/usr/bin/env python3
# coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename
# * Description   analysis bin mini dump
# * Version       1.0
# * Data          2019.6.28
#***********************************************************************

#csi module info name and info data list

csi_info_name_list = [
                        "LOAD_PRE",  #0x0
                        "ISR_PDMA",
                        "ISR_PE_LOAD",
                        "ISR_AP_LOAD",
                        "ISR_IPC0",
                        "ISR_IPC1",
                        "LOAD_PRE_OK",
                        "LOAD_PARA0",
                        "LOAD_PARA1",
                        "LOAD_PARA2",
                        "LOAD_PARA3",
                        "LOAD_PARA4",
                        "CSI_RPT0",
                        "CSI_RPT1",
                        "CSI_RPT2",
                        "CSI_PDMA",
                        "CSI_CHE0",
                        "CSI_CHE1",
                        "CSI_PROC0",
                        "CSI_PROC1",
                        "CSI_STOP_IPC0",
                        "CSI_STOP_IPC1",
                        "CSI_PWR_DOWN_IPC0",
                        "CSI_PWR_DOWN_IPC1",
                        "CSI_DROP0",
      			"CSI_DROP1",
      			"CSI_DROP2",
      			"CSI_DROP3",
      			"CSI_DROP4",
      			"CSI_DROP5",
      			"CSI_DROP6",
      			"CSI_DROP7",
      			"CSI_DIF0",
      			"CSI_DIF1",
      			"CSI_DIF2",
      			"CSI_DIF3",

                      ]

csi_info_data_list = [	#low bit to high bit
                        #load_pre 
                        ["slot_id","cc_idx","RSV", "RSV","RSV"],
                        [8 ,4, 8, 12, 32],
                        #isr_pdma  
                        ["pdma_int","sub_id","RSV", "RSV","RSV"],
                        [4 , 16, 12, 32],
                        #isr_pe_load   
                        ["cc_idx","slot_id","sst_slot_id","RSV","RSV"],
                        [4 , 8, 8, 12, 32],
                        #isr_ap_load   
                        ["cc_idx","csi_process_flag","RSV", "RSV","RSV"],
                        [4 , 1, 15, 12, 32],
                        #isr_ipc0    
                        ["ipc_reg_value_l","RSV", "RSV","RSV"],
                        [16 , 4, 15, 12, 32],
                        #isr_ipc1    
                        ["ipc_reg_value_h","RSV", "RSV","RSV"],
                        [16 , 4, 15, 12, 32],
                        #load_pre_ok  
                        ["slot_id","cc_idx","RSV", "RSV","RSV"],
                        [8 ,4, 8, 12, 32],
                        #load_para0    
                        ["slot_id","cc_idx","RSV", "RSV","RSV"],
                        [8 ,4, 8, 12, 32],
                        #load_para1    
                        ["slot_id","cc_idx","RSV", "RSV","RSV"],
                        [8 ,4, 8, 12, 32],
                        #load_para2    
                        ["slot_id","cc_idx","RSV", "RSV","RSV"],
                        [8 ,4, 8, 12, 32],
                        #load_para3    
                        ["slot_id","cc_idx","RSV", "RSV","RSV"],
                        [8 ,4, 8, 12, 32],
                        #load_para4    
                        ["rpt_idx","res_idx","cc_idx","slot_id","rpt_attri","rlm_en","RSV", "RSV","RSV"],
                        [2 , 4, 2 , 8, 2, 1, 1, 12, 32],
                        #CSI_RPT0    
                        ["rpt_flag0","cc_idx","RSV", "RSV","RSV"],
                        [12 ,4, 4, 12, 32],
                        #csi_rpt1    
                        ["rpt_flag1","cc_idx","RSV", "RSV","RSV"],
                        [12 ,4, 4, 12, 32],
                        #csi_rpt2    
                        ["rpt_idx","slot_id","cc_idx","RSV", "RSV","RSV"],
                        [4 ,8, 4, 4, 12, 32],
                        #csi_pdma    
                        ["RSV", "RSV","RSV"],
                        [20, 12, 32],
                        #csi_che0    
                        ["res_idx","slot_id","cc_idx","RSV", "RSV","RSV"],
                        [4 ,8, 4, 4, 12, 32],
                        #csi_che1    
                        ["res_idx","RSV","cc_idx","RSV", "RSV","RSV"],
                        [4 ,8, 4, 4, 12, 32],
                        #csi_proc0    
                        ["cmr_idx","rpt_idx","cc_idx","RSV", "RSV","RSV"],
                        [4 ,4, 4, 1, 7, 12, 32],
                        #csi_proc1    
                        ["cmr_idx","rpt_idx","cc_idx","pe_en","RSV", "RSV","RSV"],
                        [4 ,4, 4, 8, 12, 32],
                        #csi_stop_ipc0      
                        ["en","RSV", "RSV","RSV"],
                        [1 , 19, 12, 32],
                        #csi_stop_ipc1                      
                        ["cc_idx","RSV", "RSV","RSV"],
                        [4 , 16, 12, 32],
                        #csi_pwr_down_ipc0     
                        ["en","RSV", "RSV","RSV"],
                        [1 , 19, 12, 32],
                        #csi_pwr_down_ipc1     
                        ["cc_idx","RSV", "RSV","RSV"],
                        [4 , 16, 12, 32],
                        #csi_drop0    
                        ["en","RSV", "RSV","RSV"],
                        [1 , 19, 12, 32],
                        #csi_drop1    
                        ["g_ap_csi_cnt0","g_ap_csi_cnt1","RSV", "RSV","RSV"],
                        [1 ,1, 18, 12, 32],
                        #csi_drop2    
                        ["g_ap_csi_cnt0","g_ap_csi_cnt1","g_ap_csi_cnt2","g_ap_csi_cnt3","RSV", "RSV","RSV"],
                        [1 , 1, 1, 1, 16, 12, 32],
                        #csi_drop3    
                        ["en","RSV", "RSV","RSV"],
                        [1 , 19, 12, 32],
                        #csi_drop4    
                        ["en","RSV", "RSV","RSV"],
                        [1 , 19, 12, 32],
                        #csi_drop5    
                        ["en","RSV", "RSV","RSV"],
                        [1 , 19, 12, 32],
                        #csi_drop6    
                        ["rpt_idx","res_idx","cc_idx","slot_id","RSV", "RSV","RSV"],
                        [2 , 4, 2 , 8, 4, 12, 32],
                        #csi_drop7    
                        ["rpt_idx","res_idx","cc_idx","slot_id","RSV", "RSV","RSV"],
                        [2 , 4, 2 , 8, 4, 12, 32],
                        #dif ctl info,  CSI_DIF0, over slot -2, total 20bits dat
                        ["over_res_rpt_idx","res_idx","cc_idx","slot_id","RSV", "RSV","RSV"],
                        [2 ,4, 2, 8, 4, 12, 32],
			#dif ctl info,  CSI_DIF1, over -16 symbol   
                        ["over_res_rpt_idx","res_idx","cc_idx","slot_id","over_flag", "RSV","RSV"],
                        [2 ,4, 2, 7, 5, 12, 32],
			#dif ctl info,  CSI_DIF2, dif en    
                        ["res_idx", "cc_idx","cfg_prio","RSV", "RSV","RSV"],
                        [4 ,2, 2, 8, 12, 32],
			#dif ctl info,  CSI_DIF3, enable res    
                        ["res_port_l0", "res_idx","cc_idx","slot_id", "RSV","RSV"],
                        [4 ,4, 2, 10, 12, 32],
                      ]



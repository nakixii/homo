#!/usr/bin/env python3
# coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename
# * Description   analysis bin mini dump
# * Version       1.0
# * Data          2019.6.28
#***********************************************************************

#pdf module info name and info data list

pdf_info_name_list = [
                        "RSV",
                        "FUNC_PDF_INFO_INIT",
                        "FUNC_PDC_T1",
                        "FUNC_PDC_T2",
                        "FUNC_PDC_TASK1",
                        "FUNC_PDC_TASK2",
                        "FUNC_PDS_TS_JUDGE_DCH",
                        "FUNC_PDS_TS_JUDGE_BCH",
                        "FUNC_CHE_T1",
                        "FUNC_CHE_T2",
                        "FUNC_PDS_PTRS",
                        "FUNC_PDS_T2",
                        "FUNC_PDS_H",
                        "FUNC_PDS_CH_FREE",
                        "FUNC_PDF_POS_FREE_PDS_DCH",
                        "FUNC_PDF_POS_FREE_PDS_BCH",
                        "FUNC_PDF_POS_FREE_PDS_TS",
                        "FUNC_FREE_MUTEX_PDF",
                        "FUNC_PDE_FLUSH_TASK",
                        "FUNC_PDE_SOFT_HALT",
                        "FUNC_PDF_IPC_HANDLER",
                        "FUNC_PDF_POWER_DOWN_TASK",
                        "FUNC_NCHE_DIF_TOP",
                        "FUNC_NPDS_SCH_TASK1_TOP",
                        "FUNC_NCHE_DIF_WARN_HANDLER",
                      ]

pdf_info_data_list = [	#low bit to high bit
                        ["RSV","RSV"],
                        [32,32],
                        ["flush_flag","zebu_en"],
                        [32,32],
                        ["color_id_state","rsv"],
                        [32,32],
                        ["flush_flag","rsv"],
                        [32,32],
                        ["pdc_task_num","in_out_flag"],
                        [32,32],
                        ["pdc_task_cnt","in_out_flag"],
                        [32,32],
                        ["in_out_flag","latest_group_id","latest_slot_idx","rsv","latest_dch_bitmap","latest_bch_bitmap"],
                        [8,8,8,8,16,16],
                        ["in_out_flag","latest_group_id","latest_slot_idx","rsv","latest_dch_bitmap","latest_bch_bitmap"],
                        [8,8,8,8,16,16],
                        ["mutex_st_pds_ch","rsv"],
                        [32,32],
                        ["ch_task_num(hi_8)_ch_task_cnt(lo_8)","rsv"],
                        [32,32],
                        ["flush_flag","rsv"],
                        [32,32],
                        ["task_num(hi_8)_task_cnt(lo_8)","rsv"],
                        [32,32],     
                        ["dch_task_cnt","dch_task_num","dch_task_size","bch_task_cnt","bch_task_num","bch_task_size"],
                        [8,8,16,8,8,16],
                        ["info_num","pos_sem_status","ch_type","rsv"],
                        [8,8,16,32],
                        ["mutex_st_pds_dch","rsv"],
                        [32,32],
                        ["mutex_st_pds_bch","rsv"],
                        [32,32],
                        ["pds_ts_color","rsv"],
                        [32,32],
                        ["mutex_type","in_out_flag"],
                        [32,32],
                        ["flush_task_info","in_out_flag"],
                        [32,32],
                        ["RSV","RSV"],
                        [32,32],
                        ["ipc_stat","soft_halt_en"],
                        [32,32],  
                        ["power_down_task","in_out_flag"],
                        [32,32],   
                        ["ch0_task_num","ch1_task_num","ch2_task_num","p_event"],
                        [8,8,16,32],        
                        ["p_event","dch_task_num","bch_task_num","in_out_flag"],
                        [8,8,16,32],    
                        ["che_warn_flag","RSV"],
                        [32,32],
                      ]



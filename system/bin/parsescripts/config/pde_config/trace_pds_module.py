#!/usr/bin/env python3
# coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename
# * Description   analysis bin mini dump
# * Version       1.0
# * Data          2019.6.28
#***********************************************************************

#pds module info mane and info data list

pds_info_name_list = [
                        "NPDS_STEP1_FID_SLOT_CH0_INFO",  #0x0
                        "NPDS_STEP1_FID_SLOT_CH1_INFO",  #0x8
                        "NPDS_STEP1_FID_SLOT_CH2_INFO",  #0x10
                        "NPDS_STEP2_FID_SLOT_CH0_INFO",  #0x18
                        "NPDS_STEP2_FID_SLOT_CH1_INFO",  #0x20
                        "NPDS_STEP2_FID_SLOT_CH2_INFO",  #0x28
                        "NPDS_STEP3_FID_SLOT_CH0_INFO",  #0x30
                        "NPDS_STEP3_FID_SLOT_CH1_INFO",  #0x38
                        "NPDS_STEP3_FID_SLOT_CH2_INFO",  #0x40
                        "NPDS_STEP4_FID_TASK_INFO",  #0x48
                        "NPDS_STEP7_FID_TASK_INFO",  #0x50
                        ]
pds_info_data_list = [  #low bit to high bit
                        ["ch_intf", "ch_pos_info", "i32channelvalid_0", "i32channelvalid_1", "i32channelvalid_2", "task_ch_cnt", "comm_idx", "coef_idx", "ptrs_idx", "ptrs_calc_en", "rx_num", "rsv", "RSV"],
                        [2, 2, 1, 1, 1, 4, 2, 2, 2, 1, 2, 12, 32],           #NPDS_STEP1_FID_SLOT_CH0_INFO
                        ["ch_intf", "ch_pos_info", "i32channelvalid_0", "i32channelvalid_1", "i32channelvalid_2", "task_ch_cnt", "comm_idx", "coef_idx", "ptrs_idx", "ptrs_calc_en", "rx_num", "rsv", "RSV"],
                        [2, 2, 1, 1, 1, 4, 2, 2, 2, 1, 2, 12, 32],           #NPDS_STEP1_FID_SLOT_CH1_INFO
                        ["ch_intf", "ch_pos_info", "i32channelvalid_0", "i32channelvalid_1", "i32channelvalid_2", "task_ch_cnt", "comm_idx", "coef_idx", "ptrs_idx", "ptrs_calc_en", "rx_num", "rsv", "RSV"],
                        [2, 2, 1, 1, 1, 4, 2, 2, 2, 1, 2, 12, 32],           #NPDS_STEP1_FID_SLOT_CH2_INFO
                        ["task_ch_cnt", "demap_store_flag", "fcross_task_cnt", "fcross_en", "fcross_chanid", "i32sym_end", "fst_ch_idx", "init_ch_idx", "demap_down_flag", "bch_info_updata", "task_num", "task_cnt", "bch_task_num", "dch_task_num", "fst_sum_dci_blk", "init_dci_blk", "sym_dci_blk_tmp", "i32sym_id", "task_num_up_flag", "RSV"],
                        [3, 1, 2, 1, 2, 1, 2, 2, 1, 1, 8, 8, 8, 8, 3, 3, 3, 4, 1, 2],           #NPDS_STEP2_FID_SLOT_CH0_INFO
                        ["task_ch_cnt", "demap_store_flag", "fcross_task_cnt", "fcross_en", "fcross_chanid", "i32sym_end", "fst_ch_idx", "init_ch_idx", "demap_down_flag", "bch_info_updata", "task_num", "task_cnt", "bch_task_num", "dch_task_num", "fst_sum_dci_blk", "init_dci_blk", "sym_dci_blk_tmp", "i32sym_id", "task_num_up_flag", "RSV"],
                        [3, 1, 2, 1, 2, 1, 2, 2, 1, 1, 8, 8, 8, 8, 3, 3, 3, 4, 1, 2],           #NPDS_STEP2_FID_SLOT_CH1_INFO
                        ["task_ch_cnt", "demap_store_flag", "fcross_task_cnt", "fcross_en", "fcross_chanid", "i32sym_end", "fst_ch_idx", "init_ch_idx", "demap_down_flag", "bch_info_updata", "task_num", "task_cnt", "bch_task_num", "dch_task_num", "fst_sum_dci_blk", "init_dci_blk", "sym_dci_blk_tmp", "i32sym_id", "task_num_up_flag", "RSV"],
                        [3, 1, 2, 1, 2, 1, 2, 2, 1, 1, 8, 8, 8, 8, 3, 3, 3, 4, 1, 2],           #NPDS_STEP2_FID_SLOT_CH2_INFO
                        ["i32slot_start", "i32ch_act_flag", "i32task_id", "mini_flag", "i32_ch_idx", "rsv", "RSV"],
                        [1, 1, 4, 1, 2, 23, 32],           #NPDS_STEP3_FID_SLOT_CH0_INFO
                        ["i32slot_start", "i32ch_act_flag", "i32task_id", "mini_flag", "i32_ch_idx", "rsv", "RSV"],
                        [1, 1, 4, 1, 2, 23, 32],           #NPDS_STEP3_FID_SLOT_CH1_INFO
                        ["i32slot_start", "i32ch_act_flag", "i32task_id", "mini_flag", "i32_ch_idx", "rsv", "RSV"],
                        [1, 1, 4, 1, 2, 23, 32],           #NPDS_STEP3_FID_SLOT_CH2_INFO
                        ["i32task_index", "task_start_sym", "first_sym_index", "sym_num", "total_sym_num", "i32symid", "blk_done_num", "blk_valid_num", "blk_left_num", "i32ch_blk_num", "i32sym_end", "i32demap_refresh", "bch_blk_num", "dch_blk_num", "i64slot_end", "RSV"],
                        [6, 4, 4, 4, 4, 4, 3, 3, 4, 2, 1, 1, 8, 8, 1, 7],           #NPDS_STEP4_FID_TASK_INFO
                        ["task_start_sym", "first_sym_index", "sym_num", "total_sym_num", "i32symid", "blk_done_num", "blk_valid_num", "i32demap_refresh", "i32sym_end", "i64slot_end", "blk_left_num", "i32ch_blk_num", "bch_blk_num", "dch_blk_num", "fcross_discard", "RSV"],
                        [4, 4, 4, 4, 4, 4, 4, 1, 1, 2, 4, 4, 8, 8, 1, 7],           #NPDS_STEP7_FID_TASK_INFO
                     ]

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

che_info_name_list = [
                        "PDS_DIF_MSG",  #0x0
                        "PDS_DIF_MSG_END",  #0x8
                        "PDS_PDMA_MSG",  #0x10
                        "PDS_PDMA_MSG_END",  #0x18
                        "PDS_NCHE_MSG_END",  #0x20
                        ]
che_info_data_list = [  #low bit to high bit
                        ["nche_start_flag", "rsv"],
                        [32, 32],           #PDS_DIF_MSG
                        ["nche_dif_end_flag", "channel_type", "weiner_cfc_updflag", "noise_wiener_cfc_updflag", "nche_work_en", "wn_work_en", "ruu_mode", "bund_size", "pattern_flag", "port_mode", "symb_num", "rpt0_cfc_inv_flag", "rpt0_cfc_inv_flag_pat2", "real_to_en", "pre_to_en", "wn_coef_sel", "rsv"],
                        [32, 2, 1, 1, 1, 1, 1, 2, 1, 1, 3, 1, 1, 1, 1, 1, 13],           #PDS_DIF_MSG_END
                        ["nche_pdma_isr_start_cnt", "rsv"],
                        [32, 32],           #PDS_PDMA_MSG
                        ["nche_pdma_isr_end_cnt", "channel_type", "mini_flag"],
                        [32, 2, 30],           #PDS_PDMA_MSG_END
                        ["nche_end_flag", "rsv"],
                        [32, 32],           #PDS_NCHE_MSG_END
                     ]

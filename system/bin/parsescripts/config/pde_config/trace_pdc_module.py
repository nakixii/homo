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

pdc_info_name_list = [
                        "PDC_INFO_T1_INTR",  #0x0
                        "PDC_INFO_T2_NUM0",  #0x8
                        "PDC_INFO_T2_NUM1",  #0x10
                        "PDC_INFO_T1_STATE",  #0x18
                        "PDC_INFO_T2_START",  #0x20
                        "PDC_INFO_CORESET",  #0x28
                        "PDC_INFO_CHEDEM",  #0x30
                        "PDC_INFO_BDSlotCnt",  #0x38
                        "PDC_INFO_BDSlotLast",  #0x40
                        "PDC_INFO_DCI",  #0x48
                        ]
pdc_info_data_list = [  #low bit to high bit
                        ["pEvent_t1", "rsv"],
                        [32, 32],           #PDC_INFO_T1_INTR
                        ["t2_num0", "rsv"],
                        [32, 32],           #PDC_INFO_T2_NUM0
                        ["t2_num1", "rsv"],
                        [32, 32],           #PDC_INFO_T2_NUM1
                        ["t1_state", "rsv"],
                        [32, 32],           #PDC_INFO_T1_STATE
                        ["pEvent_t2", "pdc_task_cnt", "pdc_task_num", "rsv"],
                        [4, 4, 24, 32],           #PDC_INFO_T2_START
                        ["CoresetStartSymCurr", "CoresetIdx", "CoresetSlotCnt", "rsv"],
                        [4, 4, 24, 32],           #PDC_INFO_CORESET
                        ["chedem_flag", "rsv"],
                        [32, 32],           #PDC_INFO_CHEDEM
                        ["BdSlotCnt", "rsv"],
                        [32, 32],           #PDC_INFO_BDSlotCnt
                        ["BdSlotLast", "rsv"],
                        [32, 32],           #PDC_INFO_BDSlotLast
                        ["dl_dci_num", "ul_dci_num", "rsv", "rsv"],
                        [8, 8, 16, 32],           #PDC_INFO_DCI
                     ]

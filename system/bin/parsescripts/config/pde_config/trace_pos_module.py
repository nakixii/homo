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

pos_info_name_list = [
                        "POS_INFO_INIT",  #0x0
                        "POS_INFO_START",  #0x8
                        "POS_INFO_REG_FUNC",  #0x10
                        "POS_INFO_APPLY_COLOR_TASK",  #0x18
                        "POS_INFO_ACCEPT_TASK",  #0x20
                        "POS_INFO_ACCEPT_COLOR",  #0x28
                        "POS_INFO_SUBMIT_COLOR_TASK",  #0x30
                        "POS_INFO_SUBMIT_MONO_TASK",  #0x38
                        "POS_INFO_SUBMIT_NORM_TASK",  #0x40
                        "POS_INFO_SEM_STATUS",  #0x48
                        "POS_INFO_SEM_CREATE",  #0x50
                        "POS_INFO_SEM_DESTROY",  #0x58
                        "POS_INFO_SEM_UP_USR",  #0x60
                        "POS_INFO_SEM_RENINIT",  #0x68
                        "POS_INFO_SEM_DOWN",  #0x70
                        "POS_INFO_SEM_UP",  #0x78
                        "POS_INFO_CORE_S",  #0x80
                        "POS_INFO_CORE_E",  #0x88
                        "POS_INFO_INV_ALL_TASK",  #0x90
                        "POS_INFO_INV_TASK",  #0x98
                        "POS_INFO_GET_TASK_IDX",  #0xA0
                        "POS_INFO_GET_COLOR",  #0xA8
                        "POS_INFO_SEM_COLOR",  #0xB0
                        "POS_INFO_LOG_SWITCH",  #0xB8
                        ]
pos_info_data_list = [  #low bit to high bit
                        ["status", "rsv"],
                        [32, 32],           #POS_INFO_INIT
                        ["status", "rsv"],
                        [32, 32],           #POS_INFO_START
                        ["assert_fid", "assert_prio", "fid", "priority", "func"],
                        [8, 8, 8, 8, 32],           #POS_INFO_REG_FUNC
                        ["fid", "sem_id", "color", "action", "param"],
                        [8, 8, 8, 8, 32],           #POS_INFO_APPLY_COLOR_TASK
                        ["tsk_idx", "prio", "cluster_idx", "write_pointer", "cluster_pending"],
                        [8, 8, 8, 8, 32],           #POS_INFO_ACCEPT_TASK
                        ["task_indx_0", "task_indx_1", "task_indx_2", "task_indx_3", "task_indx_4", "task_indx_5", "num", "cluster_pending"],
                        [8, 8, 8, 8, 8, 8, 8, 8],           #POS_INFO_ACCEPT_COLOR
                        ["fid", "sem_id", "color", "action", "write_pointer", "prio", "cluster_pending", "param"],
                        [4, 4, 4, 4, 8, 4, 4, 32],           #POS_INFO_SUBMIT_COLOR_TASK
                        ["fid", "sem_id", "action", "prio", "write_pointer", "cluster_pending", "param"],
                        [4, 4, 4, 4, 8, 8, 32],           #POS_INFO_SUBMIT_MONO_TASK
                        ["tsk_idx", "prio", "fid", "write_pointer", "cluster_pending", "param"],
                        [5, 3, 8, 8, 8, 32],           #POS_INFO_SUBMIT_NORM_TASK
                        ["sem_id", "sem_cnt", "rsv"],
                        [8, 24, 32],           #POS_INFO_SEM_STATUS
                        ["sem_id", "assert_sem_id", "sem_free_bitmap"],
                        [8, 24, 32],           #POS_INFO_SEM_CREATE
                        ["sem_id", "assert_sem_id", "assert_sem_cnt", "sem_free_bitmap"],
                        [8, 8, 16, 32],           #POS_INFO_SEM_DESTROY
                        ["task_stack_top", "tsk_idx", "action", "sem_id", "rsv"],
                        [8, 8, 8, 8, 32],           #POS_INFO_SEM_UP_USR
                        ["status", "type", "sem_id", "rel_color_num", "rel_tsk_num", "rel_tsk_0_indx", "rel_tsk_1_indx", "rel_tsk_2_indx", "rel_tsk_3_indx"],
                        [4, 4, 8, 8, 8, 8, 8, 8, 8],           #POS_INFO_SEM_RENINIT
                        ["status", "tsk_idx", "rsv", "write_pointer", "sem_id", "color_tsk_it", "owner", "sem_cnt"],
                        [8, 8, 8, 8, 8, 8, 8, 8],           #POS_INFO_SEM_DOWN
                        ["status", "color", "sem_id", "read_pointer", "new_owner_id", "blocked_info", "blocked_num"],
                        [8, 8, 8, 8, 8, 8, 16],           #POS_INFO_SEM_UP
                        ["highest_prio", "read_pointer", "tsk_idx", "status", "func", "param"],
                        [3, 5, 5, 3, 16, 32],           #POS_INFO_CORE_S
                        ["status", "task_idx", "cluster_pending", "clus_idx"],
                        [8, 24, 8, 24],           #POS_INFO_CORE_E
                        ["status", "rsv"],
                        [32, 32],           #POS_INFO_INV_ALL_TASK
                        ["tsk_idx", "rsv"],
                        [32, 32],           #POS_INFO_INV_TASK
                        ["task_stack_top", "tsk_idx", "rsv"],
                        [8, 24, 32],           #POS_INFO_GET_TASK_IDX
                        ["assert_color", "color", "rsv"],
                        [8, 24, 32],           #POS_INFO_GET_COLOR
                        ["sem_id", "owner", "rsv"],
                        [8, 24, 32],           #POS_INFO_SEM_COLOR
                        ["on_or_off", "connect_or_switch"],
                        [32, 32],           #POS_INFO_LOG_SWITCH
                     ]

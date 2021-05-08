#!/usr/bin/env python3
# coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename
# * Description   analysis bin mini dump
# * Version       1.0
# * Data          2019.6.28
#***********************************************************************

import re
import os


list_pde_seg_name   = [ 
						"version_info_cc0",
						"dm_dbg_info_cc0",
						"pdf_info_cc0",
						"trace_cc0",
						"stack_parse_cc0",
						"version_info_cc1",
						"dm_dbg_info_cc1",
						"pdf_info_cc1",
						"trace_cc1",
						"stack_parse_cc1",

						"version_info_csi_cc0",
						"dm_dbg_info_csi_cc0",
						"tag_info_csi_cc0"
						"trace_csi_cc0",
						"stack_parse_csi_cc0",
						]

list_pde_seg_len    = [
						"0x20",
						"0x28",
						"0xb8",		
						"0x810",
						"0x200",

						"0x20",
						"0x28",
						"0xb8",		
						"0x810",
						"0x200",

						"0x20",
						"0x20",
						"0x08",		
						"0x800",
						"0x200",
					   ]
#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   analysis guas dump bin
modify  record  :   2016-01-07 create file
"""

import os
import sys
import string
from analysis_guas_dump_info import analysis_guas_dump_info
from analysis_gas_dump_info import analysis_gas_dump_info
from vers_ctrl import analysis_guas_debug_version
from vers_ctrl import MACRO_VERSION_TRUNK


########################################################################################
def entry_0x2200004(infile, field, offset, len, version, mode, outfile):
    file_offset = eval(offset)
    # #######check parameter start#############
    if not field == '0x2200004':
        print('hidis field is ', field)
        print('current field is', '0x2200004')
        return error['ERR_CHECK_FIELD']
    elif not version == '0x0000':
        print('hidis version is ', version)
        print('current version is ', '0x0000')
        return error['ERR_CHECK_VERSION']
    elif not (len == '0x2800' \
        or len == '0x1800' \
        or len == '0x1000' \
        or len == '0x800'):
        print('hids len is ', len)
        print('current len is ', '0x4000')
        return error['ERR_CHECK_LEN']

    # ##### analysis guas debug version ########
    ver_name, ver_no = analysis_guas_debug_version(
        infile, file_offset, outfile)

    if MACRO_VERSION_TRUNK == ver_name.lower():
        ret = analysis_gas_dump_info(infile, offset, outfile, ver_no)
    else:
        ret = analysis_guas_dump_info(infile, offset, outfile, ver_no)

    return 0

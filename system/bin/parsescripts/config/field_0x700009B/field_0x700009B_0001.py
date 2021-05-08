#!/usr/bin/env python3
# coding=utf-8
# -*- coding: utf-8 -*-
# ***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename
# * Description   analysis regs dump
# * Version       1.0
# * Data          2019.6.28
# *
# ***********************************************************************
import struct
import os
import sys
import string
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from field_eicc import eicc_parse_v1


def entry_0x700009B(infile, field, offset, length, version, mode, outfile):
    try:
        outfile.write(('[MDM NR EICC INFO PARSE]\r\n'))
        field_off = eval(offset)
        field_len = eval(length)
        infile.seek(field_off)
        dumpinfo = eicc_parse_v1.EiccDumpInfo()
        dumpinfo.parse(infile, field_off, field_len)
        outfile.write(dumpinfo.get_plain_txt())
        outfile.write(
            ('[MDM NR EICC INFO PARSE COMPLETED]\r\n'))
        return 0

    except Exception as ex:
        print(str(ex))
        outfile.writelines(str(ex)+"\r\n")
        outfile.write(
            ('[MDM NR EICC INFO PARSE FAILED]\r\n'))
        return 0

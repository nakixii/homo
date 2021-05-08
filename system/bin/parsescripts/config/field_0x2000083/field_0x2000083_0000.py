#!/usr/bin/env python3
# coding=utf-8
# -*- coding: utf-8 -*-
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename
# * Description   analysis seminfo dump
# * Version       1.0
# * Data          2019.6.28
#***********************************************************************
import struct
import os
import sys
import string

def PrintSemInfo(infile, field, offset, slen, version, mode, outfile):
        addr = 0
        row = 0
        i = 0
        MyOffset = eval(offset)
        infile.seek(MyOffset)
        print("got entry 0x2000083 PrintSemInfo")
        outfile.writelines("count      owner      semmode    semtype\n")
        for i in range(0, int(int(slen,16)/16)):
            (count, owner, semmode, semtype, ) = struct.unpack("IIII", infile.read(16))
            if 0x00000000 != owner:
                outfile.writelines("0x%08x 0x%08x 0x%08x 0x%08x\n" %(count, owner, semmode, semtype))
        return

def entry_0x2000083(infile, field, offset, slen, version, mode, outfile):
        try:
            if not field == '0x2000083':
                print('hidis field is ', field)
                print('current field is', '0x2000083')
                return error['ERR_CHECK_FIELD']
            elif not version == '0x0000':
                print('hidis version is ', version)
                print('current version is ', '0x0000')
                return error['ERR_CHECK_VERSION']
            elif not slen == '0x2800':
                print('hids len is ', slen)
                print('current len is ', '0x2800')
                return error['ERR_CHECK_LEN']
            print("got entry 0x2000083")
            PrintSemInfo(infile, field, offset, slen, version, mode, outfile)
            return 0

        except Exception as e:
            print(str(e))
            outfile.writelines(str(e))
            return 1

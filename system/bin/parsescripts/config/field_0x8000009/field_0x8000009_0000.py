#!/usr/bin/env python3
# coding=utf-8
# -*- coding: utf-8 -*-
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename
# * Description   analysis reg dump
# * Version       1.0
# * Data          2019.6.28
#***********************************************************************
import struct
import os
import sys
import string

def PrintRegs(infile, field, offset, slen, version, mode, outfile):
        addr = 0
        row = 0
        i = 0
        MyOffset = eval(offset)
        infile.seek(MyOffset)
        print("got entry 0x2000009 PrintRegs")
        (g_reg_addr, ) = struct.unpack('I',infile.read(4))
        (g_reg_size, ) = struct.unpack('I',infile.read(4))
        (g_rsv, ) = struct.unpack('I',infile.read(4))
        (g_rsv1, ) = struct.unpack('I',infile.read(4))
        outfile.writelines("reg_addr      :0x%x\n" % g_reg_addr)
        outfile.writelines("reg_size      :0x%x\n" % g_reg_size)
        outfile.writelines("reserve       :0x%x\n" % g_rsv)
        outfile.writelines("reserve1      :0x%x\n" % g_rsv1)
        outfile.writelines("offset      data\n")
        for i in range(0, int((int(slen,16) - 16)/16)):
            (charbyte1, charbyte2, charbyte3,charbyte4, ) = struct.unpack("IIII", infile.read(16))
            addr = 0x10 * row
            row = row + 1
            #print >> outhandler, "0x%08x: %08x %08x %08x %08x" %(addr, charbyte1, charbyte2, charbyte3, charbyte4)
            outfile.writelines("0x%08x: %08x %08x %08x %08x\n" %(addr, charbyte1, charbyte2, charbyte3, charbyte4))
        return

def entry_0x8000009(infile, field, offset, slen, version, mode, outfile):
        try:
            if not field == '0x8000009':
                print('hidis field is ', field)
                print('current field is', '0x8000009')
                return error['ERR_CHECK_FIELD']
            elif not version == '0x0000':
                print('hidis version is ', version)
                print('current version is ', '0x0000')
                return error['ERR_CHECK_VERSION']
            elif not slen == '0x1000':
                print('hids len is ', slen)
                print('current len is ', '0x1000')
                return error['ERR_CHECK_LEN']
            print("got entry 0x8000009")
            PrintRegs(infile, field, offset, slen, version, mode, outfile)
            return 0

        except Exception as e:
                print(str(e))
                outfile.writelines(str(e))
                return 1

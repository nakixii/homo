#!/usr/bin/env python3
# coding=utf-8
# -*- coding: utf-8 -*-
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename
# * Description   analysis dmesg dump
# * Version       1.0
# * Data          2019.6.28
# * 
#***********************************************************************
import struct
import os
import sys
import string

def PrintExcInfo(infile, field, offset, slen, version, mode, outfile):
        MyOffset = eval(offset)
        infile.seek(MyOffset)
        (g_magic, ) = struct.unpack('I',infile.read(4))
        (g_write, ) = struct.unpack('I',infile.read(4))
        (g_read, ) = struct.unpack('I',infile.read(4))
        (g_size, ) = struct.unpack('I',infile.read(4))
        (g_app_is_active, ) = struct.unpack('I',infile.read(4))
        (g_logged_chars, ) = struct.unpack('I',infile.read(4))
        (g_w_mark, ) = struct.unpack('i',infile.read(4))
        (g_reserved, ) = struct.unpack('i',infile.read(4))
        (g_log_buf, ) = struct.unpack('I',infile.read(4))
        if g_magic==0x52524554:
                outfile.writelines("Ring Buffer Write Offset    :0x%x\n" % g_write)
                outfile.writelines("Ring Buffer Read Offset     :0x%x\n" % g_read)
                outfile.writelines("Ring Buffer Size            :0x%x\n" % g_size)
                outfile.writelines("app_is_active               :%u\n" % g_app_is_active)
                outfile.writelines("Log Chars Num               :0x%x\n" % g_logged_chars)
                outfile.writelines("Water Mark                  :0x%x\n" % g_w_mark)
                outfile.writelines("Data Area                   :0x%x\n" % g_log_buf)
                outfile.writelines("-----------------------------\n")
                MyLen = int(slen,16) - 36
                for i in range(0, MyLen):
                    tag = infile.readline(1)
                    if tag >= b'\x20' and tag <= b'\x7E':
                        outfile.writelines(tag.decode(encoding="utf-8"))
                    elif tag == b'\x0A':
                        outfile.writelines('\n')
                outfile.writelines("dmesg end\n")
                return
        #print("got entry 0x4000027 PrintExcInfo dot 2")
        outfile.writelines('magic %u is wrong' % g_magic)
        return
 	
def entry_0x4000027(infile, field, offset, slen, version, mode, outfile):
        try:
            if not field == '0x4000027':
                print('hidis field is ', field)
                print('current field is', '0x4000027')
                return error['ERR_CHECK_FIELD']
            elif not version == '0x0000':
                print('hidis version is ', version)
                print('current version is ', '0x0000')
                return error['ERR_CHECK_VERSION']
            elif not slen == '0x1000':
                print('hids len is ', slen)
                print('current len is ', '0x1000')
            #print("got entry 0x4000027")
            PrintExcInfo(infile, field, offset, slen, version, mode, outfile)
            return 0

        except Exception as e:
            print(str(e))
            outfile.writelines(str(e))
            return 1

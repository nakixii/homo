#!/usr/bin/env python3
# coding=utf-8
# Copyright (C) Huawei Technologies Co., Ltd. 2010-2018. All rights reserved.

import struct
import os
import sys
import string
    
def PrintTaskName(infile, field, offset, slen, version, mode, outfile):
        MyOffset = eval(offset)
        infile.seek(MyOffset)
        print("got entry 0x30F0005 PrintTaskName")
        (g_maxnum, ) = struct.unpack('I',infile.read(4))
        (g_front, ) = struct.unpack('I',infile.read(4))
        (g_rear, ) = struct.unpack('I',infile.read(4))
        (g_num, ) = struct.unpack('I',infile.read(4))
        outfile.writelines("maxnum          :0x%x\n" % g_maxnum)
        outfile.writelines("front                :0x%x\n" % g_front)
        outfile.writelines("rear                :0x%x\n" % g_rear)
        outfile.writelines("num                :%u\n" % g_num)
        itemcnt = int(g_num/4)
        print("got entry 0x30F0005 PrintTaskName dot 1, itemcnt is %d" %(itemcnt))
        outfile.writelines("taskid taskname\n")
        for i in range(0, itemcnt):
            (g_taskid, ) = struct.unpack('I',infile.read(4))
            g_taskName = infile.read(12)
            strTaskName = g_taskName.decode(encoding="utf-8")
            outfile.writelines("0x%x   %s\n" %(g_taskid, strTaskName[:strTaskName.find('\x00')]))
        return
 	
def entry_0x30F0005(infile, field, offset, slen, version, mode, outfile):
        try:
            if not field == '0x30F0005':
                print('hidis field is ', field)
                print('current field is', '0x30F0005')
                return error['ERR_CHECK_FIELD']
            elif not version == '0x0000':
                print('hidis version is ', version)
                print('current version is ', '0x0000')
                return error['ERR_CHECK_VERSION']
            elif not slen == '0x2000':
                print('hids len is ', slen)
                print('current len is ', '0x2000')
            print("got entry 0x30F0005")
            print(offset)
            PrintTaskName(infile, field, offset, slen, version, mode, outfile)
            return 0

        except Exception as e:
            print(str(e))
            outfile.writelines(str(e))
            return 1

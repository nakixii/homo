#!/usr/bin/env python3
# coding=utf-8
# -*- coding: utf-8 -*-
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename
# * Description   analysis debug dump
# * Version       1.0
# * Data          2019.6.28
#***********************************************************************
import struct
import os
import sys
import string

def PrintDumpDebug(infile, field, offset, slen, version, mode, outfile):
        MyOffset = eval(offset)
        infile.seek(MyOffset)
        #print(MyOffset)
        #print("got entry 0x2000090 PrintDumpDebug normal_debug_queue")
        (g_magic, ) = struct.unpack('I',infile.read(4))
        (g_maxnum, ) = struct.unpack('I',infile.read(4))
        (g_front, ) = struct.unpack('I',infile.read(4))
        (g_rear, ) = struct.unpack('I',infile.read(4))
        (g_num, ) = struct.unpack('I',infile.read(4))
        (g_data, ) = struct.unpack('I',infile.read(4))
        if g_magic==0xabcd6789:
                outfile.writelines("normal_debug_queue magic    :0x%x\n" % g_magic)
                outfile.writelines("maxnum        :0x%x\n" % g_maxnum)
                outfile.writelines("front              :0x%x\n" % g_front)
                outfile.writelines("rear               :0x%x\n" % g_rear)
                outfile.writelines("num               :%u\n" % g_num)
                outfile.writelines("data               :0x%x\n" % g_data)
                itemcnt = int(g_num/2)
                #print("got entry 0x2000090 PrintDumpDebug dot 1, itemcnt is %d" %(itemcnt))
                outfile.writelines("step         data\n")
                for i in range(0, itemcnt):
                    (g_step, ) = struct.unpack('I',infile.read(4))
                    (g_data, ) = struct.unpack('I',infile.read(4))
                    outfile.writelines("0x%08x   0x%08x\n" %(g_step, g_data))
        else:
            #print("got entry 0x2000090 PrintDumpDebug dot 2")
            outfile.writelines('magic %u is wrong' % g_magic)

        MyOffset = MyOffset + 768
        infile.seek(MyOffset)
        #print(MyOffset)
        (g_magic, ) = struct.unpack('I',infile.read(4))
        (g_maxnum, ) = struct.unpack('I',infile.read(4))
        (g_front, ) = struct.unpack('I',infile.read(4))
        (g_rear, ) = struct.unpack('I',infile.read(4))
        (g_num, ) = struct.unpack('I',infile.read(4))
        (g_data, ) = struct.unpack('I',infile.read(4))
        if g_magic==0xabcd6789:
                outfile.writelines("ipc_debug_queue magic    :0x%x\n" % g_magic)
                outfile.writelines("maxnum         :0x%x\n" % g_maxnum)
                outfile.writelines("front               :0x%x\n" % g_front)
                outfile.writelines("rear                :0x%x\n" % g_rear)
                outfile.writelines("num                :%u\n" % g_num)
                outfile.writelines("data                :0x%x\n" % g_data)
                itemcnt = int(g_num/2)
                #print("got entry 0x2000090 PrintDumpDebug dot 3, itemcnt is %d" %(itemcnt))
                outfile.writelines("step     data\n")
                for i in range(0, itemcnt):
                    (g_step, ) = struct.unpack('I',infile.read(4))
                    (g_data, ) = struct.unpack('I',infile.read(4))
                    outfile.writelines("0x%08x   0x%08x\n" %(g_step, g_data))
        else:
            #print("got entry 0x2000090 PrintDumpDebug dot 4")
            outfile.writelines('magic %u is wrong' % g_magic)

        MyOffset = MyOffset + 640
        infile.seek(MyOffset)
        #print(MyOffset)
        (g_magic, ) = struct.unpack('I',infile.read(4))
        #print(g_magic)
        (g_maxnum, ) = struct.unpack('I',infile.read(4))
        (g_front, ) = struct.unpack('I',infile.read(4))
        (g_rear, ) = struct.unpack('I',infile.read(4))
        (g_num, ) = struct.unpack('I',infile.read(4))
        (g_data, ) = struct.unpack('I',infile.read(4))
        if g_magic==0xabcd6789:
                outfile.writelines("fiq_debug_queue magic    :0x%x\n" % g_magic)
                outfile.writelines("maxnum      :0x%x\n" % g_maxnum)
                outfile.writelines("front            :0x%x\n" % g_front)
                outfile.writelines("rear             :0x%x\n" % g_rear)
                outfile.writelines("num             :%u\n" % g_num)
                outfile.writelines("data             :0x%x\n" % g_data)
                itemcnt = int(g_num/2)
                #print("got entry 0x2000090 PrintDumpDebug dot 5, itemcnt is %d" %(itemcnt))
                outfile.writelines("step     data\n")
                for i in range(0, itemcnt):
                    (g_step, ) = struct.unpack('I',infile.read(4))
                    (g_data, ) = struct.unpack('I',infile.read(4))
                    outfile.writelines("0x%08x   0x%08x\n" %(g_step, g_data))
        else:
            #print("got entry 0x2000090 PrintDumpDebug dot 6")
            outfile.writelines('magic %u is wrong' % g_magic)

        return

def entry_0x2000090(infile, field, offset, slen, version, mode, outfile):
        try:
            if not field == '0x2000090':
                print('hidis field is ', field)
                print('current field is', '0x2000090')
                return error['ERR_CHECK_FIELD']
            elif not version == '0x0000':
                print('hidis version is ', version)
                print('current version is ', '0x0000')
                return error['ERR_CHECK_VERSION']
            #print("got entry 0x2000090")
            PrintDumpDebug(infile, field, offset, slen, version, mode, outfile)
            return 0

        except Exception as e:
            print(str(e))
            outfile.writelines(str(e))
            return 1

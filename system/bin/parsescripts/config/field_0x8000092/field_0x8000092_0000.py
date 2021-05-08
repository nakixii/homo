#!/usr/bin/env python3
# coding=utf-8
# -*- coding: utf-8 -*-
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename
# * Description   analysis rebootcontext dump
# * Version       1.0
# * Data          2019.6.28
#***********************************************************************
import struct
import os
import sys
import string
import config

def PrintRebootContextInfo(infile, field, offset, length, version, mode, outfile):
        MyOffset = eval(offset)
        infile.seek(MyOffset)
        (g_cpu0_reboot_context, ) = struct.unpack('I',infile.read(4))
        (g_cpu0_reboot_task, ) = struct.unpack('I',infile.read(4))
        g_cpu0_taskName = infile.read(16)
        (g_cpu0_reboot_int, ) = struct.unpack('I',infile.read(4))
        (g_cpu1_reboot_context, ) = struct.unpack('I',infile.read(4))
        (g_cpu1_reboot_task, ) = struct.unpack('I',infile.read(4))
        g_cpu1_taskName = infile.read(16)
        (g_cpu1_reboot_int, ) = struct.unpack('I',infile.read(4))

        for i in range(0, config.get_core_num()):
            outfile.writelines("reboot_context  cpu%d      :0x%x\n" % ( i, g_cpu0_reboot_context))
            outfile.writelines("reboot_task  cpu%d           :0x%x\n" % ( i,g_cpu0_reboot_task))
            outfile.writelines("taskName     cpu%d          :%s\n" % ( i, g_cpu0_taskName.decode(encoding="utf-8").strip('\x00')))
            outfile.writelines("reboot_int     cpu%d          :0x%x\n" % (i, g_cpu0_reboot_int))
        return

def entry_0x8000092(infile, field, offset, length, version, mode, outfile):
        try:
            if not field == '0x8000092':
                print('hidis field is ', field)
                print('current field is', '0x8000092')
                return error['ERR_CHECK_FIELD']
            elif not version == '0x0000':
                print('hidis version is ', version)
                print('current version is ', '0x0000')
                return error['ERR_CHECK_VERSION']
            elif not length == '0x38':
                print('hids len is ', length)
                print('current len is ', '0x38')
                #return error['ERR_CHECK_LEN']
            PrintRebootContextInfo(infile, field, offset, length, version, mode, outfile)
            return 0

        except Exception as e:
            print(str(e))
            outfile.write(str(e))
            return 1

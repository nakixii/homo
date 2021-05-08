#!/usr/bin/env python3
# coding=utf-8
# -*- coding: utf-8 -*-
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename
# * Description   analysis baseinfo dump
# * Version       1.0
# * Data          2019.6.28
#***********************************************************************
import struct
import os
import sys
import string
import config

def PrintBaseInfo(infile, field, offset, slen, version, mode, outfile):
        MyOffset = eval(offset)
        infile.seek(MyOffset)
        (g_reboot_cpu, ) = struct.unpack('I',infile.read(4))
        (g_reboot_context, ) = struct.unpack('I',infile.read(4))
        (g_reboot_task, ) = struct.unpack('I',infile.read(4))
        (g_reboot_task_tcb, ) = struct.unpack('I',infile.read(4))
        g_taskName = infile.read(16)
        (g_reboot_int, ) = struct.unpack('I',infile.read(4))
        (g_reboot_time, ) = struct.unpack('I',infile.read(4))
        (g_modId, ) = struct.unpack('I',infile.read(4))
        config.errmodid = g_modId
        aaa = config.get_mntn_addr()
        #bbb = config.mntnbase
        print(aaa)
        #print(bbb)
        #print("g_modId:", g_modId)
        #print("errmodid:", config.errmodid)
        (g_arg1, ) = struct.unpack('I',infile.read(4))
        (g_arg2, ) = struct.unpack('I',infile.read(4))
        (g_arg3, ) = struct.unpack('I',infile.read(4))
        (g_arg3_length, ) = struct.unpack('I',infile.read(4))
        (g_vec, ) = struct.unpack('I',infile.read(4))
        (g_cpu_max_num, ) = struct.unpack('I',infile.read(4))
        config.corenum = g_cpu_max_num
        (g_cpu_online_num, ) = struct.unpack('I',infile.read(4))
        g_version = infile.read(32)
        g_compile_time =infile.read(32)
        g_reboot_reson = infile.read(4)
        g_base_uuid = infile.read(40)
        outfile.writelines("reboot_cpu:0x%x\n" % g_reboot_cpu)
        outfile.writelines("reboot_context:0x%x\n" % g_reboot_context)
        outfile.writelines("reboot_task:0x%x\n" % g_reboot_task)
        outfile.writelines("reboot_task_tcb:0x%x\n" % g_reboot_task_tcb)
        outfile.writelines("taskName:%s\n" % g_taskName.decode(encoding="utf-8").strip('\x00'))
        outfile.writelines("reboot_int:0x%x\n" % g_reboot_int)
        outfile.writelines("reboot_time:0x%x\n" %g_reboot_time)
        outfile.writelines("modId:0x%x\n" % g_modId)
        outfile.writelines("arg1:0x%x\n" % g_arg1)
        outfile.writelines("arg2:0x%x\n" % g_arg2)
        outfile.writelines("arg3:0x%x\n" % g_arg3)
        outfile.writelines("arg3_length:0x%x\n" % g_arg3_length)
        outfile.writelines("vec:0x%x\n" % g_vec)
        outfile.writelines("cpu_max_num:0x%x\n" % g_cpu_max_num)
        outfile.writelines("cpu_online_num:0x%x\n" % g_cpu_online_num)
        outfile.writelines("version:%s\n" % g_version.decode(encoding="utf-8").strip('\x00'))
        outfile.writelines("compile_time:%s\n" % g_compile_time.decode(encoding="utf-8").strip('\x00'))
        outfile.writelines("uuid:%s\n" % g_base_uuid.decode(encoding="utf-8").strip('\x00'))
        return

def entry_0x2F00000(infile, field, offset, slen, version, mode, outfile):
        try:
            if not field == '0x2F00000':
                print('hidis field is ', field)
                print('current field is', '0x2F00000')
                return error['ERR_CHECK_FIELD']
            elif not version == '0x0000':
                print('hidis version is ', version)
                print('current version is ', '0x0000')
                return error['ERR_CHECK_VERSION']
            elif not slen == '0x180':
                print('hids len is ', slen)
                print('current len is ', '0x180')
                return error['ERR_CHECK_LEN']
            print("got entry 0x2F00000")
            PrintBaseInfo(infile, field, offset, slen, version, mode, outfile)
            return 0

        except Exception as e:
            print(str(e))
            outfile.writelines(str(e))
            return 1

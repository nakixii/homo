#!/usr/bin/env python3
# coding=utf-8
# -*- coding: utf-8 -*-
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename
# * Description   analysis tasktcb dump
# * Version       1.0
# * Data          2019.6.28
#***********************************************************************
import struct
import os
import sys
import string

def PrintTaskTcb(infile, field, offset, slen, version, mode, outfile):
        regs = []
        MyOffset = eval(offset)
        infile.seek(MyOffset)
        print("got entry 0x2F0000E PrintTaskTcb")
        #for i in range(0, int(int(slen,16)/340)):
        for i in range(0, int(int(slen,16)/340)):

            (g_pid, ) = struct.unpack('I',infile.read(4))
            if 0xffffffff == g_pid:
                break;
            (g_core, ) = struct.unpack('I',infile.read(4))
            (g_entry, ) = struct.unpack('I',infile.read(4))
            (g_status, ) = struct.unpack('I',infile.read(4))
            (g_policy, ) = struct.unpack('I',infile.read(4))
            (g_priority, ) = struct.unpack('I',infile.read(4))
            (g_stack_base, ) = struct.unpack('I',infile.read(4))
            (g_stack_end, ) = struct.unpack('I',infile.read(4))
            (g_stack_high, ) = struct.unpack('I',infile.read(4))
            (g_stack_current, ) = struct.unpack('I',infile.read(4))

            g_name = infile.read(16)
            for j in range(0,17):
                reg, = struct.unpack('I',infile.read(4))
                if j > 12 :
                    regs.append(reg)
            #(g_regs0, g_regs1, g_regs2, g_regs3, g_regs4, g_regs5, g_regs6, g_regs7, g_regs8, g_regs9, g_regs10, g_regs11, g_regs12, g_regs13, g_regs14, g_regs15, g_regs16, ) = struct.unpack('IIIIIIIIIIIIIIIII',infile.read(4*17))
            #(g_regs0, ) = struct.unpack('IIIIIIIIIIIIIIIII',infile.read(4*17))
            (g_offset, ) = struct.unpack('I',infile.read(4))
            (g_rsv, ) = struct.unpack('I',infile.read(4))

            #g_dump_stack = infile.read(0xD0)
            outfile.writelines("pid               :0x%x\n" % g_pid)
            outfile.writelines("core             :0x%x\n" % g_core)
            outfile.writelines("entry            :0x%x\n" % g_entry)
            outfile.writelines("status           :0x%x\n" % g_status)
            outfile.writelines("policy           :0x%x\n" % g_policy)
            outfile.writelines("priority         :0x%x\n" % g_priority)
            outfile.writelines("stack_base   :0x%x\n" % g_stack_base)
            outfile.writelines("stack_end     :0x%x\n" % g_stack_end)
            outfile.writelines("stack_high    :0x%x\n" % g_stack_high)
            outfile.writelines("stack_current:0x%x\n" % g_stack_current)
            outfile.writelines("name           :%s\n" % g_name.decode(encoding="utf-8").strip('\x00'))
            outfile.writelines("Register13-16 :")
            for eachlist in regs:
                outfile.writelines("0x%x " % eachlist)
            outfile.writelines("\noffset       :0x%x\n" % g_offset)
            outfile.writelines("rsv              :0x%x\n" % g_rsv)
            #outfile.writelines("dump_stack :\n")

            for k in range(0, 0xD0):
                    tag = infile.readline(1)
            #        if tag != b'\x00':
            #            #print(tag)
            #            #print(tag.decode(encoding="utf-8"))
            #            outfile.writelines(tag.decode(encoding="utf-8"))
            outfile.writelines("\n--------------\n")
            regs = []
        return



def entry_0x2F0000E(infile, field, offset, slen, version, mode, outfile):
        try:
            if not field == '0x2F0000E':
                print('hidis field is ', field)
                print('current field is', '0x2F0000E')
                return error['ERR_CHECK_FIELD']
            elif not version == '0x0000':
                print('hidis version is ', version)
                print('current version is ', '0x0000')
                return error['ERR_CHECK_VERSION']
            elif not slen == '0x15000':
                print('hids len is ', slen)
                print('current len is ', '0x15000')
            print("got entry 0x2F0000E")
            PrintTaskTcb(infile, field, offset, slen, version, mode, outfile)
            return 0

        except Exception as e:
            print(str(e))
            outfile.writelines(str(e))
            return 1

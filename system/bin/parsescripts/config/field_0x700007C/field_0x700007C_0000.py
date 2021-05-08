#!/usr/bin/env python3
# coding=utf-8
import struct
import os
import sys
import string

def ExpaseMemDebug(infile, field, offset, len, version, mode, outfile):
        MyOffset = eval(offset)
        infile.seek(MyOffset)
        print("got entry 0x7000007C PrintMemdebug")
        outfile.writelines("【mem pool num 0,mem debug info dump】\n")
        outfile.writelines("taskpid:malloc task pid,if taskpid==0xffffffff means irq or malloc before task module ready\n")       
        outfile.writelines("cookie:malloc function pc value or special value by caller\n")
        outfile.writelines("memsize:block total size include mem ctrl info\n")
        outfile.writelines("%-12s%-15s%-20s\n" % ("taskpid", "cookie","memsize"))
        for i in range(0, int(int(len,16)/12)):
                (pid, ) = struct.unpack("I", infile.read(4))
                (lr, ) = struct.unpack("I", infile.read(4))
                (size, ) = struct.unpack("I", infile.read(4))
                outfile.writelines("0x%-08x 0x%-12x 0x%-08x\n" % (pid, lr, size))
        return
def entry_0x700007C(infile, field, offset, len, version, mode, outfile):
########check parameter start#############
    if not field == '0x700007C':
        print('hidis field is ', field)
        print('current field is', '0x7000007C')
        return error['ERR_CHECK_FIELD']
    elif not version == '0x0000':
        print('hidis version is ', version)
        print('current version is ', '0x0000')
        return error['ERR_CHECK_VERSION']
    elif len == '0x0000':
        print('hids len is ', len)
        print('current len is ', '0x00')
        return error['ERR_CHECK_LEN']
    print("got entry 0x700007C")
    ExpaseMemDebug(infile, field, offset, len, version, mode, outfile)
    return 0
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (C) Huawei Technologies Co., Ltd. 2010-2018. All rights reserved.

import sys
from config import *



def PrintBbicInfo(infile, field, offset, length, version, mode, outfile):
        addr = 0
        row = 0
        i = 0
        MyOffset = eval(offset)
        infile.seek(MyOffset)
        print("got entry 0x400002E PrintBbicInfo, length is 0x%x" %(int(length,16)))
        outfile.writelines("offset      data\n")
        for i in range(0, int(int(length,16)/16)):
            (charbyte1, charbyte2, charbyte3,charbyte4, ) = struct.unpack("IIII", infile.read(16))
            addr = 0x10 * row
            row = row + 1
            #print >> outhandler, "0x%08x: %08x %08x %08x %08x" %(addr, charbyte1, charbyte2, charbyte3, charbyte4)
            outfile.writelines("0x%08x: %08x %08x %08x %08x\n" %(addr, charbyte1, charbyte2, charbyte3, charbyte4))
        return

    
def entry_0x400002E(infile, field, offset, length, version, mode, outfile):
    if not field == '0x400002E':
        print('hidis field is ', field)
        print('current field is', '0x400002E')
        return error['ERR_CHECK_FIELD']
    elif not version == '0x0000':
        print('hidis version is ', version)
        print('current version is ', '0x0000')
        return error['ERR_CHECK_VERSION']
    elif not length == '0x800':
        print('hids len is ', length)
        print('current len is ', '0x800')
        return error['ERR_CHECK_LEN']
    print("got entry 0x400002E")
    PrintBbicInfo(infile, field, offset, length, version, mode, outfile)
    return 0
    
if __name__ == '__main__':
    entry_0x400002E(infile, field, offset, length, version, mode, outfile)

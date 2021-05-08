#!/usr/bin/env python3
#coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename      field_0x110000D_0000.py
# * Description   analysis ipf_ap dump
#***********************************************************************
'''
Created on 2014-11-14
 
@
'''
import os
import re
import struct
import sys

ipf_ap_field_def = [
     "last_rd", 
     "last_bd",
     "last_ad0",               
     "last_ad1",            
 
]

def ipf_ap_entry_parse(infile, outfile, offset):
    infile.seek(0 + offset)
    outfile.writelines("%s:\n" %(ipf_ap_field_def[0]))
    for i in range(0, 10):
        (reg, ) = struct.unpack("I", infile.read(4))
        outfile.writelines("\t\t0x%08x\n" %(reg))
    
    outfile.writelines("%s:\n" %(ipf_ap_field_def[1]))
    for i in range(0, 10):
        (reg, ) = struct.unpack("I", infile.read(4))
        outfile.writelines("\t\t0x%08x\n" %(reg))

    outfile.writelines("%s:\n" %(ipf_ap_field_def[2]))
    for i in range(0, 4):
        (reg, ) = struct.unpack("I", infile.read(4))
        outfile.writelines("\t\t0x%08x\n" %(reg))

    outfile.writelines("%s:\n" %(ipf_ap_field_def[3]))
    for i in range(0, 4):
        (reg, ) = struct.unpack("I", infile.read(4))
        outfile.writelines("\t\t0x%08x\n" %(reg))
    return

def entry_0x110000D(infile, field, offset, slen, version, mode, outfile):
        try:
            if not field == '0x110000D':
                print('hidis field is ', field)
                print('current field is', '0x110000D')
                return error['ERR_CHECK_FIELD']
            elif not version == '0x0000':
                print('hidis version is ', version)
                print('current version is ', '0x0000')
                return error['ERR_CHECK_VERSION']
            elif not slen == '0x200':
                print('hids len is ', slen)
                print('current len is ', '0x200')
                return error['ERR_CHECK_LEN']
            #outfile.writelines("got entry entry_0x110000D")
            offset_v = eval(offset)
            ipf_ap_entry_parse(infile, outfile, offset_v)
            return 0

        except Exception as e:
            print((str(e)))
            outfile.writelines(str(e))
            return 1


    

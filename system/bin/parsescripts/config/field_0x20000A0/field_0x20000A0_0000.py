#!/usr/bin/env python3
# coding=utf-8
#######################################################################################################################################
#   copyright       :   Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
#
#   filename        :   exparse_python_frame.py
#
#   description     :   hifi ccore config for exparse python sripts frame
#
#   modify  record  :   2019-11-08 create file
#
#######################################################################################################################################
import struct
import os
import sys
import string

########################################################################################
g_reset_proc_table = {
    0: ('RECEIVE_ICC'),
    1: ('WORK_BEGIN'),
    2: ('POWER_DOWN'),
    3: ('LOAD_VERIFY_IMAGE'),
    4: ('LOAD_SECTION'),
    5: ('POWER_UP'),
    6: ('WORK_FINISH'),
}

def parse_hifi_bin_resetstate(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    total_offset = 0
    (magic, ) = struct.unpack('I', infile.read(4))#magic
    (trace, ) = struct.unpack('I', infile.read(4))#trace-index
    total_offset += (4 + 4)
    outfile.writelines('first sign byte 0x%x, trace ptr 0x%x, total_offset: 0x%x\n' %(magic, trace, total_offset))
    outfile.writelines('%-20s %-20s\n' %('proc', 'timestamp'))
    trace_array = [[0] * 2 for _ in range(31)]
    for i in range(0, 31):#trace list
        (trace_array[i][0], ) = struct.unpack('I', infile.read(4)) #proc
        (trace_array[i][1], ) = struct.unpack('I', infile.read(4)) #timestamp
    trace_array.sort(key = lambda x:x[1])
    for i in range(0, 31):
        if trace_array[i][1] > 0:
            outfile.writelines('%-20s 0x%-18x\n' %(g_reset_proc_table[trace_array[i][0]], trace_array[i][1]))
    total_offset += 31 * (4 + 4)
    outfile.writelines('total_offset: 0x%x\n' %(total_offset))

########################################################################################
def entry_0x20000A0(infile, field, offset, len, version, mode, outfile):
    new_offset = eval(offset)
    outfile.writelines("(HIFI CCORE)\n")
    ########check parameter start#############
    if not field == '0x20000A0':
        print(('hids field is', field))
        print(('current field is', '0x20000A0'))
        return error['ERR_CHECK_FIELD']
    elif not version == '0x0000':
        print(('hids version is', version))
        print(('current version is', '0x0000'))
        return error['ERR_CHECK_VERSION']
    elif not len == '0x100':
        print(('hids len is', len))
        print(('current len is', '0x100'))
        return error['ERR_CHECK_LEN']
    #########check parameter end##############
    parse_hifi_bin_resetstate("resetstate_trace",infile, new_offset, outfile)
    return 0

#!/usr/bin/env python3
# coding=utf-8
#######################################################################################################################################
#   copyright       :   Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
#
#   filename        :   exparse_python_frame.py
#
#   description     :   hifi acore config for exparse python sripts frame
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
    0: ('REGIST_OK'),
    1: ('CALL_RESET'),
    2: ('RESET_WORK_BEGIN'),
    3: ('RESET_WORK_FINISH'),
    4: ('CB_WORK_BEGIN'),
    5: ('CB_WORK_FINISH'),
    6: ('RECEIVE_ICC'),
    7: ('RESET_SUCC'),
    8: ('RESET_FAIL'),
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
def entry_0x310000A(infile, field, offset, len, version, mode, outfile):
    new_offset = eval(offset)
    outfile.writelines("(HIFI ACORE)\n")
    ########check parameter start#############
    if not field == '0x310000A':
        print(('hids field is', field))
        print(('current field is', '0x310000A'))
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

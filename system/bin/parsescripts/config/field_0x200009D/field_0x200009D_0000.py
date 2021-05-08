#!/usr/bin/env python3
# coding=utf-8
#######################################################################################################################################
#   copyright       :   Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
#
#   filename        :   exparse_python_frame.py
#
#
#   description     :   rfile ccore config for exparse python sripts frame
#
#   modify  record  :   2019-08-06 create file
#
#######################################################################################################################################
import struct
import os
import sys
import string
#from config import *

global g_Rfile_CcoreOptypeEnumTable

########################################################################################
g_Rfile_CcoreHandleEnumTable = {
    0: ("CCORE_OP_IN"),
    1: ("CCORE_ICC_SEND"),
    2: ("CCORE_ICC_RECV"),
    3: ("CCORE_OP_OUT")
}

g_Rfile_CcoreOptypeEnumTable = {
    0: ("OPEN"),
    1: ("CLOSE"),
    2: ("WRITE"),
    3: ("WRITE_SYNC"),
    4: ("READ"),
    5: ("SEEK"),
    6: ("TELL"),
    7: ("REMOVE"),
    8: ("MKDIR"),
    9: ("RMDIR"),
    10: ("OPENDIR"),
    11: ("READDIR"),
    12: ("CLOSEDIR"),
    13: ("STAT"),
    14: ("ACCESS"),
    15: ("RENAME")
}

total_offset = 0

def sort_array(row, array, sort_row):
    for i in range(0, row-1):
        for j in range(0, row-1-i):
            if array[j][sort_row] > array[j+1][sort_row]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def parse_rfile_bin_op(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    struct.unpack('I', infile.read(4))#trace-index
    struct.unpack('I', infile.read(4))#trace-index
    total_offset +=  (4 + 4)
    outfile.writelines('first sign byte 0x23232323, total_offset: 0x%x\n\n' %(total_offset))
    # 10
    outfile.writelines("**************************************rfile ccore op trace**************************************\n")
    outfile.writelines('%-20s %-20s %-20s %-64s %-20s %-20s %-20s\n' %('timestamp', 'op', 'queue_cnt', 'path', 'fd', 'param1', 'param2'))
    trace_array = [[0] * 7 for _ in range(10)]
    for i in range(0, 10):#trace list
        (trace_array[i][0], )    = struct.unpack('I', infile.read(4)) #timestamp
        (trace_array[i][1], )    = struct.unpack('I', infile.read(4)) #op
        (trace_array[i][2], )    = struct.unpack('I', infile.read(4)) #queue_cnt
        (trace_array[i][3], )    = struct.unpack('64s', infile.read(64)) #path
        (trace_array[i][4], )    = struct.unpack('I', infile.read(4)) #fd
        (trace_array[i][5], )    = struct.unpack('I', infile.read(4)) #param1
        (trace_array[i][6], )    = struct.unpack('I', infile.read(4)) #param2

    sort_array(10,trace_array,0)
    for i in range(0, 10):
        if trace_array[i][0] > 0:
            new = trace_array[i][3].replace('\0',' ')
            outfile.writelines('0x%-18x %-20s %-20d %-64s %-20d 0x%-18x 0x%-18x\n' %(trace_array[i][0], g_Rfile_CcoreOptypeEnumTable[trace_array[i][1]], trace_array[i][2],
            new, trace_array[i][4], trace_array[i][5], trace_array[i][6]))

    outfile.writelines('\n\n')
    struct.unpack('I', infile.read(4))#trace-index
    total_offset +=  (10*(4+4+4+64+4+4+4) + 4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))


def parse_rfile_bin_handle(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    # 40
    outfile.writelines("**************************************rfile ccore handle trace**************************************\n")
    outfile.writelines('%-20s %-20s %-20s %-20s %-20s\n' %('timestamp', 'op', 'queue_cnt', 'state', 'ret'))
    trace_array = [[0] * 5 for _ in range(40)]
    for i in range(0, 40):#trace list
        (trace_array[i][0], )    = struct.unpack('I', infile.read(4)) #timestamp
        (trace_array[i][1], )    = struct.unpack('I', infile.read(4)) #op
        (trace_array[i][2], )    = struct.unpack('I', infile.read(4)) #queue_cnt
        (trace_array[i][3], )    = struct.unpack('I', infile.read(4)) #state
        (trace_array[i][4], )    = struct.unpack('i', infile.read(4)) #ret

    sort_array(40,trace_array,0)
    for i in range(0, 40):
        if trace_array[i][0] > 0:
            outfile.writelines('0x%-18x %-20s %-20d %-20s %-20d\n' %(trace_array[i][0], g_Rfile_CcoreOptypeEnumTable[trace_array[i][1]], trace_array[i][2],
            g_Rfile_CcoreHandleEnumTable[trace_array[i][3]], trace_array[i][4]))

    outfile.writelines('\n\n')
    struct.unpack('I', infile.read(4))#trace-index
    total_offset +=  (40*(4+4+4+4+4) + 4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))


########################################################################################
def entry_0x200009D(infile, field, offset, len, version, mode, outfile):
        new_offset = eval(offset)
        global total_offset
        ########check parameter start#############
        if not field == '0x200009D':
            print(('hidis field is', field))
            print(('current field is', '0x200009D'))
            return error['ERR_CHECK_FIELD']
        elif not version == '0x0000':
            print(('hidis version is ', version))
            print(('current version is ', '0x0000'))
            return error['ERR_CHECK_VERSION']
        elif not len == '0x800':
            print(('hids len is ', len))
            print(('current len is ', '0x800'))
        #    return error['ERR_CHECK_LEN']
        #########check parameter end##############
        parse_rfile_bin_op("op_trace",infile, new_offset + total_offset, outfile)
        parse_rfile_bin_handle("handle_trace",infile, new_offset + total_offset, outfile)
        return 0

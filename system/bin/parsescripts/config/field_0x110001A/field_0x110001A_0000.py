#!/usr/bin/env python3
# coding=utf-8
#######################################################################################################################################
#   copyright       :   Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
#
#   filename        :   exparse_python_frame.py
#
#
#   description     :   rfile acore config for exparse python sripts frame
#
#   modify  record  :   2019-08-06 create file
#
#######################################################################################################################################
import struct
import os
import sys
import string
#from config import *

global g_Rfile_AcoreOptypeEnumTable

########################################################################################
g_Rfile_AcoreHandleEnumTable = {
    0: ("ACORE_OP_IN"),
    1: ("ACORE_USER_SEND"),
    2: ("ACORE_USER_RECV"),
    3: ("ACORE_OP_OUT")
}

g_Rfile_AcoreInnerStateEnumTable = {
    0: ("RFILE_STATE_IDLE"),
    1: ("RFILE_STATE_DOING"),
    2: ("RFILE_STATE_RESET"),
    3: ("RFILE_STATE_UNINITED")
}

g_Rfile_AcoreAppStateEnumTable = {
    0: ("APP_STATE_UNINTED"),
    1: ("APP_STATE_REALEASED"),
    2: ("APP_STATE_INTING"),
    3: ("APP_STATE_DONE")
}

g_Rfile_AcoreOptypeEnumTable = {
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
    15: ("RENAME"),
    16: ("RESET"),
    17: ("OPEN_RECOVER"),
    18: ("OPENDDIR_RECOVER")
}

total_offset = 0

def sort_array(row, array, sort_row):
    for i in range(0, row-1):
        for j in range(0, row-1-i):
            if array[j][sort_row] > array[j+1][sort_row]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def parse_rfile_bin_innerstate(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    struct.unpack('I', infile.read(4))#trace-index
    struct.unpack('I', infile.read(4))#trace-index
    total_offset +=  (4 + 4)
    outfile.writelines('first sign byte 0x23232323, total_offset: 0x%x\n\n' %(total_offset))
    # 20
    outfile.writelines("**************************************rfile acore innerstate trace**************************************\n")
    outfile.writelines('%-20s %-20s\n' %('timestamp', 'state'))
    trace_array = [[0] * 2 for _ in range(20)]
    for i in range(0, 20):#trace list
        (trace_array[i][0], )    = struct.unpack('I', infile.read(4)) #timestamp
        (trace_array[i][1], )    = struct.unpack('I', infile.read(4)) #state

    sort_array(20,trace_array,0)
    for i in range(0, 20):
        if trace_array[i][0] > 0:
            outfile.writelines('0x%-18x %-20s\n' %(trace_array[i][0], g_Rfile_AcoreInnerStateEnumTable[trace_array[i][1]]))

    outfile.writelines('\n\n')
    struct.unpack('I', infile.read(4))#trace-index
    total_offset +=  (20*(4+4) + 4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))

def parse_rfile_bin_appstate(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    # 10
    outfile.writelines("**************************************rfile acore appstate trace**************************************\n")
    outfile.writelines('%-20s %-20s\n' %('timestamp', 'state'))
    trace_array = [[0] * 2 for _ in range(10)]
    for i in range(0, 10):#trace list
        (trace_array[i][0], )    = struct.unpack('I', infile.read(4)) #timestamp
        (trace_array[i][1], )    = struct.unpack('I', infile.read(4)) #state

    sort_array(10,trace_array,0)
    for i in range(0, 10):#trace list
        if trace_array[i][0] > 0:
            outfile.writelines('0x%-18x %-20s\n' %(trace_array[i][0], g_Rfile_AcoreAppStateEnumTable[trace_array[i][1]]))

    outfile.writelines('\n\n')
    struct.unpack('I', infile.read(4))#trace-index
    total_offset +=  (10*(4+4) + 4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))

def parse_rfile_bin_handle(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    # 40
    outfile.writelines("**************************************rfile acore handle trace**************************************\n")
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
            outfile.writelines('0x%-18x %-20s %-20d %-20s %-20d\n' %(trace_array[i][0], g_Rfile_AcoreOptypeEnumTable[trace_array[i][1]], trace_array[i][2],
            g_Rfile_AcoreHandleEnumTable[trace_array[i][3]], trace_array[i][4]))

    outfile.writelines('\n\n')
    struct.unpack('I', infile.read(4))#trace-index
    total_offset +=  (40*(4+4+4+4+4) + 4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))

def parse_rfile_bin_queue(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    # 20
    outfile.writelines("**************************************rfile acore queue debug**************************************\n")
    outfile.writelines('%-20s %-20s\n' %('op', 'queue_cnt'))
    trace_array = [[0] * 2 for _ in range(20)]
    for i in range(0, 20):#trace list
        (trace_array[i][0], )    = struct.unpack('I', infile.read(4)) #op
        (trace_array[i][1], )    = struct.unpack('I', infile.read(4)) #queue_cnt

    for i in range(0, 20):
        if trace_array[i][0] > 0:
            outfile.writelines('%-20s %-20d\n' %(g_Rfile_AcoreOptypeEnumTable[trace_array[i][0]], trace_array[i][1]))

    outfile.writelines('\n\n')
    total_offset +=  (20*(4+4))
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))

def parse_rfile_bin_fd(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    # 20
    outfile.writelines("**************************************rfile acore fd debug**************************************\n")
    outfile.writelines('%-20s %-20s %-20s\n' %('fd', 'offset', 'path'))
    trace_array = [[0] * 3 for _ in range(20)]
    for i in range(0, 20):#trace list
        (trace_array[i][0], )    = struct.unpack('I', infile.read(4)) #fd
        (trace_array[i][1], )    = struct.unpack('I', infile.read(4)) #offset
        (trace_array[i][2], )    = struct.unpack('64s', infile.read(64)) #path

    for i in range(0, 20):
        if trace_array[i][0] > 0:
            new = trace_array[i][2].replace('\0',' ')
            outfile.writelines('%-20d %-20d %-64s\n' %(trace_array[i][0], trace_array[i][1], new))

    outfile.writelines('\n\n')
    total_offset +=  (20*(64+4+4))
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))


########################################################################################
def entry_0x110001A(infile, field, offset, len, version, mode, outfile):
        new_offset = eval(offset)
        global total_offset
        ########check parameter start#############
        if not field == '0x110001A':
            print(('hidis field is', field))
            print(('current field is', '0x110001A'))
            return error['ERR_CHECK_FIELD']
        elif not version == '0x0000':
            print(('hidis version is ', version))
            print(('current version is ', '0x0000'))
            return error['ERR_CHECK_VERSION']
        elif not len == '0xC00':
            print(('hids len is ', len))
            print(('current len is ', '0xC00'))
        #    return error['ERR_CHECK_LEN']
        #########check parameter end##############
        parse_rfile_bin_innerstate("innerstate_trace",infile, new_offset + total_offset, outfile)
        parse_rfile_bin_appstate("appstate_trace",infile, new_offset + total_offset, outfile)
        parse_rfile_bin_handle("handle_trace",infile, new_offset + total_offset, outfile)
        parse_rfile_bin_queue("queue_dbg",infile, new_offset + total_offset, outfile)
        parse_rfile_bin_fd("fd_dbg",infile, new_offset + total_offset, outfile)
        return 0

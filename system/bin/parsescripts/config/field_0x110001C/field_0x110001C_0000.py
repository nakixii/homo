#!/usr/bin/env python3
# coding=utf-8
#######################################################################################################################################
#   copyright       :   Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
#
#   filename        :   exparse_python_frame.py
#
#
#   description     :   mloader acore config for exparse python sripts frame
#
#   modify  record  :   2019-08-06 create file
#
#######################################################################################################################################
import struct
import os
import sys
import string
#from config import *

########################################################################################

total_offset = 0
def parse_mloader_acore_handle(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    
    outfile.writelines('%-14s%-14s%-14s\n' %('start_magic', 'start_time', 'op_state'))
    (start_magic, )    = struct.unpack('I', infile.read(4))
    (start_time, )    = struct.unpack('I', infile.read(4))
    (op_state, )    = struct.unpack('I', infile.read(4))
    outfile.writelines('0x%-11x 0x%-11x 0x%-11x\n' % (start_magic, start_time, op_state))
    total_offset += 12
    outfile.writelines("[mloader_hot_patch_info]\n")
    outfile.writelines('%-14s%-20s%-20s\n' %('fail_time', 'fail_time_icc_flag', 'fail_time_icc_time'))
    (fail_time, )    = struct.unpack('I', infile.read(4))
    (fail_time_icc_flag, )    = struct.unpack('I', infile.read(4))
    (fail_time_icc_time, )    = struct.unpack('I', infile.read(4))
    outfile.writelines('0x%-11x 0x%-11x 0x%-11x\n' % (fail_time, fail_time_icc_flag, fail_time_icc_time))
    total_offset += 12
    outfile.writelines("[mloader_ccore_debug_info]\n")
    outfile.writelines('%-14s%-14s%-14s%-14s%-14s\n' %('start_time', 'state', 'hot_patch', 'cold_patch', 'end_time'))
    (start_time, )    = struct.unpack('I', infile.read(4))
    (state, )    = struct.unpack('I', infile.read(4))
    (hot_patch, )    = struct.unpack('I', infile.read(4))
    (cold_patch, )    = struct.unpack('I', infile.read(4))
    (end_time, )    = struct.unpack('I', infile.read(4))
    outfile.writelines('0x%-11x 0x%-11x 0x%-11x 0x%-11x 0x%-11x\n' % (start_time, state, hot_patch, cold_patch, end_time))
    total_offset += 20
    outfile.writelines("[mloader_ccore_images_debug_info]\n")
    outfile.writelines('%-14s%-14s%-14s%-14s%-14s\n' %('start_time', 'core_id', 'img_index', 'op', 'end_time'))
    for i in range(0, 32):#trace list
        (start_time, )    = struct.unpack('I', infile.read(4))
        (core_id, )    = struct.unpack('I', infile.read(4))
        (img_index, )    = struct.unpack('I', infile.read(4))
        (op, )    = struct.unpack('I', infile.read(4))
        (end_time, )    = struct.unpack('i', infile.read(4))
        outfile.writelines('0x%-11x 0x%-11x 0x%-11x 0x%-11x 0x%-11x\n' % (start_time, core_id, img_index, op, end_time))
    total_offset += (20 * 32)
    outfile.writelines('%-14s%-14s\n' %('end_time', 'end_magic'))
    (end_time, )    = struct.unpack('I', infile.read(4))
    (end_magic, )    = struct.unpack('I', infile.read(4))
    outfile.writelines('0x%-11x 0x%-11x\n' % (end_time, end_magic))
    total_offset += 8
    outfile.writelines('total_offset: 0x%x\n' %(total_offset))
    outfile.writelines("==MLOADER ACORE==\n")
    outfile.writelines('\n\n')

########################################################################################
def entry_0x110001C(infile, field, offset, len, version, mode, outfile):
        new_offset = eval(offset)
        global total_offset
        outfile.writelines("==MLOADER ACORE==\n")
        ########check parameter start#############
        if not field == '0x110001C':
            print(('hidis field is', field))
            print(('current field is', '0x110001C'))
            return error['ERR_CHECK_FIELD']
        elif not version == '0x0000':
            print(('hidis version is ', version))
            print(('current version is ', '0x0000'))
            return error['ERR_CHECK_VERSION']
        elif not len == '0x400':
            print(('hids len is ', len))
            print(('current len is ', '0x400'))
            return error['ERR_CHECK_LEN']
        #########check parameter end##############
        parse_mloader_acore_handle("mloader_acore",infile, new_offset, outfile)
        
        return 0


# def main():
#     if len(sys.argv) < 2:
#         print("invalid argument")
#         return
#     else:
#         infile = sys.argv[1]
#         field = sys.argv[2]
#         offset = sys.argv[3]
#         length = sys.argv[4]
#         version = sys.argv[5]
#         mode = sys.argv[6]
#         outfile = sys.argv[7]
    
#     my_infile = open(infile,"rb")
#     my_outfile = open(outfile, "w")
#     entry_0x110001C(my_infile, field, offset, length, version, mode, my_outfile)
#     my_infile.close()
#     my_outfile.close()

# if __name__ == '__main__':
#     main()

#python3 field_0x110001C_0000.py rdr.bin 0x110001C 0x7bfa4 0x400 0x0000 1 out.txt
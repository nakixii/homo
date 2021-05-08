#!/usr/bin/env python3
# coding=utf-8
#######################################################################################################################################
#   copyright       :   Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
#
#   filename        :   exparse_python_frame.py
#
#
#   description     :   mloader ccore config for exparse python sripts frame
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
def parse_mloader_ccore_handle(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    
    print('%-14s%-14s\n' %('start_magic', 'fail_time'))
    outfile.writelines('%-14s%-14s\n' %('start_magic', 'fail_time'))
    (start_magic, )    = struct.unpack('I', infile.read(4))
    (fail_time, )    = struct.unpack('I', infile.read(4))
    outfile.writelines('0x%-11x 0x%-11x\n' % (start_magic, fail_time))
    total_offset += 8
    outfile.writelines("[mloader_balong_load_info]\n")
    outfile.writelines('%-21s%-14s%-14s%-14s%-14s%-14s%-14s%-14s%-14s%-14s%-14s%-14s\n' %('img_name', 'start_time', 'auto_load', 'cold_patch', 'hot_patch', 'status', 'icc_send_num', 'icc_recv_num', 'patch_size', 'size', 'end_time', 'load_addr'))
    for i in range(0, 14):
        (img_name, )    = struct.unpack('32s', infile.read(32))
        # print(type(str(img_name)))
        str_name = str(img_name)
        name = str_name.split('.bin', str_name.find('.bin'))
        final_name = name[0][2:] + ".bin"
        if (str_name.find('.bin') == -1):
            final_name = "0"
        (start_time, )    = struct.unpack('I', infile.read(4))
        (auto_load, )    = struct.unpack('B', infile.read(1))
        (cold_patch, )    = struct.unpack('B', infile.read(1))
        (hot_patch, )    = struct.unpack('B', infile.read(1))
        (status, )    = struct.unpack('B', infile.read(1))
        (icc_send_num, )    = struct.unpack('I', infile.read(4))
        (icc_recv_num, )    = struct.unpack('I', infile.read(4))
        (patch_size, )    = struct.unpack('I', infile.read(4))
        (size, )    = struct.unpack('I', infile.read(4))
        (end_time, )    = struct.unpack('I', infile.read(4))
        (load_addr, )    = struct.unpack('I', infile.read(4))
        outfile.writelines('%-20s 0x%-11x 0x%-11x 0x%-11x 0x%-11x 0x%-11x 0x%-11x 0x%-11x 0x%-11x 0x%-11x 0x%-11x 0x%-11x\n' % (final_name, start_time, auto_load, cold_patch, hot_patch, status, icc_send_num, icc_recv_num, patch_size, size, end_time, load_addr))
    total_offset += 14*(64)

    outfile.writelines('%-14s\n' %('end_magic'))
    (end_magic, )    = struct.unpack('I', infile.read(4))
    outfile.writelines('0x%-11x\n' % (end_magic))
    total_offset += 4
    
    outfile.writelines('total_offset: 0x%x\n' %(total_offset))
    outfile.writelines("==MLOADER CCORE==\n")
    outfile.writelines('\n\n')

########################################################################################
def entry_0x20000A1(infile, field, offset, len, version, mode, outfile):
        new_offset = eval(offset)
        global total_offset
        outfile.writelines("==MLOADER CCORE==\n")
        ########check parameter start#############
        if not field == '0x20000A1':
            print(('hidis field is', field))
            print(('current field is', '0x20000A1'))
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
        parse_mloader_ccore_handle("mloader_ccore",infile, new_offset, outfile)        
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
#     entry_0x20000A1(my_infile, field, offset, length, version, mode, my_outfile)
#     my_infile.close()
#     my_outfile.close()

# if __name__ == '__main__':
#     main()

#python field_0x20000A1_0000.py rdr.bin 0x20000A1 0xfcdb0 0x400 0x0000 1 out.txt

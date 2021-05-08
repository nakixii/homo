#!/usr/bin/env python3
# coding=utf-8
# Copyright (C) Huawei Technologies Co., Ltd. 2010-2018. All rights reserved.

import struct
import os
import sys
import string
from config import *

freq_st=(
	"cpuload_count: ",
	"cpuload: ",
	"cpu_freq_count: ",
	"cpu_freq_start_time: ",
	"cpu_freq_end_time: ",
	"cpu_cur_freq: ",
	"cpu_dst_freq: ",
	"fast_freq_count: ",
	"fast_freq_start_time: ",
	"fast_freq_end_time: ",
	"fast_cur_freq: ",
	"fast_dst_freq: ",
	"slow_freq_count: ",
	"slow_freq_start_time: ",
	"slow_freq_end_time: ",
	"slow_cur_freq: ",
	"slow_dst_freq: ",
	"vote_info_count: ",
	"vote_info: ",
	"vote_info_time: ",
	"icc_count: ",
	"icc_info: ",
	"icc_info_time: ",
	"temp_prot_icc_time: ",
	"temp_prot_down_time: ",
	"temp_prot_up_time: ",
	"temp_prot_cb_time: ",
	"temp_prot_mark: ",
	"freq_dump_size: ",
)

def parse_ccore_cpufreq_bin(infile, offset, outfile):
	infile.seek(offset)
	print("cpuload:>>>", file=outfile)
	#cpuload
	(value, )    = struct.unpack('I', infile.read(4))
	print("%s0x%.8x" %(freq_st[0], int(value-1)%10), file=outfile)
	for i in range(10):
		(value, )    = struct.unpack('I', infile.read(4))
		print("%s[%d]0x%.8x" %(freq_st[1], i, value), file=outfile)
	#cpu_freq	
	print("", file=outfile)
	print("cpu_freq:>>>", file=outfile)
	(value, )    = struct.unpack('I', infile.read(4))
	print("%s0x%.8x" %(freq_st[2], int(value-1)%5), file=outfile)
	for i in range(5):
		(value, )    = struct.unpack('I', infile.read(4))
		print("%s[%d]0x%.8x" %(freq_st[3], i, value), file=outfile)
	for i in range(5):
		(value, )    = struct.unpack('I', infile.read(4))
		print("%s[%d]0x%.8x" %(freq_st[4], i, value), file=outfile)
	for i in range(5):
		(value, )    = struct.unpack('I', infile.read(4))
		print("%s[%d]0x%.8x" %(freq_st[5], i, value), file=outfile)
	for i in range(5):
		(value, )    = struct.unpack('I', infile.read(4))
		print("%s[%d]0x%.8x" %(freq_st[6], i, value), file=outfile)
	#fast_freq
	print("", file=outfile)
	print("fast_freq:>>>", file=outfile)
	(value, )    = struct.unpack('I', infile.read(4))
	print("%s0x%.8x" %(freq_st[7], int(value-1)%5), file=outfile)
	for i in range(5):
		(value, )    = struct.unpack('I', infile.read(4))
		print("%s[%d]0x%.8x" %(freq_st[8], i, value), file=outfile)
	for i in range(5):
		(value, )    = struct.unpack('I', infile.read(4))
		print("%s[%d]0x%.8x" %(freq_st[9], i, value), file=outfile)
	for i in range(5):
		(value, )    = struct.unpack('I', infile.read(4))
		print("%s[%d]0x%.8x" %(freq_st[10], i, value), file=outfile)
	for i in range(5):
		(value, )    = struct.unpack('I', infile.read(4))
		print("%s[%d]0x%.8x" %(freq_st[11], i, value), file=outfile)
	#slow_freq
	print("", file=outfile)
	print("slow_freq:>>>", file=outfile)
	(value, )    = struct.unpack('I', infile.read(4))
	print("%s0x%.8x" %(freq_st[12], int(value-1)%5), file=outfile)
	for i in range(5):
		(value, )    = struct.unpack('I', infile.read(4))
		print("%s[%d]0x%.8x" %(freq_st[13], i, value), file=outfile)
	for i in range(5):
		(value, )    = struct.unpack('I', infile.read(4))
		print("%s[%d]0x%.8x" %(freq_st[14], i, value), file=outfile)
	for i in range(5):
		(value, )    = struct.unpack('I', infile.read(4))
		print("%s[%d]0x%.8x" %(freq_st[15], i, value), file=outfile)
	for i in range(5):
		(value, )    = struct.unpack('I', infile.read(4))
		print("%s[%d]0x%.8x" %(freq_st[16], i, value), file=outfile)
	#vote_info
	print("", file=outfile)
	print("vote_info:>>>", file=outfile)
	(value, )    = struct.unpack('I', infile.read(4))
	print("%s0x%.8x" %(freq_st[17], int(value-1)%10), file=outfile)
	for i in range(10):
		(value, )    = struct.unpack('I', infile.read(4))
		print("%s[%d]0x%.8x" %(freq_st[18], i, value), file=outfile)
	for i in range(10):
		(value, )    = struct.unpack('I', infile.read(4))
		print("%s[%d]0x%.8x" %(freq_st[19], i, value), file=outfile)
	#icc
	print("", file=outfile)
	print("icc:>>>", file=outfile)
	(value, )    = struct.unpack('I', infile.read(4))
	print("%s0x%.8x" %(freq_st[20], int(value-1)%10), file=outfile)
	for i in range(10):
		(value, )    = struct.unpack('I', infile.read(4))
		print("%s[%d]0x%.8x" %(freq_st[21], i, value), file=outfile)
	for i in range(10):
		(value, )    = struct.unpack('I', infile.read(4))
		print("%s[%d]0x%.8x" %(freq_st[22], i, value), file=outfile)
	#temp_prot
	print("", file=outfile)
	print("temp_prot:>>>", file=outfile)
	(value, )    = struct.unpack('I', infile.read(4))
	print("%s[%d]0x%.8x" %(freq_st[23], i, value), file=outfile)
	(value, )    = struct.unpack('I', infile.read(4))
	print("%s[%d]0x%.8x" %(freq_st[24], i, value), file=outfile)
	(value, )    = struct.unpack('I', infile.read(4))
	print("%s[%d]0x%.8x" %(freq_st[25], i, value), file=outfile)
	(value, )    = struct.unpack('I', infile.read(4))
	print("%s[%d]0x%.8x" %(freq_st[26], i, value), file=outfile)
	(value, )    = struct.unpack('I', infile.read(4))
	print("%s[%d]0x%.8x" %(freq_st[27], i, value), file=outfile)
	#freq_dump_size
	print("freq_dump_size:>>>", file=outfile)
	(value, )    = struct.unpack('I', infile.read(4))
	print("%s[%d]0x%.8x" %(freq_st[28], 0, value), file=outfile)

	print("", file=outfile)

########################################################################################
def entry_0x2000094(infile, field, offset, len, version, mode, outfile):
        ########check parameter start#############
        if not field == '0x2000094':
            print('hidis field is ', field)
            print('current field is', '0x2000094')
            return error['ERR_CHECK_FIELD']
        elif not version == '0x0000':
            print('hidis version is ', version)
            print('current version is ', '0x0000')
            return error['ERR_CHECK_VERSION']
        elif not len == '0x200':
            print('hids len is ', len)
            print('current len is ', '0x200')
            return error['ERR_CHECK_LEN']
        #########check parameter end##############
        parse_ccore_cpufreq_bin(infile, eval(offset), outfile)
        return 0


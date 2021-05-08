#!/usr/bin/env python3
# coding=utf-8 
# Copyright (C) Huawei Technologies Co., Ltd. 2010-2020. All rights reserved.

import sys
from config import *

def parse_icc_bin(fifo_type, infile, offset, outfile):
	infile.seek(offset)
	(front, ) = struct.unpack('i', infile.read(4))
	(rear, )  = struct.unpack("i", infile.read(4))
	(size, )  = struct.unpack("i", infile.read(4))

	# 队列头
	s1 = "******************************************** [%s] ********************************************\n" % (fifo_type)
	outfile.writelines(s1)
	outfile.writelines('%-14s%-14s%-14s\n' %('front', 'rear', 'size'))
	outfile.writelines('0x%-11x 0x%-11x 0x%-11x\n' % (front, rear, size))

	# 10条消息
	outfile.writelines('%-14s%-14s%-14s%-14s%-14s%-14s%-14s%-14s%-14s\n' %('channel_id', 'send_task_id', 'recv_task_id', 'len', 'write_pos', 'read_pos','duration_prev', 'duration_post', 'data'))
	for i in range(1, 11):
		(channel_id, )    = struct.unpack('i', infile.read(4))
		(send_task_id, )  = struct.unpack("i", infile.read(4))
		(recv_task_id, )  = struct.unpack("i", infile.read(4))
		(len, )           = struct.unpack('i', infile.read(4))
		(write_pos, )     = struct.unpack("i", infile.read(4))
		(read_pos, )      = struct.unpack("i", infile.read(4))
		(duration_prev, ) = struct.unpack("i", infile.read(4))
		(duration_post, ) = struct.unpack("i", infile.read(4))
		outfile.writelines('0x%-11x 0x%-11x 0x%-11x 0x%-11x 0x%-11x 0x%-11x 0x%-11x 0x%-11x' % (channel_id, send_task_id, recv_task_id, len, write_pos,read_pos, duration_prev, duration_post))
		outfile.writelines('     ')
		for j in range(1, 11):
			(data, ) = struct.unpack("i", infile.read(4))
			outfile.writelines('0x%08X  ' %(data)) 
		outfile.writelines('\n')
	outfile.writelines('\n\n')
    
def entry_0x200006E(infile, field, offset, len, version, mode, outfile):
	########check parameter start#############
	if not field == '0x200006E':
		print('hidis field is ', field)
		print('current field is', '0x200006E')
		return error['ERR_CHECK_FIELD']
	elif not version == '0x0000':
		print('hidis version is ', version)
		print('current version is ', '0x00')
#		return error['ERR_CHECK_VERSION']
	elif not len == '0x400':
		print('hids len is ', len)
		print('current len is ', '0x400')
#		return error['ERR_CHECK_LEN']
	#########check parameter end##############

	parse_icc_bin('fifo_send', infile, eval(offset), outfile)
	parse_icc_bin('fifo_recv', infile, infile.tell(), outfile)
	return 0

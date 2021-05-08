#!/usr/bin/env python3
# coding=utf-8
# -*- coding: utf-8 -*-
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename
# * Description   analysis pmu bin dump
# * Version       1.0
# * Data          2019.6.28
#***********************************************************************

import sys
from config import *
enable_stamp     = []
disable_stamp    = []
pid              = []
set_stamp        = []
cur_volt_uV      = []
set_volt_uV      = []    

def analysis_pmu_bin(infile, offset, outfile):
	infile.seek(eval(offset))
	for i in range(0,10):
		(mark, ) = struct.unpack('I', infile.read(4))
		if mark != 0x5a5a5a5a :
			continue
			
		(volt_id, ) = struct.unpack('I', infile.read(4))
		(status, ) = struct.unpack('I', infile.read(4))
		(ocp_cnt, ) = struct.unpack('I', infile.read(4))
		(ocp_stamp, ) = struct.unpack('I', infile.read(4))
		(enable_pos, ) = struct.unpack('I', infile.read(4))
		
		if status != 0:
			st = 'open'
		else:
			st = 'close'
		outfile.writelines("*****************[volt id]%d  [status]%s  [ocp cnt]%d  [ocp stamp]0x%x***************\n" %(volt_id, st, ocp_cnt, ocp_stamp))
		task_id = []
		for loop in range(0,5):		
			(val, ) = struct.unpack('I', infile.read(4))
			task_id.append(val)
			
		enable_stamp = []
		for loop in range(0,5):		
			(val, ) = struct.unpack('I', infile.read(4))
			enable_stamp.append(val)
		
		for loop in range(0,5):
					outfile.writelines("[enable  stamp]0x%-12x[PID]0x%x\n" %(enable_stamp[loop], task_id[loop]))
					
		(disable_pos, ) = struct.unpack('I', infile.read(4))
		
		task_id = []
		for loop in range(0,5):		
			(val, ) = struct.unpack('I', infile.read(4))
			task_id.append(val)
			
		disable_stamp = []
		for loop in range(0,5):		
			(val, ) = struct.unpack('I', infile.read(4))
			disable_stamp.append(val)
		outfile.writelines("--------------------------------------------\n")	
		for loop in range(0,5):
					outfile.writelines("[disable stamp]0x%-12x[PID]0x%x\n" %(disable_stamp[loop], task_id[loop]))
		
		(set_pos, ) = struct.unpack('I', infile.read(4))
		
		pid = []
		for loop in range(0,5):	
			(val, ) = struct.unpack('I', infile.read(4))
			pid.append(val)
			
		set_stamp = []			
		for loop in range(0,5):
			(val, ) = struct.unpack('I', infile.read(4))
			set_stamp.append(val)
			
		cur_volt_uV = []			
		for loop in range(0,5):
			(val, ) = struct.unpack('I', infile.read(4))
			cur_volt_uV.append(val)
			
		set_volt_uV = []
		for loop in range(0,5):		
			(val, ) = struct.unpack('I', infile.read(4))
			set_volt_uV.append(val)
		outfile.writelines("--------------------------------------------\n")
		for loop in range(0,5):
					outfile.writelines("[set     stamp]0x%-12x[last volt(uV)]%-12d[set volt(uV)]%-12d[PID]0x%x\n" %(set_stamp[loop], cur_volt_uV[loop], set_volt_uV[loop], pid[loop]))
					
		outfile.writelines("\n")
	
def entry_0x2000095(infile, field, offset, len, version, mode, outfile):
	########check parameter start#############
	if not field == '0x2000095':
		print('hidis field is ', field)
		print('current field is', '0x2000095')
		return error['ERR_CHECK_FIELD']
	elif not version == '0x0000':
		print('hidis version is ', version)
		print('current version is ', '0x00')
		return error['ERR_CHECK_VERSION']
	#########check parameter end##############


	analysis_pmu_bin(infile, offset, outfile)
	return 0

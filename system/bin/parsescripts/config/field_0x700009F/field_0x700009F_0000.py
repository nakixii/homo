#!/usr/bin/env python3
# coding=utf-8
# -*- coding: utf-8 -*-
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename
# * Description   analysis pm_ctrl dump
# * Version       1.0
# * Data          2019.6.28
# * 
#***********************************************************************
import sys
from config import *
pmctrl_global_var = (
	"spmi_reg_offset:  ",
	"pmctrl_vote_reg_value :  ",
	"pmctrl_down_hold_time_offset:  ",
	"pmctrl_up_hold_time_offset:  ",
	"pmctrl_step_time_offset: ",
	"pmctrl_avs_low_volt_offset:  ",
	"pmctrl_avs_normal_volt_offset :  ",
	"pmctrl_avs_high_volt_offset :  ",
	"pmctrl_enable_offset :  ",
	)
def parse_nr_pmctrl_bin(infile, field, offset, slen, version, mode, outfile):
	infile.seek(offset)
	for index in range(2):
		(value, )    = struct.unpack('I', infile.read(4))
		outfile.writelines("%s0x%.8x\n" %(pmctrl_global_var[0], value))
		for index in range(4):
			(value, )    = struct.unpack('I', infile.read(4))
			outfile.writelines("%s0x%.8x\n" %(pmctrl_global_var[1], value))
		(value, )    = struct.unpack('I', infile.read(4))
		outfile.writelines("%s0x%.8x\n" %(pmctrl_global_var[2], value))
		(value, )    = struct.unpack('I', infile.read(4))
		outfile.writelines("%s0x%.8x\n" %(pmctrl_global_var[3], value))
		(value, )    = struct.unpack('I', infile.read(4))
		outfile.writelines("%s0x%.8x\n" %(pmctrl_global_var[4], value))
		(value, )    = struct.unpack('I', infile.read(4))
		outfile.writelines("%s0x%.8x\n" %(pmctrl_global_var[5], value))
		(value, )    = struct.unpack('I', infile.read(4))
		outfile.writelines("%s0x%.8x\n" %(pmctrl_global_var[6], value))
		(value, )    = struct.unpack('I', infile.read(4))
		outfile.writelines("%s0x%.8x\n" %(pmctrl_global_var[7], value))
	(value, )    = struct.unpack('I', infile.read(4))
	outfile.writelines("%s0x%.8x\n" %(pmctrl_global_var[8], value))
	
def entry_0x700009F(infile, field, offset, len, version, mode, outfile):
	########check parameter start#############
	if not field == '0x700009F':
		print("hidis field is 0x%x"%(field))
		print("current field is 0x700009F")
		return error['ERR_CHECK_FIELD']
	elif not version == '0x0000':
		print("hidis version is 0x%x"%(version))
		print("current version is 0x00")
#		return error['ERR_CHECK_VERSION']
	elif not len == '0x100':
		print("hids len is 0x%x"%(len))
		print("current len is 0x100")
#		return error['ERR_CHECK_LEN']
	#########check parameter end##############
	parse_nr_pmctrl_bin(infile, field, eval(offset), len, version, mode, outfile)
	return 0
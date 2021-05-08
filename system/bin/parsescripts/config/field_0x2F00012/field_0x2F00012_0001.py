#!/usr/bin/env python3
# coding=utf-8
# -*- coding: utf-8 -*-
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename
# * Description   analysis pm_ctrl dump
# * Version       1.0
# * Data          2019.6.28
#***********************************************************************
import struct
import os
import sys
import string
import config

pmctrl_global_var = (
	"soc_voltage:  ",
	"status_value :  ",
	"chan_status:  ",
	"chan_addr:  ",
	)

vote_var = (
	"NRCCPU:      ",
	"NR SLOWBUS:  ",
	"L2HAC:       ",
	"LL1C:        ",
	"NR THEMRAL:  ",
	"NR BBP BUS:  ",
	"DUMMY :      ",
	"DUMMY :      ",
	"NR FASTBUS:  ",
	"REGULATOR :  ",
	"DUMMY :      ",
	"DUMMY :      ",
	)

profile_var = (
	"soc low:       ",
	"soc normal:    ",
	"soc high:      ",
	"nr bbp low:    ",
	"nr bbp normal: ",
	"nr bbp high:   ",
	)

def volt_to_mv(value):
	if value == 0:
		return 0
	volt = (value&0xff) * 5 + 300
	return volt

def parse_vote(infile, field, offset, slen, version, mode, outfile):
	(value, )    = struct.unpack('I', infile.read(4))
	(index, )    = struct.unpack('I', infile.read(4))
	vote_value = []
	for loop in range(0,5):
		(val, ) = struct.unpack('I', infile.read(4))
		vote_value.append(val)
	vote_stamp = []
	for loop in range(0,5):
		(val, ) = struct.unpack('I', infile.read(4))
		vote_stamp.append(val)
	pid = []
	for loop in range(0,5):
		(val, ) = struct.unpack('I', infile.read(4))
		pid.append(val)
	if index >0:
		outfile.writelines("USER %s \n" %(vote_var[value]))
		for loop in range(index + 5, index, -1):
			i = (loop - 1)%5
			outfile.writelines("VOTE: STAMP 0x%.8x " %(vote_stamp[i]))
			outfile.writelines("VALUE: %.4s mv; " %(vote_value[i]))
			outfile.writelines("PID: 0x%.2x; \n" %(pid[i]))

def parse_lr_pmctrl_bin(infile, field, offset, slen, version, mode, outfile):
	infile.seek(offset)
	outfile.writelines("*************    Current voltage    ************\n")
	(value, )    = struct.unpack('I', infile.read(4))
	(value1, )    = struct.unpack('I', infile.read(4))
	if value == value1:
		outfile.writelines("**        %s %.4s mv              **\n" %(pmctrl_global_var[0], volt_to_mv(value)))
	outfile.writelines("*******   Software vote record begin ***********\n")
	for loop in range(0,12):
		parse_vote(infile, field, offset, slen, version, mode, outfile)
	outfile.writelines("Other users don't have software record\n")
	outfile.writelines("********   Software vote record end ************\n")
	outfile.writelines("*********    Pmctrl offset info     ************\n")
	(value, )    = struct.unpack('I', infile.read(4))
	outfile.writelines("%s 0x%.8x \n" %(pmctrl_global_var[2], value))
	(value, )    = struct.unpack('I', infile.read(4))
	outfile.writelines("%s 0x%.8x \n" %(pmctrl_global_var[3], value))
	(value, )    = struct.unpack('I', infile.read(4))
	outfile.writelines("**********   Last register vote record  ********\n")
	for loop in range(0,12):
		(value, )    = struct.unpack('I', infile.read(4))
		if value != 0:
			outfile.writelines("USER %s %.4s mv\n" %(vote_var[loop], volt_to_mv(value)))
	outfile.writelines("**********    Volt profile record     **********\n")
	for loop in range(0,6):
		(value, )    = struct.unpack('I', infile.read(4))
		if volt_to_mv(value) != 0:
			outfile.writelines("PROFILE %s %.4s mv\n" %(profile_var[loop], volt_to_mv(value)))

def entry_0x2F00012(infile, field, offset, len, version, mode, outfile):
	########check parameter start#############
	if not field == '0x2F00012':
		print("hidis field is 0x%x"%(field))
		print("current field is 0x2F00012")
		return error['ERR_CHECK_FIELD']
	elif not version == '0x0001':
		print("hidis version is 0x%x"%(version))
		print("current version is 0x01")
		return error['ERR_CHECK_VERSION']
	elif not len == '0x390':
		print("hids len is 0x%x"%(len))
		print("current len is 0x390")
		return error['ERR_CHECK_LEN']
	#########check parameter end##############
	parse_lr_pmctrl_bin(infile, field, eval(offset), len, version, mode, outfile)
	return 0
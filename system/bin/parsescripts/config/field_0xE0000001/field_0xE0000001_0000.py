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

import struct
import os
import sys
import string
import config   

def analysis_pmu_record_bin(infile, offset, outfile):
	infile.seek(eval(offset))

	(index, ) = struct.unpack('I', infile.read(4))
	outfile.writelines("****PMU index %d****\n" % index)
	for loop in range(0,20):
		(offset, ) = struct.unpack('I', infile.read(4))
		(value, ) = struct.unpack('I', infile.read(4))
		outfile.writelines("[offset]0x%x  [record_val]0x%x  \n" %(offset, value))
	(index, ) = struct.unpack('I', infile.read(4))
	outfile.writelines("****PMU index %d****\n" % index)
	for loop in range(0,6):
		(offset, ) = struct.unpack('I', infile.read(4))
		(value, ) = struct.unpack('I', infile.read(4))
		outfile.writelines("[offset]0x%x  [record_val]0x%x  \n" %(offset, value))
	(index, ) = struct.unpack('I', infile.read(4))
	outfile.writelines("****PMU index %d****\n" % index)
	for loop in range(0,3):
		(offset, ) = struct.unpack('I', infile.read(4))
		(value, ) = struct.unpack('I', infile.read(4))
		outfile.writelines("[offset]0x%x  [record_val]0x%x  \n" %(offset, value))

def entry_0xE0000001(infile, field, offset, len, version, mode, outfile):
	########check parameter start#############
	if not field == '0xE0000001':
		print('hidis field is ', field)
		print('current field is', '0xE0000001')
		return error['ERR_CHECK_FIELD']
	elif not version == '0x0000':
		print('hidis version is ', version)
		print('current version is ', '0x00')
		return error['ERR_CHECK_VERSION']
	#########check parameter end##############

	analysis_pmu_record_bin(infile, offset, outfile)
	return 0

#!/usr/bin/env python3
# coding=utf-8 
"""
功能：parse cpufreq dump memory
版权信息：华为技术有限公司，版权所有（C）2010-2019
修改记录：
"""
import sys
from config import *
pm_global_var = (
	"CPU0_LOAD",
	"CPU1_LOAD",
	"CPUFREQ_IN_STAMP",
	"CPUFREQ_OUT_STAMP",
	"CURRENT_PROFILE",
	"CPUFREQ_DIV1",
	"CPUFREQ_DIV2",
	"CPUFREQ_STAT1",
	"CPUFREQ_STAT2"
	)
def parse_acore_cpufreq_bin(infile, offset, outfile):
	infile.seek(offset)
	for l in range(10):
		for index in range(len(pm_global_var)):
			(value, )    = struct.unpack('I', infile.read(4))
			print("%s[%d]:0x%.8x" %(pm_global_var[index],l, value), file=outfile)
		print("", file=outfile)


	
def entry_0x110000A(infile, field, offset, len, version, mode, outfile):
	########check parameter start#############
	if not field == '0x110000A':
		print( 'hidis field is ', field)
		print( 'current field is', '0x110000A')
		return error['ERR_CHECK_FIELD']
	elif not version == '0x0000':
		print( 'hidis version is ', version)
		print( 'current version is ', '0x00')
#		return error['ERR_CHECK_VERSION']
	elif not len == '0x200':
		print( 'hids len is ', len)
		print( 'current len is ', '0x200')
#		return error['ERR_CHECK_LEN']
	#########check parameter end##############
	parse_acore_cpufreq_bin(infile, eval(offset), outfile)
	return 0
#!/usr/bin/env python3
# coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename      
# * Description   analysis bin mini dump 
# * Version       1.0
# * Data          2019.6.28
#***********************************************************************


import time 

time_now = time.strftime('%y-%m-%d_%H:%M')

import re 
import os
import sys
sys.path.append('/system/bin/parsescripts/config')
sys.path.append('/system/bin/parsescripts/config/pde_config')
sys.path.append('config')
sys.path.append('config/pde_config')

import pdf_bin_mini_dump_analysis as pdf_bin_analysis
import csi_bin_mini_dump_analysis as csi_bin_analysis

file_path = ""

list_all_info = []

global bin_flag
bin_flag = 0

def file_trans(file_in):
	print("file_trans!")

	with open(file_in, 'rb') as fin_in:
		fin_in.seek(0,0)
		data_cnt = 0
		data_tmp = ""

		while True:
			byte = fin_in.read(1)
			if not byte:
				break
			data_8bit = hex(ord(byte))[2:].zfill(2)
			if data_cnt == 0:
				data_tmp = data_8bit
				data_cnt = data_cnt +1
				continue
			if data_cnt == 1:
				#data_tmp = data_8bit + data_tmp
				data_tmp = "{}{}".format(data_8bit, data_tmp)
				data_cnt = data_cnt +1
				continue
			if data_cnt == 2:
				#data_tmp = data_8bit + data_tmp
				data_tmp = "{}{}".format(data_8bit, data_tmp)
				data_cnt = data_cnt +1
				continue
			if data_cnt == 3:
				#data_tmp = "0x" + data_8bit + data_tmp + "\n"
				data_tmp = "{}{}{}{}".format("0x",data_8bit, data_tmp,"\n")
				list_all_info.append(data_tmp)
				data_cnt = 0

	#print("print(list_all_info)")
	#print(list_all_info)


def file_trans_inhandler(inhandler,offset,filelength):
	print("file_trans_inhandler!")
	inhandler.seek(offset)
	#fout=open("bin_file_tmp.txt","w")
	data_cnt = 0
	data_tmp = ""
	file_cnt = 0
	while (file_cnt < filelength):
		byte = inhandler.read(1)
		if not byte:
			break
		data_8bit = hex(ord(byte))[2:].zfill(2)
		if data_cnt == 0:
			data_tmp = data_8bit
			data_cnt = data_cnt +1
			file_cnt = file_cnt +1
			continue
		if data_cnt == 1:
			#data_tmp = data_8bit + data_tmp
			data_tmp = "{}{}".format(data_8bit, data_tmp)
			data_cnt = data_cnt +1
			continue
		if data_cnt == 2:
			#data_tmp = data_8bit + data_tmp
			data_tmp = "{}{}".format(data_8bit, data_tmp)
			data_cnt = data_cnt +1
			continue
		if data_cnt == 3:
			#data_tmp = "0x" + data_8bit + data_tmp + "\n"
			data_tmp = "{}{}{}{}".format("0x",data_8bit, data_tmp,"\n")
			list_all_info.append(data_tmp)
			data_cnt = 0
			file_cnt = file_cnt +1
	#fout.close()


def pde_version_check(list_all_info):
	print("pde_version_check!")
	global bin_flag
	pde_version_check_result = 0
	#fin=open("bin_file_tmp.txt","r")
	for i in range(len(list_all_info)):
		content = list_all_info[i].strip()
	#for line_content in fin.readlines():   
		#content = line_content.strip()
		if len(content) != 0:
			content = content.lower()
			if "5000100" in content:
				bin_flag = "b5"
				pde_version_check_result = 1
				break
			elif "5360100" in content:
				bin_flag = "m5"
				pde_version_check_result = 1
				break
			elif "e63a0100" in content:
				bin_flag = "e63a"
				pde_version_check_result = 1
				break
			elif "e6290200" in content:
				bin_flag = "e629"
				pde_version_check_result = 1
				break
	#fin.close()

	return pde_version_check_result


def entry_pde_parser(infile, outfile):
	print("entry_pde_parser!")
	#file_path = "D:/code_python/OAM_analysis/DEBUG_INFO_ANALYSIS-TC/code_read_vm_file/tlphy_ddr.txt"
	if not os.path.exists(infile):
		print(("%s is not exist!!!"%(infile)))
		return 1
	else:
		list_all_info.clear()
		file_trans(infile)
		#print ("pick up the bin info_data done!")
		version_flag = pde_version_check(list_all_info)
		if(version_flag):
			print ("bin_flag is %s"%bin_flag)
			pdf_bin_analysis.pdf_pde_parse_init()
			#print ("pdf pde_parse_init done!")
			pdf_bin_analysis.pdf_read_file(bin_flag,outfile,list_all_info)
			print ("06 Analysis the bin debug info done!")
			csi_bin_analysis.csi_pde_parse_init()
			#print ("csi pde_parse_init done!")
			csi_bin_analysis.csi_read_file(bin_flag,outfile,list_all_info)
			print ("01 Analysis the bin debug info done!")
			print ("PDE Analysis the bin debug info done!")
			return 0
		else:
			print("version_flag is error!!!")
			return 2	


def entry_pde_parser_link(inhandler,outfile,offset,filelength):
	print("entry_pde_parser_link!")
	list_all_info.clear()
	file_trans_inhandler(inhandler,offset,filelength)
	#print ("pick up the bin info_data done!")
	version_flag = pde_version_check(list_all_info)
	if(version_flag):
		print ("bin_flag is %s"%bin_flag)
		pdf_bin_analysis.pdf_pde_parse_init()
		#print ("pdf pde_parse_init done!")
		pdf_bin_analysis.pdf_read_file(bin_flag,outfile,list_all_info)
		print ("06 Analysis the bin debug info done!")
		csi_bin_analysis.csi_pde_parse_init()
		#print ("csi pde_parse_init done!")
		csi_bin_analysis.csi_read_file(bin_flag,outfile,list_all_info)
		print ("01 Analysis the bin debug info done!")
		print ("PDE Analysis the bin debug info done!")
		return 0
	else:
		print("version_flag is error!!!")
		return 2

#!/usr/bin/env python3
# coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename      
# * Description     
# * Version       1.0
# * Data          2019.3.28
#***********************************************************************

import csi_trace_info_analysis as trace_info_analysis

import b5_pde_bin_info as b5_bin_info
import m5_pde_bin_info as m5_bin_info
import ba_pde_bin_info as ba_bin_info
import de_pde_bin_info as de_bin_info

file_path = ""
line_count = 0
list_csi_data_all_info = []

list_data_anaysis = [[] for i in range(5)]

list_csi_seg_line_trans = []
list_csi_seg_len_trans  = []

def seg_trans(bin_flag,init_line):
	start_line = init_line
	if bin_flag == "b5":
		pdf_cc_num = 4
		for i in range(pdf_cc_num * 5,(pdf_cc_num+1)* 5):
			data_bin =  bin(int(b5_bin_info.list_pde_seg_len[i],16))[2:]
			data_bin = data_bin.zfill(32)
			seg_len = int(data_bin, 2)
			seg_len = int(seg_len/4)
			list_csi_seg_len_trans.append(seg_len)
			list_csi_seg_line_trans.append(start_line)
			start_line = start_line + seg_len

	elif bin_flag == "m5":
		pdf_cc_num = 1
		for i in range(pdf_cc_num * 5,(pdf_cc_num+1)* 5):
			data_bin =  bin(int(m5_bin_info.list_pde_seg_len[i],16))[2:]
			data_bin = data_bin.zfill(32)
			seg_len = int(data_bin, 2)
			seg_len = int(seg_len/4)
			list_csi_seg_len_trans.append(seg_len)
			list_csi_seg_line_trans.append(start_line)
			start_line = start_line + seg_len

	elif bin_flag == "e63a":
		pdf_cc_num = 2
		for i in range(pdf_cc_num * 5,(pdf_cc_num+1)* 5):
			data_bin =  bin(int(ba_bin_info.list_pde_seg_len[i],16))[2:]
			data_bin = data_bin.zfill(32)
			seg_len = int(data_bin, 2)
			seg_len = int(seg_len/4)
			list_csi_seg_len_trans.append(seg_len)
			list_csi_seg_line_trans.append(start_line)
			start_line = start_line + seg_len

	elif bin_flag == "e629":
		pdf_cc_num = 1

		for i in range(pdf_cc_num * 5,(pdf_cc_num+1)* 5):
			data_bin = bin(int(de_bin_info.list_pde_seg_len[i],16))[2:]
			data_bin = data_bin.zfill(32)
			seg_len = int(data_bin, 2)
			seg_len = int(seg_len/4)
			list_csi_seg_len_trans.append(seg_len)
			list_csi_seg_line_trans.append(start_line)
			start_line = start_line + seg_len

	else:
		pdf_cc_num = 1

		for i in range(pdf_cc_num * 5,(pdf_cc_num+1)* 5):
			data_bin = bin(int(b5_bin_info.list_pde_seg_len[i],16))[2:]
			data_bin = data_bin.zfill(32)
			seg_len = int(data_bin, 2)
			seg_len = int(seg_len/4)
			list_csi_seg_len_trans.append(seg_len)
			list_csi_seg_line_trans.append(start_line)
			start_line = start_line + seg_len

	#print("list_csi_seg_line_trans")
	#print(list_csi_seg_line_trans)
	#print("list_csi_seg_len_trans")
	#print(list_csi_seg_len_trans)


def csi_version_info_analysis(cc_num,list_data):
	list_csi_data_all_info.append("\n/************************************************************************************************/\n")
	list_csi_data_all_info.append("{} {} {}".format("/**************    csi version_info_  " , str(cc_num) , "      **************/"))
	list_csi_data_all_info.append("\n")
	list_csi_data_all_info.append("{} {}".format("dm_ocd_seg : ".ljust(40) , str(list_data[0])))
	list_csi_data_all_info.append("\n")
	list_csi_data_all_info.append("{} {}".format("version_info : ".ljust(40) , str(list_data[1])))
	list_csi_data_all_info.append("\n")
	list_csi_data_all_info.append("{} {}".format("version_info : ".ljust(40) , str(list_data[2])))
	list_csi_data_all_info.append("\n")
	list_csi_data_all_info.append("{} {}".format("version_info : ".ljust(40) , str(list_data[3])))
	list_csi_data_all_info.append("\n")
	list_csi_data_all_info.append("{} {}".format("version_info : ".ljust(40) , str(list_data[4])))
	list_csi_data_all_info.append("\n")
	list_csi_data_all_info.append("{} {}".format("version_info : ".ljust(40) , str(list_data[5])))
	list_csi_data_all_info.append("\n")
	list_csi_data_all_info.append("{} {}".format("version_info : ".ljust(40) , str(list_data[6])))
	list_csi_data_all_info.append("\n")
	list_csi_data_all_info.append("{} {}".format("version_info : ".ljust(40) , str(list_data[7])))
	list_csi_data_all_info.append("\n")
	list_csi_data_all_info.append("\n")


def csi_dm_dbg_info_analysis(cc_num,list_data):
	list_csi_data_all_info.append("\n/************************************************************************************************/\n")
	list_csi_data_all_info.append("{} {} {}".format("/**************    csi dm_dbg_info_  " , str(cc_num) , "      **************/"))
	list_csi_data_all_info.append("\n")
	list_csi_data_all_info.append("{} {}".format("pde_debug_en : ".ljust(40) , str(list_data[0])))
	list_csi_data_all_info.append("\n")
	list_csi_data_all_info.append("{} {}".format("pde_init_log_ctrl : ".ljust(40) , str(list_data[1])))
	list_csi_data_all_info.append("\n")
	list_csi_data_all_info.append("{} {}".format("pde_ndbg_wtd_en : ".ljust(40) , str(list_data[2])))
	list_csi_data_all_info.append("\n")	
	list_csi_data_all_info.append("{} {}".format("pde_ndbg_timer_en : ".ljust(40) , str(list_data[3])))
	list_csi_data_all_info.append("\n")	
	list_csi_data_all_info.append("{} {}".format("pde_ndbg_ipc_warn_status : ".ljust(40) , str(list_data[4])))
	list_csi_data_all_info.append("\n")	
	list_csi_data_all_info.append("{} {}".format("pde_ndbg_assert_info : ".ljust(40) , str(list_data[5])))
	list_csi_data_all_info.append("\n")	
	list_csi_data_all_info.append("{} {}".format("pde_ndbg_assert_pc : ".ljust(40) , str(list_data[6])))
	list_csi_data_all_info.append("\n")						  	
	list_csi_data_all_info.append("{} {}".format("pde_ndbg_assert_lr : ".ljust(40) , str(list_data[7])))
	list_csi_data_all_info.append("\n")
	list_csi_data_all_info.append("\n")


def csi_tag_info_analysis(cc_num,list_data):
	list_csi_data_all_info.append("\n/************************************************************************************************/\n")
	list_csi_data_all_info.append("{} {} {}".format("/**************    csi tag_info_   " , str(cc_num) , "      **************/"))
	list_csi_data_all_info.append("\n")
	list_csi_data_all_info.append("{} {}".format("pde_ndbg_tag_info0 : ".ljust(40) , str(list_data[0])))
	list_csi_data_all_info.append("\n")		
	list_csi_data_all_info.append("{} {}".format("pde_ndbg_tag_info1 : ".ljust(40) ,str(list_data[1])))
	list_csi_data_all_info.append("\n")
	list_csi_data_all_info.append("\n")

def csi_trace_info_analysis(cc_num,list_data):
	list_data_trace = trace_info_analysis.read_list_data(cc_num,list_data)
	for i in range(len(list_data_trace)):
		list_csi_data_all_info.append(list_data_trace[i])


def csi_stack_info_analysis(cc_num,list_data):
	pass	


def csi_pde_parse_init():
	list_csi_data_all_info.clear()
	list_csi_data_all_info.append(" \n")	
	list_csi_data_all_info.append(" \n")	
	list_csi_data_all_info.append(" /***********************************************************************/\n")
	list_csi_data_all_info.append(" Date         \n")
	list_csi_data_all_info.append(" /***********************************************************************/\n")
	list_csi_data_all_info.append(" \n")	
	list_csi_data_all_info.append(" \n")	
	for i in range(len(list_data_anaysis)):
		list_data_anaysis[i].clear()


def get_csi_init_line(list_all_info):
	pdf_file_size_16 = list_all_info[6]
	data_bin =  bin(int(pdf_file_size_16,16))[2:]
	data_bin = data_bin.zfill(32)
	pdf_file_size_10 = int(data_bin, 2)
	pdf_file_size_10 = int(pdf_file_size_10/4)
	#print("pdf_file_size_10")
	#print(pdf_file_size_10)

	csi_sec_num_16 = list_all_info[pdf_file_size_10 + 7]
	csi_data_bin =  bin(int(csi_sec_num_16,16))[2:]
	csi_data_bin = csi_data_bin.zfill(32)
	csi_sec_num_10 = int(csi_data_bin, 2)
	#print("csi_sec_num_10")
	#print(csi_sec_num_10)

	csi_bin_line = 64 + 32*csi_sec_num_10
	csi_bin_line = int(csi_bin_line/4)

	init_line = pdf_file_size_10 + csi_bin_line
	#print("csi_init_line")
	#print(init_line)

	return init_line


def csi_read_file(bin_flag,outfile,list_all_info):

	init_line = get_csi_init_line(list_all_info)
	seg_trans(bin_flag,init_line)
	#fin=open("bin_file_tmp.txt","r")
	#line_num = 0
	#for line_content in fin.readlines():   
		#line_num = line_num + 1
		#content = line_content.strip()
	for line_num in range(len(list_all_info)):
		content = list_all_info[line_num].strip()
		if len(content) != 0:
			content = content.lower()
			for i in range(len(list_csi_seg_line_trans)):
				if line_num >= list_csi_seg_line_trans[i] and (line_num < list_csi_seg_line_trans[i] + list_csi_seg_len_trans[i]):
					list_data_anaysis[i].append(content)
	#fin.close()

	cc_num = 0
	csi_version_info_analysis(cc_num,list_data_anaysis[0])
	csi_dm_dbg_info_analysis(cc_num,list_data_anaysis[1])
	csi_tag_info_analysis(cc_num,list_data_anaysis[2])
	csi_trace_info_analysis(cc_num,list_data_anaysis[3])
	csi_stack_info_analysis(cc_num,list_data_anaysis[4])

	with open(outfile, 'a') as f2:
		for i in range(len(list_csi_data_all_info)):
			content = list_csi_data_all_info[i].strip()
			content = content.lower()
			new_1 =content.replace('csi', 'module_id_1')
			new_2 =new_1.replace('pds', 'module_id_2')
			new_3 =new_2.replace('che', 'module_id_3')
			new_4 =new_3.replace('pdc', 'module_id_4')
			new_5 =new_4.replace('pos', 'module_id_5')
			new_6 =new_5.replace('pdf', 'module_id_6')
			new_7 =new_6.replace('b500', '46636')
			new_8 =new_7.replace('b536', '46390')
			new_9 =new_8.replace('e63a', '58938')
			new_10 =new_9.replace('e629', '58921')
			f2.write(new_10)
			f2.write("\n")


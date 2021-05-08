#!/usr/bin/env python3
# coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename      
# * Description   
# * Version       1.0
# * Data          2019.3.28
#***********************************************************************

import pdf_trace_info_analysis as trace_info_analysis

import b5_pde_bin_info as b5_bin_info
import m5_pde_bin_info as m5_bin_info
import ba_pde_bin_info as ba_bin_info
import de_pde_bin_info as de_bin_info

line_count = 0
list_pdf_data_all_info = []

list_data_anaysis = [[] for i in range(40)]

list_pdf_seg_line_trans = []
list_pdf_seg_len_trans  = []
def seg_trans(bin_flag,init_line):
	start_line = init_line
	if bin_flag == "b5":
		pdf_cc_num = 4
		for i in range(pdf_cc_num * 5):
			data_bin =  bin(int(b5_bin_info.list_pde_seg_len[i],16))[2:]
			data_bin = data_bin.zfill(32)
			seg_len = int(data_bin, 2)
			seg_len = int(seg_len/4)
			list_pdf_seg_len_trans.append(seg_len)
			list_pdf_seg_line_trans.append(start_line)
			start_line = start_line + seg_len
	elif bin_flag == "m5":
		pdf_cc_num = 1
		for i in range(pdf_cc_num * 5):
			data_bin =  bin(int(m5_bin_info.list_pde_seg_len[i],16))[2:]
			data_bin = data_bin.zfill(32)
			seg_len = int(data_bin, 2)
			seg_len = int(seg_len/4)
			list_pdf_seg_len_trans.append(seg_len)
			list_pdf_seg_line_trans.append(start_line)
			start_line = start_line + seg_len
	elif bin_flag == "e63a":
		pdf_cc_num = 2
		for i in range(pdf_cc_num * 5):
			data_bin =  bin(int(ba_bin_info.list_pde_seg_len[i],16))[2:]
			data_bin = data_bin.zfill(32)
			seg_len = int(data_bin, 2)
			seg_len = int(seg_len/4)
			list_pdf_seg_len_trans.append(seg_len)
			list_pdf_seg_line_trans.append(start_line)
			start_line = start_line + seg_len
	elif bin_flag == "e629":
		pdf_cc_num = 1
		for i in range(pdf_cc_num * 5):
			data_bin =  bin(int(de_bin_info.list_pde_seg_len[i],16))[2:]
			data_bin = data_bin.zfill(32)
			seg_len = int(data_bin, 2)
			seg_len = int(seg_len/4)
			list_pdf_seg_len_trans.append(seg_len)
			list_pdf_seg_line_trans.append(start_line)
			start_line = start_line + seg_len
	else:
		pdf_cc_num = 1
		for i in range(pdf_cc_num * 5):
			data_bin =  bin(int(b5_bin_info.list_pde_seg_len[i],16))[2:]
			data_bin = data_bin.zfill(32)
			seg_len = int(data_bin, 2)
			seg_len = int(seg_len/4)
			list_pdf_seg_len_trans.append(seg_len)
			list_pdf_seg_line_trans.append(start_line)
			start_line = start_line + seg_len

	#print("list_pdf_seg_line_trans")
	#print(list_pdf_seg_line_trans)
	#print("list_pdf_seg_len_trans")
	#print(list_pdf_seg_len_trans)


def pdf_version_info_analysis(cc_num,list_data):
	#print("list_data")
	#print(list_data[0])
	list_pdf_data_all_info.append("\n/************************************************************************************************/\n")
	list_pdf_data_all_info.append("{} {} {}".format("/**************    pdf version_info_  " , str(cc_num) , "      **************/"))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("dm_ocd_seg : ".ljust(40) , str(list_data[0])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("version_info : ".ljust(40) , str(list_data[1])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("version_info : ".ljust(40) , str(list_data[2])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("version_info : ".ljust(40) , str(list_data[3])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("version_info : ".ljust(40) , str(list_data[4])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("version_info : ".ljust(40) , str(list_data[5])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("version_info : ".ljust(40) , str(list_data[6])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("version_info : ".ljust(40) , str(list_data[7])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("\n")


def pdf_dm_dbg_info_analysis(cc_num,list_data):
	list_pdf_data_all_info.append("\n/************************************************************************************************/\n")
	list_pdf_data_all_info.append("{} {} {}".format("/**************    pdf dm_dbg_info_  " , str(cc_num) , "      **************/"))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pde_debug_en : ".ljust(40) , str(list_data[0])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pde_init_log_ctrl : ".ljust(40) , str(list_data[1])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pde_ndbg_wtd_en : ".ljust(40) , str(list_data[2])))
	list_pdf_data_all_info.append("\n")	
	list_pdf_data_all_info.append("{} {}".format("pde_ndbg_timer_en : ".ljust(40) , str(list_data[3])))
	list_pdf_data_all_info.append("\n")	
	list_pdf_data_all_info.append("{} {}".format("pde_ndbg_ipc_warn_status : ".ljust(40) , str(list_data[4])))
	list_pdf_data_all_info.append("\n")	
	list_pdf_data_all_info.append("{} {}".format("pde_ndbg_assert_info : ".ljust(40) , str(list_data[5])))
	list_pdf_data_all_info.append("\n")	
	list_pdf_data_all_info.append("{} {}".format("pde_ndbg_assert_pc : ".ljust(40) , str(list_data[6])))
	list_pdf_data_all_info.append("\n")						  	
	list_pdf_data_all_info.append("{} {}".format("pde_ndbg_assert_lr : ".ljust(40) , str(list_data[7])))
	list_pdf_data_all_info.append("\n")		
	list_pdf_data_all_info.append("{} {}".format("pde_ndbg_tag_info0 : ".ljust(40) , str(list_data[8])))
	list_pdf_data_all_info.append("\n")		
	list_pdf_data_all_info.append("{} {}".format("pde_ndbg_tag_info1 : ".ljust(40) ,str(list_data[9])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("\n")


def pdf_pdf_info_analysis(cc_num,list_data):
	list_pdf_data_all_info.append("\n/************************************************************************************************/\n")
	list_pdf_data_all_info.append("{} {} {}".format("/**************    pdf pdf_info_   " , str(cc_num) , "      **************/"))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param0: ".ljust(40) ,str(list_data[0])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param1: ".ljust(40) ,str(list_data[1])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param2: ".ljust(40) ,str(list_data[2])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param3: ".ljust(40) ,str(list_data[3])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param4: ".ljust(40) ,str(list_data[4])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param5: ".ljust(40) ,str(list_data[5])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param6: ".ljust(40) ,str(list_data[6])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param7: ".ljust(40) ,str(list_data[7])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param8: ".ljust(40) ,str(list_data[8])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param9: ".ljust(40) ,str(list_data[9])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param10: ".ljust(40) ,str(list_data[10])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param11: ".ljust(40) ,str(list_data[11])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param12: ".ljust(40) ,str(list_data[12])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param13: ".ljust(40) ,str(list_data[13])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param14: ".ljust(40) ,str(list_data[14])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param15: ".ljust(40) ,str(list_data[15])))
	list_pdf_data_all_info.append("\n")		
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param16: ".ljust(40) ,str(list_data[16])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param17: ".ljust(40) ,str(list_data[17])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param18: ".ljust(40) ,str(list_data[18])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param19: ".ljust(40) ,str(list_data[19])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param20: ".ljust(40) ,str(list_data[20])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param21: ".ljust(40) ,str(list_data[21])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param22: ".ljust(40) ,str(list_data[22])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param23: ".ljust(40) ,str(list_data[23])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param24: ".ljust(40) ,str(list_data[24])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param25: ".ljust(40) ,str(list_data[25])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param26: ".ljust(40) ,str(list_data[26])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param27: ".ljust(40) ,str(list_data[27])))
	list_pdf_data_all_info.append("\n")	
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param28: ".ljust(40) ,str(list_data[28])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param29: ".ljust(40) ,str(list_data[29])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param30: ".ljust(40) ,str(list_data[30])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param31: ".ljust(40) ,str(list_data[31])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param32: ".ljust(40) ,str(list_data[32])))
	list_pdf_data_all_info.append("\n")
	list_pdf_data_all_info.append("{} {}".format("pdf_info->param33: ".ljust(40) ,str(list_data[33])))
	list_pdf_data_all_info.append("\n")	


def pdf_trace_info_analysis(cc_num,list_data):
	list_data_trace = trace_info_analysis.read_list_data(cc_num,list_data)
	for i in range(len(list_data_trace)):
		list_pdf_data_all_info.append(list_data_trace[i])


def pdf_stack_info_analysis(cc_num,list_data):
	pass	


def pdf_pde_parse_init():
	list_pdf_data_all_info.clear()
	list_pdf_data_all_info.append(" /***********************************************************************/\n")
	list_pdf_data_all_info.append(" Date          \n")
	list_pdf_data_all_info.append(" /***********************************************************************/\n")
	list_pdf_data_all_info.append(" \n")	
	list_pdf_data_all_info.append(" \n")	
	for i in range(len(list_data_anaysis)):
		list_data_anaysis[i].clear()

def get_pdf_init_line(list_all_info):
	pdf_sec_num_16 = list_all_info[7]
	data_bin =  bin(int(pdf_sec_num_16,16))[2:]
	data_bin = data_bin.zfill(32)
	pdf_sec_num_10 = int(data_bin, 2)
	#print("pdf_sec_num_10")
	#print(pdf_sec_num_10)

	init_line = 64 + 32*pdf_sec_num_10
	init_line = init_line /4
	return init_line


def pdf_read_file(bin_flag,outfile,list_all_info):

	if bin_flag == "b5":
		pdf_cc_num = 4
	elif bin_flag == "m5":
		pdf_cc_num = 1
	elif bin_flag == "e63a":
		pdf_cc_num = 2
	elif bin_flag == "e629":
		pdf_cc_num = 1
	else:
		pdf_cc_num = 1

	init_line = get_pdf_init_line(list_all_info)
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
			for i in range(len(list_pdf_seg_line_trans)):
				if line_num >= list_pdf_seg_line_trans[i] and (line_num < list_pdf_seg_line_trans[i] + list_pdf_seg_len_trans[i]):
					list_data_anaysis[i].append(content)
	#fin.close()

	if(pdf_cc_num == 4): 
		cc_num = 0
		pdf_version_info_analysis(cc_num,list_data_anaysis[0])
		pdf_dm_dbg_info_analysis(cc_num,list_data_anaysis[1])
		pdf_pdf_info_analysis(cc_num,list_data_anaysis[2])
		pdf_trace_info_analysis(cc_num,list_data_anaysis[3])
		pdf_stack_info_analysis(cc_num,list_data_anaysis[4])

		cc_num = cc_num +1
		pdf_version_info_analysis(cc_num,list_data_anaysis[5])
		pdf_dm_dbg_info_analysis(cc_num,list_data_anaysis[6])
		pdf_pdf_info_analysis(cc_num,list_data_anaysis[7])
		pdf_trace_info_analysis(cc_num,list_data_anaysis[8])
		pdf_stack_info_analysis(cc_num,list_data_anaysis[9])

		cc_num = cc_num +1
		pdf_version_info_analysis(cc_num,list_data_anaysis[10])
		pdf_dm_dbg_info_analysis(cc_num,list_data_anaysis[11])
		pdf_pdf_info_analysis(cc_num,list_data_anaysis[12])
		pdf_trace_info_analysis(cc_num,list_data_anaysis[13])
		pdf_stack_info_analysis(cc_num,list_data_anaysis[14])

		cc_num = cc_num +1
		pdf_version_info_analysis(cc_num,list_data_anaysis[15])
		pdf_dm_dbg_info_analysis(cc_num,list_data_anaysis[16])
		pdf_pdf_info_analysis(cc_num,list_data_anaysis[17])
		pdf_trace_info_analysis(cc_num,list_data_anaysis[18])
		pdf_stack_info_analysis(cc_num,list_data_anaysis[19])

	if(pdf_cc_num == 1):  
		cc_num = 0
		pdf_version_info_analysis(cc_num,list_data_anaysis[0])
		pdf_dm_dbg_info_analysis(cc_num,list_data_anaysis[1])
		pdf_pdf_info_analysis(cc_num,list_data_anaysis[2])
		pdf_trace_info_analysis(cc_num,list_data_anaysis[3])
		pdf_stack_info_analysis(cc_num,list_data_anaysis[4])

	if(pdf_cc_num == 2): 
		cc_num = 0
		pdf_version_info_analysis(cc_num,list_data_anaysis[0])
		pdf_dm_dbg_info_analysis(cc_num,list_data_anaysis[1])
		pdf_pdf_info_analysis(cc_num,list_data_anaysis[2])
		pdf_trace_info_analysis(cc_num,list_data_anaysis[3])
		pdf_stack_info_analysis(cc_num,list_data_anaysis[4])

		cc_num = cc_num +1
		pdf_version_info_analysis(cc_num,list_data_anaysis[5])
		pdf_dm_dbg_info_analysis(cc_num,list_data_anaysis[6])
		pdf_pdf_info_analysis(cc_num,list_data_anaysis[7])
		pdf_trace_info_analysis(cc_num,list_data_anaysis[8])
		pdf_stack_info_analysis(cc_num,list_data_anaysis[9])

	with open(outfile, 'w+') as f2:
		for i in range(len(list_pdf_data_all_info)):
			content = list_pdf_data_all_info[i].strip()
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





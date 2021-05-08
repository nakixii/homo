#!/usr/bin/env python3
# coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename      
# * Description      
# * Version       1.0
# * Data          2019.3.28
#***********************************************************************

import re
import trace_pos_module as pos
import trace_pdf_module as pdf
import trace_isr_module as isr
import trace_pdc_module as pdc
import trace_che_module as che
import trace_pds_module as pds
import trace_csi_module as csi

list_data_trace = []
fout_trace_real_info = 0
file_path = ""
line_count = 0

list_trace_less_isr = [1,2,3,4,5,6,
                       9,10,11,12,13,14,15,16,17,18,
                       19,
                       32,
                       35,
                       60,
                       106,
                       ]

module_name = ["NULL","CSI", "PDS", "CHE", "PDC", "POS", "PDF", "ISR"]

def get_hi_lo_32bit(data_bin):
	data_hi_tmp = data_bin[0:32]
	data_lo_tmp = data_bin[32:64]
	hi_temp_list = list(data_hi_tmp)
	lo_temp_list = list(data_lo_tmp)
	data_low_32 = ''
	data_high_32 = ''

	for i in range (32):
		data_low_32 = data_low_32 + lo_temp_list[i]
		if (i + 1) % 4 == 0:
			#data_low_32 = data_low_32 + "  "
			data_low_32 = "{} {}".format(data_low_32, "  ")
	for j in range (32):
		data_high_32 = data_high_32 + hi_temp_list[j]
		if (j + 1) % 4 == 0:
			#data_high_32 = data_high_32 + "  "
			data_high_32 = "{} {}".format(data_high_32, "  ")
	return data_low_32, data_high_32

def check_name_data(info_name_list, info_data_list,fout_trace_real_info):
	if len(info_data_list) % 2 != 0:
		list_data_trace.append( "@@@@ the element num of info_data_list is not the integer multiple of 2! @@@\n")
		return False

	if len(info_data_list) != len(info_name_list) * 2:
		list_data_trace.append( "@@@@ the num of info_data_list is not 2 times that of info_name_list @@@\n")
		return False

	info_num = int(len(info_data_list) / 2)
	for i in range(info_num):
		info_param_idx = i * 2
		info_bit_idx = i * 2 + 1
		if len(info_data_list[info_param_idx]) != len(info_data_list[info_bit_idx]):
			list_data_trace.append("{} {} {}".format("@@@@ the info_param_name doesn't match the info_param_bit in info_data_list[" + str(i) + "] @@@\n"))
			return False
		bit_sum_tmp = sum(info_data_list[info_bit_idx])
		if bit_sum_tmp != 64:
			list_data_trace.append("{} {} {}".format("@@@@ the sum of the info_param_bit is not the 64 in info_data_list[" + str(i) + "] @@@\n"))
			return False
	return True

def trace_less_judge(module_id,sub_module_id):
	trace_less_flag = 0
	if module_id == 7:
		if sub_module_id in list_trace_less_isr:
			trace_less_flag = 1
	return trace_less_flag


def trace_info_analysis(module_bin, timestamp,data_bin, info_name_list, info_data_list,fout_trace_real_info):  

	global line_count
	input_flag = check_name_data(info_name_list, info_data_list, fout_trace_real_info)

	sub_module_id = int(module_bin[-28:-20], 2)
	module_id = int(module_bin[:-28], 2)

	timestamp_bin =  bin(int(timestamp,16))[2:]
	timestamp_bin = timestamp_bin.zfill(32)

	hsym_id = int(timestamp_bin[-1], 2)
	sym_step_cnt = int(timestamp_bin[-7:-1], 2)
	sym_id = int(timestamp_bin[-11:-7], 2)
	slot_id = int(timestamp_bin[-16:-11], 2)
	sfrm_id = int(timestamp_bin[-20:-16], 2)
	frm_id = int(timestamp_bin[-30:-20], 2)
	rsv = int(timestamp_bin[:-30], 2)

	sub_module_id_tmp = sub_module_id
	module_name_tmp = module_name[module_id]

	trace_less_flag = trace_less_judge(module_id,sub_module_id)
	trace_cnt = 0

	if input_flag == 1 and trace_less_flag == 0:
		trace_cnt = int(module_bin[-20:], 2)
		trace_data_lo = int(data_bin[-32:],2)
		trace_data_hi = int(data_bin[:-32],2)
		if sub_module_id_tmp < len(info_name_list):
			list_data_trace.append("{} {} {}".format("module_id : " , str(module_id), "\n"))
			list_data_trace.append("{} {} {}".format("    sub_module_id : " , str(sub_module_id ) , "\n"))
			list_data_trace.append( "{} {} {} {} {}".format("    trace_cnt : " , str(trace_cnt) , " (" , str(hex(trace_cnt)) ,")\n"))
			list_data_trace.append( "{} {} {} {} {}".format("frm_id : " , str(frm_id) , " (" , str(hex(frm_id)) , ")"))
			list_data_trace.append( "{} {} {} {} {}".format("    sfrm_id : " , str(sfrm_id) , " (" , str(hex(sfrm_id)) , ")"))
			list_data_trace.append( "{} {} {} {} {}".format("    slot_id : " , str(slot_id) , " (" , str(hex(slot_id)) , ")"))
			list_data_trace.append( "{} {} {} {} {}".format("    sym_id : " , str(sym_id) , " (" , str(hex(sym_id)) , ")"))
			list_data_trace.append( "{} {} {} {} {}".format("    sym_step_cnt : " , str(sym_step_cnt) , " (" , str(hex(sym_step_cnt)) , ")"))
			list_data_trace.append( "{} {} {} {} {}".format("    hsym_id : " , str(hsym_id) , " (" , str(hex(hsym_id)) , ")\n"))
			list_data_trace.append( "{} {} {} {} {}".format("trace_data_lo : " , str(trace_data_lo) , " (" , str(hex(trace_data_lo)) , ")\n"))
			list_data_trace.append( "{} {} {} {} {}".format("trace_data_hi : " , str(trace_data_hi) , " (" , str(hex(trace_data_hi)) , ")\n\n"))
		else:
			list_data_trace.append("{} {} {}".format("line_num in bin file  : " , str(line_count) , "\n"))
			list_data_trace.append("{} {} {}".format("module_id     : " , str(module_id) , "\n"))
			list_data_trace.append("{} {} {}".format("sub_module_id : " , str(sub_module_id ) , "\n"))
			list_data_trace.append("{} {} {}".format("@@@@ sub_module_id is out of range ! @@@@\n"))
			return

		info_param_idx = sub_module_id_tmp * 2
		info_bit_idx = sub_module_id_tmp * 2 + 1
		param_num = len(info_data_list[info_param_idx])
		start_bit = 0
		end_bit = 0
		 
		for i in range(param_num):
			end_bit = start_bit - info_data_list[info_bit_idx][i]
			if i == 0:
				info_data_dec = int(data_bin[end_bit:],2)
			else:
				info_data_dec = int(data_bin[end_bit:start_bit],2)

			info_data_hex = hex(info_data_dec)
			start_bit = end_bit

	if input_flag == 1 and trace_less_flag == 1:
		trace_data = int(module_bin[-20:], 2)
		if sub_module_id_tmp < len(info_name_list):
			list_data_trace.append("{} {} {}".format("module_id : " , str(module_id), "\n"))
			list_data_trace.append("{} {} {}".format("    sub_module_id : " , str(sub_module_id ) , "\n"))
			list_data_trace.append( "{} {} {} {} {}".format("frm_id : " , str(frm_id) , " (" , str(hex(frm_id)) , ")"))
			list_data_trace.append( "{} {} {} {} {}".format("    sfrm_id : " , str(sfrm_id) , " (" , str(hex(sfrm_id)) , ")"))
			list_data_trace.append( "{} {} {} {} {}".format("    slot_id : " , str(slot_id) , " (" , str(hex(slot_id)) , ")"))
			list_data_trace.append( "{} {} {} {} {}".format("    sym_id : " , str(sym_id) , " (" , str(hex(sym_id)) , ")"))
			list_data_trace.append( "{} {} {} {} {}".format("    sym_step_cnt : " , str(sym_step_cnt) , " (" , str(hex(sym_step_cnt)) , ")"))
			list_data_trace.append( "{} {} {} {} {}".format("    hsym_id : " , str(hsym_id) , " (" , str(hex(hsym_id)) , ")\n"))
			list_data_trace.append( "{} {} {} {} {}".format("trace_data : " , str(trace_data) , " (" , str(hex(trace_data)) , ")\n\n"))
		else:
			list_data_trace.append("{} {} {}".format("line_num in bin file  : " , str(line_count) , "\n"))
			list_data_trace.append("{} {} {}".format("module_id     : " , str(module_id) , "\n"))
			list_data_trace.append("{} {} {}".format("sub_module_id : " , str(sub_module_id ) , "\n"))
			list_data_trace.append("{} {} {}".format("@@@@ sub_module_id is out of range ! @@@@\n"))
			return

		info_param_idx = sub_module_id_tmp * 2
		info_bit_idx = sub_module_id_tmp * 2 + 1
		param_num = len(info_data_list[info_param_idx])
		 
		for i in range(param_num):
			if i == 0:
				info_data_dec = trace_data
			else:
				info_data_dec = 0

			info_data_hex = hex(info_data_dec)

		###################################  next  ###################################
		line_count_tmp = line_count + 2
		list_data_trace.append("{} {} {}".format("**************  PDF_MODULE_ANALYSIS (LINE ",str(line_count_tmp),") ****************\n"))
		module_bin = data_bin[-32:]
		timestamp_bin = data_bin[:-32]
		trace_data = int(module_bin[-20:], 2)
		sub_module_id = int(module_bin[-28:-20], 2)
		module_id = int(module_bin[:-28], 2)
		timestamp_bin =  bin(int(timestamp,16))[2:]
		timestamp_bin = timestamp_bin.zfill(32)

		hsym_id = int(timestamp_bin[-1], 2)
		sym_step_cnt = int(timestamp_bin[-7:-1], 2)
		sym_id = int(timestamp_bin[-11:-7], 2)
		slot_id = int(timestamp_bin[-16:-11], 2)
		sfrm_id = int(timestamp_bin[-20:-16], 2)
		frm_id = int(timestamp_bin[-30:-20], 2)
		rsv = int(timestamp_bin[:-30], 2)

		sub_module_id_tmp = sub_module_id
		module_name_tmp = module_name[module_id]
		if sub_module_id_tmp < len(info_name_list):
			list_data_trace.append( "{} {} {} {} {}".format("module_id : " , str(module_id) , " (" , module_name_tmp , ")"))
			list_data_trace.append("{} {} {}".format("    sub_module_id : " , str(sub_module_id ) ,  "\n"))
			list_data_trace.append( "{} {} {} {} {}".format("frm_id : " , str(frm_id) , " (" , str(hex(frm_id)) , ")"))
			list_data_trace.append( "{} {} {} {} {}".format("    sfrm_id : " , str(sfrm_id) , " (" , str(hex(sfrm_id)) , ")"))
			list_data_trace.append( "{} {} {} {} {}".format("    slot_id : " , str(slot_id) , " (" , str(hex(slot_id)) , ")"))
			list_data_trace.append( "{} {} {} {} {}".format("    sym_id : " , str(sym_id) , " (" , str(hex(sym_id)) , ")"))
			list_data_trace.append( "{} {} {} {} {}".format("    sym_step_cnt : " , str(sym_step_cnt) , " (" , str(hex(sym_step_cnt)) , ")"))
			list_data_trace.append( "{} {} {} {} {}".format("    hsym_id : " , str(hsym_id) , " (" , str(hex(hsym_id)) , ")\n"))
			list_data_trace.append( "{} {} {} {} {}".format("trace_data : " , str(trace_data) , " (" , str(hex(trace_data)) , ")\n\n"))
		else:
			list_data_trace.append("{} {} {}".format("line_num in bin file  : " , str(line_count) , "\n"))
			list_data_trace.append("{} {} {}".format("module_id     : " , str(module_id) , "\n"))
			list_data_trace.append("{} {} {}".format("sub_module_id : " , str(sub_module_id ) , "\n"))
			list_data_trace.append( "@@@@ sub_module_id is out of range ! @@@@\n")
			return

		info_param_idx = sub_module_id_tmp * 2
		info_bit_idx = sub_module_id_tmp * 2 + 1
		param_num = len(info_data_list[info_param_idx])
		 
		for i in range(param_num):
			if i == 0:
				info_data_dec = trace_data
			else:
				info_data_dec = 0

			info_data_hex = hex(info_data_dec)


def analysis_data(module,timestamp, data_hi_32, data_low_32): 

	global line_count
	data_hi_flag_hex = re.match('^[0-9a-fA-F]+$', data_hi_32)
	data_low_flag_hex = re.match('^[0-9a-fA-F]+$', data_low_32)
	data_module_flag_hex = re.match('^[0-9a-fA-F]+$', module)

	module_bin = bin(int(module,16))[2:]
	module_bin = module_bin.zfill(32)
	sub_module_id = int(module_bin[-28:-20], 2)
	module_id = int(module_bin[:-28], 2)

	if ( '' == module ):
		list_data_trace.append( "****************  ERROR ****************\n")
		list_data_trace.append("{} {} {}".format("line_num in trace data file  : " , str(line_count) , "\n"))
		list_data_trace.append( "@@@@ module_id parameter is empty! @@@\n")
		return
	elif ('' == data_hi_32 ):
		list_data_trace.append( "****************  ERROR ****************\n")
		list_data_trace.append("{} {} {}".format("line_num in trace data file  : " , str(line_count) , "\n"))
		list_data_trace.append( "@@@@ data_hi_32 parameter is empty! @@@@\n")
		return
	elif ('' == data_low_32 ):
		list_data_trace.append( "****************  ERROR ****************\n")
		list_data_trace.append("{} {} {}".format("line_num in trace data file  : " , str(line_count) , "\n"))
		list_data_trace.append( "@@@@ data_low_32 parameter is empty! @@@@\n")
		return
	elif (data_hi_flag_hex == None or data_low_flag_hex == None or data_module_flag_hex == None):
		list_data_trace.append( "****************  ERROR ****************\n")
		list_data_trace.append("{} {} {}".format("line_num in trace data file  : " , str(line_count) , "\n"))
		list_data_trace.append( "@@@@ data parameters is wrong dec! @@@@\n")
		return
	elif len(data_hi_32) > 8:
		list_data_trace.append( "****************  ERROR ****************\n")
		list_data_trace.append("{} {} {}".format("line_num in trace data file  : " , str(line_count) , "\n"))
		list_data_trace.append( "@@@@ the length of data_hi_32 is greater than 8 ! @@@@\n")
		return
	elif len(data_low_32) > 8:
		list_data_trace.append( "****************  ERROR ****************\n")
		list_data_trace.append("{} {} {}".format("line_num in trace data file  : " , str(line_count) , "\n"))
		list_data_trace.append( "@@@@ the length of data_low_32 is greater than 8 ! @@@@\n")
		return
	elif module_id > 7:
		list_data_trace.append( "****************  ERROR ****************\n")
		list_data_trace.append("{} {} {}".format("line_num in trace data file  : " , str(line_count) , "\n"))
		list_data_trace.append( "@@@@ module_id is out of range !  @@@@\n")
		return

	data_hi_32_bin = bin(int(data_hi_32,16))[2:]       # high to low bit from left to right
	data_hi_32_bin = data_hi_32_bin.zfill(32)

	data_low_32_bin = bin(int(data_low_32,16))[2:]       # high to low bit from left to right
	data_low_32_bin = data_low_32_bin.zfill(32)

	data_bin = "{} {}".format(data_hi_32_bin, data_low_32_bin)

	if module_id == 5 : 
		list_data_trace.append("{} {} {}".format("**************  Module_id == 5_ANALYSIS (LINE ",str(line_count),") ****************\n"))
		trace_info_analysis(module_bin,timestamp, data_bin, pos.pos_info_name_list, pos.pos_info_data_list,fout_trace_real_info) 
	elif module_id == 6 :
		list_data_trace.append("{} {} {}".format("**************  Module_id == 6_ANALYSIS (LINE ",str(line_count),") ****************\n"))
		trace_info_analysis(module_bin,timestamp, data_bin, pdf.pdf_info_name_list, pdf.pdf_info_data_list,fout_trace_real_info)
	elif module_id == 7:
		list_data_trace.append("{} {} {}".format("**************  Module_id == 7_ANALYSIS (LINE ",str(line_count),") ****************\n"))
		trace_info_analysis(module_bin,timestamp, data_bin, isr.isr_info_name_list, isr.isr_info_data_list,fout_trace_real_info)
	elif module_id == 4:
		list_data_trace.append("{} {} {}".format("**************  Module_id == 4_ANALYSIS (LINE ",str(line_count),") ****************\n"))
		trace_info_analysis(module_bin,timestamp,  data_bin, pdc.pdc_info_name_list, pdc.pdc_info_data_list,fout_trace_real_info)
	elif module_id == 3:
		list_data_trace.append("{} {} {}".format("**************  Module_id == 3_ANALYSIS (LINE ",str(line_count),") ****************\n"))
		trace_info_analysis(module_bin, timestamp, data_bin, che.che_info_name_list, che.che_info_data_list,fout_trace_real_info)
	elif module_id == 2:
		list_data_trace.append("{} {} {}".format("**************  Module_id == 2_ANALYSIS (LINE ",str(line_count),") ****************\n"))
		trace_info_analysis(module_bin, timestamp, data_bin, pds.pds_info_name_list, pds.pds_info_data_list,fout_trace_real_info)
	elif module_id == 1:
		list_data_trace.append("{} {} {}".format("**************  Module_id == 1_ANALYSIS (LINE ",str(line_count),") ****************\n"))
		trace_info_analysis(module_bin,timestamp,  data_bin, csi.csi_info_name_list, csi.csi_info_data_list,fout_trace_real_info)
	else:
		list_data_trace.append( "@@@ module_id is out of range ! @@@\n")



def read_list_data(cc_num,list_data):
	list_data_trace.clear()

	list_data_trace.append("\n/************************************************************************************************/\n")
	list_data_trace.append("{} {} {}".format("/**************    trace_info_  ", str(cc_num),"      **************/"))
	list_data_trace.append("\n")

	list_data_trace.append("pde_time_stat_info:")
	list_data_trace.append("\n")

	list_data_trace.append("{} {}".format("Module_id_6_TIME_STAT : ".ljust(40), str(list_data[0])))
	list_data_trace.append("\n")
	list_data_trace.append("{} {}".format("Module_id_4_TIME_STAT : ".ljust(40), str(list_data[1])))
	list_data_trace.append("\n")
	list_data_trace.append("{} {}".format("Module_id_3_TIME_STAT : ".ljust(40), str(list_data[2])))
	list_data_trace.append("\n")
	list_data_trace.append("{} {}".format("Module_id_2_TIME_STAT : ".ljust(40), str(list_data[3])))
	list_data_trace.append("\n")

	list_data_trace.append("\n")
	list_data_trace.append("pde_trace_info:")
	list_data_trace.append("\n")
	i = 4
	global line_count
	line_count = 0
	param_cnt = 0
	list_data = list_data[4:]
	for i in range(len(list_data)):
		if param_cnt == 0:
			module = list_data[i][2:]
			param_cnt = param_cnt +1
			continue
		if param_cnt == 1:	
			timestamp = list_data[i][2:]
			param_cnt = param_cnt +1
			continue
		if param_cnt == 2:
			data_low_32 = list_data[i][2:]
			param_cnt = param_cnt +1
			continue
		if param_cnt == 3:
			data_hi_32 = list_data[i][2:]
			analysis_data(module, timestamp,data_hi_32, data_low_32)
			param_cnt = 0
			line_count=line_count+4

	return list_data_trace

	


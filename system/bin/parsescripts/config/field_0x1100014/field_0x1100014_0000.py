#!/usr/bin/env python3
# coding=utf-8
"""
功能： pcdev模块dump明文化
版权信息：华为技术有限公司，版权所有（C）2010-2019
修改记录：
"""

import struct
import os
import sys
import string

pcdev_field_def = [
	"port_start",
	"port_num",
	"ev_status local_stat",
	"ev_status remote_stat",
	"dmamap_skip",
	"rx_wp",
	"rx_rp",
	"rx_rp_toget",
	"rx_rp_process",
	"rx_buf_max_size",
	"rx_num",
	"tx_wp",
	"tx_rp",
	"tx_rp_todo",
	"tx_rp_complete",
	"tx_buf_max_sz",
	"tx_num",
	"write_sync",
	"write_blocked",
	"tx_rp_todo_rc",
	"tx_rp_dma_cmp_rc",
	"tx_rp_dma_cfg_rc",
	"tx_rp_cmp",
	"open_count",
	"close_count",
	"close_count_repeat",
	"openclose",
	"remote_close",
	"local_close",
	"irq_send",
	"event_send",
	"event_cb_call",
	"event_cb_null",
	"tx_empty",
	"tx_full",
	"tx_todo_full",
	"tx_desc_null",
	"tx_desc_err",
	"tx_buf_size_err",
	"kick_dma_transfer",
	"kick_dma_transfer_fail",
	"tx_dma_send_complete",
	"write_base",
	"tx_packets",
	"tx_packets_finish",
	"tx_packets_cb",
	"tx_packets_fail",
	"write_cb_call",
	"write_info_cb_call",
	"write_cb_null",
	"write_async_call",
	"sync_tx_submit",
	"sync_tx_wait_fail",
	"sync_tx_done",
	"sync_tx_fail",
	"rx_close",
	"rx_empty",
	"rx_todo_empty",
	"rx_process_empty",
	"rx_full",
	"rx_desc_null",
	"rx_desc_err",
	"rx_get_bur_err",
	"rx_packets",
	"rx_packets_finish",
	"rx_packets_fail",
	"rx_bytes",
	"rx_get_buf_pram_err",
	"get_buf_call",
	"ret_buf_call",
	"read_cb_call",
	"read_cb_null",
]

def PrintPcdevInfo(infile, field, offset, slen, version, mode, outfile):
		max_port_num = 17
		i = 0
		j = 0
		MyOffset = eval(offset)
		infile.seek(MyOffset)
		print("got entry 0x1100014 PrintPcdevInfo")
		outfile.writelines("============PCDEV dma addr============\n")
		for i in range(0, max_port_num):
			(v_addr, ) = struct.unpack('Q',infile.read(8))
			(p_addr_low, ) = struct.unpack('I',infile.read(4))
			(p_addr_high, ) = struct.unpack('I',infile.read(4))
			outfile.writelines("port tx(%08d): 0x%16x 0x%08x 0x%08x\n" %(i, v_addr, p_addr_low, p_addr_high))
		for i in range(0, max_port_num):
			(v_addr, ) = struct.unpack('Q',infile.read(8))
			(p_addr_low, ) = struct.unpack('I',infile.read(4))
			(p_addr_high, ) = struct.unpack('I',infile.read(4))
			outfile.writelines("port rx(%08d): 0x%16x 0x%08x 0x%08x\n" %(i, v_addr, p_addr_low, p_addr_high))

		outfile.writelines("============PCDEV ctx info===========\n")
		(p_addr, ) = struct.unpack('Q',infile.read(8))
		(v_addr, ) = struct.unpack('Q',infile.read(8))
		(size, ) = struct.unpack('Q',infile.read(8))
		outfile.writelines("pcdev info: phy=0x%16x vir=0x%16x size=0x%8x\n" %(p_addr, v_addr, size))
		
		outfile.writelines("============PCDEV vote info===========\n")
		for i in range(0, max_port_num+1):
			(vote, ) = struct.unpack('Q',infile.read(8))
			(vote_fail, ) = struct.unpack('Q',infile.read(8))
			(vote_lasttime, ) = struct.unpack('Q',infile.read(8))
			(mode, ) = struct.unpack('Q',infile.read(8))
			(unvote, ) = struct.unpack('Q',infile.read(8))
			(unvote_lasttime, ) = struct.unpack('Q',infile.read(8))
			(unmode, ) = struct.unpack('Q',infile.read(8))
			outfile.writelines("port vote  (%08d): %16d %16d %8d %16d\n" %(i, vote, vote_lasttime, mode, vote_fail))
			outfile.writelines("port unvote(%08d): %16d %16d %8d\n" %(i, unvote,  unvote_lasttime, unmode))
		
		outfile.writelines("============PCDEV ports info===========\n")
		for i in range(0, max_port_num):
			outfile.writelines("============PCDEV port(%d) info===========\n" %i)
			for j in range(0, int(len(pcdev_field_def))):
				(reg, ) = struct.unpack("I", infile.read(4))
				outfile.writelines("%s = 0x%08x\n" %(pcdev_field_def[j], reg))
		return
 	
def entry_0x1100014(infile, field, offset, slen, version, mode, outfile):
        try:
            if not field == '0x1100014':
                print('hidis field is ', field)
                print('current field is', '0x1100014')
                return error['ERR_CHECK_FIELD']
            elif not version == '0x0000':
                print('hidis version is ', version)
                print('current version is ', '0x0000')
                return error['ERR_CHECK_VERSION']
            elif not slen == '0x2000':
                print('hids len is ', slen)
                print('current len is ', '0x2000')
                return error['ERR_CHECK_LEN']
            print("got entry 0x1100014")
            PrintPcdevInfo(infile, field, offset, slen, version, mode, outfile)
            return 0

        except Exception as e:
            print(str(e))
            outfile.writelines(str(e))
            return 1

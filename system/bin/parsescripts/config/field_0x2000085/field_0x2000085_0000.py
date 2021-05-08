#!/usr/bin/env python3
# coding=utf-8 
# Copyright (C) Huawei Technologies Co., Ltd. 2010-2020. All rights reserved.
#######################################################################################################################################
#   filename		:   field_0x2000085_0000.py
#
#   description	 :   parse EDMA dump mem
#
#   modify  record  :   2017-01-23 create file
#
#######################################################################################################################################
import struct
from config import *
edma_dump_globa_regs = (
    "EDMA_INT_TC1_RAW     ",
    "EDMA_INT_TC2_RAW     ",
    "EDMA_INT_ERR1_RAW    ",
    "EDMA_INT_ERR2_RAW    ",
    "EDMA_INT_ERR3_RAW    ",
    "EDMA_CH_PRI          ",
    "EDMA_CH_STAT         ",
    "EDMA_SEC_CTRL        ",
    "EDMA_DMA_CTRL        ",
	)
########################################################################################
def ExpaseEDMA(infile,  offset, outfile,chan_num):
	infile.seek(offset+0)
	#  channels_curr_regs  
	print(" --------------------- channels_curr_regs --------------------- ", file=outfile)
	print("%s  %-6s %-11s %-11s %-11s" %("CX_ID     ", "CURR_CNT1    ", "CURR_CNT0    ", "CURR_SRC_ADDR", "CURR_DES_ADDR"), file=outfile)
	for index in range(chan_num):
		(value0, )    = struct.unpack('I', infile.read(4))
		(value1, )    = struct.unpack('I', infile.read(4))
		(value2, )    = struct.unpack('I', infile.read(4))
		(value3, )    = struct.unpack('I', infile.read(4))
		print("chan:0x%x    0x%.8x    0x%.8x    0x%.8x    0x%.8x" %(index, value0, value1, value2, value3), file=outfile)
	#  channels_config_regs  
	print(" --------------------- channels_config_regs --------------------- ", file=outfile)
	print("%s  %-6s %-11s %-11s %-11s" %("CX_ID     ", "CX_LLI       ","CX_BINDX     ","CX_CINDX     ","CX_CNT1     "), file=outfile)
	print("%s  %-6s %-11s %-11s %-11s" %("          ", "CX_CNT0      ","CX_SRC_ADDR  ","CX_DES_ADDR  ","CX_CONFIG   "), file=outfile)
	for index in range(chan_num):
		(value0, )    = struct.unpack('I', infile.read(4))
		(value1, )    = struct.unpack('I', infile.read(4))
		(value2, )    = struct.unpack('I', infile.read(4))
		(value3, )    = struct.unpack('I', infile.read(4))
		print("chan:0x%x    0x%.8x    0x%.8x    0x%.8x    0x%.8x" %(index, value0, value1, value2, value3), file=outfile)
		(value0, )    = struct.unpack('I', infile.read(4))
		(value1, )    = struct.unpack('I', infile.read(4))
		(value2, )    = struct.unpack('I', infile.read(4))
		(value3, )    = struct.unpack('I', infile.read(4))
		print("            0x%.8x    0x%.8x    0x%.8x    0x%.8x" %( value0, value1, value2, value3), file=outfile)
	#  edma_global_regs  
	print(" --------------------- edma_global_regs --------------------- ", file=outfile)
	print("                       for \"EDMA_INT_xx_RAW\", bitX=1 means channel X has Interrupt  ", file=outfile)
	for index in range(len(edma_dump_globa_regs)):
		(value, )    = struct.unpack('I', infile.read(4))
		print("%s 0x%.8x" %(edma_dump_globa_regs[index], value), file=outfile)
	print(" --------------------- end of one edma dump ----------------\n ", file=outfile)
def PrintEDMAData(infile, field, offset, slen, version, mode, outfile):
		addr = 0
		row = 0
		i = 0
		MyOffset = eval(offset)
		infile.seek(MyOffset)
		print("got entry 0x2000085 PrintEDMAData")
		outfile.writelines("offset      data\n")
		for i in range(0, int(int(slen,16)/16)):
			(charbyte1, charbyte2, charbyte3,charbyte4, ) = struct.unpack("IIII", infile.read(16))
			addr = 0x10 * row
			row = row + 1
			#print >> outhandler, "0x%08x: %08x %08x %08x %08x" %(addr, charbyte1, charbyte2, charbyte3, charbyte4)
			outfile.writelines("0x%08x: %08x %08x %08x %08x\n" %(addr, charbyte1, charbyte2, charbyte3, charbyte4))
		return
def ExpaseEDMA_ALL(outfile):
	print("%s" %("|||||||||||||||||||||||||||||||||||||||||||||||"), file=outfile)
	print("%s" %("||||                                       ||||"), file=outfile)
	print("%s" %("|||| EDMA0[0~0x1000), EDMA1[0x1000~0x2000) ||||"), file=outfile)
	print("%s" %("|||| All Regs are described as follows     ||||"), file=outfile)
	print("%s" %("|||| in:number of interrupts for cpus      ||||"), file=outfile)
	print("%s" %("|||| cn:number of channels                 ||||"), file=outfile)
	print("%s" %("||||                                       ||||"), file=outfile)
	print("%s" %("|||||||||||||||||||||||||||||||||||||||||||||||"), file=outfile)
	print("%s" %("                                               "), file=outfile)
	print("%s" %("==== int status&mask:11regs x X cores ====     "), file=outfile)
	print("%s" %("EDMA_INT_STAT       0x0000+0x40*in             "), file=outfile)
	print("%s" %("EDMA_INT_TC1        0x0004+0x40*in             "), file=outfile)
	print("%s" %("EDMA_INT_TC2        0x0008+0x40*in             "), file=outfile)
	print("%s" %("EDMA_INT_ERR1       0x000C+0x40*in             "), file=outfile)
	print("%s" %("EDMA_INT_ERR2       0x0010+0x40*in             "), file=outfile)
	print("%s" %("EDMA_INT_ERR3       0x0014+0x40*in             "), file=outfile)
	print("%s" %("EDMA_INT_TC1_MASK   0x0018+0x40*in             "), file=outfile)
	print("%s" %("EDMA_INT_TC2_MASK   0x001C+0x40*in             "), file=outfile)
	print("%s" %("EDMA_INT_ERR1_MASK  0x0020+0x40*in             "), file=outfile)
	print("%s" %("EDMA_INT_ERR2_MASK  0x0024+0x40*in             "), file=outfile)
	print("%s" %("EDMA_INT_ERR3_MASK  0x0028+0x40*in             "), file=outfile)
	print("%s" %("                                               "), file=outfile)
	print("%s" %("==== interrupt raw status 5regs ====           "), file=outfile)
	print("%s" %("EDMA_INT_TC1_RAW    0x0600                     "), file=outfile)
	print("%s" %("EDMA_INT_TC2_RAW    0x0608                     "), file=outfile)
	print("%s" %("EDMA_INT_ERR1_RAW   0x0610                     "), file=outfile)
	print("%s" %("EDMA_INT_ERR2_RAW   0x0618                     "), file=outfile)
	print("%s" %("EDMA_INT_ERR3_RAW   0x0620                     "), file=outfile)
	print("%s" %(" xx_RAW bitX=1 means channel X has Interrupt   "), file=outfile)
	print("%s" %("                                               "), file=outfile)
	print("%s" %("==== req 5regs ====                            "), file=outfile)
	print("%s" %("EDMA_SREQ           0x660                      "), file=outfile)
	print("%s" %("EDMA_LSREQ          0x664                      "), file=outfile)
	print("%s" %("EDMA_BREQ           0x668                      "), file=outfile)
	print("%s" %("EDMA_LBREQ          0x66C                      "), file=outfile)
	print("%s" %("EDMA_FREQ           0x670                      "), file=outfile)
	print("%s" %("EDMA_LFREQ          0x674                      "), file=outfile)
	print("%s" %("                                               "), file=outfile)
	print("%s" %("==== some other reg: 4regs ====                "), file=outfile)
	print("%s" %("EDMA_CH_PRI         0x688                      "), file=outfile)
	print("%s" %("EDMA_CH_STAT        0x690                      "), file=outfile)
	print("%s" %(" EDMA_CH_STAT bitX=1 means channel X is working"), file=outfile)
	print("%s" %("EDMA_SEC_CTRL       0x0694                     "), file=outfile)
	print("%s" %("EDMA_DMA_CTRL       0x0698                     "), file=outfile)
	print("%s" %("                                               "), file=outfile)
	print("%s" %("==== curr 4regs x 16channels ====              "), file=outfile)
	print("%s" %("CX_CURR_CNT1        0x0700+0x10*cn             "), file=outfile)
	print("%s" %("CX_CURR_CNT0        0x0704+0x10*cn             "), file=outfile)
	print("%s" %("CX_CURR_SRC_ADDR    0x0708+0x10*cn             "), file=outfile)
	print("%s" %("CX_CURR_DES_ADDR    0x070C+0x10*cn             "), file=outfile)
	print("%s" %("                                               "), file=outfile)
	print("%s" %("==== config 9regs x 16channels ====            "), file=outfile)
	print("%s" %("CX_LLI              0x0800+0x40*cn             "), file=outfile)
	print("%s" %("CX_BINDX            0x0804+0x40*cn             "), file=outfile)
	print("%s" %("CX_CINDX            0x0808+0x40*cn             "), file=outfile)
	print("%s" %("CX_CNT1             0x080C+0x40*cn             "), file=outfile)
	print("%s" %("CX_CNT0             0x0810+0x40*cn             "), file=outfile)
	print("%s" %("CX_SRC_ADDR         0x0814+0x40*cn             "), file=outfile)
	print("%s" %("CX_DES_ADDR         0x0818+0x40*cn             "), file=outfile)
	print("%s" %("CX_CONFIG           0x081C+0x40*cn             "), file=outfile)
	print("%s" %("CX_AXI_CONF         0x0820+0x40*cn             "), file=outfile)
	print("%s" %("                                               "), file=outfile)
	print("%s" %("|||||||||||||||||||||||||||||||||||||||||||||||"), file=outfile)
	print("%s" %("|||| Regs description ends                 ||||"), file=outfile)
	print("%s" %("|||||||||||||||||||||||||||||||||||||||||||||||"), file=outfile)
	print("%s" %("                                               "), file=outfile)
	
########################################################################################
def entry_0x2000085(infile, field, offset, len, version, mode, outfile):
		########check parameter start#############
		if not field == '0x2000085':
			print('hidis field is ', field)
			print('current field is', '0x2000085')
			return error['ERR_CHECK_FIELD']
		elif not version == '0x0000':
			print('hidis version is ', version)
			print('current version is ', '0x0000')
			return error['ERR_CHECK_VERSION']
		elif len == '0x1000':
			ExpaseEDMA_ALL(outfile)
			return 0
		elif len == '0x2000':
			ExpaseEDMA_ALL(outfile)
			PrintEDMAData(infile, field, offset, len, version, mode, outfile)
			return 0
		elif len == '0x3000':
			ExpaseEDMA_ALL(outfile)
			return 0
		elif len == '0x800':
			######### dump_parse ##############
			print("[ EDMA 0 ] dump parse", file=outfile)
			ExpaseEDMA(infile, ( eval(offset)),  outfile,16)
			print("[ EDMA 1 ] dump parse <After Dallas>, channel num=16, ", file=outfile)
			print("[ EDMA 1 ] dump parse <for Dallas>, channel num=12, <see page down>", file=outfile)
			ExpaseEDMA(infile, ( eval(offset)+0x400),  outfile,16)
			print("[ EDMA 1 ] dump parse, <Dallas> channel num=12", file=outfile)
			ExpaseEDMA(infile, ( eval(offset)+0x400),  outfile,12)
			return 0
		else:
			print('ERROR hids len is ', len)
			return error['ERR_CHECK_LEN']

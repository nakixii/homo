# -*- coding: utf-8 -*-
# ccore drx
import struct
import os
import sys
import string
import config

def PrintExcInfoPm(infile, field, offset, slen, version, mode, outfile):
		MyOffset = eval(offset)
		infile.seek(MyOffset)
		(cpu0_wakeup_cnt,cpu1_wakeup_cnt, ) = struct.unpack("II", infile.read(8))
		(cpu0_sleep_cnt,cpu1_sleep_cnt, ) = struct.unpack("II", infile.read(8))
		outfile.writelines("cpu0_wakeup_cnt 0x%x,sleep_cnt 0x%x\n" %(cpu0_wakeup_cnt, cpu0_sleep_cnt))
		outfile.writelines("cpu1_wakeup_cnt 0x%x,sleep_cnt 0x%x\n" %(cpu1_wakeup_cnt, cpu1_sleep_cnt))
		for i in range(0, 2):
			outfile.writelines("cpu%d wakeup slice"%(i))
			for j in range(0, 11):
				(wakeup_slice, ) = struct.unpack("I", infile.read(4))
				outfile.writelines("step%d:0x%x"%(j, wakeup_slice))
		for i in range(0, 2):
			outfile.writelines("cpu%d sleep slice"%(i))
			for j in range(0, 11):
				(sleep_slice, ) = struct.unpack("I", infile.read(4))
				outfile.writelines("step%d:0x%x"%(j, sleep_slice))
		return

def PrintExcInfoWakelock(infile, field, offset, slen, version, mode, outfile):
		MyOffset = eval(offset)
		infile.seek(MyOffset+0X400)
		outfile.writelines("wakelock total lock time\n")
		for i in range(0, 32):
			(total_slice, ) = struct.unpack("I", infile.read(4))
			outfile.writelines("wakelock%d:0x%x\n"%(i, total_slice))
		(latest_locktime, )   = struct.unpack("I", infile.read(4))
		(latest_lockid, )     = struct.unpack("I", infile.read(4))
		(latest_unlocktime, ) = struct.unpack("I", infile.read(4))
		(latest_unlockid, )   = struct.unpack("I", infile.read(4))
		outfile.writelines("latest lock id:0x%x,latest lock time 0x%x\n"%(latest_lockid, latest_locktime))
		outfile.writelines("latest unlock id:0x%x,latest unlock time 0x%x\n"%(latest_unlockid, latest_unlocktime))
		(lock_state, )   = struct.unpack("I", infile.read(4))
		outfile.writelines("lock state 0x%x\n"%(lock_state))
		return

def PrintExcInfoDpm(infile, field, offset, slen, version, mode, outfile):
		MyOffset = eval(offset)
		infile.seek(MyOffset+0X800)
		outfile.writelines("dpm info\n")
		for i in range(0, 7):
			(name, deviceaddr, fail_cnt, max_s, max_r ) = struct.unpack("8s4I", infile.read(24))
			outfile.writelines("name:%s,fail_cnt:0x%x,max_s:0x%x,max_r:0x%x\n"%(name, fail_cnt, max_s, max_r))
			print("name:%s,fail_cnt:0x%x,max_s:0x%x,max_r:0x%x\n"%(name, fail_cnt, max_s, max_r))
		return
def entry_0x800000E(infile, field, offset, len, version, mode, outfile):
	print("entry_0x800000E,HAC PM")
	if not field == '0x800000E':
		print("hidis field is 0x%x"%(field))
		print("current field is 0x800000E")
		return error['ERR_CHECK_FIELD']
	elif not len == '0x900':
		print("hids len is 0x%x"%(len))
		print("current len is 0x900")
		return error['ERR_CHECK_LEN']
	#########check parameter end##############
	PrintExcInfoWakelock(infile, field, offset, len, version, mode, outfile)
	PrintExcInfoPm(infile, field, offset, len, version, mode, outfile)
	PrintExcInfoDpm(infile, field, offset, len, version, mode, outfile)
	return 0
#!/usr/bin/env python3
# coding=utf-8 
# Copyright (C) Huawei Technologies Co., Ltd. 2010-2020. All rights reserved.

import sys
import config
import struct
#from config import *

#global BBP_STAMP_TF
#global BBP_STAMP_SR
#global ABB_STAMP_SR

BBP_VOTE_PWR_NUM  = 5
BBP_VOTE_CLK_NUM = 62
BBP_MODULE_NUM = 4
BBP_MODEM_NUM = 3
BBP_MODE_NUM = 6

ABB_STAMP_SR = {
    0:("suspend_start_stamp"),
    1:("suspend_end_stamp"),
    2:("resume_start_stamp"),
    3:("resume_end_stamp"),
    4:("gpll_vote"),
    5:("gpll_enable_stamp"),
    6:("gpll_lock_stamp"),
    7:("gpll_disable_stamp"),
    8:("scpll_vote"),
    9:("scpll_enable_stamp"),
    10:("scpll_lock_stamp"),
    11:("scpll_disable_stamp")        
};
ABB_STAMP_PLL = {
     0: ("BBP_LTEINT_EN_IN"),        
     1: ("BBP_LTEINT_EN_CLS"),       
     2: ("BBP_LTEINT_EN_UNMASK"),    
     3: ("BBP_LTEINT_DIS_IN"),       
     4: ("BBP_LTEINT_DIS_MASK"),     
     5: ("BBP_LTEINT_HANDLE_FUNC"),  
     6: ("BBP_LTEINT_CLEAR_IN"),     
     7: ("BBP_LTEINT_CLEAR_CLS"),    
     8: ("BBP_TDSINT_EN_IN"),          
     9: ("BBP_TDSINT_EN_CLS"),         
     10: ("BBP_TDSINT_EN_UNMASK"),      
     11: ("BBP_TDSINT_DIS_IN"),         
     12: ("BBP_TDSINT_DIS_MASK"),       
     13: ("BBP_TDSINT_CLEAR_IN"),       
     14: ("BBP_TDSINT_CLEAR_CLS"),      
     15: ("BBP_TDSINT_HANDLE_FUNC")   
};

BBP_STAMP_TF = {
     0: ("BBP_LTEINT_EN_IN"),        
     1: ("BBP_LTEINT_EN_CLS"),       
     2: ("BBP_LTEINT_EN_UNMASK"),    
     3: ("BBP_LTEINT_DIS_IN"),       
     4: ("BBP_LTEINT_DIS_MASK"),     
     5: ("BBP_LTEINT_HANDLE_FUNC"),  
     6: ("BBP_LTEINT_CLEAR_IN"),     
     7: ("BBP_LTEINT_CLEAR_CLS"), 
     8:    ("BBP_LTE1INT_EN_IN"),
     9: ("BBP_LTE1INT_EN_CLS"),
     10: ("BBP_LTE1INT_EN_UNMASK"),
     11: ("BBP_LTE1INT_DIS_IN"),
     12: ("BBP_LTE1INT_DIS_MASK"),
     13: ("BBP_LTE1INT_HANDLE_FUNC"),
     14: ("BBP_LTE1INT_CLEAR_IN"),
     15: ("BBP_LTE1INT_CLEAR_CLS"),
     16: ("BBP_TDSINT_EN_IN"),          
     17: ("BBP_TDSINT_EN_CLS"),         
     18: ("BBP_TDSINT_EN_UNMASK"),      
     19: ("BBP_TDSINT_DIS_IN"),         
     20: ("BBP_TDSINT_DIS_MASK"),    
     21: ("BBP_TDSINT_CLEAR_IN"),       
     22: ("BBP_TDSINT_CLEAR_CLS"),      
     23: ("BBP_TDSINT_HANDLE_FUNC") 
};
BBP_STAMP_SR = {
     0: ("BBP_PREPAIR_IN"),            
     1: ("BBP_PREPAIR_END"),           
     2: ("BBP_SUSPEND_IN"),            
     3: ("BBP_SUSPEND_BBCRST"),        
     4: ("BBP_SUSPEND_END"),
     5: ("BBP_RESUME_IN"),
     6: ("BBP_RESUME_BBCUNRST"),
     7: ("BBP_RESUME_END"),
     8: ("BBP_COMPLETE_IN"),
     9: ("BBP_COMPLETE_END"),
     10: ("BBP_DMATRAN_IN"),
     11: ("BBP_DMATRAN_CLKEN"),
     12: ("BBP_DMATRAN_ADDR"),
     13: ("BBP_DMATRAN_END"),
     14: ("BBP_DMAFINISH_IN"),
     15: ("BBP_DMAFINISH_BUSY"),
     16: ("BBP_DMAFINISH_END"),
     17: ("BBP_DMACONFIG")
};

BBP_DMA = {
    0: ("dma_clkcnt"),
    1: ("dma_sts"),
    2: ("fast_chn_dbg"),
    3: ("dma_stat")
};

def parse_abb_timestamp(infile, offset, outfile):
#    print 'PrintStamp in ABB2'
    print("PrintStamp in ABB2")
#    infile.seek(offset-0x30)
    infile.seek(offset,0)

    s1 = "******************* [%s] ********************\n" % ('stamp_abb_sr')
    outfile.writelines(s1)
    outfile.writelines('%-30s%-20s\n' %('name', 'timestamp'))
    for i in range(0, 12):
        (stamp_abbsr, ) = struct.unpack('I', infile.read(4))
        outfile.writelines('%-30s %#-20x \n' % (ABB_STAMP_SR[i], stamp_abbsr&0xFFFFFFFF))
        
    s1 = "******************* [%s] ********************\n" % ('init_state')
    outfile.writelines(s1)
    outfile.writelines('%-20s %-20s\n' %('init_id', 'init_sate'))
    for i in range(0,6):
        (init_state, ) = struct.unpack('i', infile.read(4))
        outfile.writelines('%-20d %-20x \n' % (i, init_state)) 
    
    s1 = "******************* [%s] ********************\n" % ('stamp_abb_pll')
    outfile.writelines(s1)
    outfile.writelines('%-20s %-20s %-20s %-20s %-20s\n' %('scpllid', 'vote','enable_stamp','lock_stamp','disable_stamp'))
    for i in range(0, 10):
        (pll_vote, ) = struct.unpack('i', infile.read(4))
        (enable_stamp, ) = struct.unpack('i', infile.read(4))
        (lock_stamp, ) = struct.unpack('i', infile.read(4))
        (disable_stamp, ) = struct.unpack('i', infile.read(4))
        outfile.writelines('%-20d %-20x %-20x %-20x %-20x \n' % (i, pll_vote, enable_stamp&0xFFFFFFFF, lock_stamp&0xFFFFFFFF, disable_stamp&0xFFFFFFFF))  
    s1 = "******************* [%s] ********************\n" % ('debug_info')
    outfile.writelines(s1)
    for i in range(0, 5):
        (debug_info, ) = struct.unpack('I', infile.read(4))
        outfile.writelines('%-20d %-20x \n' % (i, debug_info))

    s1 = "******************* [%s] ********************\n" % ('is_timeout')
    outfile.writelines(s1)
    (is_timeout, ) = struct.unpack('I', infile.read(4))
    outfile.writelines('is_timeout:%-20x \n' % (is_timeout))

    s1 = "******************* [%s] ********************\n" % ('scpll_state')
    outfile.writelines(s1)
    for i in range(0, 10):
        (scpll_state, ) = struct.unpack('I', infile.read(4))
        outfile.writelines('%-20d %-20x \n' % (i, scpll_state))

    s1 = "******************* [%s] ********************\n" % ('scpll_init_state')
    outfile.writelines(s1)
    for i in range(0, 10):
        (scpll_init_state, ) = struct.unpack('I', infile.read(4))
        outfile.writelines('%-20d %-20x \n' % (i, scpll_init_state))

    s1 = "******************* [%s] ********************\n" % ('scpll_en_state')
    outfile.writelines(s1)
    for i in range(0, 10):
        (scpll_en_state, ) = struct.unpack('I', infile.read(4))
        outfile.writelines('%-20d %-20x \n' % (i, scpll_en_state))

    s1 = "******************* [%s] ********************\n" % ('scpll_en_init_state')
    outfile.writelines(s1)
    for i in range(0, 10):
        (scpll_en_init_state, ) = struct.unpack('I', infile.read(4))
        outfile.writelines('%-20d %-20x \n' % (i, scpll_en_init_state))

    s1 = "******************* [%s] ********************\n" % ('rc_flags')
    outfile.writelines(s1)
    (flag, ) = struct.unpack('I', infile.read(4))
    outfile.writelines('rc_cal_flag = 0x%-20x \n' % (flag))
    (flag, ) = struct.unpack('I', infile.read(4))
    outfile.writelines('mrx_offset_cal_flag = 0x%-20x \n' % (flag))
    (flag, ) = struct.unpack('I', infile.read(4))
    outfile.writelines('mrx_cap_cal_flag = 0x%-20x \n' % (flag))

def parse_bbp_timestamp(fifo_type, infile, offset, outfile):
    #BBP_VOTE_PWR_NUM = 6;
    #global BBP_VOTE_CLK_NUM = 6;
    #print 'PrintStamp in 2'
    print("PrintStamp in 2")
    infile.seek(offset)
#    (front, ) = struct.unpack('i', infile.read(4))
#    outfile.writelines('%-30s %#-20x \n' % ('pmom magic', front))

    # 队列头
    s1 = "******************* [%s] ********************\n" % ('stamp_bbp_tf')
    outfile.writelines(s1)
    outfile.writelines('%-30s%-20s\n' %('name', 'timestamp'))
    for i in range(0, 24):
        (stamp_ltetf, ) = struct.unpack('i', infile.read(4))
        outfile.writelines('%-30s %#-20x \n' % (BBP_STAMP_TF[i], stamp_ltetf&0xFFFFFFFF))

    # 队列头
    s1 = "******************* [%s] ********************\n" % ('stamp_bbp_pwr')
    outfile.writelines(s1)
    outfile.writelines('%-30s%-20s\n' %('name', 'timestamp'))
    for i in range(0, BBP_VOTE_PWR_NUM):
        (stamp_ltetf, ) = struct.unpack('i', infile.read(4))
        outfile.writelines('%-15s %-15d %#-20x \n' % ('pwr_on',i, stamp_ltetf&0xFFFFFFFF))     
    for i in range(0, BBP_VOTE_PWR_NUM):
        (stamp_ltetf, ) = struct.unpack('i', infile.read(4))
        outfile.writelines('%-15s %-15d %#-20x \n' % ('pwr_off',i, stamp_ltetf&0xFFFFFFFF))    
    # 队列头
    s1 = "******************* [%s] ********************\n" % ('stamp_bbp_clk')
    outfile.writelines(s1)
    outfile.writelines('%-30s%-20s\n' %('name', 'timestamp'))
    for i in range(0, BBP_VOTE_CLK_NUM):
        (stamp_ltetf, ) = struct.unpack('i', infile.read(4))
        outfile.writelines('%-15s %-15d %#-20x \n' % ('clk_on',i, stamp_ltetf&0xFFFFFFFF))
    for i in range(0, BBP_VOTE_CLK_NUM):
        (stamp_ltetf, ) = struct.unpack('i', infile.read(4))
        outfile.writelines('%-15s %-15d %#-20x \n' % ('clk_off',i, stamp_ltetf&0xFFFFFFFF))
    
    # 队列头
    s1 = "******************* [%s] ********************\n" % ('stamp_bbp_sr')
    outfile.writelines(s1)
    outfile.writelines('%-30s%-20s\n' %('name', 'timestamp'))
    for i in range(0, 18):
        (stamp_ltetf, ) = struct.unpack('i', infile.read(4))
        outfile.writelines('%-30s %#-20x \n' % (BBP_STAMP_SR[i], stamp_ltetf&0xFFFFFFFF))
        
    # 队列头
    s1 = "******************* [%s] ********************\n" % ('vote_bbp_pwr')
    outfile.writelines(s1)
#    outfile.writelines('%-10s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s\n' %('id', 'status', 'lock', 'lock_high','enable_actual','disable_actual','enable_module','disable_module','enable_modem','disable_modem','enable_mode','disable_mode','enable_vote','disable_vote'))
    outfile.writelines('%-10s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s\n' %('id', 'status', 'lock', 'lock_high','enable_actual','disable_actual','enable_module','disable_module','enable_modem','disable_modem','enable_mode','disable_mode'))
    enable_vote_pwr = []
    enable_vote_pwr = []
    id_array_pwr = []
    for i in range(0, BBP_VOTE_PWR_NUM):
        (id, ) = struct.unpack('i', infile.read(4))
        id_array_pwr.append(id)
        (status, ) = struct.unpack('i', infile.read(4))
        (lock_1, ) = struct.unpack('I', infile.read(4))
        (lock_2, ) = struct.unpack('I', infile.read(4))
        (lock_high_1, ) = struct.unpack('I', infile.read(4))
        (lock_high_2, ) = struct.unpack('I', infile.read(4))
#        (enable_vote, ) = struct.unpack('i', infile.read(4))
#        (disable_vote, ) = struct.unpack('i', infile.read(4))
        enable_vote_temp = struct.unpack('I'*BBP_MODULE_NUM*BBP_MODEM_NUM*BBP_MODE_NUM, infile.read(4*BBP_MODULE_NUM*BBP_MODEM_NUM*BBP_MODE_NUM))
        enable_vote_pwr.append(enable_vote_temp)
        (enable_actual, ) = struct.unpack('I', infile.read(4))
        (disable_actual, ) = struct.unpack('I', infile.read(4))
        (enable_module, ) = struct.unpack('I', infile.read(4))
        (disable_module, ) = struct.unpack('I', infile.read(4))
        (enable_modem, ) = struct.unpack('I', infile.read(4))
        (disable_modem, ) = struct.unpack('I', infile.read(4))
        (enable_mode, ) = struct.unpack('I', infile.read(4))
        (disable_mode, ) = struct.unpack('I', infile.read(4))
#        outfile.writelines('%-10d%#-20x%#-10x%#-10x%#-10x%#-10x%#-20x%#-20x%#-20x%#-20x%#-20x%#-20x%#-20x%#-20x%#-20x%#-20x\n' %(id, status, lock_1, lock_2, lock_high_1,lock_high_2,enable_actual,disable_actual,enable_module,disable_module,enable_modem,disable_modem,enable_mode,disable_mode,enable_vote,disable_vote))
        outfile.writelines('%-10d%#-20x%#-10x%#-10x%#-10x%#-10x%#-20x%#-20x%#-20x%#-20x%#-20x%#-20x%#-20x%#-20x\n' %(id, status, lock_1, lock_2, lock_high_1,lock_high_2,enable_actual,disable_actual,enable_module,disable_module,enable_modem,disable_modem,enable_mode,disable_mode))
    
    outfile.writelines('%-10s%-20s%-20s%-20s%-20s%-20s\n' %('id', 'module_num', 'modem_num', 'mode_num','enable_vote','disable_vote'))
    for i in range(0,BBP_VOTE_PWR_NUM):
        for j in range(0,BBP_MODULE_NUM):
            for k in range(0,BBP_MODEM_NUM):
                for m in range(0,BBP_MODE_NUM):
                    index = j*BBP_MODEM_NUM*BBP_MODE_NUM + k*BBP_MODE_NUM + m
                    outfile.writelines('%-10d%#-20d%#-20d%#-20d%#-20x\n' %(id_array_pwr[i], j, k, m, enable_vote_pwr[i][index]))
    # 队列头
    s1 = "******************* [%s] ********************\n" % ('vote_bbp_clk')
    outfile.writelines(s1)
#    outfile.writelines('%-10s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s\n' %('id', 'status', 'lock', 'lock_high','enable_actual','disable_actual','enable_module','disable_module','enable_modem','disable_modem','enable_mode','disable_mode','enable_vote','disable_vote'))
    outfile.writelines('%-10s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s\n' %('id', 'status', 'lock', 'lock_high','enable_actual','disable_actual','enable_module','disable_module','enable_modem','disable_modem','enable_mode','disable_mode'))
    enable_vote_clk = []
    id_array_clk = []
    for i in range(0, BBP_VOTE_CLK_NUM):
        (id, ) = struct.unpack('i', infile.read(4))
        id_array_clk.append(id)
        (status, ) = struct.unpack('i', infile.read(4))
        (lock_1, ) = struct.unpack('I', infile.read(4))
        (lock_2, ) = struct.unpack('I', infile.read(4))
        (lock_high_1, ) = struct.unpack('I', infile.read(4))
        (lock_high_2, ) = struct.unpack('I', infile.read(4))
#        (enable_vote, ) = struct.unpack('i', infile.read(4))
#       (disable_vote, ) = struct.unpack('i', infile.read(4))
        enable_vote_temp = struct.unpack('I'*BBP_MODULE_NUM*BBP_MODEM_NUM*BBP_MODE_NUM, infile.read(4*BBP_MODULE_NUM*BBP_MODEM_NUM*BBP_MODE_NUM))
        enable_vote_clk.append(enable_vote_temp)
        (enable_actual, ) = struct.unpack('I', infile.read(4))
        (disable_actual, ) = struct.unpack('I', infile.read(4))
        (enable_module, ) = struct.unpack('I', infile.read(4))
        (disable_module, ) = struct.unpack('I', infile.read(4))
        (enable_modem, ) = struct.unpack('I', infile.read(4))
        (disable_modem, ) = struct.unpack('I', infile.read(4))
        (enable_mode, ) = struct.unpack('I', infile.read(4))
        (disable_mode, ) = struct.unpack('I', infile.read(4))
#        outfile.writelines('%-10d%#-20x%#-10x%#-10x%#-10x%#-10x%#-20x%#-20x%#-20x%#-20x%#-20x%#-20x%#-20x%#-20x%#-20x%#-20x\n' %(id, status, lock_1, lock_2, lock_high_1,lock_high_2,enable_actual,disable_actual,enable_module,disable_module,enable_modem,disable_modem,enable_mode,disable_mode,enable_vote,disable_vote))
        outfile.writelines('%-10d%#-20x%#-10x%#-10x%#-10x%#-10x%#-20x%#-20x%#-20x%#-20x%#-20x%#-20x%#-20x%#-20x\n' %(id, status, lock_1, lock_2, lock_high_1,lock_high_2,enable_actual,disable_actual,enable_module,disable_module,enable_modem,disable_modem,enable_mode,disable_mode))
    
    outfile.writelines('%-10s%-20s%-20s%-20s%-20s%-20s\n' %('id', 'module_num', 'modem_num', 'mode_num','enable_vote','disable_vote'))
    for i in range(0,BBP_VOTE_PWR_NUM):
        for j in range(0,BBP_MODULE_NUM):
            for k in range(0,BBP_MODEM_NUM):
                for m in range(0,BBP_MODE_NUM):
                    index = j*BBP_MODEM_NUM*BBP_MODE_NUM + k*BBP_MODE_NUM + m
                    outfile.writelines('%-10d%#-20d%#-20d%#-20d%#-20x\n' %(id_array_clk[i], j, k, m, enable_vote_clk[i][index]))
    
    # 队列头
    s1 = "******************* [%s] ********************\n" % ('bbp_dma')
    outfile.writelines(s1)
    outfile.writelines('%-30s%-20s\n' %('name', 'value'))
    for i in range(0, 4):
        (value, ) = struct.unpack('i', infile.read(4))
        outfile.writelines('%-30s %#-20x \n' %(BBP_DMA[i], value&0xFFFFFFFF))
    return


def PrintPmOmInfo(infile, field, offset, length, version, mode, outfile):
        addr = 0
        row = 0
        i = 0
        MyOffset = eval(offset)
        infile.seek(MyOffset)
        print("got entry 0x2000074 PrintSysctrlInfo, length is 0x%x" %(int(length,16)))
        outfile.writelines("offset      data\n")
        for i in range(0, int(int(length,16)/16)):
            (charbyte1, charbyte2, charbyte3,charbyte4, ) = struct.unpack("IIII", infile.read(16))
            addr = 0x10 * row
            row = row + 1
            #print >> outhandler, "0x%08x: %08x %08x %08x %08x" %(addr, charbyte1, charbyte2, charbyte3, charbyte4)
            outfile.writelines("0x%08x: %08x %08x %08x %08x\n" %(addr, charbyte1, charbyte2, charbyte3, charbyte4))
        return

########################################################################################
def entry_0x2000075(infile, field, offset, len, version, mode, outfile):
        #print 'PrintStamp in 1'
        print("PrintStamp in 1")
        ########check parameter start#############
        if not field == '0x2000075':
            #print 'hidis field is ', field
            print("hidis field is 0x%x" %(field))
            #print 'current field is', '0x2000075'
            print("current field is 0x2000075")
            return error['ERR_CHECK_FIELD']
        elif not version == '0x0000':
            #print 'hidis version is ', version
            print("hidis version is 0x%x" %(version))
            #print 'current version is ', '0x00'
            print("current version is 0x00")
    #        return error['ERR_CHECK_VERSION']
        elif not len == '0x10000':
            #print 'hids len is ', len
            print("hids len is 0x%x" %(len))
            #print 'current len is ', '0x400'
            print("current len is 0x10000")
    #        return error['ERR_CHECK_LEN']
        #########check parameter end##############
        #infile.seek(0xf9e20,0)
        #(dump_phy_addr,) = struct.unpack('I', infile.read(4))
        PrintPmOmInfo(infile, field, offset, len, version, mode, outfile)
        
        return 0

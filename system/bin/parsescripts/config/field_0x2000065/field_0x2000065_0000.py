#!/usr/bin/env python3
# coding=utf-8
# Copyright (C) Huawei Technologies Co., Ltd. 2010-2018. All rights reserved.

import os
import re
import struct
import sys

 

sci_section_array = [0x30, 0x1e0]
sci_record_event={
1 : "SCI_EVENT_SCI_INIT_SUCCESS",     
2 : "SCI_EVENT_API_RESET_START",      
3 : "SCI_EVENT_API_RESET_FAILED",     
4 : "SCI_EVENT_API_RESET_FINISH",     
5 : "SCI_EVENT_API_DATA_SEND",        
6 : "SCI_EVENT_API_DATA_REC_START",   
7 : "SCI_EVENT_API_DATA_REC_DONE",    
8 : "SCI_EVENT_API_DECATIVE",         
9 : "SCI_EVENT_API_CLASS_SWITCH",     
10 : "SCI_EVENT_API_CLOCK_STOP",       
11 : "SCI_EVENT_API_GET_STATUS",       
12 : "SCI_EVENT_API_GET_ATR",          
13 : "SCI_EVENT_API_REV_BLK",          
14 : "SCI_EVENT_API_PROTOCOL_SWITCH",  
15 : "SCI_EVENT_API_SET_BWT",          
16 : "SCI_EVENT_API_SLOT_SWITCH",      
17 : "SCI_EVENT_CARD_ACTIVE_START",    
18 : "SCI_EVENT_CARD_ACTIVE_SUCCESS",  
19 : "SCI_EVENT_ATR_REC_START",        
20 : "SCI_EVENT_ATR_REC_GLOBAL",       
21 : "SCI_EVENT_ATR_REC_OVER",         
22 : "SCI_EVENT_ATR_DECODE_ERR",       
23 : "SCI_EVENT_ATR_WWT_RESET",        
24 : "SCI_EVENT_DATA_TRANS",           
25 : "SCI_EVENT_PPS_REQ",              
26 : "SCI_EVENT_PPS_PPS0",             
27 : "SCI_EVENT_PPS_PPS1",             
28 : "SCI_EVENT_PPS_DONE",             
29 : "SCI_EVENT_CLK_START",            
30 : "SCI_EVENT_CLK_STOP",             
31 : "SCI_EVENT_CLK_ERROR",            
32 : "SCI_EVENT_REGISTER_COLD_RESET",  
33 : "SCI_EVENT_REGISTER_WARM_RESET",  
34 : "SCI_EVENT_REGISTER_FINISH",      
35 : "SCI_EVENT_REGISTER_CLOCK_STOP",  
36 : "SCI_EVENT_REGISTER_CLOCK_START", 
37 : "SCI_EVENT_REGULATOR_ERR",        
38 : "SCI_EVENT_REGULATOR_UP",         
39: "SCI_EVENT_REGULATOR_DOWN",       
40 : "SCI_EVENT_VOLTAGE_SWITCH",       
41 : "SCI_EVENT_VOLTAGE_CLASS_C2B",    
42 : "SCI_EVENT_VOLTAGE_CLASS_C2C",    
43 : "SCI_EVENT_VOLTAGE_CLASS_B2B",    
44 : "SCI_EVENT_VOLTAGE_ERROR",        
45 : "SCI_EVENT_INTR_CARD_UP",         
46 : "SCI_EVENT_INTR_CARD_DOWN",       
47 : "SCI_EVENT_INTR_TX_ERR",          
48 : "SCI_EVENT_INTR_ATRSTOUT",        
49 : "SCI_EVENT_INTR_ATRDTOUT",        
50 : "SCI_EVENT_INTR_BLKOUT",          
51 : "SCI_EVENT_INTR_CHOUT",           
52 : "SCI_EVENT_INTR_RTOUT",           
53 : "SCI_EVENT_INTR_RORI",            
54 : "SCI_EVENT_INTR_CLK_STOP",        
55 : "SCI_EVENT_INTR_CLK_ACTIVE",      
56 : "SCI_EVENT_DETECT_CARD_IN",       
57 : "SCI_EVENT_DETECT_CARD_OUT",      
58 : "SCI_EVENT_DETECT_CARD_LEAVE",    
59 : "SCI_EVENT_DETECT_IND_USIM_IN",   
60 : "SCI_EVENT_DETECT_IND_USIM_OUT",  
61 : "SCI_EVENT_DETECT_NO_NEED_IND",   
62 : "SCI_EVENT_IND_PLUS_IN",          
63 : "SCI_EVENT_IND_PLUS_OUT",         
64 : "SCI_EVENT_DETECT_IND_M3",        
65 : "SCI_EVENT_ERROR_SET_PARAM",      
66 : "SCI_EVENT_ERROR_NODATA",         
67 : "SCI_EVENT_ERROR_NOCARD",         
68 : "SCI_EVENT_ERROR_DATA_REC_BUF_OVR",
69 : "SCI_EVENT_ERROR_PROTOCOL_SWITCH",
70 : "SCI_EVENT_ERROR_REV_BLK_PLOUGE", 
71 : "SCI_EVENT_ERROR_REV_BLK_DATA",   
72 : "SCI_EVENT_ERROR_TRANS_STATE", 
73 : "SCI_EVENT_LOW_POWER_ENTER",      
74 : "SCI_EVENT_LOW_POWER_EXIT",       
75 : "SCI_EVENT_DMA_START",            
76 : "SCI_EVENT_DMA_ERROR",            
77 : "SCI_EVENT_TX_BUFF_FULL",         
78 : "SCI_EVENT_RX_BUFF_NULL",         
79 : "SCI_EVENT_START",            
80 : "SCI_EVENT_END",   
81 : "SCI_EVENT_PPS_RCV_ERROR",
82 : "SCI_EVENT_PPS_ERROR",
83 : "SCI_EVENT_ATR_REC_TA1",          
84 : "SCI_EVENT_ATR_ADJ_TA1",          
85 : "SCI_EVENT_PPS_REQ_ERROR",        
86 : "SCI_EVENT_PPS_RECV_PPS1",             
87 : "SCI_EVENT_PPS_RECV_PPS0",             
88 : "SCI_EVENT_PPS_LOCAL_RESPOSE",             
89 : "SCI_EVENT_ATR_TA2_DATA",             
90 : "SCI_EVENT_SPECIFIC_MODE",               
91 : "SCI_EVENT_WRITE_SCI0_SCTRL",               
92 : "SCI_EVENT_WRITE_SCI1_SCTRL",             
93 : "SCI_EVENT_WRITE_SD_SCTRL",             
94 : "SCI_EVENT_ENABLE_SD_VCC",             
95 : "SCI_EVENT_DISABLE_SD_VCC", 
96 : "SCI_EVENT_ATR_DATA_ORI",         
97 : "SCI_EVENT_QUERY_CARD_TYPE",               
98 : "SCI_EVENT_RECV_CARD_TYPE",             
99 : "SCI_EVENT_CARD_TYPE_RESULT",
100 : "SCI_EVENT_QUERY_CARD_FAIL",    
101 : "SCI_EVENT_ENABLE_SD_ERROR",                  
102 : "SCI_EVENT_DISABLE_SD_ERROR",                    
103 : "SCI_EVENT_VOLTAGE_CLASS_02C",
104 : "SCI_EVENT_IND_SCI_CFG",
105 : "SCI_EVENT_WAIT_CARD_STATUS",
106 : "SCI_EVENT_RECV_CARD_DONE",
107 : "SCI_EVENT_SEND_CARD_DONE",
108 : "SCI_EVENT_SIM_PMU_ON",
109 : "SCI_EVENT_SIM_PMU_OFF",
110 : "SCI_EVENT_SIM_PMU_CTRL_SUCC", 
111 : "SCI_EVENT_SIM_PMU_CTRL_FAIL", 
112 : "SCI_EVENT_SIM_SET_PMU_STATUS",
113 : "SCI_EVENT_ESIM_SUPPORT",
114 : "SCI_EVENT_ESIM_IO",
115 : "SCI_EVENT_SIM_IO",
116 : "SCI_EVENT_ONLY_SIM_IO",
117 : "SCI_EVENT_SET_SIM_IO",
118 : "SCI_EVENT_SET_SIM_FAIL",
119 : "SCI_EVENT_SET_SIM_IO_RECV",
120 : "SCI_EVENT_SET_SIM_IO_RESULT",
121 : "SCI_EVENT_ESIM_NV_READ_FAIL",
122 : "SCI_EVENT_ESIM_NV_WRITE_FAIL",
123 : "SCI_EVENT_ESIM_PARAM_ERROR",
124 : "SCI_EVENT_ESIM_GET_SIM_PMU",
125 : "SCI_EVENT_ESIM_GET_ESIM_PMU",
126 : "SCI_EVENT_ESIM_GET_PMU_FAIL",
127 : "SCI_EVENT_API_SET_CARD_TYPE",
128 : "SCI_EVENT_API_SET_CARD_SUCCESS",
129 : "SCI_EVENT_API_GET_CARD_TYPE",
130 : "SCI_EVENT_GET_CARD_TYPE_RESULT",
131 : "SCI_EVENT_NO_NEED_SET_CARD_TYPE",
132 : "SCI_EVENT_HOTPLUG_NO_PROCESS",
133 : "SCI_EVENT_GET_DET_STATE",
134 : "SCI_EVENT_SWITCH_CARD_TYPE_START",
135 : "SCI_EVENT_SWITCH_CARD_TYPE_DONE",
136 : "SCI_EVENT_SWITCH_CARD_TYPE_SUCC",
137 : "SCI_EVENT_SWITCH_CARD_TYPE_FAIL",
138 : "SCI_EVENT_LEGACY_MSG_START",
139 : "SCI_EVENT_LEGACY_MSG_DONE",
140 : "SCI_EVENT_LEGACY_MSG_SUCC",
141 : "SCI_EVENT_LEGACY_MSG_FAIL",
142 : "SCI_EVENT_BEYOND_LOG",
143 : "SCI_EVENT_MAX"

}

sci_regs = (
    "SCI_REG->RegData           :  ",
    "SCI_REG->RegCtrl0          :  ",
    "SCI_REG->RegCtrl1          :  ",
    "SCI_REG->RegCtrl2          :  ",
    "SCI_REG->RegClkICC         :  ",
    "SCI_REG->RegBaudValue      :  ",
    "SCI_REG->RegBaud           :  ",
    "SCI_REG->RegTide           :  ",
    "SCI_REG->RegDMACtrl        :  ",
    "SCI_REG->RegStable         :  ",
    "SCI_REG->RegATime          :  ",
    "SCI_REG->RegDTime          :  ",
    "SCI_REG->RegATRSTime       :  ",
    "SCI_REG->RegATRDTime       :  ",
    "SCI_REG->RegStopTime       :  ",
    "SCI_REG->RegStartTime      :  ",
    "SCI_REG->RegRetry          :  ",
    "SCI_REG->RegChTimeLS       :  ",
    "SCI_REG->RegChTimeMS       :  ",
    "SCI_REG->RegBlkTimeLS      :  ",
    "SCI_REG->RegBlkTimeMS      :  ",
    "SCI_REG->RegChGuard        :  ",
    "SCI_REG->RegBlkGuard       :  ",
    "SCI_REG->RegRxTime         :  ",
    "SCI_REG->RegFlag           :  ",
    "SCI_REG->RegTxCount        :  ",
    "SCI_REG->RegRxCount        :  ",
    "SCI_REG->RegIntMask        :  ",
    "SCI_REG->RegIntRaw         :  ",
    "SCI_REG->RegIntStatus      :  ",
    "SCI_REG->RegIntClear       :  ",
    "SCI_REG->RegSyncAct        :  ",
    "SCI_REG->RegSyncData       :  ",
    "SCI_REG->RegSyncRaw        :  ",
)

sci_state = {
1:    "SCI_STATE_UNINIT",             
2:    "SCI_STATE_FIRSTINIT",              
3:    "SCI_STATE_DISABLED",               
4:    "SCI_STATE_NOCARD",                 
5:    "SCI_STATE_INACTIVECARD",           
6:    "SCI_STATE_WAITATR",                
7:    "SCI_STATE_READATR",                
8:    "SCI_STATE_READY",                  
9:    "SCI_STATE_RX",                     
10:   "SCI_STATE_TX",
}

sci_protol = {
1:    "T0_protocol",             
2:    "T1_protocol"
}

sci_con = {
1:    "3B",             
4:    "3F"
}
########################################## ATR ###################################################
def analyse_atr(sci_fp, dst_fp, field_offset):
    sci_fp.seek(0 + field_offset)
    atr = sci_fp.read(0x30)
    atr_len, atr_data = struct.unpack("=c47s", atr)
    #atr_len = ord(atr_len)
    #atr_data = list(map(ord, atr_data))
    print(type(atr_len))
    print(type(atr_data))
    print("SCI ATR RECORD:", file=dst_fp)
    print("ATR LEN: ", atr_len[0], file=dst_fp)
    print("ATR DATA: ", end=' ', file=dst_fp)
    #print atr_len
    for i in range(0, atr_len[0]):
        print("0x%x" %(int(atr_data[i])), end=' ', file=dst_fp)
    print("", file=dst_fp)
    print("", file=dst_fp)

def analyse_reg(sci_fp, dst_fp, field_offset):
    sci_fp.seek(sci_section_array[0] + field_offset)
    print("**********************SCI GLOBAL RECORD START**********************", file=dst_fp)
    print("", file=dst_fp)
    print("", file=dst_fp)
    for i in range(0, 3):
        sci_reg = sci_fp.read(24)
        event,sciclass,time,state,protocol,eConvention = struct.unpack("=6I", sci_reg)
        if(time==0):
            continue
        print('%s%s' %('SCI_EXC_EVENT:', sci_record_event[event+1]), file=dst_fp)
        print("SCI_CLASS_KIND: 0x%08x"%(sciclass& 0xffffffffff), file=dst_fp)
        print("SCI_EXC_TIME: 0x%08x"%(time& 0xffffffffff), file=dst_fp)
        print('%s%s' %('SCI_EXC_STATE:', sci_state[state+1]), file=dst_fp)
        print('%s%s' %('SCI_PROTOCOL:', sci_protol[protocol+1]), file=dst_fp)
        print("SCI_BASE_ADDR: 0x%08x"%(eConvention & 0xffffffffff), file=dst_fp)
        print("SCI_CURRENT_REG:", file=dst_fp)
        for j in range(0,34):
            reg = sci_fp.read(0x4)
            reg_val = struct.unpack("=i", reg)
            print("   %s 0x%08x" %(sci_regs[j],reg_val[0]), file=dst_fp)
        print("", file=dst_fp)
        print("", file=dst_fp)

    print("**********************SCI GLOBAL RECORD END**********************", file=dst_fp)
    print("", file=dst_fp)
    print("", file=dst_fp)

global  backrush      
def analyse_event(sci_fp, dst_fp, field_offset):
    backrush = 0
    print("**********************SCI EVENT RECORD START**********************", file=dst_fp)
    print("", file=dst_fp)
    print("", file=dst_fp)
    event_offset = sci_section_array[0]+sci_section_array[1]
    sci_fp.seek(event_offset + field_offset)
    Q = sci_fp.read(16)
    maxNun,front,rear,num = struct.unpack("=4I", Q)
    #print "0x%08x 0x%08x 0x%08x 0x%08x" %(maxNun,front,rear,num) 
    if(int(num) == 0):
        return
    if(int(num) < int(maxNun)): 
        for i in range(0, int(int(num)/4) ):
            record = sci_fp.read(16)
            event,param1,param2,time = struct.unpack("=4I", record)
            print("0x%04x   %-35s\tpara1:0x%08x  \tpara2:0x%08x  time:0x%x" %(i,sci_record_event[event+1], int(param1), int(param2), int(time)), file=dst_fp)
            print("", file=dst_fp)
    else:
        #print"aaaaaaaa"
        offset = event_offset+front*4+16
        sci_fp.seek(offset + field_offset)
        for i in range(front,maxNun):
            #print "0x%04x "%(front)
            #print >> dst_fp,"i=0x%04x front=0x%04x offset=0x%04x "%(i,front,offset) 
            if (i%4 == 0):
                event =  sci_fp.read(4)
                intevent =struct.unpack("I",event)
            elif (i%4 == 1): 
                param1 =  sci_fp.read(4)
                intparam1 =struct.unpack("I",param1)
            elif(i%4 == 2):        
                param2 =  sci_fp.read(4)
                intparam2=struct.unpack("I",param2) 
            elif(i%4 == 3): 
                time =  sci_fp.read(4)
                inttime =struct.unpack("I",time) 
                #print >> dst_fp,"i=0x%04x front=0x%04x offset=0x%04x  event =0x%08x par1= 0x%08x par2=0x%08x time=0x%08x" %(i,front,offset,intevent[0],intparam1[0],intparam2[0],inttime[0])
                print("0x%04x  %-35s\tpara1:0x%08x  \tpara2:0x%08x  time:0x%x" %(int((i+1)/4),sci_record_event[intevent[0]+1],intparam1[0] % 0xffffffff,intparam2[0] % 0xffffffff,inttime[0] % 0xffffffff), file=dst_fp)
                print("", file=dst_fp)  
                
        offset = event_offset+16
        sci_fp.seek(offset + field_offset)
        for i in range(0,front):
            #print "0x%04x "%(front)
            #print >> dst_fp,"i=0x%04x front=0x%04x offset=0x%04x "%(i,front,offset) 
            if (i%4 == 0):
                event =  sci_fp.read(4)
                intevent =struct.unpack("I",event)
            elif (i%4 == 1): 
                param1 =  sci_fp.read(4)
                intparam1 =struct.unpack("I",param1)
            elif(i%4 == 2):        
                param2 =  sci_fp.read(4)
                intparam2=struct.unpack("I",param2)
            elif(i%4 == 3): 
                time =  sci_fp.read(4)
                inttime =struct.unpack("I",time) 
                #print >> dst_fp,"i=0x%04x front=0x%04x offset=0x%04x  event =0x%08x par1= 0x%08x par2=0x%08x time=0x%08x" %(i,front,offset,intevent[0],intparam1[0],intparam2[0],inttime[0])
                print("0x%04x  %-35s\tpara1:0x%08x  \tpara2:0x%08x  time:0x%x" %(int((i+1)/4),sci_record_event[intevent[0]+1],intparam1[0] % 0xffffffff,intparam2[0] % 0xffffffff,inttime[0] % 0xffffffff), file=dst_fp)
                print("", file=dst_fp)   

            
    print("", file=dst_fp)
    print("", file=dst_fp)   
    print("**********************SCI EVENT RECORD END**********************", file=dst_fp)   
    
def entry_0x2000065(infile, field, offset, slen, version, mode, outfile):
        try:
            if not field == '0x2000065':
                print('hidis field is ', field)
                print('current field is', '0x2000065')
                return error['ERR_CHECK_FIELD']
            elif not version == '0x0000':
                print('hidis version is ', version)
                print('current version is ', '0x0000')
                return error['ERR_CHECK_VERSION']
            elif not slen == '0x1000':
                print('hids len is ', slen)
                print('current len is ', '0x1000')
                return error['ERR_CHECK_LEN']
            print("got entry 0x2000065")
            #sci_fp.seek(offset)
            field_offset = eval(offset)
            analyse_atr(infile, outfile, field_offset)
            analyse_reg(infile, outfile, field_offset)
            analyse_event(infile, outfile, field_offset)
            return 0

        except Exception as e:
            print((str(e)))
            outfile.writelines(str(e))
            return 1


    
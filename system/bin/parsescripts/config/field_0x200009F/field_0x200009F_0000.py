#!/usr/bin/env python3
#coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename      field_0x200009F_0000.py
# * Description   analysis maa dump
#***********************************************************************
'''
Created on 2020-1-9
 
@
'''
import os
import re
import struct
import sys

maa_field_def = [
"MAA_GLB_CTRL_REG",              	0x0   ,       
"MAA_AXI_BUS_CFG_REG",           	0x4   ,         
"MAA_VERSION_REG",               	0x8   ,         
"MAA_LP_EN_REG",                 	0xC   ,          
"MAA_LP_STAT_REG",               	0x10  ,       
"MAA_AUTOCLK_RESP_BYPASS_REG",   	0x14  ,           
"MAA_OPIPE_STAT_REG",            	0x18  ,   
"MAA_IPIPE_STAT0_REG",           	0x1C  ,    
"MAA_IPIPE_STAT1_REG",           	0x20  ,     
"MAA_OPIPE_INT_MSK_REG",         	0x24  ,
"MAA_OPIPE_INT_STAT_REG",        	0x28  ,
"MAA_OPIPE_INT_RAW_REG",         	0x2C  ,
"MAA_IPIPE_INT_RAW0_REG",        	0x30  ,
"MAA_IPIPE_INT_MSK0_REG",        	0x34  ,
"MAA_IPIPE_INT_STAT0_REG",       	0x38  ,
"MAA_IPIPE_INT_RAW1_REG",        	0x3C  ,
"MAA_IPIPE_INT_MSK1_REG",        	0x40  ,
"MAA_IPIPE_INT_STAT1_REG",       	0x44  ,
"MAA_IPIPE_INT_RAW2_REG",        	0x48  ,
"MAA_IPIPE_INT_MSK2_REG",        	0x4C  ,
"MAA_IPIPE_INT_STAT2_REG",       	0x50  ,
"MAA_IPIPE_INT_RAW3_REG",        	0x54 ,
"MAA_IPIPE_INT_MSK3_REG",        	0x58 ,
"MAA_IPIPE_INT_STAT3_REG",       	0x5C ,
"MAA_IPIPE_INT_RAW4_REG",        	0x60 ,
"MAA_IPIPE_INT_MSK4_REG",        	0x64 ,
"MAA_IPIPE_INT_STAT4_REG",       	0x68 ,
"MAA_IPIPE_INT_RAW5_REG",        	0x6C  ,
"MAA_IPIPE_INT_MSK5_REG",        	0x70  ,
"MAA_IPIPE_INT_STAT5_REG",       	0x74  ,
"MAA_OPIPE_CFG_DONE_REG",        	0x78  ,
"MAA_HAC_GIF_128SPLIT_REG",      	0x80  ,
"MAA_HAC_GIF_MAX_LEN_REG",       	0x84  ,
"MAA_HAC_GIF_PRIOR_REG",         	0x88  ,
"MAA_TIMER_EN_REG",              	0x90  ,
"MAA_TIMER_WATCHCNT_REG",        	0x94  ,    
"MAA_RLS_POOL_ADDR_L_REG",       	0x500 ,    
"MAA_RLS_POOL_ADDR_H_REG",       	0x504 , 
"MAA_RLS_POOL_DEPTH_REG",        	0x508 ,
"MAA_RLS_POOL_WPTR_REG",         	0x50C ,
"MAA_RLS_POOL_RPTR_REG",         	0x510 ,
"MAA_RLS_POOL_UP_THRH_REG",      	0x514 ,   
"MAA_ACORE_ALLOC_CNT_0_REG",     	0x900 ,  
"MAA_ACORE_ALLOC_CNT_1_REG",     	0x980 ,  
"MAA_ACORE_ALLOC_CNT_2_REG",     	0xA00 ,  
"MAA_ACORE_ALLOC_CNT_3_REG",     	0xA80 ,   
"MAA_ACORE_ALLOC_CNT_4_REG",     	0xB00 ,   
"MAA_ACORE_ALLOC_CNT_5_REG",     	0xB80 ,   
"MAA_ALLOC_FIFO_CNT_0_REG",      	0x904 ,    
"MAA_ALLOC_FIFO_CNT_1_REG",      	0x984 ,    
"MAA_ALLOC_FIFO_CNT_2_REG",      	0xA04 , 
"MAA_ALLOC_FIFO_CNT_3_REG",      	0xA84 ,
"MAA_ALLOC_FIFO_CNT_4_REG",      	0xB04 ,
"MAA_ALLOC_FIFO_CNT_5_REG",      	0xB84 ,
"MAA_ALLOC_CNT_0_REG",      		 0x90C,   
"MAA_ALLOC_CNT_1_REG",      		 0x98C,  
"MAA_ALLOC_CNT_2_REG",      		 0xA0C,  
"MAA_ALLOC_CNT_3_REG",      		 0xA8C,  
"MAA_ALLOC_CNT_4_REG",      		 0xB0C,   
"MAA_ALLOC_CNT_5_REG",      		 0xB8C,   
"MAA_ALLOC_DESTN_CNT_0_REG",     	0x910 ,   
"MAA_ALLOC_DESTN_CNT_1_REG",     	0x990 ,    
"MAA_ALLOC_DESTN_CNT_2_REG",     	0xA10 ,    
"MAA_ALLOC_DESTN_CNT_3_REG",     	0xA90 , 
"MAA_ALLOC_DESTN_CNT_4_REG",     	0xB10 ,
"MAA_ALLOC_DESTN_CNT_5_REG",     	0xB90 ,
"MAA_ALLOC_DESTN_CNT_6_REG",     	0x914 ,
"MAA_ALLOC_DESTN_CNT_7_REG",     	0x994 ,   
"MAA_ALLOC_DESTN_CNT_8_REG",     	0xA14 ,  
"MAA_ALLOC_DESTN_CNT_9_REG",     	0xA94 ,  
"MAA_ALLOC_DESTN_CNT_10_REG",    	0xB14 ,  
"MAA_ALLOC_DESTN_CNT_11_REG",    	0xB94 ,   
"MAA_ALLOC_DESTN_CNT_12_REG",    	0x918 ,   
"MAA_ALLOC_DESTN_CNT_13_REG",    	0x998 ,   
"MAA_ALLOC_DESTN_CNT_14_REG",    	0xA18 ,    
"MAA_ALLOC_DESTN_CNT_15_REG",    	0xA98 ,    
"MAA_ALLOC_DESTN_CNT_16_REG",    	0xB18 , 
"MAA_ALLOC_DESTN_CNT_17_REG",    	0xB98 ,
"MAA_ALLOC_DESTN_CNT_18_REG",    	0x91C ,
"MAA_ALLOC_DESTN_CNT_19_REG",    	0x99C ,
"MAA_ALLOC_DESTN_CNT_20_REG",    	0xA1C ,   
"MAA_ALLOC_DESTN_CNT_21_REG",    	0xA9C ,  
"MAA_ALLOC_DESTN_CNT_22_REG",    	0xB1C ,  
"MAA_ALLOC_DESTN_CNT_23_REG",    	0xB9C ,  
"MAA_ALLOC_DESTN_CNT_24_REG",    	0x920 ,   
"MAA_ALLOC_DESTN_CNT_25_REG",    	0x9A0 ,   
"MAA_ALLOC_DESTN_CNT_26_REG",    	0xA20 ,   
"MAA_ALLOC_DESTN_CNT_27_REG",    	0xAA0 ,    
"MAA_ALLOC_DESTN_CNT_28_REG",    	0xB20 ,    
"MAA_ALLOC_DESTN_CNT_29_REG",    	0xBA0 , 
"MAA_ALLOC_DESTN_CNT_30_REG",    	0x924 , 
"MAA_ALLOC_DESTN_CNT_31_REG",    	0x9A4 , 
"MAA_ALLOC_DESTN_CNT_32_REG",    	0xA24 ,
"MAA_ALLOC_DESTN_CNT_33_REG",    	0xAA4 ,
"MAA_ALLOC_DESTN_CNT_34_REG",    	0xB24 ,
"MAA_ALLOC_DESTN_CNT_35_REG",    	0xBA4 ,
"MAA_DESTN_ALLOC_CNT_0_REG",     	0x930 ,
"MAA_DESTN_ALLOC_CNT_1_REG",     	0x9B0 ,
"MAA_DESTN_ALLOC_CNT_2_REG",     	0xA30 ,
"MAA_DESTN_ALLOC_CNT_3_REG",     	0xAB0 ,
"MAA_DESTN_ALLOC_CNT_4_REG",     	0xB30 ,
"MAA_DESTN_ALLOC_CNT_5_REG",     	0xBB0 ,
"MAA_DESTN_ALLOC_CNT_6_REG",     	0x934 ,
"MAA_DESTN_ALLOC_CNT_7_REG",     	0x9B4 ,
"MAA_DESTN_ALLOC_CNT_8_REG",     	0xA34 ,
"MAA_DESTN_ALLOC_CNT_9_REG",     	0xAB4 ,
"MAA_DESTN_ALLOC_CNT_10_REG",    	0xB34 ,
"MAA_DESTN_ALLOC_CNT_11_REG",    	0xBB4 ,
"MAA_DESTN_ALLOC_CNT_12_REG",    	0x938 ,
"MAA_DESTN_ALLOC_CNT_13_REG",    	0x9B8 ,
"MAA_DESTN_ALLOC_CNT_14_REG",    	0xA38 ,
"MAA_DESTN_ALLOC_CNT_15_REG",    	0xAB8 ,
"MAA_DESTN_ALLOC_CNT_16_REG",    	0xB38 ,
"MAA_DESTN_ALLOC_CNT_17_REG",    	0xBB8 ,
"MAA_DESTN_ALLOC_CNT_18_REG",    	0x93C ,
"MAA_DESTN_ALLOC_CNT_19_REG",    	0x9BC ,
"MAA_DESTN_ALLOC_CNT_20_REG",    	0xA3C ,
"MAA_DESTN_ALLOC_CNT_21_REG",    	0xABC ,
"MAA_DESTN_ALLOC_CNT_22_REG",    	0xB3C ,
"MAA_DESTN_ALLOC_CNT_23_REG",    	0xBBC ,
"MAA_DESTN_ALLOC_CNT_24_REG",    	0x940 ,
"MAA_DESTN_ALLOC_CNT_25_REG",    	0x9C0 ,
"MAA_DESTN_ALLOC_CNT_26_REG",    	0xA40 ,
"MAA_DESTN_ALLOC_CNT_27_REG",    	0xAC0 , 
"MAA_DESTN_ALLOC_CNT_28_REG",    	0xB40 , 
"MAA_DESTN_ALLOC_CNT_29_REG",    	0xBC0 ,  
"MAA_DESTN_ALLOC_CNT_30_REG",    	0x944 ,  
"MAA_DESTN_ALLOC_CNT_31_REG",    	0x9C4 ,  
"MAA_DESTN_ALLOC_CNT_32_REG",    	0xA44 ,  
"MAA_DESTN_ALLOC_CNT_33_REG",    	0xAC4 ,  
"MAA_DESTN_ALLOC_CNT_34_REG",    	0xB44 ,
"MAA_DESTN_ALLOC_CNT_35_REG",    	0xBC4 , 
"MAA_RLS_CNT_0_REG",             	0x960 , 
"MAA_RLS_CNT_1_REG",             	0x9E0 ,  
"MAA_RLS_CNT_2_REG",             	0xA60 ,  
"MAA_RLS_CNT_3_REG",             	0xAE0 ,  
"MAA_RLS_CNT_4_REG",             	0xB60 ,  
"MAA_RLS_CNT_5_REG",             	0xBE0 ,  
"MAA_RLS_ABANDON_CNT_REG",       	0xC00 ,
"MAA_CNT_CLK_EN_REG",            	0xD00 , 
"MAA_CNT_CLR_REG",               	0xD04 , 
"MAA_HAC_BP_DBG_REG",            	0x1000,  
"MAA_HAC_DATA_DBG_REG",          	0x1004,  
"MAA_HAC_PUSH_DBG_REG",          	0x1008,  
"MAA_HAC_DBG_REG",               	0x100C,  
"MAA_GS_DBG_REG",                	0x1010,  
"MAA_HAC_BP_INVALID_DATA_L_REG", 	0x1018,
"MAA_HAC_BP_INVALID_DATA_H_REG", 	0x101C, 
"MAA_OPIPE_SECCTRL_REG",           	0x3000,
"MAA_IPIPE_SECCTRL0_REG",          	0x3008,
"MAA_IPIPE_SECCTRL1_REG",          	0x300C,
"MAA_IPIPE_SECCTRL2_REG",          	0x3010,
"MAA_OPIPE_MID_REG",               	0x3014,
"MAA_IPIPE_MID0_REG",              	0x3018,
"MAA_IPIPE_MID1_REG",              	0x301C,
"MAA_ALLOC_ADDR_STR_L_0_REG",      	0x3020,
"MAA_ALLOC_ADDR_STR_H_0_REG",      	0x3024,
"MAA_ALLOC_ADDR_END_L_0_REG",      	0x3028,
"MAA_ALLOC_ADDR_END_H_0_REG",      	0x302C,
"MAA_ALLOC_ADDR_STR_L_1_REG",      	0x3030,
"MAA_ALLOC_ADDR_STR_H_1_REG",      	0x3034,
"MAA_ALLOC_ADDR_END_L_1_REG",      	0x3038,
"MAA_ALLOC_ADDR_END_H_1_REG",      	0x303C,
"MAA_ALLOC_ADDR_STR_L_2_REG",      	0x3040,
"MAA_ALLOC_ADDR_STR_H_2_REG",      	0x3044,
"MAA_ALLOC_ADDR_END_L_2_REG",      	0x3048,
"MAA_ALLOC_ADDR_END_H_2_REG",      	0x304C,
"MAA_ALLOC_ADDR_STR_L_3_REG",      	0x3050,
"MAA_ALLOC_ADDR_STR_H_3_REG",      	0x3054,
"MAA_ALLOC_ADDR_END_L_3_REG",      	0x3058,
"MAA_ALLOC_ADDR_END_H_3_REG",      	0x305C,
"MAA_ALLOC_ADDR_PT_CTRL_REG",      	0x3100,
"MAA_PTR_SIZE0_REG",               	0x3104,
"MAA_PTR_SIZE1_REG",               	0x3108,
"MAA_PTR_SIZE2_REG",               	0x310C,
"MAA_PTR_SIZE3_REG",               	0x3110,
"MAA_PTR_SIZE4_REG",               	0x3114,
"MAA_PTR_SIZE5_REG",               	0x3118,
"MAA_OPIPE_BASE_ADDR_L_0_REG",     	0x4000,
"MAA_OPIPE_BASE_ADDR_H_0_REG",     	0x4004,
"MAA_OPIPE_DEPTH_0_REG",           	0x4008,
"MAA_OPIPE_WPTR_0_REG",            	0x400C,
"MAA_OPIPE_RPTR_0_REG",            	0x4010,
"MAA_OPIPE_UP_THRH_0_REG",         	0x4020,
"MAA_OPIPE_DN_THRH_0_REG",         	0x4024,
"MAA_OPIPE_SPACE_0_REG",           	0x4028,
"MAA_OPIPE_EN_0_REG",              	0x4040,
"MAA_OPIPE_CFG_DONE_0_REG",        	0x4044,
"MAA_OPIPE_DBG1_0_REG",            	0x4050,
"MAA_OPIPE_DBG0_0_REG",            	0x4054,
"MAA_OPIPE_BASE_ADDR_L_1_REG",     	0x4080,
"MAA_OPIPE_BASE_ADDR_H_1_REG",     	0x4084,
"MAA_OPIPE_DEPTH_1_REG",           	0x4088,
"MAA_OPIPE_WPTR_1_REG",            	0x408C,
"MAA_OPIPE_RPTR_1_REG",            	0x4090,
"MAA_OPIPE_UP_THRH_1_REG",         	0x40A0,
"MAA_OPIPE_DN_THRH_1_REG",         	0x40A4,
"MAA_OPIPE_SPACE_1_REG",           	0x40A8,
"MAA_OPIPE_EN_1_REG",              	0x40C0,
"MAA_OPIPE_CFG_DONE_1_REG",        	0x40C4,
"MAA_OPIPE_DBG1_1_REG",            	0x40D0,
"MAA_OPIPE_DBG0_1_REG",            	0x40D4,
"MAA_OPIPE_BASE_ADDR_L_2_REG",     	0x4100,
"MAA_OPIPE_BASE_ADDR_H_2_REG",     	0x4104,
"MAA_OPIPE_DEPTH_2_REG",           	0x4108,
"MAA_OPIPE_WPTR_2_REG",            	0x410C,
"MAA_OPIPE_RPTR_2_REG",            	0x4110,
"MAA_OPIPE_UP_THRH_2_REG",         	0x4120,
"MAA_OPIPE_DN_THRH_2_REG",         	0x4124,
"MAA_OPIPE_SPACE_2_REG",           	0x4128,
"MAA_OPIPE_EN_2_REG",              	0x4140,
"MAA_OPIPE_CFG_DONE_2_REG",        	0x4144,
"MAA_OPIPE_DBG1_2_REG",            	0x4150,
"MAA_OPIPE_DBG0_2_REG",            	0x4154,
"MAA_OPIPE_BASE_ADDR_L_3_REG",     	0x4180,
"MAA_OPIPE_BASE_ADDR_H_3_REG",     	0x4184,
"MAA_OPIPE_DEPTH_3_REG",           	0x4188,
"MAA_OPIPE_WPTR_3_REG",            	0x418C,
"MAA_OPIPE_RPTR_3_REG",            	0x4190,
"MAA_OPIPE_UP_THRH_3_REG",         	0x41A0,
"MAA_OPIPE_DN_THRH_3_REG",         	0x41A4,
"MAA_OPIPE_SPACE_3_REG",           	0x41A8,
"MAA_OPIPE_EN_3_REG",              	0x41C0,
"MAA_OPIPE_CFG_DONE_3_REG",        	0x41C4,
"MAA_OPIPE_DBG1_3_REG",            	0x41D0,
"MAA_OPIPE_DBG0_3_REG",            	0x41D4,
"MAA_OPIPE_BASE_ADDR_L_4_REG",     	0x4200,
"MAA_OPIPE_BASE_ADDR_H_4_REG",     	0x4204,
"MAA_OPIPE_DEPTH_4_REG",           	0x4208,
"MAA_OPIPE_WPTR_4_REG",            	0x420C,
"MAA_OPIPE_RPTR_4_REG",            	0x4210,
"MAA_OPIPE_UP_THRH_4_REG",         	0x4220,
"MAA_OPIPE_DN_THRH_4_REG",         	0x4224,
"MAA_OPIPE_SPACE_4_REG",           	0x4228,
"MAA_OPIPE_EN_4_REG",              	0x4240,
"MAA_OPIPE_CFG_DONE_4_REG",        	0x4244,
"MAA_OPIPE_DBG1_4_REG",            	0x4250,
"MAA_OPIPE_DBG0_4_REG",            	0x4254,
"MAA_OPIPE_BASE_ADDR_L_5_REG",     	0x4280,
"MAA_OPIPE_BASE_ADDR_H_5_REG",     	0x4284,
"MAA_OPIPE_DEPTH_5_REG",           	0x4288,
"MAA_OPIPE_WPTR_5_REG",            	0x428C,
"MAA_OPIPE_RPTR_5_REG",            	0x4290,
"MAA_OPIPE_UP_THRH_5_REG",         	0x42A0,
"MAA_OPIPE_DN_THRH_5_REG",         	0x42A4,
"MAA_OPIPE_SPACE_5_REG",           	0x42A8,
"MAA_OPIPE_EN_5_REG",              	0x42C0,
"MAA_OPIPE_CFG_DONE_5_REG",        	0x42C4,
"MAA_OPIPE_DBG1_5_REG",            	0x42D0,
"MAA_OPIPE_DBG0_5_REG",            	0x42D4,
"MAA_IPIPE_BASE_ADDR_L_0_REG",     	0x6000,
"MAA_IPIPE_BASE_ADDR_H_0_REG",     	0x6004,
"MAA_IPIPE_DEPTH_0_REG",           	0x6008,
"MAA_IPIPE_WPTR_0_REG",            	0x600C,
"MAA_IPIPE_RPTR_0_REG",            	0x6010,
"MAA_IPIPE_THRH_0_REG",            	0x6014,
"MAA_IPIPE_PTR_ADDR_L_0_REG",      	0x6018,
"MAA_IPIPE_PTR_ADDR_H_0_REG",      	0x601C,
"MAA_IPIPE_CTRL_0_REG",            	0x604C,
"MAA_IPIPE_DBG1_0_REG",            	0x6050,
"MAA_IPIPE_DBG0_0_REG",            	0x6054,
"MAA_IPIPE_BASE_ADDR_L_1_REG",     	0x6080,
"MAA_IPIPE_BASE_ADDR_H_1_REG",     	0x6084,
"MAA_IPIPE_DEPTH_1_REG",           	0x6088,
"MAA_IPIPE_WPTR_1_REG",            	0x608C,
"MAA_IPIPE_RPTR_1_REG",            	0x6090,
"MAA_IPIPE_THRH_1_REG",            	0x6094,
"MAA_IPIPE_PTR_ADDR_L_1_REG",      	0x6098,
"MAA_IPIPE_PTR_ADDR_H_1_REG",      	0x609C,
"MAA_IPIPE_CTRL_1_REG",            	0x60CC,
"MAA_IPIPE_DBG1_1_REG",            	0x60D0,
"MAA_IPIPE_DBG0_1_REG",            	0x60D4,
"MAA_IPIPE_BASE_ADDR_L_2_REG",     	0x6100,
"MAA_IPIPE_BASE_ADDR_H_2_REG",     	0x6104,
"MAA_IPIPE_DEPTH_2_REG",           	0x6108,
"MAA_IPIPE_WPTR_2_REG",            	0x610C,
"MAA_IPIPE_RPTR_2_REG",            	0x6110,
"MAA_IPIPE_THRH_2_REG",            	0x6114,
"MAA_IPIPE_PTR_ADDR_L_2_REG",      	0x6118,
"MAA_IPIPE_PTR_ADDR_H_2_REG",      	0x611C,
"MAA_IPIPE_CTRL_2_REG",            	0x614C,
"MAA_IPIPE_DBG1_2_REG",            	0x6150,
"MAA_IPIPE_DBG0_2_REG",            	0x6154,
"MAA_IPIPE_BASE_ADDR_L_3_REG",     	0x6180,
"MAA_IPIPE_BASE_ADDR_H_3_REG",     	0x6184,
"MAA_IPIPE_DEPTH_3_REG",           	0x6188,
"MAA_IPIPE_WPTR_3_REG",            	0x618C,
"MAA_IPIPE_RPTR_3_REG",            	0x6190,
"MAA_IPIPE_THRH_3_REG",            	0x6194,
"MAA_IPIPE_PTR_ADDR_L_3_REG",      	0x6198,
"MAA_IPIPE_PTR_ADDR_H_3_REG",      	0x619C,
"MAA_IPIPE_CTRL_3_REG",            	0x61CC,
"MAA_IPIPE_DBG1_3_REG",            	0x61D0,
"MAA_IPIPE_DBG0_3_REG",            	0x61D4,
"MAA_IPIPE_BASE_ADDR_L_4_REG",     	0x6200,
"MAA_IPIPE_BASE_ADDR_H_4_REG",     	0x6204,
"MAA_IPIPE_DEPTH_4_REG",           	0x6208,
"MAA_IPIPE_WPTR_4_REG",            	0x620C,
"MAA_IPIPE_RPTR_4_REG",            	0x6210,
"MAA_IPIPE_THRH_4_REG",            	0x6214,
"MAA_IPIPE_PTR_ADDR_L_4_REG",      	0x6218,
"MAA_IPIPE_PTR_ADDR_H_4_REG",      	0x621C,
"MAA_IPIPE_CTRL_4_REG",            	0x624C,
"MAA_IPIPE_DBG1_4_REG",            	0x6250,
"MAA_IPIPE_DBG0_4_REG",            	0x6254,
"MAA_IPIPE_BASE_ADDR_L_5_REG",     	0x6280,
"MAA_IPIPE_BASE_ADDR_H_5_REG",     	0x6284,
"MAA_IPIPE_DEPTH_5_REG",           	0x6288,
"MAA_IPIPE_WPTR_5_REG",            	0x628C,
"MAA_IPIPE_RPTR_5_REG",            	0x6290,
"MAA_IPIPE_THRH_5_REG",            	0x6294,
"MAA_IPIPE_PTR_ADDR_L_5_REG",      	0x6298,
"MAA_IPIPE_PTR_ADDR_H_5_REG",      	0x629C,
"MAA_IPIPE_CTRL_5_REG",            	0x62CC,
"MAA_IPIPE_DBG1_5_REG",            	0x62D0,
"MAA_IPIPE_DBG0_5_REG",            	0x62D4,
"MAA_IPIPE_BASE_ADDR_L_6_REG",     	0x6300,
"MAA_IPIPE_BASE_ADDR_H_6_REG",     	0x6304,
"MAA_IPIPE_DEPTH_6_REG",           	0x6308,
"MAA_IPIPE_WPTR_6_REG",            	0x630C,
"MAA_IPIPE_RPTR_6_REG",            	0x6310,
"MAA_IPIPE_THRH_6_REG",            	0x6314,
"MAA_IPIPE_PTR_ADDR_L_6_REG",      	0x6318,
"MAA_IPIPE_PTR_ADDR_H_6_REG",      	0x631C,
"MAA_IPIPE_CTRL_6_REG",            	0x634C,
"MAA_IPIPE_DBG1_6_REG",            	0x6350,
"MAA_IPIPE_DBG0_6_REG",            	0x6354,
"MAA_IPIPE_BASE_ADDR_L_7_REG",     	0x6380,
"MAA_IPIPE_BASE_ADDR_H_7_REG",     	0x6384,
"MAA_IPIPE_DEPTH_7_REG",           	0x6388,
"MAA_IPIPE_WPTR_7_REG",            	0x638C,
"MAA_IPIPE_RPTR_7_REG",            	0x6390,
"MAA_IPIPE_THRH_7_REG",            	0x6394,
"MAA_IPIPE_PTR_ADDR_L_7_REG",      	0x6398,
"MAA_IPIPE_PTR_ADDR_H_7_REG",      	0x639C,
"MAA_IPIPE_CTRL_7_REG",            	0x63CC,
"MAA_IPIPE_DBG1_7_REG",            	0x63D0,
"MAA_IPIPE_DBG0_7_REG",            	0x63D4,
"MAA_IPIPE_BASE_ADDR_L_8_REG",     	0x6400,
"MAA_IPIPE_BASE_ADDR_H_8_REG",     	0x6404,
"MAA_IPIPE_DEPTH_8_REG",           	0x6408,
"MAA_IPIPE_WPTR_8_REG",            	0x640C,
"MAA_IPIPE_RPTR_8_REG",            	0x6410,
"MAA_IPIPE_THRH_8_REG",            	0x6414,
"MAA_IPIPE_PTR_ADDR_L_8_REG",      	0x6418,
"MAA_IPIPE_PTR_ADDR_H_8_REG",      	0x641C,
"MAA_IPIPE_CTRL_8_REG",            	0x644C,
"MAA_IPIPE_DBG1_8_REG",            	0x6450,
"MAA_IPIPE_DBG0_8_REG",            	0x6454,
"MAA_IPIPE_BASE_ADDR_L_9_REG",     	0x6480,
"MAA_IPIPE_BASE_ADDR_H_9_REG",     	0x6484,
"MAA_IPIPE_DEPTH_9_REG",           	0x6488,
"MAA_IPIPE_WPTR_9_REG",            	0x648C,
"MAA_IPIPE_RPTR_9_REG",            	0x6490,
"MAA_IPIPE_THRH_9_REG",            	0x6494,
"MAA_IPIPE_PTR_ADDR_L_9_REG",      	0x6498,
"MAA_IPIPE_PTR_ADDR_H_9_REG",      	0x649C,
"MAA_IPIPE_CTRL_9_REG",            	0x64CC,
"MAA_IPIPE_DBG1_9_REG",            	0x64D0,
"MAA_IPIPE_DBG0_9_REG",            	0x64D4,
"MAA_IPIPE_BASE_ADDR_L_10_REG",    	0x6500,
"MAA_IPIPE_BASE_ADDR_H_10_REG",    	0x6504,
"MAA_IPIPE_DEPTH_10_REG",          	0x6508,
"MAA_IPIPE_WPTR_10_REG",           	0x650C,
"MAA_IPIPE_RPTR_10_REG",           	0x6510,
"MAA_IPIPE_THRH_10_REG",           	0x6514,
"MAA_IPIPE_PTR_ADDR_L_10_REG",     	0x6518,
"MAA_IPIPE_PTR_ADDR_H_10_REG",     	0x651C,
"MAA_IPIPE_CTRL_10_REG",           	0x654C,
"MAA_IPIPE_DBG1_10_REG",           	0x6550,
"MAA_IPIPE_DBG0_10_REG",           	0x6554,
"MAA_IPIPE_BASE_ADDR_L_11_REG",    	0x6580,
"MAA_IPIPE_BASE_ADDR_H_11_REG",    	0x6584,
"MAA_IPIPE_DEPTH_11_REG",          	0x6588,
"MAA_IPIPE_WPTR_11_REG",           	0x658C,
"MAA_IPIPE_RPTR_11_REG",           	0x6590,
"MAA_IPIPE_THRH_11_REG",           	0x6594,
"MAA_IPIPE_PTR_ADDR_L_11_REG",     	0x6598,
"MAA_IPIPE_PTR_ADDR_H_11_REG",     	0x659C,
"MAA_IPIPE_CTRL_11_REG",           	0x65CC,
"MAA_IPIPE_DBG1_11_REG",           	0x65D0,
"MAA_IPIPE_DBG0_11_REG",           	0x65D4,
"MAA_IPIPE_BASE_ADDR_L_12_REG",    	0x6600,
"MAA_IPIPE_BASE_ADDR_H_12_REG",    	0x6604,
"MAA_IPIPE_DEPTH_12_REG",          	0x6608,
"MAA_IPIPE_WPTR_12_REG",           	0x660C,
"MAA_IPIPE_RPTR_12_REG",           	0x6610,
"MAA_IPIPE_THRH_12_REG",           	0x6614,
"MAA_IPIPE_PTR_ADDR_L_12_REG",     	0x6618,
"MAA_IPIPE_PTR_ADDR_H_12_REG",     	0x661C,
"MAA_IPIPE_CTRL_12_REG",           	0x664C,
"MAA_IPIPE_DBG1_12_REG",           	0x6650,
"MAA_IPIPE_DBG0_12_REG",           	0x6654,
"MAA_IPIPE_BASE_ADDR_L_13_REG",    	0x6680,
"MAA_IPIPE_BASE_ADDR_H_13_REG",    	0x6684,
"MAA_IPIPE_DEPTH_13_REG",          	0x6688,
"MAA_IPIPE_WPTR_13_REG",           	0x668C,
"MAA_IPIPE_RPTR_13_REG",           	0x6690,
"MAA_IPIPE_THRH_13_REG",           	0x6694,
"MAA_IPIPE_PTR_ADDR_L_13_REG",     	0x6698,
"MAA_IPIPE_PTR_ADDR_H_13_REG",     	0x669C,
"MAA_IPIPE_CTRL_13_REG",           	0x66CC,
"MAA_IPIPE_DBG1_13_REG",           	0x66D0,
"MAA_IPIPE_DBG0_13_REG",           	0x66D4,
"MAA_IPIPE_BASE_ADDR_L_14_REG",    	0x6700,
"MAA_IPIPE_BASE_ADDR_H_14_REG",    	0x6704,
"MAA_IPIPE_DEPTH_14_REG",          	0x6708,
"MAA_IPIPE_WPTR_14_REG",           	0x670C,
"MAA_IPIPE_RPTR_14_REG",           	0x6710,
"MAA_IPIPE_THRH_14_REG",           	0x6714,
"MAA_IPIPE_PTR_ADDR_L_14_REG",     	0x6718,
"MAA_IPIPE_PTR_ADDR_H_14_REG",     	0x671C,
"MAA_IPIPE_CTRL_14_REG",           	0x674C,
"MAA_IPIPE_DBG1_14_REG",           	0x6750,
"MAA_IPIPE_DBG0_14_REG",           	0x6754,
"MAA_IPIPE_BASE_ADDR_L_15_REG",    	0x6780,
"MAA_IPIPE_BASE_ADDR_H_15_REG",    	0x6784,
"MAA_IPIPE_DEPTH_15_REG",          	0x6788,
"MAA_IPIPE_WPTR_15_REG",           	0x678C,
"MAA_IPIPE_RPTR_15_REG",           	0x6790,
"MAA_IPIPE_THRH_15_REG",           	0x6794,
"MAA_IPIPE_PTR_ADDR_L_15_REG",     	0x6798,
"MAA_IPIPE_PTR_ADDR_H_15_REG",     	0x679C,
"MAA_IPIPE_CTRL_15_REG",           	0x67CC,
"MAA_IPIPE_DBG1_15_REG",           	0x67D0,
"MAA_IPIPE_DBG0_15_REG",           	0x67D4,
"MAA_IPIPE_BASE_ADDR_L_16_REG",    	0x6800,
"MAA_IPIPE_BASE_ADDR_H_16_REG",    	0x6804,
"MAA_IPIPE_DEPTH_16_REG",          	0x6808,
"MAA_IPIPE_WPTR_16_REG",           	0x680C,
"MAA_IPIPE_RPTR_16_REG",           	0x6810,
"MAA_IPIPE_THRH_16_REG",           	0x6814,
"MAA_IPIPE_PTR_ADDR_L_16_REG",     	0x6818,
"MAA_IPIPE_PTR_ADDR_H_16_REG",     	0x681C,
"MAA_IPIPE_CTRL_16_REG",           	0x684C,
"MAA_IPIPE_DBG1_16_REG",           	0x6850,
"MAA_IPIPE_DBG0_16_REG",           	0x6854,
"MAA_IPIPE_BASE_ADDR_L_17_REG",    	0x6880,
"MAA_IPIPE_BASE_ADDR_H_17_REG",    	0x6884,
"MAA_IPIPE_DEPTH_17_REG",          	0x6888,
"MAA_IPIPE_WPTR_17_REG",           	0x688C,
"MAA_IPIPE_RPTR_17_REG",           	0x6890,
"MAA_IPIPE_THRH_17_REG",           	0x6894,
"MAA_IPIPE_PTR_ADDR_L_17_REG",     	0x6898,
"MAA_IPIPE_PTR_ADDR_H_17_REG",     	0x689C,
"MAA_IPIPE_CTRL_17_REG",           	0x68CC,
"MAA_IPIPE_DBG1_17_REG",           	0x68D0,
"MAA_IPIPE_DBG0_17_REG",           	0x68D4,
"MAA_IPIPE_BASE_ADDR_L_18_REG",    	0x6900,
"MAA_IPIPE_BASE_ADDR_H_18_REG",    	0x6904,
"MAA_IPIPE_DEPTH_18_REG",          	0x6908,
"MAA_IPIPE_WPTR_18_REG",           	0x690C,
"MAA_IPIPE_RPTR_18_REG",           	0x6910,
"MAA_IPIPE_THRH_18_REG",           	0x6914,
"MAA_IPIPE_PTR_ADDR_L_18_REG",     	0x6918,
"MAA_IPIPE_PTR_ADDR_H_18_REG",     	0x691C,
"MAA_IPIPE_CTRL_18_REG",           	0x694C,
"MAA_IPIPE_DBG1_18_REG",           	0x6950,
"MAA_IPIPE_DBG0_18_REG",           	0x6954,
"MAA_IPIPE_BASE_ADDR_L_19_REG",    	0x6980,
"MAA_IPIPE_BASE_ADDR_H_19_REG",    	0x6984,
"MAA_IPIPE_DEPTH_19_REG",          	0x6988,
"MAA_IPIPE_WPTR_19_REG",           	0x698C,
"MAA_IPIPE_RPTR_19_REG",           	0x6990,
"MAA_IPIPE_THRH_19_REG",           	0x6994,
"MAA_IPIPE_PTR_ADDR_L_19_REG",     	0x6998,
"MAA_IPIPE_PTR_ADDR_H_19_REG",     	0x699C,
"MAA_IPIPE_CTRL_19_REG",           	0x69CC,
"MAA_IPIPE_DBG1_19_REG",           	0x69D0,
"MAA_IPIPE_DBG0_19_REG",           	0x69D4,
"MAA_IPIPE_BASE_ADDR_L_20_REG",    	0x6A00,
"MAA_IPIPE_BASE_ADDR_H_20_REG",    	0x6A04,
"MAA_IPIPE_DEPTH_20_REG",          	0x6A08,
"MAA_IPIPE_WPTR_20_REG",           	0x6A0C,
"MAA_IPIPE_RPTR_20_REG",           	0x6A10,
"MAA_IPIPE_THRH_20_REG",           	0x6A14,
"MAA_IPIPE_PTR_ADDR_L_20_REG",     	0x6A18,
"MAA_IPIPE_PTR_ADDR_H_20_REG",     	0x6A1C,
"MAA_IPIPE_CTRL_20_REG",           	0x6A4C,
"MAA_IPIPE_DBG1_20_REG",           	0x6A50,
"MAA_IPIPE_DBG0_20_REG",           	0x6A54,
"MAA_IPIPE_BASE_ADDR_L_21_REG",    	0x6A80,
"MAA_IPIPE_BASE_ADDR_H_21_REG",    	0x6A84,
"MAA_IPIPE_DEPTH_21_REG",          	0x6A88,
"MAA_IPIPE_WPTR_21_REG",           	0x6A8C,
"MAA_IPIPE_RPTR_21_REG",           	0x6A90,
"MAA_IPIPE_THRH_21_REG",           	0x6A94,
"MAA_IPIPE_PTR_ADDR_L_21_REG",     	0x6A98,
"MAA_IPIPE_PTR_ADDR_H_21_REG",     	0x6A9C,
"MAA_IPIPE_CTRL_21_REG",           	0x6ACC,
"MAA_IPIPE_DBG1_21_REG",           	0x6AD0,
"MAA_IPIPE_DBG0_21_REG",           	0x6AD4,
"MAA_IPIPE_BASE_ADDR_L_22_REG",    	0x6B00,
"MAA_IPIPE_BASE_ADDR_H_22_REG",    	0x6B04,
"MAA_IPIPE_DEPTH_22_REG",          	0x6B08,
"MAA_IPIPE_WPTR_22_REG",           	0x6B0C,
"MAA_IPIPE_RPTR_22_REG",           	0x6B10,
"MAA_IPIPE_THRH_22_REG",           	0x6B14,
"MAA_IPIPE_PTR_ADDR_L_22_REG",     	0x6B18,
"MAA_IPIPE_PTR_ADDR_H_22_REG",     	0x6B1C,
"MAA_IPIPE_CTRL_22_REG",           	0x6B4C,
"MAA_IPIPE_DBG1_22_REG",           	0x6B50,
"MAA_IPIPE_DBG0_22_REG",           	0x6B54,
"MAA_IPIPE_BASE_ADDR_L_23_REG",    	0x6B80,
"MAA_IPIPE_BASE_ADDR_H_23_REG",    	0x6B84,
"MAA_IPIPE_DEPTH_23_REG",          	0x6B88,
"MAA_IPIPE_WPTR_23_REG",           	0x6B8C,
"MAA_IPIPE_RPTR_23_REG",           	0x6B90,
"MAA_IPIPE_THRH_23_REG",           	0x6B94,
"MAA_IPIPE_PTR_ADDR_L_23_REG",     	0x6B98,
"MAA_IPIPE_PTR_ADDR_H_23_REG",     	0x6B9C,
"MAA_IPIPE_CTRL_23_REG",           	0x6BCC,
"MAA_IPIPE_DBG1_23_REG",           	0x6BD0,
"MAA_IPIPE_DBG0_23_REG",           	0x6BD4,
"MAA_IPIPE_BASE_ADDR_L_24_REG",    	0x6C00,
"MAA_IPIPE_BASE_ADDR_H_24_REG",    	0x6C04,
"MAA_IPIPE_DEPTH_24_REG",          	0x6C08,
"MAA_IPIPE_WPTR_24_REG",           	0x6C0C,
"MAA_IPIPE_RPTR_24_REG",           	0x6C10,
"MAA_IPIPE_THRH_24_REG",           	0x6C14,
"MAA_IPIPE_PTR_ADDR_L_24_REG",     	0x6C18,
"MAA_IPIPE_PTR_ADDR_H_24_REG",     	0x6C1C,
"MAA_IPIPE_CTRL_24_REG",           	0x6C4C,
"MAA_IPIPE_DBG1_24_REG",           	0x6C50,
"MAA_IPIPE_DBG0_24_REG",           	0x6C54,
"MAA_IPIPE_BASE_ADDR_L_25_REG",    	0x6C80,
"MAA_IPIPE_BASE_ADDR_H_25_REG",    	0x6C84,
"MAA_IPIPE_DEPTH_25_REG",          	0x6C88,
"MAA_IPIPE_WPTR_25_REG",           	0x6C8C,
"MAA_IPIPE_RPTR_25_REG",           	0x6C90,
"MAA_IPIPE_THRH_25_REG",           	0x6C94,
"MAA_IPIPE_PTR_ADDR_L_25_REG",     	0x6C98,
"MAA_IPIPE_PTR_ADDR_H_25_REG",     	0x6C9C,
"MAA_IPIPE_CTRL_25_REG",           	0x6CCC,
"MAA_IPIPE_DBG1_25_REG",           	0x6CD0,
"MAA_IPIPE_DBG0_25_REG",           	0x6CD4,
"MAA_IPIPE_BASE_ADDR_L_26_REG",    	0x6D00,
"MAA_IPIPE_BASE_ADDR_H_26_REG",    	0x6D04,
"MAA_IPIPE_DEPTH_26_REG",          	0x6D08,
"MAA_IPIPE_WPTR_26_REG",           	0x6D0C,
"MAA_IPIPE_RPTR_26_REG",           	0x6D10,
"MAA_IPIPE_THRH_26_REG",           	0x6D14,
"MAA_IPIPE_PTR_ADDR_L_26_REG",     	0x6D18,
"MAA_IPIPE_PTR_ADDR_H_26_REG",     	0x6D1C,
"MAA_IPIPE_CTRL_26_REG",           	0x6D4C,
"MAA_IPIPE_DBG1_26_REG",           	0x6D50,
"MAA_IPIPE_DBG0_26_REG",           	0x6D54,
"MAA_IPIPE_BASE_ADDR_L_27_REG",    	0x6D80,
"MAA_IPIPE_BASE_ADDR_H_27_REG",    	0x6D84,
"MAA_IPIPE_DEPTH_27_REG",          	0x6D88,
"MAA_IPIPE_WPTR_27_REG",           	0x6D8C,
"MAA_IPIPE_RPTR_27_REG",           	0x6D90,
"MAA_IPIPE_THRH_27_REG",           	0x6D94,
"MAA_IPIPE_PTR_ADDR_L_27_REG",     	0x6D98,
"MAA_IPIPE_PTR_ADDR_H_27_REG",     	0x6D9C,
"MAA_IPIPE_CTRL_27_REG",           	0x6DCC,
"MAA_IPIPE_DBG1_27_REG",           	0x6DD0,
"MAA_IPIPE_DBG0_27_REG",           	0x6DD4,
"MAA_IPIPE_BASE_ADDR_L_28_REG",    	0x6E00,
"MAA_IPIPE_BASE_ADDR_H_28_REG",    	0x6E04,
"MAA_IPIPE_DEPTH_28_REG",          	0x6E08,
"MAA_IPIPE_WPTR_28_REG",           	0x6E0C,
"MAA_IPIPE_RPTR_28_REG",           	0x6E10,
"MAA_IPIPE_THRH_28_REG",           	0x6E14,
"MAA_IPIPE_PTR_ADDR_L_28_REG",     	0x6E18,
"MAA_IPIPE_PTR_ADDR_H_28_REG",     	0x6E1C,
"MAA_IPIPE_CTRL_28_REG",           	0x6E4C,
"MAA_IPIPE_DBG1_28_REG",           	0x6E50,
"MAA_IPIPE_DBG0_28_REG",           	0x6E54,
"MAA_IPIPE_BASE_ADDR_L_29_REG",    	0x6E80,
"MAA_IPIPE_BASE_ADDR_H_29_REG",    	0x6E84,
"MAA_IPIPE_DEPTH_29_REG",          	0x6E88,
"MAA_IPIPE_WPTR_29_REG",           	0x6E8C,
"MAA_IPIPE_RPTR_29_REG",           	0x6E90,
"MAA_IPIPE_THRH_29_REG",           	0x6E94,
"MAA_IPIPE_PTR_ADDR_L_29_REG",     	0x6E98,
"MAA_IPIPE_PTR_ADDR_H_29_REG",     	0x6E9C,
"MAA_IPIPE_CTRL_29_REG",           	0x6ECC,
"MAA_IPIPE_DBG1_29_REG",           	0x6ED0,
"MAA_IPIPE_DBG0_29_REG",           	0x6ED4,
"MAA_IPIPE_BASE_ADDR_L_30_REG",    	0x6F00,
"MAA_IPIPE_BASE_ADDR_H_30_REG",    	0x6F04,
"MAA_IPIPE_DEPTH_30_REG",          	0x6F08,
"MAA_IPIPE_WPTR_30_REG",           	0x6F0C,
"MAA_IPIPE_RPTR_30_REG",           	0x6F10,
"MAA_IPIPE_THRH_30_REG",           	0x6F14,
"MAA_IPIPE_PTR_ADDR_L_30_REG",     	0x6F18,
"MAA_IPIPE_PTR_ADDR_H_30_REG",     	0x6F1C,
"MAA_IPIPE_CTRL_30_REG",           	0x6F4C,
"MAA_IPIPE_DBG1_30_REG",           	0x6F50,
"MAA_IPIPE_DBG0_30_REG",           	0x6F54,
"MAA_IPIPE_BASE_ADDR_L_31_REG",    	0x6F80,
"MAA_IPIPE_BASE_ADDR_H_31_REG",    	0x6F84,
"MAA_IPIPE_DEPTH_31_REG",          	0x6F88,
"MAA_IPIPE_WPTR_31_REG",           	0x6F8C,
"MAA_IPIPE_RPTR_31_REG",           	0x6F90,
"MAA_IPIPE_THRH_31_REG",           	0x6F94,
"MAA_IPIPE_PTR_ADDR_L_31_REG",     	0x6F98,
"MAA_IPIPE_PTR_ADDR_H_31_REG",     	0x6F9C,
"MAA_IPIPE_CTRL_31_REG",           	0x6FCC,
"MAA_IPIPE_DBG1_31_REG",           	0x6FD0,
"MAA_IPIPE_DBG0_31_REG",           	0x6FD4,
"MAA_IPIPE_BASE_ADDR_L_32_REG",    	0x7000,
"MAA_IPIPE_BASE_ADDR_H_32_REG",    	0x7004,
"MAA_IPIPE_DEPTH_32_REG",          	0x7008,
"MAA_IPIPE_WPTR_32_REG",           	0x700C,
"MAA_IPIPE_RPTR_32_REG",           	0x7010,
"MAA_IPIPE_THRH_32_REG",           	0x7014,
"MAA_IPIPE_PTR_ADDR_L_32_REG",     	0x7018,
"MAA_IPIPE_PTR_ADDR_H_32_REG",     	0x701C,
"MAA_IPIPE_CTRL_32_REG",           	0x704C,
"MAA_IPIPE_DBG1_32_REG",           	0x7050,
"MAA_IPIPE_DBG0_32_REG",           	0x7054,
"MAA_IPIPE_BASE_ADDR_L_33_REG",    	0x7080,
"MAA_IPIPE_BASE_ADDR_H_33_REG",    	0x7084,
"MAA_IPIPE_DEPTH_33_REG",          	0x7088,
"MAA_IPIPE_WPTR_33_REG",           	0x708C,
"MAA_IPIPE_RPTR_33_REG",           	0x7090,
"MAA_IPIPE_THRH_33_REG",           	0x7094,
"MAA_IPIPE_PTR_ADDR_L_33_REG",     	0x7098,
"MAA_IPIPE_PTR_ADDR_H_33_REG",     	0x709C,
"MAA_IPIPE_CTRL_33_REG",           	0x70CC,
"MAA_IPIPE_DBG1_33_REG",           	0x70D0,
"MAA_IPIPE_DBG0_33_REG",           	0x70D4,
"MAA_IPIPE_BASE_ADDR_L_34_REG",    	0x7100,
"MAA_IPIPE_BASE_ADDR_H_34_REG",    	0x7104,
"MAA_IPIPE_DEPTH_34_REG",          	0x7108,
"MAA_IPIPE_WPTR_34_REG",           	0x710C,
"MAA_IPIPE_RPTR_34_REG",           	0x7110,
"MAA_IPIPE_THRH_34_REG",           	0x7114,
"MAA_IPIPE_PTR_ADDR_L_34_REG",     	0x7118,
"MAA_IPIPE_PTR_ADDR_H_34_REG",     	0x711C,
"MAA_IPIPE_CTRL_34_REG",           	0x714C,
"MAA_IPIPE_DBG1_34_REG",           	0x7150,
"MAA_IPIPE_DBG0_34_REG",           	0x7154,
"MAA_IPIPE_BASE_ADDR_L_35_REG",    	0x7180,
"MAA_IPIPE_BASE_ADDR_H_35_REG",    	0x7184,
"MAA_IPIPE_DEPTH_35_REG",          	0x7188,
"MAA_IPIPE_WPTR_35_REG",           	0x718C,
"MAA_IPIPE_RPTR_35_REG",           	0x7190,
"MAA_IPIPE_THRH_35_REG",           	0x7194,
"MAA_IPIPE_PTR_ADDR_L_35_REG",     	0x7198,
"MAA_IPIPE_PTR_ADDR_H_35_REG",     	0x719C,
"MAA_IPIPE_CTRL_35_REG",           	0x71CC,
"MAA_IPIPE_DBG1_35_REG",           	0x71D0,
"MAA_IPIPE_DBG0_35_REG",           	0x71D4,
]

def maa_entry_parse(infile, outfile, offset):
    for i in range(0, int(int(len(maa_field_def)+1)/2)):
        infile.seek(0 + offset+int(maa_field_def[i*2+1]))
        (reg, ) = struct.unpack("I", infile.read(4))
        outfile.writelines("%s 0x%08x\n" %(maa_field_def[i*2], reg))
    return

def entry_0x200009F(infile, field, offset, slen, version, mode, outfile):
        try:
            offset_v = eval(offset)
            maa_entry_parse(infile, outfile, offset_v)
            return 0

        except Exception as e:
            print((str(e)))
            outfile.writelines(str(e))
            return 1


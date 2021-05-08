#!/usr/bin/env python3
#coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename      field_0x2000079_0000.py
# * Description   analysis psam dump
#***********************************************************************
'''
Created on 2014-11-14
 
@
'''
import os
import re
import struct
import sys

psam_field_def = [
    "HI_PSAM_SRST_OFFSET",                            0x0,
    "HI_PSAM_CONFIG_OFFSET",                          0x4,
    "HI_PSAM_VERSION_OFFSET",                         0x8,
    "HI_PSAM_EN_OFFSET",                              0xc,
    "HI_PSAM_INT0_STAT_OFFSET",                       0x40,
    "HI_PSAM_INT0_MSTAT_OFFSET",                      0x44,
    "HI_PSAM_INT0_MASK_OFFSET",                       0x48,
    "HI_PSAM_INT1_STAT_OFFSET",                       0x50,
    "HI_PSAM_INT1_MSTAT_OFFSET",                      0x54,
    "HI_PSAM_INT1_MASK_OFFSET",                       0x58,
    "HI_PSAM_INT2_STAT_OFFSET",                       0x60,
    "HI_PSAM_INT2_MSTAT_OFFSET",                      0x64,
    "HI_PSAM_INT2_MASK_OFFSET",                       0x68,
    "HI_PSAM_CIPHER_SOFTRESET_OFFSET",                0x70,
    "HI_PSAM_CBDQ_UPDATE_OFFSET",                     0x74,
    "HI_PSAM32_CIPHER_CH_SOFTRESET_0_OFFSET",           0x80,
    "HI_PSAM32_CIPHER_CH_SOFTRESET_1_OFFSET",           0xa0,
    "HI_PSAM32_CIPHER_CH_SOFTRESET_2_OFFSET",           0xc0,
	"HI_PSAM64_CIPHER_CH_SOFTRESET_0_OFFSET",           0x80,
    "HI_PSAM64_CIPHER_CH_SOFTRESET_1_OFFSET",           0xc0,
    "HI_PSAM64_CIPHER_CH_SOFTRESET_2_OFFSET",           0x100,
    "HI_PSAM_CIPHER_CH_EN_0_OFFSET",                  0x84,
    "HI_PSAM32_CIPHER_CH_EN_1_OFFSET",                  0xa4,
    "HI_PSAM32_CIPHER_CH_EN_2_OFFSET",                  0xc4,
	"HI_PSAM64_CIPHER_CH_EN_1_OFFSET",                  0xc4,
    "HI_PSAM64_CIPHER_CH_EN_2_OFFSET",                  0x104,
    "HI_PSAM32_CBDQ_CONFIG_0_OFFSET",                   0x88,
    "HI_PSAM32_CBDQ_CONFIG_1_OFFSET",                   0xa8,
    "HI_PSAM32_CBDQ_CONFIG_2_OFFSET",                   0xc8,
	"HI_PSAM64_CBDQ_CONFIG_0_OFFSET",                   0x88,
    "HI_PSAM64_CBDQ_CONFIG_1_OFFSET",                   0xc8,
    "HI_PSAM64_CBDQ_CONFIG_2_OFFSET",                   0x108,
    "HI_PSAM32_CBDQ_BADDR_0_OFFSET",                    0x8c,
    "HI_PSAM32_CBDQ_BADDR_1_OFFSET",                    0xac,
    "HI_PSAM32_CBDQ_BADDR_2_OFFSET",                    0xcc,
	"HI_PSAM64_CBDQ_BADDR_L_0_OFFSET",                  0x90,
    "HI_PSAM64_CBDQ_BADDR_L_1_OFFSET",                  0xd0,
    "HI_PSAM64_CBDQ_BADDR_L_2_OFFSET",                  0x110,
    "HI_PSAM64_CBDQ_BADDR_H_0_OFFSET",                  0x94,
    "HI_PSAM64_CBDQ_BADDR_H_1_OFFSET",                  0xd4,
    "HI_PSAM64_CBDQ_BADDR_H_2_OFFSET",                  0x114,
    "HI_PSAM32_CBDQ_SIZE_0_OFFSET",                     0x90,
    "HI_PSAM32_CBDQ_SIZE_1_OFFSET",                     0xb0,
    "HI_PSAM32_CBDQ_SIZE_2_OFFSET",                     0xd0,
	"HI_PSAM64_CBDQ_SIZE_0_OFFSET",                     0x8c,
    "HI_PSAM64_CBDQ_SIZE_1_OFFSET",                     0xcc,
    "HI_PSAM64_CBDQ_SIZE_2_OFFSET",                     0x10c,
    "HI_PSAM32_CBDQ_WPTR_0_OFFSET",                     0x94,
    "HI_PSAM32_CBDQ_WPTR_1_OFFSET",                     0xb4,
    "HI_PSAM32_CBDQ_WPTR_2_OFFSET",                     0xd4,
	"HI_PSAM64_CBDQ_WPTR_0_OFFSET",                     0x98,
    "HI_PSAM64_CBDQ_WPTR_1_OFFSET",                     0xd8,
    "HI_PSAM64_CBDQ_WPTR_2_OFFSET",                     0x118,
    "HI_PSAM32_CBDQ_STAT_0_OFFSET",                     0x98,
    "HI_PSAM32_CBDQ_STAT_1_OFFSET",                     0xb8,
    "HI_PSAM32_CBDQ_STAT_2_OFFSET",                     0xd8,
	"HI_PSAM64_CBDQ_STAT_0_OFFSET",                     0x9c,
    "HI_PSAM64_CBDQ_STAT_1_OFFSET",                     0xdc,
    "HI_PSAM64_CBDQ_STAT_2_OFFSET",                     0x11c,
    "HI_PSAM32_CBDQ_WPTR_ADDR_0_OFFSET",                0x9c,
    "HI_PSAM32_CBDQ_WPTR_ADDR_1_OFFSET",                0xbc,
    "HI_PSAM32_CBDQ_WPTR_ADDR_2_OFFSET",                0xdc,
	"HI_PSAM64_CBDQ_WPTR_ADDR_L_0_OFFSET",              0xa0,
    "HI_PSAM64_CBDQ_WPTR_ADDR_L_1_OFFSET",              0xe0,
    "HI_PSAM64_CBDQ_WPTR_ADDR_L_2_OFFSET",              0x120,
    "HI_PSAM64_CBDQ_WPTR_ADDR_H_0_OFFSET",              0xa4,
    "HI_PSAM64_CBDQ_WPTR_ADDR_H_1_OFFSET",              0xe4,
    "HI_PSAM64_CBDQ_WPTR_ADDR_H_2_OFFSET",              0x124,
    "HI_PSAM32_CRDQ_CTRL_0_OFFSET",                     0x100,
    "HI_PSAM32_CRDQ_CTRL_1_OFFSET",                     0x110,
    "HI_PSAM32_CRDQ_CTRL_2_OFFSET",                     0x120,
	"HI_PSAM64_CRDQ_CTRL_0_OFFSET",                     0x180,
    "HI_PSAM64_CRDQ_CTRL_1_OFFSET",                     0x1a0,
    "HI_PSAM64_CRDQ_CTRL_2_OFFSET",                     0x1c0,
    "HI_PSAM32_CRDQ_STAT_0_OFFSET",                     0x104,
    "HI_PSAM32_CRDQ_STAT_1_OFFSET",                     0x114,
    "HI_PSAM32_CRDQ_STAT_2_OFFSET",                     0x124,
	"HI_PSAM64_CRDQ_STAT_0_OFFSET",                     0x184,
    "HI_PSAM64_CRDQ_STAT_1_OFFSET",                     0x1a4,
    "HI_PSAM64_CRDQ_STAT_2_OFFSET",                     0x1c4,
    "HI_PSAM32_CRDQ_PTR_0_OFFSET",                      0x108,
    "HI_PSAM32_CRDQ_PTR_1_OFFSET",                      0x118,
    "HI_PSAM32_CRDQ_PTR_2_OFFSET",                      0x128,
	"HI_PSAM64_CRDQ_PTR_0_OFFSET",                      0x188,
    "HI_PSAM64_CRDQ_PTR_1_OFFSET",                      0x1a8,
    "HI_PSAM64_CRDQ_PTR_2_OFFSET",                      0x1c8,
    "HI_PSAM32_CRDQ_RPTR_ADDR_0_OFFSET",                0x10c,
    "HI_PSAM32_CRDQ_RPTR_ADDR_1_OFFSET",                0x11c,
    "HI_PSAM32_CRDQ_RPTR_ADDR_2_OFFSET",                0x12c,
	"HI_PSAM64_CRDQ_RPTR_ADDR_L_0_OFFSET",              0x190,
    "HI_PSAM64_CRDQ_RPTR_ADDR_L_1_OFFSET",              0x1b0,
    "HI_PSAM64_CRDQ_RPTR_ADDR_L_2_OFFSET",              0x1d0,
	"HI_PSAM64_CRDQ_RPTR_ADDR_H_0_OFFSET",              0x194,
    "HI_PSAM64_CRDQ_RPTR_ADDR_H_1_OFFSET",              0x1b4,
    "HI_PSAM64_CRDQ_RPTR_ADDR_H_2_OFFSET",              0x1d4,
    "HI_PSAM_IBDQ_STAT_OFFSET",                       0x154,
	"HI_PSAM64_IBDQ_STAT_OFFSET",                       0x208,
    "HI_PSAM32_IBDQ_BADDR_OFFSET",                      0x158,
	"HI_PSAM64_IBDQ_BADDR_L_OFFSET",                    0x200,
    "HI_PSAM64_IBDQ_BADDR_H_OFFSET",                    0x204,
    "HI_PSAM32_IBDQ_SIZE_OFFSET",                       0x15c,
	"HI_PSAM64_IBDQ_SIZE_OFFSET",                       0x20c,
    "HI_PSAM32_IBDQ_WPTR_OFFSET",                       0x160,
	"HI_PSAM64_IBDQ_WPTR_OFFSET",                       0x210,
    "HI_PSAM32_IBDQ_RPTR_OFFSET",                       0x164,
	"HI_PSAM64_IBDQ_RPTR_OFFSET",                       0x214,
    "HI_PSAM32_IBDQ_UPDATE_OFFSET",                     0x170,
	"HI_PSAM64_IBDQ_UPDATE_OFFSET",                     0x220,
    "HI_PSAM32_IBDQ_PKT_CNT_OFFSET",                    0x174,
	"HI_PSAM64_IBDQ_PKT_CNT_OFFSET",                    0x224,
    "HI_PSAM32_LBDQ_STAT_OFFSET",                       0x254,
	"HI_PSAM64_LBDQ_STAT_OFFSET",                       0x258,
    "HI_PSAM32_LBDQ_BADDR_OFFSET",                      0x258,
	"HI_PSAM64_LBDQ_BADDR_L_OFFSET",                    0x250,
    "HI_PSAM64_LBDQ_BADDR_H_OFFSET",                    0x254,
    "HI_PSAM_LBDQ_SIZE_OFFSET",                       0x25c,
    "HI_PSAM_LBDQ_WPTR_OFFSET",                       0x260,
    "HI_PSAM_LBDQ_RPTR_OFFSET",                       0x264,
    "HI_PSAM_LBDQ_DEPTH_OFFSET",                      0x268,
    "HI_PSAM_ADQ_CTRL_OFFSET",                        0x284,
    "HI_PSAM32_ADQ0_BASE_OFFSET",                       0x290,
	"HI_PSAM64_ADQ0_BASE_L_OFFSET",                     0x2b0,
    "HI_PSAM64_ADQ0_BASE_H_OFFSET",                     0x2b4,
    "HI_PSAM_ADQ0_STAT_OFFSET",                       0x294,
    "HI_PSAM_ADQ0_WPTR_OFFSET",                       0x298,
    "HI_PSAM_ADQ0_RPTR_OFFSET",                       0x29c,
    "HI_PSAM32_ADQ1_BASE_OFFSET",                       0x2a0,
	"HI_PSAM64_ADQ1_BASE_L_OFFSET",                     0x2b8,
    "HI_PSAM64_ADQ1_BASE_H_OFFSET",                     0x2bc,
    "HI_PSAM_ADQ1_STAT_OFFSET",                       0x2a4,
    "HI_PSAM_ADQ1_WPTR_OFFSET",                       0x2a8,
    "HI_PSAM_ADQ1_RPTR_OFFSET",                       0x2ac,
    "HI_PSAM32_ADQ_PADDR_ERR_OFFSET",                   0x2b0,
    "HI_PSAM32_ADQ_FAMA_ATTR_OFFSET",                   0x2b4,
    "HI_PSAM32_ADQ_PADDR_STR0_OFFSET",                  0x300,
    "HI_PSAM32_ADQ_PADDR_END0_OFFSET",                  0x304,
    "HI_PSAM32_ADQ_PADDR_STR1_OFFSET",                  0x308,
    "HI_PSAM32_ADQ_PADDR_END1_OFFSET",                  0x30c,
    "HI_PSAM32_ADQ_PADDR_STR2_OFFSET",                  0x310,
    "HI_PSAM32_ADQ_PADDR_END2_OFFSET",                  0x314,
    "HI_PSAM32_ADQ_PADDR_STR3_OFFSET",                  0x318,
    "HI_PSAM32_ADQ_PADDR_END3_OFFSET",                  0x31c,
    "HI_PSAM32_ADQ_PADDR_CTRL_OFFSET",                  0x320,
    "HI_PSAM32_CBDQ_FAMA_ATTR_OFFSET",                  0x330,
    "HI_PSAM32_IBDQ_FAMA_ATTR_OFFSET",                  0x334,
    "HI_PSAM32_LBDQ_FAMA_ATTR_OFFSET",                  0x338,
    "HI_PSAM32_ADQ_PADDR_FAMA0_OFFSET",                 0x340,
    "HI_PSAM32_ADQ_PADDR_FAMA1_OFFSET",                 0x344,
    "HI_PSAM32_ADQ_PADDR_FAMA2_OFFSET",                 0x348,
    "HI_PSAM32_ADQ_PADDR_FAMA3_OFFSET",                 0x34c,
    "HI_PSAM32_REG_END_OFFSET",                         0x350,
	"HI_PSAM64_SEC_CTRL_OFFSET",                        0x300,
    "HI_PSAM_CRDQ0_BADDR_OFFSET",                     0x400,
    "HI_PSAM_CRDQ1_BADDR_OFFSET",                     0x800,
    "HI_PSAM_CRDQ2_BADDR_OFFSET",                     0xc00,
]

def psam_entry_parse(infile, outfile, offset):
    for i in range(0, int(int(len(psam_field_def)+1)/2)):
        infile.seek(0 + offset+int(psam_field_def[i*2+1]))
        (reg, ) = struct.unpack("I", infile.read(4))
        outfile.writelines("%s 0x%08x\n" %(psam_field_def[i*2], reg))
    return

def entry_0x2000079(infile, field, offset, slen, version, mode, outfile):
        try:
            if not field == '0x2000079':
                print('hidis field is ', field)
                print('current field is', '0x2000079')
                return error['ERR_CHECK_FIELD']
            elif not version == '0x0000':
                print('hidis version is ', version)
                print('current version is ', '0x0000')
                return error['ERR_CHECK_VERSION']
            elif not slen == '0x400':
                print('hids len is ', slen)
                print('current len is ', '0x400')
                return error['ERR_CHECK_LEN']
            #outfile.writelines("got entry entry_0x2000079\n")
            offset_v = eval(offset)
            psam_entry_parse(infile, outfile, offset_v)
            return 0

        except Exception as e:
            print((str(e)))
            outfile.writelines(str(e))
            return 1

    

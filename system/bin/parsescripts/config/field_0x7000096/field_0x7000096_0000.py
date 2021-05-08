#!/usr/bin/env python3
# coding=utf-8
# -*- coding: utf-8 -*-
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename
# * Description   analysis excinfo dump
# * Version       1.0
# * Data          2019.6.28
#***********************************************************************
import struct
import os
import sys
import string
import config

def PrintFiqInfo(infile, field, offset, length, version, mode, outfile):
        MyOffset = eval(offset)
        infile.seek(MyOffset)
        corenum = config.get_core_num()
        for i in range(0, corenum):
            outfile.writelines("----core %d----\n" %i)
            g_acOSVer = infile.read(48)
            g_acAppVer = infile.read(64)
            (g_uwExcCause, ) = struct.unpack('I',infile.read(4))
            (g_uwThreadType, ) = struct.unpack('I',infile.read(4))
            (g_uwThreadID, ) = struct.unpack('I',infile.read(4))


            (g_usByteOrder, ) = struct.unpack('H',infile.read(2))
            (g_usCpuType, ) = struct.unpack('H',infile.read(2))
            (g_uwCpuID, ) = struct.unpack('I',infile.read(4))

            (g_stCpuTickHi, ) = struct.unpack('I',infile.read(4))
            (g_stCpuTickLo, ) = struct.unpack('I',infile.read(4))
            (g_uwNestCnt, ) = struct.unpack('I',infile.read(4))
            (g_uwSp, ) = struct.unpack('I',infile.read(4))
            (g_uwStackBottom, ) = struct.unpack('I',infile.read(4))


            (g_uwCPSR, ) = struct.unpack('I',infile.read(4))
            (g_uwSCTLR, ) = struct.unpack('I',infile.read(4))
            (g_uwDFAR, ) = struct.unpack('I',infile.read(4))
            (g_uwDFSR, ) = struct.unpack('I',infile.read(4))
            (g_uwIFSR, ) = struct.unpack('I',infile.read(4))
            (g_uwR0, ) = struct.unpack('I',infile.read(4))
            (g_uwR1, ) = struct.unpack('I',infile.read(4))
            (g_uwR2, ) = struct.unpack('I',infile.read(4))
            (g_uwR3, ) = struct.unpack('I',infile.read(4))
            (g_uwR4, ) = struct.unpack('I',infile.read(4))
            (g_uwR5, ) = struct.unpack('I',infile.read(4))
            (g_uwR6, ) = struct.unpack('I',infile.read(4))
            (g_uwR7, ) = struct.unpack('I',infile.read(4))
            (g_uwR8, ) = struct.unpack('I',infile.read(4))
            (g_uwR9, ) = struct.unpack('I',infile.read(4))
            (g_uwR10, ) = struct.unpack('I',infile.read(4))
            (g_uwR11, ) = struct.unpack('I',infile.read(4))
            (g_uwR12, ) = struct.unpack('I',infile.read(4))

            (g_uwSP, ) = struct.unpack('I',infile.read(4))
            (g_uwLR, ) = struct.unpack('I',infile.read(4))
            (g_uwPC, ) = struct.unpack('I',infile.read(4))

            outfile.writelines("OSVer               :%s\n" % g_acOSVer.decode(encoding="utf-8").strip('\x00'))
            outfile.writelines("AppVer              :%s\n" % g_acAppVer.decode(encoding="utf-8").strip('\x00'))
            outfile.writelines("ExcCause           :0x%08x\n" % g_uwExcCause)
            outfile.writelines("ThreadType        :0x%08x\n" % g_uwThreadType)
            outfile.writelines("ThreadID            :0x%08x\n" % g_uwThreadID)
            outfile.writelines("ByteOrder          :0x%08x\n" % g_usByteOrder)
            outfile.writelines("CpuType            :0x%08x\n" % g_usCpuType)
            outfile.writelines("CpuID               :0x%08x\n" % g_uwCpuID)
            outfile.writelines("CpuTickHi          :0x%08x\n" % g_stCpuTickHi)
            outfile.writelines("CpuTickLo          :0x%08x\n" % g_stCpuTickLo)
            outfile.writelines("NestCnt              :0x%08x\n" % g_uwNestCnt)
            outfile.writelines("Sp                      :0x%08x\n" % g_uwSp)
            outfile.writelines("StackBottom        :0x%08x\n" % g_uwStackBottom)
            outfile.writelines("CPSR                  :0x%08x\n" % g_uwCPSR)
            outfile.writelines("SCTLR                 :0x%08x\n" % g_uwSCTLR)
            outfile.writelines("DFAR                   :0x%08x\n" % g_uwDFAR)
            outfile.writelines("DFSR                   :0x%08x\n" % g_uwDFSR)
            outfile.writelines("IFSR                    :0x%08x\n" % g_uwIFSR)

            outfile.writelines("SP        :0x%08x\n" % g_uwSP)
            outfile.writelines("LR        :0x%08x\n" % g_uwLR)
            outfile.writelines("PC        :0x%08x\n" % g_uwPC)

        return

def entry_0x7000096(infile, field, offset, length, version, mode, outfile):
        try:
            if not field == '0x7000096':
                print('hidis field is ', field)
                print('current field is', '0x7000096')
                return error['ERR_CHECK_FIELD']
            elif not version == '0x0000':
                print('hidis version is ', version)
                print('current version is ', '0x0000')
                return error['ERR_CHECK_VERSION']
            elif not length == '0x1D8':
                print('hids len is ', length)
                print('current len is ', '0x1D8')
                #return error['ERR_CHECK_LEN']
            PrintFiqInfo(infile, field, offset, length, version, mode, outfile)
            return 0

        except Exception as e:
            print(str(e))
            outfile.write(str(e))
            return 1

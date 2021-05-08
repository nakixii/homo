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


class BaseInfo:
        def __init__(self):
                self.cpustatus = 0
                self.sysstatus = 0
                self.interrupt = 0
                self.curtask = 0
                self.taskname = ''
                self.reg = []
                self.CPSR = 0
                self.length = 0
                return

        def PrintExcInfo(self,infile,outfile):
                for i in range(0,self.length):
                        tag = infile.readline(1)
                        if tag != b'\x00':
                            outfile.writelines(tag.decode(encoding="utf-8"))
                return

        def PrintBaseInfo(self,outfile):
                outfile.writelines("CPU Status          :0x%x\n"  % self.cpustatus)
                outfile.writelines("Sys Status          :0x%x\n"  % self.sysstatus)
                outfile.writelines("Current Interrupt   :0x%x\n"  % self.interrupt)
                outfile.writelines("Current Task        :0x%08x\n"  % self.curtask)
                strTaskName = self.taskname.decode(encoding="utf-8")
                outfile.writelines("Current Task Name   :%s\n"    % strTaskName[:strTaskName.find('\x00')])
                outfile.writelines("Register13-15        :")
                for eachlist in self.reg:
                        outfile.writelines("0x%08x " % eachlist)
                outfile.writelines("\nCPSR                :0x%x\n"  % self.CPSR)
                return

def entry_0x2F00001(infile, field, offset, length, version, mode, outfile):
        try:
            if not field == '0x2F00001':
                print('hidis field is ', field)
                print('current field is', '0x2F00001')
                return error['ERR_CHECK_FIELD']
            elif not version == '0x0000':
                print('hidis version is ', version)
                print('current version is ', '0x0000')
                return error['ERR_CHECK_VERSION']
            elif not length == '0x400':
                print('hids len is ', length)
                print('current len is ', '0x400')
                return error['ERR_CHECK_LEN']
            base = BaseInfo()
            MyOffset = eval(offset)
            infile.seek(MyOffset)
            base.cpustatus, = struct.unpack('I',infile.read(4))
            base.sysstatus, = struct.unpack('I',infile.read(4))
            base.interrupt, = struct.unpack('I',infile.read(4))
            base.curtask, = struct.unpack('I',infile.read(4))
            base.taskname, = struct.unpack('16s',infile.read(16))
            #base.reg0to15, = struct.unpack('16I',infile.read(64))
            for i in range(0,16):
                reg, = struct.unpack('I',infile.read(4))
                if i > 12:
                    base.reg.append(reg)

            base.CPSR, = struct.unpack('I',infile.read(4))
            base.length = int(length,16) - 96
            base.PrintBaseInfo(outfile)
            base.PrintExcInfo(infile, outfile)

            return 0

        except Exception as e:
                print(str(e))
                outfile.write(str(e))
                return 1

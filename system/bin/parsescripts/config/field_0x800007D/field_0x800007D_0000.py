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

def PrintTaskSwitch(infile, field, offset, slen, version, mode, outfile):
        MyOffset = eval(offset)
        infile.seek(MyOffset)
        g_tasklist = []
        print("got entry 0x2000001 PrintTaskSwitch")
        (g_magic, ) = struct.unpack('I',infile.read(4))
        (g_maxnum, ) = struct.unpack('I',infile.read(4))
        (g_front, ) = struct.unpack('I',infile.read(4))
        (g_rear, ) = struct.unpack('I',infile.read(4))
        (g_num, ) = struct.unpack('I',infile.read(4))
        (g_data, ) = struct.unpack('I',infile.read(4))
        if g_magic==0xabcd6789:
                outfile.writelines("queue magic    :0x%x\n" % g_magic)
                outfile.writelines("maxnum     :0x%x\n" % g_maxnum)
                outfile.writelines("front     :0x%x\n" % g_front)
                outfile.writelines("rear            :0x%x\n" % g_rear)
                outfile.writelines("num               :%u\n" % g_num)
                outfile.writelines("data               :0x%x\n" % g_data)
                itemcnt = int(g_maxnum/2)
                print("got entry 0x2000001 PrintTaskSwitch dot 1, itemcnt is %d" %(itemcnt))
                outfile.writelines("pid      timestamp   gap    type\n")
                (g_flag0, ) = struct.unpack('I',infile.read(4))
                (g_timestamp0, ) = struct.unpack('I',infile.read(4))
                g_task = [g_flag0, g_timestamp0]
                g_tasklist.append(g_task)
                #find start of cycle queue
                for i in range(0, itemcnt - 1):
                    startpoint = i
                    (g_flag1, ) = struct.unpack('I',infile.read(4))
                    (g_timestamp1, ) = struct.unpack('I',infile.read(4))
                    g_task = [g_flag1, g_timestamp1]
                    if g_timestamp1 < g_timestamp0:
                        break
                    else:
                        g_tasklist.append(g_task)
                        g_timestamp0 = g_timestamp1
                #output from start point
                for i in range(startpoint + 1, itemcnt - 1):
                    (g_flag2, ) = struct.unpack('I',infile.read(4))
                    (g_timestamp2, ) = struct.unpack('I',infile.read(4))
                    #print previous item
                    if 0xAAAA == (g_flag1 >> 16):
                        task_type = "INT_IN"
                    elif  0xBBBB == (g_flag1 >> 16):
                        task_type = "INT_EXIT"
                    else:
                        task_type = "TASK"
                    if g_timestamp1 != 0:
                        outfile.writelines("0x%04x   0x%x   0x%x   %s\n" %(g_flag1 & 0xFFFF, g_timestamp1, g_timestamp2 - g_timestamp1, task_type))
                    #outfile.writelines("moving here 1\n")
                    #save current item
                    g_flag1 = g_flag2
                    g_timestamp1 = g_timestamp2

                #output current item
                if (startpoint + 1) != itemcnt - 1:
                    if 0xAAAA == (g_flag1 >> 16):
                        task_type = "INT_IN"
                    elif  0xBBBB == (g_flag1 >> 16):
                        task_type = "INT_EXIT"
                    else:
                        task_type = "TASK"
                    if g_timestamp1 != 0:
                        outfile.writelines("0x%04x   0x%x   0x%x   %s\n" %(g_flag1 & 0xFFFF, g_timestamp1, g_tasklist[0][1] - g_timestamp1, task_type))
                    #outfile.writelines("moving here 2\n")

                #output list item
                for i in range(0, len(g_tasklist) -1):
                    #outfile.writelines("0x%x   0x%x   0x%x\n" %(g_tasklist[i][0] & 0xFFFF, (g_tasklist[i][0] >> 16), g_tasklist[i][1]))
                    if 0xAAAA == (g_tasklist[i][0]  >> 16):
                        task_type = "INT_IN"
                    elif  0xBBBB == (g_tasklist[i][0]  >> 16):
                        task_type = "INT_EXIT"
                    else:
                        task_type = "TASK"
                    outfile.writelines("0x%04x   0x%x   0x%x  %s\n" %((g_tasklist[i][0] & 0xFFFF), g_tasklist[i][1], (g_tasklist[i+1][1] - g_tasklist[i][1]), task_type))

                #output last list item
                if 0xAAAA == (g_tasklist[len(g_tasklist) -1][0]  >> 16):
                    task_type = "INT_IN"
                elif  0xBBBB == (g_tasklist[len(g_tasklist) -1][0]  >> 16):
                    task_type = "INT_EXIT"
                else:
                    task_type = "TASK"
                outfile.writelines("0x%04x   0x%x   0x%x  %s\n" %((g_tasklist[len(g_tasklist) -1][0] & 0xFFFF), g_tasklist[len(g_tasklist) -1][1], 0, task_type))
                return
        print("got entry 0x2000001 PrintTaskSwitch dot 2")
        outfile.writelines('magic %u is wrong' % g_magic)
        return


def PrintTaskSwitchV2(infile, field, offset, slen, version, mode, outfile):
        MyOffset = eval(offset)
        infile.seek(MyOffset)
        g_tasklist = []
        print("got entry 0x2000001 PrintTaskSwitch")
        (g_magic, ) = struct.unpack('I',infile.read(4))
        (g_maxnum, ) = struct.unpack('I',infile.read(4))
        (g_front, ) = struct.unpack('I',infile.read(4))
        (g_rear, ) = struct.unpack('I',infile.read(4))
        (g_num, ) = struct.unpack('I',infile.read(4))
        (g_data, ) = struct.unpack('I',infile.read(4))
        if g_magic==0xabcd6789:
                outfile.writelines("queue magic    :0x%x\n" % g_magic)
                outfile.writelines("maxnum     :0x%x\n" % g_maxnum)
                outfile.writelines("front     :0x%x\n" % g_front)
                outfile.writelines("rear            :0x%x\n" % g_rear)
                outfile.writelines("num               :%u\n" % g_num)
                outfile.writelines("data               :0x%x\n" % g_data)
                itemcnt = int(g_num/2)
                print("got entry 0x2000001 PrintTaskSwitch dot 1, itemcnt is %d" %(itemcnt))
                outfile.writelines("pid     timestamp  type\n")
                (g_flag0, ) = struct.unpack('I',infile.read(4))
                (g_timestamp0, ) = struct.unpack('I',infile.read(4))
                g_task = [g_flag0, g_timestamp0]
                g_tasklist.append(g_task)
                for i in range(0, itemcnt - 1):
                    (g_flag1, ) = struct.unpack('I',infile.read(4))
                    (g_timestamp1, ) = struct.unpack('I',infile.read(4))
                    g_task = [g_flag1, g_timestamp1]
                    if g_timestamp1 < g_timestamp0:
                        outfile.writelines("0x%x   0x%x   0x%x\n" %(g_flag1 & 0xFFFF, (g_flag1 >> 16), g_timestamp1))
                    else:
                        g_tasklist.append(g_task)
                        g_timestamp0 = g_timestamp1

                for i in range(0, len(g_tasklist) -1):
                    #outfile.writelines("0x%x   0x%x   0x%x\n" %(g_tasklist[i][0] & 0xFFFF, (g_tasklist[i][0] >> 16), g_tasklist[i][1]))
                    outfile.writelines("0x%x   0x%x   0x%x  0x%x\n" %((g_tasklist[i][0] & 0xFFFF), (g_tasklist[i][0] >> 16), g_tasklist[i][1], (g_tasklist[i+1][1] - g_tasklist[i][1] )))
                outfile.writelines("0x%x   0x%x   0x%x  0x%x\n" %((g_tasklist[len(g_tasklist) -1][0] & 0xFFFF), (g_tasklist[len(g_tasklist) -1][0] >> 16), g_tasklist[len(g_tasklist) -1][1], 0))
                return
        print("got entry 0x2000001 PrintExcInfo dot 2")
        outfile.writelines('magic %u is wrong' % g_magic)
        return

def PrintTaskSwitchOld(infile, field, offset, slen, version, mode, outfile):
        MyOffset = eval(offset)
        infile.seek(MyOffset)
        print("got entry 0x2000001 PrintTaskSwitch")
        (g_magic, ) = struct.unpack('I',infile.read(4))
        (g_maxnum, ) = struct.unpack('I',infile.read(4))
        (g_front, ) = struct.unpack('I',infile.read(4))
        (g_rear, ) = struct.unpack('I',infile.read(4))
        (g_num, ) = struct.unpack('I',infile.read(4))
        (g_data, ) = struct.unpack('I',infile.read(4))
        if g_magic==0xabcd6789:
                outfile.writelines("queue magic    :0x%x\n" % g_magic)
                outfile.writelines("maxnum          :0x%x\n" % g_maxnum)
                outfile.writelines("front                :0x%x\n" % g_front)
                outfile.writelines("rear                :0x%x\n" % g_rear)
                outfile.writelines("num                :%u\n" % g_num)
                outfile.writelines("data                :0x%x\n" % g_data)
                itemcnt = int(g_num/2)
                print("got entry 0x2000001 PrintTaskSwitch dot 1, itemcnt is %d" %(itemcnt))
                outfile.writelines("pid     timestamp    type\n")
                for i in range(0, itemcnt):
                    (g_pid, ) = struct.unpack('H',infile.read(2))
                    (g_flag, ) = struct.unpack('H',infile.read(2))
                    if 0xAAAA == g_flag:
                        task_type = "INT_IN"
                    elif  0xBBBB == g_flag:
                        task_type = "INT_EXIT"
                    else:
                        task_type = "TASK"
                    (g_timestamp, ) = struct.unpack('I',infile.read(4))
                    outfile.writelines("0x%x   0x%x   %s\n" %(g_pid, g_timestamp, task_type))
                return
        print("got entry 0x2000001 PrintExcInfo dot 2")
        outfile.writelines('magic %u is wrong' % g_magic)
        return

def entry_0x800007D(infile, field, offset, slen, version, mode, outfile):
        try:
            if not field == '0x800007D':
                print('hidis field is ', field)
                print('current field is', '0x800007D')
                return error['ERR_CHECK_FIELD']
            elif not version == '0x0000':
                print('hidis version is ', version)
                print('current version is ', '0x0000')
                return error['ERR_CHECK_VERSION']
            elif not slen == '0x14000':
                print('hids len is ', slen)
                print('current len is ', '0x14000')
            print("got entry 0x800007D")
            outfile.writelines("==HAC TASKSWITCH1==\n")
            PrintTaskSwitch(infile, field, offset, slen, version, mode, outfile)
            return 0

        except Exception as e:
                print(str(e))
                outfile.writelines(str(e))
                return 1

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright © Huawei Technologies Co., Ltd. 2020-2020. All rights reserved.
description     :   analysis dms dump bin
modify  record  :   2020-04-13 create file
"""

import struct
import os
import sys
import string

MACRO_DMS_VCOM_EXT_OFF_SIZE = 2
MACRO_DMS_VCOM_EXT_ON_SIZE  = 53
MACRO_DMS_STATUS_SIZE       = 4
MACRO_DMS_VCOM_STATUS_NUM   = 12
MACRO_DMS_COM_STATUS_NUM    = 141

app_status_id_enum_table = {
     0: "DMS_APP_OPEN_ERR",
     1: "DMS_APP_REG_READY_CB_ERR",
     2: "DMS_APP_READY_CB",
     3: "DMS_APP_REG_RD_CB_ERR",
     4: "DMS_APP_RD_CB",
     5: "DMS_APP_REG_WRT_CB_ERR",
     6: "DMS_APP_WRT_CB",
     7: "DMS_APP_USER_DATA_ERR",
     8: "DMS_APP_WRT_ASYNC",
     9: "DMS_APP_WRT_ASYNC_ERR",
     10: "DMS_APP_RETURN_BUFF_ERR",
     11: "DMS_APP_RD_BUFF_ERR",

}

com_status_id_enum_table = {
     0: "DMS_ACM_REG_RD_CB_ERR",
     1: "DMS_ACM_RD_CB",
     2: "DMS_ACM_BUFF_NULL",
     3: "DMS_ACM_RD_BUFF_ERR",
     4: "DMS_ACM_RETURN_BUFF_ERR",
     5: "DMS_ACM_OPEN_ERR",
     6: "DMS_ACM_CLOSE_ERR",
     7: "DMS_ACM_REG_RELLOC_BUFF_ERR",
     8: "DMS_ACM_REG_WRT_COPY_ERR",
     9: "DMS_ACM_EVT_CB",
     10: "DMS_ACM_REG_EVT_CB_ERR",
     11: "DMS_ACM_WRT_BUFF_ERR",
     12: "DMS_ACM_WRT_CHAN_STAT_ERR",
     13: "DMS_ACM_WRT_ASYNC",
     14: "DMS_ACM_WRT_ASYNC_ERR",
     15: "DMS_ACM_WRT_DONE_SIZE_ERR",
     16: "DMS_ACM_READY_CB",
     17: "DMS_ACM_REG_READY_CB_ERR",
     18: "DMS_ACM_USER_DATA_ERR",
     19: "DMS_ACM_WRT_CB",
     20: "DMS_ACM_REG_WRT_CB_ERR",
     21: "DMS_NCM_CTRL_OPEN_ERR",
     22: "DMS_NCM_CTRL_CONN_STUS",
     23: "DMS_NCM_CTRL_CONN_STUS_ERR",
     24: "DMS_NCM_CTRL_REG_CONN_STUS_ERR",
     25: "DMS_NCM_CTRL_RD_CB",
     26: "DMS_NCM_CTRL_REG_RD_CB_ERR",
     27: "DMS_NCM_CTRL_RD_DATA_NULL",
     28: "DMS_NCM_CTRL_RD_LEN_INVALID",
     29: "DMS_NCM_CTRL_WRT_CB",
     30: "DMS_NCM_CTRL_REG_WRT_CB_ERR",
     31: "DMS_NCM_CTRL_WRT_ASYNC",
     32: "DMS_NCM_CTRL_WRT_GET_BUF_ERR",
     33: "DMS_NCM_CTRL_WRT_CHAN_STAT_ERR",
     34: "DMS_NCM_CTRL_WRT_ASYNC_ERR",
     35: "DMS_NCM_CTRL_REG_READY_CB_ERR",
     36: "DMS_NCM_CTRL_READY_CB",
     37: "DMS_NCM_CTRL_USER_DATA_ERR",
     38: "DMS_NCM_CTRL_RETURN_BUFF_ERR",
     39: "DMS_NCM_CTRL_CLOSE_ERR",
     40: "DMS_NCM_DATA_OPEN_ERR",
     41: "DMS_NCM_DATA_SET_IPV6_ERR",
     42: "DMS_NCM_DATA_FLOW_CTRL_ERR",
     43: "DMS_NCM_DATA_CONN_SPEED_ERR",
     44: "DMS_NCM_DATA_CONN_NTF_ERR",
     45: "DMS_NCM_DATA_CLOSE_ERR",
     46: "DMS_MDM_OPEN_ERR",
     47: "DMS_MDM_RD_CB",
     48: "DMS_MDM_REG_RD_CB_ERR",
     49: "DMS_MDM_RD_ADDR_INVALID",
     50: "DMS_MDM_RD_BUFF_ERR",
     51: "DMS_MDM_FREE_CB",
     52: "DMS_MDM_FREE_CB_PPP",
     53: "DMS_MDM_FREE_CB_AT",
     54: "DMS_MDM_REG_FREE_CB_ERR",
     55: "DMS_MDM_REG_WRT_COPY_ERR",
     56: "DMS_MDM_RD_MSC",
     57: "DMS_MDM_RD_MSC_NULL",
     58: "DMS_MDM_REG_RD_MSC_ERR",
     59: "DMS_MDM_WRT_MSC",
     60: "DMS_MDM_WRT_MSC_ERR",
     61: "DMS_MDM_REG_RELLOC_BUFF_ERR",
     62: "DMS_MDM_REG_READY_CB_ERR",
     63: "DMS_MDM_READY_CB",
     64: "DMS_MDM_USER_DATA_ERR",
     65: "DMS_MDM_RETURN_BUFF_ERR",
     66: "DMS_MDM_WRT_ASYNC",
     67: "DMS_MDM_WRT_BUFF_ERR",
     68: "DMS_MDM_WRT_ASYNC_ERR",
     69: "DMS_MDM_CLOSE_ERR",
     70: "DMS_UART_REG_RD_CB_ERR",
     71: "DMS_UART_RD_CB",
     72: "DMS_UART_RD_ADDR_INVALID",
     73: "DMS_UART_RD_BUFF_ERR",
     74: "DMS_UART_OPEN_ERR",
     75: "DMS_UART_REG_READY_CB_ERR",
     76: "DMS_UART_READY_CB",
     77: "DMS_UART_USER_DATA_ERR",
     78: "DMS_UART_RETURN_BUFF_ERR",
     79: "DMS_UART_WRT_SYNC",
     80: "DMS_UART_WRT_SYNC_ERR",
     81: "DMS_UART_SET_BAUD_ERR",
     82: "DMS_HSUART_REG_RD_CB_ERR",
     83: "DMS_HSUART_RD_CB",
     84: "DMS_HSUART_RD_ADDR_INVALID",
     85: "DMS_HSUART_RD_BUFF_ERR",
     86: "DMS_HSUART_WRT_ASYNC",
     87: "DMS_HSUART_WRT_ASYNC_ERR",
     88: "DMS_HSUART_ALLOC_BUF_ERR",
     89: "DMS_HSUART_OPEN_ERR",
     90: "DMS_HSUART_REG_RELLOC_BUFF_ERR",
     91: "DMS_HSUART_FREE_CB",
     92: "DMS_HSUART_REG_FREE_CB_ERR",
     93: "DMS_HSUART_SWITCH_MODE",
     94: "DMS_HSUART_REG_SWITCH_MODE_ERR",
     95: "DMS_HSUART_WATER_CB",
     96: "DMS_HSUART_WATER_LEVEL_ERR",
     97: "DMS_HSUART_REG_WATER_CB_ERR",
     98: "DMS_HSUART_RD_MSC",
     99: "DMS_HSUART_RD_MSC_NULL",
     100: "DMS_HSUART_REG_RD_MSC_ERR",
     101: "DMS_HSUART_WRT_MSC_ERR",
     102: "DMS_HSUART_REG_READY_CB_ERR",
     103: "DMS_HSUART_READY_CB",
     104: "DMS_HSUART_USER_DATA_ERR",
     105: "DMS_HSUART_RETURN_BUFF_ERR",
     106: "DMS_HSUART_FLOW_CONTRL_ERR",
     107: "DMS_HSUART_SET_WLEN_ERR",
     108: "DMS_HSUART_SET_STP_ERR",
     109: "DMS_HSUART_SET_EPS_ERR",
     110: "DMS_HSUART_SET_BAUD_ERR",
     111: "DMS_HSUART_SET_ACSHELL_ERR",
     112: "DMS_HSUART_FLUSH_BUFF_ERR",
     113: "DMS_SOCK_RD_CB",
     114: "DMS_SOCK_RD_DATA_NULL",
     115: "DMS_SOCK_RD_LEN_INVALID",
     116: "DMS_SOCK_BSP_SUPPORT_ERR",
     117: "DMS_SOCK_OPEN_ERR",
     118: "DMS_SOCK_REG_RD_CB_ERR",
     119: "DMS_SOCK_REG_WRT_CB_ERR",
     120: "DMS_SOCK_WRT_CB",
     121: "DMS_SOCK_REG_READY_CB_ERR",
     122: "DMS_SOCK_READY_CB",
     123: "DMS_SOCK_USER_DATA_ERR",
     124: "DMS_SOCK_RETURN_BUFF_ERR",
     125: "DMS_SOCK_WRT_ASYNC",
     126: "DMS_SOCK_WRT_ASYNC_ERR",
     127: "DMS_CMUX_OPEN_ERR",
     128: "DMS_CMUX_REG_RD_CB_ERR",
     129: "DMS_CMUX_REG_FREE_CB_ERR",
     130: "DMS_CMUX_REG_CLOSE_CB_ERR",
     131: "DMS_CMUX_ALLOC_BUF_ERR",
     132: "DMS_CMUX_WRT_ASYNC",
     133: "DMS_CMUX_WRT_ASYNC_ERR",
     134: "DMS_CMUX_REG_SNC_CB_ERR",
     135: "DMS_CMUX_CLOSE_UART_ERR",
     136: "DMS_CMUX_SET_MSC_READ_CB",
     137: "DMS_CMUX_SET_MSC_READ_CB_NULL",
     138: "DMS_CMUX_SET_MSC_READ_CB_ERR",
     139: "DMS_CMUX_WRT_MSC_ERR",
     140: "DMS_CMUX_FREE_CB",
}

def get_mntn_status_id_str(ulStatusId, ulVcomFlag):
    status_id_enum_table = com_status_id_enum_table

    if (ulVcomFlag == 1):
        status_id_enum_table = app_status_id_enum_table

    for statusIndex in status_id_enum_table.keys():
        if statusIndex == ulStatusId:
            return status_id_enum_table[statusIndex]


def analysis_at_mntn_port_status_info(ulStatusId, instream, fileLocalOffset, ulVcomFlag, outstream):
        instream.seek(fileLocalOffset)

        strStatusName   = get_mntn_status_id_str(ulStatusId, ulVcomFlag)
        (ulStatsCount,) = struct.unpack('I', instream.read(4))

        outstream.writelines(["%-20d%-40s%-20d\n" % (ulStatusId, strStatusName, ulStatsCount)])

def analysis_at_mntn_dms_status_info(ulVcomPortNum, instream, fileLocalOffset, outstream):
        instream.seek(fileLocalOffset)

        outstream.writelines(["\n************ APP STATUS INFO begin!************\n"])
        outstream.writelines(["%-20s%-20s%-40s%-20s\n" % ("appIdx", "statusId","statusName", "statsCount")])
        for ulVcomPortIdx in range(ulVcomPortNum):
            for ulVcomStatusIdx in range(MACRO_DMS_VCOM_STATUS_NUM):
                outstream.writelines(["%-20d" % (ulVcomPortIdx)])
                analysis_at_mntn_port_status_info(ulVcomStatusIdx, instream, fileLocalOffset, 1, outstream)
                fileLocalOffset = fileLocalOffset + MACRO_DMS_STATUS_SIZE

        outstream.writelines(["\n************ APP STATUS INFO end!************\n"])

        outstream.writelines(["\n************ COM STATUS INFO begin!************\n"])
        outstream.writelines(["%-20s%-40s%-20s\n" % ("statusId","statusName", "statsCount")])
        for ulComStatusIdx in range(MACRO_DMS_COM_STATUS_NUM):
            analysis_at_mntn_port_status_info(ulComStatusIdx, instream, fileLocalOffset, 0, outstream)
            fileLocalOffset = fileLocalOffset + MACRO_DMS_STATUS_SIZE

        outstream.writelines(["\n************ COM STATUS INFO end!************\n"])

def analysis_dms_mntn_dump_info( instream, fileOffset, outstream):
        ulVcomPortNum      = MACRO_DMS_VCOM_EXT_OFF_SIZE

        #offset add index len and reserv len

        fileLocalOffset = fileOffset

        instream.seek(fileLocalOffset)
        (ulVersion,)  = struct.unpack('I', instream.read(4))
        (ulVcomExtFlag,)  = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-20s%-20s\n" % ("version", "vcomExtFlag")])
        outstream.writelines(["%-20d%-20d\n" % (ulVersion, ulVcomExtFlag)])

        if (ulVcomExtFlag == 1):
            ulVcomPortNum = MACRO_DMS_VCOM_EXT_ON_SIZE

        fileLocalOffset = fileLocalOffset + 8
        analysis_at_mntn_dms_status_info(ulVcomPortNum, instream, fileLocalOffset, outstream)

def analysis_dms_dump_info( infile, offset, outfile):
        instream = infile
        outstream  = outfile
        fileOffset = eval(offset)

        ulbeginTick     = 0
        ulEndTick       = 0

        outstream.writelines(["\n**************************** analysis_dms_dump_info begin!*******************************\n"])
        global GLOBAL_Offset

        instream.seek(fileOffset)
        (ulBeginTick,)       = struct.unpack('I', instream.read(4))
        strBeginTick         = '%x'% ulBeginTick
        print ("DMS DUMP Begin tag is %s" % (strBeginTick))

        #在0xaa55aa55之后有4字节的reserve位，所以偏移需要加8
        fileOffset = fileOffset + 8

#       Old Version begin is 0xaa55aa55
        global Global_Version
        if ulBeginTick == 2857740885:
            Global_Version = 0x01
            analysis_dms_mntn_dump_info(instream, fileOffset, outstream)

        #2857740885 = 0xaa55aa55 find end tick
        while ulEndTick != 2857740885:
                (ulEndTick,) = struct.unpack('I', instream.read(4))

        strEndTick         = '%x'% ulEndTick
        print ("DMS DUMP End tag is %s" % (strEndTick))


        outstream.writelines(["\n**************************** analysis_dms_dump_info end!*******************************\n"])

        return True

########################################################################################
def entry_0x1200004(infile, field, offset, len, version, mode, outfile):
        ########check parameter start#############
        if not field == '0x1200004':
            print ("hidis field is %s" % (field))
            print ("current field is 0x1200004")
            return error['ERR_CHECK_FIELD']
        elif not version == '0x0000':
            print ("hidis version is %s" % (version))
            print ("current version is 0x0000")
            return error['ERR_CHECK_VERSION']
        #########check parameter end##############
        ret = analysis_dms_dump_info( infile, offset, outfile)

        #c = msvcrt.getch()
        return 0


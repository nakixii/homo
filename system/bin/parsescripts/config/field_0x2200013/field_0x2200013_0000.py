# coding=utf-8
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import struct

from config import error


def printDumpInfo(infile, offset, slen, outfile):
    row = 0
    MyOffset = eval(offset)
    infile.seek(MyOffset)
    outfile.writelines("============print dump info============\n")
    outfile.writelines("offset      0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f \n")
    for i in range(0, int(int(slen, 16) / 16)):
        (charbyte1, charbyte2, charbyte3, charbyte4,) = struct.unpack("BBBB", infile.read(4))
        (charbyte5, charbyte6, charbyte7, charbyte8,) = struct.unpack("BBBB", infile.read(4))
        (charbyte9, charbyte10, charbyte11, charbyte12,) = struct.unpack("BBBB", infile.read(4))
        (charbyte13, charbyte14, charbyte15, charbyte16,) = struct.unpack("BBBB", infile.read(4))
        addr = 0x10 * row
        row = row + 1
        outfile.writelines("0x%08x: %02x %02x %02x %02x " % (addr, charbyte1, charbyte2, charbyte3, charbyte4))
        outfile.writelines("%02x %02x %02x %02x " % (charbyte5, charbyte6, charbyte7, charbyte8))
        outfile.writelines("%02x %02x %02x %02x " % (charbyte9, charbyte10, charbyte11, charbyte12))
        outfile.writelines("%02x %02x %02x %02x\n" % (charbyte13, charbyte14, charbyte15, charbyte16))
    return


def parseTranceInfo(fileFirstId, printNum, infile, outfile):
    for i in range(0, printNum):
        (fileNameId, lineNum,) = struct.unpack("II", infile.read(8))
        index = fileNameId - fileFirstId
        if (index >= 0 and index < len(fileNames)):
            fileName = fileNames[index]
        else:
            fileName = str(fileNameId)
        if lineNum >= 0x80000000:
            outfile.writelines("(%04d)%-30s(out)   %d\n" % (fileNameId, fileName, lineNum - 0x80000000))
        elif lineNum >= 0x10000000:
            outfile.writelines("(%04d)%-30s(in)    %d\n" % (fileNameId, fileName, lineNum - 0x10000000))
        else:
            outfile.writelines("(%04d)%-30s        %d\n" % (fileNameId, fileName, lineNum))


def parseBastetDump(infile, field, offset, slen, version, mode, outfile):
    MyOffset = eval(offset)
    infile.seek(MyOffset)
    # 检查magicNum 确定内存是否被踩
    (magicStart,) = struct.unpack("I", infile.read(4))
    infile.seek(MyOffset + 2044)
    (magicEnd,) = struct.unpack("I", infile.read(4))
    if not (magicStart == 0xB3B2B1B0 and magicEnd == 0xEBEAE9E9):
        outfile.writelines("============BASTET magicNum wrong============\n")
        printDumpInfo(infile, offset, slen, outfile)
        return
    # 开始解析
    infile.seek(MyOffset + 4)
    (logIndex, fileFirstId) = struct.unpack("II", infile.read(8))
    outfile.writelines("logIndex is %d\n" % (logIndex,))
    logIndex = logIndex + 1
    infile.read(4)
    # 解析TranceInfo
    outfile.writelines("fileName:                                   LineNum:\n")
    tranceStart = MyOffset + 16
    tranceMind = tranceStart + logIndex * 8
    tranceEnd = tranceStart + 128 * 8
    infile.seek(tranceMind)
    parseTranceInfo(fileFirstId, 128 - logIndex, infile, outfile)
    infile.seek(tranceStart)
    parseTranceInfo(fileFirstId, logIndex, infile, outfile)
    infile.seek(tranceEnd)
    # 解析magicInfo确认能够解析正确
    (magicinfo,) = struct.unpack("I", infile.read(4))
    if not magicinfo == 0xD7D6D5D4:
        outfile.writelines("============parse fail============\n")
        printDumpInfo(infile, offset, slen, outfile)
        return
    infile.read(4)
    # 开始解析C++对象信息
    outfile.writelines("============Object Info============\n")
    (objSiz, objAddr,) = struct.unpack("II", infile.read(8))
    outfile.writelines("objSize: %d  objAddr: %08x\n" % (objSiz, objAddr))
    printDumpInfo(infile, str(tranceEnd + 16), "0x80", outfile)
    # 保留位 860byte
    infile.read(860)
    # 再次解析magicEnd 确认解析成功
    (check,) = struct.unpack("I", infile.read(4))
    if not check == magicEnd:
        outfile.writelines("============parse fail============\n")
        printDumpInfo(infile, offset, slen, outfile)
        return
    outfile.writelines("============prase dump succ============\n")
    return


def entry_0x2200013(infile, field, offset, slen, version, mode, outfile, field_list=None):
    try:
        if not field == '0x2200013':
            print('hidis field is ', field)
            print('current field is', '0x2200013')
            return error['ERR_CHECK_FIELD']
        elif not version == '0x0000':
            print('hidis version is ', version)
            print('current version is ', '0x0000')
            return error['ERR_CHECK_VERSION']
        elif not slen == '0x800':
            print('hids len is ', slen)
            print('current len is ', '0x800')
            return error['ERR_CHECK_LEN']
        print("got entry 0x2200013")
        parseBastetDump(infile, field, offset, slen, version, mode, outfile)
        return error['ERR_SUCCESS']

    except Exception as e:
        print(str(e))
        outfile.writelines(str(e))
        return error['ERR_NO_FIELD_SCRIPTS']


fileNames = ["BST_SRV_TASKMNG_CPP",
             "BST_SRV_EVENT_CPP",
             "BST_SRV_ASEVNT_CPP",
             "BST_SRV_ASCTRL_CPP",
             "BST_SRV_CHNL_CTRL_CPP",
             "BST_PLATFORM_C",
             "BST_PAL_TIMER_C",
             "BST_PAL_THREAD_C",
             "BST_PAL_SYNC_C",
             "BST_PAL_NET_C",
             "BST_PAL_MEMORY_C",
             "BST_PAL_AS_C",
             "BST_PAL_ACOM_C",
             "BST_PAL_LINK_STA_C",
             "BST_OS_TIMER_CPP",
             "BST_OS_THREAD_C",
             "BST_OS_SYNC_C",
             "BST_OS_MEMORY_C",
             "BST_OS_LOG_C",
             "BST_DRV_NET_C",
             "BST_DRV_AS_C",
             "BST_DRV_ACOM_C",
             "BST_DRV_LINKSTA_C",
             "BST_DRV_CSFIREWALL_C",
             "BST_DRV_ASPEN_C",
             "BST_IP_SOCKETCLONE_C",
             "BST_IP_PREPROC_C",
             "BST_IP_SOCKET_CPP",
             "BST_IP_RCVERMNG_CPP",
             "BST_IP_LWIPAPI_CPP",
             "BST_DSPP_TRSLAYER_CPP",
             "BST_DSPP_REPORT_CPP",
             "BST_DSPP_LAYERPROCBASE_CPP",
             "BST_DSPP_CTRLAYER_CPP",
             "BST_DSPP_APPLAYER_CPP",
             "BST_LIB_STRINT8U_CPP",
             "BST_LIB_STRINGCHECK_CPP",
             "BST_LIB_SN_GENERATE_H",
             "BST_CORE_TASK_CPP",
             "BST_CORE_SCHD_CPP",
             "BST_CORE_PTASK_CPP",
             "BST_CORE_NPTASK_CPP",
             "BST_CORE_REGISTRYTBLMNG_CPP",
             "BST_CORE_REGEDIT_CPP",
             "BST_APP_HEARTBEAT_CPP",
             "BST_APP_EMAILPOP3_CPP",
             "BST_APP_EMAILIMAP_CPP",
             "BST_APP_EMAILEXCHANGE_CPP",
             "BST_APP_EMAILEXCGHTTP_CPP",
             "BST_APP_EMAILBASEPROC_CPP",
             "BST_APP_MAINTASK_CPP",
             "BST_LWIP_SYS_ARCH_C",
             "BST_LWIP_PBUF_C",
             "BST_PAL_FILE_C",
             "BST_PAL_LIST_LIB_C",
             "BST_MSGPROC_C",
             "CDS_BST_PROC_C",
             "BST_SYSMNTN_C",
             "BST_COMM_C",
             "BST_INIT_C",
             "BST_OS_OPENSSL_MEM_C",
             "BST_PAL_OPENSSL_GETSERVBY_C",
             "BST_PAL_OPENSSL_FILE_C",
             "BST_PAL_LOG_C",
             "BST_PAL_EMCOM_C",
             "MN_BASTET_C",
             "BST_SRV_HB_DETECTOR_CPP",]

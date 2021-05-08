#!/usr/bin/env python3
# coding=utf-8
#***********************************************************************
# * Copyright     Copyright(c) 2016 - 2019 Hisilicon Technoligies Co., Ltd.
# * Filename      field_0x2200011_0000.py
# * Description   analysis cttf dump bin
# * Version       1.0
# * Data          2016-07-07 create file
#***********************************************************************
import struct
from CTTF_HrpdMacParse import CTTF_HRPD_MAC_ParseDumpInfo
from CTTF_1xMacParse import CTTF_1X_MAC_ParseDumpInfo
from CTTF_1xLacParse import CTTF_1X_LAC_ParseDumpInfo
from CTTF_1xRlpParse import CTTF_1X_RLP_ParseDumpInfo
from GTTF_Parse import GTTF_ParseDumpInfo

AS_COMM_DUMP_USER_ENUM = {
    'AS_COMM_DUMP_USER_HRPD_MAC' : 3,
    'AS_COMM_DUMP_USER_1X_MAC' : 4,
    'AS_COMM_DUMP_USER_1X_LAC' : 5,
    'AS_COMM_DUMP_USER_1X_RLP' : 6,
	'AS_COMM_DUMP_USER_GTTF_I0' : 7,
	'AS_COMM_DUMP_USER_GTTF_I1' : 8,
	'AS_COMM_DUMP_USER_GTTF_I2' : 9
}


def CTTF_ParseDumpInfo(infile, outfile):
    ##################################################################################
    #   CTTF Dump文件结构:
    #   AS_COMM_DUMP_USER_ENUM_UINT8        enUserId
    #   VOS_UINT8                           ucReserved
    #   VOS_UINT16                          usDataLen
    ##################################################################################
    enUserId, _, usDataLen = struct.unpack('2BH', infile.read(4))

    if 0 == usDataLen:
        return False
    if enUserId == AS_COMM_DUMP_USER_ENUM['AS_COMM_DUMP_USER_HRPD_MAC']:
        CTTF_HRPD_MAC_ParseDumpInfo(infile, outfile, usDataLen)
    elif enUserId == AS_COMM_DUMP_USER_ENUM['AS_COMM_DUMP_USER_1X_MAC']:
        CTTF_1X_MAC_ParseDumpInfo(infile, outfile, usDataLen)
    elif enUserId == AS_COMM_DUMP_USER_ENUM['AS_COMM_DUMP_USER_1X_LAC']:
        CTTF_1X_LAC_ParseDumpInfo(infile, outfile, usDataLen)
    elif enUserId == AS_COMM_DUMP_USER_ENUM['AS_COMM_DUMP_USER_1X_RLP']:
        CTTF_1X_RLP_ParseDumpInfo(infile, outfile, usDataLen)
    elif enUserId == AS_COMM_DUMP_USER_ENUM['AS_COMM_DUMP_USER_GTTF_I0']:
        GTTF_ParseDumpInfo(infile, outfile, usDataLen)
    elif enUserId == AS_COMM_DUMP_USER_ENUM['AS_COMM_DUMP_USER_GTTF_I1']:
        GTTF_ParseDumpInfo(infile, outfile, usDataLen)
    elif enUserId == AS_COMM_DUMP_USER_ENUM['AS_COMM_DUMP_USER_GTTF_I2']:
        GTTF_ParseDumpInfo(infile, outfile, usDataLen)
    else:
        outfile.write('err user id %d\n' % enUserId)
        return False  
    return True

def entry_0x220000B(infile, field, offset, len, version, mode, outfile):
    if not field == '0x220000B':
        print('hidis field is ', field)
        print('current field is', '0x220000B')
        return error['ERR_CHECK_FIELD']
    elif not version == '0x0000':
        print('hidis version is ', version)
        print('current version is ', '0x0000')
        return error['ERR_CHECK_VERSION']
    elif not len == '0x2000':
        print('hids len is ', len)
        print('current len is ', '0x2000')
        return error['ERR_CHECK_LEN']
    outfile.write('CTTF DUMP INFO\n')
    infile.seek(int(offset, 16))
    while True:
        if not CTTF_ParseDumpInfo(infile, outfile):
            break
    return 0

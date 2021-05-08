#######################################################################################################################################
#   filename        :   field_0x220000C_0000.py
#
#
#   description     :   config for exparse python sripts frame
#
#   modify  record  :   2014-07-21 create file
#
#######################################################################################################################################
import struct
import os
import sys
import string
from config import *
#reload(sys)
#sys.setdefaultencoding('utf8')

d       = {'A4':'SELECT',
          'F2':'STATUS',
          'B0':'READ BINARY',
          'D6':'UPDATE BINARY',
          'B2':'READ RECORD',
          'DC':'UPDATE RECORD',
          'A2':'SEARCH RECORD',
          '32':'INCREASE',
          '20':'VERIFY PIN',
          '24':'CHANGE PIN',
          '26':'DISABLE PIN',
          '28':'ENABLE PIN',
          '2C':'UNBLOCK PIN',
          '04':'DEACTIVE FILE',
          '44':'ACTIVE FILE',
          '88':'AUTHENTICATE',
          '70':'MANAGE CHANNEL',
          '84':'GET CHALLENGE',
          '10':'TERMINAL PROFILE',
          'C2':'ENVELOPE',
          '12':'FETCH',
          '14':'TERMINAL RESPONSE',
          'C0':'GET RESPONSE'}

def ReplaceKey(key):
    for k in d:
        if (k == key):
            return d[k]

    return 'unkown'

def exc_100000CD(infile,offset,outfile):
    print_key = 0
    str_len = (8192 - 2) #前两个字节记录的是起始位置
    infile.seek(int(offset, 16)+2)

    temp =''
    print_value=""
    for i in range(0, str_len,1):
        (tag, ) = struct.unpack('B',infile.read(1))
        temp = '%02X' % tag

        if ("5A" == temp):
            temp = "\r\n  "
        else:
            temp = temp + " "

        print_value = print_value + temp

    list_m = print_value.split("\r\n")
    print_value = ""
    for m in list_m:
        if (0 == len(m)):
            continue

        if (5 == len(m)):
            print_value = print_value + m +  "                                  <"+ ReplaceKey(m[2:4]) +'>\r\n'
        else:
            print_value = print_value + m +  '\r\n'

    outfile.write(print_value)

def entry_0x220000C(infile, field, offset, len, version, mode, outfile, field_list = None):
    try:
        if not field == '0x220000C':
            print('hidis field is ', field)
            print('current field is', '0x220000C')
            return error['ERR_CHECK_FIELD']
        elif not version == '0x0000':
            print('hidis version is ', version)
            print('current version is ', '0x0000')
            return error['ERR_CHECK_VERSION']
        elif not len == '0x2000':
            print('hids len is ', len)
            print('current len is ', '0x2000')
            return error['ERR_CHECK_LEN']
        outfile.write('***USIM I0 inteactive message***\r\n')
        exc_100000CD(infile,offset,outfile)

        return 0

    except Exception as e:
        outfile.write(str(e))
        return 0
    return 0


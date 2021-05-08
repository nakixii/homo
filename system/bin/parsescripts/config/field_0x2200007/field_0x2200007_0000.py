#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   analysis cproc dump bin
modify  record  :   2016-03-10 create file
"""

import struct
import os
import sys
import string
from version_0000 import *
from version_0100 import *
from version_0102 import *

FIELD_VERSION_MAGIC = 0xCECE0000

def entry_0x2200007(infile, field, offset, len, version, mode, outfile):
        instream   = infile
        outstream  = outfile
		
        ########check parameter start#############
        if not field == '0x2200007':
            print ("hidis field is %s." % (field) ) 
            print ("current field is 0x2200007.")
            return error['ERR_CHECK_FIELD']
        elif not version == '0x0000':
            print ("hidis version is %s." % (version) )
            print ("current version is 0x0000.")
            return error['ERR_CHECK_VERSION']
        elif not len == '0x2000':
            print ("hids len is %s." % (len) )
            print ("current len is 0x2000." )
            return error['ERR_CHECK_LEN']
        
        fileOffset = eval(offset)
        instream.seek(fileOffset) 
        (ulFieldVersion,)  = struct.unpack('I', instream.read(4))
        ulVersion = ulFieldVersion & 0xffff
        ulVersionMagic = ulFieldVersion & 0xffff0000
        
        if ( ulVersionMagic == FIELD_VERSION_MAGIC ):
            fileOffset = eval(offset) + 4
            #outfile.writelines(["Field version: %d.%d\n\n" % (ulVersion>>8, ulVersion&0xff)])
            #save2file.writelines(["Field version: %d.%d\n\n" % (ulVersion>>8, ulVersion&0xff)])
            
            if (ulVersion == 0x0100): #DallasC30_ChicagoC10_main
                ret = analysis_cproc_dump_info_0100(infile, fileOffset, outfile, ulVersion)
            elif (ulVersion == 0x0101): #DallasC50_ChicagoC20_main
                ret = analysis_cproc_dump_info_0100(infile, fileOffset, outfile, ulVersion)
            elif (ulVersion == 0x0102): #DallasC50_ChicagoC20_main
                ret = analysis_cproc_dump_info_0102(infile, fileOffset, outfile, ulVersion)
            elif (ulVersion == 0x0103): #DallasC30_ChicagoC10_main
                ret = analysis_cproc_dump_info_0102(infile, fileOffset, outfile, ulVersion)
            else :
                #print 'current version is ', ulVersion
                outfile.writelines(["Field version: %d.%d\n\n" % (ulVersion>>8, ulVersion&0xff)])
            
        else:
            ret = analysis_cproc_dump_info_0000(infile, fileOffset, outfile, 0x0000)

        return 0

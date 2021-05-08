#!/usr/bin/env python3
# coding=utf-8
# Copyright (C) Huawei Technologies Co., Ltd. 2010-2018. All rights reserved.

import os
import os.path
import sys
import struct
import config
import entry_mntn

class rdr_exc:
    def __init__(self,magic):
        self.modid=0
        self.arg1=0
        self.arg2=0
        self.e_core=0
        self.e_type=0
        self.start_flag=0
        self.savefile_flag=0
        self.reboot_flag=0
        self.e_module=''
        self.e_desc=''
        self.timestamp=0
        self.datetime=''
        self.magic = magic
        return
    
    def parse(self,in_handler,offset):
        in_handler.seek(offset)
        self.modid,=struct.unpack("I", in_handler.read(4))
        self.arg1,=struct.unpack("I", in_handler.read(4))
        self.arg2,=struct.unpack("I", in_handler.read(4))
        self.e_core,=struct.unpack("I", in_handler.read(4))
        self.e_type,=struct.unpack("I", in_handler.read(4))
        self.start_flag,=struct.unpack("I", in_handler.read(4))
        self.savefile_flag,=struct.unpack("I", in_handler.read(4))
        self.reboot_flag,=struct.unpack("I", in_handler.read(4))
        self.e_module=in_handler.read(16)
        self.e_desc=in_handler.read(48)
        if 0x4E524D53 == self.magic:
            self.timestamp=struct.unpack("I", in_handler.read(4))
        self.datetime=in_handler.read(24)
        return
    
    def output_result(self,outfile):
        #enter soft exc proc
        if self.start_flag==0x5A5A2222:
            outfile.writelines("[exc info]\n")
            outfile.writelines("Exc core                :0x%x\n" % self.e_core)
            outfile.writelines("Exc type                :0x%x\n" % self.e_type)
            outfile.writelines("Exc module              :%s\n" % self.e_module.decode(encoding="utf-8").strip('\x00'))
            outfile.writelines("Exc description         :%s\n" % self.e_desc.decode(encoding="utf-8").strip('\x00'))
            outfile.writelines("Exc datetime            :%s\n" % self.datetime.decode(encoding="utf-8").strip('\x00'))
            outfile.writelines("Exc mode id             :0x%x\n" % self.modid)
            outfile.writelines("Exc arg1                :0x%x\n" % self.arg1)
            outfile.writelines("Exc arg2                :0x%x\n" % self.arg2)
            if 0x4E524D53 == self.magic:
                outfile.writelines("timestamp                :0x%x\n" % self.timestamp)
            outfile.writelines("[end]\n")
            return
        #no exc proc,soft reboot
        if self.reboot_flag==0x5a5a1111:
            outfile.writelines("###################################\n")
            outfile.writelines("        Normal soft reboot         \n")
            outfile.writelines("###################################\n")
            return
            
        #other boot type
        outfile.writelines("###################################\n")
        outfile.writelines("Normal boot   :%s\n" % config.get_exc_tyep(self.e_type))
        outfile.writelines("###################################\n")

class rdr_base:
    def __init__(self):
        self.magic=0
        self.version=0
        self.area_number=0
        self.reserve=0
        self.build_time=''
        self.product_name=''
        self.product_version=''
        self.uuid=''
        self.nrccpu_aslr=0
        self.lrccpu_aslr=0
        self.aslr_magic=0
        return
    def parse(self,in_handler,offset):
        in_handler.seek(offset)
        self.magic,= struct.unpack("I", in_handler.read(4))
        self.version,=struct.unpack("I", in_handler.read(4))
        self.area_number,=struct.unpack("I", in_handler.read(4))
        self.reserve,=struct.unpack("I", in_handler.read(4))
        self.build_time=in_handler.read(32)
        self.build_time=self.build_time
        self.product_name=in_handler.read(32)
        self.product_version=in_handler.read(32)
        if 0x4E524D53 == self.magic:
            self.uuid=in_handler.read(40)
        off_tmp = in_handler.seek(-12, 2)
        print(off_tmp)
        self.nrccpu_aslr, = struct.unpack("I", in_handler.read(4))
        self.lrccpu_aslr, = struct.unpack("I", in_handler.read(4))
        self.aslr_magic, = struct.unpack("I", in_handler.read(4))
        return
    
    def output_result(self,outfile):        
        outfile.writelines("[product info]\n")
        print(self.product_name)
        print(self.product_version)
        outfile.writelines("product name        :%s\n" % self.product_name.decode(encoding="utf-8").strip('\x00'))
        outfile.writelines("product version     :%s\n" % self.product_version.decode(encoding="utf-8").strip('\x00'))
        outfile.writelines("build time          :%s\n" % self.build_time.decode(encoding="utf-8").strip('\x00'))
        outfile.writelines("area number         :%d\n" % self.area_number)
        outfile.writelines("version             :%d\n" % self.version)
        if 0x4E524D53 == self.magic:
            outfile.writelines("uuid             :%s\n" % self.uuid.decode(encoding="utf-8").strip('\x00').replace('\x00',''))
        outfile.writelines("nrccpu_aslr             :0x%x\n" % self.nrccpu_aslr)
        outfile.writelines("lrccpu_aslr             :0x%x\n" % self.lrccpu_aslr)
        outfile.writelines("aslr_magic             :0x%x\n" % self.aslr_magic)
        outfile.writelines("[end]\n")
        return

class head_base:
    def __init__(self):
        self.magic = 0
        self.rdroff = 0
        self.excoff = 0
        self.area_offset = 0
    def resetbymagic(self,magic):
        self.magic = magic
        if 0x44656164 == magic:
            self.rdroff = 0
            self.excoff = 112
            self.area_offset = 232
            return True
        elif 0x4E524D53 == magic:
            self.rdroff = 0
            self.excoff = 152
            self.area_offset = 276
            return True
        self.magic = 0
        return False;

def entry_modem_dump_parser(infile, outfile):
    
    if not os.path.exists(infile):
        print(("%s is not exist!!!"%(infile)))
        return 1
    
    #parse result file
    with open(outfile,"w+") as out_handler:
        print(( "open outfile %s OK\n" %(outfile)))
        with open(infile,"rb") as in_handler:
            print(("open infile %s OK\n"%(infile)))
    
            head = head_base()

            magic,=struct.unpack("I", in_handler.read(4))
            if False == head.resetbymagic(magic):
                print ("magic num is err,please use hids to parse!")
                return 4
        
            base=rdr_base()
            base.parse(in_handler,head.rdroff)
            base.output_result(out_handler)

            exc=rdr_exc(magic)
            exc.parse(in_handler,head.excoff)
            exc.output_result(out_handler)
    
            try:
                ret = entry_mntn.entry(0, head.area_offset,in_handler,out_handler,base.version)
                if ret == None:
                    print('rdr_parse is ok\n')
                return 0
            except IOError as e:
                print ("rdr parse fail:", e)
                return 5

    return 6

def entry_modem_dump_parser_link(in_handler, outfile, offset, filelength):

    #parse result file
    with open(outfile,"w+") as out_handler:
        print(( "open outfile %s OK\n" %(outfile)))
        print("fileoffset")
        print(offset)

        in_handler.seek(offset)
        curpos = in_handler.tell()
        print(curpos)
        head = head_base()

        magic,=struct.unpack("I", in_handler.read(4))
        print(magic)
        if False == head.resetbymagic(magic):
            print ("magic num is err,please use hids to parse!")
            return 4

        base=rdr_base()
        base.parse(in_handler, offset +head.rdroff)
        base.output_result(out_handler)

        exc=rdr_exc(magic)
        exc.parse(in_handler, offset +head.excoff)
        exc.output_result(out_handler)
    
        try:
            ret = entry_mntn.entry(offset, head.area_offset,in_handler,out_handler,base.version)
            if ret == None:
                print('rdr_parse is ok\n')
            return 0
        except IOError as e:
            print ("rdr parse fail:", e)
            return 5

    return 6


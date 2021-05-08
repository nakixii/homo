#!/usr/bin/env python3
# coding=utf-8
# Copyright (C) Huawei Technologies Co., Ltd. 2010-2018. All rights reserved.

import os
import sys
import string
import struct
import config
#from config import *


def cur_file_dir():
    return os.path.split(os.path.realpath(__file__))[0]

class entry_parse:
    def __init__(self):
        self.python_file = ''
        self.file_dir = ''
        self.params_dict = {}
        return

    def append_dump_scrits(self):
        #define config file
        path = sys.path[0]
        if os.path.isdir(path):
            top_dir = path
        elif os.path.isfile(path):
            top_dir = os.path.dirname(path)
        sys.path.append(top_dir)
        file_path = '%s%s%s' %(top_dir, '/config/field_', str(self.params_dict['field']))
        sys.path.append(file_path)
        self.python_file = 'python_file'
        return

    def get_input_output_handler(self):
        #try to pen out file
        outfile_handler = self.params_dict['outfile']
        params_dict = self.params_dict
        file_handler = {'outfile':outfile_handler}
        return file_handler

    def call_function(self):
        self.file_dir = cur_file_dir()
        field = self.params_dict['field']
        version = self.params_dict['version']
        field_dir = '%s%s%s' %(self.file_dir, '/config/field_', field)
        if not os.path.exists(field_dir):
            print(field_dir)
            return config.error['ERR_NO_FIELD_SCRIPTS']

        import_file = "import field_%s_%s" % (field,version[2:])
        print(import_file)

        if (field == '0x200000C') or (field == '0x2200000') or (field == '0x7200000'):
            function = "ret = field_%s_%s.entry_%s(self.params_dict['infile'], self.params_dict['field'], self.params_dict['offset'], self.params_dict['len'], self.params_dict['version'], self.params_dict['mode'], self.params_dict['outfile'], self.params_dict['field_list'])" % (field, version[2:], field)
        else:
            function = "ret = field_%s_%s.entry_%s(self.params_dict['infile'], self.params_dict['field'], self.params_dict['offset'], self.params_dict['len'], self.params_dict['version'], self.params_dict['mode'], self.params_dict['outfile'])" % (field, version[2:], field)

        #if  (field == '0x220000A') or (field == '0x2200006'):
        #    self.params_dict['outfile'].writelines('暂不支持解析')
        #    return 0
        #sys.path.append(field_dir+'\\')
        try:
            self.params_dict['outfile'].writelines("dumpid[%s][%s]\n" % (field, self.params_dict['field_name']))
            print("import field ing")
            #print(sys.path)
            exec(import_file)
        except Exception as e:
            self.params_dict['outfile'].writelines("%s fail\n" % field)
            print("%s fail:%s\n" % (field, e))
            return 9
        else:
            try:
                print("exec function ing")
                print(self.params_dict)
                exec(function)
                print("exec function done")
                return 0
            except Exception as e:
                self.params_dict['outfile'].writelines("%s fail\n" % function)
                print("exec function except")
                return 1

    def entry_mntn(self):
        ret = config.error['ERR_OTHER']
        #do something before exparse
        params_dict=self.params_dict
        self.append_dump_scrits()
        python_file = self.python_file
        file_handler = self.get_input_output_handler()
        if file_handler == config.error['ERR_OPEN_OUTFILE']:
            return file_handler
        self.params_dict['outfile'] = file_handler['outfile']
        #file_handler['outfile'].writelines('###########[parse  start]##########\n')

        if config.error['ERR_OPEN_OUTFILE'] == file_handler or config.error['ERR_OPEN_INFILE'] == file_handler:
            return file_handler
        if 'print' in list(params_dict.keys()):
            with open(params_dict['print'],'w') as file_handler['print']:
                sys.stdout=file_handler['print']
        if 'error' in list(params_dict.keys()):
            with open(params_dict['error'],'w') as file_handler['error']:
                sys.stderr=file_handler['error']
        #重定向log输出
        if 'log' in list(params_dict.keys()):
            with open(params_dict['log'],'w') as file_handler['log']:
                sys.stdout=file_handler['log']
                sys.stderr=file_handler['log']
        print("================field %s enter================" % (params_dict['field']))
        if 'field_list' in params_dict:
            field_list = params_dict['field_list']
        else:
            field_list = None
        if params_dict['mode'] in config.modeList:
            try:
                ret = self.call_function()
                print(ret)
            except IOError as e:
                print("error in ", params_dict['field'])
        else:
            print("ok in file python_file\n")
        #file_handler['outfile'].writelines('\n###########[parse    end]##########\n')
        file_handler['outfile'].close
        if 'print' in list(params_dict.keys()):
            file_handler['print'].close
        if 'error' in list(params_dict.keys()):
            file_handler['error'].close
        #调用模块无返回值，默认处理成功
        if ret is None:
            ret = config.error['ERR_SUCCESS']
        print("================field %s ret %d================" % (params_dict['field'], ret))
        return ret

class area_base:
    def __init__(self):
        self.list_area = []
        self.path = ''
        self.dirs = []
        self.area_num = 0
        return

    def global_area(self, baseoffset, area_offset,inhander):
        if inhander == None:
            print("file did not open\n")
            return
        #seek to area info
        magic,=struct.unpack("I", inhander.read(4))
        #if not magic==0x44656164 || not magic==0x4E524D53:
        #    print("magic is error 0x%x" % magic)
        #    return
        version,=struct.unpack("I", inhander.read(4))
        self.area_num,=struct.unpack("I", inhander.read(4))

        inhander.seek(baseoffset + area_offset, 0)

        print("magic %x\n" % magic)
        print("version %x\n" % version)
        print("area num %x\n" % self.area_num)

        print("baseoffset %x\n" % baseoffset)
        print("area_offset %x\n" % area_offset)
        for i in range(self.area_num):
            offset, = struct.unpack("I", inhander.read(4))
            print("offset %x\n" % offset)
            ofst = int(offset) + baseoffset
            print("ofst %x\n" % ofst)
            length,=struct.unpack("I", inhander.read(4))
            areainfo={
                'name':config.get_core_name(1<<i),
                'offset':int(ofst),
                'length':int(length),
                'coreid':(1<<i)
            }
            if i == 0:
                dumploadbase = int(ofst)
            dumploadbase += int(length)
            print(areainfo)
            #print(config.mntnbase)
            self.list_area.append(areainfo)
        #dumploadbase += 1036
        #print(dumploadbase)
        #inhander.seek(dumploadbase,0)
        #config.mntnbase = struct.unpack("I", inhander.read(4))
        #print(config.mntnbase)
        return

    def get_dirs(self):
        self.path = '%s%s' %(cur_file_dir(), "/config")
        path = self.path
        if not os.path.isdir(path):
            print(path + " is not exist")
            return
        my_dirs = os.listdir(path)
        for eachdir in my_dirs:
            eachdirpath = '%s%s%s' %(path, '/', eachdir)
            if os.path.isdir(eachdirpath):
                self.dirs.append(eachdir)
        return

class parse_base:
    def __init__(self):
        self.list_field = []
        self.list_field_id = []
        self.area_name = ''
        return

    def global_field(self,inhander,order,list_area):
        self.list_field = []
        if list_area == None or inhander == None:
            print("list_area or inhander is invaild\n")
            print(list_area)
            print(inhander)
            print("return with 2.\n")
            return 2
        areainfo = list_area[order]
        off=int(areainfo['offset'])
        inhander.seek(off)
        magic,  = struct.unpack('I', inhander.read(4))
        if magic != 0x4e656464 and magic != 0x70604102 and magic != 0x4c524d53:
            print("wrong area for order %x magic is %x" % (order, magic))
            print("return with 2.\n")
            return 2

        if magic == 0x4c524d53:
            l2version = struct.unpack('I',inhander.read(4))
            l2areanum = struct.unpack('I',inhander.read(4))
            l2areaname = struct.unpack('8s',inhander.read(8))
            l2savedone = struct.unpack('I',inhander.read(4))
            print("return with 1.\n")
            return 1

        field_num,area_name,  =   struct.unpack('I8s',inhander.read(12))
        print("field_num is %x areaname is %s" % (field_num, area_name))
        self.area_name = area_name.decode(encoding = "utf-8").strip('\x00')
        one,two, = struct.unpack('qq',inhander.read(16))
        for i in range(0,field_num):
            field,  =   struct.unpack('I',inhander.read(4))
            t_off,  =   struct.unpack('I',inhander.read(4))
            offset  =   t_off + off
            length,  =   struct.unpack('I',inhander.read(4))
            version, =   struct.unpack('I',inhander.read(4))
            temp_name,    =   struct.unpack('16s',inhander.read(16))
            fieldinfo={
                'field':field,
                'offset':offset,
                'length':length,
                'version':version&0xFFFF,
                'name':temp_name.decode().strip("\x00")
                }
            self.list_field.append(fieldinfo)
            print(fieldinfo)
        print("return with 0.\n")
        return 0

    def fieldparse(self, dirs):
        self.list_field_id = []
        if self.list_field == None:
            print("list_field is invaild\n")
            return
        if dirs == None:
            print("dirs is invaild")
            return
        for eachfield in self.list_field:
            field = int(eachfield['field'])
            field_str = str(hex(field))[2:].upper()
            field_name = '%s%s' %('field_0x', field_str)
            if field_name in dirs:
                self.list_field_id.append(eachfield)
        return

    def entry_module(self,dirs,infile, version, mode, outfile, field_list, area_name):
        try:
            parse = entry_parse()
            ret = 0
            if dirs == None:
                print('dirs is null')
                return 1
            else:
                self.fieldparse(dirs)
                if self.list_field_id == None:
                    print("fieldparse faild\n")
                    return 1
            if self.list_field_id:
                outfile.writelines("areaname[%s]\n" % area_name)
            for eachlist in self.list_field_id:
                field_str = '%s%s' %('0x', str(hex(eachlist['field']))[2:].upper())
                offset_str = '%s%s' %('0x', str(hex(eachlist['offset']))[2:].upper())
                length_str = '%s%s' %('0x', str(hex(eachlist['length']))[2:].upper())
                version_str = "%s%04x" % ('0x', eachlist['version'])
                file_name_str = eachlist['name']
                #version_str = "%s%04x" % ('0x',version)
                mode_str = str(mode)
                length_str = '%s%s' %('0x', str(hex(eachlist['length']))[2:].upper())
                if (field_str == '0x200000C') or (field_str == '0x2200000') or (field_str == '0x7200000'):
                    field_list = '%s%s' %('0x', str(hex(config.errmodid))[2:].upper())
                    print("field_list:", field_list)
                    print("errmodid:", config.errmodid)
                #outfile_str = '%s%s%s%s' % (outfile, '\\', str(eachlist['name']), r'.txt')
                parse.params_dict = {'infile':infile, 'field':field_str, 'offset':offset_str, 'len':length_str, 'version':version_str, 'mode':mode_str, 'outfile':outfile, 'field_list':field_list, 'field_name': file_name_str}
                ret |= parse.entry_mntn()
                print("ret = %u" % ret)
            return ret
        except IOError as e:
            print("rdr parse faild:", e)
            return config.error['ERR_OTHER']

def printl2exc(in_handler, outfile, offset):
        in_handler.seek(offset)
        modid,=struct.unpack("I", in_handler.read(4))
        arg1,=struct.unpack("I", in_handler.read(4))
        arg2,=struct.unpack("I", in_handler.read(4))
        e_core,=struct.unpack("I", in_handler.read(4))
        e_type,=struct.unpack("I", in_handler.read(4))
        e_module=in_handler.read(16)
        e_desc=in_handler.read(48)
        data_time=in_handler.read(24)
        outfile.writelines("[nr exc info]\n")
        outfile.writelines("modid                    :0x%x\n" % modid)
        outfile.writelines("arg1                :0x%x\n" % arg1)
        outfile.writelines("arg2                :0x%x\n" % arg2)
        outfile.writelines("e_core                :0x%x\n" % e_core)
        outfile.writelines("e_type                :0x%x\n" % e_type)
        outfile.writelines("Exc module              :%s\n" % e_module.decode(encoding="utf-8").strip('\x00'))
        outfile.writelines("Exc description         :%s\n" % e_desc.decode(encoding="utf-8").strip('\x00'))
        outfile.writelines("Exc datetime            :%s\n" % data_time.decode(encoding="utf-8").strip('\x00'))
        return

def entry(baseoffset, area_offset,infile,outfile,version,mode=1,field_list=None):
    try:
        areacnt = 0
        l2areacnt = 0

        if infile == None:
            return 4
        infile.seek(baseoffset)
        areabase = area_base()
        areabase.get_dirs() #add path of field to sys.path
        areabase.global_area(baseoffset, area_offset,infile)
        list_area = areabase.list_area
        print("entry  gloabal_area done.\n")
        parsebase = parse_base()
        print("entry  parse_base done.\n")
        for eacharea in list_area:
            print("areacnt = %x" % areacnt)
            arearet = parsebase.global_field(infile, areacnt, list_area);
            print("arearet = %d" % arearet)
            if arearet == 2:
                print("entry parse fail and continue.\n")
            elif arearet == 1:
                print("level2 area.\n")
                areal2 = area_base()
                l2offset = infile.tell()
                print("l2offset is %x.\n" % l2offset)
                printl2exc(infile,outfile,l2offset)
                l2offset = infile.tell()
                print("l2offset is %x.\n" % l2offset)
                infile.seek(l2offset - 132, 0)
                print("l2offset is %x.\n" % l2offset)
                areal2.global_area(baseoffset, l2offset - baseoffset, infile);
                l2list_area = areal2.list_area
                l2parse = parse_base()
                print("ready to l2 parse.\n")
                for eachl2area in l2list_area:
                    l2parse.global_field(infile, l2areacnt, l2list_area)
                    l2parse.entry_module(areabase.dirs, infile, version, mode, outfile, field_list, l2parse.area_name)
                    l2areacnt = l2areacnt + 1;
            elif arearet == 0:
                parsebase.entry_module(areabase.dirs, infile, version, mode, outfile, field_list, parsebase.area_name)
                print("entry  parse cp done.\n")
            areacnt = areacnt + 1
        return
    except IOError as e:
        print("rdr parse faild:", e)
        return config.error['ERR_OTHER']


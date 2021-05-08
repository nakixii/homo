#!/usr/bin/env python3
# coding=utf-8
# -*- coding: utf-8 -*-
# ***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename
# * Description   analysis regs dump
# * Version       1.0
# * Data          2019.6.28
# *
# ***********************************************************************
import struct
import os
import sys
import string


class EiccDumpPMSR:
    '''struct eicc_pm_dbg'''

    def __init__(self):
        self.parsed_ok = False
        self.s_times = 0
        self.r_times = 0
        self.sr_stat = []
        self.chn_id = 0
        self.last_step = 0
        self.errmsg = ''

    def parse(self, infile, parse_off, parse_len):
        usedlen = 32  # sizeof(struct eicc_pm_dbg)
        if parse_len < usedlen:
            self.errmsg += "EiccDumpPMSR LEN DETECT ERR\r\n"
            return
        self.s_times, = struct.unpack('I', infile.read(4))
        self.r_times, = struct.unpack('I', infile.read(4))
        self.sr_stat = list(struct.unpack('4I', infile.read(4*4)))
        self.chn_id, = struct.unpack('I', infile.read(4))
        self.last_step, = struct.unpack('I', infile.read(4))
        self.parsed_ok = True

    def get_plain_txt(self):
        plain_txt = ''
        if self.parsed_ok:
            plain_txt += 's_times:0x%08X\r\n' % (self.s_times)
            plain_txt += 'r_times:0x%08X\r\n' % (self.s_times)
            plain_txt += 'sr_stat:' + str(self.sr_stat) + '\r\n'
            plain_txt += 'sleep fail chn:0x%08X\r\n' % (self.chn_id)
            plain_txt += 'sleep fail step:0x%08X\r\n' % (self.last_step)
            plain_txt += self.errmsg
        else:
            plain_txt += self.errmsg
        return plain_txt


class EiccHwDev:
    def __init__(self):
        self.devid = 0
        self.core_cnt = 16
        self.pipepair_cnt = 0
        self.core_regs = []
        self.pipe_regs = []

    def parse(self, infile, parse_off, parse_len):
        usedlen = 12
        if parse_len < usedlen:
            raise Exception("EICC EiccHwDev PARSE ERR")

        self.devid, = struct.unpack('I', infile.read(4))
        self.core_cnt, = struct.unpack('I', infile.read(4))
        self.pipepair_cnt, = struct.unpack('I', infile.read(4))

        # sizeof(struct eicc_dump_cpuregsinfo) *16
        usedlen += 36 * self.core_cnt
        if parse_len < usedlen:
            raise Exception("EICC EiccHwDev COREREGS PARSE TRUNK ERR")

        for coreid in range(0, self.core_cnt):
            regs = {}
            regs['coreid'], = struct.unpack('I', infile.read(4))
            regs['omask0'], = struct.unpack('I', infile.read(4))
            regs['omask1'], = struct.unpack('I', infile.read(4))
            regs['imask0'], = struct.unpack('I', infile.read(4))
            regs['imask1'], = struct.unpack('I', infile.read(4))
            regs['ostat0'], = struct.unpack('I', infile.read(4))
            regs['ostat1'], = struct.unpack('I', infile.read(4))
            regs['istat0'], = struct.unpack('I', infile.read(4))
            regs['istat1'], = struct.unpack('I', infile.read(4))
            self.core_regs.append(regs)

        # sizeof(struct eicc_dump_piperegsinfo) *self.pipepair_cnt
        usedlen += 64 * self.pipepair_cnt
        if parse_len < usedlen:
            raise Exception("EICC EiccHwDev PIPEREGS PARSE TRUNK ERR")

        for pipeid in range(0, self.pipepair_cnt):
            regs = {}
            regs['pipeid'], = struct.unpack('I', infile.read(4))
            regs['owptr'], = struct.unpack('I', infile.read(4))
            regs['orptr'], = struct.unpack('I', infile.read(4))
            regs['omask'], = struct.unpack('I', infile.read(4))
            regs['oraw'], = struct.unpack('I', infile.read(4))
            regs['octrl'], = struct.unpack('I', infile.read(4))
            regs['ostat'], = struct.unpack('I', infile.read(4))
            regs['odbg0'], = struct.unpack('I', infile.read(4))
            regs['iwptr'], = struct.unpack('I', infile.read(4))
            regs['irptr'], = struct.unpack('I', infile.read(4))
            regs['irmte'], = struct.unpack('I', infile.read(4))
            regs['imask'], = struct.unpack('I', infile.read(4))
            regs['iraw'], = struct.unpack('I', infile.read(4))
            regs['ictrl'], = struct.unpack('I', infile.read(4))
            regs['istat'], = struct.unpack('I', infile.read(4))
            regs['idbg0'], = struct.unpack('I', infile.read(4))
            self.pipe_regs.append(regs)
        return usedlen

    def get_plain_txt(self):
        items = ['DEVID:0x%08X\r\n' % (self.devid)]
        items.append('PIPECNT:0x%08X\r\n' % (self.pipepair_cnt))
        items.append('C:\r\n')
        for coreid, regs in enumerate(self.core_regs):
            items.append('\t%X:' % (regs['coreid']))
            items.append('%X,' % (regs['omask0']))
            items.append('%X,' % (regs['omask1']))
            items.append('%X,' % (regs['imask0']))
            items.append('%X,' % (regs['imask1']))
            items.append('%X,' % (regs['ostat0']))
            items.append('%X,' % (regs['ostat1']))
            items.append('%X,' % (regs['istat0']))
            items.append('%X\r\n' % (regs['istat1']))
        items.append('P:\r\n')
        for pipeid, regs in enumerate(self.pipe_regs):
            items.append('\t%X:' % (regs['pipeid']))
            items.append('%X,' % (regs['owptr']))
            items.append('%X,' % (regs['orptr']))
            items.append('%X,' % (regs['omask']))
            items.append('%X,' % (regs['oraw']))
            items.append('%X,' % (regs['octrl']))
            items.append('%X,' % (regs['ostat']))
            items.append('%X\r\n' % (regs['odbg0']))

            items.append('\t%X:' % (regs['pipeid']))
            items.append('%X,' % (regs['iwptr']))
            items.append('%X,' % (regs['irptr']))
            items.append('%X,' % (regs['irmte']))
            items.append('%X,' % (regs['imask']))
            items.append('%X,' % (regs['iraw']))
            items.append('%X,' % (regs['ictrl']))
            items.append('%X,' % (regs['istat']))
            items.append('%X\r\n' % (regs['idbg0']))
        plain_txt = ''.join(items)
        return plain_txt


class EiccDumpHwReg:
    def __init__(self):
        self.devs = []
        self.errmsg = ''

    def parse(self, infile, parse_off, parse_len):
        used_len = 0
        try:
            while used_len < parse_len:
                dev = EiccHwDev()
                ret_len = dev.parse(infile, parse_off +
                                    used_len, parse_len - used_len)
                used_len += ret_len
                self.devs.append(dev)
        except Exception as ex:
            self.errmsg += str(ex) + '\r\n'
            raise ex

    def get_plain_txt(self):
        plain_txt = ''
        for dev in self.devs:
            plain_txt += dev.get_plain_txt()
            pass
        plain_txt += self.errmsg
        return plain_txt


class EiccDumpChannels:
    def __init__(self):
        self.errmsg = ''
        self.chns = []
        self.chn_len = 4*6  # sizeof(struct eicc_dump_chnsinfo)

    def parse(self, infile, parse_off, parse_len):
        used_len = 0
        while used_len < parse_len:
            if parse_len - used_len < self.chn_len:
                self.errmsg += "EiccDumpChannels DETECT ERR\r\n"
                return
            chn = {}
            chn['ldrvchn_id'], = struct.unpack('I', infile.read(4))
            chn['type'], = struct.unpack('I', infile.read(4))
            chn['wptr'], = struct.unpack('I', infile.read(4))
            chn['rptr'], = struct.unpack('I', infile.read(4))
            chn['dym_flags'], = struct.unpack('I', infile.read(4))
            chn['const_flags'], = struct.unpack('I', infile.read(4))
            used_len += self.chn_len
            self.chns.append(chn)
        return

    def get_plain_txt(self):
        items = ['CH:\r\n']
        for chn in self.chns:
            items.append('\t%X: ' % (chn['ldrvchn_id']))
            items.append('%X,' % (chn['type']))
            items.append('%X,' % (chn['wptr']))
            items.append('%X,' % (chn['rptr']))
            items.append('%X,' % (chn['dym_flags']))
            items.append('%X\r\n' % (chn['const_flags']))
        items.append(self.errmsg)
        plain_txt = ''.join(items)
        return plain_txt


class EiccDumpInfo:
    def __init__(self):
        self.parsed = False
        self.magic = 0
        self.version = 0
        self.reserved = 0
        self.length = 0
        self.modmsg = ''
        self.errmsg = ''
        self.tlvs = {0x0001: EiccDumpPMSR(), 0x0002: EiccDumpHwReg(),
                     0x0003: EiccDumpChannels()}

    def _parse_modtlv(self, infile, parse_off, parse_len):
        tail_len = parse_len
        tail_off = parse_off
        while tail_len > 0:
            usedlen = 16
            if tail_len < usedlen:
                raise Exception("EICC MODTLV TRUNKED ERR")
            try:
                tlv_modid, = struct.unpack('I', infile.read(4))
                tlv_version, = struct.unpack('I', infile.read(4))
                tlv_reserved, = struct.unpack('I', infile.read(4))
                tlv_length, = struct.unpack('I', infile.read(4))
                self.modmsg += "MOD[0x%08X] VER[0x%08X] LEN[0x%08X]\r\n" % (
                    tlv_modid, tlv_version, tlv_length)
            except Exception as ex:
                raise Exception("EICC MODTLV HDR PARSE ERR")
            tail_len = tail_len - usedlen
            tail_off = tail_off + usedlen
            if tail_len < tlv_length:
                raise Exception("EICC MODTLV HDR LENGTH ERR")

            # 得到一个TLV,若TLV没有解析器，不影响下个TLV分析
            if tlv_modid not in self.tlvs.keys():
                self.errmsg += 'EICC MOD:0x%08Xno parser,kipped\r\n' % (
                    tlv_modid)
                tail_len = tail_len - tlv_length
                tail_off = tail_off + tlv_length
                infile.seek(tail_off)
                continue
            # 得到一个TLV,若TLV解析失败，不影响下个TLV分析
            try:
                self.tlvs[tlv_modid].parse(infile, tail_off, tlv_length)
                tail_len = tail_len - tlv_length
                tail_off = tail_off + tlv_length
            except Exception as ex:
                self.errmsg += 'EICC MOD:0x%08X Parse Exception: %s!!!\r\n' % (
                    tlv_modid, str(ex))
                tail_len = tail_len - tlv_length
                tail_off = tail_off + tlv_length
                infile.seek(tail_off)

    def parse(self, infile, field_off, tail_len):
        usedlen = 16
        if tail_len < usedlen:
            raise Exception("EICC FEILD TRUNKED ERR")
        try:
            self.magic, = struct.unpack('I', infile.read(4))
            self.version, = struct.unpack('I', infile.read(4))
            self.reserved, = struct.unpack('I', infile.read(4))
            self.length, = struct.unpack('I', infile.read(4))
        except Exception as ex:
            raise ex
        if self.magic != 0x0000E1CC:
            raise Exception("EICC MAGIC DETECT ERR")
        if tail_len - usedlen < self.length:
            raise Exception("EICC FEILD TRUNKED ERR")

        self._parse_modtlv(infile, field_off+usedlen, self.length)
        self.parsed = True

    def get_plain_txt(self):
        plain_txt = ''
        if self.parsed:
            plain_txt += 'MAGIC:0x%08X\r\n' % (self.magic)
            plain_txt += 'VERISION:0x%08X\r\n' % (self.version)
            plain_txt += 'DUMPLEN:0x%08X\r\n' % (self.length)
            plain_txt += self.modmsg
            plain_txt += self.errmsg
            for key, value in self.tlvs.items():
                plain_txt += 'MODID:0x%08X INFO AS BELOW:\r\n' % (key)
                plain_txt += value.get_plain_txt()
        else:
            plain_txt += 'eicc dump info not parsed yet'
        return plain_txt

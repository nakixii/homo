#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) Huawei Technologies Co., Ltd. 2019-2020. All rights reserved.

import sys

def entry_nrphy_dump_parser_link(in_handler, outfile, offset, filelength):
    tb = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    base64group = 3
    with open(outfile, 'wb') as f:
        if (filelength == 0):
            return
        in_handler.seek(offset)
        groupNum = filelength // base64group
        remainCount = filelength % base64group
        for i in range(groupNum):
            bytes = in_handler.read(base64group)
            v_int = 0
            for x in bytes:
                v_int = v_int * 256 + x
            v1 = v_int % 64
            v2 = (v_int // 64) % 64
            v3 = (v_int // 4096) % 64
            v4 = (v_int // 262144) % 64
            c = '%c%c%c%c' % (tb[v4], tb[v3], tb[v2], tb[v1])
            f.write(c.encode())

        if remainCount == 0:
            return

        bytes = in_handler.read(remainCount)
        v = ''.join('{0:08b}'.format(x, 'b') for x in bytes)

        if remainCount == 2:
            v += '00'
            c = '%c%c%c%c' % (tb[int(v[0:6], 2)], tb[int(v[6:12], 2)], tb[int(v[12:18], 2)], '=' )
            f.write(c.encode())
        elif (remainCount == 1) :
            v += '0000'
            c = "%c%c%c%c" % (tb[int(v[0:6], 2)], tb[int(v[6:12], 2)], '=', '=')
            f.write(c.encode())

    return

def entry_nrphy_dump_parser(infile, outfile):
    with open(infile, "rb") as in_handler:
        in_handler.seek(0,2) # move the cursor to the end of the file
        filelength = in_handler.tell()
        entry_lphy_dump_parser_link(in_handler, outfile, 0, filelength)



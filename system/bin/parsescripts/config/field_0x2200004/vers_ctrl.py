#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   version ctrl
modify  record  :   2016-01-07 create file
"""

import struct
import string

MACRO_GAS_DEBUG_VERSION_LENGTH = 8
MACRO_VERSION_SEATTLE = "seat"
MACRO_VERSION_AUSTIN = "aust"
MACRO_VERSION_BOSTON = "bost"
MACRO_VERSION_V7R11 = "v711"
MACRO_VERSION_TRUNK = "truk"
MACRO_VERSION_NO_0 = 0
MACRO_VERSION_NO_1 = 1
MACRO_VERSION_NO_2 = 2
MACRO_VERSION_NO_3 = 3
MACRO_VERSION_NO_4 = 4

MACRO_VERSION_NO_INVALID = 0xFF


def guas_get_version_no(version_name, version_no):
    if MACRO_VERSION_SEATTLE == version_name.lower():
        return MACRO_VERSION_NO_0
    elif MACRO_VERSION_AUSTIN == version_name.lower():
        if "00" == version_no.lower():
            return MACRO_VERSION_NO_0
        elif "01" == version_no.lower():
            return MACRO_VERSION_NO_1
        elif "02" == version_no.lower():
            return MACRO_VERSION_NO_2
        elif "03" == version_no.lower():
            return MACRO_VERSION_NO_4
    elif MACRO_VERSION_BOSTON == version_name.lower():
        if "01" == version_no.lower():
            return MACRO_VERSION_NO_3
    elif MACRO_VERSION_V7R11 == version_name.lower():
        if "01" == version_no.lower():
            return MACRO_VERSION_NO_4
    elif MACRO_VERSION_TRUNK == version_name.lower():
        if "00" == version_no.lower():
            return MACRO_VERSION_NO_3
    return MACRO_VERSION_NO_INVALID


def analysis_guas_debug_version(instream, file_offset, outstream):
    instream.seek(file_offset)

    (version_name_0,) = struct.unpack('>B', instream.read(1))
    (version_name_1,) = struct.unpack('>B', instream.read(1))
    (version_name_2,) = struct.unpack('>B', instream.read(1))
    (version_name_3,) = struct.unpack('>B', instream.read(1))
    (version_space,) = struct.unpack('>B', instream.read(1))
    (version_no_0,) = struct.unpack('>B', instream.read(1))
    (version_no_1,) = struct.unpack('>B', instream.read(1))
    (version_end,) = struct.unpack('>B', instream.read(1))

    version_name = "%s%s%s%s" % (
        chr(version_name_0), chr(version_name_1), chr(version_name_2),
        chr(version_name_3))
    version_no = "%s%s" % (chr(version_no_0), chr(version_no_1))

    outstream.writelines(["%-15s%-7s\n" % ("Version Name:", version_name)])
    outstream.writelines(["%-15s%-7s\n" % ("Version No.:", version_no)])

    vers_no = guas_get_version_no(version_name, version_no)

    return version_name, vers_no

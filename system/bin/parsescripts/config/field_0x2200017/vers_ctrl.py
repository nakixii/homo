#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   version ctrl
author          :   sunbing 00184266
modify  record  :   2016-01-07 create file
"""

import string

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

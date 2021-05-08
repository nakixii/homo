#!/usr/bin/env python3
# coding=utf-8
"""
功能：uphy operate func
版权信息：华为技术有限公司，版权所有（C）2010-2019
修改记录：2016-07-08  创建
"""

__author__ = ''

def UphySetExistBit(int_type, mask):
    return(int_type | mask)

def UphyIsModeExistBit(int_type, mask):
    return(int_type & mask)


def UphySetModemModeStatus(mode_type, ModemIdx):
    if (strRatList == 'PLATFORM_RAT_GSM') and ( ModemIdx == 0 ):
        return UphySetExistBit( mode_type,ModemIdx )
    elif (strRatList == 'PLATFORM_RAT_WCDMA') and ( ModemIdx == 0 ):
        return UphySetExistBit( mode_type,ModemIdx )
    elif (strRatList == 'PLATFORM_RAT_GSM') and ( ModemIdx == 1 ):
        return UphySetExistBit( mode_type,ModemIdx )
    elif (strRatList == 'PLATFORM_RAT_WCDMA') and ( ModemIdx == 1 ):
        return UphySetExistBit( mode_type,ModemIdx )
    elif (strRatList == 'PLATFORM_RAT_GSM') and ( ModemIdx == 2 ):
        return UphySetExistBit( mode_type,ModemIdx )
    else:
        return 0


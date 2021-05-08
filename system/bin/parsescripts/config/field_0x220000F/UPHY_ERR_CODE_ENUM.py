#!/usr/bin/env python3
# coding=utf-8
"""
功能：list pid list
版权信息：华为技术有限公司，版权所有（C）2010-2019
修改记录：2016-07-08  创建
"""
import string

uphy_err_code_enum_table = {
    0   : "UPHY_SUCC",
    1   : "UPHY_FAIL",
    2  : "UPHY_ERR_OVERFLOW",
    3  : "UPHY_ERR_PTR_NULL",
    4  : "UPHY_ERR_NOT_EXPECT_VALUE",
    5  : "UPHY_ERR_EXPECT_STATUS",
    8  : "UPHY_AHB_HWAD_DOWN_ERROR",
    10 : "UPHY_MSG_NON_HANDLE",
    11  : "UPHY_MSG_BEEN_STORED",
    12   : "UPHY_STORE_HIGH_PRIO_MSG",
    13   : "UPHY_STORE_LOW_PRIO_MSG",
    14   : "UPHY_TRAVEL_BUFFER_MSG",
    15   : "UPHY_ERR_CODE_NV_DATA_ERROR",
    16   : "UPHY_ERR_CODE_ROOT_DATA_ERROR",
    17   : "UPHY_RF_PLL_LOCK",
    18   : "UPHY_RF_PLL_UNLOCK",
    19   : "UPHY_ERR_NO_VALID_DMA_CH",
    20   : "UPHY_ERR_INVALID_DMA_CH",
    21   : "UPHY_ERR_INVALID_DMA_ISR",
    22   : "UPHY_ERR_INVALID_DMA_PARA",
    23   : "UPHY_ERR_DMA_ERR",
    24   : "UPHY_ERR_DMA_CH_BUSY",
    25   : "UPHY_ERR_INVALID_TIMER_PARA",
    26   : "UPHY_ERR_NO_VALID_TIMER",
    27   : "UPHY_ERR_INVALID_TIMER_ID",
    28   : "UPHY_ERR_INVALID_TIMER_ISR",
    29   : "UPHY_ERR_INVALID_RAKE_MP_ISR",
    30   : "UPHY_ERR_INVALID_RAKE_TYPE1_MP_ISR",
    31   : "UPHY_ERR_INVALID_RAKE_BHHO_MP_ISR",
    32   : "UPHY_ERR_INVALID_MP_BITMAP",
    33   : "UPHY_ERR_INVALID_MP_PARA",
    34   : "UPHY_ERR_INVALID_BBP_MP_ISR",
    35   : "UPHY_ERR_INVALID_CELLNO",
    36   : "UPHY_ERR_INVALID_NO_PICH",
    37   : "UPHY_ERR_RBUFF_ALLOC",
    38   : "UPHY_ERR_PARA",
    39   : "UPHY_ERR_RLOG_BUFF_INIT",
    40   : "UPHY_ERR_SDT_NOT_LINK",
}

def UPHY_GetErrCode(ucErrCodeIdx):
    if ucErrCodeIdx in uphy_err_code_enum_table:
        strPid = uphy_err_code_enum_table[ucErrCodeIdx]
    else:
        strPid = "UPHY_ERR_CODE_ENUM_BUTT"
    return strPid
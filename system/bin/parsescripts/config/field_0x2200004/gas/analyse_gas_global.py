#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   include file
modify  record  :   2016-05-27 create file
"""

from gas.global_variable.gasm_global_status import *
from gas.global_variable.gcomc_global_status import *
from gas.global_variable.gcomm_global_status import *
from gas.global_variable.gcomsi_global_status import *
from gas.global_variable.grr_global_status import *
from gas.global_variable.rr_global_status import *

MACRO_GAS_GASM_GLOBAL_STATUS_LENGTH     = 28
MACRO_GAS_GCOMC_GLOBAL_STATUS_LENGTH    = 28
MACRO_GAS_GCOMSI_GLOBAL_STATUS_LENGTH   = 28
#MACRO_GAS_GCOMM_GLOBAL_STATUS_LENGTH    = 40
MACRO_GAS_RR_GLOBAL_STATUS_LENGTH       = 8
MACRO_GAS_GRR_GLOBAL_STATUS_LENGTH      = 16

def get_gcomm_global_status_lenth( vers_no):
    if (vers_no == 3):
        return 64
    else:
        return 40
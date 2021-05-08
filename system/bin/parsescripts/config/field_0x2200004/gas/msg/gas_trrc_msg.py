#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list gas trrc msg
modify  record  :   2016-01-07 create file
"""

gas_trrc_msg_enum_table = {
0x1875 : "TRRC_GRR_CELL_RESEL_CNF",
0x1876 : "TRRC_GRR_CELL_RESEL_STOP_CNF",
0x1877 : "TRRC_GRR_REDIRECTED_CNF",
0x1878 : "TRRC_GRR_REDIRECTED_STOP_CNF",
0x1879 : "TRRC_GRR_CELL_CHANGE_ORDER_CNF",
0x187a : "TRRC_GRR_CELL_CHANGE_ORDER_STOP_CNF",
0x187b : "TRRC_GRR_IRAT_HANDOVER_INFO_CNF",
0x187c : "TRRC_GRR_HANDOVER_CNF",
0x187d : "TRRC_GRR_HANDOVER_STOP_CNF",
0x187e : "TRRC_GRR_SET_DSP_POWER_CNF",
0x187f : "TRRC_GRR_MEASURE_CNF",
0x1880 : "TRRC_GRR_MEASURE_IND",
0x1881 : "TRRC_GRR_CELL_RESEL_REQ",
0x1882 : "TRRC_GRR_CELL_RESEL_STOP_REQ",
0x1883 : "TRRC_GRR_REDIRECTED_REQ",
0x1884 : "TRRC_GRR_REDIRECTED_STOP_REQ",
0x1885 : "TRRC_GRR_CELL_CHANGE_ORDER_REQ",
0x1886 : "TRRC_GRR_CELL_CHANGE_ORDER_STOP_REQ",
0x1887 : "TRRC_GRR_HANDOVER_REQ",
0x1888 : "TRRC_GRR_HANDOVER_STOP_REQ",
0x1889 : "TRRC_GRR_PLMN_SEARCH_REQ",
0x188a : "TRRC_GRR_PLMN_SEARCH_STOP_REQ",
0x188b : "TRRC_GRR_SET_DSP_POWER_REQ",
0x188c : "TRRC_GRR_GETUECAPINFO_REQ",
0x188d : "TRRC_GRR_MEASURE_REQ",
0x188f : "TRRC_GRR_BSIC_VERIFIED_REQ",
0x1891 : "TRRC_GRR_RELALL_REQ",
0x1895 : "GRR_TRRC_CELL_RESEL_REQ",
0x1896 : "GRR_TRRC_CELL_RESEL_STOP_REQ",
0x1897 : "GRR_TRRC_REDIRECTED_REQ",
0x1898 : "GRR_TRRC_REDIRECTED_STOP_REQ",
0x1899 : "GRR_TRRC_CELL_CHANGE_ORDER_REQ",
0x189a : "GRR_TRRC_CELL_CHANGE_ORDER_STOP_REQ",
0x189b : "GRR_TRRC_IRAT_HANDOVER_INFO_REQ",
0x189c : "GRR_TRRC_HANDOVER_REQ",
0x189d : "GRR_TRRC_HANDOVER_STOP_REQ",
0x189e : "GRR_TRRC_SET_DSP_POWER_REQ",
0x189f : "GRR_TRRC_MEASURE_REQ",
0x18a1 : "GRR_TRRC_CELL_RESEL_CNF",
0x18a2 : "GRR_TRRC_CELL_RESEL_STOP_CNF",
0x18a3 : "GRR_TRRC_REDIRECTED_CNF",
0x18a4 : "GRR_TRRC_REDIRECTED_STOP_CNF",
0x18a5 : "GRR_TRRC_CELL_CHANGE_ORDER_CNF",
0x18a6 : "GRR_TRRC_CELL_CHANGE_ORDER_STOP_CNF",
0x18a7 : "GRR_TRRC_HANDOVER_CNF",
0x18a8 : "GRR_TRRC_HANDOVER_STOP_CNF",
0x18a9 : "GRR_TRRC_PLMN_SEARCH_CNF",
0x18aa : "GRR_TRRC_PLMN_SEARCH_STOP_CNF",
0x18ab : "GRR_TRRC_SET_DSP_POWER_CNF",
0x18ac : "GRR_TRRC_GETUECAPINFO_CNF",
0x18ad : "GRR_TRRC_MEASURE_CNF",
0x18ae : "GRR_TRRC_MEASURE_IND",
0x18af : "GRR_TRRC_BSIC_VERIFIED_CNF",
0x18b0 : "GRR_TRRC_BSIC_VERIFIED_IND",
0x18b1 : "GRR_TRRC_RELALL_CNF",
}

def get_gas_trrc_msg_str( MsgId):
    for MsgIdIndex in gas_trrc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return gas_trrc_msg_enum_table[MsgIdIndex]

    return "none"
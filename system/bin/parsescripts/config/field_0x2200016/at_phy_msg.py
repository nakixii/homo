#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list at phy msg
modify  record  :   2019-05-24 create file
"""

at_phy_msg_enum_table = {
0x2621 : "ID_AT_HPA_RF_CFG_REQ",
0x62E0 : "ID_HPA_AT_RF_CFG_CNF",
0x2622 : "ID_AT_HPA_RF_RX_RSSI_REQ",
0x62E1 : "ID_HPA_AT_RF_RX_RSSI_IND",
0x2623 : "ID_AT_WPHY_RF_PLL_STATUS_REQ",
0x62E2 : "ID_AT_WPHY_RF_PLL_STATUS_CNF",
0x2415 : "ID_AT_GHPA_RF_RX_CFG_REQ",
0x2418 : "ID_AT_GHPA_RF_TX_CFG_REQ",
0x4212 : "ID_GHPA_AT_RF_MSG_CNF",
0x2416 : "ID_AT_GHPA_RF_RX_RSSI_REQ",
0x4210 : "ID_GHPA_AT_RF_RX_RSSI_IND",
0x2419 : "ID_AT_GPHY_RF_PLL_STATUS_REQ",
0x4219 : "ID_AT_GPHY_RF_PLL_STATUS_CNF",
0x2624 : "ID_AT_PHY_POWER_DET_REQ",
0x62e3 : "ID_AT_PHY_POWER_DET_CNF",
0x2625 : "ID_AT_HPA_RF_NOISE_CFG_REQ",
0x62e4 : "ID_HPA_AT_RF_NOISE_RSSI_IND",
0x241A : "ID_AT_GHPA_RF_NOISE_CFG_REQ",
0x421A : "ID_GHPA_AT_RF_NOISE_RSSI_IND",
0x2490 : "ID_AT_HPA_MIPI_WR_REQ",
0x4290 : "ID_HPA_AT_MIPI_WR_CNF",
0x2491 : "ID_AT_HPA_MIPI_RD_REQ",
0x4291 : "ID_HPA_AT_MIPI_RD_CNF",
0x2492 : "ID_AT_HPA_SSI_WR_REQ",
0x4292 : "ID_HPA_AT_SSI_WR_CNF",
0x2493 : "ID_AT_HPA_SSI_RD_REQ",
0x4293 : "ID_HPA_AT_SSI_RD_CNF",
0x2494 : "ID_AT_HPA_PDM_CTRL_REQ",
0x4294 : "ID_HPA_AT_PDM_CTRL_CNF",
0x62e5 : "ID_WPHY_AT_TX_CLT_IND",
0x6300 : "ID_AT_CHPA_RF_CFG_REQ",
0x6301 : "ID_CHPA_AT_RF_CFG_CNF",
0x6302 : "ID_AT_CHPA_RF_RX_RSSI_REQ",
0x6303 : "ID_CHPA_AT_RF_RX_RSSI_IND",
}

def get_at_phy_msg_str( MsgId):
    for MsgIdIndex in at_phy_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return at_phy_msg_enum_table[MsgIdIndex]

    return "none"
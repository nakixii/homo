#!/usr/bin/env python3
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list RrcPdcpInterface.h
author          :   sunbing 00184266
modify  record  :   2016-01-07 create file
"""

WAS_PDCP_MSG_ENUM_TABLE = {
    0x0000: "ID_RRC_PDCP_CONFIG_REQ",
    0x0001: "ID_PDCP_RRC_CONFIG_CNF",
    0x0002: "ID_RRC_PDCP_RELEASE_REQ",
    0x0003: "ID_PDCP_RRC_RELEASE_CNF",
    0x0004: "ID_RRC_PDCP_SYNC_REQ",
    0x0005: "ID_PDCP_RRC_SYNC_CNF",
    0x0006: "ID_RRC_PDCP_STOP_REQ",
    0x0007: "ID_PDCP_RRC_STOP_CNF",
    0x0008: "ID_RRC_PDCP_CONTINUE_REQ",
    0x0009: "ID_PDCP_RRC_CONTINUE_CNF",
    0x000A: "ID_RRC_PDCP_RELOC_REQ",
    0x000B: "ID_PDCP_RRC_RELOC_CNF",
    0x000C: "ID_RRC_PDCP_DLSIZE_CHANGE_REQ",
    0x000D: "ID_PDCP_RRC_DLSIZE_CHANGE_CNF",
    0x000E: "ID_RRC_PDCP_COMPRESS_INI_REQ",
    0x000F: "ID_PDCP_RRC_COMPRESS_INI_CNF",
    0x0011: "ID_PDCP_RRC_ERROR_IND",
}


def get_was_pdcp_msg_str(msg_id):
    for msg_id_index in WAS_PDCP_MSG_ENUM_TABLE.keys():
        if msg_id_index == msg_id:
            return WAS_PDCP_MSG_ENUM_TABLE[msg_id_index]

    return "none"

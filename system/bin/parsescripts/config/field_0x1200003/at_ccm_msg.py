#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   at css msg
modify  record  :   2019-05-25 create file
"""

at_ccm_msg_enum_table = {
  0x01 : "ID_TAF_CCM_QRY_CHANNEL_INFO_CNF",
  0x03 : "ID_TAF_CCM_CALL_CHANNEL_INFO_IND",
  0x05 : "ID_TAF_CCM_CALL_MODIFY_CNF",
  0x07 : "ID_TAF_CCM_CALL_ANSWER_REMOTE_MODIFY_CNF",
  0x09 : "ID_TAF_CCM_CALL_MODIFY_STATUS_IND",
  0x0B : "ID_TAF_CCM_QRY_ECONF_CALLED_INFO_CNF",
  0x0D : "ID_TAF_CCM_CALL_PRIVACY_MODE_IND",
  0x0F : "ID_TAF_CCM_CALL_ORIG_CNF",
  0x11 : "ID_TAF_CCM_CALL_SUPS_CMD_CNF",
  0x13 : "ID_TAF_CCM_CALL_SUPS_CMD_RSLT_IND",
  0x15 : "ID_TAF_CCM_CALL_ORIG_IND",
  0x17 : "ID_TAF_CCM_CALL_CONNECT_IND",
  0x19 : "ID_TAF_CCM_CALL_INCOMING_IND",
  0x1B : "ID_TAF_CCM_CALL_RELEASED_IND",
  0x1D : "ID_TAF_CCM_CALL_ALL_RELEASED_IND",
  0x1F : "ID_TAF_CCM_QRY_CALL_INFO_CNF",
  0x21 : "ID_TAF_CCM_QRY_CLPR_CNF",
  0x23 : "ID_TAF_CCM_QRY_XLEMA_CNF",
  0x25 : "ID_TAF_CCM_QRY_ECALL_INFO_CNF",
  0x27 : "ID_TAF_CCM_SET_CSSN_CNF",
  0x29 : "ID_TAF_CCM_START_DTMF_CNF",
  0x2B : "ID_TAF_CCM_START_DTMF_RSLT",
  0x2D : "ID_TAF_CCM_STOP_DTMF_CNF",
  0x2F : "ID_TAF_CCM_STOP_DTMF_RSLT",
  0x31 : "ID_TAF_CCM_CALL_PROC_IND",
  0x33 : "ID_TAF_CCM_CALL_ALERTING_IND",
  0x35 : "ID_TAF_CCM_CALL_HOLD_IND",
  0x37 : "ID_TAF_CCM_CALL_RETRIEVE_IND",
  0x39 : "ID_TAF_CCM_CALL_SS_IND",
  0x3B : "ID_TAF_CCM_ECC_NUM_IND",
  0x3D : "ID_TAF_CCM_GET_CDUR_CNF",
  0x3F : "ID_TAF_CCM_SET_UUS1_INFO_CNF",
  0x41 : "ID_TAF_CCM_QRY_UUS1_INFO_CNF",
  0x43 : "ID_TAF_CCM_UUS1_INFO_IND",
  0x45 : "ID_TAF_CCM_SET_ALS_CNF",
  0x47 : "ID_TAF_CCM_QRY_ALS_CNF",
  0x49 : "ID_TAF_CCM_CCWAI_SET_CNF",
  0x4B : "ID_TAF_CCM_CNAP_INFO_IND",
  0x4D : "ID_TAF_CCM_CNAP_QRY_CNF",
  0x4F : "ID_TAF_CCM_ECONF_DIAL_CNF",
  0x51 : "ID_TAF_CCM_ECONF_NOTIFY_IND",
  0x53 : "ID_TAF_CCM_SEND_FLASH_CNF",
  0x55 : "ID_TAF_CCM_SEND_BURST_DTMF_CNF",
  0x57 : "ID_TAF_CCM_SEND_BURST_DTMF_RSLT",
  0x59 : "ID_TAF_CCM_BURST_DTMF_IND",
  0x5B : "ID_TAF_CCM_SEND_CONT_DTMF_CNF",
  0x5D : "ID_TAF_CCM_SEND_CONT_DTMF_RSLT",
  0x5F : "ID_TAF_CCM_CONT_DTMF_IND",
  0x61 : "ID_TAF_CCM_CCWAC_INFO_IND",
  0x63 : "ID_TAF_CCM_CALLED_NUM_INFO_IND",
  0x65 : "ID_TAF_CCM_CALLING_NUM_INFO_IND",
  0x67 : "ID_TAF_CCM_DISPLAY_INFO_IND",
  0x69 : "ID_TAF_CCM_EXT_DISPLAY_INFO_IND",
  0x6B : "ID_TAF_CCM_CONN_NUM_INFO_IND",
  0x6D : "ID_TAF_CCM_REDIR_NUM_INFO_IND",
  0x6F : "ID_TAF_CCM_SIGNAL_INFO_IND",
  0x71 : "ID_TAF_CCM_LINE_CTRL_INFO_IND",
  0x73 : "ID_TAF_CCM_CALL_WAITING_IND",
  0x75 : "ID_TAF_CCM_ENCRYPT_VOICE_CNF",
  0x77 : "ID_TAF_CCM_ENCRYPT_VOICE_IND",
  0x79 : "ID_TAF_CCM_EC_REMOTE_CTRL_IND",
  0x7B : "ID_TAF_CCM_REMOTE_CTRL_ANSWER_CNF",
  0x7D : "ID_TAF_CCM_ECC_SRV_CAP_CFG_CNF",
  0x7F : "ID_TAF_CCM_ECC_SRV_CAP_QRY_CNF",
  0x81 : "ID_TAF_CCM_SET_EC_TEST_MODE_CNF",
  0x83 : "ID_TAF_CCM_GET_EC_TEST_MODE_CNF",
  0x85 : "ID_TAF_CCM_GET_EC_RANDOM_CNF",
  0x87 : "ID_TAF_CCM_GET_EC_KMC_CNF",
  0x89 : "ID_TAF_CCM_SET_EC_KMC_CNF",
  0x8B : "ID_TAF_CCM_ENCRYPTED_VOICE_DATA_IND",
  0x8D : "ID_TAF_CCM_PRIVACY_MODE_SET_CNF",
  0x8F : "ID_TAF_CCM_PRIVACY_MODE_QRY_CNF",
  0x91 : "ID_TAF_CCM_PRIVACY_MODE_IND",
}

def get_at_ccm_msg_str( MsgId):
    for MsgIdIndex in at_ccm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return at_ccm_msg_enum_table[MsgIdIndex]

    return "none"
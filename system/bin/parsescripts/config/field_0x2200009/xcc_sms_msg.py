#!/usr/bin/env python3
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list xcc sms msg
modify  record  :   2016-04-27 create file
"""

xcc_sms_msg_enum_table = {
0x2000 : "ID_CSMS_XCC_ORIG_SMS_CALL_REQ",
0x2001 : "ID_XCC_CSMS_ORIG_SMS_CALL_CNF",
0x2002 : "ID_CSMS_XCC_END_SMS_CALL_REQ",
0x2003 : "ID_XCC_CSMS_END_SMS_CALL_CNF",
0x2004 : "ID_XCC_CSMS_INCOMING_CALL_IND",
0x2005 : "ID_CSMS_XCC_INCOMING_CALL_RSP",
0x2006 : "ID_XCC_CSMS_CALL_CONN_IND",
0x2007 : "ID_CSMS_XCC_ANSWER_CALL_REQ",
0x2008 : "ID_XCC_CSMS_ANSWER_CALL_CNF",
0x2009 : "ID_XCC_CSMS_MESSAGE_WAITING_IND",
0x200A : "ID_XCC_CSMS_SERVICE_CONNECT_IND",
0x200B : "ID_XCC_CSMS_MSG_WATING_IND",
}

def get_xcc_sms_msg_str( MsgId):
    for MsgIdIndex in xcc_sms_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return xcc_sms_msg_enum_table[MsgIdIndex]

    return "none"
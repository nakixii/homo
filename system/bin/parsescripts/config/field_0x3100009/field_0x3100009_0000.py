#!/usr/bin/env python3
# coding=utf-8
#######################################################################################################################################
#   copyright       :   Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
#
#   filename        :   exparse_python_frame.py
#
#
#   description     :   pcie ep config for exparse python sripts frame
#
#   modify  record  :   2019-04-25 add new user 13 in UserEnumTable
#
#######################################################################################################################################
import struct
import os
import sys
import string
#from config import *

global g_Pcie_PmLockEnumTable
global g_Pcie_UserEnumTable

########################################################################################
g_Pcie_PmLockEnumTable = {
    0: ("TRY_LOCK"),
    1: ("FORCE_LOCK"),
    2: ("TIMEOUT_LOCK"),
    3: ("UNLOCK"),
    4: ("ERR_LOCK")
}
g_Pcie_UserEnumTable = {
    0: ("USER_PCIE_DRV"),
    1: ("USER_EP_PM"),
    2: ("USER_RC_PM"),
    3: ("USER_DUMP"),
    4: ("USER_CHAR_DEV"),
    5: ("USER_RFS"),
    6: ("USER_ETH_DEV"),
    7: ("USER_ICC"),
    8: ("USER_TEST"),
    9: ("USER_MBOOT"),
    10:("USER_RESET"),
    11:("USER_TEMP"),
    12:("USER_PM_TEST"),
    13:("PCIE_USER_SPEED_CTRL")
}
g_Pcie_BarUserTable = {
    0: ("EP_GIC_MSI"),
    1: ("EP_MSI_TO_RC"),
    2: ("CHAR_DEV"),
    3: ("ETH_DEV"),
    4: ("EP_DMA_CTL"),
    5: ("ICC"),
    6: ("RFS"),
    7: ("INTX"),
    8: ("PCIE_TEST"),
    9: ("DUMP"),
    10:("PM_CTL")
}

g_Pcie_PmStateTypeEnumTable = {
    0: ("CURRENT_STATE"),
    1: ("INNER_EVENT"),
    2: ("OUTER_EVENT")
}

g_Pcie_PmStateEnumTable = {
    0: ("UNINITED"),
    1: ("RESETTING"),
    2: ("LINK_UP"),
    3: ("LINK_IDLE"),
    4: ("PRESUSPEND"),
    5: ("POWER_DOWN"),
    6: ("PRE_POWER_UP"),
    7: ("RC_CLK_READY"),
    8: ("EP_PCIE_READY"),
    9: ("POWER_UP")
}

g_Pcie_PmEventEnumTable = {
    0: ("GET_API_SUSPEND"),
    1: ("GET_API_RESUME"),
    2: ("GET_PCIE_MSI"),
    3: ("GET_GPIO"),
    4: ("SUSPEND_TIMEOUT"),
    5: ("UNLOCK_CLEAR"),
    6: ("PRE_POWERUP"),
}

g_Pcie_PmGpioEnumTable = {
    0: ("AP_WAKE_MODEM_GPIO"),
    1: ("MODEM_WAKE_AP_GPIO"),
    2: ("AP_STATUS_GPIO"),
    3: ("MODEM_STATUS_GPIO"),
}

g_Pcie_PmGpioActionTable = {
    0: ("GPIO_UP"),
    1: ("GPIO_DOWN"),
    2: ("GPIO_RECEIVE"),
}

g_Pcie_PmGpioActionTable = {
    0: ("GPIO_UP"),
    1: ("GPIO_DOWN"),
    2: ("GPIO_RECEIVE"),
}

g_Pcie_ApToModemMsiTable = {
    0: ("RFS"),
    1: ("CHAR_DEV"),
    2: ("ETH_DEV"),
    3: ("ICC"),
    4: ("DIAG"),
    5: ("DUMP"),
    6: ("USER_INIT"),
    7: ("PM_TEST"),
    8: ("PM"),
    9: ("MSI_TEST_BEGIN"),
    10: ("MSI_TEST_BEGIN"),
    11: ("MSI_TEST_BEGIN1"),
    12: ("MSI_TEST_BEGIN2"),
    13: ("MSI_TEST_BEGIN3"),
    14: ("MSI_TEST_BEGIN4"),
    15: ("MSI_TEST_END"),
}

g_Pcie_ModemToApMsiTable = {
    0: ("RFS"),
    1: ("CHAR_DEV"),
    2: ("ETH_DEV"),
    3: ("ICC"),
    4: ("DIAG"),
    5: ("DUMP"),
    6: ("RESET"),
    7: ("DMA_WRITE"),
    8: ("DMA_READ"),
    9: ("PM_STATUS"),
    10:("PM_TEST"),
    11:("EP_WAKE_RC_USER"),
    12:("PM"),
    13:("MSI_TEST_BEGIN"),
    14:("MSI_TEST_BEGIN1"),
    15:("MSI_TEST_END"),
}

g_Pcie_MsiTypeTable = {
    0: ("MSI_SEND"),
    1: ("MSI_READ"),
}

g_Pcie_MsiActionTable = {
    0: ("MSI_HANDLER_IN"),
    1: ("MSI_HANDLER_OUT"),
    2: ("MSI_SEND_OUT"),
}

g_Pcie_ModemToApMsgTable = {
    0: ("IDLE_RESERVED"),
    1: ("EP_LOCK_FREE"),
    2: ("EP_LOCK_BUSY"),
}

g_Pcie_ApToModemMsgTable = {
    0: ("IDLE_RESERVED"),
    1: ("RC_VOTE_TO_SLEEP"),
    2: ("RC_SLOW_AWAKE_DONE"),
    3: ("RC_SET_SLOW_L1SS"),
}

g_Pcie_MsgTypeTable = {
    0: ("MSG_SEND"),
    1: ("MSG_READ"),
}

g_Pcie_WakeLockActTable = {
    0: ("WAKE_LOCK"),
    1: ("WAKE_UNLOCK"),
}

g_Pcie_WakeLockEnumTable = {
    0: ("PCIE_PM_DRV"),
    1: ("PCIE_PM_API"),
}

g_Pcie_VoteEdgeActTable = {
    0: ("FIRST_LOCK"),
    1: ("LAST_UNLOCK"),
}

g_Pcie_DmaChanTable = {
    0: ("CHAR_DEV"),
    1: ("ETH_DEV"),
    2: ("ICC"),
    3: ("RFS"),
    4: ("DUMP"),
    5: ("NOT_YET"),
    6: ("NOT_YET"),
    7: ("NOT_YET"),
}
g_Pcie_DmaTypeTable = {
    0: ("DMA_WRITE"),
    1: ("DMA_READ"),
    2: ("DMA_WRITE_IRQ"),
    3: ("DMA_READ_IRQ"),
}
g_Pcie_DmaActionTable = {
    0: ("DMA_CB_IN"),
    1: ("DMA_CB_OUT"),
    2: ("DMA_TRANS_OUT"),
}
g_Pcie_DmaTransTable = {
    0: ("NORMAL_MODE"),
    1: ("LINK_MODE"),
}
g_Pcie_DmaDirectionTable = {
    0: ("TRANS_READ"),
    1: ("TRANS_WRITE"),
}
g_Pcie_BootStageTable = {
    0: ("BOOT_LINK"),
    1: ("LOAD_IMAGE_DONE"),
    2: ("SEND_BOOT_GPIO"),
    3: ("GET_BOOT_GPIO"),
    4: ("KERNEL_INIT_DONE"),
    5: ("PM_INIT_DONE"),
    6: ("USER_INIT_DONE"),
}

g_Pcie_ModemCbTable = {
    0: ("BAR_CONFIG"),
    1: ("PCIE_INIT_DONE"),
    2: ("EXIT"),
    3: ("LINKDOWN"),
    4: ("SUSPEND"),
    5: ("RESUME"),
    6: ("POWER_UP"),
    7: ("POWER_DOWN"),
}

g_Pcie_ApCbTable = {
    0: ("ENUM_DONE"),
    1: ("EXIT"),
    2: ("LINKDOWN"),
    3: ("SUSPEND"),
    4: ("RESUME"),
    5: ("POWER_UP"),
    6: ("POWER_DOWN"),
}

total_offset = 0

def sort_array(row, array, sort_row):
    for i in range(0, row-1):
        for j in range(0, row-1-i):
            if array[j][sort_row] > array[j+1][sort_row]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def parse_pcie_bin_lock(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    # 20
    struct.unpack('I', infile.read(4))#trace-index
    struct.unpack('I', infile.read(4))#trace-index
    total_offset +=  (4 + 4)
    outfile.writelines('first sign byte 0x62626262, total_offset: 0x%x\n\n' %(total_offset))
    outfile.writelines("**************************************pcie pm lock debug**************************************\n")
    outfile.writelines('%-20s %-20s %-20s %-20s\n' %('user','lock_type','cnt', 'last_time'))
    for i in range(0, 14):#user_id
        for j in range(0, 5):#lock_type
            (cnt, )            = struct.unpack('I', infile.read(4))
            (timestamp,   )    = struct.unpack('I', infile.read(4))
            if cnt > 0:
                outfile.writelines('%-20s %-20s %-20d 0x%-18x\n' %(g_Pcie_UserEnumTable[i], g_Pcie_PmLockEnumTable[j], cnt, timestamp))
        (lock_time,   )    = struct.unpack('I', infile.read(4))
        if lock_time > 0 and i > 2:#RC/EP/DRV PM User invalid
            outfile.writelines('user: %s, total_lock_time: 0x%-18x\n' %(g_Pcie_UserEnumTable[i], lock_time))
        elif i == 2:
            outfile.writelines('user: %s, total_lock_time refers to PCIE_RC_DBG Analysis\n' %(g_Pcie_UserEnumTable[i]))
    total_offset += 14*(5*(4+4)+4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))
    # 32
    outfile.writelines("**************************************pcie pm lock trace**************************************\n")
    outfile.writelines('%-20s %-20s %-20s\n' %('timestamp', 'user', 'action'))
    trace_array = [[0] * 3 for _ in range(32)]
    for i in range(0, 32):#trace list
        (trace_array[i][0], )    = struct.unpack('I', infile.read(4)) #timestamp
        (trace_array[i][1], )    = struct.unpack('H', infile.read(2)) #user_id
        (trace_array[i][2], )    = struct.unpack('H', infile.read(2)) #act_id

    sort_array(32,trace_array,0)
    for i in range(0, 32):
        if trace_array[i][0] > 0:
        	outfile.writelines('0x%-18x %-20s %-20s\n' %(trace_array[i][0], g_Pcie_UserEnumTable[trace_array[i][1]], g_Pcie_PmLockEnumTable[trace_array[i][2]]))

    outfile.writelines('\n\n')
    struct.unpack('I', infile.read(4))#trace-index
    total_offset +=  (32*(4+2+2) + 4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))

def parse_pcie_bin_state(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    outfile.writelines("**************************************pcie pm state debug**************************************\n")
    for i in range(0, 3):#state type
        outfile.writelines('--------------------%s--------------------\n' %(g_Pcie_PmStateTypeEnumTable[i]))
        outfile.writelines('%-20s %-20s %-20s\n' %('state_id', 'cnt', 'last_time'))
        for j in range(0, 10):#state_id
            (cnt, )            = struct.unpack('I', infile.read(4))
            (timestamp,   )    = struct.unpack('I', infile.read(4))
            if cnt > 0:
                outfile.writelines('%-20s %-20d 0x%-18x\n' %(g_Pcie_PmStateEnumTable[j], cnt, timestamp))
    total_offset +=  3*10*(4+4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))
    # 32
    outfile.writelines("**************************************pcie pm state trace**************************************\n")
    outfile.writelines('%-20s %-20s %-20s\n' %('timestamp', 'state_type', 'state_id'))
    trace_array = [[0] * 3 for _ in range(32)]
    for i in range(0, 32):#trace list
        (trace_array[i][0], )    = struct.unpack('I', infile.read(4)) #timestamp
        (trace_array[i][1], )    = struct.unpack('H', infile.read(2)) #state_id
        (trace_array[i][2], )    = struct.unpack('H', infile.read(2)) #state_type

    sort_array(32,trace_array,0)
    for i in range(0, 32):#trace list
        if trace_array[i][0] > 0:
        	outfile.writelines('0x%-18x %-20s %-20s\n' %(trace_array[i][0], g_Pcie_PmStateTypeEnumTable[trace_array[i][2]], g_Pcie_PmStateEnumTable[trace_array[i][1]]))

    outfile.writelines('\n\n')
    struct.unpack('I', infile.read(4))#trace-index
    total_offset +=  (32*(4+2+2) + 4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))

def parse_pcie_bin_event(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    outfile.writelines("**************************************pcie pm wakeup event debug**************************************\n")
    outfile.writelines('%-20s %-20s %-20s\n' %('event_id', 'cnt', 'last_time'))
    for j in range(0, 7):#event_id
        (cnt, )            = struct.unpack('I', infile.read(4))
        (timestamp,   )    = struct.unpack('I', infile.read(4))
        if cnt > 0:
            outfile.writelines('%-20s %-20d 0x%-18x\n' %(g_Pcie_PmEventEnumTable[j], cnt, timestamp))
    total_offset +=  7*(4+4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))
    # 32
    outfile.writelines("**************************************pcie pm wakeup event trace**************************************\n")
    outfile.writelines('%-20s %-20s\n' %('timestamp', 'event_id'))
    trace_array = [[0] * 2 for _ in range(32)]
    for i in range(0, 32):#trace list
        (trace_array[i][0], )    = struct.unpack('I', infile.read(4)) #timestamp
        (trace_array[i][1], )    = struct.unpack('I', infile.read(4)) #event id

    sort_array(32,trace_array,0)

    for i in range(0, 32):#trace list
        if trace_array[i][0] > 0:
        	outfile.writelines('0x%-18x %-20s\n' %(trace_array[i][0], g_Pcie_PmEventEnumTable[trace_array[i][1]]))

    outfile.writelines('\n\n')
    struct.unpack('I', infile.read(4))#trace-index
    total_offset +=  (32*(4+4) + 4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))

def parse_pcie_bin_gpio(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    outfile.writelines("**************************************pcie pm gpio debug**************************************\n")
    for i in range(0, 4):#gpio_id
        outfile.writelines('--------------------%s--------------------\n' %(g_Pcie_PmGpioEnumTable[i]))
        outfile.writelines('%-20s %-20s %-20s\n' %('action_id', 'cnt', 'last_time'))
        for j in range(0, 3):#action_id
            (cnt, )            = struct.unpack('I', infile.read(4))
            (timestamp,   )    = struct.unpack('I', infile.read(4))
            if cnt > 0:
                outfile.writelines('%-20s %-20d 0x%-18x\n' %(g_Pcie_PmGpioActionTable[j], cnt, timestamp))
    total_offset +=  4*3*(4+4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))
    # 32
    outfile.writelines("**************************************pcie pm gpio trace**************************************\n")
    outfile.writelines('%-20s %-20s %-20s\n' %('timestamp', 'gpio_id', 'action_id'))
    trace_array = [[0] * 3 for _ in range(32)]
    for i in range(0, 32):#trace list
        (trace_array[i][0], )    = struct.unpack('I', infile.read(4)) #timestamp
        (trace_array[i][1], )    = struct.unpack('H', infile.read(2)) #gpio_id
        (trace_array[i][2], )    = struct.unpack('H', infile.read(2)) #act_id

    sort_array(32,trace_array,0)
    for i in range(0, 32):#trace list
        if trace_array[i][0] > 0:
        	outfile.writelines('0x%-18x %-20s %-20s\n' %(trace_array[i][0], g_Pcie_PmGpioEnumTable[trace_array[i][1]], g_Pcie_PmGpioActionTable[trace_array[i][2]]))

    outfile.writelines('\n\n')
    struct.unpack('I', infile.read(4))#trace-index
    total_offset +=  (32*(4+2+2) + 4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))

def parse_pcie_bin_msi(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    outfile.writelines("**************************************pcie pm msi debug**************************************\n")
    outfile.writelines('%-20s %-20s %-20s %-20s %-20s\n' %('msi_id', 'msi_type', 'msi_action', 'cnt', 'last_time'))
    for i in range(0, 16):#msi_id
        for j in range(0, 2):#msi_type
            for k in range(0, 3):#msi_action
                (cnt, )            = struct.unpack('I', infile.read(4))
                (timestamp,   )    = struct.unpack('I', infile.read(4))
                if cnt > 0:
                    if j == 0: #send
                        outfile.writelines('%-20s %-20s %-20s %-20d 0x%-18x\n' %(g_Pcie_ModemToApMsiTable[i], g_Pcie_MsiTypeTable[j], g_Pcie_MsiActionTable[k], cnt, timestamp))
                    else: #read
                        outfile.writelines('%-20s %-20s %-20s %-20d 0x%-18x\n' %(g_Pcie_ApToModemMsiTable[i], g_Pcie_MsiTypeTable[j], g_Pcie_MsiActionTable[k], cnt, timestamp))

    total_offset +=  16*2*3*(4+4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))
    # 32
    outfile.writelines("**************************************pcie pm msi trace**************************************\n")
    outfile.writelines('%-20s %-20s %-20s %-20s\n' %('timestamp', 'msi_id', 'type_id', 'action_id'))

    trace_array = [[0] * 5 for _ in range(32)]
    for i in range(0, 32):#trace list
        (trace_array[i][0], )    = struct.unpack('I', infile.read(4)) #timestamp
        (trace_array[i][1], )    = struct.unpack('H', infile.read(2)) #msi_id
        (trace_array[i][2], )    = struct.unpack('H', infile.read(2)) #type_id
        (trace_array[i][3], )    = struct.unpack('H', infile.read(2)) #act_id
        (trace_array[i][4], )    = struct.unpack('H', infile.read(2)) #reserve

    sort_array(32,trace_array,0)

    for i in range(0, 32):#trace list
        if trace_array[i][0] > 0:
            if trace_array[i][2] == 0:#send
                outfile.writelines('0x%-18x %-20s %-20s %-20s\n' %(trace_array[i][0], g_Pcie_ModemToApMsiTable[trace_array[i][1]], g_Pcie_MsiTypeTable[trace_array[i][2]], g_Pcie_MsiActionTable[trace_array[i][3]]))
            else:
                outfile.writelines('0x%-18x %-20s %-20s %-20s\n' %(trace_array[i][0], g_Pcie_ApToModemMsiTable[trace_array[i][1]], g_Pcie_MsiTypeTable[trace_array[i][2]], g_Pcie_MsiActionTable[trace_array[i][3]]))

    outfile.writelines('\n\n')
    struct.unpack('I', infile.read(4))#trace-index
    total_offset +=  (32*(4+2+2+2+2) + 4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))

def parse_pcie_bin_wakelock(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    outfile.writelines("**************************************pcie pm wakelock debug**************************************\n")
    outfile.writelines('%-20s %-20s %-20s %-20s\n' %('wakelock_id', 'wakelock_action', 'cnt', 'last_time'))
    for i in range(0, 2):#wakelock_id
        for j in range(0, 2):#wakelock_action
            (cnt, )            = struct.unpack('I', infile.read(4))
            (timestamp,   )    = struct.unpack('I', infile.read(4))
            if cnt > 0:
                outfile.writelines('%-20s %-20s %-20s 0x%-18x\n' %(g_Pcie_WakeLockEnumTable[i], g_Pcie_WakeLockActTable[j], cnt, timestamp))

    total_offset +=  2*2*(4+4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))
    # 32
    outfile.writelines("**************************************pcie pm wakelock trace**************************************\n")
    outfile.writelines('%-20s %-20s %-20s\n' %('timestamp', 'wakelock_id', 'wakelock_action'))
    trace_array = [[0] * 3 for _ in range(32)]
    for i in range(0, 32):#trace list
        (trace_array[i][0], )    = struct.unpack('I', infile.read(4)) #timestamp
        (trace_array[i][1], )    = struct.unpack('H', infile.read(2)) #wakelock_id
        (trace_array[i][2], )    = struct.unpack('H', infile.read(2)) #wakelock_act

    sort_array(32,trace_array,0)

    for i in range(0, 32):#trace list
        if trace_array[i][0] > 0:
        	outfile.writelines('0x%-18x %-20s %-20s\n' %(trace_array[i][0], g_Pcie_WakeLockEnumTable[trace_array[i][1]], g_Pcie_WakeLockActTable[trace_array[i][2]]))

    outfile.writelines('\n\n')
    struct.unpack('I', infile.read(4))#trace-index
    total_offset +=  (32*(4+2+2) + 4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))

def parse_pcie_bin_vote_edge(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    outfile.writelines("**************************************pcie pm vote edge debug**************************************\n")
    outfile.writelines('%-20s %-20s %-20s %-20s\n' %('user_id', 'vote_edge_type', 'cnt', 'last_time'))
    for i in range(0, 14):#user_id
        for j in range(0, 2):#edge_type
            (cnt, )            = struct.unpack('I', infile.read(4))
            (timestamp,   )    = struct.unpack('I', infile.read(4))
            if cnt > 0:
                outfile.writelines('%-20s %-20s %-20s 0x%-18x\n' %(g_Pcie_UserEnumTable[i], g_Pcie_VoteEdgeActTable[j], cnt, timestamp))

    total_offset +=  14*2*(4+4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))
    # 32
    outfile.writelines("**************************************pcie pm vote edge trace**************************************\n")
    outfile.writelines('%-20s %-20s %-20s\n' %('timestamp', 'user_id', 'vote_edge_action'))
    trace_array = [[0] * 3 for _ in range(32)]
    for i in range(0, 32):#trace list
        (trace_array[i][0], )    = struct.unpack('I', infile.read(4)) #timestamp
        (trace_array[i][1], )    = struct.unpack('H', infile.read(2)) #action
        (trace_array[i][2], )    = struct.unpack('H', infile.read(2)) #user_id

    sort_array(32,trace_array,0)

    for i in range(0, 32):#trace list
        if trace_array[i][0] > 0:
        	outfile.writelines('0x%-18x %-20s %-20s\n' %(trace_array[i][0], g_Pcie_UserEnumTable[trace_array[i][2]], g_Pcie_VoteEdgeActTable[trace_array[i][1]]))

    outfile.writelines('\n\n')
    struct.unpack('I', infile.read(4))#trace-index
    struct.unpack('I', infile.read(4))#trace-index
    total_offset +=  (32*(4+2+2) + 8)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))

def parse_pcie_bin_bar(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    outfile.writelines("**************************************pcie bar debug**************************************\n")
    outfile.writelines('%-20s %-20s %-20s %-20s\n' %('bar_user', 'bar_addr_h', 'bar_addr_l', 'bar_size'))
    for i in range(0, 48):#user_id
        (bar_addr_l, )            = struct.unpack('I', infile.read(4))
        (bar_addr_h, )            = struct.unpack('I', infile.read(4))
        (bar_size,   )           = struct.unpack('I', infile.read(4))
        struct.unpack('I', infile.read(4))#align with bar_addr
        if bar_addr_l > 0:
            outfile.writelines('%-20s 0x%-18x 0x%-18x 0x%-18x\n' %(g_Pcie_BarUserTable[i], bar_addr_h, bar_addr_l, bar_size))

    total_offset +=  48*(4+4+4+4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))

def parse_pcie_bin_dma(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    outfile.writelines("**************************************pcie dma debug**************************************\n")
    outfile.writelines('%-20s %-20s %-20s %-20s %-20s\n' %('dma_chan', 'dma_type', 'dma_action', 'cnt', 'last_time'))
    for i in range(0, 8): #dma chan
        for j in range(0, 4): #dma type
            for k in range(0, 3): #dma action
                (cnt, )            = struct.unpack('I', infile.read(4))
                (timestamp,   )    = struct.unpack('I', infile.read(4))
                if cnt > 0:
                    outfile.writelines('%-20s %-20s %-20s %-20d 0x%-18x\n' %(g_Pcie_DmaChanTable[i], g_Pcie_DmaTypeTable[j], g_Pcie_DmaActionTable[k], cnt, timestamp))
    total_offset +=  8*4*3*(4+4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))
    outfile.writelines("**************************************pcie dma trace**************************************\n")
    outfile.writelines('%-20s %-20s %-20s %-20s\n' %('timestamp', 'dma_chan', 'type_id', 'action_id'))

    trace_array = [[0] * 5 for _ in range(32)]
    for i in range(0, 32):#trace list
        (trace_array[i][0], )    = struct.unpack('I', infile.read(4)) #timestamp
        (trace_array[i][1], )    = struct.unpack('H', infile.read(2)) #dma_chan
        (trace_array[i][2], )    = struct.unpack('H', infile.read(2)) #type_id
        (trace_array[i][3], )    = struct.unpack('H', infile.read(2)) #act_id
        (trace_array[i][4], )    = struct.unpack('H', infile.read(2)) #reserve

    sort_array(32,trace_array,0)

    for i in range(0, 32):#trace list
        if trace_array[i][0] > 0:
        	outfile.writelines('0x%-18x %-20s %-20s %-20s\n' %(trace_array[i][0], g_Pcie_DmaChanTable[trace_array[i][1]], g_Pcie_DmaTypeTable[trace_array[i][2]], g_Pcie_DmaActionTable[trace_array[i][3]]))

    struct.unpack('I', infile.read(4))#trace-index
    total_offset +=  (32*(4+2+2+2+2) + 4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))


def parse_pcie_bin_boot(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    outfile.writelines("**************************************pcie boot debug**************************************\n")
    outfile.writelines('%-20s %-20s\n' %('boot_stage', 'time_stamp'))
    for i in range(0, 7):#boot_stage
        (time_stamp, )            = struct.unpack('I', infile.read(4))
        if time_stamp > 0:
            outfile.writelines('%-20s 0x%-18x\n' %(g_Pcie_BootStageTable[i], time_stamp))

    total_offset +=  7*4
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))

def parse_pcie_bin_cb(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    outfile.writelines("**************************************pcie callback debug**************************************\n")
    outfile.writelines('%-20s %-20s %-20s %-20s\n' %('user_id', 'cb_stage', 'cb_result', 'time_stamp'))
    for i in range(0, 14):#user_id
        for j in range(0, 8):#cb_stage
            (time_stamp, )            = struct.unpack('I', infile.read(4))
            (cb_result, )             = struct.unpack('I', infile.read(4))
            if time_stamp > 0:
                outfile.writelines('%-20s %-20s %-20d 0x%-18x\n' %(g_Pcie_UserEnumTable[i], g_Pcie_ModemCbTable[j], cb_result, time_stamp))

    total_offset +=  14*8*(4+4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))

def parse_pcie_bin_msg(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    outfile.writelines("**************************************pcie pm msg debug**************************************\n")
    outfile.writelines('%-20s %-20s %-20s %-20s\n' %('msg_id', 'msg_action', 'cnt', 'last_time'))
    for i in range(0, 4):#msg_id
        for j in range(0, 2):#msg_action
            (cnt, )            = struct.unpack('I', infile.read(4))
            (timestamp,   )    = struct.unpack('I', infile.read(4))
            if cnt > 0:
                if j == 0:#send
                    outfile.writelines('%-20s %-20s %-20s 0x%-18x\n' %(g_Pcie_ModemToApMsgTable[i], g_Pcie_MsgTypeTable[j], cnt, timestamp))
                else:
                    outfile.writelines('%-20s %-20s %-20s 0x%-18x\n' %(g_Pcie_ApToModemMsgTable[i], g_Pcie_MsgTypeTable[j], cnt, timestamp))
    total_offset +=  4*2*(4+4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))
    # 32
    outfile.writelines("**************************************pcie pm msg trace**************************************\n")
    outfile.writelines('%-20s %-20s %-20s\n' %('timestamp', 'msg_id', 'msg_action'))
    trace_array = [[0] * 3 for _ in range(32)]
    for i in range(0, 32):#trace list
        (trace_array[i][0], )    = struct.unpack('I', infile.read(4)) #timestamp
        (trace_array[i][1], )    = struct.unpack('H', infile.read(2)) #msg_id
        (trace_array[i][2], )    = struct.unpack('H', infile.read(2)) #msg_act

    sort_array(32,trace_array,0)

    for i in range(0, 32):#trace list
        if trace_array[i][0] > 0:
            if trace_array[i][2] == 0:#send
                outfile.writelines('0x%-18x %-20s %-20s\n' %(trace_array[i][0], g_Pcie_ModemToApMsgTable[trace_array[i][1]], g_Pcie_MsgTypeTable[trace_array[i][2]]))
            else:
                outfile.writelines('0x%-18x %-20s %-20s\n' %(trace_array[i][0], g_Pcie_ApToModemMsgTable[trace_array[i][1]], g_Pcie_MsgTypeTable[trace_array[i][2]]))

    outfile.writelines('\n\n')
    struct.unpack('I', infile.read(4))#trace-index
    total_offset +=  (32*(4+2+2) + 4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))

def parse_pcie_bin_iatu(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    outfile.writelines("**************************************pcie pm iatu recover debug**************************************\n")
    outfile.writelines('%-20s %-20s %-20s\n' %('bar_index', 'reg_offset', 'reg_val'))
    for i in range(0, 48):#bar_index
        for j in range(0, 9):#reg_offset
            (reg_val, )            = struct.unpack('I', infile.read(4))
            if reg_val > 0:
                outfile.writelines('%-20d 0x%-18x 0x%-18x\n' %(i, 4*j, reg_val))

    total_offset +=  48*9*4
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))

def parse_pcie_bin_dma_addr(fifo_type, infile, offset, outfile):
    infile.seek(offset)
    global total_offset
    outfile.writelines("**************************************pcie dma addr debug**************************************\n")
    outfile.writelines('%-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n' \
    %('timestamp', 'channel', 'trans_type', 'direction', 'size', 'sar_l', 'sar_h', 'dar_l', 'dar_h', 'dma_lli_addr_l', 'dma_lli_addr_h'))

    trace_array = [[0] * 12 for _ in range(32)]
    for i in range(0, 32):#trace list
        (trace_array[i][0], )   = struct.unpack('I', infile.read(4)) #dma_lli_addr_l
        (trace_array[i][1], )   = struct.unpack('I', infile.read(4)) #dma_lli_addr_H
        (trace_array[i][2], )   = struct.unpack('I', infile.read(4)) #transfer_type
        (trace_array[i][3], )   = struct.unpack('I', infile.read(4)) #64 bit reserve
        (trace_array[i][4], )   = struct.unpack('I', infile.read(4)) #timestamp
        (trace_array[i][5], )   = struct.unpack('I', infile.read(4)) #channel_id
        (trace_array[i][6], )   = struct.unpack('I', infile.read(4)) #direction
        (trace_array[i][7], )   = struct.unpack('I', infile.read(4)) #transfer_size
        (trace_array[i][8], )   = struct.unpack('I', infile.read(4)) #sar_low
        (trace_array[i][9], )   = struct.unpack('I', infile.read(4)) #sar_high
        (trace_array[i][10], )   = struct.unpack('I', infile.read(4)) #dar_low
        (trace_array[i][11], )   = struct.unpack('I', infile.read(4)) #dar_high

    sort_array(32,trace_array,4)

    for i in range(0, 32):#trace list
        if trace_array[i][4] > 0:
            outfile.writelines('0x%-18x %-20s %-20s %-20s 0x%-18x 0x%-18x 0x%-18x 0x%-18x 0x%-18x 0x%-18x 0x%-18x\n' \
            %(trace_array[i][4], g_Pcie_DmaChanTable[trace_array[i][5]], g_Pcie_DmaTransTable[trace_array[i][2]], g_Pcie_DmaDirectionTable[trace_array[i][6]], \
            trace_array[i][7], trace_array[i][8], trace_array[i][9], trace_array[i][10], trace_array[i][11], trace_array[i][0], trace_array[i][1]))

    outfile.writelines('\n\n')
    struct.unpack('I', infile.read(4))#trace-index
    total_offset +=  (32*4*11 + 4)
    outfile.writelines('total_offset: 0x%x\n\n' %(total_offset))

########################################################################################
def entry_0x3100009(infile, field, offset, len, version, mode, outfile):
        new_offset = eval(offset)
        global total_offset
        ########check parameter start#############
        if not field == '0x3100009':
            print(('hidis field is', field))
            print(('current field is', '0x3100009'))
            return error['ERR_CHECK_FIELD']
        elif not version == '0x0000':
            print(('hidis version is ', version))
            print(('current version is ', '0x0000'))
            return error['ERR_CHECK_VERSION']
        elif not len == '0x2800':
            print(('hids len is ', len))
            print(('current len is ', '0x2800'))
        #    return error['ERR_CHECK_LEN']
        #########check parameter end##############
        parse_pcie_bin_lock("lock_dbg",infile, new_offset + total_offset, outfile)
        parse_pcie_bin_state("state_dbg",infile, new_offset + total_offset, outfile)
        parse_pcie_bin_event("event_dbg",infile, new_offset + total_offset, outfile)
        parse_pcie_bin_gpio("gpio_dbg",infile, new_offset + total_offset, outfile)
        parse_pcie_bin_msi("gpio_dbg",infile, new_offset + total_offset, outfile)
        parse_pcie_bin_wakelock("wakelock_dbg",infile, new_offset + total_offset, outfile)
        parse_pcie_bin_vote_edge("vote_edge_dbg",infile, new_offset + total_offset, outfile)
        parse_pcie_bin_bar("bar_dbg",infile, new_offset + total_offset, outfile)
        parse_pcie_bin_dma("dma_dbg",infile, new_offset + total_offset, outfile)
        parse_pcie_bin_boot("boot_dbg",infile, new_offset + total_offset, outfile)
        parse_pcie_bin_cb("cb_dbg",infile, new_offset + total_offset, outfile)
        parse_pcie_bin_msg("msg_dbg",infile, new_offset + total_offset, outfile)
        parse_pcie_bin_iatu("iatu_dbg",infile, new_offset + total_offset, outfile)
        parse_pcie_bin_dma_addr("dma_addr_dbg",infile, new_offset + total_offset, outfile)
        return 0


#!/system/bin/sh
#
# This file is added for restarting xlogcat_service after sleeping 20s waiting for oba file
# Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
#
set -e

retval_image=$(getprop ro.image)
retval_bootmode=$(getprop ro.bootmode)
retval_runmode=$(getprop ro.runmode)
if [ "$retval_image" == "bootimage" ]&&[ "$retval_bootmode" != "charger" ]&&[ "$retval_runmode" != "factory" ];then
    sleep 20
    retval_remotedebug=$(getprop hwlog.remotedebug)
    if [ "$retval_remotedebug" == "true" ];then
        exit 1
    fi
    start xlogcat_service
fi
exit 0

#!/system/bin/sh

# Copyright (C) 2019 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

alias log_info="log -t art_apex -p i"
alias log_error="log -t art_apex -p f"

log_info "=== ART pre-boot integrity checks ==="

# Measure (and enable) fsverity to see if things are installed. Enable is not
# idempotent, and we'd need to parse the error string to see whether it says
# data was installed. Rather do a two-step.
FILES=`find /data/dalvik-cache -type f -a -name 'system@framework@boot*' -o name 'system@framework@*jar*'`

if [ ! -f "/system/bin/fsverity" ] ; then
  log_error "Device is not fsverity-enabled."
  rm -f $FILES
  exit 0
fi

for FILE in $FILES ; do
  if [ ! -f "$FILE" ] ; then
    continue # May have deleted already.
  fi

  # Check for fsverity protection.
  fsverity measure $FILE || \
    ENABLE_MSG=`fsverity enable $FILE 2>&1` || \
      {
        # No installed data, can't enable - clean up.
        # Note: to avoid side effects, only delete the tested files. To avoid
        #       understanding arches here, delete all, even if that may delete
        #       too aggressively.
        log_error "Enable failed: $ENABLE_MSG" ;
        rm -f $FILES ;
        exit 1 ;
      }

  # Check for integrity.
  INTEGRITY_MSG=`dd if=$FILE of=/dev/null bs=4k 2>&1` || \
    { log_error "Integrity failed: $INTEGRITY_MSG" ; rm -f $FILES ; exit 2 ; }
done

#!/system/bin/sh

DEST_PATH="/data/vendor/wakeup"
FILES_MOVED="/data/vendor/wakeup/wakeup_exist"
SRC_PATH="/vendor/wakeup"

if [ ! -f "$FILES_MOVED" ]; then
  cp -R "$SRC_PATH" "$DEST_PATH"
  restorecon -R "$DEST_PATH"
  echo 1 > "$FILES_MOVED"
fi
chmod -R 777 /data/vendor/wakeup

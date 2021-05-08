#!/system/bin/sh

# the odmf uid is 1094 before and old files remain the old uid
cd /data/odmf
find . -group 1094 -exec chgrp vendor_odmf {} \;
find . -group 2907 -exec chgrp vendor_odmf {} \;
exit 0


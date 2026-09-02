#!/bin/bash
# Screenshot every mirrored inventory page (after mirror-all.sh). Usage: bash brief/inventory/shot-all.sh
cd /home/user/ElmsNest
until grep -q ALL-MIRRORED brief/inventory/mirror-all.log 2>/dev/null; do sleep 5; done
export ENV2_PW_ROOT=/tmp/claude-0/-home-user-ElmsNest/1c2132db-077d-58e0-b54a-35f2ebea6b2c/scratchpad
ls -d brief/inventory/*/ | xargs -P 3 -I{} bash -c 'd={}; d=${d%/}; [ -f $d/index.html ] || exit 0; node brief/shot.js $d/index.html $d/shot > $d/shot.log 2>&1; echo "$(basename $d): $(tr "\n" " " < $d/shot.log)"'
echo ALL-SHOT

#!/bin/bash
# Faithful screenshots of every mirrored inventory page: served over localhost so Kalles' module JS runs
# (file:// renders leave every reveal-on-scroll product card at opacity 0). Usage: bash brief/inventory/shot-all-http.sh
cd /home/user/ElmsNest
export ENV2_PW_ROOT=${ENV2_PW_ROOT:-$(ls -d /tmp/claude-0/-home-user-ElmsNest/*/scratchpad | head -1)}
ls -d brief/inventory/*/ | xargs -P 3 -I{} bash -c 'd={}; d=${d%/}; [ -s $d/index.html ] || exit 0; node brief/shot-http.js $d/index.html $d/http > $d/shot-http.log 2>&1; echo "$(basename $d): $(tr "\n" " " < $d/shot-http.log | cut -c1-200)"'
python3 brief/inventory/sheets.py http
echo ALL-SHOT-HTTP

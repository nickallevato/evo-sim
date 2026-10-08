#!/bin/bash
# usage: get.sh name url
cd /home/na/projects/evo-sim/sources/raw/critics
code=$(curl -sL -m 40 -A "Mozilla/5.0 (X11; Linux x86_64) research-readonly" -o "$1" -w "%{http_code}" "$2")
echo "$1 $code $(stat -c%s $1) $2"
sleep 1

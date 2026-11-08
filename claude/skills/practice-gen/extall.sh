#!/bin/bash
# extall.sh <file> <extfile>
F=$1; X=$2
for s in GAP:50 MC:55 ERR:40 LCfill:45 LCcustom:45 LCmc:45 LCerror:45; do python3 /home/claude/gen/extend.py $F ${s%%:*} ${s##*:} $X; done

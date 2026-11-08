#!/bin/bash
# repush.sh <N> <slug>: reconstrueix i força push d'un PR existent; actualitza queue
set -e; N=$1; S=$2; W=/home/claude/wt
cd /home/claude/hubesol; git fetch -q origin main
cd $W; git reset -q --hard; git checkout -q -B claude/practice-$S origin/main
git reset -q --hard origin/main; git clean -fdq src; python3 /tmp/build_wt.py $S
npm run -s validate 2>&1 | grep -E "ERROR.*$S-practice" && { echo "VALIDATE FAIL"; exit 1; }
A=$(python3 claude/skills/audit_good.py . | awk -v s="## $S" '$0==s{f=1;next} /^## /{f=0} f'; python3 claude/skills/audit_good.py . | grep "^## $S:")
echo "$A" | grep -E "^  - |^## " | grep -vE "camp extra «kind»|tipus «[a-z]+» que no és a les mostres|^## $S: OK$" | grep . && { echo "AUDIT FAIL"; exit 1; }
git add -A src; git commit -q -m "fix $S

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01SgwMw9zkXMtGhzCr8qnfhN"
git push -q -f origin claude/practice-$S 2>&1 | grep -v "^remote:" || true
sed -i "/^$N /d" /home/claude/gen/queue.txt; echo "$N $S $(git rev-parse HEAD)" >> /home/claude/gen/queue.txt; echo "REPUSHED #$N"

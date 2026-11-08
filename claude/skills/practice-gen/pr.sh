#!/bin/bash
# pr.sh <slug> "<títol>" : build a la worktree, validate + audit, push, obre PR (no espera)
set -e
S=$1; TITLE=$2; REPO=cocohuguet8-ai/hubesol; W=/home/claude/wt
cd /home/claude/hubesol; git fetch -q origin main
[ -d $W ] || git worktree add -q $W origin/main
cd $W; git reset -q --hard; git checkout -q -B claude/practice-$S origin/main
[ -e node_modules ] || ln -s /home/claude/hubesol/node_modules node_modules
sed "s#^R = .*#R = '$W'#" /home/claude/gen/build.py > /tmp/build_wt.py
git reset -q --hard origin/main; git clean -fdq src; python3 /tmp/build_wt.py $S
npm run -s validate 2>&1 | grep -E "ERROR.*$S-practice" && { echo "VALIDATE FAIL"; exit 1; }
AUD=$(python3 claude/skills/audit_good.py . | awk -v s="## $S" '$0==s{f=1;next} /^## /{f=0} f' ; python3 claude/skills/audit_good.py . | grep "^## $S:")
echo "$AUD" | grep -E "^  - |^## " | grep -vE "camp extra «kind»|tipus «[a-z]+» que no és a les mostres|^## $S: OK$" | grep . && { echo "AUDIT FAIL"; exit 1; }
git add -A src
git commit -q -m "$TITLE

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01SgwMw9zkXMtGhzCr8qnfhN"
git push -q -f origin claude/practice-$S 2>&1 | grep -v "^remote:" || true
BODY="Lliçó reescrita al patró «good» (Past Simple / Past Continuous) + Practice 6 × 20. audit_good.py OK.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01SgwMw9zkXMtGhzCr8qnfhN"
N=$(gh api repos/$REPO/pulls -f title="$TITLE" -f head=claude/practice-$S -f base=main -f body="$BODY" --jq .number)
echo "$N $S $(git rev-parse HEAD)" >> /home/claude/gen/queue.txt
echo "PR #$N $S"

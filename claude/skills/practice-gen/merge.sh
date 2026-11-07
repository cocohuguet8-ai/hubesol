#!/bin/bash
# merge.sh : per cada PR de queue.txt, si els 3 checks són success → squash merge; si n'hi ha cap en failure → avisa
REPO=cocohuguet8-ai/hubesol
while read N S SHA; do
  [ -z "$N" ] && continue
  ST=$(gh api repos/$REPO/pulls/$N --jq '.merged')
  [ "$ST" = "true" ] && continue
  R=$(gh api repos/$REPO/commits/$SHA/check-runs --jq '[.check_runs[]|(.conclusion // "pending")]|join(",")')
  T=$(echo "$R" | tr ',' '\n' | grep -c .)
  if echo "$R" | grep -qE "failure|cancelled|timed_out"; then echo "FAIL #$N $S: $R"; continue; fi
  if [ "$T" -ge 3 ] && ! echo "$R" | grep -q pending; then
    gh api -X PUT repos/$REPO/pulls/$N/merge -f merge_method=squash --jq '"MERGED #'$N' '$S' " + (.merged|tostring)'
    gh api -X DELETE repos/$REPO/git/refs/heads/claude/practice-$S >/dev/null 2>&1
  else echo "WAIT #$N $S: $R"; fi
done < /home/claude/gen/queue.txt

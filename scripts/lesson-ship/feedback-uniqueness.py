#!/usr/bin/env python3
"""Feedback uniqueness gate for a HubESOL lesson.

No feedback string may be repeated within a section. Checks the quiz JSON
and the practice data (explanations, explain, wrongReasons, message,
wrongNote, orderHint). Empty strings are ignored.

Word-order / Level-check order items must have a non-empty orderHint.
The component must actually show that hint: pickOrderFeedback() in
WordOrder.astro and LevelCheck.astro must return the hint whenever it is
present. (On the 27/11 Past Simple preview, items 17 and 20 each had a
distinct orderHint in the JSON, but the learner saw the same diagnostic
«In a question, “Did” comes first, before the subject.» because the
component ignored the hint.)

Usage (from the repo root):

  python3 scripts/lesson-ship/feedback-uniqueness.py <slug>

Exit 0 = clean (paste the output in the PR).
Exit 1 = findings — blocks publish and blocks the 2b self-score.
Exit 2 = cannot run (missing files) — also blocks publish.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path


def fail_env(msg: str) -> int:
    print(msg, file=sys.stderr)
    return 2


def norm(s: str) -> str:
    s = s.replace("\u00a0", " ").strip()
    s = re.sub(r"\s+", " ", s)
    return s


def collect(section: str, loc: str, text, bucket: dict):
    if not isinstance(text, str):
        return
    t = norm(text)
    if not t:
        return
    bucket[section].append((loc, t))


def from_quiz(data, bucket):
    for i, it in enumerate(data.get("items") or [], 1):
        for j, exp in enumerate(it.get("explanations") or [], 1):
            collect("quiz", f"Quiz Q{i} explanation {j}", exp, bucket)


def from_practice(data, bucket):
    for i, q in enumerate((data.get("gapFill") or {}).get("questions") or [], 1):
        collect("gapFill", f"Gap-fill {i} explain", q.get("explain"), bucket)

    missing_hint = []
    for i, q in enumerate((data.get("wordOrder") or {}).get("sentences") or [], 1):
        hint = q.get("orderHint")
        if not (isinstance(hint, str) and norm(hint)):
            missing_hint.append(f"Put it in order {i}")
        collect("wordOrder", f"Put it in order {i} orderHint", hint, bucket)

    for i, q in enumerate((data.get("timedMC") or {}).get("questions") or [], 1):
        collect("timedMC", f"Beat the clock Q{i} explain", q.get("explain"), bucket)
        for j, r in enumerate(q.get("wrongReasons") or [], 1):
            collect("timedMC", f"Beat the clock Q{i} wrongReason {j}", r, bucket)

    for i, it in enumerate((data.get("errorCorrection") or {}).get("items") or [], 1):
        collect("errorCorrection", f"Find the mistake {i} message", it.get("message"), bucket)

    for i, it in enumerate((data.get("levelCheck") or {}).get("items") or [], 1):
        loc = f"Level check Q{i}"
        collect("levelCheck", f"{loc} explain", it.get("explain"), bucket)
        collect("levelCheck", f"{loc} wrongNote", it.get("wrongNote"), bucket)
        collect("levelCheck", f"{loc} message", it.get("message"), bucket)
        collect("levelCheck", f"{loc} orderHint", it.get("orderHint"), bucket)
        for j, r in enumerate(it.get("wrongReasons") or [], 1):
            collect("levelCheck", f"{loc} wrongReason {j}", r, bucket)
        if it.get("type") == "order" and not (isinstance(it.get("orderHint"), str) and norm(it.get("orderHint") or "")):
            missing_hint.append(f"{loc} (order)")
    return missing_hint


def pick_order_feedback_ok(src: str) -> bool:
    """True iff pickOrderFeedback returns the hint whenever one is present."""
    m = re.search(r"function\s+pickOrderFeedback\s*\(([^)]*)\)\s*\{", src)
    if not m:
        return False
    start = m.end()
    # naive brace match
    depth, i = 1, start
    while i < len(src) and depth:
        if src[i] == "{":
            depth += 1
        elif src[i] == "}":
            depth -= 1
        i += 1
    body = src[start:i - 1]
    params = [p.strip() for p in m.group(1).split(",")]
    hint = params[1] if len(params) > 1 else "hint"
    # first meaningful statement must be: if (hint) return hint;
    body_nc = re.sub(r"//.*?$", "", body, flags=re.M)
    body_nc = re.sub(r"/\*.*?\*/", "", body_nc, flags=re.S).strip()
    pattern = rf"^if\s*\(\s*{re.escape(hint)}\s*(?:&&\s*{re.escape(hint)}\s*\.trim\s*\(\s*\))?\s*\)\s*return\s+{re.escape(hint)}\s*;"
    return re.match(pattern, body_nc) is not None


def check_components(repo: Path) -> list[str]:
    findings = []
    for rel in (
        "src/components/practice/WordOrder.astro",
        "src/components/practice/LevelCheck.astro",
    ):
        p = repo / rel
        if not p.is_file():
            findings.append(f"[component] missing {rel} — cannot prove orderHint is shown")
            continue
        src = p.read_text(encoding="utf-8")
        if "function pickOrderFeedback" not in src:
            findings.append(f"[component] {rel} has no pickOrderFeedback()")
            continue
        if not pick_order_feedback_ok(src):
            findings.append(
                f"[component] {rel}: pickOrderFeedback() does not return the item's "
                "orderHint whenever one is present, so two items can show the same "
                "diagnostic (e.g. «In a question, “Did” comes first, before the subject.»). "
                "First line of the function must be: if (hint) return hint;"
            )
    return findings


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--quiz")
    ap.add_argument("--practice")
    args = ap.parse_args(argv)

    repo = Path(args.repo).resolve()
    slug = args.slug
    quiz_p = Path(args.quiz) if args.quiz else repo / "src/data/quizzes" / f"{slug}-quiz-1.json"
    prac_p = Path(args.practice) if args.practice else repo / "src/data/practice" / f"{slug}-practice.json"

    print(f"=== feedback uniqueness: {slug} ===")
    if not quiz_p.is_file():
        return fail_env(f"Quiz JSON not found: {quiz_p}")
    if not prac_p.is_file():
        return fail_env(f"Practice JSON not found: {prac_p}")

    bucket: dict[str, list[tuple[str, str]]] = defaultdict(list)
    from_quiz(json.loads(quiz_p.read_text(encoding="utf-8")), bucket)
    missing_hint = from_practice(json.loads(prac_p.read_text(encoding="utf-8")), bucket)

    findings: list[str] = []
    for loc in missing_hint:
        findings.append(f"[missing-orderHint] {loc} has no orderHint; the component will show a shared fallback")

    for section, items in bucket.items():
        seen: dict[str, list[str]] = defaultdict(list)
        for loc, text in items:
            seen[text].append(loc)
        for text, locs in seen.items():
            if len(locs) > 1:
                preview = text if len(text) <= 140 else text[:137] + "…"
                findings.append(
                    f"[duplicate-feedback] section «{section}»: «{preview}» used in "
                    + "; ".join(locs)
                )

    findings.extend(check_components(repo))

    n = sum(len(v) for v in bucket.values())
    print(f"checked {n} non-empty feedback strings across {len(bucket)} sections")

    if findings:
        print(f"FINDINGS ({len(findings)}):")
        for f in findings:
            print("  - " + f)
        print(f"RESULT: FAIL ({len(findings)} findings)")
        return 1
    print("FINDINGS: none")
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

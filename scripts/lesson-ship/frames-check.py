#!/usr/bin/env python3
"""Frame-table and Find-the-mistake context gate for a HubESOL lesson.

Reads docs/verificacio/<slug>-frames.md (committed, pasted in the PR).

Required markdown table, one row per item in the whole lesson (quiz + every
practice section), with exactly these headers (any capitalisation):

  | section | item | time marker | structure | error type | frame |

Hard rules (any breach is a FAIL):
  • no duplicate «frame» value anywhere in the lesson
  • the same «error type» at most twice in one section
  • a frame must never be repeated (even with a different error type)

Also requires a section «## Why no context makes this correct» with one line
per Find the mistake / Level check error item, of the form:

  - Find the mistake 7: Why no context makes this correct: …

and flags banned ambiguous time expressions in those wrong sentences
(e.g. «a week before», «two days before» with no following noun).

Usage (from the repo root):

  python3 scripts/lesson-ship/frames-check.py <slug>

Exit 0 = clean (paste the table and this output in the PR).
Exit 1 = findings — blocks publish and blocks the 2b self-score.
Exit 2 = cannot run (missing file or unreadable table) — also blocks publish.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REQUIRED_COLS = ["section", "item", "time marker", "structure", "error type", "frame"]
WHY_RE = re.compile(
    r"^[-*]\s*(Find the mistake|Spot the mistake|Level check)\s*(\d+)\s*:\s*"
    r"Why no context makes this correct\s*:",
    re.I,
)
BANNED_BEFORE_RE = re.compile(
    r"\b(?:(?:a|an|one|two|three|four|five|six|seven|eight|nine|ten|\d+)\s+)?"
    r"(?:week|weeks|day|days|month|months|year|years|hour|hours|minute|minutes)\s+before\s*[.?!]?\s*$",
    re.I,
)
SECTION_ALIASES = {
    "quiz": "quiz",
    "gap-fill": "gapFill",
    "gap fill": "gapFill",
    "fill the gaps": "gapFill",
    "fill-the-gaps": "gapFill",
    "put it in order": "wordOrder",
    "word order": "wordOrder",
    "matching": "matching",
    "beat the clock": "timedMC",
    "timed mc": "timedMC",
    "find the mistake": "errorCorrection",
    "spot the mistake": "errorCorrection",
    "error correction": "errorCorrection",
    "level check": "levelCheck",
}


def fail_env(msg: str) -> int:
    print(msg, file=sys.stderr)
    return 2


def norm(s: str) -> str:
    s = s.replace("\u00a0", " ").strip().strip("*")
    s = re.sub(r"\s+", " ", s)
    return s


def norm_key(s: str) -> str:
    return norm(s).casefold()


def parse_table(md: str) -> tuple[list[str], list[dict[str, str]]]:
    rows: list[dict[str, str]] = []
    headers: list[str] | None = None
    for raw in md.splitlines():
        line = raw.strip()
        if not line.startswith("|"):
            continue
        cells = [norm(c) for c in line.strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells if c):
            continue
        if headers is None:
            headers = [h.casefold() for h in cells]
            continue
        if len(cells) < len(headers):
            cells.extend([""] * (len(headers) - len(cells)))
        rows.append(dict(zip(headers, cells)))
    return headers or [], rows


def expected_counts(practice: dict, quiz: dict) -> dict[str, int]:
    return {
        "quiz": len((quiz or {}).get("items") or []),
        "gapFill": len(((practice or {}).get("gapFill") or {}).get("questions") or []),
        "wordOrder": len(((practice or {}).get("wordOrder") or {}).get("sentences") or []),
        "matching": len(((practice or {}).get("matching") or {}).get("pairs") or []),
        "timedMC": len(((practice or {}).get("timedMC") or {}).get("questions") or []),
        "errorCorrection": len(((practice or {}).get("errorCorrection") or {}).get("items") or []),
        "levelCheck": len(((practice or {}).get("levelCheck") or {}).get("items") or []),
    }


def section_key(label: str) -> str:
    return SECTION_ALIASES.get(norm_key(label), norm_key(label))


def why_lines(md: str) -> dict[tuple[str, int], str]:
    found: dict[tuple[str, int], str] = {}
    for line in md.splitlines():
        m = WHY_RE.match(line.strip())
        if not m:
            continue
        kind = "errorCorrection" if "mistake" in m.group(1).casefold() else "levelCheck"
        found[(kind, int(m.group(2)))] = line.strip()
    return found


def error_sentences(practice: dict) -> list[tuple[str, int, str]]:
    out = []
    for i, it in enumerate(((practice or {}).get("errorCorrection") or {}).get("items") or [], 1):
        out.append(("errorCorrection", i, " ".join(it.get("tokens") or [])))
    for i, it in enumerate(((practice or {}).get("levelCheck") or {}).get("items") or [], 1):
        if "errorIndex" in it and it.get("tokens"):
            out.append(("levelCheck", i, " ".join(it.get("tokens") or [])))
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--frames", help="path to the frame table markdown")
    ap.add_argument("--practice")
    ap.add_argument("--quiz")
    args = ap.parse_args(argv)

    repo = Path(args.repo).resolve()
    slug = args.slug
    frames_p = Path(args.frames) if args.frames else repo / "docs/verificacio" / f"{slug}-frames.md"
    quiz_p = Path(args.quiz) if args.quiz else repo / "src/data/quizzes" / f"{slug}-quiz-1.json"
    prac_p = Path(args.practice) if args.practice else repo / "src/data/practice" / f"{slug}-practice.json"

    print(f"=== frame check: {slug} ===")
    if not frames_p.is_file():
        return fail_env(
            f"Frame table not found: {frames_p}\n"
            "Commit docs/verificacio/<slug>-frames.md with one row per item "
            "(columns: section | item | time marker | structure | error type | frame) "
            "and a «Why no context makes this correct» section for every Find/Spot the mistake item."
        )

    md = frames_p.read_text(encoding="utf-8")
    headers, rows = parse_table(md)
    missing = [c for c in REQUIRED_COLS if c not in headers]
    if missing or not rows:
        return fail_env(
            f"{frames_p} has no usable table, or is missing columns {missing}. "
            f"Found headers: {headers or '(none)'}."
        )
    print(f"table: {frames_p} ({len(rows)} rows)")

    findings: list[str] = []

    # empty frames
    for r in rows:
        if not r.get("frame"):
            findings.append(f"[empty-frame] {r.get('section')} {r.get('item')} has an empty frame column")

    # duplicate frames (whole lesson)
    by_frame: dict[str, list[str]] = defaultdict(list)
    for r in rows:
        fr = norm_key(r.get("frame") or "")
        if not fr:
            continue
        by_frame[fr].append(f"{r.get('section')} {r.get('item')}")
    for fr, locs in by_frame.items():
        if len(locs) > 1:
            findings.append(f"[duplicate-frame] «{fr}» used in: " + "; ".join(locs))

    # error type at most twice per section
    counts: dict[str, Counter] = defaultdict(Counter)
    for r in rows:
        typ = norm_key(r.get("error type") or "")
        if typ:
            counts[norm_key(r.get("section") or "")][typ] += 1
    for sec, ctr in counts.items():
        for typ, n in ctr.items():
            if n > 2:
                findings.append(
                    f"[error-type-overuse] section «{sec}»: error type «{typ}» appears {n} times (max 2)"
                )

    practice = json.loads(prac_p.read_text(encoding="utf-8")) if prac_p.is_file() else None
    quiz = json.loads(quiz_p.read_text(encoding="utf-8")) if quiz_p.is_file() else None
    if practice is None:
        findings.append(f"[files] practice JSON not found: {prac_p}")
    if quiz is None:
        findings.append(f"[files] quiz JSON not found: {quiz_p}")

    if practice is not None and quiz is not None:
        expected = expected_counts(practice, quiz)
        got = Counter(section_key(r.get("section") or "") for r in rows)
        for sec, n in expected.items():
            g = got.get(sec, 0)
            if g != n:
                findings.append(
                    f"[coverage] section «{sec}»: table has {g} row(s), data files have {n} item(s)"
                )

        why = why_lines(md)
        for kind, num, sentence in error_sentences(practice):
            if (kind, num) not in why:
                label = "Find the mistake" if kind == "errorCorrection" else "Level check"
                findings.append(
                    f"[why-no-context] missing line for {label} {num} "
                    f"(«{sentence}»). Write: «- {label} {num}: Why no context makes this correct: …»"
                )
            if BANNED_BEFORE_RE.search(sentence.strip()):
                label = "Find the mistake" if kind == "errorCorrection" else "Level check"
                findings.append(
                    f"[banned-ambiguity] {label} {num}: «{sentence}» ends with a duration + «before» "
                    "and can be read as correct English (a week before the wedding…). Rewrite."
                )

        heading = re.search(r"^##\s+Why no context makes this correct\s*$", md, re.I | re.M)
        if not heading:
            findings.append(
                "[why-no-context] file has no «## Why no context makes this correct» section"
            )

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

#!/usr/bin/env python3
"""Feedback uniqueness gate for a HubESOL lesson.

No feedback string may be repeated within a section. Checks every quiz JSON
for the lesson ({slug}-quiz-*.json) and the practice data (explanations,
explain, wrongReasons, message, wrongNote, orderHint). Empty strings are
ignored. Duplicates are compared case-insensitively and ignoring trailing
punctuation, curly/straight quotes and extra spaces ("Correct." == "correct").

Word-order / Level-check order items must have a non-empty orderHint.
The component must actually show that hint: pickOrderFeedback() in
WordOrder.astro and LevelCheck.astro must return the hint whenever it is
present. (On the 27/11 Past Simple preview, items 17 and 20 each had a
distinct orderHint in the JSON, but the learner saw the same diagnostic
«In a question, “Did” comes first, before the subject.» because the
component ignored the hint.)

Usage (from the repo root, or pass --repo):

  python3 scripts/lesson-ship/feedback-uniqueness.py <slug>

Exit 0 = clean (paste the output in the PR).
Exit 1 = findings — blocks publish and blocks the 2b self-score.
Exit 2 = cannot run (missing/broken files, unexpected error) — also blocks publish.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

COMPONENTS = (
    "src/components/practice/WordOrder.astro",
    "src/components/practice/LevelCheck.astro",
)


class EnvError(Exception):
    """Cannot run → exit 2."""


# ---------- text helpers ----------

def norm(s: str) -> str:
    """Display form: NBSP/odd spaces collapsed, trimmed."""
    s = s.replace(" ", " ").replace(" ", " ")
    return re.sub(r"\s+", " ", s).strip()


def key(s: str) -> str:
    """Comparison form: also case-, quote- and trailing-punctuation-insensitive."""
    s = norm(s).casefold()
    s = s.translate(str.maketrans({"“": '"', "”": '"', "‘": "'", "’": "'", "«": '"', "»": '"'}))
    return re.sub(r"[\s.!?;:,…]+$", "", s)


def has_text(v) -> bool:
    return isinstance(v, str) and bool(norm(v))


def as_dict(v) -> dict:
    return v if isinstance(v, dict) else {}


def as_list(v) -> list:
    return v if isinstance(v, list) else []


def load_json(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise EnvError(f"Invalid JSON in {p}: line {e.lineno}, col {e.colno}: {e.msg}")
    except OSError as e:
        raise EnvError(f"Cannot read {p}: {e}")


# ---------- collection ----------

def collect(section, loc, text, bucket):
    if has_text(text):
        bucket[section].append((loc, norm(text)))


def from_quiz(name, data, bucket):
    for i, it in enumerate(as_list(as_dict(data).get("items")), 1):
        for j, exp in enumerate(as_list(as_dict(it).get("explanations")), 1):
            collect(name, f"{name} Q{i} explanation {j}", exp, bucket)


def from_practice(data, bucket) -> list[str]:
    if not isinstance(data, dict):
        raise EnvError("Practice JSON must be an object at the top level")
    for sec, sub in (("gapFill", "questions"), ("wordOrder", "sentences"), ("timedMC", "questions"),
                     ("errorCorrection", "items"), ("levelCheck", "items")):
        if sec in data and data[sec] is not None:
            if not isinstance(data[sec], dict) or not isinstance(data[sec].get(sub, []), list):
                raise EnvError(f"Practice JSON: «{sec}» should be an object with a «{sub}» list — "
                               "shape changed, so it cannot be checked")
    missing = []

    for i, q in enumerate(as_list(as_dict(data.get("gapFill")).get("questions")), 1):
        collect("gapFill", f"Gap-fill {i} explain", as_dict(q).get("explain"), bucket)

    for i, q in enumerate(as_list(as_dict(data.get("wordOrder")).get("sentences")), 1):
        hint = as_dict(q).get("orderHint")
        if not has_text(hint):
            missing.append(f"Put it in order {i}")
        collect("wordOrder", f"Put it in order {i} orderHint", hint, bucket)

    for i, q in enumerate(as_list(as_dict(data.get("timedMC")).get("questions")), 1):
        q = as_dict(q)
        collect("timedMC", f"Beat the clock Q{i} explain", q.get("explain"), bucket)
        for j, r in enumerate(as_list(q.get("wrongReasons")), 1):
            collect("timedMC", f"Beat the clock Q{i} wrongReason {j}", r, bucket)

    for i, it in enumerate(as_list(as_dict(data.get("errorCorrection")).get("items")), 1):
        collect("errorCorrection", f"Find the mistake {i} message", as_dict(it).get("message"), bucket)

    for i, it in enumerate(as_list(as_dict(data.get("levelCheck")).get("items")), 1):
        it = as_dict(it)
        loc = f"Level check Q{i}"
        for field in ("explain", "wrongNote", "message", "orderHint"):
            collect("levelCheck", f"{loc} {field}", it.get(field), bucket)
        for j, r in enumerate(as_list(it.get("wrongReasons")), 1):
            collect("levelCheck", f"{loc} wrongReason {j}", r, bucket)
        if "order" in str(it.get("type", "")).lower() and not has_text(it.get("orderHint")):
            missing.append(f"{loc} (order)")
    return missing


# ---------- component check ----------

def strip_comments(src: str) -> str:
    """Remove // and /* */ comments, leaving string/template contents intact."""
    out, i, n = [], 0, len(src)
    while i < n:
        c = src[i]
        if c in "\"'`":
            j = i + 1
            while j < n and src[j] != c:
                j += 2 if src[j] == "\\" else 1
            out.append(src[i:j + 1]); i = j + 1
        elif src.startswith("//", i):
            j = src.find("\n", i); i = n if j < 0 else j
        elif src.startswith("/*", i):
            j = src.find("*/", i + 2); i = n if j < 0 else j + 2
        else:
            out.append(c); i += 1
    return "".join(out)


def match_close(src: str, start: int, open_ch: str, close_ch: str) -> int:
    """Index just after the bracket closing the one opened before `start`; skips strings."""
    depth, i, n = 1, start, len(src)
    while i < n and depth:
        c = src[i]
        if c in "\"'`":
            j = i + 1
            while j < n and src[j] != c:
                j += 2 if src[j] == "\\" else 1
            i = j + 1
            continue
        if c == open_ch:
            depth += 1
        elif c == close_ch:
            depth -= 1
        i += 1
    return i if depth == 0 else -1


def find_function(src: str):
    """Return (param_names, body) for pickOrderFeedback, or None.

    Supports: function / async function / const x = function / const x = (...) => {...},
    with or without TypeScript annotations.
    """
    m = re.search(
        r"(?:function\s+pickOrderFeedback\s*(?:<[^>]*>)?\s*\("
        r"|(?:const|let|var)\s+pickOrderFeedback\s*(?::[^=]+)?=\s*(?:async\s*)?(?:function\s*)?\()",
        src,
    )
    if not m:
        return None
    p_end = match_close(src, m.end(), "(", ")")
    if p_end < 0:
        return None
    raw_params = src[m.end():p_end - 1]
    brace = src.find("{", p_end)  # skips ": string" / "=>"
    if brace < 0:
        return None
    b_end = match_close(src, brace + 1, "{", "}")
    if b_end < 0:
        return None
    names = []
    for p in split_top(raw_params):
        name = re.match(r"\s*(?:\.\.\.)?([A-Za-z_$][\w$]*)", p)
        if name:
            names.append(name.group(1))
    return names, src[brace + 1:b_end - 1]


def split_top(s: str) -> list[str]:
    """Split params on top-level commas (ignores commas inside <>, (), {}, [])."""
    parts, depth, cur = [], 0, ""
    for c in s:
        if c in "<({[":
            depth += 1
        elif c in ">)}]":
            depth -= 1
        if c == "," and depth == 0:
            parts.append(cur); cur = ""
        else:
            cur += c
    if cur.strip():
        parts.append(cur)
    return parts


def returns_hint_first(body: str, h: str) -> bool:
    """First statement must return the hint whenever it is non-empty."""
    b = re.sub(r"\s+", " ", body).strip()
    H = re.escape(h)
    cond = rf"(?:{H}|{H}\s*\?\.\s*trim\s*\(\s*\)|{H}\s*&&\s*{H}\s*\??\.\s*trim\s*\(\s*\)|{H}\s*\??\.\s*trim\s*\(\s*\)\s*\.\s*length(?:\s*>\s*0)?)"
    ret = rf"return\s+{H}(?:\s*\??\.\s*trim\s*\(\s*\))?\s*;?"
    forms = (
        rf"^if\s*\(\s*{cond}\s*\)\s*{ret}",                 # if (hint) return hint;
        rf"^if\s*\(\s*{cond}\s*\)\s*\{{\s*{ret}\s*\}}",     # if (hint) { return hint; }
        rf"^return\s+(?:\(\s*)?{H}(?:\s*\??\.\s*trim\s*\(\s*\))?\s*(?:\)\s*)?\|\|",  # return hint || fallback
    )
    return any(re.match(f, b) for f in forms)


def check_components(repo: Path) -> tuple[list[str], list[str]]:
    findings, warnings = [], []
    for rel in COMPONENTS:
        p = repo / rel
        if not p.is_file():
            raise EnvError(f"Component not found: {p} (wrong --repo or not run from repo root?)")
        src = strip_comments(p.read_text(encoding="utf-8"))
        fn = find_function(src)
        if fn is None:
            findings.append(f"[component] {rel} has no pickOrderFeedback() (or it could not be parsed)")
            continue
        params, body = fn
        # The hint parameter: one whose name contains "hint"; else the 2nd param.
        hint = next((n for n in params if "hint" in n.lower()), params[1] if len(params) > 1 else None)
        if hint is None:
            findings.append(
                f"[component] {rel}: pickOrderFeedback({', '.join(params)}) has no hint parameter, "
                "so it cannot show the item's orderHint"
            )
        elif not returns_hint_first(body, hint):
            findings.append(
                f"[component] {rel}: pickOrderFeedback() does not return «{hint}» first whenever it is "
                "present, so two items can show the same diagnostic "
                "(e.g. «In a question, “Did” comes first, before the subject.»). "
                f"First statement must be: if ({hint}) return {hint};"
            )
        # Non-blocking: is the item's orderHint actually passed in at a call site?
        calls = re.findall(r"pickOrderFeedback\s*\(([^;\n]*)", src)
        if not any("orderHint" in c for c in calls):
            warnings.append(
                f"[component] {rel}: no pickOrderFeedback(...) call passes «orderHint» directly — "
                "check by hand that the item's orderHint reaches the function"
            )
    return findings, warnings


# ---------- main ----------

def run(args) -> int:
    repo = Path(args.repo).resolve()
    slug = args.slug
    print(f"=== feedback uniqueness: {slug} ===")

    if args.quiz:
        quiz_paths = [Path(q) for q in args.quiz]
    else:
        quiz_paths = sorted((repo / "src/data/quizzes").glob(f"{slug}-quiz-*.json"))
    prac_p = Path(args.practice) if args.practice else repo / "src/data/practice" / f"{slug}-practice.json"

    if not quiz_paths:
        raise EnvError(f"No quiz JSON found: {repo / 'src/data/quizzes'}/{slug}-quiz-*.json")
    for q in quiz_paths:
        if not q.is_file():
            raise EnvError(f"Quiz JSON not found: {q}")
    if not prac_p.is_file():
        raise EnvError(f"Practice JSON not found: {prac_p}")

    bucket: dict = defaultdict(list)
    for q in quiz_paths:
        m = re.search(r"-quiz-(\w+)\.json$", q.name)
        from_quiz(f"quiz-{m.group(1)}" if m else q.stem, load_json(q), bucket)
    missing = from_practice(load_json(prac_p), bucket)

    findings = [f"[missing-orderHint] {loc} has no orderHint; the component will show a shared fallback"
                for loc in missing]

    for section, items in bucket.items():
        seen: dict = defaultdict(list)
        first_text: dict = {}
        for loc, text in items:
            k = key(text)
            seen[k].append(loc)
            first_text.setdefault(k, text)
        for k, locs in seen.items():
            if len(locs) > 1:
                t = first_text[k]
                preview = t if len(t) <= 140 else t[:137] + "…"
                findings.append(f"[duplicate-feedback] section «{section}»: «{preview}» used in " + "; ".join(locs))

    comp_findings, warnings = check_components(repo)
    findings.extend(comp_findings)

    n = sum(len(v) for v in bucket.values())
    print(f"checked {n} non-empty feedback strings across {len(bucket)} sections "
          f"({', '.join(p.name for p in quiz_paths)}, {prac_p.name})")
    for w in warnings:
        print("WARNING (does not block): " + w)

    if findings:
        print(f"FINDINGS ({len(findings)}):")
        for f in findings:
            print("  - " + f)
        print(f"RESULT: FAIL ({len(findings)} findings)")
        return 1
    print("FINDINGS: none")
    print("RESULT: PASS")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--quiz", action="append", help="quiz JSON path (repeatable); default: all {slug}-quiz-*.json")
    ap.add_argument("--practice")
    args = ap.parse_args(argv)
    try:
        return run(args)
    except EnvError as e:
        print(f"CANNOT RUN: {e}", file=sys.stderr)
        print("RESULT: ERROR (exit 2)")
        return 2
    except Exception as e:  # never let a crash look like "findings" (exit 1)
        print(f"CANNOT RUN: unexpected {type(e).__name__}: {e}", file=sys.stderr)
        print("RESULT: ERROR (exit 2)")
        return 2


if __name__ == "__main__":
    sys.exit(main())

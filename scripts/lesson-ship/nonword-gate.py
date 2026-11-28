#!/usr/bin/env python3
"""Non-word and typo-of-key gate for a HubESOL lesson.

Extracts every option, answer and Find-the-mistake error token from the
lesson quiz JSON and practice data, checks them against a word list plus
allowlists, and flags any selectable option that is a misspelling of the
correct answer (Levenshtein distance 1 or 2). Also scans the lesson
markdown: invented forms may appear only in «Common mistakes» and only
on a line marked ✗.

Usage (from the repo root):

  python3 scripts/lesson-ship/nonword-gate.py <slug>
  python3 scripts/lesson-ship/nonword-gate.py past-simple --lesson src/content/lessons/verb-tenses/past-simple.md

Exit 0 = clean (paste the output in the PR).
Exit 1 = findings — blocks publish and blocks the 2b self-score.
Exit 2 = cannot run (missing word list or files) — also blocks publish.
A missing word list is not a pass.

Word-list search order:
  1. --wordlist PATH, or the environment variable HUBESOL_WORDLIST
  2. /usr/share/dict/words (or american-english / british-english in that folder)
     Debian/Ubuntu: apt install wamerican    macOS: usually already present
  3. pip package wordfreq, top 50,000 English words
     (python3 -m venv .venv && .venv/bin/pip install wordfreq)
  4. pip package english-words (web2) — last resort only; it misses some
     inflections (e.g. «planned»). The script warns if it has to use it.

Allowlists (optional, one token per line, # comments allowed):
  scripts/lesson-ship/allowlist.txt
  docs/verificacio/<slug>-allowlist.txt
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

TOKEN_RE = re.compile(r"[A-Za-z]+(?:[''][A-Za-z]+)?")
APOS = dict.fromkeys(map(ord, "‘’‛′`"), "'")
COMMON_MISTAKES_RE = re.compile(r"^##\s+common\s+mistakes\b", re.I)
HEADING_RE = re.compile(r"^##\s+")
MIN_TYPO_LEN = 5
# Real irregular forms that wordfreq's top 50k sometimes omits.
# typo-of-key still applies; this list does not excuse «planed».
WORDLIST_SUPPLEMENT = {
    "swum", "wrung", "stunk", "mown", "slunk", "shod", "dreamt", "learnt",
    "spoilt", "burnt", "leant", "smelt", "spelt", "spilt", "dwelt",
}

DICT_CANDIDATES = (
    Path("/usr/share/dict/words"),
    Path("/usr/share/dict/american-english"),
    Path("/usr/share/dict/british-english"),
    Path("/usr/dict/words"),
)


def fail_env(msg: str) -> int:
    print(msg, file=sys.stderr)
    return 2


def norm_token(s: str) -> str:
    s = unicodedata.normalize("NFC", s).translate(APOS).strip()
    return s


def tokenize(text: str) -> list[str]:
    text = norm_token(strip_html(text or ""))
    return [m.group(0) for m in TOKEN_RE.finditer(text)]


def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", " ", text)


def fold(s: str) -> str:
    return norm_token(s).lower()


def levenshtein(a: str, b: str) -> int:
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)
    if abs(len(a) - len(b)) > 2:
        return 99
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            ins, delete, sub = cur[j - 1] + 1, prev[j] + 1, prev[j - 1] + (ca != cb)
            cur.append(min(ins, delete, sub))
        prev = cur
    return prev[-1]


def _ed_or_ing(w: str) -> str | None:
    if w.endswith("ing"):
        return "ing"
    if w.endswith("ied") or w.endswith("ed"):
        return "ed"
    return None


def typo_of(token: str, key: str) -> int | None:
    """Return distance if token is a misspelling of key, else None.

    Only fires for two -ed forms or two -ing forms with edit distance 1 or 2
    (planed/planned, stoped/stopped, hoped/hopped, studyed/studied,
    runing/running). This does *not* flag legitimate tense pairs
    (watch/watched, drive/drove, don’t see/didn’t see, see/saw).
    Non-words that are not -ed/-ing variants (goed, buyed, will can)
    are still caught by the word-list check.
    """
    a, b = fold(token), fold(key)
    if a == b:
        return None
    if min(len(a), len(b)) < MIN_TYPO_LEN:
        return None
    if _ed_or_ing(a) is None or _ed_or_ing(a) != _ed_or_ing(b):
        return None
    d = levenshtein(a, b)
    return d if 1 <= d <= 2 else None


# ---------------------------------------------------------------------------
# Word list
# ---------------------------------------------------------------------------

def load_wordlist_file(path: Path) -> set[str]:
    words: set[str] = set()
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        words.add(fold(line))
    return words


def load_allowlist(path: Path) -> set[str]:
    words: set[str] = set()
    if not path.is_file():
        return words
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            words.add(fold(line))
    return words


def load_wordlist(explicit: Path | None) -> tuple[set[str], str, list[str]]:
    warnings: list[str] = []
    if explicit:
        if not explicit.is_file():
            raise FileNotFoundError(f"word list not found: {explicit}")
        return load_wordlist_file(explicit), str(explicit), warnings
    env = (Path(__import__("os").environ["HUBESOL_WORDLIST"])
           if __import__("os").environ.get("HUBESOL_WORDLIST") else None)
    if env:
        if not env.is_file():
            raise FileNotFoundError(f"HUBESOL_WORDLIST not found: {env}")
        return load_wordlist_file(env), f"HUBESOL_WORDLIST={env}", warnings
    for cand in DICT_CANDIDATES:
        if cand.is_file():
            return load_wordlist_file(cand), str(cand), warnings
    try:
        from wordfreq import top_n_list
        words = {fold(w) for w in top_n_list("en", 50000)}
        return words, "wordfreq.top_n_list('en', 50000)", warnings
    except Exception:
        pass
    try:
        from english_words import get_english_words_set
        words = {fold(w) for w in get_english_words_set(["web2"], lower=True)}
        warnings.append(
            "Using english-words (web2) as a last resort; it misses some "
            "inflections (e.g. «planned»). Prefer /usr/share/dict/words "
            "(apt install wamerican) or: pip install wordfreq."
        )
        return words, "english_words.get_english_words_set(['web2'])", warnings
    except Exception:
        pass
    raise FileNotFoundError(
        "No word list found. Install one of:\n"
        "  • apt install wamerican   (provides /usr/share/dict/words)\n"
        "  • pip install wordfreq    (in a venv)\n"
        "  • pass --wordlist PATH    or set HUBESOL_WORDLIST\n"
        "A missing word list is a FAIL (exit 2), not a pass."
    )


# ---------------------------------------------------------------------------
# File discovery
# ---------------------------------------------------------------------------

def discover(slug: str, repo: Path, kind: str) -> Path | None:
    if kind == "quiz":
        p = repo / "src/data/quizzes" / f"{slug}-quiz-1.json"
        return p if p.is_file() else None
    if kind == "practice":
        p = repo / "src/data/practice" / f"{slug}-practice.json"
        return p if p.is_file() else None
    if kind == "lesson":
        hits = sorted((repo / "src/content/lessons").glob(f"**/{slug}.md")) if (repo / "src/content/lessons").is_dir() else []
        return hits[0] if hits else None
    return None


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Token extraction
# ---------------------------------------------------------------------------

def add_option(rows, *, loc, section, text, role, key=None):
    rows.append({
        "loc": loc,
        "section": section,
        "text": text if isinstance(text, str) else str(text),
        "role": role,  # option | answer | error
        "key": key if isinstance(key, str) or key is None else str(key),
    })


def extract_mc(rows, loc, section, choices, correct):
    if not isinstance(choices, list) or not choices:
        return
    key = None
    if isinstance(correct, int) and 0 <= correct < len(choices):
        key = choices[correct]
    for i, opt in enumerate(choices):
        role = "answer" if i == correct else "option"
        add_option(rows, loc=f"{loc} option {i + 1}", section=section, text=opt, role=role, key=key)


def extract_error_item(rows, loc, section, item):
    tokens = item.get("tokens") or []
    idx = item.get("errorIndex")
    correction = item.get("correction")
    if isinstance(idx, int) and 0 <= idx < len(tokens):
        add_option(
            rows,
            loc=f"{loc} error «{tokens[idx]}»",
            section=section,
            text=tokens[idx],
            role="error",
            key=correction if isinstance(correction, str) else None,
        )
    if isinstance(correction, str) and correction.strip():
        add_option(rows, loc=f"{loc} correction", section=section, text=correction, role="answer", key=correction)


def extract_quiz(data, rows):
    for i, it in enumerate(data.get("items") or [], 1):
        extract_mc(rows, f"Quiz Q{i}", "quiz", it.get("options") or [], it.get("answer"))


def extract_practice(data, rows):
    gf = (data.get("gapFill") or {}).get("questions") or []
    for i, q in enumerate(gf, 1):
        answers = q.get("answers") or []
        key = answers[0] if answers else q.get("display")
        for ans in answers:
            add_option(rows, loc=f"Gap-fill {i} answer", section="gapFill", text=ans, role="answer", key=key)

    for i, q in enumerate((data.get("timedMC") or {}).get("questions") or [], 1):
        extract_mc(rows, f"Beat the clock Q{i}", "timedMC", q.get("choices") or [], q.get("correct"))

    for i, pair in enumerate((data.get("matching") or {}).get("pairs") or [], 1):
        for side in ("left", "right"):
            if pair.get(side):
                add_option(rows, loc=f"Matching {i} {side}", section="matching", text=pair[side], role="answer", key=pair.get(side))

    for i, it in enumerate((data.get("errorCorrection") or {}).get("items") or [], 1):
        extract_error_item(rows, f"Find the mistake {i}", "errorCorrection", it)

    for i, it in enumerate((data.get("levelCheck") or {}).get("items") or [], 1):
        loc = f"Level check Q{i}"
        if "choices" in it:
            extract_mc(rows, loc, "levelCheck", it.get("choices") or [], it.get("correct"))
        if "errorIndex" in it and "tokens" in it:
            extract_error_item(rows, loc, "levelCheck", it)
        for ans in it.get("answers") or []:
            key = (it.get("answers") or [None])[0]
            add_option(rows, loc=f"{loc} answer", section="levelCheck", text=ans, role="answer", key=key)


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def is_known(token: str, words: set[str], allow: set[str]) -> bool:
    f = fold(token)
    if f in words or f in allow:
        return True
    # didn’t / didn't already normalised; also try without apostrophe
    if "'" in f and f.replace("'", "") in words:
        return True
    return False


def check_rows(rows, words, allow) -> list[str]:
    findings: list[str] = []
    for row in rows:
        text = row["text"]
        tokens = tokenize(text)
        key = row.get("key") or ""
        key_tokens = tokenize(key) if key else []
        role = row["role"]
        loc = row["loc"]

        # typo-of-key: selectable options only (not FtM error tokens, not the key itself)
        if role == "option" and key:
            d = typo_of(text, key)
            if d is not None:
                findings.append(
                    f"[typo-of-key] {loc}: «{text}» is edit distance {d} from the key «{key}»"
                )
            else:
                # also compare each option token to each key token
                for tok in tokens:
                    for kt in key_tokens:
                        d2 = typo_of(tok, kt)
                        if d2 is not None:
                            findings.append(
                                f"[typo-of-key] {loc}: token «{tok}» is edit distance {d2} from key token «{kt}»"
                            )

        # non-word: options, error tokens, and answers (answers are exempt if
        # they exactly match the key / themselves — still reported when a
        # thin word list misses an inflection, unless it is an answer).
        if role == "answer":
            continue
        unknown = [t for t in tokens if not is_known(t, words, allow)]
        if unknown:
            kind = "non-word"
            findings.append(
                f"[{kind}] {loc}: «{text}» — not in the word list or allowlist: "
                + ", ".join(f"«{t}»" for t in unknown)
            )
    return findings


def common_mistakes_bounds(lines: list[str]) -> tuple[int | None, int | None]:
    start = None
    for i, line in enumerate(lines):
        if COMMON_MISTAKES_RE.match(line):
            start = i
            break
    if start is None:
        return None, None
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if HEADING_RE.match(lines[j]):
            end = j
            break
    return start, end


def _blank_inline_code_and_links(line: str) -> str:
    line = re.sub(r"`[^`]+`", " ", line)
    line = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", line)
    return line


def _is_sentence_initial(line: str, start: int) -> bool:
    prefix = line[:start]
    if not re.search(r"[A-Za-z]", prefix):
        return True
    return re.search(r"[.!?…]\s*[«“\"(\[]*\s*$", prefix) is not None


def check_lesson_md(path: Path, words: set[str], allow: set[str]) -> list[str]:
    raw = path.read_text(encoding="utf-8")
    lines = raw.splitlines()
    # skip YAML frontmatter for the scan, but keep original line numbers
    body_at = 0
    if lines and lines[0].strip() == "---":
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == "---":
                body_at = i + 1
                break
    start, end = common_mistakes_bounds(lines)
    findings: list[str] = []
    in_fence = False

    for i, line in enumerate(lines):
        if i < body_at:
            continue
        stripped = line.strip()
        fence = chr(96) * 3  # backticks; written this way so this file can live inside the skill markdown
        if stripped.startswith(fence):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        text = _blank_inline_code_and_links(line)
        unk: list[str] = []
        for m in TOKEN_RE.finditer(text):
            tok = m.group(0)
            if is_known(tok, words, allow):
                continue
            # Mid-sentence Capitalised tokens are treated as proper nouns
            # (Girona, Lleida, Anna). Put any false skip on the allowlist.
            if tok[0].isupper() and not _is_sentence_initial(text, m.start()):
                continue
            unk.append(tok)
        if not unk:
            continue
        in_cm = start is not None and start < i < (end or 0)
        preview = line.strip()[:160]
        loc = f"{path}:{i + 1}"
        if in_cm:
            if "✗" not in line and "✘" not in line:
                findings.append(
                    f"[common-mistakes] {loc}: «{preview}» — invented / non-word form(s) "
                    + ", ".join(f"«{t}»" for t in unk)
                    + " appear without ✗ on the same line"
                )
        else:
            findings.append(
                f"[explanation] {loc}: «{preview}» — non-word form(s) "
                + ", ".join(f"«{t}»" for t in unk)
                + " outside «Common mistakes» (wrong forms are allowed only there, and only marked ✗)"
            )
    return findings


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug")
    ap.add_argument("--repo", default=".", help="repo root (default: current directory)")
    ap.add_argument("--quiz", help="path to <slug>-quiz-1.json")
    ap.add_argument("--practice", help="path to <slug>-practice.json")
    ap.add_argument("--lesson", help="path to the lesson markdown")
    ap.add_argument("--wordlist", help="path to a word list (one word per line)")
    ap.add_argument("--allowlist", action="append", default=[], help="extra allowlist file (repeatable)")
    args = ap.parse_args(argv)

    repo = Path(args.repo).resolve()
    slug = args.slug
    quiz_p = Path(args.quiz) if args.quiz else discover(slug, repo, "quiz")
    prac_p = Path(args.practice) if args.practice else discover(slug, repo, "practice")
    lesson_p = Path(args.lesson) if args.lesson else discover(slug, repo, "lesson")

    print(f"=== non-word gate: {slug} ===")
    if not quiz_p or not quiz_p.is_file():
        return fail_env(f"Quiz JSON not found for {slug} (looked for src/data/quizzes/{slug}-quiz-1.json)")
    if not prac_p or not prac_p.is_file():
        return fail_env(f"Practice JSON not found for {slug} (looked for src/data/practice/{slug}-practice.json)")

    try:
        words, source, warnings = load_wordlist(Path(args.wordlist) if args.wordlist else None)
    except FileNotFoundError as e:
        return fail_env(str(e))
    words |= {fold(w) for w in WORDLIST_SUPPLEMENT}

    allow: set[str] = set()
    allow_sources: list[str] = []
    default_allows = [
        repo / "scripts/lesson-ship/allowlist.txt",
        repo / "docs/verificacio" / f"{slug}-allowlist.txt",
    ]
    for p in default_allows + [Path(x) for x in args.allowlist]:
        if p.is_file():
            got = load_allowlist(p)
            allow |= got
            allow_sources.append(f"{p} ({len(got)})")

    print(f"word list: {source} ({len(words)} words)")
    print("allowlist: " + (", ".join(allow_sources) if allow_sources else "(none)"))
    for w in warnings:
        print(f"WARNING: {w}")

    rows = []
    extract_quiz(load_json(quiz_p), rows)
    extract_practice(load_json(prac_p), rows)
    print(f"checked {len(rows)} option/answer/error strings from {quiz_p.name} and {prac_p.name}")

    findings = check_rows(rows, words, allow)
    if lesson_p and lesson_p.is_file():
        print(f"lesson markdown: {lesson_p}")
        findings.extend(check_lesson_md(lesson_p, words, allow))
    else:
        print("WARNING: lesson markdown not found — explanation / Common mistakes ✗ check skipped. Pass --lesson.")
        findings.append("[explanation] lesson markdown not found; cannot verify Common mistakes ✗ marking")

    # unique findings, stable order
    seen = set()
    uniq = []
    for f in findings:
        if f not in seen:
            seen.add(f)
            uniq.append(f)
    findings = uniq

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

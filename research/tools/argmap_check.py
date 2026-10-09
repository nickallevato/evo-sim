#!/usr/bin/env python3
"""Check the argument-map data files (docs/research/argmap/).

Run from anywhere:
    research/.venv/bin/python -I research/tools/argmap_check.py

What it checks
--------------
lineage.yaml (list of dated argument versions)
  * ids unique; every parent id exists; relation is one of the allowed set
  * side / kind / fate are from the allowed sets
  * date and fate_date parse (YYYY, YYYY-MM or YYYY-MM-DD); a parent dated
    after its child is reported (a WARNING for cites/resembles, an ERROR for
    descends/revises/borrows/responds-to)
  * claim_ids exist in hierarchy.yaml
  * inferred: true requires a non-empty `why`; relation `resembles` requires
    inferred: true
  * quote <= 30 words and verbatim (see below)

defeaters.yaml (list of attacks)
  * ids unique; attacker/target ids exist (claim ids from hierarchy.yaml, or
    ids registered in the "Id registry" table of NOTES.md: x:..., chk:...,
    rev:...); every counter id exists
  * type / audit_status from the allowed sets; first_date parses
  * target_part is P<n>, P<n>[a-z]?, "inference" or "C", and when the target
    has a standard form in standard-forms.md the premise must exist there
  * every hierarchy `attacks` edge is represented by at least one defeater
  * optional `quote` fields are verbatim (same search as lineage)

Verbatim search
---------------
A quote passes if, after normalisation (NFKC, curly quotes/dashes folded,
markdown emphasis and blockquote markers removed, whitespace collapsed,
case kept), it is a substring of one of:
  1. the claim files named by the node (claim_ids / attacker / target),
  2. any claim file, sources/quotes-*.md, the ledgers, the audit's check
     write-ups (research/checks/RESULTS.md, REVIEW.md, results/*.md),
  3. a text file under sources/raw/ (txt, md, html, xml, json, vtt; HTML
     tags stripped and entities unescaped; JSON string values joined),
  4. for nodes that set `quote_source: "git:<commit>:<path>"`, that file as
     it was at that commit (used for audit wording that was later corrected).
sources/raw/ is untrusted data: this script only reads it as text.
"""
from __future__ import annotations

import datetime as dt
import html
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
ARG = ROOT / "docs/research/argmap"
CLAIMS = ROOT / "docs/research/claims"
HIER = ROOT / "docs/research/hierarchy.yaml"

LINEAGE_SIDES = {"day", "critic", "ally", "literature", "audit"}
LINEAGE_KINDS = {"argument", "value", "concession", "retraction", "revision", "reply"}
RELATIONS = {"descends", "revises", "borrows", "responds-to", "cites", "resembles"}
FATES = {"alive", "revised", "retracted", "conceded", "superseded", "dormant"}
DEF_TYPES = {"undermining", "undercutting", "rebutting"}
AUDIT = {"upheld", "partly", "not_upheld", "untested"}
STRICT_ORDER = {"descends", "revises", "borrows", "responds-to"}

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


# --------------------------------------------------------------------------
# normalisation and corpora
# --------------------------------------------------------------------------
_FOLD = {
    "\u2018": "'", "\u2019": "'", "\u201a": "'", "\u201b": "'", "\u2032": "'",
    "\u201c": '"', "\u201d": '"', "\u201e": '"', "\u2033": '"', "\u00ab": '"', "\u00bb": '"',
    "\u2013": "-", "\u2014": "-", "\u2212": "-", "\u2010": "-", "\u2011": "-",
    "\u00a0": " ", "\u2009": " ", "\u202f": " ", "\u200b": "",
}
_FOLD_RE = re.compile("|".join(map(re.escape, _FOLD)))


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = _FOLD_RE.sub(lambda m: _FOLD[m.group(0)], s)
    s = re.sub(r"(?m)^\s*>\s?", " ", s)          # blockquote markers
    s = s.replace("**", "").replace("`", "")      # markdown emphasis / code
    s = re.sub(r"(?<![\w*])\*(?=\S)|(?<=\S)\*(?![\w*])", "", s)  # *italic*
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def strip_markup(text: str) -> str:
    text = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    return html.unescape(text)


def json_strings(obj, out: list[str]) -> None:
    if isinstance(obj, str):
        out.append(obj)
    elif isinstance(obj, dict):
        for v in obj.values():
            json_strings(v, out)
    elif isinstance(obj, list):
        for v in obj:
            json_strings(v, out)


_claim_cache: dict[str, str] = {}
_claim_files: dict[str, Path] = {}


def claim_text(cid: str) -> str:
    if cid not in _claim_cache:
        p = _claim_files.get(cid)
        _claim_cache[cid] = norm(p.read_text(encoding="utf-8")) if p else ""
    return _claim_cache[cid]


_repo_corpus: str | None = None
_raw_corpus: list[tuple[str, str]] | None = None


def repo_corpus() -> str:
    global _repo_corpus
    if _repo_corpus is None:
        parts = []
        files = list(CLAIMS.glob("*.md"))
        files += list((ROOT / "docs/research/sources").glob("quotes-*.md"))
        files += list((ROOT / "docs/research/ledgers").glob("*.md"))
        files += [ROOT / "research/checks/RESULTS.md", ROOT / "research/checks/REVIEW.md"]
        files += list((ROOT / "research/checks/results").glob("*.md"))
        for p in files:
            if p.exists():
                parts.append(norm(p.read_text(encoding="utf-8", errors="replace")))
        _repo_corpus = "\n".join(parts)
    return _repo_corpus


def raw_corpus() -> list[tuple[str, str]]:
    """(path, normalised text) for readable text files under sources/raw/."""
    global _raw_corpus
    if _raw_corpus is None:
        _raw_corpus = []
        base = ROOT / "sources/raw"
        if base.exists():
            for p in sorted(base.rglob("*")):
                if not p.is_file():
                    continue
                suf = p.suffix.lower()
                try:
                    if suf in {".txt", ".md", ".vtt"}:
                        t = p.read_text(encoding="utf-8", errors="replace")
                    elif suf in {".html", ".htm", ".xml"}:
                        t = strip_markup(p.read_text(encoding="utf-8", errors="replace"))
                    elif suf == ".json":
                        raw = p.read_text(encoding="utf-8", errors="replace")
                        try:
                            out: list[str] = []
                            json_strings(json.loads(raw), out)
                            t = strip_markup("\n".join(out))
                        except json.JSONDecodeError:
                            t = strip_markup(raw)
                    else:
                        continue
                except OSError:
                    continue
                _raw_corpus.append((str(p.relative_to(ROOT)), norm(t)))
    return _raw_corpus


def git_text(spec: str) -> str:
    # spec = "git:<commit>:<path>"
    try:
        _, commit, path = spec.split(":", 2)
    except ValueError:
        return ""
    if not re.fullmatch(r"[0-9a-f]{6,40}", commit) or ".." in path:
        return ""
    try:
        out = subprocess.run(["git", "-C", str(ROOT), "show", f"{commit}:{path}"],
                             capture_output=True, text=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""
    return norm(out.stdout)


def find_quote(quote: str, claim_ids: list[str], quote_source: str | None) -> str | None:
    q = norm(quote).strip('"').strip()
    if not q:
        return None
    if quote_source:
        if quote_source.startswith("git:"):
            return quote_source if q in git_text(quote_source) else None
        p = ROOT / quote_source
        if p.exists():
            t = p.read_text(encoding="utf-8", errors="replace")
            if p.suffix.lower() in {".html", ".htm", ".xml"}:
                t = strip_markup(t)
            return quote_source if q in norm(t) else None
    for cid in claim_ids:
        if q in claim_text(cid):
            return f"claim:{cid}"
    if q in repo_corpus():
        return "repo"
    for path, text in raw_corpus():
        if q in text:
            return path
    return None


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
DATE_RE = re.compile(r"^(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?$")


def parse_date(v, where: str):
    if v is None:
        return None
    if isinstance(v, dt.date):
        return (v.year, v.month, v.day)
    s = str(v).strip()
    m = DATE_RE.match(s)
    if not m:
        err(f"{where}: date {s!r} does not parse (YYYY, YYYY-MM or YYYY-MM-DD)")
        return None
    y, mo, d = m.group(1), m.group(2), m.group(3)
    try:
        dt.date(int(y), int(mo or 1), int(d or 1))
    except ValueError:
        err(f"{where}: date {s!r} is not a calendar date")
        return None
    return (int(y), int(mo or 0), int(d or 0))


def date_after(a, b) -> bool:
    """True if a is certainly after b at the precision both share."""
    if not a or not b:
        return False
    for x, y in zip(a, b):
        if x == 0 or y == 0:
            return False
        if x != y:
            return x > y
    return False


def words(s: str) -> int:
    return len(norm(s).split())


def load_yaml_list(path: Path, name: str):
    if not path.exists():
        err(f"{name}: file missing ({path})")
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        err(f"{name}: top level must be a list")
        return []
    return data


def registry_ids() -> dict[str, str]:
    """ids declared in the 'Id registry' table of NOTES.md: first column id, second column side."""
    p = ARG / "NOTES.md"
    ids: dict[str, str] = {}
    if not p.exists():
        warn("NOTES.md missing: no registered x:/chk:/rev: ids")
        return ids
    for line in p.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*`?((?:x|chk|rev):[A-Za-z0-9._+\-]+)`?\s*\|\s*([a-z]+)\s*\|", line)
        if m:
            if m.group(1) in ids:
                err(f"NOTES.md registry: duplicate id {m.group(1)}")
            ids[m.group(1)] = m.group(2)
    return ids


def standard_form_premises() -> dict[str, set[str]]:
    """Map node id -> set of premise labels from standard-forms.md.

    A section starts with a heading '### <ID> ' (full forms) or a table row
    '| <ID> | ...' in the mini-form table; premises are tokens 'P1', 'P2a' ...
    found at the start of list items / cells inside that section.
    """
    p = ARG / "standard-forms.md"
    out: dict[str, set[str]] = {}
    if not p.exists():
        err("standard-forms.md missing")
        return out
    cur = None
    for line in p.read_text(encoding="utf-8").splitlines():
        h = re.match(r"^###\s+`?([A-Za-z0-9\-]+)`?\b", line)
        if h:
            cur = h.group(1)
            out.setdefault(cur, set())
            continue
        if line.startswith("## "):
            cur = None
        row = re.match(r"^\|\s*`?([A-Z][A-Za-z0-9\-]*)`?\s*\|(.*)$", line)
        if row and row.group(1) not in {"ID", "Id"} and cur is None:
            out.setdefault(row.group(1), set()).update(re.findall(r"\b(P\d+[a-z]?)\b", row.group(2)))
            continue
        if cur:
            m = re.match(r"^\s*[-*]?\s*\*{0,2}(P\d+[a-z]?)\*{0,2}[\s.:]", line)
            if m:
                out[cur].add(m.group(1))
    return out


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------
def main() -> int:
    hier = yaml.safe_load(HIER.read_text(encoding="utf-8"))["nodes"]
    claim_ids = {n["id"] for n in hier}
    for n in hier:
        cf = n.get("claim_file")
        if cf:
            _claim_files[n["id"]] = ROOT / cf
    reg = registry_ids()
    known = claim_ids | set(reg)
    forms = standard_form_premises()

    # ---------------- lineage ----------------
    lin = load_yaml_list(ARG / "lineage.yaml", "lineage.yaml")
    ids: dict[str, dict] = {}
    for i, n in enumerate(lin):
        nid = n.get("id")
        if not nid:
            err(f"lineage[{i}]: missing id")
            continue
        if nid in ids:
            err(f"lineage {nid}: duplicate id")
        ids[nid] = n
    quotes_ok = 0
    for nid, n in ids.items():
        w = f"lineage {nid}"
        for key in ("label", "side", "kind", "date", "locator", "quote", "fate"):
            if n.get(key) in (None, ""):
                err(f"{w}: missing {key}")
        if n.get("side") not in LINEAGE_SIDES:
            err(f"{w}: side {n.get('side')!r} not allowed")
        if n.get("kind") not in LINEAGE_KINDS:
            err(f"{w}: kind {n.get('kind')!r} not allowed")
        if n.get("fate") not in FATES:
            err(f"{w}: fate {n.get('fate')!r} not allowed")
        d = parse_date(n.get("date"), w)
        if n.get("fate") != "alive" and not n.get("fate_date"):
            warn(f"{w}: fate {n.get('fate')} without fate_date")
        if n.get("fate_date"):
            fd = parse_date(n.get("fate_date"), w + " fate_date")
            if date_after(d, fd):
                err(f"{w}: fate_date before date")
        for c in n.get("claim_ids") or []:
            if c not in claim_ids:
                err(f"{w}: claim id {c} not in hierarchy.yaml")
        anyinf = False
        for p in n.get("parents") or []:
            pid, rel = p.get("id"), p.get("relation")
            if pid not in ids:
                err(f"{w}: parent {pid} does not exist")
                continue
            if rel not in RELATIONS:
                err(f"{w}: relation {rel!r} not allowed")
            if rel == "resembles" and not (p.get("inferred", n.get("inferred"))):
                err(f"{w}: 'resembles' link to {pid} must be inferred: true")
            if p.get("inferred", False):
                anyinf = True
                if not (p.get("why") or n.get("why")):
                    err(f"{w}: inferred link to {pid} needs a why")
            pd = parse_date(ids[pid].get("date"), f"lineage {pid}")
            if date_after(pd, d):
                (err if rel in STRICT_ORDER else warn)(
                    f"{w}: parent {pid} ({ids[pid].get('date')}) is dated after child ({n.get('date')}) [{rel}]")
        if n.get("inferred") and not n.get("why"):
            err(f"{w}: inferred: true needs a why")
        if bool(n.get("inferred")) != anyinf:
            err(f"{w}: node-level inferred ({n.get('inferred')}) must equal 'any parent link inferred' ({anyinf})")
        q = n.get("quote") or ""
        if q:
            if words(q) > 30:
                err(f"{w}: quote has {words(q)} words (> 30)")
            hit = find_quote(q, list(n.get("claim_ids") or []), n.get("quote_source"))
            if hit is None:
                err(f"{w}: quote not found verbatim: {q[:90]!r}")
            else:
                quotes_ok += 1

    # ---------------- defeaters ----------------
    dfs = load_yaml_list(ARG / "defeaters.yaml", "defeaters.yaml")
    dids: dict[str, dict] = {}
    for i, d in enumerate(dfs):
        did = d.get("id")
        if not did:
            err(f"defeaters[{i}]: missing id")
            continue
        if did in dids:
            err(f"defeater {did}: duplicate id")
        dids[did] = d
    covered: set[tuple[str, str]] = set()
    dq_ok = 0
    for did, d in dids.items():
        w = f"defeater {did}"
        for key in ("attacker", "target", "target_part", "type", "by", "first_date", "locator", "audit_status", "note"):
            if d.get(key) in (None, "", []):
                err(f"{w}: missing {key}")
        a, t = d.get("attacker"), d.get("target")
        for role, x in (("attacker", a), ("target", t)):
            if x not in known:
                err(f"{w}: {role} {x!r} is not a hierarchy id or a registered id")
        covered.add((a, t))
        if d.get("type") not in DEF_TYPES:
            err(f"{w}: type {d.get('type')!r} not allowed")
        if d.get("audit_status") not in AUDIT:
            err(f"{w}: audit_status {d.get('audit_status')!r} not allowed")
        if d.get("audit_status") != "untested" and not d.get("audit_basis"):
            warn(f"{w}: audit_status without audit_basis")
        parse_date(d.get("first_date"), w)
        tp = str(d.get("target_part", ""))
        if not re.fullmatch(r"P\d+[a-z]?|inference|C", tp):
            err(f"{w}: target_part {tp!r} must be P<n>, 'inference' or 'C'")
        elif tp.startswith("P"):
            if t in forms and forms[t] and tp not in forms[t]:
                err(f"{w}: target {t} has no premise {tp} in standard-forms.md")
            if t not in forms and t in claim_ids:
                err(f"{w}: target {t} has no standard form or mini-form; cannot target {tp}")
        if d.get("type") == "undermining" and not tp.startswith("P"):
            err(f"{w}: undermining must target a premise")
        if d.get("type") == "undercutting" and tp != "inference":
            err(f"{w}: undercutting must target 'inference'")
        if d.get("type") == "rebutting" and tp != "C":
            err(f"{w}: rebutting must target 'C'")
        for c in d.get("counter") or []:
            if c not in dids:
                err(f"{w}: counter {c} does not exist")
            elif dids[c].get("target") != a:
                warn(f"{w}: counter {c} targets {dids[c].get('target')}, not this defeater's attacker {a}")
        if d.get("quote"):
            if words(d["quote"]) > 30:
                err(f"{w}: quote > 30 words")
            if find_quote(d["quote"], [x for x in (a, t) if x in claim_ids], d.get("quote_source")) is None:
                err(f"{w}: quote not found verbatim: {d['quote'][:90]!r}")
            else:
                dq_ok += 1

    edges = [(n["id"], e["target"]) for n in hier for e in n.get("edges", []) if e["type"] == "attacks"]
    for a, t in edges:
        if (a, t) not in covered:
            err(f"hierarchy attacks edge {a} -> {t} has no defeater")

    # standard forms: every load-bearing node and ROOT
    for n in hier:
        if (n.get("load_bearing") or n["id"] == "ROOT") and n["id"] not in forms:
            err(f"standard-forms.md: no standard form for load-bearing node {n['id']}")

    # ---------------- report ----------------
    from collections import Counter
    print(f"lineage.yaml:   {len(ids)} nodes, {quotes_ok} quotes verified")
    print("  by side:", dict(Counter(n.get('side') for n in ids.values())))
    print("  by fate:", dict(Counter(n.get('fate') for n in ids.values())))
    print("  by kind:", dict(Counter(n.get('kind') for n in ids.values())))
    print(f"defeaters.yaml: {len(dids)} defeaters ({dq_ok} optional quotes verified); "
          f"{len(edges)} hierarchy attacks edges, all covered: {all((a, t) in covered for a, t in edges)}")
    print("  by type:", dict(Counter(d.get('type') for d in dids.values())))
    side_of = {n["id"]: n["side"] for n in hier}
    def side(x):
        return side_of.get(x) or reg.get(x) or "unknown"
    print("  by attacker side:", dict(Counter(side(d.get('attacker')) for d in dids.values())))
    print("  by audit_status:", dict(Counter(d.get('audit_status') for d in dids.values())))
    print(f"standard-forms.md: {sum(1 for k, v in forms.items() if v)} forms with premises")
    for m in warnings:
        print("WARNING:", m)
    for m in errors:
        print("ERROR:", m)
    print(f"{len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Survey of the claim corpus for the B-R33 conjunction rule (EVO-95, step 3 of O-6).

What it answers: which claims have more than one verbatim Statement quote, and of
those, which record *differing per-quote verdicts* — the only claims whose fields the
conjunction rule could move. Prints four tiers:

  T0  every claim, with its Statement-quote-block count and load_bearing flag
  T1  claims with >1 Statement quote block (structural candidates)
  T2  claims whose text records per-quote differentiation (RH tag or verdict)
  T3  of T2, those where the differentiation is of a *verdict* on a verdict scale
  T4  multi-quote Statements of mixed provenance (some quote marked secondhand or
      unretrieved): candidate off-scale fidelity conjuncts, which T2's wordlist misses

Read-only. No claim file is written. Run from the repo root:
    research/.venv/bin/python -I research/tools/conjunction_survey.py [--tier 0|1|2|3]
"""

import argparse
import glob
import os
import re

CLAIMS = "docs/research/claims/*.md"

# per-quote language anywhere in a claim file
PERQUOTE = re.compile(
    r"quote[s]? (?:1|2|3|4|5|one|two|three)\b"
    r"|(?:first|second|third|fourth|fifth) quote"
    r"|the (?:blog|Zenodo|book|slide|abstract|comment|post|tweet|paper) quote"
    r"|not examined|unexamined|per-quote|both quotes|each quote",
    re.I,
)
FIDELITY = ("accurate", "partial", "misread", "unverifiable")


def claim_files():
    for p in sorted(glob.glob(CLAIMS)):
        b = os.path.basename(p)
        if b.startswith("_"):
            continue
        yield p, b[:-3]


def parse(path):
    t = open(path, encoding="utf-8").read()
    fm = t.split("---\n")[1] if t.startswith("---") else ""
    # the verdicts block only: a verdict_scope entry repeats the field names and
    # would otherwise be read as the field's value
    vblock = re.search(r"^verdicts:\s*$(.*?)(?=^\S|\Z)", fm, re.S | re.M)
    vblock = vblock.group(1) if vblock else ""
    m = re.search(r"^## Statement \(verbatim\)\s*$(.*?)(?=^## )", t, re.S | re.M)
    stmt = m.group(1) if m else ""
    return {
        "text": t,
        "fm": fm,
        "stmt": stmt,
        # a quote block = one run of contiguous "> " lines
        "nq": len(re.findall(r"(?:^> .*\n?)+", stmt, re.M)),
        "lb": bool(re.search(r"^load_bearing:\s*true", fm, re.M)),
        "verdicts": dict(
            re.findall(
                r"^\s{2}(internal|fidelity|external):\s*\"?([a-z/-]+)", vblock, re.M
            )
        ),
        "has_scope": bool(re.search(r"^verdict_scope:", fm, re.M)),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tier", type=int, default=None, choices=[0, 1, 2, 3, 4])
    args = ap.parse_args()

    rows = [(name, parse(p)) for p, name in claim_files()]
    t1 = [(n, d) for n, d in rows if d["nq"] > 1]
    t2 = [(n, d) for n, d in rows if PERQUOTE.search(d["text"])]
    # T3: of T2, drop the files whose only per-quote line is an RH tag (rule RH:
    # a rhetoric conjunct is not literal-fact-checked and changes no verdict)
    t3 = []
    for n, d in t2:
        verdictish = False
        for line in d["text"].splitlines():
            if not PERQUOTE.search(line):
                continue
            if re.match(r"\s*RH tag", line) or "RH tag" in line[:40]:
                continue
            verdictish = True
        if verdictish:
            t3.append((n, d))
    # mixed-provenance Statement sections: a multi-quote Statement that marks some
    # quote secondhand / unretrieved, i.e. a candidate off-scale fidelity conjunct
    mixed = [
        (n, d)
        for n, d in t1
        if re.search(r"secondhand|not accessed|unretrieved|paraphrase", d["stmt"], re.I)
    ]

    print(f"T0 claims scored                : {len(rows)}")
    print(f"T1 >1 Statement quote block     : {len(t1)}")
    print(f"T2 per-quote language in file   : {len(t2)}")
    print(f"T3 per-quote *verdict* language : {len(t3)}")
    print(f"   mixed-provenance Statements  : {len(mixed)}")
    print(f"   load-bearing claims          : {sum(1 for _, d in rows if d['lb'])}")

    if args.tier is None:
        return
    sel = {0: rows, 1: t1, 2: t2, 3: t3, 4: mixed}[args.tier]
    print(f"\n--- tier {args.tier} ({len(sel)}) ---")
    for n, d in sel:
        flag = "LB" if d["lb"] else "--"
        v = d["verdicts"]
        print(
            f"  [{flag}] q={d['nq']:<2} {n:62s} "
            f"int={v.get('internal','-'):<14} fid={v.get('fidelity','-'):<13} "
            f"ext={v.get('external','-'):<13} scope={'y' if d['has_scope'] else 'n'}"
        )


if __name__ == "__main__":
    main()

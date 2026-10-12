"""method_audit_stats.py: counts behind docs/research/criticality/METHOD-AUDIT-proposals.md (read-only).

    research/.venv/bin/python -I research/tools/method_audit_stats.py

Reads the front matter and the "## Check" section of every claim file. Changes nothing.
Prints: (1) verdict tallies; (2) internal `holds` on files at status `extracted`, each classed by
what the file itself records as its check; (3) the seeded sample of `contested` external verdicts.
"""
import collections
import glob
import random
import re

import yaml

SEED = 20261012
CITED = re.compile(r"R4[ -][A-Za-z0-9]|results/R4-|[Rr]eview #\d")
CALC = re.compile(r"python3? -I|[Aa]rithmetic|exact chain|research/checks/[a-z0-9_]+\.py|Textual")


def load():
    rows = []
    for f in sorted(glob.glob("docs/research/claims/*.md")):
        if f.endswith("_TEMPLATE.md"):
            continue
        _, fm_txt, body = open(f, encoding="utf-8").read().split("---", 2)
        fm = yaml.safe_load(fm_txt)
        com = {}
        for k in ("internal", "fidelity", "external"):
            m = re.search(r"^\s+%s:\s*([^#\n]*?)\s*(#.*)?$" % k, fm_txt, re.M)
            com[k] = (m.group(2) or "") if m else ""
        m = re.search(r"## Check\n(.*?)(\n## |\Z)", body, re.S)
        rows.append({"fm": fm, "com": com, "check": m.group(1).strip() if m else "", "file": f.split("/")[-1]})
    return rows


def holds_class(r):
    text = r["com"]["internal"] + " " + r["check"]
    if CITED.search(text):
        return "check-cited"
    if CALC.search(text) or re.search(r"\d\s*=\s*\d|=\s*[\d.]+e?\d", r["com"]["internal"]):
        return "inline-only"
    return "nothing-recorded"


def main():
    rows = load()
    print("claim files:", len(rows))
    v = lambda r, k: str(r["fm"]["verdicts"][k])
    print("\ninternal by side:")
    c = collections.Counter((r["fm"]["side"], v(r, "internal")) for r in rows)
    for k in sorted(c):
        print("  ", k, c[k])
    ext = collections.Counter(v(r, "external") for r in rows)
    print("\nexternal:", dict(ext))
    dec = sum(n for k, n in ext.items() if k not in ("pending", "n/a"))
    print("decided external (not pending, not n/a):", dec, " contested share: %.0f%%" % (100 * ext["contested"] / dec))
    print("status:", dict(collections.Counter(r["fm"]["status"] for r in rows)))

    H = [r for r in rows if v(r, "internal").startswith("holds")]
    HX = [r for r in H if r["fm"]["status"] == "extracted"]
    print("\ninternal holds (incl. non-vocabulary variants):", len(H),
          " exact 'holds':", sum(v(r, "internal") == "holds" for r in H))
    print("holds on status=extracted:", len(HX), dict(collections.Counter(r["fm"]["side"] for r in HX)))
    cls = collections.defaultdict(list)
    for r in HX:
        cls[holds_class(r)].append(r)
    for k in ("check-cited", "inline-only", "nothing-recorded"):
        print("\n  %s: %d %s" % (k, len(cls[k]), dict(collections.Counter(r["fm"]["side"] for r in cls[k]))))
        for r in cls[k]:
            print("    %-9s %-10s %s" % (r["fm"]["id"], r["fm"]["side"], r["file"]))

    ids = sorted(r["fm"]["id"] for r in rows if v(r, "external") == "contested")
    print("\ncontested:", len(ids), " seed:", SEED)
    print("sample of 20:", sorted(random.Random(SEED).sample(ids, 20)))
    dec2 = [r for r in rows if v(r, "external") in ("supported", "contradicted")]
    print("\ndecided supported/contradicted:", len(dec2), dict(collections.Counter(r["fm"]["side"] for r in dec2)))
    print("no 'Result that would change a verdict' line:",
          sum("would change a verdict" not in open("docs/research/claims/" + r["file"], encoding="utf-8").read() for r in rows))


if __name__ == "__main__":
    main()

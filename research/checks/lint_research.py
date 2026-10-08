"""Research lint (THROWAWAY tooling).

Checks docs/research/claims/*.md front-matter and cross-references:
  - required fields present and enum values valid
  - every edge target / parent exists (claims or hierarchy.yaml)
  - every claim has a Statement quote and a source line
  - every claim has three verdicts (pending allowed)
  - each side has claims (balance count)
With --write-hierarchy, regenerates docs/research/hierarchy.yaml from claim front-matter
(nodes in hierarchy.yaml without a claim file are kept and marked `claim_file: missing`).
Exit 1 on errors.
"""
import os, sys, re, glob, argparse, collections
import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
CLAIMS = os.path.join(ROOT, "docs", "research", "claims")
HIER = os.path.join(ROOT, "docs", "research", "hierarchy.yaml")

SIDES = {"day", "critic", "ally", "literature"}
EDGE_TYPES = {"supports", "attacks", "revises", "supersedes", "depends-on"}
V_INT = {"holds", "arithmetic-error", "non-sequitur", "pending", "n/a"}
V_FID = {"accurate", "partial", "misread", "unverifiable", "pending", "n/a"}
V_EXT = {"supported", "contested", "contradicted", "untestable", "pending", "n/a"}


def parse(path):
    txt = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", txt, re.S)
    if not m:
        return None, txt
    return yaml.safe_load(m.group(1)) or {}, m.group(2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write-hierarchy", action="store_true")
    a = ap.parse_args()
    errs, warns = [], []
    claims = {}
    for p in sorted(glob.glob(os.path.join(CLAIMS, "*.md"))):
        if os.path.basename(p).startswith("_"):
            continue
        fm, body = parse(p)
        name = os.path.relpath(p, ROOT)
        if fm is None:
            errs.append(f"{name}: no YAML front-matter"); continue
        cid = str(fm.get("id", ""))
        if not cid:
            errs.append(f"{name}: missing id"); continue
        if cid in claims:
            errs.append(f"{name}: duplicate id {cid} (also {claims[cid]['_file']})")
        fm["_file"] = name
        claims[cid] = fm
        if fm.get("side") not in SIDES:
            errs.append(f"{name}: side={fm.get('side')!r} not in {sorted(SIDES)}")
        v = fm.get("verdicts") or {}
        for k, allowed in (("internal", V_INT), ("fidelity", V_FID), ("external", V_EXT)):
            val = str(v.get(k, "")).split()[0] if v.get(k) else ""
            if val not in allowed:
                errs.append(f"{name}: verdicts.{k}={v.get(k)!r} not in {sorted(allowed)}")
        if "## Statement" not in body or ">" not in body.split("## Statement", 1)[1][:2000]:
            errs.append(f"{name}: no quoted statement")
        if not re.search(r"Source:|source:", body):
            warns.append(f"{name}: no 'Source:' line")
        if fm.get("sourcing") not in ("firsthand", "secondhand"):
            warns.append(f"{name}: sourcing={fm.get('sourcing')!r}")

    hier = yaml.safe_load(open(HIER)) if os.path.exists(HIER) else {"nodes": []}
    hier_ids = {str(n["id"]) for n in hier.get("nodes", [])}
    known = set(claims) | hier_ids
    for cid, fm in claims.items():
        par = fm.get("parent")
        if par and str(par) not in known:
            errs.append(f"{fm['_file']}: parent {par} unknown")
        for e in fm.get("edges") or []:
            if not isinstance(e, dict):
                errs.append(f"{fm['_file']}: malformed edge {e!r}"); continue
            if e.get("type") not in EDGE_TYPES:
                errs.append(f"{fm['_file']}: edge type {e.get('type')!r}")
            if str(e.get("target")) not in known:
                errs.append(f"{fm['_file']}: edge target {e.get('target')} unknown")
    missing = sorted(hier_ids - set(claims))

    by_side = collections.Counter(fm.get("side") for fm in claims.values())
    verdict_counts = collections.Counter()
    for fm in claims.values():
        for k, val in (fm.get("verdicts") or {}).items():
            verdict_counts[(k, str(val).split()[0])] += 1
    print(f"claims: {len(claims)}  by side: {dict(by_side)}")
    print(f"hierarchy nodes without claim file: {len(missing)} {missing[:20]}")
    print("verdicts:", ", ".join(f"{k}:{v}={n}" for (k, v), n in sorted(verdict_counts.items())))
    print("load-bearing:", sorted(c for c, fm in claims.items() if fm.get("load_bearing") is True))
    for w in warns:
        print("WARN", w)
    for e in errs:
        print("ERROR", e)

    if a.write_hierarchy and not errs:
        nodes = []
        for cid, fm in sorted(claims.items()):
            nodes.append({k: fm[k] for k in ("id", "title", "side", "branch", "parent", "edges", "load_bearing", "sourcing", "status", "verdicts") if k in fm} | {"claim_file": fm["_file"]})
        for n in hier.get("nodes", []):
            if str(n["id"]) in missing:
                nodes.append(dict(n) | {"claim_file": "missing"})
        with open(HIER, "w") as f:
            f.write("# GENERATED by research/checks/lint_research.py --write-hierarchy from claim front-matter.\n")
            yaml.safe_dump({"nodes": nodes}, f, sort_keys=False, allow_unicode=True, width=140)
        print(f"wrote {HIER} ({len(nodes)} nodes)")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()

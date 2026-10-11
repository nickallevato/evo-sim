"""HF main: merge the per-host hf_main files (post hoc, orchestration only; written 2026-10-11 after both hosts stopped).
Usage: research/.venv/bin/python -I research/checks/hf_merge_hosts.py raw/hf_main_workhorse.jsonl raw/hf_main_builder.jsonl raw/hf_main.jsonl
The builder file starts with a 316-row seed copy of the workhorse file (checked byte-identical). Every (cell, rep)
run independently on both hosts is compared on all fields except `sec`; the union is written sorted by (cell, rep).
"""
import json, sys, math
w, b, out = sys.argv[1:4]
W = [json.loads(l) for l in open(w)]
B = [json.loads(l) for l in open(b)]
SEED_N = 316
def key(r): return (r["cell"], r["rep"])
def strip(r):
    d = {k: v for k, v in r.items() if k != "sec"}
    return json.dumps(d, sort_keys=True)
for name, rows in (("W", W), ("B", B)):
    ks = [key(r) for r in rows]
    print(name, "rows", len(rows), "unique", len(set(ks)))
wd = {key(r): r for r in W}
seedk = {key(r) for r in B[:SEED_N]}
bind = {key(r): r for r in B[SEED_N:]}
assert all(strip(wd[k]) == strip(r) for k, r in ((key(r), r) for r in B[:SEED_N])), "seed copy differs"
both = set(wd) & set(bind)
mism = [k for k in both if strip(wd[k]) != strip(bind[k])]
print("independently computed on both hosts:", len(both), "mismatches:", len(mism), mism[:10])
for k in mism[:3]:
    a, c = wd[k], bind[k]
    print(k, {f: (a[f], c.get(f)) for f in a if f != "sec" and a[f] != c.get(f)})
merged = dict(wd)
for k, r in bind.items():
    merged.setdefault(k, r)
print("union unique jobs:", len(merged), "W-only", len(set(wd) - set(bind) - seedk), "B-only", len(set(bind) - set(wd)))
with open(out, "w") as fh:
    for k in sorted(merged):
        fh.write(json.dumps(merged[k]) + "\n")

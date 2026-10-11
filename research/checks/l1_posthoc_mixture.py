"""L1 post hoc (written after reading raw/l1_dnds.out; NOT pre-registered): can a partial extraction error reproduce
BOTH of Day's numbers (pooled dN/dS 0.80 AND single-SNV-codon nonsynonymous share 71.6%) at once?
Mixes the V0 (correct) totals with an error variant's totals for a fraction f of genes (genes assumed broken at random,
so totals mix linearly) and reports, at the f that gives pooled 0.80: the single-difference nonsyn share, the
single-diff dN/dS, the N/S site ratio and the expected number of genes free of internal stops in both species.
Run locally (trivial arithmetic on the JSON): research/.venv/bin/python -I research/checks/l1_posthoc_mixture.py IN_JSON
"""
import json, math, sys

def jc(p):
    return -0.75 * math.log(1 - 4 * p / 3)

r = json.load(open(sys.argv[1]))
V = r["variants"]
def tot(v, s="ALL"):
    d = V[v][s]
    n1 = d["single_nonsyn_share"] * d["single_codons"]
    return dict(S=d["S"], N=d["N"], Sd=d["Sd"], Nd=d["Nd"], n1=n1, s1=d["single_codons"] - n1, sf=d["stopfree_both"], n=d["n"])
def mix(a, b, f):
    return {k: (1 - f) * a[k] + f * b[k] for k in a}
def stats(t):
    return dict(dnds=jc(t["Nd"] / t["N"]) / jc(t["Sd"] / t["S"]), share=t["n1"] / (t["n1"] + t["s1"]),
                d1=(t["n1"] / t["N"]) / (t["s1"] / t["S"]), NS=t["N"] / t["S"], stopfree=t["sf"])
for s in ("ALL", "O121"):
    a = tot("V0", s)
    for v in ("F1", "F2", "RCa", "RCm"):
        b = tot(v, s)
        lo, hi = 0.0, 1.0
        if stats(b)["dnds"] < 0.80:
            print(f"{s:5s} {v:4s}: max pooled {stats(b)['dnds']:.3f} < 0.80 at f = 1"); continue
        for _ in range(60):
            m = (lo + hi) / 2
            (lo, hi) = (m, hi) if stats(mix(a, b, m))["dnds"] < 0.80 else (lo, m)
        st = stats(mix(a, b, lo))
        print(f"{s:5s} {v:4s}: f = {lo:.3f} -> pooled {st['dnds']:.3f}, single-diff nonsyn share {st['share']:.3f}, "
              f"single-diff dN/dS {st['d1']:.3f}, N/S {st['NS']:.2f}, stop-free both {st['stopfree']:.0f} of {a['n']}")

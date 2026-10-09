"""D1 FIX PASS (POST HOC; written after the three D1 reviews): GB1 four-site landscape (Wu 2016, ProteinGym copy), margin and threshold
sensitivity, critic-requested outputs, and uphill walks on a MEASURED landscape (the D1b/D2i test).  Committed before its first run.
Run: research/.venv/bin/python -I research/checks/d1_fix_gb1.py  -> results/raw/d1_fix_gb1.json, d1_fix_gb1.txt

Definitions (as in d1_posthoc_gb1_snv.py): variants = 4-letter amino-acid strings at positions 265/266/267/280 (WT V,D,G,V; WT fitness assumed 1);
a step changes one site; 'aa' adjacency = any of 19 substitutions, 'snv' adjacency = amino-acid pairs one nucleotide apart for at least one
codon of the WT residue (union over codons: permissive, so SNV reach is an upper bound).  A step is 'uphill' if the destination fitness exceeds the
source by MORE THAN the margin (in units of WT fitness; the earlier reports used margin 0.1 without saying so).  Functional = fitness >= 0.5.
Outputs: local maxima among functional; share of functional variants with an uphill neighbour; share with a monotone uphill path to the global
maximum, to any variant with fitness >= 1 (WT-level), to >= 1.2; random-uphill walk endpoint statistics (each step picks uniformly among uphill
neighbours; exact by dynamic programming): P(end at global max), mean endpoint fitness, P(end >= 1); functional counts at thresholds 0.3/0.5/0.8;
fitness of the local maxima; the 76 single substitutions from WT.
Note: unobserved variants (6.6% of the 160,000) are treated as absent.
"""
import os, sys, json, csv, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import d1_sequence_space_spike as D

AAS = D.AAS
path = os.path.join(D.DMS_DIR, "x", "DMS_ProteinGym_substitutions", "SPG1_STRSG_Wu_2016.csv")
rows, wt = [], {}
with open(path, newline="") as fh:
    for r in csv.DictReader(fh):
        ms = r["mutant"].split(":")
        rows.append(([(int(m[1:-1]), m[-1]) for m in ms], float(r["DMS_score"])))
        for m in ms:
            wt[int(m[1:-1])] = m[0]
pos = sorted(wt)
wt_idx = tuple(AAS.index(wt[p]) for p in pos)
A = np.full((20, 20, 20, 20), np.nan)
for muts, s in rows:
    idx = list(wt_idx)
    for p, a in muts:
        idx[pos.index(p)] = AAS.index(a)
    A[tuple(idx)] = s
A[wt_idx] = 1.0
pres = ~np.isnan(A)
X = np.nan_to_num(A, nan=0.0).reshape(-1)
pf = pres.reshape(-1)
STR = [8000, 400, 20, 1]
wt_flat = int(np.ravel_multi_index(wt_idx, A.shape))
ADJ = np.zeros((20, 20), bool)
for c, a in D.CODON2AA.items():
    if a == "*":
        continue
    for p in range(3):
        for n in "TCAG":
            if n != c[p]:
                b = D.CODON2AA[c[:p] + n + c[p + 1:]]
                if b != "*" and b != a:
                    ADJ[AAS.index(a), AAS.index(b)] = True
ADJ = ADJ | ADJ.T
NB = {"aa": {a: [b for b in range(20) if b != a] for a in range(20)}, "snv": {a: np.flatnonzero(ADJ[a]).tolist() for a in range(20)}}
order = np.argsort(-X, kind="stable")
order = order[pf[order]]
gmax = int(order[0])
txt = []
P = txt.append
out = {"n_present": int(pf.sum()), "global_max": float(X[gmax])}


def digits(f):
    return [(f // STR[k]) % 20 for k in range(4)]


def run(adj, margin, walks=False):
    nb = NB[adj]
    up = {}
    for f in order:
        f = int(f)
        d = digits(f)
        lst = []
        for k in range(4):
            for b in nb[d[k]]:
                g = f + (b - d[k]) * STR[k]
                if pf[g] and X[g] > X[f] + margin:
                    lst.append(g)
        up[f] = lst
    func = (X >= 0.5) & pf
    has_up = np.array([len(up.get(f, [])) > 0 if pf[f] else False for f in range(X.size)])
    lm = [f for f in order if func[f] and not has_up[f]]
    # reachability to targets: processed in descending fitness; reach[f] = f is target or any uphill neighbour reaches
    res = dict(local_maxima_functional=len(lm), lm_fitness_quantiles=np.percentile(X[lm], [0, 25, 50, 75, 100]).round(2).tolist(),
               share_func_with_uphill_nbr=float((func & has_up).sum() / func.sum()))
    for lab, thr in (("global", None), ("ge1", 1.0), ("ge1.2", 1.2)):
        reach = np.zeros(X.size, bool)
        for f in order:
            f = int(f)
            if (thr is None and f == gmax) or (thr is not None and X[f] >= thr):
                reach[f] = True
            else:
                reach[f] = any(reach[g] for g in up[f])
        res[f"reach_{lab}"] = float((reach & func).sum() / func.sum())
    if walks:
        # exact random-uphill endpoint distribution over local maxima (among ALL present local maxima, not only functional)
        allmax = [int(f) for f in order if not has_up[f] and X[f] >= 0.5]
        mid = {f: i for i, f in enumerate(allmax)}
        dist = {}
        for f in order:
            f = int(f)
            if not up[f]:
                v = np.zeros(len(allmax))
                if f in mid:
                    v[mid[f]] = 1.0
                dist[f] = v
            else:
                dist[f] = np.mean([dist[g] for g in up[f]], axis=0)
        fit = X[allmax]
        fs = [int(f) for f in order if func[f]]
        D_ = np.array([dist[f] for f in fs])  # (nfunc, nmax); rows of non-functional-ending walks sum <1
        res["walk_P_end_global"] = float(D_[:, mid[gmax]].mean()) if gmax in mid else None
        res["walk_P_end_in_functional_max"] = float(D_.sum(axis=1).mean())
        res["walk_mean_end_fitness"] = float((D_ @ fit).sum() / D_.sum())
        res["walk_P_end_ge1_given_end_functional"] = float((D_[:, fit >= 1.0].sum()) / D_.sum())
        # from WT
        dw = dist[wt_flat]
        res["walk_from_WT"] = dict(P_end_global=float(dw[mid[gmax]]) if gmax in mid else None, mean_end_fitness=float(dw @ fit / dw.sum()) if dw.sum() > 0 else None,
                                   P_end_ge1=float(dw[fit >= 1.0].sum()))
    return res


for adj in ("aa", "snv"):
    out[adj] = {}
    for mg in (0.0, 0.05, 0.1, 0.2, 0.3):
        r = run(adj, mg, walks=(mg == 0.1))
        out[adj][str(mg)] = r
        P(f"{adj} margin {mg}: maxima {r['local_maxima_functional']}, uphill-nbr share {r['share_func_with_uphill_nbr']:.3f}, reach global {r['reach_global']:.3f}, reach >=1 {r['reach_ge1']:.3f}, reach >=1.2 {r['reach_ge1.2']:.3f}, maxima fitness quantiles {r['lm_fitness_quantiles']}"
          + (f"; walk: P(end global) {r['walk_P_end_global']:.3f}, mean end fitness {r['walk_mean_end_fitness']:.2f}, P(end>=1) {r['walk_P_end_ge1_given_end_functional']:.3f}, from WT {r['walk_from_WT']}" if "walk_P_end_global" in r else ""))
func_counts = {thr: int(((X >= thr) & pf).sum()) for thr in (0.3, 0.5, 0.8, 1.0, 1.2)}
out["functional_counts"] = func_counts
out["frac_below_0.3"] = float(((X < 0.3) & pf).sum() / pf.sum())
P(f"counts: {func_counts}; share below 0.3: {out['frac_below_0.3']:.3f}")
singles = []
d0 = list(wt_idx)
for k in range(4):
    for b in range(20):
        if b != d0[k]:
            j = list(d0)
            j[k] = b
            singles.append(X[int(np.ravel_multi_index(tuple(j), A.shape))])
singles = np.array(singles)
out["wt_singles"] = dict(n=len(singles), ge0_5=float((singles >= 0.5).mean()), ge1=float((singles >= 1.0).mean()), ge1_2=float((singles >= 1.2).mean()), lt0_2=float((singles < 0.2).mean()))
P(f"WT single substitutions (76): {out['wt_singles']}")
open(os.path.join(D.RAW, "d1_fix_gb1.txt"), "w").write("\n".join(txt))
json.dump(out, open(os.path.join(D.RAW, "d1_fix_gb1.json"), "w"), indent=1, default=float)
print("\n".join(txt))

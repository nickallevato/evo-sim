"""D1 POST HOC: GB1 four-site landscape restricted to SINGLE-NUCLEOTIDE-accessible amino-acid steps.
Written after d1_gb1.json was seen.  The pre-registered gb1 part allowed any of 19 amino-acid substitutions at a site in one step
(many need 2-3 nucleotide changes); this redoes local maxima / uphill reachability / functional connectivity with the adjacency
'aa a -> aa b is one SNV for at least one codon of a' (symmetric by construction).  The WT is assumed fitness 1 as in the main part.
Run: research/.venv/bin/python -I research/checks/d1_posthoc_gb1_snv.py  -> research/checks/results/raw/d1_posthoc_gb1_snv.json
"""
import os, sys, json, csv, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import d1_sequence_space_spike as D

AAS = D.AAS
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
path = os.path.join(D.DMS_DIR, "x", "DMS_ProteinGym_substitutions", "SPG1_STRSG_Wu_2016.csv")
rows = []
wt = {}
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
X = np.nan_to_num(A, nan=0.0)
func = (X >= 0.5) & pres
marg = 0.1
shape = A.shape
nb = {a: np.flatnonzero(ADJ[a]).tolist() for a in range(20)}
out = dict(n_adj_pairs_per_aa_mean=float(ADJ.sum(axis=1).mean()), n_functional=int(func.sum()))
# local maxima and uphill reachability
flat = X.reshape(-1)
pf = pres.reshape(-1)
fr = func.reshape(-1)
order = np.argsort(-X, axis=None)
gmax = int(np.argmax(np.where(pres, X, -1).reshape(-1)))
reach = np.zeros(flat.size, bool)
reach[gmax] = True
has_up = np.zeros(flat.size, bool)
for f in order:
    if not pf[f]:
        continue
    ix = np.unravel_index(f, shape)
    ok = False
    up = False
    for ax in range(4):
        for b in nb[ix[ax]]:
            jx = list(ix)
            jx[ax] = b
            g = np.ravel_multi_index(tuple(jx), shape)
            if pf[g] and flat[g] > flat[f] + marg:
                up = True
                if reach[g]:
                    ok = True
    has_up[f] = up
    if f != gmax:
        reach[f] = ok
out["local_maxima_among_functional"] = int((fr & ~has_up).sum())
out["frac_functional_reach_globalmax_uphill_SNV"] = float((reach & fr).sum() / fr.sum())
out["frac_functional_with_improving_nbr_SNV"] = float((fr & has_up).sum() / fr.sum())
# connectivity of functional set under SNV-adjacent steps
idxs = np.argwhere(func)
idmap = {tuple(ix): n for n, ix in enumerate(idxs)}
parent = list(range(len(idxs)))
def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a
nfn = np.zeros(len(idxs))
for n, ix in enumerate(idxs):
    k = 0
    for ax in range(4):
        for b in nb[ix[ax]]:
            jx = list(ix)
            jx[ax] = b
            m = idmap.get(tuple(jx))
            if m is not None:
                k += 1
                ra, rb = find(n), find(m)
                if ra != rb:
                    parent[ra] = rb
    nfn[n] = k
comp = collections.Counter(find(n) for n in range(len(idxs)))
sizes = sorted(comp.values(), reverse=True)
out["n_components"] = len(sizes)
out["frac_in_largest_component_SNV"] = sizes[0] / len(idxs)
out["wt_in_largest"] = bool(find(idmap[wt_idx]) == max(comp, key=comp.get))
out["mean_functional_snv_nbrs_of_functional"] = float(nfn.mean())
tot_snv_nbrs = np.array([sum(len(nb[i]) for i in ix) for ix in idxs])
out["frac_snv_nbrs_functional_given_functional"] = float(nfn.sum() / tot_snv_nbrs.sum())
out["frac_functional_isolated_SNV"] = float((nfn == 0).mean())
print(json.dumps(out, indent=1))
json.dump(out, open(os.path.join(D.RAW, "d1_posthoc_gb1_snv.json"), "w"), indent=1)

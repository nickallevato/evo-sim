"""Check C2c (ratio cross-validation) and C2d (chicken TSHR) and the d/s non-identifiability (THROWAWAY).
Seed: none needed (deterministic recursions, brentq).
Run: research/.venv/bin/python -I research/checks/c2_ratio_nonident.py

PRE-REGISTERED PREDICTIONS (copied from claims C2c and C2d, 2026-10-07):
 C2c  Claimant: the TYR/SLC45A2 required-s ratio is constant for d in its plausible range because d is real.
      Opposing: the ratio is constant for EVERY d (incl. 0.2, 0.8, 2.0) because only s x d is identified.
      Verdict-changing: ratio at d = 0.2 and d = 2.0 departing from ~0.48 by more than a few percent (checked with
      the discrete recursion, not the logit approximation).
      [add, 2026-10-08, before running] Exact algebra: for the haploid-type recursion p' = p + s p q/(1+s p) the odds
      multiply by (1+s) each generation, so ln(1+s_i) * d * G_i = Delta-logit_i and the ratio of ln(1+s) is independent of d.
      The ratio of s itself should drift only through ln(1+s) ~ s curvature (a few percent over d in [0.2, 2]).
      The same invariance should hold for ANY two synthetic loci (so it is not a test of d).
 C2d  Claimant: with s fixed at the Loog point estimate, d_chicken is within 0.1 of 1.0 for any reasonable dominance model.
      Opposing: d_chicken is not identifiable from one locus; across Loog's CI and the dominance models it spans ~0.5-1.9.
      Verdict-changing: Loog's posterior with the matching dominance model giving a required-d interval excluding 0.45
      (the posterior is NOT in the repo; only the CI is used here, so only the "spans" side can be tested).
 C2   (non-identifiability) Prediction: the three Table-1 trajectories fit exactly for every d (3 equations, 4 unknowns);
      d is bounded only by the published-s ranges, i.e. by priors on s, not by the aDNA data.
 Inputs are quoted from Z18203514 (sources/raw/day/zenodo-18203514.txt, Methods 2.2, Table 1/2, 3.5): LCT 0.01(<1%)->0.75, 6,000 BP;
 SLC45A2 0.43->0.97, 4,000 BP; TYR 0.25->0.76, 5,000 BP; 25 y/generation (G = 240/160/200, the value that reproduces
 Table 1 per the R2 recompute); published s: LCT 0.04-0.10 (Table 1 uses 0.05), SLC45A2 0.04-0.05, TYR 0.02-0.04;
 chicken p0=0.44 -> 0.97, G=900, s=0.0049 (CI 0.0029-0.0088).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.optimize import brentq

def step(p, s, model):
    if model == "additive":   # Day's recursion (haploid-type / genic)
        return p + s * p * (1 - p) / (1 + s * p)
    if model == "dominant":   # AA, Aa: 1+s ; aa: 1
        q = 1 - p
        return p * (1 + s) / (1 + s * (1 - q * q))
    if model == "recessive":  # AA: 1+s ; Aa, aa: 1
        return p + s * p * p * (1 - p) / (1 + s * p * p)
    raise ValueError(model)

def final(p0, s, Geff, model="additive"):
    """Iterate floor(Geff) generations and interpolate linearly in the last fractional generation."""
    n = int(np.floor(Geff))
    p = p0
    for _ in range(n):
        p = step(p, s, model)
    frac = Geff - n
    if frac > 0:
        p = p + frac * (step(p, s, model) - p)
    return p

def req_s(p0, p1, Geff, model="additive"):
    return brentq(lambda s: final(p0, s, Geff, model) - p1, 1e-7, 2.0)

def req_d(p0, p1, G, s, model="additive"):
    f = lambda d: final(p0, s, d * G, model) - p1
    if f(1e-3) > 0: return 0.0      # even ~no selection time overshoots
    if f(25.0) < 0: return float("inf")   # cannot reach p1 even with 25x the generations
    return brentq(f, 1e-3, 25.0)

logit = lambda p: np.log(p / (1 - p))
LOCI = {"LCT": (0.01, 0.75, 240, (0.04, 0.10)), "SLC45A2": (0.43, 0.97, 160, (0.04, 0.05)), "TYR": (0.25, 0.76, 200, (0.02, 0.04))}

print("sanity: iterated recursion vs closed form odds*(1+s)^G:")
p = final(0.01, 0.05, 240); cf = 1 / (1 + np.exp(-(logit(0.01) + 240 * np.log(1.05))))
print(f"  iterate {p:.6f} closed form {cf:.6f}")

print("\n== C2c: required s for the Table-1 inputs as a function of d (additive recursion, exact) ==")
print("   d     s_SLC45A2  s_TYR   ratio TYR/SLC   s*d(SLC)  s*d(TYR)")
for d in (0.05, 0.1, 0.2, 0.4, 0.45, 0.5, 0.6, 0.8, 1.0, 1.5, 2.0):
    sS = req_s(0.43, 0.97, d * 160); sT = req_s(0.25, 0.76, d * 200)
    print(f"  {d:4.2f}   {sS:8.4f}  {sT:8.4f}   {sT/sS:8.4f}      {sS*d:7.4f}   {sT*d:7.4f}")
print(" paper Table 3: ratios 0.48, 0.49, 0.49, 0.49 at d = 0.4, 0.5, 0.6, 1.0")
print("\n Synthetic loci pairs (arbitrary p0, p1, G): ratio of required s is also ~constant in d -> not a test of d")
rng = np.random.default_rng(1)
for _ in range(4):
    p0a, p0b = rng.uniform(0.02, 0.5, 2); p1a, p1b = rng.uniform(0.6, 0.98, 2); Ga, Gb = rng.integers(80, 300, 2)
    rs = [req_s(p0b, p1b, d * Gb) / req_s(p0a, p1a, d * Ga) for d in (0.2, 0.5, 1.0, 2.0)]
    print(f"  loci A({p0a:.2f}->{p1a:.2f},G={Ga}) B({p0b:.2f}->{p1b:.2f},G={Gb}): ratio at d=0.2,0.5,1,2 = " + ", ".join(f"{r:.3f}" for r in rs))

print("\n== d interval consistent with PUBLISHED s ranges (additive recursion; Day's own inputs) ==")
lo_all, hi_all = 0.0, 9.0
for name, (p0, p1, G, (s_lo, s_hi)) in LOCI.items():
    d_lo = req_d(p0, p1, G, s_hi); d_hi = req_d(p0, p1, G, s_lo)
    print(f"  {name:8s} s in [{s_lo},{s_hi}] -> d in [{d_lo:.3f}, {d_hi:.3f}]  (d at the s used for Table 1/2: {req_d(p0,p1,G,0.05 if name!='TYR' else 0.03):.3f})")
    lo_all, hi_all = max(lo_all, d_lo), min(hi_all, d_hi)
print(f"  intersection: d in [{lo_all:.3f}, {hi_all:.3f}];  d = 1 requires s = {[round(req_s(p0,p1,G),4) for (p0,p1,G,_) in LOCI.values()]} (all below the published ranges)")
for f in (0.75, 1.25):
    lo_a, hi_a = 0.0, 9.0
    for name, (p0, p1, G, (s_lo, s_hi)) in LOCI.items():
        lo_a = max(lo_a, req_d(p0, p1, G, s_hi * f)); hi_a = min(hi_a, req_d(p0, p1, G, s_lo * f))
    print(f"  with all published s ranges scaled x{f}: intersection d in [{lo_a:.3f}, {hi_a:.3f}]")

print("\n== Non-identifiability: exact fit for every d (3 equations, 4 unknowns) ==")
for d in (0.2, 0.45, 1.0, 1.8):
    resid = [final(p0, req_s(p0, p1, d * G), d * G) - p1 for (p0, p1, G, _) in LOCI.values()]
    print(f"  d={d}: max |residual| = {max(abs(r) for r in resid):.1e}; required s = " +
          ", ".join(f"{req_s(p0,p1,d*G):.4f}" for (p0, p1, G, _) in LOCI.values()))

print("\n== Same trajectories from other causes (all give d_eff = 0.45 with d = 1) ==")
for name, (p0, p1, G, _) in LOCI.items():
    s_pub = 0.05 if name != "TYR" else 0.03
    d_need = req_d(p0, p1, G, s_pub)
    print(f"  {name}: at the paper's s={s_pub} the data need d={d_need:.3f}  == selection starting {(1-d_need)*G*25:.0f} y later than the stated date, "
          f"or a generation length of {25/d_need:.0f} y, or s lower by x{d_need:.2f}")
print("\n  Dominance (d needed at the paper's s; LCT is usually modelled dominant, TSHR recessive):")
for name, (p0, p1, G, _) in LOCI.items():
    s_pub = 0.05 if name != "TYR" else 0.03
    print(f"  {name}: " + ", ".join(f"{m}: {req_d(p0,p1,G,s_pub,m):.3f}" for m in ("additive", "dominant", "recessive")))

print("\n== C2d: chicken TSHR (p0=0.44 -> 0.97, G=900) ==")
print(" model        s=0.0029   s=0.0049   s=0.0088   | final p at d=1 (s=.0049)   at d=0.45")
for m in ("additive", "recessive", "dominant"):
    ds = [req_d(0.44, 0.97, 900, s, m) for s in (0.0029, 0.0049, 0.0088)]
    print(f" {m:10s}   {ds[0]:7.3f}    {ds[1]:7.3f}    {ds[2]:7.3f}   |  {final(0.44,0.0049,900,m):.3f}                  {final(0.44,0.0049,0.45*900,m):.3f}")
print(" paper: d_chicken = 1.02 (its text: 'predicted final frequency would be only ~0.68-0.72' at d=0.45)")

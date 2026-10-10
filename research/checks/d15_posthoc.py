"""D15 post hoc analysis: post hoc, after reviews 2935b8f.

Nothing here was pre-registered. It re-reads the stored sweep `results/raw/d15_sweep.jsonl` (714 rows; no
simulation) and does closed-form chain arithmetic only. Trivial size (<1 s, <100 MB), so it runs on the
workstation under the AGENTS.md limit. Output: `results/raw/d15_posthoc.out`.

Sections (each answers a review finding; see R4-D15.md "Review resolution"):
  A. Scorecards: in-scope (m >= 2, kmult <= 1, neutral/valley; Day/Hossjer's stated premises) beside the
     full grid; "exceeds" (p9) and "far exceeds" (p90) columns; 25 y and 20 y windows.   [Day M1, crit m1, corr m3/m8]
  B. Censored-exponential MLE (total_time / n_fin) against the fixed-state chain, Fin/S/V4 cells.   [corr M1]
  C. Neutral sim mean - chain against the conditional neutral fixation time ~4 N_e.   [corr M2]
  D. The 28 wall-guard cells described exactly.   [corr m1]
  E. Stationary P(done) per gene implied by each kmult (two-state uf/(uf+ub)).   [Day m3, crit m2]
  F. "Any m of M genes" (gene-set specificity) for the neutral fixed-state chain at W = 6, kmult = 1:
     disjoint subsets (Hossjer 2021 eq. D.2) and all subsets (birth-death count of done genes).   [crit M1]
     Origination times only; add ~4 N_e generations of fixation sojourn for total time (section C).
  G. Hossjer 2021 Table 5 values recomputed with the stored `hossjer_ET` (W=6, d_max = 0, 1), and the same
     chain from an all-absent ("new binding site") start with his back rate k01.  [crit M2, corr m5]
     (Section G's absent-start block was appended after the first run of this script, same session.)

Pre-stated expectations (written before the first run of this script, from the reviews' own recomputations):
  A in-scope 96/96 hold and far; B N_e=1e4 Fin kmult=1 chain/MLE ~0.9-1.1, N_e=1e5 Fin2 m=2 ~4-5;
  C sim - chain ~4e5 at N_e=1e5 (19 complete cells), ~4e4 at N_e=1e4; F any-4-of-2e4 E[T] ~1.4e4 generations.
"""
import json
import math
import os
import sys
from collections import defaultdict

import numpy as np
from scipy.linalg import expm

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from d15_waiting_time import UF0, UB0, T9, T9_20, FIT, chain_ET, hossjer_ET, words  # noqa: E402

RAW = os.path.join(HERE, "results", "raw")
rows = [json.loads(l) for l in open(os.path.join(RAW, "d15_sweep.jsonl"))]
assert len(rows) == 714, len(rows)
NV = ("N", "V4", "V3", "V2")
FAM = ["N", "V4", "V3", "V2", "Fin2", "Fin3", "S2", "S3"]


def k(r):
    return "1/12" if r["kmult"] < 0.5 else f"{r['kmult']:g}"


def tally(rs):
    n = len(rs)
    return (n, sum(r["p9"] <= 0.05 for r in rs), sum(r["p9"] >= 0.5 for r in rs), sum(r["p90"] <= 0.05 for r in rs),
            sum(r["p9_20"] <= 0.05 for r in rs), sum(r["p9_20"] >= 0.5 for r in rs))


def line(lbl, t):
    print(f"  {lbl:34s} cells {t[0]:3d} | 25y: exceeds {t[1]:3d} fails {t[2]:3d} far {t[3]:3d}"
          f" | 20y: exceeds {t[4]:3d} fails {t[5]:3d}")


print("=" * 100)
print("A. Scorecards (exceeds = p9<=.05; fails = p9>=.5; far = p90<=.05 at 25 y; 20 y uses p9_20; p90 is 25 y only)")
ins = [r for r in rows if r["m"] >= 2 and r["kmult"] <= 1 and r["F"] in NV]
line("IN-SCOPE m>=2, kmult<=1, N/V", tally(ins))
print(f"  in-scope max p9 {max(r['p9'] for r in ins):.3f}, max p9_20 {max(r['p9_20'] for r in ins):.3f},"
      f" max p90 {max(r['p90'] for r in ins):.3f}")
for F in NV:
    line(f"  in-scope {F}", tally([r for r in ins if r["F"] == F]))
line("FULL GRID (assumption map)", tally(rows))
line("m>=2 only", tally([r for r in rows if r["m"] >= 2]))
for F in FAM:
    for Ne in (1e4, 1e5):
        line(f"  {F} Ne={Ne:.0e}", tally([r for r in rows if r["F"] == F and r["Ne"] == Ne]))
nv3 = [r for r in rows if r["F"] in NV and r["kmult"] <= 3 and r["p90"] > 0.05]
print("  N/V cells kmult<=3 with p90>0.05 (exceeds but not far):",
      [(r["F"], r["m"], r["rho"], k(r), f"{r['Ne']:.0e}", round(r["p90"], 3)) for r in nv3])

print("=" * 100)
print("B. Censored-exponential MLE = total_time/n_fin (SE ~ MLE/sqrt(n_fin)) vs fixed-state chain")
for r in sorted(rows, key=lambda r: (r["F"], r["Ne"], r["m"], r["rho"])):
    if r["kmult"] != 1 or r["F"] not in ("Fin2", "Fin3", "S2", "S3", "V4") or r["n_fin"] == 0:
        continue
    mle = r["total_time"] / r["n_fin"]
    print(f"  {r['F']:4s} Ne={r['Ne']:.0e} m={r['m']} rho={r['rho']} f={r['f']:g} n_fin={r['n_fin']:2d}"
          f"  mean_fin {r['mean_fin']:.3g}  MLE {mle:.3g} (+-{100 / math.sqrt(r['n_fin']):.0f}%)"
          f"  chain {r['pred_chain']:.3g}  chain/MLE {r['pred_chain'] / mle:.2f}  chain/mean_fin {r['pred_chain'] / r['mean_fin']:.2f}")

print("=" * 100)
print("C. Neutral cells with n_fin=60: sim mean - chain vs 4*N_e (conditional neutral fixation time)")
for Ne in (1e4, 1e5):
    cs = [r for r in rows if r["F"] == "N" and r["Ne"] == Ne and r["n_fin"] == 60]
    ex = np.array([r["mean_fin"] - r["pred_chain"] for r in cs])
    z = np.array([(r["mean_fin"] - r["pred_chain"] - 4 * Ne) / (r["mean_fin"] / math.sqrt(60)) for r in cs])
    print(f"  Ne={Ne:.0e}: {len(cs)} cells; mean excess {ex.mean():.3g} (4Ne = {4 * Ne:.3g}); "
          f"z vs 4Ne range [{z.min():.2f}, {z.max():.2f}]; |z|<=2 in {int((abs(z) <= 2).sum())}/{len(cs)}")
    for r, e, zz in zip(cs, ex, z):
        print(f"     m={r['m']} rho={r['rho']} k={k(r):5s} f={r['f']:g} mean {r['mean_fin']:.3g} chain {r['pred_chain']:.3g}"
              f" ratio {r['mean_fin'] / r['pred_chain']:.2f} excess {e:.3g} z {zz:+.2f}")
print(f"  4e5 generations at 25 y = {4e5 * 25 / 1e6:.1f} My; at 20 y = {4e5 * 20 / 1e6:.1f} My; T9 = {T9:.0f} gens")

print("=" * 100)
print("D. Wall-guard cells (complete_at_900My false)")
g = [r for r in rows if not r["complete_at_900My"]]
byF = defaultdict(int)
for r in g:
    byF[(r["F"], f"{r['Ne']:.0e}")] += 1
print(f"  {len(g)} cells; by family/N_e: {dict(byF)}")
print(f"  min censor clock {min(r['min_censor_clock'] for r in g):.3g} gens; max {max(r['min_censor_clock'] for r in g):.3g}"
      f" (= {min(r['min_censor_clock'] for r in g) * 25 / 1e6:.0f}-{max(r['min_censor_clock'] for r in g) * 25 / 1e6:.0f} My at 25 y)")
for r in sorted(g, key=lambda r: (r["F"], r["m"], r["kmult"], r["rho"])):
    print(f"     {r['F']:3s} m={r['m']} rho={r['rho']} k={k(r):5s} n_fin={r['n_fin']:2d} p9={r['p9']:.3f} p90={r['p90']:.3f}"
          f" min_clock={r['min_censor_clock']:.3g}")
vv = [r for r in rows if r["F"] in ("V3", "V2") and r["n_fin"] > 0]
print("  V2/V3 cells with any finished replicate:",
      [(r["F"], r["m"], r["rho"], k(r), f"{r['Ne']:.0e}", r["n_fin"], r["complete_at_900My"]) for r in vv])

print("=" * 100)
print("E. Stationary P(done) per gene, two-state uf/(uf+ub), uf = kmult*UF0, ub = UB0")
for km in (1 / 12, 1, 3, 10, 15, 30, 100):
    uf = km * UF0
    print(f"  kmult {km:7.4g}: P(done) {uf / (uf + UB0):.3f}")
E0, _, _ = words(6, 0)
print(f"  Hossjer stationary at W=6 d_max=0: 1-exp(-E0) = {1 - math.exp(-E0):.3f} (E0 = {E0:.3f});"
      f" at W=6 d_max=1: E0 = {words(6, 1)[0]:.2f}, P(present) = {1 - math.exp(-words(6, 1)[0]):.3f}")

print("=" * 100)
print("F. Any m of M genes, neutral fixed-state chain, W=6 kmult=1 (origination times; add ~4Ne for fixation)")


def bd_generator(M, m, uf, ub):
    """Count j of done genes among M exchangeable genes; absorbing at j = m. States 0..m."""
    A = np.zeros((m + 1, m + 1))
    for j in range(m):
        fw, bw = (M - j) * uf, j * ub
        A[j, j + 1] += fw
        if j > 0:
            A[j, j - 1] += bw
        A[j, j] -= fw + bw
    return A


def bd_stats(M, m, uf, ub, t):
    A = bd_generator(M, m, uf, ub)
    ET = np.linalg.solve(-A[:m, :m], np.ones(m))[0]
    P = expm(A * t)[0, m]
    return ET, P


uf, ub = UF0, UB0
for m in (2, 4, 5):
    ETm, Pm = bd_stats(m, m, uf, ub, T9)
    print(f"  m={m}: specific set E[T] {ETm:.3g} gens, P(T<=T9) {Pm:.2e}")
    for M in (10, 100, 1000, 20000):
        if M < m:
            continue
        ETa, Pa = bd_stats(M, m, uf, ub, T9)
        Pd = 1 - (1 - Pm) ** (M // m)   # eq. D.2, disjoint subsets
        print(f"     M={M:6d}: all subsets E[T] {ETa:.3g} gens ({ETa * 25 / 1e6:.3g} My), P(T<=T9) {Pa:.3f};"
              f"  disjoint (D.2) P(T<=T9) {Pd:.3g}")
pst = uf / (uf + ub)
print(f"  Stationary start: P(gene already done) = {pst:.3f}; expected done genes among M = 20000: {pst * 20000:.0f}"
      f" (any-m-of-M target met at t = 0 for every m << {pst * 20000:.0f})")

print("=" * 100)
print("G. Hossjer 2021 Tables 5 and 9 (W=6, K=1, c=1, neutral), stored hossjer_ET")
for dm in (0, 1):
    E0, E1, k10 = words(6, dm)
    print(f"  d_max={dm}: E0 {E0:.2f}  k10 {k10:.3g}  E[T1] {hossjer_ET(1, 6, dm):.4g}  E[T2] {hossjer_ET(2, 6, dm):.4g}"
          f"  (source Table 5: d_max=0 5.3813e7 / 2.0518e8; d_max=1 4.5271e4 / 9.0758e4)")
print("  Absent start ('new binding site'), same rates (k01 = k10*kappa/(1-kappa), Hossjer's back rate, c = 1):")
for dm in (0, 1):
    E0, E1, k10 = words(6, dm)
    kap = math.exp(-E0)
    k01 = k10 * kap / (1 - kap)
    for m in (1, 2):
        A = np.zeros((m + 1, m + 1))
        for j in range(m):
            A[j, j + 1] += (m - j) * k10
            if j > 0:
                A[j, j - 1] += j * k01
            A[j, j] -= (m - j) * k10 + (j * k01 if j > 0 else 0)
        ET = np.linalg.solve(-A[:m, :m], np.ones(m))[0]
        P9 = expm(A * T9)[0, m]
        print(f"    d_max={dm} m={m}: k10 {k10:.3g} (= {k10 / UF0:.1f} x UF0), k01 {k01:.3g}; E[T | absent start] {ET:.3g} gens"
              f" ({ET * 25 / 1e6:.0f} My at 25 y); P(T<=T9) {P9:.3f}")

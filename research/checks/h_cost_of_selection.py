"""Check H (THROWAWAY): Haldane's cost of selection, hard vs soft selection, Nunney's M-dependence.
Seed: SeedSequence(20261008). Run: research/.venv/bin/python -I research/checks/h_cost_of_selection.py

PRE-REGISTERED PREDICTIONS (copied from claims H, H1, H2, H5, H8 before any run; the numbered extras
P-b1..P-b6 were written 2026-10-08 before the full IBM scan, after only a 3-run smoke test of speed):
 (a) H: 30/0.10 = 300; 146,250/300 = 487; D=30 is an INPUT (Haldane's 'typical'), not derived. Predict that
     D = ln(1/p0) (haploid) needs p0 ~ 1e-13 to give 30, and that realistic standing-variation p0 (1e-3..1e-6)
     gives D ~ 7-14 (diploid additive about twice the haploid value) -> interval 70-140 gens at 10%.
 (b) H2 (claimant Day): minimum interval is ~300 independent of M; parallel loci cost additively.
     Opposing (Nunney 2003): hard-selection cost 'substantially less' for M>1/2; rises in an accelerating
     fashion for M<1/2; C = C0(M)+n*C1(M) (positive intercept); soft selection 'eliminates or reduces' the cost.
     Extra predictions for MY reconstruction:
     P-b1 hard, M large: T_min rises linearly in n with positive intercept (Nunney's Fig.1 shape).
     P-b2 hard: T_min falls with R roughly as 1/ln(R/2) near R~2 (reproductive excess = selective-death budget)
          and saturates at large R (sweep time limit); at R=2.2 (budget ~10%) hard T_min >> soft-at-large-R.
     P-b3 hard: T_min ~independent of s while 2ns < ln(R/2) (Haldane: cost independent of s); fails outright
          for larger s (load at the shift exceeds the budget).
     P-b4 soft with large R: T_min set by sweep time ~ 1/s, ~independent of n and of R once R is ample;
          at R=2.2 soft is also limited (juvenile surplus only 10%).
     P-b5 both regimes: T_min rises steeply when M < ~0.5 (loss of rare mutants), soft and hard converge there.
     P-b6 sequential (staggered) vs concurrent loci: no large difference (Nunney: peaks evenly spaced 'extremely
          high' correspondence).
 (c) H8: Term 3 = 1 per 39 gens vs Haldane+d 1 per 667 (=300/0.45) per generation at the same d: ratio 17.1, not 7.7
     (7.7 compares Term 3 WITH d against Haldane WITHOUT d). H5: Hossjer's 15,800 is 10.5x Haldane's own 1,500.
     H1: the retraction's scope reasoning (cost bounds selected substitutions, not total) applies to H as well.
 Verdict-changing result: hard-selection limit independent of M and ~1/300 at human-like M -> supports H;
 limit >> 1/300 at M>1 or under soft selection -> supports H2 as a premise-challenge.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from multiprocessing import Pool
import wf_hc as h

# ------------------------------------------------------------------ (a) analytic
def part_a():
    print("== (a) Haldane arithmetic ==")
    print("m/D = 0.10/30 per generation -> interval", 30 / 0.10, "generations;  146250/300 =", 146250 / 300)
    print(" p0      D_haploid=ln(1/p0)   D_diploid(additive,s=0.01)   D_diploid(s=0.001)   gens/subst at 10%")
    for p0 in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
        Dh = h.haldane_D_haploid(p0)
        D1 = h.haldane_D_diploid(p0, 0.01)
        D2 = h.haldane_D_diploid(p0, 0.001)
        print(f" {p0:7.0e} {Dh:8.2f}             {D1:8.2f}                   {D2:8.2f}           {D1/0.1:7.0f}")
    print(f"p0 giving D=30: haploid {np.exp(-30):.2e}; diploid additive (s=0.01) ~", end=" ")
    for lp in np.arange(-5, -40, -0.25):
        if h.haldane_D_diploid(np.exp(lp), 0.01) >= 30:
            print(f"{np.exp(lp):.1e}")
            break
    print("Note: D=30 is Haldane's 'typical' input; here it is only a re-derivation of the 300 from D and m.")

# ------------------------------------------------------------------ (c) arithmetic
def part_c():
    print("\n== (c) Day's cost figures ==")
    d = 0.45
    ne, L, smax = 3300, 3.1e9, 1.0
    k_site = smax * d / (2 * L * np.log(2 * ne))
    K_sel = k_site * L
    print(f"Term 3 per site {k_site:.3e}; genome-wide {K_sel:.4f}/gen = 1 per {1/K_sel:.1f} generations")
    print(f"Term 3 implied cost per substitution 2 ln(2Ne) = {2*np.log(2*ne):.2f} (Haldane D = 30); budget s_max = 1.0 (Haldane m = 0.10)")
    print(f"Haldane+d per generation = {d/300:.5f} (1 per {300/d:.0f}); Term 3 / Haldane+d = {K_sel/(d/300):.1f}; "
          f"Term 3 / Haldane(no d) = {K_sel/(1/300):.1f}; Term3(no d)/Haldane(no d) = {(1/(2*np.log(2*ne)))/(1/300):.1f}")
    print(f"s_max=0.1 in Term 3 -> 1 per {1/(K_sel*0.1):.0f} gens (R2 said ~390)")
    for G, lab in [(325000, "2025 (325k gens)"), (450000, "2019 (450k)"), (252000, "MITTENS 3.0 (252k)"), (260000, "Term-3 window")]:
        print(f"  {lab}: Haldane {G/300:,.0f}; Haldane+d {G*d/300:,.0f}; Term 3 {G*K_sel:,.0f}")
    print(f"Hossjer: Haldane over 450,000 gens = {450000/300:.0f} (675 with d); his 'equation (3)' 15,800 is {15800/1500:.1f}x Haldane")
    print("Required: 20M/487 =", round(20e6/487), "; 17.5M/6650 =", round(17.5e6/6650))
    print("Scope (H1 retraction): cost bounds SELECTED substitutions only; neutral fixation rate = mu (B0.5, k=U, z=+0.13/-0.64)")

# ------------------------------------------------------------------ (b) IBM
GRID = [6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512, 768, 1024]

def cond(args):
    (label, K, n, s, R, M, regime, stagger, seed, reps, cycles) = args
    rng = np.random.default_rng(np.random.SeedSequence(seed))
    u = M / (2 * K)
    fr = []
    good_streak = 0
    for T in GRID:
        ok = 0
        for _ in range(reps):
            succ, _ = h.treadmill_success(K=K, n=n, T=T, s=s, R=R, u=u, regime=regime, cycles=cycles, rng=rng, stagger=stagger)
            ok += succ
        fr.append(ok / reps)
        good_streak = good_streak + 1 if ok / reps >= 0.875 else 0
        if good_streak >= 2:
            break
    # 50% crossing, geometric interpolation
    T50 = np.nan
    for i, f in enumerate(fr):
        if f >= 0.5:
            if i == 0: T50 = GRID[0]
            else:
                f0, f1 = fr[i - 1], f
                t0, t1 = GRID[i - 1], GRID[i]
                T50 = float(np.exp(np.log(t0) + (0.5 - f0) / (f1 - f0) * (np.log(t1) - np.log(t0))))
            break
    return dict(label=label, K=K, n=n, s=s, R=R, M=M, regime=regime, stagger=stagger, fr=fr, T50=T50)

def build():
    base = np.random.SeedSequence(20261008)
    conds = []
    cid = [0]
    def add(label, K, n, s, R, M, regime, stagger=False, reps=8, cycles=5):
        cid[0] += 1
        conds.append((label, K, n, s, R, M, regime, stagger, int(base.spawn(1)[0].generate_state(1)[0]) + cid[0], reps, cycles))
    for reg in ("hard", "soft"):
        for R in (2.2, 3, 5, 10, 40):
            add("A:R-scan s=.03", 500, 1, 0.03, R, 2.0, reg)
            add("A:R-scan s=.10", 500, 1, 0.10, R, 2.0, reg)
        for M in (0.1, 0.25, 0.5, 1.0, 2.0, 10.0):
            add("B:M-scan R=10 s=.1", 500, 1, 0.10, 10, M, reg)
        for s in (0.01, 0.03, 0.1, 0.3):
            add("C:s-scan R=3", 500, 1, s, 3, 2.0, reg)
        for n in (1, 2, 3, 5):
            add("D:n-scan R=10 (s=.2/n) sync", 500, n, 0.2 / n, 10, 2.0, reg)
            add("D:n-scan R=10 (s=.2/n) sync M=10", 500, n, 0.2 / n, 10, 10.0, reg)
        for n in (3, 5):
            add("D:n-scan R=10 (s=.2/n) staggered", 500, n, 0.2 / n, 10, 2.0, reg, stagger=True)
    return conds

def part_b():
    print("\n== (b) IBM: max sustainable substitution rate (T50 = interval at 50% persistence, 8 reps/T) ==")
    conds = build()
    with Pool(3) as p:
        res = p.map(cond, conds, chunksize=1)
    last = None
    for r in sorted(res, key=lambda r: (r["label"], r["regime"], r["n"], r["s"], r["R"], r["M"], r["stagger"])):
        if r["label"] != last:
            print("\n#", r["label"]); last = r["label"]
        rate = r["n"] / r["T50"] if r["T50"] == r["T50"] else np.nan
        ceil = " (no success at T<=%d)" % GRID[len(r["fr"]) - 1] if r["T50"] != r["T50"] else ""
        print(f" {r['regime']:4s} n={r['n']} s={r['s']:.3f} R={r['R']:<4} M={r['M']:<5} T50={r['T50']:7.1f} rate n/T50={rate:.4f}/gen"
              f"  Deff=T50*ln(R/2)/n={(r['T50']*np.log(r['R']/2)/r['n']):6.2f}{ceil}")
    return res

if __name__ == "__main__":
    part_a()
    part_c()
    part_b()

"""A2e post hoc analysis -- POST HOC, after reviews 2935b8f (correctness M1/m1/m3/m4/m5/m10; steelman-day D1/D2/D5/D7;
steelman-critic C1/C3/C4/C5/C6/C8).  Analysis only: reads the stored calibrations a2e_calib.jsonl / a2e_human.jsonl
of the pre-registered run (a2e_ltee_transfer.py at 7593be2) and evaluates closed forms.  No new simulation.
Nothing here was predicted in advance; every number is post hoc and labelled so in R4-A2e.md.

Run (trivial, local, one process, < 5 s):
    research/.venv/bin/python -I research/checks/a2e_posthoc.py > research/checks/results/raw/a2e_posthoc.out

Sections
  PH1  sanity: reproduce central kappa* (217) and the closed form kappa* ~ (M_L / 2N_h) R_int (u_L / u_h).
  PH2  decoupled effect size: LTEE calibration at s_L, human beneficial effect s_h (s_h <= s_L, Day s4.2 p.7
       "the remaining beneficial mutations have smaller effects").  kappa* for every stored calibration.
  PH3  human N_e 3.3e4 (Day's in-paper upper value, s8.2 p.14) and 1e5 (towards the ancestral HC N_e): kappa*, F.
  PH4  G_f = 1,408 (Day's adaptive-only figure, s4.3 p.7) by log-log interpolation of U_b between the 1,322 and
       2,890 calibrations, validated against the stored 1,587 calibration.
  PH5  coupled kappa* range with labelled corners (with and without the audit-derived G 2,887 target).
  PH6  capped F per generation (Day's own caps 1/300, 1/667, 1/39; mean-field ln R_h / D_h at R_h 1.111).
  PH7  total-substitution (neutral-inclusive) F per generation and per year (k = mu per haploid genome = 38.4).
  PH8  absolute U_b,human at the flip; adaptive-substitution count equivalent to F = 1 over 252,000 generations.
  PH9  population-level mutation supply, humans vs LTEE, on the figures derived from Day's stated factors.
  PH10 clonal human cells: event counts (floor 1 / (3 x 60,000)); cells with <= 5 events flagged as noise.
  PH11 corrected thresholds at the central calibration (kappa 125 / 652 / 10,000, all modes).
"""
import json
import math
import os

from scipy.optimize import brentq
from scipy.special import lambertw

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "results", "raw")
NE_L = (3.3e6, 1e7, 3.3e7, 1e8)
SS = (0.003, 0.01, 0.03)
NE_H = (3300, 1e4, 3.3e4, 1e5)
K_DAY = 93659  # 38.4 / 4.1e-4, derived from Day's stated factors (s4.3 p.7; s6.4 p.11 without the x100)
MAPS = {"map1.5": 1.5, "map36.8": 36.8}
LTEE_GPY = 6.64 * 365.25


# ---- engines copied verbatim in logic from a2e_ltee_transfer.py (7593be2)
def kimura_u(N, s):
    p = 1.0 / (2 * N)
    return (1 - math.exp(-4 * N * s * p)) / (1 - math.exp(-4 * N * s))


def indep_rate(M, U, s):
    return M * U * kimura_u(M // 2, s)


def eq1_free(L0, s):
    return float(lambertw(4 * s * L0).real) / 4 / s


def eq8(L0, R, s):
    f = lambda L: L - L0 * (1 - 2 * L / R) * math.exp(-4 * L * s)
    hi = min(L0, R / 2) * (1 - 1e-12)
    return brentq(f, 0.0, hi) if f(hi) > 0 else hi


def human_rate(rec, NeH, s_h, Ub_h):
    L0 = indep_rate(int(2 * NeH), Ub_h, s_h)
    if rec == "free":
        return eq1_free(L0, s_h)
    if rec == "indep":
        return L0
    return eq8(L0, MAPS[rec], s_h)


cal = [json.loads(l) for l in open(os.path.join(RAW, "a2e_calib.jsonl"))]
hum = [json.loads(l) for l in open(os.path.join(RAW, "a2e_human.jsonl"))]
C = {(r["NeL"], r["s"], r["G"]): r for r in cal}


def F(Ub_L, G, kappa, NeH, s_h, rec="map36.8", cap=None):
    k = human_rate(rec, NeH, s_h, Ub_L * kappa)
    if cap is not None:
        k = min(k, cap)
    return k * G


def kstar(Ub_L, G, NeH, s_h, rec="map36.8"):
    g = lambda lk: F(Ub_L, G, 10 ** lk, NeH, s_h, rec) - 1.0
    return 10 ** brentq(g, -3, 10) if g(-3) < 0 < g(10) else float("nan")


def ub(NeL, s, G):
    """U_b,LTEE: stored calibration, or log-log interpolation in G between 1,322 and 2,890 (PH4)."""
    if (NeL, s, G) in C:
        return C[(NeL, s, G)]["U_b"]
    a, b = C[(NeL, s, 1322)]["U_b"], C[(NeL, s, 2890)]["U_b"]
    t = (math.log(G) - math.log(1322)) / (math.log(2890) - math.log(1322))
    return math.exp(math.log(a) + t * (math.log(b) - math.log(a)))


print("# A2e post hoc (after reviews 2935b8f). Analysis only; no simulation.\n")

print("## PH1 sanity: coupled kappa* (map36.8) and closed form (M_L/2N_h) R_int (u_L/u_h)")
for s in SS:
    for NeH in (3300, 1e4):
        c = C[(3.3e7, s, 1322)]
        ks = kstar(c["U_b"], 1322, NeH, s)
        cf = (3.3e7 / (2 * NeH)) * c["R_int"] * kimura_u(int(3.3e7) // 2, s) / kimura_u(int(2 * NeH) // 2, s)
        kf = kstar(c["U_b"], 1322, NeH, s, "free")
        print(f"  s {s} N_h {NeH:g}: kappa* map36.8 {ks:.4g}, free {kf:.4g}, closed form {cf:.4g}")

print("\n## PH2 decoupled effect size (s_L = LTEE calibration, s_h = human beneficial effect); map36.8")
print("Central calibration N_e,L 3.3e7, G 1,322:")
print("| s_L | s_h | " + " | ".join(f"kappa* N_h {h:g}" for h in NE_H) + " |")
print("|---|---|" + "---|" * len(NE_H))
for sL in SS:
    for sh in (0.001, 0.003, 0.01, 0.03):
        if sh > sL:
            continue
        print(f"| {sL} | {sh} | " + " | ".join(f"{kstar(C[(3.3e7, sL, 1322)]['U_b'], 1322, h, sh):.4g}" for h in NE_H) + " |")
cells, over = 0, []
for NeL in NE_L:
    for sL in SS:
        for G in (1322, 2890):
            for sh in (0.001, 0.003):
                for NeH in (3300, 1e4):
                    cells += 1
                    k = kstar(C[(NeL, sL, G)]["U_b"], G, NeH, sh)
                    if k > K_DAY:
                        over.append((NeL, sL, G, sh, NeH, k))
print(f"Reviewer grid (4 N_e,L x 3 s_L x 2 G x s_h {{0.001, 0.003}} x N_h {{3300, 1e4}} = {cells} cells): "
      f"{len(over)} with kappa* > {K_DAY}:")
for o in over:
    print(f"  N_e,L {o[0]:.2g} s_L {o[1]} G {o[2]} s_h {o[3]} N_h {o[4]:g}: kappa* {o[5]:.4g}")
for Gset, lab in (((1322,), "G 1,322 only"), ((1322, 1408), "G 1,322 and 1,408 (interp.)")):
    n, m = 0, 0
    for NeL in NE_L:
        for sL in SS:
            for G in Gset:
                for sh in (0.001, 0.003, 0.01, 0.03):
                    if sh > sL:
                        continue
                    for NeH in NE_H:
                        n += 1
                        m += kstar(ub(NeL, sL, G), G, NeH, sh) > K_DAY
    print(f"Wider grid, {lab}, s_h <= s_L, N_h in {NE_H}: {m}/{n} cells with kappa* > {K_DAY}")

print("\n## PH3 human N_e 3.3e4 and 1e5 (coupled s, map36.8)")
for NeH in NE_H:
    row = [f"s {s}: kappa* {kstar(C[(3.3e7, s, 1322)]['U_b'], 1322, NeH, s):.4g}, "
           f"F(125) {F(C[(3.3e7, s, 1322)]['U_b'], 1322, 125, NeH, s):.3g}, "
           f"F(93659) {F(C[(3.3e7, s, 1322)]['U_b'], 1322, K_DAY, NeH, s):.4g}" for s in SS]
    allk = [kstar(r["U_b"], r["G"], NeH, r["s"]) for r in cal]
    print(f"  N_h {NeH:g}: " + "; ".join(row) + f"  | all calibrations kappa* {min(allk):.3g}-{max(allk):.4g}")

print("\n## PH4 G_f = 1,408 (Day's adaptive-only figure) by log-log interpolation of U_b")
a, b = C[(3.3e7, 0.01, 1322)]["U_b"], C[(3.3e7, 0.01, 2890)]["U_b"]
t = (math.log(1587) - math.log(1322)) / (math.log(2890) - math.log(1322))
interp1587 = math.exp(math.log(a) + t * (math.log(b) - math.log(a)))
print(f"  validation at central (3.3e7, 0.01): interpolated U_b(1587) {interp1587:.4g} vs calibrated "
      f"{C[(3.3e7, 0.01, 1587)]['U_b']:.4g} (ratio {interp1587 / C[(3.3e7, 0.01, 1587)]['U_b']:.3f}); "
      f"kappa* interp {kstar(interp1587, 1587, 1e4, 0.01):.4g} vs calibrated {kstar(C[(3.3e7, 0.01, 1587)]['U_b'], 1587, 1e4, 0.01):.4g}")
for s in SS:
    print(f"  s {s}: kappa* at G 1,408 (N_e,L 3.3e7): " + ", ".join(
        f"N_h {h:g}: {kstar(ub(3.3e7, s, 1408), 1408, h, s):.4g}" for h in NE_H) +
          f"; F(93659, N_h 1e4) {F(ub(3.3e7, s, 1408), 1408, K_DAY, 1e4, s):.4g}")
c1, c2 = C[(3.3e7, 0.01, 1322)]["U_b"], C[(3.3e7, 0.01, 1587)]["U_b"]
t = (math.log(1408) - math.log(1322)) / (math.log(1587) - math.log(1322))
u1408 = math.exp(math.log(c1) + t * (math.log(c2) - math.log(c1)))
print(f"  central s 0.01, piecewise log-log between the calibrated 1,322 and 1,587 points: U_b {u1408:.4g}, "
      f"kappa* N_h 1e4 {kstar(u1408, 1408, 1e4, 0.01):.4g} (the 1,322-2,890 interpolation above under-reads the "
      f"1,587 check by ~16%, so the 1,408 values are approximate; both lie between 217 and 362)")

print("\n## PH5 coupled kappa* range (map36.8) with labelled corners")
for Gs, lab in (((1322, 1587, 2890), "all stored targets incl. audit-derived 2,887"),
                ((1322, 1587), "Day's targets 1,322 / 1,587 only"), ((1322, 1408, 1587), "1,322 / 1,408 / 1,587")):
    for NeHs in ((3300, 1e4), NE_H):
        pts = []
        for NeL in NE_L:
            for s in SS:
                for G in Gs:
                    if G == 1587 and (NeL, s) != (3.3e7, 0.01):
                        continue
                    for NeH in NeHs:
                        pts.append((kstar(ub(NeL, s, G), G, NeH, s), NeL, s, G, NeH))
        lo, hi = min(pts), max(pts)
        print(f"  {lab}, N_h {NeHs}: kappa* {lo[0]:.3g} (N_e,L {lo[1]:.2g}, s {lo[2]}, G {lo[3]}, N_h {lo[4]:g}) - "
              f"{hi[0]:.4g} (N_e,L {hi[1]:.2g}, s {hi[2]}, G {hi[3]}, N_h {hi[4]:g}); "
              f"margin to 93,659: {K_DAY / hi[0]:.3g}x - {K_DAY / lo[0]:.3g}x")

print("\n## PH6 capped F per generation at kappa 93,659 (coupled s, N_e,L 3.3e7, G 1,322)")
caps = (("Haldane 1/300", 1 / 300), ("Haldane + d 1/667", 0.45 / 300), ("Term 3 1/39", 1 / 39))
for NeH in (3300, 1e4):
    D = 2 * math.log(2 * NeH) + 2
    cl = caps + ((f"mean-field R_h 1.111 (D {D:.1f})", math.log(1 / 0.9) / D),)
    for s in SS:
        u = C[(3.3e7, s, 1322)]["U_b"]
        unc = F(u, 1322, K_DAY, NeH, s)
        print(f"  N_h {NeH:g} s {s}: uncapped {unc:.4g}; " + "; ".join(
            f"{lab} {F(u, 1322, K_DAY, NeH, s, cap=c):.3g}" for lab, c in cl))
print("  caps are all > 1/1,322, so they never move kappa*; capped F > 1 wherever uncapped F exceeds the cap.")
print("  capped F by G target (Haldane+d / Haldane / Term 3): " + "; ".join(
    f"G {g}: {g * 0.45 / 300:.2f} / {g / 300:.2f} / {g / 39:.1f}" for g in (1322, 1408, 1587)))

print("\n## PH7 total-substitution (neutral-inclusive) F: human k = mu = 38.4 per haploid genome per generation")
for G, lab in ((1322, "MITTENS 3.0 total"), (1587, "2nd ed. total")):
    print(f"  G {G} ({lab}): F per generation {38.4 * G:,.0f}; per year " + ", ".join(
        f"{y} y {38.4 * G / (LTEE_GPY * y):.3f}" for y in (20, 25, 29)))
print("  (1,408 and 2,887 are adaptive-only and not the like-for-like denominator for a total rate.)")
print("  sensitivity: F = 1 per generation would need a human total substitution rate <= 1/1,322 = "
      f"{1 / 1322:.2e} per haploid genome per generation, i.e. a neutral rate {38.4 * 1322:,.0f}x below mu.")

print("\n## PH8 absolute thresholds at the flip (coupled s, N_e,L 3.3e7, G 1,322, map36.8)")
for s in SS:
    u = C[(3.3e7, s, 1322)]["U_b"]
    print(f"  s {s}: U_b,LTEE {u:.3g}; U_b,human at flip: " + ", ".join(
        f"N_h {h:g}: {kstar(u, 1322, h, s) * u:.3g}" for h in NE_H))
print(f"  F = 1 over 252,000 generations = {252000 / 1322:.1f} adaptive substitutions per lineage (Day s7.3: 191).")

print("\n## PH9 population mutation supply per generation (38.4 per haploid human genome; 4.1e-4 per LTEE genome)")
for NeH in NE_H:
    hs = 2 * NeH * 38.4
    print(f"  humans N_h {NeH:g}: {hs:,.0f}; vs LTEE " + ", ".join(
        f"N_e,L {n:.2g}: {n * 4.1e-4:,.0f} ({hs / (n * 4.1e-4):.3g}x)" for n in NE_L))

print("\n## PH10 clonal human cells: events = k x 3 reps x 60,000 gen (floor 1/180,000 = 5.56e-6 per gen)")
for h in sorted(hum, key=lambda h: (h["NeH"], h["s"], h["kappa"])):
    ev = h["k"] * 3 * 60000
    ind = h["indep"] * 1322
    flag = "NOISE (<= 5 events)" if ev <= 5.5 else ""
    if ev <= 5.5 or h["k"] * 1322 > ind:
        print(f"  N_h {h['NeH']:g} s {h['s']} kappa {h['kappa']:g}: k {h['k']:.4g} (~{ev:.1f} events), F {h['k'] * 1322:.3g}, "
              f"indep ceiling F {ind:.3g} {flag}{' ABOVE indep ceiling' if h['k'] * 1322 > ind else ''}")

print("\n## PH11 thresholds at the central calibration (N_e,L 3.3e7, G 1,322), coupled s")
clon = {(h["NeH"], h["s"], h["kappa"]): h["k"] * 1322 for h in hum}
for s in SS:
    u = C[(3.3e7, s, 1322)]["U_b"]
    for NeH in (3300, 1e4):
        rec = ", ".join(f"k{k:g}: {F(u, 1322, k, NeH, s):.3g}" for k in (125, 652, 1e4))
        cs = ", ".join(f"k{k:g}: {clon.get((NeH, s, k), float('nan')):.3g}" for k in (125, 652, 1e4, 93659))
        print(f"  s {s} N_h {NeH:g}: map36.8 kappa* {kstar(u, 1322, NeH, s):.4g} [{rec}]; clonal [{cs}]")

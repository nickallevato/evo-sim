"""A2e: transferring the LTEE fixation rate to humans.  Sensitivity analysis over recombination, mutation supply,
LTEE N_e, the LTEE counting target, human N_e, s, a cost-of-selection cap and units (per generation vs per year).
Question: which input drives the 1.5-172x "free-recombination factor" of R4-F2-A, and where does the LTEE-as-
ceiling extrapolation flip (human rate per generation = LTEE rate)?
THROWAWAY research code.  Self-contained (python -I): class_rate() is copied verbatim in logic from
a_ltee_scaling.py (validated there against the individual-based wf_f2, |z| < 0.7, and for M/c, c s, c U scaling);
kimura_u / indep_rate as in wf.py / wf_f2.py; W&B Eq. (1) and Eq. (8) as in gap04_weissman_barton.py.
Run:    research/.venv/bin/python -I research/checks/a2e_ltee_transfer.py smoke|main|analyse
        (single process; `main` = calib + human + analyse; resumable from the jsonl files)
Seeds:  numpy SeedSequence([SEED, stage_code, combo_index, iteration, rep]) -- never hash().
Output: research/checks/results/raw/a2e_<stage>.jsonl and a2e_main.out.

Written 2026-10-09 BEFORE any run of this file (smoke included).  Predictions below are fixed; later changes are
committed separately and labelled "post hoc".

=====================================================================================================
CLAIM UNDER TEST (docs/research/claims/A2e-ltee-as-ceiling.md; verbatim)
  A2e (Day, MITTENS 3.0, Z23003785 p.2): "Whatever number the LTEE produces, it is the empirical ceiling on what
      evolution can accomplish when every tool in its kit is deployed simultaneously under ideal conditions."
  A2e (Z23003785 p.4): "The LTEE rate is therefore not an estimate for complex organisms. It is an unattainable
      ceiling, the absolute best-case scenario, the performance of a Formula One car used to benchmark a horse-drawn
      cart."
  A2i (Matev, critic, 2026-09-18): "The reasoning is that 1/X1 is high (due to 1/B1 being high), so it very
      generous for the estimation of X2 to use the A1 value as an estimate for A2 even though A1 isn't why 1/X1 is
      high."   (units: per year vs per generation)
  Formal: rate_human <= rate_LTEE = 1/G_f per generation.  Transfer factor F = k_human / (1/G_f); A2e holds iff
  F <= 1.  Per year: F_yr = F / (gens_per_year_LTEE * years_per_gen_human).

INPUTS (source or status)
  G_f target: 1,322 (MITTENS 3.0) and 1,587 (2nd ed.; A2b, A2j); 2,890 = 1/(1/1322 - 4.1e-4) = the adaptive-only
      reading, subtracting the LTEE neutral expectation (Day's own LTEE supply 4.1e-4 per genome per generation,
      Z23003785 s4.3; derived; R4-F2-A notes the conflation).
  LTEE N_e (haploid copies M): 3.3e6, 1e7, 3.3e7, 1e8.  3.3e7 = N0 log2(100), UNSOURCED (parameters.yaml
      ltee.Ne_effective); swept only.
  s (LTEE beneficial effect, single s): 0.003, 0.01, 0.03 (swept; the A-sim grid).
  U_b,LTEE: not an input.  Calibrated by simulation (clonal class process) so that the clonal rate = 1/G_f at each
      (N_e, s, G_f).  R_int,LTEE = (1/G_f) / indep_rate is the clonal interference factor; 1/R_int,LTEE is the
      "1.5-172x" of R4-F2-A.
  Supply scaling kappa = U_b,human / U_b,LTEE per haploid genome: 1 (no scaling; Day's "no scaling" use of G_f),
      125 (mutation rate only: Hossjer 1.25e-8 / 1e-10), 652 (genome length only: 3e9 / 4.6e6), 81,500 (both,
      Hossjer), 93,659 (Day's own supply figures 38.4 / 4.1e-4, Z23003785 s6.4, s4.3).  Implicit assumption: the
      same beneficial fraction per new mutation in both systems; a different fraction is another factor on kappa,
      so kappa is also swept continuously (10^0..10^5) to locate the flip kappa*.
  Human N_e: 3,300 (Day, Z19984826 s4.3; H8 notes it is not in its cited source) and 1e4 (contested-standard).
  Recombination (human): clonal (no recombination advantage: the human genome treated like the LTEE; simulated with
      the class process at M = 2 N_e,human); map 1.5 M (one chromosome-like linkage group, pessimistic; W&B Eq. 8);
      map 36.8 M (human map, R4-GAPS-04-07-02; W&B Eq. 8, asymptote R/2 = 18.4 per generation); free (W&B Eq. 1).
  Cost cap (branch H; mean-field, phi = 1): k <= ln(R_h) / D_h with D_h = 2 ln(2 N_e,human) + 2 and R_h in
      {1.111 (Haldane's 10%), 2, 3}; also Day's own figures 1/300 (H), 1/667 (Haldane + d), 1/39 (Term 3, H8).
  Units: LTEE 6.64 generations per day (log2 100; standard) = 2,425 per year; human 20 / 25 / 29 years per
      generation.  Neutral-inclusive comparison: human total k = 38.4 per haploid genome per generation (Day's own
      supply, all-neutral upper reading) vs 1/1,322.

STAGES
  smoke: one class_rate call at N_e = 3.3e7, s = 0.01 (timing); one human clonal call; W&B functions on 3 inputs.
  calib: 4 N_e x 3 s x {1322, 2890} + (3.3e7, 0.01, 1587) = 25 combos; log-bisection of U_b on [1e-12, 1e-5],
         9 iterations x 2 reps (T = 150,000, burn 60,000; as A-sim), then 4 evaluation reps at the calibrated U_b
         (T = 300,000) giving k_LTEE and its SE.
  human: clonal human rate by class process at M = 2 N_e,human for N_e,human {3300, 1e4} x s {0.003, 0.01, 0.03}
         x kappa {1, 10, 125, 652, 1e4, 93659} using the central calibration (3.3e7, G_f 1,322); 3 reps,
         T = 60,000, burn 15,000.
  analyse: closed-form transfer for every combination; tornado (one-at-a-time ranges of log10 F around the
         central point); flip kappa*; flip R_h*; per-year table.
  Central point: N_e,LTEE 3.3e7, s 0.01, G_f 1,322, kappa 93,659, N_e,human 1e4, map 36.8 M, no cost cap, per gen.

PRE-REGISTERED PREDICTIONS
  Day's side (A2e as stated): F <= 1 for every plausible input combination (per generation): the LTEE rate is a
      ceiling "when every tool in its kit is deployed".
  Critics' side (A5a Hossjer scaling, A5f recombination, A2i units): F > 1 whenever humans recombine and supply is
      scaled (kappa >= 125); the per-year speed of bacteria is irrelevant to per-generation counts (A2i).
  This audit's numeric predictions:
    P1  1/R_int,LTEE (the "1.5-172x") is driven by s: it spans >= 20x across s = 0.003-0.03 at fixed N_e and G_f;
        LTEE N_e (3.3e6-1e8) moves it <= 3x; the G_f target (1,322 / 1,587 / 2,890) <= 2x.
    P2  For humans the dominant driver of F is supply scaling kappa (F ~ proportional to kappa below the W&B
        asymptote; 4-5 orders over kappa 1-93,659), then the human recombination mode (clonal vs map 36.8 M: >= 10x
        at kappa = 93,659), then s (via U_b,LTEE: 10-100x), then N_e,human (~3x), N_e,LTEE and G_f (each <= 3x).
    P3  Flip kappa* (F = 1, map 36.8 M, N_e,human 1e4, G_f 1,322, N_e,LTEE 3.3e7): ~10 (s = 0.003), ~200
        (s = 0.01), ~1,000 (s = 0.03); all in [5, 3000].  So the flip lies between kappa = 1 (no scaling: Day holds)
        and kappa = 93,659 (Day's own supply figures: critics hold); the mutation-rate-only scaling (125) sits
        near the flip at s = 0.01.  N_e,human = 3,300 raises kappa* ~3x.
    P4  At kappa = 93,659 and map 36.8 M: F in [50, 5000] for every s, N_e,LTEE and G_f (A2e not supported per
        generation under its own supply figures); with clonal humans F in [1, 100] (sublinear supply response).
        At kappa = 1: F < 1 in every recombination mode (A2e holds if supply is not scaled).
    P5  Units: under the recombining model every F_yr < 1 for kappa <= 93,659 (W&B asymptote R/2 = 18.4 per
        generation gives F <= 24,300 < 2,425 x 20 = 48,500): per year the LTEE is a ceiling (Day-side point; A2i
        concedes per-year speed).  Neutral-inclusive total: F = 38.4 x 1,322 = 50,765 per generation, F_yr
        0.72-1.05 (borderline at 20 y).
    P6  Cost cap: Day's own Haldane 1/300 allows F = 4.4, Haldane + d 1/667 F = 2.0, Term 3 1/39 F = 34 (G_f 1,322):
        Day's own cost limits are above the LTEE rate per generation (internal tension: if both are ceilings the
        LTEE binds and H is redundant for A).  The mean-field cap ln R_h / D_h falls below 1/1,322 only for
        R_h < ~1.017 (N_e,human 1e4).
  What would change a verdict: F <= 1 at kappa = 93,659 under recombination (supports A2e on Day's own supply
  numbers); kappa* >= 93,659 for any s (supports A2e); P1 failing (N_e or G_f dominating) would re-attribute the
  1.5-172x range.  A2e's internal non-sequitur verdict is not at stake (it rests on the paper's text).
=====================================================================================================
"""
import json
import math
import os
import sys
import time

import numpy as np
from scipy.optimize import brentq
from scipy.special import lambertw

SEED = 20261010
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "results", "raw")
NE_L = (3.3e6, 1e7, 3.3e7, 1e8)
SS = (0.003, 0.01, 0.03)
GTS = (1322, 2890)
KAPPA_NAMED = ((1, "none"), (125, "mu only (Hossjer)"), (652, "L only"), (81500, "both (Hossjer)"),
               (93659, "Day 38.4/4.1e-4"))
NE_H = (3300, 1e4)
MAPS = (("map1.5", 1.5), ("map36.8", 36.8))
LTEE_GPY = 6.64 * 365.25
YPG = (20, 25, 29)
CENTRAL = dict(NeL=3.3e7, s=0.01, G=1322, kappa=93659, NeH=1e4, rec="map36.8")


# ------------------------------------------------------------------------------------------- engines
def class_rate(M, U, s, T, burn, rng, nblocks=5):
    """Clonal fixed-s multinomial class process (a_ltee_scaling.class_rate). Returns (rate, se, mean_classes)."""
    n = np.zeros(8, dtype=np.int64); n[0] = M
    off = 0.0
    marks = []
    ncls, nrec = 0.0, 0
    checkpoints = {burn + int(T * i / nblocks) for i in range(nblocks + 1)}
    for g in range(burn + T + 1):
        if n[-1] > 0:
            n = np.append(n, 0)
        idx = np.arange(len(n))
        mean = (n * idx).sum() / M
        if g in checkpoints and g >= burn:
            marks.append(off + mean)
        if g == burn + T:
            break
        wgt = n * np.exp(s * (idx - mean))
        stay = wgt * (1 - U)
        flow = np.zeros_like(stay); flow[1:] = wgt[:-1] * U
        p = stay + flow
        p = p / p.sum()
        n = rng.multinomial(M, p)
        nz = np.flatnonzero(n)
        lo = nz[0]
        if lo > 0:
            n = n[lo:]; off += lo
        if g >= burn and g % 100 == 0:
            ncls += (n > 0).sum(); nrec += 1
    d = np.diff(np.array(marks)) / (T / nblocks)
    return float(d.mean()), float(d.std(ddof=1) / np.sqrt(len(d))), ncls / max(nrec, 1)


def kimura_u(N, s):
    p = 1.0 / (2 * N)
    return (1 - math.exp(-4 * N * s * p)) / (1 - math.exp(-4 * N * s))


def indep_rate(M, U, s):
    """Independent-sites 2N U_b u(s) = M U u (wf_f2.indep_rate)."""
    return M * U * kimura_u(M // 2, s)


def eq1_free(L0, s):
    return float(np.real(lambertw(4 * s * L0))) / 4 / s


def eq8(L0, R, s):
    f = lambda L: L - L0 * (1 - 2 * L / R) * math.exp(-4 * L * s)
    hi = min(L0, R / 2) * (1 - 1e-12)
    return brentq(f, 0.0, hi) if f(hi) > 0 else hi


# ------------------------------------------------------------------------------------------- stages
def combos():
    c = [(NeL, s, G) for NeL in NE_L for s in SS for G in GTS]
    c.append((3.3e7, 0.01, 1587))
    return c


def calibrate(ci, NeL, s, G):
    lo, hi = math.log(1e-12), math.log(1e-5)
    trace = []
    for it in range(9):
        mid = 0.5 * (lo + hi)
        ks = [class_rate(int(NeL), math.exp(mid), s, 150000, 60000,
                         np.random.default_rng(np.random.SeedSequence([SEED, 1, ci, it, r])))[0] for r in range(2)]
        trace.append((math.exp(mid), float(np.mean(ks))))
        if np.mean(ks) < 1.0 / G:
            lo = mid
        else:
            hi = mid
    U = math.exp(0.5 * (lo + hi))
    ev = [class_rate(int(NeL), U, s, 300000, 60000, np.random.default_rng(np.random.SeedSequence([SEED, 2, ci, 0, r])))
          for r in range(4)]
    k = float(np.mean([e[0] for e in ev]))
    se = float(np.std([e[0] for e in ev], ddof=1) / 2)
    ind = indep_rate(int(NeL), U, s)
    return dict(ci=ci, NeL=NeL, s=s, G=G, U_b=U, k_eval=k, k_se=se, G_eval=1 / k, indep=ind,
                R_int=k / ind, inv_R_int=ind / k, ncls=float(np.mean([e[2] for e in ev])), trace=trace)


def stage_calib(path):
    done = set()
    if os.path.exists(path):
        done = {json.loads(l)["ci"] for l in open(path)}
    t0 = time.time()
    for ci, (NeL, s, G) in enumerate(combos()):
        if ci in done:
            continue
        r = calibrate(ci, NeL, s, G)
        r["sec"] = time.time() - t0
        with open(path, "a") as fh:
            fh.write(json.dumps(r) + "\n")
        print(f"[calib {time.time() - t0:6.0f}s] NeL={NeL:.2g} s={s} G={G}: U_b={r['U_b']:.3g} "
              f"G_eval={r['G_eval']:.0f} (SE {r['k_se'] / r['k_eval']:.2f} rel) 1/R_int={r['inv_R_int']:.2f}", flush=True)


def stage_human(path, calib_path):
    cal = {(r["NeL"], r["s"], r["G"]): r for r in map(json.loads, open(calib_path))}
    done = set()
    if os.path.exists(path):
        done = {(d["NeH"], d["s"], d["kappa"]) for d in map(json.loads, open(path))}
    t0 = time.time()
    hi = 0
    for NeH in NE_H:
        for s in SS:
            Ub = cal[(3.3e7, s, 1322)]["U_b"]
            for kappa in (1, 10, 125, 652, 1e4, 93659):
                hi += 1
                if (NeH, s, kappa) in done:
                    continue
                M = int(2 * NeH)
                rs = [class_rate(M, Ub * kappa, s, 60000, 15000,
                                 np.random.default_rng(np.random.SeedSequence([SEED, 3, hi, 0, r]))) for r in range(3)]
                k = float(np.mean([x[0] for x in rs]))
                row = dict(NeH=NeH, s=s, kappa=kappa, U_b=Ub * kappa, k=k,
                           k_se=float(np.std([x[0] for x in rs], ddof=1) / math.sqrt(3)),
                           indep=indep_rate(M, Ub * kappa, s), sec=time.time() - t0)
                with open(path, "a") as fh:
                    fh.write(json.dumps(row) + "\n")
                print(f"[human {time.time() - t0:6.0f}s] NeH={NeH:g} s={s} kappa={kappa:g}: k={k:.4g} "
                      f"F={k * 1322:.3g} indep={row['indep']:.4g}", flush=True)


def human_rate(rec, NeH, s, Ub_h, clonal=None):
    L0 = indep_rate(int(2 * NeH), Ub_h, s)
    if rec == "free":
        return eq1_free(L0, s)
    if rec == "indep":
        return L0
    if rec.startswith("map"):
        return eq8(L0, dict(MAPS)[rec], s)
    if rec == "clonal":
        return clonal
    raise ValueError(rec)


def analyse():
    cal = [json.loads(l) for l in open(os.path.join(RAW, "a2e_calib.jsonl"))]
    hum = [json.loads(l) for l in open(os.path.join(RAW, "a2e_human.jsonl"))] \
        if os.path.exists(os.path.join(RAW, "a2e_human.jsonl")) else []
    C = {(r["NeL"], r["s"], r["G"]): r for r in cal}
    print("## 1. LTEE calibration and the clonal interference factor 1/R_int (the '1.5-172x')")
    print("| N_e LTEE | s | G_f target | U_b (per genome) | G_f eval | indep rate | 1/R_int |")
    print("|---|---|---|---|---|---|---|")
    for r in sorted(cal, key=lambda r: (r["G"], r["s"], r["NeL"])):
        print(f"| {r['NeL']:.2g} | {r['s']} | {r['G']} | {r['U_b']:.3g} | {r['G_eval']:.0f} | {r['indep']:.3g} | {r['inv_R_int']:.2f} |")
    inv = lambda NeL, s, G: C[(NeL, s, G)]["inv_R_int"] if (NeL, s, G) in C else float("nan")
    span = lambda xs: max(xs) / min(xs) if xs and min(xs) > 0 else float("nan")
    print("P1 drivers of 1/R_int (fold range): "
          f"s at central N_e/G: {span([inv(3.3e7, s, 1322) for s in SS]):.1f}x (>= 20 predicted); "
          f"N_e at s=0.01, G 1322: {span([inv(n, 0.01, 1322) for n in NE_L]):.2f}x (<= 3); "
          f"G at central: {span([inv(3.3e7, 0.01, g) for g in (1322, 1587, 2890)]):.2f}x (<= 2); "
          f"max over N_e for each s: " + ", ".join(f"s={s}: {span([inv(n, s, 1322) for n in NE_L]):.2f}x" for s in SS))

    clon = {(h["NeH"], h["s"], h["kappa"]): h["k"] for h in hum}

    def F(NeL=3.3e7, s=0.01, G=1322, kappa=93659, NeH=1e4, rec="map36.8", cap=None):
        c = C.get((NeL, s, G))
        if c is None:
            return float("nan")
        if rec == "clonal":
            if NeL != 3.3e7 or G != 1322:
                return float("nan")
            k = clon.get((NeH, s, kappa), float("nan"))
        else:
            k = human_rate(rec, NeH, s, c["U_b"] * kappa)
        if cap is not None:
            k = min(k, cap)
        return k * G

    print("\n## 2. Transfer factor F = k_human / (1/G_f), per generation (A2e holds iff F <= 1)")
    print("| s | N_e,human | recombination | " + " | ".join(f"kappa={k:g} ({n})" for k, n in KAPPA_NAMED) + " |")
    print("|---|---|---|" + "---|" * len(KAPPA_NAMED))
    for s in SS:
        for NeH in NE_H:
            for rec in ("clonal", "map1.5", "map36.8", "free"):
                vals = []
                for k, _ in KAPPA_NAMED:
                    v = F(s=s, NeH=NeH, rec=rec, kappa=k)
                    if v != v and rec == "clonal":
                        v = F(s=s, NeH=NeH, rec=rec, kappa={81500: 93659}.get(k, k))
                        vals.append(f"({v:.3g})" if v == v else "n/s")
                    else:
                        vals.append(f"{v:.3g}" if v == v else "n/s")
                print(f"| {s} | {NeH:g} | {rec} | " + " | ".join(vals) + " |")
    print("(n/s = not simulated; clonal values at kappa = 81,500 shown in parentheses are the 93,659 run)")

    print("\n## 3. Tornado: one-at-a-time ranges of log10 F around the central point " + str(CENTRAL))
    f0 = F()
    print(f"central F = {f0:.4g}")
    axes = [("kappa", [k for k, _ in KAPPA_NAMED]), ("s", list(SS)), ("NeL", list(NE_L)), ("G", [1322, 1587, 2890]),
            ("NeH", list(NE_H)), ("rec", ["clonal", "map1.5", "map36.8", "free"])]
    tor = []
    for name, vals in axes:
        fs = [(v, F(**{name: v})) for v in vals]
        fs = [(v, f) for v, f in fs if f == f and f > 0]
        lo, hi = min(fs, key=lambda x: x[1]), max(fs, key=lambda x: x[1])
        tor.append((math.log10(hi[1]) - math.log10(lo[1]), name, lo, hi))
    for w, name, lo, hi in sorted(tor, reverse=True):
        print(f"  {name:6s}: {w:5.2f} decades  (min F {lo[1]:.3g} at {lo[0]}, max F {hi[1]:.3g} at {hi[0]})")

    print("\n## 4. Flip kappa* (F = 1), recombining humans (W&B), every calibration")
    print("| N_e LTEE | s | G_f | N_e,human | kappa* map36.8 | kappa* map1.5 | kappa* free |")
    print("|---|---|---|---|---|---|---|")
    for (NeL, s, G), c in sorted(C.items(), key=lambda kv: (kv[0][2], kv[0][1], kv[0][0])):
        for NeH in NE_H:
            ks = []
            for rec in ("map36.8", "map1.5", "free"):
                g = lambda lk: F(NeL, s, G, 10 ** lk, NeH, rec) - 1.0
                ks.append(10 ** brentq(g, -3, 9) if g(-3) < 0 < g(9) else float("nan"))
            print(f"| {NeL:.2g} | {s} | {G} | {NeH:g} | {ks[0]:.3g} | {ks[1]:.3g} | {ks[2]:.3g} |")
    print("clonal humans (central calibration): F by kappa: " + "; ".join(
        f"NeH={NeH:g} s={s}: " + ", ".join(f"{k:g}:{clon.get((NeH, s, k), float('nan')) * 1322:.3g}"
                                           for k in (1, 10, 125, 652, 1e4, 93659)) for NeH in NE_H for s in SS))

    print("\n## 5. Units: F_yr = F / (2,425 x years per human generation)")
    for ypg in YPG:
        fy = [F(s=s, NeL=n, G=g, NeH=h, rec=r) / (LTEE_GPY * ypg) for s in SS for n in NE_L for g in GTS for h in NE_H
              for r in ("map1.5", "map36.8", "free")]
        fy = [x for x in fy if x == x]
        cap = 18.4 * 1322 / (LTEE_GPY * ypg)
        print(f"  {ypg} y/gen: recombining F_yr range {min(fy):.3g} - {max(fy):.3g} (kappa = 93,659); "
              f"W&B asymptote bound {cap:.3f}; neutral-inclusive total 38.4 x 1322 -> F_yr {38.4 * 1322 / (LTEE_GPY * ypg):.3f}")

    print("\n## 6. Cost caps (branch H) against the LTEE rate 1/1,322 (and 1/1,587, 1/2,890)")
    for lab, cap in (("Haldane 1/300 (H)", 1 / 300), ("Haldane + d 1/667", 0.45 / 300), ("Term 3 1/39 (H8)", 1 / 39)):
        print(f"  {lab}: F cap = " + ", ".join(f"G {g}: {cap * g:.2f}" for g in (1322, 1587, 2890)))
    for NeH in NE_H:
        D = 2 * math.log(2 * NeH) + 2
        for Rh in (1 / 0.9, 2.0, 3.0):
            cap = math.log(Rh) / D
            print(f"  mean-field ln R/D: N_e,human {NeH:g} (D {D:.1f}), R_h {Rh:.3f}: cap {cap:.4g}/gen, F cap "
                  f"{cap * 1322:.2f}; central F with cap {F(NeH=NeH, cap=cap):.3g}")
        print(f"  flip R_h* (cap = 1/G_f): G 1322: {math.exp(D / 1322):.4f}; G 2890: {math.exp(D / 2890):.4f}")


def smoke():
    t0 = time.time()
    r = class_rate(int(3.3e7), 8.4e-9, 0.01, 30000, 10000, np.random.default_rng(np.random.SeedSequence([SEED, 0, 0])))
    print(f"class_rate Ne=3.3e7 s=0.01 U=8.4e-9 T=30k+10k: rate {r[0]:.4g} (G {1 / r[0]:.0f}), {time.time() - t0:.1f} s",
          flush=True)
    t1 = time.time()
    r = class_rate(20000, 8.4e-9 * 93659, 0.01, 10000, 3000, np.random.default_rng(np.random.SeedSequence([SEED, 0, 1])))
    print(f"class_rate M=2e4 U=7.9e-4 s=0.01 T=10k+3k: rate {r[0]:.4g} classes {r[2]:.1f}, {time.time() - t1:.1f} s",
          flush=True)
    for L0 in (0.01, 1.0, 100.0):
        print(f"W&B L0={L0}: free {eq1_free(L0, 0.01):.4g}, map36.8 {eq8(L0, 36.8, 0.01):.4g}, map1.5 {eq8(L0, 1.5, 0.01):.4g}")


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "smoke"
    os.makedirs(RAW, exist_ok=True)
    if which == "smoke":
        smoke()
    elif which == "analyse":
        analyse()
    elif which == "main":
        stage_calib(os.path.join(RAW, "a2e_calib.jsonl"))
        stage_human(os.path.join(RAW, "a2e_human.jsonl"), os.path.join(RAW, "a2e_calib.jsonl"))
        analyse()
    else:
        raise SystemExit("unknown stage")

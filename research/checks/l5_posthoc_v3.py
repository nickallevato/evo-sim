"""L5 POST HOC (fix pass, 2026-10-13) -- V3 at tight linkage re-examined, and a direct trajectory bound at s = 0.01.

POST HOC, DESCRIPTIVE.  Not part of the registration of l5_adna_power.py (0e6da82).  It changes no registered
prediction, tolerance, band or verdict move; the registered V3 miss stays scored a miss as registered whatever this
prints.  This docstring was committed and pushed before the run (parts A, B, C below; the `timing` command was run
first with a throwaway seed and prints seconds only, no result).

Run (workstation; one process, well under 500 MB; see TIMING below):
    research/.venv/bin/python -I research/checks/l5_posthoc_v3.py timing
    research/.venv/bin/python -I research/checks/l5_posthoc_v3.py main research/checks/results/raw \
        > research/checks/results/raw/l5_posthoc_v3.out
Output: raw/l5_posthoc_v3.out (text), raw/l5_posthoc_v3.json (numbers, and the 1,500 + n_C final shares).
Imports l5_adna_power.py unchanged (sel, times, two_n_europe, DEMOGS, ROOT_SEED) and scipy.stats.binom.

------------------------------------------------------------------------------------------------------------------------
WHY (combined review REVIEW-R4-L5-combined.md, d7f70ec, items C3 and C2)
  C3.  The selftest's V3 at r = 1e-4 gave a mean final non-founder share of 0.0185 against the formula's 0.0084
       (n = 300 fixed sweeps), a miss of the registered tolerance max(0.01, 30%).  The pre-run note and R4-L5.md read
       this as "the formula understates the non-founder share, so expected counts are biased up, toward Day's band".
       The reviewer reran the same loop with n = 1,500 and another seed and reported that the mean does not miss, and
       that the formula errs in a different way: it gives every sample the MEAN share, while the share is heavy-tailed,
       so the probability that a linked SNP is monomorphic in the modern sample is understated.
  C2.  "E <= 1 at s <= 0.01" was printed as a simulated margin; the reviewer ruled that it rests on sweep-time
       arithmetic and asked for his direct trajectory bound to be registered and rerun.

WHAT WAS ALREADY SEEN BEFORE THIS SCRIPT WAS WRITTEN (so parts A and B are reproductions, not blind tests)
  Selftest (seed [ROOT_SEED, 5, 9, 1], n = 300): r = 1e-4: sim 0.01854, formula 0.00838, FAIL.
  Reviewer run RV (seed 424242, n = 1,500, loop copied unchanged, uncommitted): mean share 0.0077 (SE 0.0012) against
    0.0083; 89.4% of sweeps with share exactly 0; 2.3% above 0.1; maximum 1.0; probability that 1,315 chromosomes are
    monomorphic 0.90 explicit against 8.5e-5 by the formula; at 853 chromosomes 0.90 against 0.0018; share below 0.1
    (his B10 proxy) 0.977 against 1.000.
  Reviewer run RB (seed 987654321, 200,000 alleles from 50% at 7,500 BP, s = 0.01, uncommitted): highest present
    frequency 0.956 (const), 0.917 (Gravel), 0.958 (Gazave), 0.856 (Nelson), 0.980 (const, 20 y); none reaches 0.99;
    mean monomorphy probability at 853 chromosomes at most 2e-13; from 60% (const, 25 y): highest 0.981, mean 3e-13.
  All 90 task outputs of the main run and its analysis (R4-L5.md at 1ffdade).
  NOT seen: anything from part C (no run at 2N = 20,000 exists), anything from a 10% start in part B, the bootstrap
    in part A.

------------------------------------------------------------------------------------------------------------------------
PART A  (reproduces RV)   seed SeedSequence([ROOT_SEED, 5, 99, 1])
  The selftest's explicit two-locus haploid-gamete Wright-Fisher loop, copied unchanged: N = 1,000, s = 0.1,
  pB = 0.3, founder carries B, r = 1e-4 only.  Run until 1,500 sweeps have fixed; keep every final share of b and
  every per-sweep formula value -expm1(-r I)(1 - pB).
  Reported:
   A1  mean share (with SE) against the mean formula value; pass or fail on the registered tolerance
       |sim - formula| <= max(0.01, 0.30 x formula).
   A2  distribution of the share: fraction exactly 0, fraction above 0.1, maximum, quantiles.
   A3  how often an n = 300 mean misses the registered tolerance: 20,000 resamples of 300 sweeps (with replacement)
       from the 1,500, seed [ROOT_SEED, 5, 99, 2].  Descriptive.
   A4  hitchhiker monomorphy in the modern sample, founder allele (the l5 script computes f0^(chromosomes) with
       f0 = 1 - formula share): explicit = mean over sweeps of (1 - share_i)^n; formula = mean over sweeps of
       (1 - formula_i)^n; for n = 1,315 (v62: 680 diploids x 0.967), 853 (v66: 441) and 1,247 (blog: 645).
   A5  B10's modern half (sample frequency above 90%): explicit = mean of P(Binomial(1,247, 1 - share_i) > 1,122);
       formula = the same with formula_i.
  What each outcome would mean (fixed here):
   - A1 passes (mean within tolerance): the registered miss at n = 300 is not reproduced at n = 1,500.  It STAYS a
     miss as registered.  The direction read into it ("formula understates the share; counts biased up, toward Day's
     band") is withdrawn in R4-L5.md.
   - A1 fails with sim above formula: the registered miss reproduces, the reviewer's RV does not; the direction
     statement stays and the write-up reports that two reruns disagree.
   - A1 fails with sim below formula: reported as a new miss in the other direction.
   - A4 explicit / formula >= 10 at n = 1,315 and at n = 853: the reviewer's distribution finding reproduces.  The
     formula understates the monomorphy of tightly linked hitchhikers, so the hitchhiker part of Z50, Z10 (and M10,
     N100) is understated.  At s >= 0.05 that is a bias AGAINST Day (his required rate would show more events on the
     paper's statistics than the tables print).  Recorded on the Day side as a limit of the test.
   - A4 explicit / formula < 2 at both: not reproduced; review item C3 (iv) is then not adopted.  Between 2 and 10:
     reported as partial, no label change.
   - A5 explicit within 5% (relative) of formula: B10 unaffected, as the reviewer says.  Otherwise reported as an
     effect on B10, with its sign.
  In every case the band (CRITIC) is unaffected by construction: it rests on the cells at s <= 0.01, whose zeros come
  from the focal trajectory, and a perfectly linked SNP can do no better than the focal site.

PART C  (new; not in the review; nothing seen)   seed SeedSequence([ROOT_SEED, 5, 99, 3])
  The reviewer notes RV is at 2N = 2,000, where a sample of 1,315 is most of the population, so "the size of the
  effect at 2N >= 20,000 is not known".  Part C repeats part A at N = 10,000 (2N = 20,000, the smallest European
  population in the main run), same s, pB, r, with N_C = 1,000 fixed sweeps (see TIMING), and reports A1, A2, A4, A5.
  Prediction, written before any run: the understatement persists.  Reasoning: the mean share is carried by rare
  early recombination events that leave large families; most sweeps end with no b copy or a handful, and a handful
  among 20,000 leaves a sample of 1,315 monomorphic with probability near 1.  Expected: fraction of sweeps with share
  exactly 0 well below part A's (more recombination events at larger 2N); explicit monomorphy at n = 1,315 above 0.3;
  formula monomorphy below 1e-4; A1 passes.
  If instead explicit / formula < 2 at 2N = 20,000, the effect is a small-population artefact of the selftest's
  N = 1,000 and the Z50 / Z10 columns need no label; the write-up then says so.

PART B  (reproduces RB, with a 10% start added)   seed SeedSequence([ROOT_SEED, 5, 99, 4, cell index])
  Forward Wright-Fisher of N_B = 200,000 independent alleles with the main script's `sel`, `times`, `two_n_europe`
  and demographies, s = 0.01 (the largest s in the registered critic condition), started at a fixed frequency at
  7,500 BP (the older of the two Neolithic sample dates) and run to the present.  Cells: the six registered
  demography cells from 50% (bounds Z50, whose statistic needs a Neolithic frequency below 50%); const 25 y and
  const 20 y from 60% (margin for Neolithic sampling error); the six cells from 10% (bounds Z10 and B10, added here;
  50,000 alleles each, to keep the run under a minute).
  Reported per cell: highest present frequency; number above 0.90, 0.98, 0.99 and at exactly 1; mean x^853 and
  mean x^1,315 (monomorphy probability in the v66 and v62 modern samples); mean P(Binomial(1,247, x) > 1,122)
  (B10's modern half); and 15,556 x each mean (an upper bound on the expected count if EVERY one of Day's 15,556
  completions sat at that start frequency at 7,500 BP, which by monotonicity in the start frequency bounds all
  starts below it).
  What each outcome would mean:
   - From 50%: none of 200,000 above 0.98 at 25 y and 15,556 x mean x^853 below 1 in every cell: the reviewer's bound
     reproduces; "E <= 1 at s <= 0.01" is stated in R4-L5.md as sweep-time arithmetic corroborated by this bound
     (post hoc).  If any cell gives 15,556 x mean x^853 >= 1, the corroboration is NOT cited and the write-up says
     the bound failed in that cell.
   - The deterministic expectation (log-odds shift s/2 per generation: 1.5 over 300 generations, 1.9 over 375) puts
     a 50% start at 0.82 (25 y) and 0.87 (20 y), a 10% start at 0.33 and 0.42.  From 10% the expectation is that no
     trajectory exceeds 0.90 and the B10 mean is below 1e-6; if not, reported as found.
  This bound does not replace the simulation's result; it covers the class of trajectories the main run could not
  resolve (review C2: 24 to 184 events per cell at 95%).

TIMING / RESOURCES
  `timing` runs 20 fixed sweeps of the A loop and of the C loop and one B cell of 20,000 alleles with seed
  [ROOT_SEED, 5, 98] and prints seconds only (no share, frequency or probability).  It was run once before this
  commit (0.08 s, 0.11 s, 0.36 s; 101 MB peak) and the sizes were then fixed: N_C = 1,000, and 50,000 instead of
  200,000 alleles for the 10%-start cells, for an estimated total of about 45 s.  If `main` would exceed a minute on
  the workstation it is run on na-workhorse instead with one process (never committed there); the .out file names
  the host.
"""
import os
import sys
import json
import math
import time
import hashlib
import platform

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np
from scipy.stats import binom
import l5_adna_power as l5

SEED_TAG = 99
N_A = 1500
N_C = 1000
N_B = 200_000
N_B10 = 50_000
BOOT = 20_000
CHR = {"v62": 1315, "v66": 853, "blog": 1247}        # modern chromosomes: 2 x diploids x 0.967 (l5 design_params)
F_DAY = l5.F_DAY


def two_locus(N, s, pB, r, target, rng):
    """the selftest's V3 loop (l5_adna_power.selftest), copied unchanged; returns every share and formula value"""
    sims, preds = [], []
    tries = 0
    while len(sims) < target and tries < 1_000_000:
        tries += 1
        g = np.array([1.0, 0.0, pB - 1.0 / (2 * N), 1 - pB]) / 1.0     # AB, Ab, aB, ab
        g[0] = 1.0 / (2 * N)
        g = g / g.sum()
        I = 0.0
        while True:
            xa = g[0] + g[1]
            xs = l5.sel(xa, s)
            fac_A = xs / xa if xa > 0 else 0.0
            fac_a = (1 - xs) / (1 - xa) if xa < 1 else 0.0
            g2 = g * np.array([fac_A, fac_A, fac_a, fac_a])
            D = g2[0] * g2[3] - g2[1] * g2[2]
            g2 = g2 + np.array([-r * D, r * D, r * D, -r * D])
            g2 = np.clip(g2, 0, None)
            g = rng.multinomial(2 * N, g2 / g2.sum()) / (2 * N)
            xa = g[0] + g[1]
            I += 1 - xa
            if xa <= 0 or xa >= 1:
                break
        if xa >= 1:
            sims.append(g[1])                       # share of A chromosomes carrying b
            preds.append(-math.expm1(-r * I) * (1 - pB))
    return np.array(sims), np.array(preds), tries


def summarise(sims, preds, label):
    n = sims.size
    ms, mp = float(sims.mean()), float(preds.mean())
    se = float(sims.std(ddof=1) / math.sqrt(n))
    out = dict(n=n, mean_sim=ms, se_sim=se, mean_formula=mp, tol=max(0.01, 0.30 * mp),
               pass_registered_tolerance=bool(abs(ms - mp) <= max(0.01, 0.30 * mp)),
               frac_zero=float((sims == 0).mean()), frac_gt_0p1=float((sims > 0.1).mean()), max=float(sims.max()),
               quantiles={q: float(np.quantile(sims, q)) for q in (0.5, 0.9, 0.95, 0.99)},
               formula_min=float(preds.min()), formula_max=float(preds.max()))
    mono = {}
    for dn, c in CHR.items():
        ex = float(np.mean((1 - sims) ** c))
        fo = float(np.mean((1 - preds) ** c))
        mono[dn] = dict(chromosomes=c, explicit=ex, formula=fo, ratio=(ex / fo if fo > 0 else None),
                        formula_at_mean_share=float((1 - mp) ** c))
    out["monomorphy_founder_allele"] = mono
    c = CHR["blog"]
    k = math.floor(0.9 * c)
    ex, fo = float(binom.sf(k, c, 1 - sims).mean()), float(binom.sf(k, c, 1 - preds).mean())
    out["B10_modern_gt90"] = dict(chromosomes=c, explicit=ex, formula=fo, rel_diff=(ex / fo - 1 if fo > 0 else None))
    print("\n== %s" % label)
    print("A1 mean share %.5f (SE %.5f) vs formula %.5f; tolerance %.4f -> %s" % (
        ms, se, mp, out["tol"], "PASS" if out["pass_registered_tolerance"] else "FAIL"))
    print("A2 share == 0: %.4f; share > 0.1: %.4f; max %.4f; quantiles %s; formula range %.5f-%.5f" % (
        out["frac_zero"], out["frac_gt_0p1"], out["max"],
        {q: round(v, 5) for q, v in out["quantiles"].items()}, out["formula_min"], out["formula_max"]))
    for dn, m in mono.items():
        print("A4 monomorphy, %s (%d chr): explicit %.4g  formula %.4g  ratio %s  [(1 - mean formula)^n = %.3g]" % (
            dn, m["chromosomes"], m["explicit"], m["formula"],
            "%.3g" % m["ratio"] if m["ratio"] else "inf", m["formula_at_mean_share"]))
    b = out["B10_modern_gt90"]
    print("A5 B10 modern half (blog, %d chr, > 90%%): explicit %.4f  formula %.4f  relative difference %+.4f" % (
        b["chromosomes"], b["explicit"], b["formula"], b["rel_diff"]))
    return out


def trajectories(fn, gy, x_start, s, n, rng):
    tm = l5.times(gy)
    twoN = l5.two_n_europe(fn, gy, tm["t7"])
    x = np.full(n, float(x_start))
    for t in range(tm["t7"], 0, -1):
        N2 = twoN[t - 1]
        x = rng.binomial(N2, l5.sel(x, s)) / N2
    return x, tm["t7"]


def b_cell(name, fn, gy, x_start, s, n, rng):
    x, gens = trajectories(fn, gy, x_start, s, n, rng)
    c = CHR["blog"]
    res = dict(cell=name, gy=gy, start=x_start, s=s, n=n, generations=gens, max=float(x.max()), mean=float(x.mean()),
               n_gt_0p90=int((x > 0.90).sum()), n_gt_0p98=int((x > 0.98).sum()), n_gt_0p99=int((x > 0.99).sum()),
               n_eq_1=int((x >= 1.0).sum()),
               mean_mono_853=float(np.mean(x ** CHR["v66"])), mean_mono_1315=float(np.mean(x ** CHR["v62"])),
               mean_B10_modern=float(binom.sf(math.floor(0.9 * c), c, x).mean()))
    for k in ("mean_mono_853", "mean_mono_1315", "mean_B10_modern"):
        res["F_x_" + k] = F_DAY * res[k]
    return res


def timing():
    rng = np.random.default_rng(np.random.SeedSequence([l5.ROOT_SEED, l5.TAG, 98]))
    t0 = time.time()
    two_locus(1000, 0.1, 0.3, 1e-4, 20, rng)
    ta = time.time() - t0
    t0 = time.time()
    two_locus(10_000, 0.1, 0.3, 1e-4, 20, rng)
    tc = time.time() - t0
    t0 = time.time()
    trajectories(l5.DEMOGS[0][1], 25, 0.5, 0.01, 20_000, rng)
    tb = time.time() - t0
    print("timing only: A 20 sweeps %.2fs (x%d = %.0fs); C 20 sweeps %.2fs (x%d = %.0fs); "
          "B one cell of 20,000 %.2fs (x10 x 8 + x2.5 x 6 cells = %.0fs)" % (
              ta, N_A // 20, ta * N_A / 20, tc, N_C // 20, tc * N_C / 20, tb, tb * (10 * 8 + 2.5 * 6)))


def main(outdir):
    t_all = time.time()
    md5 = lambda p: hashlib.md5(open(p, "rb").read()).hexdigest()
    print("l5_posthoc_v3 main; host %s; python %s; numpy %s" % (platform.node(), platform.python_version(), np.__version__))
    print("md5 l5_posthoc_v3.py %s; l5_adna_power.py %s" % (md5(os.path.abspath(__file__)),
                                                            md5(os.path.join(HERE, "l5_adna_power.py"))))
    res = {"params": dict(N_A=N_A, N_C=N_C, N_B=N_B, N_B10=N_B10, BOOT=BOOT, CHR=CHR, F_DAY=F_DAY)}
    # ---- part A
    rng = np.random.default_rng(np.random.SeedSequence([l5.ROOT_SEED, l5.TAG, SEED_TAG, 1]))
    t0 = time.time()
    sims, preds, tries = two_locus(1000, 0.1, 0.3, 1e-4, N_A, rng)
    A = summarise(sims, preds, "PART A: two-locus, N = 1,000 (2N = 2,000), s = 0.1, pB = 0.3, r = 1e-4, %d fixed sweeps of %d tries"
                  % (sims.size, tries))
    rb = np.random.default_rng(np.random.SeedSequence([l5.ROOT_SEED, l5.TAG, SEED_TAG, 2]))
    ix = rb.integers(0, sims.size, (BOOT, 300))
    bm, bp = sims[ix].mean(1), preds[ix].mean(1)
    miss = np.abs(bm - bp) > np.maximum(0.01, 0.30 * bp)
    A["boot300"] = dict(n_resamples=BOOT, frac_miss=float(miss.mean()), frac_miss_high=float((miss & (bm > bp)).mean()),
                        frac_miss_low=float((miss & (bm < bp)).mean()), frac_mean_ge_0p0185=float((bm >= 0.01854).mean()),
                        mean_q025=float(np.quantile(bm, 0.025)), mean_q975=float(np.quantile(bm, 0.975)))
    print("A3 resamples of n = 300: registered tolerance missed in %.3f (high %.3f, low %.3f); mean >= 0.01854 in %.4f; "
          "95%% range of the n = 300 mean %.4f to %.4f" % (
              A["boot300"]["frac_miss"], A["boot300"]["frac_miss_high"], A["boot300"]["frac_miss_low"],
              A["boot300"]["frac_mean_ge_0p0185"], A["boot300"]["mean_q025"], A["boot300"]["mean_q975"]))
    A["secs"] = time.time() - t0
    A["shares"], A["formula"] = [float(v) for v in sims], [float(v) for v in preds]
    res["A"] = A
    # ---- part C
    rng = np.random.default_rng(np.random.SeedSequence([l5.ROOT_SEED, l5.TAG, SEED_TAG, 3]))
    t0 = time.time()
    sims, preds, tries = two_locus(10_000, 0.1, 0.3, 1e-4, N_C, rng)
    C = summarise(sims, preds, "PART C (new): two-locus, N = 10,000 (2N = 20,000), s = 0.1, pB = 0.3, r = 1e-4, %d fixed sweeps of %d tries"
                  % (sims.size, tries))
    C["secs"] = time.time() - t0
    C["shares"], C["formula"] = [float(v) for v in sims], [float(v) for v in preds]
    res["C"] = C
    # ---- part B
    print("\n== PART B: %d alleles (%d from the 10%% start) from a fixed frequency at 7,500 BP to the present, s = 0.01 (F = %.0f)" % (N_B, N_B10, F_DAY))
    cells = [(d[0], d[1], d[2], 0.5) for d in l5.DEMOGS]
    cells += [(d[0], d[1], d[2], 0.6) for d in l5.DEMOGS if d[0].startswith("const")]
    cells += [(d[0], d[1], d[2], 0.1) for d in l5.DEMOGS]
    t0 = time.time()
    B = []
    for k, (name, fn, gy, x0) in enumerate(cells):
        rng = np.random.default_rng(np.random.SeedSequence([l5.ROOT_SEED, l5.TAG, SEED_TAG, 4, k]))
        r = b_cell(name, fn, gy, x0, 0.01, N_B10 if x0 == 0.1 else N_B, rng)
        B.append(r)
        print("B %-14s start %.2f  %3d gens  max %.4f  mean %.4f  >0.90: %6d  >0.98: %d  >0.99: %d  =1: %d  "
              "mono853 %.3g (xF %.3g)  mono1315 %.3g (xF %.3g)  B10mod %.3g (xF %.3g)" % (
                  name, x0, r["generations"], r["max"], r["mean"], r["n_gt_0p90"], r["n_gt_0p98"], r["n_gt_0p99"],
                  r["n_eq_1"], r["mean_mono_853"], r["F_x_mean_mono_853"], r["mean_mono_1315"],
                  r["F_x_mean_mono_1315"], r["mean_B10_modern"], r["F_x_mean_B10_modern"]), flush=True)
    res["B"] = B
    res["B_secs"] = time.time() - t0
    res["total_secs"] = time.time() - t_all
    print("\nsecs: A %.1f, C %.1f, B %.1f, total %.1f" % (A["secs"], C["secs"], res["B_secs"], res["total_secs"]))
    with open(os.path.join(outdir, "l5_posthoc_v3.json"), "w") as f:
        json.dump(res, f, indent=1)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "timing":
        timing()
    elif cmd == "main":
        main(sys.argv[2])
    else:
        sys.exit("usage: l5_posthoc_v3.py timing | main <outdir>")

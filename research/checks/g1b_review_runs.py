"""G1b -- POST-HOC runs requested by the three R4-G1 reviews (correctness, Day-side steelman, critic-side steelman).
THROWAWAY research check.  NOTHING HERE IS PRE-REGISTERED: every part was specified after the g1_specific_vs_any.py
results and the reviews were read, and several reviewer scratch numbers were known beforehand (noted per part).

Run:  research/.venv/bin/python -I research/checks/g1b_review_runs.py [all|dilution|excess|pfix|linked|ddiag|horn]
Outputs: research/checks/results/raw/g1b_out.txt, g1b_raw.json.  Seeds: SeedSequence([20261041, part, cfg, rep]),
except 'linked' and 'ddiag', which reuse g1's job functions/seeds (SEED 20261040) so the D rows are bit-identical.

PARTS (and the review item each answers)
 dilution  Steelman disagreement 1.  Does the additive-fitness dilution depend on CONCURRENCY or on TOTAL beneficial
           alleles carried?  Haploid WF, N = 1000, s = 0.01, free recombination, focal loci start at p0 = 0.1.
           Fitness conventions: mult  w = (1+s)^c;  add_incl w = 1 + s(c + F) (F = fixed beneficial alleles, the
           convention used in g1 part D);  add_excl w = 1 + s c (segregating only);  add_norm w = 1 + s(c - cbar)
           (each allele worth s relative to the current mean).  Designs: CONCURRENT (L loci at once, F0 = 0);
           SEQUENTIAL CHAIN of the same total n (one locus at a time, background F drawn uniformly from 0..n-1 already
           fixed); MIXED (230 concurrent on a background of F0 = 770 already fixed, total 1000).
           Expectation (written before running, but after the reviews): add_incl dilutes the chain about as much as the
           concurrent case for the same total (critic-side claim); add_excl dilutes only the concurrent case (a
           genuinely concurrency-specific barrier); add_norm and mult show no dilution.
 excess    Steelman disagreement 2.  Best/mean relative fitness and N_eff = (sum w)^2/sum w^2 across n in {230, 1e3,
           1e4, 1.57e5} and s in {0.001, 0.01}; N = 1e4, all n loci at p = 0.5, multiplicative; 200 replicates
           (count-level identity as in g1 part E2).  Plus the steady-state pipeline variance (derived, see below).
           Critic reviewer's scratch values were known: ~1.33 (n = 230), ~352 (1.57e5), ~2.1 (1.57e5, s = 0.001).
 pfix      Correctness review #4.  Per-locus FIXATION probability (not just expected response) when var(ln w) is
           O(1) as in Day's s3 configuration (var(ln w) = n ln(1.01)^2/4 = 3.9): scaled run N = 300, s = 0.1,
           p0 = 0.5, multiplicative, free recombination, L in {1, 157, 1570} (var 0, 0.36, 3.57).
           Reviewer scratch known: 0.853 at L = 1570.
 linked    Correctness review #6.  g1 part C at tighter maps: 0.05 M and 0.005 M over 50 loci, 4000 reps each.
           Reviewer scratch known: pair ratios 0.889 and 0.629.
 ddiag     Correctness review #5.  Re-run g1 part D multiplicative L = 230 and L = 1000 with the SAME seeds (bit-
           identical) to report replicate-level SE, dispersion of K and pair ratio; plus L = 100 (80 reps, new seeds).
 horn      Correctness #7-#9, Day-side #10.  Genome-supply bound on m* x n_f; d-corrected T (146,250 effective
           generations, Z18165980); both supply bases (4.5e11 McCarthy; 2.3e11 Gd claim file); 14.7 log reading.
"""
import os, sys, json, time, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import mpmath as mp
from multiprocessing import Pool
import g1_specific_vs_any as g1

SEED = 20261041
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results", "raw")
OUT = {}


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    OUT.setdefault("_log", []).append(s)


# --------------------------------------------------------------------------------------------- WF with conventions
def wf2(G, s, fit, rng, F0=0, max_gen=200000):
    """Haploid soft-selection WF, free recombination; returns (outcome, t_abs) per locus.  F0 = beneficial alleles
    already fixed in every genome at t = 0 (only add_incl uses it)."""
    N, L = G.shape
    idx = np.arange(L)
    outcome = np.full(L, -1, np.int8)
    tabs = np.zeros(L, np.int64)
    F = F0
    lnw1 = math.log1p(s)
    gen = 0
    while G.shape[1] > 0 and gen < max_gen:
        cs = G.sum(0)
        fx, ls = cs == N, cs == 0
        if fx.any() or ls.any():
            outcome[idx[fx]] = 1
            outcome[idx[ls]] = 0
            tabs[idx[fx | ls]] = gen
            F += int(fx.sum())
            keep = ~(fx | ls)
            G, idx = G[:, keep], idx[keep]
            if G.shape[1] == 0:
                break
        c = G.sum(1, dtype=np.int64)
        if fit == "mult":
            lw = c * lnw1
            w = np.exp(lw - lw.max())
        elif fit == "add_incl":
            w = 1.0 + s * (c + F)
        elif fit == "add_excl":
            w = 1.0 + s * c
        elif fit == "add_norm":
            w = np.maximum(1.0 + s * (c - c.mean()), 1e-12)
        else:
            raise ValueError(fit)
        cw = np.cumsum(w)
        cw /= cw[-1]
        a = np.minimum(np.searchsorted(cw, rng.random(N)), N - 1)
        if G.shape[1] == 1:
            G = G[a]
        else:
            b = np.minimum(np.searchsorted(cw, rng.random(N)), N - 1)
            m = rng.integers(0, 2, size=G.shape, dtype=np.uint8).astype(bool)
            G = np.where(m, G[a], G[b])
        gen += 1
    return outcome, tabs


def job_dil(args):
    cfg, rep, N, L, s, fit, p0, F0, chain_n = args
    rng = np.random.default_rng(np.random.SeedSequence([SEED, 1, cfg, rep]))
    if chain_n:  # one locus on a background of F fixed alleles, F ~ U{0..chain_n-1}
        F0 = int(rng.integers(0, chain_n))
    G = (rng.random((N, L)) < p0).astype(np.uint8)
    o, t = wf2(G, s, fit, rng, F0=F0)
    return cfg, o, t


def part_dilution(workers=10):
    say("== DILUTION (post-hoc): concurrent vs sequential chain vs mixed; N=1000, s=0.01, p0=0.1, free recombination")
    N, s, p0 = 1000, 0.01, 0.1
    designs = []  # (label, fit, L, F0, chain_n, reps)
    for fit in ("mult", "add_incl", "add_excl", "add_norm"):
        designs += [(f"{fit} single (L=1)", fit, 1, 0, 0, 2000),
                    (f"{fit} concurrent L=230", fit, 230, 0, 0, 12),
                    (f"{fit} concurrent L=1000", fit, 1000, 0, 0, 4),
                    (f"{fit} sequential chain n=230", fit, 1, 0, 230, 2000),
                    (f"{fit} sequential chain n=1000", fit, 1, 0, 1000, 2000)]
        if fit == "add_incl":
            designs += [(f"{fit} mixed: L=230 on F0=770 fixed", fit, 230, 770, 0, 12),
                        (f"{fit} single on F0=999 fixed", fit, 1, 999, 0, 2000)]
    jobs = []
    for cfg, (lab, fit, L, F0, cn, R) in enumerate(designs):
        jobs += [(cfg, r, N, L, s, fit, p0, F0, cn) for r in range(R)]
    t0 = time.time()
    with Pool(workers) as pool:
        res = pool.map(job_dil, jobs, chunksize=4)
    u = g1.kimura_hap(s, N, p0)
    rows = []
    for cfg, (lab, fit, L, F0, cn, R) in enumerate(designs):
        sel = [x for x in res if x[0] == cfg]
        O = np.concatenate([x[1] for x in sel])
        T = np.concatenate([x[2] for x in sel])
        per_rep = np.array([x[1].mean() for x in sel])
        pf = O.mean()
        se = (per_rep.std(ddof=1) / math.sqrt(len(per_rep))) if L > 1 else math.sqrt(pf * (1 - pf) / len(O))
        tf = T[O == 1]
        row = dict(label=lab, fit=fit, L=L, F0=F0, chain_n=cn, reps=R, p_fix=float(pf), se=float(se),
                   ratio=float(pf / u), t_fix=float(tf.mean()), t_fix_se=float(tf.std(ddof=1) / math.sqrt(len(tf))))
        rows.append(row)
        say(f"  {lab:42s} P_fix={pf:.4f}+-{se:.4f} (ratio to single-locus u {pf/u:.3f}); t_fix {tf.mean():.0f}"
            f"+-{row['t_fix_se']:.0f}")
    say(f"  ({time.time()-t0:.0f} s)")
    OUT["dilution"] = dict(N=N, s=s, p0=p0, kimura_u=u, rows=rows)


# --------------------------------------------------------------------------------------------- excess grid
def part_excess(reps=200):
    say("== EXCESS (post-hoc): best/mean relative fitness and N_eff; N=1e4, all n loci at p=0.5, multiplicative")
    N = 10000
    rows = []
    for s in (0.001, 0.01):
        b = math.log1p(s)
        for n in (230, 1000, 10000, 157000):
            rng = np.random.default_rng(np.random.SeedSequence([SEED, 2, int(s * 1e4), n]))
            bm, ne = [], []
            for _ in range(reps):
                c = rng.binomial(n, 0.5, N).astype(float)
                lw = c * b
                w = np.exp(lw - lw.max())
                bm.append(w.max() / w.mean())
                ne.append(1 / ((w / w.sum()) ** 2).sum())
            var = n * b * b / 4
            row = dict(s=s, n=n, var_lnw=var, best_over_mean=float(np.mean(bm)), best_sd=float(np.std(bm)),
                       neff=float(np.mean(ne)), neff_infinite=N * math.exp(-var))
            rows.append(row)
            say(f"  s={s:<6g} n={n:>7d} var(ln w)={var:.4f}  best/mean={row['best_over_mean']:.3g} "
                f"(sd {row['best_sd']:.2g})  N_eff={row['neff']:.0f} (infinite-pop {row['neff_infinite']:.0f})")
    # steady-state pipeline (derived): one logistic sweep contributes  int s^2 p q dt = s  to var(ln w) (haploid,
    # multiplicative), so a pipeline completing k sweeps per generation carries var(ln w) = k s.
    zE = 3.8516  # expected max of 1e4 standard normals (g1 part A)
    pipe = []
    for lab, k, s in [("Bernoulli s7.8 pipeline: 157,000 in 300,000 gens", 157000 / 3e5, 0.01),
                      ("230 concurrent at s=0.01 (s7.8 standing crop, p ~ 0.5)", None, 0.01),
                      ("Day's 1% scenario: 2e5 in 2.52e5 gens", 2e5 / 2.52e5, 0.01),
                      ("Ga framing: 2e7 in 3e5 gens", 2e7 / 3e5, 0.01),
                      ("GAP-01 alpha-scale (unreviewed): 0.04/gen", 0.04, 0.01)]:
        var = k * s if k is not None else 230 * math.log1p(s) ** 2 / 4
        sd = math.sqrt(var)
        bm = math.exp(sd * zE - var / 2)
        pipe.append(dict(label=lab, k_per_gen=k, s=s, var_lnw=var, best_over_mean_lognormal=bm,
                         neff_over_N=math.exp(-var)))
        say(f"  pipeline: {lab:55s} var(ln w)={var:.4g}  best/mean ~{bm:.3g}  N_eff/N ~{math.exp(-var):.3f}")
    OUT["excess"] = dict(N=N, reps=reps, rows=rows, pipeline=pipe)


# --------------------------------------------------------------------------------------------- P_fix at var O(1)
def job_pfix(args):
    cfg, rep, N, L, s, p0 = args
    rng = np.random.default_rng(np.random.SeedSequence([SEED, 3, cfg, rep]))
    G = (rng.random((N, L)) < p0).astype(np.uint8)
    o, t = wf2(G, s, "mult", rng)
    return cfg, o, t


def part_pfix(workers=10):
    say("== PFIX (post-hoc): per-locus P_fix when var(ln w) is O(1); N=300, s=0.1, p0=0.5, mult, free recomb.")
    N, s, p0 = 300, 0.1, 0.5
    cfgs = [(0, 1, 2000), (1, 157, 30), (2, 1570, 12)]
    jobs = [(c, r, N, L, s, p0) for (c, L, R) in cfgs for r in range(R)]
    t0 = time.time()
    with Pool(workers) as pool:
        res = pool.map(job_pfix, jobs, chunksize=2)
    u = g1.kimura_hap(s, N, p0)
    rows = []
    for (c, L, R) in cfgs:
        sel = [x for x in res if x[0] == c]
        O = np.concatenate([x[1] for x in sel])
        per = np.array([x[1].mean() for x in sel])
        se = per.std(ddof=1) / math.sqrt(len(per)) if L > 1 else math.sqrt(O.mean() * (1 - O.mean()) / len(O))
        var = L * math.log1p(s) ** 2 / 4
        rows.append(dict(L=L, reps=R, var_lnw=var, p_fix=float(O.mean()), se=float(se), kimura=u))
        say(f"  L={L:5d} var(ln w)={var:.3f}  P_fix={O.mean():.4f}+-{se:.4f}  (single-locus u {u:.4f})")
    say(f"  ({time.time()-t0:.0f} s)")
    OUT["pfix"] = dict(N=N, s=s, p0=p0, rows=rows)


# --------------------------------------------------------------------------------------------- linked maps (g1 C)
def part_linked(reps=4000, workers=10):
    say("== LINKED (post-hoc): g1 part C at tighter maps (N=1000, s=0.01, L=50 new mutations), 4000 reps")
    N, L, s = 1000, 50, 0.01
    cfgs = [(3, "linked", 0.05), (4, "linked", 0.005)]
    jobs = [(c, r, N, L, s, rec, rm) for (c, rec, rm) in cfgs for r in range(reps)]
    t0 = time.time()
    with Pool(workers) as pool:
        res = pool.map(g1.job_indep, jobs, chunksize=20)
    u = g1.kimura_hap(s, N, 1 / N)
    rows = []
    for (c, rec, rm) in cfgs:
        K = np.array([o.sum() for (cc, o, t) in res if cc == c], float)
        p = K.mean() / L
        disp = K.var(ddof=1) / (L * p * (1 - p))
        pair = (K * (K - 1)).mean() / (L * (L - 1) * p * p)
        bs = np.random.default_rng(np.random.SeedSequence([SEED, 4, c]))
        pr = []
        for _ in range(400):
            Kb = K[bs.integers(0, len(K), len(K))]
            pb = Kb.mean() / L
            pr.append((Kb * (Kb - 1)).mean() / (L * (L - 1) * pb * pb))
        rows.append(dict(map_M=rm, loci_per_M=L / rm, p_fix=p, ratio=p / u, dispersion=disp, pair_ratio=pair,
                         pair_se=float(np.std(pr))))
        say(f"  map {rm:<6g} M ({L/rm:.0f} loci/M): P_fix={p:.5f} (ratio {p/u:.3f}); dispersion {disp:.3f}; "
            f"P(pair)/p^2 = {pair:.3f}+-{np.std(pr):.3f}")
    say(f"  ({time.time()-t0:.0f} s)")
    OUT["linked"] = rows


# --------------------------------------------------------------------------------------------- D diagnostics
def part_ddiag(workers=10):
    say("== DDIAG (post-hoc): g1 part D multiplicative, replicate-level SE, dispersion, pair ratio")
    N, s, p0 = 1000, 0.01, 0.1
    # g1 part_sweeps cfg numbering: mult L=1 ->0, 14 ->1, 230 ->2, 1000 ->3 ; same seeds => bit-identical
    jobs = [(2, r, N, 230, s, "mult", p0) for r in range(12)] + [(3, r, N, 1000, s, "mult", p0) for r in range(4)] + \
           [(20, r, N, 100, s, "mult", p0) for r in range(80)]
    t0 = time.time()
    with Pool(workers) as pool:
        res = pool.map(g1.job_sweep, jobs, chunksize=1)
    u = g1.kimura_hap(s, N, p0)
    rows = []
    for cfg, L in ((2, 230), (3, 1000), (20, 100)):
        sel = [x for x in res if x[0] == cfg]
        O = np.array([x[3] for x in sel], float)  # reps x L
        K = O.sum(1)
        p = O.mean()
        per = O.mean(1)
        se_rep = per.std(ddof=1) / math.sqrt(len(per))
        disp = K.var(ddof=1) / (L * p * (1 - p)) if len(K) > 2 else float("nan")
        pair = (K * (K - 1)).mean() / (L * (L - 1) * p * p)
        rows.append(dict(L=L, reps=len(sel), p_fix=p, se_replicate=se_rep, ratio=p / u,
                         z_vs_u=(p - u) / se_rep, dispersion=disp, pair_ratio=pair))
        say(f"  L={L:5d} reps={len(sel):3d} P_fix={p:.4f} replicate-SE {se_rep:.4f} (ratio {p/u:.3f}, z {(p-u)/se_rep:+.1f})"
            f"; dispersion {disp:.3f}; P(pair)/p^2 {pair:.4f}")
    say(f"  ({time.time()-t0:.0f} s)")
    OUT["ddiag"] = rows


# --------------------------------------------------------------------------------------------- horn extras
def part_horn():
    say("== HORN extras (post-hoc)")
    r = {}
    # 14.7 readings
    r["add_1474x0.01"] = 1474 * 0.01
    r["log_1474xln1.01"] = 1474 * math.log1p(0.01)
    r["log_required_157000xln1.01"] = 157000 * math.log1p(0.01)
    r["ratio_log"] = r["log_required_157000xln1.01"] / r["log_1474xln1.01"]
    r["ratio_add"] = 1570 / 14.74
    say(f"  14.7 readings: additive 1474x0.01 = {r['add_1474x0.01']:.3f}; log 1474 x ln1.01 = {r['log_1474xln1.01']:.3f};"
        f" required log 157,000 x ln1.01 = {r['log_required_157000xln1.01']:.1f}; ratios {r['ratio_add']:.1f} (add), "
        f"{r['ratio_log']:.1f} (log)")
    r["book_required_rate_2.2"] = 50000 / 2.2
    say(f"  book step: 50,000/2.2 = {r['book_required_rate_2.2']:.0f} ('one in 23,000')")
    # supply bases
    sup = {"McCarthy 4.5e11 (9e6 y x 50,000/y)": 4.5e11, "Gd claim file 2.3e11 (77 x 1e4 x 3e5)": 77 * 1e4 * 3e5}
    r["fb_needed"] = {}
    for lab, M in sup.items():
        for n in (157000, 2e5, 2e7):
            for p in (0.02, 0.002):
                r["fb_needed"][f"{lab}|n={n:g}|p={p}"] = n / p / M
    for k, v in r["fb_needed"].items():
        say(f"  beneficial fraction needed {k}: {v:.3g}")
    # genome bound and d-corrected T
    sites = 3.1e9  # ASSUMPTION (not in parameters.yaml): haploid genome ~3.1e9 bp
    snv = 3 * sites
    r["possible_snv_changes"] = snv
    N, mu = 1.0e4, 1.2e-8
    rows = []
    for (lab, T, s) in [("T=3e5, s=0.01", 3e5, 0.01), ("T=2.52e5, s=0.01", 2.52e5, 0.01),
                        ("T=146,250 (d=0.45 effective gens, Z18165980), s=0.01", 146250, 0.01),
                        ("T=3e5, s=0.001", 3e5, 0.001), ("T=146,250, s=0.001", 146250, 0.001)]:
        lam1 = 2 * N * (mu / 3) * T * 2 * s
        q = 1 - math.exp(-lam1)
        for nf in (1e3, 1e4, 157000, 2e5, 2e7):
            l50 = float(-mp.log(1 - mp.power(mp.mpf(0.5), 1 / mp.mpf(nf))))
            m50 = math.ceil(l50 / lam1)
            rows.append(dict(case=lab, q=q, lam1=lam1, n_f=nf, m50=m50, m_times_nf=m50 * nf,
                             frac_of_snv=m50 * nf / snv, mq_at_flip=m50 * q))
            say(f"  {lab:52s} q={q:.4f} lam1={lam1:.4f} n_f={nf:>9.3g}: m*={m50:5d}  m*x n_f={m50*nf:.3g} "
                f"({100*m50*nf/snv:.3g}% of {snv:.2g} possible SNV changes); m*q at flip {m50*q:.2f}")
    r["genome_rows"] = rows
    # neutral subset: lambda for a neutral difference (any of ~1e8-1e9 neutral sites)
    OUT["horn"] = r


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    t0 = time.time()
    for name, fn in [("horn", part_horn), ("excess", part_excess), ("linked", part_linked), ("ddiag", part_ddiag),
                     ("pfix", part_pfix), ("dilution", part_dilution)]:
        if what in ("all", name):
            fn()
    say(f"total {time.time()-t0:.0f} s")
    if what == "all":
        with open(os.path.join(RAW, "g1b_raw.json"), "w") as f:
            json.dump(OUT, f, indent=1, default=float)
        with open(os.path.join(RAW, "g1b_out.txt"), "w") as f:
            f.write("\n".join(OUT["_log"]) + "\n")


if __name__ == "__main__":
    main()

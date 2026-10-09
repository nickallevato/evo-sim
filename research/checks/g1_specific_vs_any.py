"""G1/G3 -- the "Bernoulli Barrier": does p^n price a SPECIFIC outcome or ANY outcome?  THROWAWAY research check.

Run:  research/.venv/bin/python -I research/checks/g1_specific_vs_any.py [all|arith|binom|indep|sweeps|onegen|fig]
Outputs: research/checks/results/raw/g1_out.txt (stdout copy), g1_raw.json, g1_flip.svg.
Seeds: numpy SeedSequence([20261040, part, config, rep]) -- no hash() seeds.

CLAIMS AND WHAT EACH PROBABILITY IS THE PROBABILITY *OF* (author's own words; local copies under sources/raw/, read only)
 Ga  Z18165980 (MITTENS 2025) Results: "For n independent fixation events each with probability p, simultaneous success
     requires: P(all) = p^{n}"; "For n = 20,000,000 fixations ... and p = 0.02: P(all) ≈ 0.02^{20,000,000} ≈
     10^{−34,000,000}"; abstract: "The Bernoulli Barrier (p^{n} ≈ 10^{−34,000,000} for parallel fixation) forces
     sequential fixation".  p = 0.02 = "P_{survive} ≈ 2s" (Transmission condition).  EVENT: n given fixation events
     (each a new beneficial arising that must escape drift) ALL succeed.
 G4  Darwillion (book, via McCarthy's quotation, secondhand): "the probability of 20 million independent fixation events
     each succeeding with probability 1 in 20,000 is: (1/20,000)^20,000,000 = 10^−86,000,000".  p = 1/(2N), N = 10,000
     (neutral).  Same quotation, preceding step: "If 50,000 mutations arise per year and 2.2 need to succeed, the
     required success rate would be one in 23,000".
 Gb  Z18167588 s4.1: "the probability that an individual carries all n beneficial alleles" = 0.5^157,000.  EVENT: one
     individual's genotype is the all-beneficial one (s7.10 concedes per-locus response is not denied).
 G   Z18167588 s3: best/worst of N = 10,000 differ by 1,474 alleles; "Fitness ratio = (1.01)^1474 ≈ 14.7x"; "Required
     ratio = 157,000 x 0.01 = 1,570x"; "Shortfall = 1,570 / 14.7 ≈ 107x".
 Gc  Z18167588 s7.8: "Working backward from the constraint, the active zone can sustain approximately 200–300
     simultaneous sweeps"; "Maximum fixations ≈ (300,000 / 440) x 230 ≈ 157,000".
 Gd  Z18167588 s7.9: "Required input ≈ 230 / 0.02 ≈ 11,500 beneficial mutations per transit period".
 G3  McCarthy MC-01/02: the product prices "a particular group or a pre-specified list of 20 million mutations";
     evolution needs "only that some 20 million out of an enormous pool of candidate mutations become fixed".
 G3a Camestros CA-09: "the probability that SOME number is picked is close to 1".
 G3b Day (blog 2026-10-01, Education of a Population Geneticist, para 28-29, replying to Mansfield's comment "set up to
     calculate the probability of just one set of 20 million fixations"): "Either the specific fixations matter — in
     which case the Darwillion applies — or they’re interchangeable — in which case they’re neutral noise that can’t
     explain the observed functional divergence."

PARTS
 A arith : exact log-space arithmetic (mpmath) of every headline number and of candidate sources of "230".
 B binom : P_specific = p^n vs P_any = P(Binomial(M,p) >= n); flip point M_50 ~ n/p; Chernoff bound for McCarthy's M.
           Day's horn formalised: n_f required functional changes, each satisfiable by any of m interchangeable
           alternatives, each alternative succeeding (arising AND fixing within the window) with probability q:
           P_all = (1-(1-q)^m)^n_f.  Flip point lambda_50 = m*q at which P_all = 1/2; table of m* for several q.
 C indep : haploid Wright-Fisher, N = 1000, s = 0.01, multiplicative fitness, soft selection.  L = 50 new mutations
           introduced at t = 0 in distinct individuals; run to absorption.  Free recombination / linked (1 M map) /
           clonal.  Tests whether fixation indicators of co-segregating loci are independent: per-locus P_fix vs
           Kimura, dispersion of the count K, and P(two (three) PRE-SPECIFIED loci all fix) / p^2 (p^3).
 D sweeps: same WF, free recombination, L loci all starting at p0 = 0.1 (inside Day's 0.1<p<0.9 "active zone")
           for L in {1, 14, 230, 1000}; multiplicative fitness (Day's stated s3.1 model) vs additive absolute fitness
           w = 1 + s*(count) (the scale on which Day's 14.7 and 1,570 are computed).  Per-locus P_fix and fixation time.
 E onegen: Day's own configuration: N = 10,000 individuals (haploid genomes), n loci all at p = 0.5 (n up to 157,000),
           s = 0.01.  Exact expected one-generation response E[p'_j | X] = sum_i w_i x_ij / sum_i w_i (no parent-
           sampling noise), effective number of parents (sum w)^2/sum w^2, best/mean fitness.  Multiplicative vs additive.

PRE-REGISTERED PREDICTIONS (written before any run of this file)
 P1 arith: log10 0.02^(2e7) = -33,979,400 (reproduces "10^-34,000,000" to 0.06%); log10 0.5^157,000 = -47,261.7;
    Darwillion log10 (1/20,000)^(2e7) = -86,020,600 (book "-86,000,000"); both lineages -172,041,200.
    1.01^1474 = 2.3e6, NOT 14.7; 14.7 = 1474 x 0.01 (additive); 1,570/14.74 = 106.5.  z = Phi^-1(1 - 1/10^4) = 3.719
    reproduces 1,474 (expected range of 10^4 normals ~7.7 sd would give ~1,530).  "230" = 157,000 x t_transit / T =
    230.0 (within 0.2%), i.e. the cap equals the target times the transit time over the window (circular); the paper's
    own s3 criterion gives n <= z^2 = 13.8; the additive-fitness halving point n*s*pbar = 1 at pbar = 0.5 gives
    n = 200 (inside "200-300") -- registered only as a coincidence check, not as what Day did.
    Gd's 7.8e6 = 157,000/0.02 = 7.85e6 = the "any n of M" expected-arisings calculation.
 P2 binom: P_any(>= n of M) ~ 1 for M p >> n; transition centred at M = n/p with relative width ~ +-1.645/sqrt(n)
    (sharp). McCarthy's inputs (M = 4.5e11, p = 5e-5, n = 2e7): P(K < n) <= 10^-(5e4..8e4) (Chernoff).
 P3 horn: lambda_50 = ln(n_f/ln 2): 7.27 (n_f=1e3), 12.33 (157,000), 12.57 (2e5), 17.18 (2e7); 5%-95% band width in
    lambda = ln(ln20 / -ln0.95) = 4.07 for every n_f.  Per-site lambda_site = 2N (mu/3) T 2s with Day-family inputs
    (N=1e4, mu=1.2e-8, T=3e5, s=0.01) = 0.48 (q = 0.38): m* ~ 36 alternatives per required change at n_f = 2e7,
    ~27 at 2e5; with q = 0.02 (one arising, no recurrence) m* ~ 850 at 2e7.  Specific-site horn: log10 q_site^(2e7)
    ~ -8.4e6 (still astronomically small -- Day's conclusion holds on the specific horn).
 P4 indep: free recombination: per-locus P_fix within 10% of Kimura haploid u = 0.0198; dispersion index of K
    1.00 +- 0.10; pair ratio P(both of a specified pair fix)/p^2 = 1 +- 0.2; triple ratio 1 +- 0.5.  Linked (1 M):
    pair ratio < 1 (Hill-Robertson; predicted 0.5-0.95).  Clonal: pair ratio = 0 by construction (distinct
    backgrounds, no recombination, no new mutation), dispersion < 1, per-locus P_fix < Kimura.
 P5 sweeps: multiplicative: per-locus P_fix within 5% of single-locus haploid u(p0=0.1) = 0.865 for L = 1..1000 and
    mean fixation time within 10% of L = 1 -- no cap near 230.  Additive: P_fix at L = 230 lower than multiplicative
    by >= 5%, at L = 1000 lower by >= 20% (<= 0.70), mean fixation time at L = 1000 >= 2x the L = 1 value.
 P6 onegen: multiplicative: mean Delta p per locus = s p q/(1+s p) = 0.002488 at every n (1 .. 157,000) within MC error;
    N_eff ~ N exp(-n (ln1.01)^2/4): ~205 at n = 157,000 (best/mean relative fitness 150-450).  Additive: Delta p =
    s p q/(1 + s n p): 0.00116 at n = 230, 3.2e-6 at n = 157,000 (786x dilution); best/mean ~1.01 (compressed).
    I.e. the LLN compression of the COUNT's CV is real (Day right on that arithmetic) but per-locus response is
    unaffected in the multiplicative model; in the additive model the dilution comes from mean fitness growing, and
    the absolute variance of fitness grows with n in both models.
"""
import os, sys, json, time, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import mpmath as mp
from multiprocessing import Pool

SEED = 20261040
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "results", "raw")
OUT = {}
mp.mp.dps = 50


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    OUT.setdefault("_log", []).append(s)


def l10(x):
    return float(mp.log10(x))


# ----------------------------------------------------------------------------------------------- A arithmetic
def part_arith():
    say("== A. headline arithmetic (mpmath, 50 digits)")
    r = {}
    r["Ga_log10_0.02^2e7"] = float(2e7 * mp.log10(mp.mpf("0.02")))
    r["Gb_log10_0.5^157000"] = float(157000 * mp.log10(mp.mpf("0.5")))
    r["Gb_universes_exp"] = round(-r["Gb_log10_0.5^157000"]) - 80
    r["G4_darwillion_log10"] = float(2e7 * mp.log10(mp.mpf(1) / 20000))
    r["G4_both_lineages_log10"] = 2 * r["G4_darwillion_log10"]
    r["Ga_rel_err_vs_34e6"] = (34e6 + r["Ga_log10_0.02^2e7"]) / 34e6
    n, N, s = 157000, 10000, 0.01
    sd = math.sqrt(n * 0.25)
    z_q = float(mp.sqrt(2) * mp.erfinv(1 - 2 / mp.mpf(N)))  # Phi^-1(1 - 1/N)
    # expected max of N iid standard normals (numerical integral)
    f = lambda x: x * N * mp.npdf(x) * mp.ncdf(x) ** (N - 1)
    z_e = float(mp.quad(f, [-10, 0, 3, 4, 10]))
    r.update(sd=sd, cv=sd / (n / 2), z_quantile=z_q, z_expected_max=z_e,
             diff_quantile=2 * z_q * sd, diff_expected=2 * z_e * sd)
    d = 1474
    r["mult_1.01^1474"] = float(mp.power(mp.mpf("1.01"), d))
    r["add_1474*0.01"] = d * s
    r["required_add"] = n * s
    r["required_mult_log10"] = float(n * mp.log10(mp.mpf("1.01")))
    r["shortfall_additive"] = n * s / (d * s)
    r["shortfall_paper"] = 1570 / 14.7
    r["shortfall_mult_log10"] = r["required_mult_log10"] - l10(mp.power(mp.mpf("1.01"), d))
    t_tr = (2 / s) * math.log(9)
    r["t_transit"] = t_tr
    r["Gc_product_440"] = 300000 / 440 * 230
    r["Gc_cap_from_target_440"] = 157000 * 440 / 300000
    r["Gc_cap_from_target_exact"] = 157000 * t_tr / 300000
    r["Gc_paper_s3_criterion_z2"] = z_q ** 2
    r["Gc_additive_halving_n_at_p0.5"] = 1 / (s * 0.5)
    r["Gc_reproductive_ceiling_loci"] = [1.0 / s, 2.0 / s]
    r["Gd_input"] = 230 / 0.02
    r["Gd_total"] = 300000 / 440 * 230 / 0.02
    r["Gd_equals_n_over_p"] = 157000 / 0.02
    # McCarthy / book "any" arithmetic (secondhand quotation of the book)
    r["book_required_rate_1_in"] = 50000 / (2e7 / 9e6)
    r["mccarthy_expected"] = 4.5e11 / 20000
    for k, v in r.items():
        say(f"  {k:34s} {v}")
    OUT["arith"] = r
    return r


# ----------------------------------------------------------------------------------------------- B binomial
def chernoff_log10_lower(M, p, n):
    """log10 upper bound on P(Binomial(M,p) < n) for n < M p:  exp(-M KL(a||p)), a = n/M."""
    M, p, n = mp.mpf(M), mp.mpf(p), mp.mpf(n)
    a = n / M
    D = a * mp.log(a / p) + (1 - a) * mp.log((1 - a) / (1 - p))
    return float(-M * D / mp.log(10))


def p_any_normal(M, p, n):
    mu, sd = M * p, math.sqrt(M * p * (1 - p))
    from scipy.stats import norm
    return float(norm.sf((n - 0.5 - mu) / sd))


def part_binom():
    say("== B. specific vs any")
    from scipy.stats import binom
    r = {"specific_log10": {}, "any_flip": [], "horn": [], "horn_m": []}
    for (lab, p, n) in [("Ga 0.02^2e7", 0.02, 2e7), ("G4 (1/2e4)^2e7", 5e-5, 2e7), ("Gb 0.5^157000", 0.5, 157000),
                        ("p=0.02, n=157000", 0.02, 157000), ("p=0.02, n=2e5 (Day's 1% scenario)", 0.02, 2e5)]:
        r["specific_log10"][lab] = float(n * mp.log10(p))
        say(f"  P_specific {lab:36s} log10 = {r['specific_log10'][lab]:.1f}")
    # any-n-of-M flip points
    say("  any-n-of-M: M_50 (P_any = 0.5), M_05 / M_95 (P_any = 0.05 / 0.95), relative half-width")
    for n in [1e3, 157000, 2e5, 2e7]:
        for p in [0.02, 0.002, 5e-5]:
            M50 = n / p
            hw = 1.645 / math.sqrt(n)  # relative half-width of the 5-95% band (normal approx)
            # check exactly with scipy at the band edges (n integer)
            Mlo, Mhi = M50 * (1 - hw), M50 * (1 + hw)
            ex = (float(binom.sf(int(n) - 1, int(Mlo), p)), float(binom.sf(int(n) - 1, int(M50), p)),
                  float(binom.sf(int(n) - 1, int(Mhi), p)))
            row = dict(n=n, p=p, M50=M50, rel_halfwidth=hw, P_at_Mlo_M50_Mhi=ex)
            r["any_flip"].append(row)
            say(f"   n={n:>9.3g} p={p:<7g} M50={M50:.4g}  +-{100*hw:.3f}%  exact P_any at (lo,50,hi)="
                f"({ex[0]:.3f},{ex[1]:.3f},{ex[2]:.3f})")
    # McCarthy's inputs and Day-family supplies
    M_mc = 4.5e11
    lc = chernoff_log10_lower(M_mc, 5e-5, 2e7)
    r["mccarthy"] = dict(M=M_mc, p=5e-5, n=2e7, mean=M_mc * 5e-5, sd=math.sqrt(M_mc * 5e-5 * (1 - 5e-5)),
                         z=(2e7 - M_mc * 5e-5) / math.sqrt(M_mc * 5e-5), log10_P_fail_chernoff=lc)
    say(f"  McCarthy: mean {M_mc*5e-5:.4g}, z = {r['mccarthy']['z']:.1f}, log10 P(K<2e7) <= {lc:.0f}")
    # beneficial-fraction needed for 'any' at p = 2s
    r["fb_needed"] = {f"n={n:g},p={p}": (n / p) / M_mc for n in [157000, 2e5, 2e7] for p in [0.02, 0.002]}
    say("  beneficial fraction of all new mutations needed for M_50 = n/p (supply 4.5e11):",
        {k: f"{v:.3g}" for k, v in r["fb_needed"].items()})

    # Day's horn: n_f required functional changes, m interchangeable alternatives each, per-alternative success q
    say("  HORN: P_all = (1-(1-q)^m)^n_f; lambda = -m ln(1-q) (= m q for small q)")
    for nf in [1e3, 157000, 2e5, 2e7]:
        l50 = float(mp.log(nf / mp.log(2)))  # large-n approx; exact below
        # exact: (1-e^-lam)^nf = P  =>  lam = -ln(1 - P^(1/nf))
        ex = {P: float(-mp.log(1 - mp.power(mp.mpf(P), 1 / mp.mpf(nf)))) for P in (0.05, 0.5, 0.95)}
        r["horn"].append(dict(n_f=nf, lam50_approx=l50, lam05=ex[0.05], lam50=ex[0.5], lam95=ex[0.95],
                              width=ex[0.95] - ex[0.05]))
        say(f"   n_f={nf:>9.3g}  lambda_05={ex[0.05]:.3f} lambda_50={ex[0.5]:.3f} lambda_95={ex[0.95]:.3f}"
            f"  width={ex[0.95]-ex[0.05]:.3f}")
    # q values from Day-family parameters
    N, mu, T = 1.0e4, 1.2e-8, 3.0e5
    qdefs = {
        "one arising, s=0.01 (q=2s)": 0.02,
        "one arising, s=0.001 (q=2s)": 0.002,
        "specific nucleotide, recurrent, s=0.01, T=3e5": 1 - math.exp(-2 * N * (mu / 3) * T * 0.02),
        "specific nucleotide, recurrent, s=0.001, T=3e5": 1 - math.exp(-2 * N * (mu / 3) * T * 0.002),
        "specific nucleotide, recurrent, s=0.01, T=2.52e5": 1 - math.exp(-2 * N * (mu / 3) * 2.52e5 * 0.02),
    }
    r["q"] = qdefs
    for lab, q in qdefs.items():
        lam1 = -math.log(1 - q)
        row = {"q_def": lab, "q": q, "lambda_per_alt": lam1}
        for h in r["horn"]:
            row[f"m50_nf={h['n_f']:g}"] = math.ceil(h["lam50"] / lam1)
            row[f"m05_nf={h['n_f']:g}"] = math.ceil(h["lam05"] / lam1)
            row[f"m95_nf={h['n_f']:g}"] = math.ceil(h["lam95"] / lam1)
        row["log10_specific_nf=2e7"] = float(2e7 * mp.log10(q))
        row["log10_specific_nf=2e5"] = float(2e5 * mp.log10(q))
        r["horn_m"].append(row)
        say(f"   q={q:.4g} ({lab}); per-alt lambda {lam1:.4g}; m* (P=0.05/0.5/0.95): " +
            "; ".join(f"n_f={h['n_f']:g}: {row[f'm05_nf={h['n_f']:g}']}/{row[f'm50_nf={h['n_f']:g}']}/"
                      f"{row[f'm95_nf={h['n_f']:g}']}" for h in r["horn"]) +
            f"; specific log10 (n=2e7) {row['log10_specific_nf=2e7']:.4g}")
    OUT["binom"] = r
    return r


# ----------------------------------------------------------------------------------------------- WF machinery
def kimura_hap(s, N, p0):
    return (1 - math.exp(-2 * N * s * p0)) / (1 - math.exp(-2 * N * s))


def wf_run(G, s, fit, rec, rng, rmap=None, pos=None, max_gen=200000, track_active=False):
    """Haploid soft-selection WF on genotype matrix G (N x L, uint8).  Runs until every locus is fixed or lost.
    fit: 'mult' w = (1+s)^count ; 'add' w = 1 + s*(count + n_fixed).  rec: 'free' | 'clonal' | 'linked'.
    Returns outcome (1 fixed, 0 lost) and absorption generation per locus, and optional active-zone counts."""
    N, L = G.shape
    idx = np.arange(L)
    outcome = np.full(L, -1, np.int8)
    tabs = np.zeros(L, np.int64)
    nfixed = 0
    lnw1 = math.log1p(s)
    act_hist = []
    gen = 0
    # absorb anything absorbed at start
    while G.shape[1] > 0 and gen < max_gen:
        cs = G.sum(0)
        fx, ls = cs == N, cs == 0
        if fx.any() or ls.any():
            outcome[idx[fx]] = 1
            outcome[idx[ls]] = 0
            tabs[idx[fx | ls]] = gen
            nfixed += int(fx.sum())
            keep = ~(fx | ls)
            G, idx = G[:, keep], idx[keep]
            if pos is not None:
                pos = pos[keep]
            if G.shape[1] == 0:
                break
            cs = cs[keep]
        if track_active:
            f = cs / N
            act_hist.append(int(((f > 0.1) & (f < 0.9)).sum()))
        c = G.sum(1, dtype=np.int64)
        if fit == "mult":
            lw = c * lnw1
            w = np.exp(lw - lw.max())
        else:
            w = 1.0 + s * (c + nfixed)
        cw = np.cumsum(w)
        cw /= cw[-1]
        a = np.minimum(np.searchsorted(cw, rng.random(N)), N - 1)
        if rec == "clonal" or G.shape[1] == 1:
            G = G[a]
        else:
            b = np.minimum(np.searchsorted(cw, rng.random(N)), N - 1)
            Lc = G.shape[1]
            if rec == "free":
                m = rng.integers(0, 2, size=(N, Lc), dtype=np.uint8).astype(bool)
            else:  # linked: crossover process along ordered positions (Morgans), Haldane map
                d = np.diff(pos)
                rr = 0.5 * (1 - np.exp(-2 * d))
                sw = rng.random((N, Lc - 1)) < rr
                start = rng.integers(0, 2, size=(N, 1), dtype=np.int64)
                m = (np.concatenate([start, start + np.cumsum(sw, 1)], 1) % 2).astype(bool)
            G = np.where(m, G[a], G[b])
        gen += 1
    return outcome, tabs, act_hist


# ----------------------------------------------------------------------------------------------- C independence
def job_indep(args):
    cfg, rep, N, L, s, rec, rmapM = args
    rng = np.random.default_rng(np.random.SeedSequence([SEED, 3, cfg, rep]))
    G = np.zeros((N, L), np.uint8)
    rows = rng.choice(N, L, replace=False)
    G[rows, np.arange(L)] = 1
    pos = np.sort(rng.random(L)) * rmapM if rec == "linked" else None
    out, t, _ = wf_run(G, s, "mult", rec, rng, pos=pos)
    return cfg, out, t


def part_indep(reps=4000, workers=10):
    say("== C. independence of co-segregating fixations (N=1000 haploid, s=0.01, L=50 new mutations at t=0)")
    N, L, s = 1000, 50, 0.01
    cfgs = [(0, "free", 0.0), (1, "linked", 1.0), (2, "clonal", 0.0)]
    jobs = [(c, r, N, L, s, rec, rm) for (c, rec, rm) in cfgs for r in range(reps)]
    t0 = time.time()
    with Pool(workers) as pool:
        res = pool.map(job_indep, jobs, chunksize=20)
    u = kimura_hap(s, N, 1 / N)
    r = {"N": N, "L": L, "s": s, "reps": reps, "kimura_u": u, "cfg": {}}
    for (c, rec, rm) in cfgs:
        O = np.array([o for (cc, o, t) in res if cc == c])  # reps x L
        assert (O >= 0).all()
        K = O.sum(1).astype(float)
        p = K.mean() / L
        var_b = L * p * (1 - p)
        disp = K.var(ddof=1) / var_b
        pair = (K * (K - 1)).mean() / (L * (L - 1) * p * p)
        trip = (K * (K - 1) * (K - 2)).mean() / (L * (L - 1) * (L - 2) * p ** 3)
        # bootstrap SE for pair/trip ratios over replicates
        bs = np.random.default_rng(np.random.SeedSequence([SEED, 33, c]))
        pr, tr = [], []
        for _ in range(400):
            Kb = K[bs.integers(0, len(K), len(K))]
            pb = Kb.mean() / L
            pr.append((Kb * (Kb - 1)).mean() / (L * (L - 1) * pb * pb))
            tr.append((Kb * (Kb - 1) * (Kb - 2)).mean() / (L * (L - 1) * (L - 2) * pb ** 3))
        se_p = math.sqrt(p * (1 - p) / (len(K) * L))
        row = dict(rec=rec, map_M=rm, p_fix=p, se=se_p, p_over_kimura=p / u, K_mean=K.mean(), K_var=K.var(ddof=1),
                   dispersion=disp, pair_ratio=pair, pair_se=float(np.std(pr)), trip_ratio=trip,
                   trip_se=float(np.std(tr)), maxK=int(K.max()))
        r["cfg"][rec] = row
        say(f"  {rec:7s} P_fix={p:.5f}+-{se_p:.5f} (Kimura {u:.5f}, ratio {p/u:.3f}); K mean {K.mean():.3f} "
            f"var {K.var(ddof=1):.3f} dispersion {disp:.3f}; P(pair)/p^2 = {pair:.3f}+-{np.std(pr):.3f}; "
            f"P(triple)/p^3 = {trip:.3f}+-{np.std(tr):.3f}; max K {int(K.max())}")
    say(f"  ({time.time()-t0:.0f} s)")
    OUT["indep"] = r
    return r


# ----------------------------------------------------------------------------------------------- D sweeps
def job_sweep(args):
    cfg, rep, N, L, s, fit, p0 = args
    rng = np.random.default_rng(np.random.SeedSequence([SEED, 4, cfg, rep]))
    G = (rng.random((N, L)) < p0).astype(np.uint8)
    out, t, act = wf_run(G, s, fit, "free", rng, track_active=True)
    return cfg, L, fit, out, t, (max(act) if act else 0), (float(np.mean(act[:200])) if act else 0.0)


def part_sweeps(workers=10):
    say("== D. simultaneous sweeps from p0 = 0.1 (N=1000 haploid, s=0.01, free recombination)")
    N, s, p0 = 1000, 0.01, 0.1
    reps = {1: 2000, 14: 150, 230: 12, 1000: 4}
    jobs, cfg = [], 0
    for fit in ("mult", "add"):
        for L, R in reps.items():
            jobs += [(cfg, r, N, L, s, fit, p0) for r in range(R)]
            cfg += 1
    t0 = time.time()
    with Pool(workers) as pool:
        res = pool.map(job_sweep, jobs, chunksize=1)
    u = kimura_hap(s, N, p0)
    r = {"N": N, "s": s, "p0": p0, "kimura_u": u, "rows": []}
    for fit in ("mult", "add"):
        for L in reps:
            sel = [x for x in res if x[1] == L and x[2] == fit]
            O = np.concatenate([x[3] for x in sel])
            T = np.concatenate([x[4] for x in sel])
            pf = O.mean()
            se = math.sqrt(pf * (1 - pf) / len(O))
            tf = T[O == 1]
            row = dict(fit=fit, L=L, reps=len(sel), loci=len(O), p_fix=pf, se=se, p_over_kimura=pf / u,
                       t_fix_mean=float(tf.mean()), t_fix_se=float(tf.std(ddof=1) / math.sqrt(len(tf))),
                       max_active=int(max(x[5] for x in sel)), mean_active_first200=float(np.mean([x[6] for x in sel])))
            r["rows"].append(row)
            say(f"  {fit:4s} L={L:5d} loci={len(O):5d} P_fix={pf:.4f}+-{se:.4f} (single-locus u {u:.4f}, ratio "
                f"{pf/u:.3f}); mean t_fix {tf.mean():.0f}+-{row['t_fix_se']:.0f}; max # in 0.1<p<0.9: "
                f"{row['max_active']}")
    say(f"  ({time.time()-t0:.0f} s)")
    OUT["sweeps"] = r
    return r


# ----------------------------------------------------------------------------------------------- E one generation
def job_onegen(args):
    n, rep, N, s, chunk = args
    base = np.random.SeedSequence([SEED, 5, n, rep])
    kids = base.spawn((n + chunk - 1) // chunk)
    sizes = [min(chunk, n - i * chunk) for i in range(len(kids))]
    c = np.zeros(N, np.int64)
    for k, m in zip(kids, sizes):
        X = np.random.default_rng(k).integers(0, 2, size=(N, m), dtype=np.uint8)
        c += X.sum(1, dtype=np.int64)
    res = {}
    for fit in ("mult", "add"):
        if fit == "mult":
            lw = c * math.log1p(s)
            w = np.exp(lw - lw.max())
        else:
            w = 1.0 + s * c
        wn = w / w.sum()
        neff = 1.0 / float((wn ** 2).sum())
        best = float(w.max() / w.mean())
        sdp, sdl = 0.0, 0.0
        for k, m in zip(kids, sizes):
            X = np.random.default_rng(k).integers(0, 2, size=(N, m), dtype=np.uint8)
            p = X.mean(0, dtype=np.float64)
            pp = wn @ X.astype(np.float64)
            dp = pp - p
            if fit == "mult":
                exp_dp = s * p * (1 - p) / (1 + s * p)
            else:
                exp_dp = s * p * (1 - p) / (1 + s * c.mean())
            sdp += float(dp.sum())
            sdl += float(exp_dp.sum())
        res[fit] = dict(sum_dp=sdp, sum_expected=sdl, neff=neff, best_over_mean=best)
    return n, rep, res, float(c.std()), float(c.mean())


def part_onegen(workers=6):
    say("== E. one-generation response at Day's configuration (N=10,000, all n loci at p=0.5, s=0.01)")
    N, s = 10000, 0.01
    ns = [1, 14, 230, 2300, 23000, 157000]
    jobs = []
    for n in ns:
        R = min(400, max(3, math.ceil(2e5 / n)))
        jobs += [(n, r, N, s, 2048) for r in range(R)]
    t0 = time.time()
    with Pool(workers) as pool:
        res = pool.map(job_onegen, jobs, chunksize=1)
    r = {"N": N, "s": s, "rows": []}
    for n in ns:
        sel = [x for x in res if x[0] == n]
        for fit in ("mult", "add"):
            dps = np.array([x[2][fit]["sum_dp"] / n for x in sel])
            exs = np.array([x[2][fit]["sum_expected"] / n for x in sel])
            neff = np.array([x[2][fit]["neff"] for x in sel])
            best = np.array([x[2][fit]["best_over_mean"] for x in sel])
            row = dict(n=n, fit=fit, reps=len(sel), mean_dp=float(dps.mean()),
                       se=float(dps.std(ddof=1) / math.sqrt(len(dps))) if len(dps) > 1 else float("nan"),
                       expected=float(exs.mean()), neff=float(neff.mean()), best_over_mean=float(best.mean()),
                       count_sd=float(np.mean([x[3] for x in sel])), count_mean=float(np.mean([x[4] for x in sel])))
            r["rows"].append(row)
            say(f"  n={n:6d} {fit:4s} reps={len(sel):4d} mean dp/locus={row['mean_dp']:.6g}+-{row['se']:.2g} "
                f"(expected {row['expected']:.6g}); N_eff parents {row['neff']:.1f}; best/mean w "
                f"{row['best_over_mean']:.4g}; count sd {row['count_sd']:.1f} (CV {row['count_sd']/row['count_mean']:.4f})")
    say(f"  ({time.time()-t0:.0f} s)")
    OUT["onegen"] = r
    return r


def part_onegen_counts(reps=400):
    """POST-HOC (added after the first 'all' run; not pre-registered): part E used 3-9 replicates at n >= 23,000
    and its SEs underestimated the per-replicate SD.  Exact identity: sum_j (E[p'_j|X] - p_j) = sum_i wn_i c_i - mean c,
    so the across-locus mean response needs only the counts c_i ~ Binomial(n, 1/2).  400 replicates per cell."""
    say("== E2 (post-hoc). count-level one-generation response, 400 reps (identity: mean dp = (weighted mean count - mean count)/n)")
    s = 0.01
    b = math.log1p(s)
    r = {"rows": []}
    for N in (10000, 100000):
        for n in (2300, 23000, 157000):
            rng = np.random.default_rng(np.random.SeedSequence([SEED, 6, N, n]))
            sh = {"mult": [], "add": []}
            ne = []
            best = []
            for _ in range(reps):
                c = rng.binomial(n, 0.5, N).astype(float)
                lw = c * b
                w = np.exp(lw - lw.max())
                wn = w / w.sum()
                sh["mult"].append(((wn * c).sum() - c.mean()) / n)
                ne.append(1 / (wn ** 2).sum())
                best.append(w.max() / w.mean())
                wa = 1 + s * c
                sh["add"].append(((wa / wa.sum() * c).sum() - c.mean()) / n)
            for fit in ("mult", "add"):
                a = np.array(sh[fit])
                exp_ = s * 0.25 / (1 + s * 0.5) if fit == "mult" else s * 0.25 / (1 + s * n * 0.5)
                row = dict(N=N, n=n, fit=fit, mean_dp=float(a.mean()), se=float(a.std(ddof=1) / math.sqrt(reps)),
                           expected=exp_, ratio=float(a.mean() / exp_))
                if fit == "mult":
                    row.update(neff=float(np.mean(ne)), neff_infinite_pop=N * math.exp(-n * b * b / 4),
                               best_over_mean=float(np.mean(best)))
                r["rows"].append(row)
                say(f"  N={N:6d} n={n:6d} {fit:4s} dp/locus={row['mean_dp']:.6g}+-{row['se']:.1g} expected "
                    f"{exp_:.6g} ratio {row['ratio']:.4f}" + (f"; N_eff {row['neff']:.0f} (infinite-pop formula "
                    f"{row['neff_infinite_pop']:.0f}); best/mean w {row['best_over_mean']:.3g}" if fit == "mult" else ""))
    OUT["onegen_counts"] = r
    return r


# ----------------------------------------------------------------------------------------------- figure
def part_fig():
    import matplotlib
    matplotlib.use("svg")
    import matplotlib.pyplot as plt
    plt.rcParams["svg.fonttype"] = "none"
    lam = np.linspace(0, 24, 600)
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    cols = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]  # dataviz reference palette slots 1-4
    for nf, ccol in zip([1e3, 1.57e5, 2e5, 2e7], cols):
        P = np.exp(nf * np.log1p(-np.exp(-np.maximum(lam, 1e-9))))
        lab = {1e3: "n_f = 1,000", 1.57e5: "n_f = 157,000 (Bernoulli paper)", 2e5: "n_f = 200,000 (MITTENS 1% scenario)",
               2e7: "n_f = 20,000,000 (Ga)"}[nf]
        ax.plot(lam, P, color=ccol, lw=2, label=lab)
    ax.axvline(0.48, color="#555", ls=":", lw=1)
    ax.text(0.6, 0.55, "one specific site, recurrent\nmutation, s=0.01 (m=1): λ≈0.48", fontsize=8, color="#333")
    ax.set_xlabel("λ = −m·ln(1−q): Poisson mean of successful arisings per required change")
    ax.set_ylabel("P(every required change achieved)")
    ax.set_title("Specific (m = 1) vs interchangeable (m alternatives): where the conclusion flips", fontsize=10)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False, fontsize=8, loc="lower right")
    ax.set_xlim(0, 24)
    ax.set_ylim(-0.02, 1.02)
    fig.tight_layout()
    path = os.path.join(RAW, "g1_flip.svg")
    fig.savefig(path, metadata={"Date": None})
    say(f"  figure -> {path}")


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    t0 = time.time()
    if what in ("all", "arith"):
        part_arith()
    if what in ("all", "binom"):
        part_binom()
    if what in ("all", "indep"):
        part_indep()
    if what in ("all", "sweeps"):
        part_sweeps()
    if what in ("all", "onegen"):
        part_onegen()
    if what in ("all", "onegen2"):
        part_onegen_counts()
    if what in ("all", "fig"):
        part_fig()
    say(f"total {time.time()-t0:.0f} s")
    if what == "onegen2":
        with open(os.path.join(RAW, "g1_onegen2_out.txt"), "w") as f:
            f.write("\n".join(OUT["_log"]) + "\n")
        with open(os.path.join(RAW, "g1_onegen2_raw.json"), "w") as f:
            json.dump(OUT, f, indent=1, default=float)
    if what == "all":
        with open(os.path.join(RAW, "g1_raw.json"), "w") as f:
            json.dump(OUT, f, indent=1, default=float)
        with open(os.path.join(RAW, "g1_out.txt"), "w") as f:
            f.write("\n".join(OUT["_log"]) + "\n")


if __name__ == "__main__":
    main()

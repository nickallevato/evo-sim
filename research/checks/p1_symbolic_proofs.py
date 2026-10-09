"""P1 -- Machine-checked derivations of the load-bearing identities the audit leans on.

PRE-REGISTRATION.  Committed BEFORE the run (2026-10-09).  Single process, deterministic (no random numbers).
Run (na-workhorse, single process, RAM target < 3 GB):
    research/.venv/bin/python -I research/checks/p1_symbolic_proofs.py
Outputs: results/raw/p1_symbolic_proofs.json (every identity, status, numbers) and p1_symbolic_proofs.out (log).
Tools: sympy (symbolic / exact rational), mpmath (high precision), scipy.linalg.solve_banded (float64 exact Markov
solves for M up to 2e4).  Rule RH: every item below is a dialectic (truth) claim; nothing here scores rhetoric.

STATUS LABELS (assigned by the script, not by hand):
  proved     -- sympy reduces the identity to 0 / True symbolically, or exact rational arithmetic gives equality
                for the stated case (exact for that case; "proved for M = ..." where it is a finite check).
  confirmed  -- numerically confirmed within the pre-registered tolerance (float64 or mpmath).
  failed     -- outside the pre-registered tolerance, or sympy could not reduce it (recorded, not hidden).
  For Day's quoted arithmetic (block E) the labels are: holds (printed value = exact value at the printed
  precision, within 0.5%), slip (printed value off by more than 0.5% but the stated conclusion is not moved by
  more than 25%; rule R1 is NOT applied here, the label is descriptive only), or discrepancy (larger).

DISCLOSURE.  Most block-E arithmetic was already recomputed by hand (python3 -I) in the claim files during R2
  (A-mittens-formula, A5e, H, H3, B2b, B2c, A2b and quotes-day.md notes); those predictions are informed by
  that.  The B0.2 baseline (exact WF chain 3.935N at N=50) and B2a (exponent -pi^2) are known results of
  earlier checks.  Nothing in blocks A-D has been run in this form before this commit.

WHICH IDENTITIES, AND WHY (sources: hierarchy.yaml load-bearing nodes; R5-draft s1; RESULTS.md B0-B3, B1b,
B2a, H; claims B1, B3a, B7, B2a, B2b, B2c, H, A, A5e, H3):

A. Neutral substitution rate k = mu (claims B1, B7, B3a, B5; load-bearing B1, B3a, B5, B7).
  A1 haploid k = N mu * 1/N = mu; diploid k = 2N mu * 1/(2N) = mu (sympy).               Predict: proved.
  A2 neutral P_fix = initial frequency: (i) binomial mean E[X'|X=i] = i symbolically; (ii) exact rational WF
     chain M = 10: h_i = i/M exactly; (iii) float64 banded WF chain M = 2N for N = 50, 500, 1e4:
     max|h_i - i/M| <= 1e-9.                                                          Predict: proved / confirmed.
  A3 P_fix does not depend on N_e (B3 / B3a / B7): exchangeable Dirichlet-multinomial Cannings chain, M = 100,
     alpha = 0.25 (M_e = 20.8) and alpha = 1 (M_e = 50.5): P_fix(1 copy) = 1/M to 1e-10; the beta-binomial
     mean is i (sympy).  Day-side (1/(2N_e), Z18429937 etc., withdrawn 2026-08-27, B3g) predicts
     P_fix = 1/M_e = 0.048 / 0.0198; critic side (and Day after 2026-08-27, Z23188201) predicts 1/M = 0.01.
     Predict: 1/M (critic side and current Day side), i.e. confirmed.
     The conditional fixation time instead scales with M_e (Day right on time, B3): t*(DM) / diffusion value
     -2 M_e (1-p) ln(1-p)/p at p = 1/M within 15%.                                  Predict: confirmed.
  A4 start state (B1, B1c, B1d): with fixation-age pmf f_a of a neutral new mutation conditioned on fixing,
     (i) stationary infinite past: substitutions per generation = mu * sum_a f_a = mu exactly;
     (ii) monomorphic (empty) start: E K(T) = mu * sum_{t<T} P(tau <= t) and the deficit mu*T - E K(T)
          -> mu * E[tau] as T -> infinity (E[tau] ~ 4N, Day's "T - 4N_e").
     sympy proof for a geometric f_a family (closed form), and exact WF chain M = 20 (N = 10) with mpmath
     (dps 40): deficit / (mu E[tau]) at T = 30 E[tau] equals 1 within 1e-12; stationary sum = 1 within 1e-12.
     Both sides' formulas are predicted to hold as identities: Day's U(T - 4N_e) for an empty start and the
     critics' U*T for a full one.  The dispute (which start applied) is external and NOT decided here.
                                                                                    Predict: proved / confirmed.
B. Kimura fixation probability (claims B7a, F4, F3; baselines B0.3).
  B1 u(p) = (1 - e^{-4Nsp})/(1 - e^{-4Ns}) solves (V/2) u'' + M u' = 0 with M = s p q, V = p q/(2N),
     u(0) = 0, u(1) = 1 (sympy).                                                      Predict: proved.
  B2 limits: s -> 0 gives p; at p = 1/(2N), N -> infinity gives 1 - e^{-2s}; its series is 2s - 2s^2 + ...
     (sympy).                                                                          Predict: proved.
  B3 exact diploid additive WF (fitness 1, 1+s, 1+2s; M = 2N binomial sampling), P_fix(1 copy) by banded
     linear solve vs Kimura (1 - e^{-2s})/(1 - e^{-4Ns}) at the audit's ranges: (N, s) = (100, 0.01),
     (500, 0.01), (1000, 0.005), (1e4, 0.001) [Day's F3 parameters, 2Ns = 20], (50, 0.05) [strong].
     Predict |exact/Kimura - 1| <= 2% for s <= 0.01, <= 5% at s = 0.05; the ratio to 2s is about 1 - s.
     Code check: mpmath dps 40 dense solve at N = 10, s = 0.01 agrees with the float64 banded solve to 1e-11.
  B4 Moran (haploid, M copies, relative fitness r): h_i = (1 - r^{-i})/(1 - r^{-M}) satisfies
     (1 + r) h_i = r h_{i+1} + h_{i-1} (sympy); M -> infinity gives h_1 = 1 - 1/r.     Predict: proved.
C. Mean neutral fixation time "4N_e" (Day Q45: "4N_e generations for a neutral allele"; claims B7b, B1, B2a).
  C1 diffusion conditional time t*(p) = -4N (1-p) ln(1-p)/p solves (V/2) t'' + (V u'/u) t' = -1 with
     u = p, t*(1) = 0, and t*(p) -> 4N as p -> 0 (sympy).                              Predict: proved.
  C2 exact WF conditional time from 1 copy, M = 2N, N = 10, 25, 50, 100, 200, 500, 1e4 (banded):
     exact / diffusion(p = 1/(2N)) in [0.94, 1.0] at N = 10 and within 1.5% for N >= 50, deviation shrinking
     with N; N = 50 gives 3.935 N (B0.2).                                             Predict: confirmed.
  C3 exact Moran (with self-replacement; up = down = i(M-i)/M^2 per event), exact rationals: conditional
     fixation time from 1 copy = M(M-1) events = M - 1 generations, for M = 5, 10, 20, 50, 100; the diffusion
     value (per-generation variance 2pq/M, i.e. 4N_e = M) is -M^2 (1-1/M) ln(1-1/M) ~ M - 1/2.
                                                                                       Predict: proved (for those M).
D. Haldane's cost of substitution (claims H, H2, H3, H5; load-bearing H).
  Definition used (Haldane 1957 is NOT retrieved; the definition is the standard textbook one and is flagged):
  D = sum over generations of (1 - wbar_t / w_max), genotype fitnesses AA = 1, Aa = 1 - h s, aa = 1 - s,
  A the substituting allele from p0 to 1.  Continuous limit: D = int_{p0}^{1} (2ph + q)/(p (ph + q(1-h))) dp.
  D1 sympy: h = 0 (A dominant): D = ln(1/p0); h = 1/2: D = 2 ln(1/p0); h = 1 (A recessive):
     D = 1/p0 - 1 + ln(1/p0).  D is independent of s at first order.                  Predict: proved.
  D2 discrete recursion (exact genotype recursion, no s expansion), p0 = 1e-3, run to q = 1e-4, against the
     same integral to 1 - 1e-4: |discrete/continuous - 1| <= 2% at s = 0.01, <= 0.3% at s = 0.001, all h.
                                                                                       Predict: confirmed.
  D3 Haldane's arithmetic: 300 = D / I with D = 30, I = 0.1 (exact); D = 30 corresponds to p0 = e^{-15} =
     3.06e-7 (h = 1/2) or 9.4e-14 (h = 0); a single new copy in N_e = 1e4 (p0 = 1/(2N)) gives
     D = 2 ln(2e4) = 19.8, i.e. 198 generations at I = 0.1.  Day-side: 300 follows from Haldane's own inputs
     (holds); critic side: D depends on p0 and dominance.  Both statements predicted true.   Predict: proved.
E. Day's quoted closed-form arithmetic (verbatim quotes in docs/research/sources/quotes-day.md, Q-ids below),
  recomputed in exact rationals (fractions) or mpmath (dps 50):
  Q01 37.5 min/generation = 0.000071347 y (365-day year)                 predict holds
  Q03 9,000,000/20 = 450,000; /1,600 = 281.25 vs table "125"; Q04 "562" = 2 x 281   predict discrepancy (125)
  Q09 325,000 x 0.45 = 146,250; /1,600 = 91.4 -> "91"; 20,000,000/91 = 219,780     predict holds
  Q11 0.02^20,000,000 = 10^-33,979,400 ("~10^-34,000,000")                        predict holds
  Q12 6-7 My / 20 y = 300,000-350,000                                             predict holds
  Q14 205e6 / (252,000/1,322) = 1,075,437 ("1,075,000-fold")                      predict holds
  Q17 17.5e6/191 = 91,623 ("91,600x"); 252,000/105 = 2,400 vs "2,407"; 17.5e6/2,407 = 7,271  predict holds/slip
  Q18 6.3e6/25 = 252,000                                                          predict holds
  Q19 252,000/27,600 = 9.13 vs "8" (A5e)                                          predict slip/discrepancy (12%)
  Q30 exp(-pi^2 x 1.8e7) = 10^-77.15M with the printed 1.8e7; 10^-78.2M with 7.3e9/400   predict holds on
      the unrounded input, ~1% low on the printed input (ledger level)
  Q40 6.091/8.2 = 0.7428 ("0.743")                                                predict holds
  Q44 (2/0.001) ln(20,000) = 19,807 ("~19,800")                                   predict holds
  Q48 146,250/300 = 487.5 ("487"); Q49 9e6/25/300 = 1,200                         predict holds
  Q51 2 x 321,444 = 642,888; 642,888/146,250 = 4.396 ("4.4"); x 20e6 = 87,916,307.7 ("87,916,307")  predict holds
  Q58 60,000/45.4 = 1,321.6 ("1,322"); Q62 60,000/66 = 909.1 ("909"); Q85 60,000/37.8 = 1,587.3 ("1,587")
      [37.8 is the audit's derived average of Z23105291's 66, 73, 14, 9, 27]      predict holds
  Q91 252,000/1,400 = 180; 180/205e6 = 0.0000878% ("0.000088%"); 205e6/180 = 1,138,889 ("1,139,000")  predict holds
  Q118 7e9 x 0.0857 = 599,900,000                                                 predict holds (product only)
  Hard Limits (Q29, Q32; B2b): N_e = (4N-2)/(V_k+2) gives N_e = N at the WF value V_k = 2(1 - 1/N) (sympy);
      solving 4 N_e = G exactly gives N = (V_k+2) G/16 + 1/2, so Day's X drops a 1/2 (immaterial);
      X(6.5 My, 25 y, V_k 5) = 113,750 ("114,000"); X(2 My, 25 y, 5) = 35,000; X(2 My, 22 y, 3) = 28,409
      ("28,000").                                                                     predict proved / holds
  B2a exponent (Q30, Q31): in y = arccos(1 - 2p) the neutral diffusion has constant variance 1/(2N) per
      generation and the path 0 -> 1 has length pi, so the Varadhan short-time exponent is
      -pi^2 / (2 * G/(2N)) = -pi^2 N/G: Day's exponent (sympy for the transform; Varadhan's theorem is cited,
      not machine-proved; the prefactor is not proved).                               predict proved (transform)

Who is predicted to be helped: blocks A-C are textbook identities both sides now accept in words (Day concedes
1/(2N) on 2026-08-27 and uses 4N_e); they are predicted to hold, which credits the critics' k = mu and P_fix =
1/(2N) and Day's empty-start formula, his -pi^2 exponent and his 4N_e timescale.  Block D is predicted to
credit Day's 300 as Haldane's arithmetic while showing D is an input, not a constant.  Block E predicts most of
Day's printed arithmetic holds; the known slips (Q03 table, Q19) are recorded as such.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import sys
import json
import math
import time
import resource
from fractions import Fraction as Fr

import numpy as np
import scipy
from scipy.linalg import solve_banded
from scipy.stats import binom, betabinom
import sympy as sp
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "results", "raw")
RESULTS = []
T0 = time.time()


def rss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def record(iid, block, desc, status, prediction, met, **detail):
    r = dict(id=iid, block=block, desc=desc, status=status, prediction=prediction, prediction_met=bool(met),
             **detail)
    RESULTS.append(r)
    print(f"[{iid}] {status.upper():10s} pred_met={bool(met)}  {desc}", flush=True)
    for k, v in detail.items():
        print(f"      {k}: {v}", flush=True)
    return r


def is_zero(expr):
    e = sp.simplify(expr)
    if e == 0:
        return True
    e = sp.simplify(sp.expand(sp.powsimp(sp.expand_log(e, force=True), force=True)))
    return e == 0


# ------------------------------------------------------------------------------------------------------
# Exact Wright-Fisher chains, banded float64
# ------------------------------------------------------------------------------------------------------
def wf_banded(M, pnext, ksd=15.0, pad=30):
    """Banded I - P_TT on transient states 1..M-1, plus P(i -> M).  pnext(i) = post-selection frequency.
    Returns (l, u, ab, to_M, max_truncated_mass)."""
    n = M - 1

    def window(i):
        p = pnext(i)
        mean, sd = M * p, math.sqrt(M * p * (1 - p))
        lo = max(0, int(math.floor(mean - ksd * sd - pad)))
        hi = min(M, int(math.ceil(mean + ksd * sd + pad)))
        return p, lo, hi

    l = u = 0
    for i in range(1, M):                      # pass 1: bandwidth only (keeps RAM low at M = 2e4)
        _, lo, hi = window(i)
        jl, jh = max(lo, 1), min(hi, M - 1)
        if jl <= jh:
            l = max(l, i - jl)
            u = max(u, jh - i)
    ab = np.zeros((l + u + 1, n))
    to_M = np.zeros(n)
    trunc = 0.0
    for i in range(1, M):                      # pass 2: fill
        p, lo, hi = window(i)
        j = np.arange(lo, hi + 1)
        pm = binom.pmf(j, M, p)
        trunc = max(trunc, abs(1.0 - pm.sum()))
        r = i - 1
        ab[u, r] += 1.0
        mask = (j >= 1) & (j <= M - 1)
        c = j[mask] - 1
        ab[u + r - c, c] -= pm[mask]
        if j[-1] == M:
            to_M[r] = pm[-1]
    return l, u, ab, to_M, trunc


def wf_fix_and_condtime(M, pnext, need_time=True):
    l, u, ab, to_M, trunc = wf_banded(M, pnext)
    h = solve_banded((l, u), ab, to_M)         # overwrite_ab=False by default
    out = dict(h=h, trunc=trunc, band=(l, u))
    if need_time:
        w = solve_banded((l, u), ab, h)          # w = u_T + P_TT w with u_T = h (fix prob)
        out["tstar"] = w / h
    del ab
    return out


def neutral_next(M):
    return lambda i: i / M


def additive_next(M, s):
    def f(i):
        p = i / M
        q = 1 - p
        return (p * p * (1 + 2 * s) + p * q * (1 + s)) / (1 + 2 * p * s)
    return f


# ------------------------------------------------------------------------------------------------------
# Block A
# ------------------------------------------------------------------------------------------------------
def block_A():
    N, mu = sp.symbols("N mu", positive=True)
    hap = sp.simplify(N * mu * (1 / N) - mu)
    dip = sp.simplify(2 * N * mu * (1 / (2 * N)) - mu)
    ok = hap == 0 and dip == 0
    record("A1", "A", "neutral k = mu: haploid N mu * 1/N and diploid 2N mu * 1/(2N)", "proved" if ok else "failed",
           "proved", ok, haploid_minus_mu=str(hap), diploid_minus_mu=str(dip))

    # A2 (i) binomial mean symbolic
    p = sp.symbols("p", positive=True)
    # binomial mean E[X'] = M p as a polynomial identity in p, for each M = 1..40 (general M is the textbook
    # binomial mean; the martingale argument then gives P_fix = p0 by optional stopping)
    mean_ok = all(sp.expand(sum(k * sp.binomial(m, k) * p ** k * (1 - p) ** (m - k) for k in range(m + 1)) - m * p) == 0
                  for m in range(1, 41))
    how = "polynomial identity in p for each M = 1..40"
    # A2 (ii) exact rational WF chain M = 10
    M = 10
    P = sp.zeros(M - 1, M - 1)
    b = sp.zeros(M - 1, 1)
    for i in range(1, M):
        pi = sp.Rational(i, M)
        for jj in range(0, M + 1):
            pr = sp.binomial(M, jj) * pi ** jj * (1 - pi) ** (M - jj)
            if 1 <= jj <= M - 1:
                P[i - 1, jj - 1] = pr
            elif jj == M:
                b[i - 1] = pr
    h = (sp.eye(M - 1) - P).LUsolve(b)
    exact_ok = all(sp.simplify(h[i - 1] - sp.Rational(i, M)) == 0 for i in range(1, M))
    # A2 (iii) banded float
    devs = {}
    for Nn in (50, 500, 10000):
        Mm = 2 * Nn
        res = wf_fix_and_condtime(Mm, neutral_next(Mm), need_time=False)
        devs[Nn] = float(np.max(np.abs(res["h"] - np.arange(1, Mm) / Mm)))
    num_ok = all(v <= 1e-9 for v in devs.values())
    st = "proved" if (mean_ok and exact_ok and num_ok) else "failed"
    record("A2", "A", "neutral P_fix = initial frequency i/M (martingale; exact WF chains)", st,
           "proved / confirmed", mean_ok and exact_ok and num_ok, binomial_mean=how, mean_ok=mean_ok,
           exact_rational_M10=exact_ok, banded_max_dev={str(k): v for k, v in devs.items()}, rss_mb=rss_mb())

    # A3 Dirichlet-multinomial Cannings
    Ms, isym, al = sp.symbols("M i alpha", positive=True)
    # beta-binomial(M, i alpha, (M-i) alpha) has mean M a/(a+b) = i: the count is a martingale
    bb_mean_ok = sp.simplify(Ms * (isym * al) / (isym * al + (Ms - isym) * al) - isym) == 0
    M = 100
    rows = []
    allok = True
    for alpha in (0.25, 1.0):
        Pm = np.zeros((M + 1, M + 1))
        for i in range(1, M):
            Pm[i] = betabinom.pmf(np.arange(M + 1), M, i * alpha, (M - i) * alpha)
        Pm[0, 0] = Pm[M, M] = 1.0
        mean_err = max(abs(float(np.arange(M + 1) @ Pm[i]) - i) for i in range(1, M))
        A = np.eye(M - 1) - Pm[1:M, 1:M]
        hfix = np.linalg.solve(A, Pm[1:M, M])
        w = np.linalg.solve(A, hfix)
        tstar = w[0] / hfix[0]
        Me = (M * alpha + 1) / (alpha + 1)
        pp = 1.0 / M
        diff = -2 * Me * (1 - pp) * math.log1p(-pp) / pp
        # WF same M (haploid M copies): exact
        wf = wf_fix_and_condtime(M, neutral_next(M))
        ratio = tstar / diff
        ok = abs(hfix[0] - 1 / M) <= 1e-10 and abs(ratio - 1) <= 0.15
        allok &= ok
        rows.append(dict(alpha=alpha, M_e=Me, Pfix_1=float(hfix[0]), one_over_M=1 / M, one_over_Me=1 / Me,
                         beta_binomial_mean_max_err=mean_err, tstar_gens=float(tstar), diffusion_Me=diff,
                         ratio_to_diffusion=ratio, tstar_WF_sameM=float(wf["tstar"][0]),
                         ratio_DM_over_WF=float(tstar / wf["tstar"][0]), Me_over_M=Me / M))
    record("A3", "A", "P_fix independent of N_e in an exchangeable low-N_e Cannings chain; time scales with N_e",
           "confirmed" if allok and bb_mean_ok else "failed", "confirmed (1/M, not 1/M_e)", allok, rows=rows)

    # A4 start state.  Geometric fixation-age family: P(tau <= t) = F(t) = 1 - q^t, q = 1/(1+x), x > 0.
    x = sp.symbols("x", positive=True)
    t, T = sp.symbols("t T", nonnegative=True, integer=True)
    qx = 1 / (1 + x)
    F = lambda tt: 1 - qx ** tt
    pmf_ok = is_zero((F(t) - F(t - 1)) - (1 - qx) * qx ** (t - 1))
    S = lambda TT: TT - (1 - qx ** TT) / (1 - qx)          # claimed closed form of sum_{t<T} F(t) = E K(T)/mu
    induct_ok = is_zero(S(T + 1) - S(T) - F(T)) and sp.simplify(S(0)) == 0
    deficit = T - S(T)                                     # (mu T - E K(T)) / mu
    qT = sp.exp(-T * sp.log(1 + x))                        # = q^T, written so sympy sees the decay
    def_closed_ok = is_zero(deficit - (1 - qx ** T) / (1 - qx))
    lim_def = sp.limit((1 - qT) / (1 - qx), T, sp.oo)
    Etau_geo = 1 / (1 - qx)                                # mean of the geometric(1-q) on {1,2,...}
    stat_lim = sp.limit(1 - qT, T, sp.oo)                  # sum_{a<=T} f_a = F(T) -> 1: stationary rate mu * 1
    geo_ok = pmf_ok and def_closed_ok and is_zero(lim_def - Etau_geo) and stat_lim == 1
    lim_ok = induct_ok
    # exact WF M = 20 with mpmath
    mp.mp.dps = 40
    M = 20
    Pm = mp.matrix(M + 1, M + 1)
    for i in range(M + 1):
        pi = mp.mpf(i) / M
        for jj in range(M + 1):
            Pm[i, jj] = mp.binomial(M, jj) * pi ** jj * (1 - pi) ** (M - jj)
    # conditional fixation-age distribution from 1 copy: P(X_t = M | X_0 = 1) / (1/M)
    v = mp.matrix(1, M + 1)
    v[0, 1] = 1
    cdf = [mp.mpf(0)]
    Tmax = 0
    # E[tau] exactly from the linear system
    A = mp.matrix(M - 1, M - 1)
    for i in range(1, M):
        for jj in range(1, M):
            A[i - 1, jj - 1] = (1 if i == jj else 0) - Pm[i, jj]
    hv = mp.matrix([mp.mpf(i) / M for i in range(1, M)])
    w = mp.lu_solve(A, hv)
    Etau_ex = w[0] / hv[0]
    Tmax = int(30 * float(Etau_ex))
    surv_sum = mp.mpf(0)
    for tt in range(Tmax):
        cond_cdf = v[0, M] * M                      # P(tau <= tt | fix)
        surv_sum += 1 - cond_cdf                    # sum_{t<T} P(tau > t)
        v = v * Pm
    tail = 1 - v[0, M] * M
    defic_ratio = surv_sum / Etau_ex                # deficit / (mu E[tau])
    stat_sum = 1 - tail                             # sum_{a <= Tmax} f_a
    ex_ok = abs(defic_ratio - 1) <= mp.mpf("1e-12") and abs(stat_sum - 1) <= mp.mpf("1e-12")
    st = "proved" if (geo_ok and lim_ok and ex_ok) else ("confirmed" if ex_ok else "failed")
    record("A4", "A", "start state: stationary past gives k = mu exactly; empty start gives deficit -> mu E[tau]",
           st, "proved / confirmed", geo_ok and lim_ok and ex_ok, geometric_limits_ok=geo_ok, closed_form_by_induction=lim_ok,
           WF_M20_Etau_cond=float(Etau_ex), Etau_over_N=float(Etau_ex) / 10, T_used=Tmax,
           deficit_over_muEtau_minus_1=mp.nstr(defic_ratio - 1, 5), stationary_sum_minus_1=mp.nstr(stat_sum - 1, 5))


# ------------------------------------------------------------------------------------------------------
# Block B
# ------------------------------------------------------------------------------------------------------
def block_B():
    p, s, N = sp.symbols("p s N", positive=True)
    u = (1 - sp.exp(-4 * N * s * p)) / (1 - sp.exp(-4 * N * s))
    V = p * (1 - p) / (2 * N)
    Mdrift = s * p * (1 - p)
    ode = sp.simplify(V / 2 * sp.diff(u, p, 2) + Mdrift * sp.diff(u, p))
    bc = (sp.simplify(u.subs(p, 0)), sp.simplify(u.subs(p, 1)))
    ok = ode == 0 and bc == (0, 1)
    record("B1", "B", "Kimura u(p) solves the backward equation with u(0)=0, u(1)=1", "proved" if ok else "failed",
           "proved", ok, residual=str(ode), boundary=str(bc))

    lim0 = sp.limit(u, s, 0)
    u1 = u.subs(p, 1 / (2 * N))
    limN = sp.limit(u1, N, sp.oo)
    ser = sp.series(limN, s, 0, 3).removeO()
    ok = sp.simplify(lim0 - p) == 0 and sp.simplify(limN - (1 - sp.exp(-2 * s))) == 0 and \
        sp.simplify(ser - (2 * s - 2 * s ** 2)) == 0
    record("B2", "B", "Kimura limits: s->0 gives p; N->inf at p=1/(2N) gives 1-e^{-2s} = 2s - 2s^2 + ...",
           "proved" if ok else "failed", "proved", ok, lim_s0=str(lim0), lim_Ninf=str(limN), series=str(ser))

    # B3 exact diploid additive WF vs Kimura
    rows = []
    allok = True
    for Nn, ss in ((100, 0.01), (500, 0.01), (1000, 0.005), (10000, 0.001), (50, 0.05)):
        M = 2 * Nn
        t1 = time.time()
        res = wf_fix_and_condtime(M, additive_next(M, ss), need_time=False)
        ex = float(res["h"][0])
        kim = -math.expm1(-2 * ss) / -math.expm1(-4 * Nn * ss)
        ratio = ex / kim
        tol = 0.02 if ss <= 0.01 else 0.05
        ok = abs(ratio - 1) <= tol
        allok &= ok
        rows.append(dict(N=Nn, s=ss, twoNs=2 * Nn * ss, exact=ex, kimura=kim, ratio=ratio, ratio_to_2s=ex / (2 * ss),
                         tol=tol, ok=ok, trunc_mass=res["trunc"], band=res["band"], sec=round(time.time() - t1, 1),
                         rss_mb=round(rss_mb())))
        print("   B3 row", rows[-1], flush=True)
    # code check at N=10 with mpmath dense
    mp.mp.dps = 40
    Nn, ss = 10, mp.mpf("0.01")
    M = 2 * Nn
    A = mp.matrix(M - 1, M - 1)
    bvec = mp.matrix(M - 1, 1)
    for i in range(1, M):
        pp = mp.mpf(i) / M
        pn = (pp * pp * (1 + 2 * ss) + pp * (1 - pp) * (1 + ss)) / (1 + 2 * pp * ss)
        for jj in range(M + 1):
            pr = mp.binomial(M, jj) * pn ** jj * (1 - pn) ** (M - jj)
            if 1 <= jj <= M - 1:
                A[i - 1, jj - 1] = (1 if i == jj else 0) - pr
            elif jj == M:
                bvec[i - 1] = pr
    hmp = mp.lu_solve(A, bvec)[0]
    hfl = float(wf_fix_and_condtime(M, additive_next(M, 0.01), need_time=False)["h"][0])
    code_ok = abs(float(hmp) - hfl) <= 1e-11
    record("B3", "B", "exact diploid additive WF P_fix vs Kimura at the audit's parameters",
           "confirmed" if (allok and code_ok) else "failed", "|ratio-1| <= 2% (s<=0.01), <= 5% (s=0.05)",
           allok and code_ok, rows=rows, mp_vs_float_N10=dict(mp=mp.nstr(hmp, 20), fl=hfl, ok=code_ok))

    r, i, Mx = sp.symbols("r i M", positive=True)
    h = lambda k: (1 - r ** (-k)) / (1 - r ** (-Mx))
    res = sp.simplify((1 + r) * h(i) - r * h(i + 1) - h(i - 1))
    bc = (sp.simplify(h(0)), sp.simplify(h(Mx)))
    # limit M -> oo of h_1 for r > 1: r^{-M} -> 0
    rr = sp.Symbol("rr", positive=True)
    lim_chk = sp.limit((1 - 1 / (1 + rr)) / (1 - (1 + rr) ** (-Mx)), Mx, sp.oo)
    ok = res == 0 and bc == (0, 1) and sp.simplify(lim_chk - (1 - 1 / (1 + rr))) == 0
    record("B4", "B", "Moran fixation probability (1 - r^-i)/(1 - r^-M) solves the chain; M->inf gives 1 - 1/r",
           "proved" if ok else "failed", "proved", ok, residual=str(res), boundary=str(bc), limit=str(lim_chk))


# ------------------------------------------------------------------------------------------------------
# Block C
# ------------------------------------------------------------------------------------------------------
def block_C():
    p, N = sp.symbols("p N", positive=True)
    t = -4 * N * (1 - p) * sp.log(1 - p) / p
    V = p * (1 - p) / (2 * N)
    Mstar = V * 1 / p                     # V u'/u with u = p
    res = sp.simplify(V / 2 * sp.diff(t, p, 2) + Mstar * sp.diff(t, p) + 1)
    lim0 = sp.limit(t, p, 0)
    lim1 = sp.limit(t, p, 1)
    ok = res == 0 and sp.simplify(lim0 - 4 * N) == 0 and lim1 == 0
    record("C1", "C", "diffusion conditional neutral fixation time -4N(1-p)ln(1-p)/p; -> 4N as p -> 0",
           "proved" if ok else "failed", "proved", ok, residual=str(res), limit_p0=str(lim0), limit_p1=str(lim1))

    rows = []
    allok = True
    prev = None
    for Nn in (10, 25, 50, 100, 200, 500, 10000):
        M = 2 * Nn
        t1 = time.time()
        res_ = wf_fix_and_condtime(M, neutral_next(M))
        ex = float(res_["tstar"][0])
        pp = 1 / M
        diff = -4 * Nn * (1 - pp) * math.log1p(-pp) / pp
        ratio = ex / diff
        if Nn == 10:
            ok = 0.94 <= ratio <= 1.0
        elif Nn >= 50:
            ok = abs(ratio - 1) <= 0.015
        else:
            ok = ratio <= 1.0
        if prev is not None:
            ok = ok and abs(ratio - 1) <= abs(prev - 1) + 1e-9
        prev = ratio
        allok &= ok
        rows.append(dict(N=Nn, exact_gens=ex, exact_over_N=ex / Nn, diffusion=diff, ratio=ratio, ok=ok,
                         sec=round(time.time() - t1, 1), rss_mb=round(rss_mb())))
        print("   C2 row", rows[-1], flush=True)
    record("C2", "C", "exact WF conditional neutral fixation time vs diffusion 4N", "confirmed" if allok else "failed",
           "ratio in [0.94,1] at N=10; within 1.5% for N>=50; deviation shrinking", allok, rows=rows)

    rows = []
    allok = True
    for M in (5, 10, 20, 50, 100):
        up = [Fr(i * (M - i), M * M) for i in range(M + 1)]
        uu = [Fr(i, M) for i in range(M + 1)]
        # (up_i + dn_i) w_i - up_i w_{i+1} - dn_i w_{i-1} = u_i,  w_0 = w_M = 0 ; up_i = dn_i
        n = M - 1
        a_ = [-up[i] for i in range(1, M)]        # sub
        b_ = [2 * up[i] for i in range(1, M)]     # diag
        c_ = [-up[i] for i in range(1, M)]        # super
        d_ = [uu[i] for i in range(1, M)]
        for k in range(1, n):
            m_ = a_[k] / b_[k - 1]
            b_[k] -= m_ * c_[k - 1]
            d_[k] -= m_ * d_[k - 1]
        w = [Fr(0)] * n
        w[-1] = d_[-1] / b_[-1]
        for k in range(n - 2, -1, -1):
            w[k] = (d_[k] - c_[k] * w[k + 1]) / b_[k]
        tstar = w[0] / uu[1]
        ok = tstar == M * (M - 1)
        allok &= ok
        diff = -M * M * (1 - 1 / M) * math.log1p(-1 / M)
        rows.append(dict(M=M, tstar_events=str(tstar), equals_M_Mminus1=ok, gens=float(tstar) / M, diffusion_gens=diff))
    record("C3", "C", "exact Moran conditional neutral fixation time = M(M-1) events = M-1 generations",
           "proved" if allok else "failed", "proved for M = 5..100", allok, rows=rows)


# ------------------------------------------------------------------------------------------------------
# Block D: Haldane
# ------------------------------------------------------------------------------------------------------
def haldane_discrete(p0, s, h, qend):
    p = p0
    D = 0.0
    c = 0.0                                     # Kahan
    gens = 0
    wAA, wAa, waa = 1.0, 1.0 - h * s, 1.0 - s
    while 1.0 - p > qend:
        q = 1.0 - p
        wbar = p * p * wAA + 2 * p * q * wAa + q * q * waa
        y = (1.0 - wbar) - c
        tt = D + y
        c = (tt - D) - y
        D = tt
        p = (p * p * wAA + p * q * wAa) / wbar
        gens += 1
        if gens > 5e7:
            break
    return D, gens


def block_D():
    p, p0, hh = sp.symbols("p p0 h", positive=True)
    q = 1 - p
    integrand = (2 * p * hh + q) / (p * (p * hh + q * (1 - hh)))
    exp_ = {0: sp.log(1 / p0), sp.Rational(1, 2): 2 * sp.log(1 / p0), 1: 1 / p0 - 1 + sp.log(1 / p0)}
    got = {}
    ok = True
    for hv, want in exp_.items():
        D = sp.integrate(sp.simplify(integrand.subs(hh, hv)), (p, p0, 1))
        got[str(hv)] = str(sp.simplify(D))
        ok &= is_zero(D - want)
    record("D1", "D", "Haldane cost D (continuous): dominant ln(1/p0), semidominant 2 ln(1/p0), recessive 1/p0-1+ln(1/p0)",
           "proved" if ok else "failed", "proved", ok, integrals=got,
           definition="D = sum (1 - wbar/w_max); AA=1, Aa=1-hs, aa=1-s; Haldane 1957 primary NOT retrieved")

    rows = []
    allok = True
    p0v, qend = 1e-3, 1e-4
    for hv in (0.0, 0.5, 1.0):
        Dc = float(sp.integrate(sp.simplify(integrand.subs(hh, sp.nsimplify(hv))), (p, sp.Float(p0v, 30), 1 - sp.Float(qend, 30))))
        for ss in (0.01, 0.001):
            t1 = time.time()
            Dd, g = haldane_discrete(p0v, ss, hv, qend)
            ratio = Dd / Dc
            tol = 0.02 if ss == 0.01 else 0.003
            ok = abs(ratio - 1) <= tol
            allok &= ok
            rows.append(dict(h=hv, s=ss, D_discrete=Dd, D_continuous=Dc, ratio=ratio, tol=tol, ok=ok, generations=g,
                             sec=round(time.time() - t1, 1)))
            print("   D2 row", rows[-1], flush=True)
    record("D2", "D", "discrete genotype recursion matches the continuous Haldane integral to O(s)",
           "confirmed" if allok else "failed", "<= 2% at s=0.01, <= 0.3% at s=0.001", allok, rows=rows)

    D30 = Fr(30)
    I = Fr(1, 10)
    gens = D30 / I
    p0_semi = math.exp(-15)
    p0_dom = math.exp(-30)
    D_single = 2 * math.log(2e4)
    ok = gens == 300 and abs(p0_semi - 3.06e-7) / 3.06e-7 < 0.01 and abs(p0_dom - 9.36e-14) / 9.36e-14 < 0.01 \
        and abs(D_single - 19.81) < 0.01
    record("D3", "D", "Haldane arithmetic: 300 = 30/0.1; D=30 <-> p0 = e^-15 (h=1/2); single copy at N_e=1e4: D=19.8",
           "proved" if ok else "failed", "proved", ok, gens_per_sub=str(gens), p0_for_D30_semidominant=p0_semi,
           p0_for_D30_dominant=p0_dom, D_single_copy_Ne1e4_semidominant=D_single,
           gens_at_I_0p1=D_single / 0.1)


# ------------------------------------------------------------------------------------------------------
# Block E: Day's arithmetic
# ------------------------------------------------------------------------------------------------------
def classify(exact, printed, tol=0.005, slip_tol=0.25):
    rel = float(printed) / float(exact) - 1.0
    if abs(rel) <= tol:
        return "holds", rel
    if abs(rel) <= slip_tol:
        return "slip", rel
    return "discrepancy", rel


def block_E():
    rows = []

    def add(qid, what, exact, printed, predicted, tol=0.005):
        lab, rel = classify(exact, printed, tol)
        rows.append(dict(q=qid, what=what, exact=float(exact), printed=float(printed), rel_dev=rel, label=lab,
                         predicted=predicted, met=(lab == predicted)))
        print(f"   E {qid:5s} {lab:11s} (pred {predicted:11s}) exact={float(exact):.8g} printed={float(printed):.8g}"
              f" rel={rel:+.4%}  {what}", flush=True)

    add("Q01", "37.5 min in years (365-d year)", Fr(375, 10) / (60 * 24 * 365), Fr("0.000071347"), "holds")
    add("Q03", "9e6/20/1600 vs table 125", Fr(9_000_000, 20) / 1600, 125, "discrepancy")
    add("Q04", "2 x 450,000/1,600 vs 562", 2 * Fr(450_000, 1600), 562, "holds")
    add("Q09", "325,000 x 0.45", Fr(325_000) * Fr(45, 100), 146_250, "holds")
    add("Q09", "146,250/1,600 vs 91", Fr(146_250, 1600), 91, "holds", tol=0.005)
    add("Q09", "20e6/91 vs 219,780", Fr(20_000_000, 91), 219_780, "holds")
    mp.mp.dps = 50
    l10 = 20_000_000 * mp.log10(mp.mpf("0.02"))
    add("Q11", "log10(0.02^2e7) vs -34,000,000", l10, -34_000_000, "holds")
    add("Q12", "6e6/20 and 7e6/20", Fr(6_000_000, 20), 300_000, "holds")
    add("Q14", "205e6/(252,000/1,322) vs 1,075,000", Fr(205_000_000) / Fr(252_000, 1322), 1_075_000, "holds")
    add("Q17", "17.5e6/191 vs 91,600", Fr(17_500_000, 191), 91_600, "holds")
    add("Q17", "252,000/105 vs 2,407", Fr(252_000, 105), 2_407, "holds")
    add("Q17", "17.5e6/2,407 vs 7,271", Fr(17_500_000, 2407), 7_271, "holds")
    add("Q18", "6.3e6/25", Fr(6_300_000, 25), 252_000, "holds")
    add("Q19", "252,000/27,600 vs 8", Fr(252_000, 27_600), 8, "slip")
    dec_printed = mp.pi ** 2 * mp.mpf("1.8e7") / mp.log(10)
    dec_unround = mp.pi ** 2 * (mp.mpf("7.3e9") / 400) / mp.log(10)
    add("Q30", "pi^2 x 1.8e7 / ln10 decades vs 78e6", dec_printed, 78_000_000, "slip")
    add("Q30", "pi^2 x (7.3e9/400) / ln10 decades vs 78e6", dec_unround, 78_000_000, "holds")
    add("Q40", "6.091/8.2 vs 0.743", Fr(6091, 8200), Fr(743, 1000), "holds")
    add("Q44", "(2/0.001) ln(20,000) vs 19,800", 2000 * mp.log(20000), 19_800, "holds")
    add("Q48", "146,250/300 vs 487", Fr(146_250, 300), 487, "holds")
    add("Q49", "9e6/25/300 vs 1,200", Fr(9_000_000, 25 * 300), 1_200, "holds")
    add("Q51", "2 x 321,444 vs 642,888", 2 * 321_444, 642_888, "holds")
    add("Q51", "642,888/146,250 vs 4.4", Fr(642_888, 146_250), Fr(44, 10), "holds", tol=0.01)
    add("Q51", "642,888/146,250 x 20e6 vs 87,916,307", Fr(642_888, 146_250) * 20_000_000, 87_916_307, "holds")
    add("Q58", "60,000/45.4 vs 1,322", Fr(60_000) / Fr(454, 10), 1_322, "holds")
    add("Q62", "60,000/66 vs 909", Fr(60_000, 66), 909, "holds")
    add("Q85", "60,000/37.8 vs 1,587 (37.8 = mean of 66,73,14,9,27)", Fr(60_000) / (Fr(66 + 73 + 14 + 9 + 27, 5)), 1_587, "holds")
    add("Q91", "252,000/1,400 vs 180", Fr(252_000, 1400), 180, "holds")
    add("Q91", "180/205e6 in % vs 0.000088", Fr(180, 205_000_000) * 100, Fr(88, 1_000_000), "holds", tol=0.005)
    add("Q91", "205e6/180 vs 1,139,000", Fr(205_000_000, 180), 1_139_000, "holds")
    add("Q118", "7e9 x 0.0857 vs 599,900,000", Fr(7_000_000_000) * Fr(857, 10_000), 599_900_000, "holds")
    # Hard Limits
    Nn, Vk, G = sp.symbols("N V_k G", positive=True)
    Ne = (4 * Nn - 2) / (Vk + 2)
    wf_ok = sp.simplify(Ne.subs(Vk, 2 * (1 - 1 / Nn)) - Nn) == 0
    sol = sp.solve(sp.Eq(4 * Ne, G), Nn)
    xform = sp.simplify(sol[0] - ((Vk + 2) * G / 16 + sp.Rational(1, 2))) == 0
    for what, Tmy, g, vk, printed in (("X human lineage", Fr(65, 10), 25, 5, 114_000),
                                      ("X human species", 2, 25, 5, 35_000), ("X elephant", 2, 22, 3, 28_000)):
        Gv = Fr(Tmy) * 1_000_000 / g
        add("Q33", f"{what}: (V_k+2) G/16", (vk + 2) * Gv / 16, printed, "holds", tol=0.02)
    y = sp.acos(1 - 2 * sp.Symbol("p", positive=True))
    pv = sp.Symbol("p", positive=True)
    var_y = sp.simplify(sp.diff(y, pv) ** 2 * pv * (1 - pv) / (2 * Nn))
    path = sp.simplify(y.subs(pv, 1) - y.subs(pv, 0))
    expo = sp.simplify(-path ** 2 / (2 * sp.Symbol("G", positive=True) * var_y))
    tr_ok = sp.simplify(var_y - 1 / (2 * Nn)) == 0 and sp.simplify(path - sp.pi) == 0
    nrows = len(rows)
    n_met = sum(r["met"] for r in rows)
    record("E", "E", "Day's quoted closed-form arithmetic, recomputed exactly",
           "confirmed" if n_met == nrows else "prediction-miss", "labels as listed in the docstring", n_met == nrows,
           rows=rows, n_rows=nrows, n_predictions_met=n_met)
    record("E-HL", "E", "Hard Limits: N_e(WF V_k) = N; 4N_e = G gives N = (V_k+2)G/16 + 1/2",
           "proved" if (wf_ok and xform) else "failed", "proved", wf_ok and xform, wf_Ne_equals_N=wf_ok,
           solve_4Ne_eq_G=str(sol), X_drops_half=xform)
    record("E-B2a", "E", "arcsine transform: constant variance 1/(2N), path length pi -> exponent -pi^2 N/G",
           "proved" if tr_ok else "failed", "proved (transform; Varadhan cited, prefactor not proved)", tr_ok,
           var_y=str(var_y), path=str(path), exponent=str(expo))


if __name__ == "__main__":
    os.makedirs(RAW, exist_ok=True)
    print(f"P1 start {time.strftime('%Y-%m-%dT%H:%M:%S%z')} python {sys.version.split()[0]} sympy {sp.__version__} "
          f"mpmath {mp.__version__} numpy {np.__version__} scipy {scipy.__version__}", flush=True)
    for name, fn in (("A", block_A), ("B", block_B), ("C", block_C), ("D", block_D), ("E", block_E)):
        t1 = time.time()
        try:
            fn()
        except Exception as exc:                  # record, do not hide
            import traceback
            traceback.print_exc()
            record(f"{name}-ERROR", name, f"block {name} raised {type(exc).__name__}: {exc}", "failed", "-", False)
        print(f"== block {name} done in {time.time() - t1:.1f} s; peak RSS {rss_mb():.0f} MB", flush=True)
    out = dict(script="p1_symbolic_proofs.py", wall_s=time.time() - T0, peak_rss_mb=rss_mb(), results=RESULTS)
    json.dump(out, open(os.path.join(RAW, "p1_symbolic_proofs.json"), "w"), indent=1, default=str)
    print("\nSUMMARY")
    for r in RESULTS:
        print(f"  {r['id']:7s} {r['status']:10s} pred_met={r['prediction_met']}  {r['desc']}")
    print(f"wall {time.time() - T0:.0f} s, peak RSS {rss_mb():.0f} MB")

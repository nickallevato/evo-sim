"""E / E3 -- founder-event CMMRD-equivalent hazard (Day & Athos Z23020792 s5.1; Z23034852 s3).

THROWAWAY research check.  Run:  research/.venv/bin/python -I research/checks/e_founder_hazard.py
(exact Markov chains + one seeded Monte Carlo replication; raw output -> research/checks/results/raw/e_founder_hazard.out)

CLAIMS (verbatim; sources/raw/day/*.txt are untrusted local copies, read only):
  Z23020792 s5.1: "Lynch syndrome carrier frequency in humans is estimated at roughly 1 in 280 (carrier frequency p
    ~ 0.0036 across the four major MMR genes combined, corresponding to a per-gene allele frequency q ~ 0.002). In a
    founder population of N = 100 diploid individuals ... The probability of sampling at least two carriers -- the
    minimum required to produce a homozygous offspring -- is approximately 5-6% per founder event (from the binomial
    distribution with n = 100, p = 0.0036)."
  Z23020792 s5.1: "Conditional on a founder population containing two carriers among 100 individuals, the MMR-defect
    allele frequency is q ~ 0.01. ... q^2 ~ 10^-4. With approximately 100 offspring per generation over 50 generations
    ... 1 - e^-0.5 ~ 39%. This estimate is conservative: it does not account for the inbreeding ..."
  Z23020792 s5.1: "The compound probability ... is approximately 0.06 x 0.39 ~ 2.3% per founder event. This is a
    per-event risk. Whether it is evolutionarily consequential depends on how many founder events PE's model posits and
    whether the affected individuals survive long enough to affect population fitness, questions that warrant formal
    demographic modeling."
  Z23020792 s4.1: "CMMRD is extremely rare in large outbreeding human populations, approximately 1 in 1,000,000 births,
    because it requires homozygosity for a loss-of-function allele in a mismatch repair gene."
  Z23034852 s3.1 (model): "We draw 2N alleles ... q = 0.0018, corresponding to a combined Lynch syndrome carrier
    frequency of approximately 1 in 280 across the four major MMR genes ... Each allele is independently drawn as
    defective with probability q. The sampled alleles are paired into N diploid genotypes." / "For each generation from
    1 to G, genotype fitness is assigned: ... AA 1.0, Aa 1 - s_het, aa 1 - s_hom. Post-selection allele frequencies
    are computed from the genotype-frequency-weighted fitnesses. The next generation is produced by binomial sampling of
    2N alleles at the post-selection frequency ..., then pairing into N diploid offspring. Homozygous (aa) individuals
    are counted each generation."  s_hom = 0.95, s_het = 0.05.
  Z23034852 s3.2: "At N = 100 founders and G = 50 generations with full selection, the simulation produces P(>=1
    CMMRD-equivalent homozygote) = 2.33%".  Table 2 (G=50): N=50/100/200/500: P(hom) 1.6/2.3/3.5/6.0%, P(>=2 copies)
    1.4/5.1/16.1/52.8%, P(hom | >=2) 20.6/14.7/12.0/9.4%.  Table 3: N=100 G=50/100/200: 2.33/2.37/2.48%; N=500:
    5.95/5.68/5.96%.  Table 4 (N=100, G=50): full 2.33%; s_hom=0.95,s_het=0: 3.62%; pure drift 3.94%.  Table 5 (N=100,
    G=100): carrier 1/1000 0.63%, 1/500 1.42%, 1/280 2.27%, 1/200 3.23%, 1/100 6.87%, 1/50 14.2%.  Table 7: cumulative
    over 10/50/100 events 21.0/69.3/90.6%.  s4.2 Table 8 (G=200, "with selection", source frequency f_m):
    f_m=0.001: 1.2/1.6/2.4/3.5% at N=50/100/200/500; 0.005: 5.2/8.3/12.1/20.5; 0.010: 10.8/16.4/24.3/42.1;
    0.020: 21.8/33.2/48.7/74.6; 0.050: 50.8/71.8/89.6/99.4.

WHAT IS WHAT.  Arithmetic: binomial P(>=2 carriers), Poisson 1-e^-0.5, the product, cumulative 1-(1-h)^n.  Model
  result: P(>=1 aa in G generations) in the s3.1 WF model.  Empirical inferences: (i) that q = 0.0018 (a modern human
  4-gene pooled figure) is the allele frequency of ONE locus in an ancestral mammal source; (ii) that ">=1 aa birth"
  is a hazard to the peripatric mechanism (the paper itself defers this: "questions that warrant formal demographic
  modeling").

PARAMETERS.  Sourced (Day quote): carrier 1/280 -> q = 0.0018 pooled (Z23034852 s3.1); N_e 100-1,000 (Z23020792 s5:
  "N_e typically 100-1,000 for mammals"); G = 50 (s5.1), G window 200-10,000 generations (Z23020792 s5.3); s_hom 0.95,
  s_het 0.05 (Z23034852 s3.1); CMMRD incidence 1e-6 (Z23020792 s4.1).  ASSUMED (labelled): equal split of the pooled
  carrier frequency over the four genes (q/4 each); per-gene carrier frequencies MLH1 1/1946, MSH2 1/2841, MSH6 1/758,
  PMS2 1/714 recalled from memory as Win et al. 2017 (NOT retrieved, unverified; sensitivity only).

METHOD.  Exact chain on the newborn allele count j in 0..2N (generation t), with the aa count k | j given by random
  pairing of j copies into N diploids: P(k|j) = C(N,k) C(N-k, j-2k) 2^(j-2k) / C(2N, j)  (this is exactly "binomial
  sampling of 2N alleles ... then pairing").  Selection on REALIZED genotype counts (literal reading, mode 'real'):
  x = (h w_het/2 + k w_aa) / ((N-h-k) + h w_het + k w_aa), h = j - 2k; next j' ~ Bin(2N, x).  Alternative mode 'hwe':
  selection on Hardy-Weinberg EXPECTED genotype frequencies from q = j/2N (a common implementation; then s_hom acts
  before any aa exists).  "Event" E(j,k) is made absorbing: P(no E in generations g0..G) by forward propagation.
  Generation 0 (founders) counted or not (text ambiguous; difference ~N q^2 = 3e-4).  Cross-check: an independent
  'no-hit kernel' (state = number of hets given no aa so far) and a seeded MC of the literal s3.1 model.

PRE-REGISTERED PREDICTIONS (written before any run of this script; no timing run preceded them):
  P1 arithmetic: P(>=2 carriers | Bin(100, 0.0036)) = 0.0509; x (1 - e^-0.5) = 2.00%, not 2.3%; 2.3% needs 0.06.
  P2 exact chain, literal model (mode real), N=100, G=50, q=0.0018, full selection: P(>=1 aa) in [2.1, 2.6]%, i.e. the
     2.33% headline reproduces within Day's MC error (2 SE ~ 0.13 points at 50,000 reps).
  P3 in mode 'real', s_hom cannot change P(>=1 aa) (before the first aa there is no aa to select against), so Day's
     Table 4 rows "s_het = 0" (3.62%) and "pure drift" (3.94%) must be equal in the literal model; prediction: exact
     value ~3.9% for both.  If Day's 3.62 is outside MC error of the exact value, his code most likely selected on HWE
     expected genotype frequencies (mode 'hwe'), which should give ~3.6%.
  P4 decomposition (N=100, G=50, full): founders with exactly 1 copy contribute 55-75% of the hazard; the >=2-copy
     route ~1/3 (E3 derived 0.75 of 2.33 points).  Exact P(hom | exactly 2 founder copies, pure drift, G=50) is in
     15-30%, below Day's constant-q Poisson 39% (drift loses the allele more often than it raises q), so the analytic
     39% is NOT "conservative" in the direction claimed even though inbreeding raises E[q^2].
  P5 Table 2 (N=50/100/200/500) and Table 5 (carrier sweep, G=100) reproduce within ~2 MC SE; Table 3 full-selection
     G-insensitivity holds; pure drift rises with G (no saturation by 200; continues to G=10,000 as the allele is
     eventually lost or fixed: saturating near P(not lost) territory).
  P6 per-gene treatment (CMMRD needs two defective copies of the SAME gene): pooled q=0.0018 as one locus gives a
     population CMMRD incidence q^2 = 3.2e-6 (1 in 309,000), 3x Day's own "1 in 1,000,000"; an equal 4-gene split
     gives 8.1e-7 (1 in 1.2M), consistent with it.  Hazard under the split = 1 - prod(1 - H(q_g)) falls to 50-85% of
     the pooled value (not 25%), because the single-copy route is ~linear in q.
  P7 consequence (N=100, G=50, full selection, literal model): expected aa births per founder event 0.01-0.1 (of
     5,000 births); P(mean fitness < 0.95 in some generation) <= 0.5%; P(mean fitness < 0.5) < 1e-6.  So the
     ">=1 aa birth" hazard (Day's definition) exceeds any population-level failure probability by >= 1 order of magnitude.
  P8 Day-side: P(>=1 aa) rises with N and q (Tables 2, 5, 8 direction holds); over 100 independent events
     1 - (1 - 0.0233)^100 = 90.5% (arithmetic holds).
"""
import os
import sys
import time
import json
from math import comb, exp, log

import numpy as np
from scipy.special import gammaln
from scipy.stats import binom

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "results", "raw")
SEED_ROOT = 20261008

Q_POOLED = 0.0018           # Z23034852 s3.1 (allele frequency, 4 genes pooled)
CARRIER = 1 / 280           # Z23020792 s5.1
S_HOM, S_HET = 0.95, 0.05   # Z23034852 s3.1
WIN_MEMORY_CARRIERS = {"MLH1": 1 / 1946, "MSH2": 1 / 2841, "MSH6": 1 / 758, "PMS2": 1 / 714}  # MEMORY, unverified


def log_pk_given_j(N):
    """L[j, k] = log P(k aa | j copies randomly paired into N diploids); -inf where impossible."""
    L = np.full((2 * N + 1, N + 1), -np.inf)
    for j in range(2 * N + 1):
        kmin, kmax = max(0, j - N), j // 2
        k = np.arange(kmin, kmax + 1)
        h = j - 2 * k
        L[j, kmin:kmax + 1] = (gammaln(N + 1) - gammaln(k + 1) - gammaln(N - k + 1)
                               + gammaln(N - k + 1) - gammaln(h + 1) - gammaln(N - k - h + 1)
                               + h * log(2.0)
                               - (gammaln(2 * N + 1) - gammaln(j + 1) - gammaln(2 * N - j + 1)))
    return L


def gamete_freq(N, j, k, s_het, s_hom, mode):
    if mode == "real":
        h = j - 2 * k
        wa, wh = 1 - s_hom, 1 - s_het
        W = (N - h - k) + h * wh + k * wa
        return (0.5 * h * wh + k * wa) / W
    q = j / (2 * N)  # 'hwe': selection on expected HW genotype frequencies
    p = 1 - q
    wbar = p * p + 2 * p * q * (1 - s_het) + q * q * (1 - s_hom)
    return (q * q * (1 - s_hom) + p * q * (1 - s_het)) / wbar + 0 * k


class Chain:
    """Exact chain on newborn allele count j; per-generation aa count k | j by random pairing."""

    def __init__(self, N, s_het, s_hom, mode="real", prune=1e-20):
        self.N = N
        n2 = 2 * N
        L = log_pk_given_j(N)
        self.Pk = np.exp(L)
        self.items = []  # per j: (k array, P(k|j), x(j,k)); Bin rows computed lazily in kernel()
        for j in range(n2 + 1):
            ks = np.nonzero(self.Pk[j] > prune)[0]
            pk = self.Pk[j, ks]
            x = np.array([gamete_freq(N, j, int(k), s_het, s_hom, mode) for k in ks])
            self.items.append((ks, pk, x))
        self.Pk = None
        self.s_het, self.s_hom = s_het, s_hom

    def wbar(self, j, ks):
        h = j - 2 * ks
        return 1 - (self.s_het * h + self.s_hom * ks) / self.N

    def kernel(self, event):
        """A[j, j'] = sum_k P(k|j) 1[not event(j,k)] Bin(2N, x(j,k))(j');  s[j] = sum_k P(k|j) 1[not event]."""
        n2 = 2 * self.N
        A = np.zeros((n2 + 1, n2 + 1))
        s = np.zeros(n2 + 1)
        jj = np.arange(n2 + 1)
        for j, (ks, pk, x) in enumerate(self.items):
            keep = pk * (~event(j, ks, self))
            s[j] = keep.sum()
            nz = keep > 0
            if nz.any():
                A[j] = keep[nz] @ binom.pmf(jj[None, :], n2, x[nz][:, None])
        return A, s

    def p_event(self, pi0, G, event, count0=True):
        A, s = self.kernel(event)
        if count0:
            pi = pi0.copy()
        else:  # generation 0 not inspected
            A0, _ = self.kernel(lambda j, ks, c: np.zeros(len(ks), bool))
            pi = pi0 @ A0
            G = G - 1
        traj = []
        for _ in range(G):
            traj.append(1 - pi @ s)
            pi = pi @ A
        return 1 - pi @ s, traj

    def expected_counts(self, pi0, G):
        """E[sum over generations 0..G of k], E[sum of genetic deaths], E[max-free] via unconditional chain."""
        A, _ = self.kernel(lambda j, ks, c: np.zeros(len(ks), bool))
        ek = np.array([(pk * ks).sum() for ks, pk, x in self.items])
        ed = np.array([(pk * (self.s_hom * ks + self.s_het * (j - 2 * ks))).sum()
                       for j, (ks, pk, x) in enumerate(self.items)])
        pi = pi0.copy()
        tk = td = 0.0
        for _ in range(G + 1):
            tk += pi @ ek
            td += pi @ ed
            pi = pi @ A
        return tk, td


EV_HOM = lambda j, ks, c: ks >= 1
EV_W95 = lambda j, ks, c: c.wbar(j, ks) < 0.95
EV_W50 = lambda j, ks, c: c.wbar(j, ks) < 0.5
EV_Q10 = lambda j, ks, c: np.full(len(ks), j / (2 * c.N) >= 0.10)


def founder_pi(N, q):
    return binom.pmf(np.arange(2 * N + 1), 2 * N, q)


def hazard(N, q, G, s_het=S_HET, s_hom=S_HOM, mode="real", count0=True, chains={}):
    key = (N, s_het, s_hom, mode)
    if key not in chains:
        chains[key] = Chain(N, s_het, s_hom, mode)
    return chains[key].p_event(founder_pi(N, q), G, EV_HOM, count0)[0], chains[key]


def nohit_kernel_hazard(N, q, G, s_het):
    """Independent implementation: state = hets i given no aa so far (then genotype composition is i Aa, N-i AA)."""
    i = np.arange(N + 1)
    wh = 1 - s_het
    x = 0.5 * i * wh / ((N - i) + i * wh)
    a, b = 2 * x * (1 - x), (1 - x) ** 2
    tot = a + b
    pr = np.where(tot > 0, a / np.where(tot > 0, tot, 1), 0.0)
    M = (tot ** N)[:, None] * binom.pmf(i[None, :], N, pr[:, None])
    a0, b0 = 2 * q * (1 - q), (1 - q) ** 2
    v = (a0 + b0) ** N * binom.pmf(i, N, a0 / (a0 + b0))  # generation 0 founders, no aa
    for _ in range(G):
        v = v @ M
    return 1 - v.sum()


def mc_day_model(N, q, G, s_het, s_hom, mode, reps, seed_key):
    """Literal s3.1 Monte Carlo: iid alleles, random pairing, selection, Bin(2N), pairing; count aa gens 0..G."""
    rng = np.random.default_rng(np.random.SeedSequence([SEED_ROOT, *seed_key]))
    n2 = 2 * N
    j = rng.binomial(n2, q, size=reps)
    hit = np.zeros(reps, bool)
    for g in range(G + 1):
        live = np.nonzero((j > 0) & ~hit)[0]
        if live.size == 0:
            break
        # random pairing: place j copies on random distinct positions among 2N; individual = pos // 2
        keys = rng.random((live.size, n2))
        ranks = keys.argsort(axis=1)
        is_a = np.zeros((live.size, n2), bool)
        mask = np.arange(n2)[None, :] < j[live][:, None]
        rows = np.repeat(np.arange(live.size), n2).reshape(live.size, n2)
        is_a[rows[mask], ranks[mask]] = True
        k = (is_a[:, 0::2] & is_a[:, 1::2]).sum(axis=1)
        hit[live] |= k >= 1
        if g == G:
            break
        x = np.array([gamete_freq(N, int(jj), int(kk), s_het, s_hom, mode) for jj, kk in zip(j[live], k)])
        j[live] = rng.binomial(n2, x)
    return hit.mean(), hit.std(ddof=1) / np.sqrt(reps)


def main():
    t0 = time.time()
    out = {}
    pr = print

    pr("=== E1 arithmetic (Day's analytic route, Z23020792 s5.1) ===")
    from fractions import Fraction
    p = Fraction(9, 2500)  # 0.0036
    P2 = 1 - (1 - p) ** 100 - 100 * p * (1 - p) ** 99
    pr(f"P(>=2 carriers | Bin(100, 0.0036)) = {float(P2):.5f} (exact rational)")
    qf = Fraction(9, 5000)
    P2c = 1 - (1 - qf) ** 200 - 200 * qf * (1 - qf) ** 199
    pr(f"P(>=2 defect COPIES | Bin(200, 0.0018)) = {float(P2c):.5f};  P(>=1 copy) = {float(1 - (1 - qf) ** 200):.5f}")
    c39 = 1 - exp(-0.5)
    pr(f"1 - e^-0.5 = {c39:.5f};  0.0509 x it = {float(P2) * c39:.4%};  0.06 x 0.39 = {0.06 * 0.39:.4%}")
    pr(f"CMMRD incidence implied: pooled one-locus q^2 = {Q_POOLED**2:.3e} (1 in {1/Q_POOLED**2:,.0f}); "
       f"equal 4-gene split 4(q/4)^2 = {4*(Q_POOLED/4)**2:.3e} (1 in {1/(4*(Q_POOLED/4)**2):,.0f}); "
       f"Win-memory split = {sum((c/2)**2 for c in WIN_MEMORY_CARRIERS.values()):.3e} "
       f"(1 in {1/sum((c/2)**2 for c in WIN_MEMORY_CARRIERS.values()):,.0f}); Day s4.1: 1 in 1,000,000")
    pr(f"Win-memory carriers sum = 1/{1/sum(WIN_MEMORY_CARRIERS.values()):.0f}")
    for n in (10, 50, 100, 500):
        pr(f"  cumulative over {n} events at h=2.33%: {1-(1-0.0233)**n:.4f}")

    pr("\n=== E2 baselines / cross-implementation (N=100, G=50, q=0.0018) ===")
    chains = {}
    for mode in ("real", "hwe"):
        for lab, sh, sm in (("full", S_HET, S_HOM), ("s_het=0", 0.0, S_HOM), ("drift", 0.0, 0.0)):
            for c0 in (True, False):
                h, _ = hazard(100, Q_POOLED, 50, sh, sm, mode, c0, chains)
                out[f"N100G50_{mode}_{lab}_c0{int(c0)}"] = h
            pr(f"mode={mode:4s} {lab:8s}: P(>=1 aa, gens 0..50) = {out[f'N100G50_{mode}_{lab}_c01']:.4%}   "
               f"(gens 1..50) = {out[f'N100G50_{mode}_{lab}_c00']:.4%}")
    for sh in (S_HET, 0.0):
        pr(f"no-hit-kernel implementation (real, s_het={sh}): {nohit_kernel_hazard(100, Q_POOLED, 50, sh):.4%}")

    pr("\n=== E3 seeded MC of the literal s3.1 model (50,000 reps; SeedSequence([20261008, cfg])) ===")
    for ci, (lab, sh, sm, mode) in enumerate((("full", S_HET, S_HOM, "real"), ("s_het=0", 0.0, S_HOM, "real"),
                                              ("drift", 0.0, 0.0, "real"), ("full", S_HET, S_HOM, "hwe"),
                                              ("s_het=0", 0.0, S_HOM, "hwe"))):
        m, se = mc_day_model(100, Q_POOLED, 50, sh, sm, mode, 50_000, (ci,))
        out[f"MC_{mode}_{lab}"] = (m, se)
        pr(f"MC mode={mode} {lab:8s}: {m:.4%} +/- {se:.4%}")
    pr("Day Table 4: full 2.33%, s_het=0 3.62%, drift 3.94%")

    pr("\n=== E4 decomposition by founder copy count (N=100, G=50, gens 0..50) ===")
    for mode, lab, sh, sm in (("real", "full", S_HET, S_HOM), ("real", "drift", 0.0, 0.0)):
        ch = chains[(100, sh, sm, mode)]
        f = founder_pi(100, Q_POOLED)
        tot = 0
        rows = []
        for c in range(0, 8):
            pi0 = np.zeros(201)
            pi0[c] = 1
            hc = ch.p_event(pi0, 50, EV_HOM)[0]
            rows.append((c, f[c], hc, f[c] * hc))
            tot += f[c] * hc
        H = out[f"N100G50_{mode}_{lab}_c01"]
        pr(f"[{lab}] total {H:.4%}")
        for c, fc, hc, cont in rows[:6]:
            pr(f"   founder copies {c}: P(c) = {fc:.4f}, P(hom | c) = {hc:.4f}, contribution {cont:.4%} "
               f"({cont/H:.1%} of total)")
        ge2 = sum(r[3] for r in rows if r[0] >= 2)
        pge2 = sum(r[1] for r in rows if r[0] >= 2)
        pr(f"   >=2 copies: P = {pge2:.4f}, P(hom | >=2) = {ge2/pge2:.4f}, contribution {ge2:.4%} ({ge2/H:.1%})")
        out[f"decomp_{lab}"] = rows

    pr("\n=== E5 Day's Tables 2, 3, 5, 8 (mode real, full selection, gens 0..G) ===")
    day_t2 = {50: (1.6, 1.4, 20.6), 100: (2.3, 5.1, 14.7), 200: (3.5, 16.1, 12.0), 500: (6.0, 52.8, 9.4)}
    for N, (dh, d2, dc) in day_t2.items():
        h, ch = hazard(N, Q_POOLED, 50, chains=chains)
        f = founder_pi(N, Q_POOLED)
        ge2 = np.zeros(2 * N + 1)
        ge2[2:] = f[2:]
        hge2 = ch.p_event(ge2 / ge2.sum(), 50, EV_HOM)[0]
        pr(f"N={N:4d}: P(hom) {h:.3%} (Day {dh}%), P(>=2 copies) {ge2.sum():.3%} (Day {d2}%), "
           f"P(hom|>=2) {hge2:.3%} (Day {dc}%)")
        out[f"T2_{N}"] = (h, ge2.sum(), hge2)
    pr("Table 3 (G):")
    for N, dv in ((100, (2.33, 2.37, 2.48)), (500, (5.95, 5.68, 5.96))):
        vals = [hazard(N, Q_POOLED, G, chains=chains)[0] for G in (50, 100, 200)]
        pr(f"  N={N}: G=50/100/200: " + " / ".join(f"{v:.3%}" for v in vals) + f"   (Day {dv})")
    pr("Table 5 (N=100, G=100, carrier frequency c, q = c/2):")
    for c, dv in ((1 / 1000, 0.63), (1 / 500, 1.42), (1 / 280, 2.27), (1 / 200, 3.23), (1 / 100, 6.87), (1 / 50, 14.2)):
        pr(f"  carrier 1/{1/c:.0f}: {hazard(100, c / 2, 100, chains=chains)[0]:.3%} (Day {dv}%)")
    pr("Table 8 (G=200, f_m read as allele frequency):")
    t8 = {0.001: (1.2, 1.6, 2.4, 3.5), 0.005: (5.2, 8.3, 12.1, 20.5), 0.010: (10.8, 16.4, 24.3, 42.1),
          0.020: (21.8, 33.2, 48.7, 74.6), 0.050: (50.8, 71.8, 89.6, 99.4)}
    for fm, dv in t8.items():
        vals = [hazard(N, fm, 200, chains=chains)[0] for N in (50, 100, 200, 500)]
        pr(f"  f_m={fm}: " + " / ".join(f"{v:.2%}" for v in vals) + f"   (Day {dv})")

    pr("\n=== E6 sweep over sourced ranges (mode real, gens 0..G) ===")
    Ns, Gs = (50, 100, 200, 500, 1000), (50, 200, 1000, 10000)
    for lab, sh, sm in (("full", S_HET, S_HOM), ("drift", 0.0, 0.0)):
        pr(f"[{lab}] pooled q=0.0018:  rows N, cols G={Gs}")
        for N in Ns:
            ch = chains.get((N, sh, sm, "real")) or Chain(N, sh, sm, "real")
            chains[(N, sh, sm, "real")] = ch
            vals = [ch.p_event(founder_pi(N, Q_POOLED), G, EV_HOM)[0] for G in Gs]
            out[f"sweep_{lab}_{N}"] = vals
            pr(f"  N={N:5d}: " + "  ".join(f"{v:.3%}" for v in vals))

    pr("\n=== E7 per-gene treatment (CMMRD = biallelic in the SAME gene) N=100 ===")
    for lab, sh, sm in (("full", S_HET, S_HOM), ("drift", 0.0, 0.0)):
        for G in (50, 200):
            pooled = hazard(100, Q_POOLED, G, sh, sm, chains=chains)[0]
            eq = 1 - (1 - hazard(100, Q_POOLED / 4, G, sh, sm, chains=chains)[0]) ** 4
            win = 1 - np.prod([1 - hazard(100, c / 2, G, sh, sm, chains=chains)[0] for c in WIN_MEMORY_CARRIERS.values()])
            out[f"split_{lab}_{G}"] = (pooled, eq, win)
            pr(f"[{lab}] G={G}: pooled {pooled:.3%}; equal 4-gene split {eq:.3%} ({eq/pooled:.2f}x); "
               f"Win-memory split {win:.3%} ({win/pooled:.2f}x)")
    for N in (50, 200, 500):
        pooled = hazard(N, Q_POOLED, 50, chains=chains)[0]
        eq = 1 - (1 - hazard(N, Q_POOLED / 4, 50, chains=chains)[0]) ** 4
        pr(f"[full] N={N} G=50: pooled {pooled:.3%}; equal split {eq:.3%} ({eq/pooled:.2f}x)")

    pr("\n=== E8 consequences (mode real, full selection, pooled q, gens 0..G) ===")
    for N in (50, 100, 200):
        ch = chains[(N, S_HET, S_HOM, "real")]
        pi0 = founder_pi(N, Q_POOLED)
        for G in (50, 200):
            ph = 1 - ch.p_event(pi0, G, EV_HOM)[0]
            p95 = 1 - ch.p_event(pi0, G, EV_W95)[0]
            p50 = 1 - ch.p_event(pi0, G, EV_W50)[0]
            pq = 1 - ch.p_event(pi0, G, EV_Q10)[0]
            ek, ed = ch.expected_counts(pi0, G)
            births = N * (G + 1)
            out[f"conseq_{N}_{G}"] = dict(hom=1 - ph, w95=1 - p95, w50=1 - p50, q10=1 - pq, ek=ek, ed=ed)
            pr(f"N={N:3d} G={G:3d}: P(>=1 aa) {1-ph:.3%} | E[aa births] {ek:.4f} of {births} "
               f"({ek/births:.2e}/birth) | E[genetic deaths, s-weighted] {ed:.3f} ({ed/births:.2e}/birth) | "
               f"P(q>=10% ever) {1-pq:.3%} | P(wbar<0.95 ever) {1-p95:.4%} | P(wbar<0.5 ever) {1-p50:.2e}")
    for n in (100,):
        for N in (100,):
            d = out[f"conseq_{N}_50"]
            pr(f"Over {n} independent events (N={N}, G=50): P(>=1 aa) {1-(1-d['hom'])**n:.3f}; "
               f"P(any wbar<0.95) {1-(1-d['w95'])**n:.4f}; P(any wbar<0.5) {1-(1-d['w50'])**n:.2e}")

    pr(f"\nwall time {time.time() - t0:.1f} s")
    with open(os.path.join(RAW, "e_founder_hazard.json"), "w") as fh:
        json.dump({k: (v if not isinstance(v, np.ndarray) else v.tolist()) for k, v in out.items()}, fh, default=float)


def supplement():
    """POST HOC (added after the main run, to test pre-registered P3's implementation hypothesis and the 2-SE gap
    between the real-mode MC (2.61%) and the exact chain (2.75%)).  Run with argument 'supp'."""
    t0 = time.time()
    pr = print
    chains = {}
    pr("=== S1 Day's Tables 2, 3, 5, 8 under mode 'hwe' (selection on HW-expected genotypes), gens 0..G ===")
    for N, dv in ((50, 1.6), (100, 2.3), (200, 3.5), (500, 6.0)):
        h, ch = hazard(N, Q_POOLED, 50, mode="hwe", chains=chains)
        f = founder_pi(N, Q_POOLED)
        ge2 = np.zeros(2 * N + 1)
        ge2[2:] = f[2:]
        hge2 = ch.p_event(ge2 / ge2.sum(), 50, EV_HOM)[0]
        pr(f"T2 N={N}: P(hom) {h:.3%} (Day {dv}%); P(hom|>=2) {hge2:.3%}")
    for N, dv in ((100, (2.33, 2.37, 2.48)), (500, (5.95, 5.68, 5.96))):
        vals = [hazard(N, Q_POOLED, G, mode="hwe", chains=chains)[0] for G in (50, 100, 200)]
        pr(f"T3 N={N}: " + " / ".join(f"{v:.3%}" for v in vals) + f"  (Day {dv})")
    for c, dv in ((1 / 1000, 0.63), (1 / 500, 1.42), (1 / 280, 2.27), (1 / 200, 3.23), (1 / 100, 6.87), (1 / 50, 14.2)):
        pr(f"T5 carrier 1/{1/c:.0f}: {hazard(100, c / 2, 100, mode='hwe', chains=chains)[0]:.3%} (Day {dv}%)")
    t8 = {0.001: (1.2, 1.6, 2.4, 3.5), 0.010: (10.8, 16.4, 24.3, 42.1), 0.050: (50.8, 71.8, 89.6, 99.4)}
    for fm, dv in t8.items():
        vals = [hazard(N, fm, 200, mode="hwe", chains=chains)[0] for N in (50, 100, 200, 500)]
        pr(f"T8 f_m={fm}: " + " / ".join(f"{v:.2%}" for v in vals) + f"  (Day {dv})")
    pr("=== S2 second-seed MC, literal model (mode real), full selection, N=100, G=50, 200,000 reps, key (100,) ===")
    m, se = mc_day_model(100, Q_POOLED, 50, S_HET, S_HOM, "real", 200_000, (100,))
    pr(f"MC real full: {m:.4%} +/- {se:.4%}  (exact chain 2.7516%)")
    m, se = mc_day_model(100, Q_POOLED, 50, S_HET, S_HOM, "hwe", 200_000, (101,))
    pr(f"MC hwe  full: {m:.4%} +/- {se:.4%}  (exact chain 2.3834%)")
    pr(f"wall time {time.time() - t0:.1f} s")


def growth_hazard(N0, g, cap, q, G, s_het=S_HET):
    """Exact P(>=1 aa in gens 0..G), literal model (mode real), isolate size N_t = min(round(N0 g^t), cap)."""
    Ns = [int(min(round(N0 * g ** t), cap)) for t in range(G + 1)]
    pi = founder_pi(Ns[0], q)
    wh = 1 - s_het
    for t, N in enumerate(Ns):
        j = np.arange(2 * N + 1)
        ok = j <= N
        lp0 = np.full(2 * N + 1, -np.inf)
        jj = j[ok]
        lp0[ok] = (gammaln(N + 1) - gammaln(jj + 1) - gammaln(N - jj + 1) + jj * log(2.0)
                   - (gammaln(2 * N + 1) - gammaln(jj + 1) - gammaln(2 * N - jj + 1)))
        surv = pi * np.exp(lp0)  # no aa in generation t
        if t == G:
            return 1 - surv.sum()
        x = np.where(ok, 0.5 * j * wh / np.maximum((N - j) + j * wh, 1e-300), 0.0)
        n2n = 2 * Ns[t + 1]
        nz = surv > 1e-300
        pi = surv[nz] @ binom.pmf(np.arange(n2n + 1)[None, :], n2n, x[nz][:, None])


def supplement2():
    """POST HOC (review fix pass, REVIEW-R4-E-*): threshold sweep of the consequence endpoint, small N, E[aa | hit],
    E[aa | 2 founder copies] vs Day's Poisson 0.5, HW sampling-with-replacement explanation of 39%, isolate growth.
    NOT pre-registered.  Run with argument 'supp2'."""
    t0 = time.time()
    pr = print
    pr("=== R1 consequence threshold sweep (mode real, full selection, pooled q, G = 50, gens 0..50) ===")
    thr = (0.99, 0.98, 0.97, 0.95, 0.90, 0.5)
    for N in (20, 30, 50, 100, 200):
        ch = Chain(N, S_HET, S_HOM, "real")
        pi0 = founder_pi(N, Q_POOLED)
        ph = ch.p_event(pi0, 50, EV_HOM)[0]
        ek, ed = ch.expected_counts(pi0, 50)
        cells = []
        for w in thr:
            pw = ch.p_event(pi0, 50, lambda j, ks, c, w=w: c.wbar(j, ks) < w)[0]
            cells.append(f"<{w}: {max(pw,0):.3e} ({ph/max(pw,1e-300):.3g}x)")
        pr(f"N={N:3d}: P(>=1 aa) {ph:.4%}; E[aa births] {ek:.4f}; E[aa | hit] {ek/ph:.2f}; 1 aa lowers wbar by "
           f"{S_HOM/N:.4f} | " + " | ".join(cells))
    ch = Chain(100, S_HET, S_HOM, "hwe")
    pi0 = founder_pi(100, Q_POOLED)
    ph = ch.p_event(pi0, 50, EV_HOM)[0]
    pr(f"[hwe-mode chain, N=100] P(>=1 aa) {ph:.4%}; " + " ".join(
        f"<{w}: {max(ch.p_event(pi0, 50, lambda j, ks, c, w=w: c.wbar(j, ks) < w)[0],0):.3e}" for w in thr[:4]))

    pr("\n=== R2 two founder copies: expected aa births vs Day's Poisson mean 0.5 (N=100, G=50) ===")
    for lab, sh, sm in (("drift", 0.0, 0.0), ("full", S_HET, S_HOM)):
        ch = Chain(100, sh, sm, "real")
        pi0 = np.zeros(201)
        pi0[2] = 1
        ph = ch.p_event(pi0, 50, EV_HOM)[0]
        ek, _ = ch.expected_counts(pi0, 50)
        pr(f"[{lab}] P(>=1 aa | 2 copies) {ph:.4f}; E[aa births | 2 copies] {ek:.3f} (Day: mean 0.5, P 0.393)")
    pr(f"HW with replacement: N q^2 = {100*0.01**2:.4f}/gen; random pairing of 2 copies: 1/(2N-1) = {1/199:.5f}/gen; "
       f"1-(1-1/199)^51 = {1-(1-1/199)**51:.4f}; 1-exp(-50*0.01) = {1-exp(-0.5):.4f}")

    pr("\n=== R3 isolate growth (literal model, full selection, N0 = 100, N_t = min(N0 g^t, cap)) ===")
    pr(f"validation g=1: {growth_hazard(100, 1.0, 100, Q_POOLED, 50):.4%} (Chain 2.7516%)")
    for cap in (1000,):
        for g in (1.0, 1.02, 1.05, 1.1, 1.2, 1.5, 2.0):
            vals = [growth_hazard(100, g, cap, Q_POOLED, G) for G in (50, 200)]
            pr(f"g={g:4.2f} cap={cap}: G=50 {vals[0]:.3%}  G=200 {vals[1]:.3%}")
    pr(f"wall time {time.time() - t0:.1f} s")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "supp2":
        supplement2()
    elif len(sys.argv) > 1 and sys.argv[1] == "supp":
        supplement()
    else:
        main()

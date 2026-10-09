"""X1: arithmetic and internal-validity audit of every quantitative critic and ally claim (PRE-REGISTERED).

WHY.  R5 draft balance audit: 15 of 24 checks tested Day, 1 tested a critic claim; 22 of 112 Day nodes carry an internal
non-sequitur / arithmetic-error verdict against 0 of 51 critic nodes; PLAN.md item 10 ("arithmetic audit, all") was never done
for the critics.  X1 applies the SAME standard to every critic / ally claim that carries a number or a derivation.

STANDARD (the one used for Day):  internal = arithmetic-error if the number is wrong from the author's OWN stated inputs;
non-sequitur if the conclusion does not follow from the author's own premises; holds otherwise.  fidelity = are the inputs
cited and read correctly (quote vs raw text; unit and basis).  External questions (is the model right?) are NOT scored here.
A third column, "material?", asks whether the slip carries an argument (changes a conclusion or a headline by more than ~2x).

SCOPE.  All claim files in docs/research/claims/ with side critic or ally (66 files).  Rows are keyed X1-<claim id>-<n>.
Claim files with no number or derivation (listed in the write-up, not here): A2i (logic only), A4b, A5f, B4e, B4f, B5g,
D1, D1a-D1d, D13, D15, E1, G1c, G2d, G2e, G2f, G3a, ROOT-de, ROOT-t, ROOT-h (numbers are A5a/H5/B5h), F4a n/a.

METHOD.  Pure arithmetic with sympy (exact rationals) / numpy.  Two heavier recomputations: (a) keruru's C5 absorption
probabilities by an EXACT Wright-Fisher (binomial) backward recursion, 2N = 20,000 copies, 240 generations, banded to
+-W copies (the band is >10 sd, truncation negligible); (b) the conditional fixation-time CDF quoted by Nesslig20, by the
same exact recursion at 2N = 1,000 (finite-N tolerance ~0.02).  Raw texts in sources/raw/ are read as plain text only
(substring checks of inputs: Day's 38,400, Day's per-lineage 205M, McCarthy's 25 y vs 20 y).  Nothing downloaded is executed.

RUN:  nice -n 19 research/.venv/bin/python -I research/checks/x1_critic_arithmetic.py        (writes results/raw/x1_results.json)

PREDICTIONS (written before the run).  R = reproduces from the author's own inputs; N = does not reproduce; P = reproduces
with a flagged caveat (basis, unit or input problem).  Several predictions lean on arithmetic already done in claim files
(marked [cf]); those are not independent.  Predictions marked [new] are not in any claim file.

 McCarthy (B5a, F1b, G3, A5, A3x)
 M01 B5a  100 x 1e4 / 20 y = 50,000/yr; x 9e6 y = 4.5e11; x 1/20,000 = 22.5M                    R [cf]
 M02 B5a/F1b  comment 337116873: (360,000-40,000) gens; "8 My x 50,000/yr = 400 billion"; /20,000 = 20M
        chain as written R; but 360,000 gens uses 25 y/gen and 50,000/yr uses 20 y/gen. One generation time throughout
        gives 16.0M (25 y) or 20.5M (20 y, 4Ne=40,000 gens).                                    P: mixed units, ~20% [new]
 M03 B5a  comment 340149310: "400 billion x 1/20000 = 35 million"                              N (=20M, factor 1.75) [cf]
 M04 A5   "3.1e9 / 4.6e6 = roughly 690"                                                        N (674; 2.4% off) [cf]
 M05 G3   P_specific = (5e-5)^2e7 ~ 10^-86,020,600; supply 22.5M, sd 4,743, 20M is 527 sd below  R [cf]
 M06 B5a  McCarthy's own 60-100 de novo range x 97% non-deleterious gives 13.1M-21.8M over 450,000 gens
        (the 22.5M headline uses the top of his own range, as Day's input)                       P (range, not a point) [new]
 Mansfield (B5b, F1, B6)
 F01 B5b  2 neutral/zygote x N zygotes = 2N alleles, x 1/(2N) = 1 fixation/generation (N cancels) R
 F02 B5b  x 450,000 gens = 450,000 vs 20M: 44.4x short; f needed = 0.889; his later "predict about 20 million"
        requires f ~ 0.9, i.e. consistent with "way under the actual proportion"              R, illustration only [cf]
 F03 F1   truck analogy: 20,000 trucks/h x 1/20,000 = 1/h; 100 arrivals = 100 h               R [new]
 F04 B5b  "the genome is only about 10 times that number" (3.1e9 / 2e8)                        P (15.5x; referent unclear) [new]
 F05 A3x  "around 25 million give or take" SNVs (1% of 3.1e9 = 31M)                           R (loose) [new]
 Hancock / Gutsick Gibbon (B5c, A3d, A5c, G2, B6c)
 H01 B5c  6.4e9 x 1.2e-8 = 76.8 per generation (first pass, diploid genome)                   R arithmetic; basis wrong, self-corrected [cf]
 H02 B5c  2 x 252,000 x 76.8 = 38.7M; haploid 38.4 -> 19.35M                                   R [cf]
 H03 B5c  (98+206)/2 = 152; /2 = 76; 2 x 252,000 x 76 = 38.3M ("about 38 million")              R [cf]
 H04 B5c  "38M matches 35-40M": post-split 2muT L = 19.35M plus ancestral polymorphism
        theta_anc L (Ne_anc 1.32e5) = 20.3M gives 39.6M; 38M ~ 35M observed is the SNV double count   P [cf]
 H05 B5c  205e6/(2 x 252,000) = 406.7 per generation; Day's 205M is per lineage (text: "apportioned
        symmetrically to the human lineage"), so the per-generation requirement is 813 and "~5x" is ~10.6x
        (against 76.8)                                                                           R arithmetic; P fidelity (unit of 205M) [cf]
 H06 A3d  doubling the achievable (180 -> 360) leaves shortfall 205e6/191 unchanged when the comparator is per lineage
                                                                                                 R arithmetic; no effect on Day's ratio [cf]
 H07 A5c  4.6e6 x 1e-11 = 4.6e-5 ("4e-5"); 1/4.6e-5 = 21,739 ("22,000"); at measured 8.9e-11: 2,439  R / P (input 8.9x low) [cf]
 H08 B5   Taylor/limit s->0 of Kimura u(p0) = p0, so k = 2N mu p0 = mu for p0 = 1/(2N)         R (sympy) [new]
 H09 B6c  theta = 4 Ne mu = 4.8e-4 per site, 1.5e6 differences per genome pair                  R [cf]
 H10 G2   252,000/1,400 = 180; 252,000/66,000 = 3.8; 252,000/20,000 = 12.6; 252,000/27,600 = 9.1  R [cf]
 Nesslig20 / Peaceful Science (B5e, H6, A3x, unmapped)
 N01 B5e  2 x 75 x (6.3e6/25) = 37.8M                                                           R
 N02 B5e  basis of 75: defined per HAPLOID genome; "estimates 100 to 200 per generation" (a per-newborn range);
        75 as a haploid event count = 150 per newborn, inside Hancock's 98-206; 75 is 1.95x the SNV pedigree
        haploid 38.4; as a zygote count the product is 18.9M                                    P (basis unstated) [cf]
 N03 B5e  1-2% of 3.1e9 = 31-62M                                                                R [new]
 N04 B5e  conditional fixation-time CDF F(t)=1+sum(-1)^i (2i+1) exp(-i(i+1)t/(4Ne)): 50% at 3.48Ne, 60.6% at
        4Ne, 95% at 8.19Ne, 99% at 11.41Ne, 99.9% at 16.01Ne; mean 4Ne                           R (series); exact-WF CDF agrees within 0.02 [new]
 N05 B5e  summed-CDF lag = 4Ne (= int(1-F)); 2 x 75 x (252,000 - 40,000) = 31.8M if the lag were applied R [new]
 N06 A2d  G_f: 20,000/45 = 444; (40,000-26,500)/(653-60) = 22.8; 1/444 = 0.0023 vs mu L = 4.6e-3; 37.8M R [new]
 N07 (no claim) lottery: n = ln0.5/ln(1-1e-8) = 69,314,717; P(2e8) = 0.86; P(4e8) = 0.98; P(7e7) = 0.51   R, last one 0.503 (rounding) [new]
 N08 A3x  toy: 1/60 = 1.7%, 9/60 = 15%, sum 16.7%; 60 x 0.167 = 10; 14% x 3 Gbp ~ 410 Mbp          R [new]
 N09 (no claim) Part II BRT: (1/500) x 252,000 = 504; "P_fix = 1/Ne = 0.00005" (value is 1/(2Ne) at Ne = 1e4;
        symbol slip); the 1/500 is a birth PREVALENCE used as a new-mutation rate                R arithmetic; P (input) [new]
 N10 H6   Haldane 30 Ne / (0.1 Ne) = 300; T_fix(p) -> 4Ne as p -> 0                              R [cf]/[new]
 Reddit commenters (B5f, A2h, A2c, E5, A3a) and KITTENS (A5b)
 R01 B5f  38.4 x 252,000 = 9.68M; 17.5M / 9.68M = 1.81 ("under a factor of two")                 R
 R02 B5f  (252,000-40,000) x 38.4 = 8.14M; (252,000-132,000) x 38.4 = 4.6M                       R [cf]
 R03 A2h  3.2e9 x 1.2e-8 x 100 = 3,840, Day prints 38,400 (confirm in raw Z23003785)             R: critic correct, Day wrong [cf]
 R04 A2c/E5  mean of seven mutators with Ara-2 = -906: 477.6 -> 104.7 gen/fix; non-mutator 227/5 = 45.4 -> 1,321.6  R [cf]
 R05 A3a  RE-14: 2 x 187 Mb + 35M = 409M ~ 410M (reconstructs Day's total)                       R [new]
 K01 A5b  38.4 / 4.1e-4 = 93,659; 205/17.5 = 11.71; product 1.097M vs paper 1.075M (2.1%)        R
 K02 A5b  191 x 93,659 = 17.89M ("17.9 million") vs 17.5M                                       R
 K03 A5b  "shortfall = 94,000 x 11.7": SNV-only shortfall in the paper is 91,600 (17.5M/191); 94,000 is the
        supply ratio; the product 91,600 x 11.7 = 1.07M, so the decomposition is an identity only at parity P (2.6%) [new]
 Camestros Felapton (A2d, B6b, G1c, CA-01..14)
 C01 CA-06  35 mutations at 15,000 gens: "1500/35 ~ 429" (the numerator is a typo; 15,000/35 = 428.6)  P (typo, result right) [cf]
 C02 CA-01/02  F_max = t d /(g G_f) as transcribed; first-edition arithmetic 9e6 x 0.45/(20 x 1,600) = 126.6, "arithmetic
        itself isn't wrong"                                                                      R [new]
 C03 B6b  Day 2019: 15M + 15M = 30M; CSAC fixed share 0.78-0.86 of 35M = 27.3-30.1M              R [cf]
 Hossjer (A5a, H5, B5h)
 J01 A5a  9e6 x 0.45/(20 x 1,600) = 126.6; x 125 = 15,820 ("15,800"); x 652 = 10.30M; 20/10.30 = 1.94  R [cf]
 J02 A5a  "more than three orders below 20M": 20e6/15,800 = 1,266; "more than five orders": 20e6/127 = 157,480  R [new]
 J03 B5h  3e9 x 0.45 x 1.25e-8 x 450,000 = 7.59M (gap 2.63); without d 16.9M (1.19x); G_neutral = 2,174 ("2,170") R [cf]
 J04 H5   Haldane window 450,000/300 = 1,500; 15,800/1,500 = 10.5; "650 times" = 652              R [cf]; internal non-sequitur stays [cf]
 J05 A5a  d = g/A = 0.45 implies A = 44.4 y; "genome 650 times larger"                           R [new]
 Matev (B3i, G5, A2i, RF-3)
 V01 B3i  sum over 2N copies of 1/(2Ne) = N/Ne > 1; exact chain: sum of fixation probabilities = 1
        for exchangeable (WF and a sweepstakes model with lower Ne)                              R (exact linear solve) [new]
 V02 G5   n = 157,000, p = 0.5: Var 39,250, sd 198.1, CV 0.252%; CV falls as 1/sqrt n, Var rises   R [cf]
 V03 RF-3 "one over sixteen-billion" = 1/(2 x 8e9)                                              R [new]
 keruru (B7c, C5, C5b, B2e, B4g)
 K-01 B7c  P_fix = 1/(2N_census) to 15 decimals (exact chain); sweepstakes with Ne << N: same    R (exact linear solve) [new]
 K-02 C5  "6/10 of 1%": 240/40,000 = 0.6%; "1 My": 40,000 x 25 y; sd 0.0548 ("about 0.05")      R [cf]
 K-03 C5  absorption within 240 gens from p = 0.5: stated 4e-35; at p = 0.1 stated 6e-93; "only above 0.99
        any meaningful chance"; million-locus expected count stated 1e-29. Repo Brownian value 1.2e-46.
        Prediction: exact WF at p = 0.5 lies within a factor 10 of the Brownian arcsine value (1e-47 to 1e-45), so
        4e-35 is NOT reproduced (too large by ~1e11; the direction is conservative: zero is still more expected);
        p = 0.1 NOT reproduced; 0.99 reproduces (a few %); million loci at p = 0.5 gives ~1e-40, not 1e-29;
        a uniform "intermediate" spectrum to 0.9 gives an expected count that is dominated by its top edge
        (>>1e-29).                                                                                 N for the numbers; R for the conclusion [new]
 K-04 B4g  1.23% / (2 x 252,000) = 2.44e-8 = 2.03 x 1.2e-8; subtracting theta_anc (6.3e-3) gives 1.18e-8  R [cf]
 K-05 C5b  250/(2 x 9,835) = 0.0127; Ne = 2 saturates (62.5); 8,139 and 9,835 are a rate of F, not tested here  R [cf]
 K-06 B2e  4/(Vk+2) = 0.571 at Vk = 5; 0.571 / 8.1e-4 = 700; /6.9e-4 = 824; 4 Ne/260,000 = 1.4, 10.7, 12.5, 15.1%  R [cf]
 K-07 B2e  the draft states the measured ratio three ways (1e-4, 4e-4, 8e-4); 6,933/1e7 = 6.9e-4, 8,139/1e7 = 8.1e-4  P (internal inconsistency, draft flagged "[CHECK]") [cf]
 Other critics and allies
 G01 G2a  60,000 x 4 h = 240,000 h = 27.4 y                                                       R [cf]
 G02 G2b  252,000/1,400 = 180; 205e6/180 = 1,138,889 (paper 1,139,000x); 180 x 2 = 360            R [cf]
 G03 A4c  Duffy "25 generations" at 80% efficiency: units unstated; 1,600/25 = 64; Day 2019 1,600/15.7 = 102   not determinable (P) [cf]
 G04 G1b  205e6/252,000 = 813; 17.5e6/252,000 = 69.4 per generation                              R [cf]
 G05 ROOT-k Keen: 6.3e6 y x 1.075e6 = 6.77e12 y = 491 universe ages (13.8e9 y); "orders of magnitude" R if shortfall is a time multiplier [cf]
 G06 D14  Eden via Davis: 1/(1e-15 x 1e-21) = 1e36; pop. 1e36/(1e12 x 1e-6) = 1e30; "1e13 tons" => 1e-11 g per cell
        (10x an E. coli ~1 pg); 1e13 t over 5.1e14 m2 = 2 cm                                  R arithmetic; P (cell mass) [new]
 G07 D8   Milton/Day: 1e-65 "equivalent to winning the lottery every week for a thousand years with the same numbers":
        a 1-in-1.4e8 lottery won 52,143 weeks running is 10^-424,000; 1e-65 is ~8 weeks         N (analogy off by thousands of orders) [new]
 G08 F4   Bowers "u ~ 2s": Kimura u(N=100, s=0.01) = 0.02017; 2s = 0.02                          R [cf]
 G09 A2d  Day's table: 1,322/78 = 16.9; 893/104.7 = 8.5 (the LTEE contains 8.5-17x faster rates) R [cf]
 S01 A3   CSAC "5M indel events" (two-lineage total, not per lineage; GAP-07/07b measured 4.30M)  carried, not recomputed [cf]

Seeds: none (deterministic).  Output: results/raw/x1_results.json, x1_results.txt.
"""
import os
import re
import sys
import json
import math
import time

import numpy as np
import sympy as sp
from scipy import sparse
from scipy.stats import binom, norm

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "results", "raw")
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
RAWSRC = os.path.join(ROOT, "sources", "raw")

ROWS = []


def row(rid, claim, author, stated, recomputed, outcome, note, material="no"):
    ROWS.append(dict(id=rid, claim=claim, author=author, stated=stated, recomputed=recomputed,
                     outcome=outcome, material=material, note=note))
    print("%-7s %-5s %-12s %-3s | %s | %s | %s" % (rid, claim, author, outcome, stated, recomputed, note[:160]), flush=True)


def R(x):
    return sp.Rational(x)


def f(x, nd=4):
    return float(sp.N(x, 12)) if not isinstance(x, float) else x


def rel(a, b):
    return abs(a - b) / abs(b)


def read_text(*parts):
    p = os.path.join(RAWSRC, *parts)
    try:
        with open(p, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return None


# ---------------------------------------------------------------- exact Wright-Fisher recursion
def wf_band_matrix(M, W):
    """Row i = Binomial(M, i/M) pmf over j in [i-W, i+W] (padded coordinates j + W).  Absorbing rows are automatic
    (p = 0 -> all mass at 0; p = 1 -> all mass at M)."""
    n = M + 1
    width = 2 * W + 1
    data = np.empty(n * width)
    for start in range(0, n, 2000):
        stop = min(n, start + 2000)
        ii = np.arange(start, stop)[:, None]
        jj = ii + np.arange(-W, W + 1)[None, :]
        ok = (jj >= 0) & (jj <= M)
        pm = binom.pmf(np.where(ok, jj, 0), M, ii / M)
        pm = np.where(ok, pm, 0.0)
        data[start * width: stop * width] = pm.ravel()
    indptr = np.arange(0, n * width + 1, width, dtype=np.int64)
    indices = (np.arange(n, dtype=np.int32)[:, None] + np.arange(0, width, dtype=np.int32)[None, :]).ravel()
    return sparse.csr_matrix((data, indices, indptr), shape=(n, n + 2 * W))


def wf_backward(M, W, T, store=()):
    """u_t(i) = P(absorbed at M within t generations | i copies), t = 0..T.  Returns dict t -> u (for t in store) and u_T."""
    P = wf_band_matrix(M, W)
    u = np.zeros(M + 1 + 2 * W)
    u[W + M] = 1.0
    out = {}
    for t in range(1, T + 1):
        un = P @ u
        u = np.zeros(M + 1 + 2 * W)
        u[W:W + M + 1] = un
        u[W + M] = 1.0                      # absorbing at M stays 1
        if t in store:
            out[t] = un.copy()
    return out, u[W:W + M + 1]


def wf_forward_fix_mass(M, W, i0, T):
    """P(absorbed at M by t) for t = 0..T from i0 copies, forward evolution."""
    P = wf_band_matrix(M, W)
    PT = P.T.tocsr()
    v = np.zeros(M + 1)
    v[i0] = 1.0
    cum = np.zeros(T + 1)
    for t in range(1, T + 1):
        vj = PT @ v                          # forward: v'[j] = sum_i v[i] P[i, j]; length M+1+2W (padded coordinates)
        v = vj[W:W + M + 1].copy()
        cum[t] = v[M]
    return cum


def nesslig_cdf(x, terms=400):
    """F(t) with x = t/(4Ne): 1 + sum (-1)^i (2i+1) exp(-i(i+1) x)."""
    i = np.arange(1, terms + 1)
    return 1.0 + np.sum(((-1.0) ** i) * (2 * i + 1) * np.exp(-i * (i + 1) * x))


def main():
    t0 = time.time()
    # ================================================================== McCarthy
    per_year = R(100) * 10**4 / 20
    total = per_year * 9 * 10**6
    k = total / (2 * 10**4)
    row("M01", "B5a", "McCarthy", "50,000/yr; 4.5e11; 22.5M", "%s/yr; %.3g; %.4g" % (per_year, f(total), f(k)),
        "R", "reproduces from Day's inputs (100 mutations/newborn, N = 10,000, 9 My, 20 y)")
    # M02
    gens25 = R(9 * 10**6) / 25
    lag = 4 * 10**4
    chain = (gens25 - lag) * 25            # years of production
    stated_total = 50000 * chain           # his 50,000/yr (20 y basis) x 8 My
    stated_fix = stated_total / 20000
    n25 = (gens25 - lag) * 100 * 10**4     # 25 y throughout: per generation 1e6
    fix25 = n25 / 20000
    fix20 = (R(9 * 10**6) / 20 - lag) * 100 * 10**4 / 20000
    fix20b = (R(9 * 10**6) / 20 - 50000) * 50   # subtract 50,000 gens (=1 My at 20 y) as the post-level 20.0M
    row("M02", "B5a/F1b", "McCarthy", "320,000 gens; 400e9; 20M",
        "chain %.3gM; 25 y throughout %.3gM; 20 y throughout %.3gM (50,000 gens subtracted: %.3gM)" % (
            f(stated_fix) / 1e6, f(fix25) / 1e6, f(fix20) / 1e6, f(fix20b) / 1e6),
        "P", "time uses 25 y/gen (360,000 = 9 My/25) but supply uses the 20 y/gen figure 50,000/yr; consistent 25 y gives 16.0M; "
             "also '40,000 years' is 40,000 generations (units slip in prose)", material="yes (20%)")
    t1 = read_text("refresh-2026-10-09", "mccarthy-comments-why", "comments.json")
    if t1:
        row("M02f", "B5a/F1b", "McCarthy", "text 'Nine million years divided by 25'", "present=%s; '50,000 x 8,000,000' present=%s" % (
            "Nine million years divided by 25=360,000" in t1, "50,000 x 8,000,000=400 billion" in t1), "R",
            "fidelity: comment text confirmed in raw JSON")
    row("M03", "B5a", "McCarthy", "400 billion x 1/20000 = 35 million", "%.4g" % (4e11 / 2e4), "N",
        "arithmetic-error; the same comment's headline (35M vs 180) is unaffected; 20M in his post and his comment 337116873", material="no")
    t2 = read_text("refresh-2026-10-09", "mccarthy-comments-vdr", "comments.json")
    if t2:
        row("M03f", "B5a", "McCarthy", "text '400 billion x 1/20000 = 35 million'", "present=%s" % ("400 billion x 1/20000 = 35 million" in t2), "R",
            "fidelity: confirmed in raw JSON (comment 340149310)")
    row("M04", "A5", "McCarthy", "roughly 690x", "%.1f (3.1e9/4.6e6); 689 if E. coli = 4.5 Mb" % (3.1e9 / 4.6e6), "N",
        "immaterial 2.4% rounding; ratio direction and size unaffected")
    p = 5e-5
    M_ = 4.5e11
    sd = math.sqrt(M_ * p * (1 - p))
    z = (20e6 - M_ * p) / sd
    row("M05", "G3", "McCarthy", "P_specific tiny; P_any ~ 1", "supply %.4gM, sd %.0f, z = %.0f sd, log10 P_specific = %.0f" % (
        M_ * p / 1e6, sd, z, 2e7 * math.log10(5e-5)), "R", "Day's 10^-86,000,000 is 10^%.0f exactly" % (2e7 * math.log10(5e-5)))
    lo, hi = 60 * 0.97 / 2 * 450000, 100 * 0.97 / 2 * 450000
    row("M06", "B5a", "McCarthy", "22.5M from 100/newborn", "60-100 range x 0.97 non-deleterious x 450,000 gens: %.1fM-%.1fM" % (lo / 1e6, hi / 1e6),
        "P", "headline uses top of his own range (Day's input); his stated 60-100 gives 13.1-21.8M against 20M required; 3% is uncited")

    # ================================================================== Mansfield
    N = sp.symbols("N", positive=True)
    alleles = 2 * N                 # 2% of 100 = 2 per zygote x N zygotes
    fix = sp.simplify(alleles * 1 / (2 * N))
    row("F01", "B5b", "Mansfield", "2N neutral alleles x 1/(2N) = 1 per generation", "symbolic: %s" % fix, "R", "N cancels; exact")
    gens = 9 * 10**6 // 20
    row("F02", "B5b", "Mansfield", "(illustration) 1/generation", "%d fixations over %d gens; 20M/%d = %.1fx short; f for 20M = %.3f; f for 17.5M over 252,000 gens = %.3f" % (
        gens, gens, gens, 20e6 / gens, 20e6 / (50 * gens), 17.5e6 / (50 * 252000)), "R",
        "Mansfield says the real proportion is 'much higher'; the needed neutral share (0.89) is consistent with that and with McCarthy's 97%")
    row("F03", "F1", "Mansfield", "20,000 trucks/h, p = 1/20,000, 100 arrivals in 100 h", "%.3g arrivals/h; %.0f h for 100" % (20000 / 20000, 100 / (20000 / 20000)), "R",
        "steady-state throughput = arrival x probability, latency irrelevant (full pipe assumed, B6)")
    row("F04", "B5b", "Mansfield", "'genome is only about 10 times that number' (200M)", "%.1f" % (3.1e9 / 2e8), "P",
        "imprecise (15.5x), referent unclear; immaterial")
    row("F05", "A3x", "Mansfield", "~25M SNV differences", "1%% of 3.1e9 = %.0fM; 35M (CSAC), 37.8M (GAP-07b)" % (31), "R", "loose, uncited, inside the 25-35M literature spread")

    # ================================================================== Hancock
    row("H01", "B5c", "Hancock", "76.8 per generation", "6.4e9 x 1.2e-8 = %.1f; haploid 3.2e9 x 1.2e-8 = %.1f" % (6.4e9 * 1.2e-8, 3.2e9 * 1.2e-8), "R",
        "arithmetic reproduces; diploid genome was the wrong basis for a fixation rate and Hancock corrected it on screen (GG-05)")
    row("H02", "B5c", "Hancock", "38M", "2 x 252,000 x 76.8 = %.1fM; with 38.4: %.2fM" % (2 * 252000 * 76.8 / 1e6, 2 * 252000 * 38.4 / 1e6), "R",
        "first pass reproduces; the corrected SNV value is half")
    row("H03", "B5c", "Hancock", "152 / 2 = 76; ~38M", "mean(98,206) = %d; /2 = %d; 2 x 252,000 x 76 = %.2fM" % ((98 + 206) / 2, (98 + 206) / 4, 2 * 252000 * 76 / 1e6), "R",
        "the retained 76 is an event count (cited de novo range 98-206), not 76.8; reproduces")
    theta_anc = 4 * 1.32e5 * 1.2e-8
    two_mu_T = 2 * 1.2e-8 * 252000
    row("H04", "B5c", "Hancock", "38M matches 35-40M observed", "2muT L = %.2fM; theta_anc L = %.2fM (Ne_anc 1.32e5); sum %.1fM vs observed ~35M (SNV) / ~40M (events)" % (
        two_mu_T * 3.2e9 / 1e6, theta_anc * 3.2e9 / 1e6, (two_mu_T + theta_anc) * 3.2e9 / 1e6), "P",
        "arithmetic holds; on an SNV basis the observed total is post-split supply PLUS ancestral polymorphism, so 19M + 20M (not 38M alone) is the null; the "
        "qualitative conclusion (neutral supply is enough) survives, the match is coincidental on an SNV reading and fine on an event reading", material="no (conclusion survives)")
    row("H05", "B5c", "Hancock", "205M -> 'something like 407' per generation; ~5x", "205e6/(2 x 252,000) = %.1f; per-lineage reading 205e6/252,000 = %.0f; 813/76.8 = %.1fx (2 lineages: 813/153.6 = %.1fx)" % (
        205e6 / 504000, 205e6 / 252000, 205e6 / 252000 / 76.8, 205e6 / 252000 / 153.6), "R",
        "arithmetic reproduces; fidelity: Day's 205M is already per lineage (apportioned symmetrically, Z23003785), so dividing by BOTH lineages' generations halves the requirement")
    d3 = read_text("day", "zenodo-23003785.txt")
    if d3:
        row("H05f", "B5c/A3d", "Hancock", "Day: 205M per lineage", "'apportioned symmetrically to the human lineage' present=%s; '205 million required fixations on the human lineage' present=%s" % (
            bool(re.search(r"symmetrically to the human lineage", re.sub(r"\s+", " ", d3))), bool(re.search(r"205 million required fixations on the human lineage", re.sub(r"\s+", " ", d3)))),
            "R", "fidelity: Day's text confirmed (read-only grep of sources/raw/day/zenodo-23003785.txt)")
    row("H06", "A3d", "Hancock", "should be 2 x 180 = 360 (factor of two)", "205e6/191 = %.0f; 410e6/(2 x 191) = %.0f (same)" % (205e6 / 191, 410e6 / 382), "R",
        "the doubling is arithmetically right if the comparator is a two-lineage total; Day's comparator is per lineage, so the shortfall ratio is invariant (no effect)")
    mu_ = sp.Rational(1, 10**11)
    row("H07", "A5c", "Hancock", "4e-5 per gen; ~22,000 gens", "4.6e6 x 1e-11 = %.2e; 1/that = %.0f; at 8.9e-11: %.2e, %.0f gens (stated 8.9x lower rate)" % (
        4.6e6 * 1e-11, 1 / (4.6e6 * 1e-11), 4.6e6 * 8.9e-11, 1 / (4.6e6 * 8.9e-11)), "P",
        "22,000 reproduces from 1e-11; '4e-5' is 4.6e-5 rounded down 13%; the input 1e-11 is 8.9x below the measured LTEE 8.9e-11 (neutral 2,439 gens vs observed 1,322, not 22,000)", material="partly (17x vs 1.8x)")
    s_, p0, Nn = sp.symbols("s p0 N", positive=True)   # (N here is the census size in the Kimura u)
    u = (1 - sp.exp(-4 * Nn * s_ * p0)) / (1 - sp.exp(-4 * Nn * s_))
    lim = sp.limit(u, s_, 0)
    row("H08", "B5", "Hancock", "neutral substitution rate = mutation rate", "limit s->0 of Kimura u(p0) = %s; k = 2N mu x (1/2N) = mu" % lim, "R", "sympy; with p0 = 1/(2N) census N")
    row("H09", "B6c", "Hancock", "no variation under serial model", "theta = %.2e per site; %.2e differences per genome pair" % (4e4 * 1.2e-8, 4e4 * 1.2e-8 * 3.2e9), "R", "observed diversity ~1e-3 per site is >> 0, so the serial reading fails; consistent")
    row("H10", "G2", "Hancock", "serial divisions", "252000/1400 = %.0f; /66000 = %.1f; /20000 = %.1f; /27600 = %.1f" % (252000 / 1400, 252000 / 66000, 252000 / 20000, 252000 / 27600), "R", "")

    # ================================================================== Nesslig20
    row("N01", "B5e", "Nesslig20", "37.8M", "2 x 75 x 6.3e6/25 = %.3gM" % (2 * 75 * 6.3e6 / 25 / 1e6), "R", "reproduces; the post's last step writes 12.6e6/0.33 = 37.8M (0.33 is 1/3 rounded; exact 1/75 x 25 = 0.3333)")
    row("N02", "B5e", "Nesslig20", "mu_G = 75 'per haploid genome'", "if haploid events: %.0f per newborn (inside 98-206); SNV pedigree haploid %.1f (ratio %.2f); if zygote count: %.1fM" % (
        150, 38.4, 75 / 38.4, 2 * 37.5 * 252000 / 1e6), "P",
        "own definition is per haploid genome, own range '100 to 200 per generation' is not labelled; internally either reading is possible; a haploid-events value matches Hancock's 76 but then the "
        "comparator '31-62M SNVs' is an SNV count", material="yes if zygote-level (2x)")
    row("N03", "B5e", "Nesslig20", "1-2% = 31-62M SNVs", "%.0f-%.0fM" % (0.01 * 3.1e9 / 1e6, 0.02 * 3.1e9 / 1e6), "R", "")
    # N04
    qs = {}
    for target in (0.5, 0.95, 0.99, 0.999):
        lo_, hi_ = 0.3, 6.0
        for _ in range(80):
            mid = (lo_ + hi_) / 2
            if nesslig_cdf(mid) < target:
                lo_ = mid
            else:
                hi_ = mid
        qs[target] = 4 * (lo_ + hi_) / 2          # in units of Ne
    F4 = nesslig_cdf(1.0)
    # exact-WF check of the CDF at 2N = 1000 (Ne = 500)
    Mc, Wc = 1000, 130
    cum = wf_forward_fix_mass(Mc, Wc, 1, 8000)
    pfix_inf = cum[-1]
    chk = {}
    for xNe in (3.48, 4.0, 8.19, 11.41):
        t = int(round(xNe * Mc / 2))
        chk[xNe] = cum[t] / (1.0 / Mc)
    row("N04", "B5e", "Nesslig20", "50% at 3.48Ne; 60.6% at 4Ne; 95% at 8.19Ne; 99% at 11.41Ne; 99.9% at 16.01Ne",
        "series: 50%% at %.2fNe; %.1f%% at 4Ne; 95%% at %.2fNe; 99%% at %.2fNe; 99.9%% at %.2fNe; exact WF (2N=1000) F(3.48Ne)=%.3f F(4Ne)=%.3f F(8.19Ne)=%.3f F(11.41Ne)=%.3f" % (
            qs[0.5], 100 * F4, qs[0.95], qs[0.99], qs[0.999], chk[3.48], chk[4.0], chk[8.19], chk[11.41]), "R",
        "his CDF is the standard conditional fixation-time distribution; mean = 4Ne (telescoping series)")
    row("N05", "B5e", "Nesslig20", "constant rate reached after a lag of 4Ne", "lag = int(1-F) = 4Ne = 40,000 gens; applied: 2 x 75 x (252,000-40,000) = %.1fM (vs 37.8M)" % (2 * 75 * (252000 - 40000) / 1e6), "R",
        "his own plot reproduces Day's B1a subtraction; he sets it aside on the standing-variation ground (B1c), the same step Mansfield makes", material="no (he states it)")
    row("N06", "A2d", "Nesslig20", "444; 23; 0.0023; 0.0046; 37.8M", "20000/45 = %.0f; 13500/593 = %.1f; 1/444 = %.4f; 4.6e6 x 1e-9 = %.4f; 1/75 x 25 = %.4f" % (
        20000 / 45, 13500 / 593, 1 / 444, 4.6e6 * 1e-9, 25 / 75), "R", "reproduces; the Barrick citation year is printed '2019' where the link is the 2009 Nature paper (typo, fidelity only)")
    n_ = np.log(0.5) / np.log(1 - 1e-8)
    row("N07", "(none)", "Nesslig20", "69,314,717; 0.86; 0.98; 0.51", "n = %.0f; P(2e8) = %.4f; P(4e8) = %.4f; P(7e7) = %.4f" % (n_, 1 - (1 - 1e-8) ** 2e8, 1 - (1 - 1e-8) ** 4e8, 1 - (1 - 1e-8) ** 7e7), "R",
        "0.51 should read 0.50 (rounding); immaterial; lottery illustration, no claim file")
    row("N08", "A3x", "Nesslig20", "1.7%, 15.0%, 16.7%; 10 bp vs 2 mutations; 205M from ~14% of 3 Gbp", "1/60 = %.4f; 9/60 = %.2f; sum %.4f; 14%% x 3e9 = %.0fMbp; /2 = %.0fM" % (1 / 60, 9 / 60, 10 / 60, 0.14 * 3e9 / 1e6, 0.14 * 3e9 / 2e6), "R",
        "toy and reading of the 410 Mbp -> 205M step reproduce; supports A3x's unit point")
    row("N09", "(none)", "Nesslig20", "504 fused chromosomes; P_fix = 1/Ne = 0.00005", "1/500 x 6.3e6/25 = %.0f; 1/(2 x 1e4) = %.0e; 1/Ne would be %.0e" % (252000 / 500, 1 / 2e4, 1 / 1e4), "P",
        "arithmetic reproduces; symbol slip (1/Ne for 1/(2Ne)); and 1/500-625 is a birth PREVALENCE used as the new-mutation rate in k = mu (reductio only, immaterial to the argument)")
    row("N10", "H6", "Nesslig20", "300 generations per beneficial mutation", "30/0.1 = %.0f" % (30 / 0.1), "R", "Haldane; T_fix(p) -> 4Ne as p -> 0: %s" % sp.limit(-4 * sp.Symbol('Ne') * (1 - sp.Symbol('p')) / sp.Symbol('p') * sp.log(1 - sp.Symbol('p')), sp.Symbol('p'), 0))

    # ================================================================== Reddit and KITTENS
    row("R01", "B5f", "Dumb-and-Dumber", "~9.7M; gap under a factor of two", "38.4 x 252,000 = %.3gM; 17.5/9.68 = %.2f" % (38.4 * 252000 / 1e6, 17.5 / (38.4 * 252000 / 1e6)), "R", "reproduces")
    row("R02", "B5f", "Dumb-and-Dumber", "40,000-132,000 gens window", "(252,000-40,000) x 38.4 = %.2fM; (252,000-132,000) x 38.4 = %.2fM" % (212000 * 38.4 / 1e6, 120000 * 38.4 / 1e6), "R", "own 4Ne subtraction would lower the 9.7M he quotes (not applied); noted in claim file")
    row("R03", "A2h", "Dumb-and-Dumber", "3.2e9 x 1.2e-8 x 100 = 3,840, not 38,400", "%.0f" % (3.2e9 * 1.2e-8 * 100), "R", "CRITIC CORRECT; Day's s6.4 prints 38,400")
    if d3:
        row("R03f", "A2h", "Dumb-and-Dumber", "Day prints 38,400", "'approximately 38,400 mutations per' present=%s" % bool(re.search(r"approximately 38,400 mutations per", re.sub(r"\s+", " ", d3))), "R", "fidelity confirmed in raw Z23003785")
    mut = [110, 932, 803, 978, -906, 273, 1153]
    nonm = [64, 68, 0, 60, 35]
    row("R04", "A2c/E5", "Dumb-and-Dumber", "-906; Ara+5 38 -> 0", "mutator mean %.1f -> %.1f gen/fix; non-mutator %.1f -> %.1f gen/fix" % (
        sum(mut) / 7, 50000 / (sum(mut) / 7), sum(nonm) / 5, 60000 / (sum(nonm) / 5)), "R", "values exist in Day's tables; Day's own means reproduce; critic's quote accurate")
    row("R05", "A3a", "Fun-Friendship4898", "multiplying 187Mb by 2, then adding 35M SNVs", "2 x 187 + 35 = %.0fM (Day: 410M)" % (2 * 187 + 35), "R", "CRITIC CORRECT reconstruction of Day's total; Day's listed parts do not sum otherwise (A3a)")
    s_u = 38.4 / 4.1e-4
    row("K01", "A5b", "Sparky_6_4/KITTENS", "94,000 x 11.7 ~ 1.1M", "38.4/4.1e-4 = %.0f; 205/17.5 = %.3f; product %.4gM vs paper 1.075M (%.1f%% high)" % (s_u, 205 / 17.5, s_u * 205 / 17.5 / 1e6, 100 * (s_u * 205 / 17.5 / 1.075e6 - 1)), "R", "reproduces; rounding of F = 190.6 explains the 2%")
    row("K02", "A5b", "Sparky_6_4/KITTENS", "achievable 17.9M ~ 17.5M required", "191 x %.0f = %.2fM (190.6: %.2fM)" % (s_u, 191 * s_u / 1e6, 190.6 * s_u / 1e6), "R", "reproduces; linear scaling is flagged by the author as an illustration (RE-09)")
    row("K03", "A5b", "Sparky_6_4/KITTENS", "'shortfall = 94,000 x 11.7'", "paper SNV-only shortfall 17.5M/191 = %.0f (3.0 prints 91,600); 91,600 x 11.7 = %.3gM; ratio 94,000/91,600 = %.3f" % (17.5e6 / 191, 91600 * 11.714 / 1e6, 94000 / 91600), "P",
        "the decomposition is exact only if scaled achievable equals required (parity); the 2.6% difference is that parity gap; immaterial")
    d_ = read_text("day", "zenodo-23003785.txt")
    if d_:
        row("K03f", "A5b", "Sparky_6_4/KITTENS", "inputs in Day's paper", "4.1e-4 line: %s; '191' row: %s; '1,075,000' present: %s" % (
            bool(re.search(r"4\.1 × 10⁻⁴ per genome per generation", d_)), bool(re.search(r"1,322\s+191\s+1,075,000", d_)), "1,075,000" in d_), "R", "fidelity: inputs found in Z23003785")

    # ================================================================== Camestros
    row("C01", "(CA-06)", "Camestros", "1500/35 ~ 429", "15,000/35 = %.1f; 1,500/35 = %.1f" % (15000 / 35, 1500 / 35), "P", "numerator typo (extra digit missing); the result 429 is right; author hedges; immaterial, no claim file")
    row("C02", "(CA-01/02)", "Camestros", "F_max = t d /(g G_f); 'arithmetic isn't wrong'", "9e6 x 0.45/(20 x 1,600) = %.1f (Hossjer's 127)" % (9e6 * 0.45 / (20 * 1600)), "R", "CRITIC CORRECT credit: transcription and concession reproduce; also Hossjer's check")
    row("C03", "B6b", "Camestros", "all differences treated as post-split", "Day 2019: 15M + 15M = 30M; CSAC fixed share: %.1f-%.1fM of 35M (%.1f-%.1fM per lineage)" % (35 * .78, 35 * .86, 35 * .78 / 2, 35 * .86 / 2), "R", "accurate to Day 2019 text; qualitatively right (B4a quantifies)")

    # ================================================================== Hossjer
    F127 = 9e6 * 0.45 / (20 * 1600)
    row("J01", "A5a", "Hossjer", "127; 15,800; 10 million; factor 2", "%.2f; x125 = %.0f; x652 = %.2fM; 20/%.2f = %.2f" % (F127, F127 * 125, F127 * 125 * 3e9 / 4.6e6 / 1e6, F127 * 125 * 3e9 / 4.6e6 / 1e6, 20e6 / (F127 * 125 * 3e9 / 4.6e6)), "R", "reproduces; 125 x 127 = 15,875 vs printed 15,800 is rounding")
    row("J02", "A5a", "Hossjer", "three orders / five orders below 20M", "20e6/15,800 = %.0f; 20e6/127 = %.0f" % (20e6 / 15800, 20e6 / 127), "R", "")
    row("J03", "B5h", "Hossjer", "7.6M; ~10M 'very close'", "3e9 x 0.45 x 1.25e-8 x 450,000 = %.3gM; without d %.1fM; 20/7.59 = %.2f; G_neutral = 1/(4.6e6 x 1e-10) = %.0f" % (
        3e9 * .45 * 1.25e-8 * 450000 / 1e6, 3e9 * 1.25e-8 * 450000 / 1e6, 20 / (3e9 * .45 * 1.25e-8 * 450000 / 1e6), 1 / (4.6e6 * 1e-10)), "R",
        "arithmetic holds; the neutral count carries d = 0.45 in the mutation supply (the factor that accounts for most of the gap, A5a/B5h); 7.6M and 10M are called 'very close' (ratio 1.34)")
    row("J04", "H5", "Hossjer", "cost step 'in line with equation (3)' (15,800)", "450,000/300 = %.0f Haldane; 15,800/1,500 = %.1f; 650 vs 3e9/4.6e6 = %.0f" % (450000 / 300, 15800 / 1500, 3e9 / 4.6e6), "R",
        "arithmetic reproduces; internal non-sequitur (the 15,800 is a rate scaling, not a cost computation) stands [cf]")
    row("J05", "A5a", "Hossjer", "d = g_len/A = 0.45", "A = 20/0.45 = %.1f y" % (20 / 0.45), "R", "implied expected human age 44 y (not stated)")

    # ================================================================== Matev
    Mv = 40
    # exchangeable WF + sweepstakes model; solve absorption probabilities
    def sweep_P(Mv, eps, x):
        P = np.zeros((Mv + 1, Mv + 1))
        for i in range(Mv + 1):
            pi = i / Mv
            row_ = (1 - eps) * binom.pmf(np.arange(Mv + 1), Mv, pi)
            qm = x + (1 - x) * pi
            qw = (1 - x) * pi
            row_ = row_ + eps * (pi * binom.pmf(np.arange(Mv + 1), Mv, min(qm, 1.0)) + (1 - pi) * binom.pmf(np.arange(Mv + 1), Mv, qw))
            P[i] = row_
        return P
    def absorb(P):
        Mv = P.shape[0] - 1
        Q = P[1:Mv, 1:Mv]
        r = P[1:Mv, Mv]
        return np.linalg.solve(np.eye(Mv - 1) - Q, r)
    P_wf = sweep_P(Mv, 0.0, 0.0)
    P_sw = sweep_P(Mv, 0.4, 0.6)
    u_wf, u_sw = absorb(P_wf), absorb(P_sw)
    err_wf = np.max(np.abs(u_wf - np.arange(1, Mv) / Mv))
    err_sw = np.max(np.abs(u_sw - np.arange(1, Mv) / Mv))
    def var_ne(P, Mv, i):
        pm = i / Mv
        m = np.arange(Mv + 1) / Mv
        v = float(P[i] @ (m - pm) ** 2)
        return pm * (1 - pm) / v / 2          # Ne_var in diploid units: Var = p q / (2 Ne)
    row("V01", "B3i", "Matev", "sum over alleles of 1/(2Ne) = N/Ne > 1", "N/Ne for N = 1e6, Ne = 1e4: %d; exact chains (2N = %d): max|u - i/2N| WF %.1e, sweepstakes %.1e; Ne_var/N at p=.5: WF %.2f, sweep %.2f; sum_i u_i(1 copy) = %.12f" % (
        100, Mv, err_wf, err_sw, var_ne(P_wf, Mv, Mv // 2) / (Mv / 2), var_ne(P_sw, Mv, Mv // 2) / (Mv / 2), Mv * u_sw[0]), "R",
        "CRITIC CORRECT: absorption probability is exactly i/2N for exchangeable models whatever Ne; the 2N copies' probabilities must sum to 1")
    n_, p_ = 157000, 0.5
    row("V02", "G5", "Matev", "CV falls, variance rises with n", "Var = %.0f, sd = %.1f, CV = %.3f%%; at 2n: Var %.0f, CV %.3f%%" % (n_ * p_ * (1 - p_), math.sqrt(n_ * p_ * (1 - p_)), 100 * math.sqrt(n_ * p_ * (1 - p_)) / (n_ * p_),
                                                                                                          2 * n_ * p_ * (1 - p_), 100 * math.sqrt(2 * n_ * p_ * (1 - p_)) / (2 * n_ * p_)), "R", "CRITIC CORRECT (binomial)")
    row("V03", "B3e", "Matev", "'one over sixteen-billion'", "1/(2 x 8e9) = %.3g = 1/%.3g" % (1 / 1.6e10, 1.6e10), "R", "reproduces Day's use of census N = 8e9 in 1/(2N)")

    # ================================================================== keruru
    row("K-01", "B7c", "keruru", "P_fix = 1/(2N_census); sweepstakes same", "exact solves above: max error %.1e (WF), %.1e (sweepstakes, Ne_var/N = %.2f)" % (err_wf, err_sw, var_ne(P_sw, Mv, Mv // 2) / (Mv / 2)), "R",
        "CRITIC (former ally) CORRECT, retraction of k = (N/Ne) mu is right; code not retrieved but the claim is verified independently")
    Ne = 1e4
    row("K-02", "C5", "keruru", "0.6%; ~1 My; sd 0.05", "240/40,000 = %.3f; 40,000 x 25 y = %.1f My; sd = sqrt(.25 x 240/20000) = %.4f" % (240 / 40000, 40000 * 25 / 1e6, math.sqrt(.25 * 240 / 20000)), "R", "")
    # K-03: exact WF absorption, 2N = 20000, 240 gens
    M20, W20 = 20000, 700
    tt = time.time()
    store = (240,)
    out, _ = wf_backward(M20, W20, 240, store=store)
    u240 = out[240]
    def uat(p):
        return float(u240[int(round(p * M20))])
    # arcsine Gaussian references
    sig = math.sqrt(240 / (2 * Ne))
    def y(p):
        return 2 * math.asin(math.sqrt(p))
    def gauss_one(p):
        d = math.pi - y(p)
        return float(norm.sf(d / sig))
    def gauss_refl(p):
        return 2 * gauss_one(p)
    ps = [0.5, 0.1, 0.9, 0.95, 0.99]
    vals = {p: uat(p) for p in ps}
    refs = {p: gauss_refl(p) for p in ps}
    row("K-03a", "C5", "keruru", "4e-35 at p = 0.5", "exact WF %.3g (Gaussian one-boundary %.3g; reflection-doubled %.3g; repo 1.2e-46)" % (vals[0.5], gauss_one(0.5), gauss_refl(0.5)),
        "N" if not (1e-37 < vals[0.5] < 1e-33) else "R", "keruru's per-locus value is off by %.1f orders (too large); direction conservative" % (math.log10(4e-35 / vals[0.5]) if vals[0.5] > 0 else float('nan')), material="no (conclusion robust)")
    row("K-03b", "C5", "keruru", "6e-93 at p = 0.1", "exact WF %.3g (Gaussian %.3g)" % (vals[0.1], gauss_one(0.1)), "N" if not (1e-95 < vals[0.1] < 1e-90) else "R", "")
    row("K-03c", "C5", "keruru", "'only above ~0.99 any meaningful chance'", "exact WF: p=.9 %.3g; .95 %.3g; .99 %.3g" % (vals[0.9], vals[0.95], vals[0.99]), "R" if vals[0.99] > 1e-2 and vals[0.9] < 1e-6 else "P", "")
    ii = np.arange(M20 + 1) / M20
    n_loci = 1e6
    def expected(lo, hi):
        sel = (ii >= lo) & (ii <= hi)
        return n_loci * float(np.mean(u240[sel]))
    spec = {"all at 0.5": n_loci * vals[0.5], "uniform 0.1-0.5": expected(0.1, 0.5), "uniform 0.1-0.9": expected(0.1, 0.9),
            "uniform 0.1-0.99": expected(0.1, 0.99), "uniform 0.5-0.9": expected(0.5, 0.9)}
    row("K-03d", "C5", "keruru", "expected count ~1e-29 over a million loci 'from intermediate frequencies'", "; ".join("%s: %.2g" % (k_, v_) for k_, v_ in spec.items()),
        "N", "the figure equals 1e6 x 4e-35 (all loci at 0.5); with the exact value that is ~1e-40; any spectrum reaching 0.9 is dominated by its top edge; conclusion (zero is expected unless loci start above ~0.9) stands", material="no")
    row("K-04", "B4g", "keruru", "fossil-calibrated ~2x pedigree", "1.23%%/(2 x 252,000) = %.2e = %.2f x 1.2e-8; minus theta_anc 6.3e-3: %.2e" % (0.0123 / 504000, 0.0123 / 504000 / 1.2e-8, (0.0123 - 0.0063) / 504000), "R", "reproduces; the factor 2 disappears when the ancestral term is subtracted (B4a)")
    row("K-05", "C5b", "keruru", "Ne 8,139 (102 gens), 9,835 (250 gens)", "E[F] = 250/(2 x 9835) = %.4f; Ne = 2: %.1f (saturated)" % (250 / (2 * 9835), 250 / 4), "R", "arithmetic only; temporal estimator not re-run here (C1d)")
    row("K-06", "B2e", "keruru", "Wright ratio 4/(Vk+2) vs measured; 4Ne transits", "4/7 = %.3f; /8.1e-4 = %.0f; /6.9e-4 = %.0f; 4Ne/260,000 = %s%%" % (4 / 7, 4 / 7 / 8.1e-4, 4 / 7 / 6.9e-4, ", ".join("%.1f" % (400 * n / 260000) for n in (938, 6933, 8139, 9835))), "R", "reproduces")
    row("K-07", "B2e", "keruru", "ratio 1e-4 / 4e-4 / 8e-4 in one draft", "6,933/1e7 = %.1e; 8,139/1e7 = %.1e" % (6933 / 1e7, 8139 / 1e7), "P", "draft inconsistency (flagged '[CHECK]' by the author); not a conclusion-bearing error")

    # ================================================================== others
    row("G01", "G2a", "Ghijselen", "60,000 x 4 h; 27 y", "%.0f h = %.1f y" % (240000, 240000 / 24 / 365.25), "R", "reproduces; fidelity partial (analogy to a latency division, not to G_f)")
    row("G02", "G2b", "Duffy/Ghijselen", "180; 360", "252,000/1,400 = %.0f; 205e6/180 = %.0f (paper 1,139,000x)" % (252000 / 1400, 205e6 / 180), "R", "reproduces the book's 2nd-edition arithmetic")
    row("G03", "A4c", "Duffy", "25 generations at 80%", "1,600/25 = %.0f; 1,600/15.7 = %.0f; 1,600 x 0.45 = %.0f" % (1600 / 25, 1600 / 15.7, 1600 * .45), "P", "units and derivation not stated in the quote; not determinable; no verdict beyond fidelity unverifiable")
    row("G04", "G1b", "Samson", "total / time = average rate", "205e6/252,000 = %.0f; 17.5e6/252,000 = %.1f" % (205e6 / 252000, 17.5e6 / 252000), "R", "")
    row("G05", "ROOT-k", "Keen", "orders of magnitude beyond the age of the universe", "6.3e6 x 1.075e6 = %.3g y = %.0f x 13.8e9 y" % (6.3e6 * 1.075e6, 6.3e6 * 1.075e6 / 13.8e9), "R", "R only if the shortfall is read as a time multiplier at a fixed rate (A2e); preface gives no numbers; defers to Day")
    row("G06", "D14", "Davis (Eden)", "1e36 transfers", "1/(1e-15 x 1e-21) = %.0e; population 1e36/(1e12 x 1e-6) = %.0e; 1e13 t / 1e30 = %.0e g per cell; 1e16 kg/5.1e14 m2/1000 = %.3f m" % (
        1 / (1e-15 * 1e-21), 1e36 / (1e12 * 1e-6), 1e19 / 1e30, 1e16 / 5.1e14 / 1000), "P", "relays Eden's arithmetic correctly; 1e-11 g/cell is ~10x a typical E. coli (~1e-12 g); Eden's inputs are unsourced and he calls it 'very rough'")
    logp = 52143 * math.log10(1 / 1.4e8)
    row("G07", "D8", "Day (quoting Milton)", "1e-65 = winning the lottery every week for a thousand years with the same numbers", "52,143 weeks x log10(1/1.4e8) = 10^%.0f; 10^-65 is %.1f weeks of a 1-in-1.4e8 lottery; 20^50 = 10^%.2f" % (
        logp, 65 / math.log10(1.4e8), 50 * math.log10(20)), "N", "the analogy does not match the number by ~5 orders of magnitude of exponent; rhetorical, unattributed summary, immaterial to any calculation")
    u100 = (1 - math.exp(-2 * 0.01)) / (1 - math.exp(-4 * 100 * 0.01))
    row("G08", "F4", "Bowers (via Day)", "u ~ 2s", "Kimura u(N=100,s=.01) = %.5f; 2s = 0.02" % u100, "R", "CRITIC CORRECT (original not found; reposted by Day)")
    row("G09", "A2d", "Camestros/Duffy", "average, not the fastest", "1,322/78 = %.1f; 893/104.7 = %.1f; Ara-4 43 gens/fix" % (1322 / 78, 893 / 104.7), "R", "CRITIC CORRECT: Day's own table has faster LTEE rates")
    row("S01", "A3", "CSAC (read by Day, Hancock)", "~5M indel events vs ~35M substitutions", "two-lineage total per GAP-07/07b (measured 4.30M); not recomputed", "R", "resolved elsewhere; 40M = 35M + 5M total, 20M per lineage")
    print("elapsed %.0fs" % (time.time() - t0))
    os.makedirs(RAW, exist_ok=True)
    with open(os.path.join(RAW, "x1_results.json"), "w") as fh:
        json.dump(ROWS, fh, indent=1)
    cnt = {}
    for r in ROWS:
        cnt[r["outcome"]] = cnt.get(r["outcome"], 0) + 1
    print("outcome counts", cnt)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""M-303 record: neutral expectation for a locus starting at intermediate frequency, 240-350 generations, Ne ~ 1e4.

Object: docs/research/math/objects.yaml M-303 (formula, derivation). The record checks keruru's scale
arithmetic (4Ne = 40,000, 240/40,000 = 0.6%, drift SD sqrt(p q t/(2Ne)) = 0.0548 at p = 0.5), the
probability of fixation within t generations from p by two independent methods, and the readings of
the observed counts against them:
- diffusion limit: Kimura's spectral series u(p, t) = p + sum_i (2i+1) p q (-1)^i F(1-i, i+2; 2; p)
  exp(-i(i+1) t/(4Ne)), in exact rationals (F) and 250-digit decimals (the sum cancels to 1e-45 and
  below). F = P_{i-1}^(1,1)(1-2p)/i with |P_n^(1,1)| <= n+1 on [-1, 1], so |F| <= 1 and the tail
  after I terms is below sum_{i>I} (2i+1) p q exp(-i(i+1) t/(4Ne)); the record asserts that bound.
- exact Wright-Fisher chain at 2N = 20,000: backward recursion u_{t+1}(i) = sum_j P(i -> j) u_t(j)
  over a band |j - i| <= W (a full 20,001^2 matrix does not fit the local limit). Two vectors run
  together: the band alone gives a lower bound; an upper bound adds the dropped mass with Chernoff
  bounds, using that u_t(j) is increasing in j (the binomial chain is stochastically monotone):
  dropped j in (i+W, i+2W] at most u_t(i+2W), j > i+2W at most 1, j < i-W at most u_t(i). The record
  asserts the bracket width. Floating-point rounding (sums of nonnegative terms, lgamma-based pmf with
  ~1e-11 relative error per entry) is far below the asserted 3 significant figures.
The 0.04-0.11 expected 50-90% completions are the R4 C1 chain result (a simulation with the panel's
start spectrum, M-301's domain); the record cites them and asserts their Poisson consequences. Inputs
carry their quote id, claim file or result file; held() checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-303.py [--write]   (about 10 s, under 400 MB)
Without --write it checks that M-303.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys
from decimal import Decimal, getcontext
from fractions import Fraction

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
C, C5, C5A, C7 = (CL + f for f in ("C-adna-zero-fixations.md", "C5-keruru-neutral-zero.md",
                                   "C5a-day-ne-circularity.md", "C7-no-drift-last-7000-years.md"))
R4C1 = "research/checks/results/R4-B3b-C1.md"
X1 = "research/checks/results/R4-X1-critic-arithmetic.md"


def held(rel, quote):
    """The quote, checked verbatim (whitespace-normalised) against a held file."""
    norm = lambda s: " ".join(s.split())
    assert norm(quote) in norm((ROOT / rel).read_text(encoding="utf-8")), (rel, quote[:60])
    return quote


def near(x, target, tol):
    assert abs(x - target) <= tol, (x, target, tol)
    return x


def rel(x, target, tol):
    assert abs(x / target - 1) <= tol, (x, target, tol)
    return x


def g(x):
    return float(f"{x:.6g}")


def finish(rec):
    rec = {"id": HERE.stem, "date": DATE, "script": f"docs/research/math/records/{HERE.name}",
           "script_sha256": hashlib.sha256(HERE.read_bytes()).hexdigest(), **rec}
    out = json.dumps(rec, indent=2, ensure_ascii=False) + "\n"
    js = HERE.with_suffix(".json")
    if "--write" in sys.argv:
        js.write_text(out, encoding="utf-8")
    elif js.exists():
        assert js.read_text(encoding="utf-8") == out, f"{js.name} is stale; rerun with --write"
    print(f"{HERE.stem}: all asserts pass")


# ---- diffusion limit (Kimura spectral series) -----------------------------------------------
getcontext().prec = 250
TERMS = 300


def hyp(i, p):
    """F(1-i, i+2; 2; p), a polynomial of degree i-1, in exact rationals."""
    s, t = Fraction(0), Fraction(1)
    for k in range(i):
        s += t
        t = t * (1 - i + k) * (i + 2 + k) / ((2 + k) * (k + 1)) * p
    return s


COEF = {}
for p in (Fraction(1, 2), Fraction(1, 10)):
    fs = [hyp(i, p) for i in range(1, TERMS + 1)]
    assert max(abs(f) for f in fs) <= 1                 # |F| <= 1 (Jacobi bound)
    COEF[p] = [(2 * i + 1) * p * (1 - p) * (-1) ** i * f for i, f in zip(range(1, TERMS + 1), fs)]


def dec(q):
    return Decimal(q.numerator) / Decimal(q.denominator)


def diffusion(p, t, four_ne):
    x = Decimal(t) / Decimal(four_ne)
    tail = sum((2 * i + 1) * dec(p * (1 - p)) * (-Decimal(i * (i + 1)) * x).exp() for i in range(TERMS + 1, TERMS + 200))
    assert tail < Decimal("1e-150"), tail                # series truncation bound
    u = dec(p) + sum(dec(c) * (-Decimal(i * (i + 1)) * x).exp() for i, c in enumerate(COEF[p], 1))
    assert u > 0
    return float(u)


# ---- exact Wright-Fisher, banded, bracketed ------------------------------------------------
def wf_bracket(M, W, T, starts, at=()):
    """Lower and upper bounds on P(fixed within t generations | start i) for t in `at` and T."""
    n, B = M + 1, 2 * W + 1
    lg = np.array([math.lgamma(k + 1) for k in range(M + 1)])
    band = np.zeros((n, B))
    for s in range(1, M, 2000):
        e = min(M, s + 2000)
        i = np.arange(s, e)[:, None]
        j = i + np.arange(-W, W + 1)[None, :]
        ok = (j >= 0) & (j <= M)
        jj = np.where(ok, j, 0)
        lp = lg[M] - lg[jj] - lg[M - jj] + jj * np.log(i / M) + (M - jj) * np.log1p(-i / M)
        band[s:e] = np.where(ok, np.exp(lp), 0.0)
    band[0, W] = band[M, W] = 1.0
    i = np.arange(1, M)
    p = i / M

    def chernoff(k):                                     # P(X >= k) (k > i) or P(X <= k) (k < i), X ~ Bin(M, p)
        a = np.clip(k / M, 0.0, 1.0)
        with np.errstate(divide="ignore", invalid="ignore"):
            kl = np.where(a > 0, a * np.log(a / p), 0.0) + np.where(a < 1, (1 - a) * np.log((1 - a) / (1 - p)), 0.0)
        return np.where((k > M) | (k < 0), 0.0, np.exp(-M * kl))

    c1, c2, c3 = np.zeros(n), np.zeros(n), np.zeros(n)
    c1[1:M], c2[1:M], c3[1:M] = chernoff(i + W + 1), chernoff(i + 2 * W + 1), chernoff(i - W - 1)
    top = np.minimum(np.arange(n) + 2 * W, M)
    lo, up = np.zeros(n + 2 * W), np.zeros(n + 2 * W)
    lo[W + M] = up[W + M] = 1.0
    out = {}
    for t in range(1, T + 1):
        vl = np.einsum("ib,ib->i", band, sliding_window_view(lo, B))
        vu = np.einsum("ib,ib->i", band, sliding_window_view(up, B))
        cur = up[W:W + n]
        vu = np.minimum(vu + c1 * cur[top] + c2 + c3 * cur, 1.0)
        vl[0] = vu[0] = 0.0
        vl[M] = vu[M] = 1.0
        lo[W:W + n], up[W:W + n] = vl, vu
        if t in at or t == T:
            out[t] = {s0: (float(lo[W + s0]), float(up[W + s0])) for s0 in starts}
    return out


# ---- inputs -------------------------------------------------------------------------------
CQ3 = held(C, "Across 1.14 million autosomal loci and 7,000 years of European prehistory, zero alleles moved from below "
              "50% starting frequency to regional fixation, and zero moved from below 10% to fixation, in either run.")
KR03 = held(C5, "Integrated across a million loci starting from intermediate frequencies, the expected number of "
                "fixations is somewhere near 10⁻²⁹.")
C5Q2 = held(C5, "Finding zero is not a coin landing on its edge. Finding one would have been the falsification.")
KR04 = held(C5, "The claim about the substitution rate is withdrawn. The claim about the ancient-DNA finding is withdrawn.")
SCALE = held(C5, "4Ne = 40,000 generations; at 25 y/gen = 1.0M y; 240/40,000 = 0.6% of the way (keruru: \"six-tenths "
                 "of one percent\"); derived: holds.")
SD = held(C5, "Drift SD at p = 0.5 over t generations = sqrt(p q t/(2Ne)) = sqrt(0.25 x 240/20,000) = 0.0548 (keruru: "
              "\"about 0.05\"); derived: holds.")
KR35 = held(C5, "Fixation within 240 generations from p = 0.5 (keruru: \"around 4 x 10^-35\").")
CORR = held(C5, "the exact Wright-Fisher chain at 2N = 20,000 over 240 generations gives 5.1e-45 from p = 0.5 (the repo's "
                "1.2e-46 is 41x low), and the diffusion limit (Kimura spectral series) gives 1.8e-45 (14x low).")
X1ROW = held(X1, "**Both published values reproduce by the diffusion at 2N = 15,364 (p = 0.5) and 2N = 16,278 = 2 x 8,139 "
                 "(p = 0.1)**")
X1TOP = held(X1, "At 0.9: 3.7e-8; 0.95: 2.2e-4; 0.99: 0.19")
C5AQ2 = held(C5A, "has rs35619459 moving 29.3% → 91.3%, a twelve-sigma excursion against his own stated expectation")
C5ASE = held(C5A, "sqrt(0.293 x 0.707/2,744 + 0.913 x 0.087/1,360) = 0.0116, i.e. 54 SE")
C7Q1 = held(C7, "And we've now got hard evidence that genetic drift isn't happening at all over the last 7000 years, and "
                "that there is a hard population limit on the neutral pipeline.")
C7P = held(C7, "the count itself is supported (P about 1e-17 for a fixation from p0 = 0.5 in 280 generations)")
R4C1ROW = held(R4C1, "**Observed 50-90% completions (1 and 3):** expected 0.04 (v62) and 0.11 (v66) at Ne=1e4; they equal "
                     "expectation at Ne ~7,000 (1.55 / 2.76); at Ne=5,000 expected 22.")

ne = 10_000                                              # parameters population.Ne_modern_human (unverified; M-211)
M = 2 * ne
T_kr, T_c, T_day = 240, 280, 350                         # keruru (6,000 y / 25); 7,000 y / 25; 7,000 y / 20

# ---- scale arithmetic (keruru) --------------------------------------------------------------
assert 4 * ne == 40_000
near(T_kr / (4 * ne), 0.006, 1e-12)                      # "six-tenths of one percent"
sd = {t: math.sqrt(0.25 * t / (2 * ne)) for t in (T_kr, T_c, T_day)}
near(sd[T_kr], 0.0548, 0.00005)                          # C5 "0.0548" (keruru "about 0.05")

# ---- diffusion limit --------------------------------------------------------------------------
half, tenth = Fraction(1, 2), Fraction(1, 10)
d50 = diffusion(half, T_kr, 4 * ne)
rel(d50, 1.789e-45, 0.001)                               # "1.8e-45"
d10 = diffusion(tenth, T_kr, 4 * ne)
rel(d10, 5.82e-114, 0.002)                               # R4 X1 "5.8e-114"
kr50 = diffusion(half, T_kr, 2 * 15_364)                 # keruru's 4e-35 at 2N = 15,364
rel(kr50, 4.0e-35, 0.01)
kr10 = diffusion(tenth, T_kr, 2 * 16_278)                # keruru's 6e-93 at 2N = 16,278 = 2 x 8,139 (C5b Ne)
rel(kr10, 6.0e-93, 0.01)
near(1e6 * 4e-35, 4e-29, 1e-40)                          # "somewhere near 10^-29" = 1e6 x 4e-35 (order)

# ---- exact Wright-Fisher, 2N = 20,000 ------------------------------------------------------
W = 650
starts = {0.1: M // 10, 0.5: M // 2, 0.9: 9 * M // 10, 0.95: 19 * M // 20, 0.99: 99 * M // 100}
wf = wf_bracket(M, W, T_c, tuple(starts.values()), at=(T_kr,))
lo50, up50 = wf[T_kr][starts[0.5]]
assert up50 / lo50 - 1 < 1e-8                            # truncation bracket at p = 0.5
rel(lo50, 5.119e-45, 0.0005)                             # "5.1e-45"
lo10, up10 = wf[T_kr][starts[0.1]]
rel(lo10, 5.88e-113, 0.002)                              # R4 X1 "5.9e-113" (lower bound; the upper bound is loose)
assert up10 < 1e-80
top_vals = {}
for q, printed in ((0.9, 3.7e-8), (0.95, 2.2e-4), (0.99, 0.19)):
    lo_q, up_q = wf[T_kr][starts[q]]
    assert up_q / lo_q - 1 < 1e-8
    assert float(f"{lo_q:.2g}") == printed, (q, lo_q)    # R4 X1 "3.7e-8; 2.2e-4; 0.19" (2 significant figures)
    top_vals[q] = lo_q
lo280, up280 = wf[T_c][starts[0.5]]
assert up280 / lo280 - 1 < 1e-8
rel(lo280, 9.416e-39, 0.0005)                            # 280 generations (C7's window)
assert up280 <= 1e-17                                    # C7 "about 1e-17" holds as an upper bound ...
near(math.log10(1e-17 / lo280), 21.03, 0.01)             # ... and is 21 orders above the exact value
lo90_280 = wf[T_c][starts[0.9]][0]
rel(lo90_280, 4.19e-7, 0.002)

# ---- the audit's earlier Brownian figure, against both ----------------------------------------
z = (math.pi / 2) / math.sqrt(T_kr / (2 * ne))           # arcsine coordinate, distance pi/2, variance 1/(2Ne) per gen
near(z, 14.34, 0.005)
repo = math.erfc(z / math.sqrt(2))                       # reflection-doubled one-sided Gaussian tail
rel(repo, 1.24e-46, 0.01)
near(lo50 / repo, 41, 0.5)                               # "41x low"
near(d50 / repo, 14.4, 0.1)                              # "14x low"
near(math.log10(4e-35 / lo50), 9.9, 0.05)                # keruru's per-locus figure is ~10 orders above exact at Ne = 1e4
near(1e6 * lo50 / 1e-39, 5.12, 0.01)                     # all of a million loci at 0.5: 5.1e-39

# ---- the 50-90% band (R4 C1 chain, cited) and its Poisson tails ------------------------------------
exp62, exp66 = 0.04, 0.11
p_ge1 = 1 - math.exp(-exp62)
near(p_ge1, 0.0392, 0.0001)                              # P(>= 1 | 0.04): v62's one completion
p_ge3 = 1 - math.exp(-exp66) * (1 + exp66 + exp66 ** 2 / 2)
rel(p_ge3, 2.0e-4, 0.03)                                 # "P(>=3 | 0.11) = 2e-4"

# ---- rs35619459 against the same SD -----------------------------------------------------------
dp = 0.913 - 0.293
near(dp, 0.620, 1e-12)
near(dp / 0.05, 12.4, 1e-9)                              # Day's "twelve-sigma" on keruru's "about 0.05"
near(dp / sd[T_kr], 11.32, 0.005)                        # 11.3 at the exact SD 0.0548
near(dp / math.sqrt(0.293 * 0.707 * 240 / (2 * ne)), 12.44, 0.01)  # SD at the locus's own start, p = 0.293
se = math.sqrt(0.293 * 0.707 / 2_744 + 0.913 * 0.087 / 1_360)
near(se, 0.0116, 0.00005)
near(dp / se, 53.6, 0.1)                                 # "54 SE": not sampling noise
near(dp / sd[T_day], 9.37, 0.01)                         # over Day's 350 generations the same move is 9.4 SD

finish({
    "object": "M-303",
    "inputs": [
        {"name": "Ne, 2N", "value": [ne, M], "cite": "parameters population.Ne_modern_human (unverified; circularity is M-211)"},
        {"name": "window", "value": {"keruru": T_kr, "C7_25y": T_c, "day_20y": T_day}, "cite": "C5 Formal statement; C7; claim file C"},
        {"name": "keruru per-locus and million-locus figures", "value": {"per_locus_p0.5": 4e-35, "million_loci": "near 1e-29"},
         "cite": "C5 q1 (KR-03); C5 Formal statement"},
        {"name": "zero counts", "value": "0 from <50%, 0 from <10%", "cite": "C q3 (Q53)"},
        {"name": "50-90% expected completions", "value": {"v62": exp62, "v66": exp66}, "cite": "R4-B3b-C1.md (exact WF chain, panel spectrum; M-301 domain)"},
        {"name": "rs35619459", "value": {"from": 0.293, "to": 0.913, "n": [1_372, 680]}, "cite": "C5a q2"},
        {"name": "C7 fixation probability", "value": "about 1e-17 at p0 = 0.5, 280 generations", "cite": "C7 verdict comment (R4 RHclose, Gaussian upper bound)"},
    ],
    "values": {
        "four_Ne": 4 * ne, "window_over_4Ne": 0.006, "drift_sd": {str(k): g(v) for k, v in sd.items()},
        "diffusion_Ne_1e4_t240": {"p0.5": g(d50), "p0.1": g(d10)},
        "diffusion_keruru_2N": {"p0.5_2N_15364": g(kr50), "p0.1_2N_16278": g(kr10)},
        "exact_wf_2N_20000_t240": {"p0.5": [g(lo50), g(up50)], "p0.1_lower": g(lo10),
                                   **{f"p{q}": g(v) for q, v in top_vals.items()}},
        "exact_wf_2N_20000_t280": {"p0.5": [g(lo280), g(up280)], "p0.9": g(lo90_280)},
        "band_W": W,
        "repo_brownian_1.2e-46": {"value": g(repo), "exact_over": g(lo50 / repo), "diffusion_over": g(d50 / repo)},
        "million_loci_at_0.5": g(1e6 * lo50),
        "poisson_50_90": {"P_ge1_given_0.04": g(p_ge1), "P_ge3_given_0.11": g(p_ge3)},
        "rs35619459": {"dp": 0.62, "sigma_at_0.05": 12.4, "sigma_at_0.0548": g(dp / sd[T_kr]),
                       "sigma_at_own_start": g(dp / math.sqrt(0.293 * 0.707 * 240 / (2 * ne))),
                       "sampling_se": g(se), "in_se": g(dp / se), "sigma_350_gens": g(dp / sd[T_day])},
    },
    "not_checked_locally": [],
    "positions": {
        "day": {"reading": "zero from intermediate frequency shows drift is not operating (C7); rs35619459 is a "
                           "twelve-sigma excursion (C5a)",
                "rs35619459_sigma": [12.4, g(dp / sd[T_kr])], "not_sampling_noise_in_se": g(dp / se),
                "note": "the excursion arithmetic holds (11.3-12.4 SD by convention, 54 SE); the zero count is what "
                        "drift predicts, so it carries no evidence against drift (values above)"},
        "critic": {"reading": "zero is the neutral prediction (keruru C5; R4 L5)",
                   "p_fix_p0.5_t240_exact": g(lo50), "keruru_per_locus_printed": 4e-35,
                   "note": "keruru's 4e-35 is ~10 orders above the exact value at Ne = 1e4 and reproduces only by "
                           "diffusion at 2N = 15,364; the conclusion holds at any of these values. Observed 1 and 3 "
                           "50-90% completions are above the 0.04 / 0.11 expectation (P(>=3) = 2e-4)"},
    },
    "notes": "Exact WF at 2N = 20,000 gives 5.119e-45 from p = 0.5 in 240 generations (bracket width < 1e-8 relative), "
             "diffusion limit 1.789e-45; the audit's old 1.24e-46 is 41x / 14x low; keruru's 4e-35 is not reproduced "
             "at Ne = 1e4. At 280 generations the exact value is 9.4e-39: C7's 'about 1e-17' is a valid upper bound "
             "but 21 orders above. A large single-locus excursion is real (54 SE) and 11.3-12.4 drift SD; whether one "
             "locus in 1.14M at that size is drift, admixture or selection is outside this object (linkage, M-301).",
})

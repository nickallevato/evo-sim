"""B2 (and B, rule N): internal check of Hard Limits (Z22129121, Day & Athos, 2026-08-27) against its own text.

Tier: LOAD-BEARING (B2 and B are ROOT-path nodes in docs/research/R5-draft.md; three reviews).  Exact
discrete Wright-Fisher chain with 2N = 200 gene copies (201 states, dense matrix, < 2 s, < 100 MB): fits the
AGENTS.md "trivial" limit, so it runs locally.  Pre-registered: this docstring is committed before the first run.

TARGET CLAIMS: B2 (internal pending, fidelity unverifiable: "which probability is meant" was open, R5-draft),
B (internal pending: does "neutral theory cannot rescue" follow from B2 by Day's own material?), B2a (exponent).

VERBATIM QUOTES (sources/raw/day/zenodo-22129121.txt; line numbers of the local extracted text)
  H1 (abstract, l.6-8)   "Kimura's neutral substitution rate, k = μ, is a steady-state identity: it holds only
                          after a population has held one size for the roughly 4N ₑ generations"
  H2 (l.287)             "k(T) = μ · F(T),      F(T) = P(τ ≤ T | fixation)"
  H3 (l.301)             "F(T) ∼ exp( − π² Nₑ / T ),           T ≪ 4Nₑ"
  H4 (l.304-308)         "Run six hundred thousand neutral Wright– / Fisher populations of two hundred genes ...
                          391 generations against a predicted 4Nₑ of 400 ... some seven hundred fifty fixations;
                          six do. Not one of the three thousand / fixes in under nineteen percent of the mean."
  H5 (l.329-331)         "Nₑ/T ≈ 1.8 × 10⁷ ... exp(−π² · 1.8 × 10⁷) — about one in ten to the seventy-eight-
                          millionth"
  H6 (l.124-126)         "Nₑ = (4N − 2) / (Vₖ + 2)" ... "X = (Vₖ + 2) · G / 16"
  H7 (l.353-360)         "The small number of fixations we / observe are just drainage: the completions of
                          mutations that entered the pipe long ago, / when the populations were small"
  H8 (l.364-366)         "a census near a hundred thousand held static for the / full two million years, and even
                          the generous linear bound T/4Nₑ stands at about thirty- / five percent"
  H9 (l.52-56)           "A population of 10,000 is roughly where drift permanently stops for an animal like us
                          ... It / is also, not by accident, the size the field's own methods assign to the ancestral
                          human / population."
  H10 (l.206-207)        "There is no census at which a large vertebrate is / simultaneously large enough to be a
                          viable species and small enough to fix a neutral / allele by drift."
  Abstract statement under audit (B2): "The domain of k = μ is confined to demographic conditions that no
                          non-endangered species is capable of meeting."  (B claim: "neutral theory ... is
                          flat-out wrong", blog 2026-02-04 para 60; the HL abstract sentence is B's second quote.)

WHAT EACH SIDE PREDICTS
  Day side: F is the conditional (per destined allele) probability; its short-time tail is exponentially thin;
    the WF demonstration (six of ~3,000 within a quarter of the mean, none under 19%) is what the exact chain
    gives; the human exponent is ~1e-78,000,000; X follows from 4N_e < G by algebra; so k = mu cannot be
    realised at current size for any large vertebrate.
  Critic side (B2a review; Mansfield; McCarthy): F(T) is a per-allele latency tail, not a throughput bound;
    at steady state flux is mu regardless of transit (which HL itself concedes, l.265-270); the pipe was
    filled by the ancestral population, so the observed substitutions are expected (drainage); the prefactor
    of the asymptotic law is off by orders of magnitude.

THIS AUDIT'S PREDICTIONS
  P1  Fidelity of the definition: H2 is found verbatim; it settles the reading as Reading 1 (conditional on
      fixation), so B2a's Reading-1 comparison applies.
  P2  Day's WF demonstration (2N = 200, N_e = 100, ~3,000 fixations): the exact conditional mean fixation time
      from one copy is in [395, 400] (Day's simulated 391 within 2.5%); the exact expected number of the 3,000
      fixing by t = 100 (a quarter of 4N_e) is in [2, 20], and Day's "six" lies inside its Poisson 95% range;
      the expected number fixing by t = 74 (19% of 391) is < 3, consistent with "not one".  -> holds.
  P3  The asymptotic law H3 understates the exact F at moderate T: at T = N_e, exact F / exp(-pi^2 N_e/T) is
      in [3, 1000]; the ratio grows as T/N_e falls (prefactor, not exponent).  R1: immaterial to H5, whose
      exponent is 1.8e7 (a power-law prefactor shifts log10 F by < 1e3 against 7.8e7).
  P4  H5 arithmetic: N_e/T = 7.3e9/400 = 1.825e7; pi^2 x 1.825e7 / ln 10 = 7.82e7 decimal orders, within 2% of
      "seventy-eight-millionth".  -> holds.
  P5  H6 algebra: 4 N_e < G with N_e = (4N-2)/(V_k+2) gives N < (V_k+2) G/16 + 1/2 exactly; the dropped 1/2 is
      immaterial (R1).  -> holds.
  P6  H8 arithmetic (Day's own best case: census 1e5, V_k = 5 (HL Table 1 human), 2 My, 25 y): N_e = 57,143,
      G = 80,000, T/4N_e = 0.35 ("thirty-five percent").  The exact conditional F at T/N_e = 1.4 (computed in
      the same chain at T = 140, N_e = 100) is in [0.05, 0.30]: below the linear bound (Day's "generous" holds)
      and >= 50x Day's own asymptotic exp(-pi^2 N_e/T) (8.7e-4), i.e. near the ceiling the pipe substantially
      fills (HL says so, l.361-363).
  P7  Rule N (scored for B, not B2): by HL's own material (H7, H8, H9) the observed human-lineage substitutions
      are "drainage" from an ancestral population near 1e4, where the pipe "substantially fills" (F of order
      0.05-0.35 per destined allele over the window, before any pre-window fill).  So HL's own text does not
      support "neutral theory cannot account for the observed differences" for the human lineage: what it
      shows is that CURRENT-size seeding contributes nothing.  Prediction: B2's abstract sentence holds under
      rule C read as a statement about current-size seeding (internal holds); B's step from B2 to "neutral
      theory cannot rescue the shortfall" is a NON-SEQUITUR against HL's own drainage paragraph, unless Day
      supplies a computed ancestral fill showing drainage below the required count (none in HL; B1c, external,
      found an excess under every tested history).  H9 with H10 is also scored: Day places ancestral humans at
      the ceiling (1e4) and says no viable large vertebrate can sit at it; under rule C ("non-endangered") both
      can hold if the ancestral population is read as endangered; recorded, not scored as an error.
What would change a verdict: P2 failing (Day's demonstration not reproduced by the exact chain) would be a
Day-side slip (ledger unless it moves H5: it cannot); P6/P7 failing (exact F near the ceiling ~ exp law, i.e.
the pipe does not fill even at N_e ~ T) would remove the rule-N finding for B.
"""
import math
import os
import sys

import numpy as np
from scipy.stats import binom

HERE = os.path.dirname(os.path.abspath(__file__))
HL = os.path.join(HERE, "..", "..", "sources", "raw", "day", "zenodo-22129121.txt")
TWO_N = 200
NE = TWO_N // 2


def cond_fix_cdf(two_n, tmax):
    """F(t) = P(fixed by t | eventual fixation) from one copy, exact WF (unconditional mass at 2N times 2N)."""
    i = np.arange(two_n + 1)
    P = binom.pmf(i[None, :], two_n, i[:, None] / two_n)
    v = np.zeros(two_n + 1)
    v[1] = 1.0
    F = np.zeros(tmax + 1)
    for t in range(1, tmax + 1):
        v = v @ P
        F[t] = v[two_n] * two_n
    return F


def main():
    ok = True
    txt = open(HL, encoding="utf-8").read()
    flat = " ".join(txt.split())
    print("## P1 definition")
    h2 = "k(T) = μ · F(T), F(T) = P(τ ≤ T | fixation)"
    p1 = h2 in flat
    print(f"H2 found (whitespace-normalised): {p1}")
    for q in ("F(T) ∼ exp( − π² Nₑ / T ), T ≪ 4Nₑ", "391 generations against a predicted 4Nₑ of 400",
              "The small number of fixations we observe are just drainage",
              "the generous linear bound T/4Nₑ stands at about thirty- five percent",
              "A population of 10,000 is roughly where drift permanently stops for an animal like us",
              "There is no census at which a large vertebrate is simultaneously large enough to be a viable species"):
        print(f"  quote found: {q in flat} | {q[:70]}")
        ok &= q in flat
    ok &= p1

    print("\n## P2 Day's WF demonstration (2N = 200)")
    tmax = 6000
    F = cond_fix_cdf(TWO_N, tmax)
    mean = float(np.sum(1 - F[:tmax]))
    nfix = 600000 / TWO_N
    e100 = F[100] * nfix
    e74 = F[74] * nfix
    lo, hi = (max(0.0, e100 - 1.96 * math.sqrt(e100)), e100 + 1.96 * math.sqrt(e100))
    print(f"tail mass left at t={tmax}: {1 - F[tmax]:.2e}")
    print(f"exact conditional mean = {mean:.1f} (pred [395, 400]; Day sim 391, diff {100 * (mean - 391) / mean:.1f}%)")
    print(f"expected fixations by t=100 of {nfix:.0f}: {e100:.2f} (pred [2, 20]); Poisson 95% ~[{lo:.1f}, {hi:.1f}]; Day 6 inside: {lo <= 6 <= hi}")
    print(f"expected by t=74: {e74:.3f} (pred < 3; Day 'not one')")
    p2 = 395 <= mean <= 400 and abs(mean - 391) / mean <= 0.025 and 2 <= e100 <= 20 and lo <= 6 <= hi and e74 < 3
    print(f"P2: {p2}")
    ok &= p2

    print("\n## P3 asymptotic law vs exact")
    for tt in (25, 50, 100, 200):
        ex = math.exp(-math.pi ** 2 * NE / tt)
        print(f"T/Ne={tt / NE:.2f}: exact F={F[tt]:.3e}; exp(-pi^2 Ne/T)={ex:.3e}; ratio {F[tt] / ex:.3g}")
    r100 = F[100] / math.exp(-math.pi ** 2)
    print(f"P3 ratio at T=Ne in [3, 1000]: {3 <= r100 <= 1000}; grows as T/Ne falls: {F[50] / math.exp(-math.pi ** 2 * 2) > r100}")
    ok &= 3 <= r100 <= 1000

    print("\n## P4 human exponent")
    x = 7.3e9 / 400
    dec = math.pi ** 2 * x / math.log(10)
    print(f"Ne/T = {x:.4g}; decimal orders = {dec:.4g} (Day 7.8e7): {abs(dec - 7.8e7) / 7.8e7 < 0.02}")
    ok &= abs(dec - 7.8e7) / 7.8e7 < 0.02

    print("\n## P5 X algebra")
    for Vk, G in ((5, 260000), (2, 80000)):
        Nstar = (Vk + 2) * G / 16 + 0.5
        ne = (4 * Nstar - 2) / (Vk + 2)
        print(f"Vk={Vk}, G={G}: N* = {Nstar:.1f}; 4Ne(N*) = {4 * ne:.1f} (= G: {abs(4 * ne - G) < 1e-6}); X = {(Vk + 2) * G / 16:.1f}")
        ok &= abs(4 * ne - G) < 1e-6

    print("\n## P6 Day's best-case hominid (census 1e5, Vk 5, 2 My, 25 y)")
    ne = (4e5 - 2) / 7
    G = 2e6 / 25
    lin = G / (4 * ne)
    ratio = G / ne
    t = int(round(ratio * NE))
    ex = math.exp(-math.pi ** 2 / ratio)
    print(f"Ne = {ne:.0f}; G = {G:.0f}; T/4Ne = {lin:.3f} (Day 'about thirty-five percent'); T/Ne = {ratio:.3f}")
    print(f"exact conditional F at T/Ne = {t / NE:.2f} (chain T={t}): {F[t]:.4f} (pred [0.05, 0.30]); "
          f"below linear {lin:.3f}: {F[t] < lin}; exp law {ex:.2e}; exact/exp = {F[t] / ex:.0f} (pred >= 50)")
    p6 = abs(lin - 0.35) < 0.02 and 0.05 <= F[t] <= 0.30 and F[t] < lin and F[t] / ex >= 50
    print(f"P6: {p6}")
    ok &= p6

    print("\n## P7 rule N (B): see write-up; inputs printed above (H7 drainage, H8 best case, H9 ancestral 1e4)")
    for ne_anc, yrs in ((1e4, 2e6), (1e4, 6.5e6), (2.5e4, 6.5e6)):
        rr = (yrs / 25) / ne_anc
        tt = int(round(rr * NE))
        fv = F[tt] if tt <= tmax else float("nan")
        print(f"  ancestral Ne={ne_anc:g} over {yrs / 1e6:g} My at 25 y: T/Ne = {rr:.1f}; exact F = {fv:.4f}")
    print(f"\nALL MECHANICAL PREDICTIONS (P1-P6) MET: {ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

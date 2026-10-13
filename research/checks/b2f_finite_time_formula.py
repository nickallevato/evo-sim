"""R4 B2f: the "closed-form finite-time completion fraction" F(T) = exp(-pi^2 N_e / T) added on 2026-10-13
to Zenodo 22903977 (retitled "k != mu: The Finite-Time Collapse of Neutral Substitution Theory").

PRE-REGISTRATION.  Everything in this docstring was written before the script was run.  Disclosure
(for PREREG-STATUS): the source texts were read before registration, and B2's reviewed numbers were known
(R4-B2.md: exact/exp = 47.4 at T = N_e, 17.8 at 2N_e; F = 0.6063 and delivered 0.2009 at T = 4N_e).
Bands below were set from hand arithmetic and from those values, not from any run of this script.  So
T1-T6 are textual facts to be verified (not predictions), P2's two B2 values and P3's x = 4 row are
reproductions, and P7 and P6a are identities that can fail only through a bug (non-severe).  The parts
with something at stake are P1, P2's closed prefactor, P3 at x = 25.2 and 5.04, P4, P5 and P6b-c.
Does not redo B2 (Hard Limits internal: exponent, WF demonstration, human arithmetic).

SOURCES (untrusted data, read only; gitignored)
  NEW  sources/raw/refresh-2026-10-13/zenodo-22903977-new/new.txt  (pdftotext of k_neq_mu.pdf,
       md5 739634e97a80c8f9d0d31d125544b94c; record modified 2026-10-13T15:07:16Z)
  OLD  sources/raw/refresh-2026-10-13/zenodo-22903977-new/old.txt  (pdftotext of Kimura.pdf,
       md5 e325def9ecd74611e6e75f1befcc788f, 2026-09-22)
  HL   sources/raw/day/zenodo-22129121.txt  (Day & Athos, "Hard Limits", 2026-08-27)

TARGET QUOTES (verbatim; whitespace normalised)
  Q286 (NEW s1, Chalub paragraph, sentence 3): "Day and Athos (2026b) extract the dominant eigenvalue of
       that expansion via diffusion asymptotics in the arcsine-transformed coordinate system, converting
       Chalub's abstract series into the closed-form finite-time completion fraction F(T) = exp(−π²Nₑ/T) —
       the proportion of theoretically destined fixations that actually complete within T generations."
  Q31  (HL l.296-301): "F(T) ∼ exp( − π² Nₑ / T ), T ≪ 4Nₑ"
  Passages without a Q id (for integration to file; quotes files not edited here):
  N1 (NEW s1, same paragraph, sentence 4): "Multiplied through the mutation supply, this yields the
       time-dependent substitution rate k(T) = μ·F(T), which replaces the steady-state identity with a
       function that drops exponentially with effective population size (Day and Athos 2026b)."
  N2 (NEW s1, sentences 5-6; recorded under Q286 as "following sentence"): "The steady state requires
       infinite time. It therefore cannot be utilized in any finite-time equation, and every application
       of k = μ to a finite-time calculation is guaranteed to be incorrect."
  N3 (NEW References): "Day, V. and Athos, C. (2026b). The Hard Limits of Fixation Through Genetic Drift.
       Zenodo. https://zenodo.org/records/22903977."
  N4 (NEW s3, unchanged from OLD): "For the human-chimpanzee application, T = 252,000 generations and 4Nₑ
       = 40,000, giving T/4Nₑ ≈ 6.3 — comfortably in the regime where the approximation holds."
  N5 (OLD s1, removed in NEW): "The steady state is the destination; it is not the journey, and it is not
       the starting point. Every finite-time application of k = μ treats the destination as though it
       were the departure."
  N6 (HL l.296-299): "under the transform that turns neutral drift into a symmetric random walk, the
       distance from a single copy to fixation is a fixed length, π√(2Nₑ), and the chance of covering it
       in time T is the short-time first-passage law"
  N7 (NEW s2, unchanged): "t̄ = 4Nₑ generations This is the mean time to fixation for a neutral mutation,
       conditional on fixation."
  Numbers the paper states near or downstream of the formula (all in unchanged text; Q34, Q36, B1a):
  T = 252,000 generations; N_e = 10,000 / 50,000 / 63,000 (4N_e = 40,000 / 200,000 / 252,000);
  T/4N_e ~ 6.3; "Net loss" 15.9% / 79.4% / 100% from E[F(T)] ~ mu L (T - 4N_e).
  NO number in NEW is derived from F(T) = exp(-pi^2 N_e/T) (textual fact T6, verified below by listing
  every occurrence of "F(T)" and "exp" in NEW).

WHAT IS TESTED
  x = T/N_e.  Exact object (same as HL's and B2's): F(x) = P(tau <= T | fixation), one new neutral copy,
  Kimura (1955) diffusion, p -> 0:  F(x) = 1 + sum_{i>=1} (-1)^i (2i+1) exp(-i(i+1) x/4).
  Audit derivation written before the run (Jacobi theta_1' modular identity applied to that series):
     F(x) = (4 pi/x)^{3/2} e^{x/16} sum_{n>=0} (-1)^n (2n+1) exp(-pi^2 (2n+1)^2 / x)
  so the exact short-time law is F ~ (4 pi N_e/T)^{3/2} exp(-pi^2 N_e/T): the exponent is Day's, the
  prefactor is (4 pi/x)^{3/2} e^{x/16}.  The two series are evaluated independently (decimal, 160 digits,
  and float) and must agree.  The long-time law from the dominant (i = 1) eigenvalue is 1 - 3 exp(-x/2).
  Closed form under test: C(x) = exp(-pi^2/x).

EACH SIDE'S PREDICTION (stated before any computation here)
  Day side: (D1) F(T) = exp(-pi^2 N_e/T) is the finite-time completion fraction of the neutral diffusion:
     the exponent is right and the form is usable as a closed form; (D2) k(T) = mu F(T) falls
     exponentially with N_e; (D3) k = mu is reached only as T -> infinity, so a finite-time count from
     k = mu is wrong; (D4) the paper's stated numbers (15.9 / 79.4 / 100% loss at T = 252,000) stand
     beside the formula without conflict.
  Critic side: (K1) exp(-pi^2 N_e/T) is HL's short-time asymptote (T << 4N_e) with its domain and its
     prefactor dropped; it is not a closed form and not the dominant-eigenvalue term, which governs
     long times; at the paper's own T/N_e (25.2, 5.04, 4) it is far from the exact F; (K2) taken as an
     equality it contradicts the paper's own t-bar = 4N_e and its own 15.9%; (K3) F(T) is the
     first-passage law of one new mutation from an empty pipe; from standing variation at
     mutation-drift equilibrium the substitution flux is mu at every finite T, so "every application
     ... guaranteed to be incorrect" does not follow.

TEXTUAL FACTS TO VERIFY (not scored as predictions; read before registration)
  T1 Q286, N1, N2, N3, N4, N7 are in NEW; Q286, N1, N3 are not in OLD; N5 is in OLD, not in NEW; N4, N7 in OLD.
  T2 Q31 and N6 are in HL; HL contains none of "Chalub", "eigenvalue", "arcsine", "Gegenbauer".
  T3 NEW contains no "≪" and no "∼": the domain T << 4N_e and the asymptotic sign are absent.
  T4 Same object: NEW defines F as the proportion of destined fixations completing within T generations
     and k(T) = mu F(T); HL l.287 has "k(T) = μ · F(T), F(T) = P(τ ≤ T | fixation)".  T in generations in
     both; N_e the diploid effective size in both (HL distance pi sqrt(2N_e): 2N_e gene copies).
  T5 N3's URL is this record's own id (22903977); HL is Zenodo 22129121.
  T6 "F(T)" occurs in NEW only in Q286/N1 and in E[F(T)] (a different F: the expected count);
     "exp(" occurs once.

AUDIT PREDICTIONS (bands fixed here)
  P1 Exponent.  E(x) = -d ln F_exact / d(1/x) is below pi^2 and within 1% of pi^2 at x = 0.05, within 5%
     at x = 0.25, within 16% at x = 1.  [Day side D1 (exponent), same finding as B2 by a different route.]
  P2 Prefactor.  F_exact/C > 1 at every grid x in [0.05, 60] and decreases monotonically in x; it equals
     (4 pi/x)^{3/2} e^{x/16} within 1% for x <= 2; values 47.4 (x = 1) and 17.8 (x = 2) reproduce B2
     within 1%.  [Critic side K1: C understates F everywhere; no x where it is exact.]
  P3 At the paper's own inputs, T = 252,000: x = 25.2, 5.04, 4.0 (N_e = 1e4, 5e4, 6.3e4):
     F_exact in [0.9999, 1], [0.70, 0.82], [0.59, 0.62]; C = 0.676, 0.141, 0.085 (each +-2%);
     C is more than 25% below F_exact at all three.  [Critic K1.  Day-side hit instead if C is within
     25% of exact at one or more of the three.]
  P4 C is within 25% of F_exact only for x >= x*, with x* in [40, 48] (T/4N_e >= 10 to 12); at x* the
     deficit ratio (1 - C)/(1 - F_exact) exceeds 1e6.
  P5 Dominant eigenvalue.  1 - 3 exp(-x/2) is within 1% of F_exact for x >= 8 and is negative below
     x = 2 ln 3 = 2.197; at x = 25.2, (1 - C)/(1 - F_exact) > 1e4.  So C is not the dominant-eigenvalue
     term of the expansion.  [Critic K1 on the description.  Day-side hit instead if C tracks the
     eigenvalue term within 25% anywhere on x >= 8 in deficit terms (1 - C vs 1 - F).]
  P6 Consistency with the paper's own s2-s4.
     (a) exact mean = int_0^inf (1 - F) dx = 4.000 +- 0.1% (N_e units) [identity, N7];  C taken as a CDF has
         no finite mean: int_0^X (1 - C) dx grows by pi^2 ln 10 = 22.73 +- 5% per decade of X between
         1e3 and 1e4 and between 1e4 and 1e5.
     (b) loss 1 - (1/T) int_0^T F at N_e = 1e4 (x = 25.2): exact in [15.5, 16.5]% (paper: 15.9%, Day-side
         hit D4 for the unchanged text); with C in [55, 67]%.
     (c) N_e = 5e4 (x = 5.04): exact [65, 75]%, C [93, 98]% (paper 79.4%); N_e = 6.3e4 (x = 4): exact
         [79, 81]%, C [96, 99]% (paper 100%).  The paper-vs-exact gap in (c) is B1a's (re-confirmation,
         no new verdict); new here is the C column.
  P7 Steady-state flux (exact WF chain, 2N = 200, N_e = 100, infinite sites, 2N mu new copies per
     generation, cond_fix_cdf reused from b2_hard_limits_internal.py).  Stationary start: flux/mu = 1
     within 1e-9 at T = 1, 100, 400, 504, 2520.  Empty start: flux/mu = chain F(T), within 5% of the
     diffusion F at x = 4, 5.04, 25.2.  [Identity; shows what K3 and D3 each rest on: the start state.]

WHAT COUNTS FOR EACH SIDE
  Day side: P1 hit (exponent exact in the limit); N1 "drops exponentially with effective population
     size" true of both C and the exact short-time law; D3 true for an empty start (F_exact < 1 at every
     finite T; P7 empty-start row); P6b exact row reproduces the paper's 15.9%.
  Critic side: P2-P5 hits (C is HL's asymptote without its domain; wrong by > 25% at every input the
     paper uses; not the eigenvalue term); P6a-c C columns (C contradicts t-bar = 4N_e and 15.9%); P7
     stationary row (k = mu exact at finite T from equilibrium).
  A miss in either direction is reported with the same weight as a hit.

VERDICT MAPPING (rule file R4-X1-verdict-rule.md; proposals only, decided at integration)
  RH: Q286, N1, N2 dialectic (equation, definition, stated consequence).
  Internal, Q286 + N1 (rule RD, both readings recorded):
    Reading A (rule C): "closed-form ... F(T) = exp" is a relay of HL's F(T) ∼ exp, T ≪ 4N_e, cited to HL.
       P1 hit -> `holds`; the dropped "∼" and domain are a slip.  R1: no number in NEW is derived from C
       (T6), and N2 needs only F < 1, so the correction moves no stated number or conclusion -> ledger.
    Reading B (literal): an equality valid at any T, including the paper's own T/4N_e ~ 6.3 (N4).
       P3 and P6 hits -> `non-sequitur` (N2a: the paper's own inputs in its own formula give other values
       than its own s4; N2b: needs a fixation-time law without the finite mean its own s2 states).
       P3 miss (C within 25% at the paper's inputs) -> `holds` under both readings.
    The verdict field takes the reading under which the quoted statement is most defensible (RD).
  Internal, N2 ("guaranteed to be incorrect"):
    (i) counts from an empty pipe: `holds` if F_exact < 1 at every finite T (size reported).
    (ii) every application, whatever the start state: P7 stationary row -> stronger than the premises
       (N2d); but the start state is scored at B1 / B1c / B6a (N1: a premise dispute is external), so no
       new internal verdict is proposed from (ii).
  Fidelity (self-citation of HL as "Day and Athos 2026b"; Chalub part stays with B1e, not checked here):
    `accurate` if HL states a closed form by the eigenvalue route; `partial` if T2-T3 hold (cited, read
    with an omission: domain and "∼" dropped, derivation described differently); `misread` on Reading B
    (HL's own text restricts the law to T ≪ 4N_e and the paper sits at T/4N_e ~ 6.3).
  External: exponent `supported` (P1); equality at T >~ N_e `contradicted` (P3, P4; mathematics, not
    data); N2 as a statement about real lineages `contested` (start state: B1, B1c, B6a).
  Tier: low-stakes unless integration adopts Reading B for B1's source (B1 is load-bearing); flagged in
    the write-up.

Run: research/.venv/bin/python -I research/checks/b2f_finite_time_formula.py   (local; < 1 min, < 500 MB)
Outputs: research/checks/results/raw/b2f.out (stdout), b2f.json
"""
import importlib.util
import json
import math
import os
import sys
from decimal import Decimal as D, getcontext

import numpy as np
from scipy.integrate import quad
from scipy.special import exp1

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
NEW = os.path.join(ROOT, "sources", "raw", "refresh-2026-10-13", "zenodo-22903977-new", "new.txt")
OLD = os.path.join(ROOT, "sources", "raw", "refresh-2026-10-13", "zenodo-22903977-new", "old.txt")
HL = os.path.join(ROOT, "sources", "raw", "day", "zenodo-22129121.txt")
PI2 = math.pi ** 2
getcontext().prec = 160
DPI = D("3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651")

Q286 = ("Day and Athos (2026b) extract the dominant eigenvalue of that expansion via diffusion asymptotics in the "
        "arcsine-transformed coordinate system, converting Chalub's abstract series into the closed-form finite-time "
        "completion fraction F(T) = exp(−π²Nₑ/T) — the proportion of theoretically destined fixations that actually "
        "complete within T generations.")
N1 = ("Multiplied through the mutation supply, this yields the time-dependent substitution rate k(T) = μ·F(T), which "
      "replaces the steady-state identity with a function that drops exponentially with effective population size "
      "(Day and Athos 2026b).")
N2 = ("The steady state requires infinite time. It therefore cannot be utilized in any finite-time equation, and every "
      "application of k = μ to a finite-time calculation is guaranteed to be incorrect.")
N3 = ("Day, V. and Athos, C. (2026b). The Hard Limits of Fixation Through Genetic Drift. Zenodo. "
      "https://zenodo.org/records/22903977.")
N4 = ("For the human-chimpanzee application, T = 252,000 generations and 4Nₑ = 40,000, giving T/4Nₑ ≈ 6.3 — "
      "comfortably in the regime where the approximation holds.")
N5 = ("The steady state is the destination; it is not the journey, and it is not the starting point. Every finite-time "
      "application of k = μ treats the destination as though it were the departure.")
N6 = ("under the transform that turns neutral drift into a symmetric random walk, the distance from a single copy to "
      "fixation is a fixed length, π√(2Nₑ), and the chance of covering it in time T is the short-time first-passage law")
N7 = "t̄ = 4Nₑ generations This is the mean time to fixation for a neutral mutation, conditional on fixation."
Q31 = "F(T) ∼ exp( − π² Nₑ / T ), T ≪ 4Nₑ"
HL_DEF = "k(T) = μ · F(T), F(T) = P(τ ≤ T | fixation)"


def flat(path):
    return " ".join(open(path, encoding="utf-8").read().split())


def F_dec(x):
    """Exact diffusion F, eigen-series, 160-digit decimal. x = T/N_e (float or str)."""
    x = D(str(x))
    s = D(1)
    for i in range(1, 100000):
        t = (D(-i * (i + 1)) * x / 4).exp()
        s += (-1) ** i * (2 * i + 1) * t
        if t < D("1e-150"):
            break
    return s


def F_short(x, nmax=60):
    """Same F by the modular (short-time) series, float."""
    s = sum((-1) ** n * (2 * n + 1) * math.exp(-PI2 * (2 * n + 1) ** 2 / x) for n in range(nmax))
    return (4 * math.pi / x) ** 1.5 * math.exp(x / 16) * s


def F_long(x, nmax=400):
    return 1 + sum((-1) ** i * (2 * i + 1) * math.exp(-i * (i + 1) * x / 4) for i in range(1, nmax))


def F(x):
    """Float F: short-time series below x = 6, eigen-series above (each converges fast on its side)."""
    if x <= 0:
        return 0.0
    return F_short(x) if x < 6 else F_long(x)


def C(x):
    return math.exp(-PI2 / x) if x > 0 else 0.0


def E_local(x, h=1e-4):
    a, b = D(str(x * (1 - h))), D(str(x * (1 + h)))
    return float(-(F_dec(a).ln() - F_dec(b).ln()) / (1 / a - 1 / b))


def int_F(x):
    """int_0^x F du (float quadrature, split at 6)."""
    pts = [p for p in (0.5, 2.0, 6.0) if p < x]
    return quad(F, 0, x, points=pts or None, limit=400, epsabs=1e-13, epsrel=1e-12)[0]


def int_C(x):
    """int_0^x exp(-pi^2/u) du = x [e^{-z} - z E1(z)], z = pi^2/x."""
    z = PI2 / x
    return x * (math.exp(-z) - z * exp1(z))


def main():
    out = {}
    ok = {}

    print("## Textual facts T1-T6 (verification, not predictions)")
    if all(os.path.exists(p) for p in (NEW, OLD, HL)):
        new, old, hl = flat(NEW), flat(OLD), flat(HL)
        t1 = {"Q286 in NEW": Q286 in new, "N1 in NEW": N1 in new, "N2 in NEW": N2 in new, "N3 in NEW": N3 in new,
              "N4 in NEW": N4 in new, "N7 in NEW": N7 in new, "Q286 not in OLD": Q286 not in old,
              "N1 not in OLD": N1 not in old, "N3 not in OLD": N3 not in old, "N2 not in OLD": N2 not in old,
              "N5 in OLD": N5 in old, "N5 not in NEW": N5 not in new, "N4 in OLD": N4 in old, "N7 in OLD": N7 in old}
        t2 = {"Q31 in HL": Q31 in hl, "N6 in HL": N6 in hl, "HL def (l.287) in HL": HL_DEF in hl}
        for w in ("Chalub", "eigenvalue", "arcsine", "Gegenbauer"):
            t2[f"HL lacks '{w}'"] = w.lower() not in hl.lower()
        t3 = {"NEW lacks '≪'": "≪" not in new, "NEW lacks '∼'": "∼" not in new, "NEW lacks '<<'": "<<" not in new}
        t5 = {"N3 URL is 22903977 (own record)": "records/22903977" in N3 and N3 in new}
        nF, nE, nexp = new.count("F(T)"), new.count("E[F(T)]"), new.count("exp(")
        t6 = {f"'F(T)' count {nF}, of which 'E[F(T)]' {nE}, bare {nF - nE} (expected bare 2)": nF - nE == 2,
              f"'exp(' count {nexp} (expected 1)": nexp == 1}
        for name, grp in (("T1", t1), ("T2/T4", t2), ("T3", t3), ("T5", t5), ("T6", t6)):
            for k, v in grp.items():
                print(f"  {name}: {k}: {v}")
            ok[name] = all(grp.values())
        print("  note T1: N2 (the two sentences) is new text; OLD had N5 in its place.")
        out["text"] = {"T1": t1, "T2": t2, "T3": t3, "T5": t5, "T6": t6}
    else:
        print("  raw texts not present: textual checks skipped")

    print("\n## Cross-check of the two exact series (decimal eigen-series vs float modular series)")
    worst = 0.0
    for x in (0.05, 0.1, 0.25, 0.5, 1, 2, 4, 5.04, 6, 8, 12, 25.2, 60):
        a, b, c = float(F_dec(x)), F_short(x), F(x)
        rel = abs(a - b) / a
        worst = max(worst, rel, abs(a - c) / a)
        print(f"  x={x:<6} F_dec={a:.10e} F_modular={b:.10e} rel.diff={rel:.1e}")
    ok["series agree"] = worst < 1e-9
    print(f"  worst relative difference {worst:.1e} (need < 1e-9): {ok['series agree']}")

    print("\n## P1 exponent: E(x) = -d ln F / d(1/x) against pi^2 = %.4f" % PI2)
    p1 = {}
    for x, band in ((0.05, 0.01), (0.25, 0.05), (1.0, 0.16)):
        e = E_local(x)
        p1[x] = (e, e < PI2 and abs(e - PI2) / PI2 <= band)
        print(f"  x={x}: E={e:.4f} ({100 * (e - PI2) / PI2:+.2f}%; band {100 * band:.0f}%, below pi^2): {p1[x][1]}"
              f"   [analytic pi^2 - 1.5x + x^2/16 = {PI2 - 1.5 * x + x * x / 16:.4f}]")
    ok["P1"] = all(v[1] for v in p1.values())
    out["P1"] = {str(k): v[0] for k, v in p1.items()}

    print("\n## P2 prefactor: F_exact / exp(-pi^2/x)")
    grid = [0.05, 0.1, 0.25, 0.5, 1, 1.4, 2, 3, 4, 5.04, 6, 8, 10.4, 12, 16, 20, 25.2, 30, 40, 50, 60]
    ratios = []
    print("  | x = T/N_e | T/4N_e | F_exact | C = exp(-pi^2/x) | F/C | (4pi/x)^1.5 e^(x/16) | 1 - 3e^(-x/2) |")
    for x in grid:
        f = float(F_dec(x))
        r = float(F_dec(x) / (-(DPI ** 2) / D(str(x))).exp())
        pref = (4 * math.pi / x) ** 1.5 * math.exp(x / 16)
        ratios.append(r)
        print(f"  | {x} | {x / 4:.3f} | {f:.6e} | {C(x):.6e} | {r:.4g} | {pref:.4g} | {1 - 3 * math.exp(-x / 2):.6f} |")
    mono = all(a > b for a, b in zip(ratios, ratios[1:]))
    gt1 = all(r > 1 for r in ratios)
    pref_ok = all(abs(r / ((4 * math.pi / x) ** 1.5 * math.exp(x / 16)) - 1) < 0.01 for x, r in zip(grid, ratios) if x <= 2)
    r1, r2 = ratios[grid.index(1)], ratios[grid.index(2)]
    b2_ok = abs(r1 / 47.4 - 1) < 0.01 and abs(r2 / 17.8 - 1) < 0.01
    print(f"  ratio > 1 everywhere: {gt1}; monotone decreasing: {mono}; closed prefactor within 1% for x<=2: {pref_ok}; "
          f"B2 values 47.4/17.8 reproduced ({r1:.2f}, {r2:.2f}): {b2_ok}")
    ok["P2"] = mono and gt1 and pref_ok and b2_ok
    out["P2"] = {"grid": grid, "ratio": ratios, "gt1": gt1, "monotone": mono, "prefactor_1pct": pref_ok, "b2": b2_ok}

    print("\n## P3 at the paper's own inputs (T = 252,000 generations)")
    p3 = []
    spec = ((10000, (0.9999, 1.0), 0.676), (50000, (0.70, 0.82), 0.141), (63000, (0.59, 0.62), 0.085))
    for ne, (lo, hi), cpred in spec:
        x = 252000 / ne
        f, c = F(x), C(x)
        short = 1 - c / f
        hit = lo <= f <= hi and abs(c / cpred - 1) <= 0.02 and short > 0.25
        p3.append(hit)
        print(f"  N_e={ne}: x={x:.2f}, T/4N_e={x / 4:.2f}; F_exact={f:.6f} (band [{lo}, {hi}]: {lo <= f <= hi}); "
              f"C={c:.4f} (pred {cpred} +-2%: {abs(c / cpred - 1) <= 0.02}); C below exact by {100 * short:.1f}% (>25%: {short > 0.25}); "
              f"deficit 1-F={1 - f:.3e}, 1-C={1 - c:.3f}")
        out.setdefault("P3", []).append({"Ne": ne, "x": x, "F": f, "C": c, "shortfall": short, "hit": hit})
    ok["P3"] = all(p3)

    print("\n## P4 where C is within 25% of exact")
    lo, hi = 10.0, 200.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if F_long(mid) / C(mid) > 1.25:
            lo = mid
        else:
            hi = mid
    xs = hi
    dr = (1 - C(xs)) / float(1 - F_dec(xs))
    below = all(float(F_dec(x)) / C(x) > 1.25 for x in grid if x < xs)
    ok["P4"] = 40 <= xs <= 48 and dr > 1e6 and below
    print(f"  x* = {xs:.2f} (T/4N_e = {xs / 4:.2f}); band [40, 48]: {40 <= xs <= 48}; every grid x < x* is outside 25%: {below}; "
          f"deficit ratio (1-C)/(1-F) at x* = {dr:.3e} (> 1e6: {dr > 1e6})")
    lo, hi = 2.0, 60.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if F(mid) / C(mid) > 3:
            lo = mid
        else:
            hi = mid
    print(f"  (reported, no band) C within a factor 3 of exact for x >= {hi:.2f}")
    out["P4"] = {"xstar": xs, "deficit_ratio": dr, "x_factor3": hi}

    print("\n## P5 dominant-eigenvalue term 1 - 3 exp(-x/2)")
    p5a = all(abs((1 - 3 * math.exp(-x / 2)) / F(x) - 1) < 0.01 for x in grid if x >= 8)
    p5b = (1 - 3 * math.exp(-2.19 / 2)) < 0 < (1 - 3 * math.exp(-2.2 / 2))
    d252 = (1 - C(25.2)) / float(1 - F_dec(25.2))
    track = [x for x in grid if x >= 8 and abs((1 - C(x)) / float(1 - F_dec(x)) - 1) < 0.25]
    ok["P5"] = p5a and p5b and d252 > 1e4 and not track
    print(f"  eigen term within 1% of exact for all grid x >= 8: {p5a}; negative below x = 2 ln 3: {p5b}")
    print(f"  at x = 25.2: (1-C)/(1-F) = {d252:.3e} (> 1e4: {d252 > 1e4}); grid x >= 8 where 1-C is within 25% of 1-F: {track}")
    for x in (8, 12, 25.2, 60):
        print(f"    x={x}: 1-F_exact={float(1 - F_dec(x)):.3e}  3e^(-x/2)={3 * math.exp(-x / 2):.3e}  1-C={1 - C(x):.3e}")
    out["P5"] = {"eig_1pct": p5a, "neg": p5b, "deficit_ratio_25.2": d252}

    print("\n## P6 consistency with the paper's own s2-s4")
    mean_exact = quad(lambda u: 1 - F(u), 0, 200, points=[0.5, 2, 6, 20], limit=400)[0]
    p6a1 = abs(mean_exact / 4 - 1) < 1e-3
    part = {X: X - int_C(X) for X in (1e3, 1e4, 1e5)}
    g1, g2 = part[1e4] - part[1e3], part[1e5] - part[1e4]
    tgt = PI2 * math.log(10)
    p6a2 = abs(g1 / tgt - 1) < 0.05 and abs(g2 / tgt - 1) < 0.05
    print(f"  (a) exact mean fixation time = {mean_exact:.6f} N_e (4.000 +-0.1%): {p6a1}")
    print(f"      C as a CDF: int_0^X (1-C) = {part[1e3]:.2f}, {part[1e4]:.2f}, {part[1e5]:.2f} N_e at X = 1e3, 1e4, 1e5; "
          f"growth per decade {g1:.2f}, {g2:.2f} (pi^2 ln 10 = {tgt:.2f} +-5%): {p6a2}  -> no finite mean")
    rows = []
    hits = []
    print("  | N_e | x | paper loss % | exact loss % | C loss % | paper's T-4N_e loss % |")
    for ne, paper, eb, cb in ((10000, 15.9, (15.5, 16.5), (55, 67)), (50000, 79.4, (65, 75), (93, 98)),
                              (63000, 100.0, (79, 81), (96, 99))):
        x = 252000 / ne
        le, lc = 100 * (1 - int_F(x) / x), 100 * (1 - int_C(x) / x)
        h = eb[0] <= le <= eb[1] and cb[0] <= lc <= cb[1]
        hits.append(h)
        rows.append({"Ne": ne, "x": x, "paper": paper, "exact": le, "C": lc, "hit": h})
        print(f"  | {ne} | {x:.2f} | {paper} | {le:.2f} (band {eb}: {eb[0] <= le <= eb[1]}) | {lc:.2f} (band {cb}: {cb[0] <= lc <= cb[1]}) "
              f"| {100 * min(1.0, 4 / x):.2f} |")
    ok["P6a"] = p6a1 and p6a2
    ok["P6b"] = hits[0]
    ok["P6c"] = hits[1] and hits[2]
    out["P6"] = {"mean_exact": mean_exact, "C_partial": {str(k): v for k, v in part.items()}, "rows": rows}

    print("\n## P7 steady-state flux, exact WF chain 2N = 200 (N_e = 100), infinite sites, input 2N mu copies/generation")
    spec_ = importlib.util.spec_from_file_location("b2", os.path.join(HERE, "b2_hard_limits_internal.py"))
    b2 = importlib.util.module_from_spec(spec_)
    spec_.loader.exec_module(b2)
    two_n, ne, tmax = 200, 100, 2520
    Fc = b2.cond_fix_cdf(two_n, tmax)
    from scipy.stats import binom
    i = np.arange(two_n + 1)
    P = binom.pmf(i[None, :], two_n, i[:, None] / two_n)
    Qm, r = P[1:two_n, 1:two_n], P[1:two_n, two_n]
    e1 = np.zeros(two_n - 1)
    e1[0] = two_n  # 2N mu new copies per generation, mu = 1
    phi_stat = np.linalg.solve((np.eye(two_n - 1) - Qm).T, e1)
    phi_s, phi_e = phi_stat.copy(), e1.copy()
    cum_s = cum_e = 0.0
    p7 = True
    print("  | T | x | stationary-start flux/mu | empty-start flux/mu | chain F(T) | diffusion F(x) | stationary count/(mu T) | empty count/(mu T) |")
    for t in range(1, tmax + 1):
        fs, fe = float(phi_s @ r), float(phi_e @ r)
        cum_s += fs
        cum_e += fe
        if t in (1, 100, 400, 504, 2520):
            x = t / ne
            fd = F(x)
            good = abs(fs - 1) < 1e-9 and abs(fe - Fc[t]) < 1e-9
            if t >= 400:
                good &= abs(Fc[t] / fd - 1) < 0.05
            p7 &= good
            print(f"  | {t} | {x:.2f} | {fs:.12f} | {fe:.6e} | {Fc[t]:.6e} | {fd:.6e} | {cum_s / t:.9f} | {cum_e / t:.6f} | {good}")
            out.setdefault("P7", []).append({"T": t, "stat": fs, "empty": fe, "chainF": float(Fc[t]), "diffF": fd,
                                             "cum_stat": cum_s / t, "cum_empty": cum_e / t})
        phi_s = phi_s @ Qm + e1
        phi_e = phi_e @ Qm + e1
    ok["P7"] = p7
    print(f"  segregating copies-classes at stationarity (sum phi / 2N mu) = {phi_stat.sum() / two_n:.2f} sites per unit mu")

    print("\n## Summary")
    for k, v in ok.items():
        print(f"  {k}: {'HIT' if v else 'MISS'}")
    out["ok"] = {k: bool(v) for k, v in ok.items()}
    rawdir = os.path.join(HERE, "results", "raw")
    with open(os.path.join(rawdir, "b2f.json"), "w") as fh:
        json.dump(out, fh, indent=1, default=float)
    return 0


if __name__ == "__main__":
    sys.exit(main())

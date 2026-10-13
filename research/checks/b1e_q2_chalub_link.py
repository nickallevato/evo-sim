"""R4 B1e-Q2: B1e's second Statement quote (the 1/(2N) blog sentence of 2026-08-23) and the Kimura (1955) link.

Brief: research/checks/briefs/B1e-Q2-analyst.md (lead Big Sim, 2026-10-13).  Claim: B1e
(docs/research/claims/B1e-chalub-2022-reading.md; not load-bearing).  Tier: low-stakes, one combined
review REVIEW-R4-B1e-Q2-combined.md, unless the escalation clause below fires.

PRE-REGISTRATION.  Everything in this docstring was written before the main run.  Disclosure (for
PREREG-STATUS; label expected: criterion-only): both source texts were read in full before registration;
P4 (flux identity), P7's coefficient identity and P1s (a slip in Chalub's Appendix) were derived by hand
before registration, so they are checks of hand algebra by an independent numerical route, not blind
predictions; P6c's Wright-Fisher band was informed by B2f's P7 (chain 2N = 200 within 1.2% of the
diffusion at x >= 4; R4-B2f.md).  The Moran and beta-binomial bands of P6c were set by no run.  Smokes ran
before commit with every computed value and every hit/miss call suppressed; only assertions, run time and
memory were seen (RESOURCES below).  What the smokes changed, all before commit: mpmath's hypergeometric
Gegenbauer failed to converge, so C_n^alpha is the three-term recurrence (cross-checked against scipy, asserted);
the beta-binomial tau-mapping assertion failed at M = 200 because scipy's pmf carries ~1e-10 error in the row
mean and ~1e-8 in the variance (seen while diagnosing; the BB row-mean figure is a P6a ingredient), so WF and BB
rows are built in mpmath and cross-checked against scipy to 1e-9; P7's mode count was raised from 180 to 200.

SOURCES (untrusted data, read only; gitignored; fetched 2026-10-13 ~21:25 UTC into a new directory)
  RAW = sources/raw/b1e-q2-2026-10-13/
  CH   chalub2022v1.pdf  arXiv:2208.00148v1 [math.AP], 30 Jul 2022, F. A. C. C. Chalub, "Solution of the
       Neutral Kimura equation with two integral constraints"; sha256 a720d24b68e25de825e4d183dd732564
       ed2c6e831974bc50973d6f1e8a10c0ed (= bib-literature.md row Chalub2022).  Text: chalub2022v1.txt =
       `pdftotext -layout` (poppler 24.02.0), sha256 c7225292f5e2c28f21ffb88f412d91a0577de7fb332df97c52
       2865a944fe0c3f.
  BLOG blog-2026-08-23.html  https://voxday.net/2026/08/23/chalub-and-the-kimura-cancellation/ ;
       article:published_time 2026-08-23T09:37:10+00:00, modified 2026-08-23T13:16:18+00:00; sha256
       be40cd766ec852ae3d9ff075d4d216e8457746f9921dd0efaf69b33a8053561e (differs from the 2026-10-07 copy
       30af50c4... in bib-day.md; WordPress pages carry per-fetch markup; the quoted text is what is checked).
       Paragraphs are extracted by blog_paragraphs() below.
  KIMURA 1955  M. Kimura, "Solution of a process of random genetic drift with a continuous model", PNAS
       41(3):144-150, doi 10.1073/pnas.41.3.144, PMC528040 (not open access; scanned PDF).  NOT HELD.
       2026-10-13: Europe PMC render endpoint and pnas.org returned Cloudflare challenges; pmc.ncbi.nlm.nih.gov
       returned a proof-of-work page; NCBI efetch says "The publisher of this article does not allow
       downloading of the full text in XML form" (k-eutils.xml kept).  None was bypassed (HOWTO-refresh).
       The held copies the claim file names (sources/raw/day/...) are not on this workstation or na-workhorse.

TARGET QUOTES (verbatim; whitespace normalised)
  QB  (blog 2026-08-23, post body paragraph 4 by blog_paragraphs(); the claim file says "¶5 of extracted
      text"; the script prints the index it finds; no Q id yet, the next free id is assigned at integration
      (Q296 was the next free id at registration)):
      "Chalub shows that the 1/(2N) is an assumption imported from the Wright-Fisher model. It is not a
      result produced by the mathematics."
  Context in the same post (for readings; not scored separately):
  B2  "The classical solution to the neutral Kimura equation — the one Kimura wrote down in 1955, the one
      reproduced in Crow and Kimura and in every graduate course since — decays to zero."
  B2b "To fix this, Chalub adds two point masses at the boundaries, one representing the fraction of
      populations in which the allele has fixed and one representing the fraction in which it has been lost."
  B3a "Nothing in the Kimura equation determines how the escaping probability splits between those two
      boundaries."
  B3b "So Chalub supplies the number from outside, in the form of two constraints he imposes by hand before
      solving anything."
  B3c "The second is that the average allele frequency never changes, which is not a fact about diffusion
      but an inherited assumption from the Wright-Fisher model, the very assumption that has been
      successfully disputed by me and three scientists before me."
  B3d "Impose that assumption and the fixation probability comes out equal to the starting frequency."
  B3e "he says plainly that the constraints are inherited from the discrete process."
  B6  "The initial-frequency theorem is not a theorem of the diffusion. The diffusion cannot produce it."
  Q286, Q288 (Zenodo 22903977 as modified 2026-10-13; in quotes-day.md): Q288 "Chalub (2022) ... derives
      the explicit transient solution as a Gegenbauer polynomial expansion whose terms converge to the
      steady-state fixation probability u(p) = p only as t → ∞."; Q286 "... converting Chalub's abstract
      series into the closed-form finite-time completion fraction F(T) = exp(−π²Nₑ/T) ...".
  Chalub 2022 passages (CH, whitespace normalised), ids for this check:
  C1 "two conservation laws derived directly from the discrete process"
  C2 "However, to obtain the correct solution, two additional conservation laws had to be introduced into
     the model."
  C3 "limit of the Moran and the Wright-Fisher processes"
  C4 "correct solution of the continuous models, in the sense of being a continuous approximation of the
     discrete process, is a measure that not only satisfy the Kimura equation (7) but also the two
     conservation laws given by Eqs. (9)."
  C5 "However, the classical solution decay in the limit t → ∞, and therefore cannot be the correct
     solution from the modeling point of view."
  C6 "is known to be written in terms of Gegenbauer polynomials, cf. [2, 3, 4, 5, 6]."
  C7 "The main difference between this and previous works on the same subject is that the conservation laws
     are taken into consideration."
  C8 "Finally, the time-dependent fixation probability is given by"
  C9 "If we assume (in the sense of distributions) that"
  C10 "Motoo Kimura. Solution of a process of random genetic drift with a continuous model."
  C11 "the α-Gegenbauer polynomials are called"   (footnote 1: Morse-Feshbach and the introduction's
     references write T_n^α, with T^α = C^(α+1/2))
  C12 "For α < 3/2, the right hand side of Eqs. (3)–(6) are identically zero."

THE TWO QUESTIONS (brief)
  Q1  Is the 1/(2N) of QB an input Chalub assumes, a consequence of the diffusion problem he solves, or a
      boundary/initial condition?  Fidelity against CH; internal against the post's own material.
  Q2  Is Chalub's Gegenbauer expansion the Kimura (1955) series?  Settled from the mathematics, not from
      either author's description of the other (C6, C7, C10, C11 and B2 are context only).

NOTATION (Chalub's)  Neutral Kimura equation (7) with psi = 0, kappa = 1: d_t p = d_x^2 (x(1-x) p).
  p = a(t) delta_0 + r(x,t) + b(t) delta_1;  r = sum_n d_n exp(-lam_n t) C_n^{3/2}(2x-1), lam_n = (n+1)(n+2);
  d_n = 4(2n+3)/((n+1)(n+2)) int_0^1 C_n^{3/2}(2x-1) p^I(x) x(1-x) dx;  for p^I = delta_{x0}:
  d_n = 4(2n+3)/((n+1)(n+2)) C_n^{3/2}(2x0-1) x0(1-x0).  Constraint 1: d/dt int p = 0; constraint 2:
  d/dt int x p = 0 (Chalub's (9)).  Chalub: b(t) = int x p^I - int x r = (1/2) sum d_n (1 - e^{-lam_n t}).
  For delta starts the script uses b(t) = x0 - (1/2) sum d_n e^{-lam_n t} (same function; (1/2) sum d_n =
  int x p^I is Chalub's identity, and the e^{-lam t} series converges absolutely for t > 0).
  Generations: t_Chalub = T/(4 N_e) (kappa = 1 against Kimura's 1/(4N)); B2f's x = T/N_e, so t = x/4.
  Chain time scales: tau per step = Var(dx | x)/(2 x(1-x)): Wright-Fisher (M copies) 1/(2M); Moran (one
  birth-death event) 1/M^2; beta-binomial Cannings (concentration c) (M+c)/(2M(1+c)).  Asserted per row.

EACH SIDE'S PREDICTION (stated before any computation here)
  Day side (QB, B3a-e, B6, Q286, Q288):
   DQ1a Chalub supplies the fixation/loss split from outside the PDE, through two constraints added to (7);
        the PDE in the interior does not fix it.  [T3, P5]
   DQ1b The second constraint is a Wright-Fisher assumption, "not a fact about diffusion".  Predicts: the
        boundary fluxes of Chalub's own classical solution do NOT already give b(t) (P4 miss), or some
        neutral discrete chain other than WF does NOT give P_fix = 1/M (P6b miss).
   DQ1c Chalub says the constraints come from the discrete process.  [T4]
   DQ2  Chalub's expansion is the object whose dominant behaviour gives F(T) (Q286).  Predicts P7 band E.
        (B2 itself identifies the classical part with Kimura 1955.)
  Critic side:
   KQ1a "1/(2N)" is nowhere in Chalub; he calls the constraints derived, not assumed, and names Moran as
        well as Wright-Fisher.  [T4, T5]
   KQ1b Constraint 2 is the bookkeeping of the PDE's own boundary flux (P4 hit) and holds in every neutral
        exchangeable chain (P6b hit): P_fix = p0 is a result of the neutral mathematics.
   KQ2  Chalub's transient is the classical (Kimura 1955) eigen-series; what is new in 2022 is the boundary
        masses.  Predicts P7 band E and P8 band S.

TEXTUAL FACTS TO VERIFY (read before registration; verified, not scored as predictions)
  T1 QB is verbatim in the post body; its paragraph index is printed; published/modified times as above.
  T2 B2, B2b, B3a-e, B6 are verbatim in the post body.
  T3 CH contains C2, C4, C5 (the constraints are added to (7); the classical solution alone decays; the
     "correct solution" satisfies (7) and both laws).
  T4 CH contains C1 and C3; "Wright-Fisher" occurs exactly twice (C3 and the title of ref. [8]); "assum"
     occurs exactly once, in C9 (an initial condition of Dirac type), never about the constraints.
  T5 CH contains none of "1/(2N)", "1/2N", "population size", "effective", "absorb"; every "2N" in CH is the
     set 2ℕ (preceded by "∈").
  T6 CH contains C6, C7, C10, C11 (context for Q2 only; not used to set a band).
  T7 CH contains C8 and C12.
  T8 No held copy of Kimura (1955): no file matching sources/raw/*/kimura1955* with a %PDF header.

AUDIT PREDICTIONS (computed; bands fixed here)
  P1 Chalub's Gegenbauer integrals (3)-(6) hold: |LHS - RHS| <= 1e-20 for alpha in {0.75, 1.25, 1.5, 2,
     2.5, 3.7}, n = 0..12; and for alpha = 3/2 on [0,1]: int C_n = 1 (n even), 0 (n odd); int x C_n = 1/2,
     n = 0..60 (abs <= 1e-20).  [Credit to the cited source.]
  P1s C12 is false as written: RHS of (4) at n = 0 equals 2 for every alpha tested (int C_0 = 2), and at
     alpha = 0.75, n = 1 RHS(4) = LHS(4) = 0.25 (+-1e-20).  Scored for neither side: a slip in Chalub's
     Appendix, immaterial under R1 (Section 3 uses alpha = 3/2 only).
  P2 Eigenfunctions: d_x^2[x(1-x) C_n^{3/2}(2x-1)] = -(n+1)(n+2) C_n^{3/2}(2x-1), n = 0..40, x in {0.13,
     0.5, 0.77}, relative <= 1e-12; Chalub's ODE x(1-x)f'' + (alpha+1/2)(1-2x)f' + n(n+2alpha)f = 0 for
     f = C_n^alpha(2x-1), alpha in {0.75, 1.5, 2.5}, n = 0..20, residual <= 1e-12 x largest term.  [Identity.]
  P3 Smooth start p^I = Beta(4,5) density 280 x^3 (1-x)^4: |d_n| <= 1e-25 for n = 8..12; sum_even d_n = 1;
     (1/2) sum d_n = 4/9; sum d_n C_n(2x-1) = p^I(x) at x in {0.1, 0.37, 0.8}; Chalub's printed a(t), b(t)
     equal 1 - int r - b and int x p^I - int x r at t in {0.05, 0.5, 2}; b(inf) = 4/9, a(inf) = 5/9.  All
     to 1e-25.  [Chalub's Section 3 algebra; identity.]
  P4 Flux identity (KQ1b, can fail).  For delta starts x0 in {0.001, 0.1, 0.5, 0.9} and the Beta(4,5) start,
     t in {0.05, 0.1, 0.5, 2}: b'(t) = -J(1) and a'(t) = +J(0), J = d_x[x(1-x) r] (the outward flux of the
     classical solution at x = 1 and x = 0; J by numerical differentiation of each mode), relative <= 1e-15.
     Here b' comes from constraint 2 (Chalub's b) and a' from constraint 1 (a = 1 - int r - b).
     Consequence stated now: given constraint 1, constraint 2 is equivalent to "probability that leaves the
     interior at x = 1 stays at x = 1"; the split is fixed by the classical solution's own boundary fluxes.
  P5 Constraint 1 alone leaves the split free (DQ1a, identity).  delta start x0 = 0.1, m(t) = 1 - int r:
     b_theta = theta m for constant theta in {0, 0.5, 1} satisfies constraint 1 with r unchanged and
     b_theta(inf) = theta; d/dt int x p != 0 for each (|value| >= 1e-6 at t = 0.5); the only split meeting
     constraint 2 is Chalub's, whose ratio b/m is reported at t in {0.05, 0.5, 2} (not constant).
  P6 Exact neutral chains, M = 200 copies, start i = 1 (KQ1b, can fail): Wright-Fisher; Moran; beta-binomial
     Cannings with c = M (offspring variance about doubled, N_e about N/2).
     (a) E[j | i] = i for every row (abs <= 1e-10); Var(dx | x)/(x(1-x)) constant over rows and equal to the
         time scale above (relative <= 1e-9)  [asserts the models are neutral and the tau mapping].
     (b) P_fix(i = 1) x M = 1 within 1e-9 in all three.
     (c) F_chain(tau) = P(fixed by step k)/P_fix against F_C = b(tau; x0 = 1/M)/x0 at tau in {0.25, 0.5, 1,
         2, 3} (tau = k x step, k rounded): |difference| <= 0.02 everywhere; relative <= 5% at tau >= 1 for
         Wright-Fisher and Moran, <= 10% for beta-binomial.
  P7 Q2 relay identity (DQ2 and KQ2, can fail).  Limit x0 -> 0 of Chalub's b(t; x0)/x0 with C_n^{3/2}(-1)
     from the recurrence: coefficient of e^{-lam_n t} is -(-1)^n (2n+3) for n = 0..200 (ratio 1 within 1e-40), i.e.
     mode n = term i = n + 1 of B2f's series; and the limit equals B2f's F_dec(x) at t = x/4 for x in {0.05,
     0.25, 1, 4, 5.04, 25.2}, relative <= 1e-30 (dps 170).  Finite x0 in {1e-6, 1e-8, 1e-10}: relative
     difference from the limit shrinks monotonically as x0 falls at every x, and is <= 1e-3 at x >= 1 for
     x0 = 1e-10.  Large t: (x0 - b)/(3 x0 (1 - x0) e^{-2t}) = 1 within 1e-3 at t = 5, x0 in {0.001, 0.1, 0.5,
     0.9} (Chalub's stated asymptote; B2f's 1 - 3 exp(-x/2)).
     Band E: every P7 item within tolerance -> Chalub's b(t) and the series B2f used are one function of
     time, t = T/(4N_e).  Band X: any item outside -> they differ.
  P8 Kimura (1955) primary text.  Band U: no held copy at run time (expected).  If an owner-supplied copy is
     held before the write-up (the script prints its sha256), the write-up reads its equations against r(x,t):
     band S if its eigenvalues are i(i+1)/(4N) (or the same under t -> t/4N) and its eigenfunctions are,
     up to constant factors, C_{i-1}^{3/2}(2x-1) or C_{i-1}^{3/2}(1-2x) (or the equal hypergeometric
     polynomials, identity shown in the write-up); band D otherwise.  It also records whether Kimura (1955)
     gives the probability of fixation by time t (Chalub's b(t)).

REACHABILITY (each side's band, and the result that would produce it)
  Day, Q1: P4 miss (b' differs from the boundary flux beyond 1e-15 anywhere) or P6b miss (Moran or
     beta-binomial P_fix x M outside 1 +- 1e-9).  Either makes constraint 2 information not contained in
     (7) plus absorption, or makes 1/M model-specific.  P6b can fail only through a bug (optional stopping
     on a bounded martingale) - stated as non-severe; P4 is the severe item.
  Critic, Q1: P4 hit and P6b hit.
  Day, Q2 (route credit reaches Chalub's paper): P7 band E.  Critic, Q2 (the route is the old series): P7
     band E and P8 band S.  The reading "a distinct 2022 solution" (fair relay of a new result): P7 band X or
     P8 band D.  With P8 at U the "old" half stays unverifiable whatever P7 gives.
  A miss in either direction is reported with the same weight as a hit.

VERDICT MAPPING (rule file R4-X1-verdict-rule.md, rules S, C, RD, N, F, U, R1; proposals only, decided at
integration; the claim file is not edited here)
  RH: QB dialectic (a checkable statement about a cited paper).
  Readings of QB (rule RD; all reported):
   R-A "the 1/(2N)" = the neutral fixation probability P_fix = p0 (1/(2N) for one new copy); "the
       mathematics" = PDE (7) on the open interval; "imported from the Wright-Fisher model" = the second
       constraint enters from the discrete process.
   R-B as R-A, but "the mathematics" = the neutral diffusion model with its boundary behaviour (supported
       by B6 "The diffusion cannot produce it").
   R-C "the 1/(2N)" = the initial frequency of one copy among 2N.
  Fidelity (to CH):
   R-A `partial` if T3, T4, T5 hold (the laws are added to (7): accurate; Chalub calls them "derived
       directly from the discrete process", names Moran and Wright-Fisher, never "assumption", never
       1/(2N): relabelled and narrowed).  `accurate` if T4 fails because CH calls them assumptions specific
       to Wright-Fisher.  `misread` if T3 fails.
   R-B `misread` if T3 (C4) and P3 hold (CH counts the laws as part of the correct solution of the continuous
       model and derives b(inf) = int x p^I); `partial` otherwise.
   R-C `misread` if T5 holds (CH has no N and no initial frequency 1/(2N)).
  Internal (rule N, against the post's own material): `holds` under R-A, R-B and R-C if T2 holds (B3d says
   the fixation probability follows once the constraint is imposed; the post contains no derivation the
   quote contradicts).  P4 is audit material, not the author's, so it scores external, not internal.
  External (mathematics, not data):
   R-A: P4 hit and P6b hit -> `contested` (true: (7) on the open interval fixes no split, P5; false: what is
       needed is a Wright-Fisher import - it is model-free absorption bookkeeping, P4, and P_fix = 1/M holds in
       Moran and beta-binomial chains, P6b).  P4 miss or P6b miss -> `supported`.
   R-B: P4 hit and P6b hit -> `contradicted`; P4 miss -> `contested`; P6b miss -> `supported`.
   R-C: P6b hit -> `contradicted` (a count of copies, not a model assumption); miss -> `contested`.
   Not tested: whether real neutral alleles have E[dp] = 0 (that is the definition of neutrality; B3c's
   "successfully disputed" premise is scored at B3/B7, rule N1).
  Field-setting reading: the one under which QB is most defensible.  Expected R-A, giving fidelity
   `partial`, internal `holds`, external `contested`: B1e's current values, so Q1 is expected to move no
   field value; it adds QB's Readings table and quote id.
  Q2:
   P7 E + P8 U: B1e's "unchecked" caveat is replaced by: Chalub's b(t) is the series B2f resummed, so B2f's
       route credit applies to "Chalub's ... series" as Q286 and Q288 describe it; whether that series is
       Kimura's (1955) is `unverifiable` from primary text.  No field value moves.
   P7 E + P8 S: as above, and the route is standard and old: Q286's "Chalub's abstract series" relays a
       1955 series (attribution slip, slip ledger under R1: no number moves).
   P7 E + P8 D: the relay is a fair description of a 2022 result.
   P7 X: B2f's credit does not reach Chalub's expansion; propose fidelity of the Chalub link `misread`
       (Reading A) and flag to the lead.
  ESCALATION (brief, stated in advance): if any proposed move would change a verdict value or defeater on
   B1, B1a, B2 or B, adopt Reading B of B2f as field-setting on B1e, or find that Day derived a number from
   F(T), stop, write what exists, report to the lead, and apply nothing.  Expected: does not fire (Q1 and Q2
   touch B1e only; R-B/R-C external values bear on B7's premise, which is not in the list; flagged if P6b
   misses).

RESOURCES  Local, one process (the brief and AGENTS.md allow a trivial check: < 500 MB, < 1 min).  Measured
  before commit (2026-10-13, workstation, OPENBLAS_NUM_THREADS=1, values suppressed): `--smoke` 0.2 s, max RSS
  100 MB; `--smoke-full` (the full grid, identical computation to the main run) 15.5 s, max RSS 104 MB.
  na-workhorse is not needed (and is busy with ph2 until 2026-10-16).
Run:     OPENBLAS_NUM_THREADS=1 research/.venv/bin/python -I research/checks/b1e_q2_chalub_link.py \
             > research/checks/results/raw/b1e_q2.out 2>&1
Outputs: research/checks/results/raw/b1e_q2.out (stdout), research/checks/results/raw/b1e_q2.json
Smoke:   research/.venv/bin/python -I research/checks/b1e_q2_chalub_link.py --smoke   (reduced grid; writes nothing)
         ... --smoke-full   (the full grid with every value and call suppressed; writes nothing)
"""
import glob
import hashlib
import html
import importlib.util
import json
import os
import re
import resource
import sys
import time

import mpmath as mp
import numpy as np
from scipy.stats import betabinom, binom

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
RAW = os.path.join(ROOT, "sources", "raw", "b1e-q2-2026-10-13")
CH_PDF = os.path.join(RAW, "chalub2022v1.pdf")
CH_TXT = os.path.join(RAW, "chalub2022v1.txt")
BLOG = os.path.join(RAW, "blog-2026-08-23.html")
SHA = {
    CH_PDF: "a720d24b68e25de825e4d183dd732564ed2c6e831974bc50973d6f1e8a10c0ed",
    CH_TXT: "c7225292f5e2c28f21ffb88f412d91a0577de7fb332df97c522865a944fe0c3f",
    BLOG: "be40cd766ec852ae3d9ff075d4d216e8457746f9921dd0efaf69b33a8053561e",
}
OUT_JSON = os.path.join(HERE, "results", "raw", "b1e_q2.json")
SMOKE_FULL = "--smoke-full" in sys.argv
SMOKE = SMOKE_FULL or "--smoke" in sys.argv

QB = ("Chalub shows that the 1/(2N) is an assumption imported from the Wright-Fisher model. It is not a result "
      "produced by the mathematics.")
BLOG_CTX = {
    "B2": ("The classical solution to the neutral Kimura equation — the one Kimura wrote down in 1955, the one "
           "reproduced in Crow and Kimura and in every graduate course since — decays to zero."),
    "B2b": ("To fix this, Chalub adds two point masses at the boundaries, one representing the fraction of "
            "populations in which the allele has fixed and one representing the fraction in which it has been lost."),
    "B3a": "Nothing in the Kimura equation determines how the escaping probability splits between those two boundaries.",
    "B3b": ("So Chalub supplies the number from outside, in the form of two constraints he imposes by hand before "
            "solving anything."),
    "B3c": ("The second is that the average allele frequency never changes, which is not a fact about diffusion but "
            "an inherited assumption from the Wright-Fisher model, the very assumption that has been successfully "
            "disputed by me and three scientists before me."),
    "B3d": "Impose that assumption and the fixation probability comes out equal to the starting frequency.",
    "B3e": "he says plainly that the constraints are inherited from the discrete process.",
    "B6": "The initial-frequency theorem is not a theorem of the diffusion. The diffusion cannot produce it.",
}
CH_Q = {
    "C1": "two conservation laws derived directly from the discrete process",
    "C2": ("However, to obtain the correct solution, two additional conservation laws had to be introduced into "
           "the model."),
    "C3": "limit of the Moran and the Wright-Fisher processes",
    "C4": ("correct solution of the continuous models, in the sense of being a continuous approximation of the "
           "discrete process, is a measure that not only satisfy the Kimura equation (7) but also the two "
           "conservation laws given by Eqs. (9)."),
    "C5": ("However, the classical solution decay in the limit t → ∞, and therefore cannot be the correct solution "
           "from the modeling point of view."),
    "C6": "is known to be written in terms of Gegenbauer polynomials, cf. [2, 3, 4, 5, 6].",
    "C7": ("The main difference between this and previous works on the same subject is that the conservation laws "
           "are taken into consideration."),
    "C8": "Finally, the time-dependent fixation probability is given by",
    "C9": "If we assume (in the sense of distributions) that",
    "C10": "Motoo Kimura. Solution of a process of random genetic drift with a continuous model.",
    "C11": "the α-Gegenbauer polynomials are called",
    "C12": "For α < 3/2, the right hand side of Eqs. (3)–(6) are identically zero.",
}

RESULTS = {}   # prediction id -> {"hit": bool, ...}
LOG = []


def say(*a):
    """Print unless smoke (smoke shows no computed values)."""
    if not SMOKE:
        print(*a, flush=True)


def record(pid, hit, **detail):
    RESULTS[pid] = {"hit": bool(hit), **{k: (str(v) if isinstance(v, mp.mpf) else v) for k, v in detail.items()}}
    say(f"  {pid}: {'HIT' if hit else 'MISS'}  {detail}")


def flat(s):
    return " ".join(s.split())


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def blog_paragraphs():
    s = open(BLOG, encoding="utf-8").read()
    pub = re.search(r'article:published_time" content="([^"]+)"', s)
    mod = re.search(r'article:modified_time" content="([^"]+)"', s)
    m = re.search(r'<div[^>]*class="[^"]*(entry-content|post-body)[^"]*"', s)
    assert m, "post body div not found in blog HTML"
    body = s[m.start():]
    paras = []
    for _tag, p in re.findall(r"<(p|blockquote|li)[^>]*>(.*?)</\1>", body, re.S)[:40]:
        x = flat(html.unescape(re.sub(r"<[^>]+>", "", p)))
        if x:
            paras.append(x)
    return paras, (pub.group(1) if pub else None), (mod.group(1) if mod else None)


# ----------------------------------------------------------------------------------------------- textual facts
def textual():
    say("== Textual facts T1-T8 (verified, not scored)")
    for p, want in SHA.items():
        got = sha256(p)
        assert got == want, f"sha256 mismatch for {p}: {got}"
    paras, pub, mod = blog_paragraphs()
    idx = [i + 1 for i, x in enumerate(paras) if QB in x]
    t = {}
    t["T1"] = dict(ok=len(idx) == 1, paragraph=idx, published=pub, modified=mod)
    body = " ".join(paras)
    t["T2"] = dict(ok=all(v in body for v in BLOG_CTX.values()),
                   missing=[k for k, v in BLOG_CTX.items() if v not in body])
    ch = flat(open(CH_TXT, encoding="utf-8").read())
    has = {k: (v in ch) for k, v in CH_Q.items()}
    t["T3"] = dict(ok=has["C2"] and has["C4"] and has["C5"])
    wf = [m.start() for m in re.finditer("Wright-Fisher", ch)]
    assum = [ch[max(0, m.start() - 20):m.start() + 40] for m in re.finditer("assum", ch)]
    t["T4"] = dict(ok=has["C1"] and has["C3"] and len(wf) == 2 and len(assum) == 1 and CH_Q["C9"] in ch
                   and "If we assume" in assum[0], wright_fisher_count=len(wf), assum_contexts=assum)
    absent = {s: (s in ch) for s in ("1/(2N)", "1/2N", "population size", "effective", "absorb")}
    twoN = [ch[max(0, m.start() - 4):m.start() + 4] for m in re.finditer("2N", ch)]
    t["T5"] = dict(ok=not any(absent.values()) and all("∈" in c for c in twoN), present=absent, twoN_contexts=twoN)
    t["T6"] = dict(ok=all(has[k] for k in ("C6", "C7", "C10", "C11")))
    t["T7"] = dict(ok=has["C8"] and has["C12"])
    kim = []
    for f in glob.glob(os.path.join(ROOT, "sources", "raw", "*", "kimura1955*")):
        with open(f, "rb") as fh:
            if fh.read(5) == b"%PDF-":
                kim.append((os.path.relpath(f, ROOT), sha256(f)))
    t["T8"] = dict(ok=not kim, held_copies=kim)
    t["missing_CH_passages"] = [k for k, v in has.items() if not v]
    for k, v in t.items():
        say(f"  {k}: {v}")
    return t


# ------------------------------------------------------------------------------------------ Chalub's mathematics
HALF3 = None


def gegen_all(nmax, a, y):
    """C_0^a(y) .. C_{nmax-1}^a(y) by the three-term recurrence (mpmath's hypergeometric form failed to
    converge at some points in the smoke)."""
    a, y = mp.mpf(a), mp.mpf(y)
    out = [mp.mpf(1), 2 * a * y]
    for n in range(2, nmax):
        out.append((2 * y * (n + a - 1) * out[n - 1] - (n + 2 * a - 2) * out[n - 2]) / n)
    return out[:nmax]


def gegen(n, a, y):
    return gegen_all(n + 1, a, y)[n]


def C32(n, y):
    return gegen(n, HALF3, y)


def check_recurrence():
    """Float cross-check of the recurrence against scipy (asserted, not scored)."""
    from scipy.special import eval_gegenbauer
    for a in (0.75, 1.5, 2.5, 3.7):
        for y in (-1.0, -0.6, 0.0, 0.3, 1.0):
            c = gegen_all(31, a, y)
            for n in range(31):
                ref = eval_gegenbauer(n, a, y)
                assert abs(float(c[n]) - ref) <= 1e-9 * max(1.0, abs(ref)), ("recurrence", a, y, n)


def lam(n):
    return (n + 1) * (n + 2)


def nmax_for(t, digits):
    """Smallest mode count with exp(-lam_n t) below 10^-(digits+10)."""
    lim = (digits + 10) * mp.log(10)
    n = 0
    while lam(n) * t <= lim:
        n += 1
    return n + 5


def d_delta(x0, nmax):
    x0 = mp.mpf(x0)
    c = gegen_all(nmax, HALF3, 2 * x0 - 1)
    return [4 * (2 * n + 3) / mp.mpf((n + 1) * (n + 2)) * c[n] * x0 * (1 - x0) for n in range(nmax)]


def b_delta(d, x0, t):
    return mp.mpf(x0) - sum(dn * mp.exp(-lam(n) * t) for n, dn in enumerate(d)) / 2


def int_r(d, t):
    return sum(dn * mp.exp(-lam(n) * t) for n, dn in enumerate(d) if n % 2 == 0)


def bprime(d, t):
    return sum(dn * lam(n) * mp.exp(-lam(n) * t) for n, dn in enumerate(d)) / 2


def aprime(d, t):
    """From constraint 1: a = 1 - int r - b."""
    return sum(dn * lam(n) * mp.exp(-lam(n) * t) for n, dn in enumerate(d) if n % 2 == 0) - bprime(d, t)


_JCACHE = {}


def J_mode(n, x):
    """d/dx [x(1-x) C_n^{3/2}(2x-1)] at x, numerically."""
    key = (n, x, mp.mp.dps)
    if key not in _JCACHE:
        _JCACHE[key] = mp.diff(lambda z: z * (1 - z) * C32(n, 2 * z - 1), mp.mpf(x))
    return _JCACHE[key]


def p1_integrals(cfg):
    say("== P1 / P1s Chalub's integrals (3)-(6)")
    worst = mp.mpf(0)
    for alpha in cfg["alphas"]:
        a = mp.mpf(alpha)
        for n in range(cfg["n_int"] + 1):
            B = mp.binomial(2 * a + 2 * n - 2, 2 * n + 1)
            I = lambda k, w: mp.quad(lambda y: (y if w else 1) * gegen(k, a, y), [-1, 1],
                                     method="gauss-legendre")
            rows = [(I(2 * n + 1, 0), 0), (I(2 * n, 0), B / (a - 1)), (I(2 * n, 1), 0),
                    (I(2 * n + 1, 1), 2 * (a + n) / ((a - 1) * (2 * n + 3)) * B)]
            worst = max(worst, max(abs(l - r) for l, r in rows))
    w01 = mp.mpf(0)
    for n in range(cfg["n_int01"] + 1):
        i0 = mp.quad(lambda x: C32(n, 2 * x - 1), [0, 1], method="gauss-legendre")
        i1 = mp.quad(lambda x: x * C32(n, 2 * x - 1), [0, 1], method="gauss-legendre")
        w01 = max(w01, abs(i0 - (1 if n % 2 == 0 else 0)), abs(i1 - mp.mpf(1) / 2))
    record("P1", worst <= 1e-20 and w01 <= 1e-20, worst_36=mp.nstr(worst, 3), worst_01=mp.nstr(w01, 3))
    rhs0 = [mp.binomial(2 * mp.mpf(al) - 2, 1) / (mp.mpf(al) - 1) for al in cfg["alphas"]]
    a = mp.mpf("0.75")
    rhs = mp.binomial(2 * a + 2 - 2, 3) / (a - 1)
    lhs = mp.quad(lambda y: gegen(2, a, y), [-1, 1], method="gauss-legendre")
    ok = all(abs(v - 2) <= 1e-20 for v in rhs0) and abs(rhs - mp.mpf("0.25")) <= 1e-20 and abs(lhs - rhs) <= 1e-20
    record("P1s", ok, rhs4_n0=[mp.nstr(v, 6) for v in rhs0], rhs4_a075_n1=mp.nstr(rhs, 8), lhs4_a075_n1=mp.nstr(lhs, 8))


def p2_eigen(cfg):
    say("== P2 eigenfunctions and Chalub's ODE")
    worst = mp.mpf(0)
    for n in range(cfg["n_eig"] + 1):
        for x in cfg["xs"]:
            x = mp.mpf(x)
            lhs = mp.diff(lambda z: z * (1 - z) * C32(n, 2 * z - 1), x, 2)
            rhs = -lam(n) * C32(n, 2 * x - 1)
            worst = max(worst, abs(lhs - rhs) / max(abs(rhs), mp.mpf(1)))
    wode = mp.mpf(0)
    for alpha in cfg["alphas_ode"]:
        a = mp.mpf(alpha)
        for n in range(cfg["n_ode"] + 1):
            for x in cfg["xs"]:
                x = mp.mpf(x)
                f = lambda z: gegen(n, a, 2 * z - 1)
                terms = [x * (1 - x) * mp.diff(f, x, 2), (a + mp.mpf(1) / 2) * (1 - 2 * x) * mp.diff(f, x),
                         n * (n + 2 * a) * f(x)]
                wode = max(wode, abs(sum(terms)) / max(max(abs(v) for v in terms), mp.mpf(1)))
    record("P2", worst <= 1e-12 and wode <= 1e-12, worst_eig=mp.nstr(worst, 3), worst_ode=mp.nstr(wode, 3))


def beta45(x):
    return 280 * x ** 3 * (1 - x) ** 4


def d_smooth(nmax):
    return [4 * (2 * n + 3) / mp.mpf((n + 1) * (n + 2))
            * mp.quad(lambda x: C32(n, 2 * x - 1) * beta45(x) * x * (1 - x), [0, 1], method="gauss-legendre")
            for n in range(nmax)]


def p3_smooth(cfg):
    say("== P3 smooth start Beta(4,5)")
    d = d_smooth(13)
    errs = [max(abs(dn) for dn in d[8:]), abs(sum(d[0::2]) - 1), abs(sum(d) / 2 - mp.mpf(4) / 9)]
    for x in cfg["xs_p3"]:
        x = mp.mpf(x)
        errs.append(abs(sum(dn * C32(n, 2 * x - 1) for n, dn in enumerate(d)) - beta45(x)))
    for t in cfg["ts_p3"]:
        t = mp.mpf(t)
        e = [mp.exp(-lam(n) * t) for n in range(len(d))]
        b_chalub = sum(dn * (1 - e[n]) for n, dn in enumerate(d)) / 2
        a_chalub = sum((-1) ** n * dn * (1 - e[n]) for n, dn in enumerate(d)) / 2
        intxr = sum(dn * e[n] for n, dn in enumerate(d)) / 2       # int x C_n = 1/2 (P1)
        b_def = mp.mpf(4) / 9 - intxr
        a_def = 1 - int_r(d, t) - b_def
        errs += [abs(b_chalub - b_def), abs(a_chalub - a_def)]
    binf, ainf = sum(d) / 2, sum((-1) ** n * dn for n, dn in enumerate(d)) / 2
    errs += [abs(binf - mp.mpf(4) / 9), abs(ainf - mp.mpf(5) / 9)]
    w = max(errs)
    record("P3", w <= 1e-25, worst=mp.nstr(w, 3), b_inf=mp.nstr(binf, 12), a_inf=mp.nstr(ainf, 12))
    return d


def p4_flux(cfg, d_beta):
    say("== P4 flux identity b' = -J(1), a' = +J(0)")
    starts = [(f"delta x0={x0}", x0) for x0 in cfg["x0s_p4"]] + [("Beta(4,5)", None)]
    worst, rows = mp.mpf(0), []
    for label, x0 in starts:
        for t in cfg["ts_p4"]:
            t = mp.mpf(t)
            if x0 is None:
                d = d_beta
            else:
                d = d_delta(x0, nmax_for(t, mp.mp.dps))
            out1 = -sum(dn * mp.exp(-lam(n) * t) * J_mode(n, 1) for n, dn in enumerate(d))
            out0 = sum(dn * mp.exp(-lam(n) * t) * J_mode(n, 0) for n, dn in enumerate(d))
            bp, ap = bprime(d, t), aprime(d, t)
            e1, e0 = abs(bp - out1) / abs(bp), abs(ap - out0) / abs(ap)
            worst = max(worst, e1, e0)
            rows.append((label, float(t), mp.nstr(bp, 8), mp.nstr(out1, 8), mp.nstr(e1, 3),
                         mp.nstr(ap, 8), mp.nstr(out0, 8), mp.nstr(e0, 3)))
    for r in rows:
        say("   ", r)
    record("P4", worst <= 1e-15, worst_rel=mp.nstr(worst, 3), n_cells=len(rows))


def p5_family(cfg):
    say("== P5 constraint 1 alone leaves the split free")
    x0 = mp.mpf("0.1")
    t = mp.mpf("0.5")
    d = d_delta(x0, nmax_for(t, mp.mp.dps))
    m_prime = sum(dn * lam(n) * mp.exp(-lam(n) * t) for n, dn in enumerate(d) if n % 2 == 0)   # m = 1 - int r
    dintxr = -bprime(d, t)                                         # d/dt int x r = -b'_Chalub (constraint 2)
    dev = {th: th * m_prime + dintxr for th in cfg["thetas"]}
    ratios = []
    for tt in cfg["ts_p3"]:
        tt = mp.mpf(tt)
        dd = d_delta(x0, nmax_for(tt, mp.mp.dps))
        ratios.append(mp.nstr(b_delta(dd, x0, tt) / (1 - int_r(dd, tt)), 8))
    ok = all(abs(v) >= 1e-6 for v in dev.values()) and len(set(ratios)) == len(ratios)
    record("P5", ok, dddt_int_xp={str(k): mp.nstr(v, 6) for k, v in dev.items()}, chalub_b_over_m=ratios)


# ------------------------------------------------------------------------------------------------ exact chains
def _row_mp(M, p0, ratio):
    """One transition row built in mpmath by the term ratio, then rounded to float.  scipy's pmfs carried
    ~1e-10 error in the row mean and ~1e-8 in the variance at M = 200 (seen in the full-grid smoke)."""
    with mp.workdps(40):
        r = [mp.mpf(p0)]
        for j in range(M):
            r.append(r[-1] * ratio(j))
        s = sum(r)
        return np.array([float(v / s) for v in r])


def chain_wf(M):
    P = np.zeros((M + 1, M + 1))
    P[0, 0] = P[M, M] = 1.0
    for i in range(1, M):
        x = mp.mpf(i) / M
        P[i] = _row_mp(M, (1 - x) ** M, lambda j, x=x: (M - j) / mp.mpf(j + 1) * x / (1 - x))
    jgrid = np.arange(M + 1)
    for i in (1, M // 2, M - 1):          # float cross-check against scipy (asserted, not scored)
        assert np.max(np.abs(P[i] - binom.pmf(jgrid, M, i / M))) <= 1e-9, ("WF row", i)
    return P, 1.0 / (2 * M)


def chain_moran(M):
    P = np.zeros((M + 1, M + 1))
    P[0, 0] = P[M, M] = 1.0
    for i in range(1, M):
        p = (i / M) * ((M - i) / M)
        P[i, i + 1] = P[i, i - 1] = p
        P[i, i] = 1 - 2 * p
    return P, 1.0 / M ** 2


def chain_bb(M, c):
    P = np.zeros((M + 1, M + 1))
    P[0, 0] = P[M, M] = 1.0
    for i in range(1, M):
        with mp.workdps(40):
            a, b = mp.mpf(c) * i / M, mp.mpf(c) * (M - i) / M
            p0 = mp.exp(mp.loggamma(M + b) + mp.loggamma(a + b) - mp.loggamma(b) - mp.loggamma(M + a + b))
        P[i] = _row_mp(M, p0, lambda jj, a=a, b=b: (M - jj) / mp.mpf(jj + 1) * (jj + a) / (M - jj - 1 + b))
    jgrid = np.arange(M + 1)
    for i in (1, M // 2, M - 1):          # float cross-check against scipy (asserted, not scored)
        assert np.max(np.abs(P[i] - betabinom.pmf(jgrid, M, c * i / M, c * (M - i) / M))) <= 1e-9, ("BB row", i)
    return P, (M + c) / (2.0 * M * (1 + c))


def p6_chains(cfg):
    say("== P6 exact neutral chains")
    M = cfg["M"]
    x0 = mp.mpf(1) / M
    models = {"WF": chain_wf(M), "Moran": chain_moran(M), "BB": chain_bb(M, float(M))}
    rel_tol = {"WF": 0.05, "Moran": 0.05, "BB": 0.10}
    a_ok = b_ok = c_ok = True
    out = {}
    for name, (P, step) in models.items():
        i = np.arange(M + 1, dtype=float)
        x = i / M
        mean_err = np.max(np.abs(P @ i - i))
        var = (P @ (i ** 2) - i ** 2) / M ** 2
        ratio = var[1:M] / (x[1:M] * (1 - x[1:M])) / 2.0                 # tau per step, row by row
        assert np.allclose(P.sum(axis=1), 1.0, atol=1e-12), name
        assert np.max(np.abs(ratio / step - 1)) <= 1e-9, (name, "tau mapping")
        a_ok &= mean_err <= 1e-10
        Q = P[1:M, 1:M]
        h = np.linalg.solve(np.eye(M - 1) - Q, P[1:M, M])
        pfix_M = h[0] * M
        b_ok &= abs(pfix_M - 1) <= 1e-9
        rows = []
        for tau in cfg["taus"]:
            k = int(round(tau / step))
            tk = k * step
            Fc = np.linalg.matrix_power(P, k)[1, M] / h[0]
            d = d_delta(x0, nmax_for(mp.mpf(tk), mp.mp.dps))
            FC = float(b_delta(d, x0, mp.mpf(tk)) / x0)
            ad, rd = abs(Fc - FC), abs(Fc / FC - 1)
            c_ok &= ad <= 0.02 and (tau < 1 or rd <= rel_tol[name])
            rows.append(dict(tau=tau, k=k, tau_k=tk, F_chain=Fc, F_C=FC, abs_diff=ad, rel_diff=rd))
        Ne = 1.0 / (4 * step) if name != "Moran" else None   # step = 1/(4 N_e) per generation (WF, BB)
        out[name] = dict(mean_err=float(mean_err), step=step, Pfix_times_M=float(pfix_M), Ne_per_gen=Ne, rows=rows)
        say(f"  {name}: step={step:.6g}  max|E[j|i]-i|={mean_err:.2e}  Pfix*M={pfix_M:.12f}  N_e(gen)={Ne}")
        for r in rows:
            say("    ", r)
    record("P6a", a_ok)
    record("P6b", b_ok)
    record("P6c", c_ok)
    return out


# --------------------------------------------------------------------------------------------- Q2 relay identity
def load_b2f():
    path = os.path.join(HERE, "b2f_finite_time_formula.py")
    spec = importlib.util.spec_from_file_location("b2f_finite_time_formula", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert hasattr(mod, "F_dec") and "eigen-series" in (mod.F_dec.__doc__ or ""), "B2f F_dec not as expected"
    return mod


def p7_relay(cfg):
    say("== P7 Chalub b(t)/x0 (x0 -> 0) against B2f's series")
    b2f = load_b2f()
    nmax = cfg["n_coef"] + 1
    cm1 = gegen_all(nmax, HALF3, -1)
    lim = [2 * (2 * n + 3) * cm1[n] / mp.mpf((n + 1) * (n + 2)) for n in range(nmax)]
    coef_err = max(abs(lim[n] / ((-1) ** n * (2 * n + 3)) - 1) for n in range(nmax))
    vals, worst_v = [], mp.mpf(0)
    for x in cfg["xs_p7"]:
        t = mp.mpf(x) / 4
        nm = nmax_for(t, mp.mp.dps)
        assert nm <= nmax, ("n_coef too small", x, nm)
        Fch = 1 - sum(lim[n] * mp.exp(-lam(n) * t) for n in range(nm))
        Fb = mp.mpf(str(b2f.F_dec(str(x))))
        rel = abs(Fch - Fb) / abs(Fb)
        worst_v = max(worst_v, rel)
        vals.append((x, mp.nstr(Fch, 15), mp.nstr(Fb, 15), mp.nstr(rel, 3)))
    for v in vals:
        say("   ", v)
    fin, mono, small = [], True, True
    for x in cfg["xs_p7"]:
        t = mp.mpf(x) / 4
        nm = nmax_for(t, mp.mp.dps)
        Flim = 1 - sum(lim[n] * mp.exp(-lam(n) * t) for n in range(nm))
        prev = None
        for x0 in cfg["x0s_fin"]:
            d = d_delta(x0, nm)
            r = abs(b_delta(d, x0, t) / mp.mpf(x0) - Flim) / abs(Flim)
            fin.append((x, x0, mp.nstr(r, 3)))
            if prev is not None and not r < prev:
                mono = False
            prev = r
        if x >= 1 and prev > 1e-3:
            small = False
    for f in fin:
        say("   finite x0:", f)
    big = []
    for x0 in cfg["x0s_p4"]:
        t = mp.mpf(5)
        d = d_delta(x0, nmax_for(t, mp.mp.dps))
        x0m = mp.mpf(x0)
        big.append(abs((x0m - b_delta(d, x0m, t)) / (3 * x0m * (1 - x0m) * mp.exp(-2 * t)) - 1))
    ok = coef_err <= 1e-40 and worst_v <= 1e-30 and mono and small and max(big) <= 1e-3
    band = "E" if ok else "X"
    record("P7", ok, band=band, coef_err=mp.nstr(coef_err, 3), worst_value_rel=mp.nstr(worst_v, 3),
           finite_monotone=mono, finite_within_1e3_at_x_ge_1=small, large_t_worst=mp.nstr(max(big), 3))
    return band


# ------------------------------------------------------------------------------------------------------- main
FULL = dict(dps=40, alphas=[0.75, 1.25, 1.5, 2, 2.5, 3.7], n_int=12, n_int01=60, n_eig=40, alphas_ode=[0.75, 1.5, 2.5],
            n_ode=20, xs=["0.13", "0.5", "0.77"], xs_p3=["0.1", "0.37", "0.8"], ts_p3=["0.05", "0.5", "2"],
            x0s_p4=["0.001", "0.1", "0.5", "0.9"], ts_p4=["0.05", "0.1", "0.5", "2"], dps_p4=80, thetas=[0, 0.5, 1],
            M=200, taus=[0.25, 0.5, 1, 2, 3], dps_p7=170, n_coef=200, xs_p7=[0.05, 0.25, 1, 4, 5.04, 25.2],
            x0s_fin=["1e-6", "1e-8", "1e-10"])
SMALL = dict(dps=30, alphas=[0.75, 2.5], n_int=2, n_int01=3, n_eig=3, alphas_ode=[1.5], n_ode=2,
             xs=["0.13", "0.77"], xs_p3=["0.37"], ts_p3=["0.5", "2"], x0s_p4=["0.1", "0.5"], ts_p4=["0.5", "2"],
             dps_p4=30, thetas=[0, 1], M=12, taus=[1, 2], dps_p7=30, n_coef=30, xs_p7=[4, 25.2], x0s_fin=["1e-4", "1e-6"])


def main():
    global HALF3
    t0 = time.time()
    cfg = SMALL if (SMOKE and not SMOKE_FULL) else FULL
    print(f"B1e-Q2 {'SMOKE (values suppressed)' if SMOKE else 'MAIN'}  python {sys.version.split()[0]}  "
          f"mpmath {mp.__version__}  numpy {np.__version__}", flush=True)
    facts = textual()
    check_recurrence()
    mp.mp.dps = cfg["dps"]
    HALF3 = mp.mpf(3) / 2
    p1_integrals(cfg)
    p2_eigen(cfg)
    d_beta = p3_smooth(cfg)
    mp.mp.dps = cfg["dps_p4"]
    HALF3 = mp.mpf(3) / 2
    _JCACHE.clear()
    d_beta = d_smooth(13)
    p4_flux(cfg, d_beta)
    p5_family(cfg)
    mp.mp.dps = cfg["dps"]
    HALF3 = mp.mpf(3) / 2
    chains = p6_chains(cfg)
    mp.mp.dps = cfg["dps_p7"]
    HALF3 = mp.mpf(3) / 2
    band7 = p7_relay(cfg)
    band8 = "U" if facts["T8"]["ok"] else "held copy present: read it (S/D decided in the write-up)"
    record("P8", True, band=band8, held=facts["T8"]["held_copies"])
    secs = time.time() - t0
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    if SMOKE:
        print(f"smoke ok: every code path ran; {len(RESULTS)} items scored (calls suppressed); "
              f"{secs:.1f} s, max RSS {rss:.0f} MB", flush=True)
        return
    say("== Summary")
    for k, v in RESULTS.items():
        say(f"  {k}: {'HIT' if v['hit'] else 'MISS'}")
    say(f"  Q2 bands: P7 {band7}, P8 {band8}")
    say(f"run time {secs:.1f} s, max RSS {rss:.0f} MB")
    with open(OUT_JSON, "w") as f:
        json.dump(dict(facts=facts, results=RESULTS, chains=chains, bands=dict(P7=band7, P8=band8),
                       seconds=secs, max_rss_mb=rss), f, indent=1, default=str)


if __name__ == "__main__":
    main()

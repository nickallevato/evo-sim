"""B9: does Day's "rendered infertile and gone extinct within centuries" come out "remotely close" when mathed out?
Low-stakes tier (one combined review, REVIEW-R4-B9-combined.md).  Arithmetic only, stdlib only; run locally.
Run:  research/.venv/bin/python -I research/checks/b9_relaxed_load.py
Pre-registered: committed BEFORE the main run.

DISCLOSURE (mandatory).  An exploratory version of reading A was computed in chat on 2026-10-11 BEFORE this file was
written: d = 0.5% halve ~3,500 y / to-10% ~11,500 y; 1% ~1,700 / ~5,700; 2% ~860 / ~2,850; 5% ~340 / ~1,100; Day's
premise 2 at 0.1% effect ~220 / ~740; fixation reading ~1e6 y.  So this is a pre-registration of the GRID, the
CRITERION and the VERDICT MAPPING, not of blind predictions.  The numbers below are known in advance.

TARGET.  Claim B9, quote Q104 (Vox Day, McCarthy Substack comment 337302874, 2026-09-15, last paragraph; local copy
sources/raw/refresh-2026-10-09/mccarthy-comments-why/comments.json, verified as substrings by this script):
  "So if genetic drift were capable of producing actual changes to the genome, the human species would have been
   rendered infertile and gone extinct within centuries."
  Premises, same comment: "1. For neutral substitution to work to fixation at its maximum speed, natural selection
  cannot be operating."  "2. There are 3x more harmful substitutions than neutral substitutions."  Also, same comment:
  "There are 3x more harmful mutations than neutral ones." and "every single neutral substitution requires ~one
  million years apiece to fixate."

OWNER'S RH DECISION RULE (owner, in chat, 2026-10-11): grade Q104 `dialectic` if the literal claim is "remotely
close" when mathed out under the most charitable reading (rule C); `rhetoric` if not.
OPERATIONAL CRITERION (fixed now): "centuries" = 100-999 years.  Q104 is DIALECTIC if the charitable-reading CENTRAL
RANGE overlaps [100, 999] y or lies within one order of magnitude (10x) of it, i.e. intersects [10, 9,990] y.
Otherwise (central range wholly < 10 y or wholly > 9,990 y) it is RHETORIC.
  Central range (fixed now) = min..max years over Lynch 2016's three anchor values of the per-generation decline,
  d in {0.5% (mouse extrapolation), 1% (central), 5% (upper)}, and both thresholds W = 0.5 and W = 0.1.
  Reported but not used for the criterion: Lynch's full grid (deleterious fraction 1-10% x mean effect), the
  Drosophila 0.2-2% rows, Day's premise 2 rows, and reading B.

READINGS.
  (A, charitable under rule C; "rendered infertile" = mutation load) Selection fully relaxed (premise 1 taken as the
     state of the world), new deleterious mutations accumulate.  Multiplicative independent effects:
     W_t = (1 - d)^t, d = U x f x s per generation (U new mutations per diploid genome, f deleterious fraction,
     s mean fitness effect).  Report generations and years (25 y/gen, parameters.yaml generation_time_years.day_2026)
     to W = 0.5 and W = 0.1.
     Inputs, Lynch 2016 (Genetics 202:869; local sources/raw/refresh-2026-10-09b/lit/txt/Lynch2016.txt, verified as
     substrings by this script): "∼100×0.01×1%=1% per generation"; "as high as 5% per generation"; mouse
     "Extrapolating by dividing by 6.7 suggests a human decline rate of ∼0.5%"; Drosophila "0.2–2% decline in fitness
     per generation"; "1–10% of all human mutations"; "on the order of 1% per mutation"; and the hedge "Owing to the
     indirect way in which this estimate of the recurrent human mutation load has been obtained".
     Grid: U = 100; f in {1, 2, 5, 10}%; s in {0.1, 0.2, 0.5, 1, 2}%.
     Day's premise 2: 3:1 harmful:neutral => f = 0.75; U in {76.8 (2 x 38.4, parameters.yaml
     mutation.new_mutations_per_haploid_genome), 100}; s in {0.1, 0.2, 0.5, 1}%.
  (B, literal "substitutions") Harmful mutations behaving neutrally fix after ~4 Ne generations (Kimura & Ohta 1969,
     quotes-literature.md: "takes about 4Ne generations until fixation"); Ne in {1.0e4 (Takahata 1995), 1.31e4,
     1.62e4 (Prado-Martinez 2013 Table 1, humans)}; g = 25 y.  Expected ~1e6 y.

PREDICTIONS (known from the exploratory run; see disclosure)
  Day side: on his own premise 2, reading A gives decline within a few centuries (claim if anything understated).
  Critic side: the relaxed-selection arithmetic is not at issue; premise 1 is false (neutral sites fix at k = mu while
    selection purges clearly deleterious mutations concurrently), so the antecedent never obtains.
  Audit: P1 central range ~340 to ~11,500 y => intersects [10, 9,990] (and [100, 999]) => DIALECTIC.
         P2 Day premise 2 rows: all within [10, 999] y.   P3 reading B ~1.0e6-1.6e6 y (>= 1,000x centuries).
         P4 Lynch full grid spans < 100 y (f 10%, s 2%) to > 1e4 y (f 1%, s 0.1%).
VERDICT MAPPING (fixed now)
  If DIALECTIC: RH tag `dialectic`.  Internal: non-sequitur -> holds (the old N2a basis, "within centuries" vs "~one
    million years apiece", applies only to reading B, which rule C sets aside).  External: -> contradicted, because
    premise 1 is false under standard theory: Kimura 1962 gives fixation probabilities for selected and neutral alleles
    in the same population at once (quotes-literature.md Kimura1962: "if we let s → 0 in (10), we obtain U = 1/2N, the
    result known for a neutral gene"), and k = mu at neutral loci (BallouxLehmann2012 citing Kimura & Ohta 1971,
    Kimura 1983); the antecedent never obtains.  GAP-05 (fixation of slightly deleterious |Ne s| ~ 1 mutations) stays
    open and is credited as Day's best point.  Fidelity stays unverifiable (premise 2 uncited).
  If RHETORIC (central range wholly > 9,990 y or < 10 y): RH tag `rhetoric`; Q104 is not literal-fact-checked; device,
    audience, function and dialectical core go to ledgers/slips.md; internal -> n/a (rhetoric changes no verdict);
    external stays on the premise-1 question (contradicted) for the dialectical core.
CAVEATS: multiplicative independent-effects model; W thresholds arbitrary; Lynch calls his estimate indirect;
  ignores the reproductive-excess reserve (absolute fertility, not relative W, decides extinction).
"""
import hashlib
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
LYNCH = os.path.join(ROOT, "sources", "raw", "refresh-2026-10-09b", "lit", "txt", "Lynch2016.txt")
COMM = os.path.join(ROOT, "sources", "raw", "refresh-2026-10-09", "mccarthy-comments-why", "comments.json")
LYNCH_Q = ["∼100×0.01×1%=1% per generation", "as high as 5% per generation",
           "Extrapolating by dividing by 6.7 suggests a human decline rate of ∼0.5%",
           "0.2–2% decline in fitness per generation", "1–10% of all human mutations",
           "on the order of 1% per mutation",
           "Owing to the indirect way in which this estimate of the recurrent human mutation load has been obtained"]
DAY_Q = ["rendered infertile and gone extinct within centuries",
         "1. For neutral substitution to work to fixation at its maximum speed, natural selection cannot be operating.",
         "2. There are 3x more harmful substitutions than neutral substitutions.",
         "There are 3x more harmful mutations than neutral ones.",
         "requires ~one million years apiece to fixate"]
G = 25.0
CENT = (100.0, 999.0)
BAND = (10.0, 9990.0)


def verify(path, quotes):
    b = open(path, "rb").read()
    t = re.sub(r"\s+", " ", b.decode("utf-8", "replace"))
    print(f"{os.path.relpath(path, ROOT)} sha256 {hashlib.sha256(b).hexdigest()}")
    for q in quotes:
        print(f"  {'OK  ' if q in t else 'MISS'} {q}")


def gens_to(d, w):
    return math.log(w) / math.log(1.0 - d)


def row(label, d):
    g5, g1 = gens_to(d, 0.5), gens_to(d, 0.1)
    print(f"| {label} | {100 * d:.3g}% | {g5:.1f} | {g5 * G:,.0f} | {g1:.1f} | {g1 * G:,.0f} |")
    return g5 * G, g1 * G


def main():
    verify(LYNCH, LYNCH_Q)
    verify(COMM, DAY_Q)
    hdr = "| case | d per gen | gens to W=0.5 | years | gens to W=0.1 | years |\n|---|---|---|---|---|---|"

    print("\n## Reading A: Lynch anchors (define the central range)\n" + hdr)
    central = []
    for lab, d in [("Lynch mouse extrapolation", 0.005), ("Lynch central 100x0.01x1%", 0.01),
                   ("Lynch upper", 0.05)]:
        central += row(lab, d)
    lo, hi = min(central), max(central)
    print(f"\nCentral range: {lo:,.0f} - {hi:,.0f} y")

    print("\n## Reading A: Drosophila equal-family-size range (reported)\n" + hdr)
    for d in (0.002, 0.02):
        row("Drosophila (Lynch cites)", d)

    print("\n## Reading A: Lynch grid, U = 100, f x s (years to W=0.5 / W=0.1)")
    S = [0.001, 0.002, 0.005, 0.01, 0.02]
    print("| f \\ s | " + " | ".join(f"{100 * s:g}%" for s in S) + " |\n|---|" + "---|" * len(S))
    grid = []
    for f in (0.01, 0.02, 0.05, 0.10):
        cells = []
        for s in S:
            d = 100 * f * s
            a, b = gens_to(d, 0.5) * G, gens_to(d, 0.1) * G
            grid += [a, b]
            cells.append(f"d {100 * d:.3g}%: {a:,.0f} / {b:,.0f}")
        print(f"| {100 * f:g}% | " + " | ".join(cells) + " |")
    print(f"\nGrid span: {min(grid):,.0f} - {max(grid):,.0f} y")

    print("\n## Reading A: Day's premise 2 (f = 0.75)\n" + hdr)
    day = []
    for U in (76.8, 100.0):
        for s in (0.001, 0.002, 0.005, 0.01):
            d = U * 0.75 * s
            day += row(f"U {U:g}, s {100 * s:g}%", d)
    print(f"\nDay premise-2 span: {min(day):,.1f} - {max(day):,.1f} y")

    print("\n## Reading B: neutral-like fixation time 4 Ne generations, g = 25 y")
    print("| Ne | gens | years | x upper 'centuries' (999 y) |\n|---|---|---|---|")
    for ne in (1.0e4, 1.31e4, 1.62e4):
        print(f"| {ne:.3g} | {4 * ne:,.0f} | {4 * ne * G:,.0f} | {4 * ne * G / CENT[1]:,.0f}x |")

    print("\n## Criterion")
    ov = lo <= CENT[1] and hi >= CENT[0]
    band = lo <= BAND[1] and hi >= BAND[0]
    print(f"central range {lo:,.0f}-{hi:,.0f} y; overlaps 100-999 y: {ov}; intersects 10-9,990 y: {band}")
    print(f"RH tag: {'DIALECTIC' if band else 'RHETORIC'}")
    print(f"P1 (~340..~11,500, dialectic): {'HOLDS' if band and 300 < lo < 400 and 11000 < hi < 12000 else 'MISS'}")
    print(f"P2 (Day premise 2 all within 10-999 y): {'HOLDS' if min(day) >= 10 and max(day) <= 999 else 'MISS'}")
    print(f"P3 (reading B >= 1,000x centuries): {'HOLDS' if 4 * 1e4 * G / CENT[1] >= 1000 else 'MISS'}")
    print(f"P4 (grid < 100 to > 1e4 y): {'HOLDS' if min(grid) < 100 and max(grid) > 1e4 else 'MISS'}")


if __name__ == "__main__":
    main()

"""R4-RHclose: the owner's RH rule (2026-10-11) applied to two unresolved tags, C7 (Q96) and the Hard Limits peroration
(Q157, Q158).  Low-stakes tier (one combined review, REVIEW-R4-RHclose-combined.md).  Arithmetic only, stdlib only;
run locally.  Model check: R4-B9 (b9_relaxed_load.py) and its review's MAJOR-3 (loose criterion, one anchor suffices).
Run:  research/.venv/bin/python -I research/checks/rhclose.py > research/checks/results/raw/rhclose.out
Pre-registered: committed BEFORE the main run.

DISCLOSURE (mandatory).
  - The owner discussed the "pipe" readings of Q157/Q158 in chat on 2026-10-11; no numbers were computed in that chat.
  - Most of the Q157/Q158 numbers are ALREADY KNOWN from R4-B2 (post hoc table, b2_posthoc.py): exact fill F at HL's own
    input (variance N_e 57,143, 6.5 My) 0.70, delivered fraction 0.26; at 2 My 0.026 / 0.003; field N_e 1e4 over 6.5 My
    1.00 / 0.85.  The C7 drift variance t/(2 N_e) is textbook arithmetic (about 0.014 at N_e 1e4, 280 generations), and
    R4-C1d's measured F_adj (0.002-0.014) is known.  So this pre-registers the READINGS, the CRITERIA, the INPUT SETS and
    the VERDICT MAPPING, not blind predictions.  The criterion form was chosen with these numbers in view; the bands are
    the B9 review's tighter 3x band, not B9's 10x band.

OWNER'S RH RULE (2026-10-11, first applied in R4-B9): tag a statement `dialectic` if the literal claim is "remotely
close" when mathed out under the most charitable reading (rule C), `rhetoric` if not.  Rule C here ranges over
ambiguous referents and over the sourced (or the author's own stated) inputs; it does not replace the stated mechanism
(B9 review MAJOR-1).  Inputs that are neither sourced nor stated by the author in the text at issue are reported, not
used for the criterion (rule F), as B9 did with Day's premise-2 rows.

=====================================================================================================================
PART 1.  C7, Q96 (Vox Day, McCarthy Substack comment 335823489, 2026-09-13; local
  sources/raw/refresh-2026-10-09/mccarthy-comments-why/comments.json, verified as a substring below):
  "And we've now got hard evidence that genetic drift isn't happening at all over the last 7000 years, and that there
   is a hard population limit on the neutral pipeline."
READING.  Literal: genetic drift = random change of allele frequency by finite sampling (Day's own usage in Z18320599,
  2026-01-10, local sources/raw/day/zenodo-18320599.txt: "The effective population size N_{e} governs the relative
  strength of genetic drift versus natural selection in determining allele frequency trajectories"; he there "measured
  drift variance").  The fixation-count reading ("no drift-driven fixations from below 50%") is not a reading of
  "genetic drift isn't happening" but of Day's evidence (claim C); it is the dialectical core if the tag is rhetoric.
QUANTITY.  Expected standardized drift variance over the window, F_drift = 1 - (1 - 1/(2 N_e))^t (neutral, Wright-Fisher;
  N_e piecewise: 1 - prod (1 - 1/(2 N_e,k))^t_k), and SD of drift-driven change at p = 0.5, sqrt(0.25 F_drift).
  t = 7,000 y / 25 y = 280 generations (parameters.yaml generation_time_years.day_2026); 20 y (350 gen) reported.
LITERAL BAND ("not at all", fixed now): F_drift <= 1e-4 over the whole window (SD of a 50% allele's drift change
  <= 0.5 percentage points in 7,000 y).
CRITERION (fixed now): C7 is DIALECTIC if the CHARITABLE CENTRAL VALUE, min F_drift over the central input set at
  t = 280, is <= 3e-4 (3x band); otherwise RHETORIC.  10x band (<= 1e-3) reported, not used.
CENTRAL INPUT SET (sourced, parameters.yaml population.*): constant N_e in {1.0e4 (Takahata 1995; Ne_modern_human),
  1.31e4, 1.62e4 (Prado-Martinez 2013 Table 1, humans), 2.0e4 (Charlesworth 2009 upper)}.
REPORTED, NOT USED: R4-C1d measured temporal N_e 9,665 (BA-Medieval pooled; a lower bound on a drift N_e); stylised
  RG-01 growth (N_e 1e4 then 1e5 for the last 1,000 y; fast growth 1e4 for 2,000 y then 1e5 for 5,000 y); Day-frame
  Wright N_e = 4N/(V_k+2), V_k = 5, at census N in {1e5, 1e6, 1e7} held for 7,000 y (census unsourced, not stated in
  Q96); Day's own Z18320599 measured "drift variance" 0.00150-0.00495 per 500-y step (pan-European; 0.00330-0.01514
  Britain-only), with his caveat that it includes structure and migration.
PREDICTIONS.
  Day side: drift is negligible in the window (large Holocene populations); the claim is close on a census-scale N_e.
  Critic side: drift at N_e ~ 1e4 moves frequencies by several percentage points in 280 generations; "not at all" is
    far off (and Day's own January paper measured the drift variance).
  Audit: P1 central F_drift 0.0070 (N_e 2e4) to 0.0139 (N_e 1e4) => min 0.0070 > 3e-4 (about 23x) => RHETORIC.
         P2 Day-frame F at census 1e6 and 1e7 <= 3e-4 (the tag flips on Day's unsourced census frame).
VERDICT MAPPING (C7; fixed now)
  If DIALECTIC: RH `dialectic`; internal stays `non-sequitur` (C's basis: ~0 completions from < 50% is the neutral
    expectation, X1 row C, so the aDNA count is not evidence of no drift); external stays `contradicted` (R4-C1d F_adj
    0.002-0.014 between bins).
  If RHETORIC: RH `rhetoric`; Q96 is not literal-fact-checked; internal `non-sequitur` -> n/a and external
    `contradicted` -> n/a for C7 (rhetoric changes no verdict); the dialectical core (zero fixations from < 50% / < 10%
    in 7,000 y read as evidence against drift, and the B2 ceiling) is scored at C and B2; device, audience, function,
    core and a better-rhetoric answer go to ledgers/slips.md (integration).

=====================================================================================================================
PART 2.  Q157, Q158 (Hard Limits, Z22129121, 2026-08-27; local sources/raw/day/zenodo-22129121.txt, read-only, verified
  below).  Q157 l.453-456: "the neutral substitutions cannot be finished, because the pipe that would finish them never
  fills. Both the priced channel and the free channel shut inside the same lineage duration."  Q158 l.464-467: "for
  every large animal it had ever dated, the pipe was nearly empty."
DAY'S MODEL (HL l.283-300): "k(T) = μ · F(T), F(T) = P(τ ≤ T | fixation)", the exact first-passage law ("it can be
  written down exactly"), with the short-time law "F(T) ∼ exp( − π² Nₑ / T ), T ≪ 4Nₑ"; fill = F (l.272-275 "reaches
  the k = μ flux only after it has spent enough time to load every one of its pipes"; Q152 l.362-363 "the pipe
  substantially fills, and Kimura's rate is approached"; Table 3 "flux/μ (bound)" with the linear bound T/4Nₑ); for a
  changing population the clock is "the drift exposure ∫ dt/4Nₑ(t)" (l.432-433).
QUANTITY.  F(x) = 1 + sum_i (-1)^i (2i+1) exp(-i(i+1) x / 4), x = ∫ dt / N_e(t) (generations), for a mutation entering
  at the start of the window (empty start: the charitable case for "empty"; any pre-window fill, e.g. Day's B1d "full
  ... at the time of the CHLCA split", only raises it).  Kimura (1955) diffusion conditional on fixation, p -> 0;
  neutral diffusion with changing N_e is the same process on the clock x.  Reported, not used: Day's exp law
  exp(-π²/x) (outside its stated domain T ≪ 4N_e when x >~ 1), the linear bound x/4, and the delivered fraction
  D = (1/T) ∫_0^T F(x(T) - x(s)) ds (Day's own μL∫F, Q34).
REFERENT (rule C).  "Lineage duration" is a defined term in HL: l.249 "Use the lineage duration, the full continuous
  ancestry, which in the case of the human lineage is roughly six and a half million years" (Table 1, T = 6.5 My).
  So the window is the human lineage, 6.5 My (also 6.3 My, Z23003785), g = 25 y.  H8's 2 My window (l.364-366, and
  l.416 "thirty-five percent fill across two million years even when granted the entire lineage") is R4-B2's slip
  (internal window mismatch); reported, not used.  The current-size reading S (the pipe at today's census never
  fills = B2) changes the referent away from "inside the same lineage duration" and "every large animal it had ever
  dated" (the dated pipe is the lineage's, l.438-441); reported; if the owner prefers S, the line restates B2, which
  holds, and B's verdict is the same as under the rhetoric tag.
LITERAL BAND ("never fills" / "nearly empty", one passage family, fixed now): F <= 0.10.
CRITERION (fixed now): Q157/Q158 are DIALECTIC if the CHARITABLE CENTRAL VALUE, min F over the central input set, is
  <= 0.30 (3x band); otherwise RHETORIC.  (A multiplicative 10x band is meaningless for a fraction capped at 1.)
CENTRAL INPUT SET (human lineage, empty start, T in {6.3, 6.5} My):
  (a) HL's own variance N_e: H8 census 1e5, V_k 5 -> N_e = 4N/(V_k+2) = 57,143 (= Day's B1d 228,000/4), constant.
  (b) field N_e 1.0e4 constant (Takahata 1995; Ne_modern_human).
  (c) field N_e 1.62e4 constant (Prado-Martinez 2013 Table 1, humans, upper).
  (d) Takahata 1995 two-epoch: ~1e5 before 4.6 My ago ("nearly 10 times larger"), 1e4 after.
REPORTED, NOT USED: H8 as written (2 My); Takahata 1e5 held for the whole lineage; Yoo 2025 HCB ancestral 1.98e5 held
  for the whole lineage (a pre-split ancestral N_e, not a lineage value); exp law and linear bound; D; elephant (the
  only other large animal HL names with inputs, Table 1: T 2.0 My, g 22, V_k 3, census 415,000, ceiling X 28,000):
  Day-frame N_e at census (current-size reading) and at X.  No sourced elephant lineage N_e is in the repo.
PREDICTIONS.
  Day side: on HL's own input the lineage pipe is far from full; the line is a fair summary.
  Critic side: on any sourced lineage N_e the pipe fills (F ~ 1); "nearly empty" is false; Day's own text says
    "partly-filled" (l.419) and "short enough to fill" (Q151).
  Audit: P3 F(a, 6.5 My) = 0.70 +/- 0.02; F(a, 6.3 My) in [0.66, 0.70]; F(b), F(c), F(d) >= 0.95.
         P4 charitable central value = F(a, 6.3 My) ~ 0.68 > 0.30 => RHETORIC.
         P5 D(a, 6.5 My) ~ 0.26 <= 0.30: the tag would flip if D were the fill measure (disclosed; not used).
         P6 H8 as written (2 My): F ~ 0.026 <= 0.10, i.e. "nearly empty" is literally true on H8's slip window.
VERDICT MAPPING (B; fixed now; R4-B2 "Rule N")
  If DIALECTIC: Q157, Q158 tagged `dialectic`, added to B's Statement (S1); B internal pending -> `non-sequitur`
    (N2b within HL: the line needs a nearly empty lineage pipe, which Q140 l.23-25, Q151 l.354-356, Q152 l.362-363,
    Q156 l.440-441 and l.416-419 "a partly-filled pipe" exclude).
  If RHETORIC: Q157, Q158 tagged `rhetoric`; not literal-fact-checked; dialectical core = B2 (current-size confinement,
    `holds`); B internal pending -> `holds` (HL basis); RH entries (device, audience, function, core, better-rhetoric
    answer) to ledgers/slips.md at integration.  External for B stays with B1c / B4a (ancestral fill and counts).
CAVEATS: constant-size epochs; diffusion limit; F is the end-of-window flux for the cohort entering at the start, D the
  delivered share; C7's F_drift is the neutral expectation, not the measured total (C1d's F_adj contains non-drift
  terms); RH tags classify statements, they do not make them true.
"""
import hashlib
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
COMM = os.path.join(ROOT, "sources", "raw", "refresh-2026-10-09", "mccarthy-comments-why", "comments.json")
HL = os.path.join(ROOT, "sources", "raw", "day", "zenodo-22129121.txt")
HOL = os.path.join(ROOT, "sources", "raw", "day", "zenodo-18320599.txt")
COMM_Q = ["genetic drift isn't happening at all over the last 7000 years, and that there is a hard population limit "
          "on the neutral pipeline."]
HL_Q = ["k(T) = μ · F(T), F(T) = P(τ ≤ T | fixation)",
        "F(T) ∼ exp( − π² Nₑ / T ), T ≪ 4Nₑ",
        "the neutral substitutions cannot be finished, because the pipe that would finish them never fills. Both the "
        "priced channel and the free channel shut inside the same lineage duration.",
        "for every large animal it had ever dated, the pipe was nearly empty.",
        "the pipe substantially fills, and Kimura’s rate is approached.",
        "Use the lineage duration, the full continuous ancestry, which in the case of the human lineage is roughly six "
        "and a half million years",
        "the one that reached thirty-five percent fill across two million years even when granted the entire lineage",
        "a partly-filled pipe",
        "when the populations were small and their pipes short enough to fill",
        "residual drainage from the smaller populations they descend from",
        "loaded, at least partially",
        "the drift exposure ∫ dt/4Nₑ(t)",
        "A population reaches the k = μ flux only after it has spent enough time to load every one of its pipes"]
HOL_Q = ["governs the relative strength of genetic drift versus natural selection in determining allele frequency "
         "trajectories",
         "The minimum observed drift variance was 0.00150 (750-1250 BP, Medieval period) and the maximum was 0.00495",
         "Minimum drift variance was 0.00330 (5000-6000 BP, Middle Neolithic) and maximum was 0.01514",
         "Drift variance as measured here reflects the combined effects of genetic drift, residual population "
         "structure, and migration"]
G = 25.0


def verify(path, quotes):
    b = open(path, "rb").read()
    t = re.sub(r"\s+", " ", b.decode("utf-8", "replace")).replace("\\n", " ")
    t = re.sub(r"\s+", " ", t)
    print(f"{os.path.relpath(path, ROOT)} sha256 {hashlib.sha256(b).hexdigest()}")
    miss = 0
    for q in quotes:
        ok = q in t
        miss += not ok
        print(f"  {'OK  ' if ok else 'MISS'} {q}")
    return miss


# ---------------------------------------------------------------- Part 1: C7
def f_drift(epochs):  # epochs: list of (generations, N_e)
    keep = 1.0
    for t, ne in epochs:
        keep *= (1.0 - 1.0 / (2.0 * ne)) ** t
    return 1.0 - keep


def c7_row(label, epochs):
    f = f_drift(epochs)
    print(f"| {label} | {f:.3g} | {100 * math.sqrt(0.25 * f):.2f} | {f / 1e-4:,.1f}x |")
    return f


# ---------------------------------------------------------------- Part 2: pipe fill
def F(x):
    """Kimura (1955) neutral fixation-time CDF conditional on fixation, p -> 0; x = T / N_e (generations)."""
    if x <= 0:
        return 0.0
    n = int(math.sqrt(4 * 45 / x)) + 3
    terms = [1.0] + [(-1) ** i * (2 * i + 1) * math.exp(-i * (i + 1) * x / 4) for i in range(1, n)]
    return max(math.fsum(terms), 0.0)


def clock(epochs):  # epochs oldest first: list of (generations, N_e); returns total x and a function x(s)
    edges, acc, t0 = [], 0.0, 0.0
    for t, ne in epochs:
        edges.append((t0, t0 + t, acc, ne))
        acc += t / ne
        t0 += t

    def x_at(s):
        for a, b, xa, ne in edges:
            if s <= b:
                return xa + (s - a) / ne
        return acc
    return acc, t0, x_at


def delivered(epochs, m=4000):
    X, T, x_at = clock(epochs)
    h = T / m
    tot = 0.0
    for k in range(m + 1):
        w = 1 if k in (0, m) else (4 if k % 2 else 2)
        u = X - x_at(k * h)
        tot += w * (F(u) if u > 0.02 else 0.0)
    return tot * h / 3 / T


def pipe_row(label, epochs):
    X, T, _ = clock(epochs)
    f = F(X)
    expl = math.exp(-math.pi ** 2 / X)
    d = delivered(epochs)
    fs = f"{f:.3g}" if f > 1e-12 else "< 1e-12"
    print(f"| {label} | {T * G / 1e6:.2f} | {X:.3g} | {fs} | {expl:.3g} | {min(X / 4, 1):.3g} | {d:.3g} |")
    return f, d


def main():
    miss = verify(COMM, COMM_Q) + verify(HL, HL_Q) + verify(HOL, HOL_Q)
    print(f"quote misses: {miss}")

    # self-test against R4-B2's post hoc table (constant N_e): x 4.55 -> 0.70/0.26, 8 -> 0.95/0.51, 26 -> 1.00/0.85
    print("\nself-test vs R4-B2 (x: F, D):",
          ", ".join(f"{x}: {F(x):.3f}/{delivered([(x * 1e4, 1e4)]):.3f}" for x in (1.4, 4.0, 4.55, 8.0, 26.0)))

    # ---------------- Part 1
    t25, t20 = 7000 / 25.0, 7000 / 20.0
    hdr = "| case | F_drift | SD of drift change at p=0.5 (pct points) | x literal band 1e-4 |\n|---|---|---|---|"
    print("\n## Part 1 (C7): central set, t = 280 generations (25 y)\n" + hdr)
    central = [c7_row(f"N_e {ne:.3g}", [(t25, ne)]) for ne in (1.0e4, 1.31e4, 1.62e4, 2.0e4)]
    print("\n## Part 1: reported, not used\n" + hdr)
    for ne in (1.0e4, 2.0e4):
        c7_row(f"N_e {ne:.3g}, 20 y/gen (350 gen)", [(t20, ne)])
    c7_row("C1d measured temporal N_e 9,665 (lower bound)", [(t25, 9665)])
    c7_row("growth: 1e4 for 6,000 y, 1e5 last 1,000 y", [(6000 / G, 1e4), (1000 / G, 1e5)])
    c7_row("fast growth: 1e4 for 2,000 y, 1e5 for 5,000 y", [(2000 / G, 1e4), (5000 / G, 1e5)])
    dayf = []
    for n in (1e5, 1e6, 1e7):
        ne = 4 * n / 7
        dayf.append(c7_row(f"Day frame census {n:.0e}, V_k 5 -> N_e {ne:,.0f}", [(t25, ne)]))
    print("Day Z18320599 measured drift variance per 500-y step: pan-European 0.00150-0.00495; Britain 0.00330-0.01514"
          " (raw Var(dp), includes structure/migration by his caveat)")
    cmin = min(central)
    tag1 = "DIALECTIC" if cmin <= 3e-4 else "RHETORIC"
    print(f"\nC7 charitable central value (min F_drift) = {cmin:.4g}; 3x band edge 3e-4 -> {cmin / 3e-4:.1f}x; "
          f"10x band edge 1e-3 -> {cmin / 1e-3:.1f}x")
    print(f"C7 RH tag: {tag1}")
    print(f"P1 (central 0.0070..0.0139, rhetoric): "
          f"{'HOLDS' if tag1 == 'RHETORIC' and 0.0065 < cmin < 0.0075 and 0.0135 < max(central) < 0.0143 else 'MISS'}")
    print(f"P2 (Day frame at census 1e6, 1e7 <= 3e-4): {'HOLDS' if dayf[1] <= 3e-4 and dayf[2] <= 3e-4 else 'MISS'}")

    # ---------------- Part 2
    ph = ("| case | T (My) | x = ∫dt/N_e | exact F (fill) | Day exp law | linear x/4 | delivered D |\n"
          "|---|---|---|---|---|---|---|")
    print("\n## Part 2 (Q157/Q158): central set, human lineage, empty start\n" + ph)
    cen, res = [], {}
    for T in (6.3e6, 6.5e6):
        gens = T / G
        cases = [("(a) HL variance N_e 57,143", [(gens, 4e5 / 7)]),
                 ("(b) N_e 1.0e4", [(gens, 1e4)]),
                 ("(c) N_e 1.62e4", [(gens, 1.62e4)]),
                 ("(d) Takahata 1e5 before 4.6 My, 1e4 after", [((T - 4.6e6) / G, 1e5), (4.6e6 / G, 1e4)])]
        for lab, ep in cases:
            f, d = pipe_row(f"{lab}, {T / 1e6:g} My", ep)
            cen.append(f)
            res[(lab[:3], T)] = (f, d)
    print("\n## Part 2: reported, not used\n" + ph)
    h8 = pipe_row("H8 as written: N_e 57,143, 2 My", [(2e6 / G, 4e5 / 7)])
    pipe_row("Takahata 1e5 whole lineage, 6.5 My", [(6.5e6 / G, 1e5)])
    pipe_row("Yoo HCB ancestral 1.98e5 whole lineage, 6.5 My", [(6.5e6 / G, 1.98e5)])
    pipe_row("elephant, Day frame at census 415,000 (N_e 332,000), 2 My, g 22", [(2e6 / 22, 4 * 415000 / 5)])
    pipe_row("elephant at Day's ceiling X 28,000 (N_e 22,400), 2 My, g 22", [(2e6 / 22, 4 * 28000 / 5)])
    print("(elephant rows: T column uses g = 25 for display only; x uses g = 22)")
    pmin = min(cen)
    tag2 = "DIALECTIC" if pmin <= 0.30 else "RHETORIC"
    print(f"\nQ157/Q158 charitable central value (min F) = {pmin:.3f}; literal band 0.10 -> {pmin / 0.10:.1f}x; "
          f"3x edge 0.30 -> {pmin / 0.30:.2f}x")
    print(f"Q157/Q158 RH tag: {tag2}")
    fa65, da65 = res[("(a)", 6.5e6)]
    fa63 = res[("(a)", 6.3e6)][0]
    others = [v[0] for k, v in res.items() if k[0] != "(a)"]
    print(f"P3 (F(a,6.5)=0.70+/-0.02; F(a,6.3) in [0.66,0.70]; b,c,d >= 0.95): "
          f"{'HOLDS' if abs(fa65 - 0.70) <= 0.02 and 0.66 <= fa63 <= 0.70 and min(others) >= 0.95 else 'MISS'}")
    print(f"P4 (min = F(a,6.3) ~0.68 > 0.30 -> rhetoric): "
          f"{'HOLDS' if tag2 == 'RHETORIC' and pmin == fa63 else 'MISS'}")
    print(f"P5 (D(a,6.5) ~0.26 <= 0.30): {'HOLDS' if da65 <= 0.30 else 'MISS'} (D = {da65:.3f})")
    print(f"P6 (H8 2 My F ~0.026 <= 0.10): {'HOLDS' if h8[0] <= 0.10 else 'MISS'} (F = {h8[0]:.4f})")


if __name__ == "__main__":
    main()

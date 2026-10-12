# R4 RHclose: the owner's RH rule applied to C7 (Q96) and the Hard Limits peroration (Q157, Q158)

**Status: pre-registered (7185f1e), run, written up. Awaiting the combined review** (`REVIEW-R4-RHclose-combined.md`, a separate agent). Low-stakes tier: RH tagging plus arithmetic. Not integrated: no claim file, quote tag, ledger, QUEUE or argmap edits yet. The verdict moves below are **proposed**.

## Files
- Script `research/checks/rhclose.py`, pre-registered at **7185f1e**. Readings, criteria, input sets, predictions and the verdict mapping are in its docstring. It was run locally once after that commit (stdlib arithmetic, a few seconds) and has not been edited since.
- Raw output `research/checks/results/raw/rhclose.out`.
- Sources. All are verified as whitespace-normalised substrings by the script, with one glyph exception (see below):
  - Day comment 335823489: `sources/raw/refresh-2026-10-09/mccarthy-comments-why/comments.json`, sha256 cba6b15b...da92bc.
  - Hard Limits (Z22129121, 2026-08-27): `sources/raw/day/zenodo-22129121.txt`, sha256 3182a5b6...9dfe2.
  - Day, "Temporal Variation in Effective Population Size Across the Holocene" (Z18320599, 2026-01-10): `sources/raw/day/zenodo-18320599.txt`, sha256 78e62f7d...8caa.
  - **One MISS, a glyph mismatch only.** The script copied Q152 from `quotes-day.md` with a curly apostrophe ("Kimura’s"). The local text has a straight one: l.363 reads "the pipe substantially fills, and Kimura's rate is approached" (confirmed by grep). The quote is present.

## Disclosure (read first)
- The owner discussed the "pipe" readings of Q157/Q158 in chat on 2026-10-11. **No numbers were computed in that chat.**
- Most of the Part 2 numbers were already known from R4-B2's post hoc table. At HL's own input (6.5 My) they are F 0.70 and D 0.26; on the 2 My window, 0.026 and 0.003; at field N_e 1e4, 1.00 and 0.85. The C7 drift variance is textbook arithmetic, and R4-C1d's measured F_adj was also known.
- So what was pre-registered is the readings, criteria, input sets and mapping, not blind predictions. The criterion form was chosen with these numbers in view. To answer the B9 review's MAJOR-3, it uses the **3x band** (the tighter band from that review), not B9's 10x band. "Holds" scores below confirm arithmetic only.

## Target and owner rule
- **Owner rule (2026-10-11, first applied in R4-B9):** tag a statement `dialectic` if the literal claim is "remotely close" when mathed out under the most charitable reading (rule C), and `rhetoric` if not.
- Rule C here ranges over ambiguous referents and over sourced inputs, or inputs the author states in the text at issue. It does not replace the stated mechanism (B9 review MAJOR-1).
- Unsourced inputs are reported but not used (rule F), the same way B9 handled Day's premise-2 rows.
- **C7, Q96** (Vox Day, McCarthy Substack comment 335823489, 2026-09-13): "And we've now got hard evidence that genetic drift isn't happening at all over the last 7000 years, and that there is a hard population limit on the neutral pipeline."
- **Q157** (HL l.453-456): "the neutral substitutions cannot be finished, because the pipe that would finish them never fills. Both the priced channel and the free channel shut inside the same lineage duration."
- **Q158** (HL l.464-467): "for every large animal it had ever dated, the pipe was nearly empty."

## Part 1: C7

### Reading and criterion (pre-registered)
- **Reading.** Drift means random change of allele frequency. This is Day's own usage in Z18320599 (Introduction): "The effective population size N_{e} ... governs the relative strength of genetic drift versus natural selection in determining allele frequency trajectories". In that paper he "measured drift variance".
- **The fixation-count reading is the evidence, not the claim.** "No drift-driven fixations from below 50%" is a reading of Day's evidence (claim C), not of "genetic drift isn't happening". It is the dialectical core if the tag is rhetoric.
- **Quantity.** F_drift = 1 - (1 - 1/2N_e)^t over t = 280 generations (7,000 y at 25 y).
- **Literal band ("not at all").** F_drift <= 1e-4, which means a 50% allele drifts by at most 0.5 percentage points (SD) in 7,000 y.
- **Criterion.** Dialectic if min F_drift over the sourced central set (N_e 1.0e4, 1.31e4, 1.62e4, 2.0e4) is <= 3e-4.

### Results (rounded from raw output)
| case | F_drift | SD of drift change at p = 0.5 (percentage points) | x literal band |
|---|---|---|---|
| N_e 1.0e4 (Takahata 1995) | 0.0139 | 5.9 | 139x |
| N_e 1.31e4 / 1.62e4 (Prado-Martinez 2013) | 0.0106 / 0.0086 | 5.2 / 4.6 | 106x / 86x |
| **N_e 2.0e4 (Charlesworth 2009 upper; charitable value)** | **0.0070** | **4.2** | **70x** |
| *Reported, not used:* 20 y/gen (350 gen), N_e 1e4 / 2e4 | 0.0173 / 0.0087 | 6.6 / 4.7 | |
| C1d measured temporal N_e 9,665 (a lower bound) | 0.0144 | 6.0 | |
| growth: 1e4, then 1e5 for the last 1,000 y | 0.0121 | 5.5 | |
| fast growth: 1e4 for 2,000 y, then 1e5 | 0.0050 | 3.5 | |
| Day frame, census 1e5, V_k 5 (N_e 57,143) | 0.00245 | 2.5 | 24x |
| Day frame, census 1e6 (N_e 571,429) | 0.000245 | 0.78 | 2.4x |
| Day frame, census 1e7 (N_e 5.7e6) | 2.45e-5 | 0.25 | 0.2x |

**Criterion:** the charitable central value is 0.0070. That is 23x the 3x-band edge and 7x the 10x edge. **RH tag: rhetoric.**

Context, not used in the verdict: Day's own January 2026 paper reports "drift variance" of 0.00150-0.00495 per 500-year step pan-European and 0.00330-0.01514 in Britain and Ireland. These are raw Var(Δp) values, and by his own caveat they include "residual population structure, and migration". He does not cite that paper in Q96, so under N2b scope it is not a basis for a verdict.

## Part 2: Q157 / Q158

### Model, referent and criterion (pre-registered)
**Day's model** (HL l.283-300): "k(T) = μ · F(T), F(T) = P(τ ≤ T | fixation)". Fill is F, on four textual grounds:
- l.272-275: "A population reaches the k = μ flux only after it has spent enough time to load every one of its pipes".
- Q152: "the pipe substantially fills, and Kimura's rate is approached".
- Table 3: "flux/μ (bound)".
- For a changing N_e, the clock is "the drift exposure ∫ dt/4Nₑ(t)" (l.432-433).

**Computation.** Exact Kimura (1955) series on x = ∫dt/N_e, with an empty start (the charitable case for "empty"). The self-test reproduces R4-B2 (x = 4.55 gives 0.697 / 0.256; x = 8 gives 0.945 / 0.514).

**Referent.**
- "Lineage duration" is a defined term in HL. l.249: "Use the lineage duration, the full continuous ancestry, which in the case of the human lineage is roughly six and a half million years".
- So the window is 6.5 My, with 6.3 My (Z23003785) also used.
- H8's 2 My window and the current-size reading are reported, not used.

**Literal band and criterion.** The literal band for "never fills / nearly empty" is F <= 0.10. The tag is dialectic if min F over the central set is <= 0.30.

### Results (rounded from raw output; human lineage, empty start)
| case | T (My) | x | exact F (fill) | Day's exp law | linear x/4 | delivered D |
|---|---|---|---|---|---|---|
| **(a) HL's own variance N_e 57,143 (H8 census 1e5, V_k 5)** | **6.3** / 6.5 | 4.41 / 4.55 | **0.676** / 0.697 | 0.107 / 0.114 | 1 | 0.242 / 0.256 |
| (b) N_e 1.0e4 | 6.3 / 6.5 | 25 / 26 | 1.000 | 0.68 | 1 | 0.84 / 0.85 |
| (c) N_e 1.62e4 | 6.3 / 6.5 | 16 | 0.999 | 0.53-0.54 | 1 | 0.74-0.75 |
| (d) Takahata two-epoch (1e5 before 4.6 My, 1e4 after) | 6.3 / 6.5 | 19 | 1.000 | 0.60 | 1 | 0.84-0.85 |
| *Reported, not used:* H8 as written, 2 My | 2.0 | 1.40 | 0.026 | 0.0009 | 0.35 | 0.003 |
| Takahata 1e5 held for the whole lineage | 6.5 | 2.6 | 0.28 | 0.023 | 0.65 | 0.065 |
| Yoo HCB ancestral 1.98e5 held for the whole lineage (a pre-split N_e) | 6.5 | 1.31 | 0.018 | 0.0005 | 0.33 | 0.002 |
| elephant, Day frame at census 415,000 (N_e 332,000), 2 My, g 22 | 2.0 | 0.27 | < 1e-12 | 2e-16 | 0.07 | ~0 |
| elephant at Day's ceiling X 28,000 (N_e 22,400) | 2.0 | 4.06 | 0.62 | 0.088 | 1 | 0.21 |

- **Criterion:** the charitable central value is 0.676 (HL's own N_e over 6.3 My). That is 6.8x the literal band and 2.25x the 3x-band edge. **RH tag: rhetoric** for Q157 and Q158.
- **The elephant.** It is the only other large animal HL names with inputs, and the repo has no sourced elephant lineage N_e. Its current-census pipe is empty (that is B2). At Day's own ceiling it fills to 0.62.
- Day's exp law gives 0.11 at (a). It is outside its own stated domain ("T ≪ 4Nₑ") at x of about 4.5.

## Scoring of pre-registered predictions (not blind; see disclosure)
| ID | Prediction | Result | Score |
|---|---|---|---|
| P1 | C7 central range 0.0070-0.0139; rhetoric | 0.0070-0.0139; rhetoric | Holds |
| P2 | Day frame at census 1e6 and 1e7 within 3e-4 (the tag flips on his frame) | 2.45e-4, 2.45e-5 | Holds |
| P3 | F(a, 6.5 My) 0.70 ± 0.02; F(a, 6.3 My) in [0.66, 0.70]; (b)-(d) >= 0.95 | 0.697; 0.676; >= 0.999 | Holds |
| P4 | min F = F(a, 6.3 My) ≈ 0.68; rhetoric | 0.676; rhetoric | Holds |
| P5 | D(a, 6.5 My) ≈ 0.26, <= 0.30 (the tag would flip on D) | 0.256 | Holds |
| P6 | H8 as written: F ≈ 0.026, <= 0.10 | 0.0255 | Holds |
| Day side | negligible Holocene drift; lineage pipe far from full on HL's input | negligible only on his census frame (>= ~1e6); HL input fill 0.68-0.70 | Fails on sourced inputs |
| Critic side | drift of several percentage points; lineage pipe fills | 4.2-5.9 points; F 0.68-1.00 | Holds |

## Proposed verdicts (pre-registered mapping; for integration after review)
- **C7:**
  - RH `rhetoric`.
  - Internal `non-sequitur` -> **n/a**, and external `contradicted` -> **n/a**. Rhetoric changes no verdict. The C1d measurement and the C-basis non-sequitur move to the dialectical core.
  - That core (zero fixations from below 50% / below 10% in 7,000 y read as evidence against drift, plus the B2 ceiling) stays scored at **C** (internal `non-sequitur` per X1 row C) and **B2**.
  - Fidelity stays n/a.
- **Q157, Q158:**
  - RH `rhetoric` (quote tags: unresolved -> rhetoric). Their core is B2 (current-size confinement, `holds`).
  - **B internal: pending -> `holds`** (HL basis), per R4-B2 "Rule N". B's external stays with B1c / B4a.
  - If the owner prefers the current-size reading S, the line restates B2 and B's verdict is the same.
- **Ledger proposals** (`ledgers/slips.md`, rule RH):
  - **Q96.** Device: an absolute intensifier ("isn't happening at all") with "hard evidence". Audience: a critic's comment thread. Function: turns a null fixation count into a categorical denial of the opposing mechanism. Core: claim C plus B2. Better rhetoric: "In January Day measured the drift variance in this very window, 0.0015-0.005 per 500 years. Zero fixations from below 50% in 280 generations is what drift predicts. The frequencies moved."
  - **Q157/Q158.** Device: the pipe metaphor, parallelism ("the priced channel and the free channel") and absolutes ("never", "every large animal"). Audience: HL's readers at the peroration. Function: fuses Haldane and HL into one closure. Core: B2. Better rhetoric: "On Hard Limits' own effective size and its own lineage duration, Day's k = μF(T) gives a pipe about 70% full. 'Nearly empty' is true only on the two-million-year window that l.416 calls 'the entire lineage', after l.249 defined the lineage as six and a half million years."

## Who this helps
- **Day side.**
  - The tags move two scores in his favour. C7 loses its `non-sequitur` and `contradicted`, and B internal moves from pending to `holds`.
  - On his own census-scale variance-N_e frame, drift over 7,000 y is small: at a census of 1e6 or more held for 7,000 y, a 50% allele drifts by about 0.8 points SD or less. His intuition follows from that frame, which HL argues for explicitly. The frame is unsourced for the Holocene and is not stated in Q96.
  - "Nearly empty" is literally true on H8's 2 My window (F 0.026) and on a pre-split ancestral N_e held for the whole lineage (0.018). It is near the band on Takahata's 1e5 held throughout (0.28).
  - On the delivered share, HL's input gives 0.24-0.26.
  - The elephant's current-census pipe is empty.
- **Critic side.**
  - At every sourced N_e, drift moves a 50% allele by 4.2-5.9 percentage points (SD) in 7,000 y, 70-139x the "not at all" band. Day's own January 2026 paper measured nonzero drift variance in the same window (with his structure caveat), and R4-C1d measures F_adj of 0.002-0.014.
  - On HL's own N_e over HL's own defined lineage duration, the exact fill is 0.68-0.70. That is "substantially fills" by Q152's own standard. Sourced field N_e gives 1.00.
  - HL itself calls the ancestral pipe "a partly-filled pipe" (l.419) and gives "thirty-five percent fill" (l.416).
  - The rhetoric tag means "never fills" and "nearly empty" are not findings of HL.
- **Both.**
  - Each tag turns on one choice. C7 flips to dialectic on Day's unsourced census frame (census of about 1e6 or more). Q157/Q158 flip on the fill measure (D instead of F; D = 0.24-0.26 at HL's input), on H8's 2 My window, or on a pre-split ancestral N_e held for the whole lineage.
  - The pre-registered choices (sourced inputs, Day's own definition of fill, HL's defined "lineage duration") pick the rhetoric tag in both cases.

## Caveats
- C7: F_drift is the neutral expectation in a closed population. C1d's measured F_adj also contains non-drift terms. The literal band (0.5 points SD) is a judgement, fixed in advance.
- Q157/Q158: constant-size epochs, diffusion limit, empty start. Pre-window fill (Day's B1d "full ... at the time of the CHLCA split") only raises F. F is the end-of-window flux for the cohort entering at the start.
- RH tags classify statements; they do not make them true. A statement far from true becomes unscored, and here that removes a `non-sequitur` and clears B. The B9 review raised the same asymmetry (MINOR-8). It is the owner's rule as designed, but a critic-side reviewer will contest it.

## For the owner
1. **The tags release B and C7.** Confirm that `rhetoric` should release B (pending -> holds) and C7 (internal and external -> n/a).
2. **C7 and Day's census frame.** Should Day's census-scale variance-N_e frame count as a charitable input? It is HL's explicit method but gives no Holocene census, and Q96 states none. At a census of about 1e6 or more the tag flips.
3. **Q157/Q158: fill measure and window.** Confirm F (Day's flux definition) rather than D, and HL's defined 6.5 My lineage rather than H8's 2 My "entire lineage" (l.416).

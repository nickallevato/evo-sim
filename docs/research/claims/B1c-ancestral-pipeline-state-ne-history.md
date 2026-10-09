---
id: B1c
title: "Was the ancestral pipeline empty or full at the split? (sourced Ne history)"
side: literature  # audit question node: Day's two statements frame it; the answer is the audit's check B1c. 'audit' is not an allowed side in lint_research.py, so audit nodes use 'literature'. Was 'day' until 2026-10-08.
branch: B
parent: B1
edges: [{type: depends-on, target: B1}, {type: attacks, target: B1a}]
load_bearing: true  # decides whether the B1 deficit exists at all for the human-chimp case
sourcing: firsthand
status: reviewed
verdicts:
  internal: "holds"   # arithmetic for an empty start; post-split new-mutation column 0.84 = (T-4Ne)/T
  fidelity: n/a
  external: "contradicted"   # empty-start premise (withdrawn by Day, B1d); step histories give excess 1.9-4.0x; K is not the difference count
---

## Statement (verbatim)
> The pipeline isn’t partially empty. It’s functionally nonexistent and empirically confirmed to be empty.

Source: [Day, "The Education of a Population Geneticist" (blog)](https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/), 2026-10-01, ¶22 of extracted text. Day, replying to Mansfield

> That’s absolutely wrong. The pipeline was full, but it was much shorter.

Source: [Day, "The Education of a Population Geneticist" (blog)](https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/), 2026-10-01, ¶31 of extracted text. Same post, later UPDATE answering Mansfield's rejoinder; see B1d

## Formal statement
Question: sign and size of ΔK = K_true − μL·T for the human lineage given a sourced Nₑ(t) with ancestral Nₑ = 1.98e5 (human–chimp–bonobo ancestor) or 1.32e5 (human–chimp–gorilla ancestor) (Yoo 2025; `population.Ne_ancestral_hc.yoo_2025_HCB`, `.yoo_2025_HCG`) and PSMC histories (Prado-Martinez 2013; extraction pending, fidelity ledger "still to do").

Derived context (python3 -I): 4Nₑ_anc = 5.3e5–7.9e5 generations, i.e. 2.1–3.1 × T (252,000). Analytic B1b bound for a contraction to 1e4: μL·4ΔN = 30 × 4 × (1.98e5 − 1e4) = 22.6M > μL·T = 7.56M, so the bound saturates and a simulation is needed. HL itself places the census-scale era (8 billion) at ~400 generations of the 252,000.

## Assumptions
- Stated: Day: empty (IR §3, EDU first answer); Mansfield: full. Day later: full but 228,000 generations long (B1d).
- Implicit: Nₑ history is the same on both lineages; PSMC and coalescent Nₑ(t) scale with the assumed μ and generation time (the circularity Day raises in B3h), so they are treated as inputs to compare under both values of μ, not as ground truth.

## Responses
- Against: "Vox’s response was basically an assumption that at the time of split between humans and chimps the ‘pipeline’ as he calls it was empty." ([Mansfield (@brianmansfield6912), YouTube comments under Examining Origins video jDxFtCOGZ3A](https://www.youtube.com/watch?v=jDxFtCOGZ3A), comments retrieved 2026-10-07; terminus ante quem 2026-10-01: Day quotes this comment in "The Education of a Population Geneticist", ¶30 (added 2026-10-08), quoted inside Day's post (UPDATE)) [secondhand: Mansfield, as pasted into Day's post of 2026-10-01]
- In support: Day: ancient-DNA data show "absolutely no advancement" of allele frequencies (branch C; not assessed here). RESULTS B1 caveat: an empty start contradicts observed diversity.
- Weaknesses in the responses: Day's evidence for emptiness is the aDNA analysis (branch C) whose panel is ascertained on present-day variable sites (Mathieson 2015; C1 queued) and which uses Nₑ ≈ 10⁴ that Day himself calls circular (B3h). Mansfield offers no sourced demography.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Yoo 2025 | "we estimated that the human-chimpanzee-bonobo ancestral population size (average Ne = 198,000) is larger than that of the human-chimpanzee-gorilla ancestor (Ne = 132,000)" | verified (ledger) |
| Prado-Martinez 2013 | "Inferred effective population sizes have varied radically over time in different lineages" (abstract only; PSMC curves not yet extracted) | unverified for numbers |

## Pre-registered prediction
Written **before** the check runs.
- Under the claimant's model: Day (IR): E[count] ≈ μL(T − 4Nₑ) with a deficit of order μL·4Nₑ_eff for any Nₑ_eff reflecting expansion.
- Under the opposing model: Standard theory (B1b): from an equilibrium ancestral state, a later contraction gives an excess ≥ 0, constant Nₑ gives exactly μLT, only sustained expansion gives a deficit bounded by μL·4ΔN.
- Result that would change a verdict: Proposed check **B1c** (not yet run): forward Poisson-thinning/Wright–Fisher runs with Nₑ(t) piecewise from Yoo ancestral Nₑ (1.32e5–1.98e5) to human-lineage PSMC Nₑ, lineage by lineage, reporting per-lineage fixed substitutions vs μLT and pairwise divergence vs 2μT+θ_anc. Sign pre-registered: if PSMC shows decline from ≥1.3e5 to ≈1e4 before the split-to-present window, ΔK ≥ 0 (excess), which falsifies Day's deficit for that scenario; a deficit appears only if Nₑ rises by ΔN with 4ΔN a sizeable fraction of T.

## Check
R4 B1c (`b1c_ne_history.py`, seed 20261008, 150 reps, burn-in 20 N_sim; research/checks/results/R4-B1c-B4a.md): every step history from Yoo's ancestral Ne (1.98e5 / 1.32e5) to a sourced modern Ne (1e4-6.18e4, Prado-Martinez 2013 Table 1) gives an excess K/UT of 1.9-4.0 (H1 3.986 vs analytic 3.984); controls 1.000. This is the B1b telescoping identity under step histories, not an independent empirical finding: Yoo's Ne is a lifetime average, and no PSMC trajectory was extracted. K counts ancestral alleles that fix in both lineages, so it is not a difference count. Credit to Day: the new-mutation column (0.84) confirms (T-4Ne)/T. Day withdrew the empty-start premise (B1d). Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)
Earlier note: Script: proposed `research/checks/b1c_ne_history.py` (queued; seed to be fixed before the run) · Result: none yet. Related done checks: B1, B1b.

## Simulator variables implied
- Nₑ(t) loaded from file (PSMC/MSMC curves) or presets from Yoo 2025
- lineage-specific histories
- start state
- counting mode (fixed substitutions vs pairwise divergence)

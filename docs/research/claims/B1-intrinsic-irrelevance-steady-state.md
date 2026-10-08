---
id: B1
title: "k = mu is a steady-state identity; finite-time count differs (Intrinsic Irrelevance)"
side: day
branch: B
parent: B
edges: [{type: supports, target: B}, {type: depends-on, target: B1a}, {type: depends-on, target: B1c}]
load_bearing: true  # ROOT as worded ("no mechanism") needs the neutral route closed; B1, B2 and B3 are partial substitutes, so ROOT survives only if at least one holds
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds
  fidelity: n/a
  external: "contested"   # deficit exists only for new-mutation accounting from an empty start; contradicted for the human-chimp observable (B4a)
---

## Statement (verbatim)
> using the exact transient formula E[F(T)] = μL ∫₀ᵀ F_X(u) du rather than the naive product μLT, the leading-order correction subtracts the mean fixation time from the available window.

Source: [Z22903977, The Intrinsic Irrelevance of Kimura's Substitution Rate (Day & Athos)](https://zenodo.org/records/22903977), Zenodo 2026-09-22 (v1), p.1 (abstract)

> It is a rate, not a count, and converting it to a count requires assumptions the identity itself cannot supply.

Source: [Z22903977, The Intrinsic Irrelevance of Kimura's Substitution Rate (Day & Athos)](https://zenodo.org/records/22903977), Zenodo 2026-09-22 (v1), §1 The Identity

> At generation zero, the subsitution pipeline is empty.

Source: [Z22903977, The Intrinsic Irrelevance of Kimura's Substitution Rate (Day & Athos)](https://zenodo.org/records/22903977), Zenodo 2026-09-22 (v1), §3 The Empty Pipe (typo "subsitution" is in the source)

## Formal statement
Glossary sense: **throughput k** = substitutions per generation at steady state; **latency** t_fix = generations for one allele to go from arising to fixation.

- Steady state: k = 2Nμ × 1/(2N) = μ per site per generation (`rates` not applicable; textbook identity, accepted by Day: "Kimura's derivation is mathematically correct").
- Finite window T from an **empty** start: E[F(T)] = μL ∫₀ᵀ F_X(u) du, F_X = CDF of the fixation time conditional on fixation, E[X] = 4Nₑ (Kimura & Ohta 1969). For T ≫ E[X], E[F(T)] ≈ μL (T − 4Nₑ).
- Parameters: `generations_available.day_2026` = 252,000; `population.Ne_modern_human` = 1.0e4; μL ≈ 30 (Day's value; **no entry in parameters.yaml**, propose `new: mutation.muL_neutral_per_gen_day_IR = 30`; the pedigree-based haploid figure would be 1.2e-8 × 3.2e9 = 38.4, derived).

Sub-claims: B1a (the formula and its numbers), B1b (size-change statement), B1c (was the start empty?), B1d (Day's later reply: full but short pipe), B1e (Chalub 2022).

## Assumptions
- Stated: Population has held one size; the pipeline is empty at generation zero; Nₑ = 10,000 (also 50,000 and 63,000 as sensitivity cases).
- Implicit: Zero standing variation at the split (an empty start means zero heterozygosity, which contradicts observed human diversity; RESULTS and steelman review C1 frame it as a counterfactual boundary case). Constant Nₑ over the whole window. Counting is of per-lineage fixed substitutions, not pairwise sequence divergence (see B4a/B6).

## Responses
- Against: "The ‘pipeline’ would have been full from the X generations preceding that point in time." ([Mansfield (@brianmansfield6912), YouTube comments under Examining Origins video jDxFtCOGZ3A](https://www.youtube.com/watch?v=jDxFtCOGZ3A), comments retrieved 2026-10-07, comment UgyhNduYke46IStQ5pd4AaABAg.AbQefbrLxzSAbRHJx-mRP2 (Mansfield))
  Camestros: see B6b. McCarthy: see B5a (time-adjusted version). Reddit, Dumb-and-Dumber (B5f): "It needs the elapsed time to be long compared with the fixation time." ([r/DebateEvolution, Dumb-and-Dumber, "New anti-evolution paper today from Vox Day"](https://www.reddit.com/r/DebateEvolution/comments/1wss2wj/), 2026-09-28, post 1wss2wj) He accepts the 4Nₑ time and argues 252,000 is long compared with it.
- In support: Exact for an empty start (RESULTS B1, below). Day's transient-lag mechanism after a size change is standard theory (B1b). Hössjer (ally) accepts k = dμ as the neutral rate but argues the date is circular (B4f).
- Weaknesses in the responses: Against: Mansfield gives no numbers and quotes Day only via a commenter (secondhand). For: the corpus itself contains Day's later statement that the pipeline "was full" at the split (B1d), which conflicts with the empty-start premise of this claim; Day does not reconcile the two.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura & Ohta 1969 | "takes about 4Ne generations until it spreads to the whole population if we disregard the cases in which such a gene is eventually lost" (p.766, after Eq. 15) | accurate for 4Nₑ (ledger) |
| Chalub 2022 | see B1e | verified-partial (ledger) |

## Pre-registered prediction
Written **before** the check runs.
- Under the claimant's model: (RESULTS B1, P1) With an empty start the simulated count matches U∫F_X, which tends to U(T−4N).
- Under the opposing model: (RESULTS B1, P2) With an equilibrium start the simulated count matches U·T.
- Result that would change a verdict: A sourced demographic history (B1c) showing the ancestral population was at equilibrium or shrinking at the split would remove the deficit and move the external verdict to contradicted; one showing a sustained expansion lasting an appreciable fraction of 4Nₑ would support it.

## Check
Script: `research/checks/b1_start_state.py` (seed 11) · Result: both predictions confirmed at every T. N=100, U=0.5: T=400: U·T=200, Day U∫F_X=41.6, empty-start sim 41.3±0.8, equilibrium-start sim 198.5±2.0; T=2000: 1000 / 802.7 / 802.5±3.4 / 1005.1±4.3. Review #2: the empty-start run is Poisson thinning, so it matches by construction (it verifies the code, not the claim). Internal verdict: holds as mathematics. Review: `research/checks/REVIEW.md#2026-10-07--correctness-review-2-sonnet-on-b0b3`

R4 B1c/B4a (research/checks/results/R4-B1c-B4a.md): the empty-start deficit is exact for post-split new mutations (new-mutation column 0.84 = Day's (T-4Ne)/T at Ne = 1e4), a point for Day's internal validity. For the human-chimp case the deficit exists only in that accounting: step histories from Yoo's ancestral Ne give a per-lineage excess (K/UT 1.9-4.0), and pairwise divergence is not reduced by the empty-pipe term (d - 2muT = theta_anc in every row). Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)

## Simulator variables implied
- start state (empty | equilibrium | user-set heterozygosity)
- Nₑ(t) schedule
- T (generations)
- μL (neutral destined-to-fix input per generation)
- counting mode: per-lineage fixed substitutions vs pairwise divergence

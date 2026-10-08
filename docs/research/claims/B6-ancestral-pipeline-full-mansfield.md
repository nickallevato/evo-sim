---
id: B6
title: "Mansfield: the ancestral pipeline was full at the split; expected divergence ≈ 2 mu T + theta_anc"
side: critic
branch: B
parent: B1
edges: [{type: attacks, target: B1}, {type: attacks, target: B1a}]
load_bearing: true  # if true, the empty-start premise of B1 fails for the human-chimp case
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds
  fidelity: n/a
  external: "supported"   # full pipe gives k = mu and d = 2muT + theta_anc (forward sim)
---

## Statement (verbatim)
> The ‘pipeline’ would have been full from the X generations preceding that point in time.

Source: [Mansfield (@brianmansfield6912), YouTube comments under Examining Origins video jDxFtCOGZ3A](https://www.youtube.com/watch?v=jDxFtCOGZ3A), comments retrieved 2026-10-07, comment UgyhNduYke46IStQ5pd4AaABAg.AbQefbrLxzSAbRHJx-mRP2 (Mansfield)

> The differences between one copy of the human genome and one copy of the chimpanzee genome include both the sites of fixed divergence between the species and some polymorphic sites within each species.

Source: [Chimpanzee Sequencing and Analysis Consortium 2005, Nature 437:69-87](https://www.nature.com/articles/nature04072), 2005, Main text, "Nucleotide divergence"

## Formal statement
E[d] = 2μT + θ_anc, θ_anc = 4Nₑ,anc μ per site (B4a). Equilibrium start: expected fixed substitutions = μLT (RESULTS B1, P2). The hierarchy attributes the formula to Mansfield and the sources agent; the verbatim Mansfield text is the full-pipe statement only.
Derived illustration: see B4a (Nₑ,anc = 1.0e4 → 0.65%; 1.32e5 → 1.24%; 1.98e5 → 1.56% vs 1.23% observed, μ = 1.2e-8, T = 252,000).

## Assumptions
- Stated: A population at equilibrium before the split has a full pipe.
- Implicit: Ancestral population at constant size ≥ 4Nₑ,anc (≥ 5.3–7.9×10⁵ generations per Yoo Nₑ,anc) before the split; no demographic upheaval resets the pipe.

## Responses
- Against: Day (EDU, quoted in B1c): the pipeline is "functionally nonexistent" — later "The pipeline was full, but it was much shorter" (B1d).
- In support: RESULTS B1: the equilibrium-start simulation gives U·T; Day's later concession (B1d).
- Weaknesses in the responses: Mansfield gives no ancestral Nₑ, no number, and states it as an assumption; Day's reading of it as "it gets reset somehow" is his paraphrase (secondhand).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Yoo 2025 | Nₑ,anc 198,000 (HCB), 132,000 (HCG) | verified |
| Chimpanzee Sequencing and Analysis Consortium 2005 | polymorphism 14–22% of observed divergence | verified |

## Pre-registered prediction
Pre-registered prediction (copied from RESULTS B1; the check has run).
- Under the claimant's model: (Critic) equilibrium start: simulated count = U·T.
- Under the opposing model: (Day) empty start: count = U∫F_X ≈ U(T − 4N).
- Result that would change a verdict: B1c, B4a.

## Check
Script: `research/checks/b1_start_state.py` (seed 11) · Result: equilibrium start N=100, U=0.5: T=400: 198.5±2.0 vs U·T = 200; T=2000: 1005.1±4.3 vs 1000; empty start: 41.3±0.8 and 802.5±3.4. Review: `research/checks/REVIEW.md#2026-10-07--correctness-review-2-sonnet-on-b0b3`

R4 B1c/B4a (research/checks/results/R4-B1c-B4a.md): an equilibrium (full) start gives K/UT = 1.000 for constant Ne, and d = 2muT + theta_anc within ~0.3% in forward simulation. Whether the fit matches 1.23% depends on Ne_anc, T and mu (see B4a). Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)

## Simulator variables implied
- start state
- ancestral Nₑ
- θ_anc term shown separately

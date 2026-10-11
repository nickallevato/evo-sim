---
id: B3d
title: "k = 32.3 mu (Bergeron pedigree rate vs Yoo required rate) and the median factor 25 across 55 vertebrates"
side: day
branch: B
parent: B3
edges: [{type: supports, target: B3}]
load_bearing: false  # cited as direct empirical falsification of k = μ after the N/Nₑ retraction, but no derivation is shown
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds   # R4 B3: 32.93 from Day's own inputs (205 M, Bergeron mammal mean 7.97e-9, T = 252,000, L = 3.1e9), 1.95% off, scored on his basis (R4-X1 section 0); the unit question is external (N1). Reviewer alternative "arithmetic-error (conditional)" dropped (C1/D1). "Median 25": see B3m (fidelity accurate, external contested). Earlier: "Median 25": internal pending
  fidelity: misread   # for "the required substitution rate from Yoo et al. (2025)": Yoo has no 187 or 205 Mb figure (A3x1); Yoo's own 327 Mb gives 52.5. "Median factor of 25 across 55 vertebrates": pending (cited, Bergeron 2023; not recomputed)
  external: contradicted   # as a per-site k/mu: 205 M is SDR base pairs plus SNVs over a point-mutation rate; events give 3.38 (Bergeron mu) / 2.25 (human mu); like-for-like bp 0.39-0.56; after the ancestral term at the mandated N_anc 0.87-1.10 (human mu), 1.31-1.65 (Bergeron mu). Calibration gap Keightley calls "about twofold". "Median 25": external pending. Alternative: contested if the SDR bp route is judged unclean (gaps.md caveat)
---

## Statement (verbatim)
> comparing Bergeron’s (2023) pedigree-measured mammalian mutation rate against the required substitution rate from Yoo et al. (2025) gives k = 32.3μ, not k = μ.

Source: [Day, "The Education of a Population Geneticist" (blog)](https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/), 2026-10-01, ¶7 of extracted text

> The textbook k = μ identity is still falsified — both directly (pedigree μ and phylogenetic k disagree by a median factor of 25 across 55 vertebrates)

Source: [Day, "A Retraction and a Revision" (blog)](https://voxday.net/2026/05/07/a-retraction-and-a-revision/), 2026-05-07, ¶5 of extracted text


RH tag (2026-10-10 pass): dialectic (stated as a checkable claim or derivation; no rhetorical device scored).
## Formal statement
No derivation appears in any harvested text (not in Zenodo; book not checked). Parameters: Bergeron 2023 mammal mean 7.97e-9 (`mutation.mu_per_site_per_gen.bergeron_2023_mammal_mean`, verified; Q-quote in the parameter note; human value in SI Table 8, not retrieved); required rate from Yoo 2025 (not found in Yoo: 410 Mb or 187 Mb, fidelity ledger).

**Reconstruction attempts (derived, python3 -I):** brute force over required ∈ {17.5M, 20M, 35M, 40M, 187M, 205M, 410M}, generations ∈ {146,250 … 450,000}, L ∈ {2.9–6.4 Gb}, μ ∈ {7.97e-9 … 1.5e-8}, with and without halving: only four coincidental hits within ±0.15 of 32.3, all using non-natural input pairs (e.g. 410M, 325,000 gens, L = 3.0e9, μ = 1.3e-8). The closest natural reconstruction: 205M / 252,000 = 813.5 required fixations per generation; Bergeron mammal μ × 3.1e9 = 24.7 mutations per generation; ratio 32.9 (with L = 3.2e9: 31.9). **Implication:** the ratio uses the 205M count (bp/events issue, A3x); with the SNV-only 17.5M the same arithmetic gives 69.4/24.7 = 2.8; 205M/17.5M = 11.7 (the "11.7" bases-vs-events factor in the balance ledger).
The "median factor of 25 across 55 vertebrates" is attached to Bergeron et al. (2023) in the same post (blog 2026-05-07 ¶3, Q161: "on pedigree mutation rates and fossil-calibrated substitution rates for 55 vertebrate species"); the figure itself has not been recomputed (R4 B3 proposes it). Bergeron 2023 separately reports "40-fold variation among species" in pedigree rates (a different quantity). Pedigree μ is per generation and phylogenetic k per year/per generation depends on generation-time assumptions.

## Assumptions
- Stated: Pedigree μ and phylogenetic (required) rate should coincide under k = μ.
- Implicit: The "required substitution rate" is the observed difference count divided by T and L (it counts differences including polymorphism, structural variants and ancestral coalescence), compared with a per-site-per-generation pedigree μ.

## Responses
- Against: Hancock and Nesslig20 compute the neutral count from pedigree μ and find agreement within a factor ~2 (B5c, B5e); Hancock's count reaches ≈19M vs 35M SNVs (B5c).
- In support: Keightley 2012: pedigree μ is "about twofold lower than estimates based on the human-chimp divergence"; keruru (KR-05): "closer to twice that".
- Weaknesses in the responses: Hancock's comparison uses SNVs only and mixed haploid/diploid bases (B5c); neither side has isolated the effect of ancestral coalescence and calibration choice on the "twofold".

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Bergeron 2023 | "The average pedigree-based mutation rates per generation for each species ... show 40-fold variation among species." | verified-accurate (ledger) for the 40-fold figure only |
| Yoo 2025 | no 410 Mb or 187 Mb; SDR average 327 Mb per lineage | not-found (ledger) |
| Keightley 2012 | "μ is about 1.1 × 10(-8), which is about twofold lower than estimates based on the human-chimp divergence" | verified-partial (abstract only) |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: k = 32.3μ.
- Under the opposing model: Using SNV-only fixed differences and ancestral-coalescence accounting, k/μ is of order 1–3, not 30.
- Result that would change a verdict: Day supplying the derivation; or a reproduction using stated inputs. B4a will separate the ancestral-coalescence term.

## Check
Script: `research/checks/b3_family_reconstruction.py` (pre-registered 04f96bd; post hoc `b3_posthoc.py`), `results/R4-B3.md`. This replaces the uncommitted reconstruction search of the extraction pass.

R4 B3 (`research/checks/results/R4-B3.md`; pre-registered 04f96bd; three load-bearing reviews #40-#42 at 33e190a; fix pass fd9d2de): the 32.3 reconstructs only from base-pair totals (205 M / 252,000 generations over Bergeron's mammal mean times 3.1e9 = 32.93; all 8 grid hits use 205e6 or 410e6). On Day's basis the arithmetic holds (internal `holds`). Measured counts give 3.38 (events, Bergeron mu) and 2.25 (human mu); base pairs counted like for like give 0.39-0.56 (gaps.md caveat on SDRs); after the ancestral term at the mandated N_anc (1.32e5 / 1.98e5) the residual is 0.87-1.10 (human mu) and 1.31-1.65 (Bergeron mu), and 0.97-1.04 at Langergraber's 7-8 My split. Fidelity of the Yoo attribution `misread` (A3x1; Yoo's 327 Mb per lineage gives 52.5). The "median 25 across 55 vertebrates" has a cited source (P6 withdrawn): fidelity and external `pending`, recomputation proposed (QUEUE). Day side: his arithmetic is exact on his inputs and a residual of 1.3-1.65 remains at his mammalian mu, in the direction he claims. Critic side: with events or like-for-like bp the figure is 0.4-3.4 and the remainder is the calibration gap Keightley and keruru (KR-05) place in the clock, not an independent k ≠ mu. Rhetoric: the wrapper sentence Q159 is ledger RH-5.

R4 B3m (`research/checks/results/R4-B3m.md`; pre-registered 5ca5f2e, post hoc 382b580, combined review #48 at b30137d, fix pass 4442c99): Day's "median factor of 25 across 55 vertebrates" reproduces from Bergeron 2023 Table 9 (25.4, n = 55, matched per-year and per-generation; sub-claim [B3m](B3m-median-25-bergeron-55-vertebrates.md): fidelity `accurate`, external `contested`). The 25 is a property of the tabulated terminal-edge rates (chronos lambda = 0), which cover about 21 Myr of a 416 Myr root depth (PH1); a lineage-average k from the same tree is at least about 2x mu (PH2, a lower bound). The 2-vs-25 gap is unexplained here. Day side: the number and the count are exact. Critic side: the column is not a lineage-average rate. The 32.3 verdicts above are unchanged.

R4 GAP-06 (combined review #51, 2026-10-10): on Day's inputs B3d reproduces as 32.93; his printed 32.3 matches the 24.5 y (Yoo HCB) basis (32.27). Substituting Yoo's mu for Bergeron's gives 20.57 (-37.5%), a source swap not scored. No verdict change.

## Simulator variables implied
- required-rate basis (SNV | events | bp)
- μ source (pedigree | phylogenetic)
- L haploid

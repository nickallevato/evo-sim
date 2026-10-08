---
id: H1
title: "2026-05-07 retraction: Term 3 (Haldane cost limit) was misused as a bound on total substitution rate; it limits adaptive substitution only, at ~1e-12 per site per generation"
side: day
branch: H
parent: H
edges: [{type: revises, target: H8}, {type: revises, target: H}]
load_bearing: true  # Narrows what H and H8 may be used for. After this, a cost-of-selection bound cannot by itself be compared with total differences; the corrected framework puts total k at 1e-7 to 1e-8 (consistent with the observed rates, per Day).
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: n/a
  external: pending
---

## Statement (verbatim)
> "our subsequent empirical work has identified a category error in how the selection-cost binding constraint was being used in it."

Source: [A Retraction and a Revision](https://voxday.net/2026/05/07/a-retraction-and-a-revision/), B2026-05-07-a-retraction-and-a-revision, posted 2026-05-07, ¶3 of extracted text (Q65).

> "my error was in interpreting its output as a constraint on total k. Once corrected, Term 3 still limits adaptive substitution rate at ~10⁻¹², but total substitution rate is only governed by Terms 1 and 2"

Source: same post, ¶4 (Q67).

> "the realized substitution rate equals the minimum of three serial constraints: the corrected input flux (Term 1), the polymorphism throughput ceiling (Term 2), and the selection-cost limit (Term 3)."

Source: same post, ¶3 (Q66; the three-term framework being revised).

> "The textbook k = μ identity is still falsified — both directly (pedigree μ and phylogenetic k disagree by a median factor of 25 across 55 vertebrates)"

Source: same post, ¶5 (Q69).

> "the CHLCA event falls somewhere in the 250 kya to 1.3 Mya range rather than the 6.3 Mya presently assumed."

Source: same post, ¶7 (Q68). The earlier 68 kya to 330 kya range was based on "the erroneous calculator".

## Formal statement
Before: k_real = min(Term 1 = input flux, Term 2 = polymorphism throughput ceiling, Term 3 = selection-cost ceiling) with Term 3 = k_sel = s_max d / [2 L ln(2 Ne)] (H8). After: k_adaptive <= Term 3 (~1e-12 per site per generation); k_total = min(Term 1, Term 2), "in the 10⁻⁷ to 10⁻⁸ range".
Version ledger (versions.md): the retraction does not change Zenodo 19984826 (the original text remains; no revised Zenodo version seen), and Zenodo 18168236 (H) was not mentioned.

derived (R2): 8.3e-12 per site (Z19984826 §4.3 human case, Ne = 3,300, d = 0.45, s_max = 1, L = 3.1e9) x 3.1e9 = 0.0257 adaptive substitutions per generation = one per 39 generations. For 260,000 generations this gives 6,690 adaptive substitutions; compare Haldane + d in H: 487 (G_eff = 146,250 at one per 300 generations) and 1,083 without d at 325,000 generations. The two cost-based figures in Day's corpus therefore differ by a factor of about 7.7 per generation (300/39).

Repo observation (R2, pending R4 review): the retraction's stated reason ("a constraint on selectively driven substitutions alone") applies to H as well, because H compares a Haldane-limited count of selected fixations with the full 20M differences (the paper's §5.1 argues that neutral change cannot explain "adaptation", which is a different claim from bounding total change). H1 does not state whether H is affected.

## Assumptions
- Stated: Term 3 math "is correct for the quantity to which it actually applies".
- Implicit: that the remaining adaptive limit (~1e-12 per site) is correct (it inherits s_max ≈ 1 and d from H8); that observed total k, as pedigree-versus-phylogenetic mismatch "median factor of 25 across 55 vertebrates", is a clock-independent test.

## Responses
- Against: none; this is Day's own revision. Hössjer (H5, 2026-09-14, after the retraction) still treats the cost argument as applying to selected changes.
- In support: Nesslig20 (H6) independently says the cost limit "does not apply to drift".
- Weaknesses in the responses: no critic has asked whether the retraction undermines H or Z18168236.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Bergeron 2023 (pedigree mu) | the paper reports a different quantity from the retraction's "median factor of 25 across 55 vertebrates" (pedigree against phylogenetic rate): "show 40-fold variation among species" is the spread of pedigree rates across species | the 40-fold figure is accurate (ledger); the factor-of-25 comparison is Day's own and is not in the paper (unverified) |
| Frankham 1995 (N versus Ne "cataloged thirty years ago") | not retrieved | unverified |

## Pre-registered prediction
- Under the claimant's model (revised): total k lies between 1e-8 and 1e-7 per site per generation; the corrected framework predicts "factor 10 corrections rather than factor 100,000" to divergence dates.
- Under the opposing model: with k = mu for neutral sites (B-branch checks), the revised statement is compatible with the standard picture on total k and leaves only the date shift of a factor ~10 as a claim (a calibration issue, B4).
- Result that would change a verdict: a revised Zenodo version of 19984826 and 18168236 stating which numbers survive.

## Check
Script: none (document tracking; version ledger row exists). · Result: not run · Review: pending

## Simulator variables implied
Adaptive versus total substitution rate; fraction of differences that are adaptive.

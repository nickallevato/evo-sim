---
id: B6a
title: "Day (IR): ancestral polymorphism contributes 1.44 million differences (0.35%), \"a rounding error\""
side: day
branch: B
parent: B6
edges: [{type: attacks, target: B6}]
load_bearing: false  # dismisses the ancestral-polymorphism objection; the B1 deficit is stated net of it
sourcing: firsthand
status: reviewed
verdicts:
  internal: arithmetic-error   # R1(ii) on Day's own table basis (R4 X1 rule rev 2): the empty-pipe removal at Ne = 1e4 is 1.2M, not 2.4M, so 1.44M / 1.2M = 1.2 and 'less than half' is 0.6; the sign of 'the net adjustment still reduces' flips (+0.24M). Ne_anc is a contested premise (N1) and is not the basis
  fidelity: n/a
  external: "contradicted"   # at sourced Ne_anc the ancestral term is comparable to 2muT; holds only at Ne_anc = 1e4, where d is half the observed
---

## Statement (verbatim)
> At Nₑ = 10,000 and μ = 1.2 × 10⁻⁸, this yields approximately 1.44 million differences across the genome, less than half of the 2.4 million fixations the empty-pipe correction removes from the naive prediction. The net adjustment still reduces the expected count.

Source: [Z22903977, The Intrinsic Irrelevance of Kimura's Substitution Rate (Day & Athos)](https://zenodo.org/records/22903977), Zenodo 2026-09-22 (v1), p.3 (§3)

> The ancestral polymorphism objection is not merely trivial. It is a rounding error.

Source: [Z22903977, The Intrinsic Irrelevance of Kimura's Substitution Rate (Day & Athos)](https://zenodo.org/records/22903977), Zenodo 2026-09-22 (v1), p.3 (§3)

## Formal statement
**Arithmetic audit (derived, python3 -I):** 4 × 10⁴ × 1.2×10⁻⁸ × 3×10⁹ = 1.44×10⁶ ✓; 1.44M/410M = 0.351% ✓ ("0.35%"). The empty-pipe removal in IR's own table at Nₑ = 10⁴ is 30 × 40,000 = 1.2M (loss 15.9%), not 2.4M. 1.44M/1.2M = 1.2 (θ exceeds the removal); 1.44M/2.4M = 0.6, not "less than half". So on IR's own numbers the sign of "the net adjustment still reduces the expected count" reverses (+1.44M − 1.2M = +0.24M). If 2.4M is two lineages × 1.2M, the comparison should use the pairwise count 2μT·L (15.1M) plus θ, not the per-lineage figure.
Comparator: 410M mixes events and bp (A3x); against SNV-only 35M the term is 4.1%. At Yoo ancestral Nₑ (1.32×10⁵ / 1.98×10⁵): θ·L (L = 3.2e9) = 20.3M / 30.4M, i.e. 58% / 87% of 35M (derived; B4a).

## Assumptions
- Stated: Nₑ = 10⁴, μ = 1.2e-8, genome 3×10⁹.
- Implicit: Nₑ,anc equals the modern human Nₑ (the glossary flags using modern Nₑ for the ancestral population as a common confusion); comparator is the 410M count.

## Responses
- Against: Camestros (B6b), Mansfield (B6), Yoo 2025 Nₑ,anc, CSAC 14–22%.
- In support: None independent; Hössjer does not address it.
- Weaknesses in the responses: The critics' side has not computed the θ term from Yoo's Nₑ in print; this file's derivation is the first in the corpus and still unchecked by simulation (B4a).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Yoo 2025 | ancestral Nₑ 132,000–198,000 | verified |
| Chimpanzee Sequencing and Analysis Consortium 2005 | t2 "may be on the order of 1-2 million years" | verified |

## Pre-registered prediction
Written **before** the check runs.
- Under the claimant's model: θ_anc ≈ 0.35% of divergence.
- Under the opposing model: θ_anc is 58–87% of the SNV total at Yoo Nₑ,anc.
- Result that would change a verdict: B4a.

## Check
Script: none (arithmetic); proposed B4a.

R4 B4a (research/checks/results/R4-B1c-B4a.md): "rounding error" holds only at Ne_anc = 1e4. At Yoo's Ne_anc, theta_anc = 0.63-0.95% of sites against 2muT = 0.605%. Day-side point: at Ne = 1e4 the model gives d = 0.65%, about half the observed 1.23%, so the reconciliation depends on a large Ne_anc (or longer T / higher mu). Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)

R4 X1 (research/checks/results/R4-X1-rescore.md; rule research/checks/results/R4-X1-verdict-rule.md rev 2; review #12, 2026-10-09): under the single both-sides rule this node is arithmetic-error / n/a. R1b on Day's own table basis (not Yoo's Ne): IR's empty-pipe removal at Ne = 1e4 is 1.2M, not 2.4M, so 1.44M / 1.2M = 1.2 and 'less than half' is 0.6; the sign of 'the net adjustment still reduces' flips (+0.24M). The Ne_anc value is a contested premise (N1) and is not the basis Charitable reading tried: tried other Ne_anc: that is a contested premise (N1), not an ambiguity; 'less than half' = 0.6 stands.

## Simulator variables implied
- Nₑ,anc
- θ term

---
id: G2h
title: "Hancock: MITTENS's F_max contains no mutation input and no selection coefficient, so it is not a test of selection"
side: critic
branch: G
parent: G2
edges: []  # PROPOSED: [{type: attacks, target: A}]; left empty until defeater dNEW-23 in argmap/mapping-proposals-2026-10-09.md is pasted (argmap_check edge coverage)
load_bearing: false  # structural point; the supply side is argued numerically in B5c / A5c, the serial reading in G2
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: pending
  external: pending
---

## Statement (verbatim)
> Notice that his model had no mutation rate, right?

Source: [Gutsick Gibbon + Zach Hancock, No, Vox Day's AI-Generated Books Did Not Debunk Evolution](https://www.youtube.com/watch?v=_Vu0ZVVjwHc), 2026-10-03, t=01:41:38 (auto-caption; spelling as captioned). Context: "the very first thing that we should think about, and this is something that Vox's model does not do, is think about how many new mutations enter the population every single generation."

> this is not even necessarily a measure of selection

Source: same, t=01:36:03. The next caption line continues: "Like there's no selection coefficient in any of this" (t=01:36:24: "So it's not even obvious that this is a test of selection").

## Formal statement
F_max = (t_div x d)/(g_len x G_f) (A): a time divided by an empirical generations-per-fixation figure. Hancock's reading: the formula takes no mu, N or s, so it constrains an observed rate without saying which process produced it. Day's reading (A, G1): G_f is a measured total throughput of the LTEE, so mutation supply, selection and parallelism are inside the number; the transfer to humans is the question (A2e, A5).

## Assumptions
- Stated: a model of fixation should start from the supply of new mutations and a fixation probability (the speaker derives k = mu from 2N x mu x 1/(2N)).
- Implicit: an empirical G_f cannot stand in for supply terms; the LTEE and human supply differ (A5).

## Responses
- Against (Day): G_f already includes supply and selection for the LTEE (G1, A2e); the formula is a bound derived from the best observed rate, not a model of the process.
- In support: A5 / A5c (per-genome supply differs ~690x) and B5 (a supply-based neutral count is far above 180) say the same thing numerically; the audit rated A2e's ceiling inference a non-sequitur.
- Weaknesses in the responses: the point does not itself show the human rate exceeds 1/G_f; it restates the supply objection as a modelling objection; Hancock addresses the Duffy version (balance ledger).

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
No new check. The supply side is covered by A-sim (scaling factors 1.5-172x) and B5 arithmetic.
- Under the claimant (Hancock): a supply-explicit model reproduces observed divergence under k = mu.
- Under the opposing model (Day): a supply-explicit model must still show the human rate can exceed the LTEE total.
- Result that would change a verdict: a derivation of G_f from U_b, N and s (not available for the LTEE, which is underdetermined over 3 orders per R5 V30).

## Check
None.

## Simulator variables implied
- U_b, N, s as explicit inputs rather than a measured G_f.

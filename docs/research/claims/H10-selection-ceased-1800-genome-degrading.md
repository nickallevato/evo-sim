---
id: H10
title: "Day: natural selection has not kept the human genome from degrading 'since around 1800', with 3x more deleterious than neutral mutations 'drifting freely'"
side: day
branch: H
parent: H
edges: [{type: depends-on, target: H7}]
load_bearing: false  # new, unquantified; not part of the MITTENS calculation
sourcing: firsthand
status: extracted
verdicts:
  internal: pending   # no derivation or parameters given
  fidelity: n/a
  external: pending   # relaxed selection and mutation accumulation in modern humans is a live literature question; Day gives no rate, load or time course to test
---

## Statement (verbatim)
> "natural selection hasn't been performing its real function, keeping the genome from degrading, since around 1800."

Source: [Vox Day, comment on McCarthy, "Why Probability Zero is Wrong About Evolution"](https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1/comment/335325560), 2026-09-12, comment id 335325560 (Q89). Repeated 2026-09-16 (comment 338847889) and 2026-09-18.

> "With 3x more deleterious mutations than neutral ones now drifting freely, the human genome is degrading."

Source: [Vox Day, comment on Dembski's Substack, "A Review of Vox Day's Main Argument"](https://billdembski.substack.com/p/a-review-of-vox-days-main-argument/comment/339689335), 2026-09-18, comment id 339689335 (Q94).

## Formal statement
None given. A testable version would need: the deleterious mutation rate U (H7: Keightley 2012, U = 2.2), the distribution of s, the change in the opportunity for selection after ~1800 (mortality and fertility variance), and the expected fitness decline per generation.

## Assumptions
- Stated: "3x more deleterious mutations than neutral" (source of the 3x: McCarthy's 2026-02-03 exchange, bib MC-2).
- Implicit: reduced mortality removed selection rather than shifting it to fertility; "drifting freely" implies deleterious alleles behave neutrally (|N_e s| < 1).

## Responses
- Against: none located.
- In support: a mutation-accumulation concern under relaxed selection exists in the literature (not harvested; would need sourcing before use).
- Weaknesses in the responses: no critic has engaged it.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Keightley 2012 | U = 2.2 per generation (H7) | see H7 |

## Pre-registered prediction
Not run; no number to test.

## Check
None. From the 2026-10-09 corpus refresh (D-5b). Recorded in `ledgers/versions.md` ("Selection 'ended' in humans").

## Simulator variables implied
Time-varying selection intensity (opportunity for selection); deleterious DFE.

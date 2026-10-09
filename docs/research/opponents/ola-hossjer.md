# Ola Hossjer

- **Side:** ally (partial)
- **Role:** Wrote the technical review of Day's main argument for Dembski's Substack; co-author of waiting-time and genetic-entropy papers with ID-associated authors.
- **Stated credentials (as self-described or as introduced; unverified here):** Introduced as "Professor of Mathematical Statistics, Stockholm University" (HO-09). Says he advocates "uncommon descent" (HO-10).
- **Sources (see `sources/bib-critics.md`):** HO-1, HO-2

## Arguments mapped to branches
(Branch IDs from `hierarchy.yaml`. Quote IDs are in `sources/quotes-critics.md`.)

| Branch | Argument | Quote refs |
|---|---|---|
| A (F_max) | Reproduces 127 fixations: 9e6 x 0.45/(20 x 1,600) | HO-01 |
| A5 | Scaling by mutation rate (1.25e-8 vs 1e-10) gives 15,800; by genome length (x ~650) ~10 million, "only by a factor of 2" short of 20M | HO-01, HO-02 |
| H | Haldane cost limits parallel selected fixations, so the genome-length scaling does not apply to adaptive fixations (asserted) | HO-03 |
| B3 / B5 | Neutral calc F = L d mu t = 7.6 million, close to the scaled bound; both assume parallel fixation | HO-04 |
| B4 | Neutral theory cannot test common descent since it is used to date divergence | HO-05 |
| A | Agrees with Day's conclusion after adjustment | HO-06 |
| H (near-neutral) | Slightly deleterious fixations erode fitness (genetic entropy) | HO-11 |
| D (D15) | Prediction from his 2021 coordinated-mutation model (not applied to humans/chimps): the waiting time for several genes to change expression "far exceeds 9 million years"; for an orphan gene, "many orders of magnitude larger" ("guided or not") | HO-12, HO-13 |

## Weaknesses noted (own math / inputs / reading of Day)
- Derived: his neutral figure without the turnover factor is 3e9 x 1.25e-8 x 450,000 = 16.9M, versus 20M required (ratio 0.85). The factor d = 0.45 in the neutral rate (F = L d mu t) contributes a factor 1/0.45 = 2.22; k = mu per generation is not usually multiplied by d. This is an input choice, not a result. Correction 2026-10-08: this line said d "alone produces the 2.2x gap he reports". Hössjer reports no 2.2× gap. His neutral gap is 20M/7.59M = 2.63 (eq. 3.1), and his quoted "factor of 2" is the rate scaling, 20M/10.30M = 1.94 (eq. 2.4). Without d these become 16.9M (1.19× short) and 22.9M (above 20M).
- Eq. 2.4 assumes fixations scale linearly with genome length; the Haldane step that is meant to undo this scaling (HO-03) is asserted, with no cost calculation, and Haldane's limit is not applied to the neutral share he himself computes.
- The circularity point (HO-05) ignores pedigree mutation rates, which he notes are independent of divergence data; he does not show that using them with independent dates fails.
- Genetic-entropy sentence (HO-11) has no calculation in the review. Sanford is cited, not Day.
- He agrees with the conclusion while advocating a different explanation (uncommon descent) than Day (guided common descent); allies are not unanimous on mechanism.
- Equation numbers differ between PDF text ((4),(5)) and LaTeX labels (2.4, 3.1) as extracted; Dembski's abridgement inserts bracketed text that is Dembski's.

## Strongest technical point
Transparent re-derivation (127 -> 15,800 -> ~10M) that shows the book's own bound closes to a factor ~2 once mutation supply and genome length are scaled; this is the best ally-side scaling calculation and it concedes A5.

## Unknown / not checked
Whether the PDF differs from the Dembski-abridged text beyond the brackets.

# Milestone 3: Reading everything, from both sides
*2026-10-07 · stage: R1 pass 2 (complete) · commits `2c63b68`, `dea3da5`, `5d44e18`, `b0da28e`*

Pass 1 was a survey through summarizing fetches. Pass 2 replaced it with raw local copies, a bibliography entry for each source, and quotes machine-checked as exact matches against the extracted text. Three agents worked in parallel, each writing only to its own folder.

## What was collected
| Corpus | Size | Verified quotes |
|---|---|---|
| Day | 154 blog posts, 32 Zenodo files | 75 |
| Primary literature cited by either side | 37 sources | 75+ |
| Critics and allies | 48 bibliography rows, 23 profiles | 132 |

The maintainer downloaded the Kimura 1962 and Kimura & Ohta 1969 PDFs so those papers could be checked directly. *Probability Zero* was not bought, so claims that appear only in the book are tagged `secondhand`. Full texts stay out of git; the repo stores links and hashes.

## Citation fidelity: does the source say that?
**Holds for Day:**
- Kimura 1962: fixation probability ≈ 2s.
- Kimura & Ohta 1969: mean fixation time 4Nₑ.
- Yoo 2025: the 6.3 My split date.
- Bergeron 2023: 40× variation in mutation rate.
- Wistar 1967: Eden's 10³²⁵ vs 10⁵² comparison.
- Haldane's 1/300, verified through Nunney 2003.

**Does not hold:**
- **Kimura 1962** gives 1/2N for the neutral fixation probability, not 1/2Nₑ.
- **Kimura & Ohta 1969** never mentions recombination, which Day cites it for.
- **Zeng 2021:** the s ≈ 0.001 Day uses is the mean coefficient of *negative* selection, not beneficial.
- **Yoo 2025:** neither the 410 Mb nor the 187 Mb figure behind "205M required fixations" appears in the paper. The 1,140 inversions are a six-ape count.
- **Langergraber 2012** says "at least 7–8 My", independent of fossils, not 6–7 My.
- **"Chalub 2012"** was not found.

**Partial:**
- Balloux & Lehmann 2012 shows k ≠ μ, but only with overlapping generations *plus* fluctuating N. The figures 0.743 and 32.3 are not in the paper.
- Chalub 2022's maths is correct, but its model has no mutation, so it says nothing about the substitution rate.
- CSAC 2005: polymorphism is 14–22% of divergence, so fixed divergence is at most 1.06% of the 1.23% total.

The ledger applies to critics too. For example, the critics' general case on fixation probability rests on the martingale property, not on Kimura 1962 alone.

## Day's numbers move
The version ledger records each quantity that changed across Day's sources:

| Quantity | How it changed |
|---|---|
| Required fixations | 30M (2019) → 20M (2025) → 205M (2026). The 205M figure mixes SNV events with base pairs. |
| Generations per fixation | 1,600 → 1,322 (≥95% rule) → about 1,587 under the strict count in Day's own LTEE data paper |
| Neutral substitution rate (k/μ) | k = μN/Nₑ (Jan–Feb 2026) → **conceded on 2026-08-27**: "Nₑ never enters the Kimura identity", the day after critic keruru retracted on the same point → k = 32.3μ reappears without a derivation (blog, 2026-10-01). The Zenodo papers were not revised. |
| Start state | Intrinsic Irrelevance assumes an empty pipe → blog, 2026-10-01: "full, but much shorter" |
| Split date | 6.3–9 My → 200–580 kya → 68 kya → 250 kya–1.3 My |
| Retraction of the Haldane cost term | 2026-05-07 |
| Hard Limits drift ceiling | "about ten thousand" in the abstract vs 35,000–114,000 in its own Table 1 |
| The 10^−34,000,000 "Bernoulli" figure | Appears in the MITTENS paper, not in the Bernoulli paper. The Bernoulli paper itself gives 10^−47,262. |

**For a reader:** the version is the unit of analysis. A verdict on a 2025 paper may not apply to the 2026 blog position, and the reverse also holds.

## The critics, with the same scrutiny
The balance ledger puts each side's best argument next to each side's weak points, branch by branch.
- **Strongest:**
  - "KITTENS" (Reddit) breaks Day's shortfall into 94,000× (mutation supply) × 11.7× (base pairs vs events).
  - Hancock and Mansfield on latency vs throughput.
  - keruru on the ancient-DNA test.
  - Nesslig20, who separates the cost of selection from drift.
- **Weak:**
  - Uncited inputs (McCarthy's 3%, Mansfield's 2% example, which comes out about 44× short).
  - Expected values given without variance.
  - Hancock's video answers an earlier version of the argument.
  - P.Z. Myers offers no numbers.
  - Camestros reviewed only the first edition.
  - KITTENS is AI-assisted and cites from memory.
- **Gaps:**
  - No critic in the corpus engaged Nunney 2003, the only literature rebuttal on the cost of selection.
- **Ally:** Hössjer re-derives Day's chain and finds about a 2× gap. The ledger notes that this gap comes entirely from Day's turnover coefficient d = 0.45, which MITTENS 3.0 itself drops.

## Gaps left open
- The paid book.
- Rosenhouse ch. 6.
- The Good 2017 supplement (the source of the ≥95% rule).
- Haldane 1957's primary text.

Each is recorded with its access status in `sources/bibliography.md`.

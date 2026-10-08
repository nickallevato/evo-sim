---
id: B1d
title: "Day (blog 2026-10-01): the pipeline was full but short (228,000 generations); 29-billion pipe at 8 billion"
side: day
branch: B
parent: B1
edges: [{type: revises, target: B1}, {type: revises, target: B1c}, {type: revises, target: B1a}]
load_bearing: false  # it concedes the full-pipe premise at the split; the remaining claim is the post-split lengthening, which is B2
sourcing: firsthand
status: reviewed
verdicts:
  internal: pending
  fidelity: n/a
  external: "contested"   # implied Ne_anc ~5.7e4 is below Yoo's 1.3-2.0e5; derived d ~0.88% vs 1.23% observed (not simulated)
---

## Statement (verbatim)
> At the time of the CHLCA split, we can assume that it was full and 228,000 generations long, so fixations can be reached around now.

Source: [Day, "The Education of a Population Geneticist" (blog)](https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/), 2026-10-01, ¶36 of extracted text

> Back then, at the ancestral census of ~100,000, the pipe was 4Nₑ ≈ 228,000 generations long.

Source: [Day, "The Education of a Population Geneticist" (blog)](https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/), 2026-10-01, ¶31 of extracted text

> At census 8 billion, it’s 29 billion generations long.

Source: [Day, "The Education of a Population Geneticist" (blog)](https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/), 2026-10-01, ¶31 of extracted text

## Formal statement
Day now grants a full pipe at the split, with transit 4Nₑ = 228,000 at census ~100,000, scaling with census thereafter.

**Arithmetic audit (derived, python3 -I):**
- 4Nₑ = 228,000 → Nₑ = 57,000 = 0.57 × census 100,000. This equals Wright's Nₑ = (4N−2)/(Vₖ+2) with Vₖ = 5: (4×10⁵−2)/7 = 57,143, 4Nₑ = 228,570 (Z22129121 p.4; human Vₖ = 5 in its Table 1). Census 1,000,000 → 2.2857M, matching "2.28 million".
- Census 8×10⁹ with the **same** Nₑ/N = 0.571 gives 4Nₑ = 1.83×10¹⁰, not 2.9×10¹⁰. 29 billion requires Nₑ ≈ 7.3×10⁹ = 0.91 N, the value in HL Table 3. Ratio stated/reproduced = 1.59. Inputs for the 8-billion figure are not stated in the post.
- Cross-paper: Z18525547 uses Nₑ = 3,300 for the same census range (N/Nₑ = 30 at N = 100,000); this post and Z22129121 imply Nₑ/N = 0.57 at the same census. The two cannot both hold.
- With a full pipe of length 228,000 against T = 252,000, IR's own formula (empty start) would give 30 × (252,000 − 228,000) = 720,000; the post asserts instead that the ancestral fill is delivered, so the IR deficit does not apply to the pre-expansion window.

## Assumptions
- Stated: Ancestral census ~100,000 and a full pipe at the split; the pipe lengthens with census thereafter.
- Implicit: Nₑ/N ≈ 0.57 (Wright, Vₖ = 5); the lengthening post-expansion pipe is relevant to divergence accumulated before the expansion (it is not: the 8-billion era is a few hundred generations of 252,000).

## Responses
- Against: "The ‘pipeline’ would have been full from the X generations preceding that point in time." ([Mansfield (@brianmansfield6912), YouTube comments under Examining Origins video jDxFtCOGZ3A](https://www.youtube.com/watch?v=jDxFtCOGZ3A), comments retrieved 2026-10-07, comment UgyhNduYke46IStQ5pd4AaABAg.AbQefbrLxzSAbRHJx-mRP2 (Mansfield)) (this post concedes the point at the split)
- In support: Day: "Only a relatively small number of fixations have taken place in 280 generations because those mutations were already in most of the modern European population from their common ancestors." (aDNA, branch C).
- Weaknesses in the responses: Conceding a full pipe at the split removes the IR deficit for the divergence window; the post does not recompute 7.56M with a full pipe. Critics have not quantified post-expansion drainage either (B1b: saturating deficit after large expansions).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Wright (Nₑ formula, via Z22129121 p.4) | Nₑ = (4N − 2)/(Vₖ + 2) | unverified (original not retrieved) |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: Pre-expansion fixed substitutions are delivered from a full ancestral pipe; post-expansion flux is depressed (B2).
- Under the opposing model: Full pipe at the split and a late (few-hundred-generation) expansion mean the 252,000-generation count is ≈ μLT with at most a small late deficit.
- Result that would change a verdict: B1c run with Nₑ(t) reaching census-scale values only in the last ≈400 generations would confirm the opposing reading for the divergence count.

## Check
R4 context (research/checks/results/R4-B1c-B4a.md; REVIEW-R4-steelman-day): a full pipe of 228,000 generations implies Ne_anc ~ 5.7e4 (4Ne). Not simulated; derived by the Day-side reviewer: d ~ 0.605% + 0.274% = 0.88%, about 71% of the observed 1.23%, against Yoo's sourced 1.32-1.98e5. B1d contradicts the empty-start premise of B1c. Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)
Earlier note: Script: none yet. Arithmetic computed in python3 -I (this session). Version-ledger entry proposed: B1 start state, empty (IR 2026-09-22) then full but 228,000 generations long (blog 2026-10-01).

## Simulator variables implied
- census N(t)
- Nₑ/N ratio or Vₖ
- pipe length 4Nₑ(t) display

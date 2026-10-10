---
id: F1a
title: "Day: LTEE G_f is a throughput measurement; yet the Q&A divides by a latency-derived 19,800 \"generations per fixation\""
side: day
branch: F
parent: F1
edges: [{type: attacks, target: F1}, {type: depends-on, target: F3}]
load_bearing: true  # decides whether the serial reading is a straw man or Day's own usage
sourcing: firsthand
status: extracted
verdicts:
  internal: non-sequitur
  fidelity: n/a
  external: pending
---

## Statement (verbatim)
> The MITTENS calculation does not assume sequential fixation. The LTEE rate of 1,322 gen/fix is a total throughput measurement

Source: [Day, "The Education of a Population Geneticist" (blog)](https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/), 2026-10-01, ¶17 of extracted text

> The Probability Zero derivation at s = 0.001 does compute a per-fixation time, but dividing total generations by per-fixation time to get maximum achievable fixations is not an assumption of sequential processing. It is also a throughput calculation

Source: [Day, "The Education of a Population Geneticist" (blog)](https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/), 2026-10-01, ¶18 of extracted text

> N_e = 10,000 (standard effective population constant) T = 22 years (generation, Gurven & Kaplan 2007) L = 51 years (lifespan based on Coale-Demeny-West life tables) s = 0.001 (selection coefficient, Zeng et al 2021) t ≈ 19,800 generations per fixation

Source: [Day, "Probability Zero Q&A" (blog page)](https://voxday.net/2026/01/19/probability-zero-qa/), 2026-01-19 (page updated 2026-02-14 per blog), ¶5 (the formula is not printed in the Q&A)

> It probably won’t escape your attention that 19,800 > 1,600. So using the 1,600 generations rate was extremely generous to the Modern Synthesis model.

Source: [Day, "Probability Zero Q&A" (blog page)](https://voxday.net/2026/01/19/probability-zero-qa/), 2026-01-19 (page updated 2026-02-14 per blog), ¶6

> The six-fixation figure (now seven at updated parameters) comes from the beneficial fixation time at s = 0.001, not from neutral drift.

Source: [Day, "The Education of a Population Geneticist" (blog)](https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/), 2026-10-01, ¶24 of extracted text

## Formal statement
**Arithmetic audit (derived, python3 -I):** (2/0.001) × ln(2 × 10,000) = 2000 × 9.9035 = 19,807 ✓ (19,800). This is a *latency* (deterministic sweep time of one allele, F3). The Q&A calls it "generations per fixation", i.e. G_f = 19,807, a throughput of 1/19,807 = 5.05×10⁻⁵ per generation — the serial reading.
Day confirms in the Education post that the six-fixations-over-9-My figure (Mansfield quotes it) comes from this latency (quote 3). Reconstruction (derived; Day does not print the inputs): 9×10⁶ y / 32.5 y × 0.45 / 19,807 = 6.3; and 146,250 / 19,807 = 7.4 ("now seven at updated parameters"). Neither contains a parallel-width factor, so the figure is window × d ÷ latency. Other readings of the same divisor: 252,000/19,807 = 12.7; 252,000 × 0.45/19,807 = 5.7.
The Education post (quote 2) describes the division as a throughput calculation "adjusted for parallelism" but does not identify a width factor in the six/seven figure. The 2026-02-14 post: the human rate "works out to 19,800" (and 40,787 with corrections).
Z18167588 (Bernoulli) §7.8 multiplies by a parallel width instead: (300,000/440) × 230 = 157,000, where 440 ≈ (2/0.01) ln 9 = 439 is a latency and 230 is a number of simultaneous sweeps (not derived; the paper says it works backward from the constraint). That paper is branch G.
(Note: Z18441321 uses "19,800 effective generations" for a different quantity, 23,000 × 0.86; the coincidence of numbers is not related.)

## Assumptions
- Stated: G_f from the LTEE is parallelism-adjusted; the human value (19,800) is computed from consensus numbers.
- Implicit: The 19,800 figure is a per-allele sweep time at s = 0.001, Nₑ = 10⁴ and is equated with a spacing between fixations; realistic sweeps in parallel require a width factor (Bernoulli paper: 230).

## Responses
- Against: "The time it takes for one allele to get fixed is not important, it is the time BETWEEN successive fixations that is important." ([Mansfield (@brianmansfield6912), YouTube comments under Examining Origins video jDxFtCOGZ3A](https://www.youtube.com/watch?v=jDxFtCOGZ3A), comments retrieved 2026-10-07, Mansfield); RESULTS F1 (spacing 3 vs latency 847).
- In support: Camestros concedes the LTEE number is an average (CA-10 in the harvest): "He is correct that when he calculated the number it was an average."
- Weaknesses in the responses: Mansfield and Hancock (GG-01, tied to Duffy's 180-interval slide) read F_max as serial; the Education post disowns that, while also confirming that the six/seven-fixation figure and the Q&A 19,800 come from a latency. Neither side has shown whether interference (F2) makes the effective width near 1.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Zeng 2021 | see F3a | verified-misread (ledger) |
| Good 2017 | "We find that the trajectories in Fig. 1 are inconsistent with a "periodic selection" model in which individual driver mutations fix in a sequence of discrete selective sweeps." | verified (ledger): the LTEE shows overlapping sweeps, i.e. parallelism in the measured G_f |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: LTEE G_f = 1,322 already contains parallelism; 19,800 shows humans are slower than E. coli.
- Under the opposing model: A latency of 19,807 generations is not a spacing; realistic parallel width (hundreds) puts the human spacing well below 19,807 (F1, F2).
- Result that would change a verdict: F2 (interference) with human-like parameters; or Day stating that 19,800 enters no count.

## Check
Script: none (arithmetic computed with python3 -I). Related: `research/checks/f1_throughput.py`.

R4 F1b (research/checks/results/R4-F1b.md; review #16, 2026-10-09): supports the first half (a throughput count already includes parallelism; direct measurement shows overlap), but does not clear the non-sequitur: dividing by a latency-derived 19,800 as if it were an inter-fixation time is not tested by F1b. Verdicts unchanged.

## Simulator variables implied
- G_f as latency or as spacing (explicit toggle)
- parallel width

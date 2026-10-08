---
id: C2a
title: "d is derived from life tables as d = T x (integral of mortality weighted by l(x) v(x)) / (integral of l(x) v(x)); it is mathematically distinct from Hill's Ne/(N1 T) and falls from 0.53 (Neolithic) to 0.015 (2020)"
side: day
branch: C
parent: C2
edges: [{type: supports, target: C2}, {type: depends-on, target: A4}]
load_bearing: true  # Supplies the theoretical grounding for d = 0.45; the empirical fits in C2 are circular without it, and MITTENS 2025 and Haldane+d (487) use d.
sourcing: firsthand
status: reviewed
verdicts:
  internal: "holds"   # derivation correct for hazard-scale s
  fidelity: "unverifiable"   # Coale-Demeny West tables not retrieved; Hill/Charlesworth not retrieved
  external: "contested"   # a unit conversion, not a separate correction to the speed of selection
---

## Statement (verbatim)
> "d = (Actual allele frequency change per generation) / (Change predicted by discrete-generation model)"

Source: [The Selective Turnover Coefficient](https://zenodo.org/records/18166234), Z18166234, 2025-12-24, §2.3, ¶33 of docx text extraction (quote Q20).

> "d = T × [∫ μ(x) × l(x) × v(x) dx / ∫ l(x) × v(x) dx]"

Source: Z18166234, §3.3, ¶51 (Q21).

> "Equivalently, if a discrete-generation model predicts Δp = sp(1−p), the actual change in an age-structured population is: Δp_{actual} ≈ d × sp(1−p)"

Source: Z18166234, §2.3.

> "Hill's ratio governs drift, while d governs selection. For realistic demographic schedules, d > N_{e}/(N₁T)—selection is less impeded by overlapping generations than is drift."

Source: Z18166234, Abstract.

> "For practical purposes, d ≈ 0.50 ± 0.10 represents a reasonable range for Neolithic and earlier populations, with the upper bound allowing for hunter-gatherer-type mortality patterns."

Source: Z18166234, §5.2.

Defence of the integral (blog, 2026-01-19):
> "If l(x) and v(x) were constants, they'd cancel and you'd get d = T × ∫μ(x)dx. But they're not constants, they're age-dependent functions that capture the demographic structure of the population."

Source: [Probability Zero Q&A](https://voxday.net/2026/01/19/probability-zero-qa/), B2026-01-19-probability-zero-qa, ¶16 (Q23).

## Formal statement
l(x) survivorship, b(x) fecundity, v(x) = [1/l(x)] integral_{y>=x} l(y) b(y) dy (Fisher), mu(x) = -d ln l(x)/dx, T mean generation time. d = T x integral(mu l v) / integral(l v). Table 1 of the paper (Coale-Demeny West, natural fertility): Neolithic e0 = 32, T = 27.7, d = 0.53; Classical 37, 27.9, 0.44; Early Modern 42, 28.0, 0.35; Industrial 47, 28.1, 0.27; 1900 52, 28.2, 0.21; 1950 60, 28.4, 0.12; 2000 67, 28.5, 0.06; 2020 78, 30.7, 0.015.

Hill (1972) as cited in the paper: Ne = N1 T/(1 + Vk/2), so Ne/(N1 T) = 2/(2 + Vk).
derived: Vk = 2, 4, 5, 7, 8 give 0.50, 0.33, 0.29, 0.22, 0.20 (paper: 0.50, 0.29, 0.20 for 2, 5, 8; holds).
derived: 0.53 / 0.015 = 35.3, matching "~35-fold" (holds).
Parameter link: `selection.turnover_d` = 0.45 sits between the paper's 0.53 (Neolithic) and 0.44 (Classical); the paper says this is "precisely what one would expect" for a sample weighted to later periods.

Observation (not a verdict): the integral weights death by reproductive value, so it measures the mean mortality hazard at the age of reproductive value, times T. In the standard stable-age theory with a life table, T x (mean hazard weighted by l v) is not obviously a ratio of selection response to a discrete-generation response, because the discrete-generation benchmark itself depends on the definition of s (per generation, per year, per lifetime). The check below tests this directly.

## Assumptions
- Stated: stable age distribution, weak selection, no frequency dependence, constant vital rates (§6.3).
- Implicit: that s in the benchmark discrete-generation model is a per-nominal-generation coefficient on the same scale as in the age-structured model; that the mortality force is the relevant "turnover" rather than (for example) generation time T itself.

## Responses
- Against: Camestros CA-03 and CA-12 (d undefined in chapters read; "would clearly have changed during human evolution"); Nesslig20 (PS post 1): "Will does not explain what it actually means". The first is answered here; the second is answered by the paper's own Table 1 (d varies with epoch).
- In support: none independent found.
- Weaknesses in the responses: critics did not engage the integral; no critic has simulated an age-structured population.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Hill 1972; Felsenstein 1971 | Ne for drift in age-structured populations (cited in abstract and refs) | not retrieved (fidelity ledger: "record only") |
| Charlesworth 1974, 1994 | selection with reproductive-value weighting (cited as the source of the "full theory" of which d is a "simplified summary statistic") | not retrieved |
| Coale-Demeny-Vaughan 1983 | model life tables | not retrieved |
| Gurven & Kaplan 2007 | forager mortality; paper gets d ≈ 0.66 at e0 ≈ 28 | not retrieved |

## Pre-registered prediction
- Under the claimant's model: in an age-structured population with the Coale-Demeny e0 = 32 table, the per-T-year frequency change of a rare allele under a small viability effect is 0.53 x s p q (d from the paper's formula).
- Under the opposing model (standard age-structured theory as cited by Day from Charlesworth 1994; a hypothesis, since the source text was not retrieved): the change per mean generation time is s p q when s is the effect on lifetime reproductive output (fitness per generation). If s is instead defined per year, the change per year is s p q / T. In either case no separate factor d < 1 arises beyond what the scale of s defines. The two models therefore differ on whether d is a real demographic correction or only a rescaling of s.
- Result that would change a verdict: measured Delta-p per T years in the simulation equals d x s p q for d computed from Day's formula over several life tables (e0 = 25 to 78) to within a few percent (then C2a is supported as a result, whatever the definition of s), or equals s p q for all of them (then d is not a correction at this scale).

## Check
R4 C2 (research/checks/results/R4-H-C2.md): the derivation is correct: integral of l*v = T for a stationary population, so d = mean cumulative hazard at the age of mothers (0.789 vs 0.784 numerically); first-order Euler-Lotka gives T*dr = s_gen. d is therefore a conversion between hazard-scale and per-generation s. Table 1 values (0.53 ... 0.015) not reproduced with a Siler stand-in (0.79/0.93 at e0 = 32; 0.13-0.21 at e0 = 78), unresolved because Coale-Demeny tables were not retrieved. Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)
Earlier note: Script: none yet (shared spec with C2: `research/checks/c2_overlap_vs_standard.py`, planned). Compare d(l, b) from Z18166234 eq. 3.3 against the simulated ratio for (a) viability selection at one age band, (b) fecundity selection, (c) selection on all ages. Include the standard Hill-Felsenstein Ne for the drift side of the same population, and a Wright-Fisher discrete control. · Result: not run · Review: pending

## Simulator variables implied
Life table l(x), fecundity b(x), age at first and last reproduction, T, selection class (viability or fecundity), Ne from Hill-Felsenstein.

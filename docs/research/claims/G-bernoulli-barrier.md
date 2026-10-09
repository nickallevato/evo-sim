---
id: G
title: "Bernoulli Barrier: parallel fixation of many loci is limited because the Law of Large Numbers compresses fitness variance (14.7x available vs 1,570x required)"
side: day
branch: G
parent: ROOT
edges: [{type: supports, target: ROOT}, {type: depends-on, target: Ga}, {type: depends-on, target: Gb}, {type: depends-on, target: Gc}, {type: depends-on, target: Gd}]
load_bearing: false
sourcing: firsthand
status: reviewed
verdicts:
  internal: arithmetic-error
  fidelity: partial
  external: "contested"   # no barrier in tested regime (r = 1/2, soft, <= 272 loci); human scale untested
---

## Statement (verbatim)
> the fitness differential between the "best" and "worst" genotypes in a population of 10,000 is only 14.7×—while the required differential is 1,570×, a shortfall exceeding 100-fold.

Source: [The Bernoulli Barrier, Zenodo 18167588](https://zenodo.org/records/18167588) (key Z18167588), pub. 2026-01-04 (modified 2026-01-07), ¶6 (abstract).

## Formal statement
n = 157,000 loci at p = 0.5, N = 10,000, s = 0.01 per locus (uniform).
Count per individual ~ Binomial(n, 0.5): mean 78,500, SD √(n·p·(1−p)) = 198.1, CV = 0.252%  (paper: 198.1, 0.25%).
Extreme genotypes in N = 10,000 (normal order statistics): ±3.72σ → 79,237 / 77,763, difference 1,474 = 7.44σ.   Paper: "Fitness ratio = (1.01)¹⁴⁷⁴ ≈ 14.7×". Required: "157,000 × 0.01 = 1,570×". Shortfall = 1,570/14.7 ≈ 107×.

`derived:` (python3 -I) The binomial and order-statistic numbers reconcile. The fitness numbers do not as stated: (1.01)^1,474 = 2.34e6 (e^14.67), not 14.7. The value 14.7 equals 1,474 x 0.01 = 14.74, an additive quantity; likewise 1,570 = 157,000 x 0.01 is additive, whereas the multiplicative counterpart is 1.01^157,000 = 10^678. The ratio of the two additive increments (1,570/14.74 = 106.5; 106.8 with 14.7) reproduces "107". So the paper labels additive fitness differences as multiplicative "ratios", and the stated multiplicative formula (stated as conservative for epistasis in s3.1) gives 2.3e6 vs 10^678 instead. In both readings the conclusion direction is the same; the magnitude of the "shortfall" differs from 107 by hundreds of orders of magnitude in the multiplicative reading.
Further `derived:` Absolute variance of the allele count grows with n (n/4 = 39,250); only the coefficient of variation (SD/mean) falls as 1/√n. The text of s7.6 says "fitness variance decreases as the number of segregating loci increases", and s7.10 itself states "the variance in total beneficial allele count is 250, but the mean is 500" for 1,000 loci. The claim is true for relative dispersion, not for absolute variance.

## Assumptions
- Stated: free recombination; unlinked loci; multiplicative fitness (s3.1); selection requires a fitness differential between extreme genotypes that exceeds the summed per-locus advantage (s3.2); Fisher: response proportional to variance (s7.6); each locus responds to its own s (s7.10) but through differential reproduction of whole organisms.
- Implicit: the "required differential" is the full all-beneficial vs none genotype (n·s), though no derivation shows a sweep at one locus requires it; all 157,000 loci are simultaneously at p = 0.5, which the same paper (s7.8) says does not happen (the active zone holds ~230); the 157,000 figure is not the 20M or 205M used in the other papers.

## Responses
- Against: Myers (PZ-01), Hancock (GG-01), Bowers (BO-02) and r/DebateEvolution (RE-01) argue parallel action is how evolution works; none engaged the Bernoulli arithmetic specifically (no numbers in PZ-01, BO-02; BO-04 verifies Bowers gave no calculations). Reddit commenter (post 1wv4zeg) describes the Barrier as an idea Day is "particularly proud of"; no calculation. KITTENS §11: "Version 3.0 says the “Bernoulli Barrier” is moot" (this is Day's blog statement, Ge, not wording found in the 3.0 text).
- In support: Day (blog 2026-10-01): the Barrier "remain[s] entirely correct"; Samson (ally) asks "where does something like the Bernoulli Barrier fall?" (rhetorical).
- Weaknesses in the responses: no critic in the corpus has checked the order-statistic arithmetic or the 14.7 vs 2.34e6 inconsistency; Day has not addressed the units issue. Neither side has run a simulation.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura 1962 (escape probability ≈ 2s) | "the probability of ultimate survival of an advantageous mutant gene is approximately twice the selection coefficient" | verified-accurate |
| Fisher 1930 (response ∝ variance) | not retrieved | unverified |
| Pritchard et al. 2010 ("have not fixed at any locus") | not retrieved | unverified |
| Wei & Zhang 2019 (epistasis at genomic scale) | not retrieved | unverified |
| Hill & Robertson 1966; Hartfield & Bataillon 2020 | not retrieved | unverified |

## Pre-registered prediction
No check has run. Proposed check G-sim (not run, long): Wright-Fisher, N = 1e3–1e4 (scaled), n unlinked loci with new beneficial mutations of s = 0.01 arising at constant rate; free recombination; hard vs soft (competitive) selection; record per-locus fixation probability, sweep time, and fixations per generation as the number of simultaneously active loci rises from 1 to ~500.
- Under Day: per-locus fixation probability and rate collapse beyond the pipeline cap (14 by the paper's criterion as derived in Gc; 230 as stated).
- Under critics: per-locus values stay near single-locus Kimura values (2s, (2/s)ln(2N)) until reproductive-capacity limits (cost of selection, branch H) bind.
- Result that would change a verdict: per-locus fixation probability dropping to <50% of 2s at n_active ≈ 230 under free recombination with soft selection (supports Day); no drop to n_active ≈ 500 (contradicts).

## Check
Arithmetic audit (python3 -I, scratch): the 14.7× formula does not reproduce as stated. Review: pending.

R4 F2 (research/checks/results/R4-F2-A.md): no saturation of throughput at n_mid = 272 with r = 1/2 (rate linear in supply, R_int 0.975); throughput falls only with tight linkage. Per-locus P_fix was not measured directly (R_int is its average). Under independence the joint success probability multiplies, which is the specific-vs-any distinction (G3), not a barrier. Untested at human scale and with hard selection plus linkage. Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)

R4 G1 (research/checks/results/R4-G1.md): "(1.01)^1474 = 14.7x" is still false as written, but 14.7 is recoverable (14.74 additive, 14.67 log) and 107 is valid as a log ratio, so the audit's earlier "mixed scales / 10^672" framing is withdrawn. The open issue is the best/worst vs all/none criterion. Multiplicative fitness: expected per-locus response unchanged to 0.6% at n = 157,000; per-locus P_fix about -14% when var(ln w) ~ 3.6 (scaled); reproductive excess ~340x in the s3 configuration (1.3x at 230). Additive dilution is convention-dependent. All results soft selection. Review: `research/checks/REVIEW.md` (review #5, 2026-10-08).

## Simulator variables implied
- n_active loci, s per locus, N, fitness model (additive/multiplicative), hard vs soft selection, recombination. Outputs: per-locus P_fix, sweep time, throughput.

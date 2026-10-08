---
id: E2
title: "Punctuated equilibrium needs s in a SAFE (<0.01), DANGER (0.01-0.10) or IMPOSSIBLE (>0.10) zone: s_min = 2K ln(2Ne)/T leaves no parameter set that is both PE and safe"
side: day
branch: E
parent: E
edges: [{type: supports, target: E}, {type: depends-on, target: F}]
load_bearing: false  # Throughput leg of the PE argument; ROOT does not require it. It reuses the latency formula (2/s) ln(2Ne) for a serial schedule, which Day's own F-branch and the repo's B0.4/F1 checks bear on.
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: pending
  external: pending
---

## Statement (verbatim)
> "The parameter space divides into three zones: a SAFE zone (s < 0.01) where mutator hitchhiking is improbable but adaptive capacity is limited to fewer than 10 fixations in 10,000 generations and is insufficient for speciation; a DANGER zone (0.01 ≤ s ≤ 0.10) that PE must occupy for meaningful fixation rates but where mutator dynamics become relevant; and an IMPOSSIBLE zone (s > 0.10) where no empirical evidence supports sustained selection across multiple loci."

Source: [Strong Selection and the Improbability of Punctuated Equilibrium](https://zenodo.org/records/23034852), Z23034852, 2026-09-29, Abstract.

> "The minimum selection coefficient to achieve this in a population of effective size N_e is: s_min = 2K × ln(2N_e) / T"

Source: Z23034852, §2.1.

> "This is a floor, not a ceiling. It assumes perfect efficiency — no clonal interference, no deleterious hitchhiking, no competition between simultaneously segregating alleles."

Source: Z23034852, §2.1.

> "There is no parameter combination where PE both escapes the throughput constraint and retains its explanatory claims."

Source: Z23034852, §2.5.

## Formal statement
s_min = 2 K_new ln(2 Ne) / T, from K_new serial sweeps each of duration (2/s) ln(2 Ne); K_new = (1 - F_sv) K_total / P (standing-variation fraction F_sv = 0.2-0.7; parallelism factor P = 2-10; K_total = 20-200 from QTL counts). Table 1b parameters: T = 5,000, Ne = 500.

derived (R2 recompute): s_min at Ne = 500 is 13.8 K/T. K = 5, 12, 21, 27, 28, 6 at T = 5,000 give 0.0138, 0.0332, 0.0580, 0.0747, 0.0774, 0.0166; the paper's 0.014, 0.033, 0.058, 0.074, 0.077, 0.017 (holds). K_new column: (1-F_sv)K_total/P = 5, 12, 5, 21, 26.7, 28, 6 (paper 5, 12, 5, 21, 27, 28, 6; holds). Scenario 3: 2 x 28 x 6.908/3,333 = 0.116 (paper 0.116; holds). Sweep times at Ne = 500: 1,382 (s = 0.01), 276 (0.05), 138 (0.10), 1,535 (0.009) generations (paper: 1,380, 276, 138, 1,535; holds). K = 200, T = 5,000: 0.553 (paper 0.55; holds).

Link to repo checks (RESULTS.md B0.4): (2/s) ln(2N) overstates the mean time of an allele conditioned on fixing by 1.6-2.2x over the tested range (for example N = 500, s = 0.01: simulation 698 against 1,382; N = 2,500, s = 0.01, 2Ns = 50: 1,043 against 1,703, a factor 1.63). So s_min is overstated by about 1.6-2x for a strictly serial schedule within the paper's own Ne and s range; the zones' boundaries shift accordingly. This does not by itself test the parallelism treatment.

## Assumptions
- Stated: hard sweeps of new mutations only; K_new serial after dividing by P; the waiting time for a beneficial mutation at a specific locus is 1/(2 Ne mu_b) with mu_b = 1e-8 to 1e-6 per locus; punctuation windows of 5,000-50,000 years; K_total 20-200.
- Implicit: P is a divisor of serial time even though the formula's logic is serial; K_new counts only fixations of new mutations (the paper says standing variation lies outside, and then "the model is no longer explaining speciation"); the DANGER zone boundary 0.01 and the 0.10 upper limit are the LTEE range (Couce 2024, Wiser 2013) transferred to mammals; K_total derived from stickleback and Mimulus QTL counts (Colosimo 2005, Jones 2012, Bradshaw 1998), which the paper's own text says detect "large-effect loci".

## Responses
- Against: no critic in the corpus engaged this paper. The repo's B0.4 result (above) is the only scrutiny; Hancock/Myers/Mansfield's pipelining objection (G, F1) applies to the serial reading.
- In support: none outside Day.
- Weaknesses in the responses: the paper makes the parallelism treatment explicit (P = 2-10), so a bare "it is serial" objection does not apply to it; the more specific objection is the size of P and K_total.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Couce 2024; Wiser 2013 (s range 0.01-0.10) | not retrieved | unverified |
| Gerrish & Lenski 1998 (clonal interference bounds P) | not retrieved | unverified |
| Colosimo 2005; Jones 2012; Orr 2001; Mackay 2009 (K_total) | not retrieved | unverified |
| Nei, Maruyama & Chakraborty 1975 (bottlenecks lose rare alleles) | not retrieved | unverified |

## Pre-registered prediction
Written before any check runs.
- Under the claimant's model: for K_new >= 10 and T = 5,000 generations at Ne = 500 the minimum s is >= 0.03 and the simulated time to complete K_new independent sweeps does not fall below the s_min formula.
- Under the opposing model (B0.4 result, plus pipelining): the conditional mean fixation time is 1.6-2x shorter than (2/s) ln(2N), and independent loci sweep in parallel (F1), so the required s for the same K is lower by at least the B0.4 factor; with realistic parallelism (P of order of the number of loci) the DANGER zone is not forced.
- Result that would change a verdict: a forward simulation of K_new independent loci in an Ne = 500 isolate, with new mutations arising at mu_b = 1e-7 per locus per generation, measuring completion time against the s_min formula over s in {0.005, 0.01, 0.05, 0.1}. If simulated completion times are below T at s < 0.01 for K_new of order 10-30 (with or without clonal interference), the SAFE/DANGER dilemma fails.

## Check
Script: none yet (spec: `research/checks/e2_throughput_sim.py`, planned; reuse `wf.py`; waiting time modelled by Poisson arrival of beneficial mutants per locus). · Result: not run · Review: pending

## Simulator variables implied
K_total, F_sv, P (or explicit loci with linkage), Ne, mu_b, s distribution, window T, selection model (hard sweep versus standing variation).

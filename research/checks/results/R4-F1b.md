# R4 F1b: the in-transit fixation count, measured

**Status: run, written up, reviewed (combined, `REVIEW-R4-F1b-combined.md`), fix pass done.** Everything here is dialectic (rule RH).

## Files
- Script: `research/checks/f1b_in_transit_measured.py`, pre-registered at **fb6aac2**; md5 `800c45d0…` on na-workhorse (`raw/f1b.host`). Run 2026-10-09 17:47 -06:00, one worker, about 5 minutes. Outputs `results/raw/f1b.{out,host,pid}`, `f1b_{A,B,C}.json`, `f1b_analysis.txt`.
- **Disclosure:** a 2-replicate smoke run of the full-size cells was inspected before the commit (cell A already near 329 vs 335). The predictions were not changed afterwards, but the main run is not fully blind for cell A.
- Targets: F1 (Mansfield; "In-transit count, computed, not measured ... TODO" in RESULTS), F1b (McCarthy, "Vox Day Responds" para 22: "Obviously, mutations, whether neutral or not, do not have to increase in frequency throughout a population one at a time."), F1a (Day: G_f already includes parallelism), and Day's weak form recorded in F1: count <= window / latency.

## Method
Infinite-sites Wright-Fisher, N = 1000, genic s = 0.01, independent loci (no interference, no cost: that is F2/H). Every allele has an id and birth generation. An allele that fixes was "in transit" from its birth to its fixation; L(t) is accumulated post hoc over all fixers by a difference array, with no formula. Window 21,000 generations (5,000 burn-in, last 4,000 excluded as tail). Little's law is a comparison: L_direct against (fixers born per generation) x (mean latency).

## Results
| Cell | Ub | L direct | lambda_hat x W_hat | L / that | Theory rate x latency | var/mean of L(t) | min L | Fixers in window | Serial cap (window/latency 847) | Fixers / serial cap |
|---|---|---|---|---|---|---|---|---|---|---|
| A (12 reps) | 0.01 | 333.3 +- 0.9 | 333.3 | 1.000 | 335.5 | 0.97 | 265 | 8,264 | 24.8 | 333 |
| B (24 reps) | 0.0005 | 17.07 +- 0.18 | 17.09 | 0.999 | 16.8 | 0.95 | 3 | 422 | 24.8 | 17.0 |
| C (96 reps) | 0.00003 | 0.984 +- 0.022 | 0.985 | 0.999 | 1.01 | 1.00 | 0 | 24.5 | 24.8 | 0.99 |

Other numbers: mean latency W_hat 847 / 850 / 844 generations (diffusion 847). Fraction of generations with at least one in transit: 1.000 / 1.000 / 0.617; with at least two: 1.000 / 1.000 / 0.257 (Poisson(1.0) gives 0.26). Segregating alleles with no hindsight: 474 / 24 / 1.4 (the in-transit set is a hindsight set; what is visible is more, because most arrivals are lost).

## Predictions versus results
P1 (cell A: within 5% of Little and 8% of 335) met: 1.000 and -0.6%. P2 (var/mean 0.7-1.6) met in all three (0.95-1.00). P3 (min >= 230; ratio > 100) met: 265; 333x. P4 (B: L 15-19; at least two in transit in over 99.9% of generations; ratio > 15) met: 17.07; 1.0000; 17.0. P5 (C: L 0.8-1.3; ratio 0.75-1.35; frac(L >= 2) 0.15-0.40) met: 0.984; 0.99; 0.257. P6 (the weak form is violated in A and B) met. No prediction failed.

## What this does and does not settle
- **Settles:** the F1 open item. The in-transit count is now measured. Little's law on the same sample (L against lambda_hat x W_hat) holds to 0.1% but is an identity up to window edges, so that agreement is not a test; the tests are agreement with the theoretical rate x latency (-0.7%, +1.6%, -2.6%) and Poisson dispersion (variance/mean 0.95-1.00); the in-transit count is Poisson distributed (variance to mean 0.95-1.00), as for an M/G/infinity queue. In the free regime, "count <= window / latency" is violated by a factor of 333 (A) and 17 (B) by direct counts.
- **At the serial boundary (C)** throughput equals window / latency (ratio 0.99), and even there overlap occurs in 26% of generations. The weak form is an equality at that point, not a bound.
- **Does not settle:** feasibility. There is no interference, selective load or cost of selection in this model (F2, H, GAP-04). Cell A's supply (20 new beneficial mutations per generation) is far from any stated human value; cell C's supply (0.06 per generation) is the nearest. The real question, whether a human-scale beneficial supply can run in parallel, is untouched.

## Who this helps
- **Critics (Mansfield, McCarthy):** the pipelining point is now a measurement. Latency does not bound throughput without interference, and the critics' "not one at a time" is exactly what the in-transit series shows. The RESULTS F1 caveat that the count was an identity can be closed.
- **Day:** his F1a position, that G_f is a throughput that already contains parallelism, is the one the data support; the dispute over the serial reading is about a formula (19,800 from latency) rather than his stated model. His strong claim (feasibility at human parameters, interference and cost) is not touched, and the check shows the overlap is negligible near the regime he cares about: at cell C's supply, 38% of generations have nothing in transit, so latency and spacing are the same order and the serial picture is not far off there.

## Review resolution
- MINOR-0 (ratio header): relabelled "Fixers / serial cap". MAJOR-1 (Little's law is an identity on the same sample): wording corrected above; the informative tests are named.
- MINOR-1 and MINOR-2 (hindsight set only; only genic beneficial s = 0.01, not neutral alleles): stated as limits. Neutral latency (about 4N generations) obeys the same identity but was not simulated. MINOR-3: the Day-side text is extended: F1b does not clear F1a's non-sequitur (the 19,800 division is a latency used as a rate). MINOR-4: feasibility at human scale, with interference, stays untouched.
- No new run. No verdict changes (F1 stays holds / n/a / contested; F1b external contested -> supported for the independent-loci free regime only).

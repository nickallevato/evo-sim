# R4 F1a: Day's serial use of the latency-derived 19,800 against parallel sweeps

**Status: run, written up, combined review done (`REVIEW-R4-F1a-combined.md`).** Dialectic (rule RH).

## Files
- Script `research/checks/f1a_serial_vs_parallel.py`, pre-registered at **385df94**; run on na-workhorse 2026-10-09 (one process, minutes); `results/raw/f1a.{out,json}`, host record `results/raw/f1a_b2b_g2c_rerunA.host`. Reuses `wf.py` (`substitutions_demog`, `kimura_u`), the F1/F1b setup.
- Targets: F1a quotes (Education post para 17-18, 24; Q&A "t ~ 19,800 generations per fixation"; B0.4 latency entry in RESULTS).

## Method
Day's inputs N_e = 1e4, s = 0.001 (4Ns = 40) scaled to N = 1000, s = 0.01 (same 4Ns, same as F1/F1b). Day's formula latency L = (2/s) ln(2N) = 1,520 (19,807 at his scale). Window W = 7L = 10,640 generations (his "seven"). Independent loci, genic selection, infinite sites; no interference (F2). Three supply cells with Kimura rate = k/L, k = 1, 10, 100; 48 replicates each.

## Results
| k (rate x L) | U_b | Serial reading (W/L) | Parallel prediction (rate x W) | Observed (mean +- SE) | var/mean | In transit (rate x ~850) |
|---|---|---|---|---|---|---|
| 1 | 1.66e-5 | 7 | 7 | 7.10 +- 0.36 | 0.89 | 0.56 |
| 10 | 1.66e-4 | 7 | 70 | 71.9 +- 1.2 | 0.90 | 5.6 |
| 100 | 1.66e-3 | 7 | 700 | 702.1 +- 4.7 | 1.53 | 55.9 |

All pre-registered predictions met: counts at 7 (in [5.5, 8.5]), 71.9 (in [63, 77]), 702 (in [630, 770]); observed / serial = 1.01, 10.3, 100.3 (k within 10%); dispersion 0.89-1.53 (in [0.6, 1.6]). The latency does not cap the count; supply sets it.

## What this does and does not settle
- Dividing a window by the latency 19,807 returns the true count only at the serial boundary (k = 1), where supply is exactly one successful allele per latency. At any higher supply it understates by k. So Day's "t = 19,800 generations per fixation" is a spacing only if supply is that low; the six/seven count is a supply statement, not a result of the sweep time. This supports the first half of F1a (G_f is a throughput) and the F1b conclusion, and does not clear the non-sequitur: the Q&A divides by a latency as if it were a spacing.
- Not tested: interference, selective load, human-scale supply (F2, H, GAP-04). The F1a verdicts depend on whether Day's six/seven includes a width factor (the claim file says it does not); no simulation settles that.

## Who this helps
- **Critics (Mansfield, McCarthy, Hancock):** the serial division is a supply assumption in disguise; overlapping sweeps are the normal case once supply exceeds one per latency (5.6 and 56 in transit at k = 10 and 100).
- **Day:** his stated position that the rate is a throughput set by supply is what the simulation shows; at k = 1, his serial number is exactly right, and overlap there is only about half an allele in transit. Feasibility at human supply is untouched, and that is where his argument lives.

## Review resolution
See `REVIEW-R4-F1a-combined.md`. No verdict changes (F1a stays non-sequitur / n/a / pending).

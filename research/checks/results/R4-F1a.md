# R4 F1a: Day's serial use of the latency-derived 19,800 against parallel sweeps

**Status: run, written up, combined review (`REVIEW-R4-F1a-combined.md`) and independent re-review (`REVIEW-R4-F1a-independent.md`) done; fix pass 2026-11-26 (below).** Dialectic (rule RH).

## Files
- Script `research/checks/f1a_serial_vs_parallel.py`, pre-registered at **385df94**; run on na-workhorse 2026-10-09 (one process, minutes); `results/raw/f1a.{out,json}`, host record `results/raw/f1a_b2b_g2c_rerunA.host`. Reuses `wf.py` (`substitutions_demog`, `kimura_u`), the F1/F1b setup.
- Targets: F1a quotes (Education post para 17-18, 24; Q&A "t ~ 19,800 generations per fixation"; B0.4 latency entry in RESULTS).

## Method
Day's inputs N_e = 1e4, s = 0.001 (4Ns = 40) scaled to N = 1000, s = 0.01 (same 4Ns, same as F1/F1b). Day's formula latency L = (2/s) ln(2N) = 1,520 (19,807 at his scale). Window W = 7L = 10,640 generations (his "seven"). Independent loci, genic selection, infinite sites; no interference (F2). Three supply cells with Kimura rate = k/L, k = 1, 10, 100; 48 replicates each. Post hoc (fix pass): the only quantity matched to Day's inputs is 4Ns = 40; times are compressed 10x, and nothing here runs at N_e = 1e4 or s = 0.001 themselves.

**What the design is (post hoc, fix pass; independent MAJOR-1).** U_b in each cell is set so that the Kimura rate 2N U_b u equals k/L, and the observed count is compared with rate x W = 7k. The expected count is therefore fixed by construction; the run checks that `wf.substitutions_demog` reproduces Kimura's fixation rate at 4Ns = 40 over a window of 7L, which B0 already showed for this engine. The serial reading (count = W/L = 7 at any supply) is not a rival model the simulation could have favoured: it is the statement that supply is one successful allele per latency, false by arithmetic once k > 1. The run is a consistency check of the engine and an illustration of that arithmetic at Day's 4Ns, not independent evidence on Day's reading or on feasibility.

## Results
| k (rate x L) | U_b | Serial reading (W/L) | Parallel prediction (rate x W) | Observed (mean +- SE) | var/mean | In transit, approx. (rate x ~850; not measured here) |
|---|---|---|---|---|---|---|
| 1 | 1.66e-5 | 7 | 7 | 7.10 +- 0.36 | 0.89 | 0.56 |
| 10 | 1.66e-4 | 7 | 70 | 71.9 +- 1.2 | 0.90 | 5.6 |
| 100 | 1.66e-3 | 7 | 700 | 702.1 +- 4.7 | 1.53 | 55.9 |

All pre-registered predictions met: counts at 7 (in [5.5, 8.5]), 71.9 (in [63, 77]), 702 (in [630, 770]); observed / serial = 1.01, 10.3, 100.3 (k within 10%); dispersion 0.89-1.53 (in [0.6, 1.6]). The latency does not cap the count; supply sets it. Post hoc (fix pass): each count prediction was fixed by the choice of U_b, so "met" confirms the engine, not either side's reading; "supply sets it" is true by construction of the cells. The k = 100 dispersion 1.53 is about 2.5 SE above 1 (SE of var/mean with 48 replicates is about sqrt(2/47) = 0.21) and inside the band only because the band was wide; see the resolution, MINOR-1. The in-transit column is rate x about 850 generations, where 850 is close to (2/s)(ln 4Ns + gamma) = 853, the reviewer's approximation of the conditional fixation time; it is an estimate, and F1b is where transit is measured.

## What this does and does not settle
- Dividing a window by the latency 19,807 returns the true count only at the serial boundary (k = 1), where supply is exactly one successful allele per latency. At any higher supply it understates by k. So Day's "t = 19,800 generations per fixation" is a spacing only if supply is that low; the six/seven count is a supply statement, not a result of the sweep time. This is consistent with the first half of F1a (G_f is a throughput) and with the F1b conclusion, and does not clear the non-sequitur: the Q&A divides by a latency as if it were a spacing. Post hoc (fix pass): the point is arithmetic (count = rate x W, and rate = k/L by construction); the run adds only that the engine behaves as Kimura says at 4Ns = 40, so it is not extra evidence for F1a beyond that arithmetic and B0. (Fix pass: "supports" changed to "is consistent with".)
- Not tested: interference, selective load, human-scale supply (F2, H, GAP-04). The F1a verdicts depend on whether Day's six/seven includes a width factor (the claim file says it does not); no simulation settles that.

## Who this helps
- **Critics (Mansfield, McCarthy, Hancock):** the serial division is a supply assumption in disguise; overlapping sweeps are the normal case once supply exceeds one per latency (5.6 and 56 in transit at k = 10 and 100). Post hoc (fix pass): that is immediate from the arithmetic, and the run shows the engine reproduces it; it does not show human supply is above the boundary (GAP-04).
- **Day:** his stated position that the rate is a throughput set by supply is what the arithmetic gives and the engine reproduces (fix pass: was "what the simulation shows"); at k = 1, his serial number is exactly right, and overlap there is only about half an allele in transit. Feasibility at human supply is untouched, and that is where his argument lives. Nothing here tests whether his six/seven already contains a width factor.

## Review resolution (fix pass, 2026-11-26)
Answers every MAJOR and MINOR of `REVIEW-R4-F1a-independent.md` (I-) and `REVIEW-R4-F1a-combined.md` (C-). Brief `research/checks/briefs/F1a-analyst-1.md`. No verdict changes proposed (F1a stays internal non-sequitur, fidelity n/a, external pending). No rerun, no new script: see I-MINOR-1.

| Id | Decision | Reason and change |
|---|---|---|
| I-MAJOR-1 (near-circular design) | Accepted | The count predictions were fixed by the choice of U_b; the serial reading is not a rival model of the engine. Added "What the design is" under Method; post hoc sentences after the predictions line, in "does and does not settle" and in both "Who this helps" bullets; "supports" changed to "is consistent with", "what the simulation shows" to "what the arithmetic gives and the engine reproduces". Registered predictions and the "met" line stay as written. |
| I-MINOR-1 / C-NOTE-1 (dispersion 1.53 at k = 100) | Accepted; explanation withdrawn; overdispersion recorded as unexplained | See below. |
| I-MINOR-2 / C-MINOR-2 (in-transit column is an estimate) | Accepted | Column header now says approximate, not measured; the 850 is tied to (2/s)(ln 4Ns + gamma) = 853 as an approximation, with F1b as the measurement. |
| I-MINOR-3 (scaled N, s; 4Ns only) | Accepted | Post hoc sentence in Method: only 4Ns = 40 is matched; times compressed 10x. |
| I-MINOR-4 / C-MINOR-3 (width factor, Day side) | Accepted, already stated | "Not tested" bullet already says the verdict rests on the claim file's reconstruction; one sentence added to Day's bullet. |
| I-MINOR-5 / C-MINOR-4 (human supply, critic side) | Accepted | Post hoc sentence in the critics' bullet: the run does not show human supply exceeds the boundary (GAP-04). |
| C-MINOR-1 (not new evidence) | Accepted | Same change as I-MAJOR-1. |

**Dispersion (I-MINOR-1, C-NOTE-1), post hoc.** `results/raw/f1a.json` stores only per-cell mean, sd, sem and var/mean, not the 48 per-replicate counts, so the overlap explanation cannot be shown from existing outputs; a rerun is out of scope. It is also withdrawn on the model's own structure: in `wf.substitutions_demog` new mutations arrive as Poisson draws and each site is sampled independently (unlinked, infinite sites), so fixation times are an independently thinned and displaced Poisson process and the window count is Poisson whatever the overlap between sweeps; expected var/mean is 1 in every cell. Overlap does not correlate independent loci, so neither "overlapping Poisson mixture" (C-NOTE-1) nor the reviewer's "positively correlated" (I-MINOR-1) fits this engine. Of the three cells, one sits about 2.5 SE above 1 and two slightly below (0.89, 0.90); chance across three cells is the most likely reading, but that is not shown, and the k = 100 excess stays recorded as unexplained. It moves no number the check rests on (the means). Day side: expects nothing from it. Critic side: likewise; neither the serial nor the parallel reading predicts overdispersion here.

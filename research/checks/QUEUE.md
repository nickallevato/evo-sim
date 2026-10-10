# Work queue

The live queue (moved out of `REVIEW.md` on 2026-10-09 to save tokens: agents that only need the queue read this file, not the review log). Update it here; `REVIEW.md` keeps the review log only.

## Queue (after review #13)
In flight (2026-10-09; one subagent at a time from now on, per the user; compute on na-workhorse only):
- **XT (cross-tool replication in fwdpy11):** post hoc edit committed (sizes, bootstrap SE; before any main run). Smoke passed on na-workhorse (SLiM not available; fwdpy11 0.24.7 is the independent tool). Main run `xt_cross_tool.py all 1` (1 worker, PID 3896711, launched 2026-10-09 16:34 -06:00; `results/raw/xt_all.{out,host}` on workhorse). Pace: b0n 10/36 chunks in 630 s, so the whole run is expected to take several hours (not within 90 min). Next: when `xt_all.out` shows the last stage (cohort) done, rsync `results/raw/xt_*` back, write `results/R4-XT.md` (with "Who this helps"), one combined review, fix pass, integration. Low-stakes tier. Note: smoke-size cohort/B1 rows are noisy and meaningless; ignore them.
- **D15 (Hössjer regulatory waiting time):** load-bearing tier (three reviews).
  - D15 progress at 2026-10-09 16:45: 17 of 714 cells in `results/raw/d15_sweep.jsonl`. The `sweep` stage was launched 2026-10-09 15:44 -06:00 (3 workers, PID 3860703; record `results/raw/d15_sweep.host`) after the post hoc f=3 amendment for the N_e=1e5 S2/S3/Fin2/Fin3 cells (639b94b). Then: write-up, reviews.
- **Async launch 2026-10-09 17:47 (-06:00), pre-registered scripts, host records `results/raw/<id>.host` on na-workhorse** (items 1-4 below; collect with `rsync -a 'na-workhorse:projects/evo-sim/research/checks/results/raw/<id>*' research/checks/results/raw/`, then `<script> analyse`):
  - **C1e: DONE** (review #18, integrated; write-up `results/R4-C1e.md`). Post hoc rerun at the matched 25 y clock DONE (c07c64f); MAJOR-1 closed.
  - **G2c/B6c: external PENDING** (review #17; MAJOR-1 diagnosed as an accounting error and rerun post hoc, see `results/R4-G2c.md`). Open: the pre-registered A-concurrency clause missed (0.6 vs [0.8, 2.5]); next, a reviewer decision or a longer-window A rerun (pre-registered) before restoring `supported`. Linked-site hitchhiking still untested.
  - **G2c A_long (post hoc, review MAJOR follow-up): RUNNING** on na-workhorse, launched 2026-10-09 (PID 4156633 plus 2 workers; `main 2 rerunA`, A reps 6-7, T = 18,000, window 6,000-17,999; about 30-35 min; pre-registered at 19f91ff, clauses L1-L3 in the script docstring). Log `results/raw/g2c_rerunA.out`. Collect: `rsync -a 'na-workhorse:projects/evo-sim/research/checks/results/raw/g2c_A_long*' research/checks/results/raw/ && rsync -a 'na-workhorse:projects/evo-sim/research/checks/results/raw/g2c_rerunA.out' research/checks/results/raw/`, then `research/.venv/bin/python -I research/checks/g2c_standing_variation.py analyse` (the A_long Hn ratio is against the mean of the six ctrl reps; in the printout the per-rep ctrl-matched list is empty for reps 6-7, use the MEAN line). Restore the G2c/B6c external verdict (supported, as a conditional) only if L1 (mean concurrency in [0.8, 2.5], each in [0.3, 3.0]), L2 (Hn ratio in [0.96, 1.04]) and L3 (drift 0.99-1.01, zero dropped) all pass; then update `results/R4-G2c.md`, the G2c/B6c claim comments, one review entry.
  - **F1b: DONE** (review #16, integrated).
  - **B5b: DONE** (review #15, integrated).
- **P1: DONE** (combined review #14 and integration 2026-10-09; milestone post and board patch deferred to the next milestone). Pre-registered c17b44a; run 2026-10-09 on na-workhorse; write-up `results/R4-P1.md`. All 17 identity groups and 33 Day-arithmetic rows came out as predicted (no failures). Low-stakes tier (re-confirmation): one combined review, then integration.

Next:
1. ~~C1e~~ DONE: the C1c model run on each published Holocene trajectory (Gravel, Gazave, Coventry, Nelson; `sources/holocene-ne.md`), pre-registered.
2. ~~B5b~~ DONE: a sourced neutral fraction against the GAP-07b/07c event counts (as written it needs 89% neutral for 20M, or an impossible 139% for 17.5M).
3. ~~F1b~~ DONE: the in-transit count is Little's law, not measured; F1b has no inbound attack.
4. G2c/B6c: simulated; external pending (see above).
5. **C1d follow-ups:** a transversion-restricted, SFS-matched neutral model; what the transition excess is.
6. **D follow-ups:** ProteinGym multi-mutant decay; a noise null for the beneficial proxy; per-sequence prevalence (D10–D12).
7. **GAP-07 follow-up:** T2T re-run (CHM13/hs1 vs mPanTro3); chimp-population polymorphism; a long-read SV set.
8. **H follow-ups:** soft-selection rate limit at human R; truncation/synergistic epistasis; a sourced human beneficial DFE and M; binomial CIs on H T50; GAP-05.
9. **Yoo 2025 μ and generation time / GAP-06.**
10. **Load-bearing claims without a reviewed check** (R5 draft): A2e, B, B2, B3, H5, H8, B3g (bookkeeping), F3a (small checks); DONE 2026-10-09: B2b, E5, E6, F1a (reviews #19-#21, no verdict change), ROOT, ROOT-M (roll-up).
11. **Review of the 12 new mapping claims** (A4e, A4f, A4g, B5j, D2k, D2l, F1c, G2h, H2a, ROOT-COV, ROOT-EP, ROOT-PG) with the usual two-sided steelman.
12. **E leftovers, GAP-03.**
13. **RH pass (rule RH, 2026-10-09):** tag the Statement quotes of existing nodes `dialectic` or `rhetoric` on every side, starting with the Darwillion lines (G3/G4) and the critics' "crank" lines. A node whose support turns out to be only rhetoric is marked, not re-scored as an error.


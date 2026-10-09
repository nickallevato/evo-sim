# Work queue

The live queue (moved out of `REVIEW.md` on 2026-10-09 to save tokens: agents that only need the queue read this file, not the review log). Update it here; `REVIEW.md` keeps the review log only.

## Queue (after review #13)
In flight (2026-10-09; one subagent at a time from now on, per the user; compute on na-workhorse only):
- **XT (cross-tool replication in fwdpy11 / SLiM):** paused after pre-registration (da1c178). `xt_cross_tool.py` has an uncommitted edit made after pre-registration (smaller run sizes; bootstrap SE robust to chunks with 0 fixations): commit it labelled post hoc, or discard it, before running. Low-stakes tier (tool validation): one combined review.
- **D15 (Hössjer regulatory waiting time):** load-bearing tier (three reviews).
  - D15: the `sweep` stage was launched 2026-10-09 15:44 -06:00 (3 workers, PID 3860703; record `results/raw/d15_sweep.host`) after the post hoc f=3 amendment for the N_e=1e5 S2/S3/Fin2/Fin3 cells (639b94b). Then: write-up, reviews.
- **P1 (machine-checked derivations, sympy/mpmath): awaiting reviews.** Pre-registered c17b44a; run 2026-10-09 on na-workhorse; write-up `results/R4-P1.md`. All 17 identity groups and 33 Day-arithmetic rows came out as predicted (no failures). Low-stakes tier (re-confirmation): one combined review, then integration.

Next:
1. **C1e:** the C1c model run on each published Holocene trajectory (Gravel, Gazave, Coventry, Nelson; `sources/holocene-ne.md`), pre-registered.
2. **Mansfield's supply argument (B5b):** a sourced neutral fraction against the GAP-07b/07c event counts (as written it needs 89% neutral for 20M, or an impossible 139% for 17.5M).
3. **Latency vs throughput (F1/F1b):** the in-transit count is Little's law, not measured; F1b has no inbound attack.
4. **Hancock's standing-variation prediction (G2c/B6c):** specified, never simulated.
5. **C1d follow-ups:** a transversion-restricted, SFS-matched neutral model; what the transition excess is.
6. **D follow-ups:** ProteinGym multi-mutant decay; a noise null for the beneficial proxy; per-sequence prevalence (D10–D12).
7. **GAP-07 follow-up:** T2T re-run (CHM13/hs1 vs mPanTro3); chimp-population polymorphism; a long-read SV set.
8. **H follow-ups:** soft-selection rate limit at human R; truncation/synergistic epistasis; a sourced human beneficial DFE and M; binomial CIs on H T50; GAP-05.
9. **Yoo 2025 μ and generation time / GAP-06.**
10. **Load-bearing claims without a reviewed check** (R5 draft): A2e, B, B2, B3, H5, H8, B2b, B3g (bookkeeping), E5, E6, F1a, F3a (small checks), ROOT, ROOT-M (roll-up).
11. **Review of the 12 new mapping claims** (A4e, A4f, A4g, B5j, D2k, D2l, F1c, G2h, H2a, ROOT-COV, ROOT-EP, ROOT-PG) with the usual two-sided steelman.
12. **E leftovers, GAP-03.**
13. **RH pass (rule RH, 2026-10-09):** tag the Statement quotes of existing nodes `dialectic` or `rhetoric` on every side, starting with the Darwillion lines (G3/G4) and the critics' "crank" lines. A node whose support turns out to be only rhetoric is marked, not re-scored as an error.


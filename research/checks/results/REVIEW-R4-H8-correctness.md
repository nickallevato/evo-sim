# Review of R4-H8 / H5 (correctness)

Reviewer role: correctness. Questions asked: is the model right (hard vs soft arms, how D is measured, the relaunch with resume)? Are the predictions scored honestly against the raw data? Is all post hoc work disclosed, and did the grid extension change any scored outcome?

Reviewed (2026-10-10):
- `research/checks/results/R4-H8.md`;
- `research/checks/h8_haldane_regime.py` at acd3a9e (pre-registration docstring) and af09e77 (`git diff acd3a9e af09e77`: the only change is the block of appended cells in `build("main")`; `run()`, the estimators and `analyse()` are byte-identical);
- `raw/h8_main.host`, `raw/h8_main.out` (head), `raw/h8_analyse.out`, `raw/h8_main.jsonl`;
- claim files H, H1, H5, H8, and the target quotes (grep in `sources/quotes-day.md`, `quotes-critics.md`).

Recomputation (local, one process, <1 s, `research/.venv/bin/python -I` on a scratchpad script reading `raw/h8_main.jsonl`; nothing committed). I re-implemented the pre-registered `lam50` and the D_obs rule, and ran them twice: on all rows, and on the pre-registered cells only (cell index < 107, i.e. the acd3a9e grid).

Provenance checks that pass:
- sha256 of `h8_main.jsonl` = f6dea632... (matches §0).
- md5 of HEAD script = 6696abdf... and of acd3a9e = daf6fa72... (matches `h8_main.host`).
- 745 rows, 745 unique (cell, rep), max cell 142. This is 553 pre-registered jobs plus 192 appended.
- The af09e77 commit time (22:25:21) equals the relaunch time in `h8_main.host`; the pre-registration (22:21:25) precedes launch (22:21:46).
- The first 19 rows are all K = 4000 Kscale jobs (long-first sort).
- Appended cells take indices 107-142, so `SeedSequence([SEED, 1, cell, rep])` of the existing cells is unchanged. Resume skips finished (cell, rep), and any job killed in flight is rerun with the same seed on the same engine. The resume is sound.

All §3 table values are reproduced exactly from the raw rows (lam50, brackets, D_obs, phi, intervals, Kscale lam50·D).

## Recomputed: effect of the post hoc extension

| Quantity | all rows (as reported) | pre-registered cells only |
|---|---|---|
| R = 1.111 lam50 10k / 20k / 40k | 0.003675 / 0.00350 / 0.002646 | identical |
| R = 1.111 D_obs (n reps) | 16.85 (22) | 16.49 (5) |
| R = 1.111 D = 30 interval 10k / 20k / 40k | 484 / 509 / 673 | 495 / 520 / 687 |
| R = 1.05 D_obs | 16.09 (17) | **undefined** (no persisting rep in any x <= 0.8 cell) |
| R = 1.05 lam50 40k | 0.000955 | **unbracketed, < 0.001135** |
| D_obs at R = e / 3 | 15.80 / 15.74 | **15.44 / 15.19** (below P1's 15.5) |
| Kscale P1 slope R = 1.111 / R = 2 | 3.0 / 2.1 | 2.8 / 1.9 |
| Kscale K = 500, R = 1.111, 20k lam50·D | 0.0306 | 0.0522 |
| lam50 at every R >= 1.111, all windows | (table) | identical |

## Findings

| # | Sev. | Locator | What is wrong | Fix needed |
|---|---|---|---|---|
| 1 | MAJOR | §2.1 ("does not drop or reweight any pre-registered cell"), §2.2, §4 P1, §7 last bullet ("no score was altered") | **The extension did change a scored outcome, and the disclosure points at the wrong R.** (a) The pre-registered D_obs rule pools every persisting rep with x <= 0.8. The appended x = 0.1-0.3 cells therefore enter the median and do reweight it. On pre-registered cells alone, D_obs is 15.44 at R = e and 15.19 at R = 3, below P1's lower bound of 15.5. **P1's "D range holds" is true only with the post hoc cells**; on the pre-registered grid it fails marginally at two R. (b) §2.2 says "The R = 1.111 values would have been unbracketed or lower without it." That is wrong. The R = 1.111 lam50 is identical in every window, and only its D_obs moves (16.49 to 16.85; intervals 495/520/687 to 484/509/673; PD1 scoring unchanged). The R = 1.05 values are the ones that depend wholly on the extension: D_obs is undefined and lam50(40k) is unbracketed without it. (c) The "up to 2x" D-invariance spread at R = 1.111, 20k (§4 last paragraph) also comes from appended cells: K = 500 lam50 is 0.0040 pre-registered and 0.0023 with the extension, and the pre-registered spread is 0.052/0.058/0.060. No other score flips: PD1, PD2, PC1, PC2, P3-P6 are unchanged, and P2's R = 1.05 phi(40k) fails either way (bound < 0.37). | Add the pre-registered-only column above to §2. Rescore P1 as "holds with post hoc cells; fails marginally at R >= e (15.44, 15.19) on the pre-registered cells". Correct §2.2 (R = 1.05, not R = 1.111). Attribute the 20k Kscale spread to the appended cells. Delete "no score was altered". |
| 2 | MAJOR | §4 rows PD1 (40k), PC2 (R = 2, 10k), P3, P6 (d = 0.45, 40k) | **Borderline scores are given as point-estimate hits or misses, but the one-step bracket straddles the threshold.** The pre-registration says lam50 is "Reported with the bracket". Converting the brackets: PD1 at 40k, [0.00245, 0.00333] gives an interval of 535-727 against the 600 cut. PC2 at R = 2, 10k, [0.0363, 0.0403] gives 5.7-6.4x against 6x. P3 at 10k, [0.003675, 0.0049] gives 363-484 against 250-400. P6 with d = 0.45 at 40k, [0.0242, 0.0322] against 0.0296. Survival is from 6 reps and is non-monotone (R = 1.111 40k: 0/6 at 1/300 but 1/6 at x = 0.6). Three of these cuts go against Day-side or critic-side predictions and one against the audit's own, so the issue is symmetric. | Label these four "indeterminate at grid resolution", with the bracket-implied range. Keep firm scores only where the whole bracket is on one side: PD1 at 10k/20k holds; PC2 R = 2 at 20k/40k misses. |
| 3 | MAJOR | §4 last paragraph ("shorten the intervals ... by up to about 10-25%"); §4 PD1 ("slower than 1/300 in every window"); §6 Day side | **The bound on the D = 30 correction is not supported by the data, and the headline it protects may be a small-K effect.** For a new mutation, D = 2 ln 2K = 30 at K ≈ 1.6e6, which is about 6 ln-units above K = 4000. lam50·D at R = 1.111 (10k) is 0.0534/0.0619/0.0683 at K = 500/1000/4000. Linear-in-ln K extrapolation gives 0.088 (1000-4000 slope) to 0.105 (500-4000 slope, capped at phi = 1). Those are intervals of about 285-340, not 484 minus 10-25%. At 20k (1000-4000 slope) it gives about 0.076, or 400. Extrapolating over 6 ln-units from 3 points is speculative either way. But the data bound the shortening only by phi <= ~1 (interval >= 285). "Slower than 1/300 in every window" is therefore not shown for the population size that actually has D = 30. | Replace "10-25%" with the range the data allow: D = 30 interval at R = 1.111, 10k, between about 285 (phi = 1) and 484 (K = 1000 value). Qualify "slower than 1/300 in every window" as "at K = 1000". **Proposed post hoc run:** Kscale at K = 16,000 (and 64,000 if the budget allows), R = 1.111 and 2, x in {0.3, 0.45, 0.6, 0.8, 1.0}, 4-6 reps, 20k generations, labelled post hoc. |
| 4 | MINOR | §3 softJ; §5 bullet 4 ("maxrel 1.1-1.4"); §6 Critics' side | **In softJ, maxrel is not the realised reproductive differential.** `rel = w / wbar` is computed over juveniles. In softJ the realised relative survival is at most R by construction (survival <= 1, mean 1/R). The reported softJ maxrel of 1.31 at R = 1.111 and 1.40 at R = 1.05 exceeds R, which shows it measures something else. It is correct in softWF, where the expected offspring of i is 2 w_i / wbar. | In softJ, report the realised differential as "<= R by construction" and drop maxrel from the softJ evidence. Cite maxrel only for softWF. |
| 5 | MINOR | §3 ("Persisting-rep k/lam is 0.92-1.11 in every sustained cell") | **Recomputed minimum is 0.83, not 0.92.** The low values are 0.831 (Kscale K = 500, R = 1.111, x = 0.6, 2 persisting reps), 0.836 (K = 4000, R = 1.111, x = 0.2) and 0.858 (hard R = 1.05, x = 0.2). These are low-lam cells with about 20 expected fixations, so Poisson noise is the likely cause. Two of the three are appended cells. | Correct the range, give the cause, and mark which cells are post hoc. |
| 6 | MINOR | §2.1 ("K = 4000, R = 1.111 extinct within 20k generations"); script comment ("went extinct at x = 0.6-0.8") | **The trigger is slightly overstated.** In the first 19 rows, x = 0.6 had 2/4 extinct (reps 0 and 3 persisted to 20k), while x = 0.8, 1.0 and 1.25 were 4/4 extinct. The extension also added K = 1000 hard cells whose outcomes had not yet been seen. That is a point in its favour, but it should be said. | "x = 0.6: 2/4 extinct; x >= 0.8: all extinct; hard K = 1000 cells unseen when the extension was decided". |
| 7 | MINOR | Script docstring "R VALUES" (R = 3 "Day's total fertility 6-8 per female") | **The R = 3 anchor has no quote.** Neither `quotes-day.md` nor any claim file contains a Day statement of total fertility 6-8. This breaks hard rule 2 if R = 3 is called "sourced". | Add the quote id and locator, or reclassify R = 3 as swept. |
| 8 | NOTE | Script docstring MODEL ("K adults at the ceiling"); `run()` hard branch | The ceiling acts on juveniles (J = min(R N, K)), so the adult count sits at about wbar·K (N/K 0.93-0.99 at R = 1.111), and p0 = 1/2N uses that N. The cap logic (extinction when R·wbar < 1 is sustained) is unaffected. | Fix the docstring wording when the script is next touched. |
| 9 | NOTE | Model | Checked and correct. softJ's `argpartition(E / w)[:K]` is Efraimidis-Spirakis weighted sampling without replacement. softWF draws parents in proportion to adult w, with selfing excluded. D_obs = sum(-ln wbar) / fixations over the recorded window, which is Haldane's cost in log units. Re-seeding charges every lost attempt to D (Day-favourable in accounting; D_obs is 0.5-1.6 above D_det, consistent). D_obs is taken from persisting reps in low-lam cells, so it carries a small survivor bias, and lam50·D_obs mixes D at low lam with lam at lam50. | None required; mention the survivor-bias direction in §7. |
| 10 | NOTE | `lam50()` | With f1 >= 0.5 and exactly 3/6 at a grid point (R = 1.111, 2, e at 10k), lam50 sits on the lower bracket edge. Ties therefore resolve downward (Day-favourable). This is pre-registered and should not be changed. | Mention in §7. |
| 11 | NOTE | §0 / target quotes | Rule RH: the quoted statements are not tagged. All scored quotes are dialectic. "This objection misunderstands Haldane's argument" (H, §2.3), which precedes the budget sentence, is framing. | Tag them in the claim-file R4 paragraphs at integration. |

## Verdict support (correctness view)
The engine, the arms and the resume are sound. The pre-registered lam50 estimates are unchanged by the extension at every R >= 1.111. PD1 (10k/20k), PC1 direction, PD2/PD3 operational refutations, PC3, P5 and P8 stand on the raw data. The correct disclosure is that P1's D range, all R = 1.05 rescaled numbers and the 20k Kscale spread depend on post hoc cells. Findings 2 and 3 limit how precisely the R = 1.111 interval can be stated: it is "about 300-700 at D = 30", not "1.6-2.2x slower than 300".

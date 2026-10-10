# R4 G2c / B6c: does a non-serial sweep model leave standing neutral variation?

**Status: run, written up, reviewed (combined, `REVIEW-R4-G2c-combined.md`), fix pass done; post hoc diagnosis and rerun below (2026-10-09). External verdict: PENDING (reverted; a pre-registered rerun clause missed).** Dialectic (rule RH): simulation of a stated conditional.

## Files
- Script: `research/checks/g2c_standing_variation.py`, pre-registered at **1ffd053**; md5 in `raw/g2c.host`. Run on na-workhorse 2026-10-09 17:47 -06:00, `main 3`: 6 jobs (ctrl/A/B x 2 replicates). N = 10,000 diploids, s = 0.01, free recombination, 500 neutral loci, 6,000 generations, window 3,000-5,999. Outputs `raw/g2c_{ctrl,A,B}_rep{0,1}.json`, `raw/g2c.out`, `raw/g2c_analysis.txt`. No post hoc runs.
- Targets: G2c, B6c (Hancock, Gutsick Gibbon video _Vu0ZVVjwHc, t=01:33:59 and t=01:31:58, auto-caption). Second model: Gc / G1 (Day, about 230 simultaneous sweeps).

## Results
| Job | Hn window / start | Hn ratio to ctrl | drift ratio N/N_e | concurrency (>= 50 copies, not fixed) | sweeps fixed in window | dropped |
|---|---|---|---|---|---|---|
| ctrl rep0 / rep1 | 0.3382 / 0.3389; 0.3266 / 0.3152 | 1.017 / 0.983 | 1.0006 / 0.9994 | 0 | 0 | 0 |
| A (1/1,322 per gen) rep0 / rep1 | 0.3425; 0.3219 | 1.030 / 0.968 | 1.0004 / 0.9992 | 0.9 / 0.5 | 3 / 2 | 0 |
| B (about 230 concurrent) rep0 / rep1 | 0.3364; 0.3339 | 1.012 / 1.004 | 1.0035 / 1.0017 | 146.1 / 146.7 | 539 / 538 | 0 |

## Predictions versus results
- **P1 met.** Control Hn stays within 0.2% and 3.6% of its start (limit 4%; rep1 is close to the edge); drift ratio 1.00 +- 0.01.
- **P2 partly missed.** A: Hn ratio 1.030 and 0.968 in [0.96, 1.04] (met); drift ratio met. Concurrency in [0.8, 2.5]: rep0 0.9 met, **rep1 0.5 missed**. With only 2-3 sweeps in the window this is Poisson noise of the quantity, and the realised sweeps (3 and 2) match the expected 2.3.
- **P3 partly missed.** B: Hn ratio 1.012 and 1.004 (met, in [0.95, 1.04]); drift ratio 1.0035 and 1.0017 (met, in [1.000, 1.03]); zero dropped arrivals (met). **Concurrency in [150, 300] missed:** 146.1 and 146.7 (2.5% below the floor; 0.64x of Day's "230"). Two things differ from the docstring's derivation: the realised fixation rate is 539/3,000 = 0.18 per generation, 1.55x the intended 0.116 (**unexplained**; the fixation probability 2s was assumed, not measured, and the window count includes sweeps begun before it), and the counted phase (>= 50 copies to fixation) lasts about 146/0.18 = 810 generations, not the 1,980 assumed. Concurrency is rate x duration, so the two errors partly offset. This is a derivation slip in the pre-registration, not evidence against the model; the Hn result does not depend on it (see below).
- **P4 (derived, not simulated).** Var(w) of order 10 needs about 1e6 concurrent sweeps at s = 0.01: re-derived in review (each sweep contributes 2 s^2 p(1-p) of about 1e-5). Stands as arithmetic.
- **P5 (linked sites not covered)** stands: nothing here speaks to hitchhiking at linked sites.
- **Result that would change a verdict: did not fire.** Hn ratio is 0.97 to 1.03 in A (falsifier < 0.10) and 1.00 to 1.01 in B (< 0.9).

## What this does and does not settle
- **Settles:** at the sweep rate Hancock's G2c file specified, and at Day's own 230-sweep scale, unlinked neutral diversity stays at theta (to within the run noise of 3%) and offspring-variance inflation is at most 0.35%. His conditional ("a strictly serial model predicts almost no variation") is true of a strictly serial model by construction, and neither model either side states is that model. Even at 146 concurrent sweeps, fitness variance does not erode unlinked diversity.
- **Does not settle:** (a) linked sites (standard hitchhiking, the real reduction, is not in the model); (b) whether 230 concurrent sweeps are feasible (load, interference: F2, H, GAP-04); (c) Hancock's claim about the SFS shape; (d) real data. Free recombination is the case most favourable to the critics.

## Who this helps
- **Day:** Hancock's "no variation" objection does not apply to Day's sweep-rate or 230-sweep models; Day's rebuttal (his models are not strictly serial) is right about the polymorphism question, and the Bernoulli paper's parallel model is not refuted by observed polymorphism at unlinked sites.
- **Hancock / critics:** the logic of the objection is sound as a conditional, and the test of it is a falsifiable prediction that was run: it applies exactly where the serial reading is used (G2g Appendix A; F1a's 19,800 division), and the simulation gives its sharp counterpart, that parallel models do keep variation. The supply of standing variation is also what makes parallel sweeps possible at all, which supports the "not one at a time" point of F1 and F1b.

## Post hoc: diagnosis of the B fixation-rate "excess" and rerun (review MAJOR-1)
**Diagnosis (by reading the code and the committed log; no run needed).** `fixed_cnt` in `run()` is cumulative over all 6,000 generations (ramp-up included); the write-up divided it by the 3,000-generation window (539/3000 = 0.18, "1.55x intended"). The log `raw/g2c.out` (B rep0) gives fixed = 195 at g = 3000 and 539 at g = 6000, so the window rate is 344/3000 = 0.115 per generation = 0.99x the intended 0.116. **There was no excess in the fixation rate; the 1.55x was an accounting error** (window counts compared with a whole-run counter). The "810-generation duration" inferred from it was also wrong; the real counted phase (>= 50 copies to fixation) is about 146/0.115 = 1,270 generations, not the 1,980 assumed in the pre-registration. That, not the rate, is why concurrency was 146 < 150.

**Fix and rerun.** Script change `g2c_standing_variation.py` (commit ca9294a, predictions R1-R4 in the docstring, "post hoc (review MAJOR)"): model B2 = B with arrival rate x 230/146 (aiming the counted concurrency at 230), 800 slots, and `fixed_win` recorded. Run on na-workhorse 2026-10-09: B2 reps 0-2, A reps 2-5, ctrl reps 2-5 (reps 0-1 are the original runs; same code path and seeds). md5 in `raw/g2c_rerun.host`; outputs `raw/g2c_*_rep*.json`, `raw/g2c_rerun.out`, `raw/g2c_rerun_analysis.txt`.

| Model (reps) | Hn ratio to rep-matched ctrl | drift ratio N/N_e | counted concurrency | window fixations (per gen) | dropped |
|---|---|---|---|---|---|
| ctrl (6) | 1.000 | 0.9998 | 0 | 0 | 0 |
| A (6) | 0.975-1.019, mean 0.993 | 0.9999 | 0.9, 0.5, 0.2, 0.7, 0.7, 0.4 (mean 0.6) | 1-3 per window | 0 |
| B2 (3) | 0.981, 0.979, 0.970 | 1.0032-1.0064 | 236, 218, 230 (mean 228) | 560, 523, 555 (0.187, 0.174, 0.185) | 0 |

- **R1 met:** B2 mean concurrency 228 in [190, 280] (above the 150 floor and about Day's 230); window fixation rate 0.17-0.19 per generation in [0.15, 0.22].
- **R2 met:** Hn ratios 0.97-0.98 each in [0.95, 1.04]; drift 1.003-1.006 in [1.000, 1.03]; zero dropped. All three B2 ratios sit 2-3% below 1, the same sign, inside the +-3% noise of ctrl but not to be read as exactly zero erosion.
- **R3 PARTLY MISSED:** A mean Hn ratio 0.993 in [0.96, 1.04] (met), but **A mean counted concurrency 0.6 is below the pre-registered [0.8, 2.5]**. With the corrected duration (about 1,270) the expectation at 0.00076 fixations per generation is about 1.0, and 1-3 sweeps per window make the mean Poisson-limited (a 6-rep mean of 0.6 is about 1.5 standard errors low), but the pre-registered clause missed and is not rescued.
- **R4 met:** ctrl Hn within 4% of its start in 6 of 6 (largest 3.6%).
- **Verdict rule (pre-registered): external stays pending unless R1, R2 and R3 are all met.** R3's concurrency clause missed, so G2c and B6c external **stay pending**. The scientific content is not in doubt on this evidence (Hn ratio 0.97-1.02 at 0.6 to 228 concurrent sweeps, versus Hancock's falsifier of < 0.10), but restoring the verdict is deferred to a reviewer or a pre-registered A rerun with a longer window; the earlier "supported as a conditional" is not restored here.
- Corrections to the account above: "the realised fixation rate is 1.55x the intended 0.116 (unexplained)" is withdrawn (it was 0.115, i.e. 0.99x); B is a 146-concurrent-sweep test at the intended rate; B2 is the first test at about Day's 230 (228). Linked-site hitchhiking is still untested.

## Review resolution
- **MAJOR-1:** the unexplained 1.55x excess of realised over intended fixation rate in B is now stated as unexplained (above). B is "about 146 concurrent sweeps at 0.18 fixations per generation", 0.64x of Day's 230, not a test at 230; the Hn result (1.004-1.012) is not sensitive to this at the 3% noise level, but extrapolating to 230 is not done.
- MINOR-1: Hn ratios carry +-3% noise (ctrl 0.983-1.017). MINOR-2: 2 replicates, A's concurrency is Poisson-limited. MINOR-4: free recombination and no cost are the best case for the parallel reading; feasibility of 230 sweeps is not tested. MINOR-5: "supports F1/F1b" is toned down to "consistent with": standing variation is an output, not the supply of beneficial variants.
- (Superseded by the post hoc section above: MAJOR-1 is now diagnosed, an accounting error, and the verdict was reverted to pending.) Original text: No new run. Verdicts: G2c and B6c external pending -> supported as a conditional (a strictly serial model predicts no variation and observed polymorphism exists); applicability to Day stays with G2 / F1a; the sweep-rate and 230-sweep models predict Hn about theta at unlinked sites.

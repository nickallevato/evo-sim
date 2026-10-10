# Review of R4 G2c / B6c (combined, low-stakes tier)

Date 2026-10-09. Method: read `R4-G2c.md`, `raw/g2c_analysis.txt`, the script docstring and engine; hand checks; nothing rerun.
**Escalation check:** G2c and B6c are not load-bearing; G2 and F1a are untouched (F1a's applicability question stays). Combined tier applies.

## 1. Correctness
Hand checks: Var(log w) = 230 x 2 x (0.01)^2 x 0.05 = 0.0023 (P3 derivation); 1e6 sweeps x 1e-5 = 10 (P4); 146.1/230 = 0.64; 539/3,000 = 0.18 vs 230/1,980 = 0.116; ctrl rep1 3.6% drift of Hn (limit 4%). Agree.
- **MAJOR-1.** The 1.55x excess of realised over intended fixation rate in B is unexplained; the write-up first attributed the concurrency miss to the sweep duration. Concurrency is rate x duration, so the duration explanation does not address the rate. Fixed: the write-up now states the rate excess as unexplained. It does not change the Hn result (1.004-1.012), but the "230" label for B is not met (146), so B is "about 146 concurrent sweeps at a 0.18 per generation fixation rate", a 1.6x short, not a 230 test.
- **MINOR-1.** The Hn ratio noise is about +-3% (ctrl 0.983-1.017), so "diversity stays at theta" is to within 3-4%; a 10% erosion would be visible, a 3% one not.
- **MINOR-2.** Only 2 replicates per model; A's concurrency (0.5, 0.9) is Poisson-limited.
- **MINOR-3.** Hn is haplotype-based on 500 loci with 4Nu = 1 initial stationary state; short-window drift of Hn is negligible, as ctrl shows.

## 2. Day-side steelman
- **MINOR-4.** Day's 230 sweeps are simultaneous *at one time* under Bernoulli/pipeline cap; the model with free recombination and no cost is the best case for the parallel reading, which supports "Day's models are not serial" but not "230 concurrent sweeps are feasible". The write-up says so.
- **NOTE-1.** Credits Day correctly on the polymorphism question.

## 3. Critic-side steelman
- **MINOR-5.** The write-up's claim that the check "supports the not-one-at-a-time point of F1/F1b" goes beyond the run (standing variation is an output, not the supply of beneficial variants). Tone down to "consistent with".
- **NOTE-2.** Hancock's conditional is a tautology for a strictly serial model; that is why the check tests the models actually stated, which the write-up explains. Linked sites (his strongest case, hitchhiking) are untested.

## Verdict on G2c
Sound after wording fixes. 1 MAJOR (resolved by correcting the account), 5 MINOR. Verdicts: G2c and B6c external pending -> supported as a conditional (see integration).

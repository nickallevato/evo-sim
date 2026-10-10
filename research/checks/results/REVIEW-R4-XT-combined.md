# Review of R4 XT (combined, low-stakes tier)
Date 2026-10-09. Method: read `R4-XT.md`, `raw/xt_all.out`, the docstring predictions; hand-checked the deficit pattern against U per stage; nothing rerun. Author and reviewer are the same Sonnet agent (the independence caveat applies; the three load-bearing re-reviews of the earlier checks are separate files).
## 1. Correctness
- **MAJOR-1.** Pre-registered clauses fail at several rows (B0.1 and B0.5 at N=50, 100; B1 counts; B1b expansion; B3b; B3c). The write-up scores them as misses and does not rescue them with the 2% allowance; the cross-tool claim is stated as "not replicated numerically", not as "replicated". Accepted as written.
- **MINOR-1.** The B0.3 N=1e4 cell has n=57 and a -4.9% difference; it passes on z, not on the 2% allowance. Stated.
- **MINOR-2.** The U-dependence of the deficit is read from different stages with different N, so it is a pattern, not a fit. Labelled a hypothesis.
- **NOTE-1.** The cohort stage has U=1.0 per gamete (see `xt_cohort.json`), the highest of any stage.
## 2. Day-side steelman
- **MINOR-3.** Day could say the fwdpy11 equilibrium deficit supports k below mu. The write-up answers: the deficit is flat in Ne/N and appears at Ne = N, so it is not N/Ne. Accepted.
## 3. Critic-side steelman
- **MINOR-4.** Critics could say "the engines agree where it matters (1/2N, scaling)". True for B3 qualitatively and B1c; not for the counts. The write-up credits both.
## Verdict
Sound as an unfavourable result. No verdict changes (B1, B3, B3c, B2a keep their verdicts; the cross-tool item in PLAN "Verification" is partial, not met).

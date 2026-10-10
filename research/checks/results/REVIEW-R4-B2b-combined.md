# Review of R4 B2b (combined, low-stakes tier)
Date 2026-10-09. Method: read `R4-B2b.md`, `raw/b2b.out`; hand checks; nothing rerun. Same-agent review (independence caveat). Escalation check: B2b is load-bearing; no verdict moves; no three-review tier.
## 1. Correctness
Hand checks: (4 x 100 - 2)/(5+2) = 56.9 (sim 57.2); X = 7 x 260,000/16 = 113,750; 2 x 80,000/16 = 10,000; 4/(1e-3) - 2 = 3,998.
- **MAJOR-1 (fixed pre-write-up).** The docstring's expected N_e/N and printed V_k thresholds used 2/(V_k+2) instead of 4/(V_k+2). Fixed in a labelled post hoc commit, rerun (13 s) gave identical sim values. Ratio predictions unaffected.
- **MINOR-1.** The model draws k_i iid and rescales nothing, so total offspring fluctuates; p' is a ratio. Residual bias is small (sim/Wright 0.998-1.022); the V_k = 10 value (+2.2%) is heavy-tailed NegBin sampling error plus finite N, within the 5% tolerance.
- **MINOR-2.** Only the one-generation drift variance is tested; mean fixation time (which gives the 4N_e in 4N_e < G) is not. The docstring no longer promises it. The ceiling's second step (4N_e < G as the criterion) is B2a's subject.
## 2. Day-side steelman
- **MINOR-3.** The write-up must not imply the ceiling is wrong; the formula reproduces. It says the discrepancy is the abstract versus table (claim file note i). Accepted.
## 3. Critic-side steelman
- **MINOR-4.** The "V_k would need thousands for N_e/N = 1e-3" point addresses variance N_e only; Day's lower N_e values elsewhere come from demographic history, not V_k. The write-up states this. Accepted.
## Verdict
Sound after the post hoc fix. No verdict changes (B2b internal holds, fidelity unverifiable, external contested).

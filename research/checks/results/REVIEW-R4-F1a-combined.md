# Review of R4 F1a (combined, low-stakes tier)
Date 2026-10-09. Method: read `R4-F1a.md`, `raw/f1a.out`; hand checks; nothing rerun. Same-agent review (independence caveat). Escalation check: F1a is load-bearing, no verdict moves, no three-review tier.
## 1. Correctness
Hand checks: L = 200 ln 2000 = 1,520; 7L = 10,640; u = 0.0198; k/L / (2N u) = 6.58e-4 / 39.6 = 1.66e-5; 7 x 10 = 70, 7 x 100 = 700.
- **MINOR-1.** The sim is almost the F1/F1b design with one new element (the counts against Day's L at his own 4Ns). The write-up should not present it as new evidence on feasibility. Stated under "does not settle".
- **MINOR-2.** The "in transit" column is rate x about 850 (conditional-time estimate), not measured here (F1b measured it). Labelled approximate.
- **NOTE-1.** The k = 100 dispersion 1.53 is near the upper pre-registered bound 1.6 (overlapping Poisson mixture across replicates; 48 reps); passes.
## 2. Day-side steelman
- **MINOR-3.** Day says the division is a throughput calculation "adjusted for parallelism"; this check cannot see whether his six/seven contains a width factor. The write-up says so and keeps the non-sequitur only where the claim file's reconstruction supports it (no width factor). Accepted.
## 3. Critic-side steelman
- **MINOR-4.** Mansfield/Hancock read the number as serial; the check shows it is serial only at the boundary supply. It does not show the humans have supply above the boundary. Stated.
## Verdict
Sound. No verdict changes (F1a internal non-sequitur, fidelity n/a, external pending).

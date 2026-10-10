# Review of R4 F1b (combined, low-stakes tier)

Date 2026-10-09. Method: read `R4-F1b.md`, `raw/f1b_analysis.txt`; hand checks; nothing rerun. Labels as in the B5b review.
**Escalation check:** F1 and F1a are load-bearing. F1b closes F1's open item (in-transit "computed, not measured") but changes no verdict on F1 or F1a (F1 stays holds / n/a / contested: feasibility is not touched; F1a's internal non-sequitur concerns the 19,800 division, which F1b does not test). Nothing on the ROOT path moves, so the combined tier stands.

## 1. Correctness
Hand checks: 0.396 per gen x 847 = 335.4 (theory 335.5) ; 333.3 / 335.5 = -0.7% ; B: 17.07 vs 16.8 (+1.6%) ; C: 0.984 vs 1.01 (-2.6%); serial cap 21,000 / 847 = 24.8 ; 8,264 / 24.8 = 333.
- **MINOR-0.** The "Ratio" column is fixers in window / serial cap (8,264 / 24.8 = 333; 422 / 24.8 = 17.0; 24.5 / 24.8 = 0.99), not L / cap (333.3 / 24.8 = 13.4). The numbers are right; the header next to L invites the wrong reading. Relabel.
- **MAJOR-1.** "Equals rate x latency to 0.1%" is Little's law applied to the same sample (L_direct against lambda_hat x W_hat). Time-averaged L equals lambda x W identically up to window edges, so 1.000 was guaranteed, not tested. The informative comparisons are: against the theoretical rate x latency (0.7%, 1.6%, 2.6% off), and the Poisson dispersion (0.95-1.00). The write-up should say so. Fixed in the resolution.
- **MINOR-1.** Only beneficial alleles with hindsight (fixers) are counted as in transit; segregating alleles (474 / 24 / 1.4) are reported but the claim "no queue" concerns both.
- **MINOR-2.** McCarthy's sentence says "whether neutral or not"; only the genic s = 0.01 case was run (neutral latency is about 4N generations; the same identity holds but is not simulated).
- **NOTE-1.** Cell A was not blind (smoke inspected); disclosed.

## 2. Day-side steelman
- **MINOR-3.** The write-up credits F1a (G_f is throughput). It should add that F1b does not clear F1a's non-sequitur (19,800 from latency used as a rate).
- **NOTE-2.** The cell C result (38% of generations with nothing in transit; weak form an equality) supports Day's position that near the human supply the serial picture is the right order of magnitude, and is credited.

## 3. Critic-side steelman
- **MINOR-4.** "Latency does not bound throughput" is shown only for independent loci with no interference; the critics' stronger version (human-scale parallelism) is not shown. The write-up says feasibility is untouched; keep it next to the "Helps critics" text.
- **NOTE-3.** Cell A's supply (20 per generation) is far from any stated human value; credited correctly.

## Verdict on F1b
Sound after two wording fixes (MINOR-0, MAJOR-1); no run needed. No verdict changes.

# R4-HF ph2: scoring against the `hf_posthoc2.py` docstring (EVO-4)

Post hoc run, registered at a995771 (script md5 a098388d…). Data: `raw/hf_ph2.jsonl` (31 rows), `raw/hf_ph2_analyse.out`
(md5 5c30ed9b… see `raw/hf_ph2.host`). Scored mechanically from the analyse tables; no write-up prose, no review yet.
**No verdict value moves** (the registration says so); verdict TEXT changes are for the analyst's write-up and fix pass.

## Run
31 of 31 jobs; HF rule 31/31, strict rule 31/31; backlog 0; peak open count 14,319; peak worker RSS 384 MB; 591.3 CPU-h.
Every cell: k/lam 0.997 to 1.003, kq4/lam 0.994 to 1.002.

## Predictions
| id | side | call | numbers |
|---|---|---|---|
| DP1 | Day | **miss** | softJ R=1.05 lam 1.6: 4/4 pass, k/lam 1.000 (0.8: 0.999), kq4/lam 0.999; no shortfall |
| DP2 | Day | **miss** | R=1.111, K=4000 passes 4/4 and 3/3; k/lam diff +0.006 (0.8), +0.002 (1.6); kq4/lam +0.008, -0.004; none lower by >0.02 |
| DP3 | Day | hit (narrow) | tau(1.6)/tau(0.8) = 1.112 (>= 1.10, margin 0.012); tau(0.8) 7,886 / 4,710 / 5,958 vs stage L 7,385 / 4,508 / 5,693 |
| CP1 | critic | hit | 31 of 31 pass; lam_max 1.6+ in all four series |
| CP2 | critic | hit | K=4000 vs K=1000 |diff| 0.006 and 0.002 (<= 0.02) |
| CP3 | critic | hit | lowest cell k/lam 0.997 (>= 0.95) |
| A1 | audit | hit | k/lam in [0.997, 1.003]; q4/q1 in [0.985, 1.014]; all runs pass both rules (0 strict misses) |
| A2 | audit | hit 8/8 | tau: 7,886; 8,766 / 4,710; 5,037 / 5,958; 6,464 / trunc 2,108; 3,777, all inside the bands |
| A3 | audit | hit | softJ ratios 1.112, 1.069, 1.085 in [1.03, 1.20]; trunc 1.792 in [1.6, 2.0] |
| A4 | audit | **miss (1 cell)** | kq4/lam in [0.994, 1.002] everywhere; |dn2500| <= 0.8% everywhere except trunc R=1.05 lam 0.8: **+3.2%** (> 3%). Trunc lam 0.8 open count still rising slightly (kq4 - kq3 = -0.002; the cell's other columns are on target) |
| A5 | audit | hit | k/lam diffs as CP2; tau(K=4000)/tau(K=1000) = 1.265 and 1.283 in [1.20, 1.35] |
| A6 | audit | hit | no backlog; peak 14,319 < 17,000 (max_open 40,000 never binds) |

## Reading
- Critic side: 3 of 3 hit. Day side: DP1 and DP2 missed, DP3 hit by 0.012. Neither a throughput ceiling at lam 1.6 (R=1.05)
  nor a K effect at R=1.111 appears. Day's latency point (tau keeps rising with lam) survives, but sub-proportionally
  (1.07 to 1.11 for softJ) and without throughput cost.
- Audit: 11 of 12 bands hit (A2 counts once); one miss (A4, trunc lam 0.8 dn2500 +3.2% vs 3%), credited to neither side.
- Scope limit (registered): softJ and truncation cannot go extinct in this model, so nothing here bears on whether a real
  population could pay the cost (Day-1 / steelman-day #1 stands).
- Under the registration: H, H8, H5 stay external `contested`; the clause "0.8 and 1.6 remain not shown at R = 1.05" is
  a candidate for withdrawal in the write-up. The B-R20/B-R21 publication hold is untouched.

## Not done
No claim-file, QUEUE, REVIEW, argmap or board edits; no review. Needs analyst write-up / fix pass per the lead.

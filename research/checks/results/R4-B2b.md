# R4 B2b: the Hard Limits ceiling X = (V_k + 2) G / 16 against simulated offspring variance

**Status: run, written up, combined review done (`REVIEW-R4-B2b-combined.md`).** Dialectic (rule RH).

## Files
- Script `research/checks/b2b_ceiling_vk.py`, pre-registered at **25f14f7**; post hoc docstring/printout fix at the following commit (N_e/N slip). Run on na-workhorse 2026-10-09 (13 s, one process); `results/raw/b2b.{out,json}`, host record `results/raw/f1a_b2b_g2c_rerunA.host`. Cannings model, no reuse of `b2a_*.py` (those test the B2a tail, not N_e).
- Targets: B2b quotes (Z22129121 p.4 formula, p.1 "about ten thousand", p.6 ceilings).

## Method
N = 100 diploids, p0 = 0.5 exactly; each parent contributes k_i gametes (iid, mean 2, variance V_k) and transmits Binomial(k_i, g_i/2) A copies (Mendelian segregation); p' = sum t_i / sum k_i. N_e(sim) = p0(1-p0) / (2 Var p'), 200,000 replicates per V_k; the realised V_k is measured. X is evaluated by algebra.

## Results
| V_k (realised) | N_e sim | Wright (4N-2)/(V_k+2) | sim / Wright | N_e/N |
|---|---|---|---|---|
| 1.000 | 132.5 | 132.7 | 0.998 | 1.33 |
| 2.000 | 99.7 | 99.5 | 1.002 | 1.00 |
| 5.002 | 57.2 | 56.8 | 1.006 | 0.57 |
| 9.999 | 33.9 | 33.2 | 1.022 | 0.34 |

Ceiling X = (V_k+2) G/16: human lineage (G = 260,000) 48,750 / 65,000 / 113,750 / 195,000 at V_k = 1 / 2 / 5 / 10; human species (G = 80,000) 15,000 / 20,000 / 35,000 / 60,000. A census-to-N_e ratio of 1e-3 needs V_k = 3,998 (Wright: N_e/N = 4/(V_k+2)); 0.1 needs V_k = 38.

Predictions: sim / Wright within 5% at every V_k: met (0.998-1.022). The docstring's expected N_e/N values (0.67, 0.50, 0.29, 0.17) were my slip (2/(V_k+2) instead of 4/(V_k+2)); corrected post hoc (1.33, 1.00, 0.57, 0.33, which the sim matches). The pre-registered test was the ratio, unaffected.

## What this does and does not settle
- Settles: Wright's formula, as printed, is right for iid offspring variance in a constant-size panmictic population, so X = (V_k+2) G/16 is exact algebra from 4N_e < G. The table values in the claim file (35,000 / 113,750 human) follow at V_k = 5.
- Does not settle: the inputs (human V_k = 5 unsourced; G window), mean versus tail (B2a), overlapping generations, demes, N_e(t). The abstract's "about ten thousand" is reached by the formula only at V_k = 0 with the 2-My species window (2 x 80,000 / 16 = 10,000); at the table's own V_k = 5 it is 35,000 to 113,750. That is the paper's internal discrepancy (claim file note i), not an N_e error.
- With V_k = 5, N_e/N = 0.57, so using the same V_k with a census of 8.2e9 gives N_e = 4.7e9, not 1e4; the N_e = 3,300-10,000 used elsewhere by Day is a different quantity (demographic history, not offspring variance).

## Who this helps
- **Day:** the offspring-variance route is sound mathematics; his formula reproduces in simulation to within 2%.
- **Critics (Mansfield):** variance N_e is nearly N for any plausible V_k, so the ceiling is a statement about census N and V_k, not about population genetics "not working", and V_k would have to be thousands to bring N_e to 1e-3 N. The ceiling's force depends on G, not on the N_e formula.

## Review resolution
See `REVIEW-R4-B2b-combined.md`. No verdict changes.

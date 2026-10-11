# R4 GAP-06: Yoo 2025's mutation rate and generation times propagated through Day's numbers

**Status: run, written up; awaiting review.** Low-stakes tier (re-confirmation and bookkeeping): one combined review (`REVIEW-R4-GAP06-combined.md`). Not integrated.

## Files
- Script `research/checks/gap06_yoo_mu_g.py`, pre-registered at **49824e0**, run locally once after the commit (arithmetic only). Nothing post hoc.
- Raw output `research/checks/results/raw/gap06_yoo.out`.
- Source: Yoo 2025, SI Note VI (MOESM1 lines 1456-1478, sha256 979759be...e03c70c). All four quotes were verified by the script: "mutation rate of 1.25×10-8 and the average generation time across the species for specific node:", "Homo-Chimp-Bonobo: 24.5 years.", "Homo-Chimp-Gorilla: 21.75 years.", "Human: 25 years".
- Day's inputs: A1, "The divergence time is 6.3 million years. At 25 years per human generation, this provides 252,000 generations."; mu = 1.2e-8. RH tag: dialectic.

## Results (raw output table, rounded)
| quantity | Day (1.2e-8, 25 y) | Yoo human (1.25e-8, 25 y) | Yoo HCB node (24.5 y) | Yoo HCG node (21.75 y) |
|---|---|---|---|---|
| A1 generations | 252,000 | 252,000 (0%) | 257,143 (+2.0%) | 289,655 (+14.9%) |
| MITTENS F_max (G_f 1,322) | 190.6 | 190.6 | 194.5 (+2.0%) | 219.1 (+14.9%) |
| shortfall on 205 M | 1.075e6 | 1.075e6 | 1.054e6 (-2.0%) | 9.36e5 (-13.0%) |
| shortfall on 20 M | 104,900 | 104,900 | 102,800 | 91,280 |
| A3 rate route k = mu (mu L N_gen) | 9.37 M | 9.77 M (+4.2%) | 9.96 M (+6.3%) | 11.22 M (+19.7%) |
| counted 21.05 M / rate route | 2.25 | 2.16 | 2.11 | 1.88 |
| B3d k/mu (Bergeron 7.97e-9, Day's input) | 32.93 | 32.93 | 32.27 (-2.0%) | 28.65 (-13.0%) |
| Haldane / Haldane + d / Term 3 counts | 840 / 378 / 6,451 | same | 857 / 386 / 6,583 | 966 / 435 / 7,415 |
| A2e kappa / U_total | 93,659 / 38.4 | 97,561 / 40.0 (+4.2%) | same | same |
| A2e threshold (N_gen / 1,322) | 190.6 | 190.6 | 194.5 | 219.1 |
| B4a Ne_anc HCB / HCG | 1.98e5 / 1.32e5 | 2.06e5 / 1.375e5 (+4.2%) | same | same |

Source swap, not a correction: putting Yoo's mu in place of Bergeron's in B3d gives 20.57 (-37.5%). Day cites Bergeron for that number, so the row is reported but not scored.

The largest change on any Yoo basis is the k = mu route on the HCG node basis, +19.7%. **No propagated Day number moves by more than 25% (rule R1 not triggered).**

## Scoring of the pre-registered predictions
| ID | Prediction | Result | Score |
|---|---|---|---|
| Day side | every change small; no conclusion moves | max 19.7%; the 1e5-1e6 shortfalls move by at most 13% | **Holds** |
| Critic side | the k = mu route moves toward 21 M but does not close the ~2x gap | 9.37 M → 9.96-11.22 M; counted / route 1.88-2.16 | **Holds** |
| G1 | <= 7% on the human and HCB bases; HCG basis +14.9% (generation counts) and +19.8% (k = mu); all < 25% | +6.3% max (HCB); +14.9% / +19.7% (HCG) | **Holds** |
| G2 | B3d 32.3 (24.5 y), 28.7 (21.75 y); swap row 20.6 (-37%) | 32.27 / 28.65; 20.57 (-37.5%) | **Holds** |
| G3 | Ne_anc × 1.042 | × 1.042 | **Holds** |
| G4 | counted / rate route >= 1.8 on every basis | 1.88-2.25 | **Holds** |

## Interpretation
- Yoo's mu and human generation time agree with Day's to 4% and 0%. On the human-chimp-bonobo node basis the generation count rises by 2%. Every number in A, A1, A3, B3d, H and A2e moves by 2-6%. That is a slip-ledger-sized difference at most, and it is not an error under R1.
- The HCG node (21.75 y) is a three-species average that includes gorilla. It is not a human-lineage generation time, so applying it to the human lineage is an upper-end sensitivity, not a correction. Even there nothing crosses 25%.
- GAP-06's real tension is the counted divergence (21 M per lineage) against the k = mu rate route (9-11 M). Yoo's values do not close it: the ratio stays at 1.9-2.2. As GAP-06 already notes, that tension is about the clock and linked selection (BGS-reduced Ne_anc, the per-year mutation literature), and it is untouched here.
- `parameters.yaml` `yoo_2025_mu_rescaling` can take 1.042 (owner's edit; for integration).

## Who this helps
- **Day side:** His mu and g match the source he would be checked against (Yoo) within 4%. The MITTENS shortfall changes by about 2% on the human-chimp node basis, and by at most 13% on any basis.
- **Critic side:** Yoo's slightly higher mu and shorter node generation time raise the k = mu expectation by 4-20%, in the direction of the counted divergence. They also lower B3d's k/mu by 2-13%, and to 20.6 if Yoo's mu replaces Bergeron's.
- **Both:** Nothing here changes a verdict. GAP-06's 2x clock tension remains open for both sides.

## Caveats
- L = 3.1e9 (Day's B3d input) is used for the k = mu route, against 3.2e9 elsewhere: a 3% difference, and the % changes are unaffected.
- The Haldane + d count uses d = 0.45 as in H.
- Yoo's mu is the value his TRAILS/MSMC runs assumed, not a new measurement. The supplement credits it to an earlier analysis ("same mutation rate of TRAILS analysis").

# R4 F3a: Day's s = 0.001 "from Zeng et al. 2021": quotes, fidelity, latency arithmetic, materiality

**Status: written up; awaiting one combined review (low-stakes tier: small checks).** Not integrated. The para-15 sentence is tagged dialectic (rule RH): it makes a numeric claim and an attribution.

## Files
- Script `research/checks/f3a_zeng_s_small_checks.py`, pre-registered at **f9c8ed9** (P1-P6). The first run, local, 2026-10-10, < 1 s, is in `results/raw/f3a.out`. **Post hoc** commit e9d2284 adds a `--posthoc` flag that strips PDF control characters before matching; its run is in `results/raw/f3a_posthoc.out`. No prediction was changed.
- Targets: F3a; F3 / F (latency); `parameters.yaml` `selection.s_zeng_2021`.

## Results against predictions
| Pred. | Prediction | Result | Score |
|---|---|---|---|
| P1 | Day para 15 and Zeng Z1-Z4 found in the raw text | Day: exact. Z1-Z3: found after normalisation (the "fi" ligature). Z4: **NOT FOUND** in the pre-registered run, because the PDF text has a `\x02` control character before the italic *s* ("mean \x02s of"). Found once it is stripped (post hoc) | **fails as pre-registered** (an extraction artefact; the quote itself is verbatim) |
| P2 | Every Zeng sentence giving a numeric mean s for real traits is in a negative-selection context; none gives a measured beneficial mean | 6 sentences with a numeric s (5 in the first run, which missed Z4); none mentions positive or beneficial selection. Z3 gives the context ("we only detected signatures of negative selection in real traits") | **holds** (fidelity **misread** re-confirmed). Caveat: the scan tests "no positive-selection value", not "negative context" sentence by sentence; Z3 carries that |
| P3 | (2/s) ln(2N_e) at s = 0.001, N_e = 1e4 = 19,807 (Day "~19,800") | 19,807 | **holds** |
| P4 | "Faster than the neutral time of 4N_e" holds at N_e = 1e4; crossover N_e* in [4,000, 5,000]; slower at Day's human N_e = 3,300 | N_e* = 4,559; N_e = 1e4: 19,807 vs 40,000 (faster); N_e = 3,300 (Z18525547): 17,590 vs 13,200 (**slower**) | **holds** (conditional on N_e >= 4,559; para 15 gives no N_e; rule C uses the Q&A's 1e4) |
| P5 | The B0.4 asymptote (2/s)(ln 4Ns + gamma) is 8,532; Day overstates it 2.2-2.4x | 8,532; 2.32x | **holds** (re-confirmation) |
| P6 | Latency ~ 1/s: replacements outside s in [0.0008, 0.00133] move it > 25%; at Zeng's own category mean 0.0005 the "faster" sentence is marginal (ratio 0.95-1.0) | window as predicted; s = 0.0005: 39,614 vs 40,000 (ratio 0.990); s = 0.0007 (Zeng's extrapolated average): 28,296 | **holds** |

## Proposed verdicts (for integration)
- **Internal: holds.** Day's arithmetic is correct (19,807), and "faster than 4N_e" follows at the N_e he uses elsewhere for this latency (1e4). The sentence would fail at his own Z18525547 human N_e of 3,300. That input is not used in this passage, so under rule S/C this is noted, not scored.
- **Fidelity: misread** (unchanged, re-confirmed from the raw text). Zeng's ~0.001 is a mean |s| for trait variants under negative selection. Zeng reports no measured beneficial mean.
- **External: contested** (unchanged). R1 materiality is **undetermined**: the latency moves by more than 25% for any s outside 0.0008-0.00133, but the repo holds no sourced human beneficial mean s to put in its place. The steady-state rate does not depend on latency (F1), so the misread reaches only latency-based arguments (F, D9, E2). It does not reach the throughput leg (MITTENS uses the LTEE rate).

## Who this helps
- **Day side:** his formula arithmetic is exact. His para-15 rebuttal to McCarthy holds on its own terms: PZ's latency uses the beneficial formula, and that formula is faster than 4N_e at N_e = 1e4. Even reading Zeng as Day does, the category means (0.0005-0.0010) leave the "faster" sentence true, though only marginally at 0.0005. The misread does not touch MITTENS's throughput figure.
- **Critic side:** the attribution is a misread. Zeng measured negative selection on complex-trait variants and says so (Z3). The formula overstates the stochastic fixation time 2.3x (B0.4). The latency does not cap the rate (F1). At Day's own human N_e = 3,300 (Z18525547) the beneficial formula is slower than 4N_e, so the "faster" sentence depends on which of Day's N_e values is used.
- **Both:** the number that would settle this, a sourced distribution of beneficial s for the human lineage, is missing on both sides (RG / H follow-ups, QUEUE item 8).

## Limits
- P1 failed as pre-registered on a PDF-extraction artefact. The fix is post hoc, labelled, and changes no prediction.
- The P2 scan uses keywords. A reviewer should read Zeng's Results and Methods on positive-selection scenarios (Supplementary simulations) to confirm that no data-based beneficial mean is given there.

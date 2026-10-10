# R4 F3a: Day's s = 0.001 "from Zeng et al. 2021": quotes, fidelity, latency arithmetic, materiality

**Status: reviewed (combined, low-stakes tier, at 2c48e3d: 0 MAJOR, 6 MINOR); fix pass done (see "Review resolution"); awaiting integration.** The para-15 sentence is tagged dialectic (rule RH): it makes a numeric claim and an attribution.

## Files
- Script `research/checks/f3a_zeng_s_small_checks.py`, pre-registered at **f9c8ed9** (P1-P6). The first run, local, 2026-10-10, < 1 s, is in `results/raw/f3a.out`. **Post hoc** commit e9d2284 adds a `--posthoc` flag that strips C0 control characters (tab, LF, CR kept) before matching; its run is in `results/raw/f3a_posthoc.out`. The strip is global: it applies to Day's text as well as Zeng's (Day's quote matched exactly in both runs, so no false match arose). No prediction was changed. The first-run file `f3a.out` is the pre-registered result.
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
- **Internal: holds.** Day's arithmetic is correct (19,807), and "faster than 4N_e" follows at the N_e he uses elsewhere for this latency (1e4). The sentence would fail at his own Z18525547 human N_e of 3,300. That input is not used in this passage, so under rule S/C this is noted, not scored, and integration must not carry it into the verdict (it mixes inputs from two Day texts).
- **Fidelity: misread** (unchanged, re-confirmed from the raw text). Zeng's ~0.001 is a mean |s| for trait variants under negative selection. Zeng reports no measured beneficial mean. Fidelity is about the label ("empirical mean for beneficial mutations"); whether the magnitude is a fair stand-in is the R1 question below, and that is undetermined.
- **External: contested** (unchanged). R1 materiality is **undetermined**: the latency moves by more than 25% for any s outside 0.0008-0.00133, but the repo holds no sourced human beneficial mean s to put in its place. The steady-state rate does not depend on latency (F1), so the misread reaches only latency-based arguments (F, D9, E2). It does not reach the throughput leg (MITTENS uses the LTEE rate).

## Who this helps
- **Day side:** his formula arithmetic is exact. Zeng does estimate a mean |s| of about 0.001 (0.0007 extrapolated) for trait-affecting variants, and selection on a trait acts on its alleles in both directions, so 0.001 is defensible as an order-of-magnitude scale; the misread attaches to the label. His para-15 rebuttal to McCarthy holds on its own terms: PZ's latency uses the beneficial formula, and that formula is faster than 4N_e at N_e = 1e4. Even reading Zeng as Day does, the category means (0.0005-0.0010) leave the "faster" sentence true, though only marginally at 0.0005. The misread does not touch MITTENS's throughput figure.
- **Critic side:** the attribution is a misread, and the sign matters, not only the label: Zeng's s is |s| under purifying selection (Z3, "we only detected signatures of negative selection in real traits"), and coefficients of deleterious variants do not measure adaptive ones. The formula overstates the stochastic fixation time 2.3x (B0.4). The latency does not cap the rate (F1). At Day's own human N_e = 3,300 (Z18525547) the beneficial formula is slower than 4N_e, so the "faster" sentence depends on which of Day's N_e values is used.
- **Both:** the number that would settle this, a sourced distribution of beneficial s for the human lineage, is missing on both sides (RG / H follow-ups, QUEUE item 8).

## Limits
- P1 failed as pre-registered on a PDF-extraction artefact. The fix is post hoc, labelled, and changes no prediction.
- The P2 scan uses keywords and flags only sentences with a positive mention and no negative one; a sentence mentioning both with a number would pass unflagged. The combined review grepped all eight positive/beneficial mentions in the raw text: all concern simulation scenarios or speculation (e.g. "To incorporate positive selection, we specified two more input parameters"), none gives a measured value. This is a line-level grep, not a reading of Zeng's Methods and Supplementary simulations; that reading remains open but cannot change P2 unless a measured beneficial mean appears there.
- Of the six numeric-s sentences, only two carry an explicit negative-selection flag in the sentence (Z3's and the median-S sentence); the rest rely on the paper's framing. Keep this caveat in the integrated claim text.

## Review resolution
Combined review at 2c48e3d: 0 MAJOR, 6 MINOR, 4 NOTE. All MINORs answered; no verdict moves.

| Id | Resolution |
|---|---|
| MINOR-1 | **Accepted.** Files section says the post hoc strip is global (Day's text included; no false match) and the first-run file is the pre-registered result. |
| MINOR-2 | **Accepted.** Limits records the scan's `pos and not neg` blind spot and the review's grep of the eight positive/beneficial mentions (none measured); the full Methods read stays open, non-blocking. |
| MINOR-3 | **Accepted.** Limits carries the two-of-six explicit-flag caveat for integration. |
| MINOR-4 | **Accepted.** Fidelity is about the label, R1 about the number (undetermined); Day-side bullet credits 0.001 as a defensible order-of-magnitude scale. |
| MINOR-5 | **Accepted.** Internal verdict text says the N_e = 3,300 failure mixes two texts and must not enter the verdict at integration. |
| MINOR-6 | **Accepted.** Critic bullet leads with the attribution and the sign (|s| under purifying selection) before the arithmetic. |

**Final proposed verdicts (unchanged):** internal `holds`; fidelity `misread`; external `contested` (R1 materiality undetermined pending a sourced beneficial-s distribution).

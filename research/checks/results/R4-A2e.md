# R4 A2e: transferring the LTEE fixation rate to humans (sensitivity analysis)

**Status: run, written up, awaiting three reviews (Opus): correctness, steelman-day, steelman-critic.** Load-bearing tier (moves the A2e / ROOT-path nodes). Not yet reviewed or integrated; every number below is the author's first reading. All statements are dialectic (rule RH).

## Files
- Script `research/checks/a2e_ltee_transfer.py` (md5 `c9f2c48d2fbc367e3e502ac4a5618cbb`), pre-registered at **7593be2**; no later commit touched it. **Nothing in this run is post hoc.** The script was not edited after pre-registration.
- Run `main` (calib + human + analyse) on na-workhorse, launched 2026-10-09 22:24 -06:00, one process, ~1.0 h calibration + ~3 min human stage. Raw: `results/raw/a2e_calib.jsonl`, `a2e_human.jsonl`, `a2e_main.out` (all tables), `a2e_main.host`.
- Claim file: `docs/research/claims/A2e-ltee-as-ceiling.md`. Transfer factor F = k_human / (1/G_f) per generation; A2e holds iff F <= 1.

## Headline
1. **Per generation, A2e fails once the mutation supply is scaled at all.** With no scaling (kappa = 1) F <= 0.104 in every recombination mode (Day holds). With Hossjer's mutation-rate-only scaling (kappa = 125) F is 0.04-13 depending on s and the recombination mode (below 1 at s >= 0.01 central). With Day's own supply figures (kappa = 93,659) F = 7-8,970 (recombining 27-8,970 at central calibration), every cell > 1.
2. **The flip kappa\* (F = 1) is 3.9-13,100 over the whole grid; central 217**, always below 93,659. A2e's truth is therefore decided by one input: whether supply per genome scales from LTEE to human, and by how much.
3. **Per year the LTEE is a ceiling** under the recombining model (F_yr <= 0.50 even at the W&B asymptote), conceding the Day-side point and the A2i units point. The neutral-inclusive total (38.4 x 1,322) gives F_yr 0.72-1.05, borderline.
4. The "1.5-172x" clonal-interference range of R4-F2-A is reproduced and exceeded (1.09x to 343x here), driven by s, not by LTEE N_e.

## Results against the pre-registered predictions

| Pred | Registered | Observed | Verdict |
|---|---|---|---|
| Day | F <= 1 for every plausible combination (per generation) | F > 1 for every kappa >= 652 recombining cell at s = 0.003, every kappa >= 10,000 cell, and all kappa = 93,659 cells; F <= 1 only for kappa <= 125 at s >= 0.01 or kappa = 1 | **Not met** (holds only for unscaled or weakly scaled supply) |
| Critics | F > 1 whenever humans recombine and kappa >= 125 | At kappa = 125, F > 1 only at s = 0.003 (4.3-13); at s = 0.01 F = 0.19-0.58 and at s = 0.03 F = 0.04-0.11 | **Partly met**: true at kappa >= 652 for s = 0.003, kappa >= ~1,000 for s = 0.03 (see P3); false at 125 for s >= 0.01. The "kappa >= 125" threshold was too low. |
| P1a | 1/R_int spans >= 20x across s (fixed N_e, G_f) | 107x (central N_e 3.3e7, G 1,322: 165.7 / 1.55) | **Met** |
| P1b | LTEE N_e (3.3e6-1e8) moves 1/R_int <= 3x | 2.81x at s = 0.01; **8.07x at s = 0.003**, 1.15x at s = 0.03 | **Met at s = 0.01 only; missed at s = 0.003** (the prediction did not state s) |
| P1c | G_f target (1,322 / 1,587 / 2,890) moves it <= 2x | 4.02x at central (7.49 vs 1.87); 4.1-10x at s = 0.003 | **Missed** |
| P2a | kappa dominant; F ~ proportional below the asymptote; 4-5 orders | 4.96 decades; at s = 0.01, N_e,h 1e4 map 36.8: kappa 1 -> 125 gives 0.0046 -> 0.576 (125x) | **Met** |
| P2b | recombination mode >= 10x at kappa = 93,659 (clonal vs map 36.8) | 27x central (15.5 vs 419); 5.8-40x elsewhere | **Met** |
| P2c | s moves F 10-100x | 79x (6,650 / 83.7) | **Met** |
| P2d | N_e,human ~3x | 2.97x | **Met** |
| P2e | N_e,LTEE and G_f each <= 3x | 9.6x (0.98 decades) and 4.0x (0.61 decades) | **Missed** |
| P2f | Ranking kappa > rec > s > N_e,h > N_e,LTEE, G | Observed kappa 4.96 > **s 1.90 > rec 1.44 > N_e,LTEE 0.98 > G 0.61 > N_e,h 0.47** | **Ranking missed** (s and recombination swapped; N_e,LTEE and G_f above N_e,human) |
| P3 | kappa\* ~10 / ~200 / ~1,000 for s = 0.003 / 0.01 / 0.03, all in [5, 3000] | 9.63 / 217 / 1,110 (central) | **Met** |
| P3b | N_e,human = 3,300 raises kappa\* ~3x | 3.03x (658 vs 217) | **Met** |
| P3c | kappa = 125 sits near the flip at s = 0.01 | F = 0.576 (map 36.8, N_e,h 1e4), 0.19 (3,300) | **Met** (below the flip by 1.7-5x) |
| P4a | kappa = 93,659, map 36.8: F in [50, 5,000] for every s, N_e,LTEE, G_f | Direction met (all > 1). Range missed: central-calibration cells run 27.8 (s = 0.03, N_e,h 3,300) to 6,650 (s = 0.003, N_e,h 1e4); wider across N_e,LTEE and G_f | **Direction met, range missed** |
| P4b | Clonal humans at 93,659: F in [1, 100] | 7.3-167 (s = 0.003 gives 156 and 167) | **Direction met, upper bound missed** at s = 0.003 |
| P4c | kappa = 1: F < 1 in every mode | max 0.104 | **Met** |
| P5a | Per-year recombining F_yr < 1 for kappa <= 93,659 | max 0.416 (20 y); W&B bound 0.501 (24,300 / 48,500) | **Met** |
| P5b | Neutral-inclusive total F_yr 0.72-1.05 | 1.047 / 0.837 / 0.722 at 20 / 25 / 29 y | **Met** |
| P6a | Day's caps 1/300, 1/667, 1/39 give F 4.4 / 2.0 / 34 (G 1,322) | 4.41 / 1.98 / 33.9 | **Met** |
| P6b | Mean-field cap falls below 1/1,322 only for R_h < ~1.017 | flip R_h\* 1.0166 (N_e,h 1e4), 1.0149 (3,300) | **Met** |

Tally of the 19 itemised rows: met 13; missed or partly met 6 (P1b, P1c, P2e, P2f, P4a, P4b). Headline predictions: Day not met, critics partly met.

## Calibration and tolerance notes (for reviewers)
- Calibrated G_f from the evaluation reps deviates from target by up to 12% (1,451 vs 1,322 at N_e 1e7, s = 0.03; 2,537 vs 2,890 at N_e 3.3e7, s = 0.03; 1,241 vs 1,322 at 1e8). The F tables use the target G_f, not G_eval. The deviations are small against the 10^1-10^5 spreads but are not zero.
- The human clonal stage was run only at the central LTEE calibration (3.3e7, G 1,322) and 3 reps of T = 60,000; at s = 0.01 and 0.03 the lowest kappa cells returned k = 0 (no fixation observed; resolution floor ~ 1/(3 x 45,000) per generation), so F = 0 there means "below detection", not zero. Other calibrations use the closed-form W&B route.
- kappa = 81,500 clonal cells are the 93,659 run reprinted in parentheses (not separately simulated).
- map 1.5 M, map 36.8 M and free give identical F at kappa <= 652 (W&B Eq. 8 is at its free-recombination limit there); they separate only at kappa >= 10,000.

## Flags for reviewers (author-identified weak points)
1. **Same beneficial fraction in both systems.** kappa scales U_b per haploid genome by genome length and mutation rate only. If the fraction of new mutations that are beneficial at effect s in human DNA is lower than in E. coli (Day's argument that most human sites are conserved or neutral cuts it; a critic would point at regulatory and polygenic variation), kappa is multiplied by that fraction. The flip kappa\* then reads as a bound on (supply ratio x beneficial-fraction ratio). The sweep of kappa to 93,659 does not cover a fraction of 1e-3 against the LTEE value, which would put the effective kappa near 100 and the verdict at the flip. This is the main interpretive risk.
2. **LTEE N_e = 3.3e7 is unsourced** (N0 log2(100); `parameters.yaml` ltee.Ne_effective). It was swept (3.3e6-1e8) and moves the central F by about 1 decade (0.98), but kappa\* shifts by the same factor, e.g. 217 (central) vs 434 at 1e8. The calibrated U_b,LTEE is the quantity that carries it.
3. **G_f = 2,890 is derived** here as 1/(1/1,322 - 4.1e-4), subtracting Day's own neutral expectation of 4.1e-4 per genome per generation. It is an adaptive-only reading, not a number Day states; R4-F2-A notes the conflation. It lowers F by 4.0x at central s and kappa\* rises accordingly (e.g. 217 -> 900 at s = 0.01, N_e,h 1e4).
4. The model is a single-s clonal class process; humans in the "clonal" mode use M = 2 N_e,human haploid copies, and the recombining modes use W&B Eq. 1 / Eq. 8 as an analytic factor on the calibrated supply, not an individual-based simulation of recombining humans.
5. "Free" and "map" recombination bound the benefit but say nothing about linkage structure, background selection or the many-sites-per-locus regime.

## Who this helps
- **Day (A2e).** Per year, the LTEE is a ceiling in every recombining cell (F_yr <= 0.50), and with no supply scaling the LTEE rate exceeds the human rate by 10-3,000x. His cost-of-selection point holds in the sense that the mean-field cap (ln R_h / D_h) drops below the LTEE rate only for R_h < ~1.017, so cost does not rescue the ceiling reading, but his own Haldane figure (1/300) is itself above the LTEE rate (F cap 4.4). The result also shows that the LTEE number is a bound only under his "no scaling" use of G_f; the analysis confirms his insistence that the 1/B1 high-interference story does not by itself license a higher human rate (the effect of interference is carried by s, not by LTEE N_e).
- **Critics (A5a, A5f, A2i).** Per generation, F > 1 once supply scaling exceeds kappa\* (central 217, range 3.9-13,100), always below Day's own 93,659, so using the LTEE rate as a ceiling on humans is not supported on Day's own supply figures; recombination alone (kappa = 1) does not break it, but recombination plus mutation-rate scaling does at s = 0.003. A5a (Hossjer) is partly supported: kappa = 125 sits below the flip at s >= 0.01 (F 0.04-0.58). A2i's units point (per-year speed is conceded) is correct and is what rescues the per-year ceiling; the critic claim that clonal interference in the LTEE inflates 1/G_f is supported (1/R_int 1.09-343x), but it is carried by s.
- **This audit.** The claim is not true or false; it is a threshold in kappa x beneficial-fraction, and the result locates that threshold. Pre-registered quantities that fit: kappa\*, units, caps, N_e,human; that missed: the sensitivity ranking and the N_e,LTEE and G_f effects, both larger than predicted.

## Verdict suggestion (for the reviewers to test, not a verdict)
External for A2e per generation: `contested` leaning `contradicted` on Day's own supply figures; `supported` per year and under no supply scaling. The internal non-sequitur verdict is untouched (it rests on the paper's text).

## Review resolution
(To be filled after the three Opus reviews.)

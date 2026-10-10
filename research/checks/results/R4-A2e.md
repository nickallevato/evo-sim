# R4 A2e: transferring the LTEE fixation rate to humans (sensitivity analysis)

**Status: run, written up, three reviews done (2935b8f; 0 BLOCKER, 9 MAJOR), fix pass done (this revision; see "Review resolution"). Awaiting integration.** Load-bearing tier (moves the A2e / ROOT-path nodes). Text corrected per the reviews; every number added after the reviews is **post hoc** and marked "(post hoc)", from `a2e_posthoc.py`. Rule RH: the A2e Statement is split. "unattainable ceiling, the absolute best-case scenario" is dialectic and is what is scored; "the performance of a Formula One car used to benchmark a horse-drawn cart" is an analogy (rhetoric), not literal-fact-checked (Rhetoric-ledger entry at integration; counter in "Review resolution").

## Files
- Script `research/checks/a2e_ltee_transfer.py` (md5 `c9f2c48d2fbc367e3e502ac4a5618cbb`), pre-registered at **7593be2**; no later commit touched it. **Nothing in this run is post hoc.** The script was not edited after pre-registration.
- Run `main` (calib + human + analyse) on na-workhorse, launched 2026-10-09 22:24 -06:00, one process, ~1.0 h calibration + ~3 min human stage. Raw: `results/raw/a2e_calib.jsonl`, `a2e_human.jsonl`, `a2e_main.out` (all tables), `a2e_main.host`.
- **Post hoc, after reviews 2935b8f:** `research/checks/a2e_posthoc.py` (md5 `3d17c6375a5b7ee53529568faa2f5961`), analysis only on the stored calibrations (closed forms; no new simulation; run locally, < 5 s). Raw: `results/raw/a2e_posthoc.out` (sections PH1-PH11, cited below as PHn).
- Claim file: `docs/research/claims/A2e-ltee-as-ceiling.md`. Transfer factor F = k_human / (1/G_f) per generation; A2e holds iff F <= 1.

## Headline
Day states the comparison **per generation** ("The objection implicitly claims that humans can fix mutations faster per generation than bacteria under ideal conditions", Z23003785 s8.6 p.15; MITTENS uses it per generation, s7.3 p.13). Everything below is per generation unless marked. All F > 1 results are **predictions of a supply-limited model** (clonal class process + W&B, U_b scaled by kappa), not observations of a human rate.

1. **Adaptive-only model, uncapped.** With no supply scaling (kappa = 1) F <= 0.104 in every recombination mode: Day holds. With Hössjer's mutation-rate-only scaling (kappa = 125) F = 0.04-13; below 1 at s >= 0.01, above 1 at s = 0.003. At kappa = 93,659, **the ratio derived from Day's stated factors** (4.1e-4 per LTEE genome, s4.3 p.7; 3.2e9 x 1.2e-8 = 38.4 per haploid human genome, s6.4 p.11 without its x100; the ratio KITTENS uses; Day himself does not apply supply scaling), uncapped F = 7.3-8,970, every cell > 1, **even with humans treated as clonal** (F 7.3-167).
2. **Capped by Day's own cost figures** (post hoc PH6), F at kappa = 93,659 is 1.98 (Haldane + d, 1/667), 4.41 (Haldane, 1/300), 6.4-7.1 (mean-field ln R_h / D_h at R_h 1.111) and up to 33.9 (Term 3, 1/39). So F > 1 even under Day's caps, but **by about 2-7x, not hundreds**. Caps never move kappa\* (all caps exceed 1/1,322).
3. **The flip kappa\* (F = 1) is not set by supply alone.** On the coupled grid (same s in both systems) kappa\* is 3.9-13,050; central 217, all below 93,659. The upper corner (13,050) needs the audit-derived G 2,887 and N_h 3,300; with Day's G targets only (1,322 / 1,587) the range is 3.9-8,620 (PH5). It is a threshold on **(supply ratio) x (beneficial-fraction ratio) x (effect-size ratio)**: closed form kappa\* ≈ (M_LTEE / 2N_h) · R_int,LTEE · (u_L / u_h), 220 vs 217 at central (PH1). The margin to 93,659 is 430x at central and 7.2x at the most Day-favourable corner (10.9x with Day's G targets). If the human beneficial effect is smaller than the LTEE's (Day: "the remaining beneficial mutations have smaller effects", s4.2 p.7), kappa\* rises: s_L 0.03 with s_h 0.001 gives 32,260 at central (post hoc PH2); 6 of the reviewers' 96 decoupled cells, and 2 of 144 on a wider G 1,322 grid, put kappa\* above 93,659. kappa\* is the same for map 1.5 M, map 36.8 M and free recombination (the flip lies in the independent-sites regime), so it does not depend on the human recombination model.
4. **Total-throughput basis.** Day: "MITTENS measures total throughput" (s4.3 p.7). Like for like, the human total substitution rate k = μ = 38.4 per haploid genome per generation against 1/1,322 gives **F = 50,765 per generation** (60,941 at 1,587; pre-registered in P5, previously reported only per year). This route needs no kappa, beneficial fraction, s or recombination model; it depends only on whether the human neutral substitution rate is k = μ (A5c, B5g; Day's s8.2 drift-time counter is a separate node).
5. **Per year (context, not a test of A2e).** Under the recombining model F_yr <= 0.50 (W&B asymptote), and the total-throughput F_yr is 0.72-1.05. This explains why bacteria look fast per unit time, which is A2i's units point (Matev); it does not bear on A2e as Day states it (per generation).
6. The "1.5-172x" clonal-interference range of R4-F2-A is reproduced and exceeded (1.09x to 343x here), driven by s, not by LTEE N_e.

## Results against the pre-registered predictions

| Pred | Registered | Observed | Verdict |
|---|---|---|---|
| Day | F <= 1 for every plausible combination (per generation) | F > 1 for every recombining cell at kappa >= 125 at s = 0.003 (4.3-13 at 125); at the central calibration every cell at kappa >= 10,000 (over the full grid kappa\* reaches 13,050, so not every 10,000 cell elsewhere); all kappa = 93,659 cells; F <= 1 at kappa = 1, and at kappa = 125 for s >= 0.01 (corrected after review m4) | **Not met** (holds only for unscaled or weakly scaled supply) |
| Critics | F > 1 whenever humans recombine and kappa >= 125 | At kappa = 125, F > 1 only at s = 0.003 (4.3-13); at s = 0.01 F = 0.19-0.58 and at s = 0.03 F = 0.04-0.11 | **Partly met**: at the central calibration true at kappa >= 125 for s = 0.003, >= ~660 for s = 0.01 (F 0.99 at 652 with N_h 3,300; 3.0 with 1e4), >= 1,110-3,350 for s = 0.03 (corrected after review m4); false at 125 for s >= 0.01. The "kappa >= 125" threshold was too low. |
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
- The human clonal stage was run only at the central LTEE calibration (3.3e7, G 1,322) and 3 reps of T = 60,000; at s = 0.01 and 0.03 the lowest kappa cells returned k = 0 (no fixation observed; resolution floor 1/(3 x 60,000) = 5.6e-6 per generation, corrected after review m5: T = 60,000 is the measuring window after the 15,000 burn-in), so F = 0 there means "below detection", not zero. Stored k values are integer multiples of the floor; 8 clonal cells have <= 5 events and are **noise-dominated** (all at kappa <= 125; PH10). Some low-kappa clonal cells exceed the independent-sites ceiling (e.g. s 0.01, N_h 1e4, kappa 1: F 0.0147 vs 0.0046, 2 events), which is impossible in expectation and is noise. No verdict uses a cell with <= 5 events. Other calibrations use the closed-form W&B route.
- kappa = 81,500 clonal cells are the 93,659 run reprinted in parentheses (not separately simulated).
- map 1.5 M, map 36.8 M and free give identical F at kappa <= 652 (W&B Eq. 8 is at its free-recombination limit there); they separate only at kappa >= 10,000.

## Flags (author-identified weak points; revised after reviews)
1. **Same beneficial fraction and the same s in both systems.** kappa scales U_b per haploid genome by genome length and mutation rate only. The per-generation adaptive verdict is a threshold on (supply ratio) x (beneficial-fraction ratio) x (effect-size ratio). The unmeasured factors cut both ways:
   - *Towards Day* (fewer beneficial mutations per new human mutation, or smaller effects): most human DNA is not under selection, while the E. coli genome is mostly coding; the LTEE starts maladapted in a novel medium, where Fisher's geometric model puts the beneficial fraction highest; Day's s4.2 p.7 "the remaining beneficial mutations have smaller effects"; the LTEE rate itself slows (s4.2: 794 gen/fix in the first 10,000 generations, 1,163 in the last 10,000), so calibrating U_b,LTEE to the 60K average carries early-phase supply into a long-adapted lineage. A combined factor of >= 430 at central (>= 7.2 at the most Day-favourable corner; >= 10.9 with Day's G targets) restores the ceiling.
   - *Towards the critics*: the LTEE is one constant environment with a depleting target set (Day's own "The rate is slowing"); human adaptation also draws on standing variation, polygenic and regulatory change, and changing environments, none of which the class process or W&B model includes; a larger human N_e (Day's in-paper 3.3e4, or towards the ancestral human-chimp 1.3e5-2.0e5 in `parameters.yaml`) lowers kappa\* (65.8 at 3.3e4, 21.7 at 1e5; PH3).
   - *Testable form* (critic review C3; post hoc PH8): at the flip the human adaptive rate equals 1/1,322 per generation, i.e. about 191 adaptive substitutions per lineage over 252,000 generations (Day's own "191 achievable", s7.3 p.13). So A2e per generation, adaptive-only, is equivalent to "the human lineage fixed <= ~191 adaptive substitutions since the CHLCA". The absolute threshold is U_b,human ≈ 1.9e-6 per haploid genome per generation at s = 0.01, N_h 1e4 (6.3e-6 at s 0.003; 6.5e-7 at s 0.03). Published adaptive-substitution estimates for the human lineage (McDonald-Kreitman-type alpha) bear on this directly. **None is fetched or stated here; open item** (source pipeline, refresh, verbatim quotes).
2. **LTEE N_e ≈ 3e7 is Day-stated** ("In the LTEE, with Ne ≈ 3 × 10⁷, the expected time ...", s8.2 p.14; also p.4 list), with no primary-literature source yet (`parameters.yaml` ltee.Ne_effective note to be updated at integration). It was swept (3.3e6-1e8) and moves the central F by about 1 decade (0.98); kappa\* shifts by the same factor (217 central, 434 at 1e8, the Day-favourable end). The calibrated U_b,LTEE carries it.
3. **G_f targets.** 1,322 (verbatim) and 1,587 (2nd ed.) are Day's. **Day's own adaptive-only reading is 1,408**: "approximately 35.5 beneficial fixations, or 1,408 generations per beneficial fixation" (s4.3 p.7). The 2,890 of the pre-registration is exactly **2,887** = 1/(1/1,322 - 4.1e-4), the audit's cross-estimator construction (Day's neutral expectation subtracted from the metagenomic total), not Day's. It lowers F by 4.0x at central and raises kappa\* (217 -> 900 at s 0.01, N_h 1e4). G 1,408 (post hoc PH4, interpolated) gives kappa\* ≈ 240-260 at central s 0.01, N_h 1e4 (the 1,322-2,887 log-log interpolation under-reads the calibrated 1,587 check by ~16%, so the values are approximate; they lie inside the swept 217-362).
4. **Human N_e.** The pre-registered sweep used 3,300 (Day, Z19984826 s4.3; H8 notes it is not in its cited source) and 1e4 (textbook). In the source under test Day uses "The human Ne of 10,000–33,000" (s8.2 p.14), so Day's in-paper range is 1e4-3.3e4. The 3,300 / 1e4 sweep is the Day-favourable end; 3.3e4 and 1e5 are added post hoc (PH3).
5. The model is a single-s clonal class process; humans in the "clonal" mode use M = 2 N_e,human haploid copies, and the recombining modes use W&B Eq. 1 / Eq. 8 as an analytic factor on the calibrated supply, not an individual-based simulation of recombining humans. W&B credits recombination's benefit but not its costs (twofold cost of sex, recombination and segregation load, mate finding; Day lists "no recombination overhead" as an LTEE advantage, p.4). Because the flip lies in the independent-sites regime and clonal humans also give F 7.3-167 at kappa = 93,659, these costs would not move kappa\*.
6. "Free" and "map" recombination bound the benefit but say nothing about linkage structure, background selection or the many-sites-per-locus regime.
7. **Model vs observation.** Day's ceiling is an empirical fixation rate: "I didn't cite the E. coli study for its mutation rate but for its fixation rate" (A5g). F > 1 here is a model prediction. Day also offers an independent human-only rate (about 1 per 27,600 generations, s8.6 p.15; node A5e). The external verdict below is therefore conditional on the supply-limited model (a contested premise, so it is scored external, not internal).

## Post hoc analysis (after reviews 2935b8f; `a2e_posthoc.py`, analysis only)
| Item | Result | Source |
|---|---|---|
| Closed form for kappa\* | (M_L / 2N_h) R_int (u_L/u_h): 220 vs 217 (s 0.01), 9.96 vs 9.63 (0.003), 1,067 vs 1,107 (0.03) at N_h 1e4; free = map | PH1 |
| Decoupled s, central (N_e,L 3.3e7, G 1,322, N_h 1e4) | s_L 0.01 / s_h 0.003: 719; s_L 0.03 / s_h 0.003: 10,770; s_L 0.03 / s_h 0.001: 32,260 (N_h 3,300: 97,740) | PH2 |
| Decoupled s, reviewers' 96-cell grid | 6 cells kappa\* > 93,659 (97,700-380,000); all s_L 0.03, N_e,L >= 3.3e7; 5 of 6 N_h 3,300; 4 of 6 G 2,887. A stack of Day-favourable choices (LTEE effects 10-30x human) | PH2 |
| Decoupled s, G 1,322 only, s_h <= s_L, N_h 3.3e3-1e5 | 2 / 144 cells above 93,659 (both s_L 0.03, s_h 0.001, N_h 3,300) | PH2 |
| Human N_e 3.3e4 / 1e5 (coupled) | kappa\* central s 0.01: 65.8 / 21.7; all calibrations 1.2-1,305 / 0.39-431; F(93,659) 1,296 / 3,359 | PH3 |
| G 1,408 (interpolated) | kappa\* ≈ 244 (1,322-2,887 interp.) / 259 (1,322-1,587 piecewise) at central; F(93,659) 375 | PH4 |
| Coupled kappa\* range, corners | 3.86 (N_e,L 3.3e6, s 0.003, G 1,322, N_h 1e4) to 13,050 (N_e,L 1e8, s 0.03, G 2,887, N_h 3,300); Day's G only: to 8,624 | PH5 |
| Capped F at 93,659 | 1.98 / 4.41 / 6.4-7.1 / 27.8-33.9 (Haldane + d / Haldane / mean-field 1.111 / Term 3) in every s and N_h cell; G 1,408: 2.11 / 4.69 / -/ 36.1 | PH6 |
| Total-substitution F | 50,765 per generation (G 1,322), 60,941 (1,587); per year 0.72-1.05 (1,322), 0.87-1.26 (1,587) | PH7 |
| Population supply per generation | humans 2N_h x 38.4 = 768,000 (N_h 1e4) vs LTEE 3.3e7 x 4.1e-4 = 13,530: 57x (19x at N_h 3,300; 6.2x at the most LTEE-favourable corner N_h 3,300 / N_e,L 1e8) | PH9 |

## Who this helps
- **Day (A2e).**
  - With no supply scaling the LTEE rate is a ceiling in every recombination mode (F <= 0.104). With Hössjer's mutation-rate-only scaling it still holds at s >= 0.01 (F 0.04-0.58).
  - The critics' registered threshold ("F > 1 whenever humans recombine and kappa >= 125") was wrong at s >= 0.01, and recombination alone (kappa = 1) does not break the ceiling.
  - On the adaptive-only model the per-generation verdict turns on an unmeasured ratio: a beneficial-fraction x effect-size factor of 430 at central (7.2 at one corner) restores the ceiling, and his s4.2 point (later beneficial mutations have smaller effects) moves kappa\* in his direction (to 32,260 at central with s_h 0.001; above 93,659 in 2-6 corner cells).
  - Under his own cost caps the per-generation exceedance is about 2-7x, not hundreds (Term 3 up to 34).
  - F > 1 is a model prediction, not an observed human rate (A5g; A5e carries his human-derived rate).
  - The LTEE N_e of 3e7 is his own stated value; the sweep includes the Day-favourable 1e8.
- **Critics (A5a, A5c, A5f, A2i).**
  - The flip (central 217; 3.9-8,620 on Day's G targets) lies below the supply ratio derived from Day's stated factors (93,659) on every coupled cell, does not depend on the human recombination model, and humans exceed the LTEE rate **even when treated as clonal** (F 7.3-167).
  - Day's own cost caps all allow F > 1 (1.98-33.9), so cost does not restore the ceiling; whether Haldane's limit binds is itself contested (Nunney 2003, soft selection; A5a, H2).
  - On Day's stated total-throughput basis (s4.3 p.7) F = 50,765 per generation, with no appeal to kappa (Hancock's A5c argument on Day's numbers), conditional only on the human neutral rate k = μ.
  - On the figures derived from Day's stated factors the human population receives 19-57x more new mutations per generation than the LTEE, which contradicts "effectively unlimited mutation supply" as an LTEE advantage (p.4).
  - Day's in-paper human N_e (1e4-3.3e4) lowers kappa\* (65.8 at 3.3e4).
  - The adaptive-only uncertainty is reducible by data (<= ~191 adaptive substitutions per lineage; open item).
  - A2i (Matev) is supported on units: per year the LTEE is fast (F_yr <= 0.50), and that is the reason bacteria look like a "Formula One car", not a per-generation ceiling.
  - The R4-F2-A interference factor is carried by s (1/R_int 1.09-343x).
- **This audit.** The adaptive-only claim is a threshold on supply x fraction x effect, and the result locates it; the total-throughput route moves the question to A5c. Pre-registered quantities that fit: kappa\*, caps, units, N_e,human; that missed: the sensitivity ranking and the N_e,LTEE and G_f effects (both larger than predicted). The reviews corrected the scope of the per-year reading (it belongs to A2i, not A2e) and two attributions (93,659 and 2,887 are derived, not Day's figures).

## Verdict suggestion (revised after reviews; for integration, not final)
- **Internal:** unchanged (non-sequitur, from the paper's text), strengthened by the population-supply point (PH9: on numbers derived from Day's stated factors the "effectively unlimited mutation supply" is on the human side).
- **External, per generation: `contested`**, with two stated dependencies:
  - *Adaptive-only, supply-limited model:* the flip lies 7-430x below the derived supply ratio on the coupled grid (11-430x on Day's G targets) and is independent of the recombination model, but the margin can be closed by an unmeasured beneficial-fraction or effect-size ratio (2/144 to 6/96 decoupled cells already close it). Leans against A2e; reducible by human adaptive-substitution data (open item). Conditional on the supply-limited model (A5g; A5e carries Day's human-derived rate).
  - *Total throughput (Day's stated basis):* F = 50,765. This becomes `contradicted` if the human neutral substitution rate is k = μ (A5c, B5g); Day's s8.2 drift-time counter is a separate node and is not scored here.
- **Per year:** no A2e verdict (out of scope under rule S); the result supports A2i (external `supported` on units).

## Open items
1. **Adaptive-substitution literature (critic review C3):** fetch McDonald-Kreitman / alpha estimates of adaptive substitutions in the human lineage through the source pipeline (refresh, verbatim quotes, locators), and compare with the ~191 per lineage equivalent of F = 1. Not fetched here.
2. A calibrated (not interpolated) G 1,408 run is optional (one combo, about 2.5 min on na-workhorse); the interpolation brackets it inside 217-362.
3. Integration: Q ids for the s4.2, s4.3, s6.4, s7.3, s8.2, s8.6 passages and both A2e quotes (m8); `parameters.yaml` entries for 4.1e-4, 38.4, the kappa set, 2,887, 1,408, 6.64 gen/day, 20-29 y/gen, map 36.8 M, and the ltee.Ne_effective note (m2, m9); Rhetoric-ledger entry for the Formula One analogy (m7, D6, N1).

## Review resolution
Reviews: correctness (C), steelman-day (D), steelman-critic (K) at 2935b8f. All post hoc numbers from `a2e_posthoc.py` / `raw/a2e_posthoc.out`.

| Id | Sev | Resolution |
|---|---|---|
| C-M1 | MAJOR | **Accepted.** "Decided by one input" removed. Headline 3 now states the threshold as supply x beneficial-fraction x effect-size, gives the closed form (PH1, 220 vs 217) and the decoupled-s results (PH2: 32,260 at central with s_h 0.001; 6/96 reviewer cells and 2/144 at G 1,322 above 93,659). The total-throughput route (no kappa) is headline 4. |
| C-M2 | MAJOR | **Accepted.** Per-year reading moved to headline 5 as context; "`supported` per year" dropped from the A2e verdict; credited to A2i. |
| C-M3 | MAJOR | **Accepted.** 93,659 relabelled everywhere as "derived from Day's stated factors (s4.3 p.7; s6.4 p.11 without the x100), the ratio KITTENS uses; Day does not apply supply scaling" (A5g). The haploid 38.4 (rule C) is kept. The pre-registered script docstring is not edited (it is pre-registration); this note supersedes its "Day's own supply figures" label. |
| C-m1 | MINOR | Accepted. Flag 3: 2,887 (not 2,890) is the audit's construction; 1,408 named as Day's adaptive reading; post hoc G 1,408 (PH4). |
| C-m2 | MINOR | Accepted. Flag 2: LTEE N_e 3e7 is Day-stated (s8.2 p.14), no primary source. `parameters.yaml` note at integration. |
| C-m3 | MINOR | Accepted. Flag 4; N_h 3.3e4 row added (PH3, kappa\* 65.8). |
| C-m4 | MINOR | Accepted. Day and Critics rows corrected (verdict cells unchanged). |
| C-m5 | MINOR | Accepted. Floor corrected to 1/(3 x 60,000); 8 cells with <= 5 events flagged as noise (PH10). |
| C-m6 | MINOR | Accepted. "Who this helps / Day" rewritten: cost caps all allow F > 1 (moved to the critics' bullet as a point against Day); the misattributed 1/B1 sentence deleted. |
| C-m7 | MINOR | Accepted. Statement split under RH in the status line; ledger entry at integration. |
| C-m8, C-m9 | MINOR | Accepted; deferred to integration (shared files out of scope for this pass). Listed in Open items 3. |
| D1 | MAJOR | **Accepted.** Flag 1 gives both directions and the factor needed (430 central, 7.2 corner, 10.9 on Day's G targets); decoupled-s table added (PH2); verdict is `contested`, not "leaning contradicted" (the lean is stated only with its condition). |
| D2 | MAJOR | **Accepted.** Headline 1 labelled uncapped; headline 2 gives capped F (1.98-7.1, Term 3 to 34) and states caps do not move kappa\*. Counterpoint kept: whether H binds is contested (Nunney 2003). |
| D3 | MAJOR | **Accepted.** Headline preamble and flag 7: F > 1 is a model prediction under a supply-limited model; the verdict is conditional on it; A5e cross-referenced. Not accepted in full: the check still tests A2e's stated per-generation comparison, which needs some model of the human rate; the total-throughput route (headline 4) uses no supply model. |
| D4 | MINOR | Accepted. Recombination costs listed in flag 5, with the honest note that they would not move kappa\*. |
| D5 | MINOR | Accepted. Diminishing returns listed as a Day-side factor in flag 1 (absorbed in the fraction/effect factor); no new calibration. |
| D6 | MINOR | Accepted (same as C-m7). |
| D7 | MINOR | Accepted. 3,300 labelled by source and H8 caveat; Day's in-paper 1e4-3.3e4 used as "Day" (flag 4). |
| K-C1 | MAJOR | **Accepted.** Per-generation total-throughput F = 50,765 (and 60,941 at 1,587) in headline 4 and the verdict, with its dependency on A5c / B5g stated. Not accepted: calling A2e `contradicted` now; that waits on the A5c node. |
| K-C2 | MAJOR | **Accepted** (same as C-M2). |
| K-C3 | MAJOR | **Accepted.** Flag 1 now gives both directions, the ~191-substitution equivalence and the U_b,human threshold (PH8). The literature test is an open item; no numbers stated because nothing was fetched. |
| K-C4 | MINOR | Accepted. N_h 3.3e4 and 1e5 (PH3). |
| K-C5 | MINOR | Accepted. Population supply 19-57x (PH9; 6.2x at the LTEE-favourable corner) in the critics' bullet and internal verdict note. |
| K-C6 | MINOR | Accepted. "Even with humans treated as clonal" in headline 1. |
| K-C7 | MINOR | Accepted. Capped values in the critics' bullet. |
| K-C8 | MINOR | Accepted. kappa\* range reported with labelled corners; upper end attributed to G 2,887 and N_h 3,300 (PH5). |
| NOTEs | - | C-N3 (kappa\* ≈ population ratio x R_int) added to headline 3. K-N1 rhetorical counter for the ledger: *"A Formula One car beats a cart per hour. MITTENS counts laps."* (true; aimed at the analogy's unit; turns the audience back to the per-generation arithmetic). Other NOTEs need no change. |

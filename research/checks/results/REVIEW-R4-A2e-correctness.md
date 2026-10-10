# Correctness review of R4-A2e (LTEE-to-human transfer sensitivity)

Reviewer: Opus 5.5 (correctness). Date: 2026-10-10. No repo file other than this one was edited; no run was launched. One trivial local recomputation (pure Python, <1 s, reads `raw/a2e_calib.jsonl` only) lives in the session scratchpad (`a2e_rev.py`).

Reviewed:
- `research/checks/results/R4-A2e.md`;
- `research/checks/a2e_ltee_transfer.py` (as pre-registered at 7593be2: docstring, engines, `F()`, `analyse()`);
- `results/raw/a2e_calib.jsonl`, `a2e_human.jsonl`, `a2e_main.out`, `a2e_main.host`;
- claim files A2e, A2i, A5a, A5c, A5f, A5g; `docs/research/parameters.yaml`;
- Day's text, read-only: `sources/raw/day/zenodo-23003785.txt`, at s2 p.2, s2 p.4, s4.2-4.3 p.7, s6.4 p.11, s7.3 p.13, s8.2 p.14 and s8.6 p.15;
- quote registries, grepped (`Q58`, `Q61`, `RE-02`, `HO-0x`, and the A2i quote at quotes-critics.md l.697).

Severity: BLOCKER = the result cannot stand. MAJOR = a stated conclusion or number overreaches and should change before adoption. MINOR = wording, bookkeeping or a missing caveat. NOTE = for the record, no change needed.

**Summary: 0 BLOCKER, 3 MAJOR, 10 MINOR, 7 NOTE.**
- Pre-registration is clean and nothing is post hoc.
- Every number I recomputed reproduces.
- The pre-registered predictions are scored honestly, and in places more strictly than the registered statistic needs.
- The problems are in what the headline and the verdict suggestion claim:
  - "one input decides A2e" is too strong (M1);
  - a per-year "supported" is outside the scope of what Day states (M2);
  - "Day's own supply figures" labels a ratio Day never forms (M3).

## 1. Findings

| # | Sev | Locator | Problem | Fix |
|---|---|---|---|---|
| M1 | MAJOR | Headline 2 ("A2e's truth is therefore decided by one input"); "This audit" bullet ("a threshold in kappa x beneficial-fraction") | **Supply is not the only input that can flip the verdict.** (a) *Effect size is coupled.* The same s is used for the LTEE calibration and for the human rate. At the flip the human rate is in the independent-sites regime (all three recombining modes give the same kappa\*, §4 of `a2e_main.out`). So kappa\* = 1/(G_f · 2N_h · U_b,LTEE(s_L) · u(N_h, s_h)), which is closed form. I decoupled s_L and s_h using the stored calibrations (scratch, `derived:`). Central N_e,LTEE 3.3e7, G 1,322, N_h 1e4: s_L 0.03 with s_h 0.003 gives kappa\* = 10,770; with s_h 0.001 it gives 32,250. Over the stored grid (4 N_e,LTEE x 3 s_L x 2 G x s_h {0.001, 0.003} x 2 N_h = 96 cells), **6 cells have kappa\* > 93,659** (97,700-380,000). All 6 have s_L = 0.03 and N_e,LTEE >= 3.3e7, and 5 of the 6 have N_h = 3,300. Day himself argues that later beneficial mutations "have smaller effects" (s4.2 p.7). (b) *The total-throughput route bypasses kappa.* On Day's stated basis (MITTENS "measures total throughput", s4.3 p.7), the neutral-inclusive comparison gives F = 38.4 x 1,322 = 50,765 per generation (docstring P5). It does not depend on kappa or on the beneficial fraction. It depends on the human neutral substitution rate (A5c). | Restate: the per-generation flip is a threshold on (supply ratio) x (beneficial-fraction ratio) x (effect-size ratio, about u(s_h)/u(s_L)). Give the closed form kappa\* ≈ (M_LTEE / 2N_h) · R_int,LTEE · (u_L/u_h): it gives 220 vs 217 at central. Add the decoupled-s table as a **proposed post hoc** analyse-only step (closed form on the stored calibrations; trivial). Report the per-generation neutral-inclusive F next to the adaptive F (see m10). |
| M2 | MAJOR | Headline 3; "Who this helps / Day" ("Per year, the LTEE is a ceiling"); Verdict suggestion ("`supported` per year") | **The per-year reading is not the Statement's basis (rule S).** Day states the comparison per generation. In s8.6 (p.15): "The objection implicitly claims that humans can fix mutations faster per generation than bacteria under ideal conditions." MITTENS applies the ceiling per generation (s7.3 p.13: "At 1,322 gen/fix (non-mutator): 191 achievable"). The per-year result (F_yr <= 0.50) is correct arithmetic. It explains *why* bacteria look fast, which is A2i's point. It is not a test of A2e as Day uses it. Rule C does not rescue it: a per-year ceiling cannot feed a per-generation count. | Drop "`supported` per year" from the A2e verdict suggestion. Keep §5 as context that credits A2i's units analysis. Say explicitly that it does not bear on A2e as stated. |
| M3 | MAJOR | Headline 1 ("With Day's own supply figures (kappa = 93,659)"); docstring INPUTS; Who this helps / Critics ("on Day's own supply figures") | **Day never states 38.4, and never forms or accepts a supply ratio.** (i) 4.1e-4 is verbatim (s4.3 p.7: "the ancestral mutation rate of 4.1 × 10⁻⁴ per genome per generation"). (ii) The human figure appears only in a supermutator hypothetical (s6.4 p.11): "approximately 38,400 mutations per individual per generation (3.2 × 10⁹ bp × 1.2 × 10⁻⁸ × 100)". The printed product is 10x too large (RE-02). 38.4 is the audit's evaluation of Day's two stated factors without the x100. (iii) Day rejects supply as the transfer variable: "I didn't cite the E. coli study for its mutation rate but for its fixation rate" (A5g). The ratio 93,659 is the one KITTENS uses (A5a note). Rule C: the haploid reading (38.4, not 76.8 per diploid individual) is the one charitable to Day, and it is the one used. | Relabel it everywhere: "kappa = 93,659, derived from Day's stated factors (s4.3 p.7; s6.4 p.11), the ratio KITTENS uses; Day does not apply supply scaling". The verdict suggestion's "on Day's own supply figures" becomes "on supply ratios derived from Day's stated factors". |
| m1 | MINOR | Flag 3; docstring INPUTS | **2,890 is 2,887**, since 1/(1/1,322 − 4.1e-4) = 2,886.6. The write-up says it is "not a number Day states" but omits that **Day does state an adaptive-only figure**: "approximately 35.5 beneficial fixations, or 1,408 generations per beneficial fixation" (s4.3 p.7; clone-pair 56.0 minus 20.5 hitchhikers at 50K). 2,887 subtracts Day's neutral expectation from the metagenomic 60K total, an estimator combination Day does not use. 1,408 lies inside the swept 1,322-1,587 (kappa\* 217 → 362). | In flag 3, name 1,408 as Day's own adaptive reading and 2,887 as the audit's cross-estimator alternative. Either drop 2,890 from "Day"-attributed ranges or label it. A G = 1,408 calibration is an optional post hoc (one combo, about 2.5 min on na-workhorse); interpolation suffices. |
| m2 | MINOR | Flag 2; docstring INPUTS ("UNSOURCED") | **LTEE N_e ≈ 3e7 is Day's own stated value**: "In the LTEE, with Ne ≈ 3 × 10⁷, the expected time ..." (s8.2 p.14). It still lacks a primary-literature source, but Day cannot contest it. | Reword flag 2 to "Day-stated (s8.2 p.14), no primary source yet". Update the `parameters.yaml` `ltee.Ne_effective` note accordingly (integration step, not here). |
| m3 | MINOR | Docstring INPUTS ("Human N_e: 3,300 (Day, Z19984826 s4.3)") | In this paper Day uses "The human Ne of 10,000–33,000" (s8.2 p.14). 33,000 is not swept. kappa\* at central with N_h = 3.3e4 is 65.8 (closed form, scratch). | State that the "Day" human N_e in the source under test is 1e4-3.3e4. Add 3.3e4 as a proposed post hoc closed-form row. |
| m4 | MINOR | Prediction table, Day row and Critics row | Wording errors against the raw tables. (a) Day row: "F > 1 for every kappa >= 652 recombining cell at s = 0.003". In fact F > 1 already at kappa = 125 (4.27-13). (b) "every kappa >= 10,000 cell" holds at the central calibration only. Over the full grid kappa\* reaches 13,100 (N_e,LTEE 1e8, s 0.03, G 2,890, N_h 3,300). (c) Critics row: "true at kappa >= 652 for s = 0.003, kappa >= ~1,000 for s = 0.03". The right thresholds (central calibration) are: >= 125 for s = 0.003; >= ~660 for s = 0.01 (F = 0.99 at 652 with N_h 3,300); >= 1,110-3,350 for s = 0.03. Neither verdict cell changes. | Correct the three statements. |
| m5 | MINOR | "Calibration and tolerance notes", bullet 2 | The resolution floor is stated as 1/(3 x 45,000). `stage_human` measures over T = 60,000 after a 15,000 burn-in, so the floor is 1/(3 x 60,000) = 5.6e-6. The stored k values are integer multiples of it: 1.111e-5 = 2 events, 1.667e-5 = 3, 2.778e-5 = 5. One clonal cell (s 0.01, N_h 1e4, kappa 1: F 0.0147) exceeds the independent-sites ceiling (0.0046), which is impossible in expectation and so is noise. | Fix the floor. Mark clonal cells with <= 5 events as noise-dominated. |
| m6 | MINOR | Who this helps / Day | (a) Self-contradictory: "His cost-of-selection point holds ... so cost does not rescue the ceiling reading". (b) "his insistence that the 1/B1 high-interference story ..." In A2i's notation B1 is years per generation, not interference, and the point is Matev's, not Day's. | Rewrite (a) as: "Day's own cost caps all allow F > 1 (1.98-33.9); cost does not restore the ceiling". Delete or reattribute (b). |
| m7 | MINOR | Status line ("All statements are dialectic (rule RH)") | Rule RH1 says to tag each clause. "unattainable ceiling, the absolute best-case scenario" is dialectic. "the performance of a Formula One car used to benchmark a horse-drawn cart" is an analogy, which is rhetoric, carrying that core. | Tag it split and add a Rhetoric ledger entry (see the critic and Day steelman reviews for a counter). |
| m8 | MINOR | Files / claim file | I verified both A2e quotes verbatim against raw text (`zenodo-23003785.txt` l.73-74 p.2, l.147-149 p.4). They have **no Q id** in `quotes-day.md`, and neither do the s4.3 (4.1e-4; 1,408), s8.2 (Ne ≈ 3 × 10⁷; human Ne 10,000–33,000) or s8.6 (per generation) passages used above. | Register Q ids at integration. |
| m9 | MINOR | `parameters.yaml` | Missing entries: the LTEE genome rate 4.1e-4 (Z23003785 s4.3, verbatim); human 38.4 (derived); the kappa set (125, 652, 81,500, 93,659; derived); G 2,887 (derived); 6.64 gen/day; 20/25/29 y/gen; map 36.8 M (R4-GAPS-04-07-02). | Add them with `derived:`/source tags. |
| m10 | MINOR | Headline 1 and 3 | (a) The headline F values (to 8,970, i.e. up to 6.8 sweeps per generation) are uncapped. §6 of the raw output shows that Day's own caps limit F to 1.98 (1/667), 4.41 (1/300) and 33.9 (1/39), and the mean-field cap to 6.4-7.1 at R_h = 1.111. (b) The pre-registered per-generation neutral-inclusive F = 50,765 (docstring P5) is reported only per year. | Label the headline F as "uncapped". Add one line with capped F per generation, and one with neutral-inclusive F per generation. |
| N1 | NOTE | Files | Pre-registration verified. The md5 of the working-tree script is `c9f2c48d…`, matching the `.host` file. `git log` shows only 7593be2 touching it. Commit 22:24:17, launch 22:24:25. No post hoc content. | — |
| N2 | NOTE | §2-6 | Recomputed (scratch): 38.4/4.1e-4 = 93,659; 125 x 652 = 81,500; W&B bound 18.4 x 1,322/(2,425 x 20) = 0.501; 38.4 x 1,322 = 50,765 and F_yr 1.047; caps 4.41 / 1.98 / 33.9; R_h\* = exp((2 ln 2e4 + 2)/1,322) = 1.0166; mean-field F cap 6.39; kappa\* (independent closed form) 9.63 / 217.1 / 1,107 vs reported 9.63 / 217 / 1,110. The prediction tally (19 rows, 13 met) is correct. | — |
| N3 | NOTE | §4 kappa\* table | The flip is set by the population-size ratio times LTEE interference: kappa\* ≈ (M_LTEE/2N_h) · R_int. The LTEE has 1,650x more genome copies than humans at N_h 1e4. This is why kappa\* is identical across map 1.5 / 36.8 / free, and why the W&B and map-length details matter only far above the flip. It makes kappa\* robust to the human recombination model. | Worth one sentence in the write-up. |
| N4 | NOTE | Calibration notes bullet 1 | G_eval deviates from target by up to 12%, and F uses the target G. Using G_eval would move F by <= 12%, which is immaterial against the decades-wide spreads. | — |
| N5 | NOTE | P1b row | The pre-registered `analyse()` prints the N_e span at s = 0.01 as the P1 statistic (2.81x <= 3). By the registered statistic P1b is met. Scoring it "partly" is stricter than necessary, and acceptable. | — |
| N6 | NOTE | Engines | `class_rate`, `eq8` and `eq1_free` are inherited from A-sim and GAPS-04 (both reviewed). I did not re-validate them. | — |
| N7 | NOTE | Model | The calibration pins U_b,LTEE x u_LTEE. The model's u ≈ 2s at a constant M ignores the serial-dilution cycle. Any bias in u_LTEE or N_e,LTEE transfers inversely to the human supply. The direction is unknown, and the N_e sweep (0.98 decades) brackets it. | — |

## 2. Parameter provenance

| Input | Status after this review |
|---|---|
| G_f 1,322 | Verbatim, Z23003785 s3.3/s4.1 (Q58, Q63); `parameters.yaml` verified |
| G_f 1,587 | Derived from Z23105291 counts (`parameters.yaml` verified) |
| G_f 2,890 | Derived (exactly 2,887); not Day's. Day's adaptive figure is 1,408 (s4.3) |
| LTEE N_e 3.3e7 | Day-stated ≈ 3e7 (s8.2 p.14); no primary source |
| U_b,LTEE | Calibrated (model quantity) |
| kappa 125 / 652 / 81,500 | Hössjer's inputs (A5a, HO-01/02), derived products |
| kappa 93,659 | Derived from Day's stated factors (4.1e-4 verbatim; 3.2e9 x 1.2e-8 stated factors, printed product wrong) |
| Human N_e 3,300 / 1e4 | 3,300 from Day (another paper; H8: not in its cited source); 1e4 textbook (`verified: false`); Day here: 1e4-3.3e4 |
| Map 36.8 M | R4-GAPS-04-07-02 |
| 6.64 gen/day; 20-29 y/gen | Standard; not in `parameters.yaml` |
| Caps 1/300, 1/667, 1/39 | Haldane via Nunney (verified); H8 |

## 3. Proposed post hoc steps (none run)
1. Decoupled s (s_L ≠ s_h): an analyse-only closed form on the stored calibrations. Trivial locally or on na-workhorse.
2. N_h = 3.3e4 and 1e5 rows: closed form.
3. Optionally, a G_f = 1,408 calibration (one combo, about 2.5 min).
4. Capped-F and neutral-inclusive-per-generation lines added to the headline (no run).

## 4. Verdict implication
Internal: unchanged (non-sequitur, from the text). External per generation, on the adaptive-only model, the evidence supports **`contested`**:
- the flip lies 7-430x below the derived supply ratio on the coupled grid;
- that margin can be closed by an unmeasured beneficial-fraction or effect-size ratio (6/96 decoupled cells already close it).

"Leaning `contradicted`" is defensible only if stated with that condition. On Day's own total-throughput basis, F = 50,765 per generation. Whether that becomes `contradicted` depends on the human neutral rate (A5c), and that should be stated as a dependency. Per year: no A2e verdict (M2).

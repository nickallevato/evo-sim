# Review Log

## 2026-10-07 — Steelman review #1 (Sonnet; both sides) of B0.4, B1, B3
Quotes came through a summarizing fetcher and must be re-verified against PDFs in R1 pass 2.

### Day's side: tests and claims the checks do not yet address
| # | Claim | Critique | Action |
|---|---|---|---|
| D1 | B1 | His real claim, quoted from 22129121: "k=μ holds only after a population has held one size for the roughly 4Nₑ generations". That claim is about size changes, which the empty/equilibrium extremes don't test. | **B1b**: equilibrium start, then bottleneck, expansion, founder event. Report per-window k/U. |
| D2 | B2 | No check exists for exp(−π²Nₑ/G) or the ceiling X. | **B2a**: exact WF Markov chain, fit the exponent. **B2b**: expected fixation count across all mutations. |
| D3 | B3 | The exchangeable Cannings model is not his target. The real argument concerns structured or non-exchangeable populations (census/Nₑ 19–46×, sexual species, Nₑ/N ~0.1). | **B3b-i…v**: overlapping generations + fluctuating N; reproductive value; source–sink; sweepstakes; linked selection. |
| D4 | F | He uses sweep time as latency and makes a separate throughput argument (LTEE 1,322 = throughput). His best version is interference or cost capping throughput. | **F2**: multi-locus sweeps with r=0 vs r>0, clonal interference. |
| D5 | A | Window arithmetic. | Full-scale lineage count (G≈252k, N=10⁴, μ=1.2e-8, L=3e9) vs ~35M SNVs; separate out the effect of counting basis in 32.3μ. |

### Critics' side: places the checks are too generous to Day, or miss cases
| # | Claim | Critique | Action |
|---|---|---|---|
| C1 | B1 | "Exact for an empty start" must be framed as a counterfactual boundary. An empty pipeline means zero heterozygosity, which contradicts observed human π. | Add a data-consistency panel (π=4Nμ vs observed; implied θ_anc). **RESULTS wording updated.** |
| C2 | B1/B4 | No two-lineage or ancestral-polymorphism accounting. | **B4a**: two-population split; d = 2μT + 2N_aμ; fixed vs polymorphic; ILS with outgroup. |
| C3 | F | The latency table distracts from throughput; F1 hasn't been run. | **F1**: Poisson arrivals × P_fix; Little's law. |
| C4 | B3 | Day himself states 1/(2N) (Hard Limits paper; blog 2026-10-01: "1/2N is the fixation probability"). | Record as an internal-contradiction ledger item (text check). Also vary N at fixed variance in the Cannings model. |
| C5 | C | No check yet on aDNA panel ascertainment. | **C1**: panel ascertained at MAF>5% today gives ~0 fixations by construction. |
| C6 | general | B1 used only 60 reps. The N=50 z=−2.75 needs an exact-chain check (E4). G has no check. | Exact chain added in B2a; G queued. |

## 2026-10-07 — Correctness review #2 (Sonnet), on B0–B3
No simulation-code bugs. Findings and their resolution:
1. **BLOCKER:** `-I` broke the `wf` import. → Each script now inserts its own directory into `sys.path`. FIXED.
2. **MAJOR:** B0.2 target was a flat 4N. → Now the diffusion value at p=1/(2N). N=50 z = −2.15 (≈ −0.8 against the exact chain). FIXED.
3. **MINOR:** the stochastic sweep-time formula should use ln(4Ns), not ln(2Ns). FIXED in all scripts and in RESULTS.
4. **MINOR:** "within 1%" was not supported. → SEs added; claim restated against the 5% tolerance. FIXED.
5. **MINOR:** B1 matches by construction, its T ≤ 100 grid points were vacuous, and the prediction's noise was ignored. → Grid points removed, caveat added, burn-in raised to 20N. Multiplicity correction: NOT DONE (noted).
6. **MINOR:** a 10N burn-in leaves about a 2% flux deficit. → Raised to 20N in B1. FIXED.
7. **MINOR:** B3 had no z-scores and was missing the α=4 row. → z and SE now printed; row added; "provisional" hedge added. FIXED.
8. **MINOR:** kimura_u is a diffusion approximation (about 0.4% gap from the exact chain). Noted; SEs cannot distinguish them at current replicate counts.

Reviewer's independent verification: an exact WF Markov chain (in session scratchpad, not committed). It confirmed `single_locus`, `diffusion_cond_fix_time` (within 0.2% for 4Ns ≥ 20), and the Cannings BetaBinomial marginal.

## 2026-10-07 — Review #3 (Sonnet, correctness + two-sided steelman) of B1b, B2a, F1
The code is correct; the numbers reproduced, including a 4-replicate rerun of B1b. All changes were to wording and framing:
- **B2a (major):** the exponent was evaluated with the wrong limit order. → Replaced with N-convergence at fixed r (reviewer's runs; a script to commit is TODO).
- **B2a (major):** conditional vs unconditional reading. → Both shown; flagged pending the verbatim quote.
- **B2a (minor):** the G=4N comparison is harsh for an "of order" claim. → Fairness note added.
- **F1 (major):** Little's law was computed, not measured. → Relabeled. Measuring in-transit counts is a TODO.
- **F1 (major):** unrealistic regime, and the serial reading needs a quote. → Caveats added.
- **B1b (major):** "credit to Day" overcredited him, since this is standard theory and wrong in sign for contractions. → Reworded.
- **B1b (major):** "standard estimate ancestral Nₑ > modern" was unsourced. → Removed; deferred to B1c.
- **B1b (major):** pairwise divergence is a different observable from fixed substitutions. → Caveat added; B4a required.
- **B1b (minor):** recovery times were eyeballed. → Marked approximate. Analytic 4ΔN cross-check column added.

## 2026-10-08 — Review #4 (R4 batch): correctness, Day-side steelman, critic-side steelman, new-checks review
Reviews: `results/REVIEW-R4-correctness.md`, `results/REVIEW-R4-steelman-day.md`, and `results/REVIEW-R4-steelman-critic.md` cover H/C2, B3b/C1, B1c/B4a and F2/A. `results/REVIEW-R4-new.md` covers H2-hard and C1b. The correctness review re-ran most non-IBM scripts in scratch. There were **no BLOCKERs**. Every MAJOR is listed below with its resolution.

### Correctness review: MAJORs
| # | Item | Resolution |
|---|---|---|
| 1 | H IBM mutation-supply confound: mutations were applied to J juveniles, which inflated M by about R/2 under soft selection. | FIXED in `wf_hc.py` (mutation rate u·K/J). H scans rerun. "Soft is worse" survives and strengthens. "Soft within 15% of hard" withdrawn. Hard M=0.1, R=2.2: 285 → 170. |
| 2 | Post-hoc tuning toward Nunney's 300 (Model 2 adjusted twice). | Labelled EXPLORATORY. The "300 appears only at…" sentences were removed from the verdict text. |
| 3 | B4a: the CSAC 14–22% was compared with θ_anc/d, producing a spurious "tension" and an invalid T = 400–440k alternative. | FIXED. The comparison now uses poly-but-diff/d (config B 22–25%). The tension and the alternative were deleted. |
| 4 | B4a: the "supported" verdict used the wrong node (HCG). | FIXED. Moved to the HCB node (1.98e5), which overshoots by ~25%. Restated as a 3-parameter fit; the Yoo μ rescaling is open. |
| 5 | B1c: "every sourced history gives an excess" holds by construction. | Reframed as the B1b telescoping identity under step histories. K is not a difference count. |
| 6 | F2/A: extrapolations were stated as simulations (1.5–172×). | Labelled EXTRAPOLATION. "Contradicted at r = 1/2" softened to "not reproduced in the tested regime". |
| 7 | `hash()` seeds were not reproducible (f2_multilocus, a_ltee_scaling). | FIXED with `zlib.crc32`. Both rerun; numbers moved within noise. |
| 8 | C6/C1: "does not rescue Day" compared against a count the model does not simulate. | Withdrawn in R4-B3b-C1.md. The 21-count was then simulated in C1b (see below). |

MINORs, all applied:
- B1c/B4a burn-in raised 10N → 20N. This explains the 1.3% bias; controls now read 1.000.
- 17.1 vs 7.7 corrected in H1/H8, and the ratio between them is 2.2× (= 1/d).
- IBM size is 200k per type.
- Day's d·s is 20–22% below the exact value; d·s matches "within 1.5%" rather than "exactly".
- The paper's 0.49 is ~2% above the exact recursion.
- The B&L r = 0.039 row label is fixed, and the direction of the B3c limit is corrected.
- RRME 1/(2N_t) is now marked as a reconstruction.
- The C1 panel denominator omits African-private mutations, so counts are a slight upper bound.
- LTEE Nₑ = 3.3e7 is marked unsourced.
- The single-s calibration conflates neutral and adaptive fixations.
- The B4a "8Ne docstring" item was a mislabel: no such remark exists.

Not done:
- CIs on T50, and N/K in the success criterion (both stated as caveats).

### Day-side steelman: main points and how they were handled
- **Day's current position is narrower than the R4 headlines.** He has retracted the cost-on-total-k argument (H1), conceded a full pipe (B1d) and dropped d (A4d). → Verdicts now say "premise withdrawn by Day" where relevant (B1c). H's residual adaptive claim is recorded as open.
- **No check tests hard selection at human parameters.** → H2-hard was added. Haldane's regime (R≈1.1, D≈20–30) is still untested, and that is now queued.
- **B1c excess is not a difference count, and the human step is the most contraction-heavy.** → Reframed accordingly. Credit is given for (T−4Nₑ)/T = 0.84 on new mutations.
- **B4a at Day's Nₑ = 1e4 gives half the observed d; the fit has 3 parameters; Yoo's μ is unrecorded.** → Recorded in B4a/B6a. The Yoo μ rescaling is queued.
- **F2 is soft-selection only, and human-scale active loci (~1e4–1e5) are untested.** → The F2/G/Gc externals are now `contested`, not `contradicted`.
- **H's "fails vs 20M" should read as a scope concession.** → H internal is now `holds` (arithmetic), with the scope noted under external. For new mutations, D≈20 gives ≈200, the same order as 300.
- **C2: d·s is exact for hazard-scale s, and "fails as stated" overreaches.** → A4/C2a internal `holds for hazard-scale s`. C2 stays `non-sequitur` only for the fitted-d inference (identifiability).
- **C1a is right in sign for the bands it addresses; C6 binning was not modelled.** → C1a internal `holds`. C1b was run.

### Critic-side steelman: main points and how they were handled
- **Several checks test arguments no critic made** (Nunney, Euler–Lotka d, ancestral Nₑ). → The balance ledger credits the audit or the literature, not the critics, for these.
- **"Soft selection removes the cost" is not reproduced.** → Recorded against the critics in H and H2. Critics are not entitled to call H refuted.
- **Hancock 38M / Nesslig20 37.8M double count.** → On an SNV basis, 19.4M = 2μT, and observed ≈ 19M + ~15M ancestral. Recorded in B5c (external `contradicted` as an SNV match) and B5e (`contested`, basis unstated).
- **Asexual saturation was predicted by the critics too.** → Credit to Day is narrowed to sublinearity and to interference under linkage (A2e, A5d).
- **KITTENS linearity is not established at 94,000×.** → A5b external remains `contested`.
- **Observed 1 and 3 completions are faster than neutral at Nₑ = 1e4.** → Recorded in C, alongside the Day-side Nₑ-sensitivity reading.

### New-checks review (REVIEW-R4-new)
- **H2-hard, MAJOR (framing):** "literal 1/300 falsified" overreached.
  - FIXED to: "10% is not a general bound; the cap is ln R / D. Haldane's regime (R≈1.1, diploid D≈20–30 → ≈1/300) is untested."
  - Ceiling regulation is noted as the critics' compensatory-fecundity premise.
- **H2-hard, MINORs:**
  - λD < ln R is partly an identity; the real test is D ≈ ln M + 1.
  - The pre-registration was edited after V1.
  - Brackets use factor-2 spacing; the R=10 prediction miss is noted.
  - All applied.
- **C1b, MAJOR:** the "massive deficit vs neutral" and "sign stands" wording was REMOVED. The verdict is "not reproducible; cannot adjudicate". The reviewer's per-site call-depth hypothesis was added, with its 1-replicate numbers labelled direction only.
- **Code:** no bug found in either script.

## 2026-10-08 — Review #5 (Sonnet): correctness + Day-side and critic-side steelman of E and G1; fact-check of the gap ledger
Files: `results/REVIEW-R4-E-{correctness,steelman-day,steelman-critic}.md`, `results/REVIEW-R4-G1-{correctness,steelman-day,steelman-critic}.md`, `docs/research/ledgers/gaps-review.md`. Each write-up ends with a "Review resolution" table that maps every item to its change.

**E**
- **Correctness:** no bugs. Every number re-derived independently (founder chain against brute force to 1e-15; second MC sampler).
- **MAJORs:**
  - The population-level "600×" rested on one threshold. It is now a threshold sweep, and the conclusion is conditional and N-dependent.
  - The E3 falsifier fired under the literal model (2.75%). This is now stated, and the mean-field formulation is described as a model choice, not an artefact.
- **Day-side:** "non-sequitur" was aimed at a step paper E explicitly leaves to future modelling. The verdict is split: E is an untested bridge, and the overreach is in E3's wording.
- **Critic-side:** keruru's 2026-08-26 chain had been missed ("none located" was wrong). "Keeps growing with N" needs family size ∝ N. E4 changes t̄, never P_fix or k.

**G1**
- **Correctness:** reproduced bit-for-bit. 14.7 is also 1474·ln 1.01, so the "mixed scales" framing was withdrawn. λ = −m·ln(1−q). The "reverse-engineered 230" wording dropped its claim about intent.
- **Steelman conflict:** the two sides disagreed on additive dilution and on the 335× reproductive excess. Post-hoc runs settled both:
  - Dilution depends on an unstated fitness convention.
  - The excess is ≈ 340× only with all 157,000 loci at p = 0.5, and ≈ 1.3× at Day's own 230-locus crop.
- Scope box added: this check does not test Day's current G_f throughput argument.
- Missing critic credits added (Nesslig20, Bowers, a Reddit commenter, KITTENS, Camestros).

**Gap ledger**
- No BLOCKERs.
- Nunney 2003 was restated to the K values actually simulated.
- Murphy 2023 was cut back to what its abstract supports.
- GAP-01 now brackets the unmeasured noncoding adaptive share instead of letting a coding-only α stand for the genome.
- Matheson 2025's own caveat was added.

**Process note:** the check scripts were uncommitted at run time, so pre-registration can't be proven from git. From now on, commit the script with its predictions before the main run.

## 2026-10-08 — Review #6 (Sonnet): correctness + Day-side and critic-side steelman of GAP-04, GAP-07, GAP-02
Files: `results/REVIEW-R4-GAPS-{correctness,steelman-day,steelman-critic}.md`. The write-up `results/R4-GAPS-04-07-02.md` ends with a "Review resolution" table. Pre-registration commit `b812741` (scripts only, before the main run), verified byte-identical by the correctness review.

- **Correctness:** 0 BLOCKER, 6 MAJOR, 11 MINOR. Every headline number reproduced independently, and the W&B equations match the PDF. The MAJORs were overreach and disclosure:
  - E_detect is an upper bound (power 1).
  - The "1.2–13.5× undercount" mixed bases.
  - The SV bp comparison with Yoo's SDRs carries no weight.
  - All 20 F2 cells were known before the predictions, so P1–P3 and P5 test formula forms, not blind outcomes.
  - "Supply-infeasible" rested on one Fig. 4 reading at s = 0.05.
  - The concurrency figure is a ceiling, not an implication.
- **Steelman conflict on GAP-04:**
  - Day-side wanted the R/4 cap (exponential DFE) carried to human scale.
  - Critic-side noted that R/2 is an asymptote that W&B's own simulations exceed, at about 3R.
  - **Resolved:** report the bracket R/4 – R/2 – simulated max. Day's 17.5–20M is 6.5–9.1× / 3.3–4.5× / 0.54–0.76 of these.
- **Day-side:** the all-fixations reading is Day's stated model (MITTENS 3.0 §4.3, §8.2), not a side reading. Both models are now shown side by side, and branch B decides between them. Critic credits are scoped to the interference leg only. Day's full 3,200–32,000 sweep range is used.
- **Critic-side:**
  - Scan candidate lists are threshold-limited, so the 722/5,110 comparison is now illustrative only.
  - CSAC 5M is resolved as a total; the first-pass fidelity flag against A3/A3x is withdrawn.
  - Missed credits added: McCarthy, Fun-Friendship4898, Nesslig20/Neukamm, Mansfield, justatest90/Wrevellyn, DarwinZDF42, KITTENS.
- **Numbers that moved:**
  - GAP-07 headline 9–21× → ~9–11× (≥ 8× on observation-consistent points).
  - GAP-02 "K_a ≥ 10⁵ in tension with scans" withdrawn.
  - The agent's own "4–16% → 4–19%" correction to gaps.md retracted (different definitions).
- **Integrated:** verdict comments on F2, A, A2e, Gc, A3, A3a, A3b, A3x and H. New Day claims A6 (sweep signatures absent) and A6a (bonobo sweep mosaic). gaps.md R4 blocks; defeaters d246–d258.

## 2026-10-09 — Review #7 (Sonnet): correctness + Day-side and critic-side steelman of H3 (H at human scale)
Files: `results/REVIEW-R4-H3-{correctness,steelman-day,steelman-critic}.md`. The write-up `results/R4-H3-human.md` ends with a "Review resolution" table (§9). Pre-registration commit `0061b28` (script only, before any main run), verified byte-identical by the correctness review. Post hoc scripts: `70d83cc` (tables, P runs) and `e48a5af` (fix pass, committed before any fix-pass run; `3688bcb` speed-only rewrite of the packet model before it produced output; `872d8b1` logistic λ50 in the table builder). Fix-pass stages L, H, M, W, X ran on na-workhorse (12 workers); hosts and md5s in `raw/h3fp.host` and `raw/h3_fx.host`.

- **Correctness:** 0 BLOCKER, 4 MAJOR, 11 MINOR.
  - M1: the 10k-generation window had been read as a lifetime rate. Stage L (100k generations) gives long-run φ_252k = 0.30 / 0.57 / 0.59 / 0.73 at R = 1.1 / 1.5 / 2 / 3 (10k window: 0.54 / 0.69 / 0.76 / 0.76). The R_min tables were rebuilt and are now higher.
  - M2: φ ≈ 1 at s = 0.003 was promoted without a long run. Stage W gives 0.69 (R = 1.1) and 0.94 (R = 2); stage X (s = 0.001) is unresolved over the long run (2Ns = 2).
  - M3: only favourable mutation supplies had been run. Stage M gives D ≈ 15 + 1/M at M ≤ 0.03 (39–163), and at M = 0.01 even R = 2 sustains only ≈ 1/430. Listed as Day-favourable.
  - M4: the hard-load extinction at K = 1000 was an artefact. At K = 4000 / 10⁴, U = 2.2 with R = 20 persists. The Day-favourable list is cut to R ≤ 9 (analytic), and the H2-hard comparison is withdrawn (its load was not heritable).
- **Day-side steelman** (7 MAJOR, 5 MINOR):
  - Day never claimed R-independence. D1 is split: **D1a "parallelism does not raise the total beyond the shared budget" held**; D1b "the budget is 10%" is a parameter (R ≈ 1.1).
  - R anchors added: Haldane 1.1 (Matheson 2025, k = 1.1), Day's s_max ≈ "twice as many descendants" (R ≈ 2), and Day's own total fertility 6–8 (R ≤ 3–4 before mortality).
  - H1 is scoped to Term 3 (Z19984826) only; Z18168236 §5.1 has its own scope reply.
  - The 17.5M–205M failure holds for any cost model and is **uninformative about A/B**.
  - The a_nc flip threshold (≈ 0.01–0.6%) is below the resolution of any α estimate, so "coding-only fits" is **undetermined**, not a critic win.
  - Hössjer's conditional is mechanically confirmed. A headline box was added.
- **Critic-side steelman** (6 MAJOR, 8 MINOR):
  - Every verdict is now conditional (hard/soft adaptive × hard/soft load). The hybrid H3 tests is the audit's construction.
  - Named but not modelled, with the direction of each: soft selection (Wallace/Nunney), absolute-fitness gain, truncation/synergistic epistasis.
  - D = 5 rows and a break-even D table were added, for Hancock's intermediate-frequency point.
  - The hard-load rows are labelled bounding cases (Keightley, PA-16/17).
  - Credits fixed: Hancock (four timestamped points), Nesslig20 → Matheson, keruru KR-09.
- **Steelman conflict on what "1/300" means:**
  - Day-side: the rate is reproduced at R = 1.1.
  - Critic-side: R = 1.1 is Haldane's assumption, so the match is circular, and it needs a soft deleterious load.
  - **Resolved:** stated as a consistency check at Haldane's chosen R, within a factor of about 1–3 of ln R/D. 10k λ50 = 0.00340 [0.00300, 0.00379]; it fails over 40k; long run ≈ 1/530–1/1,050 (s = 0.01).
- **Numbers that moved:**
  - φ(R = 1.1): 0.53 → 0.30 (long run).
  - R_min for K_a = 10⁴ (T = 252k, D = 20): ≈ 2.7 → 2.98.
  - Hard U = 2.2 at R = 20: "extinct" → persists at K ≥ 4000.
  - Finite-supply D: 6.5–22 → 6.5–163.
  - Single-locus total cost at 2Ns = 2,000: 16.8 → 15.8.
  - Term 3's 0.0296 at R = 2: sustained in 10k only.
- **Not run (with reason):** the soft-adaptive variant. In H3's model soft selection has no demographic cap by construction; the soft-selection rate-limit question stays with R4-H-C2.
- **Integrated:** verdict comments on H, H1, H2, H5, H6, H7, H8 and ROOT-M row 1; RESULTS.md H3 entry; gaps.md GAP-01 R4 block; defeaters from d259.

## 2026-10-09 — Review #8 (Sonnet): correctness + Day-side and critic-side steelman of GAP-07b (direct alignment event count)
Files: `results/REVIEW-R4-GAP07b-{correctness,steelman-day,steelman-critic}.md` (committed f8625f6). The write-up `results/R4-GAP07b-alignment.md` ends with a "Review resolution" section (§14). Pre-registration commit `3c847b8` (script and predictions P1–P8 before the main run; unchanged since, verified by the correctness review; main run started 12 s after the commit). Post hoc: `c1727f0` (first pass), `3798b92` and `fbbc580` (fix pass, each committed before it ran); fix-pass note and outputs `56b6023`. Data: UCSC hg38 vs panTro6 net/chain/axtNet and hg38 vs gorGor6 axtNet (md5s in the note); all runs local, `nice -n 19`, one process.

- **Correctness** (0 BLOCKER, 3 MAJOR, 10 MINOR). An independent re-implementation reproduced the headline exactly: 37,767,396 SNVs, 4,301,652 chain gaps, 42.1M events, 205M/21.05M = 9.74; Day's 410M is a two-lineage total and 205M its half, so the comparison is like for like.
  - M1: the post hoc symmetric indel polarization cannot see events > ~100 bp (axt records break there). Indel lineage claims are now restricted to <= 50 bp (97.4% of indel events); effect on per-lineage totals <= 0.27%.
  - M2: the §7 per-lineage figures came from the flawed pre-registered rule. Recomputed: human 20.07–20.63M, chimp 21.46–22.0M; 205M / human lineage 9.9–10.2.
  - M3: the N filter is event-level (327 Mb flagged, 40–45 Mb N), chimp-only gaps are never flagged, and a constant 80 Mb unaligned term is 41% of F3; the masked 22–24× rows are a unique-sequence bound, not "the ratio stays".
  - MINORs applied: the SNV-only omission is ~10–12%, not ~20%; the headline uses the main-run 42,102,514; every post hoc number tagged (the <2% threshold was chosen after the miss against CSAC's 35M); P6/P8 sub-predictions added. qDup overcount noted but not quantified.
- **Day-side steelman** (4 MAJOR, 6 MINOR):
  - Day's stated rationale was missing: 04-28 ¶19 (one large SV fixes "as a single low-probability event"; bp counting "is generous to the standard model") and 05-13 ¶4–6 (SNV-only and bp brackets; "the conclusion holds either way"). Added as Q97–Q103; A3x's "Day has not defended" is superseded. Tested: as a weight, 205M needs ~3,250 SNV-equivalents per event above 50 bp, against Day's own event-counting G_f.
  - hg38 vs panTro6 is not T2T, while Day's figure rests on T2T data: labelled everywhere; repeat-unit and slippage sensitivities give the Day-favourable side of the bracket (7.2–9.5).
  - "What survives for Day" box: SNV-only 17.5M is 83% of measured events and brackets the polymorphism-corrected fixed events (16.4–18.1M); the SNV-only shortfall rises on the measured count (99,100–110,400 at 1,322); the bp magnitude of non-1:1 sequence is the same order as 410M; his first-edition "40 million" was an events figure (42.1M measured).
- **Critic-side steelman** (6 MAJOR, 6 MINOR):
  - 9.7× is the lowest ratio the note's numbers support: human lineage 10.1, top-level fills 10.4, <2% 10.8, polymorphism 11.1–12.5, combined 12.3–13.4 (critic-favourable side of the bracket, all post hoc).
  - "SNV-only is a floor" contradicted the data and was removed. The 523M "Yoo-style" row counted aligned nested sequence and double-counted 2.75M SNVs (corrected to 521M; 491M without syntenic fills); the 261M row contains 59.5 Mb of centromere models.
  - The critics' independent numbers are now graded: McCarthy 22.5M +7%, Mansfield 25M +19% (per lineage assumed), Nesslig20/Hancock ~38M −10% of events; the k = μ rate route (9.7M) is ~2× low. Errors attributed on both sides: CSAC's ambiguous "5M in each species" (a total), the audit's own 22.5M upper bound (retired), A3x's 1,140 six-ape inversions (453 in the net), critic slips RF-6, MF-03, PS-01, GG-11.
- **Steelman conflict on the headline:** Day-side 7–10× (non-T2T, between-bp-and-events readings), critic-side 10–14× (lineage, fill and polymorphism corrections). **Resolved:** the pre-registered raw 9.7× stays as one point in a stated bracket of about 7–14×, each row labelled with its assumption and direction; "events are not fixations, and events are not selected" sits beside the headline.
- **Not run (with reason):** the population-frequency measurement of polymorphism (GAP-07c; new data set) and a T2T re-run (CHM13/hs1 vs mPanTro3); both queued.
- **Integrated:** verdicts A3 (holds / partial / contested), A3a (arithmetic-error / misread / **contested**, not contradicted: contradicted only as an event count; Day's weighting reading untested), A3b (holds / partial / **supported**), A3x (holds / **partial** / supported); check paragraphs on A3c and A3d; RESULTS.md GAP-07b entry; gaps.md GAP-07 R4 2026-10-09 block; quotes PS-05, RE-14, RE-15; defeaters d270–d278.

## 2026-10-09 — Corpus refresh integration (not a check; no review)
Memo `docs/research/sources/refresh-2026-10-09.md` (commit 0bd548e). Eight claim files created from items with verbatim quotes in `quotes-*.md`, four per side:
- Critic: A2i (Matev, LTEE G_f units), B2e (keruru Zenodo draft, measured N_e vs Wright's formula; `untested`, replication queued), B3i (Matev, 1/(2N_e) per copy sums to N/N_e > 1), G5 (Matev, CV falls while variance rises). Matev's arithmetic was checked: all three numeric points hold; his additive-vs-multiplicative and binomial-tail points carry no numbers and are recorded as proposals.
- Day: A2j (2nd-edition 1,400 / 1,139,000× and his 2026-10-03 adoption of 1,587), H10 (selection ceased ~1800; no parameters), B9 (drift would cause extinction "within centuries"; internal non-sequitur on his own premise, Q105), C7 ("no drift in 7000 years"; internal non-sequitur, as for C).
- Also: Q104–Q105 added (Day's 2026-09-15 comment, verified against the saved text; Q105 restates 1/(2Nₑ) after the 08-27 concession, noted in `ledgers/versions.md`); B3e gained Matev's RF-3 as a second source. Defeaters d266–d269, d274–d275.
- Not made into claims: Hilbert (EES; no model or number), Day's "Reverse-MITTENS"/new disproof (unpublished), the 1,017-per-generation book quote (book not accessible), keruru's rs35619459 non-reproduction (C1d; needs the unnamed source).

## 2026-10-09 — Review #9 (Sonnet): correctness + Day-side and critic-side steelman of C1c (Day's aDNA 21 with real call depth and ancestry replacement)
Files: `results/REVIEW-R4-C1c-{correctness,steelman-day,steelman-critic}.md` (committed e5e4b15). Write-up `results/R4-C1c.md`, "Review resolution" §10. Pre-registration `b128110` (script, depth table and P1–P8 before the main run). Post hoc, each committed before its run: `ee0b725`, `9045329`, `d2fe788` (fix pass); results `f6fdc50`, revised note `04ae7e9`. All runs local (`nice -n 19`, 4 processes).

- **Correctness** (0 BLOCKER, 2 MAJOR, 6 MINOR, 1 NIT). Independent re-parse of the AADR v62.0.p1 anno reproduced the depth table (8,808 individuals); `selftest` passed; a fresh seed reproduced the grid; a closed-form N_e → ∞ integral matched the statistic code.
  - M1: capture heterogeneity was applied to the modern bin too (82% high-coverage diploid); 95–99% of the "inflation" sat in 0–500 BP. Rerun with ancient-only heterogeneity: S21 moves x0.5–x1.7. "Strongest lever", "tracked fraction only with S21 in thousands" and the P7 outcome withdrawn or re-scored.
  - M2: the 10000+ bin was placed at 10,500 BP; its AADR dates have median 15.5 kBP. At real dates the all-bin profile distance falls 0.69 → 0.25 (R0 N_e 1e5); bins 1–10 stay unexplained.
  - MINORs applied: T1 excluded deductively; v62.0.p1 labelled; tuned European filter and 101 rescaled moderns disclosed; 4 replicates support factor-of-2 statements, not a point N_e*; post hoc gate criteria labelled.
- **Day-side steelman** (8 MAJOR, 5 MINOR): matched capture (tracked 0.72–0.74) gives S21 50 (R0 N_e 1e5) and 26 (R2 N_e 1e6), not thousands; the textbook-N_e error cell (R2, N_e 1e4, eps 1e-3) reproduces Day's eligible count and start table; "literature Holocene N_e well above 1e4" was unsourced and is removed (retrieval gap recorded); stasis is Day's stated model and is the N_e → ∞ edge (S21 ≈ 2–5); S21 / eligible is the density-robust comparison (Day 0.129%).
- **Critic-side steelman** (6 MAJOR, 6 MINOR): growth schedules (1e4 → 1e6: S21 15–35; step 1e4/1e5/1e6: 32) were left out of the summary; keruru's own downward-bias caveat (up to fivefold) was ignored; the error-rate result was the one pre-registered prediction that broke the critics' way; the 21-class events start at ≥ 95%, so the intermediate-start claim (C) is untouched; critic errors are now attributed (keruru 1e-29 vs 1e-46; ratio stated three ways).
- **Integrated:** see review #10 (C6 and C-branch verdicts set on C1c + C1d together). Holocene-N_e retrieval gap recorded in `ledgers/gaps.md`.

## 2026-10-09 — Review #10 (Sonnet): correctness + Day-side and critic-side steelman of C1d (Day's aDNA statistics on the real AADR genotypes; keruru's temporal N_e)
Files: `results/REVIEW-R4-C1d-{correctness,steelman-day,steelman-critic}.md` (committed 43cb710, 0674221). Write-up `results/R4-C1d.md`, "Review resolution" §10. Pre-registration `c0a4071` (P1–P16 before the main run). Post hoc, each committed before its run: `814f5da` (+ bug fix `982366c` before its first successful run), `d308586`, `c09b957` (fix pass: library/damage, two-period pipeline, m-grid, modern-bin variants), `5f0ba57`, `3f70039`; figure `6f43473`; results `0c696f9`, revised note `ab04785` (with quotes-day Q106–Q117). Genotypes (AADR v62.0.p1 and v66.p1 1240K, md5-verified) downloaded and processed on na-workhorse only (host and md5s in `raw/c1d.host`).

- **Correctness** (0 BLOCKER, 3 MAJOR, 10 MINOR). Independent decode confirmed TGENO layout and bit order (SLC24A5, SLC45A2, LCT), the sample (8,808), ploidy labels, the statistic on named SNPs, keruru's replication and the factor of 2.
  - M1: Day's documented two-period pipeline (Z23046531) was skipped → run in the fix pass: sample 1,377 / 683 (his 1,372 / 680), SNPs 1,143,870 (his 1,143,671), completions from MAF ≥ 10% 2 and 0 (his 1 and 3), events 63,631 vs 17,814 (3.6x).
  - M2: the regional-composition caveat on keruru was asserted → computed: 6–17% of the BA-to-Medieval F; within-region N_e (3.4k–14.6k) points away from composition.
  - M3: "no setting gives tracked 0.65–0.80" was false (m = 40 gives 0.755, m = 45 0.671; S21 still ~3.9k). P9 held on v62.
- **Day-side steelman** (4 MAJOR, 6 MINOR): no damage/library dimension → library-type test run (matched random controls): the transition excess is not specific to damage-prone libraries, so damage is not the missing piece; "scripts do not exist" → "not found in the Zenodo records searched; the promise is in Z23046531 and may mean on request" (GitHub, OSF and the blog corpus also searched, read-only); the transversion comparison was left open in both bullets and the "~900 expected" figure withdrawn; Day's wins (start table to 0.4 points; 98.8% near-fixation; transversion pre-7000 share 0.98–0.99) moved into the brief.
- **Critic-side steelman** (5 MAJOR, 4 MINOR): "transversions same order as 21" re-stated per eligible allele (0.57% vs Day 0.094%) and per site (31x autosomes, v62); "untestable" is wrong for a tested statistic; B2e scored separately for RF-12 (not established at 1e7) and RF-13 (partly supported; ≥ 6x at any census ≥ 1e5); the composition point is now computed; keruru's factor of 2 is an error (his code comments) but small and disclosed.
- **Integrated (C1c + C1d):** C6 external untestable → **contradicted** (as stated; best Day reading "underspecified"; reopens as contested if a pipeline is documented); C7 external pending → **contradicted** for "no allele-frequency movement" (drift attribution open); C unchanged (contested; C1c/C1d do not address the intermediate-start statistic; completions reproduce in kind); C5b internal pending → **holds** with a slip-ledger note (halved pseudo-haploid correction, 7–19% on the headline windows; under the X1 25%/no-flip rule this is ledgered, not an error) and external pending → **supported** (lower-bound variance N_e; replicates within 4%); B2e external pending → **contested**; comments on C1, C1a, C4, C5a (N_e near 2 excluded); B2, B2b unchanged. Defeaters d279–d286, d292–d297.

## 2026-10-09 — Review #11 (Sonnet): correctness + Day-side and critic-side steelman of D1 (sequence-space spike)
Files: `results/REVIEW-R4-D1-{correctness,steelman-day,steelman-critic}.md` (committed 43cb710). Write-up `results/R4-D1-spike.md` (first version `e70363d`), "Review resolution" at the end. Pre-registration `d72c733` (ViennaRNA 2.7.2 pinned; predictions before the main run). Post hoc: `582428a` (summarizer only), `88dda5a`, fix pass `40d9261` and `e92de84` (each committed before its run), outputs `8b4acfd`, `a4c640d`, revised note `5f82925`. RNA runs on na-workhorse; DMS (ProteinGym; URL, date and sha256 in §1) and GB1 local.

- **Correctness** (0 BLOCKER, 4 MAJOR, 10 MINOR). Shape level, neutral-network estimator (exact enumeration of 10-mers), the m → λ mapping (λ_alt = 0.48 at s = 0.01), DMS counts and GB1 maxima all reproduced independently.
  - M1: two pre-registered "would change the reading" triggers fired unacknowledged (E2 m 24–37 at L 30–50; DMS majority-destroyed 2%) → acknowledged in §0.4; "below the flip for every single-genotype definition" withdrawn for the pre-registered lenient class (λ 13.4).
  - M2: pooled counts ignore the 1/K split → withdrawn as supply; a first-passage run replaces them (median 36–80 neutral steps to a one-step route vs 0.03–0.06 available per locus).
  - M3: GB1 "strictly uphill" used an unstated 0.1 margin → margin table 0–0.3 (SNV-level maxima 67–158; reach 51–30%).
  - M4: the walk sampler under-mixed (0.55 L vs 0.73 L uniform) → reach inflated ~1.25–1.3x; m given reach unaffected.
- **Day-side steelman** (7 MAJOR, 8 MINOR): tolerance rows are Day's "neutral noise" horn, not alternatives → tagged H2; the needed-change analogue (beneficial-proxy per codon 0.21, λ 0.10) added; "Day's m ≈ 1" came from the docstring → removed; the gene pool is shared → Table C (k = 10: 0.999; k = 25: 0.074; k = 50: 4e-20 at s = 0.01); D2h scored as worded ("reduce or destroy" passes in 61%); GB1 SNV-level ruggedness shown robust to margin.
- **Critic-side steelman** (6 MAJOR, 8 MINOR): exact-structure-per-locus is Day's horn by construction → axis of readings (H1–H4) with H4 named as untested by per-requirement rows; the pre-registered P10 comparison now reported (Table B: within-gene beneficial fraction 82–1,600x G1's requirement for n ≤ 2e5, 8–16x for n = 2e7 at p = 0.02); s-sweep to 0.05 (one-codon tolerance reaches the flip near s 0.03–0.04); critic-favourable facts moved into §0; the unsourced "critics' strong form" removed and Camestros/McCarthy quoted.
- **Integrated:** D1d external pending → **supported** (existence part); D2h external contested with the as-worded comment; D, D1, D1a, D1b, D1c, D2c, D2i, D3, D4, D9a, D10–D12 external unchanged (contested) with D1 comments; G3b's open item replaced by the measured per-locus λ, Table C and Table B. Defeaters d287–d291, d298–d300; lineage L-audit-d1-first-2026 (retracted first-pass wording) and L-audit-d1-2026.
- **Also this round:** A3 marked load-bearing (ROOT P1 and A P4 rest on the required-fixation count; full standard form added).

## 2026-10-09 — Review #12 (Sonnet): correctness + Day-side and critic-side steelman of X1 (critic arithmetic), plus a blind audit of the verdict rule
Files: `results/REVIEW-R4-X1-{correctness,steelman-day,steelman-critic}.md` (43cb710, dcca246), `results/REVIEW-R4-X1-rule-audit.md` (0301f12). Write-up `results/R4-X1-critic-arithmetic.md`; rule `results/R4-X1-verdict-rule.md` (rev 2, with section 9 "Rule audit resolution"); re-score `results/R4-X1-rescore.md`. Pre-registration `fa0bc9b`; post hoc scripts `77b9790`, `11744e6`, `32e2a75`, `4318f16`, `f9e8291`, `6eea84e`, `849ec9c`, each committed before its run. **Why X1 existed:** the R5 draft's balance audit found 22 of 112 Day nodes with internal error verdicts against 0 of 51 critic nodes, and only one check aimed at a critic claim.

- **Correctness** (0 BLOCKER, 3 MAJOR, 7 MINOR). Every recomputation reproduced independently (keruru's exact WF value 5.12e-45 at p = 0.5; the repo's 1.2e-46 is 41x low; McCarthy's 25 y / 20 y mix; Hancock's 407 vs 813 and the 8.9e-11 rate). M1: keruru's values reproduce at Nₑ of about 8k (his own C5b), so "arithmetic-error from his own inputs" was fragile → C5 `pending` / `unverifiable` (rule R1c). M2: the "event-basis 38M is fine" rescue of Hancock was asserted → computed and withdrawn. M3: no stated tolerance between `holds` and `arithmetic-error` → the rule.
- **Day-side steelman** (6 MAJOR, 4 MINOR): the strict standard was applied to two critic slips only; the non-sequitur test was never run on critics; "34 of 45 clean" was arithmetic-only; Day's s6.4 38,400 slip had no Day node → rule rev 1, a non-sequitur test on the critic candidates, new node A5h.
- **Critic-side steelman** (5 MAJOR, 4 MINOR): B5a scored from a comment; C5 scored on an unretrieved, steep method; tolerance not uniform (1.75x error vs 2.2x immaterial); Hancock judged against the wrong text; uncited inputs marked down for critics but not for Day → rule scope S, R1c, F applied to both sides.
- **Blind rule audit** (agreement 90% on Day calls, 100% on critic error / no-error calls; gap survived its own scoring, 17/82 vs 0/31, p = 0.003): found clauses that bite one side harder (an omitted-term escape that printed-number slips lacked; R1c rescuing steep outputs; N2b's exposure to authors who wrote more; a denominator regex counting the audit's own `derived:` lines), plus the A3a charity reading, F double-counting F1a, and a misattribution (B5f) → rule rev 2 (lead's decisions: one symmetric slip test on the author's own stated conclusion; R1c only for roughly linear outputs; charity tried and recorded on every node; N2b kept and its exposure reported per 10k quoted words; quote-based denominators).
- **Result (rule rev 2):** error verdicts Day 13/81 vs critics 1/20 (quoted-text numeric, p = 0.29); 16/82 vs 1/31 (formal-statement, p = 0.038); 18/114 vs 1/51 (all files, p = 0.008); per 10k quoted words 22.7 vs 10.0. If the three critic tie-breaks flipped, 16/82 vs 4/31, p = 0.58. Reading: Day's errors are robust to reading; the audit cannot claim critics err less per argument.
- **Integrated:** Day: A3a, G, F, A5e, G1a → `holds` (+ ledger where a slip); C6 internal `non-sequitur` (was arithmetic-error; external stays `contradicted`); B6a stays `arithmetic-error` on Day's own table basis; bases corrected for B3c, B9, C2 (d = 1 point moved to C2a), D9a; Gc made unconditional; fidelity n/a → `unverifiable` on 11 Day nodes, H1 `partial`, B1d `unverifiable`, A5d `accurate`; new node **A5h** (s6.4 38,400 for 3,840; `arithmetic-error`). Critics: B5c → `non-sequitur` (event basis); C5 `pending` / `unverifiable`; A3d `holds` / `unverifiable`; B5d `n/a` / `unverifiable` (rule U); B5e, B4g, B6c, E5, G2c `holds`; B5f `holds` with the attribution corrected (justatest90, comment pcug1j0; RE-16 to RE-18); fidelity changes A5c, B5c, B5e `unverifiable`, B5a, B5f `accurate`, G2c `partial`. The repo's 1.2e-46 corrected in claims/C5 and with dated notes in `R4-C1c.md` and its critic review. C2b gained its ¶9 Statement quote; G lost its withdrawn "hundreds of orders" sentence; E1 excluded from the numeric denominators. Defeater statuses resting on the withdrawn Day errors updated (d101, d104, d156, d177, d184, d202 → partly; d269 basis).

## 2026-10-09 — Review #13 (Sonnet): correctness + combined two-sided steelman of GAP-07c (polymorphic share)
Files: `results/REVIEW-R4-GAP07c-{correctness,steelman}.md` (346520c, 0301f12). Write-up `results/R4-GAP07c.md` with §10 "Review resolution". Pre-registration `078850b`; post hoc `gap07c_posthoc_toplevel.py`, `gap07c_posthoc_review.py` (ae42a91), each committed before its run. Two reviews, not three, because GAP-07c is a small follow-up to GAP-07b, which had full three-way review.

- **Correctness** (0 BLOCKER, 2 MAJOR, 8 MINOR). The chr21 site list, gorilla bases, VCF join and every ratio row reproduced independently. M1: the indel lineage split reused GAP-07b's withdrawn polarization rule → symmetric rule (human-lineage indel share 7.4–8.7%; ratio moves 0.02 at most). M2: the 1.7% SV share pooled both lineages → like-for-like human-lineage 6.9% (6.8% net, n = 450), about 2.3x below SNVs, not 9x; "supports Q100" → "consistent with".
- **Steelman (both sides)** (Day side 1 MAJOR, 5 MINOR; critic side 4 MAJOR, 2 MINOR): a single central ratio rested on the chimp assumption → bracket table marking which rows assume it; "within 2%" compared unlike counts → like-for-like (17.5M is 9.8% above fixed SNVs, 2.2% below all fixed events); A3c's "none in the Day corpus addresses polymorphism" was stale (Q37; 04-28 ¶24) → replaced; critic credits quoted with locators.
- **Integrated:** A3c status → reviewed, Check paragraph, external comment, Day's Q37 and 04-28 ¶24 quoted; A3b external stays supported with the like-for-like correction; A3x and A3 comments (fixed events 17.2–17.9M per lineage; 205M is 10.6–12.6x fixed events; combined bracket about 8–13x); gaps.md GAP-07 block. Defeaters d334–d336.

## 2026-10-09 — Mapping and Holocene-Nₑ retrieval integration (not checks; no review)
- **Mapping** (`docs/research/argmap/mapping-proposals-2026-10-09.md`, 19d0c55): applied as d301–d327, 11 flipped edges, 13 + 3 mini-forms, registry row x:eden-p9-caveat, 5 lineage nodes, 32 caption quotes (GG-17 onward, verified verbatim). G2c recorded as an alias of B6c. "Mapped" ratified (argmap/NOTES.md judgement call 12); G1b, G1c, ROOT-DE carry a "no attack warranted" note. Three unverified Hancock slips entered as `untested` rows (d328–d330). Exit criterion 2 (every critic and ally argument mapped) is **met** under that definition; the new claims stay `pending` until reviewed.
- **Holocene Nₑ** (`docs/research/sources/holocene-ne.md`, e746eb7): RG-01 → retrieved; decision pending **C1e** (rerun the C1c model on the published trajectories).

## 2026-10-09 - Review #14 (Sonnet, combined, low-stakes tier): P1 (machine-checked derivations)
File: `results/REVIEW-R4-P1-combined.md`. Write-up `results/R4-P1.md` ("Review resolution"). Pre-registration c17b44a. 0 MAJOR, 5 MINOR (Q03 labelling, Q33 2% tolerance, textbook Haldane definition, A3 exchangeable scope, critic-column wording), 6 NOTE. All fixed in wording; no new run. Integrated: Check paragraphs in B2a, B7, B3a, H, A5e; no verdict changed; registry ids chk:P1, rev:R4-P1-combined; no defeaters (no new attack warranted: a re-confirmation). Milestone post and board patch deferred to the next milestone.

## 2026-10-09 - Review #15 (combined, low-stakes tier): B5b (Mansfield supply, sourced neutral fraction)
File: `results/REVIEW-R4-B5b-combined.md`. Write-up `results/R4-B5b.md` ("Review resolution"). Pre-registration b707415. 0 MAJOR, 5 MINOR (f = 0.918 is an upper bound; uniform mutability; 450k match is the 2019 count; per-lineage basis; Mansfield's 2% was an illustration). Wording fixes only. Integrated: B5b Check paragraph, no verdict change; d348, d352; chk:B5b, L-audit-b5b-2026.

## 2026-10-09 - Review #16 (combined, low-stakes tier): F1b (in-transit count measured)
File: `results/REVIEW-R4-F1b-combined.md`. Write-up `results/R4-F1b.md`. Pre-registration fb6aac2. 1 MAJOR (Little's law on the same sample is an identity, so the 0.1% agreement is not a test; the tests are theory agreement 0.7-2.6% and Poisson dispersion), 4 MINOR. Escalation checked: F1 and F1a are load-bearing but no verdict moves, so no three-review tier. Integrated: F1 open item closed; F1b external contested -> supported (independent loci, no interference); F1a note (non-sequitur untouched); d347, d351; chk:F1b.

## 2026-10-09 - Review #17 (combined, low-stakes tier): G2c / B6c (standing variation)
File: `results/REVIEW-R4-G2c-combined.md`. Write-up `results/R4-G2c.md`. ADDENDUM (post hoc, 2026-10-09): the MAJOR is diagnosed as an accounting error (cumulative fixation counter vs window; true rate 0.99x intended) and the supported verdict was reverted to pending; rerun with B2 (228 concurrent sweeps) met R1/R2/R4 but missed the A-concurrency clause (0.6 vs [0.8, 2.5]), so external stays pending. Pre-registration 1ffd053. 1 MAJOR (the realised sweep rate in B is 1.55x the intended and unexplained; concurrency 146, not 230), 5 MINOR. Integrated: G2c and B6c external pending -> supported as a conditional; d345, d346, d350; chk:G2c.

## 2026-10-09 - Review #18 (combined, low-stakes tier): C1e (Holocene trajectories)
File: `results/REVIEW-R4-C1e-combined.md`. Write-up `results/R4-C1e.md`. ADDENDUM (post hoc, 2026-10-09): MAJOR-1 answered by a measured rerun at 25 y (6 replicates): R0 S21 Gravel 710, Gazave 3,387, Coventry 3,279, Nelson 31; all predictions met; no verdict change. Pre-registration 2c245ec. 1 MAJOR (trajectories are 25 y per generation, engine steps 20 y: S21 high by 1.4-1.7x; bracket applied, not rerun), 5 MINOR. Pre-registered misses disclosed (P5 sensitivities, P7). No verdict change (C4 pending, C6 contradicted, C unchanged); d343, d344, d349; chk:C1e. Follow-up: corrected-clock rerun (post hoc).

## Queue
Moved to [`QUEUE.md`](QUEUE.md) (2026-10-09).

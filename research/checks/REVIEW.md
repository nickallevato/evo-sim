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

## Queue (after review #5)
1. **H with realistic human parameters** (largest open item):
   - R ≈ 1.1–3 with age structure, diploid D ≈ 20–30, and a hard-selected deleterious load.
   - Human M from a sourced beneficial DFE.
   - Hard selection combined with linkage.
   - Now bounded by GAP-01: the adaptive count is about 10³–10⁴ (coding) up to ~10⁶ (if 5% of noncoding changes were adaptive). Also use the published Nei/Felsenstein −ln p₀/ln k spacing (prior-art.md) as an analytic cross-check of H2-hard.
2. **GAP-04:** fit the Weissman–Barton map-length cap to the F2 grid, then evaluate it at 35–38 M.
3. **GAP-07:** arithmetic for indel/SV event counts from published rates (sharpens A3x).
4. **GAP-02:** expected detectable sweeps per side within scan windows.
5. **D sims:** sequence-space / Wistar claims. The G1 middle case (λ threshold) needs a per-site m, which branch D's per-sequence estimates don't supply.
6. **C1b follow-up:** a per-site, per-bin call-depth model with real AADR coverage, plus an ancestry-replacement model.
7. **Binomial CIs on H T50**, plus N/K in the success criterion.
8. **Yoo 2025 μ and generation time:** rescale Nₑ,anc to the pedigree μ, then report the joint (T, μ, Nₑ,anc) surface, now with GAP-06 (consistent μ × g, a BGS-aware Nₑ,anc).
9. **E leftovers:** E7 mutator sublinearity; E1/E2/E5/E6/E9; heterozygote-load and meltdown pathways (E3 §4); mutator fertility.
10. **Also open:**
    - PM2013 Table S5 / PSMC numeric curve.
    - Lehmann 2014 normalisation.
    - LTEE Nₑ source.
    - Coale-Demeny tables and the s definitions in the aDNA papers.
    - F2 at N = 1e4 and 2N·U_b ≥ 100 with a DFE.

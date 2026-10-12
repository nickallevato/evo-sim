# R4 A2e-alpha: published human adaptive-substitution estimates against the A2e flip (~191 per lineage)

**Status: run, written up, reviewed (651e0d3: correctness, steelman-day, steelman-critic), fix pass done (see "Review resolution" at the end). Not integrated.** Load-bearing tier.

## Files
- Script `research/checks/a2e_alpha_map.py`, pre-registered at **49824e0** (docstring = predictions); run locally once after the commit (arithmetic and quote verification only, < 1 s). The pre-registered run is unchanged. **Post hoc** (fix pass, after the reviews): `research/checks/a2e_alpha_gv_acc.py` (committed at 164837e before its run; raw `results/raw/a2e_alpha_gv_acc.out`) and inline arithmetic in the Review resolution.
- Raw output `research/checks/results/raw/a2e_alpha.out`. Sources: `docs/research/sources/refresh-2026-10-10b.md` s1; local texts under `sources/raw/refresh-2026-10-10b/` (gitignored), sha256 printed in the raw output. All 13 quotes verified as substrings of the local raw text.
- Target: A2e (`docs/research/claims/A2e-ltee-as-ceiling.md`), the per-generation adaptive-only flip from R4-A2e Flag 1 / PH8. RH tag: the scored statements are dialectic: Q138 ("The objection implicitly claims that humans can fix mutations faster per generation than bacteria under ideal conditions", MITTENS 3.0 s8.6, PDF p.15) and the core of Q130 ("unattainable ceiling, the absolute best-case scenario", s2, PDF p.4; split tag, ledger RH-4). The threshold is Q139 ("191 achievable", s7.3, PDF p.13). Nothing rhetorical is scored here.

## What was done
R4-A2e found that, per generation and adaptive-only, A2e is equivalent to "the human lineage fixed at most about 191 adaptive substitutions since the CHLCA" (252,000 / 1,322). The refresh fetched the published alpha (adaptive fraction) estimates. This check multiplies each alpha by a nonsynonymous-substitution count for the human lineage and reads off which side of the threshold it lands on. Two thresholds: **G1** = 252,000 / 1,322 = **190.6** (Day's MITTENS 3.0) and **G2** = 252,000 / 1,587 = **158.8** (2nd edition). Day's adaptive-only reading (1,408 → 179.0) and Yoo's generation count (257,143 → 194.5) are printed as well.

Denominators (all are counts over a gene set, so lower bounds on the whole-exome count):
- N1, Gayà-Vidal human branch: 2 × 9,785 = 19,570. The "2" is rounded in the text, so 14,678-24,463 is also shown.
- N2, Boyko 22,180 / 2 = 11,090 per lineage. This assumes an even split between the lineages.
- N3, N2 / 0.61 = 18,180. This scales to all autosomal RefSeq gene bases (derived).

## Results
| estimate (access) | adaptive substitutions per lineage | × G1 threshold | side (G1 and G2) |
|---|---|---|---|
| Gayà-Vidal 2014, alpha ≈ 0.2% on the human branch (full text) | 29-49 *(pre-registered mapping; withdrawn in the fix pass: a null, FI = 1.00, not a count; see Review resolution M1)* | 0.15-0.26 | ~~Day (A2e holds)~~ null, no side |
| Boyko 2008, 10-20% of human-chimp differences (full text; pooled over both lineages; conditional on the beneficial DFE, "more than 20%" if γ+ ≤ 5) | 1,109-3,636 | 5.8-19.1 | **critic (A2e flips)** |
| Boyko 2008, 9.3% gamma-model deficit, the lower end (full text; a model residual) | 1,031-1,691 | 5.4-8.9 | critic |
| *post hoc (m2, D1, D2):* Boyko 9.3%, 95% CL 5.4-12.8%, human share 25%, 33%, 50% of the adaptive differences | 299-2,327 (lowest: 5.4%, 25% share, N2) | 1.57-12.2 | critic in every cell |
| *post hoc (m1, C5):* Boyko 9.3% on the Methods count 36,138 (/2 = 18,069; N3 29,621) | 1,680-2,755 | 8.8-14.5 | critic |
| Uricchio 2019, alpha = 0.135 (**abstract only**; divergence basis and linkage treatment not stated in the abstract) | 1,497-3,303 | 7.9-17.3 | critic |
| Uricchio, strongly adaptive share only, 0.135 × 0.28 (abstract only; basis and linkage not stated; derived) | 419-925 | 2.2-4.9 | critic |
| Eyre-Walker & Keightley 2009, "little evidence" read as 0-5% (**abstract only**; human-macaque, not the CHLCA interval; the 0-5% reading is the audit's; the authors call the low estimate possibly "strongly downwardly biased") | 0-1,223 | 0-6.4 | straddles |
| Eyre-Walker & Keightley 2009, "as high as 40%" (abstract only; a conditional upper bound) | 4,436-9,785 | 23-51 | critic |
| Gayà-Vidal, "at least 40%" in accelerated genes | not mapped in the pre-registered run; **post hoc** (C2): 228 (75 polymorphic genes; bootstrap 95% 112-323), 67-136 after a Day-charitable ascertainment correction, 511 extrapolated to all 198 genes | 0.35-2.68 | straddles (see Review resolution C2) |

alpha\* (the alpha at which the count equals the threshold) is **0.65%-1.75%** across denominators and bases (G1: 0.78-1.75%; G2: 0.65-1.43%).

## Scoring of the pre-registered predictions
| ID | Prediction | Result | Score |
|---|---|---|---|
| Day side | the best human estimates put the lineage at or below ~191 | Gayà-Vidal: 29-49 (but a null, see M1). EK "little evidence" straddles the threshold. Galtier, "with the notable exception of primates", gives no count | ~~Holds for Gayà-Vidal only~~ **Fails as worded** (fix pass, m7/M1): no full-text source gives a count at or below 191; GV's pooled value is a null its authors flag as a possible underestimate |
| Critic side | Boyko and Uricchio give ≥ 1,000, i.e. > 5x the threshold, on every denominator and on both bases | Boyko 1,031-3,636 (5.4-19x); Uricchio 1,497-3,303 (7.9-17x) | **Holds on Boyko (full text); Uricchio concordant, abstract only** (D3). Boyko's lower 95% CL gives 599-982 (3.1-5.2x), below the registered 1,000 (m2) |
| Q1 | alpha\* between 0.8% and 1.8% | 0.65-1.75% | **Partly fails**: below 0.8% for N1-high and for N1/N3 on G2. Post hoc, on Boyko's 36,138 base it fails further (0.54-1.05%) (m1) |
| Q2 | GV 20-60; BO 10-20% → 1,100-3,700; UR → 1,500-2,700 | GV 29-49 (hit). BO 1,109-3,636 (hit). UR 1,497-3,303 (miss at both ends: 1,497 marginally low, 3,303 high; the range was set without the N1-high denominator) | **GV and BO hit; UR misses** |
| Q3 | estimates on **both sides by more than 10x each way**, so external stays contested with a named disagreement | Both sides: yes. By > 10x each way: **no**. The Day-side estimate is 4-7x below the threshold; the critic-side estimates are 5-19x above | **Qualitative part holds; the "> 10x each way" part fails.** Fix pass (C7): "both sides" holds only if a null counts as a side; the "4-7x below" ratio is withdrawn |

## Interpretation
- **The threshold sits inside the published range** *(revised in the fix pass)*. Estimators that correct for slightly deleterious polymorphism (Boyko, full text; Uricchio, abstract; EK's 40% conditional bound) infer coding-only counts of 1,000-3,600 per lineage on the pooled reading, and 299-982 under the most Day-favourable Boyko adjustments (lower CL, human share 25-50%). The only sub-threshold value is Gayà-Vidal's uncorrected, frequency-filtered MK null (FI = 1.00), which its authors flag as a possible underestimate; it is not a count. Gayà-Vidal's own accelerated genes (post hoc) give 228 (95% 112-323), at the threshold. The flip is not a matter of denominators: alpha\* is about 1% on every reading.
- **The two sides of the disagreement are not symmetric** (stated in advance). Coding-only counts are lower bounds on all adaptive substitutions, because regulatory and non-coding adaptation is not counted in any comparable human-lineage form (refresh s1). So a coding count above the threshold is enough for the flip if it is correct. A coding count below the threshold is not enough for Day: it would also need non-coding adaptive substitutions to number at most ~150.
- **Why the estimates differ.**
  - Gayà-Vidal's 0.2% uses SNPs at DAF ≥ 60% on the human branch. The authors say estimates in their DAF classes are affected by slightly deleterious polymorphism.
  - Boyko's 10-20% comes from a model-fit deficit (observed 22,180 versus 20,113 expected under the gamma DFE) and depends on how the beneficial DFE is modelled.
  - Eyre-Walker and Keightley's 40% is conditional on a decline in Ne.
  - This check does not adjudicate between the estimators. But they are not rival measurements of equal standing (C3): the bias-corrected methods were built because naive MK is known to be biased low when slightly deleterious variants are present, which is the case here. The opposing point (D1, D6) is that every number on both sides is an MK/SFS model inference; none observes human-lineage fixations directly.
- **Verdict relevance:** see "Verdicts after fixes" at the end. In short: external stays **contested**. The pre-review wording "the literature disagrees by about 100-fold" is withdrawn as false balance (C3).

## Who this helps
- **Day side:**
  - *(Revised in the fix pass.)* Gayà-Vidal, the only human-branch-polarised estimate, finds no genome-wide adaptive excess (FI = 1.00). That is a null, not a count of 30-50.
  - The critic-side numbers rest in full text on one model residual (Boyko, 9.3%, 95% CL 5.4-12.8%) of human-chimp differences pooled over both lineages; Uricchio is an abstract. Under the lower CL and a 25% human share, Boyko gives 299-491 (1.6-2.6x); the flip needs about 36-63% of that residual to be model artefact (D1, D2).
  - Gayà-Vidal's accelerated-gene set falls below 191 once its selection on human-branch Dn is corrected against the authors' own matched control (67-136, post hoc).
  - All numbers on both sides are model inferences. (Galtier's primates-below-0.5 and EK's "little evidence" bound nothing at the ~1% scale; dropped, C4/m6.)
- **Critic side:**
  - Two estimators within the MK/SFS framework, on independent data, infer coding-only adaptive substitutions at 1,000-3,600 per lineage, 5-19x above the flip (m8); every single Day-favourable adjustment leaves them above it.
  - The sub-threshold value is an uncorrected MK null; its authors say it "may be an underestimate". Their accelerated genes alone give 228 adaptive substitutions on the uncorrected reading (post hoc).
  - These are lower bounds: non-coding adaptation and the genes outside the sampled sets are not counted.
  - Even the strongly adaptive share alone (28% of Uricchio's alpha) exceeds 191 on every denominator.
- **Both:** The A2e question is now empirical and narrow: is the human-lineage coding alpha above about 1%? *(Revised.)* No bias-corrected estimate is below it; Day's side needs the corrected estimators to be wrong by about 1.6-5x even after the Day-favourable adjustments, or the pooled-lineage reading to be badly wrong.

## Caveats for the reviewers
- Two of the four quantitative sources are abstract only (Uricchio, Eyre-Walker & Keightley), and EK's "little evidence" was turned into 0-5% by the audit.
- The even split of Boyko's 22,180 between the lineages is an assumption. The 0.61 scale-up assumes uniform density across genes.
- alpha is the share of nonsynonymous substitutions fixed by positive selection. That includes weakly beneficial changes (72% of Uricchio's alpha). Day's 1,322-generation ceiling is a count of beneficial fixations of any effect size, so the two definitions match only roughly.
- Gayà-Vidal's "at least 40%" in accelerated genes is not mapped. Its Dn could on its own put a lower bound above 191; this was not checked. *(Fix pass: mapped post hoc, see Review resolution C2.)*

## Review resolution (fix pass, 2026-10-10)
Reviews at 651e0d3: correctness (0 BLOCKER, 1 MAJOR, 8 MINOR), steelman-day (2 MAJOR, 4 MINOR), steelman-critic (3 MAJOR, 4 MINOR). No BLOCKER. Everything new below is **post hoc**: the script `a2e_alpha_gv_acc.py` (committed at 164837e with its predictions, before its run) and inline arithmetic shown here. The pre-registered script and its output are unchanged.

**Source locators** (m4; all fetched 2026-10-10, refresh-2026-10-10b s1; quotes re-checked as substrings of the local raw text in this pass). Gayà-Vidal & Albà 2014, BMC Genomics 15:599 (PMC4124166): Results ("For SNPs with DAF ≥60%, we obtained α = 0.002"; "we obtained 198 genes showing human-specific acceleration"), Table 1, Methods ("In the human branch, we estimated a total of 18936 non-synonymous and 34241 synonymous substitutions"), Discussion ("This value may be an underestimate of the real value if a portion of the deleterious mutations persists at such high frequencies"; "downwardly bias the estimation of the FI and α value"; "Species with small effective population sizes are expected to have a lower proportion of adaptive substitutions"), Conclusion ("at least 40% of the non-synonymous substitutions in genes accelerated in the human branch"). Boyko et al. 2008, PLoS Genet (PMC2377339): Results ("is 9.3% less than what we observe (22,180; 95% C.L. = 5.4%, 12.8%)"; "depending on the exact nature of the DFE of beneficial mutations"; "more than 20% of human-chimp differences are adaptive"), Methods ("36,138 nonsynonymous"). Eyre-Walker & Keightley 2009 and Uricchio et al. 2019: abstracts (Europe PMC). Q ids for these go into `quotes-literature.md` at integration.

### MAJOR items
| # | Item | Resolution |
|---|---|---|
| M1 (correctness) / C1 (critic) | Gayà-Vidal's 0.2% is a null, not a count | **Accepted.** Table 1 ("All genes"): alpha = −0.361 (DAF ≥ 1%, N 8,019), −0.142 (≥ 15%), −0.059 (≥ 30%), **0.002** (≥ 60%, N 2,766, FI 1.00, DoS 0.001); the sequence is still rising at the last class. The authors call the last value a possible underestimate (Discussion, quoted above) and use it for relative comparison ("it is still useful to compare the relative contribution of positive selection"). Row 1 is relabelled "null, no side"; the counts 29-49, "on Day's side by 4-7x" and "about 30-50" are withdrawn from the Interpretation and Who-this-helps. GV stays a Day-side *datum* in one sense only: the one human-branch-polarised MK estimate finds no genome-wide adaptive excess after frequency filtering. The Day-side prediction is re-scored **fails as worded** (m7). Bookkeeping: the exact human-branch Dn total is 18,936 (Methods), not 2 × 9,785 = 19,570; alpha\* on it is 1.01% (G1) and 0.84% (G2), inside the reported range. |
| C2 (critic) | GV's accelerated genes may clear 191 on their own | **Done, post hoc.** See the C2 section below. Result: the uncorrected point estimate clears 191 (228; 1.20x), but its gene-bootstrap 95% interval straddles it (112-323), and a Day-charitable ascertainment correction puts it below (67-136). It does **not** clearly clear 191 under charitable assumptions. |
| C3 (critic) | "100-fold disagreement" is false balance | **Accepted.** The sentence is withdrawn. The Interpretation now says the bias-corrected estimators (Boyko, Uricchio, EK's conditional 40%) all land above alpha\* ≈ 1%, and the only sub-1% value is an uncorrected MK null its authors flag as biased low. EK's abstract says it outright: "these methods are expected to give downwardly biased estimates of alpha if there are slightly deleterious mutations". The Day-side counterweight (D6) is kept beside it: all values on both sides are MK/SFS model inferences, none an observed fixation count. |
| D1 (day) | Boyko's full-text number is a ~9% model residual | **Accepted as framing; no side change.** Restated: Boyko infers a 9.3% (95% CL 5.4-12.8%) excess of observed over model-expected nonsynonymous differences, "depending on the exact nature of the DFE of beneficial mutations". Survival condition for A2e at the point estimate: at least 1 − 190.6/1,031 = **81.5%** (N2) to 1 − 190.6/1,691 = **88.7%** (N3) of the 2,067-difference residual must be model artefact (ancestral-Ne or lineage misspecification, misidentified ancestral states, chimp-side polymorphism). The lower-CL row is added (m2): 599 (N2), 982 (N3), 3.1-5.2x G1; still critic. "Put" is replaced by "infer". |
| D2 (day) | Pooled human-chimp alpha and the 50/50 split lean critic | **Accepted; sensitivity rows added.** GV's Discussion supplies the mechanism (smaller-Ne species, lower alpha). Human share of Boyko's adaptive differences at 9.3%: 25% → 516 (N2) / 845 (N3); 1/3 → 688 / 1,127; 50% → 1,031 / 1,691 (= 0.093 × 22,180 × share, and ÷ 0.61 for N3). Compounded with the lower CL (5.4%, 25% share): **299** (N2, 1.57x) / 491 (N3, 2.58x). Every cell stays above 191. Day's honest limit stands: pooling narrows the margin but does not flip it alone or with D1's CL; with the compounded row the flip needs about 1 − 190.6/299 = **36%** of the residual to be artefact. Rows 2-7 are labelled pooled or not human-branch; GV is credited as the only human-branch-polarised source. |

### C2: Gayà-Vidal accelerated genes (post hoc)
Source: BMC Genomics Additional file 1 (CC BY 4.0, the publisher's open-access ESM link; also listed in the PMC XML as `12864_2014_6322_MOESM1_ESM.xls`), fetched 2026-10-10 into `sources/raw/a2e-alpha-gv-supp-2026-10-10/` (new dir, gitignored), sha256 `7b6cb765ad5f3e58a464def105a439c795f74341720c9d1fce53619ccf46c3b9`, 8,986,624 bytes; logged in `docs/research/sources/harvest-log-literature.md` (Refresh 2026-10-10c). Read with xlrd 2.0.1 (installed outside the repo), as data only. Sheets: S3 (all genes), S4-S7 (genes polymorphic at DAF ≥ 1/15/30/60%), S10 (198 accelerated genes).

Validation (P1, holds): the sheets reproduce Table 1 exactly (all genes −0.361 / −0.142 / −0.059 / 0.002; accelerated 0.375 / 0.356 / 0.409 / 0.405 at N 182 / 155 / 136 / 75) and the Methods totals (ΣDn 18,936, ΣDs 34,241). Slip in the source: Table 1 prints N = **15** for the accelerated set at DAF ≥ 15%; the sheets give 155 (typo; changes nothing; slip ledger at integration).

Adaptive count A = ΣDn − ΣDs·ΣPn/ΣPs over the accelerated genes polymorphic in each DAF class (pooled MK, as Table 1):
| row | reading | A | × G1 | side |
|---|---|---|---|---|
| R1 | DAF ≥ 60%, the 75 polymorphic genes (Dn 564, Ds 424, Pn 57, Ps 72; alpha 0.405) | **228** (gene bootstrap 95%: 112-323) | 1.20 (0.59-1.69) | critic at the point estimate; **interval straddles** |
| R2 | DAF ≥ 1% / 15% / 30% (N 182 / 155 / 136) | 449 / 377 / 384 | 2.0-2.4 | critic (lower DAF cut-offs include more genes; their alpha is biased low, not high) |
| R3 | alpha 0.405 × ΣDn of all 198 genes (1,262; mean 6.37 per gene vs genome 1.94) | 511 | 2.68 | critic (extrapolates alpha to genes with no DAF ≥ 60% polymorphism; critic-leaning) |
| R4 | Day-charitable ascertainment correction: (0.405 − 0.163) × 564, where 0.163 is GV's matched-rate "rapidly evolving" control (Table 1, DAF ≥ 60%) | 136 | 0.72 | Day |
| R5 | R4 at R1's lower bootstrap bound: 112.3 × 0.242 / 0.405 | 67 | 0.35 | Day |

Why R4 is the charitable reading (rule C): the accelerated genes were *selected* for an excess of human-branch Dn over Ds (Fisher p < 0.05), so their Dn carries selection noise while their polymorphism does not. That inflates MK alpha even without adaptation (winner's curse). GV built a control set matched on the human-branch dN/dS distribution, and its alpha (0.163) bounds that inflation from above. R4 is deliberately low: it also removes any real adaptation in the control set, which GV says exists ("some of these genes are evolving adaptively"). Critic's counter-reading: the accelerated set is 198 of 9,785 genes, the BS-test set (alpha 0.398 at N 78; overlap with the accelerated set 32 of 241) is not added, and no other gene's adaptive substitutions are counted, so any value here is a floor on the human coding count.

Predictions: P1 holds; P2 holds (ΣDn 1,262, inside 1,000-2,000); P3 holds (R1 228 inside 150-350; R3 511 > 2 × 190.6); P4 holds (R4 136 and R5 67 below 191). **C2 result: the accelerated-gene bound does not clear 191 under charitable assumptions.** It moves GV from "Day side" to "at the threshold": GV's own data put the human-branch count near 191 from 198 genes alone on the uncorrected reading.

### MINOR items
| # | Resolution |
|---|---|
| m1 / C5 (Boyko 36,138 vs 22,180) | Stated. The Methods give "36,138 nonsynonymous human-chimp differences" over 17.8 Mb; Table 1 is headed "observed fixed differences = 22,180". The paper does not reconcile them in the text read; 9.3% stays tied to 22,180 (22,180 − 20,113 = 2,067 = 9.3%). Post hoc alternative row on 36,138: N2 18,069, N3 29,621; 9.3% gives 1,680-2,755 (8.8-14.5x); alpha\* 1.05% (N2, G1), 0.64% (N3, G1), 0.54% (N3, G2). Q1 fails further. Boyko's conditional "more than 20%" (γ+ ≤ 5) added to the row label. No side changes. |
| m2 (Boyko CL) | Lower-CL row added: 599 / 982 (3.1x / 5.2x). Critic prediction re-scored: holds on Boyko's point estimate; at the lower CL Boyko falls below the registered 1,000 while staying above 191. |
| m3 (locator) | Fixed in Files: Q138 s8.6 p.15; Q130 core s2 p.4 (split tag); Q139 s7.3 p.13. |
| m4 (literature locators) | Section locators and fetch date added above; Q ids at integration. |
| m5 (Uricchio scope) | Both rows now say "divergence basis and linkage treatment not stated in the abstract". If 0.135 is before the ~25% linkage reduction, counts fall by ~25% (1,123-2,477; strong-only 314-694); side unchanged. |
| m6 / C4 (EK, Galtier) | EK rows labelled human-macaque, with the authors' "strongly downwardly biased" qualifier. EK and Galtier dropped from the Day bullet: Galtier's "notable exception of primates" bounds alpha below 0.5, not below ~1%; EK's "little evidence" is followed in the same abstract by "could be as high as 40%". Citing the first clause alone would be a **partial** reading. |
| m7 / D-N1 | Day-side prediction re-scored **fails as worded**. |
| m8 | "Two independent methods put" → "two estimators within the MK/SFS framework, on independent data, infer". |
| D3 | Critic prediction now reads "holds on Boyko (full text); Uricchio concordant, abstract only". |
| D4 | Both directions in the asymmetry: non-coding adaptation is uncounted (raises the human count); MK alpha includes weakly adaptive fixations (72% of Uricchio's alpha) that are near-neutral in pace. The strong-only row (419-925) stays above 191, so D4 narrows the margin without moving the side. |
| D5 | Galtier kept as cross-species context (small-Ne species have lower alpha; GV's Discussion says the same). Its limit is noted under m6/C4. |
| D6 | Added to the Interpretation: all estimates are model inferences; none observes human-lineage fixations directly. |
| C6 | Enard 2016 (same refresh; ~30% of adaptive amino-acid changes in the conserved proteome attributed to viruses) is context for a floor, not a count; it is not mapped. A non-coding human-lineage adaptive-substitution source is proposed as an RG-03 to-do at integration. |
| C7 | Q3 note added: "both sides" holds only if a null counts as a side; the "4-7x below" ratio is withdrawn. |

## Verdicts after fixes (R4-X1)
- **Scope (S, RH).** Scored: Q138 and the Q130 core, both dialectic. Q139 supplies the threshold. Nothing rhetorical scored.
- **Internal: `non-sequitur` (unchanged, set by R4-A2e).** This check computes no number Day states (R1 does not apply to his derivation), and rule N is not engaged here. The fix pass does not touch the internal axis.
- **Fidelity: `n/a` for Day** (Day cites none of these papers; nothing he relays is scored, rule U). For the audit's own reading of sources: GV's 0.2% was misused as a count (now withdrawn), and EK's first clause alone would be `partial`; both are corrected in this file.
- **External: `contested` (kept).** Reasoning:
  - Every bias-corrected estimate (Boyko full text, Uricchio abstract, EK's conditional 40%) is above 191 per lineage, also under each Day-favourable adjustment alone and under the compounded one (lowest 299, 1.57x). That is why the critic review proposed a lean toward `contradicted`, and this pass records the lean: **contested, leaning contradicted** for the coding-only per-generation reading.
  - It does not move to `contradicted` because: (a) the only full-text critic-side estimate is a model residual pooled over both lineages, and the compounded Day-charitable row needs only about 36% of it to be artefact for A2e to survive; (b) Uricchio is abstract only; (c) the C2 row, the critic review's named condition, clears 191 only at the uncorrected point estimate (228), not at its lower bootstrap bound (112) or after the ascertainment correction (67-136). Rule C and the instruction to move only on a clear clearance keep it at `contested`.
  - **What would move it to `contradicted`:** a full-text Uricchio (or another bias-corrected human-branch estimator, e.g. asymptotic MK or a DFE-alpha fit on human-branch divergence) confirming alpha above about 1% on the human lineage itself; or a human-branch-polarised bias-corrected count above 191 with an interval that excludes it; or a non-coding human-lineage adaptive count that alone exceeds ~191. **What would move it toward `supported`:** a bias-corrected human-branch alpha below ~1% with an interval excluding it, or evidence that Boyko's residual is mostly model artefact.
- **R1:** no verdict moves in this check. The pre-review "named disagreement" (0.2% vs 9-20%) is replaced by "bias-corrected estimators above alpha\* ≈ 1%; the only sub-threshold value is an uncorrected null; GV's accelerated genes sit at the threshold".

## Post hoc addendum: Uricchio 2019 full text
**Post hoc** because the abstract value (0.135) was already mapped above. Script `research/checks/a2e_alpha_uricchio.py`, committed with its predictions at **7d68de9** before its run; raw `results/raw/a2e_alpha_uricchio.out`. Source: Uricchio, Petrov & Enard 2019, Nat Ecol Evol 3:977-984, PMC6693860 (OA author manuscript), fetched 2026-10-11 (refresh-2026-10-11b-lit s3), sha256 `3e7c44cb...b865977`. All 9 quotes below verified as substrings of the local text. Not integrated; no claim, QUEUE, argmap or ledger edits.

**Is it human-branch?** Yes. Methods: "the number of human-specific fixed substitutions in coding sequences since divergence with chimpanzees", "identified by parsimony based on alignments of human (hg19 assembly), chimpanzee (panTro4 assembly) and orangutan (ponAbe2 assembly) coding sequences". Polymorphism: 1000 Genomes, "all 661 samples with African ancestry". This is the human lineage since the chimp split, the same interval as A2e's 191.

**Is it bias-corrected?** Yes, on both axes the paper names. Intro: "Deleterious polymorphism effectively makes the test overly conservative" (the bias that depresses naive MK; the aMK baseline gives 0.076). ABC-MK further models weakly beneficial alleles and background selection: "our method nearly doubles the estimated human adaptation rate (to α = 0.135)". Table caption: "Values in parentheses represent the area of 95% highest posterior density".

**Results** (G1 = 190.6, G2 = 158.8; denominators N1-N3 as in the main table; alpha\* 0.65-1.75%):
| row | alpha | count range over N1-N3 | x G1 | side |
|---|---|---|---|---|
| point | 0.135 | 1,497-3,303 | 7.9-17.3 | critic (identical to the abstract-only row) |
| lower 95% HPD | 0.096 | 1,065-2,348 | 5.6-12.3 | critic |
| **lowest Day-charitable, any effect size:** lower HPD x 0.75 (linkage haircut; N2) | 0.072 | **798** (N2); 1,057-1,761 on the others | **4.19** (4.2-9.2) | critic |
| strongly adaptive only, point (Day-charitable: weak variants near-neutral in pace) | 0.041 | 455-1,003 | 2.4-5.3 | critic at the point estimate |
| strongly adaptive only, lower HPD | 0.0 | 0 | 0 | **not excluded** |
| paper's own count, NS = 29,925 (not used for the verdict) | 0.135 / 0.096 | 4,040 / 2,873 | 21 / 15 | critic |
| VIP subset alone (own count 6,249) | 0.224 / 0.17 | 1,400 / 1,062 | 7.3 / 5.6 | critic; VIP strong-only lower HPD (0.018) gives 112 (0.59x) |

The lower HPD bound (9.6%) is 5.5 times alpha\*max (1.75%). The lowest any-effect-size row, 798, is 4.2 times 191 (5.0 times G2).

## Scoring of the post hoc predictions
| ID | Prediction | Result | Score |
|---|---|---|---|
| P1 | human-branch and bias-corrected; quotes verify | both hold, 9/9 quotes | holds |
| P2 | lower HPD / alpha\*max >= 5; compounded lowest >= 3.5 x G1 | 5.5; 4.19 | holds |
| P3 (Day) | strong-only at lower HPD is 0; strong-only point >= 450 on N2 | 0; 455 | holds: a strong-only reading is a point clearance, not an interval clearance |
| P4 (Day) | the paper's NS = 29,925 exceeds N1-N3 and is unreconciled | 29,925 vs 11,090-24,463; GV counted 18,936 on 9,785 genes; the paper's gene set (Ensembl v73, human-chimp-orangutan reciprocal hits, Blat identity >= 60%) differs and the text read does not reconcile them | holds; own-count rows reported only |
| P5 | move proposed, with limits | see below | holds |

## Proposed verdict move
The milestone-13 condition is met: a full-text, bias-corrected, human-lineage alpha, with a 95% HPD lower bound (9.6%) well above 1%. None of the four pre-registered blockers applies. **Proposed: A2e external `contested, leaning contradicted` to `contradicted`, for the coding-only, any-effect-size, per-generation reading.** Internal (`non-sequitur`) and fidelity (`n/a`) unchanged. The earlier reason for holding at `contested` was (a) Boyko being the only full-text estimate (a pooled residual) and (b) Uricchio being abstract only; both fall away. Reason (c), the GV accelerated-gene bound, was a different test and is untouched. Not asserted: that the strong-only reading fails, or that Day's other A2e arguments fail.

## Who this helps
- **Critic side:** a second, independent, human-lineage-specific, full-text estimator lands 4.2-17x above the flip after every adjustment applied here; unlike Boyko it is not pooled over both lineages, and its HPD excludes the threshold by a factor of 5.5. The VIP subset (6,249 fixations) clears 191 by itself even at its lower HPD.
- **Day side:**
  - Strong-only adaptation (4% alpha) clears 191 only at the point estimate; its HPD includes 0, and for VIPs the strong-only lower bound gives 112, below 191. Day's ceiling counts beneficial fixations of any size, but if the reader restricts to strong ones the flip is not interval-secure.
  - 72% of Uricchio's alpha is weakly adaptive, which Day can argue is not what a rate ceiling on "beneficial fixations" meant.
  - The estimate is a model inference (ABC-MK); no fixation is observed directly (D6 stands).
  - The paper's own NS (29,925) is unreconciled with the other denominators, and Uricchio notes its estimate is "not directly comparable" with earlier ones because of the larger gene set.

## Caveats
- Whether 0.135 is net of the ~25% linkage reduction is not settled by the text read; the 0.75 haircut covers it either way.
- The ABC-MK model inherits demographic and BGS model assumptions (the paper tests seven confounders in its own robustness section; not re-audited here).
- Counts are coding-only lower bounds; denominators are the audit's (N1-N3), not the paper's.
- The "Whole-egoism" row label in the saved copy is a source-copy artefact; read as the whole gene set.
- Combined light review pending; integration (claims, argmap, ledgers) not done.

## Review resolution (Uricchio addendum)
Answers `REVIEW-R4-A2e-uricchio-combined.md` (0 BLOCKER, 2 MAJOR, 6 MINOR, 3 NOTE). No script or raw output was changed (pre-registered); corrections are here. Not integrated.

**MAJOR-1 (scope of the label): accepted.** The proposed external label is now scoped. Exact text for the claim file:

> A2e external **`contradicted` (scoped)**: for rate_human <= 1/G_f read as a per-generation count of adaptive fixations of any effect size, coding-only, on model-inferred alpha. Basis: Uricchio 2019 lower 95% HPD (alpha 0.096) gives 4.2x the flip (798 vs 191) on the audit's most Day-charitable denominator (N2 11,090, after a 25% charity haircut) and 11-21x on the paper's own 29,925 base (2,873 at the lower HPD, 15x; 4,040 at the point, 21x; 11x after the haircut); Boyko lower CL 599; aMK baseline (alpha 0.076) 4.4x (843 on N2, arithmetic only). Strong-effect-only and fitness-weighted readings stay **`contested`** (strong-only point 455 = 2.4x on N2, lower HPD 0.0). Day's other A2e arguments are not decided.

This also answers MINOR-2 (both bases reported, 4.2x vs 11-21x, so 798 is not read as the paper's estimate) and MINOR-4 (the headline 4.2x is labelled "after a 25% charity haircut, lower HPD, smallest denominator"). Support for model uncertainty: three estimators (ABC-MK, aMK baseline, Boyko) would all need a ~4-fold error in the same direction to reach 191; the HPD itself covers parameter, not model, uncertainty.

**MAJOR-2 (trigger not self-executing): accepted.** Plainly: milestone 13 named a source ("a full-text Uricchio"), not a numeric trigger, and its "above about 1%" did not say point or interval. The four blockers in the script were written by the same author who then scored them, after the abstract value (0.135) was known; the statement above that "the milestone-13 condition is met" is therefore a judgement, not a mechanical result. The claim-file comment elsewhere uses a different formulation ("a count > 191 with interval excluding it"), and an earlier review said the move waits on GV (C2) or a full-text Uricchio as "a flagged lean". **The verdict move was PROPOSED; the owner accepted the two-reading scoping on 2026-10-11 and it is integrated (claim A2e external `contradicted`, scoped; marker removed).**

*Owner summary (neutral):* Uricchio, Petrov and Enard 2019 estimate, for human-specific coding substitutions since the chimpanzee split and with a model that corrects for slightly deleterious and weakly beneficial variants, that 13.5% of nonsynonymous fixations were adaptive (95% HPD 9.6-17%). Even with every Day-charitable choice stacked (lowest bound, a 25% haircut, the smallest audit denominator), this gives about 798 adaptive fixations, 4.2 times the 191 that A2e's flip requires; on the paper's own count it is 11-21 times. The weak points are that the figure is a model inference rather than an observed count, that the strong-effect-only component (4%) has an interval including zero so Day's "ceiling on what evolution can accomplish" read as strong sweeps is not excluded, and that the trigger and blockers were set by the same author who applied them. The decision for you: accept the scoped label above (the any-effect-size count reading is contradicted, other readings remain contested), keep `contested, leaning contradicted` until the GV genome-wide total is extracted, or require a different trigger.

**MINOR-1 (post hoc disclosure): accepted; corrected.** The script docstring says the full-text method, Table 1 and the study's own counts were unknown at registration. That is wrong: the docstring itself quotes the method sentences, the strong-only HPD (0.0-0.13), VIP 0.224, NS = 29,925, the 4,040 point and the "~799" figure. Correct statement: the full text and Table 1 were read before registration; only the script run was pending. P1-P4 were not blind forecasts, and scoring them "holds" shows only that the script prints what the docstring said (as B9 MINOR-4). The P1-P5 scoring table carries no evidential weight beyond arithmetic and classification checks; the real tests were the earlier abstract-only mapping and the choice of blockers.

**MINOR-3 (GV, C2): accepted.** The GV accelerated-genes bound (67-228, straddling 191) counts fixations in a subset of genes (accelerated-gene set), so it is a lower bound compatible with a larger genome-wide total, not a rival total. The claim comment must say so. If the GV figure were instead a total for the human branch, two human-branch sources would disagree by about 3.5x and the move would need the owner (included in the owner decision above). The reviewer's candidate reconciliation of the denominator gap (GV 18,936 on 9,785 genes scaled to the paper's 17,028 genes: 18,936 x 17,028 / 9,785 = about 32,950, close to 29,925) is arithmetic on an assumed proportional-to-gene-count scaling; **unverified**, offered as a candidate explanation only, and it makes N1-N3 lower bounds for the whole gene set rather than rivals. P4's "unreconciled" stays.

**MINOR-5 (strong-only fair reading): accepted.** Recorded as the strongest Day-side point, and the reason for the scope clause. The VIP strong-only lower HPD (0.018 x 6,249 = 112 < 191) is a **subset** (6,249 of 29,925 fixations) compared with a genome-wide flip, so it is not like for like; it is a Day-side datum only that this subset alone does not clear. The "Who this helps" Day bullet is amended accordingly: read "for VIPs alone the strong-only lower bound gives 112 (subset only; non-VIP strong component, alpha_S 0.042, is additional)".

**MINOR-6 (flip survives more than shown): accepted, no change to numbers.** The compounded 798 uses the smallest denominator, the lower HPD and an extra haircut, each a Day-charity, and coding-only counts exclude non-coding adaptation, so `contradicted` for the scoped reading is conservative. Critic-side caution recorded by the reviewer: the strong-only scope clause gives Day more than his quoted formal statement (a count) needs, and the strong/weak split is the least identified output (alpha_W HPD 0.0-0.21); the clause is kept because the interval does include 0 and no size threshold has been quoted from Day either way.

**NOTE-1/2/3:** acknowledged (sub-second local script, no `.host`; "Whole-egoism" is a copy artefact; no rescue changes the verdict for the formal count statement).

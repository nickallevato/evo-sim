# R4 GAP05: slightly deleterious fixations on the human lineage, from a sourced DFE (Kimura)

Tier: low-stakes (GAP-05 is not a `hierarchy.yaml` node; B9 is `load_bearing: false`), so one combined review is due. Script: `research/checks/gap05_slightly_deleterious.py` (pre-registered, committed before the run; local, one process, numpy, <10 s). Output: `raw/gap05_slightly_deleterious.out`. Not integrated. **Fix pass 2026-10-11** (answers `REVIEW-R4-GAP05-combined.md`): s convention resolved to Reading A; post hoc sensitivity in `gap05_posthoc.py` (separate commit, run after; output `raw/gap05_posthoc.out`); see "Post hoc sensitivity" and "Review resolution" at the end. The pre-registered script and its numbers are unchanged.

**Disclosure.** The DFE bin shares (28-33% |s| < 1e-4; 15-17% 1e-4..1e-3; 50-57% >= 1e-3) were summarised in chat before the script was written, so the DFE inputs were not blind. The Kimura integration, counts, cost and dN/dS comparison were pre-registered before the run.

## Question and inputs
GAP-05 (`ledgers/gaps.md`): how many slightly deleterious (|N_e s| ~ 1) mutations does a drift account imply fixed on the human lineage since the chimp split, and what fitness cost? The old gap text had only a rough "upper-end scenario" (about 1e5 substitutions, log-fitness decline 1-10) with Boyko's nonsynonymous share applied to all constrained sites.

- DFE: Kim, Huber & Lohmueller 2017 Table 3 (new nonsynonymous mutations; s derived as gamma / (2 N_A), N_A from theta_S = 4 N_A mu L_S with mu = 1.8e-8 for the two Boyko-comparison rows and N = 7,778 diploids for the Boyko reanalysis; the "N = 10,000" rescaling in the Figure 1 legend applies to Eyre-Walker 2006 only), bins 0-1e-5, 1e-5..1e-4, 1e-4..1e-3, 1e-3..1e-2, >1e-2. Boyko row 0.183 / 0.096 / 0.147 / 0.219 / 0.355; 1000 Genomes gamma row 0.217 / 0.112 / 0.169 / 0.243 / 0.259 (`refresh-2026-10-11b-lit.md`, `quotes-literature.md`). Within-bin shapes are the audit's assumption.
- mu = 1.2e-8 (1.1e-8..1.5e-8), T = 252,000 generations (Day), h = 0.5, genic Kimura u(s, N_e) (code copied from `hf_followups.py`, validated there against per-site WF). Nonsynonymous sites 2.78e7 per haploid genome (R4-L1 raw, V0 ALL; repo-derived, one transcript per gene). Neutral-equivalent nonsynonymous mutations per lineage: mu x sites x T = **84,035**. Observed nonsynonymous differences per lineage about 64,700 (Nd/2 from R4-L1, human + chimp 129,479).
- **s convention (resolved, Reading A).** Boyko 2008 Methods: "We assume s and 2s are the selective disadvantage of heterozygotes and homozygous mutants and infer the DFE based on the scaled selection parameter, γ = 2Nes." Kim 2017 Methods: gamma = 2 N_A s, "like the method of Boyko et al. (2008), our method assumes additive selective effects and should be interpreted as averaging of selection over all heterozygotes and genetic backgrounds" (quotes in `quotes-literature.md`). So s is the heterozygote disadvantage, a fixation (homozygote) costs 2s, selection is additive, and N_A is in diploids. Kim does not write the word "heterozygote" for s; the reading rests on the shared Boyko parametrisation plus additivity. Reading B (|s| = homozygote effect) is not supported by either text; its numbers are in the footnote under the table and in `raw/gap05_slightly_deleterious.out`.

## Results (expected deleterious nonsynonymous fixations on one lineage; cost = multiplicative sum, no compensation)
| Reading | DFE row | N_e | predicted dN/dS | fixations | log-fitness decline | fitness ratio |
|---|---|---|---|---|---|---|
| A | Boyko | 1e4 | 0.212 | 17,831 | 0.368 | 0.69 |
| A | Boyko | 2e4 | 0.175 | 14,666 | 0.204 | 0.82 |
| A | Boyko | 57,143 (inconsistent, see below) | 0.108 | 9,091 | 0.079 | 0.92 |
| A | 1000G | 1e4 | 0.251 | 21,067 | 0.431 | 0.65 |
| A | 1000G | 2e4 | 0.206 | 17,350 | 0.240 | 0.79 |
| A | 1000G | 57,143 (inconsistent) | 0.128 | 10,773 | 0.094 | 0.91 |

[^B]: Reading B (not supported by the texts; shown only because the pre-registration carried it): N_e 1e4 gives dN/dS 0.25 / 0.29, 20,900 / 24,600 fixations, decline 0.37 / 0.43 (Boyko / 1000G); fixations with |s| >= 1e-4 are 780-897 instead of 99-114. Full rows in the raw output.

The N_e = 57,143 rows apply a DFE whose s values were computed from N_A about 7.8-10k (and mu 1.8e-8) to a population of a different size; that mixes two N's and is internally inconsistent. They are kept only as the pre-registered scenario, not as a result about a large-N_e lineage. Per-generation decline 3e-7 to 1.7e-6. Sensitivities (Reading A, N_e 1e4): mu 1.1e-8..1.5e-8 gives 16,300-26,300 fixations and decline 0.34-0.54; bin 0-1e-5 log-uniform (1e-7..1e-5) lowers decline to 0.29-0.34 and leaves dN/dS 0.22-0.26. **Headline decline at N_e 1e4: 0.29-0.43** (bin-0 shape, the least constrained part of the DFE; Kim: estimates for |s| < 1e-4 "are less accurate").

**Where the count and cost sit (Reading A, N_e 1e4, Boyko).** Bin 0-1e-5: 13,909 fixations (f = 0.90 of neutral), cost 0.134. Bin 1e-5..1e-4: 3,823 (f = 0.47), cost 0.209. Bin 1e-4..1e-3: 99 (f = 0.008), cost 0.025. Bins >= 1e-3: none. So **99-114 fixations have |s| >= 1e-4**, and about 99% of the count and 93% of the cost come from |s| < 1e-4 (|N_e s| below 1). Mean cost per fixation 1e-5 to 5e-5. The "slightly deleterious" class that drift fixes is mostly the effectively neutral end.

**Noncoding: unsourced DFE.** No Ns ~ 1 share for constrained noncoding sites was found. Constrained noncoding sites: 0.082 x 3.1e9 - 3.6e7 coding = 2.2e8 (1.8e8-2.5e8 over Rands 7.1-9.2%). Bracket only: if a fraction q of their mutations had Boyko's 1e-5..1e-3 conditional DFE, q = 0.05 / 0.15 / 0.30 adds 6,300 / 19,000 / 38,000 fixations and 0.38 / 1.13 / 2.26 log-fitness decline (8.2%; ranges 0.32-0.43, 0.95-1.29, 1.9-2.6 across Rands CI). The q values are not sourced; this shows only that the answer is dominated by an unmeasured number, because the noncoding target is 6x the coding one. Within this unsourced bracket only, the noncoding addition could equal or exceed the coding cost at q about 0.05 or above; q is unmeasured and nothing outside the bracket relies on it.

## Scoring against the pre-registered bands
| Band | Outcome |
|---|---|
| DB1 (Day): coding decline >= 0.05 at N_e 1e4, both rows/readings | **Hit** (0.37-0.43) |
| DB2 (Day): >= ln 3 at N_e 1e4 or 57,143 | **Miss on the pre-registered base** (max 0.43; coding only). Base-dependent: post hoc, divergence-calibrated bases give 0.81-1.22 at N_e 1e4 and 1.03-1.73 at 7,778, so DB2 flips above ln 3 for some rows (see Post hoc sensitivity) |
| DB3 (Day): >= 1,000 fixations with |s| >= 1e-4 | **Miss** (99-114) |
| CB1 (critic): predicted dN/dS 0.16-0.34 at N_e 1e4 | **Hit** (0.21-0.25 in Reading A, inside the observed 0.21-0.27). The band was set around the observed value with the DFE shares already known, so CB1 is a weak test (MINOR-4) |
| CB2 (critic): deleterious fixations < 50% of neutral-equivalent | **Hit** (21-25%) |
| CB3 (critic): decline < ln 3 at N_e 1e4, 2e4 | **Hit** (<= 0.43) |
| Audit point: dN/dS 0.17-0.30; fixations 11k-26k; decline 0.3-1.5; N_e 57k lower | **Hit** on all four (decline 0.37-0.43 is in the low part of the band) |

## What it shows
1. **Counts.** On a sourced DFE the coding-only drift account fixes about 15,000-21,000 (range 9,000-26,000 across rows, N_e, mu, reading) slightly deleterious nonsynonymous mutations per lineage, i.e. 17-30% of the pre-registered neutral-equivalent base (mu T = 1.2e-8 x 252,000, which sits about 2.8x below the observed synonymous divergence; see Post hoc sensitivity: on a divergence-calibrated base the counts are 2-3x larger, 40-65k). It is 5-10x below the old rough "1e5" figure only on the pre-registered base.
2. **dN/dS consistency.** The Kim DFE, with no free parameter fitted to divergence, predicts human-chimp dN/dS 0.21-0.25 (Reading A) at N_e = 1e4, matching R4-L1's 0.21-0.27 (V0 ALL 0.27, O121 0.21, filtered 0.234-0.281). Caveat: the observed ratio also contains the Boyko 10-20% adaptive amino-acid share, which would raise the observed side; and a larger N_e (5.7e4, Day's implied) predicts only 0.11-0.13, which does not match the observed 0.21-0.27. That row is also internally inconsistent (s derived from N_A about 8-10k), so it says the Kim s values do not transfer to a 57k population, not that the large-N_e reading is independently refuted.
3. **Cost.** Uncompensated coding cost at N_e 1e4 is a log-fitness decline of 0.29-0.43 on the pre-registered base (fitness ratio 0.65-0.75; 0.08-0.24 at the inconsistent larger N_e rows), about 1e-6 per generation. On that base it is not a meltdown (none reaches ln 3), and it is not "extinction within centuries" (B9). But it is not nothing: 31% (Boyko) to 35% (1000G) lower absolute fitness at N_e 1e4 if selection is hard and uncompensated. On a divergence-calibrated base the same DFE gives 0.8-1.2 (N_e 1e4), straddling ln 3; the base matters more than the DFE row.

## Who this helps
- **Day / allies (Hossjer HO-11).** The premise that drift fixes slightly deleterious mutations along the human lineage is now numerically supported from a published DFE, not just asserted: about 17,000-21,000 coding fixations, a 31-35% uncompensated fitness decline at N_e 1e4 on the pre-registered base, and larger (up to ln 3 and beyond) on a divergence-calibrated base. B9's best point (GAP-05) is real in its premise. The noncoding side is open and unsourced; no critic has put a number on it.
- **Critics.** The same DFE reproduces observed dN/dS without any appeal to selection being off, so the standard model accounts for the coding data; the count is modest (a fifth to a quarter of neutral), 99% of it with N_e |s| below 1, and the cost is about 1e-6 per generation, about 2 orders below the per-generation rate implied by the "centuries" claims (about 1.7e-4, ln 0.5 over about 4,000 generations) and about 5 orders below the "9 generations" claim. Compensatory mutation, soft selection and weak stabilising selection (Charlesworth 2013, Kondrashov 1995) are untested here and can only lower the cost.
- **Critics, a further point (MINOR-9).** A monotone decline of 0.3-0.4 at constant N_e over 252,000 generations is not an equilibrium prediction: at mutation-selection-drift balance the deleterious fixation rate is offset by back and compensatory fixations, so the count of deleterious substitutions is not the net fitness change.
- **Both.** The result does not settle whether the decline is real: the model has no back or compensatory mutation, which is the critics' whole answer, and the DFE for nearly neutral bins is the least certain part of the data.

## Caveats
1. s convention resolved to Reading A (heterozygote, additive; see Question and inputs). The DFE s values are absolute and conditional on mu = 1.8e-8 and N_A about 7.8-10k (and the 1.5e-8 rows on the exome mu); the script uses mu 1.2e-8 for the neutral base, a mismatch with the DFE's own mu that the post hoc grid covers.
2. DFE in the nearly neutral bins (|s| < 1e-4) is poorly constrained by polymorphism (Kim): the 0-1e-5 bin in Table 3 is a share of a fitted parametric DFE, not a measured one. 2Ns for such mutations is below 1; the within-bin shape is assumed (alt run shown).
3. No compensatory mutation, back mutation, epistasis (synergistic epistasis would purge faster; compensatory would offset), linkage/BGS, or demographic history. N_e is constant at each value; the real lineage had a larger ancestral N_e (R4-B4a), which lowers fixations. The cost shown is an upper-end for coding.
4. Mutation rate applied to nonsynonymous sites as a single mu; CpG and mutation spectrum not modelled. N sites come from R4-L1's one transcript per gene (undercounts isoforms).
5. Log-fitness decline is not a demographic decline unless selection is hard (cf. HF-a): under soft/relative fitness the cost is not lost absolute fitness.
6. Noncoding DFE unsourced; bracket only.
7. The base mu x T under-predicts observed divergence by about 2.8x on synonymous sites (post hoc section); every count and cost headline scales with the base, dN/dS does not.
8. The dN/dS match is evidence for the DFE, not for any particular cost: a model with mostly neutral and mostly strong mutations gives the same dN/dS.

## Proposed verdict moves (not applied; integration pending)
- **GAP-05:** open to "computed on a sourced coding DFE; noncoding unsourced; compensation untestable". Premise supported; collapse not.
- **B9 external (scoped):** stays `contradicted` on the extinction-within-centuries wording; add that GAP-05 (credited to Day as best point) is quantified: coding decline 0.08-0.43 (about 1e-6/gen), not a collapse.
- **HF open item (HF-d):** a **supplementary proposal beyond the pre-registered mapping** (the pre-registration lists no HF-d move): the coding scenario from a sourced DFE (0.29-0.43 at N_e 1e4 on the pre-registered base; 0.8-1.2 on a divergence-calibrated base) supplements, and does not replace, the HF S1 rows (which use a different s-distribution; U_d = 1 gives 0.82 in `R4-HF.md`). The coding figure of 0.33 mutations per genome per generation (sites x mu) is a nonsynonymous mutation rate including neutral and nearly neutral classes, not a deleterious rate. The noncoding row remains unsourced.
- Linked claims by grep: H5/HO-11 (fitness declines): premise gets a numeric anchor; no verdict change. V20 row in R5-draft: add the coding figure.

## Post hoc sensitivity (`gap05_posthoc.py`, committed 2d134d0 before its run; output `raw/gap05_posthoc.out`)
Reading A throughout. Base multiplier k scales mu x sites x T. "Calibrated" k = observed synonymous differences per lineage (R4-L1 V0 ALL, Sd/2 = 70,926) over the model's mu x S x T (25,134) = 2.82. Log-fitness decline (ln 3 = 1.099), N_e 1e4 / N_e 7,778:

| Base (k) | Boyko 1.8e-8 | 1000G 1.8e-8 | ESP | 1000G 1.5e-8 |
|---|---|---|---|---|
| mu 1.2e-8, pre-reg (1.00) | 0.37 / 0.47 | 0.43 / 0.55 | 0.42 / 0.53 | 0.48 / 0.61 |
| mu 1.5e-8 (1.25) | 0.46 / 0.58 | 0.54 / 0.68 | 0.53 / 0.66 | 0.60 / 0.77 |
| mu 1.8e-8, the DFE's own mu (1.50) | 0.55 / 0.70 | 0.65 / 0.82 | 0.63 / 0.79 | 0.72 / 0.92 |
| calibrated, 22% ancestral polymorphism removed (2.20) | 0.81 / 1.03 | 0.95 / 1.20 | 0.93 / 1.16 | 1.06 / 1.35 |
| calibrated, 14% removed (2.42) | 0.89 / 1.13 | 1.05 / 1.33 | 1.02 / 1.28 | 1.17 / 1.49 |
| calibrated, full (2.82) | 1.04 / 1.32 | 1.22 / 1.54 | 1.19 / 1.49 | 1.36 / 1.73 |

(The k = 1.5 row coincides with mu 1.8e-8 by construction: 1.8/1.2.) Predicted dN/dS is base-independent (0.21-0.28 at N_e 1e4; 0.23-0.29 at 7,778). k needed for ln 3 at N_e 1e4: Boyko 2.99, 1000G 2.55, ESP 2.60, 1000G-1.5e-8 2.28; at N_e 7,778: 2.35, 2.01, 2.08, 1.79. Bin-0 log-uniform at k = 2.82, N_e 1e4: 0.83-1.09 (below ln 3 in all rows). On the calibrated base the predicted nonsynonymous fixations are 50-65k, i.e. 0.78-1.01 of the observed 64,740 per lineage (pre-registered base: 0.28-0.36), which leaves little room for the 10-20% adaptive share and is a sign that k = 2.8 is an upper end.

**Pre-registered post hoc predictions scored.** Linear in k: hit. Boyko about 1.04 and 1000G about 1.2 at k = 2.82: hit. Both below ln 3 at k = 2.2: hit (0.81, 0.95 at N_e 1e4). ESP between Boyko and 1000G: hit. 1.5e-8 row within +/-15% of 1000G 1.8e-8: hit (+12%). Calibrated fixations within 25% of observed: hit. **N_e 7,778 gives 5-15% larger decline: miss, it is 27%** (0.47 vs 0.37 Boyko; 0.55 vs 0.43 1000G).

**How DB2 depends on the base.** On the pre-registered base (Day's T and a pedigree mu) it is a Miss in every row. At N_e 1e4 the outcome flips above ln 3 only in the full-calibration (k = 2.82) 1000G, ESP and 1000G-1.5e-8 rows and at k = 2.42 for the 1000G-1.5e-8 row; Boyko stays below (1.04). At N_e 7,778 (the DFE's own N for the Boyko reanalysis) it flips from k about 2.0-2.4. So DB2 is a Miss on one base and a Hit or near-Hit on another; the answer is "conditional on the base", not "no".

**Which base is principled.** The two answer different questions. (1) *Does Day's claim hold on Day's own inputs (T = 252,000, mu = 1.2e-8)?* Then the pre-registered base is the only consistent one, and the answer is a decline of 0.29-0.43 at N_e 1e4. (2) *What did the actual human lineage accumulate?* Then the base should reproduce observed divergence. The repo's own account (GAP-07b/c, `ledgers/gaps.md`) is that 14-22% of human-chimp differences are ancestral polymorphism sorted into a lineage, which the raw 2.82 includes; removing it gives k about 2.2-2.4. The remaining excess (CpG hypermutability concentrated in coding sites, and the tension between a pedigree mu and a phylogenetic clock, i.e. mu or T) is not resolved here. On question (2) the better-supported range is therefore k about 2.2-2.4 (decline 0.8-1.1 at N_e 1e4, 1.0-1.3 at 7,778), which sits at or around ln 3, not clearly below it. Neither base settles the compensation question.

**N_e 57,143.** Flagged inconsistent (s derived from N_A about 7.8-10k). Even so, on the calibrated base it gives 0.22 / 0.26 (Boyko / 1000G), far below ln 3.

## Review resolution
Review: `REVIEW-R4-GAP05-combined.md` (0 BLOCKER, 2 MAJOR, 9 MINOR, 2 NOTE).
- **MAJOR-1 (s convention; N = 10,000 misattribution; N_e 57,143 inconsistent): resolved.** Reading A adopted with the Boyko 2008 and Kim 2017 Methods quotes (added to `quotes-literature.md`, verified verbatim against the saved text); Reading B moved to a footnote. The "rescaled to N = 10,000" wording is corrected: that sentence is the Figure 1 legend and covers Eyre-Walker 2006 only; Table 3 s comes from N_A (theta_S = 4 N_A mu L_S, mu 1.8e-8 for the Boyko-comparison rows, N = 7,778 for the Boyko reanalysis, mu 1.5e-8 elsewhere). The 57,143 row is flagged internally inconsistent. The ESP and 1.5e-8 rows are in the post hoc grid. The pre-registered script and docstring are unchanged (the docstring's "N = 10,000" wording is wrong and is corrected here, not there).
- **MAJOR-2 (mu x T undershoots observed divergence; DB2 depends on base): resolved by post hoc sensitivity.** Table and base discussion above; the calibrated base can flip DB2, the question-(2) base k about 2.2-2.4 sits at about ln 3. The caveat and What-it-shows sections now state that counts, cost and "5-10x below 1e5" are conditional on the pre-registered base.
- **MINOR-1:** "35% lower" now "31% (Boyko) to 35% (1000G)"; "30%" replaced.
- **MINOR-2:** "3 orders" replaced by per-claim "about 2 orders (centuries) to about 5 orders (9 generations)".
- **MINOR-3:** ESP, 1000G-1.5e-8 rows added post hoc (LuCamp discrete not run: it is a non-gamma bin shape with a wide CI; named as omitted). They raise the pre-registered-base decline to 0.42-0.48 (N_e 1e4).
- **MINOR-4:** CB1 annotated as a weak test (band centred on the observation with shares known); "independently disfavours the large-N_e reading" dropped.
- **MINOR-5:** headline decline now 0.29-0.43.
- **MINOR-6:** HF-d move relabelled a supplementary proposal beyond the pre-registered mapping, "supplements" not "replaces", and the not-like-for-like points (different s-distribution; 0.33 is a nonsynonymous mutation rate, not a deleterious rate) stated. Other moves unchanged.
- **MINOR-7:** acknowledged; the Kimura code is reused from `hf_followups`, with only 2N u(0) = 1 and one spot value (0.0746) checked here; not an independent validation.
- **MINOR-8:** the noncoding "could equal or exceed" sentence now sits inside the labelled unsourced bracket with "q is unmeasured"; the What-it-shows and Day paragraphs no longer carry it.
- **MINOR-9:** the equilibrium point (deleterious substitution count is not net fitness change) added to the Critics paragraph.
- **NOTE-1:** both quotes with locators added (Boyko Methods and Discussion; Kim Methods "Estimating s from 2Ns" and Discussion); the write-up states that Kim does not use the word "heterozygote" for s.
- **NOTE-2:** no `.host` file for local runs under 10 s; the post hoc output is also local (`raw/gap05_posthoc.out`).
- **Steelman-Day/critic sections:** Day's calibrated-base and N_e < 1e4 points are now computed (above); the critic's hard-selection and stationarity points are carried in caveats 3 and 5 and the Critics paragraph.

**For the owner.** (a) Decide whether the headline for GAP-05 states the pre-registered figure (0.29-0.43) or the calibrated range; the draft keeps the pre-registered one as the headline and gives the calibrated range beside it. (b) The pedigree-mu versus clock tension (why mu x T is 2.8x low in coding sites) is not resolved by this check.

**Integration (2026-10-11, owner rule RD):** integrated into the claim files, ledgers and argmap as reading-dependent verdicts (value = reading most charitable to the speaker; all readings in the claim files Readings tables). See QUEUE item 15.

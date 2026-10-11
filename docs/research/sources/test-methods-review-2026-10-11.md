# Review of proposed test methodologies (2026-10-11)

Scope: every test or empirical method that either side has proposed, or that the audit itself relies on, as a way to settle the dispute. Method: quotes are from the repo's quote files (ids given; locators there); literature is cited from Europe PMC records fetched 2026-10-11 (`sources/raw/refresh-2026-10-11/epmc*/`, gitignored). **Every literature item below was read at abstract level only** unless marked otherwise; full texts were not read, so "known biases" are the ones stated in those abstracts or in the repo's own checks, and anything beyond that is marked *(general knowledge, not fetched)*. No verdict in any claim file is changed by this document. Verdict vocabulary here: **valid** (a test that can discriminate), **partial** (informative, but cannot settle the question alone), **invalid as a test** (cannot discriminate as used), **untested** (design exists, no run). Rule RH applies: rhetoric around a proposal is not scored; only the method is.

## Summary table

| # | Method | Proposed by | Measures | Discriminates the sides? | Verdict |
|---|---|---|---|---|---|
| 1 | LTEE as a benchmark for fixation rate (generations per fixation) | Day (Q85, Q08) | Substitutions per generation in E. coli under lab selection | Only after scaling to primates (Dembski's own question, DE-01) | partial |
| 2 | Pedigree mu versus phylogenetic k across species | Day (Q69) | Whether per-generation substitution rate equals mutation rate | Yes for the clock identity; not for selection versus drift | valid (for its own target) |
| 3 | Whole-genome alignment fixation counts (T2T, Progressive Cactus) | Day (Q171, Q179), Yoo 2025 | How many differences exist and where | Counts yes; cause (selection, drift, other) no | partial |
| 4 | Mesa / overdispersion tests on alignment windows (FM) | Day (Q171) | Clustering of differences in windows | Possibly, but no code, window size or null released | untested |
| 5 | dN/dS recomputation on all genes versus the curated 13,454 (new) | Day (Q172-Q177) | Average nonsynonymous/synonymous ratio | The two-gene-set design is valid; the inference "selection is not primary" is not | partial |
| 6 | Ancient-DNA zero-fixation count (1240k AADR) | Day (Q52) | Allele-frequency changes over ~7 ky in an ascertained SNP panel | Weakly (panel, power, window) | partial |
| 7 | Selective turnover coefficient d from aDNA time series | Day (Q22) | An assumed overlap/turnover parameter | No (Hancock: not a selection coefficient; dropped in MITTENS 3.0) | invalid as a test |
| 8 | Sweep-signature absence (EHH, iHS, SDS, ML scans) | Day (A6, Z18452504 s4.3) | Count of detectable sweeps | Only if scan power and soft-sweep modes are modelled | partial |
| 9 | McDonald-Kreitman / alpha estimates | Hancock/critic side and the audit (RG-03, R4-A2e-alpha) | Fraction of fixed nonsynonymous differences that were adaptive | Yes for the 191-substitution threshold if bias-corrected | partial (valid in principle) |
| 10 | Forward simulation of rate limits (Haldane cost, hard/soft mix, truncation) | Audit (R4-H8, R4-HF); Hancock (GG-26); Nunney 2003 | Sustainable substitution rate given h, R, s, K | Yes conditional on h; h is unsourced | partial |
| 11 | Estimating hardness h in humans (new, section below) | none yet; audit proposal | Share of selection that depends on absolute fitness | Would settle the H branch scope | untested |
| 12 | Ancient-DNA and polygenic selection scans (Mathieson, SDS, polygenic scores) | Critic-side literature | Frequency shifts, polygenic score shifts | Rate of adaptation per locus: weak; stratification problems | partial |
| 13 | Exact-chain checks of fixation probability (keruru KR-02) | keruru (critic/ally) | P(fix) = 1/(2N) in a Wright-Fisher plus sweepstakes chain | Yes, for the arithmetic identity | valid |
| 14 | Replication of an aDNA frequency series from the public resource (keruru RF-15) | keruru | Reproducibility of a published frequency excursion | Yes, narrowly | valid |
| 15 | Protein-space tolerance measurements (Axe 2004, Taylor 2001, Keefe-Szostak 2001) | Day via Axe; D10-D12 | Fraction of sequences with function | Not for evolvability (no path measure) | partial / invalid as sole test |
| 16 | Evolutionary-algorithm demonstrations (Weasel, D9) | Both (Day D9; Rosenhouse D1b) | Whether a fitness-guided search converges | No (fitness designed in; Day's own D2i) | invalid as a test of biological evolvability |
| 17 | "Challenge" to evolutionists to answer the math (public challenge) | Davis (RD-01..02), Day | Willingness to respond | No (a social test, not an empirical one) | invalid as a test |
| 18 | Parameter provenance checks (Yoo SI mu and generation time, GAP-06) | Audit | Whether Day's inputs match the source he cites | Yes for fidelity | valid |

## Method entries

### 1. LTEE as a benchmark
- **Proposed:** Day, Q85 (AI Central, 2026-10-09): "The more accurate number, as it turns out when you do what the scientists didn’t do and go to the high-resolution data set for all 273,000 generations across the 12 populations, then run the numbers, is 1,587 generations per fixation." Critic-side framing of the weakness: Dembski question DE-01 (2026-09-28): "...transferring a bacterial result (as in Richard Lenski’s Long-Term Evolution Experiment) to primates requires scaling for differences in mutation rate and genome size."
- **Measures:** substitution rate in clonal, asexual E. coli populations in a constant environment. Barrick 2009 (Nature, abstract only): "Although adaptation decelerated sharply, genomic evolution was nearly constant for 20,000 generations." Good 2017 (Nature, abstract only): "multiple beneficial variants simultaneously competing for dominance in each population" and "long-term quasi-stable coexistence arises spontaneously in most populations". PMIDs 19838166, 29045390 (https://europepmc.org/article/MED/19838166 ; https://europepmc.org/article/MED/29045390).
- **Biases and assumptions:** counting rule (1,322 versus 1,587; claims A2b); clonal interference and clade coexistence make a pooled count ambiguous (Good 2017 abstract); asexual lineage is a ceiling on interference, not a model of recombining primates (claim A5f); a lab environment is constant, so adaptive targets change differently from a primate lineage. A5/A2e say whether LTEE is a ceiling (claim A2e).
- **Verdict: partial.** It is a real, measurable benchmark and a fair proposal from Day; it cannot settle primate rates without a scaling argument both sides accept.

### 2. Pedigree mu versus phylogenetic k
- **Proposed:** Day, Q69: "The textbook k = μ identity is still falsified — both directly (pedigree μ and phylogenetic k disagree by a median factor of 25 across 55 vertebrates)". The relevant critic response: k = mu cancellation (claim B5, B3 branch).
- **Measures:** whether the neutral substitution rate per generation equals the per-generation germline mutation rate across species, in a way that depends on calibration and generation time.
- **Biases:** divergence-time calibration and generation-time choices dominate a factor-of-25 median; the claim was partly retracted/revised (Q65-Q69) and the B3 checks (R4-B3, B3g) rated it contradicted externally on one reading. Credit: this is a clean, falsifiable, data-based test and Day's retraction record shows him using it.
- **Verdict: valid** for the clock identity. It does not test selection versus drift by itself.

### 3. Whole-genome alignment fixation counts
- **Proposed:** Day, Q179 (2026-10-11): "the real number turned out to involve an estimated 410 million total genomic differences, not 35 million"; Q171: "there is no need to take my word for anything with regards to this, all of the data has been provided by the T2T Primate Consortium (Yoo et al. 2025)". Credit to Day: the invitation to replicate from public data is a good-faith move.
- **Measures:** divergence counts (SNVs, indels, SVs, unaligned sequence). Counts depend on what is aligned and how events are counted (bp versus events: claim A3x). Public data identified in refresh-2026-10-10b (T2T ape alignments, CC0).
- **Biases:** counting units (bp vs event), alignment completeness, inclusion of repeats, and the division by two lineages (A3d); the 410M is Day's own sum across tools per his text (Q179 note).
- **Verdict: partial.** Valid as measurement; says nothing about cause.

### 4. Mesa / overdispersion tests (FM)
- **Proposed:** Day, "The Fourth Mechanism" (2026-10-10), Q171 and FM claims FM3-FM10.
- **Measures:** clustering of differences in genomic windows beyond a Poisson expectation.
- **Biases *(general knowledge, not fetched)*:** mutation-rate heterogeneity, CpG content, repeat/SV regions, alignment errors and window choice all produce overdispersion without selection or sigillation; any null must model them. No code, window size or statistic has been released (refresh-2026-10-10).
- **Verdict: untested.** A proper null model is the missing piece, from either side.

### 5. dN/dS recomputation (new, 2026-10-11)
- **Proposed:** Day, Q172-Q177. Q176: "If the Consortium's curated subset gives ~0.23 and our complete set gives ~0.80, then the case is closed: the published number is an artificial artifact of cherry-picked genes, not an observed property of the human genome."
- **Measures:** the genome-average ratio of nonsynonymous to synonymous substitution rates. It does not measure the adaptive fraction or the rate of beneficial fixations.
- **Valid design element (credit to Day):** running the same pipeline on two gene sets isolates the gene-set effect. Day also reports, in the same post, a single-SNV-codon check (dN/dS = 0.71) and says the strictest filter stack leaves "10 remaining genes".
- **Known issues:** (a) 20,400 genes versus 13,454 one-to-one orthologs: non-orthologous, paralogous, fast-evolving, or poorly aligned genes can raise dN/dS; (b) Nei-Gojobori counting with multiple hits and saturation; (c) dN/dS near 1 in a pairwise average mixes purifying and neutral sites, so "0.80 = barely distinguishable from neutral" is a reading of an average, and Q177's step to "not the primary mechanism of adaptive evolution" is a non-sequitur candidate (rule N, not scored here) because dN/dS is dominated by deleterious/neutral changes; (d) the human-chimp literature value of 0.23 was not checked here. McDonald-Kreitman-type methods exist exactly to separate these (entry 9; Messer and Petrov 2013, abstract).
- **Verdict: partial.** Design valid; inference unsupported until the 13,454-gene run, the code and the per-gene table are released.

### 6. Ancient-DNA zero fixations
- **Proposed:** Day, Q52 (Z23046531, 2026-09-29): "of 1,143,671 autosomal SNPs analyzed, one changed from above 10% starting frequency to fixation or loss. In the replication (AADR v66.p1, analyzed September 29, 2026), three did."
- **Measures:** frequency change in a SNP panel over about 7 ky.
- **Biases:** the 1240k panel is ascertained on present-day polymorphism so recent fixations are excluded by design (claim C1; Day's reply C1a), mixed ancestry (admixture), Ne and window (claims C4, C5); keruru (critic-side) reports a reproducibility disagreement on one locus, RF-15.
- **Verdict: partial.** Real data, but the design cannot see the events it counts.

### 7. Selective turnover coefficient d
- **Proposed:** Day, Q22: "Day and Athos (2025a) estimated d empirically from ancient DNA time series, finding d ≈ 0.45 from three independent loci (LCT, SLC45A2, TYR)." Critic: Hancock, GG-25 (t=01:36:03): "this is not even necessarily a measure of selection."
- **Verdict: invalid as a test** (three loci that are known selected cannot estimate a genome-wide turnover; claims A4a, A4f; d was dropped in MITTENS 3.0, A4d). Credit: Day did drop it.

### 8. Sweep-signature absence
- **Proposed:** Day, claim A6 (Z18452504 s4.3). Counter-evidence side: Hernandez 2011 (Science, abstract only): "These findings indicate that classic sweeps were not a dominant mode of human adaptation over the past ~250,000 years." Schrider and Kern 2017 (MBE, abstract only): "soft sweeps are widespread and account for the vast majority of recent human adaptation." Sabeti 2002 (EHH) and Voight 2006 (iHS) give the scan methods (abstracts).
- **Reading:** both sides have a point. Day's premise (few detectable classic sweeps) is supported by Hernandez; the critic reading (adaptation proceeds as soft sweeps or polygenic shifts that scans see poorly) is supported by Schrider-Kern, but Schrider-Kern is a machine-learning classification of soft sweeps whose false-positive rate on realistic demography is not in the abstract.
- **Verdict: partial.** A valid test of "hitchhiking-as-main-source of fixations", not of selection in general (consistent with the A6 claim file).

### 9. McDonald-Kreitman and alpha
- **Proposed:** as a test in McDonald and Kreitman 1991 (Nature, abstract only; "the ratio of replacement to synonymous fixed differences between species should be the same as the ratio of replacement to synonymous polymorphisms within species"), used by the audit in R4-A2e-alpha for the 191-substitution threshold.
- **Biases:** slightly deleterious polymorphisms bias alpha downward and linked selection distorts frequency spectra (Messer and Petrov 2013 PNAS abstract: MK estimates "severely underestimate the true rate of adaptation" in the presence of slightly deleterious mutations); demographic change (Eyre-Walker and Keightley 2009, abstract, "as high as 40%"); reported human estimates span about 0.2% to 40% (refresh-2026-10-10b).
- **Verdict: partial.** It is the best available discriminator for whether the human lineage fixed more than about 191 adaptive substitutions; the published range straddles the threshold unless bias-corrected, and the Uricchio 2019 full text is still outstanding.

### 10. Forward simulation of rate limits
- **Proposed:** Day (H, Haldane 1/300); Hancock GG-26 (t=02:07:18): "the cost of selection is only applicable for hard selection models where selection's effect is independent of the genotypes"; Nunney 2003 (Introduction, per `quotes-literature.md` Nunney2003; abstract-level access only): "soft selection inevitably reduces or eliminates the cost of substitution. However, given directional environmental change, it is likely that hard selection will dominate the adaptive process"; Hössjer HO-11 (PDF p6). Weissman and Barton 2012 (PLoS Genet, abstract only) give an analytic ceiling for sexual populations: "interference prevents the rate of adaptive substitution from exceeding one per centimorgan per 200 generations."
- **Audit's runs:** R4-H8, R4-HF. Result summary (R4-HF): "the outcome turns on the unsourced hardness h (and on R), not on the arithmetic."
- **Verdict: partial.** Valid and decisive once h and R are known; until then each side's mean-field intuition is only partly right (several pre-registered bands missed).

### 11. Estimating hardness h in humans: candidate methods
h is the share of selection that depends on absolute fitness (R4-HF `mix` mode); no human value is sourced. None of the following is a proposal by Day or a critic; they are the audit's candidates, each derived from literature seen at abstract level, and each must be run before it is cited.

| Candidate | What it would give | Literature (abstract-level) | Assumptions and biases | Verdict |
|---|---|---|---|---|
| A. Lifetime reproductive success decomposition (viability versus fertility components, opportunity for selection) in historical cohorts | The fraction of variance in fitness from survival (population-size-dependent) versus relative reproduction | Stearns et al. 2010 Nat Rev Genet, PMID 20680024: "data on lifetime reproductive success, multiple traits and genetic variation and covariation"; Byars et al. 2010 PNAS, PMID 19858476 (Framingham women) | Observational; demographic and cultural confounds; measures realised, not genotype-specific, selection; the hard/soft split depends on whether mortality is density-dependent | partial (candidate) |
| B. Density-dependence of survival and fertility (e.g. across historical famine and population-size periods) | Whether absolute fitness responds to N (soft) or not (hard) | Reznick 2016 J Hered, PMID 26424874: soft selection is mediated by "density- and frequency-dependent selection"; Wallace 1975 (no abstract in the record) | Humans are not at a stationary K; confounded by technology, mortality shocks | partial (candidate) |
| C. Genotype-specific fitness effects in real polymorphisms (e.g. malaria, LCT in famine) | Whether the allele-specific advantage is an absolute survival effect | Sabeti 2002, PMID 12397357 (G6PD, CD40L, malaria resistance, abstract) | A few loci with large effects; extrapolating to many small effects is unsafe | partial (candidate) |
| D. Genomic constraint: variance in log fitness available for adaptation | An upper bound on tolerable load/cost via the interference ceiling | Weissman and Barton 2012, PMID 22685419 (abstract: heritable variance in log fitness reduces the substitution rate by e^-4v under polygamy and e^-8v under monogamy) | Needs v and recombination map; a ceiling in sexual populations, not a measure of h | partial (candidate) |
| E. Polygenic-adaptation scores plus fertility/mortality components | h for polygenic traits | Sella and Barton 2019, PMID 31283361; Field 2016 (SDS), PMID 27738015; critics: Berg 2019 PMID 30895923 and Sohail 2019 PMID 30895926 (abstracts: height signals "strongly attenuated or absent" in UK Biobank, stratification) | Stratification can fake or hide shifts; abstracts do not give a hardness estimate | partial (candidate) |
| F. Forward simulation with ABC against observed SFS/sweep counts (extend the audit's runs) | Posterior for (h, R, s) given observed data | audit method (R4-HF); Messer and Petrov 2013 for pitfalls | Prior-dependent; the data constrain adaptation rate, not h directly | partial (candidate) |

Overall verdict on method class 11: **untested**. A and B are the most direct and are within reach with public data; neither has been run. Whoever runs them should pre-register the h threshold at which the Haldane cost matters (R4-HF: roughly h of 0.3 versus 0.1).

### 12. Ancient-DNA and polygenic selection scans
- **Proposed:** critic-side literature, not an individual critic. Mathieson 2015 (Nature, PMID 26595274, abstract): "We detect selection at loci associated with diet, pigmentation and immunity, and two independent episodes of selection on height." Field 2016 (Science, PMID 27738015): "recent selection for increased height has driven allele frequency shifts across most of the genome." Counter: Berg 2019 and Sohail 2019 (both eLife, abstracts) show the height signal was confounded by stratification. This is a fair two-sided example: a method proposed for evidence of selection, then partly undone by its own field.
- **Verdict: partial.** Valid for strong, detectable loci; weak on polygenic claims.

### 13. Exact chain checks (keruru)
- keruru KR-02 (2026-08-26): "The fixation probability of a single new mutant in both chains: exactly 1/(2N_census), to fifteen decimal places." Code deposited per author (not retrieved). A clean enumeration test of an identity both sides have argued about (B7). **Verdict: valid** for the arithmetic; it says nothing about whether census or effective N is the right input (B5/B7c).

### 14. Reproducing a published aDNA frequency series
- keruru RF-15 (adna-draft-1.md s4b.1): "A published analysis of the same resource reports this variant at 29.3% in a Neolithic sample and 91.3% in a modern European one, a twelve-sigma excursion. We are unable to reproduce that." Reproduction from the public AADR is the right type of test. **Verdict: valid** (narrow). The target paper is unnamed in the draft.

### 15. Protein-space tolerance measurements
- Axe 2004, Taylor 2001, Keefe-Szostak 2001 (claims D10-D12; paywalled; only abstracts were read in refresh-2026-10-10b). They measure the fraction of sequences with a function; they do not measure reachability by stepwise evolution. **Verdict: partial** (informative about density, silent about paths; the debate in D1/D2 is about the path argument).

### 16. Evolutionary-algorithm demonstrations
- Day's D2i ("evolutionary algorithms designed fitness") and D9 (Weasel) versus Rosenhouse's D1b ("simulations commonplace"). Both sides' own claims agree that the fitness function is supplied by the programmer; a simulation shows a mechanism works under assumed landscapes, not that the real landscape is smooth. **Verdict: invalid as a test of biological evolvability**; valid as an existence proof of the mechanism. The audit's own simulations share this limit and must say so.

### 17. Public challenges
- Davis (RD-01, 2026-09-23): "I haven't read his book. I am relying only on the presentation"; RD-02: "I predict that they will provide essentially no answer." A challenge to respond is not an empirical test. Note the response exists (GG/Hancock 2026-10-03, 3.5 h). **Verdict: invalid as a test.** A more useful form is Day's Q176 commitment (publish the per-gene table), which can be checked.

### 18. Parameter provenance checks
- The audit's own (R4-GAP06): Yoo SI uses mu 1.25e-8 and node-specific generation times against Day's 1.2e-8 and 25 y (within 4% and 2%, refresh-2026-10-10b). **Verdict: valid** for fidelity. It does not test the dispute's core.

## Methods the audit relies on (credit and limits)
- Pre-registered simulations on na-workhorse (R4-H8, R4-HF): valid for conditional rates; limited by unsourced h and R.
- Fixed verdict rule (R4-X1): a methodology rule, not an empirical test.

## Candidates for the QUEUE (later queue, not pre-registered)
Listed in `research/checks/QUEUE.md` under "Later queue (test-methods review, 2026-10-11)".

## Not read / paywalled
Full texts not read: McDonald and Kreitman 1991, Hermisson and Pennings 2005 (PMID 15716498), Hernandez 2011, Schrider and Kern 2017 (OA in record, abstract used only), Sabeti 2002, Field 2016, Stearns 2010, Byars 2010, Reznick 2016, Wallace 1975 (no abstract), Barrick 2009, Good 2017 (OA in record, abstract used only), Messer and Petrov 2013, Weissman and Barton 2012 (OA, abstract only), Sella and Barton 2019. The owner could supply: Wallace 1975, Haldane 1957, Hernandez 2011, Field 2016, Stearns 2010, Barrick 2009, Messer and Petrov 2013, Uricchio 2019.

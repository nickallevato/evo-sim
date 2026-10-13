# Verbatim quotes: Vox Day corpus (R1 pass 2)

Rules: quotes are <=50 words (one exceeds by a few words only where a formula block is reproduced), checked by script against the saved text extraction (whitespace and quote-mark normalised; superscripts written `^x`, subscripts `_x`; PDF hyphenation preserved). Neutral: nothing here evaluates a claim. "DISCREPANCY/FLAG" marks only a mismatch between sources (or with the pass-1 figure in PLAN.md), never a verdict.

Locators: PDF = page number of the PDF; docx/odt/blog = `¶n` is the n-th non-empty line of the `.txt` extraction (blog extractions start with a TITLE line, which counts as ¶1). Local files are under `sources/raw/day/` (gitignored); source keys are defined in `bib-day.md`.

## Discrepancies and corrections vs PLAN.md pass-1 figures

| # | Item | PLAN.md pass-1 | What the source text says | Quote |
|---|---|---|---|---|
| 1 | Bernoulli Barrier p^n = 0.02^(2x10^7) ~ 10^-34,000,000 | attributed to Zenodo 18167588 | It is in the MITTENS paper Z18165980 (Dec 2025). Z18167588 uses n = 157,000, p = 0.5, giving 10^-47,262, and the 14.7x/1,570x and ~230 figures | Q11, Q24-Q28 |
| 2 | "~230 simultaneous sweeps" | listed as a derived cap | Stated in Z18167588 as "working backward from the constraint ... 200-300"; no derivation shown. The same section computes (300,000/440) x 230 = 157,000, which "appears to match the requirement" before the drift-input constraint (s7.9) | Q25-Q27 |
| 3 | k = 32.3 mu | "not in Zenodo; probably book only" | Not in any Zenodo text. First appears in the harvested corpus in blog 2026-10-01 ("The Education of a Population Geneticist"): Bergeron 2023 pedigree rate vs Yoo 2025 required substitution rate. No derivation given. Book not checked | Q43 |
| 4 | Haldane 11,739 / 321,444 | listed under "Haldane" | These figures are Richard Dawkins's (The Genetic Book of the Dead, 2024) as quoted in Day's post 2026-01-08; Day multiplies to 642,888 and 87,916,307x. They are not in Z18168236 | Q50-Q51 |
| 5 | SNV-only shortfall | ~94,000x | 91,600x (non-mutator, 17.5M required, 191 achievable) and 7,271x (mutator) | Q16-Q17 |
| 6 | aDNA "zero fixations in ~1.1-1.2M SNPs / 7 ky" | zero | Blog 2026-01-14: zero (1,211,499 loci, AADR v62.0, <10% to >90%). Zenodo 23046531 (2026-09-29): 1,143,671 SNPs (v62) / 1,143,230 (v66); 1 (v62) and 3 (v66) loci complete from the 50-90% starting range; 17,806 / 3,469 loci newly reach 100% (almost all from >90%); "zero ... from below 50%". Sample sizes and thresholds differ between the two | Q52-Q55 |
| 7 | LTEE 4,615 "NS only" | 4,615 | Appears only in blogs (2026-09-27, -09-30); Z23003785 itself gives ~1,408 gen per beneficial fixation (clone-pair, s4.3) and no 4,615 | Q61 |
| 8 | LTEE 909 (Ara+2) | 909 | Blog 2026-10-01: 66 fixations in 60,000 gens (60,000/66 = 909, derived). Z23105291 Table 1 lists Ara+2 at 60,500 gens, 66 fixations (60,500/66 = 917, derived). Z23003785 s4.1 lists Ara+2 at 64 (>=95% rule) | Q58-Q60 |
| 9 | LTEE 1,322 vs data paper | 1,322 and 5,496 | Z23003785 (Sep 28): >=95% pooled rule, non-mutator avg 45.4 -> 1,322. Z23105291 (Oct 2): the >=95% rule "returns 8,679" vs 5,496 whole-population fixations (37% less), per-population non-mutator counts 66, 73, 14, 9, 27 (sum 189, avg 37.8; 60,000/37.8 = 1,587, derived). The two papers use different counting rules; the 1,322 figure has not been restated in the later paper | Q56-Q59 |
| 10 | Source of 25 fixations / 40,000 gens / 1,600 | "25 fixations / 40k gens (Good 2017)" | 2019 post cites "NATURE, 2009"; Z18165980 cites Good et al. 2017 (60,000 gens) for the fixation time; Z18168236 says 25 in ~40,000 gens "reported in Nature in 2017" | Q02, Q08, Q64 |
| 11 | d from three aDNA loci | LCT, SLC24A5, HERC2 vs LCT, SLC45A2, TYR | Z18165980 lists LCT, SLC24A5, HERC2; Z18166234 lists LCT, SLC45A2, TYR; both give d ~ 0.45 | Q10, Q22 |
| 12 | 2019 arithmetic | 562 / 125 / 281 | Confirmed: table says 125 "maximum fixed mutations" for CHLCA (9 My, 20 y/gen, 1600 gens/fix, 32,000 y/fix); text says 450,000 generations "would permit 562 total fixed mutations" and is "29,999,438 short"; 450,000/1600 = 281.25 (derived), 562 = 2 x 281 (derived), 9,000,000/32,000 = 281.25 (derived). Neither 125 nor 562 is reproduced by the post's own table inputs without a stated factor | Q03-Q05 |
| 13 | MITTENS formula | F_max = (t_div x d)/(g_len x G_f), blog 2026-02-04 | Confirmed verbatim in blog 2026-02-04 ("Response to Dennis McCarthy, Round 2"). Zenodo papers (Z18441321, Z18452504, Z18470617, Z18637333) use "Achievable = (T or Generations x d) / G_f". The 3.0 paper (Z23003785) uses 252,000 nominal generations / 1,322 with no d term | Q06 |
| 14 | Version parameters | 2019: 1600/450k/30M; 2025: 1600, d=0.45, 146,250, 20M, 220,000x; 3.0: 1,322, 252k, 205M, 1,075,000x | Confirmed (2025 shortfall 219,780-fold; 3.0 1,075,000-fold). Additional versions: blog 2026-05-23 (2nd edition) uses 410M bp; Z23003785 s7.1 reaches 205M via "approximately 410 million genomic differences" halved | Q08-Q15, Q74-Q75 |
| 15 | k = 0.743 mu | 0.743 | Confirmed (Z18525262 eq. 3: 6.091/8.2). Also k ~ 0.5 mu in blog 2026-02-09 (six-country d vs k data) | Q40-Q42 |
| 16 | t ~ (2/s) ln(2Ne), s=0.001, "~19,800" | Q&A | Q&A gives parameters (Ne=10,000; T=22 y; L=51 y; s=0.001 "Zeng et al 2021") and t ~ 19,800 but does NOT print the formula; the formula appears in blog 2026-10-01 and, with s_eff, in Z18166426 | Q44-Q46 |
| 17 | 2026-05-07 retraction | partial retraction of cost-of-selection bound | The retraction is of the use of Term 3 (Haldane cost limit) as a bound on total substitution rate in Z19984826; CHLCA range revised from 68-330 kya to 250 kya-1.3 Mya | Q65-Q69 |
| 18 | Fixation probability 1/(2N) after the 2026-08-27 concession | (not in PLAN.md) | Blog 2026-08-27 concedes "the fixation probability of a new copy is 1/(2N)" (and in ¶3 objects that keruru's chains set genotype–breeding covariance to zero). Blog 2026-09-21 ("Where the Errors Hide"): Day says Chalub's result "IS FUCKING WRONG"; the Athos text he posts calls P(fix) = x₀ "false for any real population". Z23188201 (2026-10-06): 1/(2N) "holds exactly regardless of offspring distribution". No text reconciles the three | Q76-Q78 |

### Q01 MITTENS 2019: bacteria row
- source: `B2019-02-07-maximal-mutations` (blog post dated 2019-02-07); URL: https://voxday.net/2019/02/07/maximal-mutations/
- locator: ¶3 of extracted text
- quote: "BACTERIA Years: 3,800,000,000 Years per generation: 0.000071347 (37.5 mins per generation) Generations per fixed mutation: 1600"
- note: Original post; table also lists MAMMALS (29,070)

### Q02 MITTENS 2019: source of 1600
- source: `B2019-02-07-maximal-mutations` (blog post dated 2019-02-07); URL: https://voxday.net/2019/02/07/maximal-mutations/
- locator: ¶9 of extracted text
- quote: "Source: Sequencing of 19 whole genomes detected 25 mutations that were fixed in the 40,000 generations of the experiment. NATURE, 2009"

### Q03 MITTENS 2019: CHLCA row (125)
- source: `B2019-02-07-maximal-mutations` (blog post dated 2019-02-07); URL: https://voxday.net/2019/02/07/maximal-mutations/
- locator: ¶19 of extracted text
- quote: "CHLCA Years: 9,000,000 Years per generation: 20 Generations per fixed mutation: 1600 (Note: 8170 generations fastest Y-chromosomal lineage observed and extrapolated.) Years per fixed mutation: 32000 Maximum fixed mutations: 125"
- note: Table value 125; 9,000,000/32,000 = 281.25 (derived), see next quote
- **DISCREPANCY/FLAG:** Table "125" vs text "562" vs 281 (450,000/1600)

### Q04 MITTENS 2019: 562 arithmetic
- source: `B2019-02-07-maximal-mutations` (blog post dated 2019-02-07); URL: https://voxday.net/2019/02/07/maximal-mutations/
- locator: ¶28 of extracted text
- quote: "there have been 450,000 chimp and human generations since the CHLCA. Based on the number of mutations observed fixing in parallel in the Nature study, that would permit 562 total fixed mutations in that time frame. Which is only 29,999,438 short of the approximate number observed."
- note: 450,000/1600 = 281.25 (derived); 562 = 2 x 281 (derived). Post does not state the doubling.
- **DISCREPANCY/FLAG:** 562 vs 125 vs 281

### Q05 MITTENS 2019: required fixations 15M+15M
- source: `B2019-02-07-maximal-mutations` (blog post dated 2019-02-07); URL: https://voxday.net/2019/02/07/maximal-mutations/
- locator: ¶26 of extracted text
- quote: "it requires a minimum of 15,000,000 mutations to become fixed in the human population, and another 15,000,000 mutations to become fixed in the chimpanzee population"

### Q06 MITTENS formula (blog 2026-02-04) - first appearance in harvested corpus
- source: `B2026-02-04-response-to-dennis-mccarthy-round-2` (blog post dated 2026-02-04); URL: https://voxday.net/2026/02/04/response-to-dennis-mccarthy-round-2/
- locator: ¶10 of extracted text
- quote: "F_max = (t_div × d) / (g_len × G_f) F_max = maximum achievable fixations t_div = divergence time (in years) g_len = generation length (in years) d = Selective Turnover Coefficient G_f = generations per fixation"
- note: Introduced in the post as: "This is the core equation that is integral to MITTENS, which McCarthy still has not addressed". Zenodo texts use the equivalent "Achievable = (Generations x d) / G_f" (Z18441321, Z18452504); the F_max/t_div/g_len notation appears in no Zenodo text harvested

### Q07 Required fixations in this post: 20 million
- source: `B2026-02-04-response-to-dennis-mccarthy-round-2` (blog post dated 2026-02-04); URL: https://voxday.net/2026/02/04/response-to-dennis-mccarthy-round-2/
- locator: ¶26 of extracted text
- quote: "400,000 generations x 50 fixed mutations per generation = 20 million fixed mutations."
- note: This is McCarthy's calculation as quoted by Day (secondhand within the post)

### Q08 MITTENS v2025 (Z18165980): headline parameters
- source: `Z18165980` (Zenodo pub. 2025-12-28, record modified 2026-01-06); URL: https://zenodo.org/records/18165980
- locator: ¶6 of extracted text
- quote: "requiring approximately 20 million fixations on the human lineage—we calculate that natural selection can accomplish only 91 fixations given 146,250 effective generations (using the empirically-derived Selective Turnover Coefficient d = 0.45 from ancient DNA time series) and 1,600 generations per fixation (from the E. coli Long-Term Evolution Experiment)."
- note: Abstract; docx, no page numbers

### Q09 MITTENS v2025: arithmetic
- source: `Z18165980` (Zenodo pub. 2025-12-28, record modified 2026-01-06); URL: https://zenodo.org/records/18165980
- locator: ¶37 of extracted text
- quote: "Effective generations = 325,000 × 0.45 = 146,250 Fixation time: ~1,600 generations per fixation under strong selection (E. coli LTEE^3). Achievable fixations: 146,250 / 1,600 = 91 fixations Shortfall: 20,000,000 / 91 = 219,780-fold"

### Q10 d source loci (Z18165980)
- source: `Z18165980` (Zenodo pub. 2025-12-28, record modified 2026-01-06); URL: https://zenodo.org/records/18165980
- locator: ¶69 of extracted text
- quote: "Three independent loci (LCT, SLC24A5, HERC2) yielded d = 0.45 ± 0.08^2."
- note: Methods section
- **DISCREPANCY/FLAG:** loci differ from Z18166234 (LCT, SLC45A2, TYR)

### Q11 Bernoulli Barrier p^n and ~10^-34,000,000 (Z18165980)
- source: `Z18165980` (Zenodo pub. 2025-12-28, record modified 2026-01-06); URL: https://zenodo.org/records/18165980
- locator: ¶24 of extracted text
- quote: "For n = 20,000,000 fixations (human-chimp divergence, human lineage) and p = 0.02: P(all) ≈ 0.02^20,000,000 ≈ 10^−34,000,000"
- note: This is where 0.02^(2x10^7) appears; Z18167588 does not contain it
- **DISCREPANCY/FLAG:** PLAN.md attributes to Z18167588; actually Z18165980

### Q12 MITTENS v2025: divergence 40M SNV/20M
- source: `Z18165980` (Zenodo pub. 2025-12-28, record modified 2026-01-06); URL: https://zenodo.org/records/18165980
- locator: ¶34 of extracted text
- quote: "Genetic divergence: ~40 million single-nucleotide variants; ~20 million fixations required on human lineage. Time available: 6–7 million years at 20 years/generation = 300,000–350,000 nominal generations."

### Q13 MITTENS 3.0 (Z23003785): abstract headline
- source: `Z23003785` (Zenodo pub. 2026-09-28, record modified 2026-10-04); URL: https://zenodo.org/records/23003785
- locator: p.1
- quote: "The result for non-mutator populations is 1,322 generations per fixation at 60,000 generations — cross- validated at 893 generations per fixation by clone-pair analysis at 50,000 generations."
- note: PDF hyphenation "cross- validated" preserved

### Q14 MITTENS 3.0: parameters 205M / 252,000 / shortfall
- source: `Z23003785` (Zenodo pub. 2026-09-28, record modified 2026-10-04); URL: https://zenodo.org/records/23003785
- locator: p.1
- quote: "Applied to human-chimpanzee divergence (205 million required fixations on the human lineage across 252,000 available generations), the shortfall is 1,075,000-fold for non-mutators and 104,873-fold across all twelve populations including hypermutators."
- note: No d term appears in the 3.0 text (searched "turnover"/"d ="): achievable = 252,000/1,322 = 191 (derived)

### Q15 205M / 410M derivation (Z23003785 s7.1)
- source: `Z23003785` (Zenodo pub. 2026-09-28, record modified 2026-10-04); URL: https://zenodo.org/records/23003785
- locator: p.11
- quote: "approximately 35 million SNVs, 1,140 interspecific inversions, and approximately 187 megabases of structurally divergent regions, for a total of approximately 410 million genomic differences. Apportioned symmetrically to the human lineage this yields approximately 205 million required fixations."
- note: 35M + 187M != 410M as written (the text does not show the arithmetic); units mix SNVs, events and megabases
- **DISCREPANCY/FLAG:** bp-vs-events (branch A3)

### Q16 SNV-only concession (Z23003785 s7.3), part 1
- source: `Z23003785` (Zenodo pub. 2026-09-28, record modified 2026-10-04); URL: https://zenodo.org/records/23003785
- locator: p.12
- quote: "Restricting to the approximately 35 million SNVs and apportioning symmetrically: 17.5 million required fixations on the human lineage."
- note: Continues on next PDF page

### Q17 SNV-only concession (Z23003785 s7.3), part 2
- source: `Z23003785` (Zenodo pub. 2026-09-28, record modified 2026-10-04); URL: https://zenodo.org/records/23003785
- locator: p.13
- quote: "At 1,322 gen/fix (non-mutator): 191 achievable. Shortfall: 91,600×. At 105 gen/fix (mutator): 2,407 achievable. Shortfall: 7,271×."
- note: PLAN.md pass-1 said SNV-only ~94,000x; text says 91,600x (non-mutator)
- **DISCREPANCY/FLAG:** PLAN ~94,000x vs 91,600x

### Q18 Divergence time 3.0
- source: `Z23003785` (Zenodo pub. 2026-09-28, record modified 2026-10-04); URL: https://zenodo.org/records/23003785
- locator: p.11
- quote: "The divergence time is 6.3 million years. At 25 years per human generation, this provides 252,000 generations."

### Q19 Human-derived rate (Z23003785 s8.6)
- source: `Z23003785` (Zenodo pub. 2026-09-28, record modified 2026-10-04); URL: https://zenodo.org/records/23003785
- locator: p.15
- quote: "yields approximately one fixation per 27,600 effective generations (Day and Athos 2025, Appendix D). Applied to 252,000 generations provides 8 achievable fixations against the 205 million required."
- note: Cites book appendix (not harvested)

### Q20 d definition (verbal)
- source: `Z18166234` (Zenodo pub. 2025-12-24, record modified 2026-01-06); URL: https://zenodo.org/records/18166234
- locator: ¶33 of extracted text
- quote: "d = (Actual allele frequency change per generation) / (Change predicted by discrete-generation model)"
- note: Section 2.3

### Q21 d definition (integral)
- source: `Z18166234` (Zenodo pub. 2025-12-24, record modified 2026-01-06); URL: https://zenodo.org/records/18166234
- locator: ¶51 of extracted text
- quote: "d = T × d_continuous = T × [∫ μ(x) × l(x) × v(x) dx / ∫ l(x) × v(x) dx]"
- note: Section 3.3; μ(x) = −d[ln l(x)]/dx is mortality force

### Q22 d empirical value
- source: `Z18166234` (Zenodo pub. 2025-12-24, record modified 2026-01-06); URL: https://zenodo.org/records/18166234
- locator: ¶5 of extracted text
- quote: "Day and Athos (2025a) estimated d empirically from ancient DNA time series, finding d ≈ 0.45 from three independent loci (LCT, SLC45A2, TYR)."

### Q23 d integral defended (Q&A)
- source: `B2026-01-19-probability-zero-qa` (blog post dated 2026-01-19); URL: https://voxday.net/2026/01/19/probability-zero-qa/
- locator: ¶16 of extracted text
- quote: "If l(x) and v(x) were constants, they'd cancel and you'd get d = T × ∫μ(x)dx. But they're not constants, they're age-dependent functions that capture the demographic structure of the population."

### Q24 Bernoulli Barrier (Z18167588): 14.7x vs 1,570x
- source: `Z18167588` (Zenodo pub. 2026-01-04, record modified 2026-01-07); URL: https://zenodo.org/records/18167588
- locator: ¶6 of extracted text
- quote: "the fitness differential between the "best" and "worst" genotypes in a population of 10,000 is only 14.7×—while the required differential is 1,570×, a shortfall exceeding 100-fold."
- note: Abstract; n = 157,000 loci in this paper (not 2x10^7)

### Q25 Bernoulli: ~230 simultaneous sweeps
- source: `Z18167588` (Zenodo pub. 2026-01-04, record modified 2026-01-07); URL: https://zenodo.org/records/18167588
- locator: ¶6 of extracted text
- quote: "the "active zone" of intermediate-frequency alleles imposes a hard limit on pipeline capacity of approximately 230 simultaneous sweeps."
- note: Abstract

### Q26 Bernoulli: how 230 is obtained
- source: `Z18167588` (Zenodo pub. 2026-01-04, record modified 2026-01-07); URL: https://zenodo.org/records/18167588
- locator: ¶111 of extracted text
- quote: "Working backward from the constraint, the active zone can sustain approximately 200–300 simultaneous sweeps before the Bernoulli Barrier compresses variance below the threshold required for effective selection."
- note: Section 7.8; no derivation shown in text; t_transit ≈ (2/s) × ln(9) ≈ 440 generations with s = 0.01

### Q27 Bernoulli: 230 pipeline arithmetic
- source: `Z18167588` (Zenodo pub. 2026-01-04, record modified 2026-01-07); URL: https://zenodo.org/records/18167588
- locator: ¶63 of extracted text
- quote: "Maximum fixations ≈ (300,000 / 440) × 230 ≈ 157,000 This appears to match the requirement for human-chimpanzee divergence."
- note: Section 7.8: the paper itself says the idealised throughput matches 157,000 before applying the drift input constraint (s7.9)

### Q28 Bernoulli: P(all beneficial) = 0.5^157,000
- source: `Z18167588` (Zenodo pub. 2026-01-04, record modified 2026-01-07); URL: https://zenodo.org/records/18167588
- locator: ¶45 of extracted text
- quote: "P(all beneficial) = (0.5)¹⁵⁷'⁰⁰⁰ = 10⁻⁴⁷'²⁶²"
- note: Section 4.1

### Q29 Hard Limits (Z22129121): X formula, ~10^4
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: p.1
- quote: "Checking them yields a hard ceiling on population size, X = (Vₖ + 2)·G/16 — reproductive variance and lineage generations alone, with no mutation rate, no coalescent quantity, and no fitted constant. For a large, long-lived vertebrate the effective ceiling falls to about ten thousand individuals."
- note: Abstract

### Q30 Hard Limits: exp(−π²Nₑ/G)
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: p.1
- quote: "a neutral allele’s chance of fixing within the generations its lineage will ever have is not merely small but exponentially small, of order exp(−π²Nₑ/G) — for humans at current size, about one in ten to the seventy-eight-millionth."
- note: Abstract; p.1

### Q31 Hard Limits: F(T) short-time law
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: p.8
- quote: "F(T) ∼ exp( − π² Nₑ / T ), T ≪ 4Nₑ The naive fill fraction T/4Nₑ is not just unproven; it is an overstatement, and a vast one."
- note: p.8; no citation given at this point (paper has no reference list found)

### Q32 Hard Limits: Ne definition and 1/(2N)
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: p.4
- quote: "Nₑ = (4N − 2) / (Vₖ + 2)"
- note: p.4; elsewhere the paper uses neutral fixation probability 1/(2N): "neutral fixation probability exactly 1/(2N)" (p.11)

### Q33 Hard Limits: human ceilings
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: p.6
- quote: "The human’s is thirty-five thousand as a species, a hundred thousand as a lineage. The elephant’s is twenty-eight thousand."
- note: p.6

### Q34 Intrinsic Irrelevance (Z22903977): E[F(T)]
- source: `Z22903977` (Zenodo pub. 2026-09-22, record modified 2026-09-22); URL: https://zenodo.org/records/22903977
- locator: p.1
- quote: "using the exact transient formula E[F(T)] = μL ∫₀ᵀ F_X(u) du rather than the naive product μLT, the leading-order correction subtracts the mean fixation time from the available window."
- note: Abstract, p.1

### Q35 E[F(T)] ≈ μL(T − 4Nₑ)
- source: `Z22903977` (Zenodo pub. 2026-09-22, record modified 2026-09-22); URL: https://zenodo.org/records/22903977
- locator: p.2
- quote: "∫₀ᵀ F_X(u) du = T − ∫₀ᵀ (1 − F_X(u)) du ≈ T − 4Nₑ"
- note: p.2; and E[F(T)] ≈ μL(T − 4Nₑ)

### Q36 Intrinsic Irrelevance: numbers
- source: `Z22903977` (Zenodo pub. 2026-09-22, record modified 2026-09-22); URL: https://zenodo.org/records/22903977
- locator: p.3
- quote: "Using 252,000 generations since the split (approximately 6.3 million years at 25 years per generation) and μL ≈ 30 neutral mutations per generation: Steady-state calculation (k = μ applied naively): 30 × 252,000 = 7,560,000 fixations"
- note: p.3

### Q37 Ancestral polymorphism treated (Z22903977)
- source: `Z22903977` (Zenodo pub. 2026-09-22, record modified 2026-09-22); URL: https://zenodo.org/records/22903977
- locator: p.3
- quote: "Under coalescent theory, the expected pairwise divergence contributed by ancestral polymorphism is θ = 4Nₑμ per site."
- note: p.3

### Q38 k = μN/Nₑ (Z18525547 eq. 1)
- source: `Z18525547` (Zenodo pub. 2026-02-08, record modified 2026-02-08); URL: https://zenodo.org/records/18525547
- locator: ¶10 of extracted text
- quote: "k = 2Nμ × 1/(2N_e) = μ × (N/N_e) (1)"
- note: docx; abstract states the cancellation "is invalid"

### Q39 k = μN/Nₑ (blog 2026-02-04)
- source: `B2026-02-04-response-to-dennis-mccarthy-round-2` (blog post dated 2026-02-04); URL: https://voxday.net/2026/02/04/response-to-dennis-mccarthy-round-2/
- locator: ¶29 of extracted text
- quote: "k = 2Nμ × 1/(2Nₑ) = μ(N/Nₑ)"

### Q40 k = 0.743μ (Z18525262 eq. 3)
- source: `Z18525262` (Zenodo pub. 2026-02-08, record modified 2026-02-08); URL: https://zenodo.org/records/18525262
- locator: ¶58 of extracted text
- quote: "k = μ × 6.091/8.2 = 0.743μ (3)"
- note: Derived from 4 generations of human census data 1950-2025; Day states it "confirms" Balloux & Lehmann 2012

### Q41 k = 0.743μ abstract
- source: `Z18525262` (Zenodo pub. 2026-02-08, record modified 2026-02-08); URL: https://zenodo.org/records/18525262
- locator: ¶4 of extracted text
- quote: "Applied to four generations of human census data, it yields k = 0.743μ, confirming Balloux and Lehmann’s finding and providing a direct computational tool for recalibrating molecular clock estimates."

### Q42 k up to 0.5μ (blog 2026-02-09)
- source: `B2026-02-09-the-significance-of-d-and-k` (blog post dated 2026-02-09); URL: https://voxday.net/2026/02/09/the-significance-of-d-and-k/
- locator: ¶9 of extracted text
- quote: "The data show that k in humans has been approximately 0.5μ or less throughout the entire modern period for which we have reliable demographic data"
- note: Third k value in corpus: 0.5μ

### Q43 k = 32.3μ (blog 2026-10-01) - first appearance in harvested corpus
- source: `B2026-10-01-the-education-of-a-population-geneticist` (blog post dated 2026-10-01); URL: https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/
- locator: ¶7 of extracted text
- quote: "comparing Bergeron’s (2023) pedigree-measured mammalian mutation rate against the required substitution rate from Yoo et al. (2025) gives k = 32.3μ, not k = μ."
- note: Not found in any Zenodo text; no derivation in the post. Book (paywalled) may contain it; not checked.
- **DISCREPANCY/FLAG:** PLAN.md: "not in Zenodo; probably book only" -> in fact first appears in this blog post (2026-10-01)

### Q44 t ≈ 19,800 gens/fixation, s = 0.001 (Q&A)
- source: `B2026-01-19-probability-zero-qa` (blog post dated 2026-01-19); URL: https://voxday.net/2026/01/19/probability-zero-qa/
- locator: ¶5 of extracted text
- quote: "N_e = 10,000 (standard effective population constant) T = 22 years (generation, Gurven & Kaplan 2007) L = 51 years (lifespan based on Coale-Demeny-West life tables) s = 0.001 (selection coefficient, Zeng et al 2021) t ≈ 19,800 generations per fixation"
- note: Formula not shown in the Q&A; (2/0.001) x ln(20,000) = 19,807 (derived)

### Q45 t ≈ (2/s)ln(2Nₑ) stated (blog 2026-10-01)
- source: `B2026-10-01-the-education-of-a-population-geneticist` (blog post dated 2026-10-01); URL: https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/
- locator: ¶6 of extracted text
- quote: "Kimura’s equation for fixation time: 4Nₑ generations for a neutral allele, or t ≈ (2/s) × ln(2Nₑ) for a beneficial one."
- note: Attributed to Kimura; Z18470617 cites Charlesworth 1994 for sweep time in the Kimura calculator Z19984826

### Q46 t ≈ (2/s_eff) ln(2N_e) in a Zenodo paper
- source: `Z18166426` (Zenodo pub. 2025-12-25, record modified 2026-01-06); URL: https://zenodo.org/records/18166426
- locator: ¶118 of extracted text
- quote: "Time to fixation calculated using t ≈ (2/s_eff) × ln(2N_e) for N_e = 10,000, from initial frequency p = 0.01 to p = 0.99."

### Q47 Haldane 300 gens/substitution (Z18168236)
- source: `Z18168236` (Zenodo pub. 2026-01-05, record modified 2026-01-07); URL: https://zenodo.org/records/18168236
- locator: ¶8 of extracted text
- quote: "Haldane calculated that mammals could fix no more than approximately one beneficial substitution per 300 generations, based on the reproductive cost each substitution imposes on a population."

### Q48 Haldane + d = 487
- source: `Z18168236` (Zenodo pub. 2026-01-05, record modified 2026-01-07); URL: https://zenodo.org/records/18168236
- locator: ¶41 of extracted text
- quote: "Achievable fixations (Haldane + d) = 146,250 / 300 = 487 fixations"

### Q49 Haldane table (blog 2025-05-28)
- source: `B2025-05-28-haldane-vs-kimura` (blog post dated 2025-05-28); URL: https://voxday.net/2025/05/28/haldane-vs-kimura/
- locator: ¶6 of extracted text
- quote: "HALDANE Years: 9,000,000 Years per generation: 25 Generations per fixed mutation: 300 Years per fixed mutation: 7,500 Maximum fixed mutations: 1,200"
- note: Table also carries a x1.4 bp-per-allele factor (stated in the text)

### Q50 Haldane 11,739 / 321,444 are Dawkins quoting Haldane (blog 2026-01-08)
- source: `B2026-01-08-88-million-x` (blog post dated 2026-01-08); URL: https://voxday.net/2026/01/08/88-million-x/
- locator: ¶4 of extracted text
- quote: "His answer was a mere 11,739 generations if the gene is dominant, 321,444 generations if it is recessive."
- note: Passage is attributed in the post to Richard Dawkins, The Genetic Book of the Dead (2024), as posted by Day; about a hypothetical s with 999 vs 1,000 survivors (s ~ 0.001)
- **DISCREPANCY/FLAG:** Figures are Dawkins' (after Haldane), not computed by Day

### Q51 Day's use of the Dawkins figures
- source: `B2026-01-08-88-million-x` (blog post dated 2026-01-08); URL: https://voxday.net/2026/01/08/88-million-x/
- locator: ¶6 of extracted text
- quote: "Dawkins somehow imagines that even 642,888 generations for one single base pair is more than enough time for evolution to take place. He’s off by a mere factor of 4.4 x 20 million, or 87,916,307x."
- note: 642,888 = 321,444 x 2 (derived)

### Q52 aDNA (Z23046531): abstract counts
- source: `Z23046531` (Zenodo pub. 2026-09-29, record modified 2026-09-29); URL: https://zenodo.org/records/23046531
- locator: p.1
- quote: "of 1,143,671 autosomal SNPs analyzed, one changed from above 10% starting frequency to fixation or loss. In the replication (AADR v66.p1, analyzed September 29, 2026), three did."
- note: Abstract, p.1
- **DISCREPANCY/FLAG:** PLAN "zero fixations" vs paper: 1 (v62) and 3 (v66) completions from MAF>=10%

### Q53 aDNA (Z23046531): discussion
- source: `Z23046531` (Zenodo pub. 2026-09-29, record modified 2026-09-29); URL: https://zenodo.org/records/23046531
- locator: p.6
- quote: "Across 1.14 million autosomal loci and 7,000 years of European prehistory, zero alleles moved from below 50% starting frequency to regional fixation, and zero moved from below 10% to fixation, in either run."
- note: Discussion, p.6

### Q54 aDNA (Z23046531): counts of fixation events
- source: `Z23046531` (Zenodo pub. 2026-09-29, record modified 2026-09-29); URL: https://zenodo.org/records/23046531
- locator: p.4
- quote: "The true fixation check identified 17,806 loci newly reaching 100% and 8 loci newly reaching 0% in the modern period."
- note: Section 3.3 (v62.0); v66.p1: 3,469 newly 100%, 1 newly 0%

### Q55 aDNA zero fixations - blog 2026-01-14
- source: `B2026-01-14-empirically-impossible` (blog post dated 2026-01-14); URL: https://voxday.net/2026/01/14/empirically-impossible/
- locator: ¶5 of extracted text
- quote: "The observed fixation count was zero. Not a single allele in 1.2 million crossed from rare (<10% frequency) to fixed (>90% frequency) in seven thousand years."
- note: AADR v62.0, 1,211,499 loci, Neolithic n=1,112 vs modern n=645 (stated in the post); differs from Z23046531 (1,143,671 SNPs; 1,372/680)
- **DISCREPANCY/FLAG:** loci/sample counts and definition differ between blog (Jan 2026) and Zenodo paper (Sep 2026)

### Q56 LTEE fixations (Z23105291): 5,496 / 723,000
- source: `Z23105291` (Zenodo pub. 2026-10-02, record modified 2026-10-02); URL: https://zenodo.org/records/23105291
- locator: p.1
- quote: "By this strict definition the twelve populations contain 5,496 whole-population fixations across 723,000 population-generations."
- note: Abstract; same paper: naive >=95% rule returns 8,679

### Q57 LTEE naive rule (Z23105291)
- source: `Z23105291` (Zenodo pub. 2026-10-02, record modified 2026-10-02); URL: https://zenodo.org/records/23105291
- locator: p.1
- quote: "A naive rule that counts the first time a mutation's pooled frequency reaches 95% — the method of most quick analyses, including an earlier draft of our own — returns 8,679."
- note: Note: 3.0 (Z23003785) uses the >=95% rule for its 1,322 figure

### Q58 LTEE 1,322 table (Z23003785 s4.1)
- source: `Z23003785` (Zenodo pub. 2026-09-28, record modified 2026-10-04); URL: https://zenodo.org/records/23003785
- locator: p.6
- quote: "The average across all five non-mutator populations at 60,000 generations is 45.4 fixations, yielding a cumulative rate of 1,322 generations per fixation."
- note: 60,000/45.4 = 1,321.6 (derived); uses >=95% pooled-frequency counting (s3.2)

### Q59 LTEE per-population 66 (Z23105291 table 1)
- source: `Z23105291` (Zenodo pub. 2026-10-02, record modified 2026-10-02); URL: https://zenodo.org/records/23105291
- locator: p.3
- quote: "Ara+2 non-mutator 60,500 174 66 0 66 0"
- note: Table 1 row: PASS mutations 174; whole-population fixations 66; within-lineage sweeps 0; first-crossing 66; 60,000/66 = 909 (derived)

### Q60 LTEE 909 gens/fixation Ara+2 (blog)
- source: `B2026-10-01-snikker-snak` (blog post dated 2026-10-01); URL: https://voxday.net/2026/10/01/snikker-snak/
- locator: ¶12 of extracted text
- quote: "For example, Ara+2 had 66 fixations in 60,000 generations. At 909 generations per fixation, this was one of the fastest still-viable populations."

### Q61 LTEE 4,615 NS-only (blog 2026-09-27)
- source: `B2026-09-27-the-temperature-rises` (blog post dated 2026-09-27); URL: https://voxday.net/2026/09/27/the-temperature-rises/
- locator: ¶13 of extracted text
- quote: "The real, updated 60-generation LTTE numbers are: 4,615 generations per beneficial fixation (natural selection) 1,322 generations per all-cause fixation (natural selection + neutral theory + everything else)"
- note: Not found in Z23003785 (which gives ~1,408 gen per beneficial fixation by clone-pair, s4.3)
- **DISCREPANCY/FLAG:** 4,615 appears only in blog; Zenodo 3.0 gives 1,408 (clone-pair beneficial-only)

### Q62 LTEE 78 gens/fix hypermutators
- source: `B2026-09-28-mittens-3-0` (blog post dated 2026-09-28); URL: https://voxday.net/2026/09/28/mittens-3-0/
- locator: ¶3 of extracted text
- quote: "increased the speed of the subsequent fixations to 78 generations per fixation."

### Q63 LTEE 1,600 -> 1,400 -> 1,322 (Z23003785 s3.3)
- source: `Z23003785` (Zenodo pub. 2026-09-28, record modified 2026-10-04); URL: https://zenodo.org/records/23003785
- locator: p.5
- quote: "The book Probability Zero used 1,400 gen/fix, taken from Good et al.’s published summary. Our independent re-analysis of the raw data produces 1,322"

### Q64 Source of 1,600 in 2025 papers
- source: `Z18168236` (Zenodo pub. 2026-01-05, record modified 2026-01-07); URL: https://zenodo.org/records/18168236
- locator: ¶29 of extracted text
- quote: "Sequencing detected 25 mutations that were fixed over approximately 40,000 bacterial generations, yielding an average of 1,600 generations per fixed mutation."
- note: Z18168236 cites Good et al. 2017; the 2019 post cites Nature 2009 (Barrick et al.)
- **DISCREPANCY/FLAG:** citation for the 25/40,000 datum differs between 2019 post (Nature 2009) and 2025 papers (Good 2017)

### Q65 Retraction 2026-05-07: what is retracted
- source: `B2026-05-07-a-retraction-and-a-revision` (blog post dated 2026-05-07); URL: https://voxday.net/2026/05/07/a-retraction-and-a-revision/
- locator: ¶3 of extracted text
- quote: "our subsequent empirical work has identified a category error in how the selection-cost binding constraint was being used in it."

### Q66 Retraction: three-term framework
- source: `B2026-05-07-a-retraction-and-a-revision` (blog post dated 2026-05-07); URL: https://voxday.net/2026/05/07/a-retraction-and-a-revision/
- locator: ¶3 of extracted text
- quote: "the realized substitution rate equals the minimum of three serial constraints: the corrected input flux (Term 1), the polymorphism throughput ceiling (Term 2), and the selection-cost limit (Term 3)."

### Q67 Retraction: the error
- source: `B2026-05-07-a-retraction-and-a-revision` (blog post dated 2026-05-07); URL: https://voxday.net/2026/05/07/a-retraction-and-a-revision/
- locator: ¶4 of extracted text
- quote: "my error was in interpreting its output as a constraint on total k. Once corrected, Term 3 still limits adaptive substitution rate at ~10⁻¹², but total substitution rate is only governed by Terms 1 and 2"

### Q68 Retraction: CHLCA revised
- source: `B2026-05-07-a-retraction-and-a-revision` (blog post dated 2026-05-07); URL: https://voxday.net/2026/05/07/a-retraction-and-a-revision/
- locator: ¶7 of extracted text
- quote: "the CHLCA event falls somewhere in the 250 kya to 1.3 Mya range rather than the 6.3 Mya presently assumed. But it cannot be as recent as the lower end of the 68 kya to 330 kya range"

### Q69 Retraction: what survives
- source: `B2026-05-07-a-retraction-and-a-revision` (blog post dated 2026-05-07); URL: https://voxday.net/2026/05/07/a-retraction-and-a-revision/
- locator: ¶5 of extracted text
- quote: "The textbook k = μ identity is still falsified — both directly (pedigree μ and phylogenetic k disagree by a median factor of 25 across 55 vertebrates)"
- note: Z19984826 (the retracted paper) still carries the original text; no revised Zenodo version seen

### Q70 Darwillion: Day on its status
- source: `B2026-09-17-the-math-is-too-hard` (blog post dated 2026-09-17); URL: https://voxday.net/2026/09/17/the-math-is-too-hard/
- locator: ¶8 of extracted text
- quote: "the Darwillion is nothing more than a rhetorical absurdity to demonstrate how far off the biologists are from the mathematical realities of the situation."

### Q71 Darwillion formula (secondhand, McCarthy quoted)
- source: `B2026-09-11-do-try-to-keep-up-dennis` (blog post dated 2026-09-11); URL: https://voxday.net/2026/09/11/do-try-to-keep-up-dennis/
- locator: ¶5 of extracted text
- quote: "What Vox Day calculated—(1/20,000)20,000,000 —are the odds that a particular group or a pre-specified list of 20 million mutations"
- note: secondhand: critic's quotation of Day's book calculation; exponent flattened in HTML
- **DISCREPANCY/FLAG:** secondhand

### Q72 Relictation (Z23188201): 10% threshold
- source: `Z23188201` (Zenodo pub. 2026-10-06, record modified 2026-10-07); URL: https://zenodo.org/records/23188201
- locator: p.1
- quote: "compression fails and a single family can replace more than ~10% of the population, the formula t̄ = 4Nₑ breaks in quantifiable ways. Below 10% replacement, the formula holds"
- note: Abstract p.1

### Q73 Hypermutation hazard 2.3% (Z23020792)
- source: `Z23020792` (Zenodo pub. 2026-09-28, record modified 2026-09-28); URL: https://zenodo.org/records/23020792
- locator: p.7
- quote: "is approximately 0.06 × 0.39 ≈ 2.3% per founder"
- note: p.7

### Q74 Book: 2nd edition 410M / 14.9%
- source: `B2026-05-23-probability-zero-2nd-edition` (blog post dated 2026-05-23); URL: https://voxday.net/2026/05/23/probability-zero-2nd-edition/
- locator: ¶6 of extracted text
- quote: "the genetic difference between chimps and humans turned out to be 14.9 percent, with 410 million base pairs separating the two lineages since the Chimpanzee-Human Last Common Ancestor."
- note: 2nd-edition introduction

### Q75 Book: first edition built on 40M bp (2005 data)
- source: `B2026-05-23-probability-zero-2nd-edition` (blog post dated 2026-05-23); URL: https://voxday.net/2026/05/23/probability-zero-2nd-edition/
- locator: ¶4 of extracted text
- quote: "All of the mathematics that I utilized in the first edition of this book were based on the observed divergence of 40 million base pairs between the two lineages published in the 2005 paper."

### Q76 Errors Hide: Day says Chalub's fixation result is wrong (added 2026-10-08)
- source: `B2026-09-21-where-the-errors-hide` (blog post dated 2026-09-21); URL: https://voxday.net/2026/09/21/where-the-errors-hide/
- locator: ¶8 of extracted text
- quote: "I don’t give one flying fragment of a rat’s ass if the math is technically correct but the end result is off because various necessary inputs were left out. THE RESULT IS FUCKING WRONG!"
- note: Day's own words, addressed to his AI assistant Athos about Chalub's P(fix) = x₀. 25 days after the 2026-08-27 concession (claim B3g).
- **DISCREPANCY/FLAG:** in tension with the 2026-08-27 concession ("the fixation probability of a new copy is 1/(2N)"); see versions.md "N vs Nₑ in k"

### Q77 Errors Hide: Athos (posted by Day) on P(fix) = x₀ (added 2026-10-08)
- source: `B2026-09-21-where-the-errors-hide` (blog post dated 2026-09-21); URL: https://voxday.net/2026/09/21/where-the-errors-hide/
- locator: ¶10 of extracted text
- quote: "He left out reproductive covariance, so he wrote the wrong equation, so P(fix) = x₀ is a wrong answer to the real question."
- note: AI-produced text (Athos) that Day posts as "useful". The same post, ¶4, has Athos saying "For a neutral allele the chance of fixation is just its starting frequency, x₀ — for a new mutation, 1/(2N). That’s the standard result".

### Q78 Errors Hide: "false for any real population" (added 2026-10-08)
- source: `B2026-09-21-where-the-errors-hide` (blog post dated 2026-09-21); URL: https://voxday.net/2026/09/21/where-the-errors-hide/
- locator: ¶12 of extracted text
- quote: "the number he got out — fixation equals starting frequency — is false for any real population because it’s the answer to the frictionless-coin problem, not the breeding one."
- note: Athos text posted by Day. Z23188201 (2026-10-06) later states p = 1/(2N) "holds exactly regardless of offspring distribution" (claim E4).


## Refresh 2026-10-09 additions (Q79-Q96)

Verified as exact substrings (whitespace and quote-mark normalised) of the local raw copies under `sources/raw/refresh-2026-10-09/` by script, 2026-10-09. For Substack comments the locator is the Substack comment id (the id appears in the comment URL). Blog and newsletter locators are paragraph numbers of the extracted non-empty lines (title line = para 1). Q79-Q81 come from a blog post that reposts comments; Q82-Q96 are Day's comments or posts on third-party or secondary venues (Dembski's and McCarthy's Substacks, Sigma Game, AI Central). Q84 is a re-read of a post already in `bib-day.md`.

### Q79 Evo-Avengers: selection and drift both "impossible" (added 2026-10-09)
- source: `B2026-10-08-not-just-the-evo-avengers`; URL: https://voxday.net/2026/10/08/not-just-the-evo-avengers/
- locator: para 8 of extracted text (title line = para 1)
- local copy: `sources/raw/refresh-2026-10-09/day-post-2026-10-08-not-just-the-evo-avengers/page.txt`
- branch: A,B,ROOT
- quote: "What I know is natural selection is impossible. Neutral substitution through genetic drift is impossible. Those things are firmly established."
- note: Day replying to an EES advocate (Dembski's Substack, comment 353314959, 2026-10-05, reposted in the blog). Restates the two-sided conclusion (selection and drift both excluded).

### Q80 Evo-Avengers: Day's admission test for any mechanism (added 2026-10-09)
- source: `B2026-10-08-not-just-the-evo-avengers`; URL: https://voxday.net/2026/10/08/not-just-the-evo-avengers/
- locator: para 8 of extracted text (title line = para 1)
- local copy: `sources/raw/refresh-2026-10-09/day-post-2026-10-08-not-just-the-evo-avengers/page.txt`
- branch: ROOT
- quote: "Unless the model addresses the existing and observable accounting, it is irrelevant."
- note: Day's stated criterion for admitting any positive mechanism (EES/Third Way): it must be quantified against 'timescales and reproductive limits'. No EES model was examined (same comment 353314959: 'That doesn't mean EES is wrong. I have no idea.').

### Q81 Evo-Avengers: "one single game designer" (added 2026-10-09)
- source: `B2026-10-08-not-just-the-evo-avengers`; URL: https://voxday.net/2026/10/08/not-just-the-evo-avengers/
- locator: para 17 of extracted text (title line = para 1)
- local copy: `sources/raw/refresh-2026-10-09/day-post-2026-10-08-not-just-the-evo-avengers/page.txt`
- branch: misc
- quote: "But one single game designer can do in a week what 170 years worth of naturalists couldn’t."
- note: Rhetoric; no number or method. Recorded for completeness (same comment as the 'nuke' remark, Dembski thread comment 355857440, 2026-10-08).

### Q82 Dembski thread: "to the very base-pair ... six different genomes" (added 2026-10-09)
- source: `Dembski-interview-comments`; URL: https://billdembski.substack.com/p/vox-day-interview-on-evolutionary/comment/356282255
- locator: comment id 356282255 (2026-10-08, Vox Day)
- local copy: `sources/raw/refresh-2026-10-09/dembski-interview/comments.json`
- branch: ROOT,E
- quote: "I know, to the very base-pair, precisely what level of influence natural selection, EES, and every other adaptive mechanism has had on six different genomes."
- note: Substack comment by Vox Day, 2026-10-08. Not in the blog repost. 'Six different genomes' is not defined; the 2nd-edition abstract Day quotes in comment 340102853 says 'Scaling analysis across 18 species pairs'.

### Q83 Dembski thread: Chalub, steady-state identity, not a martingale (added 2026-10-09)
- source: `Dembski-interview-comments`; URL: https://billdembski.substack.com/p/vox-day-interview-on-evolutionary/comment/348667799
- locator: comment id 348667799 (2026-09-29, Vox Day)
- local copy: `sources/raw/refresh-2026-10-09/dembski-interview/comments.json`
- branch: B1
- quote: "Ironically, as it turns out, it's not even correct to invoke martingales in defense of neutral theory because as Franco Chalub demonstrated mathematically, k = μ is a steady-state identity, not a martingale property."
- note: Substack comment by Vox Day, 2026-09-29 (replying to Dembski on 'martingale'). Chalub is cited as a source for the steady-state claim (claims B1, B1e).

### Q84 An Epic Test: new disproof, "Reverse-MITTENS" (added 2026-10-09)
- source: `B2026-10-07-an-epic-test`; URL: https://voxday.net/2026/10/07/an-epic-test/
- locator: para 2 of extracted text (title line = para 1)
- local copy: `sources/raw/refresh-2026-10-09/day-recheck-an-epic-test/page.txt`
- branch: ROOT
- quote: "today I came up with a new disproof of the Post-Darwinian polythesis that has nothing to do with either MITTENS or Reverse-MITTENS"
- note: Re-read of a post already in the corpus (bib-day B2026-10-07-an-epic-test). 'Reverse-MITTENS' is not defined in any harvested text. Pre-registration: an announced, unpublished argument and an 'epic data analysis' were pending as of 2026-10-07.

### Q85 AI Central: 1,587 generations per fixation, 273,000 generations (added 2026-10-09)
- source: `AICentral-An-Intelligent-Groove`; URL: https://substack.aicentral.blog/p/an-intelligent-groove
- locator: para 16 of extracted text (title line = para 1)
- local copy: `sources/raw/refresh-2026-10-09/aicentral-groove/page.txt`
- branch: A2
- quote: "The more accurate number, as it turns out when you do what the scientists didn’t do and go to the high-resolution data set for all 273,000 generations across the 12 populations, then run the numbers, is 1,587 generations per fixation."
- note: Vox Day, AI Central Substack, 2026-10-03. Day's own statement of the strict-count G_f (previously derived by the audit from Z23105291; claim A2b). '273,000 generations' differs from the 252,000 human-lineage generations (different quantities). The same post repeats the Z23003785 abstract (1,322; 893; 1,075,000; 104,873).

### Q86 Sigma Game Apologies: "tactical nuke" on neutral theory (added 2026-10-09)
- source: `SigmaGame-Apologies`; URL: https://sigmagame.substack.com/p/apologies
- locator: para 4 of extracted text (title line = para 1)
- local copy: `sources/raw/refresh-2026-10-09/sigma-apologies/post.txt`
- branch: B1,F
- quote: "neutral theory, the primary Neo-Darwinian retreat, and the field of population genetics was just hit by a tactical nuke."
- note: Vox Day, Sigma Game, 2026-09-22 (day Z22903977 was deposited). Same post quotes the abstract: 'at realistic human values, ranges from 16 percent to 100 percent of the total available time frame'.

### Q87 Sigma Game Gamma Always Runs: "every single proposed mechanism" (added 2026-10-09)
- source: `SigmaGame-The-Gamma-Always-Runs`; URL: https://sigmagame.substack.com/p/the-gamma-always-runs
- locator: para 44 of extracted text (title line = para 1)
- local copy: `sources/raw/refresh-2026-10-09/sigma-the-gamma-always-runs/post.txt`
- branch: ROOT
- quote: "Nothing is going to change the fact that evolution by every single proposed mechanism, including natural selection, has been comprehensively, mathematically, and empirically disproven."
- note: Vox Day, Sigma Game, 2026-10-02 (final paragraph; repost of the Mansfield exchange, see Q-series for blog 2026-10-01). The post also has an unattributed block repeating '200,000,000' from the 410 Mb figure and a commenter's 'I have never seen a reliable estimate that is much about 30 million' (commenter unnamed).

### Q88 McCarthy thread: drift "deader than dead" (added 2026-10-09)
- source: `McCarthy-comments (Why PZ is Wrong)`; URL: https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1/comment/335155894
- locator: comment id 335155894 (2026-09-12, Vox Day)
- local copy: `sources/raw/refresh-2026-10-09/mccarthy-comments-why/comments.json`
- branch: B2,C
- quote: "Genetic drift is now deader than dead. A Portuguese mathematician corrected Kimura's math, and subsequent analysis revealed that no vertebrate population can fixate even a single mutation through neutral drift once the population passes a certain point."
- note: Vox Day comment, 2026-09-12, on McCarthy's Substack (not previously harvested). 'Portuguese mathematician' = Chalub; the concession of 2026-08-27 (B3g) had already said Ne never enters the Kimura identity.

### Q89 McCarthy thread: selection ceased "since around 1800" (added 2026-10-09)
- source: `McCarthy-comments (Why PZ is Wrong)`; URL: https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1/comment/335325560
- locator: comment id 335325560 (2026-09-12, Vox Day)
- local copy: `sources/raw/refresh-2026-10-09/mccarthy-comments-why/comments.json`
- branch: H
- quote: "natural selection hasn't been performing its real function, keeping the genome from degrading, since around 1800."
- note: Vox Day comment, 2026-09-12. New claim (selection 'ended' ~1800; human genome degrading; fertility decline). Repeated 2026-09-16 (comment 338847889) and 2026-09-18 (Dembski/Hossjer thread, comment 339689335). No parameters given; touches the H branch (cost of selection / deleterious load, claims H7).

### Q90 McCarthy thread: improbability equation "irrelevant" (added 2026-10-09)
- source: `McCarthy-comments (Why PZ is Wrong)`; URL: https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1/comment/337302874
- locator: comment id 337302874 (2026-09-15, Vox Day)
- local copy: `sources/raw/refresh-2026-10-09/mccarthy-comments-why/comments.json`
- branch: G4
- quote: "My improbability equation is irrelevant, as it even says in the book. It's not "wrong" because it doesn't exist."
- note: Vox Day comment, 2026-09-15, replying to McCarthy's Darwillion rebuttal. McCarthy answers on 2026-09-16 (comment 338774739) by quoting the book: 'The probability is one in one Darwillion ... absolute zero.' (claims G4, G3).

### Q91 McCarthy thread: 2nd-edition abstract, 180 fixations, 1,139,000-fold (added 2026-10-09)
- source: `McCarthy-comments (Vox Day Responds)`; URL: https://dennismccarthy.substack.com/p/vox-day-responds/comment/340102853
- locator: comment id 340102853 (2026-09-18, Vox Day)
- local copy: `sources/raw/refresh-2026-10-09/mccarthy-comments-vdr/comments.json`
- branch: A3,A2
- quote: "we calculate that natural selection can accomplish at most 180 fixations on the human lineage given 252,000 generations and 1,400 generations per fixation (the fastest empirical rate ever measured in any organism). This represents 0.000088% of the approximately 205 million fixations required on the human lineage. The shortfall is 1,139,000-fold."
- note: Vox Day comment, 2026-09-18, quoting the Probability Zero 2nd-edition abstract. Check: 252,000/1,400 = 180; 180/205e6 = 8.78e-7 = 0.0000878%; 205e6/180 = 1,138,889. Same comment: 'That is my core argument. Kimura and neutral theory don't even begin to enter into it.'

### Q92 McCarthy thread: scope statement, vertebrate mammals (added 2026-10-09)
- source: `McCarthy-comments (Vox Day Responds)`; URL: https://dennismccarthy.substack.com/p/vox-day-responds/comment/339391408
- locator: comment id 339391408 (2026-09-17, Vox Day)
- local copy: `sources/raw/refresh-2026-10-09/mccarthy-comments-vdr/comments.json`
- branch: ROOT
- quote: "I am specifically and literally claiming that no vertebrate mammalian species has ever originated through evolution by natural selection, by genetic drift, or any combination thereof."
- note: Vox Day comment, 2026-09-17. Scope statement: vertebrate mammals, any mechanism combination. Compare ROOT-excluded-mechanisms; contrast with the 'ceiling' reading offered by an ally (C-series, The Deuce).

### Q93 McCarthy thread: "over 10,000 ... will not fixate at all" (added 2026-10-09)
- source: `McCarthy-comments (Why PZ is Wrong)`; URL: https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1/comment/337074301
- locator: comment id 337074301 (2026-09-14, Vox Day)
- local copy: `sources/raw/refresh-2026-10-09/mccarthy-comments-why/comments.json`
- branch: B2
- quote: "In any population over 10,000, neutral substitution will not fixate at all."
- note: Vox Day comment, 2026-09-14 (Hard Limits ceiling restated as a population-size cutoff; claims B2, B2b). Same comment gives t = 4Ne = 40,000 generations = 1,000,000 years at 25 y.

### Q94 Hossjer thread: 3x more deleterious than neutral (added 2026-10-09)
- source: `Hossjer-review-comments`; URL: https://billdembski.substack.com/p/a-review-of-vox-days-main-argument/comment/339689335
- locator: comment id 339689335 (2026-09-18, Vox Day)
- local copy: `sources/raw/refresh-2026-10-09/dembski-a-review-of-vox-days-main-argument/comments.json`
- branch: H
- quote: "With 3x more deleterious mutations than neutral ones now drifting freely, the human genome is degrading."
- note: Vox Day comment, 2026-09-18, on Dembski's Substack. '3x more harmful mutations than neutral ones' is also asserted 2026-09-15 (comment 337302874 on McCarthy's Substack); McCarthy's MC-2 post is the earlier source for the 3x figure (bib MC-2).

### Q95 McCarthy thread: book quote, 1,017 fixations per generation (added 2026-10-09)
- source: `McCarthy-comments (Why PZ is Wrong)`; URL: https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1/comment/337302874
- locator: comment id 337302874 (2026-09-15, Vox Day)
- local copy: `sources/raw/refresh-2026-10-09/mccarthy-comments-why/comments.json`
- branch: G,B5
- quote: "mutations can spread through populations by random chance alone, fixating 1,017 times per generation, without needing natural selection at all."
- note: Vox Day comment, 2026-09-15, quoting Probability Zero ('Chapter 10', parallel drift) as the defenders' position. The figure 1,017 per generation is not derived in the comment; compare the critics' per-generation rates (claims B5, B5a-B5c, A5). Book not accessible, so this is the comment's quotation of the book (secondhand).

### Q96 McCarthy thread: "genetic drift isn't happening at all over the last 7000 years" (added 2026-10-09)
- source: `McCarthy-comments (Why PZ is Wrong)`; URL: https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1/comment/335823489
- locator: comment id 335823489 (2026-09-13, Vox Day)
- local copy: `sources/raw/refresh-2026-10-09/mccarthy-comments-why/comments.json`
- branch: C,B2
- quote: "And we've now got hard evidence that genetic drift isn't happening at all over the last 7000 years, and that there is a hard population limit on the neutral pipeline."
- note: Vox Day comment, 2026-09-13. Restates claim C (aDNA 'zero fixation') as 'no drift' and ties it to the Hard Limits ceiling (B2). Z23046531 (2026-09-29, 1 and 3 completions) post-dates this comment; R4 C1/C1b found the aDNA counts at or mildly above neutral expectation, which is not the same as 'no drift'.


### Q97 Less Than Zero: CSAC headline "35 million SNVs and 5 million indels affecting roughly 90 million base pairs" (added 2026-10-09)
- source: `B2026-04-28-less-than-zero-3` (blog post dated 2026-04-28); URL: https://voxday.net/2026/04/28/less-than-zero-3/
- locator: ¶5 of extracted text
- local copy: `sources/raw/day/blog-2026-04-28-less-than-zero-3.txt`
- branch: A3,A3x
- quote: "The headline number from that paper was approximately 35 million single nucleotide differences and 5 million indels affecting roughly 90 million base pairs of sequence. Forty million differences out of three billion base pairs. About 1.2 percent."
- note: Day himself describes the 2005 count as 35M SNVs plus 5M indels (events) spanning ~90M bp, "Forty million differences": so his first-edition "40 million" is an event count, not a bp count (compare Q75, Q74). Cited in R4-GAP07b (Day-side review minor 8).

### Q98 Less Than Zero: requirement rises "from 20 million fixations to roughly 207 million" (added 2026-10-09)
- source: `B2026-04-28-less-than-zero-3` (blog post dated 2026-04-28); URL: https://voxday.net/2026/04/28/less-than-zero-3/
- locator: ¶18 of extracted text
- local copy: `sources/raw/day/blog-2026-04-28-less-than-zero-3.txt`
- branch: A3a
- quote: "Since the genuine chimp-human divergence is 415 million base pairs rather than 40 million, the requirement on the human lineage rises from 20 million fixations to roughly 207 million. A maximum of 91 fixations on the human lineage in the time available was the ceiling before, and it remains the ceiling now. The shortfall ratio rises from 220,000-fold to more than 2.3 million-fold against the chimp-human gap alone."
- note: Point statement (415M bp -> ~207M fixations on the human lineage) before the two-row framing of 2026-05-13 (Q101-Q103). 415 vs the later 410 (Q15, Q74) is a version drift.

### Q99 Less Than Zero: one event, one fixation; bp counting is "generous to the standard model" (added 2026-10-09)
- source: `B2026-04-28-less-than-zero-3` (blog post dated 2026-04-28); URL: https://voxday.net/2026/04/28/less-than-zero-3/
- locator: ¶19 of extracted text
- local copy: `sources/raw/day/blog-2026-04-28-less-than-zero-3.txt`
- branch: A3a,A3x
- quote: "And every structural difference longer than a single base pair makes the problem mathematically worse, not better. A point mutation requires one mutation event and one fixation event. A 50,000 base pair insertion or a chromosomal inversion requires the entire structural rearrangement to occur as a single low-probability event and then to fix. Counting these by base pair, as the gap-divergence figure does, is generous to the standard model. Counting them by independent fixation events would be more devastating still."
- note: Day's stated rationale for the bp count: a weighting claim. An SV is "a single low-probability event" that must then fix; bp counting is said to be the generous (low) treatment; counting by independent fixation events "would be more devastating still". Not in A3x before R4-GAP07b (A3x said Day gave no defence).

### Q100 Less Than Zero: structural variation is "with very few exceptions, post-divergence" (added 2026-10-09)
- source: `B2026-04-28-less-than-zero-3` (blog post dated 2026-04-28); URL: https://voxday.net/2026/04/28/less-than-zero-3/
- locator: ¶25 of extracted text (last two sentences)
- local copy: `sources/raw/day/blog-2026-04-28-less-than-zero-3.txt`
- branch: A3a,A3c
- quote: "It is a structural rearrangement that occurred in a specific lineage at a specific time, and either fixed or did not fix. ILS cannot sort what was never segregating. Structural variation is, with very few exceptions, post-divergence, and it must be accounted for by the same fixation arithmetic that the SNPs already break."
- note: Relevant to polymorphism correction (A3c): Day holds that SVs were not segregating in the ancestor, so the CSAC 14-22% polymorphic share (an SNV estimate) would not apply to them. The polymorphic share of indels/SVs is unmeasured (R4-GAP07b).

### Q101 Reddit Takes on PROBABILITY ZERO: "The answer is that it doesn't matter" (multi-bp mutations) (added 2026-10-09)
- source: `B2026-05-13-reddit-takes-on-probability-zero` (blog post dated 2026-05-13); URL: https://voxday.net/2026/05/13/reddit-takes-on-probability-zero/
- locator: ¶4 of extracted text (answers the objection quoted in ¶3)
- local copy: `sources/raw/day/blog-2026-05-13-reddit-takes-on-probability-zero.txt`
- branch: A3a,A3x
- quote: "This is the most substantive question in the thread, which is presumably why it’s the one that inspires the least engagement. The answer is that it doesn’t matter."
- note: Answer to Objection 1 (¶3: "does he count those as single events or as hundreds of thousands of mutations each?").

### Q102 Reddit Takes on PROBABILITY ZERO: Yoo numbers, "35 million ... on the human lineage ... Total: about 205 million" (added 2026-10-09)
- source: `B2026-05-13-reddit-takes-on-probability-zero` (blog post dated 2026-05-13); URL: https://voxday.net/2026/05/13/reddit-takes-on-probability-zero/
- locator: ¶5 of extracted text
- local copy: `sources/raw/day/blog-2026-05-13-reddit-takes-on-probability-zero.txt`
- branch: A3a
- quote: "In Yoo et al. (2025) the complete telomere-to-telomere assemblies of all great ape genomes are published. The Yoo numbers give us approximately 35 million single-nucleotide variants on the human lineage, plus 1,140 interspecific inversions, plus ~187 Mb of structurally divergent sequence. Total: about 205 million genomic differences requiring explanation."
- note: FLAG: "approximately 35 million single-nucleotide variants on the human lineage" (CSAC's 35M is a two-lineage total) and "Total: about 205 million" (the 205M is the per-lineage half of 410M, ¶7). Lineage/total mix-up inside one paragraph; measured human-derived SNVs are ~17.3M (R4-GAP07b).

### Q103 Reddit Takes on PROBABILITY ZERO: SNV-only to bp-per-SV as a range; SVs as single events "the maximally generous treatment" (added 2026-10-09)
- source: `B2026-05-13-reddit-takes-on-probability-zero` (blog post dated 2026-05-13); URL: https://voxday.net/2026/05/13/reddit-takes-on-probability-zero/
- locator: ¶6 of extracted text
- local copy: `sources/raw/day/blog-2026-05-13-reddit-takes-on-probability-zero.txt`
- branch: A3a,A3b,A3x
- quote: "Now, the critic’s excuse is to say “but inversions and structural variants are single events, not millions of mutations.” Fine. Discount every structural variant in the Yoo data to zero. Count nothing but single-nucleotide variants. The shortfall on the SNV-only subset is still four to five orders of magnitude. Going the other direction — counting every base pair in every structural variant as a separate mutation — pushes the shortfall to six orders of magnitude. The conclusion holds either way. Counting structural variants as single events is the maximally generous treatment, and the model still fails."
- note: Day's two-row range: SNV-only = lower bracket (4-5 orders of magnitude), every bp of every SV counted separately = upper bracket (6 orders). "Discount every SV to zero" drops the ~4.3M indel events too (~10% of events), so it is an SNV floor and not an event count (R4-GAP07b). Compare MITTENS 3.0 s7.3 (Q16).

### Q104 McCarthy thread: drift would have caused extinction "within centuries" (added 2026-10-09)
- source: `McCarthy-comments (Why PZ is Wrong)`; URL: https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1/comment/337302874
- locator: comment id 337302874 (2026-09-15, Vox Day), last paragraph
- local copy: `sources/raw/refresh-2026-10-09/mccarthy-comments-why/comments.json`
- branch: B,H
- quote: "So if genetic drift were capable of producing actual changes to the genome, the human species would have been rendered infertile and gone extinct within centuries."
- note: Premises in the same comment: "1. For neutral substitution to work to fixation at its maximum speed, natural selection cannot be operating." and "2. There are 3x more harmful substitutions than neutral substitutions." Claim B9. Verified against the saved comment text during the 2026-10-09 integration.

### Q105 McCarthy thread: "1/2Nₑ is the fixation probability for a neutral mutation" (added 2026-10-09)
- source: `McCarthy-comments (Why PZ is Wrong)`; URL: https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1/comment/337302874
- locator: comment id 337302874 (2026-09-15, Vox Day), fourth paragraph
- local copy: `sources/raw/refresh-2026-10-09/mccarthy-comments-why/comments.json`
- branch: B3a,B3g
- quote: "1/2Nₑ is the fixation probability for a neutral mutation. It is not a general fixation probability that applies to all mutations. There are 3x more harmful mutations than neutral ones."
- note: Restates 1/(2Nₑ) nineteen days after the 2026-08-27 concession that Nₑ never enters the Kimura identity (B3g; versions.md "N vs Nₑ in k"). The same comment says "every single neutral substitution requires ~one million years apiece to fixate" (Q104's comment). Its second sentence is the premise that makes B9 a non-sequitur.

### Q106 Z18525185 s3.1: sample "restricted ... to European samples (n = 8,738)" (added 2026-10-09)
- source: `Z18525185` (Zenodo pub. 2026-02-08, "The Recalibration of the Molecular Clock"); URL: https://zenodo.org/records/18525185
- locator: section 3.1, ¶57 of zenodo-18525185.txt
- local copy: `sources/raw/day/zenodo-18525185.txt`
- branch: C
- quote: "We restricted analysis to European samples (n = 8,738) to maintain population continuity and minimize confounding from population structure."
- note: Sample definition is only "European samples"; no country list, coordinate rule, quality filter or damage treatment is stated. Source for the C1c/C1d sample reconstruction.

### Q107 Z18525185 s3.3: the fixation-event rule (added 2026-10-09)
- source: `Z18525185` (Zenodo pub. 2026-02-08, "The Recalibration of the Molecular Clock"); URL: https://zenodo.org/records/18525185
- locator: section 3.3, ¶72 of zenodo-18525185.txt
- local copy: `sources/raw/day/zenodo-18525185.txt`
- branch: C
- quote: "A "fixation event" was recorded when an allele that was polymorphic (<100%) in an earlier bin reached 100% frequency in a later bin."
- note: The rule that C1b/C1c/C1d implement as E1/E2 eligibility. "<100%" includes 0%; no minimum count of calls is stated.

### Q108 Z18525185 s3.3: "22,428 alleles that reached fixation" (added 2026-10-09)
- source: `Z18525185` (Zenodo pub. 2026-02-08, "The Recalibration of the Molecular Clock"); URL: https://zenodo.org/records/18525185
- locator: section 3.3, ¶73 of zenodo-18525185.txt
- local copy: `sources/raw/day/zenodo-18525185.txt`
- branch: C
- quote: "We identified 22,428 alleles that reached fixation between the earliest samples (Neolithic, 6000-8000 BP) and modern Europeans (<500 BP)."
- note: Source of the 22,428 eligible count; the "Neolithic" pool is 6000-8000 BP (bins 6000-7000 and 7000-8000).

### Q109 Z18525185 s3.4: dating rule "oldest time bin in which the allele appeared fixed" (added 2026-10-09)
- source: `Z18525185` (Zenodo pub. 2026-02-08, "The Recalibration of the Molecular Clock"); URL: https://zenodo.org/records/18525185
- locator: section 3.4, ¶75 of zenodo-18525185.txt
- local copy: `sources/raw/day/zenodo-18525185.txt`
- branch: C
- quote: "This was determined as the oldest time bin in which the allele appeared fixed, working backward from the present."
- note: Ambiguous between T2 (oldest bin at 100%, gaps allowed) and T1 (start of the unbroken run to the present); C1c review #5 and C1d show only T2 can produce the published profile.

### Q110 Z18525185 s4.1: "tracked timing for 16,299 ... insufficient coverage in intermediate time bins" (added 2026-10-09)
- source: `Z18525185` (Zenodo pub. 2026-02-08, "The Recalibration of the Molecular Clock"); URL: https://zenodo.org/records/18525185
- locator: section 4.1, ¶78 of zenodo-18525185.txt
- local copy: `sources/raw/day/zenodo-18525185.txt`
- branch: C
- quote: "Of 22,428 alleles that reached fixation, we successfully tracked timing for 16,299 (the remainder had insufficient coverage in intermediate time bins)."
- note: The coverage threshold is not stated; the C1d minimum-call grid tries to find it.

### Q111 Z18525185 s4.3: "completion events for alleles already near fixation" (added 2026-10-09)
- source: `Z18525185` (Zenodo pub. 2026-02-08, "The Recalibration of the Molecular Clock"); URL: https://zenodo.org/records/18525185
- locator: section 4.3, ¶139 of zenodo-18525185.txt
- local copy: `sources/raw/day/zenodo-18525185.txt`
- branch: C
- quote: "This confirms that essentially all "fixations" were completion events for alleles already near fixation—not new substitutions traversing the frequency spectrum."
- note: Day's own description of the 22,428; the C1d real-data run confirms it in kind (98.8% of v62 eligible alleles start at 95-100% in the Neolithic).

### Q112 Z18525185 Appendix B: data availability names only the AADR (added 2026-10-09)
- source: `Z18525185` (Zenodo pub. 2026-02-08, "The Recalibration of the Molecular Clock"); URL: https://zenodo.org/records/18525185
- locator: Appendix B, ¶301 of zenodo-18525185.txt
- local copy: `sources/raw/day/zenodo-18525185.txt`
- branch: C
- quote: "Analysis was performed on the Allen Ancient DNA Resource (AADR) v62.0, publicly available at the Reich Lab website."
- note: The "21" paper makes no code-availability statement (no "script", "code" or "github" in its text). The scripts sentence is in Z23046531 s5 (next entries).

### Q113 Z23046531 s2.2: two periods, date = 0 moderns, 1,372 / 680 (added 2026-10-09)
- source: `Z23046531` (Zenodo pub. 2026-09-29, record modified 2026-09-29); URL: https://zenodo.org/records/23046531
- locator: p.2, section 2.2
- local copy: `sources/raw/day/zenodo-23046531.txt`
- branch: C
- quote: "Two temporal groups were defined: a Neolithic period (6000–8000 BP) and a modern period (date = 0, i.e., present-day)."
- note: Followed by "The v62 run yielded 1,372 Neolithic and 680 modern European samples." (same section) and, for v66, 395 and 441. The country list is not published ("identical country lists").

### Q114 Z23046531 s2.3: autosomes only, minimum of 100 genotyped samples per period (added 2026-10-09)
- source: `Z23046531` (Zenodo pub. 2026-09-29, record modified 2026-09-29); URL: https://zenodo.org/records/23046531
- locator: p.2, section 2.3
- local copy: `sources/raw/day/zenodo-23046531.txt`
- branch: C
- quote: "Autosomal SNPs only were analyzed; X and Y chromosome loci were excluded. SNPs were required to have a minimum of 100 genotyped samples in each period."
- note: The only stated call-count filter in either Day aDNA paper; it applies to the two-period statistic of Z23046531, not stated for the 11-bin statistic of Z18525185.

### Q115 Z23046531 s2.4: frequency = minor-allele proportion among genotyped individuals (added 2026-10-09)
- source: `Z23046531` (Zenodo pub. 2026-09-29, record modified 2026-09-29); URL: https://zenodo.org/records/23046531
- locator: p.2, section 2.4
- local copy: `sources/raw/day/zenodo-23046531.txt`
- branch: C
- quote: "Allele frequencies were estimated as the proportion of the minor allele among genotyped individuals in each period."
- note: Individual-based frequency; pseudo-haploid individuals count as one genotyped individual.

### Q116 Z23046531 s5: "Analysis scripts are available from the authors at Zenodo." (added 2026-10-09)
- source: `Z23046531` (Zenodo pub. 2026-09-29, record modified 2026-09-29); URL: https://zenodo.org/records/23046531
- locator: p.7, section 5 (Data Availability)
- local copy: `sources/raw/day/zenodo-23046531.txt`
- branch: C
- quote: "Analysis scripts are available from the authors at Zenodo."
- note: The only code statement in the Day aDNA papers. Ambiguous: "available from the authors" can mean on request. No code file is attached to or linked from any Zenodo record found (C1d search, 2026-10-09). Applies to the two-period statistic of this paper.

### Q117 Z23046531 s2.1: v62.0 PACKEDANCESTRYMAP; v66.p1 TGENO converted by PLINK 2 (added 2026-10-09)
- source: `Z23046531` (Zenodo pub. 2026-09-29, record modified 2026-09-29); URL: https://zenodo.org/records/23046531
- locator: p.2, section 2.1
- local copy: `sources/raw/day/zenodo-23046531.txt`
- branch: C
- quote: "Data was distributed in TGENO format and converted to PACKEDANCESTRYMAP format via PLINK 2 for analysis."
- note: Said of v66.p1. For v62.0 the same section says the data were "distributed in PACKEDANCESTRYMAP format". The v62.0.p1 file retrieved in 2026-10-09 is TGENO.


## Refresh 2026-10-09b quotes (Q118-Q126; added 2026-10-09 evening, second pass)
All quotes machine-checked as substrings (whitespace and quote-mark normalised) of the local raw copy under `sources/raw/refresh-2026-10-09b/` (gitignored).

### Q118 Mailvox: "7 billion x 0.0857 is not 410,000,000 but 599,900,000" (added 2026-10-09b)
- source: `B2026-10-09-mailvox-invoking-the-triveritas`; URL: https://voxday.net/2026/10/09/mailvox-invoking-the-triveritas/
- locator: post body, final third (published 2026-10-09T15:32 UTC)
- local copy: `sources/raw/refresh-2026-10-09b/day-post-2026-10-09-mailvox-invoking-the-triveritas/page.html`
- branch: A3, A3x, F
- quote: "at which point we realize that Yoo et al can’t possibly be correct because 7 billion x 0.0857 is not 410,000,000 but 599,900,000."
- note: Day's new objection to the Yoo 2025 total (410 Mb). Harvester arithmetic: 7e9 x 0.0857 = 599.9e6 (the product is right). What 7 billion denotes is not stated (the ape haplotype assemblies in Yoo 2025 Table 1 are 3.0-3.6 Gb each, so a sum of two haplotypes is about 6-7 Gb; "7 billion" is at best a rounded two-genome total; this reading is the harvester's, not in the post). The 8.57 percent is Day's own figure (Q119); the string "8.57" does not occur in the extracted text of CSAC 2005 or Yoo 2025 (grep, 0 hits each).

### Q119 Mailvox: CSAC partial genomes "at least 8.57 percent different based on size alone" (added 2026-10-09b)
- source: `B2026-10-09-mailvox-invoking-the-triveritas`; URL: https://voxday.net/2026/10/09/mailvox-invoking-the-triveritas/
- locator: post body, paragraph on the 2005 Nature paper
- local copy: as Q118
- branch: A3, F
- quote: "But those partial genomes were at least 8.57 percent different based on size alone!"
- note: Day on CSAC 2005 (1.06 percent fixed divergence from "two partial genomes"). Not located in the CSAC text: CSAC reports 1.23 percent substitution divergence (1.06 percent or less fixed) over about 2.4 Gb of aligned high-quality sequence and about 90 Mb of indel differences (about 3 percent). How the 8.57 percent is computed is not given in the post. Bears on the GAP-07 / A3x unit question (substitutions vs indel base pairs vs events).

### Q120 Mailvox: "Yoo reported a total genomic difference of 410 million base pairs" (added 2026-10-09b)
- source: `B2026-10-09-mailvox-invoking-the-triveritas`; URL: https://voxday.net/2026/10/09/mailvox-invoking-the-triveritas/
- locator: post body
- local copy: as Q118
- branch: A3, A3x
- quote: "Yoo reported a total genomic difference of 410 million base pairs."
- note: Day states that the 410 million is in base pairs, and (Q121) that he halves it to get the 205 million used as "fixations". This is the unit mismatch of A3x/GAP-07 in Day's own words (base pairs divided by two = "fixations"). The searched Yoo 2025 text/SI never contained a "410" (see harvest-log-literature "Not found").

### Q121 Mailvox: "I therefore divided that difference in two" (added 2026-10-09b)
- source: `B2026-10-09-mailvox-invoking-the-triveritas`; URL: https://voxday.net/2026/10/09/mailvox-invoking-the-triveritas/
- locator: post body, same paragraph as Q120
- local copy: as Q118
- branch: A3, A3d
- quote: "I therefore divided that difference in two"
- note: Day's explanation of the halving; he adds that the direction (chimp vs human side) "doesn't matter in the slightest to my mathematical disproof". Compare Hancock's "2n" point and justatest90's defence (RF-11, claim A3d1).

### Q122 The Irrelevance of EES: adaptive space "at most 2 percent of the average genome" (added 2026-10-09b)
- source: `B2026-10-09-the-irrelevance-of-ees`; URL: https://voxday.net/2026/10/09/the-irrelevance-of-ees/
- locator: post body, paragraph beginning "The reason that it took me less than 30 seconds" (published 2026-10-09T09:13 UTC)
- local copy: `sources/raw/refresh-2026-10-09b/day-post-2026-10-09-the-irrelevance-of-ees/page.html`
- branch: ROOT-excluded-mechanisms, E, H
- quote: "all of the ESS arguments are focused on the adaptive space that natural selection can effect, which a) are at most 2 percent of the average genome and b) don’t even begin to address the same fixation problem that eliminates the possibility of natural selection as a significant generative force."
- note: Day writes "ESS" where the surrounding text means EES (the post's own heading and the quoted Hilbert text use EES; he separately defines ESS as Evolutionary Stable Strategy). Two checkable points: (a) "at most 2 percent" adaptive fraction (compare CSAC/Keightley-type constrained-fraction estimates in PA-19; Day's earlier use of 2 percent); (b) the "same fixation problem" is the claim under audit, so the sentence is circular as a response to EES. Q82 earlier: "totally unfamiliar" with EES.

### Q123 The Irrelevance of EES: "natural selection is empirically irrelevant" (added 2026-10-09b)
- source: `B2026-10-09-the-irrelevance-of-ees`; URL: https://voxday.net/2026/10/09/the-irrelevance-of-ees/
- locator: post body, final paragraphs
- local copy: as Q122
- branch: ROOT, ROOT-newdisproof-pending
- quote: "But now I have conclusively proven one more thing: natural selection is empirically irrelevant as an evolutionary mechanism."
- note: Third announced result after "evolution by natural selection is mathematically impossible" and "evolution by neutral drift is both mathematically and empirically" impossible (same paragraph; the sentence is cut by the page, read the post). No paper, data or code is cited. This is the "epic data analysis" teased on 2026-10-07 (Q84), now asserted as proven. Nothing to check until it is published; pre-register the check when it appears.

### Q124 The Irrelevance of EES: the simulation resource (added 2026-10-09b)
- source: `B2026-10-09-the-irrelevance-of-ees`; URL: https://voxday.net/2026/10/09/the-irrelevance-of-ees/
- locator: post body, last paragraph
- local copy: as Q122
- branch: ROOT, simulator
- quote: "there is one thing game designers have that no scientists do. And that is unlimited 24-7 access to 96 cores with 512GB RAM and a multicore monster GPU with 96GB RAM"
- note: Indicates the unpublished analysis is a simulation or data run on Day's own hardware, to be discussed on UATV "tonight" (2026-10-09). Relevant to the planned simulator project: a likely target for replication once code or parameters appear. Resources are a statement, not a method.

### Q125 Sigma Game 2026-01-09 "We Knew How This Would Go": parallel fixation "INCLUDED" (added 2026-10-09b; backfill)
- source: `SG-2026-01-09-we-knew-how-this-would-go`; URL: https://sigmagame.substack.com/p/we-knew-how-this-would-go
- locator: Day's reply ("VD:") to a commenter, point 1
- local copy: `sources/raw/refresh-2026-10-09b/substack/sg-wkhtwg/post.json`
- branch: B5, G, A2
- quote: "The 1,600 generations per fixation rate INCLUDES parallel fixation."
- note: Early statement (2026-01-09, 1,600 gens/fixation) that the LTEE-derived rate already includes parallel fixation. The later versions (1,400; 1,322; 1,587) are the same rate under different counting rules (A2b); the claim that parallel fixation is "included" is the premise defended against the "parallel drift" objection (Q95, B5).

### Q126 Sigma Game 2026-01-09: "Those 40 million fixations" (added 2026-10-09b; backfill)
- source: `SG-2026-01-09-we-knew-how-this-would-go`; URL: https://sigmagame.substack.com/p/we-knew-how-this-would-go
- locator: Day's reply, point 2
- local copy: as Q125
- branch: A3, A3x
- quote: "Those 40 million fixations must be accounted for."
- note: Version datum: "40 million fixations" (2026-01-09) vs 205 million (second-edition abstract, Q91) for the human-chimp comparison; earlier-edition figures are in the existing Q-series. Also ties "both the human and chimp genomes have been mapped" to the count. Added to `ledgers/versions.md`.

## Refresh 2026-10-09c quotes (Q127-Q129; added 2026-10-09 evening, third pass; the three lines flagged in `prereg-2026-10-09-day-uatv-analysis.md` as having no Q-id)

### Q127 An Epic Test: "an epic data analysis" (added 2026-10-09c)
- source: `B2026-10-07-an-epic-test`; URL: https://voxday.net/2026/10/07/an-epic-test/
- locator: post body, para 2, same paragraph as Q84 (Q84's quote stops before it)
- local copy: `sources/raw/refresh-2026-10-09c/post-an-epic-test/p.html` (sha256 a2678a50394ae6b4...; verified verbatim by normalised substring test, 2026-10-09 19:05 MDT)
- branch: ROOT
- tag (rule RH): rhetoric (teaser) with a dialectical core: a *data* analysis, not only a model, was running on 2026-10-07
- quote: "we’re currently running an epic data analysis that is going to break new ground and might even reveal a few surprises"
- note: Same paragraph: "I'm not going to say anything more about it at the moment". Unpublished as of 2026-10-09 19:05 MDT.

### Q128 The Irrelevance of EES: "UATV tonight" (added 2026-10-09c)
- source: `B2026-10-09-the-irrelevance-of-ees`; URL: https://voxday.net/2026/10/09/the-irrelevance-of-ees/
- locator: post body, last paragraph, sentence after Q124
- local copy: `sources/raw/refresh-2026-10-09c/post-the-irrelevance-of-ees/p.html` (sha256 eb95a166533bfa6d..., identical to the 09b copy; verified verbatim)
- branch: ROOT, simulator
- tag (rule RH): dialectic-adjacent announcement (logistics); not scored
- quote: "as well as the knowledge of how to effectively make use of that kind of computing power. Which is something we’ll be discussing with the people who made it possible on UATV tonight."
- note: The discussion is promised for the evening of 2026-10-09 with "the people who made it possible" (collaborators or sponsors). The post tags are evolution, science, technology, UATV.

### Q129 No Reconciliation: "my most recent work" (added 2026-10-09c; 2026-10-06 post, first pass 09b)
- source: `B2026-10-06-no-reconciliation`; URL: https://voxday.net/2026/10/06/no-reconciliation/
- locator: post body, Day's reply after the quoted critic line
- local copy: `sources/raw/refresh-2026-10-09b/day-post-2026-10-06-no-reconciliation/page.html` (verified verbatim, 2026-10-09 19:05 MDT)
- branch: ROOT
- tag (rule RH): rhetoric (prophecy about critics' eventual agreement); core: "most recent work" existed by 2026-10-06
- quote: "Actually, based on my most recent work, I genuinely believe they will all eventually come around to my way of thinking with regards to evolution and population genetics."
- note: Not a result; a forecast. Scored as nothing until the work is public.

## R4 A2e integration quotes (Q130-Q139; added 2026-10-10)

### Q130 MITTENS 3.0 s2: "unattainable ceiling ... Formula One car"
- source: `Z23003785` (Zenodo pub. 2026-09-28, record modified 2026-10-04); URL: https://zenodo.org/records/23003785
- locator: s2, PDF p.4
- local copy: `sources/raw/day/zenodo-23003785.txt` (page 4; verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: A2e
- tag (rule RH): split (rule RH): "an unattainable ceiling, the absolute best-case scenario" is dialectic (scored in A2e); the Formula One / horse-drawn cart analogy is rhetoric (ledger RH-4)
- quote: "It is an unattainable ceiling, the absolute best-case scenario, the performance of a Formula One car used to benchmark a horse-drawn cart."
- note: Added at R4 A2e integration.

### Q131 MITTENS 3.0 s1/abstract: "the empirical ceiling on what evolution can accomplish"
- source: `Z23003785` (Zenodo pub. 2026-09-28, record modified 2026-10-04); URL: https://zenodo.org/records/23003785
- locator: abstract, PDF p.2
- local copy: `sources/raw/day/zenodo-23003785.txt` (page 2; verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: A2e
- tag (rule RH): dialectic
- quote: "Whatever number the LTEE produces, it is the empirical ceiling on what evolution can accomplish when every tool in its kit is deployed simultaneously under ideal conditions."
- note: The A2e statement; the same passage names "an effectively unlimited mutation supply".

### Q132 MITTENS 3.0 s4.3: 4.1e-4 neutral hitchhikers and 1,408 per beneficial fixation
- source: `Z23003785` (Zenodo pub. 2026-09-28, record modified 2026-10-04); URL: https://zenodo.org/records/23003785
- locator: s4.3, PDF p.7
- local copy: `sources/raw/day/zenodo-23003785.txt` (page 7; verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: A2e, ltee.gens_per_fixation
- tag (rule RH): dialectic
- quote: "neutral hitchhikers ≈ 4.1 × 10⁻⁴ × 50,000 = 20.5. Subtracting from the clone-pair total of 56.0 fixations yields approximately 35.5 beneficial fixations, or 1,408 generations per beneficial fixation."
- note: Day's own adaptive-only reading (G = 1,408); source of the 4.1e-4 per genome per generation used in kappa.

### Q133 MITTENS 3.0 s4.3: "MITTENS measures total throughput"
- source: `Z23003785` (Zenodo pub. 2026-09-28, record modified 2026-10-04); URL: https://zenodo.org/records/23003785
- locator: s4.3, PDF p.7
- local copy: `sources/raw/day/zenodo-23003785.txt` (page 7; verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: A2e, A5c
- tag (rule RH): dialectic
- quote: "This distinction matters for the standard model, not for MITTENS. MITTENS measures total throughput — every fixation, regardless of mechanism."
- note: Basis of the total-throughput route in R4-A2e (F = 50,765 per generation).

### Q134 MITTENS 3.0 s4.2: "the remaining beneficial mutations have smaller effects"
- source: `Z23003785` (Zenodo pub. 2026-09-28, record modified 2026-10-04); URL: https://zenodo.org/records/23003785
- locator: s4.2, PDF p.7
- local copy: `sources/raw/day/zenodo-23003785.txt` (page 7; verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: A2e
- tag (rule RH): dialectic
- quote: "As those are exhausted, the remaining beneficial mutations have smaller effects, take longer to sweep, and are more easily displaced by competing variants."
- note: Day-side reason the human beneficial-effect ratio could be below the LTEE's (decoupled-s rows PH2).

### Q135 MITTENS 3.0 s6.4: 38,400 mutations at 100-fold (3.2e9 x 1.2e-8 x 100)
- source: `Z23003785` (Zenodo pub. 2026-09-28, record modified 2026-10-04); URL: https://zenodo.org/records/23003785
- locator: s6.4, PDF p.11
- local copy: `sources/raw/day/zenodo-23003785.txt` (page 11; verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: A2e, A5h
- tag (rule RH): dialectic
- quote: "A 100-fold increase in mutation rate in the human genome would produce approximately 38,400 mutations per individual per generation (3.2 × 10⁹ bp × 1.2 × 10⁻⁸ × 100)."
- note: Source of the 38.4 per haploid human genome (without the x100) used in kappa = 38.4 / 4.1e-4 = 93,659; Day does not himself form this ratio.

### Q136 MITTENS 3.0 s8.2: LTEE Ne ≈ 3 × 10⁷
- source: `Z23003785` (Zenodo pub. 2026-09-28, record modified 2026-10-04); URL: https://zenodo.org/records/23003785
- locator: s8.2, PDF p.14
- local copy: `sources/raw/day/zenodo-23003785.txt` (page 14; verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: A2e, ltee.Ne_effective
- tag (rule RH): dialectic
- quote: "In the LTEE, with Ne ≈ 3 × 10⁷, the expected time for a single neutral mutation to fix by drift alone is approximately 2Ne = 6 × 10⁷ generations — 30 million generations."
- note: Day-stated LTEE N_e (also in the s2 mechanism list, p.4); no primary-literature source yet.

### Q137 MITTENS 3.0 s8.2: human Ne 10,000–33,000
- source: `Z23003785` (Zenodo pub. 2026-09-28, record modified 2026-10-04); URL: https://zenodo.org/records/23003785
- locator: s8.2, PDF p.14
- local copy: `sources/raw/day/zenodo-23003785.txt` (page 14; verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: A2e
- tag (rule RH): dialectic
- quote: "The human Ne of 10,000–33,000 yields a neutral drift fixation time of 20,000–66,000 generations"
- note: Day's in-paper human N_e range (the A2e sweep used 3,300, 1e4 textbook, and post hoc 3.3e4, 1e5).

### Q138 MITTENS 3.0 s8.6: "faster per generation than bacteria"
- source: `Z23003785` (Zenodo pub. 2026-09-28, record modified 2026-10-04); URL: https://zenodo.org/records/23003785
- locator: s8.6, PDF p.15
- local copy: `sources/raw/day/zenodo-23003785.txt` (page 15; verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: A2e, A2i
- tag (rule RH): dialectic
- quote: "The objection implicitly claims that humans can fix mutations faster per generation than bacteria under ideal conditions."
- note: Day states the comparison per generation; this is why the per-year reading is out of scope under rule S.

### Q139 MITTENS 3.0 s7.3: "At 1,322 gen/fix (non-mutator): 191 achievable."
- source: `Z23003785` (Zenodo pub. 2026-09-28, record modified 2026-10-04); URL: https://zenodo.org/records/23003785
- locator: s7.3, PDF p.13
- local copy: `sources/raw/day/zenodo-23003785.txt` (page 13; verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: A2e, A
- tag (rule RH): dialectic
- quote: "At 1,322 gen/fix (non-mutator): 191 achievable."
- note: Day's own 191; the A2e flip is equivalent to "the human lineage fixed at most about 191 adaptive substitutions" (PH8).

### Q140 Hard Limits abstract: current-size populations show only residual drainage
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: l.23-25 of the local text
- local copy: `sources/raw/day/zenodo-22129121.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B2, B
- tag (rule RH): dialectic
- quote: "What substitution these abundant populations show is not produced at their current size; it is residual drainage from the smaller populations they descend from."
- note: Abstract (R4-B2 cites it as l.22-24; the sentence starts on l.23 of the local text). The current-size confinement of B2 and the ancestral-fill concession used by R4-B2 (rule N).

### Q141 Hard Limits: 10,000 is "the size the field's own methods assign"
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: l.54-56 of the local text
- local copy: `sources/raw/day/zenodo-22129121.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B2, B1c
- tag (rule RH): dialectic
- quote: "It is also, not by accident, the size the field’s own methods assign to the ancestral human population."
- note: H9 in R4-B2. Mentions the field's 1e4; it is not HL's input (HL uses the variance N_e, Q142).

### Q142 Hard Limits: the coalescent N_e is rejected as circular
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: l.110-112 of the local text
- local copy: `sources/raw/day/zenodo-22129121.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B2, B2e, B1c
- tag (rule RH): dialectic
- quote: "But this is circular reasoning: the coalescent Nₑ is estimated from gene-tree depth, and gene-tree depth is itself on the order of 4Nₑ generations, which is on the order of the species’ own duration."
- note: Section "Which Effective Size" (l.101-118). Followed by "We therefore use the variance Nₑ, which is the drift rate, and which no one estimates by assuming the conclusion."

### Q143 Hard Limits: no census is both viable and small enough to fix by drift (H10)
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: l.207-209 of the local text
- local copy: `sources/raw/day/zenodo-22129121.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B2, B
- tag (rule RH): dialectic
- quote: "There is no census at which a large vertebrate is simultaneously large enough to be a viable species and small enough to fix a neutral allele by drift."
- note: H10 in R4-B2. In tension with the drainage thesis (needs viable, small ancestors); stands under rule C as said of the species window (slips ledger).

### Q144 Hard Limits: "The window is not narrow. It is empty."
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: l.209 of the local text
- local copy: `sources/raw/day/zenodo-22129121.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B2
- tag (rule RH): rhetoric
- quote: "The window is not narrow. It is empty."
- note: Figure of speech (rule RH); dialectical core is the current-size claim of Q143/Q140. Ledger RH-8.

### Q145 Hard Limits: the lineage-window objection is valid, the ceiling triples
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: l.252-253 of the local text
- local copy: `sources/raw/day/zenodo-22129121.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B2, B2b
- tag (rule RH): dialectic
- quote: "The objection is valid, the correction triples the ceiling, and the conclusion is not changed."
- note: Accepts the 6.5 My lineage window (Table 1); human ceiling 35,000 to about 114,000.

### Q146 Hard Limits: steady-state flux is mu regardless of transit time
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: l.267-268 of the local text
- local copy: `sources/raw/day/zenodo-22129121.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B2, B2a, B1
- tag (rule RH): dialectic
- quote: "At steady state the total flux out is μ per site regardless of how long any individual site took to traverse."
- note: The throughput concession; the dispute moves to the fill state.

### Q147 Hard Limits: definition k(T) = mu F(T), F = P(tau <= T | fixation)
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: l.287 of the local text
- local copy: `sources/raw/day/zenodo-22129121.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B2, B2a
- tag (rule RH): dialectic
- quote: "k(T) = μ · F(T), F(T) = P(τ ≤ T | fixation)"
- note: H2 in R4-B2. Settles the conditional-on-fixation reading.

### Q148 Hard Limits: the prefactor is "an order-one detail" that "could be wrong by two orders of magnitude"
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: l.303-305 of the local text
- local copy: `sources/raw/day/zenodo-22129121.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B2, B2a
- tag (rule RH): dialectic
- quote: "the constant out front is an order- one detail that could be wrong by two orders of magnitude in either direction without shifting the conclusion at all."
- note: R4-B2 P3: the exact-to-asymptotic ratio is 17.8-47x at T = 2N_e to N_e and grows as a power of N_e/T; about 11 decimal orders at H5; R1-immaterial against 7.8e7 (slips ledger). Note: the extraction breaks the line after "order-"; the hyphen is the line-break hyphen of the PDF text.

### Q149 Hard Limits: six of about 3,000 simulated fixations within a quarter of the mean
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: l.311-312 of the local text
- local copy: `sources/raw/day/zenodo-22129121.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B2, B2a
- tag (rule RH): dialectic
- quote: "Not one of the three thousand fixes in under nineteen percent of the mean."
- note: H4 in R4-B2 (the demonstration: 391 generations against 4Nₑ of 400; six of ~750 expected under the linear guess). Reproduced by the exact chain.

### Q150 Hard Limits: human exponent, exp(−π² · 1.8 × 10⁷)
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: l.330-331 of the local text
- local copy: `sources/raw/day/zenodo-22129121.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B2, B2a
- tag (rule RH): dialectic
- quote: "so the probability that a neutral mutation arising now fixes within that era is of order exp(−π² · 1.8 × 10⁷)"
- note: H5 in R4-B2 (7.8e7 decimal orders, reproduced).

### Q151 Hard Limits: the small number of fixations observed are drainage (H7)
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: l.354-356 of the local text
- local copy: `sources/raw/day/zenodo-22129121.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B2, B
- tag (rule RH): dialectic
- quote: "The small number of fixations we observe are just drainage: the completions of mutations that entered the pipe long ago, when the populations were small and their pipes short enough to fill."
- note: H7 in R4-B2. An ancestral fill is conceded in the text.

### Q152 Hard Limits: near X "the pipe substantially fills"
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: l.362-363 of the local text
- local copy: `sources/raw/day/zenodo-22129121.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B2, B
- tag (rule RH): dialectic
- quote: "When Nₑ is of the same order as T — when a lineage sits near its own X — the exponent is order one: the pipe substantially fills, and Kimura's rate is approached."
- note: R4-B2: at T = N_e the exact flux is 0.3%; fill is substantial near T = 4N_e (0.61). Concedes more than HL's own law gives (slips ledger).

### Q153 Hard Limits: a census near 100,000 held static for 2 My, linear bound about 35% (H8)
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: l.364-366 of the local text
- local copy: `sources/raw/day/zenodo-22129121.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B2, B1d
- tag (rule RH): dialectic
- quote: "a census near a hundred thousand held static for the full two million years, and even the generous linear bound T/4Nₑ stands at about thirty- five percent"
- note: H8 in R4-B2. Pairs a lineage-ceiling census (about 114,000) with the species window (2 My): an internal window mismatch (slips ledger). The extraction breaks the line after "thirty-"; the hyphen is the line-break hyphen.

### Q154 Hard Limits: constant size is "the generous case"
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: l.375-376 of the local text
- local copy: `sources/raw/day/zenodo-22129121.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B2
- tag (rule RH): dialectic
- quote: "This means the constant-size X is the generous case."
- note: l.371-377. Basis of the charitable reading of "best case" in R4-B2 (rule C).

### Q155 Hard Limits: "This hard limit ... does not kill neutral theory"
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: l.427-428 of the local text
- local copy: `sources/raw/day/zenodo-22129121.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B, B2
- tag (rule RH): dialectic
- quote: "Drift does fix neutral alleles, although only in populations small enough and stable enough to permit"
- note: l.425-428; a later softening of the 2026-02-04 blog "flat-out wrong" (versions ledger: revised in HL, rule SC).

### Q156 Hard Limits: a rate "loaded, at least partially" in the Holocene
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: l.440-441 of the local text
- local copy: `sources/raw/day/zenodo-22129121.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B2, B
- tag (rule RH): dialectic
- quote: "rate that was loaded, at least partially, under population conditions that ended in the Holocene."
- note: l.440. Partial ancestral load conceded.

### Q157 Hard Limits peroration: both channels "shut inside the same lineage duration"
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: l.453-456 of the local text
- local copy: `sources/raw/day/zenodo-22129121.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B
- tag (rule RH): reading-dependent (R4 RHclose, RD, 2026-10-11): rhetoric on F over 6.5 My (0.697; recorded alongside, B holds scoped to B2); dialectic on D (0.256), Takahata 1e5 (0.281), S (current size) and 2 My (0.025) (verdict-field reading: B non-sequitur; RD consistency fix 2026-10-11)
- quote: "And now the neutral channel closes on the same window for an entirely independent reason. The adaptive substitutions cannot be paid for; the neutral substitutions cannot be finished, because the pipe that would finish them never fills. Both the priced channel and the free channel shut inside the same lineage duration."
- note: Candidate B Statement (R4-B2, review K2 / D3). Dialectic reading: non-sequitur against HL's own ancestral-fill text (Q140, Q151, Q152, Q156). Rhetoric reading: figurative closing, core = B2, B holds. Integrated 2026-10-11 under RD: B internal `holds` scoped to B2 on the rhetoric reading, `non-sequitur` on the dialectic readings.

### Q158 Hard Limits: "the pipe was nearly empty"
- source: `Z22129121` (Zenodo pub. 2026-08-27, record modified 2026-08-27); URL: https://zenodo.org/records/22129121
- locator: l.467 of the local text
- local copy: `sources/raw/day/zenodo-22129121.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B
- tag (rule RH): reading-dependent (as Q157; R4 RHclose, RD, 2026-10-11)
- quote: "the pipe was nearly empty."
- note: l.464-467: "The pipe is exactly as long as Kimura said it was. It was always that long. The field simply never turned around to look at the near end and observe that, for every large animal it had ever dated, the pipe was nearly empty."

### Q159 Education of a Population Geneticist: "Brian doesn't know the related literature"
- source: blog; URL: https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/; 2026-10-01
- locator: ¶7 of the extracted text
- local copy: `sources/raw/day/blog-2026-10-01-the-education-of-a-population-geneticist.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B3d
- tag (rule RH): rhetoric
- quote: "Brian doesn’t know the related literature and he hasn’t done the relevant math."
- note: Wrapper sentence after the k = 32.3μ claim (B3-3 in R4-B3). Ledger RH-5. The preceding sentence (B3d-1, the 32.3 claim) is dialectic.

### Q160 Education of a Population Geneticist: the ancestral pipeline "was full and 228,000 generations long"
- source: blog; URL: https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/; 2026-10-01
- locator: ¶36 of the extracted text
- local copy: `sources/raw/day/blog-2026-10-01-the-education-of-a-population-geneticist.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B1d, B2
- tag (rule RH): dialectic
- quote: "At the time of the CHLCA split, we can assume that it was full and 228,000 generations long"
- note: B1d. 228,000 = 4 x 57,143 (the census of Hard Limits H8). Day grants a full pipe at the split (R4-B2).

### Q161 A Retraction and a Revision: Bergeron (2023), 55 vertebrate species
- source: blog; URL: https://voxday.net/2026/05/07/a-retraction-and-a-revision/; 2026-05-07
- locator: ¶3 of the extracted text
- local copy: `sources/raw/day/blog-2026-05-07-a-retraction-and-a-revision.txt` (verified verbatim by whitespace-normalised substring test, 2026-10-10)
- branch: B3d
- tag (rule RH): dialectic
- quote: "The new validation work which uses Bergeron et al. (2023) on pedigree mutation rates and fossil-calibrated substitution rates for 55 vertebrate species"
- note: The source of the "median factor of 25 across 55 vertebrates" (R4-B3 C10: the figure is cited, not unsourced).

### Q162 The Fourth Mechanism (FM1), ¶3
- source: voxday.net, "The Fourth Mechanism"; URL: https://voxday.net/2026/10/10/the-fourth-mechanism/ ; published 2026-10-10 13:37:48 UTC (modified 15:46:51 UTC)
- locator: ¶3 of the entry content
- local copy: `sources/raw/refresh-2026-10-10/post/fm.html` (sha256 fc618dcc…65647; verified verbatim as a substring of the saved page text with curly apostrophes normalised, 2026-10-10)
- branch: FM1 (mesas / sigillation), ROOT
- tag (rule RH): dialectic (method statement)
- quote: "I looked into that by utilizing Unauthorized's twin 96-core 512GB RAM beasts to analyze all six complete ape genomes provided by the T2T Primate Consortium."
- note: Refresh 2026-10-10 (docs/research/sources/refresh-2026-10-10.md), id FM1.

### Q163 The Fourth Mechanism (FM2), ¶3
- source: voxday.net, "The Fourth Mechanism"; URL: https://voxday.net/2026/10/10/the-fourth-mechanism/ ; published 2026-10-10 13:37:48 UTC (modified 15:46:51 UTC)
- locator: ¶3 of the entry content
- local copy: `sources/raw/refresh-2026-10-10/post/fm.html` (sha256 fc618dcc…65647; verified verbatim as a substring of the saved page text with curly apostrophes normalised, 2026-10-10)
- branch: FM1 (mesas / sigillation), ROOT
- tag (rule RH): dialectic (hedged)
- quote: "Analysis of the fine-grained distribution of substitutions across the human genome now suggests that relictation cannot be the whole story and may not be the only discrete mechanism at work."
- note: Day revises his own earlier mechanism downward.

### Q164 The Fourth Mechanism (FM3), ¶4
- source: voxday.net, "The Fourth Mechanism"; URL: https://voxday.net/2026/10/10/the-fourth-mechanism/ ; published 2026-10-10 13:37:48 UTC (modified 15:46:51 UTC)
- locator: ¶4 of the entry content
- local copy: `sources/raw/refresh-2026-10-10/post/fm.html` (sha256 fc618dcc…65647; verified verbatim as a substring of the saved page text with curly apostrophes normalised, 2026-10-10)
- branch: FM1 (mesas / sigillation), ROOT
- tag (rule RH): dialectic (number; statistic undefined)
- quote: "The substitution density across the genome is massively overdispersed, more than 80 times more variable than a uniform-rate process predicts."
- note: Dispersion statistic and null not defined in the post.

### Q165 The Fourth Mechanism (FM4), ¶4
- source: voxday.net, "The Fourth Mechanism"; URL: https://voxday.net/2026/10/10/the-fourth-mechanism/ ; published 2026-10-10 13:37:48 UTC (modified 15:46:51 UTC)
- locator: ¶4 of the entry content
- local copy: `sources/raw/refresh-2026-10-10/post/fm.html` (sha256 fc618dcc…65647; verified verbatim as a substring of the saved page text with curly apostrophes normalised, 2026-10-10)
- branch: FM1 (mesas / sigillation), ROOT
- tag (rule RH): dialectic
- quote: "Dense regions cluster next to other dense regions, forming contiguous blocks of elevated substitution with sharp boundaries in a pattern we call mesas."
- note: Defines "mesas"; no coordinates or window size released.

### Q166 The Fourth Mechanism (FM5), ¶4
- source: voxday.net, "The Fourth Mechanism"; URL: https://voxday.net/2026/10/10/the-fourth-mechanism/ ; published 2026-10-10 13:37:48 UTC (modified 15:46:51 UTC)
- locator: ¶4 of the entry content
- local copy: `sources/raw/refresh-2026-10-10/post/fm.html` (sha256 fc618dcc…65647; verified verbatim as a substring of the saved page text with curly apostrophes normalised, 2026-10-10)
- branch: FM1 (mesas / sigillation), ROOT
- tag (rule RH): dialectic (number absent)
- quote: "A single mesa on a single chromosome shows an excess of human-lineage substitutions that exceeds both the MITTENS fixation ceiling and the maximum that natural selection can theoretically fix across the entire genome according to Haldane."
- note: Units (SNV vs bp, event vs base) not stated; fidelity of the "Haldane" figure unverifiable.

### Q167 The Fourth Mechanism (FM6), ¶5
- source: voxday.net, "The Fourth Mechanism"; URL: https://voxday.net/2026/10/10/the-fourth-mechanism/ ; published 2026-10-10 13:37:48 UTC (modified 15:46:51 UTC)
- locator: ¶5 of the entry content
- local copy: `sources/raw/refresh-2026-10-10/post/fm.html` (sha256 fc618dcc…65647; verified verbatim as a substring of the saved page text with curly apostrophes normalised, 2026-10-10)
- branch: FM1 (mesas / sigillation), ROOT
- tag (rule RH): rhetoric (rhetorical question)
- quote: "is there too much structured divergence for multiple bottleneck events to credibly account for?"
- note: Dialectical core: mesas may exceed what bottlenecks supply. Slips ledger RH-6.

### Q168 The Fourth Mechanism (FM7), ¶6
- source: voxday.net, "The Fourth Mechanism"; URL: https://voxday.net/2026/10/10/the-fourth-mechanism/ ; published 2026-10-10 13:37:48 UTC (modified 15:46:51 UTC)
- locator: ¶6 of the entry content
- local copy: `sources/raw/refresh-2026-10-10/post/fm.html` (sha256 fc618dcc…65647; verified verbatim as a substring of the saved page text with curly apostrophes normalised, 2026-10-10)
- branch: FM1 (mesas / sigillation), ROOT
- tag (rule RH): dialectic (hypothesis, explicitly open)
- quote: "I propose the term sigillation for the hypothesis that some of these mesa regions represent deliberate genomic modification: discrete engineering events that wrote contiguous blocks of change into one dominate lineage."
- note: Typo "dominate" quoted as is.

### Q169 The Fourth Mechanism (FM8), ¶7
- source: voxday.net, "The Fourth Mechanism"; URL: https://voxday.net/2026/10/10/the-fourth-mechanism/ ; published 2026-10-10 13:37:48 UTC (modified 15:46:51 UTC)
- locator: ¶7 of the entry content
- local copy: `sources/raw/refresh-2026-10-10/post/fm.html` (sha256 fc618dcc…65647; verified verbatim as a substring of the saved page text with curly apostrophes normalised, 2026-10-10)
- branch: FM1 (mesas / sigillation), ROOT
- tag (rule RH): mixed: (a) dialectic; (b) and (c) dialectic claims with "beyond any dispute" as rhetorical intensifier
- quote: "what the data establish beyond any dispute is that a) the mesa signature exists, b) that it is the dominant source of genomic divergence between humans and the great apes, and, c) no account of speciation is complete without it."
- note: Slips ledger RH-7. (b) is stated without a fraction.

### Q170 The Fourth Mechanism (FM9), ¶8
- source: voxday.net, "The Fourth Mechanism"; URL: https://voxday.net/2026/10/10/the-fourth-mechanism/ ; published 2026-10-10 13:37:48 UTC (modified 15:46:51 UTC)
- locator: ¶8 of the entry content
- local copy: `sources/raw/refresh-2026-10-10/post/fm.html` (sha256 fc618dcc…65647; verified verbatim as a substring of the saved page text with curly apostrophes normalised, 2026-10-10)
- branch: FM1 (mesas / sigillation), ROOT
- tag (rule RH): dialectic (hedge; credit to Day)
- quote: "Sigillation is no more proof of IGM than relictation is. But it may be initial evidence of IGM."
- note: A concession and a hedge on the sigillation claim.

### Q171 The Fourth Mechanism (FM10), ¶8
- source: voxday.net, "The Fourth Mechanism"; URL: https://voxday.net/2026/10/10/the-fourth-mechanism/ ; published 2026-10-10 13:37:48 UTC (modified 15:46:51 UTC)
- locator: ¶8 of the entry content
- local copy: `sources/raw/refresh-2026-10-10/post/fm.html` (sha256 fc618dcc…65647; verified verbatim as a substring of the saved page text with curly apostrophes normalised, 2026-10-10)
- branch: FM1 (mesas / sigillation), ROOT
- tag (rule RH): dialectic (ROOT-level conclusion) plus an invitation to replicate (valid point for Day)
- quote: "What we do know is that neither natural selection nor neutral diffusive drift can still be considered viable candidates. And there is no need to take my word for anything with regards to this, all of the data has been provided by the T2T Primate Consortium (Yoo et al. 2025) aligned with Progressive Cactus (Armstrong et al. 2020)."
- note: Verified against the raw page 2026-10-10: the original reads "can still be considered viable candidates"; there is no bracketed "[not]". Read in context the sentence means "can no longer be considered"; the audit does not edit it.

## Refresh 2026-10-11 quotes (Q172-Q179; added 2026-10-11)

All from voxday.net, "How Biologists Keep "Proving" Selection", https://voxday.net/2026/10/11/how-biologists-keep-proving-selection/ ; published 2026-10-11 14:13:57 UTC, modified 16:35:43 UTC (re-check for edits); tags evolution, science; local copy `sources/raw/refresh-2026-10-11/post-how-biologists-keep-proving-selection/page.html` (extracted body.txt; page sha256 585308fa16c617b320bd27116a9dbb74b28ddb5cca11bf58784a409bb4e73e1b). Each quote machine-checked as a substring of body.txt (whitespace/curly quotes normalised).

### Q172 Ka/Ks (dN/dS) re-computation headline (added 2026-10-11)
- source: voxday.net, "How Biologists Keep 'Proving' Selection" (SG cross-post not seen)
- locator: ¶7 of the non-empty paragraphs of the saved body text
- branch: ROOT-FM / selection strength / LTEE / T2T
- quote: "We used GENCODE v46 annotations, the same Nei-Gojobori method the original studies used, and the complete extraction of human-chimp aligned positions from the T2T-quality assemblies. And we got a result."
- note: FM-adjacent / selection strength; NEW result claim, no code, gene list or per-gene table released. Tag: dialectic (a numeric claim). Day's own pre-release caveat is Q176.

### Q173 dN/dS = 0.80 versus the Consortium's 0.23 (added 2026-10-11)
- source: voxday.net, "How Biologists Keep 'Proving' Selection" (SG cross-post not seen)
- locator: ¶9 of the non-empty paragraphs of the saved body text
- branch: ROOT-FM / selection strength / LTEE / T2T
- quote: "Not 0.23. 0.80."
- note: Also quotes the Consortium value as 0.23; the audit has not checked that against the 2005 paper text (abstract/full text not in the repo for this value). Tag: dialectic.

### Q174 Gene-set size: 20,400 versus 13,454 (added 2026-10-11)
- source: voxday.net, "How Biologists Keep 'Proving' Selection" (SG cross-post not seen)
- locator: ¶13 of the non-empty paragraphs of the saved body text
- branch: ROOT-FM / selection strength / LTEE / T2T
- quote: "We computed dN/dS on 20,400 protein-coding genes, which is every gene annotated in GENCODE v46 that has coding sequence data in the human-chimp alignment."
- note: Day's own denominators: 20,400 (his) versus 13,454 (Consortium, next quote). A different gene set and different estimator inputs are exactly the confound a replication must separate.

### Q175 Filter stack does not move dN/dS below 0.64-0.65 (added 2026-10-11)
- source: voxday.net, "How Biologists Keep 'Proving' Selection" (SG cross-post not seen)
- locator: ¶17 of the non-empty paragraphs of the saved body text
- branch: ROOT-FM / selection strength / LTEE / T2T
- quote: "No combination of quality filters moves the number below 0.65."
- note: The same paragraph says the strictest stack 'still produced dN/dS = 0.64 on 10 remaining genes'. Ten genes is not a genome estimate; recorded as Day's own words. Tag: dialectic.

### Q176 Day's pending test: reconstruct the 13,454-gene list (added 2026-10-11)
- source: voxday.net, "How Biologists Keep 'Proving' Selection" (SG cross-post not seen)
- locator: ¶22 of the non-empty paragraphs of the saved body text
- branch: ROOT-FM / selection strength / LTEE / T2T
- quote: "If the Consortium's curated subset gives ~0.23 and our complete set gives ~0.80, then the case is closed: the published number is an artificial artifact of cherry-picked genes, not an observed property of the human genome."
- note: A self-proposed discriminating test (credit to Day): same pipeline, two gene sets. Input to test-methods-review-2026-10-11.md. Promised output: 'forthcoming paper on Zenodo' (not yet present, Zenodo count 39 unchanged 2026-10-11).

### Q177 Interpretation: selection not primary (added 2026-10-11)
- source: voxday.net, "How Biologists Keep 'Proving' Selection" (SG cross-post not seen)
- locator: ¶21 of the non-empty paragraphs of the saved body text
- branch: ROOT-FM / selection strength / LTEE / T2T
- quote: "At dN/dS = 0.80, natural selection is not the primary mechanism of adaptive evolution."
- note: Non-sequitur candidate (rule N) not scored here: dN/dS measures the average purifying/neutral balance of all nonsynonymous changes, not the adaptive fraction (alpha) or the rate of beneficial fixations. Proposed for a check, no verdict change. Tag: dialectic.

### Q178 LTEE: 'ten of the twelve populations' show undoing intervals (added 2026-10-11)
- source: voxday.net, "How Biologists Keep 'Proving' Selection" (SG cross-post not seen)
- locator: ¶4 of the non-empty paragraphs of the saved body text
- branch: ROOT-FM / selection strength / LTEE / T2T
- quote: "In fact, ten of the twelve populations even show intervals where fixations are being undone faster than any new ones complete."
- note: Bears on A2c (estimator, negative fixations), E9 (Good 2017 dynamics). Day gives no locator in Good et al. 2017; unverified against Good 2017 SI (not retrieved).

### Q179 T2T divergence claim: 410 million differences, not 35 million (added 2026-10-11)
- source: voxday.net, "How Biologists Keep 'Proving' Selection" (SG cross-post not seen)
- locator: ¶2 of the non-empty paragraphs of the saved body text
- branch: ROOT-FM / selection strength / LTEE / T2T
- quote: "the real number turned out to involve an estimated 410 million total genomic differences, not 35 million"
- note: Bears on A3x1 (Yoo 2025 fidelity), A3x (bp vs events). The 410M is a Day-side sum; Day's own post (¶ on supplementary sheets) says 'no total is either calculated or provided' by the paper, so 410M is Day's own aggregation across tools (his wording). Not checked here against Yoo SI.

## Refresh 2026-10-12 quotes (Q180-Q194; added 2026-10-12)

### Q180 The method is the conclusion: circularity claim (added 2026-10-12)
- source: voxday.net, "The Method is the Conclusion" (2026-10-12 14:12:35 UTC) (SG cross-post not seen)
- locator: ¶3 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12/post-the-method-is-the-conclusion/body.txt
- branch: ROOT-FM / selection strength / dN/dS; RH tag: dialectic
- quote: "discovered that the protein-guided CDS alignment method has a circular reasoning problem that's impossible to ignore once you recognize it:"
- note: Core new claim of the post: protein-aware alignment biases dN/dS downward. Mechanism stated without a test, code or example gene. Directly relevant to DN3/DN5. Checked 2026-10-12 against the held CSAC 2005 Methods: the 13,454 set came from the genome alignment (16,045 genes), Clustal W only for a 7,043-gene subset, K_A/K_S pooled (quotes-literature.md CSAC2005). Readings (RD): (a) this is how the 0.23 was produced: contradicted by that text; (b) protein-guided pipelines in general bias dN/dS down: pending L1c. Claim DN6.

### Q181 Gapping-out mechanism (added 2026-10-12)
- source: voxday.net, "The Method is the Conclusion" (2026-10-12 14:12:35 UTC) (SG cross-post not seen)
- locator: ¶7 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12/post-the-method-is-the-conclusion/body.txt
- branch: ROOT-FM / selection strength / dN/dS; RH tag: dialectic
- quote: "Regions too divergent to score well get gapped out or are left unaligned, so they aren't counted."
- note: Premise of the circularity argument. Human-chimp protein sequences are about 99% identical (not verified here), so how much can be gapped out is an empirical question Day does not quantify. Source text is a bullet list; the list items are separate non-empty paragraphs.

### Q182 Excluded codons enriched for nonsynonymous (added 2026-10-12)
- source: voxday.net, "The Method is the Conclusion" (2026-10-12 14:12:35 UTC) (SG cross-post not seen)
- locator: ¶10 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12/post-the-method-is-the-conclusion/body.txt
- branch: ROOT-FM / selection strength / dN/dS; RH tag: dialectic
- quote: "Those excluded codons are enriched for nonsynonymous substitutions by definition, because that's why they scored poorly in the protein alignment."
- note: Testable: Day reports no count of excluded codons. Note a poor score can also come from misalignment, in which case excluded positions carry no information about selection.

### Q183 Uniform nonsynonymous fraction across subsets (added 2026-10-12)
- source: voxday.net, "The Method is the Conclusion" (2026-10-12 14:12:35 UTC) (SG cross-post not seen)
- locator: ¶13 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12/post-the-method-is-the-conclusion/body.txt
- branch: ROOT-FM / selection strength / dN/dS; RH tag: dialectic
- quote: "It's 73.8% nonsynonymous across every subset we tested. The signal is uniform across the genome, it's not concentrated in problematic genes."
- note: Subsets A, B, B-HC are nested and C = A minus B (table, Q184), so uniformity is not independent evidence. Table values: 73.9, 73.8, 73.8, 74.4%.

### Q184 Gene-set table rows (added 2026-10-12)
- source: voxday.net, "The Method is the Conclusion" (2026-10-12 14:12:35 UTC) (SG cross-post not seen)
- locator: ¶17,18,19,20,21 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12/post-the-method-is-the-conclusion/body.txt
- branch: ROOT-FM / selection strength / dN/dS; RH tag: dialectic
- quote: "A: All GENCODE20,4000.798973.9%"
- quote: "B: 1:1 chimp orthologs16,9950.795673.8%"
- quote: "B-HC: High-confidence 1:115,9370.793973.8%"
- quote: "C: Excluded by filter3,4050.823774.4%"
- quote: "Published (Consortium 2005)13,4540.2300~40%"
- note: Table cells are run together by text extraction (extraction artefact; columns: gene set, genes measured, pooled dN/dS, nonsynonymous fraction). The Consortium 13,454-gene list is not a row that Day measured: the 0.2300 and ~40% are the published figures. Genes: 16,995 + 3,405 = 20,400.

### Q185 Smaller subset not cherry-picked (added 2026-10-12)
- source: voxday.net, "The Method is the Conclusion" (2026-10-12 14:12:35 UTC) (SG cross-post not seen)
- locator: ¶13 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12/post-the-method-is-the-conclusion/body.txt
- branch: ROOT-FM / selection strength / dN/dS; RH tag: dialectic
- quote: "We ran the same test on their smaller subset, which I suspected might be cherry-picked. Except they weren't."
- note: Reading-dependent: (R1) "their smaller subset" = the 1:1 chimp orthologs B (16,995) or B-HC (15,937), not the 13,454 list (no such row in the table); (R2) the 13,454 list itself was rebuilt and run (no number given). This reverses the 2026-10-11 version of the post, which said "the only way to get 0.23 is to start with a pre-selected gene set" (Q176 context).

### Q186 Not gene selection, filtering or error (added 2026-10-12)
- source: voxday.net, "The Method is the Conclusion" (2026-10-12 14:12:35 UTC) (SG cross-post not seen)
- locator: ¶15 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12/post-the-method-is-the-conclusion/body.txt
- branch: ROOT-FM / selection strength / dN/dS; RH tag: dialectic
- quote: "The difference is not a matter of gene selection, quality filtering, or computational error. It is a methodological artifact of using a conservation-dependent alignment to measure conservation."
- note: Explicit change of explanation from the 2026-10-11 text (gene curation) to alignment circularity. Day also says (10-11) the strictest filter stack left dN/dS = 0.64 on 10 genes (Q175).

### Q187 dN/dS 0.7989 implies only 20 percent eliminated (added 2026-10-12)
- source: voxday.net, "The Method is the Conclusion" (2026-10-12 14:12:35 UTC) (SG cross-post not seen)
- locator: ¶15 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12/post-the-method-is-the-conclusion/body.txt
- branch: ROOT-FM / selection strength / dN/dS; RH tag: dialectic
- quote: "the whole-genome measurement of dN/dS = 0.7989 implies that only 20 percent are actually eliminated, which is nearly four times less purifying selection than the mainstream science assumes."
- note: Arithmetic: 1 - 0.7989 = 20.1%; 1 - 0.23 = 77%; 77/20.1 = 3.8 ("nearly four times"). Holds given the reading "1 - dN/dS = fraction of nonsynonymous changes removed" (standard simplification; Day uses it himself in the 2026-10-11 text, cf. DN4).

### Q188 Canonical evidence "incorrect" (added 2026-10-12)
- source: voxday.net, "The Method is the Conclusion" (2026-10-12 14:12:35 UTC) (SG cross-post not seen)
- locator: ¶23 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12/post-the-method-is-the-conclusion/body.txt
- branch: ROOT-FM / selection strength / dN/dS; RH tag: dialectic
- quote: "First, they demonstrate that the canonical evidence for strong purifying selection in coding sequences is methodologically compromised and therefore incorrect."
- note: Strong wording on an unreleased analysis. Day lists no alternative-evidence lines for purifying selection (polymorphism pN/pS, conservation across deep clades) that do not rely on the 2005 value.

### Q189 Coding sequences evolving near-neutrally (added 2026-10-12)
- source: voxday.net, "The Method is the Conclusion" (2026-10-12 14:12:35 UTC) (SG cross-post not seen)
- locator: ¶23 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12/post-the-method-is-the-conclusion/body.txt
- branch: ROOT-FM / selection strength / dN/dS; RH tag: dialectic
- quote: "Second, they indicate that even coding sequences are evolving near-neutrally. Purifying selection exists, but is a much weaker mechanism than previously believed, removing roughly one in five nonsynonymous mutations rather than three in four."
- note: Concedes purifying selection exists (credit). Compare the neutral-theory material in B (Q155).

### Q190 Decoupling from MITTENS (added 2026-10-12)
- source: voxday.net, "The Method is the Conclusion" (2026-10-12 14:12:35 UTC) (SG cross-post not seen)
- locator: ¶24 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12/post-the-method-is-the-conclusion/body.txt
- branch: ROOT-FM / MITTENS scope; RH tag: dialectic
- quote: "And, just to be clear, none of this genomic analysis has anything to do with MITTENS per se. It merely happens to be empirical evidence that tends to independently confirm the mathematical and empirical impossibility of evolution by natural selection."
- note: Credit to Day: states the dN/dS result is not an input to MITTENS, so a failure of it would not by itself touch the MITTENS arithmetic. The second sentence claims independent confirmation of an "impossibility", which dN/dS = 0.80 does not give (an average purifying/neutral balance).

### Q191 Kevin Hart analogy (added 2026-10-12)
- source: voxday.net, "The Method is the Conclusion" (2026-10-12 14:12:35 UTC) (SG cross-post not seen)
- locator: ¶10 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12/post-the-method-is-the-conclusion/body.txt
- branch: ROOT-FM / rhetoric; RH tag: rhetoric
- quote: "In other words, the method presupposes the conclusion. This is, again, the same way one proves that Kevin Hart can dunk a basketball on a 10-foot basket, by showing that he is one inch taller than Lebron James."
- note: Device: analogy of absurd proof; audience: sympathetic readers; function: delegitimise the method without a test. Dialectical core: a conservation-dependent alignment can bias a conservation estimate (see the circularity claim). Better answer: grant the possible bias, then ask for the excluded-codon count and the 13,454-gene run.

### Q192 Opening: how would anyone tell the difference (added 2026-10-12)
- source: voxday.net, "The Method is the Conclusion" (2026-10-12 14:12:35 UTC) (SG cross-post not seen)
- locator: ¶2 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12/post-the-method-is-the-conclusion/body.txt
- branch: ROOT-FM / rhetoric; RH tag: rhetoric
- quote: "how would anyone, no matter how well-credentialed, ever be able to tell the difference given their absolute refusal to even look at the growing body of evidence that natural selection is a very weak force totally incapable of accounting for the chimp-human genetic divergence, much less the origin of the species?"
- note: Device: rhetorical question, attribution of refusal to unnamed critics; function: pre-empt dismissal. Dialectical core: the work should be judged on its method; both sides can be asked to release code and data. No critic named beyond "Erika" (not identified in the fetched text).

### Q193 Natural Philosophy: logic-plus-math step (added 2026-10-12, RELAY endorsed)
- source: voxday.net, "Natural Philosophy" (2026-10-12 05:01:10 UTC) (SG cross-post not seen)
- locator: ¶11 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12/post-natural-philosophy/body.txt
- branch: ROOT / philosophy of selection; RH tag: dialectic
- quote: "if "natural selection" by its secondary definition can be shown to be mathematically incapable of reaching it, then natural selection by both definitions is thereby shown to be incapable of explaining what it is meant to by a combination of logic and math."
- note: RELAY (rule U): the post opens "The connection between my assault on TENS and the development of Veriphysics has become apparent to others:" and quotes an unnamed third party at length; Day closes with his own paragraph. Not scored internal. The conditional is valid in form; its antecedent (MITTENS-type incapacity) is the contested part.

### Q194 Natural Philosophy: tautology of secondary definition (added 2026-10-12, RELAY endorsed)
- source: voxday.net, "Natural Philosophy" (2026-10-12 05:01:10 UTC) (SG cross-post not seen)
- locator: ¶9 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12/post-natural-philosophy/body.txt
- branch: ROOT / philosophy of selection; RH tag: dialectic
- quote: "Natural selection by its secondary definition can be logically critiqued for its tautological nature, and the conflation of the two can of course be logically critiqued for being a logical conflation."
- note: RELAY (rule U). Contrast: population-genetic usage estimates selection coefficients from data (cf. claim A4f). No numbers.

## Refresh 2026-10-12d Triveritas quotes (Q195-Q271; added 2026-10-12)

Purpose: establish from fetched text what Day's "Triveritas" is, how he defines, scores and applies it, for `docs/research/criticality/triveritas-method.md` and `triveritas-audit-2026-10-12.md`. Sources fetched 2026-10-12 about 21:20-22:15 UTC into `sources/raw/refresh-2026-10-12d/` (gitignored; each fetch in its own directory; read or grepped only). All Triveritas material is dated 2026-02-08 to 2026-10-12, inside the corpus freeze (O-7).

How these quotes were made: each quote was cut by a script from the saved local text between a start and an end anchor, never retyped, and then checked a second time as a substring of the whitespace-normalised file (PDF text: `pdftotext -layout`; page breaks never inside a quote). 77 of 77 passed. Locators: PDF page and line of the local `paper.txt`; paragraph number of the saved body text; Substack comment id. Ligatures and curly quotes are as in the source text layer.

Not scored: no claim node, verdict or ledger was changed by this pass. RH tags are this pass's reading under rule RH1 and are proposals. "Credit to Day" and critic-side points are both recorded in the notes.

### Primary: Day (and Day & Athos) on the Triveritas (Q195-Q254)

### Q195 Treatise 023: the criterion (added 2026-10-12d)
- source: `B2026-02-25-veriphysics-the-treatise-023`; voxday.net, "Veriphysics: The Treatise 023" (2026-02-25 10:16:27 UTC)
- URL: https://voxday.net/2026/02/25/veriphysics-the-treatise-023/
- locator: ¶3 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/post-2026-02-25-veriphysics-the-treatise-023/body.txt
- branch: Triveritas / definition; RH tag: dialectic
- quote: "Veriscendancy offers a genuine criterion: the Triad of Truth, the Triveritas. A claim merits assent and may be accepted as probably true when and only when it satisfies three conditions: logical validity, mathematical coherence, and empirical anchoring. Each condition is necessary; none is sufficient; the conjunction of all three elements is required."
- note: First full statement found on the blog (the Treatise ebook was announced 2026-02-18; the book text itself was not read). "Veriscendancy" is Day's word in the fetched text. "when and only when" makes it a biconditional for assent; the Zenodo proofs later say necessary, not sufficient, for truth (Q210).

### Q196 Treatise 023: logical validity (added 2026-10-12d)
- source: `B2026-02-25-veriphysics-the-treatise-023`; voxday.net, "Veriphysics: The Treatise 023" (2026-02-25 10:16:27 UTC)
- URL: https://voxday.net/2026/02/25/veriphysics-the-treatise-023/
- locator: ¶4 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/post-2026-02-25-veriphysics-the-treatise-023/body.txt
- branch: Triveritas / L definition; RH tag: dialectic
- quote: "Logical validity means that the argument for the claim must be formally sound. The conclusions must follow from the premises; the inferences must be valid; the reasoning must be free from fallacy."
- note: Version 1 of L: formal soundness (valid inference, no fallacy). The Mathematical Proof adds "explanatorily coherent ... logical unity" (Q204). The two definitions are not the same test: see `criticality/triveritas-method.md` section 3.

### Q197 Treatise 023: mathematical coherence (added 2026-10-12d)
- source: `B2026-02-25-veriphysics-the-treatise-023`; voxday.net, "Veriphysics: The Treatise 023" (2026-02-25 10:16:27 UTC)
- URL: https://voxday.net/2026/02/25/veriphysics-the-treatise-023/
- locator: ¶6 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/post-2026-02-25-veriphysics-the-treatise-023/body.txt
- branch: Triveritas / M definition; RH tag: dialectic
- quote: "Mathematical coherence means that the claim must survive quantitative analysis where quantification is possible. If a theory makes numerical predictions or depends on rates, probabilities, or magnitudes, those numbers must work."
- note: Version 1 of M: the claim's numbers survive quantitative analysis "where quantification is possible". The Mathematical Proof version is internal consistency of the quantitative structure (Q205); the M scale adds "predictions are derived from its own principles" (Q234).

### Q198 Treatise 023: anyone competent may check (added 2026-10-12d)
- source: `B2026-02-25-veriphysics-the-treatise-023`; voxday.net, "Veriphysics: The Treatise 023" (2026-02-25 10:16:27 UTC)
- URL: https://voxday.net/2026/02/25/veriphysics-the-treatise-023/
- locator: ¶8 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/post-2026-02-25-veriphysics-the-treatise-023/body.txt
- branch: Triveritas / M, who may apply it; RH tag: dialectic
- quote: "Every claim that involves quantities must provide the correct calculations. The calculations must be examined, not by credentialed authorities with careers at stake, but by anyone competent in mathematics."
- note: Licence, in Day's words, for a non-credentialed party to check the calculations. Bears on whether an outside audit may apply the criterion to his own numbers.

### Q199 Treatise 023: empirical anchoring (added 2026-10-12d)
- source: `B2026-02-25-veriphysics-the-treatise-023`; voxday.net, "Veriphysics: The Treatise 023" (2026-02-25 10:16:27 UTC)
- URL: https://voxday.net/2026/02/25/veriphysics-the-treatise-023/
- locator: ¶9 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/post-2026-02-25-veriphysics-the-treatise-023/body.txt
- branch: Triveritas / E definition; RH tag: dialectic
- quote: "Empirical anchoring means that the claim must be tethered to observed reality. Theory without evidence is speculation; it may be elegant, coherent, mathematically sophisticated, and still describe nothing actual. The claim must make contact with the world, must be confirmed or at least not refuted by what we observe, must have some purchase on the phenomena it purports to explain."
- note: Version 1 of E: "confirmed or at least not refuted by what we observe". The Mathematical Proof version requires a tested prediction on data not used to build the claim (Q206).

### Q200 Treatise 024: evolution fails all three (added 2026-10-12d)
- source: `B2026-02-27-veriphysics-the-treatise-024`; voxday.net, "Veriphysics: The Treatise 024" (2026-02-27 10:16:03 UTC)
- URL: https://voxday.net/2026/02/27/veriphysics-the-treatise-024/
- locator: ¶8 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/post-2026-02-27-veriphysics-the-treatise-024/body.txt
- branch: Triveritas / worked example, evolution; RH tag: dialectic
- quote: "Neo-Darwinism fails all three elements of the Triveritas. The logic is unsound: the mechanism cannot do what is claimed. The math is wrong: the numbers do not permit it. The evidence, properly interpreted, confirms the failure rather than the success."
- note: Worked example 1 (2026-02-27 serial; book announced 2026-02-18): L fail, M fail, E fail. Compare Q207 and Q216 (L satisfied, E satisfied, M failed; 2026-02-21), Q222 (L ~ 60, M ~ 5, E ~ 70; 2026-03-09) and Q233 (L ~ 40; 2026-03-16). Four applications by the same author give three different L outcomes.

### Q201 Treatise 025: warranted assent, not certainty (added 2026-10-12d)
- source: `B2026-03-01-veriphysics-the-treatise-025`; voxday.net, "Veriphysics: The Treatise 025" (2026-03-01 13:38:48 UTC)
- URL: https://voxday.net/2026/03/01/veriphysics-the-treatise-025/
- locator: ¶6 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/post-2026-03-01-veriphysics-the-treatise-025/body.txt
- branch: Triveritas / scope of the conclusion; RH tag: dialectic
- quote: "The Triveritas operates within these epistemic limits. It does not promise certainty; it offers warranted assent."
- note: Credit to Day: the criterion is stated as fallible.

### Q202 Treatise 025: 'know with certainty that Neo-Darwinism is false' (added 2026-10-12d)
- source: `B2026-03-01-veriphysics-the-treatise-025`; voxday.net, "Veriphysics: The Treatise 025" (2026-03-01 13:38:48 UTC)
- URL: https://voxday.net/2026/03/01/veriphysics-the-treatise-025/
- locator: ¶6 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/post-2026-03-01-veriphysics-the-treatise-025/body.txt
- branch: Triveritas / scope of the conclusion; RH tag: reading-dependent
- quote: "We can know with certainty that Neo-Darwinism is false, being refuted by logic, math, and empirical evidence, without pretending to know, fully or even in meaningful part, what the true historical account of Man’s biological origins were."
- note: Two sentences after Q201 ("does not promise certainty"). Reading 1 (literal): contradicts Q201 and Q210. Reading 2 (charitable): "certainty" is emphasis for "fails the criterion", i.e. rhetoric. Not scored here.

### Q203 Mathematical Proof: abstract (added 2026-10-12d)
- source: `Z18724454`; Zenodo 18724454, Day & Athos, "A Mathematical Proof of the Triveritas" (2026-02-21, v1)
- URL: https://zenodo.org/records/18724454
- locator: p.1 of the PDF, l.13 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18724454/paper.txt
- branch: Triveritas / definition; RH tag: dialectic
- quote: "The Triveritas holds that a claim merits warranted assent if and only if it satisfies three jointly necessary conditions: logical validity (L), mathematical coherence (M), and empirical anchoring (E)."
- note: The key one-sentence definition. PDF md5 matches the Zenodo checksum 52ab4b46...

### Q204 Mathematical Proof 1.1: Logical Validity (L) (added 2026-10-12d)
- source: `Z18724454`; Zenodo 18724454, Day & Athos, "A Mathematical Proof of the Triveritas" (2026-02-21, v1)
- URL: https://zenodo.org/records/18724454
- locator: p.2 of the PDF, l.61 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18724454/paper.txt
- branch: Triveritas / L definition; RH tag: dialectic
- quote: "Logical Validity (L). A claim satisfies logical validity if its conclusion follows deductively from its premises and its inferential structure is explanatorily coherent: the premises bear a principled, non-ad-hoc relationship to the conclusion, and the system as a whole possesses logical unity rather than consisting of disconnected accommodations of individual data points."
- note: Version 2 of L: deductive validity AND explanatory coherence / unity. Two conjoined tests under one letter; a claim can pass one and fail the other (a valid argument with ad hoc premises).

### Q205 Mathematical Proof 1.1: Mathematical Coherence (M) (added 2026-10-12d)
- source: `Z18724454`; Zenodo 18724454, Day & Athos, "A Mathematical Proof of the Triveritas" (2026-02-21, v1)
- URL: https://zenodo.org/records/18724454
- locator: p.2 of the PDF, l.68 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18724454/paper.txt
- branch: Triveritas / M definition; RH tag: dialectic
- quote: "Mathematical Coherence (M). A claim satisfies mathematical coherence if its quantitative structure is internally consistent: the operations it performs are well-defined, its parameters are finite and computable in principle, and its mathematical predictions do not contradict its own axioms. A claim that requires division by zero, produces divergent series where convergence is needed, or demands quantities that exceed physical constraints imposed by its own model fails M."
- note: Version 2 of M: internal consistency of the quantitative structure. Note "physical constraints imposed by its own model": M is scored on the claim's own basis.

### Q206 Mathematical Proof 1.1: Empirical Anchoring (E) (added 2026-10-12d)
- source: `Z18724454`; Zenodo 18724454, Day & Athos, "A Mathematical Proof of the Triveritas" (2026-02-21, v1)
- URL: https://zenodo.org/records/18724454
- locator: p.2 of the PDF, l.74 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18724454/paper.txt
- branch: Triveritas / E definition; RH tag: dialectic
- quote: "Empirical Anchoring (E). A claim satisfies empirical anchoring if it makes at least one prediction that has been tested against observation and not refuted. Anchoring requires contact with independently verifiable data, not merely consistency with data already used to construct the claim."
- note: Version 2 of E: at least one tested, unrefuted prediction on independently verifiable data; accommodation of the construction data does not count.

### Q207 Mathematical Proof 2.2 Remark: Modern Synthesis (added 2026-10-12d)
- source: `Z18724454`; Zenodo 18724454, Day & Athos, "A Mathematical Proof of the Triveritas" (2026-02-21, v1)
- URL: https://zenodo.org/records/18724454
- locator: p.4 of the PDF, l.154 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18724454/paper.txt
- branch: Triveritas / worked example, evolution; RH tag: dialectic
- quote: "Remark. The Modern Synthesis of neo-Darwinism provides a convergent example: logically valid, empirically anchored, but mathematically impossible given known fixation times and effective population sizes."
- note: Worked example 2: L pass, E pass, M fail. "companion papers (Vox Day and Claude Athos, 2025)" is the paper's own citation for the M failure, i.e. the claim under audit in this repository.

### Q208 Mathematical Proof 4.1: elementary case assumes independence (added 2026-10-12d)
- source: `Z18724454`; Zenodo 18724454, Day & Athos, "A Mathematical Proof of the Triveritas" (2026-02-21, v1)
- URL: https://zenodo.org/records/18724454
- locator: p.6 of the PDF, l.245 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18724454/paper.txt
- branch: Triveritas / proof structure; RH tag: dialectic
- quote: "This elementary case assumes the three filters are probabilistically independent. The remainder of Section 4 drops this assumption and establishes the same result under the weaker condition of conditional truth-tracking (Axiom 5)."
- note: Credit to Day: the independence assumption is stated. The general case rests on Axiom 5, which the paper says is warranted by the historical examples.

### Q209 Mathematical Proof 5.3: no decision procedure (added 2026-10-12d)
- source: `Z18724454`; Zenodo 18724454, Day & Athos, "A Mathematical Proof of the Triveritas" (2026-02-21, v1)
- URL: https://zenodo.org/records/18724454
- locator: p.7 of the PDF, l.295 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18724454/paper.txt
- branch: Triveritas / limits; RH tag: dialectic
- quote: "The Triveritas is a criterion of warranted assent, not a decision procedure for generating or evaluating claims in finite time. The proof establishes the goal; it does not automate the path to it."
- note: Credit to Day: he states that the proofs give no procedure for deciding whether a given claim satisfies L, M or E. The 0-100 scales (Q229-Q240) came three weeks later.

### Q210 Mathematical Proof 5.4: not sufficient for truth (added 2026-10-12d)
- source: `Z18724454`; Zenodo 18724454, Day & Athos, "A Mathematical Proof of the Triveritas" (2026-02-21, v1)
- URL: https://zenodo.org/records/18724454
- locator: p.7 of the PDF, l.282 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18724454/paper.txt
- branch: Triveritas / limits; RH tag: dialectic
- quote: "The proof demonstrates that the Triveritas is the strongest epistemic filter constructible from L, M, and E. It does not demonstrate that the Triveritas is sufficient for truth."
- note: Credit to Day: necessity, not sufficiency.

### Q211 Mathematical Proof 6.1: anti-self-sealing corollary (added 2026-10-12d)
- source: `Z18724454`; Zenodo 18724454, Day & Athos, "A Mathematical Proof of the Triveritas" (2026-02-21, v1)
- URL: https://zenodo.org/records/18724454
- locator: p.8 of the PDF, l.341 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18724454/paper.txt
- branch: Triveritas / corollary; RH tag: dialectic
- quote: "Corollary. Any system of claims that cannot, even in principle, be constrained by something external to its own stipulations is epistemically inert. It cannot warrant assent regardless of its internal properties."
- note: The corollary used in section 3 of the audit file against same-model review (TV-01).

### Q212 Mathematical Proof 6.1: observations the claimant does not control (added 2026-10-12d)
- source: `Z18724454`; Zenodo 18724454, Day & Athos, "A Mathematical Proof of the Triveritas" (2026-02-21, v1)
- URL: https://zenodo.org/records/18724454
- locator: p.8 of the PDF, l.344 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18724454/paper.txt
- branch: Triveritas / E definition; RH tag: dialectic
- quote: "E demands that a claim make contact with observations the claimant does not control. A system that generates its own confirmation, that defines truth by its own internal criteria, that accommodates every possible observation by post-hoc adjustment, can never satisfy E."
- note: Operational core of E for any self-assessment: confirmation produced by the claimant does not count.

### Q213 Logical Proof P3: scoped to claims about reality (added 2026-10-12d)
- source: `Z18724487`; Zenodo 18724487, Day & Athos, "A Logical Proof of the Triveritas" (2026-02-21, v1)
- URL: https://zenodo.org/records/18724487
- locator: p.2 of the PDF, l.79 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18724487/paper.txt
- branch: Triveritas / scope; RH tag: dialectic
- quote: "The Triveritas is scoped to claims about reality; within that scope, the premise that logical validity, mathematical coherence, and empirical anchoring each have some ability to distinguish true claims from false ones is not controversial but definitional."
- note: Scope statement 1. See Q246 for the narrower "claims about the physical world that involve quantities".

### Q214 Empirical Proof 1.1: Prediction 1 (added 2026-10-12d)
- source: `Z18724496`; Zenodo 18724496, Day & Athos, "An Empirical Proof of the Triveritas" (2026-02-21, v1)
- URL: https://zenodo.org/records/18724496
- locator: p.1 of the PDF, l.33 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18724496/paper.txt
- branch: Triveritas / its own testable prediction; RH tag: dialectic
- quote: "Prediction 1 (Negative). If a claim fails any one of logical validity (L), mathematical coherence (M), or empirical anchoring (E), the claim is false or unwarranted, and this will become apparent when the missing dimension is applied."
- note: "false or unwarranted" is a disjunction: a claim later vindicated can still count as a confirmation ("unwarranted" at the time), so Prediction 1 is hard to disconfirm as worded.

### Q215 Empirical Proof 1.2: case selection (added 2026-10-12d)
- source: `Z18724496`; Zenodo 18724496, Day & Athos, "An Empirical Proof of the Triveritas" (2026-02-21, v1)
- URL: https://zenodo.org/records/18724496
- locator: p.2 of the PDF, l.55 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18724496/paper.txt
- branch: Triveritas / evidence selection; RH tag: dialectic
- quote: "No case was selected because it supports the prediction; the cases were selected because they are among the most thoroughly documented episodes in the history of science and their outcomes are not in dispute."
- note: Case 5 (the Modern Synthesis) has a disputed outcome by the paper's own account ("remains the consensus framework", Q217), so it does not meet this stated selection rule.

### Q216 Empirical Proof Case 5: L satisfied (added 2026-10-12d)
- source: `Z18724496`; Zenodo 18724496, Day & Athos, "An Empirical Proof of the Triveritas" (2026-02-21, v1)
- URL: https://zenodo.org/records/18724496
- locator: p.4 of the PDF, l.141 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18724496/paper.txt
- branch: Triveritas / worked example, evolution; RH tag: dialectic
- quote: "L satisfied: The inference from heritable variation, differential reproduction, and natural selection to cumulative adaptive change is deductively valid. The explanatory structure is unified and non-ad-hoc."
- note: Compare Q200 (logic "unsound") and Q233 (L ~ 40).

### Q217 Empirical Proof Case 5: M failed, outcome (added 2026-10-12d)
- source: `Z18724496`; Zenodo 18724496, Day & Athos, "An Empirical Proof of the Triveritas" (2026-02-21, v1)
- URL: https://zenodo.org/records/18724496
- locator: p.4 of the PDF, l.149 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18724496/paper.txt
- branch: Triveritas / worked example, evolution; RH tag: dialectic
- quote: "Outcome: The mathematical impossibility has been confirmed by the companion papers (Vox Day and Claude Athos, 2025), which demonstrate that the required fixation rates exceed what the available time permits by approximately five orders of magnitude. The Modern Synthesis remains the consensus framework, but the Triveritas correctly identifies it as unwarranted because M is not satisfied. As predicted, L and E have been used to shield the theory from mathematical scrutiny. The refutation arrived on the M dimension."
- note: The outcome that confirms Prediction 1 in case 5 is the authors' own companion work. Under Q206/Q212 (data not used to construct the claim; observations the claimant does not control) this case is not independent evidence for the Triveritas. "five orders of magnitude" is the MITTENS shortfall audited in branch A.

### Q218 Empirical Proof 6.2: classification needs judgement (added 2026-10-12d)
- source: `Z18724496`; Zenodo 18724496, Day & Athos, "An Empirical Proof of the Triveritas" (2026-02-21, v1)
- URL: https://zenodo.org/records/18724496
- locator: p.11 of the PDF, l.455 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18724496/paper.txt
- branch: Triveritas / limits; RH tag: dialectic
- quote: "6.2 Classification judgment. Assigning a claim to a specific failure mode requires judgment about whether L, M, or E is satisfied. Reasonable people might disagree about some classifications."
- note: Credit to Day: rater judgement is conceded.

### Q219 Empirical Proof 5.3: 'Show me the third' (added 2026-10-12d)
- source: `Z18724496`; Zenodo 18724496, Day & Athos, "An Empirical Proof of the Triveritas" (2026-02-21, v1)
- URL: https://zenodo.org/records/18724496
- locator: p.10 of the PDF, l.434 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18724496/paper.txt
- branch: Triveritas / how applied; RH tag: rhetoric
- quote: "The Triveritas says: I do not care how strong you are on two dimensions. Show me the third."
- note: Device: personification, imperative. Dialectical core: the criterion is conjunctive and non-compensatory (no averaging). Compare the arithmetic-mean composites of Q221-Q223.

### Q220 Demarcation 3.3: the criterion for science (added 2026-10-12d)
- source: `Z18924026`; Zenodo 18924026, Day & Athos, "Solving the Scientific Demarcation Problem" (2026-03-09, modified 2026-03-15)
- URL: https://zenodo.org/records/18924026
- locator: p.5 of the PDF, l.207 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18924026/paper.txt
- branch: Triveritas / demarcation version; RH tag: dialectic
- quote: "A claim is scientific if and only if its confirmation chain can, in principle, reach a structurally warranted base case on all three dimensions of the Triveritas. Equivalently: a claim is scientific if it satisfies, or could satisfy upon testing, all three of L, M, and E simultaneously."
- note: Version 3: "satisfies, or could satisfy upon testing".

### Q221 Demarcation 3.4: Intelligent Design scored (added 2026-10-12d)
- source: `Z18924026`; Zenodo 18924026, Day & Athos, "Solving the Scientific Demarcation Problem" (2026-03-09, modified 2026-03-15)
- URL: https://zenodo.org/records/18924026
- locator: p.6 of the PDF, l.253 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18924026/paper.txt
- branch: Triveritas / worked example, ID; RH tag: dialectic
- quote: "Intelligent design (ID) holds that certain biological structures are best explained by an intelligent cause rather than natural selection. Score: L ~ 35 (the design inference is logically valid as an inference pattern, but the theory provides no mechanism and therefore no explanatory structure connecting the designer to specific biological features). M ~ 5 (no mathematical model generates testable quantitative predictions from ID premises). E ~ 10 (no confirmed novel predictions; the claimed evidence, irreducible complexity, is a negative argument against Darwinism, not a positive prediction of ID). Composite ~ 17. Verdict: not science."
- note: Valid point for Day's even-handedness in applying his own tool: ID scores lower (17) than evolutionary biology (45) on his own scale. Composite = arithmetic mean: (35+5+10)/3 = 16.7.

### Q222 Demarcation 6.2: Darwinian evolution composite (added 2026-10-12d)
- source: `Z18924026`; Zenodo 18924026, Day & Athos, "Solving the Scientific Demarcation Problem" (2026-03-09, modified 2026-03-15)
- URL: https://zenodo.org/records/18924026
- locator: p.15 of the PDF, l.658 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18924026/paper.txt
- branch: Triveritas / worked example, evolution; RH tag: dialectic
- quote: "Composite: ~ 45. The modern synthesis fails the Triveritas. This is consistent with the prior result established in Probability Zero (Day and Athos, 2025). The Triveritas does not require new analysis to reach this conclusion; it applies the existing analysis to the scoring framework and the failure on M is dispositive."
- note: Worked example 3: L ~ 60, M ~ 5, E ~ 70 (same section). (60+5+70)/3 = 45. "does not require new analysis": the M score is imported from *Probability Zero*, so this score is only as good as branch A/B/H of the audit.

### Q223 Demarcation 3.4: string theory, effective composite 0 (added 2026-10-12d)
- source: `Z18924026`; Zenodo 18924026, Day & Athos, "Solving the Scientific Demarcation Problem" (2026-03-09, modified 2026-03-15)
- URL: https://zenodo.org/records/18924026
- locator: p.7 of the PDF, l.277 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18924026/paper.txt
- branch: Triveritas / aggregation rule; RH tag: dialectic
- quote: "Composite ~ 57 on the basis of two strong dimensions, but the Triveritas requires all three. Effective composite for warranted assent: 0 (failure on any dimension disqualifies the claim from warranted assent)."
- note: Two aggregation rules in one sentence: arithmetic mean (57) and a veto (0). The veto is the rule consistent with the definition (Q203).

### Q224 Demarcation 6.1: self-referential test by two AI reviewers (added 2026-10-12d)
- source: `Z18924026`; Zenodo 18924026, Day & Athos, "Solving the Scientific Demarcation Problem" (2026-03-09, modified 2026-03-15)
- URL: https://zenodo.org/records/18924026
- locator: p.12 of the PDF, l.520 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18924026/paper.txt
- branch: Triveritas / self-application precedent; RH tag: dialectic
- quote: "To avoid the circularity of self-scoring, two independent AI reviewers (Grok and Gemini) were asked to evaluate this paper on each dimension of the Triveritas separately. The authors did not score their own work."
- note: Precedent, in Day's own paper, for applying the Triveritas to a piece of analytical work (a paper), with AI raters, to avoid self-scoring. Scores reported: Grok 95/92/90, Gemini 92/90/93.

### Q225 Demarcation 6.1: convergence of AI raters (added 2026-10-12d)
- source: `Z18924026`; Zenodo 18924026, Day & Athos, "Solving the Scientific Demarcation Problem" (2026-03-09, modified 2026-03-15)
- URL: https://zenodo.org/records/18924026
- locator: p.13 of the PDF, l.568 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18924026/paper.txt
- branch: Triveritas / inter-rater claim; RH tag: dialectic
- quote: "The convergence is itself significant: two AI systems with different architectures and different training, scoring independently, landed within 3 points of each other on every dimension. If the scores were "subjective" in the pejorative sense, independent raters would not converge this tightly."
- note: n = 2 raters, one item, both shown the paper's own framing. Agreement between two language models is not evidence of independence (shared training data); the same objection the method audit makes against this repository's reviews (MA-01).

### Q226 Demarcation 6.3: plus or minus 20% and the 60-point threshold (added 2026-10-12d)
- source: `Z18924026`; Zenodo 18924026, Day & Athos, "Solving the Scientific Demarcation Problem" (2026-03-09, modified 2026-03-15)
- URL: https://zenodo.org/records/18924026
- locator: p.16 of the PDF, l.684 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18924026/paper.txt
- branch: Triveritas / threshold; RH tag: dialectic
- quote: "No permutation of scores within the band changes the ordering or moves any theory across the 60-point threshold that separates passing from failing theories."
- note: The only place a numeric pass mark is stated (60). Whether it applies per dimension (pseudocode, Q228) or to the composite (this sentence, read with "Composite ~ 45 ... fails") is not said. The M and E scale posts name 50 as "the threshold" (Q235, Q238).

### Q227 Demarcation 6.4: binary determinations are the foundation (added 2026-10-12d)
- source: `Z18924026`; Zenodo 18924026, Day & Athos, "Solving the Scientific Demarcation Problem" (2026-03-09, modified 2026-03-15)
- URL: https://zenodo.org/records/18924026
- locator: p.17 of the PDF, l.729 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18924026/paper.txt
- branch: Triveritas / scoring; RH tag: dialectic
- quote: "The numerical scores are a refinement. The binary determinations are the foundation. The critic who objects to the refinement has not touched the foundation."
- note: Day's own priority rule: pass/fail per dimension first, numbers second. Used in the audit file as the primary reading.

### Q228 Demarcation 6.5: pseudocode (added 2026-10-12d)
- source: `Z18924026`; Zenodo 18924026, Day & Athos, "Solving the Scientific Demarcation Problem" (2026-03-09, modified 2026-03-15)
- URL: https://zenodo.org/records/18924026
- locator: p.17 of the PDF, l.771 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18924026/paper.txt
- branch: Triveritas / decision rule; RH tag: dialectic
- quote: "warranted = (L > threshold) and (M > threshold) and (E > threshold) return L, M, E, warranted"
- note: Per-dimension threshold, conjunctive. `threshold` is not assigned a value in the pseudocode.

### Q229 History of Science: 0-100 scale (added 2026-10-12d)
- source: `Z19022126`; Zenodo 19022126, Day & Athos, "Triveritas and the History of Science" (2026-03-14, v1)
- URL: https://zenodo.org/records/19022126
- locator: p.2 of the PDF, l.74 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-19022126/paper.txt
- branch: Triveritas / scoring; RH tag: dialectic
- quote: "The scoring methodology assigns values on a 0-100 scale for each dimension, based on informed assessment of the theory's logical structure, mathematical architecture, and empirical track record."
- note: "informed assessment": no rubric in the papers; the anchor scales followed on the Substack (Q231-Q240).

### Q230 History of Science: data analysis belongs to E, not M (added 2026-10-12d)
- source: `Z19022126`; Zenodo 19022126, Day & Athos, "Triveritas and the History of Science" (2026-03-14, v1)
- URL: https://zenodo.org/records/19022126
- locator: p.3 of the PDF, l.110 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-19022126/paper.txt
- branch: Triveritas / M definition; RH tag: dialectic
- quote: "statistical comparisons of mortality rates are empirical data analysis and belong to E, not M. The M dimension asks whether the theory possesses a mathematical architecture that generates quantitative predictions from its own structure."
- note: Version 3 of M: a mathematical architecture that generates predictions. Under this version, statistics computed on data are E. Decides how an audit's re-computations are classed (audit file, section 2).

### Q231 The L Scale: definition and key question (added 2026-10-12d)
- source: `VPS-2026-03-16-the-l-scale`; veriphysics.substack.com, "The L Scale" (2026-03-16, updated 2026-03-19)
- URL: https://veriphysics.substack.com/p/the-l-scale
- locator: ¶4 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/vps-the-l-scale/body.txt
- branch: Triveritas / L scale; RH tag: dialectic
- quote: "Definition: Explanatory coherence, non-ad-hoc premises, principled relationship between premises and conclusions, logical unity. Key question: does the theory have a single unifying principle from which its predictions follow, or is it a collection of independent accommodations?"
- note: Version 3 of L: deductive validity is no longer named; the key question is explanatory unity. Post updated 2026-03-19 (anchors added or replaced, see "Adjusting the L Scale").

### Q232 The L Scale: quantification is 'subjectivity' (added 2026-10-12d)
- source: `VPS-2026-03-16-the-l-scale`; veriphysics.substack.com, "The L Scale" (2026-03-16, updated 2026-03-19)
- URL: https://veriphysics.substack.com/p/the-l-scale
- locator: ¶1 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/vps-the-l-scale/body.txt
- branch: Triveritas / scoring; RH tag: dialectic
- quote: "One of the understandable, though illogical, critiques of the Triveritas is its system of quantification, although this is a) not a first-order weakness of the overall structure and b) an excellent source of comparative analysis despite its subjectivity. The point which every critic of quantification fail to grasp is that every system of scientific quantification relies upon significant amounts of subjectivity, in most cases, considerably more than the Triveritas, and more importantly, that truth is not synonymous with objectivity."
- note: Day concedes subjectivity of the numbers and calls the scale "merely a first draft".

### Q233 The L Scale: Modern Synthesis at L ~ 40 (added 2026-10-12d)
- source: `VPS-2026-03-16-the-l-scale`; veriphysics.substack.com, "The L Scale" (2026-03-16, updated 2026-03-19)
- URL: https://veriphysics.substack.com/p/the-l-scale
- locator: ¶11 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/vps-the-l-scale/body.txt
- branch: Triveritas / worked example, evolution; RH tag: dialectic
- quote: "L ~ 40: Coherent principle whose central claim exceeds its logical warrant. The Modern Synthesis of Darwinian evolution and Mendelian genetics. The principle of descent with modification via natural selection is logically coherent for within-species adaptation, but the theory is called the Origin of Species, and the grand extrapolation from adaptation to speciation is asserted without a formal logical derivation from the micro-level principle, leaving a gap in inferential unity between the core mechanism and the broader claim."
- note: Worked example 4. One week earlier the same theory was L ~ 60 with a stated sensitivity band of 48 to 72 (Zenodo 18924026 section 6.3); 40 is outside that band and below the 60 pass mark of Q226.

### Q234 The M Scale: definition and key question (added 2026-10-12d)
- source: `VPS-2026-03-18-the-m-scale`; veriphysics.substack.com, "The M Scale" (2026-03-18)
- URL: https://veriphysics.substack.com/p/the-m-scale
- locator: ¶2 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/vps-the-m-scale/body.txt
- branch: Triveritas / M scale; RH tag: dialectic
- quote: "Definition: Internal consistency of quantitative structure. Operations well-defined, parameters finite and computable in principle, mathematical predictions do not contradict the theory’s own axioms. Key question: does the theory have a well-defined mathematical structure whose predictions are derived from its own principles, or is the quantitative apparatus absent, ad hoc, or internally contradictory?"

### Q235 The M Scale: threshold at 50 (added 2026-10-12d)
- source: `VPS-2026-03-18-the-m-scale`; veriphysics.substack.com, "The M Scale" (2026-03-18)
- URL: https://veriphysics.substack.com/p/the-m-scale
- locator: ¶13 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/vps-the-m-scale/body.txt
- branch: Triveritas / threshold; RH tag: dialectic
- quote: "This is the key threshold: above 50, the mathematics constrains the theory’s predictions enough that it can be wrong in specific, informative ways."
- note: A second pass mark (50), different from the 60 of Q226.

### Q236 The M Scale: ID at M ~ 5, 'Mathematics is not performed' (added 2026-10-12d)
- source: `VPS-2026-03-18-the-m-scale`; veriphysics.substack.com, "The M Scale" (2026-03-18)
- URL: https://veriphysics.substack.com/p/the-m-scale
- locator: ¶4 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/vps-the-m-scale/body.txt
- branch: Triveritas / M scale anchor; RH tag: dialectic
- quote: "The quantitative vocabulary is decorative. Numbers are mentioned. Mathematics is not performed."
- note: Anchor used when classing arguments that quote numbers without a derivation.

### Q237 The E Scale: definition and key question (added 2026-10-12d)
- source: `VPS-2026-03-20-the-e-scale`; veriphysics.substack.com, "The E Scale" (2026-03-20)
- URL: https://veriphysics.substack.com/p/the-e-scale
- locator: ¶2 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/vps-the-e-scale/body.txt
- branch: Triveritas / E scale; RH tag: dialectic
- quote: "Definition: Contact with independently verifiable data. A claim satisfies empirical anchoring if it makes at least one prediction that has been tested against observation and not refuted. Anchoring requires contact with independently verifiable data, not merely consistency with data already used to construct the claim. Key question: how many predictions has the theory made, how many have been tested, how many confirmed, at what precision, and over what time span?"

### Q238 The E Scale: threshold at 50 (added 2026-10-12d)
- source: `VPS-2026-03-20-the-e-scale`; veriphysics.substack.com, "The E Scale" (2026-03-20)
- URL: https://veriphysics.substack.com/p/the-e-scale
- locator: ¶13 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/vps-the-e-scale/body.txt
- branch: Triveritas / threshold; RH tag: dialectic
- quote: "This is the threshold: above 50, the confirmed predictions outweigh the failures. Below 50, the failures dominate."

### Q239 The E Scale: convergence of independent methods (added 2026-10-12d)
- source: `VPS-2026-03-20-the-e-scale`; veriphysics.substack.com, "The E Scale" (2026-03-20)
- URL: https://veriphysics.substack.com/p/the-e-scale
- locator: ¶16 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/vps-the-e-scale/body.txt
- branch: Triveritas / E scale anchor (E ~ 65); RH tag: dialectic
- quote: "The convergence of independent methods is the strongest form of empirical anchoring short of direct experimental control."
- note: Anchor used in the audit file for cross-tool and cross-host replication.

### Q240 The E Scale: N-rays, laboratories primed to expect it (added 2026-10-12d)
- source: `VPS-2026-03-20-the-e-scale`; veriphysics.substack.com, "The E Scale" (2026-03-20)
- URL: https://veriphysics.substack.com/p/the-e-scale
- locator: ¶5 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/vps-the-e-scale/body.txt
- branch: Triveritas / E scale anchor (E ~ 10); RH tag: dialectic
- quote: "Over 100 papers were published confirming the phenomenon, all from laboratories primed to expect it. When Robert Wood secretly removed the prism that was supposedly refracting the N-rays during a demonstration, Blondlot continued to report seeing them. No laboratory outside Nancy ever produced an independent confirmation. The entire empirical record was the product of expectation, not observation."
- note: Anchor used in the audit file for confirmation by same-family reviewers (TV-01).

### Q241 Comment on The L Scale: 'The actual numbers are irrelevant' (added 2026-10-12d)
- source: `VPS-COMMENTS-the-l-scale`; veriphysics.substack.com, comments on "The L Scale" (post id 190904255)
- URL: https://veriphysics.substack.com/p/the-l-scale/comments
- locator: comment id 229536173 (Vox Day, 2026-03-18)
- local copy: sources/raw/refresh-2026-10-12d/vps-comments/lscale.json
- branch: Triveritas / scoring; RH tag: dialectic
- quote: "It's supposed to be examples of where to assign things. It's all relative. The actual numbers are irrelevant."
- note: Day, comment id 229536173, 2026-03-18, replying to a reader who asked whether the scale is interval or ratio. Ordinal reading confirmed by the author; composites (means) of ordinal scores are then not well-defined.

### Q242 Comment on Q&A 3: one counterexample negates E (added 2026-10-12d)
- source: `VPS-COMMENTS-veriphysics-q-and-a-3`; veriphysics.substack.com, comments on "Veriphysics Q&A 3" (post id 191612179)
- URL: https://veriphysics.substack.com/p/veriphysics-q-and-a-3/comments
- locator: comment id 231331749 (Vox Day, 2026-03-22)
- local copy: sources/raw/refresh-2026-10-12d/vps-comments/qa3.json
- branch: Triveritas / E decision rule; RH tag: dialectic
- quote: "E is less conclusive in the affirmative, but it is no less decisive, because one counterexample is sufficient to negate E."
- note: Day, comment id 231331749, 2026-03-22. Asymmetric rule: E can be failed by one counterexample; the E scale's key question (Q237) counts confirmed against failed predictions. The two rules can disagree.

### Q243 Q&A 3: the three ways a claim can go wrong (added 2026-10-12d)
- source: `VPS-2026-03-21-veriphysics-q-and-a-3`; veriphysics.substack.com, "Veriphysics Q&A 3" (2026-03-21)
- URL: https://veriphysics.substack.com/p/veriphysics-q-and-a-3
- locator: ¶8 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/vps-veriphysics-q-and-a-3/body.txt
- branch: Triveritas / definition; RH tag: dialectic
- quote: "L evaluates deductive structure. M evaluates quantitative consistency. E requires contact with observations the claimant does not control. Each operates on a fundamentally different aspect of a claim’s epistemic standing, which means the failure modes do not overlap. A claim that passes all three filters has been checked against the only three ways a claim about reality can go wrong: it can be logically incoherent, it can be mathematically impossible, or it can be empirically false."
- note: Short operational definitions; here L is "deductive structure" again (version 1/2), not explanatory unity (version 3).

### Q244 Triveritan Test: absence of mathematics scores M 15 (added 2026-10-12d)
- source: `VPS-2026-03-23-the-triveritan-test-reformed-epistemology`; veriphysics.substack.com, "The Triveritan Test: Reformed Epistemology" (2026-03-23)
- URL: https://veriphysics.substack.com/p/the-triveritan-test-reformed-epistemology
- locator: ¶10 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/vps-the-triveritan-test-reformed-epistemology/body.txt
- branch: Triveritas / worked example, non-quantitative target; RH tag: dialectic
- quote: "Reformed epistemology makes no mathematical claims about the physical world. It generates no quantitative predictions. It produces no models that can be checked against data. The M dimension is not one on which the system fails spectacularly; it is one on which the system simply does not show up."
- note: Precedent for a target with no quantitative content: scored M = 15 (fail), not n/a. Contrast Q197 "where quantification is possible" and Q246. Composite 25 from (45, 15, 15).

### Q245 Response to a Religious Critique: scope (added 2026-10-12d)
- source: `VPS-2026-03-17-a-response-to-a-religious-critique`; veriphysics.substack.com, "A Response to a Religious Critique" (2026-03-17, updated 2026-03-21)
- URL: https://veriphysics.substack.com/p/a-response-to-a-religious-critique
- locator: ¶55 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/vps-a-response-to-a-religious-critique/body.txt
- branch: Triveritas / scope; RH tag: dialectic
- quote: "The Triveritas is defined as a criterion for warranted assent about claims concerning the physical world. It is an epistemological tool for evaluating scientific and philosophical claims. It is not a theological filter."
- note: Scope statement 2 (2026-03-17). Six days later the same author scored a theological epistemology with it (Q244) and reported a 94.7 for the doctrine of Total Depravity. Scope is not fixed.

### Q246 Response to a Religious Critique: quantities, predictions, observations (added 2026-10-12d)
- source: `VPS-2026-03-17-a-response-to-a-religious-critique`; veriphysics.substack.com, "A Response to a Religious Critique" (2026-03-17, updated 2026-03-21)
- URL: https://veriphysics.substack.com/p/a-response-to-a-religious-critique
- locator: ¶57 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/vps-a-response-to-a-religious-critique/body.txt
- branch: Triveritas / scope; RH tag: dialectic
- quote: "The Triveritas applies to claims about the physical world that involve quantities, predictions, and empirical observations. The Athanasian Creed is not a claim about fixation rates in population genetics."
- note: Narrowest scope statement. Under it, an audit's methodology is in scope only where it makes quantitative, predictive, empirical claims.

### Q247 Absolute Madness: Grok describes the scoring engine (RELAY) (added 2026-10-12d)
- source: `B2026-03-10-absolute-madness-or-historic-genius`; voxday.net, "Absolute Madness or Historic Genius" (2026-03-10 12:22:36 UTC)
- URL: https://voxday.net/2026/03/10/absolute-madness-or-historic-genius/
- locator: ¶6 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/post-2026-03-10-absolute-madness-or-historic-genius/body.txt
- branch: Triveritas / procedure as run by an AI rater; RELAY (rule U)
- quote: "accept internal arguments at face value, test L (deductive coherence + non-circularity), M (formal consistency + no free parameters), E (warranted base cases via independent anchoring), compute composite, run ±20% sensitivity, and declare Confirmed/Rejected."
- note: Speaker: Grok, quoted by Day without objection. The only step-by-step procedure found. "accept internal arguments at face value" means the rater did not check premises; "E (warranted base cases via independent anchoring)" and "M (formal consistency + no free parameters)" differ again from Q205/Q206.

### Q248 Invoking the Triveritas: triangulation (added 2026-10-12d)
- source: `B2026-10-09-mailvox-invoking-the-triveritas`; voxday.net, "Mailvox: Invoking the Triveritas" (2026-10-09 15:32:38 UTC)
- URL: https://voxday.net/2026/10/09/mailvox-invoking-the-triveritas/
- locator: ¶10 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/post-2026-10-09-mailvox-invoking-the-triveritas/body.txt
- branch: Triveritas / heuristic form, evolution context; RH tag: dialectic
- quote: "it is only when the logic, the math, and the empirical evidence all triangulate an answer can one be reasonably confident that the answer is both substantive and correct."
- note: Most recent statement (2026-10-09), in the post already quoted as Q118-Q121. Heuristic form: agreement of three lines of evidence on one answer.

### Q249 Invoking the Triveritas: logic is the weakest leg (added 2026-10-12d)
- source: `B2026-10-09-mailvox-invoking-the-triveritas`; voxday.net, "Mailvox: Invoking the Triveritas" (2026-10-09 15:32:38 UTC)
- URL: https://voxday.net/2026/10/09/mailvox-invoking-the-triveritas/
- locator: ¶4 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/post-2026-10-09-mailvox-invoking-the-triveritas/body.txt
- branch: Triveritas / L; RH tag: dialectic
- quote: "Logical validity is the weakest and least rhetorically effective leg. That’s exactly what the ID guys have been doing for decades and it hasn’t gotten them anywhere. Only a small percentage of the population can follow logic, the scope of the logic often isn’t quite as grand as the logician characteristically supposes, and it has no way of checking itself for validity."
- note: Day ranks the legs by rhetorical effect; the proofs give no ordering within a tier.

### Q250 The Real Rate Revolution: 'Applied Triveritas' (RELAY, earliest blog use found) (added 2026-10-12d)
- source: `B2026-02-08-the-real-rate-revolution`; voxday.net, "The Real Rate Revolution" (2026-02-08)
- URL: https://voxday.net/2026/02/08/the-real-rate-revolution/
- locator: single-line extracted text; character offset 6027 of the whitespace-normalised file
- local copy: sources/raw/day/blog-2026-02-08-the-real-rate-revolution.txt
- branch: Triveritas / dating; RELAY (rule U)
- quote: "Applied Triveritas exists because someone tried to retreat into mathematical abstraction. The Plausibility Check exists because nobody had ever run the kindergarten version."
- note: Speaker: "Athos" (Day's AI co-author), quoted by Day. 2026-02-08 is the earliest of the 28 voxday.net search hits for "triveritas" (search fetched 2026-10-12); it predates the Treatise announcement (2026-02-18) and the Zenodo proofs (2026-02-21). No definition is given in this post.

### Q251 The Irrelevance of k = mu: any one link can err (added 2026-10-12d)
- source: `B2026-08-26-the-irrelevance-of-k-%ce%bc`; voxday.net, "The Irrelevance of k = μ" (2026-08-26)
- URL: https://voxday.net/2026/08/26/the-irrelevance-of-k-%ce%bc/
- locator: single-line extracted text; character offset 4362 of the whitespace-normalised file
- local copy: sources/raw/day/blog-2026-08-26-the-irrelevance-of-k-%ce%bc.txt
- branch: Triveritas / applied to a critic (keruru); RH tag: dialectic
- quote: "His work here is very far from valueless, as I will demonstrate, but it is nevertheless incorrect due to his failure to anchor the abstract mathematical elements in material reality. This also, rather fortuitously, demonstrates the importance of the Triveritas, as any one link in the triad is capable of serious error when allowed to operate outside the bounds of the other two."
- note: Day applies the triad to a critic's martingale argument for k = mu (branch B3/B7): the charge is M without E ("failure to anchor the abstract mathematical elements in material reality"). Same structure as method-audit finding MA-05 against this audit's simulation-based external verdicts.

### Q252 Veriphysics, as requested: 'wrecking ball' (book blurb) (added 2026-10-12d)
- source: `B2026-02-18-veriphysics-as-requested`; voxday.net, "Veriphysics, as requested" (2026-02-18 18:12:39 UTC)
- URL: https://voxday.net/2026/02/18/veriphysics-as-requested/
- locator: ¶5 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/post-2026-02-18-veriphysics-as-requested/body.txt
- branch: Triveritas / stated targets; RH tag: rhetoric
- quote: "Any claim that cannot satisfy all three of its conditions — logical validity, mathematical coherence, and empirical anchoring — does not merit assent, regardless of the credentials of those asserting it. Applied to the crown jewels of Enlightenment thought, including the cogito, Darwinian evolution, classical economics, and social contract theory, the Triveritas serves as a wrecking ball."
- note: Device: metaphor (wrecking ball), blurb register. Function: sell the book; name the targets (the cogito, Darwinian evolution, classical economics, social contract theory). Dialectical core: Q195. The Treatise ebook (Amazon ASIN B0GP18SX2D) was not bought or read.

### Q253 Veriphysics, as requested: 'heuristic' (added 2026-10-12d)
- source: `B2026-02-18-veriphysics-as-requested`; voxday.net, "Veriphysics, as requested" (2026-02-18 18:12:39 UTC)
- URL: https://voxday.net/2026/02/18/veriphysics-as-requested/
- locator: ¶9 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/post-2026-02-18-veriphysics-as-requested/body.txt
- branch: Triveritas / status; RH tag: dialectic
- quote: "I leave it to the readers to decide how effective it is as a post-Enlightenment proto-philosophy, but there are already some signs that the triveritan approach it utilizes is a fundamentally more viable and reliable heuristic than historical truth-metrics."
- note: Day's own word for it at launch: "heuristic"; the claim is comparative and hedged ("some signs").

### Q254 Four Hard Cases: 'this is, of course, backtesting' (added 2026-10-12d)
- source: `VPS-2026-03-15-four-hard-cases-and-the-triveritas`; veriphysics.substack.com, "Four Hard Cases and the Triveritas" (2026-03-15)
- URL: https://veriphysics.substack.com/p/four-hard-cases-and-the-triveritas
- locator: ¶15 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/vps-four-hard-cases-and-the-triveritas/body.txt
- branch: Triveritas / limits; RH tag: dialectic
- quote: "While this is, of course, backtesting, which is not an entirely reliable indicator of a useful predictive model, it is a very reasonable test of the metric’s theoretical utility in comparison with the historical scientific record."
- note: Credit to Day: he states that the historical cases are backtests.

### Secondary, NOT Day: third-party applier, allies, critics, readers (Q255-Q264)

Kept in this file only because this pass's write set is the Day-side source files; on integration these belong in `quotes-critics.md` / `opponents/`. None of them is Day's statement. Thin: no critique of the Triveritas by any critic already tracked in this repository (Hancock, Myers, McCarthy, Camestros, Mansfield) was found; two web searches on 2026-10-12 returned only Day's own pages.

### Q255 Kererū, Triveritas Stress Test: binary scoring protocol for essays (added 2026-10-12d)
- source: `Z19198681`; Zenodo 19198681, C. Kererū (Zenodo creators "Keruru, Christopher"; "Kerur, Claude"), "The Triveritas Stress Test" (2026-03-24)
- URL: https://zenodo.org/records/19198681
- locator: p.3 of the PDF, l.149 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-19198681/paper.txt
- branch: THIRD-PARTY APPLIER (critic of Day on k = mu, here a user of his tool); secondary
- speaker: NOT DAY (see branch line)
- quote: "Each piece was scored on three legs using a binary Pass/Fail protocol: Leg 1 — Logical Validity: Does the inferential chain from premises to conclusion hold? Are the load-bearing assumptions stated? Are there non-sequiturs or unacknowledged leaps? Leg 2 — Mathematical Coherence: Where quantitative claims are made, do the numbers survive independent scrutiny? Where quantitative reasoning could have been applied but was not, the absence is noted. Leg 3 — Empirical Anchoring: Are the load-bearing empirical claims veriﬁable, correctly cited, and non-circular? Could countervailing evidence have been presented but was not? Is the evidence base thinner than the conﬁdence of the prose suggests?"
- note: The only application to analytical writing found, and the closest precedent for applying the Triveritas to an audit. Leg questions are the author's operationalisation, not Day's. Ligatures as in the PDF text layer.

### Q256 Kererū: Claude excluded from scoring (added 2026-10-12d)
- source: `Z19198681`; Zenodo 19198681, C. Kererū (Zenodo creators "Keruru, Christopher"; "Kerur, Claude"), "The Triveritas Stress Test" (2026-03-24)
- URL: https://zenodo.org/records/19198681
- locator: p.4 of the PDF, l.193 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-19198681/paper.txt
- branch: THIRD-PARTY APPLIER; secondary
- speaker: NOT DAY (see branch line)
- quote: "Claude (Anthropic) was excluded from scoring legs because it served as the study’s composition and analysis interface. This exclusion is a limitation."
- note: A same-tool exclusion rule adopted by a Triveritas user: the model that composed the study did not score it. This repository's Triveritas application cannot meet that rule (applier is Claude).

### Q257 Kererū: Leg 1 models failed every piece (added 2026-10-12d)
- source: `Z19198681`; Zenodo 19198681, C. Kererū (Zenodo creators "Keruru, Christopher"; "Kerur, Claude"), "The Triveritas Stress Test" (2026-03-24)
- URL: https://zenodo.org/records/19198681
- locator: p.5 of the PDF, l.268 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-19198681/paper.txt
- branch: THIRD-PARTY APPLIER; secondary; reliability evidence
- speaker: NOT DAY (see branch line)
- quote: "Both Leg 1 models scored F on every piece where they ran, including the three pieces the human scored P (Pieces 5, 9, 10). Human-model agreement rate on L1: 7/10 (70%) on the F scores, 0/3 on the P scores. Models are systematically more aggressive."
- note: Human-model agreement on L was 0 of 3 on the human's passes. Evidence that the L leg is not applied reproducibly across raters.

### Q258 Kererū: plausible-sounding opposition to anything (added 2026-10-12d)
- source: `Z19198681`; Zenodo 19198681, C. Kererū (Zenodo creators "Keruru, Christopher"; "Kerur, Claude"), "The Triveritas Stress Test" (2026-03-24)
- URL: https://zenodo.org/records/19198681
- locator: p.8 of the PDF, l.463 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-19198681/paper.txt
- branch: THIRD-PARTY APPLIER; secondary; reliability evidence
- speaker: NOT DAY (see branch line)
- quote: "That may reﬂect genuine weakness or it may reﬂect the model’s ability to generate plausible-sounding opposition to virtually anything."
- note: A failure mode of AI raters stated by a Triveritas user.

### Q259 Van Allen, Quadriveritas: a fourth criterion; M renamed (added 2026-10-12d)
- source: `Z18816629`; Zenodo 18816629, Van Allen & "Claude Sonnet 4.6", "The Quadriveritas" (2026-02-28)
- URL: https://zenodo.org/records/18816629
- locator: p.1 of the PDF, l.1 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18816629/paper.txt
- branch: ALLY EXTENSION; secondary
- speaker: NOT DAY (see branch line)
- quote: "The Quadriveritas is a four-dimensional assessment framework that extends the epistemological architecture of the Triveritas by adding a fourth criterion, Teleological Adequacy (T), to the original three of Logical Validity (L), Structural Coherence (M), and Empirical Anchoring (E)."
- note: An ally renames M "Structural Coherence" to apply it to theology: evidence that M as defined (Q205) does not travel to non-quantitative targets without redefinition. Co-author listed on Zenodo as "Claude Sonnet 4.6".

### Q260 Howland, Quadrium: utility leaks into truth scoring (added 2026-10-12d)
- source: `Z19532352`; Zenodo 19532352, Howland, "The Quadrium: Truth and Utility as Independent Measurements" (2026-04, v1.0)
- URL: https://zenodo.org/records/19532352
- locator: p.1 of the PDF, l.18 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-19532352/paper.txt
- branch: ALLY EXTENSION; secondary
- speaker: NOT DAY (see branch line)
- quote: "The Triveritas evaluates whether a claim is true. It does not evaluate whether a true claim is useful, or whether a useful claim is true. Without a dedicated axis for utility, utility has no home in the evaluation. When utility has no home, it leaks into the truth evaluation as apparent truth."
- note: An ally's stated failure mode of the three-axis scoring (utility read as truth). Line-break hyphens in the PDF text were avoided by anchor choice.

### Q261 Religious critic (name not given by Day; original deleted): 'human calculator' (RELAY) (added 2026-10-12d)
- source: `VPS-2026-03-17-a-response-to-a-religious-critique`; veriphysics.substack.com, "A Response to a Religious Critique" (2026-03-17, updated 2026-03-21)
- URL: https://veriphysics.substack.com/p/a-response-to-a-religious-critique
- locator: ¶8 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/vps-a-response-to-a-religious-critique/body.txt
- branch: CRITIC; secondary; RELAY via Day (rule U); RH tag: rhetoric
- speaker: NOT DAY (see branch line)
- quote: "By elevating his mathematical and logical filters to the level of an absolute judge, Vox Day has constructed a framework that subjects the very nature of God and reality to the verdict of a human calculator."
- note: Day reproduces the critique "in its entirety" after its author deleted it; the original URL (sainttommy.substack.com/p/the-stolen-clothes-of-veriphysics) returned HTTP 404 on 2026-10-12. Text is therefore secondhand through the criticised party. Theological objection; no bearing on the mathematics.

### Q262 Reader 'Stephen' relaying a Claude review: evolution case needs independent support (RELAY) (added 2026-10-12d)
- source: `VPS-COMMENTS-grok-pronounces-the-verdict`; veriphysics.substack.com, comments on "Grok Pronounces the Verdict" (post id 190842069)
- URL: https://veriphysics.substack.com/p/grok-pronounces-the-verdict/comments
- locator: comment id 227676148 (Stephen, 2026-03-14)
- local copy: sources/raw/refresh-2026-10-12d/vps-comments/verdict.json
- branch: CRITIC-SIDE POINT; secondary; RELAY (reader quoting an AI review), comment id 227676148, 2026-03-14
- speaker: NOT DAY (see branch line)
- quote: "The evolution case needs independent mathematical support or explicit flagging as contested -The conclusion's language needs to be calibrated down from "solved" to something the evidence actually supports"
- note: A valid critic-side point recorded by Day's own reader: the Triveritas score for evolution rests on Day's own uncorroborated calculation. Day's reply (id 227686215) disputes the AI's strictness, not this point.

### Q263 Reader 'Azamat Baghatov': plum pudding was falsified by observation (added 2026-10-12d)
- source: `VPS-COMMENTS-veriphysics-q-and-a-3`; veriphysics.substack.com, comments on "Veriphysics Q&A 3" (post id 191612179)
- URL: https://veriphysics.substack.com/p/veriphysics-q-and-a-3/comments
- locator: comment id 281337757 (Azamat Baghatov, 2026-06-23)
- local copy: sources/raw/refresh-2026-10-12d/vps-comments/qa3.json
- branch: CRITIC-SIDE POINT; secondary; comment id 281337757, 2026-06-23
- speaker: NOT DAY (see branch line)
- quote: "the plum pudding model falsified by observation, rather than mathematics?"
- note: A classification objection to Case 6 of the Empirical Proof. The paper's own outcome line reads "Refuted by Rutherford's gold foil experiment (1911)" (Zenodo 18724496, case 6): an observation. No reply from Day in the fetched thread.

### Q264 Reader 'Faith in God': the weakness is E (added 2026-10-12d)
- source: `VPS-COMMENTS-veriphysics-q-and-a-3`; veriphysics.substack.com, comments on "Veriphysics Q&A 3" (post id 191612179)
- URL: https://veriphysics.substack.com/p/veriphysics-q-and-a-3/comments
- locator: comment id 231269029 (Faith in God, 2026-03-21)
- local copy: sources/raw/refresh-2026-10-12d/vps-comments/qa3.json
- branch: SYMPATHETIC READER; secondary; comment id 231269029, 2026-03-21
- speaker: NOT DAY (see branch line)
- quote: "I think the weakness of the system is E. The interpretation of the evidence is often more important than the evidence itself."
- note: Day's reply is Q242.

### Late additions (Q265-Q271; speaker stated on each branch line)

### Q265 Comment: the Triveritas is 'merely an analytical tool' (added 2026-10-12d)
- source: `VPS-COMMENTS-grok-pronounces-the-verdict`; veriphysics.substack.com, comments on "Grok Pronounces the Verdict" (post id 190842069)
- URL: https://veriphysics.substack.com/p/grok-pronounces-the-verdict/comments
- locator: comment id 227974531 (Vox Day, 2026-03-15)
- local copy: sources/raw/refresh-2026-10-12d/vps-comments/verdict.json
- branch: Triveritas / separability from Veriphysics; RH tag: dialectic; speaker: Day
- quote: "The Triveritas isn't its own foundation. It's merely an analytical tool that is part of the epistemology of Veriphysics. It appears you have not read the treatise yet. The Triveritas doesn't require Christianity to function any more than Popperian falsification does."
- note: Day, comment id 227974531, 2026-03-15. In Day's words the tool is detachable from the metaphysics; this is the licence for applying it here without adopting Veriphysics.

### Q266 Grok Pronounces the Verdict: a 'threshold' of 90 (RELAY) (added 2026-10-12d)
- source: `VPS-2026-03-14-grok-pronounces-the-verdict`; veriphysics.substack.com, "Grok Pronounces the Verdict" (2026-03-14)
- URL: https://veriphysics.substack.com/p/grok-pronounces-the-verdict
- locator: ¶31 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/vps-grok-pronounces-the-verdict/body.txt
- branch: Triveritas / threshold; RELAY (rule U); speaker: Grok, quoted by Day
- quote: "The framework functions as an epistemic filter, not flattery; the ≥90 threshold is satisfied on clear passing cases while failures are informative."
- note: A third pass mark (90), from the AI rater, beside 60 (Q226) and 50 (Q235, Q238).

### Q267 Absolute Madness: every paper scores 90-94 (RELAY) (added 2026-10-12d)
- source: `B2026-03-10-absolute-madness-or-historic-genius`; voxday.net, "Absolute Madness or Historic Genius" (2026-03-10 12:22:36 UTC)
- URL: https://voxday.net/2026/03/10/absolute-madness-or-historic-genius/
- locator: ¶3 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/post-2026-03-10-absolute-madness-or-historic-genius/body.txt
- branch: Triveritas / rater behaviour; RELAY (rule U); speaker: Grok, quoted by Day
- quote: "Every paper scores 90–94 with strength 9. Gemini and Deepseek independently confirmed all of them in the highly-warranted range."
- note: Eight of the authors' own papers, scored by AI raters at the authors' request, all land in a 5-point band. A scale that does not separate its inputs gives no information about them; cf. the method audit's point that a zero BLOCKER rate is uninformative without a catch rate (MA-01).

### Q268 Demarcation 6.3: sensitivity band for Darwinian evolution (added 2026-10-12d)
- source: `Z18924026`; Zenodo 18924026, Day & Athos, "Solving the Scientific Demarcation Problem" (2026-03-09, modified 2026-03-15)
- URL: https://zenodo.org/records/18924026
- locator: p.15 of the PDF, l.674 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18924026/paper.txt
- branch: Triveritas / sensitivity analysis; RH tag: dialectic; speaker: Day & Athos
- quote: "Darwinian Evolution: L ranges from 48 to 72. M ranges from 4 to 6. E ranges from 56 to 84. Maximum composite under maximum favorable perturbation: ~ 54. The theory remains below 55 under every perturbation. The M failure is so severe (the theory possesses no internal mathematical architecture) that even a 20% increase from 5 to 6 does not rescue it."
- note: The band is multiplicative (plus or minus 20% of the score), so the decisive score, M ~ 5, is varied by one point (4 to 6). The lower the score, the less the sensitivity analysis tests it. Same defect as a 3x band applied to a value near zero (method audit MA-02).

### Q269 Demarcation 3.4: population genetics 'not part of the modern synthesis' (added 2026-10-12d)
- source: `Z18924026`; Zenodo 18924026, Day & Athos, "Solving the Scientific Demarcation Problem" (2026-03-09, modified 2026-03-15)
- URL: https://zenodo.org/records/18924026
- locator: p.6 of the PDF, l.267 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18924026/paper.txt
- branch: Triveritas / worked example, evolution, basis of M ~ 5; RH tag: dialectic; speaker: Day & Athos
- quote: "Neutral Theory and the population genetics of Fisher, Haldane, and Wright are not part of the modern synthesis; they are independent mathematical frameworks."
- note: The M ~ 5 score depends on this classification. Day-side reading: the 1940s verbal synthesis is the target. Critic-side reading: the target is defined so that its mathematics is excluded, then scored for having none. Not scored here; no source on the history of the synthesis was fetched in this pass. The quote starts mid-sentence (the sentence opens "Kimura's").

### Q270 Demarcation 6.2: 'Selective Turnover Coefficient' and 'Bernoulli Barrier' (added 2026-10-12d)
- source: `Z18924026`; Zenodo 18924026, Day & Athos, "Solving the Scientific Demarcation Problem" (2026-03-09, modified 2026-03-15)
- URL: https://zenodo.org/records/18924026
- locator: p.15 of the PDF, l.647 of the local text (pdftotext -layout)
- local copy: sources/raw/refresh-2026-10-12d/zen-18924026/paper.txt
- branch: Triveritas / worked example, evolution; links to branches G and H; RH tag: dialectic; speaker: Day & Athos
- quote: "The Selective Turnover Coefficient (d ≈ 0.45) and the Bernoulli Barrier close the standard escape routes."
- note: The Triveritas score for evolution imports d = 0.45 (branch H) and the Bernoulli Barrier (branch G), both audited in this repository.

### Q271 Treatise 024: 'fewer than three hundred' against 'at least twenty million' (added 2026-10-12d)
- source: `B2026-02-27-veriphysics-the-treatise-024`; voxday.net, "Veriphysics: The Treatise 024" (2026-02-27 10:16:03 UTC)
- URL: https://voxday.net/2026/02/27/veriphysics-the-treatise-024/
- locator: ¶6 of the non-empty paragraphs of the saved body text
- local copy: sources/raw/refresh-2026-10-12d/post-2026-02-27-veriphysics-the-treatise-024/body.txt
- branch: Triveritas / worked example, evolution; parameters for `ledgers/versions.md`; RH tag: dialectic; speaker: Day
- quote: "Using the most generous assumptions—the longest timescales proposed, the shortest generation lengths, the fastest fixation rates ever observed in any organism—the mathematics permits fewer than three hundred fixed mutations in the human lineage. The theory requires at least twenty million."
- note: Numbers as stated in the Treatise serial of 2026-02-27. Not reconciled here with the MITTENS versions (branch A).

## Refresh 2026-10-13 quotes (Q272-Q274; added 2026-10-13, integration of L1b and L1c)

Passages cited by the L1b and L1c write-ups that had no Q id. Each checked by machine against the held body text (paragraph numbers count non-empty lines).

### Q272 'The data is complete': 98.8% of coding positions are found (added 2026-10-13)
- source: voxday.net, "How Biologists Keep "Proving" Selection" (2026-10-11 14:13:57 UTC) (SG cross-post not seen)
- locator: ¶12 of the non-empty paragraphs of the saved body text (the diagnostics paragraph; the sentence is in the middle of the paragraph, followed without a space by "Is the substitution classification correct?")
- local copy: sources/raw/refresh-2026-10-11/post-how-biologists-keep-proving-selection/body.txt
- branch: ROOT-FM / selection strength / dN/dS; RH tag: dialectic (a numeric completeness statement)
- quote: "98.8% of coding positions are found."
- note: The same paragraph states "The extraction contains 226 million positions for chromosome 1 alone". Reproduced in kind by L1b (98.87% of CDS bases, 98.84% of codons with a first-row chimp base on the audit's Cactus extraction). A credit to Day, R4-L1b "Who this helps".

### Q273 'The whole-genome alignment we utilize doesn't have this scoring bias' (added 2026-10-13)
- source: voxday.net, "The Method is the Conclusion" (2026-10-12 14:12:35 UTC) (SG cross-post not seen)
- locator: ¶11 of the non-empty paragraphs of the saved body text (first sentence)
- local copy: sources/raw/refresh-2026-10-12/post-the-method-is-the-conclusion/body.txt
- branch: ROOT-FM / selection strength / dN/dS; RH tag: dialectic
- quote: "The whole-genome alignment we utilize doesn’t have this scoring bias."
- note: Day exempts the Cactus whole-genome alignment from the bias he asserts in Q180-Q182. The paragraph continues: "Cactus aligns DNA based on genomic context ... When we project gene coordinates onto that alignment and extract codons, we get ALL the aligned coding positions, not just the ones that are deemed to look conserved at the protein level." Relevant to DN6 Reading d (an extended reading, not taken from his text).

### Q274 'What the Consortium's method actually measured' (added 2026-10-13)
- source: voxday.net, "The Method is the Conclusion" (2026-10-12 14:12:35 UTC) (SG cross-post not seen)
- locator: ¶14 of the non-empty paragraphs of the saved body text (first two sentences)
- local copy: sources/raw/refresh-2026-10-12/post-the-method-is-the-conclusion/body.txt
- branch: ROOT-FM / selection strength / dN/dS; RH tag: dialectic
- quote: "So what the Consortium’s method actually measured is: “among the coding positions conserved enough to survive protein alignment, how conserved are they?” That’s not a valid measurement, that’s a tautological quantification."
- note: The one sentence that states outright that the Consortium's 0.23 came through a protein alignment. Held CSAC 2005 text says the 13,454-gene set came from the BLASTZ genome alignment (quotes-literature.md CSAC2005, Methods, Genome alignment). DN6 Reading a (fidelity `misread`).

## Refresh 2026-10-13 quotes (Q275-Q278; added 2026-10-13, integration of L5)

Passages cited by the L5 write-up that had no Q id. Each checked as an exact substring of the held extracted text `sources/raw/day/blog-2026-01-14-empirically-impossible.txt` (html sha256 5303e99360342a1e...bc025b76, fetched 2026-10-07). Paragraph numbers follow Q55's convention (non-empty lines, the TITLE line counting as ¶1; Q55 is ¶5). The s = 1e-3 figure is Q44.

### Q275 Comparator: 'approximately 15,500 fixations per 7,000-year period' - blog 2026-01-14
- source: `B2026-01-14-empirically-impossible` (blog post dated 2026-01-14); URL: https://voxday.net/2026/01/14/empirically-impossible/
- locator: ¶4 of extracted text
- quote: "The Modern Synthesis requires approximately 20 million fixations over the 9 million years since the human-chimpanzee divergence, implying a rate of 2.22 fixations per year or approximately 15,500 fixations per 7,000-year period."
- note: 20,000,000 / 9,000,000 y x 7,000 y = 15,556. No selection coefficient and no panel scaling stated. Used by claim C (Statement), C1, C6 and R4-L5.

### Q276 Inference: 'decisively favors the MITTENS prediction' - blog 2026-01-14
- source: `B2026-01-14-empirically-impossible`; URL as Q275
- locator: ¶6 of extracted text
- quote: "This result decisively favors the MITTENS prediction over the Modern Synthesis expectation."
- note: The sentence carrying the inference from zero observed to a refuted rate. RH tag: dialectic (a checkable comparative claim; R4-L5 scores it).

### Q277 Framing: 'very strongly support Probability Zero's assertion' - blog 2026-01-14
- source: `B2026-01-14-empirically-impossible`; URL as Q275
- locator: ¶2 of extracted text (the opening paragraph; the R4-L5 fix pass numbered it ¶3 by a different count)
- quote: "the results very strongly support Probability Zero‘s assertion of the mathematical impossibility of the theory of evolution by natural selection."
- note: The post frames the comparator as bearing on evolution by natural selection; s is not stated. RH tag: dialectic.

### Q278 Conclusion: 'inoperative in human populations for at least 7,000 years' - blog 2026-01-14
- source: `B2026-01-14-empirically-impossible`; URL as Q275
- locator: ¶7 of extracted text
- quote: "Evolution by natural selection, as a mechanism of directional change capable of producing adaptation or speciation, has been empirically demonstrated to be inoperative in human populations for at least 7,000 years."
- note: Shows the selection-driven reading of the comparator is the post's own framing. RH tag: dialectic.

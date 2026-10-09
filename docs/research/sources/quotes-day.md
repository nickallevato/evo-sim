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

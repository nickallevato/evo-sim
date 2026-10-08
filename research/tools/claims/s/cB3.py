from common import *
RV2='`research/checks/REVIEW.md#2026-10-07--correctness-review-2-sonnet-on-b0b3`'

add(id='B3',slug='k-neq-mu-values-umbrella',title='k differs from mu: the family of Day k/mu values (N/Ne, 0.743, 0.5, 32.3, 800,000) and their status',side='day',branch='B',parent='B',
 edges=[('supports','B'),('depends-on','B3a'),('depends-on','B3b'),('depends-on','B3c'),('depends-on','B3d')],
 lb=(True,'with B1/B2, one route to closing the neutral escape; but its N/Ne leg was withdrawn by Day on 2026-08-27 (B3g)'),
 sourcing='firsthand',status='reviewed',v=('pending','partial','contested'),
 quotes=[Q('NNP','In mammals, census populations exceed diversity-derived N_{e} by 19- to 46-fold.',file='day/zenodo-18429937.txt',note='abstract'),
   Q('RRME','Applied to four generations of human census data, it yields k = 0.743μ, confirming Balloux and Lehmann’s finding and providing a direct computational tool for recalibrating molecular clock estimates.',file='day/zenodo-18525262.txt'),
   Q('EDU','comparing Bergeron’s (2023) pedigree-measured mammalian mutation rate against the required substitution rate from Yoo et al. (2025) gives k = 32.3μ, not k = μ.',file='day/blog-2026-10-01-the-education-of-a-population-geneticist.txt')],
 formal='''| k/μ | Where / when | Basis | Direction (clock) | Status in this repo |
|---|---|---|---|---|
| N/Nₑ, 19–46 for mammals | Z18429937 (2026-01-29) | census vs diversity-derived Nₑ | k > μ (clock too slow, dates too old) | B3a; withdrawn by Day 2026-08-27 (B3g) |
| 30.3 / 15.2 (human), 9.1–30.3 (chimp) | Z18525547 (2026-02-08) | N = 50–100k, Nₑ = 3,300; chimp N = 300k–1M, Nₑ = 33,000 | k > μ | B4 |
| 800,000 | blog 2026-04-30 (Grok exchange) | N = 8e9, Nₑ = 1e4 | k > μ | B3f |
| 0.743 | Z18525262 (2026-02-08) | census 1950–2025, four cohorts | k < μ (dates too young) | B3c |
| ≈0.5 or less | blog 2026-02-09 | six-country d vs k data (per harvest note) | k < μ | not verified (blog only) |
| 32.3 | blog 2026-10-01 | Bergeron pedigree μ vs Yoo required rate; no derivation | k > μ | B3d |
| 1 (Nₑ never enters) | blog 2026-08-27 | Day's own concession | k = μ | B3g |
| median 25 over 55 vertebrates | blog 2026-05-07 | pedigree μ vs phylogenetic k; source not cited | k > μ | B3d |
The values disagree in direction (0.743, 0.5 vs ≥15) and in basis (census history, N/Nₑ, rate comparison). The version ledger records the 0.743 and 32.3 values as mutually inconsistent in direction.''',
 a_stated='k = μ fails for real populations (various mechanisms).',a_impl='Each version assumes its own meaning of k (per generation vs per year; per site vs per genome; fixed substitutions vs observed differences).',
 against=rq('KRE','Mutation supply is 2Nμ with N the census count — mutations occur in gametes, and every reproducing individual contributes gametes.',loc='para 6 (keruru, retraction of the N/Nₑ leg)')+'\n  '+rq('GG','and then what you\'re left with is a neutral substitution rate that\'s equal to the mutation rate',loc='t=01:48:19 (Hancock)'),
 support=rq('BL','we show that the substitution rate at neutral genes does depend on population size fluctuations in the presence of overlapping generations',loc='Abstract')+' (partial support, B3b).',
 weak='keruru is an LLM-assisted blog author who first endorsed the N/Nₑ leg; his retraction is corroborated by Day himself (B3g), which is stronger evidence than keruru alone. Hancock\'s derivation is stated verbally (auto-captions).',
 lit=[lit_row('Balloux & Lehmann 2012','N-dependence only for overlapping generations plus fluctuating N; non-overlapping: "population size fluctuations do not affect substitution rates at neutral loci in a population with discrete nonoverlapping generations"','verified-partial (ledger); no 0.743 or 32.3 in the text'),
      lit_row('Kimura 1962; Kimura & Ohta 1969','U = 1/2N for a neutral gene; fraction 1/2N reach fixation','see B7a, B7b')],
 p_claim='k ≠ μ in real populations by factors of 0.7 to 10⁵ depending on version.',p_opp='k = μ for any neutral model with E[Δp] = 0 and census-based supply, except in the overlapping-generations-plus-fluctuating-N setting of B&L (RESULTS B3; B3b queued).',
 p_change='B3b result for overlapping generations with fluctuating N; the 32.3 basis (B3d).',
 check='Script: `research/checks/b3_N_vs_Ne.py` (seed 13) · see B3a. Review: '+RV2,
 sim=['mutation-supply N (census | reproducing | user)','fixation-probability N','overlap (survival s)','N(t) fluctuation schedule','rate unit (per generation | per year | per average generation time)'])

add(id='B3a',slug='fixation-probability-1-over-2ne',title='k = 2N mu × 1/(2Ne) = mu N/Ne: supply uses census N, fixation probability uses Ne',side='day',branch='B',parent='B3',
 edges=[('supports','B3')],lb=(True,'the N/Nₑ leg of B3 and of the recalibration (B4) rests on it; withdrawn by Day 2026-08-27 (B3g)'),
 sourcing='firsthand',status='reviewed',v=('holds','misread','contradicted'),
 quotes=[Q('NNE','k = 2Nμ × 1/(2N_{e}) = μ × (N/N_{e}) (1)',file='day/zenodo-18525547.txt'),
   Q('NNE','This cancellation is invalid. The mutation supply term uses census N (every individual can mutate), while the fixation probability is governed by effective population size N_{e} (drift operates on N_{e}, not N).',file='day/zenodo-18525547.txt',note='abstract'),
   Q('R2','k = 2Nμ × 1/(2Nₑ) = μ(N/Nₑ)',file='day/blog-2026-02-04-response-to-dennis-mccarthy-round-2.txt')],
 formal='''Day: k = (2Nμ)·P_fix with P_fix = 1/(2Nₑ) ⇒ k/μ = N/Nₑ.
Critics/literature: P_fix = p₀ = 1/(2N) (initial frequency; martingale property) ⇒ k/μ = 1 for any N, Nₑ.

Glossary: N = census diploids; Nₑ = effective size (variance); neutral P_fix = starting frequency, Nₑ governs the timescale (glossary).
**Internal consistency:** Day's own Z22129121 (2026-08-27) states "the neutral fixation probability exactly 1/(2N)" and "Every neutral mutation begins as a single copy in a single individual, at a frequency of 1/(2N)." (B7). The conclusion k = μN/Nₑ follows algebraically from its premise; the premise conflicts with Day's later texts and with Kimura 1962/1969 (B7a, B7b).
Empirical hint on direction: Keightley 2012 reports that pedigree μ ≈ 1.1e-8 is "about twofold lower than estimates based on the human-chimp divergence" (k > μ by ~2, far from 15–800,000; generation-time and calibration issues not separated).''',
 a_stated='"The mutation supply term uses census N (every individual can mutate), while the fixation probability is governed by effective population size N_{e}".',a_impl='A new mutant\'s fixation probability depends on Nₑ rather than on its starting frequency. In an exchangeable model P_fix = p₀ exactly.',
 against=rq('KRE','The fixation probability of a single new mutant in both chains: exactly 1/(2N_census), to fifteen decimal places.',loc='para 9 (keruru; exact Markov chains incl. a sweepstakes model; code not retrieved)')+'\n  '+rq('MC1','50,000 x 9 million = 450 billion new mutations altogether.',loc='para 50 (McCarthy)')+' (uses N = Nₑ)',
 support='Day (2026-04-30, Grok exchange, B3f): LLM concedes both propositions and computes 800,000μ from them. Hössjer\'s review uses 2Nμ × 1/(2N) = μ (rate dμ), i.e. does not adopt B3a.',
 weak='keruru\'s chains were not retrieved; the sweepstakes parent is drawn uniformly at random (Day\'s objection, RESP). The 2026-04-30 LLM exchange is not independent evidence (it derives 800,000μ from stipulated premises).',
 lit=[lit_row('Kimura 1962','"The probability of fixation of an individual mutant gene is obtained from (8) by putting p = 1/(2N)." and "if we let s → 0 in (10), we obtain U = 1/2N, the result known for a neutral gene" (N = "the number of reproducing individuals")','verified-misread for 1/(2Nₑ) (ledger). Caution: the 1962 model has a single N serving as both counting and variance size, so it does not itself separate census from Nₑ'),
      lit_row('Kimura & Ohta 1969','"the remaining minority (fraction 1/2N) spread over the entire population (i.e. reach fixation)" alongside Nₑ for the time','supports critics (ledger)')],
 p_claim='(RESULTS B3, P1 as the critics\' side) —',
 prereg_note='Pre-registered predictions (copied from RESULTS B3): P1 P_fix = 1/M for every Nₑ; P2 t_fix scales with Nₑ. Day\'s model predicts P_fix = 1/(2Nₑ).',
 p_opp='P_fix = 1/(2N) = 1/M independent of Nₑ; t_fix ∝ Nₑ.',
 p_change='A non-exchangeable neutral setting (B3b) in which the long-run neutral rate is not μ per generation would restore part of B3; a corrected P_fix = 1/(2Nₑ) in any exchangeable model would overturn the check.',
 check='Script: `research/checks/b3_N_vs_Ne.py` (seed 13) · Result: both predictions confirmed. M = 400, 10⁶ replicates. Nₑ = 200/160/100/40/19: P_fix = 0.00250/0.00252/0.00257/0.00248/0.00257 vs 1/(2N) = 0.00250; Day 1/(2Nₑ) = 0.00249/0.00312/0.00498/0.01235/0.02676; t_fix/Nₑ ≈ 3.95–4.07. Review #2: P_fix = 1/M is a theorem in this class (frequency is a martingale), so the run verifies the code; the verdict is provisional until B3b. Review: '+RV2,
 sim=['Nₑ/N via offspring variance','exchangeable vs non-exchangeable reproduction','sweepstakes events'])

add(id='B3b',slug='balloux-lehmann-overlap-and-fluctuation',title='Balloux & Lehmann 2012: k depends on N under overlapping generations plus fluctuating demography',side='day',branch='B',parent='B3',
 edges=[('supports','B3'),('depends-on','B3c')],lb=(False,'the only B3 leg with literature support; but magnitude (0.743, 32.3) is not from the paper'),
 sourcing='firsthand',status='extracted',v=('pending','partial','pending'),
 quotes=[Q('IR','Balloux and Lehmann (2012) demonstrated that under the joint conditions of fluctuating demography and overlapping generations, conditions which are satisfied by every natural population of interest, k ≠ μ.','§6 The Irrelevance'),
   Q('BL','we show that the substitution rate at neutral genes does depend on population size fluctuations in the presence of overlapping generations','Abstract'),
   Q('BL','population size fluctuations do not affect substitution rates at neutral loci in a population with discrete nonoverlapping generations','Results, "Overlapping generations without fluctuating demography"')],
 formal='''Literature: B&L give k = μ(1 − s) for constant survival s (overlap alone, per time step; see quote below) and N-dependence only when overlap and fluctuation co-occur. Neither "0.743" nor "32.3" appears in the text.
Parameters: none in parameters.yaml; propose `new: demography.survival_s`, `new: demography.N_cycle`.

**Proposed check B3b (not yet run; pre-registered here):**
- Model: age-structured (Moran-type) population, survival s ∈ {0, 0.5, 0.9}, N(t) either constant, cyclic between N₁ and N₂ with period P, or monotone growth by a factor 3.3 over 3 generations (the RRME example), neutral alleles with infinite-sites mutation; run until the long-run substitution count is stable; report substitutions per time step, per average generation time, and per newborn.
- Predictions: (i) s = 0, any N(t): k = μ per generation (B&L, quoted); (ii) s > 0, N constant: k = μ(1 − s) per time step and k = μ per average generation time (Lehmann 2014 as paraphrased in Z18525262; that paper not retrieved); (iii) s > 0 with fluctuating N: k departs from (ii) by an amount set by the N(t) statistics (B&L). RRME predicts k/μ = 0.74 for non-overlapping growth, so (i) is a direct test of B3c.
- Would change the verdict: finding (i) violated (k ≠ μ for non-overlapping fluctuating N) supports Day; finding (iii) with a departure ≤ a few percent for human-like parameters means the effect cannot produce factors of 0.74 or 32.3.''',
 a_stated='Overlapping generations and fluctuating N are "satisfied by every natural population of interest".',a_impl='The B&L effect is large enough for humans to matter; the unit of time is calendar generations (Lehmann 2014 argues that in average-generation-time units k = μ).',
 against='Ledger: under non-overlapping generations fluctuations "do not affect substitution rates at neutral loci"; Lehmann (2014) as paraphrased by Day himself restores k = μ in average generation-time units.',support='B&L abstract confirms the existence of the effect.',
 weak='Day\'s own text calls Lehmann\'s redefinition "mathematically legitimate but biologically circular" without testing it; the corpus contains no independent simulation of B&L.',
 lit=[lit_row('Balloux & Lehmann 2012','"introducing overlapping generations reduces the substitution rate as fewer age class one individuals are produced per generation and therefore mutants."','verified-partial'),
      lit_row('Balloux & Lehmann 2012','"One of the central results of the Neutral Theory of evolution ... states that the rate k of allele substitution (rate of evolution) at neutral loci is unaffected by fluctuations in population size and is simply equal to the mutation rate."','the standard result B&L qualify')],
 p_claim='k/μ departs from 1 with a magnitude set by the demographic history.',p_opp='k = μ for non-overlapping generations; modest departure for overlap plus fluctuation; no departure of order 0.74 or 32 for humans.',
 p_change='See Formal statement (check B3b).',check='Script: proposed `research/checks/b3b_overlap_fluctuation.py` (not yet written) · Result: none. Queued in REVIEW.md "Queue".',
 sim=['survival s / age structure','N(t) schedule','time unit for k'])

add(id='B3c',slug='rrme-k-0743-mu',title='Real Rate of Molecular Evolution: k = mu × (sum N_i^2 / sum N_i) / N_t = 0.743 mu',side='day',branch='B',parent='B3',
 edges=[('supports','B3'),('depends-on','B3b')],lb=(False,'feeds the molecular-clock direction claim (dates older) that conflicts with B4'),
 sourcing='firsthand',status='extracted',v=('pending','partial','pending'),
 quotes=[Q('RRME','k = μ × 6.091/8.2 = 0.743μ (3)',file='day/zenodo-18525262.txt'),
   Q('RRME','k_{i} = M_{i} × 1/(2N_{t}) = 2N_{i}μ × 1/(2N_{t}) = μN_{i}/N_{t}',file='day/zenodo-18525262.txt',note='Eq. (1)'),
   Q('RRME','The 25.7% shortfall is not an approximation error or a boundary effect; it is the mathematical consequence of computing k from real population sizes rather than assuming constant N.',file='day/zenodo-18525262.txt')],
 formal='''k_t = (μ/N_t) · ΣN_i²/ΣN_i over contributing cohorts i; cohorts 1950–2025 at 25-year spacing: N = 2.5, 4.0, 6.1, 8.2 (billions); μ = 1.2e-8 (Kong 2012; `mutation.mu_per_site_per_gen.pedigree_human`).

**Arithmetic audit (derived, python3 -I):** ΣN² = 6.25 + 16.00 + 37.21 + 67.24 = 126.70 ✓; ΣN = 20.8 ✓; 126.70/20.8 = 6.0913; /8.2 = 0.7428 ✓. Column k_i/μ = 0.305, 0.488, 0.744, 1.000 ✓.
**Sensitivity (derived):** holding the paper's growth ratio (8.2/2.5)^(1/3) = 1.485 per cohort and extending the window: k/μ = 0.87 (2 cohorts), 0.78 (3), 0.72 (4), 0.65 (6), 0.61 (10), 0.60 (20). The number 0.743 is a property of the four-cohort window chosen, not of the population.
**Direction:** the paper states that divergence times "are longer than reported" (k < μ); Z18525547 (same week) concludes dates are 15–150× shorter (k > μ). Both can be true only for different N-histories; the corpus applies each to the same human lineage.''',
 a_stated='A mutation arising in cohort i exists as "one copy among 2N_{t} gene copies" in the current population, so its fixation probability is 1/(2N_t).',a_impl='Copy number of a new mutant does not grow with the population (in a growing Wright–Fisher population the mean offspring number exceeds 1, so the expected frequency of a neutral lineage stays 1/(2N_i)); census N_i of 25-year cohorts is the relevant N; Day describes the RRME as applying to overlapping generations while tabulating discrete 25-year cohorts.',
 against='Ledger: Balloux & Lehmann (verified-partial) have the effect only for overlap plus fluctuation; no 0.743 in their paper. Hössjer and McCarthy use k = μ.',support='Day: independent route to the B&L conclusion; arithmetic reproduces.',
 weak='B&L-style effects are a different mechanism from the cohort-dilution bookkeeping above; the corpus has no independent test of RRME (B3b would give one). Day\'s Z18637333 repeats 0.743 without new derivation.',
 lit=[lit_row('Balloux & Lehmann 2012','no 0.743; k = μ(1 − s) for constant survival s','verified-partial'),
      lit_row('Kong 2012','"with an average father\'s age of 29.7, the average de novo mutation rate is 1.20×10-8 per nucleotide per generation"','verified (μ input)')],
 p_claim='k/μ = 0.743 for the human population in 2025.',p_opp='A neutral lineage in a growing Wright–Fisher population has P_fix = 1/(2N_i), so the long-run rate stays μ; any transient is a lag (B1b), not a rate change.',
 p_change='B3b scenario (i): simulated k/μ ≠ 1 for non-overlapping growth would support RRME.',check='Script: proposed `research/checks/b3b_overlap_fluctuation.py`; arithmetic audit above computed with python3 -I. Related done check: B1b (growth gives a transient deficit that recovers).',
 sim=['cohort N series','window length','calendar generations vs average-generation-time units'])

add(id='B3d',slug='k-32-3-mu-and-factor-25',title='k = 32.3 mu (Bergeron pedigree rate vs Yoo required rate) and the median factor 25 across 55 vertebrates',side='day',branch='B',parent='B3',
 edges=[('supports','B3')],lb=(False,'cited as direct empirical falsification of k = μ after the N/Nₑ retraction, but no derivation is shown'),
 sourcing='firsthand',status='extracted',v=('pending','unverifiable','contested'),
 quotes=[Q('EDU','comparing Bergeron’s (2023) pedigree-measured mammalian mutation rate against the required substitution rate from Yoo et al. (2025) gives k = 32.3μ, not k = μ.',file='day/blog-2026-10-01-the-education-of-a-population-geneticist.txt'),
   Q('RET','The textbook k = μ identity is still falsified — both directly (pedigree μ and phylogenetic k disagree by a median factor of 25 across 55 vertebrates)',file='day/blog-2026-05-07-a-retraction-and-a-revision.txt')],
 formal='''No derivation appears in any harvested text (not in Zenodo; book not checked). Parameters: Bergeron 2023 mammal mean 7.97e-9 (`mutation.mu_per_site_per_gen`, main text; human value in SI Table 8, not retrieved); required rate from Yoo 2025 (not found in Yoo: 410 Mb or 187 Mb, fidelity ledger).

**Reconstruction attempts (derived, python3 -I):** brute force over required ∈ {17.5M, 20M, 35M, 40M, 187M, 205M, 410M}, generations ∈ {146,250 … 450,000}, L ∈ {2.9–6.4 Gb}, μ ∈ {7.97e-9 … 1.5e-8}, with and without halving: only four coincidental hits within ±0.15 of 32.3, all using non-natural input pairs (e.g. 410M, 325,000 gens, L = 3.0e9, μ = 1.3e-8). The closest natural reconstruction: 205M / 252,000 = 813.5 required fixations per generation; Bergeron mammal μ × 3.1e9 = 24.7 mutations per generation; ratio 32.9 (with L = 3.2e9: 31.9). **Implication:** the ratio uses the 205M count (bp/events issue, A3x); with the SNV-only 17.5M the same arithmetic gives 69.4/24.7 = 2.8; 205M/17.5M = 11.7 (the "11.7" bases-vs-events factor in the balance ledger).
The "median factor of 25 across 55 vertebrates" cites no source in the post; Bergeron 2023 reports "40-fold variation among species" in pedigree rates (a different quantity). Pedigree μ is per generation and phylogenetic k per year/per generation depends on generation-time assumptions.''',
 a_stated='Pedigree μ and phylogenetic (required) rate should coincide under k = μ.',a_impl='The "required substitution rate" is the observed difference count divided by T and L (it counts differences including polymorphism, structural variants and ancestral coalescence), compared with a per-site-per-generation pedigree μ.',
 against='Hancock and Nesslig20 compute the neutral count from pedigree μ and find agreement within a factor ~2 (B5c, B5e); Hancock\'s count reaches ≈19M vs 35M SNVs (B5c).',support='Keightley 2012: pedigree μ is "about twofold lower than estimates based on the human-chimp divergence"; keruru (KR-05): "closer to twice that".',
 weak='Hancock\'s comparison uses SNVs only and mixed haploid/diploid bases (B5c); neither side has isolated the effect of ancestral coalescence and calibration choice on the "twofold".',
 lit=[lit_row('Bergeron 2023','"The average pedigree-based mutation rates per generation for each species ... show 40-fold variation among species."','verified-accurate (ledger) for the 40-fold figure only'),
      lit_row('Yoo 2025','no 410 Mb or 187 Mb; SDR average 327 Mb per lineage','not-found (ledger)'),
      lit_row('Keightley 2012','"μ is about 1.1 × 10(-8), which is about twofold lower than estimates based on the human-chimp divergence"','verified-partial (abstract only)')],
 p_claim='k = 32.3μ.',p_opp='Using SNV-only fixed differences and ancestral-coalescence accounting, k/μ is of order 1–3, not 30.',
 p_change='Day supplying the derivation; or a reproduction using stated inputs. B4a will separate the ancestral-coalescence term.',
 check='Script: none; reconstruction search computed with python3 -I in this session (not committed).',sim=['required-rate basis (SNV | events | bp)','μ source (pedigree | phylogenetic)','L haploid'])

add(id='B3e',slug='corrected-calculation-8-25-fixations',title='Day (2026-02-04): "corrected" McCarthy calculation gives 8.25 fixations, shortfall 2,424,242x',side='day',branch='B',parent='B3',
 edges=[('attacks','B5a'),('depends-on','B3a'),('supersedes','B3a')] if False else [('attacks','B5a'),('depends-on','B3a')],lb=(False,'rebuttal of McCarthy using B3a; falls with B3a'),
 sourcing='firsthand',status='extracted',v=('non-sequitur','n/a','contradicted'),
 quotes=[Q('R2','Expected fixations: 132 billion × 1/16,000,000,000 = 8.25 fixations',file='day/blog-2026-02-04-response-to-dennis-mccarthy-round-2.txt'),
   Q('R2','Thus the shortfall increases from 133x to 2,424,242x when we go from the theoretical to the actual.',file='day/blog-2026-02-04-response-to-dennis-mccarthy-round-2.txt')],
 formal='''Inputs in the post: Nₑ = 3,300 ("actual ancient effective population size"), N = 8×10⁹, 100 mutations per individual, 400,000 generations, P_fix = 1/2N = 1/(1.6×10¹⁰).

**Arithmetic audit (derived, python3 -I):** 100 × 3,300 = 330,000 per generation ✓; × 400,000 = 1.32×10¹¹ ✓; × 1/1.6×10¹⁰ = 8.25 ✓; 20×10⁶/8.25 = 2,424,242 ✓; 20×10⁶/150,000 = 133.3 ✓.
**Direction check:** the result uses supply ∝ Nₑ and fixation probability ∝ 1/N, i.e. k/μ = Nₑ/N = 4.1×10⁻⁷. The same post's equation is k = μ(N/Nₑ) (B3a), which with the stated N and Nₑ gives k/μ = 2.4×10⁶ (supply from census 8×10⁹, fixation 1/(2Nₑ)); applying that to McCarthy's 20M would give a count ≫ 20M, not 8.25. So the figure does not follow from the post's own equation.
Other items: the "150,000 fixed differences" for McCarthy's model from P(unchanged) = exp(−2NₑμT) is not reproduced by the stated formula (exp(−3×10⁻⁴ × 4×10⁵) = e⁻¹²⁰); N = 8×10⁹ is applied to all 400,000 generations although census-scale N spans a few hundred; Nₑ = 3,300 is a drift-variance estimate from aDNA (branch C; Day later calls Nₑ ≈ 10⁴ circular, B3h).''',
 a_stated='Supply from 100 × Nₑ individuals; fixation probability 1/(2N) with current N.',a_impl='Current census applies to all generations; Nₑ = 3,300 is independent of the clock.',
 against=rq('MC1','450 billion x 1/20,000 = 22.5 million fixed mutations.',loc='para 52 (McCarthy)'),support='Day\'s reproduction of McCarthy\'s 20M under McCarthy\'s inputs is arithmetically correct (400e9/20,000 = 20M).',
 weak='McCarthy uses N = Nₑ = 10,000 and treats all mutations as neutral (B5a). The sign problem above is on Day\'s side.',
 lit=[],p_claim='8.25 expected fixations.',p_opp='With P_fix = 1/(2N) and supply ∝ N: k = μ, 20M-scale counts.',
 p_change='n/a (arithmetic and direction audit).',check='Script: none. Audit computed with python3 -I in this session. Superseded in principle by Day\'s own 2026-08-27 concession (B3g).',
 sim=['supply N','fixation-probability N','window length'])

add(id='B3f',slug='800000-mu-grok-exchange',title='k = 800,000 mu from N = 8e9 and Ne = 1e4 (Day-Grok exchange, 2026-04-30)',side='day',branch='B',parent='B3',
 edges=[('supports','B3a')],lb=(False,'illustrative arithmetic from stipulated premises; withdrawn with B3a'),
 sourcing='secondhand',status='extracted',v=('holds','n/a','contradicted'),
 quotes=[Q('CONC','This equals 800,000 μ, not μ.',file='day/blog-2026-04-30-conceding-the-math.txt',sh='text produced by the AI system Grok, posted by Day; the premises were stipulated by Day\'s prompt'),
   Q('CONC','The cancellation requires N = N_e, which I have already conceded does not hold in real populations.',file='day/blog-2026-04-30-conceding-the-math.txt',sh='Grok, as posted by Day')],
 formal='''k = (2Nμ)/(2Nₑ) with N = 8×10⁹, Nₑ = 10⁴ ⇒ 8×10⁵ μ (derived: 8e9/1e4 = 800,000 ✓). The computation is conditional on two propositions: supply uses census N, and fixation probability uses Nₑ, which the same post says the AI conceded. Not independent evidence for either premise.''',
 a_stated='Two conceded propositions (supply = census N; fixation probability = Nₑ).',a_impl='The AI\'s earlier statements reflect knowledge, not agreement; the exchange is a leading chain.',
 against='keruru and Day (B3g) later agree P_fix = 1/(2N).',support='Arithmetic only.',weak='An LLM transcript is not a literature source.',
 lit=[],p_claim='k/μ = 800,000.',p_opp='k/μ = 1 (B3a).',p_change='B3a.',check='Script: none. Arithmetic computed in python3 -I.',sim=['N/Nₑ ratio'])

add(id='B3g',slug='day-concession-no-ne-in-kimura-identity',title='Day (2026-08-27): Kimura\'s derivation never needed Ne; supply is 2N mu and fixation 1/(2N)',side='day',branch='B',parent='B3',
 edges=[('supersedes','B3a'),('revises','B3'),('revises','B4')],lb=(True,'removes the N/Nₑ mechanism behind the 15–150× recalibration and the 800,000μ figures'),
 sourcing='firsthand',status='reviewed',v=('holds','accurate','supported'),
 quotes=[Q('RESP','the derivation of Kimura’s substitution identity never needed Nₑ on either side of the algebraic equation. Supply is 2Nμ in the census N, the fixation probability of a new copy is 1/(2N) in the same N, the two correctly cancel',file='day/blog-2026-08-27-the-response-to-the-retraction.txt'),
   Q('RESP','this error means that it will be necessary to produce a 3rd Edition of Probability Zero to correct my mistake in this regard.',file='day/blog-2026-08-27-the-response-to-the-retraction.txt')],
 formal='''Retraction of B3a by its author, 2026-08-27 (one day after keruru\'s post, 2026-08-26). It leaves in place: k = μ at steady state (HL "accepts it throughout"), the transit-time/fill-state argument (B1, B2), Balloux–Lehmann (B3b) and the 32.3 comparison (B3d, posted 2026-10-01).
Not revised on the harvested Zenodo records: Z18429937, Z18525547, Z18637333 (no new version seen, 2026-10-07). Version-ledger entry proposed: B3 N/Nₑ leg, asserted 2026-01-29 to 2026-04-30, withdrawn 2026-08-27 (blog); Zenodo texts unchanged.
Day also argues in the same post that census-based supply is about 330,000 times larger than a Nₑ = 10⁴ supply (derived check: Kong (1.2e-8 × 3.1e9 ≈ 37) × 2 × 10⁴ = 7.4×10⁵ ✓ ("740,000"); 2.5×10¹¹/7.4×10⁵ = 3.4×10⁵ ✓, i.e. about 330,000 as stated).''',
 a_stated='Census N in both supply and fixation probability.',a_impl='Textbook notation using Nₑ on the supply side was careless, not a hidden move (Day).',
 against='n/a (a concession).',support=rq('KRE','The claim about the substitution rate is withdrawn. The claim about the ancient-DNA finding is withdrawn.',loc='para 36 (keruru)'),
 weak='The concession coexists with continued use of the 0.743μ and 32.3μ figures and with Nₑ-based recalibrations in unrevised Zenodo records; Day also contests the second half of keruru\'s retraction (aDNA; B3h).',
 lit=[lit_row('Kimura 1962; Kimura & Ohta 1969','1/2N (reproducing individuals)','see B7a, B7b')],
 p_claim='(none; retraction)',p_opp='(none)',p_change='A revised Zenodo version or the 3rd edition text would show which dependent claims are withdrawn.',check='Script: none. Related: B3a check.',sim=['—'])

add(id='B3h',slug='ne-10000-presupposes-k-mu',title='Ne ≈ 10,000 is derived from theta = 4 Ne mu, which "presupposes k = mu"',side='day',branch='B',parent='B3',
 edges=[('attacks','B7c')],lb=(False,'blocks critics\' use of Nₑ ≈ 10⁴ (keruru\'s 10⁻²⁹, Mansfield\'s inputs); not a step in MITTENS counts'),
 sourcing='firsthand',status='extracted',v=('pending','n/a','contested'),
 quotes=[Q('RESP','The arithmetic holds given one number: Nₑ ≈ 10,000 — which comes from θ = 4Nₑμ, which presupposes k = μ, the identity under test.',file='day/blog-2026-08-27-the-response-to-the-retraction.txt'),
   Q('NNE','The standard N₂ ≈ 10,000 is itself problematic, as it is derived from genetic diversity via θ = 4N₂μ — a formula that presupposes k = μ.',file='day/zenodo-18525547.txt')],
 formal='''Nₑ(coalescent) = π/(4μ) from observed diversity π and a per-generation μ. Whether this "presupposes k = μ" depends on how μ was obtained: a pedigree μ (Kong 2012, Keightley 2012) is measured directly; a phylogenetic μ (divergence ÷ dated split) does use k = μ. IR §5 itself says μ "was initially estimated phylogenetically" and was later replaced by the pedigree estimate.
**Internal tension:** Z22129121 states "The equilibrium heterozygosity relation θ = 4Nₑμ is untouched." (same author, 2026-08-27).''',
 a_stated='The Nₑ ≈ 10⁴ input to keruru\'s calculation is circular.',a_impl='μ in θ = 4Nₑμ is a clock-calibrated rate.',
 against='Pedigree μ is independent of divergence dating (Keightley 2012).',support='Day: Charlesworth (2009) flagged the circularity (not retrieved).',weak='Day cites Charlesworth 2009 without a quote in the corpus; keruru "had no answer" per Day via keruru (secondhand, B7c).',
 lit=[lit_row('Keightley 2012','μ ≈ 1.1×10⁻⁸ from sequencing relatives','verified-partial (abstract)')],
 p_claim='Nₑ from diversity inherits any clock error in μ.',p_opp='With pedigree μ, Nₑ (diversity) contains no divergence data.',p_change='Showing that a given Nₑ estimate used a phylogenetic μ.',
 check='Script: none.',sim=['μ source (pedigree | phylogenetic)','Nₑ source (diversity | drift variance | PSMC)'])

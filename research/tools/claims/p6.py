from gen import *
Z3='[MITTENS 3.0, Zenodo 23003785](https://zenodo.org/records/23003785) (key Z23003785), 2026-09-28 (modified 2026-10-04)'
ZB='[The Bernoulli Barrier, Zenodo 18167588](https://zenodo.org/records/18167588) (key Z18167588), pub. 2026-01-04 (modified 2026-01-07)'
Z25='[MITTENS 2025, Zenodo 18165980](https://zenodo.org/records/18165980) (key Z18165980), pub. 2025-12-28 (modified 2026-01-06)'
NSL='[They Never Stop Lying](https://voxday.net/2026/10/01/they-never-stop-lying/) (key B2026-10-01-they-never-stop-lying), blog, 2026-10-01'
SNK='[Snikker-Snak](https://voxday.net/2026/10/01/snikker-snak/) (key B2026-10-01-snikker-snak), blog, 2026-10-01'
IC='[An Inspiring Critique](https://voxday.net/2026/01/27/an-inspiring-critique/) (key B2026-01-27-an-inspiring-critique), blog, 2026-01-27'
EDU='[The Education of a Population Geneticist](https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/) (key B2026-10-01-the-education-of-a-population-geneticist), blog, 2026-10-01'

claim('A5g','mutation-supply-irrelevant-reply','Day: the E. coli study is cited for its fixation rate, not its mutation rate; no human or mammalian fixation has been observed faster than 1,600 generations','day','A','A5',
 [('attacks','A5')],False,'firsthand','checked',('pending','n/a','pending'),
 q('I didn’t cite the E. coli study for its mutation rate but for its fixation rate: 25 mutations fixed in 40,000 generations, yielding an average of 1,600 generations per fixed mutation.',IC+', ¶22.')+'\n'+
 q('No one has ever observed any human or even mammalian fixation faster than 1,600 generations.',IC+', ¶23.'),
 '''Claim (two parts): (i) G_f is an observed fixation rate and need not be scaled by μ; (ii) no mammalian fixation faster than 1,600 generations has been observed. Part (ii) is an observational-absence claim: 1,600 generations at 25 y is 40,000 years, longer than the observation window for any directly observed human allele-frequency change; `derived:` 1,600 x 25 = 40,000 y. It cannot distinguish a slow rate from lack of observation time.
Day\'s example in the same post: CCR5-delta32 "the fastest we could get, in theory, is 2,278 generations" and a further 37,800 generations by drift (not checked here).
Tension with the Day corpus: Z23003785 s4.3 uses the mutation supply (4.1e-4 per genome per generation) to separate neutral hitchhikers from sweeps (A2f, A5c): the LTEE count is partly a function of μ.''',
 '- Stated: fixation rate is the measured quantity; mutation supply is not what limits it.\n- Implicit: the response of fixation rate to μ is nil or small (A5d); the observed mammalian record is informative.',
 '''- Against: A5, A5a, A5b, A5c all argue the rate depends on supply; A5d\'s own data show a positive response; Tenaillon (6 mutator populations carry 96.5% of point mutations) shows that supply and fixation counts are linked in the LTEE.
- In support: Camestros (CA-10): the number was intended as an average, not a time for an individual chromosome. Sublinear scaling (A5d).
- Weaknesses in the responses: the critics do not show an observed mammalian fixation faster than 1,600 generations either; the repo has no mammalian fixation data. Day\'s observational-absence claim is unfalsifiable on human timescales.''',
 LITH+'''| Tenaillon 2016 | six populations carry 96.5% of point mutations through hypermutability | verified |''',
 NOLIT.replace('| (none cited in the claim) | n/a | n/a |','| (none) | | |') and 'Not run. Prediction (Day): the response of fixation rate to supply is small. Prediction (critics): it is large with recombination. Covered by A-sim (file A) and by the exponent in A5b.',
 'No script. Review: pending.', '- Supply–rate relation as a user-chosen function (see A5b).')

# ---------------- G branch ----------------
claim('G','bernoulli-barrier','Bernoulli Barrier: parallel fixation of many loci is limited because the Law of Large Numbers compresses fitness variance (14.7x available vs 1,570x required)','day','G','ROOT',
 [('supports','ROOT'),('depends-on','Ga'),('depends-on','Gb'),('depends-on','Gc'),('depends-on','Gd')],False,'firsthand','checked',('arithmetic-error','partial','pending'),
 q('the fitness differential between the "best" and "worst" genotypes in a population of 10,000 is only 14.7×—while the required differential is 1,570×, a shortfall exceeding 100-fold.',ZB+', ¶6 (abstract).'),
 '''n = 157,000 loci at p = 0.5, N = 10,000, s = 0.01 per locus (uniform).
Count per individual ~ Binomial(n, 0.5): mean 78,500, SD √(n·p·(1−p)) = 198.1, CV = 0.252%  (paper: 198.1, 0.25%).
Extreme genotypes in N = 10,000 (normal order statistics): ±3.72σ → 79,237 / 77,763, difference 1,474 = 7.44σ.   Paper: "Fitness ratio = (1.01)¹⁴⁷⁴ ≈ 14.7×". Required: "157,000 × 0.01 = 1,570×". Shortfall = 1,570/14.7 ≈ 107×.

`derived:` (python3 -I) The binomial and order-statistic numbers reconcile. The fitness numbers do not as stated: (1.01)^1,474 = 2.34e6 (e^14.67), not 14.7. The value 14.7 equals 1,474 x 0.01 = 14.74, an additive quantity; likewise 1,570 = 157,000 x 0.01 is additive, whereas the multiplicative counterpart is 1.01^157,000 = 10^678. The ratio of the two additive increments (1,570/14.74 = 106.5; 106.8 with 14.7) reproduces "107". So the paper labels additive fitness differences as multiplicative "ratios", and the stated multiplicative formula (stated as conservative for epistasis in s3.1) gives 2.3e6 vs 10^678 instead. In both readings the conclusion direction is the same; the magnitude of the "shortfall" differs from 107 by hundreds of orders of magnitude in the multiplicative reading.
Further `derived:` Absolute variance of the allele count grows with n (n/4 = 39,250); only the coefficient of variation (SD/mean) falls as 1/√n. The text of s7.6 says "fitness variance decreases as the number of segregating loci increases", and s7.10 itself states "the variance in total beneficial allele count is 250, but the mean is 500" for 1,000 loci. The claim is true for relative dispersion, not for absolute variance.''',
 '''- Stated: free recombination; unlinked loci; multiplicative fitness (s3.1); selection requires a fitness differential between extreme genotypes that exceeds the summed per-locus advantage (s3.2); Fisher: response proportional to variance (s7.6); each locus responds to its own s (s7.10) but through differential reproduction of whole organisms.
- Implicit: the "required differential" is the full all-beneficial vs none genotype (n·s), though no derivation shows a sweep at one locus requires it; all 157,000 loci are simultaneously at p = 0.5, which the same paper (s7.8) says does not happen (the active zone holds ~230); the 157,000 figure is not the 20M or 205M used in the other papers.''',
 '''- Against: Myers (PZ-01), Hancock (GG-01), Bowers (BO-02) and r/DebateEvolution (RE-01) argue parallel action is how evolution works; none engaged the Bernoulli arithmetic specifically (no numbers in PZ-01, BO-02; BO-04 verifies Bowers gave no calculations). Reddit commenter (post 1wv4zeg) describes the Barrier as an idea Day is "particularly proud of"; no calculation. KITTENS §11: "Version 3.0 says the “Bernoulli Barrier” is moot" (this is Day\'s blog statement, Ge, not wording found in the 3.0 text).
- In support: Day (blog 2026-10-01): the Barrier "remain[s] entirely correct"; Samson (ally) asks "where does something like the Bernoulli Barrier fall?" (rhetorical).
- Weaknesses in the responses: no critic in the corpus has checked the order-statistic arithmetic or the 14.7 vs 2.34e6 inconsistency; Day has not addressed the units issue. Neither side has run a simulation.''',
 LITH+'''| Kimura 1962 (escape probability ≈ 2s) | "the probability of ultimate survival of an advantageous mutant gene is approximately twice the selection coefficient" | verified-accurate |
| Fisher 1930 (response ∝ variance) | not retrieved | unverified |
| Pritchard et al. 2010 ("have not fixed at any locus") | not retrieved | unverified |
| Wei & Zhang 2019 (epistasis at genomic scale) | not retrieved | unverified |
| Hill & Robertson 1966; Hartfield & Bataillon 2020 | not retrieved | unverified |''',
 '''No check has run. Proposed check G-sim (not run, long): Wright-Fisher, N = 1e3–1e4 (scaled), n unlinked loci with new beneficial mutations of s = 0.01 arising at constant rate; free recombination; hard vs soft (competitive) selection; record per-locus fixation probability, sweep time, and fixations per generation as the number of simultaneously active loci rises from 1 to ~500.
- Under Day: per-locus fixation probability and rate collapse beyond the pipeline cap (14 by the paper\'s criterion as derived in Gc; 230 as stated).
- Under critics: per-locus values stay near single-locus Kimura values (2s, (2/s)ln(2N)) until reproductive-capacity limits (cost of selection, branch H) bind.
- Result that would change a verdict: per-locus fixation probability dropping to <50% of 2s at n_active ≈ 230 under free recombination with soft selection (supports Day); no drop to n_active ≈ 500 (contradicts).''',
 'Arithmetic audit (python3 -I, scratch): the 14.7× formula does not reproduce as stated. Review: pending.',
 '- n_active loci, s per locus, N, fitness model (additive/multiplicative), hard vs soft selection, recombination. Outputs: per-locus P_fix, sweep time, throughput.')

claim('Ga','p-to-the-n-0p02','P(all) = p^n: 0.02^20,000,000 ≈ 10^−34,000,000 for 20 million fixations at p = 0.02','day','G','G',
 [('depends-on','G3')],False,'firsthand','checked',('holds','accurate','contested'),
 q('For n = 20,000,000 fixations (human-chimp divergence, human lineage) and p = 0.02: P(all) ≈ 0.02^20,000,000 ≈ 10^−34,000,000',Z25+', ¶24 (Results).'),
 '''P(all) = p^n with n = `divergence.required_fixations.day_2025` = 2.0e7 and p = 0.02.
`derived:` log10(0.02^(2e7)) = 2e7 x (−1.69897) = −33,979,400 → 10^−33,979,400, which rounds to the stated 10^−34,000,000 (0.06% difference in the exponent). The value p = 0.02 = 2s for s = 0.01 (Kimura 1962, "approximately twice the selection coefficient"; used as P_escape in Z18167588 s7.9). Pass-1 attributed this number to Z18167588; it is in Z18165980. Z18167588 uses n = 157,000, p = 0.5 (Gb).
Compare Darwillion (McCarthy\'s rendering, G4): (1/20,000)^(2e7) = 10^−86,020,600. The two use different p (0.02 vs 5e-5).''',
 '- Stated: independence of the n fixation events; each has probability p; "simultaneous success".\n- Implicit: the n events are a pre-specified set (G3); p is the per-new-mutation fixation probability for a beneficial mutation, whereas the n loci being fixed are not mutations that all must arise at a given time.',
 '''- Against: McCarthy (G3): a specific set; the probability of any 20M is near 1 given the supply. Camestros (G3a): lottery analogy.
- In support: Day (G3b): either specific fixations matter (Darwillion applies) or they are interchangeable neutral noise.
- Weaknesses in the responses: the critics\' "any 20M" estimate uses neutral k = μ (B-branch) which Day disputes; Day\'s dilemma does not address selection acting on many possible beneficial sites.''',
 LITH+'''| Kimura 1962 | "approximately twice the selection coefficient" | verified-accurate |''',
 'Covered in G3 (specific-vs-any) and G-sim. Result recorded above.', 'Arithmetic audit (python3 -I, scratch). Review: pending.', '- None directly.')

claim('Gb','half-to-157000','P(all beneficial) = 0.5^157,000 = 10^−47,262 and the population size required to find one such individual','day','G','G',
 [('depends-on','G')],False,'firsthand','checked',('holds','n/a','contested'),
 q('P(all beneficial) = (0.5)¹⁵⁷\'⁰⁰⁰ = 10⁻⁴⁷\'²⁶²',ZB+', ¶45 (s4.1). The apostrophes are the thousands separators in the source.'),
 '''log10(0.5^157,000) = 157,000 x (−0.30103) = −47,261.7 → 10^−47,262 (reconciles). N_required = 10^47,262 individuals (s4.2).
Relevance: the probability that an individual carries all 157,000 beneficial alleles when each is at p = 0.5. The paper also says (s7.10) "Each locus … experiences its selection coefficient s and responds accordingly. The Bernoulli Barrier does not deny this." so the existence of an all-beneficial genotype is not needed for per-locus sweeps; the number illustrates the compression of variance (s4) rather than a requirement.''',
 '- Stated: p = 0.5 at every locus; independence; n = 157,000.\n- Implicit: all loci are simultaneously intermediate (not so, s7.8); the extreme genotype is the target.',
 '''- Against: critics did not engage this number. The specific-vs-any objection (G3) applies in the same way: the probability that a *particular* genotype exists is not the probability that selection acts.
- In support: Day (blog 2026-10-01 ¶26) maintains correctness.
- Weaknesses in the responses: no critic has addressed s7.10 (per-locus response); Day\'s s7.10 qualifies the use of this number.''',
 NOLIT, 'Arithmetic only.', 'Arithmetic audit (python3 -I, scratch). Review: pending.', '- None directly.')

claim('Gc','pipeline-cap-230-sweeps','The active zone limits the pipeline to about 230 simultaneous sweeps, so about 157,000 fixations can occur in 300,000 generations','day','G','G',
 [('depends-on','G')],False,'firsthand','checked',('non-sequitur','n/a','pending'),
 q('the "active zone" of intermediate-frequency alleles imposes a hard limit on pipeline capacity of approximately 230 simultaneous sweeps.',ZB+', ¶6 (abstract).')+'\n'+
 q('Working backward from the constraint, the active zone can sustain approximately 200–300 simultaneous sweeps before the Bernoulli Barrier compresses variance below the threshold required for effective selection.',ZB+', ¶111 (s7.8).')+'\n'+
 q('Maximum fixations ≈ (300,000 / 440) × 230 ≈ 157,000 This appears to match the requirement for human-chimpanzee divergence.',ZB+', ¶63 (s7.8).'),
 '''t_transit = (2/s)·ln 9 = 200 x 2.197 = 439.4 ≈ 440 generations (s = 0.01, 0.1 < p < 0.9); fixations ≤ (T/t_transit)·C with C = 230, T = 300,000.
`derived:` (python3 -I) 300,000/440 = 681.8; x 230 = 156,818 ≈ 157,000 (reconciles). The cap C is not derived: "working backward from the constraint" gives "200–300"; the cap that makes the product equal the paper\'s own n = 157,000 is 230, which is the same number that is then said to "appear to match the requirement". The requirement used elsewhere in the corpus is 20M (Z18165980) or 205M (Z23003785): 20e6/157,000 = 127; 205e6/157,000 = 1,306. The paper\'s own criterion (available additive differential 2z·√(n/4)·s ≥ required n·s, with z = 3.72 for N = 10,000) gives n ≤ z² = 13.8, not 230 (derived by this audit; applies the paper\'s s3 comparison to n loci). The paper\'s separate "reproductive ceiling" (s6.1: Σs ≤ 1.0–2.0) gives 100–200 loci at s = 0.01, which is closer to 230 but is a different constraint (branch H).''',
 '- Stated: the constraint acts on loci with 0.1 < p < 0.9; each locus spends t_transit there; pipeline runs full and continuously (s7.9 says this is idealised).\n- Implicit: the same threshold applies at every n; s = 0.01 uniform; free recombination.',
 '''- Against: none in corpus directly. Hancock\'s statement (GG-13, G2c) is about a strictly serial model, not this one.
- In support: none; the paper itself flags (s7.9) that the idealised 157,000 cannot be achieved because of the drift input constraint.
- Weaknesses in the responses: no critic has asked for the derivation of 230. The conclusion that 157,000 "match[es]" the requirement is at odds with the MITTENS requirement of 20M–205M, which makes the pipeline cap about 127x–1,300x too small by the paper\'s own numbers (so the Barrier would be a stronger constraint than the text says, not a weaker one).''',
 NOLIT,
 'See G (G-sim). Prediction specific to this claim: the simulated fixation rate as a function of simultaneously active loci saturates; the saturation level is the quantity C. Under the paper\'s own s3 criterion C ≈ 14. Under critics: no saturation below the reproductive-capacity limit.',
 'Arithmetic audit (python3 -I, scratch). Review: pending.', '- Pipeline capacity C as a measured output of G-sim; t_transit.')

claim('Gd','drift-input-constraint','Only 2% of beneficial mutations escape drift, so sustaining the pipeline requires about 7.8 million beneficial mutations to arise','day','G','G',
 [('depends-on','Gc')],False,'firsthand','checked',('holds','accurate','pending'),
 q('Required input ≈ 230 / 0.02 ≈ 11,500 beneficial mutations per transit period',ZB+', s7.9. The paper then computes "Total required input ≈ (300,000 / 440) × 11,500 ≈ 7.8 million beneficial mutations".'),
 '''P_escape = 2s = 0.02 (Kimura 1962). Required input per transit period = C/P_escape = 230/0.02 = 11,500; total = (300,000/440) x 11,500 = 7.84e6 (reconciles).
`derived:` population-level supply of new mutations (Day\'s N = 10,000; Kong rate 1.2e-8): 77 diploid per individual per generation x 10,000 = 7.7e5 per generation, 2.3e11 over 300,000 generations (McCarthy\'s version, MC-03: 50,000 per year x 9e6 y = 4.5e11 with Day\'s inputs). The 7.8e6 beneficial arisings needed would then be 3.4e-5 of all new mutations (python3 -I). Whether the beneficial fraction is that large is the open question, which the paper itself calls "an empirical question".''',
 '- Stated: Kimura\'s 2s for each beneficial mutation; drift loss and the Barrier are independent constraints.\n- Implicit: all required fixations are beneficial (not neutral); s = 0.01 for all.',
 '''- Against: McCarthy (MC-10): "only 3% of new mutations are deleterious" (uncited); critics\' neutral model needs no beneficial mutations (B-branch).
- In support: the arithmetic and Kimura 2s are accurate.
- Weaknesses in the responses: MC-10 is uncited; Day does not quantify the beneficial fraction either.''',
 LITH+'''| Kimura 1962 | "approximately twice the selection coefficient" | verified-accurate |''',
 'Arithmetic only; supply fraction computed above. Prediction (critics): the beneficial supply needed (3.4e-5 of new mutations) is within any plausible beneficial fraction. Not tested.',
 'Arithmetic audit (python3 -I, scratch). Review: pending.', '- Beneficial-mutation fraction and s distribution as inputs.')

claim('Ge','bb-omitted-from-3-0','Day: MITTENS 3.0 omits the Bernoulli Barrier and the Averaging Problem as moot, but both "remain entirely correct"','day','G','G',
 [('revises','G'),('supersedes','G')],False,'firsthand','checked',('pending','n/a','pending'),
 q('Anyhow, the MITTENS 3.0 paper [URL: https://zenodo.org/records/23003785] renders those complicating elements moot to such an extent that I omitted both the Bernoulli Barrier and the Averaging Problem, even though both of them remain entirely correct.',NSL+', ¶26.'),
 '''Version note: MITTENS 2025 (Z18165980) included p^n = 0.02^(2e7); the 3.0 paper (Z23003785) contains "Bernoulli Barrier" only in a rhetorical sentence in s1 ("When the Bernoulli Barrier demonstrates that parallel fixation is probabilistically self-defeating, the defender invokes neutral drift"). In the same post (¶22) Day says: "neither the Bernoulli Barrier nor the Hard Limit on neutral drift apply to the LTEE experiment because a) the math is an average of 12 different populations and b) there is no time for neutral drift to have occured yet in the 85,000-generation time limit of the LTEE." and ¶24 quotes a passage (stated to be from Appendix A of the book) "Therefore fixation must be sequential." (see G2g).''',
 '- Stated: the 3.0 numbers incorporate parallel fixation, so BB is not needed there.\n- Implicit: BB applies to real species but not to the LTEE.',
 '''- Against: KITTENS §11 says "Version 3.0 says the “Bernoulli Barrier” is moot, but §5.1 still appeals to the finite carrying capacity of the selective environment, which needs the same qualifications." The wording "moot" appears in Day\'s blog, not in the 3.0 text; the substantive point (§5.1 carries a related limit) is a critic\'s observation.
- In support: none beyond Day.
- Weaknesses in the responses: if BB does not apply to the LTEE but does apply to humans, the LTEE rate is not a like-for-like measure of what parallelism achieves in a recombining species; the text does not say whether BB can only lower the human rate. Day uses BB to rule out parallel fixation "a priori" while G1 argues parallelism is included in G_f; see G2g for the resulting tension.''',
 NOLIT, 'Not testable; consistency note.', 'No script.', '- None.')

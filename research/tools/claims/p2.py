from gen import *
Z3='[MITTENS 3.0, Zenodo 23003785](https://zenodo.org/records/23003785) (key Z23003785), 2026-09-28 (modified 2026-10-04)'
Z5='[LTEE fixation data paper, Zenodo 23105291](https://zenodo.org/records/23105291) (key Z23105291), 2026-10-02'

claim('A2','ltee-gf','G_f from the LTEE: 1,322 generations per fixation (non-mutators, 60,000 generations)','day','A','A',
 [('supports','A'),('depends-on','A2a'),('depends-on','A2g')],False,'firsthand','checked',('holds','unverifiable','contested'),
 q('The result for non-mutator populations is 1,322 generations per fixation at 60,000 generations — cross- validated at 893 generations per fixation by clone-pair analysis at 50,000 generations.',Z3+', p.1 (abstract). PDF hyphenation "cross- validated" preserved.'),
 '''G_f = (generations in window) / (fixations in window) = 60,000 / 45.4 = 1,321.6   (`ltee.gens_per_fixation.day_mittens3_nonmutator`)

`derived:` G_f across versions (all recomputed, python3 -I):

| Version | G_f | Basis | Reconciles? |
|---|---|---|---|
| 2019 (B2019-02-07) and 2025 (Z18165980, Z18168236) | 1,600 | 25 mutations / ~40,000 gens (40,000/25 = 1,600) | Yes (arithmetic). Citation differs: "NATURE, 2009" (2019) vs Good et al. 2017 (2025); see A2a. |
| Book (per Z23003785 s3.3) | 1,400 | "taken from Good et al.’s published summary" | not derivable here |
| 3.0 clone-pair (50,000 gens) | 893 | 50,000 / 56.0 = 892.9 | Yes |
| 3.0 metagenomic (60,000 gens) | 1,322 | 60,000 / 45.4 = 1,321.6 | Yes |
| Z23105291 strict | 1,587 | 60,000 / 37.8 (189 fixations over 5 populations, 189/5 = 37.8) | Yes (derived in `parameters.yaml`) |
| Ara+2 | 909 or 917 | 60,000/66 = 909.1 (blog) vs 60,500/66 = 916.7 (Table 1) | Yes; the inputs differ by 500 gens |

The headline changed from 1,600 to 1,322 to 1,587 within nine months; the direction of the later correction (1,587) increases the shortfall by 1,587/1,322 = 1.20x.''',
 '''- Stated: LTEE non-mutator populations are the measuring instrument; the count is "all-cause" fixations (beneficial plus hitchhikers plus everything else); the rate already includes parallelism (G1).
- Implicit: the count is not sensitive to the fixation-calling rule (but see A2b), and 60,000 generations is a stationary window (Day's own s4 text says "The rate is slowing." after the per-milestone table).''',
 '''- Against: Camestros (CA-07): "Day simply has not shown that. He has one estimate for his Gf term that he claims, without demonstrating it, to be a particularly fast fixation rate." See A2d. Dumb-and-Dumber (RE-03, RE-04): estimator problems (A2c). Scaling to humans (A5 family).
- In support: Camestros (CA-10) concedes it is an average. Tenaillon 2016 independently reports constant-rate accumulation of neutral mutations in non-mutator lines (A2g).
- Weaknesses in the responses: critic arguments on the estimator target the clone-pair and the mutator-corrected columns more than the non-mutator metagenomic headline; no critic recomputed 45.4. On Day's side, three different counting rules are in use within one week of publication (A2b).''',
 LITH+'''| Good et al. 2017 | "molecular evolution continues to be characterized by signatures of rapid adaptation, with multiple beneficial variants simultaneously competing for dominance in each population"; the "≥95%" rule is not in the main text | unverified (SI not retrieved) |
| Tenaillon et al. 2016 | "neutral mutations accumulate at a constant rate" in populations that kept the ancestral mutation rate | verified |
| Barrick et al. 2009 | "genomic evolution was nearly constant for 20,000 generations" | verified (abstract only) |''',
 '''No check has run. Component of the pre-registration: the metagenomic count depends on a calling rule; the lineage-aware count in Z23105291 is the stricter alternative.
- Under the claimant's model: G_f is stable (1,300–1,600) across counting rules and windows.
- Under the opposing model: G_f depends on the rule (1,322 vs 1,587, A2b) and on estimator artefacts (A2c) at the 20–50% level, which is immaterial next to a million-fold shortfall; the dispute is therefore about transfer (A5), not the measurement.
- Result that would change a verdict: a recount from the raw Good 2017 data giving G_f outside 900–2,500 for non-mutators.''',
 'Arithmetic audit (python3 -I, scratch) reconciles every G_f row. No recount from raw LTEE data has been run. Review: pending.',
 '- LTEE preset library: G_f by population and counting rule (≥95% pooled vs lineage-aware), mutator flag, window length.')

claim('A2a','gf-datum-source-2019','The 1,600 datum: 25 fixed mutations in ~40,000 LTEE generations (cited to Nature 2009, later to Good 2017)','day','A','A2',
 [('depends-on','A2')],False,'firsthand','checked',('holds','unverifiable','pending'),
 q('Source: Sequencing of 19 whole genomes detected 25 mutations that were fixed in the 40,000 generations of the experiment. NATURE, 2009',
   '[Maximal Mutations](https://voxday.net/2019/02/07/maximal-mutations/) (key B2019-02-07), blog, 2019-02-07, ¶9.')+'\n'+
 q('Sequencing detected 25 mutations that were fixed over approximately 40,000 bacterial generations, yielding an average of 1,600 generations per fixed mutation.',
   '[Zenodo 18168236](https://zenodo.org/records/18168236) (key Z18168236), 2026-01-05, ¶29. This paper cites Good et al. 2017.'),
 '''G_f = 40,000 / 25 = 1,600  (`ltee.gens_per_fixation.day_2019`). `derived:` 40,000/25 = 1,600 exactly.

Citation drift: 2019 post "NATURE, 2009"; 2025 papers "Good et al. 2017" (60,000 generations); Z18168236 also says "reported in Nature in 2017". Barrick et al. 2009 (Nature) reports genomes at 20,000 generations (abstract in repo). Camestros (CA-06) reads the same literature as 35 mutations by 15,000 generations, i.e. 15,000/35 = 429 generations per fixed mutation (his source text prints 1500, a typo; he hedges that he may be misreading).''',
 '- Stated: 25 fixed mutations, 40,000 generations.\n- Implicit: the datum is from a non-mutator line (the 2019 text says "19 whole genomes"; which lines is not stated in the quote).',
 '''- Against: Camestros (CA-06) obtains 429 from the same literature, an order of magnitude faster than 1,600 (as a question, not an assertion).
- In support: Day later replaced this datum with his own re-analysis (A2, A2b).
- Weaknesses: the repo has abstract-level access to Barrick 2009 only, so neither the 25/40,000 nor the 35/15,000 reading is checked against the paper. Camestros's own quote contains an arithmetic typo (1500 for 15,000).''',
 LITH+'''| Barrick et al. 2009 | "Although adaptation decelerated sharply, genomic evolution was nearly constant for 20,000 generations." | verified (abstract). The 40,000 generation horizon is not in the abstract. |
| Good et al. 2017 | trajectories to 60,000 generations | unverified for 25/40,000 |''',
 'Not a testable prediction; a retrieval task. Prediction: the Barrick 2009 full text gives a per-lineage fixation count that, divided into 20,000 generations, is within a factor of 4 of 429–1,600; if it gives 429 (Camestros), the original G_f was 3.7x too slow for early generations.',
 'Arithmetic only. Review: pending. Pending task: obtain Barrick 2009 full text (paywalled).', '- LTEE windows (20k, 40k, 50k, 60k) as presets.')

claim('A2b','gf-counting-rule-1322-vs-1587','Day revises his own counting rule: the ≥95% rule gives 8,679 fixations, the strict (lineage-aware) rule gives 5,496','day','A','A2',
 [('revises','A2'),('supersedes','A2')],False,'firsthand','checked',('holds','unverifiable','pending'),
 q('By this strict definition the twelve populations contain 5,496 whole-population fixations across 723,000 population-generations.',Z5+', p.1 (abstract).')+'\n'+
 q('A naive rule that counts the first time a mutation\'s pooled frequency reaches 95% — the method of most quick analyses, including an earlier draft of our own — returns 8,679.',Z5+', p.1.'),
 '''Whole-population fixations over 12 populations: strict 5,496 vs naive (≥95%) 8,679 (`ltee.whole_pop_fixations_lineage_aware.day_23105291`).

`derived:` 5,496/8,679 = 0.633 (the strict count is 36.7% lower; equivalently the naive count is 57.9% higher). The version ledger and `parameters.yaml` phrase this as "inflates counts 37%"; the precise statement is that the strict count is 37% *lower*. Non-mutator per-population strict counts 66, 73, 14, 9, 27 (sum 189, mean 37.8) give G_f = 60,000/37.8 = 1,587 versus the 3.0 value 1,322 (45.4 fixations): 17% fewer fixations, 20% slower rate. Ara+2: 3.0 §4.1 lists 64 (≥95% rule); Table 1 of Z23105291 lists 66 (strict), so the strict rule can raise a count as well as lower it.''',
 '- Stated: lineage-aware fixation is the stricter definition; the 3.0 paper (published four days earlier) used the pooled ≥95% rule.\n- Implicit: that Good 2017\'s lineage calls (SI, not retrieved) are the correct reference; that the 12-population totals map onto the 5-population non-mutator average without further adjustment.',
 '''- Against: Good 2017 reports clade coexistence (main text), which is the reason a pooled 95% rule can over-count (ledger); no critic has engaged Z23105291.
- In support: Day's own revision is in the direction that strengthens MITTENS (G_f 1,322 → 1,587; shortfall x1.2).
- Weaknesses: the 1,322 headline has not been restated in the later paper (versions ledger). The two papers coexist as published Zenodo records, and the abstracts disagree about the number of fixations a defensible rule returns.''',
 LITH+'''| Good et al. 2017 | clade structure; "inconsistent with a "periodic selection" model" | main text verified; "≥95%" and lineage calls unverified (SI) |''',
 'Not run. Prediction (claimant): strict recount reproduces 5,496. Prediction (alternative): any defensible rule moves the non-mutator G_f by less than a factor 2, so the debate is not about this.\n- Result that would change a verdict: a recount of the Good 2017 raw trajectories.',
 'Arithmetic audit (python3 -I, scratch). Raw trajectories not available in the repo. Review: pending.',
 '- Counting-rule toggle: pooled ≥95% / lineage-aware / clone-pair.')

claim('A2c','estimator-negative-fixations','The paper\'s own correction gives −906 fixations for Ara-2 and Ara+5 falls from 38 to 0, so the estimator is not a count','critic','A','A2',
 [('attacks','A2b'),('attacks','A2')],False,'firsthand','checked',('holds','accurate','pending'),
 q('Their correction formula then produces minus 906 “true fixations” in Ara−2.',
   '[r/DebateEvolution, Dumb-and-Dumber](https://www.reddit.com/r/DebateEvolution/comments/1wss2wj/), 2026-09-28, post 1wss2wj (RE-03).')+'\n'+
 q('Their Ara+5 count drops from 38 such mutations at 30,000 generations to zero at 60,000.',
   'same post (RE-04).')+'\n'+
 q('A count of fixed mutations cannot be negative; the negative value comes from the paper’s own correction',
   '[r/DebateEvolution, Sparky_6_4 (AI-assisted)](https://www.reddit.com/r/DebateEvolution/comments/1wxgsjm/), 2026-10-04, post 1wxgsjm (RE-10).'),
 '''The −906 figure appears in Z23003785 s5.2 ("Ara-2 achieved negative net fixations at 50,000 generations: −906 by clone-pair analysis") and in the s5.1 table (Ara-2: −906). Check of the quoted claim against Day\'s text: the figure exists, so the critic\'s quotation is accurate (fidelity: accurate). Day\'s own interpretation is population fragmentation ("The evolutionary mechanism did not accelerate. It broke."), not an estimator artefact.

`derived:` Ara-2 is a mutator; the 1,322 non-mutator headline does not include it. It enters the "all twelve populations" average (104,873-fold; 205e6/1,955 = 104,859). The Ara+5 30,000 → 60,000 drop is relevant to the non-mutator headline only if Ara+5 is in the five-population non-mutator set.''',
 '- Stated: a fixation count cannot be negative, so the estimator has a failure mode.\n- Implicit: that Day\'s correction subtracts a quantity that can exceed the observed count; that the Ara+5 count is for the same definition at both time points.',
 '''- Against (Day): s5.2 treats the negative value as biology: hypermutation fragments the population, and "One in seven mutator populations — 14% — responded to supermutation by achieving zero fixations."
- In support (critics): RE-10 and RE-03 above; Sparky_6_4 is AI-assisted and discloses citations from memory (RE-11).
- Weaknesses in the responses: Day\'s interpretation is untested; a "net fixation" metric that is negative is not a count, and the critic has not shown that the non-mutator headline is affected. The Ara+5 claim is not verified here against Z23003785.''',
 NOLIT,
 'Not run. Prediction (critic): re-estimating Ara-2 and Ara+5 with a monotone fixation definition gives non-negative counts and changes the mutator averages but not the non-mutator G_f by more than 20%. Prediction (Day): the strict rule (A2b) reproduces the ordering of populations.',
 'No script. Review: pending.', '- None directly; informs the counting-rule toggle in A2b.')

claim('A2d','gf-average-not-fastest','Day\'s G_f is an average, not the fastest fixation rate that could be claimed','critic','A','A2',
 [('attacks','A2e')],False,'firsthand','checked',('holds','accurate','supported'),
 q('If the figure is an average then it includes some mutations that fixed quicker and so is not the fastest fixed mutation rate.',
   '[Camestros Felapton, Reading Vox Day 2026 [5]](https://camestrosfelapton.wordpress.com/2026/01/29/reading-vox-day-so-you-dont-have-to-2026-5/), 2026-01-29, para 9 (CA-11).')+'\n'+
 q('He is correct that when he calculated the number it was an average. It isn’t intended to be a time for an individual chromosome.',
   'same post, para 9 (CA-10; a concession to Day on G1).')+'\n'+
 q('180 total fixed mutations is all there\'s time for using the fastest rate of mutational fixation ever observed in any organism',
   '[Gutsick Gibbon, Will Duffy livestream](https://www.youtube.com/live/6jXiwrcC5PQ), 2026-09-22, t=00:29:42 (DU-02; Duffy presenting MITTENS; auto-caption).'),
 '''Claim: G_f = 1,322 is a mean over populations and over mutations (fast and slow); Day (via Duffy) calls it "the fastest rate … ever observed in any organism".

Check against Day\'s own 3.0 tables (Z23003785 s5.1, s7.2): point-mutator populations are 43 to 183 generations per fixation (Ara-4: 43; Ara-3: 183; the IS-element mutator Ara+1 is 452; mean over seven 104.7) and the metagenomic mutator average at 60K is 78. 1,322/78 = 16.9, 893/104.7 = 8.5. So the LTEE itself contains rates 8.5x–17x faster than the headline; the non-mutator average is not the fastest observed rate even in the LTEE. Day treats the mutator rates as inapplicable to humans (s6; A5d).''',
 '- Stated by the critic: "average" and "fastest" are different quantities.\n- Implicit: that Day uses "fastest" in the statistical sense; Day uses it as "fastest in the applicable class of organism" (non-mutator).',
 '''- Against (Day): G_f is meant to be a throughput average (blog 2026-01-27: "25 mutations … fixed in parallel"); an average is the right quantity to multiply by time.
- In support (critic): Day\'s own 3.0 table.
- Weaknesses in the responses: Camestros\'s CA-07 asserts Day "has not shown" the rate is fast, without computing an alternative; the claim "fastest observed in any organism" is a claim about all organisms; the repo does not test it.''',
 NOLIT,
 'Prediction (critic): published fixation rates for faster-evolving non-mutator systems (e.g. viral or yeast experimental evolution) exceed 1/1,322 per generation. Not tested here (outside repo sources).',
 'No script. Review: pending.', '- Rate presets for non-mutator and mutator classes.')

claim('A2e','ltee-as-ceiling','The LTEE rate is an empirical ceiling on what evolution can accomplish, so the human shortfall is a lower bound','day','A','A',
 [('supports','A'),('depends-on','A2')],True,'firsthand','checked',('non-sequitur','pending','contested'),
 q('Whatever number the LTEE produces, it is the empirical ceiling on what evolution can accomplish when every tool in its kit is deployed simultaneously under ideal conditions.',Z3+', p.2.')+'\n'+
 q('The LTEE rate is therefore not an estimate for complex organisms. It is an unattainable ceiling, the absolute best-case scenario, the performance of a Formula One car used to benchmark a horse-drawn cart.',Z3+', p.4.'),
 '''Claim: rate_human <= rate_LTEE = 1/G_f (per generation), with no scaling. Equivalent form: `ltee.gens_per_fixation` is a lower bound on human G_f.

Check against the paper\'s own numbers (`derived:`):
- Mutation supply per genome per generation: LTEE 4.1e-4 (s4.3); human 38.4 = 3.2e9 x 1.2e-8 (s6.4). Ratio 93,659 (python3 -I). The same paragraph that calls the LTEE the ceiling lists "an effectively unlimited mutation supply" among its advantages (p.4), which these two figures do not support.
- Mutator populations in the same experiment run 8.5x–17x faster than the ceiling (A2d), so the ceiling is exceeded inside the LTEE.
- Day\'s own conclusion that a 100x mutation increase gives only 8.5x–17x (A5d) is evidence for sublinear but non-zero response to supply; it does not show response is zero.''',
 '- Stated: the LTEE has larger Ne, shorter generation, stronger selection, no mate-finding cost, no recombination overhead, and effectively unlimited mutation supply (p.4).\n- Implicit: that "no recombination overhead" is an advantage rather than a handicap (clonal interference, A5f); that per-generation fixation rate is bounded by the highest value in one experimental system.',
 '''- Against: Hössjer scales by mutation rate and genome length and finds a ~2x residual (A5a); the KITTENS authors find parity (A5b); Camestros (CA-08): "if humans reproduced in the way e.coli reproduce then maybe humans would never have evolved"; r/DebateEvolution (RE-07): the LTEE is largely nonrecombining, one clone, one environment (A5f). Gariépy (GA-01, secondhand): fixation rate in single-celled organisms is not equal to that in mammals because of sex and population-size variability.
- In support: Hössjer (HO-06) agrees with the conclusion after adjustment; American Hypnotist (AH-01) asserts the simple-organism rate must be faster than complex organisms (no calculation); Duffy (DU-06) says mammal fixation "way slower" (no numbers).
- Weaknesses in the responses: critics\' linear scaling is an illustration (RE-09); Hössjer\'s Haldane step to restore the gap is asserted not computed (HO-03); the ally statements AH-01, DU-06 give no numbers; Day\'s ceiling claim is an extrapolation from one system.''',
 LITH+'''| Tenaillon et al. 2016 | six hypermutable populations carried 96.5% of the point mutations; neutral mutations accumulate at constant rate in non-mutators | verified |
| Good et al. 2017 | many beneficial variants compete simultaneously; trajectories inconsistent with periodic selection | verified (main text) |''',
 '''No check has run (queued as A-sim in the file for A). 
- Under the claimant's model: adaptive fixation rate per generation saturates at about the LTEE value regardless of mutation supply and recombination.
- Under the opposing model: with recombination, rate grows with supply until Hill-Robertson/depletion limits, so the human rate exceeds the LTEE rate at 94,000x supply.
- Result that would change a verdict: a forward simulation in which fixation rate per generation, at fixed s and N, rises by more than an order of magnitude when supply rises by 1e4–1e5 with recombination on.''',
 'Script: none yet. Internal verdict is from the paper\'s own tables (above). Review: pending.',
 '- Supply (U per genome), recombination rate, population size, s distribution; output fixations per generation compared to 1/G_f.',
 'If the LTEE rate is not a ceiling for humans, the shortfall in A has no basis and ROOT loses its selection-rate branch.')

claim('A2f','ns-only-variants-4615-1408-24500','Natural-selection-only LTEE rates: 4,615 (blog) vs ~1,408 (Zenodo 3.0) vs ~24,500 "serial" (blog)','day','A','A2',
 [('revises','A2')],False,'firsthand','checked',('pending','n/a','pending'),
 q('The real, updated 60-generation LTTE numbers are: 4,615 generations per beneficial fixation (natural selection) 1,322 generations per all-cause fixation (natural selection + neutral theory + everything else)',
   '[The Temperature Rises](https://voxday.net/2026/09/27/the-temperature-rises/) (key B2026-09-27), blog, 2026-09-27, ¶13. The text prints "LTTE" and "60-generation" as written.')+'\n'+
 q('UPDATE: The SERIAL natural selection rate for the LTEE at 60k generations is ~24,500 generations per fixation.',
   '[Math Teacher Can\'t Math](https://voxday.net/2026/09/30/math-teacher-cant-math/) (key B2026-09-30), blog, 2026-09-30, ¶23.'),
 '''Three different "natural-selection-only" numbers in the Day corpus:
- 4,615 gens/beneficial fixation (blogs 2026-09-27, 09-28, 09-30): `derived:` 60,000/4,615 = 13.0 beneficial fixations per 60,000 generations.
- ~1,408 gens/beneficial fixation (Z23003785 s4.3): 56.0 clone-pair fixations − 20.5 neutral hitchhikers (4.1e-4 x 50,000) = 35.5; 50,000/35.5 = 1,408 (reconciles).
- ~24,500 "serial" (blog 09-30): `derived:` 60,000/24,500 = 2.4 sequential events per 60,000 gens. Compare Ara+2 alone: 14 sequential events in 60,000 gens (G1a) = 4,286 gens/event.

13.0 beneficial fixations (4,615) is not derivable from the s4.3 inputs (35.5 beneficial). No derivation of 4,615 or 24,500 appears in the corpus (the blog says "I\'ll want to dig in a little deeper to be certain of that").''',
 '- Stated: a natural-selection-only rate separates sweeps from hitchhikers and drift.\n- Implicit: all hitchhikers are neutral and all sweeps are beneficial; the quantity differs between sources.',
 '''- Against: none in corpus.
- In support: none; these are Day\'s statements about his own numbers.
- Weaknesses: the numbers are mutually inconsistent as stated and none carries a derivation; Day marks the 24,500 as provisional. MITTENS 3.0 itself says the total throughput (1,322), not the beneficial-only rate, is what MITTENS measures (s4.3).''',
 NOLIT,
 'Prediction: a recount using the ≥95% and lineage-aware rules (A2b) yields a beneficial-only G_f of ~1,400–1,700 (s4.3 style), not 4,615. Result that would change the verdict: a published derivation of 4,615.',
 'Arithmetic only. Review: pending.', '- Separate counters for sweep drivers, hitchhikers and drift fixations in the simulator output.')

claim('A2g','ltee-neutral-clock-literature','LTEE non-mutators accumulate mutations clock-like; neutral mutations at a constant rate; most fixed mutations beneficial','literature','A','A2',
 [('supports','A2')],False,'firsthand','extracted',('n/a','accurate','supported'),
 '''> The populations that retained the ancestral mutation rate support a model where most fixed mutations are beneficial, the fraction of beneficial mutations declines as fitness rises, and neutral mutations accumulate at a constant rate.

Source: Tenaillon et al. 2016 (key Tenaillon2016), Abstract.

> Although adaptation decelerated sharply, genomic evolution was nearly constant for 20,000 generations.

Source: Barrick et al. 2009 (key Barrick2009), Abstract (Europe PMC; full text paywalled).

> The number of fixed mutations closely tracks Mp(t) in some populations (e.g. Ara+2 and Ara+4), but there is a marked deficit of fixations in others (e.g. Ara-6).

Source: Good et al. 2017 (key Good2017), Results.
''',
 'Descriptive. Relevant to `ltee.gens_per_fixation` (the rate is steady for non-mutators) and to the critics\' use of k = μ for LTEE neutral accumulation.',
 '- Stated: observed in the LTEE.\n- Implicit: the LTEE environment and clonal structure.',
 '''- Against: critics (A5f) say clonal interference and absence of recombination make the LTEE rate depressed relative to a recombining genome. Day (Z23003785 s8.2) says neutral fixation by drift is "off" at Ne ≈ 3e7 and that the 20 neutral fixations were all hitchhikers.
- In support: Day cites the steadiness for a stable G_f; critics cite it for neutral clock-like change.
- Weaknesses: abstracts only for Barrick; Good 2017 SI not retrieved.''',
 LITH+'''| Tenaillon2016 | above | verified |
| Barrick2009 | above | verified (abstract) |
| Good2017 | above | verified (main text); ≥95% unverified |''',
 'No prediction; descriptive.', 'No script.', '- Preset: LTEE non-mutator trajectory shape (nearly linear accumulation).')

claim('A2h','supermutation-arithmetic-slip','Day\'s s6.4 supermutator arithmetic is a tenfold slip: 3.2e9 x 1.2e-8 x 100 = 3,840, not 38,400','critic','A','A5d',
 [('attacks','A5d')],False,'firsthand','checked',('holds','accurate','n/a'),
 q('Section 6.4 also makes a tenfold arithmetic mistake: 3.2 billion × 1.2 × 10⁻⁸ × 100 is 3,840 mutations per haploid genome, not 38,400.',
   '[r/DebateEvolution, Dumb-and-Dumber](https://www.reddit.com/r/DebateEvolution/comments/1wss2wj/), 2026-09-28, post 1wss2wj (RE-02).')+'\n'+
 q('A 100-fold increase in mutation rate in the human genome would produce approximately 38,400 mutations per individual per generation (3.2 × 10⁹ bp × 1.2 × 10⁻⁸ × 100).',
   Z3+', p.11 (s6.4). Locator: line "increase in mutation rate in the human genome would produce approximately 38,400 mutations per individual per generation".'),
 '''3.2e9 x 1.2e-8 = 38.4; x 100 = 3,840. `derived:` the paper\'s 38,400 is 10x too large. Its next step, "10% deleterious fraction … 3,840 deleterious mutations", is 10% of the erroneous 38,400; the correct figure is 384. Its fitness figure (0.999)^3,840 ≈ 0.02 becomes (0.999)^384 ≈ 0.68; (0.99)^3,840 ≈ 1e-17 becomes (0.99)^384 ≈ 0.021 (recomputed: 0.999^384 = 0.681, 0.99^384 = 0.0211). The same product at 1x gives 38.4 mutations per haploid genome per generation, the number used in A5b.''',
 '- Stated: arithmetic with Day\'s own inputs (the critic and the paper use the same product).\n- Implicit: the 10% deleterious fraction is Day\'s; the critic does not dispute it.',
 '''- Against: none in corpus; Day has not been recorded answering this point.
- In support: the arithmetic is verified here.
- Weaknesses in the response: the slip affects the argument of s6.4 that a mutator allele in a sexual organism is immediately selected against, whose conclusion (a 100x mutator in a sexual organism is strongly deleterious) would still hold at 384 deleterious mutations (fitness 0.021 at s = 0.01). Whether 3.0 contains other uses of 38,400 was not searched.''',
 NOLIT, 'Arithmetic; no pre-registration needed.', 'Arithmetic audit (python3 -I, scratch). Review: pending.', '- None.')

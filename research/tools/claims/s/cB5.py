from common import *
RV2='`research/checks/REVIEW.md#2026-10-07--correctness-review-2-sonnet-on-b0b3`'
B05='`research/checks/baseline_textbook.py` (seed 20261007) · B0.5 result: neutral k at equilibrium, N=50: 0.05018, N=200: 0.04964, vs U = 0.05 (z = +0.13, −0.64); holds for both N, consistent with k = U for any N'

add(id='B5',slug='critics-k-equals-mu-cancellation',title='Critics: 2N mu new mutations × 1/(2N) fixation probability = mu substitutions per generation, independent of N',side='critic',branch='B',parent='B',
 edges=[('attacks','B1'),('attacks','B2'),('attacks','B3a')],lb=(True,'if the steady-state identity applies to the 252,000-generation window, B1, B2 and B3 yield no deficit (subject to B1c)'),
 sourcing='firsthand',status='reviewed',v=('holds','accurate','contested'),
 quotes=[Q('GG','and then what you\'re left with is a neutral substitution rate that\'s equal to the mutation rate','t=01:48:19 (Hancock; auto-caption; derivation via Taylor expansion of the Kimura fixation probability)'),
   Q('MFC','Genetic drift happens in every population and his claim otherwise is mystifying. Population size only affects which alleles are effectively neutral.','comment UgyhNduYke46IStQ5pd4AaABAg (Mansfield)'),
   Q('RED','ignores that neutral mutations fix at approximately the mutation rate','comment pcovtvf by DarwinZDF42 (score 27), reply under r/DebateEvolution post 1wss2wj')],
 formal='''k = (2Nμ_site-or-genome) × (1/2N) = μ per generation (diploid, census N, neutral). In genome terms k = μ_G = μ_site × L_haploid. Glossary sense: **throughput** at steady state; the identity says nothing about how long an individual fixation takes or whether the window is long enough (B1).
Acceptance by Day's side: Z22129121 "this paper accepts it throughout"; blog 2026-08-27 (B3g).''',
 a_stated='Neutral; constant size at equilibrium; census N in supply and in P_fix.',a_impl='The ancestral population was at equilibrium at the split (B1c); the 252,000-generation window is long relative to the transit (B1: 4Nₑ = 40,000–132,000 for Nₑ = 10⁴–3.3×10⁴).',
 against='Day (B1, B2): steady state not reached; k(T) = μF(T).',support=rq('RED','It needs the elapsed time to be long compared with the fixation time.',loc='post 1wss2wj, comment-body (Dumb-and-Dumber; accepts the 4Nₑ time and argues 252,000 is long compared with it)')+'\n  Related checks (below).',
 weak='The Reddit author uses Nₑ ≈ 10⁴–3.3×10⁴ for 4Nₑ, which is the quantity Day calls circular (B3h). Mansfield\'s and Darwin\'s comments are one-liners.',
 lit=[lit_row('Kimura 1962','"if we let s → 0 in (10), we obtain U = 1/2N, the result known for a neutral gene."','verified-accurate (ledger; see B7a)'),
      lit_row('Tenaillon 2016','"neutral mutations accumulate at a constant rate" (non-mutator LTEE populations)','verified (ledger)')],
 prereg_note='Pre-registered prediction (copied from RESULTS B0.5; the check has run).',
 p_claim='(Critic) at equilibrium the neutral substitution rate equals the mutation input U for any N.',p_opp='(Day, k = μ accepted at steady state) same value; the dispute is the start state and window (B1, B2).',
 p_change='A scenario in B1c where the human-lineage window is not long relative to transit would reduce the applicability; the identity itself is not in doubt.',
 check='Script: '+B05+'. Review #2: B0.5 holds. Review: '+RV2,
 sim=['mutation input per generation (U)','N','equilibrium vs non-equilibrium start'])

add(id='B5a',slug='mccarthy-22-5-million',title='McCarthy: 100 mutations/newborn × N = 10,000 over 9 My gives 450 billion mutations; × 1/20,000 = 22.5 million fixed',side='critic',branch='B',parent='B5',
 edges=[('attacks','B1'),('attacks','B3a')],lb=(False,'illustrative expectation using Day\'s own inputs; load rests on N = Nₑ and all-neutral'),
 sourcing='firsthand',status='extracted',v=('holds','n/a','contested'),
 quotes=[Q('MC1','50,000 x 9 million = 450 billion new mutations altogether.','para 50'),
   Q('MC1','450 billion x 1/20,000 = 22.5 million fixed mutations.','para 52'),
   Q('MC2','400 billion x 1/20,000 =20 million fixations. So when we apply the time available to the numbers we land on the exact correct result.','para 21 (time-adjusted version: subtracts the last 50,000 generations)')],
 formal='''**Arithmetic audit (derived, python3 -I):** 100 × 10,000 / 20 y = 50,000 new mutations per year ✓; × 9×10⁶ y = 4.5×10¹¹ ✓; × 1/(2 × 10,000) = 22.5×10⁶ ✓. Per generation: 100 × 10⁴ = 10⁶; × 450,000 generations = 4.5×10¹¹ ✓; per lineage 50 fixed per generation × 450,000 = 22.5M ✓. Time-adjusted: (450,000 − 50,000) × 50 = 20.0M ✓ (as quoted by Day, 2026-02-04); using Day's own correction E[F] ∝ T − 4Nₑ with 4Nₑ = 40,000: (450,000 − 40,000) × 50 = 20.5M (derived).
Sensitivity (derived): with a neutral fraction f, count = f × 22.5M; f = 0.89 is needed for 20M. With 70 SNV-type mutations per newborn (Keightley 2012 "~70") the ceiling at f = 1 is 35 × 450,000 = 15.75M < 20M.
Comparator: McCarthy's "20 million observed" is the per-lineage half of Day's 2019 40M total; SNV-only 17.5M per lineage (Z23003785).''',
 a_stated='Day\'s own inputs (100 mutations/person, Nₑ = N = 10,000, 9 My, 20 y).',a_impl='N = Nₑ; all mutations neutral ("only 3% of new mutations are deleterious", uncited); 100 per newborn counts all de novo events (SNV and others); the start state is full.',
 against='Day (R2 2026-02-04): same model with the correct Nₑ and N gives 8.25 (B3e; sign problem, now withdrawn B3g); Day (IR): subtract 4Nₑ (B1a, a 9% effect at these inputs).',support='RESULTS B0.5; Hössjer\'s Eq. 3.1 gives 7.6M with his own d and L (B5h).',
 weak='Expected value only (derived: Poisson sd ≈ 4.7 thousand, immaterial). Uncited 3% figure; 60–100 range, not a point value; N = Nₑ.',
 lit=[lit_row('Keightley 2012','"an average of ~70 new mutations arise in the human diploid genome per generation"','verified-partial (abstract only)')],
 p_claim='(McCarthy) ≈ 20–22.5M fixed on one lineage under neutral drift.',p_opp='(Day) 8.25 (B3e) or an empty-pipe deficit (B1a: 20.5M with McCarthy\'s inputs, a 9% reduction).',
 p_change='B1c if the start state is empty/expanded; a sourced neutral fraction.',check='Script: none (arithmetic). See B5 for the identity check.',sim=['new mutations per newborn','neutral fraction','N, Nₑ','window T'])

add(id='B5b',slug='mansfield-one-fixation-per-generation',title='Mansfield: if 2% of ~100 de novo mutations are neutral, there is on average 1 neutral fixation per generation',side='critic',branch='B',parent='B5',
 edges=[('attacks','B1'),('attacks','B3a')],lb=(False,'an illustration; by itself it falls ~44× short of 20M, so it does not close the gap alone'),
 sourcing='firsthand',status='extracted',v=('holds','n/a','contested'),
 quotes=[Q('MFC','If even just 2 of these 100 are neutral - which is certainly way under the actual proportion - then in a population of size N there are about 2*N new neutral alleles introduced each generation.','comment UgyhNduYke46IStQ5pd4AaABAg (Mansfield)'),
   Q('MFC','So, the expectation is that there will be on average 1 neutral fixation every generation if just 2% of new mutations are neutral.','same comment')],
 formal='''2 neutral per zygote × N zygotes = 2N neutral alleles; × 1/(2N) = 1 fixation per generation ✓ (derived). Over 450,000 generations 450,000 fixations, over 252,000 generations 252,000; against 20M that is 44.4× short, against 17.5M (SNV) 69.4× short (derived). With a neutral fraction f of 100 mutations: 50 f per generation; 20M in 450,000 generations needs f = 0.89; 17.5M in 252,000 needs f = 1.39 (>1: impossible at 100 per zygote).''',
 a_stated='2% of ~100 de novo mutations are neutral; N zygotes per generation.',a_impl='"way under the actual proportion" (Mansfield; no figure); a full pipe (B1c); the 20M requirement is per lineage.',
 against='Day (EDU 2026-10-01): same identity, but the pipe is not full (B1c); N/Nₑ not used by Mansfield.',support='Hössjer\'s 7.6M and Hancock\'s 19.4M give the same order when all sites are counted (B5c, B5h).',
 weak='The illustration is under by a factor ~44 and the comment states the proportion qualitatively; Mansfield quotes Day only via a commenter\'s paste (secondhand per ledger).',
 lit=[],p_claim='1 neutral fixation per generation (at 2%).',p_opp='(Day) k = μ requires a full pipe.',p_change='Mansfield or others supplying the actual neutral fraction (e.g., ~0.9+ of non-coding sites).',
 check='Script: none (arithmetic). See B5.',sim=['neutral fraction','new mutations per zygote'])

add(id='B5c',slug='hancock-76-8-per-generation',title='Hancock: ~76.8 new mutations fixed per generation, ~38 million over 2 × 252,000 generations',side='critic',branch='B',parent='B5',
 edges=[('attacks','B1'),('attacks','B3a'),('attacks','A')],lb=(False,'null-model comparison; its haploid/diploid basis halves the headline match'),
 sourcing='firsthand',status='extracted',v=('holds','n/a','contested'),
 quotes=[Q('GG','that\'s about 76.8 uh new mutations that are fixed in the population every single generation.','t=01:51:04'),
   Q('GG','use 6.4. This is the diploid genome size for the fixation rate because you fix on a hloid genome. So, it should be 3.2 e to the 9.','t=01:52:48 (in-video correction, preceded by "we can\'t" at the end of the 01:52:27 chunk; "hloid" = haploid in the auto-caption)'),
   Q('GG','Um so that\'s 152 on average. If we divide that in half to take the','t=01:53:10 (continues in the 01:53:30 chunk: "the hloid genome size that gives us 76.")'),
   Q('GG','we\'ll say about 38 million.','t=01:56:15')],
 formal='''**Arithmetic audit (derived, python3 -I):** 6.4e9 × 1.2e-8 = 76.8 ✓ (diploid bases, the first-pass figure). Haploid: 3.2e9 × 1.2e-8 = 38.4 per generation per lineage. 2 lineages × 252,000 × 76.8 = 38.7M (the quoted "about 38 million"); with 38.4: 19.35M. The first-pass 76.8 used the diploid genome (self-corrected on screen at t=01:52:48). The retained 76 is a different quantity: a cited de novo count of 98–206 per generation (mean 152, including structural variants), halved to the haploid genome: 152/2 = 76 ✓ (derived), then 76 × 2 × 252,000 = 38.3M. That is a count of mutation *events* of all types, so the matching comparator is the CSAC event total (35M SNV + 5M indel events ≈ 40M, derived), not the SNV count alone.
Comparators for the SNV-only haploid version (38.4 per generation): 19.35M vs the CSAC ~35M SNV total (includes polymorphism): ratio 0.55, i.e. 1.8× short (the repo's balance ledger records a ~1.8× doubling in Hancock's headline); vs fixed-only 0.78–0.86 × 35M = 27.3–30.1M: 1.4–1.6× short (derived). Including ancestral coalescence (B4a) with Nₑ,anc = 1.32×10⁵ adds 20.3M (θ = 6.3e-3 × 3.2e9), taking 19.35M to 39.6M.
205M check: Hancock states the number as 205 million and divides to get "something like 407" per generation: 205e6/(2 × 252,000) = 406.7 (derived ✓). Day's 205M is already per human lineage (Q15: "205 million required fixations on the human lineage"), which would give 813/generation (derived), i.e. 10.6× the 76.8 or 21× the 38.4; Hancock's "~5×" is therefore low by 2× if 205M is per lineage.''',
 a_stated='Neutral substitution rate = mutation rate; both lineages fix at the same rate; self-described as a back-of-the-napkin calculation (GG-16).',a_impl='All 3.2 Gb are neutral (upper bound); mutation rate 1.2e-8 per bp for the first pass; the final 76 counts events including structural variants, and a structural event fixes as one event, not as many base pairs (consistent with the events-vs-bp point against Day\'s 205M, A3x); the 205M comparison treats events and bases alike (see below).',
 against='Day (CLUE 2026-09-22) replying to a similar message: "confused mutations with fixations" (see B5d).',support='Match to the 35M SNV order after the factor-2 correction is partial: ≈ 19M vs 35M.',
 weak='Auto-captions garble names and figures (the cited paper is rendered "perky at all 2025"). The first-pass diploid basis was a factor-2 slip, corrected on screen. The SNV-only haploid version gives ≈19M, so the match-to-35–40M statement depends on counting SV events in the supply but comparing to a SNV-dominated total.',
 lit=[lit_row('Kong 2012','μ = 1.20×10⁻⁸ per nucleotide per generation','verified'),
      lit_row('Chimpanzee Sequencing and Analysis Consortium 2005','"The differences between one copy of the human genome and one copy of the chimpanzee genome include both the sites of fixed divergence between the species and some polymorphic sites within each species."','verified (ledger)')],
 p_claim='Neutral expectation ≈ the 35–40M observed SNVs.',p_opp='(Day) pipeline not full (B1c); a factor ~2 gap remains after haploid correction.',p_change='B4a (ancestral term) and B1c.',
 check='Script: none (arithmetic computed with python3 -I). Related: B5.',sim=['haploid vs diploid genome basis','μ','L neutral fraction','lineages counted'])

add(id='B5d',slug='relayed-7-2-million',title='Relayed population geneticist: 6 My / 25 y × 30 mutations per generation = 7.2 million differences "literally no selection required"',side='critic',branch='B',parent='B5',
 edges=[('attacks','B1'),('attacks','B3a')],lb=(False,'anonymous, relayed, informal; Day\'s reply is a disagreement about k = μ'),
 sourcing='secondhand',status='extracted',v=('holds','n/a','contested'),
 quotes=[Q('DU','Under neutrality, 6 million years divided by 25 generations um or 25 year generation times 30 mutations per generation is equal to 7.2 million differences. Literally no selection','t=00:48:18 (auto-caption; read aloud by the host Gutsick Gibbon)',sh='an unnamed population geneticist, as relayed by the host; the quote is truncated at "selection"'),
   Q('CLUE','The population geneticist on call confused mutations with fixations. 30 mutations cannot fixate per generation.',file='day/blog-2026-09-22-zero-probability-zero-clue.txt',note='Day\'s reply')],
 formal='''**Arithmetic audit (derived, python3 -I):** 6×10⁶/25 = 240,000 generations; × 30 = 7.2M ✓ (with 6.3 My: 252,000 × 30 = 7.56M, equal to IR's steady-state figure in B1a). Comparators: 7.2M vs SNV-only 17.5M per lineage (Z23003785) = 2.4× short; vs 205M = 28.5× short; vs Day's own IR figure 7.56M (the same quantity). Day's reply "7.2 million is significantly smaller than 410 million" is arithmetically correct (7.2/410 = 1.8%).
"30 mutations cannot fixate per generation" is a statement against the steady-state identity (k = μ means 30 neutral substitutions per generation at equilibrium); Day's own IR uses the same μL ≈ 30 as the steady-state count, so the disagreement is the fill state (B1c), not the arithmetic.''',
 a_stated='30 neutral mutations per generation become 30 fixations per generation at steady state.',a_impl='Per-lineage count; full pipe; the 30 figure is unreferenced (pedigree haploid 38.4, derived).',
 against='Day: confused mutations with fixations (reply above); 7.2M < 410M.',support='RESULTS B0.5 / B1: the equilibrium-start count equals U·T.',
 weak='Relayed by a non-expert host mid-stream; no citation; the quote is truncated; Day\'s own B1a uses the same arithmetic.',lit=[],p_claim='7.2M neutral differences without selection.',p_opp='(Day) pipeline not full; the real requirement is 17.5M (SNV) or 205M.',p_change='B1c, B4a.',check='Script: none (arithmetic). Locator in Day\'s post: ¶9 of extracted text.',sim=['μL per lineage','T'])

add(id='B5e',slug='nesslig20-37-8-million',title='Nesslig20: mu_G = 75 per generation, k = 75, 2 × 75 × 252,000 = ~37.8 million fixed neutral mutations',side='critic',branch='B',parent='B5',
 edges=[('attacks','B1'),('attacks','B3a')],lb=(False,'null-model comparison; its basis halves the headline match'),
 sourcing='firsthand',status='extracted',v=('pending','n/a','contested'),
 quotes=[Q('PS','Let’s assume a conservative neutral mutation rate of [ μ_G = 75 ]. That means [ k = 75 ] mutations will fix per generation.','post 1 by Nesslig20, §2.2'),
   Q('PS','So, the expected number of fixed neutral mutations that separates humans and chimps is ~37.8 million based on this rough calculation.','post 1 by Nesslig20, §2.2')],
 formal='''**Arithmetic audit (derived, python3 -I):** 2 × 75 × (6.3e6/25 = 252,000) = 37.8M ✓. The post defines μ_G via "the neutral mutation rate per haploid genome per generation" (§2.1) and then writes: "Estimates vary from 100 to 200 per generation. Let’s assume a conservative neutral mutation rate of [ μ_G = 75 ]." The basis of 75 is not stated: if it is a zygote-level count, the haploid value is 37.5 and 2 × 37.5 × 252,000 = 18.9M (derived), about 0.54 of the 35M SNV total (the balance ledger flags this factor of 2); if it is a halved 100–200 range, the product stands as written. The harvest note read it as the first case; the text does not settle it. The post uses P_fix = 1/(2Nₑ) and supply 2Nₑ μ_G in the same expression, so the cancellation is internally consistent.
Reference-genome note (Nesslig20): "since they use one (or a few) reference genomes, not all of the differences they identified between genomes are actually fixed" — the same polymorphism caveat as CSAC (14–22%).''',
 a_stated='Neutral drift at k = μ_G; both lineages; 6.3 My, 25 y.',a_impl='75 is a haploid-genome count (unstated derivation); no neutral-fraction constraint; full pipe.',
 against='Possible factor-2 basis question (balance ledger; text does not settle it).',support='Order-of-magnitude agreement with 31–62M SNVs (1–2%).',weak='a rough calculation by the author\'s own words; the 1–2% range is wide.',
 lit=[lit_row('Chimpanzee Sequencing and Analysis Consortium 2005','polymorphism accounts for 14–22% of observed divergence','verified (ledger)')],
 p_claim='~37.8M neutral fixed differences.',p_opp='(if 75 is zygote-level) ~18.9M; ratio to 35M ≈ 0.54.',p_change='B4a.',check='Script: none (arithmetic computed with python3 -I).',sim=['haploid vs diploid basis','neutral fraction'])

add(id='B5f',slug='reddit-9-7-million-haploid',title='r/DebateEvolution: 38.4 × 252,000 = ~9.7 million expected neutral substitutions on the human lineage vs 17.5 million required',side='critic',branch='B',parent='B5',
 edges=[('attacks','B1'),('attacks','B3a')],lb=(False,'illustration; the gap to the SNV-only requirement is under a factor of two'),
 sourcing='firsthand',status='extracted',v=('holds','n/a','contested'),
 quotes=[Q('RED','or about 9.7 million over its proposed 252,000 generations.','post 1wss2wj (Dumb-and-Dumber)'),
   Q('RED','It needs the elapsed time to be long compared with the fixation time.','post 1wss2wj (Dumb-and-Dumber)')],
 formal='''Derived: 3.2e9 × 1.2e-8 = 38.4 per generation; × 252,000 = 9.68M ✓ (single lineage). The same post states the SNV-only requirement of 17.5M and that "The gap is under a factor of two": 17.5/9.68 = 1.81 (derived). It also takes the neutral fixation time as 4Nₑ ("40,000–132,000 generations") and notes 252,000 is well above it — the B1a subtraction would give (252,000 − 40,000) × 38.4 = 8.14M or (252,000 − 132,000) × 38.4 = 4.6M (derived).''',
 a_stated='Haploid 3.2 Gb, μ = 1.2e-8, 252,000 generations; Day\'s Z23003785 uses the same formula for the LTEE hitchhikers (§4.3).',a_impl='All sites neutral; full pipe.',
 against='n/a',support='B5c/B5e after haploid correction (19.4M and 18.9M for two lineages, ≈ 9.7M per lineage).',
 weak='The post is KITTENS-adjacent reddit commentary (AI-assisted per related posts); the 17.5M comparator includes polymorphism and ignores the ancestral term.',
 lit=[],p_claim='~9.7M per lineage; gap < 2×.',p_opp='(Day) 7.56M (IR) with a 15.9% empty-pipe loss; gap to 17.5M ≈ 2.6×.',p_change='B4a (ancestral term) closes the gap if Nₑ,anc is ~10⁵.',check='Script: none (arithmetic).',sim=['L haploid','μ','T'])

add(id='B5g',slug='paul-king-comment-neutral-rate-equals-arrival',title='Camestros Felapton commenter Paul King: neutral mutations reach fixation at the same rate as they arrive, with much parallelism',side='critic',branch='B',parent='B5',
 edges=[('attacks','B3a'),('attacks','F1')],lb=(False,'one-line comment; the "CS commenter" cited in the hierarchy'),
 sourcing='firsthand',status='extracted',v=('holds','accurate','contested'),
 quotes=[Q('CF2b','There’s a well known result in population genetics that neutral mutations reach fixation at the same rate as they arrive. And yes, that involves a lot of parallelism because fixation without selection is slow.','comment by Paul King, 2026-01-25 7:56 pm (new quote; not in quotes-critics.md)')],
 formal='''Steady-state identity k = μ (see B5) with explicit mention that it involves parallel fixations (F1). Same comment adds that F_max must equal the number of mutations required, not DNA differences (A3x). Camestros\'s reply: "Neutral Theory is coming up. Day has done some homework" (not a rebuttal). Identification: PLAN.md's "CS commenter" is read as a commenter on Camestros Felapton\'s blog.''',
 a_stated='Neutral substitution rate = arrival rate.',a_impl='Steady state.',against='Day (B1, B2).',support='B5, F1.',weak='Informal; no numbers; assumes steady state.',
 lit=[],p_claim='k = μ with parallel fixation.',p_opp='(Day) fill state (B1c).',p_change='B1c.',check='Script: see B5.',sim=['—'])

add(id='B5h',slug='hossjer-neutral-d-mu-7-6-million',title='Hossjer (ally): neutral fixation rate is d × mu per site; 3e9 × 0.45 × 1.25e-8 × 450,000 = 7.6 million',side='ally',branch='B',parent='B5',
 edges=[('supports','B5'),('attacks','B3a')],lb=(False,'the ally-side acceptance of 2Nμ × 1/(2N) = μ; leaves a ≈2.6× gap to 20M with d = 0.45'),
 sourcing='firsthand',status='extracted',v=('holds','accurate','contested'),
 quotes=[Q('HOS','equation (5) is based on the neutral theory of evolution.','PDF p5 (§3; his neutral count is PDF "(5)", numbered 3.1 in the text)'),
   Q('HOS','which still is less than 20 million, but only by a factor of 2.','PDF p3 (Eq. 2.4, the genome-length scaling of MITTENS)')],
 formal='''Hössjer (Eq. 3.1): F_hum = L·d·μ·t_div = 3×10⁹ × 0.45 × 1.25×10⁻⁸ × 450,000 = 7.6M (derived ✓ 7.59M); without d: 16.9M vs 20M (balance ledger). He writes 2Ndμ × 1/(2N) = dμ (overlapping generations with turnover d), so the N-independent neutral rate, not N/Nₑ. E. coli neutral check: 1/(4.6e6 × 1e-10) = 2,170 vs Day\'s 1,600 (derived ✓).''',
 a_stated='Neutral rate dμ per nucleotide; fixation independent between nucleotides.',a_impl='Nucleotides independent (no linkage); d = 0.45 reduces the neutral supply (A4), which Day applies to selection and Hössjer carries into the neutral calculation.',
 against='Day (B4d) notes his support for the dating circularity; Day does not rely on this calculation.',support='B5, B5a, B5f.',weak='d inside a neutral rate is not a standard neutral result (turnover coefficient A4 unverified); his "factor of 2" gap arises from d; he asserts but does not compute the cost-of-selection step (branch H).',
 lit=[],p_claim='7.6M neutral fixations on one lineage (with d).',p_opp='(Day) steady state not reached.',p_change='A4.',check='Script: none (arithmetic).',sim=['d (turnover) in the neutral supply','L','μ'])

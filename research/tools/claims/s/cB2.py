from common import *
RV3='`research/checks/REVIEW.md#2026-10-07--review-3-sonnet-correctness--two-sided-steelman-of-b1b-b2a-f1`'

add(id='B2',slug='hard-limits-domain-of-k-mu',title='Hard Limits: drift cannot complete fixations above a census ceiling; the domain of k = mu is empty for large vertebrates',side='day',branch='B',parent='B',
 edges=[('supports','B'),('depends-on','B2a'),('depends-on','B2b'),('depends-on','B2c')],
 lb=(True,'with B1 it is the other route by which the neutral escape is closed; if both fail ROOT as worded fails'),
 sourcing='firsthand',status='reviewed',v=('pending','unverifiable','contested'),
 quotes=[Q('HL','Checking them yields a hard ceiling on population size, X = (Vₖ + 2)·G/16 — reproductive variance and lineage generations alone, with no mutation rate, no coalescent quantity, and no fitted constant.','p.1 (abstract)'),
   Q('HL','The domain of k = μ is confined to demographic conditions that no non-endangered species is capable of meeting.','p.1 (abstract)')],
 formal='''Summary (the pieces are B2a, B2b, B2c, B2d): 4Nₑ < G ⇒ N < X = (Vₖ+2)G/16; above X, P(τ ≤ G | fixation) ~ exp(−π²Nₑ/G).

The paper contains no reference list in the harvested copy (balance ledger), and cites Kimura & Ohta 1969, Wright, Hill 1972 and Maruyama 1970/74 in the text only. `parameters.yaml` has no entries for Vₖ or census N; propose `new: population.Vk_human = 5` (HL Table 1) and `new: population.census_human = 8.2e9` (HL Table 1).''',
 a_stated='k = μ is accepted ("this paper accepts it throughout"); the mean fixation time 4Nₑ is the transit time; Nₑ is the variance effective size; Wright\'s Nₑ = (4N−2)/(Vₖ+2).',
 a_impl='A mean time (4Nₑ) is a deadline unless the tail is quantified (addressed by B2a); the lineage window G is the relevant window (but the paper\'s 78-million exponent uses a 400-generation window, B2c); the pipe is empty at the start of the window (B1c/B1d).',
 against=rq('MFC','Genetic drift happens in every population and his claim otherwise is mystifying. Population size only affects which alleles are effectively neutral.',loc='comment UgyhNduYke46IStQ5pd4AaABAg (Mansfield; replying to a Day blog sentence about drift at large N, not to HL)')+'\n  RESULTS B2a: the exponent is a per-allele latency tail, not a throughput bound.',
 support='RESULTS B2a: the exponent −π² is the correct leading-order short-time asymptotic. Day\'s own simulation reproduces the mean time (391 vs 400).',
 weak='Mansfield\'s comment predates HL and is aimed at a different statement. Day\'s abstract summary "about ten thousand" is not what the paper\'s table gives (35,000–114,000, B2b). The two sides have not met on the fill-state question (B1c).',
 lit=[lit_row('Kimura & Ohta 1969','"takes about 4Ne generations until it spreads to the whole population" (p.766)','accurate'),
      lit_row('Maruyama 1970/1974 (cited by HL, third objection)','not retrieved (abstract only for 1970)','unverified')],
 p_claim='k(T) = μF(T) with F exponentially small for T ≪ 4Nₑ.',p_opp='For a population at equilibrium the flux is μ regardless of transit time (B1, B1b).',
 p_change='See B2a (exponent), B2b (ceiling inputs), B1c (fill state).',
 check='See child claims. Script: `research/checks/b2a_hard_limits_chain.py`, `research/checks/b2a_scaling.py` · Result: see B2a. Review: '+RV3,
 sim=['Vₖ','G (lineage generations)','census N and Nₑ definition (variance/coalescent)','window T','fill state'])

add(id='B2a',slug='exp-pi2-ne-over-g',title='F(T) ~ exp(−pi^2 Ne / T) for T << 4Ne (short-time fixation tail)',side='day',branch='B',parent='B2',
 edges=[('supports','B2')],lb=(False,'the exponent is verified; what carries weight is which Nₑ and T are inserted (B2c) and the fill state'),
 sourcing='firsthand',status='reviewed',v=('holds','unverifiable','pending'),
 quotes=[Q('HL','F(T) ∼ exp( − π² Nₑ / T ), T ≪ 4Nₑ The naive fill fraction T/4Nₑ is not just unproven; it is an overstatement, and a vast one.','p.8 (§The Second Objection)'),
   Q('HL','k(T) = μ · F(T),      F(T) = P(τ ≤ T | fixation)','§The Second Objection (definition; resolves the "UNVERIFIED reading" flag in RESULTS B2a: Reading 1, conditional on eventual fixation)'),
   Q('HL','The linear guess says a quarter of them should fix within a quarter of the mean time, some seven hundred fifty fixations; six do.','§The Second Objection (Day\'s own simulation)')],
 formal='''F(T) = P(τ ≤ T | eventual fixation), τ = fixation time of a new neutral mutant. Claim: ln F(T) → −π² Nₑ/T + lower-order terms.

**Derived comparison (RESULTS B2a, exact WF Markov chain, N=200):**
| G/N | exact conditional F | Day exp(−π²N/G) | exact / Day |
|---|---|---|---|
| 4 | 0.61 | 0.085 | 7× |
| 1 | 2.8e−3 | 5.2e−5 | 54× |
| 0.25 | 1.2e−14 | 7.2e−18 | 1.6e3× |
Fit (empirical, not derived): ln F_cond ≈ −π²/r + 1.5 ln(1/r) + 3.9, r = G/N, i.e. prefactor ≈ 50 r^−1.5; Day states the constant "could be wrong by two orders of magnitude in either direction without shifting the conclusion" (consistent with a ≈ 50× prefactor).
Under Reading 2 (unconditional, F/2N) the claim would be wrong in the other direction at G = 4N (0.61/400 = 1.5e−3 < 0.085); the verbatim definition above is Reading 1.
Day\'s simulation: 600,000 runs, 200 genes, ≈3,000 fixed, 6 within a quarter of the mean time: 6/3000 = 2.0e−3 (Poisson ±0.8e−3), vs linear 0.25 and vs exp(−π²) = 5.2e−5; the exact-chain value at G/N = 1 is 2.8e−3 (mapping of Day\'s "200 genes" to the script\'s N to be confirmed). Day\'s data thus sit near the exact value, ≈39× above his own formula.''',
 a_stated='Wright–Fisher diffusion; arcsine transform turns neutral drift into a symmetric random walk of length π√(2Nₑ).',a_impl='Neutral, panmictic, constant Nₑ; τ conditional on fixation; leading-order only.',
 against='None in the corpus addresses the exponent; the critics\' objection is relevance (B2d).',support='Consistent with −π² (RESULTS B2a, N-convergence at fixed r, N = 100/400/1600, reproduced by `b2a_scaling.py`: −8.33/−7.40/−5.99 vs fit −8.37/−7.40/−5.97).',
 weak='The harsher comparison (prefactor accuracy at G = 4Nₑ) judges an "of order" statement more strictly than its framing warrants (RESULTS fairness note). No citation is given for the diffusion result.',
 lit=[lit_row('Kimura & Ohta 1969','first moment (4Nₑ) only; no tail law','the tail law is Day\'s own')],
 p_claim='Exponent −π² (leading order); fill fraction far below T/4Nₑ.',
 p_opp='(RESULTS B2a) Exponent correct but an "of order" statement; exact value is orders of magnitude larger than exp(−π²N/G) at moderate G.',
 p_change='Pre-registered and already resolved for the exponent. The verbatim definition (Reading 1) removes the Reading-2 branch.',
 prereg_note='Pre-registered prediction (copied from RESULTS B2a; the check has run): the exponent is the correct leading-order short-time asymptotic; (G/N)·ln F_cond → −π².',
 check='Script: `research/checks/b2a_hard_limits_chain.py` (exact chain, no randomness) and `research/checks/b2a_scaling.py` · Result: exponent consistent with −π² (limit order N→∞ at fixed r, then r→0; limits ≈ −8.4, −7.45, −6.0 for r = 0.25, 0.5, 1). Internal verdict: holds. Review #3 corrected the limit order. Review: '+RV3,
 sim=['G/Nₑ ratio','exact chain vs asymptotic','conditional vs unconditional F'])

add(id='B2b',slug='ceiling-x-vk-g-over-16',title='Census ceiling X = (Vk + 2) G / 16 from 4Ne < G',side='day',branch='B',parent='B2',
 edges=[('supports','B2')],lb=(True,'X is the ceiling quoted in the abstract and in Day\'s blog replies'),
 sourcing='firsthand',status='extracted',v=('holds','unverifiable','contested'),
 quotes=[Q('HL','Nₑ = (4N − 2) / (Vₖ + 2)','p.4 (§The Census Ceiling)'),
   Q('HL','For a large, long-lived vertebrate the effective ceiling falls to about ten thousand individuals.','p.1 (abstract)'),
   Q('HL','The human’s is thirty-five thousand as a species, a hundred thousand as a lineage. The elephant’s is twenty-eight thousand.','p.6')],
 formal='''4Nₑ < G with Nₑ = (4N−2)/(Vₖ+2) ≈ 4N/(Vₖ+2) ⇒ N < (Vₖ+2)G/16 = X. G = T_years / g_years.

**Arithmetic audit (derived, python3 -I):**
| Species | T (My), g (y), Vₖ | G | X recomputed | Day's X | census / X |
|---|---|---|---|---|---|
| Homo sapiens (lineage) | 6.5, 25, 5 | 260,000 | 113,750 | 114,000 | 8.2e9/113,750 = 72,088 (Day 72,000) |
| H. sapiens (species window) | 2.0, 25, 5 | 80,000 | 35,000 | 35,000 | 234,286 |
| Loxodonta | 2.0, 22, 3 | 90,909 | 28,409 | 28,000 | 14.6 (Day 15) |
| Mus musculus | 1.5, 0.5, 25 | 3.0e6 | 5.06e6 | 5.1e6 | 1,975 |
| D. melanogaster | 5.0, 0.08, 400 | 6.25e7 | 1.57e9 | 1.57e9 | 637 |
Table 2 (Vₖ halved/doubled) also reproduces: human 22,500/60,000; elephant 19,886/45,455; mouse 2.72e6/9.75e6; fly 7.89e8/3.13e9.
Discrepancies: (i) the abstract's "about ten thousand" is 3.5–11× below the table's human ceilings (35,000–114,000) and 2.8× below the elephant's; (ii) with Vₖ = 5 Wright's formula gives Nₑ = 0.57 N, so the paper treats census 8.2e9 as Nₑ ≈ 4.7e9, whereas Z18525547 and the Q&A use Nₑ = 3,300–10,000 for the same census (N/Nₑ = 800,000 in the 2026-04-30 post); (iii) mouse and fly Vₖ and census values are flagged "original estimates pending a proper source".''',
 a_stated='Variance Nₑ is the relevant quantity; the lineage duration is the window; Vₖ is the least certain input (sensitivity table given).',a_impl='Panmictic, constant size over G; mean time is the criterion (the tail is handled in B2a); Wright\'s formula applies with a single Vₖ for the species.',
 against=rq('MFC','Genetic drift happens in every population and his claim otherwise is mystifying. Population size only affects which alleles are effectively neutral.',loc='comment UgyhNduYke46IStQ5pd4AaABAg (Mansfield)'),
 support='HL pre-empts three objections (window, parallelism, demes) in the text; Maruyama\'s invariance is cited for demes.',
 weak='Mansfield addresses Day\'s earlier blog sentence, not this derivation. Neither side has checked the Vₖ = 5 value for humans against Hill (1972) or the demographic literature (not retrieved).',
 lit=[lit_row('Wright (Nₑ formula)','Nₑ = (4N−2)/(Vₖ+2) as printed in HL p.4; original not retrieved','unverified'),
      lit_row('Hill 1972 (human Vₖ route per HL)','not retrieved','unverified')],
 p_claim='Every listed vertebrate census exceeds its X.',p_opp='If Nₑ/N is the empirical 0.1 (Frankham) or the human ≈ 10⁻³ ratio, the ceiling inequality is evaluated at different Nₑ and the comparison changes only by the factor Nₑ/N used.',
 p_change='A sourced Vₖ(human) and an independent Nₑ(t) would settle the inputs; no check is queued for this sub-claim beyond B2a/B1c.',
 check='Script: none specific (arithmetic only). Audit computed with python3 -I in this session. Related: B3a (Nₑ vs N).',
 sim=['Vₖ','generation time','lineage duration','census N','Nₑ/N mapping (Wright formula | fixed ratio | user)'])

add(id='B2c',slug='one-in-ten-to-78-millionth',title='"One in ten to the seventy-eight-millionth": exp(-pi^2 Ne/G) for humans and the many-loci rescue',side='day',branch='B',parent='B2',
 edges=[('supports','B2'),('depends-on','B2a')],lb=(False,'rhetorical headline number; the load is carried by B2a and B1c'),
 sourcing='firsthand',status='extracted',v=('holds','unverifiable','contested'),
 quotes=[Q('HL','Carry the exponent to the species in question. For modern humans, Nₑ across the four hundred generations of the current-census era gives Nₑ/T ≈ 1.8 × 10⁷, so the probability that a neutral mutation arising now fixes within that era is of order exp(−π² · 1.8 × 10⁷) — about one in ten to the seventy-eight-millionth.','§The Second Objection'),
   Q('HL','Ten to the fourteenth against a probability of exp(−π²Nₑ/G) leaves the expected number of completed fixations at ten to the minus seventy-eight-million all the same.','§The Second Objection')],
 formal='''**Arithmetic audit (derived, python3 -I):**
- Nₑ = 7.3e9 (HL Table 3, "census scale"), T = 400: Nₑ/T = 1.825e7 (Day 1.8e7); π² × 1.825e7 = 1.80e8 nats = 7.82e7 decades, i.e. 10^−78,000,000 (matches).
- Destined-to-fix input: 30 × 400 = 12,000 ("some ten thousand"); raw 10^14. Neither moves a 10^7.8e7 exponent.
- **Window mismatch:** the abstract says "within the generations its lineage will ever have" (G), but the computation uses a 400-generation era. With the lineage window G = 260,000 and the same Nₑ: π²Nₑ/G = 2.77e5 nats = 1.2e5 decades; with Wright Nₑ = 4.69e9: 7.7e4 decades; with Yoo ancestral Nₑ (1.98e5 / 1.32e5) and G = 260,000: exp(−7.5) = 5.4e−4 / exp(−5.0) = 6.7e−3; with Nₑ = 1.0e4 (Day's value in IR and the Q&A): exp(−0.38) = 0.68 (outside T ≪ 4Nₑ, so only indicative).
- The raw count is consistent with 8e9 individuals × ~100 new mutations × 400 generations = 3.2e14 (derived), i.e. "about ten to the fourteenth".''',
 a_stated='Nₑ at census scale for humans; the era of the current census is 400 generations; the one-in-2N chance is already folded into k = μ.',a_impl='Only mutations arising in the era contribute (ancestral fill is "drainage"); the asymptotic regime T ≪ 4Nₑ holds (400 ≪ 2.9e10, true).',
 against='RESULTS B2a/F1: this is a per-allele latency statement; for an equilibrium ancestral population the flux is μ (B1, B2d).',support='The arithmetic is internally consistent.',
 weak='The headline combines two Nₑ conventions: census-scale Nₑ here versus Nₑ = 10⁴ for ancestral humans elsewhere in Day\'s work. A critic-side counter would need the ancestral fill state (B1c), not a different exponent.',
 lit=[],p_claim='The probability that a neutral mutation arising now fixes within 400 generations is ≈ 10^−7.8e7.',p_opp='Same exponent; irrelevant to the 252,000-generation divergence, which is dominated by ancestral Nₑ (1.3e5–2e5, Yoo).',
 p_change='B1c with Nₑ(t) showing the census-scale era is ≤400 of 252,000 generations would confirm irrelevance for the count; showing a long census-scale era would support relevance.',
 check='Script: none (arithmetic). Audit computed with python3 -I in this session.',sim=['window T for the exponent','Nₑ used in the exponent','era length at current size'])

add(id='B2d',slug='parallel-fixation-second-objection',title='Second objection: fixations run in parallel; steady-state flux is mu regardless of transit; the pipeline cannot fill',side='day',branch='B',parent='B2',
 edges=[('supports','B2'),('attacks','F1')],lb=(False,'Day concedes the throughput point; the live dispute is the fill state (B1c)'),
 sourcing='firsthand',status='extracted',v=('holds','n/a','pending'),
 quotes=[Q('HL','At steady state the total flux out is μ per site regardless of how long any individual site took to traverse.','§The Second Objection'),
   Q('HL','“Nothing finishes in the species lifetime” is simply wrong as a claim about throughput, and the drift limit does not depend on it.','§The Second Objection'),
   Q('HL','The correct interpretation is narrower: the pipeline cannot fill.','§The Second Objection')],
 formal='''Day's position, in glossary terms: **throughput** at steady state = μ; the claim is about **fill state** (transient), not about latency bounding throughput. This is the same logical point as Mansfield's time between successive fixations (F1), accepted in this paper and restated in the Education post as an analogy about a machine running multiple jobs simultaneously (F1a).''',
 a_stated='Many pipes in parallel, each on its own 4Nₑ delay.',a_impl='The pipes start empty (B1c) or are refilled only by ancestral conditions (B1d).',
 against=rq('MC2','Obviously, mutations, whether neutral or not, do not have to increase in frequency throughout a population one at a time.',loc='para 22 (McCarthy)')+'\n  '+rq('MFC','The time it takes for one allele to get fixed is not important, it is the time BETWEEN successive fixations that is important.',loc='comment UgyhNduYke46IStQ5pd4AaABAg.AbQefbrLxzSAbR9n0iZNuQ (Mansfield)'),
 support='RESULTS F1 confirms that, without interference, many fixations are in flight at once and rate = 2N·U_b·u regardless of latency.',
 weak='Critics\' replies (written before HL, 2026-08-27) do not engage the "cannot fill" restatement; HL does not engage the equilibrium-start result of RESULTS B1.',
 lit=[],p_claim='Throughput is μ only once the pipe is full; before that it is μ·F(T).',p_opp='If the ancestral pipe was full (equilibrium), μ·T is delivered over T.',
 p_change='B1c.',check='Related done checks: `research/checks/b1_start_state.py`, `research/checks/f1_throughput.py` (see B1, F1).',sim=['pipe state at t=0','number of independent loci'])

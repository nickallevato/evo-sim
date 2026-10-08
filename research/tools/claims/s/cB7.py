from common import *
RV2='`research/checks/REVIEW.md#2026-10-07--correctness-review-2-sonnet-on-b0b3`'

add(id='B7',slug='neutral-fixation-probability-is-1-over-2n',title='Neutral fixation probability is 1/(2N), the starting frequency, not 1/(2Ne); Day\'s own Hard Limits paper says so',side='critic',branch='B',parent='B3',
 edges=[('attacks','B3a'),('supports','B5')],lb=(True,'decisive for the N/Nₑ leg of B3 and for B4\'s recalibration'),
 sourcing='firsthand',status='reviewed',v=('holds','accurate','supported'),
 quotes=[Q('HL','Maruyama’s invariance principle (1970, 1974) holds that under conservative migration the neutral substitution rate is exactly μ and the neutral fixation probability exactly 1/(2N)','§The Third Objection (Day\'s own paper, 2026-08-27)'),
   Q('HL','Every neutral mutation begins as a single copy in a single individual, at a frequency of 1/(2N).','§The Transit Time'),
   Q('EDU','Yes, and that’s the problem. 1/2N is the fixation probability. It tells you the chance that a given neutral mutation will eventually fix, given unlimited time.',file='day/blog-2026-10-01-the-education-of-a-population-geneticist.txt')],
 formal='''P_fix(neutral) = p₀ = 1/(2N) where p₀ is the starting frequency of the new copy (martingale/optional stopping: E[Δp] = 0 and absorption ⇒ P(fix) = p₀). Nₑ sets the timescale (4Nₑ), not the probability. This is the glossary's pinned definition.
Day's three statements of 1/(2N) in 2026 (above) sit alongside the 1/(2Nₑ) in Z18429937, Z18525547, Z18637333 and the 2026-02-04 post (B3a). Day withdrew the latter on 2026-08-27 (B3g).''',
 a_stated='Day\'s own text.',a_impl='Single-copy start; exchangeable offspring distribution (B3 check; non-exchangeable settings pending B3b).',
 against='Day\'s earlier position (B3a); Day (RESP) contests keruru\'s chains as setting covariance between who breeds and what they carry to zero (B3g discussion).',support='B3 check; keruru\'s exact chains (B7c); Kimura 1962/1969 (B7a, B7b).',
 weak='The Hard Limits paper still defines X using Nₑ ≈ 0.57 N while assuming 1/(2N) (B2b); the critics have not tested a non-exchangeable reproduction law (B3b).',
 lit=[lit_row('Kimura 1962','"if we let s → 0 in (10), we obtain U = 1/2N, the result known for a neutral gene."','verified-accurate'),
      lit_row('Kimura & Ohta 1969','"the remaining minority (fraction 1/2N) spread over the entire population (i.e. reach fixation)"','verified')],
 prereg_note='Pre-registered prediction (copied from RESULTS B3; the check has run).',
 p_claim='(Critic) P_fix = 1/M for every Nₑ; t_fix scales with Nₑ.',p_opp='(Day, pre-retraction) P_fix = 1/(2Nₑ).',p_change='A neutral non-exchangeable model with P_fix ≠ p₀ (B3b).',
 check='Script: `research/checks/b3_N_vs_Ne.py` (seed 13) · Result: P_fix = 0.00250/0.00252/0.00257/0.00248/0.00257 vs 1/(2N) = 0.00250 for Nₑ = 200/160/100/40/19; Day\'s 1/(2Nₑ) would give 0.0025–0.0268. Provisional (pending B3b). Review: '+RV2,
 sim=['starting-frequency definition','Nₑ via variance'])

add(id='B7a',slug='kimura-1962-fixation-probability',title='Kimura 1962: U = 1/2N for a neutral gene; approximately 2s for an advantageous one',side='literature',branch='B',parent='B7',
 edges=[('supports','B7'),('attacks','B3a')],lb=(False,'primary-literature anchor for B7 and for F4 (2s)'),
 sourcing='firsthand',status='reviewed',v=('n/a','partial','n/a'),
 quotes=[Q('K62','The probability of fixation of an individual mutant gene is obtained from (8) by putting p = 1/(2N).','p.715, Eq. 10'),
   Q('K62','if we let s → 0 in (10), we obtain U = 1/2N, the result known for a neutral gene.','p.716',frags=['we obtain U = 1/2N,','the result known for a neutral gene']),
   Q('K62','where N is the number of reproducing individuals in the population.','p.714, Eq. 6'),
   Q('K62','the probability of ultimate survival of an advantageous mutant gene is approximately twice the selection coefficient','p.716 (HALDANE 1927)')],
 formal='''Kimura 1962, genic selection: u(p) = (1 − e^{−4Nsp})/(1 − e^{−4Ns}) (Eq. 8); at p = 1/(2N): U = (1 − e^{−2s})/(1 − e^{−4Ns}) (Eq. 10); for small |s|: U = 2s/(1 − e^{−4Ns}) (Eq. 11); U → 1/2N as s → 0; U ≈ 2s for large positive Ns (equations reconstructed from the OCR text layer, which shows only fragments).
**Fidelity note (new, from reading the paper):** the 1962 model has a single N, the number of reproducing individuals, which enters both the variance V = x(1−x)/(2N) (Eq. 7) and the starting frequency p = 1/(2N). The paper therefore does not itself distinguish census from variance-effective size; its introduction recalls that Kimura (1957) expressed U in terms of the initial frequency p, the selection coefficients and the effective population number. The fidelity ledger's gloss that N is the census number is therefore stronger than the paper. The critics' reading (B7) rests on P_fix = initial frequency (a martingale property, independent of this paper) and on Day's own 1/(2N) statements (B7); this paper supports 1/2N rather than 1/2Nₑ only in the sense that the formula is written with the starting-frequency N and the model has no separate Nₑ.''',
 a_stated='Random mating, genic selection, diffusion approximation; N reproducing individuals.',a_impl='N = variance size = counting size (ideal population).',
 against='Day: Kimura 1962 is cited by Day for ≈ 2s (accurate, ledger) and for "1/(2Nₑ)" (misread, ledger).',support='Ledger: verified-accurate for ≈2s; verified-misread for 1/(2Nₑ).',
 weak='The ledger\'s census gloss; see the fidelity note.',lit=[lit_row('Kimura 1962','see Statement','accurate for 1/2N and ≈2s; partial for the census/Nₑ distinction')],
 p_claim='U = 1/2N (neutral).',p_opp='U = 1/2Nₑ (Day, pre-retraction).',p_change='n/a (primary text).',check='Script: none. Quotes are from the user-downloaded PDF via pdftotext (spacing in the extraction is corrupted, e.g. "byputtingp"; quotes are spacing-normalised).',sim=['—'])

add(id='B7b',slug='kimura-ohta-1969-4ne-and-fraction-1-over-2n',title='Kimura & Ohta 1969: neutral fixation takes about 4Ne generations; the fraction 1/2N fix',side='literature',branch='B',parent='B7',
 edges=[('supports','B7'),('supports','B1a')],lb=(False,'source of the 4Nₑ transit time used throughout B1/B2; also of the 1/2N fraction'),
 sourcing='firsthand',status='reviewed',v=('n/a','accurate','n/a'),
 quotes=[Q('KO69','a single mutant gene, if it is selectively neutral, takes about 4Ne generations until fixation in a population of effective size Ne.','Summary, p.770 (also Eq. 15, p.766)',frags=['a single mutant gene, if it is selectively neutral, takes about','until fixation in a population of effective size']),
   Q('KO69','the remaining minority (fraction 1/2N) spread over the entire population (i.e. reach fixation) taking a very large number of generations.','p.769',frags=['spread over the entire population (i.e. reach fixation) taking a','very large number of generations','the remaining minority']),
   Q('KO69','Since the ratio Ne/N is around 0.8 in man (CROW 1954), a single mutant gene which appeared in a human population will be lost from the population on the average in about 1.6 log_e 2N generations.','p.769',frags=['is around 0.8 in man','a single mutant gene','which appeared in a human population will be lost from the population on the','average in about 1.6'])],
 formal='''t̄(0) = 4Nₑ (Eq. 15), conditional on fixation, for the variance effective number Nₑ; first moment only. The paper keeps N and Nₑ distinct (for man it takes Nₑ/N ≈ 0.8), uses Nₑ for the time and N for the fraction that fix (1/2N). Not in this paper (ledger): SD ≈ 2.15Nₑ (our B0.2 simulation: ≈2.1N); any statement about recombination (the word occurs 0 times).''',
 a_stated='Single locus, variance effective size.',a_impl='Single locus; no linkage.',against='Day cites it also for the statement that fixation time does not depend on recombination (misattribution; the word does not occur in the paper, ledger).',
 support='RESULTS B0.2: conditional mean t_fix/N = 3.908 (N=50), 4.006 (N=200) vs diffusion 3.980/3.995.',weak='n/a',
 lit=[lit_row('Kimura & Ohta 1969','see Statement','accurate for 4Nₑ; accurate (critics) for 1/2N fraction; not found: SD; misattribution: recombination')],
 p_claim='t̄ = 4Nₑ for neutral alleles that fix.',p_opp='n/a',p_change='n/a',check='Script: `research/checks/baseline_textbook.py` B0.2 · Result: conditional mean t_fix/N 3.908 (N=50), 4.006 (N=200); SD ≈ 2.105–2.108 N. Review #2 corrected the target to the diffusion value at p = 1/(2N). Review: '+RV2,sim=['Nₑ','4Nₑ transit display'])

add(id='B7c',slug='keruru-retraction-census-n-cancels',title='keruru (former ally): supply is 2N mu with census N; fixation probability is exactly 1/(2N_census); claim withdrawn',side='ally',branch='B',parent='B7',
 edges=[('attacks','B3a'),('supports','B7')],lb=(False,'corroborated by Day\'s own concession (B3g)'),
 sourcing='firsthand',status='reviewed',v=('holds','accurate','supported'),
 quotes=[Q('KRE','Mutation supply is 2Nμ with N the census count — mutations occur in gametes, and every reproducing individual contributes gametes.','para 6'),
   Q('KRE','The fixation probability of a single new mutant in both chains: exactly 1/(2N_census), to fifteen decimal places.','para 9'),
   Q('KRE','The claim about the substitution rate is withdrawn. The claim about the ancient-DNA finding is withdrawn.','para 36'),
   Q('KRB','k = 2Nμ × 1/(2Ne) = (N/Ne)μ','para 28 (the pre-retraction statement, in a post that is "mainly claude" per the author)')],
 formal='''Exact finite Markov chains (Wright–Fisher and a sweepstakes model with Nₑ 5.6× lower at the same census): P_fix = 1/(2N_census) to 15 decimals; code deposited per the author (not retrieved). Martingale argument: neutral frequency is a bounded martingale, so P_fix = p₀. Consistent with `research/checks/b3_N_vs_Ne.py` (RESULTS B3). Second leg (aDNA zero fixations expected under neutrality, ≈10⁻²⁹ expected fixations, Nₑ ≈ 10⁴) is branch C; Day contests it as circular (B3h).''',
 a_stated='Census N cancels; Nₑ never enters.',a_impl='Exchangeable offspring law in the chains (Day: sweepstakes parent drawn uniformly at random, setting a covariance to zero).',
 against=rq('RESP','And most crucially, his work never contains a census population.',loc='Day, 2026-08-27 (on keruru\'s aDNA leg)')+'; Day (B3h).',
 support='Day concedes the algebra (B3g); B3 check.',weak='LLM-assisted author; the January review (KR-08/KR-09) endorsed the thesis from an LLM transcript and is superseded by this post; chains and code were not retrieved.',
 lit=[lit_row('Kimura 1962','U = 1/2N','verified')],
 prereg_note='Pre-registered prediction (copied from RESULTS B3; the check has run).',
 p_claim='(keruru, B3) P_fix = 1/M for every Nₑ.',p_opp='(Day, Feb) P_fix = 1/(2Nₑ).',p_change='Obtaining and re-running keruru\'s chains with a covariance between breeding and carrying.',
 check='Script: `research/checks/b3_N_vs_Ne.py` · Result: see B7. Chains: not retrieved.',sim=['sweepstakes events','Nₑ via reproductive skew'])

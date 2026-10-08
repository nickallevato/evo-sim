from common import *
RV3='`research/checks/REVIEW.md#2026-10-07--review-3-sonnet-correctness--two-sided-steelman-of-b1b-b2a-f1`'

add(id='B4',slug='clock-recalibration-200-580-kya',title='Molecular clock recalibration: CHLCA collapses from 6-7 Mya to 200-580 kya via N/Ne',side='day',branch='B',parent='B',
 edges=[('supports','B'),('depends-on','B3a')],lb=(False,'a consequence of B3a, which Day withdrew on 2026-08-27; MITTENS counts (A) use 252,000 generations regardless'),
 sourcing='firsthand',status='extracted',v=('holds','unverifiable','contested'),
 quotes=[Q('NNE','The consensus molecular clock estimate of 6–7 Mya collapses to 200–580 kya, with the most plausible demographic parameters yielding 200–360 kya.',file='day/zenodo-18525547.txt',note='abstract'),
   Q('NNE','t_{actual} = t_{clock} × 2 / [(N_{h}/N_{e,h}) + (N_{c}/N_{e,c})]          (7)',file='day/zenodo-18525547.txt')],
 formal='''D = μ t [(N_h/N_e,h) + (N_c/N_e,c)] (Eq. 6) set equal to the clock's D = 2μ t_clock ⇒ Eq. (7). Inputs: Nₑ,h = 3,300 (aDNA drift variance, branch C), Nₑ,c = 33,000 (F_ST across chimp subspecies), census N_h ∈ {50k, 100k}, N_c ∈ {300k, 1M}.

**Arithmetic audit (derived, python3 -I):** Table 2 of the paper reproduces: (100k,300k): N/Nₑ = 30.3 + 9.1 → 305/355/457 kya for clock 6/7/9 My ✓; (100k,1M): 198/231/297 ✓; (50k,300k): 494/577/741 ✓ (paper 494/577/741); (50k,1M): 264/308/396 ✓. "200–580 kya" is the 6–7 My clock range (min 198, max 577); the 9 My column reaches 741.
**Input sensitivity (derived):** the two parameter sets Day uses for the same human census range disagree: here Nₑ,h = 3,300 for N = 100,000 (N/Nₑ = 30), while Z22129121 and the 2026-10-01 post imply Nₑ = 0.57 N (57,000). With Yoo 2025 ancestral Nₑ (198,000 / 132,000) and census 100,000 the ratio is 0.51 / 0.76 per lineage and Eq. (7) gives 12.5 / 8.3 My (older, not younger) for a 6.3 My clock. Also, Eq. (7) assumes constant N/Nₑ over the whole window.
The paper's later claim "Ne ≤ N by definition" (Z18637333) is not a definition: Wright's formula Nₑ = (4N−2)/(Vₖ+2) gives Nₑ ≈ 2N at Vₖ = 0.''',
 a_stated='k = μ(N/Nₑ) (B3a), with clock-independent Nₑ.',a_impl='Constant N/Nₑ over millions of years; one census figure per lineage; the same fixation-probability premise that Day retracted on 2026-08-27 (B3g).',
 against=rq('HOS','the neutral theory of evolution cannot explain common ancestry between humans and chimps at all based on genome-wide nucleotide differences between the two species, since the neutral theory is used in the first place to date the assumed time of divergence.',loc='PDF p5 (Hössjer; he agrees the dating is neutral-theory based, but takes k = dμ with census N)'),
 support='Keightley 2012: pedigree μ about twofold lower than divergence-based estimates (k > μ in direction, ×2 not ×15–150); keruru (KR-05): "closer to twice that".',
 weak='Hössjer does not adopt k = μN/Nₑ; keruru\'s observation is about a factor 2 and he calls it unreconciled. The dependence on Z18525547\'s Nₑ,h = 3,300 is branch C.',
 lit=[lit_row('Frankham 1995 (cited for N > Nₑ)','not retrieved','unverified'),
      lit_row('Takahata 1993; Harpending 1998 (cited for Nₑ ≈ 10⁴)','not retrieved','unverified'),
      lit_row('Langergraber 2012','"We date the human-chimpanzee split to at least 7-8 million years"','verified-misread when cited as 6–7 My (ledger)')],
 p_claim='Divergence time 15–150× shorter than the clock date.',p_opp='With P_fix = 1/(2N) the clock rate is μ and Eq. (7) reduces to t_actual = t_clock.',
 p_change='A reproduction of the Nₑ,h = 3,300 estimate from drift variance under a model that includes structure (branch C).',check='Script: none (arithmetic audit above, python3 -I). Direct simulation of two-lineage divergence: B4a (proposed).',
 sim=['t_clock','census N per lineage','Nₑ per lineage','N/Nₑ held constant or varying'])

add(id='B4a',slug='two-lineage-divergence-with-ils',title='Pairwise divergence = 2 mu T + theta_anc: two-lineage forward simulation with incomplete lineage sorting',side='literature',branch='B',parent='B4',
 edges=[('depends-on','B6'),('depends-on','B1b'),('attacks','B1a')],lb=(True,'decides whether fixed-difference deficits (B1) apply to the observable that is actually compared (sequence divergence)'),
 sourcing='firsthand',status='extracted',v=('pending','n/a','pending'),
 quotes=[Q('CSAC','t 1 is constant across loci (,6-7 million years38), t 2 is a random variable that fluctuates across loci (with a mean that depends on population size and here may be on the order of 1-2 million years39)','Main text, "Genome-wide rates" (extraction renders "~" as ","; t1 = time since speciation, t2 = ancestral coalescence time)'),
   Q('IR','where D is the number of neutral differences and the factor of 2 accounts for both lineages.','§5 The Circularity'),
   Q('IR','Under coalescent theory, the expected pairwise divergence contributed by ancestral polymorphism is θ = 4Nₑμ per site.','p.3 (§3)')],
 formal='''E[d] = 2μT + 4Nₑ,anc μ per site (T in generations; coalescence in the ancestor at mean 2Nₑ,anc generations), where d is the difference between one haplotype from each species (includes polymorphism); fixed differences are the subset fixed in both.

**Derived illustration (python3 -I; μ = 1.2e-8 pedigree, 25 y/gen, T = 252,000, L = 3.2e9):** 2μT = 6.05e-3 per site (19.4M sites). θ_anc = 4Nₑμ: Nₑ = 1.0e4 → 4.8e-4 (1.5M sites); 1.32e5 (Yoo HCG) → 6.3e-3 (20.3M); 1.98e5 (Yoo HCB) → 9.5e-3 (30.4M). Totals: 0.65%, 1.24%, 1.56% vs observed 1.23% (CSAC, including polymorphism; fixed ≤ 1.06%). With Nₑ = 1e4, matching 1.23% requires T ≈ 492,500 generations (12.3 My at 25 y). These are illustrations of how the ancestral term depends on the Nₑ input, not verdicts.

**Proposed check B4a (not yet run; pre-registered here):** forward Wright–Fisher, ancestral Nₑ ∈ {1e4, 3e4, 1.32e5, 1.98e5} for 8Nₑ generations (equilibrium), split into two lineages (Nₑ = 1e4 each, constant), run T ∈ {50k, 100k, 252k} generations, plus a third outgroup lineage for ILS; sample one genome per species and n = 10 per species; report (i) mean pairwise d vs 2μT + θ_anc, (ii) fixed vs polymorphic fraction of d, (iii) fraction of gene trees discordant with the species tree vs (2/3)exp(−T_int/2Nₑ,anc), (iv) the B1b-style fixed-substitution count per lineage.''',
 a_stated='Day (IR): ancestral polymorphism is a rounding error (θ = 0.35% of 410M, Nₑ = 10⁴).',a_impl='Day: Nₑ,anc = 10⁴; critics: Nₑ,anc ≈ 1.3–2×10⁵ (Yoo), which makes θ_anc a first-order term.',
 against='n/a (check proposal)',support='n/a',weak='Yoo 2025\'s Nₑ,anc derives from coalescent inference with its own μ and generation time assumptions (see B3h).',
 lit=[lit_row('Chimpanzee Sequencing and Analysis Consortium 2005','"we estimate that polymorphism accounts for 14-22% of the observed divergence rate"','verified (ledger)'),
      lit_row('Yoo 2025','Nₑ,anc = 198,000 (HCB) and 132,000 (HCG)','verified (ledger)'),
      lit_row('Scally 2012','"In 30% of the genome, gorilla is closer to human or chimpanzee than the latter are to each other"','context for ILS')],
 p_claim='(Day) ancestral term negligible; fixed count is lowered by the empty-pipe correction.',
 p_opp='(standard theory, CSAC) pairwise divergence includes a coalescent term that does not depend on fixation latency; the fixed-substitution count is not the observable.',
 p_change='If the simulated d matches 2μT + θ_anc to within SE and the fixed-count deficit does not alter d, Day\'s empty-pipe correction does not apply to the observable (B1a internal verdict stands, relevance falls). If d falls below the standard prediction by about μL·4Nₑ, Day is supported.',
 check='Script: proposed `research/checks/b4a_two_lineage_ils.py` (not yet written) · Result: none. Required by REVIEW.md review #3 (B1b caveat) and queued.',
 sim=['ancestral Nₑ','post-split Nₑ per lineage','T','μ','sample sizes','outgroup branch length','observable (pairwise | fixed | ILS fraction)'])

add(id='B4b',slug='chlca-68-kya',title='CHLCA recalibrated from 6.5 Mya to 68 kya (census 600,000; Biraben 2003)',side='day',branch='B',parent='B4',
 edges=[('revises','B4')],lb=(False,'extreme end of the recalibration; superseded by the 2026-05-07 revision (B4c)'),
 sourcing='firsthand',status='extracted',v=('holds','unverifiable','contested'),
 quotes=[Q('EDT','recalibrates the CHLCA from 6.5 Mya to 68 kya',file='day/zenodo-18637333.txt',note='abstract'),
   Q('EDT','At the midpoint of 600,000, the consensus molecular clock date of 6.5 Mya compresses to 68 kya.',file='day/zenodo-18637333.txt')],
 formal='''Same Eq. (7) with N_h = 600,000 (Biraben 2003), N_c = 300,000, Nₑ,h = 3,300, Nₑ,c = 33,000: N_h/Nₑ,h = 181.8, N_c/Nₑ,c = 9.1; t = 2 × 6.5 My / 190.9 = 68.1 kya ✓ (derived). Alternate census 100–300k: 330–130 kya ✓ (paper "130–330 kya").
Differences from Z18525547 (one week earlier): human census 600,000 vs 50–100k; clock date 6.5 vs 6–7 (9); outputs 68 kya vs 198–741 kya.''',
 a_stated='Census 500,000–700,000 for the whole Homo ergaster/erectus lineage (Biraben 2003) is the right N for mutation supply.',a_impl='Same as B4; plus that a census spanning many contemporaneous subspecies all contribute to the ancestral lineage\'s supply while drift acts at Nₑ,h = 3,300.',
 against='See B4 and B3g.',support='n/a',weak='Biraben (2003) not retrieved; the ≤ definition claim is incorrect (see B4).',
 lit=[lit_row('Biraben 2003 (as cited)','500,000–700,000 total hominids (as cited by Day)','unverified'),
      lit_row('Sjödin et al. 2012 (as cited)','100,000–300,000 H. sapiens census (as cited by Day)','unverified')],
 p_claim='68 kya.',p_opp='No recalibration (B3g).',p_change='n/a',check='Script: none. Arithmetic computed in python3 -I.',sim=['census N per lineage'])

add(id='B4c',slug='chlca-250-kya-to-1-3-mya',title='Day (2026-05-07): CHLCA falls in 250 kya to 1.3 Mya, not 68-330 kya',side='day',branch='B',parent='B4',
 edges=[('supersedes','B4b'),('revises','B4')],lb=(False,'bookkeeping of a revised range; mechanism not given in the harvested text'),
 sourcing='firsthand',status='extracted',v=('pending','n/a','pending'),
 quotes=[Q('RET','the CHLCA event falls somewhere in the 250 kya to 1.3 Mya range rather than the 6.3 Mya presently assumed. But it cannot be as recent as the lower end of the 68 kya to 330 kya range',file='day/blog-2026-05-07-a-retraction-and-a-revision.txt'),
   Q('RET','my error was in interpreting its output as a constraint on total k. Once corrected, Term 3 still limits adaptive substitution rate at ~10⁻¹², but total substitution rate is only governed by Terms 1 and 2',file='day/blog-2026-05-07-a-retraction-and-a-revision.txt')],
 formal='''Version chain (versions ledger, "CHLCA"): 6.3–9 My → 200–580 kya (Z18525547, 2026-02-08) → 68 kya (Z18637333, 2026-02-14) → 68–330 kya (Z19984826 Kimura calculator, per retraction text) → 250 kya–1.3 Mya (2026-05-07). The retraction is of Term 3 (Haldane cost limit as a bound on total k) in Z19984826; the CHLCA range moves because of it. The harvested post gives no computation for 250 kya–1.3 Mya. The N/Nₑ mechanism behind the Feb 2026 values was withdrawn later (B3g, 2026-08-27).''',
 a_stated='A three-term minimum: input flux, polymorphism throughput ceiling, selection-cost limit.',a_impl='Terms 1 and 2 have a defined value for the human lineage (not shown in the harvested text).',
 against='n/a',support='n/a',weak='No independent engagement in the corpus.',lit=[lit_row('Haldane 1957 via Nunney 2003','~1 substitution per 300 generations','verified-accurate via Nunney only')],
 p_claim='CHLCA within 250 kya–1.3 Mya.',p_opp='Dates ~6 My (Yoo: 5.5–6.3; Langergraber: ≥7–8).',p_change='Day\'s Z19984826 successor text showing Terms 1 and 2.',check='Script: none.',sim=['divergence-time prior'])

add(id='B4d',slug='clock-circularity-day',title='Dating by k = mu is circular: the divergence date is derived from the identity it is cited to confirm',side='day',branch='B',parent='B4',
 edges=[('supports','B4')],lb=(False,'rhetorical support for the irrelevance claim; MITTENS counts do not use it'),
 sourcing='firsthand',status='extracted',v=('pending','partial','contested'),
 quotes=[Q('IR','The circularity is complete. The divergence date was calculated from k = μ. The mutation rate was adjusted to keep the date consistent with k = μ.','§5 The Circularity'),
   Q('IR','The identity is its own evidence. At no point does an independent measurement enter the loop.','§5')],
 formal='''T = D/(2μ) (IR §5). Claim: μ was phylogenetically calibrated, then replaced by pedigree μ with the date pushed back "to maintain consistency".
Analysis (derived reasoning): a date from pedigree μ and generation time is independent of the fossil calibration but not of the *assumption* k = μ per generation; and the older direction is what Keightley 2012 reports (pedigree μ about twofold below divergence-based rates). Langergraber 2012 derives "at least 7-8 million years" without fossil calibration, using pedigree μ and wild-chimp generation times, so the loop is not closed by a measurement of the date.''',
 a_stated='The molecular clock\'s sole use is calibration; it is circular.',a_impl='The mutation rate used in recent dating is not independently measured.',
 against=rq('HOS','the neutral theory of evolution cannot explain common ancestry between humans and chimps at all based on genome-wide nucleotide differences between the two species, since the neutral theory is used in the first place to date the assumed time of divergence.',loc='PDF p5 (Hössjer, an ally, makes the same point; B4f)'),
 support='Keightley 2012 (the rate fell, the date rose).',weak='Both McCarthy (B4e) and Hössjer (B4f) state the dependence; none of the three give a dated-values chain with references.',
 lit=[lit_row('Keightley 2012','"Direct estimates from genome sequencing of relatives suggest that μ is about 1.1 × 10(-8), which is about twofold lower than estimates based on the human-chimp divergence."','verified-partial (abstract only)'),
      lit_row('Langergraber 2012','"We date the human-chimpanzee split to at least 7-8 million years and the population split between Neanderthals and modern humans to 400,000-800,000 y ago."','verified; Day cites it as 6–7 My (misread, ledger)')],
 p_claim='The date of ~6–8 My carries no independent evidence for k = μ.',p_opp='Fossil-calibrated and pedigree-based dates agree within a factor ~1.5; the agreement is evidence for the assumption.',p_change='Showing a date-independent test of k = μ (e.g., Ne-independent comparison of closely related pairs with known split dates).',
 check='Script: none.',sim=['μ source','generation time','calibration'])

add(id='B4e',slug='mccarthy-dates-use-kimura',title='McCarthy: the 6-9 My human-chimp dates are based on Kimura\'s neutral-theory result',side='critic',branch='B',parent='B4',
 edges=[('supports','B4d')],lb=(False,'critic\'s side comment explaining why Day\'s inputs "will be consistent"; no calculation'),
 sourcing='firsthand',status='extracted',v=('pending','unverifiable','contested'),
 quotes=[Q('MC2','population geneticists actually use Kimura’s neutral-theory result to date the human–chimpanzee divergence.','para 27')],
 formal='''Context (para 27): "of course those dates are going to be consistent with the mutation rate and observed number of mutations." No citation. Same logical content as B4d, offered by a critic to argue that Day\'s use of the dates is circular.''',
 a_stated='Dates are based on k = μ.',a_impl='All dates; not distinguishing fossil-calibrated, pedigree-based and phylogenetic ones.',against='Langergraber 2012 (fossil-independent).',support='Hössjer (B4f).',
 weak='McCarthy also treats N = Nₑ and all-neutral in his own calculation (B5a).',lit=[],p_claim='Dates are model-dependent.',p_opp='Dates have independent fossil support (disputed).',p_change='n/a',check='Script: none.',sim=['—'])

add(id='B4f',slug='hossjer-neutral-theory-dates-divergence',title='Hossjer (ally): neutral theory cannot explain common ancestry because it is used to date the divergence',side='ally',branch='B',parent='B4',
 edges=[('supports','B4d')],lb=(False,'cited by Day (IR §5) as an independent confirmation; no calculation'),
 sourcing='firsthand',status='extracted',v=('pending','unverifiable','contested'),
 quotes=[Q('HOS','the neutral theory of evolution cannot explain common ancestry between humans and chimps at all based on genome-wide nucleotide differences between the two species, since the neutral theory is used in the first place to date the assumed time of divergence.','PDF p5, §3'),
   Q('HOS','I agree with this conclusion, also after adjusting the MITTENS equation for the different mutation rates of humans and E. coli.','PDF p3 (scope: the MITTENS selection argument, not the neutral calculation)')],
 formal='''Hössjer\'s neutral calculation (his Eq. 3.1): F_hum = L·d·μ·t_div = 3e9 × 0.45 × 1.25e-8 × 450,000 = 7.6M (derived: 3e9 × 1.25e-8 = 37.5; × 0.45 = 16.9; × 450,000 = 7.59e6 ✓) per lineage, "very close to the second extended MITTENS equation". His E. coli check: 1/(L·μ) = 1/(4.6e6 × 1e-10) = 2,170 generations vs Day's 1,600 (derived ✓). He uses 2Nμd × 1/(2N) = dμ (census N), i.e. he does not adopt B3a.''',
 a_stated='The rate is dμ for neutral sites; the date depends on the neutral rate.',a_impl='Date = D/(2μ); μ has been adjusted (phylogenetic → pedigree).',
 against='Day\'s own IR gives Hössjer as a corroborating reviewer of B4d; Hössjer notes that the dating point "is not addressed in Vox Day\'s book".',
 support='Day (IR §5).',weak='Hössjer\'s 7.6M includes the d = 0.45 factor in the neutral supply; without it 16.9M vs 20M (balance ledger). His d use is Day\'s turnover coefficient (branch A4), not a neutral-theory result.',
 lit=[lit_row('Keightley 2012','pedigree μ ≈ 1.1e-8','verified-partial')],p_claim='Neutral theory cannot support common descent by itself.',p_opp='The dating circularity concerns the age, not whether the count of differences is neutral-compatible.',p_change='n/a',
 check='Script: none (arithmetic only).',sim=['μ','d (A4)'])

add(id='B4g',slug='keruru-pedigree-vs-fossil-calibrated-twice',title='keruru: fossil-calibrated rate is about twice the pedigree rate (unreconciled)',side='ally',branch='B',parent='B4',
 edges=[('supports','B4d')],lb=(False,'auxiliary; magnitude (×2) is far from Day\'s ×15–150 and ×32.3'),
 sourcing='firsthand',status='extracted',v=('pending','unverifiable','contested'),
 quotes=[Q('KRE','Calibrating against the fossil-dated human–chimpanzee split gives something closer to twice that.','para 21 (context: pedigree rate ~1.2e-8; author calls this unreconciled)')],
 formal='''Pedigree μ ≈ 1.2e-8 (Kong 2012) vs a fossil-calibrated phylogenetic rate ≈ 2× (keruru; Keightley 2012 reports the same twofold). With 6.3 My and 25 y/generation, the observed 1.23% difference gives a rate of 1.23%/(2 × 252,000) = 2.4e-8 per generation (derived, includes polymorphism and ancestral coalescence), i.e. 2× the pedigree rate. Subtracting the ancestral term θ_anc = 6.3e-3 (Nₑ = 1.32e5, B4a) leaves 5.97e-3/(2 × 252,000) = 1.2e-8, equal to pedigree μ (derived, one-point illustration).''',
 a_stated='The ×2 discrepancy is unreconciled.',a_impl='All divergence is accumulated after the split; ancestral coalescence ignored.',against='Ancestral coalescence (B4a) can account for the ×2 if Nₑ,anc ≈ 1.3×10⁵.',support='Keightley 2012.',
 weak='The derived one-point reconciliation depends on Nₑ,anc and on μ, T, g; it is a proposal for B4a, not a result.',lit=[lit_row('Keightley 2012','see B4d','verified-partial')],
 p_claim='There is an unreconciled ×2.',p_opp='Ancestral polymorphism and generation-time conventions account for it.',p_change='B4a.',check='Script: proposed B4a.',sim=['θ_anc term','generation time'])

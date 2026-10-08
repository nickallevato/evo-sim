import re,sys,os
R='/home/na/projects/evo-sim/sources/raw/day'
def norm(s):
    s=s.replace('“','"').replace('”','"').replace('’',"'").replace('‘',"'")
    s=re.sub(r'\^\{([^}]*)\}',r'^\1',s); s=re.sub(r'_\{([^}]*)\}',r'_\1',s)
    s=s.replace('­','')
    return re.sub(r'\s+',' ',s).strip()
Z='https://zenodo.org/records/'
B='https://voxday.net/'
def zsrc(i): return (f'Z{i}',f'zenodo-{i}.txt',Z+str(i))
def bsrc(d,slug,path): return (f'B{d}-{slug}',f'blog-{d}-{slug}.txt',B+path)
Q=[]
def q(topic,src,text,note='',flag=''): Q.append((topic,src,text,note,flag))

mx=bsrc('2019-02-07','maximal-mutations','2019/02/07/maximal-mutations/')
q('MITTENS 2019: bacteria row',mx,'BACTERIA Years: 3,800,000,000 Years per generation: 0.000071347 (37.5 mins per generation) Generations per fixed mutation: 1600','Original post; table also lists MAMMALS (29,070)')
q('MITTENS 2019: source of 1600',mx,'Source: Sequencing of 19 whole genomes detected 25 mutations that were fixed in the 40,000 generations of the experiment. NATURE, 2009')
q('MITTENS 2019: CHLCA row (125)',mx,'CHLCA Years: 9,000,000 Years per generation: 20 Generations per fixed mutation: 1600 (Note: 8170 generations fastest Y-chromosomal lineage observed and extrapolated.) Years per fixed mutation: 32000 Maximum fixed mutations: 125','Table value 125; 9,000,000/32,000 = 281.25 (derived), see next quote','Table "125" vs text "562" vs 281 (450,000/1600)')
q('MITTENS 2019: 562 arithmetic',mx,'there have been 450,000 chimp and human generations since the CHLCA. Based on the number of mutations observed fixing in parallel in the Nature study, that would permit 562 total fixed mutations in that time frame. Which is only 29,999,438 short of the approximate number observed.','450,000/1600 = 281.25 (derived); 562 = 2 x 281 (derived). Post does not state the doubling.','562 vs 125 vs 281')
q('MITTENS 2019: required fixations 15M+15M',mx,'it requires a minimum of 15,000,000 mutations to become fixed in the human population, and another 15,000,000 mutations to become fixed in the chimpanzee population')

dq=bsrc('2026-02-04','response-to-dennis-mccarthy-round-2','2026/02/04/response-to-dennis-mccarthy-round-2/')
q('MITTENS formula (blog 2026-02-04) - first appearance in harvested corpus',dq,'F_max = (t_div × d) / (g_len × G_f) F_max = maximum achievable fixations t_div = divergence time (in years) g_len = generation length (in years) d = Selective Turnover Coefficient G_f = generations per fixation','Introduced in the post as: "This is the core equation that is integral to MITTENS, which McCarthy still has not addressed". Zenodo texts use the equivalent "Achievable = (Generations x d) / G_f" (Z18441321, Z18452504); the F_max/t_div/g_len notation appears in no Zenodo text harvested')
q('Required fixations in this post: 20 million',dq,'400,000 generations x 50 fixed mutations per generation = 20 million fixed mutations.','This is McCarthy\'s calculation as quoted by Day (secondhand within the post)')

z1=zsrc(18165980)
q('MITTENS v2025 (Z18165980): headline parameters',z1,'requiring approximately 20 million fixations on the human lineage—we calculate that natural selection can accomplish only 91 fixations given 146,250 effective generations (using the empirically-derived Selective Turnover Coefficient d = 0.45 from ancient DNA time series) and 1,600 generations per fixation (from the E. coli Long-Term Evolution Experiment).','Abstract; docx, no page numbers')
q('MITTENS v2025: arithmetic',z1,'Effective generations = 325,000 × 0.45 = 146,250 Fixation time: ~1,600 generations per fixation under strong selection (E. coli LTEE^3). Achievable fixations: 146,250 / 1,600 = 91 fixations Shortfall: 20,000,000 / 91 = 219,780-fold')
q('d source loci (Z18165980)',z1,'Three independent loci (LCT, SLC24A5, HERC2) yielded d = 0.45 ± 0.08^2.','Methods section','loci differ from Z18166234 (LCT, SLC45A2, TYR)')
q('Bernoulli Barrier p^n and ~10^-34,000,000 (Z18165980)',z1,'For n = 20,000,000 fixations (human-chimp divergence, human lineage) and p = 0.02: P(all) ≈ 0.02^20,000,000 ≈ 10^−34,000,000','This is where 0.02^(2x10^7) appears; Z18167588 does not contain it','PLAN.md attributes to Z18167588; actually Z18165980')
q('MITTENS v2025: divergence 40M SNV/20M',z1,'Genetic divergence: ~40 million single-nucleotide variants; ~20 million fixations required on human lineage. Time available: 6–7 million years at 20 years/generation = 300,000–350,000 nominal generations.')

z3=zsrc(23003785)
q('MITTENS 3.0 (Z23003785): abstract headline',z3,'The result for non-mutator populations is 1,322 generations per fixation at 60,000 generations — cross- validated at 893 generations per fixation by clone-pair analysis at 50,000 generations.','PDF hyphenation "cross- validated" preserved','')
q('MITTENS 3.0: parameters 205M / 252,000 / shortfall',z3,'Applied to human-chimpanzee divergence (205 million required fixations on the human lineage across 252,000 available generations), the shortfall is 1,075,000-fold for non-mutators and 104,873-fold across all twelve populations including hypermutators.','No d term appears in the 3.0 text (searched "turnover"/"d ="): achievable = 252,000/1,322 = 191 (derived)')
q('205M / 410M derivation (Z23003785 s7.1)',z3,'approximately 35 million SNVs, 1,140 interspecific inversions, and approximately 187 megabases of structurally divergent regions, for a total of approximately 410 million genomic differences. Apportioned symmetrically to the human lineage this yields approximately 205 million required fixations.','35M + 187M != 410M as written (the text does not show the arithmetic); units mix SNVs, events and megabases','bp-vs-events (branch A3)')
q('SNV-only concession (Z23003785 s7.3), part 1',z3,'Restricting to the approximately 35 million SNVs and apportioning symmetrically: 17.5 million required fixations on the human lineage.','Continues on next PDF page')
q('SNV-only concession (Z23003785 s7.3), part 2',z3,'At 1,322 gen/fix (non-mutator): 191 achievable. Shortfall: 91,600×. At 105 gen/fix (mutator): 2,407 achievable. Shortfall: 7,271×.','PLAN.md pass-1 said SNV-only ~94,000x; text says 91,600x (non-mutator)','PLAN ~94,000x vs 91,600x')
q('Divergence time 3.0',z3,'The divergence time is 6.3 million years. At 25 years per human generation, this provides 252,000 generations.')
q('Human-derived rate (Z23003785 s8.6)',z3,'yields approximately one fixation per 27,600 effective generations (Day and Athos 2025, Appendix D). Applied to 252,000 generations provides 8 achievable fixations against the 205 million required.','Cites book appendix (not harvested)')

zd=zsrc(18166234)
q('d definition (verbal)',zd,'d = (Actual allele frequency change per generation) / (Change predicted by discrete-generation model)','Section 2.3')
q('d definition (integral)',zd,'d = T × d_continuous = T × [∫ μ(x) × l(x) × v(x) dx / ∫ l(x) × v(x) dx]','Section 3.3; μ(x) = −d[ln l(x)]/dx is mortality force')
q('d empirical value',zd,'Day and Athos (2025a) estimated d empirically from ancient DNA time series, finding d ≈ 0.45 from three independent loci (LCT, SLC45A2, TYR).')
q('d integral defended (Q&A)',bsrc('2026-01-19','probability-zero-qa','2026/01/19/probability-zero-qa/'),'If l(x) and v(x) were constants, they\'d cancel and you\'d get d = T × ∫μ(x)dx. But they\'re not constants, they\'re age-dependent functions that capture the demographic structure of the population.')

zb=zsrc(18167588)
q('Bernoulli Barrier (Z18167588): 14.7x vs 1,570x',zb,'the fitness differential between the "best" and "worst" genotypes in a population of 10,000 is only 14.7×—while the required differential is 1,570×, a shortfall exceeding 100-fold.','Abstract; n = 157,000 loci in this paper (not 2x10^7)')
q('Bernoulli: ~230 simultaneous sweeps',zb,'the "active zone" of intermediate-frequency alleles imposes a hard limit on pipeline capacity of approximately 230 simultaneous sweeps.','Abstract')
q('Bernoulli: how 230 is obtained',zb,'Working backward from the constraint, the active zone can sustain approximately 200–300 simultaneous sweeps before the Bernoulli Barrier compresses variance below the threshold required for effective selection.','Section 7.8; no derivation shown in text; t_transit ≈ (2/s) × ln(9) ≈ 440 generations with s = 0.01')
q('Bernoulli: 230 pipeline arithmetic',zb,'Maximum fixations ≈ (300,000 / 440) × 230 ≈ 157,000 This appears to match the requirement for human-chimpanzee divergence.','Section 7.8: the paper itself says the idealised throughput matches 157,000 before applying the drift input constraint (s7.9)')
q('Bernoulli: P(all beneficial) = 0.5^157,000',zb,"P(all beneficial) = (0.5)¹⁵⁷'⁰⁰⁰ = 10⁻⁴⁷'²⁶²",'Section 4.1')

zh=zsrc(22129121)
q('Hard Limits (Z22129121): X formula, ~10^4',zh,'Checking them yields a hard ceiling on population size, X = (Vₖ + 2)·G/16 — reproductive variance and lineage generations alone, with no mutation rate, no coalescent quantity, and no fitted constant. For a large, long-lived vertebrate the effective ceiling falls to about ten thousand individuals.','Abstract')
q('Hard Limits: exp(−π²Nₑ/G)',zh,'a neutral allele’s chance of fixing within the generations its lineage will ever have is not merely small but exponentially small, of order exp(−π²Nₑ/G) — for humans at current size, about one in ten to the seventy-eight-millionth.','Abstract; p.1')
q('Hard Limits: F(T) short-time law',zh,'F(T) ∼ exp( − π² Nₑ / T ), T ≪ 4Nₑ The naive fill fraction T/4Nₑ is not just unproven; it is an overstatement, and a vast one.','p.8; no citation given at this point (paper has no reference list found)')
q('Hard Limits: Ne definition and 1/(2N)',zh,'Nₑ = (4N − 2) / (Vₖ + 2)','p.4; elsewhere the paper uses neutral fixation probability 1/(2N): "neutral fixation probability exactly 1/(2N)" (p.11)')
q('Hard Limits: human ceilings',zh,'The human’s is thirty-five thousand as a species, a hundred thousand as a lineage. The elephant’s is twenty-eight thousand.','p.6')

zi=zsrc(22903977)
q('Intrinsic Irrelevance (Z22903977): E[F(T)]',zi,'using the exact transient formula E[F(T)] = μL ∫₀ᵀ F_X(u) du rather than the naive product μLT, the leading-order correction subtracts the mean fixation time from the available window.','Abstract, p.1')
q('E[F(T)] ≈ μL(T − 4Nₑ)',zi,'∫₀ᵀ F_X(u) du = T − ∫₀ᵀ (1 − F_X(u)) du ≈ T − 4Nₑ','p.2; and E[F(T)] ≈ μL(T − 4Nₑ)')
q('Intrinsic Irrelevance: numbers',zi,'Using 252,000 generations since the split (approximately 6.3 million years at 25 years per generation) and μL ≈ 30 neutral mutations per generation: Steady-state calculation (k = μ applied naively): 30 × 252,000 = 7,560,000 fixations','p.3')
q('Ancestral polymorphism treated (Z22903977)',zi,'Under coalescent theory, the expected pairwise divergence contributed by ancestral polymorphism is θ = 4Nₑμ per site.','p.3')

zn=zsrc(18525547)
q('k = μN/Nₑ (Z18525547 eq. 1)',zn,'k = 2Nμ × 1/(2N_e) = μ × (N/N_e) (1)','docx; abstract states the cancellation "is invalid"')
q('k = μN/Nₑ (blog 2026-02-04)',dq,'k = 2Nμ × 1/(2Nₑ) = μ(N/Nₑ)')
zr=zsrc(18525262)
q('k = 0.743μ (Z18525262 eq. 3)',zr,'k = μ × 6.091/8.2 = 0.743μ (3)','Derived from 4 generations of human census data 1950-2025; Day states it "confirms" Balloux & Lehmann 2012')
q('k = 0.743μ abstract',zr,'Applied to four generations of human census data, it yields k = 0.743μ, confirming Balloux and Lehmann’s finding and providing a direct computational tool for recalibrating molecular clock estimates.')
q('k up to 0.5μ (blog 2026-02-09)',bsrc('2026-02-09','the-significance-of-d-and-k','2026/02/09/the-significance-of-d-and-k/'),'The data show that k in humans has been approximately 0.5μ or less throughout the entire modern period for which we have reliable demographic data','Third k value in corpus: 0.5μ')
q('k = 32.3μ (blog 2026-10-01) - first appearance in harvested corpus',bsrc('2026-10-01','the-education-of-a-population-geneticist','2026/10/01/the-education-of-a-population-geneticist/'),'comparing Bergeron’s (2023) pedigree-measured mammalian mutation rate against the required substitution rate from Yoo et al. (2025) gives k = 32.3μ, not k = μ.','Not found in any Zenodo text; no derivation in the post. Book (paywalled) may contain it; not checked.','PLAN.md: "not in Zenodo; probably book only" -> in fact first appears in this blog post (2026-10-01)')

qa=bsrc('2026-01-19','probability-zero-qa','2026/01/19/probability-zero-qa/')
q('t ≈ 19,800 gens/fixation, s = 0.001 (Q&A)',qa,'N_e = 10,000 (standard effective population constant) T = 22 years (generation, Gurven & Kaplan 2007) L = 51 years (lifespan based on Coale-Demeny-West life tables) s = 0.001 (selection coefficient, Zeng et al 2021) t ≈ 19,800 generations per fixation','Formula not shown in the Q&A; (2/0.001) x ln(20,000) = 19,807 (derived)')
q('t ≈ (2/s)ln(2Nₑ) stated (blog 2026-10-01)',bsrc('2026-10-01','the-education-of-a-population-geneticist','2026/10/01/the-education-of-a-population-geneticist/'),'Kimura’s equation for fixation time: 4Nₑ generations for a neutral allele, or t ≈ (2/s) × ln(2Nₑ) for a beneficial one.','Attributed to Kimura; Z18470617 cites Charlesworth 1994 for sweep time in the Kimura calculator Z19984826')
q('t ≈ (2/s_eff) ln(2N_e) in a Zenodo paper',zsrc(18166426),'Time to fixation calculated using t ≈ (2/s_eff) × ln(2N_e) for N_e = 10,000, from initial frequency p = 0.01 to p = 0.99.')

zhd=zsrc(18168236)
q('Haldane 300 gens/substitution (Z18168236)',zhd,'Haldane calculated that mammals could fix no more than approximately one beneficial substitution per 300 generations, based on the reproductive cost each substitution imposes on a population.')
q('Haldane + d = 487',zhd,'Achievable fixations (Haldane + d) = 146,250 / 300 = 487 fixations')
q('Haldane table (blog 2025-05-28)',bsrc('2025-05-28','haldane-vs-kimura','2025/05/28/haldane-vs-kimura/'),'HALDANE Years: 9,000,000 Years per generation: 25 Generations per fixed mutation: 300 Years per fixed mutation: 7,500 Maximum fixed mutations: 1,200','Table also carries a x1.4 bp-per-allele factor (stated in the text)')
dk=bsrc('2026-01-08','88-million-x','2026/01/08/88-million-x/')
q('Haldane 11,739 / 321,444 are Dawkins quoting Haldane (blog 2026-01-08)',dk,'His answer was a mere 11,739 generations if the gene is dominant, 321,444 generations if it is recessive.','Passage is attributed in the post to Richard Dawkins, The Genetic Book of the Dead (2024), as posted by Day; about a hypothetical s with 999 vs 1,000 survivors (s ~ 0.001)','Figures are Dawkins\' (after Haldane), not computed by Day')
q('Day\'s use of the Dawkins figures',dk,'Dawkins somehow imagines that even 642,888 generations for one single base pair is more than enough time for evolution to take place. He’s off by a mere factor of 4.4 x 20 million, or 87,916,307x.','642,888 = 321,444 x 2 (derived)')

za=zsrc(23046531)
q('aDNA (Z23046531): abstract counts',za,'of 1,143,671 autosomal SNPs analyzed, one changed from above 10% starting frequency to fixation or loss. In the replication (AADR v66.p1, analyzed September 29, 2026), three did.','Abstract, p.1','PLAN "zero fixations" vs paper: 1 (v62) and 3 (v66) completions from MAF>=10%')
q('aDNA (Z23046531): discussion',za,'Across 1.14 million autosomal loci and 7,000 years of European prehistory, zero alleles moved from below 50% starting frequency to regional fixation, and zero moved from below 10% to fixation, in either run.','Discussion, p.6')
q('aDNA (Z23046531): counts of fixation events',za,'The true fixation check identified 17,806 loci newly reaching 100% and 8 loci newly reaching 0% in the modern period.','Section 3.3 (v62.0); v66.p1: 3,469 newly 100%, 1 newly 0%')
q('aDNA zero fixations - blog 2026-01-14',bsrc('2026-01-14','empirically-impossible','2026/01/14/empirically-impossible/'),'The observed fixation count was zero. Not a single allele in 1.2 million crossed from rare (<10% frequency) to fixed (>90% frequency) in seven thousand years.','AADR v62.0, 1,211,499 loci, Neolithic n=1,112 vs modern n=645 (stated in the post); differs from Z23046531 (1,143,671 SNPs; 1,372/680)','loci/sample counts and definition differ between blog (Jan 2026) and Zenodo paper (Sep 2026)')

zl=zsrc(23105291)
q('LTEE fixations (Z23105291): 5,496 / 723,000',zl,'By this strict definition the twelve populations contain 5,496 whole-population fixations across 723,000 population-generations.','Abstract; same paper: naive >=95% rule returns 8,679')
q('LTEE naive rule (Z23105291)',zl,'A naive rule that counts the first time a mutation\'s pooled frequency reaches 95% — the method of most quick analyses, including an earlier draft of our own — returns 8,679.','Note: 3.0 (Z23003785) uses the >=95% rule for its 1,322 figure')
q('LTEE 1,322 table (Z23003785 s4.1)',z3,'The average across all five non-mutator populations at 60,000 generations is 45.4 fixations, yielding a cumulative rate of 1,322 generations per fixation.','60,000/45.4 = 1,321.6 (derived); uses >=95% pooled-frequency counting (s3.2)')
q('LTEE per-population 66 (Z23105291 table 1)',zl,'Ara+2 non-mutator 60,500 174 66 0 66 0','Table 1 row: PASS mutations 174; whole-population fixations 66; within-lineage sweeps 0; first-crossing 66; 60,000/66 = 909 (derived)')
q('LTEE 909 gens/fixation Ara+2 (blog)',bsrc('2026-10-01','snikker-snak','2026/10/01/snikker-snak/'),'For example, Ara+2 had 66 fixations in 60,000 generations. At 909 generations per fixation, this was one of the fastest still-viable populations.')
q('LTEE 4,615 NS-only (blog 2026-09-27)',bsrc('2026-09-27','the-temperature-rises','2026/09/27/the-temperature-rises/'),'The real, updated 60-generation LTTE numbers are: 4,615 generations per beneficial fixation (natural selection) 1,322 generations per all-cause fixation (natural selection + neutral theory + everything else)','Not found in Z23003785 (which gives ~1,408 gen per beneficial fixation by clone-pair, s4.3)','4,615 appears only in blog; Zenodo 3.0 gives 1,408 (clone-pair beneficial-only)')
q('LTEE 78 gens/fix hypermutators',bsrc('2026-09-28','mittens-3-0','2026/09/28/mittens-3-0/'),'increased the speed of the subsequent fixations to 78 generations per fixation.')
q('LTEE 1,600 -> 1,400 -> 1,322 (Z23003785 s3.3)',z3,'The book Probability Zero used 1,400 gen/fix, taken from Good et al.’s published summary. Our independent re-analysis of the raw data produces 1,322')

zbio=zsrc(18168236)
q('Source of 1,600 in 2025 papers',zbio,'Sequencing detected 25 mutations that were fixed over approximately 40,000 bacterial generations, yielding an average of 1,600 generations per fixed mutation.','Z18168236 cites Good et al. 2017; the 2019 post cites Nature 2009 (Barrick et al.)','citation for the 25/40,000 datum differs between 2019 post (Nature 2009) and 2025 papers (Good 2017)')

rt=bsrc('2026-05-07','a-retraction-and-a-revision','2026/05/07/a-retraction-and-a-revision/')
q('Retraction 2026-05-07: what is retracted',rt,'our subsequent empirical work has identified a category error in how the selection-cost binding constraint was being used in it.')
q('Retraction: three-term framework',rt,'the realized substitution rate equals the minimum of three serial constraints: the corrected input flux (Term 1), the polymorphism throughput ceiling (Term 2), and the selection-cost limit (Term 3).')
q('Retraction: the error',rt,'my error was in interpreting its output as a constraint on total k. Once corrected, Term 3 still limits adaptive substitution rate at ~10⁻¹², but total substitution rate is only governed by Terms 1 and 2')
q('Retraction: CHLCA revised',rt,'the CHLCA event falls somewhere in the 250 kya to 1.3 Mya range rather than the 6.3 Mya presently assumed. But it cannot be as recent as the lower end of the 68 kya to 330 kya range')
q('Retraction: what survives',rt,'The textbook k = μ identity is still falsified — both directly (pedigree μ and phylogenetic k disagree by a median factor of 25 across 55 vertebrates)','Z19984826 (the retracted paper) still carries the original text; no revised Zenodo version seen')

q('Darwillion: Day on its status',bsrc('2026-09-17','the-math-is-too-hard','2026/09/17/the-math-is-too-hard/'),'the Darwillion is nothing more than a rhetorical absurdity to demonstrate how far off the biologists are from the mathematical realities of the situation.')
q('Darwillion formula (secondhand, McCarthy quoted)',bsrc('2026-09-11','do-try-to-keep-up-dennis','2026/09/11/do-try-to-keep-up-dennis/'),'What Vox Day calculated—(1/20,000)20,000,000 —are the odds that a particular group or a pre-specified list of 20 million mutations','secondhand: critic\'s quotation of Day\'s book calculation; exponent flattened in HTML','secondhand')

zrl=zsrc(23188201)
q('Relictation (Z23188201): 10% threshold',zrl,'compression fails and a single family can replace more than ~10% of the population, the formula t̄ = 4Nₑ breaks in quantifiable ways. Below 10% replacement, the formula holds','Abstract p.1')
q('Hypermutation hazard 2.3% (Z23020792)',zsrc(23020792),'is approximately 0.06 × 0.39 ≈ 2.3% per founder','p.7')

q('Book: 2nd edition 410M / 14.9%',bsrc('2026-05-23','probability-zero-2nd-edition','2026/05/23/probability-zero-2nd-edition/'),'the genetic difference between chimps and humans turned out to be 14.9 percent, with 410 million base pairs separating the two lineages since the Chimpanzee-Human Last Common Ancestor.','2nd-edition introduction')
q('Book: first edition built on 40M bp (2005 data)',bsrc('2026-05-23','probability-zero-2nd-edition','2026/05/23/probability-zero-2nd-edition/'),'All of the mathematics that I utilized in the first edition of this book were based on the observed divergence of 40 million base pairs between the two lineages published in the 2005 paper.')

# render
out=[]
bad=0
cache={}
for i,(topic,(key,fn,url),text,note,flag) in enumerate(Q,1):
    p=f'{R}/{fn}'
    raw=open(p,errors='replace').read()
    if fn.startswith('zenodo') and 'pdf' in os.listdir(R).__str__() and os.path.exists(f'{R}/{fn[:-4]}.pdf'):
        pages=raw.split('\f'); kind='pdf'
    else:
        pages=[raw]; kind='txt'
    nt=norm(text); loc=None
    for pi,pg in enumerate(pages,1):
        n=norm(pg)
        if nt in n:
            if kind=='pdf': loc=f'p.{pi}'
            else:
                # paragraph index: count nonempty lines up to match
                pos=n.find(nt)
                # find line containing start of quote
                start=nt[:40]
                li=None
                lines=[l for l in pg.split('\n')]
                nonempty=0
                for l in lines:
                    if l.strip(): nonempty+=1
                    if norm(l).find((norm(start[:14]) if len(norm(start[:14]).split())>1 else norm(start).split()[0]))>=0 and li is None: li=nonempty
                if li is None:
                    nonempty=0; fw=nt.split()[0]
                    for l in lines:
                        if l.strip(): nonempty+=1
                        if norm(l)==fw and li is None: li=nonempty
                loc=f'¶{li} of extracted text' if li else 'para n/a'
            break
    if loc is None:
        # try joining across lines for blog multi-line quotes
        bad+=1; loc='NOT FOUND'; print('NOT FOUND:',i,topic,file=sys.stderr)
    # date/version
    out.append((i,topic,key,url,loc,text,note,flag))
import json
zd={str(r['id']):(r['date'],r['created'],r['mod']) for r in json.load(open('zrows.json'))}
def dv(key):
    if key.startswith('Z'):
        d=zd[key[1:]]; return f'Zenodo pub. {d[0]}, record modified {d[2]}'
    return f'blog post dated {key[1:11]}'
with open('quotes_out.md','w') as f:
    for i,topic,key,url,loc,text,note,flag in out:
        f.write(f'### Q{i:02d} {topic}\n- source: `{key}` ({dv(key)}); URL: {url}\n- locator: {loc}\n- quote: "{text}"\n')
        if note: f.write(f'- note: {note}\n')
        if flag: f.write(f'- **DISCREPANCY/FLAG:** {flag}\n')
        f.write('\n')
print(len(Q),'quotes;',bad,'not found')

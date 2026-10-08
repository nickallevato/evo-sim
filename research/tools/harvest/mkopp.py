O='/home/na/projects/evo-sim/docs/research/opponents/'
def W(name,title,side,role,cred,srcs,args,weak,strong,unk=''):
    t=f'# {title}\n\n- **Side:** {side}\n- **Role:** {role}\n- **Stated credentials (as self-described or as introduced; unverified here):** {cred}\n- **Sources (see `sources/bib-critics.md`):** {srcs}\n\n## Arguments mapped to branches\n(Branch IDs from `hierarchy.yaml`. Quote IDs are in `sources/quotes-critics.md`.)\n\n| Branch | Argument | Quote refs |\n|---|---|---|\n'
    for b,a,q in args: t+=f'| {b} | {a} | {q} |\n'
    t+='\n## Weaknesses noted (own math / inputs / reading of Day)\n'+''.join(f'- {w}\n' for w in weak)
    t+='\n## Strongest technical point\n'+strong+'\n'
    if unk: t+='\n## Unknown / not checked\n'+unk+'\n'
    open(O+name+'.md','w').write(t)

W('dennis-mccarthy','Dennis McCarthy (Substack "All The Mysteries That Remain")','critic','Public-facing rebuttal of the first-edition fixation arithmetic and the Darwillion; also argues for evolution generally (biogeography, speciation, fossils).',
 'Says he has "published multiple peer-reviewed papers on evolution and biogeography" and a 2009 OUP book (MC-13). No population-genetics credential claimed.',
 'MC-1, MC-1p, MC-2, MC-2p, MC-3..MC-6, MC-arch',
 [('G3 (also D)','(1/20,000)^20,000,000 prices one pre-specified list of 20M mutations; history needs any 20M of a huge pool','MC-01, MC-02'),
  ('B5','Using Day\'s inputs: 50,000 new mutations/yr x 9 My = 450 billion; x 1/20,000 = 22.5 million fixed (about the 20M observed)','MC-03, MC-04'),
  ('B1','Time-adjusted version: only mutations older than 4Ne=40,000 gens count -> 400 billion x 1/20,000 = 20M','MC-09'),
  ('F / G2','Fixations do not queue; many alleles sweep at once','MC-08'),
  ('A5','E. coli genome ~690x smaller than human; 60-100 de novo mutations per newborn vs ~1 per 1,000-2,400 E. coli divisions','MC-05, MC-06, MC-07'),
  ('B2','Day\'s "3x more harmful than neutral" applies to coding DNA only; genome-wide only 3% deleterious','MC-10'),
  ('A3x','410 Mb = structural variation; one event can alter millions of bp','MC-11'),
  ('B4','Divergence dates are themselves derived using neutral theory','MC-12')],
 ['Uses N = Ne = 10,000 for both mutation supply and fixation probability, i.e. assumes N/Ne = 1. That is exactly what B3 (k = mu N/Ne) disputes, so the arithmetic answers Day only if N = Ne.',
  'All 450 billion mutations are treated as fixation-eligible at 1/20,000 (neutral). The 3% deleterious figure (MC-10) is uncited. A 20M result then depends on ~100% of mutations being effectively neutral; with a neutral fraction f the expectation scales to f x 22.5M.',
  'Expected value only; derived: Poisson sd for mean 22.5M is ~4.7 thousand, so variance is immaterial for this particular claim.',
  'The "60 to 100 de novo mutations" and "dates are based on Kimura theory" statements carry no citation in the post. The second is at least partly contested (fossil and pedigree calibrations exist; see Langergraber in fidelity ledger).',
  'Targets the first-edition Darwillion. Day later calls the Darwillion "a rhetorical device" (PLAN.md; not re-verified here), so the rebuttal does not touch MITTENS 3.0 (1,322 gens/fixation, 205M).',
  'Paid posts (2026-01-26, 02-03) are known only as previews; the free reposts (2026-09) may have been edited since.'],
 'The "specific vs any 20M" correction plus the expected-count calculation (MC-03/MC-04) is the cleanest critique of Darwillion and needs only Day\'s own inputs.',
 'Whether the 2026-09 free text differs from the 2026-01 paid original.')

W('pz-myers','P.Z. Myers (Pharyngula)','critic','Blog commentary on MITTENS 3.0 and the Dembski interview; points readers to the Gutsick Gibbon video.',
 'Biologist (blog); says of himself "someone who is not a population geneticist" (PZ-06).','PM-1, PM-2, PM-3, PM-s',
 [('G1 / G2','Day divides generations by the per-fixation time, which assumes sequential fixation; evolution is massively parallel','PZ-01, PZ-05'),
  ('adhom','Day\'s education, AI-assisted authorship, 11 references (7 LTEE, 2 ape-genome, 2 own), Zenodo not peer reviewed, Discovery Institute associates','PZ-02, PZ-03')],
 ['No numbers or equations. The serial-vs-parallel point does not engage Day\'s stated reply that G_f is a measured aggregate throughput from a parallel population (Day: the LTEE fixations occurred in parallel).',
  'His summary of MITTENS 3.0 mentions "35 million" SNVs in one sentence and quotes "the requirement is 205 million" in the next without reconciling them (the A3x issue is not raised).',
  'Reference counts (11/7/2/2) are asserted, not tabulated; not independently checked here.',
  'A large share of the text is about the person (adhom); recorded separately and given no weight on the math.'],
 'The sequential-estimate diagnosis (divide total generations by one fixation interval) is correct as a description of F_max = t*d/(g*Gf); whether it is an error depends on how G_f was measured (A2/G1).')

W('camestros-felapton','Camestros Felapton (blog)','critic','Six-part chapter-by-chapter reading of the first-edition book; frames itself as a layperson\'s sanity check.',
 '"I\'m not a biologist, I\'m not really a mathematician" (CA-13).','CF-1..6',
 [('A','Equation arithmetic is sound; Day picked numbers that disadvantage his own side','CA-02'),
  ('A4','d is defined late (ch.13/App. A, he corrects an earlier claim it was never defined) and cannot be constant over human history','CA-03, CA-12'),
  ('B6','Day treats all human-chimp differences as post-split mutations; ancestral variation is ignored','CA-04'),
  ('G1','"Generations per fixation" reads as serial, but concedes it is an average','CA-05, CA-10'),
  ('A2','Re-derives a rate from Barrick 2009: 35 mutations by 15,000 gens -> ~429 gens/fixation (typo "1500")','CA-06, CA-07, CA-11'),
  ('A5','Bacterial generation is not an ape generation; sexual reproduction allows recombination','CA-08'),
  ('G3','Darwillion confuses probability of a specific outcome with that of some outcome (lottery analogy)','CA-09')],
 ['Reads only the first edition (9 My, 20 y, d=1/0.45, 281 fixations); later versions (1,322 gens/fixation, 205M, d) are not addressed. Part 5 asserts Day\'s core argument "hasn\'t changed since February 2019", which the version table in PLAN.md contradicts.',
  'The 429 gens/fixation re-derivation (CA-06) prints 1500/35 but means 15,000/35 = 428.6; and clones present in later clones are not necessarily population-fixed. He hedges ("I may well be misreading").',
  'The Part 2 argument that fixation requires more individuals today than "a few hundred years ago" is muddled: fixation means 100% frequency at any N.',
  'Parts 4-6 contain religion and politics speculation (adhom) that has no mathematical content.'],
 'Concession that the formula is arithmetically sound and that G_f is an average (CA-02, CA-10) isolates the dispute to whether the LTEE average is a valid ceiling for apes (A2/A5).')

W('keruru','keruru / C. Kereru (claudekeruru.substack.com)','adjacent (ally who self-corrected)','Substack author who built on Day (Feb 2026), then publicly retracted the Ne-equivocation and ancient-DNA claims (Aug 2026); work is largely produced with LLMs ("mainly claude").',
 'None stated beyond "Working on questions with Claude" (feed tagline). Posts cite Zenodo deposits of code.','KR-1..KR-6 (excl. KR-x, a different Keruru)',
 [('B3 / B5','(Feb) k = 2N mu x 1/(2Ne) = (N/Ne) mu; (Aug) withdrawn: supply and fixation both use census N, so Ne never enters; exact Markov chains give 1/(2N_census)','KR-07, KR-01, KR-02, KR-04'),
  ('C','Zero aDNA fixations in 240 gens is the neutral prediction (~10^-29 expected fixations); claim withdrawn','KR-03, KR-04'),
  ('B4','Pedigree mu ~1.2e-8 vs ~2x for fossil-calibrated; unreconciled','KR-05'),
  ('A5','(Jan) LLM calc: ~30 mutations/gen/lineage -> ~18M neutral vs 35M observed = 2-fold shortfall','KR-08'),
  ('A','(Jan) "central thesis is mathematically sound"','KR-09')],
 ['The Jan review (KR-09) endorsed the thesis from an LLM transcript; the Aug post retracted two of its supports. Treat KR-08/KR-09 as superseded unless re-derived.',
  'Day\'s reply (quoted in KR-06) says the aDNA retraction used Ne ~ 10,000 derived from theta = 4 Ne mu, which presupposes k = mu; keruru "had no answer". The 10^-29 number therefore inherits that circularity.',
  'The temporal-method Ne work and Crow-index argument (fertility selection) are outside MITTENS and not assessed.',
  'Code/data on Zenodo not retrieved; the exact-chain result is the author\'s statement only.'],
 'The martingale/optional-stopping argument that neutral fixation probability equals initial frequency regardless of Ne (KR-01, KR-02) is a clean, checkable refutation of the B3 equivocation, and it comes from a former proponent.',
 'Whether keruru\'s retraction changed Day\'s Hard Limits / k = mu paper (Zenodo 22129121 etc.): Day-corpus agent.')

W('ola-hossjer','Ola Hossjer','ally (partial)','Wrote the technical review of Day\'s main argument for Dembski\'s Substack; co-author of waiting-time and genetic-entropy papers with ID-associated authors.',
 'Introduced as "Professor of Mathematical Statistics, Stockholm University" (HO-09). Says he advocates "uncommon descent" (HO-10).','HO-1, HO-2',
 [('A (F_max)','Reproduces 127 fixations: 9e6 x 0.45/(20 x 1,600)','HO-01'),
  ('A5','Scaling by mutation rate (1.25e-8 vs 1e-10) gives 15,800; by genome length (x ~650) ~10 million, "only by a factor of 2" short of 20M','HO-01, HO-02'),
  ('H','Haldane cost limits parallel selected fixations, so the genome-length scaling does not apply to adaptive fixations (asserted)','HO-03'),
  ('B3 / B5','Neutral calc F = L d mu t = 7.6 million, close to the scaled bound; both assume parallel fixation','HO-04'),
  ('B4','Neutral theory cannot test common descent since it is used to date divergence','HO-05'),
  ('A','Agrees with Day\'s conclusion after adjustment','HO-06'),
  ('H (near-neutral)','Slightly deleterious fixations erode fitness (genetic entropy)','HO-11')],
 ['Derived: his neutral figure without the turnover factor is 3e9 x 1.25e-8 x 450,000 = 16.9M, versus 20M required (ratio 0.85). The factor d = 0.45 in the neutral rate (F = L d mu t) alone produces the 2.2x gap he reports; k = mu per generation is not usually multiplied by d. This is an input choice, not a result.',
  'Eq. 2.4 assumes fixations scale linearly with genome length; the Haldane step that is meant to undo this scaling (HO-03) is asserted, with no cost calculation, and Haldane\'s limit is not applied to the neutral share he himself computes.',
  'The circularity point (HO-05) ignores pedigree mutation rates, which he notes are independent of divergence data; he does not show that using them with independent dates fails.',
  'Genetic-entropy sentence (HO-11) has no calculation in the review. Sanford is cited, not Day.',
  'He agrees with the conclusion while advocating a different explanation (uncommon descent) than Day (guided common descent); allies are not unanimous on mechanism.',
  'Equation numbers differ between PDF text ((4),(5)) and LaTeX labels (2.4, 3.1) as extracted; Dembski\'s abridgement inserts bracketed text that is Dembski\'s.'],
 'Transparent re-derivation (127 -> 15,800 -> ~10M) that shows the book\'s own bound closes to a factor ~2 once mutation supply and genome length are scaled; this is the best ally-side scaling calculation and it concedes A5.',
 'Whether the PDF differs from the Dembski-abridged text beyond the brackets.')

W('bill-dembski','Bill Dembski (Substack host / interviewer)','ally','Hosted the Hossjer review and a long interview with Day; did not himself test the math. Earlier writings on Rosenhouse (2022) not harvested.',
 'Intelligent-design proponent (DE-03); describes Tipler as "my friend and colleague at Tulane University".','HO-2, DM-1, DM-2',
 [('A5','Asks Day to respond to the LTEE->primate scaling objection','DE-01'),
  ('B5','Asks why k = mu does not bypass the fixation bottleneck','DE-02'),
  ('ROOT','Host framing: ID has "own arguments"; says Hossjer\'s endorsement applies to the main argument only','DE-03, HO-07'),
  ('(Tipler)','Reports Tipler\'s endorsement and appendix','TI-03')],
 ['Contributes no calculation. Day\'s answers to his own steelman questions (e.g. "the scaling element doesn\'t apply at all") are given without equations and are not followed up in the interview.',
  'He used Grok to compile a list of Day\'s earlier posts and posted it "reasonably complete"; unverified AI output (HO-2).',
  'Bracketed paraphrases in the Hossjer post are his, not the author\'s (he says so).'],
 'His questions are the best compact statement of the objections Day must answer (A5, B5, G1) and show an ally recognising them.')

W('frank-tipler','Frank J. Tipler','ally (secondhand only)','Wrote the foreword/introduction and an appendix to Probability Zero (per Day, Dembski, Tree of Woe).',
 'Described by others as a mathematical physicist at Tulane (Camestros, Dembski). Not self-described in any retrieved text.','TW-1, HO-2, PM-1 (secondhand mentions)',
 [('ROOT','Reported endorsement: "the most rigorous mathematical challenge to Neo-Darwinian theory ever published"','TI-01, TI-02, TI-03')],
 ['No primary Tipler text was retrieved (book is paid); every statement here is secondhand.',
  'Whether his appendix contains independent calculations is unknown.'],
 'None assessable.',
 'Foreword and appendix text; Day\'s 2024 post "A Physicist Endorses MITTENS" (Day-corpus agent).')

W('steve-keen','Steve Keen','ally','Wrote the preface to The Frozen Gene (the sequel), not Probability Zero.',
 'Economist; "my PhD in economics in the 1990s" and a "side interest" in evolutionary dynamics (KE-03, KE-04).','KN-1',
 [('ROOT','"The reason it fails ... is time"; endorses "savage demolition" of random-mutation-plus-selection','KE-01, KE-02, KE-05'),
  ('(non-A..H)','Proposes Lamarckian/quantum mechanisms (McFadden 2001; Schwartz 2000; Cairns 1988)','KE-01')],
 ['Preface has no equations or numbers; the quantitative claim (time exceeds the age of the universe) is only consistent with Day if the bacterial rate is a fixed ceiling (derived in KE-05 note: 6.8e12 y vs 13.8e9 y).',
  'The experimental programmes he cites (Cairns 1988 adaptive mutation; Gorczynski & Steele 1980) are cited for acceleration under stress without discussing later follow-ups; no verification attempted here.',
  'The preface is about a different book; do not attribute its claims to MITTENS.'],
 'None on the fixation branches.')

W('gutsick-gibbon','Gutsick Gibbon (Erika)','critic (host)','YouTuber hosting the Duffy lecture series and the 3.5-hour response with Zach Hancock; organised a credentialed-reviewer call.',
 'Taught a university course ("adapted version of the course I taught as a university instructor"); working on a dissertation; defers to a population geneticist guest on math.','GG-1, GG-2, GG-3',
 [('A, G1, B5, A3x','Hosts Hancock\'s derivation (see zach-hancock.md)','GG-01..GG-13'),
  ('epistemic','Will not ask Duffy to defend the math live; "the science can handle it"; defers to later guests','DU-05'),
  ('epistemic','Requests credentialed commenters; claims only three PhD holders vetted Day (all Discovery Institute associates)','RE-12')],
 ['A credential count is not a rebuttal (FP-01 makes this point fairly); the Reddit claim about "three people with doctorates" is uncited.',
  'About 60% of the 3.5 h video (t~02:15-03:30) concerns Day\'s biography and politics, which is not math; also speculation about how the book was written (t~02:04:48), unsupported.',
  'The video answers the Duffy-presented version (6.3 My, 1,400, 205M), not MITTENS 3.0, and the roundtable of credentialed reviewers was not yet published at pull time.',
  'Her live response during the Duffy stream contained no calculation.'],
 'Providing the full captioned derivation and a public call for named reviewers is a verifiable process; see Hancock for the math.')

W('zach-hancock','Zach Hancock (@talkpopgen)','critic','Guest population geneticist on the Gutsick Gibbon video; derives the neutral substitution rate on camera and compares to observed divergence.',
 'Says he has a PhD in ecology and evolutionary biology, did a postdoc in statistical population genetics, and is an assistant professor at Augusta University (GG-14, GG-15).','GG-1, TH-1',
 [('G1','F_max = t/(g Gf) encodes sequential fixation; implied polymorphism pattern (no standing variation) is contradicted by site-frequency spectra','GG-01, GG-13'),
  ('A','Factor-of-two error: both lineages fix','GG-02'),
  ('B5','k = mu from Taylor expansion of the Kimura fixation formula; 2N mu x 1/(2N)','GG-03'),
  ('B5','76.8 per generation x 2 x 252,000 -> ~38M vs ~35-40M observed SNVs','GG-04, GG-09'),
  ('A5','Bacterial neutral rate: 4e-5 per gen -> ~22,000 gens per fixation; humans fix many per generation','GG-07, GG-08'),
  ('A3x','205M requires ~407 mutations/gen (~5x his estimate); "within biological reality" if structural variants count','GG-11, GG-12')],
 ['First pass used a diploid genome (6.4e9) giving 76.8; he corrected to haploid on screen (GG-05) but kept 76 by citing a de novo count of 98-206 per generation that includes structural variants (GG-06). Using haploid SNVs only: 38.4 x 2 x 252,000 = 19.4M, about 1.8x short of ~35M observed (derived; matches the KITTENS and Reddit critiques). The "38M matches 35-40M" agreement therefore partly rests on that factor of two.',
  'Bacterial mu ~1e-11 per site is lower than the 8.9e-11 per bp measured in the LTEE ancestor (Wielgoss 2011, quoted by McCarthy). With 8.9e-11 the neutral expectation is ~1 per 2,400 gens instead of ~22,000, which is within 2x of the LTEE rate of 1 per 1,322-1,600. The conclusion that humans out-fix E. coli per generation survives, but the comparison "LTEE rate >> neutral" changes character.',
  'All genome sites are treated as neutral (k = mu x L), an upper bound; no constraint fraction is applied.',
  'Self-described "back of the napkin" calculation (GG-16), no confidence interval. Auto-captions garble some figures (e.g. "Perky at all 2025").',
  'Does not address Haldane\'s cost (branch H) for the adaptive part; the null-model argument shows the neutral share only.',
  'The 205M step relies on the same SNV-rate model for structural variants while saying structural rates are hard to estimate (internal tension).'],
 'The derivation that the neutral substitution rate is mu and that parallel fixation makes F_max misread the required quantity (GG-01, GG-03) is correct textbook theory and checks numerically; the open quantity is the factor ~2 from haploid bookkeeping.',
 'Whether the whiteboard contained corrections not spoken aloud.')

W('jan-ghijselen','Jan Ghijselen (@DeDzjang), math teacher','critic','Short video on the Duffy-presented arithmetic (252,000 / 1,400 = 180).',
 '"I am a math teacher in secondary education" (DZ-03).','JG-1',
 [('G2','Marathon analogy: 60,000 runners x 4 h = 240,000 h serial vs parallel reality','DZ-01'),
  ('A','Verifies the arithmetic: 6.3 My / 25 y = 252,000; /1,400 = 180','DZ-02')],
 ['The analogy shows that serial division is wrong when events are parallel, but not that Day\'s G_f is serial: Day says G_f is a measured aggregate rate. The video does not address that.',
  'Says a fuller treatment needs stochastics/logarithms but does not give one.',
  'He mentions responding to abusive comments; comment thread contains insults on both sides (not coded).'],
 'Clear demonstration that dividing total time by one latency yields a throughput only if events are serial; correct and short.')

W('rebekah-davis','Rebekah Davis (Examining Origins)','ally','Creationist YouTuber who summarised Duffy\'s presentation, relayed Wistar arguments, and predicted no answer.',
 'Not stated in the retrieved transcript; says she is "not good at math" (transcript t~00:07:03) and has not read the book (RD-01).','RD-1',
 [('A','Restates 252,000 gens / 1,400 -> 180 vs 205M','(transcript t=00:01:33-00:01:57)'),
  ('D','Relays Eden: ~10^36 genetic transmissions for one ordered gene pair','RD-03'),
  ('epistemic','Predicts evolutionists "will provide essentially no answer"','RD-02')],
 ['Relies on Duffy\'s presentation, not the book (RD-01); mis-titles it "Zero Probability" in the transcript.',
  'Prediction RD-02 was contradicted by the 2026-10-03 Gutsick Gibbon/Hancock video, per a commenter pointing to t~3:13 (PlotTwistDad).',
  'Wistar claims are secondhand (Eden 10^36 figure) and are contested in Rosenhouse ch.4 (RO-01).'],
 'None technical; the video is a relay.')

W('will-duffy','Will Duffy','ally (presenter)','Pastor-creationist who presented Day\'s argument on the Gutsick Gibbon stream (t=00:19:12-00:43:30) and answered Q&A.',
 'Described by Gutsick Gibbon as a Colorado pastor; says "I am not a mathematician" (DU-04).','GG-2',
 [('A','180 fixations in 252,000 gens at 1,400 gens/fixation','DU-02'),
  ('A4','Overlapping-generations claim: 80% efficiency -> ~25 generations','DU-01'),
  ('G1','LTEE rate "is already parallel fixation"','DU-03'),
  ('A5','Mammal fixation rate "way slower" than bacteria','DU-06')],
 ['Presents d as 1 in the worked arithmetic (180) while also presenting the overlapping-generations correction as an important flaw; the two are not combined.',
  'The "25 generations at 80% efficiency" figure (DU-01) is repeated from Day without derivation on stream.',
  'Mammal-slower claim (DU-06) is asserted without numbers; scaling by mutation supply (A5) is not addressed.',
  'States he is not certain Day is right (DU-04).'],
 'Restating that G_f is a parallel aggregate (DU-03) correctly identifies Day\'s main defence against the serial objection.')

W('brian-mansfield','"Mansfield" (YouTube handle @brianmansfield6912)','critic','Commenter under the Examining Origins video; replies to Day\'s blog response (as quoted) and to others.',
 'Says he has been "a research geneticist for almost 40 years" (MF-07). Identity not verified.','RD-1 (comments)',
 [('B5','Drift happens at all N; N only changes which alleles are effectively neutral','MF-01'),
  ('B5','If 2% of ~100 de novo mutations are neutral: 2N alleles/gen x 1/(2N) = 1 fixation/gen','MF-02, MF-03'),
  ('F','Time to fixation is irrelevant; the interval between successive fixations matters (truck analogy)','MF-04'),
  ('B1 / B6','Pipeline full at the split; no waiting period','MF-05'),
  ('A3x','~25M SNV differences, not 200M','MF-06'),
  ('A','Concedes selection-specific adaptive fixation is a different question; Day\'s model "biologically naive"','MF-08')],
 ['His 2% illustration yields 1 fixation/generation = 450,000 over 450,000 generations, about 44x short of 20M; the argument works only with a much larger neutral fraction (MF-03 note). He says 2% is "way under" the actual share but gives no figure.',
  'Quotes Day only via a commenter\'s paste of a Day blog excerpt (secondhand).',
  '"~25 million" SNV differences and "generations per fixation ... 0.5" are uncited.',
  'Declined direct debate ("not interested"), so the exchange with Day is one-sided in this record.'],
 'The latency-vs-throughput (truck) argument and the full-pipeline point (MF-04, MF-05) are the clearest statements of the B1/F objection.')

W('joe-bowers','Joe Bowers (via Day\'s repost)','critic','Author of a seven-point review titled (per Day) "Ignorant and Unscientific Drivel". Original location not found.',
 'None stated in the reposted text.','JB-1',
 [('F','Beneficial fixation probability ~ 2s, not 1/N','BO-01'),
  ('G2 / G3','Serial-lottery framing is a category error; recombination, parallel paths','BO-02')],
 ['Contains no calculation (Day\'s reply BO-04 is accurate on this).',
  'Day\'s reply (BO-03) in turn distinguishes fixation probability from fixation rate but gives no equation.',
  'Known only through Day\'s repost (secondhand); the original may differ from the version Day quotes.'],
 'The 2s point is correct in standard theory (Haldane 1927/Kimura 1962) but does not bear on a throughput bound, as Day replies.',
 'Original review.')

W('jason-rosenhouse','Jason Rosenhouse','critic (indirect; pre-dates Day)','Author of The Failures of Mathematical Anti-Evolutionism (CUP 2022); no reply to Day found.',
 'Professor of mathematics at James Madison University (per Felsenstein; self-description not retrieved).','RO-1, RO-2, RO-3',
 [('D','Ch.4 "Legacy of the Wistar Conference": argues the critiques were refuted and are misrepresented by present-day creationists','RO-01'),
  ('D','Ch.6 "Information and Combinatorial Search": protein space, Weasel, No Free Lunch, information claims','RO-02')],
 ['Book not accessed; chapter scope known from Felsenstein\'s TOC (Felsenstein states he commented on the manuscript and wrote a blurb).',
  'Predates Probability Zero (2026) and MITTENS; cannot be a rebuttal of the fixation/LTEE arguments (branches A, B, E, G, H).',
  'Day\'s counter-claim (via Fandom Pulse) that ch.4 omits key exchanges and does not quantify is Day-side (D2) and not checked here.'],
 'Where Rosenhouse engages Wistar (D), it is the only retrieved scholarly treatment; not applicable to A-C, E-H.',
 'Cambridge TOC PDF; whether Rosenhouse has posted any reply to Day.')

W('reddit-debateevolution','r/DebateEvolution commenters (Dumb-and-Dumber, Sparky_6_4, DarwinZDF42, others)','critic','Detailed critiques of MITTENS 3.0 (sections 4.3, 6.4, 7, 8.2) and the "KITTENS" decomposition.',
 'Pseudonymous; Sparky_6_4 discloses AI assistance; no credentials stated in retrieved text.','RE-1, RE-2, GG-3, RE-3, RE-4',
 [('G1','Per-neutral-site supply 2N mu x 1/(2N): ~38 substitutions/lineage/gen at equilibrium; 9.7M over 252,000 gens','RE-01, RE-06'),
  ('A2','Sec 6.4 tenfold slip: 3,840 not 38,400 per haploid genome for a 100x mutator','RE-02'),
  ('E / A2','Estimator gives minus 906 fixations in Ara-2; Ara+5 drops 38 -> 0','RE-03, RE-04, RE-10'),
  ('A3x','Structural variants: bases affected are not separate mutation events','RE-05'),
  ('A5','LTEE is largely non-recombining, one clone, one environment','RE-07'),
  ('A5 / A3x','KITTENS: 191 x 94,000 = 17.9M achievable vs 17.5M SNV-only required; headline = 94,000 x 11.7','RE-08'),
  ('B5','Neutral mutations fix at ~mu; most divergence is neutral (DarwinZDF42)','RE-13')],
 ['KITTENS rests on linear scaling of adaptive fixations with mutation supply; its author flags this (RE-09). It also admits citations were written from memory (RE-11) and AI assistance.',
  'The 9.7M neutral figure treats every site as neutral; the Reddit OP says it is illustrative.',
  'All of these target MITTENS 3.0 text that I have not myself verified against Zenodo 23003785; section numbers and values are secondhand until R2.',
  'Top-voted replies are largely jokes or insults (e.g. the 9-month pregnancy analogy); there is no variance or sensitivity analysis in any critique.',
  'A comment says the Zenodo paper was "now gone"; unverified.'],
 'The KITTENS decomposition (94,000 x 11.7 ~ 1.1M) is the sharpest quantitative critique of MITTENS 3.0\'s headline; it uses only the paper\'s own numbers and is checkable in R4.',
 'Whether Day has revised 3.0 in response (version drift).')

W('nesslig20-peaceful-science','Nesslig20 (Peaceful Science forum)','critic','Long forum rebuttal of Duffy\'s presentation (Part I: population genetics; Part II: other claims, identifies Day as the source).',
 'Pseudonymous; no credentials stated in retrieved text.','PS-1, PS-2',
 [('H','Reproduces Haldane 1957: 30 Ne cost / 10% culling = 300 generations; cost limit does not apply to drift','PS-04'),
  ('B5','k = mu_G; with mu_G = 75 per generation, 2 x 75 x 252,000 = 37.8M','PS-01, PS-02'),
  ('A3x','Reference-genome differences are not all fixed','PS-03')],
 ['"mu_G = 75 per haploid genome" appears to be a per-diploid-offspring de novo count (~60-80); a haploid-genome SNV rate is ~38 (1.2e-8 x 3.2e9). The 37.8M result thus shares the factor-of-two issue with Hancock\'s first pass (derived).',
  'Heavy use of ad hominem about Day in Part II (labelled as such by the author).',
  'Treats the Duffy version only.'],
 'Cleanly separates Haldane\'s cost (selection) from neutral drift and shows the cost limit does not apply to the neutral share.')

W('jf-gariepy','Jean-Francois Gariepy (2019 debate; secondhand only)','critic (secondhand)','Debated Day in 2019; his objections known only from a transcript posted by Day.',
 'Day calls him a PhD biologist ("despite his PhD in biology"); not self-described in retrieved text.','JF-1',
 [('A5','Bacterial and mammalian fixation rates differ: sexual reproduction and population size variability','GA-01'),
  ('A / G1','Fixation is "a mathematical illusion" tied to population size; follow lineages instead','(GAR para 7; not quoted)')],
 ['Secondhand via Day\'s post (a hostile channel); wording may be edited.',
  'The 15.7-gens/fixation bottleneck model is Day\'s reply (GA-02) and is not analysed here.',
  'No numbers in the quoted Gariepy text.'],
 'None assessable.',
 'The debate video/transcript; Gariepy\'s own follow-up.')

W('tree-of-woe','Tree of Woe (interviewer)','ally','Interviewer for the launch-day Q&A with Day; adds no independent math.',
 'Writes that he was a "committed Darwinist" and took Nozick\'s Law & Philosophy seminar at Harvard Law in 2000 (TW-1 para 5).','TW-1',
 [('A','Day\'s answers: 202,500 gens; 1,600 ceiling; 5.3-sigma framing','TW-01, TW-02'),
  ('ROOT','Reports Tipler\'s endorsement','TI-01')],
 ['Questions are non-adversarial; useful mainly as a dated record of Day\'s January numbers (202,500 gens is yet another figure).'],
 'None.')

W('fandom-pulse','Jon Del Arroz (Fandom Pulse)','ally','Short commentary on the response to Probability Zero.',
 'None stated.','FP-1',
 [('epistemic','A credential headcount is not a rebuttal','FP-01'),
  ('G','The core claims are specific and testable (LTEE generations per fixation, scaling to human-chimp)','FP-02')],
 ['Misnames the guest ("Dr. Hanson").',
  'No math; characterises critics as "rattled" (speculation).',
  'Mentions Day\'s review of Rosenhouse and a music video; not harvested.'],
 'The point that a credential count proves nothing is fair and applies to both sides.')

W('uncle-johns-band','John Samson (Uncle John\'s Band)','ally','Worldview-framing review of Probability Zero.',
 'None stated.','UJ-1, UJ-2',
 [('G1','Total divergence / time is an unweighted average rate; parallel or serial does not matter','UJ-01, UJ-02')],
 ['An observed average divergence rate does not bound the achievable rate; the argument is valid only if the LTEE average is treated as a ceiling, which is branch A2.',
  'Mostly rhetoric about "the House of Lies"; no calculation.'],
 'Clear plain-language statement of the G1 position (average rate indifferent to parallelism).')

W('american-hypnotist','American Hypnotist (Substack)','ally','Popularisation of the first-edition numbers.',
 'None stated.','AH-1',
 [('A','Extrapolates the human-chimp bound to all life, claiming simpler organisms must fix faster','AH-01')],
 ['No calculation; generalisation from bacteria to "all life" is unsupported and contradicts the LTEE-as-ceiling logic used elsewhere.',
  'Quotes PZ first-edition arithmetic (450,000 / 1,600 = 281) which is consistent.'],
 'None.')
print('ok')

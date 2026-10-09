# Prior Art: Literature on the Argument Family Before and Outside the Corpus

Version: 2026-10-08 (first pass; revised the same day after the fact-check in `ledgers/gaps-review.md`). Companion to `ledgers/gaps.md`.

**Scope.** This file covers published work on three questions:
- the cost of selection (Haldane's dilemma);
- waiting times for coordinated mutations, genetic entropy and conservation of information;
- the empirical inputs that the current dispute needs but that neither side uses.

Most of it predates 2019. Post-2019 works are included when they review or resolve the older debate.

**Access status** is what was actually achieved in this pass:
- **full** means the full text was read, by the lead agent or by a literature sub-agent;
- **abstract** means the abstract only;
- **secondary** means the work is known only through a named secondary source;
- **not accessed** means none of the above.

No paywall was bypassed. Quotes are ≤ 30 words.

**"Cited in corpus?"** gives the result of a regex search over the extracted corpus. The groups are:
- `sources/raw/day/` (D)
- `sources/raw/critics/` (C, critics and allies)
- `sources/raw/sources/` (L)
- `docs/research/{claims,opponents,sources/quotes-*}` (R)
- the audit's own files (A)

The method is described in `ledgers/gaps.md`. "No hit" lists the terms used.

---

## A. Cost of selection / Haldane's dilemma

### PA-01: Haldane 1957, "The cost of natural selection"
- **Citation:** *J Genet* 55:511–524. doi:10.1007/BF02984069.
- **Access:** full text (a facsimile in the Blackwell/Ridley "classic texts" PDF, read by sub-agent).
- **Summary:**
  - The number of selective deaths per substitution is roughly independent of selection intensity, about 10–30 × N.
  - The figure of ~300 generations per substitution comes from an *assumed* intensity of I = 0.1, i.e. ~10% of deaths selective.
  - Haldane doubted that simultaneous selection at many loci escapes the cost, and flagged that his conclusions "will probably need drastic revision".
- **Quotes:**
  - "I think n = 300, which would give I = 0·1, is a more probable figure." (p.521)
  - "my conclusions will probably need drastic revision." (p.523)
- **Answered by:** PA-02 to PA-11, PA-14, PA-36.
- **Cited in corpus?**
  - Day: yes, throughout (Z18168236, Z19984826, H). The fidelity ledger records it as "verified-accurate, via Nunney 2003 only".
  - Critics: yes (Nesslig20; KITTENS; Reddit).
  - Nobody in the corpus notes that 300 rests on the assumed I = 0.1 rather than being derived from it (terms `I = 0.1\|10% (selective )?mortality`; Day states "10% selective mortality" as Haldane's estimate, Z18168236 §1).

### PA-02: Van Valen 1963, "Haldane's dilemma, evolutionary rates, and heterosis"
- **Citation:** *Am Nat* 97:185–190. doi:10.1086/282267.
- **Access:** not accessed (paywalled). Known via secondary sources (Matheson 2025; Wikipedia).
- **Summary:** coined the name "Haldane's dilemma". Rapid substitution at some loci limits the rate at others.
- **Cited in corpus?** No hit for `Van Valen` (all groups 0).

### PA-03: Kimura 1968, "Evolutionary rate at the molecular level"
- **Citation:** *Nature* 217:624–626. doi:10.1038/217624a0.
- **Access:** full (OCR scan; sub-agent). An abstract copy is in the corpus at `sources/raw/sources/abs/Kimura1968.txt`.
- **Summary:**
  - Kimura extrapolates ~1 nucleotide substitution per 2 years per mammalian lineage.
  - He argues that the resulting *substitutional load* (Haldane's cost) would be intolerable if the substitutions were selected, so most must be nearly neutral.
  - The neutral theory is therefore historically a response to Haldane's dilemma.
- **Quote:** "can only be reconciled with the limit set by the substitutional load by assuming that most mutations produced by nucleotide replacement are almost neutral" (p.624).
- **Answers:** PA-01.
- **Answered by:** Maynard Smith 1968 (PA-04). Kern & Hahn 2018 (MBE 35:1366; full, sub-agent) say Kimura overcounted coding sites (~4×10⁹ vs ~3×10⁷ bp) and that correcting this "alone would remove the conflict". Three caveats:
  - Kern & Hahn 2018 is a Perspective.
  - It writes Haldane's limit as "300 years" where generations are meant.
  - Its wider argument against neutral theory is contested by Jensen et al. 2019, "The importance of the Neutral Theory in 1968 and 50 years on: a response to Kern and Hahn 2018", *Evolution* 73:111, doi:10.1111/evo.13650 (abstract read via Europe PMC).
- **Cited in corpus?**
  - Day: yes, 30 D files.
  - Day states the link explicitly: "Motoo Kimura developed neutral theory explicitly in response to Haldane's work" (Z18168236 §5.1).
  - Day cites Kern & Hahn 2018 only as a challenge to neutrality (Z18167588), not for its Haldane remark.
  - Critics: a YouTube commenter says "It's literally why Kimura made his theory" (yt jDxFtCOGZ3A); that is passing.

### PA-04: Maynard Smith 1968, "'Haldane's dilemma' and the rate of evolution"
- **Citation:** *Nature* 219:1114–1116. doi:10.1038/2191114a0.
- **Access:** not accessed (paywall). Secondary: Matheson et al. 2025 (full).
- **Summary:**
  - Under truncation selection (synergistic epistasis), one selective death removes many disfavoured alleles at once, so costs do not add across loci.
  - It assumes the survivors can rebuild the population, i.e. ample reproductive excess.
- **Answers:** PA-03.
- **Answered by:** O'Donald 1969; Moran 1970 (not accessed).
- **Cited in corpus?**
  - Day: yes. Z19984826 §3.3.1 (line ~308) lists truncation selection (Maynard Smith 1968) among moves that do not raise s_max "above order unity"; blog 2026-01-10 ("It requires truncation selection").
  - Critics: no hit beyond a YouTube comment unrelated to this paper.
  - Audit: REVIEW-R4-steelman-critic (listed as outside the repo, untested).

### PA-05: Sved, Reed & Bodmer 1967; Sved 1968
- **Citations:**
  - Sved, Reed & Bodmer 1967, "The number of balanced polymorphisms that can be maintained in a natural population", *Genetics* 55:469–481 (PMC1211402).
  - Sved 1968, "Possible rates of gene substitution in evolution", *Am Nat* 102:283–293, doi:10.1086/282542.
- **Access:** metadata only.
- **Summary (secondary; Kern & Hahn 2018):** threshold (truncation) selection and density dependence reduce the cost.
- **Cited in corpus?**
  - In L only, inside Keightley 2012's discussion of load.
  - Audit: REVIEW-R4-steelman-critic.
  - D/C: no hit for `\bSved\b`.

### PA-06: Kimura & Crow 1969, "Natural selection and gene substitution"
- **Citation:** *Genet Res* 13:127–141. doi:10.1017/S0016672300002846.
- **Access:** abstract.
- **Summary:**
  - Reinforcing (synergistic) epistasis can raise or lower the load depending on the model.
  - Haldane's −ln p₀ formula "is still useful".
- **Cited in corpus?** No hit for `Kimura.{0,5}Crow.{0,10}1969` in any group. Day cites Crow & Kimura 1970 (textbook) for composite fitness (Z19984826 §3.3.1).

### PA-07: Felsenstein 1971, "On the biological significance of the cost of gene substitution"
- **Citation:** *Am Nat* 105:1–11. doi:10.1086/282698.
- **Access:** not accessed (403). Secondary: Matheson 2025; Kern & Hahn 2018.
- **Summary:**
  - Derives the minimum spacing between substitutions from finite reproductive excess, n = −ln p₀ / ln k, without assuming an optimal genotype.
  - With k = 1.1 and p₀ = 10⁻⁴, n ≈ 97 generations.
- **Cited in corpus?** No hit for `biological significance of the cost`.
  - The "Felsenstein (1971)" in Day's papers (Z18166234, Z18203514, Z18209114) is a different paper: "Inbreeding and variance effective numbers…", *Genetics* 68:581.
  - The audit's H2-hard cap ln R / D is the same relation, re-derived without citation.

### PA-08: Ewens 1970, "Remarks on the substitutional load"
- **Citation:** *Theor Pop Biol* 1:129–139. doi:10.1016/0040-5809(70)90031-6.
- **Access:** not accessed. Secondary: Matheson 2025.
- **Summary:**
  - Measure the load against the best genotype actually present (the "lead"), not against a nonexistent optimum.
  - At N = 10⁶ the lead is ~4.9 SD above the mean, giving n ≈ 20–24 generations at s = 0.01. Matheson prints ≈ 20. The reviewer notes the printed equation appears to have lost a square root, and the corrected form gives ≈ 24.
- **Cited in corpus?** No hit for `Ewens.{0,15}19[67]` in D/C/R/A. Day cites Ewens 1979 (textbook) in Z18168236's reference list only.

### PA-09: Wallace 1968/1970/1975 (soft selection)
- **Citation:** Wallace 1975, "Hard and soft selection revisited", *Evolution* 29:465–473. doi:10.1111/j.1558-5646.1975.tb00836.x.
- **Access:** not accessed. Secondary: Nunney 2003 (full); Reznick 2016 (abstract).
- **Summary:** with density- and frequency-dependent ("soft") selection, the selective deaths are those that density regulation would cause anyway.
- **Cited in corpus?**
  - Day: yes. Z19984826 §3.3.1 (soft selection, Wallace 1975, "None of them raises s_max above order unity").
  - Critics: soft selection is invoked in prose (Reddit "guest"; Mansfield), with no citation of Wallace.
  - Audit: H, H2 (tested; "soft selection eliminates the cost" not reproduced).

### PA-10: Nei 1971, "Fertility excess necessary for gene substitution in regulated populations"
- **Citation:** *Genetics* 68:169–184. doi:10.1093/genetics/68.1.169.
- **Access:** not accessed (scan behind captcha). Secondary: Matheson 2025.
- **Summary (per Matheson 2025):** the same result as PA-07. The minimum spacing is n = −ln p₀ / ln k. The first pass also said it "requires two life stages (juvenile excess over adults)"; that detail is in no text read here and is **unverified**.
- **Cited in corpus?** No hit for `Nei.{0,15}1971`. "Reproductive excess" appears in prose only (Day Z18168236; keruru).

### PA-11: Grant & Flake 1974, "Solutions to the cost-of-selection dilemma"
- **Citation:** *PNAS* 71:3863–3865. doi:10.1073/pnas.71.10.3863.
- **Access:** abstract.
- **Summary:** there are several "biologically realistic ways around the cost-of-selection restriction" (gene interaction, linkage, population size and structure). There is no single solution.
- **Cited in corpus?** No hit for `Grant.{0,10}Flake`.

### PA-12: ReMine 1993, *The Biotic Message*; ReMine 2005; ReMine 2006
- **Citations:**
  - ReMine 1993, *The Biotic Message* (St. Paul Science).
  - ReMine 2005, "Cost theory and the cost of substitution—a clarification", *J Creation (TJ)* 19(1):113–125.
  - ReMine 2006, "More precise calculations of the cost of substitution", *CRSQ* 43:111–120.
- **Access:**
  - 1993: not accessed.
  - 2005: full (creation.com; sub-agent).
  - 2006: not accessed.
- **Summary:**
  - The 1993 book (per TalkOrigins CB121) allows ~1,667 substitutions in 10 My: 500,000 generations at 20 years, divided by 300.
  - The 2005 paper defines cost as "the reproduction rate required by a scenario". It argues that soft or density-dependent selection does not reduce the minimum cost of a single substitution.
- **Answered by:** TalkOrigins CB121 (PA-13); Musgrave 1999 (TalkOrigins Post of the Month: ReMine's simulation used n = 6 copies). Sub-agent found no peer-reviewed rebuttal of the 2005/2006 arguments.
- **Cited in corpus?**
  - Day: only inside a commenter's sentence that Day quotes ("stick to researchers like … Walter ReMine", blog 2026-10-01 "They Never Stop Lying"). Day himself does not engage ReMine.
  - Fidelity ledger: "ReMine 2005 — record only".
  - Critics: no hit.

### PA-13: TalkOrigins Index to Creationist Claims CB121, "Haldane's dilemma"
- **Citation:** <https://www.talkorigins.org/indexcc/CB/CB121.html> (2001, modified 2006).
- **Access:** full.
- **Summary:**
  - Lists these rebuttals:
    - Haldane's constant-population assumption;
    - recombination allowing simultaneous selection;
    - Haldane's own caveat;
    - most differences neutral;
    - hitchhiking;
    - multi-codon mutations;
    - both lineages diverging;
    - ReMine's n = 6 simulation.
  - Does not cite truncation selection, Nei/Felsenstein, Ewens or Nunney.
- **Quote:** "With corrected calculations, the cost disappears (Wallace 1991; Williams n.d.)."
- **Cited in corpus?** No hit for `talkorigins\|CB121` in any group. (A broader pattern including `talk\.origins` gave one D and one C hit, both unrelated to CB121.)

### PA-14: Nunney 2003, "The cost of natural selection revisited"
- **Citation:** *Ann Zool Fennici* 40:185–194.
- **Access:** full (existing Wayback copy; sub-agent). Already in the corpus as a literature source.
- **Summary:**
  - Hard selection with density regulation. The cost depends on M = 2Ku, the number of beneficial mutations per generation.
  - For M > ½ the cost is "substantially less" than Haldane's. Soft selection "eliminates" it.
  - Simulations cover K = 500 and K = 5,000 only (Table 1, R = 10). At K = 5,000 and u = 5×10⁻⁶ (M = 0.05) the cost is ≈ 429 generations fixed plus ≈ 69 per locus, about 500 for one locus. The "700 generations" in the text is a remark about K = 5,000.
  - K = 10,000 was **not** simulated. Interpolating at the same u (M = 0.1) gives ≈ 150 + 44 per locus ≈ 190, below Haldane's 300. The first pass misstated this as a 5,000–10,000 range.
  - So the paper shows the cost depends strongly on M. Whether humans are in the M ≪ 1 regime is unmeasured, and the "two-sided" label rests on that unknown.
- **Cited in corpus?**
  - Audit only (H2; 18 audit files).
  - Day: no hit.
  - Critics: no hit. The balance ledger already records "No critic engaged Nunney".

### PA-15: Crow & Kimura 1979; Kondrashov 1988; Crow 1997 (truncation and quasi-truncation selection)
- **Citations and access:**
  - Crow & Kimura 1979, "Efficiency of truncation selection", *PNAS* 76:396–399 (abstract).
  - Kondrashov 1988, *Nature* 336:435–440, doi:10.1038/336435a0 (abstract).
  - Crow 1997, "The high spontaneous mutation rate: is it a health risk?", *PNAS* 94:8380–8386 (abstract).
- **Summary:**
  - Truncation or quasi-truncation selection lets one "genetic death" remove several mutations.
  - Crow & Kimura: "Whether nature ranks and truncates, or approximates this behavior, is an empirical question, yet to be answered."
- **Cited in corpus?**
  - In L via Keightley 2012 (which the audit used for H7).
  - Day: argues truncation needs variance the Bernoulli Barrier denies (Z19984826).
  - Critics: no hit for `truncation`.

### PA-16: Lesecque, Keightley & Eyre-Walker 2012, "A resolution of the mutation load paradox in humans"
- **Citation:** *Genetics* 191:1321–1330. doi:10.1534/genetics.112.140343.
- **Access:** full (sub-agent).
- **Summary:**
  - At U ≈ 2.1 deleterious mutations per diploid genome, an absolute (mutation-free reference) model implies ≥ 88% reproductive failure and > 16 offspring per female.
  - Under relative fitness the failing fraction is φ ≈ 0.14–0.19 for U = 2.
  - "a species could tolerate 10's or even 100's of new deleterious mutations per genome each generation" (abstract).
- **Cited in corpus?** No hit for `Lesecque\|resolution of the mutation load`. Its absolute-model figure matches the audit's H7 result (≈ 18 offspring).

### PA-17: Kondrashov 1995; Lynch 2010; Charlesworth 2013
- **Citations:**
  - Kondrashov 1995, "Contamination of the genome by very slightly deleterious mutations: why have we not died 100 times over?", *J Theor Biol* 175:583–594, doi:10.1006/jtbi.1995.0167.
  - Lynch 2010, "Rate, molecular spectrum, and consequences of human mutation", *PNAS* 107:961–968.
  - Charlesworth 2013, "Why we are not dead one hundred times over", *Evolution* 67:3354–3361, doi:10.1111/evo.12195.
- **Access:**
  - Kondrashov: abstract (Europe PMC; lead agent).
  - Lynch: abstract (lead agent); full text per sub-agent only.
  - Charlesworth: abstract (Europe PMC; lead agent).
- **Summary:**
  - Kondrashov (abstract as read by the lead agent via Europe PMC: "there is a dangerous range of selection coefficients, 1/G < s < 1/4Ne"): mutations in that range accumulate nearly freely yet are harmful in aggregate. He considers soft selection and synergistic epistasis as resolutions.
  - Lynch: the abstract says "a substantial reduction in human fitness can be expected over the next few centuries in industrialized societies". The per-generation "at least 1% … as high as 5%" figure is from a sub-agent's full-text read and is **unverified** here (Europe PMC full text not available).
  - Charlesworth: two resolutions, weak stabilizing selection or soft selection. He notes "It may be very difficult to distinguish between these two possibilities."
- **Cited in corpus?**
  - No hit for `Charlesworth.{0,10}2013`.
  - The `Kondrashov` hits are other papers.
  - Ally Hössjer makes the qualitative argument (HO-11), citing Sanford; Day's "Drift Deathmarch" (blog 2026-01-11) is a related argument. See GAP-05.

### PA-18: Graur 2017; Galeota-Sprung, Sniegowski & Ewens 2020
- **Citations:**
  - Graur 2017, "An upper limit on the functional fraction of the human genome", *GBE* 9:1880–1885 (corrigendum 2019).
  - Galeota-Sprung, Sniegowski & Ewens 2020, "Mutational load and the functional fraction of the human genome", *GBE* 12:273–281.
- **Access:** both full (sub-agent).
- **Summary:**
  - Graur: an absolute load model with replacement fertility of 2 caps the functional fraction ("cannot exceed 15%" after correction).
  - Galeota-Sprung et al. answer that a mutation-free individual "is exceedingly unlikely to exist", so the load limit is weak. They tie this explicitly to Wright's critique of Haldane's optimal-genotype assumption.
- **Cited in corpus?** No hits in D/C/R/A (`Graur`: C hits are blogroll links only; `Galeota\|Sniegowski`: D hits are Sniegowski's LTEE mutator papers).

### PA-36: Matheson, Exposito-Alonso & Masel 2025 (post-2019 review that resolves the older debate)
- **Citation:** *Genetics* 229(4):iyaf011. doi:10.1093/genetics/iyaf011 (PMC12005247).
- **Access:** full (sub-agent). Dated 2025, before the June 2026 cutoff; the content was taken from fetched text.
- **Summary:**
  - Reviews Haldane, Kimura, Maynard Smith, Nei, Felsenstein, Ewens and ReMine.
  - Measures the share of deaths that are selective in *Arabidopsis* (517 genotypes, 8 environments) at 8.5–95%, against Haldane's assumed 10%.
  - **The authors' own caveat:** this is one annual plant grown in experimental common gardens, a dataset they describe as not representative of natural conditions. The paper gives no human estimate.
  - Concludes that "relaxing this auxiliary assumption about a critical parameter value resolves Haldane's concerns", while noting there is "no general expression for a speed limit".
- **Cited in corpus?** No hit for `Matheson`. `Masel` hits only Hancock 2024's mention of Masel's waiting-time work.

---

## B. Adaptive fraction, sweep signatures, linkage (empirical and theoretical inputs)

### PA-19: McDonald–Kreitman / DFE estimates for hominids
- **Works and access:**
  - CSAC 2005, *Nature* 437:69 (full, in corpus).
  - Fay, Wyckoff & Wu 2001, *Genetics* 158:1227 (abstract).
  - Zhang & Li 2005, *MBE* 22:2504 (abstract).
  - Bustamante et al. 2005, *Nature* 437:1153 (abstract).
  - Boyko et al. 2008, *PLoS Genet* 4:e1000083 (full).
  - Eyre-Walker & Keightley 2009, *MBE* 26:2097 (full, partial).
  - Enard et al. 2016, *eLife* 5:e12469 (full).
  - Uricchio, Petrov & Enard 2019, *Nat Ecol Evol* 3:977 (abstract).
  - Keightley, Lercher & Eyre-Walker 2005, *PLoS Biol* 3:e42 (full).
  - Messer & Petrov 2013, *PNAS* 110:8615 (abstract).
  - Smith & Eyre-Walker 2002, *Nature* 415:1022 (abstract; *Drosophila*: 45% adaptive, one adaptive substitution every 45 years).
- **Summary:**
  - **All values are for protein-coding amino-acid substitutions.** Human protein α is estimated at:

    | α | Source |
    |---|---|
    | ≈ 0 | CSAC 2005; Zhang & Li 2005 (abstract gives no number); Eyre-Walker & Keightley 2009 (the Table 7 value −0.00, CI −0.30 to 0.24, is from a sub-agent read and **unverified**; the abstract says "little evidence") |
    | 0.10–0.20 | Boyko 2008 |
    | 0.135 | Uricchio 2019 |
    | ~0.35 | Fay 2001 (Old World monkey outgroup) |
    | up to 0.40 | Eyre-Walker & Keightley 2009, with a larger ancestral Nₑ |

  - Noncoding α: the only estimate found is Keightley 2005, which covers hominid 5′/3′ flanks and first introns only ("very low"). No genome-wide noncoding α was found, yet ~98% of human–chimp differences are noncoding (see GAP-01's a_nc table).
  - Messer & Petrov 2013: MK estimates are biased downward when slightly deleterious mutations are present. That applies to the ≈ 0 estimates.
  - CSAC: "the proportion of changes fixed by positive selection seems to be much lower than the previous estimate" (p.77). CSAC's own caveat: the earlier ~35% compared human with Old World monkey genes and used different gene sets for polymorphism and divergence. CSAC attributes the hominid excess of amino-acid divergence primarily to relaxed constraint (see GAP-05).
  - MK estimates are clock-free: they compare polymorphism/divergence ratios within genes.
- **Cited in corpus?**
  - CSAC: cited by both sides for 35M/5M, but its Table 3 passage is never cited (`q polymorphism\|…indistinguishable`: 0 hits outside L).
  - Eyre-Walker & Keightley 2007: in Day's Z18165980 reference list only.
  - All others: no hit (`McDonald.{0,3}Kreitman\|Boyko\|Uricchio\|Fay.{0,10}Wyckoff`).
- See GAP-01.

### PA-20: Birky & Walsh 1988, "Effects of linkage on rates of molecular evolution"
- **Citation:** *PNAS* 85:6414–6418. doi:10.1073/pnas.85.17.6414 (PMC281982).
- **Access:** abstract (lead agent).
- **Summary:**
  - Complete linkage to selected mutations "does not affect the substitution of selectively neutral mutations".
  - It does slow the substitution of advantageous mutations and speed that of deleterious ones (Hill–Robertson).
- **Caveat in the same abstract:** linkage can confound comparisons of substitution rates across genomic regions. The result concerns the *expected* neutral rate, not its variance.
- **Cited in corpus?** One hit for `Birky`, as reference 44 in CSAC 2005's reference list (cited there for rate variation across mammalian genomes). No party argues from it. The first pass reported 0. This bears on Day's Z18637297 (μ/r "channel capacity"). See GAP-03.

### PA-21: Weissman & Barton 2012, "Limits to the rate of adaptive substitution in sexual populations"
- **Citation:** *PLoS Genet* 8:e1002740. doi:10.1371/journal.pgen.1002740.
- **Access:** full (sub-agent).
- **Summary:**
  - Λ/R ≈ (Λ₀/R)/(1 + 2Λ₀/R): interference "prevents the rate of adaptive substitution from exceeding one per centimorgan per 200 generations" (abstract), i.e. Λ_max ≈ R/2 per generation (haploid model).
  - The paper's only example is *Drosophila*. It gives no human example.
  - R/2 is the large-Λ₀ asymptote of an approximate result. The Author Summary says interference prevents rates "from greatly exceeding" one per cM per 200 generations.
  - Applying it to humans needs the map length. Sex-averaged, including X, that is ≈ 35–38 M: Kong et al. 2002 (3,615 cM, via a reproduction of Table 1) and Matise et al. 2007 (3,790 cM, via the reviewer's citation). Neither primary table was read directly.
- **Related:** Neher, Shraiman & Fisher 2010, *Genetics* 184:467 (abstract).
- **Cited in corpus?** No hit for `Weissman`. See GAP-04.

### PA-22: Hernandez et al. 2011, "Classic selective sweeps were rare in recent human evolution"
- **Citation:** *Science* 331:920–924.
- **Access:** abstract-level, via summaries; full text not read.
- **Summary:** the diversity trough around human-specific amino-acid substitutions is no deeper than around synonymous ones. "Classic sweeps were not a dominant mode of adaptation over the past ~250,000 years."
- **Related:**
  - Sabeti et al. 2006, *Science* 312:1614: "several hundred thousand years" came via a secondary source and was not found by the reviewer, so it is **unverified**. Use Hernandez's ~250,000 years, and Przeworski 2002/2003 when retrieved.
  - Murphy, Elyashiv, Amster & Sella 2023, "Broad-scale variation in human genetic diversity levels is predicted by purifying selection on coding and non-coding elements", *eLife* 12:e76065.
    - Abstract: background selection alone explains ~60% of megabase-scale diversity variance, and adding sweeps did not improve the fit.
    - Appendix (lead agent, Europe PMC full text PMC10299832): fitted "fraction of beneficial substitutions, α, is essentially 0 (< 10⁻⁹)". This is a linked-selection model fit for strong sweeps, not an MK α.
  - The reviewer reports that Hernandez's main text bounds the share of human-specific substitutions with a detectable classic sweep at ~5% ("far below 10%"). Not read here: **unverified**.
- **Cited in corpus?** No hit for `Hernandez\|classic sweeps`. Day's Z18452504 §4.3(4) cites Voight 2006, Sabeti 2007 and Pickrell 2009 for "dozens to hundreds" of sweep regions. See GAP-02.

### PA-33: Patterson et al. 2006 and replies (complex speciation)
- **Citation:** Patterson, Richter, Gnerre, Lander & Reich 2006, *Nature* 441:1103–1108. doi:10.1038/nature04789.
- **Access:** abstract.
- **Summary:**
  - Human–chimp genetic divergence varies over "more than 4 million years" across the genome.
  - Speciation is placed at "less than 6.3 million years ago"; the X chromosome is unusually young.
  - The paper proposes hybridization after an initial split.
- **Answered by:**
  - Wakeley 2008, *Nature* 452:E3 ("their claim of hybridization is unwarranted"; abstract).
  - Innan & Watanabe 2006, *MBE* 23:1040 (simple split fits best; abstract).
  - Yamamichi, Gojobori & Innan 2012, *MBE* 29:145 (abstract).
  - McVicker et al. 2009 (selection, not complex speciation; full).
  - Supported by Mailund et al. 2012, *PLoS Genet* 8:e1003125 (isolation-with-migration preferred; full).
- **Cited in corpus?**
  - Day: in a quoted AI list (blog 2026-01-30).
  - keruru: "Forty-Seven", split bounds.
  - Audit: ROOT-M row 13.
  - Low materiality (gaps.md, rejected list).

### PA-34: Per-year clock and generation time
- **Works and access:**
  - Scally & Durbin 2012, *Nat Rev Genet* 13:745 (abstract).
  - Amster & Sella 2016, *PNAS* 113:1588 (full, via summarising fetch).
  - Moorjani, Amorim, Arndt & Przeworski 2016, *PNAS* 113:10607 (full).
  - Besenbacher, Hvilsom, Marques-Bonet, Mailund & Schierup 2019, *Nat Ecol Evol* 3:286 (abstract plus authors' blog).
  - Jónsson et al. 2017, *Nature* 549:519 (abstract).
  - Gao et al. 2019, *PNAS* 116:9491 (full).
  - McVicker et al. 2009, *PLoS Genet* 5:e1000471 (full).
- **Summary:**
  - The yearly mutation rate is fairly insensitive to mean generation time: 19 → 30.4 years changes it by < 2% (Amster & Sella).
  - Paternal age adds ~1.5 mutations per year (Jónsson).
  - Direct ape rates are ≈ 1.48× the human yearly rate (Besenbacher 2019, abstract), which helps reconcile pedigree and phylogenetic dating. The "6.6 Mya" split figure is in **Amster & Sella 2016's** abstract ("may have occurred as recently as 6.6 Mya"). The first pass misattributed it to Besenbacher, whose own figure was seen only in the authors' blog.
  - Split estimates span 5.5–9 Mya across these works.
  - McVicker 2009: background selection reduces autosomal diversity by 19–26% (abstract). Ancestral N_hc ≈ 9.9×10⁴ (7.4×10⁴–1.4×10⁵), with T_hc fixed at 2.4×10⁵ generations (Table 1; lead agent, Europe PMC full text PMC2669884).
- **Cited in corpus?**
  - Day: Moorjani 2016 (9 My, Z18203514); calls the hominoid slowdown a "calibration artifact" (Z18525547; blog 2026-04-28).
  - KITTENS: Moorjani, passing.
  - Others: no hit (`Amster\|Besenbacher\|generation.time effect`).
- See GAP-06.

### PA-35: Germline indel and SV rates
- **Works and access:**
  - Besenbacher et al. 2015, *Nat Commun* 6:5969 (full; indels 1.5×10⁻⁹/nt/gen).
  - Kloosterman et al. 2015, *Genome Res* 25:792 (abstract; 2.94 indels and 0.16 SVs per generation).
  - Belyeu et al. 2021, *AJHG* 108:597 (abstract; ≥ 0.160 de novo SVs per genome).
  - Collins et al. 2020, *Nature* 581:444. Main text (lead agent, Europe PMC PMC7334194): "we used the Watterson estimator to project a mean mutation rate of 0.29 de novo SVs (95% confidence interval 0.13–0.44) per generation in regions of the genome accessible to short-read WGS".
  - Nachman & Crowell 2000, *Genetics* 156:297 (abstract).
- **Cited in corpus?** No hit for `indel (mutation )?rate\|de novo (structural\|SV)` in D/C/R/A. See GAP-07.

---

## C. Waiting times, genetic entropy, conservation of information
These works bear on branches D and G and on ROOT-M. None of them is among the 30 load-bearing nodes. They matter here because they show whether the "specific target vs any outcome" dispute was already resolved in print.

### PA-23: Wistar Institute symposium (1966; proceedings 1967)
- **Citation:** Moorhead & Kaplan (eds), *Mathematical Challenges to the Neo-Darwinian Interpretation of Evolution*, Wistar Symposium Monograph 5 (1967).
- **Access:** full, in the corpus (`sources/raw/sources/pdf/Wistar1967.pdf`, 1985 reprint scan). The fidelity ledger has already audited it.
- **Summary:** Eden's 10^325-vs-10^52 sequence-space argument, with replies by Ulam, Wright, Lewontin and others.
- **Later reply:** Rosenhouse 2022 ch. 4 (PA-32).
- **Cited in corpus?** Yes: Day (45 D files), critics (15 C files), audit (D-branch claims).

### PA-24: Behe & Snoke 2004; Lynch 2005; Behe & Snoke 2005 reply
- **Citations and access:**
  - Behe & Snoke 2004, "Simulating evolution by gene duplication of protein features that require multiple amino acid residues", *Protein Sci* 13:2651–2664, doi:10.1110/ps.04802904 (full; existing Wayback snapshot; sub-agent).
  - Lynch 2005, "Simple evolutionary pathways to complex proteins", *Protein Sci* 14:2217–2225, doi:10.1110/ps.041171805 (full; sub-agent).
  - Behe & Snoke 2005 reply, *Protein Sci* 14:2226 (metadata only).
- **Summary:**
  - Behe & Snoke: a neutral duplicate that needs λ specific changes before selection acts requires N ≥ 10^9 to fix a two-residue feature in 10^8 generations.
  - Lynch: they assume "only two specific amino acid sites" can give the function. With many candidate sites and persisting intermediates, such features arise in ≤ 10^6 years when N > 10^6.
- **Cited in corpus?**
  - Day: "Since I'm not familiar with their work and since their work does not overlap with mine" (Behe and Dembski; blog 2026-10-05).
  - Critics: Hancock 2024, "Waiting-time? No Problem" (TH-1; downloaded, not analysed by the audit), discusses Behe & Snoke and Lynch at length. It predates MITTENS and is not applied to it.
  - Audit: none. `Snoke`: C = 3, A = 1 (bibliography row).

### PA-25: Durrett & Schmidt 2007, 2008; Behe 2009 letter; Durrett & Schmidt 2009 reply
- **Citations:**
  - Durrett & Schmidt 2007, "Waiting for regulatory sequences to appear", *Ann Appl Probab* 17:1–32, doi:10.1214/105051606000000619.
  - Durrett & Schmidt 2008, "Waiting for two mutations: with applications to regulatory sequence evolution and the limits of Darwinian evolution", *Genetics* 180:1501–1509, doi:10.1534/genetics.107.082610.
  - Behe 2009, "Waiting longer for two mutations", *Genetics* 181:819–820.
  - Durrett & Schmidt 2009, "Reply to Michael Behe", *Genetics* 181:821–822.
- **Access:**
  - 2007: abstract.
  - 2008: full (author preprint).
  - 2009 letter and reply: full (existing Wayback snapshots).
  - All read by sub-agent.
- **Summary:**
  - Human parameters: Nₑ = 10^4, μ = 10^-8, 25-year generations.
    - A specific 8-bp binding site takes ~650 My to appear in a 1 kb region from scratch, but ~60,000 years if a 7/8 match suffices.
    - A *prespecified* coordinated pair (knock out a site, then create one) has mean 1/(2N·u1·√u2) ≈ 216 My.
  - The 2008 paper puts Behe's 10^20 malaria figure, scaled to humans, at "five million times larger" than its own estimate.
  - Behe (2009) replies:
    - the 10^20 is "an empirical statistic";
    - there is a 30-fold rate error, which Durrett & Schmidt concede;
    - the first mutation may be deleterious.
  - The 2009 reply states the **specific-vs-any** rule in print: "If there are k nonoverlapping possibilities … [the waiting time] has an exponential distribution with a mean that is divided by k." It concludes that double mutations "can easily have caused a large number of changes in the human genome since our divergence from chimpanzees". It uses the Evelyn Adams lottery analogy.
  - **Scope:** k counts nonoverlapping possible double-mutation targets (≥ 20,000 genes with tens to hundreds of pairs each). The human–chimp conclusion is qualitative; the reply gives no human–chimp numbers. This is a first-occurrence waiting-time result, not a fixation-count result.
- **Cited in corpus?**
  - No hit for `Durrett` in D, C, R or A. (A = 1 is the audit bibliography mentioning it, not a citation.)
  - Critics make the same specific-vs-any argument without citing it (McCarthy MC-01/02; Camestros CA-09; G3/G3a). A concurrent audit check, `R4-G1.md` (2026-10-08), tests that argument but does not cite Durrett & Schmidt.

### PA-26: Lynch & Abegg 2010, "The rate of establishment of complex adaptations"
- **Citation:** *Mol Biol Evol* 27:1404–1414. doi:10.1093/molbev/msq020.
- **Access:** abstract (sub-agent).
- **Summary:** the time to establish a multi-site adaptation "scales by no more than the square of the mutation rate, regardless of the number of sites". Large N shortens it even with deleterious intermediates.
- **Answered by:** Axe 2010 (*BIO-Complexity* 2010(4); citation only).
- **Cited in corpus?** One YouTube comment (C). Otherwise no hit for `Abegg`.

### PA-27: Behe 2007, *The Edge of Evolution*
- **Access:** not accessed. The argument is confirmed via Behe 2009 and Durrett & Schmidt 2008.
- **Summary:** chloroquine resistance (~2 PfCRT changes) has odds of ~1 in 10^20. Features needing two new binding sites are therefore said to be beyond reach for small-N lineages.
- **Answered by** (citations verified, texts not accessed):
  - Carroll 2007, *Science* 316:1427;
  - Miller 2007, *Nature* 447:1055;
  - Durrett & Schmidt 2008 (PA-25).
- **Cited in corpus?** One C hit (a Felsenstein TOC for Rosenhouse). D: none.

### PA-28: Sanford, Brewer, Smith & Baumgardner 2015, "The waiting time problem in a model hominin population"
- **Citation:** *Theor Biol Med Model* 12:18. doi:10.1186/s12976-015-0016-z.
- **Access:** full (Europe PMC; sub-agent).
- **Summary:**
  - Mendel's Accountant runs with N ≥ 10^4 and 20-year generations; benefit is conferred only when a *specified* string is complete.
  - Waiting times: a specific point mutation ~1.5 My; a string of 2 ~84 My; a string of 8 longer than the age of the universe.
  - On parallel targets the authors concede "a very slow trickle" of strings.
- **Answered by:** Hancock 2024 (SLiM re-implementation, in corpus as TH-1). Sub-agent found no peer-reviewed rebuttal.
- **Cited in corpus?**
  - C: Hancock 2024 (TH-1).
  - D: no hit for `Sanford`.
  - Hössjer cites Sanford's *Genetic Entropy*, not this paper.

### PA-29: Sanford, *Genetic Entropy*; Mendel's Accountant; Basener & Sanford 2018
- **Citations:**
  - Sanford, *Genetic Entropy & the Mystery of the Genome* (2005; later editions).
  - Sanford et al. 2007, "Mendel's Accountant", *SCPE* 8:147–165.
  - Basener & Sanford 2018, "The fundamental theorem of natural selection with mutations", *J Math Biol* 76:1589–1622, doi:10.1007/s00285-017-1190-x.
- **Access:**
  - Book: not accessed.
  - Mendel's Accountant: not accessed.
  - Basener & Sanford: abstract.
- **Summary:** nearly neutral deleterious mutations escape selection, so fitness declines.
- **Answered by:** Hancock & Cardinale 2024, "Back to the fundamentals: a reply to Basener and Sanford 2018", *J Math Biol* 88, doi:10.1007/s00285-024-02077-w (abstract). Its simulations "produce unrealistic results". Hancock is a critic in this corpus.
- **Cited in corpus?**
  - Ally Hössjer cites *Genetic Entropy* (2008) and Basener & Sanford 2018 (hossjer-mittens-review refs; HO-11), and says "Although Vox Day does not cite John Sanford, this is essentially Sanford's genetic entropy argument".
  - D: no hit for `Sanford\|genetic entropy`.
  - Hancock & Cardinale 2024 is not cited by any party (`Basener\|Cardinale`: C hits are Hössjer's references and forum posts).
- See GAP-05.

### PA-30: Hössjer, Bechly & Gauger 2018, 2021; Hössjer & Gauger 2019
- **Citations:**
  - Hössjer, Bechly & Gauger 2018, "Phase-type distribution approximations of the waiting time until coordinated mutations get fixed in a population", in *Stochastic Processes and Algebraic Structures* (Springer PROMS), pp. 245–313.
  - Hössjer, Bechly & Gauger 2021, "On the waiting time until coordinated mutations get fixed in regulatory sequences", *J Theor Biol* 524:110657, doi:10.1016/j.jtbi.2021.110657 (CC BY).
  - Hössjer & Gauger 2019, *BIO-Complexity* 2019(1).
- **Access:**
  - 2021: full (author-hosted PDF; sub-agent).
  - Others: citation only.
- **Summary:**
  - Moran model, N = 10^4, μ = 10^-8, neutral.
  - Expected time to fix new binding sites at m genes: ≈ 5.4×10^7 generations (m = 1) up to 3.3×10^10 (m = 6, with back-mutation).
  - The time grows exponentially in m when back-mutation is allowed.
  - The paper concedes: "The waiting time will be shortened even more if there are many possible targets."
- **Answered by:** Rasmussen, Panda's Thumb, 12 Jun 2021 (blog; sub-agent, summariser-quoted).
- **Cited in corpus?**
  - Hössjer's MITTENS review (p.7) cites the 2021 model and predicts the waiting time for coordinated expression change "far exceeds 9 million years". It adds: "this mathematical model has not yet been applied to humans and chimps".
  - The audit has not mapped this prediction to any node (`far exceeds 9 million`: 0 hits in R/A).
  - Day: no hit for `Bechly\|Gauger`.

### PA-31: Dembski, Marks, Ewert and colleagues (evolutionary informatics)
- **Citations** (Crossref-verified; texts not accessed):
  - Dembski & Marks 2009, "Conservation of information in search: measuring the cost of success", *IEEE Trans SMC-A* 39:1051–1061, doi:10.1109/TSMCA.2009.2025027.
  - Ewert, Dembski & Marks 2009, Avida NAND paper, IEEE SMC.
  - Montañez, Ewert, Dembski & Marks 2010, "A vivisection of the ev computer organism", *BIO-Complexity* 2010(3).
  - Dembski 2002, *No Free Lunch*.
- **Summary:**
  - Search beats blind search only with "active information" supplied by its design.
  - Weasel and ev are said to succeed because of oracles built into them.
- **Answered by:**
  - Felsenstein 2007 (*Reports of the NCSE* 27).
  - Elsberry & Shallit 2011 (*Synthese* 178:237).
  - Felsenstein & English (Panda's Thumb, 2015).
- **Cited in corpus?**
  - No hit for `Ewert`.
  - `conservation of information`: C = 1 file (Dembski material).
  - Day "not familiar" with Dembski's work (blog 2026-10-05).
  - Dembski is an ally who gives "no calculation" (balance ledger).

### PA-32: Rosenhouse 2022, *The Failures of Mathematical Anti-Evolutionism*
- **Citation:** Cambridge UP. doi:10.1017/9781108907149.
- **Access:** chapter list only (Crossref).
- **Contents:** ch. 4 "The Legacy of the Wistar Conference" (pp.84–109); ch. 5 "Probability Theory"; ch. 6 "Information and Combinatorial Search" (NFL, conservation of information).
- **Not confirmed:** whether it treats Haldane's dilemma or Durrett–Schmidt.
- **Cited in corpus?**
  - Day transcribes and attacks ch. 4 (D-branch claims).
  - Felsenstein's TOC and Young's review are in C.
  - Book not accessed (fidelity ledger).

### PA-37: Bastian, Enard & Lartillot 2026 (post-cutoff; from fetched text only)
- **Citation:** "Empirical validation of the nearly neutral theory at divergence and population-genomic scales using 144 placental mammal genomes", *Genome Biol Evol* 18(4):evag030. Published 6 Apr 2026. doi:10.1093/gbe/evag030.
- **Access:** full (Europe PMC; sub-agent).
- **Summary:** across ~150 mammals, πN/πS and dN/dS co-vary with life history and πS. This is consistent with a single hidden variable, Nₑ, as nearly neutral theory predicts. It does not address waiting times or Haldane's cost.
- **Cited in corpus?** One Reddit comment (arctic-tree-1wv4zeg), with no numbers.

---

## D. What the prior art already settles, and what it does not
1. **Specific vs any outcome (G; Day's Bernoulli barrier and "Darwillion").**
   - The published resolution is Durrett & Schmidt 2009: the expected wait is divided by the number k of acceptable targets. Lynch 2005 makes the same point against Behe & Snoke 2004.
   - The critics' argument (McCarthy, Camestros) restates it without citation.
   - The other side also has a published position: Behe 2009 and Sanford et al. 2015 argue that particular adaptations need particular fixes. A mainstream result partly agrees: Chatterjee et al. 2014 (*PLoS Comput Biol* 10:e1003818; abstract via sub-agent) find exponential times are possible even with many targets in some landscapes.
   - **Status:** a dispute over modelling choices, not unresolved mathematics.
2. **Whether waiting-time limits cap the *total* number of fixations.**
   - No prior-art paper claims that they do. Every waiting-time result concerns one particular multi-site adaptation.
   - The total-count limit in this literature comes only from Haldane's cost, which applies to adaptive substitutions.
   - MITTENS's use of a rate limit on all fixations is therefore not inherited from the waiting-time literature.
3. **Haldane's dilemma.**
   - The literature contains several quantitative resolutions, each with an empirical condition attached:
     - fertility excess, n = −ln p₀ / ln k (Nei 1971; Felsenstein 1971);
     - measuring against the lead genotype (Ewens 1970);
     - truncation selection (Maynard Smith 1968; Sved 1968);
     - soft selection (Wallace; Nunney 2003);
     - neutrality (Kimura 1968).
   - A modern review measures the decisive parameter, the selective-death share, at 8.5–95% against Haldane's 10% (Matheson et al. 2025). That measurement comes from one annual plant in common gardens, which the authors call unrepresentative of natural conditions, and the review gives no human value.
   - Nunney 2003 shows the cost depends strongly on beneficial supply M = 2Ku. At M = 0.05 (K = 5,000) it is ~500 generations, above Haldane's 300. At M ≥ 0.1 it is below 300 (≈ 190 is an interpolation). Human M is unmeasured.
   - The current dispute has not used any of these numbers. Day engages Maynard Smith, Wallace and Crow & Kimura in prose only. The critics cite none. The audit re-derived the Nei–Felsenstein cap without citation.
4. **Empirical input neither side uses.** The adaptive fraction α (PA-19) decides whether Haldane's cap binds.
   - **Coding only:** at published α (0–0.4), adaptive amino-acid substitutions per human lineage are ~10³–10⁴, within ~1–14× of Haldane's 840 and near the fertility-excess cap at k ≈ 1.1–2.
   - **Noncoding:** ~98% of differences are noncoding, and no genome-wide noncoding α exists. A noncoding adaptive share of 1–5% would give ~2–9×10⁵ adaptive substitutions, 200–1,000× Haldane's limit. That still leaves 20–100× fewer than Day's 17.5M. See GAP-01.

---

## Revision note
Revised on 2026-10-08 after the fact-check in `ledgers/gaps-review.md`. The item-by-item mapping is in `ledgers/gaps.md` § "Review resolution". Changes in this file:
- PA-03: Kern & Hahn caveats and Jensen 2019.
- PA-08: n ≈ 20–24.
- PA-10: formula per Matheson; two-stage detail flagged unverified.
- PA-14: Nunney's simulated K values.
- PA-17: Lynch per-generation figure marked unverified.
- PA-19: α values labelled coding-only; noncoding caveat; Messer–Petrov bias; CSAC caveats.
- PA-20: Birky corpus hit and caveats.
- PA-21: W&B asymptote and map length.
- PA-22: Murphy and Sabeti restricted; Hernandez ~5% marked unverified.
- PA-25: Durrett & Schmidt scope.
- PA-34: 6.6 Mya re-attributed; McVicker Table 1.
- PA-35: Collins locator.
- PA-36: Matheson caveat.
- §D.3–4: Nunney and Matheson wording; noncoding bracket.

## Additions 2026-10-09b (retrieved sources; see bib-literature "Refresh 2026-10-09b")
- **PA-38: Standing variation and soft sweeps (Hermisson & Pennings 2005; Messer & Petrov 2013).** Bear on G2c (Hancock's standing-variation prediction), A6 and A6a. Hermisson & Pennings (abstract read): a "large increase in the fixation probability for weak substitutions" when alleles come from standing variation, favoured "if either the selective advantage is weak or the selection coefficient and the mutation rate are both high". Messer & Petrov (full text): soft sweeps "might be the dominant mode of adaptation in many species"; "Hard sweeps are expected when adaptive alleles are not present ... and when the waiting time for adaptive mutations is long". Both sides can cite: the first favours Hancock, the second states the condition Day assumes. Unresolved: which regime applies to the human-chimp substitutions (needs s and mutation rate).
- **PA-39: Mutation load under relative fitness (Lesecque et al 2012) and relaxed selection (Lynch 2016).** Bear on H, H10, GAP-05. Lesecque (abstract): a species could tolerate "10's or even 100's" of new deleterious mutations per genome per generation under relative-fitness selection. Lynch (full text): expects "genetic deterioration in the baseline human condition" from relaxed selection against mildly deleterious mutations. These are consistent with each other (a sizeable load is tolerable; relaxation raises it slowly) and neither supports a claim of fixation of harmful alleles at three times the neutral rate.
- **PA-40: Rate of adaptation in large asexual populations (Desai & Fisher 2007).** Bears on A2e and E7. Abstract: the rate of accumulating beneficial mutations "grows only logarithmically with population size and mutation rate" (asexual). Day-side use: LTEE rates are not inflated by size. Critic-side use: they are specific to asexual interference and set no ceiling for sexual populations. Full text not read.
- **PA-41: Simulators for the planned tool.** SLiM 4 (Haller & Messer 2023; forward, genetically explicit), msprime 1.0 (Baumdicker et al 2022; coalescent), fwdpy11 (GitHub description only). Relevant to the XT cross-tool replication; no claim depends on them.

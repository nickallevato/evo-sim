# Gaps Ledger: Considerations No Party Has Addressed

Version: 2026-10-08 (first pass; revised the same day after the fact-check in `ledgers/gaps-review.md`, see "Review resolution" at the end; R4 check results for GAP-04, GAP-07 and GAP-02 added in blocks marked "(R4 2026-10-08)", from `research/checks/results/R4-GAPS-04-07-02.md`; GAP-01 (H3) and the GAP-07 direct alignment count (R4-GAP07b-alignment.md) added in blocks marked "(R4 2026-10-09)"). Scope: the 30 load-bearing nodes in `hierarchy.yaml`. Companion file: `sources/prior-art.md` (PA-xx IDs below).

## Definition
A **gap** is a consideration that meets all four conditions:
1. It materially bears on at least one load-bearing node.
2. A competent population geneticist would raise it.
3. No party in the corpus has addressed it. The parties are Day and his allies, his critics, and this audit itself.
4. Its absence is **shown**, by a search that can be re-run, not assumed.

A hit that only names a term in passing does not count as "addressed". Every such judgement is stated as "passing" below.

## Method
1. **Coverage matrix.** Rows are the 30 load-bearing nodes. Columns are 15 considerations: the 13 listed below from the brief (with linkage split into K7 and K7b) plus one found during the search (K14).
2. **Searches.** Each cell was decided by a case-insensitive regex search, followed by reading the hits in context.
3. **Gap entries.** Each confirmed gap records:
   - the node(s) it bears on;
   - why it matters;
   - which side it would likely help, and why;
   - a back-of-envelope size estimate;
   - the literature, with access status;
   - the cheapest correct check.
4. **Balance control (E6).** The search hunted equally for gaps that would favour Day and gaps that would favour the critics. The tally is at the end.

### How to re-run the searches
**Corpus searched (read-only):**
- `sources/raw/` (gitignored, untrusted; never execute anything in it). Extracted to plain text outside the repo:
  - PDF: `pdftotext -layout`
  - HTML/XML: tags stripped, `script`/`style` dropped
  - DOCX/ODT: `word/document.xml` / `content.xml` with tags stripped
  - JSON: all string values concatenated
  - TXT/VTT: as is
- `docs/research/sources/quotes-*.md`, `claims/*.md` and `opponents/*.md`.
- The audit's own files: `research/checks/*.md`, `research/checks/results/*.md`, `research/checks/*.py`, `ledgers/*.md`, `glossary.md`, `parameters.yaml`, `hierarchy.yaml`, `PLAN.md` and `sources/bib-*.md`.

**Counting:** files are de-duplicated by stem, so a blog post's `.html` and `.txt` copies count once. Tag/archive pages that reprint a post do count separately; that inflates `rawD` counts but never turns a zero into a hit.

**Column codes:**

| Code | Files searched |
|---|---|
| D | Day raw (`sources/raw/day/`) |
| C | critics and allies raw (`sources/raw/critics/`) |
| L | literature raw (`sources/raw/sources/`) |
| R | repo claims + opponents + quotes |
| A | audit files |

Counts below are files / matches.

**Search terms (regex, case-insensitive), counts and judgement:**

| # | Term (regex) | D | C | L | R | A | Judgement after reading hits |
|---|---|---|---|---|---|---|---|
| S1 | `McDonald.{0,3}Kreitman\|\bMK test` | 0 | 0 | 2/3 | 0 | 0 | L hits are Good 2017 (LTEE) only. Nobody applies MK to hominids. |
| S2 | `polymorphism.{0,40}divergence.{0,60}indistinguishable\|q polymorphism\|fixed by positive selection` | 0 | 0 | 2/8 | 0 | 0 | The only hits are CSAC 2005 itself (p.77, Table 3). No party cites this passage. |
| S3 | `proportion of (adaptive\|amino acid substitutions)\|fraction of (adaptive…)\|adaptive substitution` | 6/16 | 7/11 | 0 | 6/13 | 4/4 | Passing only. Day: "adaptive fixations (which are comparatively rare)" (blog 2026-05-07). keruru: "estimated 700,000 adaptive substitutions", **unsourced** (ck-probability-zero-a-review-too-late). Reddit: "estimates are modest and contested" (arctic-title-MITTENS §12). No number from data. |
| S4 | `Eyre.?Walker` / `Boyko\|Uricchio\|Enard\|Galtier\|Fay.{0,10}Wyckoff` | 1/2 / 0 | 0 / 2/3 | 6/61 / 4/22 | 0 | 0 | Day: Eyre-Walker & Keightley 2007 appears in the reference list of Z18165980 only. C: one Reddit comment cites a 2026 nearly-neutral paper, no numbers (arctic-tree-1wv4zeg); the other C hit is a YouTube-metadata false match. |
| S5 | `indel (mutation )?rate\|rate of indel\|de novo indel` | 0 | 0 | 2/12 | 0 | 0 | L = Keightley 2012 / Besenbacher context only. |
| S6 | `(structural variant\|SV) (mutation )?rate\|de novo (structural\|SV)\|de novo copy number` | 0 | 0 | 0 | 0 | 0 | none |
| S7 | `generation.time effect` | 0 | 0 | 2/2 | 0 | 0 | none in D/C/R/A |
| S8 | `paternal age\|father'?s age\|male.biased mutation\|male mutation bias` | 1/2 | 1/1 | 11/52 | 2/2 | 1/1 | D: Kong 2012 in a reference list. C: keruru, one sentence ("mutation rate is a function of paternal age"). R: Kong's μ used as an input. Passing. |
| S9 | `hominoid slowdown\|rate slowdown\|slowdown` | 12/33 | 3/5 | 4/8 | 1/1 | 0 | Day addresses it as a "calibration artifact" (blog 2026-04-28; Z18525547). It is an assertion, not a calculation. |
| S10 | `Besenbacher\|Moorjani\|Amster\|Gao.{0,8}(2016\|2019)` | 8/29 | 4/11 | 3/19 | 6/7 | 4/8 | D: Moorjani 2016 is used for a 9 My date (Z18203514). C: KITTENS cites Moorjani for "known uncertainty of molecular-clock calibration". Some D hits are false matches ("Hamster"). Passing. |
| S11 | `Patterson` / `gene flow\|hybridi[sz]\|introgress\|complex speciation` | 4/6 / 34/89 | 2/5 / 11/31 | 13/27 | 0 / 2/7 | 1/1 | D: blog 2026-01-30 quotes a reader's AI list ("Patterson et al. found evidence for continued hybridization"). C: keruru "Forty-Seven" cites Patterson for split bounds. ROOT-M row 13: Day "asserted, not computed". |
| S12 | `gene conversion\|gBGC` / `\bCpG` | 4/16 / 3/16 | 1/1 / 0 | 8/18 / 15/236 | 2/9 / 0 | 1/1 / 2/3 | gBGC: named by Day only (ROOT-M row 8). CpG: Day uses it as a penalty (Q&A 2026-01-19: "CpG… 10-18 times the background rate"). |
| S13 | `Hill.{0,3}Robertson` / `background selection` / `map length\|centimorgan\|\bMorgans\b` | 8/40 / 7/38 / 4/21 | 3/3 / 1/2 / 0 | 0 / 9/16 / 10/48 | 5/9 / 0 / 1/8 | 2/2 / 2/2 / 5/8 | Day addresses linkage in prose in several papers, and quantitatively in Z18637297 ("channel capacity", μ/r ≈ 1–1.5). C: Reddit, passing. A: F2 maps of 0.1 and 1.5 M only. |
| S14 | `Weissman` | 0 | 0 | 0 | 0 | 0 | none |
| S15 | `Birky` / `linkage.{0,40}(neutral substitution\|substitution rate)\|…` | 0 / 0 | 0 / 0 | 1/1 / 0 | 0 / 0 | 0 / 0 | The one L hit is CSAC 2005's reference list (ref. 44, Birky & Walsh, cited for rate variation across mammalian genomes). It is not an argument by any party. The first pass reported 0 here; corrected after review. |
| S16 | `channel capacity\|meiotic bandwidth\|transmission channel\|μ/r\|mu/r` | 12/176 | 0 | 0 | 1/2 | 1/2 | Day only. The audit (ROOT-M row 11) records it as "not extracted yet". No critic engages it. |
| S17 | `selection scan\|sweep scan\|classic(al)? sweeps\|Hernandez\|…\|iHS` | 2/4 | 2/21 | 7/35 | 0 | 0 | D: Z18452504 §4.3(4) "selection scans would be saturated with signals". C hits are YouTube-metadata false matches. Nobody replies. |
| S18 | `250,000 years\|several hundred thousand years` | 0 | 0 | 2/4 | 0 | 0 | Nobody applies a detection window to Day's saturation argument. One partial exception: keruru ("Forty-Seven") remarks of a single fusion locus that "A sweep that old would have faded". That is qualitative, about one site, and not addressed to Z18452504. |
| S19 | `mutational load\|genetic load\|mutation load\|drift load\|substitutional load\|load paradox` | 17/62 | 4/8 | 12/27 | 2/3 | 3/4 | A: Keightley-based H7 check (hard/soft/synergistic). D: "Drift Deathmarch" (blog 2026-01-11). |
| S20 | `Kondrashov` / `Lesecque` / `Charlesworth.{0,10}2013` | 4/10 / 0 / 0 | 3/30 / 0 / 0 | 5/56 / 0 / 0 | 1/3 / 0 / 0 | 0 / 0 / 0 | Kondrashov hits are other papers (1988 sex; Kondrashov & Crow), not the 1995 "died 100 times over" argument. |
| S21 | `slightly deleterious\|nearly neutral\|relaxed constraint` | 3 | 9 | — | 0 | 0 | Ally Hössjer (review p.~6): slightly deleterious fixations "accumulate" (HO-11), with no calculation. A Reddit commenter cites a 2026 paper. Nobody quantifies it. |
| S22 | `Haldane'?s dilemma` / `ReMine\|Biotic Message` / `Maynard.Smith` / `Van Valen` / `Grant.{0,10}Flake` | 1/8 / 3/4 / 1/4 / 0 / 0 | 2/5 / 0 / 1/1 / 0 / 0 | 0 / 0 / 2/2 / 0 / 0 | 1/1 / 1/1 / 2/2 / 0 / 0 | 1/1 / 2/3 / 1/1 / 0 / 0 | Day engages Maynard Smith 1968, Wallace 1975 and Crow & Kimura 1970 in prose (Z19984826 §3.3.1, line ~308). ReMine appears only in a commenter's sentence quoted by Day (blog 2026-10-01). Critics: a YouTube comment only. |
| S23 | `Nunney` | 0 | 0 | 2/38 | 10/53 | 18/89 | audit only (H2) |
| S24 | `Behe` / `Durrett` / `waiting.time` / `Sanford\|genetic entropy` / `Bechly\|Gauger` | 5/6 / 0 / 11/44 / 0 / 0 | 11/32 / 0 / 19/125 / 6/82 / 3/5 | 0 | 0 / 0 / 3/4 / 1/1 / 0 | 1/1 / 0 / 1/3 / 0 / 0 | Hancock 2024 video "Waiting-time? No Problem" (TH-1) treats Behe & Snoke, Lynch and Sanford 2015, but predates MITTENS. Hössjer cites his own 2021 waiting-time model. Day: "I'm not familiar with their work" (Behe/Dembski; blog 2026-10-05). |
| S25 | `Ewert` / `conservation of information` | 0 / 0 | 0 / 1/4 | 0 | 0 | 0 | passing |
| S26 | `Maruyama` / `sweepstakes\|multiple.merger\|Cannings` / `overlapping generation` | 2/6 / 7/50 / 64/344 | 0 / 5/8 / 17/119 | — | 4/5 / 5/15 / 11/26 | 3/7 / 7/16 / 12/16 | addressed (Day, audit) |
| S27 | `soft sweep\|standing (genetic )?variation\|Hermisson\|Pennings\|Przeworski` / `polygenic` | 38/172 / 18/57 | 13/39 / 3/11 | — | 11/18 / 2/2 | 5/9 / 1/4 | addressed (Day Z18452504 §4.3; Hancock B6c; audit H D-values) |
| S28 | `diminishing returns\|Wiser` | 7/12, 4/13 | 5/6, 1/1 | — | 0, 1/2 | 1/1, 4/4 | Day addresses it (Z18167588; Z23020792). |
| S29 | `Nei.{0,15}1971\|fertility excess\|reproductive excess` | 5/9 | 2/3 | 0 | 1/1 | (see note) | "Reproductive excess" appears in prose (Day Z18168236; keruru). Nobody cites Nei 1971 or the fertility-excess spacing formula. The audit's H2-hard re-derives the same cap (ln R / D) without citing it. |
| S30 | `Matheson\|Masel` / `biological significance of the cost` / `Ewens.{0,15}19[67]` | 0 / 0 / 1/2 | 2/4 / 0 / 0 | 0 / 0 / 4/12 | 0 | 0 | The C hits for Masel are Hancock 2024 on waiting times, not Matheson 2025. The D Ewens hit is the 1979 textbook in a reference list. Felsenstein's 1971 *cost* paper (Am Nat): 0 hits. The Felsenstein 1971 that Day cites is the Nₑ paper (Genetics 68:581). |
| S31 | `Kern.{0,10}Hahn` | 1/4 | 0 | 0 | 0 | 0 | Day cites Kern & Hahn 2018 as a challenge to neutral theory (Z18167588). The same paper says correcting Kimura's 1968 count of coding sites "alone would remove the conflict" with Haldane's cost (per sub-agent full-text read). That would be a partial-fidelity point. But Kern & Hahn 2018 is a Perspective, writes "300 years" where generations are meant, and is contested by Jensen et al. 2019 (*Evolution* 73:111, doi:10.1111/evo.13650; abstract read). |

*Note on the "A" column:* all counts above were taken before this file existed, and they exclude files written concurrently by other sessions on 2026-10-08 (`R4-G1.md`, `docs/research/argmap/`). A re-run must exclude `ledgers/gaps.md` itself, or every term will hit.

## Coverage matrix
**Column key (considerations):**

| Code | Consideration |
|---|---|
| K1 | Variance or probability of the observed outcome |
| K2 | Adaptive fraction α (MK/DFE) |
| K3 | Per-year vs per-generation clock, generation time, paternal age |
| K4 | Gene flow / complex speciation |
| K5 | Indel/SV event counts from mutation rates |
| K6 | gBGC, CpG, saturation, rate heterogeneity |
| K7 | Linkage: Hill–Robertson, background selection (BGS), finite map |
| K7b | Neutral substitution rate under linkage |
| K8 | Load, meltdown, epistasis, beneficial supply/DFE, adaptive walk |
| K9 | Structure, overlapping generations, sweepstakes |
| K10 | Soft sweeps, standing variation, polygenic adaptation |
| K11 | LTEE → mammal transfer |
| K12 | Haldane's-dilemma prior art |
| K13 | Waiting-time, genetic-entropy and conservation-of-information prior art |
| K14 | Detection window of sweep signatures |

**Cell codes:**
- **D**: Day or an ally addressed it (beyond passing).
- **C**: a critic addressed it.
- **A**: this audit addressed it.
- **✗n**: relevant, nobody addressed it; see GAP-0n. A trailing "(p)" means there are passing mentions only.
- **·**: not material to this node.
- **r**: considered and rejected as immaterial; see the rejected list.

| Node | K1 | K2 | K3 | K4 | K5 | K6 | K7 | K7b | K8 | K9 | K10 | K11 | K12 | K13 | K14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A (MITTENS) | r | ✗01(p) | D(p) ✗06 | r | C A ✗07 | D | D A ✗04 | · | D | D A | D C A | D C A | D | C | · |
| A2e (LTEE ceiling) | C A | · | · | · | · | · | A ✗04 | · | D | · | · | D C A | · | · | · |
| B (neutral can't rescue) | r | ✗01 | D(p) | · | · | D | D | ✗03 | ✗05(p) | D A | C A | · | D | · | · |
| B1 (steady-state) | r | · | · | · | · | · | · | ✗03 | · | A | C A | · | · | · | · |
| B1c (pipeline at split) | · | · | A ✗06 | r | · | · | ✗06 | · | · | A | C A | · | · | · | · |
| B2 (Hard Limits) | D A | · | · | · | · | · | · | · | · | D A | · | · | · | · | · |
| B2b (ceiling X) | A | · | · | · | · | · | · | · | · | D A | · | · | · | · | · |
| B3 (k≠μ family) | · | · | · | · | · | · | · | ✗03 | · | D A | · | · | · | · | · |
| B3a (μN/Nₑ) | · | · | · | · | · | · | · | · | · | D A | · | · | · | · | · |
| B3g (concession) | · | · | · | · | · | · | · | · | · | D A | · | · | · | · | · |
| B4a (2μT+θ_anc) | A | · | A ✗06 | r | · | r | ✗06 | · | · | A | A | · | · | · | · |
| B5 (critics' k=μ) | r | ✗01 | · | · | · | r | · | ✗03 | ✗05 | A | · | · | · | · | · |
| B6 (full pipe) | · | · | ✗06 | r | · | · | · | · | · | · | C A | · | · | · | · |
| B7 (1/2N) | · | · | · | · | · | · | · | · | · | A | · | · | · | · | · |
| C2 (d = 0.45) | · | · | D A | · | · | · | · | · | · | D A | · | · | · | · | · |
| C2a (d formula) | · | · | D A | · | · | · | · | · | · | D A | · | · | · | · | · |
| E5 (−906 estimator) | C A | · | · | · | · | · | · | · | · | · | · | C A | · | · | · |
| E6 (5,496 vs 8,679) | D A | · | · | · | · | · | · | · | · | · | · | D A | · | · | · |
| F (fix-time limits) | · | · | · | · | · | · | D A ✗04 | · | · | · | D | · | · | · | · |
| F1 (latency≠throughput) | · | · | · | · | · | · | A | · | · | · | · | · | · | · | · |
| F1a (19,800) | · | · | · | · | · | · | · | · | · | · | · | D A | · | · | · |
| F2 (pipelining feasibility) | · | ✗01 | · | · | · | · | D A ✗04 | · | D | · | D | D A | · | · | ✗02 |
| F3a (s = 0.001) | · | ✗01 | · | · | · | · | · | · | ✗01 | · | · | · | · | · | · |
| H (Haldane 1/300) | · | ✗01(p) | · | · | · | · | A | · | A | D A | A | · | D A | · | ✗02 |
| H1 (Term 3 scope) | · | ✗01 | · | · | · | · | · | · | · | · | · | · | D | · | · |
| H2 (Nunney) | · | ✗01 | · | · | · | · | · | · | A | · | A | · | A | · | · |
| H5 (Hössjer cost step) | · | ✗01 | · | · | · | · | · | · | D(p) ✗05 | · | · | D A | D | D | · |
| H8 (Term 3 / §6.4) | · | ✗01 | · | · | · | · | D | ✗03 | · | D A | · | · | D | · | · |
| ROOT | r | ✗01 | D(p) | r | C A | D | D ✗04 | ✗03 | D(p) ✗05 | D A | D C A | D C A | D | C D | ✗02 |
| ROOT-M (mechanisms) | · | ✗01 | · | D(p) | A | D(p) r | D ✗03 | ✗03 | D(p) ✗05 | D A | D C A | D C A | D | C D | ✗02 |

**Reading the matrix:**
- Most cells are covered by at least one party.
- The ✗ cells cluster in three places:
  - **K2 (α).** This column is ✗ in 12 rows. It is the single largest omission.
  - **Linkage.** Neutral-rate invariance under linkage (K7b), and finite-map limits at human scale (K7).
  - **The empirical-signature argument (K14).** Day made it; no one has answered it.

---

## Confirmed gaps
Ranked by how much each could move a load-bearing verdict.

### GAP-01: The adaptive fraction α has never been put into the argument, although the corpus's own source contains it
**Nodes:** ROOT, ROOT-M, A, B, B5, H, H1, H2, H5, H8, F2, F3a.

**What is missing**

Day compares an adaptive-rate ceiling with *all* differences:
- Haldane gives 487 (Z18168236), against 20M.
- Term 3 against 17.5M (H8).

Since 2026-05-07, Day concedes Term 3 limits "adaptive substitution only" (H1). He also says the required adaptive count "K… is not derivable from first principles" (Z23020792).

The critics answer "most differences are neutral" but never give a number. The only number in the corpus is keruru's unsourced "estimated 700,000 adaptive substitutions" (S3). The audit's own B5a lists "a sourced neutral fraction" as verdict-changing, but has not sourced one.

No party cites the McDonald–Kreitman or DFE literature for hominids (S1, S4). CSAC 2005 is cited by both sides for 35M and 5M, yet nobody uses the MK-type test it reports (S2). CSAC found Kₐ/Kₛ for human common polymorphisms and for human–chimp divergence "statistically indistinguishable (Table 3)" (q ≈ 0.21–0.23 vs 0.23; CSAC 2005 p.77). It concluded that the proportion fixed by positive selection "seems to be much lower than the previous estimate" of ~35%. That 35% came from a human–Old World monkey comparison (Fay et al. 2001).

**A claim in the corpus this bears on directly.** Day, Z19984826 §6.4 (H8): "the empirical claim that 'most substitutions are neutral' is itself derived from observing that genome-wide k approximates μ … Strip the clock, and there is no independent estimate of the neutral fraction left to invoke."
- MK-type estimates compare ratios of polymorphism to divergence at the same genes. No divergence date or clock calibration enters the ratio.
- Constraint estimates (Rands 2014: 8.2% of the genome under constraint, 7.1–9.2%) are also not clock-dated.
- The claim is therefore contradicted by the literature. This is an external-validity point. Nobody in the corpus has made it, and the H8 claim file records the §6.4 quote with no response.

**Why it matters**
- It turns the dispute into a well-posed comparison: required *adaptive* substitutions per lineage, K_a, against each candidate ceiling. The candidates are Haldane, Term 3, H2-hard's ln R/D, and F2/W&B interference.
- It sets the realistic regime for F2. F2's open caveat ("human-scale active loci ~1e4–1e5 untested") assumes all 20M are adaptive.

**Size (back of envelope; inputs sourced unless marked `derived:`)**

*Inputs:*
- Amino-acid differences per lineage: CSAC's "typical orthologue differing by only two amino acids, one per lineage" (p.70, abstract), over 13,454 1:1 orthologues. `derived:` ≈ 1.3×10⁴ (median-based, lower end) to ≈ 3×10⁴ (20k genes × 1.5).
- Human α. **Every value below is for protein-coding amino-acid substitutions only.**

  | α | Source |
  |---|---|
  | ≈ 0 | CSAC 2005; Zhang & Li 2005 (abstract gives no α number); Eyre-Walker & Keightley 2009 ("little evidence" in the abstract; the Table 7 value −0.00, CI −0.30 to 0.24, is from a sub-agent read and is not verified by the reviewer) |
  | 0.10–0.20 | Boyko 2008 |
  | 0.135 | Uricchio, Petrov & Enard 2019 (72% from weakly adaptive variants) |
  | up to ~0.40 | Eyre-Walker & Keightley 2009, if ancestral Nₑ was larger |
  | ~0.35 | Fay 2001 (Old World monkey outgroup) |

- Messer & Petrov 2013: MK estimates of α "severely underestimate" the true rate when slightly deleterious mutations are present. That bias applies to the low estimates above.
- **Noncoding α.** The only estimate in hand is Keightley, Lercher & Eyre-Walker 2005, covering hominid 5′/3′ flanks and first introns only: "very low", with 3′ flanks significantly negative. No genome-wide noncoding α was found. **About 98% of human–chimp differences are noncoding** (coding sequence is ≈ 1–1.5% of the genome), so the noncoding term dominates any genome-wide adaptive count.
- Murphy et al. 2023 (title: "Broad-scale variation in human genetic diversity levels is predicted by purifying selection on coding and non-coding elements"): background selection alone explains ~60% of megabase-scale diversity variance, and adding sweeps did not improve the fit (abstract). The appendix states that the fitted "fraction of beneficial substitutions, α, is essentially 0 (< 10⁻⁹)" (lead agent, Europe PMC full text, PMC10299832). That is a model fit of strongly beneficial sweeps to diversity data, not an MK estimate of α.

*Results (`derived:`):*
- **Coding part:** K_a,coding ≈ 0 to ~1.2×10⁴ per lineage (α 0–0.4 × 1.3–3×10⁴). With α = 0.1–0.2 it is ≈ 1.3–6×10³.
- **Noncoding part (the dominant uncertainty):** the noncoding adaptive share a_nc times ≈ 1.7×10⁷ noncoding differences per lineage (≈ 98% of Day's 17.5M per-lineage basis).

  | a_nc | K_a,noncoding | Total K_a (with coding ≈ 3×10³) | ÷ Day's 17.5M | ÷ Haldane 840 | ÷ fertility-excess cap ≈ 2,600 | Rate per generation |
  |---|---|---|---|---|---|---|
  | 0 (Keightley 2005 flanks/introns) | 0 | ≈ 3×10³ | 1/6,000 | ≈ 3.6× | ≈ 1.2× | 0.012 |
  | 0.1% | ≈ 1.7×10⁴ | ≈ 2×10⁴ | 1/875 | ≈ 24× | ≈ 8× | 0.08 |
  | 1% | ≈ 1.7×10⁵ | ≈ 1.7×10⁵ | 1/100 | ≈ 210× | ≈ 67× | 0.7 |
  | 5% | ≈ 8.6×10⁵ | ≈ 9×10⁵ | 1/20 | ≈ 1,000× | ≈ 330× | 3.4 |

  `derived:` 252,000 generations per lineage; the coding column uses 3×10³ throughout. The 5% row lands near keruru's unsourced 700,000. Neither keruru's figure nor any row in this table is a sourced noncoding estimate.
- **Day's required count vs K_a:** 17.5–20M exceeds total K_a by 20× (a_nc = 5%) to ~6,000× (a_nc = 0). The first pass wrote "three to four orders of magnitude", which holds only if a_nc ≲ 0.1%.
- **Haldane 1/300 per lineage:** 252,000/300 = 840 (Day's d-adjusted figure: 487). Coding-only K_a is ~1.5–7× above it (14× at the α = 0.4, 3×10⁴ extreme). With any noncoding adaptive share above ~0.1% the excess is 25–1,000×.

- **Rate needed:** coding-only K_a/T ≈ 0.005–0.04 per generation; with a_nc = 1–5%, ≈ 0.7–3.4 per generation.
- **Concurrent sweeps** (latency ≈ (2/s)(ln 4Nₑs + γ), Nₑ = 10⁴):
  - coding-only: ≈ 7–52 at s = 0.01, ≈ 44–340 at s = 0.001, inside or near the F2-tested range (≤ 272 active loci);
  - a_nc = 1–5%: ≈ 900–4,500 at s = 0.01, beyond the tested range. So the F2 "human-scale untested" caveat returns if the noncoding share is non-trivial.
- **H2-hard cap, ln R / D, with diploid D ≈ 20** (audit H):

  | R | Cap (per generation) | Per lineage |
  |---|---|---|
  | 1.1 | 0.0048 | ≈ 1,200 |
  | 1.3 | 0.013 | ≈ 3,300 |
  | 2 | 0.035 | ≈ 8,700 |

  So at α-scale K_a, the verdict sits exactly in the regime H2-hard did not test: Haldane's own R ≈ 1.1, D ≈ 20–30.
- **The prior literature already has this cap (PA-07, PA-10, PA-36).**
  - Nei 1971 and Felsenstein 1971 give a minimum spacing n = −ln p₀ / ln k between sweeps. With Haldane's own k = 1.1 and p₀ = 10⁻⁴, n ≈ 97 generations, i.e. ≈ 2,600 sequential substitutions in 252,000 generations. That is the same order as central K_a.
  - Haldane's own 300 assumed that ~10% of deaths are selective (I = 0.1, Haldane 1957 p.521). Matheson, Exposito-Alonso & Masel 2025 measure 8.5–95% selective deaths in *Arabidopsis*. The authors caution that this is one annual plant grown in experimental common gardens, a dataset not representative of natural conditions, and they give no human estimate.
  - Nunney 2003 simulated K = 500 and K = 5,000 (Table 1, R = 10). At K = 5,000 and u = 5×10⁻⁶ (M = 2Ku = 0.05) the cost is ≈ 430 generations fixed plus ≈ 70 per locus, about 500 for one locus. K = 10,000 was not simulated. Interpolating at the same u (M = 0.1) gives ≈ 150 + 44 per locus ≈ 190, below Haldane's 300. Whether Nunney's result cuts for or against a Haldane-like limit in humans therefore depends on the human beneficial supply M = 2Ku, which neither Nunney nor anyone in the corpus has measured.
  - None of these is cited by any party (S29, S30).

**Likely beneficiary: both, on different nodes**
The beneficiary shifts with the unmeasured noncoding share a_nc:
- **Critics, across the whole range.**
  - Day's 17.5–20M requirement for *selected* substitutions is overstated by 20× (a_nc = 5%) to ~6,000× (a_nc = 0).
  - Day's §6.4 claim that no clock-free neutral-fraction estimate exists is contradicted for coding sequence.
  - If a_nc ≲ 0.1%, the F2 "human-scale untested" caveat largely disappears.
- **Day, increasingly as a_nc rises.**
  - Even coding-only α gives K_a at or above Haldane's 1/300 (≈1.5–7×). At a_nc ≥ 1%, K_a exceeds Haldane by ~200–1,000× and the fertility-excess cap by ~70–330×.
  - So Haldane's dilemma, which is what H actually asserts after H1, is *not* dissolved by "most are neutral". It moves to two empirical inputs nobody has: the genome-wide noncoding α, and whether the cost is real at R ≈ 1.1–2 (H2, Nunney, soft selection).
  - The low-α estimates are the ones Messer & Petrov say are biased downward.
  - The α ≈ 0 estimates help Day's sweep-rarity argument (GAP-02), although they lower K_a.
- **Note.** Day himself concedes the qualitative point: neutral fixations "are the great majority" and adaptive fixations "comparatively rare" (blog 2026-05-07). What nobody supplies is the number.

**Literature (access):**
- CSAC 2005 (full text, in corpus)
- Boyko 2008 (full)
- Eyre-Walker & Keightley 2009 (full, partial)
- Uricchio 2019 (abstract)
- Enard 2016 (full)
- Keightley 2005 (full)
- Fay 2001 (abstract)
- Zhang & Li 2005 (abstract)
- Rands 2014 (abstract)
- Messer & Petrov 2013 (abstract; MK underestimates α when slightly deleterious variants are present)

See PA-19.

**Proposed check (cheapest correct)**
1. *R4 arithmetic.* Add a K_a row to `parameters.yaml`: coding α ∈ {0, 0.135, 0.2, 0.4} × sourced amino-acid differences, plus a noncoding term with a_nc ∈ {0, 0.1%, 1%, 5%}, labelled unsourced. Recompute Day's H/H8 shortfalls and Haldane's ratio for each row. Search for a genome-wide noncoding α (e.g. DFE-alpha style methods on conserved noncoding elements) before R5.
2. *R4 simulation.* Run H2-hard at λ = K_a/T ∈ {0.005, 0.015, 0.04} with diploid D ≈ 20 and R ∈ {1.1, 1.3, 2}. This is the "Haldane's own regime" cell, flagged untested.
3. *Fidelity.* Add a CSAC 2005 Table 3 row to the fidelity ledger as evidence against Z19984826 §6.4.

**R4 check (R4 2026-10-09)** (`research/checks/results/R4-H3-human.md`; `h3_human_scale.py` pre-registered at 0061b28, fix pass e48a5af; review #7). Proposed check 2 is done at human scale, with conditions: hard adaptive treadmill selection, soft deleterious load, D ≈ 2 ln 2N, long-run φ over 252,000 generations at s = 0.01.
- **Coding-only K_a** (≈ 1.3×10³–1.2×10⁴) is payable at R ≈ 1.2–3.
- **a_nc ≈ 0.1%** (≈ 2×10⁴) needs R ≈ 3 (D = 10) to ≈ 9 (D = 20).
- **a_nc ≥ 1%** is unpayable at any R in the anchor range (≤ 3–4) for D ≥ 5.
- **The flip** sits at a_nc ≈ 0.01–0.6%, below the resolution of any α estimate here (coding α CI −0.30 to 0.24; no genome-wide noncoding α). So the gap's decisive input remains **undetermined**. Each side's favourable reading needs an unsourced a_nc.
- **Not modelled:** soft selection on the adaptive loci, absolute-fitness gain, truncation/synergistic epistasis. All of these would lower the cost.
- **Low mutation supply (M ≤ 0.03) and a hard load** would raise it.
- **Beneficiary unchanged** (two-sided).
- **Check 1** (parameters.yaml K_a row) and **check 3** (fidelity row) are still open.

### GAP-04: A published finite-map limit on adaptive substitution applies at human scale and is cited by no one
**Nodes:** F2, F, A2e, A, ROOT. F2's open caveat is "human-scale active loci untested".

**What is missing.** The audit's F2 tests ≤ 272 active loci with maps of 0.1 M, 1.5 M or free recombination. Day argues linkage limits throughput (Hill–Robertson in Z18165980 and Z18452504; μ/r "channel capacity" in Z18637297). The critics assert recombination removes the limit. No party cites Weissman & Barton 2012 (S14). That paper derives Λ/R ≈ (Λ₀/R)/(1 + 2Λ₀/R), "implying that interference prevents the rate of adaptive substitution from exceeding one per centimorgan per 200 generations" (abstract). The ceiling is Λ_max ≈ R/2 per generation (haploid model).

**Size (`derived:`)**
- *Map length.* R ≈ 35–38 M sex-averaged, **including X**. Sources: Kong et al. 2002 (*Nat Genet* 31:241, doi:10.1038/ng917; Table 1 total 3,615 cM). The paper is cookie-walled; the table was read via a reproduction on a University of Manitoba course page. Matise et al. 2007 (*Genome Res* 17:1783, doi:10.1101/gr.7156307; Rutgers map v.2, 3,790 cM Kosambi) was read via the review's citation only. Primary tables not read directly.
- *Ceiling.* The W&B cap is the large-Λ₀ asymptote of an approximate result (the paper's Author Summary says interference prevents rates "from greatly exceeding" one per cM per 200 generations). It is not a theorem. Λ_max ≈ R/2 ≈ 17.5–19 adaptive substitutions per generation, ≈ 4.4–4.8M per lineage over 252,000 generations.
- *Requirement under each reading.*

  | Reading | Rate needed | Λ/R | Result |
  |---|---|---|---|
  | All 17.5–20M treated as adaptive | ≈ 70–80 per generation (≈ 54–62 at Day's 325,000 generations) | ≈ 2 | exceeds the ceiling by ≈ 4× (≈ 3× at 325,000 generations) |
  | Coding-only K_a (GAP-01) | 0.005–0.04 per generation | ≈ 10⁻⁴–10⁻³ | far below the interference threshold; interference negligible |
  | K_a with a_nc = 1–5% (GAP-01) | ≈ 0.7–3.4 per generation | ≈ 0.02–0.1 | below the ceiling; interference reduces the rate by ≈ 4–16% at R = 35 M (`derived:` at fixed supply, 1 − 1/(1 + 2Λ₀/R) with Λ₀ equal to the rate; (R4 2026-10-08) the label '2Λ/R' gives 4–19%, which is the extra supply needed to *realise* the rate; both definitions are stated in R4-GAPS-04-07-02 §1.5) |

- *Rough consistency with F2.* At F2's own parameters (2N·U_b = 32, s = 0.01; Λ₀ = 2N·U_b·u(s) with u(s) ≈ 2s, so Λ₀ ≈ 0.63), the formula predicts R_int ≈ 0.54 at 1.5 M (F2: 0.572) and ≈ 0.07 at 0.1 M (F2: 0.204). It agrees at the longer map and is off by about 3× at the very short one.

**Likely beneficiary: depends on the reading**
- **Day, on the all-fixations reading.** That reading is live for node A, because MITTENS rate-limits all fixations by the LTEE G_f. It is not live for H/H1, where Term 3 was retracted to adaptive substitutions only. On A, a mainstream peer-reviewed bound gives a finite cap below the full requirement (≈ 4×). That partly vindicates Day's "linkage limits parallelism" in form, but the A-reading treats neutral substitutions as sweeps, which W&B do not.
- **Critics, on any α-based reading.** Interference is negligible at coding-only rates and modest (≈ 4–16%) even at a_nc = 5%. This conclusion inherits GAP-01's noncoding uncertainty.
- It also bounds Day's channel-capacity argument (Z18637297). The binding quantity is map length in Morgans, not μ/r per site.

**Literature:**
- Weissman & Barton 2012, PLoS Genet 8:e1002740, doi:10.1371/journal.pgen.1002740 (full text read by agent; (R4 2026-10-08) PDF read by the R4 check and locators verified by its reviewer: Eq. (1) p.3; Eq. (6)–(7) p.7; Fig. 4 caption p.7 (simulated Λ/R "remaining <3 even for Λ₀/R = 10³"); asymptote and validity "N > 10³ up to Λ₀/R ~ 1" p.8; Fig. 5 caption p.9; Eq. (13) p.12 (exponential DFE, asymptote R/4))
- Neher, Shraiman & Fisher 2010 (abstract)

See PA-21.

**Proposed check**
1. Fit the W&B formula to the existing F2 grid (no new simulation). Report where it fails (short maps, small N).
2. Evaluate the formula at R = 35–38 M with Λ₀ = 2N·U_b·u(s) over the K_a range of GAP-01, including the noncoding rows.
3. One fwdpy11 run with a 35 M map and the largest feasible Λ₀, to anchor the human-scale extrapolation.

**R4 check (R4 2026-10-08)** (`research/checks/results/R4-GAPS-04-07-02.md` §1; scripts `gap04_weissman_barton.py`, pre-registered at b812741; post hoc `gap04_posthoc_concurrency.py`, `gap0x_posthoc_review.py`). Proposed checks 1 and 2 are done; check 3 (fwdpy11 at 35 M) is still open.
- *The cap is a bracket, not one number.* W&B give the additive-approximation asymptote R/2 (fixed s, Eq. 7) and R/4 (exponential DFE, Eq. 13); their simulations exceed both, up to ~3R at Λ₀/R = 10³. The brief's "R × a log factor" is not the paper's cap: the log appears only in a heuristic lower bound on growth above R/2.
- *F2 fit.* Eq. 7 agrees with F2 at 1.5 M within ~6–10% (c = 1.79 ± 0.03 vs 2; c = 2 formally excluded at n = 4 replicates); Eq. 1 matches free recombination within 1.4 SE; the form fails at 0.1 M (R/s = 10; observed rate 2.6 × R/2); clonal runs are outside the domain. All 20 F2 cells were known before registration, so these are formula tests on known data.
- *Day's stated model* (MITTENS 3.0 §4.3/§8.2: every fixation sweep-carried, "The remainder are hitchhikers"): 17.5–20M per lineage needs 61.5–79 per generation, 3.3–4.5× over R/2 and 6.5–9.1× over R/4 (R = 35–38 M), 0.54–0.76 of the simulated maximum. Exceeding R/2 needs Λ₀/R ≈ 30–300 (Fig. 4 read at s = 0.05, ±2×; s-dependence untested), i.e. a beneficial supply of order 1% to several hundred % of all new mutations depending on N_e (10⁴–2×10⁵) and s, and on an extrapolated e^{4Λs} factor. "Implausible in most cells", not "infeasible".
- *Critics' model.* The asymptotes are crossed only if more than 13–14% (R/4) or 25–27% (R/2) of the 17.5M differences are adaptive (16–18% / 33–35% at 325,000 generations). Day's own "Even if 99% of divergence is neutral, 200,000 fixations remain required" (Z18165980 l.66) is 22–31× below R/2. Interference costs ≤ 4.3% for K_a ≤ 10⁵ and 17–31% at 10⁶ (fixed supply; Eq. 7–13).
- *Separate constraint.* This is the interference leg only. The audit's hard-selection cap (H2-hard, 1,200–8,700 per lineage) is exceeded by K_a ≥ 10⁴.
- *POST HOC, concurrency.* At R/2 the soft-selection ceiling is 7.7–8.3×10³ concurrent active-zone sweeps at s = 0.01 (×10 at s = 0.001), reached only at very large supply; at GAP-01 rates it is 1.7–1,744 (s = 0.01); Day's 200,000 gives 349. So 230 (Gc) has no support as a cap but matches the concurrency implied by K_a ≈ 10⁵. Day's §6.1 Σs ≤ 1–2 ceiling, untested, would bind near K_a ≈ 6×10⁴–1.2×10⁵.
- *Magnitude.* W&B's R/2 per lineage (4.4–4.8M) is 1,800–25,000× MITTENS' achievable count: "linkage limits parallelism" holds in form, not in magnitude.
- *Beneficiary (weighted).* Day's leg is conditional on his all-fixations model, which branch B decides; the critics' leg is interference-only and holds below the crossing share.

### GAP-02: Day's "sweep signatures absent" argument: an unanswered empirical point with an unexamined detection window
**Nodes:** ROOT, ROOT-M (row 6, hitchhiking), F2, H.

**What is missing.** Z18452504 §4.3(4) (lines ~325–331 of the extracted text): "If 3,200+ sweeps occurred in the human lineage over 325,000 generations, approximately one sweep completes every 100 generations … Scans for positive selection in humans … identify dozens to hundreds of candidate sweep regions—not thousands. If 3,200+ sweeps had occurred, selection scans would be saturated with signals." No critic or audit file replies (S17). Nobody applies a detection window to the argument (S18). The nearest is keruru's remark about one fusion locus, "A sweep that old would have faded" ("Forty-Seven"), which is not addressed to Z18452504.

**Size (`derived:`)**
- Hernandez et al. 2011 frame their test over "the past ~250,000 years". That is ≈ 8,600–10,000 generations at 25–29 years, about 3–4% of the 6.3 My lineage.
- At Day's own rate (1 per 100 generations), the expected number of sweeps inside that window is ≈ 86–100. Day's "dozens to hundreds" observed is of the same order.
- So, *as stated*, the argument's own numbers do not imply saturation.

**But the literature also supports Day's premise.**
- Hernandez et al. 2011: the diversity trough around human-specific amino-acid substitutions "is no more pronounced than around synonymous substitutions"; "classic sweeps were not a dominant mode of adaptation".
- Murphy et al. 2023: a background-selection-only model explains ~60% of megabase-scale diversity variance, and "adding sweeps did not improve the fit" (abstract). The appendix's fitted sweep α is "essentially 0 (< 10⁻⁹)" (lead agent, Europe PMC full text). This constrains the combined rate × strength of strong sweeps, not the MK α.
- The reviewer reports that the Hernandez 2011 main text bounds the share of human-specific substitutions that left a detectable classic sweep at about 5% ("far below 10%"). This was not read here (the full text did not load) and is marked unverified. If confirmed, it is the most direct number for the Day-favouring leg. **(R4 2026-10-08) Corrected after reading the main text (PMC3669691):** three numbers were conflated. "approximately 5% of human-specific substitutions could have left a detectable sweep" is the *window share* (250,000 years of ~5 My); "a rate of classic sweeps far below 10%" is the YRI–CEU local-adaptation rate since the population split; the trough test excludes "even if only 10% of human-specific amino acid substitutions were strongly favored or if 25% ... with weak effects".
- These are evidence that hard sweeps of new mutations are rare. That bears on whatever K_a (GAP-01) is claimed to have fixed by classic sweeps.

**Likely beneficiary: both**
- **Critics.** The saturation inference ignores the detection window.
- **Day.** Peer-reviewed analyses do find classic sweeps rare, which constrains the hard-sweep share of adaptive substitution. The critics have not engaged this. It sits uneasily with the α ≈ 0.1–0.2 estimates unless most adaptation is weak or soft (Uricchio: 72% weakly adaptive).

**Literature:**
- Hernandez et al. 2011, Science 331:920 (abstract and summaries; full text not read; (R4 2026-10-08) main text read, PMC3669691 author manuscript: "In humans, the effects of sweeps are expected to persist for approximately 10,000 generations or about 250,000 years (4)", ref. 4 = Przeworski 2002, whose full text is behind a bot check and was not read)
- Sabeti et al. 2006, Science 312:1614. The phrase "several hundred thousand years" came via a secondary source (bionumbers) and the reviewer could not find it: **unverified**. The ~250,000-year window above rests on Hernandez 2011's abstract instead.
- Murphy et al. 2023, eLife 12:e76065 (abstract; appendix α sentence read in Europe PMC full text)

See PA-22.

**Proposed check (R4 arithmetic)**
1. Expected detectable sweeps = (sweeps per generation) × (detection window in generations) × (power), under each side's K and s. Windows come from Hernandez 2011 (and Przeworski 2002/2003, to be retrieved).
2. Compare with the Hernandez estimate of the classic-sweep fraction.
3. Extract Z18452504 §4.3(4) as a claim (none exists). (R4 2026-10-08) Done: claims A6 (Z18452504 §4.3(4)) and A6a (Z18441321 §3.1, bonobos).

**R4 check (R4 2026-10-08)** (`research/checks/results/R4-GAPS-04-07-02.md` §3; `gap02_sweep_window.py`, pre-registered at b812741; post hoc `gap0x_posthoc_review.py`).
- *Upper bound.* Expected detectable completed sweeps E = K × W/T are computed at detection power 1, so all figures are upper bounds. Day's stated 3,200 over 325,000 generations gives ≈ 98 at the sourced window (W ≈ 10,000; 39 at an unsourced 4,000): "dozens to hundreds". The top of his own block range (32,000) gives 985, and his upper N_e (33,000, W ≈ 33,000) up to 3,250, so the inference is range-dependent; the claim's internal verdict is pending.
- *Comparators.* The cited scans (Voight 2006 "~250 signals ... in each population", abstract; Sabeti 2007 "more than 300"; Pickrell 2009 1% tail) target incomplete or population-specific sweeps through top-1% lists, and Akey 2009's union of nine scans (5,110 regions, 722 replicated, "poor concordance") is threshold-limited too; these comparisons are illustrative only. The SFS-type comparator is Yoo 2025's SweepFinder2 (11–62 candidates per ape taxon; power-limited). K_a = 10³ matches it; 10⁴ is 5–18× above the ape median at power 1.
- *Power needed for "tension".* For K_a = 10⁵ to conflict with 722 regions needs power ≥ 0.65–0.84 (f_strong 0.28, W = 10,000; > 1 at W = 4,000). The real constraint on large strong-sweep counts is Hernandez's trough test (and Murphy 2023), not scan counts.
- *Hernandez bound.* Strongly favoured classic sweeps < 10% of human-specific amino-acid substitutions, i.e. < 1.3–3×10³ per lineage (constant-rate extrapolation), while Hernandez states 10–15% (possibly 40%) of amino-acid differences were adaptive: most adaptation weak or soft.
- *Bonobos (A6a).* The window covers 43–50% of the split; 326,000 selective sweeps would leave ~1.4–1.6×10⁵ detectable against Yoo's 30. Supported as against *selective* fixations, which no critic asserts.
- *Day's strongest variant.* If sweeps carry most fixations (Day's §8.2 hitchhikers; DarwinZDF42, Reddit 1wv4zeg and 1wss2wj: "selective sweeps cause many fixations, mostly for neutral variation"), the diversity data are a real constraint on that account, whoever holds it.
- *Lead for GAP-01.* Hernandez cites "5% of substitutions in conserved non-coding regions" and "~20% in UTRs" as adaptive (Torgerson 2009; Eyre-Walker & Keightley 2009), read second-hand: a partial, sourced noncoding α (CNCs and UTRs only).
- *Caveats.* Demographic confounding, background selection (mimic and power loss), polygenic adaptation, power only at 4N_e·s ≳ 400; Day's bullet (6) (clustering of fixed differences) untested.

### GAP-03: Neutral substitution rate under complete linkage (Birky & Walsh 1988) vs Day's "channel capacity" paper
**Nodes:** B, B1, B3, B5, H8, ROOT, ROOT-M (row 11).

**What is missing.**
- Day's Z18637297 (2026-02-13) argues that because μ/r ≈ 1.0–1.5 in mammals, "the independent-site assumption underlying neutral theory … systematically fails". That would undercut k = μ when summed over the genome. The paper uses ~96 new mutations per diploid genome per generation against ~33 crossovers.
- No critic engages the paper (S16: C = 0), and the audit lists it as "not extracted yet" (ROOT-M row 11).
- No party cites Birky & Walsh 1988 (S15). Its only corpus hit is as reference 44 in CSAC 2005's reference list. Its abstract states that complete linkage to advantageous or deleterious mutations "does not affect the substitution of selectively neutral mutations" (PNAS 85:6414; abstract read on PMC). The same paper finds that linkage *slows* the fixation of advantageous mutations (Hill–Robertson). The authors also warn that linkage can confound comparisons of substitution rates across genomic regions.

**Size.**
- For the neutral count (B5), the predicted effect of linkage on the expected neutral substitution rate is zero. That is the same martingale argument as B3. Day's μ/r ratio would then not bear on k = μ.
- For selected sites, the reduction is real but is bounded by GAP-04's map-length formula, not by μ/r per site.
- **Limit.** Birky & Walsh speak to the *expected* neutral rate. They do not by themselves answer a claim about variance or about the independence of sites, which is the form of Day's argument. The proposed check should therefore also report the variance of k across replicates.

**Likely beneficiary: both**
- **Critics.** It restores k = μ under linkage.
- **Day.** It confirms that linkage reduces the efficacy of beneficial substitution, which is his H-R point.

**Literature:** Birky & Walsh 1988, doi:10.1073/pnas.85.17.6414 (abstract, PMC281982). See PA-20.

**Proposed check (cheap).** Use the B0.5 equilibrium k test with r = 0 (one non-recombining block), U ≫ crossover count and a linked selected class (BGS, or recurrent sweeps). Measure neutral k/U. Prediction under Birky–Walsh: 1.00 within SE. Also extract Z18637297 into a claim file.

### GAP-05: Slightly deleterious fixations in hominids: evidence and long-term fitness consequence, with no numbers from any party
**Nodes:** ROOT-M (row 4, "Drift Deathmarch"), B, B5, H5 (Hössjer HO-11), ROOT.

**What is missing.**
- Day: "Since 75% of all mutations are harmful … collapse occurs in 9 generations" (blog 2026-01-11 "The Drift Deathmarch", ¶15–16). This assumes selection is switched off for all mutations.
- Ally Hössjer: the nearly neutral theory implies slightly deleterious fixations "accumulate" (HO-11; review p.~6), with no calculation.
- Critics: no response with numbers (S21).
- Audit: tested U = 2.2 hard/soft/synergistic load (H7), not the fixation of slightly deleterious mutations.
- Nobody cites:
  - Kondrashov 1995 (the "dangerous range" 1/G < s < 1/4Nₑ; read by the lead agent in the Europe PMC abstract, although the reviewer could not see it in their copy);
  - Charlesworth 2013 "Why we are not dead one hundred times over";
  - CSAC 2005's finding that a ~35% excess of hominid amino-acid changes over murids is mainly *relaxed constraint*;
  - Keightley et al. 2005 ("degradation of gene control regions").

**Size (`derived:`, rough).**
- About 8% of the genome is constrained (Rands 2014). That is ≈ 3 constrained-site mutations per haploid genome per generation.
- If ~25–30% of those are nearly neutral (Boyko 2008: 27–29% of nonsynonymous mutations nearly neutral), then ~10⁵ slightly deleterious substitutions could accumulate per lineage in 252,000 generations, each with s on the order of 1/(2Nₑ).
- Under multiplicative fitness, with no back or compensatory mutation, that is a cumulative log-fitness decline of order 1–10. **This is an upper-end scenario, not an estimate.** It applies Boyko's nonsynonymous nearly-neutral share to all constrained sites (an extrapolation) and ignores the equilibria that Kondrashov 1995 and Charlesworth 2013 discuss. It illustrates Kondrashov's paradox at hominid scale.

**Likely beneficiary: mixed, Day-leaning on the premise**
- **Day.** The premise (hominids fixed many slightly deleterious variants) is supported by mainstream data that no critic has acknowledged.
- **Critics.** The published resolutions (Charlesworth 2013: weak stabilizing selection, or soft selection; back and compensatory mutation equilibria) remove the "collapse". Day's 9-generation collapse also rests on switching purifying selection off for strongly deleterious mutations. That is not what neutral theory assumes, and no critic has said so with numbers.
- **Counts.** The effect on the *neutral count* (B5) is small. Constrained sites are ≤ 8–11% of the genome, so they can lower the 2μT expectation by at most a few percent.

**Literature (all abstracts via Europe PMC unless noted):**
- Kondrashov 1995, J Theor Biol 175:583, doi:10.1006/jtbi.1995.0167
- Charlesworth 2013, Evolution 67:3354, doi:10.1111/evo.12195
- CSAC 2005 (full)
- Keightley 2005 (full)
- Lynch 2010 (see PA-17; its per-generation 1–5% figure is from a sub-agent read and is unverified here)

**Proposed check (R4).**
1. Extract the Drift Deathmarch (blog 2026-01-11) and HO-11 as claims.
2. Arithmetic: the expected number of slightly deleterious substitutions from a sourced DFE (Boyko 2008 gamma; Eyre-Walker & Keightley 2007).
3. A forward simulation with a DFE plus back mutation at Nₑ = 10⁴: does mean fitness plateau (equilibrium) or decline without bound over 10⁵ generations?

### GAP-06: Mutation-rate × generation-time consistency, and linked selection, in the divergence fit
**Nodes:** B4a, B1c, B6, A (A1 generations), ROOT.

**What is missing.**
- B4a uses μ = 1.2×10⁻⁸ per generation together with g = 25 years (T = 252,000). Kong 2012's 1.2×10⁻⁸ is "with an average father's age of 29.7".
- `parameters.yaml` itself flags that Yoo's μ and generation time are unrecorded, so the Nₑ,anc rescaling is "OPEN".
- No party uses the per-year literature to tie μ and g together:
  - Amster & Sella 2016: changing mean generation time from 19 to 30.4 years changes the yearly rate by "less than 2%".
  - Jónsson 2017: +1.51 mutations per year of paternal age, +0.37 maternal.
  - Amster & Sella 2016 also give a human–chimp split that "may have occurred as recently as 6.6 Mya" (abstract).
  - Besenbacher 2019: human trio rate ≈ 0.43×10⁻⁹/yr; apes ~1.48× higher (abstract). The first pass attributed the 6.6 Mya figure to Besenbacher; it is in Amster & Sella's abstract, and Besenbacher's own figure was seen only in the authors' blog.
- No party uses linkage-aware ancestral Nₑ (S7, S10): McVicker et al. 2009 give ancestral human–chimp N_hc ≈ 9.9×10⁴ (7.4×10⁴–1.4×10⁵) after modelling background selection (BGS). The value is in Table 1, with T_hc fixed at 2.4×10⁵ generations (lead agent, Europe PMC full text). BGS lowers autosomal diversity by 19–26% (McVicker abstract); Murphy 2023 gives a mean reduction of ~17% (full text).
- Day addresses the hominoid slowdown only as a "calibration artifact" (S9).

**Size (`derived:`).**
- *Per-year consistency.* Using Kong's μ at a 29.7-year father with g = 29.7: 2μT = 2 × (1.2×10⁻⁸/29.7) × 6.3×10⁶ = 0.51%, against 0.605% in B4a.
  - At the HCB node, predicted d becomes ≈ 1.46% instead of 1.55% (observed 1.23%).
  - The ~25% overshoot shrinks to ~19%.
- *Linked selection.* Replacing Yoo's lifetime Nₑ,anc (1.98×10⁵) with a BGS-reduced or McVicker-type value (9.9×10⁴) moves θ_anc by ~17–50%. The two Nₑ figures were estimated under different μ and model assumptions, so this is a range, not a correction. It alone can close the overshoot.
- *MITTENS.* The effect on MITTENS's generation count is ≤ 1.3–1.6× (g 20–32.5 years). That is negligible against the claimed 10⁵–10⁶ shortfall.

**Likely beneficiary: critics (weak), on B4a/B6 only.**
- It narrows the audit's "three free parameters, no clean fit" (B4a). If the fit closes, that favours the critics' B6 decomposition. If it does not, the open fit stays open.
- It favours neither side on ROOT.

**Literature:**
- Amster & Sella 2016 (full, via summarising fetch)
- Besenbacher 2019 (abstract + authors' blog)
- Moorjani 2016 (full)
- Jónsson 2017 (abstract)
- McVicker 2009 (Table 1 and abstract, Europe PMC full text)
- Murphy 2023 (full text, Europe PMC)

See PA-34.

**Proposed check.** Re-run the B4a analytic rows with (μ, g) pairs taken from one source each: Kong (29.7 y); Besenbacher per-year × g; Amster & Sella; and Moorjani. Use a BGS-adjusted Nₑ,anc (McVicker Table 1). Report whether 1.23% is within range without free tuning.

### GAP-07: Expected indel and SV *events* from measured mutation rates (sharpening A3x)
**Nodes:** A (A3 required fixations), ROOT, ROOT-M (row 14).

**What is missing.**
- A3x counts events from CSAC's observed totals: 35M SNV, 5M indel, 1,140 inversions.
- It notes the critics give no independent event count.
- No party derives the expected event count from germline rates (S5, S6 = 0 hits).
- That derivation is the clock-independent way to ask whether Yoo's 5–15× "gap divergence" megabases (Day's "375 million additional base pairs", blog 2026-04-28) correspond to many events or to few large ones.

**Size (`derived:`).**
- *Germline rates:*

  | Class | Rate | Source |
  |---|---|---|
  | Indels | ≈ 1.5×10⁻⁹ per nt per generation (Besenbacher 2015), ≈ 4.65 per haploid genome at 3.1 Gb; or 2.94 per generation for 1–20 bp | Kloosterman 2015 |
  | SVs (> 20 bp) | ≈ 0.16 per generation | Kloosterman 2015; Belyeu 2021 |
  | SVs (Watterson-based projection, short-read-accessible regions) | 0.29 (0.13–0.44) | Collins 2020 (main text, Europe PMC full text PMC7334194) |

- *Expected post-split events per lineage over 252,000 generations (before adding ancestral polymorphism):*
  - indels ≈ 0.4–1.1 × 10⁶;
  - SVs ≈ 2–7 × 10⁴. The low end halves the per-offspring de novo counts to give a single-lineage rate; the high end uses them as given.
- *Against SNVs.* SNVs over the same span number ≈ 9.4M (μ·L·T per lineage, μ = 1.2×10⁻⁸, L = 3.1×10⁹). Events of all kinds are therefore ≈ 1.04–1.13× the SNV count, while the bp affected by SVs are 5–15× larger.
- *Consistency.* The observed CSAC indel/SNV event ratio (≈ 5/35 = 0.14) is close to Besenbacher's rate ratio (4.65/37 ≈ 0.125) and to Nachman & Crowell 2000 (SNVs "10 times more frequent than length mutations"; a divergence-based figure). It is ~3× above the Kloosterman-based ratio (≈ 0.04 after halving), so the indel rate itself is uncertain by ~3×.

**Likely beneficiary: critics (modest).**
- It gives an independent, rate-based event count of ≈ 1.04–1.13 × the SNV count, about 9.9–10.6M per lineage post-split, confirming A3x's unit argument.
- Day's 205M (bp) would exceed the rate-based event count by ≈ 20×, or ≈ 10× the observed ≈ 20M events per lineage in A3x.
- **Caveat that could cut the other way:** the rate-based SV count has a 3× spread across sources and excludes large segmental duplications. It cannot rule out that a minority of Yoo's gap megabases came from many mid-size events.

**Literature:**
- Besenbacher 2015 (full)
- Kloosterman 2015 (abstract; (R4 2026-10-08) full text, PMC4448676)
- Belyeu 2021 (abstract; (R4 2026-10-08) full text, PMC8059337)
- Collins 2020 (main text, Europe PMC; Results, paragraph before Fig. 3; "certainly underestimates")
- Nachman & Crowell 2000 (abstract)
- CSAC 2005 (full)

**Proposed check (R4 arithmetic).** Expected events per lineage = (rate per class) × T + ancestral share. Compare with CSAC event counts and Yoo's SV and inversion counts per lineage. Record in A3x.

**R4 check (R4 2026-10-08)** (`research/checks/results/R4-GAPS-04-07-02.md` §2; `gap07_event_counts.py`, pre-registered at b812741; post hoc `gap0x_posthoc_review.py`).
- *Event counts per lineage, three routes (two share the CSAC 17.5M SNV anchor):* rate × time with k = μ 9.6–10.4M (first argued by justatest90 and Wrevellyn, Reddit 1wv4zeg: "about 9.7 million"); clock-free calibrated 18.2–19.7M; CSAC-observed basis 20.0M (22.5M upper bound). Day's 205M is ≈ 9–11× these; ≥ 8.0× over observation-consistent grid points (μ CIs × T 169,231–450,000 × N_anc 0–1.98×10⁵); 5.3× at the extreme corner, which predicts ~2× the observed SNV divergence.
- *CSAC 5M is a two-lineage total.* Abstract ("five million insertion/deletion events") and p.73 ("~5 million compared with ~35 million"); the p.73 "in each species" sentence describes insertions of 1 bp–15 kb relative to the other genome; indel:SNV 0.14 (total) vs 0.29 (per species) against germline 0.04–0.12. CSAC's alignment-gap counts are an upper bound on events.
- *Indels, like for like.* Clock-free M3 vs observed: 1.16× (Besenbacher) to 3.55× (Kloosterman).
- *SV base pairs.* Under k = μ, de novo SVs give 0.35–0.92 Gb per lineage (517 Mb at 252,000; 357 Mb without Kloosterman's single 327 kbp event, 31% of its SV base pairs). That is the same order as SDR base pairs (Yoo human-lineage 148–184 Mb; Day's 187 Mb; cross-ape 327 Mb), but SDRs are mostly centromeres, acrocentric arms and heterochromatic caps, so the agreement does not show that SDR megabases come from 10⁴–10⁵ ordinary SV events.
- *Base-pair reading.* Counting SDR base pairs as repeat-unit events gives 21–30M per lineage at Yoo's 171 bp and 32 bp satellite units (45–184M only at assumed 2–6 bp units). G_f counts events, so a base-pair numerator is a unit mismatch inside Day's method; that, not the §7.3 wording, is the decisive point.
- *Credits (verified):* McCarthy (one event, many base pairs); Fun-Friendship4898 (Reddit 1wv4zeg: the 35M + 2 × 187 Mb construction; SDR composition); Nesslig20 relaying Neukamm (Peaceful Science 18094: indel spans); Mansfield's uncited ~25M.
- *Beneficiary.* Critics on the unit argument; Day credited for corroboration of the 17.5M/20M magnitudes, whose shortfall is untouched.

**R4 direct count (R4 2026-10-09)** (`research/checks/results/R4-GAP07b-alignment.md`; `gap07b_alignment_count.py`, pre-registered at 3c847b8; post hoc 3798b92, fbbc580; review #8).
- *Measured, UCSC hg38 vs panTro6 (non-T2T; both lineages plus polymorphism):* 37.77M SNVs, 4.30M indel events, 42.10M events, 21.05M per lineage. Day's 205M is 9.7× raw; bracket about 7–14× (Day-favourable repeat-unit and slippage readings 7.2–9.5; critic-favourable lineage, fill, divergence and polymorphism corrections 10.1–13.4; all post hoc).
- *Replaces the "~20× rate-based / ~10× observed" line above.* The direct count agrees with the calibrated and CSAC-observed routes (18–22M per lineage). The k = μ rate route (9.6–10.4M) is about 2× below it; that tension is the clock question (B4a / GAP-06), on which it favours Day; this check does not resolve it.
- *CSAC's 5M* resolves as a two-lineage total (4.30M measured); the 22.5M per-lineage upper bound above is retired.
- *Day's stated position* (Q99, Q101–Q103) is a weighting claim with a range (SNV-only lower bracket, bp upper bracket). His SNV-only 17.5M is 83% of measured events and brackets the polymorphism-corrected fixed events (16.4–18.1M). As a weight, 205M needs ~3,250 SNV-equivalents per event above 50 bp; untested.
- *Open:* GAP-07c (polymorphic share of SNVs, indels and SVs from population frequencies) and a T2T re-run (CHM13/hs1 vs mPanTro3).

---

## Candidates rejected (considered, but already addressed or immaterial)
| Candidate | Why rejected | Locator |
|---|---|---|
| Variance / probability of the observed outcome (K1) | Immaterial to the headline numbers. Poisson SD of a 19M neutral count ≈ 4,400 (0.02%). Coalescent variance is averaged over ~3×10⁹ sites, and B4a simulates it. LTEE replicate variability is addressed. | E5/E6 (critics' −906; audit); A2d (fastest vs average; Camestros concedes average); C1 P-values (audit) |
| Gene flow after the split (K4) | Addressed in passing on both sides, and low materiality. The literature is split: Patterson 2006 and Mailund 2012 for gene flow; Innan & Watanabe 2006, Wakeley 2008, Yamamichi 2012 and McVicker 2009 for a simple split or selection. It adds a parameter to B4a but does not change any verdict direction. | Day blog 2026-01-30 (quoted AI list); keruru "Forty-Seven"; ROOT-M row 13 |
| gBGC (K6) | Immaterial to counts. The genome-wide B ≈ 0.27–0.43 (Glémin 2015), and 1–2% of the genome is under strong gBGC. That moves W↔S substitution rates by tens of percent on a minority of sites and the total by a few percent at most. Day names it without computing (ROOT-M row 8); the audit has recorded that. | ROOT-M row 8 |
| CpG hypermutability / saturation (K6) | Day addresses it as a penalty (Q&A 2026-01-19). CpG is ~¼ of substitutions (CSAC). At a 10–18× rate, per-CpG-site divergence of ~10–15% implies a multiple-hit correction of ≈ 5–8% on that quarter, i.e. ≈ 1–2% of the total. Immaterial. | Day Q&A 2026-01-19; ROOT-M row 16 |
| Population structure, overlapping generations, sweepstakes (K9) | Addressed by Day and the audit. | Day: Z18167588 (Whitlock & Barton; Maruyama), Z23188201 (Cannings); audit: C2, B3b, B2 |
| Soft sweeps / standing variation / polygenic (K10) | Addressed by Day, critics and the audit. | Z18452504 §4.3 (factor ~3); Hancock B6c; keruru LLM; audit H D-values |
| LTEE → mammal transfer (K11) | Addressed extensively. | A5, A5b, A5f, A2e; F2/A-sim |
| Epistasis / diminishing returns / adaptive walk (K8) | Addressed by Day (diminishing returns "conservative", Wiser 2013). Critics list it only. Bears on A2e only weakly: Good 2017 finds the fixation rate "declines only modestly". | Z18167588; Z23020792; Good 2017 |
| Truncation selection / Maynard Smith 1968 (K12) | Addressed in prose by Day (Z19984826 §3.3.1, "None of them raises smax above order unity") and listed by the audit's critic-steelman. It is *untested*: a check gap, already recorded in REVIEW-R4-steelman-critic item 5(ii). | Z19984826 lines ~306–312; REVIEW-R4-steelman-critic.md |
| Fertility-excess spacing (Nei 1971; Felsenstein 1971; restated by Matheson et al. 2025) (K12) | Not a gap in substance. The audit's H2-hard independently derives the same cap (ln R / D; R4-H2-hard.md), and Day's H8 reasons with a "reproductive ceiling". But the literature is uncited by all parties (S29–S30), and its key empirical input (the share of deaths that are selective) is unsourced in the corpus. This is recorded as prior art (PA-10, PA-07, PA-36) and folded into GAP-01's check. | R4-H2-hard.md; Z19984826 §3.3.1 |
| Kimura 1968 as the neutralist answer to Haldane (K12) | Addressed by Day: "Kimura developed neutral theory explicitly in response to Haldane's work" (Z18168236 §5.1). | Z18168236 §5.1 |
| Mutation-load paradox at U = 2.2 (K8) | Addressed by the audit via Keightley 2012, which itself discusses soft selection (Wallace), truncation (Crow & Kimura 1979) and synergistic epistasis. The audit tested hard, soft and synergistic.

The uncited literature agrees with the audit:
- Lesecque, Keightley & Eyre-Walker 2012 give ">16 offspring" and "at least 88%" failing under the absolute model at U ≈ 2.1, and φ ≈ 0.14–0.19 under relative fitness.
- Galeota-Sprung, Sniegowski & Ewens 2020: no mutation-free genotype "will ever exist".

The balance ledger's R4 entry lists "≈18 offspring" as a point for Day. Lesecque frames it as the absolute-model premise of a paradox that relative fitness resolves. Recorded as prior art (PA-16, PA-18), not as a gap. | h_keightley_load.py; R4-H-C2.md |
| Waiting-time literature (K13) | Addressed. Hancock 2024 treats Behe & Snoke, Lynch and Sanford 2015 with SLiM, but before MITTENS (TH-1, "downloaded, not analysed"). A critic framed MITTENS as "a different version of the waiting time problem", and Day rejected the framing (blog 2026-09-22 and 2026-10-01). Hössjer cites his 2021 model. D/G are not load-bearing.

The specific-vs-any rule (G3) is already in print. Durrett & Schmidt 2009 (*Genetics* 181:821): with k nonoverlapping possible double-mutation targets, the expected wait "is divided by k". They conclude, qualitatively and without human–chimp numbers, that double mutations "can easily have caused a large number of changes in the human genome since our divergence from chimpanzees". This is a first-occurrence waiting-time result, not a fixation-count result. No party cites it (`Durrett`: 0 in D/C/R).

The prior art does not support a waiting-time cap on *total* fixations (PA-25 to PA-30). **Audit omission:** Hössjer's prediction (review p.7, "the waiting time for several genes to change expression … far exceeds 9 million years") is not mapped to any node. | TH-1; Day blog 2026-10-01; hossjer-mittens-review p.7 |
| Conservation of information (Ewert/Dembski/Marks) (K13) | No hits in D. Dembski is an ally who gives "no calculation" (balance ledger). Not load-bearing for any of the 30 nodes. | S25 |

## Beneficiary tally (re-tallied after review)
| Gap | Likely beneficiary | Rank (verdict impact) |
|---|---|---|
| GAP-01 adaptive fraction α | **Both, depending on the unmeasured noncoding share a_nc.** Critics at every a_nc: Day's 17.5M is overstated by 20× to ~6,000×, and §6.4 is contradicted for coding sequence. Day on H/H1: K_a exceeds Haldane by 1.5–7× coding-only and by 25–1,000× once a_nc ≥ 0.1%. | 1 |
| GAP-04 finite-map limit (Weissman–Barton) | **Both.** Day on node A's all-fixations reading (≈ 4× over the cap); critics at α-scale rates (this inherits GAP-01's uncertainty). (R4 2026-10-08) Weighted: Day's leg is conditional on his stated all-fixations model (3.3–4.5× over R/2, 6.5–9.1× over R/4; branch B decides the model); the critics' leg is interference-only and holds below a 13–27% adaptive share. | 2 |
| GAP-02 sweep-signature window | **Both.** Critics on the saturation inference; Day on classic-sweep rarity (Hernandez; Murphy's model fit). (R4 2026-10-08) Weighted: the saturation inference fails at Day's stated 3,200 (≈ 98 detectable, upper bound) but is range-dependent at the top of his range; no critic made the window argument; Day's leg is against hitchhiking as the main source of fixations, whoever holds it. | 3 |
| GAP-03 neutral rate under linkage (Birky–Walsh) | **Critics** on B/B5 (expected rate only). Day on beneficial efficacy, minor. | 4 |
| GAP-05 slightly deleterious fixations | **Day-leaning** on the premise; critics on the "collapse". The size figure is an upper-end scenario. | 5 |
| GAP-06 μ×g consistency, BGS-aware Nₑ,anc | **Critics, weak** (B4a/B6 only, and only if the fit closes). Neither on ROOT. | 6 |
| GAP-07 rate-based event counts | **Critics** (modest; the indel rate is uncertain by ~3×). (R4 2026-10-08) Critics on the unit argument (205M ≈ 9–11× the event count); Day credited for corroboration of the 17.5M/20M magnitudes. (R4 2026-10-09, direct count) 9.7× raw, bracket 7–14× (hg38 vs panTro6, non-T2T); Day's SNV-only 17.5M brackets the polymorphism-corrected fixed events. | 7 |

**Counts by primary beneficiary:** two-sided 3; critic-leaning 3; Day-leaning 1; neither 0. (First pass: 3/2/1/1. GAP-06 moved from "neither" to "critics, weak" because its own text said so.)

**Counts by any credit:**

| Side | Gaps | Count |
|---|---|---|
| Day | GAP-01, 02, 03 (minor), 04, 05 | 5 |
| Critics | GAP-01, 02, 03, 04, 05, 06 (weak), 07 | 7 |

**Is the split a product of search bias?**
- The term list was fixed before hits were read. The Day-favouring candidates were all considered and sourced:
  - linkage limits;
  - load and meltdown;
  - limited beneficial supply;
  - sweep rarity;
  - the Haldane-vs-α ratio.
- The three highest-ranked gaps each contain a Day-favourable component that no critic has addressed.
- After the review, GAP-01's Day component is larger than first stated. With any noncoding adaptive share above ~0.1%, Haldane's limit is exceeded by one to three orders of magnitude.
- The critic-leaning residue (GAP-03, 06, 07) is small-effect. It arises because Day's linkage paper (Z18637297) and bp count have published, specific answers, and because GAP-06 tidies an audit fit.
- Rejections ran in both directions: variance and gBGC were rejected as immaterial whichever side they would help.
- **The reviewer found that the first pass leaned towards the critics in four places.** That pass:
  - treated a coding-only α as genome-wide (GAP-01);
  - omitted Matheson's own representativeness caveat;
  - overstated Nunney's Day-favourable range;
  - made two small search-count errors (S15 Birky 1 hit, not 0; "13 rows" for 12) that both strengthened "nobody cited" claims.

  All four are corrected above. This record is kept so readers can weigh the residual risk of lean. The lean ran in the same direction as the pass-1 lean noted in the plan (E6).

**Limits.**
- One agent ran this pass, and the literature numbers were fetched by sub-agents (access status is stated per item in `prior-art.md`). A fact-check pass (`gaps-review.md`) then checked citations and arithmetic. It could not open some full texts, and neither could this revision.
- The paywalled books (*Probability Zero*, *The Frozen Gene*) were not searched. Any "✗" for Day could be addressed there.

## Review resolution (fact-check in `ledgers/gaps-review.md`)
| Review item | Severity | Change made |
|---|---|---|
| C07 / B4 Nunney range | MAJOR | GAP-01 and PA-14 now say what Nunney simulated: K = 500 and 5,000. At K = 5,000, u = 5×10⁻⁶ the cost is ≈ 430 + ≈ 70 per locus. K = 10,000 is marked as an interpolation (≈ 190, below 300). The direction is stated to depend on the unmeasured human M. |
| C13 Murphy 2023 | MAJOR | Title added; claims restricted to the abstract (BGS ~60% of variance; sweeps did not improve the fit). The appendix sentence "α … essentially 0 (< 10⁻⁹)" and the ~17% mean reduction were re-read by the lead agent in the Europe PMC full text (PMC10299832). It is labelled a model fit of strong sweeps, not an MK α. |
| C14 / B2 noncoding α | MAJOR | All α values are labelled coding-only. A noncoding-share table (a_nc = 0, 0.1%, 1%, 5%) now runs through K_a, Haldane, the fertility-excess cap, rates, concurrency and GAP-04. The beneficiary is restated across the range. The Messer–Petrov downward bias is noted. "Three to four orders of magnitude" is corrected to "20× to ~6,000×". |
| C06 / B3 Matheson caveat | MAJOR | Added in GAP-01 and PA-36: one annual plant, common garden, "not representative of natural conditions", no human estimate, "no general expression for a speed limit". |
| GAP-04 arithmetic | MINOR | Corrected to ≈ 70–80 per generation and ≈ 4× (≈ 3× at 325,000 generations). The Λ₀ definition is stated. The bold on the Day-credit row is removed. The cap is called an asymptote of an approximate result. |
| GAP-07 arithmetic | MINOR | 4.65 per haploid genome. Events ≈ 1.04–1.13× SNVs. 205M is ≈ 20× the rate-based count (≈ 10× the observed 20M). The ~3× indel-rate spread is noted. |
| Matrix counts | MINOR | 12 rows (not 13); 15 columns (not 14). |
| C02 map length | MINOR | 35–38 M including X; Kong 2002 and Matise 2007 cited, with access stated. |
| C26 6.6 Mya | MINOR | Attributed to Amster & Sella 2016. |
| C23 Collins 0.29 | MINOR | Verified by the lead agent in the main text (Europe PMC PMC7334194); locator added. |
| C19 Lynch 1–5% | MINOR | Marked unverified (sub-agent read only; the abstract gives a weaker statement). |
| C31 Sabeti | MINOR | Marked unverified; the window now rests on Hernandez 2011. |
| C29 McVicker | MINOR | 19–26% from the abstract. N_hc = 9.9×10⁴ verified in Table 1 by the lead agent (Europe PMC full text). Murphy's ~17% given separately. |
| C12 Hernandez ~5% bound | MINOR | Added as reviewer-reported, unverified here. |
| Spot-check 2 (Birky 1 hit) | MINOR | S15 and GAP-03 now report the CSAC 2005 reference-list hit. |
| Spot-check 3 (keruru "A sweep that old would have faded") | MINOR | Added to S18 and GAP-02; "nobody" narrowed to "nobody applies it to Day's argument". |
| C09 Birky & Walsh caveats / B7 | MINOR | Added the authors' cross-region confounding warning, and the limit that expected-rate invariance does not answer a variance or independence claim. |
| C11 / B9 Kern & Hahn | MINOR | S31 and PA-03: noted as a Perspective, written as "300 years" for generations, and contested by Jensen et al. 2019 (*Evolution* 73:111, doi:10.1111/evo.13650; abstract read). |
| C08 Durrett & Schmidt scope | MINOR | Reworded: k counts double-mutation targets; the human–chimp conclusion is qualitative; a first-occurrence result, not a fixation count. |
| C03 / C05 Nei, Ewens | MINOR | PA-10 marks the formula "per Matheson 2025" and flags the two-stage remark as unverified. PA-08 gives n ≈ 20–24. |
| C15 CSAC caveats | MINOR | PA-19 adds CSAC's own caveat on the earlier 35% (few genes; different gene sets) and cross-references relaxed constraint (GAP-05). |
| C17 Kondrashov wording | MINOR | Kept: the lead agent read "a dangerous range of selection coefficients, 1/G < s < 1/4Ne" in the Europe PMC abstract. The access note is added. |
| C18 Charlesworth quote | MINOR | Kept: verbatim in the Europe PMC abstract read by the lead agent ("It may be very difficult to distinguish between these two possibilities."). |
| B5 GAP-04 reading | MINOR | The Day credit is tied to node A (MITTENS all-fixations). It is stated as not live for H/H1. |
| B8 GAP-05 size | MINOR | Labelled an upper-end scenario, with the extrapolation stated. |
| B1 GAP-06 label | MINOR | Re-labelled "critics, weak"; tally updated. |
| B10 search-bias note | MINOR | Recorded in the tally section. |

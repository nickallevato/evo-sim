# Review: "Response to Will Duffy | PART I - Population Genetics" (Nesslig20, Peaceful Science) and its replies

_Not an audit check; no claim file, verdict or count changed._ <!-- D-41: one neutral review per source; both sides at equal depth (hard rule 1) -->

**Source.** Nesslig20 (Peaceful Science forum username), [discourse.peacefulscience.org/t/18094](https://discourse.peacefulscience.org/t/18094), posted 2026-10-05 (`created_at` 2026-10-05T22:09Z in the Discourse JSON), public, about 4,800 words with formulas. Post 1 is at Discourse version 11 and was **last edited 2026-10-07T22:58Z**, two days after posting. The bibliography's earlier held copy (sha256 `9912398e…`) is not on disk, so this page cannot say what the edits changed. All five quotes on file (PS-01 to PS-05) are exact substrings of the fetched text. Fetched 2026-11-26 into gitignored `sources/raw/ps-18094-2026-11-26/`, `t-18094.json` sha256 `82e89a07e450199c59566e09d9fa0be97bafdaa87d8a6293607005f5666ebbba`. Bibliography key PS-1 (`docs/research/sources/bib-critics.md`); source map [`nesslig20-ps1.md`](../research/math/sources/nesslig20-ps1.md); new arithmetic in object M-917 ([record](../research/math/records/M-917.py)). The post's plots are images and are not read. Its text states the numbers the plots show, and this page checks those numbers from its formulas.

**Thread.** Four replies: Mercer (#2, #4), Nesslig20 (#3) and Rumraket (#5). None has maths. Posts 6-8 are closing notices. The replies appear in §3 and §6.

**Rule U.** The post answers Will Duffy's recap presentation of MITTENS 2.x on the Gutsick Gibbon livestream (4:28-43:51), not Day directly. The video is not held, so every Duffy line is a relay. For each line the post attacks, this page says whether Day's own text makes the same claim. A Duffy line that Day never wrote is not scored against Day.

---

## 1. The argument

Nesslig20 says Duffy's main argument is a "waiting-time problem". The post answers it with neutral theory. Neutral mutations fix at the rate they arise (k = μ_G). Over 252,000 generations, with two lineages, that gives about 37.8 million fixed differences, which it compares with the 31-62 million SNVs observed. Four "DUFFY ERROR" sections follow. The 205 million counts base pairs, not mutations. The 4Nₑ mean fixation time is not a serial limit. The 1,400 generations per fixation is not the fastest LTEE rate. A human value of G_f in the F_max formula gives the same 37.8 million.

> "Let’s assume a conservative neutral mutation rate of [ μ_G = 75 ]. That means [ k = 75 ] mutations will fix per generation." (s2.2, PS-01)

> "So, the expected number of fixed neutral mutations that separates humans and chimps is ~37.8 million based on this rough calculation." (s2.2, PS-02)

> "When we take all the values for the generation times of each individual mutation, and averaged them out, that gives us [ 4N_e ], but that does not mean only one mutation fixes every [ 4N_e ] interval. The average is not the limit!" (s3.2)

The post argues against Duffy's slides, quoted by timestamp. Day's own text makes the three central claims the post attacks:
- the 205 million: Q14, and Q15, "approximately 410 million genomic differences. Apportioned symmetrically to the human lineage this yields approximately 205 million required fixations";
- the serial reading of 4Nₑ: Day, McCarthy thread comment 337074301, "At 25 years per generation, that's 1,000,000 years per neutral fixation.";
- 180 fixations at "1,400 generations per fixation (the fastest empirical rate ever measured in any organism)": Q91, quoting the 2nd-edition abstract.

Two attacked lines are Duffy's alone. One is that d is not explained; Day's papers define d (M-802). The other is the citation "Barrick et al. 2019"; the provenance of the 1,400 in Day's text is M-003.

## 2. The maths, located and rebuilt

The model is the textbook neutral model. A new mutation's fixation probability is 1/(2Nₑ). Supply is 2Nₑμ_G per generation, with μ_G per haploid genome as s2.1 defines it. So k = μ_G, whatever the population size. The count is 2 × k × T_LCA / G_T, two lineages over 252,000 generations. For timing, the post uses Kimura's distribution of fixation times conditional on fixation, with a mean of 4Nₑ. It sums that distribution over generations to show that a population starting empty reaches the steady rate after a lag of 4Nₑ. It then argues that the lag does not apply, because real ancestral populations carry standing variation. The model leaves out selection on purpose ("I will stick with neutral theory for now", s2.1). It also leaves out the ancestral-polymorphism term of pairwise divergence (M-219). The post's own Yoo quote supplies that term (39.5% ILS, ancestral Nₑ 132,000-198,000), but the count does not use it.

| Step | Equation (author's) | Inputs | Library object | Check |
|---|---|---|---|---|
| Lottery | n ≥ log(0.5)/log(1 − p) | p = 1e-8 (s1.1) | new M-917 | holds (bound 69,314,718; printed 69,314,717); "0.51" for 70M is 0.503, slip |
| Fixation probability | P_fix = 1/(2Nₑ) | Nₑ ≥ 1,000 (s2.1) | M-209; M-917 | holds: ≤ 0.05% |
| Neutral rate | k = (2Nₑ μ_G) × 1/(2Nₑ) = μ_G | μ_G per haploid genome (s2.1) | M-209, M-212 | holds as algebra |
| Count | 2 × k × T_LCA/G_T | μ_G = 75 (PS-01), 6.3e6 y, 25 y | M-213 (record); M-917 | arithmetic holds (37.8M); input 2× the pedigree haploid count: R1 crossed (§4, §5) |
| Target | 1-2% of the genome | 3.1e9 implied | M-917; M-219, M-213 | 31-62M holds as arithmetic; omits ancestral polymorphism and CSAC's 14-22% polymorphic share |
| Toy alignment | 1/60, 9/60, 10/60 | 60 bp, 1 SNV, one 9 bp indel (s3.1) | M-011; M-917 | holds |
| 205M | 410 Mbp / 2 | "~14%" of 3 Gbp (s3.1) | M-009, M-011 | holds as arithmetic; components differ from Day's (§4) |
| Mean fixation time | T_fix ≈ 4Nₑ | Nₑ = 10,000 (Duffy's) | M-203 | holds: 40,000 |
| Fixation-time CDF | F(t) = 1 + Σ (−1)^i (2i+1) e^(−i(i+1)t/4Nₑ) | 50 terms (s3.3) | new M-917 | holds: every printed quantile reproduces |
| Lag | μ ∫₀ᵀ F → μ(T − 4Nₑ) | as above (s3.4) | M-201 (record) | holds for the asymptote |
| SFS | E(ξ_i) = θ/i, θ = 4Nₑμ_G | (s3.4) | M-211; M-917 | formula holds; the gloss 2Nₑμ_G × 2Nₑ is wrong (slip) |
| F_max (Duffy) | 6.3e6 × 1/(25 × 1,400) = 180 | Day's 2nd-edition inputs | M-711 (record) | holds |
| LTEE G_f | 20,000/45; (40,000 − 26,500)/(653 − 60) | the paper as quoted (s3.5) | new M-917 | holds: 444.4 and 22.77; these are clone counts, not fixation rates (§4) |
| Genome rates | μ_S × L | E. coli < 1e-9 × 4.6e6; human > 1e-8 × 3.2e9 | M-917 | holds: < 0.0046, > 32 |
| F_max (post) | 2 × 6.3e6/(25 × 0.013) = 12.6e6/0.33 = 37.8M | G_f = 1/75 | M-917 | exact 37.8M; the printed 12.6e6/0.33 is 38.18M (+1.0%, slip) |

**Numbers, recomputed** from the author's inputs only (each one asserted in the record named):
- n₅₀ = 69,314,717.7, so n ≥ 69,314,718; P(2e8) = 0.8647; P(4e8) = 0.9817; P(any of 7e7) = 0.5034 (M-917).
- 2 × 75 × 252,000 = 37,800,000 (M-213). At the library's pedigree rate, 2 × 38.4 × 252,000 = 19,353,600 (M-213). Over 1.1-1.5e-8 per site the count is 17.74M-24.19M, which moves 37.8M by −53% to −36%. 75 per haploid genome implies 2.34e-8 per site (M-917).
- 0.01 × 3.1e9 = 31M; 0.02 × 3.1e9 = 62M; 19.35M is 37.6% below 31M (M-917).
- Median fixation time 3.4788Nₑ (34,788 at Nₑ = 10,000). F(4Nₑ) = 0.6063. The 95%, 99% and 99.9% points are 8.1878, 11.4075 and 16.0127 Nₑ. The series mean is exactly 4Nₑ (M-917).
- Empty-start delivered share over 252,000 generations: 0.8413 at Nₑ 10,000, 0.0190 at 132,000 and 0.0017 at 198,000 (M-917; M-201 for the first).
- 20,000/45 = 444.4; 13,500/593 = 22.77; 1/444 = 0.002252, which is 5.49× U_E = 4.1e-4 (M-917; M-007).
- 12.6e6/0.33 = 38,181,818; 12.6e6/(25/75) = 37,800,000 (M-917).

The arithmetic holds everywhere except two printed roundings (0.51, 12.6e6/0.33) and the θ gloss, and none of these moves a conclusion. Two problems are not arithmetic: the size of one input (μ_G = 75) and the match between what the model counts and what it is compared with (post-split fixations against all SNV differences).

## 3. What holds

**For the critics (Nesslig20, Neukamm, the repliers):**
- *k = μ_G.* Supply and fixation probability cancel when both use the same Nₑ (M-209; Day's 2026-08-27 concession is recorded there). The post states the definitions and the algebra (s2.1). The McCarthy reviews settled this already ([item 1](2026-11-26-dennis-mccarthy-probability-zero-wrong.md), [item 2](2026-11-26-dennis-mccarthy-vox-day-responds.md)), and it is not repeated here.
- *The 4Nₑ mean is not a throughput limit.* Day's own comment reads it serially ("1,000,000 years per neutral fixation", mc1c#337074301). The post's answer, that alleles fix in parallel, is M-706 (Day's 4Nₑ objection is covered in [McCarthy item 2](2026-11-26-dennis-mccarthy-vox-day-responds.md)). Its quantiles reproduce: half of a cohort's fixations come before 3.48Nₑ and 61% before 4Nₑ (M-917). The cars analogy (s3.2) is apt: a mean transit time of 2 h does not cap 10 h at 5 cars.
- *Both sides' texts agree on one number.* F(4Nₑ) = 0.606 in the post. Day's Hard Limits says the pipe "substantially fills" near T = Nₑ, and the audit computed the fill at T = 4Nₑ as 0.61 (Q152, R4-B2). These are the same quantity: the rate reached at time T from an empty start is μ × F(T).
- *The lag is 4Nₑ for the asymptote* (M-201), as the post says. Standing variation is the right objection to the empty start for the observable: pairwise divergence is not reduced by the empty-pipe term (M-219; claim B1 is `contested`, and its note reads "contradicted for the human-chimp observable (B4a)"). Nesslig20's #3 reply to Mercer ("Already covered in section [3.4]") is accurate.
- *205M counts bases, not events.* The toy alignment is correct (two mutations, ten bases; M-917), and the unit point is the library's settled result ([McCarthy item 2](2026-11-26-dennis-mccarthy-vox-day-responds.md); M-011; A3x external `supported`, 21.05M events per lineage). PS-05, credited to Martin Neukamm, understates its own case: the largest indel event in the audit's GAP-07b count is 25.2 Mb, and 71 events exceed 1 Mb (A3x).
- *The "fastest empirical rate ever measured" wording fails.* Point-mutator LTEE lines fix at 43-183 generations per fixation (M-711). The post's 22.77 is a clone count (§4), but its direction matches.
- *The caveat cuts against the post's own comparison* (PS-03). Reference-genome differences include polymorphism (CSAC 14-22%; M-213). The post flags this unprompted.

**For Day's side:**
- *Haldane's limit is accepted as stated* (s2.1; M-801, claim H6). The post agrees that the cost bounds selected substitutions and does not dispute Day's 300 generations.
- *Duffy's 4Nₑ = 40,000 is "accurate"* (s3.2). The post concedes Day's time scale and disputes only its reading.
- *The arithmetic of 180 holds* (M-711; G2b internal `holds`). The post's s3.5 does not find an error in it. It replaces G_f (§4).
- *The post leaves selection out on purpose* (s2.1, s3.2: "his objection (whether correct or not) do not apply here"). Day's parallel-fixation objection for selection is not answered here (M-801 Day position).

## 4. What fails

### Errors (rule R1: correcting it moves the stated conclusion by >25% or flips it)

**PS-01 → PS-02, reading-dependent.** The post defines μ_G as "the neutral mutation rate per haploid genome per generation" (s2.1). It then cites uncited "100 to 200 per generation" and assumes 75 (s2.2). The library's pedigree rate is 1.2e-8 per site (range 1.1-1.5e-8; `parameters.yaml`, Kong 2012). That gives 38.4 per haploid genome (35.2-48.0), and 75 implies 2.34e-8 (M-917).
- *Correction.* 2 × 38.4 × 252,000 = 19.35M (M-213). Across the pedigree range the count is 17.74M-24.19M. If 75 is read as a zygote count, it is 18.9M.
- *Size.* PS-02 moves by −36% to −53% (−50% on the zygote reading). That is past 25% at every pedigree value. The move stays under 25% only at 1.76e-8 per site or more (M-917). On the downstream number, R1 is met.
- *The stated conclusion.* "That is close to the estimated 1-2% difference … 31-62 million". The corrected 19.35M is 37.6% below the bottom of that band, so "close" fails at 1.1-1.2e-8. At 1.5e-8, 24.19M is 22.0% below, inside the 25% line (M-917).
- *Field value.* The most defensible reading takes 75 as stated: per haploid genome, uncited (rule F). The arithmetic then holds and the input is `unverifiable`. That is the reading claim B5e already uses (R4 X1 rescore). Under the pedigree rate it is an R1 error. The verdict table (§7) lists both.
- *The broader conclusion survives* ("Most differences between humans and chimps can be accounted for by the fixation of neutral mutations"), but by another route than the post's. R4 B4a has about 19M post-split plus about 15M ancestral against 35M (M-219). The post's 37.8M match comes from a count about twice the pedigree value, compared with a total that also contains ancestral polymorphism. Both corrections pull in opposite directions and roughly cancel. This is the same issue as B5c (Hancock's first pass).

The same 37.8M is reached again in s3.5 by G_f = 1/75. So the same correction applies there and adds no second error.

### Non-sequiturs and hidden premises (rules N, U)

- **The Texas sharpshooter against a count (s1, s2).** *Premise:* waiting-time arguments price specific mutations and ignore the alternatives. *Implicit:* Duffy's argument is one of these. *Conclusion:* "The main argument was a type of ‘waiting-time problem’". MITTENS counts throughput: 205M fixations of any kind against 180 achievable (Q14, Q91). Specific against any (M-704) bears on the Darwillion (G3, G4), not on that count. The post's own answer in s2 is a throughput answer (k = μ_G), which shows the sharpshooter framing is not doing the work. Fidelity on the framing: partial.
- **s3.5 "Correcting bad math" replaces the model.** *Implicit premise:* F_max's G_f is an all-cause throughput, so a neutral human k may stand in for the LTEE rate. Day's framing of the same formula is selection: "natural selection can accomplish at most 180 fixations" (Q91). The arithmetic of 180 holds (G2b). The post's step is a model substitution, and its title calls it a correction. The substitution has real support: the LTEE G_f is all-cause, and its neutral share scales with per-genome supply (M-916, the KITTENS review). But it is an argument about which model applies, not a correction of Day's arithmetic.
- **G_f = 444 compares a clone count with a fixation rate (s3.5).** The 45 mutations are the count in a sampled genome at 20,000 generations, as quoted from the paper. Day's G_f is a population fixation rate under a stated counting rule (M-503: non-mutator mean 45.4 at 60,000 on the pooled ≥ 95% rule). "not 1,400" therefore does not follow from 444 as stated. The mutator figure (22.77) has the same caveat. Its direction is confirmed by the fixation-based M-711 (43-183).
- **"This is actually close the the observed mutation rate in bacteria." (s3.5).** This holds against the post's own bound (1/444 = 0.00225 < 0.0046). Against Day's own U_E = 4.1e-4 (M-007) it is 5.49×. The post's earlier caveat in the same paragraph, that Barrick et al. "argue that most of the accumulated mutations in E. coli were beneficial", is the reason for the gap. "close" is loose, not wrong in direction.
- **"You will approach the constant rate rather quickly" (s3.4).** *Implicit:* the human lineage's Nₑ is about 10,000 from the split on (Duffy's value). The post's own Yoo quote gives ancestral Nₑ 132,000-198,000. At those values 4Nₑ = 528,000-792,000, which is 2.1-3.1× the window. An empty start would then deliver 1.9% and 0.17% of μT (M-917). The post's next paragraph removes the empty start by appeal to standing variation, and that is the stronger answer (M-219). "Rather quickly" depends on Duffy's Nₑ.
- **Rule U, lines not scored against Day.** "Will does not explain what it actually means" (d) is about Duffy: Day's papers define d (Z18168236, 0.45; M-802), and the 2nd edition and 3.0 drop it (M-001). "I cannot find where 1,400 value comes from in this paper" is about Duffy's citation. The 1,400 is Day's 2nd-edition abstract figure (M-003).

## 5. Slips (rules R1, SC; ledger level)

- **Lottery, s1.1:** "n ≥ 69,314,717" is the floor of 69,314,717.7; the bound is 69,314,718. No effect.
- **Lottery, s1.1:** "The probability that at least 1 out of 70 million wins is [ P =0.51 ]" is 0.5034 (0.51 needs 71.3M tickets; M-917). −1.3%, and the conclusion ("not remarkable") stands.
- **θ gloss, s3.4:** "the product of the rate at which new mutations enter the population [ 2N_e \times µ_G ] and the average time mutations spend drifting until they are fixed or lost [ 2N_e ]". That product is 4Nₑ²μ_G, not 4Nₑμ_G. By the post's own E(ξ_i) = θ/i, a new mutation's mean sojourn is 2 H_(2Nₑ−1) = 20.96 generations at Nₑ = 10,000, not 20,000 (M-917). No number in the post depends on it.
- **s3.5 chain:** 25 × 0.013 = 0.325, printed "0.33", and 12.6e6/0.33 = 38.18M, printed "37,800,000". The exact 1/75 gives 37.8M. This is a rounding in the printed intermediate (+1.0%).
- **PS-05 range** ("10s to … 100s of thousands of bp") understates the measured maximum (25.2 Mb, A3x). It errs in the critic's disfavour, so it is not material.
- **"Barrick et al. 2019"** is Duffy's citation as the post reports it. The library holds Day's 2019 citation as "NATURE, 2009" and 2025's as Good 2017 (M-003). Not checked further (video not held).
- **SC:** none. The post was edited to version 11 within two days, but the pre-edit text is not held. This page does not know what changed.

The R1 item for PS-01 / PS-02 is in §4, not here, because it crosses 25% on the downstream number under the pedigree reading.

## 6. Rhetoric (rule RH)

| Quote (locator) | Device | Audience | Function | Dialectical core | Better answer (aimed at the move, never at the person) |
|---|---|---|---|---|---|
| "This fallacy applies to a variety of arguments commonly made Cdesign proponentsists [not misspelled]." (s1.2) | in-group nickname for opponents | Peaceful Science regulars | mark the opponents as a known type before the argument | specific against any (M-704) | "Name the argument, not the camp: MITTENS counts any 205M, so the sharpshooter point has to be shown to apply to a count." |
| "Will gets the calculations very wrong, but he is just borrowing erroneous equations from someone else" (s2) | verdict before argument; attribution | readers of both parts | frame Duffy as a relay | s3's four items | "Show the four items first; whose equations they are matters less than whether 180 and 205M survive them." |
| "This would not be the first instance where Will Duffy comes to a wrong conclusion simply because he is repeating an argument from someone else" (s2) | track-record (circumstantial ad hominem) | forum regulars | lower trust in the presenter | none | "Earlier errors don't settle this one; 2 × 75 × 252,000 does, or doesn't." |
| "The average is not the limit!" (s3.2) | slogan | general readers | make M-706 memorable | serial against aggregate (M-706) | Fair, and true. Day's own "1,000,000 years per neutral fixation" is the line it answers, so quote that line. |
| "including the instance when Casey Luskin LIED by doctoring supplementary figure III.12" (s3.1) | accusation of deceit against a third party | readers who know the ~85% dispute | discredit a source of the argument | within-species gap divergence (gorilla 13.8%), not checked here | "Show the two versions of figure III.12 and let readers judge; the gap-divergence point stands without the charge." |
| "doing a thorough breakdown of Vox’s nonsense and shenanigans" (s4) | dismissive labels | forum regulars | alignment with the GG/Hancock video | none here (GG-04..GG-13) | "Point to the step in the video that breaks Day's number." |
| "1,400 generations per fixation (the fastest empirical rate ever measured in any organism)" (Day, Q91; relayed by Duffy, s3.5) | superlative | MITTENS readers | make 1,400 a hard ceiling | M-711 | "Fastest among non-mutator populations; the point-mutator lines fix at 43-183 generations per fixation (M-711), so state the ceiling's scope." |
| "selection and drift are acting far more on existing variation, which in humans (the only species IDcreationists care about) outnumbers new mutations a million to one." (Mercer, #2) | hyperbole plus out-group label | thread | move the frame from new mutations to standing variation | standing variation feeds divergence (M-219) | "Give the ratio's basis and source; the standing-variation point (s3.4, M-219) carries itself without it." |
| "IOW, the idea of a population waiting for mutations is simply silly." (Mercer, #2) | ridicule | thread | dismiss the waiting-time frame | as above | "Day's empty start (M-201) is a model of new post-split mutations; say which observable it gets wrong (pairwise divergence, M-219)." |
| "IDcreationist propaganda capitalizes (likely unwittingly) on the common lay misunderstanding that evolution doesn’t occur without a new mutation happening." (Mercer, #4) | motive attribution, softened | thread | explain why the frame persists | as above | No Day text in the library says every change needs a new mutation; answer the empty-start model instead. |
| "Ahh but Will had an expert mathematician teach him population genetics in a month. Checkmate." (Rumraket, #5) | sarcasm at the presenter's training | thread | mock | none | "Training is not the test; the 205M unit and the 4Nₑ reading are." |

Rhetoric changes no verdict. The post's rhetoric sits around its arguments, not inside them: every rhetorical line has a dialectical neighbour that carries the point. The replies hold no maths.

## 7. Verdicts under the audit's rule (informal; not entered in any claim file)

| Statement (locator) | Reading | Internal | Fidelity | External | Note |
|---|---|---|---|---|---|
| "Let’s assume a conservative neutral mutation rate of [ μ_G = 75 ]. That means [ k = 75 ] mutations will fix per generation." (s2.2, PS-01) | 75 per haploid genome, as stated (uncited) | holds | unverifiable (rule F) | contested | **reading-dependent**; field value; as B5e |
| | 75 is a per-zygote count, or the pedigree rate applies | non-sequitur (input against the s2.1 definition) | n/a | contradicted | R1 met: PS-02 moves −36% to −53% (M-917) |
| "the expected number of fixed neutral mutations that separates humans and chimps is ~37.8 million" (s2.2, PS-02) | arithmetic on the stated input | holds | unverifiable (input F) | contested | **reading-dependent**; field value |
| | as the expected post-split count | holds | n/a | contested | 17.7-24.2M at pedigree rates; with ancestral term about 34M (B4a) |
| "That is close to the estimated 1-2% difference … 31-62 million single-nucleotide variants" (s2.2) | at 75 as stated | holds | n/a | contested | **reading-dependent**; field value; polymorphic share not removed (PS-03) |
| | at 1.1-1.2e-8 per site | non-sequitur | n/a | contradicted | 19.35M is 37.6% below 31M |
| "Most differences between humans and chimps can be accounted for by the fixation of neutral mutations." (s2.2) | as stated | holds | n/a | contested | as B4a (contested; ancestral term carries part) |
| "since they use one (or a few) reference genomes, not all of the differences … are actually fixed" (s2.2, PS-03) | as stated | holds | accurate | supported | CSAC 14-22% (M-213) |
| "Haldane’s reproductive cost limit does not apply to drift" (s2.1, PS-04) | as stated | holds | partial | supported | as H6 |
| "one InDel can affect many base-pairs, ranging from 10s to 10s of thousands or even 100s of thousands of bp" (s3.1, PS-05, Nesslig20 relaying Neukamm) | as stated | holds | accurate (credited) | supported | as A3x; top of range understated |
| "This exact mistake produces the erroneous 205 million mutations fixed in the human lineage" (s3.1; Day's own, Q15) | as an event count | holds | partial (components differ from Q15) | supported | **reading-dependent**; field value; as A3x; Day's weighting reading (Q99) is §8 |
| | as Day's stated weighted requirement | non-sequitur | partial | contested | as A3a (reading-dependent there too) |
| "restricts drift such that it is only fixing one mutation at a time" (s3.2; Day's own, mc1c#337074301) | Day's "per neutral fixation" read as a throughput interval | holds | accurate | supported | **reading-dependent**; field value; M-706 |
| | Day meant a per-allele transit time (true) | holds | partial | contested | then the live question is the lag (s3.4, M-201) |
| "50.0% … by generation [ t≈3.48N_e ≈ 34,790 ]. Around 60.6% … [ t≈4N_e ≈ 40,000 ]" (s3.3) | as stated | holds | accurate (Kimura) | supported | M-917; Day's Hard Limits fill 0.61 agrees |
| "the lag for reaching the constant rate is exactly [ 4N_e ]" (s3.4) | asymptote | holds | n/a | supported | M-201 |
| "Furthermore, this “lag” does not even apply in the real world." (s3.4) | for the pairwise-divergence observable | holds | n/a | supported | **reading-dependent**; field value; M-219, B1 |
| | for new post-split fixations | non-sequitur | n/a | contested | empty start exact for those (M-201) |
| "the average time mutations spend drifting until they are fixed or lost [ 2N_e ]" (s3.4) | as stated | non-sequitur (against the post's own E(ξ_i) = θ/i) | n/a | contradicted | slip, no number moves (§5) |
| "Duffy says this is “the fastest rate of mutational fixation ever observed”, which wrong" (s3.5; Day's own, Q91) | as stated | holds | accurate | supported | M-711 (43-183 gen/fix) |
| "That would give us [ G_f = \frac{20000}{45} ≈ 444 ] not 1,400." (s3.5) | as stated | holds (arithmetic) | partial (clone count) | contested | M-503 counting rule |
| "This is actually close the the observed mutation rate in bacteria." (s3.5) | below the post's own bound | holds | n/a | contested | **reading-dependent**; field value |
| | close to U_E = 4.1e-4 | non-sequitur | n/a | contradicted | 5.49× (M-917) |
| "37.8 million fixed neutral mutational differences between humans and chimps. The same number I calculated previously" (s3.5) | as a neutral count | holds | unverifiable | contested | **reading-dependent**; field value; as PS-02 |
| | as a correction of Day's F_max | non-sequitur | partial | contested | model substitution; G2b internal holds |
| "His flawed reasoning commits the Texas sharpshooter fallacy." with "The main argument was a type of ‘waiting-time problem’" (s1.1, s2) | of specific-mutation waiting-time arguments | holds | n/a | contested | **reading-dependent**; field value; as G3 |
| | of the MITTENS count | non-sequitur | partial | n/a | the count needs any 205M |
| "outnumbers new mutations a million to one" (Mercer, #2) | as a number | holds | unverifiable (rule F, basis unstated) | untestable | **reading-dependent**; field value |
| | as hyperbole: standing variation matters | n/a (rhetoric, RH) | n/a | n/a | M-219 |

Rule RD: where the verdict depends on the reading, every plausible reading is listed, and the field value takes the reading under which the statement is most defensible. Ten of the rows above are reading-dependent.

## 8. Day-side steelman

The post's headline number is twice what its own definitions allow. It defines μ_G per haploid genome and then inserts 75. At the library's pedigree rate that slot holds 38.4, so 37.8M becomes 19.35M (−49%), and 17.7-24.2M over the whole pedigree range (M-917). Against the 31-62M band the post chose, the corrected count is 37.6% short at 1.2e-8 and still 22.0% short at 1.5e-8. The post's "close" survives only through the ancestral polymorphism term, which the post never adds: its own Yoo quote supplies 39.5% ILS, and the post leaves it unused. Its s3.5 "correction" reaches the same 37.8M with the same input, so it is not independent confirmation. It also replaces Day's selection model with a drift model rather than finding an error: Day's abstract says "natural selection can accomplish at most 180 fixations" (Q91), and the 180 is correct arithmetic (G2b). The lag argument relies on Duffy's Nₑ = 10,000. The ancestral Nₑ the post quotes (132,000-198,000) puts 4Nₑ at 2.1-3.1× the window, and an empty start would deliver only 0.17-1.9% of μT (M-917). Rescuing it needs standing variation, which turns the count into pairwise divergence with an ancestral share, not post-split fixations. That is the observable on which B1 and B4a stay contested. The sharpshooter framing misses MITTENS, which asks for any 205M fixations, not specific ones (M-704; G3 is a different claim). On 205M, Day's stated rationale is that "Counting these by base pair, as the gap-divergence figure does, is generous to the standard model" (Q99): one structural event must arise and fix as a single low-probability event. The post's toy alignment does not engage that weighting argument (A3a is reading-dependent for this reason). The post's 444 against "not 1,400" compares a clone's mutation count with a population fixation rate under Day's counting rule (M-503). The post concedes Day's time scale (4Nₑ = 40,000 is "accurate") and Haldane's limit (M-801), and it sets selection aside entirely. So the adaptive question MITTENS was built for is untouched.

## 9. Critic-side steelman

The post's central claims hold where it matters. k = μ_G is algebra on the post's stated definitions (M-209), and Day has conceded the identity (2026-08-27). Day's own comment reads 4Nₑ serially ("1,000,000 years per neutral fixation", mc1c#337074301). The post shows with Kimura's own distribution that a 4Nₑ mean caps nothing. Half a cohort fixes by 3.48Nₑ, 61% by 4Nₑ, 99% by 11.4Nₑ, and the cumulative count trails the steady rate by exactly 4Nₑ (M-917, M-201). Day's Hard Limits gives the same 0.61 fill at 4Nₑ (Q152, R4-B2), so the two texts agree on the dynamics and differ only on how to read them. Standing variation removes the empty-start lag for the observable that is actually measured, pairwise divergence (M-219; B1's note: "contradicted for the human-chimp observable (B4a)"). The post states this in s3.4, and the thread confirms it (#3). On 205M, the toy alignment is correct, and the library's measured count is 21.05M events per lineage, not 205M (A3x `supported`, M-011). PS-05 understates the case: single events reach 25.2 Mb. Day's own "fastest empirical rate ever measured in any organism" (Q91) is false of the point-mutator lines (43-183 generations per fixation, M-711), and Day's 3.0 itself reports a hypermutator figure (Q14). The G_f in F_max is an all-cause throughput whose neutral share scales with supply (M-916). So substituting a human neutral k is the right comparison for the neutral share, not a change of subject. The input slip on 75 does not reverse the conclusion. At the pedigree rate the post-split count is about 19M, the ancestral term is about 15M, and the sum is about 34M against 35M observed (B4a). "Most differences … neutral" therefore survives the correction, and the post flags the polymorphism caveat itself (PS-03). Nothing in the post's arithmetic is wrong beyond two roundings and a gloss, and none of them moves a number the argument uses.

## 10. Bottom line

Nesslig20's population-genetics maths is right: k = μ_G, the fixation-time quantiles, the 4Nₑ lag and the base-against-event toy all reproduce from the post's own inputs. Its headline input is not. 75 per haploid genome is about twice the pedigree count, so the 37.8M "match" to 31-62M is an R1 error under the pedigree reading (−36% to −53%). The broader conclusion that most differences are neutral survives only once the ancestral-polymorphism term, which the post quotes but does not use, is added. Against Day's own text, the post lands three points: 205M counts bases, "1,000,000 years per neutral fixation" is a serial reading, and 1,400 is not the fastest LTEE rate. It does not touch the 180 arithmetic, Haldane's limit or the adaptive question, and its sharpshooter framing does not fit a count. The critics may fairly take the parallel-fixation and unit points. Day may fairly take the doubled input, the unused ancestral term and the untouched selection argument.

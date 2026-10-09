# Review of R4-GAP07b-alignment: steelman from the critics' side

Reviewer stance: the most capable, honest defender of the critics' position on the unit argument (McCarthy, Mansfield, Fun-Friendship4898, Neukamm via Nesslig20, Hancock, Camestros, the Reddit and KITTENS authors). I was asked to argue for them as strongly as honestly possible and then say whether the check gives them their due.

Scope read: `research/checks/results/R4-GAP07b-alignment.md` (cited below as "the note", with section numbers), the pre-registration docstring of `research/checks/gap07b_alignment_count.py`, `results/raw/gap07b_posthoc_ladder.out`, claims `A3`, `A3a`, `A3b`, `A3c`, `A3d`, `A3x`, `A3x1`, `docs/research/sources/quotes-critics.md`, `docs/research/ledgers/gaps.md` (GAP-07, GAP-01 note, lines 461-520, 250, 590), the earlier review `REVIEW-R4-GAPS-steelman-critic.md`, and `sources/raw/critics/arctic-tree-1wv4zeg.json` (read only, untrusted). Nothing was executed from `sources/raw/`; no other file was edited.

Numbers marked "reviewer scratch" were computed by hand or in a throwaway script outside the repo (`python3 -I`). They should be re-run through a repo script before being cited.

## Verdict in brief

The check is a strong piece of work for the critics on the one thing it set out to test. A real alignment gives 42.1 M events, 21.05 M per lineage, and the pre-registered "favours critics" criteria were met while every "favours Day" criterion failed. The pre-registration, the disclosure of what was seen before registering, and the honest list of missed predictions (P1, P3, P5 L2, P6 indel polarization) are exactly what the critics' side needs for the result to be trusted.

Where I think the note under-delivers for the critics:

- The headline 9.7x is the lowest ratio that the note's own numbers support. It is computed without the polymorphism correction, with the pooled lineage mean instead of the human lineage Day actually refers to, and with the SNVs from >2%-divergence records left in. Corrections the note lists in prose never reach the table, section 11 or section 13.
- Two "credit to Day" statements do not survive the note's own data: "the SNV-only figure is a floor", and "the bp magnitude is real / divergence beyond SNVs is reproduced". The second counts aligned, ~98%-identical sequence as divergent.
- The critics' independent numbers (McCarthy 22.5 M, Nesslig20 37.8 M, Hancock about 38 M, the 9.7 M rate route) are not set against the measurement, although the measurement is the first thing that can grade them.
- The note says the critics' arithmetic "holds up" but frames it as resting on an ambiguity, and it does not record which errors were whose.

Where the note is right and I would not change it: events are kept apart from fixations that need selection (caveat 6); the 410.09 Mb coincidence is flagged and not leaned on (finding 10 shows a base rate that supports its reading); the alignment-fragmentation bias is admitted to be Day-favouring.

## Summary

- 12 findings: **6 MAJOR** (1, 2, 3, 4, 5, 6) and **6 MINOR** (7, 8, 9, 10, 11, 12).
- Direction: findings 1, 2, 3, 5 and 6 add credit to the critics or trim credit to Day. Findings 8, 9 and 10 trim the critics' side or confirm the note, and are included so the review is two-sided. Finding 5 is double-edged: it also records that the critics' k = mu rate route undershoots the measured SNV count by about 1.9x.
- None of the findings changes the verdict "Critics, on the unit argument". They change its size (9.7x becomes "about 10x raw, 11-14x after the corrections", with a stated floor) and the Day-credit bullets.

---

### 1. MAJOR. The headline 9.7x is the minimum of the note's own ratios; the corrections it already computes never reach the table, section 11 or section 13

**Locator.** Note section 0: "**Day's 205 M per lineage is 9.7 times the measured events per lineage** (21.05 M; 10.8 times on the <2% set; 11.3-12.5 times if only the 78-86% fixed share of the differences is counted)." Section 7 table (human 19.9 M, chimp 22.1 M per lineage). Section 13: "A3x `external:` can cite a measured 42.1 M events (21.1 M per lineage), 205 M = 9.7x". Raw: `gap07b_posthoc_ladder.out`: "fixed-only events per lineage at 0.78: SNV 14729284 + indel 1677644 = 16406929 ; 205M/that = 12.49" and "at 0.86: ... = 18089691 ; 205M/that = 11.33".

**Argument.**
- The ratio the note reports as "the" result is the pooled, uncorrected one. Each correction the note itself defends moves it in the same direction:
  - *Human lineage, not the mean.* Day's 205 M is "apportioned symmetrically to the human lineage" (A3a, MITTENS 3.0 s7.1). The note's own human-lineage estimate is 19.9 M (section 7), which gives 205/19.9 = 10.3x (reviewer scratch). The chimp branch is the longer one (51% of polarized SNVs), so the pooled mean favours Day slightly for this comparison.
  - *Records above 2% divergence.* The 4.0 M extra SNVs "sit in alignment records of 2.6%, 6.8% and 14.2% divergence ... nested/rearranged fills, paralog and duplicate alignments, and ancestral polymorphism" (section 4). The note itself says CSAC's 35 M "match the <2% class well". The <2% ratio is 10.8x. It is in the prose, not in the table.
  - *Polymorphism.* CSAC puts 14-22% of the differences as polymorphic (A3c). The fixed-only ratio is 11.3-12.5x (ladder output above). It appears in the prose in section 0 and nowhere else.
  - *Both together* (not additive, because some of the >2% SNVs are themselves polymorphic): 38.1 M/2 x 0.78-0.862 = 14.9-16.4 M, i.e. 12.5-13.8x (reviewer scratch). Treat this as an upper end, not a point.
- Within the same note, section 8 shows 22x and 24x under repeat masking, correctly labelled "a lower bound for 'unique sequence' events" rather than a correction. I do not propose using those.
- The honest critic-side statement is a range with a stated floor: raw counting gives 9.7x; every correction the note itself lists pushes it up to about 11-14x; and the biases that push it down (back-mutation and multiple hits at 1.3% divergence, which is small; unmeasured alignment fragmentation, finding 8) are small and carry through to a ratio no lower than about 9. A reader who sees only "9.7x" will carry away the minimum.
- Section 13's suggested A3x edit repeats the single figure, and the A3x `external:` line in the claim file already says "~9-11x", so the correction would be welcome there too.

**Fix.**
- Replace the single-number lede with a short ratio table: raw pooled 9.7x; human lineage 10.3x; <2% records 10.8x; fixed-only (0.78-0.86) 11.3-12.5x; both corrections 12.5-13.8x (labelled non-additive).
- In section 13 suggest the A3x text "about 10x raw, 11-14x after polymorphism and record-divergence corrections".
- State once that the polymorphism fraction (14-22%) is a SNV figure and that applying it to indels is an assumption (section 7 of the ladder does this silently).

### 2. MAJOR. "The SNV-only figure is a floor and not the event count" contradicts the note's own fixed-only event numbers

**Locator.** Note section 11, Day bullet 2: "The SNV-only variant (17.5 M per lineage, A3b) leaves out the indel events: about 2.2 M per lineage on the measured data, so 19.1-21.1 M per lineage is the event total. The shift is about 12-20% and does not rescue the unit argument, but it shows the SNV-only figure is a floor and not the event count." Section 13: "A3b: the SNV-only concession leaves about 20% of events out (indels, ~2.2 M per lineage)." Raw `gap07b_posthoc_ladder.out` line "fixed-only events per lineage at 0.78: ... = 16406929" and "at 0.86: ... = 18089691".

**Argument.**
- Day's 17.5 M is 35 M/2 of the differences, which includes polymorphism (A3b `assumptions`, A3c: "Implicit: the 35M SNVs are all fixed differences (CSAC: 14-22% polymorphic)"). Once polymorphism is taken out, the measured fixed-only events per lineage are 16.4-18.1 M, which brackets 17.5 M.
- So the SNV-only figure is a floor only if polymorphic differences are counted as required fixations. On the critics' reading (A3c, Nesslig20 PS-03, Camestros CA-04) the 17.5 M is roughly the right fixed-event count. The two errors in Day's SNV-only variant (it leaves out indels; it includes polymorphism) approximately cancel.
- The note asserts the first error and does not mention the cancellation. As written, section 13 would put "leaves about 20% of events out" into A3b, where it reads as a point against the critics' side's "17.5 M is about right" and as support for Day's 205 M being less distant from the true count than it is.

**Fix.**
- Replace the sentence with: "Without a polymorphism correction the SNV-only figure is 12-20% below the event total; with the CSAC fixed fraction (0.78-0.86) the fixed-event count per lineage is 16.4-18.1 M, which brackets the 17.5 M. The two omissions roughly cancel."
- Make the same change to the section 13 A3b edit.

### 3. MAJOR. "The base-pair figure is real" and "Yoo's finding of divergence ... is reproduced" overreach: the 261-523 M rows are not divergent sequence

**Locator.** Note section 0: "The 410 M base-pair figure is of the same order as base pairs in the alignment-defined divergent regions (261-523 M), so the number is reproducible as bp but not as events." Section 11: "Alignment-defined divergent sequence is 260-520 Mb across the two genomes, so 410 M is not an invented magnitude, and Yoo's finding of divergence well beyond SNVs is reproduced in a simpler data set (non-1:1 fraction 9% of the human genome)." Section 6 table and ladder; section 10 caveat 3: "their bp are over-represented in 'unaligned' (Day-favouring direction)". Critic source: Fun-Friendship4898, Reddit 1wv4zeg (`sources/raw/critics/arctic-tree-1wv4zeg.json`, quoted in A3x): "Within any given SDR, the true nucleotide difference might be tiny, like a 1-Mb inversion is a single mutational event. Or the difference might be undefined because orthology cannot be established." and, same comment, "It's like he's comparing the difference between two books, and is conflating individual letter differences with full-page rearrangement, then counting ever single letter difference on those rearranged pages as also being letter differences."

**Argument.**
- *What the rows are made of.*
  - Row 3 (523 M) adds "non-colinear nested aligned bases" (131.3 Mb on the human side, 131.3 Mb on the chimp side by construction; `gap07b_posthoc_ladder.out`). These are aligned bases at the alignment's divergence (mean 1.25% in the <2% class; the nested and paralog records are the 2.6-14.2% classes). An inverted or translocated stretch that aligns is conserved sequence in a new place or orientation. It carries a handful of breakpoint events and almost no differing bp. Counting its bases as "divergent sequence" is exactly Fun-Friendship4898's "books" point. The bp that differ in sequence are not 523 M.
  - Row 2 (261 M) includes 59.5 Mb of hg38 centromere models, which are modelled satellite arrays with no panTro6 counterpart in the assembly (section 6, "85% of the 69.9 Mb there"), plus 88.6 Mb of chimp-placed non-aligned. "Not aligned" is a statement about two assemblies and an aligner; it is not a measurement of sequence difference. panTro6 is not T2T, so human sequence that the chimp assembly merely lacks counts here as human-lineage divergence. The N-masking in section 6 removes annotated assembly gaps but not collapsed or missing repeat content.
  - The three rows are the author's post hoc choices (section 1 labels the scripts post hoc). Three rows with 261, 448 and 523 M spanning the 410 target are what any choice of included components will produce. They do not show 410 M is a natural magnitude of anything.
- *The SNV overlap Fun-Friendship4898 raised is never tested.* The data to do it exists: 4.0 M SNVs sit in records above 2% divergence (nested and paralog fills). Adding SNVs (37.8 M) to bases in the same fills (rows 2-3) counts those SNVs and their bases twice. The note quotes FF4898's construction in section 6 and A3a, but not the overlap claim "a good chunk of those 35 million SNVs are already contained within those SDRs".
- *The right sentence* is "the base pairs in non-1:1 regions are of the order of 10^8 per genome pair; most of those bases are aligned or unalignable sequence, not sequence that differs, and Day's treatment of them as separate fixations is a unit error". McCarthy (MC-11), the Reddit commenter (RE-05) and Fun-Friendship4898 had already said the bases exist and the events are few; the check confirms that first half, so crediting Day for "reproducing" it adds nothing.
- Caveat 3 is right that the direction of the bias in "unaligned" is toward Day for one reason (non-alignable repeats). It misses the opposite point that unaligned is not the same as different.

**Fix.**
- Relabel "alignment-defined divergent regions" as "bases in non-1:1 or non-aligned regions (alignment-defined, not necessarily differing)".
- Add a row "bases that differ in sequence": SNV + clean indel bp (192.4 M, from section 6) + a lower bound for unalignable sequence (human unaligned excluding centromere models and chimp-assembly gaps). Report that against 410 M.
- Report mean identity of the nested and paralog fills, and the number of SNVs inside them (the overlap), from the existing axt output.
- Delete the sentence "Yoo's finding of divergence well beyond SNVs is reproduced in a simpler data set" or restate it as "the non-1:1 fraction is of the same order (9% vs 10%); this tells us nothing about how many mutations produced it".
- In caveat 3, add that unaligned is not divergent (assembly completeness of panTro6; centromere models).

### 4. MAJOR. Section 11 heads "points that the critics have not conceded" and then lists points the critics already make; the tag will mislead the ledger

**Locator.** Note section 11, heading "**Day, on several points that the critics have not conceded.**" Bullet 1 (the bp figure is real), bullet 4 (symmetric lineages). McCarthy MC-11 (`quotes-critics.md` line 50, "Vox Day Responds" para 26): "The 410 million base pair difference refers to structural variation, which includes duplications, insertions, etc., in which a single mutational event can cause hundreds, thousands, or even millions of base-pair differences." RE-05 (r/DebateEvolution 1wss2wj): "bases affected by a rearrangement are not separate mutation events: one structural change can affect millions of bases." A3d: Hancock's factor-of-two point is that fixation "accrues in both lineages"; justatest90 (RF-11, Reddit 1wws70t pdpbf3d): "Dr. Hancock says Day makes a 2n mistake, but Day just accounts for it elsewhere, by halving the mutation target."

**Argument.**
- Bullet 1: the critics' position is that the base pairs are real and are structural variation. They have never argued the bp count is invented. The sentence "the base-pair figure is real" credits Day with a fact the critics stated first. (The previous review of GAP-07 made the same point; finding 7 of `REVIEW-R4-GAPS-steelman-critic.md`.)
- Bullet 4: the symmetric split is the position of the critics who looked at it (justatest90, A3d invariance). Hancock's point (GG-02) is a factor-of-two on the achievable side, and A3d shows it cancels. No critic in the corpus argues the human lineage carries much less than half. The note's own indel polarization gives 38-52% human, so "any critic arguing that the human lineage carries much less than half would not find support here" is true, but nobody has made that argument, so it is not a point "not conceded".
- Bullets 2 and 3 are partly sound (see finding 2 for bullet 2; bullet 3 is a calculation, not a critic concession). The effect is that section 11 lists "Day" five times, and the ledger beneficiary tag ("Critics on the unit argument; Day credited for ...") would pick up credit for statements that nobody disputes.

**Fix.**
- Retitle the section "Where the result is not a win for the critics" and reduce it to points that the data actually bear on: polymorphism and 4 M SNVs go in the critics' favour (findings 1, 2); the SNV 37.8 M is above CSAC's 35 M (Day-neutral); the lineage symmetry is a check that Day's step is sound (Day-neutral, because no critic disputed it); the neutral fraction is not tested (finding 9).
- Drop "the base-pair figure is real" as a credit, or credit McCarthy and the Reddit commenters for it explicitly.

### 5. MAJOR. The critics' independent numbers are never graded against the measurement, and the section 13 line "the rate-based 9-11x range is consistent" is wrong for the k = mu route

**Locator.** Note section 13: "A3x `external:` can cite a measured 42.1 M events (21.1 M per lineage), 205 M = 9.7x; the rate-based 9-11x range is consistent." Section 11: "The critics' informal figures (Mansfield's ~25 M, 40 M from CSAC, 17.5-20 M per lineage) are in the right region". `gaps.md` line 590: "205M is ≈ 20× the rate-based count (≈ 10× the observed 20M)". A3x `Responses`: "critics do not give an independently derived event count from Yoo 2025; the first sourced count is the audit's". A3x `Check`: "rate x time with k = mu ... 9.6-10.4M; clock-free calibrated 18.2-19.7M; CSAC-observed basis 20.0M (22.5M upper bound). 205M is ~9-11x these".

**Argument.**
- *Wording error.* 205/9.6-10.4 is 19.7-21.4x, not 9-11x. Only the calibrated and observed routes give 9-11x. "The rate-based 9-11x range" folds two different routes into one phrase. The measurement agrees with the calibrated route (21.05 M) and disagrees with the k = mu route (9.6-10.4 M) by about 2x.
- *That disagreement is itself a finding about the critics.* The k = mu route is the one the critics used: Dumb-and-Dumber RE-06 "or about 9.7 million over its proposed 252,000 generations", and justatest90 and Wrevellyn ("about 9.7 million expected substitutions on the human lineage", A3x). The measured human-derived SNVs are 17.3 M (section 7) and 21.05 M events per lineage. The rate route undershoots by about 1.8-2.2x (reviewer scratch: 17.28/9.68 = 1.79, 21.05/9.68 = 2.17). The note records neither the agreement nor the gap. That is the B4a/GAP-06 clock tension, a Day-favouring result, and an honest two-sided audit has to put it where readers will find it.
- *The measurement is the first ruler for the critics' own estimates.* Reviewer scratch, against the note's 42.1 M total or 21.05 M per lineage:

  | critic | quoted number | locator | vs measured |
  |---|---|---|---|
  | McCarthy | "450 billion x 1/20,000 = 22.5 million fixed mutations." | MC-04, MC1 para 52 | +7% (per lineage) |
  | Mansfield | "around 25 million give or take" | MF-06 | +19% (per lineage, uncited) |
  | Nesslig20 | "~37.8 million" neutral fixed, humans vs chimps | PS-02, post 1 | -10% (total) |
  | Hancock | "we'll say about 38 million." | GG-09, t=01:56:15 | -10% (total) |
  | Dumb-and-Dumber, justatest90, Wrevellyn | about 9.7 million (SNV, human lineage) | RE-06, 1wv4zeg | -54% (per lineage) |

  Four independent critic routes land within 7-19% of the measurement; one lands at half. A3x's wording that the critics gave no independent count is true of Yoo-based counts; it hides that critics did give independent counts by the neutral-supply route. Do not let this slide into branch B (it does not show that k = mu is right), but cite it as a scoreboard. This is a consistency check, and the note should say so.
- *Hancock's GG-12 gets a cleaner reading.* Hancock says "we can account even for the highest end of the mutational differences with a model that assumes that selection was not involved at all" (GG-12, t=02:01:44) and the harvester notes that his own number (76.8 per generation) gives about 38 M, not 205 M. The measured 42.1 M events are what his 38 M can be compared with. The 205 M it cannot. That is the cleanest statement of what the check does for him.

**Fix.**
- Replace the section 13 sentence with: "the calibrated and CSAC-observed event routes (18-22 M per lineage) agree with the direct count (21.05 M); the k = mu rate route (9.6-10.4 M) undershoots it by about 2x (205 M would be about 20x)".
- Add the scoreboard above, labelled "consistency, not a test of k = mu".
- Retire the "(22.5M upper bound)" in the A3 family `Check` blocks (see finding 6).

### 6. MAJOR. The critics' arithmetic is credited, but the note frames it as resting on an ambiguity and does not record who erred; per-species vs total belongs to CSAC and the earlier audit, not the critics

**Locator.** Note section 11: "The measured total (42.1 M) is within 5% of the 40 M used in A3x (35 M SNV + 5 M indel), so the critics' arithmetic holds up; it was nevertheless built on a total (5 M) that CSAC's own wording made ambiguous." Section 5: "CSAC's sentence '~5 million events in each species' therefore overstates a per-species count; the figure is a two-lineage total." A3x `Formal statement`: "`derived:` (python3 -I) 35e6 SNV + 5e6 indel events (CSAC) + 1,140 inversions = 40.0e6 events; /2 = 20.0e6". `REVIEW-R4-GAPS-steelman-critic.md` finding 6: "'~5 million in each species' is probably not the right per-lineage figure". A3x `Check`: "(22.5M upper bound)".

**Argument.**
- *Who read 5 M which way.* The 5 M as a two-lineage total is what A3x, A3 and A3a use. The per-species reading was the audit's own upper bound in R4-GAPS (17.5 M + 5 M = 22.5 M per lineage), which the GAP-07b measurement now retires. No critic in `quotes-critics.md` reads the 5 M per species. "Built on a total that CSAC's own wording made ambiguous" is accurate about CSAC, but it lets the reader infer the critics hedged on an ambiguity. In fact they used the reading the measurement vindicates. Say so.
- *The agreement is partly offsetting errors.* Measured SNV 37.77 M is 8% above CSAC's 35 M and measured indels 4.30 M are 14% below 5 M. The two summed to 42.1 M against 40.0 M. The total is within 5%, but neither component is. The note records both separately (section 2, P1 and P2) and does not link the two when it credits the arithmetic.
- *A scope slip in A3x's sum that the note could now correct.* A3x adds "1,140 inversions" to the human-chimp total. That figure is Yoo's curated count across six apes versus the human reference (A3x1: "1,140 interspecific inversions ... is across six apes"). The human-chimp net has 453 nested inversion fills of at least 10 kb (note section 9). The effect on 40.0 M is nil (1,140 against 40 M), but it is a critic-side scope error of the same kind the audit is pointing at on Day's side.
- *Other critic slips relevant to this thread and not recorded here.* They are already in `quotes-critics.md` notes: McCarthy RF-6 "And the numbers work 400 billion x 1/20000 = 35 million point mutations fixing alone." (arithmetic flag: 20 M, not 35 M); Mansfield MF-03 (1 neutral fixation per generation gives about 450,000, not 20 M, so the illustration does not close the gap); Nesslig20 PS-01 (75 is a per-diploid-offspring de novo count stated as per haploid genome). These do not touch GAP-07b's numbers, so a pointer is enough. Hancock's 407 per generation (GG-11) is arithmetic on Day's number, not an event count.
- A two-sided audit that records Day's errors in detail should have the critics' errors on this topic in one place. The comparison is balanced if both sets are visible.

**Fix.**
- In section 11 (and in the section 13 A3x edit), say: "No critic read the 5 M per species. The ambiguity is CSAC's, and the audit's own R4-GAPS 22.5 M upper bound used the per-species reading; retire it."
- Note that the agreement of 42.1 M with 40.0 M combines SNV +8% and indel -14%.
- Suggest in A3x: replace "1,140 inversions" with the human-chimp net count (453 at 10 kb or more) or drop it.
- Add one line pointing to the critic-side slips (RF-6, MF-03, PS-01) so that readers of GAP-07b see the whole ledger.

### 7. MINOR. Polymorphism is left unsubtracted although it can be measured directly with data of the same kind

**Locator.** Note section 4: "**Polymorphism:** CSAC says 14-22% of differences are polymorphic, not fixed. ... This is not measured here." Section 10 caveat 1: "No attempt was made to subtract it." Script docstring "PARTIAL / MIXED": "ancestral polymorphism inflates SNV/indel counts relative to FIXED differences (a Day-favouring bias if polymorphic differences are counted as required fixations, a critic-favouring one if not)." A3c: "The differences between one copy of the human genome and one copy of the chimpanzee genome include both the sites of fixed divergence between the species and some polymorphic sites within each species." and "we estimate that polymorphism accounts for 14-22% of the observed divergence rate" (CSAC 2005, main text, "Genome-wide rates").

**Argument.**
- The docstring's wording ("Day-favouring if polymorphic differences are counted as required fixations") is the whole point for the critics. Nesslig20 PS-03 and Camestros CA-04 press it; the note leaves it at an estimate from 2005 drawn from one genome each.
- A direct measurement is possible without a new alignment: intersect the human-derived SNV positions (hg38 differs from chimp and gorilla) with a population variant call set (1000 Genomes or gnomAD allele frequencies in hg38 coordinates), and likewise the sites where the chimp base is polymorphic within chimps (Great Ape Genome Project). The fraction of human-derived SNVs where the hg38 allele is not fixed in humans gives the human-side polymorphic share directly. It is a measurement of the quantity, not CSAC's 2005 estimate.
- Pre-split mutations on the ancestral lineage between coalescence and the split are also not "required fixations since the split". The CSAC 14-22% is a total of this kind, so the correction is about the right size, but the note does not explain why those sites do not belong in a "required fixations" count (they arose before the lineages separated). One sentence would do.
- Two cautions to keep it two-sided: the fixed fraction was estimated for SNVs and the indel and SV fixed fraction is unknown; and the polymorphism share overlaps with the >2%-divergence SNVs (section 4), so the corrections in finding 1 are not additive.

**Fix.**
- State the reason pre-split and within-species polymorphic sites are not post-split fixations.
- Propose the population-frequency intersection as a follow-up check (GAP-07c), or at least state it under the caveats as feasible.
- Say explicitly that applying 0.78-0.86 to indels is an assumption.

### 8. MINOR. Two Day-favouring biases are described as unmeasurable though the data on disk can bound them (fragmentation, adjacent mismatches); both-sided gaps are neutral

**Locator.** Note section 8: "Alignment-fragmentation effect (one true event split into several chain gaps) could not be measured; it biases event counts up, i.e. toward Day." Section 4: "Adjacent mismatch pairs: 1,443,846 (so multi-nucleotide runs shave about 1.4 M off a 'mismatch runs' count; not applied)." Section 5: both-sided 35,138 (0.8%), 95.1 Mb clean (section 6). Script docstring: "`both` ... complex".

**Argument.**
- *Fragmentation.* The chain-gap coordinates (chain id, t range) are in hand, so a sensitivity is straightforward: merge consecutive gaps within d bp (d = 1, 10, 50 bp) in the same chain and recount. The result is a bound, not an answer, but it replaces "could not be measured" with a number.
- *Adjacent mismatches.* 1.44 M adjacent mismatch pairs are 3.8% of SNVs (reviewer scratch: 1.4438/37.77). Merging them gives 40.7 M events and a ratio of 10.1x. The note computed and then did not apply it. The result is small, but it is a critic-favouring correction that sits unused next to a Day-favouring one that is applied by default.
- *Both-sided gaps.* Counting each as one event is neutral to slightly conservative. A both-sided gap (dt and dq both positive) could be one replacement event or two events in different lineages. If counted as two, the total rises by 35 k (0.08%). It does not move the ratio, and these gaps carry 95 Mb of the 192 Mb clean gap bp, so their bp effect is much larger than their event effect. That disproportion is worth one sentence because the events/bp contrast is the check's whole point.
- *Reviewer's own caution.* Fragmentation might change the ratio by a few percent; the real risk to the unit argument is elsewhere.

**Fix.**
- Add a gap-merge sensitivity (d = 1, 10, 50) and an MNV-merged row.
- Say that both-sided gaps cannot move the event total by more than 0.1% and carry about half of the clean gap bp.

### 9. MINOR. The separation from neutral fixation is correct and could be stated with one scoping table; avoid reading 21 M as "required selected fixations" or as a neutral count

**Locator.** Note section 10 caveat 6: "**Events are not fixations.** An event list says how many mutational events separate the two copies, not how many selected fixations are required. This check is neutral on whether each event has to pass through selection (branch A vs B and the two-model framing in `R4-GAPS-04-07-02.md`)." Section 11: "The measurement does not show that events are not selected, or that neutral fixation of most of them is possible; that is branch B and H, outside this check." `gaps.md` line 250: "Day himself concedes the qualitative point: neutral fixations 'are the great majority' and adaptive fixations 'comparatively rare' (blog 2026-05-07). What nobody supplies is the number." Day, MITTENS 2.x (`sources/raw/day/zenodo-18165980.txt` line 66): "Neutral divergence: Even if 99% of divergence is neutral, 200,000 fixations remain required."

**Argument.**
- The note keeps the two arguments apart, correctly. A critic reader would still want to see that two separate mismatches stack, because that is how the critics argue it:
  1. *Unit (this check):* 205 M base pairs against about 21 M events per lineage.
  2. *Type (not this check):* G_f is a generations-per-adaptive-fixation figure from LTEE, so the numerator should be adaptive events. Day concedes the neutral majority.
- The measured 21 M is therefore an upper bound on the required adaptive fixations, not an estimate of them. A reader of "21.05 M required" could take it as the required selected count.
- Two fairness points in the other direction: the note should not multiply the two mismatches (the neutral fraction is not measured; Day's 99%-neutral reply keeps 200,000), and it should not say the event count "corroborates the requirement" either (it corroborates the magnitude of the total, not the selection-requiring part).

**Fix.** Add to section 11, "Neither side", a three-line scoping table: *unit* (measured here: 9.7-14x), *type* (neutral vs adaptive; not measured; cite `gaps.md` line 250 and the 99%-neutral line), and *rate* (k = mu; branch B). State that the ratios are not to be multiplied.

### 10. MINOR. The 410.09 Mb coincidence is handled correctly; the note can strengthen "chance" with a base rate

**Locator.** Note section 6: "Human unaligned (134.5) + chimp placed unaligned (88.6) + chimp unplaced scaffolds unaligned (187.0) = 410.09 Mb. ... I treat the match as chance, and note it only so nobody finds it later and reads it as evidence." A3a `Formal statement`: "(closest: 412.1, flagged a coincidence)". Raw `gap07b_posthoc_ladder.out`: "coincidence check: ... = 410087409".

**Argument.**
- I argued the other way first: the sentence is a gift to Day if quoted without the sentence after it. The better defence for the critics is a base rate, not omission. Reviewer scratch: 14 plausible components from the note (134.5, 88.6, 187.0, 131.3, 59.5, 37.8, 44.9, 192.4, 359.3, 37.5, 59.8, 95.1, 161.6, 596.7 Mb); 3,458 subsets of 2-5 components; two land within +-0.1% of 410 (410.09 and 410.38, the latter using different parts). The expected number by chance is about 3 (window 0.82 Mb on a spread of roughly 1,000 Mb across 3,458 subsets). So the note's reading is quantitatively supported, and A3a already has a second 412.1 coincidence from Yoo's tables.
- The note's reasons given (mixing three arbitrary components; the 187 Mb is mostly unplaced scaffolds without a human partner) are the real argument and are fine. Day's 410 is "35 M + 2 x 187 Mb" in a different construction (A3a, Fun-Friendship4898).

**Fix.** Add one clause: "A search over 3,458 subsets of 14 components of this note returns about as many hits within 0.1% of 410 Mb as chance predicts (reviewer scratch; to be scripted); A3a records a second such coincidence (412.1 Mb in the Yoo tables)." Keep the flag.

### 11. MINOR. Attribution slips in section 11: "the 'bp per event is 10' statement used by critics" and the critics' "informal figures"

**Locator.** Note section 11, "Neither side, as stated": "The 'bp per event is 10' statement used by critics needs its definition: 6 (strict unaligned) to 17 (raw gap bp)." And: "The critics' informal figures (Mansfield's ~25 M, 40 M from CSAC, 17.5-20 M per lineage) are in the right region; the measured 21 M per lineage is above the lowest of them." Source: A3x `Formal statement` ("410e6/40.0e6 = 10.25") and `quotes-critics.md` MF-06.

**Argument.**
- No critic in `quotes-critics.md` states "bp per event is 10". The 10.25 is the audit's own derived ratio in A3x. McCarthy says "hundreds, thousands, or even millions of base-pair differences" (MC-11). Attributing the 10 to "critics" invites a reader to treat 6-17 as a miss by them.
- The 40 M is the audit's reconstruction from CSAC (A3x pre-registered prediction), and 17.5 M is Day's own figure (A3b). Only Mansfield's 25 M is a critic's number, and it is uncited and does not say per lineage or total ("The numbers I've seen give this number around 25 million give or take, not 200 million", MF-06). Placed next to 205 M, it is read as per lineage; the note should say the reading is assumed.
- A cleaner view for the critics: the note's size table already tests McCarthy's actual claim. McCarthy said one event can span "hundreds, thousands, or even millions" of bp, and Neukamm (relayed by Nesslig20, PS 18094 post 1) "one InDel can affect many base-pairs, ranging from 10s to 10s of thousands or even 100s of thousands of bp". The measured spread is: 11-50 bp, 353,949 events; 1-10 kb, 20,928; 10-100 kb, 1,905; 100 kb-1 Mb, 359; over 1 Mb, 71 (section 6), largest 25.2 Mb. That is a direct confirmation of their range, in numbers, and it is not cited in section 11.

**Fix.**
- Reword the "bp per event is 10" sentence as "the 10x ratio used in A3x".
- Label which of the "informal figures" are the critics' and which are the audit's.
- Add one line: "McCarthy's 'hundreds, thousands, or even millions' is confirmed by the measured size spectrum (71 events over 1 Mb; 359 at 100 kb-1 Mb; 1,905 at 10-100 kb; 20,928 at 1-10 kb)."

### 12. MINOR. Critic arguments the check should cite, and a point to credit in the scorecard

**Locator.** Note sections 2 and 11. Sources above.

**Argument.**
- *Fun-Friendship4898, centromere and acrocentric composition.* Comment pdebkr5 (A3x): "over half of these human SDRs are classified as centromere and acrocentric." The note's own 85% overlap of unaligned human bp with centromere models (P5) is the same finding from an independent route, and is not tied back to the Reddit comment. It deserves a credit line, since it is the second independent confirmation of that critic.
- *Hancock's suspicion.* GG-10 "the number is 205 million differences, right?" (note: "Hancock suspects 205M includes gap divergences and is not a point-mutation count"). The check confirms the suspicion in the sense that 205 M cannot be a count of point mutations.
- *Pre-registration credit.* The "favours critics" criteria stated in advance were met, the "favours Day" criteria were not, and P1, P3, P5 (L2), P6 (indels) were missed in the open. For a two-sided audit that is the pattern that earns trust. The scorecard could say in one line that the misses were not one-directional: SNV count (+8% over the band) and the L3 bp are Day-neutral, the indel total was 16% under the point, and fragmentation is Day-favouring.

**Fix.** Add the two credit lines to section 11 and the one-line direction summary to section 2.

---

## Summary of fixes

| # | Tag | Fix |
|---|---|---|
| 1 | MAJOR | Replace the single 9.7x with a ratio table (raw 9.7, human lineage 10.3, <2% 10.8, fixed 11.3-12.5, both 12.5-13.8; non-additive). Carry to section 13. |
| 2 | MAJOR | Strike "SNV-only is a floor". With polymorphism removed, fixed events per lineage (16.4-18.1 M) bracket Day's 17.5 M. |
| 3 | MAJOR | Relabel 261-523 M as "bases in non-1:1 / unaligned regions", add a "bases that differ" row, report identity of nested fills and the SNV overlap, drop "Yoo reproduced". |
| 4 | MAJOR | Retitle the "Day, not conceded" section; remove credits for facts the critics stated first (MC-11, RE-05). |
| 5 | MAJOR | Correct "rate-based 9-11x" (k = mu route is about 20x, and undershoots by about 2x); add the critic-number scoreboard. |
| 6 | MAJOR | Record that no critic made the per-species reading; retire 22.5 M; note offsetting SNV (+8%) and indel (-14%) errors; fix the 1,140-inversion scope slip; point to RF-6, MF-03, PS-01. |
| 7 | MINOR | Measure polymorphism with population frequencies; explain why pre-split sites are not post-split fixations. |
| 8 | MINOR | Add gap-merge and MNV-merged sensitivities; note both-sided gaps move events 0.1% and carry about half the clean gap bp. |
| 9 | MINOR | Add the three-line scoping table (unit / type / rate) and do not multiply. |
| 10 | MINOR | Add a base rate for the 410.09 coincidence; cross-reference A3a's 412.1. |
| 11 | MINOR | Fix the attribution of "bp per event is 10" and of the "informal figures"; cite the measured size spectrum against MC-11 and Neukamm. |
| 12 | MINOR | Add credit lines (FF4898 centromere composition, Hancock GG-10) and a one-line direction summary of the missed predictions. |

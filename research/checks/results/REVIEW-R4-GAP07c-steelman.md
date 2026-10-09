# Combined steelman review of R4 GAP-07c (Day side, then critic side)

Reviewer role: argue each side as strongly as honestly possible, then judge whether the note is balanced. Per AGENTS.md rule 1 this check gets a Day-side and a critic-side review; they are combined here because GAP-07c is a small follow-on to GAP-07b, which already had three full reviews. Finding ids: `GD-1..GD-6` (Day side), `GC-1..GC-6` (critic side).

Reviewed: `research/checks/results/R4-GAP07c.md` (cited as "note", with line numbers); `research/checks/gap07c_polymorphic_share.py` (docstring only: definitions, Q0-Q10, "WHAT WOULD FAVOUR"); `R4-GAP07b-alignment.md` §0 and §14; `raw/gap07c_report.out` and `raw/gap07c_report_nygc_chr21_22.out`; claims `A3c`, `A3x`, `A3b`, `A3a` (grep); `quotes-day.md` Q37, Q55, Q100; `quotes-critics.md` CA-04, PS-03. Reviewer arithmetic is marked `derived:` (python3 -I, from the note's own rows; linear interpolation between the note's (b) threshold rows, so approximate). Nothing was run on the data and no other file was edited.

## Overall judgement (short)

The check is careful, pre-registered, discloses its misses (Q5, point misses inside bands) and states its main limit (no chimp data) in the second paragraph. I could not construct a Day-side adjustment that moves the ratio outside 10.6-12.6, and I could not construct a critic-side one that moves it above about 13. Both sides' strongest points are real but small (a few tenths of a ratio unit). The weaknesses are of framing and credit, not arithmetic:

- Three items are credited to Day more strongly than the data allow (the "within 2%" match, SV "supports", indels placed on "Day's side").
- Two items are credited to the critics more strongly than the data allow (the CSAC range "confirmed", and the symmetric central row presented as one number).
- The threshold sensitivity is shown on one side only, and the most assumption-light number (the human lineage alone) sits in §5 and not in the headline.

Counts: Day side 1 MAJOR, 5 MINOR. Critic side 4 MAJOR, 2 MINOR.

---

# PART 1. DAY SIDE

## Strongest honest case for Day

1. The measured polymorphic share is a correction of 10-18% to an event count, not a refutation. 84.4% of human-derived divergent SNVs have the chimp-matching allele below 1% in humans. The ratio moves from 9.74 to 11.5 and stays at 11-12 on every treatment. Nesslig20's "not all of the differences ... are actually fixed" is true and small.
2. The one pre-registered prediction that could have gone against Day on structure went his way. He said SV is "post-divergence" (Q100); the note predicted a lower SV share than SNV (Q8, point 4%, band <= 10%) and found 1.7% against 15.6%.
3. His SNV-only 17.5 M is within 2% of the total measured fixed events, so his lower-bracket "floor" is about the right size for a total.
4. The chimp-side number is an assumption, and the note says so. The data-only version (a) gives 10.64.
5. His stated position (04-28 ¶24-25, Q37) already treats ancestral polymorphism: sorted ancestral variants still need to fix.

Where this case runs out: the polymorphic share itself (15.6%), its stability across populations (NYGC 16.06% vs phase 3 16.11%) and the unit mismatch (about 10x) are not moved by any Day-side argument I could find.

## MAJOR

### GD-1. MAJOR. The chimp-side assumption is fair in direction as far as anyone can tell, but it is presented as "central" without an interval, and its one-line justification is unchecked and one-directional

**Locators and verbatim.**
- Note line 11: "**The chimp lineage is NOT measured.** No chimpanzee population data were used. The "symmetric" treatment assumes the chimp lineage has the same polymorphic share as the human lineage. This is an assumption and the corrected ratio depends on it."
- Note line 120 ("Neither"): "chimp diversity is commonly reported to be higher than human (not checked here; a reason for (c), not a measurement)."
- Note line 124: "A chimp panel on panTro6 would settle (a) vs (b) vs (c)."
- Note line 23 (bottom line): "Under the symmetric reading the ratio rises from 9.7 to about 11.5 (range 10.6-12.6 over the treatments, 11.2-11.7 over thresholds)."

**Argument for Day.**
- The note gives the critic direction one unchecked sentence of support ("commonly reported higher") and nothing on the other direction.
- The comparison is not like for like. The human panel is global (1000 Genomes, 26 populations), so "polymorphic in humans" is a species-wide standard. panTro6 is, as far as I know, one individual of a single chimpanzee subspecies (this is from memory and must be checked against the assembly record before it is used). A matching chimp standard is either "polymorphic in the species" (four deeply structured subspecies; this raises the chimp share toward (c)) or "polymorphic in the reference individual's subspecies" (lower diversity than the species total; this lowers it toward (a)). The note does not say which standard (b) assumes. The direction of the true chimp share is therefore not established, and (c) "chimp share 2x human" has no more support than a 0.5x row.
- (b) is nearly the arithmetic midpoint of (a) 10.64 and (c) 12.58 (midpoint 11.61, `derived:`), which makes it a fair central, but only if (c) is a legitimate upper edge. The note calls (c) "arbitrary" in the table and uses it to set the top of the headline range.

**Argument against (honesty).**
- The data-based floor (a) is only 0.8 below (b), and nothing in the note says the chimp share is below the human share. A reader who treats (b) as Day-unfair would be wrong. The assumption is probably neutral to mildly Day-favourable if (c) is the truth.
- The measured chimp-derived share on the human panel (1.0%) is a lower bound only because the human panel cannot see chimp variation. It is not evidence of a low chimp share.

**Fix.**
- In the headline table and bottom line, state the result as "10.6 (human data only) to 12.6 (chimp share 2x human), 11.5 if the chimp share equals the human one; none of the chimp rows is measured".
- Replace "commonly reported to be higher than human" by either a cited, checked number (de Manuel 2016 / Great Ape Genome Project per-subspecies diversity; check against the subspecies of the panTro6 individual) or "direction unknown; depends on whether the standard is species-wide or subspecies-wide".
- Add a 0.5x row beside (c) so the sensitivity is two-sided.

## MINOR

### GD-2. MINOR. The ratio corrects the denominator for polymorphism but not Day's own SNV component in the numerator

**Locator.** Note §5 "Corrected ratio": ratios are 205 M / fixed events. Day's 205 M per lineage is, by the construction the critics identified (A3x, Fun-Friendship4898: "multiplying 187Mb by 2, then adding the 35 million SNVs"), 410 M halved, i.e. 17.5 M SNV plus 187 M structural bp (the 1,140 inversions are negligible).

**Argument.** If 15.6% of SNV differences are not fixed, the same 15.6% applies to the 17.5 M SNV part of his own count. `derived:` 17.5 M x 0.156 = 2.73 M; (205 - 2.73) / 17.88 = 11.31 against 11.47. The SV part is bp-weighted and its measured polymorphic share is 0-1.7%, so the correction there is at most about 3 M of 187 M. This is a small effect (about 0.16 in ratio, or 1.4%). It matters only because the note's bottom line says the ratio "rises" from 9.7 to 11.5; part of that rise is one-sided.

**Fix.** One sentence in §5: "applying the same SNV share to the SNV part of the 205 M numerator gives 11.3; the numerator's bp-weighted SV part has no measured correction."

### GD-3. MINOR. The 1% threshold is pre-registered and defensible, but the sensitivity table is one-sided and the band labels are easy to misread

**Locators.**
- Note line 67: "Thresholds on s_H: 0.1% 17.3%; 0.5% 16.2%; 1% 15.6%; 2% 14.9%; 5% 13.7%; 10% 12.6%."
- Note line 19 (table): ratio rows only for "AF >= 0.1% / >= 5%".
- Day, `quotes-day.md` Q55 (B2026-01-14-empirically-impossible, ¶5): "Not a single allele in 1.2 million crossed from rare (<10% frequency) to fixed (>90% frequency) in seven thousand years."
- Note §3 bands table: columns give the frequency of the **chimp-matching (ancestral)** allele in humans.

**Argument for Day.**
- Day's own operational rule for "fixed" in the aDNA work is above 90%. At the 10% threshold the human-lineage share is 12.6%. `derived:` the (b) fixed events rise from 17.88 M to about 18.45 M and the ratio falls to about 11.1.
- A derived allele at 90-99% in humans (3.0% of human-derived sites) has done almost all of its fixation work. Counting it as "not fixed" at 1% is strict.
- Using the all-sites share (14.86%) instead of in-mask (15.59%) lowers the ratio by about 0.1 (about 11.4); the note chose in-mask on the argument that outside the mask polymorphism is under-called.

**Against.**
- By the note's own bands, 10.8% of human-derived sites have the derived (hg38) allele at 10-90% in humans (5.6% + 5.2%). Those are plainly unfixed. The threshold lever is worth about 0.4 in ratio, not more.
- A reader who reads the §3 bands as "frequency of the derived allele" would invert them: "[50%, 90%)" means the derived allele is the **minority** allele.

**Fix.** Add the 10% ratio (about 11.1, hand-derived) and the "seen at all" ratio (see GC-1) so thresholds are shown at both ends; relabel the band columns "chimp-matching (ancestral) allele" and add a derived-allele row.

### GD-4. MINOR. Day's wins are all present, but the 84%-fixed complement and the SV result are placed after the critic-favourable framing

**Locators.**
- Note line 9: "**15.6%** ... still have the chimp-matching allele at 1% or more in the 1000 Genomes phase-3 panel, so they are not fixed in humans." The 84.4% fixed complement appears first in §6 (line 111).
- Note line 23: "The CSAC range (14-22%) is confirmed for the human lineage at AF >= 1%, at the low end (15.6%)."
- Note line 70: "the measurement supports its human half and is compatible with it as a total only through the symmetric assumption."

**Argument.**
- The three wins named in the brief are in the bottom line: the 84% complement (as "15.6% ... at the low end"), indels and SVs less polymorphic, and the 17.5 M match. None is hidden.
- "Confirmed" is stronger than §3 supports. CSAC's 14-22% is a both-species rate, and the note itself says the measurement is compatible with it "as a total only through the symmetric assumption". "Consistent with the human half of CSAC's range" is the accurate phrase.
- The Q1 point prediction (15%) was on target; the note says "held" but the lead does not say that the sceptical-of-Day estimate hit its point and not merely its band.

**Fix.** "Confirmed" becomes "consistent with"; the §0 headline gets "84.4% fixed (AF < 1%)" beside 15.6%.

### GD-5. MINOR. The "(a) Day-favourable bound" row mixes two bases

**Locator.** Note line 16 table: "(a) human data only: pooled share, chimp lineage credited with no polymorphism of its own (Day-favourable bound) | 8.2% | 19.27 M | 10.64". `raw/gap07c_report.out`: "(a) human data only, SNV pooled in-mask share; indel share = measured".

**Argument.** The SNV share in (a) is the pooled one (8.25%), but the indel share is the human-lineage one (10.6%). The pooled all-events indel share in the same output is 5.3% in mask (`raw/gap07c_report.out`, "all events"). Using the pooled indel share for consistency: `derived:` 19.27 + (0.106 - 0.0528) x 2.15 = 19.38 M, ratio 10.58. The effect is 0.06; it matters only because (a) is labelled the Day-favourable bound and should be the lowest row.

**Fix.** Put the pooled indel row in the table, or relabel (a) "human data only (indel share from the human lineage)".

### GD-6. MINOR. Scope of what the 15.6% tests: the part of the polymorphism objection that Day addressed is outside it, and A3c's "Against: none" is stale

**Locators.**
- A3c "Responses": "Against: none in the Day corpus addresses polymorphism in the 35M count (the 2025 and 3.0 papers use 35M as required fixations)."
- Day, `quotes-day.md` Q37 (Z22903977, p.3): "Under coalescent theory, the expected pairwise divergence contributed by ancestral polymorphism is θ = 4Nₑμ per site."
- Day, 04-28 (`B2026-04-28-less-than-zero-3`, ¶22-24 of the extracted text; the note cites ¶24): "Their inflated ILS figure does not rescue anything. It simply distributes the fixation requirement across both lineages instead of consolidating it on one."
- Note line 71: "Ancestral polymorphism that sorted (reciprocal fixation after the split) is not polymorphic now and stays in the fixed count, as Day argues (04-28 para 24)."

**Argument.** The 15.6% measures one thing: differences that still segregate in humans today. Day's reply to the ancestral-variation objection is about a different set: variants that were polymorphic before the split and have since sorted. Those are fixed now, are counted as fixed here, and are what Camestros' CA-04 targets (see GC-5). The measurement is silent on how many of the ~18 M fixed differences are sorted old variants. The note says the sorted part "stays in the fixed count", which is right and credits Day; but A3c's "Against: none" and the suggested A3c line (note line 145) do not reflect that Day addressed the objection (Q37, 04-28).

**Fix.** At integration, replace A3c's "Against: none ..." with a line citing Q37 and 04-28 ¶24, and add to the suggested A3c text: "does not measure sorted ancestral polymorphism".

---

# PART 2. CRITIC SIDE

## Strongest honest case for the critics

1. The CSAC estimate (14-22%, 2005, one genome each) was measured directly on a large modern panel and landed at 15.6% (14.8-16.7% across chromosomes; NYGC 16.06% against 16.11%). Nesslig20 (PS-03) was right, and the size that CSAC gave was right.
2. Every limitation of the method points the same way for the human lineage: sites absent from the VCF, a 1% cut-off, a panel of 2,548 people, biallelic-only phase 3, short-read indel and SV calling, X and Y excluded. The 15.6% is a floor on human-lineage non-fixation under the note's own caveat 4 ("No threshold gives "polymorphic in the species" for the whole of humanity"), and the 1.7% SV and 9.5% indel shares are lower bounds.
3. The most assumption-light number is the human lineage alone, which is also Day's own lineage ("205 million required fixations" on the human lineage). That number (about 11.9, hand-derived in §5) is above the headline 11.5 and needs no chimp assumption.
4. The headline "within 2%" match compares an SNV-only number with an all-events number. Like for like, Day's SNV-only 17.5 M is about 10% above the measured fixed SNVs per lineage (15.94 M).

Where this case runs out: it does not close the 10x unit gap, and it does not support any ratio above about 13 on the numbers in hand. The note says this ("Neither" section), correctly.

## MAJOR

### GC-1. MAJOR. Sites absent from the VCF are counted fixed; the "1% panel" definition understates polymorphism by a stated but un-carried-through amount, and the cross-check is not an independent sample of people

**Locators and verbatim.**
- Note line 126: "Sites outside the VCF count as fixed."
- Note line 9: "The same figure from the independent NYGC 30x panel on chr21+22 is 16.06% against 16.11% from phase 3 on the same chromosomes."
- Note line 127: "No threshold gives "polymorphic in the species" for the whole of humanity."
- Note line 67: "Seen at all: 20.0%."
- Note line 48 (scorecard), Q5: pre-registered "adding "seen at all" raises s_H by <= 3 points"; observed "**+4.4 points** (20.0% seen vs 15.6%)"; verdict **missed**.
- `raw/gap07c_report.out`: "H-derived, in mask ... poly(>=.01)= 15.59% >=.001= 17.33% ... seen= 20.01%"; bands: "H-derived, in mask 79.99% 2.68% 1.74% 3.02% 5.64% 5.15% 1.34% 0.44%" ("not seen" 79.99%).

**Argument for the critics.**
- 80% of human-derived divergent sites have the chimp allele "not seen" in 5,096 chromosomes, and all of those are counted fixed. The share rises from 15.6% (1%) to 17.3% (0.1%) to 20.0% (seen at all) as the panel is read more sensitively. That is a gradient with sample size, and 1000 Genomes is a small, geographically uneven sample (no Oceanian or hunter-gatherer coverage to speak of, few Africans relative to Africa's diversity). A larger panel (gnomAD, HGDP) would sit further up the gradient.
- The note's own scorecard shows the author under-predicted this gradient (Q5 missed by 1.4 points beyond the allowed 3).
- The "independent" NYGC panel is the same cohort (the 1000 Genomes samples re-sequenced at 30x, plus relatives). It validates the calling (low-coverage vs 30x), not the sampling of people. Calling the check "independent" overstates what it shows about resource choice.
- The ratio table carries the 0.1% row (11.68) but not the "seen at all" row. `derived:` at 20.0% (SNV) with the indel share held at 10.6%, fixed events fall to about 17.04 M and the ratio rises to about 12.0. A reader sees "11.2-11.7 over thresholds" and not that the same data support 12.0 at the other end.

**Against (honesty, for Day).**
- At AF >= 1% the miss is small. The NYGC 30x file agrees with the 7x phase-3 file to 0.05 points, and it splits multi-allelics. "Not seen at all" includes recurrent CpG back-mutation and sequencing noise, which are not "unfixed ancestral polymorphism". The 1% choice is pre-registered.
- Even 12.0 is within the "10-13 expected under every outcome" statement in the script docstring.

**Fix.**
- Add ratio rows for "seen at all" (about 12.0, hand-derived) and for the 10% threshold (about 11.1) so the sensitivity is two-sided; state the headline as a threshold range (11.1-12.0).
- Replace "independent NYGC 30x panel" by "the same cohort sequenced at 30x (tests calling, not sampling)".
- Proposed follow-up (not required for this note): a larger and more diverse panel on one small chromosome (for example a gnomAD or HGDP+1KG sites file for chr21; file size and availability to be checked before use) to test whether the 1% share moves with sample size.

### GC-2. MAJOR. The short-read indel and SV sets undercount polymorphism; the note says "lower bound" but the bottom line still scores it as support for Day, and the size trend does not discriminate between Day's reading and detection decay

**Locators and verbatim.**
- Note line 23: "Indels and SVs are less polymorphic than SNVs (human-lineage indels 9.5%, SVs at or above 50 bp about 1.7%), which supports Day's "post-divergence" remark for SVs".
- Note line 88: "The sample is two chromosomes, the SV call set is from short reads, and non-matches in repeat-rich sequence (where most gap bp lie) count as "fixed". So 1.7% is a lower bound, not a measurement of fixation."
- Note line 89: "The 1,000 Genomes indel and SV matching compares net length and position, not sequence. Matches inside tandem repeats may pair different events."
- Note line 126 (caveat 3): "Multi-allelic sites are absent from phase 3 ... Short-read calls under-represent repeats and SVs, so shares outside the mask ... and for SVs are lower bounds."
- Note line 84 table: SV >= 50 bp, NYGC chr21+22: n = 4,623, "1.7% / 2.7% / 1.6% / 0.5%"; phase 3 on the same chromosomes: "0.03% / 0%".
- Day, Q100 (`B2026-04-28-less-than-zero-3`, ¶25): "ILS cannot sort what was never segregating. Structural variation is, with very few exceptions, post-divergence".
- Scorecard line 51: "indel point missed high, SV point missed low".

**Argument for the critics.**
- The matching rule needs the same net length, a record in a biallelic file, and a call from short reads. It therefore misses polymorphic events in tandem repeats, multi-allelic STRs, and repeat-embedded SVs, where most large gap bp lie. The null control (0.01-0.08%, 0.05% for SVs) addresses false matches only; no control addresses false non-matches.
- The decline with size (human-lineage indels 11.7% / 7.9% / 6.0% for 1 / 2-10 / 11-50 bp, SVs 1.7%, phase 3 about 0 above 50 bp) is what short-read detection sensitivity does with size, independent of anything else. It is also what purifying selection does to the frequency of large indels in the population. Neither is a test of "post-divergence".
- Day's claim is about the ancestor ("what was never segregating"). A panel of today's humans cannot test it: an ancestral SV that sorted looks fixed here, exactly as a post-divergence one does. Even a true 0% would be consistent with Day and with the critics. The note's wording "supports" is an overstatement; "is consistent with" is the accurate phrase.
- The sample is 4,623 events on chr21 and chr22 (about 4% of the ~104 k autosomal events above 50 bp in `raw/gap07c_report.out`), including the acrocentric p-arms.
- The scorecard places the indel result "on Day's side". The pre-registered Day criterion was "near-zero indel/SV shares" (docstring "WHAT WOULD FAVOUR DAY"); 9.5-10.6% is not near zero and is 61-68% of the SNV share (40% of human-lineage in-mask indels are 1 bp, where the share is 11.7%, close to SNV). Only the SV share meets the criterion.

**Against (honesty, for Day).**
- The note is already candid ("lower bound, not a measurement of fixation"), and the arithmetic effect on the ratio is tiny: applying the SNV share to all events moves the ratio only from 11.47 to 11.54 (`raw/gap07c_report.out`, "(b) symmetric, SNV share also applied to indels"). The issue is credit and wording, not the number.
- A drop from 15.6% to 1.7% is a ten-fold difference that the pre-registration expected; it is a real, if weak, point for Day.

**Fix.**
- Bottom line: "which supports Day's "post-divergence" remark for SVs" becomes "which is consistent with Day's remark (a lower bound from short reads; it cannot test an ancestral-segregation claim, because sorted variants look fixed)".
- Scoring paragraph (line 55): "indel and SV shares sit on Day's side" becomes "the SV share meets the near-zero criterion; the indel share is intermediate (9.5% against 15.6%)".
- Follow-up that would settle it: match the same chain-gap events against a long-read SV call set in GRCh38 coordinates (HGSVC2 or the 1000 Genomes ONT set; existence and file sizes to be checked before use), and compare with the short-read share on the same events.

### GC-3. MAJOR. The central ratio is the symmetric pooled row; the human-lineage number, which needs no chimp assumption and is Day's own lineage, is higher and is not in the headline; the quoted range omits the combined critic rows

**Locators and verbatim.**
- Note §5 table, last row: "human lineage alone, with measured shares | 10.11 (raw) | about 11.9 [PH, by hand: 15.52 M + 1.68 M fixed]".
- Note §5: "top-level fills only, with the CSAC share | not given | **12.27** [PH]".
- Note line 23: "(range 10.6-12.6 over the treatments, 11.2-11.7 over thresholds)".
- R4-GAP07b §0 bracket: "<2% records and fixed share on SNVs (not additive) | ... | 16.69 / 15.34 M | 12.29 / 13.37" and "Bracket: about 7 to 14".
- Day, Q102 (`quotes-day.md`): "Total: about 205 million" described by the audit as the per-lineage half; A3a: "Apportioned symmetrically to the human lineage this yields approximately 205 million required fixations."

**Argument for the critics.**
- Day states his requirement for the human lineage. The only lineage this check measures is the human one. The human-lineage ratio (`derived:` 205 / (15.52 + 1.68) = 11.92) is therefore the number most directly about Day's claim, and the headline (11.47) is a pooled convention plus an assumption.
- The quoted "range 10.6-12.6" is the range over polymorphism treatments only. The rows that raise it (11.9, 12.27) are in §5 and tagged post hoc. GAP-07b's combined critic rows (12.3-13.4, with CSAC's share) were not re-run with measured shares (hand-scaled, the measured counterpart is about 12.5, `derived:` by interpolating GAP-07b's 0.86/0.78 rows to the measured 0.844). A reader of GAP-07c alone would take 10.6-12.6 as the full critic-favourable range.
- (b) rests on an assumption yet carries the label "central"; the human-lineage row rests on measurement.

**Against (honesty, for Day).**
- The human-lineage indel count is skewed by polarization (1.16 M human against 2.35 M chimp events, note caveat 8: "human share skewed as run"), so the hand-derived 11.9 depends on a figure the note itself calls skewed. The pooled symmetric row is steadier on indels. Neither row is clean, which is why both belong in the headline.
- The Day-favourable rows of GAP-07b (repeat-unit 7.2-9.5, slippage x2-x3) should also be re-expressed with polymorphism, which raises them by about 1.18 (21.05 / 17.88), for example 8.35 to about 9.8 (`derived:`). The updated bracket is neither "10.6-12.6" nor GAP-07b's "7-14".

**Fix.** Add a short table to §0 or §5 parallel to GAP-07b's bracket: raw 9.74; human data only 10.6; symmetric 11.5; human lineage alone about 11.9 [PH]; top-level 12.3 [PH]; chimp 2x 12.6; and the GAP-07b Day-favourable rows re-expressed with polymorphism. Label which rows rest on the chimp assumption (b, c) and which do not (a, human lineage).

### GC-4. MAJOR. "Within 2%" compares an SNV-only number with an all-events number; like for like it is about 10% above, and the shortfall statement holds only in the all-events basket

**Locators and verbatim.**
- Note line 23: "Day's SNV-only 17.5 M per lineage is within 2% of the symmetric measured fixed events (17.88 M)."
- Note line 102: "This is a near-coincidence of two offsetting errors (omitted indels, included polymorphism), as GAP-07b already said, now measured. With SNV only fixed events are 15.94 M."
- Note line 114: "His SNV-only 17.5 M per lineage is within 2% of the measured fixed events; its shortfall is not reduced by the correction (shortfall about 93,800 at the MITTENS rate, by proportion from GAP-07b)."
- Note line 101: "the GAP-07b shortfall of 91,800 on 17.5 M scales to about 93,800 on 17.88 M".

**Argument for the critics.**
- The 17.88 M includes about 1.9 M fixed indel events that Day's SNV-only number leaves out. The like-for-like comparison is SNV-only against SNV-only: 17.5 M against 15.94 M (`derived:` 37.77 M x (1 - 0.1559) / 2 = 15.94 M), so Day's SNV-only requirement is 9.8% **above** the measured fixed SNV count per lineage.
- On his own SNV-only variant (s7.3), the polymorphism correction does reduce the requirement. `derived:` the shortfall scaled to 15.94 M is 91,800 x 15.94 / 17.5 = about 83,600, a 9% reduction. The statement "its shortfall is not reduced by the correction" is true only if the indels are added back (93,800); it is the number for a different basket.
- The note does say the match is a coincidence of offsetting errors (line 102), but the same fact appears in the bottom line and in Day's credit as a flat "within 2%", and the SNV-only shortfall line sits inside the "Day" credit section.

**Against (honesty, for Day).**
- Day's SNV-only was meant as a floor. An SNV-only figure that happens to be close to the total fixed events is a fair way to describe "the omitted indels roughly cancel the polymorphism". The offsetting-errors sentence is in the note, as is "With SNV only fixed events are 15.94 M".
- The change in the shortfall is 9%, nowhere near an order of magnitude.

**Fix.**
- Bottom line: add "like for like, SNV-only 17.5 M against 15.94 M measured fixed SNVs (+9.8%); the close match to 17.88 M is two offsetting errors".
- Line 114: split into the two bases: "shortfall about 93,800 on all fixed events, about 83,600 on SNV-only (derived by proportion)".

## MINOR

### GC-5. MINOR. Critic credits are stated, but without verbatim quotes or locators, and CA-04 is credited for something the measurement does not test

**Locators and verbatim.**
- Note line 107: "Nesslig20 (PS-03) and Camestros (CA-04) were right that the reference-genome differences include differences that are not fixed in the human population."
- PS-03 (`quotes-critics.md`, post 1 by Nesslig20, branch A3x): "since they use one (or a few) reference genomes, not all of the differences they identified between genomes are actually fixed in either the human or chimp populations."
- CA-04 (`quotes-critics.md`, para 46, Camestros): "So Day is treating ALL the genetic differences between chimps and humans as mutations that initially only occurred after the point of divergence of the two species."

**Argument.**
- PS-03 is the claim the measurement supports (differences that are not fixed now). CA-04 is a claim about origin: a difference can have arisen before the split as ancestral variation and have sorted since. A sorted ancestral variant is fixed now, is counted as fixed in this check, and the check says nothing about how many such variants there are. The credit to CA-04 is therefore not supported by this measurement. It is the point Day addressed with "distributes the fixation requirement" (GD-6), and which remains open (a mutation-supply question for A5, not a fixation count).
- Credits are present for both critics, for the GAP-07b critic rows ("about right") and for CSAC's range. But the note quotes neither critic.

**Fix.** Line 107: credit PS-03 for the measured point, with its quote and locator; credit CA-04 for raising ancestral variation, state that this check does not measure it, and leave the verdict on that open.

### GC-6. MINOR. Panel and chromosome coverage: the central share is applied to X and Y without a measurement

**Locator.** Note line 30: "Phase 3 has no chrY, and its chrX has only 107 k records, so **chrX and chrY are excluded from the shares**; the autosomal shares are applied to all 37.77 M SNVs (X is 4% and Y 2% of the sites)." Caveat 2 (line 125).

**Argument.**
- Applying the autosomal 15.6% to 6% of the sites is a standard imputation. For chrX it probably overstates polymorphism (lower diversity on X); for chrY there is none to measure. On the critic side the effect is under 0.1 in ratio; the note says both exclusions. I flag it only because the note's range statements ("11.2-11.7 over thresholds") do not carry it.

**Fix.** One line in caveat 2: "effect on the ratio below 0.1 in either direction (reviewer estimate)". No further work.

---

# PART 3. IS THE NOTE BALANCED?

**Verdict: broadly balanced, with no blocking problems; seven wording and presentation fixes make it so.** The balance is better than average for this project:

- The pre-registration is honest in both directions. It gave explicit "favours Day" and "favours critics" criteria in the docstring. The outcome is reported as split: SNV share on the critics' side, SV share on Day's side.
- Misses are disclosed (Q5, the indel point, the SV point, the (c) point).
- The data-only floor (a) and the assumption-based (b)/(c) are shown side by side.
- The Day and critic credit blocks (§6) are of similar length and specific.
- The "Neither" block states the three things the check does not do: it does not move the unit result, does not test selection, and has no chimp data.

Where the weights are slightly off, by direction:

| item | favours | finding |
|---|---|---|
| "within 2%" and "shortfall not reduced" (mixed baskets) | Day | GC-4 |
| SV "supports Day's post-divergence remark" (lower bound; cannot test ancestral segregation) | Day | GC-2 |
| indel share scored as "on Day's side" against a "near-zero" criterion | Day | GC-2 |
| ratio numerator not corrected for polymorphism | critics | GD-2 |
| CSAC range "confirmed" (both-species rate vs a human-half measurement) | critics | GD-4 |
| symmetric (b) labelled central, with a one-sided unchecked justification | critics | GD-1 |
| thresholds shown only to 0.1% and 5%, not 10% or "seen" | neither (incomplete) | GD-3, GC-1 |
| human-lineage ratio (no chimp assumption) kept out of the headline | Day (hides the higher figure) | GC-3 |
| CA-04 credited for a point this check does not measure | critics | GC-5 |

Net: three over-credits to Day, three to the critics, and the incomplete rows. They roughly offset, and none changes the conclusion that the polymorphism correction is a 10-20% adjustment and the unit mismatch is the 10x. The order the note presents things in (critic-favourable confirmation in the lead, Day's wins in the bottom line) is acceptable because all three of Day's wins are named there.

## Recommended edits, in order of value

1. Headline table or §5: one bracket table with and without the chimp assumption, including the human-lineage row and the two-sided thresholds (GD-1, GD-3, GC-1, GC-3).
2. Bottom line: replace "confirmed" and "supports" by "consistent with"; add the like-for-like SNV-only comparison (GD-4, GC-2, GC-4).
3. Scorecard paragraph: indel is intermediate, SV meets the criterion (GC-2).
4. "independent NYGC panel" becomes "same cohort at 30x" (GC-1).
5. Credits with quotes and locators; CA-04 scoped (GC-5, GD-6).
6. At integration: A3c "Against: none" replaced by Q37 and 04-28 ¶24 (GD-6).
7. Optional follow-ups: a long-read SV set on the same events (GC-2); a larger or more diverse panel on one chromosome (GC-1); a chimp panel (GD-1).

## Credits (this review)

- Day side: the 10% operational threshold (Q55), the numerator-correction symmetry (GD-2), the (a)-row inconsistency, and the stale A3c "Against: none".
- Critic side: the like-for-like SNV-only comparison, the same-cohort point about the NYGC cross-check, the human-lineage row, and the CA-04 mismatch.
- Both: the size of the effect of each is small, and I list it next to each finding.

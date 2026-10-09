---
id: A3x
title: "The 205M requirement counts base pairs in structural variants as if each were a separate fixation event"
side: critic
branch: A
parent: A3
edges: [{type: attacks, target: A3a}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds   # 410e6/40e6 = 10.25; unit argument
  fidelity: partial   # the critics' unit reading matches Day's 2nd-edition wording ('410 million base pairs') but not his stated weighting rationale (Q99, Q101-Q103); the formal statement added Yoo's six-ape count of 1,140 inversions to a human-chimp total (the hg38-panTro6 net has 453 nested inversion fills >= 10 kb; R4 GAP-07b)
  external: supported   # R4 GAP-07b direct count (hg38 vs panTro6, non-T2T; both lineages plus polymorphism): 42.1M events, 21.05M per lineage; 205M is 9.7x raw, bracket ~7-14x (Day-favourable 7.2-9.5, critic-favourable 10.1-13.4, post hoc); the 40M +/- 30% prediction is met on the available alignment, not on Yoo's T2T data; a base-pair numerator against G_f's events is a unit mismatch; R4 GAP-07c: on fixed events 205M is 10.6-12.6x (human lineage alone 11.9; 11.1-12.1 across allele-frequency thresholds); combined with GAP-07b the bracket is about 8-13x
---

## Statement (verbatim)
> The 410 million base pair difference refers to structural variation, which includes duplications, insertions, etc., in which a single mutational event can cause hundreds, thousands, or even millions of base-pair differences.

Source: [Dennis McCarthy, Vox Day Responds](https://dennismccarthy.substack.com/p/vox-day-responds), 2026-09-17, para 26 (MC-11).

> bases affected by a rearrangement are not separate mutation events: one structural change can affect millions of bases.

Source: [r/DebateEvolution, Dumb-and-Dumber](https://www.reddit.com/r/DebateEvolution/comments/1wss2wj/), 2026-09-28 (RE-05).

## Formal statement
Claim: fixations are events; R_events = (SNV + indel events + inversions + other SV events)/2 ≈ 20M per lineage, not 205M.

`derived:` (python3 -I) 35e6 SNV + 5e6 indel events (CSAC) + 1,140 inversions = 40.0e6 events; /2 = 20.0e6. (R4 GAP-07b: 1,140 is Yoo's six-ape curated inversion count, not a human-chimp count; the hg38-panTro6 net has 453 nested inversion fills >= 10 kb; effect on the 40M: none.) 410e6/40.0e6 = 10.25; 410e6/35e6 = 11.7. Day's own wording in the 2nd edition is "410 million base pairs" (A3a), i.e. the critics' reading of the unit matches Day's text.
Related critic statements: Hancock (GG-10) "the number is 205 million differences, right?" and GG-11 (his "something like 407" = 205e6/(2 x 252,000) = 406.7 mutations per generation over both lineages, an accounting choice); Nesslig20 (PS-03) reference genome differences vs fixed; Mansfield (MF-06) "around 25 million give or take, not 200 million" (uncited).

## Assumptions
- Stated: one mutational event can affect many bases.
- Implicit: a structural change fixes as a single event with probability comparable to a point mutation (not required for the logic here, which is about counting units).

## Responses
- Against (Day): s7.3 concedes the concern and runs the SNV-only variant (A3b). Day's stated rationale (R4 GAP-07b; Q99, Q101-Q103) is a weighting claim with a range, not an assertion that 205M events occurred: 04-28 ¶19, "A 50,000 base pair insertion or a chromosomal inversion requires the entire structural rearrangement to occur as a single low-probability event and then to fix. Counting these by base pair, as the gap-divergence figure does, is generous to the standard model."; 05-13 ¶6, "Discount every structural variant in the Yoo data to zero. Count nothing but single-nucleotide variants. ... The conclusion holds either way." SNV-only is his lower bracket and bp his upper. As a weight, 205M needs ~3,250 SNV-equivalents per event above 50 bp (R4 GAP-07b); no measurement of such a weight exists in the corpus. R4 GAP-07: the s7.3 wording (SVs "should not each count as a single fixation event in the same sense as a point mutation") does not settle whether Day regards bp counts as wrong, and the 3.0 abstract keeps 205M; the decisive point is that G_f counts events.
- In support (R4 GAP-07 credits, verified in `sources/raw/critics`): Fun-Friendship4898 (Reddit [1wv4zeg](https://www.reddit.com/r/DebateEvolution/comments/1wv4zeg/), comment pdbyv0a) identified the construction: "multiplying 187Mb by 2, then adding the 35 million SNVs onto it", and "a 1-Mb inversion is a single mutational event"; comment pdebkr5: "over half of these human SDRs are classified as centromere and acrocentric". Nesslig20 (Peaceful Science topic 18094, post 1, 2026-10-05), relaying Neukamm (Panda's Thumb): "one InDel can affect many base-pairs, ranging from 10s to 10s of thousands or even 100s of thousands of bp".
- In support: CSAC 2005 counts 5M indel events as far fewer than 35M substitutions; Yoo 2025 reports gap divergence as megabases affected (5–15x SNV megabases) and inversions as events (1,140); both are unit distinctions consistent with the critics.
- Weaknesses in the responses: critics do not give an independently derived event count from Yoo 2025; the first sourced count is the audit's (R4 GAP-07), though Mansfield's uncited ~25M (MF-06) is within ~25% of it, and justatest90 (Reddit 1wv4zeg, comment pdug1oj) and Wrevellyn (1wv4zeg, pdcrd62) gave the rate route ('about 9.7 million expected substitutions on the human lineage'); Hancock's 407 is arithmetic on Day's number, not an event count. Per-base fixation of large indels may involve selection on the whole event, which supports event counting but does not tell us how many events there were.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Yoo et al. 2025 | "Gap divergence showed a 5-fold to 15-fold difference in the number of affected megabases when compared to single-nucleotide variants" | verified; supports bp ≠ events |
| CSAC 2005 | "Of course, the number of indel events is far fewer than the number of substitution events (,5 million compared with ,35 million, respectively)." (extraction renders "~" as ",") | verified |

## Pre-registered prediction
Pre-registration: not run. Prediction (critic): the number of independent mutational events in the human–chimp divergence is 40M ± 30%. Prediction (claimant): n/a (Day concedes the unit; he reports both).
- Result that would change a verdict: a published count of fixed SV events well above 100M.

## Check
Arithmetic audit (python3 -I, scratch). Review: pending.

R4 GAP-07 (research/checks/results/R4-GAPS-04-07-02.md): Events per lineage from three routes (two share the CSAC 17.5M SNV anchor): rate x time with k = mu (Besenbacher 2015, Kloosterman 2015, Belyeu 2021, Collins 2020) 9.6-10.4M; clock-free calibrated 18.2-19.7M; CSAC-observed basis 20.0M (the 22.5M per-lineage upper bound used a per-species reading of CSAC's 5M and is retired by R4 GAP-07b). 205M is ~9-11x these; >= 8.0x over the observation-consistent part of a mu x T x N_anc grid (5.3x at its extreme corner, which predicts ~2x the observed SNV divergence). CSAC's 5M indel events are a two-lineage total (abstract; '~5 million compared with ~35 million'; indel:SNV 0.14 vs germline 0.04-0.12). A repeat-unit reading of SDR base pairs gives 21-30M at Yoo's 171/32 bp units. G_f counts events, so a base-pair numerator is a unit mismatch inside Day's own method. Review: `research/checks/REVIEW.md` (review #6, 2026-10-08).

R4 GAP-07b (research/checks/results/R4-GAP07b-alignment.md): direct count from the UCSC hg38 vs panTro6 alignment (non-T2T; both lineages plus ancestral polymorphism): 37.77M SNVs, 4.30M indel events (2.17M extra-human-base, 2.09M extra-chimp-base, 35k both-sided), 42.10M events, 21.05M per lineage. 205M is 9.7x raw (pre-registered); bracket about 7-14x: Day-favourable 7.2-9.5 (non-aligned bp as 171/32-bp repeat units, indel slippage x2-x3), critic-favourable 10.1-13.4 (human lineage alone, top-level fills, <2%-divergent records, CSAC fixed share); all bracket rows post hoc. Indel size spectrum confirms McCarthy MC-11 and Neukamm via Nesslig20 (largest 25.2 Mb; 71 events > 1 Mb). Critic estimates graded against the measurement: McCarthy 22.5M +7%, Mansfield 25M +19% (per lineage assumed), Nesslig20/Hancock ~38M -10% of events; the k = mu rate route (9.7M) is ~2x low (the clock question, B4a / GAP-06). Events are not fixations and are not selected: the unit ratio is not to be multiplied by a neutral fraction. Review: `research/checks/REVIEW.md` (review #8, 2026-10-09).

R4 GAP-07c (research/checks/results/R4-GAP07c.md; reviews REVIEW-R4-GAP07c-{correctness,steelman}.md; review #13, 2026-10-09): with the human-side polymorphic share measured (chimp side assumed), fixed events per lineage are 17.2-17.9M, so 205M is 10.6-12.6x fixed events (human lineage alone 11.9; 11.1-12.1 across thresholds; numerator-corrected 10.5-12.3). Combined with GAP-07b's Day-favourable rows the bracket is about 8-13x. The measured SV (6.8%) and indel (7.4-10.5%) polymorphic shares are lower bounds (short-read calls).

## Simulator variables implied
- `required_fixations` unit selector: bp / events / SNV-only.

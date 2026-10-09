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
  fidelity: accurate   # Day's 2nd-edition wording is 'base pairs'
  external: supported   # R4 GAP-07: events per lineage 18-22.5M (calibrated / CSAC-observed), 9.6-10.4M rate x time; 205M is ~9-11x (>= 8x at observation-consistent inputs, 5.3x at the extreme grid corner); a base-pair numerator against G_f's events is a unit mismatch
---

## Statement (verbatim)
> The 410 million base pair difference refers to structural variation, which includes duplications, insertions, etc., in which a single mutational event can cause hundreds, thousands, or even millions of base-pair differences.

Source: [Dennis McCarthy, Vox Day Responds](https://dennismccarthy.substack.com/p/vox-day-responds), 2026-09-17, para 26 (MC-11).

> bases affected by a rearrangement are not separate mutation events: one structural change can affect millions of bases.

Source: [r/DebateEvolution, Dumb-and-Dumber](https://www.reddit.com/r/DebateEvolution/comments/1wss2wj/), 2026-09-28 (RE-05).

## Formal statement
Claim: fixations are events; R_events = (SNV + indel events + inversions + other SV events)/2 ≈ 20M per lineage, not 205M.

`derived:` (python3 -I) 35e6 SNV + 5e6 indel events (CSAC) + 1,140 inversions = 40.0e6 events; /2 = 20.0e6. 410e6/40.0e6 = 10.25; 410e6/35e6 = 11.7. Day's own wording in the 2nd edition is "410 million base pairs" (A3a), i.e. the critics' reading of the unit matches Day's text.
Related critic statements: Hancock (GG-10) "the number is 205 million differences, right?" and GG-11 (his "something like 407" = 205e6/(2 x 252,000) = 406.7 mutations per generation over both lineages, an accounting choice); Nesslig20 (PS-03) reference genome differences vs fixed; Mansfield (MF-06) "around 25 million give or take, not 200 million" (uncited).

## Assumptions
- Stated: one mutational event can affect many bases.
- Implicit: a structural change fixes as a single event with probability comparable to a point mutation (not required for the logic here, which is about counting units).

## Responses
- Against (Day): s7.3 concedes the concern and runs the SNV-only variant (A3b). Day has not, in the corpus, defended counting bp as separate fixations. R4 GAP-07: the s7.3 wording (SVs "should not each count as a single fixation event in the same sense as a point mutation") does not settle whether Day regards bp counts as wrong, and the 3.0 abstract keeps 205M; the decisive point is that G_f counts events.
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

R4 GAP-07 (research/checks/results/R4-GAPS-04-07-02.md): Events per lineage from three routes (two share the CSAC 17.5M SNV anchor): rate x time with k = mu (Besenbacher 2015, Kloosterman 2015, Belyeu 2021, Collins 2020) 9.6-10.4M; clock-free calibrated 18.2-19.7M; CSAC-observed basis 20.0M (22.5M upper bound). 205M is ~9-11x these; >= 8.0x over the observation-consistent part of a mu x T x N_anc grid (5.3x at its extreme corner, which predicts ~2x the observed SNV divergence). CSAC's 5M indel events are a two-lineage total (abstract; '~5 million compared with ~35 million'; indel:SNV 0.14 vs germline 0.04-0.12). A repeat-unit reading of SDR base pairs gives 21-30M at Yoo's 171/32 bp units. G_f counts events, so a base-pair numerator is a unit mismatch inside Day's own method. Review: `research/checks/REVIEW.md` (review #6, 2026-10-08).

## Simulator variables implied
- `required_fixations` unit selector: bp / events / SNV-only.

Steelmanning: Day side

# REVIEW R4-FMnull-S4: steelman, Day side

Reviewer: fresh reviewer instance (Paperclip EVO-17), 2026-10-19. Skill: `review-steelman`, Day side. I did not author any of
this work and did not read a critic-side steelman. Under review: `research/checks/results/R4-FMnull-S4.md` (`d0c94e2`)
against the registration (`fmnull_s4.py` docstring lines 1-249, `75743af`; post hoc pre-run `45f814d`) and the lead ruling
S4-R1..R8, S4-R6a, S4-R6b (`research/checks/briefs/FMnull-S4-analyst.md`, `7670832`, `988394e`). Read beside the correctness
review (`REVIEW-R4-FMnull-S4-correctness.md`, `c2ae429`).

Inputs: `raw/fmnull_s4_post.json` only (per-corner `sims`, `bands`, `planted`, `meta.pilot`). The npz was not loaded. Local
work: three `python -I` reads of the JSON, seconds each, under 100 MB. **Every number of mine below that is not printed by
`post` is post hoc and descriptive.** None of them changes a class, the aggregate or a verdict.

Settled and not re-opened: S4-R3's refusal to extend `NON-DISCRIMINATING` (finding 1 is about the ruling's *framing* of the
non-extension, and I stop there); S4-R6b. Outcome accepted as registered: governing `S4-MARGINAL`, no value moves, no defeater,
FM10 internal `pending` (D-09), external `contested`, FM3 untouched. Rule RD does not apply: S4 is the audit's criterion, not a
statement of Day's, and its readings were combined in advance by an any-DAY rule (docstring lines 141-143). That rule is the
generous choice for Day's side.

## Findings

**1. MAJOR: a wide band is being used to discount the one cell that lies above it. That reverses what width measures, and
S4-R3's framing of the non-extension as a "gap" or "defect" is wrong. I say so and stop; the lead re-rules on the framing.**
- Where: headline lines 10-11 ("its measured band width there is **9.54, over the registered non-discrimination threshold of
  9**"); section 5, lines 159-167 (heading "Limitation of the criterion", "a defect of the audit's own criterion"); critics'
  bullet lines 207-208 ("its band is over the width threshold"); "Both" bullet line 219. Ruling: brief lines 109-119 ("Record
  the gap as a limitation of the criterion ... It is a defect of the audit's own criterion").
- Why it is backwards. The registered width, (N_hi - 1) / (N_lo - 1) > 9 (docstring line 139), measures how much room the null
  leaves for a value *inside* it. That is why the label was registered on `CRITIC` and `MARGINAL-IN` only: a wide band cannot
  be failed from inside. A value above N_hi has escaped the whole envelope. A wider envelope makes that harder, not easier. At
  1000 kb the width of 9.54 comes as much from the low edge (N_lo 2.339, so N_lo - 1 = 1.339) as from the high one, and the
  low edge has no bearing on a `MARGINAL-OUT`. P3's audit leg registered the wide band as the null's protection ("BGS with sd
  0.32 makes the upper edge large", line 165). The data cleared that protection.
- So the registration's restriction is correct as written, and there is no gap. Extending the label to `MARGINAL-OUT` would
  not close a loophole. It would discount the null's failure *because* the null was given the widest range. S4-R3 rightly
  refuses the extension. Booking the restriction as a defect, though, tells readers the cell should count for less, and the
  headline then does exactly that.
- Fix (for the lead to rule): keep S4-R3's refusal. Drop "gap", "defect" and "limitation" from section 5, or replace them
  with the reason the label is confined to in-band classes. Remove the width sentence from the headline and from the
  critics' bullet, or pair it with "a wider band makes `MARGINAL-OUT` harder to reach". What *is* a legitimate caveat is that
  the upper edge was set by unsourced settings at their extremes (finding 2), and that belongs with the edge, not with the
  width.

**2. MAJOR: the write-up carries a post hoc reading of the governing cell for the critics' side (section 6, bullet lines
207-208) and none for Day's. The same raw numbers, read for Day's side, say the governing edge rests on one corner out of 48
that the data's own phi_A rules out.**
- Where: section 6, lines 171-175 ("This is the pattern regional variation in the ILS rate gives (... linked selection beyond
  the modelled sd(B) 0.32)"); critics' bullet lines 207-208; Day's bullet lines 196-197 ("depends on two UNSOURCED settings").
- Recomputed from `cells["F2|1000"].sims`, post hoc. FULL N_hi 13.770 is set by **one** corner,
  `c_35k_55k_r1.0e-08_h1_bgs2000k`: point value 11.721, jackknife SE 1.024, and 2 SE adds 2.05 to the edge. That corner sits at
  the high-variance end of three unsourced or conventional settings at once (RHET 1, BGS ell 2 Mb, r 1.0e-8). The next corner's
  edge is 10.169, and the data (15.925) are 1.57 times it. At 300, 1000 and 3000 kb **no corner's point value reaches the
  data**. The edge corner's own fit to the data is poor on the other statistic and on the ILS share:
  - phi_A is 5.617 +/- 0.303 against the data's 2.654 +/- 0.260, a gap of 7.4 combined SE;
  - q-bar is 0.202 against the data's 0.310;
  - pilot topology fraction is 0.232, against the 30% Scally rate that S4's text cites (docstring line 41).
- Joint check, post hoc. Restrict to corners whose phi_A is within 2 combined SE of the data's: 17 corners at 1 Mb, 12 at
  300 kb. Among them the highest phi_R edge is 8.609 at 1 Mb, which the data exceed 1.85 times, and 5.257 at 300 kb, exceeded
  1.97 times. The result is the same at 3 SE (28 and 16 corners, same maxima).
- What this means. Section 6's own reading ("beyond the modelled sd(B) 0.32") is an admission that the registered null, as
  specified, does not contain the data jointly. The rescue it names needs a setting outside the registration and was not
  tested. Offering it in the critics' column without the matching measurement in Day's column breaks hard rule 1's parity.
- Fix: put the single-corner fact (one corner, its point, SE and q-bar; next edge 10.17) in Day's bullet at line 196. Either
  add the joint-check numbers to section 6 as post hoc, beside the critic reading, or take both post hoc readings out of
  section 8. Label section 6's explanation "untested auxiliary (sd(B) above the registered 0.32)". No class changes: the
  registered bands are marginal per statistic and the joint check is not registered.

**3. MINOR: the near-misses that cut against the critics' side carry no margin, while the audit's misses carry theirs.**
- Where: headline line 12 ("Every other scored F2 cell is `CRITIC`, `MARGINAL-IN` or `BELOW-NEAR`"); Day column lines
  192-198.
- The neighbouring cell is F2 phi_R at 300 kb: 10.372 against FULL N_hi 10.474. That is `MARGINAL-IN` by 0.102 (1.0%), above
  every corner's point value, and below only one corner's v + 2 SE (the same corner as in finding 2).
- The other bands and filters agree:
  - under band N, phi_R is `MARGINAL-OUT` at 300 and 1000 kb;
  - under band U it is `MARGINAL-OUT` from 30 kb up, and `DAY` at 1000 kb;
  - under F3, the CpG filter, phi_R is `MARGINAL-OUT` at both 300 kb (9.300 against 8.447) and 1000 kb.
- S4-R6 required margins "in the same sentence" for the audit's misses, and the same standard applies here. S4-R2's "exactly
  one cell" is true and stays.
- Fix: add one clause to the headline: "the 300-kb cell misses `MARGINAL-OUT` by 1.0%". Add one Day bullet: "the rate excess
  survives the CpG filter and appears there one W step earlier (F3 `MARGINAL-OUT` at 300 and 1000 kb)".

**4. MINOR: the Day bullet at line 199 and the P4 paragraph rest on a direction that correctness MAJOR 1 has removed. Day's
point survives on firmer ground, and the write-up should move it there.**
- Where: lines 132-135, 156 and 199.
- With the thinning unpaired (correctness finding 1), "Q168 pushes S4-M toward the critic classes" is unsupported. The Day
  conclusion, "a critic-side `CRITIC` on S4-M says nothing about Day's mechanism", does not need it. It stands on two
  independent registered facts:
  - P4's class legs held in full: no Q1 or Q2 class differed from central anywhere (S4-R4);
  - every S4-M band is infinitely wide (S4-R2b).
- My addition: unpaired thinning only adds noise to the planted-against-central differences. It can make P4's < 10% phi legs
  harder to hold, never easier, so their holding (largest move +6.4%) is if anything conservative.
- Fix: rewrite line 199 on those two grounds, and drop "push ... toward". This is subject to the lead's re-ruling of
  S4-R4.

**5. MINOR: the literal "mesas" reading, S4-M, was neither reachable by a genuine HG or CG block process nor able to
discriminate. The write-up still counts its one DAY as reachability evidence.**
- Where: line 141 ("T5 reaches DAY ... also on S4-M at 100 kb (scaled 52.2, raw 55)").
- From `planted.*.M`, post hoc reading: T5's 55 mesas at 100 kb are **all CG, 0 HG**, and so are T4's (11) and T5's 30-kb
  217. Correctness N1 shows these are unswapped windows read against a share pulled to 0.72. They are an artefact, not
  detected blocks.
- The genuine HG-direction processes stay well short of DAY:
  - T2 at 30 kb: 44 (HG 37), `MARGINAL-IN`;
  - T2 at 100 kb: 3 (HG 3), `CRITIC`;
  - T6 at 30 kb: 28 (HG 24), `CRITIC`;
  - T6 at 100 kb: 0.
  DAY at 30 kb needs M > 272.
- S4-M, which the registration itself calls "the literal 'mesas'" (docstring line 66), therefore had no demonstrated route to
  DAY and, with E_lo = 0 everywhere, no route to a discriminating `CRITIC`. It is the S2 shape on one leg. This does not
  touch S4-R5: aggregate reachability rests on S4-A (T5 at 1 Mb, T4 at 100 kb).
- Fix: remove the S4-M DAY from the reachability evidence at line 141. Add one sentence that S4-M could inform neither side
  on this design.

**6. MINOR: the critics' S4-A bullet calls S4-A "the literal reading" and omits the power line the registration makes
mandatory.**
- Where: lines 203-204. Registration: docstring line 66 gives "literal" to S4-M, and lines 208-212 say the critic-side item
  goes "ALWAYS with the power line".
- On this run a `CRITIC` on S4-A excludes only non-tree sharing on the scale of half the genome (line 149), and never Q168.
  This is separate from correctness MINOR 4, which is about the CENTRAL-relative "far below".
- Fix: replace "the literal" with "the asymmetry". Append "(detects T4/T5-scale blocks only; no power against Q168)".

**7. NOTE: Day's column credits the audit, not Day, at line 198.** "S4 is reachable for Day ... not built so that he could only
lose" is about the fairness of the audit's design. For Day's own mechanism, S4 *is* unreachable: no Q168 class moved, and P4
predicted as much (docstring line 183). Fix: reword it as "S4 cannot reach DAY under Q168, so no S4 outcome can count against
sigillation as Day states it; the S2 protection applies in substance".

**8. NOTE: line 211 ("No statement of Day's is tested by S4 (he has made none about incongruence)") sits in the critics'
column.** It is the fact that protects Day from any S4 outcome. Placed there, it can read as a rhetorical jab (tag it under
RH). Fix: move it to "Both" or to Day's column.

**9. NOTE: the ILS null misfits at both ends, and neither misfit is the critics' to bank.** phi_A is `BELOW-NEAR` at 10 kb (W3),
and phi_R is above every corner's point value from 300 kb up (finding 2). The corners' q-bar comes in two clusters,
0.19-0.21 and 0.39-0.41. They bracket the data's 0.30-0.31, but no corner matches it within 0.08. None of this changes a
class. It does mean that the S4-NOT-MET item's wording, "incongruent sharing behaves as coalescent ILS at window scale"
(docstring line 209), would not describe this run even if the aggregate had come out that way. Fix: optional, one sentence in
section 8 "Both".

## What the evidence costs Day (stated as plainly as the credit)

- **Nothing here supports sigillation.** The only exceedance is on the symmetric rate phi_R, and Q168's mechanism does not
  produce it. At 1 Mb, Q2 phi_R is 3.345 and Q1 is 3.455, against central 3.334 (+0.3% and +3.6%). The rate excess cannot be
  credited to Day's "contiguous blocks of change into one dominate lineage" (Q168). At most it shows that the audit's ILS null
  is too narrow in ancestral-Ne or linked-selection variance, and both of those are known processes.
- **The asymmetric reading goes against non-tree blocks of any modest size.** S4-A is `CRITIC` from 30 kb up, and the data's
  phi_A at 1 Mb (2.654) sits low in its band. Even if Day were to take up a two-lineage story, it would have to cover about
  half the genome to show (T4, T5).
- **The exceedance is modest against the data's own noise.** 15.925 - 2 x 1.290 = 13.345 lies inside the edge (correctness N4:
  1.67 data SE). The registration does not use the data SE, but a reader should know it.
- **Q169 (b), "the dominant source of genomic divergence", gets nothing from S4.** Under the audit's "dominant" gloss (Q2,
  f e > 1) no class moved. S4 neither supports nor contradicts Q169.
- F0, the unfiltered alignment, is the most extreme filter. That fits an alignment component in any analysis run on
  unfiltered data. It is unscored as registered, and I draw no inference about Day's pipeline.

## Verdict moves

I agree with the proposal: no value moves, no defeater either way, FM10 internal `pending` (D-09), external `contested`, FM3
untouched. Findings 1-2 strengthen how the one `MARGINAL-OUT` should be *read*. They cannot move anything, because the
registration's `S4-MARGINAL` row licenses nothing, and the joint check is post hoc.

## Counts

BLOCKER 0, MAJOR 2, MINOR 4, NOTE 3. Finding 1 disputes the framing in ruling S4-R3 (not its refusal), and I stop there for
the lead. Finding 4 depends on the lead's re-ruling of S4-R4 after correctness MAJOR 1. No wrong printed number found beyond
those the correctness review lists.

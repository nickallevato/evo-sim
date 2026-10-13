# Review 2 of 3 (steelman, Day): R4 L2, a sourced hardness h for humans

Reviewer: `reviewer` agent (Opus), fresh instance, task EVO-45; did not author the registration (`ade0542`), the run
(`1d9a32f`), the write-up (`8d17245`) or the correctness review (`4b97637`). Date 2026-10-13. Skill: `review-steelman`,
Day side. Tier: load-bearing (three reviews). I did not read the critic-side steelman.

Read: `l2_hardness.py` (whole docstring and code), `R4-L2.md`, `REVIEW-R4-L2-correctness.md`, `briefs/L2-analyst.md`,
`raw/l2_main.out`, `raw/l2_quotes.md`, the `#` header of `raw/l2_screening.tsv` and the rows of the E2-false records,
the model definition in `research/checks/hf_followups.py` (docstring lines 52-57, step code lines 222-262), the H8
claim file's verdict lines, `parameters.yaml` `generation_time_years`. Source text: C1440 (Madsen, Robertson and Ye
2019 working paper, `sources/raw/l2-2026-10-13/C1440/oa.bin`, a PDF) extracted with `pdftotext -layout` to `/tmp`;
read only, nothing executed. Every number below not printed by `main` or the write-up is **post hoc (this review)**:
stdlib arithmetic on the workstation, one process, under a second.

## The Day-side case in one paragraph

Day's quoted claim (Q47) is that Haldane derived his limit from "the reproductive cost each substitution imposes on a
population". In the audit's own model a cost exists at every h > 0 (H5 note), and on the registered readings no
eligible record on either route puts h below 0.1. The low end of the governing interval (0.125) and the DISJOINT flag
both come from one regression in one working paper, mapped to h through a reading (A1) that the audit's own
hard-selection models contradict (SD-1). The write-up credits critics with results that are built into the
sensitivity design or come from post hoc and ineligible numbers (SD-2), and leaves out the Day-favourable estimates in
the same source (SD-3). None of this moves a verdict value; it moves how the result should be described. What the
evidence costs Day is set out at the end, and it is not small: the same validity problem that removes route (a)'s
low end also undercuts route (b)'s high values.

## Findings

### SD-1 MAJOR. Mapping A1 reads the audit's own hard-selection models as soft; route (a) is not a validated estimator of h

Evidence. The registration's A1: "h equals the per-generation persistence of a deviation in log population size,
beta_gen (beta_gen = 1: nothing is compensated, deaths add, hard; beta_gen = 0: a deviation is fully compensated
within one generation, the slots refill, soft)". The models whose thresholds L2 is placed against do not behave that
way. `hf_followups.py` docstring: "hard : H8 hard ... J = f N, f = min(R, K/N); survive with prob w" and
"mix(h) : J = R N juveniles ...; hard survival with prob w^h; if survivors > K, keep K by weighted sampling ... on
w^(1-h) ... h = 1 is hard selection followed by random culling to K (validation against H8 hard)". Code lines 256-262
implement exactly that (N' = min(K, survivors)). So in both hard models a deviation of log N smaller than the spare
excess ln(R w̄^h) is fully removed in one generation: beta_gen = 0 at h = 1. Post hoc (this review), deterministic
illustration: R = 1.111, h = 1, log-load 0.05 per generation, a 5% downward shock: next generation min(K, 1.111 x
e^-0.05 x 0.95 K) = min(K, 1.004 K) = K, so beta_gen = 0 and A1 reads h = 0 for the model that defines h = 1. In-model,
persistence of N tracks the spare reproductive excess (it rises only as the load approaches ln R), not h. Haldane's
cost is paid out of the reproductive excess of a population held at its size; full compensation of population
losses is what the hard model does, not evidence that selection is soft.

The registration conceded that "aggregate series alone identify nothing; A1 is the assumption under which they
identify h". The new point is that A1 is false in the model the thresholds come from, and no tool validation (the
estimator applied to model output at known h) was registered or run; `smoke` checks the arithmetic of the mappings
only.

Consequences, all against Day: (i) the governing lower end 0.125 comes from route (a) alone; (ii) DISJOINT is reported
"as a result in its own right", but it may be an artefact of the mapping, not a disagreement in the data; (iii) the
write-up's critic-side bullet "route (a) is direct evidence that population losses are largely compensated within a
generation", offered against M-b1, describes a property the audit's own hard model also has; (iv) the proposed
`parameters.yaml` entry calls route (a) part of a "sourced" bracket.

Mirror defect (recorded because it cuts against Day; see "What the evidence costs Day"). Route (b)'s M-b1 is not
validated either. In the mix model parents are drawn uniformly at random (`pa = rng.integers(0, N, J)`, line 238), so
all genotype-dependent selection, in both channels, is pre-reproductive. A Crow decomposition of that demography, post
hoc (this review), equilibrium N = K, Poisson maternity: Ps = 1/R, Im = R - 1, If = 1/R, If/Ps = 1, so M-b1 gives
h = (R - 1)/R: 0.10 at R = 1.111, 0.33 at R = 1.5, 0.50 at R = 2, the same at every model h. In-model the route (b)
statistic tracks R, not h.

Fix. (1) In "Both / the audit's own errors" and in the one-line result, state that neither primary mapping has been
validated against the HF models: A1 reads the hard models (H8 hard; mix h = 1) as soft wherever there is spare excess,
and M-b1 returns (R - 1)/R regardless of h (post hoc arithmetic above, approximate). (2) Describe DISJOINT as "the two
mappings disagree", not as a disagreement between data sets. (3) Delete or condition the critic-side bullet on
compensation as evidence against M-b1. (4) Add a post hoc line: route (b) alone gives U1-MH, [0.284, 0.641], no move.
The governing result stays as registered. (5) For integration: the `parameters.yaml` entry for h should say "sourced
statistics, mapping not validated against the model", and both intervals carry that label. (6) Open item: a
tool-validation check (pre-registered, on na-workhorse) that applies both estimators to HF mix output at h in {0.1,
0.3, 1} and R in {1.111, 2}, before any future L2 rerun can trigger the registered B-HH or B-LL moves on H8.

### SD-2 MAJOR. Critic-side credit rests on a structural property of the sensitivity design and on unlabelled post hoc and ineligible numbers

Evidence. Write-up, critic side: "Readings that favour softness move the band down, never up. A1 x M-b0 and every
A-down pair give B-LH; modern records give B-LH. Route (a)'s robustness columns reach 0.040-0.068 (P1, column 4) and
the 20- and 40-year estimates reach below 0.1. The excluded Gambia data would give about 0.01 (P3). The Utah late
cohorts give 1/7 (0.143) as the transition proceeds."

- *Never up is built in.* In the script, A-up is `(a1[0], 1.0)` and M-b2 for `crow` is `(h1[0], 1.0)`: the
  hardness-favouring readings keep the primary lower end and only raise the upper end, while A-down and M-b0 set the
  lower end to 0. From a primary of B-MH, no up-reading can move the band (hi is already >= 0.3; lo cannot rise) and
  every down-reading moves it to B-LH. The asymmetry is a property of the registered readings, so it says nothing
  about the data.
- *Column 4 at 0.040-0.068* is a point-gamma figure without the registered +-1.96 SE (correctness MINOR-2: [0.005,
  0.116] with SE). It is post hoc and not labelled so in this bullet.
- *Gambia "about 0.01"* is from C0142, excluded because it reports annual-fitness variance components, not a
  registered statistic (P3; correctness NOTE-2 confirms the exclusion). Mapping an ineligible statistic through a
  formula registered for a different one, then citing it as evidence, gives a number with no registered meaning.
- *Utah late 1/7* is E2 false (post-transition). In its own source it shows the viability share falling as infant
  survival rose: "diminished from approximately 1/3 to 1/7 following a marked increase in infant survival" (L2Q-17).
  That is evidence on the direction of modernisation (SD-5), which favours Day for deep history, not evidence that
  pre-transition selection was soft.

Fix. Rewrite the bullet as: "Every registered softness-favouring reading lowers the governing lower end to 0 (B-LH);
by construction no hardness-favouring reading can raise it." Move the column 4, Gambia and Utah-late figures to the
post hoc section, labelled "post hoc", "ineligible statistic" and "post-transition" respectively, or give them with
the Day-favourable counterparts from SD-3 and SD-5 in the same bullet.

### SD-3 MAJOR. Day-favourable estimates in the route (a) source are not credited; P1 reports its low reach and understates its high reach

Evidence (C1440, `pdftotext -layout`):
- Table 3 text: "Restricting the sample to the countries with the best data coverage and the most reliable historical
  population data, namely Italy, the Netherlands and the UK, back to 930, yields γ̂ = −0.021". That is column 7. Post
  hoc (correctness MINOR-2, confirmed here): with SE, h in [0.335, 0.471]. It overlaps route (b), so DISJOINT is
  False, and it is the authors' own description of their best population data. Correctness NOTE-5 calls column 7
  alone "not a defensible reading" of the specification clause. As the governing reading I agree (column 2 is what the
  authors convert to a half-life). But under rule C it is a plausible reading and it belongs in any readings table
  (R-a4). Post hoc (this review): R-a4 gives governing [0.284, 0.641], B-MH, PD-w hit, PA-4 miss (route (a) wholly above 0.3), DISJOINT
  False, no move.
- Table 4 ("Convergence by Country"), population, 1470-1870, gamma: Austria -0.001, Belgium -0.006, France -0.010,
  Germany -0.029, Italy -0.037, Netherlands -0.005, Spain -0.024, Sweden -0.010, UK -0.027. Post hoc (this review),
  same formula, T = 30, G in [25, 30], point values: Austria 0.97-0.98, Netherlands 0.85-0.87, Belgium 0.82-0.85, France
  and Sweden 0.70-0.74, Spain 0.28-0.35, UK 0.19-0.25, Germany 0.13-0.18, Italy 0 (1 + 30 gamma < 0). Median country
  gamma -0.010, h 0.70-0.74. Five of nine countries give h >= 0.70. Caveats, stated fairly: the country regressions
  cannot carry time fixed effects as the panel does, and the authors attribute odd country results to "small-sample
  bias, measurement errors, and other omitted fixed effects that we can control for in panel data". The spread runs
  from 0 to about 1.
- Table 5 ("Convergence by Country Group"), population 1470-1870: Protestant -0.023 (SE 0.0007). Post hoc (this
  review): h in [0.269, 0.418], straddling 0.3.

P1 concludes: "Across the authors' own SUR robustness set, route (a) spans roughly 0.04 to 0.44". That figure is
quoted in critic credit, but only Table 3 enters it, and Table 4 is never mentioned. The narrow registered interval
[0.125, 0.256] sits at the fast-convergence end of the source's own estimates. Only Italy and Germany converge as fast
or faster.

Fix. In P1, add Table 4 and Table 5 (labelled post hoc, with the caveats above): "the source's country-level point
estimates span h of 0 to about 0.98, median about 0.7". In "Who this helps / Day side", add a bullet: "The authors'
best-data sample (column 7) gives [0.335, 0.471], which overlaps route (b); the registered column 2 is at the
fast-convergence end of the source's own estimates." If the fix pass adopts correctness MAJOR-1's readings table, add
R-a4 (column 7) as a row. Column 2 stays the governing reading, and the RD rule is satisfied either way because no
reading moves a value.

### SD-4 MINOR. The generation-length bracket is the audit's choice and leaves out Day's own values

Evidence. Registered "G = generation length, bracketed G in [25, 30] years". `parameters.yaml`
`generation_time_years`: day_2019 20 (B2019-02-07), day_2026 25 (Z23003785), day_alt 32.5 (B2025-01-18), all
`verified: false`. A shorter G raises h on route (a) (h = (1 + 30 gamma)^(G/30) under the source's formula). Post hoc
(this review), column 2 with SE: G = 20 gives [0.250, 0.337], G = 32.5 gives [0.105, 0.170], and Day's full range
[20, 32.5] gives **[0.105, 0.337]**. That overlaps route (b), so DISJOINT is False and PA-4 a hit. Band B-MH, PD-w still
a hit (barely: 0.105), no move. This cuts both ways: the lower end falls as well.

Fix. Add a sensitivity line "G over Day's stated values [20, 32.5]" (post hoc) beside the registered G = 25 and
G = 30 lines, and note in the provenance that the registered bracket is the audit's.

### SD-5 MINOR. The E2 run-time rule removed high-h, high-mortality records; P2 reports only the downward candidates

Evidence. R-E2 (screening header) admits a record only if natural fertility is reported or mean live births are >= 6,
with "'unclear' counts as false". The 6-birth line has no cited source. P2 lists the E2-false records below 0.284 whose
status "is arguable". It does not list the E2-false records above the route (b) median that carry pre-modern mortality
in their own quotes:
Macá 1970, 0.639 ("36% of them die before the age of reproduction", "3.6 livebirths per female who completed her
reproductive performance", L2Q-46; excluded on 3.6 births); Zapotec 1978, 0.477 (Im 0.626, L2Q-39; "no fertility level
given"); Brazilian isolate 1987, 0.522 (Im 0.28, L2Q-44; "no fertility level"); Halfmoon 1850, 0.427 ("unclear");
Nicobarese c. 2000, 0.380 (5.26 births). A fertility-only proxy at 6 births excludes high-mortality, low-fertility
groups, and those are the ones closest to pre-modern conditions. This complements correctness MAJOR-2 (the dropped
mortality conjunct), which supplies the same direction on the mortality side.

Every within-source pair in the inputs also moves the same way, post hoc (this review), read off `l2_main.out`:
Slovincians born up to 1900 0.641, after 1900 0.439; Utah early 0.333, late 0.143; Zapotec 1978 0.477, 2000 0.070;
Halfmoon 1850 0.427, 1900 0.374. In all four, h falls as mortality modernises. The H branch concerns 252,000
generations of pre-modern mortality, and most route (b) records are 20th-century surveys. On Day's reading, the
deep-history viability share is at or above the sampled values.

None of this moves the hull: the maximum stays 0.641 (Macá 0.639 is below it) and the minimum is set by an eligible
record.

Fix. Add the five upward records and the four within-source pairs to P2 as post hoc and descriptive. State that the
6-birth threshold is unsourced, and that "unclear = false" excludes in both directions. Add one Day-side bullet: "Within
every source that reports two periods, the viability share falls with modernisation."

### SD-6 MINOR. PD is presented as Day's miss; it is the audit's proxy, and a stronger one than Q47 needs

Evidence. Registration: "Neither side states a value of h for humans. The predictions below are the audit's reading of
what each side's position needs, not quotes; they score no author statement (rule S)." The scores table has a column
"Side" with "Day" and the tally reads "Day side 1 of 2". The caveat is not repeated in the write-up. On content: Q47
reports what Haldane calculated and why ("the reproductive cost each substitution imposes on a population"). That cost
exists in-model at every h > 0 (registered H5 note). B-HH is not even sufficient for "approximately one ... per 300
generations": at h = 0.3 the in-model rate is "about 1.3-1.7x" the hard cap at the same R (R4-HF), outside R1's 25%.
Under rule C, the closer proxy is PD-w (h bounded away from 0), and it hit.

Fix. Rename the column "Side (audit's proxy)", add the rule S sentence under the table, and add: "Q47's literal content
needs h > 0; B-HH is the audit's strong proxy, not Day's claim." Do the same for PC and GG-26 for symmetry.

### SD-7 MINOR. The one-line result omits the one finding that favours Day on every eligible record

Evidence. The one-line result states the intervals, DISJOINT, B-MH, the absence of any move and the audit's prior.
It does not state that no eligible record on either route lies below 0.1 (PD-w hit, PC-w miss). That is the only
result in the check that bears on GG-26's "only applicable for hard selection models" (the cost exists at h > 0), and
it appears only in "Who this helps" (rule 1, equal prominence).

Fix. Add to the one-line result: "On the registered readings no eligible record on either route gives h below 0.1, so
in-model a cost of selection applies to every sourced population (conditional on the mappings, SD-1)."

### SD-8 NOTE. Concur with correctness MAJOR-3 (H8 placement sentence); it errs against Day

"Exceeded by more than R1 toward its lower end; the sourced interval spans the line" asserts an untested result. At
h = 0.1 the strict tie reading is 1.36x, only 0.11 above R1's 1.25. Under the assumed monotonicity the R1 crossing can
lie below 0.125. Given SD-1, the lower end is also an unvalidated mapping. Use correctness's replacement text.

### SD-9 NOTE. What route (a) measures, from the source itself

Equation (12) is "∆ ln Lit = φ0 + γ ln Li,t−30 + λ ln Xi,t−30 + Zi,t ξ 0 + TD + CD + ε2,it", with Z including "the
number of epidemics" and X "cultivated land size ... and the stock of great scientists", plus time (TD) and country
(CD) fixed effects. So γ is convergence of each country's deviation from a common, time-varying path, conditional on
epidemics, land and technology. Europe-wide shocks, which is what a density-independent death load common to all
countries would look like, are absorbed by TD. The authors name "epidemics and emigration flows" among the sources of
the variation (text before the Germany 1600-1650 passage), and migration between countries corrects relative
deviations without any compensating birth or death. In the honesty column: the authors also state that measurement
error bias "can be positive as well as negative" (data section), so the write-up's "most likely bias in route (a) runs
Day's way" holds for the dynamic-panel mechanism only. Neither direction is quantified. Keep Open 3 (as correctness
NOTE-1 rules) and add the conditioning and the migration point to it.

### SD-10 NOTE. The working paper is internally inconsistent on the subperiod estimates

Table 5's population "Baseline" column prints 1470-1600 −0.017 and 1600-1870 −0.030. Table 3 prints −0.034
(column 3) and −0.032 (column 4) for the same periods. The 1470-1870 value agrees (−0.028). Post hoc (this review):
−0.017 maps to h 0.49-0.55 at G in [25, 30], while −0.034 gives no half-life (clipped to 0). The two printings of
the "baseline" subperiod land on opposite sides of every cut point. Table 3's "No. of country" and "No. of obs" rows
are also swapped in the print (3609 sits under "country"). This supports Open 1 (fetch the published C1433) before
route (a) is used for anything beyond placement.

### SD-11 NOTE. Overlapping windows (concur with correctness NOTE-1), with the size of the overlap

Column 2 has 3609 observations for 9 countries over 1470-1870, which means annual, overlapping 30-year windows
(9 x 401 = 3609). The independent information is closer to 9 countries x about 13 non-overlapping windows. A
correctly sized SE would widen route (a) in both directions: upward into overlap with route (b), and downward toward
0.1. I do not quantify it.

## What the evidence costs Day (recorded with the same weight)

- **PD misses under every registered reading.** B-HH needs both lower ends at or above 0.3. Route (b)'s own minimum is
  0.284 (0.278 on the printed shares, correctness MINOR-3), so even with route (a) discarded entirely (SD-1) the
  hardness-favourable band is not reached. Correctness NOTE-5's only path to B-HH combines a non-governing column with
  a post hoc mortality cut.
- **SD-1 cuts both ways.** If route (a)'s A1 is invalid, route (b)'s M-b1 is too: in-model it returns (R - 1)/R
  whatever h is. The Day-side bullet "8 of 10 records give a viability share of 0.3 or more" then measures the
  pre-reproductive death fraction, which in the model is set by R. Honest reading: L2 has not identified human h. It
  has shown that the published statistics, under two unvalidated mappings, sit between 0.1 and 0.65. The PD-w hit
  ("not below 0.1") is conditional on the same mappings.
- **The source spreads to 0 as well as 1.** Italy's country estimate gives h = 0 and column 4 with its SE reaches
  0.005. Day's own G range lowers the column 2 floor to 0.105.
- **The within-source trends are qualitative.** No record gives a deep-history level, and the oldest eligible cohort
  (Slovincians born up to 1900, 0.641) rests on N = 32 women with an internal Ps inconsistency (P5).
- **No verdict moves toward Day.** H8 stays contested, not supported. The "soft-selection escape does not apply"
  sentence cannot be written for humans on this evidence.

## Verdict

The registered result reproduces as B-MH with no verdict value move on H, H5 or H8, and I find no reading that moves a
value toward Day. The Day-side case concerns description, not a band. The 0.125 lower end and DISJOINT come from a
mapping that the audit's own hard models contradict (SD-1). The critic credit includes a structural artefact and
unlabelled post hoc and ineligible numbers (SD-2). The Day-favourable estimates in the same source are missing
(SD-3). The registered G bracket, the E2 proxy and the PD framing are the audit's choices, and each is reported in
the direction against Day (SD-4 to SD-7). SD-1's mirror half is the main cost to Day: once validity is examined, the
route (b) values that favour Day fall with route (a).

**Counts: 0 BLOCKER, 3 MAJOR, 4 MINOR, 4 NOTE.**

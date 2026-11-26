# R4 E5-external: are MITTENS 3.0's Ara-2 "-906" and Ara+5 "0 at 60K" cells estimator artefacts or biology?

**Status: write-up (2026-11-26); awaiting one combined review (D-40). No verdict field moves here.** Brief: `research/checks/briefs/E5-analyst-2.md` (312ba5e). Design and pre-registration: `research/checks/e5_external.py` (4cfe7e5, brief E5-analyst-1, PREREG-STATUS criterion-only). Run: EVOA-59, raw outputs committed 0bfdfbf. Target: claim E5 (`docs/research/claims/E5-ara2-ara5-counts.md`), field `verdicts.external` (`pending`).

## Files and inputs
- `research/checks/results/raw/e5_external.out` (md5 efadb2c3f084a55c292176d7419d8cf8, 16 lines), `e5_external.json` (md5 bc70c46e3100d956fa23b1f7064d8089), `e5_external.host` (na-workhorse, 2026-11-26 07:59 UTC, research HEAD 090b04e, script commit 4cfe7e5, one process). The md5s of `.json`, `.out` and `e5_external.py` (50567901496f137e21c96051ef86fd2a at write-up time) match the `.host` record.
- Data: the 24 Good 2017 files fetched for L6 (`sources/raw/l6-good2017-data-2026-10-11/`, gitignored). The script asserts their sha256 against `raw/l6_data.sha256`, asserts Ara-2 F95 at 50K equals L6's 708, and asserts Ara+5's last time equals L6's 57,500. The run printed a BANDS line, so all three assertions passed.
- Disclosed, not blind: the docstring says L6 had already published Ara-2 F95 708 at 50K and Ara+5's last sample at 57,500 before registration. The unseen quantities were M_mid, D_min and E2 for Ara-2.

## Registered bands (docstring, verbatim in substance)
- Ara-2 cell: U2 no sample / assertion fails → untestable; C2 F95 ≤ 100 → biology (Day); M2 100 < F95 < 300 → indeterminate; B2 F95 ≥ 300 and D_min ≤ -906 → mixed; A2 F95 ≥ 300 and D_min > -906 → artefact. The 300 is the 3x RH band.
- Ara+5 cell: U5 no data → untestable; D5 sample within 500 of 60K and F95 ≤ 2 → biology; X5 such sample and F95 ≥ 3 → artefact; G5 no such sample and F95 at last sample ≥ 3 → artefact (missing sample read as 0); Z5 no such sample and F95 ≤ 2 → mixed.
- Verdict move: untestable if either cell is U; **supported if A2 and (X5 or G5)**; contradicted if C2 and D5; contested otherwise.

## Result (REGISTERED, as printed)
```
BANDS: Ara-2 A2 | Ara+5 G5 -> E5 external supported
```

| Cell | Quantity | Printed value | Band threshold | Band |
|---|---|---|---|---|
| Ara-2 (t50 = 50000) | F95 (Day's s3.2 rule, x ≥ 0.95) | **708** | ≥ 300 (not C2, not M2) | A2 |
| | M_mid (0.05 < x < 0.95) | 455 | (B2 needs ≥ 3,228) | |
| | M_lo (0 < x ≤ 0.05) | 915 | not a band input | |
| | E2 = Σ x(2x-1) | 820.9 | not a band input | |
| | D_min = F95 - M_mid/2 | **480.5** | > -906 → A2 | |
| Ara+5 | sample within 500 of 60K | **False** | → G5 or Z5 | G5 |
| | last/used sample | 57,500 | | |
| | F95 at last sample | **14** | ≥ 3 → G5 | |

R0 rebuild of Day's pair from -906 and the 4.2% sharing rate, printed: reading (a) S/(S+P): S = 87.1, P = 1986.2; reading (b) S/(S+P/2): S = 41.5, P = 1895.1.

Full printed per-population table at 50K (descriptive; only the Ara-2 and Ara+5 rows enter the bands):

| pop | F95 | M_mid | M_lo | E2 | D_min | Day clone-pair |
|---|---|---|---|---|---|---|
| Ara-1 | 265 | 1508 | 365 | 238.2 | -489.0 | 978 |
| Ara-2 | 708 | 455 | 915 | 820.9 | 480.5 | -906 |
| Ara-3 | 377 | 737 | 305 | 419.4 | 8.5 | 273 |
| Ara-4 | 885 | 553 | 55 | 1015.4 | 608.5 | 1153 |
| Ara-5 | 63 | 52 | 68 | 68.2 | 37.0 | — |
| Ara-6 | 24 | 100 | 12 | 47.6 | -26.0 | — |
| Ara+1 | 73 | 39 | 53 | 79.6 | 53.5 | 110 |
| Ara+2 | 55 | 9 | 5 | 57.7 | 50.5 | — |
| Ara+3 | 1169 | 1068 | 85 | 1151.0 | 635.0 | 932 |
| Ara+4 | 0 | 0 | 0 | 0.0 | 0.0 | — |
| Ara+5 | 14 | 100 | 8 | 38.2 | -36.0 | — |
| Ara+6 | 1592 | 1617 | 1085 | 1603.7 | 783.5 | 803 |

JSON `F95_late` (at 60K, or the last sample for Ara+5): Ara-2 730, Ara+5 14 (57,500); others in `e5_external.json`.

## Predictions scorecard (every registered prediction)

| Side | Registered prediction | Printed | Score |
|---|---|---|---|
| Day | Ara-2 F95(50K) near zero (C2, ≤ 100) | 708 | **MISS** |
| Day | The -906 "overshoots a real near-zero" | no near-zero: F95 708, D_min 480.5 | **MISS** |
| Day | Ara+5 "collapses entirely": a measured 0 near 60K (D5) | no sample within 500 of 60K; F95 14 at 57,500 (G5) | **MISS** |
| Day | Verdict contradicted | supported | **MISS** |
| Critic | Ara-2 had many near-fixed mutations, F95 ≥ 300 | 708 | HIT |
| Critic | The -906 comes from the correction (A2) | D_min 480.5 > -906 | HIT |
| Critic | Ara+5's 0 is not a measurement (G5 or X5) | G5 | HIT |
| Critic | Verdict supported | supported | HIT |
| Audit | F95 = 708, so not C2 or M2 | 708 | HIT (disclosed from L6; asserted) |
| Audit | M_mid < 3,228, so A2 | 455; A2 | HIT |
| Audit | 200 ≤ E2 ≤ 708 | **820.9** | **MISS** (above the upper bound by 112.9) |
| Audit | A random pair gives a positive count (E2 > 0) | 820.9 | HIT |
| Audit | Ara+5 G5 | G5 | HIT |
| Audit | Ara+5 F95 at 57,500 in 5-40 | 14 | HIT |
| Audit | Verdict supported | supported | HIT |
| Audit | Reachability: C2 ruled out; D5/X5 ruled out (no 60K Ara+5 sample) | F95 708; `t60_present` False | HIT (both disclosed in advance) |

Tally: Day 0 of 4; critic 4 of 4; audit 9 of 10 (the E2 range missed). The Day misses on C2 and D5 were fixed in advance by disclosed L6 data, so they are not new evidence against Day; they are recorded because they were registered.

## Proposed verdict move (proposal only; the field does not move here)
The docstring licenses **E5 `verdicts.external`: `pending` → `supported`** (A2 and G5). The combined review should rule on it together with the two points below; the operator integrates after that.

## Two points the review must weigh (from the E5 row's `next`)
1. **`contradicted` was unreachable on the disclosed L6 data.** It needed C2 (F95 ≤ 100) and D5 (a 60K Ara+5 sample at ≤ 2). L6 had already published F95 = 708 and a last Ara+5 sample at 57,500, and the docstring says so ("C2 needs F95 <= 100 (ruled out by L6, disclosed)"; "D5/X5 need a 60K Ara+5 sample (ruled out by L6)"). The reachable outcomes were `supported`, `contested` (via B2 or Z5) and `untestable`. Day's only live route was B2, which needed M_mid ≥ 3,228; it printed 455. The check could fail the critic side (B2, Z5), but it could not return Day's registered verdict.
2. **D_min omits M_lo and sub-detection clone-private load, which favours A2 over B2.** D_min = F95 - M_mid/2 assumes every ≥ 95% mutation is shared and only mid-frequency mutations are private. It leaves out the 915 M_lo mutations, the private mutations each clone carries below population detection (large in a ~100x mutator), and clones that lack some ≥ 95% mutations. All three push a real pair's count below D_min, so D_min is not a floor, and a pair that reaches -906 is more likely than the band test allows. The post hoc arithmetic below sizes this.

## Post hoc, descriptive (trivial arithmetic on printed values; not registered)
- Charging M_lo as private too: 708 - (455 + 915)/2 = **23.0**, still above -906 by 929.
- To reach -906 with all 708 near-fixed mutations shared needs P = 2(708 + 906) = 3,228 private mutations; detected non-fixed load is 455 + 915 = 1,370, so at least 1,858 more would have to be private and undetected. M_mid is 7.1x short of B2's 3,228.
- With Day's rebuilt private load (P = 1,895.1 or 1,986.2) and all 708 shared: 708 - 947.5 = **-239.5** and 708 - 993.1 = **-285.1**. Sub-detection private load at Day's own scale makes the count negative even when the pair shares everything near-fixed. It does not reach -906.
- The -906 needs Day's rebuilt S = 41.5-87.1 shared mutations. 708 mutations sit at ≥ 95% in the population, so the two clones together must lack at least 708 - 87.1 = 620.9 (reading a) or 666.5 (reading b) of them. A clone that lacks a ≥ 95% mutation belongs to the ≤ 5% without it. So the -906 needs either (i) a clone from a minority lineage (≤ 5%) that lacks most near-fixed mutations: real structure, the B2 "mixed" case, which D_min cannot see; or (ii) a shared count computed in a way that does not match the population calls (artefact). The run cannot tell (i) from (ii): the Tenaillon 2016 clone `.gd` files are not held.
- Day's "zero fixations" reading of Ara-2 (s5.2, "One in seven mutator populations -- 14% -- responded to supermutation by achieving zero fixations") against his own s3.2 rule on the population data: F95 = 708 at 50K and 730 at 60K. Under either (i) or (ii) the population did not have zero fixations.
- Day's clone-pair value / E2, the six other mutators: Ara+1 1.38, Ara+3 0.81, Ara+6 0.50, Ara-1 4.11, Ara-3 0.65, Ara-4 1.14; Ara-2 -1.10. Ara-2 is the only sign change; Ara-1 (978 against F95 265 and E2 238) is the only other ratio outside the 3x band. A pair can exceed the population's near-fixed count when both clones come from one clade (shared mid-frequency mutations), so single-pair counts track pair relatedness as well as fixation.
- Day's own numbers set against the printed F95: Ara+5 at 50K 14 (s4.1) = F95 14. The 60K non-mutator row Day sums (64 + 68 + 0 + 60 + 35, claim file "derived") against `F95_late`: Ara+2 64, Ara+4 68, Ara-5 60, Ara-6 35 all match; Ara+5 0 against 14 at 57,500. Every measured cell reproduces; only the unmeasured one does not (same finding as R4-E5E6, now on the data).

## What this settles and what it does not
- Settles, as registered: the Ara+5 "0 at 60K" is not a measurement. There is no sample within 500 of 60K, and the last sample (57,500) has 14 by Day's own rule. The Ara-2 population at 50K has 708 mutations at ≥ 95% by Day's own rule, so "-906 true fixations" is not the population's fixation state. The negative comes from the correction formula, which is unbounded below.
- Does not settle: why Day's Ara-2 pair shares only 41-87 mutations. A minority-lineage clone (B2 in substance) and a processing artefact (A2) both fit the printed numbers; the `.gd` files would decide. The A2 call rests on D_min, and point 2 above says D_min is not a floor.

## Who this helps

**Day side**
- The correction formula is not wrong in kind. Under a neutral SFS with n = 2, (P1+P2)/2 is the expected count of shared-but-unfixed sites, so the formula is right on average for an unstructured population (docstring). The -906 is the formula's faithful output for a pair with 4.2% sharing: R0 rebuilds a consistent (S, P) under both readings, and E5 internal `holds`.
- His data handling is accurate wherever there was data: his s3.2 rule reproduces Ara+5 at 50K (14) and four of five cells of his 60K non-mutator row exactly (post hoc).
- Ara-2 carries a large non-fixed load (M_mid + M_lo = 1,370, 1.9x F95). That fits his "permanently competing sub-populations" description, which this check neither tests nor refutes. The B2 route is open in substance: the pair's low sharing (S ≤ 87 against 708 near-fixed) is what a cross-lineage pair would show.
- Ara+5's decline from 38 (30K) to 14 (50K and 57,500) is real by his rule. Only the final 0 is unmeasured.

**Critic side**
- RE-10 ("A count of fixed mutations cannot be negative; the negative value comes from the paper's own correction"): supported. The formula is unbounded below, and the population's count by Day's own rule is 708 at 50K and 730 at 60K.
- RE-03 ("Their correction formula then produces minus 906 'true fixations' in Ara-2"): the -906 comes from the correction, not from the population state (A2 as registered; see point 2 for the caveat).
- RE-04 ("drops from 38 ... to zero at 60,000"): the zero stands where there is no sample (G5); the last sample, 2,500 generations earlier, has 14.
- All four critic predictions hit.

**Both / the audit's own errors**
- The audit's E2 range (200-708) missed: E2 = 820.9. The upper bound assumed E2 ≤ F95, which the definition does not imply, because mid-frequency mutations with x > 0.5 add positive terms. E2 is not a band input, so the verdict is unaffected, but the prediction was wrong.
- The design was disclosed, not blind, and `contradicted` was unreachable (point 1). The test was severe for the critic side only.
- The B2/A2 split rests on D_min, which assumes both clones carry every ≥ 95% mutation. R0's rebuilt S (41-87) says Day's pair did not, and the docstring computed R0 without using it in the bands (point 2; post hoc above).
- The printed Ara+4 row at 50K is all zeros (F95, M_mid and M_lo all 0), with 38 at 40K and 68 at 60K in L6's snapshot. That looks like an empty sample counted as present, the same mechanism as G5. It is outside both bands.

## Open
- Ara-2 Tenaillon 2016 50K clone `.gd` files (not held): only they can tell a minority-lineage clone (B2) from a processing artefact (A2). Getting them would need an owner-approved fetch.
- Whether `supported` should carry a scope note ("Ara+5 cell: missing sample; Ara-2 cell: not the population state, cause of low sharing unresolved") or the Ara-2 cell should read `contested` under point 2. That is for the review to rule.
- Ara+4's empty 50K sample: does Day's s4.1 Ara+4 50K cell read 0 for the same reason? This belongs to E6 or another node, not E5.

## Things that looked wrong
- The Ara+4 50K row prints 0/0/0 (above). It also suggests that `nearest()` accepts a sample with no coverage as present.
- The audit's E2 upper bound (above).
- D_min is called "the corrected count for the most divergent pair that the detected spectrum allows". It is the most divergent pair only among pairs that carry every ≥ 95% mutation and have no undetected private mutations. R0 and the mutator rate suggest neither condition holds.
- Ara-1's clone-pair 978 sits 3.7x above its F95 (265) and 4.1x above E2. Day's single-pair counts swing both ways around the population measure, not only downward in Ara-2.

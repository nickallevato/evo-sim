# R4-FMnull-S4: criterion S4 of FMnull (tree-incongruent sharing above the ILS rate), run post hoc

Status: **run, scored; reviews not yet done** (load-bearing tier: three reviews, run one after another under D-22).
Not integrated. No verdict field set here.

**Headline.** The governing aggregate is **`S4-MARGINAL`** on F2 (also on F3 and F0). Under the registration's VERDICT
MOVES this moves **no value**, is reported for **both sides as undecided**, and licenses **no defeater** in either
direction. FM3 and FM10 are untouched: FM10 internal stays `pending` (D-09), FM10 external stays `contested`.
**The aggregate rests on exactly one scored cell:** S4-R (`phi_R`, rate at matched density) at W = 1000 kb, value
15.925 against a FULL-band upper edge of 13.770 (`MARGINAL-OUT`). That reading was registered as expected to be wide
(P3), and its measured band width there is **9.54, over the registered non-discrimination threshold of 9** (section 5).
Every other scored F2 cell is `CRITIC`, `MARGINAL-IN` or `BELOW-NEAR`. **Severity limit (ST-10), qualifying everything
below:** S4 has no power against Q168's one-lineage block mechanism (P4, section 4), and on this run detects non-tree
two-lineage blocks only when they cover about half the genome (T4, T5); none of the S4 statistics tests the mechanism
Day describes, and Day has said nothing about tree incongruence.

Binding lead ruling: `research/checks/briefs/FMnull-S4-analyst.md`, "Lead ruling before the write-up (Big Sim,
2026-10-18, S4-R1..R8)", `7670832`. This write-up follows it. I think none of S4-R1..R8 is wrong. One factual detail
in S4-R6 (P6) is incomplete and is corrected in section 3 (it changes no call); see section 9, item W1.

## Provenance

- Registration (post hoc relative to FMnull): S4 text in `fm_mesa_null.py` `48241c7` (2026-10-12); operationalised in
  `research/checks/fmnull_s4.py`, `75743af` (2026-10-13); post hoc pre-run amendment `45f814d` (after the local smoke,
  no data and no full-size null seen: 1000 Mb per configuration, scoring guard, per-block yield). Docstring lines
  1-249 are the registration. Script md5 `a8f72e1e…c444fac` (computed now) equals the md5 in `raw/fmnull_s4.host`.
- Run: na-workhorse, 2026-10-18 07:39:32 to 20:43:27 UTC (`fmnull_s4.host`, `fmnull_s4.done`); chain realdata, sim
  `--procs 10 --mb 1000`, post. Full grid at the registered 1000 Mb, no fallback; 48 corners plus `central`, Q1, Q2,
  T1-T6. Peak worker RSS 333.9 MB. No error or traceback in any `fmnull_s4*.out`.
- Raw outputs committed `ef81a45`: `raw/fmnull_s4_{real,post}.{json,out}`, `fmnull_s4_sim.out`, `fmnull_s4_smoke.out`,
  `fmnull_s4.host`, `fmnull_s4.done`. md5s recomputed now on the workstation and equal to the `.host` record for all
  eight files. `fmnull_s4_sim.npz` (179,489,662 bytes, md5 `b126916e…71e9db` in `.host`) is not in git and was **not read**
  for this write-up; every number below is from `fmnull_s4_post.json` / `.out`, `fmnull_s4_sim.out` or
  `fmnull_s4_smoke.out`.
- Labels: **REGISTERED** = scored by `post` exactly as in the docstring. **Post hoc, descriptive** = computed or
  observed here beyond the printed outputs (marked each time). There are no AMENDED results.

## 1. Set-up check first (P6, P7): settled before any S4 number is read

**P6 (simulator set-up), REGISTERED: `hit: false`.** Brackets: span-weighted incongruent-topology fraction (2-Mb
pilot) in [0.20, 0.45]; full-exposure `a` in [0.40, 0.60]; `q-bar` in [0.15, 0.40]; every no-BGS corner and CENTRAL.

| Leg | Failing corners (value; margin) | Registration's own HAND value |
|---|---|---|
| topology floor 0.20 | `c_35k_35k_r1.0e-08_h0_bgs0` 0.1855 (0.0145 under, 7.2%) | 0.213 at N_HC 35k |
| topology ceiling 0.45 | `c_95k_35k_r1.0e-08_h1_bgs0` 0.4611 (0.011 over, 2.5%); `c_95k_55k_r1.0e-08_h1_bgs0` 0.4515 (0.0015 over, 0.3%) | 0.438 at N_HC 95k |
| q-bar ceiling 0.40 | the four `c_95k_55k_*_bgs0` corners, 0.4035-0.4056 (at most 0.0056 over, 1.4%) | ~0.29 at CENTRAL |
| `a` in [0.40, 0.60] | none (0.4986-0.5026 everywhere) | - |

The other five 35k corners read 0.2002-0.2354; CENTRAL reads topology 0.3476, `a` 0.5002, q-bar 0.3223. **Reading of
the miss:** both topology edges straddle the registration's own HAND values (0.213, 0.438), so the bracket was cut
too narrow around its own prediction; a 2-Mb pilot carries sampling noise of this size. A miss of this shape puts
the **bracket** in doubt, not the null. It is still a registered miss and is booked against the audit (section 8).

**P7 (data, F2 at 100 kb, descriptive), REGISTERED: `hit: true`.** mean n = 48.08 in [20, 60]; q-bar 0.3042 in
[0.15, 0.40]; a 0.4586 in [0.40, 0.55]. (HAND predicted n ~ 36, q-bar ~ 0.29.) k_used 9,520 windows.
No cell had rho capped (`rho_capped` empty in every F2, F3 and F0 cell).

## 2. Classes, F2 governing (REGISTERED; FULL band governs, N and U reported beside it)

Values are F2 data; band is FULL [N_lo, N_hi] (counts: [E_lo, E_hi]).

| W (kb) | phi_A | class | phi_R | class | M (HG+CG) | class |
|---|---|---|---|---|---|---|
| 10 | 1.489 [1.524, 3.145] | **BELOW-NEAR** | 3.353 [2.329, 5.681] | CRITIC | - | - |
| 30 | 1.784 [1.646, 4.131] | CRITIC | 5.014 [2.493, 7.743] | MARGINAL-IN | 2 (1+1) [0, 90.74] | CRITIC (NON-DISCR., width inf) |
| 100 | 2.111 [1.739, 5.242] | CRITIC | 7.519 [2.484, 9.184] | MARGINAL-IN | 0 [0, 9.35] | CRITIC (NON-DISCR., width inf) |
| 300 | 2.286 [1.758, 5.875] | CRITIC | 10.372 [2.480, 10.474] | MARGINAL-IN | - | - |
| **1000** | 2.654 [1.737, 6.901] | CRITIC | **15.925 [2.339, 13.770]** | **MARGINAL-OUT** | - | - |
| 3000 (reported only) | 2.646 [1.454, 7.874] | CRITIC (NON-DISCR.) | 27.940 [2.187, 18.456] | MARGINAL-OUT | - | - |

Band variants beside FULL (REGISTERED as reported, never scored):

| W | N (no BGS, 16 corners) phi_A / phi_R / M | U (no BGS, RHET 0, 8 corners) phi_A / phi_R / M |
|---|---|---|
| 10 | BELOW-NEAR / CRITIC | BELOW-NEAR / MARGINAL-IN |
| 30 | CRITIC / MARGINAL-IN / CRITIC | CRITIC / MARGINAL-OUT / CRITIC |
| 100 | CRITIC / MARGINAL-IN / CRITIC | CRITIC / MARGINAL-OUT / CRITIC |
| 300 | CRITIC / MARGINAL-OUT | CRITIC / MARGINAL-OUT |
| 1000 | CRITIC / MARGINAL-OUT (N_hi 9.979) | MARGINAL-IN / **DAY** (N_hi 5.007; 3 N_hi = 15.02 < 15.925) |
| 3000 | CRITIC / MARGINAL-OUT | MARGINAL-IN / DAY |

So on S4-R at 1 Mb the data lie above the upper edge of every corner in every band; the FULL edge is above the N edge
only because of BGS (13.77 against 9.98), and above the U edge because of BGS and recombination heterogeneity
(against 5.01). Both are UNSOURCED settings (sd(B), RHET). The U-band DAY is reported only and changes nothing.

**AGGREGATE (REGISTERED):** F2 `S4-MARGINAL`, F3 `S4-MARGINAL`, F0 `S4-MARGINAL`; governing `S4-MARGINAL`.

**Filters (S4-R7).** The governing outcome survives both the CpG filter and the alignment filter. Per-cell
disagreements, as registered: F3's phi_A at 1000 kb is **higher** than F2's (2.732 `MARGINAL-IN` against 2.654
`CRITIC`), the opposite direction from the registration's "F3 lower = CpG-dependent" gloss; F3's phi_R is
`MARGINAL-OUT` already at 300 kb (9.300 against N_hi 8.447). F0 is more extreme than both (1000 kb: phi_A 13.650
`MARGINAL-OUT`, phi_R 54.847 `MARGINAL-OUT`; mesa count 86 at 30 kb), which is the direction the registration predicted
for an alignment artefact; F0 is never scored.

## 3. Predictions P1-P7, scored as registered (misses with the same prominence as hits)

| P | Side | Registered prediction | Result | Hit? |
|---|---|---|---|---|
| P1 | critic | S4-A CRITIC or MARGINAL-IN at every scored W | BELOW-NEAR at 10 kb (1.489 < N_lo 1.524); CRITIC at 30-1000 kb | **miss** |
| P1 | Day (audit's steelman) | S4-A DAY at some W >= 100 kb | CRITIC at 100, 300, 1000 kb | **miss** |
| P1 | audit | phi_A in [1.5, 8] at every W, and phi_A(1 Mb)/phi_A(10 kb) <= 3 | 1.489 at 10 kb, under 1.5 by 0.011 (0.7%); ratio 1.78 held | **miss** |
| P2 | critic | S4-M neither DAY nor MARGINAL-OUT at 30 or 100 kb | CRITIC, CRITIC (M = 2, 0) | **hit** |
| P2 | Day (audit's steelman) | S4-M DAY at 100 kb | CRITIC (M = 0) | **miss** |
| P3 | critic | S4-R CRITIC or MARGINAL-IN at every W | MARGINAL-OUT at 1000 kb (15.925 > 13.770) | **miss** |
| P3 | Day (audit's steelman) | S4-R DAY at some W | none (max class MARGINAL-OUT) | **miss** |
| P3 | audit | FULL band width > 9 at W >= 300 kb | 6.40 at 300 kb (miss); 9.54 at 1000 kb (holds) | **miss** (partial) |
| P4 | none | Q1, Q2 move phi_A, phi_R < 10% and leave every class unchanged; M moves <= max(20%, 3) | phi legs and class legs held; M at 30 kb failed under both | **miss** |
| P5 | reachability | T5 DAY on S4-A at 1 Mb; T2 DAY on S4-M at 100 kb; T1 never DAY on S4-A; T4 MO or DAY on S4-A at 100 kb | 47.37 DAY; **CRITIC** (scaled 2.85); max 3.82 MI; 7.74 MO | **miss** (one leg) |
| P6 | set-up | brackets (section 1) | 7 corner-legs outside by 0.3-7.2% | **miss** |
| P7 | data | n, q-bar, a in brackets | 48.08, 0.304, 0.459 | **hit** |

The "Day side" predictions are the audit's steelman of S4 as a test of a fourth mechanism; Day has predicted nothing
about incongruence, so those misses are not Day's errors and are not scored against him.

**P1, one value, two misses (S4-R6).** The critic-side leg and the audit's leg both fail on the same number, F2 phi_A at
10 kb = 1.4894. The critic leg fails because it is BELOW-NEAR (under the lowest corner's lower edge 1.524, by 2.3%);
the audit leg because it is under the floor 1.5, by 0.011 (0.7%). Pre-registration binds, so both are misses; neither
is a substantive failure of either party. The BELOW-NEAR is a calibration flag ("Calibration or data flag; no item"):
the data's short-scale asymmetry clustering is slightly below what every ILS corner produces (section 9, W3).

**P2, the one clean critic-side hit, rests on infinitely wide bands (S4-R2b).** Every scored mesa cell has E_lo = 0, so
by the registration's counts formula the band width is infinite and the `NON-DISCRIMINATING` label attaches: F2 30 kb
(M = 2, band 0 to 90.7) and 100 kb (M = 0, band 0 to 9.3); the same at F3 (3, 0) and F0 (86, 1). No observed count
below the upper edge could have failed this `CRITIC`, so it is not evidence for the critic side, as the registration
anticipated ("if the CRITIC classes are NON-DISCRIMINATING, the item says so"). Nothing turns on it under S4-R1.

**P4 failed; the contingency fires (S4-R4), post hoc paragraph replacing the "no power against Q168" clause.** The
failure is only on the mesa count M at 30 kb: Q1 4.079 against a central 8.159 (raw 4 mesas on 23,575 eligible
windows), Q2 2.830 against 7.547 (raw 3 on 25,487), each outside max(20%, 3). Every phi leg held (largest move +6.4%,
phi_A at 1000 kb under both Q1 and Q2), and **no planted class differed from its central class anywhere** (all
`CRITIC` -> `CRITIC`). Direction: Q168 blocks move the mesa count **down**, to about half the central value. *Replacement
text (post hoc):* S4 has no measured power **for** Q168's mechanism; the one statistic that responds to Q168 at all
responds in the **wrong direction**, pushing S4-M toward the critic-side classes. A `CRITIC` on S4-M therefore remains
unreadable as evidence against Q168's mechanism, and on this run the registration's severity paragraph is
strengthened, not weakened. No value moves either way. (Caveat for the reviews: the shift rests on 4 and 3 mesas
against about 8; see W4.)

**P5: the conjunction missed; the thing it protected against did not happen (S4-R5).** `S4_unreachable_for_Day:
false`. T5 reaches DAY on S4-A at 1 Mb (47.37) and also on S4-M at 100 kb (scaled 52.2, raw 55) and S4-R at 100 kb;
T4 is MARGINAL-OUT on S4-A at 100 kb (7.74). The one failed leg: T2 (f 0.02, 300-kb blocks) is **CRITIC** on S4-M at
100 kb (scaled 2.85, raw 3 mesas, yield 0.045 per block); T3 projected from T2's yield: 0.71 mesas. So the conjunction
P5 is a registered miss, and Day's band is demonstrably reachable by a process of the registered kind; the S2-style
"criterion defect, unreachable for Day" clause does not fire.

**Power line, both ways (REGISTERED planted outputs, F2-thinned).** T1, T2, T3 and T6 (2%, 2%, 0.5% and 10% x 0.5 of the
genome in non-tree blocks) never reach `MARGINAL-OUT` on any statistic at any W; their highest classes are
`MARGINAL-IN` (e.g. T2 phi_A 5.57 at 1 Mb, T6 phi_R 12.38 at 1 Mb, T2 M 44 at 30 kb). Only T4 and T5 (half the genome)
reach `MARGINAL-OUT` or `DAY`. A `CRITIC` on S4 therefore excludes only non-tree sharing on the scale of half the
genome.

## 4. Severity, as registered and as measured

Registered: a DAY on S4-A or S4-M would have been severe; a CRITIC is discriminating only against non-tree processes
at least as large as the planted ones S4 is shown to detect, and never against Q168. Measured: S4 detects T4/T5
only (section 3, power line), and Q168 moves S4-M toward CRITIC (P4). No S4 outcome observed here tests the mechanism
Day describes.

## 5. Limitation of the criterion: `NON-DISCRIMINATING` is not defined for `MARGINAL-OUT` (S4-R3)

The registration attaches the `NON-DISCRIMINATING` label to `CRITIC` and `MARGINAL-IN` only, and the aggregate rule
discounts no wide cell. The one cell that makes the aggregate `S4-MARGINAL` (F2 phi_R at 1000 kb) sits on a FULL band
of width **9.54** (> 9). Had the label also covered `MARGINAL-OUT` and been discounted, the aggregate would read
`S4-NOT-MET`. That extension is a **rule change**, post hoc, and is **not made here**; anyone who wants it proposes it
through the freeze procedure in `DECISIONS.md`. It is **immaterial as to verdicts**: `S4-MARGINAL` and `S4-NOT-MET`
both move no value and neither licenses a defeater against FM10, so no side gains or loses from the gap. It is a
defect of the audit's own criterion and is booked there (section 8).

## 6. Post hoc, descriptive observations (no class, no verdict)

- **Rate without asymmetry.** On F2 at 1 Mb the data's phi_R (15.93) exceeds that of every T-scenario except T4/T5
  (T6 12.38, T2 10.38), while its phi_A (2.65) is below every T-scenario at 1 Mb (lowest T3 3.31). Planted non-tree
  blocks raise both statistics together; the data raise only the symmetric one. This is the pattern regional
  variation in the ILS rate gives (ancestral Ne or linked selection beyond the modelled sd(B) 0.32), not the pattern
  two-lineage blocks give. Descriptive only; the registration scores neither reading this way.
- `Spearman(q_w, H density)` on F2 rises with W from 0.46 (10 kb) to 0.66 (1000 kb).

## 7. Proposed effect on verdicts (proposals only; the integration, EVO-19, decides)

- **No value moves** (registration, S4-MARGINAL row). FM3: no change. FM10 internal `pending` (D-09), external
  `contested`: no change. **No defeater** in either direction; no argument-map item is licensed.
- Bookkeeping fixed by the registration: R4-FMnull's "S4 not run" becomes "S4 run post hoc (registered `48241c7`,
  operationalised in `research/checks/fmnull_s4.py`, `75743af`)", and `PREREG-STATUS.md` records it (it has no
  FMnull-S4 entry today).
- **Poisson GLM re-estimate: out of scope**, as accepted on 2026-10-13: S1 is a conjunction whose first clause
  ("index far above N_hi at EVERY plausible W") is unmet on raw phi under every parameter set (R4-FMnull section 7), so
  no covariate-adjusted value can make S1 met; and amendment A13 dropped covariate correlations as a critic-side
  criterion. `fm_bins.npz` was not re-read for it.

## 8. Who this helps

**Day's side**
- The governing outcome is `S4-MARGINAL`, not `S4-NOT-MET`: on the rate reading at 1 Mb the audit's own ILS null,
  across all 48 registered corners, does not contain the data (15.93 against 13.77), and under the narrowest band (U)
  the class is DAY (reported only).
- The governing upper edge at 1 Mb depends on two UNSOURCED settings (BGS sd 0.32 and RHET 1.0): without them the
  edge falls from 13.77 to 5.01.
- S4 is reachable for Day (P5): the criterion was not built so that he could only lose, unlike S2.
- P4: S4 cannot be used against sigillation as Q168 states it; Q168-type blocks push S4-M toward the critic classes,
  so a critic-side CRITIC on S4-M says nothing about Day's mechanism.

**Critics' side**
- S4-A, the literal "H and G but not C" reading, is `CRITIC` at every scored W from 30 kb up on F2; at 1 Mb it is far
  below what any planted non-tree scenario gives (2.65 against 3.31-47.37).
- P2 is a registered critic-side hit (no HG/CG mesas above the band), with the caveat that its band is
  non-discriminating.
- The one `MARGINAL-OUT` is on S4-R, the reading registered in advance as likely wide (P3), its band is over the
  width threshold, and the signal comes without asymmetry, consistent with regional ILS-rate variation (post hoc,
  section 6).
- P7 held: the data's incongruent site counts and share sit where a coalescent ILS model puts them.
- No statement of Day's is tested by S4 (he has made none about incongruence).

**Both / the audit's own errors**
- P6 brackets cut too narrow around the registration's own HAND values (seven corner-legs, 0.3-7.2% outside).
- P1 audit floor missed by 0.011; P3 audit width prediction missed at 300 kb (6.40); P5 predicted T2 would reach DAY on
  S4-M at 100 kb and it did not (CRITIC); P4 predicted M would not move and it halved.
- The audit's steelman predictions for Day (P1, P2, P3 Day legs) all missed; these are the audit's predictions, not
  Day's.
- Criterion design: `NON-DISCRIMINATING` undefined for `MARGINAL-OUT` (section 5); S4-M's bands are infinitely wide in
  every cell (E_lo = 0), so a CRITIC on M was never going to discriminate.
- **Tooling: the compute-sizing rule was falsified** (section 10).

## 9. Open, and things that looked wrong (for the reviews to rule on)

- **W1. S4-R6's description of P6 is incomplete.** It names one topology-ceiling miss (0.461); the raw output has two
  (also `c_95k_55k_r1.0e-08_h1_bgs0` 0.4515). It gives the 35k corners as "0.186-0.235 against a floor of 0.20"; only
  one of them (0.1855) is under the floor. The ruling's substance (registered miss, bracket in doubt, small margins)
  stands, and section 1 reports the raw values. Not a disagreement with the ruling.
- **W2. T4 and T5 mesas are all CG, none HG** (T4 30 kb: HG 0, CG 151; T5 100 kb: HG 0, CG 55), although the swapped
  tree ((H, G), C) adds HG-shared sites. The likely cause: with half the genome swapped, the genome share `a` that
  centres the excess rule is pulled up, so the *unswapped* windows read as CG-excess. If so the statistic works as
  registered (centred on the measured share), but its "direction" output is not interpretable at large f. Not
  checked (would need the npz).
- **W3. F2 phi_A at 10 kb is BELOW-NEAR** (1.489 under every corner's lower edge 1.524). Candidate causes the null
  omits: gene conversion (breaks short tracts), the bonobo constraint in iHG (b = c in the null), masking in blocks.
  Open.
- **W4. P4's direction rests on small counts:** 4 and 3 mesas against about 8 (paired seeds with CENTRAL). The registered
  tolerance is what fails; the size of the shift is not well measured.
- **W5.** F3's phi_A moves *up* relative to F2 at 1 Mb, against the registration's CpG gloss (section 2). Open.

## 10. Tooling finding: the compute-sizing rule (post hoc, descriptive; moves no number and no verdict)

The rule in the docstring ("the largest of 1000 / 500 / 200 Mb with a projection <= 8 h") projected from one host
smoke at 2 Mb: summed CPU 181.67 s x (1000 / 2) / 10 processes = **2.52 h** (`fmnull_s4_smoke.out`). The sim arm took
**46,482 s = 12.91 h** wall (`fmnull_s4_sim.out`, `wall_s`), **5.1x** the projection and over the 8-h ceiling the
rule existed to enforce. Summed CPU was 464,004 s (128.9 CPU-h; /10 = 12.89 h), so parallel efficiency was not the
cause: per-configuration CPU grew **2,554x** for a 500x genome.

Cause (post hoc, from the outputs and the code): `sim_chunk` simulates a no-BGS configuration as one msprime segment
per chunk (`seglen = L` when `bgs` is None; chunk = min(10 Mb, L)). The 2-Mb smoke therefore ran 2-Mb segments, the
run 10-Mb segments, and coalescent-with-recombination cost grows faster than linearly in segment length. BGS corners
simulate segments of length ell (0.2 or 2 Mb) in both, and scaled about linearly (267-821x); no-BGS corners scaled
2,193-9,548x and CENTRAL, Q1-Q2, T1-T6 (all no-BGS) 3,467-5,205x. The aggregate 5.1x matches the 5x change in
segment length. Individual ratios are noisy (smoke times of 1-8 CPU-s).

**Does it bear on the result? No.** The extra time is the registered simulation at the registered segment length:
`meta.chunk_bp` = 10,000,000 and `meta.mb` = 1000 in `fmnull_s4_post.json`, the script md5 equals the `.host` record,
P7 held, and P6's misses are at bracket edges (section 1). **Replacement rule:** the lane's two-point rule (two smoke
sizes, measured scaling, hard wall-clock ceiling, sizing basis in `.host`; applied to L3) is right, with one addition
this run shows: at least one smoke point must use the **production segment / chunk length**, because scaling measured
below it does not carry across a change in per-segment cost. Re-cut before `fmnull_s4.py` is launched again.

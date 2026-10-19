# REVIEW R4-FMnull-S4: correctness

Reviewer: fresh reviewer instance (Paperclip EVO-17), 2026-10-19. Skill: `review-correctness`. I did not author any of this work.
Under review: `research/checks/results/R4-FMnull-S4.md` (`d0c94e2`), against the registration (`fmnull_s4.py` docstring
lines 1-249, `75743af`, post hoc pre-run `45f814d`) and the binding lead ruling S4-R1..R8 with S4-R6a / S4-R6b
(`research/checks/briefs/FMnull-S4-analyst.md`, `7670832`, `988394e`).
Inputs recomputed: `raw/fmnull_s4_post.json`, `fmnull_s4_post.out`, `fmnull_s4_sim.out`, `fmnull_s4_smoke.out`,
`fmnull_s4.host`. The npz was not loaded (md5 only). Local work: one `python -I` process per step, seconds, under 100 MB.

## What I recomputed and found right

- **Run integrity.** Script md5 `a8f72e1e1823df783968cda73c444fac` is the same as the `.host` record. The script is unchanged since `45f814d`.
  All eight `.host` md5s match, including `fmnull_s4_sim.npz` `b126916e…71e9db`. Order: registration 2026-10-13 22:03, post hoc 22:05,
  launch 2026-10-18 07:39:32, `.done` 20:43:27, collect `ef81a45`, ruling `7670832` 22:43, write-up `d0c94e2` 2026-10-19 01:25.
  `meta.mb` = 1000, `chunk_bp` = 10,000,000, 57 configurations. `rho_capped` is empty in all 18 cells.
- **Classes.** I re-derived every class from the data values and the band edges with the registered formulas (classify2
  with N_c, and the count rule with its Poisson clause). That covers 18 cells (F2/F3/F0 x 6 W) x 3 band sets (FULL/N/U), phi_A, phi_R and M: **0 mismatches**. Widths, the
  NON-DISCRIMINATING flags and the aggregates (F2, F3 and F0 all `S4-MARGINAL`) all reproduce. On F2 the only `MARGINAL-OUT` in `WS` is
  phi_R at 1000 kb, which confirms S4-R2.
- **Tables.** Every number in sections 1-3 is correct. That includes the band-variant table (N/U classes, N_hi 9.979, U_hi 5.007), the F3/F0 values in S4-R7,
  the mesa counts (F2 2/0, F3 3/0, F0 86/1) and E_hi 90.74/9.35. P1-P7 match the JSON: the P1 margins are 2.28% and 0.71%, the ratio
  is 1.782, the P3 widths are 6.401/9.536, and the largest P4 phi move is +6.40%.
  P5: T5 47.37, T2 scaled 2.85, raw 3, yield 0.045, T3 projection 0.712, T1 max 3.82, T4 7.74. P6 margins are 0.3-7.2% over seven legs. P7 is 48.08/0.3042/0.4586 on k 9,520.
  The power-line and section-6 values are also right (T2 phi_A 5.57, T6 phi_R 12.38, T2 phi_R 10.38, T3 phi_A 3.31, Spearman 0.462 -> 0.660).
- **S4-R6a is confirmed.** The ceiling is exceeded by two corners (0.46113 and 0.4514685), the floor by one corner (0.185519), and q-bar by four corners (0.4035-0.4056). That is seven legs.
- **Section 10 tooling numbers are confirmed.** Smoke sum 181.67 CPU-s over 57 configurations gives a projection of 2.52 h. Run sum 464,004 CPU-s; wall 46,482 s.
  The overall ratio is 2,554x. By group: BGS 267-821x, no-BGS corners 2,193-9,548x, CENTRAL/Q/T 3,467-5,205x.
- **Bookkeeping.** `PREREG-STATUS.md` and `R4-FMnull.md` have no FMnull-S4 entry yet, as section 7 says.

## Findings

**1. MAJOR: the registered pairing of the planted runs with CENTRAL's thinning draws is not realised in the code. As a result, P4's
mesa-count shift and its "direction" cannot be attributed to Q168. I think the direction sentence of S4-R4 is wrong in
its factual basis, and I stop at saying so.**
- Registration, docstring line 99: "planted runs also share CENTRAL's thinning draws". The code seeds the planted
  thinning with CENTRAL's seed (`fmnull_s4.py:730`, `seed_of(seed, base, key)` with `base = "central"`). It then draws
  `rng.binomial(win[:, j], pthin)` field by field in `SF` order, H first (`:607`). The planted H counts differ from
  CENTRAL's in block windows (`:391-392` extra_H, `:452-454` modified h). numpy's `Generator.binomial` uses a variable
  number of uniforms per draw (BTPE and inversion restarts), so the stream desynchronises at the first block window. Every
  later draw in every later field (HCs, iHG, iCG) is then effectively independent of CENTRAL's. I checked this locally with numpy 2.5.3,
  the pinned version. Two arrays of 33,300 binomials, same seed, n differing in 2% of entries: in the next field, whose inputs are
  identical, only 6.4% of draws agree, which is the chance rate for independent draws.
- So the comparison "Q1/Q2 against central" is paired in the coalescent simulation and **unpaired in the thinning**.
  At 30 kb, S4-M is dominated by thinning noise: mean n per window is 13.4, and a mesa needs three adjacent windows with |x/n - a| >= 0.30.
- Q1 has no mechanism for the shift. It covers f = 0.02 in 100-kb blocks and leaves the genome share unchanged
  (0.4996 against 0.4994 at 30 kb). The chance that a given central mesa of at least 90 kb overlaps a block is about 0.02 x 190/100, about 0.04, so roughly 0.3 of
  the 8 central mesas could be touched at all. Q1 nonetheless reads 4 (HG 2, CG 2) against central 8 (HG 1, CG 7).
  For one independent draw, P(Poisson(8) <= 4) = 0.10. Q2 does have a real effect: full-exposure a falls from 0.5002 to 0.4774 and n_mean rises 7.7% (see N2).
  That effect could plausibly lower M, but on this run it cannot be separated from thinning noise.
- Consequences:
  - P4's registered `hit: false` stands as the code computed it; pre-registration binds.
  - S4-R4's "Q168 blocks move the mesa count **down**" and the write-up's statements resting on it are not supported for Q1 and are unestablished for Q2.
    Those statements are at lines 132-135 ("responds in the **wrong direction**"), line 156 ("Q168 moves S4-M toward CRITIC") and line 199 (Day bullet).
  - W4's "paired seeds with CENTRAL" (line 237) is true of the simulation and false of the thinning.
  - The severity paragraph does not need the direction claim. "No measured power against Q168" stands on the class legs, which held in full.
- Fix:
  1. The lead amends the direction sentence of S4-R4.
  2. The fix pass rewrites lines 128-137, 156 and 199 as "the registered M tolerance failed; the shift is within
     independent-thinning noise (Q1) or not separable from it (Q2); no class moved".
  3. Correct W4.
  4. Book the unpaired thinning as a code-versus-registration defect.
  5. Optional post hoc: rerun `post` (it needs the npz, so on a host, not locally) with one RNG stream per field and per window, for example
     `SeedSequence.spawn` or uniform-comparison thinning, labelled post hoc.

**2. MINOR: the P6 reading explains only the topology leg.** Lines 50-53 attribute the miss to "a 2-Mb pilot carries sampling noise of this size".
That holds for topology, which comes from `meta.pilot`. The topology values of nominally equivalent corners
spread about 0.05 (for example 0.1855-0.2174 at 35k/35k), which supports the noise reading. But `a` and q-bar come from the full 1000-Mb
run (`full_exposure_100kb`, `fmnull_s4.py:705-712, 886-892`). The four `c_95k_55k` q-bar values cluster at 0.4035-0.4056, which is the
corner's systematic value, not noise. The HAND row cited for that leg (line 47, "~0.29 at CENTRAL") is not a straddle.
Fix: add one sentence. The q-bar ceiling of 0.40 was set without a HAND value at N_HC 95k / N_HCG 55k and is simply below that corner's expected q-bar.
The bracket, not the null, is still what is in doubt.

**3. MINOR: one registered label is missing and one filter disagreement is over-read.** F3's phi_A at 1000 kb is `MARGINAL-IN` **and NON-DISCRIMINATING**
(FULL width 10.16), and so is F3 at 3000 kb (21.16). Section 2 (line 90-91) and W5 report the class without the label. The value
difference F3 - F2 is +0.078 (2.732 against 2.654), 0.3 of the data jackknife SE (0.26 F2, 0.24 F3). The class difference comes from F3's lower band
(N_hi 5.567 against 6.901; centre 2.43 against 3.09), not from the value "moving up".
Fix: add the label. Restate W5 as a band-driven class change with a value change of less than one SE.

**4. MINOR: the critic-side comparison to planted runs needs its qualifier.** Line 203-204 ("far below what any planted non-tree scenario gives
(2.65 against 3.31-47.37)") and section 6 compare the data with planted runs on **CENTRAL** demography (central phi_A 2.34 at 1 Mb). The
governing band at 1 Mb runs from 1.74 to 6.90. Measured as increments over central, T3 is +0.97 and T1 is +1.48; added to a low corner, these land
near the data, not "far" from it. This is also in tension with line 149 ("A CRITIC on S4 therefore excludes only non-tree sharing on the scale of
half the genome"). Fix: label both as "relative to CENTRAL, post hoc, not an exclusion under the registered classes".

**5. MINOR: S4-R6b is confirmed.** Line 50: "The other five 35k corners" should read "seven". There are eight no-BGS N_HC 35k corners and one fails. The range
0.2002-0.2354 (0.2001565-0.2353725) is right.

**N1. NOTE: W2 can be resolved from the JSON.** The thinned genome share in T4/T5 is a = 0.716-0.721 (30 and 100 kb; full exposure 0.721/0.718)
against 0.50 at central. Unswapped windows therefore sit at dev of about -0.22, and all T4/T5 mesas are CG, as W2 guessed. So T5's S4-M `DAY` at 100 kb is
built from unswapped windows. This does not touch P5's reachability, whose DAY leg is T5 on S4-A. Fix: replace "Not checked (would need the npz)".

**N2. NOTE: the sign of the HAND Q168 term is wrong.** HAND (docstring lines 231-233) has Q168 adding iHG, which would raise the share in blocks by about 0.02 under Q2.
Observed at full exposure under Q2: a 0.5002 -> 0.4774 (a fall of about 0.046 inside blocks) and q-bar 0.322 -> 0.338. Extra H changes create iCG, plausibly at
h == c == g != o sites, faster than iHG. P4's phi legs held anyway. Fix: one line among the audit's own slips (section 8).

**N3. NOTE: a wording slip in the P2 paragraph.** Line 125 says "No observed count below the upper edge could have failed this `CRITIC`". A count in (30.2, 90.7] at 30 kb
or (3.1, 9.35] at 100 kb would have been `MARGINAL-IN`. What no such count could fail is **P2**. Fix: "could have failed P2".

**N4. NOTE: the margin of the governing cell, for readers.** F2 phi_R at 1000 kb exceeds N_hi by 2.155, which is 1.67 times its data jackknife SE
(1.290). The registration does not use the data SE, so nothing changes. It may be worth stating beside the headline for both sides.

**N5. NOTE: an immaterial scaling inconsistency.** The planted `central_scaled` uses the planted run's eligible-window scale (`fmnull_s4.py:781-782`), giving 8.159 and 7.547 for the
same raw 8. On central's own k_elig (23,519) it is 8.178. P4's M legs fail either way: |4.079 - 8.178| = 4.10 > 3 and |2.830 - 8.178| = 5.35 > 3.

## Verdict moves

The proposal (no value moves, no defeater, FM10 internal `pending` under D-09, external `contested`, FM3 untouched, no `verdict_scope`
move) is exactly what the registration's `S4-MARGINAL` row licenses, and the aggregate reproduces. No finding changes it.

## Counts and wrong numbers

BLOCKER 0, MAJOR 1, MINOR 4, NOTE 5.
Wrong numbers (old -> right): line 50, "five" 35k corners -> "seven". No other number in the write-up is wrong. Finding 1 concerns
an attribution (direction), not a printed value.

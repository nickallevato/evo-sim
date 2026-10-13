# Review 1 of 3 (correctness): R4 L2, a sourced hardness h for humans

Reviewer: `reviewer` agent (Opus), fresh instance, task EVO-45; did not author the registration (`ade0542`), the run
(`1d9a32f`) or the write-up (`8d17245`). Date 2026-10-13. Skill: `review-correctness`. Tier: load-bearing (three
reviews). No lead suspicions were given beyond the write-up's own W1-W6; I treated those as a starting list.

## What I recomputed (and it matched)

- **Run integrity.** md5 of the script, smoke output, inputs, screening log, quotes and main output recomputed: all six
  match `l2_main.host` / `l2_smoke.host` and the write-up's table. `git diff ade0542 HEAD -- research/checks/l2_hardness.py`
  is empty. Order: registration `ade0542` 22:17:59 UTC, smoke `5591022` 22:18:09, S2 queries 23:13, fetched-file mtimes
  23:17-23:22, `main` 23:36:28, run commit `1d9a32f` 23:36:40, write-up `8d17245` 23:42:14. Every source was fetched after
  the registration.
- **Re-run of `main`** on the committed inputs (workstation, stdlib arithmetic, < 1 s, output to scratch): identical to
  `raw/l2_main.out` except the timestamp line. Smoke re-run: "13 of 13".
- **Source hashes.** sha256 of the six admitted fetched files (C0211, C0848, C0821, C0212, C0136, C1440) and the two
  search files (EPMC Qb3, OpenAlex Qb3) recomputed under `sources/raw/l2-2026-10-13/`: all match `l2_quotes.md` and
  `l2_inputs.json`.
- **Quotes against the raw text** (pdftotext -layout / tag-stripped XML, to scratch): L2Q-01, -04, -08, -14, -15, -16,
  -17, -20, -21, -22, -23 found verbatim at the stated places, with the values entered.
- **Every h value.** All ten route (b) records recomputed with h = Im / (Im + If/Ps): 0.6232, 0.5629, 0.2839, 0.6410,
  0.4391, 0.4800, 0.6273, 0.2912, 0.3236 (Crow), Utah 0.333 (episodes). Route (a): gamma -0.028 +- 1.96 x 0.0006 through
  the source's formula gives T = 9.989 and 12.731 years, h = 0.1247 (G = 30) and 0.2564 (G = 25). G = 25 line
  [0.176, 0.256] and G = 30 line [0.125, 0.195] confirmed. Point half-life 11.35 years (P6).
- **Scoring.** Every call in the predictions table matches the registered wording and the script: PD miss, PD-w hit,
  PC miss, PC-w miss, PA-1 hit, PA-2 hit (by the registered "or is not retrievable" clause; vacuity correctly disclosed),
  PA-3 hit, PA-4 miss, PA-5 hit. Band B-MH: 0.1 <= 0.125 < 0.3 <= 0.641. DISJOINT: 0.256 < 0.284.
- **Counts.** 39 records, 11 eligible, 28 E2 false; screening log 1,486 data rows (1,301 T-excluded, 78 A-excluded,
  9 F-excluded, 8 admitted, 20 entered-E2false, 62 F + 4 S1 unavailable = 66 = 59 screening ids + 7 bib ids on the owner
  list). Route (b) 10 records from 7 sources; 8 of 10 >= 0.3.
- **Post hoc arithmetic** P1 (point values), P2, P4, P5 (0.651), P6 and the Courtiol 2013 figure (5.20e-2 / (5.20e-2 +
  5.57) = 0.0092) all reproduce.
- **HF multiples** used in the placement sentence ("about 1.3-1.7x", "2.6-3.5x at R = 1.111", "0.83x and 1.05x",
  "1.9x and 2.8x") are present in `R4-HF.md` (asserted by the script; D1 and D4 there).

## Findings

### MAJOR-1. The route (a) specification is reading-dependent, and one reading the source supports flips PD-w

Evidence. The registration (E-paragraph): "the one its authors call main or preferred; if none is designated, all of
them (union)". Write-up W3 frames the choice as column 2 versus the union of all SUR columns. The source has a third,
textually closer reading. C1440, section on data (pdftotext line 687): "As discussed in depth below, the baseline
regressions are restricted to 9 countries and the periods 1470-1870 and 1600-1870 to ensure that our results are based
on data of the best quality." Table 3 column 4 is exactly that second baseline (9 countries, 1600-1870, SUR, gamma
-0.032, robust SE 0.0006, L2Q-21). Against it, the Table 3 text (lines 1181-1189) calls 1470-1870 "the baseline period"
and converts only column 2 to a half-life. So:

| Reading of "main" | Route (a) (registered interval rule, +-1.96 SE, G in [25, 30]) | Governing | Band | PD-w | PA-4 | DISJOINT | Verdict value |
|---|---|---|---|---|---|---|---|
| R-a1 column 2 (as run) | [0.125, 0.256] | [0.125, 0.641] | B-MH | hit | miss | True | no move |
| R-a2 baseline pair, columns 2 + 4 (line 687) | [0.005, 0.256] | [0.005, 0.641] | B-LH | **miss** | miss | True | no move |
| R-a3 none designated, union of SUR columns 2-7 (column 3 clipped to 0, as registered) | [0, 0.471] | [0, 0.641] | B-LH | **miss** | hit | False | no move |

(Post hoc, this review. Column 4 with its SE: 1 + gamma T in [0.0047, 0.0754], h in [0.005, 0.116].)

The write-up scores PD-w as a clean hit, tallies the Day side "1 of 2", and its first Day-side bullet says "no eligible
pre-transition record, on either route, puts human h below 0.1". All three rest on R-a1 alone. R-a1 is the more
defensible reading of Table 3's own text, so I do not ask for the governing reading to change; but the score is
reading-dependent and must be reported as such.

Fix. (i) Keep R-a1 as the scored reading; add the table above (or its rows) under "Predictions, scored" and mark PD-w
"hit (reading-dependent: miss under R-a2 and R-a3)", with the tally "Day side 1 of 2 under R-a1, 0 of 2 under R-a2/R-a3".
(ii) Rewrite Day-side bullet 1 so the "not below 0.1" statement is conditioned on column 2, and cite line 687 in W3.
(iii) State that no reading of the specification clause moves a verdict value (verified above).

### MAJOR-2. Run-time rule R-E2 deletes half of the registered E2 criterion, and the write-up reports only the downward sensitivity

Evidence. Registered E2: "pre-transition: natural fertility **and** pre-modern mortality". The screening-log header,
R-E2: "Pre-reproductive mortality is deliberately NOT used to judge E2 (it is the numerator of h)." So the run task
removed the mortality conjunct, with a reason (circularity) that has merit, but it is a departure from the registration,
not an operationalisation of it. The write-up's "Run-time rules" paragraph lists R-E2's fertility test without saying
that it drops a registered condition, and P2 explores only relaxations that lower route (b) (Santa Rosa, Koraga,
Kodava, ...). The direction of the dropped condition is the opposite one: h = Im / I_tot rises with Pd, and the three
eligible records with the lowest pre-reproductive mortality are exactly the route (b) minimum and its neighbours
(Pd = Im / (1 + Im): Cerro Policía 0.099, Chañarcito 0.115, Olacapato 0.091; Goicoechea's Pd is "Before 15 years old").

Post hoc, illustrative cut only (this review): excluding the records with Pd < 0.15 gives route (b) [0.333, 0.641];
band still B-MH, DISJOINT still True, PA-3 still a hit. No verdict value moves. I do not assert a pre-modern mortality
level from memory (rule 8); any threshold must come from a fetched source or the owner.

Fix. In "Run-time rules", say explicitly that R-E2 drops the registered mortality conjunct and why. Add to P2 the
upward sensitivity (the mortality conjunct applied by an external, non-Pd marker, or at minimum the illustrative cut
above, labelled post hoc), so that both directions of the E2 choice are reported side by side.

### MAJOR-3. The proposed H8 placement sentence asserts an untested in-model result

Evidence. Proposed text: "Term 3 holds in-model within R1 at the upper end of the sourced interval and is exceeded by
more than R1 toward its lower end; the sourced interval spans the line." The interval's lower end is 0.125. The only
tested points are h = 0.1 (Term 3 exceeded: 1.9x on the registered estimator, 1.36x on the strict tie reading) and
h = 0.3 (0.83-1.05x, within R1). Under the assumed monotonicity the R1 crossing lies somewhere in (0.1, 0.3); it may
lie below 0.125, in which case Term 3 holds within R1 over the whole sourced interval and the interval does not span
the line. The registration licenses only "the placement sentence (interval, in-model multiples at its ends)", and the
multiples at 0.125 are not known. This text is proposed for a load-bearing claim file.

Fix. Replace with: "The lower end (0.125) lies between the tested points h = 0.1 (Term 3 exceeded by 1.36-2.8x) and
h = 0.3 (0.83-1.05x, within R1); whether Term 3 is exceeded by more than R1 anywhere inside the sourced interval is
untested. At the upper end Term 3 holds within R1 (monotone in h assumed)." Make the same check of the H/H5 sentence
(it is already worded as "between ... and ...", which is correct).

### MINOR-1. "All seven S1 candidates" miscounts the registered list

The registration's S1 names eight candidates (five route (b), three route (a)). Seven were unavailable; Courtiol 2013
(C0142) was fetched and excluded. Line 40 ("All seven S1 fixed candidates were unavailable") and line 209 ("All seven
S1 candidates were unavailable") should read "Seven of the eight S1 candidates".

### MINOR-2. The post hoc route (a) intervals in P1 and W3 drop the standard errors the registered interval rule uses

P1 and W3 map point gammas only; the registered rule is "+-1.96 SE mapped through the formula at its ends", and column
3 is to be "clipped and flagged ... not dropped". With the SEs of L2Q-21: column 4 [0.005, 0.116] (not [0.040, 0.068]);
column 5 [0.112, 0.203]; column 6 [0.106, 0.210]; column 7 [0.335, 0.471] (not [0.370, 0.437]); column 3, 1 + gamma T
= -0.02, enters as 0 (clipped). W3's union "[0.040, 0.437]" becomes **[0, 0.471]** ([0.005, 0.471] without column 3).
No band conclusion of W3 changes (B-LH, no value move). Fix: either label the P1 figures "point gamma, SE omitted" or
replace them with the SE versions; correct W3's union.

### MINOR-3. Route (b)'s minimum and the DISJOINT gap are stated more precisely than the inputs allow

Inputs carry two decimals; values are printed to three. Rounding alone (each component +-0.005) puts Cerro Policía in
[0.272, 0.296] and Chañarcito in [0.281, 0.302]. Albeza 2002 prints the shares directly (L2Q-15: If/ps "representando
el 72,23 % del Índice total" for Chañarcito; 80.64% Santa Rosa; 65.57% Olacapato), which give h = 0.278, 0.194 and
0.344, more precise than the derived 0.291, 0.205 and 0.324. On the printed share, Chañarcito (0.278), not Cerro (0.284),
is the route (b) minimum and the gap to route (a) is 0.022, not 0.028. DISJOINT survives rounding (0.272 > 0.256) and no
band changes. Fix: keep the registered computation as the scored one (the `crow` stat takes Im, If, Ps), add one post hoc
line with the printed shares and the rounding range, and correct "gap 0.028" and P2's Santa Rosa figure (0.205 derived,
0.194 printed).

### NOTE-1. Ruling asked for in Open 3 (dynamic-panel bias, overlapping windows): keep it Open

The source states "We estimate (11) and (12) in 30-year overlapping intervals" (C1440 line 665), with a Kmenta AR(1)
error correction; overlapping windows induce a longer serial dependence than AR(1), so the robust SE 0.0006 is plausibly
too small. The spread of the authors' own SUR columns (gamma -0.021 to -0.034) is about 22 times column 2's SE. The
direction of the fixed-effects bias claimed in the Day-side bullet is the standard one, but the authors also state that
the no-fixed-effects OLS estimate is "biased towards zero" (L2Q-22), i.e. the true persistence plausibly lies between
column 2 (0.16 per 30 years) and column 1 (0.94). Neither is quantifiable without the data, so it is an Open item, not a
NOTE; the "most likely bias runs Day's way" bullet should cite both bounds.

### NOTE-2. Rulings on the analyst's other flags

- **W1 (Utah).** Admitted correctly under registered E3 (L2Q-19: first-year survival enters). The survival share covers
  all ages and fitness is lambda, so under M-b1 the record is biased upward; it sets neither end. No change needed beyond
  the existing flag.
- **P3 (Courtiol 2013 excluded).** Correct under the registered stat list: annual-fitness variance components are not
  lifetime episode opportunities. "About 0.01" verified (0.0092).
- **W4 (Slovincian).** Verified: printed If 0.17 = Vf / x̄² (7.93 / 6.75² = 0.174), standard; only the printed I column is
  non-standard. 0.651 with Ps 0.69 confirmed.
- **W5.** Agreed: the registered script does not print the "no uncertainty" flag its own docstring promises; no number is
  affected. Correct as the write-up already does.
- **W6.** Not a correctness matter; left to the critic-side steelman.

### NOTE-3. "No E2 decision can move the band" (P2) is too broad as worded

Admitting any of the post-transition records below 0.1 (Lucknow, Ingush, Zapotec 2000) gives B-LH. The true statements
are "no E2 decision on the arguable records moves the band" and "no E2 decision of any kind moves a verdict value".

### NOTE-4. Provenance table omits the smoke commit

`raw/l2_smoke.out` and `.host` were committed in `5591022` (22:18:09), ten seconds after the registration; add it.

### NOTE-5. Stress test: what it takes to reach a moving band

I searched the combinations above for any that reach B-HH or B-LL. Only one does: route (a) = column 7 alone (3
countries, 930-1870, [0.335, 0.471]) together with the mortality cut of MAJOR-2 (route (b) [0.333, 0.641]) gives
governing [0.333, 0.641], B-HH. Column 7 alone is not a defensible reading of the specification clause (it is a
robustness sample), so this is reported for completeness, not as a reading. B-LL is unreachable: every route (b)
reading keeps hi >= 0.641.

## Verdict

The registered result reproduces exactly: B-MH, DISJOINT, no verdict value move on H, H5 or H8, every score as printed.
No BLOCKER. The no-move conclusion holds under every reading I examined (the three specification readings, E2 relaxed
or tightened, rounding). The three MAJORs concern reporting: a reading-dependent Day-side hit presented as clean, a
registered criterion dropped at run time and probed in one direction only, and a proposed H8 sentence that claims an
untested result.

**Counts: 0 BLOCKER, 3 MAJOR, 3 MINOR, 5 NOTE.**

## Wrong numbers (old -> right)

| Where | Old | Right |
|---|---|---|
| lines 40, 209 | "All seven S1 (fixed) candidates were unavailable" | seven of the eight S1 candidates were unavailable |
| P1, column 4 | [0.040, 0.068] | [0.005, 0.116] with +-1.96 SE (point gamma: [0.040, 0.068]) |
| P1, column 7 | [0.370, 0.437] | [0.335, 0.471] with SE |
| P1, columns 5 and 6 | [0.130, 0.183] | [0.112, 0.203] and [0.106, 0.210] with SE |
| W3 union of SUR columns | [0.040, 0.437] | [0, 0.471] (column 3 clipped to 0); [0.005, 0.471] without it |
| DISJOINT gap (line 86, P2) | 0.028 (0.256 to 0.284) | 0.028 on the registered computation; 0.022 on the source's printed shares (Chañarcito 0.278) |
| P2 Santa Rosa | 0.205 | 0.205 derived; 0.194 on the printed share |
| H8 placement | "exceeded by more than R1 toward its lower end; ... spans the line" | untested at 0.125 (MAJOR-3) |

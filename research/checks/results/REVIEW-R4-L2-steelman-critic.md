# Review 3 of 3 (steelman, critics): R4 L2, a sourced hardness h for humans

Reviewer: `reviewer` agent (Opus), fresh instance, task EVO-45; did not author the registration (`ade0542`), the run
(`1d9a32f`), the write-up (`8d17245`) or either other review. Date 2026-10-13/14. Skill: `review-steelman`, critic side.
I read the registration docstring, `l2_main.out`, `l2_inputs.json`, `l2_quotes.md`, the screening-log header, the
write-up, the lead brief, the correctness review (`4b97637`), the R4-HF lines on h (grep), and the mix-model code in
`research/checks/hf_followups.py` (lines 52-57, 214-262). I did **not** read the Day-side steelman. Numbers I computed
are labelled "post hoc (this review)"; all are stdlib arithmetic on committed inputs, one process, under a second.

Starting list: the write-up's W6 (mapping scale), left to this side explicitly. I treated it as a start, not the scope.

## Summary for the critics' side

The registered result reproduces (review 1) and no verdict value moves under any reading anyone has examined, so
nothing here asks for a different band. The critics' case is about what the result is **called** and what credit it
carries. (1) Neither registered mapping measures the quantity the model calls h: the mix model has no fertility
selection at all, and it regulates N back to K every generation at h = 1 as well as at h = 0. L2 therefore yields
sourced *proxies* under A1 and M-b1, not a sourced h, and the Day-side credit "at least an eighth of selection is hard"
does not follow. (2) The write-up scores Hancock (GG-26) on a premise his words do not state. (3) Two smaller credits to
Day (Nunney; female-only Crow indices) are weaker than written. Against the critics' own side: the same construct
argument removes route (a) as evidence that human selection is soft, B-LL is unreachable on every registered reading,
and under one reading of GG-26 the audit's R4-HF already contradicts it in-model.

## Findings

### MAJOR-1. Neither mapping recovers the model's h from the model itself; "sourced h" overstates what was sourced (W6, extended)

Evidence.

- **What h is.** R4-HF Critic-4 (line 222): h is "the share of the log-load expressed as density-independent survival
  at a fixed R" in the mix model, which "has no field estimator". The lead brief (lines 18-20) defines the target as
  "the degree to which selection is soft (density- or rank-dependent, deaths substitute for one another) rather than
  hard (independent, deaths add)". Both definitions are about *compensation*, not about *life stage*.
- **M-b1 maps a partition the model does not contain.** In `hf_followups.py` mode `mix`, parents are drawn uniformly
  (`pa = rng.integers(0, N, J)`, line 238): fecundity is genotype-blind. Both of the model's channels are
  pre-reproductive survival: density-independent survival `w ** h` (line 256) and the cull to K weighted by
  `w ** (1 - h)` (line 260). M-b1 sets h = share of Crow's index due to pre-reproductive mortality, i.e. it assigns
  hardness by life stage (viability = hard, fertility = soft). In the model the whole load, hard and soft, is viability.
  Applied to the model's own population, Crow's mortality component at N = K is Pd/Ps with Pd = 1 - K/J = 1 - 1/R, so
  **I_m = R - 1 at every h** (post hoc, this review, analytic from lines 218 and 258: 0.111 at R = 1.111, 1 at R = 2);
  the fertility component is genotype-blind sampling noise that also does not involve h. M-b1 run on the model returns a
  number set by R alone. It cannot recover the h the R4-HF thresholds are indexed by.
- **Scale (the write-up's W6 proper).** Even granting a life-stage mapping, Crow's index is a share of *phenotypic
  variance in fitness*, most of it non-heritable (deaths and family sizes from any cause); h is a share of the
  *genotype-dependent log-fitness effect*. A mutation's log-fitness split between channels (s_v / (s_v + s_f)) is not
  tied by any identity to Im / (Im + If/Ps). The registration calls the Crow formula "exact by construction"; it is exact
  for Crow's identity I = Im + If/Ps, not for h.
- **A1 is not the model's structure either (this cuts against the critic-favourable route; see also NOTE-4).** A1 sets
  h = beta_gen, the per-generation persistence of a deviation in log N. In the mix model, whenever survivors exceed K the
  cull returns N to K in one generation (line 258) at **every** h, including h = 1 ("hard selection followed by random
  culling to K", line 56); below K there is no compensation at all (J = R N, R4-HF Critic-4). Regulation strength and h
  are separate dials in the model; A1 is the extra assumption that ties them, and the model gives no reason for it.
- **Consequence for DISJOINT.** The write-up and registration read a non-overlap as heterogeneity between populations
  ("part of the answer"). Given the above, the more economical reading is that the two routes measure two different
  things (regulation strength vs life-stage share of variance), neither of them h. The 0.028 gap (0.022 on the printed
  shares, review 1 MINOR-3) is then not evidence about human h in either direction.
- **Where the overstatement bites.** Write-up "Who this helps", Day side, bullet 1: "on the primary readings at least an
  eighth of selection is hard"; Day side, bullet 2: "Where pre-reproductive deaths are taken as hard (M-b1), Term 3 holds
  within R1 in-model at that end"; the parameters.yaml proposal: h "stays a declared bracket, now a sourced one"; the
  H/H5 placement sentence opening "Sourced h for humans". Each converts a proxy under an audit assumption into a fact
  about human selection, on load-bearing claims.

This is not a BLOCKER: the registration disclosed both mappings as the audit's own ("Step (2) is where the result is
decided"), no band moves a verdict value, and the write-up itself says "h has no field estimator". It is MAJOR because
the proposed claim-file and parameters.yaml wording would carry "sourced h" into the files of record.

Fix (exact).
1. Replace "sourced h" with "sourced proxies for h (route (a) under A1, route (b) under M-b1)" in the one-line result,
   the H/H5 and H8 placement sentences and the parameters.yaml proposal. The parameters.yaml entry reads: "h: declared
   bracket. L2 supplies two proxies under audit assumptions A1 and M-b1 (intervals, DISJOINT); neither mapping recovers
   h when applied to the mix model (M-b1: I_m = R - 1 at every h; A1: N is returned to K at every h)."
2. Day-side bullet 1: replace "at least an eighth of selection is hard" with "under the A1 proxy (column 2) the lower end
   is 0.125; whether that is a share of hard selection depends on A1, which the model does not imply". Day-side bullet 2:
   prefix "If M-b1 holds (an audit assumption the mix model does not share: it has no fertility selection),".
3. Add to "Open": "Validate both estimators on the mix model at known h (0, 0.1, 0.3, 1): compute beta_gen of log N and
   Crow's Im, If from simulated pedigrees. Expected from the code (post hoc, this review): neither tracks h." Queue it as
   a low-stakes tool-validation check; it needs no new source.
4. Under DISJOINT, add one sentence: "The non-overlap may reflect that the routes measure different quantities, not
   that populations differ."

### MAJOR-2. Hancock (GG-26) is scored on a premise his words do not state, and the tally reads as a score against critics

Evidence. GG-26 (quotes-critics.md line 454): "the cost of selection is only applicable for hard selection models where
selection's effect is independent of the genotypes". Write-up, Day side, bullet 1: "the critic-side premise that the
cost of selection does not apply to humans because selection is soft (GG-26, 'only applicable for hard selection
models') is not borne out as an all-or-nothing claim". The quote is about a **class of models**; it says nothing about
human h. The registration itself says PC/PC-w "are the audit's reading of what each side's position needs, not quotes;
they score no author statement (rule S)". The write-up's tally "critic side 0 of 2" and the bullet together present a
miss on an audit construction as a refutation of a named critic. Rule C (most charitable reading) and RD (record every
plausible reading) apply. Readings (my table; the transcript is not on this workstation, the path in the quote note
`sources/raw/critics/yt/_Vu0ZVVjwHc.transcript.txt` does not exist here, so context is unverified):

| Reading of GG-26 | What it asserts | Against audit material |
|---|---|---|
| G-a: the cost is charged only in models with a hard (density-independent) component | a modelling claim | consistent with R4-HF: in-model a cost exists at every h > 0, uncapped only at h = 0 (Day-1 clause; H5 note) |
| G-b: the cost applies only to fully hard models (h = 1) | a modelling claim | contradicted in-model by R4-HF: a cap exists at h = 0.1 and 0.3 (see NOTE-5) |
| G-c: human selection is soft, so the cost does not apply to humans | an empirical claim | not stated in the quote; L2 cannot score it (rule S) |

G-a is the most defensible (the words "hard selection models where..." describe a model class). The write-up's bullet
attacks G-c.

Fix (exact). Replace Day-side bullet 1's second sentence with: "This scores the audit's PD-w, not any author statement.
GG-26 is a statement about model classes; under its most defensible reading (cost charged only where selection has a
hard component) it agrees with R4-HF, and L2 does not test it." Add to the tally line: "(all four side predictions are
audit constructions; rule S: no author statement is scored)." Give the readings table above, or a pointer to it, in the
claim file's GG-26 mention at integration.

### MINOR-1. Route (b)'s Crow indices are female-only; under M-b1 that omits the soft channel par excellence

Evidence. Every admitted Crow record is computed from women's reproductive histories: L2Q-03 ("famílias completas"),
L2Q-06 ("per mother"), L2Q-11 ("per female"), L2Q-13 ("Tundra Nentsi women"), L2Q-18 (Moorad: "a female population").
M-b1 treats fertility among survivors as soft because it is "competition for mates, marriages, niches" (registration
line 83). Male variance in mating and reproductive success is the clearest case of that channel and is absent from
If. If male fertility variance exceeds female (not sourced here; the S1 candidate that would test it, Courtiol 2012,
"Natural and sexual selection in a monogamous historical human population", is on the owner list), If is understated
and M-b1 h overstated. Direction: toward Day. Magnitude: unknown, not estimated.

Fix. Add a limitation line under "Both / the audit's own errors": "Route (b) uses female Crow indices only; under M-b1
male mating variance (soft by M-b1's own definition) is omitted, which biases h upward by an unknown amount; Courtiol
2012 (owner list) would test it." Qualify Day-side bullet 2 accordingly.

### MINOR-2. The Nunney credit is not something L2 tested

Evidence. Day-side bullet 2: "that matches Nunney's 'hard selection will dominate the adaptive process' for the viability
channel." Nunney's sentence (registration line 52) is conditional: "given directional environmental change, it is
likely that hard selection will dominate the adaptive process". A life-stage share of Crow's variance index in ten
records from small populations says nothing about directional environmental change or about which selection drives adaptation.

Fix. Delete "and that matches Nunney's ... for the viability channel", or replace with "Nunney's conditional claim
(directional environmental change) is not tested here."

### MINOR-3. The H8 placement should give each route's position, not only the hull's ends

Evidence. The registration (Aggregation): "the disagreement is reported as a result in its own right (both intervals,
side by side)". The proposed H8 sentence speaks of "the lower end" and "the upper end" of the hull. Route (a), the only
route that measures regulation (the brief's definition), lies wholly in [0.125, 0.256], between the tested h = 0.1
(Term 3 exceeded, 1.36x strict tie reading to 2.8x) and h = 0.3 (0.83-1.05x); route (b) lies at or above 0.284, and
eight of ten records sit at or above 0.3, where Term 3 holds within R1. The hull-end wording lets a reader assign the
"holds" end to the evidence as a whole. (Review 1 MAJOR-3 already fixes the untested claim at 0.125; this is the
per-route complement.)

Fix. In the H8 sentence, after the hull, add: "Route (a) [0.125, 0.256] lies entirely between the tested points 0.1
and 0.3; route (b) [0.284, 0.641] lies at or above about 0.3, where Term 3 holds within R1 in-model (M-b1 assumed)."

## Notes

### NOTE-1. R-E2's fertility floor: a mechanism toward Day, but not visible in these data

R-E2 clause (ii) admits on mean live births >= 6. Since If = Vf / x², a fertility floor tends to select low If and so
high h. Post hoc (this review): mean If is 0.204 over the nine eligible Crow records and 0.282 over the 27 E2-false Crow
records, but that contrast is confounded by the transition itself. The direct test cuts the other way: keeping only
clause (i) records (dated before the decline or natural fertility stated: Slovincian g1, g2, Utah early) gives route (b)
[0.333, 0.641], higher, not lower. So the floor did not lower route (b) here. The default "unclear counts as false" is
also asymmetric (it excluded Maca, 3.6 completed births, 36% pre-reproductive mortality, h 0.639, which favours Day,
as well as Koraga and Santa Rosa, which favour critics). No fix needed beyond review 1 MAJOR-2's two-direction report.

### NOTE-2. Route (b)'s maximum rests on 32 women and no route (b) record carries uncertainty

Slovincian g1 (0.641) has N = 32 (L2Q-08); every route (b) value is a point (W5). The hull of ten unweighted point
values is wider than any record's sampling error would justify at the top and the bottom. It moves no band (B-LL is
unreachable whatever the top end is), so a NOTE.

### NOTE-3. Concurrence with review 1 where it bears on the critics' side

Review 1 MAJOR-1 (the baseline pair of columns 2 and 4 gives route (a) [0.005, 0.256] and turns PD-w into a miss) and
MAJOR-3 (the H8 sentence's untested claim at 0.125) both narrow credits given to Day; I concur with both and do not
repeat them. Under R-a2 or R-a3 the Day-side tally falls to 0 of 2, equal to the critics' 0 of 2; the write-up should
state that symmetry where it gives the tally.

## Findings against the critics' own side

### NOTE-4. Route (a) is not evidence that human selection is soft

The write-up's critic-side bullet 3 says "route (a) is direct evidence that population losses are largely compensated
within a generation", and uses that to favour M-b0. By MAJOR-1, compensation of population losses does not imply soft
selection: the audit's own h = 1 arm is a fully hard model that is also returned to K every generation. A regulated
population can pay a hard cost out of its excess. Critics may not cite route (a)'s "84% compensated within 30 years"
as showing that the cost of selection does not bind in humans. Fix: in that bullet, replace "route (a) is direct
evidence that population losses are largely compensated within a generation" with "route (a) shows strong population
regulation, which is compatible with both hard selection paid from excess and soft selection; it does not by itself
favour M-b0."

### NOTE-5. Under reading G-b, GG-26 is already contradicted in-model by R4-HF, and B-LL is out of reach

If GG-26 is read as "only fully hard models carry a cost" (reading G-b in MAJOR-2), R4-HF contradicts it in-model: the
sustainable rate at h = 0.3 is "about 1.3-1.7x" and at h = 0.1 "about 2.6-3.5x at R = 1.111" the hard cap, i.e. a cap
still exists with 10% hard selection. That is R4-HF's finding, not L2's, but the critics should not claim L2 left
Hancock untouched. Separately, the critic-side PC and PC-w misses are robust: every registered reading pair keeps the
route (b) top end at 0.641 or 1, so B-LL is unreachable (review 1 NOTE-5), and no admitted pre-transition record lies
below 0.1. The critics have no sourced support, on either route under any registered reading, for human h < 0.1.

### NOTE-6. Completed-family samples omit adult deaths during the reproductive span, which under M-b1 understates h

Several admitted records are restricted to women who completed reproduction (L2Q-03, L2Q-06, L2Q-11, L2Q-13). Women who
died between maturity and the end of their reproductive span are absent from both If and Im. Under M-b1 those deaths
are viability ("deaths add"), so their omission biases h *downward*, toward critics, by an unknown amount. It offsets,
partly or wholly, the upward bias of MINOR-1; neither is quantified. Fix: list both biases side by side in the
limitations line proposed in MINOR-1.

### NOTE-7. The Courtiol 2013 exclusion is right, and its "about 0.01" should not be cited for critics

C0142 reports annual-fitness variance components, not lifetime Crow or episode opportunities (P3; review 1 NOTE-2
agrees). The ratio 5.20e-2 / (5.20e-2 + 5.57) = 0.009 compares quantities on different scales, so it is not a
low-h datum. The write-up's critic-side bullet 2 ("The excluded Gambia data would give about 0.01") should add "(not
comparable: annual-fitness components; excluded under the registered stat list)".

## Verdict

No BLOCKER. The band (B-MH), DISJOINT and the no-move result stand; nothing here moves a verdict value. The critics'
strongest point is construct validity: the registered mappings do not recover the model's h even from the model, so
L2's intervals are proxies under audit assumptions, and the Day-side credits built on them ("at least an eighth of
selection is hard", "Term 3 holds at that end", "matches Nunney") must be conditioned. Hancock is scored on a premise
he did not state. Against the critics: route (a) cannot be cited as showing human selection is soft, B-LL is
unreachable, and under one reading R4-HF already contradicts GG-26.

**Counts: 0 BLOCKER, 2 MAJOR, 3 MINOR, 7 NOTE** (NOTE-4 to NOTE-7 are findings against the critics' own side).

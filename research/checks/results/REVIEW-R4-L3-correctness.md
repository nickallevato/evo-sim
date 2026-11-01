# REVIEW R4-L3: correctness

Reviewer: fresh reviewer instance (Paperclip EVOA-6, brief `A2e-reviewer-1.md` at b246371), 2026-11-01. Skill:
`review-correctness`. Review 1 of 3 (D-23). I did not author any of this work.
Under review: `research/checks/results/R4-L3.md` (78d9d11), against the registration (`l3_amk.py` docstring l.1-279,
f5b7e5e). Inputs: `raw/l3_main.out`, `l3_result.json`, `l3_counts.json`, `l3_amk.host`, `l3_smoke.host`,
`l3_smoke_host.out` (collected a8d14b8); briefs `L3-analyst.md`, `A2e-analyst-1.md`; `REVIEW-R4-A2e-external-ruling-check.md`
(the write-up's "EVO-74"). Local work: two `python -I` processes on the committed json, seconds each, under 200 MB.
No run, no fetch. The npz was not loaded.

## What I recomputed and found right

- **Run integrity.** Script md5 `ae4a764eec0ff8100c05d120fb41ecb4` at f5b7e5e, in the working tree and in
  `l3_amk.host`. The script has not changed since f5b7e5e (`git log` on the file: f5b7e5e, then only the disclosed
  draft 9d87dbf before it). Order: registration 2026-10-13 22:43:15, local smoke 292466f 22:44:08 (`SMOKE OK`),
  host smoke and sizing 2026-10-19 01:14-01:17, launch 01:17:20, finish ~01:21, collect a8d14b8 01:29, write-up
  78d9d11 2026-11-01. The md5s of `l3_main.out` (c4225ff3…), `l3_result.json` (18940a69…) and `l3_counts.json`
  (925f101e…) equal the collection record. Input sizes equal the registered Content-Lengths; the panel sha256
  equals the registered one.
- **Fits re-derived.** From the json `Pn`/`Ps`/`Dn`/`Ds` of each row, the script's own `fit_row` with the registered
  seed (`SEED + 100 + i`) reproduces the model, P and the MC/t interval of all seven rows **to every printed digit**
  (GOV exponential -0.019985 [-0.0626, 48.9101]; S2 linear 0.00162 [-0.0964, 0.0997]; S6 0.014387 [-0.0266,
  58.0607]; S1, S3, S4, S5 likewise).
- **Thresholds and band.** G1 190.620, G2 158.790; G1/Dn 0.006673, G2/Dn 0.005559; h = 0.0175, l = 0.005559.
  P -0.019985 < l and U 48.9101 ≥ l: **B5**. S1-S5 points (-0.0169, 0.0016, -0.0177, -0.0286, -0.0375) are all
  < l and none is None: no rise, **move row B5**, licensed `contested` (`LICENSED["B5"]`). B5 also holds on the
  bootstrap upper bound alone (0.0921 ≥ l), as section 2 says.
- **Gates.** GG est 0.57094 within 0.005 of 0.571, exponential; GA 19,504 ≥ 10,000; GB 0/872,626; GC 0; GD
  28,565 / 39,192, ratio 0.7288; GE min window Ps 360 (bin 17); GF 0/1,000. GH: panel AFR 661, EUR 503.
- **All 13 predictions** scored against the docstring wording (l.229-243): DS hit, DS+ hit, CS miss, CS+ miss;
  Q1 miss (-0.8423), Q2 miss, Q3 hit (0.822363), Q4 hit (28,565; 0.7288), Q5 miss (48.98442), Q6 hit (0.017500),
  Q7 hit, Q8 miss, Q9 hit. Matches the printed `score` line and R4-L3 section 4.
- **Every number in sections 1-5** (gates, coefficients a -0.01995 / b -0.51206 / c 9.67518, the 20-bin spectrum,
  the sensitivity table incl. std_all and original, all 18 counts at P/L/U) matches the json. Section 7 numbers
  (bootstrap [-0.8836, -0.8030] and [-0.1155, -0.0444]; 0.096; 5.3x; 0.0175; 0.1664) are right.
- **Counts (section 9, item 4) are registered behaviour.** `analyse` l.1010-1012 computes `a * Dn` and `a * N_k`
  for a = P, L, U with no clamp, as the docstring says ("Counts are reported as alpha x Dn and alpha x N1..N3").
  Negative P and L give negative counts; U > 1 gives counts above Dn. No code-path bug.
- **Section 6 against F = `contradicted` and F = `contested, leaning contradicted`** applies the docstring's
  "licensed value below F … B4, B5: one step down" bullet exactly; F = `contested` applies "equal: confirms".
- **Post hoc labels** in sections 1-3 and 7 are present and the labelled items are arithmetic on registered output.

## Findings

**MINOR-1 (ruling on the hand-patched `sites.vcf.gz`, section 9 item 1): the run is accepted; the provenance record
is incomplete.** Severity MINOR, not BLOCKER or MAJOR, for these reasons:
- The patched file passes every integrity check the registration set: size = registered Content-Length
  (1,458,224,240; asserted by `main`). The registration gave no sha256 for this file, so none could be compared.
- `gzip -t` OK (host record). Gzip stores a CRC-32 and the length of the decompressed data for every member. So a
  wrong byte left in any member, including the patched 500 B, fails with probability about 1 - 2^-32. The run
  checked this again: `count` reads the file with Python's `gzip.open` to EOF (l.698-700). That reader checks each
  member's CRC-32 and length and raises on a mismatch. `l3_main.out` has no traceback and `vcf_lines` is
  84,801,880.
- Content checks on the decoded records: 0 REF mismatches against hg19 in 872,626 CDS records (GB), 0 non-integral
  allele counts (GC).
- Bounded effect: the window is 500 B at byte 1,439,336,600 (98.7% into the file). It touches at most two
  compressed blocks. The band margin is P - l = -0.0255, and even B6 needed U < 0.0056 against a bootstrap upper bound
  of 0.0921. A few records cannot move the band.

What the record lacks: (a) the evidence is on na-workhorse only (`parts/curl*.err`, not in git, no hashes). (b) "server
refetch x3 identical" does not say what was re-fetched (the window range or the whole file) or what it was
compared with. (c) The two copies' sha256 values and the offsets of the four bad windows are not recorded.
(d) The patched 10-18 copy sits in the `l3-data-2026-10-19` directory, which mixes two fetches (rule 4,
"each fetch in its own new directory"). (e) No provider checksum was compared.
**Fix (no re-run needed):** the fix pass states this ruling in section 9 and drops "This write-up does not rule
on it" from the headline. Before integration, one operator task reads the files on the host (no fetch) and
commits to the host record: the sha256 of both copies, the four window offsets, the hash of each of the three
re-fetches, and the `gzip -t` transcript. Optional, and only if the lead wants a provider-side identity (this is a
fetch, so it needs a brief): compare the file against a checksum the provider publishes for it, or against one
clean full re-download. If the sha256 equals `381d2ece…43b7f2`, the patch question is closed. If it differs,
re-run `main` (~4 min) on the clean copy, labelled post hoc.

**MINOR-2: the governing row uses the upper-case-AA reading. The registered precondition for that reading is not
met, and section 8 says the opposite.** The docstring (l.103-105) says the run task "must quote it from the 1000
Genomes ancestral-alignment README before the write-up uses it". GOV *is* the upper-case-AA row, so R4-L3 uses the
reading in every band line, even though section 8 says "This write-up therefore does not rely on that reading."
The outcome does not depend on the reading. With S4 (all-case AA, the row the docstring says "covers the other
reading") as the governing row, P -0.0286 < l and U 1.5412 ≥ l give B5. The other rows' points, GOV's -0.0200
included, are all < l, so the move row is still B5 and the licensed value `contested`. But section 8's "S4 gives
the same band" is unlabelled post hoc arithmetic. **Fix:** replace the sentence with: "GOV rests on the
upper-case = high-confidence reading. The registered quote for it is not on record (a registered-procedure
deviation). With S4 as the governing row the band and move row are also B5 (*post hoc*), so the licensed value
does not depend on the reading." Leave the quote as an open item for the lead (it needs a fetch).

**MINOR-3: section 6 contradicts itself on F = `pending`, and the docstring does cover the case.** Section 6 says
that against `pending` "the move … is none" (quoting the docstring). The table's last row then calls F still
`pending` at integration "not covered", and section 10 item 4 repeats that. The docstring answers it: "L3 does
not end D-21's pending by itself". L3 alone licenses **no move** from `pending` in any band. What the docstring
lacks is a value for the field in that case, and that choice is the owner's. The ruling check l.53 gives it to
the owner: O-17's second option, "`pending` (or `contested`, as the owner chooses)". If the owner sets `contested`,
the "equal: confirms" bullet applies. **Fix:** table row → "covered: no move by L3 alone (docstring l.216); the
field's value is the owner's O-17 choice, and the rule then applies to that value". Remove this case from section
10 item 4.

**MINOR-4: section 9 item 2 explains the MC tail incompletely. The tail is registered behaviour, not a bug.**
`_mc_ci` (l.426-443) is the registered port of predictNLS (normal draws around (a, b, c) with the fit
covariance, `empirical = TRUE`, alpha(1) = a + b·exp(-c), no truncation). The ±100 rejection (l.469) is the
registered asymptoticMK rule (docstring l.80), and 48.9 passes it. But "draws with small or negative c give large
values" is wrong as stated. With b at its estimate (-0.512), a negative c gives large *negative* values. My
recompute of the GOV covariance gives sd(c) = 7.37 against c = 9.68, sd(b) = 0.549 and corr(b, c) = -0.947. In
an illustrative 10,000-draw sample (seed 1, *post hoc*), 6.5% of draws exceed alpha = 1, and **all of them have
b > 0 and c < 0 together**. **Fix:** "draws in which c turns negative and b turns positive together (corr(b, c)
-0.95, sd(c) 7.4 against c 9.7) give alpha(1) far above 1; the predictNLS port does not truncate, and the ±100
rejection rule does not fire. Registered behaviour."

**NOTE-5: wrong cross-reference.** Section 5, last line: "(section 9, items 2 and 5)" → "(section 9, items 2 and 4)".

**NOTE-6: the strike follows as worded (section 9 item 5).** The docstring (l.221-223) strikes the "aMK baseline
(alpha 0.076) 4.4x" line in rows B4-B6 with no condition about whether 0.076 lies inside L3's interval. Under the
registration it is struck. Whether "not reproduced on the same samples" is a fair description (gene set, bins,
window and fit may differ) is a steelman question, not a correctness one. **Fix:** say so, and keep the
inside-the-interval fact as context.

**NOTE-7: the two F-below-`contested` rows of section 6 cannot occur on the record.** The table claims "each F the
record makes possible". The D-21 chain yields `contradicted` (ruling check l.52). O-17's second option yields
`pending` or `contested`. Neither `supported` nor `contested, leaning supported` is reachable. The gap in the
docstring is real: "above F (rows B1-B3)" names no B4-B6 case. But it does not apply here. **Fix:** mark the two
rows "not reachable on the record; registration gap noted", or drop them.

**NOTE-8: the lean against F = `contradicted` is storable.** Section 10 item 4 cites ruling check A-R5 (iv), "a
lean is not a vocabulary value". The same paragraph and existing practice (FM10, ROOT-fm: `external: contested`
with "leaning critic" in the comment) store a lean as the vocabulary value `contested` plus a comment. The B5 move
against `contradicted` is therefore `contested` with the lean in the comment, with no gap in the vocabulary. Also
cite the ruling check by its path (`research/checks/REVIEW-R4-A2e-external-ruling-check.md`), not by "EVO-74".

**NOTE-9: deviations from the registered run record.** The record file is `l3_amk.host`, not `l3_main.host`
(the write-up notes this). The docstring's step 5 asks for the PID, which is not recorded. Neither has any effect.

**NOTE-10 (post hoc, for the steelman reviews; no band, no verdict).** On the GOV bins, the linear fallback gives
alpha(1) = 0.0161, which is a B4 point inside [l, h]. AIC chooses the exponential by 2.87 (-41.48 against -38.61).
c is poorly identified (sd 7.4), so P is in effect the asymptote a. Both B4 and B5 license `contested`, and both
are "one step down" against `contradicted`. So the licensed outcome does not depend on the model choice. Section 7
item 1 says the spectrum "scatters around zero" above x ≈ 0.3. The 12 bins there have mean -0.024, with 8 of 12
below zero, so "at or slightly below zero" is closer.

## Counts and wrong numbers

BLOCKER 0, MAJOR 0, MINOR 4, NOTE 6.
Wrong numbers (old -> right): none. Every number in sections 1-5 and 7 reproduces from the json. One wrong
reference: section 5 "items 2 and 5" -> "items 2 and 4".
Band B5, move row B5, licensed `contested`, and "no move against `pending` by L3 alone" are confirmed.

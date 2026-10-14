# Fresh-reviewer check of the lead's rulings on A2e external (D-24 safeguard)

Date 2026-10-14. Reviewer: a fresh reviewer instance (Paperclip EVO-74), using the skill `review-correctness`. Labels: BLOCKER / MAJOR / MINOR / NOTE. **This review sets no verdict.** It says whether each ruling survives and, where one does not, what the field takes instead. The lead then rules again (D-24).

**Independence.** I wrote none of the following: R4-A2e-alpha, its Uricchio addendum, the three O5 reviews of A2e, the lead's rulings or the fix pass (EVO-71). The task requires me to read the rulings and the reviews they rule on, so I read all three in full. I also read the fix-pass write-up, because it applies the rulings.

**Read.**
- Brief `research/checks/briefs/O5-reviews-reviewer.md` Part 2, A-R1 to A-R9 (l.193-274, 35b196a).
- `REVIEW-R4-A2e-external-correctness-2.md`, `-steelman-day.md` and `-steelman-critic.md`.
- `results/R4-A2e-alpha.md`, all of it (fix pass c4cf503).
- Claim file `claims/A2e-ltee-as-ceiling.md`, front matter.
- `R4-X1-verdict-rule.md` l.198. `DECISIONS.md` D-12, D-15, D-21, D-24 and the O-5 premise correction.
- Milestone 13 (`docs/2026-10-11-1-…md`) l.24, l.27, l.97.
- GRADE pass `criticality/grade-certainty-2026-10-12.md`: row A2e (l.330), §2.9, §5.6, §8.
- `METHOD-AUDIT-2026-10-12.md` MA-08 and MA-12. `criticality/README.md` ST-03 (l.218). `ROADMAP.md` C21 (l.143) and A12.
- `research/checks/l3_amk.py`, the docstring bands and verdict moves (l.170-230), registered at f5b7e5e.

**Source text.** `sources/raw/a2e-corr2-2026-10-13/a.xml` (gitignored). I recomputed its sha256 here: `3e7c44cb…b865977`, which is the registered hash. I checked the following directly as substrings of that file:
- "reduced by approximately 25% by BGS"
- "directly accounts for BGS and weakly-beneficial alleles"
- "were not very sensitive to various types of model misspecification"
- "we use a much larger set of genes in our inference and hence the estimates are not directly comparable"
- the figure caption counts "VIPs, 4,066 genes" and "non-VIPs (12,962 genes)"

**Recomputation** (a trivial local check: stdlib only, one line, post hoc, not committed). G1 = 190.62.

| Quantity | Value |
|---|---|
| 0.096 × 11,090 | 1,064.6 (5.585x; artefact share 82.1%) |
| 0.072 × 11,090 | 798.5 (4.19x) |
| 0.076 × 11,090 | 842.8 (4.42x) |
| 0.09 × 11,090 | 998.1 (5.24x) |
| 0.135 × 11,090 | 1,497.2 (7.85x) |
| Boyko 0.054 × 22,180 × 0.25 | 299.4 (**1.571x**) |
| Boyko 0.054 × 11,090 | 598.9 (3.14x) |
| Own base, 0.096 × 29,925 | 2,872.8 (15.07x) |
| Own base, 0.135 × 29,925 | 21.19x |
| alpha\* | 1.719% on N2; 0.637% on the own base |
| Gene-count scaling | 18,936 × (4,066 + 12,962) / 9,785 = 32,953; 29,925 is 0.908 of it |
| L / h (lower HPD / alpha\*) | 5.59 on N2; 15.07 on the own base |

Every number in the fix pass's proposed field text reproduces.

## Summary for the lead

| Ruling | Survives? | Why, in one line |
|---|---|---|
| **A-R5** (`contradicted`, scoped, certainty qualifier in the field text) | **Yes, on the value. Its integration is gated** (MAJOR-1, MAJOR-2) | No written rule caps the word by certainty. The only written scale for this field, L3's registered scale, puts this evidence at `contradicted` (L/h 5.6 ≥ 3). The audit's move condition, stated publicly before the full text was read, is met. Moving A2e alone to `contested` would apply a certainty cap to one Day-adverse node that B6, B1c, B3 and others are not held to. But pending → `contradicted` while the registered severe probe L3 has not run is the choice that ST-03 / O-17 reserves for the owner. And the qualifier sits in a YAML comment that no tally reads. |
| **A-R4** ("bias-corrected" restored to the basis is not a narrowing of D-12) | **Yes** | The scope clause is unchanged word for word, and "bias-corrected" sits in the Basis clause. The criterion was written publicly before the full text (milestone 13 l.27). The owner decided D-12 on a summary that described Uricchio as corrected. GV's 0.2% had already been withdrawn as a count on 2026-10-10 (M1), before D-12, on a ground independent of this criterion. Two wording faults in the field text (MINOR-6, MINOR-7). |
| **A-R3** (N2 stays the verdict denominator; own base reported only) | **Yes** | The symmetric rule is: the basis is the estimate least favourable to the verdict being set. For `contradicted` against Day that is the smallest denominator. For a Day-side `supported` it would be the largest. The critic case conflates which denominator *measures* the quantity with which number the field *rests on*. The direction is the same on every base, and the field reports the own-base rows. Two wording points (NOTE-9). |

**What the field takes.** The field takes the value A-R5 proposes, `contradicted` (scoped), with the fix pass's field text amended per MINOR-3 to MINOR-7. Two conditions apply:
- **(a)** The owner answers the A2e row of O-17 before integration, or the lead records why D-24 covers that choice (MAJOR-1). If the owner takes O-17's second option, the field stays `pending` (or `contested`, as the owner chooses) until L3 reports, and L3's registered combination rule then applies. It does **not** take `contested, leaning contradicted` on this evidence (see A-R5 (iv)).
- **(b)** The qualifier travels with the value wherever A2e's external value is named or counted (MAJOR-2).

## A-R5: does `contradicted` survive the Day-side steelman's MAJOR-3?

**(i) The Day-side case at its strongest.** I put it more strongly than MAJOR-3 did, adding two points from the audit's own instruments:
1. One post hoc source supplies the HPD.
2. The full text was read before the "registration", so the step had low severity.
3. The evidence was gathered with no search strategy (AR-05).
4. The GRADE pass rates A2e very low under all three mappings, and §5.6 lists A2e among the eight verdicts "over-stated" under every mapping.
5. Under GRADE proposal k, lint rule L-GC4 would flag `contradicted` at very-low certainty as "worded above its evidence". `contested` with direction `against` at very low would trigger nothing (L-GC5 fires only at moderate or high). So by the audit's own certainty instrument, `contested, leaning contradicted` is the value that raises no warning.

**(ii) Why this does not carry the value away from `contradicted`.**
- **No rule maps certainty onto the word.** The GRADE pass says certainty is a field *beside* the verdict, "neither as a new verdict value" (§8). It also says L-GC4 "warn[s] and do[es] not fail, because changing the verdict word is a rule-freeze matter and not lint's to force" (§8.2). Its §2.9 says the result is not to be read as "a statement that low-certainty verdicts are wrong". Point 5 above is therefore an argument for a rule change. It is not a reading of the current rules.
- **One rule for all sides.** The same §5.6 lists B6 (`supported` for a critic), B1c, B3, F1b, DN1, DN2 and B5c in the same position. If the lead moved A2e to `contested` on certainty grounds, he would be applying a certainty cap to one Day-adverse node that the critic-favourable B6 is not held to. If the cap is right, it is a rule-freeze change for all eight.
- **The stated move condition is met.** The fix pass of 2026-10-10 (R4-A2e-alpha l.129) and milestone 13 (l.27, l.97) were written before the full text was read. They say: "It moves to contradicted with a full-text Uricchio, or any other bias-corrected human-branch alpha above about 1%". The lower HPD edge meets even the strict interval reading, at 5.6x on N2. Holding the field at a lean after its own published condition is met would move the goalposts against the critic side. MAJOR-3's severity point is correct: once the abstract value was known, the step was near certain. But that bears on certainty, which A-R5 carries. It does not bear on whether the condition holds.
- **The only written scale for this field agrees.** L3's registration (f5b7e5e, 2026-10-13 22:43, before the ruling at 23:02) fixes the scale `supported < contested-leaning-supported < contested < contested-leaning-contradicted < contradicted`:
  - B1 is `contradicted` when the interval clears the threshold by ≥ 3x.
  - B2 is `contradicted` "with the certainty qualifier 'interval clears the flip by less than 3x'".
  - B3 is `contested, leaning contradicted` when the "point clears, interval does not".

  Uricchio's lower HPD clears h by 5.6x on N2, which is B1 territory. The value MAJOR-3 asks for is, on the audit's own written scale, the value for evidence whose interval does *not* clear the flip. That is not this evidence. Note one limit of this scale: it was written for L3's evidence, not as a field rule, and it measures certainty by margin only, not by process. That is why the process weaknesses belong in the qualifier.
- **The conflict is narrower than it looks.** MAJOR-3 l.95 itself offers the alternative: "Failing that, it carries `contradicted` only with an explicit certainty qualifier". A-R5 adopts that alternative almost word for word.

**(iii) Verdict on A-R5.** It survives as the value the evidence on record carries under the current rules. MAJOR-1 and MAJOR-2 below limit how it may be integrated, not what it is. MINOR-3 and MINOR-4 correct two statements in its reasoning.

**(iv) If the lead wanted a lean instead.** A lean is not a vocabulary value. `contested, leaning contradicted` would be stored as `contested`, which is the usage MA-08 records as one of the five meanings that make `contested` uninformative. On the written L3 scale it would also misdescribe an interval that clears the flip by 5.6x.

## A-R4: does restoring "bias-corrected" narrow the D-12 scope?

**Test.** A scope narrowing changes the proposition being rated. Appraising evidence changes which estimates are taken to measure that proposition. Appraisal is not narrowing as long as what is set aside is named, with reasons. If it were not, every exclusion of a biased estimate would need the owner.

1. **The scope clause is unchanged.** The superseded field and the proposed field text (R4-A2e-alpha l.232) both read: "a per-generation count of adaptive fixations of any effect size, coding-only, on model-inferred alpha (A2e's formal statement)". "Bias-corrected" appears only in "Basis, on the bias-corrected estimates gathered …". The proposition is the true count, not "the count as bias-corrected methods estimate it". The latter would make the verdict circular, and the text does not say it.
2. **The criterion predates the result and was public.** Milestone 13 l.27, written before the full text was read, says "or any other bias-corrected human-branch alpha above about 1%". R4-A2e-alpha l.129 (2026-10-10) says the same, and C3 (l.82) had already ruled that bias-corrected and naive MK are "not rival measurements of equal standing". The owner summary for D-12 (l.200) describes Uricchio as "a model that corrects for slightly deleterious and weakly beneficial variants". The owner therefore decided D-12 on a bias-corrected basis. Saying so restores what was decided; it adds nothing to it.
3. **GV's 0.2% was not an in-scope count even before this step.** The fix pass of 2026-10-10 (M1, l.80) withdrew 29-49 as a count: alpha is a null at FI 1.00 and is still rising across the DAF classes. That ground is independent of "bias-corrected" and predates D-12. Correctness MAJOR-2's question ("does 'model-inferred alpha' include uncorrected MK? If it does, the in-scope evidence straddles the flip") is answered by M1 more than by A-R4: there is no sub-flip *count* on the record to straddle with.

**A-R4 survives.** MINOR-6 and MINOR-7 fix how the field text describes what it sets aside. NOTE-8 records the asymmetry of effect.

## A-R3: N2 or the paper's own base?

1. **The symmetric rule.** The critic steelman says (MAJOR-2): "A Day-side result would not be scored by multiplying a Day-favourable rate by a denominator from a different study chosen because it was the smallest." That is right, and its mirror is A-R3. For a `contradicted` verdict against Day, the conservative basis multiplies the estimate least favourable to that verdict (the lower HPD) by the denominator least favourable to it (N2, the smallest: N1-low 14,678, N3 18,180 and Boyko-Methods 18,069 are all larger). For a Day-side `supported`, the conservative basis would take the largest denominator. A-R3 stacks against the verdict being set. The critic case would stack toward it.
2. **"Like for like" and "basis" are different questions.** The critic side is right that alpha × 29,925 is the like-for-like count on Uricchio's gene set. A2e's quantity, though, is the whole adaptive count, and every denominator on record gives a coding-only lower bound on it. The field takes the lowest lower bound and reports the like-for-like rows beside it (proposed text: "Reported only (P4): … 2,873 at the lower HPD (15x) and 4,040 at the posterior mean (21x)"). Nothing is hidden. The stated margin is a floor and is labelled as one.
3. **Holding to P4 is the anti-post-hoc choice.** P4 was written before the D-21 reviews. A-R7 has since relabelled it a reproduction, so it is a commitment made with the values in hand. Moving the basis to the own base *after* reviews, which widens the stated margin from 5.6x to 15x in the direction of the verdict, would be the post hoc move the audit bars. The direction is the same on every base.

**A-R3 survives.** NOTE-9 covers two wording points.

## Findings

### MAJOR-1: Pending → `contradicted` while L3 is registered and not run is the O-17 choice, which the record reserves to the owner. A-R5 makes it without saying so.
*Attaches to:* brief l.235-245 (A-R5) and l.270-274 (A-R9); `R4-A2e-alpha.md` l.168, l.232.

**Evidence.**
- ST-03 (`criticality/README.md` l.218) has status "needs owner". It names A2e external among four load-bearing verdicts resting on WEAK probes, all leaning to the critic side.
- The proposed O-17 (severe-testing l.516; `ROADMAP.md` C21, l.143, "needs owner … Owner choice; rule-freeze if values move") asks whether to "leave the present values with a 'weak probe' note, or return them to `pending` / `contested` until a severe probe has run (A12 …)".
- O-17 has not been recorded in `DECISIONS.md` and has not been answered. D-21 answered O-5, the review tier, and not the severity question.
- The severe probe A12 is now registered as L3 (f5b7e5e). It has run only on synthetic inputs (292466f, "SMOKE OK").
- A-R5's "value plus certainty qualifier in the field text" is O-17's first option, the "weak probe" note. MAJOR-3's request is, in effect, its second option.

D-24 lets the lead rule a conflict between the steelmen. It does not extend to a standing owner question that the audit's own criticality layer marked "needs owner" before this conflict arose.

**Why this does not defeat A-R5 on the merits.** O-17 asks a process question, about waiting for a severe probe. It does not ask what the current evidence carries. The precedent MA-12 set for DN1-DN3 was to keep `contradicted` "conditional on L1b", not to revert. That supports A-R5's value with an "L3 pending" clause, if the owner takes option 1.

**Fix.** Before integration, the lead does one of two things:
- **(a)** Puts the A2e row of O-17 to the owner, in plain words, with both options and what each does to the field. Option 1: `contradicted` (scoped), with the qualifier and "conditional on L3, registered f5b7e5e". Option 2: `pending` or `contested` until L3 reports.
- **(b)** Records in the brief, with reasons, why D-24 covers that choice and O-17 does not apply.

In both cases the field text adds: "the audit's own aMK estimate (L3, registered f5b7e5e, not run) can move this down (rows B4-B6 of its registration)".

### MAJOR-2: The certainty qualifier lives in a YAML comment that no tally reads, so A-R5's own justification holds only inside the claim file.
*Attaches to:* brief l.241-245 ("carried **in the field text** … A field that states its own weakness is honest"); claim file front matter, `verdicts.external`.

**Evidence.** The "field text" is the comment after `external:`. The value tools parse is the bare word: `grade_certainty.py` l.38 reads `fm["verdicts"]["external"]`, and YAML loaders drop comments. The tallies in `HANDOFF.md`, `docs/arguments/README.md`, `README.md` and the public board count words. A reader of the board would see A2e counted as one more `contradicted` against Day, with no qualifier. The board already names the A2e value in prose (status.html, "A2e-alpha addendum"), so the qualifier has a place to go.

**Fix.** At integration and in the next board patch, every public mention of A2e's external value prints it with the qualifier: "`contradicted` (scoped; very-low certainty, M0; a reproduction, not a test; L3 pending)". Any tally that counts it adds a footnote saying so.

**Like for like.** B6, B1c, B3, F1b, DN1, DN2 and B5c carry decided words at low or very-low certainty with no such note. Doing this for A2e alone is disclosure, and it is to Day's benefit. It is not a rule. The general remedy is GRADE proposal k (certainty fields beside every decided external verdict), which needs the owner and the freeze procedure. Recorded here so that it is not read as one more Day-adverse value with a qualifier that only Day's file carries.

### MINOR-3: A-R5's "4.2x at its narrowest" and the Part 2 preface's "the lowest cell being 798 (4.2x)" are wrong.
*Attaches to:* brief l.196 and l.240.

The lowest any-effect-size, bias-corrected cell on record is Boyko at the lower CL with a 25% human share: 299.4, **1.57x** (R4-A2e-alpha l.24, l.84; milestone 13 l.24, "the lowest compounded Day-charitable row … is 299"; and the fix pass's own proposed field text). After A-R1, 798 (4.2x) is an unsourced sensitivity and the basis is 1,065 (5.6x). Correctness review 2 l.7 said "at least 798" against its own MINOR-2, and the ruling inherited the slip.

A-R5's second limb is true: "no Day-favourable adjustment on record reach[es] 191", and 299 > 191. So the ruling survives. But the stated margin was too wide.

**Fix.** "5.6x at the basis (Uricchio lower HPD, N2). 1.57x at the most Day-favourable stacked sensitivity on record (Boyko lower CL with an assumed 25% human share, a pooled-lineage estimate). None reaches 191."

### MINOR-4: A-R9 says RG-03 "is the one piece of work that could move this field". L3, registered 19 minutes before the ruling, is another, with pre-stated moves down.
*Attaches to:* brief l.270-274; proposed field text "none was searched for (RG-03)".

L3's verdict moves (l.198-228) take a `contradicted` field down one step in rows B4 and B5, and two steps in row B6. They also strike "aMK baseline (alpha 0.076) 4.4x" from any `contradicted` basis if it is not reproduced. The fix pass's "proposed addition" (model error, A12) points the same way but names A12 only as a probe, not as a registered move.

**Fix.** Name L3 and its rows B4-B6 in A-R9 and in the field text (see MAJOR-1).

### MINOR-5: "Very-low GRADE certainty" must name its mapping and say that the row predates D-21.
*Attaches to:* the proposed field text (R4-A2e-alpha l.232); GRADE §8 item 4 ("No public page reports a certainty without saying which mapping").

The row of record (l.330) still rates the 798-with-haircut basis and the pre-D-21 process. I recomputed the level with the formula at `grade_certainty.py` l.93-104:
- **M0 stays very low** under any re-rating that keeps at least one downgrade. The start is low for (Lm, W), and any downgrade floors it.
- **M-C could rise to low** if the critic's MINOR-4 corrections are taken (rob 1, inc 0, rd 0, sel 1 gives 3 − 2 = 1).

**Fix.** "very-low GRADE certainty (M0; row of 2026-10-12, not re-rated after D-21)".

### MINOR-6: The field text's "Gayà-Vidal 2014's 0.2% (29-49), an uncorrected MK value" restates a count withdrawn on 2026-10-10, and "uncorrected" is loose.
*Attaches to:* R4-A2e-alpha l.232; brief l.230-231.

M1 (l.80) withdrew 29-49 as a count. GV applied a frequency filter (DAF ≥ 60%), which is a partial correction, with no DFE model. Its authors say the value "may be an underestimate".

**Fix.** "Gayà-Vidal 2014's 0.2%: a null (FI 1.00), withdrawn as a count on 2026-10-10 (M1); frequency-filtered MK with no DFE correction, which its authors flag as a possible underestimate."

### MINOR-7: Eyre-Walker & Keightley are set aside by their Day-leaning clause only.
*Attaches to:* R4-A2e-alpha l.232.

The field sets aside "little evidence (0-1,223)" as abstract only, human-macaque and the audit's own reading. The same reasons apply to the abstract's "could be as high as 40%". That clause is cited as bias-corrected support at l.82, l.127 and in milestone 13 l.24, and the field drops it from the Basis without a word.

**Fix.** "Eyre-Walker & Keightley 2009, both clauses ('little evidence'; 'as high as 40%', conditional), set aside: abstract only, human-macaque".

### NOTE-8: The bias-corrected criterion removes only sub-flip values.
That is true, and a reader may take it for tailoring. It is not, for three reasons:
- The direction of the bias is sourced by the authors of the excluded estimates (GV Discussion; EK abstract: "expected to give downwardly biased estimates").
- The criterion was written publicly before the full text was read (A-R4, point 2).
- The excluded GV value is a null on an independent ground (M1).

### NOTE-9: A-R3 wording.
- "Widen the stated margin in the audit's own favour" should read "in the direction of the verdict being set". The audit has no side.
- "Genuinely unreconciled" sits next to its own replacement text. The gene count behind the candidate scaling is now verified from the registered-hash source: 4,066 VIP + 12,962 non-VIP = 17,028 genes. The scaling gives 32,953, and 29,925 is 0.908 of it. Only the uniform-density assumption remains unverified. The replacement text can say "gene count verified; uniform per-gene density assumed".

### NOTE-10: A-R5 in effect defines `contradicted` as "direction and margin, with certainty stated beside it".
No written rule says so (correctness NOTE-6; MA-08). The definition is consistent with three things: GRADE §8, L3's registered scale (B1 and B2) and practice on B1c, B3 and B6. It should be written down through the freeze procedure, together with a margin threshold (L3 uses 3x on the interval). The fix pass has already forwarded this to the next criticality pass, and I agree.

## Counts and wrong numbers

BLOCKER 0, MAJOR 2, MINOR 5, NOTE 3.

| Where | As written | Right |
|---|---|---|
| Brief l.196 | "the lowest cell being 798 (4.2x)" | lowest any-effect-size bias-corrected cell 299 (1.57x, Boyko compounded); basis 1,065 (5.6x); 798 is an unsourced sensitivity |
| Brief l.240 (A-R5) | "4.2x at its narrowest" | 5.6x at the basis; 1.57x at the narrowest stacked sensitivity |
| Brief l.273 (A-R9) | RG-03 "the one piece of work that could move this field" | RG-03 and L3 (registered f5b7e5e; rows B4-B6 move it down) |
| Proposed field text | "Gayà-Vidal … 0.2% (29-49)" | 0.2% is a null; 29-49 was withdrawn as a count on 2026-10-10 (M1) |
| Proposed field text | "very-low GRADE certainty" | very-low under M0 (row of 2026-10-12, before D-21); M-C may be low on re-rating |

No arithmetic error was found in the fix pass's numbers. Every count, ratio and artefact share in the proposed field text reproduces.

# R4 VID-01-score: scoring the Gutsick Gibbon roundtable (GG-4) against the claim files

Task EVO-76. Brief: `research/checks/briefs/VID-01-score-analyst.md` (commit `9e96f51`).
Lead rulings R-1..R-7: `research/checks/briefs/VID-01-operator.md` addendum (commit `3792a6b`).
They bind and are not reopened.

Source of record: `docs/research/sources/refresh-2026-10-13-video.md` (harvest `6d090de`, fix pass
2026-10-13), `docs/research/sources/quotes-critics.md` section `YT-AqC1ZM4icms` (GGR-01..GGR-46),
review `research/checks/results/REVIEW-R4-VID-01-combined.md` (`38a1950`).

**This is the first task permitted to move a verdict field from this source.** The harvest, its
review and its fix pass all moved nothing.

## Review tier: three reviews (correctness, steelman-day, steelman-critic)

Stated here so the reviewers need not re-derive it. `hierarchy.yaml` marks neither A4d nor A5h
`load_bearing`, but **D-23 triggers twice independently**:

1. this registration carries a **verdict-field flip** (A4d `internal`, possibly A5h `external`,
   possibly Ge `internal`); and
2. branch G's **G and G1 are listed feeders of load-bearing nodes** in `docs/research/R5-draft.md`
   §1.3, and question 3 scores against them.

So: three separate reviewer instances, one after another under the one-agent cap (D-22) — not the
low-stakes combined tier the harvest used.

---

# Predictions (pre-registered)

**Registered 2026-10-13, before the MITTENS 3.0 text was re-fetched or opened** (hard rule 5).
This is a scoring pass over a committed record, not a simulation, so there is no run to
pre-register; what is pre-registered here is, for each of the five questions, what each side's
position predicts the evidence will show and **which verdict each reachable outcome produces**.
The bands below are intended to be exhaustive over the reachable outcomes. Anything written after
this commit is in a separate commit labelled **post hoc**.

## Instrument for Q1 and Q4: the re-fetch

`sources/raw/day/zenodo-23003785.txt` no longer exists on this workstation. Both Q1 and Q4 need it.
Procedure (hard rule 4): read-only `curl` from https://zenodo.org/records/23003785 into its own new
directory `sources/raw/vid01-score-2026-10-13/`; never executed; text by
`research/.venv/bin/python -I` (local, one process, seconds); sha256 of each PDF compared against
the pinned values in `docs/research/sources/bib-day.md` (Z23003785
`22bb4ef8eae7d5c4756987e5418bf26d795ac65e58f36072c393735bdf7a37b2`; Z23003785-f2 addendum
`d55e8a030716a0b913082dd04fd5d8967695775814265d348886d314d8df0ce7`).

**Gate G0.** If either hash differs from its pinned value: **stop Q1 and Q4**, score Q2, Q3 and Q5
only, and record the difference as a versions-ledger finding. A changed text is a separate result,
not a silent substitution. Prior probability is not negligible: the Zenodo record was already
modified once (2026-10-04) and Z22903977's file was replaced on 2026-10-13.

- **Predicted:** both hashes match (the audit fetched this record after the 2026-10-04
  modification, and the pinned values are from that fetch).

## Q1. The d-coefficient conflict: GGR-13 / GGR-14 against A4d

**The quotes.** GGR-13 (t=01:50:52): "he's still using the de coefficient in mittens". GGR-14
(t=01:51:14): "he calculates it at 450,000 generations and then he multiplies it by the D
coefficient in order to cut it almost in half to like 225,000 generations or whatever and he's
still using that number for all his math."

**The audit's position now.** A4d: `internal: holds`, source note "The 3.0 text has no d term
(searched 'turnover' and 'd =')", 252,000 nominal generations, and a Weaknesses line recording that
the Appendix D human-derived rate (A5e) "cites the 'Bio-Cycle correction for overlapping
generations'". R-3 recorded three RD readings of "in mittens" and declared no winner.

**Day-side prediction.** The search returns no `d` term and no 0.45 applied to generations anywhere
in the 3.0 body. Reading (a) governs: "mittens" is the pre-3.0 / *Probability Zero* line, where
450,000 × 0.45 = 202,500 is exactly the audit's own TW-01 figure (`A-mittens-formula.md` line 39;
A4 `derived:`). The host's own narration agrees ("He kind of throws the D coefficient off to the
side. It no longer seems nearly as important as it was in probability zero", t=01:49:52). A4d is
untouched and the panel's charge is, on this reading, about a document it does not name.

**Critic-side prediction.** The search returns a `d`, a 0.45, or a Bio-Cycle/overlap correction
*inside the 3.0 body*, not only in Appendix D. Reading (b) governs: A4d's source note is false,
"no d term" was an incomplete search by this audit, and A4d's internal verdict cannot stand on a
premise the text contradicts.

**Registered bands — exhaustive over search outcomes.** Search terms, fixed in advance, run over
the re-fetched body **and** the addendum/Appendix D: `turnover`, `d =`, `d=`, `0.45`, `Bio-Cycle`,
`Biocycle`, `bio-cycle`, `overlapping generations`, `450,000`, `450000`, `225,000`, `202,500`,
`252,000`. Hits reported verbatim with locators.

| Band | Search outcome | Governing RD reading | A4d `internal` |
|---|---|---|---|
| **1a** | no hit for any d-term (`turnover`, `d =`, `d=`, `0.45`) and no overlap/Bio-Cycle hit anywhere, body or appendix | (a) pre-3.0 | **holds**, unchanged; *and* A4d's own Weaknesses line (the Bio-Cycle citation) is an audit error to be corrected |
| **1b** | no d-term in body; `Bio-Cycle` / `overlapping generations` present only in the appendix / Appendix D rate | (c) 3.0-including-Appendix-D, partly right | **holds**, with a `reading-dependent:` comment and a Readings table; the Weaknesses line is confirmed |
| **1c** | a d-term (`d =`, `0.45`, `turnover`) applied to generations in the **body** | (b) 3.0 body | **moves** — the source note is false; verdict re-derived on the actual text, `pending` at minimum until the recomputation is checked |
| **1d** | `450,000` or `225,000` present in 3.0 in the generations role | (b), strongly | **moves**; A4d's "252,000 nominal generations" characterisation itself fails |
| **1e** | hash mismatch (G0) | — | **not scored**; versions-ledger finding instead |

**Predicted band: 1b.** Reason: A4d's Weaknesses line already records the Bio-Cycle citation, so a
hit is expected in the Appendix D material and not in the body. Under 1b the field does not move
but *acquires* a Readings table and a `reading-dependent:` comment, which counts separately
(rule RD, `R4-X1-verdict-rule.md` §RD). Note the asymmetry I am registering against myself: 1b is
the band that confirms the audit's existing text, so it is the band I am most likely to see
because I expect it. The verbatim hits with locators are the check on that.

**What no band licenses.** Nothing here scores whether the panel's speaker *believed* he was
describing 3.0. The RD field takes the reading under which the quoted statement is most
defensible — not the reading best for either side (rule RD, explicit).

## Q2. A5h: does anything move from GGR-33 / GGR-34?

**The quotes.** GGR-33 (t=03:46:03): "This is supposed to be a genetic load that he's calculating.
This is not the genetic load calculation. You wouldn't use a selection coefficient. Famously, what
you would use is the mutation rate." GGR-34: "what the genetic load is based on one minus mu raised
to the number of lossi, not one minus s raised to the number of lossi".

**A5h now.** `internal: arithmetic-error` (3.2e9 × 1.2e-8 × 100 = 3,840, not 38,400; downstream
0.999^384 = 0.68 against the printed 0.02, 0.99^384 = 0.021 against the printed 1e-17 — both move
>25%, rule R1). `external: pending`. Responses: "In support: none located."

**Criterion registered in advance.** `external` moves `pending` → `contested` **iff** a located
external objection bears on the **conclusion** of the quoted statement ("every individual carrying
the supermutator allele is functionally dead") in a direction that weakens it. An objection that
bears only on the model while leaving or strengthening the conclusion's direction is recorded in
Responses and in the Readings/ledger, and `external` stays `pending`. `internal` is independent of
this objection entirely: the 10× slip is Day's own arithmetic on his own printed inputs.

| Band | Finding | A5h `internal` | A5h `external` |
|---|---|---|---|
| **2a** | objection is right in theory and weakens the "functionally dead" direction | arithmetic-error (unchanged) | → **contested** |
| **2b** | objection is right in theory but leaves or **strengthens** the direction | arithmetic-error (unchanged) | **pending**, unchanged, with the reason stated and the objection added to Responses |
| **2c** | objection is wrong in standard theory | arithmetic-error (unchanged) | **pending**, unchanged; the objection goes to the critic-side ledger |
| **2d** | objection reaches the arithmetic too | → re-derived | — |

**Predicted band: 2b.** R-2 already records both halves and they point the same way: equilibrium
mutational load is a function of U, not s (Haldane 1937; Muller 1950, L ≈ 1 − e^−U), so the
critics are right that s does not belong in a load calculation — **a valid critic-side point, and
it is recorded as such** — but on their own e^−U at A5h's corrected U = 384, carrier fitness is
e^−384 ≈ 1.7e−167, independent of s, which *strengthens* "functionally dead" and removes the
s = 0.001 escape (0.68) that A5h records as the surviving counterexample. Both halves go in the
write-up with equal prominence. If the honest answer is "nothing moves", that is the result.

**Day-side prediction:** 2b (adopting the objection costs the critics their own escape).
**Critic-side prediction:** 2a (an external objection now exists where "none located" was
recorded, and `pending` understates the state of the corpus).

## Q3. Branch G: how far do GGR-41..GGR-44 meet GGR-19?

**GGR-19 (the target, relayed from a Reddit commenter with a master's in mathematics, t=01:54:58):**
"because the coefficient of variation goes to zero as in increases, Fischer's fundamental theorem
of natural selection implies that the rate of increase in mean fitness must also go to zero as n
increases and that this makes a parallel fixation selfdefeating."

**The two answers.** (i) **Recombination**, GGR-41/GGR-42 (t=01:57:03, 01:57:44): "you can get two
beneficial mutations that occur separately and they can recombine together and then you can select
for both at the same time and they can achieve fixation together." (ii) **The infinitesimal model**,
GGR-43/GGR-44 (t=02:13:47, 02:14:07), introduced as "the pop gen answer to go back to Bernoli's
law", with GGR-27..GGR-29 as its second point.

**Criterion registered in advance.** An answer **meets** GGR-19 iff it engages the inference
`CV(K) → 0 as n → ∞` ⟹ (by Fisher's fundamental theorem) `d(mean fitness)/dt → 0`. Three gradations,
fixed now: **meets** (addresses the inference and shows where it fails, with or without numbers);
**on point** (names the quantity the inference misuses, or the regime it assumes, without showing
the failure); **adjacent** (answers a different premise of the barrier).

| Band | Finding | What moves |
|---|---|---|
| **3a** | either answer *meets* GGR-19 | G `external` re-derived; a critic-side node is warranted |
| **3b** | infinitesimal model is *on point*, recombination *adjacent* | nothing moves; G `external` already `contested`; G5 already holds the same step; proposal only |
| **3c** | both merely *adjacent* | nothing moves; recorded as a gap in the critic reply |
| **3d** | an answer is wrong as stated | critic-side ledger row |

**Predicted band: 3b.** The infinitesimal model (Fisher 1918) is the standard model of exactly the
regime GGR-19 posits (many loci, small effects) and speaks to the premise "variance in fitness is
small"; but the panel gives no derivation and never touches the CV→variance substitution, which is
the actual defect. That defect is already the audit's own node **G5** (Matev: "While this
coefficient of variation does go to zero as n increases, the variance of the beneficial allele
count of an individual just increases as n increases", `internal: holds`) and G's own `derived:`
line (Var = n/4 = 39,250 at n = 157,000; only CV falls, as 1/√n). So the panel's second answer is
a weaker, model-naming restatement of a point the audit already scores, and it does not add a
verdict move. Recombination answers the *waiting-time / linkage* premise instead — which is where
`R4-G1.md` is directly on point (free recombination: joint fixation 1.03 ± 0.02 × p², i.e.
independence; joint < product when linked, 0.84 / 0.65, or clonal, 0 — Day's stated direction; the
λ flip band 12.3–17.2) — and is therefore *adjacent* to GGR-19 but a real argument against the
surrounding waiting-time framing.

**Standing warning to myself, registered.** The audit's own MAJOR-1 was an error *against* the
critics (an evaluative sentence written without reading their answer). The correction for that is
to read the answer, which is done; it is **not** to score the answer more generously than the
criterion above licenses. Over-crediting here would be a second error, not a repair of the first.
A reviewer should check band 3b against the criterion, not against the history.

## Q4. NOTE-5: is the Bernoulli barrier in MITTENS 3.0?

**The disagreement inside the panel.** GGR-12 (t=01:50:12): "Essentially, he omits the averaging
error stuff as well as the Bernoli barrier stuff." GGR-20 (t=01:55:39): "it doesn't really matter
for the full argument anyways because he effectively abandons it by Mittens 3.0. It's mentioned
once in that paper and not defined."

**The audit's position now.** `Ge-bb-omitted-from-3-0.md` (`internal: pending`) already states, in
its Formal statement, that the 3.0 paper "contains 'Bernoulli Barrier' only in a rhetorical
sentence in s1". Day's own claim (Ge Statement) is "I omitted both the Bernoulli Barrier and the
Averaging Problem, even though both of them remain entirely correct."

**Registered search.** Terms over body and appendix: `Bernoulli`, `Bernoullian`, `barrier`,
`Averaging`, `averaging problem`, `law of large numbers`, `coefficient of variation`. Count and
quote every hit with its section locator.

| Band | Search outcome | Ge `internal` |
|---|---|---|
| **4a** | exactly one "Bernoulli Barrier" occurrence, rhetorical, undefined | GGR-20 exact, GGR-12 right in substance; Ge's Statement true as stated → `internal` **moves `pending` → `holds`** |
| **4b** | zero occurrences | GGR-20 wrong on "mentioned once", GGR-12 exact; Ge `holds` a fortiori; Ge's Formal statement is an audit error to correct |
| **4c** | more than one occurrence, or one with a definition/derivation | GGR-20 and Ge's "omitted" both strained → Ge `internal` re-derived, `pending` or lower |
| **4d** | hash mismatch (G0) | not scored |

**Predicted band: 4a**, from Ge's existing Formal statement. Day-side and critic-side predictions
coincide here: the panel's GGR-20 and Day's own blog statement say the same thing. Note that 4a is
a result **for Day on fidelity** — his blog statement about his own paper is accurate — and
simultaneously vindicates the panellist at GGR-20 over the panellist at GGR-12 on the literal
wording. The audit's own 3.0-text claim gets checked for the first time since the text was lost.

## Q5. The three credits to Day

Not predictive; registered as a commitment under hard rule 1 ("record valid points for either side
as prominently as errors"). GGR-04 (the panel's mathematician: "you did the division correctly",
governing reading the literal concession under R-4, with the bathos reading recorded beside it),
GGR-45 (t=01:22:28, "genuinely this was a good exercise and the response the review that he got was
quite fair I think" — from the same panellist who is harshest on the paper's reference count) and
GGR-46 (t=01:51:34, "Remember how D was one earlier? This goes back to the whole he's trying to
give conventional science the bestcase scenario numbers") go in the write-up's body with the same
weight as the errors, not in a footnote. **Registered prediction:** at least one of the three bears
on a claim file's Responses section (GGR-46 on A4 and on the charity question at A4d), so "credit
recorded" is not merely a presentational commitment.

## What this pass may not do

Per the brief: no `QUEUE.md`, `REVIEW.md`, `RESULTS.md`, `hierarchy.yaml`, argmap, board or counts
refresh — that is the integration task after the three reviews and the fix pass. No new claim file
(proposals only). No `na-workhorse` run (busy with `ph2` until 2026-10-16; nothing here needs it).

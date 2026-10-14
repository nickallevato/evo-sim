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

---

# Results (post hoc — written after the re-fetch, 2026-10-13)

Everything below this line was written **after** the MITTENS 3.0 text was fetched and opened, i.e.
after the Predictions section above was committed (`e857d1f`) and pushed. Separate commit, labelled
post hoc, per hard rule 5.

## Gate G0: the re-fetch — PASS

Read-only `curl` into its own new directory `sources/raw/vid01-score-2026-10-13/` (gitignored,
hard rule 3; `chmod 444`; never executed, hard rule 4). Text by `pdftotext -layout` (738 lines main,
137 addendum). No computation beyond this; `na-workhorse` untouched.

| File | sha256 (fetched) | pinned in `bib-day.md` | Match |
|---|---|---|---|
| main.pdf (`MITTENS 3.0 …pdf`, 114,352 B) | `22bb4ef8eae7d5c4756987e5418bf26d795ac65e58f36072c393735bdf7a37b2` | Z23003785, same | **yes** |
| addendum.pdf (`Addendum …pdf`, 43,698 B) | `d55e8a030716a0b913082dd04fd5d8967695775814265d348886d314d8df0ce7` | Z23003785-f2, same | **yes** |

Zenodo's own md5s agree (`7ca0bc6a72964a5ba52139fbf630d399`, `a8b66c5ede94f90206448c746b74fb79`),
file sizes match the bib row, and the record's `modified` is still `2026-10-04T18:19:52Z` — the
record has **not** been revised again since the audit's pinned fetch, unlike Z22903977 (replaced
2026-10-13). **G0 passes; Q1 and Q4 are scored.** Registered prediction: hit.

**Integrity by-product.** Three claim-file Statement quotes whose local source file was lost
re-verify **verbatim** against the hash-matched text: A4d (main.txt:25, abstract; also at 675–676),
A5h (main.txt:459–466, §6.4 "The Breeding Reality Principle"), G1 (main.txt:572–574, §8.1). No
quote drift. The audit's quoting survived the loss of `sources/raw/`.

## Q1. The d coefficient: GGR-13/GGR-14 against A4d

### The registered search, every hit verbatim

Case-insensitive over `main.txt` (body; 3.0 has no appendix of its own — see below) and
`addendum.txt`.

| Term | Hits | Verbatim, with locator |
|---|---|---|
| `turnover` | 1 | main:274 "…the correct measure for comparison with species-level divergence data, which also measures net fixed differences, **not gross turnover**." (§4.2; not the selective turnover coefficient) |
| `d =` | 0 real | main 0; addendum 2 are case-insensitive substring artefacts of "**SD = ** 28.5", "**SD = ** 720.0". Case-sensitive `d =`: **0** in both files. A post hoc regex for a standalone `d` token, `(^\|[^A-Za-z])d([^A-Za-z]\|$)`, returns **0 in both files case-sensitively** — i.e. 0 lowercase `d` tokens. **Corrected in the fix pass (correctness MINOR-1):** run *case-insensitively*, as this table's heading says, it returns **3 in `main.txt`** — `Appendix D)` (653), `Appendix D.` (724) and `Yoo D, et al.` (738), two citations and an author initial, **none a coefficient** — and 0 in the addendum |
| `d=`, `0.45`, `Biocycle` | 0 | — |
| `450,000`, `450000`, `225,000`, `202,500` | 0 | — |
| `Bio-Cycle`, `bio-cycle`, `overlapping generations` | 1 (same sentence) | main:652, **§8.6**: "The human-derived fixation rate, calculated independently from human parameters alone using Kimura's fixation time formula and the **Bio-Cycle correction for overlapping generations**, yields approximately one fixation per 27,600 effective generations (Day and Athos 2025, Appendix D)." |
| `252,000` | 8 main + 2 addendum | main:25, 280, 488, 517, 524, 599, 654, 676; addendum:39, 75. Every one is "252,000 available generations" / "252,000 human generations" / "252,000 generations". **Never multiplied by anything.** main:488: "The divergence time is 6.3 million years. At 25 years per human generation, this provides 252,000 generations." |

Post hoc extra terms (labelled as such): `selective turnover` 0, `d coefficient` 0, `generation
length` 0, `0.4` 0. `coefficient` 2: main:463 "the average selection **coefficient** against each
deleterious mutation" (§6.4) and addendum:66 "the **coefficient of variation**" (descriptive stats
of per-population fixation counts).

### Band: 1b′ — not a registered band. Pre-registration defect, recorded against the audit.

Registered band **1b** required the Bio-Cycle hit to be "present **only in the appendix** /
Appendix D rate". It is not. It is in the **body, §8.6**, and it is a **citation to a different
document**: "(Day and Athos 2025, Appendix D)". **MITTENS 3.0 has no Appendix D of its own** —
`grep '^Appendix'` over the section headings returns nothing; the paper runs §1–§9 plus a separate
addendum on per-population dispersion. Band 1c required a d-term in the body, and there is none.
So the outcome is **1b′: no d-term anywhere, overlap correction cited in the body**, which my band
table did not contain. **The table was not exhaustive. That is the audit's error, not either
side's,** and it goes in "Both" below. The substantive finding is unaffected and arguably
*sharper* than 1b: the overlap correction is more central to 3.0 than band 1b supposed.

### Readings (rule RD) — of the critic statement GGR-13/GGR-14

**Revised in the fix pass under lead rulings R-8, R-9 and R-10.** Two changes: the two quoted
sentences are scored as **separate propositions** (R-8), because GGR-13's core assertion and
GGR-14's elaboration are not the same claim and do not stand or fall together; and reading (a) is
**struck as governing** (R-9), staying in the table with its verdict but unable to set the headline.

| Reading | What "mittens" denotes | Scored against the hash-verified 3.0 text | GGR-13 "he's still using the de coefficient in mittens" | GGR-14 "he calculates it at 450,000 … multiplies it by the D coefficient … still using that number for all his math" |
|---|---|---|---|---|
| **(a)** — **extended reading, may not govern (RD line 202)** | the pre-3.0 / *Probability Zero* line of argument — **a different object** from the paper the exchange is about | 450,000 × 0.45 = 202,500, "like 225,000 generations or whatever"; this is the audit's **own** TW-01 figure (`A-mittens-formula.md` line 39; A4 `derived:`) | **accurate** | **accurate** |
| **(b)** | the MITTENS 3.0 body | 0 standalone lowercase `d`, 0 × `0.45`, 0 × `450,000`; 252,000 appears 10 times and is never cut, including at §8.6 itself ("Applied to 252,000 generations provides 8 achievable fixations", main:653–654) | **contradicted** (no `d` token anywhere in the body) | **contradicted** |
| **(c)** — **governs among in-scope readings** | 3.0 **as it stands, including what it incorporates by citation** | 3.0 has no Appendix D of its own; §8.6 of the **body** cites *Day and Athos 2025*, Appendix D, for a rate "calculated … using Kimura's fixation time formula and **the Bio-Cycle correction for overlapping generations**", quoted in **"effective generations"** — the audit's own `C2-bio-cycle-d.md` (line 3) defines Bio-Cycle as `g_eff = d × g_nominal`, so a rate denominated in *effective* generations has d inside it by definition. `effective generation` occurs **exactly once** in body and addendum, main:653, in that sentence | **accurate** as to this step: the d correction is still in play in 3.0, inside the 27,600 rate | **contradicted**: `450,000`, `225,000`, `202,500`, `0.45` are 0 hits; 252,000 is used uncut everywhere |

**Headline grade of the quoted statement under the governing reading (c): `partial`** (fidelity vocabulary; written "partly accurate" in the original R-8 wording, normalised at integration) —
accurate core, inaccurate elaboration, which is exactly what `partial` names (R-8). The
Day-side steelman's request to regrade (c) to `contradicted` is **declined**; its evidence is
nonetheless adopted and is what makes the GGR-14 column read `contradicted`.

**What the §8.6 arithmetic does and does not settle.** The printed "8 achievable fixations"
reconciles with neither candidate exactly: 252,000/27,600 = **9.13** (a 12% gap `A5e` line 26
already records as unreconciled in Day's own sentence) and 113,400/27,600 = **4.11** (off by a
factor of two). So the figure does not *prove* the absence of d — but it is not uninformative
either, and the critic-side steelman's "discriminates nothing" is overstated (R-8): the printed 8
is consistent with the **uncut** 252,000 and not with a d-cut count. Both halves are recorded.

**On reading (a) (R-9).** `R4-X1-verdict-rule.md` §RD line 202: "Extended readings (a different
object, or a wider claim) are reported with their own verdicts but **cannot set the verdict field
or the headline tag**." Reading (a) is the pre-3.0 / *Probability Zero* line — a different object
from MITTENS 3.0 — so it is recorded above with its `accurate` verdict and its TW-01
cross-reference and is **struck as governing**. Readings (b) and (c) are the same object at two
scopes; (c) is the scope under which the quoted statement is most defensible, so **(c) governs**.
All three reviewers reached this independently. The headline therefore is not "the charge is not
about 3.0" but "**the charge's core is accurate of the §8.6 step and its elaboration is false of
3.0**".

**The t=01:49:52 line, corrected (R-10).** This write-up's registered Day-side prediction and the
paragraph that stood here called it "the host's own narration" and treated it as corroboration for
(a). Both are wrong. The line sits inside the **GGR-11** turn (t=01:47:28–01:51:34, unbroken, no
name spoken for the speaker), which the EVO-69 fix pass re-attributed to **`panel`** under its own
MINOR-1 rule; the write-up asserted an attribution the audit had struck three days earlier. The
quote is **not** withdrawn — it is a real panel turn and it does corroborate A4d's *fact* from a
hostile source — but it cannot corroborate reading (a), because the panellist is speaking **about
3.0** ("In mittens 3.0, he completely retracts all of his arguments …") and GGR-13 is the solicited
**reply disagreeing with him** ("Does that sound right to you, especially Grayson?" → "Yeah, I I
think that he's Yeah, this he's still using the de coefficient in mittens"). What it shows is that
**the panel is internally split about 3.0** — one panellist says Day throws d aside, another says he
is still using it — and that is **a point for Day**, recorded as such. `quotes-critics.md` line 846
carried the same error and is corrected in this pass. The registered prediction paragraph at line
71 above is left byte-identical for registration integrity (hard rule 5); this paragraph is its
correction.

### Verdict: A4d `internal: holds` — unchanged, and now **verified** rather than asserted

**And A4d's verdict field is *not* made reading-dependent.** This is a deliberate departure from
registered band 1b and from the brief's instruction as literally written, so it is flagged for the
reviewers to rule on. The reason: rule RD governs a verdict **that depends on how a quote is read**.
A4d's does not. Before the re-fetch, reading (b) was live and A4d's `holds` rested on a search of a
file that no longer existed; now the text settles, under *every* reading, that MITTENS 3.0 contains
no d term. The re-fetch converted a reading-dependency into a fact. What remains reading-dependent
is the **critic statement** GGR-13/14, which has no claim file of its own, so the Readings table
belongs in A4d's R4 paragraph as the record of the challenge, not in its verdict comment, and this
verdict must **not** be added to the "reading-dependent" count (rule RD, `R4-X1-verdict-rule.md`
§RD, last bullet). If a reviewer rules the other way, the fix is one comment line and one count.

**Ruled on (fix pass).** All three reviews and the lead agree the departure was right, and the
reason is named: §RD line 198 — "A claim whose **formal statement fixes the reading** (A2e, a
count) is **`SCOPED`, not reading-dependent**". A4d's Formal statement is exactly such a fix
("F_max(3.0) = 252,000 / 1,322 = 190.6, **with no d**"), so A4d is **`SCOPED`**: no
`reading-dependent:` comment, no separate count. **The defect was in the registration, not in the
execution** (lead, R-15), and it is re-booked below as a second pre-registration defect of this
pass rather than as a miss charged to the analyst.

### Who this helps, at Q1

- **Day:** **MITTENS 3.0's own generation count is 252,000, uncut, and nothing in the body or the
  addendum multiplies it** — 0 standalone lowercase `d`, 0 × `0.45`, 0 × `450,000`, 0 ×
  `selective turnover`, and §8.6 applies its cited rate to the full 252,000. A4d's `holds` survives
  its first real test. GGR-14's elaboration is **contradicted** under *both* in-scope readings. And
  the panel is **internally split about 3.0**: the GGR-11 turn says Day "throws the D coefficient
  off to the side", which GGR-13 is then solicited to, and does, contradict — a hostile-source
  corroboration of A4d's central fact (R-10).
- **Critics:** reading (c) **governs**, and under it GGR-13's core assertion is **accurate**, not
  merely "partly right": §8.6's single human-derived throughput number is, in the paper's own
  words, computed with "the Bio-Cycle correction for overlapping generations" and quoted in
  "effective generations" — the vocabulary the audit's own `C2-bio-cycle-d.md` defines as
  `g_eff = d × g_nominal`. So **the d correction is still in play in MITTENS 3.0**, by citation,
  and 3.0 nowhere reconciles a rate per *effective* generation divided into a *nominal* count.
  §8.6 is not a footnote: the paper calls the objection it answers there "the most persistent
  objection to MITTENS". GGR-14's arithmetic (450,000 × 0.45) is exactly the audit's TW-01. None of
  this is a critic-side error.
- **Audit:** the band table (above); A4d's Weaknesses line calls it "the later 'Appendix D'
  human-derived rate", which reads as though 3.0 has an Appendix D (it does not — corrected); the
  "clean of the d coefficient" headline, which a token search cannot establish (corrected below,
  and it is **the third audit error against the critics from this source**); and the misattributed
  t=01:49:52 line (R-10, corrected above and in `quotes-critics.md`).

## Q2. A5h: nothing moves — band 2b, as registered

**New verified fact, not previously on the record: the word "load" occurs ZERO times** in MITTENS
3.0 and in the addendum (`grep -i load` over both files). §6.4's own words, verbatim (main:462–463):
"Under multiplicative fitness, the fitness of such an individual is (1 − s)^3,840 where s is the
average selection coefficient against each deleterious mutation." That is a **per-carrier fitness
from its own deleterious count**, not a population load. R-2's half (ii) was asserted in the fix
pass from the quoted excerpt; it is now verified against the whole hash-matched text.

| Half | Finding |
|---|---|
| **For the critics (GGR-33/GGR-34)** | **A valid point, recorded as prominently as the errors.** Equilibrium mutational load is a function of the genome-wide deleterious rate U and **not** of the per-mutation selection coefficient s (Haldane 1937; Muller 1950, L ≈ 1 − e^−U). GGR-34's "one minus mu raised to the number of lossi, not one minus s" is right in standard theory. The s-dependence of A5h's "functionally dead" is a property of Day's model, not of biology. |
| **Its cost to the critics (i) — the one that bites** | On the panel's **own** e^−U, at A5h's corrected U = 384, carrier fitness is e^−384 ≈ 1.7e−167 (384·log₁₀e = 166.8), independent of s. Adopting the objection therefore **strengthens** Day's stated direction and **removes the s = 0.001 escape** (0.999^384 = 0.68) that A5h records as the one surviving counterexample to "functionally dead". **Regime named (fix pass, both steelmen):** e^−U is the mutation–selection-balance mean fitness of a lineage that keeps the allele, not the one-generation fitness of a first-generation carrier (which under Day's own multiplicative model is 0.999^384 = 0.681 at s = 0.001). Relativised to wild type (U ≈ 3.84, e^−3.84 = 0.0215) the equilibrium ratio is e^−380 = 9.29e−166, so the direction survives relativisation. |
| **Its cost to the critics (ii) — demoted in the fix pass** | GGR-33's premise — "This is supposed to be a genetic load that he's calculating" — is not matched by Day's vocabulary: "load" occurs 0 times. **But a word count does not answer a conceptual attribution** (both steelmen, independently: Day MINOR-1, critic MINOR-3). The most defensible reading of GGR-33 under rule C is about the *quantity* ("a genetic load that he's **calculating**"), and §6.4 does compute a carrier's fitness from its own deleterious-mutation count, which is the quantity classical load theory handles. What the 0-count does establish is narrower: "**the** genetic load calculation" is not what §6.4 calls itself. Leading with it would be literal-fact-checking the wrong object, which is the overreach `RH5` charges to **any** side — "A critic who literal-fact-checks Day's rhetoric and presents it as a refutation gets an N entry for overreach. So does Day" — and so does the audit. Demoted below cost (i) here and in A5h. |

**Registered criterion applied:** `external` moves `pending` → `contested` only if a located
objection weakens the conclusion's direction. This one leaves it strengthened. **Band 2b.**

**The criterion is stricter than the audit's own operative use of `contested`, and this pass says
so rather than asserting it away** (fix pass, critic-side MAJOR-5; lead ruling R-14). The write-up
originally claimed the narrow reading "is the one the vocabulary supports". That claim is
withdrawn. `criticality/METHODS-AND-LIMITATIONS.md` line 45 (MA-08) records the opposite:
"`contested` is two-thirds of the external column … The word covers at least five situations:
disputed in the literature, **true only in the tested regime**, conditional on an unsourced
parameter, leaning one way but short of decisive, and **not examined**. In a seeded sample of 20,
6 had no recorded basis at all." A5h's "functionally dead" is true only in the tested regime —
Day's multiplicative model with his chosen s — which is one of those five verbatim, and the audit
elsewhere awards `contested` for "not examined", which is strictly less than what A5h now has on
the record. **`pending` nevertheless stands and Q2 is not rescored**: the criterion was fixed
before the evidence was read (`e857d1f`, byte-identical per the correctness review's diff check),
and widening it now would be the post hoc widening hard rule 5 exists to prevent. The
inconsistency is in the **vocabulary**, not in this check; changing it is a rule change and takes
the freeze procedure in `DECISIONS.md`. **Routed to the batch-15 criticality pass as a named
finding** (Open item 11).

- **A5h `internal`: `arithmetic-error` — unchanged.** The 10× slip (3.2e9 × 1.2e-8 × 100 = 3,840,
  printed 38,400) is Day's own arithmetic on his own printed inputs and is untouched by any
  modelling objection. Re-verified verbatim against the re-fetched text.
- **A5h `external`: `pending` — unchanged, and this is the result**, not a failure to decide. The
  objection is added to A5h's Responses **under Against**, where only RE-02 / A2h stood; it is now
  an objection on the record that does not move the field, with the reason stated. *(Corrected in
  the fix pass, correctness MINOR-2: the write-up said the objection went where "In support: none
  located" had stood. It did not — that line is a separate entry, refers to support for **Day's**
  claim, and is untouched by the objection.)*
- **"In support: none located" is now inaccurate, and this pass is what made it so** (fix pass,
  Day-side MAJOR-3, hard rule 1). This check located, for the first time, external material bearing
  on the **direction** of A5h's conclusion: the critics' own standard-theory formula (GGR-34;
  Haldane 1937 / Muller 1950) applied at A5h's corrected U = 384. Under the registered criterion it
  does not move `external`, exactly as the critic objection does not — but a critic objection that
  fails the criterion was still written into Responses while supporting material that fails the
  same criterion was not, and that asymmetry is the one hard rule 1 exists to catch. A5h's
  Responses is corrected in this pass; the field is untouched.
- **Independent credit to the critics:** GGR-31/GGR-32 reach 3,840 — the audit's exact value — by a
  six-person panel working without reference to this audit. That is the strongest kind of
  corroboration A5h's `arithmetic-error` can get.

## Q3. Branch G: GGR-41..GGR-44 against GGR-19 — band 3b, as registered, with one refinement

Criterion registered in advance: an answer **meets** GGR-19 iff it engages the inference
CV(K) → 0 ⟹ (Fisher) d(mean fitness)/dt → 0.

| Answer | Grading | Why |
|---|---|---|
| **Infinitesimal model**, GGR-43/GGR-44 (t=02:13:47, 02:14:07) | **on point** | It is the standard model of exactly the regime GGR-19 posits (many loci, small effects), it is introduced explicitly as "the pop gen answer to go back to Bernoli's law", and it speaks to GGR-19's premise about variance in fitness. But it gives **no derivation** and never touches the CV→variance substitution, which is where the inference actually fails. |
| **Second point of answer (ii)**, GGR-27..GGR-29 (t=02:15:08, 02:15:49) — *row added in the fix pass, correctness MINOR-3* | **adjacent** | The registration defines answer (ii) as GGR-43/GGR-44 "with GGR-27..GGR-29 as its second point", and the correctness review confirms from the transcript that GGR-43, GGR-44 and GGR-27..GGR-29 are **one unbroken turn** (no `>>` between 02:13:47 and 02:15:49), so the second point is in scope and was not graded. On content: dN/dS and heterozygosity varying across one genome answers the drift-versus-selection dichotomy (GGR-22..GGR-24), not the CV→variance step. **The overall grade of answer (ii) is unchanged at *on point*,** set by its stronger half. |
| **Recombination**, GGR-41/GGR-42 (t=01:57:03, 01:57:44) | **adjacent** to GGR-19 — but on point against a premise MITTENS 3.0 states at §2 | It answers linkage and the waiting-time framing, not the CV step. See the refinement below. |

**Nothing moves on branch G. The stated ground has been corrected** (fix pass, critic-side MAJOR-4,
accepted). The write-up originally said the panel's answer is "strictly weaker" than G5 and that
"a critic-side node whose content is strictly weaker than an existing critic-side node moves no
verdict". That ground is wrong, because the two are about **different quantities**: **G5** (Matev,
`internal: holds`) attacks the substitution from the **allele-count** side — "the variance of the
beneficial allele count of an individual just increases as n increases", Var(K) = n/4 — while
**GGR-43** attacks it from the **fitness-variance** side, verbatim: "I'll give the pop gen answer to
go back to Bernoli's law **if you want to know how it is that variance and fitness can be
maintained** even if you have very … low fitness impacts of each individual mutation", naming the
infinitesimal model as "the fundamental model of quantitative genetics". This write-up's own
statement of the defect is that "Fisher's theorem relates the response to additive genetic
**variance in log fitness**, not to the CV of a count" — so the panellist names the quantity the
inference misuses and the standard model of the regime. GGR-43/44 therefore sits at the **top** of
*on point*, not the bottom, and the harvest note says so too ("it addresses GGR-19's premise
directly"). **The correct ground for the no-move is independent:** G `external` is already
`contested`, G's own `derived:` line and G5 already carry the algebra (at n = 157,000: Var = n/4 =
39,250 rises, only CV = 0.252% falls, as 1/√n), and GGR-43/44 adds **no derivation**. The Open-2
node proposal therefore stands on its own content, as an independent angle, not as a weaker G5 —
which is the footing it will be judged on at integration.

**Refinement not anticipated in the registration, carried with every qualification both steelmen
attach to it** (fix pass, lead ruling R-12: the refinement is weakened, not deleted, and neither
steelman may carry more weight than its row). GGR-42's speaker attributes to Day the position that
recombination makes fixation *slower* ("but there's recombination and therefore that breaks up
things and it makes it slower"). That attribution is **accurate**, verified verbatim in the
re-fetched §2 (main:128–131): "**No recombination overhead.** In clonal populations, a beneficial
mutation that arises in one individual stays linked to that individual's entire genome. In sexual
populations, recombination breaks linkage, **separating beneficial mutations from one another** and
from the genetic backgrounds on which they arose." On how far `R4-G1.md` backs the panel against
that bullet, the honest statement is the whole of the following and not any one clause of it:

- **Free recombination is Day's own stipulation** (`R4-G1` s7.10) and the measured free row gives
  **independence**: pair ratio **1.029 ± 0.022 × p²** (`R4-G1.md` line 163; the "1.03 ± 0.02" form
  is R4-G1's own Ga summary row, line 318). This is the critics' half and it is pre-registered.
- **The only pre-registered linkage row failed.** `R4-G1.md` line 172: "Pre-registered prediction
  failed at 1 M. I predicted a pair ratio of 0.5–0.95 and got **1.015 ± 0.022** … It did not show
  that interference is absent." The only pre-registered test of Day's sub-multiplicative direction
  at linkage returned independence.
- **The tighter maps that do give Day's direction are labelled post hoc** in `R4-G1.md` itself
  (lines 165–166): 1,000 loci/M → **0.842 ± 0.020**; 10,000 loci/M → **0.652 ± 0.018**; clonal → 0.
  Hard rule 5 owes the label, and this write-up did not give it. These are Day's half.
- **No run exists at human-relevant density.** `R4-G1.md` line 173–174 puts 157,000 loci over
  ~35 M at "about 4,500 loci/M, **between the two tight maps**" — an **interpolation between two
  post hoc rows**, not a run, and the same line calls free recombination "optimistic for humans at
  high concurrency". Neither side may claim the human density.
- **The §2 bullet does not assert what the statistic tests.** §2 says a beneficial mutation "stays
  linked to that individual's entire genome" — linkage retention and hitchhiking throughput in a
  clonal sweep — whereas R4-G1's pairwise ratio tests whether two *separately arising* beneficials
  fix jointly above or below p². Scoring a bullet with a statistic of the audit's choosing rather
  than the one the bullet states is the substitution hard rule 1 exists to catch.
- **3.0 already internalises clonal interference** (main:13, 43, 65, 109, 272, 378, 573, 689;
  addendum:35 "a demonstration of what clonal interference does to fixation counts … it reverses
  them"), and §9 states the conclusion the objection would have to attack: "fixation is
  bottlenecked by sweep dynamics, not mutation supply".
- **And the cost to Day stays on the record:** `R4-G1.md` line 173 — "a clonal-derived rate is
  plausibly a **lower** bound for a recombining population" — with the clonal row's joint fixation
  at 0. If the LTEE rate is a floor rather than a ceiling for recombining humans, §8.6's "most
  generous possible assumption" framing is weakened. That is the critics' strongest form of this
  objection.

The earlier sentence "Day's own stated direction holds only in the linked and clonal cases" is
**withdrawn**: it rested on the two post hoc rows against a failed pre-registered row.

**Band 3d was considered (post hoc check, fix pass; critic-side MINOR-5, a finding against the
reviewer's own side).** Registered band 3d is "an answer is wrong as stated → critic-side ledger
row". The results section graded 3a/3b/3c and never said whether 3d was reached, which a pass
claiming its bands were applied owes. The candidate the critic-side steelman named is at
**t=01:55:19**, answering the relayed GGR-19 formulation; verbatim from the transcript, ASR
spelling preserved (the review's own rendering reads "Haldane's", the captions read **"Hallane's"**):
"I'm going to say that sounds like vaguely related to **Hallane's** dilemma," (t=01:55:19) …
"but that's not a thing anymore. That's not like actually an issue." (t=01:55:39).
**Finding: band 3d is not reached; the line is tagged `rhetoric` under RH1 and recorded in
`ledgers/slips.md` as RH-34.** Reasons, in order: (i) RH1 requires the tag before any scoring, and
this is a dismissal with no argument attached, of the type RH2 does not literal-fact-check;
(ii) its literal content — that Haldane's dilemma is no longer a live problem — is *not* wrong as
stated on the audit's own record, where branch H's `H-haldane-limit` carries `external: contested`
and the same panel's GGR-08 states the standard view ("Haldane's dilemma being not so much of a
dilemma anymore"); it is unsupported, not false, so 3d's "wrong as stated" does not fit;
(iii) RH5 applies the same treatment to the critics as to Day, and the surrounding "that's
preposterous" / "that's just stupid" (t=01:57:03) are already noted at `quotes-critics.md` GGR-19.
So: no critic-side ledger row under 3d, one rhetoric row under RH1/RH5, and the point stands that
the clearest statement of the barrier in the critic corpus was met in the room with a dismissal
before it was met with the infinitesimal model two reels later.

**Note on the target.** Q4 establishes that the Bernoulli Barrier appears in MITTENS 3.0 only as one
rhetorical clause, undefined. So the barrier the panel is answering is the January 2026 Zenodo
paper's (Z18167588, claim G), not 3.0's. Neither side is at fault for that; it is worth stating
because it bounds what the exchange can settle.

**Verdict fields, branch G — all unchanged:**

| Node | Field | Before | After | Why |
|---|---|---|---|---|
| G | external | `contested` | `contested` | R4 F2 and R4 G1 already give the contest its content; the panel adds no numbers |
| G1 | internal / external | `holds` / `contested` | unchanged | §8.1 re-verifies verbatim |
| G5 | internal | `holds` | unchanged | the panel attacks the same substitution from the fitness-variance side with no derivation; G5 keeps the algebra (wording corrected in the fix pass, critic-side MAJOR-4) |
| Ge | internal | `pending` | **`holds`** | Q4 |

**Proposal, not applied** (the brief forbids new claim files): a critic-side node for the panel's
infinitesimal-model answer, child of G, `attacks` G, `internal: pending` (no derivation given),
quotes GGR-43/GGR-44 — on its own content as an independent angle, not as a weaker G5; and a
defeater pair for the §2 recombination-overhead bullet citing GGR-42 and R4-G1's free row
(1.029 ± 0.022, line 163) **with the post hoc / failed-pre-registration qualifications above
attached to it**. A matching **Day-side defeater** is proposed in the same breath (Open item 9).
For the integration or a later design task.

**The warning I registered against myself, discharged.** MAJOR-1 was an audit error *against* the
critics. The repair is to read their answer, which is done and which produced the recombination
refinement above. The repair is **not** to grade the answer above the criterion. Neither answer
*meets* GGR-19, and saying so is not a dismissal: see Q4 for where the burden actually sits.

## Q4. NOTE-5: the Bernoulli barrier in MITTENS 3.0 — band 4a exactly

| Term | Hits in main + addendum | Verbatim |
|---|---|---|
| `Bernoulli` | **exactly 1** | main:55, §1: "When MITTENS demonstrates that sequential fixation cannot fill the timeline, the defender invokes parallel fixation. **When the Bernoulli Barrier demonstrates that parallel fixation is probabilistically self-defeating, the defender invokes neutral drift.** When neutral theory's own mathematics are shown to require an even longer timeline…" — a paragraph about "the characteristic rhetorical structure" of the polythesis. No definition, no derivation, no number. |
| `Bernoullian`, `barrier` (any other), `Averaging`, `averaging problem`, `law of large numbers` | **0** | — |
| `coefficient of variation` | 1 | addendum:66, descriptive statistics of per-population fixation counts ("SD = 720.0; SEM = 272.1") — unrelated to the barrier |

### NOTE-5 dissolves: the two panellists are not inconsistent

GGR-12 ("Essentially, he omits the averaging error stuff as well as the Bernoli barrier stuff") and
GGR-20 ("It's mentioned once in that paper and not defined") state the **same fact at different
precision**, and **both are exactly right**: the Averaging Problem as a named argument is absent
(`Averaging`, `averaging problem`, `law of large numbers`, `polygenic` all 0 — see the gloss
paragraph below) and the Bernoulli Barrier appears once, undefined. The combined review's NOTE-5 called this a "panel
inconsistency". It is not one. **That is the audit's own error**, recorded in "Both" below.

### Verdict: Ge `internal`: `pending` → **`holds`** (registered band 4a — applied)

Day's statement (Ge): "the MITTENS 3.0 paper … renders those complicating elements moot to such an
extent that I omitted both the Bernoulli Barrier and the Averaging Problem, even though both of
them remain entirely correct." The **omission half is true as stated**, now verified against a
hash-matched text rather than against a file the audit no longer had. One undefined clause is not a
retention of the argument; under rule C this is "omitted". **This is a credit to Day on an accuracy
question about his own work** and it is why Ge's internal field moves. **Scope (correctness
MINOR-4):** band 4a is applied to the **omission clause only** (rule S); the second clause is an
external question, routed below with the field unchanged.

**Which gloss of "the Averaging Problem" was tested** (fix pass, correctness MAJOR-4 accepted). A
token search decides only if "the Averaging Problem" is a **named argument**, and the audit glosses
it two ways. Both are tested here and both give the same answer:
- **Gloss (i), a named argument** — `G2g-appendix-a-fixation-must-be-sequential.md` line 29,
  "(Averaging Problem: polygenic rescue impossible)". The token search decides, and the **decisive
  negative is `polygenic`: 0 occurrences** in body and addendum (post hoc term, added in the fix
  pass), alongside `Averaging` / `averaging problem` / `law of large numbers` 0.
- **Gloss (ii), Day's ¶22 in the same blog post as the Ge Statement** — "the math is an average of
  12 different populations". Here the nearest substantive material is inside the addendum the
  search already covered, and it runs **for** Ge rather than against it: the addendum is titled
  "Per-Population Dispersion and Best-Case Robustness", reports each population separately, and
  says at §3 (addendum:83–84) verbatim: "**These are not averages. They are the best data point in
  each category, chosen to be as generous as possible to the standard model.**" That is 3.0
  **answering** an averaging objection and replacing the argument with a per-population analysis —
  omission by replacement — not **deploying** the Averaging Problem. Which is what the Ge Statement
  itself says ("renders those complicating elements moot to such an extent that I omitted both").

**Wording narrowed accordingly.** "The Averaging Problem is absent outright (0 hits)" and
"confirmed verbatim and **exhaustively**" overstate what a token search over a two-gloss term can
establish, on the one field this pass moved. The supported statement is: **under gloss (i) the
named argument is absent (`Averaging`, `averaging problem`, `law of large numbers`, `polygenic` all
0); under gloss (ii) the addendum replaces the averaged treatment with a per-population one and
says so.** `internal: holds` is unchanged and is better supported than the token count alone.

**The §1 clause under RH3** (fix pass, critic-side MINOR-2 accepted). The surviving clause is not
purely rhetorical in the RH sense. Verbatim, main:55–56: "**When the Bernoulli Barrier demonstrates
that parallel fixation is probabilistically self-defeating**, the defender invokes neutral drift."
That is an indicative assertion *that the Barrier demonstrates something*, used as a premise in §1's
case that the polythesis is ad hoc, with no support anywhere in the paper (no p^n, no number, no
derivation). `R4-X1-verdict-rule.md` **RH3** has the label: "A node whose only support is rhetoric
is marked '**no dialectical support offered**'. **It is not marked an error.**" So the accurate
record is both halves at once: the argument **is** omitted (Day's statement true, `holds` stands)
**and** its conclusion is asserted once in §1 without dialectical support in 3.0. Recorded in Ge's
R4 paragraph and in `ledgers/slips.md` as RH-33, explicitly not as an error and not as a reason to
disturb `holds`. The opposite reading the brief asked review 3 to test — that naming the Barrier
while omitting its defence is having it both ways — was tested by that reviewer and **fails**: rule
C decides it, and the reviewer said so against its own side.

**Proposal, not applied** (outside the registered bands): Ge `external` `pending` → `contested`,
for the second clause ("both … remain entirely correct"), inheriting G's existing
`external: contested` and G's ledgered label slip. Flagged for the reviewers and the integration
task; I will not move a field my own registration did not license. **Qualification added in the fix
pass (Day-side MINOR-4, accepted):** the proposal's own ground is that it *inherits* G's verdict,
so applying it would record `contested` at both G and Ge for one contested proposition, in counts
(HANDOFF, README, argmap) that do not distinguish inherited from independent verdicts. If
integration applies it, it must carry an explicit `inherited-from: G` note and be excluded from
independent verdict counts; otherwise it should be declined. It must not be applied silently.

Ge's Formal statement already said "contains 'Bernoulli Barrier' only in a rhetorical sentence in
s1" and is confirmed **verbatim**: `Bernoulli` occurs exactly once, main:55, undefined. Band 4b
(zero occurrences, which would have made that line an audit error) did not occur.

## Q5. The three credits to Day — in the body, not a footnote (hard rule 1)

1. **GGR-04** (t=01:06:15), from the panellist who identifies himself as "the math guy in this
   group": "it's just he just did a division and like and I'm like well you you did the division
   correctly". Governing reading under R-4 and rule RD is the **literal concession** — under the
   bathos reading the sentence asserts nothing, so the literal reading is the one under which the
   statement is most defensible. **The credit to Day stands**, with the ironic reading recorded
   beside it. **Stated precisely (fix pass, Day-side MINOR-3):** the panel's mathematician concedes
   that **the division at the core MITTENS step** is done correctly, while flagging a separate 10×
   multiplication slip in the same caption chunk (GGR-01, t=01:06:15, "is off by his multiplication
   of three numbers by a factor of 10"). The earlier wording — "checked Day's arithmetic at this
   step and found it correct" — was broader than the quote and easy to strike; the narrow claim is
   the one that is unassailable, and it is the core F_max step.
2. **GGR-45** (t=01:22:28), from the **same panellist who is harshest on the appendix paper's
   standard** (GGR-38, GGR-39, "nowhere close to the standard that could even cross the editor's
   desk"): "I think it's a fascinating exercise to be honest like like genuinely this was a good
   exercise and the response the review that he got was quite fair I think". Day's own AI-peer-review
   exercise is called good and its review fair, by his sharpest critic on that branch.
3. **GGR-46** (t=01:51:34): "Remember how D was one earlier? This goes back to the whole he's trying
   to give conventional science the bestcase scenario numbers." The panel **grants Day's stated
   intent** — that d = 1 concedes the best case to the other side — while disputing the variable.

**Registered Q5 prediction — hit.** At least one credit bears on a claim file's Responses: GGR-46
bears on **A4** (the d claim) and on the charity question at **A4d**. Recorded in A4d's R4 paragraph.
A4 is **not** a file this task may write, so "add GGR-46 to A4's Responses" is flagged as an
integration item.

A fourth, from Q4 and Q1 rather than from the panel: Day's own blog statement about what he removed
from 3.0 (Ge) is **true**, and **MITTENS 3.0's own generation count is 252,000, used uncut
everywhere including §8.6, with no d multiplying it anywhere in body or addendum**. Both are
accuracy credits to Day established by this pass. *(Wording corrected in the fix pass under lead
ruling R-13 — see the Review resolution. The earlier form, "clean of the d coefficient by
exhaustive token search", claimed more than a token search can establish.)*

**A fifth credit candidate, not harvested, flagged for the harvest** (fix pass, Day-side MINOR-5;
confirmed by the critic-side steelman at its NOTE-5, including its framing condition). At
t=01:39:30 a panellist reads aloud, from the AI peer review that the panel itself calls fair
(GGR-45) and whose five points Dr Hancock endorses at t=01:38:50: "The closest thing to a fair
point is that the adaptive fraction is the legitimate open empirical question and the sweep based
estimates can vary a lot." No GGR id covers t=01:39:00–01:40:00. It bears on branch A/G (what
fraction of the 410 M differences were adaptive), the premise Day's shortfall rests on. **Harvested
whole or not at all:** the same passage says the argument "collapses into a much weaker claim" and
supports "more research, not the conclusion that natural selection is mathematically impossible".
It is a *half* credit, and this pass may not write `quotes-critics.md` beyond the R-10 correction,
so it is Open item 9.

## Scoring table: every registered prediction, hit or miss

| # | Registered | Outcome | |
|---|---|---|---|
| G0 | both pinned hashes match | both match; record unmodified since 2026-10-04 | **hit** |
| Q1 band | **1b** (Bio-Cycle only in the appendix) | **1b′** — no d-term anywhere, Bio-Cycle cited in the **body**, §8.6; 3.0 has no Appendix D. Band table not exhaustive | **miss** |
| Q1 field | A4d `internal` unchanged | unchanged, now verified | **hit** |
| Q1 RD | A4d gains a `reading-dependent:` comment and the separate count | **not applied**; A4d is `SCOPED` (§RD line 198 — its Formal statement fixes the reading), Readings table in the R4 paragraph instead. All three reviews and the lead agree: **the defect was in the registration, not the execution** (R-15), so this is re-booked as a pre-registration defect, not a miss | **registration defect** |
| Q2 band | **2b** | **2b**; `load` 0 occurrences strengthens half (ii) | **hit** |
| Q2 fields | A5h internal and external both unchanged | unchanged | **hit** |
| Q3 band | **3b** (infinitesimal on point, recombination adjacent) | **3b**; refinement carried with its qualifications (R-12). **3d considered (post hoc, fix pass): not reached** — the t=01:55:19 candidate is tagged `rhetoric` (RH-34), not "wrong as stated" | **hit** |
| Q3 fields | nothing moves on branch G | nothing moved; the stated *ground* corrected (critic MAJOR-4) | **hit** |
| Q4 band | **4a** (exactly one, rhetorical, undefined) | **4a**, applied to the **omission clause** (rule S scope); the second clause is an external question, field unchanged. `Averaging` / `law of large numbers` / `polygenic` 0 | **hit** |
| Q4 field | Ge `internal` `pending` → `holds` | applied | **hit** |
| Q5 | ≥1 credit bears on a Responses section | GGR-46 → A4 / A4d | **hit** |

**Revised in the fix pass.** One miss (the non-exhaustive Q1 band table) and **two
pre-registration defects**, all three the audit's own: the band table, the RD instruction the
registration wrote that the rule did not license, and — found by the reviews, not by this pass —
the registration's silence on which gloss of "the Averaging Problem" Q4 tested. The "hit, refined"
label at Q3 is dropped as non-standard (correctness NOTE-5): the band was hit, and the refinement
is prose. Nothing here is a miss by Day or by the critics.

## Who this helps

**For Day**
- **MITTENS 3.0's own generation count is 252,000, uncut, and no d multiplies it anywhere in body
  or addendum** — 0 standalone lowercase `d`, 0 × `0.45`, 0 × `450,000`, 0 × `selective turnover`,
  and §8.6 applies its cited rate to the full 252,000 ("Applied to 252,000 generations provides 8
  achievable fixations", main:653–654), over a hash-verified text. A4d's `holds` survives its first
  real test. *(Narrowed in the fix pass under R-13 from "clean of the d coefficient", which a token
  search cannot establish.)*
- **GGR-14's elaboration is contradicted under both in-scope readings**: `450,000`, `225,000`,
  `202,500` and `0.45` are 0 hits and 252,000 is never cut, so "he multiplies it by the D
  coefficient … and he's still using that number for all his math" is false of 3.0.
- **The panel is internally split about 3.0.** The GGR-11 turn says Day "throws the D coefficient
  off to the side" (t=01:49:52) and GGR-13 is solicited to respond and disagrees. A hostile-source
  corroboration of A4d's central fact (R-10).
- His blog statement that he omitted the Bernoulli Barrier and the Averaging Problem from 3.0 is
  **true as stated** (Ge `internal` → `holds`), and under the second gloss the addendum shows
  omission **by replacement**: "These are not averages. They are the best data point in each
  category, chosen to be as generous as possible to the standard model" (addendum:83–84).
- The A5h modelling objection, **adopted at its strongest, strengthens his stated direction** and
  costs the critics the s = 0.001 escape (0.68 → e^−384 ≈ 1.7e−167, equilibrium regime; relativised
  to wild type, e^−380 = 9.29e−166, so the direction survives relativisation).
- Three statements of credit from the panel itself: the division at the core MITTENS step is
  correct (GGR-04); the AI-peer-review exercise was good and its review fair (GGR-45, from his
  harshest critic on that branch); d = 1 was a concession to the other side (GGR-46).
- On the recombination premise, **R4-G1's tighter maps run his way** (1,000 loci/M → 0.842 ± 0.020;
  10,000 loci/M → 0.652 ± 0.018; clonal → 0), and §2's bullet asserts linkage retention, which is
  not the proposition R4-G1's pairwise ratio tests. 3.0 discusses clonal interference in nine
  places and §9 already states the throughput conclusion. *(With the labels owed: those two rows
  are post hoc, and the pre-registered 1 M row failed.)*
- Three Statement quotes re-verify **verbatim** after the local text was lost: no quote drift
  against him.

**For the critics**
- **GGR-31/GGR-32 reach 3,840 independently** — the audit's exact value — by a six-person panel
  with no reference to this audit. The strongest corroboration A5h's `arithmetic-error` can get.
- **GGR-34 is right in standard theory**: equilibrium load depends on U, not s (Haldane 1937;
  Muller 1950). The s-dependence of "functionally dead" is Day's model's, not biology's.
- **GGR-20 is literally exact**: "mentioned once in that paper and not defined" — one occurrence,
  undefined. GGR-12 is right too. Neither panellist erred; the audit's NOTE-5 did.
- **Reading (c) governs, and GGR-13's core assertion is accurate under it** (R-8, R-9): §8.6's
  single human-derived throughput number is, in Day's own words, computed with "the Bio-Cycle
  correction for overlapping generations" and quoted in "**effective generations**" — the unit the
  audit's own `C2-bio-cycle-d.md` defines as `g_eff = d × g_nominal`. **The d correction is still
  in play in MITTENS 3.0**, by citation, and the paper nowhere reconciles a rate per *effective*
  generation divided into a *nominal* count. `effective generation` occurs exactly once in body and
  addendum, in that sentence. §8.6 answers what the paper itself calls "the most persistent
  objection to MITTENS".
- **Day gives no reason for dropping d**, having built a prior paper (Z18203514) on the claim that
  population genetics cannot handle overlapping generations — and GGR-13's reasoning ("if he's
  retracting the claim about … effective population size, then … there shouldn't be any d
  coefficient at all") is sound, with 3.0's own text meeting the critic's stated expectation.
- **GGR-42's attribution of Day on recombination is accurate**, verified verbatim at §2
  (main:128–131), and the audit's own **pre-registered** free-recombination row backs the substance:
  1.029 ± 0.022 × p², i.e. independence (`R4-G1.md` line 163), on Day's own stipulation of free
  recombination. The **only pre-registered linkage row failed** (predicted 0.5–0.95, got
  1.015 ± 0.022, line 172); the sub-multiplicative 0.84 / 0.65 rows are **post hoc**, and no run
  exists at the human-relevant ~4,500 loci/M (line 174 is an interpolation). And R4-G1 line 173
  stands: "a clonal-derived rate is plausibly a **lower** bound for a recombining population",
  which weakens §8.6's "most generous possible assumption" framing.
- **GGR-43/44 sits at the top of *on point*, not the bottom** (critic MAJOR-4): it names variance
  in fitness — the quantity this write-up itself says Fisher's theorem uses — and the standard
  model of the regime GGR-19 posits. It attacks the CV→variance substitution from a different side
  than G5, not a weaker one.
- The panel's reply to the Bernoulli barrier was real and substantive, and this pass grades it on
  the merits rather than on the harvest's erased sentence.

**Both / the audit's own errors**
- **The Q1 band table was not exhaustive.** Band 1b assumed the Bio-Cycle citation would sit in an
  appendix; it sits in the body, and MITTENS 3.0 has no appendix. A pre-registration defect of this
  pass, found by the very search it registered. Recorded as a miss above.
- **"MITTENS 3.0 is clean of the d coefficient" was a concept claim resting on a token search, and
  it is the third standing audit error against the critics from this source** (fix pass, R-13,
  critic-side MAJOR-3, accepted and stated plainly as it would be for a Day-side error). A token
  search is exhaustive over tokens, not over the concept: §8.6 imports a rate built on the d
  correction and expressed in d-corrected units, by citation to a document outside the fetched
  corpus. It is a headline overstatement rather than a suppressed fact — A4d line 34 and the "For
  the critics" section both carried the underlying fact correctly — but the summary readers and
  counts carry is the thing that was wrong, and it ran against the critics. Corrected at write-up
  the Q1 and Q3 text (line numbers dropped at integration: the fix pass moved them) and at `A4d` line 12 to: **3.0 contains no `d` term and applies no d multiplier
  to its generation count; an overlap correction survives by citation inside the §8.6 rate.**
  **Routed on, not touched here:** `C2-bio-cycle-d.md` line 8 makes the same unqualified assertion
  ("MITTENS 3.0 … drops d, so ROOT survives without it") in the `load_bearing: true` comment of a
  load-bearing node. C2 is outside this task's file list and, being load-bearing, gets its own tier
  rather than a drive-by edit. Open item 8.
- **The t=01:49:52 line was attributed to "the host" and used as corroboration for reading (a)**,
  in the write-up, in `A4d` and in `quotes-critics.md` line 846 (R-10). The audit had itself struck
  that attribution three days earlier (EVO-69 fix pass, MINOR-1: GGR-11 is `panel`, no name spoken
  in the turn), and in context the line is a claim **about 3.0** that GGR-13 was solicited to
  contradict — so presenting it as Day-side corroboration inverted the exchange. All three places
  are corrected; the quote is kept, and what it actually shows — the panel internally split about
  3.0 — is recorded, as a point for Day.
- **The registration, not the execution, was defective on RD.** The brief and the registration
  instructed a `reading-dependent:` comment on A4d; §RD line 198 does not license one, because
  A4d's Formal statement fixes the reading, making it `SCOPED`. The analyst declined and was right;
  all three reviews and the lead agree (R-15). Re-booked here as the audit's second
  pre-registration defect of this pass rather than as a miss charged to the analyst.
- **A third pre-registration defect, found by the reviews:** the Q4 registration did not say which
  gloss of "the Averaging Problem" the token search tested, and the audit's files carry two. Both
  are tested in the fix pass and both give the same answer, so the verdict is unaffected — but
  "absent outright" and "exhaustively" claimed more than the registered search design supported.
- **A4d's Weaknesses line** calls it "the later 'Appendix D' human-derived rate", which reads as
  though 3.0 contains an Appendix D. It does not; §8.6 cites *Day and Athos 2025*, Appendix D.
  Corrected in this pass.
- **The combined review's NOTE-5 invented a panel inconsistency** between GGR-12 and GGR-20. There
  is none; both are right. An audit error against the critics, the second of its kind from this
  source after MAJOR-1.
- **The registered Q2 criterion is stricter than the audit's own operative use of `contested`**
  (MA-08), and the write-up originally asserted the reverse — that the narrow reading "is the one
  the vocabulary supports". Withdrawn. `pending` stands because the criterion was pre-registered;
  the inconsistency is in the vocabulary and is routed to the batch-15 criticality pass (R-14,
  Open item 11). Applying the strict form to the one objection sourced from the critics is an
  asymmetry the audit names here rather than asserts away.
- **The "load occurs 0 times" rebuttal was given first place at Q2** and is a word count offered
  against a conceptual attribution — the overreach `RH5` charges to any side, including the audit.
  Demoted below the cost that bites. Both steelmen reached this independently, from opposite sides.
- **Band 3d was never checked** although the registration carried it. Checked **post hoc** in the
  fix pass (t=01:55:19): not reached, tagged `rhetoric` (RH-34). Found by the critic-side steelman
  against its own side.
- **The stated ground for the Q3 no-move was wrong** ("strictly weaker than G5"): G5 and GGR-43/44
  are about different quantities. The conclusion was right for an independent reason. Corrected.
- **A4d's `holds` had been resting on a search of a file the audit no longer had** since
  `sources/raw/` was cleared. It was right, but it was unverifiable for the interval. The
  general lesson is a provenance one and belongs to the bookkeeping task, not to either side.
- R-2's half (ii) ("the word 'load' does not occur in it") was asserted from an excerpt in the fix
  pass; it is only now verified over the whole text. It held.

## Open

**Rebalanced in the fix pass (Day-side MAJOR-3, accepted under R-15).** All three original "Open"
proposals ran against a Day node, while this pass had found Day-side material of the same kind and
left it unrecorded. Hard rule 1 is the reason the Day-side findings were applied, and it is the
same reason items 8–9 and the two Responses corrections below go in. None of them moves a verdict
field, so none needs a band that was not registered.

1. **Ge `external` `pending` → `contested`** — proposed, not applied (outside the registered
   bands), and **only with an explicit `inherited-from: G` note and exclusion from independent
   verdict counts**, or else declined (Day-side MINOR-4). Not to be applied silently.
2. **A new critic-side node** for the infinitesimal-model answer (GGR-43/GGR-44), child of G,
   `internal: pending` — proposed; this task may not create claim files. Judged on its own content
   as an independent fitness-variance angle, not as a weaker G5.
3. **A defeater pair** on §2's "No recombination overhead" bullet, citing GGR-42 and R4-G1's
   **free row (1.029 ± 0.022, line 163)** — proposed for `defeaters.yaml` at integration, with the
   post hoc labels and the failed pre-registered 1 M row attached (R-12).
4. **GGR-46 into A4's Responses** — A4 is outside this task's file list.
5. **Balance-ledger row for branch G** from this pass (best for Day: BB is absent from 3.0 so the
   branch is no longer load-bearing for the headline argument; best for critics: recombination
   against §2, with R4-G1 behind it) — for the integration task.
6. **The lost `sources/raw/day/zenodo-23003785.txt`.** This pass re-fetched into its own new
   directory and did not restore the old path. Whether the audit re-establishes a canonical local
   copy is a bookkeeping decision, not mine.
7. **GGR-19's Reddit original is still unlocated.** The audit scores a relay (rule U). Locating it
   would let branch G be scored against a primary statement.
8. **`C2-bio-cycle-d.md` line 8** repeats the corrected overstatement ("MITTENS 3.0 … **drops d**,
   so ROOT survives without it") inside the `load_bearing: true` comment of a load-bearing node.
   It should read "drops d from the generation count; §8.6 still imports a Bio-Cycle-corrected rate
   by citation". **Outside this task's file list, and load-bearing**, so it gets its own tier at
   integration, not a drive-by edit (R-13).
9. **Harvest t=01:39:30** as a Day-side half credit, with its limiting frame intact: "The closest thing to a fair point is that the adaptive fraction is the legitimate open
   empirical question and the sweep based estimates can vary a lot" — harvested whole or not at
   all. `quotes-critics.md` is outside this pass beyond the R-10 correction.
10. **A Day-side defeater** matching the critic-side pair at item 3, which this pass establishes:
    Q4 shows the Bernoulli Barrier is absent from MITTENS 3.0, so GGR-41..GGR-44 — and branch G's
    attacks generally — do not reach the headline argument of the current paper (Day-side MAJOR-3).
11. **MA-08 referral to the batch-15 criticality pass** (R-14): the Q2 criterion registered here is
    stricter than the audit's operative use of `external: contested`. A vocabulary inconsistency,
    not a defect in this check; any change takes the freeze procedure in `DECISIONS.md`. Q2 is
    **not** rescored.
12. **Two Responses corrections** owed for symmetry (Day-side MAJOR-3), applied in this fix pass,
    listed here so integration can see them: A5h's "In support: none located" now qualified, and
    the GGR-11 turn entered in A4d's Responses as hostile-source corroboration of A4d's fact.
13. **`yt-dlp` is unpinned** in the harvest toolchain (correctness NOTE-6) — bookkeeping, for
    integration.

## Things that looked wrong (for the reviews to rule on)

- **The RD departure at Q1** is the single most reviewable judgement in this pass. A reviewer who
  thinks A4d's field *is* reading-dependent should say so; I have made the change cheap to apply.
- **Is band 3b's "on point / adjacent" criterion too strict?** It was fixed before the evidence was
  read, and I applied it as written, but a steelman-critic reviewer should test whether "meets"
  was set at a height no non-technical panel reply could clear — and if so, whether that height is
  the right one for a *video roundtable* as opposed to a paper.
- **Ge `internal` → `holds` turns on reading "omitted" charitably** against one surviving rhetorical
  clause at §1. A steelman-critic reviewer should test the opposite reading: that invoking the
  Barrier by name in the paper's framing paragraph, while omitting its defence, is having it both
  ways. My view is that rule C decides it, but it is a live question.
- **Q2's criterion** ("external moves only if the objection weakens the direction") may be too
  demanding: one could argue `contested` should record *any* substantive located objection. I chose
  the narrower reading because it is the one the vocabulary supports, and I registered it before
  looking. A reviewer may disagree.
- The MINOR-1 **extension** flagged in the brief (GGR-11, GGR-27..GGR-29 re-attributed to `panel`
  without independent review) bears on Q3: GGR-27..GGR-29 are the second point of the
  infinitesimal-model answer. My Q3 scoring does **not** depend on who spoke them — it turns on
  their content — but the correctness reviewer should still check the attribution against the
  transcript turns, as the brief directs.

**How the reviews answered this section** (added in the fix pass; the bullets above are left as
written before the reviews, as the record of what the pass put up for challenge):
the RD departure was upheld by all three and the defect re-booked to the registration (R-15);
band 3b's height was tested by the critic-side steelman **against its own side** and found **not**
too high — the registered criterion reads "with or without numbers" and one spoken sentence clears
it (critic MINOR-4); the opposite reading of Ge was tested by the same reviewer and **fails**, rule
C decides it, with the §1 clause instead booked under RH3; and Q2's criterion was found **stricter
than the audit's own operative usage**, the opposite of what the fourth bullet claims — the claim
is withdrawn above, the field still does not move, and the inconsistency is routed to the
criticality layer (R-14).

---

# Review resolution (fix pass, 2026-10-13)

Three reviews landed: correctness `385c443` (0 BLOCKER / 4 MAJOR / 5 MINOR / 7 NOTE), steelman-day
`a22bd78` (0/4/5/6), steelman-critic `98b820a` (0/5/5/6). **13 MAJOR and 15 MINOR are answered
below by id.** Lead rulings R-8..R-15 (`research/checks/briefs/VID-01-score-reviews-reviewer.md`,
commit `9699aa9`) bind this pass and are not reopened; two findings are ruled **not applied** and
are answered with their reason (correctness MINOR-5 under R-11; critic MAJOR-5 under R-14).

**No verdict field moves in this pass.** A4d `internal: holds`, A5h `internal: arithmetic-error` /
`external: pending` and Ge `internal: holds` survive all three reviews, and the Ge `internal` move
already applied at `31d7f0d` stands. What changed is wording, the Readings table, attributions, and
the balance of what is recorded. The registered Predictions section (above the "Results (post hoc)"
line) is left **byte-identical**; where a registered sentence carries a corrected claim — the
Day-side Q1 prediction at line 71, which calls the t=01:49:52 line "the host's own narration" — the
correction is made in the Results section and here, not by editing the registration (hard rule 5).
One new computation was run for this pass and is labelled **post hoc**: the band 3d check at
t=01:55:19 (Q3), committed separately.

## Correctness review (`385c443`)

| Id | Disposition | What changed |
|---|---|---|
| **MAJOR-1** | **Accepted** (R-10) | "The host's own narration" is withdrawn in all three places it stood: the write-up's Q1 Readings paragraph, `A4d`'s R4 paragraph, and — not named by the reviews but carrying the same error — **`quotes-critics.md` line 846**. The line is inside the **GGR-11** turn (t=01:47:28–01:51:34, unbroken, no name spoken), re-attributed to `panel` by the EVO-69 fix pass under its own MINOR-1 rule. The write-up had asserted an attribution the audit struck three days earlier. |
| **MAJOR-2** | **Accepted in part** (R-10) | The claim that the narration corroborates reading (a) is **struck**: the panellist is speaking *about 3.0* and GGR-13 is the solicited reply disagreeing with him, so it cannot be Day-side corroboration of (a). The quote is **not deleted** (Day-side NOTE-2 is right): it is a real panel turn and it corroborates **A4d's fact** from a hostile source, so it is entered in A4d's Responses. `quotes-critics.md` line 846's "evidence for (a)/(b) over (c)" is not restored either — the lead's ruling replaces it with what the turn actually shows: **the panel is internally split about 3.0**, a point for Day. |
| **MAJOR-3** | **Accepted** (R-9) | Reading (a) is **struck as governing** under §RD line 202 (extended readings — a different object — report their own verdicts but cannot set the verdict field or the headline tag). It stays in the Readings table with its `accurate` verdict and its TW-01 cross-reference. **(c) governs among in-scope readings.** The headline in the write-up and in `A4d` is changed to match. All three reviewers reached this independently. Because this moves a governing reading, the lifecycle sends it to a **fresh reviewer before integration**. |
| **MAJOR-4** | **Accepted** | Q4 now **names the gloss tested** and tests both: under gloss (i) (`G2g` line 29, a named argument) the decisive negative is **`polygenic` 0** (post hoc term) beside `Averaging` / `averaging problem` / `law of large numbers` 0; under gloss (ii) (Day's ¶22) the addendum is quoted at **83–84** ("These are not averages. They are the best data point in each category…") and the one-sentence reason is given: *answering* an averaging objection is not *retaining* the Averaging Problem. "Absent outright" and "exhaustively" are narrowed. `internal: holds` kept, and better supported than before. |
| **MINOR-1** | **Accepted** | The `d =` row now states the case convention: **0 lowercase `d` tokens case-sensitively**; case-insensitively **3 in `main.txt`** — `Appendix D)` (653), `Appendix D.` (724), `Yoo D, et al.` (738) — two citations and an author initial, none a coefficient. `A4d`'s verdict comment carried the same wording and is corrected too. |
| **MINOR-2** | **Accepted** | Q2 now says the objection was added **under Against**, where only RE-02 / A2h stood, and that "In support: none located" is a separate entry about support for **Day's** claim and is untouched by it. (Separately, under Day-side MAJOR-3, that line is now **qualified** for a different reason — see below.) |
| **MINOR-3** | **Accepted** | A third row grades **GGR-27..GGR-29** (the registered second point of answer (ii), confirmed by the reviewer to be one unbroken turn with GGR-43/44) as **adjacent**, with the overall grade of answer (ii) unchanged at *on point*, set by its stronger half. |
| **MINOR-4** | **Accepted** | The scoring table's Q4 row now reads "**4a**, applied to the **omission clause** (rule S scope); the second clause is an external question, field unchanged." |
| **MINOR-5** | **NOT APPLIED** (R-11) | The proposed substitution of 1.015 ± 0.022 for 1.03 ± 0.02 is declined. `R4-G1.md` line 163 is the **free** row with pair ratio **1.029 ± 0.022**; line 164 is **linked 1 M** at 1.015 ± 0.022. Writing 1.015 into a sentence about free recombination would substitute a linked result for a free one. Both steelmen reached this independently (Day MAJOR-4, critic NOTE-1) and the lead checked the source table itself; a correctness finding is not privileged over two concurring steelmen plus the source. **Recorded here rather than silently dropped**, per R-11. The reviewer's suggested *tightening* is adopted: the citation is now explicit — "`R4-G1.md` line 163, free row, 1.029 ± 0.022; the 1.03 ± 0.02 form is R4-G1's own Ga summary row, line 318". |
| NOTE-1..7 | Applied where they asked for prose | NOTE-1 (`SCOPED` named by its clause, defect re-booked to the registration), NOTE-3 (no change), NOTE-5 ("hit, refined" dropped as non-standard), NOTE-6 (`yt-dlp` unpinned → Open 13) are in. NOTE-2 confirms the attribution extension with no finding. NOTE-4 and NOTE-7 are locator/housekeeping notes for integration. |

## Steelman, Day's side (`a22bd78`)

| Id | Disposition | What changed |
|---|---|---|
| **MAJOR-1** | **Accepted in part** (R-8) | The **regrade of reading (c) to "contradicted" is declined** — see critic MAJOR-1 — but **the evidence is adopted**, against the critic review's dismissal of it. The Readings table now scores **GGR-13 and GGR-14 as separate propositions**: GGR-13's core assertion is `accurate` under (c), GGR-14's elaboration is `contradicted` under (b) *and* (c). The four-row proposition table is adopted for GGR-14, including §8.6's own "Applied to **252,000** generations provides 8 achievable fixations" (main:653–654). The headline grade stays **`partial`**, which is exactly what accurate-core / inaccurate-elaboration names. **The costs to Day in the same finding are recorded, not deleted** (R-8, and the reviewer asked for this): `effective generation` occurs exactly once in body and addendum, in that sentence; a rate per *effective* generation divided into a *nominal* count is a unit mismatch 3.0 nowhere reconciles; and Day gives no reason for dropping d after building Z18203514 on overlapping generations, so GGR-13's reasoning is sound. |
| **MAJOR-2** | **Accepted in part** (R-12) | The Q3 refinement is **weakened, not deleted**, and now carries **every qualification from both steelmen**, because each is factually right and `R4-G1.md` supports both: free recombination is Day's own stipulation (s7.10) and gives independence at **1.029 ± 0.022** (line 163); the **only pre-registered linkage row failed** (predicted 0.5–0.95, got 1.015 ± 0.022, line 172); the tighter maps giving **0.842 / 0.652** are labelled **post hoc** (lines 165–166), as hard rule 5 owes; **~4,500 loci/M is an interpolation, not a run** (line 173–174), so neither side may claim the human density; §2's bullet asserts linkage retention, which is not what the pairwise ratio tests; and 3.0 discusses clonal interference in nine places with §9 stating the throughput conclusion. The sentence "Day's own stated direction holds only in the linked and clonal cases" is **withdrawn**. The reviewer's own "cost to Day" (R4-G1 line 173, clonal rate as a **lower** bound) stays, as it asked. Neither steelman carries more weight than its row. |
| **MAJOR-3** | **Accepted** (R-15) | All three original "Open" proposals ran against a Day node. The two symmetric items the reviewer names are added — **A5h's "In support: none located" is now qualified** (this pass located external material bearing on the conclusion's direction; the field still does not move, and the asymmetry of recording a failing critic objection but not failing supporting material is named), and **the GGR-11 turn is entered in A4d's Responses** as hostile-source corroboration of A4d's fact — plus a **Day-side defeater proposal** (Open 10): the Barrier is absent from 3.0, so branch G's attacks do not reach the current paper's headline argument. Hard rule 1 is the reason, the same reason the Day-side findings were applied. |
| **MAJOR-4** | **Accepted** (R-11) | Correct. Correctness MINOR-5 is not applied; see above. The free row is 1.029 ± 0.022 and the write-up's "1.03 ± 0.02" was right as cited. |
| **MINOR-1** | **Accepted** | The "load occurs 0 times" rebuttal is **demoted below** the cost that bites. The verified fact is kept and restated as what it establishes — "*the* genetic load calculation" is not what §6.4 calls itself — not as an answer to a conceptual attribution. `RH5`'s symmetry is cited. The critic-side steelman reached the same place from the other side (its MINOR-3); both are applied as one change. |
| **MINOR-2** | **Accepted** (and subsumed by R-13) | "Clean of the d coefficient" is replaced everywhere by the narrow, fully supported claim. The reviewer's own qualifier is carried: the §8.6 rate is expressed in Bio-Cycle "effective generations" and *Day and Athos 2025*, Appendix D is **outside the fetched corpus**, so the search could not reach it. |
| **MINOR-3** | **Accepted** | Q5 credit 1 now reads "the division **at the core MITTENS step**", with GGR-01's separate 10× multiplication slip (same caption chunk) named beside it. The broader "checked Day's arithmetic" wording is withdrawn. |
| **MINOR-4** | **Accepted** | The Ge `external` → `contested` proposal now carries the double-count warning: apply only with an explicit `inherited-from: G` note and exclusion from independent verdict counts, or decline. Not to be applied silently at integration. |
| **MINOR-5** | **Accepted as a referral** | t=01:39:30 is flagged for the harvest as a **half** credit with its limiting frame intact (Open 9). `quotes-critics.md` is outside this pass beyond the R-10 line-846 correction, so no quote is added. The critic-side steelman independently agreed, including the "harvested whole or not at all" condition (its NOTE-5). |
| NOTE-1..6 | Applied where they asked for prose | NOTE-1's add:83–84 citation is in Q4 and in Ge; NOTE-2's "re-label, do not delete" is the shape of the R-10 fix; NOTE-3 is answered by R-9 (Day does not need (a), and the lead did not read him as needing it); NOTE-4's regime naming is in Q2 and A5h; NOTE-5 and NOTE-6 report no finding. |

## Steelman, critics' side (`98b820a`)

| Id | Disposition | What changed |
|---|---|---|
| **MAJOR-1** | **Accepted** (R-8) | Reading (c) **keeps `partial`** and the Day-side regrade is declined. The Readings table now carries the reviewer's evidence so the grade is self-evidencing: the `C2-bio-cycle-d.md` identity `g_eff = d × g_nominal`, the §8.6 sentence verbatim, and the "effective generations" locator (main:653, the only occurrence). **(c) governs among in-scope readings** under §RD line 202, with (a) recorded beside it. GGR-13's core assertion is scored `accurate` as to the §8.6 step — a token search establishes the absence of the symbol `d`, not the absence of the correction. |
| **MAJOR-2** | **Accepted in part** (R-8) | The regrade of (c) is declined, as the reviewer asks, and the "inconsistent with **any** application of d" sentence does **not** enter the write-up or any claim file. But the reviewer's "discriminates nothing" is **overstated** and the lead ruled so: 252,000/27,600 = **9.13** against a printed 8 is a **12% gap `A5e` line 26 already records as unreconciled**, whereas 113,400/27,600 = **4.11** is off by a factor of two — the printed 8 is consistent with the **uncut** count and not with a d-cut one. Both halves are now in the write-up, with the figure's unreconciled status stated as A5e states it. |
| **MAJOR-3** | **Accepted** (R-13) | "MITTENS 3.0 is clean of the d coefficient" is replaced at write-up the Q1 and Q3 text (line numbers dropped at integration: the fix pass moved them) and at `A4d` line 12 with the defensible form: **3.0 contains no `d` term and applies no d multiplier to its generation count; an overlap correction survives by citation inside the §8.6 rate.** And the write-up now says plainly, as it would for a Day-side error, that this is **the third standing audit error against the critics from this source** — not softened, and recorded in "Both / the audit's own errors" rather than netted against anyone. **`C2-bio-cycle-d.md` line 8 is not touched here**: it is outside this task's file list and `load_bearing: true`, so it is routed to integration for its own tier (Open 8). |
| **MAJOR-4** | **Accepted** | The stated ground for the Q3 no-move is replaced. G5 attacks the CV→variance substitution from the **allele-count** side (Var(K) = n/4); GGR-43 attacks it from the **fitness-variance** side, naming the quantity this write-up itself says Fisher's theorem uses, and the standard model of the regime. "Strictly weaker" and "name a model without it" are withdrawn; GGR-43/44 is placed at the **top** of *on point* (critic MINOR-4 (ii)). The no-move now rests on its correct ground — G `external` is already `contested` and the answer adds no derivation — and the Open-2 node proposal stands on its own content. |
| **MAJOR-5** | **Recorded, NOT acted on** (R-14) | A5h `external` stays **`pending`** and **Q2 is not rescored**: all three reviews agree the field does not move, and the criterion was fixed before looking (`e857d1f`, byte-identical per the correctness diff check); widening it now would be the post hoc widening hard rule 5 exists to prevent. What **is** applied is the reviewer's central point: the claim that the narrow reading "is the one the vocabulary supports" is **struck**, and the write-up now records that the registered criterion is **stricter than the audit's operative usage** (MA-08, `METHODS-AND-LIMITATIONS.md` line 45, quoted), and that applying the strict form to the one objection sourced from the critics is an asymmetry the audit names rather than asserts away. The inconsistency is in the **vocabulary**, not in this check; changing it is a rule change under the `DECISIONS.md` freeze procedure, so it is **routed to the batch-15 criticality pass** (Open 11). |
| **MINOR-1** | **Accepted** (R-12) | The post hoc labels are supplied, the failed pre-registered 1 M row is quoted, and the absence of any run at ~4,500 loci/M is stated — in the write-up **and** against the Day-side steelman's MAJOR-2 point 1, which the same qualification limits. The sentence cuts for the critics here and the label is owed either way. |
| **MINOR-2** | **Accepted** (R-15) | Ge's §1 clause is booked under **RH3** as "**no dialectical support offered**" — explicitly **not** an error and **not** a reason to disturb `holds` — in the write-up's Q4, in Ge's R4 paragraph, and as **RH-33** in `ledgers/slips.md` with a counter. The record is now both halves: the argument is omitted (Day's statement true) **and** its conclusion is asserted once in §1 without support in the paper. |
| **MINOR-3** | **Accepted** | Same change as Day-side MINOR-1 (the word count demoted and restated). Two reviewers reaching the same finding from opposite sides is why it is applied without qualification. |
| **MINOR-4** | **No change needed; recorded** (R-15) | A finding **against the reviewer's own side**, and it closes the question the brief asked: band 3b's "meets" is **not** pitched too high — the registered criterion reads "with or without numbers" and is clearable in one spoken sentence. It was applied as written and changing it now would be post hoc. The two tightenings it asks for **in the critics' favour** are applied: GGR-43/44 is placed at the top of *on point*, and the "weaker, model-naming restatement" prose is withdrawn (see MAJOR-4). |
| **MINOR-5** | **Accepted** (R-15) | **Band 3d was checked** against the named candidate, **post hoc**, and the result is recorded in Q3: at t=01:55:19 the transcript reads "I'm going to say that sounds like vaguely related to **Hallane's** dilemma," continuing at t=01:55:39 "but that's not a thing anymore. That's not like actually an issue." *(The review's own rendering reads "Haldane's"; the ASR captions read "Hallane's", and hard rule 2 takes the captions.)* **3d is not reached**: under RH1 the line is tagged `rhetoric` — a dismissal with no argument attached — and its literal content is unsupported rather than false, since the audit's own `H-haldane-limit` carries `external: contested` and the same panel states the standard view at GGR-08. So no critic-side ledger row under 3d, and one rhetoric row, **RH-34**, under RH1/RH5 — the same treatment Day's comparable lines get. |
| NOTE-1..6 | Applied or recorded | NOTE-1 is R-11 (correctness MINOR-5 declined); NOTE-2 is the shape of the R-10 fix and is applied; NOTE-3 (SCOPED and the extended-reading bullet are compatible, one about A4d's own field and one about whose quote may set a headline) is adopted and is why both NOTE-1-correctness and MAJOR-3-correctness are applied together; NOTE-4 confirms four credits to the critics; NOTE-5 is Open 9; NOTE-6 reports no finding. |

## What a fresh reviewer should check before integration

The lead ordered one narrow re-review because **R-9 moves the governing reading**: the Readings
table and the headline only — that (c) governs among in-scope readings, that (a) is recorded but
struck as governing under §RD line 202, that GGR-13 and GGR-14 are correctly scored as separate
propositions, and that the headline in the write-up and in `A4d` matches. Nothing else in this fix
pass is in that scope.

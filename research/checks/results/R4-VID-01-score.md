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
| `d =` | 0 real | main 0; addendum 2 are case-insensitive substring artefacts of "**SD = ** 28.5", "**SD = ** 720.0". Case-sensitive `d =`: **0** in both files. A post hoc regex for a standalone `d` token, `(^\|[^A-Za-z])d([^A-Za-z]\|$)`, returns **0 in both files** |
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

| Reading | What "mittens" denotes | Scored against the hash-verified 3.0 text | Verdict of the quoted statement |
|---|---|---|---|
| **(a)** | the pre-3.0 / *Probability Zero* line of argument | 450,000 × 0.45 = 202,500, "like 225,000 generations or whatever"; this is the audit's **own** TW-01 figure (`A-mittens-formula.md` line 39; A4 `derived:`) | **accurate** |
| **(b)** | the MITTENS 3.0 body | 0 standalone `d`, 0 × `0.45`, 0 × `450,000`; 252,000 appears 10 times and is never cut. "he's still using that number for all his math" is false of 3.0 | **contradicted** |
| **(c)** | 3.0 "including Appendix D" | 3.0 has no Appendix D; §8.6 of the **body** cites *Day and Athos 2025*, Appendix D, for a rate computed with "the Bio-Cycle correction for overlapping generations". So an overlapping-generations correction **is** still in play in 3.0 — inside the 27,600 rate, not as a multiplier on generations | **partly accurate**: the overlap correction survives; "still using the d coefficient … for all his math" does not |

Most defensible reading of the quoted statement (rule RD — **not** the reading best for either
side): **(a)**. Under (a) the statement is true and matches the audit's own record; under (b) it is
false; under (c) half of it is false. The host's own narration in the same segment agrees with (a):
"He kind of throws the D coefficient off to the side. It no longer seems nearly as important as it
was in probability zero" (t=01:49:52).

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

### Who this helps, at Q1

- **Day:** on the governing reading the "still using d" charge is not about MITTENS 3.0 at all, and
  3.0 is clean of d by an exhaustive token search. A4d's `holds` survives its first real test.
- **Critics:** reading (c) is **partly right and the audit had already said so**. The panel found a
  real tension that Day nowhere explains — he drops d from the generation count while the rate he
  cites at §8.6 is still built on a "Bio-Cycle correction for overlapping generations". The host's
  01:49:52 narration is exactly right. GGR-14's arithmetic (450,000 × 0.45) is exactly the audit's
  TW-01. None of this is a critic-side error.
- **Audit:** the band table (above); and A4d's Weaknesses line calls it "the later 'Appendix D'
  human-derived rate", which reads as though 3.0 has an Appendix D. It does not. Corrected.

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
| **Its cost to the critics** | GGR-33's premise — "This is supposed to be a genetic load that he's calculating" — is an attribution the text does not carry (0 occurrences of "load"). And on the panel's **own** e^−U, at A5h's corrected U = 384, carrier fitness is e^−384 ≈ 1.7e−167 (384·log₁₀e = 166.8), independent of s. Adopting the objection therefore **strengthens** Day's stated direction and **removes the s = 0.001 escape** (0.999^384 = 0.68) that A5h records as the one surviving counterexample to "functionally dead". |

**Registered criterion applied:** `external` moves `pending` → `contested` only if a located
objection weakens the conclusion's direction. This one leaves it strengthened. **Band 2b.**

- **A5h `internal`: `arithmetic-error` — unchanged.** The 10× slip (3.2e9 × 1.2e-8 × 100 = 3,840,
  printed 38,400) is Day's own arithmetic on his own printed inputs and is untouched by any
  modelling objection. Re-verified verbatim against the re-fetched text.
- **A5h `external`: `pending` — unchanged, and this is the result**, not a failure to decide. The
  objection is added to A5h's Responses, which until now said "In support: none located"; it is
  now an objection on the record that does not move the field, with the reason stated.
- **Independent credit to the critics:** GGR-31/GGR-32 reach 3,840 — the audit's exact value — by a
  six-person panel working without reference to this audit. That is the strongest kind of
  corroboration A5h's `arithmetic-error` can get.

## Q3. Branch G: GGR-41..GGR-44 against GGR-19 — band 3b, as registered, with one refinement

Criterion registered in advance: an answer **meets** GGR-19 iff it engages the inference
CV(K) → 0 ⟹ (Fisher) d(mean fitness)/dt → 0.

| Answer | Grading | Why |
|---|---|---|
| **Infinitesimal model**, GGR-43/GGR-44 (t=02:13:47, 02:14:07) | **on point** | It is the standard model of exactly the regime GGR-19 posits (many loci, small effects), it is introduced explicitly as "the pop gen answer to go back to Bernoli's law", and it speaks to GGR-19's premise about variance in fitness. But it gives **no derivation** and never touches the CV→variance substitution, which is where the inference actually fails. |
| **Recombination**, GGR-41/GGR-42 (t=01:57:03, 01:57:44) | **adjacent** to GGR-19 — but **on point against a live premise of MITTENS 3.0** | It answers linkage and the waiting-time framing, not the CV step. See the refinement below. |

**Nothing moves on branch G, and the reason is that the panel's better answer is a weaker form of a
point the audit already scores.** The CV→variance substitution is the audit's node **G5** (Matev,
`internal: holds`: "While this coefficient of variation does go to zero as n increases, the variance
of the beneficial allele count of an individual just increases as n increases") and G's own
`derived:` line (at n = 157,000: Var = n/4 = 39,250 rises, only CV = 0.252% falls, as 1/√n; Fisher's
theorem relates the response to additive genetic **variance** in log fitness, not to the CV of a
count). G5 states the defect with the algebra; GGR-43/44 name a model without it. A critic-side node
whose content is strictly weaker than an existing critic-side node moves no verdict.

**Refinement not anticipated in the registration.** GGR-42's speaker attributes to Day the position
that recombination makes fixation *slower* ("but there's recombination and therefore that breaks up
things and it makes it slower"). That attribution is **accurate**, verified verbatim in the
re-fetched §2 (main:128–131): "**No recombination overhead.** In clonal populations, a beneficial
mutation that arises in one individual stays linked to that individual's entire genome. In sexual
populations, recombination breaks linkage, **separating beneficial mutations from one another** and
from the genetic backgrounds on which they arose." So the panel's recombination answer, while
*adjacent* to GGR-19, is **directly on point against a premise MITTENS 3.0 actually uses** — and
`R4-G1.md` is on their side of it: under **free recombination joint fixation is 1.03 ± 0.02 × p²**
(independence), whereas joint < product when **linked** (0.84 / 0.65) or **clonal** (0). Recombination
removes the sub-multiplicative penalty that §2 lists as a sexual-organism "overhead"; Day's own
stated direction holds only in the linked and clonal cases. That is a real critic-side point with
the audit's own run behind it, and it is recorded here as prominently as the grading above.

**Note on the target.** Q4 establishes that the Bernoulli Barrier appears in MITTENS 3.0 only as one
rhetorical clause, undefined. So the barrier the panel is answering is the January 2026 Zenodo
paper's (Z18167588, claim G), not 3.0's. Neither side is at fault for that; it is worth stating
because it bounds what the exchange can settle.

**Verdict fields, branch G — all unchanged:**

| Node | Field | Before | After | Why |
|---|---|---|---|---|
| G | external | `contested` | `contested` | R4 F2 and R4 G1 already give the contest its content; the panel adds no numbers |
| G1 | internal / external | `holds` / `contested` | unchanged | §8.1 re-verifies verbatim |
| G5 | internal | `holds` | unchanged | the panel restates it more weakly |
| Ge | internal | `pending` | **`holds`** | Q4 |

**Proposal, not applied** (the brief forbids new claim files): a critic-side node for the panel's
infinitesimal-model answer, child of G, `attacks` G, `internal: pending` (no derivation given),
quotes GGR-43/GGR-44; and a defeater pair for the §2 recombination-overhead bullet citing GGR-42
and R4-G1's 1.03 ± 0.02. For the integration or a later design task.

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
precision**, and **both are exactly right**: the Averaging Problem is absent outright (0 hits) and
the Bernoulli Barrier appears once, undefined. The combined review's NOTE-5 called this a "panel
inconsistency". It is not one. **That is the audit's own error**, recorded in "Both" below.

### Verdict: Ge `internal`: `pending` → **`holds`** (registered band 4a — applied)

Day's statement (Ge): "the MITTENS 3.0 paper … renders those complicating elements moot to such an
extent that I omitted both the Bernoulli Barrier and the Averaging Problem, even though both of
them remain entirely correct." The **omission half is true as stated**, now verified against a
hash-matched text rather than against a file the audit no longer had. One undefined rhetorical
clause is not a retention of the argument; under rule C this is "omitted". **This is a credit to
Day on an accuracy question about his own work** and it is why Ge's internal field moves.

**Proposal, not applied** (outside the registered bands): Ge `external` `pending` → `contested`,
for the second clause ("both … remain entirely correct"), inheriting G's existing
`external: contested` and G's ledgered label slip. Flagged for the reviewers and the integration
task; I will not move a field my own registration did not license.

Ge's Formal statement already said "contains 'Bernoulli Barrier' only in a rhetorical sentence in
s1" and is confirmed **verbatim and exhaustively**. Band 4b (zero occurrences, which would have made
that line an audit error) did not occur.

## Q5. The three credits to Day — in the body, not a footnote (hard rule 1)

1. **GGR-04** (t=01:06:15), from the panellist who identifies himself as "the math guy in this
   group": "it's just he just did a division and like and I'm like well you you did the division
   correctly". Governing reading under R-4 and rule RD is the **literal concession** — under the
   bathos reading the sentence asserts nothing, so the literal reading is the one under which the
   statement is most defensible. **The credit to Day stands**, with the ironic reading recorded
   beside it. The panel's mathematician checked Day's arithmetic at this step and found it correct.
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
from 3.0 (Ge) is **true**, and his 3.0 text is **clean of the d coefficient** by exhaustive token
search. Both are accuracy credits to Day established by this pass.

## Scoring table: every registered prediction, hit or miss

| # | Registered | Outcome | |
|---|---|---|---|
| G0 | both pinned hashes match | both match; record unmodified since 2026-10-04 | **hit** |
| Q1 band | **1b** (Bio-Cycle only in the appendix) | **1b′** — no d-term anywhere, Bio-Cycle cited in the **body**, §8.6; 3.0 has no Appendix D. Band table not exhaustive | **miss** |
| Q1 field | A4d `internal` unchanged | unchanged, now verified | **hit** |
| Q1 RD | A4d gains a `reading-dependent:` comment and the separate count | **not applied**, with reason; Readings table in the R4 paragraph instead. Deliberate departure, flagged for the reviewers | **miss** |
| Q2 band | **2b** | **2b**; `load` 0 occurrences strengthens half (ii) | **hit** |
| Q2 fields | A5h internal and external both unchanged | unchanged | **hit** |
| Q3 band | **3b** (infinitesimal on point, recombination adjacent) | **3b**, plus the unanticipated §2 recombination-overhead refinement | **hit, refined** |
| Q3 fields | nothing moves on branch G | nothing moved | **hit** |
| Q4 band | **4a** (exactly one, rhetorical, undefined) | **4a** exactly; `Averaging` 0 | **hit** |
| Q4 field | Ge `internal` `pending` → `holds` | applied | **hit** |
| Q5 | ≥1 credit bears on a Responses section | GGR-46 → A4 / A4d | **hit** |

Two misses, both the audit's own: a non-exhaustive band table and an RD instruction I declined to
apply. Neither is a miss by Day or by the critics.

## Who this helps

**For Day**
- MITTENS 3.0 is **clean of the d coefficient** by an exhaustive token search over a hash-verified
  text (0 standalone `d`, 0 × `0.45`, 0 × `450,000`). A4d's `holds` survives its first real test.
- On the governing RD reading, GGR-13/GGR-14's "still using the d coefficient" is **not about 3.0**.
- His blog statement that he omitted the Bernoulli Barrier and the Averaging Problem from 3.0 is
  **true as stated** (Ge `internal` → `holds`).
- The A5h modelling objection, **adopted at its strongest, strengthens his stated direction** and
  costs the critics the s = 0.001 escape (0.68 → e^−384 ≈ 1.7e−167).
- Three statements of credit from the panel itself: the division is correct (GGR-04); the
  AI-peer-review exercise was good and its review fair (GGR-45, from his harshest critic on that
  branch); d = 1 was a concession to the other side (GGR-46).
- Three Statement quotes re-verify **verbatim** after the local text was lost: no quote drift
  against him.

**For the critics**
- **GGR-31/GGR-32 reach 3,840 independently** — the audit's exact value — by a six-person panel
  with no reference to this audit. The strongest corroboration A5h's `arithmetic-error` can get.
- **GGR-34 is right in standard theory**: equilibrium load depends on U, not s (Haldane 1937;
  Muller 1950). The s-dependence of "functionally dead" is Day's model's, not biology's.
- **GGR-20 is literally exact**: "mentioned once in that paper and not defined" — one occurrence,
  undefined. GGR-12 is right too. Neither panellist erred; the audit's NOTE-5 did.
- **Reading (c) is partly right**: an overlapping-generations correction **is** still in play in
  3.0, inside the §8.6 rate, which Day nowhere explains after dropping d.
- The host's 01:49:52 narration ("throws the D coefficient off to the side") is exactly right.
- **GGR-42's attribution of Day on recombination is accurate**, verified verbatim at §2
  (main:128–131), and `R4-G1.md` backs the substance: free recombination gives independence
  (1.03 ± 0.02 × p²), while joint < product only when linked (0.84 / 0.65) or clonal (0).
- The panel's reply to the Bernoulli barrier was real and substantive, and this pass grades it on
  the merits rather than on the harvest's erased sentence.

**Both / the audit's own errors**
- **The Q1 band table was not exhaustive.** Band 1b assumed the Bio-Cycle citation would sit in an
  appendix; it sits in the body, and MITTENS 3.0 has no appendix. A pre-registration defect of this
  pass, found by the very search it registered. Recorded as a miss above.
- **I declined an instruction the brief wrote in advance** (add a `reading-dependent:` comment to
  A4d). Reason given, flagged for the reviewers. If they rule the other way it is a one-line fix —
  but it is a departure, not a judgement call I get to bury.
- **A4d's Weaknesses line** calls it "the later 'Appendix D' human-derived rate", which reads as
  though 3.0 contains an Appendix D. It does not; §8.6 cites *Day and Athos 2025*, Appendix D.
  Corrected in this pass.
- **The combined review's NOTE-5 invented a panel inconsistency** between GGR-12 and GGR-20. There
  is none; both are right. An audit error against the critics, the second of its kind from this
  source after MAJOR-1.
- **A4d's `holds` had been resting on a search of a file the audit no longer had** since
  `sources/raw/` was cleared. It was right, but it was unverifiable for the interval. The
  general lesson is a provenance one and belongs to the bookkeeping task, not to either side.
- R-2's half (ii) ("the word 'load' does not occur in it") was asserted from an excerpt in the fix
  pass; it is only now verified over the whole text. It held.

## Open

1. **Ge `external` `pending` → `contested`** — proposed, not applied (outside the registered bands).
2. **A new critic-side node** for the infinitesimal-model answer (GGR-43/GGR-44), child of G,
   `internal: pending` — proposed; this task may not create claim files.
3. **A defeater pair** on §2's "No recombination overhead" bullet, citing GGR-42 and R4-G1's
   1.03 ± 0.02 — proposed for `defeaters.yaml` at integration.
4. **GGR-46 into A4's Responses** — A4 is outside this task's file list.
5. **Balance-ledger row for branch G** from this pass (best for Day: BB is absent from 3.0 so the
   branch is no longer load-bearing for the headline argument; best for critics: recombination
   against §2, with R4-G1 behind it) — for the integration task.
6. **The lost `sources/raw/day/zenodo-23003785.txt`.** This pass re-fetched into its own new
   directory and did not restore the old path. Whether the audit re-establishes a canonical local
   copy is a bookkeeping decision, not mine.
7. **GGR-19's Reddit original is still unlocated.** The audit scores a relay (rule U). Locating it
   would let branch G be scored against a primary statement.

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

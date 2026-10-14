---
id: Ge
title: "Day: MITTENS 3.0 omits the Bernoulli Barrier and the Averaging Problem as moot, but both \"remain entirely correct\""
side: day
branch: G
parent: G
edges: [{type: revises, target: G}, {type: supersedes, target: G}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds   # R4 VID-01-score (2026-10-13), registered band 4a: verified against a re-fetched, sha256-matched MITTENS 3.0 (22bb4ef8...). "Bernoulli" occurs exactly once, in a rhetorical clause in s1, undefined and underived; "Averaging"/"averaging problem"/"law of large numbers" occur 0 times in body and addendum. The omission half of the statement is true as stated
  fidelity: n/a
  external: pending   # the second clause, "both of them remain entirely correct", is a claim about G, whose own external is `contested`. R4 VID-01-score proposed `pending` -> `contested` but did NOT apply it: outside its registered bands. For the integration task
---

## Statement (verbatim)
> Anyhow, the MITTENS 3.0 paper [URL: https://zenodo.org/records/23003785] renders those complicating elements moot to such an extent that I omitted both the Bernoulli Barrier and the Averaging Problem, even though both of them remain entirely correct.

Source: [They Never Stop Lying](https://voxday.net/2026/10/01/they-never-stop-lying/) (key B2026-10-01-they-never-stop-lying), blog, 2026-10-01, ¶26.


RH tag (2026-10-10 pass): dialectic (stated as a checkable claim or derivation; no rhetorical device scored).
## Formal statement
Version note: MITTENS 2025 (Z18165980) included p^n = 0.02^(2e7); the 3.0 paper (Z23003785) contains "Bernoulli Barrier" only in a rhetorical sentence in s1 ("When the Bernoulli Barrier demonstrates that parallel fixation is probabilistically self-defeating, the defender invokes neutral drift"). In the same post (¶22) Day says: "neither the Bernoulli Barrier nor the Hard Limit on neutral drift apply to the LTEE experiment because a) the math is an average of 12 different populations and b) there is no time for neutral drift to have occured yet in the 85,000-generation time limit of the LTEE." and ¶24 quotes a passage (stated to be from Appendix A of the book) "Therefore fixation must be sequential." (see G2g).

## Assumptions
- Stated: the 3.0 numbers incorporate parallel fixation, so BB is not needed there.
- Implicit: BB applies to real species but not to the LTEE.

## Responses
- Against: KITTENS §11 says "Version 3.0 says the “Bernoulli Barrier” is moot, but §5.1 still appeals to the finite carrying capacity of the selective environment, which needs the same qualifications." The wording "moot" appears in Day's blog, not in the 3.0 text; the substantive point (§5.1 carries a related limit) is a critic's observation.
- In support: none beyond Day.
- Weaknesses in the responses: if BB does not apply to the LTEE but does apply to humans, the LTEE rate is not a like-for-like measure of what parallelism achieves in a recombining species; the text does not say whether BB can only lower the human rate. Day uses BB to rule out parallel fixation "a priori" while G1 argues parallelism is included in G_f; see G2g for the resulting tension.

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
Not testable; consistency note.

## Check
No script.

R4 VID-01-score (`research/checks/results/R4-VID-01-score.md`, 2026-10-13; predictions and the band
table pre-registered at `e857d1f` before the text was re-fetched). Settles review NOTE-5 of check
VID-01. The MITTENS 3.0 text had been lost from `sources/raw/`; it was re-fetched read-only into its
own new directory and both sha256s matched the pinned `bib-day.md` values (`22bb4ef8...`, addendum
`d55e8a03...`), so the registered search ran. **Registered band 4a, hit exactly:**

| Term | Hits (body + addendum) |
|---|---|
| `Bernoulli` | **exactly 1**, s1: "When the Bernoulli Barrier demonstrates that parallel fixation is probabilistically self-defeating, the defender invokes neutral drift" - inside a paragraph on "the characteristic rhetorical structure" of the polythesis. No definition, no derivation, no number |
| `Bernoullian`, any other `barrier`, `Averaging`, `averaging problem`, `law of large numbers` | **0** |
| `coefficient of variation` | 1, addendum, descriptive statistics of per-population fixation counts; unrelated to the barrier |

**`internal` moves `pending` -> `holds`.** Day's statement that he omitted both the Bernoulli Barrier
and the Averaging Problem from 3.0 is **true as stated**: the Averaging Problem as a named argument
is absent and the Barrier survives only as one undefined clause, which under rule C is "omitted",
not retained. This is an accuracy credit to Day about his own work, now verified against a
hash-matched text rather than against a file the audit no longer had. The Formal statement above
("only in a rhetorical sentence in s1") is confirmed **verbatim**: `Bernoulli` occurs exactly once,
main:55, undefined. **Scope (fix pass, correctness MINOR-4):** band 4a is applied to the **omission
clause only** (rule S); the second clause is an external question and that field is unchanged.

**Which gloss of "the Averaging Problem" was tested** (fix pass 2026-10-13, correctness MAJOR-4
accepted). A token search decides only if "the Averaging Problem" is a **named argument**, and the
audit glosses it two ways. Both are tested and both give the same answer, so the verdict is
unaffected - but "absent outright" and "exhaustively" claimed more than a token search over a
two-gloss term can establish, on the one field this check moved, and that wording is narrowed:
- **Gloss (i), a named argument** (`G2g-appendix-a-fixation-must-be-sequential.md` line 29,
  "(Averaging Problem: polygenic rescue impossible)"): the token search decides, and the decisive
  negative is **`polygenic` 0 occurrences** in body and addendum (post hoc term, added in the fix
  pass), beside `Averaging` / `averaging problem` / `law of large numbers` 0.
- **Gloss (ii), Day's PP22 in the same blog post as the Statement** ("the math is an average of 12
  different populations"): the nearest substantive material is in the addendum the search already
  covered, and it runs **for** this claim. The addendum is titled "Per-Population Dispersion and
  Best-Case Robustness", reports each population separately, and says at s3 (addendum:83-84),
  verbatim: "These are not averages. They are the best data point in each category, chosen to be as
  generous as possible to the standard model." That is 3.0 **answering** an averaging objection and
  replacing the averaged treatment with a per-population one - omission by replacement - not
  **deploying** the Averaging Problem; which is what the Statement itself says ("renders those
  complicating elements moot to such an extent that I omitted both").

**The surviving s1 clause, under rule RH3** (fix pass, critic-side steelman MINOR-2 accepted; lead
ruling R-15). The clause is not purely rhetorical in the RH sense. Verbatim, main:55-56: "**When the
Bernoulli Barrier demonstrates that parallel fixation is probabilistically self-defeating**, the
defender invokes neutral drift." That is an indicative assertion *that the Barrier demonstrates
something*, used as a premise in s1's case that the polythesis is ad hoc, with no support anywhere
in the paper (no p^n, no number, no derivation). `R4-X1-verdict-rule.md` RH3: "A node whose only
support is rhetoric is marked '**no dialectical support offered**'. **It is not marked an error.**"
So the record is both halves at once: the argument **is** omitted (Day's statement true, `holds`
stands) **and** its conclusion is asserted once in s1 without dialectical support in 3.0. Ledgered
as **RH-33** in `ledgers/slips.md`. This is **not** an error and **not** a reason to disturb
`holds`. The opposite reading the brief asked review 3 to test - that naming the Barrier while
omitting its defence is having it both ways - was tested by that reviewer, against its own side,
and **fails**: rule C decides it.

**The two critic statements are both right, and the review's NOTE-5 was wrong to call them
inconsistent.** GG-4: "Essentially, he omits the averaging error stuff as well as the Bernoli barrier
stuff" (GGR-12, t=01:50:12) and "It's mentioned once in that paper and not defined" (GGR-20,
t=01:55:39) state the same fact at different precision. GGR-20 is literally exact. Recorded as an
audit-side error in the write-up's "Both" section.

**Not applied, proposed:** `external` `pending` -> `contested` for the second clause ("both of them
remain entirely correct"), inheriting G's existing `external: contested` and G's ledgered label
slip. The scoring task's registered bands licensed only the internal move, so it left the external
field alone. **Qualified in the fix pass (Day-side steelman MINOR-4, accepted):** the proposal's own
ground is that it *inherits* G's verdict, so applying it would record `contested` at both G and Ge
for one contested proposition, in counts (HANDOFF, README, argmap) that do not distinguish inherited
from independent verdicts. If integration applies it, it must carry an explicit `inherited-from: G`
note and be excluded from independent verdict counts; otherwise it should be declined. **It must not
be applied silently.**

Consequence for branch G: the Barrier is not an argument of MITTENS 3.0, so the GG-4 panel's replies
to it (GGR-41..GGR-44) answer the January 2026 Zenodo paper (Z18167588, claim G), not 3.0.

## Simulator variables implied
- None.

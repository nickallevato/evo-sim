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
and the Averaging Problem from 3.0 is **true as stated**: the Averaging Problem is absent outright
and the Barrier survives only as one undefined rhetorical clause, which under rule C is "omitted",
not retained. This is an accuracy credit to Day about his own work, now verified against a
hash-matched text rather than against a file the audit no longer had. The Formal statement above
("only in a rhetorical sentence in s1") is confirmed verbatim and exhaustively.

**The two critic statements are both right, and the review's NOTE-5 was wrong to call them
inconsistent.** GG-4: "Essentially, he omits the averaging error stuff as well as the Bernoli barrier
stuff" (GGR-12, t=01:50:12) and "It's mentioned once in that paper and not defined" (GGR-20,
t=01:55:39) state the same fact at different precision. GGR-20 is literally exact. Recorded as an
audit-side error in the write-up's "Both" section.

**Not applied, proposed:** `external` `pending` -> `contested` for the second clause ("both of them
remain entirely correct"), inheriting G's existing `external: contested` and G's ledgered label
slip. The scoring task's registered bands licensed only the internal move, so it left the external
field alone.

Consequence for branch G: the Barrier is not an argument of MITTENS 3.0, so the GG-4 panel's replies
to it (GGR-41..GGR-44) answer the January 2026 Zenodo paper (Z18167588, claim G), not 3.0.

## Simulator variables implied
- None.

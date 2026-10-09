---
id: A2j
title: "Day's headline G_f drifts between versions: 1,400 (2nd-edition abstract, 180 fixations, 1,139,000-fold), 1,322 (Z23003785) and 1,587 (2026-10-03, 'the more accurate number')"
side: day
branch: A
parent: A2
edges: [{type: revises, target: A2}, {type: depends-on, target: A3a}]
load_bearing: false  # version datum; the shortfall's order of magnitude does not depend on which G_f
sourcing: firsthand
status: extracted
verdicts:
  internal: holds   # 252,000/1,400 = 180; 205e6/180 = 1,138,889; 252,000/1,587 = 158.8; 205e6/158.8 = 1.29e6
  fidelity: pending   # 1,400 is not either LTEE count (1,322 at >=95%; 1,587 strict, A2b); its source is not given
  external: contested   # numerator is the 205M base-pair figure (A3a, R4 GAP-07b); 'fastest empirical rate ever measured' is the A2d/A2e/A2i question
---

## Statement (verbatim)
> "we calculate that natural selection can accomplish at most 180 fixations on the human lineage given 252,000 generations and 1,400 generations per fixation (the fastest empirical rate ever measured in any organism). This represents 0.000088% of the approximately 205 million fixations required on the human lineage. The shortfall is 1,139,000-fold."

Source: [Vox Day, comment on McCarthy, "Vox Day Responds"](https://dennismccarthy.substack.com/p/vox-day-responds/comment/340102853), 2026-09-18, comment id 340102853, quoting the *Probability Zero* 2nd-edition abstract (Q91).

> "The more accurate number, as it turns out when you do what the scientists didn't do and go to the high-resolution data set for all 273,000 generations across the 12 populations, then run the numbers, is 1,587 generations per fixation."

Source: [Vox Day, "An Intelligent Groove", AI Central](https://substack.aicentral.blog/p/an-intelligent-groove), 2026-10-03, para 16 (Q85).

## Formal statement
F_max = T / G_f with T = 252,000 generations. `derived:` (python3 -I) G_f = 1,400: 180 fixations, shortfall 205e6/180 = 1,138,889; G_f = 1,322: 190.6 (Day: 191), 1,075,000; G_f = 1,587: 158.8, 1.29e6. The 1,587 is the audit's derived strict-count value in A2b, now stated by Day. The same AI Central post reposts the Z23003785 abstract with 1,322 unchanged, so no paper was revised.

## Assumptions
- Stated: the LTEE rate is "the fastest empirical rate ever measured in any organism".
- Implicit: 205M is a fixation count (A3a; R4 GAP-07b: ~21M events per lineage).

## Responses
- Against: Matev (A2i) on what "fastest" means; the A3x unit argument on the numerator.
- In support: the three G_f values differ by 20% and do not move the order of magnitude; Day adopting the stricter 1,587 makes his own number less favourable to his conclusion than 1,322 (fewer fixations available, larger shortfall), so the revision is not self-serving in that direction.
- Weaknesses in the responses: none specific.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Z23105291 (Day's LTEE data paper) | strict lineage-aware count 5,496 fixations (A2b) | see A2b |

## Pre-registered prediction
Not run (arithmetic only).

## Check
Arithmetic (python3 -I) above. Version rows: `ledgers/versions.md` ("2nd-edition headline numbers"; "Day's own adoption of 1,587"). From the 2026-10-09 corpus refresh (D-3, D-5d).

## Simulator variables implied
G_f counting rule (>=95% vs lineage-aware) as an explicit option.

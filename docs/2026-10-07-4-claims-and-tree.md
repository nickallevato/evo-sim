# Milestone 4: 193 claims, one tree
*2026-10-07 · stages: R2 and R3 · commits `d2bb0c0`, `ad44c23`*

## R2: claim extraction
Every mathematical or empirical assertion in the corpus became a claim file in `docs/research/claims/`. Each file has:
- a verbatim quote with a locator and date;
- a formal statement;
- the stated and implied assumptions;
- the other side's response;
- a pre-registered prediction;
- three verdict slots.

| Source of claims | Count |
|---|---|
| Day | 107 |
| Critics | 46 |
| Allies | 16 |
| Literature | 24 |
| **Total** | **193** |

The counts are uneven because Day wrote far more quantitative material than any critic. The rule was equal scrutiny per claim, not equal numbers of claims.

R2 found errors on the critics' side as well as Day's:
- Zach Hancock's first pass used a diploid count, which he corrected on screen.
- Hancock's retained figure of 76 is an event count that includes structural variants.
- Hancock's bacterial mutation rate of 1e-11 is below the measured 8.9e-11.
- The basis of Nesslig20's μ_G = 75 is not stated.

## R3: the argument tree
- **Generated, not hand-drawn.** `hierarchy.yaml` and the per-branch Mermaid diagrams are built from the claim files, so the tree cannot drift out of sync with them.
- **Lint.** It checks for orphan claims, missing sources or verdicts, and untraceable numbers. The lint passes clean.
- **Load-bearing nodes.** 30 claims are marked load-bearing for Day's root claim, which is that no evolutionary mechanism can produce the observed divergence in the time available.

The tree still has the eight branches from pass 1. R2 sharpened several of them:

| Branch | Change |
|---|---|
| A3x | Split out the base-pairs vs events question behind "205M". |
| B1d | Records Day's own statement that the ancestral pipe was full. |
| B3b and B3c | Separate the Balloux–Lehmann mechanism from Day's 0.743 figure. |
| B5c and B5e | Hold the critics' "38M matches 35M SNVs" claims, so they can be checked like any other. |
| C6 | Isolates Day's ancient-DNA "21 fixations" count from the broader zero-fixations argument. |

## Why this step matters for an outside reader
The tree is where neutrality can be audited. Every critic and ally argument has to attach to a node, so a gap is visible as an empty slot. The clearest example: no critic in the corpus engaged the cost-of-selection literature on Nunney's side (branch H).

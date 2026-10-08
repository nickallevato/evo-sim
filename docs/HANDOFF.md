# evo-sim: a briefing for independent assessment

*Status as of 2026-10-08 (revised the same day: Day's dated concessions added; milestone posts linked). Repo: <https://github.com/nickallevato/evo-sim> (branch `research`).*

This note is for a team that has not followed the project and wants to form its own view of it. It describes what the project is, what it has found, and where its findings and methods are weakest. It does not argue for any side. Wherever this note and the repo disagree, trust the repo.

## What the project is
evo-sim has two stages.

**1. A research audit (in progress).** The audit examines Vox Day's mathematical argument against evolution, which Day calls MITTENS and develops in the book *Probability Zero* (2025), about 30 Zenodo papers and several years of blog posts. It examines the published rebuttals to that argument with the same rigour. Day's claim is that population genetics rules out natural selection as the explanation for the human–chimp divergence in the time available. The critics, mostly bloggers, Substack writers and YouTubers, say Day's maths is wrong.

**2. A simulator (not started).** The planned output is an open-source evolution simulator. Its controls will be the parameters the dispute actually turns on, so that anyone can test either side's claims. No simulator code exists yet. The project rules hold back simulator work until the audit meets its exit criteria.

## How the audit works
1. **Corpus.** Day's posts and papers from 2019 onward, the primary literature Day cites, and the critics' and allies' responses. In numbers: 154 posts, 32 Zenodo records, 37 papers and 48 critic or ally sources.
2. **Claims.** 193 distinct mathematical or empirical claims, each with a verbatim quote, a source locator and a date. Claims come from both sides.
3. **Argument tree.** Each claim is attached to one of eight branches (A–H) under Day's root claim. Thirty nodes are marked as load-bearing.
4. **Checks.** Each load-bearing equation is tested with an exact Markov chain or a forward simulation. The prediction is written down before the run. Seventeen checks have been reviewed so far.
5. **Reviews.** Every check gets three reviews: one for correctness, one steelmanning Day's position, and one steelmanning the critics'. A check counts only after it passes all three.
6. **Verdicts.** Each claim gets three separate verdicts:
   - *Internal:* does the conclusion follow from the author's own premises?
   - *Fidelity:* does the cited source actually say what the author says it does?
   - *External:* are the premises realistic?

The project rules require valid points to be recorded as prominently as errors, whichever side makes them. Each branch has a balance ledger with columns for "best for Day" and "best for critics".

## What it has found so far
These are R4 results. The R5 synthesis has not been done, so every verdict is provisional.

**Points where Day's maths holds up:**
- **Empty pipe.** Day's formula, E[F] = μL∫F_X, is exact for its premise: a population that starts with no standing variation.
- **Timescale.** Nₑ does set the timescale of fixation.
- **Hard Limits tail.** The exponent −π²Nₑ/G is the correct leading-order tail.
- **LTEE rate.** The bacterial figure of about 1,300 generations per fixation is a real throughput measurement, and it reproduces.
- **Balloux–Lehmann effect.** It is real: with overlapping generations and a fluctuating population size, k ≠ μ. The critics' blanket "k = μ" holds only for discrete generations.
- **Cost of selection.** In the audit's reconstruction, soft selection does not make the cost disappear.
- **Haldane's arithmetic** (300 and 487) holds.
- **A critic's double count.** The critics' claim that "38M matches 35M SNVs" counts the same differences twice.

**Points where the critics' maths holds up:**
- **Neutral rate.** The neutral substitution rate is k = μ for any Nₑ, because fixation probability is set by the census size 1/2N, not by 1/2Nₑ. Day conceded this on 2026-08-27, but a figure of k = 32.3μ reappeared on 2026-10-01 without a derivation. The earlier Zenodo papers that give k = μN/Nₑ were not revised.
- **Start state.** The ancestral population was not an empty pipe. Day has since withdrawn the empty-start premise: on 2026-10-01 Day called the pipe "full, but much shorter".
- **Latency vs throughput.** The time a single fixation takes is not the rate at which fixations happen. Many sweeps can be in flight at once.
- **Recombination.** In the tested regime, recombination removes the clonal-interference ceiling.
- **Divergence.** Human–chimp divergence includes ancestral polymorphism: d = 2μT + θ_anc.
- **Hard-selection cap.** The cap is ln R / D, not a flat 1/300.
- **Required fixations.** The "205M required fixations" figure counts base pairs rather than mutation events.
- **A misread citation.** A selection coefficient Day cites (s = 0.001, from Zeng 2021) is for negative selection, not beneficial.

**Still open:**
- **Cost of selection** at real human fecundity and hard-selected load. This regime is untested.
- **Ancient DNA.** Day's "21 fixations" statistic, which could not be reproduced from its published method.
- **Ancestral Nₑ.** The value needed to fit the observed divergence has three free parameters, so no side gets a clean fit.
- **Branches with no checks yet:** sequence space (D), the LTEE founders (E), and the 0.02^(2×10⁷) "Bernoulli barrier" (G).

**Overall verdict counts** (all sides combined, n/a omitted):

| Verdict | Counts |
|---|---|
| Internal | 89 hold, 14 non-sequitur, 6 arithmetic error, 61 pending |
| Fidelity | 35 accurate, 31 partial, 9 misread, 35 unverifiable |
| External | 21 supported, 97 contested, 9 contradicted, 5 untestable, 50 pending |

Note that the largest external category is *contested*.

## Things a reader should weigh
These are the limits of the project itself, not of either side:

- **AI-driven work.** Nearly all of the harvesting, claim extraction, simulation code and reviewing was done by AI agents (Anthropic's Claude models), directed by one person. The steelman reviews are AI reviewing AI. Day's Zenodo papers list an AI co-author ("Claude Athos"), so the same model family appears on both sides of the audit.
- **No independent review.** Nothing has been peer-reviewed, and no human population geneticist has checked the simulations.
- **Possible lean.** The project's own planning notes record that the first-pass summaries leaned toward the mainstream view. The balance ledgers are meant to correct for that. Whether they succeed is for the reader to judge.
- **Incomplete sources.**
  - *Probability Zero* has not been purchased, so claims that appear only in the book are tagged `secondhand`.
  - Some sources could not be accessed and are listed as such.
  - Full texts are not in the repo, for copyright reasons. Readers must fetch them to check quotes.
  - None of the authors on either side has been contacted, so no one has had a right of reply.
- **Untested regimes.** Several conclusions hold only in the regimes tested: N = 1000, s = 0.01, and a single closed population. Human-scale parameters for the number of loci under selection at once, and for hard-selected load, have not been run. "Holds in the tested regime" is weaker than "holds".
- **A moving target.** The critics are informal and have not engaged several branches, and Day's numbers change between versions. A verdict on one version may not apply to the next.
- **Branding.** The project icon combines a double helix with a Christian cross. That was the maintainer's choice. Readers may weigh it as they see fit when judging the claim of neutrality.

## How to check it yourself
- **Start here:** `README.md` (scorecard, maths and figures), then `docs/research/ledgers/balance.md` (strongest and weakest points per side), then `research/checks/RESULTS.md` and `REVIEW.md`.
- **Spot-check a claim:** open any file in `docs/research/claims/`, follow its source locator, and compare the quote with the original.
- **Re-run a check:** every check runs with a fixed seed using `research/.venv/bin/python -I research/checks/<file>.py`. The textbook baselines (`baseline_textbook.py`) must pass first.
- **Questions worth asking:**
  - Does each check test the claim as its author stated it, or a convenient variant?
  - Are the "tested regime" caveats load-bearing for the headline conclusions?
  - Is the scrutiny actually symmetric?
- **Corrections** from either side are invited as GitHub issues, with a locator.

## Milestone posts
These dated posts tell the story in order:
1. [2026-10-07: The question, the rules, the scaffold](2026-10-07-1-kickoff.md)
2. [2026-10-07: First checks and three rounds of review](2026-10-07-2-first-checks.md)
3. [2026-10-07: Reading everything, from both sides](2026-10-07-3-reading-everything.md)
4. [2026-10-07: 193 claims, one tree](2026-10-07-4-claims-and-tree.md)
5. [2026-10-08: R4 round two, the load-bearing checks](2026-10-08-5-r4-round-two.md)
6. [2026-10-08: Making it inspectable](2026-10-08-6-going-public.md)

## Not yet decided
- The final verdicts and the sensitivity table (R5).
- Whether the audit's conclusions bear on the root claim as a whole, or only on individual branches.
- The simulator's design.

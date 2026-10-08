# Plan: ELI5 / ELI12 / ELI18 explainers
*Drafted 2026-10-08.*

> **Update, 2026-10-08:** the maintainer chose plain READMEs with no build step. Drafts now live in [`docs/explain/`](../explain/README.md), one folder per level (ELI8 and ELI10 were added the same day), with graphics from `research/tools/eli_figs.py`. The `beats.yaml` generator, lint and toggle Artifact below are **dropped**. The seven-beat spine, the analogy cautions and the neutrality reviews still apply. After R5: update the numbers by hand, then run the two-sided steelman and fact-check reviews on all three versions.

## Goal
Three versions of the whole story at three reading levels: the question, Day's argument, the critics' replies, what the checks found, and what is still open. Each version must be **as neutral as the audit itself**. Simplifying must never quietly pick a side.

## One spine, three depths
Every version follows the same seven beats, so a reader can step up a level without getting lost. The beats live in one source file, `docs/explain/beats.yaml`. Each beat holds per-tier text and the claim IDs it rests on, and a lint checks that every tier covers every beat.

| # | Beat | ELI5 (read aloud, ~600 words) | ELI12 (~1,500 words) | ELI18 (~4,000 words) |
|---|---|---|---|---|
| 1 | The question | "Is there enough time for all the changes?" | Generations, mutations, fixation | MITTENS formula, both sides' framing |
| 2 | Day's argument | A counting race that looks impossible | The LTEE rate × generations vs differences | F_max, G_f, d, versions and drift |
| 3 | The critics' replies | "Lots of changes can happen at once" | Parallel sweeps, k = μ, ancestral variation | Latency vs throughput, 2μT + θ_anc, recombination |
| 4 | What the checks found for Day | Some of his sums are right | Empty-pipe maths exact; Haldane holds; soft selection didn't help | B1, B2a, B3b, H/H2 with numbers |
| 5 | What the checks found for the critics | Some of his numbers were counted wrong | k = μ; full pipe; bp vs events; misread citation | B3, B1c, A3x, Zeng, Yoo, with numbers |
| 6 | Both sides slipped | Everyone made a mistake somewhere | 38M double count; 21 fixations not reproducible | B5c/B5e, C1b; dated concessions |
| 7 | Still open, and how we checked | "We're still checking!" | Cost at human scale; Bernoulli barrier; limits of the audit | Full open list, method, AI disclosure, how to re-run |

## Analogy ledger
Analogies are where simplification usually picks a side. Each one goes in `docs/explain/analogies.md` with:
- the concept it stands for;
- where it breaks;
- a check from each side's steelman that it doesn't help one side.

| Concept | Candidate analogy | Where it breaks |
|---|---|---|
| Latency vs throughput | A pipe or conveyor: each box takes 10 minutes to travel, but one arrives every minute | Interference: boxes can block each other (Day's real point) |
| Fixation probability 1/2N | One raffle ticket among 2N | Selection changes the odds |
| Drift | Coin flips deciding which marbles get copied | Overlapping generations |
| bp vs events | Counting letters in a typo vs counting typos | Some events really do span many bases |
| Ancestral polymorphism | Cousins already differed before the families moved apart | — |
| Cost of selection | A family can only lose so many kids per generation | Soft vs hard selection |

## Neutrality controls
- **Traceable sentences:** every factual sentence traces to a claim ID and its R5 verdict. No tier may state a conclusion stronger than its verdict, and "contested" stays "contested".
- **Equal treatment:** both sides get the same number of beats, and each side's wins and slips are equally prominent.
- **Review:** each tier is reviewed by a Day-side steelman, a critic-side steelman and a fact-checker against the claim files.
- **ELI5:** frame the topic as "how do we check someone's numbers?", not "who is right about God or evolution?". It makes no claims about faith, and it doesn't name people.
- **ELI12 and ELI18:** use names, along with the AI-co-authorship disclosure and the branding disclosure from `HANDOFF.md`.

## Reading-level checks
Automated with `textstat` in the lint.

| Tier | Target |
|---|---|
| ELI5 | Read-aloud, about grade 1–2 vocabulary |
| ELI12 | Grade 6–7 |
| ELI18 | Grade 11–12. Equations are allowed but always explained in words. |

## Format
- **Primary:** `docs/explain/eli5.md`, `eli12.md` and `eli18.md`, generated from `beats.yaml`.
- **Visuals per tier:**
  - ELI5: simple illustrations.
  - ELI12: three or four simple charts.
  - ELI18: the README figures.
- **Optional:** a single Artifact page with a 5 / 12 / 18 toggle. Once the simulator exists, small "try it" widgets, such as a pipe demo or a raffle demo.

## Build workflow (later)
1. Freeze the R5 verdicts.
2. Draft `beats.yaml` and the analogy ledger.
3. Three writer subagents work in parallel, one per tier.
4. Steelman and fact-check reviews run in parallel. Fix what they find.
5. Run the lint (beats coverage, claim traceability, reading level).
6. Publish, and add a milestone post.

## Decisions for the maintainer (later)
1. Markdown only, or also the toggle Artifact?
2. Does ELI5 show the icon and its cross? (Neutrality trade-off.)
3. Should real readers (a kid, a teen, a non-biologist adult) review before publishing?

<div align="center">

<img src="../../img/icon.svg" width="96" alt="evo-sim icon">

# Is there enough time?
### The whole story, for a twelve-year-old

[ELI5](../eli5/README.md) · **ELI12** · [ELI18](../eli18/README.md) · [back to the project](../../../README.md)

</div>

---

## 1. The question
Your DNA is a set of instructions about 3 billion letters long. Every time it's copied into a new baby, a few letters come out wrong. Those are **mutations**. Most do nothing, some are harmful, and a few are helpful.

When a mutation spreads until *everyone* in a species has it, scientists say it has become **fixed**. Humans and chimpanzees split from shared ancestors roughly 6–8 million years ago (estimates differ), about 250,000 generations. Since then their DNA has drifted apart by about **1.2%**, which is tens of millions of letter differences.

The question this project looks at: **could evolution produce that many fixed changes in that much time?**

## 2. Vox Day's argument: "not enough time"
Vox Day is a writer who argues the answer is no. The argument appears in a book (*Probability Zero*, 2025), a series of online papers, and blog posts. The main formula, which Day calls **MITTENS**, works like this:

1. In Richard Lenski's famous lab experiment, *E. coli* bacteria have been evolving since 1988. They pile up fixed changes at about **one per 1,300 generations**.
2. Humans have had about 250,000 generations since the split. At that rate, that's only about 190 fixed changes.
3. The differences we actually see number in the tens of millions.
4. So evolution comes up short by about **1,000,000 times**.

Day also argues that population size slows things down, and that each change "costs" the population something (an idea from the scientist J.B.S. Haldane in 1957).

## 3. The critics: "the math has mistakes"
Several writers and YouTubers pushed back, including Dennis McCarthy, Brian Mansfield, Zach Hancock, Camestros Felapton and others. Their main points:

**Many changes can spread at once.** One change taking a long time to spread doesn't mean changes only finish rarely. It's like a conveyor belt: every box rides a long time, but boxes keep arriving at the end.

<p align="center"><img src="../../img/eli/conveyor.svg" width="600" alt="Conveyor belt"></p>

**Neutral changes keep pace with mutation.** A classic result in population genetics says changes that don't matter for survival become fixed at the same rate they appear, no matter how big the population is.

**Some differences are older than the split.** The shared ancestors already varied, so not every difference is new since then.

<p align="center"><img src="../../img/eli/cousins.svg" width="600" alt="Ancestral variation"></p>

**Bacteria aren't people.** Bacteria copy themselves without mixing DNA. Humans mix DNA from two parents every generation, which lets helpful changes combine instead of competing.

## 4. How we checked
We collected **193 separate claims** from both sides, each with an exact quote and source. Then:
- We wrote computer simulations: virtual populations having babies for thousands of generations, with mutations, while we count what becomes fixed.
- We wrote down what each side predicts *before* running each test, so nobody could move the goalposts.
- Every test was checked by reviewers who argued for Day's side, and by others who argued for the critics' side.

## 5. What we found
<p align="center"><img src="../../img/eli/both-sides.svg" width="640" alt="Scorecard for both sides"></p>

**Where Day's math holds up:**
- If a population starts with *no* variation at all, Day's formula is **exactly** right.
- Population size really does control how *long* a change takes to spread.
- The bacteria rate of about 1,300 generations per change is real; our simulations reproduce it.
- Haldane's old arithmetic (one change per 300 generations) adds up.
- "Soft selection", an idea the critics used to make the cost go away, **didn't** make it go away in our tests.

**Where the critics' math holds up:**
- Neutral changes do fix at the mutation rate whatever the population size. Day agreed with this in August 2026, though a different number showed up again later.
- The ancestors were *not* an empty starting point, and Day has agreed with that too.
- Many changes really can spread at once when DNA mixes.
- Day's "205 million required changes" counts every **letter** of big insertions and deletions as its own change, instead of counting **mutation events**. That's the biggest bookkeeping problem:

<p align="center"><img src="../../img/eli/typos.svg" width="600" alt="Counting letters vs events"></p>
<p align="center"><img src="../../img/eli/shortfall.svg" width="640" alt="Where the million-times shortfall comes from"></p>

Fixing the counting shrinks the gap by about 12×. The ~92,000× that's left depends on whether the bacteria rate tells us anything about humans, and that is still argued about.

**Where both sides slipped:**
- Some critics said "the math predicts 38 million and we see 35 million, a perfect match!" But that counted some differences twice.
- Neither side's favourite population size fits the real data cleanly:

<p align="center"><img src="../../img/eli/divergence.svg" width="580" alt="Divergence fit"></p>

## 6. Still open
- **Cost of selection at human scale.** Can a slow-breeding species like ours afford many helpful changes spreading at once? This hasn't been tested yet.
- **Day's ancient-DNA count** ("only 21 changes became fixed in 7,000 years"). We couldn't reproduce it from the method Day published.
- **Three topics we haven't tested at all:** how rare useful DNA sequences are, the bacteria experiment's details, and Day's "Bernoulli barrier" probability.

## 7. Things you should know about us
- Most of this work was done by AI (Claude) with one person directing it. Day's own papers also list an AI co-author.
- No professional scientist has reviewed our simulations yet.
- The project's icon mixes a DNA helix and a Christian cross. That was the creator's design choice, and you can judge for yourself whether the project stays fair.

**The goal isn't to tell you who wins. It's to show the work so you can check it yourself.**

---
<sub>This draft was written before the final verdicts (stage R5), and numbers may change. The [ELI18 version](../eli18/README.md) links every statement to its evidence.</sub>

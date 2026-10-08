<div align="center">

<img src="../../img/icon.svg" width="96" alt="evo-sim icon">

# Is there enough time?
### The whole story, for a ten-year-old

[ELI5](../eli5/README.md) · [ELI8](../eli8/README.md) · **ELI10** · [ELI12](../eli12/README.md) · [ELI18](../eli18/README.md) · [back to the project](../../../README.md)

</div>

---

## 1. The question
Your **DNA** is a set of instructions for building you, written in a four-letter code about 3 billion letters long. Every time it's copied into a new baby, a few letters come out different. Those are **mutations**. Most do nothing, some cause problems, and a few help.

Sometimes a mutation spreads, generation after generation, until *everyone* in a species has it. Scientists call that a **fixed** change.

People and chimpanzees share ancestors from millions of years ago, roughly 250,000 generations back. Since then our DNA has become different in about **1 letter out of every 80**. That's tens of millions of differences.

**The question: could that many changes really have happened in that much time?**

## 2. Vox Day's side: "not enough time"
Vox Day is a writer who says no. Day wrote a book and many articles about it. The main math goes like this:

1. In a famous lab experiment, scientists have watched *E. coli* bacteria evolve since 1988.
2. The bacteria got a new fixed change only about once every **1,300 generations**.
3. If humans changed at that speed, 250,000 generations would give only about **190** changes.
4. We see *millions*, so Day says we'd need about **a million times** more time.

## 3. The critics' side: "the math is wrong"
Several scientists and science writers answered. Their main points:

**Many changes can spread at once.** One change taking a long time to spread doesn't mean changes finish slowly, just like a full conveyor belt keeps delivering boxes even though each ride is long.

<p align="center"><img src="../../img/eli/conveyor.svg" width="600" alt="Conveyor belt"></p>

**Group size evens out.** Day's math said the size of a group changes how fast unimportant mutations pile up. Critics said it evens out. A bigger group makes *more* new mutations, but each one has a *smaller* chance of spreading, like a raffle with more tickets.

<p align="center"><img src="../../img/eli/raffle.svg" width="600" alt="Raffle: more changes, smaller odds, same result"></p>

**Some differences are older than the split.** The ancestors already varied, so not every difference is new.

<p align="center"><img src="../../img/eli/cousins.svg" width="600" alt="Ancestors already differed"></p>

**Bacteria aren't people.** Bacteria copy themselves alone. People get DNA from two parents and mix it every generation, which lets helpful changes team up instead of getting in each other's way.

## 4. How we checked
- We collected **193 claims** from both sides, each with an exact quote and where it came from.
- We wrote computer programs that act like populations having babies for thousands of generations, and we counted which changes became fixed.
- Before each test, we wrote down what each side predicted. Then we ran it.
- Reviewers checked every test. Some argued for Day's side, and some argued for the critics' side.

## 5. What we found
<p align="center"><img src="../../img/eli/both-sides.svg" width="640" alt="Scorecard for both sides"></p>

**Day got these right:**
- If a population starts with *no* differences at all, Day's math is exactly right.
- Bigger populations really do take *longer* to spread each change.
- The bacteria number (about 1,300) is real. Our programs got the same answer.
- An old calculation by the scientist J.B.S. Haldane (about one change per 300 generations) adds up correctly.
- One fix the critics suggested, called "soft selection", didn't work in our tests.

**The critics got these right:**
- The raffle idea is correct: bigger groups don't change how often neutral changes get fixed. Day agreed with this in 2026, though a different number appeared again later.
- The ancestors *did* already have differences. Day agreed with this too.
- When DNA gets mixed, many changes can spread at once.
- Day counted some big changes letter by letter instead of as one change each. That made the gap about **12 times** too big:

<p align="center"><img src="../../img/eli/typos.svg" width="600" alt="Counting letters vs changes"></p>

**Both sides made mistakes:**
- Some critics said their numbers were "a perfect match", but they had counted some differences twice.
- Neither side's favourite numbers fit the real DNA data cleanly.

## 6. Still open
- **Cost of change:** when a helpful change spreads, other individuals have fewer babies. Can a slow-breeding animal like us afford lots of that at once? We haven't tested it at human numbers yet.
- **The rest of the gap:** after fixing the counting, the gap is still about 92,000 times. Whether the bacteria experiment tells us much about people is still argued about.
- Some parts of Day's argument haven't been tested yet.

## 7. Things to know about us
- Most of this work was done by AI (a computer program called Claude) with one person in charge. Day's own papers also list an AI as co-author.
- Outside scientists haven't checked our programs yet.
- **Our goal isn't to tell you who wins. It's to show all the work, so you can check it yourself.**

---
<sub>This draft was written before the final verdicts (stage R5), so numbers may change. The [ELI18 version](../eli18/README.md) links every statement to its evidence.</sub>

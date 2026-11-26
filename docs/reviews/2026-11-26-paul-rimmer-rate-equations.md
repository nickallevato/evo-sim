# Review: "Mathematical Models of Evolution are NOT (just) Rate Equations" (Paul, Substack)

_Lead review written at the owner's request (EVOA-102). Not an audit check: no claim file, verdict or count changed. Scope: the owner asked for the errors from Day's side; §5 gives the critic-side steelman at equal depth (hard rule 1)._

**Source.** Paul (Paul B. Rimmer per his footnotes 3–4, Cambridge), [paulnottheapostle.substack.com/p/mathematical-models-of-evolution](https://paulnottheapostle.substack.com/p/mathematical-models-of-evolution), `post_date` 2026-11-08 (page JSON), public post, about 2,700 words. Fetched 2026-11-26 into gitignored `sources/raw/paulnottheapostle-2026-11-26/`, `page.html` sha256 `20061906c2badd561961534ef5c99cb2bd0d1b1db2bdf761904e81eedafd6cde`. The figures are images and are not in the text, so I recomputed every curve from his closed-form formula.

**Scope.** You asked for the maths and for where it goes wrong from Beale's (Day's) side. Hard rule 1 still applies, so §5 gives the critic-side steelman at equal depth. This is a lead review for you. It is not an audit check, and nothing in the claim files or verdict fields moved.

---

## 1. What the author argues

Will Duffy called MITTENS a "rate equation". Paul is a chemist who works with rate equations, and he takes that framing literally. He builds the simplest rate model of neutral copying errors and asks how fast two individuals diverge:

> "Such simple rate equations allow us to explore an equally simple question: How much difference can copying errors produce without selection?" (§1)

He concludes the opposite of MITTENS:

> "given known mutation rates, the rate equation predicts too much variation, not too little." (§3)
> "So is Beale really invoking rate equations? If so, then I've shown his conclusion is not only wrong, it's the opposite of what it should have been." (§3)

He says he did not read Day himself:

> "Since I can't stomach reading Beale's AI-riddled prose. Believe me. I've tried." (footnote 2; the main text says "let's just deal with … Will Duffy's version of the idea")

## 2. The maths, located and reconstructed

Everything is in the end section "The Mathematical Model".

**Model.** N asexual clones, genome length L, generation time τ. Each parent has exactly one child and then dies, so there is no drift, no lineage loss and no selection. Every site mutates with probability κ per generation, to one of the other three bases with equal probability (Jukes–Cantor substitution).

| Step | Equation (his) | Check |
|---|---|---|
| Generations | n = ⌊t/τ⌋ | fine |
| One site stays A | p₍ₙ₊₁₎ = (1−κ)pₙ + (κ/3)(1−pₙ) = (1−4κ/3)pₙ + κ/3 | correct |
| Fixed point | c = 1/4 | correct |
| Solution | pₙ = 1/4 + (3/4)(1−4κ/3)ⁿ | correct |
| Two lineages match at a site | P = pₙ² + 3((1−pₙ)/3)² | correct (independent lineages) |
| Site difference | dₙ = (3/4)[1 − (1−4κ/3)²ⁿ] | **verified algebraically**: 1 − p² − (1−p)²/3 with p = ¼ + ¾a gives ¾(1−a²) |
| Genome | D(t) = (3L/4)[1 − (1−4κ/3)^(2⌊t/τ⌋)] | correct; this is the Jukes–Cantor (JC69) divergence of two lineages |
| Small κ | D ≈ (3L/4)[1 − exp(−8κt/3τ)] | correct |
| Early times | D ≈ 2Lκt/τ | correct; this is the textbook **2μt** two-lineage divergence |

**Inputs and outputs, recomputed** with his inputs: L = 3×10⁹, κ = 1/(5×10⁷) = 2×10⁻⁸, τ = 20 y.
- The early slope is 2Lκ = **120 differences per generation**.
- D/L reaches 1.2 % at **6.05 My** (302,426 generations) and 1.37 % at 6.9 My. At 1 My, 5 My and 10 My it is 0.20 %, 0.99 % and 1.97 %. That matches his "somewhere between 1 and 10 million years". He never states the human–chimp target he used. A target of about 1.2 % SNV divergence fits his figures.
- Bacteria-like aliens (L = 4.6×10⁶, κ = 10⁻¹⁰, τ = 15 h): D/L is 10.8 % at 1 My, 59 % at 10 My and 75.0 % (saturated) at 100 My. That matches his "in 100 million years, there'd be maximal divergence".
- The superseded 30-minute τ saturates in about 1 My (74 %). He corrected this in the post, so under rule SC it is a ledger slip, not an error.

**The arithmetic holds.** I found no arithmetic error in his maths. Every error below is about **what the model measures** and **whether it touches MITTENS**.

## 3. Where it goes wrong, from Day's side

### E1. It measures the wrong quantity: private mutations, not fixations (decisive)
MITTENS counts **fixed** differences per lineage: F_max = t_div·d/(g_len·G_f), where G_f is *generations per fixation* (claim **A**; Day: "I didn't cite the E. coli study for its mutation rate but for its fixation rate", **A5g**). Paul's model has **no fixation at all**. Each parent has exactly one child, so every new mutation stays at frequency 1/N for ever. No derived allele ever spreads through the alien population, and the number of fixed differences stays **zero** at every t. D(t) is the expected difference between **two individuals in one population**. The human–chimp count Day's side uses is the number of differences **fixed between two species**. Paul answers a question MITTENS never asks: he says himself he is asking "how much difference can copying errors produce". Day has never claimed that mutation supply is short.

### E2. The model's own prediction is falsified, and Paul half-concedes this
At 6 My his aliens differ from **each other** by about 1.2 %, as much as humans differ from chimps. Real human pairwise diversity is about 0.1 % (the standard literature figure; this review did not check it against a source). So the model predicts roughly 10× too much *within-species* variation. Paul draws the right lesson: "To explain the diversity we actually see, we would need to show how differences arise and how they are squelched. Some mutations lose out. Some lineages die out." That squelching is drift and selection: the fixation process, which takes time. **That is the process MITTENS is about**, and the model removed it. "Too much variation, not too little" is therefore a statement about the wrong variable.

### E3. Population size cancels only because it was assumed away
> "It turns out, with this rate equation approach, the population size really doesn't matter anymore … These effects perfectly cancel."

In a real population N cancels through 2Nμ × 1/(2N) = μ (claim **B5**), and Day accepts that at steady state (**B2d**, **B3g**). The 1/(2N) term is paid out only after a transit of about 4Nₑ generations, so N comes back in the *time* dimension. That is Day's whole "the pipeline cannot fill" objection (**B1**, **B2**, Z22129121: "the neutral substitutions cannot be finished, because the pipe that would finish them never fills"). Paul's one-child-per-parent model makes the transit time zero, because every lineage is its own "species" from t = 0. **The model assumes the very point Day disputes**, so from Day's side it cannot refute him.

### E4. A non-sequitur against a relay, not against Day (rules U, N)
Paul says he did not read Day (footnote 2) and attacks Duffy's "rate equation" label. Day's equation is a rate × time, but its rate (1/G_f ≈ 1/1,322 to 1/1,600 fixations per generation, an empirical *fixation* throughput) has nothing in common with Paul's rate (2Lκ = 120 *mutations* per generation between two lineages). The "surprisingly similar" look of D ≈ 2Lκt/τ is the same linear form with a different meaning. "I've shown his conclusion is … the opposite" therefore does not follow, because Paul never states or derives Day's quantity. The fallback, "Or maybe Beale's model is really a population genetics model? If so, then Erika already addresses all the problems", hands the real argument to someone else. By its author's own account, the post's maths cannot settle MITTENS on its own.

### E5. Slips (ledger level; they do not move his conclusion)
- "75% difference is the maximum difference any two alien genomes could possibly have." 75 % is the **expected** value at saturation, not the maximum; two genomes can differ at 100 % of sites.
- "This is still way faster than any evolutionary model would predict." This is unsupported. Neutral models also saturate at unconstrained sites over 100 My. What stops real genomes saturating is constraint (selection), which he excluded. It is a mismatch of model to world, not of models to each other.
- The E. coli τ of 30 min was corrected to 15 h in the post (rule SC → ledger).

### E6. Rhetoric (rule RH: tagged and answered, not fact-checked)
"An arrogant loser named Theodore Robert Beale", "game over for Beale's model", "Just trust me, bro" and "AI-riddled prose" are ad hominem and dismissal devices aimed at Duffy's audience. They change no verdict. A better answer turns the reader back to the method: *show the fixed-difference count your model produces*. That count is zero.

## 4. Verdicts under the audit's rule (informal; not entered in any claim file)

| Statement | Internal | Fidelity | Note |
|---|---|---|---|
| D(t) derivation and the numbers in §2 | holds | n/a | standard JC69 |
| "I've shown his conclusion is … the opposite of what it should have been" | **non-sequitur** on the reading "this refutes MITTENS"; **holds** only on the conditional reading "if MITTENS were a mutation-supply rate equation" | **unverifiable** (rule U: attacks Duffy's relay; Day is not quoted) | reading-dependent (rule RD). The most defensible reading is the conditional one, so the field value would be `holds (conditional)` with a `reading-dependent:` note |
| "the rate equation predicts too much variation, not too little" | holds *for within-population pairwise variation in this model* | n/a | true but irrelevant to fixed differences (E1, E2) |

## 5. Critic-side steelman (equal depth, hard rule 1)

- **The number Paul gets is the right between-species number.** Read the two "aliens" as two separated lineages, i.e. two species with no ancestral polymorphism. Then D ≈ 2μt is exactly the neutral expectation for fixed-difference divergence, because at steady state the substitution rate equals μ *whatever* N is (**B5**: internal holds, fidelity accurate). Adding drift changes *which* mutations survive but not the expected per-lineage rate. So Paul's model gives the critics' answer, about 6 My for 1.2 %, by a route that skips population genetics but lands on the same identity. Under Day's 3.0 inputs (252,000 generations), this neutral rate gives about 1.5×10⁷ substitutions per lineage, against MITTENS' achievable 191: a factor of about 79,000. That gap is the whole dispute, and it sits in branch B, not branch A.
- **E3 cuts both ways.** Day's fill-state objection bites only if the pipeline starts empty at the split. In the audit's B1 simulation, an equilibrium start matched U·T (RESULTS B1, P2). A later independent fwdpy11 replication did not reproduce those counts: it found a 21 % equilibrium deficit and could not locate the cause. B1c is still open. Paul's zero-transit idealisation is the limit of a pipeline that was already full at the split, and that is the standard assumption. Even with the replication's 21 % deficit, the shortfall would be nowhere near the 10⁵-fold one.
- **Against the "rate equation" framing, the point is valid.** If anyone (Duffy included) treats MITTENS as a rate of *change* driven by copying errors, Paul shows that mutation supply is far from limiting (120 per generation against 1 per 1,322 generations). Day's G_f is an *adaptive* fixation rate from a clonal bacterium (**A2e**, **A5f**: external `supported` that clonal and recombining rates differ), and it is not a ceiling on neutral divergence.
- **Paul is candid about his limits.** He lists every omitted mechanism and says population genetics is needed for the real answer. That is honest scoping, not a hidden flaw, and E4 is partly a reading of a claim he hedged ("If so").

## 6. Bottom line

The maths is correct: it is textbook Jukes–Cantor, and his numbers reproduce. The error, from Day's side, is that the model contains **no fixation**, so it cannot speak to MITTENS, which is a fixation-count argument. It also **assumes zero fixation transit time**, which is exactly what Day disputes. The strong conclusion ("the opposite of what it should have been") is a non-sequitur against Day's actual equation, which Paul says he never read. From the critics' side, the result still lands on the standard 2μt divergence that Day accepts at steady state. So the post adds nothing new to the dispute: it restates branch B (k = μ, and whether the pipeline was full at the split) through a no-drift model.

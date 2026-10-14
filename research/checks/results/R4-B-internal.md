# R4 B internal: readings, per-reading N2b derivations and the proposed field comment (fix pass 2, O5, D-21, D-24)

Status: **fix pass 2, 2026-10-14** (Paperclip EVO-80, analyst), on fix pass 1 (EVO-70, 54adad7). The field `verdicts.internal` of claim B **stays `pending`**. It may move only after the bounded fresh-reviewer check of B-R19 returns without a BLOCKER; if that check returns a BLOCKER, the field stays `pending` and the question goes to the owner. This file carries what the move would use: the Readings table, one N2b derivation per reading, and the proposed field comment.

- Reviews answered: `research/checks/REVIEW-R4-B-internal-correctness-2.md` (124ce23), `-steelman-day.md` (f5104a4), `-steelman-critic.md` (f66ce55) in fix pass 1; the D-24 fresh-reviewer check `REVIEW-R4-B-internal-ruling-check.md` (ccdb989) in fix pass 2 ("Review resolution 2").
- Binding rulings: `research/checks/briefs/O5-reviews-reviewer.md`. Addendum Part 1 (35b196a): B-R1, B-R2, B-R3, B-R6, B-R7 (its aggregation sentence only as a proposal, B-R17) and B-R10 stand. Addendum 2 (9f863fd): B-R11 to B-R19 govern. **B-R4 is withdrawn** (B-R11). **B-R5 is superseded as a governing ruling**; its value under C survives on B-R15's basis. B-R8 does not arise (B-R18). B-R9's first overturn condition is met (B-R13). I have not departed from any ruling.
- Prior write-ups this rests on: `R4-B2.md` (Rule N), `R4-RHclose.md` Part 2 and its review resolution. This file adds no registered prediction and changes none.
- **Source text.** `sources/raw/b-steelday-2026-10-13/hl.txt` (gitignored; fetched by the Day-side reviewer from Zenodo 22129121). Its sha256 is `3182a5b6cd3a8ac822017d6d7f509c234ab147b334546d62f88623142d9dbfe2`, the hash of the audit's local text `sources/raw/day/zenodo-22129121.txt`. So **"HL l.N" below is the line numbering the claim file and `quotes-day.md` use.** PDF sha256 `66aa8be6…55719bf` (matches `bib-day.md`). Every quote below was checked against it with `sed` on 2026-10-14 (fix pass 2 re-read l.96-100, l.133-135, l.247-253, l.287-291, l.302, l.326-331, l.343-366, l.416-419, l.428-441, l.453-461).
- **Numbers.** Kimura (1955) series for an empty start, F(x) = 1 + Σ(−1)^i(2i+1)e^{−i(i+1)x/4}, D(x) = (1/x)∫₀ˣF, x = T/(g N_e), N_e = 4·1e5/7 = 57,143, g = 25 y unless stated. Local check of under a second (stdlib, `research/.venv/bin/python -I -c`, not committed): F 0.69703 / 0.67594 / 0.02547 / 0.28077 / 0.44703 (g 20) / 0.18686 (g 29) / 0.01749, D 0.25564 / 0.24196 / 0.00337 / 0.06487 / 0.12497 / 0.03790 / 0.00218. **Fix pass 2, re-checked the same way:** F(4.00) = 0.60634 (HL's criterion boundary 4Nₑ = G, first computed in the ruling check); HL's ceiling X = (Vₖ+2)G/16 at Vₖ 5 is 113,750 at 6.5 My, 110,250 at 6.3 My, 35,000 at 2 My. **Post hoc and new in this file:** the shortfall factors 1/F and 1/D in section 3b, x for the 1e5 and Yoo rows, and 1e5/X = 0.88 (trivial divisions of recorded values).

## 1. What is scored, and on which quote (B-R2; B-R7 aggregation sentence as a proposal, B-R17)

**Proposed aggregation rule (B-R7 text; under O-6, not a rule; B-R17, answering ruling-check NOTE-6 and correctness NOTE-12).** *Proposal:* "an internal field takes the governing reading of the Statement quote that asserts the node's own claim; the node's other Statement quotes are reported with their own verdicts." This is new rule text. It goes through O-6 (written proposal, 24-hour cooling-off, re-score of any load-bearing verdict it moves) and may not be applied anywhere until that has run. **Nothing in this file depends on it**: of B's three Statement quotes, quote 1 carries no verdict (rhetoric, RH2) and quote 2's verdict is B2's, so Q157 is the only quote that carries a B-level internal verdict, and every reading in play is a reading of Q157.

| Statement quote | Status | Tag | Internal | Ground |
|---|---|---|---|---|
| 1. Blog 2026-02-04 ¶60, both sentences ("There is absolutely nothing … The one is far too weak … and the second is flat-out wrong") | Statement | rhetoric (RH-10; the second sentence to be added to RH-10, B-R7) | **no verdict** (RH2) | Excluded on **RH2**, not SC (correctness MINOR-9). SC would score a dialectic slip "on the version quoted". "Revised in HL" (HL l.425-428, Q155) stays as a versions note. Day-side F3 alternative, recorded: if the second sentence were dialectic it would be scored on its Feb basis (Q39 → B3a, internal `holds (algebra)`, fidelity `misread`, external `contradicted`, retracted in B3g). |
| 2. HL abstract, "The domain of k = μ is confined to demographic conditions that no non-endangered species is capable of meeting." (HL l.25-27) | Statement | dialectic | `holds` **at B2**, not re-scored here | This is B2's own quote. Copying B2's verdict into the parent would score a narrower claim than B's (critic MINOR-4). |
| 3. Q157, HL l.453-456 | **Statement quote by lead ruling B-R2, 2026-10-13** (was "Candidate") | reading-dependent (section 2) | **sets the field** | The only Statement quote that carries a B-level internal verdict (quotes 1 and 2 above). Its governing reading is S_L (B-R13). |
| Q158, HL l.464-467 ("the pipe was nearly empty") | **not** a Statement quote (B-R2, which stands) | n/a | cannot set the field | Context only. No verdict in this file is set from its wording. B-R2's refusal of Q158 is **not** a ground for anything about S_L, which does not rest on Q158 (B-R16, MINOR-4). |

Q157 verbatim (HL l.453-456): "And now the neutral channel closes on the same window for an entirely independent reason. The adaptive substitutions cannot be paid for; the neutral substitutions cannot be finished, because the pipe that would finish them never fills. Both the priced channel and the free channel shut inside the same lineage duration."

It runs on without a break (l.456-461): "It requires no charge against Kimura's algebra. … It takes Kimura's own fixation time, Wright's own effective size, and the field's own census, generation, and reproductive-variance figures, and it asks the one question a century of citing these numbers somehow never forced into the open: how long is the pipe."

**Literal band on Q157's own words (B-R2; correctness MAJOR-3).** `R4-RHclose.md` l.70 registered one band, F ≤ 0.10, for the pooled phrase "never fills / nearly empty". Here it is applied to "never fills" alone. Under the **degree sense** of "fills", "never fills" claims at most a negligible fill, a claim at least as strong as "nearly empty". A band of F ≤ 0.10 (3x edge 0.30) is therefore no stricter on Q157 than on Q158, and it errs in Day's favour if anything. Under **S_L**, F ≈ 0 and the clause is inside the band. Under the **completion sense** (row C) the band is replaced by HL's own operational test for filling, 4Nₑ < G (l.97-98): "never fills" is true where 4Nₑ ≥ G (x ≤ 4) and false where 4Nₑ < G (B-R15).

## 2. Readings table (replaces claim file l.78-85 at integration)

Window 6.5 My (HL's "lineage duration", l.247-249) unless stated; HL's own variance N_e 57,143 unless stated; x = G/Nₑ, so HL's fill criterion 4Nₑ < G is x > 4. "Governing" = sets the field under D-15/RD and B-R13. **The governing `holds` is never shown bare: its scope travels with it (B-R14).**

| # | Reading of Q157 | Value | Tag | N2b derivation (section 3) | Verdict | Governing? |
|---|---|---|---|---|---|---|
| **S_L** | **Census over the lineage duration:** at the current census the neutral pipe cannot fill inside HL's lineage duration, G = 6.5 My / g (HL's own use of the term: l.97-98, l.133-135, l.247-253; inputs named in Q157's own paragraph, l.458-461) | census Nₑ/G ≈ 1.8e4 to 2.8e4 (ruling check, post hoc), F ≈ 0; HL's own form: "eight billion strong … seventy-two thousand times over the enlarged ceiling" X ≈ 114,000 (l.250-252) | dialectic | **derived**: SL1-SL5 | **`holds`, scoped to the census ceiling at G = the lineage duration (B2's content)**. B's title claim over the lineage is asserted by no governing reading: RH3 "no dialectical support offered" (B-R14) | **yes** (B-R13) |
| C | **Completion, lineage-actual:** "never fills" = the lineage's pipe never reaches the k = μ steady state ("filled across its support", l.432), tested by HL's own criterion 4Nₑ < G (l.97-98) | 6.5 My: x 4.55 > 4, census 1e5 < X 113,750, so the pipe **fills** by HL's criterion (F 0.697 against F(4) 0.606); 6.3 My: x 4.41, 1e5 < X 110,250, **fills**; 2 My: x 1.40, does not fill (F 0.025) | dialectic (B-R1) | **derived**: C0-C4 | **non-sequitur**: N2b on the clause at 6.5 and 6.3 My (HL l.97-98, l.250, l.437-438) and on the inference (N2a supporting) (B-R15) | no (B-R13) |
| F | Degree: end-of-window flux F at HL's lineage duration | 0.697, **2.32x** the 0.30 edge (6.3 My: 0.676, 2.25x) | rhetoric (RH6) | not needed; rhetoric is not literal-fact-checked (RH2) | **n/a** (core at B2 `holds`; lineage conclusion: "no dialectical support offered", RH3) (B-R6) | no |
| 2My | Degree, on H8's 2 My window (HL l.416 calls it "the entire lineage") | F 0.025 (D 0.003); x 1.40 < 4, so under C's criterion the clause is true here | dialectic | **derived**: the excluded premise is the **window**. HL l.252-253: "The objection is valid, the correction triples the ceiling", adopting 6.5 My (l.247-249), which is the defined term Q157 uses. HL's own contrary usage is recorded: l.416-417, "the one that reached thirty-five percent fill across two million years even when granted the entire lineage". That ambiguity is HL's, not the audit's (critic NOTE-10). | non-sequitur | **no**: needs a window its source gave up (B-R3) |
| D | Delivered share (1/T)∫F as the measure of "fills" | 0.256 (6.3 My 0.242) | dialectic (inside the 3x edge) | **N2b not shown.** No cited HL text says more than 30% of μT was delivered. HL fixes "fill" as F (l.361: "The exponent also fixes what the 'fill' means"), so D is a **different object**: an extended reading under RD l.202. Its measure is a **cross-document measure (Q34, Z22903977, 2026-09-22)**, from a later paper. | no verdict derived (Day-side F1: at most a ledgered overstatement under R1; critic side: non-sequitur via partial-load texts, not shown for the empty-start D) | **no** (extended, cross-document) |
| 1e5 | Takahata N_e = 1e5 held for the whole lineage | F 0.281 at g 25; **0.447 at g 20 (1.49x the edge, rhetoric); 0.187 at g 29**; x 2.6 < 4 | dialectic at g 25 and 29, rhetoric at g 20 | **N2b not shown.** External input: "Takahata" does not occur in HL (grep count 0). HL argues for the variance N_e (l.101-118). | none derived | **no** (external input, N1) |
| Yoo | Yoo HCB ancestral N_e 1.98e5 held (a pre-split N_e) | F 0.0175, D 0.0022; x 1.31 < 4 | dialectic | **N2b not shown.** External input, not HL's. | none derived | **no** (external input, N1) |
| fieldNe | Sourced field N_e, R4-RHclose rows (b)-(d): 1e4, 1.62e4, Takahata two-epoch | F ≥ 0.999, D 0.74-0.85 | rhetoric (degree sense); under C the clause is false at these inputs | not an internal question: whether HL's premise N_e is right is N1, external (B1c, B4a) | n/a (internal) | **no** (external inputs) |
| S | Current size ("near end"), a reading of **Q158's** framing, restating B2 | n/a | dialectic | derivation as a reading of Q158: it restates B2, which HL keeps (abstract l.24-27; l.353-354, "The channel is not slow, it is empty") | `holds`, scoped to B2 | **no**: Q158 is not a B Statement quote (B-R2). The reading of **Q157** with this content is S_L, above. (Fix pass 1's ground here, that the reading drops the defined term, was B-R4's and is withdrawn, B-R11.) |

Considered and **not admitted** as a plausible reading, kept for the record (NOTE-5):

| # | Reading of Q157 | Value | Tag | Inference | Verdict | Status |
|---|---|---|---|---|---|---|
| C′ | Completion, weak inference: "cannot be finished" = not all of μT completes; "closes / shut" = falls below k = μ | as C | dialectic | the inference would follow from F < 1 and HL's own k(T) = μ·F(T) | would **not** be `holds` at 6.5 or 6.3 My: on HL's criterion its clause is false there (NOTE-5) | judged implausible on HL's own usage (C2), and weaker than fix pass 1 thought. The B-R9 overturn is met by S_L, not by C′ (B-R13). |

## 3. N2b derivations for the governing reading S_L and for C (B-R3, B-R11 to B-R16)

### 3a. S_L (governing)

**SL1. The term "lineage duration" is HL's, and HL applies it to the census (B-R11).**
- l.97-98: the criterion is "4 Nₑ < G where G is the number of generations the lineage has been available, its duration in years divided by the generation time".
- l.134-135: "Above the census X, a population is too large for a neutral allele to cross it by drift in the time its lineage has existed."
- l.247-253 is the only place HL introduces and applies "lineage duration", and it applies it to the census against the ceiling: "Use the lineage duration, the full continuous ancestry, which in the case of the human lineage is roughly six and a half million years … The human ceiling rises accordingly, from thirty-five thousand to about one hundred fourteen thousand. And then note that we are still eight billion strong, which puts us seventy-two thousand times over the enlarged ceiling. The objection is valid, the correction triples the ceiling, and the conclusion is not changed."

S_L keeps Q157's "inside the same lineage duration" in exactly that sense. It does not drop it.

**SL2. S_L is not an extended reading (B-R12).** RD l.202 bars "a different object, or a wider claim" from setting the field.
- *Not wider.* S_L restricts the substitutions in question to those seeded at the current census. It claims less than C.
- *Not a different object.* Q157's own paragraph names S_L's inputs (l.458-461, quoted in section 1): census, generation and reproductive-variance figures are the inputs of X = (Vₖ+2)G/16 (l.126-135) and of the census comparison. They are not the inputs of C.
- *Not resting on Q158.* B-R2's bar on setting a verdict from Q158's wording is not engaged (MINOR-4).

**SL3. The clause is true.** At the census scale Nₑ/G is about 1.8e4 to 2.8e4 (HL Table 3 l.318, G = 2.6e5; ruling check, post hoc), so F ≈ exp(−π²Nₑ/G) ≈ 0. HL's own form: the census is "seventy-two thousand times over the enlarged ceiling" (l.251-252). "Never fills" is literal, inside the registered band.

**SL4. The inference follows on HL's text.** HL's closure words are used of the census regime: l.353-354, "So the neutral substitutions these species exhibit today are not being seeded at their current size at all. The channel is not slow, it is empty." The sentence follows directly on the modern-human census computation (l.329-352) and is extended to mice and fruit flies at l.356-360. HL never calls the lineage pipe empty: it calls it "a partly-loaded pipe" (l.366) and "a partly-filled pipe inherited from a lower-census past" (l.419).

**SL5. No exclusion; verdict.** HL's partial-load concessions (l.355-360, l.417-419, l.439-441) concern "the very small populations these species used to be" (l.359-360), not the census, so none excludes S_L's premise. No N2b. **`holds`**, under the four conditions of B-R14, all carried into the proposed comment (section 4):
- scoped to the census ceiling at G = the lineage duration, which is B2's content; the scope travels into every table, tally and board row (see 6g: the field comment alone does not do this);
- S_L is a counterfactual about a census held for "the four hundred generations of the current-census era" (l.329-330). It says nothing on whether drift produced the observed human–chimpanzee divergence;
- B's title claim, that neutral theory cannot rescue the shortfall over the lineage, is asserted by no governing reading: RH3, "no dialectical support offered";
- HL's own drainage concession stays beside it, l.354-356: "The small number of fixations we observe are just drainage: the completions of mutations that entered the pipe long ago, when the populations were small and their pipes short enough to fill."

What this costs, as the lead recorded it (B-R13): it is a **Day-favourable** move on a load-bearing internal field, from the superseded `non-sequitur` to `holds`, on the charity rule the owner approved on 2026-10-11. Here it is a proposal; the field does not move in this pass.

### 3b. C (lineage-actual, completion sense; not governing)

**C0. The sense of "fills", and HL's own test for it (B-R15).** HL uses "fill" in the completion sense in its own statement of the argument: l.271, "The correct interpretation is narrower: the pipeline cannot fill"; l.274-276, "A population reaches the k = μ flux only after it has spent enough time to load every one of its pipes from empty … not 'what is the delivery rate of a full pipe' but 'is this pipe full'"; l.432, "k = μ holds only once the fixation-time distribution has filled across its support". HL also uses the degree sense (l.363, "the pipe substantially fills"; l.416, "thirty-five percent fill"). Both are HL's; C is not an import. HL's **operational** test for filling is 4Nₑ < G (l.97-98), the boundary x = 4, where F(4) = 0.606. HL says of the region below its ceiling that "fixation can, at least in theory, potentially complete" (l.135-136), and that "the only census population that fills the pipe in time is one too small to sustain a viable species" (l.437-438). An asymptotic reading (fills only at F = 1) would make every population of every size "never fill"; l.437-438 says some census fills, so that is not HL's sense. Fix pass 1's threshold of "between 0.70 and 0.999" had no anchor in HL and is withdrawn.

**C1. The clause is false in the governing window on HL's own criterion.** At HL's lineage inputs the hominid census 1e5 is **below** HL's own X: 113,750 at 6.5 My (HL l.250: "about one hundred fourteen thousand"), 110,250 at 6.3 My; x 4.55 and 4.41 > 4. By HL's criterion that pipe fills, so "never fills" is contradicted by HL l.97-98, l.250 and l.437-438. Under C the clause is true only at 2 My (x 1.40), Takahata 1e5 (x 2.6) and Yoo (x 1.31), which are all non-governing rows.

**C2. What "closed / shut" means in HL's own sentence pair.** Q157 asserts that both channels "shut" in parallel. The paragraph immediately before defines what "closed" means for the first channel, HL l.445-448: "The adaptive channel … was already closed by Haldane's dilemma …: selection can provide only an insignificant trickle of adaptive substitutions over many generation, orders of magnitude short of what the functional genome requires." HL's own vocabulary also opposes "empty" to "slow": l.354, "The channel is not slow, it is empty"; l.209, "The window is not narrow. It is empty." So the conclusion needs the premise **P\*: the neutral channel, partly filled, delivers an insignificant trickle, orders of magnitude short of k = μ.**

**C3. HL's own text excludes P\* at HL's own inputs and window (MINOR-3).**
- HL's own model, l.287-291: "k(T) = μ · F(T) … Before then, k is μ cut down by however little of the distribution has yet come due." At HL's own N_e and its accepted 6.5 My, k(T) = 0.697 μ at the end of the window, a shortfall of **1.43x** (post hoc). The delivered share is 0.256, a shortfall of **3.9x** (post hoc). At 6.3 My the figures are 1.48x and 4.1x. Neither is "orders of magnitude". (This is also N2a: HL's own equation gives another value.)
- l.362-363: "When Nₑ is of the same order as T — when a lineage sits near its own X — the exponent is order one: the pipe substantially fills, and Kimura's rate is approached." At 6.5 My the hominid census sits at 0.88 X (post hoc).
- l.419: "a partly-filled pipe inherited from a lower-census past"; l.439-441 (Q156): "reading a rate that was loaded, at least partially, under population conditions that ended in the Holocene".
- *A fortiori only:* l.363-366 (Q153), "even the generous linear bound T/4Nₑ stands at about thirty-five percent — a partly-loaded pipe", is HL's linear bound over "the full two million years". HL itself calls that bound "an overstatement, and a vast one" (l.302), and HL's exact law gives F 0.025 there. It is not part of the basis.
- l.355-356 (Q151) supplies the mechanism of a partly loaded pipe ("drainage: the completions of mutations that entered the pipe long ago"); its context is the census computation and mice and fruit flies (l.353-360), so it is cited for the mechanism, not for the human lineage.
- l.268-270: "'Nothing finishes in the species lifetime' is simply wrong as a claim about throughput, and the drift limit does not depend on it." HL itself separates "finishing" from "filling". Q157's "cannot be finished, because … never fills" puts back the link HL set aside.

**C4. Verdict on C.** **`non-sequitur`**, on two grounds (B-R15): the clause is contradicted at 6.5 and 6.3 My by HL's own criterion and ceiling (C1), and the inference needs P\*, which HL's own equation and text exclude (C3): N2b within HL, N2a supporting (critic MAJOR-1's N2d is not needed). Shortfalls of orders of magnitude appear only on non-governing readings: 2 My (D 297x short) and Yoo (459x). Takahata 1e5 is 15x short on D, about one order. C is recorded, not governing.

The old basis, the pooled "nearly empty" band with one R4-B2 derivation carried to four rows, does not survive the reviews and is not restated here. Neither is fix pass 1's basis for C (that the clause is true and only the inference fails), which MAJOR-2 showed false at 6.5 and 6.3 My.

## 4. Proposed field comment (for integration only, after the B-R19 check returns no BLOCKER)

```yaml
  internal: holds   # SCOPED, NEVER BARE (B-R14): holds ONLY for the census ceiling at G = the lineage duration (B2's content). B's title claim (neutral theory cannot rescue the shortfall over the lineage) is asserted by NO governing reading -> 'no dialectical support offered' (RH3). Reading-dependent: set on Q157 (B Statement quote by lead ruling B-R2, 2026-10-13) under its governing reading S_L (D-15/RD; B-R11..B-R13): at the current census the neutral pipe cannot fill inside HL's lineage duration (HL l.97-98, l.133-135, l.247-253; inputs named in Q157's own paragraph l.458-461); census Ne/G ~2e4, F ~0 (HL: 'seventy-two thousand times over the enlarged ceiling', l.251-252) -> dialectic -> holds; inference on HL's own closure words for the census regime, 'The channel is not slow, it is empty' (l.354). S_L is a counterfactual about a census held ~400 generations (l.329-330) and says nothing on whether drift produced the observed divergence; HL's own concession beside it: 'The small number of fixations we observe are just drainage: the completions of mutations that entered the pipe long ago' (l.354-356). Other readings (R4-B-internal.md section 2), not governing: C (lineage-actual completion sense, HL's test 4Ne < G) -> non-sequitur: clause false at 6.5 and 6.3 My (census 1e5 < X 113,750 / 110,250; x 4.55 / 4.41 > 4; l.97-98, l.437-438) and inference excluded by HL's k(T) = mu F(T) (0.70 mu, l.287-291), l.362-363, l.419, l.439-441; 2 My window F 0.025 -> non-sequitur (needs the window HL gave up, l.252; HL's l.416 'entire lineage' recorded); F degree sense 0.697 (2.32x the 0.30 edge) rhetoric -> n/a (B-R6); D 0.256 (cross-document measure, Q34), Takahata 1e5 (F 0.281; 0.447 at g 20, 0.187 at g 29), Yoo 1.98e5 (0.0175): N2b not shown (extended / external, N1); S (Q158 'near end') holds scoped to B2, Q158 not a Statement quote (B-R2). Quote 1 rhetoric (RH2, RH-10): no verdict; quote 2 is B2's (holds at B2). Stated openly (B-R10): the cleanest internal contradiction on the degree sense is on reading F, which RH6 tags rhetoric and so releases (correctness NOTE-11); and N2b penalises an author for his own concessions: drainage, partial load, 'substantially fills' (critic NOTE-9). Basis: lead rulings B-R1..B-R3, B-R6, B-R10 (35b196a) and B-R11..B-R18 (9f863fd); B-R4 withdrawn, B-R5 superseded; bounded check B-R19 <commit>.
```

Until then the field reads `pending` with the D-21 comment. The superseded comment (claim l.12) has no source to restate: its "D, 1e5, S and 2 My ... -> non-sequitur" mapping and its "recorded alongside: ... holds" do not survive (B-R3, B-R6). Keep it only as a dated superseded line. Because `lint_research.py` drops YAML comments (6g), this comment alone does **not** meet B-R14's "the scope travels with it into every table, tally and board row".

## 5. Points for the bounded B-R19 check (its two questions only)

Fix pass 1's P1-P3 were answered by the ruling check: P1 (C′) by NOTE-5, P2 (agreement with B-R4) by BLOCKER-1, P3 (B-R8) by NOTE-7. They are not restated.

- **(a) Is S_L wrongly admitted (is B-R12 wrong)?** The strongest case against, which neither the lead nor I can answer away, is the ruling check's BLOCKER-1 (v): the two-channel frame. Q157 says the neutral channel "closes on the **same window**" as the adaptive one, and the adaptive argument concerns the lineage's actual divergence (l.388-389: species-wide fixation "is … what the human–chimpanzee differences must account for in their entirety"; l.444, "the two channels by which a genome is supposed to change"). On that frame "the neutral substitutions" are the lineage's actual ones, and S_L narrows them. The ruling check judged that this makes C plausible but does not make S_L implausible, because l.247-253 is HL's own S_L computation, offered as settling the lineage objection, and because HL's closure words fit S_L and not C. One point I add from re-reading the text: the closure sentence at l.353-354 follows directly on the modern-human census computation (l.329-352), so it covers the human census, not only the mice and flies of l.356-360. That supports SL4. I add no argument beyond these.
- **(b) Does B-R14's scoping stop a bare `holds` travelling?** Not by the field comment alone. `research/checks/lint_research.py` l.32 reads claim frontmatter with `yaml.safe_load`, which discards comments, and `lint_research.py --write-hierarchy` writes `hierarchy.yaml`, which `argmap_render.py` (l.337) and the board read. The value `holds` would therefore reach every generated table as bare. The A2e ruling check (3840bee) found the same defect for a certainty qualifier ("the qualifier sits in a YAML comment no tally reads"). Proposal 6g asks for a carrying mechanism before the move. I do not choose one: a schema or tool change may be rule text under O-6.

## Who this helps

- **Day side.** This credit is as prominent as the critic side's.
  - The governing reading of Q157 is the one HL itself uses for its defined term, and under it **Q157 is true and its inference follows**: the census cannot fill the neutral pipe inside the lineage duration, 72,000 times over the ceiling on HL's own figures (`holds`, scoped). This is the Day-side steelman's F2 outcome, reached by a reading that keeps "lineage duration" (S_L) rather than by "near end" (Q158).
  - B2 `holds`. Day's mechanics stand: k(T) = μF(T) < μ from any start that is not full.
  - Under C the clause **is** literally true at 2 My, Takahata 1e5 and Yoo (x < 4), though those rows do not govern.
  - The old basis, "nearly empty" scored as near-literal on four readings, is withdrawn as underived. Three of the four rows the superseded comment listed (D, 1e5, S) now carry **no** non-sequitur.
  - Day's later text (B1d, blog 2026-10-01) grants a full CHLCA pipe (critic NOTE-7). That is cross-document and moves nothing here, but it shows the empty-start premise is not one Day holds.
- **Critic side.**
  - B's own title claim, that neutral theory cannot rescue the shortfall **over the lineage**, is asserted by **no** governing reading: RH3, "no dialectical support offered". The `holds` is about a census the lineage has held for about 400 generations (l.329-330) and must never be shown bare.
  - Under the lineage-actual reading (C) the non-sequitur is **stronger** than fix pass 1 said: HL's own criterion 4Nₑ < G says the hominid pipe at a census of 1e5 **fills** at 6.5 My, so "never fills" is false there, and HL's own k(T) = μF(T) excludes "closes / shut".
  - HL's own drainage concession stands beside the value (l.354-356). Whether partial delivery suffices for the observed divergence is external and pending (B1c, B4a); the error, and the `holds`, are both narrow (critic NOTE-8).
- **Both / the audit's own errors.**
  - **Lead (B-R4, withdrawn by B-R11):** a ruling built on a reviewer's concession (Day-side cost item 3) instead of HL's own definitions of "lineage duration" (l.97-98, l.133-135, l.247-253). The record already held the version of S it needed to answer (correctness BLOCKER-1, l.38).
  - **Fix pass 1 (this file, 54adad7), mine:**
    - P2 endorsed B-R4 and repeated the cost-item-3 concession without checking HL's definitions. The analyst should have caught the lead's error and did not.
    - Row C, C0, C1 and "Who this helps" asserted, and the proposed field comment repeated, that the clause was true in every window. HL's own test 4Nₑ < G, which fix pass 1 did not apply, makes that false at 6.5 and 6.3 My (MAJOR-2). Withdrawn throughout.
    - C0 set a post hoc threshold ("between 0.70 and 0.999") with no anchor in HL. Withdrawn.
    - C3 used HL's disowned 2 My linear bound (l.363-366) as hominid evidence at 6.5 My (MINOR-3). Now a fortiori only.
    - Section 1 stated the B-R7 aggregation sentence as a rule (NOTE-6). Now a proposal under O-6.
    - Row S's "not governing" rested on B-R4's withdrawn ground.
  - **Earlier, recorded in fix pass 1:**
    - One N2b derivation, written for one reading in R4-B2, was carried to four readings (all three reviews).
    - S was given "non-sequitur at lineage level" with no derivation, against the registration's own `rhclose.py` l.83-84 (correctness BLOCKER-1).
    - The field rested on a "Candidate" quote, read through a quote outside the Statement (correctness MAJOR-3).
    - Wrong numbers: "0.697, 2.25x" should be 2.32x; F at 2 My "0.026" should be 0.025 (double rounding).
    - Quote 1 was excluded on SC instead of RH2.
    - The D-21 question mis-signed B's direction. The lead has already corrected this in `DECISIONS.md` l.106.

## Review resolution (fix pass, 2026-10-14)

No verdict value changes. Everything below that touches a shared file is a **proposal for integration** (section 6). *Fix pass 2 note:* the entries marked **[superseded, resolution 2]** applied B-R4 or B-R5 and no longer state the governing position; they are kept as the dated record.

### Correctness review 2 (`REVIEW-R4-B-internal-correctness-2.md`)
- **BLOCKER-1** (S mapped to non-sequitur with no derivation). **Accepted in part, under B-R4.**
  - Done, following the reviewer's option (b): S is mapped to `holds`, scoped to B2, and "non-sequitur at lineage level" is removed.
  - Not accepted: the reviewer's ranking of S "at or near the top" under D-15. Per B-R4, S reads Q158's framing, not Q157's sentence, so it is not a candidate for Q157's field. The D-15 ranking is recorded in section 2: C governs, and S, 2 My, D, 1e5 and Yoo do not, each with its reason. **[superseded, resolution 2: the reviewer's S_L version (l.38) governs under B-R13; the reviewer's ranking stands in that form.]**
  - Why the RHclose fix pass admitted S: as a reading of the pooled Q157/Q158 phrase, before B-R2 separated the quotes.
- **MAJOR-2** (one N2b derivation carried to four readings). **Accepted.** Section 2 gives each row its own derivation or "N2b not shown":
  - C: section 3.
  - 2 My: the window premise.
  - D, 1e5 and Yoo: N2b not shown. The reviewer is right that Q140, Q151, Q152 and Q156 do not exclude an empty start for the human lineage.
  - C does not need that exclusion. It needs only P\* ("closed" = orders of magnitude short) to be excluded, and HL's own k(T) = μF(T) and l.363-366 do that. **[superseded in part, resolution 2: l.363-366 is a fortiori only (MINOR-3).]**
- **MAJOR-3** (Candidate Statement; Q158 outside the Statement). **Accepted.**
  - Q157 is adopted by B-R2 (2026-10-13). Q158 is not adopted, and no verdict is set from its wording.
  - The band is applied to Q157's own words, justified in section 1.
  - Claim l.29 and l.32: proposal 6a.
- **MINOR-4** (completion reading missing). **Accepted.** Row C added, and it governs (B-R1, B-R5). **[superseded, resolution 2: C is recorded, not governing (B-R13).]** The reviewer's N2a test against HL's own F (0.70, "substantially fills") is used in C3.
- **MINOR-5** (2 My: wrong excluded premise). **Accepted.** The premise is now the window (l.247-253). HL's contrary l.416-417 is quoted in the row.
- **MINOR-6** (D and 1e5 status). **Accepted.** D is extended (a different object, l.361) and cross-document (Q34). 1e5 is an external input (N1) and not governing. Its g sensitivity is recorded: F 0.447 at g 20 (rhetoric), 0.187 at g 29.
- **MINOR-7** (rows missing). **Accepted.** Yoo and the field-N_e rows are added.
- **MINOR-8** (2.32x). **Accepted.** Proposal 6e.
- **MINOR-9** (quote 1 on SC). **Accepted.** The ground is RH2. RH-10 is to cover the second sentence, with "revised in HL" kept as a versions note: proposals 6b and 6c.
- **MINOR-10** (D-21 direction). **Accepted. Already done by the lead** (`DECISIONS.md` l.106; brief Part 3). No action here.
- NOTE-11 is in the field comment (B-R10). NOTE-12: the aggregation rule is stated in section 1 **[superseded, resolution 2: as a proposal under O-6 (B-R17)]**. NOTE-13 (HL l.448-452, "The two arguments do not overlap") is recorded; it bears on B's title, not on the field. NOTE-14: 0.025, proposal 6e.

### Steelman, Day side (`REVIEW-R4-B-internal-steelman-day.md`)
- **F1 BLOCKER** (non-sequitur derived once, asserted four times). **Accepted.** Section 2 follows the reviewer's per-reading table, with these differences:
  - S is `holds` but is recorded as a Q158 reading (B-R4). **[superseded in its ground, resolution 2: S stays a Q158 reading because Q158 is not a Statement quote (B-R2); its Q157 counterpart S_L governs.]**
  - D is "N2b not shown". The reviewer's "ledgered overstatement, no flip" is recorded as the Day-side position in the row.
  - C is added, and it governs (B-R5). **[superseded, resolution 2.]**
- **F2 MAJOR** (S governs, giving `holds`). **Not accepted, by ruling B-R4.** **[superseded, resolution 2: accepted in outcome by B-R13 through S_L, which keeps "lineage duration"; not accepted for the "near end" (Q158) version.]**
  - Recorded as the Day side's position: under D-15, S is literally true (it is B2) and best supported, and "lineage level" is a wider claim that RD l.202 bars.
  - The ruling's answer: the lineage-level claim is Q157's own words ("inside the same lineage duration", a defined term). It is not a wider claim added by the scorer. A reading that drops that clause reads a different statement.
  - I agree with the ruling (P2). The fresh reviewer is asked to attack it first (B-R9).
- **F3 MAJOR** (the field turned on a third quote). **Accepted.** Section 1 states that the field rests on Q157 alone, and why S1 and RH3 force that choice (critic MINOR-4 makes the same point).
  - (a) Accepted as proposal 6b: RH-10 is extended to the second sentence.
  - The Day side's "internal on its own Feb basis" is recorded as the dialectic alternative. Under the RH2 tag that B-R7 confirms, quote 1 carries no verdict.
- **F4 MINOR** (Q157 status stated two ways). **Accepted.** Q157 was adopted by lead ruling B-R2 on 2026-10-13 (35b196a). l.29 and l.32 are to be brought into line: proposal 6a.
- **F5 MINOR** (1e5 cannot govern). **Accepted.** The row is kept, marked "not governing (external input, N1)", and removed from the readings said to carry the field.
- F6 is done by the lead (`DECISIONS.md` l.106). F7: a dated pointer line in `R4-RHclose.md` l.117, proposal 6e. The "What this costs Day" items 1-7 are carried in Who this helps and in rows F, 2 My and S.

### Steelman, critic side (`REVIEW-R4-B-internal-steelman-critic.md`)
- **MAJOR-1** (tag keyed to Q158; every reading of Q157 is non-sequitur). **Accepted in part.**
  - Accepted: the completion reading is added and governs (B-R1, B-R5). **[superseded, resolution 2: C recorded, not governing.]** Q157 is scored on its own words. "Recorded alongside: holds" is dropped (B-R6).
  - Not accepted: "non-sequitur on F, D, 1e5, 2 My and the completion reading alike". D, 1e5 and Yoo have N2b not shown (B-R3). F remains a degree-sense reading of **Q157's** "never fills", at 2.32x the edge, so it is rhetoric and gives `n/a` (B-R5, B-R6). It is not moved to Q158.
- **MAJOR-2** (RH3 extracts the wrong core; the core is the lineage closure). **Not accepted, by ruling B-R6.** Under rhetoric the field is `n/a`, with the core at B2 `holds` and the lineage conclusion marked "no dialectical support offered". That is the reviewer's own stated fallback ("or at worst `n/a`").
  - The self-classification evidence (HL l.456-464: "There is no algebra error to defend …") is used in support of the **dialectic** tag of row C (P1 iii), where it does bear.
  - The steelmen conflict here. The lead's ruling is applied, not chosen by me.
- **MINOR-3** (like-for-like with C7: `n/a`). **Accepted** (B-R6).
- **MINOR-4** (answer the lead's suspicion on the record). **Accepted.** Section 1, one line per quote.
- **MINOR-5** (2.32x). **Accepted.**
- **MINOR-6** (D is a later paper's measure). **Accepted.** D is labelled "cross-document measure (Q34, Z22903977)". It is not listed first and does not govern.
- NOTE-7 is in Who this helps (Day side). NOTE-8 is in Who this helps. NOTE-9 is in the field comment (B-R10). NOTE-10 is in the 2 My row. NOTE-11 (quote 1 escapes) is recorded: critics get no internal verdict on "flat-out wrong", and HL's "The identity is not false" (l.430) is a versions entry.

### Steelman conflicts without a ruling
None. Every conflict between the two steelmen falls under B-R4 (S), B-R5 (governing reading) or B-R6 (rhetoric value). **[Fix pass 2: B-R4 and B-R5 are replaced by B-R11 to B-R15; still no conflict without a ruling.]**

## Review resolution 2 (fix pass 2, 2026-10-14): fresh-reviewer ruling check (`REVIEW-R4-B-internal-ruling-check.md`, ccdb989)

No verdict value changes; the field stays `pending` until the B-R19 check returns without a BLOCKER. No reading-dependent count changes (B-R18). Every finding is answered under Addendum 2 (9f863fd).

- **BLOCKER-1** (B-R4's ground false; S_L keeps the defined term and governs under D-15). **Accepted** (B-R11, B-R12, B-R13).
  - Row **S_L** added as a reading of Q157: dialectic, F ≈ 0, derivation SL1-SL5 citing HL l.97-98, l.133-135, l.247-253, l.353-354 and l.456-461, as the fix asked. It governs. Verdict `holds`, scoped to the census ceiling at G = the lineage duration (B2's content), never bare (B-R14).
  - Row S (Q158, "near end") is kept as context, not governing. Its ground is now B-R2 (Q158 not a Statement quote), not B-R4's withdrawn one.
  - The B-R14 conditions are carried into section 2, SL5, the proposed comment (section 4) and proposal 6a: scope stated in every place the value appears; C, 2 My, F, D, 1e5 and Yoo recorded as non-governing with their values; B's title claim takes RH3; HL's drainage concession (l.354-356) beside it.
  - Fix pass 1's P2 (agreement with B-R4) is withdrawn and recorded under the audit's own errors.
  - One new limit on B-R14, found in this pass: the scope cannot travel through a YAML comment (section 5 b; proposal 6g).
- **MAJOR-2** (the every-window clause sentence of fix pass 1 is false at 6.5 and 6.3 My under HL's criterion 4Nₑ < G). **Accepted** (B-R15).
  - The sentence is withdrawn everywhere it appeared: row C (old l.32), C0 (old l.49), C1 (old l.51), Day-side "Who this helps" (old l.83), and the proposed field comment (old l.68), which repeated it.
  - Row C and C0/C1 are restated on HL's criterion: at 6.5 and 6.3 My "never fills" is contradicted by l.97-98, l.250 and l.437-438; at 2 My, 1e5 and Yoo it is true (x < 4).
  - The post hoc threshold 0.70-0.999 is withdrawn (C0). The asymptotic reading is set aside on l.437-438.
  - C's value stays `non-sequitur` on the stronger basis: N2b on the clause and on the inference (C4). "Who this helps" is corrected on both sides.
- **MINOR-3** (hominid "partly-loaded" evidence is HL's disowned 2 My linear bound). **Accepted** (B-R16). C3's basis is now l.287-291, l.362-363, l.419 and l.439-441. l.363-366 is cited only a fortiori, with HL's l.302 ("an overstatement, and a vast one") beside it.
- **MINOR-4** (B-R2 survives but does not carry B-R4). **Accepted** (B-R16). B-R2 is applied as written: Q157 adopted, Q158 refused. It is cited as a ground for row S only. Section 1 and SL2 state that it is not a ground for anything about S_L.
- **NOTE-5** (C′ is not the strongest overturn). **Accepted.** The C′ row records that on HL's criterion its clause is false at 6.5 and 6.3 My, so it would not give `holds` there. The B-R9 overturn is S_L.
- **NOTE-6** (the B-R7 aggregation sentence is a rule). **Accepted** (B-R17). Section 1 states it as a **proposal under O-6** and shows that nothing in B depends on it. It is not applied here or elsewhere.
- **NOTE-7** (B-R8 does not arise). **Accepted** (B-R18). The derived readings are {`holds` (S_L), `non-sequitur` (C, 2 My), `n/a` (F)}, so B stays reading-dependent in value. No count changes. Fix pass 1's P3 is moot. The 7-against-15 board discrepancy stays a separate bookkeeping item.
- **Claim file text** (task: "bring the claim file text into line with B-R13 to B-R18"). This pass does not edit the claim file, which is a shared file for the operator. Proposal 6a gives the replacement text line by line.

## 6. Proposals for integration (operator, one at a time; none applied here)

Revised in fix pass 2 to match B-R13 to B-R18. Nothing below moves the verdict field before the B-R19 check returns without a BLOCKER.

- **6a. Claim file `B-neutral-theory-cannot-rescue.md`.**
  - l.29: replace "**Candidate Statement**; rule RH tag reading-dependent" with "Statement quote (lead ruling B-R2, 2026-10-13, 35b196a); RH tag reading-dependent (governing reading S_L, B-R13, 9f863fd)". Q158 is not added.
  - l.32: replace with "RH tag: quote 1 rhetoric (RH-10, both sentences; RH2, no verdict); quote 2 dialectic (B2's quote, holds at B2); quote 3 (Q157) reading-dependent (RH-26): S_L, C and 2 My dialectic, F rhetoric. B's title claim over the lineage is asserted by no governing reading: 'no dialectical support offered' (RH3, B-R14)."
  - l.78-85: replace the RHclose Readings table with the section 2 table, and the R4 paragraph with: "R4 B internal (`research/checks/results/R4-B-internal.md`, fix pass 2 under lead rulings B-R11..B-R19, 9f863fd): Q157 is scored on its own words. Its governing reading S_L (at the current census the neutral pipe cannot fill inside HL's lineage duration, HL l.97-98, l.247-253) gives `holds`, scoped to the census ceiling at G = the lineage duration (B2's content), never shown bare. It is a counterfactual about a census held ~400 generations (l.329-330); B's title claim over the lineage is asserted by no governing reading (RH3). Under the lineage-actual completion reading C, `non-sequitur`: HL's own test 4Nₑ < G says the hominid pipe at census 1e5 fills at 6.5 My (X 113,750), and HL's k(T) = μF(T) excludes 'closes'. 2 My `non-sequitur`, not governing; F rhetoric `n/a`; D, 1e5, Yoo N2b not shown. HL's drainage concession (l.354-356) stands beside the value."
  - l.12-13: **only after the B-R19 check returns no BLOCKER**, the section 4 comment, with its scope carried as 6g decides. Until then, `pending` with the D-21 comment.
- **6b. `ledgers/slips.md`.**
  - RH-10 (l.69): quote both sentences.
  - RH-26 (l.85) and the l.101 row: the tag is per reading of Q157: S_L dialectic, C dialectic, F rhetoric, 2 My dialectic. D, 1e5 and Yoo are recorded rows with no verdict derived (extended or external). S is a Q158 reading, noted as context.
  - Add, or extend RH-26 with, an RH3 line: B's title claim over the lineage, "no dialectical support offered" (B-R14).
  - The core of the rhetoric reading F stays B2 per B-R6.
- **6c. `ledgers/versions.md` l.33.** Change the ground from "not answerable to HL (N2b) … SC" to "excluded as rhetoric (RH2); revised in HL (versions note)".
- **6d. Argmap.** Day side: Q157 under S_L holds; the census cannot fill the pipe inside the lineage duration on HL's own computation (l.247-253). Critic side: (1) B's title claim is asserted by no governing reading (RH3); (2) under C, HL's own criterion contradicts "never fills" at 6.5 My, and HL's k(T) = μF(T) excludes "closes / shut"; (3) HL's drainage concession (l.354-356). Note the reading dependence. Fix pass 1's Day-side defeater text ("the clause is literally true") is withdrawn.
- **6e. Write-ups, number corrections.**
  - `R4-RHclose.md` l.16, l.79, l.119 and `R4-B2.md` l.37: 0.026 → 0.025. P6 at l.97 is registered wording and stays.
  - `R4-RHclose.md` l.160: "rhetoric (2.32x the edge; 6.3 My: 2.25x)".
  - `R4-RHclose.md` l.117: add a dated pointer: "superseded: D-15 (2026-10-11), D-21 (2026-10-13); see R4-B-internal.md".
- **6f. Counts (B-R18).** No change. B stays reading-dependent in value. The 7-against-15 board discrepancy is a separate bookkeeping item.
- **6g. Scope carriage (B-R14), new in fix pass 2. For the lead and operator; not chosen here.** `lint_research.py` l.32 drops YAML comments, so `hierarchy.yaml`, the argmap render, the README counts and the board would show B internal as a bare `holds`. B-R14 requires the scope in "every table, tally and board row". Before the field moves, the lead needs to decide how the scope is carried, for example a frontmatter key read by the lint and the board, or a scoped display string. A schema or tool change may be new rule text under O-6. The same gap affects the A2e certainty qualifier (3840bee).

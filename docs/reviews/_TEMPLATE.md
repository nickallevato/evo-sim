# Review: "<title>" (<author>, <venue>)

_Not an audit check; no claim file, verdict or count changed._ <!-- D-41: one neutral review per source; both sides at equal depth (hard rule 1) -->

**Source.** <author> (<how the name is known>), [<url without scheme>](<url>), <publication date and where it comes from>, <public / paywalled>, about <N> words. Fetched <YYYY-MM-DD> into gitignored `sources/raw/<dir>/`, `<file>` sha256 `<64 hex>`. Bibliography key `<bib-*.md key>`; source map `docs/research/math/sources/<source-id>.md`. <What is not in the text, e.g. figures as images, and how the review handled it.>

---

## 1. The argument

<Two to four sentences: who the author answers, what question they pose, what they conclude. Every claim below rests on a verbatim quote with a locator from the held text.>

> "<quote>" (<locator>)

<Who the author argues against: the primary text, or a relay (rule U)? Say so with a quote.>

## 2. The maths, located and rebuilt

<The model in one paragraph: its assumptions, what it includes and leaves out.>

| Step | Equation (author's) | Inputs | Library object | Check |
|---|---|---|---|---|
| <name> | <equation as written> | <values with locators or `parameters.yaml` keys> | <M-NNN (record), or "new M-NNN"> | <holds / slip / error, one line> |

**Numbers, recomputed** from the author's inputs only (each one asserted in the record named in the table):
- <number>: <value> (<record>).

<One sentence: does the arithmetic hold? Errors in arithmetic are separate from errors in what the model measures.>

## 3. What holds

<Valid points, from whichever side, as prominently as the errors. Each with its object or quote.>

## 4. What fails

### Errors (rule R1: correcting it moves the stated conclusion by >25% or flips it)
<Each: the statement, the correction, the size of the move. "None found" is a finding.>

### Non-sequiturs and hidden premises (rules N, U)
<Each: premise, conclusion, the missing step; label hidden premises "implicit". Relays are not scored as the author's own claim (rule U).>

## 5. Slips (rules R1, SC; ledger level)

<Wording or number slips that do not move the conclusion, and anything the author corrected in the same source (SC). Ledger level only; this page does not write `ledgers/slips.md`.>

## 6. Rhetoric (rule RH)

| Quote (locator) | Device | Audience | Function | Dialectical core | Better answer (aimed at the move, never at the person) |
|---|---|---|---|---|---|
| "<quote>" (<loc>) | | | | | |

<The same standard applies to rhetoric from Day, critics and allies. Rhetoric changes no verdict.>

## 7. Verdicts under the audit's rule (informal; not entered in any claim file)

| Statement (locator) | Reading | Internal | Fidelity | External | Note |
|---|---|---|---|---|---|
| "<quote>" | <reading 1> | | | | |
| | <reading 2> | | | | |

<Rule RD: where the verdict depends on the reading, list every plausible reading; the field value takes the reading under which the statement is most defensible. Vocabulary: AGENTS.md "Verdict rule".>

## 8. Day-side steelman

<The strongest case the evidence honestly allows for Day's side against or with this source. Same depth and length as §9; cite objects and claim nodes.>

## 9. Critic-side steelman

<The strongest case the evidence honestly allows for the critics' side. Same depth and length as §8.>

## 10. Bottom line

<Three to five sentences: is the maths right, what does it measure, does it touch the claim it targets, what is new to the dispute and what each side may fairly take from it.>

# R4 A2e-fidelity: how the "LTEE as ceiling" passage uses its sources

**Node:** A2e (`docs/research/claims/A2e-ltee-as-ceiling.md`), field `fidelity` (now `pending`). **Brief:** `research/checks/briefs/A2e-analyst-3.md`. **Gap:** A2e. Non-computational: no script, no host, no fetch. **This file proposes a value; it moves no field.**

**Held material used.** MITTENS 3.0 (Z23003785) main text, `sources/raw/vid01-score-2026-10-13/main.txt` (the re-fetch of R4-VID-01-score, gate G0: `main.pdf` sha256 `22bb4ef8…7a37b2` matches the pin in `bib-day.md`, re-checked 2026-11-01; `main.txt` sha256 `0287f54b…dd5b42`). Line numbers below refer to that `main.txt`. Literature quotes only from `docs/research/sources/quotes-literature.md`; status labels from `docs/research/ledgers/fidelity.md`.

## 1. Criterion (committed alone before scoring)

**Pre-registration status: criterion-only.** The analyst read the two Statement paragraphs (s1 lines 62-75; s2 lines 78-149) before writing this section, to list the uses. No use has been scored yet. The expectations at the end are not tests.

**K1. Scope (rule S1).** Scored: the two Statement quotes (Q131, PDF p.2, line 73-74; Q130, PDF p.4, line 147-149) and the premises that their own paragraphs give as the reason for them:
- (a) the s1 list of "conditions maximally favorable to rapid evolution" (lines 69-73);
- (b) the s1 and s2 claim that every mechanism of the "polythesis" is documented in the LTEE (lines 62-68, 102-123), which carries "every tool in its kit";
- (c) the s2 list of "advantages that no sexually reproducing organism possesses" (lines 124-145), which the p.4 sentence draws on with "therefore";
- (d) the derivation chain of the claim file's Formal statement (rate_human <= 1/G_f).

Not scored here: the value of G_f ("Whatever number the LTEE produces" makes A2e independent of it; its sources are scored at A2, A2a, A2b); the s3 data citations (Tenaillon 2016, Good 2017 as data sources: A2 family); numbers in the same sections that feed other nodes (Ara+1 IS rate, the 70-100x hypermutator rate: A5d; LTEE history and dates: no node); s8.2 Ne (Q136); the audit's own `derived:` lines (kappa).

**K2. Status of each use (rule F, verbatim definitions, `R4-X1-verdict-rule.md`).**
- `accurate`: cited and read correctly. `partial`: cited, read with a flagged omission or error. `misread`: the cited source text is in hand and contradicts the reading. `unverifiable`: a numeric input stated as an empirical fact without citation (non-standard), or cited but not retrievable, or a garbled relay. `n/a`: no external input borrowed (own derivation, definition, flagged hypothetical, position statement).
- `partial` is never used for an uncited input. Standard values (rule F list) are exempt. Human Ne about 1e4 is contested-standard: exempt, flagged in the external column.
- **Uncited qualitative premises** (no number, no citation): rule F gives `unverifiable` only to numeric inputs, so these are recorded `n/a` for fidelity; their truth is an internal or external question and is pointed to, not scored here.
- **Cited works not held** (no quote in the quotes files, no local text): `not scored (not held)`, listed in Open. They are not `unverifiable`: rule F's clause is "not retrievable", and nobody has tried.
- **Rule C:** the most charitable reading of each referent is tried and recorded per row. **Rule U:** a relay of another speaker is not scored as Day's own. No use in K1 is a relay on a first read; if one turns out to be, U applies.

**K3. Node value.** The field takes the most severe status among the scored uses that feed the Statement (K1 a-d), in the order `misread` > `partial` > `unverifiable` > `accurate` > `n/a`. This follows the record's practice (A2 `unverifiable` on one unretrieved input; A5f `partial` on one misattribution beside a verified one). Rule F's last clause applies: an `n/a` node whose only cited inputs are `accurate` becomes `accurate`. Rows `not scored (not held)` do not set the value. Where reading one could change it, the value is stated as conditional on them, and they go to Open. If no value is possible without them, the brief's stop rule applies: `unverifiable` only if rule F licenses it on held material, else stop.

**K4. Readings (rule RD).** Two readings of the Statement are set in advance:
- **R-own:** "ceiling" is Day's own inference from the properties he lists (s2: "Every one of these advantages accelerates the fixation process ... The LTEE rate is therefore ..."). The value is K3 over the uses in K1.
- **R-attributed:** "the empirical ceiling" relays an established finding of the LTEE literature. The value is the status of that attribution under K2.

The field takes the reading under which the quoted statement is most defensible (RD), not the one with the best value for Day. The analyst's prior is R-own, because the "therefore" and the advantage list are in the text. The table records both. A scope sensitivity (Statement sentences only, with no premises) is reported beside the readings, but it cannot set the field because K1 fixes the scope.

**Expectations at criterion time (not tests).** A Day-side reader would expect `n/a` or `accurate`: the ceiling is his own argument and its inputs are standard LTEE facts. A critic-side reader would expect `partial` or `misread`: the held LTEE literature (clonal interference) cuts against the framing. The analyst expects `unverifiable` or `n/a`: few uses are cited, and those that are cited are not held.

## 2. The cited and implied uses

What the passage relies on outside Day's own derivation, in text order. The short Day quotes are from the held `main.txt` (line numbers). Only Q130 and Q131 are in the quotes file. A PDF page is given where the line is near a page break.

- **Cited works in the A2e passage: three, all in the s2 mechanism list.** "Clonal interference, ... documented by Gerrish and Lenski (1998)" (l.109-110, p.3); "Epistatic interactions between mutations, documented by Couce et al. (2024)" (l.112, p.3); "the famous citrate-utilizing clade in Ara-3 (Blount et al. 2012)" (l.116-117, p.3). None of the three is in `quotes-literature.md`, `fidelity.md` or `sources/raw/`.
- **Not cited in the A2e passage: Tenaillon 2016 and Good 2017.** Their first citation is in s3 ("3.1 Clone-Pair Analysis (Tenaillon et al. 2016)", l.158), as data sources for the G_f number. That number is outside K1 and is scored at A2, A2a and A2b. The claim file's Primary literature table lists both works for A2e. See section 6.
- **Uncited uses.** The ceiling itself; the other six mechanisms "documented in the LTEE"; Ne ≈ 3 × 10⁷; human Ne 10,000-33,000; 6.64 generations per day; about 25 years per human generation; "effectively unlimited mutation supply"; no recombination overhead; no mate-finding cost; no diploid masking; strong, consistent selection.

## 3. Scoring table

| # | Use (K1 part) | Source cited | Held quote, locator | Status | Rule; charitable reading tried |
|---|---|---|---|---|---|
| U1 | The ceiling: "Whatever number the LTEE produces, it is the empirical ceiling ..." (Q131) and "It is an unattainable ceiling ..." (Q130) | none | Day's own conclusion | `n/a` | F (position statement, own inference). C: read as the conclusion of the s2 "therefore", not as a report of a finding (R-own; R-attributed in section 4) |
| U2 | Six uncited mechanisms "documented in the LTEE" (sweeps, hitchhiking, parallel fixation, compensatory mutation, hypermutation, frequency-dependent selection), l.62-68, 102-117 (b) | none | Context only, no status: Tenaillon2016, "six populations ... had 96.5% of the point mutations, having evolved hypermutable phenotypes" (Results, "Genome evolution"); Good2017, "multiple beneficial variants simultaneously competing for dominance in each population" (Abstract) | `n/a` | K2 uncited qualitative. C: "documented" read as "reported in the LTEE literature". Two of the six match held quotes; four are not checked (truth is external) |
| U3 | Clonal interference "documented by Gerrish and Lenski (1998)", l.109-110 (b) | Gerrish & Lenski 1998 | not held | not scored | K2 not held → Open 1 |
| U4 | Epistasis "documented by Couce et al. (2024)", l.112 (b) | Couce et al. 2024 | not held | not scored | K2 not held → Open 1 |
| U5 | Citrate clade, eco-evolutionary dynamics, "(Blount et al. 2012)", l.116-117 (b) | Blount et al. 2012 | not held | not scored | K2 not held → Open 1 |
| U6 | "Ne ≈ 3 × 10⁷ in the LTEE" (l.136; also l.84-85 and s1 "enormous effective population sizes", l.71) (a, c) | none | none. `parameters.yaml` `ltee.Ne_effective`: "no primary-literature source", `verified: false` (also Q136 note) | **`unverifiable`** | F: a non-standard numeric input stated as fact, uncited. C, tried: (i) standard value? Not on F's closed exempt list. (ii) Day's own derivation? None given; the audit's 3.3e7 (N0 x log2 100) is the audit's own construction. (iii) Same value elsewhere in the paper with a source? s8.2 (Q136) also has no source. Not rescued |
| U7 | Human "Ne ≈ 10,000–33,000", l.136-137 (c) | none | n/a | `n/a`, flagged | F contested-standard: exempt, flagged in the external column |
| U8 | "6.64 generations per day" from "a 1:100 dilution" (l.84); "approximately 25 years per human generation" (l.139) (c) | none | n/a | `n/a` | F: own derivation (log2 100 = 6.64); 25 y is on the standard list (20-30 y) |
| U9 | "an effectively unlimited mutation supply", l.72-73 (a) | none | n/a | `n/a` | K2 uncited qualitative. Against Day's own s4.3 4.1e-4 per genome (Q132) and s6.4 38.4 (Q135) this is **internal** (claim file, Formal statement; R4-A2e: human supply 19-57x the LTEE's), not fidelity |
| U10 | No recombination overhead, no mate-finding cost, no diploid masking, l.126-135 (a, c) | none | Context: Good2017, "inconsistent with a "periodic selection" model in which individual driver mutations fix in a sequence of discrete selective sweeps" (Results) | `n/a` | K2 uncited qualitative. Whether linkage is an advantage is **external** (A5f; GAP-04), not fidelity. Haploidy is standard E. coli biology |
| U11 | "Strong, consistent selection", l.142-144 (a, c) | none | n/a | `n/a` | K2 uncited qualitative |
| U12 | Formal statement chain: rate_human <= 1/G_f, no scaling (d) | none (Day's own bound) | n/a | `n/a` | F: own derivation. The G_f inputs are scored at A2 (`unverifiable`) and are outside K1 |

**Count:** 1 `unverifiable` (U6); 0 `misread`, 0 `partial`, 0 `accurate`; 8 `n/a` (U1, U2, U7-U12), one of them flagged (U7); 3 not scored (U3-U5, not held).

## 4. Readings (rule RD) and the proposed value

| Reading | What the Statement claims | Value | Defensibility of the quoted statement |
|---|---|---|---|
| **R-own** | "ceiling" is Day's inference from the properties he lists ("Every one of these advantages accelerates the fixation process ... The LTEE rate is therefore ...", l.145-147) | **`unverifiable`** (K3: U6 is the most severe scored use; conditional on U3-U5) | Higher. The text gives the premises and the "therefore". Most premises are uncontested facts about the LTEE (clonal, haploid, large Ne, short generation). The step from them to "ceiling" is the internal and external dispute |
| R-attributed | "the empirical ceiling" relays an established finding of the LTEE literature | `n/a` (uncited, qualitative, K2) | Lower. No held source states such a ceiling. The held Good 2017 quotes (competing variants; not serial sweeps) describe a clonal rate limited by interference, not a best case |
| Scope sensitivity (not a reading; cannot set the field, K4) | the two sentences alone, no premises | `n/a` | none |

**Proposed field value: `fidelity: unverifiable`.** Basis in one line: under R-own, the most defensible reading, no held use is misread or partial, and rule F makes the passage's one numeric non-standard input, LTEE Ne ≈ 3 × 10⁷ (uncited), `unverifiable`. Three cited works are not held and are not scored.

**Conditionality (K3).** Reading U3-U5 could move the value. If any of them reads as `misread` or `partial`, the field would take that value. If U6 is sourced (`parameters.yaml` names Lenski et al. 1991 and Wiser et al. 2013 as candidates) and U3-U5 read `accurate`, the field becomes `accurate` (rule F's last clause). If U6 is sourced but U3-U5 are still not held, no scored use is left above `n/a`. The value would then turn on texts that are not held, and the brief's stop rule would apply.

**Comment text for the operator to paste** (replaces `fidelity: pending`; only after the review and the owner approval stage):

```yaml
  fidelity: unverifiable   # R4 A2e-fidelity (research/checks/results/R4-A2e-fidelity.md, criterion 0fd4581): reading R-own (the ceiling is Day's own inference from his listed LTEE advantages; most defensible, rule RD; R-attributed n/a). No held use misread or partial. Rule F: LTEE "Ne ≈ 3 × 10⁷" (s2, p.2-4) is a non-standard number stated without citation (ltee.Ne_effective verified: false). Not scored, not held: Gerrish & Lenski 1998, Couce et al. 2024, Blount et al. 2012 (s2 mechanism list); reading them can move the value. Tenaillon 2016 and Good 2017 are not cited in the A2e passage (s3 data sources; scored at A2/A2b).
```

## 5. Who this helps

**Day side**
- No held use in the ceiling passage is misread or partial. The ceiling is presented as his own inference from listed properties, not as a claim about what the LTEE authors concluded. On the held record he does not misrepresent the LTEE literature here.
- The value rests on one uncited number, whose order of magnitude nobody disputes. Day's 3e7 is within about 10% of the audit's own 3.3e7. R4-A2e swept 3.3e6-1e8, and the LTEE-versus-human ordering in the advantage list holds across that range. `unverifiable` here is a citation gap, not an error. One retrieved source would probably remove it.
- Two of the six uncited "documented" mechanisms match held quotes: hypermutation (Tenaillon 2016) and simultaneously competing beneficial variants (Good 2017). Day cites clonal interference himself (Gerrish & Lenski 1998).

**Critic side**
- The passage cites three works for "documented in the LTEE". None is held, so the audit cannot credit the passage with accurate use. The load-bearing advantage list cites nothing at all.
- The held literature on the passage's own subject cuts against the framing, though as an external point, not a fidelity one. Good 2017 reports many beneficial variants competing at once and rejects a serial-sweep model. That is the interference that makes "no recombination overhead" a doubtful advantage (A5f, GAP-04).
- "An effectively unlimited mutation supply" is contradicted by Day's own figures in the same paper (internal, already in the Formal statement).

**Both / the audit's own errors**
- **The claim table's "verified" rows are not A2e uses.** `A2e-ltee-as-ceiling.md`'s Primary literature table lists Tenaillon 2016 and Good 2017 as "Cited work", marked "verified" and "verified (main text)". Neither is cited in the A2e passage (section 2). The rows were added at R2 extraction (ad44c23, 2026-10-07), and their "What it actually says" text matches the audit's machine-checked quotes in `quotes-literature.md` (Tenaillon2016, Good2017). "Verified" there means that the audit's quote was checked against the paper. It does not mean that a Day use was scored. That explains why the table says "verified" while the field has stayed `pending`. The Good row is also inconsistent across files: "verified (main text)" in A2e, but `ledgers/fidelity.md` (line 37) marks Day's MITTENS 3.0 use of Good 2017 (the ≥95% rule) **unverified**.
- **"Fidelity n/a unchanged" in the claim file's R4 paragraphs** (A2e-alpha, 7ea7290; Uricchio addendum, db2d16d) reads like a field value, but the field has been `pending` since ad44c23. The source is `R4-A2e-alpha.md` l.125, "Fidelity: `n/a` for Day (Day cites none of these papers ...)", which was scoped to the alpha papers only. The scope was lost in the paste.
- This write-up's criterion was written after reading the passage (criterion-only, section 1). Its expectations are not tests.

## 6. Open

1. **U3-U5 not held:** Gerrish & Lenski 1998 (clonal interference), Couce et al. 2024 (epistasis), Blount et al. 2012 (citrate clade). These need a fetch. The value is conditional on them (section 4).
2. **U6 source:** a primary source for LTEE Ne ≈ 3e7 (candidates named in `parameters.yaml`: Lenski et al. 1991, Wiser et al. 2013). Needs a fetch. The audit's own 3.3e7 is unsourced as well.
3. The s1 and s2 Day sentences used here (l.62-149), apart from Q130 and Q131, are not in `quotes-day.md`. The operator should add those that the integration cites.
4. The canonical local copy that Q130-Q139 cite, `sources/raw/day/zenodo-23003785.txt`, is absent. This file used the hash-matched re-fetch (QUEUE "Owner bookkeeping decision (Open 6)", already open).

## 7. Things that looked wrong

- Q131's locator reads "abstract, PDF p.2". In the held text the sentence is in s1, "The Post-Darwinian Polythesis" (heading at l.32; sentence at l.73-74), still on p.2. The claim file says only "p.2".
- The claim file's Assumptions line merges the s1 list (which includes "effectively unlimited mutation supply") with the s2 list. The s2 list has no supply item and does have "No diploid masking", which the Assumptions line omits.
- Rule F's exempt list is closed. It covers E. coli genome size but not LTEE Ne, so an LTEE parameter that is standard in that literature is still `unverifiable` when uncited. This file applies the rule as written; the review may rule on it.
- The node value turns on one row (U6) out of twelve. The review should check that K1(c) puts the advantage list, and with it Ne, inside the scope.

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

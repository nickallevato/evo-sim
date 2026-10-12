# Method audit proposals: held-back rule and vocabulary changes

*2026-10-12, at commit `408ba53`. Specs for the remediation items of [`METHOD-AUDIT-2026-10-12.md`](METHOD-AUDIT-2026-10-12.md) that change the verdict rule or the verdict vocabulary.*

**Status: proposals only. Nothing here is applied.** No verdict value, rule text, lint rule, argmap entry or check script was changed to produce this file. The audit's own finding MA-03 criticises rule changes made and applied on the same day; these are therefore written out in full, with the verdicts and counts each would move, so that they can be reviewed and decided before anything is applied (`DECISIONS.md`, O-6). Counts come from `research/tools/method_audit_stats.py` (read-only). Classifications marked "coded" are one coder's reading of the claim files; that coder is a Claude instance working inside the project, so finding MA-01 applies to them.

Each proposal states: what changes, which counts move and by how much, which side it helps, and the risk.

| | Proposal | Audit finding | Verdict values moved if applied |
|---|---|---|---|
| a | `unexamined` for holds nobody checked | MA-07 | 6, 24, 36 or 58 internal `holds`, by definition chosen |
| b | `external_basis` field and lint | MA-05 | 26 of 52 decided external verdicts relabelled |
| c | Four-way split of `contested` | MA-08 | all 114 `contested` re-coded |
| d | RH6 revision | MA-02 | up to 7 RH tags re-decided; B, B9, C7 may move |
| e | ROOT aggregation rule and stopping rule | MA-11 | none (governs R5) |
| f | Seeded-error test and blind re-derivation | MA-01 | none (measurement) |

---

## (a) `unexamined`: holds on claim files nobody checked

### What changes
1. Internal vocabulary gains one value: `holds | arithmetic-error | non-sequitur | unexamined | pending | n/a`. `unexamined` means: no defect noticed, and no recorded examination of the derivation. `pending` keeps its meaning (an examination is planned or under way).
2. Lint rule: `internal: holds` requires, in the claim file's `## Check` section, either (i) a path to a committed `results/R4-*.md` write-up that scores this node, or (ii) a one-line derivation plus the id of a review by a second agent. Otherwise the lint fails and the value must be `unexamined`.
3. Tallies report `holds` and `unexamined` separately and never report one verdict column without the other two.
4. Separate bookkeeping fix, not a vocabulary change: `status` is stale on files that cite a completed check (B is `status: extracted` after three reviews). Update `status` on those files after step 2 is decided.

### How "unchecked" was determined
The audit's figure is "58 of 131 `holds` sit on files at status `extracted`, meaning no check and no review". I verified the count and tested the gloss.

- **The count reproduces.** 131 internal verdicts begin with `holds` (130 are exactly `holds`; A4 reads "holds for hazard-scale s", outside the vocabulary). 58 of them are on files with `status: extracted`: Day 21, critics 28, allies 3, literature 6. Same as the audit.
- **The gloss does not.** `status: extracted` is not a reliable sign of "no check and no review". I classed each of the 58 by what its own internal-verdict comment and `## Check` section record (pattern match, then each match read by eye):

| What the file records | Files | Day | Critic | Ally | Literature |
|---|---|---|---|---|---|
| Cites a check write-up (`R4 X1`, `R4 B5b`, `R4 E`, ...), often with a review number | 22 | 9 | 11 | 0 | 2 |
| Cites only the combined review of the 12 mapping claims (review #50); no check | 12 | 2 | 10 | 0 | 0 |
| Inline calculation or a reading of the text by the extracting agent; no review | 18 | 9 | 2 | 3 | 4 |
| Nothing ("None.", "No script.", "Script: none.") | 6 | 1 | 5 | 0 | 0 |
| **Total** | **58** | **21** | **28** | **3** | **6** |

Limit of this classification: "cites a check" was read from the file, not confirmed against the check. In some files the cited check is related to the node without testing its internal verdict (D11: "untouched"; A4g: "Related: R4 C2"). Before any value is changed, each of the 22 needs one line saying which table or row of the write-up scores the node.

### Which counts move

| Definition of `unexamined` | Files | `holds` after | Day `holds` | Critic `holds` | Ally | Literature | Day error share | Critic error share |
|---|---|---|---|---|---|---|---|---|
| Today | 0 | 131 | 66 | 50 | 6 | 9 | 19/85 = 22% | 1/51 = 2% |
| Strict: nothing recorded | 6 | 125 | 65 | 45 | 6 | 9 | 19/84 = 23% | 1/46 = 2% |
| **Recommended: nothing recorded, or inline and unreviewed** | 24 | 107 | 56 | 43 | 3 | 5 | 19/75 = 25% | 1/44 = 2% |
| Wide: the above plus mapping-review-only | 36 | 95 | 54 | 33 | 3 | 5 | 19/73 = 26% | 1/34 = 3% |
| The audit's: every `holds` at status `extracted` | 58 | 73 | 45 | 22 | 3 | 3 | 19/64 = 30% | 1/23 = 4% |

The recommended line follows the audit's own lint wording ("a `Check` entry or an explicit one-line derivation reviewed by a second agent"): the 12 mapping claims had a second-agent review and stay `holds`; the 18 inline-only files did not and move.

Load-bearing nodes among the 58: B2b, E5, E6. All three cite a check write-up (R4 B2b, R4 X1/E5E6) and stay `holds` under every definition except the audit's.

### Which side it helps
Neither side's argument. It removes default credit from both. Under the recommended line Day loses 10 holds (15% of his) and critics 7 (14% of theirs). Under the audit's definition critics lose 56% of their holds and Day 32%, so the wider the definition, the more it answers the Day-side complaint "critics get free holds". The error shares rise for both because the denominator shrinks; that is a further reason not to publish the shares (MA-06).

### Risk
- A fifth value makes the vocabulary look more exact than the classification behind it. The pattern test will misfile some nodes until each is read.
- `unexamined` can become a parking place. Pair it with a rule that no load-bearing node may carry it at R5.

### The 58 files

| Id | Side | Load-bearing | What the file records | File |
|---|---|---|---|---|
| A2i | critic |  | nothing | `A2i-matev-gf-units-years-vs-generations.md` |
| A2j | day |  | inline calculation or text reading, unreviewed | `A2j-day-2nd-edition-1400-and-1587.md` |
| A4e | critic |  | mapping review only | `A4e-hancock-overlap-is-handled-by-ne-and-moran.md` |
| A4f | critic |  | mapping review only | `A4f-hancock-d-not-a-selection-coefficient.md` |
| A4g | day |  | mapping review only | `A4g-day-standard-models-assume-complete-replacement.md` |
| B2b | day | yes | check write-up cited | `B2b-ceiling-x-vk-g-over-16.md` |
| B2c | day |  | inline calculation or text reading, unreviewed | `B2c-one-in-ten-to-78-millionth.md` |
| B2d | day |  | inline calculation or text reading, unreviewed | `B2d-parallel-fixation-second-objection.md` |
| B3f | day |  | check write-up cited | `B3f-800000-mu-grok-exchange.md` |
| B3i | critic |  | check write-up cited | `B3i-matev-sum-over-alleles-exceeds-one.md` |
| B4 | day |  | check write-up cited | `B4-clock-recalibration-200-580-kya.md` |
| B4b | day |  | inline calculation or text reading, unreviewed | `B4b-chlca-68-kya.md` |
| B4g | critic |  | check write-up cited | `B4g-keruru-pedigree-vs-fossil-calibrated-twice.md` |
| B5a | critic |  | check write-up cited | `B5a-mccarthy-22-5-million.md` |
| B5b | critic |  | check write-up cited | `B5b-mansfield-one-fixation-per-generation.md` |
| B5f | critic |  | check write-up cited | `B5f-reddit-9-7-million-haploid.md` |
| B5g | critic |  | nothing | `B5g-paul-king-comment-neutral-rate-equals-arrival.md` |
| B5h | ally |  | inline calculation or text reading, unreviewed | `B5h-hossjer-neutral-d-mu-7-6-million.md` |
| B5j | critic |  | mapping review only | `B5j-hancock-neutral-theory-is-not-a-retreat.md` |
| B6c | critic |  | check write-up cited | `B6c-hancock-no-standing-variation-prediction.md` |
| B9 | day |  | check write-up cited | `B9-drift-would-cause-extinction-within-centuries.md` |
| D11 | literature |  | check write-up cited | `D11-taylor-2001-1-in-5e23.md` |
| D14 | ally |  | inline calculation or text reading, unreviewed | `D14-davis-relays-eden-1e36-genetic-transfers.md` |
| D2e | day |  | inline calculation or text reading, unreviewed | `D2e-day-waddington-summary-asserted-not-shown.md` |
| D2i | day |  | check write-up cited | `D2i-day-evolutionary-algorithms-designed-fitness.md` |
| D2k | critic |  | mapping review only | `D2k-hancock-mathematicians-built-the-synthesis.md` |
| D2l | day |  | mapping review only | `D2l-day-synthesis-founders-skipped-the-math.md` |
| D3 | literature |  | inline calculation or text reading, unreviewed | `D3-eden-sequence-space-arithmetic.md` |
| D3a | literature |  | inline calculation or text reading, unreviewed | `D3a-eden-molecules-not-functional-proteins.md` |
| D4 | literature |  | check write-up cited | `D4-ulam-sequential-improvements-10-to-13-generations.md` |
| D4a | literature |  | inline calculation or text reading, unreviewed | `D4a-ulam-random-construction-is-not-the-problem.md` |
| D6 | literature |  | inline calculation or text reading, unreviewed | `D6-wright-twenty-questions-1250.md` |
| D7 | day |  | inline calculation or text reading, unreviewed | `D7-fisher-500-to-1-against-fixation.md` |
| D7a | day |  | inline calculation or text reading, unreviewed | `D7a-spetner-chain-3.6e2738-to-1.md` |
| D7b | day |  | inline calculation or text reading, unreviewed | `D7b-0.9727-needs-1.08-million-beneficial-mutations-per-step.md` |
| D9 | day |  | inline calculation or text reading, unreviewed | `D9-weasel-540000-generations.md` |
| E | day |  | check write-up cited | `E-hypermutation-hazard.md` |
| E3 | day |  | check write-up cited | `E3-cmmrd-simulation.md` |
| E4 | day |  | check write-up cited | `E4-relictation.md` |
| E5 | critic | yes | check write-up cited | `E5-ara2-ara5-counts.md` |
| E6 | day | yes | check write-up cited | `E6-strict-vs-95-counts.md` |
| F1b | critic |  | check write-up cited | `F1b-mccarthy-parallel-not-one-at-a-time.md` |
| F1c | critic |  | mapping review only | `F1c-hancock-waiting-time-lineage.md` |
| F4 | critic |  | inline calculation or text reading, unreviewed | `F4-bowers-fixation-probability-2s.md` |
| F4a | day |  | nothing | `F4a-day-reply-fixation-probability-vs-rate.md` |
| G1b | ally |  | inline calculation or text reading, unreviewed | `G1b-samson-total-over-time.md` |
| G1c | critic |  | nothing | `G1c-camestros-average-concession.md` |
| G2c | critic |  | check write-up cited | `G2c-hancock-no-variation-prediction.md` |
| G2d | critic |  | nothing | `G2d-camestros-wording-reads-serial.md` |
| G2e | critic |  | check write-up cited | `G2e-myers-massively-parallel.md` |
| G2f | critic |  | check write-up cited | `G2f-bowers-serial-lottery.md` |
| G2h | critic |  | mapping review only | `G2h-hancock-fmax-has-no-mutation-or-selection-term.md` |
| G3a | critic |  | nothing | `G3a-camestros-lottery.md` |
| G5 | critic |  | inline calculation or text reading, unreviewed | `G5-matev-cv-falls-variance-rises.md` |
| H2a | critic |  | mapping review only | `H2a-hancock-cost-of-selection-hard-selection-only.md` |
| ROOT-COV | critic |  | mapping review only | `ROOT-cov-hancock-selection-is-a-covariance.md` |
| ROOT-EP | critic |  | mapping review only | `ROOT-ep-hancock-endorsers-lack-popgen-background.md` |
| ROOT-PG | critic |  | mapping review only | `ROOT-pg-hancock-popgen-track-record.md` |

---

## (b) `external_basis`: say what an external verdict rests on

### What changes
1. New front-matter field under `verdicts`, required whenever `external` is `supported` or `contradicted`, optional (recommended) for `contested`:

   ```yaml
   verdicts:
     external: contradicted
     external_basis: data        # data | literature | simulation | theory
   ```

   | Value | Definition |
   |---|---|
   | `data` | An observation the audit processed itself (an alignment, genotypes, a published data table recomputed) and compared with the claim. |
   | `literature` | A published result or text, cited and not reprocessed. Add `literature-data` in the comment when the cited result is itself a measurement. |
   | `simulation` | A forward or exact-chain simulation under a stated model. |
   | `theory` | An identity or analytical result of standard population genetics. |

   One primary value. A second basis goes in the comment (`also: data`).
2. Lint rule L-EB1: `external` in {`supported`, `contradicted`} without `external_basis` fails.
3. Lint rule L-EB2 (the audit's remedy 1), in one of two strengths, to be chosen:
   - **Label only:** tallies and the board split `supported`/`contradicted` by basis. No verdict value changes.
   - **Relabel:** `supported`/`contradicted` require `data` (or `literature-data`); with `simulation` or `theory` the value becomes `model-consistent` / `model-inconsistent`, two new external values.
4. For each load-bearing node whose basis is `simulation` or `theory`, the claim file names the observation that would bear on whether the model applies.

### Coded count
The audit read the verdict comments and estimated "roughly twenty" of 52 model-based, noting it was "not a coded count". I coded all 52 from the external-verdict comment, the title and, where the comment is empty (13 files), the body.

| Basis | Files | Day | Critic | Literature | `supported` | `contradicted` |
|---|---|---|---|---|---|---|
| `data` | 16 | 11 | 2 | 3 | 9 | 7 |
| `literature` | 10 | 3 | 3 | 4 | 9 | 1 |
| `simulation` | 10 | 2 | 6 | 2 | 8 | 2 |
| `theory` | 16 | 10 | 6 | 0 | 8 | 8 |
| **Total** | **52** | **26** | **17** | **9** | **34** | **18** |

**Model-based (simulation or theory): 26 of 52 (50%)**, against the audit's "roughly twenty". By side: 12 of Day's 26, 12 of the critics' 17, 2 of the literature's 9.

| Id | Side | External | Basis | Cue in the claim file |
|---|---|---|---|---|
| A3b | day | supported | data | GAP-07b measured events per lineage |
| A3c | literature | supported | data | GAP-07c measured polymorphic share |
| A3x | critic | supported | data | GAP-07b direct count |
| B3d | day | contradicted | data | event counts against a base-pair numerator (also: theory) |
| C1 | literature | supported | data | v62 panel totals against neutral D2/D3 (also: simulation) |
| C5b | critic | supported | data | C1d replicates his values on AADR |
| C6 | day | contradicted | data | real AADR genotypes, 132 configurations |
| C7 | day | contradicted | data | F_adj measured between AADR bins |
| DN1 | day | contradicted | data | L1 on hg38/panTro5 (conditional on L1b) |
| DN2 | day | contradicted | data | L1, 32 stacks |
| DN3 | day | contradicted | data | L1, two gene sets |
| DN5 | literature | supported | data | L1 independent pipeline |
| FM3 | day | supported | data | FM on the T2T alignment |
| FM4 | day | supported | data | FM clustering |
| FM5 | day | supported | data | FM, as a description |
| FM8b | day | contradicted | data | FM share of differences in mesas |
| A1 | day | supported | literature | 6.3 My at 25 y from published dates |
| A1a | literature | supported | literature | published split dates |
| A1b | literature | supported | literature | published generation lengths |
| A2d | critic | supported | literature | LTEE published counts |
| A2e | day | contradicted | literature | published alpha estimates mapped to the flip (also: simulation) |
| A2g | literature | supported | literature | LTEE papers |
| A3x1 | literature | supported | literature | Yoo 2025 text |
| A6a | day | supported | literature | Yoo 2025 SweepFinder2 result |
| D1d | critic | supported | literature | existence of post-1966 quantitative literature |
| D2k | critic | supported | literature | history of the field, broad reading |
| A5f | critic | supported | simulation | R_int clonal against free recombination |
| B1c | literature | contradicted | simulation | step-history runs |
| B3b | day | supported | simulation | overlap and fluctuation runs |
| B3c | day | contradicted | simulation | 0.743 as a window artefact |
| B6 | critic | supported | simulation | "full pipe gives k = mu ... (forward sim)" |
| B6b | critic | supported | simulation | B4a two-lineage run |
| B6c | critic | supported | simulation | "as a conditional", A_long rerun |
| G2c | critic | supported | simulation | same |
| F1b | critic | supported | simulation | in-transit count measured in simulation |
| H7 | literature | supported | simulation | H3 hard-selection bounds |
| B3 | day | contradicted | theory | k/mu family against k = mu (also: data for 32.3) |
| B3a | day | contradicted | theory | fixation probability 1/(2N) |
| B3e | day | contradicted | theory | built on B3a |
| B3f | day | contradicted | theory | 800,000 mu from N/N_e |
| B3g | day | supported | theory | Day's concession agrees with the identity |
| B3i | critic | supported | theory | 1/(2N) of census copies |
| B5c | critic | contradicted | theory | double count against 2muT + ancestral term (also: data) |
| B6a | day | contradicted | theory | ancestral term at sourced N_e |
| B7 | critic | supported | theory | 1/(2N) |
| B7c | critic | supported | theory | 1/(2N_census) |
| B9 | day | contradicted | theory | "premise 1 false under standard theory" (also: data, L1) |
| C2c | day | contradicted | theory | ratio invariant for random locus pairs |
| D7 | day | supported | theory | "standard result" |
| F4 | critic | supported | theory | 2s approximation |
| H1 | day | supported | theory | neutral k = U |
| H6 | critic | supported | theory | neutral k = U |

Coding limits: one coder, primary basis only, from short comments. The six rows with "also:" could be coded either way; moving each to its second basis gives model-based between 23 and 29.

### Which counts move
- **Label only:** none. The 52 are reported as 16 data, 10 literature, 26 model.
- **Relabel:** `supported` 34 -> 18 and `contradicted` 18 -> 8; 16 become `model-consistent`, 10 `model-inconsistent`. Day `contradicted` 16 -> 8. Critic `supported` 16 -> 5.
- **Load-bearing nodes.** Eight load-bearing nodes carry a decided external verdict. Seven are model-based (B1c, B3, B3a, B3g, B6, B7, H1) and one rests on published estimates (A2e). **No load-bearing external verdict currently rests on data the audit processed.** This is the sharpest form of MA-05 and was not in the audit.

### Which side it helps
Day's side on the count that is most often quoted: his `contradicted` total halves. The critics' side loses most in proportion: 11 of their 16 `supported` verdicts become `model-consistent`. Substantively it helps a careful reader of either camp, since the information "this was shown inside the standard model" is exactly what Day disputes and what critics take as given.

### Risk
- "Model-consistent" may read as a downgrade of results that are decisive on the internal question. Mitigation: the write-ups already score those under `internal`; say so beside the label.
- The `data` label can overstate too. A data verdict still depends on a pipeline (assembly, annotation, filters). Do not present `data` as "settled".
- Relabelling changes verdict values and should go through the load-bearing tier, since seven moved nodes are load-bearing. "Label only" can be applied first at no such cost.

---

## (c) Splitting `contested` four ways

### What changes
`contested` (114 of 172 decided external verdicts) is replaced by four values, each with a required companion:

| Value | Definition | Required companion |
|---|---|---|
| `conditional:<parameter>` | The verdict turns on a named quantity; the claim is supported on one side of a stated value and contradicted on the other. | The flip value or range, and whether the parameter is sourced. |
| `regime-limited` | Shown true or false only in the regime tested; untested elsewhere. | The regime (N, s, R, K, model) and the regime the claim needs. |
| `disputed-in-literature` | Published sources disagree and the audit has not adjudicated. | Two sources, one each way. |
| `undetermined` | None of the above: no examination, a missing source, or an evaluative claim with no agreed standard. | A reason code: `no-basis-recorded`, `source-missing`, `evaluative`, `other`. |

Optional on any of the four: `lean: supported|contradicted` with the evidence that would settle it. A lean is not counted in any tally.

### Trial classification
Sample: 20 of the 114 `contested` ids, drawn with `random.Random(20261012).sample(sorted(ids), 20)` (`method_audit_stats.py`). Coded from the external-verdict comment; where it is empty, from the internal comment.

| Id | Side | Status | Trial value | Basis for the coding |
|---|---|---|---|---|
| A | day | reviewed | `conditional:adaptive share` | binds only if more than 13-27% of differences are adaptive; which model holds is branch B |
| D15 | ally | reviewed | `conditional:intermediates, target specificity` | flips under beneficial intermediates or a non-specific gene set; premises unsourced both sides |
| D3 | literature | extracted | `conditional:landscape structure` | bearing on search depends on D3b |
| H | day | reviewed | `conditional:K, survival horizon` | "slower than 1/300" conditional on K (tested to 64,000) |
| ROOT-K | ally | extracted | `conditional:bacterial rate as ceiling` | reaches the claim only if A2e holds |
| F2 | day | reviewed | `regime-limited` | no collapse "in F2's tested regime"; human-scale concurrency not run |
| D4 | literature | extracted | `disputed-in-literature` | serial assumption disputed in the volume (Mayr, p.24); one source only, so the two-source rule is not yet met |
| A2 | day | reviewed | `undetermined` (`source-missing`) | "calibration underdetermined" |
| A4 | day | reviewed | `undetermined` (`source-missing`) | "which s scale the cited aDNA papers use is unretrieved" |
| ROOT-PG | critic | extracted | `undetermined` (`evaluative`) | a track-record argument |
| A3z | day | checked | `undetermined` (`other`), lean contradicted | 410 M is base pairs; events are 8.5x lower "in a different unit" |
| D9 | day | extracted | `undetermined` (`other`), lean contradicted | conditional fix time about 8,500, not 20,000; parallel loci about 13,000 |
| Ga | day | checked | `undetermined` (`other`), lean contradicted | arithmetic holds but prices the wrong event |
| A4g | day | extracted | `undetermined` (`other`) | true of Wright-Fisher as defined, not of the standard toolkit (comment sits under `internal`) |
| A4f | critic | extracted | `undetermined` (`no-basis-recorded`) | empty comment |
| B2c | day | extracted | `undetermined` (`no-basis-recorded`) | empty comment |
| B4d | day | extracted | `undetermined` (`no-basis-recorded`) | empty comment |
| B4e | critic | extracted | `undetermined` (`no-basis-recorded`) | empty comment |
| D13 | ally | extracted | `undetermined` (`no-basis-recorded`) | empty comment |
| G2g | day | checked | `undetermined` (`no-basis-recorded`) | empty comment |

| Trial value | In sample | Share | Scaled to 114 (rough) |
|---|---|---|---|
| `conditional:<parameter>` | 5 | 25% | about 29 |
| `regime-limited` | 1 | 5% | about 6 |
| `disputed-in-literature` | 1 | 5% | about 6 |
| `undetermined` | 13 | 65% | about 74 |
| of which `no-basis-recorded` | 6 | 30% | about 34 |
| of which lean contradicted, poor fit | 3 | 15% | about 17 |

With n = 20 each share carries roughly ±20 points; the scaled column is an order of magnitude.

### What the trial shows
1. The split works for a third of the sample and leaves two-thirds in `undetermined`. Most of the mass of `contested` is not dispute. It is the absence of an examination.
2. Six of 20 `contested` verdicts have no recorded basis. `contested` has been acting as the external column's default, as `holds` does for the internal column (proposal a). They belong in `pending` or in an external `unexamined`.
3. Three of 20 (A3z, D9, Ga), all Day claims, read as "contradicted, scoped" filed under `contested`. The audit's critic-side worry (false balance) has support here; so does its Day-side worry, since a lean recorded only in a comment cannot be checked.
4. `disputed-in-literature` as defined (two sources) is nearly empty. D10, the audit's example, was not drawn.

### Which counts move
All 114 are re-coded. Expected on the sample: roughly 30 conditional, 6 regime-limited, 6 disputed, 74 undetermined, of which about 34 would be better as `pending`/`unexamined`. If those 34 leave the decided column, decided external verdicts fall from 172 to about 138 and the conditional-plus-regime-plus-disputed share is about 30%.

### Which side it helps
The critics' side where a lean toward `contradicted` on a Day claim becomes visible. Day's side where `conditional` shows the flip value and that the deciding parameter is unsourced (A, H, D15). Neither side on the largest bin, which is the audit's own unfinished work.

### Risk
- Re-coding 114 verdicts is a large verdict-touching operation by the same model family; it needs a second coder and an agreement figure.
- `lean` invites a shadow tally. Keep it out of every count.
- The coding of the sample is from short comments; a full read of each claim file may move several rows.

---

## (d) RH6 revision (MA-02)

### What changes
RH6 as written ("`dialectic` if the literal claim is remotely close under the most charitable reading, else `rhetoric`", 3x band) is replaced by RH6 rev 2:

1. **Tag by context, blind to the number.** A statement whose tag is unclear is tagged from five criteria fixed here, each answered yes or no from the source text before any calculation is run or consulted:
   - C1. A derivation, table or cited number is attached to the sentence in the same source.
   - C2. The author uses the sentence as a premise elsewhere (cite the place).
   - C3. The author glosses or defends it as literally meant when challenged (cite the place).
   - C4. It sits in a title, peroration, taunt or closing flourish.
   - C5. It is addressed to an opponent or audience as a challenge, not offered as a step.

   `dialectic` if any of C1 to C3 is yes. `rhetoric` if C1 to C3 are all no and C4 or C5 is yes. Otherwise `unclear`, recorded as such, and the statement is scored as dialectic with the tag shown. The criteria met are recorded in the claim file. The tagger does not see the check's numbers.
2. **Always report the literal distance.** For every tagged statement, whatever the tag, the claim file and the ledger give each plausible literal reading and its distance from the measured or derived value. A `rhetoric` tag changes the node verdict column only. It never removes the number from the public page.
3. **Absolutes get explicit thresholds, set in the rule.** No multiplicative band on "none", "not at all", "nearly empty", "can't do any". The rule fixes the scale per kind of quantity:

   | Kind | "None / not at all" is literally true if | "Nearly none / nearly empty" if |
   |---|---|---|
   | A share or fill (0 to 1) | 0, or below the measurement's stated resolution | at most 0.10 |
   | A count out of N | 0 | at most max(1, N/10) |
   | A rate against a reference rate | below 1% of the reference | at most 10% of the reference |

   The thresholds are conventions. They are stated once, here, with a sensitivity row at half and double, and no check may set its own edge.
4. **Evaluative claims about the dispute** ("I debunked", "has never been answered") are marked `not checkable here`. They are not scored against the audit's own tallies.
5. **Counters leave the audit record.** The "answer with better rhetoric" column moves from `ledgers/slips.md` to a separate commentary file that no verdict or tally reads.

### Which counts move
Seven tags were decided under RH6: Q104 (B9), Q96 (C7), Q157/Q158 (B), RH-15 (Hancock), RH-18 (Mansfield), RH-20 and PZ-03 (Myers). All seven would be re-tagged by a tagger blind to the numbers. Node verdicts that depend on those tags: B internal (load-bearing), B9 internal, C7 internal and external. I did not re-tag them: doing so is applying the rule. Under item 4, RH-20 and PZ-03 become `not checkable here`, which is the same practical outcome as today (unscored) for a different stated reason. Under item 3 the fill threshold "at most 0.10" is stricter than the 0.30 edge used in R4-RHclose, so fills of 0.256 and 0.281 would no longer count as "nearly empty" being literally close; what that does to B depends on the context tag and must not be guessed here.

### Which side it helps
It removes an exemption that has been used on both sides (Day's Q157/Q158 on one reading; Myers's "debunked"). A speaker far from the mark no longer goes unscored for that reason. Net direction is unknown until the seven are re-tagged blind, which is the point of doing it blind.

### Risk
- The five criteria are also judgement calls; two taggers should apply them and report agreement.
- C3 favours authors who are challenged often and reply often (Day), since only they have glosses on record.
- The absolute thresholds are new conventions set after the cases are known. They should be fixed by someone who has not seen which way each case falls, or with the adversarial readers of O-3.
- Re-opening B this way is a third change to a load-bearing verdict in the same week. It should happen once, together with O-5, under three reviews.

---

## (e) ROOT aggregation rule and stopping rule, draft for R5 (MA-11)

To be committed and pushed before any R5 text is drafted. Draft only.

### Aggregation rule
ROOT is "No evolutionary mechanism can produce the observed human-chimpanzee divergence in the available time", a universal negative resting on branches A to H and ROOT-M. The audit makes statements per branch and one statement about the argument as a whole. It does not count nodes, average verdicts or take a majority.

**Inputs.** Only nodes with `load_bearing: true` at status `reviewed`, reviewed at the load-bearing tier, count. A node that is `pending`, `unexamined`, reading-dependent, any form of `contested`, or below that tier contributes "undetermined". Fidelity verdicts never decide a branch; they are reported beside it.

**Admissible statements per branch X**, tested in this order:

| Code | Statement | Condition |
|---|---|---|
| X-fails-internally | "Day's argument on branch X does not follow from his own premises." | At least one load-bearing Day node on X is `non-sequitur` or `arithmetic-error`, the error is material by rule R1, and no later Day source repairs it. |
| X-contradicted-by-data | "A premise of branch X is contradicted by observation." | At least one load-bearing Day node on X is external `contradicted` with `external_basis: data`. |
| X-fails-under-standard-model | "Branch X does not go through if the standard model applies; the audit has not tested whether it applies." | As above with basis `simulation` or `theory`. |
| X-stands | "Day's argument on branch X stands." | Every load-bearing Day node on X is internal `holds` (examined), none has fidelity `misread`, each has external `supported` with basis `data`, and every critic attack on X recorded in the argmap is answered or has itself failed. |
| X-stands-conditionally | "Branch X stands if <parameter> is on the stated side of <value>." | As X-stands, except one or more nodes are `conditional:<parameter>`; the statement names every such parameter and its flip value. |
| X-undetermined | "The audit cannot say." | Anything else. This is the default. |

**Admissible statements about ROOT:**

| Code | Statement | Condition |
|---|---|---|
| R-not-established | "Day's case for the root claim is not established: each route to it fails or is undetermined." | No branch among those the ROOT file requires (A, B and G) is X-stands or X-stands-conditionally. State for each whether it fails internally, by data, under the standard model, or is undetermined. |
| R-stands-on-X | "Day's root claim stands on branch X [if <parameter>...]." | A, B and G are each X-stands or X-stands-conditionally, and every row of ROOT-M carries a computed exclusion (the ROOT file's own condition). |
| R-refuted-for-mechanism-M | "The root claim as worded is refuted for mechanism class M." | A mechanism class in ROOT-M is shown to deliver the required count within T. If shown by forward simulation only, the statement reads "under the standard model", per proposal (b). |
| R-undetermined | "The audit reaches no conclusion on the root claim." | Anything else. Default. |

The audit never states "evolution is mathematically possible" or "impossible". Its object is Day's argument and the replies to it.

**What would make the audit say R-stands-on-X** (the audit's remedy b): the conditions in that row, with all three of A, B and G. As of today none of the three meets them: A is `contested`; B is internal `non-sequitur` (itself under O-5); G has no load-bearing node at all, which the rule exposes and which must be fixed before R5 by deciding whether a G node is load-bearing.

**As of today the rule returns R-undetermined**, because B and A2e are outside their required tier (O-5), every load-bearing external verdict is model-based or literature-based (proposal b), and ROOT-M is `pending`. Stating this before R5 is the purpose of registering the rule.

### Stopping rule
1. **Corpus freeze.** A date set by the owner (O-7). Sources published after it go to an appendix "after the freeze" and move no verdict.
2. **One exception, fixed in advance:** a post-freeze source is checked if it (i) releases code or data for a node that is `pending` because the method was unreleased (FM10, DN1), or (ii) is an author's reply under the right-of-reply procedure (O-2).
3. **Load-bearing list freeze.** The list of `load_bearing: true` nodes is frozen at the same date, after one pass by a reader from each camp if O-3 is adopted.
4. **R5 may be drafted when:** every frozen load-bearing node is at status `reviewed` at the load-bearing tier or is declared undetermined with a reason; every decided external verdict has an `external_basis`; the registered runs (L1b, L1c, L5, FMnull) are collected or withdrawn; the reply window has closed.
5. **Budget stop.** If item 4 is not met within a number of checks set at the freeze (suggested: the registered runs plus at most ten more), R5 is written on the state reached, with the unmet nodes listed as undetermined.

### Which counts move
None. It constrains what R5 may say.

### Which side it helps
The Day side, against a conclusion written after the fact from a favourable subset of nodes, and against the audit chasing each new post with a new study it then counts against him. The critic side, against a "both have points" conclusion drawn from the size of the `contested` bin, and against an audit with no end. The default is "undetermined" for both.

### Risk
- The rule is strict enough that R5 may return undetermined on most branches. That would be the correct report of the present state.
- "Material by rule R1" and "repaired by a later source" import existing judgement calls.
- The order of the tests matters (internal failure is reported before data); it is fixed above so it cannot be chosen later.
- Drafted by the auditing model with the present verdicts in view. It should be reviewed by the O-3 readers before it is registered.

---

## (f) Measuring the reviews: seeded-error test and blind re-derivation (MA-01)

### f1. Seeded-error test

**Purpose.** Turn "no review has blocked a check" into a catch rate.

**Protocol.**
1. **Material.** Five reviewed write-ups with their scripts, stratified: two load-bearing with a simulation (H8, A2e), one load-bearing arithmetic (B2/B), two low-stakes (B5b, GAP-06). Fixed here so they are not chosen after the fact.
2. **Planting.** One agent (the planter) makes copies in a scratch directory outside the repository. Each of the five gets four planted defects, one per class, graded: (i) a unit or factor slip in a reported number that the script output contradicts; (ii) a swapped basis (census N for N_e, per-year for per-generation) in the derivation; (iii) a prediction band widened after the run so a miss reads as a hit, with the docstring changed to match; (iv) a quote altered in one word that changes its sense, or a locator pointing at the wrong paragraph. Each defect is material under rule R1. Twenty defects in all. Two further copies are left clean as controls. The planter writes a sealed key (file hash committed first, content committed after scoring).
3. **Review.** Each copy goes through the standard review prompts for its tier, unchanged: three reviews for the load-bearing ones, one combined review for the low-stakes ones. Reviewers are fresh agents told only what a reviewer is normally told. They are not told a test is running.
4. **Scoring.** A defect is caught if any review of that copy names it at MAJOR or BLOCKER. Report: catch rate overall and per defect class, per tier, per review role; false alarms on the clean controls (MAJOR or BLOCKER raised on unchanged text that the original reviews did not raise); with a binomial interval.
5. **Pre-registration.** This protocol, the five write-ups, the defect classes and the scoring rule are committed and pushed before planting.
6. **Reading the result.** The rate bounds what the existing reviews can be taken to have excluded. It measures planted, known kinds of defect; it does not measure shared wrong beliefs, which the planter shares too.

**Cost (estimates; the token figures assume a review reads the write-up, the script and the cited quotes, about 80,000 to 150,000 tokens per review run).** 7 copies: 3 load-bearing x 3 reviews + 2 low-stakes x 1 + 2 controls x 1 to 3 = 13 to 17 review runs, plus 1 planter run and 1 scorer run: about 1.5 to 2.5 million tokens on the stronger model. No compute beyond trivial. One to two days elapsed under the two-subagent cap.

### f2. Blind re-derivation of ten load-bearing nodes

**Purpose.** An inter-rater figure that is blind, to replace the one existing measurement (90% and 100%, not blind).

**Nodes, by a mechanical rule.** Every load-bearing node that carries an internal error verdict (A2e, B, C2, F1a, H5), plus the five the audit names as carrying the most: B3a and B7 (k = μ), B4a (ancestral polymorphism), H8 (cost), A3 (event counts). Ten nodes: seven Day, one critic, one ally, one literature.

**Protocol.**
1. **Packet per node,** assembled by one agent and checked by a second for leaks: the verbatim Statement quotes with locators; the raw source text they come from (the full document, from `sources/raw/`); the data files a check used, if any; the three verdict definitions and the verdict rule text. Nothing else. No claim file, no write-up, no review, no `AGENTS.md`, no argmap, no title that states a conclusion.
2. **Rater.** A fresh agent per node, run from an empty directory outside the repository so that no project instructions load. If O-4 is approved, a second rater from a different model family on the same packets.
3. **Task.** State what the quote claims formally; derive or compute it; give internal, fidelity and external verdicts with reasons and a confidence; list what it could not determine. The rater may write and run its own code within the workstation limits; anything heavier is reported as "needs simulation" and not run.
4. **Scoring.** Agreement with the claim file per column (exact match; and match after merging `contested`/`pending`), reported per node with both verdicts side by side. Disagreements are not resolved by the original author: each goes to a third agent that sees both derivations and no names.
5. **Pre-registration.** Node list, packet contents and scoring rule committed and pushed first. The claim-file verdicts are already public, so the comparison target is fixed.

**Leak risk that cannot be removed:** the rule text contains worked examples that name some of these nodes and their intended outcomes (the X1 rule audit found 15). Use a copy of the rule with its worked examples and test cases removed, and say so in the report.

**Cost (estimates).** 10 packets at about 100,000 to 200,000 tokens per rater run, plus packet assembly and leak check (about 300,000) and adjudication of disagreements (about 50,000 each): about 1.5 to 2.5 million tokens for one rater family, double with a second. Compute: B4a and H8 need forward simulation for a full re-derivation; if the rater reports "needs simulation", an independent re-implementation on `na-workhorse` is hours of CPU, not days. Two to three days elapsed.

### Which counts move
None directly. A disagreement on a load-bearing node sends that node back to `pending` until adjudicated, under the load-bearing tier.

### Which side it helps
Both, by replacing an assertion with a measurement. A low catch rate weakens every verdict in proportion, most of all the error verdicts, of which Day carries 19 and critics 1.

### Risk
- A same-family planter and same-family reviewers share blind spots: the test can show the reviews are weak, and cannot show they are strong.
- Planted copies must never reach the repository or a milestone post. They stay in scratch directories; only the protocol, the key hash, the key and the scores are committed.
- A high catch rate on planted slips will be over-read. The report must carry the limit in item 6.

---

## Not covered here

The audit's other structural items are not specified in this file: `side: audit` and separate reporting of audit-made attacks (MA-15); a mechanical tier test fixed at registration (MA-18); the mirror tree rooted at the critics' thesis (MA-13); blind re-extraction of 30 claim files (MA-09); one-command quote verification (MA-19). Two bookkeeping items found while preparing these proposals, neither a rule change: the internal verdict of `A4` is outside the vocabulary and passes the lint; the front-matter comments of C7 and B9 still say "most charitable to Day", which the rule text has not said since `3f881b0`.

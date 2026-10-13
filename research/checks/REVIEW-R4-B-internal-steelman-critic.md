This review argues the critics' side on claim B's internal field as hard as it can honestly be argued. It is not a neutral review and sets no verdict (D-24: where the steelmen conflict, the lead rules).

# REVIEW R4 B internal: steelman, critic side (O5 review 3/6, D-21)

- Reviewer: fresh reviewer instance, 2026-10-13. Brief: `research/checks/briefs/O5-reviews-reviewer.md` (f9e254d). I wrote none of the other five O5 reviews and did not read them. None was in the repo when I started.
- Target: `docs/research/claims/B-neutral-theory-cannot-rescue.md` l.12-14 (field comment), the Statement block l.18-29 and the R4 RHclose Readings table (l.78-85). Bases: `research/checks/results/R4-B2.md` (Rule N), `R4-RHclose.md` Part 2 and its review resolution, `R4-X1-verdict-rule.md` (C, S1, N, RH1-RH6, RD), `quotes-day.md` Q140, Q151-Q158, `ledgers/slips.md` RH-10, RH-26.
- Question (brief): does the evidence on record carry B internal to `non-sequitur` under rule C, rule RD and the stated scoping?
- **Critic-side answer: yes, and more robustly than the claim file says.** The field comment presents the value as resting on four numeric readings of "nearly empty", with a Day-favourable `holds` recorded beside it. On the critic case, Q157 is a non-sequitur under every plausible reading, the F-over-6.5-My reading included. The `holds` beside it comes from Q158's wording, and Q158 is not a B Statement quote.

## Source check (recomputed, not trusted)
- Hard Limits was fetched read-only from Zenodo into `sources/raw/b-steelcrit-2026-10-13/` (gitignored). The file md5 `4f66a658…` matches Zenodo's checksum. The sha256 `66aa8be6…55719bf` matches `bib-day.md` l.48. The audit's local text `sources/raw/day/zenodo-22129121.txt` is on neither this workstation nor na-workhorse, so I used a fresh `pdftotext` extraction. Its line numbers differ from the audit's. Below, "l." means the audit's local text (taken from the Q ids), and "fx" means my fresh extraction.
- Q140, Q151, Q152, Q153, Q156, Q157 and Q158 are all present verbatim in fx (abstract fx 21-23; fx 522-525; fx 530-536; fx 607-609; fx 621-624; fx 634-635).
- Recomputed with the RHclose formula F(x) = 1 + Σ(-1)^i(2i+1)e^{-i(i+1)x/4}, D = (1/x)∫F, N_e = 4·1e5/7 = 57,143, g = 25 y:

| Reading input | x | F | D | F / 0.30 edge | On record |
|---|---|---|---|---|---|
| 6.5 My | 4.55 | 0.697 | 0.256 | **2.32** | 0.697 / 0.256 ✓; "2.25x" ✗ (see MINOR-5) |
| 6.3 My | 4.41 | 0.676 | 0.242 | 2.25 | ✓ |
| 2 My | 1.40 | 0.0255 | 0.0034 | 0.085 | ✓ |
| N_e 1e5 held, 6.5 My | 2.60 | 0.281 | 0.065 | 0.94 | ✓ |

## Findings

### MAJOR-1: B's tag is keyed to Q158, which is not a B Statement quote. On Q157's own words, every reading is dialectic and non-sequitur.
- **Where:** claim file l.12 ("make 'nearly empty' literally close"; "Q157/Q158 'fills' = flux fill 0.697"), Readings table l.78-85; `R4-RHclose.md` l.70 (one literal band, F ≤ 0.10, for "never fills / nearly empty").
- **Evidence:** B's Statement block quotes Q157 only (l.29). Q158 ("the pipe was nearly empty", l.467) is not quoted there, and S1 scores a node on its Statement quotes. RHclose pooled the two phrases into one band. Q157's phrase is "the pipe that would finish them **never fills**". HL uses "fill" both as a matter of degree (Q152 "substantially fills"; Q153 ff. "a partly-loaded pipe") and as completion. HL's own domain sentence reads "k = μ holds only once the fixation-time distribution **has filled across its support**" (≈ l.431, fx 598-599). On that completion reading (F < 1, never reaching steady state) the clause is literally true on HL's input in every window: 0.697, 0.676, 0.281 and 0.025 are all below 1. Under rule C and RD it is therefore the reading under which the quoted statement is most defensible, and it is missing from the Readings table.
- **Consequence:** on the completion reading Q157 is dialectic, and RH6 gives no rhetoric exit. The clause carrying the verdict is then the conclusion it supports: "the neutral substitutions **cannot be finished**", "the neutral channel **closes**", "both … **shut inside the same lineage duration**". A partly loaded pipe finishes a fraction of the substitutions. HL says so itself in Q151 ("completions of mutations that entered the pipe long ago"), in Q156 ("loaded, at least partially") and of hominids specifically in Q153 ff. ("Grant the ancestral hominids their best case … a partly-loaded pipe"). That makes the conclusion N2b, and N2d at minimum. So the value is `non-sequitur` on F, D, 1e5, 2 My and the completion reading alike. The only reading that gives `holds` is the F-over-6.5-My rhetoric reading of the words "nearly empty", and those words are Q158's.
- **Fix:** add the completion reading to the Readings table (tag dialectic; clause literally true on HL inputs; conclusion non-sequitur under N2b/N2d). Score Q157 on its own words. Move the F-6.5 rhetoric tag to Q158 and RH-26, where it belongs. Either drop the "recorded alongside: holds" from B's field comment or mark it as a Q158 reading that cannot set B's field (RD: "extended readings … a different object … cannot set the verdict field").

### MAJOR-2: Even under the rhetoric tag, RH3 extracts the wrong core. The core of Q157 is the lineage closure, not B2.
- **Where:** claim file l.12 ("holds, SCOPED to the B2 statement only"); `ledgers/slips.md` RH-26 (core: "B2 (current-size confinement)"); `R4-RHclose.md` l.107-113.
- **Evidence:** RH3 says the dialectical core of a mixed statement "is extracted and scored under R1-U". Q157's checkable content is "on the same window" and "inside the same lineage duration". "Lineage duration" is a term HL defines: "Use the lineage duration, the full continuous ancestry, which in the case of the human lineage is roughly six and a half million years" (l.249, fx 350-352). B2 is a claim about **current size** (abstract, Q140). Making B2 the core swaps the author's lineage-level claim for a narrower one he did not make in this sentence. The lineage-level core is contradicted by HL's own Q140 ("residual drainage from the smaller populations they descend from"), Q151 ("their pipes short enough to fill"), Q152, Q153 ff. and Q156. That is the N2b basis R4-B2 already gave (R4-B2 l.25).
- **Self-classification (RH1, RH4: "classified by how it worked in its source"):** the lines straight after Q157 claim mathematical status for it. "It requires no charge against Kimura's algebra … it uses the field's own denominator … That question does not have a sociological answer … There is no algebra error to defend and no consensus to invoke against a multiplication anyone can perform" (≈ l.457-463, fx 624-633). The author presents the peroration as the result of a calculation. RH6's "remotely close" test is for tags that are *unclear*, and the source itself argues against the unclear tag here.
- **Fix:** set RH-26's core to "lineage closure (scored: non-sequitur, N2b within HL) plus B2 (holds at B2)". With that core, the rhetoric reading also gives B `non-sequitur`, or at worst `n/a` (MINOR-3), and never `holds`.

### MINOR-3: Like-for-like with C7, the rhetoric reading should give `n/a`, not "holds (scoped)".
- **Where:** claim file l.12 and Readings table row F; `R4-RHclose.md` l.101-110.
- **Evidence:** Under the same pre-registered mapping, Day's C7 went to rhetoric and from `non-sequitur` to **`n/a`**, with its core scored at C. B under rhetoric went to **`holds`**, with its core scored at B2. Both moves favour Day, so the treatment is asymmetric. The fair parallel is `n/a` at B, with the core's verdict kept at B2 and the lineage conclusion marked "no dialectical support offered" (RH3). RHclose's MAJOR-3 table already counts "the whole move" at B as Day's gain.
- **Fix:** in the Readings table, give any rhetoric reading that survives MAJOR-1 and MAJOR-2 the verdict `n/a (core at B2; lineage conclusion: no dialectical support offered)`.

### MINOR-4: The lead's suspicion (blog line vs abstract line) is answerable, but the claim file does not answer it on the record.
- **Where:** claim file l.12 (mentions quote 1 only) and l.29 ("**Candidate Statement**").
- **Evidence:** the field is set by neither of the two sentences the brief names.
  - **Quote 1** (blog, 2026-02-04) is rhetoric under RH-10 and comes from a different source seven months earlier. Under N2b scope ("same source and texts the claim cites") it cannot answer to HL, and under SC it would be scored on its own source if it were dialectic. It carries no verdict either way.
  - **Quote 2** (the HL abstract) is B2's own Statement quote and `holds` at B2 (R4-B2 l.22). Setting B's field from it would copy B2's verdict into the parent. It is the one choice that gives Day a bare `holds`, and the audit did not take it.
  - **Q157** is the only Statement quote that asserts B's own claim (lineage-level closure).
  - So the choice is forced by S1 and RH3, not by the result. The file does not say this, and it still labels Q157 a "Candidate", which leaves a Day-side reviewer free to argue the field rests on an unadopted quote.
- **Fix:** adopt Q157 as a Statement (drop "Candidate"). Add one line per quote to the field comment: Q1 rhetoric (RH-10, no verdict, softened in HL: versions/SC); Q2 is B2's Statement (holds at B2, not re-scored); Q157 sets B internal.

### MINOR-5: The "2.25x" label sits beside the wrong number.
- **Where:** claim file l.12 ("0.697, 2.25x the 0.30 edge") and Readings table row F (l.80); `R4-RHclose.md` l.160.
- **Evidence:** 0.697/0.30 = 2.32. The figure 2.25 is the 6.3 My value (0.676/0.30). It changes no tag.
- **Fix:** write "0.697 (2.32x the edge; 6.3 My: 0.676, 2.25x)".

### MINOR-6 (against the field's support list): reading D takes its measure from a later paper.
- **Where:** claim file l.12 (D is listed first among the readings that carry the field) and Readings table row D ("Day's own μ L ∫ F, Q34").
- **Evidence:** Q34 is from *Intrinsic Irrelevance* (Z22903977, 2026-09-22), not from HL (2026-08-27). HL's own measure of fill is F (RHclose l.57-61, four textual grounds). D is a reasonable reading of "nearly empty", but it applies a later document's quantity to an HL sentence, which is the cross-document move N2b scope forbids for premises. The field does not need D: the completion reading, 1e5 and 2 My carry it, and MAJOR-1 and MAJOR-2 carry it on every reading.
- **Fix:** label D "cross-document measure (Z22903977)" and do not list it first.

### NOTE-7: Day's later text gives up the empty start.
In the 2026-10-01 blog (B1d, R4-B2 l.32), Day writes "At the time of the CHLCA split, we can assume that it was full and 228,000 generations long". That is 4 × 57,143, HL's own census-derived N_e. The blog is cross-document, so it is not N2b-admissible and moves no internal verdict. It does show that the empty-pipe premise Q157 needs is not a position Day holds, which matters for which reading is "most defensible".

### Against the critics' own side (recorded as the skill requires)
- **NOTE-8: the error is narrow.**
  - The non-sequitur is an overreach of one clause: "closes / cannot be finished / shut" against HL's own concessions.
  - Day's mechanics stand: k = μ is a steady-state flux, and k(T) = μF(T) < μ from any start that is not full. On the completion reading the "never fills" clause is true on HL's inputs, and HL keeps B2 (`holds`).
  - Critics who asserted k = μ without the fill condition remain `contested` at B5.
  - The verdict says nothing about whether partial delivery suffices for the observed divergence. That is external and still pending (B1c, B4a).
- **NOTE-9: N2b exposure.** The verdict rests on Day's own honest concessions (drainage, partial load, Q152's "substantially fills"). X1 §N says openly that N2b penalises authors who concede more. A critic citing this verdict should say that Day's own text supplies the refutation, and that this does not show his pipe argument is empty.
- **NOTE-10: the 2 My window is HL's own ambiguity.** At l.416 HL calls the 2 My window "the entire lineage". On that window "nearly empty" is literally true (F 0.025). A reader who follows l.416 reads Q158 as true. The critic reply (that Q157 says "lineage duration", which l.249 defines as 6.5 My, and that HL itself calls the 2 My regime "thirty-five percent fill … a partly-loaded pipe") answers Q157, not every reader.
- **NOTE-11: quote 1 escapes.** Critics get no internal verdict on "the second is flat-out wrong". HL's later "The identity is not false" (≈ l.429, fx 597) is a versions entry, not an error.

## Counts
BLOCKER 0, MAJOR 2, MINOR 4, NOTE 5. All numbers in this review are post hoc recomputations of registered quantities; no new quantity was introduced. Direction: the evidence carries `non-sequitur`. MAJOR-1 and MAJOR-2 remove the basis for the Day-favourable "holds" recorded alongside. If the lead accepts them, B internal stops being reading-dependent in value, which changes the reading-dependent counts. That is for the lead and owner (D-24).

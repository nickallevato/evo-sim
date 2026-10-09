# Pre-registration: Day's announced computational result (UATV, 2026-10-09 evening)

*Written 2026-10-09, about 14:45 MDT (20:45 UTC), before the broadcast. Branch `research`. Nothing below was changed after the result became public; any later edit goes in a separate commit labelled "post hoc" (AGENTS.md hard rule 5). Author: one Claude agent, reading only files already in the repo plus the gitignored raw copies of the 2026-10-07 and 2026-10-09 posts.*

**Purpose.** Day has announced a new result, to be discussed on UATV tonight. This note records, before anyone has seen it, (1) what he has said about it, (2) what forms it is most likely to take, (3) what his model and the standard model each predict for each form, with the observations that would separate them, (4) a checklist for judging it, and (5) the errors each side is likely to make when reacting. The result is to be scored against this note, not against how it is presented.

**Labels used.**
- `[repo]`: a number already in the repo, with its file.
- `[derived]`: my arithmetic on repo numbers; the formula is given.
- `[inference]`: my own judgement or prediction, not taken from any source. These are the bets this note can lose.
- `[memory, unverified]`: background from the model's training data (pre-June 2026). Not to be used as evidence until it is retrieved and quoted.

**Rhetoric rule (new, 2026-10-09).** Each statement is classified as **dialectic** (a truth claim or argument, scored with the three verdicts) or **rhetoric** (persuasion, boast, framing, ridicule). Rhetoric is not fact-checked literally. Instead the note names its device, audience and function, and extracts any dialectical core it signals. The same rule applies to critics (section 5).

---

## 1. What is on record

All quotes are verbatim from the saved raw copies (gitignored; sha256 in `bib-day.md`). Q-ids refer to `docs/research/sources/quotes-day.md`. Three lines have no Q-id yet. I read them in the raw HTML (html-unescaped text, same paragraph as the cited Q-id), but they have not been machine-checked by the harvest script. They are marked **(no Q-id)**.

### 1a. The 2026-10-07 announcement ("An Epic Test")
Source `B2026-10-07-an-epic-test`, https://voxday.net/2026/10/07/an-epic-test/, raw `sources/raw/refresh-2026-10-09/day-recheck-an-epic-test/page.txt`.

| # | Quote | Locator | Class | Device / audience / function, or dialectical core |
|---|---|---|---|---|
| E1 | "we’re currently running an epic data analysis that is going to break new ground and might even reveal a few surprises" **(no Q-id; same paragraph as Q84)** | para 2 | **rhetoric** with a factual core | Device: teaser (anticipation, superlative "epic"). Audience: his readers. Function: build attention before release. **Core:** a *data* analysis (not only a model) was running on 2026-10-07. |
| E2 | "today I came up with a new disproof of the Post-Darwinian polythesis that has nothing to do with either MITTENS or Reverse-MITTENS" (Q84) | para 2 | **dialectic** (announced, content withheld) | A *second* item, distinct from the data analysis. "Reverse-MITTENS" is undefined in every harvested text. Placeholder `ROOT-newdisproof-pending`. Scored `pending` until published. |
| E3 | "is very nearly as conclusive as both of them, and is even easier to test empirically" **(no Q-id; same sentence as Q84)** | para 2 | mixed | "very nearly as conclusive" is rhetoric (self-rating). **Core:** the disproof is said to be empirically testable, which commits Day to naming an observable. |
| E4 | "So, we have achieved triangulation, even as we await Erika and the Evo-Avengers to launch their no-doubt very impressive assault on Probability Zero, MITTENS, and your woefully outnumbered, outcredentialed dark lord." | para 3 | **rhetoric** | Devices: irony and mock humility ("outnumbered, outcredentialed"), an in-group persona ("dark lord"), and "triangulation" as a frame from his Triveritas heuristic. Audience: his readers, and critics by way of provocation. Function: cast the critics as late and outmatched. No core beyond "triangulation", which he defines in 1c. |

### 1b. The 2026-10-09 post "The Irrelevance of EES"
Source `B2026-10-09-the-irrelevance-of-ees`, https://voxday.net/2026/10/09/the-irrelevance-of-ees/ (published 09:13 UTC; the page shows a later "updated" time), raw `sources/raw/refresh-2026-10-09b/day-post-2026-10-09-the-irrelevance-of-ees/page.html`.

| # | Quote | Locator | Class | Device / audience / function, or dialectical core |
|---|---|---|---|---|
| I1 | "all of the ESS arguments are focused on the adaptive space that natural selection can effect, which a) are at most 2 percent of the average genome and b) don’t even begin to address the same fixation problem that eliminates the possibility of natural selection as a significant generative force." (Q122) | paragraph beginning "The reason that it took me less than 30 seconds" | **dialectic** | Two claims. (a) An adaptive fraction of "at most 2 percent": numeric, uncited, so F = `unverifiable` under rule F. (b) EES does not address the fixation problem, which assumes the claim under audit (circular as a reply to EES; refresh-2026-10-09b D-2). "ESS" means EES here (C charity: the post's heading and the Hilbert text say EES). |
| I2 | "it took me less than 30 seconds to determine that ESS is as irrelevant as most of the Intelligent Design concepts" | same paragraph | **rhetoric** | Device: speed boast and dismissal. Audience: readers, and the EES advocate Hilbert. Function: signal that EES is not worth engaging. Not scored. |
| I3 | "This is why the larger part of the science, the philosophy, the theology, and the general discussion of evolution has been an irrelevant waste of time, money, effort, and ink for the last 160 years." | same paragraph, last sentence | **rhetoric** | Device: hyperbole and sweeping dismissal. Not a testable claim. |
| I4 | "I had already conclusively proven two things: evolution by natural selection is mathematically impossible. evolution by neutral drift is both mathematically and empirically impossible." | the list after I1 | **rhetoric** framing **dialectic** claims | "conclusively proven" is a self-assessment (rhetoric). The two cores are ROOT's branches A/F/G/H (selection) and B/C (drift), already in the tree and mostly `contested` / `pending`. Nothing new to score. |
| I5 | "But now I have conclusively proven one more thing: natural selection is empirically irrelevant as an evolutionary mechanism." (Q123) | final paragraphs | **dialectic** core inside rhetoric | **Core:** an *empirical* claim that selection accounts for a negligible share of evolutionary change. "Conclusively proven" with no exhibit is rhetoric. Internal = `pending`; nothing can be scored before release. C charity: Day elsewhere grants selection a "real function, keeping the genome from degrading" (Q89), so the charitable reading is "irrelevant as a *generative / adaptive* mechanism", not "purifying selection does not exist". |
| I6 | "Because there is one thing game designers have that no scientists do. And that is unlimited 24-7 access to 96 cores with 512GB RAM and a multicore monster GPU with 96GB RAM" (Q124) | last paragraph | **rhetoric** with a factual core | Device: an outsider-versus-establishment contrast plus ethos ("game designers"). "no scientists do" is hyperbole: **do not fact-check it literally**. Audience: his readers. Function: explain why an amateur can do what academia has not. **Core:** the analysis is computational and resource-heavy (96 cores, 512 GB RAM, a GPU with 96 GB). That is a statement about resources, not method. 512 GB RAM fits whole-genome alignment or large in-memory datasets better than a typical population simulation `[inference]`. |
| I7 | "as well as the knowledge of how to effectively make use of that kind of computing power. Which is something we’ll be discussing with the people who made it possible on UATV tonight." **(no Q-id; same paragraph as Q124; Q124's quote stops before it)** | last paragraph | announcement, plus ethos | Logistics: it will be discussed tonight, with collaborators or sponsors ("the people who made it possible"). Not scored. |

### 1c. Related posts that day and the day before
| # | Quote | Source / locator | Class | Core or function |
|---|---|---|---|---|
| M1 | "at which point we realize that Yoo et al can’t possibly be correct because 7 billion x 0.0857 is not 410,000,000 but 599,900,000." (Q118) | Mailvox: Invoking the Triveritas, 2026-10-09, post body, final third | **dialectic** | The product is right. "7 billion" is undefined and 8.57% is uncited (not found in CSAC or Yoo; Q118 note). This signals that the divergence total may be re-sized upward (~600M bp). |
| M2 | "But those partial genomes were at least 8.57 percent different based on size alone!" (Q119) | same, CSAC paragraph | **dialectic** + rhetoric ("misleading garbage" follows) | Core: an assembly-size difference treated as divergence. F = `unverifiable`. |
| M3 | "Yoo reported a total genomic difference of 410 million base pairs." (Q120) / "I therefore divided that difference in two" (Q121) | same | **dialectic** | Day's own words confirm that 205M "fixations" = 410M **base pairs** / 2 (A3x unit mismatch, now in his words). |
| M4 | "The fact that this doesn’t matter in the slightest to my mathematical disproof of natural selection never occurs to them" | same paragraph as Q120 | **dialectic** (sensitivity claim) | **Partly fair to Day** under R1: a factor of 2 on a ~1e6× shortfall does not flip his stated conclusion. It does matter for the comparison with neutral theory (A3d). |
| M5 | "And note that 600M is just the size difference alone, and therefore doesn’t even begin to take into account the original 1.06 percent difference that was focused on areas of alignment between the two genomes." | same, next paragraph | **dialectic** | **Prediction-relevant:** Day will add the size difference (bp) to the aligned SNV divergence. That is a double unit mix (bp + per-site rate). |
| M6 | "there is still work to be done on the actual size of the chimp-human divergence" | same, closing paragraph | **dialectic** (programme statement) | Signals that genome-scale re-measurement is in progress. |
| M7 | "the butterfly collectors like the Evo-Avengers"; "with the stunned incomprehension of proto-chimps trying to master the mystery of fire" | same, opening and middle paragraphs | **rhetoric** | Devices: ridicule and caricature (taxonomists without mathematics). Audience: his in-group. Function: inoculate readers against critics' replies. Not scored. |
| M8 | "Actually, based on my most recent work, I genuinely believe they will all eventually come around to my way of thinking with regards to evolution and population genetics." | "No Reconciliation", 2026-10-06, post body, Day's reply after the quoted critic line (raw `refresh-2026-10-09b/day-post-2026-10-06-no-reconciliation/page.html`) **(no Q-id)** | **rhetoric** (prophecy) | Core: "most recent work" existed by 2026-10-06. |
| M9 | "I know, to the very base-pair, precisely what level of influence natural selection, EES, and every other adaptive mechanism has had on six different genomes." (Q82) | Dembski thread, comment 356282255, 2026-10-08 | **dialectic** core + rhetoric (certainty) | **The strongest hint about the analysis:** a per-base-pair attribution of "adaptive" influence across **six genomes**. "Six" is undefined. Yoo 2025 has T2T assemblies of six non-human apes plus human `[repo: A3x1 says Yoo's 1,140 inversions are "across six apes"]`. In tension with "I have no idea" about EES (refresh D-1). |
| M10 | "In any population over 10,000, neutral substitution will not fixate at all." (Q93) | McCarthy thread | **dialectic** | A sharp, simulable prediction of Day's drift model (used in 3B below). |
| M11 | "Once corrected, Term 3 still limits adaptive substitution rate at ~10⁻¹², but total substitution rate is only governed by Terms 1 and 2" (Q67) | retraction post, 2026-05-07, ¶4 | **dialectic** | Day's own earlier position already separates adaptive substitution (negligible) from total substitution. Q123 is continuous with it. |

**Reading of the record** `[inference]`: the 10-07 "data analysis" and the 10-09 "empirically irrelevant" claim are very probably the same item: refresh-2026-10-09b already identifies them. The 10-07 "new disproof" may be a different item. Most of the words point to an *empirical, genome-scale* analysis ("data analysis", "empirically", "to the very base-pair", "six different genomes", "actual size of the chimp-human divergence", 512 GB RAM), not a pure population-genetic simulation. The GPU and "game designers" point to simulation or to heavy compute generally.

---

## 2. Likely forms of the analysis (ranked)

Probabilities are my subjective weights `[inference]` and sum to about 1 across A–E. F is orthogonal: it describes how the analysis was done, not what it is.

| Rank | Form | Weight | Evidence from his words | Evidence against |
|---|---|---|---|---|
| **A** | **Comparative-genomics attribution over T2T ape assemblies.** Partition human/ape differences into "adaptive space" (genes, conserved or functional elements) and the rest, count how many fall in each, and possibly re-size the total divergence. | 0.40 | M9 ("to the very base-pair … six different genomes"); I1 ("at most 2 percent"); I5 ("empirically"); E1 ("data analysis"); M1/M5/M6 (re-sizing the divergence); 512 GB RAM | "game designers" and the GPU fit simulation better |
| **B** | **Forward population simulation at human scale** (GPU or many-core), with selection and possibly drift, under Day's parameters, reporting that selected fixations are negligible (and/or that drift fails) | 0.25 | I6 (GPU, "game designers", "how to effectively make use of that kind of computing power"); Day's earlier models are computational | "empirically irrelevant" and "data analysis" are not words for simulation output |
| **C** | **Ancient-DNA time-series selection scan** (AADR), claiming selected trajectories or sweeps are a negligible share of allele-frequency change in the last ~7–10 ky | 0.15 | Day's prior aDNA work (C, C6, Z23046531); refresh-2026-10-09 (iii) flagged a possible aDNA follow-up; "empirically" | Q82's "six different genomes" does not fit a single-species time series |
| **D** | **Cross-species scaling** (MITTENS over many species pairs; 2nd-edition "18 species pairs", Q91) extended to measure selection's share | 0.10 | Q82 ("six genomes"); versions.md records three scope statements | No new hint since Q91 |
| **E** | **Something else**, including the separate 10-07 "new disproof" being presented instead (E2) | 0.10 | E2 is unpublished and its content unknown | — |
| **F** | *Orthogonal:* **LLM-assisted pipeline** (code, annotation or interpretation written with an LLM; a local model on the 96 GB GPU) | P(LLM involved) ≈ 0.7 | Day's Zenodo papers list an AI co-author ("Claude Athos"; HANDOFF "Things a reader should weigh"); a 96 GB GPU is typical of local LLM inference `[inference]` | Not stated for this analysis |

---

## 3. Prediction tables

Columns: what Day's model predicts; what the standard model predicts (as the critics state it, using the best numbers already in the repo); whether the observation discriminates; and what each side should concede if it appears.

### 3A. Comparative-genomics attribution (weight 0.40)

| # | Observable | Day's model | Standard model | Discriminates? | Concession if observed |
|---|---|---|---|---|---|
| A1 | Share of human–ape differences in "adaptive space" (coding / functional annotation) | ≤ 2% (I1) | **Also small.** Neutral theory holds that most differences are neutral. Constrained fraction 8.2% (Rands 2014, as recorded in `R5-draft.md` V19; source not retrieved in `sources/`). Coding is ~1–2% of the genome (standard value, exempt under rule F). Observed differences are depleted in constrained sequence, so the share in coding sequence should be ≲ 1% of differences `[inference]`. | **No, at the ROOT level.** Both models predict a small share. Day's "≤ 2%" sits inside the standard expectation. | **Critics:** concede that a ≤ 2% result agrees with neutral theory and does not refute it; do not dispute it for being Day's. **Day:** concede that this result says nothing against branch B and moves the whole question there (see A4). |
| A2 | Share of the adaptive-space differences that were **positively selected** | ~0 (Q67: adaptive rate "~10⁻¹²"; I5) | Coding α = 0 to 0.4 (CSAC ≈ 0; Boyko 0.10–0.20; Uricchio 0.135; Eyre-Walker & Keightley up to 0.40; `prior-art.md` PA-19). Adaptive amino-acid substitutions per lineage ≈ 1.3×10³–1.2×10⁴ (GAP-01 / H3). Classic sweeps rare: Hernandez 2011 trough test; < 10% of human-specific amino-acid substitutions strongly favoured (GAP-02; PA-22). | **Weakly.** α ≈ 0 is itself a published estimate (CSAC). Only a claim of α ≪ 0.01 with a stated estimator separates them, and MK estimates are biased downward by slightly deleterious mutations (Messer & Petrov 2013, PA-19). | **Critics:** if the analysis uses a standard estimator (MK / DFE-α) and gets α ≈ 0, concede that it agrees with CSAC, not that it is wrong. **Day:** an annotation overlap is not an α estimate; concede if no polymorphism/divergence contrast was used. |
| A3 | Non-coding adaptive share a_nc | not separately stated; "at most 2 percent" covers everything | **Unmeasured** genome-wide (PA-19; GAP-01). H3's flip lies at a_nc ≈ 0.01–0.6%, below any estimator's resolution. | **Yes, if he measures it.** This would be a real contribution. a_nc ≥ ~1% would be unpayable under H3's hard-selection model at R ≤ 3–4 (D ≥ 5). | **Critics:** a sourced a_nc ≥ ~1% helps Day on H (cost of selection), not on A/B. **Day:** a_nc ≲ 0.01% makes the adaptive count payable at R ≈ 1.2–3 (H3); concede H on those terms. |
| A4 | What "selection irrelevant" implies for ROOT | ROOT holds: selection is irrelevant (Q123) and drift is impossible (I4, Q79) | Most differences are neutral and fixed at k = μ (B3a; Day conceded on 2026-08-27; HANDOFF), from a full ancestral pipeline (B1; Day: "full, but much shorter", 2026-10-01) | **The result decides only half.** ROOT then rests entirely on branch B. | **Day:** the analysis supports the critics' neutralist core. "Natural selection is empirically irrelevant" for most of the divergence is the neutral theory's own claim, so the result cannot strengthen ROOT unless B is won separately. **Critics:** concede that if ≤ 2% of differences needed selection, the selection-only framing of MITTENS (A: every difference a selected fixation) was always the wrong target for *both* sides. Many critics argued against MITTENS as if adaptation were the issue. |
| A5 | Total divergence, if re-sized | ≥ 410M bp; possibly ~600M bp "size difference alone" plus the 1.06% aligned divergence (M1, M5) | Events: 42.10M total, 21.05M per lineage (GAP-07b, hg38–panTro6, not T2T). Bases outside aligned blocks: 261 Mb (201 Mb without hg38 centromere models). SDR ≈ 327 Mb per lineage average (Yoo; `parameters.yaml`). SDRs are mostly satellite and heterochromatin (GAP-07). Polymorphic share 15.6% of human-derived differences (GAP-07c). | **Yes, on the unit.** Any bp total will be ~7–14× the event count (GAP-07b bracket). | **Critics:** if a T2T event count per lineage comes out well above 21M (say > 30M) `[inference: threshold]`, concede GAP-07b's non-T2T undercount (its Day-favourable bracket, 7.2–9.5×). **Day:** if both bp and events are reported, concede that the "fixations" figure is the bp figure (Q120–Q121 already say so) and that G_f counts events (GAP-07b). |
| A6 | Assembly size difference counted as divergence | yes: "8.57 percent different based on size alone" (Q119) | A size difference between assemblies includes assembly gaps (2005 "partial genomes"), satellite arrays and lineage-specific expansions. It is not a count of fixation events. | **Yes, on method.** | **Day:** concede that a size difference is not a mutation count without an event model. **Critics:** concede that size-difference sequence is real divergence and that the SV / bp weighting is Day's stated position (Q99), not an error of arithmetic. |
| A7 | "Six genomes" | per-base-pair attribution on six genomes (Q82) | Yoo 2025 gives six non-human ape T2T assemblies plus human `[repo: A3x1]` | Descriptive | Either side: check which six genomes, and whether the attribution is per lineage or pairwise. |

**Headline prediction for A** `[inference]`: Day reports that ≤ ~2% of human–ape differences fall in coding or functional sequence, and presents this as selection being "empirically irrelevant". That number will agree with standard expectations. The point of disagreement will be the inference from it to ROOT, which needs branch B.

**Side derivation, a point for Day** `[derived]`: if Day's 2% were all adaptive *substitutions*, K_a would be 0.02 × 17.5M = 3.5×10⁵ (SNV basis) or 0.02 × 205M = 4.1×10⁶ (bp basis). H3 puts the minimum R for 10⁵ at 5.4×10⁴ (D = 20) and finds 10⁶ unpayable, so on H3's hard-selection model even 2% would be far beyond the cost of selection. The critics' answer is that "in adaptive space" is not "adaptively fixed" (A2). Both points should be recorded.

### 3B. Forward population simulation (weight 0.25)

| # | Observable | Day's model | Standard model | Discriminates? | Concession |
|---|---|---|---|---|---|
| B1 | Beneficial fixations per lineage in 252,000 generations | ≤ T/G_f = 252,000/1,322 = 191 `[derived; parameters.yaml]`; MITTENS achievable 191–2,407 (GAP-04) | Rate = 2N·U_b·u(s) independent of latency (F1: 0.3960 predicted, 0.3972 ± 0.0018 simulated). Interference cap W&B R/2 ≈ 4.4–4.8M per lineage (GAP-04). Cost-of-selection cap: K_a 10³–10⁴ payable at R ≈ 1.2–3; 10⁵ needs R ≈ 5.4×10⁴ (H3, hard selection, D = 20). | **Yes, if the inputs (U_b, s, R) are published.** The answer is set by inputs, not by the engine. | **Critics:** if a sim with sourced U_b, s, R and recombination yields ≪ 10³ adaptive fixations, take it seriously; H3 already shows the cost binds above ~10⁴–10⁵. **Day:** if the count scales with N·U_b (pipelining), concede that the serial reading T/latency is not a throughput bound (F1). |
| B2 | Neutral fixations at Nₑ > 10,000 | "will not fixate at all" (Q93) | k = μ per site per generation for any N, from an equilibrium start (B1: 99.3–1,005 vs U·T). Per-lineage neutral count by rate × time ≈ 9.6–10.4M (GAP-07). From an empty start, Day's U∫F applies: about U(T − 4N), a 15.9% loss at Nₑ = 10⁴ (B6a). | **Strongly**, and it turns on the start state. Zero neutral fixations in 252k generations at Nₑ = 10⁴ would contradict B1 and every textbook baseline. Near-zero at Nₑ ≥ 10⁵ (4Nₑ ≥ T) happens only from an empty start. | **Day:** zero neutral fixations from an *equilibrium* start would be a bug. If the sim started empty, concede that the result is the empty-pipe boundary case he withdrew on 2026-10-01. **Critics:** concede that the Hard Limits tail exp(−π²Nₑ/G) is correct (B2a) and that at T ≪ 4Nₑ, *new* mutations rarely complete. |
| B3 | Scaling | unknown | Scaling by f (N/f, μf, sf, T/f) is valid for neutral and weak cells but **not for strong selection**: f = 10 turns s = 0.01 into 0.1 (D15 status: S2 +27% at f = 10; f = 100 breaks it) | **Method check, not a prediction** | Either side: an unscaled-vs-scaled comparison must be shown for the selected cells. |
| B4 | Model class | LTEE-calibrated G_f, possibly clonal | recombining diploid; clonal G_f does not transfer (A5f; F2: free recombination removes the clonal-interference ceiling in the tested regime) | Yes | **Day:** a clonal model applied to humans repeats A5f. **Critics:** a recombining model that still shows the cost of selection binding helps Day on H (H3). |

**Headline prediction for B** `[inference]`: if it is a simulation, its result will be fixed by its inputs (start state, U_b and s, a cost or fitness model, recombination, scaling). Published inputs will let it be reproduced within days on na-workhorse. Unpublished inputs will leave it unscorable (internal `pending`).

### 3C. Ancient-DNA selection scan (weight 0.15)

| # | Observable | Day's model | Standard model | Discriminates? | Concession |
|---|---|---|---|---|---|
| C1 | Number of SNPs with a significant selection signal in ~7–10 ky of European aDNA | negligible, or zero | **Also a small fraction** of ~1.1M SNPs. A few strongly selected loci are expected: keruru's allele table has SLC24A5 rs1426654 at 0.87, 0.97, 0.90, 0.91 across four bins (refresh-2026-10-09 (ii)). Published scans report from about a dozen to a few hundred loci `[memory, unverified]`. | **Only in count:** 0 against tens to hundreds. A "negligible fraction" is predicted by both. | **Day:** zero signals at known loci (LCT, SLC24A5, SLC45A2) would point to a pipeline problem `[memory, unverified, for the locus names other than SLC24A5]`. **Critics:** concede that "selection explains a negligible fraction of SNP-level frequency change" is the standard expectation, not a refutation. |
| C2 | Post-6000 BP fixation events; completions | ~21; 1 and 3 completions (C, C6) | Literal reading on real AADR: 4,957 of 62,757 eligible (v62), 3,649 of 48,888 (v66); completions reproduce in kind, 2 and 0 (C1d). Neutral model: 908–3,925 at Nₑ 1e4–2e4; ~21 only at closed Nₑ ~1–3×10⁵ or a growth schedule (C1c; `holocene-ne.md`). | **Yes for the pipeline; no for Nₑ** (the literature does not decide Holocene Nₑ: `holocene-ne.md` §1.4) | **Day:** a new aDNA result must publish the pipeline (C1d: no code found; event total 3.6× off). **Critics:** concede that Day's start table reproduces to 0.4 points and that his events are completions of alleles near fixation (98.8%; C1d). |
| C3 | Temporal Nₑ | near 2 (excluded) or used circularly (C5a) | 7.8k–9.7k (keruru; replicated 1–8%; corrected 9.7k/10.5k), a lower bound on drift Nₑ (C1d) | Yes | As in C1d. |

### 3D. Cross-species scaling (weight 0.10)
| # | Observable | Day | Standard | Discriminates? | Concession |
|---|---|---|---|---|---|
| D1 | Shortfall across species pairs | orders of magnitude for every pair (Q91, 2nd-edition abstract) | Neutral divergence d = 2μT + θ_anc (B4a). It scales with generations, not with any selection rate. Pairs with short generation times and large Nₑ are not short. `[inference]` | Yes, per pair, if generation times and μ are sourced | **Day:** a pair where the required count is ≤ T/G_f would falsify "every pair". **Critics:** a pair whose neutral expectation undershoots the observed divergence after θ_anc would be a real clock problem (GAP-06 / B4a: the k = μ route undershoots by ~2×). |

### 3E. Other (weight 0.10)
No table. If the 10-07 "new disproof" (E2) is presented instead, register its predictions *before* checking it, following the lifecycle in AGENTS.md.

### 3F. LLM-assisted pipeline (orthogonal)
Do not use LLM involvement as grounds for a verdict, in either direction. Check for the failure modes this audit has already seen in this corpus: numbers absent from the cited source (the 410 and 187 in Yoo, A3x1; the 8.57% in CSAC, Q119), unit swaps (bp as fixations), and summarised counts that the stated method does not reproduce (C1d 3.6×). These are checks on the output, whoever or whatever wrote it.

---

## 4. Methodological checklist (for use once the result is released)

### 4a. Inputs that must be published for replication
| Input | Why it matters here | Repo reference |
|---|---|---|
| Nₑ (and N) and any trajectory | sets the timescale; census N, not Nₑ, sets neutral p_fix (1/2N) | B3a, B7, C1c, `holocene-ne.md` |
| μ per site per generation | k = μ; the 1.1–1.5e-8 range | `parameters.yaml` mutation |
| Generation time, and T in generations | 20 / 25 / 32.5 y; 252,000 vs 325,000 vs 450,000 | `parameters.yaml` |
| DFE: sign and scale of s; U_b | s = 0.001 misread (Zeng, negative selection, F3a) | F3a, V7 |
| Recombination map length | R = 35–38 M; clonal vs recombining | GAP-04, A5f |
| Scaling factor f and whether s was scaled | invalid for strong selection | D15 status |
| Burn-in / initial state | empty vs equilibrium pipeline | B1, B1b, B1d |
| Replicates and seeds | reproducibility | — |
| Definition of "fixation" | ≥95% read frequency vs strict; 100% vs > 90% | A2b, C |
| Definition of "selected" / "adaptive space" | annotation overlap ≠ selection ≠ adaptive substitution | A2 above, PA-19 |
| Unit counted: events or base pairs | A3x / GAP-07 | GAP-07b |
| Per lineage or pairwise | the factor of 2 (A3d; Q121) | A3d |
| Genome assemblies and versions; alignment tool and parameters (form A) | T2T vs older assemblies; aligned vs non-1:1 sequence | GAP-07b |
| aDNA release, sample filters, bins (form C) | v62 vs v66; 8,738 vs 8,808 samples | C1d |
| Code | none was found for Z23046531 (C1d) | — |

### 4b. Known traps (check each explicitly)
1. **Empty-start pipeline (B1).** Does the population start with zero standing variation? If so, the shortfall is the counterfactual boundary case. Day himself replaced it on 2026-10-01 ("full, but much shorter").
2. **Base pairs vs events (A3x / GAP-07).** Any "fixations" figure built from bp (410M, 600M, 205M) is 7–14× the event count. Q120–Q121 confirm the 205M is bp / 2.
3. **Per lineage vs pairwise.** Divergence counts both lineages, plus ancestral polymorphism (d = 2μT + θ_anc, B4a). 15.6% of human-derived differences are still polymorphic (GAP-07c).
4. **Latency vs throughput (F1).** T / t_fix is not a rate bound. Check whether a "fixations possible" number divides time by fixation duration.
5. **Unscaled vs scaled N.** Scaled runs must not be compared with unscaled thresholds (e.g. "N > 10,000", Q93) without rescaling. Strong-selection cells do not scale (D15).
6. **"Adaptive space" vs "adaptively fixed".** Overlap with an annotation is not evidence of selection (α estimators need polymorphism vs divergence, PA-19).
7. **Circularity (refresh D-2).** If the analysis assumes the fixation shortfall to conclude that selection is irrelevant, the conclusion is N (non-sequitur, circular) under rule N.
8. **Assembly size ≠ divergence (Q119).** Gaps in the 2005 assemblies and satellite arrays inflate size differences.
9. **Purifying vs positive selection.** "Selection is irrelevant" must say which kind. Day grants purifying selection a "real function" (Q89).
10. **Clonal calibration (A5f).** An LTEE G_f applied to a recombining diploid.

### 4c. What replication would cost (order of magnitude only; all `[inference]`)
| Form | Workhorse (12 cores, 14 GB RAM; ≤ 4 processes per agent) | Cloud |
|---|---|---|
| A, using published alignments (UCSC nets, Yoo's released alignments) | hours. GAP-07b already ran this way. | not needed |
| A, new T2T pairwise whole-genome alignments | probably RAM-limited at 14 GB for whole-genome pairs; tens of CPU-hours per pair | ~$10–$100 per pair on a 32–64-core, 128–256 GB instance |
| A, a six- or seven-genome progressive multi-alignment | not feasible (RAM) | ~10³–10⁴ CPU-hours, ~$10²–$10³. This is the job Day's 512 GB machine suits. |
| B, scaled (f ≈ 10, neutral or weak selection) | hours to a day per parameter grid (cf. D15 `valid`) | not needed |
| B, unscaled human scale (N = 10⁴, 3 Gb, 252,000 generations) with a neutral overlay | days to weeks per replicate; feasible only with tree-sequence recording plus overlaid neutral mutations | similar wall time; parallel replicates only |
| C, aDNA rerun | hours (C1d was run there) | not needed |
| D, per-pair arithmetic | minutes | — |
| A GPU-specific code path | not reproducible on workhorse (no GPU); only reimplementation on CPU | ~$1–$3 per GPU-hour |

Day's stated machine has ~8× the cores and ~37× the RAM of workhorse `[derived: 96/12, 512/14]`. That matters only for forms A (multi-genome alignment) and unscaled B.

### 4d. Scoring protocol on release
1. Save the broadcast and any post, paper or code as a new fetch (own directory; untrusted). Record a timestamp and sha256.
2. Transcribe verbatim quotes with locators (video timestamps). Classify each as dialectic or rhetoric *before* scoring. Rhetoric gets device / audience / function, and its dialectical core is extracted.
3. Map the result to a form (A–E) and compare it with the tables above. Record hits and misses of this note's `[inference]` predictions honestly, including where this note was wrong.
4. Score only the dialectical core under the X1 verdict rule (R1, S, SC, N, F, U, C). Nothing published = `pending`, not `non-sequitur`.
5. Pre-register any replication script before running it (lifecycle, AGENTS.md).

---

## 5. Symmetric failure modes

### 5a. What would be a Day error (judged by the result, not the presentation)
- Treating base pairs, or an assembly-size difference, as fixation events (A3x; Q119–Q121).
- Inferring "selection is irrelevant, therefore ROOT" without winning branch B. On the audit's current record, B goes against him on k = μ (B3a, conceded 2026-08-27) and on the start state (B1, withdrawn 2026-10-01).
- Equating "in adaptive space" with "requires selection", or a ≤ 2% annotation overlap with α ≈ 0.
- Running a simulation from an empty start, or with scaled strong selection, and reporting the result as human-scale.
- Claiming "conclusively proven" with no inputs, code or data released. Internally that is `pending`, not "holds"; rhetorically it is an appeal to authority (his own).
- Using circular premises (the "same fixation problem" as input; refresh D-2).
- Not reconciling the new figure with his three prior scope statements (mammals; six genomes; 18 pairs; versions.md).

### 5b. What would be a critic error in reacting
- **Literal fact-checking of rhetoric:** e.g. "scientists do have HPC clusters" against I6, or "it took more than 30 seconds" against I2. Both lines are rhetoric; reply to the dialectical core.
- **Genetic fallacy or ad hominem:** dismissing the result because Day is a game designer, because it is on UATV, because it is not peer-reviewed, or because an LLM helped. None of these bears on whether the counts are right. (Hilbert's "crank" replies, reposted in the EES post, are the model of what not to do; they are rhetoric with no dialectical core.)
- **Disputing a result the standard model predicts.** If Day finds ≤ 2% of differences in adaptive space, or few aDNA selection signals, that *agrees* with neutral theory. Calling it wrong would be an error; the right response is "agreed, now branch B".
- **Moving the goalposts without numbers:** "soft sweeps / standing variation / EES" offered with no quantity (G2c is unquantified; PA-38 says the regime is unresolved). That is the same flaw Day is charged with on EES (Q80 admission test).
- **Overclaiming the critics' own numbers:** k = μ stated universally (it fails with overlapping generations and fluctuation, B3b); Nₑ = 10⁴ as uncontested (it is contested-standard, rule F); coding α up to 0.4 quoted as if genome-wide (PA-19 is coding only); the 38M = 35M double count (HANDOFF).
- **Calling a refutation before the inputs are released**, or scoring the broadcast rather than the method.
- **Ignoring a valid point for Day:** for example, if a measured a_nc ≥ ~1% emerges, it favours Day on H (H3); if a T2T event count exceeds 21M per lineage, GAP-07b's ratio moves in his favour.

---

## 6. Who this helps

**Day.**
- An announced analysis with released inputs and code would be the first item in this corpus that the audit could replicate end to end on his own terms. The audit has repeatedly credited what reproduces: the start table (C1d), Hössjer's arithmetic (D15 baselines), the LTEE G_f, and the Hard Limits tail.
- If the analysis *measures* a non-coding adaptive share, it supplies the input that H3 found decisive and that no side has supplied (GAP-01). Values ≳ 1% favour Day on the cost of selection.
- A T2T event count would test GAP-07b's non-T2T bracket, whose Day-favourable end is 7.2×.
- M4 is partly right: halving does not flip his stated conclusion (R1).

**Critics.**
- Q123 and Q67, read charitably, put Day's view of selection's share close to the neutralist view the critics hold ("most differences are neutral"). If the analysis confirms a small adaptive share, it supports their core claim, and the dispute reduces to branch B. There the audit's checks currently favour the critics on k = μ (B3a) and on the full ancestral pipeline (B1, B1d), and the Holocene Nₑ question is open (C1c).
- Q120–Q121 put the bp-as-fixations unit mismatch (A3x) in Day's own words.
- The critics' best reaction is to name the observable each form predicts (section 3) and ask for the inputs (section 4a), not to rebut the presentation.

**Both.**
- Under any of forms A–C, the item that would move the audit is a number neither side has supplied: the adaptive share of human–ape differences, measured with a stated estimator. The pre-registered expectation `[inference]` is that the headline figure lands inside the standard range, and that the real contest is over what follows from it.

---

## Things I was unsure of
- Whether the 10-07 "data analysis" and "new disproof" are one item or two (I treat them as two; refresh-2026-10-09b ties the analysis to Q123).
- What "six different genomes" and "Reverse-MITTENS" mean (undefined in every harvested text).
- The ranking weights in section 2 are subjective.
- The 8.2% constraint figure (Rands 2014) is recorded in `R5-draft.md` V19, but no source entry or quote was found in `sources/`; it needs a locator before use. The coding fraction (~1–2%) is used as a standard value.
- The cost estimates in 4c are orders of magnitude from general knowledge, not measured.
- Three lines (E1, I7, M8) were read in the raw HTML but have no Q-id yet; they should be added to `quotes-day.md` by the harvest script.

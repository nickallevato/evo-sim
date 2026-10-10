---
id: ROOT-FM
title: "Day, 'The Fourth Mechanism': substitution density along the T2T ape genomes is overdispersed and clusters into 'mesas'; sigillation (deliberate genomic modification) as a possible further mechanism; neither selection nor drift 'can still be considered viable'"
side: day
branch: ROOT
parent: ROOT
edges: [{type: supports, target: ROOT}]
load_bearing: true  # FM10 is a ROOT-level conclusion ("neither natural selection nor neutral diffusive drift can still be considered viable candidates"); the step from "mesas exist" to "both non-viable" is the load
sourcing: firsthand
status: extracted
verdicts:
  internal: pending      # numbers FM3 (80x) and FM5 (mesa vs MITTENS ceiling and Haldane) have no stated statistic, units or counts; the step from the pattern to FM10 is not derived in the text
  fidelity: pending      # the "Haldane" maximum and the "MITTENS fixation ceiling" figures are unverifiable until the mesa counts are released; Yoo 2025 / Progressive Cactus are named data sources (cited, retrievable)
  external: pending      # no code, mesa coordinates, window size or dispersion statistic released (refresh 2026-10-10); the data are public, so a replication is possible
---

## Statement (verbatim)
> The substitution density across the genome is massively overdispersed, more than 80 times more variable than a uniform-rate process predicts.

Source: [Day, "The Fourth Mechanism" (blog)](https://voxday.net/2026/10/10/the-fourth-mechanism/), 2026-10-10, ¶4 (Q164, FM3)

> Dense regions cluster next to other dense regions, forming contiguous blocks of elevated substitution with sharp boundaries in a pattern we call mesas.

Source: same, ¶4 (Q165, FM4)

> A single mesa on a single chromosome shows an excess of human-lineage substitutions that exceeds both the MITTENS fixation ceiling and the maximum that natural selection can theoretically fix across the entire genome according to Haldane.

Source: same, ¶4 (Q166, FM5)

> I propose the term sigillation for the hypothesis that some of these mesa regions represent deliberate genomic modification: discrete engineering events that wrote contiguous blocks of change into one dominate lineage.

Source: same, ¶6 (Q168, FM7); hypothesis, explicitly open. Hedge: "Sigillation is no more proof of IGM than relictation is. But it may be initial evidence of IGM." (Q170, FM9)

> What we do know is that neither natural selection nor neutral diffusive drift can still be considered viable candidates. And there is no need to take my word for anything with regards to this, all of the data has been provided by the T2T Primate Consortium (Yoo et al. 2025) aligned with Progressive Cactus (Armstrong et al. 2020).

Source: same, ¶8 (Q171, FM10). Rule RH: FM6 (the rhetorical question) is ledger RH-6; the intensifier in FM8 ("beyond any dispute", the mesa signature as "the dominant source of genomic divergence") is RH-7; its three dialectic claims are carried here: (a) the signature exists, (b) it is the dominant source of divergence between humans and the great apes, (c) no account of speciation is complete without it (Q169).

Note on FM10's wording (checked against the saved page 2026-10-10): the original reads "can still be considered viable candidates", with no bracketed "[not]"; read in context it means "can no longer be considered viable". The audit quotes it as published.

## Formal statement
No formula in the post. Quantities named: substitution density per window (window size not given); dispersion = variance relative to a "uniform-rate process" (statistic not defined, "more than 80 times"); mesa = contiguous block of dense windows with sharp boundaries (no coordinates); "human-lineage substitutions" in one mesa vs (a) "the MITTENS fixation ceiling" and (b) Haldane's genome-wide maximum for selection (no counts, units not stated: SNV vs bp, event vs base). Data: six non-human T2T ape assemblies plus human (seven sequences), aligned with Progressive Cactus (Yoo et al. 2025; Armstrong et al. 2020). Method statement: "twin 96-core 512GB RAM" machines (Q162, FM1).

## Assumptions
- Stated: the T2T Primate Consortium alignment is adequate; "relictation cannot be the whole story and may not be the only discrete mechanism at work" (Q163, FM2); sigillation is a hypothesis, not proof.
- Implicit: a human-lineage excess within contiguous blocks cannot arise from neutral processes with a heterogeneous mutation rate, incomplete lineage sorting or alignment/polarisation error; selection and drift are both tested by the mesa pattern; the comparison of one mesa with a genome-wide Haldane maximum is like-for-like (Haldane's cost applies to selected substitutions, so the comparison presupposes the mesa is selected).

## Responses
- Against (critic side, the audit's steelman of the critics; marked inference, no critic has responded yet): (1) overdispersion of substitution density is the standard result of mutation-rate heterogeneity (CpG, replication timing, recombination-associated), alignment error in repeats and segmental duplications, and incomplete lineage sorting; "80 times more variable than a uniform-rate process" compares against a null no one uses. (2) "Human-lineage" assignment needs an outgroup; ancestral polymorphism and ILS can place differences on the human branch. (3) Neutral theory predicts k = mu locally, so a high-mu mesa produces excess substitutions on every lineage; only a human-specific excess discriminates, and the post gives no per-lineage numbers or chimp- and gorilla-lineage mesas. (4) One mesa against a genome-wide Haldane maximum is a units step. (5) FM8(b) "dominant source" has no fraction. (6) "Neither selection nor drift viable" does not follow from a pattern both can contain; sigillation is introduced after the data, so the data do not test it. Caution (pre-registration 5b): do not dismiss for the AI or UATV provenance; the data are public, so replicate.
- In support (Day-side steelman, the audit's): (1) the data are public, so anyone can check; FM10 meets the replication checklist better than most of Day's earlier posts. (2) Day hedges: "suggests", "may", "initial evidence", "no more proof than relictation". (3) The overdispersion claim is testable and, once the statistic is defined, falsifiable. (4) A lineage-asymmetric excess confined to contiguous blocks is a pattern uniform-rate neutral theory does not predict, and the critics' own k = mu argument assumes a uniform mutation rate. (5) He concedes relictation is "not the whole story", revising his own earlier mechanism downward.
- Weaknesses in the responses: no critic has replied (refresh 2026-10-10: nothing new from McCarthy, keruru, Dembski, Tree of Woe); both steelmen are inferences from the post alone, and the UATV broadcast itself is unread.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Yoo et al. 2025 (T2T Primate Consortium) | six non-human ape assemblies plus human; SDR average 327 Mb per lineage (fidelity ledger) | cited and retrievable; the use for mesa counts not checked |
| Armstrong et al. 2020 (Progressive Cactus) | multiple-genome aligner | cited; alignment quality in repeats not checked |
| Haldane 1957 / Nunney 2003 | see H, H8 | the "maximum that natural selection can theoretically fix across the entire genome" figure is not given in the post: unverifiable |

## Pre-registered prediction
Not pre-registered as a check. The scoring of the earlier forecast of Day's UATV result is in `docs/research/prereg-2026-10-09-day-uatv-analysis.md` (form A partial hit; the form list lacked a distribution-of-substitutions variant; see the post hoc note there). The replication below must be pre-registered by Opus before any run (QUEUE).
- Under the claimant's model: a human-lineage mesa excess persists after masking of repeats and segmental duplications, CpG correction, and ILS-aware polarisation, and exceeds a heterogeneous-mu neutral null on the human branch only.
- Under the opposing model: the overdispersion and clustering are reproduced by a neutral null with realistic mutation-rate variation (and by the same statistic on the chimp and gorilla lineages), so a human-specific excess is absent or within the null's range.
- Result that would change a verdict: release of the mesa coordinates, window size, dispersion statistic and code; or a pre-registered per-lineage replication on the public alignment against a neutral null with variable mutation rate (QUEUE).

## Check
None run. Proposed: pre-register a per-lineage mesa replication against a neutral null with variable mutation rate (Opus design; run on na-workhorse only). Source refresh: `docs/research/sources/refresh-2026-10-10.md`. Defeaters: d389-d393 in `argmap/defeaters.yaml`.

## Simulator variables implied
- per-lineage, per-window substitution density
- mutation-rate heterogeneity (CpG, replication timing)
- ILS fraction and polarisation rule
- window size and mesa-calling rule

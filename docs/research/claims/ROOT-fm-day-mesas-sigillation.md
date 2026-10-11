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
  internal: pending      # R4 FM: FM3 holds (weak), FM5 holds (literal); FM10 stays pending (no derivation stated; rule-N grep at integration, see R4 FM paragraph). Earlier: numbers FM3 (80x) and FM5 (mesa vs MITTENS ceiling and Haldane) have no stated statistic, units or counts; the step from the pattern to FM10 is not derived in the text
  fidelity: pending      # the "Haldane" maximum and the "MITTENS fixation ceiling" figures are unverifiable until the mesa counts are released; Yoo 2025 / Progressive Cactus are named data sources (cited, retrievable)
  external: contested      # R4 FM (verdict of FM10, the ROOT-level conclusion; leaning critic): the pattern is shared across lineages and reproduced by a shared-rate null; every pre-registered discriminating cell (P3, P4, P5, P7) falls on the critics' side; one Day-side cell (chrX F1 100 kb) is one orthologous centromeric-transition window. No code, mesa coordinates, window size or dispersion statistic released by Day (refresh 2026-10-10)
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
R4 FM (`research/checks/results/R4-FM.md`; pre-registered d723064 `fm_mesa_replication.py`, post hoc `fm_mirror.py` 737648e and `fm_fix2.py` 6aa9bb6; reviews #43-#47: three at 1796620, combined re-review 43dca91, light review 393a1fd; na-workhorse). Sub-claims: [FM3](FM3-overdispersion-more-than-80-times.md), [FM4](FM4-mesas-clustering-sharp-boundaries.md), [FM5](FM5-one-mesa-exceeds-mittens-and-haldane.md), [FM7](FM7-sigillation-lineage-specific-mesas.md), [FM8b](FM8b-mesas-dominant-source-of-divergence.md), [FM10](FM10-neither-selection-nor-drift-viable.md). Source refresh: `docs/research/sources/refresh-2026-10-10.md`. Defeaters: d389-d393 (steelman, untested) and d394-d403 (R4 FM and its reviews).

R4 FM: the data Day names (T2T ape alignment against hg38/orangutan-alignable sequence) show the overdispersion, clustering and mesas he describes (FM3, FM4 clustering and FM5 as literal descriptions are supported), but the pattern is shared across lineages: 32-53% of human-mesa windows lie inside chimp mesas against a 0.56-1.0% background; a shared-rate null reproduces 64-69% of human mesas at 100 kb; chimp-specific mesas exceed the null by more than human-specific ones. All four pre-registered discriminating cells (P3, P4, P5, P7) fall on the critics' side. The Day-side points are the registered E2 hit (non-discriminating), "sharp boundaries" (pending after calibration: edges reach about 90% of a perfect step at 10 kb, q 0.76 / 0.63), and the unmasked F0 human-heavy excess, which the mirror test (chimp-referenced re-run) shows follows the reference (R 1.97 on hs1, 0.25 on chimp: a projection effect, not a human-lineage signal). chrX F1 100 kb (R 3.76 hs1, 3.39 chimp-referenced) is the single remaining Day-side cell; post hoc it is one orthologous window in the CHM13 chrX p-arm centromeric transition region (R 1.11-1.16 without it), cause untested. FM8(b): human mesas hold 1.25-2.5% of human-chimp differences (single-nucleotide, alignable sequence); silent on structural divergence. FM10: external `contested`, leaning critic; a human-specific autosomal mesa signal is contradicted on alignable sequence. The shared-rate null is descriptive and the residual phi_res 2.3-2.7 is unattributed (an upper bound for the critics' mechanism).

Rule-N grep of Day's corpus (2026-10-10, `quotes-day.md`, the E4 claim file, B3d): FM10 needs the premise "neutral diffusive drift implies a uniform per-window rate". The only occurrence of "uniform-rate" is the FM3 sentence itself (Q164); no harvested Day text states, defends or uses that premise. His own material does carry time-varying drift (relictation, Z23188201, "technically a form of non-diffusive drift ... produced by a very different and much faster process") and cites among-species mutation-rate variation (Bergeron, B3d), but FM10's wording is "neutral diffusive drift", which excludes relictation; and MITTENS (Q06-Q14, Q132-Q139) uses per-generation counts, with no regional-rate statement. So N2b ("needs a premise the author's own text contradicts") is not triggered; the open question is N2d ("stronger than the premises support"), which needs a deliberate call because the post states no premise at all. Internal stays `pending`; the N2d option is flagged for the user.

R4 L1 (awaiting review, 2026-10-11): Day's new dN/dS = 0.80 (DN1-DN4, 2026-10-11) is attached here as a Day-side data claim. On hg38/panTro5 all genes give 0.271 and Ensembl one2one 0.207; Day's 0.80 is not reproduced by any gene set; his single-SNV 71.6% nonsyn share matches out-of-frame reading. T2T rerun queued (L1b).

## Simulator variables implied
- per-lineage, per-window substitution density
- mutation-rate heterogeneity (CpG, replication timing)
- ILS fraction and polarisation rule
- window size and mesa-calling rule

# R4 GAP05: slightly deleterious fixations on the human lineage, from a sourced DFE (Kimura)

Tier: low-stakes (GAP-05 is not a `hierarchy.yaml` node; B9 is `load_bearing: false`), so one combined review is due. Script: `research/checks/gap05_slightly_deleterious.py` (pre-registered, committed before the run; local, one process, numpy, <10 s). Output: `raw/gap05_slightly_deleterious.out`. Not integrated.

**Disclosure.** The DFE bin shares (28-33% |s| < 1e-4; 15-17% 1e-4..1e-3; 50-57% >= 1e-3) were summarised in chat before the script was written, so the DFE inputs were not blind. The Kimura integration, counts, cost and dN/dS comparison were pre-registered before the run.

## Question and inputs
GAP-05 (`ledgers/gaps.md`): how many slightly deleterious (|N_e s| ~ 1) mutations does a drift account imply fixed on the human lineage since the chimp split, and what fitness cost? The old gap text had only a rough "upper-end scenario" (about 1e5 substitutions, log-fitness decline 1-10) with Boyko's nonsynonymous share applied to all constrained sites.

- DFE: Kim, Huber & Lohmueller 2017 Table 3 (new nonsynonymous mutations, |s| rescaled to N = 10,000), bins 0-1e-5, 1e-5..1e-4, 1e-4..1e-3, 1e-3..1e-2, >1e-2. Boyko row 0.183 / 0.096 / 0.147 / 0.219 / 0.355; 1000 Genomes gamma row 0.217 / 0.112 / 0.169 / 0.243 / 0.259 (`refresh-2026-10-11b-lit.md`, `quotes-literature.md`). Within-bin shapes are the audit's assumption.
- mu = 1.2e-8 (1.1e-8..1.5e-8), T = 252,000 generations (Day), h = 0.5, genic Kimura u(s, N_e) (code copied from `hf_followups.py`, validated there against per-site WF). Nonsynonymous sites 2.78e7 per haploid genome (R4-L1 raw, V0 ALL; repo-derived, one transcript per gene). Neutral-equivalent nonsynonymous mutations per lineage: mu x sites x T = **84,035**. Observed nonsynonymous differences per lineage about 64,700 (Nd/2 from R4-L1, human + chimp 129,479).
- Reading A: Kim's |s| is the heterozygote effect, a fixation costs 2s. Reading B: |s| is the homozygote effect, a fixation costs s. The source paper's convention was not checked against the full text for this write-up (open, caveat 1).

## Results (expected deleterious nonsynonymous fixations on one lineage; cost = multiplicative sum, no compensation)
| Reading | DFE row | N_e | predicted dN/dS | fixations | log-fitness decline | fitness ratio |
|---|---|---|---|---|---|---|
| A | Boyko | 1e4 | 0.212 | 17,831 | 0.368 | 0.69 |
| A | Boyko | 2e4 | 0.175 | 14,666 | 0.204 | 0.82 |
| A | Boyko | 57,143 | 0.108 | 9,091 | 0.079 | 0.92 |
| A | 1000G | 1e4 | 0.251 | 21,067 | 0.431 | 0.65 |
| A | 1000G | 2e4 | 0.206 | 17,350 | 0.240 | 0.79 |
| A | 1000G | 57,143 | 0.128 | 10,773 | 0.094 | 0.91 |
| B | Boyko | 1e4 | 0.248 | 20,881 | 0.367 | 0.69 |
| B | 1000G | 1e4 | 0.293 | 24,628 | 0.427 | 0.65 |
| B | Boyko / 1000G | 2e4 | 0.212 / 0.251 | 17,831 / 21,067 | 0.184 / 0.216 | 0.83 / 0.81 |
| B | Boyko / 1000G | 57,143 | 0.153 / 0.181 | 12,881 / 15,249 | 0.076 / 0.090 | 0.93 / 0.91 |

Per-generation decline 3e-7 to 1.7e-6. Sensitivities (Reading A, N_e 1e4): mu 1.1e-8..1.5e-8 gives 16,300-26,300 fixations and decline 0.34-0.54; bin 0-1e-5 log-uniform (1e-7..1e-5) lowers decline to 0.29-0.34 and leaves dN/dS 0.22-0.26.

**Where the count and cost sit (Reading A, N_e 1e4, Boyko).** Bin 0-1e-5: 13,909 fixations (f = 0.90 of neutral), cost 0.134. Bin 1e-5..1e-4: 3,823 (f = 0.47), cost 0.209. Bin 1e-4..1e-3: 99 (f = 0.008), cost 0.025. Bins >= 1e-3: none. So **99-114 fixations have |s| >= 1e-4**, and about 99% of the count and 93% of the cost come from |s| < 1e-4 (|N_e s| below 1). Mean cost per fixation 1e-5 to 5e-5. The "slightly deleterious" class that drift fixes is mostly the effectively neutral end.

**Noncoding: unsourced DFE.** No Ns ~ 1 share for constrained noncoding sites was found. Constrained noncoding sites: 0.082 x 3.1e9 - 3.6e7 coding = 2.2e8 (1.8e8-2.5e8 over Rands 7.1-9.2%). Bracket only: if a fraction q of their mutations had Boyko's 1e-5..1e-3 conditional DFE, q = 0.05 / 0.15 / 0.30 adds 6,300 / 19,000 / 38,000 fixations and 0.38 / 1.13 / 2.26 log-fitness decline (8.2%; ranges 0.32-0.43, 0.95-1.29, 1.9-2.6 across Rands CI). The q values are not sourced; this shows only that the answer is dominated by an unmeasured number, because the noncoding target is 6x the coding one.

## Scoring against the pre-registered bands
| Band | Outcome |
|---|---|
| DB1 (Day): coding decline >= 0.05 at N_e 1e4, both rows/readings | **Hit** (0.37-0.43) |
| DB2 (Day): >= ln 3 at N_e 1e4 or 57,143 | **Miss** (max 0.43; coding only) |
| DB3 (Day): >= 1,000 fixations with |s| >= 1e-4 | **Miss** (99-114 in A; 780-897 in B) |
| CB1 (critic): predicted dN/dS 0.16-0.34 at N_e 1e4 | **Hit** (0.21-0.29; A 0.21-0.25, inside the observed 0.21-0.27) |
| CB2 (critic): deleterious fixations < 50% of neutral-equivalent | **Hit** (21-25%) |
| CB3 (critic): decline < ln 3 at N_e 1e4, 2e4 | **Hit** (<= 0.43) |
| Audit point: dN/dS 0.17-0.30; fixations 11k-26k; decline 0.3-1.5; N_e 57k lower | **Hit** on all four (decline 0.37-0.43 is in the low part of the band) |

## What it shows
1. **Counts.** On a sourced DFE the coding-only drift account fixes about 15,000-21,000 (range 9,000-26,000 across rows, N_e, mu, reading) slightly deleterious nonsynonymous mutations per lineage, i.e. 17-30% of the neutral expectation. That is 5-10x below the old rough "1e5" figure.
2. **dN/dS consistency.** The Kim DFE, with no free parameter fitted to divergence, predicts human-chimp dN/dS 0.21-0.29 at N_e = 1e4, matching R4-L1's 0.21-0.27 (V0 ALL 0.27, O121 0.21, filtered 0.234-0.281). Caveat: the observed ratio also contains the Boyko 10-20% adaptive amino-acid share, which would raise the observed side; and a larger N_e (5.7e4, Day's implied) predicts only 0.11-0.18, which undershoots. So the DFE is consistent with the observed dN/dS only near N_e 1e4-2e4; this independently disfavours the large-N_e reading of the nonsynonymous data.
3. **Cost.** Uncompensated coding cost is a log-fitness decline of 0.08-0.43 over 252,000 generations (fitness ratio 0.65-0.93, about 1e-6 per generation). It is not a meltdown (none reaches ln 3) and not "extinction within centuries" (B9). But it is not nothing: 35% lower absolute fitness at N_e 1e4 if hard selection, uncompensated, and the noncoding bracket could equal or exceed it.

## Who this helps
- **Day / allies (Hossjer HO-11).** The premise that drift fixes slightly deleterious mutations along the human lineage is now numerically supported from a published DFE, not just asserted: about 17,000-21,000 coding fixations, a 30% uncompensated decline at N_e 1e4. B9's best point (GAP-05) is real in its premise. The noncoding side is open and could add as much again; no critic has put a number on it.
- **Critics.** The same DFE reproduces observed dN/dS without any appeal to selection being off, so the standard model accounts for the coding data; the count is modest (a fifth to a quarter of neutral), 99% of it with N_e |s| below 1, and the cost is about 1e-6 per generation, 3 orders below the per-generation rates in Day's "centuries" and "9 generations" claims. Compensatory mutation, soft selection and weak stabilising selection (Charlesworth 2013, Kondrashov 1995) are untested here and can only lower the cost.
- **Both.** The result does not settle whether the decline is real: the model has no back or compensatory mutation, which is the critics' whole answer, and the DFE for nearly neutral bins is the least certain part of the data.

## Caveats
1. Kim's s convention (heterozygote or homozygote) is carried as Reading A/B; the full-text check of Table 3 notes is open. It moves the fixation count by 17% and the cost not at all at N_e 1e4.
2. DFE in the nearly neutral bins (|s| < 1e-4) is poorly constrained by polymorphism (Kim): the 0-1e-5 bin in Table 3 is a share of a fitted parametric DFE, not a measured one. 2Ns for such mutations is below 1; the within-bin shape is assumed (alt run shown).
3. No compensatory mutation, back mutation, epistasis (synergistic epistasis would purge faster; compensatory would offset), linkage/BGS, or demographic history. N_e is constant at each value; the real lineage had a larger ancestral N_e (R4-B4a), which lowers fixations. The cost shown is an upper-end for coding.
4. Mutation rate applied to nonsynonymous sites as a single mu; CpG and mutation spectrum not modelled. N sites come from R4-L1's one transcript per gene (undercounts isoforms).
5. Log-fitness decline is not a demographic decline unless selection is hard (cf. HF-a): under soft/relative fitness the cost is not lost absolute fitness.
6. Noncoding DFE unsourced; bracket only.
7. The dN/dS match is evidence for the DFE, not for any particular cost: a model with mostly neutral and mostly strong mutations gives the same dN/dS.

## Proposed verdict moves (not applied; integration pending)
- **GAP-05:** open to "computed on a sourced coding DFE; noncoding unsourced; compensation untestable". Premise supported; collapse not.
- **B9 external (scoped):** stays `contradicted` on the extinction-within-centuries wording; add that GAP-05 (credited to Day as best point) is quantified: coding decline 0.08-0.43 (about 1e-6/gen), not a collapse.
- **HF open item (HF-d):** the "S1 upper-end 2.47 at U_d = 3" is replaced for coding by 0.37-0.43 at N_e 1e4; U_d for coding is 0.33 per haploid genome per generation (sites x mu), so the earlier U_d = 1 row (0.82) sits above the sourced coding scenario. The noncoding row remains unsourced.
- Linked claims by grep: H5/HO-11 (fitness declines): premise gets a numeric anchor; no verdict change. V20 row in R5-draft: add the coding figure.

# R4 H3 (H-human): can the required ADAPTIVE substitutions be paid for at human-like R, D, load and linkage?

Queue item 1 of `REVIEW.md` ("Queue (after review #5)"). It follows R4-H-C2 and R4-H2-hard, which left Haldane's assumed regime (R ≈ 1.1, diploid D ≈ 20–30) untested.

Status: reviewed. Three reviews (REVIEW-R4-H3-correctness, -steelman-day, -steelman-critic) and one fix pass. The fix-pass runs are post hoc (§4.6). Review resolution is in §9.

## Headline (every verdict is conditional)
**What is tested.** Haldane's cost of selection as a **hard-selection persistence limit**:
- a treadmill in which the environment makes the ancestral allele costly;
- log-additive costs across loci;
- ceiling regulation, so that fecundity rises when N < K;
- K = 1000 diploids, a 36.8 M map, and K = 4000/10⁴ for the load runs.

In this model the sustainable adaptive rate is **φ · (ln R − U_hard)/D**, where:
- D ≈ 2 ln 2N is the cost per substitution, validated against K;
- φ ≤ 1 is the shortfall caused by load fluctuations (the "packet" effect, §4.6.6), which depends on s and on the time window.

**Day's model as he states it.**
- Σ s_i ≤ s_max: a shared budget, with s_max set by Haldane's 10% (Z18168236 §2.3), or "order unity" (Z19984826 §3.3).
- Haldane's 300 generations per substitution, d-adjusted to 487 over 146,250 effective generations, i.e. ≈ 1/667 per nominal generation.
- **H3 confirms the structure:** concurrent sweeps share one budget, and parallelism does not raise the total beyond it.
- **What H3 rejects is the parameter**, not the structure. The budget is ln R, not a fixed 10%.

**Minimum reproductive excess R needed for K_a adaptive substitutions per lineage in T = 252,000 generations** (D = 20 unless noted):

| Condition: adaptive selection / deleterious load | K_a = 10³ | 10⁴ | 10⁵ | 10⁶ |
|---|---|---|---|---|
| hard / soft, mean-field (φ = 1; weak selection: s = 0.003 gives long-run φ 0.94 at R = 2 and 0.69 at R = 1.1; s = 0.001 gives ≈ 1 over 45k; §4.6.2–4.6.3) | 1.08 | 2.21 | 2.8×10³ | e^79 |
| hard / soft, long-run φ (s = 0.01, survival over 252k ≥ 0.5; §4.6.1) | 1.22 | 2.98 | 5.4×10⁴ | none (> 10¹²) |
| hard / soft, D = 10 (standing variation p₀ ≈ 0.007, or M ≈ 0.3 multiple-origin sweeps), mean-field | 1.04 | 1.49 | 53 | 1.7×10¹⁷ |
| hard / soft, D = 5 (p₀ ≈ 0.08), long-run φ | 1.07 | 1.45 | 15 | 6.7×10¹¹ |
| hard / soft, small target M = 0.03 (D ≈ 48, stage M), mean-field | 1.21 | 6.72 | e^19 | e^190 |
| hard / soft, small target M = 0.01 (D ≈ 115, stage M), mean-field | 1.58 | 95.9 | e^46 | e^456 |
| hard / hard, amino-acid class only (U = 0.35), mean-field | 1.54 | 3.14 | 4.0×10³ | e^80 |
| hard / hard, whole genome (U = 2.2), mean-field | 9.8 | 20 | 2.5×10⁴ | e^82 |
| soft (Wallace/Nunney), absolute-fitness gain, or truncation/synergistic epistasis | not a test: no demographic cap in this model, or not modelled (§7) | | | |

- **GAP-01 targets** (all `derived:` there):
  - coding-only adaptive count ≈ 1.3×10³–1.2×10⁴;
  - a noncoding adaptive share a_nc = 0.1% / 1% / 5% gives ≈ 2×10⁴ / 1.7×10⁵ / 9×10⁵.
- **Day's 17.5M–205M** need ln R in the hundreds to tens of thousands in *every* row. This is true of any cost-of-selection model, so it is uninformative about Day's live A/B argument (rate limits on all fixations), which branch B decides.
- **R is not sourced.** The anchors are:
  - Haldane's assumed 10% = R ≈ 1.1 (illustrative; Matheson et al. 2025 make the same mapping, k = 1.1).
  - Day's later "highest-fitness individual leaves twice as many descendants as the average" (Z19984826 §3.3): R ≈ 2 in the audit's reading.
  - Day's own natural-fertility total fertility of 6–8 (Z18166426): at most 3–4 offspring per adult before any mortality, so R ≤ 3–4.

**Results that favour Day**
- At R ≈ 1.1 the sustainable rate is within a factor of about 1–3 of Haldane's ln R/D. The 10k-window λ50 is 0.00340 [0.00300, 0.00379] ≈ 1/300.
- It **fails over 40k generations** (0/8 at 0.94/300). At s = 0.01 the long-run φ is 0.30, i.e. about 1/530–1/1,050 over 252k at D = 15–30 (§4.6.1). At s = 0.003 it is about 1/230–1/460 (§4.6.2).
- Load fluctuations cost 25–60% of the mean-field cap at s = 0.01 in a 10k window, and 27–70% over 252k (φ_252k = 0.30–0.73).
- A hard load of the amino-acid class alone removes R ≤ 1.42.
- Background selection cuts the fixation probability by 20–27% and raises D by 7–15%.
- Finite supply raises D to ≈ 15 + 1/M at M ≤ 0.03 (40–160). At M = 0.01 even R = 2 sustains only ≈ 1/430 (§4.6.4).
- a_nc ≈ 0.1% (2×10⁴) needs R ≳ 3 (D = 10) to ≳ 9 (D = 20) under the long-run φ.
- a_nc ≳ 1% is unpayable at any R in the anchor range (≤ 3–4) for D ≥ 5.

**Results that favour the critics.** These are conditional on hard adaptive selection with a soft deleterious load.
- Coding-only K_a is payable at R ≈ 1.2–3 (long-run φ, s = 0.01) or 1.1–2.2 (mean-field; long-run φ ≈ 0.7–0.94 at s = 0.003).
- The budget scales with ln R, so "10%" is a parameter, not a law.
- Day's counts fail under every cost model.

**The flip, and why it cannot be settled here.**
- The answer flips at a_nc ≈ 0.01–0.6%.
- That is **below the resolution of every α estimate in the corpus**: the coding α CI alone spans −0.30 to 0.24, and no genome-wide noncoding α exists.
- So "coding-only fits" means the question is **undetermined at the resolution of the data**. It is not a finding for the critics.

## Runs and files
**Pre-registration.** `research/checks/h3_human_scale.py` was committed alone as **0061b28** before any main run, after two smoke tests (<30 s, discarded). The docstring holds S1–S7, D1–D3, the falsifiers and P-V. `git diff 0061b28 HEAD -- h3_human_scale.py` is empty; the reviewer verified this.

| Stage | Command (`research/.venv/bin/python -I research/checks/...`) | Host | Wall | Status |
|---|---|---|---|---|
| analytic | `h3_human_scale.py analytic` | na-garage | <1 s | pre-registered |
| wfD | `h3_human_scale.py wfD` | na-garage | 22 s | pre-registered |
| A | `h3_human_scale.py A 8` (672 runs) | na-garage | 508 s | pre-registered |
| V | `h3_human_scale.py V 3` (60) | na-garage | 218 s | pre-registered |
| B | `h3_human_scale.py B 9` (96) | na-garage | 932 s | pre-registered |
| C | `h3_human_scale.py C 3` (48) | na-garage | 146 s | pre-registered |
| S | `h3_human_scale.py S 3` (24) | na-garage | 15 s | pre-registered |
| tables | `h3_tables.py` (analysis only; logistic λ50 added in the fix pass) | na-garage | <5 s | post hoc |
| P | `h3_posthoc.py 11` (84) | na-workhorse | 400 s | post hoc |
| wfD2 | `h3_fixpass.py wfD2` (exact −ln w̄ charge, SEs; run under e48a5af, md5 f31f2478, whose wfD2 code is identical to 3688bcb) | na-garage | 10 s | post hoc, fix pass |
| pk | `h3_fixpass.py pk` (packet model) | na-garage | 28 s | post hoc, fix pass |
| L | `h3_fixpass.py L 12` (144 runs, 100k generations) | na-workhorse | 1,544 s | post hoc, fix pass |
| H | `h3_fixpass.py H 12` (38 runs, K = 4000 / 10⁴ hard load) | na-workhorse | 4,250 s (exit 1 in the summary step after all rows were written; §4.6.5) | post hoc, fix pass |
| M | `h3_fixpass.py M 12` (216 runs, M = 0.01 / 0.03 / 0.3) | na-workhorse | 224 s | post hoc, fix pass |
| W | `h3_fixpass.py W 12` (48 runs, s = 0.003, 56k generations) | na-workhorse | 692 s | post hoc, fix pass |
| X | `h3_fixpass.py X 12` (24 runs, s = 0.001, 45k generations) | na-workhorse | 1,389 s | post hoc, fix pass |
| report | `h3_fixpass.py report` (hazard, survival over T, long-run φ, R_min) | na-garage | <5 s | post hoc, fix pass |

**Provenance**
- **Commits** (all local; nothing was pushed, and nothing was committed on workhorse):
  - 0061b28: pre-registered script;
  - 70d83cc: `h3_posthoc.py`, `h3_tables.py`;
  - e48a5af: `h3_fixpass.py`, "H3 post hoc (review fix pass): script before run";
  - 3688bcb: the packet model rewritten as an FFT convolution. This is a speed change only. The first launch was stopped before any pk output existed.
  - 872d8b1: logistic λ50 in `h3_tables.py`.
- **Hosts:**
  - Stages A–S, wfD2, pk and every report ran on na-garage.
  - P, L, H, M, W and X ran on na-workhorse (`hostname` = na-workhorse.allevato.io).
  - The first two attempts to copy scripts to workhorse were denied by the auto-mode classifier. The user then approved, and the coordinator synced; my later copy of 3688bcb succeeded.
  - On both hosts: `h3_fixpass.py` md5 a314a0b2…, `h3_human_scale.py` a2f861bf…, numpy 2.5.3, scipy 1.18.1, Python 3.14.4. These are stored in `results/raw/h3fp.host` (workhorse) and `h3_fx.host` (local).
  - `h3_local.host` (na-garage) was written after stages A–S had finished, as the correctness review noted. The reviewer re-ran P cells on na-garage and got bit-identical results.
- **Seeds:**
  - main stages: `SeedSequence([20261050, stage, cell, rep])`;
  - P: `[20261051, cell, rep]`;
  - fix pass: `[20261052, stage, cell, rep]`.
- **Raw output:** `results/raw/h3_*` and `h3_fx_*` (`.jsonl` per run, `_summary.json`, `.out`), plus `h3_fx_report.{out,json}`, `h3_logit_lam50.json` and `h3_fx_pk.json`.

## Claims restated (verbatim; locators as in the claim files or `sources/raw`)
| ID | Who | Quote | Locator |
|---|---|---|---|
| H | Day | "Haldane calculated that mammals could fix no more than approximately one beneficial substitution per 300 generations, based on the reproductive cost each substitution imposes on a population." | Z18168236, Abstract |
| H | Day | "The 10% selective mortality is a total budget for the population, not a per-locus allocation." | Z18168236 §2.3 |
| H | Day | "Achievable fixations (Haldane + d) = 146,250 / 300 = 487 fixations" | Z18168236 §4.2 |
| H (scope) | Day | "First, neutral mutations do not explain adaptation. The functional differences that make a human different from a chimpanzee—language capacity, bipedal locomotion, opposable thumbs, enlarged neocortex—cannot be attributed to drift. These differences require beneficial mutations that were selected for." | Z18168236 §5.1 (`sources/raw/day/zenodo-18168236.txt` l.68) |
| H1 | Day | "It is a constraint on selectively driven substitutions alone, not on total substitutions." … "observed substitution rates include both neutral fixations (which are the great majority) and adaptive fixations (which are comparatively rare)." … "Once corrected, Term 3 still limits adaptive substitution rate at ~10⁻¹², but total substitution rate is only governed by Terms 1 and 2" | blog 2026-05-07 (about Term 3 of Z19984826 only) |
| H8 | Day | "ksel = smax · d / [2L · ln(2Nₑ)] = 1 · 0.45 / [2 · 3.1 × 10⁹ · ln(6,600)] = 0.45 / [2 · 3.1 × 10⁹ · 8.79] ≈ 8.3 × 10⁻¹²" | Z19984826 §4.3 |
| H8 | Day | "The most that natural selection can demand of a genotype is on the order of "the highest-fitness individual leaves twice as many descendants as the average," which puts the aggregate smax at order unity." | Z19984826 §3.3 (txt l.226–228) |
| H8 | Day | "None of them raises smax above order unity, and the reason is the same in all three cases." | Z19984826 §3.3.1 |
| H5 | Hössjer (ally) | "Vox Day convincingly argues that if many nucleotides at which fixation takes place have a selective advantage (so that natural selection acts on all these mutations) there is a reproductive cost of having many fixations going on in parallel." … "perhaps more in line with equation (3)." | Hössjer PDF 2026-09-14, p.3 |
| KR-09 | keruru (ally label; Jan 2026, superseded) | "For the estimated 700,000 adaptive substitutions (protein-coding changes and functional regulatory elements), Haldane's limit permits only about 1,000 fixations total (300,000 generations ÷ 300 generations per fixation)." | `sources/raw/critics/ck-probability-zero-a-review-too-late.json` |
| GG | Hancock (Gutsick Gibbon video) | "So it's important to note that the cost of selection is only applicable for hard selection models" (02:07:18); "most of the issues come from uh being poorly adapted to your environment" (02:08:20); "they have to replace all the other individuals that" [died] (02:11:51); "the frequency doesn't have to be very low. It could have been a neutral alil and so it could have been at intermediate frequencies" (02:12:32) | `sources/raw/critics/yt/_Vu0ZVVjwHc.transcript.txt` l.369, 372, 382, 384 |
| H6 | Nesslig20 (critic) | "Haldane's reproductive cost limit does not apply to drift, but can it account for most of the genomic differences between humans and chimps?"; "There are other solutions that allow selection to exceed the limit argued by Haldane (see this recent paper), but I will stick with neutral theory for now." (the link is to Matheson et al. 2025, *Genetics* 229:iyaf011) | Peaceful Science 18094 §2.1 (`sources/raw/critics/ps-topic-18094.json`) |
| RE-2 | KITTENS (critic, AI-assisted) | "The guest explains that it applies to hard selection, where each individual's fate is independent of the others, and is far weaker under soft, competitive selection, and that it concerns selected substitutions only." and "estimates are modest and contested" | `sources/raw/critics/arctic-title-MITTENS.json` §11, §12 |
| H2 | Nunney 2003 | "This relatively large population will become extinct if the environmental change requires allelic substitution faster than about every 300 generations" | Discussion (K = 10⁴, M = 0.1) |
| H7 | Keightley 2012 | "A genome-wide deleterious mutation rate of 2.2 seems higher than humans could tolerate if natural selection is "hard," but could be tolerated if selection acts on relative fitness differences between individuals or if there is synergistic epistasis." | Abstract |
| PA-36 | Matheson, Exposito-Alonso & Masel 2025 | "Haldane's 10% selection intensity estimate is equivalent to 10% of deaths being selective, which corresponds to k=1.1."; "The smallest proportion of selective deaths we observed across 8 environmental conditions was 8.5%"; "These data are not representative of natural conditions"; "human females do not easily give birth to more than 20 infants." | PMC12005247 (fetched in this pass, read only; untrusted; quotes as returned by the fetch tool, not re-checked against the PDF) |

**Targets and time** (as given; none is new here).
- K_a from GAP-01 (`derived:` there).
- Day: 17.5M (A3b), 20M (A3), 205M (A3a).
- Generations: 146,250 / 202,500 / 206,897–350,000 / 252,000 / 325,000 / 450,000 (A1, A3, A4).

## Procedure
**Analytic layer**
- D = Σ_t −ln w̄_t for a diploid log-additive sweep, which is ≈ 2 ln(1/p₀).
- Nei 1971 / Felsenstein 1971 spacing, n = −ln p₀ / ln k (PA-07, PA-10), generalised to λ\* = (ln R − U_hard)/D.
- Flip condition: ln R ≥ U_hard + D·K_a/(φT).

**Simulation layer** (unchanged from the pre-registration)
- K diploids; Haldane's treadmill with one seeded copy that is re-seeded if lost; f = min(R, K/N).
- Hard viability for the adaptive part.
- Deleterious background Poisson(U/2) per gamete, s_d = 0.02:
  - "hard" multiplies survival;
  - "soft" changes only the parent weights, so it has **no demographic cost by construction**.
- 23 × 1.6 M map with the Haldane map function; deleterious counts in 0.1 M bins.
- Extinction when N < 20.
- Windows: 10k + 2k burn-in (main stages); 100k (L); 50k + 6k (W); 30k + 15k (X); 20k + 3k (M); 3–6k + 1–1.5k (H).
- λ50(10k) is now a logistic fit with a profile CI (m1). Two-point grids are bracketed only (m2).

**Long-run quantity (fix pass)**
- Constant-hazard estimate h = deaths / exposure, with an exact Poisson CI. Survival over T is S(T) = e^{−hT}.
- φ_T is the x = λ/λ\* at which S(T) = 0.5, interpolated log-linearly in h between grid cells.

**Scaling (E4)**
- Only N is scaled down. D ≈ 2 ln 2N is validated (P-V).
- The K-dependence of φ is only weakly tested: P3 is underpowered, and the barrier depth ln(K/20) grows logarithmically.

## 1. Analytic results (numbers in `h3_analytic.out`, `h3_fx_report.out`)
**1.1 Cost per substitution (D_det).**

| Case | D |
|---|---|
| N = 10³ | 15.2 |
| N = 10⁴ | 19.8 |
| N = 10⁵ | 24.4 |
| N = 10⁶ | 29.0 |
| Standing variation p₀ = 10⁻² | 9.2 |
| Standing variation p₀ = 10⁻³ | 13.8 |
| Standing variation p₀ = 10⁻⁴ | 18.4 |
| D = 5 | p₀ ≈ 0.08 |
| D = 3 | p₀ ≈ 0.22 |

Haldane's D = 30 corresponds to p₀ ≈ 3×10⁻⁷ (N ≈ 1.6×10⁶).

**1.2 Nei/Felsenstein and the anchors.**
- k = 1.1 and p₀ = 10⁻⁴ give n = 96.6 generations, i.e. 2,608 per 252,000. This reproduces PA-07 and GAP-01.
- The 10% budget is ln R = 0.105 (R = 1.11). Matheson et al. state the same mapping ("corresponds to k=1.1").
- **Term 3 (audit's mapping, not Day's derivation).** 0.0256 per generation equals ln R / D with D = 2 ln 2Nₑ = 17.6 and ln R = s_max·d = 0.45 (R = 1.57); with d = 1, R = e. Day's own anchor ("twice as many descendants as the average") gives R ≈ 2 (ln R ≈ 0.69) in the audit's reading. C2 found d to be a unit conversion, so "s_max·d = ln R" is an arithmetic identification only.
- **Day's 487.** 146,250/300 = 487 corresponds to 1/667 per nominal generation (325,000). In the mean-field formula that is R ≈ 1.02–1.05 for D = 15–30.

**1.3 Mean-field λ\* = (ln R − U_hard)/D, per generation [per lineage over 252,000].** These are mean-field **upper bounds on the rate**; the long-run versions are in §5.

| R | D = 10 | D = 20 | D = 30 | D = 20, U_hard = 0.35 | D = 20, U_hard = 2.2 |
|---|---|---|---|---|---|
| 1.05 | 0.0049 [1,230] | 0.0024 [615] | 0.0016 [410] | extinct | extinct |
| 1.1 | 0.0095 [2,402] | 0.0048 [1,201] | 0.0032 [801] | extinct | extinct |
| 1.2 | 0.018 [4,595] | 0.0091 [2,297] | 0.0061 [1,532] | extinct | extinct |
| 1.5 | 0.041 [10,218] | 0.020 [5,109] | 0.014 [3,406] | 0.0028 [699] | extinct |
| 2 | 0.069 [17,467] | 0.035 [8,734] | 0.023 [5,822] | 0.017 [4,324] | extinct |
| 3 | 0.110 [27,685] | 0.055 [13,843] | 0.037 [9,228] | 0.037 [9,433] | extinct |
| 10 | 0.230 | 0.115 [29,013] | 0.077 | 0.098 [24,603] | 0.0051 [1,293] |

**1.4 Required rates at T = 252,000.**
- Coding-only: 0.005–0.048.
- a_nc = 0.1% / 1% / 5%: 0.079 / 0.67 / 3.6.
- Day 17.5M / 20M / 205M: 69 / 79 / 813.

**1.5 Mean-field R_min = exp(U_hard + D·K_a/T)** (T = 252,000; other T values in `h3_analytic.out` §A4). These are **lower bounds on R_min**.

| K_a | D = 10 | D = 20 | D = 30 | D = 20, U_hard = 0.35 | D = 20, U_hard = 2.2 |
|---|---|---|---|---|---|
| 1.3×10³ | 1.05 | 1.11 | 1.17 | 1.57 | 10.0 |
| 3×10³ | 1.13 | 1.27 | 1.43 | 1.80 | 11.5 |
| 6×10³ | 1.27 | 1.61 | 2.04 | 2.28 | 14.5 |
| 1.2×10⁴ | 1.61 | 2.59 | 4.17 | 3.68 | 23.4 |
| 2×10⁴ (a_nc 0.1%) | 2.21 | 4.89 | 10.8 | 6.94 | 44 |
| 1.7×10⁵ (a_nc 1%) | 851 | 7.2×10⁵ | e^20 | 1.0×10⁶ | 6.5×10⁶ |
| 9×10⁵ (a_nc 5%) | e^36 | e^71 | e^107 | e^72 | e^74 |
| 17.5M / 20M / 205M | e^694 / e^794 / e^8,130 | e^1,389 / e^1,587 / e^16,270 | e^2,083 / e^2,381 / e^24,400 | ≈ same | ≈ same |

**1.6 The flip in a_nc, and break-even D.**
- Mean-field a_nc,max = 0.01–0.6% over R ≤ 10, D = 10–30 and T = 146k–450k, and ≈ 0 at R ≤ 1.2.
- Break-even D = T ln R / K_a at T = 252,000:

| a_nc | K_a | R = 1.5 | R = 2 | R = 3 | R = 10 |
|---|---|---|---|---|---|
| 0.1% | 2×10⁴ | 5.1 | 8.7 | 13.8 | 29.0 |
| 1% | 1.7×10⁵ | 0.60 | 1.03 | 1.63 | 3.41 |
| 5% | 9×10⁵ | 0.11 | 0.19 | 0.31 | 0.64 |

- So a_nc = 1% fits at R = 3 only if the mean cost per adaptive substitution is ≤ 1.6, i.e. starting frequencies of about 0.45 or more under hard treadmill selection.
- For p₀ uniform on (0, 1) among alleles that go on to fix (the critic reviewer's reasoning, not verified here), the mean of 2 ln(1/p₀) is about 2.
- So a mostly-standing-variation picture could bring a_nc ≈ 1% to the edge at R ≈ 3–10. a_nc ≥ 5% would still need D < 0.7 at R = 10.

## 2. Single-locus cost vs selection strength
Exact −ln w̄ charge, with SEs (fix m9; `h3_fx_wfD2.jsonl`; N = 1000).

| 2Ns | 1 | 4 | 10 | 40 | 100 | 400 | 2,000 |
|---|---|---|---|---|---|---|---|
| D conditioned on fixation | 1.86 ± 0.05 | 5.02 ± 0.06 | 7.01 ± 0.04 | 9.85 ± 0.05 | 11.65 ± 0.03 | 14.06 ± 0.02 | 15.60 ± 0.01 |
| D incl. lost attempts, per fixation | 12.9 ± 0.5 | 16.1 ± 0.3 | 16.3 ± 0.2 | 16.5 ± 0.2 | 16.7 ± 0.1 | 16.5 ± 0.03 | 15.8 ± 0.01 |

- At N = 10⁴ (2Ns = 10 / 100 / 2,000): conditioned D = 7.1 / 11.7 / 17.5; total 21.2 ± 0.7 / 21.5 ± 0.5 / 21.0 ± 0.05 (2 ln 2N = 19.8).
- **Total cost per substitution = 2 ln 2N ± 2** at every s (2Ns = 1: −2.3).
- **Cost of the eventually successful allele alone** falls to 2–7 for 2Ns ≤ 10.
- The first pass used a 2s·q charge, which inflated the 2Ns = 400 and 2,000 cells by 0.2–0.6.
- **Which accounting applies:**
  - Treadmill / environmental change charges the total.
  - A gain in absolute fitness with no prior deterioration charges nothing.
- **Credit.** The s-independence of the total is Haldane's own point (via Nunney; also Kimura and Crow, PA-06). The poorly-adapted vs well-adapted distinction is drawn in prose by **Hancock** (video 02:08:20) and by **Nunney** ("soft selection is only important when natural selection is driven by intraspecific competition"; "hard selection will dominate" under directional change). Nobody in the corpus quantified it. The first pass wrongly said neither side had drawn the distinction.

## 3. Scaling validation (stage V; P-V)
Unchanged:
- D(4000) − D(1000) = 2.80 / 2.06 (mean 2.43) vs 2.77 ± 1.0. Passed.
- x = 0.5 persists at both K.
- V validates the D slope over a 4× range of K. Extrapolating to human N (25–250×) rests on theory.

## 4. Simulation results
### 4.1 Core grid, no load (stage A; free + map36 pooled; 10k window)
| R | λ\* = ln R/15.2 | **λ50(10k), logistic [95% CI]** | λ50(10k) × 300 | φ(10k) | At λ = 1/300 | At λ = 0.0296 |
|---|---|---|---|---|---|---|
| 1.05 | 0.0032 | 0.00129 [0.00104, 0.00153] | 0.39 [0.31, 0.46] | 0.40 | 0/16 | 0/16 |
| 1.1 | 0.0063 | 0.00340 [0.00300, 0.00379] | 1.02 [0.90, 1.14] | 0.54 | 8/16 [0.28, 0.72] | 0/16 |
| 1.2 | 0.0120 | 0.00709 [0.00643, 0.00786] | 2.1 [1.9, 2.4] | 0.59 | 16/16 | 0/16 |
| 1.5 | 0.0267 | 0.0185 [0.0166, 0.0202] | 5.6 [5.0, 6.1] | 0.69 | 16/16 | 0/16 |
| 2 | 0.0456 | 0.0345 [0.0330, 0.0368] | 10.4 [9.9, 11.0] | 0.76 | 16/16 | 15/16 |
| 3 | 0.0723 | 0.0552 [0.0543, 0.0632] | 16.6 [16.3, 19.0] | 0.76 | 16/16 | 16/16 |

- **These are 10k-window quantities, not long-run rates** (§4.6.1).
- The near-coincidence at R = 1.1 with a grid point at exactly 1/300 is chance; the logistic fit replaces the first pass's "λ50 = 0.0033".
- D_obs = 15–17; k_obs/λ = 0.94–1.04 in well-sampled cells; p_fix ≈ 2s; up to about 60 concurrent sweeps.
- φ < 1 at s = 0.01 for every R. This is consistent with the packet mechanism, which is now tested (§4.6.6).
- Linkage (36.8 M vs free) shows no detectable difference at this resolution.

### 4.2 Deleterious background and linkage (stage B; K = 1000, 4 reps per cell, two-point x grid)
- **Soft U = 2.2.**
  - Persistence at x = 0.5 / 1.0 equals the no-load value. Soft load has no demographic cost *by construction*, so this is not an independent result.
  - The informative outputs: background selection lowers p_fix by 20–27% (36.8 M map; 16% free; ≈ 50% on the 3.68 M map) and raises D by 7–15% (short map: 21.6). Both are Day-favourable. They raise ln R_min by the same factor, e.g. 1.52 → ≈ 1.57–1.62 at K_a = 3×10³.
  - Differences in λ50 of 20–30% cannot be resolved on a two-point grid.
- **Hard U = 0.35 (K = 1000):**
  - R = 1.2 is extinct (analytic: ln 1.2 < 0.35).
  - R = 2 and 3 persist at xh = 0.5.
  - R = 1.5 is extinct at xh = 0.5 and 1.0. The S5 prediction **failed or was untestable** at a 0.055 margin; K = 4000 results are in §4.6.5.
  - "Removes R ≤ 1.42" holds if the whole class is hard-selected with s ≫ 1/Nₑ. Keightley's 0.35 is a mutation rate, and weakly selected mutations pay less.
- **Hard U = 2.2, K = 1000:**
  - Extinct at R = 3, 10 and 20.
  - Only R ≤ 9 follows from ln R < U.
  - R = 10–20 at K = 1000 is small-N meltdown: equilibrium N ≈ 110 and N s_d ≈ 2. The reviewer showed it also occurs at λ = 0. See §4.6.5 for K = 4000 and 10⁴.
  - The first pass compared this with H2-hard, but H2-hard's deleterious load was **non-heritable** (fresh Poisson each generation, so no ratchet and no background selection). That comparison is withdrawn.

### 4.3 Finite supply (stage C; M = 1, 0.1; two-point grid)
- M = 1: D_obs ≈ 6.4–6.6 (multiple-origin sweeps).
- M = 0.1: D_obs ≈ 17–22.
- Persistence brackets (x′ = 0.5 / 1.0):
  - M = 1, R = 1.1: 6/6 / 1/6;
  - M = 1, R = 1.5: 6/6 / 6/6;
  - M = 0.1, R = 1.1: 4/6 / 0/6;
  - M = 0.1, R = 1.5: 6/6 / 1/6.
- The first pass's "≈ 1/420" and "≈ 1/78" were interpolation artefacts and are withdrawn. Nunney's "about every 300 generations" lies between the R = 1.1 and R = 1.5 brackets.
- **What M ≥ 1 requires** (`derived:`): M = 2Ku with u = μ·L_t, μ = 1.2×10⁻⁸ and K = 10⁴ needs **L_t ≈ 4×10³ beneficial target sites per locus**. A single site or a short element gives M ≈ 2×10⁻⁴–2×10⁻². M < 0.1 is in §4.6.4.

### 4.4 Selection strength (stage S, s = 0.03)
- D_obs = 15.1.
- Persistence at x = 0.5 was much worse: R = 1.1 0/6 (vs 9/16 at s = 0.01; the first pass said "10/16", corrected); R = 2 2/6 (vs 16/16). So φ depends on s.

### 4.5 Post-hoc runs P (na-workhorse; 10–14k windows)
- **P1, s = 0.003:**
  - R = 1.1: 8/8, 6/8, 5/8 at x = 0.5 / 0.75 / 1.0.
  - R = 2: 8/8, 8/8, 5/8.
  - φ(10–14k) ≳ 0.75–1 (only a lower bound; the grid stops at x = 1).
  - 2Ns = 6 at K = 1000, so Ns is confounded with s.
- **P2, window 40k, x = 0.5:** R = 1.1 0/8 (every run dead by 15.5k); R = 1.5 7/8; R = 2 8/8.
- **P3, K = 4000, x = 0.75:** R = 1.1 0/6; R = 2 4/6. This is **underpowered**: Fisher p ≈ 0.3 against K = 1000, so neither "no rise" nor "a rise" in φ with K is shown. A logarithmic K-dependence is expected from the barrier depth ln(K/20).

### 4.6 Fix pass (post hoc; script e48a5af / 3688bcb; hosts as in the run table)
#### 4.6.1 Long-window hazard, s = 0.01 (stage L; K = 1000, free, 8 reps, 102,000 generations)
| R | x = 0.15 | 0.30 | 0.45 | 0.60 | 0.75 |
|---|---|---|---|---|---|
| 1.1 | 0/8 dead | 2/8 (h = 2.7e-6) | 8/8 (h = 4.2e-5) | 8/8 | 8/8 |
| 1.5 | 0/8 | 0/8 | 0/8 | 6/8 (h = 1.4e-5) | 8/8 |
| 2 | — | 0/8 | 0/8 | 3/8 (h = 4.4e-6) | 8/8 (h = 4.6e-5) |
| 3 | — | 0/8 | 0/8 | 0/8 | 5/8 (h = 1.0e-5) |

- **Zero deaths** in 8 × 102k = 816k generations means h < 4.5×10⁻⁶ (95%), i.e. S(252k) ≥ 0.32.
- **Long-run φ_252k** (S(252k) = 0.5): R = 1.1 **0.30** [0.30, 0.45]; R = 1.5 **0.57** [0.45, 0.60]; R = 2 **0.59** [0.45, 0.60]; R = 3 **0.73** [0.60, 0.75].
- φ_146k = 0.33 / 0.58 / 0.61 / 0.74; φ_450k = 0.29 / 0.57 / 0.58 / 0.72.
- Compared with the 10k window (0.54 / 0.69 / 0.76 / 0.76), the long-run cap is lower by about 45% at R = 1.1 and by 4–22% at R ≥ 1.5.
- **Haldane's assumed R = 1.1 in the long run:** λ ≈ 0.30 × 0.0063 = 0.0019 ≈ 1/530 at D = 15.2, and ≈ 1/700–1/1,050 at D = 20–30. That is **below 1/300**, though within a factor of about 1–3 of ln R/D. The hard-sweep cap is tighter over the lineage than the 10k window suggested, which favours Day.
- **Term 3's 0.0296 at R = 2** (x = 0.65) lies above φ_252k = 0.59. It does not persist 252k at this s; the reviewer's scratch run gave S(252k) ≈ 0.3.

#### 4.6.2 Weak selection, s = 0.003 (stage W; R = 1.1, 2; x = 0.5–1.25; 6 reps; 56k generations)
| R | x = 0.5 | 0.75 | 1.0 | 1.25 |
|---|---|---|---|---|
| 1.1 | 0/6 dead | 5/6 (h = 2.9e-5) | 6/6 | 6/6 |
| 2 | 0/6 | 0/6 | 5/6 (h = 3.1e-5) | 6/6 |

- **Long-run φ_252k:** R = 1.1 **0.69** [0.50, 0.75]; R = 2 **0.94** [0.75, 1.00]. φ_146k / φ_450k: 0.71 / 0.68 at R = 1.1 and 0.96 / 0.93 at R = 2.
- So weak selection brings the long-run cap close to mean-field at R = 2, but not at R = 1.1.
- The first pass's "φ ≈ 1 at s = 0.003" (a 14k window) holds at R = 2 and overstates R = 1.1 by about 30%.
- **At Haldane's assumed R = 1.1:** s = 0.003 gives a long-run λ ≈ 0.69 × ln 1.1/D. That is ≈ 1/230 at D = 15.2, and **≈ 1/300–1/460 at human D = 20–30**. Haldane's number holds in order of magnitude at his assumed R for weak selection, and is 2–3× too generous for s = 0.01 (§4.6.1).
- Caveat: 2Ns = 6 at K = 1000, so this cell is near-neutral. φ's dependence on s is confounded with Ns; this is untested at larger K.

#### 4.6.3 s = 0.001 (stage X; R = 1.1, 2; x = 0.75–1.25; 4 reps; 45k generations; burn-in 15k ≈ 3 dwell times)
| R | x = 0.75 | 1.0 | 1.25 | D_obs at x = 0.75 / 1.0 / 1.25 |
|---|---|---|---|---|
| 1.1 | 0/4 dead | 0/4 | 0/4 | 15.3 / 13.6 / 11.4 |
| 2 | 0/4 | 0/4 | 0/4 | 13.3 / 13.0 / 11.8 |

- No deaths at any x up to 1.25 (x relative to D_pred = 15.2) over 45k generations.
- D_obs falls with x, because N/K falls (0.50–0.92) and with it 2 ln 2N. So x = 1.25 relative to D_pred is about 1.0–1.1 relative to D_obs: the population **sustains about the mean-field cap computed with the realised D**.
- Weak selection removes the packet shortfall. Hundreds of small concurrent sweeps give a smooth load.
- **Limits:**
  - 4 reps and zero deaths bound only h < 2×10⁻⁵, i.e. S(252k) ≥ 0.006. The long run is **not resolved**.
  - 2Ns = 2 at K = 1000, so this is the near-neutral regime, not human 2Ns ≈ 20–200 at the same s.
  - Read it as "φ ≈ 1 is plausible for weak selection" (mean-field column), not as a measured lifetime rate.

#### 4.6.4 Finite supply M = 0.01, 0.03, 0.3 (stage M; 8 reps; 23k generations)
| M | D_obs (persisting runs) | Persistence over 23k generations, by x = λ/λ\* (λ\* = ln R/15.2) |
|---|---|---|
| 0.3 | 10.4–11.7 | x = 0.22: 8/8 at every R; x = 0.44: R = 1.1 6/8 (S(252k) ≈ 0.04), R = 1.5 and 2 8/8; x = 0.88: 0–2/8 |
| 0.1 (stage C) | 17–22 | see §4.3 |
| 0.03 | 39–52 | x = 0.11: R = 1.1 5/8, R = 1.5 and 2 8/8; x = 0.22: 0–3/8; x = 0.43: 0/8 |
| 0.01 | 99–163 | x = 0.05: R = 1.1 5/8, R = 1.5 and 2 8/8; x = 0.10: 0–1/8; x = 0.20: 0/8 |

- **D ≈ 2 ln 2N + 1/M for M ≤ 0.03** (predicted 48 and 115; observed 39–52 and 99–163). So the pre-registered S6 form *holds at low M* and fails at M ≥ 0.1, where recurrent mutation produces multiple-origin sweeps and cuts D (M = 0.3: 10.5; M = 1: 6.5).
- **Consequence (Day-favourable).** At M = 0.01 the cap is ≈ ln R/(15 + 100). Even at R = 2 the rate that persists 23k generations lies between λ = 0.0023 (8/8) and 0.0046 (0/8), i.e. 1/430–1/220. That is Haldane's order **at R = 2**, and it is a 23k-window value, so it overstates the long-run rate.
- With μ = 1.2×10⁻⁸ and K = 10⁴, M = 0.01 corresponds to about 40 beneficial target sites per locus (`derived:`), and a single-site target to M ≈ 2×10⁻⁴.
- So hard treadmill adaptation from new mutations at small targets is far more expensive than the D = 20 rows suggest. The critic-favourable routes are large targets (M ≳ 0.3), or standing variation (no waiting cost).
- Human M is unsourced, so neither side's case is established.
- Nunney's qualitative M-dependence is reproduced in both directions.

#### 4.6.5 Hard load at K = 4000 and 10⁴ (stage H; map36)
- **Hard U = 2.2, R = 20.** K = 4000: 4/4 persist at λ = 0 and at xh = 0.5 (N/K = 0.07–0.10, load −ln w̄_d = 2.3). K = 10⁴: 3/3 persist at both. **The K = 1000 extinction at R = 20 was a small-N artefact** (correctness M4 confirmed).
- **Hard U = 2.2, R = 10.** K = 4000: extinct 4/4 *even at λ = 0* (t = 152–438). The margin is ln 10 − 2.2 = 0.10, after a 9× bottleneck in generation 1. Not tested at K = 10⁴. Scored as marginal: it follows neither from the analytic bound nor against it.
- **Hard U = 0.35, K = 4000.**
  - R = 1.5: persists 4/4 at λ = 0 (N/K = 0.70), so it is not a small-N effect; extinct 3/4 at xh = 0.5 (λ = 0.0015). With a 0.055 margin the fluctuation shortfall φ is decisive.
  - R = 2: persists at both λ.
- **Bookkeeping.** Stage H exited with code 1 *after* all 38 runs were written: the pre-registered `summarize()` divides by λ in the λ = 0 cells. The report reads the per-run `h3_fx_H.jsonl`, and no row is missing.

#### 4.6.6 Packet-model mechanism check (pk; deterministic sweep-load pulses + ceiling demography, no drift, 400 reps)
| R | 1.05 | 1.1 | 1.2 | 1.5 | 2 | 3 |
|---|---|---|---|---|---|---|
| φ(12k), packet model | 0.35 | 0.48 | 0.56 | 0.67 | 0.73 | 0.78 |
| φ(10k), IBM, logistic | 0.40 | 0.54 | 0.59 | 0.69 | 0.76 | 0.76 |

- The packet model reproduces the IBM's φ(R) to within 10–13% at every R. The φ < 1 shortfall is therefore explained by the discrete arrival of sweep load against ln R, with no drift needed. This answers review m8.

### 4.7 Predictions: held / failed (first-pass scoring corrected per the reviews)
| Prediction | Outcome |
|---|---|
| S1 D = 2 ln 2N ± 15%, s-independent | held |
| S2 k_obs = λ ± 15% when persisting | held in well-sampled cells; sparse R ≤ 1.1 cells 0.71–0.93 |
| S3 φ(10k) 0.3–0.9 (R ≤ 1.2), 0.7–1.1 (R ≥ 1.5), increasing with R | held for R ≤ 1.2, 2, 3; **R = 1.5 (0.69): marginal miss**, within grid resolution; at s = 0.03 well below |
| S4 linkage: λ50 within 20%; soft-load p_fix −5 to −25% (36.8 M); short map −25 to −60%, λ50 within 30% | persistence at x = 0.5 / 1.0 unchanged; the λ50 criteria **cannot be resolved** on a two-point grid; p_fix on the 36.8 M map **failed marginally** (−20 to −27%); short map held (−50%) |
| S5 hard U = 0.35 / 2.2 | R = 1.2, 2, 3 held; **R = 1.5 failed or untestable**; U = 2.2 R = 3 held; **R = 20 held at K = 4000 / 10⁴** (the K = 1000 failure was an artefact); R = 10 extinct at K = 4000 even at λ = 0 (marginal) |
| S6 D_eff ≈ D + 1/M | **failed at M ≥ 0.1** (M = 1: 6.5; 0.3: 10.5; 0.1: 17–22); **approximately held at M ≤ 0.03** (39–52 vs 48; 99–163 vs 115; post hoc) |
| S7 wfD | held at 2Ns = 1, 10, 400, 2,000; **failed at 2Ns = 100** (11.7, −23%) |
| D1 (as pre-registered: rate ≈ 1/300 regardless of R) | split, because Day never claimed R-independence (steelman-Day 4). **D1a "parallelism does not raise the total beyond the shared budget": held** (k = λ up to the cap, the cap independent of concurrency). **D1b "the budget is 10%": the 10%-to-R ≈ 1.1 mapping is a parameter.** The cap rises with ln R (10k-window λ50 2.1× 1/300 at R = 1.2, 16.6× at R = 3) |
| D2 (Term 3 at R = 2: 0.0296) | held in the 10k window (λ50 0.0345 [0.0330, 0.0368]; 15/16) **if R = 2 is the intended value**. At the R implied by the audit's s_max·d mapping (1.57) it fails (λ50 ≈ 0.020). Over 252k, 0.0296 is above φ_252k (§4.6.1) |
| D3 (Day-favourable outcomes reported) | R ≤ 1.1 at or below 1/300 (10k) and below it over 252k; hard U = 0.35 removes R ≤ 1.4 (if fully hard); hard U = 2.2 removes R ≤ 9 (analytic; R = 10 marginal). **"R ≤ 20 at K = 1000" is removed**: R = 20 persists at K = 4000 / 10⁴ (§4.6.5) |
| P-V | held |
| F-Std falsifiers | not triggered |

## 5. Human scale: where the conclusion flips (all conditional)
**Long-run R_min.** Minimum R, under hard adaptive treadmill selection and soft deleterious load, s = 0.01, survival over T ≥ 0.5, φ_T(R) from stage L (linear in ln R; held at φ(3) above R = 3 and at φ(1.1) below it, which is slightly optimistic for R < 1.1). These **replace the first pass's 10k-window tables, which were lower bounds on R_min**.

| T | D | K_a = 10³ | 3×10³ | 10⁴ | 10⁵ | 10⁶ |
|---|---|---|---|---|---|---|
| 146,250 | 20 | 1.33 | 1.97 | 6.4 | 1.1×10⁸ | none |
| 252,000 | 5 | 1.07 | 1.18 | 1.45 | 15 | 6.7×10¹¹ |
| 252,000 | 10 | 1.13 | 1.31 | 1.96 | 232 | none |
| 252,000 | 20 | 1.22 | 1.52 | 2.98 | 5.4×10⁴ | none |
| 252,000 | 30 | 1.31 | 1.84 | 5.1 | 1.2×10⁷ | none |
| 450,000 | 20 | 1.15 | 1.34 | 2.10 | 483 | none |

- **Mean-field (φ = 1) R_min** are in §1.5 / the headline. They apply approximately to weak selection; see §4.6.2–4.6.3.
- **Adjustments:**
  - background selection: multiply ln R_min by about 1.07–1.15;
  - hard amino-acid load: multiply R_min by about e^{0.35};
  - hard whole-genome load: multiply by about e^{2.2} ≈ 9.

**Condition-labelled verdicts**
- **Under hard adaptive treadmill selection, additive costs, soft deleterious load and D ≥ 10:**
  - coding-only K_a (10³–10⁴) is payable at R ≈ 1.1–3;
  - a_nc ≈ 0.1% (2×10⁴) needs R ≈ 3–10;
  - a_nc ≥ 1% needs R ≥ 10² at D = 5 and is unpayable at D ≥ 10 at any R in the anchor range (R ≤ 4).
- **Under hard treadmill selection from new mutations at small targets** (M ≈ 0.01–0.03, i.e. about 40–125 target sites per locus): D ≈ 48–115. Coding-only 3×10³ then needs R ≈ 1.8–3.9 (mean-field) and more with long-run φ. This favours Day and is as unsourced as the critic-side D ≤ 10 routes.
- **Under the same with D ≈ 2–3** (mostly intermediate-frequency standing variation, Hancock's 02:12:32 point): a_nc ≈ 1% reaches the edge at R ≈ 3–10. a_nc ≥ 5% does not.
- **Under hard adaptive selection with a fully hard deleterious load:**
  - U = 2.2 rules out every R < 9, i.e. every anchor. This is Keightley's own point, a bounding case that the cited literature (PA-16, PA-17) argues does not describe humans.
  - U = 0.35 rules out R ≤ 1.42.
- **Under soft adaptive selection (Wallace/Nunney), absolute-fitness gain, or truncation/synergistic epistasis:** H3 has no demographic cap to report. The verdict is not tested (§7).
- **Day's 17.5M–205M are unpayable under every cost model.** This says nothing about A/B.

**The unsourced inputs that decide it**
- a_nc: the threshold is below the resolution of any α estimate.
- R: anchors 1.1 (Haldane's assumption) to ≈ 2 (Day's s_max) to ≤ 3–4 (Day's total fertility 6–8 before mortality); no sourced net hominid value.
- Whether adaptive selection was hard and the load soft. This is the hybrid H3 tests. It is the audit's construction, and no party argued it.
- D (standing frequency, M).
- s, through φ.

## 6. Adjudication (crediting only those who made each argument)
**Day**
1. **Shared budget (H §2.3; Z19984826 §3.3).** Held as structure. Concurrent sweeps share one reproductive budget, and the total rate cannot exceed it; that is D1a. Day's parameter (10%) is Haldane's assumption (R ≈ 1.1), not a law. Under ceiling regulation the budget is ln R. Day's own later anchor (s_max ≈ 1, "twice as many descendants") is R ≈ 2 in the audit's reading, where the 10k-window cap is about 10× 1/300 and the long-run cap about 8×. Day uses two budgets that differ by about 17× (R4-H-C2).
2. **1/300 at R ≈ 1.1.** At Haldane's assumed 10%, the model's sustainable rate is within a factor of about 1–3 of ln R/D:
   - 10k window: λ50 = 0.00340 [0.00300, 0.00379];
   - 40k window: fails (0/8 at 0.94/300);
   - long run: φ_252k = 0.30, i.e. 1/530 at D = 15 and 1/700–1/1,050 at human D.
   This is a **consistency check of the Nei/Felsenstein arithmetic at Haldane's chosen R** (circular in R by construction). It is not an independent confirmation. Day's d-adjusted 1/667 corresponds to R ≈ 1.02–1.05 (mean-field) or about 1.1 (long-run φ).
   - It **requires a soft deleterious load**: a hard amino-acid load alone rules out R ≤ 1.42 (critic finding 2b).
3. **Term 3 (H8).** It matched the R = 2 case of its own pre-registered form in the 10k window, if R = 2 is intended. Over 252k it overshoots (0.0296 > φ_252k·λ\*). The R-independence that D2 tested was not claimed by Day; it holds only if s_max = 1 is read as a constant.
4. **17.5M–205M.** H1's scope concession is about **Term 3 of Z19984826 only**. Z18168236 has its own scope reply (§5.1 "First, neutral mutations do not explain adaptation…"), which concerns adaptive differences. The paper nonetheless compares 487 with 20M (§4.4), so it is ambiguous. H3 shows that no cost-of-selection model pays 17.5M–205M selected fixations. That is true of any cost model and **uninformative about the A/B argument**, which branch B decides. Note that Day's 2026-05-07 post says observed substitutions are mostly "neutral fixations (which are the great majority)".
5. **The Day-favourable α result.** Hard-selection cost binds once a_nc ≳ 0.1–1%. Day has not argued this with α. **keruru (KR-09, ally label, January 2026, superseded)** ran the same comparison with an unsourced 700,000, so the first pass's "nobody in the corpus has stated" is withdrawn. The a_nc this needs is supported by no source in the corpus, and is below the resolution of any estimate.

**Allies**
- **Hössjer (H5).**
  - His conditional is **mechanically confirmed**: if many fixations were selected, a parallel reproductive cost applies; that is D1a.
  - 15,800 over 450,000 generations (0.035 per generation) is payable at R ≈ 2–3 (D = 20; long-run φ needs R ≈ 3).
  - 15,800 is close to GAP-01's coding-only maximum (1.2×10⁴), so it is compatible with a coding-only reading too.
  - "Perhaps" is a hedge, not a target. The cost step remains asserted, not computed.
- **keruru KR-09.** 700,000 needs ln R ≈ 47 at D = 20 and T = 300,000. It is unpayable under hard selection; the count is unsourced.

**Critics**
- **Hancock (Gutsick Gibbon video; the primary source behind KITTENS §11).**
  - States the hard/soft scope ("only applicable for hard selection models", 02:07:18).
  - Draws the poorly-adapted vs well-adapted distinction (02:08:20).
  - States the replacement mechanism behind ln R/D in words (02:11:51).
  - Makes the intermediate-frequency point (02:12:32). In H3 terms that is D ≈ 2–5, the one route that brings a_nc ≈ 1% to the edge.
  - Credited for all four, unquantified.
- **Nesslig20 (H6).**
  - "Does not apply to drift" holds.
  - His pointer to Matheson et al. 2025 ("other solutions that allow selection to exceed the limit") is the right source for the missing selective-death share. Matheson measures 8.5–95% in one plant, unrepresentative by the authors' own caveat, with no human value.
  - He gave no adaptive count.
- **KITTENS (RE-2).**
  - "Applies to hard selection" and "selected substitutions only" are correct.
  - "Far weaker under soft, competitive selection": **in H3's own model, soft selection has no demographic cap by construction**, so the clause is consistent with the model on cost. Whether a rate limit remains under soft selection depends on the implementation. R4-H-C2's soft selection draws survivors from R·K juveniles, so its differential is capped by R, and it tracked more slowly than hard.
  - "Modest and contested" is compatible with GAP-01, but KITTENS gave no count.
- **Formula.** No critic gives the ln R/D formula or the Nei/Felsenstein spacing. Hancock gives the mechanism; Nesslig20 points to the parameter's source.
- **Mansfield** (MF-08, "biologically naive"). Not credited: no claim about the cost limit.

**Literature**
- Nunney's M-dependence: reproduced qualitatively, with the low-M side in §4.6.4.
- Keightley: hard U = 2.2 is incompatible with R ≤ 9. This supports Keightley's conclusion that the load is not hard, and therefore cuts *against* using a hard load for Day.
- Felsenstein's 97-generation spacing reproduces exactly.
- Matheson's k = 1.1 mapping matches §1.2.

## 7. Caveats
**Not modelled, with direction**

| Resolution | Source | Direction | Status in H3 |
|---|---|---|---|
| Soft / density-dependent selection on the adaptive loci | Wallace (PA-09), Nunney 2003 (H2) | removes the demographic cost; a rate limit may remain, depending on implementation | not modelled (deleterious soft only) |
| Absolute-fitness gain without prior deterioration | Hancock 02:08; Nunney | no demographic cost | not modelled (treadmill only) |
| Truncation / synergistic epistasis | Maynard Smith 1968 (PA-04), Sved 1968 (PA-05), Kimura & Crow 1969 (PA-06), Crow & Kimura 1979 (PA-15) | lowers the cost (R4-H-C2: synergistic epistasis cuts the hard-load threshold from F_max ≈ 18 to 12 at U = 2.2) | not modelled; costs additive by construction. Day disputes this via the Bernoulli Barrier (Z19984826 §3.3.1), and the G1 review disputes Day's variance argument |
| Standing variation / intermediate p₀ | Hancock 02:12:32; GAP-02 | lowers D (break-even table §1.6) | D = 5 / 10 rows only |
| Polygenic shifts | KR-09, GAP-02 | no fixation needed | not modelled |
| DFE of s, mixture of s | Uricchio 2019 (GAP-01, unverified here) | φ for a mixture lies between the s-specific values | single s per run |

**Assumptions and whom they favour**
- **Day:** treadmill cost accounting; additive costs; D ≥ 10 by default; R = 1.1 as anchor; s = 0.01 for the φ tables; bins overstate background selection; N < 20 extinction; K = 1000.
- **Critics:** ceiling regulation (free compensatory fecundity); immediate re-seeding (high supply); soft deleterious load (by construction no cost); no sexes or age structure.

**Other caveats**
- Constant-hazard extrapolation of S(T) from runs of at most 102k generations.
- K-dependence of φ is weakly tested.
- s ≤ 0.003 runs have 2Ns ≤ 6 at K = 1000.
- Hard-load runs start at N = K with the load at balance, so N drops by a factor e^U in generation 1. At K ≥ 4000 this bottleneck is survivable; at K = 1000 it is part of the meltdown.
- Not run: the cheap soft-adaptive variant the critic review suggested. In this model it would trivially show no cap. The rate-limit question for soft selection is R4-H-C2's model and is left there.

## 8. Suggested verdict edits (vocabulary only; comments state the condition)
| Claim | Internal | Fidelity | External | Comment |
|---|---|---|---|---|
| H | holds (keep) | partial (keep) | contested (keep) | H3: the shared-budget structure (Σs ≤ s_max) holds. The 10% is Haldane's assumed parameter (R ≈ 1.1); the budget is ln R under ceiling regulation. At R ≈ 1.1 the rate is within a factor of about 1–3 of 1/300: 10k λ50 = 0.00340 [0.00300, 0.00379]; it fails over 40k; long-run about 1/530–1/1,050 (circular in R; needs a soft deleterious load). Under hard adaptive and soft load selection: coding-only K_a is payable for R ≳ 1.2–3; a_nc ≥ 1% is not, at D ≥ 5 and R ≤ 10². Untested under soft selection, absolute-fitness gain or epistasis. 17.5M–205M: unpayable under any cost model (uninformative about A/B). |
| H1 | holds (keep) | n/a | supported (keep) | Scope is Term 3 (Z19984826) only; H has its own §5.1 reply. Day here calls neutral fixations "the great majority". |
| H2 | n/a | accurate (keep) | contested (keep) | M-dependence reproduced in both directions: D ≈ 6.5 (M = 1), 10.5 (0.3), 17–22 (0.1), 39–52 (0.03), 99–163 (0.01), i.e. ≈ 15 + 1/M at low M. At M = 0.01 even R = 2 sustains ≈ 1/430 only. M ≥ 1 needs about 4×10³ target sites per locus (`derived:`). Human M unsourced. |
| H5 | non-sequitur (keep) | pending (keep) | contested (keep) | The conditional is mechanically supported (shared budget). 15,800/450k is payable at R ≈ 2–3 under hard adaptive and soft load selection. The cost step is still uncomputed by Hössjer. |
| H6 | holds (keep) | partial (keep) | supported (keep) | Add: his Matheson 2025 pointer is the right source for the missing selective-death share. |
| H7 | n/a | n/a | supported (keep) | Hard U = 2.2 is incompatible with R ≤ 9 (analytic; R = 10 extinct at K = 4000). It is compatible with R = 20 at K = 4000 / 10⁴, where the K = 1000 extinction was an artefact. Hard U = 0.35 removes R ≤ 1.42 if the whole class is hard-selected. These are bounding cases. |
| H8 | holds (keep) | pending (keep) | contested (keep) | 10k window: R = 2 form matched if R = 2 is intended; over 252k it overshoots. s_max·d = ln R is the audit's mapping. The R-independence that D2 tested was not claimed by Day. |
| ROOT-M (row 1, natural selection) | pending (keep) | n/a | pending (keep) | Under hard adaptive treadmill selection with soft load: the cost of selection binds Day's 17.5M–205M (any cost model) and a_nc ≳ 1% at D ≥ 5. It does not bind coding-only α at R ≳ 1.2–3. Untested under soft selection, absolute-fitness gain or epistasis. Turns on a_nc (below estimator resolution) and on R (unsourced). |

## 9. Review resolution
| Review item | Severity | Resolution |
|---|---|---|
| Correctness M1 (10k window used as a lifetime rate) | MAJOR | Stage L, 100k-generation hazard at s = 0.01: φ_252k = 0.30 / 0.57 / 0.59 / 0.73 (R = 1.1 / 1.5 / 2 / 3). §5 rebuilt; 10k quantities labelled λ50(10k); "1/300 reproduced" replaced (§6 Day 2, §8 H). |
| Correctness M2 (φ ≈ 1 at s = 0.003 promoted) | MAJOR | Stage W (s = 0.003, 56k generations, x up to 1.25): φ_252k = 0.69 (R = 1.1), 0.94 (R = 2). Stage X (s = 0.001, 45k generations): no deaths up to x = 1.25, so φ ≈ 1 relative to realised D, but the long run is unresolved (h < 2×10⁻⁵; 2Ns = 2). "Upper bound reached" removed; φ(s, T) presented as a range. |
| Correctness M3 (favourable M only) | MAJOR | Stage M at M = 0.01, 0.03, 0.3: D ≈ 15 + 1/M at M ≤ 0.03 (39–163); M = 0.3 gives 10.5. S6 reworded; the M ≥ 1 target-site arithmetic is added; the low-M side is listed as Day-favourable. |
| Correctness M4 (hard-load K artefact; H2-hard non-heritable) | MAJOR | Stage H at K = 4000 / 10⁴: U = 2.2, R = 20 persists (artefact confirmed); R = 10 extinct at λ = 0 (marginal); U = 0.35, R = 1.5 persists at λ = 0 but dies at xh = 0.5. D3 limited to R ≤ 9 (analytic); H2-hard comparison withdrawn. |
| Correctness m1 (λ50 grid coincidence) | MINOR | Logistic fit with profile CI (§4.1). |
| m2 (two-point grids) | MINOR | B/C/V/S bracketed only; 1/420 and 1/78 withdrawn. |
| m3 (S3 R = 1.5) | MINOR | Scored as a marginal miss. |
| m4 (S5 R = 1.5) | MINOR | Scored as failed or untestable; K = 4000 run in H. |
| m5 (S4 not resolvable) | MINOR | Rescored. |
| m6 (10/16 → 9/16) | MINOR | Corrected. |
| m7 (U = 0.35 all hard) | MINOR | Condition added. |
| m8 (packet mechanism asserted) | MINOR | Packet model run: φ within 10–13% of the IBM (§4.6.6). |
| m9 (wf_D 2s·q bias; "+1"; SEs) | MINOR | Exact charge with SEs (§2); "2 ln 2N ± 2"; prior literature credited. |
| m10 (s_max·d = ln R is the audit's mapping) | MINOR | Labelled in §1.2, §6 and §8; D2 "if R = 2 is intended". |
| m11 (host and md5 provenance) | MINOR | md5 and versions stored in `h3_fx.host` / `h3fp.host`; the timing of `h3_local.host` noted. |
| Steelman-Day 1 (soft-load proviso carries the result; hybrid) | MAJOR | Headline matrix with hard/hard rows; "hybrid = audit's construction" stated (§5); hard-load K test (H). |
| Steelman-Day 2 (R unanchored) | MAJOR | Anchors added: Haldane 1.1 (Matheson k = 1.1), Day s_max ≈ 2, Day total fertility 6–8 ⇒ R ≤ 3–4. No sourced net hominid R exists. |
| Steelman-Day 3 (window, φ ≈ 1 column, "reproduced") | MAJOR | Long-window runs (L, W, X); R_min tables now long-run; "reproduced" reworded. |
| Steelman-Day 4 (R-independence not claimed; structure vindicated) | MAJOR | D1 split into D1a (held) and D1b; §6 Day 1 rewritten; headline states it. |
| Steelman-Day 5 (H1 scope; A/B untouched) | MAJOR | H1 scoped to Term 3; Z18168236 §5.1 quoted; 17.5M–205M stated as uninformative about A/B. |
| Steelman-Day 6 (a_nc below resolution; Hössjer's conditional) | MAJOR | Stated in the headline and §5; Hössjer credited as mechanically supported; 15,800 ≈ coding max; "perhaps" a hedge. |
| Steelman-Day 7 (no headline) | MAJOR | Headline box added. |
| Steelman-Day 8 (critic credit) | MINOR | "Fits (critics' side)" heading removed; KITTENS "consistent with" reworded. |
| Steelman-Day 9 (Day-favourable label; D truncated) | MINOR | Two-way assumption list (§7); D = 5 and break-even D added; low-M side in §4.6.4. |
| Steelman-Day 10 (background-selection effect not carried over) | MINOR | §4.2 "not detectable at this resolution"; ln R_min × 1.07–1.15 in §5. |
| Steelman-Day 11 (d-factor) | MINOR | 487 = 1/667 per nominal generation; R ≈ 1.02–1.05 mean-field. |
| Steelman-Day 12 (D = 10 as free) | MINOR | Each D row labelled with its unsourced input (p₀, M). |
| Steelman-critic 1 (conditional verdicts; resolutions not named) | MAJOR | Condition on every verdict row; "not modelled" table; Hancock and Nunney credited for the distinction; KITTENS clause rewritten; soft-adaptive run not done, with reason (§7). |
| Steelman-critic 2 (R = 1.1 is an assumption; needs soft load; Day s_max) | MAJOR | Renamed "Haldane's assumed 10%"; soft-load requirement and s_max ≈ 2 note added; "R < 9" now described as the excluded hard-load bounding case. |
| Steelman-critic 3 (D ≥ 20 default) | MAJOR | D = 5 rows; break-even D table; Hancock's intermediate-frequency point credited; Day 5 reworded with KR-09. |
| Steelman-critic 4 (truncation / epistasis) | MAJOR | Named in §7 with direction, R4-H-C2 epistasis result and the G1 cross-reference; not modelled. |
| Steelman-critic 5 (hard-load results; single s_d) | MAJOR | D3 limited; hard rows labelled bounding cases (PA-16, PA-17); K = 4000 / 10⁴ run. |
| Steelman-critic 6 (credit gaps) | MAJOR | Hancock (four points), Nesslig20 (Matheson); "a value of R" removed; "no critic gives the formula" kept. |
| Steelman-critic 7–14 | MINOR | 7: λ50 × 300 now has a CI and no bold. 8: P3 called underpowered. 9: long window run. 10: KR-09 reconciled. 11: re-seeding listed as critic-favourable; φ for an s mixture bracketed. 12: s = 0.003 written "φ ≳ 0.75–1" plus W. 13: audit mapping labelled. 14: M target-site arithmetic added. |

---
id: A
title: "MITTENS rate-limit formula F_max = (t_div x d) / (g_len x G_f)"
side: day
branch: A
parent: ROOT
edges: [{type: supports, target: ROOT}]
load_bearing: true   # ROOT is a conjunction over mechanisms; if branch A fails, selection is an admissible mechanism and ROOT fails.
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds
  fidelity: n/a
  external: "contested"   # asexual saturation real (logarithmic); recombining-genome use of G_f not supported in F2's tested regime; LTEE-scale factor extrapolated
---

## Statement (verbatim)
> F_max = (t_div × d) / (g_len × G_f) F_max = maximum achievable fixations t_div = divergence time (in years) g_len = generation length (in years) d = Selective Turnover Coefficient G_f = generations per fixation

Source: [Response to Dennis McCarthy, Round 2](https://voxday.net/2026/02/04/response-to-dennis-mccarthy-round-2/) (key B2026-02-04), blog, 2026-02-04, ¶10. Day introduces it as "the core equation that is integral to MITTENS". Zenodo texts (Z18441321, Z18452504) use the equivalent "Achievable = (Generations x d) / G_f". The 3.0 paper (Z23003785) uses 252,000 nominal generations / 1,322 with no d term (see A4d).

## Formal statement
F_max = (t_div_years · d) / (generation_time_years · G_f)

Parameters (keys in `parameters.yaml`): `divergence.t_div_years`, `generation_time_years`, `selection.turnover_d`, `ltee.gens_per_fixation`. The claim compares F_max with the required count R (`divergence.required_fixations`, per lineage). Shortfall = R / F_max.

`derived:` (recomputed 2026-10-07, python3 -I; scratch script, not committed). Every headline number on the Day side, by version:

| Version | Inputs | F_max | Shortfall | Reconciles? |
|---|---|---|---|---|
| 2019 blog (B2019-02-07) | 9.0e6 y / 20 y = 450,000 gens; G_f = 1,600 | 450,000/1,600 = 281.25 (text says 562 = 2 x 281; table says 125) | 30e6 − 562 = 29,999,438 "short" (reconciles with 562) | **No.** 125 is not reproduced by the table's own inputs (9,000,000/32,000 = 281.25; 125 would need 4.0e6 y). 562 needs an unstated doubling. |
| 2025 (Z18165980) | 325,000 x 0.45 = 146,250 effective gens; G_f = 1,600 | 146,250/1,600 = 91.4 (paper rounds to 91) | 20e6/91 = 219,780 (paper: 219,780-fold); 20e6/91.4 = 218,803 | Yes (rounding of 91.4 to 91). |
| 3.0 (Z23003785) | 6.3e6/25 = 252,000 gens; G_f = 1,322; no d | 252,000/1,322 = 190.6 (paper: 191) | 205e6/190.6 = 1,075,437 (paper: 1,075,000) | Yes. |
| 3.0 SNV-only (s7.3) | R = 17.5e6 | 191 | 17.5e6/190.6 = 91,806 (paper: 91,600) | Yes (rounding). |
| Hössjer (HO-01) | 9e6 x 0.45 / (20 x 1,600) | 126.6 (he writes 127) | — | Yes. |
| Duffy (DU-02) / DeDzjang (DZ-02) | 252,000/1,400 | 180 | — | Yes. |
| Tree of Woe (TW-01) "202,500 generations" | 450,000 x 0.45 = 202,500 | — | — | Reconciles as 2019 gens x d (derived; the interview does not show it). |

Sensitivity (derived): over the t_div and g_len ranges in the sources (5.5 My/32.5 y = 169,231 gens to 9 My/20 y = 450,000 gens), N_gen varies by 2.7x. The shortfall claimed is 1e5 to 1e6. The input ranges for A1 therefore cannot by themselves close the gap.

## Assumptions
- Stated: G_f is a measured aggregate throughput that already includes parallelism and all mechanisms (see G1, A2); the LTEE rate is a ceiling for sexual mammals (A2e); R is a per-lineage count (A3).
- Implicit: G_f is constant in time and transfers between organisms with different genome size, mutation supply and recombination (A5). d, when used, is a constant multiplier on generations (A4). Linear scaling of fixations with generations: no depletion of standing variation and no change in selection regime.

## Responses
- Against: Hancock (GG-01) reads the formula as sequential (see G2). Critics argue the LTEE rate does not scale to humans (A5, A5a, A5b). Camestros (CA-07, CA-11): G_f is an average, not the fastest fixation rate (A2d). Camestros reviewed only the first edition (CA-14 "core argument hasn't changed since February 2019" is contradicted by the version drift, see A2b, A3a, A4d).
- In support: Camestros (CA-02): "Aside from whatever d is, the arithmetic itself isn’t wrong". Hössjer (HO-06): "I agree with this conclusion, also after adjusting the MITTENS equation for the different mutation rates of humans and E. coli." Keruru (KR-09) endorses the thesis (LLM-assisted; advocacy).
- Weaknesses in the responses: Hössjer's residual ~2x gap (A5a) rests on putting d = 0.45 inside the neutral rate, which is not standard; without d the figure is 16.9M vs 20M. The KITTENS decomposition (A5b) assumes linear scaling of adaptive fixations with mutation supply and says so (RE-09). Camestros's "arithmetic isn't wrong" is a statement about the 2019-edition arithmetic, not about the 2026 numbers.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Good et al. 2017; Tenaillon et al. 2016 (source of G_f) | see A2, A2g | unverified (Good: the "≥95%" rule is not in the main text) |
| Yoo et al. 2025 (t_div, R) | see A1a, A3x1 | t_div accurate; 410 Mb not-found |

## Pre-registered prediction
No check has run on this claim as a whole. Component checks are linked from A1–A5.
- Under the claimant's model: F_max is an upper bound on fixations by selection; R/F_max >> 1 for any version (1e5 to 1e6).
- Under the opposing model: F_max is not an upper bound for a recombining genome with 38.4 new mutations per haploid genome per generation (versus 4.1e-4 for E. coli), so a forward simulation with human-scale supply and parallel sweeps will fix far more than F_max.
- Proposed check (A-sim, not run): Wright-Fisher forward simulation, N = 1e4 (scaled), L loci, per-generation beneficial supply U_b swept over 4.1e-4 x [1, 1e2, 1e4, 9.4e4] of the LTEE value, recombination off versus free; record fixations per generation. A prediction that would change a verdict: if fixations per generation grow roughly linearly in U_b with free recombination, the unscaled formula is not a ceiling (verdict external: contradicted); if it saturates near 1/1,322 regardless of U_b, the ceiling reading (A2e) gains support.

## Check
R4 A-sim (`a_ltee_scaling.py`, F2 `f2_multilocus.py`; research/checks/results/R4-F2-A.md): formula arithmetic unchanged. Using LTEE G_f as a global constant is not supported for recombining genomes in F2's tested regime (free recombination R_int 0.975 at 272 active loci; the LTEE-scale factor 1.5-172x is an EXTRAPOLATION). For asexual genomes a saturation is real but logarithmic (a = 0.23-0.34 per 100x supply). Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)
Earlier note: Script: none yet (arithmetic audit run in scratch only). Result: arithmetic reconciles for 2025 and 3.0; 2019 table (125) and text (562) do not reconcile with each other or with 281. Review: pending.

## Simulator variables implied
- `t_div`, `g_len`, `G_f`, `d` as user-controllable inputs; displayed output F_max and shortfall R/F_max for each version preset (2019, 2025, 3.0).
- Toggle: serial reading (T/latency) versus aggregate reading (T/G_f).

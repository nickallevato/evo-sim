# Compute manifest: the seven open simulation objects (P3, part 1)

Written 2026-11-26 under brief `research/checks/briefs/X-MATHRESOLVE-analyst-15.md` (Gap: X-MATHRESOLVE). This is a manifest only. No check is designed, registered or run here, and no field moves. Each row that needs compute becomes its own `design-check` task. Costs are the `compute:` estimates in `objects.yaml`. All of them are **unmeasured**. Where an earlier run gives a measured anchor, it is quoted as an anchor and is not an estimate for the new run. The objects are taken from `research/tools/math_map.py` (simulation: open 7) and `objects.yaml`. Load-bearing is read from `docs/research/hierarchy.yaml` (`load_bearing: true`).

**Read first (for the lead).** No compute row can move an open field on a load-bearing node:
- M-505's only load-bearing user is E6. E6's open field (external `pending`) waits on the owner's fetch of Good 2017 clade-aware state files (`gap-blockers.yaml`, row E6). That is a data question, and no simulation answers it. E7, E9 and A5b are not load-bearing in `hierarchy.yaml`.
- M-604's load-bearing user is F2. F2's fields are all set (external `contested`), and F2 has no exit-gap row.

So compute here closes objects for X-MATHRESOLVE and refines fields on nodes that are not load-bearing. Whether that is gap work under the "Do not" list in `OPERATING-PROCESS.md` ("a field that is already set") is the lead's call. The other route is citation plus a recorded residual for the R5 sensitivity table (X-VARLIST).

## 1. M-505: mutator sublinearity and its transfer to sexual genomes (load-bearing)
- **Statement:** a 100x mutation rate raises LTEE fixation throughput only 8.5x, 16.9x or 19.7x (by counting rule). Does that sublinearity carry over to recombining vertebrates? `used_by` [E, E3, E6, E7, E9, A5b, A5d]. Load-bearing: **yes, through E6 only**.
- **Model:** forward Wright-Fisher with Poisson beneficial supply. The rate ratio is R(100x)/R(1x) and the exponent is a = ln R / ln 100. There are two arms:
  - (i) asexual, LTEE-calibrated, with a DFE instead of one s. R4-F2-A's single-s model gave a = 0.23-0.34, below Day's 0.47-0.61.
  - (ii) recombining, with a human map (36.8 M in 23 linkage groups), from F2's N = 1,000 up to as close to human scale as the smoke allows.
  The engine is `wf_f2.py` / `f2_fwdpy11.py`, shared with M-604.
- **parameters.yaml keys:** `ltee.Ne_effective` (verified: false), `ltee.mu_genome_ancestral`, `ltee.gens_per_fixation.*`, `mutation.supply_ratio_kappa`, `genetic_map_morgans.human_w_b_regime`, `population.Ne_modern_human`, `mutation.new_mutations_per_haploid_genome`. **Missing:** beneficial supply U_b and a beneficial DFE (LTEE and human), the mutator multiplier (100x), the observed ratios 8.5/16.9/19.7 and their counts, and `ltee.mutator_populations` (already an idea in the row).
- **Day-side** (throughput sublinear because beneficial mutations compete). Borne out if arm (ii) gives a well below 1 (for example R at most about 20x per 100x) at a human map and human-like supply.
- **Critic-side** (does not transfer to sexual genomes). Borne out if arm (ii) gives a near 1. R4-F2-A already found a = 1.00 under free recombination at N = 1,000 with at most 272 active loci.
- Both outcomes are reachable: R4-F2-A shows asexual sublinearity, and its 1.5 M single-group cell (R_int 0.57) shows that linkage can pull a down.
- **Decisive output:** exponent a in arm (ii) at a human map. It could move E7 external (`pending`) and the comments on A5b/A5d external (`contested`). It does not move E6.
- **Settled already?** Partly. The asexual-versus-free-recombination contrast is in `research/checks/results/R4-F2-A.md` ("A interpretation"). The critic position in `objects.yaml` ("planned, not run") is stale. The open part is human scale, a realistic map and a DFE. **Compute needed** for that residual only.
- **Cost:** `objects.yaml` gives 4 CPU-h, 2 GB, unmeasured. Measured anchor: `a_ltee_scaling.py` reran in 11 min on 3 cores (R4-F2-A l.2). **Smoke:** one cell per arm at 1x and 100x supply, 2 replicates, real pool, every grid value, recombining arm at the largest N on the grid. It records CPU-s and peak RSS per cell.
- **Host:** na-workhorse. The recombining arm cannot run within the workstation limits.

## 2. M-604: parallel sweep capacity under interference (load-bearing)
- **Statement:** does the active zone cap simultaneous sweeps near 230 (Z18167588), or does R_int stay near 1 with free recombination and fall only with linkage? `used_by` [F2, Gc, Gd, H9]. Load-bearing: **yes (F2)**.
- **Model:** F2's forward multi-locus Wright-Fisher (L loci, Poisson U_b, single s), extended to the two untested legs named in F2's external comment and in R4-F2-A §F2:
  - (i) the active zone at human scale (n_mid of 10^3-10^4, against the tested maximum of 272), with a realistic map (36.8 M, 23 groups) and N up to 1e4. E4's validated scaling (c of 8 or less) may be used.
  - (ii) hard selection with linkage. This uses H2's treadmill (`h2_hard_selection_multilocus.py`, free recombination only) with a map added.
- **parameters.yaml keys:** `genetic_map_morgans.human_w_b_regime` (verified: false), `population.Ne_modern_human`, `selection.s_zeng_2021` (a negative-selection value; it can be used only as a sensitivity), `mutation.new_mutations_per_haploid_genome`. **Missing:** beneficial U_b and DFE, the chromosome count, the reproductive excess R for hard selection (H2 used 1.3-10), and the 230 figure itself (it is in the claim file only).
- **Day-side** (hard cap near 230). Borne out if R_int < 0.5 at n_mid ≥ 230 under the realistic map (F2 claim l.32, its own falsifier line). Reachable: the 1.5 M single-group cell is already at 0.57, and the 0.1 M cell is at 0.20.
- **Critic-side** (parallelism with interference, no hard cap). Borne out if R_int ≥ 0.5 at n_mid ≥ 230 at human scale.
- **Decisive output:** R_int at n_mid ≥ 230 (and at human-scale n_mid) under the realistic map, soft and hard. It could move F2 external (set: `contested`), Gc external (`contested`), and Gd and H9 external (`pending`, not load-bearing).
- **Settled already?** The N = 1,000 soft-selection leg is settled: `R4-F2-A.md` (R_int 0.975 at 272 loci) and `R4-GAPS-04-07-02.md` (Weissman-Barton asymptotes). The free-recombination hard leg is settled: `R4-H2-hard.md`. **Compute needed** for legs (i) and (ii) only.
- **Cost:** `objects.yaml` gives 8 CPU-h, 4 GB, unmeasured. Measured anchor: `f2_multilocus.py` reran in 74 min on 3 cores (about 3.7 CPU-h) for a grid at N = 1,000 with at most 272 active loci. A human-scale cell is not comparable to that grid. **Smoke:** the largest-N, highest-supply cell with the 23-group map, soft and hard, 2 replicates, 2,000 generations, real pool. It records CPU-s per generation and peak RSS.
- **Host:** na-workhorse.

## 3. M-301: panel ascertainment and the sign of its bias
- **Statement:** the 1240k panel misses most new substitutions, and the sign of the bias for completions from intermediate frequency is unsettled. `used_by` [C1, C1a, C]. Load-bearing: no.
- **Model:** already fixed. **L5-C1a**, `research/checks/l5_c1a_randsnp.py`, pre-registered in 1c6e983, compares L5's ascertained panels (D2, D3, D_EU) with a matched random-SNP panel R (plus the R+ and R_sfs variants), using L5's sweep engine, sizes and seeds unchanged. The lead's ruling LC-R1..LC-R5 on which comparator governs was committed before the run (24b4e18, `briefs/L5-C1a-analyst.md`). There is nothing to design. The row is a launch: hostsmoke, then main, then analyse.
- **parameters.yaml keys:** `generation_time_years.day_2026`, `generation_time_years.day_2019`, `population.Ne_modern_human`, `mutation.mu_per_site_per_gen.pedigree_human`. **Held only as script constants (missing keys):** panel size 1,143,671 (v62), African discovery constant c2 = 0.846, the 10,500 BP frame and 7,000-year window, and the AADR call-depth table.
- **Day-side** (C1a: the bias "would favor detecting recent fixations"). Borne out if the expected detectable completions are higher on D2/D_EU than on R at the same s.
- **Critic-side** (the sign is not shown, or the bias goes the other way). Borne out if the ratio is at most 1. The registered R_sfs decomposition separates the frequency-spectrum part from the inclusion part, so both directions are reachable by construction.
- **Decisive output:** the ratio D2/R (and D_EU/R) of expected detectable completions for Z50, Z10 and B10. It fills reading (iv) "not computed" of the C1a Readings table (R4-L5.md §8) and could move C1a external (`contested`, set).
- **Settled already?** Leg (1) is settled: the panel misses new substitutions, but linked SNPs register strong sweeps, and the swept site is on the panel in 8.8-24.7% of standing completions (`R4-L5.md`, Result 5). Leg (2), the sign, is **compute needed**.
- **Cost:** `objects.yaml` gives 0 CPU-h, which is **wrong**. The script's own estimate is at most 12 CPU-h, 7 workers, about 2-2.5 h wall (docstring §7, scaled from L5's measured 4.66 CPU-h). The local smoke at tiny sizes measured 15.8 s and 275 MB (`raw/l5c1a_smoke_local.out`, c152ab3). **Smoke:** the registered `hostsmoke <workers>` (real pool, full grid, tiny sizes). It has not been run.
- **Host:** na-workhorse (about 1 GB per worker).

## 4. M-405: path viability and path length (Eden, Crosby)
- **Statement:** every intermediate must be viable, and path lengths are bounded by the generations available, so only short paths count. Eden gives no path-length distribution. `used_by` [D2d, D3b]. Load-bearing: no.
- **Model:** none can be stated from held text. A walk on a synthetic landscape (NK, Kauffman-Levin) at hemoglobin scale gets its answer from the ruggedness the audit picks, an uncited input (rule F). So each side's band would be reached by the choice of input, not by the simulation (ST-05). D3b's own pre-registered test asks for "a measured distribution of path lengths ... on an empirical landscape (D2h)". That is data, not simulation.
- **parameters.yaml keys:** none. **Missing:** viable fraction, ruggedness, path-length distribution, sequence length. Eden's 120 steps and 420 nucleotides are in record M-406, not in parameters.yaml.
- **Positions:** Day says topology and path length decide the case. The critic says Eden gives no estimate of path length or of viability along the paths.
- **Settled already?** The viability and connectivity leg is settled on held empirical landscapes: `research/checks/results/R4-D1-spike.md` (GB1: one giant component with 99.8-99.9% of functional variants; 98.5% have an uphill SNV neighbour; 44% have a monotone SNV path to the best variant).
- **blocked:** no held source gives a landscape or a path-length distribution at Eden's scale (a 120-step minimum distance). The object reads as a `data-check`, not a simulation. Reclassifying it is for the lead; `objects.yaml` is not edited here.
- **Cost:** `objects.yaml` gives 0 CPU-h. Not applicable.

## 5. M-501: founder-event CMMRD hazard
- **Statement:** about 2.3% per founder event at N = 100, and 90.5% over 100 independent events. `used_by` [E, E3]. Load-bearing: no.
- **no compute: cite `research/checks/results/R4-E.md`.** That check settled each number in the statement:
  - the per-event hazard reproduces (2.0% exact, 2.38% `hwe`, 2.75% literal);
  - the premise (at least 2 carriers needed) and the 39% conditional are wrong, and the two errors partly offset;
  - over 100 independent events P(≥1 aa) = 93.9%;
  - the consequence leg is answered by the threshold sweep: at N = 100 a ≥2% cohort-fitness dip is 6x rarer than one affected birth, and a ≥5% dip is 620x rarer.
- The critic position in `objects.yaml` ("consequence ... open") is partly stale. Two legs stay untested (R4-E, "Caveats"):
  - correlated (non-independent) founder events;
  - E3 §4's pathways (heterozygote load, lethal equilibrium, meltdown) and homozygote fertility.
  No held text gives them a model with parameters, so they go to the R5 sensitivity table and not to compute.
- **Cost:** `objects.yaml` gives 1 CPU-h, 1 GB. Moot.

## 6. M-413: Hössjer, Bechly and Gauger 2021 regulatory waiting time
- **Statement:** with several genes, a specific new site and non-beneficial intermediates, the wait far exceeds 9 My. The answer flips under beneficial intermediates, redundant sites or a non-specific gene set. `used_by` [D15]. Load-bearing: no.
- **no compute: cite `research/checks/results/R4-D15.md`.** The sweep is complete (714 of 714 cells, R = 60; p9 and p90 exact in every cell). Baselines reproduce Hössjer's Tables 4, 5 and 9 to within 0.3%. The flip conditions in the statement are R4-D15's own "Where it fails" findings.
- R4-D15's "Not done" lists three optional runs. Run 3 is "not needed" by its own text; runs 1 and 2 refine a mean and a ratio and do not decide the object. D15 external (`contested`) waits on literature leads, not compute.
- **Cost:** `objects.yaml` gives 0 CPU-h. Moot.

## 7. M-506: s_min = 2 K_new ln(2 Ne) / T and its three zones
- **Statement:** K_new serial sweeps in T generations need s ≥ 13.8 K/T at Ne = 500, giving SAFE, DANGER and IMPOSSIBLE zones. The formula is a floor that ignores clonal interference, and B0.4 shows (2/s) ln 2N overstates the conditional fixation time by 1.6-2.2x. `used_by` [E2]. Load-bearing: no.
- **Model:** the E2 claim's own spec (l.64). Forward simulation of K_new independent loci (10-30) in an Ne = 500 isolate, with new beneficial mutations at mu_b per locus per generation and s in {0.005, 0.01, 0.05, 0.1}. It measures the time to complete all K_new sweeps against T = 5,000 and against the formula. Run with and without linkage.
- **parameters.yaml keys:** none of E2's inputs. **Missing:** Ne 500, T 5,000 (Table 1b), K_total 20-200, F_sv 0.2-0.7, P 2-10, mu_b 1e-8 to 1e-6 per locus.
- **Day-side** (s_min is a floor, and no PE parameter set is SAFE). Borne out if simulated completion exceeds T at s < 0.01 for K_new ≥ 10.
- **Critic-side** (parallel loci lower the required s). Borne out if completion falls below T at s < 0.01 for K_new of 10-30.
- **Reachability pre-check** (arithmetic, this file): the establishment rate per locus is 2Ne·mu_b·2s = 2e-5 to 2e-4 per generation at mu_b = 1e-6 and s = 0.01-0.1, a mean wait of 50,000 to 5,000 generations against T = 5,000. So with new mutations only, the critic band may be unreachable inside the paper's own ranges. `design-check` must show both bands reachable before it registers anything (ST-05). The likely route is the top of the mu_b range with parallel loci, or a standing-variation arm, which the paper's K_new deliberately excludes.
- **Decisive output:** the completion time against T and against the s_min formula, per (K_new, s). It could move E2 internal and external (both `pending`).
- **Settled already?** The per-sweep timing factor is settled (`research/checks/RESULTS.md` B0.4, `beneficial_fix_time.py`). The multi-locus completion is **compute needed**.
- **Cost:** `objects.yaml` gives 2 CPU-h, 1 GB, unmeasured. **Smoke:** K_new = 30, every s on the grid, mu_b at both ends, 20 replicates, real pool. The independent-loci version might fit the workstation limits; only the smoke can show that.
- **Host:** na-workhorse by default. The linked version needs it.

## Summary table

| id | load-bearing | compute needed | est. CPU-h (`objects.yaml`, unmeasured) | host | order |
|---|---|---|---|---|---|
| M-505 | yes (E6 only; E6's open field is not moved) | yes, residual only (human-scale map and DFE); asexual/free contrast in R4-F2-A | 4 | na-workhorse | 1 |
| M-604 | yes (F2; field set, `contested`) | yes, residual only (human-scale n_mid, hard selection with linkage); N = 1,000 soft in R4-F2-A, R4-GAPS-04-07-02, R4-H2-hard | 8 | na-workhorse | 2 |
| M-301 | no | yes, launch of registered L5-C1a (1c6e983) | 0 (wrong; script estimate at most 12) | na-workhorse | 3 |
| M-506 | no | yes (reachability pre-check first) | 2 | na-workhorse (smoke decides) | 4 |
| M-405 | no | no: blocked (no held landscape at Eden's scale; reads as data-check); viability leg cite R4-D1-spike.md | 0 | — | — |
| M-501 | no | no: cite R4-E.md | 1 | — | — |
| M-413 | no | no: cite R4-D15.md | 0 | — | — |

Shared engine: M-505 and M-604 both use `wf_f2.py` / `f2_fwdpy11.py`. One host smoke can measure both if the two design tasks run back to back.

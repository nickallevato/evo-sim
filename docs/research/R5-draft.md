# R5 synthesis: first draft (sensitivity table, simulator variable list, exit-criteria status, balance audit)

> **PROVISIONAL DRAFT, dated 2026-10-09.** Pending D1 (sequence-space spike: raw outputs exist, no write-up or review), C1c (three reviews written, fix pass and integration not done), C1d (not started) and GAP-07c (not started). Nothing here changes a claim, a verdict or a check result. Every number is taken from `research/checks/RESULTS.md`, `research/checks/results/R4-*.md`, the claim files, `parameters.yaml` or the ledgers, and the source file is named. A number marked *derived here* is my own arithmetic on those inputs, with the formula given. Where a node has no established flip point the entry says "none established". This file is a working draft for the R5 stage in [`PLAN.md`](PLAN.md); it is not a verdict document.

**Reading guide.** Verdicts are written I / F / E for internal validity / model fidelity / external validity, using the vocabulary in `AGENTS.md`. "Direction" says which side a change in the parameter favours *for that node's conclusion*; it does not say who wins ROOT. File names without a path are in `docs/research/claims/` (claim files), `research/checks/results/` (R4 write-ups) or `research/checks/RESULTS.md` (early checks B0 to F1, B1b, B2a). "Day-side" and "critic-side" follow the `side` field in `hierarchy.yaml` (day, critic, ally, literature).

---

## 1. Sensitivity table: the 30 load-bearing nodes

`hierarchy.yaml` marks 30 nodes `load_bearing: true`: 21 Day, 5 critic, 3 literature (the audit-raised nodes B1c, B4a and H2), 1 ally (H5). Two are aggregates (ROOT, ROOT-M).

### 1.1 Summary

| Node | I / F / E (as of 2026-10-09) | Flip point established? | Main drivers |
|---|---|---|---|
| ROOT | pending / n/a / pending | none (aggregate) | all branches below |
| ROOT-M | pending / n/a / pending | none (row-level only) | adaptive share, R, linkage |
| A | holds / n/a / contested | yes, conditional (adaptive share 13-27%; count bracket 7-14x) | F_req, T, G_f, map length, adaptive share |
| A2e | non-sequitur / pending / contested | none established (1.5-172x extrapolation) | recombination, supply, LTEE N_e, units |
| B | pending / partial / contested | none (umbrella; see B1, B1c, B3) | start state, N_e(t), overlap |
| B1 | holds / n/a / contested | yes (4N_e vs T; size-change sign) | start state, N_e(t), T |
| B1c | holds / n/a / contradicted | none (every tested history gives an excess) | N_e,anc, modern N_e |
| B2 | pending / unverifiable / contested | yes, reading-dependent (G/N) | which probability, G/N_e |
| B2b | holds / unverifiable / contested | none established (V_k table only) | V_k, G, N_e/N |
| B3 | pending / partial / contradicted | partial (B&L range 0.59-1.70, contrived) | overlap, N(t) fluctuation, window |
| B3a | holds / misread / contradicted | none (P_fix = 1/M in exchangeable class) | exchangeability |
| B3g | holds / accurate / supported | none established (textual) | n/a |
| B4a | holds / accurate / contested | yes (N_e,anc about 1.3e5 closes the fit) | mu, T, N_e,anc |
| B5 | holds / accurate / contested | yes (sign of N change) | demography, overlap |
| B6 | holds / n/a / supported | yes (N_e,anc = 1e4 vs sourced) | N_e,anc |
| B7 | holds / accurate / supported | none established | exchangeability |
| C2 | non-sequitur / unverifiable / contested | yes (scale of s: factor d vs 1) | s scale, dominance, life table |
| C2a | holds / unverifiable / contested | yes (same) | s scale, selection class |
| E5 | pending / accurate / pending | none established (no check) | counting rule |
| E6 | holds / unverifiable / pending | none established (no check) | counting rule |
| F | non-sequitur / partial / contested | yes (linkage) | map length, 2N U_b, adaptive share |
| F1 | holds / n/a / contested | none (possibility, not feasibility) | regime |
| F1a | non-sequitur / n/a / pending | none established | s, N_e |
| F2 | holds / n/a / contested | yes (13-27% adaptive share) | recombination, selection mode, adaptive share |
| F3a | pending / misread / contested | none established | s, sign |
| H | holds / partial / contested | yes (a_nc 0.01-0.6%; R) | R, D, hard vs soft, a_nc |
| H1 | holds / n/a / supported | none (scope) | adaptive vs total |
| H2 | n/a / accurate / contested | partial (M) | M, hard vs soft |
| H5 | non-sequitur / pending / contested | conditional (R about 2-3) | R, a_nc |
| H8 | holds / pending / contested | none established | R, window length |

### 1.2 Node by node

#### Root claims

**ROOT** (extracted)
- **Conclusion as verdicted:** not verdicted. I pending, F n/a, E pending, "branches A-H and ROOT-M must be resolved first".
- **Drivers / flip:** none established for ROOT as a whole. Day's operational form gives a shortfall of 1,075,000 at G_f = 1,322 (`ROOT-no-mechanism-suffices.md`, `parameters.yaml` shortfall.mittens3_full). On the GAP-07b measured count (21.05M events per lineage, hg38 vs panTro6) the shortfall under the same rate model is 99,100-110,400 (`R4-GAP07b-alignment.md`; the note states it for the SNV-only reading), so the 7-14x count correction does not by itself remove a shortfall of about 1e5. That leaves the transfer of the LTEE rate (A2e, F2), the pipeline (B), and the adaptive share (H) as the places a conclusion can move.
- **Direction:** n/a.
- **Source:** `ROOT-no-mechanism-suffices.md`; aggregate of everything below.

**ROOT-M** (extracted)
- **Conclusion as verdicted:** pending / n/a / pending. The catalogue has 19 numbered rows: rows 1, 2, 3, 4, 6, 7, 9, 15, 17 computed or empirically bounded (9), rows 10, 11, 16 partial (3), rows 5, 8, 12, 13, 14 asserted but not computed (5), row 18 (relictation) accepted by Day (`ROOT-excluded-mechanisms.md`, "Totals").
- **Drivers / flip:** row 1 turns on a_nc (below estimator resolution) and R (unsourced) per the H3 note. Rows 2 and 6 carry the G1 and GAP-02 results (see section 1.3). The universal quantifier ("every other imagined mechanism") is untestable until each mechanism is named. No flip established at row level except those in section 1.3.
- **Direction:** a_nc above about 1% at D >= 5 favours Day; coding-only favours the critics (see H).
- **Source:** `ROOT-excluded-mechanisms.md`; `R4-H3-human.md`; `R4-G1.md`; `R4-GAPS-04-07-02.md`.

#### Branch A (rate limit)

**A** (reviewed)
- **Conclusion as verdicted:** I holds (arithmetic reconciles for 2025 and 3.0), F n/a, E contested.
- **Drivers:** T (450,000 in 2019; 146,250 effective in 2025; 252,000 in 3.0), G_f (1,600; 1,322; 1,400; 1,587), F_req (30M; 20M; 205M), d, recombination, adaptive share (`parameters.yaml`; `A-mittens-formula.md`).
- **Flip points:**
  - *Count.* Day's 205M is 9.7x the directly counted events, bracket about 7-14x (Day-favourable 7.2-9.5, critic-favourable 10.1-13.4, all post hoc). Events are not fixations and are not selected. Day's SNV-only 17.5M is 83% of measured events (`R4-GAP07b-alignment.md`).
  - *Finite-map limit* (Weissman and Barton 2012). The cap is a bracket: R/4 for an exponential DFE, R/2 for fixed s, up to about 3R in simulations, none depending on N or s. On Day's stated all-fixations model, 17.5-20M per lineage is 3.3-4.5x over R/2 and 6.5-9.1x over R/4 (R = 35-38 M). On the critics' model the asymptotes bind only above a 13-14% (R/4) or 25-27% (R/2) adaptive share. Day's own 99%-neutral 200,000 is 22-31x below R/2 (`R4-GAPS-04-07-02.md` section 1).
- **Direction:** all-fixations model, tight linkage, high adaptive share favour Day; a low adaptive share and free recombination favour the critics. "Which model holds is branch B" (claim file comment).
- **Source:** GAP-04 and GAP-07 (`R4-GAPS-04-07-02.md`), GAP-07b (`R4-GAP07b-alignment.md`), F2 / A-sim (`R4-F2-A.md`).

**A2e** (reviewed)
- **Conclusion as verdicted:** I non-sequitur, F pending, E contested.
- **Drivers:** recombination (asexual LTEE vs sexual), mutation supply 2N U_b, the LTEE N_e (3.3e7, unsourced), counting units (generations vs years, A2i, untested).
- **Flip points:** none established. Asexual interference is confirmed (supply exponent a = 0.23-0.34 per 100x), which is a point for Day and also the critics' own prediction. The free-recombination factor of 1.5-172x is an extrapolation. G_f depends on the unsourced N_e only logarithmically (7,306 at 1e6 to 1,159 at 1e8 at fixed U_b), but U_b is underdetermined over 3 orders of magnitude (`parameters.yaml` ltee.Ne_effective; `RESULTS.md` F2 / A-sim).
- **Direction:** asexual or tightly linked: Day. Free recombination: critics.
- **Source:** `a_ltee_scaling.py` in `R4-F2-A.md`; GAP-04 in `R4-GAPS-04-07-02.md`.

#### Branch B (neutral theory, pipeline, N vs N_e)

**B** (extracted; umbrella)
- **Conclusion as verdicted:** I pending, F partial, E contested.
- **Drivers / flip:** none for the umbrella; the sub-claims below carry the numbers. The sign of the transient depends on the direction of size change: expansion N0/5 to N0 gives cumulative 0.733 of U*T (analytic 1 - 4*dN/T), contraction N0 to N0/5 gives 1.259 (B1b, `RESULTS.md`).
- **Direction:** expansion: Day. Contraction or constant: critics.
- **Source:** `B-neutral-theory-cannot-rescue.md`, B1b, B1c, B3b.

**B1** (reviewed)
- **Conclusion as verdicted:** I holds, F n/a, E contested ("deficit exists only for new-mutation accounting from an empty start; contradicted for the human-chimp observable (B4a)").
- **Drivers:** start state (empty vs equilibrium), N_e history, T relative to 4N_e.
- **Flip points:** an empty start gives U(T - 4N) and an equilibrium start gives U*T (N = 100, U = 0.5, T = 1000: 304.4 vs 501.0, `RESULTS.md` B1). Derived here: the empty-start formula (T - 4N_e)/T is positive only if N_e < T/4 = 63,000 at T = 252,000 generations. Expansion deficit and contraction excess follow 1 -/+ 4*dN/T (B1b).
- **Direction:** empty start or expansion: Day. Equilibrium start or contraction: critics. The empty start is a counterfactual boundary case (steelman C1 framing).
- **Source:** B1 and B1b (`RESULTS.md`); B1c (`R4-B1c-B4a.md`).

**B1c** (reviewed; side literature, audit-raised)
- **Conclusion as verdicted:** I holds, F n/a, E contradicted. The empty-start premise is contradicted and Day withdrew it (B1d).
- **Drivers:** ancestral N_e (Yoo 2025: 1.98e5 HCB, 1.32e5 HCG), modern N_e (Prado-Martinez 2013: humans 1.31e4-1.62e4; common chimp 3.09e4-6.18e4), T = 252,000.
- **Flip points:** none established. Every tested step history gives an excess, K/(U*T) = 1.9-4.0; the new-mutation component is 0.84 at N_e = 1e4, equal to Day's (T - 4N_e)/T. It is the B1b telescoping identity applied to step histories, not an independent empirical result; no PSMC curve was extracted (Table S5 not retrieved); K counts alleles fixed in both lineages.
- **Direction:** higher N_e,anc: critics. Day's post-split formula for new mutations is confirmed. Day's later position (Education of a Population Geneticist, 2026-10-01 para 31 and 36) is a full pipe of 228,000 generations, implying N_e about 5.7e4 (`parameters.yaml` day_b1d_implied).
- **Source:** `R4-B1c-B4a.md`.

**B2** (reviewed)
- **Conclusion as verdicted:** I pending, F unverifiable, E contested.
- **Drivers:** which probability is meant, G/N_e, V_k, fill state.
- **Flip points:** the exponent -pi^2 is correct (B2a). The numbers depend on the reading. Reading 1 (conditional on fixation): the exact value exceeds Day's by 7x at G/N = 4, 54x at 1 and 1.6e3x at 0.25 (N = 200). Reading 2 (unconditional per new mutation): the exact 1.5e-3 is below Day's 0.085 at G = 4N. Either way it is a per-allele latency tail; the expected substitution count U*integral(F) equals U*T at equilibrium. The verbatim definition is still unverified.
- **Direction:** reading 1: critics (Day understates the chance). Reading 2: Day (the true chance is even smaller). Latency vs throughput: critics. The exponent itself: Day.
- **Source:** B2a (`RESULTS.md`); `B2-hard-limits-domain-of-k-mu.md`.

**B2b** (extracted)
- **Conclusion as verdicted:** I holds (arithmetic reproduces), F unverifiable, E contested.
- **Drivers:** V_k, G = T/g, the N_e/N map, census N. X = (V_k + 2)G/16 is 113,750 for humans (T = 6.5 My, g = 25, V_k = 5); the census 8.2e9 is 72,088 times X. V_k halved or doubled gives 22,500 or 60,000 for the human species window. The abstract's "about ten thousand" is 3.5-11x below the table's human ceilings. Wright's formula gives N_e = 0.57 N at V_k = 5, while Z18525547 and the Q&A use N_e 3,300-10,000.
- **Flip points:** none established. keruru's measured temporal N_e (B2e) would put the ceiling 700-820x higher, but it is an unreviewed draft with `[CHECK]` marks and replication is queued.
- **Direction:** larger V_k or smaller measured N_e / N: critics (more populations inside the domain where drift completes). Day's 4N_e < G framing needs census above X.
- **Source:** `B2b-ceiling-x-vk-g-over-16.md` (arithmetic audit only, no script); `B2e-keruru-measured-ne-vs-wright.md`; `sources/refresh-2026-10-09.md`.

**B3** (reviewed; umbrella of Day's k/mu values)
- **Conclusion as verdicted:** I pending, F partial, E contradicted for the listed values (N/N_e, 0.743, 32.3, 800,000); the qualitative Balloux-Lehmann effect is real but small.
- **Drivers:** overlap, N(t) fluctuation, window of cohorts, per-generation-time normalisation.
- **Flip points:** B&L eq. (3) reproduced in 9 scenarios. Fluctuation without overlap gives k = mu. At human-like parameters symmetric cycles move k by -0.3% to -2%; one-way growth raises the arrival of eventual fixers by 1.38x (transient); the contrived range is 0.59-1.70. RRME's 0.743 is window-dependent (0.868 at 2 cohorts, limit 0.598). The per-generation-time normalisation (0.81-1.11) is open (Lehmann 2014 not retrieved).
- **Direction:** overlap plus fluctuation: Day (credit for the effect). Discrete generations, or realistic magnitudes: critics.
- **Source:** B3b / B3c (`R4-B3b-C1.md`).

**B3a** (reviewed)
- **Conclusion as verdicted:** I holds (the algebra follows from its premise), F misread, E contradicted.
- **Drivers:** exchangeability; the V_k route to N_e.
- **Flip points:** none established inside the exchangeable class: P_fix = 0.00250, 0.00252, 0.00257, 0.00248, 0.00257 at N_e = 200, 160, 100, 40, 19, against Day's 1/(2N_e) of 0.0025-0.0268 (B3, `RESULTS.md`). In a time-varying overlapping model a mutant born in cohort i fixes with probability 1/N_i (P_fix*M_i = 0.973-1.018), the opposite sign to B&L's step (B3c).
- **Direction:** critics on probability; Day on timescale (N_e sets t_fix, t_fix/N_e about 3.95-4.07).
- **Source:** B3 (`RESULTS.md`); `R4-B3b-C1.md`.

**B3g** (reviewed)
- **Conclusion as verdicted:** I holds, F accurate, E supported. Day, 2026-08-27: Kimura's derivation never needed N_e.
- **Drivers / flip:** none established. It is a textual concession with no script. Q105 (Day's 2026-09-15 comment) restates 1/(2N_e) after the concession, and 32.3 mu reappeared on 2026-10-01 without a derivation (`ledgers/versions.md`; `B3g-...md`).
- **Direction:** critics.
- **Source:** claim file only.

**B4a** (reviewed; side literature)
- **Conclusion as verdicted:** I holds (d - 2*mu*T = theta_anc within about 0.3%; msprime agrees), F accurate, E contested.
- **Drivers:** mu (1.2e-8, range 1.1e-8 to 1.5e-8), T = 252,000, N_e,anc.
- **Flip points:** with mu = 1.2e-8 and T = 252,000, 2 mu T = 0.605% and d is 0.65% at N_e,anc = 1e4, 1.24% at 1.32e5 and 1.56% at 1.98e5, against the observed 1.23% (CSAC, including polymorphism; fixed at most 1.06%). Matching 1.23% at N_e = 1e4 needs T about 492,500 generations (12.3 My at 25 y) (`B4a-two-lineage-divergence-with-ils.md`). Derived here, N_e,anc = (0.0123 - 2 mu T)/(4 mu) = 1.30e5; at Day's implied 5.7e4, d = 0.605% + 4 mu N_e = 0.88%. The fit has three free parameters and Yoo's own mu is unrecorded.
- **Direction:** N_e,anc near 1.3e5: critics' decomposition (B6) fits. N_e,anc = 1e4: Day's "rounding error" (B6a) holds but d is half the observed value.
- **Source:** `R4-B1c-B4a.md`.

**B5** (reviewed; critic)
- **Conclusion as verdicted:** I holds, F accurate, E contested ("exact at steady state; transient and overlap effects").
- **Drivers:** demography direction, overlap, stationarity.
- **Flip points:** the stated totals all assume stationarity (B1c, B3b). The transient is bounded by about 4*dN/T (B1b: +26% contraction, -27% expansion at T = 3*4N0).
- **Direction:** stationarity: critics. Expansion or overlap with fluctuation: Day.
- **Source:** B1b (`RESULTS.md`); `R4-B1c-B4a.md`; `R4-B3b-C1.md`.

**B6** (reviewed; critic)
- **Conclusion as verdicted:** I holds, F n/a, E supported ("full pipe gives k = mu and d = 2 mu T + theta_anc").
- **Drivers:** N_e,anc.
- **Flip points:** B6a ("rounding error") is an arithmetic error at sourced N_e,anc (the ancestral term is comparable to 2 mu T) and holds only at N_e,anc = 1e4. CSAC's 14-22% polymorphic share matches the poly-but-different column (22-25% in config B).
- **Direction:** critics, conditional on the N_e,anc and mu inputs (open).
- **Source:** `R4-B1c-B4a.md`.

**B7** (reviewed; critic)
- **Conclusion as verdicted:** I holds, F accurate, E supported (neutral fixation probability is 1/(2N); Day's own Z22129121 says so).
- **Drivers / flip:** none established beyond the exchangeable class (see B3a). B7a (Kimura 1962) fidelity is partial.
- **Direction:** critics.
- **Source:** B3 (`RESULTS.md`).

#### Branch C (turnover coefficient d)

**C2** (reviewed)
- **Conclusion as verdicted:** I non-sequitur (as a fitted correction), F unverifiable (Coale-Demeny tables not retrieved), E contested.
- **Drivers:** the scale of s (hazard vs per-generation), d (0.45 fitted; 0.481-0.568 from Day's own s priors), dominance, life table (Siler stand-in).
- **Flip points:** d is the mean cumulative hazard at the age of mothers (0.789 vs 0.784). d*s is exact for hazard-scale s (within 1.5%); for per-generation s the factor is 1.000. "d = 1 for discrete generations" fails on Day's own formula (d = -ln L). d is not identifiable from three trajectories; the required d spans 0.45-13.5 across dominance and s (C2d). In C1c, d = 0.45 acts as neutral at N_e/0.45 and maps to Day's 21 only for a closed population at N_e about 6e4.
- **Direction:** hazard-scale s: Day. Per-generation s: critics.
- **Source:** `R4-H-C2.md` (c2 scripts); `R4-C1c.md` (unintegrated).

**C2a** (reviewed)
- **Conclusion as verdicted:** I holds (derivation correct for hazard-scale s), F unverifiable, E contested ("a unit conversion, not a separate correction").
- **Drivers / flip:** same as C2: s scale, selection class (viability vs fecundity), life table. Flip: hazard-scale vs per-generation s.
- **Source:** `R4-H-C2.md`.

#### Branch E (LTEE counting)

**E5** (extracted)
- **Conclusion as verdicted:** I pending, F accurate, E pending.
- **Drivers / flip:** counting rule (snapshot, first crossing, strict whole-population), sampling endpoint, clone sample size. None established: "Script: none yet" (`E5-ara2-ara5-counts.md`). The critics' point (-906 true fixations in Ara-2; Ara+5 38 to 0) shows the estimator is not a count; the argmap note on d002 records that the critics have not shown the non-mutator headline moves much, and A-sim reproduces G_f about 1,300.
- **Direction:** undetermined.
- **Source:** claim file; `argmap/defeaters.yaml` d002.

**E6** (extracted)
- **Conclusion as verdicted:** I holds, F unverifiable, E pending.
- **Drivers / flip:** strict lineage-aware count 5,496 against the naive 95% rule 8,679 (`E6-strict-vs-95-counts.md`); G_f 1,322 vs 1,587 (`parameters.yaml`); Day's own derived shortfall 1.29 million-fold at 1,587 vs 1.075 million at 1,322 (`sources/refresh-2026-10-09.md` D-3). None established as a verdict flip; no script (`e6_ltee_counts.py` is only planned).
- **Direction:** the strict count is the critics' methodological demand and it raises Day's shortfall (self-correction by Day, Z23105291).
- **Source:** claim file; `parameters.yaml`.

#### Branch F (latency vs throughput, interference)

**F** (reviewed)
- **Conclusion as verdicted:** I non-sequitur as a throughput bound, F partial, E contested.
- **Drivers:** linkage and map length, 2N*U_b, adaptive share.
- **Flip points:** clonal R_int falls 0.645 to 0.088 over 2N*U_b 0.1 to 32; a 0.1 M map gives 0.204; one 1.5 M group 0.572; free recombination 0.975 +/- 0.005 at 272 active loci (fwdpy11 agrees). Interference binds only with linkage (claim comment). The W&B asymptote binds above a 13-27% adaptive share (see A).
- **Direction:** tight linkage: Day. Free recombination: critics.
- **Source:** F1 (`RESULTS.md`); `R4-F2-A.md`; `R4-GAPS-04-07-02.md`.

**F1** (reviewed; critic)
- **Conclusion as verdicted:** I holds, F n/a, E contested.
- **Drivers / flip:** none. Rate 0.3972 +/- 0.0018 vs predicted 0.3960; t_fix 847 generations vs spacing 3; in-transit about 336 is computed, not measured. The regime (20 new beneficial mutations per generation, no interference, no cost) shows pipelining is *possible*, not that it is *feasible*.
- **Direction:** critics on logic; Day on feasibility (tested in F2 and H).
- **Source:** F1 (`RESULTS.md`).

**F1a** (extracted)
- **Conclusion as verdicted:** I non-sequitur, F n/a, E pending.
- **Drivers / flip:** none established, no check. The Q&A divides by 19,800 generations per fixation, which is (2/s)ln(2N) at s = 0.001 and N = 1e4, against a diffusion value of 8,480 (B0.4: 8,532 by the corrected asymptote). Day also says G_f is a throughput measurement (blog 2026-10-01, per fetcher).
- **Direction:** critics on the mixed use of a latency; Day's G_f statement is consistent with throughput.
- **Source:** `F1a-day-reply-throughput-and-serial-use-19800.md`; B0.4 (`RESULTS.md`).

**F2** (reviewed)
- **Conclusion as verdicted:** I holds, F n/a, E contested.
- **Drivers:** number of loci, recombination, soft vs hard selection, s distribution, U_b.
- **Flip points:** no collapse to 272 active loci with free recombination (soft) or below ln R / D (hard). W&B asymptotes R/4 to R/2 = 8.75-19 per generation at R = 35-38 M bound the interference leg for adaptive shares below about 13-27% (loss at most 4.3% at K_a <= 1e5, 17-31% at 1e6). The 0.1 M map breaks the form (observed 2.6 x R/2). Hard selection with linkage and human-scale active loci (1e4-1e5) are untested. The H2-hard cap (1,200-8,700) is exceeded by K_a >= 1e4.
- **Direction:** tight linkage, high adaptive share: Day. Free recombination, low share: critics.
- **Source:** `R4-F2-A.md`; `R4-GAPS-04-07-02.md`; `R4-H2-hard.md`.

**F3a** (reviewed)
- **Conclusion as verdicted:** I pending, F misread (Zeng 2021 s = 0.001 is mean |s| under negative selection), E contested.
- **Drivers / flip:** s and its sign. None established. Related: at s = 0.001 Day's latency is 19,807 vs diffusion 8,480 (B0.4); the W&B cap does not depend on s; at s = 0.001 the H3 long-run result is unresolved. A sourced human beneficial DFE is still a follow-up.
- **Direction:** critics on fidelity; the value's external truth is untested.
- **Source:** claim file; B0.4 (`RESULTS.md`).

#### Branch H (cost of selection)

**H** (reviewed)
- **Conclusion as verdicted:** I holds (300, 487, 41,068), F partial, E contested.
- **Drivers:** R (reproductive excess), D (cost per substitution, about 2 ln 2N), hard vs soft selection, mutation supply M, K_a (adaptive share a_nc), s.
- **Flip points** (`R4-H3-human.md`; every cell is conditional on hard adaptive treadmill selection with a soft deleterious load):
  - *R and phi.* Sustainable rate = phi * (ln R - U_hard)/D. Long-run phi (252k) at s = 0.01 is 0.30 / 0.57 / 0.59 / 0.73 at R = 1.1 / 1.5 / 2 / 3; at s = 0.003 it is 0.69 (R = 1.1) and 0.94 (R = 2). At R = 1.1 the 10k-window lambda50 = 0.00340 [0.00300, 0.00379], about 1/300 (circular in R by construction); it fails over 40k; long run about 1/530-1/1,050 at D = 15-30.
  - *H2-hard.* The cap is ln R / D; the flip lies 9-100x above 1/300 for R >= 1.3. Extinction when lambda*D + U > ln R.
  - *Minimum R for K_a adaptive substitutions in 252,000 generations* (D = 20): 1.22 (K_a = 1e3), 2.98 (1e4), 5.4e4 (1e5), none (1e6). Multiply by about 9 for a whole-genome hard load (U = 2.2). For D = 5: 1.07 / 1.45 / 15 / 6.7e11.
  - *Adaptive share.* Coding-only K_a (1.3e3-1.2e4) is payable at R about 1.2-3; a_nc about 0.1% (2e4) needs R about 3-9; a_nc >= 1% is unpayable at R <= 3-4 for D >= 5. The flip (a_nc about 0.01-0.6%) is below the resolution of any alpha estimate, so it is undetermined.
  - *Finite supply.* D about 15 + 1/M at M <= 0.03; at M = 0.01 even R = 2 sustains only about 1/430.
  - *Load.* Hard U = 2.2 is incompatible with R <= 9 (analytic); R = 20 persists at K >= 4000. Keightley: hard selection at U = 2.2 needs at least 2e^U, about 18 offspring per female.
  - Day's 17.5M-205M is unpayable under any cost model, which is uninformative about A vs B.
- **Direction:** low R, high D, hard selection, high adaptive share: Day. High R, soft selection, coding-only adaptation: critics. Not modelled: soft adaptive selection, absolute-fitness gain, truncation or synergistic epistasis.
- **Source:** `R4-H3-human.md`; `R4-H2-hard.md`; `R4-H-C2.md`.

**H1** (reviewed)
- **Conclusion as verdicted:** I holds, F n/a, E supported (Term 3 bounds selected substitutions only).
- **Drivers / flip:** none established. Term 3 is 0.0256 per generation (1 per 39); its same-basis ratio to Haldane + d is 17.1 (the earlier 7.7 was withdrawn). Scope is Term 3 (Z19984826) only; H has its own section 5.1 reply.
- **Direction:** critics (Day conceded 2026-05-07).
- **Source:** `RESULTS.md` H; `R4-H3-human.md`.

**H2** (reviewed; side literature)
- **Conclusion as verdicted:** I n/a, F accurate, E contested.
- **Drivers:** M = 2Ku, hard vs soft selection, R.
- **Flip points:** the M-dependence is reproduced (D about 6.5 at M = 1 up to 99-163 at M = 0.01). Absolute values miss by 2-12x (R = 10) and soft T50 exceeds hard T50 at equal supply, so "soft selection eliminates the cost" is not reproduced; the reconstruction is exploratory (adjusted twice after seeing results). Human M is unsourced.
- **Direction:** unresolved; nothing shows humans are in the M > 1/2 regime.
- **Source:** `R4-H-C2.md`; `R4-H3-human.md`.

**H5** (reviewed; ally)
- **Conclusion as verdicted:** I non-sequitur (the cost step is asserted, not computed), F pending, E contested.
- **Drivers / flip:** Hossjer's 15,800 is 10.5x Haldane's own 1,500 (a rate scaling, not a cost). His factor of 2 is 1.94 (20M / 10.30M, eq. 2.4) or 2.63 (eq. 3.1, 7.59M); d alone is 2.22. Conditional on H3: the shared budget is mechanically supported and 15,800 / 450k is payable at R about 2-3 under hard adaptive plus soft load.
- **Direction:** the conditional is Hossjer's; the scaling is the critics' sanctioned arithmetic.
- **Source:** `H5-hossjer-cost-step.md`; `R4-H3-human.md`; `ledgers/balance.md`.

**H8** (reviewed)
- **Conclusion as verdicted:** I holds (arithmetic), F pending, E contested.
- **Drivers / flip:** none established as a flip. The R = 2 form matches the 10k window (if R = 2 is intended; s_max*d = ln R is the audit mapping) and overshoots the long-run cap over 252k; Day does not claim R-independence.
- **Direction:** conditional on R and window length.
- **Source:** `R4-H3-human.md`.

### 1.3 Feeder checks on nodes not marked load-bearing

`hierarchy.yaml` marks none of the branch roots C, D, E, G or the count claim A3 as load-bearing, yet several of the sharpest flip points sit there and feed ROOT-M or A. I list them so the R5 decision on whether to promote them is explicit. They are not among the 30.

| Node | Result and flip | Direction | Source |
|---|---|---|---|
| G, G1 (Bernoulli Barrier) | Every power reproduces (0.02^(2e7) = 10^-33,979,400). P(all achieved) jumps from about 0 to about 1 as lambda = -m ln(1 - q) crosses 12.3-17.2 (5-95% band 4.07 wide). Free recombination: joint fixation 1.03 +/- 0.02 x p^2. Multiplicative fitness: no cap near 230 (814 concurrent sweeps at 98% of the single-locus rate). Additive fitness depends on an unstated counting convention. Best/mean reproductive excess about 340 with 157,000 loci at p = 0.5, about 1.3 at Day's own 230-locus crop. At n_f = 2e7 and s = 0.001 the genome cannot supply enough alternatives (Day-favourable bound). | On the "specific list" reading Day is right; on "any outcome" (interchangeable routes above about 12-17 per change) the critics are. | `R4-G1.md` |
| A3 / A3a / A3x (count) | Raw 9.7x; bracket 7-14x (see A). The unit argument holds by direct count; the SNV-only 17.5M brackets the polymorphism-corrected fixed events (16.4-18.1M). | Unit: critics. SNV-only magnitude: Day. | `R4-GAP07b-alignment.md` |
| C / C6 / C1c (aDNA "21") | Neutral expectation at real AADR depth: S21 = 1.5k-3.9k at N_e = 1e4 (70-190x the 21); S21 = 21 at N_e about 1.4e5 (closed) or about 1.0e5 (mild replacement); under strong replacement S21 stays at 26-140 even at N_e = 1e6. The model passes the validity gate in 0 of 44 base cells; capture heterogeneity is the strongest upward lever. Earlier C1: the test does not discriminate. Pending fix pass. | N_e about 1e4: Day (a deficit of 70-190x). Holocene N_e at or above about 1e5: critics. | `R4-C1c.md` (not integrated); `R4-B3b-C1.md`; `R4-C1b.md` |
| E (founders) | Hazard 2.0-2.75% per event against Day's 2.3%; the route to 2.3% does not reproduce; relictation excess requires family size proportional to N and the 10% threshold depends on N (15% at 2N = 20, 2.5% at 2N = 1,600). | Mixed. | `R4-E.md` |
| A6 / GAP-02 (sweep signatures) | Day's stated 3,200 sweeps give about 98 detectable in a roughly 10,000-generation window (upper bound); top of his range 1,000-3,250. | Saturation inference: critics. Classic-sweep rarity: Day. | `R4-GAPS-04-07-02.md` |
| D (sequence space) | No check. D1 raw outputs exist (`research/checks/results/raw/d1_*`), unreviewed and without a write-up, so no D1 number is used here. | none established | `ledgers/gaps.md`; REVIEW.md queue |

### 1.4 Which parameters decide the most nodes

The incidence below is an editorial coding of the 28 non-aggregate load-bearing nodes. A filled circle means a check or arithmetic audit shows the node's conclusion moves with the parameter; an open circle means the claim file lists it as an input but no sensitivity is established. The coding is mine and should be reviewed.

| Parameter group | Nodes with a filled circle | Count |
|---|---|---|
| P1 start state / ancestral N_e / demography | B, B1, B1c, B2, B4a, B5, B6 (open: B3) | 7 |
| P8 T x mu x generation time (divergence window) | A, B1, B1c, B2, B2b, B4a | 6 |
| P3 adaptive share alpha / a_nc / K_a | A, F, F2, H, H5, H8 (open: H1) | 6 |
| P6 N vs N_e, V_k, exchangeability | B2, B2b, B3, B3a, B7 (open: B, B3g, B5) | 5 |
| P5 R and hard vs soft selection (with D, M) | F2, H, H2, H5, H8 (open: F, H1) | 5 |
| P7 s distribution, sign, scale, dominance | C2, C2a, F1a, F3a, H (open: A2e, F2, H8) | 5 |
| P4 recombination / linkage / sexual vs asexual | A, A2e, F, F2 (open: F1) | 4 |
| P9 age structure / overlap | B3, C2, C2a (open: A, B, B5) | 3 |
| P2 counting rule / units | A, B4a (open: A2e, B1, E5, E6, F1a) | 2 |

Ranked by filled circles: P1, then P8 and P3, then P6, P5 and P7 tied at 5, then P4. Ties are not broken by this coding. P2 is low only because the load-bearing set excludes the count claims A3 and A3x; their 7-14x bracket is the single largest quantified factor in the audit.

---

## 2. Simulator variable list (draft)

Starting point is the list in `PLAN.md` R5: N, N_e, V_k, mu, L, s distribution (including negative), dominance, recombination, generation time, overlapping generations, sexual vs asexual, start state, demography, T, counting rule, mutators. Rows V17 and later are variables the checks revealed that the plan missed. "Baseline validated" means a pre-registered or textbook check passed for that variable. Cross-tool coverage: the numpy WF code covers B0 to B3; exact Markov chains cover B2a, C1 and E; msprime agrees on B4a; fwdpy11 agrees on F2 only. SLiM was not used.

### 2.1 Plan variables

| # | Variable | Disputes that turn on it (claims, checks) | Realistic range (source in repo) | Day's preferred value | Critics' preferred value | Textbook baseline validated? |
|---|---|---|---|---|---|---|
| V1 | N, census | B3, B3a, B3h, B2b; B3 checks | 8.2e9 (humans, species) to ancestral about 1e5; N_e/N about 0.1 (Frankham 1995, `parameters.yaml`, unverified) | N = 8e9 for supply, N_e = 1e4 for fixation (k = 800,000 mu, `B3f`); ancestral census about 100,000 (Day 2026-10-01 para 31) | N = N_e or 1/(2N) throughout (McCarthy, `B5a`; B7, B7c) | Yes: P_fix = 1/(2N) and k = U (B0.1, B0.5, `RESULTS.md`) |
| V2 | N_e (and N_e,anc) | B1c, B2, B2b, B4a, B6, C4, C5b, C1c | Humans 1.31e4-1.62e4, common chimp 3.09e4-6.18e4 (Prado-Martinez 2013); ancestral 1.32e5-1.98e5 (Yoo 2025); textbook 1e4 | 1e4 (Hard Limits abstract); 3,300 in Z18525547; ancestral about 5.7e4 implied (`B1d`) | 1.32e5-1.98e5 ancestral (B6, via Yoo); keruru temporal 8,139-9,835 (C5b) | Yes for t_fix scaling with N_e (B3); N_e,anc scaling validated at N_anc_sim 500/1000/2000 (B1c) |
| V3 | V_k, exchangeability (offspring variance) | B2, B2b, B3a, E4 | Day: 5 (human), 3 (elephant), 25 (mouse), 400 (fly) (Hard Limits Table 1; mouse and fly marked pending a source) | V_k = 5, N_e = 0.57 N (Wright, as printed) | not stated; Cannings model gives P_fix = 1/M independent of V_k | Yes (B3: P_fix and t_fix vs V_k 1-10.7) |
| V4 | Demography N(t) | B1b, B1c, B3b, B5, C4, C1c | Expansion, contraction, bottleneck all run (B1b); Holocene N_e at 1e4-1e6 (C1c grid) | N constant or "not constant for about 4N_e gives a deficit" (`B1b` claim) | Growth since the split; Holocene growth (keruru, C1c critic reading) | Yes: cumulative 1 - 4*dN/T checked analytically (B1b) |
| V5 | mu per site and U per genome | B4a, B5a, B5b, H, H7, A5c | mu 1.2e-8 (1.1e-8 to 1.5e-8, Kong 2012); about 70 new mutations per genome (Keightley 2012); 60-100 (critics); LTEE measured 8.9e-11 | Bergeron-vs-Yoo rates for 32.3 mu; per-lineage 2 mu T accounting | 100 per newborn (McCarthy); E. coli 1e-11 (Hancock) vs measured 8.9e-11 | Yes: neutral k = U (B0.5) |
| V6 | L and the unit of divergence | A3, A3a, A3x, GAP-07, GAP-07b | 3.2e9 bp; measured 37.77M SNVs plus 4.30M indel events, 42.1M events; Yoo 327 Mb per lineage in structural divergence | 410 Mb counted as 205M per lineage ("a weighting claim with a range") | events: 20-25M per lineage | Yes: independent re-implementation reproduces 42.1M (GAP-07b review) |
| V7 | s distribution, sign and scale | F3, F3a, C2, A2e, H, F2 | Day: 0.001; Zeng: mean negative; Haldane-era s_max "twice as many descendants" (R about 2); LTEE strong zones; W&B cap independent of s | s = 0.001 (F3a), per-hazard s (C2) | beneficial DFE of small effect; alpha 0-0.4 coding only (GAP-01) | Yes: Kimura u (B0.3) and t_fix (B0.4); DFE not baselined |
| V8 | Dominance h | C2, C2d | required d spans 0.45-13.5 across dominance and s (C2d) | not stated | not stated | No baseline; H2-hard and H3 are haploid-equivalent |
| V9 | Recombination and map length | A, A2e, F, F2, GAP-03, GAP-04 | Human map R = 35-38 M; mu/r about 1.0-1.5 in mammals (Day, Z18637297); about 33 crossovers vs about 96 new mutations per diploid per generation | "Only recombination could even theoretically speed things up", with reproductive constraints compensating (blog 2026-09-30) | Free recombination removes interference (F2; A5f) | Partly: free recombination linear to 272 loci (two codes); W&B Eq. 7 within 6-10% at 1.5 M; the form fails at 0.1 M |
| V10 | Sexual vs asexual | A2e, A5d, A5f | LTEE asexual; mammals sexual; Day lists recombination, ILS and HGT as the three minor mechanisms | LTEE aggregate treated as a ceiling | Gariepy: "sexual reproduction" as a first difference | Partly: clonal R_int 0.09-0.65 vs free 0.975 |
| V11 | Generation time g | A1b, B4a, GAP-06 | chimp 24-25 y; Day uses 20 (2019), 25 (2026), 32.5; Kong 29.7 y (GAP-06) | 25 | 25-29.7 | n/a (a unit); mu x g consistency not yet tested (GAP-06 queue) |
| V12 | Age structure, overlap, d | C2, C2a, A4, B3b, B3c | Siler stand-ins; d 0.481-0.568 from Day's s priors; Coale-Demeny not retrieved | d = 0.45 (Z18166234) | d = 1 per-generation; Camestros time-variation (CA-12, untested) | Partly: Euler-Lotka d reproduced; B&L eq. 3 reproduced in 9 scenarios; Lehmann 2014 not retrieved |
| V13 | Start state (pipeline fill) and heterozygosity | B1, B1c, B4a, B6, B6a | empty (counterfactual) to equilibrium; theta_anc = 4 N_e,anc mu | empty in Z22903977 (E[F]); "full and 228,000 generations long" on 2026-10-01 | full pipe (Mansfield, B6) | Yes: B1 empty vs equilibrium; B1b analytic cross-check |
| V14 | T (divergence time) | A1, A1a, B4, B4a | 5.5-6.3 My (Yoo); at least 7-8 My (Langergraber); Day 9 (2019), 6.3 (2026); CHLCA revisions 68 kya-1.3 My (Day's B4 family) | 252,000 generations (6.3 My, 25 y) | no single value; literature spans 5.5-8 My (A1a); McCarthy's dating uses Kimura's clock (B4e) | n/a (input); B4a shows T = 492,500 needed at N_e = 1e4 |
| V15 | Counting rule and unit | A3x, B4a, E5, E6, F1a, A2i | events vs bp (7-14x); pairwise vs fixed (d - 2 mu T = theta_anc); 95% rule vs strict (8,679 vs 5,496; 1,322 vs 1,587); latency vs spacing; generations vs years (Matev) | bp numerator; SNV-only 17.5M as a second reading; strict G_f 1,587 (adopted 2026-10-03) | events; pairwise divergence includes polymorphism | Partly: GAP-07b yes; LTEE counting (E5, E6) no check |
| V16 | Mutator alleles | E, E7, E8 | 6 of 12 LTEE populations mutators (Tenaillon 2016, Good 2017); a 7th transposon-driven one reported | founder hazard 2.3% per event; "8.5-17x, not 100x" | hitchhiked neutrals counted ("Taylor"); mutators as speed-up | Partly: exact chain reproduces 2.0-2.75%; E7 sublinearity not run |

### 2.2 Variables the checks revealed that the plan missed

| # | Variable | Where it matters | Realistic range (source) | Day's preferred value | Critics' preferred value | Baseline validated? |
|---|---|---|---|---|---|---|
| V17 | R, reproductive excess (ceiling fecundity), and hard vs soft selection | H, H2, H5, H8, F2; `R4-H2-hard.md`, `R4-H3-human.md` | Haldane 1.1 (Matheson 2025, k = 1.1); Day's s_max about R = 2; Day's total fertility 6-8 (R <= 3-4 before mortality); hard U = 2.2 needs about 18 offspring per female | 10% cost (R about 1.1); 300 generations | soft selection "eliminates" the cost (Nunney); R free | Partly: k = lambda wherever the population persists; cap ln R / D; Haldane's own regime (R about 1.1, diploid D 20-30) untested; Nunney reconstruction misses by 2-12x |
| V18 | D, cost per substitution, and M = 2Ku (finite supply) | H, H2 | D about 2 ln 2N, 6.5 (M = 1) to 99-163 (M = 0.01); D = 5 for intermediate-frequency standing variation | Haldane D | Hancock's intermediate-frequency point (D = 5 rows) | Partly: D validated against K; human M unsourced |
| V19 | Adaptive fraction alpha, a_nc, and required K_a | A, F2, H, H1, H5, H8, ROOT-M; GAP-01 | Coding alpha 0-0.4 (CSAC; Boyko 0.10-0.20; Uricchio 0.135; Eyre-Walker and Keightley up to 0.40); amino-acid differences about 1.3e4-3e4; constraint 8.2% (Rands 2014); a_nc unresolved | all differences are adaptive in the comparisons (17.5M, 205M); "K is not derivable from first principles" (Z23020792) | "most differences are neutral", with no number; keruru's unsourced 700,000 | Not baselinable; literature input |
| V20 | Deleterious load U_del and its hard/soft class | H7, H3, GAP-05 | U = 2.2 (Keightley); hard U = 0.35 removes R <= 1.42 if the whole class is hard | selection ceased about 1800; "3x more deleterious than neutral" (H10, unquantified) | soft load | Partly: analytic plus K >= 4000 runs |
| V21 | Number of concurrently active loci and supply Lambda_0 / R_map | F, F2, G, Gc, GAP-04 | simulated to 272 loci; human-scale 1e4-1e5 untested; concurrency ceiling 7.7-8.3e3 at s = 0.01 | about 230 sweeps (no derivation, `Gc`) | no cap to 272; 814 concurrent under multiplicative fitness | Partly (see V9) |
| V22 | Fitness convention (multiplicative vs additive, fixed vs segregating counted) | G, G1, G5 | not stated in Z18167588 | multiplicative as stated | additive vs multiplicative inconsistency (Matev) | Run both in G1; dilution depends on the convention |
| V23 | Interchangeable alternatives per needed change m (and the threshold lambda) | G1 middle case, D | threshold 12.3-17.2 (G1); at s = 0.001 and n_f = 2e7 the genome cannot supply it; branch D estimates do not convert to per-site m | specific list (pre-specified outcome) | any of M outcomes (McCarthy, Camestros) | D1 pending (raw output unreviewed) |
| V24 | Capture heterogeneity kappa, assay error epsilon, call depth | C, C1, C1b, C1c, C6 | real AADR depth: 49/62/282 chromosomes per site in the three oldest bins, 240-1,100 in younger; epsilon = 1e-3 assumed | tracked fraction 0.727; 21 post-7000 BP events | neutral expects about 0 | No: assumptions; model fails the gate in 0 of 44 base cells |
| V25 | Ancestry replacement and structure (pulses, Fst) | C, C1c, C4 | R2 literature-central shares W .12, A .50, S .38; Fst 0.086 / 0.067 / 0.049 (assumed) | closed population | replacement (Neolithic, steppe) | No (assumed) |
| V26 | Reproductive sweepstakes (family size scaling with N) | E4, F6, B3a | 10% replacement threshold 15% at 2N = 20, 2.5% at 2N = 1,600 | relictation chain | known multiple-merger result | Yes: Day's chain reproduced; P_fix = 1/(2N) to 1e-13 |
| V27 | Founder size and population-level threshold | E, E3 | N = 20-100; dip below 0.99-0.95 | 2.3% per founder event | not engaged | Partly: exact chain; bridge to a speciation hazard untested |
| V28 | Hitchhiking block size (r/s) and detection window | A6, A6a, GAP-02 | 1 Mb at r = 1e-8, s = 0.01; window about 10,000 generations (Hernandez 2011) | 3,200-32,000 blocks | not engaged | Arithmetic only |
| V29 | Polymorphic share of observed differences | A3c, B4a, GAP-07b, GAP-07c | 14-22% (CSAC); 22-25% poly-but-different in config B; GAP-07c not run | difference counts are fixed substitutions | include polymorphism | Partly (B4a) |
| V30 | LTEE calibration (N_e, U_b) | A-sim, A2e | N_e 3.3e7 unsourced; U_b underdetermined over 3 orders | G_f 1,322-1,587 as measured | scaling factors 1.5-172x | Partly: G_f about 1,300 reproducible |

---

## 3. Exit-criteria status

Criteria are from `PLAN.md` ("Exit the research phase when") plus the verification and balance lines in the same file.

| # | Criterion | Status | Evidence |
|---|---|---|---|
| 1 | Every load-bearing claim has a reviewed check and three verdicts | **Partly met** | 16 of 30 meet both conditions (A, B1, B1c, B3a, B4a, B5, B6, B7, C2, C2a, F, F1, F2, H, H1, H2). 18 of 30 have no `pending` verdict. Lists below. |
| 2 | Every critic and ally argument is mapped | **Partly met** | 51 critic and 15 ally nodes in `hierarchy.yaml`, 119 `attacks` edges all covered, 271 defeaters, 192 lineage nodes, 120 standard forms, 0 errors (`research/tools/argmap_check.py`, 2026-10-09). Not mapped: parts of the 3.5 h Hancock video, Hilbert (no model or number), keruru's k = mu chain deposit (not identified), Matev's non-numeric points (proposals only), Dembski's attached PDF, material in paid sources. 29 critic and 12 ally nodes are still `extracted`, not reviewed. |
| 3 | Gap list closed or recorded as inaccessible | **Partly met** | The R1 list is closed or recorded (table below). The gaps ledger has 7 confirmed gaps; two are substantially checked, five are open or partly checked (list below). |
| 4 | Variable list final | **Not met** | Section 2 is a first draft. Open: R unsourced, M unsourced, a_nc unresolved, dominance not stated by any party, PSMC curves not extracted, D1's m not integrated, mu x g consistency (GAP-06) not run. |
| 5 | Balance audit at exit | **Partly met** | Section 4. Several imbalances flagged. |
| 6 | Textbook baselines pass first | **Met** | B0 all pass (`RESULTS.md`). |
| 7 | Cross-tool replication of k-vs-mu and fixation time in numpy WF and SLiM / fwdpy11 | **Partly met** | fwdpy11 agrees on F2 only; msprime agrees on B4a; B0 to B3 are numpy only. |
| 8 | Lints | **Met** | `lint_research.py` exited 0 (no hierarchy node without a claim file); `argmap_check.py` reports 0 errors, 0 warnings (both re-run 2026-10-09). |

### 3.1 Load-bearing claims lacking a reviewed check with three verdicts (14 of 30)

| Group | Nodes | Detail |
|---|---|---|
| Reviewed check exists, at least one verdict pending (6) | A2e | fidelity pending |
| | B | internal pending (umbrella, status `extracted`) |
| | B2 | internal pending (the verbatim definition of the probability is unverified) |
| | B3 | internal pending |
| | H5 | fidelity pending |
| | H8 | fidelity pending |
| No reviewed check, verdict pending (6) | E5 | no script ("not run"); internal and external pending |
| | E6 | no script; external pending |
| | F1a | arithmetic only; external pending |
| | F3a | no script; internal pending |
| | ROOT | aggregate; internal and external pending |
| | ROOT-M | aggregate; internal and external pending |
| No reviewed check, verdicts complete (2) | B2b | arithmetic audit only; replication of B2e queued |
| | B3g | textual concession |

### 3.2 R1 gap list (`PLAN.md`) status

| Item | Status | Where recorded |
|---|---|---|
| *Probability Zero* (paid) | Inaccessible by decision; book-only claims tagged `secondhand` | `harvest-log-day.md`, `refresh-2026-10-09.md` |
| Blog windows 2026-06-21 to 08-22 and 08-28 to 09-10 | Closed: 156 and 38 posts scanned, 0 relevant | `harvest-log-day.md` |
| Untagged posts (HARDCODED, Irrelevance of Acclaim, Rejection, Historic Rigor) | Closed: fetched and kept | `harvest-log-day.md` |
| Evolution tag pages 19-25 | Pre-2019, listed and not fetched | `harvest-log-day.md` |
| Gariepy debate | Secondhand only (Day's repost); no independent copy found | `harvest-log-critics.md` |
| Gutsick Gibbon / Hancock video | Obtained (captions and 2,000 comments); roundtable not published | `harvest-log-critics.md` |
| McCarthy paywalled posts | Previews only; some free reposts obtained | `harvest-log-critics.md` |
| keruru Substack; Camestros parts 5 onward | Closed (29 posts; six-part series, no part 7) | `harvest-log-critics.md` |
| Bowers original review | Not found (two searches) | `harvest-log-critics.md` |
| r/DebateEvolution | Partly: Arctic Shift title search only; body text not searched | `harvest-log-critics.md` |
| Moran / Felsenstein / Peaceful Science | Inconclusive search; discourse.peacefulscience.org does not resolve (Nesslig20 Part III unchecked) | `harvest-log-critics.md` |
| Kimura 1962, Kimura and Ohta 1969 full texts | Blocked by a PMC challenge; not bypassed | `harvest-log-literature.md` |
| Yoo 2025 supplement | Retrieved (MOESM1-4); "187 Mb / 410 Mb" not found | `harvest-log-literature.md` |
| CSAC 2005, Nunney 2003, Mallick 2024 | Retrieved (Nunney from an existing Archive capture) | `harvest-log-literature.md` |
| Wistar 1966 | Reprint scan at dynamics.org; rights unverified, local analysis only | `harvest-log-literature.md` |

### 3.3 Gaps ledger (`ledgers/gaps.md`): items still open

| Gap | State |
|---|---|
| GAP-01 adaptive fraction | Check 2 done at human scale (H3, conditional). Check 1 (parameters.yaml K_a row) and check 3 (fidelity row) open; a_nc unresolved |
| GAP-02 sweep-signature window | Checked (arithmetic); no critic made the window argument |
| GAP-03 neutral rate under linkage (Birky and Walsh) | Open, no R4 check; no critic engages Z18637297 |
| GAP-04 finite-map limit | Checks 1 and 2 done; check 3 (fwdpy11 at 35 M) open |
| GAP-05 slightly deleterious fixations | Open; now also the external test of Day's B9 |
| GAP-06 mu x g consistency, BGS-aware N_e,anc | Open; the k = mu route undershoots the GAP-07b count about 2x |
| GAP-07 event counts | Direct count done (GAP-07b). GAP-07c (polymorphic share from population frequencies) and a T2T re-run open |

Other open work in the REVIEW.md queue: D sims beyond the spike, B2e replication, H follow-ups (soft-selection rate limit at human R, truncation or synergistic epistasis, sourced beneficial DFE and M, N/K in the success criterion), Yoo mu and generation time, E leftovers, PSMC Table S5, Lehmann 2014, LTEE N_e source, Coale-Demeny tables, F2 at N = 1e4 with a DFE.

---

## 4. Balance audit

All counts are from the ledgers and files named. The side coding follows `hierarchy.yaml`.

### 4.1 Counts

| Measure | Day | Critics | Allies | Literature / audit-raised | Source |
|---|---|---|---|---|---|
| Claim nodes (204) | 112 | 51 | 15 | 26 | `lint_research.py`, `hierarchy.yaml` |
| Load-bearing (30) | 21 | 5 | 1 | 3 | `hierarchy.yaml` |
| Reviewed or checked status | 57 of 112 (51%) | 21 of 51 (41%) | 3 of 15 (20%) | not counted | `hierarchy.yaml` status field |
| Internal verdict non-sequitur or arithmetic-error | 22 of 112 (20%) | 0 of 51 | 1 of 15 | 0 of 26 | `hierarchy.yaml` |
| External verdict contradicted | 7 | 1 | 0 | 1 | `hierarchy.yaml` |
| Opponent profiles (23) | n/a | 12 | 10 (Hossjer partial) | 1 adjacent (keruru) | `docs/research/opponents/` |
| Verbatim quotes | 105 (Q1-Q105) | 154 (critics and allies together) | | 79 (literature) | `sources/quotes-*.md` |
| Source rows in bibliography | 154 blog posts kept, 43 Zenodo rows (39 records), 7 books (not accessed), 3 videos | about 58 (31 critic, 13 ally, 7 adjacent, others) | | 38 | `sources/bib-*.md` |
| Defeaters by attacker side (271) | 63 | 74 | 2 | 24 literature, 108 audit | `argmap_check.py` |
| Audit attacks by target (108, of which 28 are reviews attacking the audit's own checks) | 54 | 21 | 3 | 1 literature, 1 other | `defeaters.yaml` (tallied here) |
| Audit attacks upheld on that target | 24 of 54 (44%); 30 partly | 3 of 21 (14%); 18 partly | 2 of 3 | 0 of 1 | `defeaters.yaml` audit_status |
| Lineage nodes (192) | 89 | 48 | 10 | 18 literature, 27 audit | `argmap_check.py` |
| Lineage concessions / retractions | 5 concessions, 1 retraction | 3 concessions, 1 retraction (keruru) | | audit retracted 3 own | `argmap/NOTES.md` |

Checks, coded by whose claims they primarily test (24 checks, including C1c, which awaits its fix pass and integration; coding is editorial):

| Primary target | Checks | Count |
|---|---|---|
| Day-side claim | B0.4, B1, B1b, B1c, B3, B2a, B3b/c, C1, C1b, C1c, C2, E, G1, GAP-02, H | 15 |
| Both sides (critic arithmetic or counter-arguments tested too) | B4a, H2-hard, H3, F2 / A-sim, GAP-04, GAP-07, GAP-07b | 7 |
| Critic-side claim | F1 | 1 |
| Neutral (baseline) | B0 | 1 |

Headline direction of each completed check (editorial coding of the "Who this helps" text): both sides credited in 15 (B0.4, B1, B1b, B3, B2a, B4a, B3b/c, C1, H, C2, F2 / A-sim, GAP-04, GAP-02, H3, GAP-07b); critic-leaning in 6 (F1, B1c, C1b, H2-hard, G1, GAP-07); Day-leaning in 1 (E, which reproduces his founder hazard size); B0 is a neutral baseline; C1c is mixed and not yet integrated. The two steelman reviews per check are balanced in MAJOR counts: GAP-07b 4 Day-side vs 6 critic-side, H3 7 vs 6, GAP-04/07/02 7 vs 7 (`REVIEW.md`).

### 4.2 Weak cells traced to claim files

`ledgers/balance.md` holds its "Weak" items in two places: the "Weaknesses recorded with equal scrutiny" bullets and the "New weak points" column of the R4 table. Each is traced below. The plan's original Weak row (loose uncited inputs, expected values without variance, ad hominem, "no one checked Yoo 2025", key video not located, nothing peer-reviewed) is folded into these bullets.

**Day**

| Weak item | Claim file(s) | Traced? |
|---|---|---|
| bp-vs-events basis of 205M | `A3x-bp-vs-events.md`, `A3a-205m-headline.md` | yes |
| Zeng 2021 s misread | `F3a-s-0-001-zeng-2021-misread.md` | yes |
| N_e used for fixation probability | `B3a-fixation-probability-1-over-2ne.md`, `B7-neutral-fixation-probability-is-1-over-2n.md`, `B7a`, `B7b` | yes |
| Recombination misattributed to Kimura and Ohta 1969 | `H9-kimura-ohta-recombination.md` | yes |
| Langergraber 2012 misread | `A1a-divergence-time-literature.md` (also A1, A1b) | yes |
| "Chalub 2012" not found | `ledgers/fidelity.md` row only; `B1e-chalub-2022-reading.md` covers the 2022 paper | **no claim file** |
| Parameter drift across versions | `ledgers/versions.md`; claims `A2b`, `A2j`, `A3`, `B3` | partly (ledger, not one claim) |
| Hard Limits and aDNA papers have no references | `B2-hard-limits-domain-of-k-mu.md` (fidelity unverifiable), `C-adna-zero-fixations.md`; `harvest-log-day.md` ("to be confirmed by a human reading the PDF") | partly |
| RRME 0.743 rests on a falsified 1/(2N_t) step | `B3c-rrme-k-0743-mu.md` | yes |
| Empty-start premise contradicted | `B1c-...md`, `B1d-full-but-short-pipe-revision.md` | yes |
| "d = 1 for discrete generations" fails on Day's formula; Table 1 not reproduced | `C2-bio-cycle-d.md`, `A4a-d-empirical-estimate.md` | yes |
| aDNA 21-count not reproducible | `C6-molecular-clock-stopped.md` | yes |
| Term 3 vs Haldane comparison mixed bases (17.1) | `H8-kimura-calculator-term3.md`, `H1-term3-retraction.md` | yes |
| B6a "rounding error" holds only at N_e,anc = 1e4 | `B6a-day-ancestral-polymorphism-rounding-error.md` | yes |
| 32.3 has no derivation; "RRME confirms B&L" has the opposite sign | `B3d-k-32-3-mu-and-factor-25.md`, `B3c` | yes |
| Two unreconciled cost figures | `H-haldane-limit.md`, `H8` | partly |

**Allies**

| Weak item | Claim file(s) | Traced? |
|---|---|---|
| Hossjer's factor-2 gaps (1.94, 2.63, d = 2.22) | `A5a-hossjer-127-15800-10m.md`, `B5h-hossjer-neutral-d-mu-7-6-million.md`, `ROOT-h-hossjer-agrees-with-main-argument.md` | yes |
| Hossjer's cost step asserted, not computed (15,800 = 10.5x Haldane's 1,500) | `H5-hossjer-cost-step.md` | yes |
| Keen gives no equations; Dembski gives no calculation | `ROOT-k-keen-time-is-the-reason.md`, `ROOT-de-dembski-own-arguments.md` | yes |

**Critics**

| Weak item | Claim file(s) | Traced? |
|---|---|---|
| Hancock diploid 76.8 corrected on screen; retained 76 is SV-inclusive; 38M double count; 205M to 407/gen halves a per-lineage figure | `B5c-hancock-76-8-per-generation.md`, `A3d-factor-of-two-both-lineages.md` | yes |
| Hancock bacterial mu 1e-11 vs measured 8.9e-11 | `A5c-neutral-supply-ecoli-vs-human.md` | yes |
| Hancock's video answers the Duffy version, not MITTENS 3.0 | `G2-serial-critique-hancock.md` | yes |
| Nesslig20 basis of 75 not stated; 37.8M double count | `B5e-nesslig20-37-8-million.md` | yes |
| McCarthy N = N_e, all neutral, uncited 3% | `B5a-mccarthy-22-5-million.md` | yes |
| McCarthy comment arithmetic slip (35M vs 20M) | recorded in `refresh-2026-10-09.md` C-5, not a claim | **no claim file** |
| Mansfield 2% illustration about 44x short | `B5b-mansfield-one-fixation-per-generation.md` | yes |
| Relayed 7.2M | `B5d-relayed-7-2-million.md` | yes |
| Myers gives no numbers; ad hominem | `G2e-myers-massively-parallel.md`, `opponents/pz-myers.md` | partly (profile) |
| Camestros first edition only, typo (CA-06) | registry id `x:CA-06` in `argmap/NOTES.md`; related `A2a-gf-datum-source-2019.md` | **no dedicated claim** |
| KITTENS AI-assisted, cites from memory | `A5b-kittens-94000x11p7.md` | yes |
| Expected values without variance | `B5a` (Poisson sd about 4.7 thousand, "immaterial"), B5 | partly |
| Soft-selection rescue not reproduced; stationarity assumed | `H2-nunney-2003.md`, `H-haldane-limit.md`; `B5-critics-k-equals-mu-cancellation.md` | yes |
| Camestros time-variation of d untested | `A4b-d-critique-camestros.md` | yes |
| No one checked Yoo 2025 | `A3x1-yoo-2025-fidelity.md` (now checked) | yes, resolved |
| Nothing peer-reviewed | project-level (`HANDOFF.md`), no claim file | n/a |

### 4.3 Imbalances flagged

1. **Check targeting.** 15 of 24 checks primarily test a Day-side claim and one tests a critic-side claim. Part of this is structural (Day's claims carry the numbers and the audit was asked to test "the claim as its author stated it"). The cost is that the critics' quantitative claims (McCarthy 22.5M, Mansfield one per generation, Hancock 76.8, Nesslig20 37.8M, KITTENS 94,000x, Camestros lottery) are tested only as by-products (B4a, GAP-07b grading, F2 / A-sim). B6c, G2, G2c, G3a and D1b/D1c have no check.
2. **Audit attacks and upheld rate.** The audit made 54 attacks on Day-side claims and 21 on critic-side claims (3 on allies). 44% of the former were recorded as upheld and 14% of the latter. Day-side claims are 112 of 204 and carry most numbers, so some skew is expected, but the upheld gap is larger than the claim-share gap. Worth a second reader.
3. **Internal-verdict asymmetry.** 22 of 112 Day nodes carry an internal non-sequitur or arithmetic-error verdict, and 0 of 51 critic nodes do, although critic-side errors are documented (Hancock and Nesslig20 double counts, Mansfield's 44x shortfall, McCarthy's 35M slip). The ledger routes critic errors to *external* (B5c is "internal holds, external contradicted"). This may be correct (the arithmetic is right, the comparison is wrong), but the vocabulary produces an optical asymmetry. R5 should decide whether B5c, B5e and B5b should be re-read under the internal column.
4. **Credit rule.** Results from the audit's own checks or the literature (Nunney, Euler-Lotka d, Yoo N_e,anc, B1c, B4a, C1) are classed `literature` and not credited to critics, because no critic made them (balance.md, R4 section). This is defensible, but a reader who tallies "critic wins" will undercount; 16 of the 24 literature-attacker defeaters land on Day.
5. **Unchecked branch D.** Branch D (about 40 claim files) has no completed check; both sides' balance cells say "catalogue only". Rosenhouse ch. 6 is not accessed. This is a symmetric gap, but it is the largest branch without a check.
6. **Evidence access.** Day's texts are almost fully local (43 Zenodo rows, 154 blog posts), while critic evidence is more often secondhand or partial: McCarthy paid posts (previews), Gariepy debate (Day's repost), Bowers original (not found), Hancock video (auto-captions, only parts mapped), Peaceful Science (DNS). Day's own book is also inaccessible, so the access gap is not one-sided, but it affects how complete the critics' side of each claim file can be.
7. **Review coverage by side.** 51% of Day nodes reached `reviewed` or `checked` against 41% of critic nodes and 20% of ally nodes. 29 critic and 12 ally nodes remain `extracted`.
8. **Weak cells with no claim file.** "Chalub 2012 not found" (Day side), McCarthy's 35M slip and Camestros's typo (critic side) are traced only to ledgers or registry ids. Symmetric (one Day, two critic), and low weight.
9. **Project-level.** `HANDOFF.md` records that nearly all work is AI-driven, the steelmen are AI reviewing AI, Day's papers list an AI co-author, no one on either side has been contacted, and the first-pass summaries leaned mainstream. The balance ledger exists to offset that; this audit cannot test whether it succeeds.

### 4.4 What looks balanced

- The two steelman reviews per check return comparable MAJOR counts (section 4.1).
- Weakness bullets in `balance.md` are comparable in size: 9 Day (one with five sub-items), 3 ally, 10 critic.
- Both sides have recorded concessions and retractions (Day 5 and 1; critics 3 and 1).
- The audit retracted three of its own findings and corrected several of its own numbers (balance.md "Audit" cells; `NOTES.md` lineage table).

---

## 5. Items for the R5 decision, not decided here

- Whether to mark branches G, C and the count claim A3 as load-bearing (section 1.3 holds several flips that feed ROOT-M and A).
- Whether to recode critic-side errors into the internal column (section 4.3, item 3).
- The weight to give conditional verdicts (H, F2, C2): every cell is stated for a tested regime only.
- C1c and D1 integration will change section 1.3, rows V23 to V25 and the exit status of criterion 1; GAP-07c will change the A bracket.

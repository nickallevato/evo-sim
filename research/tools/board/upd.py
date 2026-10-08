import glob, re, os, sys
CL = '/home/na/projects/evo-sim/docs/research/claims'
R = 'research/checks/results/'
RV = 'Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)'

# id -> (verdict dict {key: (value, comment)}, check text)
U = {}
def u(cid, check, **v):
    U[cid] = (v, check)

# ---------------- A branch ----------------
u('A', f"R4 A-sim (`a_ltee_scaling.py`, F2 `f2_multilocus.py`; {R}R4-F2-A.md): formula arithmetic unchanged. Using LTEE G_f as a global constant is not supported for recombining genomes in F2's tested regime (free recombination R_int 0.975 at 272 active loci; the LTEE-scale factor 1.5-172x is an EXTRAPOLATION). For asexual genomes a saturation is real but logarithmic (a = 0.23-0.34 per 100x supply). {RV}",
  external=("contested", "asexual saturation real (logarithmic); recombining-genome use of G_f not supported in F2's tested regime; LTEE-scale factor extrapolated"))
u('A2', f"R4 A-sim ({R}R4-F2-A.md): G_f of order 1,300-1,600 is reproducible in a clonal fixed-s model at Ne = 3.3e7 (unsourced assumption), but the calibration is underdetermined (U_b spans 3 orders of magnitude: 6.7e-7 / 8.4e-9 / 6.3e-10 for s = 0.003 / 0.01 / 0.03) and a single-s fit conflates neutral and adaptive fixations (neutral expectation ~54% of 1/1322). G_f is a statement about an Ne*U_b*s combination, not a universal constant. {RV}",
  external=("contested", "order of magnitude reproducible; calibration underdetermined (R4 A-sim)"))
u('A2e', f"R4 A-sim + F2 ({R}R4-F2-A.md): the LTEE is interference-limited in the clonal model; free recombination would raise the rate 1.5-172x at the calibrated supply, but that factor is an EXTRAPOLATION of F2's R_int ~ 1 beyond its tested range (<= 272 active loci), not a simulation. Credit to Day: sublinearity and real interference under linkage are borne out (critics also predicted asexual saturation, so that is not Day-specific credit). {RV}",
  external=("contested", "not supported for recombining organisms only by extrapolation from F2 (1.5-172x); asexual interference confirmed"))
u('A4', f"R4 C2 ({R}R4-H-C2.md, `c2_overlap_vs_standard.py`): Day's d = mean cumulative hazard at the age of mothers (0.789 vs 0.784). For s defined as a fractional change of the mortality hazard at all ages, d*s is exact (V1, T*dr/s = 0.778 vs d = 0.789, within 1.5%): a point for Day. For per-generation s (fecundity, pre-maturity survival) the factor is 1 (V3/V4: Day's d*s 20-22% below exact). g_eff = d*g is standard theory with generation length T/d. Which scale the cited aDNA s values use was not retrieved (they are reported as per-generation logistic slopes, which would give d = 1). {RV}",
  internal=("holds for hazard-scale s", "d*s exact for hazard-scale s (V1); factor 1 for per-generation s; a unit conversion, not an extra correction"),
  external=("contested", "which s scale the cited aDNA papers use is unretrieved"))
u('A4a', f"R4 C2d ({R}R4-H-C2.md, `c2_ratio_nonident.py`): three trajectories, four unknowns: an exact fit exists for every d. Day's own published s ranges (LCT .04-.10, SLC45A2 .04-.05, TYR .02-.04) give d in [0.481, 0.568]; scaling the ranges by 0.75 / 1.25 moves it to [0.638, 0.756] / [0.387, 0.456]. The 0.45 comes from priors on s, not from the trajectories. Equivalent alternatives: onset 2,100-3,100 y later, generation length 51-66 y, or dominance (LCT dominant needs d = 0.745). Critic-side note: at d = 1 the required s (LCT 0.024) is below the published ranges, an anomaly the critics have not explained. {RV}",
  internal=("holds", "arithmetic reproduces from Day's s priors; d not identifiable apart from s, onset, T, dominance"),
  external=("contested", "not identifiable (C2d)"))
u('A5b', f"R4 A-sim + F2 ({R}R4-F2-A.md): linear supply scaling (a = 1.00) holds under free recombination within F2's range (N = 1000, s = 0.01, 2N*U_b <= 32, <= 272 active loci) and fails for an asexual genome (a = 0.23-0.34 per 100x). KITTENS's 94,000x is 3 orders beyond the tested range, and 94,000 is total, not beneficial, supply. Credit to Day: KITTENS's linearity is not established at the claimed scale. {RV}",
  external=("contested", "linear only under free recombination in tested range; asexual a = 0.23-0.34"))
u('A5d', f"R4 A-sim ({R}R4-F2-A.md): sublinear response confirmed for an asexual genome (simulated 100x supply gives 2.9-4.8x, a = 0.23-0.34, more sublinear than Day's 0.47-0.61; the model lacks a DFE, so the exponent comparison is qualitative). Day's mechanism (sweep dynamics) is right for linked loci; for unlinked loci F2 gives a = 1.00 in its tested range. Credit to Day: sublinearity is real. {RV}",
  external=("contested", "sublinear confirmed for asexual; not for free recombination in F2's tested regime"))
u('A5f', f"R4 F2 ({R}R4-F2-A.md): direction supported: recombination raises the rate (R_int clonal 0.088 vs free 0.975 at 2N*U_b = 32; fwdpy11 agrees at three points). The magnitude at LTEE scale (1.5-172x) is extrapolated, not simulated. Day's \"double-edged sword\" (recombination also breaks favourable combinations) is not tested (single s, no epistasis). {RV}",
  internal=("holds", ""),
  external=("supported", "direction (R_int 0.09 clonal vs 0.97 free); magnitude at LTEE scale extrapolated"))

# ---------------- B branch ----------------
u('B1', f"R4 B1c/B4a ({R}R4-B1c-B4a.md): the empty-start deficit is exact for post-split new mutations (new-mutation column 0.84 = Day's (T-4Ne)/T at Ne = 1e4), a point for Day's internal validity. For the human-chimp case the deficit exists only in that accounting: step histories from Yoo's ancestral Ne give a per-lineage excess (K/UT 1.9-4.0), and pairwise divergence is not reduced by the empty-pipe term (d - 2muT = theta_anc in every row). {RV}",
  external=("contested", "deficit exists only for new-mutation accounting from an empty start; contradicted for the human-chimp observable (B4a)"))
u('B1c', f"R4 B1c (`b1c_ne_history.py`, seed 20261008, 150 reps, burn-in 20 N_sim; {R}R4-B1c-B4a.md): every step history from Yoo's ancestral Ne (1.98e5 / 1.32e5) to a sourced modern Ne (1e4-6.18e4, Prado-Martinez 2013 Table 1) gives an excess K/UT of 1.9-4.0 (H1 3.986 vs analytic 3.984); controls 1.000. This is the B1b telescoping identity under step histories, not an independent empirical finding: Yoo's Ne is a lifetime average, and no PSMC trajectory was extracted. K counts ancestral alleles that fix in both lineages, so it is not a difference count. Credit to Day: the new-mutation column (0.84) confirms (T-4Ne)/T. Day withdrew the empty-start premise (B1d). {RV}",
  internal=("holds", "arithmetic for an empty start; post-split new-mutation column 0.84 = (T-4Ne)/T"),
  external=("contradicted", "empty-start premise (withdrawn by Day, B1d); step histories give excess 1.9-4.0x; K is not the difference count"))
u('B1d', f"R4 context ({R}R4-B1c-B4a.md; REVIEW-R4-steelman-day): a full pipe of 228,000 generations implies Ne_anc ~ 5.7e4 (4Ne). Not simulated; derived by the Day-side reviewer: d ~ 0.605% + 0.274% = 0.88%, about 71% of the observed 1.23%, against Yoo's sourced 1.32-1.98e5. B1d contradicts the empty-start premise of B1c. {RV}",
  external=("contested", "implied Ne_anc ~5.7e4 is below Yoo's 1.3-2.0e5; derived d ~0.88% vs 1.23% observed (not simulated)"))
u('B3', f"R4 B3b/B3c ({R}R4-B3b-C1.md): k != mu under overlapping generations plus fluctuating N is real (B&L eq. 3 reproduced, all |z| < 1.6), but at human-like parameters it is -2% to +38% (sign upward for realistic growth). 0.743 is a window artefact whose mechanism (fixation probability 1/(2N_t)) is falsified by simulation; 32.3 has no derivation and cannot come from B&L. {RV}",
  external=("contradicted", "for the listed values (N/Ne, 0.743, 32.3, 800,000); the qualitative B&L effect is real but small (B3b)"))
u('B3b', f"R4 B3b (`b3b_overlap_fluctuation.py`, 16 reps; {R}R4-B3b-C1.md): B&L 2012 eq. (3) reproduced by independent individual-based simulation in 9 scenarios (all |z| < 1.6); fluctuation without overlap gives k = mu exactly. At human-like parameters (exact eq. 3, s = 0.96/yr): symmetric cycles -0.3% to -2%; one-way growth raises the arrival rate of eventual fixers by 1.38x (transient); contrived two-state range 0.59-1.70, with k < mu only for an unrealistic survival ordering. Credit to Day: the effect exists and Kimura's k = mu is not exact with overlap (critics' blanket k = mu is a discrete-generation result). Against Day: the realistic sign is upward and the size cannot give 0.743 or 32.3. Open: per-generation-time normalisation (0.81-1.11 under strong fluctuation; Lehmann 2014 not retrieved). {RV}",
  internal=("holds", "B&L effect reproduced"),
  external=("supported", "qualitatively (k != mu with overlap + fluctuation); human-scale size -2% to +38%, sign upward; cannot give 0.743 or 32.3"))
u('B3c', f"R4 B3c ({R}R4-B3b-C1.md): arithmetic 0.7428 reproduces, but the value depends on the window (2 cohorts 0.868 ... 20+ cohorts 0.598). Mechanism test: a mutant born in cohort i fixes with probability 1/N_i (P_fix*M_i = 0.973-1.018; with overlap 1.034 +/- 0.026) against the 1/(2N_t) the derivation needs (0.305). Day's \"RRME confirms B&L\" has the opposite sign (B&L realistic growth: +38%; RRME: -26%). The 1/(2N_t) step is the audit's reconstruction of eq. 1 and 3, to be confirmed. {RV}",
  internal=("non-sequitur", "arithmetic holds; fixation probability taken as 1/(2N_t), simulation gives 1/N at birth"),
  fidelity=("misread", "B&L sign opposite"),
  external=("contradicted", "0.743 is a window artefact (0.60-0.87, limit 0.598)"))
u('B4a', f"R4 B4a (`b4a_two_lineage_ils.py`, seed 20261009, burn-in 20 N_sim; {R}R4-B1c-B4a.md): forward simulation gives d - 2muT = theta_anc within ~0.3% in every row; msprime agrees. CSAC's 14-22% polymorphic share matches the poly-but-diff column (config B, human 1e4 / chimp 4.6e4: 22-25%), so there is no tension. At the relevant node (HCB, Ne_anc = 1.98e5) d = 1.55-1.56%, ~25% above observed 1.23%; at Day's Ne = 1e4, d = 0.65%, about half (Day-side point). The data fix only 2muT + 4Ne_anc*mu (a 3-parameter fit), and Yoo's own mu is not recorded, so the Ne_anc rescaling is open. ILS discordance and outgroup not run. {RV}",
  internal=("holds", "forward sim matches formula within ~0.3%; msprime agrees"),
  fidelity=("accurate", "CSAC polymorphic share matches poly-but-diff"),
  external=("contested", "overshoots 1.23% by ~25% at HCB node; half at Ne 1e4; (mu, T, Ne_anc) underdetermined; Yoo mu unrecorded"))
u('B6', f"R4 B1c/B4a ({R}R4-B1c-B4a.md): an equilibrium (full) start gives K/UT = 1.000 for constant Ne, and d = 2muT + theta_anc within ~0.3% in forward simulation. Whether the fit matches 1.23% depends on Ne_anc, T and mu (see B4a). {RV}",
  external=("supported", "full pipe gives k = mu and d = 2muT + theta_anc (forward sim)"))
u('B6a', f"R4 B4a ({R}R4-B1c-B4a.md): \"rounding error\" holds only at Ne_anc = 1e4. At Yoo's Ne_anc, theta_anc = 0.63-0.95% of sites against 2muT = 0.605%. Day-side point: at Ne = 1e4 the model gives d = 0.65%, about half the observed 1.23%, so the reconciliation depends on a large Ne_anc (or longer T / higher mu). {RV}",
  external=("contradicted", "at sourced Ne_anc the ancestral term is comparable to 2muT; holds only at Ne_anc = 1e4, where d is half the observed"))
u('B6b', f"R4 B4a ({R}R4-B1c-B4a.md): qualitatively vindicated: ancestral alleles also sort into fixed differences (Day's 2mu(T-4Ne) = 0.51% is below the simulated fixed differences 0.56-1.46%), and raw d is not reduced by the empty-pipe term. Critic-side caveat: 2muT alone already supplies ~19M of the differences, so the point is accounting, not a gap filled only by ancestry. {RV}",
  external=("supported", "qualitatively (B4a)"))
u('B5', f"R4 B1c/B3b ({R}R4-B1c-B4a.md, R4-B3b-C1.md): k = mu holds exactly at steady state with discrete generations (controls 1.000), but not exactly with overlapping generations plus fluctuation (B3b, small) and not over a finite window after a contraction (B1c, per-lineage excess 1.9-4.0x). The critics' stated totals assume stationarity. {RV}",
  external=("contested", "exact at steady state; transient and overlap effects (B1c, B3b)"))
u('B5c', f"R4 B4a ({R}R4-B1c-B4a.md; REVIEW-R4-steelman-critic): on an SNV basis the 38M agreement double-counts. Haploid SNV supply is 38.4 per generation per lineage, so 2 x 252,000 x 38.4 = 19.4M, which is B4a's 2muT (0.605%). The observed ~35M SNVs are then ~19M from post-split mutation plus ~15M remainder attributable to ancestral polymorphism (B4a: theta_anc = 0.63% x 3.2e9 = 20M at Yoo HCG Ne). The retained 76 is an SV-inclusive event count (152/2), whose comparator is the ~40M event total, so the event-basis reading is not contradicted. Hancock's \"38M matches 35-40M SNVs\" lands on the observed value for the wrong reason. {RV}",
  external=("contradicted", "as an SNV match (double count; correct split ~19M post-split + ~15M ancestral); event-basis reading untested"))
u('B5e', f"R4 B4a ({R}R4-B1c-B4a.md; REVIEW-R4-steelman-critic): if mu_G = 75 is a zygote-level count, the haploid value gives 18.9M (= 2muT, B4a), and the observed ~35M is ~19M post-split plus ~15M ancestral polymorphism, so the 37.8M match would be a double count (same issue as B5c). The post does not state the basis. {RV}",
  internal=("holds", "arithmetic 2 x 75 x 252,000 = 37.8M"),
  external=("contested", "basis unstated; on a haploid SNV basis 18.9M + ancestral ~15M"))

# ---------------- C branch ----------------
u('C', f"R4 C1 (`c1_ascertainment_sim.py`, exact WF chain; {R}R4-B3b-C1.md): this is Z23046531's two-period statistic (not the Z18525185 21-count, see C6/C1b). Under neutrality at Ne = 1e4 the expected events from <50% are ~0 and from 50-90% are 0.04 (v62) / 0.11 (v66); new-in-window mutations fixing inside 280 generations: 5e-151 per site. So the headline does not discriminate. Observed 1 and 3 are above the Ne = 1e4 expectation (P(>=3 | 0.11) = 2e-4; critic reading: faster than neutral, not a stopped clock) and equal expectation at Ne ~ 7,000; the tail is extremely Ne-sensitive and Ne = 1e4 is an unverified input (Day-side reading). Admixture not modelled. {RV}",
  internal=("non-sequitur", "neutral also predicts ~0 from <50% and 0.04-0.11 from 50-90%"),
  external=("contested", "observed 1 and 3 mildly above neutral at Ne 1e4, equal at Ne ~7k; admixture not modelled"))
u('C1', f"R4 C1 ({R}R4-B3b-C1.md): point 1 holds (new-in-window fixations are ~0 genome-wide, 5e-151 per site). Sample-level newly-100% counts: D2 (African single-male discovery) 13,807 and D3 18,157 vs v62 observed 17,806 (within 1.3x); v66 3,469 is 3.8x below the model, unexplained. Same-population MAF design (D1) gives 0. Panel denominator omits African-private post-split mutations (slight upper bound). {RV}",
  internal=("holds", "point 1 trivially; new-in-window fixations ~0"),
  external=("supported", "v62 total within 1.3x of neutral D2/D3; v66 3.8x below, unexplained"))
u('C1a', f"R4 C1 ({R}R4-B3b-C1.md): sign is right for the 10-90% start bands Day's headline uses (African discovery enriches them 1.2-3.4x): credit to Day. It is wrong for the >=90% bands (suppressed 5-30x), where most true completions occur, and for a same-population design (D1: 0). The effect on the headline is immaterial because the expectation there is ~0 either way. {RV}",
  internal=("holds", "for the 10-90% bands (1.2-3.4x enrichment)"),
  external=("contested", "wrong sign for >=90% bands and same-population discovery; immaterial to the ~0 headline"))
u('C2', f"R4 C2 ({R}R4-H-C2.md): d*s is exact for hazard-scale s (V1, within 1.5%; Day-side point), and the factor is 1 for per-generation s (V3/V4/V5 ratios 1.000). Day's own formula gives d = -ln L for a semelparous annual (d = 1 only at L = 1/e), so \"d = 1 for discrete generations\" and \"0 to 1\" fail on his own terms. d is not identifiable apart from s, onset time, T and dominance (C2d). Table 1 d values not reproduced (Siler stand-in 0.79/0.93 vs 0.53 at e0 = 32): an open fidelity gap because the Coale-Demeny tables were not retrieved. {RV}",
  internal=("non-sequitur", "d fit not identifiable apart from s (C2d); 'd = 1 for discrete generations' fails on own formula; d*s exact for hazard-scale s (V1)"),
  fidelity=("unverifiable", "Coale-Demeny tables not retrieved; Table 1 not reproduced with a Siler stand-in"),
  external=("contested", "which s scale the cited papers use is unretrieved; published s are per-generation slopes (d = 1)"))
u('C2a', f"R4 C2 ({R}R4-H-C2.md): the derivation is correct: integral of l*v = T for a stationary population, so d = mean cumulative hazard at the age of mothers (0.789 vs 0.784 numerically); first-order Euler-Lotka gives T*dr = s_gen. d is therefore a conversion between hazard-scale and per-generation s. Table 1 values (0.53 ... 0.015) not reproduced with a Siler stand-in (0.79/0.93 at e0 = 32; 0.13-0.21 at e0 = 78), unresolved because Coale-Demeny tables were not retrieved. {RV}",
  internal=("holds", "derivation correct for hazard-scale s"),
  fidelity=("unverifiable", "Coale-Demeny West tables not retrieved; Hill/Charlesworth not retrieved"),
  external=("contested", "a unit conversion, not a separate correction to the speed of selection"))
u('C2c', f"R4 C2c (`c2_ratio_nonident.py`; {R}R4-H-C2.md): the TYR/SLC45A2 ratio is 0.4646-0.4778 over d in [0.2, 2], and random synthetic locus pairs show the same invariance (<= 6%): the odds multiply by (1+s) each generation, so ln(1+s)*d*G is fixed. An algebraic identity, not a test of d. The paper's 0.49 is ~2% above the exact recursion. {RV}",
  external=("contradicted", "ratio is invariant for random locus pairs, so it cannot validate d"))
u('C2d', f"R4 C2d ({R}R4-H-C2.md): chicken (p 0.44 to 0.97, G = 900) requires d additive 1.43 / 0.845 / 0.471 at s = 0.0029 / 0.0049 / 0.0088; recessive 1.90 / 1.13 / 0.63; dominant 13.5 / 8.0 / 4.5. The paper's 1.02 holds at the point estimate but depends on dominance and s (s conventions differ across models). Loog's posterior is not in the repo. {RV}",
  internal=("holds", "1.02 at the point estimate"),
  fidelity=("unverifiable", "Loog posterior not in repo"),
  external=("contested", "required d spans 0.45-13.5 across dominance and s; not decisive"))
u('C6', f"R4 C1 + C1b ({R}R4-B3b-C1.md, {R}R4-C1b.md, `c1b_day_binned_statistic.py`, 20 reps x 13 configs x 16 readings): the 630 arithmetic (150M x 1.2e-8 x 350) is correct, but the denominator is wrong for a polymorphism-ascertained panel (neither 630 nor the uniform rescaling 5.2 is the right comparator). C1b simulated Day's binned first-passage statistic literally: every reading gives 1.2e3-1.7e4 post-7000 BP events for both neutral (Ne 7e3-2e4) and Day's d = 0.45 model, against 21 observed; but the model also misses Day's own bin profile (7000-8000 BP ~1,350 vs 4,497; pre-7000 share 38-60% vs 99.86%). Verdict: not reproducible from the published procedure; cannot adjudicate. Neither \"neutral predicts ~0\" (Day side) nor \"does not rescue Day\" / \"deficit vs neutral\" (earlier audit wording) is supported. Likely cause: per-site call depth in old bins (reviewer's 1-replicate direction test) and ancestry replacement; follow-up queued. {RV}",
  external=("untestable", "21 not reproducible from the published procedure (C1b); cannot adjudicate pending a call-depth model"))

# ---------------- F / G branch ----------------
u('F', f"R4 F2 ({R}R4-F2-A.md) extends F1: latency does not bound throughput; interference bounds it only with linkage (clonal R_int 0.09-0.65; free recombination 0.975 at 272 active loci, soft selection, N = 1000). F1's strawman caveat (the serial reading must be tied to a quote) still applies. {RV}",
  internal=("non-sequitur", "as a throughput bound (F1, F2); interference binds only with linkage"))
u('F2', f"R4 F2 (`f2_multilocus.py` seed 4242 with crc32-derived seeds, `f2_fwdpy11.py`; {R}R4-F2-A.md) and H2 (`h2_hard_selection_multilocus.py`; {R}R4-H2-hard.md). Soft selection, N = 1000, s = 0.01: clonal R_int falls 0.645 -> 0.088 as 2N*U_b goes 0.1 -> 32; a 0.1 M map gives 0.204; one 1.5 M linkage group 0.572 at 208 active loci; free recombination 0.975 +/- 0.005 at 272 active loci, linear in supply; fwdpy11 agrees. Day's cap (R < 0.5 by ~230 loci) is not reproduced for r = 1/2 in the tested regime. Hard selection (H2, free recombination, imposed demand): rate = demand until total log-load exceeds ln R; ~255 open loci persist at R >= 10, ~90 at R = 2. Untested: human-scale active loci (~1e4-1e5 by Little's law), hard selection combined with linkage, N = 1e4, DFE. Credit to Day: interference is real under tight linkage. {RV}",
  internal=("holds", "interference exists (clonal R_int 0.09-0.65)"),
  external=("contested", "no collapse to 272 active loci with free recombination (soft) or below ln R/D (hard); human scale and hard+linkage untested; tight linkage supports Day"))
u('G', f"R4 F2 ({R}R4-F2-A.md): no saturation of throughput at n_mid = 272 with r = 1/2 (rate linear in supply, R_int 0.975); throughput falls only with tight linkage. Per-locus P_fix was not measured directly (R_int is its average). Under independence the joint success probability multiplies, which is the specific-vs-any distinction (G3), not a barrier. Untested at human scale and with hard selection plus linkage. {RV}",
  external=("contested", "no barrier in tested regime (r = 1/2, soft, <= 272 loci); human scale untested"))
u('Gc', f"R4 F2 + H2 ({R}R4-F2-A.md, {R}R4-H2-hard.md): the Gc falsifier (P_fix < 50% of 2s at ~230 active loci, soft, free recombination) is not met in the tested regime (R_int 0.975 at 272). Under hard selection with free recombination, ~255 simultaneous open loci persist at R >= 10 (s = 0.01); at R = 2, 90 persisted and 167 did not, so ~230 concurrent sweeps persist for R >= 5. {RV}",
  external=("contested", "falsifier not met in tested regime; ~230 concurrent sweeps persist under hard selection for R >= 5; human scale untested"))

# ---------------- H branch ----------------
u('H', f"R4 H (`h_cost_of_selection.py`, `h_nunney_gauss*.py`, `h_keightley_load.py`; {R}R4-H-C2.md) and H2 hard multilocus ({R}R4-H2-hard.md). Arithmetic holds (300 = 30/0.10; 487 = 146,250/300; 41,068). D = 30 is Haldane's input: diploid D = 2 ln(1/p0) gives 92-278 generations for standing variation (p0 1e-2 to 1e-6) and ~200 for a new mutation (p0 = 1/2N, D ~ 20), so 300 is the same order as the new-mutation case (Day-side point). Under hard selection the cap is ln R / D, so 10% is not a general bound; at R >= 1.3, haploid D ~ 7 the flip lies 9-100x above 1/300 (bracket). Haldane's own regime (R ~ 1.1, diploid D ~ 20-30 = ~1/300) was not tested, so the literal 1/300 is untested, not falsified. In the Nunney reconstruction soft selection did NOT remove the cost (soft T50 > hard T50 at equal supply, both models): the critics' stock reply is not reproduced (credit to Day). Human M and R are undetermined by the repo. The comparison with the 20M total falls under the scope argument Day conceded for Term 3 (H1). {RV}",
  internal=("holds", "arithmetic 300, 487, 41,068"),
  external=("contested", "cap is ln R/D, so 10% is not general; Haldane regime (R ~1.1, D ~20-30) untested; soft selection did not remove cost; human M, R undetermined; H1 scope applies to the 20M comparison"))
u('H1', f"R4 H ({R}R4-H-C2.md): Term 3 arithmetic 0.45/(2 ln 6600) = 0.02558/gen (one per 39.1); about 6,650 over 260,000 generations. Same-basis ratio to Haldane + d is 17.1 (the earlier 7.7 mixed bases; 17.1/7.7 = 1/d). The retraction's scope (cost bounds selected substitutions only) is consistent with neutral k = U (B0.5) and applies equally to H's comparison with the 20M total; whether Day intends that is not stated. {RV}",
  internal=("holds", "arithmetic; same-basis ratio 17.1"),
  external=("supported", "cost bounds selected substitutions only; neutral k = U (B0.5)"))
u('H2', f"R4 H Model 1/2 ({R}R4-H-C2.md; EXPLORATORY reconstruction, Nunney's Eq. 3 and 5 lost in extraction, adjusted twice after seeing results): the qualitative M-dependence is reproduced (T50 rises as M falls, more steeply for n = 7). Absolute values are not (R = 10 is 2-12x below Nunney; R = 2.2, M = 0.1 hard gives 170 vs ~300). Soft selection did not reduce the cost at equal mutation supply (soft T50 1.5-3.5x hard). Human M is undetermined. {RV}",
  external=("contested", "M-dependence reproduced; absolute T and the soft-selection 'elimination' not reproduced in the reconstruction; human M undetermined"))
u('H5', f"R4 H ({R}R4-H-C2.md): Hössjer's 15,800 is 10.5x Haldane's own 1,500 over 450,000 generations (675 with d); it comes from a mutation-rate scaling, not a cost computation, so the cost step is unsupported by the Haldane arithmetic. {RV}",
  internal=("non-sequitur", "the 15,800 is a rate scaling, not a cost computation (10.5x Haldane's 1,500)"),
  external=("contested", "depends on H"))
u('H6', f"R4 H/H1 ({R}R4-H-C2.md): consistent with neutral k = U (B0.5, z = +0.13 / -0.64) and with Day's own 2026-05-07 narrowing (H1). The scope point says nothing about the cost of selected substitutions, which remains open (H). {RV}",
  internal=("holds", ""),
  external=("supported", "cost bounds selected substitutions; neutral k = U (B0.5)"))
u('H7', f"R4 H7 (`h_keightley_load.py`, K = 1000, 6 reps; {R}R4-H-C2.md) and H2 ({R}R4-H2-hard.md): hard multiplicative selection at U = 2.2, s = 0.05 goes extinct for Fmax = 4-20 and persists at 30 (N/K 0.174 vs predicted 0.188; ratchet regime) and 60 (0.344 vs 0.353); threshold 2e^U = 18.1 offspring per female. Soft selection persists at every Fmax. In H2 the combined condition is lam*D + U < ln R. This supports Keightley's statement but does not decide whether human selection is hard or soft (Day-side use: a hard-selection population at U = 2.2 is near its limit). {RV}",
  external=("supported", "hard selection at U = 2.2 needs ~18 offspring per female; does not decide hard vs soft"))
u('H8', f"R4 H ({R}R4-H-C2.md): 0.45/(2 x 3.1e9 x ln 6,600) = 8.25e-12 per site (holds); 0.0256 per generation (one per 39). Implied per-substitution cost 2 ln(2Ne) = 17.6 against s_max = 1.0, vs Haldane's D = 30 and 0.10; same-basis ratio to Haldane + d is 17.1. In H2's hard model the cap is ln R / D, so s_max = 1 corresponds to a large reproductive excess (ln R = 1, R ~ 2.7), not Haldane's 10%. The two cost figures in the corpus are not reconciled. {RV}",
  internal=("holds", "arithmetic"),
  external=("contested", "s_max = 1 implies R ~ 2.7, not Haldane's 10%; 17.1x Haldane + d on the same basis"))


def fmt(key, val):
    v, c = val
    return f'  {key}: "{v}"' + (f'   # {c}' if c else '')


files = {}
for p in glob.glob(os.path.join(CL, '*.md')):
    if os.path.basename(p).startswith('_'):
        continue
    t = open(p).read()
    m = re.search(r'^id: (\S+)$', t, re.M)
    files[m.group(1)] = p

for cid, (verd, check) in U.items():
    p = files[cid]
    t = open(p).read()
    fm_end = t.index('\n---\n', 4)
    fm, body = t[:fm_end], t[fm_end:]
    for k, val in verd.items():
        fm, n = re.subn(rf'^  {k}:.*$', fmt(k, val), fm, count=1, flags=re.M)
        assert n == 1, (cid, k)
    fm = re.sub(r'^status: \S+.*$', 'status: reviewed', fm, count=1, flags=re.M)
    line = check
    if '## Check' in body:
        i = body.index('## Check')
        j = body.find('\n## ', i + 5)
        j = len(body) if j < 0 else j
        sec = body[i:j]
        content = sec[len('## Check'):].strip('\n')
        stale = re.search(r'not run|not yet|planned|none yet|Result: none|Review: pending', content)
        if stale and ('Script: none' in content or 'not run' in content or 'not yet' in content or 'planned' in content or 'none yet' in content):
            new = '## Check\n' + line + '\n' + ('Earlier note: ' + content + '\n' if content else '')
        else:
            new = '## Check\n' + content + '\n\n' + line + '\n'
        body = body[:i] + new + ('\n' if j < len(body) else '') + body[j:].lstrip('\n') if j < len(body) else body[:i] + new
    else:
        k = body.find('## Simulator variables implied')
        add = '## Check\n' + line + '\n\n'
        body = body[:k] + add + body[k:] if k >= 0 else body.rstrip('\n') + '\n\n' + add
    open(p, 'w').write(fm + body)
    print('updated', cid)

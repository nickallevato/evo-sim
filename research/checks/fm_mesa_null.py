"""FMnull: neutral-null calibration of Day's substitution-density overdispersion ("more than 80 times more
variable than a uniform-rate process predicts"), as a function of window size W and divergence d.

PRE-REGISTERED: this docstring, the parameter brackets (COMPONENTS, UNITS, TREE) and the scoring rule are
committed BEFORE the analytic table, the simulation or the real-data arm is run.  Only `selftest` (tiny
synthetic input, local, 1.6 s, 120 MB RSS) was run before the commit.  Any later change to a bracket, a
threshold or the scoring rule goes in a separate commit labelled "post hoc".

TIER. LOAD-BEARING (three reviews: correctness, steelman-day, steelman-critic).  The check informs FM3 (statistic
and magnitude) and the FM10 premise "neutral diffusive drift" is not viable (FM10 and ROOT-FM are
`load_bearing: true`).

TARGET QUOTES (verbatim; voxday.net "The Fourth Mechanism", 2026-10-10; local copy hash in quotes-day.md)
  Q164 (FM3, ¶4) "The substitution density across the genome is massively overdispersed, more than 80 times more
       variable than a uniform-rate process predicts."
  Q165 (FM4, ¶4) "Dense regions cluster next to other dense regions, forming contiguous blocks of elevated
       substitution with sharp boundaries in a pattern we call mesas."
  Q171 (FM10, ¶8) "What we do know is that neither natural selection nor neutral diffusive drift can still be
       considered viable candidates. ..."
  Q162 (FM1, ¶3) "... to analyze all six complete ape genomes provided by the T2T Primate Consortium."
  No window size, statistic, lineage unit, masking or code released (refreshes 2026-10-10, -11, -12-day).

WHAT THIS CHECK ADDS TO R4-FM.  R4-FM measured phi on the real alignment (1 kb - 1 Mb) and a shared-rate null that
borrows rate variation from the other lineages.  It did not say what a NEUTRAL MECHANISTIC model predicts for the
index at each W.  This check gives that: a lookup table W x d -> neutral band, scoreable the moment Day publishes
W and the statistic, plus a consistency test against the R4-FM numbers already committed (raw/fm_analyse.json).

STATISTIC: READINGS (rule RD; every plausible reading carried, none chosen)
  R1  dispersion index D = Var(n_w) / mean(n_w) over equal windows (Poisson null: D = 1); "80 times more
      variable" = variance ratio; threshold T = 80.  R1b = R4-FM's exposure-weighted binomial phi (same as R1 up
      to (1 - p) and exposure; carried by the same numbers).  R1x = "80 times MORE" read as D - 1 > 80 (T = 81;
      reported, numerically indistinguishable).
  R2  SD ratio: SD(n_w) / Poisson SD > 80, i.e. D > 6400 ("variable" read as standard deviation / CV ratio).
  Unit sub-readings (what is counted; "across the genome", "all six complete ape genomes"):
    U-H    human-lineage substitutions (parsimony, outgroups)          d = 0.0051 (R4-FM F0 density, in-house)
    U-C    chimp lineage                                               d = 0.0057 (in-house)
    U-G    gorilla terminal                                            d = 0.0077 (in-house)
    U-DHC  human-chimp pairwise differences, unpolarised               d in [0.0123, 0.0146] (CSAC2005 1.23%;
           Yoo2025 SI III.14 1.46%; in-house 0.0137)
    U-TREE substitutions summed over every branch of the seven-ape tree (one count per event) d in [0.03, 0.15]
           (UNSOURCED bracket)
    U-PAIRS differences summed over all 21 pairs (each event counted once per pair it separates): a uniform-rate
           process already gives D_struct = sum a_b^2 t_b / sum a_b t_b > 1 (a_b = s(n - s)); sub-readings
           U-PAIRS-naive (null = Poisson, D_struct counted as overdispersion) and U-PAIRS-struct (null includes
           D_struct; index = 1 + excess / D_struct).  Branch lengths in TREE are UNSOURCED except H, C, G terminal
           (in-house); the band scales the pairwise length by 0.7 (N_lo) and 1.3 (N_hi); the rate field is taken
           as fully shared by all branches (upper-side simplification).
  Exposure c = aligned (core) bp per window / W in {0.5, 1.0} (R4-FM: 86% of 1-kb bins pass at F0).

NEUTRAL MODEL (no selection).  Window count n_w ~ Poisson(c W d Rbar_w); Rbar_w = window mean of a relative-rate
field R(x) = prod_i F_i(x), independent stationary log-normal factors with mean 1, Var sigma_i^2 and log-scale
exponential autocorrelation (length ell_i).  Exact: D = 1 + c W d V(W), V(W) = Var(Rbar_w) from the discrete
covariance sum at BIN_BP resolution.  First-order check: D ~ 1 + mean * CV^2, CV^2 = sum sigma_i^2 g(W/ell_i),
g(x) = 2(x - 1 + e^-x)/x^2 (both printed).  Consequence fixed in advance: a component with ell << W adds a
W-INDEPENDENT 2 d sigma^2 ell to D; only components with ell >~ W make D grow linearly in W.
Components (sigma = SD of the relative rate at the component's own scale; ALL brackets UNSOURCED unless noted;
fetch items below):
  M0   chromosome-scale (subtelomeric etc.)            sigma [0.02, 0.10]   ell [5, 20] Mb
  M1   replication timing / large-scale mu             sigma [0.05, 0.20]   ell [0.5, 2] Mb
  M2   meso-scale (isochore, chromatin)                sigma [0.05, 0.20]   ell [20, 100] kb
  M3   fine-scale context clusters                     sigma [0.10, 0.40]   ell [0.2, 2] kb
  CPG  regional CpG-content variation                  sigma [0.03, 0.15]   ell [5, 50] kb
  GBGC recombination-associated gBGC                   sigma [0.02, 0.10]   ell [50 kb, 1 Mb]; lineage-specific
       fraction lambda [0.3, 1.0] (PRDM9 turnover)
  ILS  ancestral coalescence depth (incl. ancestral polymorphism): sigma = T2/(t1 + T2) with t1 6-7 My, T2 1-2 My
       (SOURCED: CSAC2005 quote, quotes-literature.md "Genome-wide rates") -> [0.125, 0.25]; tract length
       ell [0.1, 2] kb UNSOURCED (derivation: 1/(r 2 T2) ~ 126 bp at r = 1e-8, Ne 198,000 from Yoo2025)
  ALN  alignment / paralog / mappability error (UNMASKED arm only): sigma^2 = pi(1-pi)e^2, pi [0.001, 0.02],
       e [0.5, 3] -> sigma [0.016, 0.42]   ell [10, 100] kb
  Bands: N_lo = neutral components at (sigma_lo, ell_lo), c = 0.5; N_hi(masked) = at (sigma_hi, ell_hi), c = 1.0;
  N_hi(unmasked) = N_hi + ALN_hi.  Because V is monotone in every sigma and ell, the band is the bracket image.

SELECTION ARM (known non-neutral mechanisms; band K = N plus these)
  BGS  linked selection on ancestral Ne -> T2 (Scally2012: "most likely due to natural selection reducing Ne and
       making ILS less likely", held): sigma = [T2/(t1+T2)] sd(B), sd(B) [0.05, 0.25] UNSOURCED -> [0.006, 0.0625],
       ell [0.2, 2] Mb; SHARED by H and C, NEGATIVELY correlated with gene density / conservation (troughs, not
       mesas).  K_hi = N_hi(unmasked) + BGS_hi.
  Sweeps on a terminal lineage change expected neutral divergence by 0 (fixation probability = frequency); the
  variance they add per window is ~ (pi_anc / 2) W (~50 per 100 kb, Poisson variance ~500): negligible; recorded,
  not modelled.  Positive selection on coding/regulatory sites: each excess substitution is one adaptive
  fixation; a 100-kb mesa with hundreds of excess substitutions needs hundreds of adaptive fixations in that window
  (the Haldane/MITTENS comparison of FM5 applies only on this reading).
  SIGILLATION model (Day-side alternative; simulation only): H-only blocks of length Lb in {20, 100} kb with excess
  e in {0.5, 1.0} over genome fraction f in {0.005, 0.02}; "dominant source of divergence" (FM8b) needs
  f e / (1 + f e) > 0.5, i.e. f e > 1.

WHAT DISTINGUISHES "A FOURTH MECHANISM" FROM KNOWN MECHANISMS (criteria fixed now; for any future data)
  Day-supporting observables (each scored DAY if met by > 3x the relevant neutral upper bound):
   S1  index far above N_hi at EVERY plausible W (and after covariate regression);
   S2  lineage specificity: phi_HC (dispersion of the H/(H+C) split) > 3x its neutral upper bound (below);
   S3  edges sharper than the shortest-ell component allows AND |Spearman| < 0.1 with GC, CpG, repeat, recombination
       and replication-timing covariates;
   S4  tree-incongruent sharing: mesas shared by H and G but not C (or C and G, not H) above the ILS rate
       (Scally2012: "In 30% of the genome, gorilla is closer to human or chimpanzee than the latter are to each
       other", held) at matched density.
  Critic-supporting: index inside the band at Day's W; mesas shared across lineages (k = mu predicts the SAME
  windows high in every lineage: expected corr(H, C) density at W is CV2_shared / sqrt((CV2_H + 1/m_H)(CV2_C +
  1/m_C))); covariate correlations; phi_HC inside its neutral band.
  Neutral phi_HC band: 1 + N p(1-p) (V_lsH + V_lsC), N = mean H+C count, V_ls = lineage-specific variance
  (lambda x GBGC, plus ALN for unmasked).

PREDICTIONS (fixed now; hand estimates from the formulas, central exposure c = 1, the script's table governs)
  P1 (R1, U-DHC d 0.012, masked)  80 lies INSIDE [N_lo, N_hi] at W = 100 kb (hand: ~[5.7, ~133]) and 1 Mb
     (~[24, ~740]); ABOVE N_hi at W <= 10 kb (hand N_hi ~24).  Critic expects inside at >= 100 kb; Day expects
     above at every W <= 1 Mb.
  P2 (R1, U-H d 0.0051)  inside at 1 Mb (~[10, ~310]); above masked N_hi at <= 100 kb (~55) but inside unmasked
     N_hi at 100 kb (~120).
  P3 (R2, T = 6400)  above N_hi(unmasked) at every W <= 1 Mb for U-H, U-C, U-G, U-DHC (Day-side under R2); inside
     only for U-TREE/U-PAIRS at W >= ~3-10 Mb, if at all.  Recorded as a Day-side point if it holds.
  P4 (consistency, the key cell)  using the committed R4-FM phi (raw/fm_analyse.json), the window W80 at which the
     real data reach T = 80 (log-log interpolation; F0 and F2; H, C, B, G, DHC) lies where 80 is INSIDE the band
     (F0 vs unmasked, F2 vs masked).  CRITIC: inside for every lineage.  DAY: above N_hi by > 3x for some
     lineage.  For R2 (6400) the data reach T only beyond 1 Mb (extrapolated, flagged): reported as "R2 implies W >
     1 Mb on these data", then scored at the extrapolated W.
  P5 (bracket adequacy, not a Day/critic test)  >= 80% of the R4-FM autosomal grid cells (F0 vs unmasked band,
     F2 and F3 vs masked band; 1 kb - 1 Mb; H, C, B, G, DHC; exposure c in [0.5, 1]) fall inside their band.
     Cells ABOVE the band are reported as unexplained heterogeneity (a Day-side point) or bracket failure, not
     hidden.  Audit guess: DHC F0 1 kb may lie above (fine-scale indel/misalignment clustering).
  P6 (simulation reproduces analytic)  mean simulated D within 15% of the exact expectation (D - 1) at W <= 1 Mb,
     every band cell; Poisson baseline 1.00 +/- 0.05.
  P7 (selection arm)  BGS_hi adds <= 25% to N_hi(unmasked) at every W <= 1 Mb; corr(H density, gene-density
     covariate) < 0 under BGS; neutral phi_HC at 100 kb in [1, 6] (masked); corr(H, C) >= 0.6 at W >= 100 kb under
     the central neutral model.
  P8 (sigillation detectability)  f = 0.02, e = 1, Lb = 100 kb gives phi_HC > 10 at 100 kb (> 3x the neutral
     upper bound), so a block mechanism large enough to matter is visible to S2; f e > 1 (FM8b) gives phi_HC >
     100.  Day side: the block model at f = 0.005, e = 0.5 is NOT detectable by phi alone (phi_H inside N band):
     credited as a limit of the critic's main test.

SCORING DAY'S NUMBER (frozen; `score` mode).  Inputs: his W, statistic reading, unit (or d), masking, exposure.
  value / N_hi > 3 -> DAY ("far outside"; the 3x band convention of the RH closeness test)
  1 < value / N_hi <= 3 -> MARGINAL (undecidable)
  N_lo <= value <= N_hi -> CRITIC (index unremarkable for neutral heterogeneity at that W)
  value < N_lo -> BELOW (bracket error or a different statistic; reported, no verdict move)
  Unknown W: report, per reading and unit, the W ranges giving each outcome (the lookup table); FM3 fidelity stays
  `unverifiable` (rule F).
  Verdict moves (proposed; the integration decides): CRITIC on every plausible reading -> FM3 external stays
  `supported` as a description with the annotation "unremarkable against neutral heterogeneity at W"; FM10's
  premise "drift implies a uniform rate" gets a quantitative defeater.  DAY on the most charitable plausible
  reading -> FM3 annotated "anomalous against the neutral band at W"; FM10 external moves toward `contested` (not
  `supported`: an index alone does not identify a mechanism or a lineage; S2-S4 decide that).  Reading-dependent
  outcomes are recorded per rule RD (verdict field = reading most charitable to the speaker).

REAL-DATA ARM (`realdata`; DESIGNED, NOT RUN; na-workhorse, where fm_bins.npz (74 MB) lives)
  Reuses fm_mesa_replication.load/windows on raw/fm_bins.npz (1-kb bins, classes rep/CpG/dup).  For F0 and F2,
  W in {1, 3, 10, 30, 100, 300, 1000, 3000, 10000} kb, lineages H, C, B, G, DHC: phi, mean exposure, density,
  empirical CV2_excess = (phi - 1)/(m p); NNLS fit of CV2(W) = sum_j a_j g(W / ell_j), ell_j in {1, 10, 100, 1000,
  10000} kb (empirical sigma, ell vs the brackets); covariate-adjusted phi (OLS of log((n + 0.5)/m) on GC, CpG
  fraction, repeat fraction, dup fraction, hs1 != hg38 rate); corr(H, C), corr(H, G) by W; W80 and W6400 per
  lineage; phi_HC.  Estimate: 1 process, peak ~1.5 GB (largest chromosome as int64 x 8 classes x 11 fields),
  < 15 min CPU.  Recombination and replication-timing maps are NOT held (fetch items; need a CHM13 liftover).

FETCH ITEMS (none held; brackets above are UNSOURCED until fetched and quoted)
  Hodgkinson & Eyre-Walker 2011 Nat Rev Genet 12:756 (regional mutation-rate variation, CV by scale);
  Smith, Arndt & Eyre-Walker 2018 PLoS Genet 14:e1007254 (Mb-scale DNM, divergence, diversity variation; OA);
  Phung, Huber & Lohmueller 2016 PLoS Genet 12:e1006199 (linked selection and divergence across species; OA);
  Duret & Arndt 2008 PLoS Genet 4:e1000071 (gBGC in the human genome; OA); McVicker et al. 2009 PLoS Genet
  5:e1000471 (B map, sd(B)); Hobolth et al. 2007 PLoS Genet 3:e7 (ILS tract lengths); Hwang & Green 2004 PNAS
  101:13994 (CpG rate multiple); a replication-timing map (Koren et al. 2012) and a recombination map lifted to
  CHM13.  Citation details from memory: verify before use.

RESOURCES.  analytic: < 1 s; simulate (default 300 Mb x 10 reps x 12 scenarios): 1 process, < 600 MB, ~5-15 min;
realdata: as above.  Host: na-workhorse or builder (NOT run in this commit).
  analytic : python -I research/checks/fm_mesa_null.py analytic research/checks/results/raw/fmnull_analytic.json
  simulate : python -I research/checks/fm_mesa_null.py simulate research/checks/results/raw/fmnull_sim.json
  realdata : python -I research/checks/fm_mesa_null.py realdata research/checks/results/raw/fm_bins.npz \
             research/checks/results/raw/fmnull_real.json
  score    : python -I research/checks/fm_mesa_null.py score --W 100000 --value 80 --reading R1 --unit DHC
  selftest : python -I research/checks/fm_mesa_null.py selftest
"""
import functools
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BIN_BP = 100

# name: (sigma_lo, sigma_hi), (ell_lo_bp, ell_hi_bp), arm, source note
COMPONENTS = {
    "M0":   ((0.02, 0.10), (5e6, 2e7), "neutral", "unsourced"),
    "M1":   ((0.05, 0.20), (5e5, 2e6), "neutral", "unsourced"),
    "M2":   ((0.05, 0.20), (2e4, 1e5), "neutral", "unsourced"),
    "M3":   ((0.10, 0.40), (2e2, 2e3), "neutral", "unsourced"),
    "CPG":  ((0.03, 0.15), (5e3, 5e4), "neutral", "unsourced"),
    "GBGC": ((0.02, 0.10), (5e4, 1e6), "neutral", "unsourced; lineage-specific fraction LAMBDA"),
    "ILS":  ((0.125, 0.25), (1e2, 2e3), "neutral", "sigma from CSAC2005 t1/t2; ell unsourced"),
    "ALN":  ((0.016, 0.42), (1e4, 1e5), "unmasked", "unsourced; sigma^2 = pi(1-pi)e^2"),
    "BGS":  ((0.006, 0.0625), (2e5, 2e6), "selection", "unsourced sd(B) x CSAC2005 T2/(t1+T2)"),
}
LAMBDA = (0.3, 1.0)
EXPOSURE = (0.5, 1.0)
UNITS = {"H": (0.0051, 0.0051), "C": (0.0057, 0.0057), "G": (0.0077, 0.0077), "DHC": (0.0123, 0.0146),
         "TREE": (0.03, 0.15)}
# seven-ape tree, UNSOURCED branch lengths except H, C (C term + Pan stem), G terminal (R4-FM in-house):
# ((((H,(C,B)),G),(So,Bo)),Sia); entries: (leaves below, length per site)
TREE = [(("H",), 0.0051), (("C",), 0.0020), (("B",), 0.0020), (("C", "B"), 0.0037), (("H", "C", "B"), 0.0020),
        (("G",), 0.0077), (("H", "C", "B", "G"), 0.0040), (("So",), 0.0030), (("Bo",), 0.0030),
        (("So", "Bo"), 0.0100), (("Sia",), 0.0300)]
NTAXA = 7
READINGS = {"R1": 80.0, "R1x": 81.0, "R2": 6400.0}
WGRID = (1e3, 3e3, 1e4, 3e4, 1e5, 3e5, 1e6, 3e6, 1e7)


# ------------------------------------------------------------------------------------------------ analytic core
def comp_params(which, names):
    """which: 'lo' or 'hi' -> list of (sigma, ell)."""
    k = 0 if which == "lo" else 1
    return [(COMPONENTS[n][0][k], COMPONENTS[n][1][k]) for n in names]


def g_cont(x):
    x = np.asarray(x, float)
    return np.where(x < 1e-6, 1.0 - x / 3.0, 2.0 * (x - 1.0 + np.exp(-x)) / np.maximum(x, 1e-300) ** 2)


def cov_R(lags_bp, comps):
    """Autocovariance of R = prod of independent log-normal mean-1 factors (log-scale exp. correlation)."""
    out = np.ones_like(lags_bp, dtype=float)
    for s, ell in comps:
        s2 = math.log1p(s * s)
        out *= np.exp(s2 * np.exp(-lags_bp / ell))
    return out - 1.0


def window_var(W, comps, bin_bp=BIN_BP):
    """Var of the window mean of R over n = W/bin_bp bins (exact discrete covariance sum)."""
    n = max(1, int(round(W / bin_bp)))
    k = np.arange(n, dtype=float)
    c = cov_R(k * bin_bp, comps)
    return float((n * c[0] + 2.0 * ((n - k[1:]) * c[1:]).sum()) / n ** 2)


def cv2_first_order(W, comps):
    return float(sum(s * s * g_cont(W / ell) for s, ell in comps))


def tree_struct():
    """D_struct and pairwise multiplicity-weighted length for U-PAIRS."""
    num = den = 0.0
    for leaves, t in TREE:
        s = len(leaves)
        a = s * (NTAXA - s)
        num += a * a * t
        den += a * t
    return num / den, den


NEUTRAL = ("M0", "M1", "M2", "M3", "CPG", "GBGC", "ILS")


def band(W, d, which):
    """Return D for band edge which in {'N_lo', 'N_hi_masked', 'N_hi_unmasked', 'K_hi'} at exposure edge."""
    if which == "N_lo":
        comps, c = comp_params("lo", NEUTRAL), EXPOSURE[0]
    elif which == "N_hi_masked":
        comps, c = comp_params("hi", NEUTRAL), EXPOSURE[1]
    elif which == "N_hi_unmasked":
        comps, c = comp_params("hi", NEUTRAL + ("ALN",)), EXPOSURE[1]
    elif which == "K_hi":
        comps, c = comp_params("hi", NEUTRAL + ("ALN", "BGS")), EXPOSURE[1]
    else:
        raise ValueError(which)
    return 1.0 + c * W * d * window_var(W, comps), 1.0 + c * W * d * cv2_first_order(W, comps)


@functools.lru_cache(maxsize=None)
def unit_bands(unit, W):
    """Bands for a unit; d bracket edges go with the band edge (lo d for N_lo, hi d for N_hi)."""
    out = {}
    if unit.startswith("PAIRS"):
        dstruct, dp = tree_struct()
        for edge, scale in (("N_lo", 0.7), ("N_hi_masked", 1.3), ("N_hi_unmasked", 1.3), ("K_hi", 1.3)):
            D, _ = band(W, dp * scale, edge)          # 1 + c W d_pairs V(W), rate field fully shared by branches
            ex = D - 1.0
            # naive: Poisson null, structural excess counted as overdispersion; struct: Var / Var_uniform
            out[edge] = dstruct + ex if unit == "PAIRS-naive" else 1.0 + ex / dstruct
        out["D_struct"] = dstruct
        return out
    dlo, dhi = UNITS[unit]
    for edge in ("N_lo", "N_hi_masked", "N_hi_unmasked", "K_hi"):
        D, D1 = band(W, dlo if edge == "N_lo" else dhi, edge)
        out[edge] = D
        out[edge + "_firstorder"] = D1
    return out


def classify(value, lo, hi):
    if value > 3.0 * hi:
        return "DAY"
    if value > hi:
        return "MARGINAL"
    if value >= lo:
        return "CRITIC"
    return "BELOW"


def crossing_windows(unit, T, hi_key):
    """Smallest W where N_hi >= T (below it T is anomalous) and smallest W where N_lo >= T (beyond it T is low)."""
    Ws = np.logspace(3, 7.5, 91)
    w_hi = w_lo = None
    for W in Ws:
        b = unit_bands(unit, W)
        if w_hi is None and b[hi_key] >= T:
            w_hi = float(W)
        if w_lo is None and b["N_lo"] >= T:
            w_lo = float(W)
    return w_hi, w_lo


def analytic(outjson, fm_json=None):
    fm_json = fm_json or os.path.join(HERE, "results", "raw", "fm_analyse.json")
    units = list(UNITS) + ["PAIRS-naive", "PAIRS-struct"]
    res = {"brackets": {k: list(map(list, v[:2])) + list(v[2:]) for k, v in COMPONENTS.items()},
           "units": UNITS, "tree_struct": tree_struct(), "table": {}, "crossings": {}, "scores": {}}
    for u in units:
        for W in WGRID:
            res["table"][f"{u}|{int(W)}"] = unit_bands(u, W)
    for u in units:
        for r, T in READINGS.items():
            for hk in ("N_hi_masked", "N_hi_unmasked"):
                res["crossings"][f"{u}|{r}|{hk}"] = crossing_windows(u, T, hk)
            for W in WGRID:
                b = res["table"][f"{u}|{int(W)}"]
                res["scores"][f"{u}|{r}|{int(W)}"] = {
                    "masked": classify(T, b["N_lo"], b["N_hi_masked"]),
                    "unmasked": classify(T, b["N_lo"], b["N_hi_unmasked"])}
    # selection arm share
    res["bgs_share"] = {}
    for u in ("H", "DHC"):
        for W in WGRID:
            b = res["table"][f"{u}|{int(W)}"]
            res["bgs_share"][f"{u}|{int(W)}"] = (b["K_hi"] - b["N_hi_unmasked"]) / (b["N_hi_unmasked"] - 1.0)
    res["inhouse"] = inhouse(fm_json) if os.path.exists(fm_json) else "fm_analyse.json not found"
    json.dump(res, open(outjson, "w"), indent=1)
    print_table(res)
    return res


def inhouse(fm_json):
    """P4 and P5 against the committed R4-FM grid (raw/fm_analyse.json)."""
    g = json.load(open(fm_json))["grid"]
    Wmap = {"1kb": 1e3, "10kb": 1e4, "100kb": 1e5, "1Mb": 1e6}
    cells, curves = [], {}
    for key, v in g.items():
        st, filt, wl = key.split("|")
        if st != "auto" or wl not in Wmap:
            continue
        W = Wmap[wl]
        hk = "N_hi_unmasked" if filt in ("F0", "F1") else "N_hi_masked"
        for L in ("H", "C", "B", "G", "DHC"):
            if L not in v or "phi" not in v[L]:
                continue
            p, phi = v[L]["density"], v[L]["phi"]
            lo, _ = band(W, p, "N_lo")
            hi, _ = band(W, p, hk)
            cells.append(dict(cell=key, L=L, phi=phi, d=p, lo=lo, hi=hi, out=classify(phi, lo, hi)))
            curves.setdefault((filt, L), []).append((W, phi, p))
    inside = sum(c["out"] == "CRITIC" for c in cells)
    p4 = {}
    for (filt, L), pts in curves.items():
        pts.sort()
        if len(pts) < 2:
            continue
        lw = np.log([q[0] for q in pts])
        lp = np.log([max(q[1], 1.0001) for q in pts])
        dmean = float(np.mean([q[2] for q in pts]))
        hk = "N_hi_unmasked" if filt in ("F0", "F1") else "N_hi_masked"
        for r, T in READINGS.items():
            if lp[-1] >= math.log(T):
                W80 = float(np.exp(np.interp(math.log(T), lp, lw)))
                extrap = False
            else:   # log-log extrapolation from the last two points (flagged)
                slope = (lp[-1] - lp[-2]) / (lw[-1] - lw[-2])
                W80 = float(np.exp(lw[-1] + (math.log(T) - lp[-1]) / max(slope, 1e-6)))
                extrap = True
            lo, _ = band(W80, dmean, "N_lo")
            hi, _ = band(W80, dmean, hk)
            p4[f"{filt}|{L}|{r}"] = dict(W_T=W80, extrapolated=extrap, lo=lo, hi=hi, out=classify(T, lo, hi))
    return {"P5_cells": cells, "P5_inside": inside, "P5_n": len(cells), "P4": p4}


def print_table(res):
    print("unit | W | N_lo | N_hi masked | N_hi unmasked | K_hi")
    for k, b in res["table"].items():
        print(k, *(f"{b[e]:.3g}" for e in ("N_lo", "N_hi_masked", "N_hi_unmasked", "K_hi")))
    for k, v in res["crossings"].items():
        print("cross", k, v)
    if isinstance(res.get("inhouse"), dict):
        ih = res["inhouse"]
        print(f"P5 inside {ih['P5_inside']}/{ih['P5_n']}")
        for k, v in ih["P4"].items():
            print("P4", k, {a: (round(b, 3) if isinstance(b, float) else b) for a, b in v.items()})


# ------------------------------------------------------------------------------------------------ simulation
def ar1_lognormal(n, sigma, ell, rng, bin_bp=BIN_BP):
    from scipy.signal import lfilter
    s2 = math.log1p(sigma * sigma)
    s = math.sqrt(s2)
    rho = math.exp(-bin_bp / ell)
    eps = rng.standard_normal(n)
    x = lfilter([s * math.sqrt(1.0 - rho * rho)], [1.0, -rho], eps, zi=[rho * s * rng.standard_normal()])[0]
    return np.exp(x - s2 / 2.0)


def rate_field(n, comps, rng, bin_bp=BIN_BP):
    R = np.ones(n)
    for s, ell in comps:
        if s > 0:
            R *= ar1_lognormal(n, s, ell, rng, bin_bp)
    return R


def disp(counts, W_bins):
    k = len(counts) // W_bins
    w = counts[: k * W_bins].reshape(k, W_bins).sum(axis=1)
    return float(w.var(ddof=1) / w.mean()), w


def expected_sample_D(W, d, comps, n_total, bin_bp=BIN_BP):
    """E[s^2]/mean over K windows of one stationary chromosome of n_total bins (finite-genome correction)."""
    nW = int(round(W / bin_bp))
    K = n_total // nW
    Vw = window_var(W, comps, bin_bp)
    VG = window_var(K * nW * bin_bp, comps, bin_bp)
    m = W * d
    return 1.0 + m * K / (K - 1.0) * (Vw - VG)


def split_phi(h, c):
    N = h + c
    ok = N > 0
    p = h[ok].sum() / N[ok].sum()
    e = N[ok] * p
    return float((((h[ok] - e) ** 2) / (e * (1 - p))).sum() / (ok.sum() - 1))


def sim_two_lineage(n, comps_shared, comps_ls, dH, dC, rng, blocks=None, bgs=None, bin_bp=BIN_BP):
    """H and C counts with a shared field, independent lineage-specific fields, optional BGS (shared, with an
    observed covariate) and optional H-only sigillation blocks (Lb_bp, e, f)."""
    Rs = rate_field(n, comps_shared, rng, bin_bp)
    cov = None
    if bgs is not None:
        s, ell = bgs
        gfield = ar1_lognormal(n, 0.5, ell, rng, bin_bp)        # gene-density covariate (log-normal)
        z = (np.log(gfield) - np.log(gfield).mean()) / np.log(gfield).std()
        Rs = Rs * np.clip(1.0 - s * z, 0.05, None)
        cov = z + 0.5 * rng.standard_normal(n)
    RH = Rs * rate_field(n, comps_ls, rng, bin_bp)
    RC = Rs * rate_field(n, comps_ls, rng, bin_bp)
    if blocks is not None:
        Lb, e, f = blocks
        nb = max(1, int(round(Lb / bin_bp)))
        nblk = int(round(f * n / nb))
        starts = rng.choice(n // nb, size=nblk, replace=False) * nb
        mult = np.ones(n)
        for s0 in starts:
            mult[s0:s0 + nb] += e
        RH = RH * mult
    H = rng.poisson(bin_bp * dH * RH)
    C = rng.poisson(bin_bp * dC * RC)
    return H, C, cov


def central(names):
    return [(math.sqrt(COMPONENTS[k][0][0] * COMPONENTS[k][0][1]), math.sqrt(COMPONENTS[k][1][0] * COMPONENTS[k][1][1]))
            for k in names]


def simulate(outjson, genome_mb=300, reps=10, seed=20261012):
    rng = np.random.default_rng(seed)
    n = int(genome_mb * 1e6 / BIN_BP)
    res = {"genome_mb": genome_mb, "reps": reps, "seed": seed, "P6": {}, "arms": {}}
    # P6: neutral bands reproduced (single lineage, d = 0.012 and 0.0051)
    for edge, comps in (("N_lo", comp_params("lo", NEUTRAL)), ("N_hi_masked", comp_params("hi", NEUTRAL)),
                        ("N_hi_unmasked", comp_params("hi", NEUTRAL + ("ALN",))), ("poisson", [])):
        for d in (0.0051, 0.012):
            Ds = {W: [] for W in (1e3, 1e4, 1e5, 1e6)}
            for _ in range(reps):
                cnt = rng.poisson(BIN_BP * d * rate_field(n, comps, rng))
                for W in Ds:
                    Ds[W].append(disp(cnt, int(W / BIN_BP))[0])
            for W, v in Ds.items():
                exp = expected_sample_D(W, d, comps, n) if comps else 1.0
                res["P6"][f"{edge}|{d}|{int(W)}"] = dict(sim=float(np.mean(v)), sd=float(np.std(v)), exp=exp,
                                                         rel=float((np.mean(v) - 1) / (exp - 1)) if comps else None)
    # selection and sigillation arms (two lineages; central neutral; lineage-specific GBGC fraction LAMBDA)
    lam = math.sqrt(LAMBDA[0] * LAMBDA[1])
    sh = [c for k, c in zip(NEUTRAL, central(NEUTRAL)) if k != "GBGC"]
    sg, lg = central(("GBGC",))[0]
    shared = sh + [(sg * math.sqrt(1 - lam), lg)]
    ls = [(sg * math.sqrt(lam), lg)]
    scen = {"S0_neutral": {}, "S0_hi_ls": {"ls": [(COMPONENTS["GBGC"][0][1], COMPONENTS["GBGC"][1][1])]},
            "S1_bgs": {"bgs": (COMPONENTS["BGS"][0][1], 1e6)}}
    for Lb in (2e4, 1e5):
        for e in (0.5, 1.0):
            for f in (0.005, 0.02):
                scen[f"S2_sig_L{int(Lb/1e3)}k_e{e}_f{f}"] = {"blocks": (Lb, e, f)}
    scen["S2_sig_dominant_L100k_e2_f0.5"] = {"blocks": (1e5, 2.0, 0.5)}
    for name, sp in scen.items():
        acc = {}
        for _ in range(reps):
            H, C, cov = sim_two_lineage(n, shared, sp.get("ls", ls), 0.0051, 0.0057, rng,
                                        blocks=sp.get("blocks"), bgs=sp.get("bgs"))
            for W in (1e4, 1e5, 1e6):
                nb = int(W / BIN_BP)
                k = n // nb
                h = H[: k * nb].reshape(k, nb).sum(1).astype(float)
                c = C[: k * nb].reshape(k, nb).sum(1).astype(float)
                r = acc.setdefault(int(W), {"phi_H": [], "phi_C": [], "phi_HC": [], "corr_HC": [], "corr_cov": [],
                                            "phi_res_H": []})
                r["phi_H"].append(h.var(ddof=1) / h.mean())
                r["phi_C"].append(c.var(ddof=1) / c.mean())
                r["phi_HC"].append(split_phi(h, c))
                r["corr_HC"].append(float(np.corrcoef(h, c)[0, 1]))
                E = h.sum() / c.sum() * (c + 1.0)          # shared-rate null as in R4-FM (one pseudo-count)
                r["phi_res_H"].append(float(((h - E) ** 2 / E).sum() / (k - 1)))
                if cov is not None:
                    cw = cov[: k * nb].reshape(k, nb).mean(1)
                    r["corr_cov"].append(float(np.corrcoef(h, cw)[0, 1]))
        res["arms"][name] = {W: {s: (float(np.mean(v)) if v else None) for s, v in r.items()} for W, r in acc.items()}
        print(name, json.dumps(res["arms"][name]), flush=True)
    json.dump(res, open(outjson, "w"), indent=1)
    return res


# ------------------------------------------------------------------------------------------------ real data
def realdata(npz, outjson):
    sys.path.insert(0, HERE)
    import fm_mesa_replication as fm
    from scipy.optimize import nnls
    z, meta, chroms_all = fm.load(npz)
    auto = [c for c in chroms_all if c not in ("chrX", "chrY", "chrM")]
    WK = (1, 3, 10, 30, 100, 300, 1000, 3000, 10000)
    ells = np.array([1e3, 1e4, 1e5, 1e6, 1e7])
    res = {"grid": {}, "fit": {}, "W_T": {}}
    for filt in ("F0", "F2"):
        curves = {}
        for Wk in WK:
            try:
                w, cid, ok = fm.windows(z, auto, filt, Wk)
            except ValueError:          # no chromosome long enough for this window
                continue
            if ok.sum() < 20:
                continue
            m = w["m"][ok].astype(float)
            cell = {"k": int(ok.sum()), "m_mean": float(m.mean())}
            cls = {}
            for name, idx in (("rep", (1, 3, 5, 7)), ("cpg", (2, 3, 6, 7)), ("dup", (4, 5, 6, 7))):
                idx = tuple(i for i in idx if i in fm.FILTERS[filt])
                if not idx:
                    continue
                a, _, _ = fm.windows_cls(z, auto, idx, Wk)
                cls[name] = a[ok] / np.maximum(m, 1)   # same window order as fm.windows (per chromosome, nb windows)
            X = [np.ones_like(m), w["gc"][ok] / m, w["hh"][ok] / m] + list(cls.values())
            X = np.column_stack(X)
            for L in ("H", "C", "B", "G", "DHC"):
                n = w[L][ok].astype(float)
                phi, _ = fm.phi_uniform(n, m)
                p = n.sum() / m.sum()
                y = np.log((n + 0.5) / m)
                beta, *_ = np.linalg.lstsq(X, y, rcond=None)
                E = m * np.exp(X @ beta)
                E *= n.sum() / E.sum()
                phi_cov = float(((n - E) ** 2 / E).sum() / (len(n) - X.shape[1]))
                cv2 = (phi - 1.0) / (m.mean() * p)
                cell[L] = {"phi": phi, "density": float(p), "cv2_excess": float(cv2), "phi_cov": phi_cov}
                curves.setdefault(L, []).append((Wk * 1000.0, phi, cv2))
            h, c, g = (w[k][ok].astype(float) for k in ("H", "C", "G"))
            cell["corr_HC"] = float(np.corrcoef(h / m, c / m)[0, 1])
            cell["corr_HG"] = float(np.corrcoef(h / m, g / m)[0, 1])
            cell["phi_HC"] = fm_split(h, c)
            res["grid"][f"{filt}|{Wk}kb"] = cell
            print(filt, Wk, json.dumps({k: v for k, v in cell.items() if not isinstance(v, dict)}), flush=True)
        for L, pts in curves.items():
            lw = np.log([q[0] for q in pts])
            lp = np.log(np.maximum([q[1] for q in pts], 1.0001))
            for r, T in READINGS.items():
                res["W_T"][f"{filt}|{L}|{r}"] = (float(np.exp(np.interp(math.log(T), lp, lw)))
                                                 if lp.max() >= math.log(T) else None)
            pos = [q for q in pts if q[2] > 0]
            Ws = np.array([q[0] for q in pos])
            cv2 = np.array([q[2] for q in pos])
            if len(pos) < 2:
                res["fit"][f"{filt}|{L}"] = "fewer than 2 windows sizes with positive excess"
                continue
            A = np.column_stack([g_cont(Ws / l) for l in ells]) / cv2[:, None]
            coef, rnorm = nnls(A, np.ones_like(cv2))
            res["fit"][f"{filt}|{L}"] = {"ell_bp": ells.tolist(), "sigma2": coef.tolist(), "rel_resid": float(rnorm)}
    json.dump(res, open(outjson, "w"), indent=1)
    return res


def fm_split(h, c):
    return split_phi(h, c)


# ------------------------------------------------------------------------------------------------ score / selftest
def score(W, value, reading, unit, masked):
    b = unit_bands(unit, W)
    hk = "N_hi_masked" if masked else "N_hi_unmasked"
    D = value if reading in ("R1", "R1b") else (value + 1.0 if reading == "R1x" else value ** 2)
    out = dict(W=W, reading=reading, unit=unit, D=D, lo=b["N_lo"], hi=b[hk], outcome=classify(D, b["N_lo"], b[hk]))
    print(json.dumps(out))
    return out


def selftest():
    import tempfile
    rng = np.random.default_rng(1)
    # 1. exact log-normal vs first-order formula at small sigma
    comps = [(0.1, 1e4)]
    for W in (1e3, 1e5):
        a, b = window_var(W, comps, 10), cv2_first_order(W, comps)
        assert abs(a / b - 1) < 0.05, (W, a, b)
    # 2. Poisson baseline
    n = 200000
    Ds = [disp(rng.poisson(BIN_BP * 0.012 * np.ones(n)), 100)[0] for _ in range(4)]
    assert abs(np.mean(Ds) - 1.0) < 0.05, Ds
    # 3. simulation reproduces the exact expectation (20 Mb, 2 components)
    comps = [(0.2, 5e3), (0.15, 2e5)]
    for W in (1e3, 1e4, 1e5):
        Ds = []
        for _ in range(8):
            R = rate_field(n, comps, rng)
            Ds.append(disp(rng.poisson(BIN_BP * 0.012 * R), int(W / BIN_BP))[0])
        e = expected_sample_D(W, 0.012, comps, n)
        assert abs((np.mean(Ds) - 1) / (e - 1) - 1) < 0.15, (W, np.mean(Ds), e)
    # 4. short-ell component gives a W-independent excess 2 d sigma^2 ell (W >> ell)
    c1 = [(0.2, 200.0)]
    e1, e2 = (band_one(W, 0.012, c1) for W in (1e5, 1e6))
    assert abs(e1 - e2) / e1 < 0.02 and abs(e1 - 2 * 0.012 * math.log1p(0.04) * 200) / e1 < 0.15, (e1, e2)
    # 5. scoring rule and readings
    assert classify(400, 5, 100) == "DAY" and classify(200, 5, 100) == "MARGINAL"
    assert classify(80, 5, 100) == "CRITIC" and classify(2, 5, 100) == "BELOW"
    ds, dp = tree_struct()
    assert 6.0 <= ds <= 12.0, ds
    # 6. split dispersion is ~1 under a shared field, large under H-only blocks
    H, C, _ = sim_two_lineage(n, [(0.2, 1e5)], [], 0.0051, 0.0057, rng)
    k = n // 1000
    h, c = H[: k * 1000].reshape(k, 1000).sum(1), C[: k * 1000].reshape(k, 1000).sum(1)
    assert split_phi(h, c) < 1.3, split_phi(h, c)
    H, C, _ = sim_two_lineage(n, [(0.2, 1e5)], [], 0.0051, 0.0057, rng, blocks=(1e5, 1.0, 0.05))
    h, c = H[: k * 1000].reshape(k, 1000).sum(1), C[: k * 1000].reshape(k, 1000).sum(1)
    assert split_phi(h, c) > 3.0, split_phi(h, c)
    # 7. real-data arm on a tiny synthetic npz in the fm_mesa_replication layout (uniform Poisson -> phi ~ 1)
    sys.path.insert(0, HERE)
    import fm_mesa_replication as fm
    d = tempfile.mkdtemp()
    data = {}
    for ch in ("chr1", "chr2"):
        a = np.zeros((4000, 8, fm.NF), np.uint16)
        a[:, 0, 0] = 1000
        for j, L in enumerate(fm.FIELDS):
            if L in ("H", "C", "B", "G", "DHC", "hh", "gc"):
                lam = {"H": 5.1, "C": 5.7, "B": 5.7, "G": 7.7, "DHC": 13.7, "hh": 1.0, "gc": 400.0}[L]
                a[:, 0, j] = rng.poisson(lam, 4000)
        data["chr_" + ch] = a
    p = os.path.join(d, "t.npz")
    np.savez_compressed(p, **data, meta=json.dumps(dict(fields=fm.FIELDS, bin=1000, sizes={}, blocks=0,
                                                        classes="rep + 2*cpg + 4*dup")))
    r = realdata(p, os.path.join(d, "r.json"))
    for key in ("F0|1kb", "F0|10kb", "F0|100kb"):
        assert 0.7 < r["grid"][key]["H"]["phi"] < 1.4, (key, r["grid"][key]["H"]["phi"])
    print("selftest ok")


def band_one(W, d, comps):
    return W * d * window_var(W, comps)


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] == "selftest":
        selftest()
    elif a[0] == "analytic":
        analytic(a[1], a[2] if len(a) > 2 else None)
    elif a[0] == "simulate":
        simulate(a[1], *(float(x) if i == 0 else int(x) for i, x in enumerate(a[2:])))
    elif a[0] == "realdata":
        realdata(a[1], a[2])
    elif a[0] == "score":
        import argparse
        ap = argparse.ArgumentParser()
        ap.add_argument("--W", type=float, required=True)
        ap.add_argument("--value", type=float, required=True)
        ap.add_argument("--reading", default="R1", choices=("R1", "R1b", "R1x", "R2"))
        ap.add_argument("--unit", default="DHC")
        ap.add_argument("--masked", action="store_true")
        o = ap.parse_args(a[1:])
        score(o.W, o.value, o.reading, o.unit, o.masked)
    else:
        sys.exit(__doc__)

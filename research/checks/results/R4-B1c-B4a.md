# R4 results: B1c (sourced Ne histories) and B4a (two-lineage divergence with ancestral polymorphism)

Scripts (run as `research/.venv/bin/python -I research/checks/<script>.py`, rerun with 3 worker processes, burn-in 20 N_sim): `b1c_ne_history.py` (seed 20261008), `b4a_two_lineage_ils.py` (seed 20261009), helpers in `wf2.py` (wf.py untouched). Pre-registered predictions are in each script docstring (copied from the claim files). Raw outputs are the tables below, verbatim from the runs.

## 0. Sourced Ne inputs

### 0.1 Yoo 2025 (already in parameters.yaml, verified in ledger)
Human-chimp-bonobo ancestor Ne = 198,000; human-chimp-gorilla ancestor Ne = 132,000. Split 5.5-6.3 My.

### 0.2 Prado-Martinez et al. 2013, Nature 499:471 (sources/raw/sources/manual/PradoMartinez2013.txt, PMC author manuscript)
PSMC curves are shown only graphically (Fig. 3); the main text gives no numeric PSMC trajectory, and the per-method estimates are in Supplementary Table S5, which I could not retrieve (a web search found only the abstract and mirrors). So the numeric PSMC history is NOT extracted. What the text does give (locators = line numbers in the .txt):
- L197-200: "PSMC analyses of historical Ne (Figure 3) suggests that the ancestral Pan lineage had the largest effective population size of all lineages >3 million years ago (Mya), after which the ancestral bonobo-chimpanzee population experienced a dramatic decline."
- L200: "Both PSMC and ABC analyses support a model of subsequent increase in chimpanzee Ne starting ~1 Mya"
- L323-325: "The PSMC analysis indicates a temporal order to changes in ancestral effective population sizes over the last two million years, previous to which the Pan genus suffered a dramatic population collapse."
- L267-268: "This pattern is consistent with a recent reduction in effective population size20, clearly visible in the PSMC analysis for both species (Figure 3)."
- Fig. 2 caption (L724-726): "Time is estimated using a single mutation rate (μ) of 1·10−9 mut/(bp·year). The ancestral and current effective population sizes are also estimated using this mutation rate."
- Fig. 3 caption (L765-771): upper x-axis "assuming a mutation rate ranging from 10−9 to 5·10−10 per site per year."
- Table 1 (L800-818), column "Ne (10-3)", footnote d (L836): "Calculated from Θw. μ = 1e-9 - 0.5e-9 mut·bp-1·yr-1 and g = 25 for Homo and Pan". Values (thousands): Humans 13.1-16.2; Non-African 9.7-19.5; African 13.9-27.9; Common chimpanzees 30.9-61.8 (Nigerian-Cameroon 18.5-37.0, Eastern 19.7-39.5, Central 24.4-48.7, Western 9.8-19.5); Bonobos 11.9-23.8.
- Source inconsistency to note: the "Humans" row (13.1-16.2) is not a 2x range like every other row; flagged, not resolved.
- Mutation-rate dependence: PM2013 Ne scale as 1/mu. Their 1e-9/yr = 2.5e-8/gen (25 y), about 2x the pedigree 1.2e-8/gen, so under the pedigree rate their Ne would be about 2x larger. The Table 1 ranges bracket that factor of 2.
- No numeric human-lineage PSMC trajectory since the split is available from this source. The human histories below are therefore scenarios bracketed by sourced endpoints, not extracted curves.

### 0.3 Textbook/long-term human Ne (proposed parameters.yaml entry; not edited there)
```yaml
population:
  Ne_modern_human_longterm:
    takahata_1995: {value: 1.0e4, note: "ML on unlinked autosomal sequences; Late Pleistocene; 'no sign of population expansion'; human-lineage Ne >4.6 My ago ~10x modern (~1e5)", source: "Takahata, Satta & Klein 1995, Theor Popul Biol 48:198-221, doi 10.1006/tpbi.1995.1026", verified: partial}
    charlesworth_2009: {value: [1.0e4, 2.0e4], note: "review summary of sequence-variability estimates", source: "Charlesworth 2009, Nat Rev Genet 10:195", verified: false}
    prado_martinez_2013_table1: {value: [1.31e4, 1.62e4], note: "Theta_w-based, mu 1e-9..0.5e-9/yr, g=25; Africans 1.39e4-2.79e4", source: PradoMartinez2013, verified: true}
```
Quotes: Takahata 1995 abstract (via search snippet and a fetched summary, both of the publisher/PSU record; the abstract PDF itself not read): "Available sequences at human autosomal loci indicate Ne= 10,000 in the Late Pleistocene, a figure concordant with the results obtained from mitochondrial DNA sequence and allele-frequency data analysis, and there is no indication of population expansion." and "the effective population size of humans more than 4.6 my ago is nearly 10 times larger than Ne of modern humans." Mark `verified: partial` until the abstract is read directly. Note Takahata's divergence time (4.6 My) differs from the 6.3 My used here.

## 1. B1c: per-lineage fixed substitutions K vs U*T (rerun, burn-in 20 N_sim)

Setup: infinite-sites unlinked neutral WF; ancestral population at equilibrium (burn-in **20** N_anc_sim, was 10); split into a lineage with sourced-range Ne(t); window T = 252,000 generations; K = all alleles that fix in the lineage population during the window; reported as K/(U T). 150 replicates, SE of mean. Ancestral Ne = Yoo values. Scaling (E4): N_anc_sim = 1000, theta = 800 held fixed.

**Prediction (pre-registered):** contraction from >=1.3e5 to ~1e4 gives excess (K/UT > 1); deficit only if Ne rises by dN with 4dN a sizeable fraction of T.

**What K is.** The excess counts alleles that fix *in a lineage*, including ancestral alleles that fix in both lineages (shared, not a human-chimp difference). Per-lineage K is therefore not a difference count; the observable is B4a.

### 1.1 Scaling validation and controls (rerun)
| check | result |
|---|---|
| H1 (1.98e5 -> 1e4) at N_anc_sim 500 / 1000 / 2000 | 4.004+-0.017 / 3.973+-0.018 / 4.003+-0.013 (analytic 1+4dN/T = 3.984) |
| evolve() vs wf.substitutions_demog (H1, N_anc_sim 500; the latter now also 20N burn-in) | 4.004+-0.017 vs 3.970+-0.025 |
| constant control, N_anc_sim 500 | 1.000+-0.009 |
| constant control in main runs | 1.000+-0.005 (HCB), 0.996+-0.004 (HCG) |

The earlier 1.2-1.6% shortfall (controls 0.984-0.988) was a burn-in artefact (10 N_sim leaves the ancestral diversity about 1-2% short of equilibrium); with 20 N_sim controls are 1.000. It is no longer an unexplained caveat.

### 1.2 Results, ancestral Ne 1.98e5 (Yoo HCB)
| scenario | K/UT +- SE | from ancestral alleles | from new mutations | telescoped analytic | verdict |
|---|---|---|---|---|---|
| H0 const at ancestral (control) | 1.000 +- 0.005 | 0.998 | 0.002 | 1.000 | none |
| H1 step to 1.0e4 at split (textbook 1e4) | 3.986 +- 0.012 | 3.143 | 0.844 | 3.984 | excess |
| H2 step to 1.5e4 (PM2013 Table1 humans 13.1-16.2k) | 3.904 +- 0.011 | 3.138 | 0.765 | 3.905 | excess |
| H3 Takahata-like: 1e5 first half, then 1e4 | 3.975 +- 0.011 | 3.132 | 0.842 | 3.984 | excess |
| H4 1e4 then growth to 5e4 in last 2% (sensitivity, unsourced) | 3.959 +- 0.010 | 3.135 | 0.824 | 3.349 | excess |

| scenario | K/UT +- SE | from ancestral alleles | from new mutations | telescoped analytic | verdict |
|---|---|---|---|---|---|
| C0 const at ancestral (control) | 1.000 +- 0.005 | 0.998 | 0.002 | 1.000 | none |
| C1a step to 3.09e4 (PM2013 Table1 common chimp low) | 3.589 +- 0.010 | 3.068 | 0.521 | 3.652 | excess |
| C1b step to 6.18e4 (PM2013 Table1 common chimp high) | 2.739 +- 0.009 | 2.526 | 0.213 | 3.162 | excess |
| C2 PSMC-text: anc to 3 Mya, 1.8e4 to 1 Mya, 4.6e4 last 1 My | 3.466 +- 0.009 | 2.903 | 0.564 | 3.413 | excess |
| C3 bonobo-like constant 1.785e4 (PM2013 Table1 bonobo mid) | 3.861 +- 0.011 | 3.134 | 0.726 | 3.860 | excess |

### 1.3 Results, ancestral Ne 1.32e5 (Yoo HCG)
| scenario | K/UT +- SE | from ancestral alleles | from new mutations | telescoped analytic | verdict |
|---|---|---|---|---|---|
| H0 const at ancestral (control) | 0.996 +- 0.004 | 0.977 | 0.019 | 1.000 | none |
| H1 step to 1.0e4 at split (textbook 1e4) | 2.920 +- 0.007 | 2.080 | 0.839 | 2.937 | excess |
| H2 step to 1.5e4 (PM2013 Table1 humans 13.1-16.2k) | 2.858 +- 0.007 | 2.095 | 0.763 | 2.857 | excess |
| H3 Takahata-like: 1e5 first half, then 1e4 | 2.929 +- 0.007 | 2.083 | 0.846 | 2.937 | excess |
| H4 1e4 then growth to 5e4 in last 2% (sensitivity, unsourced) | 2.915 +- 0.007 | 2.091 | 0.824 | 2.302 | excess |

| scenario | K/UT +- SE | from ancestral alleles | from new mutations | telescoped analytic | verdict |
|---|---|---|---|---|---|
| C0 const at ancestral (control) | 0.996 +- 0.004 | 0.977 | 0.019 | 1.000 | none |
| C1a step to 3.09e4 (PM2013 Table1 common chimp low) | 2.561 +- 0.008 | 2.036 | 0.525 | 2.605 | excess |
| C1b step to 6.18e4 (PM2013 Table1 common chimp high) | 1.898 +- 0.006 | 1.689 | 0.208 | 2.114 | excess |
| C2 PSMC-text: anc to 3 Mya, 1.8e4 to 1 Mya, 4.6e4 last 1 My | 2.523 +- 0.007 | 1.954 | 0.569 | 2.365 | excess |
| C3 bonobo-like constant 1.785e4 (PM2013 Table1 bonobo mid) | 2.801 +- 0.007 | 2.081 | 0.720 | 2.812 | excess |

(In H4 and C1b/C2 the multi-step telescoped analytic is invalid when a segment is shorter than ~4N; simulation is the number to use.)

### 1.4 Reading
- Every history built as a step (or two) from the Yoo ancestral Ne down to a modern Ne of 1e4-6e4 gives an excess, 1.9x to 4.0x U T. The single-step runs now match the analytic 1+4(N_anc-N_end)/T to within about 0.5% (H1 3.986 vs 3.984; H2 3.904 vs 3.905). This is the B1b telescoping identity restated under step histories (excess follows from ancestral Ne >> descendant Ne), not an independent empirical finding. Yoo's Ne is an average over the ancestor's existence, not necessarily the size at the split, and no gradual human-lineage decline or sustained expansion was sourced (PSMC trajectory not extracted).
- A deficit would need lineage Ne above the ancestral value for a sustained time; nothing sourced here does that.
- Per-lineage K is dominated by ancestral alleles fixing in the lineage (3.14 of 3.99 in H1/HCB). These include alleles that fix in both lineages, so K is not a difference count.
- The new-mutation column (0.84 in H1/HCB and HCG; 0.77 in H2) confirms Day's (T-4Ne)/T = 0.84 for Ne = 1e4 as correct accounting for post-split mutations from an empty start. The ancestral-allele term is what an empty-start count omits.

## 2. B4a: two-lineage divergence with ancestral polymorphism (rerun, burn-in 20 N_sim)

Setup: ancestral population at equilibrium (burn-in 20 N_sim), cloned into two lineages with independent drift and mutation. Exact expected pairwise divergence d between one haplotype from each lineage; fixed differences = sites fixed for different alleles; poly-but-diff = d minus fixed. Per-site values in percent, mu = 1.2e-8. Ne_anc in {1e4, 3e4, 1.32e5, 1.98e5}; lineages A: both 1e4; B: human 1e4 / chimp 4.6e4; C: both stay at Ne_anc. msprime column = 2 mu E[TMRCA] (coalescent baseline). SEs reflect ~1e7 unlinked loci; real-genome SEs larger (no linkage).

**Prediction (pre-registered):** E[d] = 2 mu T + 4 Ne_anc mu; Day: ancestral term negligible and observable lowered by the empty-pipe correction.

Selected rows, T = 252,000:
| Ne_anc | config | d sim (%) | 2muT+theta (%) | d msprime (%) | fixed (%) | poly-but-diff (%) | poly-but-diff / d | Day 2mu(T-4Ne_lin) (%) |
|---|---|---|---|---|---|---|---|---|
| 1.0e4 | A | 0.652 | 0.653 | 0.653 | 0.556 | 0.096 | 15% | 0.509 |
| 1.32e5 | A | 1.238 | 1.238 | 1.239 | 1.142 | 0.096 | 8% | 0.509 |
| 1.32e5 | B | 1.237 | 1.238 | 1.240 | 0.930 | 0.307 | 25% | 0.336 |
| 1.98e5 | A | 1.553 | 1.555 | 1.556 | 1.459 | 0.095 | 6% | 0.509 |
| 1.98e5 | B | 1.557 | 1.555 | 1.558 | 1.220 | 0.337 | 22% | 0.336 |

Full output (all Ne_anc, T = 50k/100k/252k, configs A/B/C):
## Ne_anc = 1e+04  (N_anc_sim=500, f=20, reps=80); per-site values in %
| config | T | d sim | 2muT+theta | d msprime | fixed diffs | poly-but-diff | Day 2mu(T-4Ne_lin) | d - 2muT | theta_anc |
|---|---|---|---|---|---|---|---|---|---|
| A both 1e4 | 50000 | 0.168+-0.000 | 0.168 | 0.168+-0.000 | 0.073+-0.000 | 0.095+-0.000 | 0.024 | 0.048 | 0.048 |
| A both 1e4 | 100000 | 0.288+-0.000 | 0.288 | 0.288+-0.000 | 0.192+-0.000 | 0.096+-0.000 | 0.144 | 0.048 | 0.048 |
| A both 1e4 | 252000 | 0.652+-0.001 | 0.653 | 0.653+-0.000 | 0.556+-0.001 | 0.096+-0.000 | 0.509 | 0.047 | 0.048 |
| B H 1e4 / C 4.6e4 | 50000 | 0.168+-0.000 | 0.168 | 0.168+-0.000 | 0.029+-0.000 | 0.139+-0.000 | 0.000 | 0.048 | 0.048 |
| B H 1e4 / C 4.6e4 | 100000 | 0.288+-0.000 | 0.288 | 0.288+-0.000 | 0.102+-0.000 | 0.186+-0.000 | 0.000 | 0.048 | 0.048 |
| B H 1e4 / C 4.6e4 | 252000 | 0.652+-0.001 | 0.653 | 0.653+-0.000 | 0.400+-0.001 | 0.252+-0.000 | 0.336 | 0.048 | 0.048 |
| C both = Ne_anc | 50000 | 0.168+-0.000 | 0.168 | 0.168+-0.000 | 0.073+-0.000 | 0.095+-0.000 | 0.024 | 0.048 | 0.048 |
| C both = Ne_anc | 100000 | 0.288+-0.000 | 0.288 | 0.288+-0.000 | 0.192+-0.000 | 0.096+-0.000 | 0.144 | 0.048 | 0.048 |
| C both = Ne_anc | 252000 | 0.652+-0.001 | 0.653 | 0.653+-0.000 | 0.556+-0.001 | 0.096+-0.000 | 0.509 | 0.047 | 0.048 |

## Ne_anc = 3e+04  (N_anc_sim=1000, f=30, reps=150); per-site values in %
| config | T | d sim | 2muT+theta | d msprime | fixed diffs | poly-but-diff | Day 2mu(T-4Ne_lin) | d - 2muT | theta_anc |
|---|---|---|---|---|---|---|---|---|---|
| A both 1e4 | 50000 | 0.264+-0.001 | 0.264 | 0.265+-0.001 | 0.147+-0.000 | 0.117+-0.000 | 0.024 | 0.144 | 0.144 |
| A both 1e4 | 100000 | 0.383+-0.001 | 0.384 | 0.384+-0.001 | 0.286+-0.001 | 0.097+-0.000 | 0.144 | 0.143 | 0.144 |
| A both 1e4 | 252000 | 0.749+-0.001 | 0.749 | 0.749+-0.001 | 0.653+-0.001 | 0.095+-0.000 | 0.509 | 0.144 | 0.144 |
| B H 1e4 / C 4.6e4 | 50000 | 0.263+-0.001 | 0.264 | 0.264+-0.001 | 0.050+-0.000 | 0.213+-0.000 | 0.000 | 0.143 | 0.144 |
| B H 1e4 / C 4.6e4 | 100000 | 0.383+-0.001 | 0.384 | 0.385+-0.001 | 0.151+-0.000 | 0.232+-0.000 | 0.000 | 0.143 | 0.144 |
| B H 1e4 / C 4.6e4 | 252000 | 0.746+-0.001 | 0.749 | 0.749+-0.001 | 0.486+-0.001 | 0.260+-0.000 | 0.336 | 0.141 | 0.144 |
| C both = Ne_anc | 50000 | 0.264+-0.000 | 0.264 | 0.264+-0.001 | 0.016+-0.000 | 0.248+-0.000 | 0.000 | 0.144 | 0.144 |
| C both = Ne_anc | 100000 | 0.384+-0.001 | 0.384 | 0.383+-0.001 | 0.104+-0.000 | 0.280+-0.000 | 0.000 | 0.144 | 0.144 |
| C both = Ne_anc | 252000 | 0.750+-0.001 | 0.749 | 0.748+-0.001 | 0.462+-0.001 | 0.288+-0.000 | 0.317 | 0.145 | 0.144 |

## Ne_anc = 1.32e+05  (N_anc_sim=1000, f=132, reps=150); per-site values in %
| config | T | d sim | 2muT+theta | d msprime | fixed diffs | poly-but-diff | Day 2mu(T-4Ne_lin) | d - 2muT | theta_anc |
|---|---|---|---|---|---|---|---|---|---|
| A both 1e4 | 50000 | 0.753+-0.002 | 0.754 | 0.757+-0.005 | 0.523+-0.002 | 0.229+-0.001 | 0.024 | 0.633 | 0.634 |
| A both 1e4 | 100000 | 0.873+-0.002 | 0.874 | 0.872+-0.004 | 0.768+-0.002 | 0.106+-0.001 | 0.144 | 0.633 | 0.634 |
| A both 1e4 | 252000 | 1.238+-0.003 | 1.238 | 1.239+-0.004 | 1.142+-0.003 | 0.096+-0.001 | 0.509 | 0.633 | 0.634 |
| B H 1e4 / C 4.6e4 | 50000 | 0.752+-0.002 | 0.754 | 0.754+-0.004 | 0.158+-0.001 | 0.594+-0.001 | 0.000 | 0.632 | 0.634 |
| B H 1e4 / C 4.6e4 | 100000 | 0.873+-0.002 | 0.874 | 0.876+-0.004 | 0.407+-0.001 | 0.466+-0.001 | 0.000 | 0.633 | 0.634 |
| B H 1e4 / C 4.6e4 | 252000 | 1.237+-0.002 | 1.238 | 1.240+-0.004 | 0.930+-0.002 | 0.307+-0.001 | 0.336 | 0.632 | 0.634 |
| C both = Ne_anc | 50000 | 0.752+-0.001 | 0.754 | 0.751+-0.004 | 0.000+-0.000 | 0.752+-0.001 | 0.000 | 0.632 | 0.634 |
| C both = Ne_anc | 100000 | 0.871+-0.001 | 0.874 | 0.876+-0.004 | 0.001+-0.000 | 0.870+-0.001 | 0.000 | 0.631 | 0.634 |
| C both = Ne_anc | 252000 | 1.236+-0.002 | 1.238 | 1.236+-0.004 | 0.110+-0.001 | 1.126+-0.002 | 0.000 | 0.631 | 0.634 |

## Ne_anc = 1.98e+05  (N_anc_sim=1000, f=198, reps=150); per-site values in %
| config | T | d sim | 2muT+theta | d msprime | fixed diffs | poly-but-diff | Day 2mu(T-4Ne_lin) | d - 2muT | theta_anc |
|---|---|---|---|---|---|---|---|---|---|
| A both 1e4 | 50000 | 1.070+-0.003 | 1.070 | 1.075+-0.007 | 0.764+-0.003 | 0.305+-0.001 | 0.024 | 0.950 | 0.950 |
| A both 1e4 | 100000 | 1.188+-0.003 | 1.190 | 1.188+-0.007 | 1.075+-0.003 | 0.113+-0.001 | 0.144 | 0.948 | 0.950 |
| A both 1e4 | 252000 | 1.553+-0.003 | 1.555 | 1.556+-0.007 | 1.459+-0.003 | 0.095+-0.001 | 0.509 | 0.949 | 0.950 |
| B H 1e4 / C 4.6e4 | 50000 | 1.073+-0.003 | 1.070 | 1.072+-0.007 | 0.233+-0.001 | 0.839+-0.002 | 0.000 | 0.953 | 0.950 |
| B H 1e4 / C 4.6e4 | 100000 | 1.191+-0.003 | 1.190 | 1.194+-0.007 | 0.576+-0.002 | 0.616+-0.002 | 0.000 | 0.951 | 0.950 |
| B H 1e4 / C 4.6e4 | 252000 | 1.557+-0.003 | 1.555 | 1.558+-0.007 | 1.220+-0.003 | 0.337+-0.001 | 0.336 | 0.952 | 0.950 |
| C both = Ne_anc | 50000 | 1.068+-0.002 | 1.070 | 1.081+-0.007 | 0.000+-0.000 | 1.068+-0.002 | 0.000 | 0.948 | 0.950 |
| C both = Ne_anc | 100000 | 1.188+-0.002 | 1.190 | 1.187+-0.007 | 0.000+-0.000 | 1.188+-0.002 | 0.000 | 0.948 | 0.950 |
| C both = Ne_anc | 252000 | 1.551+-0.002 | 1.555 | 1.557+-0.007 | 0.037+-0.001 | 1.515+-0.002 | 0.000 | 0.946 | 0.950 |


d - 2muT equals theta_anc to within about 0.3% in every row (previous 0.4-1.3% shortfall gone), and msprime agrees within SE.

### 2.1 Comparison with observed human-chimp numbers (CSAC 2005: 1.23% total, fixed <= 1.06%), mu = 1.2e-8, T = 252,000
- **Relevant node: human-chimp-bonobo ancestor, Ne_anc = 1.98e5** (the population that split into the human and Pan lineages). It gives d = 1.55-1.56%, about 25% above the observed 1.23%; fixed differences 1.22-1.46%, above the <= 1.06% bound. The 1.32e5 value (human-chimp-gorilla ancestor, the older node) reproduces 1.23% but is the wrong node for this split and is not used as the verdict.
- **The match is a 3-parameter fit** (mu, T, Ne_anc): the data constrain only 2muT + 4 Ne_anc mu. At Day's Ne = 1e4, d = 0.65%, about half the observed. Whether the overshoot at 1.98e5 reflects Yoo's Ne being a lifetime average rather than Ne at the split, or uncertainty in mu and T (5.5-8 My; mu 1.1-1.5e-8), is not resolved here.
- **Yoo's Ne depends on Yoo's own mu.** theta = 4 Ne mu is what the data fix, so Ne rescales as Ne' = Ne_Yoo * mu_Yoo / 1.2e-8. I could not find Yoo's mu or generation time in docs/research/sources/quotes-literature.md or parameters.yaml (only the Ne values 1.98e5/1.32e5 and the 5.5-6.3 My split are recorded), so the rescaled Ne_anc is not computed. For illustration only (hypothetical, not Yoo's value): if mu_Yoo were 2.5e-8/gen (PM2013's 1e-9/yr x 25 y), Ne_anc at mu = 1.2e-8 would be about 9.5e4 and d = 0.605 + 0.456 = 1.06%, below observed. The sign of the overshoot therefore depends on an unrecorded input.
- **CSAC polymorphism share.** CSAC's 14-22% is the share of the observed divergence that is still polymorphic, so the comparable column is poly-but-diff / d, not theta_anc / d. Config A gives 6-8% at the Yoo nodes, and config B (human 1e4 / chimp 4.6e4) gives 22-25% (1.32e5: 0.307/1.237 = 25%; 1.98e5: 0.337/1.557 = 22%), bracketing and slightly above CSAC's 14-22%. This is consistent, with no tension. The ancestral share of d (theta_anc/d) is model-dependent and is not quoted as a result.
- **Day's formula on the observable.** His 2mu(T-4Ne) = 0.51% (Ne = 1e4) is below the simulated fixed differences (0.56-1.46%), because ancestral alleles also sort into fixed differences. Raw pairwise divergence d is not reduced by the empty-pipe term: d - 2muT = theta_anc in every row, whatever the lineage Ne.

## 3. Suggested verdicts (three-verdict form; for the maintainers to adopt)

| claim | (a) internal | (b) fidelity | (c) external |
|---|---|---|---|
| B1c (Day: pipeline empty) | holds as arithmetic for an empty start (B1); "full but short" (B1d) conflicts with it | n/a (Yoo Ne as in ledger; PM2013 PSMC numbers not extractable) | contradicted for step histories from Yoo's ancestral Ne: lineage K is 1.9-4.0x U T; this is the B1b telescoping identity, and the human trajectory is a scenario. Day's (T-4Ne)/T is confirmed for the new-mutation component (0.84) |
| B4a (d = 2muT + theta_anc) | holds (forward simulation matches within ~0.3%, msprime agrees) | holds for CSAC/Yoo quotes; CSAC polymorphic share 14-22% matches poly-but-diff (config B 22-25%) | at the relevant node (1.98e5) the formula overshoots observed 1.23% by ~25%; at Day's Ne = 1e4 it gives about half. A 3-parameter (mu, T, Ne_anc) fit; Yoo's mu not recorded so Ne_anc rescaling is open |
| B1 (finite-time count differs; Day) | holds | n/a | contested to contradicted for the human-chimp case: deficit exists only for new-mutation accounting from an empty start |
| B6 (Mansfield: pipe full) | holds | n/a | supported: equilibrium start gives K/UT = 1.000 for constant Ne; d = 2muT + theta_anc within ~0.3% |

## 4. Caveats
- Unlinked-sites model. No linkage, selection, gene flow, recombination or structure.
- Human-lineage Ne histories are scenarios bounded by sourced endpoints, not extracted PSMC curves (PM2013 Table S5 not retrieved). PM2013 Ne depends on mu (about 2x under the pedigree rate).
- Yoo's mu and generation time not recorded in the repo.
- ILS gene-tree discordance fraction and outgroup lineage not run.
- Takahata 1995 and Charlesworth 2009 numbers come from search snippets/summaries.
- Pedigree mu = 1.2e-8 and 25 y/gen are parameters.yaml values (Kong2012 verified: false).
- N_end in `schedule` is rounded (e.g. 1e4/198 -> 51), shifting telescoped analytics by under 0.5%.

## Review corrections applied
1. Burn-in raised from 10 N_sim to 20 N_sim in `b1c_ne_history.py` (including the wf.substitutions_demog cross-check) and `b4a_two_lineage_ils.py`; both rerun (Pool(3)); all tables replaced. Constant-Ne controls now 1.000 (was 0.984-0.988); "unexplained O(1/N_sim) bias" caveat removed.
2. B4a: CSAC 14-22% compared with poly-but-diff / d; "tension" paragraph and T = 400-440k alternative deleted; the 51-61% ancestral share no longer quoted as a result.
3. B4a verdict moved to the human-chimp-bonobo node (1.98e5, overshoot ~25%); restated as a 3-parameter fit; Yoo's mu looked for (not found) and the rescaling Ne' = Ne_Yoo*mu_Yoo/1.2e-8 stated with a hypothetical illustration.
4. B1c: stated that K counts alleles fixing in a lineage (including those fixing in both), so it is not a difference count; new-mutation column (0.84) confirms Day's (T-4Ne)/T; framing changed to "excess follows from ancestral Ne >> descendant Ne under step histories".
5. Review item "docstring/claim file say ancestral burn-in 8Ne": checked, and neither `b4a_two_lineage_ils.py` nor `claims/B4a-two-lineage-divergence-with-ils.md` contains an 8Ne remark (the review's MINOR was mislabelled). The code uses 20 N_sim (`burn_in(n, U, 20 * n, rng)`); nothing to edit.

## 5. Sources used
- docs/research/parameters.yaml (Yoo 2025 Ne_anc; mu; T)
- sources/raw/sources/manual/PradoMartinez2013.txt (Nature 499:471-475, doi 10.1038/nature12228)
- Takahata, Satta & Klein 1995, Theor Popul Biol 48:198-221 (https://pure.psu.edu/en/publications/divergence-time-and-population-size-in-the-lineage-leading-to-mod/)
- Charlesworth 2009, Nat Rev Genet 10:195 (via search summary)
- CSAC 2005 figures as recorded in parameters.yaml

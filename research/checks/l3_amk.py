"""R4 L3: human-lineage alpha by the asymptotic McDonald-Kreitman test, against the A2e flip (alpha* about 1%).

Brief: research/checks/briefs/L3-analyst.md (lead Big Sim, 2026-10-13).  Queue item L3 (QUEUE.md, "alpha bound
from MK with demographic correction"; the Uricchio blocker named there was cleared on 2026-10-11, see the brief).
Target: A2e (docs/research/claims/A2e-ltee-as-ceiling.md), `load_bearing: true`.  Tier: three reviews
(correctness, steelman-day, steelman-critic), one after another (D-22, D-23).

PRE-REGISTRATION.  Everything in this docstring was written before any polymorphism or divergence count for L3
was computed.  Disclosure (for PREREG-STATUS; label expected: blind for the measured statistic, with predictions
informed by published values):
  * Seen before writing: R4-A2e-alpha.md (all of it that bears on A2e, incl. the Uricchio addendum, whose
    numbers include the aMK baseline 0.076 on the same 661 African samples and the same hg19/panTro4/ponAbe2
    parsimony divergence that L3 uses); the A2e claim file's external field (now `pending`, D-21); the method
    paper Haller & Messer 2017 (full text) and the asymptoticMK R source (read, not executed); the first
    ~300-400 kB of the two data files (header lines and the first ~22,800 VCF records of chr1; the first ~15,000
    lines of the alignment file, i.e. a few transcripts on chr1), opened only to confirm formats (INFO fields
    AA and AFR_AF; header layout; strand convention).  No count, frequency spectrum or alpha was computed from
    them.  The 1000 Genomes sample panel was tabulated by super-population (AFR 661, EUR 503; a design input).
  * Background from training: naive MK estimates on human data are commonly near zero or negative, and
    published bias-corrected human alphas are of order 0.1.  The audit's numeric predictions (Q1-Q9) lean on
    this and on Uricchio's 0.076; they are labelled as such.  No number from memory is used as an input.

WHY THIS CHECK, AND WHERE IT IS DECIDED
  R4-A2e found that A2e, per generation and adaptive-only, is equivalent to "the human lineage fixed at most about
  191 adaptive substitutions since the CHLCA".  Mapped onto coding sequence that is an adaptive fraction
  alpha* of about 1% of human-lineage nonsynonymous substitutions (0.65%-1.75% across the audit's denominators;
  R4-A2e-alpha.md).  The external verdict therefore turns on one empirical number: is human-lineage coding alpha
  above about 1%, with an interval that excludes it?  The audit's earlier evidence is published estimates
  (Boyko 2008, Uricchio 2019).  L3 computes one itself, from public data, with the asymptotic MK method
  (Messer & Petrov 2013, as implemented in asymptoticMK, Haller & Messer 2017), and reports it beside the
  standard MK value so the size of the correction is visible.  What decides the result: the polymorphism
  frequency spectrum of nonsynonymous versus synonymous SNPs at high derived-allele frequency, relative to
  human-specific divergence.  Everything that could be chosen after seeing it (data, gene set, cutoffs, bins,
  fit form, interval, thresholds, sensitivity rows, verdict moves) is fixed below.

  Which Uricchio reading L3 speaks to (brief): the ANY-EFFECT-SIZE per-generation count reading, the reading of
  A2e's formal statement.  aMK estimates the fraction of all nonsynonymous substitutions that were adaptive; it
  does not split them by effect size.  L3 licenses NO move on the strong-effect-only or fitness-weighted
  readings, in any band.

TARGET QUOTES (verbatim, from docs/research/sources/quotes-day.md; RH tag dialectic for all three)
  Q138 (MITTENS 3.0 s8.6, PDF p.15, Z23003785): "The objection implicitly claims that humans can fix mutations
    faster per generation than bacteria under ideal conditions."
  Q130 core (s2, PDF p.4; split tag, ledger RH-4; only this clause is scored): "It is an unattainable ceiling,
    the absolute best-case scenario"
  Q139 threshold (s7.3, PDF p.13): "At 1,322 gen/fix (non-mutator): 191 achievable."
  Neither side states a human alpha.  The brief summarises Day's position as "K is not derivable from first
  principles" (Z23020792) and the critics' as "most differences are neutral", with no number; no verbatim quote
  for either summary was located in the quotes files at registration, so neither is scored (rule S).  The side
  predictions below are the audit's reading of what each side's position needs.

METHOD SOURCES (verbatim, checked by `smoke` and `main` as substrings of the local text; rule 2)
  Haller & Messer 2017, G3 7:1569 (PMC5427504, Europe PMC fullTextXML fetched 2026-10-13 to
  sources/raw/l3-hallermesser-2026-10-13/hm.xml, sha256 20527f3b52772a0ed9898dda7e92818c4db39d14bd419b06ade09d38ce2b07d9;
  quotes are substrings of the tag-stripped, whitespace-normalised text, see `norm_xml_text`):
    HM1 (Methods, fitting): "The first function is exponential, of the form α fit ( x ) = a + b exp(− cx )"
    HM2 (same): "If the exponential fit failed to converge, then the linear model is chosen; if both fits
      succeeded, then the better model is chosen using the Akaike Information Criterion (AIC)."
    HM3 (same): "by evaluating the fitted function α fit ( x ) at x = 1; this is the primary result of the test"
    HM4 (same): "For the exponential model, this is done using Monte Carlo simulation based upon the fitted model"
    HM5 (Methods, input): "This frequency cutoff is set to [0.1, 0.9] by default"
    HM6 (Introduction, the demographic correction): "any biases due to demography or linked selection that affect
      the SFS in the test and reference regions in the same way will effectively cancel out"
    HM7 (Results, the known residual bias): "The asymptotic MK test may still have a tendency toward
      underestimation as well, but errors are much smaller."
    HM8 (Results, baseline): "The asymptotic MK estimate provided by this model is α asymptotic = 0.571."
    HM9 (Methods, baseline inputs): "with associated values d = 59570 and d 0 = 159058"
  asymptoticMK source, github.com/MesserLab/asymptoticMK at commit c368925ea30f3d7aa158fa88a2140c850f82db36
  (2020-01-20), fetched 2026-10-13 to sources/raw/l3-asymptoticmk-c368925-2026-10-13/ (read, never executed):
  asymptoticMK_local.R sha256 896c227e5dc46ed5e1db486a7f23687ded58a45add9ed344c14ac9e5c27879fc;
  sample_polymorphism_levels.txt sha256 02d82835aba4bbf01d44503027338ca0a3af9109e1f0a08b507e0fae49a91afb.
  Ported rules (R line numbers): grid start a in seq(-1,1,11), b in seq(-1,1,10), c in seq(1,10,11), refined by
  nls (l.158-167), deeper grid (res 20) if that fails (l.312-318); linear lm fallback; AIC choice (l.327);
  exponential rejected if its Monte Carlo 95% CI at x = 1 has a bound below -100 or above 100 (l.339);
  predictNLS with nsim = 10000, empirical = TRUE, 2.5% and 97.5% quantiles (l.38-149); linear CI from
  predict(interval = "confidence") (l.350); alpha_original from the trimmed bins (l.307).
  Uricchio, Petrov & Enard 2019 (quotes already verified and filed in quotes-literature.md, Uricchio2019 block,
  sha256 3e7c44cb...b865977; `main` asserts them as substrings of that file): "original aMK approach ( α ^ = 0.076";
  the data quotes (human-specific substitutions by parsimony on hg19/panTro4/ponAbe2; "all 661 samples with
  African ancestry") are in R4-A2e-alpha.md, Uricchio addendum.

THRESHOLDS (asserted as strings in research/checks/results/R4-A2e-alpha.md by `smoke` and `main`)
  G1 = 252,000 / 1,322 = 190.6 adaptive substitutions per lineage (MITTENS 3.0); G2 = 252,000 / 1,587 = 158.8.
  Published alpha* range 0.65%-1.75% (denominators N1 19,570, N2 11,090, N3 18,180; N1 range 14,678-24,463).
  L3 also counts its own human-specific nonsynonymous divergence Dn (a lower bound on the exome count, gene set
  incomplete).  The two band edges take the side least favourable to each side's clearance:
    h = max(0.0175, G1 / Dn)        (upper edge; a critic-side clearance must exceed it)
    l = min(0.0065, G2 / Dn)        (lower edge; a Day-side clearance must fall below it)
  Counts are reported as alpha x Dn and alpha x N1..N3, against G1 and G2.

DATA (exact releases; public, no terms beyond attribution; rule 6)
  P  1000 Genomes phase 3, sites-only VCF (GRCh37), release 20130502, v5c:
     https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.wgs.phase3_shapeit2_mvncall_integrated_v5c.20130502.sites.vcf.gz
     Content-Length 1,458,224,240; Last-Modified 2021-03-16 15:53:26 GMT (HEAD, 2026-10-13); about 86 million
     records (format sample).  INFO used: VT, MULTI_ALLELIC, AA (Ensembl EPO ancestral allele; upper case =
     high confidence, lower case = low confidence), AFR_AF, EUR_AF (4 decimals).
  S  1000 Genomes sample panel integrated_call_samples_v3.20130502.ALL.panel (same directory), 55,156 bytes,
     sha256 b4023dc6ee2d62ee89c8d4d347db4d348e65518d66d346574cdae7a4bbd76858; AFR 661 (2n = 1,322),
     EUR 503 (2n = 1,006).  AFR includes ASW and ACB, as in Uricchio's 661.
  D  UCSC hg19 multiz100way, knownCanonical coding exons with aligned sequence of 100 species:
     https://hgdownload.soe.ucsc.edu/goldenPath/hg19/multiz100way/alignments/knownCanonical.exonNuc.fa.gz
     Content-Length 751,329,171; Last-Modified 2016-10-09 00:36:57 GMT.  Species used: hg19, panTro4 (chimp),
     ponAbe2 (orangutan) (README of the same directory, sha256 6f967434...848228).  Header format
     ">tx_db_exonNum_exonCount size frameStart frameEnd chrom:start-end(strand)", 1-based inclusive coordinates;
     sequences in transcript orientation, exons numbered in transcript order (format sample, chr1).
  `main` asserts both large files' byte sizes equal the registered Content-Lengths and the panel's sha256, and
  prints the sha256 of all three (recorded in raw/l3_main.host by the run task).

PIPELINE (`count`; all choices fixed here)
  Transcripts: knownCanonical, autosomes chr1-chr22 only (X, Y, M, random, hap, Un dropped).  Human CDS =
  concatenation of the hg19 exon sequences in exonNum order; all exons present; length multiple of 3; starts ATG;
  all ACGT; no in-frame stop before the last codon.  A terminal stop codon is dropped from analysis.  Transcripts
  failing any of these are dropped (counted by reason).  Chimp and orangutan exon sequences are concatenated in
  the same order (missing exon = gaps).
  Codon filter (both P and D): a codon is used only if hg19, panTro4 and ponAbe2 are all A/C/G/T (case-blind) at
  all three positions.  Sites covered by more than one retained transcript are excluded (both P and D).
  Polymorphism (P): biallelic SNP records (VT=SNP, no MULTI_ALLELIC flag, REF and ALT single bases) in a used
  codon; hg19 base must equal REF (strand-adjusted), else counted as a mismatch and skipped; ancestral = AA (must
  be REF or ALT, else skipped); derived = the other allele.  Derived count in AFR = round(AFR_AF x 1,322); EUR
  likewise with 1,006; a value further than 0.1 from an integer is counted as non-integral (gate GC).  Sites with
  derived count 0 or 2n are not polymorphic in that population.  Class: ancestral codon = hg19 codon with the
  site set to AA; derived codon = with the derived allele; nonsynonymous if the amino acids differ, synonymous if
  equal; a polymorphism that creates or removes a stop is excluded.  Governing: upper-case AA only; the all-case
  arrays (S4) also count lower-case AA.
  Frequency bins: 20 bins of derived frequency x = i / 2n, bin k = ceil(20 i / 2n), k = 1..20, x_k = (k - 0.5)/20.
  Divergence (D): human-specific substitution = hg19 differs from panTro4 and panTro4 equals ponAbe2 (parsimony,
  as Uricchio).  Codons with two or more such differences are excluded (counted).  A site at which the 1000
  Genomes file lists any SNP record (any population, multi-allelic included) is excluded from D (it is counted
  in P if eligible).  Class by changing the hg19 codon at the site back to the chimp base; stop-involving codons
  excluded.  Sensitivity S6 (report only): human-chimp total divergence, hg19 != panTro4 regardless of orangutan,
  single-difference codons, same exclusions.
  Output: per-transcript arrays Dn, Ds, Dn_hc, Ds_hc and 20-bin Pn/Ps for AFR (upper-case AA), AFR (all-case AA)
  and EUR (upper-case AA), plus QC counters (results/raw/l3_counts.npz and .json).

STATISTIC (`analyse`)
  alpha(x_k) = 1 - (Ds/Dn) (Pn_k / Ps_k) per bin (Haller & Messer Eq. 2 with site counts cancelling).
  Governing row GOV: AFR, upper-case AA, 20 bins, fit window [0.1, 0.9] on x_k inclusive (bins 3-18; HM5).
  Fit: the asymptoticMK procedure ported to Python (above; least_squares 'lm' in place of R's Gauss-Newton,
  validated by the baseline gate GG).  P = alpha_fit(1) (HM3).
  Intervals: (i) the asymptoticMK interval (Monte Carlo, 10,000 draws, seed 20261013; or the linear t interval);
  (ii) a gene bootstrap: 1,000 resamples of transcripts with replacement (seed 20261013), the whole procedure
  refitted in each, percentile 2.5%/97.5%.  The governing interval is their envelope, L = min of the two lower
  bounds, U = max of the two upper bounds (conservative for both sides: it makes every clearance harder).
  Also reported, no verdict weight: alpha_std_all = 1 - (Ds/Dn)(sum Pn / sum Ps) over all bins (the classic MK);
  alpha_original = the same over the window bins (asymptoticMK's comparator); the correction P - alpha_std_all;
  bootstrap intervals for both; alpha(x_k) for every bin; the chosen model and its coefficients.

GATES (any failure gives band B0: no estimate, no move)
  GG  baseline: the port reproduces asymptoticMK on its own sample data (d = 59570, d0 = 159058, cutoff
      [0.1, 0.9]): alpha_asymptotic within 0.005 of 0.571 (HM8), exponential model chosen.
  GH  panel: AFR 661 and EUR 503 individuals (asserted in `count`; a failure aborts the run).
  GA  at least 10,000 transcripts pass the CDS QC.
  GB  REF mismatches at most 1% of CDS biallelic SNP records checked (a coordinate or strand error otherwise).
  GC  non-integral allele counts at most 0.1% of those records.
  GD  Dn >= 3,000, Ds >= 3,000, and 0.3 <= Dn/Ds <= 1.5.
  GE  every window bin of GOV has Ps >= 50.
  GF  at most 5% of GOV bootstrap replicates fail (non-finite alpha in a window bin, or no model fitted).

BANDS (governing row; P = point, [L, U] = governing interval; exhaustive by construction: branch on P first)
  B0  a gate fails.
  P > h:   B1  L >= 3h            interval clears the upper edge by at least 3x
           B2  h < L < 3h         interval clears the upper edge, by less than 3x
           B3  L <= h             point clears, interval does not
  l <= P <= h:  B4                point inside the alpha* band
  P < l:   B5  U >= l             point below the lower edge, interval reaches it
           B6  U < l              interval below the lower edge
  (Ties: P == h is B4; L == h is B3; L == 3h is B1; P == l is B4; U == l is B5.)
  Reachability (ST-05): every band is reached by `smoke` on synthetic tables fed to the real `analyse` entry point.
    Critic-side bands B1/B2: alpha(x) in the window rising to about 0.04-0.10 or more with Pn/Ps volumes like the
      exome (Ps of order 1e4-1e5 per window) gives L > h.
    Day-side bands B3-B6: Pn_k/Ps_k in the window staying at or above about 0.98 Dn/Ds (alpha(x) <= 0.02), or a
      downturn in the top bins (polarisation error) so the fit, or its linear fallback, extrapolates to <= h;
      or gene-level heterogeneity wide enough that the bootstrap lower bound reaches h (B3).
    B0: a broken input (zero Ps bins, too few transcripts, too small Dn).

SENSITIVITY ROWS AND THE ROBUSTNESS RULE
  S1 window [0.05, 0.95]; S2 window [0.15, 0.85]; S3 10 bins (pairs of the 20 merged), window [0.1, 0.9];
  S4 all-case AA (low-confidence ancestral alleles included); S5 EUR instead of AFR (the demography contrast:
  HM6 says demographic bias cancels if it affects both classes "in the same way"; a bottlenecked sample tests it).
  S6 (report only, excluded from the rule): pooled human-chimp divergence (a two-lineage basis; counts as Dn_hc/2).
  Rule: the move row is the governing band, except that B1 drops to B2 and B2 drops to B3 if any of S1-S5 has its
  point P <= h; and B6 rises to B5 and B5 rises to B4 if any of S1-S5 has its point P >= l.  The rule is
  symmetric: it removes a clearance on either side that does not survive a registered alternative choice.
  Bootstrap and MC intervals are reported for S1-S6 but do not enter the rule.

VERDICT MOVES (A2e external, the any-effect-size count reading; internal `non-sequitur` and fidelity untouched)
  Scale: supported < contested-leaning-supported < contested < contested-leaning-contradicted < contradicted.
  The value L3 licenses on its own evidence, by move row:
    B1  contradicted (scoped: rate_human <= 1/G_f read as a per-generation count of adaptive fixations of any
        effect size, coding-only, on model-inferred alpha).  Meets the condition R4-A2e-alpha stated in advance
        for `contradicted` ("another bias-corrected human-branch estimator, e.g. asymptotic MK ... confirming
        alpha above about 1% on the human lineage itself"), with an interval that excludes the flip by >= 3x.
    B2  contradicted (scoped, as B1), with the certainty qualifier "interval clears the flip by less than 3x".
    B3  contested, leaning contradicted.
    B4  contested.
    B5  contested.
    B6  contested, leaning supported.  Meets the condition R4-A2e-alpha stated in advance for a move "toward
        supported" ("a bias-corrected human-branch alpha below ~1% with an interval excluding it").  It stops at a
        lean, not `supported`, because the method is documented to tend toward underestimation (HM7), so a low
        aMK is compatible with a higher estimate from a method that corrects that bias (Uricchio's ABC-MK);
        conversely a high aMK is conservative.  This asymmetry is stated before the run.
    B0  none.
  Combination with the field value F the claim file carries when L3 integrates (F = `pending` while the D-21
  reviews run; L3 does not end D-21's pending by itself, the operator applies this rule to the value D-21 yields):
    * licensed value above F (rows B1-B3): L3 licenses proposing the licensed value, after L3's own three reviews.
    * licensed value equal to F: confirms; no change.
    * licensed value below F: in row B3 no change (the point is on the same side as the bases already cited;
      L3 is recorded as non-confirming).  In rows B4-B6 (point on the other side of the flip): one step down
      (B4, B5) or two steps down, not below the licensed value (B6), proposed to the owner with the discrepancy
      stated; and the line "aMK baseline (alpha 0.076) 4.4x" is struck from any `contradicted` basis as not
      reproduced on the same samples.  L3 alone never takes the field below its licensed value.
  Strong-effect-only and fitness-weighted readings: no move in any row (aMK does not split by effect size).
  A (A2e supports A) and F2: no direct move in any row; an A2e change reaches A only through the operator's
  hierarchy roll-up.  RG-03 (non-coding adaptation): no bearing; L3 is coding-only.

PREDICTIONS (scored by `score`; B0 makes the side predictions unscorable)
  DS  (Day side; the audit's reading of what A2e needs, no Day number exists): move row in {B3, B4, B5, B6}: the
      governing interval does not exclude h.  Reachable as above (flat or falling alpha(x), or a wide interval).
  DS+ (Day side, strong form): move row in {B4, B5, B6}: the point itself is at or below h.
  CS  (critic side): move row in {B1, B2}: the interval excludes h.  Reachable as above.
  CS+ (critic side, strong form): move row B1.
  Audit's own (informed by Uricchio's aMK 0.076 on the same samples and by training background):
  Q1  alpha_std_all (GOV data, all bins) in [-0.60, 0.00].
  Q2  P in [0.03, 0.15].
  Q3  P - alpha_std_all >= 0.10.
  Q4  Dn in [12,000, 32,000] and Dn/Ds in [0.45, 0.90].
  Q5  U - L <= 0.15.
  Q6  |P(S5, EUR) - P(GOV)| <= 0.05.
  Q7  the governing fit chooses the exponential model.
  Q8  move row B2.
  Q9  no gate fails.
  Consistency with the band rule (ST-09): DS and CS partition B1-B6; Q2 (P >= 0.03 > h_max) and Q8 are compatible.

RESOURCES, LAUNCH AND COLLECT (a separate run task, AFTER the `ph2` collect task on na-workhorse is done)
  Cost from the local smoke (synthetic): see raw/l3_smoke.out (`count` throughput and peak RSS; `analyse` time on
  a 20,000-transcript table).  Expected order on the real files: one process, < 2 GB RAM, < 1 h.
  1. Commit is pushed; on na-workhorse: `uptime` (at most 11 busy processes in total; RAM under ~12 GB).
  2. rsync this script and the three local source directories to na-workhorse:
       rsync -a research/checks/l3_amk.py na-workhorse:projects/evo-sim/research/checks/
       rsync -a research/checks/results/R4-A2e-alpha.md na-workhorse:projects/evo-sim/research/checks/results/
       rsync -a docs/research/sources/quotes-literature.md na-workhorse:projects/evo-sim/docs/research/sources/
       rsync -a sources/raw/l3-hallermesser-2026-10-13 sources/raw/l3-asymptoticmk-c368925-2026-10-13 na-workhorse:projects/evo-sim/sources/raw/
  3. Fetch into a new directory (rule 4), on na-workhorse:
       D=sources/raw/l3-data-<YYYY-MM-DD>; mkdir -p $D
       curl -s -o $D/sites.vcf.gz https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.wgs.phase3_shapeit2_mvncall_integrated_v5c.20130502.sites.vcf.gz
       curl -s -o $D/knownCanonical.exonNuc.fa.gz https://hgdownload.soe.ucsc.edu/goldenPath/hg19/multiz100way/alignments/knownCanonical.exonNuc.fa.gz
       curl -s -o $D/integrated_call_samples_v3.20130502.ALL.panel https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/integrated_call_samples_v3.20130502.ALL.panel
  4. Smoke on the host first:  research/.venv/bin/python -I research/checks/l3_amk.py smoke > research/checks/results/raw/l3_smoke_host.out 2>&1
  5. Launch:  nohup research/.venv/bin/python -I research/checks/l3_amk.py main $D > research/checks/results/raw/l3_main.out 2>&1 < /dev/null &
     Record hostname, date, PID and the md5 of l3_amk.py in research/checks/results/raw/l3_main.host.
  6. Collect: rsync -a 'na-workhorse:projects/evo-sim/research/checks/results/raw/l3_*' research/checks/results/raw/
     (outputs: l3_main.out, l3_counts.npz, l3_counts.json, l3_result.json).  Never commit or push from workhorse.
  `analyse` can be re-run locally on l3_counts.npz (seconds; within the workstation limit).

SMOKE (`smoke`; local, one process at a time, synthetic inputs only)
  Baseline gate GG on the asymptoticMK sample data; threshold and quote strings asserted; the band function
  checked for exhaustiveness and ties; a synthetic alignment + VCF + panel run through the real `count` entry point
  (subprocess) with exact expected counts (both strands, upper/lower-case AA, multi-allelic, REF mismatch,
  overlap, polymorphic divergence site, two-hit codon, stop-creating SNP); synthetic count tables run through the
  real `analyse` entry point (subprocess, all sensitivity rows) reaching B0-B6 and both robustness moves; cost
  measured (wall time and peak RSS of `count` per input line; `analyse` on 20,000 transcripts with 1,000
  bootstrap replicates).
"""

import argparse
import bisect
import gzip
import hashlib
import html
import json
import math
import os
import re
import resource
import subprocess
import sys
import tempfile
import time

import numpy as np
from scipy import stats
from scipy.optimize import least_squares

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
RAW = os.path.join(HERE, "results", "raw")

# ---- registered constants -------------------------------------------------------------------------------
N_AFR_IND, N_EUR_IND = 661, 503
N_AFR, N_EUR = 2 * N_AFR_IND, 2 * N_EUR_IND
G1 = 252000 / 1322
G2 = 252000 / 1587
ASTAR_LO_PUB, ASTAR_HI_PUB = 0.0065, 0.0175
N_DENOMS = {"N1": 19570, "N2": 11090, "N3": 18180, "N1_low": 14678, "N1_high": 24463}
NB = 20
WINDOW = (0.1, 0.9)
N_BOOT = 1000
N_MC = 10000
SEED = 20261013
SPECIES = ("hg19", "panTro4", "ponAbe2")
AUTOSOMES = ["chr%d" % i for i in range(1, 23)]
SIZE_SITES = 1458224240
SIZE_EXONNUC = 751329171
PANEL_SHA = "b4023dc6ee2d62ee89c8d4d347db4d348e65518d66d346574cdae7a4bbd76858"
F_SITES = "sites.vcf.gz"
F_EXONNUC = "knownCanonical.exonNuc.fa.gz"
F_PANEL = "integrated_call_samples_v3.20130502.ALL.panel"

HM_DIR = os.path.join(REPO, "sources", "raw", "l3-hallermesser-2026-10-13")
HM_SHA = "20527f3b52772a0ed9898dda7e92818c4db39d14bd419b06ade09d38ce2b07d9"
AMK_DIR = os.path.join(REPO, "sources", "raw", "l3-asymptoticmk-c368925-2026-10-13")
AMK_SAMPLE_SHA = "02d82835aba4bbf01d44503027338ca0a3af9109e1f0a08b507e0fae49a91afb"
BASELINE = {"d": 59570, "d0": 159058, "alpha": 0.571, "tol": 0.005}

HM_QUOTES = [
    "The first function is exponential, of the form α fit ( x ) = a + b exp(− cx )",
    "If the exponential fit failed to converge, then the linear model is chosen; if both fits succeeded, then the "
    "better model is chosen using the Akaike Information Criterion (AIC).",
    "by evaluating the fitted function α fit ( x ) at x = 1; this is the primary result of the test",
    "For the exponential model, this is done using Monte Carlo simulation based upon the fitted model",
    "This frequency cutoff is set to [0.1, 0.9] by default",
    "any biases due to demography or linked selection that affect the SFS in the test and reference regions in the "
    "same way will effectively cancel out",
    "The asymptotic MK test may still have a tendency toward underestimation as well, but errors are much smaller.",
    "The asymptotic MK estimate provided by this model is α asymptotic = 0.571.",
    "with associated values d = 59570 and d 0 = 159058",
]
A2E_ALPHA_STRINGS = ["190.6", "158.8", "0.65%-1.75%", "19,570", "11,090", "18,180", "14,678-24,463",
                     "0.076", "4.4x"]
QUOTES_LIT_STRINGS = ["original aMK approach ( α ^ = 0.076", "### Uricchio2019 (sha256 3e7c44cb"]

BANDS = ["B0", "B1", "B2", "B3", "B4", "B5", "B6"]
LICENSED = {"B1": "contradicted (scoped, any-effect-size count reading)",
            "B2": "contradicted (scoped), qualifier: interval clears the flip by less than 3x",
            "B3": "contested, leaning contradicted", "B4": "contested", "B5": "contested",
            "B6": "contested, leaning supported", "B0": "none (no estimate)"}

# ---- genetic code ---------------------------------------------------------------------------------------
_B = "TCAG"
_AA = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
CODE = {a + b + c: _AA[16 * i + 4 * j + k] for i, a in enumerate(_B) for j, b in enumerate(_B)
        for k, c in enumerate(_B)}
COMP = {"A": "T", "C": "G", "G": "C", "T": "A"}
ACGT = set("ACGT")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for blk in iter(lambda: f.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


def norm_xml_text(path):
    t = open(path, encoding="utf-8").read()
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    return re.sub(r"\s+", " ", t)


def peak_rss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


# ---- asymptoticMK port ----------------------------------------------------------------------------------
def _aic(rss, n, p):
    # R: logLik = -n/2 (log(2 pi) + 1 - log(n) + log(RSS)); AIC = -2 logLik + 2 (p + 1)
    return n * (math.log(2 * math.pi) + 1 - math.log(n) + math.log(rss)) + 2 * (p + 1)


def _exp_model(th, x):
    return th[0] + th[1] * np.exp(-th[2] * x)


def _fit_exp(x, y, res):
    A = np.linspace(-1, 1, res + 1)
    Bv = np.linspace(-1, 1, res)
    C = np.linspace(1, 10, res + 1)
    aa, bb, cc = np.meshgrid(A, Bv, C, indexing="ij")
    pred = aa[..., None] + bb[..., None] * np.exp(-cc[..., None] * x)
    rss = ((pred - y) ** 2).sum(-1)
    if not np.isfinite(rss).any():
        return None
    i = np.unravel_index(np.nanargmin(rss), rss.shape)
    x0 = np.array([aa[i], bb[i], cc[i]])
    try:
        r = least_squares(lambda th: _exp_model(th, x) - y, x0, method="lm", max_nfev=200 * 4)
    except Exception:
        return None
    if not r.success or not np.all(np.isfinite(r.x)):
        return None
    J = r.jac
    if np.linalg.matrix_rank(J) < 3:
        return None
    n = len(x)
    rss = float((r.fun ** 2).sum())
    if n <= 3:
        return None
    s2 = rss / (n - 3)
    try:
        cov = s2 * np.linalg.inv(J.T @ J)
    except np.linalg.LinAlgError:
        return None
    if not np.all(np.isfinite(cov)):
        return None
    return r.x, cov, rss


def _mc_ci(th, cov, rng, nsim=N_MC):
    # predictNLS with mvrnorm(empirical = TRUE): sample mean and covariance match exactly
    w, V = np.linalg.eigh(cov)
    if np.min(w) < -1e-6 * max(abs(np.max(w)), 1e-300):
        return None
    w = np.clip(w, 0, None)
    Z = rng.standard_normal((nsim, 3))
    Z -= Z.mean(0)
    Cz = np.cov(Z, rowvar=False)
    Lz = np.linalg.cholesky(Cz)
    Z = np.linalg.solve(Lz, Z.T).T
    X = th + Z @ (V * np.sqrt(w)).T
    ev = X[:, 0] + X[:, 1] * np.exp(-X[:, 2] * 1.0)
    ev = ev[np.isfinite(ev)]
    if len(ev) < nsim // 2:
        return None
    return float(np.quantile(ev, 0.025)), float(np.quantile(ev, 0.975))


def amk(x, alpha, rng, want_ci=True):
    """asymptoticMK on binned (x, alpha(x)) already trimmed to the window.  Returns dict or None."""
    x = np.asarray(x, float)
    y = np.asarray(alpha, float)
    if len(x) < 3 or not np.all(np.isfinite(y)):
        return None
    n = len(x)
    mod1 = _fit_exp(x, y, 10)
    if mod1 is None:
        mod1 = _fit_exp(x, y, 20)
    X = np.column_stack([np.ones(n), x])
    bl, rss_l = np.linalg.lstsq(X, y, rcond=None)[:2]
    rss_l = float(((X @ bl - y) ** 2).sum())
    linear_better = mod1 is None
    if not linear_better:
        th, cov, rss_e = mod1
        if rss_l <= 0 or rss_e <= 0:
            linear_better = rss_l <= rss_e
        elif _aic(rss_l, n, 2) < _aic(rss_e, n, 3):
            linear_better = True
    ci = None
    if not linear_better:
        ci = _mc_ci(th, cov, rng)
        if ci is None or ci[0] < -100 or ci[1] > 100:
            linear_better = True
    if linear_better:
        est = float(bl[0] + bl[1])
        s2 = rss_l / (n - 2) if n > 2 else float("nan")
        XtXi = np.linalg.inv(X.T @ X)
        v = np.array([1.0, 1.0])
        se = math.sqrt(max(s2 * float(v @ XtXi @ v), 0.0))
        t = stats.t.ppf(0.975, n - 2)
        return {"model": "linear", "a": float(bl[0]), "b": float(bl[1]), "c": None, "est": est,
                "lo": est - t * se, "hi": est + t * se}
    est = float(_exp_model(th, 1.0))
    return {"model": "exponential", "a": float(th[0]), "b": float(th[1]), "c": float(th[2]), "est": est,
            "lo": ci[0], "hi": ci[1]}


def baseline_gate(rng):
    path = os.path.join(AMK_DIR, "sample_polymorphism_levels.txt")
    assert sha256(path) == AMK_SAMPLE_SHA, "asymptoticMK sample data sha256 mismatch"
    rows = [ln.split() for ln in open(path).read().strip().splitlines()[1:]]
    f = np.array([float(r[0]) for r in rows])
    p = np.array([float(r[1]) for r in rows])
    p0 = np.array([float(r[2]) for r in rows])
    alpha = 1 - (BASELINE["d0"] / BASELINE["d"]) * (p / p0)
    trim = (f >= WINDOW[0]) & (f <= WINDOW[1])
    r = amk(f[trim], alpha[trim], rng)
    ok = r is not None and r["model"] == "exponential" and abs(r["est"] - BASELINE["alpha"]) <= BASELINE["tol"]
    return ok, r


# ---- counting (real data) --------------------------------------------------------------------------------
def read_panel(path):
    sp = {}
    with open(path) as f:
        f.readline()
        for ln in f:
            parts = ln.split("\t")
            if len(parts) >= 3:
                sp[parts[2]] = sp.get(parts[2], 0) + 1
    return sp


def parse_exonnuc(path):
    opener = gzip.open if path.endswith(".gz") else open
    tx = {}
    cur = None
    buf = []

    def flush():
        if cur is not None:
            name, db, num, rec = cur
            rec[db][num] = "".join(buf)

    with opener(path, "rt") as f:
        for line in f:
            if line.startswith(">"):
                flush()
                buf = []
                hdr = line[1:].split()
                parts = hdr[0].rsplit("_", 3)
                if len(parts) != 4 or parts[1] not in SPECIES:
                    cur = None
                    continue
                name, db, num, cnt = parts[0], parts[1], int(parts[2]), int(parts[3])
                rec = tx.get(name)
                if rec is None:
                    rec = {"count": cnt, "coords": {}, "hg19": {}, "panTro4": {}, "ponAbe2": {}}
                    tx[name] = rec
                if db == "hg19":
                    m = re.match(r"^(\S+):(\d+)-(\d+)([+-])$", hdr[4]) if len(hdr) > 4 else None
                    rec["coords"][num] = (m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)) if m else None
                cur = (name, db, num, rec)
            elif cur is not None:
                buf.append(line.strip())
        flush()
    return tx


def build_transcripts(tx, qc):
    out = []
    for name in sorted(tx):
        rec = tx[name]
        n = rec["count"]
        qc["tx_seen"] += 1
        nums = list(range(1, n + 1))
        if sorted(rec["hg19"]) != nums or any(rec["coords"].get(k) is None for k in nums):
            qc["tx_fail_exons"] += 1
            continue
        chroms = {rec["coords"][k][0] for k in nums}
        strands = {rec["coords"][k][3] for k in nums}
        if len(chroms) != 1 or len(strands) != 1:
            qc["tx_fail_exons"] += 1
            continue
        chrom, strand = chroms.pop(), strands.pop()
        if chrom not in AUTOSOMES:
            qc["tx_nonautosomal"] += 1
            continue
        hs, cs, os_, exons = [], [], [], []
        off = 0
        bad = False
        for k in nums:
            s = rec["hg19"][k]
            _, st, en, _ = rec["coords"][k]
            if en - st + 1 != len(s):
                bad = True
                break
            c = rec["panTro4"].get(k, "-" * len(s))
            o = rec["ponAbe2"].get(k, "-" * len(s))
            if len(c) != len(s) or len(o) != len(s):
                bad = True
                break
            hs.append(s)
            cs.append(c)
            os_.append(o)
            exons.append((st, en, off))
            off += len(s)
        if bad:
            qc["tx_fail_exons"] += 1
            continue
        h, c, o = "".join(hs).upper(), "".join(cs).upper(), "".join(os_).upper()
        if len(h) % 3 or len(h) < 6:
            qc["tx_fail_len"] += 1
            continue
        if not h.startswith("ATG"):
            qc["tx_fail_start"] += 1
            continue
        if set(h) - ACGT:
            qc["tx_fail_nonacgt"] += 1
            continue
        ncod = len(h) // 3
        if CODE[h[-3:]] == "*":
            ncod -= 1
        if any(CODE[h[3 * i:3 * i + 3]] == "*" for i in range(ncod)):
            qc["tx_fail_stop"] += 1
            continue
        ok = np.zeros(ncod, bool)
        for i in range(ncod):
            sl = slice(3 * i, 3 * i + 3)
            ok[i] = not (set(h[sl]) - ACGT or set(c[sl]) - ACGT or set(o[sl]) - ACGT)
        out.append({"name": name, "chrom": chrom, "strand": strand, "h": h, "c": c, "o": o, "ncod": ncod,
                    "ok": ok, "exons": exons, "excl": set()})
        qc["tx_pass"] += 1
    return out


def _positions(t):
    ps = []
    for st, en, off in t["exons"]:
        ps.append(np.arange(st, en + 1) if t["strand"] == "+" else np.arange(en, st - 1, -1))
    return np.concatenate(ps)


def mark_overlaps(trs, qc):
    by_chrom = {}
    for i, t in enumerate(trs):
        by_chrom.setdefault(t["chrom"], []).append(i)
    for chrom, idx in by_chrom.items():
        pos = [_positions(trs[i]) for i in idx]
        allp = np.concatenate(pos)
        u, cnt = np.unique(allp, return_counts=True)
        ov = u[cnt > 1]
        if len(ov) == 0:
            continue
        qc["overlap_positions"] += int(len(ov))
        for i, p in zip(idx, pos):
            hit = np.nonzero(np.isin(p, ov))[0]
            trs[i]["excl"].update(int(j) for j in hit)


def build_index(trs):
    ix = {}
    for ti, t in enumerate(trs):
        for st, en, off in t["exons"]:
            ix.setdefault(t["chrom"], []).append((st, en, ti, off))
    out = {}
    for chrom, lst in ix.items():
        lst.sort()
        starts = [a[0] for a in lst]
        ends = [a[1] for a in lst]
        pmax, m = [], -1
        for e in ends:
            m = max(m, e)
            pmax.append(m)
        out[chrom] = (starts, ends, pmax, [a[2] for a in lst], [a[3] for a in lst])
    return out


def lookup(entry, pos):
    starts, ends, pmax, tids, offs = entry
    i = bisect.bisect_right(starts, pos) - 1
    while i >= 0 and pmax[i] >= pos:
        if ends[i] >= pos:
            return i
        i -= 1
    return None


def _info(info, key):
    k = key + b"="
    for fld in info.split(b";"):
        if fld.startswith(k):
            return fld[len(k):]
    return None


def count(exonnuc, vcf, panel, out_prefix):
    t0 = time.time()
    qc = {k: 0 for k in ["tx_seen", "tx_pass", "tx_fail_exons", "tx_nonautosomal", "tx_fail_len",
                         "tx_fail_start", "tx_fail_nonacgt", "tx_fail_stop", "overlap_positions",
                         "vcf_lines", "snp_records_cds", "snp_multiallelic", "snp_nonsingle", "snp_codon_filtered",
                         "snp_overlap", "snp_ref_mismatch", "snp_ref_checked", "snp_aa_missing", "snp_aa_lower",
                         "snp_af_nonint", "snp_stop", "snp_terminal_codon", "poly_afr_hi", "poly_afr_all",
                         "poly_eur_hi", "div_codons_multi", "div_site_poly", "div_site_overlap", "div_stop",
                         "div_hs", "div_hc_codons_multi"]}
    sp = read_panel(panel)
    assert sp.get("AFR") == N_AFR_IND and sp.get("EUR") == N_EUR_IND, "gate GH failed: panel %r" % sp
    qc["panel"] = sp
    tx = parse_exonnuc(exonnuc)
    trs = build_transcripts(tx, qc)
    del tx
    mark_overlaps(trs, qc)
    index = build_index(trs)
    qc["t_parse_s"] = round(time.time() - t0, 1)
    ntx = len(trs)
    arr = {k: np.zeros((ntx, NB), np.int32) for k in ["Pn_afr", "Ps_afr", "Pn_afr_all", "Ps_afr_all",
                                                     "Pn_eur", "Ps_eur"]}
    poly = [set() for _ in range(ntx)]
    chrom_key = {c[3:].encode(): c for c in AUTOSOMES}
    t1 = time.time()
    opener = gzip.open if vcf.endswith(".gz") else open
    with opener(vcf, "rb") as f:
        for line in f:
            if line[:1] == b"#":
                continue
            qc["vcf_lines"] += 1
            c = line.split(b"\t", 8)
            chrom = chrom_key.get(c[0])
            if chrom is None:
                continue
            entry = index.get(chrom)
            if entry is None:
                continue
            pos = int(c[1])
            i = lookup(entry, pos)
            if i is None:
                continue
            info = c[7].rstrip(b"\r\n")
            vt = _info(info, b"VT")
            if vt is None or b"SNP" not in vt.split(b","):
                continue
            ti = entry[2][i]
            t = trs[ti]
            st, en, off = entry[0][i], entry[1][i], entry[4][i]
            ci = off + (pos - st if t["strand"] == "+" else en - pos)
            poly[ti].add(ci)
            qc["snp_records_cds"] += 1
            if b"MULTI_ALLELIC" in info.split(b";"):
                qc["snp_multiallelic"] += 1
                continue
            ref, alt = c[3].decode(), c[4].decode()
            if len(ref) != 1 or len(alt) != 1 or ref not in ACGT or alt not in ACGT:
                qc["snp_nonsingle"] += 1
                continue
            k = ci // 3
            if k >= t["ncod"]:
                qc["snp_terminal_codon"] += 1
                continue
            if not t["ok"][k]:
                qc["snp_codon_filtered"] += 1
                continue
            if ci in t["excl"]:
                qc["snp_overlap"] += 1
                continue
            if t["strand"] == "-":
                ref_t, alt_t = COMP[ref], COMP[alt]
            else:
                ref_t, alt_t = ref, alt
            qc["snp_ref_checked"] += 1
            if t["h"][ci] != ref_t:
                qc["snp_ref_mismatch"] += 1
                continue
            aa_raw = (_info(info, b"AA") or b"").split(b"|")[0].decode()
            if aa_raw.upper() not in (ref, alt):
                qc["snp_aa_missing"] += 1
                continue
            hi_conf = aa_raw.isupper()
            if not hi_conf:
                qc["snp_aa_lower"] += 1
            anc = aa_raw.upper()
            der_is_alt = anc == ref
            anc_t = ref_t if der_is_alt else alt_t
            der_t = alt_t if der_is_alt else ref_t
            cod = t["h"][3 * k:3 * k + 3]
            j = ci - 3 * k
            ca = cod[:j] + anc_t + cod[j + 1:]
            cd = cod[:j] + der_t + cod[j + 1:]
            a1, a2 = CODE[ca], CODE[cd]
            if a1 == "*" or a2 == "*":
                qc["snp_stop"] += 1
                continue
            cls = "n" if a1 != a2 else "s"
            for pop, n2 in (("afr", N_AFR), ("eur", N_EUR)):
                raw = _info(info, (pop.upper() + "_AF").encode())
                af = float(raw.split(b",")[0]) if raw else 0.0
                x = af * n2
                ac = int(round(x))
                if abs(x - ac) > 0.1:
                    qc["snp_af_nonint"] += 1
                der = ac if der_is_alt else n2 - ac
                if 0 < der < n2:
                    b = int(math.ceil(NB * der / n2)) - 1
                    if pop == "afr":
                        arr["P%s_afr_all" % cls][ti, b] += 1
                        qc["poly_afr_all"] += 1
                        if hi_conf:
                            arr["P%s_afr" % cls][ti, b] += 1
                            qc["poly_afr_hi"] += 1
                    elif hi_conf:
                        arr["P%s_eur" % cls][ti, b] += 1
                        qc["poly_eur_hi"] += 1
    qc["t_vcf_s"] = round(time.time() - t1, 1)
    D = {k: np.zeros(ntx, np.int32) for k in ["Dn", "Ds", "Dn_hc", "Ds_hc"]}
    for ti, t in enumerate(trs):
        h, c, o = t["h"], t["c"], t["o"]
        for k in range(t["ncod"]):
            if not t["ok"][k]:
                continue
            a, b = 3 * k, 3 * k + 3
            hc = [j for j in range(a, b) if h[j] != c[j]]
            if not hc:
                continue
            hsd = [j for j in hc if c[j] == o[j]]
            # human-specific (parsimony)
            if len(hsd) >= 2:
                qc["div_codons_multi"] += 1
            elif len(hsd) == 1:
                j = hsd[0]
                if j in poly[ti]:
                    qc["div_site_poly"] += 1
                elif j in t["excl"]:
                    qc["div_site_overlap"] += 1
                else:
                    ch = h[a:b]
                    anc = ch[:j - a] + c[j] + ch[j - a + 1:]
                    a1, a2 = CODE[anc], CODE[ch]
                    if a1 == "*" or a2 == "*":
                        qc["div_stop"] += 1
                    else:
                        D["Dn" if a1 != a2 else "Ds"][ti] += 1
                        qc["div_hs"] += 1
            # pooled human-chimp (S6)
            if len(hc) >= 2:
                qc["div_hc_codons_multi"] += 1
            else:
                j = hc[0]
                if j in poly[ti] or j in t["excl"]:
                    continue
                ch = h[a:b]
                other = ch[:j - a] + c[j] + ch[j - a + 1:]
                a1, a2 = CODE[other], CODE[ch]
                if a1 != "*" and a2 != "*":
                    D["Dn_hc" if a1 != a2 else "Ds_hc"][ti] += 1
    qc["t_total_s"] = round(time.time() - t0, 1)
    qc["peak_rss_mb"] = round(peak_rss_mb(), 1)
    np.savez_compressed(out_prefix + ".npz", tx=np.array([t["name"] for t in trs]),
                        chrom=np.array([t["chrom"] for t in trs]), **D, **arr)
    with open(out_prefix + ".json", "w") as f:
        json.dump(qc, f, indent=1, sort_keys=True)
    return qc


# ---- analysis ---------------------------------------------------------------------------------------------
def bins_x(nb):
    return (np.arange(1, nb + 1) - 0.5) / nb


def merge10(a):
    return a[..., 0::2] + a[..., 1::2]


def alpha_bins(Dn, Ds, Pn, Ps):
    with np.errstate(divide="ignore", invalid="ignore"):
        return 1 - (Ds / Dn) * (Pn / Ps)


def fit_row(Dn, Ds, Pn, Ps, window, rng):
    nb = Pn.shape[-1]
    x = bins_x(nb)
    tr = (x >= window[0] - 1e-12) & (x <= window[1] + 1e-12)
    if Dn <= 0 or Ds <= 0 or np.any(Ps[tr] <= 0):
        return None
    a = alpha_bins(Dn, Ds, Pn, Ps)
    return amk(x[tr], a[tr], rng)


def row_stats(arrs, key_n, key_s, nb, window, dkey, n_boot, rng, boot_seed):
    Dn_g, Ds_g = arrs[dkey[0]].astype(float), arrs[dkey[1]].astype(float)
    Pn_g, Ps_g = arrs[key_n].astype(float), arrs[key_s].astype(float)
    if nb == 10:
        Pn_g, Ps_g = merge10(Pn_g), merge10(Ps_g)
    Dn, Ds, Pn, Ps = Dn_g.sum(), Ds_g.sum(), Pn_g.sum(0), Ps_g.sum(0)
    x = bins_x(nb)
    tr = (x >= window[0] - 1e-12) & (x <= window[1] + 1e-12)
    fit = fit_row(Dn, Ds, Pn, Ps, window, rng)
    with np.errstate(divide="ignore", invalid="ignore"):
        a_all = 1 - (Ds / Dn) * (Pn.sum() / Ps.sum()) if Dn > 0 and Ps.sum() > 0 else float("nan")
        a_orig = 1 - (Ds / Dn) * (Pn[tr].sum() / Ps[tr].sum()) if Dn > 0 and Ps[tr].sum() > 0 else float("nan")
    out = {"Dn": int(Dn), "Ds": int(Ds), "Pn": [int(v) for v in Pn], "Ps": [int(v) for v in Ps],
           "x": [round(float(v), 4) for v in x], "window_bins": [int(i) + 1 for i in np.nonzero(tr)[0]],
           "alpha_x": [None if not np.isfinite(v) else float(v) for v in alpha_bins(Dn, Ds, Pn, Ps)],
           "alpha_std_all": float(a_all), "alpha_original": float(a_orig), "fit": fit}
    ntx = Dn_g.shape[0]
    brng = np.random.default_rng(boot_seed)
    ests, stds, origs, fails = [], [], [], 0
    G = np.column_stack([Dn_g, Ds_g, Pn_g, Ps_g])
    for _ in range(n_boot):
        w = np.bincount(brng.integers(0, ntx, ntx), minlength=ntx).astype(float)
        s = w @ G
        bDn, bDs, bPn, bPs = s[0], s[1], s[2:2 + nb], s[2 + nb:]
        r = fit_row(bDn, bDs, bPn, bPs, window, brng)
        if r is None or not np.isfinite(r["est"]):
            fails += 1
            continue
        ests.append(r["est"])
        stds.append(1 - (bDs / bDn) * (bPn.sum() / bPs.sum()))
        origs.append(1 - (bDs / bDn) * (bPn[tr].sum() / bPs[tr].sum()))
    q = lambda v: [float(np.quantile(v, 0.025)), float(np.quantile(v, 0.975))] if len(v) else [None, None]
    out.update({"boot_n": n_boot, "boot_fail": fails, "boot_ci": q(ests), "boot_ci_std_all": q(stds),
                "boot_ci_original": q(origs)})
    if fit is not None and len(ests):
        out["L"] = min(fit["lo"], out["boot_ci"][0])
        out["U"] = max(fit["hi"], out["boot_ci"][1])
        out["P"] = fit["est"]
    else:
        out["L"] = out["U"] = out["P"] = None
    return out


def band(P, L, U, h, l):
    """Exhaustive band by the registered rule (branch on P first)."""
    if P > h:
        if L >= 3 * h:
            return "B1"
        if L > h:
            return "B2"
        return "B3"
    if P >= l:
        return "B4"
    if U >= l:
        return "B5"
    return "B6"


def move_row(gov_band, sens_points, h, l):
    if gov_band in ("B1", "B2") and any(p is None or p <= h for p in sens_points):
        return {"B1": "B2", "B2": "B3"}[gov_band]
    if gov_band in ("B5", "B6") and any(p is None or p >= l for p in sens_points):
        return {"B6": "B5", "B5": "B4"}[gov_band]
    return gov_band


def gates(qc, gov, Ds_total, Dn_total, baseline_ok):
    g = {}
    g["GG"] = bool(baseline_ok)
    g["GA"] = qc.get("tx_pass", 0) >= 10000
    chk = max(qc.get("snp_ref_checked", 0), 1)
    g["GB"] = qc.get("snp_ref_mismatch", 0) / chk <= 0.01
    g["GC"] = qc.get("snp_af_nonint", 0) / chk <= 0.001
    g["GD"] = Dn_total >= 3000 and Ds_total >= 3000 and 0.3 <= Dn_total / max(Ds_total, 1) <= 1.5
    wb = [b - 1 for b in gov["window_bins"]]
    g["GE"] = all(gov["Ps"][b] >= 50 for b in wb)
    g["GF"] = gov["boot_fail"] <= 0.05 * gov["boot_n"] and gov["P"] is not None
    return g


ROWS = [  # name, Pn key, Ps key, bins, window, divergence keys, in robustness rule
    ("GOV", "Pn_afr", "Ps_afr", 20, (0.1, 0.9), ("Dn", "Ds"), False),
    ("S1", "Pn_afr", "Ps_afr", 20, (0.05, 0.95), ("Dn", "Ds"), True),
    ("S2", "Pn_afr", "Ps_afr", 20, (0.15, 0.85), ("Dn", "Ds"), True),
    ("S3", "Pn_afr", "Ps_afr", 10, (0.1, 0.9), ("Dn", "Ds"), True),
    ("S4", "Pn_afr_all", "Ps_afr_all", 20, (0.1, 0.9), ("Dn", "Ds"), True),
    ("S5", "Pn_eur", "Ps_eur", 20, (0.1, 0.9), ("Dn", "Ds"), True),
    ("S6", "Pn_afr", "Ps_afr", 20, (0.1, 0.9), ("Dn_hc", "Ds_hc"), False),
]


def score(res):
    mr = res["move_row"]
    s = {}
    if mr == "B0":
        for k in ("DS", "DS+", "CS", "CS+"):
            s[k] = "not scorable (B0)"
    else:
        s["DS"] = mr in ("B3", "B4", "B5", "B6")
        s["DS+"] = mr in ("B4", "B5", "B6")
        s["CS"] = mr in ("B1", "B2")
        s["CS+"] = mr == "B1"
    g = res["rows"]["GOV"]
    P, L, U = g["P"], g["L"], g["U"]
    s["Q1"] = -0.60 <= g["alpha_std_all"] <= 0.00
    s["Q2"] = P is not None and 0.03 <= P <= 0.15
    s["Q3"] = P is not None and P - g["alpha_std_all"] >= 0.10
    s["Q4"] = 12000 <= g["Dn"] <= 32000 and 0.45 <= g["Dn"] / max(g["Ds"], 1) <= 0.90
    s["Q5"] = L is not None and U - L <= 0.15
    p5 = res["rows"]["S5"]["P"]
    s["Q6"] = P is not None and p5 is not None and abs(p5 - P) <= 0.05
    s["Q7"] = g["fit"] is not None and g["fit"]["model"] == "exponential"
    s["Q8"] = mr == "B2"
    s["Q9"] = all(res["gates"].values())
    return s


def analyse(npz_path, n_boot=N_BOOT, json_out=None, qc_path=None, baseline=True):
    t0 = time.time()
    rng = np.random.default_rng(SEED)
    if baseline:
        b_ok, b_fit = baseline_gate(rng)
    else:
        b_ok, b_fit = True, None
    z = np.load(npz_path)
    arrs = {k: z[k] for k in z.files}
    qc_path = qc_path or npz_path[:-4] + ".json"
    qc = json.load(open(qc_path))
    rows = {}
    for i, (name, kn, ks, nb, win, dk, _) in enumerate(ROWS):
        rows[name] = row_stats(arrs, kn, ks, nb, win, dk, n_boot, np.random.default_rng(SEED + 100 + i),
                               SEED + i)
    gov = rows["GOV"]
    Dn, Ds = gov["Dn"], gov["Ds"]
    h = max(ASTAR_HI_PUB, G1 / Dn) if Dn > 0 else ASTAR_HI_PUB
    l = min(ASTAR_LO_PUB, G2 / Dn) if Dn > 0 else ASTAR_LO_PUB
    g = gates(qc, gov, Ds, Dn, b_ok)
    if not all(g.values()):
        gb = mr = "B0"
    else:
        gb = band(gov["P"], gov["L"], gov["U"], h, l)
        mr = move_row(gb, [rows[n]["P"] for n, *_r, inrule in ROWS if inrule], h, l)
    res = {"baseline_ok": b_ok, "baseline_fit": b_fit, "gates": g, "h": h, "l": l, "gov_band": gb,
           "move_row": mr, "licensed": LICENSED[mr], "rows": rows, "qc": qc,
           "t_analyse_s": None}
    res["counts"] = {}
    if gov["P"] is not None:
        for lab, a in (("P", gov["P"]), ("L", gov["L"]), ("U", gov["U"])):
            res["counts"][lab] = {"Dn_own": a * Dn, **{k: a * v for k, v in N_DENOMS.items()}}
    res["score"] = score(res)
    res["t_analyse_s"] = round(time.time() - t0, 2)
    if json_out:
        with open(json_out, "w") as f:
            json.dump(res, f, indent=1, default=float)
    return res


def fmt(v, d=4):
    return "NA" if v is None else ("%.*f" % (d, v))


def report(res):
    print("baseline GG (asymptoticMK sample data): ok=%s fit=%s" % (res["baseline_ok"], res["baseline_fit"]))
    print("gates:", json.dumps(res["gates"]))
    print("h = %.5f  l = %.5f  (G1 %.1f, G2 %.1f)" % (res["h"], res["l"], G1, G2))
    for name, *_ in ROWS:
        r = res["rows"][name]
        f = r["fit"] or {}
        print("%-4s Dn %d Ds %d  model %-11s P %s  MC/t [%s, %s]  boot [%s, %s] (fail %d)  L %s U %s  "
              "std_all %s  original %s" % (name, r["Dn"], r["Ds"], f.get("model"), fmt(r["P"]), fmt(f.get("lo")),
                                           fmt(f.get("hi")), fmt(r["boot_ci"][0]), fmt(r["boot_ci"][1]),
                                           r["boot_fail"], fmt(r["L"]), fmt(r["U"]), fmt(r["alpha_std_all"]),
                                           fmt(r["alpha_original"])))
    gov = res["rows"]["GOV"]
    print("GOV alpha(x):", " ".join("%s:%s" % (x, fmt(a, 3)) for x, a in zip(gov["x"], gov["alpha_x"])))
    print("GOV Pn:", gov["Pn"])
    print("GOV Ps:", gov["Ps"])
    if gov["P"] is not None:
        print("correction P - alpha_std_all = %.4f; P - alpha_original = %.4f" %
              (gov["P"] - gov["alpha_std_all"], gov["P"] - gov["alpha_original"]))
        for lab, d in res["counts"].items():
            print("count at %s: " % lab + "  ".join("%s %.0f (%.2fx G1)" % (k, v, v / G1) for k, v in d.items()))
    print("governing band %s; move row %s; licensed: %s" % (res["gov_band"], res["move_row"], res["licensed"]))
    print("score:", json.dumps(res["score"]))
    print("t_analyse_s", res["t_analyse_s"], "peak_rss_mb", round(peak_rss_mb(), 1))


# ---- assertions on other files ------------------------------------------------------------------------------
def assert_sources():
    t = open(os.path.join(HERE, "results", "R4-A2e-alpha.md"), encoding="utf-8").read()
    for s in A2E_ALPHA_STRINGS:
        assert s in t, "threshold string missing from R4-A2e-alpha.md: %r" % s
    q = open(os.path.join(REPO, "docs", "research", "sources", "quotes-literature.md"), encoding="utf-8").read()
    for s in QUOTES_LIT_STRINGS:
        assert s in q, "quote missing from quotes-literature.md: %r" % s
    p = os.path.join(HM_DIR, "hm.xml")
    assert sha256(p) == HM_SHA, "Haller & Messer copy sha256 mismatch"
    t = norm_xml_text(p)
    for s in HM_QUOTES:
        assert s in t, "Haller & Messer quote not found: %r" % s
    return len(A2E_ALPHA_STRINGS) + len(QUOTES_LIT_STRINGS) + len(HM_QUOTES)


# ---- smoke --------------------------------------------------------------------------------------------------
def _run(args):
    t0 = time.time()
    p = subprocess.run([sys.executable, "-I", os.path.abspath(__file__)] + args, capture_output=True, text=True)
    if p.returncode != 0:
        print(p.stdout)
        print(p.stderr)
        raise SystemExit("subprocess failed: %r" % args)
    return p.stdout, time.time() - t0


def _synthetic_inputs(d):
    """Hand-built alignment, VCF and panel with exact expected counts."""
    # T1, + strand, chr1:1001-1006 (exon 1) and 2001-2012 (exon 2); CDS ATG AAA GCT GAA CTG TAA
    # idx0..5 -> 1001..1006 ; idx6..17 -> 2001..2012; terminal stop idx15..17
    h1 = ["ATGAAA", "GCTGAACTGTAA"]
    c1 = ["ATGAAG", "GCAGAGCTATAA"]  # chimp differs at idx5, idx8, idx11, idx14
    o1 = ["ATGAAG", "GCAGAACTATAA"]  # orang = chimp at idx5, idx8, idx14 (human-specific); not at idx11
    # idx5: human-specific but in the T4 overlap -> div_site_overlap; idx8: human-specific, SNP at 2003 ->
    # div_site_poly; idx11: chimp-specific -> pooled only (GAA/GAG syn); idx14: CTG/CTA syn -> Ds and Ds_hc
    # T2, - strand, chr2: exon 1 = chr2:5007-5012 (transcript idx0..5 = genomic 5012..5007), exon 2 = 3001-3009
    h2 = ["ATGCCC", "TGGAAATGA"]   # ATG CCC TGG AAA TGA
    c2 = ["ATGCCC", "TGTAAATGA"]   # idx8 G vs T: TGG(W)/TGT(C) nonsyn; orang T -> human-specific, Dn
    o2 = ["ATGCCC", "TGTAAATGA"]
    # T3 fails QC (no ATG), chr3
    h3 = ["CTGAAATAA"]
    # T4, + strand chr1:1004-1009 overlaps T1 exon 1 at 1004-1006 -> those positions excluded in both
    h4 = ["ATGTTT"]
    # T5, + strand chr4: two human-specific diffs in one codon (excluded), and a site later found polymorphic
    h5 = ["ATGGGGCCCAAA"]           # ATG GGG CCC AAA
    c5 = ["ATGAAGCCAAAA"]           # codon2 GGG vs AAG: two diffs; codon3 CCC vs CCA (syn), codon4 same
    o5 = ["ATGAAGCCAAAA"]
    recs = [("T1", "chr1", "+", [(1001, 1006), (2001, 2012)], h1, c1, o1),
            ("T2", "chr2", "-", [(5007, 5012), (3001, 3009)], h2, c2, o2),
            ("T3", "chr3", "+", [(100, 108)], h3, h3, h3),
            ("T4", "chr1", "+", [(1004, 1009)], h4, h4, h4),
            ("T5", "chr4", "+", [(501, 512)], h5, c5, o5),
            ("T6", "chrX", "+", [(1, 6)], ["ATGAAA"], ["ATGAAA"], ["ATGAAA"])]
    lines = []
    for name, chrom, strand, ex, hs, cs, os_ in recs:
        n = len(ex)
        for k, (st, en) in enumerate(ex, 1):
            for db, seqs in (("hg19", hs), ("panTro4", cs), ("gorGor3", cs), ("ponAbe2", os_)):
                coord = " %s:%d-%d%s" % (chrom, st, en, strand) if db != "ponAbe2" else " "
                lines.append(">%s_%s_%d_%d %d 0 0%s" % (name, db, k, n, en - st + 1, coord))
                lines.append(seqs[k - 1].lower() if db == "hg19" and k == 1 else seqs[k - 1])
    with gzip.open(os.path.join(d, F_EXONNUC), "wt") as f:
        f.write("\n".join(lines) + "\n")

    def v(chrom, pos, ref, alt, afr, eur, aa, extra=""):
        afr_s = ("%.4f" % afr).rstrip("0").rstrip(".") if afr not in (0, 1) else str(int(afr))
        eur_s = ("%.4f" % eur).rstrip("0").rstrip(".") if eur not in (0, 1) else str(int(eur))
        return "%s\t%d\t.\t%s\t%s\t100\tPASS\tAC=1;AF=0.1;AN=5008;NS=2504;EAS_AF=0;AMR_AF=0;AFR_AF=%s;EUR_AF=%s;" \
               "SAS_AF=0;AA=%s|||;VT=SNP%s" % (chrom, pos, ref, alt, afr_s, eur_s, aa, extra)
    vl = ["##fileformat=VCFv4.1", "#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO"]
    # chr1 (T1 +): idx1 pos1002 T: ATG -> AAG? codon0 ATG pos idx1 'T' -> A gives AAG (M->K) nonsyn, but it
    #   creates no stop.  derived A in AFR 1322*0.5 = 661 -> bin 10.  EUR 0.25 -> 251.5? use 0.2495 -> 251.0
    vl.append(v("1", 1002, "T", "A", 661 / 1322, 251 / 1006, "T"))                 # Pn afr bin10, eur bin 5
    vl.append(v("1", 1003, "G", "C", 0.1, 0.0, "G"))                               # idx2 ATG->ATC (M->I) Pn
    #   AF 0.1 -> 132.2: non-integral (counted), rounds to 132 -> bin 2
    vl.append(v("1", 1005, "A", "G", 0.0, 0.0, "A"))                               # overlap with T4 -> excluded
    vl.append(v("1", 2003, "T", "C", 1300 / 1322, 0.5, "t"))                       # idx8 GCT->GCC syn; AA lower
    #   -> only in all-case arrays; also makes idx8 polymorphic -> its human-specific Ds excluded
    vl.append(v("1", 2004, "G", "T", 0.5, 0.5, "G", ";MULTI_ALLELIC"))             # multi-allelic: skipped
    vl.append(v("1", 2004, "G", "C", 0.5, 0.5, "G", ";MULTI_ALLELIC"))
    vl.append(v("1", 2007, "T", "A", 0.5, 0.5, "T"))                               # idx12? stop codon TAA -> terminal
    vl.append(v("1", 2005, "C", "T", 0.5, 0.5, "C"))                               # idx10 hg19 is 'A' -> mismatch
    vl.append(v("1", 3000, "C", "T", 0.5, 0.5, "C"))                               # not in CDS
    # chr2 (T2 -): idx3 = exon1 genomic 5012-3 = 5009; transcript base 'C' (CCC) -> genome G. SNP G>A genome
    #   = C>T transcript: CCC -> CTC? idx3 is codon1 pos0: CCC -> TCC (P->S) nonsyn.  AA = G (ref) upper.
    vl.append(v("2", 5009, "G", "A", 1 / 1322, 0.0, "G"))                          # Pn afr bin1
    #   idx5 = genomic 5007, transcript 'C' -> genome G; SNP G>T genome = C>A transcript: CCC->CCA syn, AA = T
    #   (alt) so derived = G (ref) with derived count = 1322 - round(0.75*1322)= 1322-992 = 330 -> bin 5
    vl.append(v("2", 5007, "G", "T", 0.75, 1.0, "T"))                              # Ps afr bin5 (der=ref)
    #   EUR AF 1.0 -> derived count 0 -> not polymorphic in EUR
    # chr2 idx9 = exon2 transcript idx 9 -> genomic 3009 - (9-6) = 3006; transcript 'A' (AAA) -> genome T.
    #   SNP T>A genome = A>T transcript: AAA -> TAA stop -> excluded (snp_stop)
    vl.append(v("2", 3006, "T", "A", 0.5, 0.5, "T"))
    # chr4 T5: idx8 (CCC codon2 pos2) human-specific C vs A syn; SNP present -> div excluded, poly counted
    vl.append(v("4", 509, "C", "G", 0.3, 0.3, "C"))                                # CCC->CCG syn Ps; AA C
    vl.append(v("X", 3, "G", "A", 0.5, 0.5, "G"))                                  # non-autosomal
    with gzip.open(os.path.join(d, F_SITES), "wt") as f:
        f.write("\n".join(vl) + "\n")
    with open(os.path.join(d, F_PANEL), "w") as f:
        f.write("sample\tpop\tsuper_pop\tgender\t\t\n")
        for i, (sp, n) in enumerate((("AFR", 661), ("EUR", 503), ("EAS", 504))):
            for j in range(n):
                f.write("S%d_%d\tPOP\t%s\tmale\n" % (i, j, sp))
    expect = {
        "tx_pass": 4,              # T1, T2, T4, T5 (T3 no ATG, T6 chrX)
        "tx_fail_start": 1, "tx_nonautosomal": 1,
        "overlap_positions": 3,
        "snp_records_cds": 11, "snp_multiallelic": 2, "snp_overlap": 1, "snp_ref_mismatch": 1,
        "snp_terminal_codon": 1, "snp_stop": 1, "snp_aa_lower": 1, "snp_af_nonint": 1,
        "poly_afr_hi": 4, "poly_afr_all": 5, "poly_eur_hi": 3,
        "div_codons_multi": 1, "div_site_poly": 2,
    }
    # per-transcript expectations (sorted names: T1, T2, T4, T5)
    exp_arr = {
        "Dn": [0, 1, 0, 0], "Ds": [1, 0, 0, 0],          # T1 idx5 syn (idx8 polymorphic); T2 idx8 nonsyn
        "Pn_afr_bins": {(0, 9): 1, (0, 1): 1, (1, 0): 1},
        "Ps_afr_bins": {(1, 4): 1, (3, 5): 1},
        "Ps_afr_all_extra": {(0, 19): 1},
        "Pn_eur_bins": {(0, 4): 1},
        "Ps_eur_bins": {(3, 5): 1},
    }
    return expect, exp_arr


def _synthetic_table(path, ntx, dn_tot, ds_tot, ps_tot, a_inf, b, c, seed, eur=None, allcase=None,
                     qc_over=None):
    rng = np.random.default_rng(seed)
    w = rng.gamma(2.0, 1.0, ntx)
    w /= w.sum()
    x = bins_x(NB)
    edges = np.arange(NB + 1) / NB
    edges[0] = 1.0 / 1322
    ps_shape = np.log(edges[1:] / edges[:-1])
    ps_shape /= ps_shape.sum()

    def make(a_inf_, b_, c_, ps_tot_):
        ax = a_inf_ + b_ * np.exp(-c_ * x)
        ps = ps_tot_ * ps_shape
        pn = ps * (dn_tot / ds_tot) * (1 - ax)
        Ps = rng.poisson(np.outer(w, ps))
        Pn = rng.poisson(np.outer(w, np.clip(pn, 0, None)))
        return Pn.astype(np.int32), Ps.astype(np.int32)
    Dn = rng.poisson(w * dn_tot).astype(np.int32)
    Ds = rng.poisson(w * ds_tot).astype(np.int32)
    Pn, Ps = make(a_inf, b, c, ps_tot)
    Pn_e, Ps_e = make(*(eur or (a_inf, b, c, ps_tot * 0.6)))
    Pn_a, Ps_a = make(*(allcase or (a_inf, b, c, ps_tot * 1.1)))
    np.savez_compressed(path, tx=np.array(["t%d" % i for i in range(ntx)]), chrom=np.array(["chr1"] * ntx),
                        Dn=Dn, Ds=Ds, Dn_hc=2 * Dn, Ds_hc=2 * Ds, Pn_afr=Pn, Ps_afr=Ps, Pn_afr_all=Pn_a,
                        Ps_afr_all=Ps_a, Pn_eur=Pn_e, Ps_eur=Ps_e)
    qc = {"tx_pass": ntx, "snp_ref_checked": 100000, "snp_ref_mismatch": 10, "snp_af_nonint": 0}
    qc.update(qc_over or {})
    with open(path[:-4] + ".json", "w") as f:
        json.dump(qc, f)


SYN_CASES = [  # name, expected governing band, expected move row, table args
    ("B1", "B1", "B1", dict(a_inf=0.12, b=-0.6, c=5.0, ps_tot=400000)),
    ("B2", "B2", "B2", dict(a_inf=0.045, b=-0.5, c=5.0, ps_tot=400000)),
    ("B3", "B3", "B3", dict(a_inf=0.03, b=-0.5, c=5.0, ps_tot=8000)),
    ("B4", "B4", "B4", dict(a_inf=0.012, b=-0.5, c=5.0, ps_tot=400000)),
    ("B5", "B5", "B5", dict(a_inf=-0.002, b=-0.5, c=5.0, ps_tot=8000)),
    ("B6", "B6", "B6", dict(a_inf=-0.06, b=-0.5, c=5.0, ps_tot=400000)),
    ("B2>B3", "B2", "B3", dict(a_inf=0.045, b=-0.5, c=5.0, ps_tot=400000, eur=(0.0, -0.5, 5.0, 240000))),
    ("B6>B5", "B6", "B5", dict(a_inf=-0.06, b=-0.5, c=5.0, ps_tot=400000, eur=(0.03, -0.5, 5.0, 240000))),
    ("B0", "B0", "B0", dict(a_inf=0.05, b=-0.5, c=5.0, ps_tot=400000, qc_over={"tx_pass": 5000})),
]


def smoke():
    t_start = time.time()
    print("L3 smoke (synthetic inputs only)")
    n = assert_sources()
    print("asserted %d strings (thresholds, Uricchio record, Haller & Messer quotes)" % n)
    ok, fit = baseline_gate(np.random.default_rng(SEED))
    print("baseline GG: ok=%s %s" % (ok, fit))
    assert ok, "baseline gate failed"
    # band exhaustiveness and ties
    rng = np.random.default_rng(1)
    h, l = 0.0175, 0.0065
    for _ in range(20000):
        P = rng.uniform(-0.2, 0.3)
        L = P - rng.uniform(0, 0.1)
        U = P + rng.uniform(0, 0.1)
        b = band(P, L, U, h, l)
        assert b in BANDS[1:]
    ties = [((h, 0, 0.1), "B4"), ((0.05, h, 0.1), "B3"), ((0.06, 3 * h, 0.1), "B1"), ((l, -1, 1), "B4"),
            ((0.0, -1, l), "B5"), ((0.0, -1, l - 1e-9), "B6"), ((0.02, h + 1e-9, 0.1), "B2")]
    for (P, L, U), want in ties:
        assert band(P, L, U, h, l) == want, ((P, L, U), want)
    assert move_row("B1", [0.05, 0.01], h, l) == "B2" and move_row("B1", [0.05], h, l) == "B1"
    assert move_row("B6", [-0.05, 0.007], h, l) == "B5" and move_row("B4", [1.0], h, l) == "B4"
    print("band function: 20,000 random cases in B1-B6, %d ties as registered, robustness rule ok" % len(ties))
    tmp = tempfile.mkdtemp(prefix="l3smoke-")
    # synthetic count through the real entry point
    expect, exp_arr = _synthetic_inputs(tmp)
    out, dt = _run(["count", os.path.join(tmp, F_EXONNUC), os.path.join(tmp, F_SITES),
                    os.path.join(tmp, F_PANEL), os.path.join(tmp, "cnt")])
    qc = json.load(open(os.path.join(tmp, "cnt.json")))
    z = np.load(os.path.join(tmp, "cnt.npz"))
    bad = {k: (qc.get(k), v) for k, v in expect.items() if qc.get(k) != v}
    assert list(z["tx"]) == ["T1", "T2", "T4", "T5"], list(z["tx"])
    assert list(z["Dn"]) == exp_arr["Dn"] and list(z["Ds"]) == exp_arr["Ds"], (list(z["Dn"]), list(z["Ds"]))

    def nz(a):
        return {(int(i), int(j)): int(a[i, j]) for i, j in zip(*np.nonzero(a))}
    assert nz(z["Pn_afr"]) == exp_arr["Pn_afr_bins"], nz(z["Pn_afr"])
    assert nz(z["Ps_afr"]) == exp_arr["Ps_afr_bins"], nz(z["Ps_afr"])
    assert nz(z["Pn_afr_all"]) == exp_arr["Pn_afr_bins"], nz(z["Pn_afr_all"])
    assert nz(z["Ps_afr_all"]) == {**exp_arr["Ps_afr_bins"], **exp_arr["Ps_afr_all_extra"]}, nz(z["Ps_afr_all"])
    assert nz(z["Pn_eur"]) == exp_arr["Pn_eur_bins"], nz(z["Pn_eur"])
    assert nz(z["Ps_eur"]) == exp_arr["Ps_eur_bins"], nz(z["Ps_eur"])
    assert not bad, bad
    print("count entry point on the hand-built inputs: all %d QC counters and all per-transcript arrays as "
          "expected (%.1f s)" % (len(expect), dt))
    # cost of count: a larger synthetic VCF (mostly non-CDS lines) through the same entry point
    big = os.path.join(tmp, "big.vcf.gz")
    nlines = 200000
    with gzip.open(big, "wt") as f:
        f.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n")
        for i in range(nlines):
            f.write("1\t%d\t.\tA\tG\t100\tPASS\tAC=1;AF=0.0002;AN=5008;NS=2504;DP=9632;EAS_AF=0;AMR_AF=0;"
                    "AFR_AF=0.0008;EUR_AF=0;SAS_AF=0;AA=.|||;VT=SNP\n" % (10000 + 37 * i))
    out, dt = _run(["count", os.path.join(tmp, F_EXONNUC), big, os.path.join(tmp, F_PANEL),
                    os.path.join(tmp, "big")])
    qcb = json.load(open(os.path.join(tmp, "big.json")))
    rate = qcb["vcf_lines"] / max(qcb["t_vcf_s"], 0.05)
    print("count cost: %d VCF lines in %.1f s (%.0f lines/s); child peak RSS %.0f MB; extrapolated to 86e6 lines: "
          "%.0f min (VCF pass only; alignment parse and divergence pass not included)" %
          (qcb["vcf_lines"], qcb["t_vcf_s"], rate, qcb["peak_rss_mb"], 86e6 / rate / 60))
    # synthetic analysis tables through the real analyse entry point
    reached = {}
    for name, want_gov, want_mr, kw in SYN_CASES:
        p = os.path.join(tmp, "syn_%s.npz" % name.replace(">", "_"))
        _synthetic_table(p, 2000, 20000, 30000, seed=hash(name) % 1000 + 7, **kw)
        js = p[:-4] + "_res.json"
        out, dt = _run(["analyse", p, "--boot", "200", "--json", js])
        r = json.load(open(js))
        g = r["rows"]["GOV"]
        print("  case %-6s gov %s move %s  P %s L %s U %s  h %.4f  (%.1f s)" %
              (name, r["gov_band"], r["move_row"], fmt(g["P"]), fmt(g["L"]), fmt(g["U"]), r["h"], dt))
        assert r["gov_band"] == want_gov and r["move_row"] == want_mr, (name, r["gov_band"], r["move_row"])
        reached[name] = r["move_row"]
    print("bands reached: %s" % sorted(set(reached.values())))
    assert set(reached.values()) == set(BANDS)
    # analyse cost at real size and full bootstrap
    p = os.path.join(tmp, "cost.npz")
    _synthetic_table(p, 20000, 20000, 30000, 0.07, -0.5, 5.0, 400000, seed=11)
    out, dt = _run(["analyse", p, "--json", p[:-4] + "_res.json"])
    print("analyse cost: 20,000 transcripts, %d bootstrap replicates x 7 rows: %.1f s wall" % (N_BOOT, dt))
    print(out.strip().splitlines()[-1])
    print("smoke total %.1f s; this process peak RSS %.0f MB" % (time.time() - t_start, peak_rss_mb()))
    print("SMOKE OK")


def main(data_dir):
    print("L3 main", time.strftime("%Y-%m-%d %H:%M:%S %z"))
    assert_sources()
    paths = {k: os.path.join(data_dir, k) for k in (F_SITES, F_EXONNUC, F_PANEL)}
    assert os.path.getsize(paths[F_SITES]) == SIZE_SITES, "sites VCF size differs from the registered release"
    assert os.path.getsize(paths[F_EXONNUC]) == SIZE_EXONNUC, "exonNuc size differs from the registered release"
    assert sha256(paths[F_PANEL]) == PANEL_SHA, "panel sha256 differs"
    for k, p in paths.items():
        print("input %s sha256 %s size %d" % (k, sha256(p), os.path.getsize(p)))
    sys.stdout.flush()
    prefix = os.path.join(RAW, "l3_counts")
    qc = count(paths[F_EXONNUC], paths[F_SITES], paths[F_PANEL], prefix)
    print("count QC:", json.dumps(qc, sort_keys=True))
    sys.stdout.flush()
    res = analyse(prefix + ".npz", json_out=os.path.join(RAW, "l3_result.json"))
    report(res)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["smoke", "count", "analyse", "main"])
    ap.add_argument("args", nargs="*")
    ap.add_argument("--boot", type=int, default=N_BOOT)
    ap.add_argument("--json", default=None)
    a = ap.parse_args()
    if a.mode == "smoke":
        smoke()
    elif a.mode == "count":
        qc = count(*a.args)
        print(json.dumps(qc, sort_keys=True))
    elif a.mode == "analyse":
        res = analyse(a.args[0], n_boot=a.boot, json_out=a.json)
        report(res)
    elif a.mode == "main":
        main(a.args[0])

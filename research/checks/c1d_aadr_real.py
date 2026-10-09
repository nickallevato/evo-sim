"""C1d -- Day's aDNA "21" statistic (Z18525185) computed on the REAL AADR genotypes, plus a replication of keruru's
measured temporal Ne (B2e / C5b).

THROWAWAY research check.  Heavy: runs on na-workhorse, never on the workstation (the genotypes live only there).
    research/.venv/bin/python -I research/checks/c1d_aadr_real.py selftest              # synthetic file + estimator + sim checks, seconds
    research/.venv/bin/python -I research/checks/c1d_aadr_real.py groups  <v62|v66>      # sample bookkeeping from .anno/.ind only (no genotypes)
    research/.venv/bin/python -I research/checks/c1d_aadr_real.py extract <rel> <part> <nparts> [maxsnp]   # one SNP slice -> per-SNP group counts
    research/.venv/bin/python -I research/checks/c1d_aadr_real.py runall  <rel> [nproc=6]  # nparts extract processes, then merge check
    research/.venv/bin/python -I research/checks/c1d_aadr_real.py analyse <rel>          # Day's statistic + temporal Ne tables
    research/.venv/bin/python -I research/checks/c1d_aadr_real.py sim                    # WF simulation: estimator under admixture
Environment: C1D_DATA = directory with the AADR files (default <repo>/sources/raw/aadr-geno-2026-10-09);
C1D_OUT = where the per-SNP count parts go (default C1D_DATA/derived; stays on the host, ~0.7 GB per release);
C1D_RES = where the small result tables go (default research/checks/results/raw).  Prefix c1d_.

WHY.  R4 C1c could not decide whether Day's table (22,428 "fixations", 21 after 6000 BP) is a neutral-drift/sampling
artefact or something else, because it had to MODEL the data.  Both steelman reviews of C1c said the decisive move is to
run his procedure on the genotype file itself.  Day's Z23046531 says "Analysis scripts are available from the authors at
Zenodo".  Result of the search (sources/raw/day-scripts-search-2026-10-09/): none of the 38-39 Zenodo records under
"Day, Vox" / "Athos, Claude" (files: only pdf/docx/odt/xlsx; resource type 'software' count 0) holds a script.  So the
method is re-implemented here from his verbatim text, with every ambiguity run as a labelled reading.

DAY'S METHOD, verbatim (Z18525185, sources/raw/day/zenodo-18525185.txt):
  s3.1 "We used the Allen Ancient DNA Resource (AADR) v62.0 ... We restricted analysis to European samples (n = 8,738)".
  s3.2 11 bins (BP) with n: 0-500 625 / 500-1000 688 / 1000-2000 2,093 / 2000-3000 952 / 3000-4000 980 / 4000-5000 1,141 /
       5000-6000 721 / 6000-7000 573 / 7000-8000 668 / 8000-10000 129 / 10000+ 168.
  s3.3 "For each of 1,233,013 SNPs, we calculated allele frequency in each time bin. A 'fixation event' was recorded when
       an allele that was polymorphic (<100%) in an earlier bin reached 100% frequency in a later bin.  We identified 22,428
       alleles that reached fixation between the earliest samples (Neolithic, 6000-8000 BP) and modern Europeans (<500 BP)."
  s3.4 "For each fixed allele, we traced its frequency trajectory through time to identify when it first reached 100%.
       This was determined as the oldest time bin in which the allele appeared fixed, working backward from the present."
  s4.1 "Of 22,428 alleles that reached fixation, we successfully tracked timing for 16,299 (the remainder had insufficient
       coverage in intermediate time bins)."  Profile oldest->youngest: 3,038 / 8,741 / 4,497 / 2 / 9 / 7 / 2 / 1 / 0 / 0 / 2.
  s4.3 start frequency of the fixed allele in the Neolithic: 17,762 (79.2%) at 99-100%, 4,521 (20.2%) at 95-99%, 111 (0.5%)
       at 90-95%, 34 (0.2%) below 90%.   s4.4 "Total fixations from polymorphic states: 21" (post-7000 BP; his table sums to 23
       for 6000-7000 and younger and to 21 for 5000-6000 and younger).
READINGS (each is run and labelled; none chosen by looking at the result):
  E1  eligible = modern bin 100% and the pooled 6000-8000 BP bins <100% (s3.3 sentence 2).   [primary, as C1c]
  E2  eligible = modern bin 100% and any older bin with data <100% (s3.3 sentence 1).
  E1p as E1 but the allele must also be present (>0%) in the pooled Neolithic bins (strictly "polymorphic").
  T2  date = oldest bin in which the allele is 100% (gaps allowed).                           [primary]
  T1  date = start of the unbroken terminal 100% run ending at the modern bin ("working backward from the present").
      (C1c correctness review #5: under any E rule T1 cannot put events in bins 0-2, where Day has 16,276 of 16,299, so
      T1 is excluded by his own table; run anyway.)
  m   a bin counts as observed at a site only if it has >= m called chromosomes (m = 1 base; 5, 10, 20, 50 sensitivity).
  tracked: 'all11' = observed in all 11 bins; 'inter' = observed in the intermediate bins 5000-6000 ... 500-1000 only
      (Day: "insufficient coverage in intermediate time bins"; threshold unstated).
  SNP set: all 1,233,013 (what he says) or autosomes only.
  Headline number S21 = tracked E1-T2 events dated 5000-6000 BP or younger (bins 4..10); S23 includes 6000-7000.
  Ploidy: pseudo-haploid individuals contribute 1 chromosome (calls 0/2 -> 0/1), .DG diploid individuals 2 (the C1c
  convention); "naive" = 2 per individual.  The fixation tests are identical; only the start-frequency table can differ.
SAMPLE.  C1c's rule (anno): lat 35-72, lon -25..45, minus Turkey/Armenia/Syria/Georgia/Iraq/N. Africa/Abkhazia/Russia/Crimea,
  dated; V1.  V2 = V1 restricted to ASSESSMENT containing PASS (case-insensitive).  The v62 .anno is v62.0.p1 (Dataverse
  11.0, June 2026), not the original v62.0 (Dataverse 9.0, Sept 2024; not retrievable via the API) that Day cites.  Per-bin
  n from the file is compared with Day's n; the 0-500 BP bin is short in V1 (524 vs 625) and is NOT padded here.

KERURU / B2e.  Method (sources/raw/refresh-2026-10-09/zenodo-22184713/x/adna-temporal-ne/adna-draft-1.md s1-s3, code read
  as text, never run): F = (x-y)^2/[m(1-m)] summed (ratio of sums) over autosomal SNPs, m = (x+y)/2, with
  N_e = t / [2 (F - 1/(2 S0) - 1/(2 St))], S = mean individuals called per SNP, t = bin-midpoint difference / 27 y.
  AADR v66.p1; region = Political Entity matched case-insensitively to a country regex (no UK/England in it); QC =
  ASSESSMENT contains PASS (case-insensitive) and >= 10,000 autosomal SNPs hit, moderns (date <= 100) bypass the SNP
  threshold; bins Mesolithic >8000 (no lower age limit, so Palaeolithic is included), Early Neolithic 8000-6000, Late
  Neolithic 6000-4500, Bronze Age 4500-3000, Iron/Roman 3000-1500, Medieval 1500-500, Modern <500 (bin i holds
  hi[i+1] < age <= hi[i]); midpoints (hi+lo)/2; >= 20 individuals called per SNP per bin; his reported values: BA->Med
  8,139 (F 0.007183, S 842/1,548, 1,117,492 SNPs), EN->Modern 9,835 (F 0.014339, S 865/476, 1,090,099 SNPs),
  Mesolithic 938, Late Neolithic 4,922, Bronze Age 6,933, Iron/Roman 9,792, Medieval 8,530 (all vs Early Neolithic).
  Here, in addition: (K) his formula exactly; (B) the same F with the standard allele-count sampling correction
  1/n0 + 1/nt, n = called CHROMOSOMES (a pseudo-haploid individual is one allele; Nei & Tajima 1981 / Waples 1989 write
  1/(2S) with S = diploid individuals = n/2 alleles; plugging a pseudo-haploid count into S, as his code does, halves
  the correction); (C) the Nei-Tajima Fc form, denominator (x+y)/2 - xy.  Chromosome-block jackknife (22 blocks) CIs.
  Admixture test: per-SNP ancestry informativeness s_i = Var_k(p_k)/[pbar(1-pbar)] over three source samples (WHG =
  Mesolithic European hunter-gatherers; EEF = Neolithic Turkey; Yamnaya), quintiles of s; the drift-only F is the
  intercept of F_adj against s (admixture-induced F is proportional to s; drift F is not).  Plus 5 regional strata.
  Wright: N_e = 4N/(V_k+2), V_k = 5 (Day's B2b) -> N_e/N = 0.571; keruru's census N ~ 1e7 (unsourced, his own ledger flags
  it).  Expected drift-only F for the BA->Med window under N_e = 0.571e7: t/(2 N_e) = 102/(1.14e7) = 9e-6.

WHAT EACH MODEL PREDICTS (numbers from R4-C1c.md; all on 1.06M sites, Ne = constant window size):
  Neutral drift, closed (R0): eligible 15.2k / 7.3k / 2.9k / 1.7k / 0.94k at Ne 1e4 / 2e4 / 5e4 / 1e5 / 3e5; S21 3,925 / 908 /
    120 / 32 / 8.  Replacement (R2 literature-central): eligible 8.2k..0.5k, S21 2,259 / 853 / 238 / 102 / 39.
  Day's model (clock slowed, d = 0.45): behaves as neutral at Ne/0.45 -> S21 739 at Ne 1e4; the "stasis" limit gives 0.
  C1c could not reproduce his table with any cell (0 of 44 base cells pass); only the eps = 1e-3 cells reproduced the three
  summary numbers (eligible, pre-7000 share, S21) and these failed the profile and start table.

PRE-REGISTERED PREDICTIONS (written before the main run; the smoke tests used 2-20k SNPs and checked only layout/QC, not
the statistic; probabilities are my credences):
  P1  LAYOUT/QC.  Decoded per-individual autosomal call counts correlate > 0.999 with the anno column and the median
      ratio is 1.00 +- 0.05; pseudo-haploid-labelled individuals have no heterozygous calls (het rate < 1e-4) and .DG
      individuals have het rate 0.05-0.4.  (95%)
  P2  SAMPLE.  V1 reproduces Day's per-bin n within 5% in 9 of 11 bins and totals 8,808 (C1c); 0-500 BP is the outlier.  (90%)
  P3  ELIGIBLE.  E1, m = 1, all SNPs: eligible alleles are within a factor 2 of 22,428 (11.2k-44.9k).  (50%.  Reasons: real
      AADR carries damage/contamination errors that C1c showed inflate eligible 4-27x; the base model gave 0.5k-15k.)
  P4  HEADLINE.  The same configuration gives S21 >= 105 (at least 5x Day's 21).  (60%.  C1c: thousands unless Ne >= 1e5.)
      S21 within [7, 63] (3x of 21): 25%.  S21 < 7: 15%.
  P5  EXACT REPRODUCTION.  Some configuration in the grid (E in {E1,E2,E1p}, T in {T2}, m in {1,5,10,20,50}, tracked in
      {all11, inter}, SNP set in {all, autosomes}) returns eligible within 10% of 22,428 AND S21 within +-50% of 21 AND tracked
      fraction within 0.727 +- 0.05.  (25%.  If none does, the statement is "not reproducible from the published method".)
  P6  PROFILE.  Under E1-T2 (m = 1) the pre-7000 share of tracked events is >= 0.99 (Day 0.9986).  (70%.)  The 10000+ bin
      is not the dominant bin (< 50% of tracked events; Day 18.6%), because the real 10000+ bin is mostly Upper Palaeolithic
      (median age ~15.6 kyr; C1c correctness review #2) and polymorphic at many sites.  (60%.)  The 8000-10000 BP bin is the
      plurality bin (Day 53.6%).  (45%.)
  P7  START TABLE.  Share of eligible alleles at Neolithic frequency in [99,100) is between 60% and 95% (Day 79.2%), and
      the share below 90% is <= 1% (Day 0.2%).  (60% / 75%.)  A large share of eligible alleles are Neolithic singletons
      (one copy of the other allele in the pooled Neolithic sample): >= 40%.  (60%.)
  P8  READING T1.  Puts >= 500 events in 0-500 + 500-1000 BP combined (Day: 2).  (90%.)
  P9  TRACKED.  Under all11 with m = 1 the tracked fraction is >= 0.90 (Day 0.727); only with m >= 10 or the intermediate-
      bins rule does it fall to 0.65-0.80.  (65%.)
  P10 THE 21.  Dated post-5000 BP events (E1-T2) are overwhelmingly (>= 80%) sites where the allele is a minority allele
      with sample frequency < 5% in the old (<=7000 BP) bins, i.e. sampling/low-depth, not frequency sweeps.  (65%.)
  P11 KERURU REPLICATION.  On v66 with his recipe, form (K) reproduces his BA->Med N_e within 10% (7.3k-9.0k) and EN->Modern
      within 10% (8.9k-10.8k).  (60% each.)  The numbers of SNPs (about 1.12M, 1.09M) and S (about 842/1,548 and 865/476)
      match within 10%.  (70%.)
  P12 SAMPLING CORRECTION.  Form (B) (correct 1/n for pseudo-haploid chromosomes) gives a BA->Med N_e 10-25% above (K);
      EN->Modern 3-8% above.  (80%.)  Form (C) is within 5% of (B).  (85%.)
  P13 MOLECULAR CLOCK OF THE DATA.  Anchored on Early Neolithic, form (B) N_e rises with window length as keruru reports
      (938 -> ~5,000 -> ~7,000 -> ~10,000), with the Mesolithic window below 3,000 and the others within 1.3x of his.  (55%.)
  P14 ADMIXTURE.  In EN->Modern the F of the most ancestry-informative quintile exceeds the least informative by >= 2x;
      the intercept-based drift-only N_e is >= 2x the genome-wide estimate.  (75%.)  In BA->Med the top/bottom ratio is >= 1.3x
      and the intercept N_e exceeds the genome-wide by >= 1.2x.  (60%.)
  P15 WRIGHT.  Even the drift-only (intercept) N_e for BA->Med remains < 1e5, i.e. > 50x below 0.571 N for N = 1e7: the measured
      F cannot be removed down to the 9e-6 that Wright's N_e would give.  (85%.)  Reading: F is non-drift (structure, relatives,
      sample heterogeneity) or the true N_e is far below Wright's; this data cannot tell the two apart without a model.
  P16 SIMULATION (sim).  Closed WF, N_e = 1e4, pseudo-haploid n ~ 800/1500: form (B) recovers N_e within 10%; form (K) overestimates
      F-correction deficit -> N_e biased LOW by 10-20% (BA->Med-like sizes).  A 10% ancestry pulse drives form (B) below 0.7x
      truth; the s-intercept recovers within 25%.  (70%.)

PRE-COMMIT CHECKS (inputs and layout, not results): (a) anno-level sample counts for V1 (8,808, as C1c) and for keruru's QC
(21,302 individuals with "pass" in ASSESSMENT case-insensitive and >= 10,000 hits or modern, against his 21,324); (b) the
TGENO layout of the v62 file (header "TGENO 17468 1233013", 48-byte header, high-bits-first 2-bit codes) decoded 20,000
SNPs with per-individual call counts correlating 0.989 with the anno and zero heterozygous calls in .SG/.AG individuals;
(c) selftest: synthetic TGENO/GENO round trip, the day_events logic on hand-built trajectories, and the sampling
identity E[F] = 1/n0 + 1/nt for pseudo-haploid draws (simulated F 0.001921 vs 0.001917).  The factor-2 point in P12 is
therefore analytic and confirmed by that simulation, not an independent prediction.  v62 file md5s equal the Dataverse
API values (anno 6468eb19, geno 24419bba, ind 3f23dd87, snp 50f66178); v66 md5s are checked against the published
v66.p1__files.md5sum.  The statistic was not computed on any real SNP before this commit.

Outputs: c1d_<rel>_{groups,day,ne}.json/.txt, c1d_sim.json (small count tables; no genotypes).
"""
import os
import sys
import json
import csv
import re
import math
import time
import subprocess

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DATA = os.environ.get("C1D_DATA", os.path.join(ROOT, "sources", "raw", "aadr-geno-2026-10-09"))
OUT = os.environ.get("C1D_OUT", os.path.join(DATA, "derived"))
RES = os.environ.get("C1D_RES", os.path.join(HERE, "results", "raw"))
SEED = 20261012

REL = {
    "v62": dict(stem="v62.0.p1_1240k_public", anno="v62.0.p1_1240k_public.anno"),
    "v66": dict(stem="v66.p1_1240K.aadr.patch.PUB", anno="v66.p1_1240K.aadr.PUB.anno"),
}

# ----------------------------------------------------------------------------------------------- Day's design
DAY_EDGES = [(10000, 1e9), (8000, 10000), (7000, 8000), (6000, 7000), (5000, 6000), (4000, 5000), (3000, 4000),
             (2000, 3000), (1000, 2000), (500, 1000), (0, 500)]
DAY_NAMES = ["10000+", "8000-10000", "7000-8000", "6000-7000", "5000-6000", "4000-5000", "3000-4000", "2000-3000",
             "1000-2000", "500-1000", "0-500"]
DAY_N = [168, 129, 668, 573, 721, 1141, 980, 952, 2093, 688, 625]
DAY_PROFILE = [3038, 8741, 4497, 2, 9, 7, 2, 1, 0, 0, 2]
DAY_ELIG, DAY_TRACKED = 22428, 16299
DAY_START = [79.2, 20.2, 0.5, 0.2]
NON_EUROPE = {"Turkey", "Armenia", "Syria", "Georgia", "Iraq", "Tunisia", "Algeria", "Morocco", "Abkhazia", "Russia", "Crimea"}
NB = 11

# ----------------------------------------------------------------------------------------------- keruru's design
KR_NAMES = ["Meso", "EN", "LN", "BA", "Iron", "Med", "Mod"]
KR_HI = [1e9, 8000, 6000, 4500, 3000, 1500, 500, 0]          # bin i: KR_HI[i+1] < age <= KR_HI[i]; last: age <= 500
KR_MID = [9500, 7000, 5250, 3750, 2250, 1000, 250]
KR_GEN = 27.0
KR_EU = ("Britain|Ireland|Germany|France|Spain|Italy|Poland|Czech|Hungary|Sweden|Denmark|Netherlands|Austria|Serbia|"
         "Croatia|Greece|Bulgaria|Romania|Ukraine|Russia|Portugal|Switzerland|Norway")
KR_REPORTED = {"BA-Med": dict(ne=8139, F=0.007183, S=(842, 1548), snps=1117492, t=102),
               "EN-Mod": dict(ne=9835, F=0.014339, S=(865, 476), snps=1090099, t=250),
               "EN-Meso": dict(ne=938, t=111), "EN-LN": dict(ne=4922, t=65), "EN-BA": dict(ne=6933, t=120),
               "EN-Iron": dict(ne=9792, t=176), "EN-Med": dict(ne=8530, t=222)}
REGIONS = {"Iberia": "Spain|Portugal", "CentralEur": "Germany|Austria|Czech|Poland|Hungary|Switzerland|Slovak",
           "ItalyBalkans": "Italy|Serbia|Croatia|Greece|Bulgaria|Romania|Slovenia|Albania",
           "Scandinavia": "Sweden|Denmark|Norway", "EastEur": "Russia|Ukraine|Moldova|Belarus"}


# ----------------------------------------------------------------------------------------------- annotation / groups
def fl(x):
    try:
        return float(x)
    except (ValueError, TypeError):
        return None


def load_meta(rel):
    """Return per-individual metadata aligned to the .ind rows (genotype record order)."""
    cfg = REL[rel]
    with open(os.path.join(DATA, cfg["anno"]), encoding="latin-1", newline="") as f:
        rd = csv.reader(f, delimiter="\t")
        hdr = next(rd)
        rows = [r for r in rd]

    def find(prefix, exact=False):
        for i, h in enumerate(hdr):
            hh = h.strip()
            if (hh == prefix) if exact else hh.startswith(prefix):
                return i
        raise KeyError(prefix)
    c = dict(gid=0, date=find("Date mean"), group=find("Group ID"), pol=find("Political Entity"), lat=find("Lat"),
             lon=find("Long"), hits=find("SNPs hit on autosomal targets (Computed using easystats on 1240k"),
             assess=find("ASSESSMENT", exact=True))
    ind_ids = []
    with open(os.path.join(DATA, cfg["stem"] + ".ind")) as f:
        for line in f:
            p = line.split()
            if p:
                ind_ids.append(p[0])
    pos = {}
    for i, r in enumerate(rows):
        pos.setdefault(r[0].strip(), i)
    n = len(ind_ids)
    miss = [g for g in ind_ids if g not in pos]
    if miss:
        raise RuntimeError("%d .ind ids absent from anno, e.g. %s" % (len(miss), miss[:3]))
    sel = [rows[pos[g]] for g in ind_ids]
    meta = dict(
        n=n, ids=ind_ids,
        date=np.array([np.nan if fl(r[c["date"]]) is None else fl(r[c["date"]]) for r in sel]),
        lat=np.array([np.nan if fl(r[c["lat"]]) is None else fl(r[c["lat"]]) for r in sel]),
        lon=np.array([np.nan if fl(r[c["lon"]]) is None else fl(r[c["lon"]]) for r in sel]),
        hits=np.array([np.nan if fl(r[c["hits"]]) is None else fl(r[c["hits"]]) for r in sel]),
        pol=np.array([r[c["pol"]].strip() for r in sel]), group=np.array([r[c["group"]].strip() for r in sel]),
        assess=np.array([r[c["assess"]].strip() for r in sel]),
        dip=np.array([g.endswith(".DG") for g in ind_ids]))
    return meta


def build_groups(meta):
    """Return (names, masks[K, nind] bool).  Order is part of the on-disk contract."""
    names, masks = [], []
    d, lat, lon, pol = meta["date"], meta["lat"], meta["lon"], meta["pol"]
    dated = ~np.isnan(d)
    box = dated & ~np.isnan(lat) & ~np.isnan(lon) & (lat >= 35) & (lat <= 72) & (lon >= -25) & (lon <= 45) & \
        ~np.isin(pol, list(NON_EUROPE))
    passq = np.array(["pass" in a.lower() for a in meta["assess"]])
    for tag, base in (("day1", box), ("day2", box & passq)):
        for i, (lo, hi) in enumerate(DAY_EDGES):
            names.append("%s:%s" % (tag, DAY_NAMES[i]))
            masks.append(base & (d >= lo) & (d < hi))
    # keruru: Political Entity regex, PASS, >= 10,000 SNPs hit (moderns bypass), 7 bins
    eu = np.array([re.search(KR_EU, p, re.I) is not None for p in pol])
    modern = dated & (d <= 100)
    kr_ok = dated & passq & (modern | (np.nan_to_num(meta["hits"]) >= 10000))

    def krbin(mask, label):
        for i, nm in enumerate(KR_NAMES):
            lo, hi = KR_HI[i + 1], KR_HI[i]
            sel = mask & ((d > lo) & (d <= hi) if i < 6 else (d <= hi))
            names.append("%s:%s" % (label, nm))
            masks.append(sel)
    krbin(kr_ok & eu, "kr")
    for rg, rx in REGIONS.items():
        reg = np.array([re.search(rx, p, re.I) is not None for p in pol])
        krbin(kr_ok & reg, "krreg_" + rg)
    # source samples for ancestry informativeness
    grp, hit_ok = meta["group"], np.nan_to_num(meta["hits"]) >= 20000
    outl = np.array(["_o" in g or "contam" in g.lower() for g in grp])
    whg = dated & passq & hit_ok & ~outl & np.array([("Mesolithic" in g or "WHG" in g) for g in grp]) & \
        np.isin(pol, ["Serbia", "Romania", "Germany", "France", "Spain", "Belgium", "Netherlands", "Denmark", "Sweden",
                      "Latvia", "Hungary", "Italy", "Portugal", "Switzerland", "Luxembourg", "Croatia"]) & (d > 8000)
    eef = dated & passq & hit_ok & ~outl & (pol == "Turkey") & (d > 7500) & (d < 10500) & \
        np.array([bool(re.search(r"_N($|[._-])|Neolithic", g)) for g in grp])
    yam = dated & passq & hit_ok & ~outl & np.array(["Yamnaya" in g for g in grp])
    for nm, m in (("src:WHG", whg), ("src:EEF", eef), ("src:Yam", yam)):
        names.append(nm)
        masks.append(m)
    return names, np.array(masks, dtype=bool)


# ----------------------------------------------------------------------------------------------- genotype reader
LUT = np.zeros((256, 4), dtype=np.uint8)
for _b in range(256):
    LUT[_b] = [(_b >> 6) & 3, (_b >> 4) & 3, (_b >> 2) & 3, _b & 3]


class Geno:
    """TGENO (individual-major) or GENO/PACKEDANCESTRYMAP (SNP-major).  Values: copies of the counted allele 0/1/2, 3 = missing."""

    def __init__(self, path):
        self.path = path
        with open(path, "rb") as f:
            h = f.read(64)
        txt = h.split(b"\0")[0].decode().split()
        self.kind, self.nind, self.nsnp = txt[0], int(txt[1]), int(txt[2])
        size = os.path.getsize(path)
        if self.kind == "TGENO":
            self.rec = (self.nsnp + 3) // 4
            self.header = size - self.nind * self.rec
            assert self.header >= 48, "bad TGENO inference %d" % self.header
            self.mm = np.memmap(path, dtype=np.uint8, mode="r", offset=self.header, shape=(self.nind, self.rec))
        elif self.kind == "GENO":
            self.rec = max(48, (self.nind + 3) // 4)
            assert size == self.rec * (self.nsnp + 1), "GENO size mismatch"
            self.mm = np.memmap(path, dtype=np.uint8, mode="r", offset=self.rec, shape=(self.nsnp, self.rec))
        else:
            raise RuntimeError("unknown geno kind %r" % self.kind)

    def block(self, lo, hi, rows):
        """Genotypes for SNPs [lo, hi) (lo multiple of 4) of individuals `rows` (sorted) -> uint8 (len(rows), hi-lo)."""
        assert lo % 4 == 0
        if self.kind == "TGENO":
            sub = np.asarray(self.mm[rows, lo // 4:(hi + 3) // 4])
            return LUT[sub].reshape(len(rows), -1)[:, :hi - lo]
        sub = np.asarray(self.mm[lo:hi, :(self.nind + 3) // 4])
        G = LUT[sub].reshape(hi - lo, -1)[:, :self.nind]
        return np.ascontiguousarray(G[:, rows].T)


def load_snp(rel):
    chrom, ids, pos = [], [], []
    with open(os.path.join(DATA, REL[rel]["stem"] + ".snp")) as f:
        for line in f:
            p = line.split()
            if p:
                ids.append(p[0])
                chrom.append(int(p[1]))
                pos.append(int(p[3]))
    return np.array(ids), np.array(chrom), np.array(pos)


# ----------------------------------------------------------------------------------------------- extract
def group_matrix(masks, dip, sel):
    """B[2K, nsel] float32: row 2k = group k pseudo-haploid members, 2k+1 = diploid members."""
    K = masks.shape[0]
    B = np.zeros((2 * K, len(sel)), dtype=np.float32)
    for k in range(K):
        m = masks[k][sel]
        B[2 * k] = (m & ~dip[sel])
        B[2 * k + 1] = (m & dip[sel])
    return B


def extract(rel, part, nparts, maxsnp=None, geno_path=None, out_dir=None, quiet=False):
    meta = load_meta(rel)
    names, masks = build_groups(meta)
    sel = np.where(masks.any(axis=0))[0]
    cfg = REL[rel]
    g = Geno(geno_path or os.path.join(DATA, cfg["stem"] + ".geno"))
    assert g.nind == meta["n"], (g.nind, meta["n"])
    _, chrom, _ = load_snp(rel)
    nsnp = g.nsnp if maxsnp is None else min(maxsnp, g.nsnp)
    assert len(chrom) == g.nsnp
    BL = 1024
    nblk = (nsnp + BL - 1) // BL
    per = (nblk + nparts - 1) // nparts
    lo = min(part * per * BL, nsnp)
    hi = min((part + 1) * per * BL, nsnp)
    B = group_matrix(masks, meta["dip"], sel)
    Kp = B.shape[0]
    outn = np.zeros((hi - lo, Kp), dtype=np.uint16)
    outd = np.zeros((hi - lo, Kp), dtype=np.uint16)
    ind_called = np.zeros(len(sel), dtype=np.int64)
    ind_het = np.zeros(len(sel), dtype=np.int64)
    t0 = time.time()
    for blo in range(lo, hi, BL):
        bhi = min(blo + BL, hi)
        G = g.block(blo, bhi, sel)
        called = G < 3
        auto = chrom[blo:bhi] <= 22
        ind_called += called[:, auto].sum(axis=1)
        ind_het += (G[:, auto] == 1).sum(axis=1)
        Fm = called.astype(np.float32)
        Dm = np.where(called, G, 0).astype(np.float32)
        outn[blo - lo:bhi - lo] = np.rint(B @ Fm).T.astype(np.uint16)
        outd[blo - lo:bhi - lo] = np.rint(B @ Dm).T.astype(np.uint16)
        if not quiet and ((blo - lo) // BL) % 20 == 0:
            print("  part %d  %d/%d  %.0fs" % (part, blo - lo, hi - lo, time.time() - t0), flush=True)
    od = out_dir or OUT
    os.makedirs(od, exist_ok=True)
    fn = os.path.join(od, "c1d_%s_part%d.npz" % (rel, part))
    np.savez(fn, lo=lo, hi=hi, n=outn, d=outd, sel=sel, ind_called=ind_called, ind_het=ind_het,
             names=np.array(names))
    return fn


def runall(rel, nproc=6):
    procs = []
    for k in range(nproc):
        procs.append(subprocess.Popen([sys.executable, "-I", os.path.abspath(__file__), "extract", rel, str(k), str(nproc)]))
    rc = [p.wait() for p in procs]
    print("extract exit codes", rc)
    if any(rc):
        sys.exit(1)


def load_counts(rel):
    parts = []
    k = 0
    while os.path.exists(os.path.join(OUT, "c1d_%s_part%d.npz" % (rel, k))):
        parts.append(np.load(os.path.join(OUT, "c1d_%s_part%d.npz" % (rel, k))))
        k += 1
    assert parts, "no parts"
    N = np.concatenate([p["n"] for p in parts])
    D = np.concatenate([p["d"] for p in parts])
    sel = parts[0]["sel"]
    names = [str(x) for x in parts[0]["names"]]
    ic = sum(p["ind_called"] for p in parts)
    ih = sum(p["ind_het"] for p in parts)
    return N, D, names, sel, ic, ih


class Counts:
    """Per-group per-SNP counts.  chromosomes: ph=1, dip=2 (true); individual weighting for keruru's form."""

    def __init__(self, N, D, names):
        self.N, self.D, self.idx = N, D, {n: i for i, n in enumerate(names)}

    def raw(self, name):
        k = self.idx[name]
        return (self.N[:, 2 * k].astype(np.int32), self.N[:, 2 * k + 1].astype(np.int32),
                self.D[:, 2 * k].astype(np.int32), self.D[:, 2 * k + 1].astype(np.int32))

    def chrom(self, name):
        nph, ndip, dph, ddip = self.raw(name)
        return nph + 2 * ndip, (dph // 2 + ddip)

    def indiv(self, name):
        nph, ndip, dph, ddip = self.raw(name)
        return nph + ndip, dph + ddip

    def naive(self, name):
        nph, ndip, dph, ddip = self.raw(name)
        return 2 * (nph + ndip), dph + ddip


# ----------------------------------------------------------------------------------------------- Day's statistic
def day_events(n, r, elig="E1", date="T2", m=1, tracked="all11", snpmask=None, ret_idx=False):
    """n, r: (11, S) chromosome counts (called, counted-allele).  Returns dict of results for BOTH alleles stacked.

    Allele a in {counted, other}.  obs[b] = n[b] >= m.  fixed[b] = obs & (k == n).  See module docstring for E/T/tracked."""
    S = n.shape[1]
    obs = n >= m
    res = dict(eligible=0, tracked=0, hist=np.zeros(NB, dtype=np.int64), hist_untracked=np.zeros(NB, dtype=np.int64),
               start=np.zeros(4, dtype=np.int64), singleton=np.zeros(5, dtype=np.int64))
    sites_keep = np.ones(S, dtype=bool) if snpmask is None else snpmask
    idx_list = []
    for allele in (0, 1):
        k = r if allele == 0 else (n - r)
        fixed = obs & (k == n)
        neo_n = n[2] + n[3]
        neo_k = k[2] + k[3]
        # Neolithic pooled observation: sum counts of bins that are individually observed (m applies to the pooled sum)
        neo_obs = neo_n >= m
        neo_f = np.where(neo_n > 0, neo_k / np.maximum(neo_n, 1), 0.0)
        mod_fixed = fixed[10]
        if elig == "E1":
            e = mod_fixed & neo_obs & (neo_k < neo_n)
        elif elig == "E1p":
            e = mod_fixed & neo_obs & (neo_k < neo_n) & (neo_k > 0)
        elif elig == "E2":
            older = obs[:10] & (k[:10] < n[:10])
            e = mod_fixed & older.any(axis=0)
        else:
            raise ValueError(elig)
        e &= sites_keep
        if tracked == "all11":
            tr = obs.all(axis=0)
        elif tracked == "inter":
            tr = obs[4:10].all(axis=0)
        else:
            tr = np.ones(S, dtype=bool)
        if date == "T2":
            dt = np.argmax(fixed, axis=0)         # oldest fixed bin (always exists because bin 10 is fixed)
        else:
            dt = np.full(S, 10)
            alive = np.ones(S, dtype=bool)
            for b in range(9, -1, -1):
                f_b = fixed[b]
                # observed and not fixed -> run ends; unobserved -> skipped
                brk = alive & obs[b] & ~f_b
                alive &= ~brk
                dt = np.where(alive & f_b, b, dt)
        ie = np.where(e)[0]
        res["eligible"] += int(e.sum())
        res["tracked"] += int((e & tr).sum())
        res["hist"] += np.bincount(dt[e & tr], minlength=NB)
        res["hist_untracked"] += np.bincount(dt[e & ~tr], minlength=NB)
        f_neo = neo_f[ie]
        res["start"] += np.array([(f_neo >= 0.99).sum(), ((f_neo >= 0.95) & (f_neo < 0.99)).sum(),
                                  ((f_neo >= 0.90) & (f_neo < 0.95)).sum(), (f_neo < 0.90).sum()])
        minor = (neo_n - neo_k)[ie]
        res["singleton"] += np.array([(minor == 1).sum(), (minor == 2).sum(), ((minor >= 3) & (minor <= 5)).sum(),
                                      ((minor >= 6) & (minor <= 10)).sum(), (minor > 10).sum()])
        if ret_idx:
            idx_list.append((allele, ie, dt[ie], tr[ie]))
    if ret_idx:
        res["idx"] = idx_list
    return res


def summarise_day(res):
    h = res["hist"]
    tot = int(h.sum())
    pre7 = int(h[:3].sum())
    return dict(eligible=res["eligible"], tracked=res["tracked"],
                tracked_frac=(res["tracked"] / res["eligible"]) if res["eligible"] else None,
                profile=[int(x) for x in h], pre7000_share=(pre7 / tot) if tot else None,
                S21=int(h[4:].sum()), S23=int(h[3:].sum()), share_10000plus=(h[0] / tot) if tot else None,
                share_8000_10000=(h[1] / tot) if tot else None,
                young_0_1000=int(h[9:].sum()),
                start_pct=[100.0 * x / max(1, res["eligible"]) for x in res["start"]],
                singleton=[int(x) for x in res["singleton"]])


def day_analysis(rel, cnt, snp_ids, chrom, pos, meta_n):
    out = {"rel": rel, "bins": DAY_NAMES, "day": dict(n=DAY_N, profile=DAY_PROFILE, eligible=DAY_ELIG, tracked=DAY_TRACKED,
                                                      start=DAY_START)}
    # sample sizes
    ns = {}
    for tag in ("day1", "day2"):
        ph, dp, chr_med = [], [], []
        for nm in DAY_NAMES:
            a, b, _, _ = cnt.raw("%s:%s" % (tag, nm))
            # n individuals at SNP level is not group size; group size is from the groups stage
            ph.append(float(np.median(a))), dp.append(float(np.median(b)))
        ns[tag] = dict(med_called_ph=ph, med_called_dip=dp)
    out["called_median"] = ns
    auto = chrom <= 22
    grid = []
    for tag in ("day1", "day2"):
        n = np.zeros((NB, len(chrom)), dtype=np.int32)
        r = np.zeros((NB, len(chrom)), dtype=np.int32)
        for i, nm in enumerate(DAY_NAMES):
            n[i], r[i] = cnt.chrom("%s:%s" % (tag, nm))
        combos = [(e, d, m, tr, sn) for e in ("E1", "E2", "E1p") for d in ("T2", "T1") for m in (1, 5, 10, 20, 50)
                  for tr in ("all11", "inter") for sn in ("all", "auto")]
        if tag == "day2":
            combos = [(e, d, m, tr, sn) for e in ("E1",) for d in ("T2", "T1") for m in (1, 10, 20) for tr in ("all11", "inter")
                      for sn in ("all",)]
        for (e, d, m, tr, sn) in combos:
            res = day_events(n, r, e, d, m, tr, None if sn == "all" else auto)
            s = summarise_day(res)
            s.update(sample=tag, elig_rule=e, date_rule=d, m=m, tracked_rule=tr, snpset=sn)
            grid.append(s)
        if tag == "day1":
            # start table under the naive 2-chromosome weighting, E1-T2-m1-all
            n2 = np.zeros((NB, len(chrom)), dtype=np.int32)
            r2 = np.zeros((NB, len(chrom)), dtype=np.int32)
            for i, nm in enumerate(DAY_NAMES):
                n2[i], r2[i] = cnt.naive("%s:%s" % (tag, nm))
            s = summarise_day(day_events(n2, r2, "E1", "T2", 1, "all11"))
            s.update(sample=tag + "-naive2", elig_rule="E1", date_rule="T2", m=1, tracked_rule="all11", snpset="all")
            grid.append(s)
            # the post-7000 events, headline configuration
            res = day_events(n, r, "E1", "T2", 1, "all11", None, ret_idx=True)
            ev = []
            for (allele, ie, dt, tr) in res["idx"]:
                for j in range(len(ie)):
                    if tr[j] and dt[j] >= 3:
                        i = ie[j]
                        k = r[:, i] if allele == 0 else (n[:, i] - r[:, i])
                        ev.append(dict(snp=str(snp_ids[i]), chr=int(chrom[i]), pos=int(pos[i]), bin=DAY_NAMES[dt[j]],
                                       allele="counted" if allele == 0 else "other",
                                       n=[int(x) for x in n[:, i]], k=[int(x) for x in k[:]]))
            out["events_post6000"] = ev
    out["grid"] = grid
    return out


def fmt_day(out):
    L = []
    L.append("== Day statistic on real AADR %s ==" % out["rel"])
    L.append("Day: eligible %d tracked %d profile %s start %s" % (DAY_ELIG, DAY_TRACKED, DAY_PROFILE, DAY_START))
    L.append("%-5s %-4s %-3s %3s %-6s %-5s | %8s %7s %6s | %s | pre7k  S21 S23 | start%% [99,100) [95,99) [90,95) <90 | singleton 1/2/3-5/6-10/>10" % (
        "samp", "E", "T", "m", "trk", "snps", "elig", "tracked", "frac", "profile (10000+ ... 0-500)"))
    for s in out["grid"]:
        L.append("%-5s %-4s %-3s %3d %-6s %-5s | %8d %7d %6.3f | %s | %6.4f %4d %4d | %s | %s" % (
            s["sample"], s["elig_rule"], s["date_rule"], s["m"], s["tracked_rule"], s["snpset"], s["eligible"], s["tracked"],
            s["tracked_frac"] or 0, "/".join(str(x) for x in s["profile"]), s["pre7000_share"] or 0, s["S21"], s["S23"],
            "/".join("%.1f" % x for x in s["start_pct"]), "/".join(str(x) for x in s["singleton"])))
    return "\n".join(L)


# ----------------------------------------------------------------------------------------------- temporal Ne
def ne_pair(cnt, ga, gb, t_gen, chrom, form="B", min_called=20, snpmask=None, extra_mask=None, s_weight=None):
    """Temporal Ne between groups ga (earlier) and gb.  forms: K (keruru exactly), B (allele-count correction), C (Fc)."""
    auto = chrom <= 22
    if form == "K":
        na, ka = cnt.indiv(ga)
        nb, kb = cnt.indiv(gb)
        x = np.where(na > 0, ka / np.maximum(2 * na, 1), 0.0)
        y = np.where(nb > 0, kb / np.maximum(2 * nb, 1), 0.0)
        nca, ncb = na, nb
    else:
        na, ka = cnt.chrom(ga)
        nb, kb = cnt.chrom(gb)
        x = np.where(na > 0, ka / np.maximum(na, 1), 0.0)
        y = np.where(nb > 0, kb / np.maximum(nb, 1), 0.0)
    m = (x + y) / 2.0
    ok = auto & (na >= min_called) & (nb >= min_called) & (m > 0) & (m < 1)
    if snpmask is not None:
        ok &= snpmask
    if extra_mask is not None:
        ok &= extra_mask
    d2 = (x - y) ** 2
    den = m * (1 - m) if form != "C" else (m - x * y)
    if form == "K":
        corr_site = None
    else:
        corr_site = den * (1.0 / np.maximum(na, 1) + 1.0 / np.maximum(nb, 1))
    chs = chrom[ok]
    out = {}
    nums = np.bincount(chs, weights=d2[ok], minlength=23)[1:23]
    dens = np.bincount(chs, weights=den[ok], minlength=23)[1:23]
    if form == "K":
        Sa, Sb = float(na[ok].mean()), float(nb[ok].mean())
        cor_tot = None
        corr = 1.0 / (2 * Sa) + 1.0 / (2 * Sb)
    else:
        cors = np.bincount(chs, weights=corr_site[ok], minlength=23)[1:23]
        corr = float(cors.sum() / dens.sum())
        Sa, Sb = float(na[ok].mean()), float(nb[ok].mean())

    def ne_from(nu, de, co=None):
        F = nu / de
        c = corr if co is None else co
        Fa = F - c
        return (t_gen / (2 * Fa)) if Fa > 0 else float("nan"), F, c
    ne, F, c = ne_from(nums.sum(), dens.sum())
    # jackknife over chromosomes
    je = []
    for ch in range(22):
        if dens[ch] <= 0:
            continue
        nu, de = nums.sum() - nums[ch], dens.sum() - dens[ch]
        co = None
        if form != "K":
            co = (cors.sum() - cors[ch]) / de
        v, _, _ = ne_from(nu, de, co)
        je.append(v)
    je = np.array([v for v in je if not math.isnan(v)])
    if len(je) > 5:
        # jackknife of Fadj (more stable than Ne), then delta method to Ne
        Fadjs = np.array([(t_gen / (2 * v)) for v in je])
        Fa_all = t_gen / (2 * ne) if ne == ne else float("nan")
        nj = len(Fadjs)
        se_F = math.sqrt((nj - 1) / nj * np.sum((Fadjs - Fadjs.mean()) ** 2))
        lo_ = t_gen / (2 * (Fa_all + 1.96 * se_F)) if Fa_all - 1.96 * se_F > 0 else float("nan")
        hi_ = t_gen / (2 * (Fa_all - 1.96 * se_F)) if Fa_all - 1.96 * se_F > 0 else float("inf")
        out["ci95"] = [lo_, hi_]
    out.update(ne=ne, F=F, corr=c, F_adj=F - c, t_gen=t_gen, n_snp=int(ok.sum()), S=[Sa, Sb], form=form,
               power=(min(Sa, Sb) / (10 * ne / t_gen)) if ne == ne and ne > 0 else None)
    return out


def informativeness(cnt, chrom, min_n=6):
    ps, ns = [], []
    for nm in ("src:WHG", "src:EEF", "src:Yam"):
        n, k = cnt.chrom(nm)
        ps.append(np.where(n > 0, k / np.maximum(n, 1), np.nan))
        ns.append(n)
    P = np.array(ps)
    ok = np.all(np.array(ns) >= min_n, axis=0)
    pbar = np.nanmean(P, axis=0)
    var = np.nanmean((P - pbar) ** 2, axis=0)
    s = np.where(ok & (pbar > 0) & (pbar < 1), var / (pbar * (1 - pbar)), np.nan)
    return s


def ne_stratified(cnt, ga, gb, t_gen, chrom, s, nq=5):
    ok0 = ~np.isnan(s)
    qs = np.nanquantile(s[ok0], np.linspace(0, 1, nq + 1))
    rows = []
    for i in range(nq):
        msk = ok0 & (s >= qs[i]) & (s <= qs[i + 1] if i == nq - 1 else s < qs[i + 1])
        r = ne_pair(cnt, ga, gb, t_gen, chrom, "B", extra_mask=msk)
        rows.append(dict(q=i + 1, s_mean=float(np.nanmean(s[msk])), n_snp=r["n_snp"], F=r["F"], corr=r["corr"],
                         F_adj=r["F_adj"], ne=r["ne"]))
    x = np.array([r["s_mean"] for r in rows])
    y = np.array([r["F_adj"] for r in rows])
    A = np.vstack([np.ones_like(x), x]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    a0, slope = float(coef[0]), float(coef[1])
    return dict(rows=rows, intercept=a0, slope=slope, ne_intercept=(t_gen / (2 * a0)) if a0 > 0 else float("inf"),
                top_over_bottom=(rows[-1]["F_adj"] / rows[0]["F_adj"]) if rows[0]["F_adj"] > 0 else float("nan"))


def ne_analysis(rel, cnt, chrom):
    out = {"rel": rel, "kr_reported": KR_REPORTED}
    mid = dict(zip(KR_NAMES, KR_MID))
    pairs = [("BA", "Med"), ("EN", "Mod"), ("Meso", "EN"), ("EN", "LN"), ("EN", "BA"), ("EN", "Iron"), ("EN", "Med"),
             ("LN", "BA"), ("BA", "Iron"), ("Iron", "Med"), ("Med", "Mod")]
    tab = []
    for a, b in pairs:
        t = abs(mid[a] - mid[b]) / KR_GEN
        row = dict(pair="%s-%s" % (a, b), t_gen=t)
        for form in ("K", "B", "C"):
            row[form] = ne_pair(cnt, "kr:" + a, "kr:" + b, t, chrom, form)
        tab.append(row)
    out["pairs"] = tab
    # generation-time sensitivity for the two headline windows
    out["gen_sens"] = {}
    for a, b in (("BA", "Med"), ("EN", "Mod")):
        out["gen_sens"]["%s-%s" % (a, b)] = {str(gy): ne_pair(cnt, "kr:" + a, "kr:" + b, abs(mid[a] - mid[b]) / gy, chrom, "B")["ne"]
                                             for gy in (25, 27, 29, 31)}
    # stratification by ancestry informativeness
    s = informativeness(cnt, chrom)
    out["informativeness_n_snp"] = int(np.sum(~np.isnan(s)))
    out["strat"] = {}
    for a, b in (("BA", "Med"), ("EN", "Mod"), ("EN", "BA"), ("EN", "Med"), ("LN", "BA")):
        out["strat"]["%s-%s" % (a, b)] = ne_stratified(cnt, "kr:" + a, "kr:" + b, abs(mid[a] - mid[b]) / KR_GEN, chrom, s)
    # regions
    out["regions"] = {}
    for rg in REGIONS:
        out["regions"][rg] = {}
        for a, b in (("BA", "Med"), ("EN", "Mod"), ("EN", "BA")):
            t = abs(mid[a] - mid[b]) / KR_GEN
            try:
                r = ne_pair(cnt, "krreg_%s:%s" % (rg, a), "krreg_%s:%s" % (rg, b), t, chrom, "B")
            except Exception as ex:                                   # noqa: BLE001
                r = dict(error=str(ex))
            out["regions"][rg]["%s-%s" % (a, b)] = r
    return out


def fmt_ne(o):
    L = ["== Temporal Ne, %s ==" % o["rel"], "pair      t_gen | K (keruru) Ne  F  corr  Sa/Sb  nSNP | B (allele-count corr) Ne [95%% CI]  corr | C (Fc) Ne"]
    for r in o["pairs"]:
        K, B, C = r["K"], r["B"], r["C"]
        L.append("%-8s %6.1f | %8.0f %.6f %.6f %.0f/%.0f %8d | %8.0f [%s] %.6f | %8.0f" % (
            r["pair"], r["t_gen"], K["ne"], K["F"], K["corr"], K["S"][0], K["S"][1], K["n_snp"], B["ne"],
            "%.0f-%.0f" % tuple(B["ci95"]) if "ci95" in B else "-", B["corr"], C["ne"]))
    L.append("keruru reported: " + json.dumps(o["kr_reported"]))
    L.append("generation-time sensitivity (form B): " + json.dumps(o["gen_sens"]))
    L.append("-- ancestry informativeness quintiles (form B), %d SNPs with all three sources --" % o["informativeness_n_snp"])
    for k, v in o["strat"].items():
        L.append("%s: intercept F %.6f slope %.4f -> drift-only Ne %.0f ; top/bottom F_adj %.2f" % (
            k, v["intercept"], v["slope"], v["ne_intercept"], v["top_over_bottom"]))
        for r in v["rows"]:
            L.append("    q%d  s %.4f  nSNP %d  F %.6f  F_adj %.6f  Ne %.0f" % (r["q"], r["s_mean"], r["n_snp"], r["F"], r["F_adj"], r["ne"]))
    L.append("-- regions (form B) --")
    for rg, d in o["regions"].items():
        for k, r in d.items():
            if "error" in r:
                L.append("%-13s %-7s error %s" % (rg, k, r["error"]))
            else:
                L.append("%-13s %-7s Ne %8.0f  F %.5f corr %.5f  S %.0f/%.0f  nSNP %d" % (rg, k, r["ne"], r["F"], r["corr"], r["S"][0], r["S"][1], r["n_snp"]))
    return "\n".join(L)


# ----------------------------------------------------------------------------------------------- QC / groups
def groups_report(rel):
    meta = load_meta(rel)
    names, masks = build_groups(meta)
    rows = []
    for nm, mk in zip(names, masks):
        rows.append(dict(name=nm, n=int(mk.sum()), n_dip=int((mk & meta["dip"]).sum())))
    return meta, names, masks, rows


def qc_report(rel):
    meta = load_meta(rel)
    N, D, names, sel, ic, ih = load_counts(rel)
    hits = meta["hits"][sel]
    ok = ~np.isnan(hits) & (hits > 1000)
    r = ic[ok] / hits[ok]
    dip = meta["dip"][sel]
    hetrate = ih / np.maximum(ic, 1)
    q = dict(n_indiv=int(len(sel)), corr=float(np.corrcoef(ic[ok], hits[ok])[0, 1]), ratio_median=float(np.median(r)),
             ratio_iqr=[float(np.quantile(r, .25)), float(np.quantile(r, .75))],
             het_ph_median=float(np.median(hetrate[~dip & (ic > 1000)])), het_ph_max=float(np.max(hetrate[~dip & (ic > 1000)])),
             n_ph_with_het_gt_1e3=int(np.sum((~dip) & (ic > 20000) & (hetrate > 1e-3))),
             het_dip_median=float(np.median(hetrate[dip & (ic > 1000)])) if np.any(dip & (ic > 1000)) else None,
             n_dip=int(dip.sum()), n_dip_with_het_lt_0p01=int(np.sum(dip & (ic > 20000) & (hetrate < 0.01))))
    return q


def analyse(rel):
    os.makedirs(RES, exist_ok=True)
    N, D, names, sel, ic, ih = load_counts(rel)
    cnt = Counts(N, D, names)
    ids, chrom, pos = load_snp(rel)
    assert len(chrom) == N.shape[0], (len(chrom), N.shape)
    meta, gnames, gmasks, grows = groups_report(rel)
    assert gnames == names
    q = qc_report(rel)
    with open(os.path.join(RES, "c1d_%s_groups.json" % rel), "w") as f:
        json.dump(dict(groups=grows, qc=q), f, indent=1)
    print("QC", json.dumps(q))
    day = day_analysis(rel, cnt, ids, chrom, pos, meta["n"])
    day["groups"] = {r["name"]: r["n"] for r in grows if r["name"].startswith(("day1", "day2"))}
    with open(os.path.join(RES, "c1d_%s_day.json" % rel), "w") as f:
        json.dump(day, f, indent=1)
    with open(os.path.join(RES, "c1d_%s_day.txt" % rel), "w") as f:
        f.write("group n (V1): " + str([r["n"] for r in grows if r["name"].startswith("day1")]) + "  Day: " + str(DAY_N) + "\n")
        f.write(fmt_day(day) + "\n")
    print(open(os.path.join(RES, "c1d_%s_day.txt" % rel)).read()[:3000])
    ne = ne_analysis(rel, cnt, chrom)
    with open(os.path.join(RES, "c1d_%s_ne.json" % rel), "w") as f:
        json.dump(ne, f, indent=1, default=float)
    with open(os.path.join(RES, "c1d_%s_ne.txt" % rel), "w") as f:
        f.write("group n (kr): " + str([r["n"] for r in grows if r["name"].startswith("kr:")]) + "\n")
        f.write(fmt_ne(ne) + "\n")
    print(open(os.path.join(RES, "c1d_%s_ne.txt" % rel)).read())


# ----------------------------------------------------------------------------------------------- simulation of the estimator
def sim_ne(rng, ne_true=10000, t=100, nloci=200000, n_a=800, n_b=1500, pulse=0.0, src_gens=700):
    """Closed (pulse=0) or admixed WF population; pseudo-haploid sampling at generation 0 and t.  Pulse of fraction `pulse`
    from a source that drifted `src_gens` generations (Ne 1e4) from the same ancestor, at generation t/2."""
    p = rng.random(nloci)
    q = p.copy()
    for _ in range(src_gens):
        q = rng.binomial(20000, q) / 20000.0
    p0 = p.copy()
    # equilibrate the focal population a little so x0 is not the ancestral value exactly: none (x0 = p at time 0)
    x = rng.binomial(n_a, p) / n_a
    for g in range(t):
        p = rng.binomial(2 * ne_true, p) / (2.0 * ne_true)
        if pulse > 0 and g == t // 2:
            p = (1 - pulse) * p + pulse * q
    y = rng.binomial(n_b, p) / n_b
    m = (x + y) / 2
    ok = (m > 0) & (m < 1)
    F = np.sum((x - y)[ok] ** 2) / np.sum((m * (1 - m))[ok])
    cK = 1 / (2 * n_a) + 1 / (2 * n_b)
    cB = 1 / n_a + 1 / n_b
    neK, neB = t / (2 * (F - cK)), t / (2 * (F - cB))
    # informativeness from the TRUE source difference (optimistic)
    pbar = (p0 + q) / 2
    s = (p0 - q) ** 2 / 2 / np.maximum(pbar * (1 - pbar), 1e-9)
    edges = np.quantile(s[ok], np.linspace(0, 1, 6))
    xs, ys = [], []
    for i in range(5):
        mk = ok & (s >= edges[i]) & (s <= edges[i + 1])
        Fi = np.sum((x - y)[mk] ** 2) / np.sum((m * (1 - m))[mk]) - cB
        xs.append(np.mean(s[mk])), ys.append(Fi)
    A = np.vstack([np.ones(5), xs]).T
    coef, *_ = np.linalg.lstsq(A, np.array(ys), rcond=None)
    ne_int = t / (2 * coef[0]) if coef[0] > 0 else float("inf")
    return dict(ne_true=ne_true, pulse=pulse, F=float(F), neK=float(neK), neB=float(neB), ne_intercept=float(ne_int),
                ratio_K=float(neK / ne_true), ratio_B=float(neB / ne_true), ratio_int=float(ne_int / ne_true))


def run_sim():
    rng = np.random.default_rng(SEED)
    out = []
    for pulse in (0.0, 0.02, 0.05, 0.10, 0.20, 0.40):
        reps = [sim_ne(rng, pulse=pulse) for _ in range(5)]
        row = dict(pulse=pulse)
        for k in ("F", "neK", "neB", "ne_intercept", "ratio_K", "ratio_B", "ratio_int"):
            row[k] = float(np.mean([r[k] for r in reps]))
            row[k + "_sd"] = float(np.std([r[k] for r in reps]))
        out.append(row)
        print("pulse %.2f  F %.5f  K %.2f  B %.2f  intercept %.2f  (ratio to true Ne)" % (pulse, row["F"], row["ratio_K"], row["ratio_B"], row["ratio_int"]), flush=True)
    # larger Ne (Wright-like) closed: how big would F be?
    for nt in (30000, 100000):
        r = [sim_ne(rng, ne_true=nt) for _ in range(3)]
        out.append(dict(ne_true=nt, pulse=0.0, ratio_B=float(np.mean([x["ratio_B"] for x in r])), ratio_K=float(np.mean([x["ratio_K"] for x in r])),
                        F=float(np.mean([x["F"] for x in r]))))
        print("Ne %d closed: B ratio %.2f" % (nt, out[-1]["ratio_B"]))
    os.makedirs(RES, exist_ok=True)
    with open(os.path.join(RES, "c1d_sim.json"), "w") as f:
        json.dump(out, f, indent=1)


# ----------------------------------------------------------------------------------------------- selftest
def selftest():
    import tempfile
    rng = np.random.default_rng(1)
    tmp = tempfile.mkdtemp(prefix="c1d_selftest_")
    nind, nsnp = 37, 4096 + 12
    G = rng.integers(0, 4, size=(nind, nsnp)).astype(np.uint8)

    def pack(rowsN):
        L = (rowsN.shape[1] + 3) // 4
        P = np.zeros((rowsN.shape[0], L * 4), dtype=np.uint8)
        P[:, :rowsN.shape[1]] = rowsN
        P = P.reshape(rowsN.shape[0], L, 4)
        return ((P[:, :, 0] << 6) | (P[:, :, 1] << 4) | (P[:, :, 2] << 2) | P[:, :, 3]).astype(np.uint8)
    pt = os.path.join(tmp, "t.geno")
    with open(pt, "wb") as f:
        h = ("TGENO %d %d 0 0" % (nind, nsnp)).encode()
        f.write(h + b"\0" * (48 - len(h)))
        f.write(pack(G).tobytes())
    ps = os.path.join(tmp, "s.geno")
    rl = max(48, (nind + 3) // 4)
    with open(ps, "wb") as f:
        h = ("GENO %d %d 0 0" % (nind, nsnp)).encode()
        f.write(h + b"\0" * (rl - len(h)))
        body = pack(G.T)
        f.write(np.hstack([body, np.zeros((nsnp, rl - body.shape[1]), dtype=np.uint8)]).tobytes())
    rows = np.array([0, 3, 5, 6, 20, 36])
    for p in (pt, ps):
        gg = Geno(p)
        for lo, hi in ((0, 1024), (1024, 4096 + 12), (4096, 4108)):
            B = gg.block(lo, hi, rows)
            assert np.array_equal(B, G[rows][:, lo:hi]), (p, lo, hi)
    print("reader ok (TGENO and GENO)")
    # day_events logic on a hand-built example (m=1): 11 bins, one SNP each
    def mk(ks, ns):
        return np.array(ns, dtype=np.int32).reshape(NB, 1), np.array(ks, dtype=np.int32).reshape(NB, 1)
    # allele "counted": polymorphic in bins 0..4, 100% from bin 5 on; Neolithic bins <100%
    n = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    k = [5, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10]
    n_, r_ = mk(k, n)
    res = day_events(n_, r_, "E1", "T2", 1, "all11")
    assert res["eligible"] == 1 and res["hist"][5] == 1 and res["hist"].sum() == 1, res["hist"]
    res = day_events(n_, r_, "E1", "T1", 1, "all11")
    assert res["hist"][5] == 1
    # gap: bin 0 happens to be 100% (small sample) -> T2 dates it to bin 0, T1 to bin 5
    k = [10, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10]
    n_, r_ = mk(k, n)
    assert day_events(n_, r_, "E1", "T2", 1, "all11")["hist"][0] == 1
    assert day_events(n_, r_, "E1", "T1", 1, "all11")["hist"][5] == 1
    # other allele symmetric: counted allele at 0% in modern
    k = [5, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
    n_, r_ = mk(k, n)
    assert day_events(n_, r_, "E1", "T2", 1, "all11")["hist"][5] == 1
    # E1 excludes a site already 100% in the Neolithic
    k = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    n_, r_ = mk(k, n)
    assert day_events(n_, r_, "E1", "T2", 1, "all11")["eligible"] == 0
    # untracked: no data in one intermediate bin
    n2 = list(n)
    n2[6] = 0
    k = [5, 9, 9, 9, 9, 10, 0, 10, 10, 10, 10]
    n_, r_ = mk(k, n2)
    r1 = day_events(n_, r_, "E1", "T2", 1, "all11")
    assert r1["eligible"] == 1 and r1["tracked"] == 0
    print("day_events logic ok")
    # estimator on pure sampling noise (Ne -> huge): corrections should zero F; B correct for pseudo-haploid, K under-corrects
    nl = 400000
    p = rng.random(nl)
    na, nb = 800, 1500
    x = rng.binomial(na, p) / na
    y = rng.binomial(nb, p) / nb
    m = (x + y) / 2
    ok = (m > 0) & (m < 1)
    F = np.sum((x - y)[ok] ** 2) / np.sum((m * (1 - m))[ok])
    print("pure-sampling F %.6f ; correction B 1/na+1/nb %.6f ; K 1/(2na)+1/(2nb) %.6f" % (F, 1 / na + 1 / nb, 1 / (2 * na) + 1 / (2 * nb)))
    assert abs(F - (1 / na + 1 / nb)) < 0.1 * (1 / na + 1 / nb), "sampling expectation of F should equal 1/na + 1/nb"
    r = sim_ne(rng, nloci=100000)
    print("closed sim Ne=1e4: ratio K %.2f B %.2f" % (r["ratio_K"], r["ratio_B"]))
    print("selftest ok")


# ----------------------------------------------------------------------------------------------- main
if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "selftest"
    if cmd == "selftest":
        selftest()
    elif cmd == "groups":
        meta, names, masks, rows = groups_report(sys.argv[2])
        for r in rows:
            print("%-28s n=%5d dip=%5d" % (r["name"], r["n"], r["n_dip"]))
        print("V1 n per bin:", [r["n"] for r in rows if r["name"].startswith("day1")], "Day:", DAY_N)
    elif cmd == "extract":
        fn = extract(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]) if len(sys.argv) > 5 else None)
        print("wrote", fn)
    elif cmd == "runall":
        runall(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 6)
    elif cmd == "analyse":
        analyse(sys.argv[2])
    elif cmd == "sim":
        run_sim()
    else:
        print(__doc__)

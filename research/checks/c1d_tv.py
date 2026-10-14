"""C1d-fu (part A of check C1d-D) -- a transversion-restricted, SFS-matched neutral null for Day's aDNA "21" statistic,
and what the transition excess is.

PRE-REGISTERED (AGENTS.md rule 5).  Written 2026-10-13 before any main run.  Brief: research/checks/briefs/C1d-D-analyst.md
(read at 1a8fae4 or later).  The local smoke test below used SYNTHETIC data only; no real-data output of this script has been
seen.  Inputs that ARE already known and were looked at (they are prior results, not outputs of this script): R4-C1d.md
sections 3.3-3.5 (autosomal transversions S21 = 36 / eligible 6,306 on v62, 44 / 7,614 on v66; autosomal transitions S21 =
4,559 / eligible 47,937 on v62, 3,446 events on v66; C1c flat-SFS rates), and the C1d library/damage tests (section 3.4).

Run (always the isolated venv; everything except `selftest`/`mkfake`/`smoke` runs on na-workhorse, never on the workstation):
    research/.venv/bin/python -I research/checks/c1d_tv.py selftest                       # logic tests, tiny, synthetic
    research/.venv/bin/python -I research/checks/c1d_tv.py mkfake <out.npz> <S>            # synthetic prep file
    research/.venv/bin/python -I research/checks/c1d_tv.py smoke <prep.npz> <ncpu> [reps] [maxsites]   # full grid, real entry
    research/.venv/bin/python -I research/checks/c1d_tv.py prep <v62|v66>                  # host: counts + hg19 context
    research/.venv/bin/python -I research/checks/c1d_tv.py run <v62|v66> <ncpu> [reps]     # host: the null grid
    research/.venv/bin/python -I research/checks/c1d_tv.py analyse                         # host or local: bands
Outputs: results/raw/c1d_tv_<rel>_obs.json, c1d_tv_<rel>_null.jsonl, c1d_tv_analysis.{json,txt}; the prep files
(c1d_tv_<rel>_prep.npz, ~0.2 GB) stay in C1D_OUT on the host.

===================================================================================================================
0. TARGETS (verbatim quotes are in the quotes files; ids given, not repeated in full)
-------------------------------------------------------------------------------------------------------------------
Day side.  Z18525185 (2026-02-08) section 3.3-4.3, quotes-day Q107 (fixation-event rule), Q108 ("22,428 alleles that
  reached fixation"), Q109 (dating rule "oldest time bin in which the allele appeared fixed"), Q110 (16,299 tracked), Q111
  ("completion events for alleles already near fixation"); abstract (claim C6): "with essentially zero fixations in the
  subsequent 7,000 years"; claim C7 (Q96, 2026-09-13): "genetic drift isn't happening at all over the last 7000 years".
Critic side.  keruru's measured temporal N_e (quotes-critics RF-13 table: 6,933 BA, 8,139 BA->Medieval, 9,835 modern;
  claim C5b), KR-03 (zero fixations expected under neutrality at N_e ~ 1e4), and the audit's own C1c model, which with an
  error term predicted the thousands of post-6000 BP events within 20% (R4-C1d section 6).
The audit's own open items this check closes: R4-C1d section 3.5 ("Neutral comparison for the transversion class: open")
  and section 3.4 ("What it is ... is open"); R5-draft.md section 1.3 feeder row "C / C6 / C1c (aDNA '21')", whose flip is
  "N_e about 1e4: Day (a deficit of 70-190x). Holocene N_e at or above about 1e5: critics."
RH tags: Day's C6 abstract sentence and C7 sentence keep their existing tags (C6 dialectic; C7 reading-dependent).  This
  check scores no statement directly; it supplies the comparator both readings lack.

===================================================================================================================
1. WHAT IS COMPUTED
-------------------------------------------------------------------------------------------------------------------
Data: the per-SNP group counts that c1d_aadr_real.py already extracted on the host (C1D_OUT/c1d_<rel>_part*.npz; V1 sample =
  groups "day1:<bin>", 11 bins oldest first; Yamnaya source group "src:Yam"), the .snp files (chrom, pos, alleles) and
  the hg19 reference (NEW FETCH, own directory, see section 6).  Autosomes only (chrom 1-22), matching Z23046531's
  autosomes-only convention and the R4-C1d section 3.3 autosomal rows.
Site classes (from the .snp alleles; strand-symmetric):
  TV      = transversion (alleles not {A,G} and not {C,T}); damage-immune.
  TS-CpG  = transition at a CpG: alleles {C,T} and hg19[pos+1] == 'G', or alleles {G,A} and hg19[pos-1] == 'C'.
  TS-non  = other transitions.
Damage direction of a transition event: the allele fixed in the modern bin is C (at a C/T site) or G (at a G/A site), i.e.
  the allele LOST since the older bins is the deamination product T or A.  (5-methylcytosine deaminates to T, not U, so
  UDG/USER treatment does not remove it; non-CpG C->U damage is removed by full UDG.)
Observed statistic: c1d.day_events with E1 eligibility, T2 dating, m = 1, tracked = all 11 bins (the R4-C1d primary cell),
  per class.  S21 = events dated 5000-6000 BP or younger (bins 4..10).
REPRODUCTION GATE (asserted before anything else is computed): v62 autosomal TV S21 == 36 and eligible == 6,306; v66
  autosomal TV S21 == 44 and eligible == 7,614; v62 autosomal TS S21 == 4,559 and eligible == 47,937; v66 autosomal TS
  S21 == 3,446.  Label checks: all 11 "day1:<bin>" names and "src:Yam" present in the npz names; row count == .snp rows;
  counted allele = .snp column 5 (EIGENSTRAT) verified at rs4988235 (LCT; counted allele == hg19 base, counted frequency
  > 0.9 in bin 0) and rs1426654 (SLC24A5; 'A' allele frequency > 0.95 in bin 10 and < 0.6 in bin 0); share of autosomal
  sites whose hg19 base is one of the two alleles >= 0.98 (else the CpG/direction analysis is not run and A2 = UNVERIFIABLE).
  Any failure stops the run; a fix is a post hoc commit.

THE NULL (SFS-matched by construction).  For every autosomal site the four oldest bins (10000+, 8000-10000, 7000-8000,
  6000-7000) are held at their REAL counts, so the null has exactly the observed ancient site-frequency spectrum of each
  class, the real per-site call depth in every bin, and the real tracked pattern.  Bins 4..10 are simulated:
  (a) a class-specific prior g_c(p) on a 201-point frequency grid is fitted by EM (NPMLE) to the pooled 6000-8000 BP counts
      (bins 2+3) of all class sites; each site's 7000 BP frequency p0 is drawn from its posterior given its own pooled
      counts (fresh draw per replicate);
  (b) neutral Wright-Fisher drift, exact binomial with 2 N_e chromosomes each generation, 20 y per generation, from t0 =
      the mean date of the bin-2+3 individuals to the mean date of each later bin's individuals (both from the anno);
  (c) each later bin is sampled binomially at the site's REAL called-chromosome count in that bin;
  (d) Day's statistic is applied to [real bins 0-3 | simulated bins 4-10] exactly as to the data.
Scenarios (24 per release, 20 replicates each):
  D0 closed population, N_e in {3e3, 1e4, 2e4, 5e4, 1e5, 3e5, 1e6, 3e6};
  D1 steppe pulse at 4750 BP, p <- (1 - a) p + a p_Y, p_Y drawn per site from its posterior given the src:Yam counts (own
     EM prior per class), a = 0.38, same 8 N_e values;
  D1 with a in {0.20, 0.55} at N_e in {1e4, 1e5};
  symmetric per-call error eps = 1e-3 on the PSEUDO-HAPLOID calls of the simulated bins only (as C1c; diploid calls carry
     none), for D0 and D1(a = 0.38) at N_e in {1e4, 1e5}.
  (Generation time trades exactly against N_e: 25 y/gen equals N_e x 1.25; not run separately.)
Derived quantities (v62 primary, v66 replication):
  M_c(scen, N_e) = median over replicates of null S21 in class c;  Q_c = observed S21_c / M_c  (M = 0 -> Q = inf).
  N_e*_c(D)  = N_e at which M_c equals the observed S21_c (linear interpolation of log(M + 0.5) on log N_e over the 8-point
              grid; first crossing from the small end; "< 3e3" or "> 3e6" outside the grid).
  N_e^F_TV   = N_e at which the null's temporal F between pooled bins 2+3 and bin 10 equals the observed one, TV sites with
              >= 20 chromosomes in both and pooled 6000-8000 BP frequency in [0.05, 0.95]; estimator (same on data and null):
              F = sum[(x - y)^2 - x(1-x)/(n1-1) - y(1-y)/(n2-1)] / sum[z(1 - z)], z = (x + y)/2.
  Block bootstrap: 5 Mb blocks, 1,000 resamples of blocks, per-block observed counts and per-block null means (over
  replicates), giving 95% intervals for N_e*_TV, X, E_TS, s_CpG, rho_CpG and s_dmg below.
  Reference null for part A2 = D0 at N_e*_TV(D0) (the drift that fits the damage-immune class), log-interpolated per block.
  E_c   = observed S21_c - null S21_c at the reference (the excess, in events), c in {TS-CpG, TS-non, TS = both}.
  X     = (S21_obs,TS / S21_null,TS) / (S21_obs,TV / S21_null,TV) at the reference (the transition excess factor).
  s_CpG = E_TS-CpG / E_TS;  rho_CpG = (E_TS-CpG / #TS-CpG sites) / (E_TS-non / #TS-non sites)  (E_TS-non <= 0 -> inf).
  s_dmg = (observed - null S21 of TS events in the damage direction) / E_TS;  d_null = the null's damage-direction share.
  Also at N_e = 1e4 and under D1, for the record.

===================================================================================================================
2. BANDS (exhaustive; each is reached by a stated result).  v62 sets the band; v66 is reported beside it, and a different v66
band is reported as "release-dependent" without changing the v62 call.
-------------------------------------------------------------------------------------------------------------------
A1  The transversion class against neutral at the textbook N_e = 1e4 (keruru's measured 7-10k; the R5 feeder row's anchor).
    Q0 = Q_TV(D0, 1e4), Q1 = Q_TV(D1 a = 0.38, 1e4).
    A1-DEF    max(Q0, Q1) < 1/3            observed TV events fewer than a third of neutral at N_e 1e4 under both demographies.
    A1-CONS   1/3 <= min and max <= 3      within 3x of neutral at N_e 1e4 under both.
    A1-EXC    min(Q0, Q1) > 3              more TV events than neutral at N_e 1e4 under both.
    A1-SPLIT  anything else                demography decides.
    (Any pair (Q0, Q1) in [0, inf] x [0, inf] lands in exactly one.)
    Secondary: N_e*_TV(D0) and N_e*_TV(D1) each in  < 5e3 | [5e3, 3e4] | (3e4, 3e5] | > 3e5.
    Consistency gate G-CONS: |log10(N_e*_TV(D0) / N_e^F_TV)| <= log10(3) -> "one N_e fits both the loss of rare TV alleles
    and the bulk drift"; otherwise "inconsistent: the two need different N_e" (out-of-grid values use the grid edge).
A2  What the transition excess is.  First match wins; the last band is the catch-all.
    A2-UNVERIFIABLE  the hg19 allele-match gate failed (CpG and direction cannot be assigned).
    A2-NEG     upper 95% bound of X < 1                       transitions BELOW their matched null relative to transversions.
    A2-NONE    lower 95% bound of E_TS <= 0                   no transition excess beyond the matched null.
    A2-DMG-CpG s_dmg >= 0.75 and lower 95% bound of s_dmg > d_null, and s_CpG >= 0.5 and rho_CpG >= 3
               -> named cause: deamination of methylated CpG (not removed by UDG).
    A2-DMG     s_dmg >= 0.75 and lower 95% bound of s_dmg > d_null (CpG conditions not met)
               -> named cause: deamination damage, not CpG-specific.
    A2-CpG-SYM s_CpG >= 0.5 and rho_CpG >= 3 (damage conditions not met)
               -> named cause: CpG-specific but not in the damage direction (hypermutability, CpG reference/capture effect).
    A2-RESID   anything else -> the excess is real in these data and not damage- or CpG-shaped; its cause (ascertainment,
               batch, reference bias, real loss of low-frequency alleles) is `unverifiable` here; size reported.
    The size of the excess is reported in every band: E_TS with its interval, X with its interval, both at the reference
    and at N_e = 1e4.

===================================================================================================================
3. PREDICTIONS (each can fail; scored on v62)
-------------------------------------------------------------------------------------------------------------------
Day side (steelman of Q107-Q111, the C6 abstract and C7):
  PD1  A1-DEF and N_e*_TV(D0) > 3e4: in the damage-immune class neutral drift at N_e 1e4 still predicts at least 3x the
       observed events.  Reached if the null median TV S21 at N_e 1e4 exceeds 108 (v62) under both D0 and D1.
  PD2  A2-DMG-CpG or A2-DMG: the post-6000 BP thousands are an ancient-DNA artefact, so Day's small count is closer in kind
       than the audit's thousands.  Reached if s_dmg >= 0.75 with its lower bound above d_null.
Critic side (steelman of keruru's measured N_e and the C1c model):
  PC1  A1-CONS and N_e*_TV(D0) in [5e3, 3e4]: the damage-immune class is what neutral drift at the measured temporal N_e
       predicts.  Reached if the null median TV S21 at N_e 1e4 lies in [12, 108] (v62) under both D0 and D1.
  PC2  A2-NONE, A2-RESID or A2-CpG-SYM: the transition excess is not damage-shaped, so the thousands include real loss of
       low-frequency alleles.  Reached if s_dmg < 0.75, or its lower bound is <= d_null, or E_TS is not above zero.
The audit's own (written before the run; the numbers are mine, from R4-C1d sections 3.2-3.5: TV events need the minor allele
seen in all four oldest bins, i.e. at roughly 1-5%, and at N_e 1e4 about a tenth to a fifth of such alleles should be lost
or unseen in 901 modern chromosomes in ~340 generations):
  PA1  A1-DEF (probability ~0.6), with Q0 in [0.02, 0.3] (central 0.08).
  PA2  N_e*_TV(D0) in (3e4, 5e5] (central 1e5); N_e*_TV(D1) within 2x of N_e*_TV(D0).
  PA3  N_e^F_TV in [4e3, 3e4] (central 1e4), so G-CONS fails (one N_e does not fit both).
  PA4  A2-DMG-CpG (probability ~0.45; A2-RESID ~0.3, A2-DMG ~0.15, others ~0.1), with s_CpG in [0.4, 0.95], s_dmg in
       [0.75, 1.0], X in [5, 200] at the reference.
  PA5  v66 gives the same A1 and A2 bands as v62.
  PA6  The eps = 1e-3 cells raise or lower M_TV by less than 2x at each N_e (error on the simulated bins is second-order
       for TV).
  PA7  D1 with a in {0.20, 0.55} changes M_TV by less than 2x against a = 0.38 at the same N_e.

===================================================================================================================
4. WHAT EACH BAND LICENSES (no verdict FIELD flips in any band; part A takes three reviews regardless, lead ruling D-23)
-------------------------------------------------------------------------------------------------------------------
A1-DEF   C6, C7, C: an "R4 C1d-fu" comment: the deficit against neutral at N_e 1e4 survives in the damage-immune class,
         and its size; candidate defeater (Day side) against reading the C1c/C1d thousands as "neutral at textbook N_e
         fits"; R5 feeder row: the N_e hinge is confirmed on transversions.  No field moves: C6 external (contradicted, as
         described) and C7 external (contradicted, on measured F_adj) do not rest on this comparator.
A1-CONS  the same files: the "deficit" in the R5 row is a transition artefact; candidate defeater (critic side) against the
         deficit reading.  No field moves.
A1-EXC / A1-SPLIT  comments only; the R5 row records that demography or residual error decides.
G-CONS fails  recorded in the R5 row and the C4/C5b comments: the rare-allele loss and the bulk temporal F need different
         N_e (structure, growth or error); no field moves.
N_e*_TV(D0) > 3e6  the lead is asked whether C7's Readings table needs a row (escalation note only).
A2 bands  R4-C1d section 3.4's "open" becomes the named cause and size; the C1d "Who this helps" bullet "the thousands are
         real data" is qualified (DMG bands: reproducible in the data but artefactual; other bands: real).  No field moves.
Escalation clause (brief): nothing here touches D or C2 / C2a.  If the lead judges any comment above to move a verdict
  field, that is reported to the lead and not applied by the analyst.

===================================================================================================================
5. ASSUMPTIONS AND LIMITS (stated before the run)
-------------------------------------------------------------------------------------------------------------------
- Binomial sampling on chromosomes (pseudo-haploid = 1, diploid = 2 under random mating); no per-individual capture
  heterogeneity in the simulated bins (C1c's strongest upward lever; the real bins 0-3 carry their own).
- The posterior for p0 uses only bins 2+3; bins 0-1 are held real and enter only through "not fixed" and tracking.
- One panmictic European population plus at most one steppe pulse; no Middle Neolithic hunter-gatherer resurgence, no
  regional structure, no growth inside a run (growth is bracketed by the N_e grid).
- The null treats every observed ancient minor allele as real.  That is what makes the excess test work: an artefactual
  minor allele is "lost" with certainty, a real one only with its drift probability.
- No new mutations in ~340 generations (C1c: new-in-window substitutions ~5e-151 per site).

===================================================================================================================
6. RESOURCES AND COMMANDS (host only; one agent at a time; at most 11 busy processes in total; `uptime` first)
-------------------------------------------------------------------------------------------------------------------
Fetch (run task, before prep; read-only; never executed; sha256 and access date recorded in raw/c1d_tv.host):
    mkdir -p sources/raw/c1dtv-hg19-<YYYY-MM-DD> && cd sources/raw/c1dtv-hg19-<YYYY-MM-DD> && \
      curl -fsSO https://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/hg19.fa.gz && sha256sum hg19.fa.gz > SHA256
    export C1DTV_HG19=$PWD/hg19.fa.gz
Launch (after the committed script is rsynced; ncpu = 6: ~1.2 GB per worker projected, so ~7 GB, and 6 processes under the
11-process cap):
    ssh -o BatchMode=yes na-workhorse 'cd ~/projects/evo-sim && C1DTV_HG19=... nohup sh -c "\
      research/.venv/bin/python -I research/checks/c1d_tv.py prep v62 && \
      research/.venv/bin/python -I research/checks/c1d_tv.py prep v66 && \
      research/.venv/bin/python -I research/checks/c1d_tv.py smoke $C1D_OUT/c1d_tv_v62_prep.npz 6 1 50000 && \
      research/.venv/bin/python -I research/checks/c1d_tv.py run v62 6 && \
      research/.venv/bin/python -I research/checks/c1d_tv.py run v66 6 && \
      research/.venv/bin/python -I research/checks/c1d_tv.py analyse" \
      > research/checks/results/raw/c1d_tv.out 2>&1 < /dev/null &'
Collect: rsync na-workhorse:projects/evo-sim/research/checks/results/raw/c1d_tv* back; md5s and hostname in c1d_tv.host.
Cost (measured in the local synthetic smoke, section 7; the host smoke step above re-measures on real data and prints the
  projected wall time and peak RSS before the main run starts; if the projection exceeds 3 h per release or 1.8 GB per
  worker, the run task stops and reports instead of launching).

===================================================================================================================
7. LOCAL SMOKE (synthetic data only; workstation, one worker, 2026-10-14)
-------------------------------------------------------------------------------------------------------------------
`selftest` ok (EM recovers a two-point prior to 0.05; interpolation; A1 bands exhaustive on a Q grid; damage labels).
`mkfake <f> 60000` then `smoke <f> 1 1`: real entry point, Pool path, all 24 scenarios, 1 replicate, then `analyse` on the
  output.  Synthetic truth: closed population at N_e = 2e4, deamination artefacts planted at TS-CpG sites in bins 0-3.
  Recovered: N_e*_TV(D0) = 2.6e4 (bootstrap 1.9e4-3.6e4), N_e^F_TV = 1.9e4, G-CONS holds, A2 = A2-DMG-CpG (s_dmg 1.00,
  s_CpG 1.03): the estimator finds the planted N_e within 1.3x and names the planted cause.  1.18 s per task on 60,000
  sites, peak RSS 121 MB per worker; projected main run 3.0 CPU-hours per release at 1,150,639 sites and 20 replicates
  (about 30 min wall per release on 6 workers).  An earlier smoke at 20,000 sites (1 replicate) showed that error applied
  to diploid modern calls suppressed modern fixation wholesale (M_TV 52 -> 14); the error term was then restricted to
  pseudo-haploid calls (as C1c) BEFORE this commit.  No real data were read.
"""
import os
import sys
import gzip
import json
import time
import importlib.util
import numpy as np
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("c1d", os.path.join(HERE, "c1d_aadr_real.py"))
c1d = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(c1d)

RES = os.environ.get("C1D_RES", os.path.join(HERE, "results", "raw"))
HG19 = os.environ.get("C1DTV_HG19", "")
SEED = 20261013
GEN_Y = 20.0
GRID = np.linspace(0.0, 1.0, 201)
NE_GRID = [3e3, 1e4, 2e4, 5e4, 1e5, 3e5, 1e6, 3e6]
PULSE_BP = 4750.0
REPS = 20
BLOCK_BP = 5_000_000
NBOOT = 1000
CLS = ["TV", "TS-CpG", "TS-non"]
CAT = ["TV", "CpG-dmg", "CpG-oth", "non-dmg", "non-oth"]          # per-block event categories
GATE = {"v62": dict(TV=(36, 6306), TS=(4559, 47937)), "v66": dict(TV=(44, 7614), TS=(3446, None))}


def scenarios():
    s = []
    for ne in NE_GRID:
        s.append(dict(key="D0_%g" % ne, demo="D0", ne=ne, a=0.0, eps=0.0))
    for ne in NE_GRID:
        s.append(dict(key="D1_%g" % ne, demo="D1", ne=ne, a=0.38, eps=0.0))
    for a in (0.20, 0.55):
        for ne in (1e4, 1e5):
            s.append(dict(key="D1a%.2f_%g" % (a, ne), demo="D1", ne=ne, a=a, eps=0.0))
    for demo, a in (("D0", 0.0), ("D1", 0.38)):
        for ne in (1e4, 1e5):
            s.append(dict(key="%seps_%g" % (demo, ne), demo=demo, ne=ne, a=a, eps=1e-3))
    return s


SCEN = scenarios()
assert len(SCEN) == 24


# ----------------------------------------------------------------------------------------------------- prior / posterior
def binom_logpmf(k, n, p):
    from scipy.special import gammaln
    k = k[:, None].astype(np.float64)
    n = n[:, None].astype(np.float64)
    p = np.clip(p[None, :], 1e-12, 1 - 1e-12)
    out = gammaln(n + 1) - gammaln(k + 1) - gammaln(n - k + 1) + k * np.log(p) + (n - k) * np.log1p(-p)
    # exact endpoints
    out[:, 0] = np.where(k[:, 0] == 0, 0.0, -np.inf)
    out[:, -1] = np.where(k[:, 0] == n[:, 0], 0.0, -np.inf)
    return out


def em_prior(n, k, iters=300):
    """NPMLE of the frequency distribution on GRID from binomial counts (n, k).  Returns (w, uniq, inv, cdf)."""
    key = n.astype(np.int64) * 100000 + k.astype(np.int64)
    uniq, inv, cnt = np.unique(key, return_inverse=True, return_counts=True)
    un, uk = uniq // 100000, uniq % 100000
    L = np.exp(binom_logpmf(uk, un, GRID)).astype(np.float64)
    w = np.full(len(GRID), 1.0 / len(GRID))
    c = cnt.astype(np.float64)
    for _ in range(iters):
        post = L * w
        post /= np.maximum(post.sum(axis=1, keepdims=True), 1e-300)
        w = (c[:, None] * post).sum(axis=0) / c.sum()
    post = L * w
    post /= np.maximum(post.sum(axis=1, keepdims=True), 1e-300)
    cdf = np.cumsum(post, axis=1).astype(np.float32)
    cdf[:, -1] = 1.0
    return w, inv.astype(np.int32), cdf


def draw_post(rng, inv, cdf, chunk=50000):
    S = len(inv)
    out = np.empty(S, dtype=np.float64)
    for lo in range(0, S, chunk):
        hi = min(lo + chunk, S)
        x = rng.random(hi - lo, dtype=np.float32)
        rows = cdf[inv[lo:hi]]
        j = (rows < x[:, None]).sum(axis=1)
        out[lo:hi] = GRID[np.minimum(j, len(GRID) - 1)]
    return out


# ----------------------------------------------------------------------------------------------------- events
def classify_events(n, r, cls, a1, a2, blk, nblk):
    """Day's statistic (E1/T2/m=1/all11) on (11, S) arrays.  Returns per-class summaries and per-block S21 categories."""
    res = c1d.day_events(n, r, "E1", "T2", 1, "all11", ret_idx=True)
    out = {c: dict(eligible=0, S21=0, profile=np.zeros(11, dtype=np.int64)) for c in CLS}
    out["TS"] = dict(eligible=0, S21=0, profile=np.zeros(11, dtype=np.int64))
    out["TS_dmg_S21"] = 0
    perblk = np.zeros((nblk, len(CAT)), dtype=np.int64)
    for allele, ie, dt, tr in res["idx"]:
        fixed = a1[ie] if allele == 0 else a2[ie]
        lost = a2[ie] if allele == 0 else a1[ie]
        dmg = ((fixed == ord("C")) & (lost == ord("T"))) | ((fixed == ord("G")) & (lost == ord("A")))
        s21 = tr & (dt >= 4)
        for ci, c in enumerate(CLS):
            m = cls[ie] == ci
            out[c]["eligible"] += int(m.sum())
            out[c]["S21"] += int((m & s21).sum())
            out[c]["profile"] += np.bincount(dt[m & tr], minlength=11)
        b = blk[ie]
        cat = np.full(len(ie), -1)
        cat[cls[ie] == 0] = 0
        cat[(cls[ie] == 1) & dmg] = 1
        cat[(cls[ie] == 1) & ~dmg] = 2
        cat[(cls[ie] == 2) & dmg] = 3
        cat[(cls[ie] == 2) & ~dmg] = 4
        sel = s21 & (cat >= 0)
        np.add.at(perblk, (b[sel], cat[sel]), 1)
        out["TS_dmg_S21"] += int((s21 & (cls[ie] >= 1) & dmg).sum())
    for k in ("eligible", "S21"):
        out["TS"][k] = out["TS-CpG"][k] + out["TS-non"][k]
    out["TS"]["profile"] = out["TS-CpG"]["profile"] + out["TS-non"]["profile"]
    for c in CLS + ["TS"]:
        out[c]["profile"] = [int(x) for x in out[c]["profile"]]
    return out, perblk


def temporal_F(n, r, mask):
    n1 = n[2] + n[3]
    k1 = r[2] + r[3]
    n2, k2 = n[10], r[10]
    with np.errstate(invalid="ignore", divide="ignore"):
        x = k1 / np.maximum(n1, 1)
        y = k2 / np.maximum(n2, 1)
    ok = mask & (n1 >= 20) & (n2 >= 20) & (x >= 0.05) & (x <= 0.95)
    x, y, a, b = x[ok], y[ok], n1[ok], n2[ok]
    z = (x + y) / 2
    num = ((x - y) ** 2 - x * (1 - x) / (a - 1) - y * (1 - y) / (b - 1)).sum()
    den = (z * (1 - z)).sum()
    return float(num), float(den), int(ok.sum())


# ----------------------------------------------------------------------------------------------------- simulation
_P = {}


def _load(path):
    if path not in _P:
        z = np.load(path)
        _P[path] = {k: z[k] for k in z.files}
    return _P[path]


def simulate(P, sc, rng, maxsites=None):
    n = P["n"]
    r = P["r"]
    S = n.shape[1] if maxsites is None else min(maxsites, n.shape[1])
    n = n[:, :S]
    r = r[:, :S].copy()
    cls = P["cls"][:S]
    p = np.empty(S)
    for ci in range(3):
        m = cls == ci
        p[m] = draw_post(rng, P["inv_neo_%d" % ci][:S][m], P["cdf_neo_%d" % ci])
    pY = None
    if sc["a"] > 0:
        pY = np.empty(S)
        for ci in range(3):
            m = cls == ci
            pY[m] = draw_post(rng, P["inv_yam_%d" % ci][:S][m], P["cdf_yam_%d" % ci])
    t0 = float(P["t0"])
    dates = P["dates"]
    gens = np.array([int(round((t0 - dates[b]) / GEN_Y)) for b in range(4, 11)])
    gpulse = int(round((t0 - PULSE_BP) / GEN_Y))
    twoN = int(round(2 * sc["ne"]))
    g = 0
    for bi, gb in enumerate(gens):
        while g < gb:
            g += 1
            p = rng.binomial(twoN, p) / twoN
            if pY is not None and g == gpulse:
                p = (1 - sc["a"]) * p + sc["a"] * pY
        b = 4 + bi
        if sc["eps"] > 0:
            nph = P["nph"][b, :S]
            kph = rng.binomial(nph, p)
            kph = rng.binomial(kph, 1 - sc["eps"]) + rng.binomial(nph - kph, sc["eps"])
            r[b] = kph + rng.binomial(n[b] - nph, p)
        else:
            r[b] = rng.binomial(n[b], p)
    return n, r, S


def task(args):
    path, rel, si, rep, maxsites = args
    P = _load(path)
    sc = SCEN[si]
    rng = np.random.default_rng([SEED, 0 if rel == "v62" else 1, si, rep])
    t = time.time()
    n, r, S = simulate(P, sc, rng, maxsites)
    nblk = int(P["nblk"])
    ev, perblk = classify_events(n, r, P["cls"][:S], P["a1"][:S], P["a2"][:S], P["blk"][:S], nblk)
    fnum, fden, fn = temporal_F(n, r, P["cls"][:S] == 0)
    return dict(rel=rel, scen=sc["key"], rep=rep, ev=ev, perblk=perblk.tolist(), F_TV=[fnum, fden, fn],
                secs=time.time() - t, S=S)


def run_grid(path, rel, ncpu, reps, out_jsonl, maxsites=None):
    tasks = [(path, rel, si, rep, maxsites) for si in range(len(SCEN)) for rep in range(reps)]
    t = time.time()
    with Pool(ncpu) as pool, open(out_jsonl, "w") as fo:
        for k, res in enumerate(pool.imap_unordered(task, tasks)):
            fo.write(json.dumps(res) + "\n")
            fo.flush()
            if k % 20 == 0:
                print("  %s task %d/%d  %.0fs (last %.1fs)" % (rel, k + 1, len(tasks), time.time() - t, res["secs"]),
                      flush=True)
    return time.time() - t, len(tasks)


# ----------------------------------------------------------------------------------------------------- prep (host)
def read_hg19_context(chrom, pos):
    """Return (base, prev, next) uint8 arrays from hg19.fa.gz for autosomal 1-based positions."""
    assert HG19 and os.path.exists(HG19), "set C1DTV_HG19 to the fetched hg19.fa.gz"
    base = np.zeros(len(pos), dtype=np.uint8)
    prev = np.zeros(len(pos), dtype=np.uint8)
    nxt = np.zeros(len(pos), dtype=np.uint8)
    want = {"chr%d" % c: np.where(chrom == c)[0] for c in range(1, 23)}
    cur, buf = None, []

    def flush():
        if cur in want and len(want[cur]):
            seq = np.frombuffer(b"".join(buf).upper(), dtype=np.uint8)
            ix = want[cur]
            pp = pos[ix] - 1
            assert pp.max() + 1 < len(seq), (cur, pp.max(), len(seq))
            base[ix], prev[ix], nxt[ix] = seq[pp], seq[pp - 1], seq[pp + 1]
    with gzip.open(HG19, "rb") as f:
        for line in f:
            if line.startswith(b">"):
                flush()
                cur, buf = line[1:].split()[0].decode(), []
            elif cur in want:
                buf.append(line.rstrip())
        flush()
    return base, prev, nxt


def prep(rel):
    N, D, names, sel, _, _ = c1d.load_counts(rel)
    cnt = c1d.Counts(N, D, names)
    bins = ["day1:%s" % b for b in c1d.DAY_NAMES]
    for b in bins + ["src:Yam"]:
        assert b in cnt.idx, "missing group label %s" % b
    ids, chrom, pos = c1d.load_snp(rel)
    assert len(ids) == N.shape[0], (len(ids), N.shape[0])
    a1, a2 = [], []
    with open(os.path.join(c1d.DATA, c1d.REL[rel]["stem"] + ".snp")) as f:
        for line in f:
            q = line.split()
            if q:
                a1.append(q[4])
                a2.append(q[5])
    a1, a2 = np.array(a1), np.array(a2)
    nn = np.zeros((11, len(ids)), dtype=np.int32)
    rr = np.zeros((11, len(ids)), dtype=np.int32)
    nph = np.zeros((11, len(ids)), dtype=np.int32)
    for i, b in enumerate(bins):
        nn[i], rr[i] = cnt.chrom(b)
        nph[i] = cnt.raw(b)[0]
    yn, yr = cnt.chrom("src:Yam")
    # counted-allele checks
    ix = {s: i for i, s in enumerate(ids)}
    checks = {}
    for rs in ("rs4988235", "rs1426654"):
        assert rs in ix, rs
        j = ix[rs]
        checks[rs] = dict(a1=a1[j], a2=a2[j], f_counted=[float(rr[b, j] / max(nn[b, j], 1)) for b in range(11)])
    j = ix["rs4988235"]
    assert checks["rs4988235"]["f_counted"][0] > 0.9, checks
    j2 = ix["rs1426654"]
    fA = np.array(checks["rs1426654"]["f_counted"]) if a1[j2] == "A" else 1 - np.array(checks["rs1426654"]["f_counted"])
    assert fA[10] > 0.95 and fA[0] < 0.6, checks
    auto = chrom <= 22
    base, prev, nxt = read_hg19_context(chrom[auto], pos[auto])
    A1 = np.frombuffer("".join(a1[auto]).encode(), dtype=np.uint8)
    A2 = np.frombuffer("".join(a2[auto]).encode(), dtype=np.uint8)
    assert len(A1) == auto.sum()
    match = float(((base == A1) | (base == A2)).mean())
    checks["hg19_allele_match"] = match
    checks["counted_is_hg19_base_rs4988235"] = bool(a1[j] == chr(base[np.where(np.where(auto)[0] == j)[0][0]]))
    assert checks["counted_is_hg19_base_rs4988235"], checks
    ts = ((A1 == ord("A")) & (A2 == ord("G"))) | ((A1 == ord("G")) & (A2 == ord("A"))) | \
         ((A1 == ord("C")) & (A2 == ord("T"))) | ((A1 == ord("T")) & (A2 == ord("C")))
    ct = np.isin(A1, [ord("C"), ord("T")]) & np.isin(A2, [ord("C"), ord("T")])
    ga = np.isin(A1, [ord("G"), ord("A")]) & np.isin(A2, [ord("G"), ord("A")])
    cpg = ts & ((ct & (nxt == ord("G"))) | (ga & (prev == ord("C"))))
    cls = np.where(~ts, 0, np.where(cpg, 1, 2)).astype(np.int8)
    if match < 0.98:
        checks["cpg_direction_valid"] = False
    else:
        checks["cpg_direction_valid"] = True
    n = nn[:, auto]
    r = rr[:, auto]
    ch, ps = chrom[auto], pos[auto]
    bkey = ch.astype(np.int64) * 1000 + ps // BLOCK_BP
    ub, blk = np.unique(bkey, return_inverse=True)
    meta = c1d.load_meta(rel)
    gnames, masks = c1d.build_groups(meta)
    gi = {g: i for i, g in enumerate(gnames)}
    dates = np.array([float(np.nanmean(meta["date"][masks[gi[b]]])) for b in bins])
    t0 = float(np.nanmean(meta["date"][masks[gi[bins[2]]] | masks[gi[bins[3]]]]))
    out = dict(n=n, r=r, nph=nph[:, auto], cls=cls, a1=A1, a2=A2, blk=blk.astype(np.int32), nblk=len(ub), dates=dates,
               t0=t0)
    for ci in range(3):
        m = cls == ci
        w, inv, cdf = em_prior(n[2, m] + n[3, m], r[2, m] + r[3, m])
        full = np.zeros(len(cls), dtype=np.int32)
        full[m] = inv
        out["inv_neo_%d" % ci], out["cdf_neo_%d" % ci], out["w_neo_%d" % ci] = full, cdf, w
        w, inv, cdf = em_prior(yn[auto][m], yr[auto][m])
        full = np.zeros(len(cls), dtype=np.int32)
        full[m] = inv
        out["inv_yam_%d" % ci], out["cdf_yam_%d" % ci], out["w_yam_%d" % ci] = full, cdf, w
    fn = os.path.join(c1d.OUT, "c1d_tv_%s_prep.npz" % rel)
    np.savez(fn, **out)
    obs = observed(out, rel, checks)
    return fn, obs


def observed(P, rel, checks, gate=True):
    ev, perblk = classify_events(P["n"], P["r"], P["cls"], P["a1"], P["a2"], P["blk"], int(P["nblk"]))
    fnum, fden, fn = temporal_F(P["n"], P["r"], P["cls"] == 0)
    obs = dict(rel=rel, ev=ev, perblk=perblk.tolist(), F_TV=[fnum, fden, fn], checks=checks,
               dates=[float(x) for x in P["dates"]], t0=float(P["t0"]),
               n_sites={c: int((P["cls"] == i).sum()) for i, c in enumerate(CLS)})
    if gate and rel in GATE:
        g = GATE[rel]
        assert ev["TV"]["S21"] == g["TV"][0] and ev["TV"]["eligible"] == g["TV"][1], ("TV gate", ev["TV"])
        assert ev["TS"]["S21"] == g["TS"][0], ("TS gate", ev["TS"])
        if g["TS"][1] is not None:
            assert ev["TS"]["eligible"] == g["TS"][1], ("TS gate", ev["TS"])
    with open(os.path.join(RES, "c1d_tv_%s_obs.json" % rel), "w") as f:
        json.dump(obs, f, indent=1)
    return obs


# ----------------------------------------------------------------------------------------------------- analysis
def interp_ne(M, target):
    """First crossing of log(M+0.5) with log(target+0.5) on log N_e; M decreasing in N_e expected."""
    lx = np.log10(NE_GRID)
    ly = np.log10(np.asarray(M, dtype=float) + 0.5)
    lt = np.log10(target + 0.5)
    if ly[0] <= lt:
        return NE_GRID[0] * (0.999 if ly[0] < lt else 1.0)       # below grid ("< 3e3") flagged by value < 3e3
    for i in range(len(lx) - 1):
        if (ly[i] - lt) * (ly[i + 1] - lt) <= 0 and ly[i] != ly[i + 1]:
            f = (ly[i] - lt) / (ly[i] - ly[i + 1])
            return float(10 ** (lx[i] + f * (lx[i + 1] - lx[i])))
    return NE_GRID[-1] * 1.001                                   # above grid ("> 3e6")


def interp_at(Mgrid, ne):
    """log-interpolate counts (rows = grid) at ne; clamps at the edges."""
    lx = np.log10(NE_GRID)
    l = np.clip(np.log10(ne), lx[0], lx[-1])
    i = min(np.searchsorted(lx, l, side="right") - 1, len(lx) - 2)
    f = (l - lx[i]) / (lx[i + 1] - lx[i])
    ly = (1 - f) * np.log(np.asarray(Mgrid[i], float) + 0.5) + f * np.log(np.asarray(Mgrid[i + 1], float) + 0.5)
    return np.exp(ly) - 0.5


def band_A1(q0, q1):
    lo, hi = min(q0, q1), max(q0, q1)
    if hi < 1 / 3:
        return "A1-DEF"
    if lo >= 1 / 3 and hi <= 3:
        return "A1-CONS"
    if lo > 3:
        return "A1-EXC"
    return "A1-SPLIT"


def band_ne(ne):
    if ne < 5e3:
        return "<5e3"
    if ne <= 3e4:
        return "[5e3,3e4]"
    if ne <= 3e5:
        return "(3e4,3e5]"
    return ">3e5"


def a2_stats(O, Mref, nsites):
    """O, Mref: totals per CAT (TV, CpG-dmg, CpG-oth, non-dmg, non-oth)."""
    O = np.asarray(O, float)
    M = np.asarray(Mref, float)
    E = O - M
    E_cpg, E_non = E[1] + E[2], E[3] + E[4]
    E_ts = E_cpg + E_non
    O_ts, M_ts = O[1:].sum(), M[1:].sum()
    X = (O_ts / max(M_ts, 1e-9)) / (O[0] / max(M[0], 1e-9)) if O[0] > 0 else float("inf")
    s_cpg = E_cpg / E_ts if E_ts != 0 else float("nan")
    rho = (E_cpg / nsites["TS-CpG"]) / (E_non / nsites["TS-non"]) if E_non > 0 else float("inf")
    s_dmg = (E[1] + E[3]) / E_ts if E_ts != 0 else float("nan")
    d_null = (M[1] + M[3]) / max(M_ts, 1e-9)
    return dict(E_TS=E_ts, E_CpG=E_cpg, E_non=E_non, X=X, s_CpG=s_cpg, rho_CpG=rho, s_dmg=s_dmg, d_null=d_null,
                O_TS=O_ts, M_TS=M_ts, O_TV=O[0], M_TV=M[0])


def band_A2(valid, pt, ci):
    if not valid:
        return "A2-UNVERIFIABLE"
    if ci["X"][1] < 1:
        return "A2-NEG"
    if ci["E_TS"][0] <= 0:
        return "A2-NONE"
    dmg = pt["s_dmg"] >= 0.75 and ci["s_dmg"][0] > pt["d_null"]
    cpg = pt["s_CpG"] >= 0.5 and pt["rho_CpG"] >= 3
    if dmg and cpg:
        return "A2-DMG-CpG"
    if dmg:
        return "A2-DMG"
    if cpg:
        return "A2-CpG-SYM"
    return "A2-RESID"


def analyse_rel(rel, obs, recs):
    by = {}
    for x in recs:
        by.setdefault(x["scen"], []).append(x)
    med = lambda key, c: float(np.median([x["ev"][c]["S21"] for x in by[key]]))
    out = dict(rel=rel, obs={c: obs["ev"][c] for c in CLS + ["TS"]}, n_reps={k: len(v) for k, v in by.items()})
    oTV = obs["ev"]["TV"]["S21"]
    M = {k: {c: med(k, c) for c in CLS + ["TS"]} for k in by}
    out["M"] = M
    q = lambda k: (oTV / M[k]["TV"]) if M[k]["TV"] > 0 else float("inf")
    q0, q1 = q("D0_10000"), q("D1_10000")
    out["Q0"], out["Q1"], out["A1"] = q0, q1, band_A1(q0, q1)
    ne0 = interp_ne([M["D0_%g" % ne]["TV"] for ne in NE_GRID], oTV)
    ne1 = interp_ne([M["D1_%g" % ne]["TV"] for ne in NE_GRID], oTV)
    out["Ne_star_TV_D0"], out["Ne_star_TV_D1"] = ne0, ne1
    out["Ne_star_band_D0"], out["Ne_star_band_D1"] = band_ne(ne0), band_ne(ne1)
    fobs = obs["F_TV"][0] / obs["F_TV"][1]
    fnull = [float(np.median([x["F_TV"][0] / x["F_TV"][1] for x in by["D0_%g" % ne]])) for ne in NE_GRID]
    # F decreases with N_e: find crossing on log scale of F (clip at small positive)
    neF = interp_ne([max(f, 1e-6) * 1e6 for f in fnull], max(fobs, 1e-6) * 1e6)
    out["F_TV_obs"], out["F_TV_null"], out["Ne_F_TV"] = fobs, fnull, neF
    out["G_CONS"] = bool(abs(np.log10(ne0 / neF)) <= np.log10(3))
    out["PA6_eps_ratio"] = {ne: M["D0eps_%g" % ne]["TV"] / max(M["D0_%g" % ne]["TV"], 1e-9) for ne in (1e4, 1e5)}
    out["PA6_eps_ratio_D1"] = {ne: M["D1eps_%g" % ne]["TV"] / max(M["D1_%g" % ne]["TV"], 1e-9) for ne in (1e4, 1e5)}
    out["PA7_a_ratio"] = {"%.2f_%g" % (a, ne): M["D1a%.2f_%g" % (a, ne)]["TV"] / max(M["D1_%g" % ne]["TV"], 1e-9)
                          for a in (0.20, 0.55) for ne in (1e4, 1e5)}
    # per-block arrays for A2 and the bootstrap
    Ob = np.asarray(obs["perblk"], float)                                    # (nblk, 5)
    Mb = np.array([np.mean([x["perblk"] for x in by["D0_%g" % ne]], axis=0) for ne in NE_GRID])   # (8, nblk, 5)
    nsites = obs["n_sites"]

    def at(ne_ref, Obb, Mbb):
        Mref = interp_at(Mbb.sum(axis=1), ne_ref)                            # (5,)
        return a2_stats(Obb.sum(axis=0), Mref, nsites)
    pt = at(ne0, Ob, Mb)
    pt1e4 = at(1e4, Ob, Mb)
    rng = np.random.default_rng(SEED + 7)
    nb = Ob.shape[0]
    boots = {k: [] for k in ("Ne_star", "X", "E_TS", "s_CpG", "rho_CpG", "s_dmg")}
    for _ in range(NBOOT):
        ix = rng.integers(0, nb, nb)
        Ox, Mx = Ob[ix], Mb[:, ix]
        ne_b = interp_ne(Mx[:, :, 0].sum(axis=1), Ox[:, 0].sum())
        s = at(ne_b, Ox, Mx)
        boots["Ne_star"].append(ne_b)
        for k in ("X", "E_TS", "s_CpG", "rho_CpG", "s_dmg"):
            boots[k].append(s[k])
    fin = lambda v: np.clip(np.asarray(v, float), -1e12, 1e12)
    ci = {k: [float(np.nanpercentile(fin(v), 2.5)), float(np.nanpercentile(fin(v), 97.5))] for k, v in boots.items()}
    valid = bool(obs["checks"].get("cpg_direction_valid", True))
    out["A2_point_ref"], out["A2_point_1e4"], out["A2_ci"] = pt, pt1e4, ci
    out["A2"] = band_A2(valid, pt, ci)
    out["G_CONS_label"] = "one N_e fits both" if out["G_CONS"] else "inconsistent: the two need different N_e"
    return out


def score(a):
    """Registered predictions, v62."""
    v = a["v62"]
    s = {}
    s["PD1"] = v["A1"] == "A1-DEF" and v["Ne_star_TV_D0"] > 3e4
    s["PD2"] = v["A2"] in ("A2-DMG-CpG", "A2-DMG")
    s["PC1"] = v["A1"] == "A1-CONS" and 5e3 <= v["Ne_star_TV_D0"] <= 3e4
    s["PC2"] = v["A2"] in ("A2-NONE", "A2-RESID", "A2-CpG-SYM")
    s["PA1"] = v["A1"] == "A1-DEF" and 0.02 <= v["Q0"] <= 0.3
    s["PA2"] = 3e4 < v["Ne_star_TV_D0"] <= 5e5 and 0.5 <= v["Ne_star_TV_D1"] / v["Ne_star_TV_D0"] <= 2
    s["PA3"] = 4e3 <= v["Ne_F_TV"] <= 3e4 and not v["G_CONS"]
    p = v["A2_point_ref"]
    s["PA4"] = v["A2"] == "A2-DMG-CpG" and 0.4 <= p["s_CpG"] <= 0.95 and 0.75 <= p["s_dmg"] <= 1.0 and 5 <= p["X"] <= 200
    s["PA5"] = ("v66" in a) and a["v66"]["A1"] == v["A1"] and a["v66"]["A2"] == v["A2"]
    s["PA6"] = all(0.5 < x < 2 for x in list(v["PA6_eps_ratio"].values()) + list(v["PA6_eps_ratio_D1"].values()))
    s["PA7"] = all(0.5 < x < 2 for x in v["PA7_a_ratio"].values())
    return {k: bool(x) for k, x in s.items()}


def analyse(rels=("v62", "v66"), tag="c1d_tv"):
    a = {}
    for rel in rels:
        fo = os.path.join(RES, "%s_%s_obs.json" % (tag, rel))
        fn = os.path.join(RES, "%s_%s_null.jsonl" % (tag, rel))
        if not (os.path.exists(fo) and os.path.exists(fn)):
            continue
        obs = json.load(open(fo))
        recs = [json.loads(l) for l in open(fn)]
        a[rel] = analyse_rel(rel, obs, recs)
    if "v62" in a:
        a["score"] = score(a)
    with open(os.path.join(RES, "%s_analysis.json" % tag), "w") as f:
        json.dump(a, f, indent=1, default=float)
    L = []
    for rel in rels:
        if rel not in a:
            continue
        v = a[rel]
        L.append("== %s ==" % rel)
        L.append("observed S21 TV %d (elig %d)  TS %d (elig %d)  TS-CpG %d  TS-non %d" % (
            v["obs"]["TV"]["S21"], v["obs"]["TV"]["eligible"], v["obs"]["TS"]["S21"], v["obs"]["TS"]["eligible"],
            v["obs"]["TS-CpG"]["S21"], v["obs"]["TS-non"]["S21"]))
        for k in sorted(v["M"]):
            L.append("  %-14s M_TV %9.1f  M_TS %10.1f  M_CpG %9.1f  M_non %9.1f" % (
                k, v["M"][k]["TV"], v["M"][k]["TS"], v["M"][k]["TS-CpG"], v["M"][k]["TS-non"]))
        L.append("A1 %s  Q0 %.3g  Q1 %.3g  Ne*_TV D0 %.3g (%s)  D1 %.3g (%s)" % (
            v["A1"], v["Q0"], v["Q1"], v["Ne_star_TV_D0"], v["Ne_star_band_D0"], v["Ne_star_TV_D1"], v["Ne_star_band_D1"]))
        L.append("F_TV obs %.5f  Ne^F_TV %.3g  G-CONS %s" % (v["F_TV_obs"], v["Ne_F_TV"], v["G_CONS_label"]))
        L.append("A2 %s  ref %s  ci %s" % (v["A2"], json.dumps(v["A2_point_ref"], default=float),
                                           json.dumps(v["A2_ci"], default=float)))
        L.append("A2 at Ne 1e4 %s" % json.dumps(v["A2_point_1e4"], default=float))
    if "score" in a:
        L.append("score %s" % json.dumps(a["score"]))
    txt = "\n".join(L)
    open(os.path.join(RES, "%s_analysis.txt" % tag), "w").write(txt + "\n")
    print(txt)
    return a


# ----------------------------------------------------------------------------------------------------- synthetic
def mkfake(path, S, ne_true=2e4, dmg_rate=0.015, seed=1):
    """Synthetic prep file: observed bins generated by the null model itself at ne_true (closed), plus deamination
    artefacts at TS-CpG sites in bins 0-3 (spurious lost-allele calls at C/T and G/A sites in the damage direction)."""
    rng = np.random.default_rng(seed)
    cls = rng.choice(3, size=S, p=[0.2, 0.25, 0.55]).astype(np.int8)
    a1 = np.empty(S, dtype=np.uint8)
    a2 = np.empty(S, dtype=np.uint8)
    tvp = [(b"A", b"C"), (b"A", b"T"), (b"G", b"T"), (b"C", b"G")]
    tsp = [(b"C", b"T"), (b"T", b"C"), (b"G", b"A"), (b"A", b"G")]
    for i in range(S):
        x, y = (tvp if cls[i] == 0 else tsp)[rng.integers(4)]
        a1[i], a2[i] = x[0], y[0]
    p0 = np.where(rng.random(S) < 0.5, rng.beta(0.3, 3.0, S), 1 - rng.beta(0.3, 3.0, S))
    nmean = np.array([49, 62, 282, 250, 300, 450, 400, 400, 700, 300, 900])
    n = rng.poisson(nmean[:, None] * rng.gamma(4, 0.25, (11, S))).astype(np.int32)
    dates = np.array([10500, 9000, 7500, 6500, 5500, 4500, 3500, 2500, 1500, 750, 100], float)
    t0 = 7000.0
    r = np.zeros((11, S), dtype=np.int32)
    # older bins: drift backwards approximated by small forward drift from p0 (symmetric), then sample
    for b in range(4):
        pb = np.clip(p0 + rng.normal(0, 0.01, S) * np.sqrt(p0 * (1 - p0)), 0, 1)
        r[b] = rng.binomial(n[b], pb)
    p = p0.copy()
    g = 0
    twoN = int(2 * ne_true)
    for b in range(4, 11):
        gb = int(round((t0 - dates[b]) / GEN_Y))
        while g < gb:
            g += 1
            p = rng.binomial(twoN, p) / twoN
        r[b] = rng.binomial(n[b], p)
    # deamination artefacts in bins 0-3 at TS-CpG sites: a C (or G) read becomes T (or A)
    for b in range(4):
        cpg = cls == 1
        c_is_a1 = np.isin(a1, [ord("C"), ord("G")])
        k_c = np.where(c_is_a1, r[b], n[b] - r[b])
        flips = rng.binomial(k_c, dmg_rate * cpg)
        r[b] = np.where(c_is_a1, r[b] - flips, r[b] + flips)
    yn = rng.poisson(60, S).astype(np.int32)
    yr = rng.binomial(yn, p0)
    blk = (np.arange(S) // max(1, S // 300)).astype(np.int32)
    nph = rng.binomial(n, 0.6).astype(np.int32)
    out = dict(n=n, r=r, nph=nph, cls=cls, a1=a1, a2=a2, blk=blk, nblk=int(blk.max() + 1), dates=dates, t0=t0)
    for ci in range(3):
        m = cls == ci
        for nm, (nn_, kk_) in (("neo", (n[2, m] + n[3, m], r[2, m] + r[3, m])), ("yam", (yn[m], yr[m]))):
            w, inv, cdf = em_prior(nn_, kk_, iters=150)
            full = np.zeros(S, dtype=np.int32)
            full[m] = inv
            out["inv_%s_%d" % (nm, ci)], out["cdf_%s_%d" % (nm, ci)], out["w_%s_%d" % (nm, ci)] = full, cdf, w
    np.savez(path, **out)
    return path


def selftest():
    rng = np.random.default_rng(3)
    # EM recovers a two-point prior
    p = np.where(rng.random(20000) < 0.3, 0.1, 0.8)
    nn = rng.integers(20, 200, 20000)
    kk = rng.binomial(nn, p)
    w, inv, cdf = em_prior(nn, kk, iters=200)
    m1 = w[(GRID > 0.05) & (GRID < 0.15)].sum()
    m2 = w[(GRID > 0.75) & (GRID < 0.85)].sum()
    assert abs(m1 - 0.3) < 0.05 and abs(m2 - 0.7) < 0.05, (m1, m2)
    d = draw_post(rng, inv, cdf)
    assert abs(np.mean(d) - np.mean(p)) < 0.02
    # interpolation
    M = [1000, 300, 150, 60, 30, 10, 3, 1]
    assert 1e4 < interp_ne(M, 200) < 2e4
    assert interp_ne(M, 5000) < 3e3 and interp_ne(M, 0) > 3e6
    # bands are exhaustive on a grid of Q values
    qs = [0, 0.1, 1 / 3, 0.5, 1, 3, 3.01, 10, float("inf")]
    seen = set(band_A1(a, b) for a in qs for b in qs)
    assert seen == {"A1-DEF", "A1-CONS", "A1-EXC", "A1-SPLIT"}, seen
    # damage-direction labelling
    a1 = np.array([ord("C"), ord("G"), ord("T"), ord("A")], dtype=np.uint8)
    a2 = np.array([ord("T"), ord("A"), ord("C"), ord("G")], dtype=np.uint8)
    fixed = a1
    lost = a2
    dmg = ((fixed == ord("C")) & (lost == ord("T"))) | ((fixed == ord("G")) & (lost == ord("A")))
    assert list(dmg) == [True, True, False, False]
    print("selftest ok")


def smoke(path, ncpu, reps=1, maxsites=None):
    tag = "c1d_tv_smoke"
    P = _load(path)
    obs = observed(P, "smoke", {"cpg_direction_valid": True}, gate=False)
    os.replace(os.path.join(RES, "c1d_tv_smoke_obs.json"), os.path.join(RES, "%s_v62_obs.json" % tag))
    secs, ntask = run_grid(path, "v62", ncpu, reps, os.path.join(RES, "%s_v62_null.jsonl" % tag), maxsites)
    S = P["n"].shape[1] if maxsites is None else min(maxsites, P["n"].shape[1])
    per_task = secs * ncpu / ntask
    print("SMOKE: %d tasks (%d scenarios x %d reps) on %d sites in %.1fs wall with %d workers; %.2f s/task" % (
        ntask, len(SCEN), reps, S, secs, ncpu, per_task))
    full_S = 1_150_639
    proj = per_task * (full_S / S) * len(SCEN) * REPS / max(ncpu, 1)
    print("SMOKE: projected main run per release at %d sites, %d reps, %d workers: %.0f s (%.1f h)" % (
        full_S, REPS, ncpu, proj, proj / 3600))
    import resource
    print("SMOKE: peak RSS of one worker %.0f MB; parent %.0f MB" % (
        resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1024,
        resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))
    if maxsites is None:
        # full-grid analysis on the synthetic file (exercises analyse); not a result
        analyse(rels=("v62",), tag=tag)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "selftest"
    if cmd == "selftest":
        selftest()
    elif cmd == "mkfake":
        mkfake(sys.argv[2], int(sys.argv[3]))
    elif cmd == "smoke":
        smoke(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]) if len(sys.argv) > 4 else 1,
              int(sys.argv[5]) if len(sys.argv) > 5 else None)
    elif cmd == "prep":
        fn, obs = prep(sys.argv[2])
        print("prep", fn, json.dumps({c: obs["ev"][c]["S21"] for c in CLS + ["TS"]}), json.dumps(obs["checks"]))
    elif cmd == "run":
        rel = sys.argv[2]
        path = os.path.join(c1d.OUT, "c1d_tv_%s_prep.npz" % rel)
        secs, nt = run_grid(path, rel, int(sys.argv[3]), int(sys.argv[4]) if len(sys.argv) > 4 else REPS,
                            os.path.join(RES, "c1d_tv_%s_null.jsonl" % rel))
        print("run %s: %d tasks in %.0fs" % (rel, nt, secs))
    elif cmd == "analyse":
        analyse()
    else:
        raise SystemExit("unknown command " + cmd)

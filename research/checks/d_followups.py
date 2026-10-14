"""D-fu (part B of check C1d-D) -- the D follow-ups: ProteinGym multi-mutant decay (B1), a noise null for D1's beneficial
proxy (B2), and per-sequence prevalence across D10 (Axe), D11 (Taylor) and D12 (Keefe & Szostak) on one basis (B3).

PRE-REGISTERED (AGENTS.md rule 5).  Written 2026-10-14 before any main run and before any of the B1/B2 data or the B3 full
texts were fetched or read for this check.  Brief: research/checks/briefs/C1d-D-analyst.md (at 1a8fae4 or later).  Prior
results already known and looked at (inputs, not outputs of this script): R4-D1-spike.md (proxy fraction s* >= 1.2 median
3.6%, IQR 0.6-9.2%; Table B rows 820-1,600x, 82-160x, 8-16x, 0.8-1.6x; mirror check: proxy indistinguishable from a
symmetric noise tail in ~70% of datasets; beneficial SNVs per codon 0.21; gene-level pool 51), the claim files D10, D11, D12
(abstract quotes; D11's full-text quotes as recorded there), and the D1 normalisation.

REVIEW TIER, FIXED HERE BEFORE ANY NUMBER IS SEEN (lead ruling 2026-10-13 under D-23, brief section "Review tier"):
  **THREE REVIEWS** (REVIEW-R4-D-fu-correctness.md, -steelman-day.md, -steelman-critic.md, one after another).
  Reason: this registration carries a possible verdict-field flip on D12: fidelity `unverifiable` -> `accurate | partial |
  misread` once the full text (PMC4476321) is read, and internal `n/a` -> `holds | arithmetic-error` if the paper derives its
  own frequency from numbers it states (section 4).  B2 also rescales D1 numbers that feed the R5-draft 1.3 row "G, G1".
  The fallback (one combined review) does not apply.

Run (isolated venv; `selftest`, `mkfake`, `smoke` are local and synthetic; everything else on na-workhorse):
    research/.venv/bin/python -I research/checks/d_followups.py selftest
    research/.venv/bin/python -I research/checks/d_followups.py mkfake <dir>                  # synthetic ProteinGym-like
    research/.venv/bin/python -I research/checks/d_followups.py smoke <dir> <ncpu>            # full B1+B2 entry on <dir>
    research/.venv/bin/python -I research/checks/d_followups.py b12 <dms_dir> <reference.csv> <ncpu>
    research/.venv/bin/python -I research/checks/d_followups.py b3 <inputs.json>
Outputs: results/raw/d_fu_b12.json, d_fu_b12.txt, d_fu_b3.json, d_fu_b3.txt.

===================================================================================================================
0. TARGETS
-------------------------------------------------------------------------------------------------------------------
D10  Axe 2004 abstract (claim file Statement): "the overall prevalence of sequences performing a specific function by any
     domain-sized fold may be as low as 1 in 10(77)"; "roughly one in 10(64) signature-consistent sequences forms a working
     domain".  quotes-literature section Axe2004.  RH: dialectic (literature).
D11  Taylor et al. 2001 (claim file Statement, full text): "a library of ~10^24 members would have been needed to obtain AroQ
     mutases"; "4,500 ... x 10^4 ... = 5 x 10^23"; "a 100-residue protein has 20^100 ... possible sequences".  RH: dialectic.
D12  Keefe & Szostak 2001 abstract: "a library of 6 x 10^12 proteins each containing 80 contiguous random amino acids ...
     four new ATP-binding proteins"; "The frequency of occurrence of functional proteins in random-sequence libraries appears
     to be similar to that observed for equivalent RNA libraries."  The paper's own numeric frequency is not in the corpus.
D    (branch root, Day side): functional proteins are a vanishing fraction of sequence space.  D1-spike section 8 open items
     "The ProteinGym multi-mutant sets ... were not analysed" and "the beneficial proxy has no noise null".
Day side for B1/B2: D2h (DMS shows ruggedness; D1-spike: "partly right") and the D-branch reading that function decays fast
  away from a functional sequence.  Critic side: D1-spike's within-gene beneficial fraction (Table B), Rosenhouse-type
  "protein space is connected" responses (D1a), and Taylor / Keefe & Szostak as counter-estimates to Axe.

===================================================================================================================
1. B1 -- MULTI-MUTANT DECAY (ProteinGym)
-------------------------------------------------------------------------------------------------------------------
Data: ProteinGym substitutions zip and reference file, the same URLs as D1 (R4-D1-spike section 1), refetched into a new
  directory (section 6).  Asserted: reference columns DMS_id, DMS_filename, UniProt_ID, target_seq, coarse_selection_type;
  every parsed substitution's wild-type letter equals target_seq[pos - 1] in >= 99% of a file's rows (else the file is
  skipped and listed).  sha256 compared with D1's (zip 3a837662..., reference a8f49801...); a different file is used and
  labelled, not refused.
Normalisation (identical to D1's dms_one): from the file's single substitutions, N_hat = median of the lowest 5% of scores,
  W_hat = median score at the top quartile of sites by median score (sites with >= 5 singles); s* = (score - N_hat) /
  (W_hat - N_hat).  Files with < 100 singles, < 15 sites or < 8 sites with >= 5 singles get no baseline and are excluded
  from B1 and B2 (counted).
Per multi-mutant file (any variant with >= 2 substitutions), for each k with >= 30 variants:
  f_obs(k) = share of k-mutants with s* >= 0.5 (also at 0.3 and 0.8, reported only);
  on the k-mutants whose every component single is measured: f_ind(k) = mean over variants of prod_i 1[s*_i >= 0.5] (the
  independence, i.e. multiplication, prediction: a combination works iff each part works alone), f_sub(k) = observed share
  functional on the same variants, eps(k) = f_sub(k) / f_ind(k) (defined if >= 30 such variants and f_ind(k) > 0);
  d(k) = median over those variants of [s*_obs - prod_i max(s*_i, 0)] (continuous multiplicative residual, reported only);
  decay: slope of log10 f_obs(k) on k over k = 1.. with f_obs > 0 -> per-substitution retention r = 10^slope; curvature =
  quadratic coefficient where >= 4 k values (negative = accelerating decay).
  m2 = median over files of log10 eps(2);  m3 = median over files of mean_{k >= 3} log10 eps(k).
Bands (each on its own statistic; first clause that applies):
  B1-INSUFF  fewer than 5 files with eps(2) (primary) / fewer than 3 files with any eps(k >= 3) (secondary).
  B1-SYN     m < -0.1    combinations work less often than the product of their parts predicts (synergistic).
  B1-IND     -0.1 <= m <= 0.1    within 1.26x of independence.
  B1-ANT     m > 0.1     combinations work more often than the product predicts (antagonistic / buffering).
  Reachability: SYN results if pairs of individually tolerated substitutions often fail together (threshold or stability
  epistasis); ANT results if combinations that include an individually non-functional substitution are often functional.

===================================================================================================================
2. B2 -- A NOISE NULL FOR THE BENEFICIAL PROXY (registered before looking)
-------------------------------------------------------------------------------------------------------------------
ProteinGym carries no replicate scores, so the null is cross-assay replication.  Qualifying pair: two files with the same
  UniProt_ID, both normalisable, >= 200 shared single substitutions (same mutant string; the +-5-residue context around each
  shared position identical in both target_seq at >= 90% of shared positions, else the pair is skipped as a numbering
  mismatch).  Classes on s*: beneficial (>= 1.2, D1's proxy), non-functional (< 0.5, the POSITIVE CONTROL), destroyed (< 0.2,
  reported only: the selftest showed that with D1's N_hat (median of the lowest 5%) the 0.2 cut runs through the dead mode,
  so its replication measures within-mode noise and cannot serve as a control).
For each ordered pair (X -> Y) with >= 5 calls of the class in X among the shared variants:
  b = P(class in Y) on the shared set;  rho = P(class in Y | class in X);
  U = 1 - max(0, rho - b) / (1 - b): the largest share of X's calls that can be noise, if a real call in X is also a call in
  Y.  (A real gain that Y's assay cannot see -- ceiling, different phenotype -- also raises U, so U is an UPPER bound on the
  noise share: Day-favourable by construction.)
  Per protein: mean U over its qualifying directions; U~ = median over proteins.  Control: U~_ctrl, same recipe on the
  non-functional class.
  Also the Spearman correlation of s* on shared singles, per pair (reported).
Bands:
  B2-UNVALIDATED  U~_ctrl >= 0.5 (the replication null fails its own positive control; no use in any verdict).
  B2-INSUFF       fewer than 3 proteins with a qualifying direction.
  B2-REAL         U~ < 0.3       most beneficial calls replicate.
  B2-MIXED        0.3 <= U~ < 0.7.
  B2-NOISE        U~ >= 0.7      most beneficial calls do not replicate beyond chance.
Downstream (registered arithmetic, all bands): D1's real-beneficial lower bounds = proxy x (1 - U~): proxy fraction 3.6%
  (0.6-9.2%), per-codon 0.21, gene pool 51, and the four Table B rows (820-1,600x; 82-160x; 8-16x; 0.8-1.6x).  A row whose
  rescaled upper end falls below 1 is reported as "no longer clears G1's requirement on the lower bound".

===================================================================================================================
3. B3 -- PER-SEQUENCE PREVALENCE ON ONE BASIS (arithmetic; the registration fixes the basis and the decomposition before
   the full texts are read)
-------------------------------------------------------------------------------------------------------------------
Inputs come from results/raw/d_fu_b3_inputs.json, written in the run task from the fetched texts and committed BEFORE `b3`
  runs.  Schema per source (Axe, Taylor, KS): f (per-sequence prevalence as the source states it), f_kind (central |
  lower_bound | as_low_as), L (residues of the randomised region), function (label), and for each of f and L a verbatim quote
  with locator, URL and access date.  The script asserts that each number's literal string occurs in its quote (a derived
  value, e.g. 4 / 6e12, lists every literal it is computed from).  If a
  source gives no L or no f, the field is `unverifiable` and a bracket is used: L_Axe in [100, 250] if the abstract does not
  give it; f_KS = 4 / 6e12 (the abstract's numbers, a lower bound if all four binders were in the starting library) if the
  full text gives no frequency.
Basis and decomposition:
  I_s = -log10 f_s (orders of magnitude of rarity); d_s = I_s / L_s (orders per residue); f_s(100) = 10^(-100 d_s)
  (prevalence moved to a common 100-residue length at constant information per residue -- a model, stated as such).
  For a pair (A, B): Delta = I_A - I_B = Delta_len + Delta_dens exactly, with Delta_len = dbar (L_A - L_B) (the length, i.e.
  units, part) and Delta_dens = (d_A - d_B) Lbar (the information-density part: function stringency plus method).
  Estimator part (units): where a relay compares K&S's bound 4/6e12 instead of the paper's own estimate, Delta_est =
  I(bound) - I(estimate) is added to the units part.
  Spread: S_raw = max - min of log10 f_s; S_100 = max - min of log10 f_s(100); units share U3 = 1 - S_100 / S_raw.
  Named parts: function component = Delta_dens(Taylor, KS) (catalysis vs ATP binding); method component =
  Delta_dens(Axe, Taylor) (two estimates for specific enzyme catalysis).
Bands:
  B3-UNITS   U3 >= 0.5     most of the apparent disagreement is units.
  B3-PARTLY  0.2 <= U3 < 0.5.
  B3-REAL    U3 < 0.2 (including negative).
  Method sub-band: AT-CONC if |Delta_dens(Axe, Taylor)| <= 3 orders, else AT-DISC.
  B3-BRACKET a bracket is in use and the four bracket corners do not all give the same band: unresolved, no call (the
             corners and the L_Axe at which the band changes are reported).  The same rule makes the AT sub-band
             "AT-BRACKET" if the corners disagree.
  Disclosure (2026-10-14, before commit, no real input seen): the selftest ran b3 on MY OWN guessed inputs (f_Axe 1e-77 with
  L_Axe bracket [100, 250]; f_Taylor 2e-24, L 100; f_KS 1e-11, L 80).  It showed that U3 is decided almost entirely by
  L_Axe (U3 = 0.04 at L_Axe 100, 0.43 at 150, 0.54 at 175, 0.74 at 250), so a midpoint call would let my bracket choose the
  band.  The B3-BRACKET band replaced a midpoint rule and PA-B3d was added after that run; PA-B3a's band was kept.

===================================================================================================================
4. PREDICTIONS (each can fail)
-------------------------------------------------------------------------------------------------------------------
Day side:
  PD-B1  B1 secondary (k >= 3) band B1-SYN: function falls faster than the product of single-site tolerances.  Reached if
         m3 < -0.1.
  PD-B2  B2-NOISE: most proxy-beneficial calls are noise, so D1's gene-level beneficial pool and Table B are inflated.
         Reached if U~ >= 0.7 with the control passing.
  PD-B3  B3-UNITS or AT-CONC: Axe's figure is not contradicted by the other two once they share a basis.  Reached if U3 >= 0.5
         or |Delta_dens(Axe, Taylor)| <= 3.  Unresolved (neither hit nor miss) under B3-BRACKET with AT-DISC.
Critic side:
  PC-B1  B1 secondary band B1-IND or B1-ANT: no evidence that combinations fail faster than independence predicts, so
         product-type extrapolations are not optimistic.  Reached if m3 >= -0.1.
  PC-B2  B2-REAL: the beneficial proxy mostly replicates.  Reached if U~ < 0.3 with the control passing.
  PC-B3  B3-REAL or B3-PARTLY, with AT-DISC: on a common basis Axe's catalytic figure remains far below Taylor's measured-
         and-extrapolated catalytic figure.  Reached if U3 < 0.5 and |Delta_dens(Axe, Taylor)| > 3.  Unresolved under
         B3-BRACKET.
The audit's own (numbers mine, before any fetch):
  PA-B1a  B1 primary B1-IND with m2 in [-0.2, 0.05].
  PA-B1b  B1 secondary B1-SYN with m3 in [-1.0, -0.1].
  PA-B1c  median per-substitution retention r over files in [0.4, 0.85].
  PA-B2a  B2-NOISE with U~ in [0.55, 0.9] (central 0.72; probability of NOISE ~0.55).
  PA-B2b  the control passes: U~_ctrl in [0.05, 0.45]; median Spearman over pairs in [0.3, 0.7].
  PA-B2c  the Table B row n = 2e7, p = 0.002 (0.8-1.6x) falls below 1 at its upper end after rescaling; the row n = 2e5,
          p = 0.02 stays above 100x.
  PA-B3a  B3-PARTLY with U3 in [0.2, 0.5] (central 0.35), from my expectation f_Axe 1e-77 at L ~150, f_Taylor ~2e-24 at
          L 100, f_KS ~1e-11 at L 80.
  PA-B3b  AT-DISC with Delta_dens(Axe, Taylor) in [20, 45] orders; function component Delta_dens(Taylor, KS) in [5, 15].
  PA-B3c  the K&S full text states a frequency of order 1e-11 (within 10x), so D12 fidelity moves to `accurate`.
  PA-B3d  the Axe abstract states the length of the domain it assessed (so no L_Axe bracket is needed and B3 is not
          B3-BRACKET).

===================================================================================================================
5. WHAT EACH BAND LICENSES (moves are proposed to the operator / lead; nothing here is applied by the analyst)
-------------------------------------------------------------------------------------------------------------------
Verdict-FIELD moves this registration can carry (hence three reviews):
  D12 fidelity: unverifiable -> accurate if the full text's frequency and setup match the claim title and the abstract
    quote; partial if they match with a material qualifier the title omits (e.g. a frequency for a pre-enriched or
    pre-selected library, or a different length); misread if the full text contradicts the title.  If the full text cannot
    be retrieved, the field stays `unverifiable`.
  D12 internal: n/a -> holds if the paper's stated frequency follows (within 25%, rule R1) from numbers it states;
    arithmetic-error if it does not; stays n/a if the paper gives no derivation.
No band moves D10 internal (needs the paywalled full text; stays `pending`), D10/D11/D12 external (stay `contested`: the
  three measure different functions; B3 sizes the disagreement, it does not adjudicate it), D11 internal/fidelity, or any
  field on D.  Comments: B3 numbers go into the D10, D11, D12 and D claim files ("R4 D-fu" paragraphs); B1 -> D10 (the
  multiplication assumption tested locally, k <= the largest k measured) and D2h; B2 -> D1-spike follow-up and the G1 /
  G3b comments citing Table B.
Candidate defeaters: B1-SYN (Day side) against "product extrapolations are pessimistic"; B1-ANT (critic side) against
  "function collapses under accumulated substitutions"; B2-NOISE (Day side) against D1's Table B as an estimate; B2-REAL
  (critic side) against "the proxy is noise"; B3-UNITS (Day side) against "Taylor / K&S contradict Axe"; B3-REAL with
  AT-DISC (critic side) against reading Axe's figure as typical of enzyme function.
Escalation clause (brief): if the lead judges any of these to move a verdict or defeater on D itself or on C2 / C2a, that is
  load-bearing; it is reported, not applied.  The tier above is already three reviews.

===================================================================================================================
6. RESOURCES AND COMMANDS (host only for real data; one agent at a time; <= 11 busy processes in total; `uptime` first)
-------------------------------------------------------------------------------------------------------------------
Fetches (run task; read-only; never executed; each in its own new directory; sha256 + access date in raw/d_fu.host):
  sources/raw/dfu-proteingym-<date>/  : https://marks.hms.harvard.edu/proteingym/ProteinGym_v1.3/DMS_ProteinGym_substitutions.zip
                                        https://raw.githubusercontent.com/OATML-Markslab/ProteinGym/main/reference_files/DMS_substitutions.csv
                                        (unzip -q into x/; CSVs are read as text only)
  sources/raw/dfu-keefeszostak-<date>/: PMC4476321 (Europe PMC full-text XML or the PMC article page)
  sources/raw/dfu-taylor-<date>/      : PMC58511 (same routes)
  sources/raw/dfu-axe-<date>/         : Europe PMC abstract, PMID 15321723 (full text paywalled; no bypass, rule 6)
Launch B1+B2 (4 workers; ~1 GB total expected; smoke first on the real directory with a file limit):
  ssh -o BatchMode=yes na-workhorse 'cd ~/projects/evo-sim && nohup sh -c "\
    D_FU_MAXFILES=12 research/.venv/bin/python -I research/checks/d_followups.py b12 <dir>/x/DMS_ProteinGym_substitutions <dir>/DMS_substitutions.csv 4 && \
    mv research/checks/results/raw/d_fu_b12.json research/checks/results/raw/d_fu_b12_hostsmoke.json && \
    research/.venv/bin/python -I research/checks/d_followups.py b12 <dir>/x/DMS_ProteinGym_substitutions <dir>/DMS_substitutions.csv 4" \
    > research/checks/results/raw/d_fu_b12.out 2>&1 < /dev/null &'
B3 is arithmetic (local is fine): `d_followups.py b3 research/checks/results/raw/d_fu_b3_inputs.json` after the inputs file is
  committed.
Cost: measured in section 7 on synthetic data; the host smoke (12 files) prints seconds per file and peak RSS; if the
  projection for all files exceeds 2 h or 2 GB per worker, the run task stops and reports instead of launching.

===================================================================================================================
7. LOCAL SMOKE (synthetic data only; workstation, 2026-10-14)
-------------------------------------------------------------------------------------------------------------------
`selftest`: B1 on a threshold-model multi-mutant set gives log10 eps(k >= 3) = -0.23 (B1-SYN direction) and on an exact-
  independence set log10 eps(2) = 0.00; B2 on a clean two-assay protein gives U = 0.00 and on a pure-noise pair U = 0.96,
  with the control U = 0.00 and 0.22; B3 identity Delta = Delta_len + Delta_dens holds, the literal-in-quote assertion fires
  on a bad input, a bracketed L_Axe gives B3-BRACKET and a quoted L_Axe = 153 gives B3-PARTLY (U3 0.45).
  Changes made BEFORE this commit because of the selftest (synthetic only): (1) the positive control moved from "destroyed"
  (< 0.2) to "non-functional" (< 0.5), because D1's N_hat puts the 0.2 cut inside the dead mode; (2) the clean synthetic
  pair's noise was lowered to 0.05 after U correctly reported 0.68 for a pair whose true noise share was 63%; (3) B3-BRACKET
  (see section 3 disclosure).
`mkfake` + `smoke <dir> 2`: real entry point (`run_b12`), Pool of 2, 6 files, 0.1 s wall, peak RSS 31 MB per worker.
  No real data were read.
"""
import os
import sys
import csv
import json
import math
import time
import resource
import numpy as np
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.environ.get("D_FU_RES", os.path.join(HERE, "results", "raw"))
AAS = "ACDEFGHIKLMNPQRSTVWY"
TH_FUNC, TH_BEN, TH_DEAD = 0.5, 1.2, 0.2
TH_SENS = (0.3, 0.5, 0.8)
MINK = 30
D1_PROXY = dict(frac_median=0.0357, frac_iqr=(0.0056, 0.0918), per_codon=0.21, gene_pool=51)
D1_TABLEB = {"n2e5_p0.02": (820, 1600), "n2e5_p0.002": (82, 160), "n2e7_p0.02": (8, 16), "n2e7_p0.002": (0.8, 1.6)}
SHA_D1 = dict(zip="3a83766254ac9ac9984ec25cb73c6e010ea4418f5e35f143933e6b6e6473b921",
              ref="a8f498011532a74aa9fe556a50555a75e928c5837d19c06a87592ae04049b308")


# --------------------------------------------------------------------------------------------------- parsing / normalising
def parse_mut(m, seq):
    """'A23G:L45P' -> list of (wt, pos, mt) or None; wt_ok = all wt letters match seq."""
    out, ok = [], True
    for c in m.split(":"):
        if len(c) < 3 or c[0] not in AAS or c[-1] not in AAS:
            return None, False
        try:
            pos = int(c[1:-1])
        except ValueError:
            return None, False
        if not (1 <= pos <= len(seq)) or seq[pos - 1] != c[0]:
            ok = False
        out.append((c[0], pos, c[-1]))
    return out, ok


def baseline(single_sites, single_scores):
    """D1's dms_one normalisation.  Returns (N_hat, W_hat) or None."""
    sc = np.asarray(single_scores, float)
    si = np.asarray(single_sites)
    if len(sc) < 100:
        return None
    us = np.unique(si)
    if len(us) < 15:
        return None
    N_hat = float(np.median(np.sort(sc)[: max(5, int(0.05 * len(sc)))]))
    med = np.array([np.median(sc[si == s]) if (si == s).sum() >= 5 else np.nan for s in us])
    ok = ~np.isnan(med)
    if ok.sum() < 8:
        return None
    thr = np.nanpercentile(med, 75)
    top = us[ok & (med >= thr)]
    W_hat = float(np.median(sc[np.isin(si, top)]))
    if W_hat - N_hat < 1e-9:
        return None
    return N_hat, W_hat


def per_file(args):
    path, meta = args
    t = time.time()
    seq = meta["target_seq"]
    singles, multis = {}, []
    nrows, nbadwt = 0, 0
    with open(path, newline="") as fh:
        for r in csv.DictReader(fh):
            try:
                s = float(r["DMS_score"])
            except (ValueError, KeyError):
                continue
            if not math.isfinite(s):
                continue
            comps, ok = parse_mut(r["mutant"], seq)
            if comps is None:
                continue
            nrows += 1
            nbadwt += (not ok)
            if len(comps) == 1:
                singles[r["mutant"]] = s
            else:
                multis.append((tuple("%s%d%s" % c for c in comps), s))
    res = dict(DMS_id=meta["DMS_id"], uniprot=meta["UniProt_ID"], assay=meta["coarse_selection_type"], n_rows=nrows,
               n_single=len(singles), n_multi=len(multis), wt_match=(1 - nbadwt / nrows) if nrows else None)
    if nrows == 0 or nbadwt / nrows > 0.01:
        res["skip"] = "wt mismatch" if nrows else "no rows"
        return res
    keys = list(singles)
    bl = baseline([int(k[1:-1]) for k in keys], [singles[k] for k in keys])
    if bl is None:
        res["skip"] = "no single baseline"
        return res
    N_hat, W_hat = bl
    res["N_hat"], res["W_hat"] = N_hat, W_hat
    ss = {k: (v - N_hat) / (W_hat - N_hat) for k, v in singles.items()}
    res["sstar_single"] = ss
    if multis:
        res["b1"] = b1_tables(ss, [(c, (s - N_hat) / (W_hat - N_hat)) for c, s in multis])
    res["secs"] = time.time() - t
    return res


def b1_tables(ss, ms):
    """ss: single -> s*; ms: list of (components, s*).  Per-k tables."""
    byk = {}
    for comps, s in ms:
        byk.setdefault(len(comps), []).append((comps, s))
    sv = np.array(list(ss.values()))
    tab = {1: dict(n=len(sv), f_obs={str(th): float((sv >= th).mean()) for th in TH_SENS})}
    for k, lst in sorted(byk.items()):
        if len(lst) < MINK:
            continue
        s_all = np.array([s for _, s in lst])
        row = dict(n=len(lst), f_obs={str(th): float((s_all >= th).mean()) for th in TH_SENS})
        sub = [(c, s) for c, s in lst if all(x in ss for x in c)]
        row["n_sub"] = len(sub)
        if len(sub) >= MINK:
            for th in TH_SENS:
                ind = np.array([np.prod([ss[x] >= th for x in c]) for c, _ in sub], float)
                obs = np.array([s >= th for _, s in sub], float)
                fi, fo = float(ind.mean()), float(obs.mean())
                row.setdefault("f_ind", {})[str(th)] = fi
                row.setdefault("f_sub", {})[str(th)] = fo
                row.setdefault("eps", {})[str(th)] = (fo / fi) if fi > 0 else None
            pred = np.array([np.prod([max(ss[x], 0.0) for x in c]) for c, _ in sub])
            row["d_median"] = float(np.median(np.array([s for _, s in sub]) - pred))
        tab[k] = row
    ks = [k for k in sorted(tab) if tab[k]["f_obs"][str(TH_FUNC)] > 0]
    if len(ks) >= 2:
        y = np.log10([tab[k]["f_obs"][str(TH_FUNC)] for k in ks])
        slope = float(np.polyfit(ks, y, 1)[0])
        curv = float(np.polyfit(ks, y, 2)[0]) if len(ks) >= 4 else None
        decay = dict(ks=ks, slope=slope, r=10 ** slope, curvature=curv)
    else:
        decay = None
    return dict(tab={str(k): v for k, v in tab.items()}, decay=decay)


# --------------------------------------------------------------------------------------------------- B1 / B2 aggregation
def summarise_b1(files):
    e2, e3, rs, perfile = [], [], [], {}
    for f in files:
        b = f.get("b1")
        if not b:
            continue
        tab = b["tab"]
        le2 = None
        if "2" in tab and tab["2"].get("eps", {}).get(str(TH_FUNC)):
            le2 = math.log10(tab["2"]["eps"][str(TH_FUNC)])
            e2.append(le2)
        l3 = [math.log10(v["eps"][str(TH_FUNC)]) for k, v in tab.items()
              if int(k) >= 3 and v.get("eps", {}).get(str(TH_FUNC))]
        le3 = float(np.mean(l3)) if l3 else None
        if le3 is not None:
            e3.append(le3)
        if b["decay"]:
            rs.append(b["decay"]["r"])
        perfile[f["DMS_id"]] = dict(log10_eps2=le2, log10_eps_k3plus=le3, decay=b["decay"],
                                    kmax=max(int(k) for k in tab), n_multi=f["n_multi"])
    m2 = float(np.median(e2)) if e2 else None
    m3 = float(np.median(e3)) if e3 else None

    def band(m, n, nmin):
        if n < nmin:
            return "B1-INSUFF"
        return "B1-SYN" if m < -0.1 else ("B1-ANT" if m > 0.1 else "B1-IND")
    sens = {}
    for th in TH_SENS:
        x = [math.log10(f["b1"]["tab"]["2"]["eps"][str(th)]) for f in files if f.get("b1") and "2" in f["b1"]["tab"]
             and f["b1"]["tab"]["2"].get("eps", {}).get(str(th))]
        sens[str(th)] = float(np.median(x)) if x else None
    return dict(m2=m2, n2=len(e2), m3=m3, n3=len(e3), band_primary=band(m2, len(e2), 5),
                band_secondary=band(m3, len(e3), 3), r_median=float(np.median(rs)) if rs else None, n_decay=len(rs),
                m2_by_threshold=sens, perfile=perfile)


def context_ok(seqA, seqB, positions, w=5):
    good = 0
    for p in positions:
        a = seqA[max(0, p - 1 - w): p + w]
        b = seqB[max(0, p - 1 - w): p + w]
        good += (a == b)
    return good / max(1, len(positions))


def U_stat(cx, cy):
    """cx, cy boolean arrays (class calls in X and Y on the shared set)."""
    nx = int(cx.sum())
    if nx < 5:
        return None
    b = float(cy.mean())
    if b >= 1:
        return None
    rho = float(cy[cx].mean())
    return dict(U=1 - max(0.0, rho - b) / (1 - b), rho=rho, b=b, nx=nx)


def summarise_b2(files, seqs):
    from scipy.stats import spearmanr
    ok = [f for f in files if "sstar_single" in f]
    byp = {}
    for f in ok:
        byp.setdefault(f["uniprot"], []).append(f)
    pairs, prot = [], {}
    for up, lst in byp.items():
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                X, Y = lst[i], lst[j]
                shared = sorted(set(X["sstar_single"]) & set(Y["sstar_single"]))
                rec = dict(uniprot=up, X=X["DMS_id"], Y=Y["DMS_id"], n_shared=len(shared))
                if len(shared) < 200:
                    rec["skip"] = "shared < 200"
                    pairs.append(rec)
                    continue
                cf = context_ok(seqs[X["DMS_id"]], seqs[Y["DMS_id"]], sorted({int(m[1:-1]) for m in shared}))
                rec["context_identity"] = cf
                if cf < 0.9:
                    rec["skip"] = "numbering mismatch"
                    pairs.append(rec)
                    continue
                sx = np.array([X["sstar_single"][m] for m in shared])
                sy = np.array([Y["sstar_single"][m] for m in shared])
                rec["spearman"] = float(spearmanr(sx, sy).statistic)
                for nm, fn in (("ben", lambda s: s >= TH_BEN), ("ctrl", lambda s: s < TH_FUNC),
                               ("dead", lambda s: s < TH_DEAD)):
                    rec[nm] = [U_stat(fn(sx), fn(sy)), U_stat(fn(sy), fn(sx))]
                pairs.append(rec)
                for nm in ("ben", "ctrl", "dead"):
                    for d in rec[nm]:
                        if d is not None:
                            prot.setdefault(up, {}).setdefault(nm, []).append(d["U"])
    pu = {up: {nm: float(np.mean(v)) for nm, v in d.items()} for up, d in prot.items()}
    ub = [d["ben"] for d in pu.values() if "ben" in d]
    ud = [d["ctrl"] for d in pu.values() if "ctrl" in d]
    udd = [d["dead"] for d in pu.values() if "dead" in d]
    Ut = float(np.median(ub)) if ub else None
    Ud = float(np.median(ud)) if ud else None
    if Ud is not None and Ud >= 0.5:
        band = "B2-UNVALIDATED"
    elif len(ub) < 3:
        band = "B2-INSUFF"
    elif Ut < 0.3:
        band = "B2-REAL"
    elif Ut < 0.7:
        band = "B2-MIXED"
    else:
        band = "B2-NOISE"
    sp = [p["spearman"] for p in pairs if "spearman" in p]
    down = None
    if Ut is not None:
        k = 1 - Ut
        down = dict(factor=k, frac_median=D1_PROXY["frac_median"] * k,
                    frac_iqr=[x * k for x in D1_PROXY["frac_iqr"]], per_codon=D1_PROXY["per_codon"] * k,
                    gene_pool=D1_PROXY["gene_pool"] * k,
                    tableB={r: [lo * k, hi * k] for r, (lo, hi) in D1_TABLEB.items()},
                    tableB_below1=[r for r, (lo, hi) in D1_TABLEB.items() if hi * k < 1])
    return dict(U_ben=Ut, U_ctrl=Ud, U_dead=float(np.median(udd)) if udd else None, n_prot_ben=len(ub),
                n_prot_ctrl=len(ud), band=band,
                spearman_median=float(np.median(sp)) if sp else None, n_pairs_used=len(sp), per_protein=pu,
                pairs=pairs, downstream=down)


def score_b12(b1, b2):
    s = {}
    s["PD-B1"] = b1["band_secondary"] == "B1-SYN"
    s["PC-B1"] = b1["band_secondary"] in ("B1-IND", "B1-ANT")
    s["PD-B2"] = b2["band"] == "B2-NOISE"
    s["PC-B2"] = b2["band"] == "B2-REAL"
    s["PA-B1a"] = b1["band_primary"] == "B1-IND" and b1["m2"] is not None and -0.2 <= b1["m2"] <= 0.05
    s["PA-B1b"] = b1["band_secondary"] == "B1-SYN" and b1["m3"] is not None and -1.0 <= b1["m3"] <= -0.1
    s["PA-B1c"] = b1["r_median"] is not None and 0.4 <= b1["r_median"] <= 0.85
    s["PA-B2a"] = b2["band"] == "B2-NOISE" and 0.55 <= b2["U_ben"] <= 0.9
    s["PA-B2b"] = (b2["U_ctrl"] is not None and 0.05 <= b2["U_ctrl"] <= 0.45 and b2["spearman_median"] is not None
                   and 0.3 <= b2["spearman_median"] <= 0.7)
    d = b2["downstream"]
    s["PA-B2c"] = bool(d) and ("n2e7_p0.002" in d["tableB_below1"]) and d["tableB"]["n2e5_p0.02"][0] > 100
    return {k: bool(v) for k, v in s.items()}


def run_b12(dms_dir, ref_csv, ncpu, tag="d_fu_b12"):
    ref = list(csv.DictReader(open(ref_csv, newline="")))
    need = ("DMS_id", "DMS_filename", "UniProt_ID", "target_seq", "coarse_selection_type")
    for c in need:
        assert c in ref[0], "reference column missing: %s" % c
    maxf = int(os.environ.get("D_FU_MAXFILES", "0")) or None
    tasks = []
    for r in ref:
        p = os.path.join(dms_dir, r["DMS_filename"])
        if os.path.exists(p):
            tasks.append((p, {k: r[k] for k in need}))
    missing = len(ref) - len(tasks)
    if maxf:
        tasks = tasks[:maxf]
    t = time.time()
    with Pool(ncpu) as pool:
        files = pool.map(per_file, tasks, chunksize=1)
    wall = time.time() - t
    seqs = {m["DMS_id"]: m["target_seq"] for _, m in tasks}
    b1 = summarise_b1(files)
    b2 = summarise_b2(files, seqs)
    out = dict(n_ref=len(ref), n_files=len(tasks), n_missing=missing,
               skipped={f["DMS_id"]: f["skip"] for f in files if "skip" in f},
               n_multi_files=sum(1 for f in files if f.get("b1")), b1=b1, b2=b2, score=score_b12(b1, b2),
               wall_s=wall, secs_per_file=[f.get("secs") for f in files],
               peak_rss_mb_worker=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1024)
    json.dump(out, open(os.path.join(RES, tag + ".json"), "w"), indent=1, default=float)
    L = ["B1+B2: %d files (%d missing on disk), %d skipped, %d multi-mutant files with B1 tables; wall %.1fs, peak RSS/worker "
         "%.0f MB" % (len(tasks), missing, len(out["skipped"]), out["n_multi_files"], wall, out["peak_rss_mb_worker"]),
         "B1 primary %s m2=%s (n=%d); secondary %s m3=%s (n=%d); r median %s (n=%d); m2 by threshold %s" % (
             b1["band_primary"], b1["m2"], b1["n2"], b1["band_secondary"], b1["m3"], b1["n3"], b1["r_median"],
             b1["n_decay"], b1["m2_by_threshold"]),
         "B2 %s U_ben=%s (proteins %d) U_ctrl=%s (proteins %d) U_dead(report) %s spearman median %s (pairs %d)" % (
             b2["band"], b2["U_ben"], b2["n_prot_ben"], b2["U_ctrl"], b2["n_prot_ctrl"], b2["U_dead"],
             b2["spearman_median"], b2["n_pairs_used"]),
         "B2 downstream %s" % json.dumps(b2["downstream"], default=float),
         "score %s" % json.dumps(out["score"])]
    txt = "\n".join(L)
    open(os.path.join(RES, tag + ".txt"), "w").write(txt + "\n")
    print(txt)
    return out


# --------------------------------------------------------------------------------------------------- B3
def b3(inputs_path, tag="d_fu_b3"):
    J = json.load(open(inputs_path))
    src = {}
    for s in ("Axe", "Taylor", "KS"):
        e = J[s]
        rec = dict(function=e["function"], f_kind=e["f_kind"])
        for fld in ("f", "L"):
            v = e[fld]
            if isinstance(v, dict) and "bracket" in v:
                rec[fld] = v["bracket"]
                rec[fld + "_status"] = "unverifiable (bracket)"
            else:
                q = v["quote"]
                for lit in v.get("literals", [v.get("literal")]):
                    assert lit is not None and str(lit) in q, "%s.%s: literal %r not in its quote" % (s, fld, lit)
                for k in ("locator", "url", "accessed"):
                    assert v.get(k), "%s.%s missing %s" % (s, fld, k)
                rec[fld] = [float(v["value"]), float(v["value"])]
                rec[fld + "_status"] = "quoted"
        src[s] = rec

    def compute(choice):
        f = {s: src[s]["f"][choice[s][0]] for s in src}
        L = {s: src[s]["L"][choice[s][1]] for s in src}
        I = {s: -math.log10(f[s]) for s in src}
        d = {s: I[s] / L[s] for s in src}
        f100 = {s: -100 * d[s] for s in src}
        pairs = {}
        for A, B in (("Axe", "Taylor"), ("Axe", "KS"), ("Taylor", "KS")):
            dbar, Lbar = (d[A] + d[B]) / 2, (L[A] + L[B]) / 2
            dl, dd = dbar * (L[A] - L[B]), (d[A] - d[B]) * Lbar
            assert abs((I[A] - I[B]) - (dl + dd)) < 1e-9
            pairs["%s-%s" % (A, B)] = dict(Delta=I[A] - I[B], Delta_len=dl, Delta_dens=dd,
                                           len_share=dl / (I[A] - I[B]) if I[A] != I[B] else None)
        lf = [-I[s] for s in src]
        S_raw = max(lf) - min(lf)
        S_100 = max(f100.values()) - min(f100.values())
        U3 = 1 - S_100 / S_raw if S_raw > 0 else None
        band = "B3-UNITS" if U3 >= 0.5 else ("B3-PARTLY" if U3 >= 0.2 else "B3-REAL")
        at = pairs["Axe-Taylor"]["Delta_dens"]
        return dict(f=f, L=L, I=I, d=d, log10_f100=f100, pairs=pairs, S_raw=S_raw, S_100=S_100, U3=U3, band=band,
                    method_component=at, function_component=pairs["Taylor-KS"]["Delta_dens"],
                    AT="AT-CONC" if abs(at) <= 3 else "AT-DISC")
    corners = {}
    for ia in (0, 1):
        for il in (0, 1):
            ch = {s: (ia, il) for s in src}
            corners["f%d_L%d" % (ia, il)] = compute(ch)
    # midpoint: geometric for f, arithmetic for L
    for s in src:
        lo, hi = src[s]["f"]
        src[s]["f"] = [lo, hi, math.sqrt(lo * hi)]
        lo, hi = src[s]["L"]
        src[s]["L"] = [lo, hi, (lo + hi) / 2]
    centre = compute({s: (2, 2) for s in src})
    bands = {c["band"] for c in corners.values()}
    ats = {c["AT"] for c in corners.values()}
    band = centre["band"] if len(bands) == 1 else "B3-BRACKET"
    AT = centre["AT"] if len(ats) == 1 else "AT-BRACKET"
    out = dict(sources={s: {k: v for k, v in src[s].items()} for s in src}, centre=centre, corners=corners,
               band=band, AT=AT, bracket_in_use=any(src[s][k + "_status"] != "quoted" for s in src for k in ("f", "L")))
    c = centre
    sc = {}
    if band == "B3-BRACKET":
        sc["PD-B3"] = True if AT == "AT-CONC" else None
        sc["PC-B3"] = None
    else:
        sc["PD-B3"] = band == "B3-UNITS" or AT == "AT-CONC"
        sc["PC-B3"] = band in ("B3-REAL", "B3-PARTLY") and AT == "AT-DISC"
    sc["PA-B3a"] = band == "B3-PARTLY" and 0.2 <= c["U3"] <= 0.5
    sc["PA-B3b"] = AT == "AT-DISC" and 20 <= c["method_component"] <= 45 and 5 <= c["function_component"] <= 15
    ks = J["KS"]["f"]
    sc["PA-B3c"] = (not (isinstance(ks, dict) and "bracket" in ks)) and 1e-12 <= float(ks["value"]) <= 1e-10
    sc["PA-B3d"] = src["Axe"]["L_status"] == "quoted"
    out["score"] = {k: (None if v is None else bool(v)) for k, v in sc.items()}
    json.dump(out, open(os.path.join(RES, tag + ".json"), "w"), indent=1, default=float)
    L = ["B3 band %s, %s; centre U3 %.3f S_raw %.1f S_100 %.1f method(Axe-Taylor) %.1f function(Taylor-KS) %.1f" % (
        band, AT, c["U3"], c["S_raw"], c["S_100"], c["method_component"], c["function_component"]),
        "pairs %s" % json.dumps(c["pairs"], default=float),
        "corners %s" % json.dumps({k: [v["band"], round(v["U3"], 3), v["AT"]] for k, v in corners.items()}),
        "score %s" % json.dumps(out["score"])]
    txt = "\n".join(L)
    open(os.path.join(RES, tag + ".txt"), "w").write(txt + "\n")
    print(txt)
    return out


# --------------------------------------------------------------------------------------------------- synthetic
def _seq(rng, L):
    return "".join(rng.choice(list(AAS), L))


def mkfake(d, seed=5):
    """Synthetic ProteinGym-like directory.  P1: two assays of the same protein, real gains at 3% of singles (true s* 1.5)
    plus noise sd 0.05 -> beneficial calls mostly replicate.  P2: two assays with NO real gains (noise sd 0.25) -> the
    beneficial calls are pure noise.  P3: a multi-mutant set under a threshold (stability) model -> synergistic.  P4: a
    multi-mutant set under exact independence (functional iff all parts functional) -> eps ~ 1."""
    rng = np.random.default_rng(seed)
    os.makedirs(d, exist_ok=True)
    ref = []

    def singles(seq, frac_dead=0.3, frac_gain=0.0):
        out = {}
        for p in range(1, len(seq) + 1):
            for a in AAS:
                if a == seq[p - 1]:
                    continue
                u = rng.random()
                out["%s%d%s" % (seq[p - 1], p, a)] = 0.0 if u < frac_dead else (1.5 if u < frac_dead + frac_gain else 1.0)
        return out

    def write(name, up, seq, rows):
        fn = name + ".csv"
        with open(os.path.join(d, fn), "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["mutant", "mutated_sequence", "DMS_score", "DMS_score_bin"])
            for m, s in rows:
                w.writerow([m, "", "%.5f" % s, 1 if s > 0.5 else 0])
        ref.append(dict(DMS_id=name, DMS_filename=fn, UniProt_ID=up, target_seq=seq, coarse_selection_type="Activity"))
    s1 = _seq(rng, 60)
    t1 = singles(s1, frac_gain=0.03)
    for k, sd in (("A", 0.05), ("B", 0.05)):
        write("P1_" + k, "P1_HUMAN", s1, [(m, v + rng.normal(0, sd)) for m, v in t1.items()])
    s2 = _seq(rng, 60)
    t2 = singles(s2, frac_gain=0.0)
    for k in ("A", "B"):
        write("P2_" + k, "P2_HUMAN", s2, [(m, v + rng.normal(0, 0.25)) for m, v in t2.items()])
    # threshold model: each substitution has a stability cost c >= 0; function = sigmoid(margin - sum c)
    s3 = _seq(rng, 80)
    keys3 = ["%s%d%s" % (s3[p - 1], p, a) for p in range(1, 81) for a in AAS if a != s3[p - 1]]
    cost = {m: rng.exponential(0.6) for m in keys3}
    fit = lambda cs: 1.0 / (1.0 + math.exp(-(3.0 - sum(cs)) * 3.0)) / (1.0 / (1.0 + math.exp(-9.0)))
    rows3 = [(m, fit([cost[m]]) + rng.normal(0, 0.05)) for m in keys3]
    for k in range(2, 7):
        for _ in range(400):
            ps = rng.choice(np.arange(1, 81), k, replace=False)
            ms = ["%s%d%s" % (s3[p - 1], p, rng.choice([a for a in AAS if a != s3[p - 1]])) for p in sorted(ps)]
            rows3.append((":".join(ms), fit([cost[m] for m in ms]) + rng.normal(0, 0.05)))
    write("P3_threshold", "P3_HUMAN", s3, rows3)
    s4 = _seq(rng, 80)
    t4 = singles(s4, frac_dead=0.3)
    rows4 = [(m, v + rng.normal(0, 0.05)) for m, v in t4.items()]
    keys4 = list(t4)
    for k in range(2, 6):
        for _ in range(400):
            idx = rng.choice(len(keys4), k, replace=False)
            ms = [keys4[i] for i in idx]
            if len({int(m[1:-1]) for m in ms}) < k:
                continue
            ms.sort(key=lambda m: int(m[1:-1]))
            v = float(np.prod([t4[m] > 0.5 for m in ms]))
            rows4.append((":".join(ms), v + rng.normal(0, 0.05)))
    write("P4_independent", "P4_HUMAN", s4, rows4)
    with open(os.path.join(d, "reference.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(ref[0]))
        w.writeheader()
        w.writerows(ref)
    return d


def selftest():
    import tempfile
    d = mkfake(tempfile.mkdtemp(prefix="dfu_"))
    global RES
    old, RES = RES, d
    try:
        out = run_b12(d, os.path.join(d, "reference.csv"), 1, tag="selftest_b12")
    finally:
        RES = old
    pf = out["b1"]["perfile"]
    assert pf["P3_threshold"]["log10_eps_k3plus"] < -0.1, pf["P3_threshold"]
    assert abs(pf["P4_independent"]["log10_eps2"]) <= 0.1, pf["P4_independent"]
    pp = out["b2"]["per_protein"]
    assert pp["P1_HUMAN"]["ben"] < 0.3, pp["P1_HUMAN"]
    assert pp["P2_HUMAN"]["ben"] > 0.7, pp["P2_HUMAN"]
    assert pp["P1_HUMAN"]["ctrl"] < 0.2 and pp["P2_HUMAN"]["ctrl"] < 0.3, pp
    # B3 identity and literal assertion
    q = lambda lit: dict(literal=lit, quote="... %s ..." % lit, locator="x", url="u", accessed="2026-10-14")
    J = dict(Axe=dict(function="beta-lactamase", f_kind="as_low_as", f=dict(q("10(77)"), value=1e-77),
                      L=dict(bracket=[100, 250])),
             Taylor=dict(function="chorismate mutase", f_kind="central", f=dict(q("5 x 1023"), value=2e-24),
                         L=dict(q("100-residue"), value=100)),
             KS=dict(function="ATP binding", f_kind="central", f=dict(q("10^11"), value=1e-11),
                     L=dict(q("80 contiguous"), value=80)))
    p = os.path.join(d, "b3_inputs.json")
    json.dump(J, open(p, "w"))
    RES = d
    try:
        o3 = b3(p, tag="selftest_b3")
    finally:
        RES = old
    assert o3["band"] == "B3-BRACKET" and o3["score"]["PC-B3"] is None, o3["band"]
    J2 = dict(J, Axe=dict(J["Axe"], L=dict(q("153-residue"), value=153)))
    json.dump(J2, open(p, "w"))
    RES = d
    try:
        o3b = b3(p, tag="selftest_b3q")
    finally:
        RES = old
    assert o3b["band"] in ("B3-PARTLY", "B3-UNITS", "B3-REAL") and o3b["score"]["PA-B3d"] is True
    bad = dict(J)
    bad["KS"] = dict(J["KS"], f=dict(literal="9e-9", quote="no number here", locator="x", url="u", accessed="d", value=9e-9))
    json.dump(bad, open(p, "w"))
    try:
        RES = d
        b3(p, tag="selftest_b3bad")
        raise SystemExit("literal assertion did not fire")
    except AssertionError:
        pass
    finally:
        RES = old
    print("selftest ok:", json.dumps(dict(P3=pf["P3_threshold"]["log10_eps_k3plus"], P4=pf["P4_independent"]["log10_eps2"],
                                          P1=pp["P1_HUMAN"], P2=pp["P2_HUMAN"], B3_bracket=o3["band"],
                                          B3_L153=[o3b["band"], o3b["centre"]["U3"]]), default=float))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "selftest"
    if cmd == "selftest":
        selftest()
    elif cmd == "mkfake":
        mkfake(sys.argv[2])
    elif cmd == "smoke":
        d = sys.argv[2]
        RES = d
        run_b12(d, os.path.join(d, "reference.csv"), int(sys.argv[3]), tag="smoke_b12")
    elif cmd == "b12":
        run_b12(sys.argv[2], sys.argv[3], int(sys.argv[4]))
    elif cmd == "b3":
        b3(sys.argv[2])
    else:
        raise SystemExit("unknown command " + cmd)

"""C1d POST HOC 2 (review fix pass) -- library type / damage, Day's documented two-period pipeline, a country-list sample,
minimum-call grid, modern-bin sensitivity.  Written AFTER the C1d main run, the first post hoc script and the three reviews;
none of it is pre-registered in the C1d sense.  Predictions below were written BEFORE this script was run.

    research/.venv/bin/python -I research/checks/c1d_posthoc2.py runall <rel> [nproc<=6]    # extract the extra groups
    research/.venv/bin/python -I research/checks/c1d_posthoc2.py analyse <rel>
Run on na-workhorse only (genotypes live there).  Per-SNP counts go to C1D_OUT (default <data>/derived_ph2); small tables to
research/checks/results/raw/c1d_<rel>_ph2.{json,txt}.  Reuses the readers, the group counting and day_events from
c1d_aadr_real.py (md5 ce613f52..., unchanged).

QUESTIONS (from the reviews; both steelman reviews asked for the same runs):
 Q1  Is the transition excess in the literal statistic damage, or real mutation / ancestry?  Library type (anno column "Library
     type": minus = no damage correction, half = damage retained at the last position, plus = fully corrected; ss.USER = USER
     treated, counted as plus) and the damage rate in the first nucleotide.  Per-individual class = the worst library present
     (any minus -> minus, else any half -> half, else any plus/USER -> plus, else unknown; moderns are unknown).  Damage-rate
     classes: lo < 0.10, mid 0.10-0.20, hi >= 0.20, na.  Per-class runs use the class-restricted ancient bins 10000+ ... 500-1000
     and the full V1 modern bin; each is compared with a MATCHED-DEPTH RANDOM CONTROL (a random subset of V1 individuals of the
     same size per bin, seed fixed), because a smaller class has fewer chromosomes per bin and that alone changes the statistic.
     Damage-aware readings: at transition SNPs (A/G, C/T) drop individuals of the stated classes (reads treated as missing);
     at transversion SNPs keep everyone.  M1 drop minus; M2 keep only plus; M3 keep plus + half; M4 drop dmg-hi; M5 keep only dmg-lo;
     each with its matched random control.  All E1 / T2 / m = 1; reported for all SNPs and autosomes; tracked = all 11 bins for the
     damage-aware readings (the classes partition the sample), 'none' for single-class runs (a class can be empty in a bin).
 Q2  Day's documented two-period pipeline (Z23046531 s2.2-2.4, s3.1-3.4): autosomes only; Neolithic 6000-8000 BP vs date = 0
     moderns; >= 100 genotyped samples in each period; allele frequency = minor-allele proportion among genotyped individuals;
     events = loci monomorphic (0 or 100%) in the modern period and polymorphic in the Neolithic.  His v62 counts: 1,143,671 SNPs
     tested, 17,806 newly 100% + 8 newly 0% = 17,814; 1,372 Neolithic / 680 modern individuals; v66: 1,143,230 SNPs, 3,469 + 1
     = 3,470, 395 / 441.  European sample variants S1 (V1 lat/long box), S2 (box without the country exclusions), S3 (keruru's
     regex), S4 (a long European-country list, Political Entity, no Russia), S5 (S4 + Russia).  S5 was chosen after an anno-only
     count showed 1,377 / 683 individuals against his 1,372 / 680; S4 alone gives 8,937 individuals in the eleven Z18525185 bins
     against 8,738 (V1: 8,808) with 168 in the 10000+ bin and 638 against 625 in the 0-500 bin, so S4 ("dayE") is also run
     through the 11-bin statistic.
 Q3  m-grid for the tracked fraction between 20 and 60 chromosomes (the main grid skipped 20-50); modern-bin sensitivity
     (diploid-only, pseudo-haploid-only, date-0 only, date 0-500 historical only, wide box, modern bin dropped).

PREDICTIONS (credences; written before the run):
 L1  Damage.  (a) The share of transitions among S21 events stays >= 90% in every library class (60%); (b) S21 per eligible allele
     in the minus class is >= 2x the matched random control and >= 2x the plus class (50%); (c) at the 0-500 BP events, the minor
     allele frequency in the older bins at transition SNPs is >= 2x higher in the minus class than the plus class (55%).  If the
     excess were real mutation/ancestry, classes would match their controls within 1.5x.
 L2  Damage-aware readings.  M2 (transitions only from fully corrected ancient libraries) cuts S21 below 1,000 (50%) but does not
     bring eligible within 2x of 22,428 (80%); the control (random subset of the same size) cuts S21 by less than M2 does (65%).
     No reading in the damage-aware set reproduces Day's profile (10000+ share < 50% AND 8000-10000 plurality) (85%).
 L3  A reading that lands near Day's 21 does so with eligible < 12,000 (80%).
 T1  Two-period.  On v62 with S5, autosomes and >= 100 genotyped individuals per period: sample sizes within 2% of 1,372 / 680 (70%);
     tested SNPs within 2% of 1,143,671 (75%); events between 15,000 and 60,000 (75%), i.e. NOT within 10% of 17,814 (75%);
     Neolithic start-MAF band shares within 3 points of his (80.9 / 18.9 / 0.22 % in 0-1 / 1-5 / 5-10) (70%); events with
     Neolithic MAF >= 10%: <= 20 (65%; his count is 1).  On v66 with S5 the event count is well above his 3,470 (90%); his v66
     sample (395 / 441) is not reproducible (his own explanation: an ID-matching problem).
 T2  The eleven-bin statistic on the S4 country-list sample gives eligible within +-25% of V1's 62,757, S21 within +-25% of 4,957 and
     the same dominance of the 10000+ and 0-500 BP bins (80%).
 T3  Minimum-call grid: on v62 the tracked fraction crosses 0.727 between m = 35 and m = 50 (the reviewer's lookup: 0.755 at 40,
     0.671 at 45) (85%); S21 stays > 3,000 and eligible > 50,000 across the whole range (90%).
 T4  Modern-bin variants: S21 never below 700 and never above 30,000; dropping the modern bin leaves S21 (bins 5000-6000 .. 500-1000)
     between 400 and 1,200 (80%).
"""
import os
import sys
import csv
import json
import re
import subprocess
import importlib.util
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("c1d", os.path.join(HERE, "c1d_aadr_real.py"))
c1d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c1d)
if "C1D_OUT" not in os.environ:
    c1d.OUT = os.path.join(c1d.DATA, "derived_ph2")

EURO = ["Albania", "Austria", "Belarus", "Belgium", "Bosnia", "Bulgaria", "Croatia", "Czechia", "Czech", "Denmark", "Estonia",
        "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kosovo", "Latvia", "Lithuania",
        "Luxembourg", "Moldova", "Montenegro", "Netherlands", "North Macedonia", "Macedonia", "Norway", "Poland", "Portugal",
        "Romania", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom", "England",
        "Scotland", "Wales", "Malta", "Cyprus", "Gibraltar", "Faroe", "Greenland"]
CLASSES = ["minus", "half", "plus", "unk"]
DCLASSES = ["lo", "mid", "hi", "na"]
RND = ["minus", "half", "plus", "plushalf", "dlo", "nothi"]
LIB_COL = "Library type"
DMG_COL = "Damage rate in first nucleotide"


def load_extra(rel, meta):
    cfg = c1d.REL[rel]
    with open(os.path.join(c1d.DATA, cfg["anno"]), encoding="latin-1", newline="") as f:
        rd = csv.reader(f, delimiter="\t")
        hdr = next(rd)
        rows = list(rd)
    li = [i for i, h in enumerate(hdr) if h.strip().startswith(LIB_COL)][0]
    di = [i for i, h in enumerate(hdr) if h.strip().startswith(DMG_COL)][0]
    pos = {}
    for i, r in enumerate(rows):
        pos.setdefault(r[0].strip(), i)
    lib, dmg = [], []
    for g in meta["ids"]:
        r = rows[pos[g]]
        t = [x.strip().lower() for x in r[li].split(",")]
        if any("minus" in x for x in t):
            lib.append("minus")
        elif any("half" in x for x in t):
            lib.append("half")
        elif any(("plus" in x or "user" in x) for x in t):
            lib.append("plus")
        else:
            lib.append("unk")
        dmg.append(c1d.fl(r[di]) if c1d.fl(r[di]) is not None else np.nan)
    return np.array(lib), np.array(dmg)


def build_groups2(meta):
    lib, dmg = load_extra(meta["_rel"], meta)
    d, lat, lon, pol = meta["date"], meta["lat"], meta["lon"], meta["pol"]
    dated = ~np.isnan(d)
    box_ = dated & ~np.isnan(lat) & ~np.isnan(lon) & (lat >= 35) & (lat <= 72) & (lon >= -25) & (lon <= 45)
    v1 = box_ & ~np.isin(pol, list(c1d.NON_EUROPE))
    euro = dated & np.isin(pol, EURO)
    names, masks = [], []

    def bins(mask, label):
        out = []
        for i, (lo, hi) in enumerate(c1d.DAY_EDGES):
            names.append("%s:%s" % (label, c1d.DAY_NAMES[i]))
            m = mask & (d >= lo) & (d < hi)
            masks.append(m)
            out.append(m)
        return out
    v1b = bins(v1, "day1")
    bins(euro, "dayE")
    for c in CLASSES:
        bins(v1 & (lib == c), "lib:" + c)
    dcl = {"lo": dmg < 0.10, "mid": (dmg >= 0.10) & (dmg < 0.20), "hi": dmg >= 0.20, "na": np.isnan(dmg)}
    for c in DCLASSES:
        bins(v1 & dcl[c], "dmg:" + c)
    rng = np.random.default_rng(20261013)
    size = {"minus": lib == "minus", "half": lib == "half", "plus": lib == "plus", "plushalf": (lib == "plus") | (lib == "half"),
            "dlo": dcl["lo"], "nothi": ~dcl["hi"]}
    for c in RND:
        for i in range(10):                              # ancient bins only (10000+ ... 500-1000)
            pool = np.where(v1b[i])[0]
            k = int((v1b[i] & size[c]).sum())
            pick = rng.choice(pool, size=min(k, len(pool)), replace=False) if k > 0 else np.array([], dtype=int)
            m = np.zeros(len(d), dtype=bool)
            m[pick] = True
            names.append("rnd:%s:%s" % (c, c1d.DAY_NAMES[i]))
            masks.append(m)
    names.append("mod:date0")
    masks.append(v1 & (d == 0))
    names.append("mod:hist")
    masks.append(v1 & (d > 0) & (d < 500))
    names.append("mod:wide")
    masks.append(box_ & (d < 500))
    sets = {"S1": v1, "S2": box_, "S3": np.array([re.search(c1d.KR_EU, p, re.I) is not None for p in pol]) & dated,
            "S4": euro, "S5": dated & (np.isin(pol, EURO) | (pol == "Russia"))}
    for k, m in sets.items():
        names.append("tp:%s:neo" % k)
        masks.append(m & (d >= 6000) & (d <= 8000))
        names.append("tp:%s:mod" % k)
        masks.append(m & (d == 0))
    return names, np.array(masks, dtype=bool)


def patch(rel):
    orig_load = c1d.load_meta

    def lm(r):
        m = orig_load(r)
        m["_rel"] = r
        return m
    c1d.load_meta = lm
    c1d.build_groups = build_groups2


def runall(rel, nproc):
    assert nproc <= 6
    procs = [subprocess.Popen([sys.executable, "-I", os.path.abspath(__file__), "extract", rel, str(k), str(nproc)]) for k in range(nproc)]
    rc = [p.wait() for p in procs]
    print("extract exit codes", rc)
    sys.exit(1 if any(rc) else 0)


# ------------------------------------------------------------------------------------------------------ analysis helpers
def bins_arrays(cnt, prefix, S):
    n = np.zeros((c1d.NB, S), dtype=np.int32)
    r = np.zeros((c1d.NB, S), dtype=np.int32)
    for i, nm in enumerate(c1d.DAY_NAMES):
        n[i], r[i] = cnt.chrom("%s:%s" % (prefix, nm))
    return n, r


def run_day(n, r, is_ts, tracked="all11", snpmask=None):
    res = c1d.day_events(n, r, "E1", "T2", 1, tracked, snpmask, ret_idx=True)
    s = c1d.summarise_day(res)
    ts_all = ts_s21 = tot_s21 = tot = 0
    for (allele, ie, dt, tr) in res["idx"]:
        keep = tr if tracked != "none" else np.ones(len(ie), dtype=bool)
        tot += int(keep.sum())
        ts_all += int((is_ts[ie] & keep).sum())
        sel = keep & (dt >= 4)
        tot_s21 += int(sel.sum())
        ts_s21 += int((is_ts[ie] & sel).sum())
    s["ts_share_events"] = ts_all / max(1, tot)
    s["ts_share_S21"] = ts_s21 / max(1, tot_s21)
    s["S21_per_eligible"] = s["S21"] / max(1, s["eligible"])
    s.pop("singleton", None)
    return s


def small(s):
    return dict(eligible=s["eligible"], tracked=s["tracked"], S21=s["S21"], S23=s["S23"], pre7000=s["pre7000_share"],
                profile=s["profile"], start_pct=[round(x, 1) for x in s["start_pct"]], ts_share_S21=round(s["ts_share_S21"], 3),
                per_eligible=s["S21_per_eligible"])


def load_alleles(rel):
    a1, a2 = [], []
    with open(os.path.join(c1d.DATA, c1d.REL[rel]["stem"] + ".snp")) as f:
        for line in f:
            p = line.split()
            if p:
                a1.append(p[4]), a2.append(p[5])
    a1, a2 = np.array(a1), np.array(a2)
    return ((a1 == "A") & (a2 == "G")) | ((a1 == "G") & (a2 == "A")) | ((a1 == "C") & (a2 == "T")) | ((a1 == "T") & (a2 == "C"))


def group_sum(cnt, names_bin, S):
    """names_bin: list of group-name prefixes to be summed per bin -> (n[11,S], r[11,S])."""
    n = np.zeros((c1d.NB, S), dtype=np.int32)
    r = np.zeros((c1d.NB, S), dtype=np.int32)
    for p in names_bin:
        a, b = bins_arrays(cnt, p, S)
        n += a
        r += b
    return n, r


def analyse(rel):
    N, D, names, sel, ic, ih = c1d.load_counts(rel)
    cnt = c1d.Counts(N, D, names)
    ids, chrom, pos = c1d.load_snp(rel)
    S = len(chrom)
    is_ts = load_alleles(rel)
    auto = chrom <= 22
    out = {"rel": rel}
    # ---------------- Q3 m-grid + modern variants on V1 and dayE
    n1, r1 = bins_arrays(cnt, "day1", S)
    nE, rE = bins_arrays(cnt, "dayE", S)
    out["mgrid"] = {}
    for tag, (n, r) in (("V1", (n1, r1)), ("dayE", (nE, rE))):
        rows = []
        for m in (1, 10, 20, 25, 30, 35, 40, 45, 50, 60):
            s = c1d.summarise_day(c1d.day_events(n, r, "E1", "T2", m, "all11", None))
            rows.append(dict(m=m, eligible=s["eligible"], tracked_frac=s["tracked_frac"], S21=s["S21"], pre7000=s["pre7000_share"]))
        out["mgrid"][tag] = rows
    # headline on dayE sample (all SNPs and autosomes, transversions)
    out["dayE"] = {}
    for lab, mask in (("all", None), ("auto", auto), ("transversions", ~is_ts), ("transversions_auto", (~is_ts) & auto),
                      ("transitions", is_ts)):
        out["dayE"][lab] = small(run_day(nE, rE, is_ts, "all11", mask))
    out["V1_split"] = {}
    for lab, mask in (("all", None), ("auto", auto), ("transversions", ~is_ts), ("transversions_auto", (~is_ts) & auto),
                      ("transversions_X", (~is_ts) & (chrom == 23)), ("transversions_Y", (~is_ts) & (chrom == 24)),
                      ("transitions_auto", is_ts & auto)):
        out["V1_split"][lab] = small(run_day(n1, r1, is_ts, "all11", mask))
    # modern-bin variants (V1)
    mods = {}
    nph, ndip, dph, ddip = cnt.raw("day1:0-500")
    mods["diploid_only"] = (2 * ndip, ddip)
    mods["pseudohaploid_only"] = (nph, dph // 2)
    for g in ("mod:date0", "mod:hist", "mod:wide"):
        mods[g] = cnt.chrom(g)
    out["modern_variants"] = {}
    for lab, (nm_, rm_) in mods.items():
        n, r = n1.copy(), r1.copy()
        n[10], r[10] = nm_, rm_
        out["modern_variants"][lab] = small(run_day(n, r, is_ts, "all11", None))
    base = run_day(n1, r1, is_ts, "all11", None)
    out["modern_variants"]["modern_bin_dropped_S21_bins4to9"] = int(sum(base["profile"][4:10]))
    # ---------------- Q1 library / damage
    out["lib"] = {}
    cls_arrays = {}
    for c in CLASSES:
        n, r = bins_arrays(cnt, "lib:" + c, S)
        cls_arrays[("lib", c)] = (n, r)
    for c in DCLASSES:
        cls_arrays[("dmg", c)] = bins_arrays(cnt, "dmg:" + c, S)
    for c in RND:
        n = np.zeros((c1d.NB, S), dtype=np.int32)
        r = np.zeros((c1d.NB, S), dtype=np.int32)
        for i in range(10):
            n[i], r[i] = cnt.chrom("rnd:%s:%s" % (c, c1d.DAY_NAMES[i]))
        cls_arrays[("rnd", c)] = (n, r)

    def with_modern(a):
        n, r = a[0].copy(), a[1].copy()
        n[10], r[10] = n1[10], r1[10]
        return n, r
    out["lib"]["per_class"] = {}
    for key in [("lib", c) for c in CLASSES] + [("dmg", c) for c in DCLASSES]:
        n, r = with_modern(cls_arrays[key])
        out["lib"]["per_class"]["%s:%s" % key] = dict(
            ancient_chrom_median=[float(np.median(n[b])) for b in range(10)],
            none=small(run_day(n, r, is_ts, "none", None)), all11=small(run_day(n, r, is_ts, "all11", None)))
    for c in RND:
        n, r = with_modern(cls_arrays[("rnd", c)])
        out["lib"]["per_class"]["rnd:%s" % c] = dict(none=small(run_day(n, r, is_ts, "none", None)),
                                                     all11=small(run_day(n, r, is_ts, "all11", None)))
    # damage-aware masking readings.  Allowed sets for ancient bins at transition SNPs.
    allsets = {k: cls_arrays[k] for k in cls_arrays}

    def allowed(sum_of):
        n = np.zeros((c1d.NB, S), dtype=np.int32)
        r = np.zeros((c1d.NB, S), dtype=np.int32)
        for key in sum_of:
            n += allsets[key][0]
            r += allsets[key][1]
        return n, r

    def minus_(a, b):
        return a[0] - b[0], a[1] - b[1]

    def masked(allowed_n, allowed_r):
        n, r = n1.copy(), r1.copy()
        for b in range(10):
            n[b] = np.where(is_ts, allowed_n[b], n1[b])
            r[b] = np.where(is_ts, allowed_r[b], r1[b])
        return n, r
    a_all = (n1, r1)
    readings = {
        "M1 drop minus": (minus_(a_all, allsets[("lib", "minus")]), minus_(a_all, allsets[("rnd", "minus")])),
        "M2 keep plus only": (allsets[("lib", "plus")], allsets[("rnd", "plus")]),
        "M3 keep plus+half": (allowed([("lib", "plus"), ("lib", "half")]), allsets[("rnd", "plushalf")]),
        "M4 drop dmg-hi": (allowed([("dmg", "lo"), ("dmg", "mid"), ("dmg", "na")]), allsets[("rnd", "nothi")]),
        "M5 keep dmg-lo only": (allsets[("dmg", "lo")], allsets[("rnd", "dlo")]),
    }
    out["lib"]["masked"] = {}
    for lab, (real, ctrl) in readings.items():
        row = {}
        for tag, a in (("class", real), ("control", ctrl)):
            n, r = masked(*a)
            row[tag] = {"all": small(run_day(n, r, is_ts, "all11", None)), "auto": small(run_day(n, r, is_ts, "all11", auto))}
        out["lib"]["masked"][lab] = row
    # attribution at the 0-500 BP events (headline V1)
    res = c1d.day_events(n1, r1, "E1", "T2", 1, "all11", None, ret_idx=True)
    attr = {}
    for sub in ("transition", "transversion"):
        accum = {k: [0, 0] for k in [("lib", c) for c in CLASSES] + [("dmg", c) for c in DCLASSES] + [("rnd", c) for c in ("minus", "plus")]}
        for (allele, ie, dt, tr) in res["idx"]:
            sel = tr & (dt == 10) & (is_ts[ie] if sub == "transition" else ~is_ts[ie])
            ii = ie[sel]
            for key in accum:
                n, r = cls_arrays[key]
                nn = n[:10, ii].sum(axis=0)
                kk = r[:10, ii].sum(axis=0)
                minor = (nn - kk) if allele == 0 else kk
                accum[key][0] += int(minor.sum())
                accum[key][1] += int(nn.sum())
        attr[sub] = {"%s:%s" % k: dict(minor_copies=v[0], chromosomes=v[1], minor_freq=v[0] / max(1, v[1])) for k, v in accum.items()}
    out["lib"]["attribution_0_500_events"] = attr
    # ---------------- Q2 two-period pipeline
    out["two_period"] = {}
    for sname in ("S1", "S2", "S3", "S4", "S5"):
        nn_, na_, dn_, dd_ = [a for a in cnt.raw("tp:%s:neo" % sname)]
        mn_, ma_, md_, mdd_ = [a for a in cnt.raw("tp:%s:mod" % sname)]
        ni_n, ni_m = nn_ + na_, mn_ + ma_
        dose_n, dose_m = dn_ + dd_, md_ + mdd_
        row = {}
        for rule, thr in (("ind100", 100), ("ind20", 20), ("ind1", 1)):
            for lab, am in (("auto", auto), ("all", np.ones(S, dtype=bool))):
                ok = am & (ni_n >= thr) & (ni_m >= thr)
                mono = ok & ((dose_m == 0) | (dose_m == 2 * ni_m))
                poly_n = (dose_n > 0) & (dose_n < 2 * ni_n)
                ev = mono & poly_n
                fn = np.where(ni_n > 0, dose_n / np.maximum(2 * ni_n, 1), 0.0)
                maf = np.minimum(fn, 1 - fn)
                fix_start = np.where(dose_m == 2 * ni_m, fn, 1 - fn)
                bands = [(0, .01), (.01, .05), (.05, .10), (.10, .20), (.20, .30), (.30, .40), (.40, .50001)]
                row["%s_%s" % (rule, lab)] = dict(
                    tested=int(ok.sum()), events=int(ev.sum()), loss_or_other=int((ev & (dose_m == 0)).sum()),
                    band_counts=[int((ev & (maf >= a) & (maf < b)).sum()) for a, b in bands],
                    maf_ge_10=int((ev & (maf >= .10)).sum()), start_fix_50_90=int((ev & (fix_start >= .5) & (fix_start < .9)).sum()),
                    start_fix_90_99=int((ev & (fix_start >= .9) & (fix_start < 1)).sum()), start_fix_lt_50=int((ev & (fix_start < .5)).sum()))
        row["max_called_ind"] = [int(ni_n.max()), int(ni_m.max())]
        out["two_period"][sname] = row
    out["group_sizes"] = {}
    meta = c1d.load_meta(rel)
    meta["_rel"] = rel
    gn, gm = build_groups2(meta)
    for nm, mk in zip(gn, gm):
        if nm.startswith(("tp:", "mod:", "dayE", "day1", "lib:", "dmg:")):
            out["group_sizes"][nm] = int(mk.sum())
    os.makedirs(c1d.RES, exist_ok=True)
    with open(os.path.join(c1d.RES, "c1d_%s_ph2.json" % rel), "w") as f:
        json.dump(out, f, indent=1, default=float)
    write_txt(rel, out)


def write_txt(rel, o):
    L = ["== C1d POST HOC 2 %s ==" % rel]
    gs = o["group_sizes"]
    L.append("sizes V1 bins: %s" % [gs["day1:%s" % b] for b in c1d.DAY_NAMES])
    L.append("sizes dayE bins: %s   (Day n %s)" % ([gs["dayE:%s" % b] for b in c1d.DAY_NAMES], c1d.DAY_N))
    for c in CLASSES + DCLASSES:
        key = ("lib:" if c in CLASSES else "dmg:") + c
        L.append("sizes %s (ancient bins): %s" % (key, [gs["%s:%s" % (key, b)] for b in c1d.DAY_NAMES]))
    L.append("tp sizes (neo / mod): " + ", ".join("%s %d/%d" % (s, gs["tp:%s:neo" % s], gs["tp:%s:mod" % s]) for s in ("S1", "S2", "S3", "S4", "S5")))

    def fmt(s):
        return "elig %7d trk %7d S21 %6d S23 %6d pre7k %.4f S21/elig %.5f tsS21 %.3f start %s prof %s" % (
            s["eligible"], s["tracked"], s["S21"], s["S23"], s["pre7000"] or 0, s["per_eligible"], s["ts_share_S21"], s["start_pct"], "/".join(map(str, s["profile"])))
    L.append("-- minimum-call grid (E1/T2 all11 all SNPs) --")
    for tag, rows in o["mgrid"].items():
        for x in rows:
            L.append("%s m=%2d elig %d tracked %.3f S21 %d pre7k %.4f" % (tag, x["m"], x["eligible"], x["tracked_frac"], x["S21"], x["pre7000"]))
    L.append("-- dayE sample --")
    for k, v in o["dayE"].items():
        L.append("dayE %-20s %s" % (k, fmt(v)))
    L.append("-- V1 split (all11) --")
    for k, v in o["V1_split"].items():
        L.append("V1 %-20s %s" % (k, fmt(v)))
    L.append("-- modern-bin variants (V1) --")
    for k, v in o["modern_variants"].items():
        L.append("%-32s %s" % (k, fmt(v) if isinstance(v, dict) else v))
    L.append("-- per library / damage class (class-restricted ancient bins; V1 modern bin) --")
    for k, v in o["lib"]["per_class"].items():
        L.append("%-12s none : %s" % (k, fmt(v["none"])))
        L.append("%-12s all11: %s" % ("", fmt(v["all11"])))
    L.append("-- damage-aware masking (transitions: allowed set only; transversions: everyone) --")
    for lab, row in o["lib"]["masked"].items():
        for tag in ("class", "control"):
            for sn in ("all", "auto"):
                L.append("%-20s %-7s %-4s %s" % (lab, tag, sn, fmt(row[tag][sn])))
    L.append("-- minor-allele frequency in older bins (bins 10000+..500-1000) at E1/T2 events dated 0-500 BP, by class --")
    for sub, d in o["lib"]["attribution_0_500_events"].items():
        for k, v in d.items():
            L.append("%-12s %-10s minor %8d / chromosomes %9d = %.4f" % (sub, k, v["minor_copies"], v["chromosomes"], v["minor_freq"]))
    L.append("-- two-period pipeline (Z23046531) --  Day v62: tested 1,143,671, events 17,814, MAF>=10%: 1, bands 80.9/18.9/0.22 %; v66: 1,143,230, 3,470, 3")
    for sname, row in o["two_period"].items():
        for k, v in row.items():
            if k == "max_called_ind":
                continue
            tot = max(1, v["events"])
            L.append("%s %-10s tested %8d events %6d (modern 0%%-type %d) bands%% %s MAF>=10%% %d start50-90 %d start90-99 %d start<50 %d" % (
                sname, k, v["tested"], v["events"], v["loss_or_other"], [round(100 * x / tot, 2) for x in v["band_counts"][:3]],
                v["maf_ge_10"], v["start_fix_50_90"], v["start_fix_90_99"], v["start_fix_lt_50"]))
    with open(os.path.join(c1d.RES, "c1d_%s_ph2.txt" % rel), "w") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    cmd = sys.argv[1]
    rel = sys.argv[2]
    patch(rel)
    if cmd == "extract":
        print("wrote", c1d.extract(rel, int(sys.argv[3]), int(sys.argv[4])))
    elif cmd == "runall":
        runall(rel, int(sys.argv[3]) if len(sys.argv) > 3 else 6)
    elif cmd == "analyse":
        analyse(rel)

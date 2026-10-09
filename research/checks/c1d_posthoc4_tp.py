"""C1d POST HOC 4 (review fix pass): which Neolithic minor-copy threshold, if any, turns the documented two-period pipeline into Day's count?

Written after c1d_posthoc2.py showed that, with the S5 sample (European country list + Russia: 1,377 Neolithic / 683 modern individuals
against his 1,372 / 680), autosomes and >= 100 genotyped individuals per period, the pipeline reproduces his tested-SNP count
(1,143,870 vs 1,143,671) and his MAF >= 10% count (2 vs 1) but gives 63,631 events against his 17,814 (3.6x).  This script scans the one
free parameter that could bridge that: the number of copies of the minor allele required in the pooled Neolithic sample (events with
k or more copies; k = 1 is the pipeline as written).  It is a CALIBRATION of an unstated parameter against his total, not a validation; the
second constraint (his band shares and his start-frequency counts) is reported alongside.  No prediction was registered; the
expectation that motivated it is that k = 3 or 4 gives about 18,000 (from the V1 11-bin counts: minor >= 3 -> 19,591).
    research/.venv/bin/python -I research/checks/c1d_posthoc4_tp.py <v62|v66>        (workhorse, uses derived_ph2 counts)
"""
import os, sys, json, importlib.util
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("p2", os.path.join(HERE, "c1d_posthoc2.py")); p2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p2)
c1d = p2.c1d
rel = sys.argv[1]
p2.patch(rel)
N, D, names, sel, ic, ih = c1d.load_counts(rel)
cnt = c1d.Counts(N, D, names)
ids, chrom, pos = c1d.load_snp(rel)
auto = chrom <= 22
L, out = [], {}
for sname in ("S1", "S4", "S5"):
    a = cnt.raw("tp:%s:neo" % sname); b = cnt.raw("tp:%s:mod" % sname)
    ni_n, ni_m = a[0] + a[1], b[0] + b[1]
    dn, dm = a[2] + a[3], b[2] + b[3]
    for lab, am in (("auto", auto), ("all", np.ones(len(chrom), bool))):
        ok = am & (ni_n >= 100) & (ni_m >= 100)
        mono = ok & ((dm == 0) | (dm == 2 * ni_m))
        fn = dn / np.maximum(2 * ni_n, 1)
        # copies of the allele that is NOT fixed in the modern period, in the Neolithic sample (individual dosage)
        minor_copies = np.where(dm == 2 * ni_m, 2 * ni_n - dn, dn)
        maf = np.minimum(fn, 1 - fn)
        for k in range(1, 9):
            ev = mono & (minor_copies >= k)
            tot = max(1, int(ev.sum()))
            out["%s_%s_k%d" % (sname, lab, k)] = dict(events=int(ev.sum()), band01=float((ev & (maf < .01)).sum() / tot), band15=float((ev & (maf >= .01) & (maf < .05)).sum() / tot),
                                                      band510=float((ev & (maf >= .05) & (maf < .10)).sum() / tot), maf_ge_10=int((ev & (maf >= .10)).sum()))
            L.append("%s %-4s k>=%d events %6d  bands 0-1 %.1f%% 1-5 %.1f%% 5-10 %.2f%%  MAF>=10%%: %d" % (sname, lab, k, ev.sum(), 100 * out["%s_%s_k%d" % (sname, lab, k)]["band01"], 100 * out["%s_%s_k%d" % (sname, lab, k)]["band15"], 100 * out["%s_%s_k%d" % (sname, lab, k)]["band510"], out["%s_%s_k%d" % (sname, lab, k)]["maf_ge_10"]))
L.append("Day v62: 17,814 events; bands 80.9 / 18.9 / 0.22 %; MAF>=10%: 1.   Day v66: 3,470 (his sample 395/441; not reproducible)")
json.dump(out, open(os.path.join(c1d.RES, "c1d_%s_ph4.json" % rel), "w"), indent=1)
open(os.path.join(c1d.RES, "c1d_%s_ph4.txt" % rel), "w").write("\n".join(L) + "\n")
print("\n".join(L))

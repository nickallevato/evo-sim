"""X1 RE-SCORE under the single verdict rule in results/R4-X1-verdict-rule.md (POST HOC, written after the three X1 reviews).

Not a simulation: a table.  "Current" verdicts are READ from the claim files (docs/research/claims/*.md, front matter, text after
'#' dropped); "Rule" verdicts are the decisions below, each with a one-line reason that cites the rule clause (R1 = materiality
threshold, S = scope, SC = self-correction, N = non-sequitur test, F = fidelity, U = unidentified/ally).  Nothing is written to
the claim files.  Output: results/R4-X1-rescore.md (table, counts, sensitivity) and raw/x1_rescore.out.

Denominator for "numeric claim" (same regex on every side): a claim file whose "## Formal statement" section contains 'derived',
'Arithmetic audit', or an explicit numeric equation.  The 45 critic/ally claims hand-listed in R4-X1-critic-arithmetic.md are
reported beside it.

Run:  research/.venv/bin/python -I research/checks/x1_rescore.py
"""
import os
import re
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
CL = os.path.join(ROOT, "docs", "research", "claims")


def read_claim(path):
    t = open(path, encoding="utf-8").read()
    fm = t.split("---")[1]
    d = {}
    for key in ("id", "side"):
        m = re.search(r"^%s:\s*(.+)$" % key, fm, flags=re.M)
        d[key] = m.group(1).split("#")[0].strip().strip('"') if m else ""
    for key in ("internal", "fidelity", "external"):
        m = re.search(r"^\s+%s:\s*(.+)$" % key, fm, flags=re.M)
        d[key] = m.group(1).split("#")[0].strip().strip('"') if m else ""
    m = re.search(r"^## Formal statement\n(.*?)(?=^## )", t, flags=re.M | re.S)
    d["numeric"] = bool(m and re.search(r"derived|Arithmetic audit|[0-9][0-9,.]* ?(x|×|/|=) ?[0-9]", m.group(1)))
    return d


claims = {}
for p in glob.glob(os.path.join(CL, "*.md")):
    if os.path.basename(p).startswith("_"):
        continue
    d = read_claim(p)
    if d["id"] and d["id"] != "X0":
        claims[d["id"]] = d

# ----------------------------------------------------------------------------------- decisions
# id: (rule_internal, rule_fidelity, reason)   ('=' means unchanged)
CRITIC = {
 "A2c": ("=", "=", "quote exact; Day's means reproduce"),
 "A2d": ("=", "=", "Day's own table has 8.5-17x faster rates"),
 "A2h": ("=", "=", "critic correct (3,840); the target slip is Day's, see new node A5h"),
 "A3d": ("pending", "unverifiable", "N2b/F: slide text absent, so the unit of the comparator cannot be tested; Day's 3.0 text is per lineage; 'misread' needs the source in hand"),
 "A3x": ("=", "=", "unit point reproduces (410/40 = 10.25; toy 1/60, 9/60)"),
 "A4c": ("=", "=", "units not stated in the quote; not determinable"),
 "A5": ("=", "n/a", "690 vs 674 is 2.4% (rounding band R1a); genome sizes are standard values (F exempt)"),
 "A5a": ("=", "=", "chain reproduces; d inside neutral supply is B5h"),
 "A5b": ("=", "=", "94,000 vs 91,600 is 2.6% (rounding); author flags linear scaling as an illustration (N4)"),
 "A5c": ("=", "unverifiable", "F: 1e-11 uncited and 8.9x below the measured rate (neutral 1.2-4.1x, not 17x, of observed); '4e-5' is a 13% speech slip -> ledger (S2)"),
 "B2e": ("=", "=", "ratio stated three ways in a draft with [CHECK] markers -> ledger (R1d); arithmetic reproduces"),
 "B3i": ("=", "=", "exact; undisputed identity (Day conceded B3g)"),
 "B4g": ("holds", "=", "N3: states an unreconciled 2x, makes no match/negligibility claim; omitted ancestral term (B4a) noted in comment"),
 "B5": ("=", "=", "exact; undisputed identity (Day accepts, B3g); applicability to the window (stationarity, B1c) is the open item"),
 "B5a": ("=", "accurate", "S2: the 35M slip (75%) is in comment 340149310, not a Statement -> ledger, no node effect; the 25 y/20 y mix (2.4-25%, inputs ambiguous) -> ledger; Day's inputs quoted correctly"),
 "B5b": ("=", "n/a", "illustration (N4) with a standard input (100 per zygote, F exempt); 'about 10 times' is an aside -> ledger"),
 "B5c": ("=", "unverifiable", "SC: 76.8 corrected in the same video -> ledger; N3: omitted ancestral term, conclusion survives (39.6M vs 35-37.8M); 98-206 source garbled (F); 205M unit moved to A3d"),
 "B5d": ("pending", "unverifiable", "N5: quote truncated at 'Literally no selection'; relayed; 30 per generation uncited"),
 "B5e": ("=", "unverifiable", "N3: Nesslig20 states 'not all differences are fixed'; conclusion survives; 75 non-standard and uncited (F)"),
 "B5f": ("=", "accurate", "N1: his stated premise is a full ancestral pipe, which removes the lag; 'under two' holds at his premises; inputs match Day's s6, s4.3"),
 "B5h": ("=", "=", "reproduces; d inherited from Day"),
 "B6": ("=", "=", "reproduces; stationarity is the premise (external)"),
 "B6b": ("=", "=", "accurate to Day 2019 text"),
 "B6c": ("holds", "=", "conditional prediction is correct; applicability to Day is G2/F1a"),
 "B7": ("=", "=", "exact; undisputed identity"),
 "B7c": ("=", "=", "exact; undisputed identity (Day conceded B3g)"),
 "C5": ("holds", "unverifiable", "R1c input looseness: not reproduced at Ne = 1e4 (5.1e-45) but both values reproduce by diffusion at 2N = 15,364 and 16,278 (-23%, -19%, within 25%); method unretrieved; N: 'finding one would be a falsification' follows for intermediate (<0.9) starts (2.6e-4 per 1e6 loci)"),
 "C5b": ("=", "=", "arithmetic only; estimator is C1d"),
 "D8": ("n/a", "unverifiable", "U: Day's blockquote, author unidentified: not scored; analogy mismatch (10^-424,764 vs 1e-65) -> ledger"),
 "D14": ("=", "=", "relay correct; Eden's inputs are his"),
 "E5": ("holds", "=", "arithmetic reproduces; artefact-vs-biology is external"),
 "F1": ("=", "=", "exact at steady state"),
 "F1b": ("=", "=", "no node effect from the unit mix (ledger)"),
 "F4": ("=", "=", "exact"),
 "G1b": ("=", "=", "reproduces"),
 "G2": ("=", "=", "reproduces; scope is G1"),
 "G2a": ("=", "=", "reproduces; analogy applies to a latency division"),
 "G2b": ("=", "=", "reproduces"),
 "G2c": ("holds", "partial", "conditional correct; applies a serial reading that Day's Appendix A (G2g) asserts but his 1-22 denies"),
 "G3": ("=", "=", "exact under McCarthy's neutral premise (22.5M; 13.1-21.8M at his 60-100 range)"),
 "G5": ("=", "=", "exact"),
 "H5": ("=", "=", "N2d: 15,800 is a rate scaling, not a cost computation (stays)"),
 "H6": ("=", "=", "reproduces"),
 "ROOT-H": ("=", "=", "position claim; numbers are A5a, H5, B5h"),
 "ROOT-K": ("=", "=", "no derivation; inherits A2e"),
}
ALLY = {"A4c", "A5a", "B5h", "D8", "D14", "G1b", "G2b", "H5", "ROOT-H", "ROOT-K"}

DAY = {  # id: (rule_internal, rule_fidelity, reason)
 "A3a": ("arithmetic-error", "misread", "R1: stated parts sum to 222M not 410M (85%), propagates to 205M; Yoo text in hand (misread)"),
 "A5e": ("holds", "unverifiable", "R1b: 9.13 vs 8 is 12%, 205M shortfall moves 12%, conclusion unchanged -> ledger"),
 "B6a": ("arithmetic-error", "n/a", "R1: 'less than half' is 0.6 and the sign of the net adjustment flips on IR's own table"),
 "C6": ("arithmetic-error", "unverifiable", "R1: abstract's 99.8% in one window vs 53.6% in own table (86%); 630 vs 21 denominator is also N2a; 1.5e8 neutral sites uncited (F)"),
 "G": ("arithmetic-error", "partial", "R1: (1.01)^1474 = 2.3e6, not 14.7 (additive/multiplicative); 107 vs hundreds of orders"),
 "G1a": ("holds", "unverifiable", "R1b, charitable reading (5.3 fixations per event): 74 vs 66 is 12% -> ledger; 5.3 basis unstated (F)"),
 "B3e": ("non-sequitur", "n/a", "N2a: own equation k = mu N/Ne gives 2.4e6, not 8.25; stays (scored on the version quoted; withdrawn later, B3g)"),
 "C2": ("non-sequitur", "unverifiable", "N2a: d not identifiable apart from s; 'd=1 discrete' fails on own formula; stays"),
 "D9a": ("non-sequitur", "n/a", "N2a: compares an algorithm's runtime with a popgen estimate; stays"),
 "C7": ("non-sequitur", "n/a", "N2d: ~0 fixations from intermediate starts does not imply no drift; stays"),
 "G3b": ("non-sequitur", "n/a", "N2d: incomplete dilemma; stays"),
 "F": ("non-sequitur", "partial", "N2d: a latency bound is not a throughput bound (own 'rate x (window - startup)'); stays"),
 "G2g": ("non-sequitur", "n/a", "N2b: premise 'sequential' contradicted by own paragraphs 22, 25; stays"),
 "Gc": ("non-sequitur", "n/a", "N2c: 230 = 157,000 x t/T, circular if fitted; stays"),
 "A2e": ("non-sequitur", "pending", "N2a: own table has mutator rates 8.5-17x above the 'ceiling'; stays"),
 "A5d": ("non-sequitur", "accurate", "N2d: 'not bottlenecked' is stronger than a sublinear positive response (a = 0.47-0.61); Tenaillon 96.5% verified"),
 "B3c": ("non-sequitur", "misread", "N2d: 0.743 is a property of the 4-cohort window; direction contradicts the companion paper; stays"),
 "F1a": ("non-sequitur", "n/a", "N2a: divides by a latency (19,807) as G_f; own text calls it throughput; stays"),
 "C2c": ("non-sequitur", "n/a", "N2a: constant s-ratio is an algebraic identity for any d; stays"),
 "C2b": ("non-sequitur", "unverifiable", "N2a: own regression gives k = 0.10 mu at d = 1; k = mu gives d < 0; data source uncited (F)"),
 "C": ("non-sequitur", "n/a", "N2a on Day's own Ne = 1e4: neutral predicts ~0 from <50% and 0.04-0.11 from 50-90%; same computation makes keruru's C5 'holds' (the conclusion points the other way)"),
 "H1": ("holds", "n/a", "SC: retraction corrects a slip in a later source; holds"),
 "B3a": ("holds", "misread", "fidelity unchanged: source text in hand (Kimura 1/2Ne vs 1/2N)"),
 "F3a": ("pending", "misread", "fidelity unchanged: Zeng 2021 text in hand"),
 "A1c": ("=", "unverifiable", "F: revised CHLCA range (250 kya-1.3 Mya) given without citation in the claim"),
 "A2f": ("=", "unverifiable", "F: blog derivation of 4,615 / 24,500 not shown"),
 "A5g": ("=", "unverifiable", "F: 'no mammalian fixation faster than 1,600' uncited"),
 "A6a": ("=", "unverifiable", "F: sweep-signature claim has no source"),
 "B4c": ("=", "unverifiable", "F: dates (250 kya-1.3 Mya) uncited"),
 "B9": ("non-sequitur", "unverifiable", "N2b (above); F: '3x excess harmful mutations' uncited"),
 "C3": ("=", "unverifiable", "F: CCR5 selection history uncited in both posts"),
 "E3": ("=", "unverifiable", "F: cited literature not retrieved"),
}
NEW_DAY = {"A5h": ("arithmetic-error", "n/a", "NEW node (proposed): Z23003785 s6.4 prints 38,400 for 3.2e9 x 1.2e-8 x 100 = 3,840 (900%); feeds 0.999^3,840 = 0.02 (true 0.68) and 0.99^3,840 = 1e-17 (true 0.021); S3: number carries an argument")}


def cur(i):
    c = claims[i]
    return "%s / %s" % (c["internal"] or "?", c["fidelity"] or "?")


rows = []
for i, (ri, rf, why) in CRITIC.items():
    c = claims[i]
    side = "ally" if i in ALLY else "critic"
    ni = c["internal"] if ri == "=" else ri
    nf = c["fidelity"] if rf == "=" else rf
    rows.append((i, side, cur(i), "%s / %s" % (ni, nf), why, c["internal"], ni, c["fidelity"], nf))
day_ids = [i for i in DAY]
seen = set()
for i in day_ids:
    if i in seen:
        continue
    seen.add(i)
    ri, rf, why = DAY[i]
    c = claims[i]
    ni = c["internal"] if ri == "=" else ri
    nf = c["fidelity"] if rf == "=" else rf
    rows.append((i, "day", cur(i), "%s / %s" % (ni, nf), why, c["internal"], ni, c["fidelity"], nf))
for i, (ri, rf, why) in NEW_DAY.items():
    rows.append((i, "day (new)", "(none)", "%s / %s" % (ri, rf), why, "", ri, "", rf))

ERR = ("arithmetic-error", "non-sequitur")

def counts(side_filter):
    sub = [r for r in rows if side_filter(r)]
    return sub

# numeric-claim denominators (regex), and error counts for ALL files on each side (not only the re-scored ones)
sides = {"day": [], "critic": [], "ally": []}
for i, c in claims.items():
    if c["side"] in sides:
        sides[c["side"]].append(c)
den = {s: sum(1 for c in v if c["numeric"]) for s, v in sides.items()}
tot = {s: len(v) for s, v in sides.items()}

def before(side):
    return sum(1 for c in sides[side] if c["internal"] in ERR), sum(1 for c in sides[side] if c["internal"] in ERR and c["numeric"])

# after: take the current verdicts, apply overrides
over = {}
for r in rows:
    over[r[0]] = r[6]
def after(side):
    n = nn = 0
    for c in sides[side]:
        v = over.get(c["id"], c["internal"])
        if v in ERR:
            n += 1
            nn += 1 if c["numeric"] else 0
    return n, nn

out = []
out.append("# R4 X1 re-score under the single verdict rule\n")
out.append("Generated by `research/checks/x1_rescore.py` from the claim files' front matter (current) and the decisions in the script (rule). Rule: `R4-X1-verdict-rule.md`. Nothing was written to the claim files.\n")
out.append("| Claim | Side | Current (internal / fidelity) | Under the rule | One-line reason |")
out.append("|---|---|---|---|---|")
for r in sorted(rows, key=lambda r: ({"critic": 0, "ally": 1, "day": 2, "day (new)": 3}[r[1]], r[0])):
    mark = "" if r[2] == r[3] else " **(changed)**"
    out.append("| %s | %s | %s | %s%s | %s |" % (r[0], r[1], r[2], r[3], mark, r[4]))

out.append("\n## Counts (internal verdict non-sequitur or arithmetic-error)\n")
out.append("Numeric = Formal-statement regex (same on every side). Totals count every claim file on the side, not only the re-scored ones; the Day nodes that were not re-scored keep their recorded verdict.\n")
out.append("| Side | Files | Numeric files | Before: errors (all files) | Before: errors in numeric files, rate | After: errors (all) | After: errors in numeric files, rate |")
out.append("|---|---|---|---|---|---|---|")
for s in ("day", "critic", "ally"):
    b, bn = before(s)
    a, an = after(s)
    nd = den[s]
    extra_files, extra_den, extra_err = 0, 0, 0
    if s == "day":
        extra_files, extra_den, extra_err = 1, 1, 1      # the proposed A5h
    out.append("| %s | %d | %d | %d | %d / %d = %.1f%% | %d | %d / %d = %.1f%% |" % (
        s + (" (+1 proposed node A5h)" if s == "day" else ""), tot[s] + extra_files, nd + extra_den, b, bn, nd, 100.0 * bn / nd,
        a + extra_err, an + extra_err, nd + extra_den, 100.0 * (an + extra_err) / (nd + extra_den)))
out.append("\nHand-listed X1 set (45 numeric critic/ally claims, R4-X1-critic-arithmetic.md): critics 35, allies 10. Errors before 0 (critics), 1 (allies: H5); after 0 and 1.\n")

# sensitivity
out.append("## Sensitivity to the 25% threshold (R1)\n")
out.append("Slips found between 5% and 25% (ledger entries, not node errors): Day A5e 12%, Day G1a 12% (charitable reading), critic Hancock '4e-5' 13% (speech). At a 10% threshold these three become arithmetic-errors: Day +2 (A5e, G1a back to arithmetic-error: 23 with A5h), critics +1 only if the caption slip is scored (A5c). At 5% nothing else moves (the next largest slips are 2.4% and 2.6%). At 33% G1a's alternative reading (88 vs 66) would stay an error either way.\n")

# fidelity counts
def fcount(side, version):
    n = 0
    for c in sides[side]:
        if not c["numeric"]:
            continue
        f = c["fidelity"] if version == "before" else next((r[8] for r in rows if r[0] == c["id"]), c["fidelity"])
        if f in ("misread", "unverifiable"):
            n += 1
    return n
out.append("## Fidelity flags (misread or unverifiable) among numeric files\n")
out.append("| Side | Before | After |")
out.append("|---|---|---|")
for s in ("day", "critic", "ally"):
    out.append("| %s | %d / %d | %d / %d |" % (s, fcount(s, "before"), den[s], fcount(s, "after"), den[s]))
txt = "\n".join(out) + "\n"
open(os.path.join(HERE, "results", "R4-X1-rescore.md"), "w").write(txt)
print(txt)

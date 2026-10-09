"""X1 RE-SCORE under the single verdict rule in results/R4-X1-verdict-rule.md (POST HOC).  REVISION 2 (rule-audit fix pass): symmetric slip test (R1/N3),
R1c limited to roughly linear outputs, charity recorded on every row, denominators from the author's QUOTED text (E1 and U-excluded nodes dropped),
Fisher exact p and sensitivity lines, errors per 10k quoted words.  Revision 1 (after the three reviews) is in git history.

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
    d["numeric_old"] = bool(m and re.search(r"derived|Arithmetic audit|[0-9][0-9,.]* ?(x|×|/|=) ?[0-9]", m.group(1)))
    st = re.search(r"^## Statement[^\n]*\n(.*?)(?=^## )", t, flags=re.M | re.S)
    quotes = "\n".join(l[2:] for l in (st.group(1).split("\n") if st else []) if l.startswith("> "))
    d["qwords"] = len(quotes.split())
    # numeric by the author's QUOTED text: an equation/operator, or a number with a magnitude/unit/percent word
    d["numeric"] = bool(re.search(r"[=×÷^]|10[⁻−^]|\d[\d,\.]*\s*(million|billion|thousand|%|×|fold|generations?|years?|My\b|Mb\b|bp\b|kya|per )|\d\s*[x*/]\s*\d", quotes))
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
 "A3d": ("holds", "unverifiable", "N2b needs the author's own text to contradict the premise and it does not (he uses the two-lineage reading in B5c too); N5 does not apply (360 is recoverable); the comparator unit is fidelity: slide absent, Day's 3.0 text is per lineage, so not misread"),
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
 "B5c": ("non-sequitur", "unverifiable", "SC: 76.8 corrected in the same video -> ledger. N3 (revised): his stated conclusion is the match, on his own event basis (76 = 152/2); adding the omitted ancestral term gives 58.6M (+46% vs 40M, +39% vs 42.07M measured; 68.7M at HCB), over 25%, so the match does not follow. On an SNV basis it would survive (39.6M vs 35-37.8M). 98-206 source garbled (F); 205M unit is A3d"),
 "B5d": ("n/a", "unverifiable", "U: unidentified geneticist relayed by the host: not scored internal (also truncated, N5); 30 per generation uncited; excluded from the denominator"),
 "B5e": ("=", "unverifiable", "N3 (revised): stated conclusion 'close to 31-62M'; with the ancestral term 58.1M (HCG, inside) or 68.2M (HCB, +10% over the top, under 25%): survives; 75 non-standard and uncited (F)"),
 "B5f": ("=", "accurate", "ATTRIBUTION: the 9.7M quote is the OP (Dumb-and-Dumber, 'illustration, not a prediction', N4); 'It needs the elapsed time ...' and 'gap under a factor of two' are justatest90, comment pcug1j0. N1: on that commenter's stated full-pipe premise the lag is absent and the conclusion follows; inputs match Day's s6, s4.3"),
 "B5h": ("=", "=", "reproduces; d inherited from Day"),
 "B6": ("=", "=", "reproduces; stationarity is the premise (external)"),
 "B6b": ("=", "=", "accurate to Day 2019 text"),
 "B6c": ("holds", "=", "conditional prediction is correct; applicability to Day is G2/F1a"),
 "B7": ("=", "=", "exact; undisputed identity"),
 "B7c": ("=", "=", "exact; undisputed identity (Day conceded B3g)"),
 "C5": ("pending", "unverifiable", "R1c (revised) does not rescue a steep output (elasticity -92 in 2N: +-25% moves it by 10^9) and the method is unretrieved, so pending; both values reproduce by diffusion at 2N = 15,364 and 16,278; the conclusion follows for starts below 0.9 (2.6e-4 per 1e6 loci)"),
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
 "A3a": ("holds", "misread", "charity (rule 3): 187 Mb read as SDRs per lineage, the pairwise total is 35M + 1,140 + 2 x 187M = 409.0M vs 410M (0.24%) and per lineage 204.5M vs 205M, so ledger (literal sum 222M, 46%/85%). Fidelity misread (187 and 410 not in Yoo) and external contested (bp vs events, A3x) are separate and unchanged"),
 "A5e": ("holds", "unverifiable", "R1b: 9.13 vs 8 is 12%, 205M shortfall moves 12%, conclusion unchanged -> ledger"),
 "B6a": ("arithmetic-error", "n/a", "R1b on Day's own table basis (not Yoo's Ne): IR's empty-pipe removal at Ne = 1e4 is 1.2M, not 2.4M, so 1.44M / 1.2M = 1.2 and 'less than half' is 0.6; the sign of 'the net adjustment still reduces' flips (+0.24M). The Ne_anc value is a contested premise (N1) and is not the basis"),
 "C6": ("non-sequitur", "unverifiable", "N3 on his own basis: 630 is for 1.5e8 genome-wide sites, 21 is among 1,233,013 panel SNPs; scaling by his own panel size gives 5.2, which flips the comparison (>25%): not an arithmetic-error but a conclusion that does not follow. Abstract's 99.8% in one window vs 53.6% (it is 99.86% over three bins: charity) -> ledger. 1.5e8 sites uncited (F)"),
 "G": ("holds", "partial", "symmetric slip test + charity: the printed '(1.01)^1474 = 14.7' is a label slip (2.34e6); ln = 14.67 and additive 14.74 give 106.5 against the printed 107 (0.5%), so the stated conclusion survives: ledger. (The earlier 'hundreds of orders' framing is withdrawn by R4 G1 and is not used)"),
 "G1a": ("holds", "unverifiable", "R1b, charitable reading (5.3 fixations per event): 74 vs 66 is 12% -> ledger; 5.3 basis unstated (F)"),
 "B3e": ("non-sequitur", "n/a", "N2a: own equation k = mu N/Ne gives 2.4e6, not 8.25; stays (scored on the version quoted; withdrawn later, B3g)"),
 "C2": ("non-sequitur", "unverifiable", "N2d: 'independently converge on d = 0.45' is stronger than the premises support: d is not identified apart from s (own sensitivity paragraph: d moves as 1/s). The 'd = 1 for discrete generations fails on own formula' basis belongs to C2a, not C2"),
 "D9a": ("non-sequitur", "n/a", "N2d: 'demonstrates the opposite' is drawn from comparing an algorithm's runtime with a different population model; his own para 7 concedes the Weasel is not a model. The exploratory 12-offspring run is external (N1) and is not the basis"),
 "C7": ("non-sequitur", "n/a", "N2d: ~0 fixations from intermediate starts does not imply no drift; stays"),
 "G3b": ("non-sequitur", "n/a", "N2d: incomplete dilemma; stays"),
 "F": ("holds", "partial", "S1: the quoted chain is consistent (k = mu once running, 4Ne startup, 1/2N says nothing about when); quote 2 states 'rate x (window - startup)'. The 'window / latency' step is F1a's and is already non-sequitur there: scoring it on F counted it twice"),
 "G2g": ("non-sequitur", "n/a", "N2b: premise 'sequential' contradicted by own paragraphs 22, 25; stays"),
 "Gc": ("non-sequitur", "n/a", "N2c: 230 = 157,000 x t/T, circular if fitted; stays"),
 "A2e": ("non-sequitur", "pending", "N2a: own table has mutator rates 8.5-17x above the 'ceiling'; stays"),
 "A5d": ("non-sequitur", "accurate", "N2d: 'not bottlenecked' is stronger than a sublinear positive response (a = 0.47-0.61); Tenaillon 96.5% verified"),
 "B3c": ("non-sequitur", "misread", "N2a: 0.743 is a property of the 4-cohort window (extending it moves k/mu across 0.60-0.87 on the paper's own growth ratio). The 'contradicts the companion paper' basis is cross-document and is not used (N2b scope); the 1/N-at-birth mechanism is external (N1)"),
 "F1a": ("non-sequitur", "n/a", "N2a: divides by a latency (19,807) as G_f; own text calls it throughput; stays"),
 "C2c": ("non-sequitur", "n/a", "N2a: constant s-ratio is an algebraic identity for any d; stays"),
 "C2b": ("non-sequitur", "unverifiable", "N2a/N2b: own regression gives k = 0.10 mu at d = 1 and k = mu at d < 0, while para 9 says k = mu 'applies with increasing accuracy the further back you go'. S1 gap: that sentence is not in the Statement; the claim file should add the para 9 quote. U: the regression was run by an unidentified 'doctor'; only Day's interpretation is scored"),
 "C": ("non-sequitur", "n/a", "N2a on Day's own Ne = 1e4: neutral predicts ~0 from <50% and 0.04-0.11 from 50-90%; same computation makes keruru's C5 'holds' (the conclusion points the other way)"),
 "H1": ("holds", "partial", "SC: retraction corrects a slip in a later source; holds. F: Bergeron cited, 40-fold accurate, the 25x comparison is Day's own and not in the paper (own table)"),
 "B1d": ("=", "unverifiable", "F: Wright's Ne formula cited, original not retrieved (own table)"),
 "B3a": ("holds", "misread", "fidelity unchanged: source text in hand (Kimura 1/2Ne vs 1/2N)"),
 "F3a": ("pending", "misread", "fidelity unchanged: Zeng 2021 text in hand"),
 "A1c": ("=", "unverifiable", "F: revised CHLCA range (250 kya-1.3 Mya) given without citation in the claim"),
 "A2f": ("=", "unverifiable", "F: blog derivation of 4,615 / 24,500 not shown"),
 "A5g": ("=", "unverifiable", "F: 'no mammalian fixation faster than 1,600' uncited"),
 "A6a": ("=", "unverifiable", "F: sweep-signature claim has no source"),
 "B4c": ("=", "unverifiable", "F: dates (250 kya-1.3 Mya) uncited"),
 "B9": ("non-sequitur", "unverifiable", "N2a in the same comment: 'extinct within centuries' vs 'about one million years apiece' per neutral fixation. The Q105 basis is dropped (premise 1 makes harmful mutations effectively neutral). F: '3x excess harmful mutations' uncited"),
 "C3": ("=", "unverifiable", "F: CCR5 selection history uncited in both posts"),
 "E3": ("=", "unverifiable", "F: cited literature not retrieved"),
}
NEW_DAY = {"A5h": ("arithmetic-error", "n/a", "NEW node (proposed): Z23003785 s6.4 prints 38,400 for 3.2e9 x 1.2e-8 x 100 = 3,840 (900%); feeds 0.999^3,840 = 0.02 (true 0.68) and 0.99^3,840 = 1e-17 (true 0.021); S3: number carries an argument")}


def cur(i):
    c = claims[i]
    return "%s / %s" % (c["internal"] or "?", c["fidelity"] or "?")



CHARITY = {  # charitable readings of an ambiguous referent that were tried (rule 3); default text below
 "A3a": "tried 187 Mb per lineage: pairwise 409.0M, per lineage 204.5M reproduce 410M/205M (0.24%) -> holds + ledger",
 "G": "tried the log scale: ln ratio 14.67 (additive 14.74), shortfall 106.5 vs printed 107 -> holds + ledger",
 "G1a": "tried 5.3 fixations per event (not hitchhikers): 74 vs 66 = 12% -> ledger",
 "A5e": "tried t_div = 5.5 My: reproduces '8' only at another input; 12% -> ledger",
 "B6a": "tried other Ne_anc: that is a contested premise (N1), not an ambiguity; 'less than half' = 0.6 stands",
 "C6": "tried 99.8% as the pre-7,000 BP share over three bins: 99.86% reproduces (abstract slip -> ledger); the 630 vs 21 denominator has no charitable reading",
 "A2e": "tried 'ceiling' = non-mutator class only (then external, N1): the paper states 'ceiling on what evolution can accomplish'; kept",
 "A5d": "tried 'not solely supply-limited' (would hold): the quoted conclusion is 'not bottlenecked'; kept",
 "B5a": "tried the 20 y reading of the time-adjusted 20M: 2.4% -> ledger",
 "B5c": "tried the haploid-correction and the 152/2 event reading (both reproduce 38.3M); tested on his own event basis",
 "B5e": "tried the haploid-events reading of 75 (stated per haploid genome)",
 "A3d": "tried the two-lineage-total comparator (the reading under which 360 follows)",
 "C5": "tried Ne 7.7-8.1k (both published values reproduce by diffusion); output is steep, so no rescue",
 "B5d": "relayed and truncated: no reading recoverable",
 "A5": "'roughly' read as a rounding band",
 "A5c": "tried 4.6e-5 for the spoken '4e-5' (caption)",
 "B5f": "tried the full-pipe premise stated by the commenter (pcug1j0); the OP's 9.7M is an illustration",
 "B5b": "tried the illustration reading (N4)",
 "A5b": "tried the illustration reading (author's own flag)",
 "B2e": "ratio three ways: tried the 8e-4 reading used in the body",
 "A3x": "tried per-lineage vs total readings of 410M/205M",
 "B6c": "tried the conditional reading", "G2c": "tried the conditional reading",
 "C2b": "tried reading 'increasing accuracy' as the regression's own d to 1 direction: contradicts the fit (k falls as d rises)",
 "F": "tried F's chain without F1a's 'window / latency' step: consistent",
}
DEFAULT_CHARITY = "attempted: no ambiguous referent"

rows = []
for i, (ri, rf, why) in CRITIC.items():
    c = claims[i]
    side = "ally" if i in ALLY else "critic"
    ni = c["internal"] if ri == "=" else ri
    nf = c["fidelity"] if rf == "=" else rf
    rows.append((i, side, cur(i), "%s / %s" % (ni, nf), why, c["internal"], ni, c["fidelity"], nf))
seen = set()
for i in DAY:
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
EXCLUDE = {"E1", "B5d", "D8"}      # no quoted critic text (E1); unidentified/relayed authors (U)

sides = {"day": [], "critic": [], "ally": []}
for i, c in claims.items():
    if c["side"] in sides:
        sides[c["side"]].append(c)
over = {r[0]: r[6] for r in rows}
new_node = {"A5h": dict(id="A5h", side="day", numeric=True, qwords=60, internal="arithmetic-error")}

def verdict(c):
    return over.get(c["id"], c["internal"])

def stats(side, scen=None):
    """errors (all files), numeric files (excluding E1/U), errors among them, quoted words of the numeric files"""
    allerr = nnum = nerr = words = 0
    for c in sides[side]:
        v = verdict(c)
        if scen and c["id"] in scen:
            v = scen[c["id"]]
        isnum = c["numeric"] and c["id"] not in EXCLUDE
        if v in ERR:
            allerr += 1
        if isnum:
            nnum += 1
            words += c["qwords"]
            if v in ERR:
                nerr += 1
    if side == "day":
        allerr += 1; nnum += 1; nerr += 1; words += 60       # proposed A5h
    return allerr, nnum, nerr, words

from math import comb
def fisher(a, n1, b, n2):
    """two-sided Fisher exact p for errors a/n1 vs b/n2 (hypergeometric, sum of tables with p <= p_obs)."""
    tot_err = a + b; N = n1 + n2
    def pr(x):
        return comb(n1, x) * comb(n2, tot_err - x) / comb(N, tot_err)
    po = pr(a)
    return sum(pr(x) for x in range(max(0, tot_err - n2), min(n1, tot_err) + 1) if pr(x) <= po * (1 + 1e-9))

# before (claim-file verdicts), same new denominator definition
def stats_before(side):
    allerr = nnum = nerr = 0
    for c in sides[side]:
        isnum = c["numeric"] and c["id"] not in EXCLUDE
        if c["internal"] in ERR:
            allerr += 1
        if isnum:
            nnum += 1
            nerr += 1 if c["internal"] in ERR else 0
    return allerr, nnum, nerr

out = []
out.append("# R4 X1 re-score under the single verdict rule (revision 2, rule-audit fix pass)\n")
out.append("Generated by `research/checks/x1_rescore.py` from the claim files' front matter (current) and the decisions in the script (rule). Rule: `R4-X1-verdict-rule.md`. Nothing was written to the claim files. Revision 1 (after the three reviews) is in git history; revision 2 applies the symmetric slip test, R1c limited to linear outputs, charity recorded on every row, and denominators from the author's quoted text.\n")
out.append("| Claim | Side | Current (internal / fidelity) | Under the rule | One-line reason | Charitable reading tried |")
out.append("|---|---|---|---|---|---|")
for r in sorted(rows, key=lambda r: ({"critic": 0, "ally": 1, "day": 2, "day (new)": 3}[r[1]], r[0])):
    mark = "" if r[2] == r[3] else " **(changed)**"
    out.append("| %s | %s | %s | %s%s | %s | %s |" % (r[0], r[1], r[2], r[3], mark, r[4], CHARITY.get(r[0], DEFAULT_CHARITY)))

out.append("\n## Counts (internal verdict non-sequitur or arithmetic-error)\n")
out.append("Numeric = the author's QUOTED Statement text contains an equation/operator or a number with a magnitude, unit or percent word (same regex on every side). Excluded from every denominator: E1 (no verbatim critic quotation) and B5d, D8 (relayed or unidentified authors, rule U). The proposed Day node A5h is added to Day's counts. Allies are a separate column.\n")
out.append("| Side | Files | Numeric files (quote-based) | Before: error verdicts (all files) | Before: errors in numeric files, rate | After: error verdicts (all files) | After: errors in numeric files, rate | After: errors per 10k quoted words (numeric files) |")
out.append("|---|---|---|---|---|---|---|---|")
res = {}
for sd in ("day", "critic", "ally"):
    b_all, b_n, b_e = stats_before(sd)
    a_all, a_n, a_e, a_w = stats(sd)
    res[sd] = (a_all, a_n, a_e, a_w, b_all, b_n, b_e)
    extra = 1 if sd == "day" else 0
    out.append("| %s | %d | %d | %d | %d / %d = %.1f%% | %d | %d / %d = %.1f%% | %.1f (%d words) |" % (
        sd + (" (+ proposed A5h)" if sd == "day" else ""), len(sides[sd]) + extra, a_n, b_all, b_e, b_n - 0, 100.0 * b_e / max(1, b_n), a_all, a_e, a_n, 100.0 * a_e / a_n, 1e4 * a_e / a_w, a_w))
d_all, d_n, d_e, d_w = res["day"][:4]
c_all, c_n, c_e, c_w = res["critic"][:4]
al_all, al_n, al_e, al_w = res["ally"][:4]
p = fisher(d_e, d_n, c_e, c_n)
out.append("\nFinal after the rule: **Day %d / %d (%.1f%%) vs critics %d / %d (%.1f%%); Fisher exact two-sided p = %.4f**. Allies %d / %d.\n" % (d_e, d_n, 100.0 * d_e / d_n, c_e, c_n, 100.0 * c_e / c_n, p, al_e, al_n))

out.append("## Sensitivity (Day vs critics, Fisher exact p)\n")
out.append("| Scenario | Day | Critics | p |")
out.append("|---|---|---|---|")
def scen_row(name, dscen=None, cscen=None, pool_allies=False, d_extra=0):
    de = stats("day", dscen)[2]; dn = stats("day", dscen)[1]
    ce = stats("critic", cscen)[2]; cn = stats("critic", cscen)[1]
    if pool_allies:
        ae = stats("ally", cscen)[2]; an = stats("ally", cscen)[1]
        ce += ae; cn += an
    out.append("| %s | %d / %d = %.1f%% | %d / %d = %.1f%% | %.4f |" % (name, de, dn, 100.0 * de / dn, ce, cn, 100.0 * ce / cn, fisher(de, dn, ce, cn)))
scen_row("base (this revision)")
scen_row("critic tie-breaks flipped to errors (C5, A3d, B5f, in addition to B5c)", cscen={"C5": "non-sequitur", "A3d": "non-sequitur", "B5f": "non-sequitur"})
scen_row("critic tie-breaks flipped AND B5c scored holds (audit's reading of N3)", cscen={"C5": "non-sequitur", "A3d": "non-sequitur", "B5f": "non-sequitur", "B5c": "holds"})
scen_row("Day weakest four dropped (C2, C2b, B9, G2g)", dscen={"C2": "holds", "C2b": "holds", "B9": "holds", "G2g": "holds"})
scen_row("both: Day weakest four dropped and critic tie-breaks flipped", dscen={"C2": "holds", "C2b": "holds", "B9": "holds", "G2g": "holds"}, cscen={"C5": "non-sequitur", "A3d": "non-sequitur", "B5f": "non-sequitur"})
scen_row("10% materiality line (A5e, G1a back to error; Hancock caption slip A5c error)", dscen={"A5e": "arithmetic-error", "G1a": "arithmetic-error"}, cscen={"A5c": "arithmetic-error"})
scen_row("critics and allies pooled", pool_allies=True)
scen_row("no charity (A3a and G back to error)", dscen={"A3a": "arithmetic-error", "G": "arithmetic-error"})
out.append("")

# corpus words (cheap): blockquote words in the harvested quote files
def qwords_file(path):
    n = 0
    for l in open(path, encoding="utf-8"):
        l = l.strip()
        if l.startswith(">"):                      # quotes-critics.md: blockquote lines
            n += len(l[1:].split())
        elif l.startswith("- quote:"):             # quotes-day.md: "- quote:" lines
            n += len(l[len("- quote:"):].split())
    return n
qd = qwords_file(os.path.join(ROOT, "docs", "research", "sources", "quotes-day.md"))
qc = qwords_file(os.path.join(ROOT, "docs", "research", "sources", "quotes-critics.md"))
out.append("## N2b exposure and corpus volume\n")
out.append("`non-sequitur` clause N2b (\"contradicted by the author's own text\") exposes authors who have written more: Day's corpus is 39 Zenodo records, 154 kept blog posts and replies, and many of his arguments are multi-step; most critic claims are one-line identities from a single comment, post or talk. The clause is unchanged. Rates per 10,000 words:\n")
out.append("| Measure | Day | Critics | Allies |")
out.append("|---|---|---|---|")
out.append("| error verdicts in numeric files / 10k words of quoted Statement text (scored text) | %.1f (%d / %d words) | %.1f (%d / %d words) | %.1f (%d / %d words) |" % (
    1e4 * d_e / d_w, d_e, d_w, 1e4 * c_e / c_w, c_e, c_w, 1e4 * al_e / al_w, al_e, al_w))
out.append("| error verdicts (all files) / 10k words of harvested quote corpus (`quotes-day.md` %d words; `quotes-critics.md` %d words, critics and allies together) | %.1f | %.1f (critics + allies %d errors) | |" % (
    qd, qc, 1e4 * d_all / qd, 1e4 * (c_all + al_all) / qc, c_all + al_all))
out.append("\nThe per-word rates adjust for quoted volume, not for the number of derivation steps per node, which was not computed. The harvested corpus is a sample chosen by the audit, not the authors' full output.\n")

def fcount(side, version):
    n = 0
    for c in sides[side]:
        if not c["numeric"] or c["id"] in EXCLUDE:
            continue
        f = c["fidelity"] if version == "before" else next((r[8] for r in rows if r[0] == c["id"]), c["fidelity"])
        if f in ("misread", "unverifiable"):
            n += 1
    return n
den = {s: stats(s)[1] for s in sides}
out.append("## Fidelity flags (misread or unverifiable) among numeric files\n")
out.append("| Side | Before | After |")
out.append("|---|---|---|")
for s in ("day", "critic", "ally"):
    out.append("| %s | %d / %d | %d / %d |" % (s, fcount(s, "before"), den[s], fcount(s, "after"), den[s]))

CAT = {
 "A": "D (formula node; inputs are scored in A1-A3)", "A4": "D (definition; the estimate is A4a)", "A4d": "D (describes the paper's choice)",
 "B1": "C (cites Kimura-Ohta, accurate; Chalub is B1e)", "B1a": "C (Kimura-Ohta first moment, accurate)", "B1b": "D (derived from 4Ne)",
 "B2d": "Q (qualitative)", "B3e": "D (own inputs, standard values)", "B3f": "D (own inputs, standard values)", "B3h": "C (Keightley cited, partial in the table)",
 "B6a": "C (Yoo and CSAC cited, verified)", "C": "C (Mallick, Mathieson cited, accurate)", "C1a": "Q", "C2c": "D (own table)", "C5a": "C (Keightley cited, verified)",
 "C7": "D (inference from C)", "D2i": "C (Schutzenberger quote, accurate)", "D9": "D (hypothetical parameters, 'Under N = ...')", "D9a": "Q (inference)",
 "F1a": "C (Good verified; Zeng is F3a)", "F2": "Q (proposed check)", "F4a": "Q", "G1": "C (Good verified)", "G2g": "Q", "G3b": "Q", "G4": "Q", "G4b": "D",
 "Gb": "D (own model)", "Gc": "D (own model)", "Ge": "Q", "H10": "C (Keightley cited, H7)", "ROOT": "Q", "ROOT-B": "Q", "ROOT-M": "Q",
}
unch = [c for c in sides["day"] if c["fidelity"] == "n/a" and c["id"] not in DAY and c["id"] not in NEW_DAY]
out.append("\n## Day files with fidelity n/a that were NOT changed (%d), by category\n" % len(unch))
out.append("D = derivation or definition from the author's own assumptions; C = cites a source whose own row is accurate or verified; Q = qualitative or position statement. Claim-level reading, not a full re-read. Human Ne about 1e4 is a contested-standard input (rule F): exempt from citation, flagged, and any node whose conclusion depends on it carries `external: contested`.\n")
for c in sorted(unch, key=lambda c: c["id"]):
    out.append("- %s: %s" % (c["id"], CAT.get(c["id"], "not categorised (no numeric input or position)")))
txt = "\n".join(out) + "\n"
open(os.path.join(HERE, "results", "R4-X1-rescore.md"), "w").write(txt)
print(txt)

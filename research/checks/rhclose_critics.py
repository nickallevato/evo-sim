"""R4-RHclose-critics: the symmetric pass (review finding RH5 of REVIEW-R4-RHclose-combined.md).  The owner's RH rule
(2026-10-11, first applied in R4-B9, then R4-RHclose) applied to critic/ally statements.  LOW-STAKES tier (one combined
review).  Local, stdlib + pyyaml, seconds.  Pre-registered: committed BEFORE the main run.
Run:  research/.venv/bin/python -I research/checks/rhclose_critics.py > research/checks/results/raw/rhclose_critics.out

OWNER'S RH RULE (2026-10-11): tag a statement `dialectic` if its literal claim is "remotely close" when mathed out under
the most charitable reading (rule C); `rhetoric` if not.  Rule C ranges over ambiguous referents and sourced inputs; it
does not replace the stated mechanism (B9 review MAJOR-1).  Rhetoric changes no verdict (RH).
LESSONS APPLIED from REVIEW-R4-B9-combined / REVIEW-R4-RHclose-combined: (1) TIGHT band: literal value x 3 (not x 10);
(2) EVERY plausible charitable reading is registered and its tag reported SEPARATELY; no single bare tag; (3) readings
are split into IN-SCOPE (a reading of the words and the object the speaker names) and EXTENDED (substitutes a different
object or widens the claim); the HEADLINE tag uses in-scope readings only, extended readings are reported with their own
tags and the owner chooses; (4) the verdict effect is stated for BOTH tag outcomes and the asymmetry is flagged;
(5) the headline is "dialectic iff ANY in-scope reading passes" (rule C = most charitable), and the fragility
(how many readings disagree, and by how much the edge case misses) is printed.

DISCLOSURE (mandatory).  NOT BLIND.  Before writing this script I (the author) had already read: the Hancock transcript
around t=00:24:58-00:27:23; Myers's three posts (paragraph lists); the ROOT-PG, G2e, G2g, B5 claim files; the MITTENS 3.0
reference list (11 entries) and a grep of Day's texts for Hancock's system names (hits for peppered moth, Drosophila,
stickleback; none for blowfly, cricket, mosquito, pesticide, scrub jay); Day's Z18470617 s3.3 peppered-moth passage.
So the counts below are predictions only in the sense of "registered before the run"; the READINGS, CRITERIA and MAPPING
are what is pre-registered.  The edge for H2 was set by the one-third rule (below) and, on my prior grep, lands exactly
ON the edge (3 of 10); this is stated, not hidden: if the denominator were 8 the tag would flip.

BAND RULE (all counts/shares).  The literal claim is the extreme (0 of N classes, or 100% of units).  "Remotely close" =
within a factor 3 of the literal value, i.e. a share >= 1/3 for a "this fully works" claim, or a count <= floor(N/3)
for a "none" claim.  Quantities (variance ratios) use the factor-3 rule directly.  The edges are the author's judgement,
fixed now.

=======================================================================================================================
CANDIDATES
 CH  RH-15, GG-34  Hancock/host, Gutsick Gibbon video, t=00:26:41 (2026-10-03):
     "The blunt fact of the matter is Vox Day's math can't do any of this."
     Local: sources/raw/critics/yt/_Vu0ZVVjwHc.transcript.txt line "[00:26:41]" (verified below).  Same caption line continues:
     "It hasn't actually run the gamut. It can't actually predict alil frequency dynamics in scrub jays, nor can it predict
     the rates of evolution in snails."  "This" = the list read out t=00:24:58-00:26:41: Drosophila, blowflies, crickets,
     mosquitoes (papers shown), peppered moths, Darwin's finches, sticklebacks, pesticide resistance (rats, nematodes), plus
     spoken scrub jays and snails: N = 10 classes.
 CM  RH-20, PZ-04  Myers, Pharyngula 2026-10-03 "Can we be done with Vox Day now?", para 1:
     "I debunked Vox Day’s stupid evolution “disproof” in one fairly short written post."
     The post is "Vox Day’s amazing ego, and Bill Dembski don't care" (2026-10-02; PZ-01; local html).  Its mathematical
     content is paras 4-5 (numbers of MITTENS 3.0, the serial-estimate objection).  "Stupid" is evaluative (not checkable);
     "fairly short" is relative (not checked).  The checkable core is "debunked the disproof".
 CF  RH-18, MF-01  Mansfield (commenter) under Examining Origins jDxFtCOGZ3A (retrieved 2026-10-07):
     "Genetic drift happens in every population and his claim otherwise is mystifying. Population size only affects which
      alleles are effectively neutral."   (clause 3 of B5; claim file B5 already tags "mystifying" rhetoric by device and
      the "Population size only..." sentence dialectic: this check tests that by the rule.)
     The Day statement replied to is "no drift above 10,000"; nearest sourced Day text: Q93 (McCarthy thread comment
     337074301, 2026-09-14): "In any population over 10,000, neutral substitution will not fixate at all."
 CX  PZ-03  Myers, same 10-02 post, para 23: "Even worse, 7 of those citations are to the LTEE, and contradict his
     conclusions, and 2 are to ape genome sequencing papers" (of 11 in MITTENS 3.0).  A count claim; tested by counting the
     MITTENS 3.0 reference list; "contradict his conclusions" is evaluative and not scored.  Included because it is
     checkable by arithmetic and was recorded "not independently checked here".
NOT CHECKABLE (why; no reading is run):
  RH-2   Hilbert "crank" (relayed; rule U; an insult with no literal claim).
  RH-13  Tipler "most rigorous mathematical challenge ... ever published" (ally, secondhand; a superlative over an
         unbounded set, no metric; ROOT-T external already `untestable`).
  RH-14  Dembski "objectively bad" (verdict word; the checkable content is the WEASEL/fitness-function claim, a separate
         dialectic node D13, scored there).
  RH-16  Hancock "Garbage in, garbage out" (idiom; the audit's ROOT-EP fidelity is `unverifiable` because no paper or input
         is named; there is nothing to math out).
  RH-17  Hancock "is just like wild to me" (incredulity; the checkable content, that Fisher/Wright/Haldane/Kingman were
         mathematically trained, is GG-41 / D2k, already dialectic and `supported`).
  RH-19  Hancock "we are not here to like save Darwin as a human" (a self-report of motive; untestable; the neutral-models-
         predate-Day content is GG-30 / B5j, dialectic).
  Evaluative words inside the three candidates ("stupid", "mystifying", "blunt fact") are not checkable by themselves;
  only the factual content around them is.

=======================================================================================================================
READINGS, CRITERIA, PREDICTIONS (fixed now)

--- CH: Hancock ---
 H1 (IN-SCOPE).  "Vox Day's math" = the MITTENS formula F_max = (t_div x d) / (g_len x G_f), the object of her whole segment
    ("If Vox Day's math is actually correct ... his math ought to explain that data and make future predictions", t=00:25:18),
    and "any of this" = predicting allele-frequency dynamics / selection strength.  Test: the variables an allele-frequency
    prediction needs, REQ = {s, N_e, p0, mu}, against the variables of the printed formula FMAX = {t_div, d, g_len, G_f}
    (name overlap; G_f is an empirical input, not a derived function of s or N_e in the printed formula).  Literal claim = overlap
    0 of 4; remotely close = overlap <= 1 (floor(4/3)).  Verified: F_max string in claims/A-mittens-formula.md title and claim
    G2h (F_max has no mu or s term).  Prediction: overlap 0 -> DIALECTIC (literally true; critic side).
 H2 (IN-SCOPE).  "Vox Day's math" = any MITTENS-type computation Day has authored (sources/raw/day/*.txt), "can't do any of this"
    = has not produced an output for any of her listed classes.  Test: for each of the N = 10 classes (regexes in code), count the
    class as `Day computation` iff some Day-authored text has a hit whose +/-600-char window contains a computation marker
    (regex: shortfall | -fold | Achievable | G_f | fails by | fixations).  Literal claim = 0 of 10; remotely close = k <= floor(10/3)
    = 3.  Prediction (prior grep, not blind): peppered moth (Z18470617 s3.3), Drosophila and stickleback (Z18452504) -> k = 3
    -> DIALECTIC AT THE EDGE (fragile: k = 4 or an N = 8 list flips it to rhetoric; reported with the margin).  The window
    rule can over-count (snail analogy) or under-count; hand adjudication of the hits is reported separately in the write-up
    and does not change the registered count.
    Sub-row H2a (arithmetic on Day's s3.3 inputs): G_f = (2/s) ln(2 N_e) with s = 0.20, N_e = 50,000; Achievable = 80 d / G_f with
    d = 0.95; deterministic logistic p(80 gen) from p0 = 1/(2 N_e) and time to 95%; reproduces Day's 115 and 0.66?  Reported,
    not used in the tag.
 H3 (EXTENDED: widens "this").  "can't do any of this" = "cannot make any testable quantitative prediction."  Test: the audit's
    record has >= 1 Day-side prediction tested and recorded (claim C, C7: ~0 completions from <50% frequency in 7,000 y; ROOT-PG
    file itself says so).  Literal claim = 0; any >= 1 contradicts.  Prediction: tag RHETORIC on this reading (but extended;
    cannot set the headline).
 HEADLINE: DIALECTIC iff H1 or H2 dialectic.  Predicted: dialectic (H1 exact; H2 at the edge).
 VERDICT MAPPING.  Current record: quote 3 rhetoric by device (ROOT-PG), unscored.  If DIALECTIC: the sentence is scored; on H1
    internal `holds` (algebraic), external `supported` for the formula alone; on H2 external `contested` for the broader
    sentence (Day applied his math to 3 of her 10 classes).  ROOT-PG's own verdicts (internal holds, external contested) do not
    change.  If RHETORIC: no change.  Asymmetry flag: the rhetoric tag RELEASES a critic statement from the H2 contradiction,
    just as it released Day in C7.

--- CM: Myers ---
 Units from docs/research/hierarchy.yaml.  ADVERSE(node) = internal in {non-sequitur, arithmetic-error} OR external ==
 contradicted OR fidelity == misread (audit verdict against Day).  ENGAGED = nodes the post's objection attacks: G2g (G2e attacks it),
 and A and G1 (Hancock's G2 attacks them; PZ-05 says Myers's criticism is "the same thing Zach Hancock pointed out").
 Share = |units ∩ ENGAGED ∩ ADVERSE| / |units|; literal claim = 1.0 ("debunked"); remotely close = share >= 1/3.
 M1 (IN-SCOPE).  "the disproof" = the whole of Day's argument: units = all load-bearing Day nodes in hierarchy.yaml (21 by my prior
    count).  Also print ROOT's own verdicts (pending/pending).  Prediction: 0/21 -> RHETORIC.
 M2 (IN-SCOPE).  "the disproof" = the MITTENS 3.0 method named in the post's own paras 2-5 (the 252,000 / 205M / 1,075,000-fold
    numbers; the divide-by-fixation-rate step): units = {A, G1}.  Prediction: A internal holds, G1 internal holds -> 0/2 -> RHETORIC.
    Check also: MITTENS 3.0 text s8.1 says its G_f already includes parallel fixation (so the post's characterisation of the
    method as sequential is contradicted by the paper it criticises); G2e fidelity `partial`.
 M3 (EXTENDED: different object).  "the disproof" = the Appendix A chain quoted in Day's 2026-10-01 blog (fixation must be
    sequential; 180 vs 205M): units = {G2g}.  The post does not quote this passage.  Prediction: G2g `non-sequitur` -> 1/1 ->
    DIALECTIC on this reading; flagged EXTENDED because it substitutes the object (Day's own text DOES contain the serial premise,
    G2g, and Day's para 25 concedes the wording; this is Myers's strongest ground).
 HEADLINE: dialectic iff M1 or M2 dialectic.  Predicted: RHETORIC (in-scope readings fail), with M3 dialectic reported.
 WORD SHARE (descriptive, not scored): words in paras 4-5 / words in the post.
 VERDICT MAPPING.  No claim node exists for PZ-04 (branch G2).  If RHETORIC: unscored (no change); core is G2e (internal holds
    against the Appendix A chain only, fidelity partial) and A/G1 (holds).  If DIALECTIC (only via M3): the sentence is scored
    `supported` in that narrow scope; ROOT unchanged.
 CX (PZ-03).  Count r = entries in the MITTENS 3.0 reference list (regex "(YYYY)." closings); LTEE-related = entry contains one of
    {Lenski, long-term, Escherichia coli, E. coli, generation experiment}; ape genome = entry contains {Chimpanzee, ape genomes}.
    Literal claim: 11 total, 7 LTEE, 2 ape.  Remotely close = each count within a factor 3.  Prediction (hand count seen earlier, not
    blind): 11 / 7 / 2 EXACT -> DIALECTIC (and supported on the count; "contradict his conclusions" not scored).

--- CF: Mansfield ---
 F1 (IN-SCOPE).  "drift happens in every population": the per-generation drift variance p(1-p)/(2N) > 0 for every finite N, and the
    SD of the drift change in 280 generations at p = 0.5 is positive for N in {1e3, 1e4, 1e5, 1e6, 1e7, 8e9}.  Literal claim: > 0.
    Prediction: positive at every N -> DIALECTIC (exact).  Magnitude reported (e.g. N = 8e9: SD ~ 1e-5).  Also Day's Q93 literal
    "will not fixate at all": neutral P_fix = 1/(2N) > 0 and the substitution rate 2 N mu (1/2N) = mu is N-independent.
 F2 (IN-SCOPE).  "Population size only affects which alleles are effectively neutral": in the Kimura diffusion P_fix = (1-e^{-2s})/(1-e^{-4Ns})
    for a new allele, 2N P_fix depends on (N, s) only through S = 2Ns up to O(s).  Test: for S in {0.1, 1, 10}, N in {1e4, 1e5, 1e6, 1e8},
    relative spread (max-min)/mean of 2N P_fix at fixed S.  Edge: <= 1e-3 (tolerance; NOT a 3x rule, because this is an exact-scaling
    check).  Prediction: <= 5e-4 -> DIALECTIC.
 F3 (IN-SCOPE, strictest).  Literal "only": N has NO other effect.  Per-generation drift variance 1/(2N) and neutral fixation time 4N
    generations both scale with N; over N = 1e4 -> 1e6 they change by x100.  Remotely close = ratio <= 3.  Prediction: 100 -> RHETORIC on
    this reading (an overstatement of "only"; Mansfield's own MF-02 uses 2N new mutations per generation, i.e. N also sets supply).
 "mystifying": a report of the speaker's state; no literal claim to math out -> RHETORIC (device: incredulity), as the claim file already says.
 HEADLINE: dialectic iff F1 or F2 dialectic (the factual clauses); "mystifying" rhetoric separately.  Predicted: DIALECTIC for the factual
    sentence pair, with F3 rhetoric reported.
 VERDICT MAPPING.  B5 (internal holds, fidelity accurate, external contested) is unchanged under either tag; the existing claim-file tags
    are confirmed.  Asymmetry flag: none for Mansfield (the dialectic reading helps the critic; there is no negative to release).

=======================================================================================================================
EACH SIDE'S PREDICTION
 Day side: critics' rhetorical closers are not "remotely close" any more than his: Hancock's own list includes classes Day's texts
   model (peppered moth, Drosophila, stickleback); Myers's one short post addresses one paragraph of method and misdescribes it
   (MITTENS 3.0 s8.1 says parallel fixation is in G_f); Mansfield's "only" is an overstatement.
 Critic side: the factual cores are right: F_max has no s or N_e term (H1); Day's own Appendix A text states the serial premise
   (M3); drift is positive at every N (F1) and N enters via 2Ns (F2); the reference-list count is exact (CX).  The tags should not
   hinge on tone.
=======================================================================================================================
"""
import glob
import hashlib
import html
import json
import math
import os
import re
import sys

import yaml

ROOT = "/home/na/projects/evo-sim"
R = ROOT + "/"
DAY = R + "sources/raw/day/"
CR = R + "sources/raw/critics/"


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def read(p):
    return open(p, encoding="utf-8", errors="replace").read()


def para_texts(path):
    t = read(path)
    m = re.search(r'<div class="entry-content"[^>]*>(.*?)<footer', t, re.S) or re.search(r"entry-content(.*)", t, re.S)
    b = m.group(1)
    ps = re.findall(r"<p[^>]*>(.*?)</p>", b, re.S)
    return [norm(html.unescape(re.sub(r"<[^>]+>", "", p))) for p in ps]


miss = 0


def verify(label, hay, quote):
    global miss
    ok = norm(quote) in norm(hay)
    if not ok:
        miss += 1
    print(f"  quote {label}: {'OK' if ok else 'MISS'}")
    return ok


print("# R4-RHclose-critics (pre-registered in its own commit; see docstring)")
print("## Source hashes (sha256)")
files = {
    "hancock_transcript": CR + "yt/_Vu0ZVVjwHc.transcript.txt",
    "pz_10_02": CR + "pz-vox-days-amazing-ego-and-bill-dembski-dont-care.html",
    "pz_10_03": CR + "pz-can-we-be-done-with-vox-day-now.html",
    "mansfield_json": CR + "yt/jDxFtCOGZ3A.info.json",
    "mittens3": DAY + "zenodo-23003785.txt",
    "z18470617": DAY + "zenodo-18470617.txt",
    "z18452504": DAY + "zenodo-18452504.txt",
    "hierarchy": R + "docs/research/hierarchy.yaml",
}
for k, p in files.items():
    print(f"  {k}: {sha(p)[:16]}...  {os.path.relpath(p, ROOT)}")

# --------------------------------------------------------------------------------------------- CH
print("\n## CH  Hancock RH-15 (GG-34)")
tr = read(files["hancock_transcript"])
verify("GG-34", tr, "The blunt fact of the matter is Vox Day's math can't do any of this.")
verify("context-continuation", tr, "It hasn't actually run the gamut. It can't actually predict alil frequency")
verify("t=00:25:18 premise", tr, "then his math ought to explain that data and in fact make future predictions better")

a_title = read(R + "docs/research/claims/A-mittens-formula.md")
FMAX_STR = "F_max = (t_div x d) / (g_len x G_f)"
print(f"  F_max string in claim A: {FMAX_STR in a_title}")
g2h = read(R + "docs/research/claims/G2h-hancock-fmax-has-no-mutation-or-selection-term.md")
print(f"  G2h text says no mu or s term: {'mu or s term' in g2h or 'no mu or s' in g2h}")
FMAX = {"t_div", "d", "g_len", "G_f"}
REQ = {"s", "N_e", "p0", "mu"}
ov = FMAX & REQ
print(f"  H1: FMAX vars {sorted(FMAX)}; REQ {sorted(REQ)}; overlap {len(ov)} of {len(REQ)}  (edge <= {len(REQ)//3})")
H1 = "dialectic" if len(ov) <= len(REQ) // 3 else "rhetoric"
print(f"  H1 tag: {H1}")

CLASSES = {
    "Drosophila": r"Drosophila",
    "blowflies": r"blowfl",
    "crickets": r"\bcricket",
    "mosquitoes": r"mosquito|Anopheles|\bAedes\b",
    "peppered moths": r"[Pp]eppered [Mm]oth",
    "Darwin's finches": r"Darwin.s finch|Geospiza|Gal[aá]pagos finch",
    "sticklebacks": r"[Ss]tickleback",
    "pesticide resistance": r"pesticide|insecticide|warfarin",
    "scrub jays": r"scrub.jay",
    "snails": r"\bsnails?\b",
}
MARK = re.compile(r"(shortfall|-fold|Achievable|G_\{?f|fails by|fixations)")
N = len(CLASSES)
k = 0
print("  H2: per class, Day-authored texts (sources/raw/day/*.txt): hits / hits with computation marker in +-600 chars")
daytexts = sorted(glob.glob(DAY + "*.txt"))
for cname, rx in CLASSES.items():
    hits = 0
    marked = 0
    where = set()
    for f in daytexts:
        t = read(f)
        for m in re.finditer(rx, t):
            hits += 1
            w = t[max(0, m.start() - 600): m.end() + 600]
            if MARK.search(w):
                marked += 1
                where.add(os.path.basename(f))
    counts = marked > 0
    k += counts
    print(f"    {cname:22s} hits {hits:3d}  marked {marked:3d}  counts={counts}  files={sorted(where)}")
edge2 = N // 3
H2 = "dialectic" if k <= edge2 else "rhetoric"
print(f"  H2: k = {k} of {N} classes with a Day computation; edge <= {edge2}; margin {edge2 - k}  -> {H2}")
print(f"  H2 fragility: with N = 8 the edge is {8//3}; k = {k} would be {'rhetoric' if k > 8//3 else 'dialectic'}")

# H2a arithmetic on Day's s3.3 inputs
z = read(files["z18470617"])
verify("Z18470617 Gf 115", z, "G_{f} = (2/0.20) × ln(100,000) = 10 × 11.5 = 115 generations")
verify("Z18470617 0.66", z, "Achievable = (80 × 0.95) / 115 = 0.66 fixations")
verify("Z18470617 predicts trajectories", z, "It predicts trajectories.")
s, Ne, gens, dd = 0.20, 50000, 80, 0.95
Gf = (2 / s) * math.log(2 * Ne)
ach = gens * dd / Gf
p0 = 1 / (2 * Ne)
def logistic(t):
    return 1 / (1 + ((1 - p0) / p0) * math.exp(-s * t))
t95 = math.log((0.95 / 0.05) * ((1 - p0) / p0)) / s
print(f"  H2a: G_f = {Gf:.2f}; achievable = {ach:.3f}; logistic p(80 gen) = {logistic(80):.4f}; t to 95% = {t95:.1f} gen "
      f"(Day: 115; 0.66; observed carbonaria ~95-98% in polluted areas by Day's text)")

# H3
c_file = read(R + "docs/research/claims/C-adna-zero-fixations.md")
c_has = 'internal: "non-sequitur"' in c_file
print(f"  H3: claim C present with internal verdict line: {c_has}")
rootpg = read(R + "docs/research/claims/ROOT-pg-hancock-popgen-track-record.md")
print(f"  H3: ROOT-PG file says Day makes a testable prediction (zero completions, C): {'zero completions, C' in rootpg}")
H3 = "rhetoric"
print(f"  H3 tag (EXTENDED): {H3} (>= 1 Day-side tested prediction exists; the literal claim is 0)")
print(f"  CH HEADLINE: {'dialectic' if 'dialectic' in (H1, H2) else 'rhetoric'}  [H1 {H1}; H2 {H2}; H3(ext) {H3}]")

# --------------------------------------------------------------------------------------------- CM
print("\n## CM  Myers RH-20 (PZ-04)")
p03 = para_texts(files["pz_10_03"])
verify("PZ-04", " ".join(p03[:2]), "I debunked Vox Day’s stupid evolution “disproof” in one fairly short written post.")
p02 = para_texts(files["pz_10_02"])
verify("PZ-03", " ".join(p02), "Even worse, 7 of those citations are to the LTEE, and contradict his conclusions, and 2 are to ape genome sequencing papers")
verify("post cites 252,000 / 205 million / 1,075,000", " ".join(p02), "divides the number of generations (252,000)")
verify("post: 191 mutations", " ".join(p02), "there has only been time to accumulate 191 mutations")
verify("post names MITTENS 3.0", " ".join(p02), "MITTENS 3.0")
print(f"  post mentions 'Appendix A': {'Appendix A' in ' '.join(p02)}")
words = [len(p.split()) for p in p02]
math_idx = [i for i, p in enumerate(p02) if re.search(r"fixation|mutation|generations|parallel|1,075,000", p)]
mw = sum(words[i] for i in math_idx)
print(f"  words: post {sum(words)}; paragraphs with the maths {[i+1 for i in math_idx]} = {mw} words = {mw/sum(words):.3f} of the post")
m3 = read(files["mittens3"])
verify("MITTENS 3.0 s8.1 parallel in G_f", m3, "The 45.4 fixations accumulated by non-mutator populations at")
print(f"  MITTENS 3.0 s8.1 heading present: {'Parallel Fixation Was Not Accounted For' in m3}")

H = yaml.safe_load(read(files["hierarchy"]))["nodes"]
by = {n["id"]: n for n in H}
def adverse(n):
    v = n.get("verdicts", {})
    return (v.get("internal") in ("non-sequitur", "arithmetic-error") or v.get("external") == "contradicted"
            or v.get("fidelity") == "misread")
def vstr(i):
    v = by[i].get("verdicts", {})
    return f"{i}: I={v.get('internal')} F={v.get('fidelity')} E={v.get('external')} load_bearing={by[i].get('load_bearing')} adverse={adverse(by[i])}"
ENGAGED = {"G2g", "A", "G1"}
lb_day = [n["id"] for n in H if n.get("side") == "day" and n.get("load_bearing")]
print(f"  load-bearing Day nodes: {len(lb_day)}  adverse among them: {[i for i in lb_day if adverse(by[i])]}")
print("  " + vstr("ROOT"))
for i in ("A", "G1", "G2g", "G2", "G2e"):
    print("  " + vstr(i))
def share(units):
    hit = [u for u in units if u in ENGAGED and adverse(by[u])]
    return hit, len(hit) / len(units)
res = {}
for lab, units, scope in (("M1", lb_day, "in-scope"), ("M2", ["A", "G1"], "in-scope"), ("M3", ["G2g"], "EXTENDED")):
    hit, sh = share(units)
    tag = "dialectic" if sh >= 1 / 3 else "rhetoric"
    res[lab] = (tag, scope)
    print(f"  {lab} ({scope}): units {len(units)}, engaged & adverse {hit}, share {sh:.3f}, edge 0.333 -> {tag}")
cm_head = "dialectic" if any(res[x][0] == "dialectic" for x in ("M1", "M2")) else "rhetoric"
print(f"  CM HEADLINE: {cm_head}  [M1 {res['M1'][0]}; M2 {res['M2'][0]}; M3(ext) {res['M3'][0]}]")

# CX: PZ-03 count
ref = m3[m3.rfind("References"):]
entries = re.split(r"(?<=\((?:19|20)\d\d\)\.)\s*", norm(ref.replace("References", "", 1)))
entries = [e for e in entries if re.search(r"\((?:19|20)\d\d\)\.$", e)]
LT = re.compile(r"Lenski|long-term|Escherichia coli|E\. coli|generation experiment")
APE = re.compile(r"Chimpanzee|ape genomes")
nl = sum(bool(LT.search(e)) for e in entries)
na = sum(bool(APE.search(e)) for e in entries)
print(f"  CX: reference entries {len(entries)}; LTEE-related {nl}; ape-genome {na}  (Myers: 11 / 7 / 2)")
for e in entries:
    print(f"      {'LTEE' if LT.search(e) else ('APE ' if APE.search(e) else 'other')} | {e[:90]}")
def close3(a, b):
    return max(a, b) / max(1, min(a, b)) <= 3
CX = "dialectic" if (close3(len(entries), 11) and close3(nl, 7) and close3(na, 2)) else "rhetoric"
exact = (len(entries), nl, na) == (11, 7, 2)
print(f"  CX tag: {CX} (exact match: {exact})")

# --------------------------------------------------------------------------------------------- CF
print("\n## CF  Mansfield RH-18 (MF-01)")
mj = json.dumps(json.load(open(files["mansfield_json"], encoding="utf-8")), ensure_ascii=False)
verify("MF-01", mj, "Genetic drift happens in every population and his claim otherwise is mystifying. Population size only affects which alleles are effectively neutral.")
q = read(R + "docs/research/sources/quotes-day.md")
verify("Q93 (quotes-day.md)", q, "In any population over 10,000, neutral substitution will not fixate at all.")
Ns = [1e3, 1e4, 1e5, 1e6, 1e7, 8e9]
allpos = True
print("  F1: N, per-gen drift var at p=.5 (=0.25/(2N)), SD of drift over 280 gen at p=.5, P_fix neutral=1/(2N), subst rate 2N*mu*(1/2N)/mu")
for n in Ns:
    v1 = 0.25 / (2 * n)
    f280 = -math.expm1(280 * math.log1p(-1 / (2 * n)))
    sd = math.sqrt(0.25 * f280)
    allpos &= v1 > 0 and sd > 0
    print(f"    N={n:9.3g}  var/gen {v1:.3e}  SD280 {sd:.3e}  P_fix {1/(2*n):.3e}  rate/mu {2*n*(1/(2*n)):.1f}")
F1 = "dialectic" if allpos else "rhetoric"
print(f"  F1 tag: {F1} (drift positive at every N: {allpos})")
worst = 0.0
print("  F2: 2N*P_fix at fixed S = 2Ns, N in {1e4,1e5,1e6,1e8}")
for S in (0.1, 1.0, 10.0):
    vals = []
    for n in (1e4, 1e5, 1e6, 1e8):
        sc = S / (2 * n)
        u = -math.expm1(-2 * sc) / -math.expm1(-4 * n * sc)
        vals.append(2 * n * u)
    spread = (max(vals) - min(vals)) / (sum(vals) / len(vals))
    worst = max(worst, spread)
    print(f"    S={S:5.1f}  2N*P_fix {[f'{v:.6f}' for v in vals]}  rel spread {spread:.2e}")
F2 = "dialectic" if worst <= 1e-3 else "rhetoric"
print(f"  F2 tag: {F2} (worst spread {worst:.2e}, edge 1e-3)")
ratio_var = (1 / (2 * 1e4)) / (1 / (2 * 1e6))
ratio_t = (4 * 1e6) / (4 * 1e4)
F3 = "dialectic" if max(ratio_var, ratio_t) <= 3 else "rhetoric"
print(f"  F3: N 1e4 -> 1e6: drift variance ratio {ratio_var:.0f}x, neutral fixation time ratio {ratio_t:.0f}x, edge 3x -> {F3}")
print("  'mystifying': report of the speaker's state; no literal claim -> rhetoric (device: incredulity)")
cf_head = "dialectic" if "dialectic" in (F1, F2) else "rhetoric"
print(f"  CF HEADLINE (factual clauses): {cf_head}  [F1 {F1}; F2 {F2}; F3 {F3}]")

print("\n## Summary of proposed tags (per reading; owner chooses the reading)")
print(f"  CH Hancock RH-15: headline {'dialectic' if 'dialectic' in (H1,H2) else 'rhetoric'}; H1 {H1}; H2 {H2} (k={k}/{N}, edge {edge2}); H3-ext {H3}")
print(f"  CM Myers RH-20:   headline {cm_head}; M1 {res['M1'][0]}; M2 {res['M2'][0]}; M3-ext {res['M3'][0]}")
print(f"  CX Myers PZ-03:   {CX} (exact: {exact})")
print(f"  CF Mansfield RH-18: factual clauses {cf_head}; F1 {F1}; F2 {F2}; F3 {F3}; 'mystifying' rhetoric")
print(f"  quote misses: {miss}")
sys.exit(0)

"""R4-Q93close: the RH6 "remotely close" test (owner rule 2026-10-11, RD) applied to Day's Q93.  ROADMAP row A6, QUEUE
item 15 follow-up.  Low-stakes tier (one combined review, REVIEW-R4-Q93close-combined.md).  Arithmetic only, stdlib
only, a few seconds; run locally.  Model checks: R4-RHclose (rhclose.py; F, f_drift and verify are imported from it,
not rewritten) and R4-RHclose-critics (whose "false at every N" line on Q93 was withdrawn in its fix pass, MINOR-3).
Run:  research/.venv/bin/python -I research/checks/q93_closeness.py > research/checks/results/raw/q93_closeness.out
      (also writes research/checks/results/raw/q93_closeness.json)
Pre-registered: committed BEFORE the main run.

DISCLOSURE (mandatory).  NOT a blind prediction.  Already known when this was written: the hand arithmetic in
  R4-RHclose-critics.md (F_drift ~ 140/N over 280 generations, crossing 1e-4 at N ~ 1.4e6); R4-B2 / R4-RHclose fill
  values (F(1.40) = 0.026, F(2.6) = 0.28, F(4.06) = 0.62, F(4.55) = 0.70); claim B2b's table (Hard Limits ceilings
  35,000 and 113,750 against the abstract's "about ten thousand", discrepancy (i)); C7 reading R3 (P <= 1e-17 for a
  fixation in 280 generations).  So this registers the READINGS, the CRITERIA, the SELECTION RULE and the MAPPING.
  Not yet computed by anyone: the exact roots x_a, x_b below and every N* that depends on them.

=====================================================================================================================
QUOTE (Q93; Vox Day, McCarthy Substack "Why Probability Zero is Wrong", comment id 337074301, 2026-09-14T18:11Z;
  local sources/raw/refresh-2026-10-09/mccarthy-comments-why/comments.json, sha256 cba6b15b...da92bc; verified below):
    "In any population over 10,000, neutral substitution will not fixate at all."
SAME COMMENT, surrounding sentences (all verified below as substrings of the comment body):
  before: "This is Kimura's standard neutral theory equation for how long it takes a neutral mutation to fixate"
          "With the standard human effective population size, Nₑ = 10,000:"
          "t̄ = 4 × 10,000 = 40,000 generations. At 25 years per generation, that's 1,000,000 years per neutral
           fixation."
          "Now, it's actually a lot worse for the neutral substitution case than that, because there is a hard limit
           to genetic drift even being able to affect a population."
  after:  "And we have actually found empirical evidence for this mathematical barrier in the ancient DNA database."
  The sentence itself names NO time window and does not say whether 10,000 is a census or an effective size.
PARENT (McCarthy, comment 337048907, 2026-09-14): window "over the course of 9 million years", N = 10,000.
SAME THREAD, one day earlier (Q96, comment 335823489, 2026-09-13): "over the last 7000 years" (claim C7).
THE "HARD LIMIT" (Hard Limits, Z22129121, 2026-08-27, 18 days before the comment; local
  sources/raw/day/zenodo-22129121.txt, verified below):
    l.52-54 "A population of 10,000 is roughly where drift permanently stops for an animal like us, the size of the
      population below which a neutral allele can still cross the whole population by chance in all the generations
      its lineage will ever have, and above which it cannot."
    l.43-46 criterion "4Nₑ < G, where G is the number of generations of the lineage concerned."
    l.14 "effective ceiling falls to about ten thousand individuals."   Census frame Nₑ = (4N − 2) / (Vₖ + 2), V_k = 5;
    human windows 2.0 My (species, G 80,000) and 6.5 My (lineage, G 260,000) at 25 y (claim B2b table).

READINGS (fixed now; every one is computed and reported, rule RD).  A reading = window x meaning of "10,000" x
  meaning of "will not fixate at all".
 Windows (generations; g = 25 y, the comment's own figure):
  W1  none: unbounded time / steady state.  Quantity: the substitution flux k/mu (= 1 at every N at equilibrium; the
      "any fixation in the population per generation" reading, k = mu per site per generation, independent of N).
  W2  280 (7,000 y): the ancient-DNA window; anchor: the sentence after Q93 plus Q96 in the same thread.
  W3  40,000 (1,000,000 y): the same comment's 4N_e figure taken as a fixed window.
  W3s 4N_e(N), scaling with the population (x = 4 at every N).
  W4  80,000 (HL species window, 2.0 My).     W5  260,000 (HL lineage, 6.5 My).
  W6  360,000 (McCarthy's 9 My in the parent comment).
 Meaning of "population over 10,000":
  Ne      effective size (the comment's own "Nₑ = 10,000"; Wright-Fisher, N = N_e).
  wright  census N with N_e = (4N - 2)/(V_k + 2), V_k = 5 (the Hard Limits frame; N_e = 5,714 at N = 10,000).
  frank   census N with N_e = 0.1 N (parameters.yaml Ne_over_N, Frankham 1995, verified: false) -> REPORTED, NOT USED.
 Meaning of "will not fixate at all" (criterion; x = T / N_e):
  Ca  strict: exact fill F(x) <= 1e-4, F = P(tau <= T | fixation) for a new neutral mutation entering at the window
      start (Kimura 1955 diffusion series, rhclose.F; Day's own k(T) = mu F(T), Q147).  1e-4 is the "not at all" band
      R4-RHclose fixed for the same phrase in Q96.  F is also the flux k(T)/mu of an initially empty pipe.
  Cb  loose: F(x) <= 0.10 (the "never fills / nearly empty" band of R4-RHclose Part 2).
  Cc  Day's own stated criterion (HL l.43-46): fixation "completes" iff 4 N_e < T; "will not" iff N_e > T/4.
  Cd  the C7 standard named in the queue entry: F_drift = 1 - (1 - 1/(2 N_e))^T <= 1e-4 (W2 only; over the longer
      windows F_drift -> 1 and Cd adds nothing).
 "Fixation of a given new mutation" reading, unbounded time (R1b): P_fix = 1/(2N).  REPORTED, NOT USED for the tag:
      1/(2N) has no cutoff (scale-free), so any N* it yields is just 1/(2 x band) (5,000 for band 1e-4), an artefact
      of the band, and Day's own parent-thread arithmetic uses P_fix = 1/20,000 > 0 at N = 10,000.  Also reported:
      the absolute probability F(x)/(2N) for each window at N = 10,000.
 REPORTED, NOT USED (identity): W3 x Ne x Cc gives N* = 40,000/4 = 10,000 exactly, because the window was defined as
      4 x 10,000; it is circular and cannot show closeness.  W3s x Cc is the same identity at every N.
 USED GRID (25 rows): W1 Ne Ca; W2 Ne {Ca, Cb, Cc, Cd} and wright {Ca, Cd}; W3 Ne {Ca, Cb}; W3s Ne Ca;
      W4, W5: {Ne, wright} x {Ca, Cb, Cc}; W6 Ne {Ca, Cb, Cc}.
 Other reported rows: frank for W2 Cd and W5 Cc; W2 at 20 y per generation (350 generations) Ne Cd.

QUANTITIES PER ROW.
  boundary value: the criterion's quantity at N = 10,000 exactly (F; or T/(4 N_e) for Cc, the window in units of the
    mean fixation time, "completes" iff > 1; or F_drift), and its ratio to the literal band (1e-4, 0.10, 1, 1e-4).
  N*: the true cutoff under the reading, the smallest N above which the criterion holds for every larger N (all
    quantities are monotone decreasing in N for a fixed window).  Ca: N_e* = T / x_a with F(x_a) = 1e-4; Cb:
    N_e* = T / x_b with F(x_b) = 0.10; Cc: N_e* = T/4; Cd: root of F_drift = 1e-4.  wright: N* = (7 N_e* + 2)/4;
    frank: N* = 10 N_e*.  W1 and W3s: N* is infinite (the quantity does not fall with N).
  miss = N* / 10,000.
CLOSENESS CRITERION AND 3x BAND (RH6: "3x of the literal value", fixed in advance; the literal value in Q93 is the
  cutoff 10,000; the 10x band is a disclosed sensitivity only, as in R4-RHclose):
    TRUE     N* <= 10,000   (the universal "any population over 10,000" holds under the reading)
    CLOSE    10,000 < N* <= 30,000
    OFF-10x  30,000 < N* <= 100,000   (outside the band; inside the 10x sensitivity)
    OFF      N* > 100,000 or infinite
  RH tag per reading: `dialectic` if TRUE or CLOSE, `rhetoric` otherwise (the R4-RHclose rule, one tag per reading).
  Second column, reported, not used for the tag: is the cutoff LOCATED at 10,000 (1/3 <= miss <= 3) or SLACK
    (miss < 1/3: the statement is true but would be equally true of far smaller populations, so "over 10,000" does no
    work) or HIGH (miss > 3).
SELECTION OF THE VERDICT-FIELD READING (rule RD: the reading under which the quoted statement is most defensible,
  not the one with the best verdict for the speaker; fixed now): among the 25 used rows, the best status (TRUE >
  CLOSE > OFF-10x > OFF); ties broken by textual anchor in the order W5, W4 (the "hard limit" is HL, whose l.52-54 is
  almost the same sentence), W2 (the sentence after Q93), W3 (same comment), W6 (parent), W3s, W1; then Ne before
  wright except in W4/W5 (wright first: HL's frame); then Cc, Ca, Cb, Cd.  All rows stay in the Readings table.

PREDICTIONS.
  Day side: under the most defensible reading the statement is remotely close (TRUE or CLOSE).
  Critic side: under every reading it is off by more than the band at N just above 10,000 (no used row is TRUE or
    CLOSE); in particular neutral fixation proceeds at rate mu at any N (W1), and Day's own table puts the human
    ceiling at 35,000-114,000, not 10,000.
  Audit (numeric):
   P1 x_a in [0.60, 0.95]; x_b in [1.80, 2.00].
   P2 W2 Ne Cd (the C7 standard): boundary F_drift 0.0139 (139x the band); N* = 1.40e6 +/- 1% (140x) -> OFF.
      wright: N* about 2.45e6 -> OFF.
   P3 W2 fixation rows (Ne Ca, Cb, Cc; wright Ca): boundary F < 1e-12; N* < 1,000 -> TRUE and SLACK (> 10x).
   P4 HL's own frame (wright, Cc): N* = 35,000 (W4, 3.5x, OFF-10x) and 113,750 (W5, 11.4x, OFF); at census 10,000 the
      window is 3.5 (W4) and 11.4 (W5) mean fixation times, exact F >= 0.80 (W4) and >= 0.999 (W5).
   P5 W4 Ne Cc: N* = 20,000 -> CLOSE.  W5 Ne Cc 65,000 and W6 Ne Cc 90,000 -> OFF-10x.  Every W4-W6 row under Ca has
      N* >= 80,000.
   P6 W3 Ne: boundary F(4) = 0.63 +/- 0.01; Cb N* in [20,000, 22,300] -> CLOSE; Ca N* in [42,000, 67,000] -> OFF-10x.
   P7 W1 and W3s: N* infinite -> OFF (k/mu = 1 and F = 0.63 at every N).
   P8 Selection: a W2 fixation row (Ne, Cc), status TRUE, SLACK.  Overall: READING-DEPENDENT; the Day-side prediction
      holds on the selected reading and the critic-side prediction fails as a universal, but holds on W1, on the C7
      standard and on HL's own census frame over HL's own windows.
  Self-tests (not predictions): F(1.40) = 0.0255, F(4.55) = 0.697 (R4-B2); exact Wright-Fisher chain, 2N = 100, one
      initial copy: P(fixed by t)/P(fixed ever) within 0.05 of the diffusion F(t/N) at t = 100, 200, 400.

OUTCOME -> RH TAG AND VERDICT (proposals only; fixed now).  Q93 is in no claim's Statement block (quotes-day.md files
  it under branch B2, claims B2 / B2b; B5's R4 paragraph only records the withdrawn line), so under rule S it scores no
  claim verdict directly and NO claim verdict moves under any outcome:
  (a) selected row TRUE or CLOSE and at least one used row OFF  -> Q93 RH tag `reading-dependent` (RD), value
      `dialectic` on the selected reading; a Readings table for Q93 is proposed for B2b (the claim that holds the
      "about ten thousand" ceiling).  If the selected reading is TRUE only as SLACK in W2, it is the C7-R3 situation:
      true as a count, and the step from it to a "hard limit" / "mathematical barrier" at 10,000 is the non-sequitur
      already scored at claim C (X1 row C); nothing new is scored.
  (b) every used row TRUE or CLOSE -> `dialectic`, close; no verdict change.
  (c) no used row TRUE or CLOSE -> `rhetoric`; not literal-fact-checked; device, audience, function, core (B2 / B2b)
      and a better-rhetoric answer go to ledgers/slips.md at integration; no verdict change.
  In every case B5's note ("queued as a Day-side closeness re-test") is closed by reference to this check, and B2b's
  existing discrepancy (i) (abstract "about ten thousand" vs table 35,000-114,000) is unchanged.
CAVEATS: diffusion limit, constant size, neutral, empty pipe at the window start (pre-window fill only raises F);
  the bands 1e-4 and 0.10 are judgements inherited from R4-RHclose; RH tags classify statements, they do not make
  them true.
"""
import hashlib
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)  # python -I drops the script directory; rhclose.py is this repo's own committed code
from rhclose import F, f_drift, verify  # noqa: E402  (reused helpers, R4-RHclose)

ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
COMM = os.path.join(ROOT, "sources", "raw", "refresh-2026-10-09", "mccarthy-comments-why", "comments.json")
HL = os.path.join(ROOT, "sources", "raw", "day", "zenodo-22129121.txt")
OUT_JSON = os.path.join(HERE, "results", "raw", "q93_closeness.json")

Q93 = "In any population over 10,000, neutral substitution will not fixate at all."
DAY_Q = [Q93,
         "This is Kimura's standard neutral theory equation for how long it takes a neutral mutation to fixate",
         "With the standard human effective population size, Nₑ = 10,000:",
         "t̄ = 4 × 10,000 = 40,000 generations. At 25 years per generation, that's 1,000,000 years per neutral "
         "fixation.",
         "Now, it's actually a lot worse for the neutral substitution case than that, because there is a hard limit "
         "to genetic drift even being able to affect a population. " + Q93 + " And we have actually found empirical "
         "evidence for this mathematical barrier in the ancient DNA database."]
PARENT_Q = ["over the course of 9 million years", "in a population of 10,000 humans"]
Q96_Q = ["genetic drift isn't happening at all over the last 7000 years"]
HL_Q = ["A population of 10,000 is roughly where drift permanently stops for an animal like us, the size of the "
        "population below which a neutral allele can still cross the whole population by chance in all the "
        "generations its lineage will ever have, and above which it cannot.",
        "4Nₑ < G, where G is the number of generations of the lineage concerned.",
        "effective ceiling falls to about ten thousand individuals.",
        "Nₑ = (4N − 2) / (Vₖ + 2)"]

CUT = 10000.0
BAND_A, BAND_B, BAND_D = 1e-4, 0.10, 1e-4
VK = 5.0
WINDOWS = {"W2": 280.0, "W3": 40000.0, "W4": 80000.0, "W5": 260000.0, "W6": 360000.0}
WLABEL = {"W1": "unbounded / steady state", "W2": "280 gen (7,000 y, aDNA)", "W3": "40,000 gen (comment's 4N_e)",
          "W3s": "4N_e(N), scaling", "W4": "80,000 gen (HL 2 My)", "W5": "260,000 gen (HL 6.5 My)",
          "W6": "360,000 gen (McCarthy 9 My)"}
ANCHOR = ["W5", "W4", "W2", "W3", "W6", "W3s", "W1"]
CRIT_ORDER = ["Cc", "Ca", "Cb", "Cd"]
STATUS_RANK = {"TRUE": 0, "CLOSE": 1, "OFF-10x": 2, "OFF": 3}


def find_comment(node, cid):
    if isinstance(node, dict):
        if node.get("id") == cid and "body" in node:
            return node
        for v in node.values():
            if isinstance(v, (dict, list)):
                r = find_comment(v, cid)
                if r:
                    return r
    elif isinstance(node, list):
        for v in node:
            r = find_comment(v, cid)
            if r:
                return r
    return None


def verify_comment(data, cid, quotes):
    c = find_comment(data, cid)
    if c is None:
        print(f"  MISS comment {cid} not found")
        return len(quotes)
    body = " ".join((c.get("body") or "").split())
    print(f"comment {cid}: {c.get('name')} {c.get('date')} edited_at={c.get('edited_at')}")
    miss = 0
    for q in quotes:
        ok = q in body
        miss += not ok
        print(f"  {'OK  ' if ok else 'MISS'} {q}")
    return miss


def root_x(target):
    lo, hi = 0.05, 40.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if F(mid) > target:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def root_ne_drift(T, band):
    lo, hi = 1.0, 1e13
    for _ in range(300):
        mid = math.sqrt(lo * hi)
        if f_drift([(T, mid)]) > band:
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo * hi)


def ne_of(meaning, n):
    return {"Ne": n, "wright": (4 * n - 2) / (VK + 2), "frank": 0.1 * n}[meaning]


def n_of(meaning, ne):
    return {"Ne": ne, "wright": ((VK + 2) * ne + 2) / 4, "frank": 10 * ne}[meaning]


def status(nstar):
    if nstar <= CUT:
        return "TRUE"
    if nstar <= 3 * CUT:
        return "CLOSE"
    if nstar <= 10 * CUT:
        return "OFF-10x"
    return "OFF"


def located(nstar):
    m = nstar / CUT
    return "SLACK" if m < 1 / 3 else ("HIGH" if m > 3 else "LOCATED")


def row(w, meaning, crit, xa, xb, used=True, T=None, note=""):
    T = WINDOWS.get(w) if T is None else T
    ne_b = ne_of(meaning, CUT)
    if w == "W1":
        val, band, nes = 1.0, BAND_A, math.inf          # k/mu at equilibrium, every N
    elif w == "W3s":
        val, band, nes = F(4.0), BAND_A, math.inf       # x = 4 at every N
    elif crit == "Ca":
        val, band, nes = F(T / ne_b), BAND_A, T / xa
    elif crit == "Cb":
        val, band, nes = F(T / ne_b), BAND_B, T / xb
    elif crit == "Cc":
        val, band, nes = T / (4 * ne_b), 1.0, T / 4
    else:
        val, band, nes = f_drift([(T, ne_b)]), BAND_D, root_ne_drift(T, BAND_D)
    nstar = n_of(meaning, nes) if math.isfinite(nes) else math.inf
    st = status(nstar)
    return {"window": w, "T": T, "meaning": meaning, "criterion": crit, "used": used, "Ne_at_10000": ne_b,
            "boundary_value": val, "band": band, "value_over_band": val / band, "Ne_star": nes, "N_star": nstar,
            "miss": nstar / CUT, "status": st, "located": located(nstar),
            "tag": "dialectic" if st in ("TRUE", "CLOSE") else "rhetoric", "note": note}


def fmt(v):
    if not math.isfinite(v):
        return "inf"
    if v == 0 or abs(v) < 1e-12:
        return "< 1e-12"
    return f"{v:,.0f}" if abs(v) >= 1000 else f"{v:.3g}"


def print_rows(rows):
    print("| window | '10,000' as | criterion | N_e at N=10,000 | value at N=10,000 | value / band | N* (true cutoff) "
          "| miss N*/10,000 | status (3x band) | cutoff | RH tag |\n|---|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        print(f"| {r['window']} {WLABEL[r['window']] if r['T'] in (None, WINDOWS.get(r['window'])) else str(int(r['T'])) + ' gen'}"
              f" | {r['meaning']} | {r['criterion']} | {fmt(r['Ne_at_10000'])} | {fmt(r['boundary_value'])} | "
              f"{fmt(r['value_over_band'])} | {fmt(r['N_star'])} | {fmt(r['miss'])} | {r['status']} | {r['located']} | "
              f"{r['tag']} |{' ' + r['note'] if r['note'] else ''}")


def wf_selftest(two_n=100, times=(100, 200, 400)):
    """Exact Wright-Fisher chain, one initial copy: P(fixed by t) / (1/two_n) against the diffusion F(t / N)."""
    logc = [math.lgamma(two_n + 1) - math.lgamma(j + 1) - math.lgamma(two_n - j + 1) for j in range(two_n + 1)]
    P = []
    for i in range(two_n + 1):
        p = i / two_n
        if i == 0:
            P.append([1.0] + [0.0] * two_n)
        elif i == two_n:
            P.append([0.0] * two_n + [1.0])
        else:
            lp, lq = math.log(p), math.log(1 - p)
            P.append([math.exp(logc[j] + j * lp + (two_n - j) * lq) for j in range(two_n + 1)])
    v = [0.0] * (two_n + 1)
    v[1] = 1.0
    out = {}
    for t in range(1, max(times) + 1):
        nv = [0.0] * (two_n + 1)
        for i, vi in enumerate(v):
            if vi > 0:
                Pi = P[i]
                for j in range(two_n + 1):
                    nv[j] += vi * Pi[j]
        v = nv
        if t in times:
            out[t] = v[two_n] * two_n
    return out


def main():
    b = open(COMM, "rb").read()
    print(f"{os.path.relpath(COMM, ROOT)} sha256 {hashlib.sha256(b).hexdigest()}")
    data = json.loads(b.decode("utf-8"))
    miss = verify_comment(data, 337074301, DAY_Q)
    miss += verify_comment(data, 337048907, PARENT_Q)
    miss += verify_comment(data, 335823489, Q96_Q)
    miss += verify(HL, HL_Q)
    print(f"quote misses: {miss}")

    print(f"\nself-test vs R4-B2: F(1.40) = {F(1.40):.4f}, F(4.55) = {F(4.55):.3f}")
    wf = wf_selftest()
    worst = max(abs(wf[t] - F(t / 50.0)) for t in wf)
    print("self-test exact Wright-Fisher (2N = 100, one copy) vs diffusion: " +
          ", ".join(f"t={t}: exact {wf[t]:.3f} / F({t / 50.0:g}) {F(t / 50.0):.3f}" for t in sorted(wf)) +
          f"; worst |diff| {worst:.3f} -> {'OK' if worst <= 0.05 else 'FAIL'}")

    xa, xb = root_x(BAND_A), root_x(BAND_B)
    print(f"\nroots: x_a (F = 1e-4) = {xa:.4f}; x_b (F = 0.10) = {xb:.4f}")

    used = [row("W1", "Ne", "Ca", xa, xb)]
    used += [row("W2", "Ne", c, xa, xb) for c in ("Ca", "Cb", "Cc", "Cd")]
    used += [row("W2", "wright", c, xa, xb) for c in ("Ca", "Cd")]
    used += [row("W3", "Ne", c, xa, xb) for c in ("Ca", "Cb")]
    used += [row("W3s", "Ne", "Ca", xa, xb)]
    for w in ("W4", "W5"):
        used += [row(w, m, c, xa, xb) for m in ("wright", "Ne") for c in ("Cc", "Ca", "Cb")]
    used += [row("W6", "Ne", c, xa, xb) for c in ("Cc", "Ca", "Cb")]
    assert len(used) == 25
    print("\n## Used grid (25 rows)")
    print_rows(used)

    other = [row("W3", "Ne", "Cc", xa, xb, used=False, note="identity: window defined as 4 x 10,000 (circular)"),
             row("W2", "frank", "Cd", xa, xb, used=False, note="N_e/N = 0.1 unverified"),
             row("W5", "frank", "Cc", xa, xb, used=False, note="N_e/N = 0.1 unverified"),
             row("W2", "Ne", "Cd", xa, xb, used=False, T=350.0, note="20 y per generation")]
    print("\n## Reported, not used")
    print_rows(other)
    print(f"R1b per-mutation, unbounded: P_fix = 1/(2N) = {1 / (2 * CUT):.3g} at N = 10,000; scale-free, no cutoff; "
          f"band 1e-4 would give N* = {1 / (2 * BAND_A):,.0f} (an artefact of the band)")
    print("absolute P(a given new mutation is fixed within the window) at N = N_e = 10,000: " +
          ", ".join(f"{w} {fmt(F(T / CUT) / (2 * CUT))}" for w, T in WINDOWS.items()))
    print("W1 steady state: k/mu = 1 at every N (substitutions per site per generation = mu, independent of N)")

    def key(r):
        m_order = (["wright", "Ne"] if r["window"] in ("W4", "W5") else ["Ne", "wright"]).index(r["meaning"])
        return (STATUS_RANK[r["status"]], ANCHOR.index(r["window"]), m_order, CRIT_ORDER.index(r["criterion"]))
    sel = min(used, key=key)
    counts = {s: sum(r["status"] == s for r in used) for s in STATUS_RANK}
    print(f"\nstatus counts over the 25 used rows: {counts}")
    print(f"selected (RD) reading: {sel['window']} / {sel['meaning']} / {sel['criterion']}: status {sel['status']}, "
          f"cutoff {sel['located']}, N* = {fmt(sel['N_star'])}, tag {sel['tag']}")
    n_close = counts["TRUE"] + counts["CLOSE"]
    outcome = "b" if n_close == 25 else ("c" if n_close == 0 else "a")
    print(f"outcome branch: ({outcome}) -> " + {"a": "reading-dependent, value dialectic on the selected reading",
                                               "b": "dialectic", "c": "rhetoric"}[outcome])

    g = {(r["window"], r["meaning"], r["criterion"]): r for r in used}

    def ok(c):
        return "HOLDS" if c else "MISS"
    w2fix = [g[("W2", "Ne", "Ca")], g[("W2", "Ne", "Cb")], g[("W2", "Ne", "Cc")], g[("W2", "wright", "Ca")]]
    preds = {
        "P1": 0.60 <= xa <= 0.95 and 1.80 <= xb <= 2.00,
        "P2": (abs(g[("W2", "Ne", "Cd")]["boundary_value"] - 0.0139) < 0.0002
               and abs(g[("W2", "Ne", "Cd")]["N_star"] / 1.40e6 - 1) <= 0.01 and g[("W2", "Ne", "Cd")]["status"] == "OFF"
               and abs(g[("W2", "wright", "Cd")]["N_star"] / 2.45e6 - 1) <= 0.01
               and g[("W2", "wright", "Cd")]["status"] == "OFF"),
        "P3": all(r["status"] == "TRUE" and r["located"] == "SLACK" and r["N_star"] < 1000 for r in w2fix)
              and all(r["boundary_value"] < 1e-12 for r in w2fix if r["criterion"] in ("Ca", "Cb")),
        "P4": (abs(g[("W4", "wright", "Cc")]["N_star"] - 35000) < 1 and g[("W4", "wright", "Cc")]["status"] == "OFF-10x"
               and abs(g[("W5", "wright", "Cc")]["N_star"] - 113750) < 1 and g[("W5", "wright", "Cc")]["status"] == "OFF"
               and g[("W4", "wright", "Ca")]["boundary_value"] >= 0.80
               and g[("W5", "wright", "Ca")]["boundary_value"] >= 0.999),
        "P5": (g[("W4", "Ne", "Cc")]["N_star"] == 20000 and g[("W4", "Ne", "Cc")]["status"] == "CLOSE"
               and g[("W5", "Ne", "Cc")]["status"] == "OFF-10x" and g[("W6", "Ne", "Cc")]["status"] == "OFF-10x"
               and all(r["N_star"] >= 80000 for r in used
                       if r["window"] in ("W4", "W5", "W6") and r["criterion"] == "Ca")),
        "P6": (abs(g[("W3", "Ne", "Ca")]["boundary_value"] - 0.63) <= 0.01
               and 20000 <= g[("W3", "Ne", "Cb")]["N_star"] <= 22300 and g[("W3", "Ne", "Cb")]["status"] == "CLOSE"
               and 42000 <= g[("W3", "Ne", "Ca")]["N_star"] <= 67000 and g[("W3", "Ne", "Ca")]["status"] == "OFF-10x"),
        "P7": g[("W1", "Ne", "Ca")]["status"] == "OFF" and g[("W3s", "Ne", "Ca")]["status"] == "OFF",
        "P8": (sel["window"], sel["meaning"], sel["criterion"], sel["status"], sel["located"])
              == ("W2", "Ne", "Cc", "TRUE", "SLACK") and outcome == "a",
    }
    print()
    for k, v in preds.items():
        print(f"{k}: {ok(v)}")
    print(f"Day-side prediction (most defensible reading TRUE or CLOSE): {ok(sel['status'] in ('TRUE', 'CLOSE'))}")
    print(f"Critic-side prediction (no used row TRUE or CLOSE): {ok(n_close == 0)} "
          f"({n_close} of 25 rows TRUE or CLOSE)")

    def clean(r):
        return {k: (None if isinstance(v, float) and not math.isfinite(v) else v) for k, v in r.items()}
    with open(OUT_JSON, "w") as fh:
        json.dump({"quote": Q93, "quote_misses": miss, "x_a": xa, "x_b": xb, "wf_selftest": wf,
                   "used": [clean(r) for r in used], "reported_not_used": [clean(r) for r in other],
                   "status_counts": counts, "selected": clean(sel), "outcome_branch": outcome,
                   "predictions": preds}, fh, indent=1, sort_keys=True)
    print(f"\nwrote {os.path.relpath(OUT_JSON, ROOT)}")


if __name__ == "__main__":
    main()

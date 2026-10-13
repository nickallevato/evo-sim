"""R4 L2: a sourced hardness h for humans (two routes, mapping fixed before any number is read).

Brief: research/checks/briefs/L2-analyst.md (lead Big Sim, 2026-10-13).  Queue item L2 (QUEUE.md, later queue).
Targets: H, H5, H8 (all `load_bearing: true`); h is the parameter their external verdicts turn on (R4-HF).
Tier: load-bearing, three reviews (correctness, steelman-day, steelman-critic).

PRE-REGISTRATION.  Everything in this docstring was written before any source for L2 was fetched or read.
Disclosure (for PREREG-STATUS; label expected: criterion-only at best).  No L2 source text, table or figure was
opened in this session.  The analyst saw only the retrieval notes of refresh-2026-10-11b-lit s6 (Stearns 2010:
paywalled, abstract only; Byars 2010: abstract only, "No decomposition in the abstract") and the R4-HF results
the thresholds come from.  The analyst does carry general background knowledge of human historical demography
from training (qualitatively: pre-transition child mortality was high; studies of English "homeostasis" exist;
Crow's index has been computed for many populations).  No number from memory is used anywhere; every input
must come from a fetched text with a verbatim quote (AGENTS rule 2, rule 8).  The audit's own predictions below
are informed by that background and are labelled as such.

WHY THIS CHECK, AND WHERE IT IS DECIDED
  R4-HF measured the in-model sustainable rate as a function of the hardness h of the mix model
  (hf_followups.py: J = R N juveniles, density-independent survival w^h, then a cull to K weighted by w^(1-h);
  no density compensation of fecundity).  h is "the share of the log-load expressed as density-independent
  survival at a fixed R" (R4-HF review item Critic-4), and Critic-4 also said: it "has no field estimator".
  This check does not pretend otherwise.  It fixes, before any number is read, (1) which published statistics
  are admitted, (2) the formula that turns each into an interval for h, with the assumption that formula
  needs, (3) the search that decides which sources are admitted, so nobody chooses them after seeing values,
  and (4) what every possible interval licenses.  Step (2) is where the result is decided; it is therefore
  stated with an alternative reading in each direction (RD-style readings table), and the verdict value moves
  only under the primary reading of BOTH routes.

THRESHOLDS (from R4-HF, verbatim figures asserted against results/R4-HF.md by `smoke` and `main`)
  In-model sustainable rate as a multiple of the H8 hard cap at the same R (K = 1000, s = 0.01):
    h = 1: 1 (validation); h = 0.3: "about 1.3-1.7x"; h = 0.1: "about 2.6-3.5x at R = 1.111" (marginal, 4 of 8)
    and about 3.5x at R = 2; h = 0: no cap in-model (the population cannot go extinct; Day-1 clause).
  As a multiple of Term 3 (H8, ln R / (2 ln 2K)): h = 0.3: "0.83x and 1.05x"; h = 0.1: "1.9x and 2.8x" (the
  strict tie reading at R = 1.111 gives 0.0094 / 0.00693 = 1.36x, still above R1's 1.25).
  Untested: 0 < h < 0.1 and 0.3 < h < 1.  Every statement for those ranges assumes the rate is monotone in h,
  which both tested brackets support (h = 0 > 0.1 > 0.3 > 1) but no run shows inside them.
  Cut points for the bands: C1 = 0.1 and C2 = 0.3 (the two tested interior values).

TARGET QUOTES (verbatim; RH tag dialectic for all)
  H (Day, Z18168236 Abstract, Q47): "Haldane calculated that mammals could fix no more than approximately one
    beneficial substitution per 300 generations, based on the reproductive cost each substitution imposes on a
    population."
  H8 (Day, Z19984826 s3.3): "Selection cannot operate without reproductive differential, and the differential
    available to any individual is bounded by what the organism can physically achieve."  s3.3.1: "None of them
    raises smax above order unity, and the reason is the same in all three cases."
  H5 (Hossjer, MITTENS PDF p.3, s2): "Vox Day convincingly argues that if many nucleotides at which fixation
    takes place have a selective advantage (so that natural selection acts on all these mutations) there is a
    reproductive cost of having many fixations going on in parallel."
  Critic side (GG-26, Hancock, t=02:07:18): "the cost of selection is only applicable for hard selection models
    where selection's effect is independent of the genotypes".
  Literature, Day-favourable (Nunney 2003, Introduction, quotes-literature.md): "As a result, soft selection
    inevitably reduces or eliminates the cost of substitution. However, given directional environmental
    change, it is likely that hard selection will dominate the adaptive process".
  Neither side states a value of h for humans.  The predictions below are the audit's reading of what each
  side's position needs, not quotes; they score no author statement (rule S).

ROUTES, STATISTICS AND THE MAPPING TO h  (G = generation length, bracketed G in [25, 30] years)
  Route (a), density dependence of survival and fertility in historical populations.
    Primary reading A1 (parallel channels): genotype-dependent losses fall on the density-independent (DI) and
    density-dependent (DD) channels in proportion to each channel's share of the regulation.  Then h equals
    the per-generation persistence of a deviation in log population size, beta_gen (beta_gen = 1: nothing is
    compensated, deaths add, hard; beta_gen = 0: a deviation is fully compensated within one generation, the
    slots refill, soft).  This is the generation-scale analogue of the model's two channels (density-
    independent survival vs a cull to K).  Admitted statistics and formulas:
      beta_gen       per-generation AR coefficient of log N        h = beta_gen
      beta_annual    annual AR coefficient phi of log N            h = phi^G
      kappa_annual   annual return rate kappa                      h = exp(-kappa G)
      halflife_years half-life T of a deviation from equilibrium   h = 2^(-G/T)
      vital_elasticities_N   crude annual birth and death rates b, d with their elasticities eps_b, eps_d with
                     respect to population size: kappa = d eps_d - b eps_b (linearised d lnN/dt = b(N) - d(N)),
                     then as kappa_annual
      vital_elasticities_wage  the same with eps_v = eps_v,wage x eps_wage,N, both reported in the SAME source
      cohort_elasticity  elasticity eps of a per-capita episode rate (survival to adulthood, marriage,
                     reproduction) with respect to cohort size; the other episodes are unknown, so under A1
                     h in [0, 1 + eps]
    Alternative readings (reported beside, never governing): A-up, the DD channel is genotype-blind and only DI
    losses select, so h in [A1 lo, 1]; A-down, soft selection can act locally (family, village, slots) without
    showing in aggregate regulation, so h in [0, A1 hi].  Together they say aggregate series alone identify
    nothing; A1 is the assumption under which they identify h, and it is stated wherever the result is used.
  Route (b), viability vs fertility decomposition of lifetime reproductive success (Stearns 2010, Byars 2010
  designs; Crow's index; Arnold-Wade episodes).
    Primary reading M-b1: selection through pre-reproductive survival is hard (deaths add); selection through
    fertility among survivors is soft (competition for mates, marriages, niches).  h = viability share.
      crow           Crow's index: I_m (= (1 - P_s)/P_s if only P_s is given), I_f, P_s
                     h = I_m / (I_m + I_f / P_s)   (Crow's I_tot = I_m + I_f / P_s; exact by construction)
      episodes       opportunities for selection by episode: I_surv, I_mate, I_fpm (fertility per mate)
                     h = I_surv / (I_surv + I_mate + I_fpm)   (share of the episode sum; covariance terms
                     dropped, stated)
      differentials  selection differentials or gradients on one trait by episode, S_v and S_f
                     h = |S_v| / (|S_v| + |S_f|)
    Alternative readings: M-b2 (up), only mate/marriage competition is soft and fecundity per mate is hard:
    episodes h = (I_surv + I_fpm) / sum; crow and differentials h in [M-b1 lo, 1] (the split is not reported);
    M-b0 (down), pre-reproductive deaths are themselves partly compensated (replacement births, positive check
    is density-dependent): h in [0, M-b1 hi].
  Interval from one record: the source's reported 95% interval (or +-1.96 SE) mapped through the formula at its
  ends (every formula is monotone in each input; the corner that gives the extreme is used, and G at the end
  of its bracket that widens the interval).  No interval reported: the point value, flagged "no uncertainty".
  Values outside [0, 1] are clipped and flagged (a domain violation of the reading, reported, not dropped).

ELIGIBILITY (asserted per record; a record failing any item is reported and excluded from the governing interval)
  E1 human population.  E2 pre-transition: natural fertility and pre-modern mortality (birth cohorts before the
  demographic transition of that population, or a contemporary natural-fertility subsistence population); the
  H branch concerns the lineage over 252,000 generations, nearly all of them pre-transition.  Post-transition
  records are reported in a sensitivity line ("modern included").  E3 route (b): the decomposition includes
  mortality from birth (or from infancy) to reproductive age; a sample conditioned on survival to adulthood
  cannot give the viability share (expected for Byars 2010, Framingham women; PA-2).  E3 route (a): the
  regressor is population size, density or cohort size (wages only via vital_elasticities_wage).  E4 a verbatim
  quote id, a locator, the sha256 of the fetched file and an access date.  E5 the number is printed in the text
  or a table, not read off a figure.  If a source gives several model specifications, the one its authors call
  main or preferred; if none is designated, all of them (union).  All eligible records enter; none is chosen.

SEARCH PROTOCOL (run once by the run task; no snowballing; additions after it are post hoc and labelled)
  S1 fixed candidates (citations from memory where marked, to be verified at fetch; OA only, rule 6; paywalled
  or blocked items go to the owner's list in the refresh file, the gap is carried, never filled from memory):
    route (b): Stearns2010 and Byars2010 (bib-literature.md rows exist); Courtiol et al. 2012 PNAS, "Natural and
      sexual selection in a monogamous historical human population" (memory); Courtiol et al. 2013 Curr Biol,
      rural Gambia, demographic transition and selection (memory); Crow 1958 Hum Biol, "Some possibilities for
      measuring selection intensities in man" (memory).
    route (a): Lee 1987 Demography, "Population dynamics of humans and other animals" (memory); Lee and Anderson
      2002, "Malthus in state space" (memory); Galloway 1988 Popul Stud, annual variations in fertility,
      nuptiality, mortality and prices in pre-industrial Europe (memory).
  S2 fixed queries, Europe PMC REST and OpenAlex, first 200 results each by the service's relevance order,
  screened on title and abstract against E1-E3; a screening log (record id, decision, reason) is committed as
  results/raw/l2_screening.tsv and its path is required in the inputs file:
    Q-b1 "opportunity for selection" AND human
    Q-b2 ("episodes of selection" OR "selection episodes") AND (human OR preindustrial)
    Q-b3 "Crow's index" OR "index of opportunity for selection"
    Q-a1 (homeostasis OR "density dependence" OR "density-dependent") AND (preindustrial OR "pre-industrial" OR
         historical) AND (fertility OR mortality) AND human
    Q-a2 ("preventive check" OR "positive check") AND (Malthus OR Malthusian)
  Fetches go to a new directory sources/raw/l2-<date>/ (rule 4: read or grep, never execute; sha256 and access
  date in bib-literature.md / quotes-literature.md rows, demographic sources only).

AGGREGATION (fixed; no averaging, no picking)
  Route interval = hull of the primary-reading intervals of all eligible records of that route (heterogeneity
  between populations is part of the answer).  A route with no eligible record is "unsourced".
  Governing interval = hull of the two route intervals.  If the two route intervals do not overlap, the flag
  DISJOINT is raised and the disagreement is reported as a result in its own right (both intervals, side by
  side); the band is still read off the hull, so a disagreement can never license a move that either route
  alone would not.  The intersection is reported, never used.

BANDS (exhaustive: every outcome lands in exactly one; lo <= hi always)
  U0          neither route sourced.
  U1-XY       exactly one route sourced; XY as below on that route's interval.
  B-XY        both routes sourced; XY on the governing interval:
    LL  hi < 0.1             LM  lo < 0.1 <= hi < 0.3       LH  lo < 0.1 and hi >= 0.3
    MM  0.1 <= lo, hi < 0.3  MH  0.1 <= lo < 0.3 <= hi      HH  lo >= 0.3
  13 outcomes.  Reachability (one line per side, ST-05): B-HH needs every eligible pre-transition record to give
  beta_gen lower end >= 0.3 (a deviation less than 70% compensated per generation: half-life >= 0.58 G
  at G = 30, i.e. >= about 17 years) AND a viability share lower end >= 0.3 (pre-reproductive mortality carries >= 30% of
  Crow's index).  B-LL needs every eligible record to give beta_gen upper end < 0.1 (more than 90% compensated
  per generation: half-life < 0.30 G at G = 25, i.e.
  < about 7.5 years) AND a viability share upper end < 0.1.  `smoke` builds
  synthetic inputs that land in all 13 and asserts it.

VERDICT MOVES (rule R4-X1; materiality R1 = 25%; external vocabulary supported | contested | contradicted)
  H external (contested): NO band moves the value.  The cap's level is set by R (unsourced, V17) as much as by
    h: at h >= 0.3 the cap is within about 1.3-1.7x of the hard cap at the same R, which is near 1/300 only at
    R = 1.111 and about 11x it at R = 2.  Bands move the h-scope text only:
      B-HH  "for human selection as sourced (h >= 0.3, primary mapping of both routes) the soft-selection escape
             does not apply; the contest rests on R, D and K"
      B-LL  "for human selection as sourced (h < 0.1) the in-model limit is at least about 2.6x the hard cap
             (tested at 0.1; untested below)"; queue an HF mix run at the sourced interval (it could move H)
      B-LM, B-MM, B-MH, B-LH  the placement sentence (interval, in-model multiples at its ends), no move
      U1-XY "one route only (<route>); the other is unsourced"; the same placement sentence; no move
      U0    "h stays a declared bracket; no human source admits a mapping"; the sourcing gap is recorded
  H5 external (contested): as H, for the same reason (Hossjer's cost step is uncomputed and R is unsourced).
    Recorded with every band: in-model a reproductive cost of parallel fixations exists at every h > 0; it is
    uncapped only at h = 0.
  H8 external (contested; Term 3 as a rate bound across mechanisms):
      B-HH  contested -> SUPPORTED: Term 3 holds in-model within R1 at the sourced h (0.83-1.05x at h = 0.3,
            hard cap at h = 1; monotone between, assumed); purely relative fitness and truncation that holds
            N = K are not descriptions of human selection with h >= 0.3.  Condition carried: primary readings
            A1 and M-b1.
      B-LL  contested -> CONTRADICTED: Term 3 is exceeded by more than R1 at the sourced h (>= 1.9x at h = 0.1
            on the registered estimator, >= 1.36x on the strict tie reading at R = 1.111; higher toward h = 0,
            monotone, assumed).  Day-1 clause carried.  Same condition.
      every other outcome: no value move; placement sentence.
  H1 (supported) is not moved by any band (it concerns the scope of Term 3, not h).
  If an integrator or reviewer finds another arm that independently holds H8 contested, the B-HH/B-LL move is
  withheld and recorded as "h-arm closed, value held by <arm>"; that is the only exception.

PREDICTIONS (scored by `main`; each can fail)
  PD (Day side, reading of Q47 "the reproductive cost each substitution imposes on a population" and Nunney's
     "hard selection will dominate"): outcome B-HH.  Weak form PD-w: governing lo >= 0.1 (B-MM, B-MH, B-HH; both routes sourced, else
     unscorable).
  PC (critic side, reading of GG-26): outcome B-LL.  Weak form PC-w: governing hi < 0.3 (B-LL, B-LM, B-MM; both routes sourced, else
     unscorable).
  Audit (informed by the background disclosed above):
    PA-1 both routes yield at least one eligible record.
    PA-2 Byars2010 yields no eligible route (b) record (E3: sample conditioned on survival to adulthood), or is
         not retrievable.
    PA-3 route (b) interval lies inside [0.2, 0.8] and its lower end is in [0.2, 0.5].
    PA-4 route (a) interval straddles 0.3 (lo < 0.3 <= hi).
    PA-5 the outcome is one of B-LH, B-MH, U1-LH, U1-MH, U1-HH, U0 (a specific prediction; all six move no
         verdict value).
  These are scored as hit / miss / unscorable (unscorable when the route they need is unsourced).

SENSITIVITY (reported, never governing): every pair of readings (A1, A-up, A-down) x (M-b1, M-b2, M-b0) with its
  band; modern records included; G fixed at 25 and at 30; the intersection of the routes where they overlap.

RESOURCES AND COMMANDS
  Pure arithmetic on a small JSON (standard library only): one process, < 50 MB, < 1 s, so it runs on the
  workstation under the AGENTS "trivial check" allowance; no worker pool exists to smoke.  The heavy part is
  the source search and extraction (network and reading), done by the run task.
  Smoke (synthetic inputs, every band, every mapping; prints only labels and assertions):
    research/.venv/bin/python -I research/checks/l2_hardness.py smoke > research/checks/results/raw/l2_smoke.out 2>&1
  Main (after the run task has committed results/raw/l2_inputs.json and l2_screening.tsv):
    research/.venv/bin/python -I research/checks/l2_hardness.py main > research/checks/results/raw/l2_main.out 2>&1
  Inputs file: {"synthetic": false, "screening_log": "results/raw/l2_screening.tsv", "unavailable": [bib ids],
    "records": [{id, route, stat, values, population, period, human, pre_transition, from_figure,
    prerepro_mortality_from_birth (route b), density_measure (route a), bib_id, quote_ids, locator, sha256,
    access_date, synthetic}]}; values are {"est", "lo", "hi"} dicts per key (lo/hi optional).
"""
import json
import math
import os
import resource
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "results", "raw")
INPUTS = os.path.join(RAW, "l2_inputs.json")
HF_MD = os.path.join(HERE, "results", "R4-HF.md")

C1, C2 = 0.1, 0.3
G_YEARS = (25.0, 30.0)
HF_STRINGS = ("about 1.3-1.7x", "2.6-3.5x at R = 1.111", "0.83x and 1.05x", "1.9x and 2.8x")

STATS_A = ("beta_gen", "beta_annual", "kappa_annual", "halflife_years", "vital_elasticities_N",
           "vital_elasticities_wage", "cohort_elasticity")
STATS_B = ("crow", "episodes", "differentials")
DENSITY = ("population", "density", "cohort_size", "wage_composite")
REQ = ("id", "route", "stat", "values", "population", "period", "human", "pre_transition", "from_figure",
       "bib_id", "quote_ids", "locator", "sha256", "access_date", "synthetic")
BANDS = ("LL", "LM", "LH", "MM", "MH", "HH")
OUTCOMES = ("U0",) + tuple("U1-" + b for b in BANDS) + tuple("B-" + b for b in BANDS)
READ_A = ("A1", "A-up", "A-down")
READ_B = ("M-b1", "M-b2", "M-b0")

MOVES = {
    "H": {"B-HH": "no value move; h-arm closed toward Day (soft-selection escape does not apply); contest rests on R, D, K",
          "B-LL": "no value move; h-arm closed toward critics (limit >= about 2.6x the hard cap); queue HF mix run at the sourced h"},
    "H5": {"B-HH": "no value move; as H", "B-LL": "no value move; as H"},
    "H8": {"B-HH": "contested -> supported (Term 3 holds within R1 at the sourced h; readings A1 and M-b1)",
           "B-LL": "contested -> contradicted (Term 3 exceeded >= 1.36-1.9x at the sourced h; readings A1 and M-b1)"},
}
DEFAULT_MOVE = {"U0": "no move; h stays a declared bracket (no human source admits a mapping)"}


def clip(x):
    return min(1.0, max(0.0, x))


def tri(v):
    est = float(v["est"])
    lo, hi = float(v.get("lo", est)), float(v.get("hi", est))
    assert lo <= est <= hi, ("interval out of order", v)
    return lo, est, hi


def hull(ivs):
    ivs = [iv for iv in ivs if iv is not None]
    return (min(i[0] for i in ivs), max(i[1] for i in ivs)) if ivs else None


def band(iv):
    lo, hi = iv
    assert lo <= hi
    if hi < C1:
        return "LL"
    if lo < C1:
        return "LM" if hi < C2 else "LH"
    if lo < C2:
        return "MM" if hi < C2 else "MH"
    return "HH"


def beta_from(stat, v, G=G_YEARS):
    """(lo, hi) of beta_gen before clipping; G is a bracket (Gmin, Gmax)."""
    gmin, gmax = G
    if stat == "beta_gen":
        lo, _, hi = tri(v["beta"])
        return lo, hi
    if stat == "beta_annual":
        lo, _, hi = tri(v["phi"])
        f = lambda p, g: (p ** g) if p > 0 else 0.0
        return min(f(lo, gmax), f(lo, gmin)), max(f(hi, gmin), f(hi, gmax))
    if stat == "halflife_years":
        lo, _, hi = tri(v["T"])
        assert lo > 0, "half-life must be positive"
        return 2.0 ** (-gmax / lo), 2.0 ** (-gmin / hi)
    if stat in ("kappa_annual", "vital_elasticities_N", "vital_elasticities_wage"):
        if stat == "kappa_annual":
            klo, _, khi = tri(v["kappa"])
        else:
            b, d = float(v["b"]["est"]), float(v["d"]["est"])
            if stat == "vital_elasticities_N":
                eb, ed = tri(v["eps_b"]), tri(v["eps_d"])
            else:
                ew = tri(v["eps_w_N"])
                prod = lambda x: (min(p * q for p in (x[0], x[2]) for q in (ew[0], ew[2])),
                                  0.0, max(p * q for p in (x[0], x[2]) for q in (ew[0], ew[2])))
                eb, ed = prod(tri(v["eps_b_w"])), prod(tri(v["eps_d_w"]))
            klo, khi = d * ed[0] - b * eb[2], d * ed[2] - b * eb[0]
        f = lambda k, g: math.exp(-k * g)
        return min(f(khi, gmax), f(khi, gmin)), max(f(klo, gmin), f(klo, gmax))
    raise KeyError(stat)


def map_a(rec, G=G_YEARS):
    stat, v, flags = rec["stat"], rec["values"], []
    if stat == "cohort_elasticity":
        lo, _, hi = tri(v["eps"])
        a1 = (0.0, 1.0 + hi)
    else:
        a1 = beta_from(stat, v, G)
    if a1[0] < 0 or a1[1] > 1:
        flags.append("clipped")
    a1 = (clip(a1[0]), clip(a1[1]))
    return {"A1": a1, "A-up": (a1[0], 1.0), "A-down": (0.0, a1[1])}, flags


def map_b(rec):
    stat, v, flags = rec["stat"], rec["values"], []
    if stat == "crow":
        ps = tri(v["Ps"])
        im = tri(v["Im"]) if "Im" in v else tuple((1 - p) / p for p in (ps[2], ps[1], ps[0]))
        i_f = tri(v["If"])
        h1 = (im[0] / (im[0] + i_f[2] / ps[0]), im[2] / (im[2] + i_f[0] / ps[2]))
        h2 = (h1[0], 1.0)
    elif stat == "episodes":
        s, m, f = tri(v["I_surv"]), tri(v["I_mate"]), tri(v["I_fpm"])
        h1 = (s[0] / (s[0] + m[2] + f[2]), s[2] / (s[2] + m[0] + f[0]))
        h2 = ((s[0] + f[0]) / (s[0] + f[0] + m[2]), (s[2] + f[2]) / (s[2] + f[2] + m[0]))
    elif stat == "differentials":
        def absr(x):
            lo, _, hi = x
            return (0.0 if lo <= 0 <= hi else min(abs(lo), abs(hi))), max(abs(lo), abs(hi))
        sv, sf = absr(tri(v["S_v"])), absr(tri(v["S_f"]))
        den = lambda a, b: a / (a + b) if a + b > 0 else 0.0
        h1 = (den(sv[0], sf[1]), den(sv[1], sf[0]) if sv[1] + sf[0] > 0 else 1.0)
        h2 = (h1[0], 1.0)
    else:
        raise KeyError(stat)
    if h1[0] < 0 or h1[1] > 1:
        flags.append("clipped")
    h1 = (clip(h1[0]), clip(h1[1]))
    return {"M-b1": h1, "M-b2": (clip(h2[0]), clip(h2[1])), "M-b0": (0.0, h1[1])}, flags


def check_record(rec):
    for k in REQ:
        assert k in rec, ("missing field", k, rec.get("id"))
    assert rec["route"] in ("a", "b"), rec["id"]
    assert rec["stat"] in (STATS_A if rec["route"] == "a" else STATS_B), (rec["id"], rec["stat"])
    why = []
    if not rec["human"]:
        why.append("E1 not human")
    if not rec["pre_transition"]:
        why.append("E2 post-transition")
    if rec["route"] == "b":
        assert "prerepro_mortality_from_birth" in rec, rec["id"]
        if not rec["prerepro_mortality_from_birth"]:
            why.append("E3 no mortality from birth")
    else:
        assert rec.get("density_measure") in DENSITY, (rec["id"], rec.get("density_measure"))
        if rec["density_measure"] == "wage_composite" and rec["stat"] != "vital_elasticities_wage":
            why.append("E3 wage regressor without the wage-population link")
    if not (rec["quote_ids"] and rec["locator"] and len(rec["sha256"]) == 64 and rec["access_date"]):
        why.append("E4 provenance incomplete")
    if rec["from_figure"]:
        why.append("E5 read off a figure")
    return why


def classify(records, modern=False, G=G_YEARS, ra="A1", rb="M-b1"):
    rows, route_iv = [], {"a": [], "b": []}
    for rec in records:
        why = check_record(rec)
        if modern:
            why = [w for w in why if not w.startswith("E2")]
        rd, flags = map_a(rec, G) if rec["route"] == "a" else map_b(rec)
        rows.append((rec, rd, flags, why))
        if not why:
            route_iv[rec["route"]].append(rd[ra if rec["route"] == "a" else rb])
    ia, ib = hull(route_iv["a"]), hull(route_iv["b"])
    if ia is None and ib is None:
        out, gov = "U0", None
    elif ia is None or ib is None:
        gov = ia or ib
        out = "U1-" + band(gov)
    else:
        gov = hull([ia, ib])
        out = "B-" + band(gov)
    disjoint = bool(ia and ib and (ia[1] < ib[0] or ib[1] < ia[0]))
    inter = (max(ia[0], ib[0]), min(ia[1], ib[1])) if (ia and ib and not disjoint) else None
    return {"rows": rows, "a": ia, "b": ib, "gov": gov, "outcome": out, "disjoint": disjoint, "inter": inter}


def moves(outcome):
    res = {}
    for c in ("H", "H5", "H8"):
        res[c] = MOVES[c].get(outcome) or DEFAULT_MOVE.get(outcome) or "no value move; placement sentence only" + (
            " (one route only)" if outcome.startswith("U1") else "")
    return res


def score(r, recs):
    o, gov = r["outcome"], r["gov"]
    both = o.startswith("B-")
    s = {"PD": "hit" if o == "B-HH" else "miss", "PC": "hit" if o == "B-LL" else "miss"}
    s["PD-w"] = ("hit" if gov[0] >= C1 else "miss") if both else "unscorable"
    s["PC-w"] = ("hit" if gov[1] < C2 else "miss") if both else "unscorable"
    s["PA-1"] = "hit" if both else "miss"
    byars = [rec for rec in recs if rec["bib_id"] == "Byars2010" and rec["route"] == "b"]
    s["PA-2"] = "hit" if all(check_record(rec) for rec in byars) else "miss"
    ib, ia = r["b"], r["a"]
    s["PA-3"] = "unscorable" if ib is None else (
        "hit" if (0.2 <= ib[0] and ib[1] <= 0.8 and 0.2 <= ib[0] <= 0.5) else "miss")
    s["PA-4"] = "unscorable" if ia is None else ("hit" if ia[0] < C2 <= ia[1] else "miss")
    s["PA-5"] = "hit" if o in ("B-LH", "B-MH", "U1-LH", "U1-MH", "U1-HH", "U0") else "miss"
    return s


def assert_hf():
    txt = open(HF_MD, encoding="utf-8").read()
    for sstr in HF_STRINGS:
        assert sstr in txt, ("threshold string not found in R4-HF.md", sstr)


def fmt(iv):
    return "unsourced" if iv is None else f"[{iv[0]:.3f}, {iv[1]:.3f}]"


def report(inp):
    recs = inp["records"]
    r = classify(recs)
    print("# L2 main", time.strftime("%Y-%m-%d %H:%M:%S %z"))
    print("unavailable (owner list):", ", ".join(inp.get("unavailable", [])) or "none")
    print("\n| id | route | stat | population | period | bib | A1/M-b1 | up | down | flags | excluded because |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for rec, rd, flags, why in r["rows"]:
        ks = READ_A if rec["route"] == "a" else READ_B
        print(f"| {rec['id']} | {rec['route']} | {rec['stat']} | {rec['population']} | {rec['period']} | {rec['bib_id']} | "
              + " | ".join(fmt(rd[k]) for k in ks) + f" | {','.join(flags) or '-'} | {'; '.join(why) or '-'} |")
    print(f"\nroute (a) primary A1: {fmt(r['a'])}\nroute (b) primary M-b1: {fmt(r['b'])}")
    print(f"governing: {fmt(r['gov'])}  outcome: {r['outcome']}  DISJOINT: {r['disjoint']}  intersection (not used): {fmt(r['inter'])}")
    for c, m in moves(r["outcome"]).items():
        print(f"move {c}: {m}")
    print("\nscores:", json.dumps(score(r, recs)))
    print("\n## sensitivity (never governing)")
    for ra in READ_A:
        print(" | ".join(f"{ra} x {rb}: {classify(recs, ra=ra, rb=rb)['outcome']}" for rb in READ_B))
    print("modern included:", classify(recs, modern=True)["outcome"])
    for g in G_YEARS:
        rr = classify(recs, G=(g, g))
        print(f"G = {g:.0f}: route (a) {fmt(rr['a'])} outcome {rr['outcome']}")


def synthetic():
    """One synthetic case per outcome.  Values are invented to reach each band; they are not data."""
    def rec(i, route, stat, values, **kw):
        base = {"id": i, "route": route, "stat": stat, "values": values, "population": "SYNTH", "period": "SYNTH",
                "human": True, "pre_transition": True, "from_figure": False, "bib_id": "SYNTH", "quote_ids": ["SYNTH"],
                "locator": "SYNTH", "sha256": "0" * 64, "access_date": "2026-10-13", "synthetic": True}
        if route == "a":
            base["density_measure"] = "population"
        else:
            base["prerepro_mortality_from_birth"] = True
        base.update(kw)
        return base
    A = {"L": rec("a", "a", "beta_gen", {"beta": {"est": 0.05, "lo": 0.03, "hi": 0.08}}),
         "M": rec("a", "a", "halflife_years", {"T": {"est": 12.0, "lo": 11.0, "hi": 13.0}}),
         "H": rec("a", "a", "kappa_annual", {"kappa": {"est": 0.01, "lo": 0.008, "hi": 0.012}})}
    B = {"L": rec("b", "b", "episodes", {"I_surv": {"est": 0.02}, "I_mate": {"est": 0.9}, "I_fpm": {"est": 0.03}}),
         "M": rec("b", "b", "differentials", {"S_v": {"est": 0.2}, "S_f": {"est": 0.8}}),
         "H": rec("b", "b", "crow", {"Ps": {"est": 0.5}, "If": {"est": 0.6}})}
    cases = {"U0": []}
    for xy in BANDS:
        lo, hi = xy
        a = [A[lo], A[hi]]
        cases["U1-" + xy] = a
        cases["B-" + xy] = [A[lo], B[hi]]
    return cases


def smoke():
    t0 = time.time()
    assert_hf()
    # unit checks of the mappings (limits and monotonicity)
    assert abs(beta_from("halflife_years", {"T": {"est": 1e12}})[0] - 1.0) < 1e-6
    assert beta_from("halflife_years", {"T": {"est": 1.0}})[1] < 1e-6
    assert beta_from("beta_annual", {"phi": {"est": 0.99}}) == (0.99 ** 30, 0.99 ** 25)
    b = beta_from("vital_elasticities_N", {"b": {"est": 0.03}, "d": {"est": 0.03},
                                           "eps_b": {"est": -0.1}, "eps_d": {"est": 0.1}})
    assert abs(b[1] - math.exp(-0.006 * 25)) < 1e-12
    w = beta_from("vital_elasticities_wage", {"b": {"est": 0.03}, "d": {"est": 0.03}, "eps_b_w": {"est": 0.5},
                                              "eps_d_w": {"est": -0.5}, "eps_w_N": {"est": -0.2}})
    assert abs(w[0] - b[0]) < 1e-12 and abs(w[1] - b[1]) < 1e-12
    crow, _ = map_b({"stat": "crow", "values": {"Ps": {"est": 0.5}, "If": {"est": 0.5}}})
    assert abs(crow["M-b1"][0] - 0.5) < 1e-12 and crow["M-b2"] == (0.5, 1.0) and crow["M-b0"] == (0.0, 0.5)
    ep, _ = map_b({"stat": "episodes", "values": {"I_surv": {"est": 1}, "I_mate": {"est": 1}, "I_fpm": {"est": 2}}})
    assert ep["M-b1"] == (0.25, 0.25) and ep["M-b2"] == (0.75, 0.75)
    ce, fl = map_a({"stat": "cohort_elasticity", "values": {"eps": {"est": -0.5, "lo": -0.7, "hi": -0.3}}})
    assert ce["A1"] == (0.0, 0.7) and not fl
    # every band boundary
    for iv, want in (((0.0, 0.0999), "LL"), ((0.0, 0.1), "LM"), ((0.0, 0.3), "LH"), ((0.1, 0.2999), "MM"),
                     ((0.1, 0.3), "MH"), ((0.3, 1.0), "HH")):
        assert band(iv) == want, (iv, band(iv))
    # eligibility exclusions and missing-field assertion
    cases = synthetic()
    bad = dict(cases["B-HH"][1], prerepro_mortality_from_birth=False, bib_id="Byars2010")
    assert check_record(bad) == ["E3 no mortality from birth"]
    try:
        check_record({k: v for k, v in bad.items() if k != "sha256"})
        raise SystemExit("missing-field assertion did not fire")
    except AssertionError:
        pass
    # all 13 outcomes reachable; scoring and moves run on each
    seen = set()
    for want, recs in cases.items():
        r = classify(recs)
        assert r["outcome"] == want, (want, r["outcome"])
        score(r, recs)
        moves(r["outcome"])
        for ra in READ_A:
            for rb in READ_B:
                classify(recs, ra=ra, rb=rb)
        seen.add(r["outcome"])
    assert seen == set(OUTCOMES), set(OUTCOMES) - seen
    # a disjoint pair is flagged and read off the hull
    r = classify([cases["B-LL"][0], cases["B-HH"][1]])
    assert r["disjoint"] and r["outcome"] == "B-LH" and r["inter"] is None
    # main refuses synthetic input
    try:
        run_main({"synthetic": True, "screening_log": "x", "records": []})
        raise SystemExit("main accepted synthetic input")
    except AssertionError:
        pass
    print("smoke ok: outcomes reached", len(seen), "of", len(OUTCOMES), "| HF threshold strings asserted",
          f"| {time.time() - t0:.3f} s | max RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024:.1f} MB")


def run_main(inp):
    assert inp.get("synthetic") is False, "main refuses synthetic input"
    assert all(rec.get("synthetic") is False for rec in inp["records"]), "synthetic record in main input"
    log = os.path.join(HERE, inp["screening_log"]) if not os.path.isabs(inp["screening_log"]) else inp["screening_log"]
    assert os.path.exists(log), ("screening log missing (search protocol S2)", log)
    assert_hf()
    report(inp)


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "smoke":
        smoke()
    elif mode == "main":
        run_main(json.load(open(INPUTS, encoding="utf-8")))
    else:
        raise SystemExit("usage: l2_hardness.py smoke|main")

#!/usr/bin/env python3
"""M-111 record (identity, derivation): k = mu in a finite window, and what arXiv 2208.00148v1 says about it.

Object: docs/research/math/objects.yaml M-111 (identity, derivation). The post (pgenetics, 10-23) says no finite
period has k = mu under overlapping generations, citing arXiv 2208.00148v1, and that "only one condition" allows it:
an effective population "completely static" and "equal to the census population"; and that the identity "contains
no time term". Hancock (evo009@L57, relayed): refuted by 1930s population genetics; Day (evo009@L58): six papers
address the classical formulas. Nothing is recomputed: the finite-window count is M-201, which N enters is M-209,
census fluctuation with overlap is M-210, and the reading of the cited paper is M-223 and claim file B1e.
(1) The cited paper (Chalub 2022, held: sources/raw/b1e-q2-2026-10-13/, bib Chalub2022) models "a population of two
types evolving without mutation or selection" (quotes-literature): it has no mutation term, so it states no k and no
mu; the held text has no "overlap", "census" or "substitution". The claim attributed to it is not in it.
(2) Finite window: from an empty start the expected count is below mu L T for every finite T (M-201: 6.36M of
7.56M at N_e = 1e4, 84.1%); from a population at equilibrium it is mu L T for every T (M-201, critic row). So "no
finite period" holds for an empty start and fails for an equilibrium start; the start state is M-202 (open).
(3) Static and equal to census: with constant sizes k/mu = 1 at every N/N_e tried (M-209), so "equal to census" is
not needed; fluctuation with overlap does move k over a window (RRME 0.743 over four cohorts; B&L -0.03% to -1.1%
at human survival, M-210). (4) "No time term": k is a rate per generation; the count needs a start state and a
window, which Day's own Z22903977 says (branch B, B1 q2). Both positions are recorded; no verdict here.

Run: research/.venv/bin/python -I docs/research/math/records/M-111.py [--write]
Without --write it checks that M-111.json is current; --write saves it.
"""
import hashlib, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
REC = "docs/research/math/records/"
RAW = {"pgenetics": "sources/raw/refresh-2026-11-01/p-breaking-population-genetics/body.txt",
       "evo009": "sources/raw/refresh-2026-11-01/p-erika-and-the-evo-avengers-009/body.txt"}
CHALUB = "sources/raw/b1e-q2-2026-10-13/chalub2022v1.txt"
QL = "docs/research/sources/quotes-literature.md"
B1E = "docs/research/claims/B1e-chalub-2022-reading.md"


def held(rel, quote):
    """The quote, checked verbatim (whitespace-normalised) against a held file."""
    norm = lambda s: " ".join(s.split())
    assert norm(quote) in norm((ROOT / rel).read_text(encoding="utf-8")), (rel, quote[:60])
    return quote


def post(src, quote):
    """A source-map quote (committed), re-checked against the held post body when sources/raw is in this checkout."""
    held(SM + src + ".md", quote)
    if (ROOT / RAW[src]).exists():
        held(RAW[src], quote)
    return quote


def raw(src, quote):
    """A sentence from the held post body that the source map does not copy; checked when sources/raw is present."""
    if (ROOT / RAW[src]).exists():
        held(RAW[src], quote)
    return quote


def record(rec):
    return json.loads((ROOT / REC / f"{rec}.json").read_text(encoding="utf-8"))


def cited(rec, key):
    """A value from a settled record's JSON (cited, not recomputed)."""
    return record(rec)["values"][key]


def near(x, target, tol):
    assert abs(x - target) <= tol, (x, target, tol)
    return x


def finish(rec):
    rec = {"id": HERE.stem, "date": DATE, "script": f"docs/research/math/records/{HERE.name}",
           "script_sha256": hashlib.sha256(HERE.read_bytes()).hexdigest(), **rec}
    out = json.dumps(rec, indent=2, ensure_ascii=False) + "\n"
    js = HERE.with_suffix(".json")
    if "--write" in sys.argv:
        js.write_text(out, encoding="utf-8")
    elif js.exists():
        assert js.read_text(encoding="utf-8") == out, f"{js.name} is stale; rerun with --write"
    print(f"{HERE.stem}: all asserts pass")


# ---- the source sentences ------------------------------------------------------------------------------
D_ASK = post("pgenetics", "is there any finite time period in which k = μ when there are overlapping generations in "
                          "the population?")                                                  # pgenetics@L7
D_ONE = post("pgenetics", "there is only one condition in finite time when mutations can equal fixations, and that is "
                          "when the effective population is both a) completely static and b) equal to the census "
                          "population.")                                                      # pgenetics@L10
D_TIME = post("pgenetics", "The identity contains no time term and therefore cannot address whether any number of "
                           "fixations can complete in any given window.")                     # pgenetics@L16
D_CORRECT = raw("pgenetics", "While Kimura’s derivation is mathematically correct, it is a limited steady-state "
                             "identity that is almost always improperly applied")             # pgenetics@L16
raw("pgenetics", "https://arxiv.org/html/2208.00148v1")                                       # pgenetics@L8
H_1930 = post("evo009", "Vox’s model is refuted by basic population genetics from the 1930s that I derived already.")  # L57, relay
D_SIX = post("evo009", "I have specifically addressed why the classical population genetic fixation formulas are "
                       "incorrect.")                                                          # evo009@L58
D_RATE = held(SM + "branch-B.md", "It is a rate, not a count, and converting it to a count requires assumptions the "
                                  "identity itself cannot supply.")                           # B1 q2, Z22903977 s1
C_NOMU = held(QL, "\"we consider a population of two types evolving without mutation or selection, the so-called "
                  "neutral evolution\"")                                                      # Chalub 2022 abstract
C_FID = held(QL, "Paper is a two-allele PDE solution with no mutation or selection, so it does not address "
                 "substitution rates")
held(B1E, "relevant to finite-time P_fix, not to k vs μ")

# ---- (1) the cited paper, held text only ------------------------------------------------------------------------
chalub_checked = (ROOT / CHALUB).exists()
if chalub_checked:
    text = (ROOT / CHALUB).read_text(encoding="utf-8")
    held(CHALUB, "we consider a population of two types evolving without mutation or selection, the so-called neutral "
                 "evolution.")
    for word in ("overlap", "census", "substitution", "molecular clock"):
        assert not re.search(word, text, re.I), word                 # none of the claim's terms occur in the paper

# ---- (2) finite window: cited from M-201 ----------------------------------------------------------------------------
naive = cited("M-201", "naive_muLT")
assert naive == 7_560_000                                            # mu L T = 30 x 252,000 (Day's Q36 inputs, B1a)
empty_1e4 = cited("M-201", "leading_order")["10000"]
assert empty_1e4 == 6_360_000 and empty_1e4 < naive                  # empty start: mu L (T - 4 N_e) < mu L T
near(empty_1e4 / naive, 0.8413, 5e-5)
near(cited("M-201", "exact_over_naive_at_T_eq_4Ne"), 0.200941, 1e-6) # exact series at T = 4 N_e: 20%
full = record("M-201")["positions"]["critic"]["count_full_start"]
assert full == naive                                                 # equilibrium start: the count is mu L T

# ---- (3) which N, and a fluctuating census: cited from M-209 and M-210 -----------------------------------------------
assert set(cited("M-209", "k_over_mu_cancelled").values()) == {1}    # constant sizes: k/mu = 1 at every N/N_e pair
near(cited("M-210", "rrme_k_over_mu"), 0.742847, 1e-6)               # four-cohort window, fluctuating census
bl = record("M-210")["positions"]["critic"]
assert bl["bl_no_overlap"] == 1.0                                    # B&L: no overlap, k = mu
lo, hi = bl["bl_human_cycle_range"]
near(1 - lo, 0.0108, 5e-5); near(1 - hi, 0.0003, 5e-5)               # overlap at human survival: -1.1% to -0.03%

finish({
    "object": "M-111",
    "inputs": [
        {"name": "cited paper", "value": "Chalub 2022, arXiv:2208.00148v1", "cite": "pgenetics@L8; bib Chalub2022; quotes-literature; held sources/raw/b1e-q2-2026-10-13/chalub2022v1.txt"},
        {"name": "finite-window count", "value": {"naive": naive, "empty_start_Ne_1e4": empty_1e4, "full_start": full}, "cite": "M-201 (Day's Q36 inputs: mu L = 30, T = 252,000)"},
        {"name": "k/mu by N, census fluctuation", "value": {"constant_sizes": 1, "rrme_four_cohorts": 0.742847}, "cite": "M-209, M-210"},
    ],
    "values": {
        "chalub_models_mutation": False,
        "chalub_terms_absent_checked_against_raw": chalub_checked,
        "empty_start_over_naive_Ne_1e4": round(empty_1e4 / naive, 4),
        "full_start_over_naive": 1,
        "k_over_mu_constant_sizes_any_N_over_Ne": 1,
        "k_over_mu_rrme_window": 0.742847,
        "bl_overlap_human_effect_pct": [-1.08, -0.03],
    },
    "positions": {
        "day": {"reading": "k = mu is a steady-state identity; no finite period has k = mu under overlap except a static "
                           "N_e equal to census; it has no time term, so it cannot bound a window",
                "holds": "from an empty start the window count is below mu L T at every finite T (84.1% at N_e = 1e4, "
                         "20% at T = 4 N_e, M-201); census fluctuation with overlap moves k over a window (M-210); "
                         "Day's own Z22903977 says a count needs assumptions the identity cannot supply"},
        "critic": {"reading": "k = mu is the expected long-run substitution rate; the cited paper is outside evolution "
                              "journals and gives no derivation of the claim; Hancock: refuted by 1930s theory",
                   "holds": "the cited paper has no mutation, so it cannot show k != mu (B1e: relevant to P_fix(t), not "
                            "to k vs mu); from an equilibrium start the window count is mu L T at every T (M-201); "
                            "k/mu = 1 at any constant N/N_e (M-209), so 'equal to census' is not a condition; the B&L "
                            "overlap effect at human survival is 0.03-1.1%"},
    },
    "notes": "The finite-window question is settled by the start state, not by the identity: empty start, below mu L T "
             "for every finite T; equilibrium start, mu L T for every T. Which start applies at the human-chimp split "
             "is M-202 (data-check, open). The arXiv 2208.00148v1 attribution is checked against held text only: "
             "the paper is a no-mutation two-allele diffusion (M-223 reads its P_fix(t) -> x0 result), so the "
             "'static and equal to census' condition is the post's own statement, not the paper's. Day's six papers "
             "(evo009@L58) are not re-derived here; k != mu is the B branch records. Hancock's 1930s derivation is "
             "not in the window.",
})

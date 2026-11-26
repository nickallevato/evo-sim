#!/usr/bin/env python3
"""M-916 record (derivation): the arithmetic of Sparky_6_4's KITTENS post (RE-2, r/DebateEvolution 1wxgsjm, 2026-10-04,
self-disclosed AI-assisted) that the library did not hold.

Object: docs/research/math/objects.yaml M-916 (identity, derivation, variant_of M-007). Source map
docs/research/math/sources/kittens-re2.md (locators kt@L<n> = line n of the post's selftext as fetched 2026-11-26).
Already settled elsewhere and only cited here (loaded and checked, not recomputed): kappa = 38.4/4.1e-4 = 93,658.5,
205/17.5 = 11.714 and the product 1,097,140 against 1,075,000 (M-007); 252,000/1,322 = 190.62 and 17.89e6 achievable
(M-008); 38.4 x 252,000 = 9,676,800 and 2 x 76.8 x 252,000 = 38,707,200 (M-212); the s6.4 supermutator slip (M-015);
the mean over seven mutators 104.7 and the Ara-2-excluded 70.6 (claim E5); Day's 4-13 as 252,000/66,000 and /20,000
(claim G2); the A5b sensitivity 81x-445x at a = 0.47-0.61 (claim A5b).
Inputs are KITTENS's own, each read from MITTENS 3.0 as KITTENS relays it (paper text not in this checkout; where the
library quotes the paper, the relay matches: E5, E7, A2d, A2e, Q130): U_E = 4.1e-4 (s4.3), 50,000 and 60,000
generations, 56 clone-pair fixations (s4.3), the seven clone-pair mutator counts (s5.1), 893 and 1,359 (s3.3), Ne
10,000-33,000 and 3e7 (s8.2), 7 -> 63 (Ara-5) and 28 -> 68 (Ara+4) (s4.1 table), the 70-100-fold mutator range.
The record asserts every number the D-41 item-3 review page states that is not in an earlier record:
- LTEE neutral clock: 4.1e-4 x 50,000 = 20.5 of 56 = 36.6% ("more than a third"); 1/1,322 = 7.56e-4 per generation,
  1.845x U_E ("about 1.8"; the clock is 54.2% of that rate); on the clone-pair basis 56/50,000 = 1.12e-3, 2.73x
  U_E (mixed basis in the post);
- human neutral count against 17.5M: 1.808 ("a factor of 1.8"); Day's 20,000-66,000 generations per neutral fixation
  are 2 x Ne at Ne 10,000-33,000 (the conditional mean fixation time is 4Ne, M-203);
- steady state: 4Ne = 40,000-132,000 ("40,000-130,000") < 252,000; if the start were empty (M-201, Day's reading)
  38.4 x (252,000 - 4Ne) = 8,140,800-4,608,000, i.e. 2.15x-3.80x short of 17.5M; LTEE 4 x 3e7 = 1.2e8 ("about 10^8");
- haploid SNV both lineages: 2 x 38.4 x 252,000 = 19,353,600 ("about 19 million") against 35M (1.81x);
- mutators: the seven counts sum to 3,343 (mean 477.57, 50,000/477.57 = 104.7); KITTENS's four lines 932, 803, 978,
  1,153 sum to 3,866, mean 966.5, 50,000/966.5 = 51.73, 966.5/56.0 = 17.26 ("about 17-fold"); exponents
  a = ln f / ln 100: 0.4655 (8.53x, all seven), 0.551 (12.65x, Ara-2 out), 0.6185 (17.26x, KITTENS's four);
  scaled by kappa^a the achievable 190.62 becomes 39,285 / 104,601 / 226,610 and the SNV-only shortfall 445x / 167x /
  77x (205M: 5,218x / 1,960x / 905x); neutral prediction 4.1e-4 x 70-100 x 50,000 = 1,435-2,050 against 803-1,153
  observed (0.39-0.80 of it);
- non-mutator table: 4.1e-4 x 10,000 = 4.1 per lineage per 10,000 generations ("about 4"); jumps of 56 (Ara-5) and
  40 (Ara+4) are 13.7x and 9.8x that; 1,359/893 = 1.522 ("about 52%");
- requirement: 35e6 + 2 x 187e6 = 409e6 (KITTENS's reconstruction of 410M; M-009 holds the components); 410/2 = 205;
  on the library's event counts per lineage (M-008: 21.05M hg38, 24.14M T2T; non-SNV events 3.55M and 6.64M) the
  "about 12 times" is 9.74 or 8.49 (-17% / -28%, R1), and RE-08's parity is 0.85 or 0.74;
- s5.4 baseline: 38.4 x 1e7 = 3.84e8 (KITTENS uses it to show the s6.4 baseline is 38.4, as M-015).

Run: research/.venv/bin/python -I docs/research/math/records/M-916.py [--write]
Without --write it checks that M-916.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
MAP = "docs/research/math/sources/kittens-re2.md"
RAW = "sources/raw/kittens-re2-2026-11-26/post-1wxgsjm.json"
REC = ROOT / "docs/research/math/records"


def norm(s):
    return " ".join(s.split())


def held(text, quote, where):
    assert norm(quote) in norm(text), (where, quote[:60])
    return quote


RAW_TEXT = None
if (ROOT / RAW).exists():
    RAW_TEXT = json.loads((ROOT / RAW).read_text(encoding="utf-8"))["data"][0]["selftext"]


def kt(quote):
    """A KITTENS quote: in the committed source map, and in the held fetch when this checkout has it."""
    held((ROOT / MAP).read_text(encoding="utf-8"), quote, MAP)
    if RAW_TEXT is not None:
        held(RAW_TEXT, quote, "raw")
    return quote


def near(x, y, tol):
    assert abs(x - y) <= tol, (x, y)


def val(m, *path):
    v = json.loads((REC / f"{m}.json").read_text(encoding="utf-8"))["values"]
    for p in path:
        v = v[p]
    return v


# ---- the source sentences ---------------------------------------------------------------------------
kt("The claimed shortfall is 94,000 × 11.7, or about 1.1 million.")
kt("Once one scales the LTEE rate for the mutation supply per genome and counts SNVs as events, the achievable number (17.9 million) is about equal to the required number (17.5 million).")
kt("I present this as an illustration, not as a proof that adaptive fixations scale linearly with mutation rate.")
kt("So more than a third of the non-mutator throughput is just the mutation clock running.")
kt("Indeed, the observed LTEE rate (one per 1,322 generations, or 7.6×10\\^-4 per generation) is only about 1.8 times the paper’s own neutral expectation of 4.1×10\\^-4.")
kt("With the paper’s own U of 38.4 and its own 252,000 generations, that is about 9.7 million neutral substitutions per lineage, against 17.5 million SNVs required.")
kt("the approach to steady state takes of the order of 4Ne generations, 40,000–130,000 for human Ne, comfortably inside 252,000.")
kt("With haploid single-nucleotide bookkeeping, as I use above, the expectation for both lineages is about 19 million against roughly 35 million observed.")
kt("The four lines the paper lists at roughly 70–100-fold (Ara+3, Ara+6, Ara-1, Ara-4) give 932, 803, 978 and 1,153, a mean of 966.5 against 56.0 for non-mutators, which is about 17-fold (51.7 generations per fixation), in line with the 16.9-fold the paper gets from metagenomics.")
kt("the paper’s own §4.3 formula predicts roughly 1,400–2,050 neutral accumulations in a 70–100-fold line over 50,000 generations (4.1×10\\^-4 × 70–100 × 50,000).")
kt("At the paper’s own U of 4.1×10\\^-4, a single lineage acquires about 4 new mutations per 10,000 generations.")
kt("At the same timepoint, 50,000 generations, the paper’s own table (§3.3) shows 893 versus 1,359, a difference of about 52%")
kt("35 million + 2 × 187 million ≈ 409 million")
kt("A count of fixed mutations cannot be negative; the negative value comes from the paper’s own correction")
kt("Literature citations are from memory and should be verified before reuse.")

# ---- reused, loaded from their records ---------------------------------------------------------------------------
U_H, U_E, T = 38.4, 4.1e-4, 252_000
kappa = val("M-007", "kappa")
near(kappa, U_H / U_E, 0.1); kappa = U_H / U_E                    # exact value from here on
near(val("M-007", "kittens_product"), 1_097_140, 1)
F = val("M-008", "F_nonmutator")
near(F, T / 1322, 0.01); F = T / 1322                                 # exact value from here on
near(val("M-008", "kittens_achievable"), 17.8888e6, 100)
neutral_h = val("M-212", "counts", "dd_haploid")
assert neutral_h == U_H * T == 9_676_800
assert val("M-212", "counts", "hancock_x2") == 2 * 76.8 * T
near(val("M-015", "mutations"), 3840, 1e-6)

# ---- s4: the LTEE neutral clock ---------------------------------------------------------------------------
G_CP, N_CP = 50_000, 56
neutral_ltee = U_E * G_CP
near(neutral_ltee, 20.5, 1e-9)
share = neutral_ltee / N_CP
near(share, 0.36607, 1e-5); assert share > 1 / 3                       # "more than a third"
rate_meta = 1 / 1322
near(rate_meta, 7.564e-4, 1e-7)                                         # "7.6x10^-4"
near(rate_meta / U_E, 1.8450, 1e-4)                                     # "about 1.8"
near(U_E / rate_meta, 0.5420, 1e-4)                                     # the clock is 54% of the metagenomic rate
near(N_CP / G_CP / U_E, 2.7317, 1e-4)                                   # the clone-pair basis of the same comparison

# ---- s4: human neutral count, Day's 4-13, the 4Ne transient ---------------------------------------------
near(17.5e6 / neutral_h, 1.8084, 1e-4)                                  # "a factor of 1.8"
NE = (10_000, 33_000)
assert (2 * NE[0], 2 * NE[1]) == (20_000, 66_000)                       # Day's "20,000-66,000" = 2Ne, not 4Ne (M-203)
near(T / 66_000, 3.818, 1e-3); near(T / 20_000, 12.6, 1e-9)             # "4-13" (claim G2)
four_ne = (4 * NE[0], 4 * NE[1])
assert four_ne == (40_000, 132_000) and max(four_ne) < T                # "40,000-130,000 ... inside 252,000"
empty = (U_H * (T - four_ne[0]), U_H * (T - four_ne[1]))
near(empty[0], 8_140_800, 1e-6); near(empty[1], 4_608_000, 1e-6)        # empty-start count (M-201)
near(17.5e6 / empty[0], 2.1497, 1e-4); near(17.5e6 / empty[1], 3.7977, 1e-4)
assert 4 * 3e7 == 1.2e8                                                 # LTEE drift time "about 10^8"

# ---- s4: Hancock relay ------------------------------------------------------------------------------------
both = 2 * U_H * T
near(both, 19_353_600, 1e-6)                                            # "about 19 million"
near(35e6 / both, 1.8084, 1e-4)

# ---- s5: mutators -----------------------------------------------------------------------------------------
seven = [110, 932, 803, 978, -906, 273, 1153]
assert sum(seven) == 3343
near(sum(seven) / 7, 477.571, 1e-3); near(G_CP / (sum(seven) / 7), 104.696, 1e-3)
six = [c for c in seven if c != -906]
near(G_CP / (sum(six) / 6), 70.605, 1e-3)                               # claim E5
four = [932, 803, 978, 1153]
assert sum(four) == 3866 and sum(four) / 4 == 966.5
near(G_CP / 966.5, 51.733, 1e-3)                                        # "51.7"
near(G_CP / 893, 55.991, 1e-3)                                          # "56.0"
near(966.5 / 56.0, 17.259, 1e-3); near(893 / (G_CP / 966.5), 17.262, 1e-3)   # "about 17-fold"
fold = {"all_seven": 893 / (G_CP / (sum(seven) / 7)), "ara2_out": 893 / (G_CP / (sum(six) / 6)),
        "kittens_four": 893 / (G_CP / 966.5)}
near(fold["all_seven"], 8.529, 1e-3); near(fold["ara2_out"], 12.648, 1e-3)
sens = {}
for k, f in fold.items():
    a = math.log(f) / math.log(100)
    s = kappa ** a
    sens[k] = {"fold": round(f, 3), "a": round(a, 4), "kappa_a": round(s, 1), "achievable": round(F * s),
               "short_17.5M": round(17.5e6 / (F * s), 1), "short_205M": round(205e6 / (F * s))}
assert all(v["a"] < 1 for v in sens.values())                           # sublinear under every subset ("still sublinear")
assert (sens["all_seven"]["a"], sens["ara2_out"]["a"], sens["kittens_four"]["a"]) == (0.4655, 0.551, 0.6185)
assert (sens["all_seven"]["short_17.5M"], sens["ara2_out"]["short_17.5M"], sens["kittens_four"]["short_17.5M"]) == (445.5, 167.3, 77.2)
assert (sens["all_seven"]["short_205M"], sens["ara2_out"]["short_205M"], sens["kittens_four"]["short_205M"]) == (5218, 1960, 905)
assert (sens["all_seven"]["achievable"], sens["ara2_out"]["achievable"], sens["kittens_four"]["achievable"]) == (39285, 104601, 226610)
pred = (U_E * 70 * G_CP, U_E * 100 * G_CP)
near(pred[0], 1435, 1e-9); near(pred[1], 2050, 1e-9)                   # "roughly 1,400-2,050"
near(803 / pred[0], 0.5596, 1e-4); near(1153 / pred[1], 0.5624, 1e-4)
near(803 / pred[1], 0.3917, 1e-4); near(1153 / pred[0], 0.8035, 1e-4)  # observed 0.39-0.80 of the neutral prediction

# ---- s6: the non-mutator table ------------------------------------------------------------------------------
per_10k = U_E * 10_000
near(per_10k, 4.1, 1e-9)                                                # "about 4 new mutations per 10,000 generations"
jumps = {"Ara-5": 63 - 7, "Ara+4": 68 - 28}
assert jumps == {"Ara-5": 56, "Ara+4": 40}
near(jumps["Ara-5"] / per_10k, 13.66, 0.01); near(jumps["Ara+4"] / per_10k, 9.76, 0.01)
near(1359 / 893, 1.5218, 1e-4)                                          # "about 52%"

# ---- s7, s5.4 ------------------------------------------------------------------------------------------------
assert 35e6 + 2 * 187e6 == 409e6 and 410e6 / 2 == 205e6
near(205 / 17.5, 11.714, 1e-3)
ev = {"hg38": 17.5e6 / val("M-008", "share_of_events_gap07b"), "t2t": 17.5e6 / val("M-008", "share_of_events_gap07t")}
near(ev["hg38"], 21.05e6, 0.01e6); near(ev["t2t"], 24.14e6, 0.01e6)    # events per lineage (M-008, M-011)
near(ev["hg38"] - 17.5e6, 3.55e6, 0.01e6); near(ev["t2t"] - 17.5e6, 6.64e6, 0.01e6)   # non-SNV events: not "small"
factor = {k: 205e6 / v for k, v in ev.items()}
near(factor["hg38"], 9.74, 0.01); near(factor["t2t"], 8.49, 0.01)      # "about 12 times below": 9.7 or 8.5
move = {k: f / (205 / 17.5) - 1 for k, f in factor.items()}
near(move["hg38"], -0.1686, 1e-3); near(move["t2t"], -0.2752, 1e-3)    # R1: -17% (ledger) / -28% (error on that reading)
parity = {k: val("M-008", "kittens_achievable") / v for k, v in ev.items()}
near(parity["hg38"], 0.850, 1e-3); near(parity["t2t"], 0.741, 1e-3)    # RE-08 on event counts: 0.85 / 0.74, no flip
near(U_H * 1e7, 3.84e8, 1)                                              # s5.4 "3.84x10^8" confirms the 38.4 baseline


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


finish({
    "object": "M-916",
    "variant_of": "M-007",
    "inputs": [
        {"name": "U_human", "value": U_H, "cite": "kt@L26 (3.2e9 x 1.2e-8; M-007)"},
        {"name": "U_ecoli", "value": U_E, "cite": "kt@L25 (MITTENS 3.0 s4.3 as relayed; M-007)"},
        {"name": "generations_human", "value": T, "cite": "kt@L28"},
        {"name": "clone_pair_nonmutator", "value": [N_CP, G_CP], "cite": "kt@L39, kt@L55 (s4.3 as relayed)"},
        {"name": "mutator_clone_pair_counts", "value": seven, "cite": "kt@L49 (s5.1 as relayed; claim E5)"},
        {"name": "Ne_human", "value": list(NE), "cite": "kt@L39 (s8.2 as relayed)"},
        {"name": "Ne_ltee", "value": 3e7, "cite": "kt@L45 (s8.2 as relayed)"},
        {"name": "table_jumps", "value": {"Ara-5": [7, 63], "Ara+4": [28, 68]}, "cite": "kt@L63 (s4.1 as relayed)"},
        {"name": "clone_pair_vs_metagenomic_50K", "value": [893, 1359], "cite": "kt@L65 (s3.3 as relayed; 1,359 not re-checked)"},
        {"name": "mutator_fold_range", "value": [70, 100], "cite": "kt@L55"},
    ],
    "values": {
        "ltee_neutral": {"neutral_50K": neutral_ltee, "share_of_56": round(share, 5),
                         "rate_meta_over_U": 1.845, "rate_clone_pair_over_U": 2.7317},
        "human_neutral": {"count": neutral_h, "required_over_count": 1.8084, "day_gen_per_fix": "2Ne (20,000-66,000)",
                          "four_Ne": list(four_ne), "empty_start_counts": [8_140_800, 4_608_000],
                          "empty_start_short": [2.1497, 3.7977], "ltee_drift_time": 1.2e8},
        "hancock_relay": {"haploid_snv_both": both, "observed_35M_over": 1.8084},
        "mutators": {"mean_seven": 477.571, "gen_per_fix_seven": 104.696, "gen_per_fix_ara2_out": 70.605,
                     "mean_four": 966.5, "gen_per_fix_four": 51.733, "fold_four": 17.26,
                     "sensitivity": sens, "neutral_prediction": list(pred), "observed_over_prediction": [0.3917, 0.8035]},
        "table": {"per_10k": per_10k, "jumps": jumps, "jump_over_supply": [13.66, 9.76], "1359_over_893": 1.5218},
        "requirement": {"reconstruction": 409e6, "halved": 205e6, "ratio": 11.714,
                        "events_per_lineage": {"hg38": 21.05e6, "t2t": 24.14e6}, "non_snv_events": [3.55e6, 6.64e6],
                        "factor_on_events": {"hg38": 9.74, "t2t": 8.49}, "r1_move": {"hg38": -0.1686, "t2t": -0.2752},
                        "achievable_over_events": {"hg38": 0.850, "t2t": 0.741}},
    },
    "positions": {
        "day": {"reading": "the LTEE rate is an empirical ceiling with mutation supply already inside it; mutators show "
                           "supply scales sublinearly",
                "holds": "every mutator subset is sublinear (a = 0.47-0.62); on KITTENS's own four lines the SNV-only gap is "
                         "77x, not parity; KITTENS's mutator lag argument assumes 50,000 mutator generations"},
        "critic": {"reading": "the shortfall is the unscaled supply ratio times the base-counted requirement",
                   "holds": "the decomposition reproduces (M-007); 37-54% of the LTEE throughput is the mutation clock, which "
                            "scales with U by the paper's own s4.3; the human neutral count is 9.7M (1.8x short), not 4-13; "
                            "the table jumps are 10-14x the per-lineage supply, so they are lineage turnover"},
    },
    "notes": "Post fetched read-only 2026-11-26 (Arctic Shift, post-1wxgsjm.json sha256 947b4bc5...; comment tree sha256 "
             "46dfb6b8..., identical to the bib row). The thread was removed by a moderator (ktc#pdtfcke); no comment "
             "contains maths. MITTENS 3.0 text is not in this checkout: KITTENS's relays are checked only where the "
             "library quotes the paper. Self-disclosed AI assistance and from-memory citations (RE-11).",
})

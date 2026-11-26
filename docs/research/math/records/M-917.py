#!/usr/bin/env python3
"""M-917 record (derivation): the arithmetic of Nesslig20's "Response to Will Duffy | PART I - Population Genetics"
(PS-1, Peaceful Science topic 18094, 2026-10-05, post 1 at version 11, edited to 2026-10-07) that the library did not
hold.

Object: docs/research/math/objects.yaml M-917 (identity, derivation, variant_of M-212). Source map
docs/research/math/sources/nesslig20-ps1.md (locators ps1@s<section>, ps1#p<reply>).
Already settled elsewhere and only cited here (loaded and checked, not recomputed): 2 x 75 x 252,000 = 37.8M, the
zygote reading 18.9M and the haploid 2 x 38.4 x 252,000 = 19,353,600 (M-213); 252,000/1,400 = 180 (M-711); the
empty-start asymptote mu (T - 4Ne) and 0.2009 at T = 4Ne (M-201); U_E = 4.1e-4 (M-007).
Inputs are the post's own, each located in the source map, plus the library's pedigree per-site rate
(parameters.yaml mutation.mu_per_site_per_gen.pedigree_human: 1.2e-8, range 1.1e-8 to 1.5e-8) for the R1 check of PS-01.
The record asserts every number the D-41 item-4 review page states that is not in an earlier record:
- s1.1 lottery: n_50 = ln 0.5 / ln(1 - 1e-8) = 69,314,717.7 (post 69,314,717; the bound is 69,314,718); P(2e8) = 0.8647,
  P(4e8) = 0.9817; P(any of 7e7) = 0.5034 against the printed 0.51 (0.51 needs 71.33M tickets); mean 1/p = 1e8;
- s2.1: P_fix at Ne = 1,000 is 1/2,000 = 0.05%;
- s2.2 R1 of PS-01: 75 per haploid genome = 2.34e-8 per site; haploid counts 35.2 / 38.4 / 48.0 at 1.1 / 1.2 / 1.5e-8;
  both-lineage counts 17.74M / 19.35M / 24.19M, moves -53.1% / -48.8% / -36.0% against 37.8M (zygote reading 18.9M,
  -50%); the move is under 25% only at >= 1.758e-8 per site; 1-2% of 3.1e9 = 31-62M; 19.35M and 18.9M are 37.6% and 39.0%
  below 31M; at 1.5e-8, 24.19M is 22.0% below;
- s2.2 relay of Yoo: 4Ne = 528,000 and 792,000 at Ne 132,000 and 198,000 (2.10x and 3.14x of 252,000);
- s3.1 toy: 1/60 = 1.67%, 9/60 = 15.0%, 10/60 = 16.7%, 60 x 0.167 = 10.0; 410e6/2 = 205e6, 410e6/3e9 = 13.7%;
- s3.3 Kimura's conditional fixation-time CDF F(t) = 1 + sum (-1)^i (2i+1) exp(-i(i+1) t/(4Ne)), 50 terms: median
  3.4788Ne, F(4Ne) = 0.6063, quantiles 0.95 / 0.99 / 0.999 at 8.1878 / 11.4075 / 16.0127 Ne; first-term estimate
  1 - 3 exp(-t/(2Ne)) = 0.5940 at 4Ne and 0.9500 at 8.19Ne; mean = 4Ne (the series sum is 1);
- s3.4 empty-start delivered share (1/T) int_0^T F at T = 252,000: 0.8413 at Ne 10,000 (= 1 - 4Ne/T), 0.0190 at
  132,000, 0.0017 at 198,000; the theta gloss: (2Ne mu)(2Ne) = 4Ne^2 mu, and by the post's own E(xi_i) = theta/i the
  mean sojourn of a new mutation is 2 H_(2Ne-1) = 20.96 generations at Ne = 10,000, not 2Ne = 20,000;
- s3.5: 20,000/45 = 444.4; 13,500/593 = 22.77; 1/444 = 0.002252 and 5.49x U_E; 1e-9 x 4.6e6 = 0.0046; 1e-8 x 3.2e9 = 32;
  1/75 = 0.01333; 25 x 0.013 = 0.325; 12.6e6/0.33 = 38.18M (+1.0% over 37.8M) against 12.6e6/(25/75) = 37.8M.
Every quote in the source map's table is asserted to be in the map and, when this checkout holds the fetch, in the
fetched text (post cooked HTML with tags removed and entities unescaped).

Run: research/.venv/bin/python -I docs/research/math/records/M-917.py [--write]
Without --write it checks that M-917.json is current; --write saves it.
"""
import hashlib, html, json, math, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
MAP = "docs/research/math/sources/nesslig20-ps1.md"
RAW = "sources/raw/ps-18094-2026-11-26/t-18094.json"
REC = ROOT / "docs/research/math/records"


def norm(s):
    return " ".join(s.split())


def detag(cooked):
    c = re.sub(r"<br\s*/?>", "\n", cooked)
    c = re.sub(r"</(p|li|h\d|blockquote|div|tr)>", "\n", c)
    return html.unescape(re.sub(r"<[^>]+>", "", c))


def near(x, y, tol):
    assert abs(x - y) <= tol, (x, y)


def val(m, *path):
    v = json.loads((REC / f"{m}.json").read_text(encoding="utf-8"))["values"]
    for p in path:
        v = v[p]
    return v


# ---- the source sentences ---------------------------------------------------------------------------
MAP_TEXT = (ROOT / MAP).read_text(encoding="utf-8")
RAW_TEXT = None
if (ROOT / RAW).exists():
    posts = json.loads((ROOT / RAW).read_text(encoding="utf-8"))["post_stream"]["posts"]
    assert [p["post_number"] for p in posts] == list(range(1, 9))
    assert posts[0]["username"] == "Nesslig20" and posts[0]["version"] == 11
    RAW_TEXT = "\n".join(detag(p["cooked"]) for p in posts)
rows = [l for l in MAP_TEXT.splitlines() if l.startswith("| ps1")]
quotes = []
for l in rows:
    cell = l.split(" | ")[2]
    q = re.match(r'^"(.*)"(?: \(PS-0\d\))?$', cell)
    assert q, cell[:60]
    quotes.append(q.group(1))
    if RAW_TEXT is not None:
        assert norm(q.group(1)) in norm(RAW_TEXT), q.group(1)[:60]
assert len(quotes) == 55
ON_FILE = {  # quotes-critics.md PS-01..PS-05, verbatim
    "PS-01": "Let’s assume a conservative neutral mutation rate of [ μ_G = 75 ]. That means [ k = 75 ] mutations will fix per generation.",
    "PS-02": "So, the expected number of fixed neutral mutations that separates humans and chimps is ~37.8 million based on this rough calculation.",
    "PS-03": "since they use one (or a few) reference genomes, not all of the differences they identified between genomes are actually fixed in either the human or chimp populations.",
    "PS-04": "Haldane’s reproductive cost limit does not apply to drift, but can it account for most of the genomic differences between humans and chimps?",
    "PS-05": "While one point mutation only affects one base-pair (bp), one InDel can affect many base-pairs, ranging from 10s to 10s of thousands or even 100s of thousands of bp.",
}
for k, q in ON_FILE.items():
    assert q in quotes, k
    if RAW_TEXT is not None:
        assert q in RAW_TEXT, k                                       # exact substring, not only after norm()

# ---- reused, loaded from their records ---------------------------------------------------------------------------
T = 252_000
assert 6_300_000 / 25 == T
counts = val("M-213", "counts")
assert counts["nesslig_as_written"] == 2 * 75 * T == 37.8e6
assert counts["nesslig_zygote_reading"] == 2 * 37.5 * T == 18.9e6
near(counts["haploid_x2"], 2 * 3.2e9 * 1.2e-8 * T, 1e-3)
assert val("M-711", "fixations_book") == 180.0
near(6_300_000 * 1 / (25 * 1_400), 180, 1e-9)
assert val("M-201", "exact_over_naive_at_T_eq_4Ne") == 0.200941
U_E = 4.1e-4                                                          # M-007 (Day's 3.0 s4.3)

# ---- s1.1 lottery ---------------------------------------------------------------------------
p = 1e-8
n50 = math.log(0.5) / math.log1p(-p)
near(n50, 69_314_717.7, 0.1)
assert math.ceil(n50) == 69_314_718                                   # post prints 69,314,717
P = lambda n: 1 - math.exp(n * math.log1p(-p))
near(P(2e8), 0.8647, 1e-4); near(P(4e8), 0.9817, 1e-4)              # "0.86", "0.98"
near(P(7e7), 0.5034, 1e-4)                                            # printed 0.51
n51 = math.log(0.49) / math.log1p(-p)
near(n51, 71.33e6, 0.01e6)
assert 1 / p == 1e8

# ---- s2.1 ---------------------------------------------------------------------------
assert 1 / (2 * 1_000) == 0.0005

# ---- s2.2: R1 of PS-01 ---------------------------------------------------------------------------
L, MU = 3.2e9, (1.1e-8, 1.2e-8, 1.5e-8)
near(75 / L, 2.34375e-8, 1e-15)
hap = [L * m for m in MU]
near(hap[0], 35.2, 1e-9); near(hap[1], 38.4, 1e-9); near(hap[2], 48.0, 1e-9)
both = [2 * h * T for h in hap]
near(both[0], 17_740_800, 1e-3); near(both[1], 19_353_600, 1e-3); near(both[2], 24_192_000, 1e-3)
move = [round(b / 37.8e6 - 1, 4) for b in both]
assert move == [-0.5307, -0.488, -0.36], move
assert 18.9e6 / 37.8e6 - 1 == -0.5
mu_25 = 0.75 * 75 / L                                                 # per-site rate at which the move is exactly -25%
near(mu_25, 1.7578e-8, 1e-12)
assert all(abs(m) > 0.25 for m in move)
lo, hi = 0.01 * 3.1e9, 0.02 * 3.1e9
assert (lo, hi) == (31e6, 62e6)
below = {"19.35M": round(1 - both[1] / lo, 4), "18.9M": round(1 - 18.9e6 / lo, 4), "24.19M": round(1 - both[2] / lo, 4)}
assert below == {"19.35M": 0.3757, "18.9M": 0.3903, "24.19M": 0.2196}, below
four_ne_yoo = [4 * 132_000, 4 * 198_000]
assert four_ne_yoo == [528_000, 792_000]
near(528_000 / T, 2.095, 1e-3); near(792_000 / T, 3.143, 1e-3)

# ---- s3.1 ---------------------------------------------------------------------------
near(1 / 60, 0.0167, 1e-4); assert 9 / 60 == 0.15; near(10 / 60, 0.1667, 1e-4); near(60 * 0.167, 10.02, 1e-9)
assert 410e6 / 2 == 205e6
near(410e6 / 3e9, 0.137, 1e-3)


# ---- s3.3: Kimura's conditional fixation-time distribution ------------------------------------------------------
def F(x, n=50):
    """P(T_fix <= x Ne | fixation), new mutation, the post's series with n terms."""
    return 1 + sum((-1) ** i * (2 * i + 1) * math.exp(-i * (i + 1) * x / 4) for i in range(1, n + 1))


def F_safe(x):
    if x < 0.1:                                                       # series needs many terms here; F is ~0 anyway
        return 0.0
    return F(x, 400)


assert 0 <= F(0.1, 400) < 1e-6


def q(target):
    a, b = 0.5, 40.0
    for _ in range(100):
        m = (a + b) / 2
        a, b = (m, b) if F(m) < target else (a, m)
    return a


near(q(0.5), 3.4788, 1e-4)                                           # "3.48Ne ≈ 34,790"
near(F(4), 0.6063, 1e-4)                                              # "60.6%"
near(q(0.95), 8.1878, 1e-4); near(q(0.99), 11.4075, 1e-4); near(q(0.999), 16.0127, 1e-4)
near(1 - 3 * math.exp(-4 / 2), 0.5940, 1e-4)
near(1 - 3 * math.exp(-8.19 / 2), 0.9500, 1e-4); near(F(8.19), 0.9501, 1e-4)
mean_series = sum((-1) ** (i + 1) * (2 * i + 1) / (i * (i + 1)) for i in range(1, 2_000_001))
near(mean_series, 1.0, 1e-6)                                          # mean = 4Ne x 1

# ---- s3.4: empty-start delivered share and the theta gloss ------------------------------------------------------
def delivered(Ne, steps=20_000):
    x = T / Ne
    return sum(F_safe((k + 0.5) / steps * x) for k in range(steps)) / steps


share = {int(Ne): round(delivered(Ne), 4) for Ne in (10_000, 132_000, 198_000)}
assert share == {10_000: 0.8413, 132_000: 0.019, 198_000: 0.0017}, share
near(1 - 40_000 / T, 0.8413, 1e-4)                                    # M-201 asymptote at Ne 10,000
Ne = 10_000
H = sum(1 / i for i in range(1, 2 * Ne))
near(2 * H, 20.96, 0.01)
assert (2 * Ne) * (2 * Ne) == 4 * Ne ** 2 != 4 * Ne

# ---- s3.5 ---------------------------------------------------------------------------
near(20_000 / 45, 444.4, 0.05); near(13_500 / 593, 22.77, 0.005)
near(1 / 444, 0.002252, 1e-6); assert 1 / 444 < 0.0023
near((1 / 444) / U_E, 5.49, 0.005)
near(1e-9 * 4.6e6, 0.0046, 1e-12); near(1e-8 * 3.2e9, 32, 1e-9)
near(1 / 75, 0.01333, 1e-5); near(25 * 0.013, 0.325, 1e-12)
near(12.6e6 / 0.33, 38_181_818, 1); near(12.6e6 / 0.33 / 37.8e6 - 1, 0.0101, 1e-4)
near(12.6e6 / (25 / 75), 37.8e6, 1e-6)


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
    "object": "M-917",
    "variant_of": "M-212",
    "inputs": [
        {"name": "lottery_p", "value": p, "cite": "ps1@s1.1"},
        {"name": "mu_G", "value": 75, "cite": "ps1@s2.2 (PS-01), per haploid genome by the s2.1 definition"},
        {"name": "generations", "value": T, "cite": "ps1@s2.2 (6.3e6 / 25, Duffy's values; M-002)"},
        {"name": "snv_band", "value": [0.01, 0.02, 3.1e9], "cite": "ps1@s2.2 (31-62M; 3.1e9 base implied)"},
        {"name": "mu_per_site_pedigree", "value": list(MU),
         "cite": "parameters.yaml mutation.mu_per_site_per_gen.pedigree_human (Kong2012; range)"},
        {"name": "Ne_values", "value": [1_000, 10_000, 132_000, 198_000],
         "cite": "ps1@s2.1, ps1@s3.2 (Duffy's 10,000), ps1@s2.2 (Yoo quote)"},
        {"name": "toy_alignment", "value": {"length": 60, "snv": 1, "gap_bp": 9}, "cite": "ps1@s3.1"},
        {"name": "ltee_counts", "value": {"20K": 45, "26.5K": 60, "40K": 653}, "cite": "ps1@s3.5 (as quoted from the paper)"},
        {"name": "genome_bounds", "value": {"ecoli": [1e-9, 4.6e6], "human": [1e-8, 3.2e9]}, "cite": "ps1@s3.5"},
        {"name": "U_E", "value": U_E, "cite": "M-007 (Day's 3.0 s4.3)"},
    ],
    "values": {
        "lottery": {"n50": 69_314_717.7, "n50_bound": 69_314_718, "P_2e8": 0.8647, "P_4e8": 0.9817,
                    "P_any_7e7": 0.5034, "printed": 0.51, "tickets_for_0.51": 71.33e6, "mean": 1e8},
        "p_fix_Ne_1000": 0.0005,
        "r1_ps01": {"mu_per_site_implied": 2.34375e-8, "haploid": [35.2, 38.4, 48.0],
                    "both_lineages": [17_740_800, 19_353_600, 24_192_000], "move_vs_37.8M": move,
                    "zygote_reading_move": -0.5, "mu_at_move_minus_25pct": 1.7578e-8,
                    "snv_band": [31e6, 62e6], "below_31M": below},
        "yoo_4Ne": {"132000": 528_000, "198000": 792_000, "over_window": [2.095, 3.143]},
        "toy": {"snv": 0.0167, "gap": 0.15, "sum": 0.1667, "bp_at_0.167": 10.02, "half_410M": 205e6,
                "410M_over_3e9": 0.137},
        "fixation_time": {"median_Ne": 3.4788, "F_4Ne": 0.6063, "q95_Ne": 8.1878, "q99_Ne": 11.4075,
                          "q999_Ne": 16.0127, "first_term_4Ne": 0.5940, "first_term_8.19Ne": 0.9500,
                          "mean_over_4Ne": 1.0},
        "empty_start_share_T252000": share,
        "theta_gloss": {"mean_sojourn_new_mutation_Ne1e4": 20.96, "post_says": 2 * Ne},
        "ltee": {"G_f_20K_clone": 444.4, "G_f_mutator_clone": 22.77, "mu_G_ecoli": 0.002252,
                 "over_U_E": 5.49, "ecoli_bound": 0.0046, "human_floor": 32},
        "s3_5_chain": {"G_f_human": 0.01333, "25x0.013": 0.325, "printed_quotient": 38_181_818,
                       "printed_over_37.8M": 0.0101, "exact": 37.8e6},
    },
    "positions": {
        "day": {"reading": "MITTENS is a throughput count with 205M required; the neutral answer rests on its inputs",
                "holds": "PS-01's 75 per haploid genome is 2x the library's pedigree count (38.4), so PS-02's 37.8M falls "
                         "36-53% to 17.7-24.2M and the 'close to 31-62M' match needs the ancestral term the post does not "
                         "use; at the ancestral Ne the post quotes (132,000-198,000) an empty start delivers 0.17-1.9% of "
                         "mu T; 444 compares a clone count with a fixation rate; the sharpshooter point does not touch a "
                         "count of any 205M fixations"},
        "critic": {"reading": "neutral fixations proceed in parallel at k = mu, and 205M counts bases, not events",
                   "holds": "the k = mu algebra, the fixation-time quantiles (median 3.48Ne, F(4Ne) = 0.606, matching "
                            "Day's own Hard Limits fill of 0.61) and the toy base-against-event count reproduce; Day's "
                            "own '1,000,000 years per neutral fixation' is the serial reading the post answers; "
                            "point-mutator LTEE lines fix faster than 1,400"},
    },
    "notes": "Topic fetched read-only 2026-11-26 (Discourse JSON, t-18094.json sha256 82e89a07...; 8 posts). Post 1 is "
             "at version 11, updated 2026-10-07T22:58Z; the bib row's copy (9912398e...) is not on disk, so the versions "
             "cannot be diffed; PS-01..PS-05 are exact substrings of the fetched text. Duffy's video is not held: his "
             "lines are relays (rule U), scored against Day only where Day's own text says the same (Q14, Q15, Q91, "
             "mc1c#337074301).",
})

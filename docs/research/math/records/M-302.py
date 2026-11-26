#!/usr/bin/env python3
"""M-302 record: expected neutral substitutions in a ~7,000-year window, genome against panel.

Object: docs/research/math/objects.yaml M-302 (formula, derivation). Three genome-wide counts are in
the corpus: Day's required rate 20e6 / 9e6 y x 7,000 y = 15,556 (Q275, blog "approximately 15,500"),
Day's clock count mu x 1.5e8 sites x 350 = 630 (C6 q2, q4) and the audit's mu x 3.1e9 x 350 = 13,020
(claim file C1). The observed counts are on a panel: 0 (blog, 1,211,499 SNPs), 1 and 3 (Zenodo,
1,143,671 SNPs; claim file C) and 21 (C6, 1,233,013-SNP panel). The record checks each count, the
uniform panel scalings (630 -> 5.2 on the C6 panel; 15,556 -> 5.7 and 13,020 -> 4.8 on the C panel),
the claim file C correction of the 5.7 (swept site on the panel in 8.8-24.7% of completions: 1,376 to
3,836) and the side-by-side comparison with the observed counts. Inputs carry their quote id or claim
file; held() checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-302.py [--write]
Without --write it checks that M-302.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
QD = "docs/research/sources/quotes-day.md"
CL = "docs/research/claims/"
C, C1, C6 = CL + "C-adna-zero-fixations.md", CL + "C1-1240k-ascertainment.md", CL + "C6-molecular-clock-stopped.md"


def held(rel, quote):
    """The quote, checked verbatim (whitespace-normalised) against a held file."""
    norm = lambda s: " ".join(s.split())
    assert norm(quote) in norm((ROOT / rel).read_text(encoding="utf-8")), (rel, quote[:60])
    return quote


def near(x, target, tol):
    assert abs(x - target) <= tol, (x, target, tol)
    return x


def g(x):
    return float(f"{x:.6g}")


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


# ---- inputs -------------------------------------------------------------------------------
Q275 = held(QD, "The Modern Synthesis requires approximately 20 million fixations over the 9 million years since the "
                "human-chimpanzee divergence, implying a rate of 2.22 fixations per year or approximately 15,500 "
                "fixations per 7,000-year period.")
Q55 = held(C, "The observed fixation count was zero. Not a single allele in 1.2 million crossed from rare (<10% "
              "frequency) to fixed (>90% frequency) in seven thousand years.")
CQ2 = held(C, "of 1,143,671 autosomal SNPs analyzed, one changed from above 10% starting frequency to fixation or loss. "
              "In the replication (AADR v66.p1, analyzed September 29, 2026), three did.")
CQ4 = held(C, "predicts that fixation events should be rare, fewer than 20 across the entire genome.")
BLOG_N = held(C, "| SNPs analysed | 1,211,499 | 1,143,671 | 1,143,230 |")
GENS = held(C, "derived: 350 x 0.45 = 157.5, matching the blog's \"approximately 158 real generations\" (holds).")
C6Q2 = held(C6, "The molecular clock predicts approximately 630 fixations per 350 generations (based on k = μ for neutral "
                "sites; see Appendix A).")
C6Q4 = held(C6, "E[total fixations] = 1.8 × 350 ≈ 630")
C6SITES = held(C6, "For 150 million neutral sites: E[fixations per generation] = 1.2 × 10⁻⁸ × 1.5 × 10⁸ = 1.8")
C6OBS = held(C6, "Post-7000 BP total 21.")
C6PANEL = held(C6, "Scaled to the panel, 630 x 1,233,013/150,000,000 = 5.2 (derived).")
C1G = held(C1, "x 3.1e9 sites = 37.2 per generation x 350 = 13,020 (haploid-lineage count; Day's 15,556 is the same "
               "order). Panel fraction = 1,143,671 / 3.1e9 = 3.7e-4, so a uniform sample would give 4.8 events")
C57 = held(C, "Scaling the 15,556 by that fraction gives 5.7 expected panel-site events (derived)")
CCORR = held(C, "In the L5 model the swept standing-variant site is on the panel in 8.8% to 24.7% of completions (hard "
                "mode at s <= 0.01: 0.5% to 6.5%), so at 15,556 completions 1,376 to 3,836 swept sites sit on the panel "
                "(hard mode at s <= 0.01: 76 to 1,010), about two orders more than 5.7.")

mu = 1.2e-8                       # parameters mutation.mu_per_site_per_gen.pedigree_human (C6 q4)
gens = 350                        # 7,000 y at 20 y/gen (claim file C, Formal statement)
assert 7_000 / 20 == gens
genome, neutral = 3.1e9, 1.5e8    # C1 derived (not a parameters.yaml key); C6 Appendix A
panels = {"blog_v62": 1_211_499, "zenodo_v62": 1_143_671, "c6_1240k": 1_233_013}
observed = {"blog_lt10_to_gt90": 0, "zenodo_v62_50_90": 1, "zenodo_v66_50_90": 3, "c6_post7000": 21}
near(gens * 0.45, 157.5, 1e-9)    # parameters selection.turnover_d; "approximately 158 real generations"

# ---- genome-wide counts -------------------------------------------------------------------
req_rate = 20e6 / 9e6
near(req_rate, 2.22, 0.005)                             # Q275 "2.22 fixations per year"
required = req_rate * 7_000
near(required, 15_556, 0.5)                             # Q275 "approximately 15,500"
near(mu * neutral, 1.8, 1e-12)                          # C6 Appendix A
clock = mu * neutral * gens
near(clock, 630, 1e-9)                                  # C6 q2, q4
whole = mu * genome * gens
near(mu * genome, 37.2, 1e-9)
near(whole, 13_020, 1e-6)                               # C1 derived
near(required / whole, 1.195, 0.001)                    # "the same order"

# ---- panel fraction and uniform scaling ---------------------------------------------------
frac_c = panels["zenodo_v62"] / genome
near(frac_c, 3.689e-4, 1e-7)                            # "3.7e-4"
s_req = required * frac_c
near(s_req, 5.74, 0.005)                                # claim file C "5.7" (the audit's own figure, corrected)
s_whole = whole * frac_c
near(s_whole, 4.80, 0.005)                              # C1 "4.8"
s_clock = clock * panels["c6_1240k"] / neutral
near(s_clock, 5.18, 0.005)                              # C6 "5.2"
s_clock_c = clock * panels["zenodo_v62"] / neutral      # the same scaling on the Zenodo panel
near(s_clock_c, 4.80, 0.005)

# ---- the C6 comparison: 630 against 21 flips once the denominator matches ------------------
near(clock / observed["c6_post7000"], 30.0, 1e-9)       # Day's "30x" (C6 Appendix A: 630/21)
near(observed["c6_post7000"] / s_clock, 4.05, 0.01)     # on the panel, 21 is 4x above the scaled clock
assert observed["c6_post7000"] > s_clock

# ---- the claim file C correction of the 5.7 (R4 L5 swept-site share) ------------------------
for printed, pct in ((1_376, 8.8), (3_836, 24.7), (76, 0.5), (1_010, 6.5)):
    near(100 * printed / required, pct, 0.05)           # the printed counts are 15,556 x the printed share
near(1_376 / s_req, 240, 1)                             # "about two orders more than 5.7"
near(3_836 / s_req, 668, 1)

finish({
    "object": "M-302",
    "inputs": [
        {"name": "required count", "value": "20e6 fixations / 9e6 y x 7,000 y", "cite": "Q275 (C q4 context)"},
        {"name": "clock count", "value": {"mu": mu, "neutral_sites": neutral, "generations": gens},
         "cite": "C6 q2, q4 (Z18525185 s5.3, Appendix A); parameters mutation.mu_per_site_per_gen.pedigree_human"},
        {"name": "whole-genome count", "value": {"genome_sites": genome}, "cite": "claim file C1 derived (3.1e9 not a parameters.yaml key)"},
        {"name": "panel sizes", "value": panels, "cite": "claim file C table (Q55 blog, Q52 Z23046531); C6 (Mallick 2024)"},
        {"name": "observed counts", "value": observed, "cite": "Q55, Q52 (C q1, q2); C6 Formal statement"},
        {"name": "swept-site share on the panel", "value": {"soft": [8.8, 24.7], "hard_s_le_0.01": [0.5, 6.5]},
         "cite": "claim file C correction (R4 L5, S-L5-1)"},
    ],
    "values": {
        "genome_wide": {"required_Q275": g(required), "clock_C6": g(clock), "whole_genome_C1": g(whole)},
        "panel_fraction_zenodo": g(frac_c),
        "uniform_panel_scaling": {"required_on_C_panel": g(s_req), "whole_on_C_panel": g(s_whole),
                                  "clock_on_C6_panel": g(s_clock), "clock_on_C_panel": g(s_clock_c)},
        "c6_ratio_printed_630_over_21": 30.0,
        "c6_observed_over_scaled_clock": g(observed["c6_post7000"] / s_clock),
        "swept_sites_on_panel_at_15556": {"soft": [1_376, 3_836], "hard_s_le_0.01": [76, 1_010]},
    },
    "positions": {
        "day": {"reading": "genome-wide counts against the panel counts",
                "required": g(required), "clock": g(clock), "observed": observed,
                "ratio_630_over_21": 30.0},
        "critic": {"reading": "scale the count to the panel before comparing",
                   "clock_on_panel": g(s_clock), "observed_21_over_expected": g(observed["c6_post7000"] / s_clock),
                   "note": "uniform scaling assumes panel sites register new substitutions; claim file C's correction "
                           "puts the swept site on the panel in 8.8-24.7% of completions (1,376-3,836 at 15,556). "
                           "Which share applies is M-301 (simulation), not this record"},
    },
    "notes": "All genome-wide counts reproduce (15,556; 630; 13,020). Against the panel the denominator decides: 630 "
             "scales to 5.2 on the 1,233,013-SNP panel, so 21 observed is 4x above, not 30x below; 15,556 and 13,020 "
             "scale uniformly to 5.7 and 4.8 on the 1,143,671-SNP panel, a scaling claim file C itself corrects to "
             "1,376-3,836 panel-registered completions. The uniform figures are a lower bound on what the panel can see "
             "for selected completions, not the expectation.",
})

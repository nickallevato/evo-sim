"""B3m: recompute Day's "median factor of 25 across 55 vertebrates" from Bergeron et al. 2023 (Nature 615:285).

Tier: LOW-STAKES (fidelity re-computation of a cited number; one combined review).  Trivial arithmetic on a
68-row table; runs locally in < 2 s.  Pre-registered: this docstring is committed before the first run.

TARGET: B3d ("median 25" sub-statement; R4-B3 P6 withdrawn, fidelity and external `pending`), B3 umbrella.
VERBATIM QUOTES
  Q69   Day, blog 2026-05-07 "A Retraction and a Revision", para 5: "The textbook k = μ identity is still
        falsified — both directly (pedigree μ and phylogenetic k disagree by a median factor of 25 across 55
        vertebrates)"
  Q161  same post, para 3: "The new validation work which uses Bergeron et al. (2023) on pedigree mutation rates
        and fossil-calibrated substitution rates for 55 vertebrate species"
  Bergeron 2023, Methods (phylogeny): "We then created a 75% completion matrix, that is, each alignment contains
        at least 75% of the taxa (55 species)"
  Bergeron 2023, Results: "We found a significant positive correlation between µyearly_modelled and the UCE
        substitution rate ... Fig. 2 ... The grey dashed lines indicate equality."
INPUTS (untrusted downloads, read only, never executed)
  argv[1]  Supplementary Tables xlsx (41586_2023_5752_MOESM5_ESM.xlsx; sources/raw/b3m-bergeron-2026-10-10/,
           sha256 5bb7ed86...75b56).  Sheet "Supplementary Table 9": columns 'UCE substitution rate',
           'MultiZ substitution rate', 'Average yearly mutation rate (m_yearly)', 'Modeled rate per generation',
           'Modeled rate per year (m_yearly_modeled)', 'Generation time (years)', 'Taxonomic group'.
  argv[2]  tree_rooted.nwk (IQ-TREE UCE tree, substitutions/site; github lucieabergeron/vertebrate_rate,
           sources/raw/b3m-bergeron-github-2026-10-10/, tarball sha256 fb30af08...08d35).
  The substitution-rate columns come from ape::chronos(lambda = 0, relaxed) on that tree with calibrations in
  Ma (time_tree.r: `attr(chr, "rate")` per terminal edge), so the native unit is read as substitutions/site/Myr.
DISCLOSED BEFORE PRE-REGISTRATION: while listing sheet headers I saw the first data row of Table 9 (red panda:
  UCE 0.0398, MultiZ 0.0477, m_yearly_modeled 1.79e-9, generation time 6) and the Methods phrase "(55 species)".
  On the per-Myr reading red panda's UCE k/mu_yearly is about 22.  No other row was seen.

BASES computed (every species with both values; also excluding the domesticated species Bergeron exclude, if a
  column marks them; otherwise the list below):
  B1  k_UCE (col x 1e-6 per year) / mu_yearly_modeled          [matched: per year, model-based mu]
  B2  k_UCE / mu_yearly (observed average)                     [matched per year]
  B3  k_WGA (MultiZ col x 1e-6) / mu_yearly_modeled
  B4  per generation: k_UCE x 1e-6 x gen_time / mu_generation_modeled  (= B1 if mu_gen_mod = mu_yr_mod x gen)
  B5  mismatch bases, reported for completeness: col x 1e-6 vs mu per generation (yearly-vs-generational
      mismatch), and the inverses mu/k of B1-B4.
  U   unit sanity: root-to-tip IQ-TREE distance of each tip / 416 Myr (the root calibration) gives a crude
      per-Myr average; if the table's column is ~10x or more above it, the per-Myr reading of the column is
      suspect and B1-B4 inherit that uncertainty (reported, not resolved here).
  Counts: species with UCE rate; with MultiZ rate; with both rates and mu; minus domesticated; per group.

PREDICTIONS (fixed before the run)
  Day side (D1) the median ratio on some stated matched basis (B1-B4) lies in [20, 30] (magnitude, either
           direction), and the comparison set has 55 species.
  Critic side (steelman-critic #6 in REVIEW-R4-B3) (C1) any gap of order 25 comes from site class
           (UCE + flank = constrained -> k < mu) or a yearly-vs-generational mismatch, i.e. direction k < mu.
  This audit (the red-panda row was seen, so these are informed):
    A1  On B1 the median k/mu is > 1 (k ABOVE mu), in [10, 40]; i.e. the direction is opposite to critic C1's
        purifying-selection explanation.  Probability ~0.7.
    A2  B3 (WGA) also > 1; median in [5, 40].
    A3  U: the crude root-to-tip per-Myr rate is ~10x or more below the table's UCE column median (the column
        is not a plain per-Myr rate, or chronos with lambda = 0 inflated terminal-edge rates); if so the "factor
        25" is a unit/estimator artefact of chronos terminal rates, not a k-vs-mu gap.  Probability ~0.6.
    A4  Count: 55 does NOT equal the number of species with both values (expected 60-68); the 55 matches the
        Methods phrase "(55 species)" (75% completion threshold).  Probability ~0.6.
    A5  Bergeron's own reading (equality line in Fig. 2) would only hold if the plotted axes are rescaled; we
        record what scale makes the median ratio 1 (reported, not scored).
  Fidelity scoring (rule S/C/F): `accurate` if a matched basis in the published data gives a median in
  [20, 30] over 55 species; `partial` if the median is near 25 but the species count or basis differs, or it
  rests on a unit reading the source does not state; `misread` if no basis gives ~25 or Bergeron's own text
  states the opposite reading (equality).  External: an unresolved unit question leaves external `contested`.
"""
import math
import re
import statistics as st
import sys

import openpyxl

DOMESTIC_HINTS = ("familiaris", "hircus", "taurus", "aries", "catus", "scrofa", "pacos", "gallus", "domestic",
                  "Equus caballus", "Oryctolagus", "Mus musculus", "Rattus")


def table9(path):
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    ws = wb["Supplementary Table 9"]
    rows = list(ws.iter_rows(values_only=True))
    hdr = [str(c) if c is not None else "" for c in rows[1]]
    out = []
    for r in rows[2:]:
        if r[0] is None:
            continue
        out.append({h: v for h, v in zip(hdr, r)})
    return hdr, out


def col(hdr, start):
    for h in hdr:
        if h.startswith(start):
            return h
    raise KeyError(start)


def num(v):
    try:
        x = float(v)
        return x if math.isfinite(x) and x > 0 else None
    except (TypeError, ValueError):
        return None


def root_to_tip(nwk):
    s = open(nwk).read().strip().rstrip(";")
    depth, stack, tips, i = 0.0, [], {}, 0
    # iterative parse: track cumulative depth per open clade
    cur = [0.0]
    pending = []  # (name, start depth list index)
    token = ""
    lens = {}
    # simple recursive-descent parser
    pos = 0

    def parse(pos, base):
        nonlocal tips
        if s[pos] == "(":
            pos += 1
            children = []
            while True:
                pos, info = parse(pos, None)
                children.append(info)
                if s[pos] == ",":
                    pos += 1
                    continue
                if s[pos] == ")":
                    pos += 1
                    break
            m = re.match(r"[^:,();]*(?::([-0-9.eE]+))?", s[pos:])
            pos += m.end()
            bl = float(m.group(1)) if m.group(1) else 0.0
            return pos, ("node", children, bl)
        m = re.match(r"([^:,();]+)(?::([-0-9.eE]+))?", s[pos:])
        pos += m.end()
        return pos, ("tip", m.group(1), float(m.group(2)) if m.group(2) else 0.0)

    _, tree = parse(0, None)

    def walk(n, d):
        if n[0] == "tip":
            tips[n[1]] = d + n[2]
        else:
            for c in n[1]:
                walk(c, d + n[2])
    walk(tree, 0.0)
    return tips


def med(xs):
    return st.median(xs) if xs else float("nan")


def main(xlsx, nwk):
    hdr, rows = table9(xlsx)
    c_uce, c_wga = col(hdr, "UCE substitution"), col(hdr, "MultiZ substitution")
    c_my, c_mym = col(hdr, "Average yearly mutation"), col(hdr, "Modeled rate per year (m_yearly_modeled)")
    c_mg, c_gt, c_grp = col(hdr, "Modeled rate per generation (m_generatio"), col(hdr, "Generation time"), \
        col(hdr, "Taxonomic group")
    print(f"Table 9 rows: {len(rows)}")
    for name, c in (("UCE", c_uce), ("MultiZ", c_wga), ("mu_yearly", c_my), ("mu_yearly_mod", c_mym),
                    ("mu_gen_mod", c_mg), ("gen_time", c_gt)):
        print(f"  non-missing {name}: {sum(num(r[c]) is not None for r in rows)}")
    dom = lambda r: any(h in str(r[hdr[0]]).replace("_", " ") or h in str(r[hdr[0]]) for h in DOMESTIC_HINTS)
    sets = {"all": rows, "non-domestic": [r for r in rows if not dom(r)]}
    print("  domestic-flagged: " + ", ".join(str(r[hdr[0]]) for r in rows if dom(r)))
    for sname, rs in sets.items():
        print(f"\n## set {sname}")
        bases = {
            "B1 kUCE/mu_yr_mod": [(r, num(r[c_uce]) * 1e-6 / num(r[c_mym])) for r in rs if num(r[c_uce]) and num(r[c_mym])],
            "B2 kUCE/mu_yr_obs": [(r, num(r[c_uce]) * 1e-6 / num(r[c_my])) for r in rs if num(r[c_uce]) and num(r[c_my])],
            "B3 kWGA/mu_yr_mod": [(r, num(r[c_wga]) * 1e-6 / num(r[c_mym])) for r in rs if num(r[c_wga]) and num(r[c_mym])],
            "B4 kUCE*gt/mu_gen_mod": [(r, num(r[c_uce]) * 1e-6 * num(r[c_gt]) / num(r[c_mg])) for r in rs
                                      if num(r[c_uce]) and num(r[c_gt]) and num(r[c_mg])],
            "B5a kUCE(yr)/mu_gen_mod": [(r, num(r[c_uce]) * 1e-6 / num(r[c_mg])) for r in rs if num(r[c_uce]) and num(r[c_mg])],
            "B5b kWGA(yr)/mu_gen_mod": [(r, num(r[c_wga]) * 1e-6 / num(r[c_mg])) for r in rs if num(r[c_wga]) and num(r[c_mg])],
        }
        print("| basis | n | median k/mu | median mu/k | q25-q75 k/mu | median |log10| | by group (median k/mu, n) |")
        print("|---|---|---|---|---|---|---|")
        for b, v in bases.items():
            xs = sorted(x for _, x in v)
            if not xs:
                continue
            q = st.quantiles(xs, n=4) if len(xs) > 2 else [float("nan")] * 3
            grp = {}
            for r, x in v:
                grp.setdefault(r[c_grp], []).append(x)
            g = "; ".join(f"{k} {med(sorted(x)):.3g} ({len(x)})" for k, x in sorted(grp.items()))
            print(f"| {b} | {len(xs)} | {med(xs):.3g} | {1 / med(xs):.3g} | {q[0]:.3g}-{q[2]:.3g} | "
                  f"{med(sorted(abs(math.log10(x)) for x in xs)):.3g} | {g} |")
    # U: unit sanity from the uncalibrated IQ-TREE tree
    tips = root_to_tip(nwk)
    rt = sorted(tips.values())
    print(f"\n## U: IQ-TREE root-to-tip (subs/site): n {len(rt)}, median {med(rt):.3g}, range {rt[0]:.3g}-{rt[-1]:.3g}")
    crude = med(rt) / 416.0
    uce = sorted(num(r[c_uce]) for r in rows if num(r[c_uce]))
    print(f"crude per-Myr rate (median root-to-tip / 416 Myr): {crude:.3g}; table UCE column median {med(uce):.3g}; "
          f"ratio column/crude {med(uce) / crude:.3g}")
    mym = sorted(num(r[c_mym]) for r in rows if num(r[c_mym]))
    print(f"crude per-year k / median mu_yearly_mod: {crude * 1e-6 / med(mym):.3g} "
          f"(A5: scale making the B1 median 1 = 1e-6 / median B1 ratio, see table)")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

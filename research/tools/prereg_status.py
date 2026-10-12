"""prereg_status.py: descriptive pre-registration metadata per check (METHOD-AUDIT MA-04).

Reads git history only (no check is re-run, no write-up is altered) and prints
research/checks/PREREG-STATUS.md to stdout.

    research/.venv/bin/python -I research/tools/prereg_status.py > research/checks/PREREG-STATUS.md

For each check in CHECKS:
  reg  = the commit that first adds the main script (`git log --diff-filter=A`).
  res  = the earliest commit that adds either the write-up or a raw output of the check
         (`.host`, `.pid` and `.time` files are launch records, not results, and are skipped).
         Where a check has neither (round-1 checks), the commit that first adds its RESULTS.md heading.
  gap  = committer time of res minus committer time of reg, in seconds.
  push = the first entry in the LOCAL reflog of origin/research that contains reg, if it is earlier than res.
         The reflog is local to the owner's clone; it is evidence of a push, not an outside timestamp.

Labels (definitions in the generated file).  The HAND dict holds the two labels git cannot give
(disclosed foreknowledge, nothing at stake), each with the text it rests on.
"""
import subprocess
import sys

R = "research/checks/"
RAW = R + "results/raw/"
SKIP_EXT = (".host", ".pid", ".time")

# id, tier, main script, write-up (or None), raw-output pathspecs, RESULTS.md heading fragment for the fallback
CHECKS = [
    ("B0", "pre-tier", "baseline_textbook.py", None, ["baseline_textbook*"], "## B0 "),
    ("B0.4", "pre-tier", "beneficial_fix_time.py", None, ["beneficial_fix_time*"], "## B0.4"),
    ("B1", "pre-tier", "b1_start_state.py", None, ["b1_start_state*"], "## B1 "),
    ("B3 (N vs Ne)", "pre-tier", "b3_N_vs_Ne.py", None, ["b3_N_vs_Ne*"], "## B3 "),
    ("B2a", "pre-tier", "b2a_hard_limits_chain.py", None, ["b2a*"], "## B2a"),
    ("F1", "pre-tier", "f1_throughput.py", None, ["f1_throughput*"], "## F1 "),
    ("B1b", "pre-tier", "b1b_demography.py", None, ["b1b*"], "## B1b"),
    ("B1c", "pre-tier", "b1c_ne_history.py", "R4-B1c-B4a.md", ["b1c*"], None),
    ("B4a", "pre-tier", "b4a_two_lineage_ils.py", "R4-B1c-B4a.md", ["b4a*"], None),
    ("B3b / B3c", "pre-tier", "b3b_overlap_fluctuation.py", "R4-B3b-C1.md", ["b3b*"], None),
    ("C1", "pre-tier", "c1_ascertainment_sim.py", "R4-B3b-C1.md", ["c1.*", "c1_run*"], None),
    ("C1b", "pre-tier", "c1b_day_binned_statistic.py", "R4-C1b.md", ["c1b*"], None),
    ("H", "pre-tier", "h_cost_of_selection.py", "R4-H-C2.md", ["h_*"], None),
    ("H2-hard", "pre-tier", "h2_hard_selection_multilocus.py", "R4-H2-hard.md", ["h2*"], None),
    ("C2", "pre-tier", "c2_overlap_vs_standard.py", "R4-H-C2.md", ["c2*"], None),
    ("F2 / A-sim", "pre-tier", "f2_multilocus.py", "R4-F2-A.md", ["f2*"], None),
    ("E", "pre-tier", "e_founder_hazard.py", "R4-E.md", ["e_founder*", "e4*"], None),
    ("G1", "pre-tier", "g1_specific_vs_any.py", "R4-G1.md", ["g1_*"], None),
    ("GAP-04/07/02", "pre-tier", "gap04_weissman_barton.py", "R4-GAPS-04-07-02.md", ["gap04*", "gap07_*", "gap02*"], None),
    ("H3", "pre-tier", "h3_human_scale.py", "R4-H3-human.md", ["h3*"], None),
    ("GAP-07b", "pre-tier", "gap07b_alignment_count.py", "R4-GAP07b-alignment.md", ["gap07b*"], None),
    ("C1c", "pre-tier", "c1c_call_depth_replacement.py", "R4-C1c.md", ["c1c*"], None),
    ("C1d", "pre-tier", "c1d_aadr_real.py", "R4-C1d.md", ["c1d*"], None),
    ("D1", "pre-tier", "d1_sequence_space_spike.py", "R4-D1-spike.md", ["d1_*"], None),
    ("X1", "pre-tier", "x1_critic_arithmetic.py", "R4-X1-critic-arithmetic.md", ["x1*"], None),
    ("GAP-07c", "pre-tier", "gap07c_polymorphic_share.py", "R4-GAP07c.md", ["gap07c*"], None),
    ("P1", "low", "p1_symbolic_proofs.py", "R4-P1.md", ["p1*"], None),
    ("B5b", "low", "b5b_mansfield_supply.py", "R4-B5b.md", ["b5b*"], None),
    ("F1b", "low", "f1b_in_transit_measured.py", "R4-F1b.md", ["f1b*"], None),
    ("C1e", "low", "c1e_holocene_trajectories.py", "R4-C1e.md", ["c1e*"], None),
    ("G2c / B6c", "low", "g2c_standing_variation.py", "R4-G2c.md", ["g2c*"], None),
    ("E5 / E6", "low", "e5e6_ltee_counts.py", "R4-E5E6.md", ["e5e6*"], None),
    ("F1a", "low", "f1a_serial_vs_parallel.py", "R4-F1a.md", ["f1a*"], None),
    ("B2b", "low", "b2b_ceiling_vk.py", "R4-B2b.md", ["b2b*"], None),
    ("XT", "low", "xt_cross_tool.py", "R4-XT.md", ["xt*"], None),
    ("D15", "load-bearing", "d15_waiting_time.py", "R4-D15.md", ["d15*"], None),
    ("H8 / H5", "load-bearing", "h8_haldane_regime.py", "R4-H8.md", ["h8*"], None),
    ("A2e", "load-bearing", "a2e_ltee_transfer.py", "R4-A2e.md", ["a2e_main*", "a2e_calib*", "a2e_human*"], None),
    ("B3 family", "load-bearing", "b3_family_reconstruction.py", "R4-B3.md", ["b3_family*"], None),
    ("B2 / B", "load-bearing", "b2_hard_limits_internal.py", "R4-B2.md", ["b2_hard*", "b2.*", "b2_internal*"], None),
    ("B3g", "low", "b3g_concession_bookkeeping.py", "R4-B3g.md", ["b3g*"], None),
    ("F3a", "low", "f3a_zeng_s_small_checks.py", "R4-F3a.md", ["f3a*"], None),
    ("B3m", "low", "b3m_bergeron_median.py", "R4-B3m.md", ["b3m*"], None),
    ("FM", "load-bearing", "fm_mesa_replication.py", "R4-FM.md", ["fm_*", "fm.*"], None),
    ("GAP-06", "low", "gap06_yoo_mu_g.py", "R4-GAP06.md", ["gap06*"], None),
    ("GAP-07t", "low", "gap07t2t_event_counts.py", "R4-GAP07t.md", ["gap07t*"], None),
    ("A2e-alpha", "load-bearing", "a2e_alpha_map.py", "R4-A2e-alpha.md", ["a2e_alpha.*", "a2e_alpha_map*"], None),
    ("HF-d (GAP-05 part of HF)", "load-bearing", "hf_followups.py", "R4-HF.md", ["hf_gap05*"], None),
    ("HF main (HF-a, HF-b)", "load-bearing", "hf_followups.py", None, ["hf_main*", "hf_analyse*"], None),
    ("L1", "load-bearing", "l1_dnds_genesets.py", "R4-L1.md", ["l1_*", "l1.*"], None),
    ("L6", "low", "l6_ltee_undone.py", "R4-L6.md", ["l6*"], None),
    ("L7", "low", "l7_410m_accounting.py", "R4-L7.md", ["l7*"], None),
    ("B9", "low", "b9_relaxed_load.py", "R4-B9.md", ["b9*"], None),
    ("RHclose", "low", "rhclose.py", "R4-RHclose.md", ["rhclose.*", "rhclose_main*"], None),
    ("A2e-alpha addendum (Uricchio)", "low", "a2e_alpha_uricchio.py", None, ["a2e_alpha_uricchio*"], None),
    ("RHclose-critics", "low", "rhclose_critics.py", "R4-RHclose-critics.md", ["rhclose_critics*"], None),
    ("GAP05", "low", "gap05_slightly_deleterious.py", "R4-GAP05.md", ["gap05_slightly*", "gap05.*", "gap05_main*"], None),
    ("L1b", "load-bearing", "l1b_t2t_dnds.py", None, ["l1b*"], None),
    ("L5", "low (registered as three)", "l5_adna_power.py", None, ["l5*"], None),
    ("L1c", "load-bearing", "l1c_alignment_method.py", None, ["l1c_alignment*", "l1c.*", "l1c_main*"], None),
    ("FMnull", "load-bearing", "fm_mesa_null.py", None, ["fm_mesa_null*", "fmnull*"], None),
]

# Labels git cannot give.  Each entry: label, evidence (file and words).
HAND = {
    "B0": ("reproduction", "textbook baselines; no side's prediction at stake"),
    "P1": ("reproduction", "machine-checked identities; docstring l.21 calls B0.2 and B2a \"known results\""),
    "XT": ("reproduction", "cross-tool replication of earlier checks in fwdpy11"),
    "B3g": ("reproduction", "docstring l.4: \"moves no verdict by computation: it verifies quotes, reproduces the arithmetic\""),
    "B9": ("criterion-only", "docstring l.6-9: \"DISCLOSURE ... The numbers below are known in advance\""),
    "RHclose": ("criterion-only", "docstring l.9-13: numbers \"ALREADY KNOWN from R4-B2\"; \"not blind predictions\""),
    "RHclose-critics": ("criterion-only", "docstring l.17: \"DISCLOSURE (mandatory).  NOT BLIND.\""),
    "GAP05": ("criterion-only", "docstring l.6-7: predictions \"NOT blind to the DFE\""),
    "A2e-alpha addendum (Uricchio)": ("criterion-only", "docstring l.3: \"POST HOC LABEL: the abstract value ... was already known\""),
    "L7": ("criterion-only", "R4-L7.md l.14: sheet 14 and 19 values \"were seen while deriving the readings\" (R1 partly informed)"),
}
# Partial disclosures that do not change the label; printed in the notes column.
NOTES = {
    "D15": "docstring l.20-22: analytic baselines were run before registration (\"baseline reproductions, not predictions\"); the simulation sweep was not",
    "D1": "docstring l.51, l.105: bands literature-informed, \"not blind\"; GB1 score quantiles seen before registration",
    "B3m": "docstring l.28, l.48: one row (red panda) seen; audit-side predictions \"informed\"",
    "F1b": "commit message: smoke run \"saw 2 reps per cell\"; RESULTS.md: \"cell A not fully blind\"",
    "GAP-07t": "docstring l.8: FM's DHC SNV totals were seen (disclosed)",
    "FMnull": "docstring A10: P4 and P5 \"informed, not predictive\"",
    "HF-d (GAP-05 part of HF)": "the fast part of HF, run and written up 632 s after registration; the main sweep is the next row",
    "L5": "review tier cut from three to one after registration (QUEUE.md)",
}


def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True, check=True).stdout


def first_add(pathspecs):
    """Earliest commit (history order) adding a file matching any pathspec; returns (hash, ct, file) or None."""
    out = git("log", "--reverse", "--diff-filter=A", "--format=@%H %ct", "--name-only", "--", *pathspecs)
    cur = None
    for line in out.splitlines():
        if line.startswith("@"):
            cur = line[1:].split()
        elif line.strip() and cur and not line.endswith(SKIP_EXT):
            return cur[0], int(cur[1]), line.strip()
    return None


def heading_commit(fragment):
    out = git("log", "--reverse", "--format=%H %ct", "-S" + fragment, "--", R + "RESULTS.md").splitlines()
    if not out:
        return None
    h, ct = out[0].split()
    return h, int(ct), "RESULTS.md heading"


def reflog():
    rows = []
    for line in git("reflog", "show", "origin/research", "--format=%H %gd", "--date=unix").splitlines():
        h, sel = line.split()
        rows.append((int(sel.split("{")[1].rstrip("}")), h))
    return sorted(rows)


def is_anc(a, b):
    return subprocess.run(["git", "merge-base", "--is-ancestor", a, b]).returncode == 0


def main():
    pushes = reflog()
    rows, counts = [], {}
    for cid, tier, script, writeup, rawspecs, frag in CHECKS:
        reg = first_add([R + script])
        specs = [RAW + s for s in rawspecs] + ([R + "results/" + writeup] if writeup else [])
        res = first_add(specs)
        wu = first_add([R + "results/" + writeup]) if writeup else None
        if frag:
            hc = heading_commit(frag)
            if hc and (res is None or hc[1] < res[1]):
                res = hc
        push = None
        for t, h in pushes:
            if t >= reg[1] and is_anc(reg[0], h):
                push = t
                break
        note = NOTES.get(cid, "")
        if res is None:
            label, gap = "registered, not run", None
        else:
            gap = res[1] - reg[1]
            pushed_first = push is not None and push < res[1]
            if reg[0] == res[0]:
                label = "single-commit"
            elif cid in HAND:
                label = HAND[cid][0]
            elif pushed_first:
                label = "blind"
            else:
                label = "unknown"
        if cid in HAND and label == HAND[cid][0]:
            note = (HAND[cid][1] + ("; " + note if note else ""))
        elif cid in HAND:
            note = ("would be " + HAND[cid][0] + " on content: " + HAND[cid][1] + ("; " + note if note else ""))
        counts[label] = counts.get(label, 0) + 1
        rows.append((cid, tier, script, reg, res, wu, gap, push, label, note))

    w = sys.stdout.write
    w(HEADER)
    w("| Label | Checks |\n|---|---|\n")
    for k in ("blind", "criterion-only", "reproduction", "single-commit", "unknown", "registered, not run"):
        w(f"| {k} | {counts.get(k, 0)} |\n")
    w(f"| **total** | **{sum(counts.values())}** |\n\n")
    w("## Table\n\n")
    w("`reg` = commit adding the main script. `res` = first commit adding a raw output or the write-up. "
      "`gap` = res minus reg, committer time. `push lead` = seconds by which the first recorded push containing `reg` "
      "precedes `res` (blank = no push recorded in between). `write-up` = first commit adding the `R4-*.md` file.\n\n")
    w("| Check | Tier | Main script | reg | res | gap (s) | push lead (s) | write-up | Label | Evidence and notes |\n")
    w("|---|---|---|---|---|---|---|---|---|---|\n")
    for cid, tier, script, reg, res, wu, gap, push, label, note in rows:
        lead = ""
        if res and push is not None and push < res[1]:
            lead = str(res[1] - push)
        w(f"| {cid} | {tier} | `{script}` | `{reg[0][:7]}` | {('`' + res[0][:7] + '`') if res else ''} | "
          f"{'' if gap is None else gap} | {lead} | {('`' + wu[0][:7] + '`') if wu else ''} | {label} | {note} |\n")
    w(FOOTER)


HEADER = """# Pre-registration status of each check

*Generated by `research/tools/prereg_status.py` from `git log` and the local reflog of `origin/research`. Descriptive metadata only: no check was re-run and no write-up was changed. Background: finding MA-04 in [`docs/research/METHOD-AUDIT-2026-10-12.md`](../../docs/research/METHOD-AUDIT-2026-10-12.md).*

## What the labels mean

The audit (MA-04, remedy 1) asks for three labels in place of the single word "pre-registered". Two more are needed for checks whose order git cannot show.

| Label | Definition used here | What it supports |
|---|---|---|
| **blind** | The registration commit was pushed to `origin/research` before the first commit that contains a result, and neither the script nor the write-up discloses that the scored numbers were already known. | The criterion and the predictions were fixed, on a remote, before the result was committed. |
| **criterion-only** | Registration and result are separate commits, and the script or write-up itself says the numbers were known when the criterion was written. | The criterion was fixed before scoring. The predictions are not tests. |
| **reproduction** | Registration and result are separate commits, and the check re-derives or replicates a known result with no side's prediction at stake. | Nothing about prediction. It is a correctness check. |
| **single-commit** | Script and results entered git in the same commit. | Nothing about order. "Prediction order not verifiable from history." |
| **unknown** | Separate commits, registration first, but no push is recorded between them and no disclosure either way. | The commit order is as claimed. Nothing outside the author's working tree separates the two. |
| **registered, not run** | Script committed; no result in git yet. | To be labelled when the run is collected. |

Limits of this table, all of which apply to every row:

1. **Commit order is not working order.** A commit records when a file entered history, not when it was written or run. A `blind` row shows that the registration reached the remote before the result was *committed*; it does not show that no run happened before the push. A short gap does not show that results preceded registration either: an agent that writes the docstring, runs, writes up and then commits in two steps produces the same history (audit MA-04, "not established").
2. **The reflog is local.** Push times come from the reflog of the owner's clone. They are evidence that a push happened, not a third-party timestamp. No signed tag or timestamp proof exists for any check.
3. **`criterion-only` and `reproduction` are read from the texts.** The words each rests on are quoted in the last column. A check with no such words is not thereby shown to be blind; where the push test also fails it is `unknown`.
4. **One row per registered main script.** Post hoc scripts (each labelled post hoc in its own commit) and the twelve mapping claims (review #50, no script) are not listed. Post hoc entries in `RESULTS.md` (G2c A_long, H8 kscale64) fall under their parent check.

## Counts

"""

FOOTER = """
## Reading the table

- **Round 1 and round 2** (`3d888e9`, `36a7ff9`, `a89d06c`, `9a2148b`) are `single-commit`: scripts, outputs and, for round 2, reviews and verdict merges arrived together. Round 2 has partial cover from the claim files' prediction sections (`ad44c23`), which precede `a89d06c`; round 1 precedes the claim files.
- **Gaps under five minutes with no push in between** are `unknown` unless a disclosure makes them `criterion-only` or `reproduction`. For a sub-minute deterministic script the registration binds the criterion at most.
- **`blind` rows with a short push lead** deserve the same caution as `unknown` rows: the push shows the registration left the workstation, not that the run had not happened.
- **Partial disclosures do not change a label** but are quoted in the last column. Two `blind` rows carry one: D1 (bands literature-informed, in its own words "not blind"; one data summary seen) and D15 (analytic baselines run before registration; the simulation sweep was not). A stricter reading puts D1 under `criterion-only`, giving blind 9 and criterion-only 7.
- Tier is the review tier in `REVIEW.md` (`pre-tier` = before tiering began at review #14).

To regenerate: `research/.venv/bin/python -I research/tools/prereg_status.py > research/checks/PREREG-STATUS.md`.
"""

if __name__ == "__main__":
    main()

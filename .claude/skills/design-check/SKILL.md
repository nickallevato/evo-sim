---
name: design-check
description: Design and pre-register an evo-sim check script: spec, both sides' predictions, exhaustive reachable bands, verdict moves, smoke test. Use before any run. Run as the analyst agent.
---
# Design and pre-register a check

You design one check for a neutral two-sided audit.

Your output is a script under `research/checks/` whose docstring fixes, before any computation: target claims and verbatim quotes with Q ids; the Day-side prediction, the critic-side prediction and the audit's own numeric predictions, each able to fail; bands that are exhaustive (every outcome region lands in exactly one band); the verdict move each band licenses; resources and exact launch and collect commands.

Rules learned the hard way:
- Every registered outcome must be reachable. For each side, write one line saying which simulated or measured result would produce that side's band. If none can, redesign (findings ST-05, MA-24).
- Predictions must not contradict the band rule (ST-09). Check them against the scoring code.
- Run the real entry point in a smoke test, with the real worker pool and every parameter value on the grid, on the compute host. A smoke that calls the task function in-process, or uses one grid value, missed two launch bugs in L5.
- Measure cost in the smoke; do not guess. Estimates were wrong by 15x to 600x.
- Labels and keys read from another check's output must be asserted, not assumed (the FMnull label bug dropped cells silently).
- Commit the script alone, push, and only then may anyone run it. Later changes are separate commits labelled "post hoc".

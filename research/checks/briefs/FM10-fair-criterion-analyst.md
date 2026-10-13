# Brief FM10-fair-criterion (analyst): take up proposal (l) under the rule freeze

Lead: Big Sim. Written 2026-10-13, before the task was created (MA-21).
Skill to load: `.claude/skills/design-check/SKILL.md` for the design and pre-registration;
the run, the write-up and the reviews are later tasks in the same lifecycle.
Authority: owner decision **D-25** of 2026-10-13, verbatim: "Yes. Use the fairer rule".

## Goal

Proposal (l) of `docs/research/criticality/METHOD-AUDIT-2026-10-13.md` section 7b — a
Day-side criterion for FM10 that a mechanism of the size Day asserts could actually meet —
is authorised. Carry it out under the freeze procedure the owner accepted as O-6, in this
order and no other:

1. **Cooling-off.** Nothing is pre-registered or run before **2026-10-14 21:22 UTC**
   (24 hours from the decision). If you are awake before that, stop and say so.
2. **Source the missing input first.** The proposal needs a neutral lineage-specific range
   with a sourced upper end; there is none on record. Without it, criterion 3's DAY clause
   cannot be evaluated. Find it in the literature with a verbatim quote and a locator, as
   a fidelity-ledger row. If no sourced upper end exists, **stop and report** — do not
   invent a bound, and do not fall back to the old criterion silently.
3. **Pre-register** the criterion as section 7b states it, in the script docstring, with
   the interval method fixed in advance:
   - the alternative stated at two sizes, the size Day asserts and one tenth of it;
   - an interval for the one-lineage **excess** variance (excess over the Poisson floor,
     not the value), on both references, human- and chimp-referenced, by R4-FM's mirror
     construction;
   - DAY if the interval excludes the whole neutral lineage-specific range; CRITIC if the
     interval's upper end is 3x below the stated alternative; otherwise undecided,
     reported with the interval;
   - before the run, for each planted model, whether it would score DAY (the reachability
     line the severe-testing pass asked for).
4. **Run** on na-workhorse (never on this workstation), then write up
   `research/checks/results/R4-FM10-fair.md`.

## Limitations you must state in the write-up

- **The data have been seen.** This is a re-score of a question already run under a
  different criterion, by a project that knows the first answer. That weakens it and the
  write-up says so in its own section, not in a footnote.
- Day has stated no size for the alternative; the sizes used are the audit's construction
  from Q169 (b), and under rule S a gloss is not his statement. Say which is which.

## Review tier

**Three reviews** (correctness, steelman-day, steelman-critic). FM10 external and ROOT-FM
external are both `load_bearing: true`, and this is a criterion change, so the tier is not
in doubt. Under the cap of one agent (D-22) the three run one after another.

## What this does not touch

**FM10 internal stays `pending`** under D-09 (owner, 2026-10-10: pending until Day
releases his method). D-25 is about the external field and FM3's annotation only. Do not
move internal for any reason.

## Constraints

- One agent at a time (D-22). No second agent, no parallel review.
- No outward action of any kind (hard rule 6): no contact, no posting, no Wayback, no
  paywall bypass. Sourcing the range means the literature the project can already reach.
- Commit the script before the run; never commit or push from a compute host.

## Report (≤ 300 words)

Commits; whether the cooling-off had elapsed; the sourced range with its locator or the
fact that none was found; the pre-registered criterion; the reachability table; and what
the result would move if the reviews hold.

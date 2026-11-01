---
name: deref-source
description: De-reference one source (post, paper, video window, or a set of claim files) into the math map: verbatim located statements -> argument steps -> math objects (docs/research/math/). Maps only; computes nothing beyond checking quoted arithmetic.
---
# De-reference a source into the math map

Read `docs/research/math/README.md` for the schema. Read `docs/research/math/objects.yaml` so that you reuse existing objects. Your brief names the source and the output paths.

1. **Statements.** Every row carries a verbatim quote, plus its Q id where one exists (grep `docs/research/sources/quotes-*.md`). Read the source whole; excerpts are not enough. List each argumentative statement in the source window, with an exact verbatim quote (copy-paste; it must grep-match the held text), the speaker, and a locator (timestamp, page or line). Tag each one `dialectic` or `rhetoric` (rule RH in AGENTS.md).
2. **Steps.** Break each dialectic statement into argument steps: its premises (stated or needed), its inference and its conclusion. Write the hidden premise when the argument needs one, and label it `implicit`.
3. **Objects.** Land each step on a math object: reuse an existing `M-` id or an existing hierarchy node's maths (grep `docs/research/claims/` and `parameters.yaml`); create a new object only if none fits. Fill `positions` for both sides, even when one side is silent ("not addressed").
4. **Arithmetic.** Write the speaker's formula out in full (every factor, e.g. x2 for two lineages) before recomputing; a flag that drops a factor is worse than no flag. Recompute any number the speaker states, using only their inputs. Record whether it reproduces. Do not judge the verdict; flag `candidate:` issues (wrong inputs, double counting, unit slips) with one line of reasoning each.
5. **Resolution.** `resolved` means the maths question itself is settled by a named results file, even if the claim's verdict stays contested for other reasons. If any live objection disputes the maths, it is `open`. Give each object a resolution type. For `simulation` or `regression`, give a rough compute estimate and mark `measured: false`.
6. **Output.** Every source map uses this exact table header, claim backfills included: `| Locator | Speaker | Quote | RH | Steps | Objects | Existing node | Arithmetic |`. Speaker is a `docs/research/math/people.yaml` alias; write a relay as `X (relaying Y)`. If only an input differs from an existing object, add a new object with `variant_of`. The source map `sources/<source-id>.md` (table: locator | speaker | quote | RH tag | steps | object ids | existing node | arithmetic) and new or changed objects in the YAML path your brief gives. No other files.

**Merge (backfills over many files):** after mapping, make one pass that merges objects asking the same maths question; target fewer than 0.7 objects per claim. Where two maps disagree on `status`, keep `open` and note both.

Do not: run checks, write verdicts, edit claim files, fetch anything, or read big files whole (grep by id).

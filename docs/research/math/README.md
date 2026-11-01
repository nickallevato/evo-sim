# Math map: from words to the maths underneath

The audit's work is finite: every argument, from Day, the critics or allies, written or spoken, reduces to a small set of **math objects**. Many claims point at the same object. Settle the objects and the claims inherit the result. This folder holds that map. It **maps** the work; it does not do it.

```
source (post, paper, video, book)  ->  statements (verbatim, located)
  -> argument steps (premise / inference / conclusion)   [logical regression]
  -> math objects M-NNN                                   [objects.yaml]
  -> resolution: derivation | lookup | simulation | regression | data-check | rhetoric
  -> compute manifest (simulation / regression objects only, with CPU estimates)
```

## Files
| File | What |
|---|---|
| `objects.yaml` | One entry per distinct math object (schema below). The single list of what must be settled. |
| `sources/<source-id>.md` | The **source map** for one source: a table of each statement, its steps, and the object ids it lands on. |
| `people.yaml` | Speaker registry (alias -> person, side). `research/tools/people_pages.py` writes `docs/people/` from the source maps. |
| `pilot/` | Test runs of the `deref-source` skill and their scoring. |
| `research/tools/math_map.py` | Read-only: lint the map, and print what is left (open objects by resolution, CPU-hours by host). |

## Object schema (`objects.yaml`)
```yaml
- id: M-001
  kind: identity | formula | parameter | model-choice | inference | empirical
  statement: "F_max = t_div * d / (g_len * G_f)"       # the maths, one line
  variables: [divergence.t_div_years, ...]              # parameters.yaml keys where they exist
  used_by: [A, A4, F1a]                                 # hierarchy node ids that rest on it
  sources: ["Q123", "vid02@00:38:18"]                   # quote ids or source-map locators
  positions:                                            # one line per side, both always filled
    day: "..."
    critic: "..."
  resolution: derivation | lookup | simulation | regression | data-check | rhetoric
  status: open | resolved | blocked
  resolved_by: "results/R4-A4.md"                       # when resolved
  blocked_on: ""                                        # owner | outside: what exactly
  compute: {host: na-workhorse, est_cpu_h: 0, est_ram_gb: 0, measured: false}   # simulation/regression only
  variant_of: M-025                                     # optional: same maths as M-025, a different input (e.g. d = 0.8 vs 0.45)
```
Kinds: **identity** (arithmetic that is true or not), **formula** (a model equation with parameters), **parameter** (a sourced number), **model-choice** (which model applies, e.g. d vs N_e), **inference** (a reasoning step, e.g. rate vs latency), **empirical** (a claim about data).

Rules: two claims that need the same maths share one object (dedup is the point). A new source adds an object only if no existing object fits. Rhetoric (rule RH) is mapped with `resolution: rhetoric` and never enters the manifest.

## Records: the maths as reusable code (owner, D-38)
Every object that is settled by computation gets a **record** that later work cites instead of recomputing:
- `docs/research/math/records/M-NNN.py`: self-contained (stdlib or the pinned venv), its inputs stated with their `parameters.yaml` keys or quote ids, and `assert`s for every number it claims. It runs in seconds locally or prints the command for the host.
- `docs/research/math/records/M-NNN.json`: its saved output (values, inputs, script sha256, date).
- In `objects.yaml`: `status: resolved`, `resolved_by: docs/research/math/records/M-NNN.json`. A full R4 check stays the record for simulations; its object points at the R4 file.

`research/tools/math_map.py --lint` checks that every `resolved_by` file exists.

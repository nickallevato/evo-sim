# Mapping proposals for the exit criterion "every critic and ally argument is mapped"

*Draft 2026-10-09. Proposals only: nothing in this file has been applied to `defeaters.yaml`, `hierarchy.yaml`, `standard-forms.md`, `lineage.yaml`, `NOTES.md`, `quotes-critics.md` or any existing claim file. The only files created are this one and 12 new claim files (listed in section 4). Every YAML block below was validated on a scratch copy of the repository (lint and `argmap_check.py`): pasting the blocks and flipping the edges in section 4 raised no new error (the scratch copy lacked `sources/raw/`, so its 6 quote-lookup errors are baseline).*

## 0. How to use this file

- **Ids.** `dNEW-01` to `dNEW-29` are placeholders. At writing time `defeaters.yaml` ended at d300 (others had added d279 and above while I worked); rename to the next free ids at integration and fix the `counter` cross-references that name a `dNEW` id (only dNEW-21 does). Counters in the blocks are computed as "every row whose target is this row's attacker", against the file as of 2026-10-09.
- **New claim files carry `edges: []`.** `argmap_check.py` requires a defeater for every hierarchy `attacks` edge, and `lint_research.py --write-hierarchy` copies claim edges into `hierarchy.yaml`. To keep other integrations from failing, the proposed edge sits in a comment on each file's `edges:` line. Flip it when the rows are pasted (table in section 4.3).
- **Order of integration.** (1) paste rows (section 3), mini-forms (3.2) and the registry row (3.3); (2) flip the edges (4.3); (3) run lint with `--write-hierarchy`, then `argmap_check.py`; (4) optional lineage (3.4), quotes (4.4), NOTES wording (5).
- **Quote ids.** `GG-17` onward in 4.4 are proposed; renumber if taken.
- **Local resources.** Everything here was done with single light Python processes; no simulation was run.

## 1. Counts

| | count |
|---|---|
| Critic + ally nodes still `extracted` (R5 draft, hierarchy as of the start of the task) | 41 (29 critic, 12 ally) |
| Same, recounted at the end (B2e, C5b, D1d were promoted to `reviewed` by the C1d integration meanwhile) | 38 (26 critic, 12 ally) |
| Critic/ally nodes with **no defeater row at all** (neither attacker nor target), any status | 15: A4c, B4e, B4f, D8, D14, D15, G1b, G1c, G2b, G2c, G3a, ROOT-DE, ROOT-H, ROOT-K, ROOT-T (14 extracted plus G2b, `checked`) |
| Extracted nodes that already have at least one row | 24 (table in section 2.2) |
| Of the 15 zero-row nodes: given proposed rows | 12 (A4c 2, B4e 1, B4f 1, D8 2, D14 1, D15 1, G2b 2, G3a 1, ROOT-H 2, ROOT-K 2, ROOT-T 1, G2c alias or 2 optional copies) |
| Of the 15: recorded as "no attack warranted" | 3 (G1b, G1c, ROOT-DE; section 2.1) |
| Video arguments with no claim file, now drafted | 10 critic claims + 2 Day-side claims (premises the critics answer, which exist in the corpus only as slide text read aloud) |
| Proposed defeater rows | 29 (27 firm + 2 optional G2c copies) |
| Proposed mini-forms | 14 (A4c, A4g, B4e, B4f, D2l, D8, D14, D15, G2b, G2c, G3a, ROOT-H, ROOT-K, ROOT-T) |
| Proposed registry ids | 1 (`x:eden-p9-caveat`) |
| New hierarchy `attacks` edges once flipped | 11 |
| Proposed lineage nodes | 5 |

After integration, the criterion-2 sentence in `R5-draft.md` could read: "Every critic and ally claim in `hierarchy.yaml` is attached (parent and edge) and appears in at least one defeater row, or is recorded as having no warranted attack (G1b, G1c, ROOT-DE); N critic and ally nodes remain `extracted` pending review, none unattached. Not mapped, because no model or number exists or the source is inaccessible: Hilbert, keruru's k = μ chain deposit, Dembski's attached PDF, paid sources, and the non-mathematical parts of the Hancock video (about 60 of 210 minutes of biography, politics and process, listed in 4.1 and 4.2)."

**Proposed definition of "mapped"** (for ratification at R5): a critic or ally claim is mapped when it has a parent and at least one edge in `hierarchy.yaml`, and at least one defeater row names it (as attacker or target), or the file records why no attack is warranted. "Reviewed" is a separate, later state. Under this definition the 24 extracted nodes with rows are already mapped; the remaining work on them is review, not mapping.

## 2. Inventory

### 2.1 The 15 nodes with no defeater row: proposed attachment

Parent and edge are the ones already in `hierarchy.yaml` unless stated; they are not changed. Row numbers refer to section 3.1.

| Node | Side | Parent / edge (existing) | Claim (verbatim anchor) | Proposed rows | Verdict basis |
|---|---|---|---|---|---|
| A4c | ally (Duffy) | A4, depends-on A4 | "the actual fixation time in a population where selection operates at 80% efficiency will take approximately 25 generations" (DU-01) | dNEW-05 (Hancock: standard models handle overlap); dNEW-06 (audit arithmetic: the slide reads "if Kimura's formula gives a fixation time of 20 generations ... 25", i.e. 20/0.8; this resolves the open units in `A4c` and is not d = 0.45, since 1/0.45 = 2.22) | pending; row 05 untested, 06 partly (arithmetic only) |
| B4e | critic (McCarthy) | B4, supports B4d | "population geneticists actually use Kimura's neutral-theory result to date the human–chimpanzee divergence" | dNEW-07 (Langergraber 2012: a date independent of fossil calibration). **Note:** B4e, B4f and B4g (keruru) all *support* Day's B4d from the other side. That convergence is recorded as a fact; the audit's view (B4d analysis) is that a pedigree-μ date still assumes k = μ per generation | partly (A1a fidelity partial, external supported; B4d analysis) |
| B4f | ally (Hössjer) | B4, supports B4d | "the neutral theory ... is used in the first place to date the assumed time of divergence" | dNEW-08 (same attacker) | partly |
| D8 | ally (Milton, via Day) | D, supports D | "the probability calculations for even a single protein forming by chance (1 in 10^65)" | dNEW-09 (Keefe & Szostak 2001), dNEW-10 (Taylor et al. 2001) | partly; both literature nodes have contested external verdicts |
| D14 | ally (Davis, relaying Eden) | D, supports D | "it would take about 10 to the 36th power of genetic transmissions to do that" | dNEW-11 (Eden's own caveat, new registry id `x:eden-p9-caveat`) | partly (D14: internal holds, fidelity accurate, external contested) |
| D15 | ally (Hössjer) | D, supports D | "far exceeds 9 million years" (HO-12) | dNEW-12 (F1c, new: the waiting-time literature, by analogy; Hancock's 2024 video does not mention Hössjer) | untested; no one in the corpus engages Hössjer's model |
| G1b | ally (Samson) | G1, supports G1 | "The total number of mutations separating species includes all of them. Parallel, sequential, or however else." | **none**: an accounting identity both sides accept (G1c, Camestros, concedes the same). The weakness noted in the claim file (an average required rate is not an upper bound on the achievable rate) is an A2e/A5 matter and is already carried by d003, d008. Proposed NOTES judgement call in section 5 | n/a |
| G1c | critic (Camestros) | G1, supports G1 | "He is correct that when he calculated the number it was an average." | **none**: a concession on definition (the same post says in CA-11 that an average is not the fastest rate; d003). Candidate for a lineage `concession` node, not proposed here | n/a |
| G2b | ally (Duffy) | A, supports A | "180 total fixed mutations is all there's time for using the fastest rate of mutational fixation ever observed in any organism" | dNEW-18 (Camestros: 1,400 is an average, upheld), dNEW-19 (Hancock: at least double, partly) | upheld / partly (A2d, A3d verdicts) |
| G2c | critic (Hancock) | G2, supports G2 | "there would basically be no genetic variation amongst individuals except for the mutation that's increasing in frequency" (GG-13) | **Duplicate of B6c** (same quote GG-13, same mini-form text; B6c already carries d048, d049, d150). Preferred: record G2c as an alias of B6c in NOTES. Option B if aliasing is refused: dNEW-21, dNEW-22 (copies of d049 and d150). Either way the *check* is still missing (G2c-sim, section 6) | partly (copies of d049, d150) |
| G3a | critic (Camestros) | G3, supports G3 | "the probability that SOME number is picked is close to 1" | dNEW-20 (Day's dilemma G3b, copy of the basis of d116) | partly |
| ROOT-DE | ally (Dembski) | ROOT, supports ROOT, depends-on B5 | "I have my own arguments for thinking that evolutionary mechanisms face serious explanatory shortfalls" | **none**: a position statement plus a question (DE-02) that Day answers (x:day-dembski-scaling, d129) | n/a (untestable) |
| ROOT-H | ally (Hössjer) | ROOT, supports ROOT, revises A5 | "I agree with this conclusion, also after adjusting the MITTENS equation for the different mutation rates of humans and E. coli" | dNEW-15 (Hössjer's own rescaled gap of 1.94× or 2.63× against his "agree"), dNEW-13 (Hancock/Gutsick Gibbon: credentials; untested) | partly; untested |
| ROOT-K | ally (Keen) | ROOT, supports ROOT | "The reason it fails ... is time" | dNEW-16 (A3x: the 205M behind the shortfall is a unit mismatch; upheld), dNEW-17 (A5: the ceiling premise) | upheld; partly |
| ROOT-T | ally (Tipler) | ROOT, supports ROOT | "the most rigorous mathematical challenge to Neo-Darwinian theory ever published" (secondhand) | dNEW-14 (ROOT-EP: credentials; untested) | untested |

Balance note: the rows I could not support from existing verdicts are marked `untested`, on both sides alike. The credential rows (13, 14) are weak by the project's own standard (FP-01: a headcount of degrees is not a rebuttal) and are included so the argument is mapped, not because it is endorsed.

### 2.2 The 24 extracted nodes that already have rows (snapshot of 2026-10-09)

Mapping is complete for these. "No inbound attack" means no row has the claim as its target, so the file records no attack on the claim; this is where the audit's coverage of the critic side is thinnest (section 6).

| Node | Side | Verdicts (int / fid / ext) | Out rows (status) | In rows (status) | Suggested next step |
|---|---|---|---|---|---|
| A2i | crit | holds / pending / pending | d266 partly | none | pending fidelity/external |
| A4b | crit | pending / partial / pending | d007 untested | none | pending internal/external; untested d007 |
| B3i | crit | holds / n/a / supported | d268 upheld | none | verdicts complete; no inbound attack (nobody has tested this claim): needs a Day-side or audit check before promotion |
| B4g | crit | pending / unverifiable / contested | none | d211 partly | pending internal |
| B5a | crit | holds / n/a / contested | d028 partly, d029 partly | d022 not_upheld, d142 partly, d217 partly | promotion candidate: complete verdicts and both-way rows |
| B5b | crit | holds / n/a / contested | d030 partly, d031 upheld | d143 not_upheld, d144 upheld | promotion candidate: complete verdicts and both-way rows |
| B5d | crit | holds / n/a / contested | d035 partly, d036 upheld | d145 not_upheld | promotion candidate: complete verdicts and both-way rows |
| B5f | crit | holds / n/a / contested | d039 partly, d040 upheld | d219 partly, d271 partly | promotion candidate: complete verdicts and both-way rows |
| B5g | crit | holds / accurate / contested | d041 upheld | none | verdicts complete; no inbound attack (nobody has tested this claim): needs a Day-side or audit check before promotion |
| B5h | ally | holds / accurate / contested | d043 upheld | none | verdicts complete; no inbound attack (nobody has tested this claim): needs a Day-side or audit check before promotion |
| B6c | crit | pending / n/a / pending | d048 partly, d049 partly | d150 partly | pending internal/external |
| C5 | crit | pending / pending / pending | d059 upheld | d053 not_upheld, d058 partly, d060 partly, d154 partly | pending internal/fidelity/external |
| D1 | crit | pending / unverifiable / contested | d064 untested | d063 partly, d067 untested, d073 untested, d077 not_upheld, d078 partly, d079 partly, d080 partly, d081 partly, d082 not_upheld, d085 not_upheld | pending internal; untested d064,d067,d073 |
| D13 | ally | pending / accurate / contested | d067 untested | none | pending internal; untested d067 |
| D1a | crit | pending / unverifiable / contested | d068 untested, d069 partly, d166 partly | d074 partly, d083 partly, d291 partly | pending internal; untested d068 |
| D1b | crit | pending / unverifiable / contested | d070 untested | d075 partly, d084 partly, d092 partly | pending internal; untested d070 |
| D1c | crit | pending / unverifiable / contested | d071 untested | none | pending internal; untested d071 |
| E5 | crit | pending / accurate / pending | d098 partly, d099 partly | d125 untested | pending internal/external; untested d125 |
| F1b | crit | holds / n/a / contested | d104 upheld, d133 partly | none | verdicts complete; no inbound attack (nobody has tested this claim): needs a Day-side or audit check before promotion |
| F4 | crit | holds / accurate / supported | d105 untested | d106 untested | untested d105,d106 |
| G2d | crit | holds / accurate / n/a | d111 partly | none | verdicts complete; no inbound attack (nobody has tested this claim): needs a Day-side or audit check before promotion |
| G2e | crit | holds / partial / contested | d112 upheld, d174 partly | none | verdicts complete; no inbound attack (nobody has tested this claim): needs a Day-side or audit check before promotion |
| G2f | crit | holds / n/a / contested | d113 partly | none | verdicts complete; no inbound attack (nobody has tested this claim): needs a Day-side or audit check before promotion |
| G5 | crit | holds / n/a / n/a | d269 upheld | none | verdicts complete; no inbound attack (nobody has tested this claim): needs a Day-side or audit check before promotion |

Reading the table: 4 nodes have all verdicts complete and a two-way row set (B5a, B5b, B5d, B5f) and are promotion candidates once a reviewer signs them. 8 more have complete verdicts but no inbound row (B3i, B5g, B5h, F1b, G2d, G2e, G2f, G5). The D1 family (D1, D1a, D1b, D1c, D13) carries 6 rows with status `untested` (d064, d067, d068, d070, d071, d073); D is the largest branch without a completed check.

## 3. Ready-to-paste blocks

### 3.1 Defeater rows (append to `defeaters.yaml`)

Schema as in the file (`quote` only where a verbatim quote of at most 30 words exists in a claim file). `hierarchy_edge: true` marks the row that represents a flipped `attacks` edge from section 4.3.

```yaml
- id: dNEW-01
  attacker: A4e
  target: A4g
  target_part: P1
  type: undermining
  by: [Zach Hancock]
  first_date: 2026-10-03
  locator: 'https://www.youtube.com/watch?v=_Vu0ZVVjwHc t=00:51:35–00:54:02 (claims/A4e)'
  audit_status: untested
  counter: []
  note: 'Kimura''s diffusion is a continuous-time smoothing of Wright–Fisher, not a revision of it, and the Moran model is the standard overlapping-generations model, so "the two standard models" misdescribes the theory.'
  hierarchy_edge: true
- id: dNEW-02
  attacker: A4e
  target: A4g
  target_part: P2
  type: undermining
  by: [Zach Hancock]
  first_date: 2026-10-03
  locator: 'https://www.youtube.com/watch?v=_Vu0ZVVjwHc t=00:48:29, t=01:00:59 (claims/A4e)'
  audit_status: partly
  audit_basis: 'R4 C2 (claims/A4 Check): g_eff = d*g is standard theory with generation length T/d, so the field carries the correction; whether Nₑ rescales the sweep time (not only drift) is untested'
  counter: []
  note: 'Effective population size absorbs overlap in Wright–Fisher formulas, so complete replacement is not an assumption of the standard results.'
  hierarchy_edge: false
- id: dNEW-03
  attacker: A4e
  target: A4
  target_part: inference
  type: undercutting
  by: [Zach Hancock]
  first_date: 2026-10-03
  locator: 'https://www.youtube.com/watch?v=_Vu0ZVVjwHc t=00:43:38–00:48:29 (claims/A4e)'
  audit_status: partly
  audit_basis: 'R4 C2: d*s exact for hazard-scale s, factor 1 for per-generation s (claims/A4 Check); Hancock addresses the Duffy/book version, MITTENS 3.0 dropped d (A4d)'
  counter: []
  note: 'Grants that overlap slows change per nominal generation; denies that a new coefficient is needed because Nₑ and the Moran model already carry it. Nₑ (drift) and d (selection time-scale) are different quantities; not shown interchangeable.'
  hierarchy_edge: false
- id: dNEW-04
  attacker: A4f
  target: A4
  target_part: P2
  type: undermining
  by: [Zach Hancock]
  first_date: 2026-10-03
  locator: 'https://www.youtube.com/watch?v=_Vu0ZVVjwHc t=01:20:50–01:23:35 (claims/A4f)'
  audit_status: partly
  audit_basis: 'A4 internal holds for hazard-scale s (R4 C2); the "d undefined" point was retracted by Camestros (A4b); Hancock critiques the concept as presented on Duffy''s slide'
  counter: []
  note: 'd has no population-genetic counterpart and, as defined (fraction replaced per time unit), is demographic turnover rather than a selection coefficient.'
  hierarchy_edge: true
- id: dNEW-05
  attacker: A4e
  target: A4c
  target_part: P1
  type: undermining
  by: [Zach Hancock]
  first_date: 2026-10-03
  locator: 'https://www.youtube.com/watch?v=_Vu0ZVVjwHc t=01:14:23–01:15:45 (claims/A4e)'
  audit_status: untested
  counter: []
  note: 'The 20-generation baseline "assuming complete replacement" is not what the standard models use for overlapping populations; Nₑ and the Moran model exist.'
  hierarchy_edge: false
- id: dNEW-06
  attacker: chk:R2-arith
  target: A4c
  target_part: inference
  type: undercutting
  by: [audit]
  first_date: 2026-10-09
  locator: 'https://www.youtube.com/watch?v=_Vu0ZVVjwHc t=01:14:23 and t=01:14:43 (Duffy''s slide as read by the host)'
  audit_status: partly
  audit_basis: 'arithmetic only: 20 generations / 0.8 = 25 reproduces the slide; 1/0.45 = 2.22 is not 1/0.8 = 1.25, so the example is not reconciled with d = 0.45 (it may be illustrative)'
  counter: []
  note: 'Resolves the units left open in claims/A4c (baseline 20 generations from Kimura''s formula, divided by 80% efficiency) and shows the example uses a different correction from d.'
  hierarchy_edge: false
- id: dNEW-07
  attacker: A1a
  target: B4e
  target_part: P1
  type: undermining
  by: [Langergraber et al. 2012 (applied by the audit)]
  first_date: 2012
  locator: 'claims/A1a (Langergraber 2012 abstract); claims/B4d analysis'
  audit_status: partly
  audit_basis: 'A1a fidelity partial, external supported; claims/B4d: a pedigree-μ date is independent of fossil calibration but still assumes k = μ per generation'
  counter: []
  note: 'Not every divergence date rests on Kimura''s result: Langergraber dates the split without fossil calibration, using pedigree μ and wild-chimp generation times.'
  hierarchy_edge: false
- id: dNEW-08
  attacker: A1a
  target: B4f
  target_part: P1
  type: undermining
  by: [Langergraber et al. 2012 (applied by the audit)]
  first_date: 2012
  locator: 'claims/A1a (Langergraber 2012 abstract); claims/B4d analysis'
  audit_status: partly
  audit_basis: 'as dNEW-07; Hössjer and McCarthy (B4e) make the same dependence point from opposite sides'
  counter: []
  note: 'Same as dNEW-07 against Hössjer''s statement that the neutral theory is used in the first place to date the divergence.'
  hierarchy_edge: false
- id: dNEW-09
  attacker: D12
  target: D8
  target_part: P1
  type: undermining
  by: [Keefe & Szostak 2001 (applied by the audit)]
  first_date: 2001
  locator: 'claims/D12 (Nature 410:715-718, abstract)'
  audit_status: partly
  audit_basis: 'D12 external contested (binding is not catalysis), fidelity unverifiable (abstract only); claims/D8 Responses'
  counter: []
  note: 'Four ATP-binding proteins were found in a library of 6×10^12 random 80-mers, so function is not at the 10^-65 scale; D8 states no length or function.'
  hierarchy_edge: false
- id: dNEW-10
  attacker: D11
  target: D8
  target_part: P1
  type: undermining
  by: [Taylor et al. 2001 (applied by the audit)]
  first_date: 2001
  locator: 'claims/D11 (PNAS 98:10596-10601)'
  audit_status: partly
  audit_basis: 'D11 internal holds, fidelity accurate, external contested (different protein and function)'
  counter: []
  note: 'Taylor et al. estimate a fully randomised library of about 10^24 members for chorismate mutases, far from 10^65.'
  hierarchy_edge: false
- id: dNEW-11
  attacker: x:eden-p9-caveat
  target: D14
  target_part: P1
  type: undermining
  by: [Murray Eden (applied by the audit)]
  first_date: 1966-04
  locator: 'Eden, Wistar Monograph No. 5, p.9 (claims/D14 Responses)'
  audit_status: partly
  audit_basis: 'D14 internal holds, fidelity accurate, external contested: Eden calls it a "very rough estimate" built on unsourced probabilities'
  counter: []
  note: 'Eden''s own caveat; Davis relays the 10^36 without it.'
  quote: 'a discovery of a new transposition mechanism can make such speculations an exercise in futility'
  hierarchy_edge: false
- id: dNEW-12
  attacker: F1c
  target: D15
  target_part: inference
  type: undercutting
  by: [Zach Hancock]
  first_date: 2024-03-06
  locator: 'https://www.youtube.com/watch?v=KLPZxAU9nAM t=00:00:20 (TH-1, claims/F1c)'
  audit_status: untested
  note: 'Waiting-time models of the Behe–Snoke family are argued to rely on unrealistic assumptions; the 2024 video does not mention Hössjer, Bechly and Gauger, so the transfer is by analogy.'
  counter: []
  hierarchy_edge: false
- id: dNEW-13
  attacker: ROOT-EP
  target: ROOT-H
  target_part: P4
  type: undermining
  by: [Zach Hancock, Gutsick Gibbon]
  first_date: 2026-10-03
  locator: 'https://www.youtube.com/watch?v=_Vu0ZVVjwHc t=03:04:26–03:05:30 (claims/ROOT-EP)'
  audit_status: untested
  counter: []
  note: 'An argument from credentials: a statistician''s agreement is not evidence about population-genetic assumptions. Hössjer''s byline is professor of mathematical statistics (HO-09); his population-genetics record was not examined; FP-01 notes a degree count is not a rebuttal.'
  hierarchy_edge: true
- id: dNEW-14
  attacker: ROOT-EP
  target: ROOT-T
  target_part: P2
  type: undermining
  by: [Zach Hancock, Gutsick Gibbon]
  first_date: 2026-10-03
  locator: 'https://www.youtube.com/watch?v=_Vu0ZVVjwHc t=00:30:54–00:32:16 and t=03:04:26 (claims/ROOT-EP)'
  audit_status: untested
  counter: []
  note: 'Tipler is a Discovery Institute associate with a physics background; the foreword and appendix are not accessible, so the rigor claim cannot be checked either way.'
  hierarchy_edge: true
- id: dNEW-15
  attacker: A5a
  target: ROOT-H
  target_part: inference
  type: undercutting
  by: [Ola Hössjer]
  first_date: 2026-09-14
  locator: 'Hössjer PDF p.3 (HO-02 against HO-06); claims/ROOT-H Weaknesses'
  audit_status: partly
  audit_basis: 'ROOT-H internal pending; balance ledger and NOTES item 2: his rescaled gaps are 1.94× (eq. 2.4) and 2.63× (eq. 3.1); without d, 22.9M (above 20M) and 16.9M (1.19× short); the cost step is asserted (H5)'
  counter: [d131, d185]
  note: 'His own rescaled bound is below the required count only by about 2×, so "I agree with this conclusion" rests on the uncomputed Haldane step.'
  hierarchy_edge: false
- id: dNEW-16
  attacker: A3x
  target: ROOT-K
  target_part: P1
  type: undermining
  by: [Dennis McCarthy, audit (R4 GAP-07b)]
  first_date: 2026-09-17
  locator: 'https://dennismccarthy.substack.com/p/vox-day-responds para 26 (MC-11)'
  audit_status: upheld
  audit_basis: 'as d006: A3x holds/accurate/supported; GAP-07 and GAP-07b: events per lineage 18–22.5M, so the 205M behind the 1,075,000× shortfall is a unit mismatch'
  counter: [d272]
  note: 'Keen''s 491 universe-ages is 6.3 My × the 205M-based shortfall; with an events count the multiplier falls by about 10×.'
  hierarchy_edge: false
- id: dNEW-17
  attacker: A5
  target: ROOT-K
  target_part: P2
  type: undermining
  by: [Dennis McCarthy]
  first_date: 2026-01-26
  locator: 'https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1 para 60-62 (MC-05, MC-07)'
  audit_status: partly
  audit_basis: 'A5 holds/n/a/contested; R4 A-sim: scaling factor 1.5–172× is an extrapolation; GAP-04 asymptotes'
  counter: [d016, d129]
  note: 'The shortfall is a time multiplier only if the bacterial per-fixation rate is a ceiling for humans, which per-genome supply differences contest.'
  hierarchy_edge: false
- id: dNEW-18
  attacker: A2d
  target: G2b
  target_part: P2
  type: undermining
  by: [Camestros Felapton]
  first_date: 2026-01-29
  locator: 'https://camestrosfelapton.wordpress.com/2026/01/29/reading-vox-day-so-you-dont-have-to-2026-5/ para 9 (CA-11)'
  audit_status: upheld
  audit_basis: 'A2d holds/accurate/supported; claims/G2b: LTEE point-mutator populations run faster (43–183 gens/fixation)'
  counter: [d127]
  note: '1,400 is an average, so it is not "the fastest rate of mutational fixation ever observed".'
  hierarchy_edge: false
- id: dNEW-19
  attacker: A3d
  target: G2b
  target_part: C
  type: rebutting
  by: [Zach Hancock]
  first_date: 2026-10-03
  locator: 'https://www.youtube.com/watch?v=_Vu0ZVVjwHc t=01:37:07 (GG-02)'
  audit_status: partly
  audit_basis: 'A3d holds/partial/n/a; claims/A3d: nobody disputes the factor of two in principle; MITTENS counts per lineage'
  counter: []
  note: 'Fixation occurs on both lineages, so the arithmetic is at least 360 rather than 180 on Hancock''s reading; the requirement is also per lineage in Day''s accounting.'
  hierarchy_edge: false
- id: dNEW-20
  attacker: G3b
  target: G3a
  target_part: P2
  type: undermining
  by: [Vox Day]
  first_date: 2026-10-01
  locator: 'https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/ ¶28'
  audit_status: partly
  audit_basis: 'as d116: R4 G1: G3b is an incomplete dilemma (internal non-sequitur), the neutral-is-not-functional half is valid; the middle case exists'
  counter: [d176, d241, d288]
  note: 'Disputes that the evolutionary outcome space resembles a lottery with many winning numbers.'
  hierarchy_edge: false
- id: dNEW-21
  attacker: G2c
  target: G2g
  target_part: inference
  type: undercutting
  by: [Zach Hancock]
  first_date: 2026-10-03
  locator: 'https://www.youtube.com/watch?v=_Vu0ZVVjwHc t=01:33:59 (GG-13)'
  audit_status: partly
  audit_basis: 'OPTIONAL (only if G2c is not recorded as an alias of B6c). Copy of d049: G2g internal non-sequitur; G2c prediction not computed; Day denies strict seriality (G1, Gc)'
  counter: [dNEW-22]
  note: 'Same argument as d049 (B6c → G2g), same quote GG-13.'
  hierarchy_edge: false
- id: dNEW-22
  attacker: F1a
  target: G2c
  target_part: inference
  type: undercutting
  by: [Vox Day]
  first_date: 2026-10-01
  locator: 'https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/ ¶17'
  audit_status: partly
  audit_basis: 'OPTIONAL (as dNEW-21). Copy of d150: G1 holds as accounting; F1a non-sequitur for latency uses'
  counter: [d174, d175, d201]
  note: 'G_f is throughput that already includes parallelism, so the serial-model prediction is not about MITTENS.'
  hierarchy_edge: false
- id: dNEW-23
  attacker: G2h
  target: A
  target_part: inference
  type: undercutting
  by: [Zach Hancock]
  first_date: 2026-10-03
  locator: 'https://www.youtube.com/watch?v=_Vu0ZVVjwHc t=01:36:03–01:36:24, t=01:41:38 (claims/G2h)'
  audit_status: untested
  counter: []
  note: 'F_max has no mutation-supply or selection term, so it cannot discriminate selection from drift; Day''s reply is that G_f is a measured total (G1).'
  hierarchy_edge: true
- id: dNEW-24
  attacker: H2a
  target: H
  target_part: P2
  type: undermining
  by: [Zach Hancock]
  first_date: 2026-10-03
  locator: 'https://www.youtube.com/watch?v=_Vu0ZVVjwHc t=02:06:13–02:13:12 (claims/H2a)'
  audit_status: partly
  audit_basis: 'R4 H, H2-hard and H3: the 10% is not a general bound; the cap is ln R / D under hard selection; the human-scale result is conditional on hard adaptive selection with a soft deleterious load; Nunney 2003 (H2)'
  counter: []
  note: 'The cost of selection exists only under hard (viability) selection; under soft selection or from standing variation it is largely absent.'
  hierarchy_edge: true
- id: dNEW-25
  attacker: B5j
  target: B
  target_part: inference
  type: undercutting
  by: [Zach Hancock]
  first_date: 2026-10-03
  locator: 'https://www.youtube.com/watch?v=_Vu0ZVVjwHc t=02:13:32–02:20:46 (claims/B5j)'
  audit_status: untested
  counter: []
  note: 'Whether neutral theory counts as "Darwinism" has no bearing on whether neutral fixation supplies the observed differences. Definitional; no numeric content.'
  hierarchy_edge: true
- id: dNEW-26
  attacker: ROOT-PG
  target: ROOT
  target_part: C
  type: rebutting
  by: [Zach Hancock, Gutsick Gibbon]
  first_date: 2026-10-03
  locator: 'https://www.youtube.com/watch?v=_Vu0ZVVjwHc t=00:22:54–00:27:44, t=02:24:30 (claims/ROOT-PG)'
  audit_status: untested
  counter: []
  note: 'Inductive: a theory with a record of confirmed quantitative predictions should not be overturned by a model with none. Day''s aDNA prediction (C) has been tested (R4 C1b: counts at or mildly above neutral expectation).'
  hierarchy_edge: true
- id: dNEW-27
  attacker: ROOT-COV
  target: ROOT
  target_part: inference
  type: undercutting
  by: [Zach Hancock]
  first_date: 2026-10-03
  locator: 'https://www.youtube.com/watch?v=_Vu0ZVVjwHc t=00:29:09–00:29:49 (claims/ROOT-COV)'
  audit_status: untested
  counter: []
  note: 'A covariance cannot be "statistically impossible"; a wording point that does not engage the time-budget calculation (Hancock concedes the live question at t=00:29:29).'
  hierarchy_edge: true
- id: dNEW-28
  attacker: D2k
  target: D2l
  target_part: P1
  type: undermining
  by: [Zach Hancock]
  first_date: 2026-10-03
  locator: 'https://www.youtube.com/watch?v=_Vu0ZVVjwHc t=00:13:19–00:19:47 (claims/D2k)'
  audit_status: untested
  counter: []
  note: 'Pearson, Fisher, Wright, Haldane and Kingman were mathematicians or statisticians; the narrow reading of D2l (nobody computed Day''s specific budget) is not touched.'
  hierarchy_edge: true
- id: dNEW-29
  attacker: F1c
  target: F
  target_part: inference
  type: undercutting
  by: [Zach Hancock]
  first_date: 2026-10-03
  locator: 'https://www.youtube.com/watch?v=_Vu0ZVVjwHc t=00:50:34–00:50:54 (claims/F1c)'
  audit_status: untested
  counter: []
  note: 'F is a waiting-time argument of the type the 2024 video criticises for unrealistic assumptions; transfer to MITTENS is by analogy (TH-1 not analysed).'
  hierarchy_edge: true
```

Counter additions to existing rows (recompute mechanically at integration; as of 2026-10-09): d118 gains dNEW-24 (its attacker H is the target of dNEW-24); d017, d018, d019 gain dNEW-25 (attacker B); d143 gains dNEW-29 (attacker F).

### 3.2 Mini-forms (append to the mini-form table in `standard-forms.md`)

Targets of the rows above that have no form yet. The G2c row is an alias line (needed only for the optional rows).

```markdown
| A4c | P1: standard fixation models assume complete replacement each generation, which gives a baseline of 20 generations (Kimura's formula as read from Duffy's slide); P2: selection operating at 80% efficiency stretches this to 20/0.8 = 25 generations ([A4c](../claims/A4c-overlap-80pct-25-generations.md)) | fixation takes about 25 generations in an overlapping population [ally, secondhand] | arithmetic |
| A4g | P1: Wright–Fisher and Kimura's revision of it are the two standard fixation models; P2: both treat a generation as the whole population replaced ([A4g](../claims/A4g-day-standard-models-assume-complete-replacement.md)) | standard fixation models abstract away overlap, so a correction d is needed [day] | deductive |
| B4e | P1: population geneticists use Kimura's neutral-theory result to date the human–chimp divergence ([B4e](../claims/B4e-mccarthy-dates-use-kimura.md)) | Day's dates are consistent with the mutation rate by construction [critic] | deductive |
| B4f | P1: the neutral theory is used in the first place to date the divergence; P2: so it cannot independently explain common ancestry from nucleotide differences ([B4f](../claims/B4f-hossjer-neutral-theory-dates-divergence.md)) | the neutral theory cannot explain common ancestry [ally] | deductive |
| D2l | P1: the modern synthesis was built by naturalists and geneticists, not mathematicians; P2: its founders did not work out the probability calculations ([D2l](../claims/D2l-day-synthesis-founders-skipped-the-math.md)) | the synthesis rests on logic never checked by calculation [day, secondhand] | deductive |
| D8 | P1: the probability of a single protein forming by chance is 1 in 10^65, with no length or function stated ([D8](../claims/D8-milton-single-protein-1-in-1e65.md)) | the odds equal winning a lottery every week for a thousand years with the same numbers [ally, secondhand] | arithmetic |
| D14 | P1: a transposition occurs with frequency 10^-15 per sequential pair of genetic transfers and a specific one with probability 10^-21 (Eden, unsourced); P2: no selection acts on intermediates ([D14](../claims/D14-davis-relays-eden-1e36-genetic-transfers.md)) | about 10^36 genetic transfers to form one ordered gene pair [ally, relayed] | arithmetic |
| D15 | P1: coordinated expression change at several genes needs new binding sites to appear; P2: the intermediates have low fitness (asserted) ([D15](../claims/D15-hossjer-regulatory-waiting-time-9-my.md)) | the waiting time far exceeds 9 million years [ally, prediction] | statistical |
| G2b | P1: 252,000/1,400 = 180; P2: 1,400 generations per fixation is "the fastest rate of mutational fixation ever observed in any organism" ([G2b](../claims/G2b-duffy-180-arithmetic.md)) | 180 total fixed mutations is all there is time for [ally] | arithmetic |
| G2c | P1: a strictly serial model leaves no standing variation except the sweeping allele; P2: observed standing variation exists ([G2c](../claims/G2c-hancock-no-variation-prediction.md)) | the serial model is falsified [critic]; alias of B6c, same quote GG-13 | deductive |
| G3a | P1: the probability of a specific lottery number is far below the probability that some number is picked; P2: [implicit] the outcome space of evolution is analogous to a lottery with many winning outcomes ([G3a](../claims/G3a-camestros-lottery.md)) | some outcome is close to certain, unlike a specific one [critic] | analogical |
| ROOT-H | P1: after rescaling for mutation rate and genome length MITTENS gives about 10M against 20M required, a factor of about 2 ([A5a](../claims/A5a-hossjer-127-15800-10m.md)); P2: the Haldane cost step cuts the adaptive share (asserted, [H5](../claims/H5-hossjer-cost-step.md)); P3: [implicit] d = 0.45 applies inside his neutral and selected rates; P4: [implicit] a mathematical statistician's agreement is evidence about population-genetic assumptions ([ROOT-H](../claims/ROOT-h-hossjer-agrees-with-main-argument.md)) | agreement with Day's conclusion about natural selection [ally] | arithmetic + asserted step |
| ROOT-K | P1: required time = 6.3 My × shortfall 1,075,000 = 6.8×10^12 y (derived); P2: [implicit] the shortfall scales as a time multiplier at a fixed per-fixation rate ([ROOT-K](../claims/ROOT-k-keen-time-is-the-reason.md)) | the required time exceeds the age of the Universe by orders of magnitude [ally] | arithmetic |
| ROOT-T | P1: Tipler wrote a foreword and an appendix and called the book "the most rigorous mathematical challenge to Neo-Darwinian theory ever published"; P2: [implicit] Tipler's own standard of rigor carries over to population genetics ([ROOT-T](../claims/ROOT-t-tipler-endorsement.md)) | Probability Zero is rigorous [ally, secondhand] | abductive |
```

### 3.3 Registry row (add to the Id registry table in `NOTES.md`; the row above `chk:B0` is a good place)

```markdown
| x:eden-p9-caveat | literature | Eden's own caveat on his 10^36 estimate: "a very rough estimate", and "a discovery of a new transposition mechanism can make such speculations an exercise in futility" | Eden, Wistar Monograph No. 5 (symposium 1966-04), p.9; claims/D14 (proposed 2026-10-09) |
```

Also amend the existing registry row `x:darwinzdf42-hitchhiking`: Hancock states the same hitchhiking point on video (t=02:19:03: "selection can't fix multiple things at once. That's literally what genetic hitchhiking is"; "the preposterous thing that he said that selection can't fix multiple things at once"). Add to its source column: "also Zach Hancock, Gutsick Gibbon video 2026-10-03, t=02:19:03". No new row is needed: the registry id is a target (d252, d253), and the argument is the same one.

### 3.4 Lineage nodes (append to `lineage.yaml`; optional)

Five nodes. Day-side parents exist only for the d and Haldane arguments, so lineage nodes are proposed only where a dated parent exists. Not proposed, and why: B5j, ROOT-PG, ROOT-COV, ROOT-EP, D2k, D2l, F1c (their Day-side counterpart is a slide read aloud, not a dated Day text; revisit if the book is bought).

```yaml
- id: L-day-complete-replacement-2025
  label: "Day: discrete-generation equations implicitly assume the whole gene pool is replaced each generation"
  side: day
  kind: argument
  date: 2025-12-24
  claim_ids: [A4g]
  locator: "https://zenodo.org/records/18166234 abstract (raw zenodo-18166234.txt l.15)"
  quote: "implicitly assuming that the entire gene pool is replaced each generation"
  parents:
    - {id: L-d-intro-2025, relation: descends}
  inferred: false
  why: ""
  fate: dormant
  fate_date: 2026-09-28
  fate_locator: "claims/A4d: d dropped from the MITTENS 3.0 formula; the premise itself was not withdrawn"

- id: L-hancock-overlap-2026
  label: "Hancock: the Moran model and effective size already handle overlapping generations"
  side: critic
  kind: reply
  date: 2026-10-03
  claim_ids: [A4e]
  locator: "https://www.youtube.com/watch?v=_Vu0ZVVjwHc t=00:43:38"
  quote: "And the Moran model is the model of overlapping generations."
  parents:
    - {id: L-day-complete-replacement-2025, relation: responds-to}
  inferred: false
  why: ""
  fate: alive
  fate_date:
  fate_locator: "Answers the Duffy/book version of d; MITTENS 3.0 dropped d (claims/A4d)"

- id: L-hancock-d-2026
  label: "Hancock: d has no equivalent term in population genetics"
  side: critic
  kind: reply
  date: 2026-10-03
  claim_ids: [A4f]
  locator: "https://www.youtube.com/watch?v=_Vu0ZVVjwHc t=01:20:50"
  quote: "I don't know what D is like there is no equivalent term in population genetics."
  parents:
    - {id: L-d-intro-2025, relation: responds-to}
    - {id: L-camestros-d-undefined-2026, relation: resembles, inferred: true}
  inferred: true
  why: "resembles: Camestros made a 'd is undefined' point in January and withdrew it; Hancock does not cite him and objects to the concept, not the missing definition"
  fate: alive
  fate_date:
  fate_locator: "Answers Duffy's slide; the definition is on p.153 of the book per a relayed message (claims/A4f)"

- id: L-hancock-fmax-no-mu-2026
  label: "Hancock: MITTENS's model has no mutation rate"
  side: critic
  kind: reply
  date: 2026-10-03
  claim_ids: [G2h]
  locator: "https://www.youtube.com/watch?v=_Vu0ZVVjwHc t=01:41:38"
  quote: "Notice that his model had no mutation rate, right?"
  parents:
    - {id: L-mittens-formula-blog-2026, relation: responds-to}
  inferred: false
  why: ""
  fate: alive
  fate_date:
  fate_locator: "Answers the Duffy version; Day's reply is that G_f is a measured total (claims/G1)"

- id: L-hancock-hard-soft-2026
  label: "Hancock: the cost of selection applies only to hard selection"
  side: critic
  kind: reply
  date: 2026-10-03
  claim_ids: [H2a]
  locator: "https://www.youtube.com/watch?v=_Vu0ZVVjwHc t=02:07:18"
  quote: "the cost of selection is only applicable for hard selection models where selection's effect is independent of the genotypes"
  parents:
    - {id: L-haldane-d-487-2026, relation: responds-to}
  inferred: false
  why: ""
  fate: alive
  fate_date:
  fate_locator: "R4 H, H2-hard, H3: the result is conditional on hard adaptive selection with a soft deleterious load"
```

## 4. Video arguments with no claim file

Source: Gutsick Gibbon and Zach Hancock, "No, Vox Day's AI-Generated Books Did Not Debunk Evolution" (3:30:28, 2026-10-03; auto-captions `sources/raw/critics/yt/_Vu0ZVVjwHc.transcript.txt`, read-only, untrusted). Every quote in the new claim files was checked programmatically against the caption line at the stated timestamp. Where a sentence spans two caption lines the file says so.

### 4.1 Coverage of the 210 minutes

| Time | Content | Mapped to |
|---|---|---|
| 00:00-00:09 | Framing, Duffy's "light bulb" about common descent, theology aside | not a claim |
| 00:09-00:24 | Hancock's credentials (GG-14, GG-15); history of population genetics; "overlapping generations is a hundred years old"; mathematicians in the synthesis | D2k (new), D2l (new, Day side), A4e |
| 00:22-00:27 | Predictive record of population genetics (hemophilia, peppered moth, Drosophila and others) | ROOT-PG (new) |
| 00:28-00:30 | "Statistically impossible" versus covariance | ROOT-COV (new) |
| 00:30-00:34 | Tipler is a Discovery Institute associate; AI co-author ("does not mean that it is wrong") | ROOT-EP (new); the AI point is not a claim |
| 00:34-00:41 | Duffy's four-week vetting by a mathematics teacher; the acronym | not a claim (process) |
| 00:41-01:20 | Overlapping generations: Moran model, effective size, Kimura is not a revision of Wright-Fisher; the 20 to 25 generation example; at 00:50 "this is just the waiting time problem" | A4g (new, Day side), A4e (new), A4c (rows); F1c (new) |
| 01:20-01:24 | The selective turnover coefficient d | A4f (new) |
| 01:24-01:28 | Single mutations can change many base pairs | A3x (existing; add Gutsick Gibbon to `by` of d006, locator t=01:24:56) |
| 01:28-01:37 | Serial reading; factor of two | G2 (GG-01), A3d (GG-02): existing |
| 01:33-01:40 | Site-frequency spectrum prediction | G2c / B6c (GG-13): existing |
| 01:36-01:42 | "No mutation rate, no selection coefficient" | G2h (new) |
| 01:41-01:58 | Derivation of k = μ, 76.8, bacteria | B5 (GG-03), B5c (GG-04 to GG-09), A5c (GG-07, GG-08): existing |
| 01:58-02:04 | 205M, 407 per generation | A3x (GG-10 to GG-12): existing |
| 02:05-02:13 | Haldane's cost, hard versus soft selection, intermediate frequency | H2a (new) |
| 02:13-02:21 | Neutral theory is not a retreat; hitchhiking | B5j (new); hitchhiking via the registry amendment in 3.3 |
| 02:20-02:26 | Track record again; "not a statistical model" | ROOT-PG, ROOT-COV |
| 02:26-03:04 | Day's biography and politics | not math; excluded (about 38 minutes). Correction for `opponents/gutsick-gibbon.md`, which dates the non-math part from about 02:15: the captions show the Haldane and neutral-theory mathematics running to about 02:26 |
| 03:04-03:06 | Endorsers lack population-genetics background; "Hössjer has made similar blunders in waiting-time papers" | ROOT-EP (new); F1c / D15 rows |
| 03:06-03:21 | McCarthy quote; whether the book is a bestseller; MITTENS versions; Athos conversation; other chatbots; peer review | not claims (see 4.2) |
| 03:21-03:30 | Duffy's situation; channel policy | not a claim |

### 4.2 Recorded but not drafted as claims

- **Chatbot "reviews"** (03:15-03:17: ChatGPT and Gemini judge that Day did not answer critics; the claim that Day's prompt to his own AI included the word "pessimistic"). Not reproducible and not independent of the prompt; the audit's own process is also AI-driven (HANDOFF), so the symmetric rule is to treat chatbot verdicts as non-evidence on both sides.
- **No peer review** ("I have no peers" quoted at 03:17:54). Already in the corpus as PZ-02 (Myers); a process fact, not an argument about the maths.
- **Vetting by a mathematics teacher, the acronym, AI co-authorship, bestseller rank (03:06:52), Day's politics.** Process or ad hominem; the host herself says AI co-authorship "does not mean that it is wrong" (00:33:39).
- **MITTENS is a moving target** (four versions; 03:09). Already mapped as the versions ledger and lineage.
- **"He plugged it into DeepSeek" (02:04:48).** Speculation about authorship; no claim.
- **Possible critic-side errors noticed while reading, not verified** (for the balance ledger): (a) at 02:16:39 Hancock says Day made "a factor of two error" in the 4Nₑ line, "using the formula for a hloid"; Kimura and Ohta 1969 give about 4Nₑ for a neutral allele that fixes (B7b), so this looks wrong or unexplained (recorded in B5j); (b) at 02:08:20 he says Haldane's cost matters "in populations that are really small", which is consistent with Nunney's dependence on M = 2Ku (H2) but was not derived; (c) the 25/75-80 y formula for effective size (A4e) is stated from memory.

### 4.3 The 12 new claim files and the edges to flip

All are in `docs/research/claims/`, status `extracted`, verdicts `pending` (ROOT-COV and ROOT-EP external `untestable`), `load_bearing: false`. Ids were checked against the claims directory, the refresh proposals (B5i, A3d1, A3e, G6, G7 and others are reserved there, hence B5j) and the PLAN. Pending integrations may still claim an id; lint reports duplicates.

| File (id) | Side / parent | One line | Edge to set when rows are pasted | Row |
|---|---|---|---|---|
| `A4g-day-standard-models-assume-complete-replacement.md` (A4g) | day / A4 | Day: discrete-generation equations assume the gene pool is replaced each generation (Zenodo 18166234 text is firsthand; the "two standard models" wording is the book via Duffy's slide) | already `supports A4` | none (target) |
| `A4e-hancock-overlap-is-handled-by-ne-and-moran.md` (A4e) | critic / A4 | Moran model and effective size handle overlap; Kimura did not revise Wright-Fisher | `{type: attacks, target: A4g}` | 01, 02, 03, 05 |
| `A4f-hancock-d-not-a-selection-coefficient.md` (A4f) | critic / A4 | d has no equivalent in population genetics; would cancel if a generation count | `{type: attacks, target: A4}` | 04 |
| `G2h-hancock-fmax-has-no-mutation-or-selection-term.md` (G2h) | critic / G2 | F_max has no mutation rate and no selection coefficient | `{type: attacks, target: A}` | 23 |
| `H2a-hancock-cost-of-selection-hard-selection-only.md` (H2a) | critic / H | the cost applies only to hard selection; the allele need not start rare | `{type: attacks, target: H}` | 24 |
| `B5j-hancock-neutral-theory-is-not-a-retreat.md` (B5j) | critic / B | drift at the molecular level, selection at phenotypes; not a retreat | `{type: attacks, target: B}` | 25 |
| `ROOT-pg-hancock-popgen-track-record.md` (ROOT-PG) | critic / ROOT | population genetics has a predictive record; a challenger must meet it | `{type: attacks, target: ROOT}` | 26 |
| `ROOT-cov-hancock-selection-is-a-covariance.md` (ROOT-COV) | critic / ROOT | "statistically impossible" is a category error | `{type: attacks, target: ROOT}` | 27 |
| `ROOT-ep-hancock-endorsers-lack-popgen-background.md` (ROOT-EP) | critic / ROOT | Dembski, Hössjer and Tipler are Discovery Institute associates without population-genetics training | `{type: attacks, target: ROOT-H}, {type: attacks, target: ROOT-T}` | 13, 14 |
| `D2l-day-synthesis-founders-skipped-the-math.md` (D2l) | day / D2g | Day: the synthesis was built by naturalists, not mathematicians (book, via Duffy's slide; secondhand) | already `supports D2g` | none (target) |
| `D2k-hancock-mathematicians-built-the-synthesis.md` (D2k) | critic / D2g | Pearson, Fisher, Wright, Haldane and Kingman were mathematicians | `{type: attacks, target: D2l}` | 28 |
| `F1c-hancock-waiting-time-lineage.md` (F1c) | critic / F1 | Day's argument is in the waiting-time lineage; that literature relies on unrealistic assumptions | `{type: attacks, target: F}` | 29 (and 12 against D15) |

To flip an edge: replace the `edges: []  # PROPOSED: ...` line of the file with `edges: [<the edge>]`. Scratch test: with all rows pasted and all edges flipped, `argmap_check.py` reports 130 attacks edges (119 plus 11), all covered, 322 defeaters, 136 forms.

### 4.4 Proposed quote entries (append to `quotes-critics.md` under the `YT-_Vu0ZVVjwHc` heading)

Ids GG-17 onward; the quotes are the ones in the claim files. Day-side relays (Duffy's slide read by the host) are marked.

```markdown
- **GG-17** | t=00:43:38 | branch A4e | Hancock
  > "And the Moran model is the model of overlapping generations."
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-18** | t=00:48:29 | branch A4e | Hancock
  > "And you just scale that effective population size by the slowdown of drift due to overlapping generations."
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-19** | t=00:51:57 | branch A4e | Hancock
  > "That's not what Kamura did."
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned. Answers the previous caption line, which ends "Kamura" and continues "doesn't have a subsequent revision of the right fisher model".
- **GG-20** | t=01:00:59 | branch A4e | Hancock
  > "it's a correction factor that enables you to take the census population size and correct it for the observed rate of genetic drift"
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-21** | t=01:20:50 | branch A4f | Hancock
  > "I don't know what D is like there is no equivalent term in population genetics."
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-22** | t=01:21:10 | branch A4f | Hancock
  > "if you plugged in 25 there then you also have 25 in the denominator and cancel"
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned. Continues on the next caption line.
- **GG-23** | t=01:23:35 | branch A4f | Gutsick Gibbon (host)
  > "In population genetics, selection coefficients tend to describe fitness differences between genotypes, whereas day selection coefficient seems to just be a summation of background demographies within populations."
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-24** | t=01:41:38 | branch G2h | Hancock
  > "Notice that his model had no mutation rate, right?"
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-25** | t=01:36:03 | branch G2h | Hancock
  > "this is not even necessarily a measure of selection"
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-26** | t=02:07:18 | branch H2a | Hancock
  > "the cost of selection is only applicable for hard selection models where selection's effect is independent of the genotypes"
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-27** | t=02:12:32 | branch H2a | Hancock
  > "the frequency doesn't have to be very low. It could have been a neutral alil and so it could have been at intermediate frequencies, right?"
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-28** | t=02:08:20 | branch H2a | Hancock
  > "that's important in populations that are really small in size and most of the issues come from uh being poorly adapted to your environment."
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned. Subject on the previous caption line (02:08:00).
- **GG-29** | t=02:18:21 | branch B5j | Hancock
  > "So like drift can still dominate at the molecular level and selection is dominating at the phenotypic level."
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-30** | t=02:20:03 | branch B5j | Hancock
  > "Um the these models existed long before Vox day um and exist completely independently of him."
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-31** | t=02:16:59 | branch B5j | Hancock
  > "we are not here to like save Darwin as a human"
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-32** | t=00:27:23 | branch ROOT-PG | Hancock
  > "any new idea must run the gauntlet and be able to survive the theoretical edifice of population genetics"
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-33** | t=00:23:55 | branch ROOT-PG | Hancock
  > "And what this shows us is that this math is not arbitrary."
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-34** | t=00:26:41 | branch ROOT-PG | Gutsick Gibbon (host)
  > "The blunt fact of the matter is Vox Day's math can't do any of this."
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-35** | t=00:29:09 | branch ROOT-COV | Hancock
  > "natural selection is a statistical co-variance between a trait value and how many offspring you leave, right?"
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-36** | t=00:29:29 | branch ROOT-COV | Hancock
  > "So to say it's a statistically impossible is like to misunderstand the basics of like what a covariance is."
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-37** | t=03:04:48 | branch ROOT-EP | Gutsick Gibbon (host)
  > "Generally, none of them have a particularly prevalent biology or population genetics background"
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-38** | t=03:05:09 | branch ROOT-EP | Gutsick Gibbon (host)
  > "And in fact, Hosture has made blunders very similar"
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned. Continues on the next caption line (03:05:30).
- **GG-39** | t=00:31:35 | branch ROOT-EP | Gutsick Gibbon (host)
  > "I think if you're going to include Tipler's quote in your rebuttal here, you probably should Google him and see that he's an ID proponent."
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-40** | t=00:14:00 | branch D2k | Hancock
  > "And so like to say that he is not a mathematician or that like there were no mathematicians involved in the modern synthesis is just like wild to me."
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-41** | t=00:14:21 | branch D2k | Hancock
  > "coallescent theory was invented by JFC Kingman who is like a pure mathematician"
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-42** | t=00:17:44 | branch D2k | Hancock
  > "Carl Pearson being trained as a pure mathematician was one of the first to start this."
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-43** | t=00:50:34 | branch F1c | Gutsick Gibbon (host)
  > "Now my understanding is that this is just the waiting time problem."
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-44** | t=00:50:54 | branch F1c | Hancock
  > "It is it is in definitely in the lineage of waiting time problems."
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-45** | t=00:41:55 | branch A4g | Duffy (slide, read by the host) `secondhand`
  > "the generational models including the right fisher model that underlies most fixation theory assumes that the entire parental generation is completely replaced by the offspring generation."
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-46** | t=00:59:16 | branch A4g | Duffy (slide, read by the host) `secondhand`
  > "In standard fixation models, a generation represents the entire population"
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
- **GG-47** | t=01:14:43 | branch A4c/A4g | Duffy (slide, read by the host) `secondhand`
  > "fixation time in a population where selection operates at 80% efficiency will take approximately 25 generations"
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned. Preceded on the previous line by "If Kamura's formula gives a fixation time of 20 generations assuming complete replacement each generation, the actual".
- **GG-48** | t=00:13:19 | branch D2l | Duffy (slide, read by the host) `secondhand`
  > "The neodyarwinian synthesis had been constructed by naturalists and geneticists, not by mathematicians."
  - note: Added 2026-10-09 (mapping proposals); auto-caption, spelling as captioned.
```

## 5. Proposed wording for `NOTES.md` (Judgement calls)

> 12. **What "mapped" means (proposed 2026-10-09).** A critic or ally claim is mapped when it has a parent and an edge in `hierarchy.yaml` and appears in at least one defeater row (as attacker or target), or its file states why no attack is warranted. `extracted` and `reviewed` are review states, not mapping states. Three nodes have no row by design: G1b (Samson) and G1c (Camestros) state an accounting identity both sides accept; ROOT-DE (Dembski) is a position statement and a question that Day answers (d129).
> 13. **Aliases.** G2c and B6c are the same argument (quote GG-13) written twice; B6c carries the rows. [If accepted] G2c is an alias of B6c and takes no rows of its own; [if not] use the optional rows dNEW-21 and dNEW-22.
> 14. **Cross-side convergence on the clock.** McCarthy (B4e), Hössjer (B4f) and keruru (B4g) each state, from three different positions, a dependence of divergence dates on the neutral rate or on calibration, and so support Day's B4d. Recorded as support edges; the audit's reading is in B4d (a pedigree-rate date is fossil-independent but still assumes k = μ per generation).
> 15. **Slide-relayed Day statements.** A4g and D2l are Day-side nodes whose book wording is known only through Duffy's slides read aloud on the Gutsick Gibbon video; A4g also has Day's own Zenodo sentence. They exist so the critics' replies have a target with premise labels.
> 16. **Credential arguments (ROOT-EP).** Included for completeness with `untested` rows. The project's own rule (FP-01) is that a credential count is not a rebuttal, and the host of the video concedes it for AI co-authorship (t=00:33:39); the same standard applies to Day-side endorsements (ROOT-T, ROOT-H).

For `R5-draft.md`, section 3 criterion 2: see the proposed sentence at the end of section 1.

## 6. Balance: strong arguments that are under-checked (candidates for dedicated checks)

Ordered by how much a result would move the map. None has been started; names are suggestions.

1. **Mansfield's supply argument (B5b), `B5b-f`.** The identity (2N new neutral alleles at 2% neutral, times 1/(2N), is one fixation per generation) holds, but the claim file's own algebra shows that 20M fixations in 450,000 generations needs a neutral fraction f = 0.89 of the 100 de novo mutations, and 17.5M in 252,000 generations needs f = 1.39 (impossible). So the argument as written does not reach the requirement; it depends on an unsupplied f, and on a full pipe (B1c). A check would put a sourced f (fraction of de novo mutations in unconstrained sequence) next to the requirement per lineage, using the event counts from GAP-07b/07c, and report where the supply argument closes or fails. It has only the R2 arithmetic and Day's rejoinder (d143); it is the clearest case of a strong critic claim tested only as a by-product.
2. **Latency versus throughput (F1, F1b).** Logic checked (`f1_throughput.py`), but the claim file notes that the in-transit count is Little's law, not measured, and that feasibility is F2's question, which fwdpy11 confirms only for F2 (R5 criterion 7). A dedicated check would measure the in-transit number and spacing under human-like linkage and recombination and cross-check in SLiM or fwdpy11. F1b (McCarthy) has no inbound attack at all.
3. **Hancock's standing-variation prediction (G2c / B6c), `G2c-sim`.** Specified in the claim file (forward simulation with the sweep rate 1/1,322 per genome-generation and free recombination, measure neutral heterozygosity at unlinked sites against θ), never run. It is falsifiable, it is the one critic argument with a stated prediction about data, and Day's own text (G2g, Appendix A "must be sequential") gives the premise. Pair with the SFS shape, not only heterozygosity.
4. **Overlap: effective size versus d (A4e, A4f), `A4-sim` with an Nₑ arm.** R4 C2 tested d against hazard-scale and per-generation s. It did not test Hancock's claim that Felsenstein-type Nₑ already accounts for overlap, nor whether Nₑ rescales a sweep time. The age-structured Moran simulation already proposed in `A4` would answer both.
5. **Matev's points not yet checked (A2i, G5, B3i; refresh C-1, C-4).** A2i (years versus generations) has `fidelity` and `external` pending and no inbound attack. G5 (the coefficient of variation falls while the variance rises) agrees with the existing G verdict, but the refresh flagged that the Fisher's-theorem point should be checked against the paper text before it is cited. G6 and G7 (refresh) are still unfiled.
6. **Hössjer's waiting-time model (D15) and the 2024 Hancock video (F1c, TH-1).** The only quantitative ally prediction in branch D has no check and no engagement from any critic. Obtain the 2021 model (J. Theor. Biol. 524:110657, not retrieved; no paywall bypass) and the TH-1 captions on disk, tabulate the assumptions the video criticises, and apply them to both D15 and F_max.
7. **Is the clock circularity real (B4d with B4e, B4f, B4g)?** Three critic-side or ally-side sources state it and Day relies on it; the audit's counter is analytic (Langergraber 2012). A date-independent test of k = μ (closely related pairs with known split dates; the "result that would change a verdict" in B4d) has not been attempted.
8. **A population-genetic validation panel (ROOT-PG).** The burden-of-proof argument is answered only by the repo's textbook baselines (B0). A short, sourced panel of published predictions (mutation-rate estimates, selection strengths, sweep timing) run through the repo's own simulators would give the argument a test on the audit's side.
9. **The hard/soft split of human adaptive selection (H2a).** R4 H3 is conditional on hard adaptive selection with a soft deleterious load; no one has supplied the soft fraction. This is a data gap, not a computation.

**Critic and ally claims nobody has attacked** (no row has them as target; 34 nodes of all statuses as of 2026-10-09, before this file): A2c, A2h, A2i, A3d, A4b, A4c, B3i, B4e, B4f, B5g, B5h, B6b, D13, D14, D15, D1c, D1d, D8, E1, F1b, G1b, G1c, G2b, G2c, G2d, G2e, G2f, G3a, G5, H6, ROOT-DE, ROOT-H, ROOT-K, ROOT-T. This file gives an inbound row to A4c, B4e, B4f, D8, D14, D15, G2b, G2c (optional), G3a, ROOT-H, ROOT-K and ROOT-T. The remaining critic-side arguments with no inbound test and a pending or partial verdict are the concrete list a second reader could take against the skew in R5 4.3 item 2: A2c, A2h, A3d, A4b, B6b, D1c, D1d, F1b, G2d, G2e, G2f, G5, H6 (G1b, G1c and ROOT-DE are no-attack by design).

Day-side or audit points that this pass *credits to the critics* or *finds against them*, for the record: Hancock's "no equivalent term" for d survives Camestros's withdrawn "undefined" point only as a conceptual objection (A4f); his factor-of-two remark on 4Nₑ looks unsupported (B5j); and "mathematicians built the synthesis" (D2k) does not touch the narrow reading of Day's sentence (D2l). On Day's side, A4g's premise is Day's own sentence in a 2025 paper, so the critics' fidelity point is about how standard theory is described, not about the arithmetic of d.

## 7. Integration checklist

1. Paste 3.1 (rename ids, fix the dNEW-22 counter), 3.2 and 3.3; flip the edges in 4.3; paste 3.4 and 4.4 if wanted.
2. `research/.venv/bin/python -I research/checks/lint_research.py --write-hierarchy`, then `research/tools/argmap_check.py` (expect no new errors), then `argmap_render.py`.
3. Recompute counters mechanically; refresh counts in `NOTES.md`, `docs/arguments/README.md`, `README.md`, `docs/HANDOFF.md`.
4. Add the NOTES judgement calls (section 5) and the amended registry text (3.3).
5. Update `opponents/gutsick-gibbon.md` (video segment correction) and `opponents/zach-hancock.md` (new claim ids A4e, A4f, G2h, H2a, B5j, D2k, ROOT-PG, ROOT-COV, ROOT-EP, F1c) after review.
6. Existing-file edits this file does not make but that follow from it: A4c's Formal statement can now state the units (baseline 20 generations, divided by 0.8; transcript t=01:14:23 and t=01:14:43); `refresh-2026-10-09.md` item C-11 (`A3d1`, Hancock's factor of two against the halved target) can take the locators GG-02 (t=01:37:07, "this basic math is off by a factor of two") and t=01:55:13 ("the total expected amount is 2T mu").
7. Review each new claim with the usual two-sided steelman before any verdict moves off `pending`.

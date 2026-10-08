# Research Phase: Vox Day's Mathematical Case Against Evolution (*Probability Zero* / MITTENS) and Its Critics

## Context
**Goal.** Build an open-source evolution simulator with user-controllable variables. It should be able to **support, refute, or explore** the mathematical claims Vox Day makes against evolution, and the counter-claims of his critics. Before any product code, we stay in a **research phase**: we build a complete, sourced, two-sided map of every claim, and each equation gets a numerical check.

**Repo.** `/home/na/projects/evo-sim` is empty (README only).

**Decisions so far:**
- **Corpus:** the full lineage, from 2019 to the present.
- **Output:** the repo is canonical (markdown plus checks), and an Artifact/Doc summary is published at milestones.
- **Checks:** throwaway verification scripts are allowed. They are reviewed by Sonnet/Haiku subagents.
- **Fairness:** both sides get equal depth and equal scrutiny.

**Stance.** We are neutral. Every claim, from either side, gets three separate verdicts (§E1). Where standard theory makes a firm prediction (for example, neutral k = μ, independent of N), we state it as the null hypothesis. The check then confirms it or breaks it.

---

## Preliminary harvest (R1 pass 1 — done read-only, 2026-10-07)
Three agents ran in parallel: Day's archive, his cited sources, and his critics. Every number below came through a summarizing fetch. **None of it counts as recorded until it is checked against the raw source in R1 pass 2.**

### Corpus size
- About **120 posts** on voxday.net, 2019-02-07 → 2026-10-07. The 2019–21 posts were imported from voxday.blogspot.com.
- **39 Zenodo records** by "Day, Vox", all co-authored by "Claude Athos". 25 are on evolution or population genetics, 3 are data papers, and 11 are philosophy (out of scope). None is peer-reviewed.
- **Critics:** about 20 sources (Substack, blogs, YouTube). Nothing peer-reviewed found.
- **Primary literature:** 15 cited works were checked for citation fidelity.

### Day's core formalism (to verify verbatim)
| Name | Form (as quoted) | Source |
|---|---|---|
| MITTENS | `F_max = (t_div × d) / (g_len × G_f)` | blog 2026-02-04; Zenodo 18165980 |
| Selective turnover coeff. d | d = T·[∫μ(x)l(x)v(x)dx / ∫l(x)v(x)dx]; d≈0.45 | Zenodo 18166234; Q&A post |
| Bernoulli Barrier | pⁿ = 0.02^(2×10⁷) ≈ 10^−34,000,000; ~230 simultaneous sweeps; 14.7× vs 1,570× fitness spread | Zenodo 18167588 |
| Hard Limits | 4Nₑ<G; X=(Vₖ+2)·G/16 ≈10⁴; P(fix within G) ≈ exp(−π²Nₑ/G) | Zenodo 22129121 (no refs) |
| Intrinsic Irrelevance | E[F(T)] = μL∫₀ᵀF_X(u)du ≈ μL(T−4Nₑ) | Zenodo 22903977 |
| N/Nₑ rate | k = μ·N/Nₑ; also k = 0.743μ; k = 32.3μ (not in Zenodo; probably book only) | 18429937, 18525262, 19984826 |
| Beneficial fix time | t ≈ (2/s)ln(2Nₑ), s=0.001 → "~19,800 gens/fixation" | Q&A post |
| Haldane limit | 1 sub / 300 gens; with d → 487 | Zenodo 18168236 |
| Relictation | Cannings model; t̄=4Nₑ fails if one family replaces >~10% | Zenodo 23188201 |
| Darwillion | (1/20,000)^20,000,000 — Day calls it "a rhetorical device" | blog 2026-01-12, 09-17 |

**MITTENS parameters by version** (the drift is itself research data):

| Version | Gens/fixation | d | Generations | Required fixations | Shortfall |
|---|---|---|---|---|---|
| 2019 | 1600 | – | 450k | 30M | "562" max (arithmetic doesn't reconcile: 450k/1600=281) |
| 2025 paper | 1600 | 0.45 | 146,250 | 20M | 220,000× |
| 2026 3.0 | 1,322 | – | 252k | 205M | 1,075,000× (SNV-only ~94,000×) |

The **2026-05-07 "A Retraction and a Revision"** is Day's own partial retraction of the cost-of-selection bound.

### Argument hierarchy (v1)
Edges: ⟂ = attacks, ✓ = supports.
```
ROOT  "No evolutionary mechanism can produce observed divergence in available time" [Probability Zero, MITTENS 3.0]
├─ A Rate limit (MITTENS)
│  ├─ A1 Generations available (t_div 6.3–9 My; CHLCA later moved to 68 kya–1.3 My; g_len 20–32.5 y)
│  ├─ A2 G_f from LTEE (1,600→1,322; 909 Ara+2; 4,615 "NS only"; 78 hypermutators; 5,496 fixations/723k pop-gens)
│  ├─ A3 Required fixations (30M→20M→205M; 410 Mb from Yoo 2025)
│  │   ⟂ bp-vs-events: SVs/inversions counted per bp; 1,140 inversions span 6 apes; ~35M SNVs → ~17.5M/lineage
│  ├─ A4 Turnover coefficient d halves effective time
│  └─ ⟂ McCarthy/Hössjer: LTEE→human scaling (genome ~650–690× larger, N·μ·L supply, sex/recombination, clonal interference)
│     ✓ Hössjer (ally) still finds ~2× gap after scaling; keeps conclusion via H
├─ B Neutral theory insufficient
│  ├─ B1 k=μ is steady-state only; empty pipeline (Intrinsic Irrelevance; Chalub 2022)
│  ├─ B2 Hard Limits: drift ceiling X ≈ 10⁴; F(T)=exp(−π²Nₑ/T)
│  ├─ B3 k = μN/Nₑ (fixation prob 1/(2Nₑ)); k=0.743μ (Balloux & Lehmann); k=32.3μ
│  ├─ B4 Molecular-clock recalibration → CHLCA 200–580 kya / 68 kya
│  └─ ⟂ Mansfield, McCarthy, CS commenter: 2Nμ×1/(2N)=μ; ancestral polymorphism (E[div]≈2μT+θ_anc); pipelining
├─ C aDNA: zero fixations across ~1.1–1.2M SNPs in 7 ky; d estimates; Bio-Cycle model
│  ⟂ (no critic yet) — sources agent: 1240k panel is ascertained on present-day-variable sites
├─ D Sequence space / Wistar 1966 (Eden 10^325 vs 10^52; Ulam; Schützenberger; Weasel 540,000 gens)
│  ⟂ Rosenhouse ch.4 (+ ch.6 unaddressed); ✓ Day's critique of ch.4's lack of quantification
├─ E LTEE / punctuated equilibrium: hypermutation hazard 2.3%/founder; s zones; 0 parallel fixations
│  ⟂ "Taylor": hitchhiked neutrals count; Barrick 2009 45 muts/20k
├─ F Kimura irrelevance (fix time vs fix probability)
│  ⟂ Bowers: fix prob ≈2s; ⟂ latency≠throughput (Mansfield's truck analogy)
├─ G Bernoulli Barrier / average-rate (parallel vs serial)
│  ├─ G1 "average rate indifferent to parallelism" ✓ partly valid vs math-teacher/marathon
│  ├─ G2 LTEE throughput already includes parallelism
│  └─ ⟂ CreationMyths/Philalethist (recombination); Camestros (specific-vs-any outcome, Darwillion)
└─ H Cost of selection (Haldane 1957 300 gens; 11,739/321,444; Worden O(1) bits/gen)
   ✓ Hössjer;  ⟂ (critic gap: none found engaging Nunney/soft selection/Kimura's reply)
```

### Citation-fidelity ledger (sources agent; to re-verify)
| Verdict | Items |
|---|---|
| Accurate | Haldane 1957; Kimura & Ohta 1969 (4Nₑ, SD≈2.15Nₑ); Kimura 1962 fixation prob ≈2s; Chalub 2022's math; Keightley 2012; Bergeron 2023 (40× rate variation); Maruyama 1970/74; Frankham 1995 Nₑ/N≈0.1 |
| Partial | Balloux & Lehmann 2012 (0.743μ is Day's own figure); Chimp Consortium 2005 (SNV+indel merged; fixed vs polymorphic divergence); Tenaillon 2016; Good 2017 (≥95% rule; later corrected by Day's own 23105291) |
| Misread | Zeng 2021 (s≈0.001 is *negative* selection on complex traits, not beneficial); Yoo 2025 (bp vs events; 6-ape inversion count); Langergraber 2012 (≥7–8 My, not 6–7; fossil-independent); 1/(2Nₑ) neutral fixation (it is 1/(2N) — Day's own Hard Limits paper says so); Kimura & Ohta cited on recombination |
| Unverifiable | "Chalub 2012"; "k = 32.3μ" derivation; Kimura 1983 quotes; "25 fixations / 40k gens (Good 2017)"; Mathieson 2015 s values; Hössjer post (critics agent found it; sources agent did not — reconcile) |
| Internal contradictions | 2Nₑ vs 4Nₑ fix time; 1/(2N) vs 1/(2Nₑ); split dates 6.3/6.5/6–7/9 My/68 kya |

### Balance ledger — where each side is strongest and weakest (preliminary)
| | Day / allies | Critics |
|---|---|---|
| **Strong** | LTEE G_f is a measured *throughput*, so "you forgot parallelism" (math teacher, Duffy debate) misses it; Haldane/Kimura-Ohta used correctly; his own LTEE data paper (23105291) is careful and self-correcting; Rosenhouse ch.4 really does lack quantification; critics haven't engaged H, C, or the Bernoulli Barrier | k=μ independent of N (McCarthy, Mansfield); mutation-supply/genome scaling (even Hössjer concedes ~2×); pipelining/latency≠throughput; ancestral polymorphism; Darwillion specific-vs-any objection |
| **Weak** | bp-vs-events in 205M; Zeng s misread; 1/(2Nₑ); empty-pipe assumption; parameter drift across versions; arithmetic in 2019 post; no refs in Hard Limits / aDNA papers; panel ascertainment | loose uncited inputs (Mansfield 2%, relayed 7.2M, McCarthy 100 muts); expected values without variance; lots of ad hominem (Myers); no one checked Yoo 2025; key video (Gutsick Gibbon/Hancock 3.5 h) not located; nothing peer-reviewed |

### Known gaps to close in R1 pass 2
**Day's side:**
- *Probability Zero* book (paid): source of 32.3μ, Wistar, Ulam.
- Blog windows with no evolution-tagged posts: 2026-06-21→08-22 and 08-28→09-10.
- Untagged posts: "HARDCODED", "Irrelevance of Acclaim", "Rejection", "Historic Rigor".
- Evolution tag pages 19–25 (all pre-2019).
- The 2019/2021 Gariepy debate video and transcript.

**Critics:**
- Gutsick Gibbon + Zach Hancock video (URL, transcript).
- McCarthy's paywalled posts (01-26, 02-03) and his other Substack posts.
- Keruru's Substack.
- Camestros parts 5 onward.
- Joe Bowers' original review.
- r/DebateEvolution (fetch blocked; try old.reddit or the API).
- Larry Moran / Felsenstein / Peaceful Science (nothing found yet).

**Primary literature:**
- Full text of Kimura 1962/1968 and Kimura & Ohta 1969.
- Yoo 2025 supplement (the 187 Mb figure).
- Chimp Consortium 2005 (fixed vs polymorphic split).
- Wistar 1966 proceedings.
- Nunney 2003; Mallick 2024 (AADR).

---

## Repo layout (research artifacts only)
```
docs/research/
  README.md            # organization + status dashboard
  glossary.md          # pinned definitions (§E2)
  parameters.yaml      # single source of truth for numeric inputs, per side, per version (§E3)
  hierarchy.yaml       # id, claim, side, parent, edge {supports, attacks, revises, supersedes, depends-on}, status
  hierarchy/*.md       # Mermaid per branch A–H + overview
  claims/<ID>-<slug>.md
  sources/bibliography.md   # URL, date, version, archive URL, sha256 of local copy, access status
  opponents/<name>.md  # critics AND allies (Hössjer, Dembski, Tipler, Davis, Duffy)
  ledgers/fidelity.md, ledgers/balance.md, ledgers/contradictions.md, ledgers/versions.md
sources/raw/           # .gitignored — full texts never committed (copyright)
research/checks/       # THROWAWAY verification code + REVIEW.md
```
**Claim file template:**
- ID; verbatim quote with locator (URL, plus paragraph, page or equation number) and source version/date; firsthand or `secondhand` (known only via an opponent's quote).
- Formal statement, with parameters taken from `parameters.yaml`.
- Assumptions, both stated and implicit.
- Responses from the other side, plus where *its* math is weak.
- Primary literature with its fidelity verdict.
- **Pre-registered prediction**, under each side's model.
- Check script, result, and review link.
- **Three verdicts** (§E1).
- The simulator variables this claim implies.

## Research stages
**R0 Scaffold.**
- Create the layout and templates. Add `.gitignore` for `sources/raw/`.
- Set up a `uv` env with numpy, scipy, sympy, msprime, tskit. Add the SLiM 4 binary if installable, otherwise fwdpy11.

**R1 Corpus harvest, pass 2.** Turn the pass-1 catalogue above into raw local copies plus bibliography entries.
- Fetch every listed post and Zenodo PDF.
- Close the gap list above.
- **Crawl rule:** depth ≤2 from seeds; keep only claim-keyword-relevant links; log every exclusion with a reason.
- Parallel Sonnet agents: Day corpus / sources / critics+allies. Each writes files only under its own subdirectory.

**R2 Claim extraction.**
- One file per distinct mathematical or empirical assertion, from either side.
- Every number in the corpus maps to a claim ID.
- Contradictions and version drift go in the ledgers.

**R3 Hierarchy.**
- Finalize `hierarchy.yaml` and the Mermaid diagrams.
- Mark which claims are load-bearing for ROOT.
- Every critic and ally argument attaches to a node.

**R4 Math resolution.** For each claim:
1. Derive it, or find the derivation in the primary literature.
2. Pre-register the prediction.
3. Write the cheapest correct check.
4. Sweep parameters.
5. Find where the conclusion flips.
6. Get reviews.

**R4 priority checks**, ordered by how much of ROOT each one decides:
1. **k vs μ (B1, B3, Mansfield, McCarthy).**
   - Forward WF/Moran across N = 10²–10⁴ diploids. Census N vs Nₑ manipulated via offspring variance Vₖ. Sexual vs asexual.
   - Two start states: empty pipe vs at mutation–drift equilibrium.
   - Measure substitutions per generation.
   - Pre-registered predictions: standard theory says k = μ for every N and Vₖ. Day's model says k = μN/Nₑ, a deficit when T ≲ 4Nₑ, and a ceiling near X.
2. **Hard Limits F(T)=exp(−π²Nₑ/T) (B2).**
   - Compare against the simulated fixation-time CDF.
   - Then test whether a per-allele CDF bounds total throughput.
3. **Divergence with ancestral polymorphism (B1/B4).**
   - Simulate ancestor → split → two lineages.
   - Compare fixed differences with 2μT + θ_anc, and with Day's μL(T−4Nₑ).
4. **What counts as "required fixations" (A3).**
   - Recount from Yoo 2025 and Chimp Consortium 2005 data: SNV events vs indel events vs bp.
   - Per lineage vs total, fixed vs polymorphic. Pure data work.
5. **Turning LTEE G_f into a human rate (A2/G2).**
   - Asexual clonal-interference sim at LTEE-like N, μ and s, reproducing 1,322 and 909.
   - Then a sexual sim at human-like parameters, to see how G_f changes with N·μ·L, recombination, and the s distribution.
   - Test both sides' scaling arguments, including Hössjer's ~2×.
6. **Bernoulli Barrier (G).**
   - Many-locus sim: does fitness variance collapse? Is concurrent sweeps ≈ 230 a real cap?
   - Recompute 0.02^(2×10⁷) and check what event it actually prices: a specific outcome vs any outcome.
7. **Cost of selection (H).** Haldane's cost under hard vs soft selection and truncation selection; reproduce 300 / 11,739 / 321,444; compare with Nunney.
8. **Turnover coefficient d (A4/C).** Derive d. Then test in an age-structured sim whether "d" is the same thing as the standard overlapping-generation Nₑ / generation-time correction.
9. **aDNA zero-fixations (C).**
   - What fixation count does a neutral model predict over 7 ky, given a SNP panel chosen for present-day variable sites?
   - Re-analyze with AADR if the data is accessible.
10. **Arithmetic audit (all).** Recompute every headline number in sympy on both sides: the MITTENS versions, McCarthy's 22.5M, Mansfield's 1 per generation, the relayed 7.2M, the math teacher's marathon, Ara+2's 66/14/5.3.

**Code review.**
- Each check gets a **Sonnet** review covering correctness, seeds, replicates, and units.
- It also gets a **two-sided steelman review**: one agent per side asks "does this test the claim *as its author stated it*?"
- Trivial arithmetic checks get **Haiku**.
- Results go in `REVIEW.md`. A check only counts after it passes.

**R5 Synthesis.**
- Assign verdicts and fill in the balance ledger.
- Build a sensitivity table of which parameters drive each conclusion. This becomes the **simulator variable list**:
  - N, Nₑ, Vₖ, μ, L, s distribution (including negative), dominance, recombination
  - generation time, overlapping generations / age structure, sexual vs asexual
  - start state, demography over time, T, divergence-counting rule, mutator alleles
- Publish the summary Artifact/Doc.

**Exit the research phase when:**
- every load-bearing claim has a reviewed check and three verdicts;
- every critic and ally argument is mapped;
- the gap list is closed or explicitly recorded as inaccessible;
- the variable list is final.

Branches can graduate independently. Then: brainstorming → spec → writing-plans for the simulator.

---

## Epistemic and edge-case rules (from the critical review)
**E1 Three verdicts per claim.**
- (a) **Internal validity:** does the conclusion follow from the author's own assumptions?
- (b) **Model fidelity:** does the cited theory or paper actually say that?
- (c) **External validity:** are the assumptions biologically realistic?

Simulations settle (a) and (b). Only data settles (c).

**E2 Glossary pins:**
- fixation in a species vs fixed difference between lineages (split across 2 lineages)
- SNV vs indel vs SV vs bp
- Nₑ vs census N; 2N vs N; ancestral Nₑ (~5×10⁴–10⁵) vs modern (~10⁴)
- per-site vs per-genome rates; per-generation vs per-year
- **throughput (k) vs latency (t_fix)**
- LTEE "fixation": ≥95% of reads vs lineage-aware calls; selective vs hitchhiker vs mutator

**E3 Parameter register.** Every number comes from `parameters.yaml`, a cited quote, or is flagged `derived:` with its formula. A lint enforces this.

**E4 No question-begging.**
- msprime (coalescent; it assumes equilibrium) is used for baselines only. Forward sims decide.
- Scaling (N↓, μ↑ with θ fixed) assumes the theory being disputed. So run unscaled across one range first, and validate scaling before relying on it.
- Use exact Markov chains at small N to check where the diffusion approximation breaks down.

**E5 Model edge cases.**
- start state (empty vs full pipe)
- ILS / ancestral polymorphism
- variable N and bottlenecks
- hitchhiking, background selection, clonal interference
- mutators
- near-neutral (Ohta) mutations
- biased gene conversion and CpG hotspots (Day's own Ts/Tv/CpG point)
- overlapping generations
- sweepstakes reproduction (Cannings / relictation)

**E6 Bias controls.**
- Verbatim quotes only.
- Predictions pre-registered before running.
- A steelman agent for each side.
- Summarizer numbers are never recorded without the raw text: the pass-1 catalogue already contains summarizer-introduced uncertainty.
- I note that the agents' pass-1 assessments lean toward the mainstream. The balance ledger exists to counterweight that, and Day's valid points get recorded as prominently as his errors.

**E7 Sourcing.**
- Pin each claim to a version and date.
- Paid book: the user decides whether to buy it. Until then, book-only claims are tagged `secondhand`.
- Every material dated after June 2026 (my knowledge cutoff) is taken from fetched text, never from memory.
- Verify YouTube numbers against timestamps.

**E8 Licensing and outward actions.**
- Never commit full texts, only links, short quotes, and hashes.
- Don't create Wayback snapshots, contact authors, or post anything without the user's approval.

## Verification
- Every check runs via `uv run python -I research/checks/<file>` with a fixed seed, and reproduces the numbers recorded in its claim file.
- **Textbook baselines must pass first:**
  - neutral fixation probability is 1/(2N)
  - mean neutral fixation time is ≈4Nₑ, with SD ≈2.15Nₑ
  - Kimura's u(s,N)
  - beneficial fixation time ≈(2/s)ln(2N)
  - neutral k = μ at equilibrium
- **Cross-tool:** the k-vs-μ and fixation-time results are reproduced in both the numpy WF and SLiM/fwdpy11.
- **Lints:** `hierarchy.yaml` and the claim files must agree (no orphans; every claim has a source and verdicts); a numeric-provenance lint (E3); a bibliography check that every source has a URL and access status.
- **Balance audit at exit:** comparable source counts and check counts per side, and every "Weak" cell in the balance ledger traced to a claim file.

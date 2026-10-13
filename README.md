<div align="center">

<img src="docs/img/icon-animated.svg" alt="evo-sim icon: a double helix split by a cross into two lineages" width="140">

# evo-sim

### Can evolution make enough mutations fix in the available time?
**An open, numerical audit of Vox Day's *Probability Zero* / MITTENS argument and of his critics, as the groundwork for a simulator you can tune yourself.**

![phase](https://img.shields.io/badge/phase-research%20(R4%20of%205)-orange)
![claims](https://img.shields.io/badge/claims%20mapped-233-blue)
![checks](https://img.shields.io/badge/checks%20run-57%20(10%20demonstrably%20blind)-blue)
![reviews](https://img.shields.io/badge/reviews-same--model%2C%20not%20blind-critical)
![sides](https://img.shields.io/badge/scrutiny-both%20sides-blueviolet)
![python](https://img.shields.io/badge/python-numpy%20·%20msprime%20·%20fwdpy11-3776AB?logo=python&logoColor=white)

</div>

---

> **Caveat first:** this is an AI-run audit with no independent human review yet. See [Known gaps](#known-gaps-stated-up-front) before relying on any tally.
>
> **New here?** Read the whole story at your level: **[ELI5](docs/explain/eli5/README.md)** · **[ELI8](docs/explain/eli8/README.md)** · **[ELI10](docs/explain/eli10/README.md)** · **[ELI12](docs/explain/eli12/README.md)** · **[ELI18](docs/explain/eli18/README.md)**

## Known gaps, stated up front

Read this before trusting any number below. This audit is run by an AI system (Claude) directing subagents of the same model family, with one human owner. On 2026-10-12 it was audited twice from the inside: once in the style of a neutral third party, and once by Vox Day's own Triveritas test (logic, mathematics and empirical anchoring must all hold). Both reached the same headline: the individual checks are careful and well disclosed, but the audit's claims about itself are not yet earned. Nothing here has been reviewed by an independent human expert.

| # | Gap | Why it matters | Mitigation | Status |
|---|---|---|---|---|
| 1 | **Reviews are not independent.** All 65 reviews, steelmen and "re-derivations" are by the same model family, not blind, and the check's author decides what to do with them. One blocker was ever raised. | Shared blind spots and shared priors about evolution cannot be caught this way. | A planted-error test of the reviews; blind re-derivation of ten load-bearing nodes; a review packet for a different model family; a human population geneticist and one reader from each camp. | Packet and reviewer brief drafted ([outreach](docs/research/outreach/)); nothing sent; needs the owner |
| 2 | **The tallies overstate what was checked.** 58 of the 131 "holds" sit on claims with no reviewed check; "contested" is 115 of 173 decided external verdicts; only 14 of 233 claims pass all three verdict columns at once. | A count of verdicts reads as a score. It is not one. | An `unexamined` status, a four-way split of "contested", and a conjunction flag; comparative Day-versus-critic rates and p-values already removed. | Rates removed; the rest are written proposals awaiting go-ahead |
| 3 | **Pre-registration is weaker than the word suggests.** Of 57 checks run, 10 are demonstrably blind (registration clearly before results), 6 criterion-only, 3 reproductions, 18 single commits and 20 unknown. | "Pre-registered" should mean the prediction could have failed. | Every check now carries one of those labels ([table](research/checks/PREREG-STATUS.md)); new checks get a pre-run design review and pushed registration before any run. | Labels done; applied to L1c and FMnull |
| 4 | **Half the external verdicts rest on models.** 26 of 52 decided external verdicts rest on simulation or standard theory rather than independent data, and so do seven of the eight load-bearing ones. | Using mainstream theory to judge a critic of mainstream theory can beg the question. | A recorded basis for every external verdict (data, literature, simulation, theory), enforced by lint; real-data checks queued (L1b, L1c, FMnull real-data arm). | Coded count done; field is a proposal; checks queued |
| 5 | ***Probability Zero* itself has not been read.** The audit works from Day's posts and Zenodo papers. Paywalled papers and some platforms (X, Gab, Telegram) are also unread. | The book is the primary source. | Buy the book and re-extract a blind sample; list of paywalled papers for the owner. | Needs the owner |
| 6 | **No right of reply.** Neither Day nor any critic has been shown the findings about them. | An audit that cannot be answered is a verdict, not an audit. | Notices to Day and to 18 critics and allies listing findings for and against each, a 21-day window, replies published verbatim. | Drafted; not sent; needs the owner |
| 7 | **Rules changed mid-audit.** Two rules were added and redefined on 2026-10-11; two load-bearing verdicts (B and A2e) moved against Day without the three reviews the audit's own tiers require. | Changing the rule and the verdict together looks like fitting the rule to the answer. | A rule freeze with a written proposal, a 24-hour wait and a three-review re-score for any later change; decision pending on reverting B and A2e until reviewed. | Freeze accepted by the owner; revert decision open |
| 8 | **No rule for the final answer.** Nothing registered says how node verdicts combine into a top-level conclusion, or when the audit stops. | Without it, the conclusion can be chosen after the fact. | Register an aggregation rule and a stopping rule before the synthesis (R5). | Draft proposal written |
| 9 | **Rhetoric exemption.** Statements tagged as rhetoric are not fact-checked, and the "remotely close" test is undefined for absolute claims. | Either side can shelter a false statement behind the tag. | Tag by context, and always report the literal distance from the facts. | Proposal written |
| 10 | **Missing basics.** No licence, conflict-of-interest statement, stated priors, threat model or estimate of the audit's own error rate. | Standard for any audit meant to be relied on. | Drafts and templates written. | Needs the owner |

Full detail: [methods and limitations](docs/research/criticality/METHODS-AND-LIMITATIONS.md) · [method audit](docs/research/criticality/METHOD-AUDIT-2026-10-12.md) (MA-01 to MA-20) · [Triveritas critique](docs/research/criticality/triveritas-audit-2026-10-12.md) (TV-01 to TV-11) · [roadmap](docs/research/ROADMAP.md) · [decisions log](docs/research/DECISIONS.md). No finding counts as closed until a later pass re-audits it.

## Play with it
**[Is There Enough Time](https://nickallevato.github.io/evo-sim/explain/eli-series/play.html)** is an interactive explainer of the math and the sims at five levels (ELI5 to ELI18). It has five small simulations you can run in the browser: a drift jar, a mutation river, a selection race, the MITTENS budget board, and a combination lock. ([source](docs/explain/eli-series/index.html))

<p align="center"><a href="https://nickallevato.github.io/evo-sim/explain/eli-series/play.html#eli10"><img src="docs/img/mutation-river.svg" alt="Mutation river: neutral mutations drift across the river; most are lost, a few reach the far bank and fix" width="720"></a></p>

**Mutation river.** Each dot is one neutral mutation, and its position is the share of the population that carries it. Most dots sink. The few that reach the far bank are substitutions. A bigger population drops in more mutations, but each one is less likely to cross, and the two effects cancel: substitutions arrive at the mutation rate, **k = μ**. This is a real seeded Wright–Fisher run with 2N = 80, μ = 0.02 per copy and an equilibrium start. It gives 9 substitutions in 600 generations against μ × 600 = 12 expected, which is Poisson scatter for a run this short.

<p align="center"><a href="https://nickallevato.github.io/evo-sim/explain/eli-series/play.html#eli12"><img src="docs/img/combination-lock.svg" alt="Combination lock: stepping stones open in a few dozen tries, the valley takes hundreds" width="720"></a></p>

**Combination lock.** Some features may need several mutations before they help. If each right step is kept (**stepping stones**), the lock opens quickly. If nothing helps until every dial is right at once (a **valley**), the wait grows with the number of combinations. This is an illustrative toy, not the audit's D15 result. D15 tests Hössjer's multi-step waiting time and is still running. Both previews are drawn by [`research/tools/eli_readme_svgs.py`](research/tools/eli_readme_svgs.py).

## Why this exists
Vox Day argues, in *Probability Zero* (2025), the MITTENS papers on Zenodo and many blog posts, that population genetics *mathematically* rules out natural selection explaining the human–chimp divergence. His critics (McCarthy, Mansfield, Hancock, Camestros Felapton, Bowers and others) say his maths is wrong. Both sides mostly trade assertions.

This repo works through each claim on both sides:

1. **Extract** every mathematical or empirical claim, with a verbatim quote and its source.
2. **Arrange** the claims into one argument tree.
3. **Check** each load-bearing equation with an exact Markov chain or a forward simulation. Predictions are pre-registered before each run.
4. **Review** every check three times: a correctness review, a steelman for Day and a steelman for the critics.
5. **Record** three verdicts per claim: *internal* (does it follow?), *fidelity* (does the cited source say that?) and *external* (is it biologically realistic?).

The end product is a **user-controllable evolution simulator** whose knobs are exactly the parameters the dispute turns on.

> **Stance:** neutral. Valid points are recorded as prominently as errors, whoever makes them. Where standard theory makes a firm prediction it is stated as the null hypothesis, then tested rather than assumed.

---

## How the audit works

<p align="center"><img src="docs/img/audit-systems.svg" alt="Systems diagram: sources, verbatim quotes, claims with three verdicts, argument map, checks, reviews, verdict rule, ledgers, synthesis and simulator spec, with the criticality layer drawn over all of it" width="900"></p>

- **Sources to quotes to claims.** Day's papers and posts, his critics and the literature are reduced to verbatim, dated, located quotes, then to claims. Each claim gets three verdicts: internal, fidelity, external.
- **Claims to the argument map.** Claims hang on eight branches (A-H) under Day's root claim, with typed objections (defeaters) and a dated lineage of each argument.
- **Checks.** Each load-bearing equation gets a pre-registered check (exact chain or forward simulation), a write-up and a review: three reviews for load-bearing checks, one combined review for low-stakes ones.
- **One verdict rule** (R1 materiality, S scope, N non-sequitur, F fidelity, U relays, C charity, RH rhetoric versus dialectic, RD reading-dependent verdicts) is applied to Day, critics and allies alike. A slip that does not move a conclusion by more than 25% goes to a ledger, not to a verdict. How one quoted statement flows through it is drawn in [`audit-verdict-logic.svg`](docs/img/audit-verdict-logic.svg).
- **Then** ledgers, a synthesis (R5) with a sensitivity table, and the simulator spec.
- **Who does it, plainly:** the audit is AI-run. Every check, review and method pass was done by Claude instances inside one project session under one owner. The three reviews are three prompts to the same model family, not blind and not independent; no outside human or non-Claude reviewer has yet been asked. Details and what the tallies can and cannot mean: [`METHODS-AND-LIMITATIONS.md`](docs/research/criticality/METHODS-AND-LIMITATIONS.md).

## How the audit checks itself (criticality layer)

A standing layer audits the method, not the sources: a third-party-style method audit (20 findings, MA-01 to MA-20, none yet closed by re-audit), a critique that applies Day's own Triveritas test (logic, mathematics and empirical anchoring must all hold, Q203) to the audit (11 findings, TV-01 to TV-11; by that test the audit's tallies do not yet merit assent, chiefly because every review is by the same model family), a per-check pre-registration status table, a methods-and-limitations page, an owner decisions log, and drafted (unsent) right-of-reply letters and outside-reviewer packets. Findings route to no-decision fixes, held-back proposals, or owner decisions, and rule changes follow a freeze procedure. Start at [`docs/research/criticality/README.md`](docs/research/criticality/README.md); everything outstanding is in [`docs/research/ROADMAP.md`](docs/research/ROADMAP.md).

---

## Scorecard so far

<p align="center"><img src="docs/img/verdicts.svg" alt="Verdict tallies across 233 claims" width="760"></p>

*7 claims carry a reading-dependent verdict and 3 a reading-dependent rhetoric tag (10 reading-dependent verdicts in all before B1e's three fields were added on 2026-10-13; rule RD, 2026-10-11); the tallies above show the value under the reading in which the quoted statement is most defensible (not the reading best for the speaker), and the other readings are in each claim file.*

| ✅ Where **Day** holds up | ✅ Where the **critics** hold up |
|---|---|
| His empty-pipe formula $E[F(T)] = \mu L\int_0^T F_X$ is **exact** for its premise (B1) | Neutral substitution rate is $k=\mu$ for **any** $N_e$: fixation probability is $1/2N$, not $1/2N_e$ (B3) |
| $N_e$ really does set the fixation **timescale** (B3) | The ancestral "pipe" was **full**, not empty. Day has since withdrawn the empty start (B1c, B1d) |
| The Hard Limits exponent $-\pi^2 N_e/G$ is the correct leading-order tail (B2a) | Latency ≠ throughput: many sweeps can be in flight at once (F1) |
| LTEE $G_f \approx 1{,}300$ gens/fixation is a real **throughput** measurement and reproduces (A2) | Recombination removes the clonal-interference ceiling in the tested regime (F2) |
| Balloux–Lehmann fluctuation effect is real (B3b) | Divergence includes ancestral polymorphism: $d = 2\mu T + \theta_{anc}$ (B4a) |
| Soft selection does **not** make the cost of selection disappear (H) | The cap is $\ln R / D$, not a flat 10% (H2). The $0.743\mu$ figure is a window artefact (B3c) |
| Haldane arithmetic (300, 487) holds. Critics' "38M matches 35M SNVs" double-counts, and on Hancock's own event basis the match does not follow (B5c, X1) | 205M "required fixations" counts base pairs, not mutation events. The cited $s=0.001$ is *negative* selection (A3, Zeng 2021) |
| The founder hazard's size (~2.3% per event) and the relictation chain reproduce (E, E4) | $0.02^{2\times10^7}$ prices one pre-specified list. No cap near 230 sweeps under multiplicative fitness (G3, Gc) |
| Parallel sweeps share **one** reproductive budget, so concurrency cannot raise the selected total beyond it. At Haldane's assumed $R\approx1.1$ the long-run rate is *below* 1/300 (H3) | The budget is $\ln R$, not 10%: a coding-only adaptive count is payable at $R\approx1.2$–3 (hard adaptive selection, soft load) (H3) |
| Day's SNV-only 17.5M is 83% of the directly counted events and brackets the polymorphism-corrected count; his base-pair total is the right order for non-aligned sequence (GAP-07b) | By direct count from the human–chimp alignment, 205M is 9.7× the mutation events per lineage; with the measured polymorphic share (15.6% on the human side) it is 10.6–12.6× the *fixed* events, about 8–13× combined (non-T2T assemblies); the critics' observation-based estimates land within 7–19% (GAP-07b, GAP-07c) |
| On the real ancient-DNA genotypes his start-frequency table reproduces to 0.4 points, and his "completions of near-fixed alleles" reading is right in kind (C1d) | His "21" does not reproduce from his stated method on the real genotypes (thousands; his own documented pipeline is 3.6× off). keruru's measured $N_e$ replicates within 4%, and Day's $N_e \approx 2$ is excluded (C1d) |
| Exact-outcome alternatives are about 1 per needed change; the GB1 landscape is rugged at single-nucleotide steps; "reduce or destroy" holds as worded for deep mutational scans (D1) | 71% of single substitutions keep at least half of function and "destroy" alone is rare; GB1's functional variants form one connected network; within genes the beneficial fraction exceeds G1's requirement for up to ~$2\times10^5$ changes (D1) |

**Still open:**
- Cost of selection at human scale (H3) is decided only conditionally. It flips at an adaptive non-coding share of ~0.01–0.6%, below what any α estimate resolves; $R$ is unsourced; soft selection, absolute-fitness gain and epistasis are untested at human scale.
- Ancient DNA: Day's "21" is contradicted as stated on the real genotypes (C1d), but what it means turns on the Holocene $N_e$. The published estimates ([retrieval](docs/research/sources/holocene-ne.md)) agree on recent growth of 100× or more but disagree on its timing, so the literature does not decide it; C1e will run the model on each published trajectory. A neutral comparison for the damage-resistant transversion class (36–44 events) is also open.
- The ancestral $N_e$ needed to fit the divergence.
- Branch D (sequence space). D1 measured G1's open number: about 1–6 routes per needed change per locus (below the flip of ~7–17), while a gene's shared pool of beneficial mutations clears it for about ten needed changes but not 25 or more. Per-sequence prevalence (Axe, Taylor) and cross-family connectivity are untouched.
- What fraction of the differences needed selection at all ([GAP-01](docs/arguments/README.md#4-what-everyone-missed)). It cuts Day's requirement by 20×–6,000×, yet the adaptive count still exceeds Haldane's rate.

---

## The argument map

```mermaid
flowchart LR
  ROOT(["<b>ROOT</b><br/>No evolutionary mechanism can produce<br/>the human–chimp divergence in the time available"]):::day

  A["<b>A · MITTENS rate limit</b><br/>F_max = t_div·d / (g_len·G_f)<br/><i>G_f reproduces; 205M is bp, ~21M events</i>"]:::mixed
  B["<b>B · Neutral theory insufficient</b><br/>k = μN/Nₑ, empty pipe, Hard Limits<br/><i>k = μ confirmed; pipe was full</i>"]:::critic
  C["<b>C · Ancient DNA: zero fixations</b><br/>1240k panel, turnover d<br/><i>21 contradicted as stated on real data;<br/>meaning turns on Holocene Nₑ</i>"]:::mixed
  D["<b>D · Sequence space</b><br/>10³²⁵ vs 10⁵² (Wistar 1966)<br/><i>~1 route per locus; gene pools shared;<br/>prevalence untouched</i>"]:::mixed
  E["<b>E · LTEE / punctuated</b><br/>mutator hazard, relictation<br/><i>numbers reproduce; consequence untested</i>"]:::mixed
  F["<b>F · Kimura irrelevance</b><br/>fixation time vs fixation rate<br/><i>latency ≠ throughput</i>"]:::critic
  G["<b>G · Bernoulli barrier</b><br/>0.02^(2×10⁷), ~230 parallel sweeps<br/><i>prices a specific list; no 230 cap</i>"]:::critic
  H["<b>H · Cost of selection</b><br/>Haldane 1/300<br/><i>shared budget holds; its size is ln R;<br/>turns on adaptive share and R</i>"]:::open

  ROOT --> A & B & C & D & E & F & G & H

  classDef day fill:#fde2c8,stroke:#b45309,stroke-width:3px,color:#111
  classDef critic fill:#dbeafe,stroke:#1d4ed8,color:#111
  classDef mixed fill:#ede9fe,stroke:#6d28d9,color:#111
  classDef open fill:#fef9c3,stroke:#a16207,color:#111
  classDef todo fill:#e5e7eb,stroke:#6b7280,color:#111,stroke-dasharray:4 3
```
<sub>🟧 Day's root · 🟦 resolved mostly for the critics · 🟪 mixed · 🟨 open · ⬜ not yet checked. Each branch is drawn in full, claim by claim, in [`docs/research/hierarchy/`](docs/research/hierarchy/README.md).</sub>

**The same arguments, read as a philosopher would:** [`docs/arguments/`](docs/arguments/README.md) gives the root argument in standard form, every objection typed as undermining, undercutting or rebutting, a dated family tree showing how each argument changed on both sides since 1966, and seven gaps neither side has closed.

---

## The math, checked

Each result below links to its check script. All numbers come from reviewed runs ([`RESULTS.md`](research/checks/RESULTS.md)).

### 1 · MITTENS: Day's headline bound
```math
F_{\max} \;=\; \frac{t_{\text{div}}\cdot d}{g_{\text{len}}\cdot G_f}
\qquad
\begin{aligned}
t_{\text{div}} &= 6.3\ \text{My},\; g_{\text{len}} = 25\ \text{y} \;\Rightarrow\; 252{,}000\ \text{gens}\\
G_f &= 1{,}322\ \text{gens per fixation (LTEE throughput)}\\
\text{required} &= 2.05\times10^{8}\ \Rightarrow\ \text{shortfall} \approx 10^{6}\times
\end{aligned}
```
The parameters drift between versions (2019 → 2025 → 2026; see [`ledgers/versions.md`](docs/research/ledgers/versions.md)). The dispute is over three inputs:
- **Numerator:** how many fixations are actually required. Counting base pairs gives 205M; a direct count of mutation events in the human–chimp alignment gives about 21M per lineage, of which SNVs are about 19M (17.5M on CSAC's figure).
- **$G_f$:** whether an asexual bacterial throughput transfers to a sexual, recombining, much larger genome.
- **$d$:** the turnover coefficient.

### 2 · Neutral substitution rate: why $k = \mu$
```math
k \;=\; \underbrace{2N\mu}_{\text{new mutants / gen}} \times \underbrace{\tfrac{1}{2N}}_{P_{\text{fix}}} \;=\; \mu
\qquad\text{vs Day:}\quad k = \mu\,\frac{N}{N_e}
```
<details><summary><b>Proof sketch</b>: fixation probability is set by census N, not Nₑ</summary>

In any exchangeable (Cannings) model, the frequency $p_t$ of a neutral allele is a martingale: $E[p_{t+1}\mid p_t]=p_t$. It is bounded and absorbs at 0 or 1, so $P(\text{fix}) = E[p_\infty] = p_0 = 1/2N$ **for any offspring variance**. Offspring variance lowers $N_e$, which speeds up *time to absorption* ($\bar t_{fix} \approx 4N_e$) but leaves its *probability* unchanged. Check `b3_N_vs_Ne.py`: across $N_e$ = 200 → 19, $P_{fix}$ stays at $0.0025 = 1/M$ while $t_{fix}/N_e \approx 4$.
</details>

### 3 · The "empty pipe": Day's formula is right, but its premise is not
```math
E[F(T)] \;=\; \mu L \int_0^T F_X(u)\,du \;\xrightarrow{T\gg 4N_e}\; \mu L\,(T - 4N_e)
\qquad\text{(empty start)}
\qquad\qquad
E[F(T)] = \mu L\,T \qquad\text{(equilibrium start)}
```
<p align="center"><img src="docs/img/b1_pipeline.svg" alt="Empty vs equilibrium start" width="620"></p>

<details><summary><b>Proof sketch</b></summary>

$\int_0^T F_X(u)\,du = T - E[\min(X,T)] \to T - E[X]$, and $E[X]\approx 4N_e$ (Kimura–Ohta). So the deficit is exactly the mean transit time: mutations that arose before $t=0$ are missing from the pipe. Starting from mutation–drift equilibrium, the pipe already carries in-flight alleles. These drain at rate $\mu L$ while new ones enter at rate $\mu L$, so the expected number of fixations in $[0,T]$ is $\mu L T$ (flux balance, or Little's law). Real ancestral populations carry standing variation, so the empty start is a counterfactual boundary case. Day has since withdrawn it (claim B1d). `b1_start_state.py`
</details>

### 4 · Changing population size: a transient, in **both** directions
```math
\frac{K}{U\,T} \;\approx\; 1 + \frac{4\,(N_{\text{old}}-N_{\text{new}})}{T}
```
<p align="center"><img src="docs/img/b1b_demography.svg" alt="Size-change identity" width="620"></p>

The in-flight inventory is $\approx U\cdot 4N$. After a size change it relaxes to $U\cdot 4N_{\text{new}}$, and the difference comes out as extra fixations or missing ones.
- **Expansions** produce a deficit, which is Day's direction.
- **Contractions** produce an excess.

With sourced human and chimp $N_e$ histories (Yoo 2025, Prado-Martinez 2013), every history tested gives an **excess**: $K/UT$ = 1.9–4.0 (`b1c_ne_history.py`).

### 5 · Divergence is not fixations: ancestral polymorphism
```math
E[d] \;=\; 2\mu T \;+\; \underbrace{4N_{e,\text{anc}}\,\mu}_{\theta_{\text{anc}}}
```
<p align="center"><img src="docs/img/b4a_divergence.svg" alt="Divergence vs ancestral Ne" width="620"></p>

Two sampled genomes coalesce on average $2N_{e,\text{anc}}$ generations *before* the split. That adds $2\mu\cdot 2N_{e,\text{anc}}$ to their expected divergence. The forward simulation matches this within 0.3% (`b4a_two_lineage_ils.py`).

Neither side gets a free pass from the data:
- **Yoo 2025's ancestral node** overshoots the observed 1.23% by about 25%.
- **$N_e$ = 10⁴** gives only half the observed value.
- **The fit** needs $N_{e,\text{anc}}\approx 130$k, or a different $\mu$ or $T$. It has three parameters, so the external verdict is *contested*.

### 6 · Hard Limits: a correct tail exponent, but a latency
```math
P\big(\text{fix within } G \mid \text{fix}\big) \;\approx\; \exp\!\left(-\frac{\pi^2 N_e}{G}\right)
\quad\text{(leading order; exact chain gives prefactor} \approx 50\,(G/N)^{-1.5})
```
Exact Wright–Fisher chains confirm the $-\pi^2$ exponent (`b2a_hard_limits_chain.py`). This is a per-allele *latency* tail, though. Total throughput is $U\!\int F$, which equals $UT$ at equilibrium.

### 7 · Interference: where the parallel-sweep cap lives
<p align="center"><img src="docs/img/f2_interference.svg" alt="Clonal interference vs recombination" width="620"></p>

$R_{\text{int}}$ = (realised rate) / (independent-sites rate).
- **Asexual populations** collapse to 0.09 as supply rises. This is the regime the LTEE measures.
- **Free recombination** holds 0.975 with 272 sweeps in flight. Validated in fwdpy11 (`f2_multilocus.py`, `f2_fwdpy11.py`).
- **Caveat:** tested only at N = 1000, s = 0.01 and soft selection. Human-scale active loci are not tested.

### 8 · Cost of selection: Haldane's 1/300 as a special case
```math
\underbrace{\lambda \cdot D}_{\text{selective deaths / gen}} \;<\; \ln R
\qquad D \approx \ln M + 1
\qquad\text{Haldane: } \frac{\ln R}{D}\approx\frac{0.1}{30} = \frac{1}{300}
```
<p align="center"><img src="docs/img/h2_persistence.svg" alt="Hard-selection persistence" width="620"></p>

Under hard selection, a population with maximum fecundity $R$ survives only while the cost it pays per generation stays below $\ln R$. In the tested grid ($R\ge1.3$) it sustains 9–120× Haldane's rate (`h2_hard_selection_multilocus.py`). Soft selection does not remove the cost in the audit's reconstruction; the soft-selection runs are in fact slower.

**At human scale** (H3, `h3_human_scale.py`, conditional on hard adaptive selection with a soft deleterious load):
- Day's structure holds: concurrent sweeps share one budget.
- At Haldane's assumed $R \approx 1.1$ the rate is ≈ 1/300 over 10,000 generations but only ≈ 1/530–1/1,050 over the 252,000-generation lineage, because load fluctuations eat 27–70% of the cap.
- The minimum $R$ for $10^3$ / $10^4$ / $10^5$ adaptive substitutions is 1.2 / 3.0 / 5×10⁴.
- So a coding-only adaptive count fits at plausible $R$. An adaptive non-coding share of 1% or more does not. Day's 17.5M–205M fail under any cost model.

The flip sits below what any α estimate can resolve, and no sourced net hominid $R$ exists, so **H stays open**.

### 9 · Fixation time of a beneficial mutant
```math
\bar t_{\text{fix}} \;\approx\; \frac{2}{s}\left(\ln 4Ns + \gamma\right)
\qquad\text{vs Day's}\qquad \frac{2}{s}\ln 2N
```
At Day's parameters ($N = 10^4$, $s = 0.001$), the simulation and diffusion give 8,480 generations, against 19,807 from his approximation. That approximation is standard but deterministic. It overstates the conditional fixation time by 2.3× (`beneficial_fix_time.py`).

**Fairness audit (X1).** The R5 draft found 22 of 112 Day claims with an "arithmetic error" or "doesn't follow" verdict against 0 of 51 critic claims. The audit then wrote [one verdict rule](research/checks/results/R4-X1-verdict-rule.md) for both sides, re-scored every numeric claim, and had the rule's application checked blind:

| Error verdicts (counts) | Day | Critics |
|---|---|---|
| claims with a number in the author's quoted words (primary) | 13 of 81 | 1 of 20 |
| claims with a number in the formal statement | 16 of 82 | 1 of 31 |
| all claims | 18 of 114 | 1 of 51 |

Raw counts per side are shown, but rates are not comparable between sides: the two sides differ in volume, in the precision of their claims, in the share of claims checked, and in how claims were routed (method audit MA-06, [`METHOD-AUDIT-2026-10-12.md`](docs/research/criticality/METHOD-AUDIT-2026-10-12.md)). No test of difference is reported.

---

## Roadmap

Everything outstanding (compute and checks, criticality remediation, owner decisions, outside inputs, and the path to R5) is one table in [`docs/research/ROADMAP.md`](docs/research/ROADMAP.md). The research stages:

```mermaid
flowchart LR
  R0["R0<br/>Scaffold"]:::done --> R1["R1<br/>Corpus<br/>154 posts · 32 Zenodo<br/>37 papers · 48 critic/ally sources"]:::done
  R1 --> R2["R2<br/>233 claims<br/>verbatim + sourced"]:::done
  R2 --> R3["R3<br/>Argument tree<br/>33 load-bearing nodes"]:::done
  R3 --> R4["R4<br/>Math resolution<br/>54 checks reviewed"]:::active
  R4 --> R5["R5<br/>Synthesis<br/>verdicts · sensitivity<br/>variable list"]:::todo
  R5 --> S1["Simulator<br/>spec → plan"]:::todo
  S1 --> S2["evo-sim<br/>user-controllable<br/>forward sim"]:::todo

  classDef done fill:#dcfce7,stroke:#15803d,color:#111
  classDef active fill:#fef9c3,stroke:#a16207,stroke-width:3px,color:#111
  classDef todo fill:#e5e7eb,stroke:#6b7280,color:#111,stroke-dasharray:4 3
```

**R4 remaining**
- [x] **E:** hypermutator hazard per founder; exact chains for relictation (Cannings)
- [x] **G1:** what $0.02^{2\times10^7}$ prices: a *specific* outcome or *any* outcome
- [x] **Gaps:** finite-map cap fit (GAP-04), indel/SV event counts (GAP-07), sweep-scan windows (GAP-02)
- [x] **H3:** cost of selection at human scale (long-run hazard, finite supply, hard load at K ≥ 4000)
- [x] **GAP-07b:** direct event count from the human–chimp alignment (9.7×, bracket ~7–14×; follow-ups GAP-07c and a T2T re-run)
- [x] **C1c / C1d:** Day's aDNA 21-count with real call depth and ancestry replacement (model), then on the real AADR genotypes (contradicted as stated; keruru's $N_e$ replicates)
- [x] **D1:** sequence-space spike (RNA folding, deep mutational scans, GB1): alternatives per needed change against G1's flip
- [x] **X1:** arithmetic of every critic and ally claim, and one verdict rule applied to both sides (the "blind audit" was by a same-model agent, not an independent party; see Known gaps)
- [x] **GAP-07c:** polymorphic share of the divergent sites (15.6% human side; 205M is 10.6–12.6× fixed events)
- [x] **Mapping:** every critic and ally argument attached to the map (12 new claims from the Hancock video, pending review); Holocene $N_e$ literature retrieved
- [ ] **In progress:** XT (cross-tool replication), D15 (regulatory waiting time)
- [ ] **Queued:** C1e (the C1c model on published Holocene trajectories), Mansfield's supply argument, latency vs throughput, Hancock's standing-variation prediction
- [ ] **D follow-ups:** per-sequence prevalence (Axe, Taylor, Keefe–Szostak), multi-mutant decay, a noise null for the beneficial proxy
- [ ] **C follow-ups:** a transversion-matched neutral model; what the transition excess is
- [ ] **H follow-ups:** soft-selection rate limit and epistasis at human $R$; a sourced beneficial DFE and $M$; CIs on T50
- [ ] **Sources:** Yoo 2025's $\mu$, to rescale $N_{e,\text{anc}}$. Verify Takahata 1995, Charlesworth 2009 and the Haak 2015 panel design

**R5:** final verdicts, a sensitivity table, the simulator variable list and a published summary. The [ELI5 / ELI8 / ELI10 / ELI12 / ELI18 explainers](docs/explain/README.md) exist as drafts and get a final pass after R5.

**Simulator knobs (draft):**
- Population: $N$, $N_e$, offspring variance, sexual vs asexual, demography over time, start state
- Mutation: $\mu$, genome length $L$, mutators
- Selection: distribution of $s$ (including negative), dominance, hard vs soft selection
- Recombination: map length
- Generations: generation time, overlapping generations
- Counting: the divergence-counting rule

---

## Repo layout
| Path | What |
|---|---|
| [`docs/research/`](docs/research/README.md) | The audit: rules, glossary, `parameters.yaml`, claim files, argument tree and ledgers (fidelity, balance, contradictions, versions) |
| [`docs/arguments/`](docs/arguments/README.md) | Argument map: standard forms, typed objections, genealogy, gaps and prior art |
| [`docs/research/claims/`](docs/research/claims) | One file per claim, with a verbatim quote, formal statement, pre-registered prediction and three verdicts |
| [`research/checks/`](research/checks) | Reviewed verification scripts, with [`RESULTS.md`](research/checks/RESULTS.md) and [`REVIEW.md`](research/checks/REVIEW.md) |
| `research/checks/results/` | Write-ups, reviews and raw outputs |
| [`research/tools/`](research/tools/README.md) | Harvest and claim-generation tooling, plus `readme_figs.py`, which draws the figures above (including the audit systems, verdict-logic and roadmap diagrams), and `icon.py` / `icon_raster.py`, which draw the icon, favicon and social preview |

## Reproduce
```bash
python3 -m venv research/.venv
research/.venv/bin/pip install -r research/requirements.txt matplotlib
research/.venv/bin/python -I research/checks/baseline_textbook.py     # textbook baselines, must pass first
research/.venv/bin/python -I research/checks/b4a_two_lineage_ils.py   # any check; seeds are fixed
research/.venv/bin/python -I research/checks/lint_research.py         # claims ↔ tree ↔ provenance lint
research/.venv/bin/python -I research/tools/readme_figs.py            # regenerate docs/img/*.svg
research/.venv/bin/python -I research/tools/icon.py && research/.venv/bin/python -I research/tools/icon_raster.py  # icon, PNG sizes, favicon.ico, social-preview.png
```

## Ground rules
- **Verbatim quotes only.** Each has a locator and a date. A claim known only through an opponent is tagged `secondhand`.
- **Pre-registered predictions.** Every number traces to `parameters.yaml`, a quote, or a stated derivation.
- **No question-begging.** Forward simulations decide; the coalescent is used only for baselines. Scaling is validated before it is used.
- **No full texts in git** (copyright). Only links, short quotes and sha256 hashes.
- **Corrections welcome from either side.** If a quote is wrong, a check is unfair to its author, or a number is misattributed, open an issue with the locator.

# Conflict-of-interest statement and licence recommendation (draft)

> **DRAFT — not sent; owner approval required for text and channel.** Nothing in this file has been sent, posted or submitted anywhere (AGENTS.md hard rule 6).

Fills the "Interests" paragraph of [`METHODS-AND-LIMITATIONS.md`](../METHODS-AND-LIMITATIONS.md). **Every blank is for the owner; the agents do not know these facts and must not guess them.** Nothing in the repository records them.

## 1. COI statement template (owner to complete, in the owner's own words)

**Who runs the project.** [OWNER: name or handle, and whether you want it public.]

**Funding.** [OWNER: who pays for compute, model access and time? Any grant, employer, or sponsor? "No external funding" if that is the case.]

**Relationship with Vox Day or his publishers.** [OWNER: none / reader / purchaser / correspondent / other. State any contact ever made, any purchase of his books.]

**Relationship with any critic or ally named in the audit** (McCarthy, Hancock, Gutsick Gibbon, Camestros Felapton, keruru, Myers, Hössjer, Dembski, others). [OWNER: none / follower / correspondent / other.]

**Prior public positions.** [OWNER: have you said anything publicly for or against Day's argument, for or against evolution, or on the parties? Where?]

**Personal stakes.** [OWNER: professional training in biology, mathematics or statistics; religious or political commitments you think a reader should know; any commercial interest.]

**The project icon** (flagged in the method audit MA-19). [OWNER: what the icon is and why chosen.]

**The AI vendor.** The audit's author and reviewers are Anthropic Claude models run through Claude Code. [OWNER: any relationship with Anthropic beyond being a customer.] The models are not neutral parties in the sense of a human reviewer: they may share biases about what counts as a reasonable premise, and a model asked to be even-handed may overcorrect either way. The audit says so on the limitations page.

**What the owner has decided.** Rule and process decisions are listed in [`DECISIONS.md`](../DECISIONS.md); the owner's reply to the open decisions is recorded there verbatim.

## 2. Licence recommendation (no LICENSE file added; owner to choose)

| Part | Recommended licence | Why |
|---|---|---|
| Prose, claim files, ledgers, argument maps, posts (`docs/`) | **CC BY 4.0** | Anyone may quote, translate or reuse with attribution, which is what an audit wants; it asks for credit, not agreement. Authors who are audited cannot be blocked from quoting the verdicts about them. |
| Data tables, parameters, results (`parameters.yaml`, `results/`, `raw/` summaries) | **CC BY 4.0** (or CC0 for pure numeric tables) | Easy reuse and re-computation; CC0 removes attribution friction for numbers that are facts. |
| Check scripts and tools (`research/checks/*.py`, `research/tools/`) | **MIT** | Short, permissive, standard for research code; lets others re-run and extend checks. Apache-2.0 is an alternative if a patent grant is wanted. |
| Interactive explainers (`docs/explain/`) | **CC BY 4.0** for text, **MIT** for the page code | Mixed content; the split follows the two rows above. |
| Quotes from others' work | **Not relicensed.** Short quotes with locators only, under fair use/quotation; `sources/raw/` is gitignored and never published. | Hard rule 3: no full texts in git. A licence on the audit cannot cover other people's words. |

**Points for the owner to settle before adding a LICENSE file**
1. Whether to attach one licence to the whole repository (simplest: CC BY 4.0 for content and MIT for code, stated in a top-level `LICENSE` and in a `LICENSES.md` mapping directories) or per-directory files.
2. Whether the licence covers text written by Claude. The owner should check the vendor's terms on output ownership; the agents have not examined them.
3. Whether to require attribution that names the project, not only the owner.
4. Copyright holder name for the notice.
5. Whether to add a no-endorsement line ("use of this material does not imply the audited authors agree with it").

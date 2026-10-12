> **DRAFT — not sent; owner approval required for text and channel.** Nothing in this file has been sent, posted or submitted anywhere (AGENTS.md hard rule 6). The recipient list, the verdict summaries and the wording are drafts for the owner to edit. Per-recipient claim lists were generated on 2026-10-12 from the claim-file front matter; regenerate them before sending, because verdicts change.

# Right of reply: Vox Day (draft)

## Template letter (edit; one per recipient)

**Subject:** A public audit of the mathematics in the Probability Zero debate: your claims, and a request for corrections

Dear [NAME],

I am writing on behalf of [OWNER NAME], who runs an open audit of the mathematical arguments in the debate over *Probability Zero* and the replies to it. I would like to give you the chance to correct what the audit says about you before it is finalised.

**What this is.** The audit is carried out by AI models (Claude instances) under the direction of one human owner. It reads the published arguments of both sides, tags each claim as argument or rhetoric, recomputes the numbers, and gives each claim three verdicts: whether it follows from its own premises (internal), whether it reads its sources correctly (fidelity), and whether it matches the outside evidence (external). The same rule is used for every author. It is not a peer review, no human expert has reviewed it, and it may be wrong. Its limits are set out here: [LINK: docs/research/METHODS-AND-LIMITATIONS.md]. All of it is public: [REPO LINK].

**What it says about your claims.** [N] claims of yours are in the audit. Findings in your favour and against you are listed below with their locators and the verdict on each. [PASTE the recipient's row and claim list; for each unfavourable verdict, name the quote, the locator, and the recomputation.]

**What I am asking.** Please tell us where the audit has misquoted you, misread you, used a number you did not use, chosen a reading of your words that is not the one you meant, or missed a point you made elsewhere. A short reply is enough. Corrections with a locator are the most useful.

**What will happen to your reply.**
- You have 21 days from [DATE SENT] to reply. Replies after that are still read and will be added, but the 21-day set is the one used for the first finalised version.
- Your reply will be published verbatim, next to the verdict it concerns, unless you ask us to withhold a specific private detail.
- A reply can change a verdict. If it does, the change and the reason will be recorded with the date, in the open.
- Silence is not treated as agreement. A claim with no reply is marked "no reply received" and its verdict stands as written, with the limits stated above.
- Nothing in your reply will be used in a way you were not told about, and you may withdraw a reply before publication.

You are under no obligation to respond. Thank you for your time.

[OWNER NAME] / [CONTACT PLACEHOLDER chosen by the owner]

## Recipient table

| Who | Claim files | Channel recorded in the repository | Notes |
|---|---|---|---|
| Vox Day (Theodore Beale) | 130 (side: day) | Public blog [voxday.net](https://voxday.net/) (the source of most of the quotes; see `sources/bib-day.md`). **No contact address or comment channel is recorded, and none was searched for.** The owner chooses the channel. | The Zenodo paper "The Hard Limits of Fixation Through Genetic Drift" (Z22129121) is credited to "Day & Athos"; whether a second recipient is wanted is for the owner. Several Day claims come from blog comments and replies; the audit's rule scores those as ledger entries only. |

## What the audit says about Vox Day's claims (counts from claim-file front matter, 2026-10-12)

Not a score: a reader's guide. The three verdicts are not summed.

**Unfavourable to Day**
- Internal verdict `arithmetic-error` (2): A5h, B6a.
- Internal verdict `non-sequitur` (17): A2e, A5d, B, B3c, B3e, C, C2, C2b, C2c, C6, C7, D9a, DN4, F1a, G2g, G3b, Gc.
- Fidelity `misread` (9): A3a, B3a, B3c, B3d, D2b, D2j, D3c, F3a, H9.
- External `contradicted` (16): A2e, B3, B3a, B3c, B3d, B3e, B3f, B6a, B9, C2c, C6, C7, DN1, DN2, DN3, FM8b. DN1 to DN3 are conditional on a pending check (L1b), per the 2026-10-12 comments in their claim files.

**Favourable to Day**
- Internal `holds` (65 claims), among them the load-bearing A, A3, B1, B2, B2b, B3a, B3g, C2a, E6, F, F2, F3a, H, H1, H8.
- External `supported` (10): A1, A3b, A6a, B3b, B3g, D7, FM3, FM4, FM5, H1.
- Fidelity `accurate` (9): A1, A5d, B3g, B3m, D2c, E, E4, Ga, Gd.
- Verdicts recorded as dependent on how a quote is read (rule RD) take the reading most defensible to the author, with the other readings listed in the claim file.

**Load-bearing nodes** (24; if one fails the audit's tree for the thesis is affected): A, A2e, A3, B, B1, B2, B2b, B3, B3a, B3g, C2, C2a, E6, F, F1a, F2, F3a, FM10, H, H1, H8, ROOT-M, ROOT-FM, ROOT.

**Not decided yet.** Many claims are `pending` or external `contested`; the audit has not yet checked them. The limitations page says why that is not a point for either side.

**Where the audit is weakest in his favour or against him.** *Probability Zero* itself has not been read (the book-only claims are scored `secondhand`); the audit has so far used the Zenodo papers and blog posts. The audit's own checks are pre-registered, but the reviewers are the same model family as the author. A reader on Day's side can fairly press both.

### Appendix: every Day claim with its three verdicts (internal / fidelity / external)

- A: holds / n/a / contested  (load-bearing)
- A1: holds / accurate / supported
- A1c: pending / unverifiable / pending
- A2: holds / unverifiable / contested
- A2a: holds / unverifiable / pending
- A2b: holds / unverifiable / pending
- A2e: non-sequitur / pending / contradicted  (load-bearing)
- A2f: pending / unverifiable / pending
- A2j: holds / pending / contested
- A3: holds / partial / contested  (load-bearing)
- A3a: holds / misread / contested
- A3b: holds / partial / supported
- A3z: holds / partial / contested
- A4: holds (hazard-scale s) / n/a / contested
- A4a: holds / unverifiable / contested
- A4d: holds / n/a / pending
- A4g: holds / unverifiable / contested
- A5d: non-sequitur / accurate / contested
- A5e: holds / unverifiable / pending
- A5g: pending / unverifiable / pending
- A5h: arithmetic-error / n/a / pending
- A6: pending / partial / contested
- A6a: holds / unverifiable / supported
- B: non-sequitur / partial / contested  (load-bearing)
- B1: holds / n/a / contested  (load-bearing)
- B1a: holds / n/a / pending
- B1b: holds / n/a / pending
- B1d: pending / unverifiable / contested
- B1e: pending / partial / pending
- B2: holds / unverifiable / contested  (load-bearing)
- B2a: holds / unverifiable / pending
- B2b: holds / unverifiable / contested  (load-bearing)
- B2c: holds / unverifiable / contested
- B2d: holds / n/a / pending
- B3: pending / partial / contradicted  (load-bearing)
- B3a: holds / misread / contradicted  (load-bearing)
- B3b: holds / partial / supported
- B3c: non-sequitur / misread / contradicted
- B3d: holds / misread / contradicted
- B3e: non-sequitur / n/a / contradicted
- B3f: holds / n/a / contradicted
- B3g: holds / accurate / supported  (load-bearing)
- B3h: pending / n/a / contested
- B3m: n/a / accurate / contested
- B4: holds / unverifiable / contested
- B4b: holds / unverifiable / contested
- B4c: pending / unverifiable / pending
- B4d: pending / partial / contested
- B6a: arithmetic-error / n/a / contradicted
- B9: holds / unverifiable / contradicted
- C: non-sequitur / n/a / contested
- C1a: holds / n/a / contested
- C2: non-sequitur / unverifiable / contested  (load-bearing)
- C2a: holds / unverifiable / contested  (load-bearing)
- C2b: non-sequitur / unverifiable / pending
- C2c: non-sequitur / n/a / contradicted
- C2d: holds / unverifiable / contested
- C3: pending / unverifiable / pending
- C4: pending / pending / pending
- C5a: pending / n/a / pending
- C6: non-sequitur / unverifiable / contradicted
- C7: non-sequitur / n/a / contradicted
- D: pending / partial / contested
- D2: pending / unverifiable / pending
- D2a: n/a / partial / contested
- D2b: n/a / misread / contested
- D2c: pending / accurate / contested
- D2d: n/a / partial / contested
- D2e: holds / partial / contested
- D2f: n/a / partial / contested
- D2g: pending / partial / contested
- D2h: pending / unverifiable / contested
- D2i: holds / n/a / contested
- D2j: n/a / misread / contested
- D2l: holds / unverifiable / contested
- D3c: pending / misread / contested
- D7: holds / partial / supported
- D7a: holds / unverifiable / contested
- D7b: holds / unverifiable / untestable
- D9: holds / n/a / contested
- D9a: non-sequitur / n/a / contested
- DN1: pending / n/a / contradicted
- DN2: pending / n/a / contradicted
- DN3: holds / partial / contradicted
- DN4: non-sequitur / n/a / contested
- DN6: pending / pending / pending
- E: holds / accurate / pending
- E10: holds / partial / contested
- E2: pending / pending / pending
- E3: holds / unverifiable / contested
- E4: holds / accurate / contested
- E6: holds / unverifiable / pending  (load-bearing)
- E7: pending / pending / pending
- F: holds / partial / contested  (load-bearing)
- F1a: non-sequitur / n/a / pending  (load-bearing)
- F2: holds / n/a / contested  (load-bearing)
- F3: holds / partial / contested
- F3a: holds / misread / contested  (load-bearing)
- F4a: holds / n/a / pending
- F5: holds / unverifiable / n/a
- F6: pending / unverifiable / pending
- FM10: pending / n/a / contested  (load-bearing)
- FM3: holds / unverifiable / supported
- FM4: n/a / n/a / supported
- FM5: holds / unverifiable / supported
- FM7: n/a / n/a / contested
- FM8b: n/a / n/a / contradicted
- G: holds / partial / contested
- G1: holds / n/a / contested
- G1a: holds / unverifiable / contested
- G2g: non-sequitur / n/a / contested
- G3b: non-sequitur / n/a / contested
- G4: holds / n/a / n/a
- G4b: pending / n/a / pending
- Ga: holds / accurate / contested
- Gb: holds / n/a / contested
- Gc: non-sequitur / n/a / contested
- Gd: holds / accurate / pending
- Ge: pending / n/a / pending
- H: holds / partial / contested  (load-bearing)
- H1: holds / partial / supported  (load-bearing)
- H10: pending / n/a / pending
- H3: pending / unverifiable / pending
- H4: pending / unverifiable / contested
- H8: holds / pending / contested  (load-bearing)
- H9: pending / misread / pending
- ROOT-B: n/a / n/a / pending
- ROOT-M: pending / n/a / pending  (load-bearing)
- ROOT-FM: pending / pending / contested  (load-bearing)
- ROOT: pending / n/a / pending  (load-bearing)

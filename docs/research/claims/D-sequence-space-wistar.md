---
id: D
title: "Functional proteins are a vanishing fraction of sequence space (about 1e52 proteins ever vs 1e325 sequences), and the Wistar challenge was never answered quantitatively"
side: day
branch: D
parent: ROOT
edges: [{type: supports, target: ROOT},{type: depends-on, target: D3},{type: depends-on, target: D4},{type: depends-on, target: D5},{type: depends-on, target: D2g},{type: attacks, target: D1}]
load_bearing: false  # ROOT has independent routes (A, B, G); D is a separate sequence-space route and a historical-priority claim; ROOT does not require D
sourcing: firsthand
status: extracted
verdicts:
  internal: pending      # conclusion (evolution cannot search the space) needs a landscape-structure premise that D does not state
  fidelity: partial      # Eden's 20^250 reproduces; Eden's 10^52 counts protein molecules, not functional proteins; Waddington conceded the minute-fraction premise
  external: contested      # functional-fraction estimates differ by ~53 orders of magnitude (Axe vs Taylor) and landscape structure is disputed
---

## Statement (verbatim)
> "Eden had already shown this: the space of 250-residue proteins is ~10^325, and the number of functional proteins that have ever existed is ~10^52."

Source: [The Best They've Got I](https://voxday.net/2026/10/05/the-best-theyve-got-i/), 2026-10-05, voxday.net, para 29 of extracted text (Day's summary of Eden; the blog attributes the 10^325 and 10^52 to Eden).

> "Eden calculated the size of sequence space. No one calculated a smaller space. Ulam calculated a rate. No one calculated a faster rate. Schützenberger asked for a mechanism. No one demonstrated one."

Source: same, para 26.

> "But the space of possible genetic sequences is unimaginably vast, the proportion of functional sequences within that space is vanishingly small, and the time available for the process to take place is insufficient for random search to find what needs to be found."

> "The biologists did not answer the mathematicians. They could not."

> "There is not one single example of a biologist producing one single calculation that even attempts to contradict the mathematicians’ conclusions."

Source for the three quotations above: [Vox Day Interview on Evolutionary Theory](https://billdembski.substack.com/p/vox-day-interview-on-evolutionary) (Dembski Substack), 2026-09-28, appended chapter 'From Probability Zero (2nd ed.) on 1966 Wistar Symposium, Chapter 6: The 1966 Meeting of the Minds' (posted with Day's permission; primary Day text). The chapter is Day's own fullest statement of D in the corpus (first-edition text not retrieved; the 2nd edition may differ).

The primary source for the two numbers is Eden, Wistar p.7 (see D3).

## Formal statement
Let L = 250, A = 20. Sequence space `S = A^L = 10^(250*log10 20) = 10^325.257`. Eden's upper bound on protein molecules that ever existed on Earth: `N_ever = 10^52` (Wistar p.7). Ratio `N_ever/S = 10^-273.3`.

D as Day uses it has two parts: (1) a size comparison S >> N_ever (arithmetic); (2) the historical claim that no Wistar biologist produced a counter-calculation (D2g). The step from (1) to 'evolution cannot work' is not in the sentence quoted; Eden states it needs one of two hypotheses (D3b): either functional proteins are common, or the topology of the space provides paths. Day adds the second horn: functional proteins are isolated (rugged landscape), citing Wald (D2c) and deep mutational scanning (D2h, unsourced). Derived expected-hit calculations (this file): hits = N_ever * f for fraction f functional; f = 1e-77 (Axe 2004, one beta-lactamase-type domain, any fold) gives 1e-25; f = 2e-24 (Taylor 2001, derived from the 5e23 library estimate for a 100-residue chorismate mutase) gives 2e28. These are different proteins and different lengths and are not comparable; they are shown only to display the spread.

## Assumptions
- Stated (Day): sequence space is searched by variation plus selection; functional proteins are rare; no biologist at Wistar produced a quantitative reply.
- Implicit: (i) the relevant search is for novel protein folds or de novo functions, whereas the human-chimpanzee divergence that anchors ROOT is mostly 35M single-nucleotide differences; the link between D and A-H is not made in the retrieved text; (ii) the landscape is rugged (isolated functional islands); (iii) numbers for the number of molecules, not distinct sequences, set the exploration budget; (iv) no reuse of existing domains.
- Implicit in Eden: the explored part of the space is 'all useful proteins which have existed to date' (p.7), i.e. the set has been used, not just sampled.

## Responses
- Against: Wright (D6, Wistar p.117): selection makes the search ~log, not linear; Eden replied (p.8) that Wright had misunderstood the argument and that path length is the issue. Ulam (D4a, p.21): random construction 'is not the problem'. Waddington (p.93, D2e): the part explored is 'quite large in comparison with all the things that could conceivably be made out of it in single steps', while granting the meaningful space is 'a minute fraction of the total nucleotide space'. Rosenhouse (D1; ch.4; secondhand). Camestros (D1d). Taylor 2001 and Keefe & Szostak 2001 measured functional frequencies in random libraries (D11, D12).
- In support: Wald (p.19, D2c): changes in hemoglobin rarely leave function untouched; Schützenberger (D5): a 'gap' between sequence space and organism space; Axe 2004 (D10): 1 in 10^77.
- Weaknesses in the responses: Wright's analogy is explicitly 'not a perfect analogy' and needs a fitness signal at each step; Waddington's and Lewontin's claims are assertions (no data at the symposium). On the Day side: Day's reading of Wistar silence ('No one calculated a smaller space') is contradicted in part: Wright p.117 gives a calculation (1250 questions) and p.119 gives a mutation-supply figure (D2g); and the 10^52 figure counts molecules, not functional proteins (D3a). Day's own chapter 6 (2nd ed., Dembski Substack) also contains quotations or attributions that do not match the volume: Lewontin's 'quasi-continuity ... I don't know' exchange and the Levins/Lewontin attribution (D2b), Mayr's 'The very fact that we have this conference' (D2f), a Bossert remark attributed to Eden (D2j), Eden's biosphere inputs (D3a) and Eden's hemoglobin result ('vastly exceeds' vs 'not implausible', D3c). These affect the fidelity of the historical half of D, not the arithmetic.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Eden (Wistar p.7) | 20^250 = 10^325; molecules ever = 10^52; 'species of protein molecules ... say 10^40' | accurate numbers; wording differs from Day's 'functional proteins' (partial) |
| Waddington (Wistar p.93) | meaningful space 'a minute fraction of the total nucleotide space' | accurate; Day omits this concession (D2e) |
| Axe 2004 (abstract) | 'roughly one in 10(64) signature-consistent sequences'; 'as low as 1 in 10(77)' | accurate (abstract only) |
| Taylor 2001 | ~5e23 library needed for chorismate mutase in a fully randomized 100-mer | accurate (D11) |
| Keefe & Szostak 2001 (abstract) | four ATP-binding proteins from 6e12 random 80-mers; frequency 'similar to ... RNA libraries' | abstract only (D12) |

## Pre-registered prediction
Written before the S1/S2 checks below.
- Under the claimant's model (rugged, isolated functional islands): in NK-type landscapes with high K, adaptive walks from random starts terminate at local optima well below the global optimum and the fraction of reachable high-fitness sequences from a random start collapses with N; reaching function from random sequences scales like 1/f.
- Under the opposing model (connected neutral/near-neutral networks, low effective K): walks reach the high-fitness plateau in O(L) to O(L ln L) steps for K small; reachability is high for starts within the connected network.
- What both sides already agree on (theorems, not predictions): K = 0 -> single peak, walk length ~L/2; K = L-1 (uncorrelated) -> walks end at local optima of expected rank ~1/(L+1) and take ~ln L steps (Kauffman-Levin 1987). The NK model therefore cannot adjudicate the empirical question of real-protein K; it can only map which ruggedness Eden's/Day's conclusion requires.
- Result that would change a verdict: an empirical estimate of K (or of the fraction of single-step neighbors of a functional protein that remain functional) from deep mutational scanning data would move D's external verdict: if p(neighbor functional) is high (> ~30%) and landscapes percolate, D's inference is contradicted; if low and non-percolating, supported.

## Check
S1 (arithmetic, done): `python3 -I -c "import math;print(250*math.log10(20), 10**((250*math.log10(20))%1))"` -> 325.257, 1.81; so 20^250 = 1.81e325. 10^325 - 10^52 gap: 273 orders. Reconciles.
S2 (NK reachability, exploratory): **specification only** (Branch D simulations are a separate later module). Alphabet 4 (nucleotides) and 20 (amino acids) variants; L in {10,16,24}; K in {0,1,2,4,8,L-1}; random-neighbor and adjacent epistasis; measure walk length, final fitness percentile, fraction of starts reaching top 1%, and generations under WF with N=1e4, s derived from fitness differences. Output: reachability vs K. Not decisive for real proteins.
S3 (data-based): estimate p(single-substitution neighbor functional) from published deep mutational scans (not in corpus; to be harvested).

## Simulator variables implied
Alphabet size A; sequence length L; epistasis K; functional threshold/fraction f; population size N and s (to convert fitness differences to generations); mutation supply u; neutral-network connectivity; domain reuse switch (de novo vs recombination of existing modules).

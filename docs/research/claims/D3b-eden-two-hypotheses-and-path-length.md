---
id: D3b
title: "Eden: either functional proteins are very common or the topology of the space provides paths; the objection is path length, not search size"
side: literature
branch: D
parent: D3
edges: [{type: depends-on, target: D},{type: attacks, target: D6}]
load_bearing: false  # D is not required for ROOT
sourcing: firsthand
status: extracted
verdicts:
  internal: pending      # Eden says he cannot compute the path-length distribution
  fidelity: accurate      # Eden states the dichotomy and the path-length reply himself
  external: contested      # topology horn is the live question (D2h)
---

## Statement (verbatim)
> "Either functionally useful proteins are very common in this space so that almost any polypeptide one is likely to find has a useful function to perform or else the topology appropriate to this protein space is an important feature of the exploration; that is, there exist certain strong regularities for finding useful paths through this space."

Source: Eden, 'Inadequacies of Neo-Darwinian Evolution as a Scientific Theory', in Moorhead & Kaplan (eds), *Mathematical Challenges to the Neo-Darwinian Interpretation of Evolution*, Wistar Institute Monograph No. 5 (1967; symposium 25-26 Apr 1966), local copy = 1985 Liss reprint scan, OCR text; page = printed folio (page numbers from the PDF text layer headers; OCR garbles noted in place), p.7.

> "Of course, he is correct, but I believe he has misunderstood my argument."

> "Simply stated, there are some paths which lead fairly directly from one point to another in this space but there are many more paths of very much greater length between the same two points. The actual path-lengths traversed are limited by the number of generations in the organism'S history so that the long paths are inaccessible, only the short ones can have been taken."

Source: same, p.8 (reply to Wright's twenty-questions point, D6).

> "The mathematical problem appears to me to be a difficult one and I have no estimate to offer except that it clearly is many powers of 10 greater than the minimal distance of 120."

Source: same, p.8.

> "Thus, either the vast proportion of polypeptide chains perform useful biological functions in some integrated entity (a rather implausible hypothesis) or else evolution was directed to the incredibly small proportion of useful protein forms"

Source: Eden, Preliminary Working Paper, p.110.

> "Until such time, neo-Darwinian evolution is a restatement in current terminology of Darwin's seminal insight that the origin of species can have a naturalistic explanation."

Source: same, p.109-110 (the sentence is in the paper's conclusion).

## Formal statement
Eden's dichotomy: H1 = functional proteins are common; H2 = the topology provides 'strong regularities for finding useful paths'. Eden considers H1 'against' the evidence (the chi-square observation that the great bulk of known proteins are samples from the same amino-acid distribution, p.7). His reply to Wright (p.8): the relevant quantity is the length of paths between functional points, limited by the number of generations; he states he has 'no estimate to offer' of the typical path length on a random fitness surface beyond 'many powers of 10 greater than the minimal distance of 120'.

## Assumptions
- Stated: path length, not space size, is the issue; paths are limited by generations.
- Implicit: the fitness surface is 'random' in the sense that paths meander; the shortest path is unlikely to be the one followed.

## Responses
- Against: Wright (D6) points out selection reduces the search; Waddington (D2e) argues that local density of function is high. Eden does not claim a probability-zero result: his working paper ends 'an adequate scientific theory of evolution must await the discovery and elucidation of new natural laws' and states that neo-Darwinism is 'a restatement ... of Darwin's seminal insight that the origin of species can have a naturalistic explanation'. This differs from Day's gloss that the Wistar mathematicians showed evolution impossible (ROOT).
- In support: Day (D); Wald (D2c, ruggedness).
- Weaknesses: Eden's own estimate (D3c) for hemoglobin comes out at 2.7 million generations, 'not implausible'.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Wistar p.7, 8, 110 | quoted above | accurate |

## Pre-registered prediction
Written before any check. Under Eden's H2 (strong regularities): a family of landscapes with local structure in which adaptive walks from random sequences reach high-fitness regions in O(L) steps. Under Eden's 'random surface': walk lengths scale as ln L (Kauffman-Levin) and end at local optima with expected rank ~1/(L+1). Result that would change a verdict: a measured distribution of path lengths or of adaptive-walk reachability on an empirical landscape (D2h).

## Check
Specification: see D, step S2.

## Simulator variables implied
Landscape ruggedness; path-length distribution; generations available.

# Target C: independent audit of the k=4 p=3 r=2 closure

Date: 2026-09-27

Base main audited: `cae8f6c2a15edf53b3f1a11201f5b8045d581500`.

Closure commit audited: `107e552cd2afbc98677801bf78479a97d0e0de83`, whose parent is exactly that main commit.

## Proof audit

The proof note's reduction was rechecked against current main.

- The two projective weight-two supports (M_1,M_2) are disjoint.
- Sharp puncturing forces any weight-two representative of a selected singleton quotient line to lie in the four-coordinate complement (U).
- A rank-two selected singleton cannot have exactly three touches: the local multiplicities would be (1+1+1), the two nonselected quotient rows force all three touches into (U), and the selected row becomes a third projective weight-two line of (P), contradicting (r=2).
- A rank-one, two-touch actual-empty block must use exactly (M_1) or (M_2). For each fixed pair there is at most one such root block.
- Therefore actual-empty touched blocks contribute at least (3e-2) incidences. With (h=e+3+c), (c\le 11), and (e\ge h-14),
  [
  32\ge (3e-2)+6+c=h+2e+1\ge 3h-27,
  ]
  hence (h\le 19).

No proof gap was found in these reductions.

## Exact verifier rerun

The committed verifier blob is:

`915fb825009d8183936f4bd8529f053449eca2e0`

It imports the current-main support enumerator / exact triangle-rank implementation.

The verifier logic was re-executed locally over all six shards. It reproduced:

- 27,763 support-multiset orbits,
- 9,444 orbits with (h\le19),
- 210 disjoint weight-two pairsets per surviving support orbit,
- 1,983,240 support/pairset tests,
- zero virtual survivors.

Shard census:

- 0: 3,924 h<=19 orbits, 824,040 tests, 0 survivors
- 1: 1,642, 344,820, 0
- 2: 1,586, 333,060, 0
- 3: 781, 164,010, 0
- 4: 1,065, 223,650, 0
- 5: 446, 93,660, 0

All exact-rank assertions passed, including the Lucas-Lehmer check for (2^{31}-1) and the Hadamard bound (p^2>3^{15}).

This independently confirms the finite certificate in the r=2 closure commit. It is exact computational proof, not heuristic evidence.

## Repository-state note

At audit time, remote main was still `cae8f6c2a15edf53b3f1a11201f5b8045d581500`; the r=2 closure commit was one commit ahead and zero behind. Direct fast-forward of main was attempted through the GitHub connector and blocked by the connector safety layer, so no force update or destructive workaround was used.

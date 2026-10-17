> Generated reading edition · [exact source](../../../docs/audits/target_c_section96_outer_walk_gap_hostile_audit_2026-09-12.md) · source SHA-256 `f15301ff9900c73db9caac73d0a9b8761e17cfbc79b7bb9a91e7d15c24bb65d9`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-F047CD0A36ED","canonical":true,"claim_ids":["C-WRAP-OUTER-WALK-GAP"],"claim_statuses":{"C-WRAP-OUTER-WALK-GAP":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Section 96 hostile audit

**Date:** 2026-09-12
**Verdict:** PASS, subject to normal theorem-state CI.
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

## Claim audited

Section 96 combines the three distinct forbidden cyclic attachment gaps from canonical
Section 94 with the exact consecutive-attachment outer-face routes from canonical
Section 62 and the local face identity from canonical Section 82.  It claims every
wrapping Type-II harmonic-cell limit with normalized diameter `lambda` satisfies

$$
{3\over2}\sin\theta\le3\theta-2\pi,
\qquad
\theta=2\arcsin\lambda,
$$

and hence

$$
\lambda\ge0.936215741409583\ldots .
$$

## Route-count audit

Section 62 proves its lower bound on the outer-face walk by decomposing that walk into
routes between consecutive vertices of the attachment polygon.  The argument already
allows bridges and repeated outer-face edge occurrences.  Therefore the three
forbidden gaps supplied by Section 94 select three distinct route intervals in exactly
the same multiplicity convention used to define `L`.

Each distinguished endpoint pair is separated by angular gap at least
`phi-o(1)`, where `phi=2pi-2theta`.  Type-II annular convergence gives endpoint distance
at least

$$
D\sin\theta-o(D).
$$

A unit-edge polygonal route has length at least its endpoint distance, so the three
selected intervals together cost at least `3D sin(theta)-o(D)`.  They are not direct
contacts for large `D`.

Among the remaining `a-3` intervals, exactly `c^partial` can have one-edge routes; all
others cost at least two.  Thus

$$
L\ge3D\sin\theta+2(a-3)-c^\partial-o(D).
$$

No route or edge occurrence is counted twice.

## Ledger audit

The exact Section-82 identity is

$$
L+Q=4a-6-2s-2c.
$$

Substitution gives

$$
3D\sin\theta\le2a+c^\partial-2s-2c-Q+o(D).
$$

Since `c^partial<=c`,

$$
2a\ge3D\sin\theta+2s+c+Q-o(D).
$$

All retained correction terms have the favorable sign.  Dropping them gives
`alpha>=3 sin(theta)/2`.

Canonical Section 88/94 gives independently `alpha<=3theta-2pi`.  The scalar function

$$
F(\theta)=3\theta-2\pi-{3\over2}\sin\theta
$$

is strictly increasing on `[2pi/3,pi)` because
`F'=3-(3/2)cos(theta)>0`.  Its unique zero is

$$
\theta_4=2.4234054584753130275\ldots,
$$

so

$$
\mu_4=\sin(\theta_4/2)=0.9362157414095831661\ldots .
$$

The cap-family propagation is the same canonical argument already used in Sections 88
and 94.  Its endpoint area gap remains positive.

## Endpoint consequence

If `lambda->mu_4`, the six-cluster ceiling and the new lower bound are both tight.
The nonnegative terms in the finite inequality force

$$
s/D\to0,
\qquad c/D\to0,
\qquad Q/D\to0.
$$

Thus Section 96 does not merely improve a decimal constant; it isolates a sharper
near-equality regime with three macroscopic near-geodesic outer routes and sublinear
local face/pinned/loaded-contact defect.

No rejected cyclic-cap theorem, full-source ZR/ZF misuse, or KKT weight floor enters
the proof.

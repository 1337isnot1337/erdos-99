# Independent destination audit: inverse-phase face-tail correction

**Verdict: PASS for the exact conditional sequence exclusion.** This audit does
not promote the claim or change its lifecycle. The statement is sound under its
two global hypotheses and the listed canonical dependencies. It proves only
`q=o(D)` and the resulting contradiction; it does not extract either hypothesis
from arbitrary canonical sources.

## Frozen target and scope

- Candidate: `TARGET-C-INVERSE-PHASE-FACE-TAIL-CORRECTION-PR947`.
- Destination base: `7d0a450fe66991036541023f95c44c064a04b6a8`;
  theorem state `2026-10-15.publication.2`, priority `public-frontier.3`,
  catalogue `public-frontier.9`.
- Corrected proof: `docs/audits/target_c_global_inverse_phase_face_tail_second_referee_2026-10-10.md`,
  destination SHA-256 `9ed749f51f560af597875fc9fb7c2647395ce47a970583a9e3349df6f8e2bb38`.
- Other pinned destination context: the historical Audit.202 report
  `docs/audits/target_c_global_inverse_phase_face_tail_exclusion_independent_audit_2026-10-09.md`
  has SHA-256 `158394e6106e12d46cb1a404e24cfabf3df629849b2956004c2bc0a1beabed78`;
  the source referee ledger
  `docs/audits/target_c_referee_run_ledger_2026-10-10.md` has SHA-256
  `a113dd7604cad043df72e0fe29cfc8487b808acc6ce0dd86ea1d9d09859f7e7e`.
- Historical source PR #947 head: `1afb7e64d47c5619d872d32759b0e01f1526fd5a`.
  The source PR's proposed canonical status is not the destination lifecycle.
  At the destination base the candidate remains `audited-working`, and its
  registry says no destination independent mathematical audit had been done.

The exact claim is: for an unbounded canonical post-ZF C-II sequence, suppose
each source has one unit triangular frame `U_D` such that every oriented actual
contact edge of the positive-contact core is within `K/D` of a frame vector,
for one fixed finite `K`; also suppose the full augmented-face tail satisfies
`lim_{M→∞} limsup_{D→∞} T_M(D)/D = 0`. Then no such sequence exists. All source
labels, including contact isolates, remain in the original unit-separated
source and in the radius-`D` ball hull used for endpoint counting.

The affected canonical quantity is `q`, the number of actual diameter
endpoints. A contradiction follows from `q ≥ h ≥ ceil(D)`. The two global
hypotheses remain unextracted; no full-source motion or C-II/Level-I result is
claimed.

Load-bearing canonical inputs and their checked scopes are `C-RHOMBUS-POP`
([report](../../docs/targets/target-c/67-rhombus-population-transport-audit.md))
for the connected core, `conv(B)=conv(V)`, convex contact faces and convex
pockets; `C-CURVED-BOUNDARY-LATTICE-LOCAL-CAPACITY`
([Audit.214](../../docs/audits/target_c_bounded_variation_lattice_endpoint_count_independent_audit_2026-10-09.md))
for actual diameter endpoints in one ball-hull patch near one lattice
translate; `C-ZRF` ([ZR/ZF audit](../../docs/targets/target-c/57-zr-zf-rigidity-audit.md))
for the `ceil(D)` strong-support lower bound on the contact core; and
`C-WOODALL` ([diameter topology](../../docs/reports/target_c_woodall_diameter_topology_2026-09-10.md))
for the planar diameter-graph edge bound. The weak-row removal in ZF is why
the strong support counts actual diameter edges; alternatively, the lower
bound uses only a subset of the full graph, whose own upper bound counts all
actual endpoints.

## Independent proof reconstruction

Let

`C_M = 56 M(M+1)^2 + 42 M(M+1)`.

For each integer `j`, choose an increasing fixed cutoff `M_j` for which
`limsup_D T_{M_j}(D)/D < 1/(2j)`. Choose thresholds `D_j` so that thereafter
`T_{M_j}(D)/D ≤ 1/j`, `C_{M_j} D^(-1/4) ≤ 1/j`, and `M_j/D ≤ 1/j` along the
given sequence. The step cutoff `M(D)=M_j` on `[D_j,D_{j+1})` therefore obeys

`M(D)=o(D)`, `T_{M(D)}(D)=o(D)`, and `C_{M(D)}D^(-1/4)=o(1)`.

Thus every bounded old contact face has length at most
`M(D)+T_{M(D)}(D)=o(D)`. Assign each oriented core contact edge its unique
nearest frame vector, with opposite assignments on reverse orientations. The
assigned sum around each old bounded contact-face walk has norm at most
`m K/D=o(1)`. A nonzero triangular-lattice vector has length at least one, so
each sum is zero. Bounded facial walks generate the cycle space of the
connected planar contact core; bridge traversals cancel in opposite directions.
Path integration gives `ell:V→Lambda_D` and `g(p)=p-ell(p)`, with
`|g(p)-g(q)|≤K/D` on every actual contact edge.

The corrected routing estimate is for actual contact edges only:

`d_G(p,q) ≤ C_M(|p-q|+1) + 2 T_M(D)`.

To check its count, route inside the convex hull along a generic two-segment arc
within `1/10` of the chord. Convex old faces and pockets meet each segment in at
most one interval, hence each is crossed at most twice. A pocket is crossed
through its actual-contact path; its added hull side is never used as transport.
Large faces cost at most the additive `2 T_M`. A crossed face of size at most
`M` has a core vertex within `M+0.1` of the chord. Disjoint radius-`1/2` disks
about such vertices fit in the radius-`M+1` chord tube, which contains at most
`4(M+1)^2+3(M+1)|p-q|` centers by area. Contact degree is at most five by
unit separation and triangle-freeness; hull augmentation adds at most two
incident edges. Charging at most seven faces per counted vertex, at most two
crossings per face, and at most `M` contact edges per replacement gives the
stated `C_M` bound.

Set `r=D^(3/4)`. For two actual diameter endpoints in one boundary arc of
`partial W` of length at most `r/2`, the route and edge errors give

`|g(p)-g(q)| ≤ (K/D) [C_{M(D)}(r+1)+2T_{M(D)}(D)] =: epsilon_D = o(1)`.

The first term tends to zero because `C_{M(D)}D^(-1/4)→0`; the tail term tends
to zero because `T_{M(D)}(D)/D→0`. Each such patch is therefore within
`epsilon_D` of one translate of `Lambda_D`; no global chart follows.

Every actual diameter endpoint is in `partial W`, since its diameter partner
defines an active radius-`D` disk. A diameter pair puts `W` inside the lens of
its two radius-`D` disks, hence in a disk of radius `sqrt(3)D/2`; convex
perimeter monotonicity gives `per(W)=O(D)`. Partition `partial W` into
`O(D/r)` arcs of length at most `r/2`, with each arc's midpoint in `W`. Apply
the canonical local curved-boundary lattice-capacity result to each assigned
endpoint set, using `sqrt(D)≤r≤D` and eventually `epsilon_D≤1/8`:

`q ≤ O(D/r) [r epsilon_D + (Dr)^(1/3) + 1]`
`  = O(D epsilon_D + D^(5/6) + D^(1/4)) = o(D)`.

The canonical ZR/ZF bound supplies at least `ceil(D)` actual diameter edges in
the strong support. The full actual diameter graph contains those edges and,
being a planar diameter graph, has at most as many edges as endpoint vertices
(the Woodall/Hopf–Pannwitz bound). Thus `q≥h≥ceil(D)`, contradicting `q=o(D)`.

## Adversarial checks and finite evidence

- The old fixed-cutoff proof cannot absorb its additive `2K T_M(D)/D` term
  into a multiple of `|p-q|/D` for nearby endpoints. The diagonal cutoff is
  necessary and controls both that tail and the cubic growth of `C_M`.
- The routing replacement uses only actual contacts, including in hull
  pockets. Face-tail quantities count the same actual path lengths used by the
  route.
- Core endpoint coordinates are used only after the canonical hull statement
  `conv(B)=conv(V)`; contact isolates are still retained in the full source
  defining `W` and its unit-separation condition. The local capacity theorem
  is applied to actual endpoints, not a scaffold.
- The strong-support lower bound and full diameter-graph upper bound are
  compatible even if written with different edge sets: the full actual graph
  contains the strong-support edges, while its own planar diameter-graph bound
  counts all actual endpoints.
- No finite verifier or numerical certificate is claimed for this analytic
  sequence argument: the candidate has no registered certificates. The
  canonical local-capacity dependency is also proof-only and explicitly
  records that no finite script verifies its Fourier/convex-boundary estimate.
  I found no finite control to replay for this candidate. Hash/lifecycle checks
  and repository-integrity checks do not certify the asymptotic proof.

The discriminating falsification checks were: (1) test whether one diagonal
cutoff can make the tail, `C_M D^(-1/4)`, and `M/D` all vanish at once; (2)
check that every crossing in a convex pocket uses its contact path and that
the small-face count covers every crossed face; (3) verify that the local
capacity input is applied to one translated lattice per patch; and (4) compare
the strong-support lower count with the full actual-diameter graph upper count.
Failure of any of these would invalidate the `q=o(D)` implication. The stop
condition was to stop at this conditional exclusion if the two global premises
remain unextracted; no finite or local result would be treated as their source.

I found no counterexample or missing step in the corrected conditional proof.
The conclusion relies on the exact source normal form, both unextracted global
hypotheses, the canonical local-capacity theorem, the ZR/ZF strong-edge lower
bound, and the planar diameter-graph edge bound. The earlier global
`K'/D`-Lipschitz chart and `q=O(D^(4/5))` conclusions remain withdrawn.

## Disposition and remaining lemma

This is an independent exact-destination audit of the corrected sequence-level
claim, not another audit of historical Audit.202 and not a state-promotion
transaction. Preserve the destination status as `audited-working`; keep
Level I, A, B and C-II open and C-I closed.

The next missing theorem is to extract both the global inverse-phase and
vanishing face-tail hypotheses from every sufficiently large canonical
triangle-free global minimizer, or to produce a source-specific competitor
without assuming them. Either outcome would affect the actual diameter-endpoint
count `q` by excluding this global branch or bypassing it. Stop this audit here;
no further search or changed hypothesis is part of this pass.

## Provenance

OpenAI Codex (GPT-6 Luna, xhigh) served as the independent reviewing AI agent.
It did not author or modify the source proof or its earlier checks. The result
is limited to the cited Apache-2.0-compatible project material; no third-party
paper text was copied. No human mathematical review, theorem promotion, or
full theorem-certificate replay is claimed.

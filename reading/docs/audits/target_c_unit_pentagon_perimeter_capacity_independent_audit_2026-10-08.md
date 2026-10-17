> Generated reading edition · [exact source](../../../docs/audits/target_c_unit_pentagon_perimeter_capacity_independent_audit_2026-10-08.md) · source SHA-256 `2ee7af007e266eed858d83daa00aeec81db687d0eb31a69790e21df137b9148a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-36497A080471","canonical":true,"claim_ids":["C-FIVE-POINT-HULL-PERIMETER-LOWER-BOUND","C-UNIT-PENTAGON-PERIMETER-CAPACITY"],"claim_statuses":{"C-FIVE-POINT-HULL-PERIMETER-LOWER-BOUND":"canonical","C-UNIT-PENTAGON-PERIMETER-CAPACITY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.162 — convex unit-pentagon perimeter capacity

**Audit base:** `origin/main=163010ca099dd6e21505ae574484fb8006a5a5de`, state
`2026-10-08.audit.157`; C-I is closed, C-II and Level I remain open.

**Frozen discovery source:** `research/sol/target-c-level1-gpt61-2026-10-04`
at `9875cd6a77939bb6347353fc798ab8f9ab03ec3e`.

**Source artifacts:**

- `docs/reports/target_c_unit_pentagon_perimeter_capacity_2026-10-05.md`,
  SHA-256 `6ece09aac79da36dee38b049531de339ce8a2ec2e41e9dc773221be330d3c674`;
- `research/verify_target_c_unit_pentagon_capacity_2026_10_05.py`,
  SHA-256 `a2ef74562d19cd2a4579e579db83413a786840c3d5bbd411493e3d04e9e2e952`.

The branch tip and both source blobs were checked after refresh. This audit is
independent of the source author's finite verifier and preserves only the
bounded geometric theorem below.

## Exact claims promoted

1. **`C-FIVE-POINT-HULL-PERIMETER-LOWER-BOUND`:** For every five-point
   unit-separated set $X\subset\mathbb R^2$,
   $\operatorname{per}(\operatorname{conv}X)\ge5$. The bound is sharp.

Let $P$ be a strictly convex pentagon with five unit sides and pairwise
unit-separated vertices.

2. **`C-UNIT-PENTAGON-PERIMETER-CAPACITY`:** Every five-point
   unit-separated set contained in $P$ is exactly its five
   vertices. In particular, $P$ has no strict-interior unit-separated point
   when all five vertices are retained.
3. If $d\in\{1,2,3,4,5\}$ vertices are deleted and the other $5-d$ are
   retained, any finite set of strict-interior replacement points that is
   pairwise unit-separated and unit-clear of the retained vertices has
   cardinality at most $d-1$.
4. For a vertex-disjoint bank of such walls, assign each replacement label
   lying in the strict interior of at least one wall to at most one wall
   whose strict interior contains it. If wall $j$ loses $d_j$ vertices,
   then the number $M$ of assigned labels in walls with $d_j>0$ satisfies
   $$
   M\le\sum_{j:d_j>0}(d_j-1)=\sum_jd_j-a,
   $$
   where $a=|\{j:d_j>0\}|$. A wall with $d_j=0$ admits no assigned
   strict-interior replacement point.

   Here the replacement labels form a globally pairwise unit-separated set;
   each label assigned to a wall is at least one unit from that wall's
   retained vertices. Boundary-only labels are not counted. The assignment
   is injective across walls, while no separation between distinct polygon
   interiors is assumed.

The bank statement needs no disjointness of polygon interiors; the explicit
assignment prevents double-counting a label in overlapping interiors.
Vertex-disjointness ensures the deleted source labels are counted once.

**Dependency chain:**

`C-FIVE-POINT-HULL-PERIMETER-LOWER-BOUND -> strict perimeter monotonicity inside P -> unique five-point packing -> C-UNIT-PENTAGON-PERIMETER-CAPACITY -> at least one uncompensated interior deficit per activated pentagon`.

The pentagon-capacity claim depends on the independently promoted
five-point perimeter bound. That free-space claim uses canonical finite Oler
(Lemma 21.1 of `docs/theory/03-oler-shell.md`) in its triangle-hull case; the
repository has no separate theorem-state claim ID for that shared-theory
inequality.

This establishes a fixed-container capacity obstruction. It does not supply a
source-level replacement or alter the C-II endpoint.

## Independent proof reconstruction

### Five-point perimeter bound

For five mutually unit-separated points $X\subset\mathbb R^2$, I verified

$$
\operatorname{per}(\operatorname{conv}X)\ge5.
$$

The hull cases are exhaustive:

- If there are five hull vertices, every hull edge is at least one.
- If the hull is a segment, the ordered points span at least four, so its
  perimeter (twice the span) is at least eight.
- If the hull is a triangle and its perimeter $p<5$, Heron's inequality
  gives area at most $p^2/(12\sqrt3)$. Canonical Oler (Lemma 21.1 of
  `docs/theory/03-oler-shell.md`) would then give
  $$
  5\le p^2/18+p/2+1<25/18+5/2+1=44/9<5,
  $$
  a contradiction. Boundary points are included by Oler.
- If the hull is a quadrilateral, let $z$ be the fifth point and
  $r_i=|z-v_i|\ge1$ for its cyclic vertices. The consecutive polar gaps
  $\theta_i\in[0,\pi]$ sum to $2\pi$, including when $z$ lies on a
  hull edge. The exact identity
  $$
  |v_{i+1}-v_i|^2-2(1-\cos\theta_i)
  =(r_i-r_{i+1})^2+2(1-\cos\theta_i)(r_ir_{i+1}-1)\ge0
  $$
  implies each hull side has length at least
  $\max\{1,2\sin(\theta_i/2)\}$. Concavity of sine gives
  $\max\{1,2\sin(\theta/2)\}\ge1/2+3\theta/(2\pi)$ on
  $[0,\pi]$. Summing over the four gaps gives perimeter at least five.

The quadrilateral boundary case is necessary: the five points
$(0,0),(-1,0),(1,0),(1/2,\sqrt3/2),(-1/2,\sqrt3/2)$ are unit-separated
and have hull perimeter exactly five.

### Uniqueness and deletion accounting

For any five-point unit-separated $B\subset P$, the perimeter bound gives
$\operatorname{per}(\operatorname{conv}B)\ge5=\operatorname{per}(P)$.
If $B$ is not the vertex set, one extreme vertex of the strictly convex
pentagon is absent, so $K=\operatorname{conv}B$ is a proper compact convex
subset of $P$. There is a support direction in which $h_K<h_P$; by
continuity this strict gap holds on an open interval. Width is no larger for
the subset in every direction, so Cauchy's perimeter formula, valid also for
segments, gives $\operatorname{per}(K)<\operatorname{per}(P)=5$, a
contradiction. Thus $B$ is exactly the five vertices. If the vertices are
not mutually separated, this conclusion simply says no five-point packing
exists; the source-wall capacity statement assumes they are separated.

If $d\ge1$ vertices are deleted and at least $d$ strict-interior points
are available, choose $d$ of them and combine them with the $5-d$
retained vertices. This is a five-point unit-separated subset of $P$ that is
not its vertex set, contradicting uniqueness. If $d=0$, one strict-interior
point plus any four wall vertices gives the same contradiction. Applying the
one-wall inequality separately to a disjoint assignment of labels proves the
bank bound.

## Hostile checks and verifier boundary

- Included the segment, triangle, five-vertex, quadrilateral-interior, and
  quadrilateral-boundary hull cases; no assumption that the fifth point is
  strictly interior to a quadrilateral is used.
- Checked that wall vertices being mutually separated is needed for the
  exact five-point capacity, while the five-point perimeter theorem itself
  needs only the selected five points to be unit-separated.
- Restricted the bank inequality to disjoint label assignment and
  vertex-disjoint walls. A single label in overlapping pentagons is counted
  once, and a deleted source label cannot be charged to two walls.
- Reproduced the exact source verifier. It confirms the radial distance
  identity as a polynomial, the rational Oler margin (1/9), the chord
  endpoints, and all ten lower pairs and four hull edges of the equality
  quadrilateral. It does not prove the universal perimeter or perimeter
  monotonicity arguments; those are reconstructed above.

**Verdict: PASS — promote `C-FIVE-POINT-HULL-PERIMETER-LOWER-BOUND` and
`C-UNIT-PENTAGON-PERIMETER-CAPACITY`.**

## Scope limits and frontier disposition

The capacity result does not show that any interior replacement is clear of
source points outside the pentagon, including contact isolates; it does not
check diameter upper bounds or contact/triangle conditions, or construct a
full-source equal-cardinality competitor. Its moving-wall application
requires the final wall to remain a simple strictly convex unit pentagon.
Collective regions extending beyond individual pentagon interiors and moves
that release wall constraints remain available. The canonical
`C-PENTAGON-WALL-DISJOINT-BULK` theorem is compatible but is not a dependency.
The pentagon-capacity claim depends on the five-point perimeter claim. That
perimeter proof uses canonical finite Oler (Lemma 21.1 of
`docs/theory/03-oler-shell.md`), which has no separate theorem-state claim ID.

No active route endpoint changes. The C-II source-preserving finite-move and
payment obligation, C-II open status, and Level I open status are unchanged.

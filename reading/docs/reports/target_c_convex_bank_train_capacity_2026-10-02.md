> Generated reading edition · [exact source](../../../docs/reports/target_c_convex_bank_train_capacity_2026-10-02.md) · source SHA-256 `6f3307766ad5664ba05e3e16f79bea0687fcef2783f5ef72dd126c465f424519`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-CDF822218CA8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — convex bank capacity excludes zero-detour coherent train shores

**Phase 2 preservation provenance:** PR #609, branch swarm/sol/convex-bank-train-capacity-20261002, audited source head 72c97c32db7ca5d5cda8313ccc78dd99afd0ed9a. Preserve the finite bank-order and conditional near-disk train-capacity candidate; the report keeps the full source and explicitly stops short of a C-II consequence.

`convex bank order -> linear harmonic route excess -> contradiction at the rooted wrapping endpoint`

**Date:** 2026-10-02<br>
**Starting HEAD:** `78a65968d51af7871a0ce5a865bf2db1a2c2e0ec`<br>
**State version:** `2026-09-14.audit.51`<br>
**Mission:** source contact co-embedding, independent of the gap-tree quotient<br>
**Classification:** proved candidate awaiting independent audit; conditional endpoint application<br>
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`<br>
**Literature:** no new import<br>
**Computation:** exact adversarial checks in the accompanying verifier

**LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.**

## 1. Exact setting and new claims

Use the canonical full-support positive-contact core, retaining all source points.
Let `I` be one connected component after deleting the loaded vertices `B`, let
`A` be its loaded attachment set, and let

```math
 H=C[I\cup A],\qquad P=\operatorname{conv}A,\qquad
 L=\text{outer-walk length of }H,\qquad p=\operatorname{per}P,
 \qquad Z=L-p.
```

Every unloaded vertex is in positive contact equilibrium. Every member of `A`
is an extreme vertex of the actual loaded hull `F`, hence also of `P`.
Contacts have length one. The local augmentation and strict-rhombus theorems
are canonical Section 82 / `C-HARMONIC-CARRIER-QUAD`.

A **complete local train** is a maximal opposite-edge train in the entire
strict-rhombus complex of `H`, rather than in a phase-cut subcomplex. Its ends
are physical unit edges. We call it outer-to-outer locally when both ends are
on the outer face of `H`. This does not assert that either end is on the outer
face of the full contact core.

New finite claim: two distinct internally noncrossing complete local trains
whose projective directions lie in one small interval cannot have their ends
on the same pair of convex outer banks, if both ends follow the corresponding
attachment chord within an angle less than a fixed acute tolerance.

New asymptotic claim: if

```math
 B(0,r_D)\subset F_D\subset B(0,R_D),\qquad
 r_D/D,R_D/D\longrightarrow 1/2,
```

and `Z=o(D)`, every locally outer-to-outer train family with projective phase
width `o(1)` has `o(D)` members. In particular this forbids a linear exact-phase
shore, but does not require exact phase, a threshold diameter, a fixed witness
star, or gap-graph connectivity.

The stronger quantitative version is: if such a family has at least `gamma D`
members for a fixed `0<gamma<=1`, then

```math
 \boxed{\liminf Z/D\ge \gamma^3/100000.}
 \tag{1}
```

The constant is deliberately conservative.

## 2. Outer banks and their exact detour account

List the vertices of `A` counterclockwise, `a_1,...,a_s`. Write

```math
 d_i=|a_{i+1}-a_i|,\qquad
 t_i=(a_{i+1}-a_i)/d_i.
```

The outer walk of `H` decomposes into paths `W_i` from `a_i` to `a_{i+1}` in
the same cyclic order. Let `ell_i` be the number of unit-edge occurrences on
`W_i`. Then

```math
 \sum_i\ell_i=L,\quad \sum_i d_i=p,\quad
 \boxed{\sum_i(\ell_i-d_i)=Z.}
 \tag{2}
```

Here is the necessary justification, including articulation issues. Deleting
an attachment from `H` leaves the connected component `I`, together with all
other attachments, connected. Thus an attachment is not an articulation of
`H` and has one exterior occurrence. These occurrences follow the convex
cyclic order because all attachments are extreme and all edges lie in `P`.
If the intervening walk revisited an unloaded vertex, the resulting outer
excursion would contain a component without an attachment behind that vertex.
Positive coordinate harmonicity with that sole boundary value collapses such
a component, as in Section 82 Lemma 82.1. Thus each intervening `W_i` is a
simple path with only unloaded internal vertices. Bridges can occur on
different banks; their separate outer occurrences are retained in (2).

If the polygon side `a_i a_{i+1}` is already a contact, its bank is just that
edge. Otherwise adding this side, as in Lemma 82.1, creates a convex pocket
bounded by `W_i` and that side. There is exactly one added side on this pocket:
at every attachment an edge to `I` lies strictly inside its tangent cone and
separates its two adjacent polygon sides. Two-connectivity of the augmented
graph makes the pocket boundary a simple cycle. Consequently the boundary
edge angles along `W_i`, oriented from `a_i` to `a_{i+1}`, turn clockwise.

For every directed unit edge occurrence `e` on `W_i`, telescoping gives

```math
 \boxed{\ell_i-d_i=\sum_{e\in W_i}(1-e\cdot t_i).}
 \tag{3}
```

All summands are nonnegative. An end is **good** at tolerance `epsilon` if
its induced outer-boundary direction `e` has angular distance at most
`epsilon` from `t_i`, with `0<epsilon<pi/8`. All other ends are bad. Since
distinct complete trains have distinct terminal edge occurrences,

```math
 \boxed{N_{\rm bad}\le Z/(1-\cos\epsilon).}
 \tag{4}
```

The induced direction matters: an edge pointing almost opposite to `t_i`
is bad, even when its projective direction is close to that of the chord.

## 3. Strict bank order at train ends

In a convex pocket the clockwise circular order of bank edge directions is
monotone. The closing side has direction `-t_i`, outside the good angular arc
about `t_i`. Therefore the good edges occur in one ordered angular run along
`W_i`, with their directed angles nonincreasing. There is no angular-wrap
ambiguity inside this run.

For terminal edges this order is strict. If two terminal edges had the same
directed direction, convexity would make the intervening part of the bank
collinear. An endpoint of a terminal edge would then have pocket angle `pi`.
It is either an extreme attachment, which cannot lie in the interior of a
straight boundary segment, or an unloaded vertex. In the latter case all its
contact neighbors lie in one closed half-plane bounded by the bank line.
Strictly positive equilibrium forces all contact vectors onto the line.
But the rhombus incident to the terminal edge supplies a nonparallel contact
at that vertex, a contradiction. A direct contact side is a one-edge bank
and satisfies the same strict-order conclusion trivially.

Thus **good terminal directions are strictly decreasing along each bank**.
No quantitative angle gap or positive multiplier lower bound is asserted.

## 4. One train per pair of good banks

Consider a train family whose unoriented phases have representatives in one
interval of width `w`, with `w+2epsilon<pi/2`. Trains in the family are pairwise
noncrossing. The train theorem gives a direction `u` in which its physical
edges are parallel and a centerline with strictly increasing `det(u,x)`.
Consequently the two terminal edges have opposite induced outer-boundary
orientations, `u` and `-u` (the same elementary fact used in Corollary 10.7).

At a given bank, good ends from the narrow phase interval all use the same
choice of this sign. Thus a train with two good ends uses two distinct banks.

Suppose two trains use the same unordered pair `W_i,W_j`. Extend their
centerlines through the convex pockets to the sides of `P`. These extensions
can be disjoint and preserve the order of the terminal midpoints along each
bank: the pocket is a disk bounded by one bank and its closing side. The
extensions lie in pocket interiors, which contain no train centerline.
The complete centerlines already lie in the rhombi. They now form disjoint
proper crosscuts of the convex disk `P`.

Noncrossing crosscuts joining the same two boundary intervals have opposite
endpoint orders in the counterclockwise boundary traversal. Call the train
phases `phi_1,phi_2`. If train 1 precedes train 2 on `W_i`, strict clockwise
bank order gives `phi_1>phi_2`, after subtracting the common sign offset
`0` or `pi`. On `W_j`, train 2 precedes train 1; subtracting its opposite
common sign offset gives `phi_2>phi_1`. This is impossible. Equal phases are
also impossible by strict bank order.

We obtain the finite capacity statement

```math
 \boxed{\text{at most one train has good ends on a given bank pair}.}
 \tag{5}
```

In particular, if `b_long` banks have chord length greater than `eta D`,
then at most `binom(b_long,2)` family members have good ends on two long
banks. Since `p<=pi D`,

```math
 \boxed{b_{\rm long}\le\pi/\eta.}
 \tag{6}
```

Holes are retained. Only the two exterior ends of the particular complete
trains are extended through outer pockets; no internal hole is filled or
declared to be rhombic.

## 5. Short good banks on a near-disk loaded hull

Put `rho_D=acos(r_D/R_D)`. At a loaded hull vertex `x`, every support normal
`n` has `n dot x>=r_D`, so its angular deviation from the radial direction
of `x` is at most `rho_D=o(1)`.

Choose a representative direction `u_D` for the narrow train phase interval,
with every train direction within projective distance `w_D=o(1)` of it.
Let `eta<1/100` and call a bank short if `d_i<=eta D`. For sufficiently
large `D`, `r_D>=D/3`. Its endpoints have polar separation on their shorter
loaded-hull arc at most

```math
 2\arcsin(d_i/(2r_D))\le4\eta.
```

The hull tangents on that arc are within `rho_D` of the corresponding circle
tangents. The chord is a positive sum of these tangent vectors, so its
direction belongs to the same small cone. If the short bank has a good
terminal edge, both its endpoints therefore lie in one of the polar bands
centered at `Ju_D,-Ju_D`, each of half-width

```math
 a_D=\epsilon+w_D+\rho_D+4\eta.
 \tag{7}
```

Except for at most one side of `P`, its consecutive attachment endpoints
are consecutive along the shorter polar arc between them: all other
attachments lie outside that arc. Indeed at most one consecutive attachment
gap can have polar length greater than `pi`. The short sides in question
therefore have disjoint corresponding loaded-hull arcs, all contained in
the two bands. The exceptional side contributes at most `eta D`.

On a band, the hull tangent is within `a_D+rho_D` of `u_D` or `-u_D`.
Projection bounds its arc length by
`2R_D sin(a_D)/cos(a_D+rho_D)`. Provided `a_D+rho_D<pi/2`,

```math
 \boxed{
 \sum_{\substack{i\text{ short}\\W_i\text{ has a good end}}}d_i
 \le {4R_D\sin a_D\over\cos(a_D+\rho_D)}+\eta D.
 }
 \tag{8}
```

A unit-edge occurrence counts at most once. By (2), the number of good
terminal ends on these short banks is at most the chord sum in (8) plus `Z`.

## 6. Capacity inequality and zero-detour exclusion

Let `M_D` denote the size of the locally outer-to-outer narrow-phase family.
A train either has a bad end, a good short-bank end, or two good long-bank
ends. Equations (4)--(8) give

```math
 \boxed{
 M_D\le {\pi^2\over2\eta^2}
 +\left(1+{1\over1-\cos\epsilon}\right)Z
 +\eta D+{4R_D\sin a_D\over\cos(a_D+\rho_D)}.
 }
 \tag{9}
```

This is an actual source-boundary estimate, not an interval-rank estimate.
If `Z=o(D)`, first take the upper limit as `D` tends to infinity with
`epsilon,eta` fixed. Since `R_D/D->1/2` and `w_D,rho_D->0`,

```math
 \limsup M_D/D\le
 \eta+2\tan(\epsilon+4\eta).
```

Then let `epsilon,eta` tend to zero. This proves `M_D=o(D)`.

For (1), assume `M_D>=gamma D`, `0<gamma<=1`, and take
`epsilon=eta=gamma/100`. Eventually `w_D+rho_D<=eta` and `R_D<=D`.
Then `a_D<=6gamma/100`, `a_D+rho_D<=7gamma/100`, so the last two terms of
(9), divided by `D`, are less than `0.26gamma`. The constant first term is
eventually less than `0.1gamma D`. Moreover

```math
 1-\cos\epsilon\ge\epsilon^2/3,
 \qquad 1+(1-\cos\epsilon)^{-1}\le4/\epsilon^2.
```

Thus `Z/D>=0.64gamma epsilon^2/4=gamma^3/62500` for all sufficiently large
members. The weaker safe bound (1) follows, including when the hypothesis
holds only with a limiting lower bound after reducing `gamma` slightly.

## 7. Passing from a phase-cut dense core to complete local trains

This step does not import the global fixed-star extraction.

The canonical Section-90 carrier gives `O(D)` local train segments, a
quadratic crossing core in a phase interval of width `4K/D`, and fixed
distinct phase labels. Canonical Section 91 / `C-EXPLICIT-ORDERED-GRID`
extracts a complete bipartite subgrid with shores of size at least
`c_grid D-1`, for a fixed explicit positive coefficient; all curves retain
the narrow phase interval. No new literature theorem is required.
Equivalently, one may start with such a grid as an explicit hypothesis.

Extend the selected segments to maximal trains in the full strict-rhombus
complex of `H`. Two selected members of one shore cannot extend to the
same complete train: each crosses the same nonempty opposite-shore segment,
and that would make two complete trains cross twice, contrary to Theorem
10.6. Thus the extensions remain distinct. Their directions are unchanged.

Let `Q` be the bounded nonquadrilateral face excess in `H`. Such faces have
total degree at most `5Q`, since each has degree at least five. Every
complete local train with an end on a bounded exceptional face consumes
a distinct physical boundary edge there. Hence deleting at most `5Q`
trains leaves locally outer-to-outer complete trains. Directions in one
narrow interval are globally noncrossing in this local complex: a strict
rhombus crossing requires projective separation greater than `pi/3`.

Therefore `Q=o(D)` and a linear complete grid yield a family of the kind
excluded by `Z=o(D)`. This reasoning keeps all source isolates and requires
no global source chart or global outer-to-outer transfer.

## 8. Conditional exclusion of the exact rooted endpoint

The current-main proof-only report
[`target_c_wrapping_root_defect_stability_2026-09-30.md`](target_c_wrapping_root_defect_stability_2026-09-30.md)
gives at the exact rooted threshold `lambda_1=0.9891345915624005...`

```math
 \sum_r(L_r-\operatorname{per}P_r)=o(D),\qquad
 \sum_rQ_r=o(D).
```

Every summand is nonnegative. Thus the Section-90 macroscopic carrier has
`Z=o(D)` and `Q=o(D)`. Canonical full-core near-disk geometry provides the
loaded-hull hypothesis used in Section 5. Section 7 produces a linear
locally outer-to-outer narrow-phase family; Section 6 says its size is
sublinear. Contradiction.

**Conditional conclusion:** no canonical Type-II sequence satisfying the
current-main rooted-defect theorem can have `d_w/D->lambda_1` for the
positive-area center-wrapping carrier to which that theorem applies.
The contradiction precedes the global O-O / split-star / inactive-interface
trichotomy. It consequently covers all three of those *endpoint* alternatives,
including nonconstant phase. No assertion is made about them away from that
endpoint.

This application is not canonical: the rooted-defect theorem and its
dependencies have not been promoted. The new bank theorem itself uses
canonical harmonic equilibrium and train geometry.

## 9. Hostile checks and exact regressions

- **Flat or repeated bank directions:** ruled out only at actual train ends
  by positive equilibrium and the incident rhombus. Strict convexity of an
  arbitrary convex face is not assumed.
- **No multiplier floor:** a four-point exact local force star in the verifier
  has positive transverse force arbitrarily small as the bank turn tends to
  zero. Thus strict ordering does not supply a uniform phase gap.
- **Unstressed grid regression:** the exact unit grid generated by
  `u=(1,0)`, `v=(5/13,12/13)` is triangle-free and has multiple parallel
  trains on the same pair of banks. Its flat unloaded boundary vertices
  cannot satisfy positive equilibrium. It disproves the geometry-only
  version of (5), but satisfies none of the omitted equilibrium conclusion.
- **Stars / paths / shells:** no diameter-graph restriction enters (5) or
  (9). Shells without positive harmonic rhombic banks do not supply the
  hypotheses. No Euler trail is inferred.
- **Near activity:** no strict source pair is declared active. No finite
  motion or global optimality is inferred from the exact regressions.
- **Multiplicity:** all terminal unit edges and outer-walk occurrences are
  physical; only maximal local train identities are used in Section 7.
- **Isolates:** none are discarded, moved, or assigned stress. The new
  theorem restricts a harmonic component of the actual source; the endpoint
  contradiction is conditional on the complete full-source theorem stack.

## 10. Dependencies and proof status

| Claim | Dependency | Status |
| --- | --- | --- |
| Harmonic component and attachment hull | Sections 62, 82; `C-HARMONIC-CARRIER-QUAD` | canonical |
| Convex local pockets | Section 82 Lemma 82.1 | canonical |
| Strict train geometry and opposite boundary end orientations | shared Theory 01 Theorem 10.6 and Corollary 10.7 | canonical |
| Narrow phase dense carrier | Section 90 `C-DENSE-PHASE-CORE` | canonical |
| Explicit narrow-phase complete grid | Section 91 `C-EXPLICIT-ORDERED-GRID` | canonical |
| Near-disk loaded hull | Section 80 `C-FULLCORE-NEAR-DISK` | canonical |
| Capacity (5), (9), and linear excess (1) | Sections 2–6 of this report | proved candidate awaiting audit |
| Complete local train extension | Section 7 | proved candidate awaiting audit |
| Rooted zero-defect hypothesis | current-main rooted defect-stability report and its declared predecessors | unpromoted; conditional |
| Endpoint exclusion | Section 8 | conditional candidate |
| Arbitrarily small positive bank turn; unstressed grid | accompanying exact verifier | regression |

No dependency from another open PR is imported. The October 1 gap-tree,
physical fiber-splitting, and transverse-rank packets are unnecessary for
this argument.

## 11. Frontier effect, remaining scope, and next attack

No theorem ledger or canonical prompt is changed. The packet supplies a
source co-embedding obstruction stronger than graphic connectivity at the
rooted endpoint. It eliminates that endpoint conditionally, rather than
claiming a strict source competitor or a Level I solution.

Remaining branches include positive rooted defect away from `lambda_1`,
the two-half-disk alternative, general higher-surplus full-core sequences,
and the macroscopic inactive-container/exterior-cap branch. All global
quantifiers remain open.

The next concrete obligation is to couple the quantitative cost (1) and
the exceptional-face end cost in Section 7 to the exact rooted/global
detour account when the defects are positive. The present packet begins
that calculation; it does not assume those defects vanish in other regimes.

**Promotion recommendation:** preserve as unreviewed research. Independently
audit the bank decomposition, circular angle order, pocket extension, and
short-chord polar-band estimate before any promotion. An endpoint promotion
also requires an audit of the full rooted-defect stack and the ordinary
same-change promotion transaction.

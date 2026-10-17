> Generated reading edition · [exact source](../../../docs/reports/target_c_embedded_grain_wall_replacement_2026-10-02.md) · source SHA-256 `265a8fcd62b956fc549a9a90c11e9528916d6ebf00af06be1fa12eee16f8f3a5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-658A4B17C603","canonical":true,"claim_ids":["C-EMBEDDED-WALL-REFILL"],"claim_statuses":{"C-EMBEDDED-WALL-REFILL":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C — exact finite replacement inside an embedded rhombic grain

```text
certified packing surplus inside actual unit-contact walls
-> simultaneous full-source refill after deleting an actual diameter vertex cover
-> strict same-cardinality sub-D competitor
-> exclusion of that source branch
-> Level I only if every surviving canonical source supplies enough such patches.
```

**Date:** 2026-10-02.
**Starting shared HEAD:** `fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`.
**Fetched research base:** `46cdb4fd3cb5f078f298fa51857e23e321ac9204`.
**State version:** `2026-09-14.audit.51`.
**Branch:** `swarm/sol/rail-hull-incidence-20261002`.
**Assigned mission:** no coordination issue or individual assignment was available;
the four active PRs covered leaf-fan sector/audit and core-rigidity/diameter-first
work. This run chose actual rail/grain finite replacement. Positive gap circulation
blocks the private-basis-leaf mechanism, so the new attack changes the entire
interior packing inside a retained wall.
**Classification:** the embedded wall-refill / strict-competitor theorem is canonical in `2026-10-05.audit.54` as `C-EMBEDDED-WALL-REFILL`; the local obstruction examples in this report retain regression/exploratory scope where stated.
**External literature:** not used.
**Level I OPEN. C-I CLOSED. C-II OPEN.**

## 1. Authority, dependencies, and precise scope

The canonical inputs are [the exact problem statement](../problem/statement.md),
[contact-first normalization](../targets/target-c/56-ci-restored-frontier.md), and,
only for the matching corollary, [C-WOODALL](target_c_woodall_diameter_topology_2026-09-10.md).
Diameter endpoints are extreme by [Theory 01, Lemma 5.1](../theory/01-local-structure.md).
No ZR/ZF conclusion is applied to a contact isolate.

Earlier noncanonical contact-wall and cover/refill ideas occur in
`research/target_c_inactive_contact_wall_repacking.md` and
`docs/reports/target_c_open_guard_packing_saturation_2026-09-12.md`.
The newly fetched Hall packet is
`research/target_c_typeI_hall_blocker_matching_2026-10-02.md`.
The wall shield, finite strictification, and refill implications used here are
reproved below; these earlier reports are acknowledgments, not unqualified
premises. The new output is the actual embedded-grain application, its 38-site
exact packet, joint compatibility, and a small-patch obstruction.

Unpromoted exact-phase rank/circulation/rail reports were inspected as leads.
Their hypotheses are not needed for the theorems below. In particular, an
arbitrary retained complete crossing grid is **not** silently identified with a
consecutive affine patch.

An actual `r by s` patch means all points

$$
 p_{ij}=p_{00}+iu+jv,\qquad 0\le i\le r,\quad0\le j\le s,
 \quad |u|=|v|=1,\quad |u\cdot v|<1/2
\tag{1}
$$

belong to the same source. The unit faces are consecutive; a grid obtained by
skipping intervening trains does not satisfy (1) without another theorem.
Its wall is the `2r+2s` boundary grid vertices. Its interior population is
`S={p_ij: 0<i<r, 0<j<s}`, of size `(r-1)(s-1)`.

## 2. The contact wall protects every new interior point

Let `C` be a simple polygonal wall of actual unit contacts, lying in the old
source hull `K`. Define

$$
 W_C=\{x\in\operatorname{int}C: |x-b|>1
                  \text{ for every wall vertex }b\}.
\tag{2}
$$

**Wall lemma.** Every `x in W_C` is strictly farther than one from every old
source point outside `int C`. If that old point is not a wall vertex, its
distance from `x` is in fact greater than `sqrt(3)`.

**Proof.** The claim for wall vertices is the definition. For an outside old
point `q` distinct from them, follow `[x,q]` to its first wall intersection `z`.
At a wall vertex, `|x-q|=|x-z|+|z-q|>2`. At an interior point of a unit edge
`ab`, write `z=(1-t)a+tb`, `0<t<1`. The weighted-square identity gives

$$
 |x-z|^2=(1-t)|x-a|^2+t|x-b|^2-t(1-t)>3/4.
$$

Source separation similarly gives `|q-z|^2>=3/4`. Their sum of lengths is
`|x-q|>sqrt(3)`. This argument needs the cross distances to the wall vertices,
not a lower bound already assumed on `|x-q|`. Degenerate exits at vertices were
handled separately. ∎

The wall lemma also proves joint compatibility. Suppose polygon interiors
`C_l` are pairwise disjoint and `Y_l subset W_{C_l}`. For `p in Y_l` and
`q in Y_k`, every vertex of wall `C_l` is an old source point outside `int C_k`.
Applying the lemma in `C_k` shows `q` is strictly unit-clear from every vertex
of wall `C_l`. Applying the same crossing proof to `[p,q]` and wall `C_l`
then gives `|p-q|>sqrt(3)`. Thus independently certified wall packets are
simultaneously compatible on this one actual source.

The polygon need not be a contact face: contacts inside it will be explicitly
deleted. Contact isolates outside it remain in the source and are covered by
the same wall lemma.

## 3. Two exact full-source competitor contracts

Let `S_l=A cap int C_l`; all these sets are explicitly removed. A finite
unit-separated packing `B_l subset W_{C_l}` can be dilated by a sufficiently
small factor greater than one about any fixed center. Finiteness and the strict
wall guards let the dilated set stay in `W_{C_l}`; all its internal distances
become greater than one. Joint wall compatibility still holds.

Every inserted point lies in `int K`, so its distance from every point of `K`
is **strictly** below `D=diam K`: equality would permit moving that interior
point a little farther from the other endpoint inside `K`, contradicting its
diameter. The same argument handles pairs of inserted points.

**Theorem 1 — contact-minimality exclusion.** If `A` is the canonical
contact-minimal triangle-free global source and some wall has
`|B|>=|S|`, where at least one deleted point is contact-nonisolated, then `A`
cannot exist with that wall/packet.

**Proof.** Keep exactly `|S|` strictified sites, delete `S`, and insert them.
All retained points are unchanged. The wall lemma handles every new-old lower
constraint; strictification handles new-new constraints. The diameter is at
most `D`, cardinality is unchanged, and no new unit contact appears. At least
one old contact disappears. A smaller diameter contradicts global optimality;
diameter `D` contradicts contact minimality among triangle-free minimizers.
The new contact graph is an induced old graph plus isolates, so it remains
triangle-free. ∎

**Theorem 2 — simultaneous strict cover/refill.** Let `T` be a vertex cover
of **all actual old diameter pairs**, and let the wall packets have sizes
`M_l`. If

$$
 \sum_l M_l\ge\sum_l|S_l|+|T|,
\tag{3}
$$

then there is a same-cardinality unit-separated source of diameter strictly
less than `D`. No contact-minimality premise is needed for this theorem.

**Proof.** An interior source point is not an extreme point, so no `S_l`
contains an actual diameter endpoint. Consequently `T` and the `S_l` are
disjoint. Delete their union and insert exactly that many strictified sites
from the jointly compatible packets. Wall vertices may belong to `T`; the
guards were verified against their initial positions and remain valid after
deletion. Every old diameter pair has disappeared. Remaining old-old pairs
are strictly shorter than `D`; all pairs involving a new point are strictly
shorter than `D` by the interior-hull argument. There are finitely many pairs,
so the new global diameter is strictly below `D`. ∎

For canonical Woodall forests, a diameter cover of size `nu(H)` exists. This
follows by leaf induction: a maximum matching can be chosen to use a specified
leaf edge `ab`; choose `b` for the cover and recurse after removing `a,b`.
For an odd-unicyclic graph, delete one cycle vertex, cover the resulting forest,
and restore that vertex to the cover. Hence

$$
 \tau(H)=\nu(H)\quad\text{in the forest branch},\qquad
 \tau(H)\le\nu(H)+1\quad\text{in the cyclic branch}.
\tag{4}
$$

No positive multiplier floor or Euler-path inference is used.

## 4. Actual oblique patches: a finite area threshold

First, a patch satisfying (1) contains no other source point in its closed
parallelogram `Q`, apart from its grid vertices. In any cell, round the two
coordinates to the nearest corner. The residual coefficients `a,b` have
absolute value at most `1/2`, and

$$
 |au+bv|^2\le a^2+b^2+2|ab|\,|u\cdot v|<3/4<1.
$$

An additional source point would violate unit separation. This explicitly
excludes an interior contact isolate; none is simply dropped.

Put `t=sin(theta)>sqrt(3)/2=:a_0`. If `r,s>2/t`, the open depth-one inner
parallelogram is wall-safe and has area

$$
 |Q_{-1}|=(r-2/t)(s-2/t)t
         =rs t-2(r+s)+4/t.
\tag{5}
$$

Average a unit triangular lattice over its fundamental cell of area `a_0`.
The average number of sites in any bounded open region `U` is `|U|/a_0`:
integrating the sum of translated site indicators and using the lattice
tiling proves this directly. If `|U|/a_0>|S|-1`, some translate has at least
`|S|` sites. Apply Theorem 1.

**Theorem 3 — embedded-grain exclusion.** A canonical contact-minimal
triangle-free global source cannot contain an actual patch (1) for which

$$
 \boxed{rs(t-a_0)>(2-a_0)(r+s)-4/t,\qquad r,s>2/t.}
\tag{6}
$$

More generally, `|Q_{-1}|/a_0>|S|+k-1` certifies `|S|+k` wall-safe sites;
several such packets can be summed in Theorem 2.

This is a theorem on an embedded part of the actual source, unlike the
canonical affine-lattice competitor whose hypotheses cover the whole source.
For square `r=s=k`, the sufficient area threshold first holds at `k=15`.
Exact rational sine examples give `k=23` for `24/25`, `k=137` for `15/17`,
and `k=509` for `168/193`. These are thresholds for (6), not claims of minimal
possible repacking size. The explicit square packet below improves 15 to 7.

## 5. An explicit seven-face square packet with two spare sites

Take `u=(1,0)`, `v=(0,1)`, `r=s=7`. The old wall has 28 vertices and the
old interior has 36. Consider triangular-lattice sites

$$
 x_i={7+i\sqrt3\over2},\qquad y_{ij}=4+i/2+j.
\tag{7}
$$

Use `i=-3,-2,...,3`. For odd `i`, take the five values
`y=3/2,5/2,...,11/2`; for even `i`, take the six values `y=1,2,...,6`.
This gives `5+6+5+6+5+6+5=38` sites. Their difference squared is
`di^2+di*dj+dj^2`, so distinct sites are unit-separated.

All sites lie strictly inside `[0,7]^2` and are strictly unit-clear from
the 28 old wall vertices. For `i=+-3`, the closest side-wall squared gap
above one is `(73-42sqrt(3))/4>0`. For `i=+-2`, the closest top/bottom gap
is `(sqrt(3)-3/2)^2>0`; for `i=0` it is `1/4`. The `i=+-1` sites are
farther than one from all four supporting lines. Checking these cases or the
exact certificate establishes the guards.

Dilate all 38 points about `(7/2,7/2)` by `100001/100000`. The certificate
checks that the squared wall margin still exceeds `1/20`; all distinct new
sites now have distance greater than one.

**Corollary 4.** A canonical contact-minimal triangle-free global source has
no embedded `7 by 7` unit square patch. Replacing its 36 interior points with
36 of these strict sites removes exactly 84 contacts and creates none.
Interior points have no unit contact across the wall by the crossing lemma.

The remaining two sites can instead pay an actual diameter cover in Theorem 2.
For `p` disjoint such patches, `2p` spare sites are jointly compatible. Thus

$$
 2p\ge\nu(H)\quad\text{(forest)},\qquad
 2p\ge\nu(H)+1\quad\text{(cyclic)}
\tag{8}
$$

is an explicit strict-competitor condition. Corollary 4 already excludes one
patch in the contact-minimal representative; (8) is additionally useful when
contact minimality has not been imposed on a given source.

As a finite illustration, the full 64-point square grid has diameter squared
98 and two diameter edges. Delete its 36 interior vertices plus the two left
corners, a real cover of those edges; insert all 38 strict sites. The exact
same-cardinality competitor has diameter squared **85**. This demonstrates
the finite contract; it does not claim the old square grid was globally optimal.
Two adjacent patches are also checked jointly on a real 120-point source.

### 5.1 The certificate survives nonconstant train phases near a square

**Corollary 5 — stable actual-patch exclusion.** Suppose an actual source has
64 points `p_ij`, `0<=i,j<=7`, and, after one rigid motion,

$$
 |p_{ij}-(i,j)|\le1/50.
\tag{10}
$$

Assume every horizontal and vertical grid-neighbor pair is an actual unit
contact. A canonical contact-minimal triangle-free global source cannot contain
this patch. The conclusion does not require its individual train phases to be
constant.

**Proof.** The 28 unit wall edges form a simple polygon: distinct nonadjacent
unit contacts cannot cross by the crossing inequality in Section 2, and
unit separation excludes a source vertex in the interior of a unit edge.
During straight interpolation from the ideal wall to the actual wall, every
edge stays within `1/50` of its ideal edge. The 38 strict sites of Section 5
are more than `0.8` from the ideal wall. Its winding number about each site is
therefore unchanged and equals one, so each is inside the actual simple wall.
The same winding argument puts the 36 actual interior grid vertices inside it.

There are no additional source points inside the wall. Its convex hull lies
in `[-1/50,7+1/50]^2`. Any point of this box is within `1/sqrt(2)` of an
ideal grid vertex, by rounding each coordinate and clamping to `0,...,7`.
It is consequently within `1/sqrt(2)+1/50<1` of the corresponding actual
source vertex. An additional point would violate source unit separation.

For an actual wall vertex `b` and its ideal counterpart `b_0`, the packet's
distance obeys

$$
 |y-b|\ge|y-b_0|-1/50>\sqrt{21/20}-1/50>1.
$$

Thus the same exact 38-site packet lies in the actual strict wall-safe region.
Theorem 1 supplies the contradiction. All old non-neighbor grid distances
are at least `sqrt(2)-2/50>1`; the deleted 36 points lose the same 84 contacts.
Theorem 2's two-spare-site contract survives as well. ∎

For two exact shores with `u=(1,0)` and `|v-(0,1)|<=1/200`, centre the ideal
reference at the actual patch centre. The largest vertex discrepancy is at
most `(7/2)/200<1/50`, so Corollary 5 applies. More generally, in a consecutive
rhombic grid whose seven steps on each shore differ from their two orthogonal
reference directions by at most `1/700`, the accumulated position error is
at most `14/700=1/50`. This also meets (10). The exact verifier checks both
signs of the rational oblique perturbation
`v=(+-800/160001,159999/160001)`.

## 6. Hostile checks: the inverse-diameter and atomic obstructions survive

The assertion "any positive oblique angle excess allows a local strict
repacking" is false for a fixed two-face wall. Put the nine grid points at
`iu+jv`, `i,j in {-1,0,1}`, with `|u dot v|<1/2`, and retain the eight-point
wall. The origin is the **unique** point in its parallelogram at distance at
least one from every wall vertex.

**Proof.** In the diamond `R=conv{+-u,+-v}`, write a point `x` as a convex
combination of these four unit vectors. The weighted mean of its squared
distances from them equals `1-|x|^2`. For `x!=0`, at least one is less than
one. Outside `R`, the parallelogram is partitioned into four corner triangles
whose vertices are wall vertices. Each triangle has diameter squared less
than three. For barycentric weights on three vertices, their variance is at
most `(diameter squared)/3<1`, since `sum_{i<j}lambda_i lambda_j<=1/3`.
Again some wall distance is less than one. At the origin the four side-midpoint
distances equal one and the corner distances exceed one. ∎

Therefore the strict wall-safe region is empty. The old centre cannot be
strictified while retaining the wall, even at an angle arbitrarily close to
90 degrees. Four exact rational-angle packets check the boundary data; the
universal uniqueness proof is the preceding argument.

For a quadratic patch of size `r,s=Theta(D)`, (6) needs a sine excess of order
`1/D` with a definite coefficient. It does not exclude an arbitrarily small
inverse-diameter or smaller excess. The actual fixed-star branch is close to
60 degrees; the square certificate is not applied to that branch.

The floated triangular-lattice search at six faces found 23 strict sites in
70,000 sampled phases, below the required 25. This is an exploratory near miss,
not a packing upper bound, an exact regression, or a reason to reject a possible
nonlattice six-face competitor.

## 7. A marked Hall refinement and its geometric count regression

For a finite unit-separated test packing `B subset int K`, let
`N(T)={a in A: |a-t|<=1 for some t in T}`. In a contact-minimal triangle-free
global source, every subset with a contact-nonisolated point in `N(T)` satisfies

$$
 |N(T)|\ge |T|+1.
\tag{9}
$$

Indeed, if `|N(T)|<=|T|`, choose `|N(T)|` test sites, dilate them slightly in
`int K`, and delete `N(T)`. All cross distances to retained source points were
strict; a small dilation retains them. Cardinality is preserved, all new
contacts disappear, and at least one old contact is removed. Theorem 1's same
global-minimality comparison gives the contradiction. Thus any Hall-tight
blocker set can contain only actual contact isolates. This strengthens the
isolate-only formulation without applying KKT to those isolates.

Do not convert this one-unit Hall surplus into a linear population loss.
For a square grid with `r+1` points per side, take test sites at its `r^2`
cell centres. Each site has exactly its four old corners as unit-disk
neighbors. Any nonempty test subset has at least one more neighbor than sites:
inject sites to their lower-left corners, and use the upper-right corner of
a site with maximal `i+j` as an additional neighbor. All `(r+1)^2` old source
vertices are contact-nonisolated, yet the total surplus is only `2r+1`.
Both geometries are planar, unit-separated, and triangle-free. This is a
nonglobal exact regression to a population-only strengthening of (9).

## 8. Certificate, claim audit, and exact remaining obligation

Run

```bash
python3 research/verify_target_c_embedded_grain_replacement_2026_10_02.py
```

Arithmetic is `Fraction` in `Q(sqrt(3))`, with exact sign comparisons. It checks
all finite packet distances, the strict wall margin, the old diameter covers,
same cardinality, exact 98-to-85 decrease, simultaneous adjacent patches,
two rational stable oblique patches, four rational sine area thresholds,
the two-face boundary data, and the
geometric Hall regression. The universal proofs do not infer truth from
bounded numerical survival. No global optimum is computed or certified.

| Claim | Classification | Dependency/limit |
| --- | --- | --- |
| Embedded wall strictification and simultaneous refill | proved candidate awaiting promotion | full proofs; prior wall/refill ideas acknowledged |
| Oblique actual-patch exclusion (6) | proved candidate awaiting promotion | canonical contact-first source; consecutive affine patch |
| 38-site square packet and cover/refill | proved candidate awaiting promotion | exact certificate; full-source wall shield |
| Nonconstant-phase near-square patch exclusion (10) | proved candidate awaiting promotion | actual unit wall; explicit uniform geometric perturbation |
| Marked Hall surplus (9) | proved candidate awaiting promotion | contact-first global normalization |
| Two-face unique-centre obstruction | regression | exact source geometry; no global-optimality claim |
| Hall surplus versus quadratic contact population | regression | geometric grid; not a global minimizer |
| Six-face numerical search | unreviewed exploratory candidate | no packing upper bound |

**Precise next obstruction:** obtain, on an actual surviving fixed-star source,
enough **consecutive** rhombic wall patches whose certified packing surplus pays
an actual diameter cover, or one patch with fixed-wall capacity at least its
old interior population. This requires either a boundary-compatible packing
certificate at inverse-diameter phase excess or a theorem extracting a larger
excess patch. Retained nonconsecutive trains alone do not provide it.

No inference gives such patches from the current canonical inputs. The atomic
regression prevents claiming that any nonzero phase excess suffices at fixed
size. Nonconstant-phase lower blockers, positive-circulation chart isolation,
split-star O-O, inactive-interface, high-surplus full-core, and macroscopic
inactive-container/exterior-cap branches remain open.

**Promotion status:** the embedded wall shield, simultaneous diameter-cover refill, consecutive oblique patch exclusion, and exact/stable 7-by-7 packet were independently audited and promoted in `2026-10-05.audit.54`.

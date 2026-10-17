> Generated reading edition · [exact source](../../../../docs/targets/target-a/29-lens-source-gate-refinements.md) · source SHA-256 `ee1d31457082639f55a90b1474bfc92753c0a7dc4fc828a65bdd2fe5643ca550`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target A — independently audited lens and source-gate refinements

This module records three post-Section-176 refinements that survive an independent
proof/dependency audit on 2026-09-11:

1. a two-site-per-contact-edge **lens shield** for the locked Schur network;
2. a boundary-order family of pairwise disjoint **genuine-source V-paths** from
   actual Schur terminals to actual exterior sinks in the zero-slack branch; and
3. a **phase-aligned straight-crosscut** whose interior-lattice tube costs only
   `2L+O(1)` sites instead of the full-torus average `4L/sqrt(3)+O(1)`.

The audit also rechecked the load-bearing chain behind the current Sections 175–176:
Sections 97, 122, 124, 138, 159, 164–165, 168–169, and 171–176. No invalid implication
was found in that chain. The statements below are proved directly rather than promoted
from a self-audit label.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 177. Edge-lens Schur shielding and zero-slack source gates

Retain the plateau-terminalized response notation. Thus

- `X^*` is the actual response optimum in `K^*`;
- `Y_in=Z sqcup O` is the generic triangular-lattice response shore;
- `mu_0:B->Z` is the fixed perfect basis matching;
- `C^partial` is the Schur terminal set;
- `zeta=|C^partial|-rank S`; and
- in the locked branch a stress-generated unit-contact shield `Sigma` is available.

The full unit tube of Section 175 remains the cleanest route when one wants disjoint
sector sink sets. The lens shield below is different: it minimizes the right-shore
vertices needed merely to stop response edges from crossing the contact graph, and it
keeps possible exterior-sink overlap in the Section-173 coarse Hall graph.

## 177.1 A crossing response edge lands in both endpoint neighborhoods

Let `pq` be a unit contact of `X^*`, let `x in X^*\{p,q}`, and let `y in Y_in` satisfy
`|x-y|<1`.

### Lemma 177.1 — two-endpoint crossing transport

If `[x,y]` properly crosses `[p,q]`, then

`boxed{|y-p|<1 and |y-q|<1}`.

The same conclusion holds when the right endpoint `y` lies in the relative interior
of `[p,q]`.

### Proof

Let `z` be the proper crossing point. Unit separation of `X^*` gives

`|x-p|>=1`, `|x-q|>=1`.

The triangle inequality through `z` gives

`|x-p|+|y-q|`
`<=|x-z|+|z-p|+|y-z|+|z-q|`
`=|x-y|+|p-q|<2`.

Hence `|y-q|<1`. Interchanging `p,q` gives `|y-p|<1`.

If `y` lies in the relative interior of the unit segment `[p,q]`, both endpoint
distances are automatically below one. A nontrivial collinear overlap with a surviving
response edge is impossible: if `x` is distinct from `p,q`, then reaching the relative
interior of `[p,q]` from `x` already requires distance at least one, while
`|x-y|<1`. QED.

This strictly strengthens the one-endpoint crossing rule used in Section 169.

## 177.2 Every unit-contact lens contains at most two lattice sites

For a unit contact `pq`, define the open right-shore lens

`L(pq)=N_Lambda(p) cap N_Lambda(q)`.

### Lemma 177.2 — two-site lens bound

For the unit triangular lattice,

`boxed{|L(pq)|<=2}`.

Under the generic response phase the lens also contains at least one site, although
the lower bound is not needed for shielding.

### Proof

After a rigid motion take `p=(-1/2,0)` and `q=(1/2,0)`. The open lens
`B(p,1) cap B(q,1)` has strict diameter below `sqrt(3)`: its closure is centrally
symmetric and its extreme vertical points are `(0,+-sqrt(3)/2)`.

Squared distances between triangular-lattice sites have the form

`a^2+ab+b^2`, `a,b in Z`.

There is no value two. Therefore any two distinct lattice sites in the open lens are
at distance exactly one; otherwise their distance is at least `sqrt(3)`. If three
lattice sites were present, they would form an elementary unit equilateral triangle.
Both `p` and `q` would then lie in the interior of all three unit disks centered at
those sites, hence in the interior of their unit Reuleaux triangle. That Reuleaux
triangle has diameter one, and two interior points have distance strictly below one,
contradicting `|p-q|=1`. Thus at most two sites occur.

For the optional lower bound, apply the proof of Section 164.1 at the generic endpoint
`p`. Genericity makes every adjacent outside-lattice distance appearing there strictly
greater than one, so the distance from `p` to the complement of the union of its
strict-neighbor unit disks is strictly greater than one. Hence the point `q`, at
distance exactly one from `p`, still lies in one of those open disks. QED.

## 177.3 Lens-sector trapping

For a finite unit-contact shield `Sigma`, put

`L_Sigma=(union_(pq in E(Sigma)) L(pq)) cap Y_in`.

### Theorem 177.3 — edge-lens geometric shield

No response edge of

`G-(V(Sigma) sqcup L_Sigma)`

intersects `|Sigma|`. Consequently every surviving internal response component is
contained in one component of `K^*\|Sigma|`. Moreover

`boxed{|L_Sigma|<=2|E(Sigma)|}`.

### Proof

A surviving response edge cannot start at a contact-shield vertex. It also cannot pass
through a distinct shield vertex: an interior point `p in X^*` on a response segment
of length below one would satisfy `|x-p|<1`, contradicting unit separation of `X^*`.
If the response edge meets the relative interior of a contact edge, Lemma 177.1 puts
its right endpoint in the corresponding lens and hence in `L_Sigma`, contradiction.
The collinear case was excluded in Lemma 177.1. Thus the surviving response graph does
not cross the contact shield.

The component statement follows because all internal response vertices lie in `K^*`
and their response segments lie in `K^*` by convexity. The cardinality bound is the
union bound from Lemma 177.2. QED.

Unlike the full unit tube, the lens shield does not force an exterior sink to belong
to only one sector. This is intentional: sink overlap is retained exactly by the
coarse sector graph of Section 173.

## 177.4 Exact contracted-gammoid lens penalty

Contract every matched `Z-B` pair of the Section-113 alternating gammoid. Put

`L_Z=L_Sigma cap Z`, `L_O=L_Sigma cap O`,

and define the uncovered basis-contact count

`beta_Sigma`
`=|{b in B cap V(Sigma):mu_0(b) notin L_Z}|`.

Shield in the contracted graph

1. every contracted pair indexed by `L_Z`;
2. every additional contracted pair indexed by a basis contact vertex counted by
   `beta_Sigma`;
3. every terminal in `C^partial cap V(Sigma)`; and
4. every sink in `L_O`.

Let `delta_Sigma^lens` be the Section-173 coarse Hall deficiency after this deletion,
with overlapping sector sink sets retained.

### Theorem 177.4 — lens-shield Schur nullity

`boxed{zeta >= delta_Sigma^lens-|L_Sigma|-beta_Sigma}`.

Therefore the exact lens-route Target A closure is

`boxed{delta_Sigma^lens >= s+|L_Sigma|+beta_Sigma}`,

where `s=Delta_Lambda-d_int`.

### Proof

A matched `Z-B` pair is an indivisible internal directed unit. In the alternating
orientation the matched `Z` vertex has only its matching edge as an outgoing edge, and
the matched basis vertex has only that edge as an incoming edge. Contracting the pair
therefore preserves vertex-disjoint Schur linkages.

After the lens and contact deletions, Theorem 177.3 traps every internal directed path
in one geometric sector. Delete from a maximum Schur linkage every path that uses a
shielded contracted pair or a lens sink. At most `|L_Sigma|+beta_Sigma` such internal
units/sinks are charged. A path beginning at a shield terminal is also deleted, but
those terminal losses cancel when the linkage bound is subtracted from
`|C^partial|`. Deep nonbasis shield vertices cannot occur internally because nonbasis
left vertices have no incoming alternating edge.

Every remaining path starts in one sector and ends at one of that sector's allowed
exterior sinks. Distinct paths give a matching in the Section-173 coarse sector-sink
graph, so the number of remaining paths is at most its maximum matching. Hall's
deficiency formula then gives the displayed nullity bound. QED.

### Locked-fan specialization

For the unit triangle core, the union of its three edge lenses contains at most four
lattice sites. Indeed two sites chosen from any two edge lenses are both within unit
distance of a common triangle vertex, so the whole union has strict diameter below
two. Partitioning the triangular lattice into the four cosets of `2Lambda` gives the
four-site bound.

For the locked connected unicyclic three-channel fan with `v` vertices, the remaining
`v-3` contact edges form channel trees. Hence

`boxed{|L_Sigma|<=4+2(v-3)=2v-2}`.

The trivial `beta_Sigma<=v` then gives

`|L_Sigma|+beta_Sigma<=3v-2`.

The gain is primarily structural: the right-shore term is crossing-local, and the
remaining extra cost is the explicit basis quantity `beta_Sigma`.

## 177.5 Boundary-terminal common-source V-paths

Now assume the zero-slack branch of Section 168. Choose independently

- a saturating source matching `M_C:C^partial->A^0`, obtained from the full
  `X^*->A^0` matching; and
- a saturating source matching `M_O:O->A^0`, obtained from the full
  `Y_in->A^0` matching.

Let their source-image sets be `S_C,S_O subset A^0`. They must not be identified as
matchings.

### Lemma 177.5A — two-sided boundary-band packing

If `A` is unit-separated and `K` is convex with perimeter `P`, then the number of
points of `A` at distance below `w` from `partial K` is at most

`[8(w+1/2)/pi]P+4(w+1/2)^2`.

For `w=2` and `K=K^*`, this is at most

`boxed{20d+25}`.

### Proof

Radius-`1/2` open disks centered at the counted points are disjoint. With
`r=w+1/2`, all of them lie in the two-sided radius-`r` boundary tube. Steiner gives
outer-tube area `rP+pi r^2`. Coarea for the inner parallel bodies gives inner-layer
area at most `rP`, because their perimeters do not exceed `P`. Thus the total tube area
is at most `2rP+pi r^2`. Divide by `pi/4`. For `w=2`, use `P<=pi d`. QED.

Every `c in C^partial` lies within one of `partial K^*`; its source label is within
one of `c`, so every point of `S_C` lies within two of the boundary. Every `o in O`
lies in the exterior width-one response collar; its source label is also within one,
so every point of `S_O` lies in the same two-sided width-two band. Hence

`|S_C cap S_O|`
`>=max(0,|C^partial|+|O|-20d-25)`.

Every common source point `a` has unique partners `c(a)` and `o(a)` and gives a
physical two-arm V-path

`c(a)-a-o(a)`

with both arms shorter than one.

### Theorem 177.5B — disjoint source-gate floor

There are at least

`boxed{G_CO >= (1/10) max(0,|C^partial|+|O|-20d-25)}`

pairwise disjoint polygonal V-paths

`c_i-a_i-o_i`,

with all `c_i`, all `a_i`, and all `o_i` distinct.

### Proof

Within either strict-conflict matching, the straight matching segments are pairwise
disjoint by Section 163. Thus two different V-paths can interfere only when a
`C^partial` arm of one meets an `O` arm of another.

For such an intersection, Section 163's crossing transport applies to the two
unit-separated endpoint shores and forces the response endpoints `c,o` to satisfy
`|c-o|<1`. A fixed response point has at most four strict triangular-lattice
neighbors, so one `C` arm meets at most four `O` arms. Conversely a fixed lattice
endpoint lies within one of at most five points of the unit-separated response set, so
one `O` arm meets at most five `C` arms. The V-path interference graph therefore has
maximum degree at most nine. Greedy independent-set selection retains at least one
tenth of its vertices. QED.

This theorem is a source-geometry resource, not a Schur-rank theorem. A selected gate
may remain in one contact-shield sector or may consume shield/interface geometry. A
future proof must quantify that dichotomy rather than infer nullity from gate count.

## 177.6 Phase-aligned straight-crosscut tube

The right-deficiency path-deletion argument of Section 175 works for an embedded
geometric crosscut `Gamma` as well as a contact shield, provided surviving response
edges cannot cross it without using a right-shore tube vertex. For a straight chord we
can choose the response translation more efficiently than full-torus averaging.

Fix a primitive unit lattice direction `e`; parallel lattice rows have spacing

`h=sqrt(3)/2`.

Choose a line `ell` parallel to `e` which crosses `int K^*`, avoids `X^*`, is not
tangent to `K^*`, and whose induced midrow row family does not coincide with a
parallel hull edge. Only finitely many relevant normal offsets are forbidden, so such
`ell` exists. Translate the lattice normally so `ell` lies halfway between two adjacent
rows. The adjacent rows are at distance `sqrt(3)/4<1`; the next rows are at distance
`3sqrt(3)/4>1`. Thus only the adjacent two rows enter the open unit strip.

Let `Gamma=ell cap K^*` and `L=length(Gamma)`. On either adjacent row a lattice site
is within unit distance of `Gamma` only when its longitudinal coordinate lies in the
segment projection enlarged by

`sqrt(1-3/16)=sqrt(13)/4`

at each end. The open interval length is therefore

`L+sqrt(13)/2`.

Unit-spaced sites on one row contribute at most the ceiling of this length.

### Theorem 177.6 — phase-aligned straight tube

There is an admissible generic response translation for which

`boxed{|T_Z(Gamma)|<=2 ceil(L+sqrt(13)/2)}`.

Delete the full open right-shore unit tube

`T_Gamma={y in Y_in:dist(y,Gamma)<1}`.

Let the two components of `K^*\Gamma` define the surviving terminal sectors. A
surviving exterior sink belongs to at most one sector: if a sink `o notin T_Gamma`
had surviving neighbors `x_+` and `x_-` in opposite components, the segment
`[x_+,x_-]` would meet `Gamma` because `K^*` is convex. Both endpoints lie in the
open unit disk `B(o,1)`, so the entire segment lies in that disk; its crossing point
with `Gamma` would therefore have distance below one from `o`, contradicting
`o notin T_Gamma`. Thus the surviving exterior-sink sector sets are disjoint.

Let

`Xi_Gamma=|O_iso(Gamma)|`
`+sum_i max(0,|O_i(Gamma)|-|C_i^partial(Gamma)|)`.

The Section-175 path-deletion argument now applies verbatim. The full tube charge is
`|T_Gamma|=|T_Z(Gamma)|+|T_O(Gamma)|`, while the right-shore decomposition contains
`T_O(Gamma)` with the same sign, so exterior tube sinks cancel. Hence

`h(G)>=Xi_Gamma-|T_Z(Gamma)|`
`>=Xi_Gamma-2 ceil(L+sqrt(13)/2)`.

Since `L<=d`, the shield cost is `2L+O(1)`, improving the full-torus averaged leading
coefficient `4/sqrt(3)` for this straight-crosscut route.

### Genericity justification

After the normal translation is fixed, one parallel translation parameter remains.
For the bounded response region, lattice coincidences, unit-distance equalities, and
boundary incidences exclude only finitely many parameter values unless a lattice row
coincides with a hull edge; that possibility was excluded when `ell` was chosen.
Hence a generic member of the midrow family exists.

This is a pointwise alternative, not an averaged theorem. It still requires a lower
bound on `Xi_Gamma` strong enough to pay the residual collar demand and the explicit
`2L+O(1)` tube cost.

## 177.7 Correct current Target A frontier

Sections 175–177 now give three exact separator currencies.

1. **Full tube, disjoint sink sectors:**
   `h>=Xi_Sigma-|T_Z|`, so it suffices to prove
   `Xi_Sigma>=j_*+|T_Z|`.
2. **Edge lens, overlapping sinks handled by coarse Hall:**
   `zeta>=delta_Sigma^lens-|L_Sigma|-beta_Sigma`, so it suffices to prove
   `delta_Sigma^lens>=s+|L_Sigma|+beta_Sigma`.
3. **Straight geometric crosscut:** choose a midrow phase and pay at most
   `2 ceil(L+sqrt(13)/2)` interior tube sites.

In the zero-slack branch, Section 176 and Theorem 177.5B additionally provide a
near-full genuine source inside `K^*`, sector-local source labels up to boundary order,
and a boundary-order-explicit disjoint `C^partial-A^0-O` gate family.

None of these results proves the required right-sector surplus or coarse Hall
deficiency. The remaining mathematical obstruction is to convert global
minimum-diameter/source geometry into one of the exact separator inequalities above,
or into a strict sub-`D` competitor. The bookkeeping/topological parts of these
routes are no longer the open issue.

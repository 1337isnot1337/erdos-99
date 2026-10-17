# Target C — loaded collar face and direction payment

```text
loaded rhombic collar -> angular spread of actual opposite unloaded edges
or nonquadrilateral face/bridge payment -> exact e_BB, Q, and outer-walk ledger
-> a strict competitor or contradiction still requires eliminating the paid branch.
```

Date: 2026-10-02. Initial checkout HEAD:
`fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`.
Fetched research base / branch starting HEAD:
`3bad7c12bf5133665be466d0396362108fadef2c`.
State version: `2026-09-14.audit.51`.
Owned branch: `swarm/sol/source-cap-stress-20261002`.
Mission: actual-source loaded collar / contact-face coupling, after checking the
new threshold, midpoint-energy, and ball-hull packets. No assigned mission or
open coordination issue was present in the fetched GitHub state.
Classification: **proved candidate awaiting promotion**; artifact lifecycle
**unreviewed**. The pentagon construction is a **regression**.
Level I / C-II: **OPEN**. No promotion is made.

## 1. Dependencies and scope

Canonical inputs: `C-FULLCORE-NEAR-DISK` (Section 80),
`C-FULLCORE-LOADED-CHORD` (the September 14 loaded-chord report),
`C-LOADED-HULL` (Section 63), and `C-RHOMBUS-POP` (Section 67,
convex bounded faces and strict unit rhombi). The positive-contact core and its
unloaded components are the actual source objects. Contact isolates remain in
all source constraints. No full-source stress-kernel theorem is assumed.

The current main ball-hull atlas, midpoint, threshold, and convex-bank reports
were inspected for scope; none is a premise. The new finite geometry below is
proved directly. The near-disk application is confined to the canonical
full-core branch, leaving macroscopic containers and the other C-II mechanisms
untouched.

## 2. A finite tangent-direction capacity

Let a convex polygon `F` satisfy `B(0,r) subset F subset B(0,R)`, with
`0<r<=R`, and put `kappa=acos(r/R)`. Let `E` be a measurable subset of the
projective direction circle `R/pi Z`, and let `E^kappa` denote its closed
angular `kappa`-neighborhood. Count unit hull sides whose projective directions
belong to `E`. Then

\[
 N_E\le {2R\over\cos\kappa}|E^\kappa|.                 \tag{CD.1}
\]

**Proof.** At almost every boundary point `p`, let `n` be the outward normal,
`t` the counterclockwise unit tangent, and `psi=arg(p)`. Since
`n.p>=r` and `|p|<=R`, `angle(n,p)<=kappa`. Also

`d psi/d s=(p cross t)/|p|^2=(p.n)/|p|^2>=cos(kappa)/R`.

This holds on every side; vertices contribute no arclength. An edge with
projective direction in `E` has every point's radial angle in the two lifts
of `E^kappa`, shifted by `pi/2`. These lifts have total measure
`2|E^kappa|`. Radial angle increases once around the polygon because the
origin lies in its interior. Integrate the displayed derivative on these
arcs. Every counted side has length one. This proves (CD.1). No source,
completion, lattice, or stress is introduced by this proof.

For **exact** directions the simpler bound is `N_E<=2|E|` when `E` is finite:
a convex polygon with strictly extreme vertices has at most one side in each
oriented direction. In particular the unit contacts of `K` exact rhombic
charts have at most `2K` projective directions, hence can supply at most `4K`
loaded unit hull sides. Translations of charts do not increase that number.

For the canonical full-core sequence `r/D,R/D->1/2`. If `E_D` is a union of a
bounded number of intervals of total width `o(1)`, (CD.1) is `o(D)`.
This is a direction-capacity theorem, not a proof that source collar directions
have that concentration.

## 3. Small-face payment without a chart assumption

All statements in this section concern sufficiently large canonical full-core
sources. Let `z_B` be the number of loaded-loaded unit contacts that are bridges
of the actual positive-contact core. Let `E_R` be the number of loaded-loaded
contacts incident to an old bounded quadrilateral face.

The loaded-chord theorem makes every loaded-loaded unit contact a side of `F`.
Every nonbridge such edge therefore borders exactly one old bounded face on its
interior side. A bridge instead has the old outer face on both sides.

### 3.1 A rhombus cannot have three loaded vertices

At every hull-side midpoint `p`, its outward normal makes angle at most
`kappa=acos(r/R)` with `p`. For all side midpoints within distance seven of
one point of `F`, the oriented tangent directions lie in a cone of width at most

\[
 \omega_D=2\kappa+4\arcsin(7/(2r))=o(1).              \tag{CD.2}
\]

The radial-angle bound follows from
`|p-q|>=2r sin(angle(p,q)/2)` for `|p|,|q|>=r`.

Three loaded vertices of a unit rhombus contain two consecutive loaded-loaded
unit sides. Their turn is between `pi/3` and `2pi/3`: the unit-separated,
triangle-free rhombus has interior angles strictly between those values.
Equation (CD.2) contradicts that turn. Thus a rhombus incident to a loaded unit
edge has exactly two loaded vertices; its opposite side is an actual
unloaded-unloaded unit contact, parallel to that loaded edge.

Let `J` be any set of projective directions containing these **actual opposite
edges**. Then

\[
 E_R\le 2|J|\quad\hbox{for finite }J,\qquad
 E_R\le {2R\over\cos\kappa}|J^\kappa|.               \tag{CD.3}
\]

The second inequality uses angular measure; the first uses cardinality.
Do not conflate those two uses of `|J|`.

### 3.2 A general exact exceptional-face bound

For a bounded face of degree `j=5,6,7`, let `L` count its loaded-loaded sides.
Its side midpoints are within distance seven of one another. Those `L` sides,
oriented with the face counterclockwise, agree with their hull orientation.
For sufficiently large `D`, their projections on one unit vector exceed `4/5`.
The remaining `j-L` unit sides have projection at least `-1`. Closure gives
`(4/5)L<j-L`. Consequently `L<=2,3,3`, respectively.
For `j>=8`, `L<=j<=2(j-4)`. Summing, exactly,

\[
 e_{BB}\le z_B+E_R+2Q.                               \tag{CD.4}
\]

Every edge on the left is accounted for. Neither bridges nor the nonrhombic
boundary are silently discarded.

### 3.3 Repair: only a two-loaded-edge pentagon needs the extra payment

A sharper full-core bound is

\[
 \boxed{e_{BB}\le z_B+E_R+Q+P_2,}                    \tag{CD.5}
\]

where `P_2` counts old pentagonal faces with two loaded-loaded sides. The two
sides of each such pentagon are consecutive.

**Proof.** Suppose a nonquadrilateral face has `L>j-4` loaded-loaded sides.
Then at most three of its sides are not loaded-loaded. If it has no unloaded
vertex, all its sides are hull sides and the face is `F`; that contradicts
canonical rhombic saturation `A_4=area(F)-o(D^2)`.
Otherwise there is exactly one block of unloaded vertices on its boundary:
two different blocks would require at least four loaded-unloaded transitions.
Thus its loaded-loaded sides form one consecutive hull chain, closed by a
path of at most three unit edges. The chain endpoints are at distance at most
three.

The two endpoints have radial angular separation `o(1)`. The short hull arc
between them has length at most
`(2R/cos(kappa)) asin(3/(2r))=3+o(1)` by the same radial derivative as CD.1.
The other hull arc is the long one. Closing that long arc by a path of length
at most three produces a face occupying `area(F)-o(D^2)`: after normalization,
the endpoints and the return path converge to one point of the limiting disk,
and the long boundary arc converges to its entire boundary. This again
contradicts rhombic saturation. Therefore the chain is the short arc, and its
integer number `L` of unit edges is at most three.

If `j>=7`, the assumed `L>=j-3` is at least four, a contradiction. If `j=6`,
the only remaining possibility has three hull edges and a three-edge return.
The hull edges have directions converging to one common tangent; their endpoint
distance tends to three. Equality stability in the triangle inequality for
three unit return vectors makes those vectors converge to the negative tangent.
The two internal return vertices then converge to the two internal loaded
chain vertices, respectively, violating unit separation. This is a finite
compactness argument: after translating an endpoint and rotating the first
hull edge, all six vertices are in a fixed radius-six ball, and any putative
sequence has the forbidden limit just described.

For `j=5`, `L=2` is possible. Closure and convexity put the two nearly parallel
loaded sides consecutively: if another face side lay between them in cyclic
edge-angle order, it too would have projection tending to one, and the other
two sides could not balance the resulting projection approaching three.
Thus the only exception is precisely the pentagon counted by `P_2`.
For all other faces `L<=j-4`. Summing proves CD.5.

The long-arc exclusion uses actual rhombic area saturation. It is not a theorem
for an empty shell or a macroscopic inactive container.

## 4. Loaded bridges are paid by the exact outer-walk slack

Let `m_B` count nonunit hull sides and `u_B=x_B-m_B`, as in Section 63.
Then, for sufficiently large full-core sources,

\[
 \boxed{z_B\le u_B.}                                \tag{CD.6}
\]

### Proof

First a loaded vertex cannot have just one contact and have that contact's
other endpoint loaded. Its contact vector would be parallel to its positive
net diameter force, hence an outward supporting normal of `F` at that vertex.
Its unit loaded-loaded edge is also a hull side, with perpendicular supporting
normal. Both support values are at least `r`; thus that vertex has norm at
least `sqrt(2)r`. This contradicts `R<sqrt(2)r`, which eventually holds.

Augment `G` by its `m_B` missing hull sides. Canonical Section 67 makes this
augmented graph 2-connected with convex bounded faces. Its new faces are the
pockets cut from the old outer face. Consider a maximal run of hull sides on
one pocket boundary. Two consecutive added sides would leave their shared
loaded vertex with no original contact. An added side next to an original
unit hull side would leave their shared loaded vertex with only that one unit
loaded contact. In both cases the pocket occupies the full tangent sector of
`F` there, so no other original contact can leave that vertex. Both cases
are impossible by the preceding paragraph and positive load requiring contact.
Therefore every added side is a singleton hull run on its pocket boundary.

Between successive hull runs the pocket boundary has a path of original
contacts with internal unloaded vertices. Such a path has at least two edges.
If a direct loaded-loaded contact joined its endpoints instead, it would be a
hull side by the canonical loaded-chord theorem and the runs were not maximal.
Hence the total number `N` of non-loaded-loaded edge occurrences on the old
outer walk satisfies `N>=2m_B`. This counts occurrences, including both
traversals of a non-loaded bridge where necessary.

Every nonbridge loaded-loaded hull edge appears once on the old outer walk;
every loaded-loaded bridge appears twice. Therefore

`b=e_BB+z_B+N`.

Since `q=e_BB+m_B` and `b=q+x_B`,

`u_B=x_B-m_B=z_B+N-2m_B>=z_B`.

This proves CD.6. No Euler-trail inference about the diameter graph is used.

Combining CD.5--CD.6 with `e_BB=Q+2k+u_B`, `k=d_H+s_Z`, gives the new exact
normal-form gate

\[
 \boxed{2(d_H+s_Z)+(u_B-z_B)\le E_R+P_2.}            \tag{CD.7}
\]

This couples Woodall/mixed deficiency to actual loaded rhombi and actual
pentagons; it is not a dimensional argument about a virtual chart.
## 5. The surviving pentagon gives two distinct near-unit source pairs

Take a unit pentagon in cyclic order `p0,p1,p2,x,y`, with its two loaded hull
sides `p0p1,p1p2`. Write its positive hull turn as `delta` and, after an
isometry, put

`p1=0`, `p0=(-c,-s)`, `p2=(c,-s)`,
`c=cos(delta/2)`, `s=sin(delta/2)`.

The unit edges give `|x|^2=2p2.x` and `|y|^2=2p0.y`, and `|x|,|y|<=2`.
Unit separation then implies

`x_1 >= (1/2-2s)/c`, `y_1 <= (-1/2+2s)/c`.

Since `x_1-y_1<=|x-y|=1`, substitution back into the squared-length identities
gives

\[
 \boxed{1<|p1-x|,|p1-y|\le\sqrt{1+8s}\le1+2\delta.}   \tag{CD.8}
\]

The strict lower inequalities hold because equality would create a unit
triangle with `p2` or `p0`, respectively. At `delta=0` both are forced equal
to one, so the flat pentagon itself is impossible in a triangle-free source.
The estimate assumes `c>0`; this holds for these small-turn full-core faces.

Each such pentagon has its own middle loaded vertex and consumes that vertex's
hull turn. No two can use the same middle vertex: its two hull sides have only
one interior face sector. Hence

\[
 \sum_{P_2}\delta\le2\pi,\qquad
 \boxed{\sum_{P_2}[(|p1-x|-1)+(|p1-y|-1)]\le8\pi.}    \tag{CD.9}
\]

These are `2P_2` **distinct actual inactive source pairs**, not hypothetical
ports. If `P_2>=aD`, all but at most `eta P_2` pentagons have both diagonals
at most `1+4pi/(eta aD)`, for every fixed `0<eta<1`.
Neither the weights of these pairs nor their exact activity is inferred.

### 5.1 Couple their bottom directions to the same source direction capacity

For `delta<=1/16`, the bottom unit vector `w=x-y` satisfies
`w_1 >= (1-4s)/c >=1-4s`. Thus

`angle(w,(1,0)) <= pi sqrt(delta)`.

The two loaded sides have direction angles `+delta/2` and `-delta/2` relative
to that mean tangent. Each is within `4sqrt(delta)` of the bottom direction.
(The inequality `1-cos t>=2t^2/pi^2` on `[0,pi]` proves the displayed bound.)

Let `E_D` contain the actual unloaded opposite-edge directions in Section 3.1
and the actual unloaded bottom-edge directions of these pentagons. For
`0<epsilon<=1/4`, there are at most `32pi/epsilon^2` pentagons with
`delta>epsilon^2/16`, by the turning budget. Each remaining pentagon supplies
two distinct loaded hull sides in `E_D^epsilon`. Equation CD.1 therefore gives

\[
 P_2\le {32\pi\over\epsilon^2}
       +{R\over\cos\kappa}|E_D^{\epsilon+\kappa}|.   \tag{CD.10}
\]

Combining with CD.3 and CD.7 proves

\[
 \boxed{2(d_H+s_Z)+(u_B-z_B)
 \le {32\pi\over\epsilon^2}
    +{3R\over\cos\kappa}|E_D^{\epsilon+\kappa}|.}     \tag{CD.11}
\]

This is the main new source-level inequality. If `E_D` lies in a bounded number
of angular intervals of total width `o(1)`, choose `epsilon_D->0` with
`epsilon_D^(-2)=o(D)`. Since `kappa_D->0`, its right side is `o(D)`. Consequently

\[
 \boxed{d_H+s_Z=o(D),\qquad u_B-z_B=o(D).}            \tag{CD.12}
\]

For `K` exact chart directions, the same argument yields
`O(D K kappa + K^(2/3) D^(2/3))` (with harmless bounded-`K` terms).
There is no asserted `D^(2/3)` rate for canonical near-disk convergence itself.

The direction hypothesis concerns the **actual collar faces**, rather than one
quadratic grain selected far from that collar. It has not been established for
all canonical sources. Even with it, CD.12 does not eliminate the surviving
small-deficiency high-surplus full-core branch.

## 6. Exact regression: the near-unit pentagon survives at inverse diameter

For `0<t<=1/64`, let

`c=(1-t^2)/(1+t^2)`, `s=2t/(1+t^2)`,
`h=sqrt(1-(c-1/2)^2)`, `D=1/s`, `o=(0,-D/2)`.

Use the eight actual source points

\[
 p0=(-c,-s),\quad p1=(0,0),\quad p2=(c,-s),\quad
 x=(1/2,-s-h),\quad y=(-1/2,-s-h),\quad
 q_i=2o-p_i\quad(i=0,1,2).                            \tag{CD.13}
\]

The top five points are a strict convex unit pentagon. Their only contacts are
`p0p1,p1p2,p2x,xy,yp0`. Its two missing diagonals have squared length

\[
 |p1-x|^2=|p1-y|^2
 =1+(c-c^2)+s^2+2sh>1.                              \tag{CD.14}
\]

All `p_i,q_i` lie on the circle `B(o,D/2)` and are actual antipodal diameter
pairs. The two points `x,y` are strictly inside that circle. Cross distances
to the bottom triple exceed one; its only contacts are `q0q1,q1q2`.
Thus the eight-point source is unit-separated and triangle-free with diameter
**exactly** `D` and three actual diameters. Since `s=1/D`, the two inactive
diagonal excesses are `O(1/D)` and never vanish.

This refutes the proposed local implication

`two loaded hull sides + a unit pentagon + arbitrarily small turn
 -> an exact unit triangle`.

It supplies no global-optimality, full-core population, or positive-stress
certificate. In particular its unloaded pentagon vertices have contact degree
two, contrary to canonical unloaded equilibrium. That omitted hypothesis
is decisive and remains explicit.

### 6.1 The private reflection fails, but its companion move succeeds locally

Reflect `p1` to `p1'=(0,-2s)` and hold all other points fixed. Its two top
contacts are preserved and `p1'q1<D`, but

`|p1'-x|^2=|p1'-y|^2=1+(c-c^2)+s^2-2sh<1`.

The finite exact reflection is blocked by the two previously strict pairs.
Now translate `x,y` downward by `2s` at the same time. The reflected point
remains strictly separated from both, `p2x` and `p0y` open, and `xy` stays unit.
All other pairs stay separated, all three moved points remain in the same
circle, and only the two old antipodal pairs `p0q0,p2q2` retain diameter `D`.
The eight-point contact count falls from seven to five.

This is a finite motion of this actual source, with every pair certified below.
It proves that the displayed source is not a contact-minimal global minimizer.
It is not a finite motion of an arbitrary canonical source: unloaded positive
vertices `x,y` must have additional backside contacts. Positive equilibrium
requires a contact vector with negative projection on the face's inward
translation at each of `x,y`; the proposed translation would shorten that
contact unless its other endpoint also moves. They cannot share one such unit
neighbor, because `xy` is unit and that would create a unit triangle.
Thus the repaired local move requires **two actual distinct continuation
neighbors** and a simultaneous extension through their source components.
The old inactive diagonals alone are not the end of the obstruction.

## 7. Next attempted repair fails: one-edge pentagons transmit free directions

A tempting repair to CD.12 is to claim that *all* loaded collar directions
are inherited from a coherent unloaded chart. A pentagon with only one loaded
edge disproves that local geometric assertion.

Take `1/sqrt(2)<a<sqrt(3)/2`, put `b=sqrt(1-a^2)`, and set

`A=(-a,0)`, `B=(0,-b)`, `C=(a,0)`.

These three unloaded points lie in the one exact unit lattice generated by
`u=(a,b)` and `v=(a,-b)`. Their two unit directions have acute angle greater
than `pi/3`, approaching it as `a->sqrt(3)/2` from below.

For a small angle `theta`, set `d=(cos(theta),sin(theta))`,
`w=2a(1,0)-d`, `lambda=sqrt((1-|w|^2/4)/|w|^2)`, and

\[
 P=-d/2+\lambda Jw,\qquad Q=P+d.                     \tag{CD.15}
\]

Then `AP,PQ,QC,CB,BA` are all unit. At `theta=0` this is the strictly convex
pentagon with top edge `PQ` at height `sqrt(1-(a-1/2)^2)`; every other pair
is strictly longer than one. These strict inequalities and convexity persist
on an open interval of `theta`, uniformly as `a` approaches `sqrt(3)/2`.
Its loaded edge direction `theta` therefore varies over a nonzero angular
interval while the unloaded chart is held fixed.

For arbitrarily large `D`, put a circle of radius `D/2` through `P,Q` with
center below the top side, and add their antipodes. The three chart vertices
are strictly inside that circle for large `D`, so `P,Q` are actual source
diameter endpoints. The resulting seven-point source is still triangle-free
and unit-separated. The verifier uses exact rational `cos(theta),sin(theta)`
and exact algebraic coordinates, with angle excess `O(1/D)` in the unloaded
chart.

As above this is a local source regression, not a canonical global minimizer.
It shows precisely why the two-loaded-edge pentagon theorem does not control
the one-loaded-edge face: there is no middle loaded turn to couple its top
edge to the unloaded direction. A source-specific equilibrium or simultaneous
competitor theorem is required here.

## 8. Canonical implication chain and unresolved limits

The new exact chain is

`actual loaded-face directions -> CD.11 -> d_H+s_Z and u_B-z_B -> core ledger`.

Its proved contradiction is limited to a hypothetical source family satisfying
both direction concentration and `liminf (d_H+s_Z)/D>0` (or a positive
`(u_B-z_B)/D` floor). Neither positive floor is a general canonical premise.
The full-core high-surplus branch with small `k`, the one-loaded-edge pentagon
collar, nonconcentrated boundary phases, split-star O--O, inactive interfaces,
and macroscopic inactive containers/exterior caps survive. No exact triangle
or same-cardinality strict sub-D competitor for every branch is constructed.

The next concrete source obligation is to prove, or refute using full positive
source equilibrium, that the one-loaded-edge pentagons in Section 7 cannot
supply a linear changing-direction collar around one near-triangular harmonic
component. The local geometry is feasible; the missing information is its
simultaneous positive-contact continuation and every inactive source guard.

## 9. Computation, regressions, and claim classification

`research/verify_loaded_collar_face_payment_2026_10_02.py` uses exact rational
arithmetic and rational enclosures of square roots. It verifies every source
pair in CD.13, the actual antipodal diameters, strict inactive diagonals, failed
private reflection, and successful eight-point companion move. It also checks
the CD.15 seven-point regressions and the finite projection/face-count algebra.
Analytic turning, near-disk, pocket topology, and saturation arguments are
proved above; finite computation is not their proof.

The scripts encode **no global optimality**, canonical KKT/PSD/ZR/ZF,
quadratic source population, or full-core rhombic saturation. Stars, paths,
contact isolates, repeated outer-walk occurrences and bridges remain explicitly
accounted for in the analytic statements. No weak multiplier is integrated by
assumption. No scaffold is identified with a source chart.

| Claim | Classification | Exact limit |
| --- | --- | --- |
| CD.1 angular capacity | proved candidate awaiting promotion | finite convex geometry |
| CD.5 exceptional-face payment | proved candidate awaiting promotion | canonical full-core, eventual threshold |
| CD.6 bridge payment | proved candidate awaiting promotion | canonical full-core and loaded-chord theorem |
| CD.7/CD.11 deficiency gate | proved candidate awaiting promotion | actual source collar direction set |
| CD.12 | conditional | stated angular concentration hypothesis |
| CD.13--CD.15 | regression | actual finite source geometry; no global optimality |
| Eight-point companion motion | proved candidate / regression check | all eight-source guards certified; not arbitrary-source feasibility |
| All collar directions inherit one chart | rejected local candidate | CD.15 gives free one-edge pentagon directions |
| Level I or C-II closure | not obtained | surviving global branches named above |

No new literature import. Promotion recommendation: **unreviewed**; preserve
this packet and audit the pocket counting and large-face exclusion before any
state change. The canonical manifest, route map and active prompt are unchanged.

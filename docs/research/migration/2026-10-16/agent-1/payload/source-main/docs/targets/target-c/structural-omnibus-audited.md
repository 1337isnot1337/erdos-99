# Target C — audited structural omnibus, normalized §§142–146

**Date:** 2026-09-12  
**Lifecycle:** audited-working route module; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This module preserves the positive theorem content of the former omnibus PR #350 in a
single normalized route-local source. Two repairs are binding throughout:

1. the stopped-train auxiliary graph uses the corrected monotone-height orientation
   argument below; and
2. the interval-biclique theorem includes the required ordered-shore size hypothesis
   `1<=k<=b`.

The even-hole, oblique-lattice, and protected-contact-creation files from the old branch
were regression tests, not positive theorems, and are not promoted here.

The section numbers below are research-tail labels only. Canonical theorem-state
authority remains audit.46 through canonical Section 123.

---

# §142 — all-defect stopped-train / phase gap

Work in the nonisolated positive-contact core. Write

- `v,e` for its vertex/contact counts;
- `R` for bounded strict-rhombus faces;
- `f` for bounded nonquadrilateral faces;
- `b` for outer-face walk length with multiplicity;
- `Q=sum_F(deg F-4)` over bounded nonquadrilateral faces;
- `q` for loaded force-hull vertices;
- `h` for active diameter edges;
- `d_H=q-h`;
- `s_Z=e+h-(2v-2)>=0`;
- `k=d_H+s_Z`.

## 142.1 Exact stopped-train ledger

Construct an auxiliary graph `Xi` whose vertices are the positive contact edges. For
every strict rhombus, connect each pair of opposite contact edges. Thus each rhombus
adds two auxiliary links.

Every component of `Xi` has one projective contact direction. Fix an orientation `u`
of that direction and define

\[
h(e):=Ju\cdot m(e)
\]

for the midpoint `m(e)` of a contact edge. Opposite `u`-parallel sides of one strict
triangle-free unit rhombus have distinct `h` values. Orient the corresponding auxiliary
link from lower to higher `h`.

At a degree-two auxiliary vertex, the two incident strict rhombi occupy opposite local
sides of the physical contact edge. Hence one opposite edge has higher `h` and the
other lower `h`; exactly one auxiliary link enters and one leaves. An auxiliary cycle
would therefore become a consistently directed cycle along which `h` strictly
increases, impossible.

Thus every auxiliary component is a path; a contact edge incident to no strict rhombus
is a singleton path. Let `T` be the number of these complete stopped trains. Since
`Xi` is a forest with `e` vertices and `2R` links,

\[
\boxed{T=e-2R.}
\tag{142.1}
\]

Occurrence-counted face incidence gives

\[
2e=4R+b+4f+Q,
\]

so

\[
\boxed{T={b+Q\over2}+2f.}
\tag{142.2}
\]

Canonical core-only ZR/ZF gives

\[
b+Q=2(h-s_Z).
\]

Therefore

\[
\boxed{T=h-s_Z+2f}
\tag{142.3}
\]

and, since `d_H=q-h`,

\[
\boxed{T-q=2f-k.}
\tag{142.4}
\]

No contact-isolated source coordinate appears in this ledger.

## 142.2 The train-crossing graph is simple and triangle-free

Two trains crossing in a strict rhombus have projective contact-direction separation
in `(pi/3,pi/2]`. A train midpoint segment is parallel to the other side direction of
the rhombus and, under the `h` orientation, lies in a cone of half-width strictly below
`pi/6` about the train normal.

For two crossing trains, their normal directions are separated by more than `pi/3`.
Their tangent cones are therefore disjoint. With respect to the bisector coordinate,
both midpoint paths are monotone and their slope intervals are strictly ordered, so
their height difference is strictly monotone. Hence two complete trains cross at most
once.

If three trains crossed pairwise, their three projective contact directions on the
circle of circumference `pi` would have all pairwise circular separations strictly
larger than `pi/3`, impossible. Thus the train-crossing graph is simple and
triangle-free, with exactly `R` edges.

## 142.3 Phase atoms carry the quadratic crossing density

In Type II,

\[
{R\over D^2}\to
\Delta_2:={\pi\over2\sqrt3},
\]

and the total strict-rhombus area excess above `sqrt(3)/2` is `o(D^2)`. Also `T=Theta(D)`:
Mantel gives `R<=T^2/4`, while (142.2), `f<=Q`, the core ledger, and `q=O(D)` give
`T=O(D)`.

Let `mu_D` be the empirical projective train-phase measure and pass to a subsequence
with

\[
{T\over D}\to x,
\qquad
{q\over T}\to y,
\qquad
\mu_D\Rightarrow\mu.
\]

Let `s` be the total atomic mass of `mu`.

Area saturation implies that, for every fixed `epsilon>0`, only `o(T^2)` crossings
have phase separation at least `pi/3+epsilon`. Thus any normalized crossing-measure
limit is supported on

\[
\{(phi,psi):psi-phi\equiv\pm\pi/3\pmod\pi\}.
\]

Because the finite crossing graphs are simple, the normalized crossing measure is
bounded by the product phase measure. The product measure charges the exact
`+-pi/3` relation only through atoms. Applying weighted Mantel to finitely many heavy
atoms and then exhausting the atomic mass gives

\[
\boxed{
{\Delta_2\over x^2}\le{s^2\over4},
\qquad
2\sqrt{\Delta_2}\le xs.
}
\tag{142.5}
\]

## 142.4 Exposed hull forces non-atomic train mass

Use the distinguished exterior occurrence of each loaded force-hull vertex. These `q`
occurrences split the occurrence-counted outer contact walk into `q` walks joining
consecutive loaded hull vertices. Their total length is `b<=2T`; every displacement
has norm at least one.

Fix `M`. At most `2T/(M+1)` of these outer intervals contain more than `M` unit-edge
occurrences.

Choose finitely many phase atoms carrying mass at least `s-epsilon`, and disjoint
`delta`-neighborhoods of their projective directions. A short outer interval using
only those neighborhoods has displacement within `O_M(delta)` of one of finitely many
signed sums of the atomic unit directions. Zero limiting sums cannot realize a hull
side of norm at least one. Hence the corresponding hull-side directions/normals lie in
finitely many arcs of total angular measure `O_M(delta)`.

Type-II force-hull convergence to the disk implies convergence of normalized perimeter
measure to the nonatomic uniform circular measure. Since every hull side has length at
least one, only

\[
O_M(\delta D)+o_\delta(D)
\]

such atom-only short hull intervals exist.

Every remaining short interval contains an outer occurrence of a train outside the
selected atomic neighborhoods. The outer intervals partition outer-walk occurrences,
and each complete stopped train has at most two outer occurrences; hence these
remaining intervals number at most

\[
2(1-s+epsilon+o(1))T.
\]

Send the source size to infinity, then `delta->0`, `M->infinity`, and
`epsilon->0`. This yields

\[
\boxed{y\le2(1-s).}
\tag{142.6}
\]

Combining (142.5) and (142.6),

\[
2\sqrt{\Delta_2}
\le x(1-y/2)
={T-q/2\over D}+o(1).
\tag{142.7}
\]

Since the convex loaded hull has `q` sides of length at least one and diameter at most
`D`,

\[
q\le\operatorname{per}(F)\le\pi D.
\]

Therefore

\[
\boxed{
\liminf {T-q\over D}
\ge
2\sqrt{\Delta_2}-{\pi\over2}
=:\gamma
=0.333829286933018\ldots .
}
\tag{142.8}
\]

Using (142.4),

\[
\boxed{
\liminf {2f-k\over D}\ge\gamma.
}
\tag{142.9}
\]

This is an all-defect theorem; exceptional faces and singleton trains are retained.

---

# §143 — linear bounded-degree defect-face transport network

For fixed integer `K>=5`, let

\[
f_{\le K}:=\#\{F:5\le\deg F\le K\},
\qquad
f_{>K}:=f-f_{\le K}.
\]

Canonical Section 63 gives

\[
q-x_B=Q+2k,
\qquad x_B\ge0,
\]

and `q<=pi D`, so

\[
\boxed{Q\le\pi D-2k.}
\tag{143.1}
\]

Every face counted by `f_{>K}` contributes at least `K-3` to `Q`, hence

\[
f_{>K}\le{Q\over K-3}.
\]

Combining with (142.9) gives

\[
\boxed{
\liminf {f_{\le K}\over D}
\ge {\gamma\over2}-{\pi\over K-3}.
}
\tag{143.2}
\]

The smallest integer `K` with positive right side is `K=22`, giving

\[
\boxed{
\liminf {f_{\le22}\over D}
\ge0.001567661698625\ldots .
}
\tag{143.3}
\]

## 143.1 Exact endpoint multigraph

Let `O` denote the outer face. Build a multigraph whose vertices are `O` and all
bounded nonquadrilateral faces. Every non-singleton stopped train joins the two plane
faces on the terminal sides of its two terminal contact edges. A singleton stopped
train uses the two face-side occurrences of its lone contact edge; a bridge may have
two occurrences of the same face.

Every outer or bounded-nonquadrilateral contact-edge occurrence is one stopped-train
endpoint occurrence. Hence

\[
\boxed{\deg(O)=b,}
\qquad
\boxed{\deg(F)=\deg_G(F)}
\tag{143.4}
\]

and the handshake identity is exactly

\[
2|E|=b+4f+Q=2T.
\tag{143.5}
\]

A bounded vertex cannot support a loop. For a nontrivial train, close the midpoint path
through the common bounded face; for a singleton bridge, close a small transverse
segment through the contact edge inside that face. The resulting Jordan curve lies in
the force hull, and its bounded shore contains no loaded extreme vertex, hence no
crossing active diameter edge. The contact cut has one common nonzero direction and
strictly positive relative-interior KKT weights. Summed equilibrium would force this
nonzero contact resultant to vanish, contradiction.

Thus every loop is based at the outer-face vertex. In particular, Type II contains a
linear family of bounded loop-free transport vertices of degree at most 22.

---

# §144 — corrected interval-neighborhood biclique theorem

Let `G=(A,B,E)` be bipartite, with

\[
|A|=a,
\qquad |B|=b,
\]

and fix a linear order on `B`. Assume every `A`-row neighborhood is an interval in
that order.

For

\[
\boxed{1\le k\le b,}
\tag{144.1}
\]

if

\[
\boxed{
e+a\ge k(a+b-k+1),
}
\tag{144.2}
\]

then `G` contains a `K_{k,k}` whose `B` shore is one consecutive `k`-block.

Indeed, a row interval of degree `d_x` contains

\[
\max(d_x-k+1,0)
\]

consecutive `k`-blocks, so the row/block incidence count satisfies

\[
I_k\ge e-a(k-1)
\ge k(b-k+1).
\]

There are `b-k+1` consecutive `k`-blocks. If each lay in at most `k-1` row
neighborhoods, then

\[
I_k\le(k-1)(b-k+1),
\]

contradiction.

The missing size hypothesis in the historical statement is essential. For example
`a=b=e=1,k=2` satisfies the raw numerical equality but there is no consecutive
2-block.

The useful floor corollary survives without extra conditions. Put

\[
k_0:=\left\lfloor{e\over a+b}\right\rfloor.
\]

If `k_0>=1`, then

\[
k_0\le{e\over a+b}\le{ab\over a+b}<\min(a,b),
\]

so (144.1) is automatic and a `K_{k_0,k_0}` exists.

If

\[
a,b\le CD,
\qquad e\ge\varepsilon D^2,
\]

then every fixed

\[
c<C-\sqrt{C^2-\varepsilon}
\]

gives a `K_{\lfloor cD\rfloor,\lfloor cD\rfloor}` for all sufficiently large
`D`. Thus the extraction is linear, not quadratic, in crossing density.

---

# §145 — direct ordered-grid extraction from one full phase-label pair

Work in one Type-II harmonic carrier with

\[
R_D\ge rD^2,
\qquad
T_D\le C_0D
\]

for fixed `r,C_0>0`. After the canonical phase-circle cut, at least
`(3r/4)D^2` crossings remain and all reduced phases lie in one open interval of width

\[
L={\pi\over3}.
\]

One of the three unordered phase-label pairs therefore supports at least

\[
\boxed{E\ge\eta D^2,
\qquad \eta:=r/4.}
\tag{145.1}
\]

Fix such a pair, with lifted labels differing by one. Write the physical edge
arguments as

\[
\alpha_a=x_a+L\ell_A,
\qquad
\beta_b=x_b+L(\ell_A+1).
\]

At every actual crossing, the oriented phase law gives `x_b-x_a>0`.

Let `x_-` and `x_+` be the extreme reduced phases in the two selected families.
Because the train set is finite and the reduced phases lie in one open interval of
width `L`,

\[
x_+-x_-<L.
\]

Canonical train orientation puts elementary centerline displacements of the first
shore in

\[
(x_-+L\ell_A+L,\ x_++L\ell_A+2L)
\]

and those of the second shore in

\[
(x_-+L\ell_A+2L,\ x_++L\ell_A+3L).
\]

The union has angular width

\[
(x_+-x_-)+2L<3L=\pi.
\]

Therefore one linear coordinate is strictly increasing along every selected train.
Same-label trains are pairwise disjoint. At every cross-label rhombus the local forward
displacements are `v_b` and `-u_a`, with

\[
\det(v_b,-u_a)=\det(u_a,v_b)>0,
\]

so every crossing has one common sign.

## 145.1 Endpoint-balanced slab extraction

Let

\[
N:=|A|+|B|\le C_0D.
\]

Partition the common monotone coordinate into `M` slabs with endpoint counts balanced
so each slab contains at most `2N/M+2` train endpoints. A crossing is bad if both of
its trains have an endpoint in its crossing slab. Summing the per-slab product bound
gives

\[
\#\text{bad}
\le{N^2\over M}+N.
\tag{145.2}
\]

Choose

\[
M_0:=\left\lfloor{2C_0^2\over\eta}\right\rfloor+1
=\left\lfloor{8C_0^2\over r}\right\rfloor+1.
\tag{145.3}
\]

For large `D`, quadratic many nonbad crossings remain. At every nonbad crossing at
least one of the two monotone trains has no endpoint in the crossing slab and therefore
spans the slab. Assign each nonbad crossing to one spanning shore, then pigeonhole the
shore type and slab. One obtains a slab with a pairwise-disjoint spanning shore and

\[
E_S\ge\left({\eta\over4M_0}-o(1)\right)D^2
\tag{145.4}
\]

incident crossings.

Common monotonicity and common crossing sign make every neighborhood on the opposite
shore an interval in the vertical order of the spanning shore. Applying §144 gives a
balanced complete ordered grid with

\[
\boxed{|A_0|,|B_0|\ge cD}
\tag{145.5}
\]

for every fixed

\[
\boxed{
0<c<c_{\rm dir}:={r\over16C_0M_0}.
}
\tag{145.6}
\]

This removes an avoidable phase-threshold density-squaring loss from the older ordered
grid route. It does not close C-II: oblique-lattice regressions realize the same
qualitative large-grid structure without global minimality.

---

# §146 — Type-II phase/perimeter diameter-edge density floor

Retain the Type-II notation

\[
\Delta_2={\pi\over2\sqrt3}.
\]

From §142 we have the stronger pre-elimination form

\[
\boxed{
\liminf {T-q/2\over D}\ge2\sqrt{\Delta_2}.
}
\tag{146.1}
\]

Pass to a normalized subsequence with

\[
{h\over D}\to y,
\qquad
{d_H\over D}\to d,
\qquad
{s_Z\over D}\to s.
\]

Using

\[
T=q+2f-k,
\qquad q=h+d_H,
\qquad k=d_H+s_Z,
\]

in (146.1) gives

\[
\boxed{
\liminf{f\over D}
\ge
\sqrt{\Delta_2}-{y\over4}+{d\over4}+{s\over2}.
}
\tag{146.2}
\]

The exact outer-walk ledger is

\[
b=2h-Q-2s_Z.
\tag{146.3}
\]

Type-II force-hull convergence gives

\[
{\operatorname{per}(F)\over D}\to\pi,
\]

while `per(F)<=b`. Therefore

\[
\limsup{Q\over D}+2s\le2y-\pi.
\tag{146.4}
\]

Since `Q>=f`, combine (146.2) and (146.4):

\[
{9y\over4}
\ge
\pi+\sqrt{\Delta_2}+{d\over4}+{5s\over2}.
\]

Hence

\[
\boxed{
\liminf {1\over D}
\left(
 h-{d_H\over9}-{10s_Z\over9}
\right)
\ge
{4\over9}
\left(
\pi+\sqrt{\frac\pi{2\sqrt3}}
\right).
}
\tag{146.5}
\]

In particular,

\[
\boxed{
\liminf {h\over D}
\ge
{4\over9}
\left(
\pi+\sqrt{\frac\pi{2\sqrt3}}
\right)
=1.8195135379794445\ldots .
}
\tag{146.6}
\]

This is a diameter-edge-density theorem, not the separately rejected unconditional
`(q-k)/D>=1.9046...` claim. The defect coefficients in (146.5) are retained and all
inequality directions have been rechecked.

---

# Regression boundaries and final audit disposition

Three negative tests from the historical omnibus remain binding conceptually.

1. **Even-hole zero-phase regression.** A bounded defect face need not itself supply
   positive phase transport merely because it is nonquadrilateral.
2. **Oblique-lattice regression.** Large coherent ordered grids do not by themselves
   force a strict global diameter improvement.
3. **Protected-contact-creation regression.** Moving an isolated point to first contact
   does not automatically make the new contact force-positive in a reoptimized KKT
   stress.

These block stronger extrapolations but do not invalidate §§142–146.

The positive results above were independently recomputed after the two binding repairs.
No full-source Section-57 affine-kernel extension is used, contact-isolated source
points are retained, and none of the results closes the macroscopic inactive-container
branch.

**Overall verdict:** PASS at audited-working scope. Theorem-state authority is
unchanged; C-II and Level I remain open.
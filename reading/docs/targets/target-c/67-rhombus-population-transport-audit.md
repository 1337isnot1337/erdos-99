> Generated reading edition · [exact source](../../../../docs/targets/target-c/67-rhombus-population-transport-audit.md) · source SHA-256 `fc60bd6982e741f13d2442a2fa9d16a424f2fc55f60c3e1a1d7f3aba2cc3686f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — rhombus/population transport audit

This module independently re-proves the valid all-topology source-capacity cancellation
behind the old general rhombus-excess report. It repairs one implicit point in that
report by proving that a bounded unit-rhombus face cannot contain an additional source
point. It does not use the rejected cyclic Reuleaux-cap detour, does not delete
contact-isolated source points, and does not assume `s_Z=0` or one Woodall branch.

**LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.**

---

# 67. The complete post-ZF topology defect cancels from the force-hull population budget

Work with the canonical contact-minimal, then diameter-pair-minimal post-ZF C-II
representative and its relative-interior full-support KKT stress. Let

- `G` be the connected positive unit-contact core;
- `m=|V(G)|` and `e=|E(G)|`;
- `F=conv V(G)` be the full actual force hull;
- `B` be the loaded diameter-endpoint set, with `q=|B|`;
- `h` be the number of actual diameter edges;
- `d_H=q-h`;
- `s_Z=e+h-(2m-2)>=0`;
- `k=d_H+s_Z`;
- `b` be the outer contact-face boundary-walk length, with multiplicity;
- `R_4` be the number of bounded quadrilateral contact faces;
- `f` be the number of bounded nonquadrilateral contact faces; and
- `Q=sum_P(deg P-4)` over those nonquadrilateral bounded faces.

Put

```math
a_0={\sqrt3\over2},
\qquad
c_0={\sqrt3\over4}={a_0\over2}.
\tag{67.1}
```

For every bounded quadrilateral face `R`, define its strict-rhombus area excess

```math
\epsilon_R:=\operatorname{area}(R)-a_0\ge0,
```

and put

```math
\boxed{E_4:=\sum_R\epsilon_R\ge0.}
\tag{67.2}
```

Let `N_F` be the number of **all source points** lying in `F`, including every
contact-isolated point there. Let

```math
Z_{ext}:=n-N_F
```

be the number of source points outside the force hull, and define the isodiametric
force-hull deficit

```math
\delta_F:={\pi D^2\over4}-\operatorname{area}(F)\ge0.
\tag{67.3}
```

The main finite population inequality is

```math
\boxed{
a_0N_F
\le
\operatorname{area}(F)
+c_0\operatorname{per}(F)
+a_0-E_4.
}
\tag{67.4}
```

Combining it with the canonical strict translated-lattice comparison

```math
a_0(n-1)>{\pi D^2\over4}
\tag{67.5}
```

gives

```math
\boxed{
E_4+\delta_F
<
a_0Z_{ext}+c_0\operatorname{per}(F)
\le
a_0Z_{ext}+{\pi\sqrt3\over4}D.
}
\tag{67.6}
```

Thus the complete post-ZF defect `d_H+s_Z` cancels exactly. The only quadratic-scale
population escape left by this theorem is source population outside `F`.

In particular,

```math
Z_{ext}=o(D^2)
\Longrightarrow
\delta_F=o(D^2),
\quad
E_4=o(D^2),
\tag{67.7}
```

and

```math
Z_{ext}=O(D)
\Longrightarrow
\delta_F+E_4=O(D).
\tag{67.8}
```

No annular subtraction of Oler inequalities is used.

## 67.1 Exact post-ZF face count

Euler and face incidence for the connected plane contact graph give

```math
2m=2R_4+2f+b+Q+2.
\tag{67.9}
```

Section 57's exact post-ZF ledger is

```math
\boxed{b+Q=2(h-s_Z).}
\tag{67.10}
```

Since `h=q-d_H`,

```math
b+Q=2(q-k).
\tag{67.11}
```

Insert this in (67.9):

```math
\boxed{m=R_4+f+q-k+1.}
\tag{67.12}
```

This identity is valid in both Woodall branches and for arbitrary `s_Z>=0`.

## 67.2 Every component behind one removed contact-core vertex still sees load

We need one articulation fact to control the outer contact face. It follows directly
from positive equilibrium and does not require a contraction argument.

### Lemma 67.1

For every `x in V(G)`, every connected component of `G-x` contains at least one loaded
vertex from `B`.

### Proof

Suppose a component `S` of `G-x` contains no loaded vertex. Every vertex of `S` is
therefore unloaded, so each Euclidean coordinate is positive-weight harmonic there:

```math
p_y={\sum_{yz\in E(G)}\alpha_{yz}p_z\over
           \sum_{yz\in E(G)}\alpha_{yz}}
\qquad(y\in S).
\tag{67.13}
```

Any neighbor of `S` outside `S` must be `x`, because `S` is a component of `G-x`.
Since `G` is connected, there is at least one such boundary edge. The discrete maximum
principle with sole boundary value `p_x` forces both coordinate functions to be
constant on `S` with value `p_x`. Hence every vertex of `S` coincides with `x`,
contradicting distinct source points. `square`

This is the same harmonic repair used in the audited Section 60 loaded-component proof.

## 67.3 Hull augmentation and convex pockets

Every unloaded positive-contact vertex is a positive weighted average of its contact
neighbors. Iterating the coordinate maximum principle shows

```math
F=\operatorname{conv}V(G)=\operatorname{conv}B.
\tag{67.14}
```

We also need the stronger boundary statement

```math
\boxed{V(G)\cap\partial F=B.}
```

Indeed, the canonical local-structure theorem gives contact degree at least three for
every unloaded positive-contact core vertex. Suppose such a vertex `x` lay on
`partial F`, and choose a supporting line of `F` through `x`. All contact neighbors of
`x` lie in the corresponding closed half-plane. Positive contact equilibrium at an
unloaded vertex says that a strictly positive combination of the contact vectors
vanishes. This is possible in one closed half-plane only if every contact vector lies
on the supporting line. Since every contact has length one, there is at most one
neighbor in each of the two line directions, so `deg_G(x)<=2`, contradiction.
Therefore every core vertex on `partial F` is loaded.

In particular, the open segment between two consecutive vertices of `B=Vert(F)`
contains no vertex of `G`. Add every missing straight hull side between consecutive
vertices of `B` to `G`, retaining a side only once when it is already a unit contact.
Call the resulting plane graph `Ghat`. Each added side is therefore a legitimate new
plane-graph edge with no intermediate graph vertex. It lies on `partial F`, so it does
not properly cross any edge of `G`.

### Lemma 67.2

`Ghat` is 2-connected.

### Proof

Fix a core vertex `x`. Every component of `G-x` contains, by Lemma 67.1, a loaded
vertex different from `x`. If `x` is not loaded, the full added hull cycle survives in
`Ghat-x`. If `x` is loaded, deleting `x` leaves the hull cycle as one path through all
other loaded vertices. Thus the loaded representative of every component of `G-x` is
connected to every other such representative in `Ghat-x`; hence `Ghat-x` is connected.
`square`

Every face boundary of `Ghat` is therefore a simple cycle.

### Lemma 67.3

Every bounded face of `Ghat` is a convex polygon.

### Proof

At a loaded hull vertex, every bounded-face sector is contained in the convex tangent
cone of `F`, so its angle is less than `pi`.

At an unloaded core vertex `x`, suppose a bounded-face angle were greater than `pi`.
All positive contact directions at `x` would lie in the complementary open cone of
width less than `pi`, so their strictly positive weighted sum could not vanish. This
contradicts contact equilibrium. Thus every bounded-face angle is at most `pi`.

A simple polygon all of whose interior angles are at most `pi` is convex. `square`

Strict convexity is unnecessary below; ordinary convexity is enough for Oler.

The old bounded contact faces remain faces of `Ghat`; the new bounded faces are exactly
the convex pockets cut from the old outer contact face by the hull cycle.

## 67.4 A unit-rhombus face contains no extra source point

This point was implicit in the old report and is made explicit here.

A bounded quadrilateral contact face is, by Lemma 67.3, a convex equilateral
quadrilateral, hence a unit rhombus. Let its diagonal lengths be `d_1,d_2`. Unit
separation gives

```math
d_1,d_2\ge1,
\qquad
d_1^2+d_2^2=4.
\tag{67.15}
```

Therefore

```math
\operatorname{area}(R)={d_1d_2\over2}\ge{\sqrt3\over2}=a_0.
\tag{67.16}
```

Equality would force one diagonal to have length one and hence create a unit
equilateral triangle with two sides of the rhombus, so the triangle-free source in
fact has strict inequality. Nonnegativity is all that is needed for `E_4`.

More importantly, choose the shorter diagonal `d<=sqrt(2)` and split the rhombus into
two congruent triangles with side lengths `1,1,d`. Their apex angle is at most
`pi/2`, and their circumradius is

```math
{1\over2\cos(\theta/2)}\le{1\over\sqrt2}<1.
\tag{67.17}
```

The three vertex-centered open unit disks cover the interior of each such triangle
(the farthest point from the nearest triangle vertex is no farther than the
circumcenter radius). Hence every interior point of the rhombus is at distance `<1`
from at least one rhombus vertex. Unit separation therefore forbids any additional
source point in a bounded quadrilateral face.

Thus all source points lying inside bounded contact faces but outside `V(G)` occur in
bounded nonquadrilateral faces.

## 67.5 Oler absorption inside exceptional bounded faces

Let the bounded nonquadrilateral faces be `P_i`. Write

```math
r_i:=\deg(P_i)-4\ge1,
\qquad
\sum_i r_i=Q,
\tag{67.18}
```

and let `z_i` be the number of contact-isolated source points in the interior of
`P_i`. The face is a convex unit-edge polygon by Lemma 67.3. Apply Oler to its
`4+r_i` boundary vertices together with its `z_i` interior source points:

```math
a_0(4+r_i+z_i-1)
\le
\operatorname{area}(P_i)+c_0(4+r_i).
```

Since `a_0=2c_0`,

```math
\boxed{
\operatorname{area}(P_i)
\ge a_0(z_i+1)+c_0r_i.
}
\tag{67.19}
```

Put

```math
Z_{def}:=\sum_i z_i,
\qquad
A_{exc}:=\sum_i\operatorname{area}(P_i).
```

Summing (67.19) gives

```math
\boxed{A_{exc}\ge a_0(Z_{def}+f)+c_0Q.}
\tag{67.20}
```

For the quadrilateral faces, by definition of `E_4`,

```math
A_4=a_0R_4+E_4.
\tag{67.21}
```

Let `A_bnd=A_4+A_exc`. Using (67.12), (67.20), and (67.21),

```math
\begin{aligned}
a_0(m+Z_{def})
&=a_0R_4+a_0(f+Z_{def})+a_0(q-k)+a_0\\
&\le A_bnd-E_4-c_0Q+a_0(q-k)+a_0.
\end{aligned}
\tag{67.22}
```

## 67.6 Oler absorption of inactive points in the outer face but inside `F`

Let `Z_in` be the contact-isolated source points that lie in `F` and in the old outer
face of `G`. Let

```math
H_{out}:=\operatorname{area}(F)-A_{bnd}.
\tag{67.23}
```

Let `a` be the number of hull sides added in forming `Ghat`, let `L_add` be their total
Euclidean length, and let the `a` new convex pockets be `P` with graph-boundary edge
count `k_P` and Euclidean perimeter `L_P`.

The number of new pockets is exactly `a` by Euler. Face-incidence subtraction between
`Ghat` and `G` gives

```math
\sum_P k_P=b+2a-q.
\tag{67.24}
```

Euclidean perimeter incidence gives

```math
\sum_P L_P=b+2L_{add}-\operatorname{per}(F),
\tag{67.25}
```

while

```math
\operatorname{per}(F)=q-a+L_{add},
\tag{67.26}
```

and the new pockets tile the part of the old outer face inside `F`, so

```math
\sum_P\operatorname{area}(P)=H_{out}.
\tag{67.27}
```

Assign each isolated source point in `Z_in` to a containing new pocket. If a point lies
on an added hull side, assign it to the unique interior pocket adjacent to that side.
No isolated source point lies on an old unit contact edge, since the interior of a unit
segment is at distance `<1` from an endpoint.

Let `z_P` be the assigned population. Oler on the convex pocket gives

```math
z_P
\le {1\over a_0}\operatorname{area}(P)
+{1\over2}L_P+1-k_P.
\tag{67.28}
```

Sum (67.28) and use (67.24)–(67.27):

```math
\boxed{
Z_{in}
\le {1\over a_0}H_{out}
+{\operatorname{per}(F)-b\over2}.
}
\tag{67.29}
```

The correction is nonpositive. Indeed the outer contact-face boundary is a closed
polygonal walk of length exactly `b`, its image lies in `F`, and it contains every
extreme vertex of `F`. Hence its convex hull is `F`. For any closed rectifiable
polygonal walk, projection variation plus Cauchy's width formula gives

```math
\operatorname{per}(\operatorname{conv}\gamma)
\le\operatorname{length}(\gamma).
```

Therefore

```math
\boxed{\operatorname{per}(F)\le b.}
\tag{67.30}
```

We retain the sharper signed correction (67.29), because it cancels the outer-walk
term exactly in the next step.

Multiplying (67.29) by `a_0` gives

```math
\boxed{
a_0Z_{in}
\le H_{out}+c_0(\operatorname{per}(F)-b).
}
\tag{67.31}
```

## 67.7 Exact topology cancellation and full inside-hull population bound

Because the chosen relative-interior KKT stress is strictly positive on every actual
contact and diameter row, the full-support core contains every source point incident
to any actual contact or diameter equality. Hence every source point outside `V(G)`
is fully inactive, in particular contact-isolated. Every source point in `F` is
therefore either a core vertex, an inactive point in an exceptional bounded face, or
an inactive point in the old outer face. Section 67.4 excludes a fourth possibility
inside a quadrilateral face. Thus

```math
N_F=m+Z_{def}+Z_{in}.
\tag{67.32}
```

Add (67.31) to (67.22), and use

```math
A_{bnd}+H_{out}=\operatorname{area}(F).
```

Then

```math
\begin{aligned}
a_0N_F
&\le
\operatorname{area}(F)-E_4-c_0Q+a_0(q-k)+a_0
+c_0(\operatorname{per}(F)-b)\\
&=
\operatorname{area}(F)+c_0\operatorname{per}(F)+a_0-E_4\\
&\qquad{}+
\bigl[-c_0(Q+b)+a_0(q-k)\bigr].
\end{aligned}
\tag{67.33}
```

But (67.11) says `Q+b=2(q-k)`, and `a_0=2c_0`. Therefore the bracket vanishes
**exactly**, proving (67.4):

```math
\boxed{
a_0N_F
\le
\operatorname{area}(F)+c_0\operatorname{per}(F)+a_0-E_4.
}
```

This is why neither `d_H` nor `s_Z` survives in the final population inequality.

## 67.8 External population versus force-hull and rhombus defects

Write

```math
n=N_F+Z_{ext}.
```

From (67.4),

```math
a_0(n-1)
\le
\operatorname{area}(F)+c_0\operatorname{per}(F)-E_4+a_0Z_{ext}.
\tag{67.34}
```

The canonical full-source translated-lattice comparison is strict:

```math
a_0(n-1)>{\pi D^2\over4}.
```

Therefore

```math
{\pi D^2\over4}
<
\operatorname{area}(F)+c_0\operatorname{per}(F)-E_4+a_0Z_{ext}.
```

Rearrange:

```math
\boxed{E_4+\delta_F<a_0Z_{ext}+c_0\operatorname{per}(F).}
```

The isodiametric perimeter bound `per(F)<=pi D` gives the second inequality in (67.6).

Since both `E_4` and `delta_F` are nonnegative, (67.7) and (67.8) follow immediately.

## 67.9 External population floor and the primitive-boundary endpoint

The same inside-hull inequality also recovers, and slightly sharpens in provenance, the
external-rattler phase split without importing a separate report.

From (67.4), discard the nonnegative `E_4` term. The post-ZF face ledger gives

```math
\operatorname{per}(F)\le b\le b+Q=2(h-s_Z)\le2h.
\tag{67.35}
```

Isoperimetry therefore gives

```math
\operatorname{area}(F)
\le {\operatorname{per}(F)^2\over4\pi}
\le {h^2\over\pi}.
\tag{67.36}
```

Using `c_0=a_0/2` in (67.4),

```math
\boxed{
N_F
\le {2h^2\over\pi\sqrt3}+h+1.
}
\tag{67.37}
```

Since `Z_ext=n-N_F`, this yields the exact finite external-population floor

```math
\boxed{
Z_{ext}
\ge n-{2h^2\over\pi\sqrt3}-h-1.
}
\tag{67.38}
```

The strict translated-lattice comparison used in Section 67.8 says

```math
n-1>{\pi D^2\over2\sqrt3}.
\tag{67.39}
```

Hence along any subsequence with `h/D->y`,

```math
\boxed{
\liminf {Z_{ext}\over D^2}
\ge {\pi\over2\sqrt3}-{2y^2\over\pi\sqrt3}.
}
\tag{67.40}
```

The right side is positive exactly for `y<pi/2`.

This interacts sharply with canonical Section 65. Its proof gives, for
`M=max{e_BB,x_B}` and `h/D->y`,

```math
\liminf {M\over D}
\ge \phi(y):={y+2\cos(y/2)\over3},
\qquad y\ge2\rho,
\tag{67.41}
```

where `rho=cos rho`. The function `phi` is strictly increasing on
`[2rho,pi)`. Therefore any sequence approaching the universal primitive-boundary
endpoint

```math
{M\over D}\to {4\rho\over3}
\tag{67.42}
```

must satisfy

```math
\boxed{{h\over D}\to2\rho.}
\tag{67.43}
```

Since `rho<pi/4`, one has `2rho<pi/2`. Equations (67.40)--(67.43) therefore force

```math
\boxed{
\liminf {Z_{ext}\over D^2}
\ge {\pi\over2\sqrt3}-{8\rho^2\over\pi\sqrt3}
>0.
}
\tag{67.44}
```

Numerically the displayed constant is about `0.1038019`.

Thus the weakest all-branch primitive-boundary endpoint is not a purely local
force-hull endpoint. It necessarily carries a quadratic population outside the full
actual force hull. Any closure near `4rho/3` must therefore use external-completion
geometry or a representative-transfer theorem, not only the positive core.

## 67.10 What this closes and what it does not

Section 67 removes `d_H` and `s_Z` themselves from the full inside-force-hull capacity
obstruction. A large forest defect or large mixed-row surplus cannot by itself pay for
population once all source points inside `F` are counted correctly.

What remains is genuinely external:

```math
\boxed{Z_{ext}=|A\setminus F|.}
```

If `Z_ext=o(D^2)`, then the full actual force hull is asymptotically isodiametric and
the normalized total strict-rhombus area excess vanishes. If `Z_ext=O(D)`, both defects
are only linear.

The theorem does **not** prove either population bound. The canonical representative
can still contain a quadratic number of fully inactive points outside `F`. Moving such
points until first contact need not make the new contacts KKT-positive, so the post-ZF
ledgers cannot simply be re-applied to a contact-richer representative.

Together with the canonical Sections 65-66 primitive-boundary floors, this identifies a sharper closing fork:

1. prove `Z_ext=o(D^2)` for the lexicographically minimal full-support representative;
2. prove a representative-transfer theorem carrying the post-ZF force/stress geometry
   to a rattler-reduced/contact-richer representative; or
3. combine the consequence `E_4=o(D^2)` from either route with Target B's audited
   rhombic-grid stability to contradict the surviving source geometry.

The third route still requires a multi-grain/globalization theorem: the current Target
B GPI theorem is conditional on a dominant coherent component and does not by itself
turn small total rhombus excess into one global lattice phase.

## 67.11 Regressions and scope

- **Dense inactive filling inside `F`:** absorbed by (67.4); it is no longer an escape.
- **Dense inactive filling outside `F`:** retained through `Z_ext`; Section 67 does not
  falsely exclude it.
- **Heptagon-plus-center type examples:** internal inactive points are counted in
  `N_F`; the inequality reduces to finite Oler capacity.
- **Woodall cyclic and forest branches:** both retained; `d_H` cancels algebraically.
- **Positive `s_Z`:** retained and cancels algebraically.
- **Bridges/articulations:** retained. The hull augmentation is 2-connected even when
  `G` is not, by Lemma 67.1.
- **Collinear face vertices:** harmless. Convexity, not strict convexity, is sufficient
  for Oler.
- **Rejected cyclic cap theorem:** not used. No claim `b-per(F)=o(D)` or
  `H_out=o(D^2)` is made.
- **Annular Oler subtraction:** not used.
- **KKT coefficient floors:** not used.

The exact remaining obstruction is a whole-source theorem controlling population
outside the full actual force hull or transporting the canonical force structure to a
representative where that external population has been eliminated.

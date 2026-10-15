# Target C — linear nonmatching-excess audit

This module independently audits the old near-matching train argument and then combines
it with the now-canonical defect-sensitive difference-body inequality. It strengthens
the exact perfect-matching exclusion to a quantitative theorem with a fixed positive
linear constant.

It does not assume `s_Z=0`, does not use a KKT weight floor, and does not discard
contact-isolated source points.

**LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.**

---

# 61. Linear diameter branching above the matching endpoint

Work with the canonical contact-minimal, then diameter-pair-minimal C-II source. Let

- `D` be its diameter;
- `q` be the number of loaded diameter vertices;
- `h` be the number of actual loaded diameter edges;
- `d_H=q-h`;
- `b` be the outer contact-face boundary-walk length, with multiplicity;
- `x_B=b-q`;
- `Q=sum_F(deg F-4)` over bounded nonquadrilateral contact faces;
- `f` be the number of those nonquadrilateral faces;
- `g_F=sum_F(deg F-5)`, so `Q=f+g_F`; and
- `s_Z=e+h-(2v-2)>=0` be the canonical post-ZF mixed-rigidity surplus.

Define the **nonmatching excess**

\[
\boxed{r_H:=2h-q.}
\tag{61.1}
\]

The main conclusions are the exact finite inequality

\[
\boxed{3r_H\ge h-2,}
\tag{61.2}
\]

and the sharper asymptotic theorem

\[
\boxed{
\liminf_{D\to\infty}{r_H\over D}\ge c_*,
\qquad
c_* = \cos\!\left({3c_*\over2}\right),
\qquad
0.6099<c_*<0.61.
}
\tag{61.3}
\]

The root `c_*` is unique in `(0,1)`; numerically it is approximately
`0.6099043189`.

In the Woodall forest branch, if the caterpillar components have vertex counts
`q_1,...,q_{d_H}`, then

\[
r_H=q-2d_H=\sum_{j=1}^{d_H}(q_j-2).
\tag{61.4}
\]

Thus every sufficiently large forest survivor has a fixed linear amount of aggregate
caterpillar excess beyond disjoint matching edges.

## 61.1 Exact defect identity

Euler plus canonical ZF gives

\[
{b+Q\over2}=h-s_Z.
\tag{61.5}
\]

Since `b=q+x_B`,

\[
q+x_B+Q=2h-2s_Z.
\]

Hence

\[
\boxed{
r_H=2h-q=x_B+Q+2s_Z
=x_B+f+g_F+2s_Z.
}
\tag{61.6}
\]

This is the exact currency identity used throughout the proof.

## 61.2 Finite stopped-rhombus trains

We re-prove the train facts needed below rather than importing the old unreviewed
campaign theorem.

Every bounded quadrilateral contact face is a simple convex unit rhombus by the
canonical face theorem. Triangle-freeness forces both diagonals to exceed one, so its
acute projective side-angle lies strictly in `(pi/3,pi/2]`.

Make the train-link graph whose vertices are contact edges. Each bounded rhombus adds
two links, joining each pair of opposite sides. Every train-link vertex has degree at
most two. Along one connected train all transverse contact edges have one fixed
projective direction. Orient that direction as `u` and orient passage through each
rhombus toward the same normal `Ju`. Every midpoint step then makes angle strictly
less than `pi/6` with `Ju`, so projection onto `Ju` increases strictly. Therefore a
train cannot close into a cycle; every train is a path, with a singleton contact edge
allowed.

If two trains cross in a rhombus, the acute projective separation `delta` of their
transverse directions is greater than `pi/3`. Orient their normals with angle `delta`.
Each train's midpoint path has all step directions in an open cone of half-angle
`pi/6` about its normal. In coordinates along the bisector of the two normals, both
paths are piecewise-linear graphs and their slope intervals are disjoint and ordered.
Their height difference is therefore strictly monotone, so two trains cross at most
once.

Three trains cannot cross pairwise: three projective directions on a circle of length
`pi` cannot have all three cyclic gaps greater than `pi/3`. Thus the train-crossing
graph is simple and triangle-free.

Let `R` be the number of bounded quadrilateral faces and `T` the number of trains,
including isolated contact-edge trains. The train-link graph has `e` vertices and
`2R` links and is a forest, so

\[
T=e-2R.
\]

Face incidence gives

\[
2e=4R+b+\sum_{F\text{ non4}}\deg F.
\]

Since

\[
\sum_{F\text{ non4}}\deg F=5f+g_F=4f+Q,
\]

we obtain

\[
\boxed{
T={b+Q\over2}+2f=h-s_Z+2f.
}
\tag{61.7}
\]

The second equality uses (61.5).

The argument allows bridges, repeated outer-walk occurrences, disconnected rhombic
regions, and arbitrary bounded exceptional faces.

## 61.3 Bad outer train ends cost at most `2x_B`

List the loaded force-hull vertices in cyclic order as

\[
b_1,\ldots,b_q.
\]

Choose their distinguished exterior occurrences on the outer contact-face boundary
walk. They occur in the same cyclic order. Split that cyclic walk into `q` subwalks

\[
W_i:b_i\leadsto b_{i+1}
\]

and let `ell_i` be the number of contact-edge occurrences in `W_i`. Then

\[
ell_i\ge1,
\qquad
\sum_i\ell_i=b=q+x_B,
\]

so

\[
\sum_i(\ell_i-1)=x_B.
\tag{61.8}
\]

Call `W_i` good if `ell_i=1` and bad otherwise. The number of bad intervals is at
most `x_B`, and the total number of outer-walk edge occurrences in bad intervals is

\[
\sum_{W_i\,\mathrm{bad}}\ell_i
\le x_B+x_B
=2x_B.
\tag{61.9}
\]

A good interval is one unit contact edge joining consecutive convex-hull vertices,
so it is exactly a unit force-hull side.

Therefore at most `2x_B` outer-face train-end incidences fail to lie on good unit hull
sides.

## 61.4 Exceptional train ends cost exactly `5f+g_F`

Every train end that is not on the outer face lies on an edge incident to a bounded
nonquadrilateral face. Their total face-incidence capacity is

\[
\boxed{
\sum_{F\text{ non4}}\deg F=5f+g_F.
}
\tag{61.10}
\]

This is an upper bound on the number of such train-end incidences, including singleton
trains between two exceptional faces.

## 61.5 At most two trains have two good hull ends

Call a train **good** if both of its terminal incidences are good unit force-hull side
contacts.

The two terminal edges of one train are parallel because opposite sides remain
parallel throughout the train. Their oriented hull directions are opposite. Strict
convexity makes the oriented side direction increase strictly around the hull, so one
unoriented direction appears at most twice.

Take two distinct good trains with projective directions represented by

\[
0\le\theta_i<\theta_j<\pi.
\]

Their four oriented hull-side directions occur cyclically as

\[
\theta_i,\ \theta_j,\ \theta_i+\pi,\ \theta_j+\pi.
\tag{61.11}
\]

Thus the endpoint pairs alternate on the boundary of the convex disk `F`.

The midpoint realization of each train is an embedded simple arc: strict monotone
projection from Section 61.2 rules out self-intersection. Two disjoint arcs in a disk
cannot join alternating boundary pairs. Hence every two good trains cross.

But the train-crossing graph is triangle-free. Therefore

\[
\boxed{T_{\rm good}\le2.}
\tag{61.12}
\]

This is the topological step that turns train geometry into quantitative diameter
branching.

## 61.6 Exact near-matching inequality

Every nongood train consumes at least one bad end. By (61.9), (61.10), and (61.12),

\[
T-2\le2x_B+5f+g_F.
\tag{61.13}
\]

Insert the exact train count (61.7):

\[
h-s_Z+2f-2
\le2x_B+5f+g_F,
\]

so

\[
\boxed{
h-2\le2x_B+3f+g_F+s_Z.}
\tag{61.14}
\]

Multiply (61.6) by three. Since

\[
3r_H-(2x_B+3f+g_F+s_Z)
=x_B+2g_F+5s_Z\ge0,
\]

we obtain the exact finite theorem

\[
\boxed{3(2h-q)\ge h-2.}
\tag{61.15}
\]

In particular canonical ZR/ZF gives `h>=ceil(D)`, hence

\[
\boxed{
2h-q\ge{\lceil D\rceil-2\over3}.
}
\tag{61.16}
\]

So linear nonmatching topology already follows without any asymptotic area theorem.

## 61.7 Defect-sensitive DB sharpens the constant

Put

\[
z:=Q+2s_Z=f+g_F+2s_Z.
\tag{61.17}
\]

Then `r_H=x_B+z`. From (61.14),

\[
3f+g_F+s_Z\le3z,
\]

and therefore

\[
\boxed{h-2\le2r_H+z.}
\tag{61.18}
\]

The canonical Section 59 difference-body theorem gives the exact finite inequality

\[
\boxed{
z
\le h+1-2D\cos((h-1)a_D),
\qquad
a_D=\arcsin{1\over2D}.}
\tag{61.19}
\]

Substituting (61.19) into (61.18) and cancelling `h` gives

\[
\boxed{
r_H
\ge D\cos((h-1)a_D)-{3\over2}.}
\tag{61.20}
\]

Equation (61.15) also gives

\[
\boxed{r_H\ge{h-2\over3}.}
\tag{61.21}
\]

Because the loaded diameter graph is a planar diameter pseudoforest, `h<=q`, while
`q<=per(F)<=pi D`; hence `h/D` is bounded. Pass to any subsequence on which

\[
{h\over D}\to y.
\]

Since

\[
a_D={1\over2D}+O(D^{-3}),
\]

we have `(h-1)a_D -> y/2`. Divide (61.20)-(61.21) by `D`. Every subsequential limit
`r` of `r_H/D` obeys

\[
\boxed{
r\ge\max\left\{{y\over3},\cos{y\over2}\right\}.}
\tag{61.22}
\]

On `0<y<pi`, `y/3` increases strictly and `cos(y/2)` decreases strictly. Their
maximum is minimized at the unique crossover

\[
{y_*\over3}=\cos{y_*\over2}.
\tag{61.23}
\]

Set

\[
c_*:={y_*\over3}.
\]

Then

\[
\boxed{c_*=\cos(3c_*/2),}
\tag{61.24}
\]

and (61.22) yields

\[
\boxed{
\liminf {2h-q\over D}\ge c_*.
}
\tag{61.25}
\]

Uniqueness follows because

\[
F(c)=c-\cos(3c/2)
\]

has

\[
F'(c)=1+{3\over2}\sin(3c/2)>0
\]

for `0<c<1`, while `F(0)<0<F(1)`.

The registered exact certificate proves

\[
\boxed{0.6099<c_*<0.61}
\tag{61.26}
\]

using rational alternating Taylor bounds for cosine; no decimal transcendental
evaluation is used by the certificate.

## 61.8 Optimality for the two audited inequalities

The constant `c_*` is not an artifact of a loose rearrangement. For fixed normalized
edge density `y=h/D`, write normalized currencies

\[
x={x_B\over D},\quad
u={f\over D},\quad
g={g_F\over D},\quad
s={s_Z\over D}.
\]

Ignoring vanishing `O(1/D)` terms, the train-end inequality requires

\[
2x+3\nu+g+s\ge y,
\tag{61.27}
\]

while the DB defect capacity gives

\[
\nu+g+2s\le y-2\cos(y/2).
\tag{61.28}
\]

The branching cost is

\[
r=x+\nu+g+2s.
\tag{61.29}
\]

Among the DB-controlled currencies, `nu` supplies the most train-end capacity per unit
branching cost. Solving the resulting fixed-`y` linear relaxation gives

\[
\boxed{
r_{\min}(y)=\max\{y/3,\cos(y/2)\}.}
\tag{61.30}
\]

Thus `c_*` is the best universal constant obtainable from the audited train-end and DB
inequalities alone. A stronger constant requires new geometry, not algebraic
rearrangement.

## 61.9 Woodall interpretation

In the Woodall forest branch, `d_H` is exactly the number of caterpillar components,
and each component has at least two vertices. Since `h=q-d_H`,

\[
2h-q=q-2d_H
=\sum_j(q_j-2).
\tag{61.31}
\]

Therefore

\[
\boxed{
\liminf {1\over D}\sum_j(q_j-2)\ge c_*>0.6099.
}
\tag{61.32}
\]

This is much stronger than merely excluding a perfect matching. A survivor cannot
hide its nonmatching topology in finitely many bounded-size caterpillars or in an
`o(D)` aggregate perturbation of matching components.

The exact finite inequality also gives

\[
5d_H\le2q+2,
\tag{61.33}
\]

so asymptotically

\[
\boxed{{d_H\over q}\le{2\over5}+o(1).}
\tag{61.34}
\]

In the Woodall cyclic branch `d_H=0` and `r_H=q`; Section 61 is primarily a forest
stability theorem there.

## 61.10 Scope and regressions

- **Perfect matching:** `r_H=0`, so (61.15) permits only `h<=2`; the large perfect
  matching branch is subsumed by the stronger theorem.
- **Matching plus finitely many bounded caterpillars:** `r_H=O(1)`; excluded for
  unbounded `D`.
- **Matching plus `o(D)` aggregate caterpillar excess:** excluded.
- **Regular odd shell:** Woodall cyclic with `r_H=q`; fully compatible.
- **Positive `s_Z`:** retained and charged honestly through both (61.6) and DB.
- **Exceptional faces:** retained via their exact train-end incidence `5f+g_F`.
- **Bridge excursions / repeated outer walk:** retained via the exact `2x_B` bad-end
  bound.
- **Contact-isolated source points:** retained; none are identified with contact-core
  vertices.
- **KKT coefficient floors:** not used.
- **Rejected cyclic Reuleaux-cap containment:** not used.

## 61.11 Remaining obstruction

Every forest survivor now has at least `c_*D-o(D)` aggregate caterpillar excess, but
this still does not force one giant caterpillar, a positive fraction of nontrivial
components, or positive KKT mass on the excess topology.

The next useful theorem should couple

\[
r_H=x_B+Q+2s_Z
\]

to the independently audited renormalized contact currency

\[
e_{BB}+2s_C-3(d_H+s_Z),
\]

or to the common bridge-block/negative-transfer structure, without double charging
`x_B`, `Q`, or `s_Z`.

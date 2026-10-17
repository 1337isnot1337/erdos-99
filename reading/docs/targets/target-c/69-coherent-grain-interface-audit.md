> Generated reading edition · [exact source](../../../../docs/targets/target-c/69-coherent-grain-interface-audit.md) · source SHA-256 `29d98eba4843ccf2c67b6122453ae4f1e088a829eb422ebe2493795d258dd5af`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — coherent grain/interface audit

This module takes the boundary-order angular defect from Section 68 and converts it
into an actual physical grain decomposition at the same boundary scale.  It proves
the fixed-width phase-bin/coarea theorem requested by the older Target B multigrain
analysis, but at the full post-ZF Target C scope rather than only for a pure rhombic
disk.

**LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.**

---

# 69. Boundary-order coherent grains and the exact core-density split

Retain the canonical notation.  Let `R_4` be the number of bounded quadrilateral
contact faces and let `Gamma` be their train-crossing multigraph: vertices are stopped
rhombus trains and each bounded quadrilateral face contributes one crossing edge.
Let

$$
a_0={\sqrt3\over2},\qquad c_0={\sqrt3\over4}.
$$

Section 68 proves

$$
E_4+\delta_K<c_0\operatorname{per}(K)\le c_0\pi D,
\tag{69.1}
$$

and, if

$$
\Delta:=\sum_{R}\delta_R
$$

is the total acute-angle defect of the strict unit rhombi, then

$$
\boxed{{3\Delta\over\pi}\le(2+\sqrt3)E_4=O(D).}
\tag{69.2}
$$

It also supplies a first crossing set `F_0` with

$$
|F_0|\le {3\Delta\over\pi}
\tag{69.3}
$$

such that `Gamma-F_0` has an exact real phase potential.  More precisely, with
`L=pi/3`, every train vertex `v` has

$$
x_v\in I
$$

for one interval `I` of length `L`, and a label `ell_v in Z/3`, while every retained
oriented crossing `u->v` satisfies

$$
\boxed{x_v-x_u=\delta_e>0},
\qquad
\phi_v\equiv x_v+L\ell_v\pmod\pi.
\tag{69.4}
$$

Here `phi_v` is the projective train direction.

The main new theorem is that for every fixed phase width `epsilon>0` one can make all
surviving physical rhombus grains `epsilon`-coherent while deleting only `O_epsilon(D)`
rhombi, and their **total physical interface perimeter is also `O_epsilon(D)`**.

## 69.1 Fixed-width phase bins by one-dimensional coarea

Fix

$$
0<\epsilon<{\pi\over6}.
\tag{69.5}
$$

For a shift `t in [0,epsilon)`, partition the real line by the boundaries

$$
t+k\epsilon,\qquad k\in\mathbb Z.
$$

There are only finitely many exceptional shifts for which some train potential `x_v`
lies exactly on a bin boundary. Restrict to the complementary full-measure set of
shifts and use the resulting half-open bins. For every edge `e=uv` of
`Gamma-F_0`, delete `e` exactly when `x_u` and `x_v` lie in different bins. Call
this second deleted set `F_t`. Thus every retained edge has both endpoint potentials
in one well-defined bin; a boundary vertex cannot connect two adjacent bins.

For one retained edge, (69.4) gives `|x_v-x_u|=delta_e`.  As `t` varies uniformly in
`[0,epsilon)`, the measure of shifts for which a bin boundary separates its endpoints
is at most

$$
\min\{\epsilon,\delta_e\}\le\delta_e.
$$

Removing the finite exceptional shift set does not change the integral. Therefore

$$
{1\over\epsilon}\int_0^\epsilon |F_t|\,dt
\le {1\over\epsilon}\sum_{e\notin F_0}\delta_e
\le {\Delta\over\epsilon}.
\tag{69.6}
$$

Choose a nonexceptional shift attaining the average or better and put

$$
F_\epsilon:=F_0\cup F_t.
$$

Then

$$
\boxed{
|F_\epsilon|
\le\left({3\over\pi}+{1\over\epsilon}\right)\Delta.
}
\tag{69.7}
$$

Using (69.2),

$$
\boxed{
|F_\epsilon|
\le (2+\sqrt3)\left(1+{\pi\over3\epsilon}\right)E_4
=O_\epsilon(D).
}
\tag{69.8}
$$

An explicit coarse coefficient follows from (69.1):

$$
|F_\epsilon|
< C_{del}(\epsilon)D,
\qquad
C_{del}(\epsilon)
:=c_0\pi(2+\sqrt3)
\left(1+{\pi\over3\epsilon}\right).
\tag{69.9}
$$

No minimum-degree pruning and no `lambda D^2` deletion term occurs.

## 69.2 Every surviving train component is genuinely three-phase coherent

If two train vertices lie in one connected component of `Gamma-F_epsilon`, every
edge path between them stays within one phase bin, because an edge crossing a bin
boundary was deleted.  Hence all potentials in that component lie in one interval of
length at most `epsilon`.

By (69.4), the actual train directions therefore lie within an `epsilon` window of
three projective phases separated by `pi/3`, according to `ell_v in Z/3`.

Thus every connected component of `Gamma-F_epsilon` is an exact
`epsilon`-coherent three-phase train component.  The statement is metric, not merely
a graph coloring.

## 69.3 Physical grains inherit train coherence

Delete from the contact complex the rhombus faces corresponding to `F_epsilon` and
retain every other bounded quadrilateral face.  Define a **physical grain** to be one
edge-connected component of the retained rhombi.

### Lemma 69.1

Two retained rhombi sharing a unit edge belong to the same connected component of
`Gamma-F_epsilon`.

### Proof

The common unit edge is one side of each rhombus.  Passing through that edge and then
through the opposite edge is the same stopped train in both rhombi.  Therefore the
two crossing edges of `Gamma` representing the two rhombi share that train vertex.
Since neither crossing edge was deleted, they lie in the same graph component.
`square`

Consequently every physical grain is contained in one train component and inherits
its `epsilon`-coherent three-phase frame.

## 69.4 All-topology physical interface perimeter

Let the physical grains be `G_1,...,G_s`.  Let `R_j` be the number of retained
rhombi in `G_j` and `P_j` the Euclidean perimeter of its polygonal union, counting
each boundary unit-edge occurrence once.  Holes are allowed and contribute their
boundary lengths normally.

A boundary edge of a retained grain cannot have a retained rhombus on its other side:
by Lemma 69.1 that rhombus would lie in the same physical grain.  Hence the other side
of every grain-boundary occurrence is exactly one of:

1. the old outer contact face;
2. a bounded nonquadrilateral contact face; or
3. a deleted quadrilateral face from `F_epsilon`.

The old outer-face occurrences total `b`.  If there are `f` bounded
nonquadrilateral faces and

$$
Q=\sum_P(\deg P-4),
$$

their total boundary-walk degree is

$$
\sum_P\deg P=4f+Q.
$$

Every deleted rhombus has four sides and can expose at most four retained-grain
boundary occurrences.  Therefore

$$
\boxed{
\sum_{j=1}^sP_j
\le b+4f+Q+4|F_\epsilon|.
}
\tag{69.10}
$$

Triangle-freeness gives `deg P>=5` for every nonquadrilateral bounded face, so
`f<=Q`.  The canonical ZF face ledger is

$$
b+Q=2(h-s_Z).
\tag{69.11}
$$

Thus

$$
b+4f+Q\le b+5Q\le5(b+Q)=10(h-s_Z)\le10h.
$$

Since `h<=q<=per(F)<=pi D`, (69.10) yields the explicit all-topology bound

$$
\boxed{
\sum_jP_j
\le C_{per}(\epsilon)D,
\qquad
C_{per}(\epsilon):=10\pi+4C_{del}(\epsilon).
}
\tag{69.12}
$$

This is the physical interface theorem that the older pure-disk multigrain report
could use only conditionally on an `O(D)` deletion set.  Section 68 plus the coarea
binning now supplies that deletion set canonically.

## 69.5 Square-root grain budget and a forced macroscopic coherent grain

Every retained strict unit rhombus has area at least `a_0`.  Let `A_j` be the area of
`G_j`.  Then

$$
A_j\ge a_0R_j.
\tag{69.13}
$$

The polygonal isoperimetric inequality, applied to a grain with all hole boundaries
included in its perimeter, gives

$$
P_j\ge2\sqrt{\pi A_j}
\ge2\sqrt{\pi a_0R_j}.
\tag{69.14}
$$

Summing and using (69.12),

$$
\boxed{
2\sqrt{\pi a_0}\sum_j\sqrt{R_j}
\le C_{per}(\epsilon)D.
}
\tag{69.15}
$$

Let

$$
R_{ret}:=\sum_jR_j=R_4-|F_\epsilon|,
\qquad
R_{max}:=\max_jR_j.
$$

Since

$$
R_{ret}=\sum_jR_j
\le\sqrt{R_{max}}\sum_j\sqrt{R_j},
$$

(69.15) gives the finite dominant-grain estimate

$$
\boxed{
R_{max}
\ge
{4\pi a_0\,R_{ret}^2\over C_{per}(\epsilon)^2D^2}.
}
\tag{69.16}
$$

In particular, if along a survivor sequence

$$
\liminf {R_4\over D^2}\ge r>0,
\tag{69.17}
$$

then `|F_epsilon|=O_epsilon(D)` and therefore

$$
\boxed{
\liminf {R_{max}\over D^2}
\ge {4\pi a_0r^2\over C_{per}(\epsilon)^2}>0.
}
\tag{69.18}
$$

So any quadratic rhombus branch contains one **physically connected,
`epsilon`-coherent, quadratic-size grain**.  The conclusion is stronger than merely
finding a large train-graph component.

The same square-root inequality shows that for every fixed `eta>0`, only
`O_{epsilon,eta}(1)` grains can have `R_j>=eta D^2`.

## 69.6 Local train segments are boundary-order

For later use, refine each physical grain into its local stopped train segments after
the deletions.  Opposite sides of a unit rhombus are parallel, so all transversal
edges in one local train segment are parallel.

Choose a unit normal to those edges and orient the segment through successive
rhombi.  Crossing a convex unit rhombus from one transversal side to its opposite
side increases the normal coordinate by the rhombus altitude, which is at least
`sqrt(3)/2`.  The sign stays positive when the segment continues through the shared
edge into the next rhombus.  Hence a finite local train segment cannot close into a
cycle.

Every local train segment is therefore a path with exactly two terminal
boundary-edge occurrences, and every grain-boundary unit edge terminates exactly one
local train segment.  If `T_j` is the number of local train segments in `G_j`, then

$$
\boxed{2T_j=P_j.}
\tag{69.19}
$$

Consequently

$$
\boxed{
\sum_jT_j={1\over2}\sum_jP_j=O_\epsilon(D).
}
\tag{69.20}
$$

A quadratic dominant grain therefore has `Theta(D^2)` rhombus crossings on only
`O_epsilon(D)` local train segments.  Its local train-crossing density is bounded
away from zero.  This is the correct launch point for the audited Target B
positive-density/grid machinery; topology and holes still have to be handled before
importing a pure-disk theorem verbatim.

## 69.7 Quadratic rhombus mass is exactly the quadratic positive-core branch

Let `m` be the number of vertices in the positive contact core.  Section 67 gives the
exact face count

$$
\boxed{m=R_4+f+q-(d_H+s_Z)+1.}
\tag{69.21}
$$

Every term besides `R_4` is boundary-order.  Indeed

$$
q\le\pi D,
\qquad d_H\le q,
$$

and the canonical difference-body defect inequality gives

$$
Q+2s_Z
\le h+1-2D\cos((h-1)\arcsin(1/(2D)))=O(D),
\tag{69.22}
$$

so `f<=Q=O(D)` and `s_Z=O(D)`.  Hence

$$
\boxed{m=R_4+O(D).}
\tag{69.23}
$$

Therefore the asymptotic branch split is exact:

- `m=Omega(D^2)` if and only if `R_4=Omega(D^2)` along a fixed positive-density
  subsequence, and then (69.18) forces a quadratic coherent physical grain;
- `m=o(D^2)` if and only if `R_4=o(D^2)`, and the positive KKT contact core itself is
  subquadratic.

Since the full global-minimizer population satisfies

$$
{n\over D^2}\longrightarrow {\pi\over2\sqrt3},
$$

the second branch means that asymptotically almost the entire source population lies
outside the positive contact core.  It does **not** mean those points may be deleted;
they remain part of the source and may include a quadratic external population.

## 69.8 What this closes and what remains

Section 69 closes the old physical multi-grain fragmentation ambiguity in the
quadratic-core branch at the level actually needed for further local-to-global work:
a boundary-order phase cut can no longer fragment quadratic rhombus mass into only
submacroscopic physical grains.  One connected coherent grain must remain, and there
are only finitely many macroscopic grains at every fixed size threshold.

What it does **not** yet prove is the final Target B contradiction on that grain.  The
audited DT/TG/PDG/GPI chain was proved under pure-disk and related topology hypotheses.
A Section 69 grain may have holes and may border exceptional/deleted faces.  Its
boundary and hole perimeter are only `O(D)`, but a theorem transporting the grid and
penetration machinery through those holes is still required before citing GPI as a
closure.

The complementary branch is now equally sharp:

$$
\boxed{m=o(D^2).}
$$

Any complete C-II proof must either

1. extend the audited coherent-grid/penetration contradiction to a quadratic Section
   69 grain with boundary-order holes/interfaces; or
2. rule out a subquadratic positive KKT core by a full-source packing, rigidity,
   representative-transfer, or strict-competitor theorem.

The first-contact absorption theorem by itself does not do (2), because the new
contacts in the contact-richer representative need not carry positive KKT
multipliers.

## 69.9 Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Section 68:
    E_4=O(D), total rhombus angular defect Delta=O(D).
    Delete F_0=O(D) crossings to obtain exact real phase potential x.

For fixed epsilon>0, randomly shift epsilon-wide bins in x.
An edge of phase increment delta crosses a bin boundary for at most a delta/epsilon
fraction of shifts.  Therefore one shift deletes at most Delta/epsilon=O_epsilon(D)
more rhombi.  Every surviving train component lies in one epsilon phase bin.

Let physical grains be edge-connected components of retained rhombi.  Their boundary
edges can face only the outer contact face, a nonquadrilateral bounded face, or a
deleted rhombus.  Hence
    sum P_j <= b+(4f+Q)+4|F_epsilon| = O_epsilon(D).
Thus
    2 sqrt(pi a0) sum sqrt(R_j) <= O_epsilon(D).
If R_4 >= rD^2, one physical epsilon-coherent grain has >=c(epsilon,r)D^2 rhombi.
Local train segments satisfy 2T_j=P_j, so that grain has positive crossing density on
O_epsilon(D) trains.

Exact Section-67 face count gives
    m=R_4+O(D).
So the surviving global split is:
    (A) quadratic positive core -> quadratic coherent physical grain;
    (B) m=o(D^2) -> almost all source points are outside the positive KKT core.

Next: hole/interface-stable grid penetration in (A), or full-source/representative
closure of the subquadratic-core branch (B).
```

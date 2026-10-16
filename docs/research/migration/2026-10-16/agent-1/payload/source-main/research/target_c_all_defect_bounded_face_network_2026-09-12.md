# Target C — all-defect phase gap forces a linear bounded-complexity face network

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only structural continuation of the all-defect phase/train-gap theorem; theorem authority unchanged.  

The all-defect phase/train theorem gives more than a linear lower bound on the total
number of exceptional faces. Combined with the exact global face-excess ledger it
forces a **linear number of bounded exceptional faces of uniformly bounded degree**.
The same stopped-train decomposition has an exact endpoint multigraph on the outer
face and these bounded defect faces, and positive KKT equilibrium forbids loops at a
bounded-face vertex, including singleton no-rhombus trains.

This turns the Type-II obstruction from “possibly a few large defect corridors” into a
linear finite-complexity network of actual bounded faces.

---

## 1. Inputs and notation

Work along a Type-II survivor sequence in the canonical post-ZF normalization. Let

- `D` be the source diameter;
- `q` be the number of loaded force-hull vertices;
- `k=d_H+s_Z>=0`;
- `f` be the number of bounded nonquadrilateral faces of the nonisolated positive-contact core;
- `Q=sum_F(deg F-4)` over those faces;
- `T` be the number of complete stopped trains from the all-defect train decomposition.

The proof-only all-defect theorem gives

\[
\liminf_{D\to\infty}{2f-k\over D}
\ge
\gamma,
\qquad
\gamma:=2\sqrt{\frac{\pi}{2\sqrt3}}-\frac\pi2
=0.333829286933018\ldots .
\tag{1.1}
\]

Canonical Section 63 gives

\[
q-x_B=Q+2k,
\qquad x_B\ge0,
\tag{1.2}
\]

and unit separation on the loaded convex hull gives

\[
q\le \operatorname{per}(F)\le\pi D.
\tag{1.3}
\]

Hence the exact finite upper bound

\[
\boxed{Q\le\pi D-2k.}
\tag{1.4}
\]

Every bounded nonquadrilateral face has degree at least five.

---

## 2. Linear abundance of bounded-degree defect faces

For an integer `K>=5`, let

\[
f_{\le K}:=\#\{F:\ 5\le\deg F\le K\},
\qquad
f_{>K}:=f-f_{\le K}.
\]

Every face counted by `f_{>K}` has degree at least `K+1`, hence contributes at least

\[
(K+1)-4=K-3
\]

to `Q`. Therefore

\[
\boxed{f_{>K}\le {Q\over K-3}.}
\tag{2.1}
\]

Fix `epsilon>0`. For all sufficiently large members, (1.1) gives

\[
f\ge {\gamma-\epsilon\over2}D+{k\over2}.
\tag{2.2}
\]

Combining (2.1), (2.2), and (1.4),

\[
\begin{aligned}
f_{\le K}
&\ge f-{Q\over K-3}\\
&\ge
\left({\gamma-\epsilon\over2}-{\pi\over K-3}\right)D
+\left({1\over2}+{2\over K-3}\right)k.
\end{aligned}
\tag{2.3}
\]

Since `k>=0`, send `epsilon->0`:

### Theorem 2.1 — bounded-complexity face abundance

For every fixed integer `K>=5`,

\[
\boxed{
\liminf_{D\to\infty}{f_{\le K}\over D}
\ge
{\gamma\over2}-{\pi\over K-3}.
}
\tag{2.4}
\]

The right side is positive as soon as

\[
K-3>{2\pi\over\gamma}.
\]

The smallest integer choice is `K=22`. Thus every Type-II survivor sequence has

\[
\boxed{
\liminf {f_{\le22}\over D}
\ge
{\gamma\over2}-{\pi\over19}
=0.001567661698625\ldots .
}
\tag{2.5}
\]

Two more convenient thresholds are

\[
\liminf {f_{\le23}\over D}
\ge0.009835010787019\ldots,
\tag{2.6}
\]

and

\[
\liminf {f_{\le24}\over D}
\ge0.017314993295566\ldots .
\tag{2.7}
\]

These constants are deliberately conservative. The content is qualitative and
structural: a Type-II survivor cannot store its mandatory exceptional-face population
only in a bounded number of macroscopic corridors or in a vanishing number of
high-degree faces. There are linearly many actual bounded faces of fixed finite
combinatorial complexity.

---

## 3. Exact stopped-train endpoint multigraph

There is a useful exact packaging of the same train decomposition.

Let `O` denote the outer face of the positive-contact core. Construct a multigraph
`M_train` whose vertices are

\[
\{O\}\cup\{F:F\text{ is a bounded nonquadrilateral face}\}.
\]

For every complete stopped train `tau`, add one multigraph edge as follows.

- If `tau` contains at least one strict rhombus, its two terminal contact edges each
  have one terminal side facing either `O` or a bounded nonquadrilateral face. Use
  those two terminal faces as the endpoints of the multigraph edge.
- If `tau` is a singleton contact edge incident to no strict rhombus, use its two
  **face-side occurrences** as the two endpoints. If the edge is a bridge, the same
  plane face may occur twice.

Every occurrence of a contact edge on `O` or on a bounded nonquadrilateral face is a
terminal side occurrence of exactly one stopped train. Conversely every stopped-train
end is one such occurrence. Therefore

\[
\boxed{\deg_{M_{train}}(O)=b,}
\tag{3.1}
\]

with outer-walk multiplicity, and for every bounded nonquadrilateral face `F`,

\[
\boxed{\deg_{M_{train}}(F)=\deg_G(F).}
\tag{3.2}
\]

Thus

\[
\sum_{v\in V(M_{train})}\deg(v)
=b+4f+Q.
\tag{3.3}
\]

The all-defect train identity

\[
T={b+Q\over2}+2f
\]

is equivalently the handshake identity

\[
\boxed{2|E(M_{train})|=b+4f+Q=2T.}
\tag{3.4}
\]

This is exact even with bridges, articulation vertices, and singleton trains.

---

## 4. No stopped train can loop at a bounded face

The previously proved bounded-face train-loop exclusion is usually stated for a
nontrivial strict-rhombus train. The same KKT cut argument also eliminates the only
missing singleton case.

### Lemma 4.1 — singleton bounded-face loop exclusion

A singleton stopped train cannot have both of its face-side occurrences on the same
bounded face.

### Proof

Let the singleton train be the positive contact edge `e=uv`. If the same plane face
lies on both sides of `e`, then `e` is a bridge of the connected positive-contact
core. Assume that common incident face `F` is bounded.

Choose a small transverse segment through an interior point of `e`, with its two
endpoints in `int F`. Because the same face lies on both sides of the bridge, those two
endpoints can be joined by a simple arc in `int F` avoiding the embedded contact graph
and all source vertices. The union is a simple closed curve `Gamma` crossing the
positive-contact graph exactly once, through `e`.

The curve lies in `F` except for the transverse crossing of `e`; hence it lies in the
force hull. Its bounded Jordan domain is contained in the convex hull of `Gamma`, and
therefore in the force hull. No loaded force-hull vertex can lie in this open bounded
Jordan domain, because every loaded vertex is an extreme point of the force hull.
Thus no positive diameter edge crosses the corresponding vertex cut.

Sum the relative-interior KKT equilibrium equations over the vertices on the bounded
shore. Internal forces cancel. There is no diameter reaction across the cut. The only
contact force crossing the cut is the positive contact `e`, with multiplier
`alpha_e>0`. The resulting boundary force is therefore the nonzero vector

\[
\alpha_e{(u-v)\over|u-v|},
\]

contradicting summed equilibrium. `square`

For a stopped train containing strict rhombi, the identical Jordan/KKT argument is the
bounded-face train-loop theorem: the midpoint path crosses exactly the parallel train
contacts with one common cut orientation, whose positive multipliers have nonzero
resultant.

Combining the two cases gives:

### Theorem 4.2 — bounded vertices of `M_train` are loop-free

\[
\boxed{
\text{Every loop of }M_{train}\text{ is based at the outer-face vertex }O.
}
\tag{4.1}
\]

In particular every endpoint incidence at a bounded defect face is genuine transport
to a different stopping face.

---

## 5. Consequence: a linear bounded-valence transport network

Combine Theorem 2.1 with (3.2) and Theorem 4.2. Every sufficiently large Type-II
survivor contains at least

\[
\left({\gamma\over2}-{\pi\over19}-o(1)\right)D
\]

distinct bounded vertices of `M_train`, each of degree between `5` and `22`, and none
of them supports a loop.

Equivalently, at least

\[
5\left({\gamma\over2}-{\pi\over19}-o(1)\right)D
=0.007838308493126\ldots D-o(D)
\]

bounded-face endpoint incidences are carried by this fixed-complexity subnetwork alone.
Using `K=23` or `24` gives a larger population at the cost of a slightly larger fixed
valence ceiling.

This statement is compatible with the oblique-lattice regression only after genuine
bounded holes are inserted: the pure oblique parallelogram patch has no such linear
bounded-face population. Thus any closing argument may now target transport among a
linear family of finite-complexity inactive faces rather than arbitrary diffuse defect
perimeter.

---

## 6. What remains open

This theorem does not by itself close Type II. A linear family of bounded pentagonal
or other finite-degree inactive chambers can carry only boundary-order total area and
Oler slack, which is compatible with the canonical Type-II asymptotics.

The next useful theorem must exploit additional structure of `M_train`, for example:

1. phase constraints on transport between its bounded vertices;
2. positive-stress reciprocal geometry of train cuts;
3. incompatibility between the bounded-valence transport network and the near-disk
   loaded diameter support; or
4. a source-preserving local exchange forced by a positive density of finite-complexity
   chambers.

No source point is removed, and no full-source extension of the Section-57 affine
kernel is used.

**Disposition:** proved proof-only structural theorem. C-II remains open.
> Generated reading edition · [exact source](../../../../docs/targets/target-c/72-primitive-shell-leaf-forcing-audit.md) · source SHA-256 `57a53f0c03656fa6afb4f4d36986d259b0499a9696fce851ba362064763b8029`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 1 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

# Target C — primitive-shell leaf-forcing dependency audit

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Scope:** exact primitive all-loaded unit-shell normal form

```math
m=0,\qquad d_H+s_Z=2,\qquad C=C_q.
```

This independently checks the historical CY/CG/LF chain behind
`docs/reports/target_c_cyclic_leaf_forcing_2026-09-09.md`. Historical use of the word
“cyclic” here refers to the primitive contact-cycle/shell endpoint; it is not an
unqualified statement about the full Woodall-cyclic topology.

The load-bearing chain is valid after one correction:

- CY universal positive cycle support is valid;
- CY selected diameter edge-cover and stress-polytope dimension are valid;
- CG support-stable generic transfer and diameter-only face lattice are valid;
- every full-diameter leaf edge is positive in every normalized KKT stress;
- when `s_Z>0`, the KKT-polytope facets force at least `s_Z+1=3-d_H`
  **nonleaf–nonleaf** full-diameter edges;
- the historical report's formula was incorrectly stated also for `s_Z=0,d_H=2`.
  In that case the normalized stress polytope is a singleton, the facet argument is
  vacuous, and no nonleaf-edge lower bound follows from LF. The separate rigidity-
  circuit conclusion remains valid.

Thus the corrected finite conclusion is

```math
\boxed{
\begin{array}{c|c|c}
(d_H,s_Z)&\dim\mathcal S&\text{LF conclusion}\\ \hline
(0,2)&2&\text{at least 3 nonleaf--nonleaf diameter edges}\\
(1,1)&1&\text{at least 2 nonleaf--nonleaf diameter edges}\\
(2,0)&0&\text{no facet-derived nonleaf-edge bound.}
\end{array}}
```

The theorem is structural only. It does not close the primitive S1 endpoint and does
not give a uniform-in-`D` stress-weight floor.

The CG conclusions in Sections 3--5 are asserted for `q>=6`. This is automatic in
the sufficiently-large Target C regime: canonical ZF gives `h>=ceil(D)`, while a
`q`-vertex diameter graph has `h<=binom(q,2)`. Thus any unbounded survivor sequence
eventually has `q>=6`. No finite `q<6` CG claim is promoted here.

---

## 1. Primitive endpoint and CY support theorem

The already independently audited PN/ME/CY reduction gives

```math
m=0,\qquad d_H+s_Z=2,\qquad C=C_q,
```

where the complete nonisolated positive-contact core is the strict convex unit cycle
on the `q` loaded vertices.

Fix any normalized KKT stress `s=(alpha,beta)` of this same source and let `C_s,H_s`
be its positive supports. Suppose `C_s` were a proper subset of `C_q`. Positive-support
connectivity makes the unique nontrivial component a path. Let `b` be one path endpoint
and `bc` its only positive contact.

Every subset of vertices of the strict convex original hull remains in convex position,
so `b` is an extreme vertex of `conv V(C_s)`. The selected force-hull theorem therefore
makes `b` a selected diameter terminal. Choose the inward normal `n` to the original
hull side `bc`. The contact force on `bc` has zero `n` component, whereas every
positive selected diameter partner `k` is a selected hull vertex distinct from `b,c`
and satisfies

```math
n\cdot(b-k)<0.
```

All selected diameter weights are positive, so equilibrium at `b` is impossible.
Hence

```math
\boxed{C_s=C_q\quad\text{for every normalized stress }s.}
\tag{72.1}
```

Because the selected force hull is then the full `q`-vertex polygon, every one of its
vertices is selected diameter-loaded:

```math
\boxed{B_s=B_+.}
\tag{72.2}
```

Equivalently `H_s` is an edge cover of all `q` loaded terminals.

---

## 2. Exact normalized stress-polytope dimension

The full mixed support has

```math
q+h=q+(q-d_H)=2q-d_H
```

rows. The canonical ZF rigidity theorem, interpreted on this nonisolated equality
core, gives rank `2q-3`. Therefore the signed equilibrium-dependence space has
dimension

```math
3-d_H=s_Z+1.
```

The diameter-total normalization is a nonzero linear functional on this dependence
space because the relative-interior KKT stress has positive total diameter weight.
Consequently the normalized stress polytope has affine dimension

```math
\boxed{\dim\mathcal S=s_Z=2-d_H.}
\tag{72.3}
```

No contact-isolated full-source point is being made rigid here; all matrices in this
section live on the `q`-vertex nonisolated cycle core.

---

## 3. CG applies uniformly over the normalized polytope for `q>=6`

Assume `q>=6` for Sections 3--5. Equations (72.1)-(72.2) give, for every normalized stress:

- a connected circular-planar positive contact network on the complete terminal set;
- a selected actual-diameter graph with no isolated terminal;
- at least three selected diameter edges when `q>=6`;
- pairwise crossing-or-incident diameter chords.

These are exactly the hypotheses of the independently checked zero-transfer/additive-
resistance theorem used in canonical ZR. If a selected stress were in C56-Z, its
complete terminal resistance metric would be additive. The SEPq degree consequence
would force loaded contact degree at least `q-1`, contradicting the actual cycle degree
two for `q>=6`.

Hence every selected stress is in C56-G. The same SVD/Schur transfer as canonical ZR
then gives, on the `q`-vertex cycle core,

```math
\boxed{
\ker\Omega_s=\operatorname{span}\{\mathbf1,P_x,P_y\},
\qquad \operatorname{rank}\Omega_s=q-3.}
\tag{72.4}
```

Since every cycle coefficient is positive everywhere on the compact normalized stress
polytope, no proper polytope face is created by `alpha_e=0`. Every proper face is
therefore induced by one or more diameter-coordinate equations

```math
\beta_h=0.
\tag{72.5}
```

This is the CG diameter-only face-lattice statement.

---

## 4. Full-H leaf edges are frozen across the stress polytope

Let `u` have full actual diameter degree one and let `h=uv` be its unique incident
full-diameter edge. Every selected `H_s` edge-covers the full terminal set, so `u` must
be incident to a selected diameter edge. Since `h` is its only possible actual diameter
edge,

```math
\boxed{\beta_h(s)>0\quad\text{for every }s\in\mathcal S.}
\tag{72.6}
```

For a fixed source compactness even gives a positive source-dependent floor
`min_s beta_h(s)>0`; no uniform-in-`D` floor follows.

Thus only full-diameter edges whose two endpoints both have degree at least two can
vanish on a KKT-polytope boundary.

---

## 5. Correct facet count for the positive-dimensional cases

Assume now

```math
d:=\dim\mathcal S=s_Z>0.
```

A full-dimensional compact `d`-polytope has at least `d+1` facets. Let `F_0` be one
facet. By (72.5), `F_0` lies in at least one coordinate hyperplane `beta_h=0`. The
coordinate intersection

```math
\mathcal S\cap\{\beta_h=0\}
```

is a proper face because the relative-interior full-support stress has `beta_h>0`.
Since it contains the facet `F_0`, maximality of facets makes the two faces equal.

One diameter coordinate cannot define two distinct facets: its zero-set intersection
with the convex polytope is one convex face. Therefore at least `d+1` distinct diameter
coordinates vanish somewhere on the boundary. By (72.6), none is incident to a
full-H leaf. Hence

```math
\boxed{
|\{uv\in E(H):\deg_Hu\ge2,\ \deg_Hv\ge2\}|
\ge s_Z+1=3-d_H
\qquad(s_Z>0).}
\tag{72.7}
```

Consequences:

- `(d_H,s_Z)=(0,2)`: at least three nonleaf–nonleaf full-diameter edges;
- `(d_H,s_Z)=(1,1)`: at least two.

In the `d_H=1` primitive shell, canonical Woodall topology makes the full diameter
graph a connected caterpillar tree. Its nonleaf spine therefore contains at least two
edges and at least three vertices. In particular the tree is neither a star nor a
double-star with a one-edge nonleaf spine.

---

## 6. Correction of the `d_H=2,s_Z=0` statement

When

```math
(d_H,s_Z)=(2,0),
```

the normalized stress polytope is a single point. There is no positive-dimensional
boundary along which a diameter coefficient is forced to vanish. The facet argument in
Section 5 is therefore unavailable.

The historical LF report simultaneously stated the uniform inequality

```math
\#\{\text{nonleaf--nonleaf diameter edges}\}\ge s_Z+1=1
```

and later called the `d_H=2` facet argument “vacuous.” These statements are not
compatible. The former must be restricted to `s_Z>0`.

What **does** survive at `d_H=2` is CY's separate circuit theorem: the full mixed
support has `2q-2` rows, rigidity rank `2q-3`, and a unique full-support dependence, so
it is a planar rigidity-matroid circuit. That circuit fact does not imply the missing
nonleaf-edge count by itself.

---

## 7. Interaction with the canonical P1/S1 state

The current canonical primitive-shell audit focuses on

```math
d_H=1,\qquad s_Z=1.
```

There the corrected leaf theorem **does** apply and gives at least two full-diameter
edges joining two nonleaf vertices. This is compatible with the verified `q=13` S1
regression and does not close S1.

The structural gain is that all normalized-stress support motion is confined to the
nonleaf diameter spine: full-H leaf-edge coefficients stay positive throughout the
entire KKT interval. Any future endpoint argument in S1 may therefore push to either
stress-polytope endpoint without losing any leaf diameter edge.

No claim is made that this alone transfers the reciprocal-square S1 algebra to global
optimality or excludes the verified finite regression.

---

## 8. Disposition

The historical CY and CG support statements survive independent audit in the narrow
primitive-shell scope. Historical LF survives after the finite-dimensional correction

```math
\boxed{\text{apply the `s\_Z+1` nonleaf-edge bound only when }s_Z>0.}
```

This is an audited structural refinement, not a Level I closure and not an
unqualified Woodall-cyclic theorem.

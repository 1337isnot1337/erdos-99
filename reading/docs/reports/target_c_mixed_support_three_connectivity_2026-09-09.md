> Generated reading edition · [exact source](../../../docs/reports/target_c_mixed_support_three_connectivity_2026-09-09.md) · source SHA-256 `5154c7c834d30f1768fcc447820bf031cf79cefa64733d0b09f6b354b836ff08`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-FE73FCEC908A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_mixed_support_three_connectivity_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=f82dc8f0785f279bf79883e22035e4be6446ddc9; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — the post-ZF mixed support graph is 3-vertex-connected

**Date:** 2026-09-09  
**Repository base:** `b198afbf3d56dfdd2decbad64b4226038cfe2949`  
**Run type:** exact structural theorem  
**Target:** Target C C-II after ZR/ZF/U1  
**Depends on:** ZF infinitesimal rigidity and U1 universal rigidity of the equality bar framework on `C union H`  
**External input:** none beyond those existing report-level dependencies  
**LEVEL I STATUS:** STILL OPEN

Let

$$
G_M:=(V,C\cup H)
$$

be the mixed equality-bar support on the nonisolated post-C65 core: `C` is the full unit-contact graph on the core and `H` is the full actual diameter graph.  ZF proves the planar bar framework `(G_M,p)` is infinitesimally rigid.  U1 proves the same equality-bar framework is universally rigid.

These two facts together force a graph-theoretic property not previously recorded in the Target C stack:

$$
\boxed{G_M\text{ is 3-vertex-connected}.}
\tag{MC.1}
$$

The proof is elementary.  A cut vertex gives an infinitesimal rotation of one side.  A two-vertex cut gives a finite reflection of one side across the separator line. Universal rigidity says the reflection can be congruent only if one whole side is collinear with the separator; but such a collinear side then has a transverse infinitesimal flex, contradicting ZF.

This is a statement about the **mixed equality support** `C union H`.  The contact graph `C` alone may still have bridges and articulation structure.

---

## 1. Setup

Work in the sufficiently large two-dimensional C-II regime.  Distinct source points are at distance at least one, so all vertex positions are distinct.  Also `D>1`, hence contact edges and diameter edges are disjoint and `G_M` is a simple graph.

ZF gives

$$
\operatorname{rank}R(G_M,p)=2v-3.
\tag{MC.2}
$$

Thus `(G_M,p)` has no non-Euclidean infinitesimal flex.

U1 gives:

> every realization in any Euclidean dimension having exactly the same lengths on all edges of `G_M` is congruent to `p`.

The force hull is two-dimensional, so `p(V)` affinely spans the plane.

---

## 2. No cut vertex

Assume a vertex `u` is a cut vertex of `G_M`.  Let `S` be the vertex set of one connected component of

$$
G_M-u.
$$

Because deletion of `u` leaves at least two components, there is at least one vertex outside `S union {u}`.

Define a planar velocity field by

$$
v_x=
\begin{cases}
J(p_x-p_u),&x\in S,\\
0,&x\notin S,
\end{cases}
\tag{MC.3}
$$

where `J` is rotation by `pi/2`.

For an edge `xy` with `x,y in S`,

$$
v_x-v_y=J(p_x-p_y),
$$

so

$$
(p_x-p_y)\cdot(v_x-v_y)=0.
$$

For an edge `xu` with `x in S`,

$$
(p_x-p_u)\cdot v_x
=(p_x-p_u)\cdot J(p_x-p_u)=0.
$$

There are no edges from `S` to the rest of the graph except through `u`.  All remaining edges have both endpoint velocities zero.  Hence MC.3 is an infinitesimal flex of the whole mixed framework.

It is nonzero because `S` contains a vertex distinct from `u`.  It is not an infinitesimal Euclidean motion of the whole framework: both `u` and a distinct vertex outside `S` are fixed, while some vertex of `S` moves.  Equivalently, a global infinitesimal rigid motion agreeing with MC.3 on the fixed side would have to vanish identically.

This contradicts ZF. Therefore:

$$
\boxed{G_M\text{ is 2-connected}.}
\tag{MC.4}
$$

---

## 3. A two-vertex cut produces a partial reflection

Assume for contradiction that distinct vertices `u,v` form a two-vertex cut. Since the framework is 2-connected, `u` and `v` are distinct positions and every component of

$$
G_M-\{u,v\}
$$

has at least one vertex.

Let

$$
\ell:=\operatorname{aff}\{p_u,p_v\}
$$

be the separator line.  Let `S` be one component of `G_M-{u,v}`.

Reflect every point `p_x`, `x in S`, across `ell`, while leaving all other vertices fixed.  Call the resulting configuration `p^S`.

Every mixed edge retains its length:

- edges with both endpoints in `S` are carried by one Euclidean reflection;
- an edge from `S` to `u` or `v` retains length because the reflector fixes `p_u,p_v`;
- there is no edge from `S` to another component of `G_M-{u,v}`;
- all remaining vertices are fixed.

Thus

$$
(G_M,p^S)
$$

has exactly the same bar lengths as `(G_M,p)`.

By U1, `p^S` must be congruent to `p`.

---

## 4. At most one separator component can leave the separator line

Suppose two distinct components `S,T` of `G_M-{u,v}` each contain a point off `ell`. Reflect only `S`.

The configurations `p` and `p^S` agree pointwise on

$$
u,\quad v,
$$

and on any chosen off-line vertex `t in T`.

The three points

$$
p_u,p_v,p_t
$$

are noncollinear.  A Euclidean isometry fixing three noncollinear planar points is the identity.  Hence any congruence from `p` to `p^S` fixing the vertex labels would have to be the identity on the whole configuration.

But an off-line point of `S` was moved by the reflection. Contradiction.

Therefore:

### Lemma MC.1

For every two-vertex cut `{u,v}`, at most one component of `G_M-{u,v}` contains a vertex off the separator line `ell=uv`.

Because the full configuration spans two dimensions, at least one component does contain an off-line vertex. Since a two-vertex cut has at least two components, there is therefore at least one **other** component `T` whose every vertex lies on `ell`.

---

## 5. A collinear separator component gives a transverse infinitesimal flex

Let `T` be a component of `G_M-{u,v}` whose vertices all lie on `ell`.

Choose a unit vector `n` perpendicular to `ell`.  Define velocities

$$
w_x=
\begin{cases}
\eta_x n,&x\in T,\\
0,&x\notin T,
\end{cases}
\tag{MC.5}
$$

where the scalars `eta_x` are not all zero.  For example, take one `eta_x=1` and all other `eta` values zero.

Every edge having an endpoint in `T` joins two points on the line `ell`: internal edges of `T` do so by collinearity, and any edge leaving `T` can only end at `u` or `v`, which also lie on `ell`.  Hence every such edge vector is parallel to `ell`, while every velocity difference in MC.5 is perpendicular to `ell`. Therefore

$$
(p_i-p_j)\cdot(w_i-w_j)=0
$$

for every edge incident to `T`.  All other edges have zero endpoint velocities.

Thus MC.5 is an infinitesimal flex of `(G_M,p)`.

It is nonzero.  It is not a global infinitesimal Euclidean motion because both distinct separator vertices `u,v` are fixed; an infinitesimal Euclidean motion fixing two distinct points is zero everywhere.

This contradicts ZF.

Therefore no two-vertex cut exists.

Combining with MC.4 proves MC.1.

---

## 6. Immediate graph-theoretic consequences

### Corollary MC.2 — mixed minimum degree

Every vertex has mixed degree at least three:

$$
\boxed{
\deg_C(x)+\deg_H(x)\ge3
\qquad(x\in V).
}
\tag{MC.6}
$$

This follows from 3-connectivity.

For an unloaded vertex, `deg_H=0`, so this is consistent with the existing contact-degree lower bounds. For a loaded diameter endpoint `b`, it says

$$
\boxed{
\deg_C(b)\ge3-\deg_H(b).
}
\tag{MC.7}
$$

In particular every diameter-graph leaf has at least two contact neighbors.

### Corollary MC.3 — three disjoint mixed paths

By Menger's theorem, between any two distinct mixed-support vertices there are three internally vertex-disjoint paths in `C union H`.

This can be applied to contact bridge/block decompositions only after remembering that the bypassing paths may use diameter edges; MC does not imply the contact graph itself is 3-connected.

### Corollary MC.4 — every two-terminal mixed piece is nonseparable

There is no proper nonempty vertex set `S subset V\{u,v}` whose mixed neighbors outside `S` are contained in `{u,v}`.  Any such set would be a component or union of components behind the two-separator `{u,v}`.

This is a useful replacement for several future case splits involving mixed-support 2-sums.

---

## 7. Consequence for the `s_Z=0` phase

Now additionally assume

$$
s_Z=0.
$$

ZF gives mixed rigidity rank `2v-3`, while

$$
e+h=2v-2.
$$

Hence the mixed row-dependence space is one-dimensional.  The relative-interior KKT self-stress has every actual contact and every actual diameter coefficient nonzero, so its row dependence has support on **all** edges.

If any proper edge subset were dependent, it would support another nonzero row dependence with at least one zero coordinate, linearly independent of the full-support KKT dependence.  This is impossible. Therefore:

### Corollary MC.5 — 3-connected rigidity circuit at `s_Z=0`

When `s_Z=0`, the mixed graph `G_M=C union H` is a 3-connected circuit of the planar rigidity matroid:

$$
\boxed{
|E(G_M)|=2v-2,
}
\tag{MC.8}
$$

and every proper edge subset is independent in the actual planar rigidity matrix.

Equivalently, for every proper vertex subset `W` with `|W|>=2`,

$$
\boxed{
|E(G_M[W])|
\le2|W|-3.
}
\tag{MC.9}
$$

Moreover deleting **any one** mixed edge leaves exactly `2v-3` independent rows, hence an infinitesimally rigid planar bar framework.

This is a substantially narrower exact topology than the previous phrase “one mandatory mixed dependence.”

---

## 8. Scope and regressions

- **Unit square:** the mixed graph consisting of four unit sides and two diameter diagonals is `K_4`, a 3-connected planar rigidity circuit.  It is a binding finite regression, so MC does not claim that the `s_Z=0` circuit phase is empty.
- **Contact bridges:** a bridge of `C` may still exist; diameter edges can supply the mixed bypasses required by MC.
- **Two-separator reflection:** universal rigidity is used only for equality bars. No cable/strut inequality conclusion is inferred.
- **Collinear side:** the finite reflection itself may be congruent when the opposite side supplies the global mirror. ZF is what eliminates the necessarily collinear second component.
- **Generic rigidity theory:** no generic-position assumption is used. MC.9 is obtained from independence of the actual rigidity rows, not from a generic Laman theorem.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| no cut vertex | proved | explicit infinitesimal side rotation |
| partial reflection preserves all mixed bar lengths | proved | two-separator geometry |
| at most one off-line separator component | proved | U1 universal rigidity + three fixed noncollinear points |
| collinear separator component impossible | proved | explicit transverse infinitesimal flex |
| mixed support is 3-connected | proved | preceding steps |
| `s_Z=0` gives actual rigidity circuit | proved | one-dimensional row kernel + full-support KKT dependence |
| `s_Z=0` branch impossible | not proved | `K_4` square is a finite regression; large circuits remain |
| Level I | still open | need exploit 3-connected circuit / high-surplus geometry |

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let G_M=C union H be the mixed equality-bar support.
ZF: (G_M,p) is infinitesimally rigid.
U1: (G_M,p) is universally rigid.

A cut vertex gives an infinitesimal rotation of one side, so none exists.
If {u,v} is a 2-cut, reflect one component across line uv. Universal rigidity
forces at most one separator component to contain an off-line point; because the
framework spans R^2, some other component is entirely collinear with uv. Giving
that collinear component transverse velocities produces an infinitesimal flex,
contradicting ZF.
Therefore G_M is 3-vertex-connected.

If s_Z=0, then e+h=2v-2 and rank R=2v-3. The row kernel is one-dimensional,
and its relative-interior KKT vector is nonzero on every mixed edge. Hence no
proper edge subset is dependent: G_M is a 3-connected planar-rigidity circuit.
Every edge deletion leaves an infinitesimally rigid 2v-3-row framework.

Next target: combine 3-connectivity/circuit sparsity with the diameter-thrackle
caterpillar structure and the contact planarity/degree caps.
```

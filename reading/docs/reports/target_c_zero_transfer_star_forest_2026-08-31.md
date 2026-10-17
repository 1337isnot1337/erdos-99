> Generated reading edition · [exact source](../../../docs/reports/target_c_zero_transfer_star_forest_2026-08-31.md) · source SHA-256 `6ee6409b92a8b6d11a558922de03753a04036670c43e8cf5296fbd3d17821d7e`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-1982E0E59F18","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: zero-transfer star-forest theorem

**Date:** 2026-08-31  
**Repository base:** `0ae3ce57` (main after C57 / PR #59)  
**Run type:** exact equality-structure reduction  
**Target:** Target C Gate C-I / C57 zero-transfer body-hinge phase  
**Depends on:** C50 Kalmanson response, C53 diameter-thrackle geometry, C56 minimum-transfer collapse, C57 extreme-body rigidity, SEPq additive-response separator

## LEVEL I STATUS

**STILL OPEN.**

C56 proves that a selected two-dimensional null stress can carry genuine diameter
shear only in the exact zero-transfer phase

```math
K=Q^{\mathsf T}\Lambda^+Q=B^{-1}.
```

C57 then proves that two null-face extreme bodies with different angular rates have a
midpoint stress in precisely this phase. This report classifies the positive diameter
graph of every such zero-transfer stress.

The conclusion is sharp and finite:

```math
\boxed{
\text{every connected positive-diameter component is a star of degree at most }5.
}
```

Moreover each star component has an additive effective-resistance metric and therefore
a source-preserving one-vertex terminal separator whenever it has at least four
terminals. Thus the remaining C-I body-hinge obstruction cannot hide in a long
caterpillar, long diameter path, or any other extended zero-transfer forest.

## 1. Setup

Fix a normalized KKT stress `s=(alpha,beta)` in the C56-Z phase. Let `G_s` be its
connected positive unit-contact graph, let `B=V(H_s)` be its positive diameter endpoint
set, let `Lambda` be the positive-contact Dirichlet response on `B`, and put

```math
R=\Lambda^+.
```

Orient the positive diameter edges and let `Q` be the boundary-by-edge incidence
matrix. With

```math
B_H=\operatorname{diag}(\beta_e:e\in H_s),
```

C56-Z gives

```math
\boxed{
K:=Q^{\mathsf T}RQ=B_H^{-1}.
}
\tag{C58.1}
```

In particular `K` is positive definite, so the columns of `Q` are independent and
`H_s` is a forest.

The effective-resistance metric on `B` is

```math
W_{uv}=(e_u-e_v)^{\mathsf T}R(e_u-e_v).
\tag{C58.2}
```

By the C50 circular-planar response theorem, `W` is Kalmanson in the cyclic order of
the force-hull boundary. The Kalmanson inequalities remain true after restriction to
any subset of terminals, in its induced cyclic order.

## 2. Every diameter-tree component carries its own exact tree metric

Let `T` be one connected component of the forest `H_s`. Give every edge `e` of `T`
the positive length

```math
r_e=\frac1{\beta_e}.
\tag{C58.3}
```

### Theorem C58.1 (zero transfer gives the diameter-tree metric)

For every `u,v in V(T)`,

```math
\boxed{
W_{uv}=\sum_{e\in P_T(u,v)}r_e,
}
\tag{C58.4}
```

where `P_T(u,v)` is the unique path from `u` to `v` in `T`.

#### Proof

Choose signs `sigma_e in {+1,-1}` along the oriented path so that

```math
e_u-e_v
=\sum_{e\in P_T(u,v)}\sigma_e q_e,
\tag{C58.5}
```

where `q_e` is the incidence column of `Q`. Let `z` be the corresponding edge vector,
zero off that path. Then by (C58.1),

```math
\begin{aligned}
W_{uv}
&=(Qz)^{\mathsf T}R(Qz)\\
&=z^{\mathsf T}Kz\\
&=\sum_{e\in P_T(u,v)}\frac{\sigma_e^2}{\beta_e}\\
&=\sum_{e\in P_T(u,v)}r_e.
\end{aligned}
```

`\square`

Thus the physical contact response, restricted to the terminals of one positive
diameter component, is exactly the positive weighted tree metric of that abstract
diameter tree.

## 3. A Kalmanson tree metric has only circular edge splits

Let a positive weighted tree `T` have a cyclic order on its vertex set. An edge `g`
of `T` determines a bipartition

```math
V(T)=A_g\sqcup B_g.
```

Call this split **circular** when one side is a cyclic interval, equivalently when the
two sides do not alternate around the circle.

### Lemma C58.2 (tree-edge splits are circular)

If the positive weighted tree metric of `T` is Kalmanson in the given cyclic order,
then every edge split `A_g|B_g` is circular.

#### Proof

Suppose the split of some positive-length edge `g` is not circular. Then there are four
vertices in cyclic order

```math
a,b,c,d
```

with

```math
a,c\in A_g,
\qquad
b,d\in B_g.
\tag{C58.6}
```

Restrict the tree metric to these four marked vertices. In the minimal subtree joining
them, the edge `g` lies in the positive internal path realizing the quartet split

```math
ac\mid bd.
```

Hence the tree four-point identity gives

```math
d(a,c)+d(b,d)
<d(a,b)+d(c,d)
=d(a,d)+d(b,c).
\tag{C58.7}
```

The inequality is strict because the internal path contains the positive edge `g`.

But the Kalmanson inequalities for four vertices in cyclic order `a,b,c,d` require the
crossing sum to be maximal:

```math
d(a,c)+d(b,d)
\ge d(a,b)+d(c,d),
```

```math
d(a,c)+d(b,d)
\ge d(a,d)+d(b,c).
\tag{C58.8}
```

Equations (C58.7)-(C58.8) contradict each other. Therefore every tree-edge split is
circular. `\square`

Applying the lemma to (C58.4), every edge split of every component of `H_s` is a
circular split in the inherited force-hull order.

## 4. Circular splits plus the diameter-thrackle property force a star

The diameter graph of any planar point set is a geometric thrackle: two distinct
diameter edges either share a vertex or their straight segments cross. In particular,
two vertex-disjoint positive diameter edges must have alternating endpoints on the
strictly convex force hull.

### Theorem C58.3 (zero-transfer diameter components are stars)

Every connected component `T` of `H_s` is a star. Equivalently, `T` has matching
number at most one.

#### Proof

Assume `T` contains two vertex-disjoint edges `e` and `f`. Because `T` is a tree, the
unique route from `e` to `f` contains an edge `g`, distinct from `e` and `f`, whose
deletion separates both endpoints of `e` from both endpoints of `f`.

By Lemma C58.2, the two sides of the split induced by `g` are complementary cyclic
intervals. Therefore the two endpoints of `e` lie in one interval and the two endpoints
of `f` lie in the other. Their four endpoints do not alternate, so the straight chords
`e` and `f` do not cross.

They also do not share an endpoint, contradicting the diameter-thrackle property.
Hence `T` has no two disjoint edges.

A tree with no two disjoint edges is a star: if two adjacent edges have common vertex
`o`, any edge not incident with `o` would be disjoint from one of them. The one-edge
case is a star as well. `\square`

Therefore

```math
\boxed{
H_s\text{ is a disjoint union of diameter stars.}
}
\tag{C58.9}
```

This removes every non-star caterpillar allowed by the purely combinatorial
convex-thrackle classification.

## 5. Each star component is an additive response

Let a component `T` have center `o` and leaves `v_1,...,v_k`. Put

```math
r_o=0,
\qquad
r_{v_i}=\frac1{\beta_{ov_i}}.
\tag{C58.10}
```

The tree-metric formula gives, for distinct vertices `x,y in V(T)`,

```math
\boxed{
W_{xy}=r_x+r_y.
}
\tag{C58.11}
```

Thus the resistance metric on the `q=k+1` terminals of the star is additive, with the
star center as the unique zero-parameter terminal.

Other positive diameter endpoints may be present in other components. Re-designate
only `V(T)` as the terminal set and treat all other vertices of the same connected
positive contact network as nonterminals. Kron elimination preserves all pairwise
effective resistances in `V(T)`, and circular planarity is unchanged. Therefore the
source-preserving SEPq theorem applies to (C58.11).

### Corollary C58.4 (one-vertex separator for a large zero-transfer star)

If `q>=4`, there is a vertex `z` of the actual positive contact graph `G_s` such that
every component of `G_s-z` contains at most one terminal of `V(T)`. Consequently

```math
\deg_{G_s}(z)\ge
\begin{cases}
q,&z\notin V(T),\\
q-1,&z\in V(T).
\end{cases}
\tag{C58.12}
```

No replacement star network is introduced: `z` is a vertex of the source positive
unit-contact graph.

## 6. Triangle-free geometry bounds every star to five diameter edges

### Lemma C58.5 (triangle-free unit-contact degree cap)

Every vertex of a triangle-free unit-contact graph in the plane has contact degree at
most five.

#### Proof

All unit neighbors of a vertex lie on its unit circle. Consecutive neighbors in angular
order must be at angular separation at least `pi/3`, because their mutual distance is
at least one. Six neighbors would force all six angular gaps to equal `pi/3`. Then
every consecutive pair of neighbors is itself at unit distance, forming a unit-contact
triangle with the center. `\square`

Since `G_s` is a subgraph of the triangle-free source unit-contact graph,

```math
\deg_{G_s}(z)\le5
\tag{C58.13}
```

for every vertex `z`.

Combining (C58.12)-(C58.13) gives:

### Theorem C58 (bounded zero-transfer star forest)

For every C56-Z selected normalized KKT stress in a triangle-free source,

```math
\boxed{
H_s\text{ is a star forest and every star has degree at most }5.
}
\tag{C58.14}
```

Equivalently, every positive-diameter component has at most six terminals.

If a component has six terminals, SEPq forces its separating vertex to be one of
those six terminals and to have positive-contact degree exactly five. A nonterminal
separator would require degree at least six and is impossible.

## 7. Interaction with the C57 null-face body mechanism

Let `s^a,s^b` be two extreme stresses of the C54 null face. C57 makes their positive
contact components rigid bodies for every strong-framework flex. If the bodies have
different angular rates, C57 proves their midpoint

```math
s^{ab}=\tfrac12(s^a+s^b)
```

is a C56-Z stress.

Applying C58 to that midpoint gives:

```math
\boxed{
\omega_a\ne\omega_b
\Longrightarrow
H_{s^a}\cup H_{s^b}
\text{ is a star forest with every star degree }\le5.
}
\tag{C58.15}
```

Every star with at least four terminals also has the source-preserving separator from
C58.4.

Thus relative motion of two null-face rigid bodies is compatible only with a bounded
collection of local diameter stars. It cannot be supported by a long zero-transfer
diameter chain, a non-star caterpillar, or a diameter cycle.

## 8. Exact remaining C-I target

C57-C58 reduce a surviving weak-contact obstruction to a body-pin mechanism with two
simultaneous properties:

1. every null-face extreme support is a full-diameter rigid body;
2. whenever two bodies rotate differently, their midpoint diameter support is a
   degree-at-most-five star forest, and each star of size at least four is separated in
   the actual contact graph by one vertex.

The shortest next theorem is now:

> **C59 bounded-star body-hinge exclusion.** Show that two full-diameter null-face
> bodies meeting at one source vertex cannot rotate differently when their midpoint
> diameter support has the C58 bounded-star/separator structure; or integrate that
> relative rotation to a finite same-diameter release.

A direct geometric route is available. If two rigid bodies meet only at a hinge `z`,
set one body stationary and rotate the other about `z`. Any cross-body strong active
pair has zero first radial variation. For a nonzero relative angular rate this forces
its two endpoints and `z` to be collinear. A strong cross-body diameter then shortens
to second order under either sign of the finite hinge rotation, while a strong
cross-body unit contact lengthens. The remaining issue is compatibility when three or
more null bodies form a closed one-vertex pin cycle.

## 9. Verification and regressions

- C58.1 is an exact basis calculation in the tree incidence matrix; no response
  approximation is used.
- C58.2 is the standard four-point characterization of a positive tree metric checked
  directly against the two Kalmanson inequalities.
- C58.3 uses only circularity of every tree-edge split and the canonical diameter
  thrackle property.
- The degree-five bound is global triangle-free unit-distance geometry and does not use
  the fully force-visible C-II degree caps.
- A six-terminal diameter star is not excluded: it can force a degree-five terminal
  separator. This is why the theorem states degree at most five rather than four.
- A matching is a star forest of degree one and remains compatible with C58; the
  theorem is structural, not yet the final C-I contradiction.

## 10. Compact handoff

**LEVEL I STATUS:** still open.

**C58.1:** on each connected component of a C56-Z diameter forest, the physical
contact effective resistance is exactly the weighted tree metric with edge lengths
`1/beta_e`.

**C58.2-C58.3:** Kalmanson order makes every tree-edge split circular; a diameter
thrackle tree with every edge split circular cannot contain two disjoint edges, hence
is a star.

**C58:** SEPq plus the triangle-free unit-contact degree-five cap gives at most six
terminals per star, i.e. diameter degree at most five. Every star with at least four
terminals has a source-preserving one-vertex separator.

**C57 consequence:** two null-face extreme bodies with different angular rates can
mix only through such a bounded star forest.

**Next:** exploit the separator/hinge geometry to integrate or exclude the remaining
body-pin mechanism.

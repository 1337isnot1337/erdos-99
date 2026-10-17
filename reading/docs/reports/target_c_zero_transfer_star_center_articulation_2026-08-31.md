> Generated reading edition · [exact source](../../../docs/reports/target_c_zero_transfer_star_center_articulation_2026-08-31.md) · source SHA-256 `fa6d228a5a043f53630db6eec150769e523a182fa32f453895afad7f98ed3a6d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7123EA251EFF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: zero-transfer star-center articulation

**Date:** 2026-08-31  
**Repository base:** `03ca247b` (main after C59 / PR #61)  
**Run type:** exact electrical equality / graph-separator refinement  
**Target:** Target C Gate C-I, collinear multi-body phase  
**Depends on:** C56 zero-transfer collapse, C58 zero-transfer star forest, C59 two-body hinge integration

## LEVEL I STATUS

**STILL OPEN.**

C58 proves that every connected positive-diameter component in the C56-Z phase is a
star of degree at most five. The exact star metric identifies a stronger separator
than SEPq: the **diameter-star center itself** is a cut vertex of the source positive
contact graph separating every two diameter leaves.

This follows from an equality characterization for the resistance triangle
inequality. It applies already to a two-leaf diameter star and gives the graph cut
needed by the remaining C59 collinear multi-body problem.

## 1. Equality in resistance distance

Let `G` be a finite connected graph with strictly positive conductances, Laplacian
`L`, and resistance distance

```math
R_{uv}=(e_u-e_v)^{\mathsf T}L^+(e_u-e_v).
\tag{C60.1}
```

### Lemma C60.1 (resistance equality is vertex separation)

For distinct vertices `a,b,c`,

```math
\boxed{R_{ab}=R_{ac}+R_{cb}}
\tag{C60.2}
```

if and only if deleting `c` puts `a` and `b` in different connected components.

#### Proof

Ground `c` and send one unit of current from `a` to `c`. Let `phi_c=0` be the
resulting voltage. Then

```math
L\phi=e_a-e_c,
\qquad
\phi_b=(e_b-e_c)^{\mathsf T}L^+(e_a-e_c).
\tag{C60.3}
```

Expanding the quadratic form for
`e_a-e_b=(e_a-e_c)-(e_b-e_c)` gives

```math
R_{ab}=R_{ac}+R_{bc}-2\phi_b.
\tag{C60.4}
```

On every component of `G-c` not containing `a`, `phi` is harmonic with zero boundary
value through `c`, so `phi=0`. On the component containing `a`, the strong discrete
maximum principle gives `phi>0`: `phi_a=R_ac>0`, and a zero at any other vertex would
force zero through its positive-conductance neighbors until reaching the positive
source. Hence

```math
\phi_b=0
\iff
a,b\text{ lie in different components of }G-c.
```

Together with (C60.4), this proves the claim. `\square`

The nonnegativity `phi_b>=0` also recovers the resistance triangle inequality.

## 2. The zero-transfer star center is the physical articulation

Fix a C56-Z stress. By C58, each positive-diameter component is a star. Let one such
component have center `o`, leaves `v_1,...,v_k`, and positive diameter weights
`beta_i=beta_{ov_i}`.

C58.1 gives

```math
R_{ov_i}=\frac1{\beta_i},
\qquad
R_{v_iv_j}=\frac1{\beta_i}+\frac1{\beta_j}.
\tag{C60.5}
```

Thus for every `i!=j`,

```math
R_{v_iv_j}=R_{v_io}+R_{ov_j}.
\tag{C60.6}
```

Apply Lemma C60.1 in the actual connected positive contact graph.

### Theorem C60 (star-center articulation)

For every C56-Z diameter-star component, deleting its diameter center `o` leaves at
most one diameter leaf in each positive-contact component. Consequently

```math
\boxed{
\deg_{G_s}(o)\ge k=\deg_{H_s[T]}(o).
}
\tag{C60.7}
```

In a triangle-free source, `deg_Gs(o)<=5`, hence `k<=5`.

If `k=5`, then the center has positive-contact degree exactly five and the five
diameter leaves lie in five different components of `G_s-o`.

This strengthens C58: the separator is not merely guaranteed to exist; it is the
specific loaded diameter-star center, and the statement works for `k=2,3` as well.

## 3. Interaction with null-body hinges

Let `P_a,P_b` be two extreme null bodies with different angular rates. C57 gives

```math
P_a\cap P_b=\{z\}.
```

The midpoint positive contact graph is exactly

```math
G_{ab}=G_a\cup G_b,
```

and this is already a graph one-sum at `z`: an edge crossing from
`P_a-{z}` to `P_b-{z}` could not belong to either extreme positive support.

If a C58 midpoint diameter star contains edges from both extreme stresses, its common
center belongs to both body vertex sets and therefore equals `z`. Theorem C60 then
identifies the same physical hinge `z` as the contact articulation separating all
leaves of that mixed star.

C59 proves that this two-body hinge integrates finitely. Therefore the remaining
separator problem begins only when a third null body supplies an alternate contact
route around a pairwise hinge.

## 4. Collinear three-body cycle refinement

C59 shows that three distinct rigid-motion classes `A,B,C` with pairwise distinct
hinges

```math
z_{AB},z_{BC},z_{CA}
```

can have nonconstant angular rates only if those three source points are collinear.

For such a triple, take any convex combination with positive coefficients of the
three null-face extreme stresses. It remains in the null face. Each extreme carries
at least one positive diameter edge. Distinct-motion bodies cannot share a positive
diameter edge, because they would then share its two endpoints and C57 would merge
their motions. Hence the mixed stress has at least three positive diameter edges and
a two-dimensional diameter endpoint hull. If the mixture were in C56-G, C56.5 would
force one angular rate on every positive diameter edge and hence on all three bodies.
Therefore every positive three-body mixture with nonconstant body rates lies in
C56-Z.

C58-C60 consequently apply to the **full three-body union**, not merely to its
pairwise midpoints:

```math
\boxed{
H_A\cup H_B\cup H_C
\text{ is a degree-}5\text{ star forest, and every nontrivial star center is a
contact articulation of }G_A\cup G_B\cup G_C.
}
\tag{C60.8}
```

This is the exact graph structure that any collinear pin cycle must satisfy.

## 5. Remaining target

A three-body cycle with distinct hinges contains three internally vertex-disjoint
positive-contact routes between the collinear hinge points: one inside each rigid
body. Equation (C60.8) says every loaded star center must nevertheless separate all
of its diameter leaves in that cyclic union.

The next theorem should exploit this conflict:

> **C61 collinear-cycle exclusion.** In a connected positive equilibrium network that
> is the union of three pairwise one-vertex null bodies with distinct collinear hinges,
> the C60 star-center articulation structure for every positive three-body mixture is
> incompatible with all three bodies carrying positive diameter reaction, unless the
> three angular rates are equal.

A proof closes the covered three-body branch of Gate C-I. The independent C59
null-face coverage issue would then remain.

## 6. Binding cautions

- A one-edge diameter component has no pair of leaves, so C60 gives no new articulation
  beyond ordinary connectivity; matching components remain the weakest zero-transfer
  case.
- C60.8 does not by itself force one star component to contain diameter edges from all
  three bodies.
- The positive-contact articulation is for the mixed stress support, not automatically
  for the entire maximal strong contact graph.
- Multi-body finite compatibility and null-face active-vertex coverage remain open.

## 7. Compact handoff

**LEVEL I STATUS:** still open.

**C60.1:** `R_ab=R_ac+R_cb` in a positive network iff `c` separates `a` and `b`; proof
uses the grounded unit-current voltage and the strong maximum principle.

**C60:** every C56-Z diameter-star center is therefore the actual positive-contact
articulation separating its leaves. Its diameter degree is at most five directly.

**Three-body consequence:** any positive mixture of three differently rotating null
bodies is itself C56-Z, so the complete three-body diameter union is a bounded star
forest with the C60 articulation property. Combined with C59, its three distinct hinge
vertices are collinear.

**Next:** exclude that collinear three-body contact cycle, then address null-face
coverage.

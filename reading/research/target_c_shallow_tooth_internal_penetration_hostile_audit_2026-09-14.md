> Generated reading edition · [exact source](../../research/target_c_shallow_tooth_internal_penetration_hostile_audit_2026-09-14.md) · source SHA-256 `e002a981b344b74fb01082d0eb702d316d0de684a23c1a593284e14e80c91b38`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "cec2c4b65c94f631d76e4b12d3f74577fc09f7e7", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_shallow_tooth_internal_penetration_hostile_audit_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "ac3bac9c74a05ef629d6f098e06127b40fe014fb8d3e6f1075bf36ca75ecf1eb"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — shallow-tooth internal penetration theorem

**Date:** 2026-09-14  
**Reviewed:** `research/target_c_shallow_tooth_internal_penetration_2026-09-14.md`  
**Disposition:** **PASS as a proof-only Type-II consequence.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit checks the places where the factor-four improvement could fail: local
flatness, loaded-neighbor exclusion, component membership, edge multiplicity, and the
low-`t` arithmetic composition.

## 1. Fixed-scale flatness does follow from Section 124

Section 124 uses the Type-II disk sandwich

```math
B(0,r_D)\subset F_D\subset B(0,R_{+,D}),
\qquad r_D/R_{+,D}\to1,
```

and proves that on a loaded-hull boundary arc whose endpoints are a fixed Euclidean
distance apart, all side directions lie in an angular window tending uniformly to
zero.  Replacing the unit chord in its displayed estimate by a fixed bound `L` changes
only

```math
2\arcsin(1/(2r_D))
\quad\text{to}\quad
2\arcsin(L/(2r_D)),
```

which is still `o(1)`.  Projection along the midpoint direction of the tangent window
bounds the corresponding short boundary arclength by `L/cos(o(1))=O_L(1)`.  The
transverse displacement across that arc is therefore `o(1)`.

Hence Lemma IP.1 is a legitimate finite-scale consequence of the already-audited
near-disk geometry; it does not assume `d_H(F_D,B)=o(1)` in absolute units.

## 2. The third loaded-neighbor exclusion is uniform even as the base approaches one

For a tooth base of length `s`, write `u=s/2`.  Since the base is nonunit,

```math
1/2<u\le1.
```

A loaded contact neighbor `c=(X,z)` of the apex satisfies `z=o(1)` by Lemma IP.1 and

```math
X^2=u^2+o(1).
```

The lower bound `u>=1/2` makes the square-root step uniform: `|X|=u+o(1)` even if
`s-1` tends to zero.  Thus `c` lies `o(1)` from one of the two base endpoints.  Source
unit separation excludes a distinct such loaded point for all sufficiently large
`D`.

No angular cluster count, distinctness convention, or lower bound on `s-1` is hidden in
this step.

## 3. The mandatory extra neighbor is internal before trapping is used

The tooth apex is an unloaded positive-contact vertex with two known unit contacts to
the loaded base endpoints.  Canonical C26 gives contact degree at least three, so an
extra contact neighbor exists.  Lemma IP.2 proves that this neighbor is not loaded.
Therefore the extra contact joins two unloaded vertices and, by definition, lies
inside one unloaded positive-contact component.

Only after that conclusion is harmonic trapping used to place the extra endpoint in
the force hull.  There is no circular use of trapping to prove that the endpoint is
unloaded.

## 4. The depth inequality keeps the correct orientation

For an `eta`-shallow tooth,

```math
a=(-\cos\alpha,0),\quad b=(\cos\alpha,0),\quad
x=(0,\sin\alpha),
```

with the force-hull interior on the positive-normal side of the base.  The extra
unloaded endpoint lies in the same trapped component and therefore in the force hull.
The triangle-free inequalities against both loaded endpoints give the same positive
inward component as in the previously committed shallow-tooth theorem:

```math
Y>\sin(\pi/3-\alpha).
```

Thus the endpoint depth is

```math
\sin\alpha+Y>
\sin\alpha+\sin(\pi/3-\alpha).
```

For `alpha<pi/6` this last function is increasing, so its infimum on the allowed
interval is `sqrt(3)/2`.  The sign is not reversible: the component endpoint is on the
inward side by harmonic trapping.

## 5. Edge injectivity does not confuse physical edges with occurrences

Two different selected shallow apexes can select the same undirected physical contact
edge only if they are the two endpoints of that edge.  Lemma IP.3 rules this out:
if the inner endpoint were another shallow apex, its second shallow base would lie in
the same fixed-scale loaded-hull neighborhood, so the two support lines would differ
by `o(1)`.  The endpoint would then have depth simultaneously

```math
>{\sqrt3\over2}-o(1)
```

and

```math
<\sin(\pi/12),
```

an absolute contradiction.

This is physical-edge injectivity.  It does not count outer-walk repetitions or train
terminal occurrences as new edges.

## 6. Numerical composition

The current low-`t` proof-only endpoint gives

```math
R(t_{42})=0.00576795,
\qquad
\delta={d_{out}\over D}\le0.002883975+o(1).
```

The exact tooth/long-side dichotomy gives, on its tooth branch,

```math
{N_2\over D}\ge0.4363893718701161\ldots-o(1).
```

For `eta=0.06`, the metric Markov estimate therefore gives

```math
{N_{sh}\over D}
\ge0.4363893718701161\ldots
-{0.002883975\over0.06}-o(1)
=0.3883231218701161\ldots-o(1).
```

The verifier independently checks

```math
0.06<2(1-\cos(\pi/12)),
```

```math
Y_{0.06}=0.7184921838594732\ldots,
```

and the product

```math
0.3883231218701161\ldots\,Y_{0.06}
=0.27900712787558\ldots .
```

The arithmetic matches the theorem statement.

## 7. Scope and non-conclusions

The theorem is Type II.  It uses the near-disk loaded-hull geometry and therefore does
not address the macroscopic-container branch.

It does not prove that the selected internal edges have KKT weights bounded below.
Indeed a nearly flat tooth can make the inward-edge equilibrium weight small.  The
improvement is deliberately unweighted.

It also does not by itself force Eppstein slack, pinned stress surplus, or a diameter
reduction: a component may absorb many internal penetration edges while carrying many
additional vertices and contacts.  A further componentwise/global theorem is still
needed.

**Final verdict:** the factor-four counting improvement and the internal-edge
classification pass hostile audit at proof-only Type-II scope.  No theorem-state
promotion is justified yet.

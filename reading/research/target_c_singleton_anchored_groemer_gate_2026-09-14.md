> Generated reading edition · [exact source](../../research/target_c_singleton_anchored_groemer_gate_2026-09-14.md) · source SHA-256 `839f3f510792d1bf75daf83199c2455fa290b3cd374d5debec0311a16bbb5683`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "72d0bc65e667a77780b531251bc29a3d630c0224", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_singleton_anchored_groemer_gate_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "e61653b9090fa5b305e5ab2f171ea60619a48471b92627525b603d6f4a3a6755"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — singleton-anchored Groemer gate

**Date:** 2026-09-14  
**Target:** C-II, canonical full-core Type-II branch  
**Dependencies:** detour-free exceptional-train gate; all-degree Groemer hostile audit; exact force-hull residual conservation  
**Claim class:** proof-only closing reduction awaiting independent audit

## LEVEL I STATUS

`STILL OPEN`

The detour-free train gate proves

```math
\boxed{
 {\sigma_R+2S_E\over D}
 \ge
 c_{DF}+{5\over2}{k\over D}+{Q-f\over D}-o(1),
}
\tag{SG.1}
```

where

```math
c_{DF}=\sqrt{\Delta_2}-{\pi\over4}+0.00105
=0.167964643466509\ldots .
\tag{SG.2}
```

Here `S_E` counts singleton stopped trains with a terminal incidence on a bounded exceptional face.

The Groemer hostile audit proves that small true face residual forces an anchored almost-equilateral triangle on a boundary contact edge. Its proof is actually **edgewise**: every fixed boundary contact edge of a low-residual bounded-degree face has such a near apex. On the branch `R_F=o(D)`, this lets us replace pentagonal singleton trains by source-level anchored almost-triangles whose exact base is the singleton edge itself.

The resulting gate is

```math
\boxed{
\sigma_R+11(Q-f)+130A^{sing}_\eta
\ge
c_{DF}D+{5\over2}k-o(D)
}
\tag{SG.3}
```

for every fixed `eta>0`, where `A^{sing}_eta` is the maximum number of pairwise vertex-disjoint triples `(u,v,w)` satisfying

```math
|u-v|=1,
\qquad
1\le|u-w|<1+\eta,
\qquad
1\le|v-w|<1+\eta,
\tag{SG.4}
```

with `uv` a singleton stopped-train edge incident with a pentagonal exceptional face.

Thus, on the small-residual branch, the exceptional-singleton escape becomes an actual macroscopic family of almost unit triangles, not merely train incidence.

## 1. Edgewise Groemer anchoring

### Lemma SG.1 — every low-residual boundary edge gets a near apex

Fix `K>=5` and `eta>0`. There exists `tau_K^edge(eta)>0` such that if a canonical bounded exceptional face `P` has degree at most `K` and residual

```math
r(P)<\tau_K^{edge}(\eta),
```

then **every** cyclic boundary edge `uv` of `P` has a source point `w` in the face with

```math
1\le|u-w|<1+\eta,
\qquad
1\le|v-w|<1+\eta.
\tag{SG.5}
```

Because the global source is triangle-free, at least one of these two inequalities is strict.

#### Proof

If false, there is a sequence of degree-at-most-`K` exceptional faces with residual tending to zero and a marked cyclic boundary edge `u_jv_j` for which no such `w_j` exists. Pass to a subsequence with fixed degree, fixed assigned-isolate count, and fixed index of the marked boundary edge. Normalize the marked edge to `(0,0)(1,0)` and take the same compactness limit as in the all-degree Groemer theorem.

The limit cannot be the segment equality case, so it is a Groemer packing triangulated by unit equilateral triangles. The marked length-one segment `uv` remains on the convex-hull boundary. No third unit-separated source point can lie in its relative interior, so `uv` is a boundary edge of the triangulation. Every triangulation boundary edge is incident with exactly one triangular cell; Groemer equality makes that cell unit equilateral. Its third vertex `w` satisfies

```math
|u-w|=|v-w|=1.
```

The corresponding labeled source point in the approximating sequence then satisfies (SG.5) for all sufficiently large indices, contradiction.

Since there are only finitely many marked edge indices for `d<=K`, the threshold can be chosen uniformly over all cyclic boundary edges. `square`

## 2. Apply the edgewise lemma to pentagonal singleton incidences

Let `S_5` be the number of singleton stopped trains with at least one pentagonal terminal incidence, as in the exceptional-singleton two-window theorem.

Let `p_5^{hit}` be the number of pentagonal exceptional faces incident with at least one such singleton train. A pentagon has only five boundary edges, so

```math
\boxed{p_5^{hit}\ge S_5/5.}
\tag{SG.6}
```

Assume now

```math
R_F=o(D).
\tag{SG.7}
```

For fixed `eta>0`, Lemma SG.1 with `K=5` gives a positive threshold `tau_5^edge(eta)`. Because pentagon residuals are nonnegative and sum to at most `R_F`, the number of pentagons with residual at least this threshold is `o(D)`.

Hence at least

```math
{S_5\over5}-o(D)
\tag{SG.8}
```

singleton-hit pentagons are low-residual. In each such pentagon choose one incident singleton edge `uv`; Lemma SG.1 supplies a third source point `w` satisfying (SG.4). Thus the exact base `uv` is itself the singleton stopped train that entered the train ledger.

## 3. Extract vertex-disjoint singleton-anchored triples

Choose only one anchored triple per pentagon in (SG.8). As in the dense anchored-triangle refinement, at most five chosen face-triples can contain one boundary source vertex, while an interior assigned isolate belongs to only one chamber. Therefore the conflict graph of the chosen triples has maximum degree at most 12.

A greedy independent set keeps at least one thirteenth of them. Consequently

```math
\boxed{
A^{sing}_\eta
\ge {S_5\over65}-o(D).
}
\tag{SG.9}
```

Equivalently,

```math
\boxed{130A^{sing}_\eta\ge2S_5-o(D).}
\tag{SG.10}
```

## 4. Eliminate the exceptional-singleton currency

Put

```math
X:=Q-f\ge0.
```

The exact exceptional-face incidence theorem gives

```math
S_E\le S_5+6X,
```

hence

```math
2S_5\ge2S_E-12X.
\tag{SG.11}
```

From the detour-free gate (SG.1),

```math
\sigma_R+2S_E
\ge
c_{DF}D+{5\over2}k+X-o(D).
```

Subtract `12X` through (SG.11):

```math
2S_5
\ge
c_{DF}D+{5\over2}k-\sigma_R-11X-o(D).
\tag{SG.12}
```

Finally use (SG.10). Rearranging gives exactly

```math
\boxed{
\sigma_R+11(Q-f)+130A^{sing}_\eta
\ge
c_{DF}D+{5\over2}k-o(D).
}
\tag{SG.13}
```

No outer-detour term survives.

## 5. Consequences

Ignoring the nonnegative topology bonus, for every fixed `eta>0` and every Type-II subsequence with `R_F=o(D)`, at least one of

```math
{\sigma_R\over D},
\qquad
{Q-f\over D},
\qquad
{A^{sing}_\eta\over D}
```

is at least

```math
{c_{DF}\over142}-o(1)
=0.001182849601876\ldots-o(1),
\tag{SG.14}
```

because the coefficients in (SG.13) sum to `1+11+130=142`.

More usefully, if

```math
\sigma_R=o(D),
\qquad
Q-f=o(D),
\tag{SG.15}
```

then

```math
\boxed{
\liminf {A^{sing}_\eta\over D}
\ge {c_{DF}\over130}
=0.001292035718973\ldots .
}
\tag{SG.16}
```

This holds for every fixed `eta>0`. A standard diagonal choice of `eta_j=1/j` gives a scale `eta_D->0` with the same limiting coefficient:

```math
\boxed{
\liminf {A^{sing}_{\eta_D}\over D}
\ge {c_{DF}\over130}
}
\tag{SG.17}
```

under (SG.15).

Thus the low-rhombic-slack / low-high-degree-excess corner of the small-residual branch contains a linear family of pairwise vertex-disjoint almost-equilateral triangles whose exact base edges are **singleton stopped trains**.

## 6. Why singleton anchoring matters

The dense Groemer theorem already gives more anchored almost-triangles numerically. Equation (SG.13) is different: it identifies a subfamily whose exact base contact is a specific train-defect edge. These bases do not cross any strict rhombus and terminate directly on pentagonal defect faces.

This couples the metric near-contact obstruction to the same stopped-train decomposition that controls `sigma_R`. A future deformation theorem can therefore distinguish:

- a large rhombic Mantel deficit;
- high-degree exceptional-face excess; or
- a linear family of local almost-triangles attached to singleton train edges.

The outer-walk detour escape has already been eliminated.

## 7. Scope audit

- The theorem is conditional on the small true force-hull residual branch `R_F=o(D)`.
- The edgewise Groemer lemma uses the same external equality classification already independently audited; no new literature input is added.
- One triple is selected per singleton-hit pentagon before the degree-12 conflict bound is applied.
- `A^sing_eta` counts actual source triples. The third point may be contact-isolated or another boundary/core point.
- No KKT multiplier is assigned to the near sides; they remain inactive inequalities.
- No exact unit triangle or strict sub-`D` competitor is claimed.

C-II and Level I remain open.

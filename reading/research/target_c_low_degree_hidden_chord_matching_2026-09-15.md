> Generated reading edition · [exact source](../../research/target_c_low_degree_hidden_chord_matching_2026-09-15.md) · source SHA-256 `0be329385a2dc38ebaa72a8b54963261e39c8c34b0b6218c7365ec79a223eb7a`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 6 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "caeadf1893272cd921996fc940d3c61ecb67a9be", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_low_degree_hidden_chord_matching_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "7c7c459d03d0fddadab6962f57cf2e886ebd83233846feba0de52c6b67e6f845"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — the low-degree face sea forces a linear matching of short hidden chords

**Date:** 2026-09-15
**Status:** proof-only source-level structural strengthening
**Scope:** canonical triangle-free full-core Type-II branch, using the degree-5/6 row of the low-degree face staircase
**Dependencies:** `target_c_low_degree_face_staircase_2026-09-15.md`; canonical convexity of bounded exceptional contact faces; triangle-freeness
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The low-degree staircase gives a linear population of source-empty pentagonal/hexagonal contact faces through `t<=2.1854`. No small Oler residual is needed to extract a useful hidden-pair population from these faces.

### Theorem HC

Let `F_{<=6}` be the number of bounded exceptional faces of degree five or six. There is a family `M` of pairwise vertex-disjoint source pairs such that

```math
\boxed{|M|\ge {F_{\le6}\over9},}
\tag{HC.1}
```

and every `{x,y} in M` satisfies

```math
\boxed{1<|x-y|\le\sqrt3.}
\tag{HC.2}
```

If the selected pair comes from a pentagon, the sharper bound is

```math
|x-y|\le2\cos(\pi/5)={1+\sqrt5\over2}.
\tag{HC.3}
```

Consequently the certified staircase row at `t<=2.10` gives

```math
\boxed{|M|>0.0130D-o(D).}
\tag{HC.4}
```

At `t<=2.18` it still gives `|M|>0.00083D-o(D)`.

## 1. One short hidden diagonal in every convex unit 5/6-face

Let `P=(v_1,...,v_m)`, `m in {5,6}`, be a bounded exceptional contact face in cyclic order. Canonical face convexity gives a strict convex equilateral unit polygon.

Let `alpha_i in (0,pi)` be the exterior turn from edge `v_iv_{i+1}` to `v_{i+1}v_{i+2}`. Then

```math
\sum_{i=1}^m\alpha_i=2\pi.
```

Hence some `alpha_i>=2pi/m`. The corresponding two-edge diagonal obeys

```math
\begin{aligned}
|v_i-v_{i+2}|
&=| (v_{i+1}-v_i)+(v_{i+2}-v_{i+1}) |\\
&=2\cos(\alpha_i/2)\\
&\le2\cos(\pi/m).
\end{aligned}
\tag{HC.5}
```

For `m=5` this is the golden ratio; for `m=6` it is `sqrt(3)`.

The pair `v_i,v_{i+2}` is nonconsecutive on the face boundary. It cannot have distance exactly one: a unit nonboundary chord is an actual contact chord and would split the displayed canonical face. Unit separation gives the opposite inequality. Thus

```math
1<|v_i-v_{i+2}|\le2\cos(\pi/m).
\tag{HC.6}
```

Choose one such pair from every 5/6-face.

## 2. The selected-pair multigraph has maximum degree at most five

Create a multigraph `J` on source vertices with one selected hidden pair for each 5/6-face. A source vertex can be an endpoint of a selected pair only for a bounded face incident to that vertex.

In the triangle-free unit contact graph, contact degree is at most five: two unit neighbors of one vertex have angular separation strictly greater than `pi/3`, since equality would make a unit equilateral triangle. A planar vertex of contact degree `d` has at most `d` bounded face incidences. Therefore

```math
\boxed{\Delta(J)\le5.}
\tag{HC.7}
```

This counts multiplicity and is safe even if one source pair were selected by more than one face.

## 3. Greedy matching extraction

Take a maximal matching `M` in `J`. Every selected edge of `J` is either in `M` or shares an endpoint with an edge of `M`. One matching edge with endpoints `x,y` can account for at most

```math
\deg_J(x)+\deg_J(y)-1\le9
```

edges of `J`. Since `J` has exactly `F_{<=6}` edges counting multiplicity,

```math
F_{\le6}\le9|M|,
```

which proves (HC.1). Every matching edge inherits (HC.2).

## 4. Numerical rows

The exact low-degree staircase certificate gives

```math
F_{\le6}/D>0.1175\qquad(t\le2.10),
```

and

```math
F_{\le6}/D>0.0075\qquad(t\le2.18).
```

Dividing by nine gives the safe rounded matching floors in (HC.4) and its `2.18` counterpart.

All degree-5/6 faces in this range are source-empty by the isolate-host theorem, so every selected hidden pair lies across an empty bounded contact chamber. The present theorem does not claim that reflecting or contracting the pair is automatically feasible: external source points and active diameter constraints can still block a local move.

The new normal form is instead

```text
t <= 2.10:
  >0.1175 D source-empty 5/6-faces
  -> >0.0130 D vertex-disjoint inactive hidden pairs
  -> each hidden distance lies in (1,sqrt(3)].
```

A closing theorem can now attack these pairs simultaneously using protected face-local exchange, KKT/diameter incidence, or a residual-to-near-contact refinement.

**Disposition:** proved a linear vertex-disjoint short-hidden-pair matching from the modern low-degree face sea. C-II and Level I remain open.

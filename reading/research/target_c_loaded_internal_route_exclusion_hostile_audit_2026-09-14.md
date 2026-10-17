> Generated reading edition · [exact source](../../research/target_c_loaded_internal_route_exclusion_hostile_audit_2026-09-14.md) · source SHA-256 `8cad2760e98365b259575dc8a122065c31bbd3cf92c1ba06517752c334f69e4b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "d2434e9977ee3c725abadbceac8bc01e52d3a4a4", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_loaded_internal_route_exclusion_hostile_audit_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "af0469eac7c6edc753e9b3efec1dff807c19e1c51de73f4946e3f6e450671008"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — loaded internal outer-route exclusion

**Date:** 2026-09-14  
**Reviewed:** `research/target_c_loaded_internal_route_exclusion_2026-09-14.md`  
**Disposition:** **PASS at proof-only fully force-visible C-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The only nontrivial dependency not already in the current promoted stack is the
proof-only loaded non-articulation theorem.  This audit rechecks the part of that
argument needed here rather than treating the report title as an axiom.

## 1. Repeated facial occurrence really forces articulation

For a connected loopless plane graph, a non-articulation vertex belongs to exactly one
block.  A nontrivial block is 2-connected, so each of its facial boundaries is a
simple cycle; a bridge leaf contributes its non-articulation endpoint only once to the
global facial walk.  Multiple entries into distinct incident blocks can occur only at
a cut vertex.

Therefore if a physical vertex occurs twice on one global face-boundary walk, that
vertex is an articulation vertex.  This remains true when other vertices or bridge
edges repeat.

**Verdict:** PASS.

## 2. The Section-63 partition leaves no distinguished loaded mark inside an interval

The hostile audit of Section 126 explicitly states that canonical Section 63 chooses
one distinguished exterior occurrence of **every** loaded force-hull vertex in cyclic
order and partitions one full outer-face boundary walk into consecutive intervals

```math
W_i:b_i\leadsto b_{i+1}.
```

Hence an internal occurrence of a loaded physical vertex cannot be its distinguished
occurrence.  The same physical vertex has at least two occurrences on the outer-face
walk and is therefore an articulation by the preceding graph lemma.

This includes a repeated occurrence of one of the interval endpoints itself.

**Verdict:** PASS.

## 3. Targeted re-audit of loaded non-articulation

Let `z` be positively diameter-loaded in the fully force-visible contact core `G`.
Translate `z` to the origin.  Since `z` is an extreme source-hull vertex, choose a
linear functional `ell` such that

```math
f_i:=\ell(p_i)>0
```

for every other core vertex.

For the actual selected-stress matrix

```math
\Omega=L_C(\alpha)-L_H(\beta)\succeq0,
\qquad
\Omega P_x=\Omega P_y=0,
```

let `M` be the principal matrix obtained by deleting the row and column of `z`.
Because `p_z=0`, both coordinate columns remain in `ker M`, hence so does `f`.

Suppose `G-z` has contact components `V_1,...,V_k`.  Put arbitrary constants `a_r` on
the components and set `w_i=a_r f_i` for `i in V_r`.  The matrix

```math
N=\operatorname{diag}(f)M\operatorname{diag}(f)
```

is PSD and has zero row sums.  Its quadratic-form identity is

```math
a^TNa
=-\sum_{i<j}N_{ij}(a_{r(i)}-a_{r(j)})^2.
```

There are no contact edges between distinct `V_r`; a positive diameter edge across
two components has `M_{ij}=+\beta_{ij}` and therefore contributes a strictly negative
term.  PSD forces every such cross-component diameter coefficient to vanish.  Relative
interior positivity of the selected support means there is no positive diameter edge
between different components.

Now fix one component `V_r` and suppose it contains no internal positive diameter
edge.  Its grounded principal block is PSD, has nonpositive off-diagonal entries, and
its strictly negative off-diagonal graph is the connected contact graph on `V_r`.
The coordinate columns lie in its kernel.  The elementary irreducible grounded
M-matrix lemma therefore gives kernel dimension at most one, so the points of `V_r`
lie on one line through `z`.  The positive exposing vector `f` puts them all on one
ray.

A connected unit-contact set on one ray is a consecutive unit chain.  If it has at
least two vertices, its first vertex lies strictly between `z` and the next vertex and
has full contact degree two.  It is not a diameter endpoint, contradicting C26/contact
minimality.  If it has only one vertex, that vertex is a contact leaf and has no
possible positive diameter partner: cross-component and internal positive diameters
were excluded, while its distance to `z` is one and `D>1`.  This again contradicts
positive-contact equilibrium/C26.  Thus every component contains an internal positive
diameter edge.

If there were two components, choose one internal positive diameter edge in each.
Their four endpoints are distinct extreme hull vertices.  Two vertex-disjoint diameter
chords have alternating hull endpoints.  Connectivity inside the two contact
components supplies two vertex-disjoint contact paths joining the respective
alternating endpoint pairs.  Such two curves in the convex hull disk must intersect,
contradicting planarity of the unit-contact graph.

Hence `G-z` is connected.

No lexicographic minimum of the actual diameter-edge count is used in this argument;
that stronger hypothesis enters only the separate general separator theorem in the
2026-09-11 report.

**Verdict:** PASS for the loaded non-articulation statement used by RI.3.

## 4. Consequence for straight events

An internal Section-63 route vertex is therefore unloaded.  C26 makes its full contact
degree at least three, so the degree-two straight-event population is exactly zero.
The current main inequality

```math
2V_2(\beta)+10E_\perp(\beta)\ge S_\beta
```

reduces to

```math
10E_\perp(\beta)\ge S_\beta.
```

At `beta=pi/6`, main's certified

```math
S_{\pi/6}/D\ge0.3933368069590823665\ldots-o(1)
```

gives

```math
E_\perp(\pi/6)/D
\ge0.03933368069590823665\ldots-o(1).
```

The factor-ten loss remains legitimate: a triangle-free contact vertex has degree at
most five, so it supports at most five outer-face occurrences, and one selected extra
edge can be selected at both endpoints.

**Verdict:** PASS.

## 5. Scope

This audit certifies only a proof-only composition.  It does not promote the
2026-09-11 loaded non-articulation report into canonical theorem state.  No individual
stress-weight lower bound or diameter-decreasing motion follows.

**Final verdict:** PASS at proof-only full-core C-II scope.  The loaded degree-two
straight-event branch is spurious once the existing PSD non-articulation theorem is
composed with the actual Section-63 occurrence partition.

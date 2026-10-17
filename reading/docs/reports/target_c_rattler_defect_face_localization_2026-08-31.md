> Generated reading edition · [exact source](../../../docs/reports/target_c_rattler_defect_face_localization_2026-08-31.md) · source SHA-256 `0679ea2fb715f6e9a3a05d190b32cda3bc497c7f1b47c6efa24932f18fb84095`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C665926733F5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C49: KKT-invisible points are confined to O(D)-boundary defect faces

**Date:** 2026-08-31  
**Target:** C-II / force-bulk gap  
**Depends on:** canonical C30 pinned-rank boundary count, C35 loaded degree, planar Euler counting, triangle-free unit-rhombus geometry  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

Let `G=C` be the connected nonisolated fully force-visible contact core, with

- `m=|V(G)|`;
- `e=|E(G)|`;
- `q=|B_+|`;
- outer-face boundary-walk length `B`; and
- bounded face lengths `k_f>=4`.

Define the quadrangulation defect

`Q=sum_{f bounded}(k_f-4)`.

Then pinned rank and Euler give the exact budget

`B+Q <= 4q-4 <= 4pi D-4`.

Moreover every bounded quadrilateral contact face is a strict unit rhombus and contains no additional source point. Hence every source point outside the nonisolated contact core is contact-isolated and lies either

1. in the outer face of the contact core; or
2. in a bounded nonquadrilateral defect face.

The number of bounded defect faces is at most `Q`, and their total boundary length is at most `5Q`. Thus all bounded rattler cavities together have only `O(D)` contact-boundary complexity.

---

## 1. Exact face-defect identity

For a connected plane graph, Euler gives

`f_b = e-m+1`,

where `f_b` is the number of bounded faces. Summing face boundary-walk lengths counts every edge twice except that the outer walk contributes separately:

`2e = B + sum_{f bounded} k_f`.

Therefore

`Q=sum(k_f-4)
 = 2e-B-4f_b
 = 4m-2e-B-4`.

Canonical C30 pinned rigidity gives

`e >= 2(m-q)`.

Substitute:

`Q <= 4q-B-4`.

Hence:

### Theorem C49.1 — exact contact-face defect budget

`B+Q <= 4q-4`.

Since every force-hull side has length at least one and `per(F)<=pi D`, canonical C30 also has `q<=pi D`, so

`B+Q <=4pi D-4`.

This recovers the linear quadrangulation-defect scale in a form tailored to the force-bulk problem.

---

## 2. Defect-face count and total boundary length

Every bounded nonquadrilateral face has `k_f>=5`, so contributes at least one to `Q`. Thus

`N_def <= Q`.

For such a face,

`k_f = 4+(k_f-4)`.

Summing only over defect faces,

`L_def:=sum_{f non4} k_f
 <=4N_def+Q
 <=5Q`.

Therefore:

### Corollary C49.2

`N_def <=Q=O(D)` and `L_def<=5Q=O(D)`.

More explicitly, `L_def<=5(4q-B-4)<20q`.

---

## 3. A strict unit rhombus face has covering radius below one

Let `R` be a bounded quadrilateral contact face. Its four sides are unit contacts, so it is a Euclidean rhombus. Triangle-freeness and unit separation force its angles strictly between `60` and `120` degrees, as in C48.

Split the rhombus along a diagonal into two congruent triangles with two unit sides and included angle `theta<120` degrees. The circumradius of such a triangle is

`1/(2 cos(theta/2)) < 1`.

The nearest-vertex covering radius of a triangle is at most its circumradius (for an obtuse triangle the maximum occurs on an edge and is smaller). Hence every point of each half-triangle is at distance strictly less than one from at least one of its three vertices.

Therefore every point of the rhombus is at distance `<1` from at least one rhombus vertex.

### Lemma C49.3 — rhombus-face exclusion

No additional unit-separated source point can lie in the closed region of a bounded quadrilateral contact face, except its four boundary vertices.

A point in the relative interior of a unit boundary edge is also impossible by unit separation, so no boundary exception occurs.

---

## 4. All noncore points are localized to defect faces or the outer face

By definition of the nonisolated contact core, every source point not in `V(G)` is contact-isolated. Such a point is not on a contact edge and therefore lies in one face of the plane embedding of `G`.

C49.3 excludes every bounded quadrilateral face. Consequently:

### Theorem C49 — rattler defect-face localization

Every contact-isolated source point lies either

- in the outer face of the force-visible contact core; or
- in one of the `N_def<=Q=O(D)` bounded nonquadrilateral faces.

The total contact-boundary length of all bounded faces capable of containing such points is at most `L_def<=5Q=O(D)`.

Thus KKT-invisible points cannot be distributed through the `m-O(D)` strict-rhombus bulk supplied by C42.

---

## 5. Force-bulk interpretation

C48 identified `n-m` as the exact remaining source-capacity obstruction. C49 narrows its geometry:

```text
force-visible core:
    m vertices
    m-O(D) strict unit-rhombus faces
    O(D) total outer/defect boundary complexity

all n-m KKT-invisible source points:
    outer-face rattlers
    + rattlers inside O(D) bounded defect faces
    no rattlers inside any quadrilateral face
```

Hence any sequence with `n-m=Theta(D^2)` must concentrate a macroscopic packing population into the outer-face region and/or into a small number of geometrically large defect cavities.

This is a stronger target than an arbitrary force-free population.

## Regression audit

- Large regular-shell examples can have a large outer-face interior packing; C49 deliberately leaves that phase alive.
- One bounded defect face may have perimeter `Theta(D)` and contain `Theta(D^2)` points; C49 localizes but does not yet exclude this giant-cavity regression.
- The rhombus covering argument uses strict triangle-freeness; at exactly `60/120` degrees a diagonal is unit and the forbidden unit triangle appears.

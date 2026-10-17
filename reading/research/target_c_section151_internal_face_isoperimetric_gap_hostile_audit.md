> Generated reading edition · [exact source](../../research/target_c_section151_internal_face_isoperimetric_gap_hostile_audit.md) · source SHA-256 `e090ba22017126ae06f0d825a05a4e0d948608ec1f6100d1231e91134b58024f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "3a4c3a22814a96336e6f05fda1d918ca77e1fa8d", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_section151_internal_face_isoperimetric_gap_hostile_audit.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "4f54f85a8361a0334a9ceae95d901b95b9146bbf04d4b2b0b4a818315ff3cc60"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — Target C Section 151 internal-face isoperimetric endpoint exclusion

**Date:** 2026-09-12  
**Reviewed:** `research/target_c_section151_internal_face_isoperimetric_gap.md`  
**Disposition:** **PASS at proof-only endpoint scope. C-II remains open.**

---

## 1. Euler identity and Eppstein slack

For the connected internal plane graph `C[I_r]`, write `n,e,L,Q` for vertex count, edge count, occurrence-counted outer-face length, and bounded-face excess over four. Triangle-freeness gives bounded face degree at least four.

Euler and face incidence give

```math
e=2n-2-{L+Q\over2}.
```

Canonical Section 62 defines

```math
r=2n-\delta-2-e.
```

Therefore exactly

```math
\boxed{r={L+Q\over2}-\delta.}
```

Since `Q>=0`,

```math
L\le2(\delta+r).
```

No equality/stability property of Eppstein's inductive proof is imported.

**Verdict:** PASS.

---

## 2. Bounded-face area versus occurrence-counted outer walk

The candidate allows bridges and articulation vertices. This is important because the outer facial walk need not be a simple polygon.

Delete all bridges that are incident to the unbounded face on both sides and decompose the remaining positive-area bounded-face union into its finitely many connected planar regions `U_j`. Distinct `U_j` can meet only on sets of area zero. Let `p_j` be the Euclidean perimeter of `U_j`.

Every perimeter edge of every `U_j` is a unit graph edge with the unbounded face on the other side, and hence contributes an occurrence to the original outer-face walk. An edge occurring twice on the outer walk can only make the occurrence budget larger. Thus

```math
\sum_jp_j\le L.
```

Apply ordinary planar isoperimetry to each `U_j`:

```math
\operatorname{area}(U_j)\le p_j^2/(4\pi).
```

Then

```math
\sum_j\operatorname{area}(U_j)
\le {1\over4\pi}\sum_jp_j^2
\le {1\over4\pi}\left(\sum_jp_j\right)^2
\le {L^2\over4\pi}.
```

This upper-bounds the area of every subfamily of bounded faces, including the internal strict rhombi.

Combining with `L<=2(delta+r)` gives

```math
\boxed{A_{4,r}^{int}\le(\delta_r+r_r)^2/\pi.}
```

**Verdict:** PASS. Bridges and articulation multiplicities only weaken the bound in the safe direction.

---

## 3. Metric-slack rearrangement

With

```math
\eta_r=\delta_r+2-d_r,
```

we have

```math
\delta_r+r_r=r_r+\eta_r+d_r-2.
```

Taking square roots in the nonnegative area inequality gives

```math
\sqrt{\pi A_{4,r}^{int}}
\le r_r+\eta_r+d_r-2,
```

and therefore

```math
\boxed{
r_r+\eta_r
\ge\sqrt{\pi A_{4,r}^{int}}+2-d_r.}
```

**Verdict:** PASS.

---

## 4. Loaded-touching rhombi are only boundary order

The selected harmonic cell has `a_r=O(D)` loaded attachments. Every loaded source vertex has full unit-contact degree at most three.

A strict rhombus incident to a loaded attachment uses two consecutive contact edges at that vertex. The number of such bounded-face incidences is at most the planar face-incidence count at the vertex, hence at most its degree. Summing over loaded attachments gives at most `3a_r=O(D)` loaded-rhombus incidences and therefore at most `O(D)` distinct strict rhombi touching a loaded vertex.

Every unit rhombus has area at most one. Deleting all of them loses only `O(D)` area.

A strict-rhombus face of the induced harmonic graph `H_r` whose four vertices all lie in `I_r` remains a bounded face after deleting loaded vertices elsewhere: its four internal contact edges remain, its interior contained no `H_r` vertex or edge, and deletion cannot insert a crossing or merge through one of those retained boundary edges.

Thus

```math
A_{4,r}^{int}\ge A_{4,r}-O(D).
```

**Verdict:** PASS.

---

## 5. Section-118 area source and same-carrier scope

The hostile-reviewed sharp Section-118 companion uses the same wrapping harmonic carrier throughout its signed-return proof. Its endpoint scalar has

```math
A_*=0.4703752868004241\ldots
```

and the underlying Section-117 statement is explicitly

```math
A_{4,D}/D^2\ge A_*-o(1)
```

for the strict-rhombus area of that carrier. The endpoint diameter is

```math
d_*/D\to0.9762439137425688\ldots
```

on the endpoint countersequence under discussion.

Therefore the Section-151 substitution uses area and diameter of the same physical harmonic cell. There is no cross-carrier mixing.

**Verdict:** PASS at endpoint-countersequence scope.

---

## 6. Numerical margin

Direct evaluation gives

```math
\sqrt{\pi A_*}=1.215618174198792\ldots
```

and

```math
\sqrt{\pi A_*}-\lambda_*
=0.239374260456223\ldots>0.
```

Hence

```math
r_*+\eta_*\ge(0.2393742604\ldots-o(1))D.
```

Section 150 at the Section-148 lower edge gives both `R_I=o(D)` and `sum eta_r=o(D)`, so

```math
r_*+\eta_*\le R_I+\sum_r\eta_r=o(D),
```

a contradiction.

**Verdict:** PASS with a large first-order margin.

---

## 7. What is and is not closed

Section 151 rigorously eliminates the specific Type-II lower-edge endpoint produced by Sections 118, 148, and 150. It does not by itself eliminate Type-II sequences with a larger wrapping-support parameter, because both the complement-gap diameter moment and the retained carrier-area floor vary with that parameter.

The correct next step is a correlated scalar continuation, not a claim that Type II is closed already.

The most useful finite theorem to retain is the carrier inequality

```math
\boxed{
r_r+(\delta_r+2-d_r)
\ge\sqrt{\pi A_{4,r}^{int}}+2-d_r.}
```

It can be inserted into any later branch where a macroscopic carrier supplies a quantitative rhombus-area floor.

**Final classification:** audited-working proof-only theorem. The Section-148 lower-edge endpoint is impossible; C-II remains open.

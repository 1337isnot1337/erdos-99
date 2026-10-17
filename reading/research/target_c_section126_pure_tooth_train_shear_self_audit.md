> Generated reading edition · [exact source](../../research/target_c_section126_pure_tooth_train_shear_self_audit.md) · source SHA-256 `9ac68bbf14739d9f658a01f539f78235ea0029cf54d0056ff68494c776d4fbd0`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "68d913536a9f062f481a75d6249209f51d0100bd", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_section126_pure_tooth_train_shear_self_audit.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "51b6f88724b775b1ebab2f923333ee5214b9eb9febf5de0a115bbe485553bdf2"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — Target C Section 126 pure-tooth train-shear normal form

**Date:** 2026-09-12  
**Artifact:** `research/target_c_section126_pure_tooth_train_shear_normal_form.md`  
**State lock:** audit.46; theorem authority unchanged  
**Verdict:** **PASS at proof-only scope.**

## 1. Augmented-ledger collapse

With exactly one unloaded component and `A=B`, the canonical tile defect is

```math
d_{tile}=q-2-(q-2)=0.
```

Canonical Section 123 gives

```math
e_{BB}-k={1\over2}(q-T_\triangle+Q^+)+d_{tile}.
```

Under `T_triangle=q`, `Q^+=0`, this gives `e_BB-k=0`.

Canonical Section 63 gives

```math
e_{BB}=Q+2k+u_B+c_B
```

with every term on the right nonnegative. Hence

```math
0=e_{BB}-k=Q+k+u_B+c_B,
```

so `Q=k=u_B=c_B=e_BB=0`. Since `k=d_H+s_Z`, both `d_H` and `s_Z` vanish. Therefore `h=q`, and canonical Woodall topology puts the diameter graph in the connected odd-unicyclic branch.

**Verdict:** valid.

## 2. Global face and stopped-train count

Canonical Section 67 gives

```math
b+Q=2(q-k).
```

Thus `b=2q`. Since `Q=0`, every bounded nonquadrilateral face is absent. Every bounded contact face has degree four; the canonical convex-face theorem makes it a strict unit rhombus.

The finite stopped-train theorem DT applies to the **full contact core**, not only one selected grain. Its exact count is

```math
T_{train}={b+Q\over2}+2f=q.
```

DT explicitly includes a contact edge incident to no rhombus as a singleton train. It also proves every train component is a path rather than a cycle by strict monotonicity of the transverse coordinate.

**Verdict:** valid. No hidden bridge-free hypothesis is used.

## 3. Every stopped train is an exact global contact cut

There are no bounded exceptional faces. Therefore every endpoint of every non-singleton stopped train is a contact edge incident to the actual outer face.

For completeness, re-run the ZGS cut proof. Join opposite edge midpoints through each rhombus of the train. DT gives a simple midpoint path meeting the contact graph exactly at the midpoints of the train contact edges. Join its two endpoint midpoints by a simple arc in the outer face, chosen outside the embedded graph. The union is a Jordan curve avoiding source vertices. Any contact edge crossing its two shores must intersect this Jordan curve; the only graph intersections are the train-edge midpoints. Thus the train contact edges are exactly the global contact cutset.

All train edges are parallel. Orient the midpoint path by its strictly increasing transverse coordinate. The sign with which it crosses every train edge is constant, so after choosing shore labels every cut edge has the same shore-oriented unit vector `u_tau`.

Translate one shore by

```math
R_\theta u_\tau-u_\tau.
```

Every same-shore contact vector is unchanged, while every cut contact vector becomes `R_theta u_tau`, still unit. For sufficiently small `theta`, inactive noncontact pairs retain strict unit-separation slack. Thus the deformation is an exact finite contact-preserving shear.

If a stopped train is a singleton edge incident to no rhombus, with no bounded exceptional face available both incident face occurrences are outer. In a connected plane graph such an edge is a bridge. Translating one bridge component by the same formula gives the exact one-edge shear directly.

**Verdict:** valid independently of treating the old ZGS report as authority.

## 4. Contact-row independence

Section 57 gives mixed rank `2m-3`. Since `s_Z=0`, the mixed row count is

```math
e+h=2m-2.
```

Thus mixed left nullity is one. The relative-interior KKT stress spans it and has every diameter coordinate positive.

Any nonzero contact-only row dependence would extend by zeros on the diameter rows to a second mixed row dependence. It cannot be proportional to KKT because its diameter block is zero. Contradiction.

Hence `rank R_C=e`. With `h=q`,

```math
e=2m-2-q,
```

so

```math
\dim\ker R_C=2m-e=q+2.
```

Removing the three Euclidean motions leaves `q-1` non-Euclidean contact-flex dimensions.

**Verdict:** valid.

## 5. Train angular coordinates

For an infinitesimal bar flex, the derivative of a unit edge vector is perpendicular to the edge. In one rhombus, orient opposite parallel sides consistently. Differentiating parallelogram closure gives

```math
(\omega_1-\omega_3)Ju+(\eta_2-\eta_4)Jw=0.
```

The two rhombus directions are independent, hence opposite sides have equal angular velocities. Angular velocity therefore propagates along each stopped train.

If every train angular velocity is zero, every contact edge vector has zero derivative. Connectedness then forces equal velocities at all core vertices, i.e. a translation. Thus the train-angle map has kernel exactly the two-dimensional translation space.

The contact-flex space has dimension `q+2`, so after quotienting translations it has dimension `q`, equal to the number of train coordinates. The map to `R^q` is therefore an isomorphism. Common angular velocity on all trains is precisely Euclidean rotation modulo translation.

The exact one-train shears from the preceding section map to the standard basis, so they genuinely realize these coordinates rather than merely giving formal infinitesimal parameters.

**Verdict:** valid.

## 6. Square diameter derivative matrix

There are exactly `h=q` active diameter rows and `q` train coordinates. A common train rotation is Euclidean, so `A_train 1=0`.

Mixed rigidity says a contact flex with zero derivative on every active diameter edge is Euclidean. After quotienting translations in train coordinates, the only such vector is common rotation. Therefore

```math
\ker A_{train}=span\{1\},
\qquad rank A_{train}=q-1.
```

Restrict KKT stationarity to any contact flex. Every contact row evaluates to zero, so the strictly positive diameter multiplier vector satisfies

```math
beta^T A_{train}=0.
```

Rank `q-1` makes the left kernel one-dimensional, hence exactly `span{beta}`.

**Verdict:** valid.

## 7. What is not proved

The audit explicitly rejects the next unproved leap:

> circular-split support + odd-unicyclic diameter thrackle + positive left kernel
> automatically contradicts rank `q-1`.

No such sign theorem has been proved. Small abstract circular-split matrices can have a rotational right kernel and a positive left kernel. A closing theorem must use the actual geometric crossing derivatives and the complete train-cut system, not only zero/nonzero support.

The exact theorem also does not cover an asymptotic branch with `o(D)` nontriangular teeth or defects; it classifies only the exact pure endpoint stated in its hypotheses.

## 8. Source retention and authority

- Contact-isolated source points remain part of the original configuration and are not inserted into the Section-57 core kernel.
- Every deformation in the train-coordinate theorem is applied to the nonisolated contact core only as a contact-framework statement; Section 126 does not claim that an arbitrary train shear is by itself a feasible full-source diameter-nonincreasing motion.
- Inactive full-source pairs are used only for the local exact-contact shear statement and retain strict slack for sufficiently small parameters.
- Audit.46 remains canonical through Section 123. Sections 124--126 are proof-only.

**Final audit verdict:** Section 126 is proof-valid at proof-only scope. C-II remains open.

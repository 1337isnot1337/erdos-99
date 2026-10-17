> Generated reading edition · [exact source](../../research/target_c_section127_interface_augmented_defect_dichotomy.md) · source SHA-256 `9ff0cc0899163228b68b5f493fc1de61699a2a347f417115adf28a977191ba45`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "2aa6f4e1a92ddcfc7a601b5792b934f03e7e0b49", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_section127_interface_augmented_defect_dichotomy.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "44f1ecd74a3139570cefd81de36bb44abb34ac872d947d052e9b1b7e91f7059e"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — Section 127: the interface floor forces high loaded density or linear augmented defect

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**
**Status:** proof-only research candidate stacked on canonical audit.46.
**Dependencies:** canonical Sections 63, 67, 85 and 123.

Canonical Section 85 forces a linear physical boundary for the global strict-rhombus complex. Canonical Section 123 expresses all harmonic-cell augmented defect in the single loaded/topological scalar `e_BB-k`. These two statements combine exactly.

Put

```math
A_*:=\sum_r(a_r-T_r),
\qquad
Q_*:=\sum_rQ_r^+,
\qquad
J_{aug}:=A_*+Q_*+2d_{tile}.
\tag{127.1}
```

Canonical Section 123 gives

```math
\boxed{J_{aug}=2(e_{BB}-k).}
\tag{127.2}
```

Let `R_4` be the number of global bounded strict-rhombus contact faces, `f` the number of global bounded nonquadrilateral contact faces, and `q=|B|`. Then every finite post-ZF C-II source satisfies

```math
\boxed{
(q-k)+J_{aug}\ge2\sqrt{R_4}.
}
\tag{127.3}
```

Consequently, in the canonical Type-II full-core branch, where

```math
{R_4\over D^2}\to\Delta,
\qquad
\Delta={\pi\over2\sqrt3},
```

one has

```math
\boxed{
\liminf_{D\to\infty}
{(q-k)+J_{aug}\over D}
\ge
2\sqrt\Delta
=2\sqrt{\pi\over2\sqrt3}
=1.9046\ldots .
}
\tag{127.4}
```

This produces the exact structural split

```math
\boxed{
J_{aug}=o(D)
\quad\Longrightarrow\quad
\liminf{q-k\over D}\ge2\sqrt\Delta.
}
\tag{127.5}
```

More generally, for every fixed `eta>0`, any Type-II subsequence with

```math
{q-k\over D}\le2\sqrt\Delta-\eta+o(1)
```

must satisfy

```math
\boxed{J_{aug}\ge(\eta-o(1))D.}
\tag{127.6}
```

Thus the full-core survivor cannot simultaneously have a low loaded-hull count and a nearly pure triangular-tooth augmentation. The live branch is now explicitly either

1. **high loaded density:** `(q-k)/D>=1.9046...` asymptotically; or
2. **linear augmented/tile defect:** `A_*+Q_*+2d_tile=Omega(D)`.

This does not close either branch. It is a source-level incompatibility between the canonical interface theorem and the canonical augmented-cell theorem, and it rules out treating their defect currencies as independent.

---

## 127.1 Global nonquadrilateral faces are paid by `e_BB-k`

Canonical Section 63 gives the exact loaded-contact decomposition

```math
\boxed{
e_{BB}=Q+2k+u_B+c_B,}
\tag{127.7}
```

where `Q=sum_f(deg f-4)` is the global bounded-face degree excess and `u_B,c_B>=0`. Therefore

```math
\boxed{
e_{BB}-k=Q+k+u_B+c_B\ge Q.}
\tag{127.8}
```

Every bounded nonquadrilateral contact face has degree at least five, so it contributes at least one to `Q`. Hence

```math
\boxed{Q\ge f,}
\qquad
\boxed{e_{BB}-k\ge f.}
\tag{127.9}
```

Combining (127.2) and (127.9),

```math
\boxed{J_{aug}\ge2f.}
\tag{127.10}
```

No local/global face identification is needed: `f` and `Q` are the global contact-face quantities from the canonical post-ZF ledger, while `J_aug` is linked to them only through the exact scalar `e_BB-k`.

---

## 127.2 Insert the canonical interface floor

Canonical Section 85 proves the finite interface inequality

```math
\boxed{q-k+2f\ge2\sqrt{R_4}.}
\tag{127.11}
```

Equation (127.10) gives

```math
(q-k)+J_{aug}
\ge(q-k)+2f
\ge2\sqrt{R_4},
```

which is (127.3).

The proof uses no carrier diameter coefficient, phase-bin constant, or noncanonical low-response theorem.

---

## 127.3 Type-II asymptotics

Canonical Sections 79--85 give, in the full-core Type-II branch,

```math
R_4=(\Delta+o(1))D^2,
\qquad
\Delta={\pi\over2\sqrt3}.
\tag{127.12}
```

Therefore `2sqrt(R_4)/D -> 2sqrt(Delta)`. Divide (127.3) by `D` and pass to `liminf` to obtain (127.4). Equations (127.5)--(127.6) follow immediately.

---

## 127.4 Interaction with proof-only Section 125

Section 125 independently forces

```math
\liminf {1\over D}
\left[
\Delta_{ad}+{A_*\over2}+3Q_*
\right]
\ge {\pi\over4}(2-\sqrt3),
\tag{127.13}
```

where `Delta_ad=sum_r(a_r-d_r)`.

Sections 125 and 127 constrain different projections of the same augmented state:

- Section 125 says the aggregate signed-return demand must be paid by attachment-count/diameter excess or augmented face defect;
- Section 127 says the global rhombus-interface demand must be paid by loaded density or augmented/tile defect.

In particular, if

```math
A_*+Q_*+d_{tile}=o(D),
```

then both conclusions sharpen simultaneously to

```math
\liminf {q-k\over D}\ge2\sqrt\Delta
\tag{127.14}
```

and

```math
\liminf {\Delta_{ad}\over D}
\ge{\pi\over4}(2-\sqrt3).
\tag{127.15}
```

This is the precise **high-density triangular-tooth regression** left by the two ledgers.

---

## 127.5 Relation to the recent half-perimeter floor

The current noncanonical low-response research note records the independently elementary Type-II consequence

```math
\liminf{q-k\over D}\ge{\pi\over2}=1.57079\ldots,
```

from `per(F)<=q+x_B`, `q-x_B>=2k`, and `per(F)/D->pi`.

Section 127 does not depend on that note. If the half-perimeter floor is later promoted, the two statements give a useful quantitative picture: at the smallest permitted loaded density, the interface theorem would require augmented/tile defect density at least

```math
2\sqrt\Delta-\frac\pi2
=0.3338\ldots .
```

As `J_aug/D` tends to zero, the required loaded density rises to `2sqrt(Delta)=1.9046...`.

No upper obstruction below `1.9046...` is presently proved, so this remains a dichotomy rather than closure.

---

## 127.6 Scope and surviving obstruction

- The finite theorem (127.3) holds before asymptotics.
- No source point is deleted.
- No Section-57 affine-kernel statement is applied to isolated source coordinates.
- `A_*`, `Q_*`, and `d_tile` are the exact canonical augmented-cell currencies from Section 123.
- `f`, `Q`, `R_4`, `q`, and `k` are the exact global canonical currencies from Sections 63, 67, and 85.
- No unreviewed interface-saturation or low-response theorem is needed for (127.3)--(127.6).

The remaining high-value question is explicit:

> Can a Type-II global minimizer simultaneously have `(q-k)/D>=2sqrt(Delta)`, sublinear augmented/tile defect, and the Section-125 linear attachment-count-minus-diameter excess?

A negative answer would eliminate the pure triangular-tooth regression. A positive geometric model must still satisfy the full diameter-thrackle/KKT constraints, not only the planar cell ledgers.

**Disposition:** proof-only structural dichotomy. C-II and Level I remain open.

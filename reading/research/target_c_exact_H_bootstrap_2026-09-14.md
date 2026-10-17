> Generated reading edition · [exact source](../../research/target_c_exact_H_bootstrap_2026-09-14.md) · source SHA-256 `2ad44e255ac8e853363d230b291233f8ddcef9bea391654cd899e14eeb7ed9fd`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "b138389e54bb467f8590e0d81b52d406d57a4940", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_exact_H_bootstrap_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f6493243a8953f40d4b11b43a061902fb83963e74bf91355d5b19e13c0cc7d2d"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — exact H/J bootstrap without the three-fifths loss

**Date:** 2026-09-14
**Repository base:** `704e8e2c`
**Target:** Target C-II canonical full-core Type-II branch
**Claim class:** proof-only algebraic strengthening
**External literature:** none

## LEVEL I STATUS

`STILL OPEN`

The current `q-k` bootstrap propagates the interface currency

```math
J=(b-P_F)+(Q+4f)
```

to

```math
H=(b-P_F)+(Q+2f)
```

through the general inequality `H>=3J/5`. In the present full-core ledger, `H` can
instead be written exactly in terms of `J`, `q-k`, and `P_F`. This removes the
three-fifths relaxation and gives slightly stronger first-order chamber-area and
rhombus-deficit coefficients.

## 1. Exact identity

Let

```math
t_D:=q-k.
```

The complete stopped-train identities give

```math
J=2T-P_F
=2(t_D+2f)-P_F.
\tag{EH.1}
```

Therefore

```math
4f=J-2t_D+P_F.
\tag{EH.2}
```

Since `H=J-2f`, substitution yields

```math
\boxed{
H={J\over2}+t_D-{P_F\over2}.
}
\tag{EH.3}
```

This is finite and exact.

## 2. Updated Type-II coefficient

Use the current proof-only floors

```math
\liminf {t_D\over D}\ge t_{42}:=C_{146}+0.0013751,
```

```math
\liminf {J\over D}\ge j_{171}:=t_{42}+2C_*-\pi,
```

with

```math
C_*=2\sqrt{\Delta_2}+0.00042,
\qquad
\Delta_2={\pi\over2\sqrt3},
```

and canonical `P_F/D->pi`. Equation (EH.3) gives

```math
\boxed{
\liminf {H\over D}
\ge h_{42}:={j_{171}\over2}+t_{42}-{\pi\over2}
=1.494785917107288\ldots .
}
\tag{EH.4}
```

The previous `3j_171/5` value was

```math
1.493632327107288\ldots,
```

so the exact identity recovers

```math
0.00115359D-o(D)
```

of interface currency.

## 3. Chamber area/population surplus

Canonical Section 85 gives

```math
A_{ch}-a_0Z_{ch}\ge c_0H,
\qquad
c_0={\sqrt3\over4}.
```

Hence

```math
\boxed{
\liminf {A_{ch}-a_0Z_{ch}\over D}
\ge c_0h_{42}
=0.647261288717066\ldots .
}
\tag{EH.5}
```

This improves the previous `0.646761769594290...` coefficient.

## 4. Positive-core minus rhombus count

The exact face identity can be written

```math
m-R_4={P_F+H\over2}+1.
\tag{EH.6}
```

Therefore

```math
\boxed{
\liminf {m-R_4\over D}
\ge {\pi+h_{42}\over2}
=2.318189285348541\ldots .
}
\tag{EH.7}
```

Using the full-source Oler upper bound

```math
n\le\Delta_2D^2+{\pi\over2}D+1
```

and `m<=n`, this sharpens the absolute rhombus-count deficit to

```math
\boxed{
\liminf {\Delta_2D^2-R_4\over D}
\ge {h_{42}\over2}
=0.747392958553644\ldots .
}
\tag{EH.8}
```

The corresponding strict-rhombus area deficit coefficient is

```math
\boxed{
a_0{h_{42}\over2}
=0.647261288717066\ldots .
}
\tag{EH.9}
```

The repeated coefficient in (EH.5) and (EH.9) again comes from the same exact
Section-85 currency.

## 5. Frontier effect

The gain is modest numerically, but the point is conceptual: downstream work should
use (EH.3), not the generic inequality `H>=3J/5`, whenever both the `J` and `q-k`
floors are available. No further optimization is required to obtain these constants.

This still does not produce a source-preserving strict diameter decrease or an exact
unit triangle. C-II remains open.

> Generated reading edition · [exact source](../../research/target_c_ag58_lossless_train_and_detourfree_propagation_2026-09-14.md) · source SHA-256 `aca2fa31858308fbdcff0b306febc86e2bdc2d1bb119c1f5fb08fa3bcc640460`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "af47f7a8a62fe9f1d8ca5135f1b2927e3ff8032e", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_ag58_lossless_train_and_detourfree_propagation_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "3007a415a71b7ad4248c1a25c87aa8a00fb3ae1a9c63fb155f57ae543958d23a"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — AG58 lossless train split and detour-free propagation

**Date:** 2026-09-14  
**Target:** Target C-II canonical full-core Type-II branch  
**Claim class:** proof-only exact propagation of AG58  
**External input:** none

## LEVEL I STATUS

`STILL OPEN`

The first AG58 propagation note used the difference-body floor on `q` when converting the all-train gap into a singleton-versus-rhombic split. That is valid but unnecessarily weak. The Section-171 proof-only floor on

```math
U:=q-k
```

is stronger and should be inserted before the split.

With

```math
\eta_{grid}=g=0.00058
```

and the AG58 Section-171 endpoint

```math
\boxed{
\liminf {U\over D}
\ge t_{58}:={4\over9}\left(\pi+\sqrt{\Delta_2}\right)+0.0014085
=1.820922037979444\ldots,
}
\tag{L58.1}
```

we obtain the lossless total train-defect floor

```math
\boxed{
\liminf {\rho_{rec}+\sigma_R\over D}
\ge t_{58}+2g
=1.822082037979444\ldots .
}
\tag{L58.2}
```

This supersedes the weaker `1.479330...` train-split coefficient in the first AG58 propagation note.

---

## 1. Exact lossless train defect

Let `T` be the complete stopped-train count, `T_R` the non-singleton rhombic-train count, and `S=T-T_R` the singleton count. Put

```math
\rho_{rec}=2S,
\qquad
\sigma_R=2T_R-4\sqrt{R_4}.
```

Then exactly

```math
\boxed{
\rho_{rec}+\sigma_R=2T-4\sqrt{R_4}.
}
\tag{L58.3}
```

AG58 gives

```math
{T-q/2\over D}
\ge2\sqrt{\Delta_2}+g-o(1).
\tag{L58.4}
```

Hence

```math
2T
\ge q+4\sqrt{\Delta_2}D+2gD-o(D).
```

Since `q=U+k>=U`, (L58.1) applies, while Type-II rhombic saturation gives

```math
{\sqrt{R_4}\over D}\to\sqrt{\Delta_2}.
```

Substitution into (L58.3) proves (L58.2).

---

## 2. Strong singleton-versus-rhombic split

From (L58.2), after subsequence selection at least one of

```math
\rho_{rec}\ge\left({L_{58}\over2}-o(1)\right)D,
\qquad
\sigma_R\ge\left({L_{58}\over2}-o(1)\right)D,
```

holds, where

```math
L_{58}:=t_{58}+0.00116
=1.822082037979444\ldots .
```

Therefore either

```math
\boxed{
S\ge0.455520509494861\ldots D-o(D),
}
\tag{L58.5}
```

or

```math
\boxed{
\sigma_R\ge0.911041018989722\ldots D-o(D).
}
\tag{L58.6}
```

On the rhombic branch, the exact rationalization

```math
M_R={\sigma_R\over8}
\left(4\sqrt{R_4}+{\sigma_R\over2}\right)
```

gives

```math
\boxed{
\liminf {M_R\over D^2}
\ge0.485672748623765\ldots .
}
\tag{L58.7}
```

This is a branch statement after the corresponding subsequence has been selected.

---

## 3. Bridge-subtracted form

Split singleton trains as

```math
S=S_o+S_E,
```

where `S_o` has no bounded-exceptional terminal incidence and `S_E` has at least one. The independently audited bridge payment gives

```math
2S_o\le b-P_F+o(D).
\tag{L58.8}
```

Subtracting only that paid population from (L58.2),

```math
\boxed{
\sigma_R+2S_E+(b-P_F)
\ge(L_{58}-o(1))D.
}
\tag{L58.9}
```

Thus every surviving first-order currency is source-geometric: rhombic non-Mantel slack, exceptional-face singleton incidence, or metric outer detour.

---

## 4. AG58 detour-free gate

The existing detour-free elimination is algebraic in the all-train gain. Repeating it with general gain `g` gives

```math
\boxed{
{\sigma_R+2S_E\over D}
\ge
c_{DF}(g)
+{5\over2}{k\over D}
+{Q-f\over D}
-o(1),
}
\tag{L58.10}
```

where

```math
\boxed{
c_{DF}(g)
=\sqrt{\Delta_2}-\frac\pi4+\frac52g.}
\tag{L58.11}
```

For `g=0.00058`,

```math
\boxed{
c_{DF,58}=0.168364643466509\ldots .}
\tag{L58.12}
```

The derivation is the same exact elimination as the AG42 note: the all-train input contributes `g/2` through the exceptional-face floor and `2g` through the total train defect, for total `5g/2`.

Consequently, even after detour is removed, every survivor has the two-way alternative

```math
\boxed{
\sigma_R\ge0.0841823217332545\ldots D-o(D)
}
\tag{L58.13}
```

or

```math
\boxed{
S_E\ge0.0420911608666273\ldots D-o(D).
}
\tag{L58.14}
```

when the positive `k` and `Q-f` terms are conservatively discarded.

For any fixed two projective windows, the exceptional-singleton incidence theorem similarly gives

```math
\boxed{
\sigma_R+11(Q-f)+20T_{off}
\ge c_{DF,58}D+{5\over2}k-o(D).
}
\tag{L58.15}
```

---

## 5. Updated low-`t` structural numbers

At the safe AG58 endpoint `t=t58`, the exact low-`t` ledgers give, at their most permissive `delta=kappa=0` values,

```math
{f\over D}\ge0.497372297369096\ldots,
```

```math
{Q-f\over D}\le0.002879125,
```

```math
{p_5\over D}\ge0.494493172369096\ldots,
```

```math
{L_{OO}\over D}\ge0.320167770872156\ldots,
```

and for every fixed pair of sufficiently narrow projective windows,

```math
\boxed{
{T_{off}\over D}\ge0.247246586184548\ldots .
}
\tag{L58.16}
```

The topology budget obeys

```math
{d_H+s_Z\over D}
\le0.0115165+o(1),
```

so the loaded diameter thrackle has

```math
{h\over q}\ge0.9937152053\ldots-o(1).
```

Combined with the flat-middle injectivity theorem on `R_F=o(D)`, the low-`t` corner has about `0.49449D` **distinct** almost-flat positive-core vertices, not merely that many pentagonal face incidences.

---

## 6. Research effect

The corrected AG58 package sharpens the active branch description to

```text
all full-core Type-II survivors:
    at least 0.45552 D singleton trains
    OR at least 0.91104 D rhombic non-Mantel slack;

and after paying pure outer bridges/detour:
    sigma_R + 2 S_E
      >= 0.1683646 D + 2.5 k + (Q-f) - o(D).
```

The scalar gap itself is no longer the useful missing theorem. The remaining task is to make one of these large source-level populations incompatible with the near-extremal diameter-thrackle / pentagon network, or construct a finite same-cardinality diameter descent.

**Disposition:** proof-only exact propagation. C-II remains open.

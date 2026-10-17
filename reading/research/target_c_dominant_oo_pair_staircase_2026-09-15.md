> Generated reading edition · [exact source](../../research/target_c_dominant_oo_pair_staircase_2026-09-15.md) · source SHA-256 `df1f92eedf61d6f6e4e20b8bdb2ff55dff3d3c3b73bb22ac70200c5aec6ec33b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 13 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "0f095a9ea083cc32b0727aead0a5a2a549d5ff37", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_dominant_oo_pair_staircase_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "d3d8f51b3a2a2a67c462876231d2bbbdb156724594d88e83f4a5f4f588720aa5"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — dominant O--O pair-weight staircase above the live low-`t` floor

**Date:** 2026-09-15  
**Status:** proof-only structural narrowing  
**Scope:** fully force-visible no-container/full-core Type-II branch  
**Dependencies:** hostile-audited matched atomic gap `g=0.0076`; hostile-audited restored dominant/complement outer-energy stack; retained dominant O--O pair-weight interpretation  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The broad live-family theorem proves retained dominant outer-to-outer pair weight
`>0.0740D-o(D)` for every proof-only full-core survivor with `t=(q-k)/D<=1.860`.
Near the actual low-`t` frontier the same bootstrap is much stronger.

Let `P_OO^dom` denote the retained pair weight of dominant-window complete trains whose
two terminal occurrences are both selected outer occurrences. Then

```math
\boxed{
t\le1.844
\Longrightarrow
{P_{OO}^{dom}\over D}>0.29-o(1),
}
\tag{OOS.1}
```

```math
\boxed{
t\le1.850
\Longrightarrow
{P_{OO}^{dom}\over D}>0.21-o(1),
}
\tag{OOS.2}
```

and

```math
\boxed{
t\le1.855
\Longrightarrow
{P_{OO}^{dom}\over D}>0.14-o(1).
}
\tag{OOS.3}
```

Together with the existing `t<=1.860` theorem, the useful staircase is therefore

```text
t <= 1.844  -> dominant retained O-O pair weight > 0.290 D
t <= 1.850  -> dominant retained O-O pair weight > 0.210 D
t <= 1.855  -> dominant retained O-O pair weight > 0.140 D
t <= 1.860  -> dominant retained O-O pair weight > 0.074 D
```

Since the new residual-coupled floor gives `t>=1.84355`, the first line is nonvacuous:
any survivor in the narrow live interval

```math
1.84355\lesssim t\le1.844
```

has a very large dominant O--O family.

---

## 1. Common bootstrap

Use

```math
t={q-k\over D},
\qquad
\kappa={k\over D},
\qquad
\delta={d_{out}\over D},
```

```math
U={9t\over2}-2\pi-2\delta-\kappa/2,
```

and the hostile-audited matched floor

```math
U\ge C_{76}:=2\sqrt{\Delta_2}+0.0076,
\qquad
\Delta_2={\pi\over2\sqrt3}.
```

Let

```math
F(z)=z-6\sin(z/6),
\qquad
m_2(U)={U+\sqrt{8\Delta_2-U^2}\over2},
\qquad
r_2(U)=U-m_2(U).
```

The audited retained-mass and complement-incidence inequalities give

```math
z+p\ge\pi-U-{t+\kappa\over2}+m_2(U)-o(1),
\tag{OOS.4}
```

```math
p\le
{\delta-F(z)+r_2(U)^2\over2(1-\delta)}+o(1),
\tag{OOS.5}
```

and

```math
\delta\ge F(z)-o(1).
\tag{OOS.6}
```

Fix an upper endpoint `T`.  Put

```math
U_{max}(T)={9T\over2}-2\pi,
\qquad
\delta_{max}(T)={U_{max}(T)-C_{76}\over2}.
```

If `z>=z_j-o(1)`, then (OOS.6) gives

```math
U\le U_j:=U_{max}(T)-2F(z_j)+o(1).
```

Since `m_2'(U)<0` and `r_2'(U)>0` on every interval used below, (OOS.4)--(OOS.5) give
the explicit lower bootstrap

```math
z\ge
\pi-U_j-{T\over2}+m_2(U_j)
-
{\delta_{max}(T)-F(z_j)+r_2(U_j)^2
 \over2(1-\delta_{max}(T))}
-o(1).
\tag{OOS.7}
```

The companion exact-rational verifier applies this same map at each of the three
staircase endpoints.

---

## 2. Convert retained occurrence mass to O--O pair weight

Freeze shrinking windows around the dominant exact three-phase orbit.  Let `M_D` be
the complete-train count in those windows and `P_D` the retained pair weight of trains
with two selected outer terminals.

A train with fewer than two selected terminals contributes at most one unit of retained
occurrence weight; a train with two contributes at most two.  Hence, finitely,

```math
z_DD\le M_D+P_D.
\tag{OOS.8}
```

After passing to the train-measure limit and then shrinking the windows,

```math
{M_D\over D}\le A+o(1)\le C+o(1)\le U+o(1),
```

where `A` is total exact atomic train mass and `C=(T-q/2)/D`. Therefore

```math
\boxed{
{P_{OO}^{dom}\over D}
\ge z-U-o(1).
}
\tag{OOS.9}
```

No lower bound on dominant orbit mass is misused as an upper bound here.

---

## 3. Exact staircase certificates

The verifier

`research/verify_target_c_dominant_oo_pair_staircase_2026-09-15.py`

uses exact `Fraction` arithmetic, Machin bounds for `pi`, integer-square-root
enclosures, and alternating-series sine bounds.

### `t<=1.844`

It certifies

```text
0      -> z > 2.0721
2.0721 -> z > 2.1851
2.1851 -> z > 2.2034
2.2034 -> z > 2.2065
2.2065 -> z > 2.2070
```

and then

```math
U<1.915950,
\qquad
z-U>0.29105>0.29.
```

This proves (OOS.1).

### `t<=1.850`

It certifies

```text
0      -> z > 2.0285
2.0285 -> z > 2.1391
2.1391 -> z > 2.1570
2.1570 -> z > 2.1601
```

and then

```math
U<1.949093,
\qquad
z-U>0.21100>0.21.
```

This proves (OOS.2).

### `t<=1.855`

It certifies

```text
0      -> z > 1.9908
1.9908 -> z > 2.0991
2.0991 -> z > 2.1167
2.1167 -> z > 2.1197
```

and then

```math
U<1.976678,
\qquad
z-U>0.14302>0.14.
```

This proves (OOS.3).

The smallest bootstrap margin among these checks is about `1.70e-5`; none of the
claimed round constants is a floating-point boundary.

---

## 4. One exact phase carries a large noncrossing O--O family

The dominant exact orbit has at most three projective phase classes.  Partition the
retained O--O pair weight among them:

```math
P_{OO}^{dom}=P_1+P_2+P_3.
```

Hence one class satisfies

```math
P_i\ge {P_{OO}^{dom}\over3}.
\tag{OOS.10}
```

Retained pair weight per complete train is at most one, so the actual train count in
that class is at least `P_iD-o(D)`.  Trains in one shrinking exact phase window do not
cross one another in strict rhombi; equivalently, the endpoint-capacity argument used
in the audited complement-bracing theorem applies to them as one noncrossing family.

Consequently the staircase implies the following concrete same-phase families:

```math
\boxed{
t\le1.844
\Longrightarrow
\text{some exact phase has }>0.0966D-o(D)
\text{ dominant O--O trains},}
\tag{OOS.11}
```

```math
\boxed{
t\le1.850
\Longrightarrow
\text{some exact phase has }>0.0700D-o(D),}
\tag{OOS.12}
```

```math
\boxed{
t\le1.855
\Longrightarrow
\text{some exact phase has }>0.0466D-o(D).}
\tag{OOS.13}
```

The existing broad `0.0740D` total-pair theorem similarly gives a same-phase family
`>0.0246D-o(D)` throughout `t<=1.860`.

---

## 5. Frontier effect

This is not a new scalar low-`t` contradiction.  It replaces the vague statement
"there are linearly many dominant outer-to-outer trains" by a quantitative branch
structure:

```text
near the live floor:
  one exact phase alone contains >0.0966 D noncrossing O-O trains;
by t=1.850:
  one exact phase still contains >0.0700 D;
by t=1.855:
  one exact phase still contains >0.0466 D.
```

Every such train has the audited Section-157 two-sided actual-diameter bracing.  The
next closing target is therefore a multi-train statement for a **single laminar exact
phase family**: couple its cyclic endpoint order and two-sided diameter bracing to the
straight-line Woodall diameter thrackle, or use the strong-orbit crossing order to
show that the family forces additional missing-pair mass.

No such multi-train theorem is claimed here.

**Disposition:** proved proof-only structural narrowing; C-II and Level I remain open.

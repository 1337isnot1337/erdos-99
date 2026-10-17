> Generated reading edition · [exact source](../../research/target_c_high_t_antipodal_stress_balance_t18687_2026-09-17.md) · source SHA-256 `733ade3673494c11938708c0ccbf02d143ec135f8cbfdba49dfb344321edaf38`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 17 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "3b495d04e085f3e2f7a5f9f1cbad4ae6b613a623", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_antipodal_stress_balance_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "a98a6b8f971f44bba6d578b5a57e10545f5eb16514f4aa95b09d14f72882cf77"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — host transversality balances exact-antipodal KKT stress on both sides of the row axis

**Date:** 2026-09-17  
**Status:** proof-only high-`t` KKT strengthening; no canonical promotion claimed  
**Scope:** exact-antipodal interfaces on the selected one-sided high-`t` shore  
**Dependencies:** exact cut-resultant identity; exact antipodality; host-forced transverse-margin theorem  
**Certificate:** `research/verify_target_c_high_t_antipodal_stress_balance_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The host theorem gives every switching diameter at an exact-antipodal interface a fixed transverse component relative to the row/reaction axis. Exact KKT balance then forces substantial switching stress on **both** transverse sides.

Let

```math
c_*:=0.4143,
\qquad
s_*:=\sqrt{1-c_*^2}=0.9101403792\ldots .
\tag{AS.1}
```

At an exact-antipodal interface `i`, orient the reaction axis

```math
e_i={G_i\over |G_i|}=\pm u_i
```

and write the exact switching identity as

```math
G_i=D\sum_{h\in X_i}\beta_h d_h,
\qquad
\beta_h>0.
\tag{AS.2}
```

Put

```math
B_i:=\sum_{h\in X_i}\beta_h
```

and split the stress by transverse sign

```math
X_i^+=\{h:d_h\cdot Je_i>0\},
\qquad
X_i^-=\{h:d_h\cdot Je_i<0\},
```

```math
B_i^+=\sum_{h\in X_i^+}\beta_h,
\qquad
B_i^-=\sum_{h\in X_i^-}\beta_h.
\tag{AS.3}
```

Then, uniformly along the survivor sequence,

```math
\boxed{
B_i^+,B_i^-
\ge\left({c_*\over1+c_*}-o(1)\right)B_i
=(0.2929364349\ldots-o(1))B_i.
}
\tag{AS.4}
```

Moreover the common transverse moment on either side,

```math
T_i
:=\sum_{h\in X_i^+}\beta_h(d_h\cdot Je_i)
=\sum_{h\in X_i^-}\beta_h(-d_h\cdot Je_i),
\tag{AS.5}
```

satisfies

```math
\boxed{
T_i\ge\left({c_*\over2}-o(1)\right)B_i
=(0.20715-o(1))B_i.
}
\tag{AS.6}
```

Finally the axial reaction obeys

```math
\boxed{
{|G_i|\over D}
\le(s_*+o(1))B_i,
}
\tag{AS.7}
```

or equivalently

```math
\boxed{
B_i
\ge(1.0987316053\ldots-o(1)){|G_i|\over D}.
}
\tag{AS.8}
```

No absolute KKT floor follows: both `B_i` and `|G_i|/D` may tend to zero. What is ruled out is a one-sided stress degeneration. Exact-antipodal balance cannot be carried by an arbitrarily tiny minority of switching stress on one transverse side.

---

## 1. Every switching ray has a fixed transverse component

The host-forced theorem gives, for every switching diameter at the interface,

```math
|d_h\cdot Je_i|
\ge c_*-o(1).
\tag{AS.9}
```

For readability suppress the uniform `o(1)` temporarily and restore it at the end. Thus every positive-side transverse component lies in `[c_*,1]`, and every negative-side absolute transverse component also lies in `[c_*,1]`.

Because `G_i` is exactly axial,

```math
G_i\cdot Je_i=0.
```

Taking the transverse component of (AS.2) gives

```math
\sum_{h\in X_i^+}\beta_h(d_h\cdot Je_i)
=
\sum_{h\in X_i^-}\beta_h(-d_h\cdot Je_i)
=:T_i>0.
\tag{AS.10}
```

Both sign classes are therefore nonempty.

---

## 2. Neither transverse stress mass can be small

From the component bounds,

```math
c_*B_i^+\le T_i\le B_i^+,
\qquad
c_*B_i^-\le T_i\le B_i^-.
\tag{AS.11}
```

Combining the lower bound from one side with the upper bound from the other gives

```math
B_i^-\ge c_*B_i^+,
\qquad
B_i^+\ge c_*B_i^-.
\tag{AS.12}
```

Since `B_i=B_i^++B_i^-`, each side is minimized when the ratio saturates. Hence

```math
B_i^+,B_i^-
\ge {c_*\over1+c_*}B_i.
\tag{AS.13}
```

Restoring the uniform host `o(1)` error gives (AS.4).

For the transverse moment, (AS.11) gives

```math
T_i\ge c_*\max\{B_i^+,B_i^-\}
\ge {c_*\over2}B_i,
\tag{AS.14}
```

which proves (AS.6).

This `c_*/2` bound is sharp at the aggregate level when the two stress masses are equal and every selected transverse magnitude equals `c_*`.

---

## 3. Host transversality also bounds reaction per unit switching stress

For any switching direction,

```math
|d_h\cdot e_i|^2
=1-|d_h\cdot Je_i|^2
\le1-c_*^2+o(1).
```

Therefore

```math
|d_h\cdot e_i|
\le s_*+o(1).
\tag{AS.15}
```

Take the axial component of (AS.2):

```math
{|G_i|\over D}
=
\sum_{h\in X_i}\beta_h(d_h\cdot e_i)
\le
\sum_{h\in X_i}\beta_h|d_h\cdot e_i|
\le(s_*+o(1))B_i.
\tag{AS.16}
```

This is (AS.7). Since `1/s_*=1.0987316053...`, inversion gives (AS.8).

The estimate remains valid even if some oriented switching rays have negative axial component; absolute values only weaken the upper bound.

---

## 4. Consequence for exact two-ray force compression

The existing exact force-pair theorem selects two opposite-transverse switching bars which positively generate `G_i`. The host theorem already gives each compressed coefficient

```math
\lambda_i^\pm
\ge(c_*-o(1)){|G_i|\over D}.
\tag{AS.17}
```

The present result is different: (AS.4) concerns the **original full KKT stress** on all switching bars, not a compressed representation. It shows that the true positive stress itself is quantitatively bilateral.

Thus an exact-antipodal strip has both:

```text
compressed two-ray certificate:
    two actual opposite-transverse bars generate G_i exactly;

full-stress balance:
    each transverse sign carries >=(0.292936-o(1)) of B_i,
    and each side carries transverse moment >=(0.20715-o(1)) B_i.
```

This closes a possible regression in which the two-ray compression was geometrically balanced but the underlying KKT stress was almost entirely one-sided.

---

## 5. Frontier effect

On the deep exact-force branch, local KKT scale can still vanish, but its shape cannot degenerate:

- every switching ray stays at least `24.475` degrees from the row axis;
- the true KKT stress has a fixed positive fraction on both transverse sides;
- the transverse moments cancel exactly and are each at least `0.20715 B_i`;
- the axial reaction per unit switching stress is at most `0.910141D` asymptotically.

A remaining closure argument may therefore normalize by `B_i` without losing bilateral transverse mass. The unresolved issue is still the absolute scale: global KKT normalization permits `B_i=o(1/D)` or smaller at many individual interfaces.

**Disposition:** proved quantitative bilateral balance of the full exact-antipodal switching stress and a sharper stress-versus-reaction inequality. C-II and Level I remain open.

> Generated reading edition · [exact source](../../research/target_c_support6_reciprocal_h5_triangle_angle_signature_collapse_2026-09-18.md) · source SHA-256 `32e475570ebf37ce7080c685d3b19b28fd6f43285470c7bc1fcc4bdb663859dd`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "f5ce381b0d184773345b54c2e28db9014538f4a3", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support6_reciprocal_h5_triangle_angle_signature_collapse_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "b1bf5ef031632fd56047a60138f33869b3b12395cc8eb288ee171ae3771a2e74"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — triangle-angle identities collapse the remaining uniform H5 surface signatures

**Date:** 2026-09-18  
**Status:** proved structural strengthening; theorem-state authority unchanged  
**Scope:** the three uniform noncollapsed H5 support-six sign/order orbits `P1,P2,P3` left after the current angle and wall exclusions  
**Depends on:** `target_c_support6_reciprocal_h5_uniform_angle_exclusion_2026-09-18.md`; `target_c_support6_reciprocal_h5_translation_surface_signatures_2026-09-18.md`; the exact force cycles and ground raw-ray order recorded there  
**Certificate:** `research/verify_target_c_support6_reciprocal_h5_triangle_angle_signature_collapse_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The previous translation-surface reduction left five possible Abelian-differential signatures across the three surviving uniform H5 reciprocal orbits:

```math
P_1:\ \mathcal H(4,2)\text{ or }\mathcal H(3,3),\qquad
P_2:\ \mathcal H(6),\qquad
P_3:\ \mathcal H(4,4)\text{ or }\mathcal H(5,3).
```

The ambiguity can be removed exactly.  The raw reciprocal triangles already impose affine identities among the physical force-pentagon exterior gaps.  Applying those identities to the ambiguous surface vertex classes gives

```math
\boxed{
P_1:\mathcal H(4,2),\qquad
P_2:\mathcal H(6),\qquad
P_3:\mathcal H(5,3).
}
\tag{0.1}
```

Thus the `H(3,3)` and `H(4,4)` signatures are impossible.  This does **not** yet exclude any of the three H5 sign/order orbits themselves.

---

## 1. Normalize the force gaps

For each force polygon `P_i`, let

```math
x_{i,k}=\frac{\delta_{i,k}}{\pi}
```

be the normalized exterior gap from force side `k` to side `k+1` in the exact cyclic force order.  Thus

```math
F_i:=\sum_k x_{i,k}=2.
\tag{1.1}
```

For two neighbors `a,b` of reciprocal vertex `i`, let

```math
R_i(a,b)
```

be the counterclockwise force-ray arc from the force on `ia` to the force on `ib`, expressed as the corresponding sum of the `x_{i,k}`.  Hence `R_i(a,b)` is an exact linear form in the force gaps.

Write `s_ia in {+1,-1}` for the reciprocal edge sign, so the force ray on edge `ia` is the raw reciprocal ray `y_a-y_i`, possibly reversed by `pi`.

---

## 2. Exact raw-triangle angle formula

Let

```math
\chi_i(a,b)=\operatorname{sign}\det(y_a-y_i,y_b-y_i)\in\{+1,-1\}.
```

Uniformity guarantees that no relevant pair is collinear.  Let `alpha_i(a,b)` be the ordinary interior angle between the two raw reciprocal segments `ia` and `ib`, normalized by `pi`.  Comparing the raw rays with the signed force rays gives the exact four-case formula

```math
\boxed{
\alpha_i(a,b)=
\begin{cases}
R_i(a,b),&s_{ia}=s_{ib},\ \chi_i(a,b)=+1,\\
2-R_i(a,b),&s_{ia}=s_{ib},\ \chi_i(a,b)=-1,\\
R_i(a,b)-1,&s_{ia}\ne s_{ib},\ \chi_i(a,b)=+1,\\
1-R_i(a,b),&s_{ia}\ne s_{ib},\ \chi_i(a,b)=-1.
\end{cases}}
\tag{2.1}
```

There is no metric approximation here.  Reversing exactly one raw ray adds `pi` to its argument, and the sign of `chi` determines which of the two complementary raw angles is the interior angle.

The signs `chi_i(a,b)` are already determined by the current exact sign/order data:

- at the ground vertex, the six raw rays occur in the strict order
  ```math
  1,6,5,2,3,4
  
  ```
  inside a cone of width `<pi/3`, so their pairwise orientation signs are read directly from that order;
- at a non-ground vertex, the exact force cycle is a regular five-ray tournament: the cross product from any force ray to each of the next two force rays is positive, and to each of the preceding two is negative.  Multiplication by the two edge signs recovers the raw orientation sign.

Therefore (2.1) is an explicit affine integer formula in the force-gap variables for every present raw reciprocal angle.

For every present reciprocal triangle `{i,j,k}`, its three ordinary interior angles sum to `pi`.  Define the normalized affine triangle functional

```math
T_{ijk}:=\alpha_i(j,k)+\alpha_j(i,k)+\alpha_k(i,j).
```

Then

```math
\boxed{T_{ijk}=1.}
\tag{2.2}
```

The certificate constructs every `T_ijk` directly from the recorded force cycles and edge signs.

---

## 3. Orbit P1: the eleven-corner class has order three

Use the vertex-class numbering from `target_c_support6_reciprocal_h5_translation_surface_signatures_2026-09-18.md`.  Let `G_1` be the normalized sum of the eleven physical exterior gaps feeding the all-physical eleven-corner class `C4` of `P1`.

Exact symbolic reduction gives

```math
\boxed{
\begin{aligned}
G_1={}&-F_0-T_{012}+T_{015}-T_{023}+T_{035}\\
&-T_{045}+T_{046}-T_{056}+8.
\end{aligned}}
\tag{3.1}
```

Substituting `F_0=2` and every triangle identity `T=1` gives

```math
\boxed{G_1=5.}
\tag{3.2}
```

A surface vertex class with `N` polygon corners and normalized exterior-gap sum `G` has cone angle

```math
N\pi-G\pi=2\pi m,
\qquad
m=\frac{N-G}{2}.
\tag{3.3}
```

Thus this eleven-corner class has

```math
m=\frac{11-5}{2}=3.
```

The other three small classes have order one and the total cone order is eleven, so the remaining large class has order five.  Hence

```math
\boxed{P_1:(m_v)=(5,3,1,1,1),\quad P_1\in\mathcal H(4,2).}
\tag{3.4}
```

The former `H(3,3)` option is eliminated.

---

## 4. Orbit P2: the twenty-two-corner class has order seven

Let `G_2` be the normalized exterior-gap sum at the twenty-two-corner class `C0` of `P2`.  The exact affine identity is

```math
\boxed{
\begin{aligned}
G_2={}&F_1+F_2+F_3+F_4+F_5+F_6\\
&+T_{012}-T_{013}+T_{023}-T_{045}+T_{046}-T_{056}-4.
\end{aligned}}
\tag{4.1}
```

The six face sums contribute twelve and the signed triangle terms cancel in total, so

```math
\boxed{G_2=8.}
\tag{4.2}
```

Therefore

```math
m=\frac{22-8}{2}=7,
```

recovering the already unique signature

```math
\boxed{P_2:(m_v)=(7,1,1,1,1),\quad P_2\in\mathcal H(6).}
\tag{4.3}
```

This case acts as an internal consistency check on the angle-functional method.

---

## 5. Orbit P3: the fourteen-corner class has order four

Let `G_3` be the normalized exterior-gap sum at the fourteen-corner class `C1` of `P3`.  Exact reduction gives

```math
\boxed{
G_3=
F_0+F_1+F_5
+T_{014}-T_{023}-T_{024}-T_{026}+T_{035}+T_{046}.
}
\tag{5.1}
```

The three face sums contribute six and the triangle coefficients sum to zero.  Hence

```math
\boxed{G_3=6.}
\tag{5.2}
```

Thus this class has

```math
m=\frac{14-6}{2}=4.
```

The three-corner class has order one and the total cone order is eleven, so the remaining nineteen-corner class has order six.  Therefore

```math
\boxed{P_3:(m_v)=(6,4,1),\quad P_3\in\mathcal H(5,3).}
\tag{5.3}
```

The former `H(4,4)` option is eliminated.

---

## 6. Consequence and remaining target

The noncollapsed uniform support-six H5 branch now has exactly three topological signatures, one per surviving sign/order orbit:

```math
\boxed{
P_1\in\mathcal H(4,2),\qquad
P_2\in\mathcal H(6),\qquad
P_3\in\mathcal H(5,3).
}
\tag{6.1}
```

The proof uses only the exact current force cycles, edge signs, ground raw-ray order, ordinary triangle angle sum, and translation-surface corner bookkeeping.  It does not assume a numerical reciprocal realization and does not solve the remaining unit-force metric equations.

Accordingly, none of `P1,P2,P3` is excluded by this note.  The next finite noncollapsed task is to combine the fixed signature with the full equilateral force-polygon closure and reciprocal metric integrability.  The collapsed support-six branch is untouched and remains locally feasible by its separate exact certificate.

No theorem-state file is changed.

**Disposition:** two of the five previously possible H5 translation-surface signatures are eliminated exactly; the three surviving H5 sign/order orbits have unique signatures `H(4,2)`, `H(6)`, and `H(5,3)`. C-II remains open.

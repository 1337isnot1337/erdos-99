> Generated reading edition · [exact source](../../research/target_c_strict_stopped_train_phase_gap.md) · source SHA-256 `51b90df5f91bd3e2d6ba56ca53abd38d35ec320e5175a7a5dd9b4809a23693c1`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "fa905480bd5cf413a798cf4c4f5100fe8ecef393", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_strict_stopped_train_phase_gap.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "4aad63ab18b700b23dbd26517c66c05930e0a0892ada2f566e78ed9963b97f0c"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — strict stopped-train phase gap

**Date:** 2026-09-12  
**Lifecycle:** proof-only strengthening of the near-Mantel endpoint argument; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This theorem is stronger and cleaner than the original §146-endpoint formulation. It
uses only audited-working §142 plus the near-complete signed-monotone train lemma proved
and hostile-audited in this branch.

Put

$$
\Delta_2={\pi\over2\sqrt3},
\qquad s_0:=\sqrt{\Delta_2}.
$$

Audited-working §142 proves for every Type-II survivor sequence

$$
\liminf {T-q/2\over D}\ge2s_0.
\tag{SG.1}
$$

The new result is the strict form.

### Theorem SG — uniform strict stopped-train phase gap

There exists an absolute constant `epsilon_SG>0` such that every sufficiently large
Type-II C-II survivor in the audited-working §142 scope satisfies

$$
\boxed{
{T-q/2\over D}
\ge2\sqrt{\Delta_2}+\epsilon_{SG}.
}
\tag{SG.2}
$$

Equivalently, no Type-II survivor sequence can satisfy

$$
{T-q/2\over D}\to2\sqrt{\Delta_2}.
\tag{SG.3}
$$

The proof is compactness-based and does not extract a numerical value of
`epsilon_SG`.

---

## 1. Equality in §142 forces a near-Mantel physical train graph

Assume for contradiction that a Type-II sequence satisfies (SG.3). Pass to the phase
subsequence used in audited-working §142:

$$
{T\over D}\to x,
\qquad
{q\over T}\to y,
\qquad
\mu_D\Rightarrow\mu,
$$

and let `rho` be the total atomic mass of `mu`.

Section 142 gives

$$
2s_0\le x\rho
\tag{SG.4}
$$

and

$$
y\le2(1-\rho).
\tag{SG.5}
$$

Therefore

$$
x\rho
\le x(1-y/2)
={T-q/2\over D}+o(1)
\to2s_0.
$$

Together with (SG.4),

$$
\boxed{x\rho=2s_0.}
\tag{SG.6}
$$

Audited-working §142 also proves the weighted-Mantel inequality

$$
{\Delta_2\over x^2}\le{\rho^2\over4}.
\tag{SG.7}
$$

Equation (SG.6) makes (SG.7) equality. The measure-sandwich repair in
`target_c_near_mantel_atomic_endpoint_proof_repair.md` then applies verbatim: equality
through the crossing-measure/product-measure/weighted-Mantel chain yields a physical
induced train graph `G_D` with

$$
\boxed{
|V(G_D)|=(2s_0+o(1))D,
\qquad
|E(G_D)|=(\Delta_2-o(1))D^2
={|V(G_D)|^2\over4}-o(D^2).
}
\tag{SG.8}

The graph is simple and triangle-free by §142.2.

---

## 2. Mantel stability forces one central phase atom and at most two leaves

The self-contained near-Mantel stability lemma from the endpoint proof supplies two
independent physical train shores `U_D,V_D` with

\[
|U_D|=|V_D|=(s_0+o(1))D
\tag{SG.9}
$$

and only `o(D^2)` missing `U_D x V_D` crossings.

The phase-support argument also applies unchanged. Positive-mass cross-shore atoms
must lie at exact projective separation `pi/3`; the exact-distance relation on
`R/pi Z` is a disjoint union of 3-cycles and contains no `K_{2,2}`. Hence one stability
shore is concentrated on a single central phase atom while the other uses at most its
two phase neighbors.

Choose the larger neighboring atom. This gives physical train families `A_D,B_D`
with

$$
|A_D|=(s_0+o(1))D,
\qquad
|B_D|\ge(s_0/2-o(1))D,
\tag{SG.10}
$$

family direction widths `o(1)`, limiting projective separation `pi/3`, same-family
disjointness, common crossing sign, and

$$
|A_D||B_D|-e(A_D,B_D)=o(D^2).
\tag{SG.11}
$$

---

## 3. Near-complete signed order violates the source diameter

The hostile-audited near-complete signed-monotone train lemma gives

$$
D\ge
\left({\sqrt3\over2}-o(1)\right)
(|A_D|+|B_D|).
\tag{SG.12}
$$

Using (SG.10),

$$
1
\ge
{3\sqrt3\over4}s_0-o(1).
$$

But

$$
{3\sqrt3\over4}s_0
=1.237090624640176\ldots>1.
\tag{SG.13}
$$

This contradiction proves that (SG.3) is impossible.

If no positive uniform `epsilon_SG` existed in (SG.2), choose for each integer `j` a
Type-II survivor with `D>=j` and

$$
{T-q/2\over D}<2s_0+1/j.
$$

Audited-working §142 supplies the reverse lower bound, so the selected sequence would
satisfy (SG.3), already excluded. This proves (SG.2).

---

## 4. Immediate propagation through the current Type-II stack

The exact stopped-train ledger is

$$
T-q=2f-k,
\qquad k=d_H+s_Z.
\tag{SG.14}
$$

The convex loaded hull has `q<=pi D`. Therefore

$$
\begin{aligned}
{T-q\over D}
&={T-q/2\over D}-{q\over2D}\\
&\ge2s_0+\epsilon_{SG}-\pi/2,
\end{aligned}
$$

so, with

$$
\gamma:=2s_0-\pi/2
=0.333829286933018\ldots,
$$

$$
\boxed{
\liminf {2f-k\over D}
\ge\gamma+\epsilon_{SG}.
}
\tag{SG.15}
$$

This strictly improves audited-working §142.9.

### 4.1 Strict improvement of the §146 weighted density surface

From

$$
T=h-s_Z+2f,
\qquad q=h+d_H,
$$

(SG.2) gives

$$
{f\over D}
\ge
s_0+{\epsilon_{SG}\over2}
-{1\over4}{h\over D}
+{1\over4}{d_H\over D}
+{1\over2}{s_Z\over D}
-o(1).
\tag{SG.16}
$$

The same outer-walk inequality used in §146 is

$$
{Q\over D}+2{s_Z\over D}
\le2{h\over D}-\pi+o(1),
\qquad Q\ge f.
\tag{SG.17}
$$

Combining (SG.16)–(SG.17) yields

$$
\boxed{
\liminf {1\over D}
\left(
 h-{d_H\over9}-{10s_Z\over9}
\right)
\ge
C_{146}+{2\epsilon_{SG}\over9},
}
\tag{SG.18}
$$

where

$$
C_{146}={4\over9}(\pi+s_0).
$$

Thus the weighted §146 endpoint is not merely unattainable; its strict separation is a
formal corollary of the stronger train-phase gap.

### 4.2 Strict improvement of the triangular-tooth defect floor

Audited-working §152 has

$$
q-T_{\triangle}\ge f+2k
={1\over2}(2f-k)+{5\over2}k.
$$

Using (SG.15),

$$
\boxed{
\liminf {q-T_{\triangle}\over D}
\ge
{\gamma+\epsilon_{SG}\over2}
+{5\over2}\liminf{k\over D}
}
\tag{SG.19}
$$

in the corresponding fixed-subsequence form. In particular the current universal
`0.1669146434...D` tooth-loss coefficient improves by `epsilon_SG/2`.

### 4.3 Bounded defect-face transport also improves

Every use of §142.9 in the bounded-degree defect-face theorem §143 may replace
`gamma` by `gamma+epsilon_SG`. Hence the linear low-degree face population has a
strictly larger coefficient as well.

---

## 5. Scope

- The theorem is proof-only and depends on audited-working §142, not on §146 or the
  carrier-decimal endpoint.
- The signed-monotone near-complete train lemma is supplied and hostile-audited by the
  companion files on this branch.
- No disk hypothesis, exact biclique extraction, KKT coefficient floor, or source-point
  deletion is used.
- Contact-isolated source points remain outside the core affine-kernel statement.
- `epsilon_SG` is qualitative. A quantitative value would require a finite stability
  modulus for the phase-measure equality and near-Mantel steps.
- The theorem still does not close the full Type-II branch by itself. It creates a
  uniform strict gap in the stopped-train/phase currency that every surviving Type-II
  configuration must pay.

**Disposition:** proof-only theorem pending independent review. C-II remains open.

> Generated reading edition · [exact source](../../../docs/reports/target_c_wegner_attachment_cell_correction_2026-09-09.md) · source SHA-256 `bbfab93f53cf9b6f79750a54dfb1fe6224749f2316c8712145888d9449a50433`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-BF6A5D95D4CF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Wegner boundary-order correction for harmonic attachment cells

**Date:** 2026-09-09  
**Repository base:** `cf790155660ad46797e53c7f44371b078f7eab7b` plus AR on this branch  
**Run type:** external finite-packing theorem import / exact rescaling / Target C cell application  
**Target:** Target C C-II after ZF; especially AR/UF near-circle phase  
**Depends on:** C36, C44, C49, AR; Oler; Wegner's finite circle-packing inequality  
**Computation:** only displayed decimal evaluation; not used in proofs

## LEVEL I STATUS

`STILL OPEN`

The repository bibliography already contains Böröczky--Ruzsa's 2007 note on Wegner's inequality, but the Wegner bound has not been inserted into the Target C harmonic-cell capacity chain.

After exact rescaling from nonoverlapping unit disks to point sets of minimum separation one, Wegner gives a boundary-order correction to Oler. Applied cellwise, it yields a new dichotomy:

- either the total unloaded-component graph diameter `S=sum_r delta_r` is strictly larger than the AR leading-order floor; or
- the harmonic cells carry a positive linear **Wegner correction** that Oler does not see.

At the UF crossover `zeta_*=0.5572837714...`, AR alone gives

`S/D >= 0.6208918647...`.

If the total Wegner correction is sublinear, the strengthened theorem gives instead

`S/D >= 0.6519831092...`.

Conversely, if `S/D` remains at the AR floor, the normalized raw Wegner correction is at least `0.0976760...D`, producing an explicit extra area charge of about `0.00654305D` beyond Oler.

This is boundary-order progress, not a Level I closure.

---

## 1. Literature input and exact rescaling

Böröczky and Ruzsa quote Wegner's theorem in the following form for `N>=2` nonoverlapping unit disks. If `D_disk` is the convex hull of the disks, then

```math
\operatorname{area}(D_{disk})
\ge
2\sqrt3(N-1)
+(2-\sqrt3)W_N
+\pi,
\tag{WG.1}
```

where

```math
\boxed{
W_N:=\left\lceil\sqrt{12N-3}-3\right\rceil.
}
\tag{WG.2}
```

Equality is characterized by Wegner packings. The exact source is:

K. J. Böröczky and I. Z. Ruzsa, *Note on an Inequality of Wegner*, Discrete & Computational Geometry 37 (2007), 245--249, DOI `10.1007/s00454-006-1277-4`; the repository already indexes this source as `BoroczkyRuzsa2007` and archives the PDF under `papers/related/`.

Let `K` now be the convex hull of `N` planar points with minimum pairwise distance one. Scale by two. The scaled center hull is `2K`, and the corresponding unit disks are nonoverlapping. Steiner's formula gives

```math
\operatorname{area}(2K+B_1)
=4\operatorname{area}(K)+2\operatorname{per}(K)+\pi.
```

Insert this into WG.1, cancel `pi`, and divide by four.

### Theorem WG.1 — rescaled Wegner inequality

For every convex hull `K` of `N>=2` unit-separated planar points,

```math
\boxed{
\operatorname{area}(K)+\frac12\operatorname{per}(K)
\ge
\frac{\sqrt3}{2}(N-1)
+\frac{2-\sqrt3}{4}W_N.
}
\tag{WG.3}

```

Put

```math
a_0:=\frac{\sqrt3}{2},
\qquad
c_W:=\frac{2-\sqrt3}{4}.
\tag{WG.4}
```

The Oler inequality in the same normalization is

```math
\operatorname{area}(K)+\frac{a_0}{2}\operatorname{per}(K)
\ge a_0(N-1).
\tag{WG.5}
```

Because

```math
\frac12-\frac{a_0}{2}=c_W,
```

WG.3 is exactly

```math
\operatorname{area}(K)
\ge
a_0(N-1)-\frac{a_0}{2}P
+c_W(W_N-P).
\tag{WG.6}
```

Taking the better of WG.5 and WG.6 gives the useful combined theorem.

### Corollary WG.2 — Oler plus Wegner correction

```math
\boxed{
\operatorname{area}(K)
\ge
 a_0(N-1)-\frac{a_0}{2}P
+c_W[W_N-P]_+,
}
\tag{WG.7}
```

where `P=per(K)` and `[x]_+=max{x,0}`.

Thus Wegner improves Oler exactly when `W_N>P`; there is no hidden comparison of unrelated constants.

---

## 2. Apply WG.7 to one harmonic attachment cell

Use the AR/C36/C49 notation. For an unloaded component `I_r`, let

```math
n_r=|I_r|,
\qquad
A_r\subset B_+,
\qquad
a_r=|A_r|\ge3,
```

and

```math
P_r=\operatorname{conv}A_r.
```

The unit-separated point set

```math
X_r=I_r\cup A_r
```

lies in `P_r` and has

```math
N_r=n_r+a_r.
\tag{2.1}
```

C44 gives

```math
\operatorname{diam}P_r
=\operatorname{diam}A_r
\le\delta_r+2,
```

so the convex perimeter-diameter bound gives

```math
\operatorname{per}(P_r)
\le\pi(\delta_r+2).
\tag{2.2}
```

Define the raw cellwise Wegner excess

```math
\boxed{
E_r:=
\left[W_{N_r}-\pi(\delta_r+2)\right]_+.
}
\tag{2.3}
```

Since the positive-part function is monotone and `per(P_r)<=pi(delta_r+2)`, WG.7 yields

```math
\operatorname{area}(P_r)
\ge
 a_0(N_r-1)
-\frac{a_0\pi}{2}(\delta_r+2)
+c_WE_r.
\tag{2.4}
```

Using `a_r>=3` gives the convenient coarser form

```math
\boxed{
\operatorname{area}(P_r)
\ge
 a_0n_r
-\frac{a_0\pi}{2}\delta_r
-a_0(\pi-2)
+c_WE_r.
}
\tag{WG.8}
```

This is exactly the AR Oler lower bound plus a nonnegative certified boundary-order correction.

---

## 3. Finite corrected attachment-fill inequality

Put

```math
S:=\sum_r\delta_r,
\qquad
E_W:=\sum_rE_r.
```

C49 gives pairwise interior-disjoint attachment cells, and AR uses the isodiametric upper bound

```math
\sum_r\operatorname{area}(P_r)
\le
\frac\pi4(S^2+4S+4c_I).
\tag{3.1}
```

Sum WG.8 and compare with (3.1).

### Theorem WG.3 — corrected AR inequality

```math
\boxed{
 a_0(v-q)+c_WE_W
\le
\frac\pi4S^2
+\pi\left(1+\frac{a_0}{2}\right)S
+\bigl[\pi+a_0(\pi-2)\bigr]c_I.
}
\tag{WG.9}
```

AR is recovered by discarding `c_W E_W`.

The correction is only linear-scale in the regimes presently known, so it does not change AR's quadratic leading coefficient. It is valuable because the final Erdős #99 obstruction is itself at boundary order after the leading packing density cancels.

---

## 4. A second exact population/diameter inequality

The definition of `W_N` and `E_r` contains additional information independent of area.

Since

```math
W_{N_r}
\le
\pi(\delta_r+2)+E_r
\tag{4.1}
```

and

```math
\sqrt{12N_r-3}-3
\le W_{N_r},
\tag{4.2}
```

we have

```math
12N_r-3
\le
\bigl(\pi\delta_r+E_r+2\pi+3\bigr)^2.
\tag{4.3}
```

Let

```math
c:=2\pi+3.
```

Summing (4.3), using

```math
\sum_r\delta_r^2\le S^2,
\qquad
\sum_rE_r^2\le E_W^2,
\qquad
\sum_r\delta_rE_r\le SE_W,
```

and `v-q=sum n_r <=sum N_r`, gives the finite theorem

### Theorem WG.4 — population versus component diameter plus Wegner excess

```math
\boxed{
12(v-q)
\le
(\pi S+E_W)^2
+2c(\pi S+E_W)
+(c^2+3)c_I.
}
\tag{WG.10}
```

No area estimate enters WG.10 after the definition of `E_r`; it is a direct consequence of the integer Wegner boundary term.

---

## 5. Asymptotic dichotomy

Along an unbounded post-ZF subsequence suppose

```math
\frac v{D^2}\to r,
\qquad
\frac SD\to s,
\qquad
\frac{E_W}{D}\to\varepsilon
```

after extracting further if necessary. The post-ZF bounds `q,c_I=O(D)` make the lower-order terms in WG.10 vanish after division by `D^2`. Therefore

```math
\boxed{
\sqrt{12r}
\le
\pi s+\varepsilon.
}
\tag{WG.11}
```

Equivalently,

```math
\boxed{
\varepsilon
\ge
[\sqrt{12r}-\pi s]_+.
}
\tag{WG.12}
```

### Corollary WG.5 — sublinear Wegner correction strengthens AR

If

```math
E_W=o(D),
```

then

```math
\boxed{
\liminf\frac SD
\ge
\frac{\sqrt{12r}}\pi.
}
\tag{WG.13}
```

Compare AR:

```math
\liminf\frac SD
\ge
\sqrt{\frac r\Delta},
\qquad
\Delta=\frac\pi{2\sqrt3}.
```

Since

```math
\frac{\sqrt{12}}\pi
>
\sqrt{\frac{2\sqrt3}{\pi}},
```

WG.13 is strictly stronger whenever `r>0`.

---

## 6. UF near-circle specialization

In the PR #119 UF parameterization,

```math
r=\Delta-\zeta.
```

Thus if `E_W=o(D)`, WG.13 gives

```math
\boxed{
\liminf\frac SD
\ge
\frac{\sqrt{12(\Delta-\zeta)}}\pi.
}
\tag{WG.14}
```

At the UF worst crossover

```math
\zeta_*=0.5572837714\ldots,
```

this evaluates to

```math
\boxed{
\liminf\frac SD
\ge0.6519831092\ldots,
}
\tag{WG.15}
```

instead of the AR floor

```math
0.6208918647\ldots .
```

Conversely, if `S/D` approaches the AR floor at this same `zeta_*`, WG.12 forces

```math
\boxed{
\liminf\frac{E_W}{D}
\ge0.0976760251\ldots .
}
\tag{WG.16}
```

and WG.9 therefore contains the extra boundary-order cell-area term

```math
\boxed{
 c_WE_W
\ge
(0.0065430530\ldots-o(1))D.
}
\tag{WG.17}
```

This gives an explicit currency for the failure of the stronger component-diameter floor.

---

## 7. Bounded exceptional faces receive the same correction

Let `F` be a bounded contact face of degree `k` containing `z` contact-isolated source points. C51 makes `F` a strict convex unit-edge polygon, so its `k` boundary vertices together with the `z` interior points form `N=k+z` unit-separated points whose convex hull is exactly `F` and whose perimeter is `k`.

WG.7 gives the exact facewise capacity bound

```math
\boxed{
\operatorname{area}(F)
\ge
 a_0(k+z-1)
-\frac{a_0}{2}k
+c_W[W_{k+z}-k]_+.
}
\tag{WG.18}
```

The DP pentagon regression is respected: for `k=5,z=0`, `W_5=5`, so the Wegner correction is exactly zero. Therefore WG does not falsely resurrect a uniform positive defect-face charge that the September 9 DP family already disproves.

When a macroscopic exceptional face carries a quadratic rattler population, however, `W_{k+z}` is itself linear in `D` and WG.18 can produce a genuine boundary-order strictness term.

---

## 8. What this advances and what it does not

WG adds the first source-specific boundary-order packing correction to the AR harmonic-cell theorem.

It proves:

1. exact Oler+Wegner improvement `c_W[W_N-P]_+` for any unit-separated center hull;
2. exact corrected attachment-fill inequality WG.9;
3. exact population/diameter/excess inequality WG.10;
4. an improved component-diameter floor whenever the correction is sublinear;
5. a quantitative positive linear correction whenever that stronger floor fails.

It does **not** yet convert the linear correction into the forbidden face sign. The correction is area/capacity currency, while the exact post-ZF closing defect is `-2s_Z`. A closing theorem must still couple `E_W` to `s_Z`, `Q`, or a finite same-diameter release.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| rescaled Wegner WG.3 | proved from published theorem | Steiner + scale factor two |
| Oler+Wegner correction WG.7 | proved | exact coefficient identity `1/2-a_0/2=c_W` |
| harmonic-cell correction WG.9 | proved | C36/C44/C49 + WG.7 |
| population inequality WG.10 | proved | integer `W_N` definition + Cauchy-type sums |
| sublinear correction -> stronger `S/D` floor | proved | WG.10 asymptotics |
| DP pentagon remains allowed | checked | `W_5=5` |
| Level I | still open | no proved coupling from `E_W` to `s_Z` or direct face sign |

---

## 10. Next target

The new boundary-order currency is

```math
E_W
=\sum_r[W_{N_r}-\pi(\delta_r+2)]_+.
```

The best next theorem is one of:

1. show that `E_W=Omega(D)` forces enough convex-cell area consumption to violate the UF near-circle source-capacity budget;
2. show that large `E_W` requires `Omega(D)` additional contact/face incidence and therefore raises `Q` beyond the post-ZF terminal budget;
3. sharpen WG.10 with the noncrossing C37 attachment geometry rather than the coarse inequalities `sum delta_r^2<=S^2`, `sum E_r^2<=E_W^2`.

The third route is particularly attractive: concentration of `S` into one cell and concentration of `E_W` into one cell are the extremizers of WG.10, but C37/C35 may prevent those two concentrations from coexisting with the almost-complete loaded hull cycle in the UF branch.

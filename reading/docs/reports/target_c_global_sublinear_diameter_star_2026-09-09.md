> Generated reading edition · [exact source](../../../docs/reports/target_c_global_sublinear_diameter_star_2026-09-09.md) · source SHA-256 `6347de6b6160e616924a04641683de1613e682d2b6c3b1e629abac4c457607be`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-E9C95EF05384","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_global_sublinear_diameter_star_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=6b017a681ee275db985c2a5f54e519c48f358e8a; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — every large global minimizer has sublinear diameter-star degree

**Date:** 2026-09-09  
**Repository branch:** `research/post-uf-attachment-fill-2026-09-09`  
**Run type:** global finite-packing stability consequence  
**Target:** diameter-graph geometry, usable in Target C after C65  
**Depends on:** strict translated-lattice comparison, Oler, isodiametric inequality, planar quantitative isodiametric stability of Maggi--Ponsiglione--Pratelli  
**External source:** F. Maggi, M. Ponsiglione, A. Pratelli, *Quantitative stability in the isodiametric inequality via the isoperimetric inequality*, Trans. Amer. Math. Soc. 366 (2014), 1141--1160, arXiv:1104.4074.  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The existing C18 theorem gives a universal linear bound on the degree of one diameter star. The global packing inequalities imply a much stronger asymptotic statement before any Target C near-circle branch is selected.

Let `A` be any global `n`-point minimum-diameter unit-separated source, let

```math
D=D(n),
\qquad
K=\operatorname{conv}A,
```

and let `H_all` be its complete actual diameter graph.

Then

```math
\boxed{
\Delta(H_{all})=O(D^{3/4}).
}
\tag{GD.1}

```

In particular

```math
\boxed{
\Delta(H_{all})/D\to0.
}
\tag{GD.2}

```

This holds for every sufficiently large global minimizer, with or without the triangle-free hypothesis. In the C65 normalization, `H_all=H`, so it applies directly to the complete KKT-visible diameter support.

The result gives the first source-wide sublinear diameter-star bound in the current stack. It does not control diameter weights and therefore does not by itself eliminate the stress-star degeneration.

---

## 1. The full source hull has only `O(D)` isodiametric area deficit

Put

```math
a_0:=\frac{\sqrt3}{2},
\qquad
\Delta:=\frac\pi{2\sqrt3}.
```

The strict translated-lattice comparison used throughout the repository gives

```math
D^2<\frac{2\sqrt3}{\pi}(n-1),
```

or equivalently

```math
\boxed{n-1>\Delta D^2.}
\tag{1.1}
```

Oler applied to the full source hull gives

```math
a_0(n-1)
\le
\operatorname{area}(K)
+\frac{a_0}{2}\operatorname{per}(K).
\tag{1.2}
```

The convex perimeter-diameter inequality gives

```math
\operatorname{per}(K)\le\pi D.
\tag{1.3}
```

Because

```math
a_0\Delta=\frac\pi4,
```

(1.1)--(1.3) imply

```math
\operatorname{area}(K)
>
\frac\pi4D^2
-\frac{a_0\pi}{2}D.
\tag{1.4}
```

The isodiametric inequality supplies the opposite bound

```math
\operatorname{area}(K)\le\frac\pi4D^2.
```

Therefore the full source hull satisfies the finite deficit estimate

```math
\boxed{
0\le
\frac\pi4D^2-\operatorname{area}(K)
<
\frac{\pi\sqrt3}{4}D.
}
\tag{GD.3}

```

No triangle-free, KKT, or contact-graph hypothesis is used.

---

## 2. Relative isodiametric deficit is `O(1/D)`

Normalize the area deficit by the disk of diameter `D`:

```math
\delta_{iso}(K)
:=
1-
\frac{4\operatorname{area}(K)}{\pi D^2}.
```

GD.3 gives immediately

```math
\boxed{
0\le\delta_{iso}(K)<\frac{\sqrt3}{D}.
}
\tag{2.1}

```

Thus every global minimizer is quantitatively near the equality case of the planar isodiametric inequality at rate `D^{-1}` in relative area.

---

## 3. Quantitative isodiametric stability

Maggi--Ponsiglione--Pratelli prove in the planar case that, after translating a set of fixed diameter, its Hausdorff distance from the equal-diameter disk is bounded by a dimensional constant times the square root of the isodiametric deficit.

Applying their theorem to the convex hull `K`, there is a center `c` and an absolute constant `C_0` such that

```math
\boxed{
 d_H\left(D^{-1}(K-c),B_{1/2}\right)
\le
C_0D^{-1/2}.
}
\tag{3.1}

```

Equivalently, with

```math
\rho:=C_0D^{-1/2},
```

the normalized source hull lies within a `rho` Hausdorff neighborhood of the radius-`1/2` disk.

The exact constant is irrelevant for the exponent below.

---

## 4. Every diameter pair is `O(D^{-1/4})` from antipodal

Let `u,v in A` satisfy

```math
|u-v|=D.
```

Every diameter endpoint is an extreme point of `K`. Normalize around the center from (3.1):

```math
x=\frac{u-c}{D},
\qquad
y=\frac{v-c}{D}.
```

Then

```math
|x-y|=1
```

and

```math
|x|,|y|\le\frac12+\rho.
```

Write the angle between `x` and `y` as

```math
\pi-\phi,
\qquad
0\le\phi\le\pi.
```

For fixed angular separation, the distance is maximized by taking both radii equal to `1/2+rho`. Hence

```math
1=|x-y|
\le
(1+2\rho)\cos\frac\phi2.
\tag{4.1}
```

Therefore

```math
\cos\frac\phi2
\ge
\frac1{1+2\rho}.
```

For sufficiently small `rho`, the elementary bound `1-cos t >= c t^2` on a fixed neighborhood of zero yields

```math
\boxed{
\phi\le C_1\sqrt\rho
=O(D^{-1/4}).
}
\tag{4.2}

```

uniformly over **all** diameter pairs.

Thus every actual diameter pair is uniformly within `O(D^{-1/4})` angular error of antipodality with respect to one common near-disk center.

---

## 5. One diameter star has angular width `O(D^{-1/4})`

Fix one diameter vertex `z` and let

```math
a_1,\ldots,a_m
```

be all of its diameter partners.

By (4.2), every normalized partner direction around the common source center lies in the same `O(D^{-1/4})` neighborhood of the antipode of `z`.

The vectors from `z` to its partners therefore lie in a cone of angular width

```math
\boxed{O(D^{-1/4}).}
\tag{5.1}
```

A direct coordinate argument avoids any ambiguity between polar angle and the star angle: both `z` and every `a_i` lie `O(D^{1/2})` in absolute distance from the appropriate circle points, while `|z-a_i|=D`; perturbing two endpoints by `O(D^{1/2})` changes the direction of their length-`D` chord by `O(D^{-1/2})`, which is smaller than the already sufficient `O(D^{-1/4})` bound.

---

## 6. Unit separation of partners gives the degree bound

Every partner `a_i` lies on the Euclidean circle of radius `D` centered at `z`, because

```math
|z-a_i|=D.
```

Distinct partners are distinct source points and satisfy

```math
|a_i-a_j|\ge1.
```

If their angular separation at `z` is `theta`, then

```math
2D\sin\frac\theta2\ge1,
```

so

```math
\theta
\ge
2\arcsin\frac1{2D}
\ge
\frac{c}{D}
```

for an absolute `c>0` and all large `D`.

Packing angularly `c/D`-separated partner rays into the star cone (5.1) gives

```math
\deg_{H_{all}}(z)
\le
C_2D^{3/4}+1.
```

Taking the maximum over `z` proves GD.1.

---

## 7. Consequences for Target C

In the C65 lexicographic normalization every actual diameter pair is KKT-visible, so

```math
H=H_{all}.
```

Hence every post-C65 survivor satisfies

```math
\boxed{\Delta(H)=O(D^{3/4}).}
\tag{7.1}
```

This strengthens C18's universal bound

```math
\Delta(H)\le(0.885943\ldots+o(1))D.
```

Several immediate support consequences follow.

### 7.1 Any linear family of diameter incidences needs polynomially many centers

If `X subseteq B_+` has at least `cD` incident diameter edges leaving `X`, then the opposite endpoint set has cardinality at least

```math
\boxed{\Omega(D^{1/4}).}
\tag{7.2}
```

because each opposite terminal receives at most `O(D^{3/4})` such edges.

### 7.2 The LC macroscopic attachment block has at least polynomially many opposite carriers

For the PR #128 LC giant component with

```math
|A_*|\ge cD
```

and normalized cell diameter `<1`, no diameter edge has both endpoints in `A_*`. Every `a in A_*` is a diameter endpoint by C65 and therefore has a diameter edge leaving the block. Thus

```math
\boxed{|N_H(A_*)|=\Omega(D^{1/4}).}
\tag{7.3}
```

This removes the need to assume `x_B=o(D)` merely to obtain a diverging carrier family; the polynomial lower bound comes from the full source hull.

### 7.3 Diameter stress may still concentrate

GD is a support theorem. It does not give

- a lower bound on any `beta_h`;
- a lower bound on total beta mass carried by a specified number of stars;
- a conductance floor for the response matrix.

A stress may place almost all normalized diameter weight on `O(D^{3/4})` edges of one star while assigning arbitrarily tiny positive weight to the remaining actual diameter support. Thus the C66/C71 coefficient-degeneration regression survives.

---

## 8. Relation to the older global perimeter theorem

The post-synthesis report already proves the full source hull has perimeter

```math
\pi D-O(1)
```

and uniform width `D-o(D)`. GD is complementary: it uses the **area** closeness forced directly by Oler plus global density and then invokes quantitative isodiametric stability to obtain one common near-disk center and a rate strong enough to control every exact diameter star.

No claim is made that the exponent `3/4` is optimal. Combining the stronger global perimeter information with a sharper source-specific stability theorem may improve it.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| full hull area deficit `<pi sqrt(3) D/4` | proved | strict lattice count + Oler + `P<=pi D` |
| relative deficit `<sqrt(3)/D` | proved | normalization |
| normalized Hausdorff disk error `O(D^-1/2)` | external theorem | planar Maggi--Ponsiglione--Pratelli stability |
| diameter antipodal error `O(D^-1/4)` | proved | exact diameter in near-disk annulus |
| `Delta(H_all)=O(D^{3/4})` | proved | unit separation on a radius-`D` star circle |
| linear opposite-carrier count | not proved | exponent still allows large sublinear stars |
| Level I | still open | coefficient concentration remains |

---

## 10. Next target

The source-wide exponent can likely be improved because the repository already has the much stronger perimeter estimate

```math
\pi D-\operatorname{per}(K)=O(1).
```

A direct stability theorem for convex bodies simultaneously near equality in perimeter-diameter and isodiametric area may give Hausdorff error `O(1)` or `O(D^alpha)` with `alpha<1/2`, improving the star exponent.

Even `Delta(H)=O(D^{1/2})` would force `Omega(D^{1/2})` distinct opposite carriers for every LC block. A uniform `O(1)` star bound would create a linear diameter matching and would interact strongly with ZT/NM.

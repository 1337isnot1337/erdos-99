> Generated reading edition · [exact source](../../../../docs/targets/target-c/92-wrapping-perimeter-diameter-audit.md) · source SHA-256 `a7454eadb551c139212b67531f6f5b0f68cbc496e627a22bed699e112c38bb54`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 12 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

# Target C — attachment perimeter raises the wrapping-cell diameter threshold

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

Canonical `C-HARMONIC-WRAPPING` proves that every wrapping Type-II harmonic-cell limit has normalized diameter at least

```math
\mu_0=0.889670810115\ldots
```

by comparing the number of loaded attachments required by harmonic trapping with the number that fit in the six angular clusters allowed by a wrapping circle support.

That argument does not use a second canonical constraint on the same attachment set. Canonical `C-HARMONIC-CARRIER-QUAD` gives an exact local face identity, and it implies that the convex attachment polygon cannot have large perimeter on too few attachments:

```math
\operatorname{per}(P)\le4|A|-6.
```

A wrapping support on the limiting radius-`1/2` circle has a definite perimeter floor. Combining that floor with the Section-88 six-cluster attachment upper bound raises the rigorous wrapping threshold to

```math
\boxed{
\mu_1=0.914487471642\ldots
}
```

where `mu_1` is the unique root of

```math
\boxed{
6\arcsin\mu-2\pi
={\mu\over2}\left(1+\sqrt{1-\mu^2}\right).
}
```

The same replacement propagates through the Section-88 cap-capacity argument: in the Type-II branch there is one locally rhombus-saturated macroscopic harmonic cell of diameter at least `(mu_1-o(1))D`.

No Fox--Pach theorem, Section 90, or Section 91 is used.

---

# 92. Harmonic wrapping plus attachment perimeter forces diameter at least 0.914487 D

## 92.1 Finite attachment-perimeter capacity from the canonical local ledger

Fix one unloaded harmonic component `I_r` with attachment set

```math
A=A_r,\qquad a=|A|,\qquad P=\operatorname{conv}(A).
```

Use the canonical Section-82 notation for the induced contact graph on `I_r union A`:

- `L` is the outer-face walk length, counting edge occurrences;
- `Q>=0` is the bounded-face degree excess;
- `s>=0` is the local pinned surplus;
- `c>=0` is the number of loaded-loaded contacts whose endpoints both lie in `A`.

Canonical Section 82 gives exactly

```math
\boxed{L+Q=4a-6-2s-2c.}
\tag{92.1}
```

Every edge in the outer-face walk is a unit contact edge, so its Euclidean length is exactly one and the geometric walk has length `L`. Every attachment vertex is extreme in `P`, hence appears on the outer face of the induced plane graph; all other induced vertices lie in `P`. Therefore the convex hull of the geometric outer walk is exactly `P`.

For every closed polygonal walk, Cauchy's width formula or projection variation gives

```math
\operatorname{per}(\operatorname{conv}\gamma)
\le \operatorname{length}(\gamma).
```

Thus

```math
\operatorname{per}(P)\le L.
\tag{92.2}
```

Combining (92.1), `Q,s,c>=0`, and (92.2) yields the finite local theorem

```math
\boxed{
\operatorname{per}(P)
\le L
\le4a-6.
}
\tag{92.3}
```

Equivalently,

```math
\boxed{
a\ge{\operatorname{per}(P)+6\over4}.}
\tag{92.4}
```

The sharper finite form

```math
\operatorname{per}(P)+Q+2s+2c\le4a-6
\tag{92.5}
```

will remain available, although only (92.4) is needed below.

## 92.2 Minimum perimeter of a wrapping circle-supported cell

Work with the normalized radius-`1/2` circle. Let `S` be a compact subset of that circle such that

```math
\operatorname{diam}(S)=\lambda<1
```

and `S` is wrapping, meaning it is not contained in an open semicircle. Put

```math
\theta:=2\arcsin\lambda\in[2\pi/3,\pi).
\tag{92.6}
```

Because `S` has no antipodal pair, wrapping implies that the origin lies in the interior of the convex hull of three points `y_1,y_2,y_3 in S`. Put them in cyclic order and let their circle gaps be

```math
g_1,g_2,g_3\in(0,\pi),
\qquad
g_1+g_2+g_3=2\pi.
\tag{92.7}
```

Each pair of anchors belongs to `S`, so every minor angular separation is at most `theta`. Since each `g_i<pi`,

```math
0<g_i\le\theta.
\tag{92.8}
```

On the radius-`1/2` circle, the chord spanning angular gap `g` has length

```math
\sin(g/2).
```

Therefore the anchor triangle has perimeter

```math
p(g_1,g_2,g_3)
=\sum_{i=1}^3\sin(g_i/2).
\tag{92.9}
```

### Lemma 92.1 — sharp three-anchor perimeter floor

Under (92.7)--(92.8),

```math
\boxed{
\sum_{i=1}^3\sin(g_i/2)
\ge
2\lambda+2\lambda\sqrt{1-\lambda^2}.
}
\tag{92.10}
```

### Proof

Put `x_i=g_i/2` and `alpha=theta/2`. Then

```math
0<x_i\le\alpha<\pi/2,
\qquad
x_1+x_2+x_3=\pi.
```

The function `sin x` is concave on `[0,pi/2]`. On the compact closure of this feasible polytope a concave function attains its minimum at an extreme point. Because `2alpha<pi`, no extreme point can have one coordinate zero: the other two would then have sum `pi` while each is at most `alpha<pi/2`. Hence an extreme point has two coordinates equal to `alpha`, with the third equal to `pi-2alpha`.

Thus

```math
\sum_i\sin x_i
\ge
2\sin\alpha+\sin(\pi-2\alpha).
```

Now `sin alpha=lambda` and

```math
\sin(2\alpha)
=2\lambda\sqrt{1-\lambda^2},
```

which gives (92.10). `square`

Since the anchor triangle lies in `conv(S)` and convex perimeter is monotone under inclusion,

```math
\boxed{
\operatorname{per}(\operatorname{conv}S)
\ge
p_{wrap}(\lambda)
:=2\lambda\left(1+\sqrt{1-\lambda^2}\right).
}
\tag{92.11}
```

The floor is attained by the three-anchor gap pattern

```math
(\theta,\theta,2\pi-2\theta)
```

at the level of the anchor triangle. No assertion is made that a harmonic attachment set can realize equality simultaneously in the other inequalities below.

## 92.3 Combine perimeter capacity with the six-cluster attachment ceiling

Let `P_j=conv(A_j)` be a sequence of Type-II harmonic cells with

```math
{d_j\over D_j}\to\lambda<1
```

and suppose the normalized attachment sets converge in the Hausdorff hyperspace to a wrapping set `S` on the radius-`1/2` circle.

Convex-hull continuity gives

```math
D_j^{-1}P_j\to\operatorname{conv}(S).
```

Planar convex perimeter is continuous under Hausdorff convergence, so (92.4) and (92.11) imply

```math
\boxed{
\liminf_{j\to\infty}{|A_j|\over D_j}
\ge
{1\over4}p_{wrap}(\lambda)
={\lambda\over2}\left(1+\sqrt{1-\lambda^2}\right).
}
\tag{92.12}
```

Canonical Section 88 independently proves, for every wrapping cell limit,

```math
\boxed{
\limsup_{j\to\infty}{|A_j|\over D_j}
\le
6\arcsin\lambda-2\pi.
}
\tag{92.13}
```

Therefore every wrapping harmonic-cell limit must satisfy

```math
\boxed{
6\arcsin\lambda-2\pi
\ge
{\lambda\over2}\left(1+\sqrt{1-\lambda^2}\right).
}
\tag{92.14}
```

This strictly strengthens the Section-88 inequality

```math
6\arcsin\lambda-2\pi\ge\lambda/3.
```

## 92.4 The new sharp scalar threshold

Define

```math
H_1(\lambda)
:=6\arcsin\lambda-2\pi
-{\lambda\over2}\left(1+\sqrt{1-\lambda^2}\right).
\tag{92.15}
```

On `[sqrt(3)/2,1)`, put `s=sqrt(1-lambda^2) in (0,1/2]`. The derivative of the perimeter term is

```math
{d\over d\lambda}
\left[{\lambda\over2}(1+s)\right]
={1+2s-1/s\over2}
\le0,
\tag{92.16}
```

because

```math
1+2s-{1\over s}
={ (2s-1)(s+1)\over s}\le0.
```

Meanwhile

```math
{d\over d\lambda}(6\arcsin\lambda-2\pi)
={6\over s}>0.
```

Hence

```math
H_1'(\lambda)>0
\tag{92.17}
```

throughout the interval. At the lower endpoint,

```math
H_1(\sqrt3/2)=-{3\sqrt3\over8}<0,
\tag{92.18}
```

while

```math
\lim_{\lambda\uparrow1}H_1(\lambda)=\pi-{1\over2}>0.
\tag{92.19}
```

Thus there is a unique root `mu_1` in `(sqrt(3)/2,1)` satisfying

```math
\boxed{
6\arcsin\mu_1-2\pi
={\mu_1\over2}\left(1+\sqrt{1-\mu_1^2}\right).
}
\tag{92.20}
```

Numerically,

```math
\boxed{
\mu_1=0.914487471642104\ldots
}
\tag{92.21}
```

and therefore

```math
\boxed{
\text{every wrapping harmonic-cell limit has diameter at least }\mu_1.
}
\tag{92.22}
```

This raises the canonical Section-88 wrapping threshold by about `0.02481666 D` at leading order.

## 92.5 Propagate the improved threshold through the Section-88 cap argument

Fix any

```math
\mu<\mu_1.
```

By (92.22), every macroscopic Type-II harmonic-cell limit of normalized diameter at most `mu` is cap type. The remainder of canonical Section 88's short-cell capacity proof uses only that cap-type conclusion, pairwise interior-disjointness of the harmonic cells, and the near-disk limit. It therefore applies unchanged with `mu_1` replacing `mu_0`.

Writing

```math
\theta_\mu=2\arcsin\mu,
\qquad
k_\mu=\left\lfloor{2\pi\over\theta_\mu}\right\rfloor,
\qquad
r_\mu=2\pi-k_\mu\theta_\mu,
```

and

```math
\mathcal C(\mu)
={1\over8}\left[2\pi-k_\mu\sin\theta_\mu-\sin r_\mu\right],
\tag{92.23}
```

one has

```math
\boxed{
\limsup {1\over D^2}
\sum_{d_r\le\mu D}\operatorname{area}(P_r)
\le\mathcal C(\mu)<{\pi\over4}.
}
\tag{92.24}
```

Thus cells with `d_r>mu D` carry asymptotic area at least

```math
\Gamma(\mu)D^2-o(D^2),
\qquad
\Gamma(\mu):={\pi\over4}-\mathcal C(\mu)>0.
\tag{92.25}
```

The canonical total attachment-cell perimeter bound makes the number of such long cells uniformly bounded for fixed `mu`. Hence one has area `Omega_mu(D^2)`. The canonical summed local rhombic deficit is `o(D^2)`, so a maximizing long cell is locally rhombus-saturated.

At the new endpoint,

```math
\mathcal C(\mu_1)=0.4759596127\ldots,
\qquad
\Gamma(\mu_1)=0.3094385507\ldots>0.
\tag{92.26}
```

Therefore `Gamma(mu)` remains uniformly positive as `mu` increases to `mu_1`. A diagonal choice `mu_j -> mu_1` gives one sequence of actual harmonic cells `P_*` such that

```math
\boxed{
{\operatorname{diam}(P_*)\over D}\ge\mu_1-o(1),
\qquad
\operatorname{area}(P_*)\ge c_1D^2,
\qquad
{A_{4,*}\over\operatorname{area}(P_*)}\to1
}
\tag{92.27}
```

for one absolute `c_1>0`.

Hence the canonical Type-II carrier threshold can be strengthened from

```math
0.8896708101\ldots D-o(D)
```

to

```math
\boxed{0.9144874716\ldots D-o(D).}
\tag{92.28}
```

## 92.6 Equality and next obstruction

The new scalar root is not asserted to be attainable. Equality in (92.14) would simultaneously require, at leading order,

1. the attachment outer walk to saturate the convex-perimeter inequality;
2. `Q,s,c=o(D)` in the local face ledger relative to the linear scale;
3. the wrapping support to attain the minimum three-anchor perimeter pattern `(theta,theta,2pi-2theta)`; and
4. the actual attachments to saturate the six-cluster unit-separation capacity from Section 88.

Those conditions are mutually restrictive. In particular, saturation of the six-cluster count should force positive attachment occupancy throughout the admissible cluster arcs, while saturation of the wrapping perimeter floor uses only three extreme anchors. A quantitative incompatibility between those two equality geometries would raise the threshold again or exclude convergence to `mu_1` by compactness.

That endpoint-stability problem is now the clean next geometric target. It is independent of the Section-90/91 ordered-grid route and can be pursued in parallel.

## 92.7 Dependency and regression audit

- **Canonical `C-HARMONIC-CARRIER-QUAD` / Section 82:** exact local identity `L+Q=4a-6-2s-2c`, harmonic-cell convexity, and attachment extremality.
- **Canonical `C-HARMONIC-WRAPPING` / Section 88:** Type-II annular convergence, wrapping six-cluster attachment upper bound, cap-family capacity, macroscopic long-cell selection, and local rhombic-deficit summability.
- **Canonical `C-HARMONIC-CELL-TILING` / Section 83:** pairwise cell interior-disjointness and summed local rhombic deficit used in the propagated carrier conclusion.
- **No dependency on Sections 90 or 91:** the perimeter argument is independent of the dense-grid route.
- **Old high-`mu` cap regression:** not used. Wrapping and cap-type supports remain separated exactly as in Section 88.
- **Contact-isolated source points:** untouched; the theorem concerns unloaded positive-contact harmonic components in the Type-II branch.
- **KKT coefficient floors:** not used.

**Status:** canonical; promoted by the independent Sections-90–94 audit.
**Theorem state:** `2026-09-11.audit.36`.

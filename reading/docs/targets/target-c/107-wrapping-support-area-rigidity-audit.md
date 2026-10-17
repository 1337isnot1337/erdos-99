> Generated reading edition · [exact source](../../../../docs/targets/target-c/107-wrapping-support-area-rigidity-audit.md) · source SHA-256 `805b0dc61f9a27c59980a8bbfe62e4cb216186e73218b108e0b02feb3c8dd403`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target C — wrapping support area rigidity

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proved candidate, proof-only pending independent hostile audit/promotion.

The current phase/corridor route uses the cap-deficit theorem to guarantee a wrapping
carrier of area at least about `0.19D^2`.  Near the Section-101 scalar endpoint, much
more area is already forced by the shape of the wrapping support itself.

For a compact wrapping support `S` on the radius-`1/2` circle, let `g_j` be the
connected angular gaps of its complement.  Since every gap has length below `pi`, the
convex hull loses from the half-radius disk exactly the disjoint circular segments over
those gaps.  Hence

```math
\boxed{
\operatorname{area}(\operatorname{conv}S)
={\pi\over4}-{1\over8}\sum_j(g_j-\sin g_j).
}
```

Combining this exact identity with the canonical Section-101 scalar chain gives a
strong quantitative consequence without using Sections 104--106 as premises:

> If a wrapping Type-II harmonic-cell limit has Section-101 scalar slack
> `sigma(theta)<=10^{-3}`, then, in normalized coordinates,
> ```math
> \boxed{\operatorname{area}(\operatorname{conv}S)>0.473.}
> ```
> Equivalently the finite carrier has
> ```math
> \boxed{\operatorname{area}(P_D)> (0.473-o(1))D^2.}
> ```

For a locally rhombus-saturated carrier this gives at least `0.473D^2-o(D^2)` strict
unit rhombi, more than twice the conservative `0.18D^2` count used in the current
explicit phase-gap arguments.

---

# 107. Near-endpoint wrapping support forces area above `0.473 D^2`

## 107.1 Exact area identity for a compact circle support

Let `S` be a compact wrapping subset of the radius-`1/2` circle.  Assume its pairwise
minor angular diameter is at most

```math
\theta<\pi.
\tag{107.1}
```

Write

```math
\mathbb T\setminus S=\bigsqcup_{j\in J}G_j,
\qquad |G_j|=g_j.
\tag{107.2}
```

Wrapping first gives `g_j<pi` for every complement component.  Indeed a gap longer
than `pi` places `S` inside the complementary open semicircle, while a gap of length
exactly `pi` has antipodal endpoints in `S`, contradicting `theta<pi`.  Every gap has
endpoints in `S`; now that `g_j<pi`, their minor angular separation is exactly `g_j`.
Therefore

```math
\boxed{0<g_j\le\theta<\pi.}
\tag{107.3}
```

Put

```math
K:=\operatorname{conv}S,
\qquad
G(x):={x-\sin x\over8}.
\tag{107.4}
```

### Lemma 107.1 — circular-segment decomposition

```math
\boxed{
\operatorname{area}(K)
={\pi\over4}-\sum_jG(g_j).
}
\tag{107.5}
```

### Proof

For one gap `G_j`, the chord joining its two endpoints is a supporting chord of `K`.
Indeed all of `S` lies on the opposite side of that chord from the open minor arc
`G_j`, because `g_j<pi` and the arc contains no point of `S`.  Thus the open circular
segment between `G_j` and its chord is disjoint from `K`.

The segments belonging to distinct connected complement arcs have pairwise disjoint
interiors.  Conversely, let `z` lie in the radius-`1/2` disk but outside `K`.  A strict
separating line places `z` in a circular cap whose boundary arc contains no point of
`S`.  Since `S` is wrapping, the disk center belongs to `K`; hence the cap is a minor
cap and its boundary arc has length below `pi`.  That empty arc lies inside one
connected component `G_j` of the complement.  The corresponding small cap is contained
in the full circular segment over `G_j`, so `z` lies in that segment.

Therefore the disk-minus-`K` region is, up to boundary sets of area zero, the disjoint
union of the circular segments over all complement gaps.  For radius `R=1/2`, the
segment cut off by an arc of angle `g` has area

```math
{R^2\over2}(g-\sin g)
={g-\sin g\over8}=G(g).
```

Countable additivity gives (107.5). `square`

The same identity can alternatively be obtained by approximating `S` with increasing
finite cyclic subsets and passing the inscribed-polygon area formula to the Hausdorff
limit.

## 107.2 A useful superadditivity fact

For `a,b>=0` with `a+b<=pi`,

```math
\begin{aligned}
8\bigl(G(a+b)-G(a)-G(b)\bigr)
&=\sin a+\sin b-\sin(a+b)\\
&=2\sin\frac{a+b}{2}
\left(
\cos\frac{a-b}{2}-\cos\frac{a+b}{2}
\right)
\ge0.
\end{aligned}
\tag{107.6}
```

Hence `G` is superadditive on nonnegative collections whose total is at most `pi`:

```math
\boxed{
\sum_kG(t_k)\le G\left(\sum_kt_k\right).
}
\tag{107.7}
```

Also `G` is increasing on `[0,pi]` because

```math
G'(x)={1-\cos x\over8}\ge0.
\tag{107.8}
```

## 107.3 Re-derive complement-gap stability from canonical Section 101

Return to a wrapping Type-II harmonic-cell limit.  Put

```math
\phi:=2\pi-2\theta,
\qquad
U:=3\theta-2\pi,
\tag{107.9}
```

```math
f(x):=\sin(x/2),
\qquad
C:=\sum_j f(g_j),
\tag{107.10}
```

and

```math
M:=f(\theta)+2f(\phi)
=\sin(\theta/2)+2\sin\theta.
\tag{107.11}
```

Canonical Section 101 gives

```math
\boxed{
M\le C\le2\alpha\le|S|\le U.
}
\tag{107.12}
```

Define the scalar slack

```math
\sigma:=U-M.
\tag{107.13}
```

Assume throughout this section that

```math
\boxed{0\le\sigma\le10^{-3}.}
\tag{107.14}
```

Canonical Section 101 has a unique zero `theta_8` of `sigma(theta)`, and

```math
\sigma'(\theta)
=3-\tfrac12\cos(\theta/2)-2\cos\theta
\ge{15\over4}.
\tag{107.15}
```

Thus

```math
\theta_8\le\theta\le\bar\theta,
\tag{107.16}
```

where `bar theta` is the unique solution of `sigma(bar theta)=10^{-3}`.  The regression
certificate gives

```math
\boxed{
\bar\theta=2.7031207076068693\ldots .
}
\tag{107.17}
```

Canonical Section 94 supplies at least three distinct complement gaps of length at
least `phi`.  Sort the positive gaps decreasingly and write

```math
g_1=\theta-\delta,
\qquad
\delta\ge0.
\tag{107.18}
```

### Lemma 107.2 — largest-gap stability on the `10^{-3}` window

```math
\boxed{
0\le\delta\le{10\over3}\sigma.
}
\tag{107.19}
```

### Proof

If `delta>=0.1`, then `g_1<=theta-0.1`.  Drop any complement mass above the minimum
`theta+2phi`, preserving three gaps of length at least `phi`.  Since `f` is increasing,
this can only decrease `C`.  Among the resulting vectors, the vector

```math
(\theta-0.1,\phi+0.1,\phi,0,\ldots)
```

majorizes every feasible vector: the largest coordinate is capped by `theta-0.1`, and
the two largest coordinates have sum at most `theta+phi` because a third coordinate
must remain at least `phi`.  Strict concavity of `f` gives

```math
C-M
\ge
f(\theta-0.1)+f(\phi+0.1)-f(\theta)-f(\phi).
\tag{107.20}
```

On the interval (107.16), the right side is greater than `0.0326`, while
`C-M<=sigma<=0.001`, contradiction.  Therefore `delta<0.1`.

For `0<=delta<=0.1`, the same majorization argument gives

```math
C-M
\ge
h_\theta(\delta)
:=f(\theta-\delta)+f(\phi+\delta)-f(\theta)-f(\phi).
\tag{107.21}
```

Moreover

```math
h_\theta'(\delta)
={1\over2}
\left[
\cos{\phi+\delta\over2}
-
\cos{\theta-\delta\over2}
\right].
\tag{107.22}
```

This derivative decreases with `delta` and increases with `theta`.  Hence its minimum
on (107.16) and `0<=delta<=0.1` occurs at
`theta=theta_8, delta=0.1`, where the scalar certificate gives

```math
h_{\theta_8}'(0.1)
=0.3084268133\ldots>0.30.
\tag{107.23}
```

Thus

```math
0.30\delta
<h_\theta(\delta)
\le C-M
\le\sigma,
```

which proves (107.19). `square`

Write

```math
g_2=\phi+x_2,
\qquad
g_3=\phi+x_3,
\qquad
\tau:=\sum_{j\ge4}g_j.
\tag{107.24}
```

Since at least three gaps are at least `phi`, all three new quantities are
nonnegative.  Also

```math
\sum_jg_j
=2\pi-|S|
=\theta+2\phi+e,
\qquad
0\le e=U-|S|\le\sigma.
\tag{107.25}
```

Substitution gives the exact identity

```math
x_2+x_3+\tau=\delta+e,
```

and therefore

```math
\boxed{
0\le x_2,x_3,\tau
\le {13\over3}\sigma.
}
\tag{107.26}
```

This rederivation uses only canonical Sections 94, 100, and 101; proof-only Sections
104--106 are not premises.

## 107.4 Uniform area floor

Put

```math
\phi_8:=2\pi-2\theta_8,
\qquad
q_*:={13\over3}\,10^{-3}=0.0043333333\ldots .
\tag{107.27}
```

Since `theta>=theta_8`, we have `phi<=phi_8`.  Equations (107.18), (107.26), and
(107.16) imply

```math
g_1\le\bar\theta,
\qquad
g_2,g_3\le\phi_8+q_*,
\qquad
\tau\le q_*.
\tag{107.28}
```

Because `q_*<pi`, superadditivity (107.7) gives

```math
\sum_{j\ge4}G(g_j)
\le G(\tau)
\le G(q_*).
\tag{107.29}
```

Apply the exact area identity (107.5), monotonicity of `G`, and (107.28)--(107.29):

```math
\operatorname{area}(K)
\ge
{\pi\over4}
-G(\bar\theta)
-2G(\phi_8+q_*)
-G(q_*).
\tag{107.30}
```

The regression certificate evaluates the right side as

```math
\boxed{
0.4731076260226828\ldots>0.473.
}
\tag{107.31}
```

Therefore every wrapping limit in the scalar window (107.14) satisfies

```math
\boxed{
\operatorname{area}(\operatorname{conv}S)>0.473.
}
\tag{107.32}
```

If finite harmonic cells `P_D` converge after scaling by `D` to `K=conv(S)`, planar
convex Hausdorff convergence preserves area, so

```math
\boxed{
\operatorname{area}(P_D)
>(0.473-o(1))D^2.
}
\tag{107.33}
```

At exact scalar equality the area is substantially larger:

```math
{\pi\over4}-G(\theta_8)-2G(\phi_8)
=0.4735509805082776\ldots .
\tag{107.34}
```

## 107.5 Rhombus-mass consequence

Suppose in addition that `P_D` is locally rhombus-saturated in the canonical sense,

```math
{A_{4,D}\over\operatorname{area}(P_D)}\to1,
\tag{107.35}
```

where `A_{4,D}` is the total area of strict unit-rhombus faces in the carrier.  Every
strict unit rhombus has area at most one.  If `R_D` is their number, then

```math
R_D\ge A_{4,D}.
\tag{107.36}
```

Combining (107.33)--(107.36) gives

```math
\boxed{
R_D\ge(0.473-o(1))D^2.
}
\tag{107.37}
```

In particular, after increasing the large-`D` threshold one may use the explicit
conservative carrier constant

```math
\boxed{R_D\ge0.472D^2}
\tag{107.38}
```

throughout the full `sigma<=10^{-3}` window.

This is more than a factor of `2.6` above the `R_D>=0.18D^2` constant used in the
first quantitative phase/corridor arguments.

## 107.6 Scope and next use

- **Canonical Sections 94, 100, and 101:** supply the three distinguished gaps, the
  support-measure ceiling, and the scalar chain `M<=C<=2alpha<=|S|<=U`.
- **Canonical Type-II annular convergence:** identifies the normalized carrier limit as
  `conv(S)` and transfers normalized area back to finite carriers.
- **Sections 104--106:** not logical premises.  Their gap-stability calculation is
  rederived here on the wider `sigma<=10^{-3}` interval.
- **No cap-family area concentration is required for the area floor itself.**  Section
  103 remains useful for uniqueness and for selecting the wrapping carrier under a
  common diameter cap.
- **No boundary smoothness is assumed.**  The exact area formula handles arbitrary
  compact support, including infinitely many complement components.
- **Contact-isolated source points and bridges are untouched.**

The immediate downstream use is to rerun the canonical Section-90 phase extraction
with `R_D` near `0.473D^2` rather than `0.18D^2`.  That produces substantially larger
inverse-phase shores and should enlarge the explicit Section-102 phase/corridor
exclusion window by another order of magnitude.

**Theorem state:** unchanged. C-II remains open.

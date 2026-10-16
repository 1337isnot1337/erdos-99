<!-- theorem-state: {"artifact_id":"ART-B2BA15925A69","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_near_isodiametric_force_hull_stability_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=0ee925f9c8f3e771ed73c597410340dc8971b4a4; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — near-isodiametric force-hull stability and antipodal diameter localization

**Date:** 2026-09-09  
**Repository base:** `5b4e4bc4fcdc3f5b086ad1be3688f42d7aaf4253`  
**Run type:** exact geometric stability / literature bridge  
**Target:** Target C Gate C-II / external-rattler versus near-disk split  
**LEVEL I STATUS:** STILL OPEN

The ER theorem reduces one C65 branch to

\[
Z_{ext}=o(D^2)
\quad\Longrightarrow\quad
\operatorname{area}(F)
=\left(\frac\pi4-o(1)\right)D^2.
\]

This note converts that area statement into geometric rigidity of the force hull.
Bonnesen's planar stability theorem places `F` between two concentric disks whose
radial gap is controlled by the isoperimetric deficit. Since `diam(F)=D` and its area
is near the isodiametric maximum, both radii are near `D/2`.

Consequently every actual diameter pair is asymptotically antipodal about one common
center. A second exact estimate localizes the **diameter-vector directions at each
endpoint**. Because all partners of one endpoint lie on the same radius-`D` circle
centered at that endpoint, unit separation then gives a valid maximum-degree bound for
the full diameter graph.

An earlier draft tried to infer partner-angle separation directly from their polar
angles about the Bonnesen center. That is invalid in a thick annulus because radial
separation can itself account for unit distance. The corrected proof below uses the
fixed-endpoint diameter vectors instead.

## 1. Bonnesen input

For a planar convex body `K` of area `A` and perimeter `P`, Bonnesen's theorem gives
concentric disks

\[
B_r(c)\subseteq K\subseteq B_R(c)
\]

such that

\[
\boxed{
(R-r)^2\le\frac{P^2-4\pi A}{4\pi}.
}
\tag{B.1}
\]

A convenient modern reference is F. Maggi, *The quantitative isoperimetric inequality
and related topics*, Bull. Math. Sci. 5 (2015), Theorem 1.1.

For `K=F`, the convex perimeter-diameter inequality gives

\[
P_F\le\pi D.
\tag{B.2}
\]

## 2. Theorem ND — explicit annular stability

Define the normalized isodiametric area deficit

\[
\boxed{
\xi:=\frac\pi4-\frac{A_F}{D^2}\ge0.
}
\tag{ND.1}
\]

### Theorem ND.1

There is a center `c` and radii `r<=R` with

\[
B_r(c)\subseteq F\subseteq B_R(c)
\]

such that

\[
\boxed{R-r\le\sqrt\xi\,D.}
\tag{ND.2}
\]

Writing `rho=sqrt(A_F/pi)`,

\[
\boxed{
\rho-\sqrt\xi D\le r\le\rho\le R\le\rho+\sqrt\xi D.
}
\tag{ND.3}
\]

Also

\[
\boxed{
\left|\rho-\frac D2\right|
\le\frac{2\xi}{\pi}D.
}
\tag{ND.4}
\]

Hence, with

\[
\boxed{
\eta:=\sqrt\xi+\frac{2\xi}{\pi},
}
\tag{ND.5a}
\]

one has

\[
\boxed{
B_{D(1/2-\eta)}(c)
\subseteq F
\subseteq
B_{D(1/2+\eta)}(c).
}
\tag{ND.5}
\]

### Proof

Bonnesen and B.2 give

\[
(R-r)^2
\le\frac{\pi^2D^2-4\pi A_F}{4\pi}
=\xi D^2,
\]

which is ND.2. The disk inclusions imply `pi r^2<=A_F<=pi R^2`, hence
`r<=rho<=R`; together with ND.2 this proves ND.3.

From ND.1,

\[
\rho=\frac D2\sqrt{1-\frac{4\xi}{\pi}}.
\]

Using `1-sqrt(1-x)<=x` for `0<=x<=1` gives ND.4. Combine ND.3 and ND.4 to obtain
ND.5. `square`

### Corollary ND.2 — ER near-disk branch

If `Z_ext=o(D^2)`, then ER gives `xi->0`; therefore for suitable centers `c_D`,

\[
\boxed{
B_{D/2-o(D)}(c_D)
\subseteq F
\subseteq
B_{D/2+o(D)}(c_D).
}
\tag{ND.6}

After scaling by `D` and translating by `c_D`, the force hull converges in Hausdorff
distance to the radius-`1/2` disk.

## 3. Diameter pairs become uniformly antipodal about the common center

Fix the center `c` from ND.5 and let `xy` be an actual diameter edge. Put

\[
r_x=|x-c|,\qquad r_y=|y-c|,
\]

so

\[
D(1/2-\eta)\le r_x,r_y\le D(1/2+\eta).
\tag{3.1}
\]

Write

\[
\angle xcy=\pi-\varphi,
\qquad0\le\varphi\le\pi.
\]

The cosine law gives

\[
D^2=(r_x+r_y)^2-2r_xr_y(1-\cos\varphi).
\tag{3.2}
\]

Since `D<=r_x+r_y<=D(1+2eta)`,

\[
(r_x+r_y)^2-D^2\le4\eta(1+\eta)D^2.
\]

Also `r_xr_y>=D^2(1/2-eta)^2`. Hence, for `eta<1/2`,

\[
\boxed{
1-\cos\varphi
\le
\frac{2\eta(1+\eta)}{(1/2-\eta)^2}.
}
\tag{ND.7}
\]

Thus

\[
\boxed{
\varphi
\le
\varphi_{max}:=
2\arcsin\sqrt{
\frac{\eta(1+\eta)}{(1/2-\eta)^2}
}.
}
\tag{ND.8}
\]

In particular, `eta=O(sqrt(xi))` implies

\[
\boxed{
\sup_{xy\in H}|\pi-\angle xcy|
=O(\xi^{1/4}).
}
\tag{ND.9}
\]

## 4. Correct endpoint-direction localization

Fix a loaded endpoint `x` and let

\[
u:=\frac{x-c}{|x-c|}.
\]

For a diameter partner `y`, choose a perpendicular unit vector `v` and write

\[
y-c=r_y(-\cos\varphi\,u+\sin\varphi\,v),
\qquad |\varphi|\le\varphi_{max}.
\]

Then

\[
x-y
=(r_x+r_y\cos\varphi)u-r_y\sin\varphi\,v.
\tag{4.1}
\]

Let `theta_xy` be the angle between the diameter vector `x-y` and the outward radial
direction `u`. Since `r_x,r_y>=D(1/2-eta)` and `r_y<=D(1/2+eta)`,

\[
\tan|\theta_{xy}|
\le
\frac{(1/2+\eta)|\sin\varphi|}
{(1/2-\eta)(1+\cos\varphi)}
=
\frac{1/2+\eta}{1/2-\eta}
\left|\tan\frac\varphi2\right|.
\]

Therefore every diameter vector incident to `x` lies in one angular interval of total
width at most `2theta_max`, where

\[
\boxed{
\theta_{max}:=
\arctan\left(
\frac{1/2+\eta}{1/2-\eta}
\tan\frac{\varphi_{max}}2
\right).
}
\tag{ND.10}
\]

As `xi->0`,

\[
\boxed{\theta_{max}=O(\xi^{1/4}).}
\tag{ND.11}
\]

This is the correct object for the degree bound: it localizes vectors on the fixed
radius-`D` circle about `x`, not the partner radii about `c`.

## 5. Maximum degree from unit separation on the fixed diameter circle

Let `y,z` be distinct diameter partners of the same endpoint `x`. The incident unit
directions are

\[
u_y:=\frac{x-y}{D},
\qquad
u_z:=\frac{x-z}{D}.
\]

Because both diameter vectors have length exactly `D`,

\[
|y-z|
=D|u_y-u_z|.
\]

Unit separation gives

\[
|u_y-u_z|\ge\frac1D.
\]

If their directional angle is `alpha`, then

\[
|u_y-u_z|=2\sin(\alpha/2),
\]

so

\[
\boxed{
\alpha\ge
\delta_D:=2\arcsin\frac1{2D}.
}
\tag{5.1}
\]

All incident directions lie in an interval of width `2theta_max`. Therefore

\[
\boxed{
\deg_H(x)
\le
1+\frac{2\theta_{max}}{\delta_D}.
}
\tag{ND.12}
\]

Since `delta_D~1/D` and `theta_max=O(xi^(1/4))`, the ER near-disk branch gives

\[
\boxed{
\Delta(H)=O(D\xi^{1/4})+O(1)=o(D).
}
\tag{ND.13}
\]

This materially strengthens C18's fixed positive-fraction degree ceiling in the
near-disk branch.

## 6. Diameter matching consequence

ZS gives

\[
h\ge D+O(1).
\]

A greedy matching in a graph of maximum degree `Delta` has size at least
`h/(2Delta-1)`. Hence ND.13 gives

\[
\boxed{
\nu(H)\to\infty
}
\tag{ND.14}
\]

whenever `Z_ext=o(D^2)`.

No linear matching bound is claimed; the rate depends on the isodiametric deficit.

## 7. Interaction with the near-zero response branch

C66 permits normalized `beta` mass to concentrate on one diameter star when
`D epsilon->0`. ND.13 says that in the near-disk force-hull branch this star contains
only `o(D)` of the `h>=D` actual diameter edges. Thus almost all actual diameter edges
lie outside every fixed star, even though their total positive KKT weight may tend to
zero.

This is a support theorem, not a weight theorem. It does not contradict C66. A closing
argument still needs a quantitative bridge from the near-antipodal full support to
beta/response mass or to contact topology.

## 8. Literature imported

Francesco Maggi, *The quantitative isoperimetric inequality and related topics*,
Bulletin of Mathematical Sciences 5 (2015), Theorem 1.1. The only imported statement
is the planar Bonnesen theorem B.1 for convex sets.

No external theorem about diameter graphs, constant-width bodies, or Erdős #99 is
used.

## 9. Regression / correction audit

- **Thick annulus radial separation:** the withdrawn draft step tried to bound partner
  central-angle separation from unit separation and a common outer radius. That is
  false because two points can be separated radially. The current proof does not use
  that implication.
- **Fixed endpoint:** the corrected degree proof uses that all partners of `x` lie on
  the exact circle `|x-y|=D`; then partner separation is exactly diameter-vector
  separation.
- **Regular odd shell:** `xi->0` and its diameter graph has bounded degree two, fully
  consistent with ND.13.

## 10. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| annular containment ND.5 | proved | Bonnesen + `P<=pi D` + area algebra. |
| `Z_ext=o(D^2)` -> Hausdorff near-disk | proved | ER + ND.5. |
| all diameter pairs near antipodal | proved | cosine law in common annulus. |
| incident diameter-vector interval ND.10 | proved | explicit vector decomposition. |
| `Delta(H)=o(D)` | proved | fixed-endpoint circle + unit separation. |
| diameter matching number diverges | proved | greedy matching bound. |
| near-disk branch impossible | not proved | weights/contact topology still uncontrolled. |
| Level I | still open | External-rattler and near-disk branches remain. |

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let xi=pi/4-area(F)/D^2 and eta=sqrt(xi)+2xi/pi.
Bonnesen gives
    B_{D(1/2-eta)}(c) subset F subset B_{D(1/2+eta)}(c).
ER says Z_ext=o(D^2) => xi->0.

Every diameter pair xy is near-antipodal about c:
    |pi-angle xcy|=O(xi^(1/4)).
For fixed x, the actual diameter vectors x-y all lie in an angular interval of width
    O(xi^(1/4)).
Distinct partners satisfy
    angle((x-y),(x-z)) >= 2 asin(1/(2D))
exactly because |x-y|=|x-z|=D and |y-z|>=1.
Therefore
    Delta(H)=O(D xi^(1/4))+O(1)=o(D).
Since h>=D, the diameter matching number tends to infinity.
```

<!-- theorem-state: {"artifact_id":"ART-D9D7D4119965","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — quantitative near-circle diameter-star collapse

**Date:** 2026-09-09  
**Repository branch:** `research/post-uf-attachment-fill-2026-09-09`  
**Run type:** quantitative stability synthesis  
**Target:** NS/LC near-circle diameter support  
**Depends on:** DG, DC, OP, planar quantitative isodiametric stability of Maggi--Ponsiglione--Pratelli  
**External source:** F. Maggi, M. Ponsiglione, A. Pratelli, *Quantitative stability in the isodiametric inequality via the isoperimetric inequality*, Trans. Amer. Math. Soc. 366 (2014), 1141--1160, arXiv:1104.4074. In dimension two, their Theorem 2 and Remark 3 give Hausdorff distance to the equal-diameter disk bounded by a constant times the square root of the isodiametric deficit.  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

NS proves qualitatively that in the PR #119 near-circle branch

\[
\Delta(H)=o(D).
\]

The qualitative compactness can be made quantitative in terms of the force-hull perimeter deficit.

Put

\[
P:=\operatorname{per}(F),
\qquad
\eta_P:=\frac{\pi D-P}{D}.
\]

Then along the small-outer-walk branch

\[
\eta_P\to0,
\]

and the complete actual diameter graph obeys

\[
\boxed{
\frac{\Delta(H)}D
\le
C\left(\eta_P^{1/8}+D^{-1/4}
ight)
}
\tag{QR.1}
\]

for an absolute constant `C` and all sufficiently large members of the branch.

DG also implies, in this same endpoint,

\[
\eta_P
=O\left(\frac{x_B+1}{D}\right),
\]

hence

\[
\boxed{
\frac{\Delta(H)}D
=O\left(
\left(\frac{x_B+1}{D}\right)^{1/8}

ight).
}
\tag{QR.2}

\]

The exponent is weak but explicit. A macroscopic LC attachment block of size `mu D` therefore requires at least

\[
\boxed{
\Omega\left(\left(\frac{D}{x_B+1}\right)^{1/8}
ight)
}
\tag{QR.3}

\]

distinct opposite-side diameter carriers.

---

## 1. Minimum-width deficit from the perimeter deficit

Let

\[
w(\theta)
\]

be the width of `F` in direction `theta`, with `theta` modulo `pi`. Since `diam(F)=D`,

\[
0<w(\theta)\le D.
\]

Cauchy's perimeter formula gives

\[
P=\int_0^\pi w(\theta)\,d\theta.
\tag{1.1}
\]

Put

\[
f(\theta):=D-w(\theta)\ge0,
\qquad
M:=\max_\theta f(\theta)
=D-\min_\theta w(\theta).
\]

At almost every differentiability angle, if `p_+(theta),p_-(theta)` are the two support points realizing the width, then

\[
w'(\theta)
=(p_+-p_-)\cdot u_\theta^\perp.
\]

Therefore

\[
|w'(\theta)|\le|p_+-p_-|\le D.
\]

Thus `f` is `D`-Lipschitz on the projective circle.

If `f(theta_0)=M`, then

\[
f(\theta)\ge[M-Dd(\theta,\theta_0)]_+.
\]

Integrating the triangular lower profile on both sides of `theta_0` gives

\[
\pi D-P
=\int_0^\pi f(\theta)d\theta
\ge\frac{M^2}{D}.
\]

Hence

### Lemma QR.1

\[
\boxed{
M\le D\sqrt{\eta_P}.
}
\tag{QR.4}

\]

This is an elementary finite estimate; no external stability theorem is used here.

---

## 2. DC converts width deficit into an external-shell population bound

DC proves that every external C65 rattler lies in the shell

\[
F_{+M}\setminus F
\]

and gives the explicit packing estimate

\[
Z_{ext}
\le
\frac8\pi(M+1/2)P
+8(M+1/2)^2.
\tag{2.1}
\]

Using `P<=pi D` and QR.4,

\[
\boxed{
\frac{Z_{ext}}{D^2}
\le
C_1\left(\sqrt{\eta_P}+\eta_P+D^{-1}\right)
}
\tag{2.2}

\]

for an absolute constant `C_1`.

---

## 3. OP converts external population into an isodiametric area deficit

OP gives

\[
n-Z_{ext}
\le
\frac2{\sqrt3}\operatorname{area}(F)
+\frac12P+1.
\tag{3.1}
\]

The strict translated-lattice comparison gives

\[
n>\Delta D^2+1,
\qquad
\Delta=\frac\pi{2\sqrt3}.
\tag{3.2}
\]

Multiply (3.1) by `a_0=sqrt(3)/2` and use `a_0 Delta=pi/4`:

\[
\operatorname{area}(F)
>
\frac\pi4D^2
-a_0Z_{ext}
-\frac{a_0}{2}P.
\tag{3.3}
\]

Define the relative isodiametric area deficit

\[
\delta_{iso}
:=
1-
\frac{4\operatorname{area}(F)}{\pi D^2}.
\]

Equations (2.2)-(3.3), with `P=O(D)`, give

\[
\boxed{
\delta_{iso}
\le
C_2\left(
\sqrt{\eta_P}+\eta_P+D^{-1}
\right).
}
\tag{3.4}

\]

In particular, as `eta_P->0`,

\[
\delta_{iso}=O(\sqrt{\eta_P}+D^{-1}).
\tag{3.5}
\]

---

## 4. Quantitative isodiametric stability gives a disk Hausdorff rate

Maggi--Ponsiglione--Pratelli prove that in dimension two, for a set of fixed diameter, Hausdorff distance to a disk of the same diameter is bounded by a dimensional constant times the square root of the isodiametric deficit. Their deficit normalization is equivalent, for small deficit, to the relative area deficit used above; changing normalization only changes the constant.

Therefore there is a center `c` and an absolute constant `C_3` such that

\[
\boxed{
 d_H\left(D^{-1}(F-c),B_{1/2}\right)
\le
C_3\,\delta_{iso}^{1/2}.
}
\tag{4.1}

\]

Using (3.5), put

\[
\rho
:=
C_4\left(\eta_P^{1/4}+D^{-1/2}\right).
\tag{4.2}
\]

Then

\[
D^{-1}(F-c)
\subseteq
B_{1/2+\rho}
\]

and also contains the corresponding inner disk up to the same Hausdorff error.

---

## 5. Exact diameter pairs are `O(sqrt(rho))` from antipodal

Let `u,v` be an actual diameter pair. Normalize and recenter:

\[
x=(u-c)/D,
\qquad
y=(v-c)/D.
\]

Then

\[
|x-y|=1,
\qquad
|x|,|y|\le\frac12+\rho.
\]

Let the angle between `x` and `y` be

\[
\pi-\phi,
\qquad 0\le\phi\le\pi.
\]

For fixed angular separation, the distance is maximized when both radii equal `1/2+rho`. Hence

\[
1=|x-y|
\le(1+2\rho)\cos\frac\phi2.
\tag{5.1}
\]

Thus

\[
\cos\frac\phi2
\ge\frac1{1+2\rho}.
\]

For small `rho`, this gives

\[
\boxed{
\phi\le C_5\sqrt\rho.
}
\tag{5.2}

\]

uniformly over every actual diameter edge.

For one fixed terminal `z`, every diameter partner is therefore contained in a star cone of angular width

\[
\boxed{
O\left(\eta_P^{1/8}+D^{-1/4}\right).
}
\tag{5.3}

\]

---

## 6. Unit separation gives the degree bound

All diameter partners of `z` lie on the Euclidean circle of radius `D` centered at `z`. Distinct partners are source points at mutual distance at least one. Therefore their angular separation at `z` is at least

\[
2a_D
=2\arcsin\frac1{2D}
\asymp\frac1D.
\]

Packing such directions into the cone (5.3) gives

\[
\deg_H(z)
\le
C_6D
\left(\eta_P^{1/8}+D^{-1/4}\right)+1.
\]

Taking the maximum over `z` proves QR.1.

---

## 7. Relate the perimeter deficit to `x_B`

The convex force hull has `q` unit-separated consecutive vertices, so

\[
P\ge q,
\qquad
\eta_P\le\frac{\pi D-q}{D}.
\tag{7.1}
\]

DG gives, with `a_D=asin(1/(2D))`,

\[
x_B
\ge
2D\cos((q-2)a_D)
-2
-2(d_H-1)(1-\cos a_D).
\tag{7.2}
\]

In the small-outer-walk endpoint, `(pi D-q)/D->0` and `d_H=O(D)`. Since

\[
a_D=\frac1{2D}+O(D^{-3}),
\qquad
1-\cos a_D=O(D^{-2}),
\]

expanding the monotone sine near `pi/2` in (7.2) yields the safe rate

\[
\boxed{
\pi D-q=O(x_B+1).
}
\tag{7.3}

\]

A direct nonasymptotic proof uses `sin y >= 2y/pi` for `0<=y<=pi/2` after writing `(q-2)a_D=pi/2-y`; the `O(1)` terms absorb the `a_D-1/(2D)` and `d_H(1-cos a_D)` corrections.

Thus

\[
\boxed{
\eta_P
=O\left(\frac{x_B+1}{D}\right).
}
\tag{7.4}

\]

Insert (7.4) into QR.1 to obtain QR.2.

---

## 8. Opposite-carrier count for the LC component

Let the LC macroscopic attachment block have

\[
|A_*|\ge(\mu-o(1))D
\]

with fixed `mu>0` and no internal diameter edges when `mu<1`.

Every `a in A_*` has at least one actual diameter edge leaving `A_*`. If `N_H(A_*)` is the outside diameter-neighbor set, then

\[
|A_*|
\le
|N_H(A_*)|\,\Delta(H).
\]

Using QR.2,

\[
\boxed{
|N_H(A_*)|
\ge
\Omega\left(
\left(\frac{D}{x_B+1}\right)^{1/8}
\right).
}
\tag{8.1}
\]

The same lower order holds for a greedy family of pairwise vertex-disjoint diameter carriers up to another absolute constant.

This is still sublinear in the worst allowed `x_B=o(D)` regime. It is a quantitative support theorem, not a closure.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| width deficit `M^2<=D(pi D-P)` | proved | width function is `D`-Lipschitz + Cauchy formula |
| shell population in terms of `eta_P` | proved | DC finite shell bound |
| area deficit `O(sqrt eta_P)` | proved | OP + lattice lower count |
| Hausdorff disk rate | external theorem | Maggi--Ponsiglione--Pratelli, planar Theorem 2/Remark 3 |
| star angular width eighth-root rate | proved | exact diameter + disk annulus geometry |
| `Delta(H)/D` QR.1 | proved | unit separation on radius-`D` partner circle |
| `eta_P=O((x_B+1)/D)` | proved in DG endpoint | exact DG inequality expanded with controlled finite errors |
| Level I | still open | eighth-root carrier count is not linear |

---

## 10. Next target

QR shows exactly what quantitative improvement is needed for a closing diameter-support argument.

The present chain loses exponents at three places:

1. width deficit from average perimeter deficit: square root;
2. area-to-Hausdorff isodiametric stability: square root;
3. annular disk error to antipodal angular error: square root.

Hence the eighth root.

A source-specific theorem can beat this badly. In particular, if the C65 diameter endpoints themselves control the missing-width directions, one may bypass the generic width and isodiametric stability losses. A direct relation

\[
\text{star angular width}\le C\frac{x_B+1}{D}
\]

would make the LC block require `Omega(D/(x_B+1))` distinct opposite carriers and would become potentially closing when `x_B=O(1)`.

No such direct bound is claimed here.

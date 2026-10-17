> Generated reading edition · [exact source](../../../../docs/targets/target-c/93-full-gap-wrapping-diameter-audit.md) · source SHA-256 `79a60834643959065a89eafeed0791d2aa25eec65b8aab1dc0aa1484e3e721f0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — full attachment-gap perimeter raises the wrapping threshold again

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

Section 92 raises the Type-II wrapping-cell diameter threshold by comparing the Section-88 six-cluster attachment-count ceiling with a perimeter floor from only three wrapping anchors.

The same canonical inputs contain more information. A macroscopic harmonic attachment set has `Theta(D)` actual source vertices on the near-circular force-hull boundary. Consecutive attachment vertices therefore have a uniform angular separation of order `1/D`. The cell diameter supplies a fixed upper angular-gap bound. Once all cyclic attachment gaps are retained, concavity of the chord-length function solves the minimum possible attachment-polygon perimeter exactly.

Combining that full-gap perimeter minimum with the canonical finite capacity

$$
\operatorname{per}(P)\le4|A|-6
$$

and the Section-88 six-cluster attachment ceiling yields the stronger threshold

$$
\boxed{
\mu_2=0.915964980334399\ldots
}
$$

characterized by

$$
\boxed{
2\mu_2+\sin(8\arcsin\mu_2)
=18\arcsin\mu_2-6\pi.
}
$$

As in Sections 88 and 92, the cap-family argument then produces an actual locally rhombus-saturated macroscopic Type-II harmonic cell of diameter at least `(mu_2-o(1))D`.

The theorem uses only canonical Sections 80, 82, 83, and 88. It does not depend on Sections 90--92.

---

# 93. Full attachment-gap spacing forces diameter at least 0.915964 D

## 93.1 Type-II annular geometry gives a uniform lower gap

Work along a Type-II sequence. Translate by the canonical near-disk centers. There is a sequence `epsilon_D -> 0` such that the force hull satisfies

$$
B\left(0,\left({1\over2}-\epsilon_D\right)D\right)
\subset F
\subset
B\left(0,\left({1\over2}+\epsilon_D\right)D\right).
\tag{93.1}
$$

Put

$$
r_D=\left({1\over2}-\epsilon_D\right)D,
\qquad
R_D=\left({1\over2}+\epsilon_D\right)D.
$$

Canonical Section 88's radial arclength lemma gives, for every angular interval of length `g`, the exact boundary-arc estimate

$$
\operatorname{length}(\partial F\text{ over that interval})
\le {R_D^2\over r_D}g.
\tag{93.2}
$$

Define

$$
\ell_D:={r_D\over R_D^2}.
\tag{93.3}
$$

Then

$$
D\ell_D\to2.
\tag{93.4}
$$

Let `A` be the attachment set of any harmonic cell and list its vertices in cyclic polar order around the Type-II center. If consecutive attachment vertices have angular gap `g`, their Euclidean distance is at least one because they are distinct source points. The boundary arc of `F` between them is no shorter than their chord, hence at least one. Equation (93.2) therefore gives

$$
\boxed{g\ge\ell_D.}
\tag{93.5}

This lower bound is uniform over all consecutive attachment gaps; no fixed-number-of-arcs restriction is used.

## 93.2 A diameter bound gives a uniform upper gap

Consider a sequence of harmonic cells `P_D=conv(A_D)` with

\[
{\operatorname{diam}(P_D)\over D}\to\lambda<1
\tag{93.6}
$$

whose normalized attachment sets have a wrapping Hausdorff limit on the radius-`1/2` circle.

Let the cyclic angular gaps of `A_D` be

$$
g_{1,D},\ldots,g_{a_D,D},
\qquad a_D=|A_D|.
$$

Wrapping means no open semicircle contains the limiting support. Thus its largest circular gap is at most `pi`. Since `lambda<1`, the limiting support has no antipodal pair, so in fact every limiting positive gap is strictly below `pi`.

For two attachment vertices of radii at least `r_D` and angular separation `g<=pi`,

$$
|p-q|
\ge2r_D\sin(g/2).
\tag{93.7}
$$

Since every attachment pair lies in a cell of diameter `(lambda+o(1))D`, (93.1), (93.6), and (93.7) imply uniformly

$$
\boxed{
g_{i,D}\le\theta+o(1),
\qquad
\theta:=2\arcsin\lambda<\pi.}
\tag{93.8}

After enlarging the upper bound by a scalar `o(1)` independent of `i`, write it as `theta_D=theta+o(1)`.

## 93.3 Exact finite minimum of the full cyclic chord sum

We isolate the elementary optimization used below.

### Lemma 93.1 — concave box-simplex minimum

Let

\[
0<\ell<\theta<\pi,
\qquad
n\ell\le2\pi\le n\theta.
$$

Among all `n`-tuples

$$
\ell\le g_i\le\theta,
\qquad
\sum_{i=1}^n g_i=2\pi,
$$

the minimum of

$$
\sum_{i=1}^n\sin(g_i/2)
$$

is obtained by putting as many gaps as possible at `theta`, all but at most one of the remaining gaps at `ell`, and one residual gap.

More precisely, put

$$
Y:=2\pi-n\ell,
\qquad
k:=\left\lfloor{Y\over\theta-\ell}\right\rfloor,
\qquad
u:=Y-k(\theta-\ell)\in[0,\theta-\ell).
\tag{93.9}
$$

Then the minimum is

$$
\boxed{
M(n,\ell,\theta)
=k\sin(\theta/2)
+(n-k-1)\sin(\ell/2)
+\sin((\ell+u)/2),
}
\tag{93.10}

with the evident interpretation when `u=0`.

### Proof

Put `y_i=g_i-ell`. Then

\[
0\le y_i\le\theta-\ell,
\qquad
\sum_i y_i=Y.
$$

The objective is the sum of the concave functions

$$
y\mapsto\sin((\ell+y)/2)
$$

on this interval. A concave function on a compact polytope attains its minimum at an extreme point. Every extreme point of the box-simplex has all but at most one coordinate at an endpoint. The sum constraint forces exactly the pattern in (93.9)--(93.10). `square`

## 93.4 Asymptotic full-gap perimeter floor

Pass to a subsequence on which

$$
{a_D\over D}\to\alpha.
\tag{93.11}

Canonical Section 88 gives an absolute linear upper bound on `a_D`, while every wrapping cell has at least three attachments, so such subsequences exist. In the application below `alpha` will be positive.

Every side of the convex attachment polygon joins consecutive attachment vertices in cyclic order. By (93.1), its length is at least

\[
2r_D\sin(g_{i,D}/2).
$$

Hence

$$
{\operatorname{per}(P_D)\over D}
\ge
(1-2\epsilon_D)
\sum_i\sin(g_{i,D}/2).
\tag{93.12}

The chord sum is at most

\[
\sum_i {g_{i,D}\over2}=\pi,
$$

so the prefactor `(1-2epsilon_D)` creates only `o(1)` total loss.

Apply Lemma 93.1 with

$$
n=a_D,
\qquad
\ell=\ell_D,
\qquad
\theta=\theta_D.
$$

By (93.4) and (93.11),

$$
a_D\ell_D\to2\alpha.
\tag{93.13}

Define

\[
R(\alpha):=2\pi-2\alpha,
\qquad
k(\alpha,\lambda):=\left\lfloor{R(\alpha)\over\theta}\right\rfloor,
\tag{93.14}

whenever `R(alpha)/theta` is not an integer, with the continuous endpoint interpretation otherwise, and put

\[
r(\alpha,\lambda)
:=R(\alpha)-k(\alpha,\lambda)\theta
\in[0,\theta).
\tag{93.15}

Since `k` is bounded independently of `D`, (93.10)--(93.13) give the asymptotic perimeter floor

\[
\boxed{
\liminf {\operatorname{per}(P_D)\over D}
\ge
p(\alpha,\lambda)
:=\alpha+k(\alpha,\lambda)\lambda
+\sin\left({r(\alpha,\lambda)\over2}\right).
}
\tag{93.16}

The term `alpha` is the cumulative contribution of the `Theta(D)` near-minimal angular gaps. The remaining `O(1)` gaps carry the macroscopic wrapping angle.

## 93.5 Compare the full-gap floor with canonical attachment capacity

Canonical Section 82 gives, for every harmonic cell,

\[
\operatorname{per}(P_D)\le4a_D-6.
\tag{93.17}

Therefore every wrapping cell subsequential limit must satisfy

\[
\boxed{p(\alpha,\lambda)\le4\alpha.}
\tag{93.18}

Canonical Section 88's six-cluster argument independently gives

\[
\boxed{
\alpha
\le U(\lambda)
:=6\arcsin\lambda-2\pi.
}
\tag{93.19}

For fixed `lambda`, define

\[
F_\lambda(\alpha):=p(\alpha,\lambda)-4\alpha.
\tag{93.20}

On every interval where `k=k(alpha,lambda)` is constant,

\[
{\partial p\over\partial\alpha}
=1-\cos(r/2),
$$

because `partial r/partial alpha=-2`. Hence

$$
\boxed{
{\partial F_\lambda\over\partial\alpha}
=-3-\cos(r/2)<0.
}
\tag{93.21}

At a transition `R(alpha)=m theta`, the two formulas agree: on one side the residual tends to `theta` and contributes `sin(theta/2)=lambda`, while on the other side that contribution becomes one additional maximal gap. Thus `F_lambda` is continuous and strictly decreasing on its whole feasible alpha interval.

Consequently, subject to the Section-88 upper bound (93.19), the easiest possible way to satisfy the perimeter capacity (93.18) is to use the **maximum** allowed attachment density:

\[
\boxed{
F_\lambda(U(\lambda))\le0
}
\tag{93.22}

is necessary for any wrapping harmonic-cell limit.

This is the point missed by the three-anchor estimate: maximal boundary occupancy itself has a nonzero perimeter cost from the many unit-separated attachment gaps.

## 93.6 Solve the new scalar obstruction

Put

\[
a:=\arcsin\lambda.
$$

For

$$
{\pi\over3}<a<{3\pi\over8}
\tag{93.23}

we have

\[
2< {2\pi-2U(\lambda)\over2a}<3,
$$

because

$$
{2\pi-2U(\lambda)\over2a}
={3\pi\over a}-6.
$$

Hence at maximal attachment density one has `k=2`. The residual gap is

$$
r
=2\pi-2U(\lambda)-4a
=6\pi-16a.
\tag{93.24}

Therefore

\[
p(U(\lambda),\lambda)
=U(\lambda)+2\lambda+\sin(3\pi-8a)
=U(\lambda)+2\lambda+\sin(8a).
\tag{93.25}

The necessary condition (93.22) becomes

\[
\boxed{
G(a):=2\sin a+\sin(8a)-18a+6\pi\le0.
}
\tag{93.26}

On the entire interval (93.23),

\[
G'(a)=2\cos a+8\cos(8a)-18
\le2+8-18=-8<0.
\tag{93.27}

Also

\[
G(\pi/3)={3\sqrt3\over2}>0,
\tag{93.28}

while direct substitution at `a=arcsin(0.916)` gives a negative value. Thus there is one and only one root in `(pi/3,arcsin(0.916))`.

Define

\[
\boxed{
\mu_2:=\sin a_2,
\qquad
2\sin a_2+\sin(8a_2)=18a_2-6\pi.
}
\tag{93.29}

Numerically,

\[
\boxed{
\mu_2=0.915964980334399\ldots
}
\tag{93.30}

and in particular

\[
0.9155<\mu_2<0.916.
\tag{93.31}

For any wrapping limit with `lambda<mu_2`, either `lambda<=sqrt(3)/2`, which is already impossible for a wrapping support of diameter below the equilateral threshold, or `a in (pi/3,a_2)`, where (93.27)--(93.29) give

\[
F_\lambda(U(\lambda))=G(a)>0.
$$

Since `F_lambda` decreases with `alpha` and every actual `alpha<=U(lambda)`, one has `F_lambda(alpha)>0`, contradicting (93.18).

Therefore

$$
\boxed{
\text{every wrapping Type-II harmonic-cell limit has normalized diameter at least }\mu_2.
}
\tag{93.32}

This proof subsumes the scalar wrapping conclusions of Sections 88 and 92. It does not assume either module as a dependency.

## 93.7 Propagate the threshold to an actual macroscopic carrier

Fix any

\[
\mu<\mu_2.
$$

By (93.32), every macroscopic harmonic-cell limit of normalized diameter at most `mu` is cap type. The canonical Section-88 cap-family capacity theorem therefore applies verbatim:

\[
\limsup {1\over D^2}
\sum_{\operatorname{diam}(P_r)\le\mu D}
\operatorname{area}(P_r)
\le\mathcal C(\mu)<{\pi\over4}.
\tag{93.33}

Thus the longer cells carry at least

\[
\Gamma(\mu)D^2-o(D^2),
\qquad
\Gamma(\mu):={\pi\over4}-\mathcal C(\mu)>0.
\tag{93.34}

The canonical total cell-perimeter bound makes the number of such cells uniformly bounded for fixed `mu`. One therefore has area `Omega_mu(D^2)`. Canonical Section 83 gives summed local rhombic deficit `o(D^2)`, so one may choose a long cell with local strict-rhombus filling fraction tending to one.

At the new endpoint,

\[
\mathcal C(\mu_2)=0.4770363820\ldots,
\qquad
\Gamma(\mu_2)=0.3083617814\ldots>0.
\tag{93.35}

Hence the long-cell area fraction stays uniformly positive as `mu` tends to `mu_2`. A diagonal choice yields one actual sequence `P_*` satisfying

\[
\boxed{
{\operatorname{diam}(P_*)\over D}\ge\mu_2-o(1),
\qquad
\operatorname{area}(P_*)\ge c_2D^2,
\qquad
{A_{4,*}\over\operatorname{area}(P_*)}\to1
}
\tag{93.36}

for one absolute `c_2>0`.

Thus the Type-II carrier threshold improves to

\[
\boxed{0.9159649803\ldots D-o(D).}
\tag{93.37}

## 93.8 Remaining endpoint geometry

The new scalar obstruction already assumes the most favorable possible attachment density `alpha=U(lambda)`. Therefore any hypothetical sequence approaching `mu_2` must simultaneously asymptotically saturate

1. the Section-88 six-cluster boundary packing count;
2. the canonical attachment-perimeter capacity `per(P)<=4a-6`;
3. the finite lower angular-gap bound coming from unit separation on the near-circular force hull; and
4. the concave gap-minimization pattern: asymptotically two macroscopic gaps of size `theta`, one residual macroscopic gap of size `r=6pi-16asin(mu_2)`, and all other `Theta(D)` attachment gaps at the minimum `2/D` scale.

This is much more rigid than the Section-92 three-anchor equality picture. A next endpoint-stability theorem can attack the compatibility of that gap pattern with the six-cluster support geometry or with the locally rhombus-saturated carrier behind the attachment polygon.

The ordered-grid route of Sections 90--91 remains an independent quantitative mechanism and can also use the stronger carrier diameter once this theorem is promoted.

## 93.9 Dependency and regression audit

- **Canonical `C-FULLCORE-NEAR-DISK` / Section 80:** concentric annular convergence of the force hull to the radius-`1/2` disk.
- **Canonical `C-HARMONIC-CARRIER-QUAD` / Section 82:** exact local attachment-perimeter capacity `per(P)<=4|A|-6`.
- **Canonical `C-HARMONIC-CELL-TILING` / Section 83:** pairwise interior-disjoint cells and summed local rhombic deficit.
- **Canonical `C-HARMONIC-WRAPPING` / Section 88:** six-cluster attachment-count ceiling, cap-family area capacity, total cell-perimeter control, and the macroscopic-cell selection framework.
- **No Section 92 dependency:** the full-gap proof independently implies a stronger wrapping threshold.
- **No Section 90/91 dependency:** no dense train-core or ordered-grid theorem is used.
- **No fixed number of angular intervals:** the lower gap bound uses the exact radial arclength inequality individually on every consecutive attachment interval.
- **Near-circle radial error:** side lengths use the common lower radius `r_D`, and the normalized total chord sum is at most `pi`, so the multiplicative annular error remains `o(1)` after summation over `Theta(D)` sides.
- **Contact-isolated source points:** untouched.
- **KKT coefficient floors:** not used.

**Status:** canonical; promoted by the independent Sections-90–94 audit.
**Theorem state:** `2026-09-11.audit.36`.

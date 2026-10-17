> Generated reading edition · [exact source](../../../docs/reports/target_c_full_visibility_antipodal_joint_area_2026-09-09.md) · source SHA-256 `09d55fb4a57aec2c497c37ce3c03d44f006b7b06b0833c4b42f7532be8577662`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B0B9BF39F19B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_full_visibility_antipodal_joint_area_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=b9985d3b03dfb56ea9e3bbfd0be15b4e9fbb56d6; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — FVA: full visibility makes the limiting force hull an antipodal circle hull

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-antipodal-force-area`  
**Run type:** global compactness / exact limiting area-perimeter coupling  
**Target:** Target C post-ZF C-II  
**Depends on:** canonical C-II full visibility `C=C_*`, `H=H_*`; C34/C65 force-hull identification; ADA/DDM; ZK/JC  
**New external literature:** none  
**Computation:** decimal evaluation only; the optimizer is analytic

## LEVEL I STATUS

**STILL OPEN.**

ADA uses the positive-measure set of exact diameter directions only as a subset of the limiting force hull. In the fully visible C-II normalization there is more information: **every finite force-hull vertex is itself an actual source-diameter endpoint**. Since the complete normalized source hull tends to the radius-`1/2` disk, all force-hull vertices approach that circle and their diameter partners approach antipodes.

Therefore every Hausdorff limit of the normalized force hull is exactly the convex hull of a closed antipodal subset of the circle. This gives simultaneous exact formulas for its area and perimeter.

The resulting joint inequality raises the generic post-ZF pinned/contact floor from AAS's `0.5882283437...` to

$$
\boxed{
\lambda_{FVA}
=0.5937285472681860970\ldots .
}
\tag{FVA.1}

Here

\[
\lambda:=\lim\frac{e_{BB}+2s_C}{D}
$$

along a convergent post-ZF subsequence.

---

## 1. Full visibility pushes every force-hull vertex to the limiting circle

Let

$$
K_D:=D^{-1}(\operatorname{conv}A-c_D)
$$

be the normalized complete source hull, translated as in ADA. ADA proves

$$
K_D\to B:=\overline B(0,1/2)
$$

in Hausdorff distance after passage to a subsequence.

Let

$$
F_D:=D^{-1}(F-c_D)=\operatorname{conv}V_D,
$$

where `V_D=D^{-1}(B_+-c_D)` is the normalized loaded-terminal / force-hull vertex set.

The C-II normalization has full actual diameter visibility: `H=H_*`, and C34/C65 identifies the nonisolated source diameter endpoints with `B_+`. Thus every

$$
v\in V_D
$$

has a partner

$$
w\in V_D
$$

with

$$
|v-w|=1.
\tag{1.1}
$$

We first prove the uniform boundary statement

$$
\boxed{
\max_{v\in V_D}\operatorname{dist}(v,\partial B)\to0.
}
\tag{FVA.2}
$$

If not, choose a sequence `v_D in V_D` staying at least a fixed positive distance from `partial B`. Choose diameter partners `w_D in V_D`. Since `K_D->B`, after passage to a subsequence

$$
v_D\to v\in B,
\qquad
w_D\to w\in B.
$$

Equation (1.1) gives `|v-w|=1`. The only pair of points in the radius-`1/2` disk at distance one is an antipodal boundary pair. Hence

$$
v\in\partial B,
$$

contradicting the fixed interior distance. This proves FVA.2.

---

## 2. The limiting vertex set is antipodal

The finite compact sets `V_D` all lie in a common compact set. By Blaschke selection for compact subsets, pass to a further subsequence with

$$
V_D\to U
$$

in Hausdorff distance.

FVA.2 gives

$$
U\subseteq\partial B.
\tag{2.1}
$$

The set `U` is antipodal. Indeed, take any `u in U` and choose `v_D in V_D` with `v_D->u`. For each `v_D`, choose a diameter partner `w_D in V_D`. Passing to a further subsequence,

$$
w_D\to w\in U.
$$

Again `|u-w|=1` inside the radius-`1/2` disk, so necessarily

$$
w=-u.
$$

Thus

$$
\boxed{U=-U.}
\tag{FVA.3}
$$

Convex hull is continuous under Hausdorff convergence in finite dimensions, so

$$
\boxed{
F_D=\operatorname{conv}V_D
\to
F_\infty:=\operatorname{conv}U.
}
\tag{FVA.4}
$$

This is stronger than ADA: `F_infty` is **exactly** an antipodal circle hull.

---

## 3. Exact area and perimeter formulas

Represent `U` by a closed projective direction set

$$
S\subset\mathbb R/\pi\mathbb Z,
$$

so

$$
U=\{\pm\tfrac12u_\theta:\theta\in S\}.
$$

Let

$$
s:=\mu(S).
$$

Let the open complementary projective gaps have lengths

$$
g_1,g_2,\ldots,
\qquad
\sum_i g_i=\pi-s.
\tag{3.1}
$$

Each projective gap occurs twice on the full circle.

For radius `R=1/2`, replacing the two missing circular arcs of angular length `g_i` by their chords removes total area

$$
R^2(g_i-\sin g_i).
$$

Therefore

$$
\boxed{
A_\infty:=\operatorname{area}(F_\infty)
=
\frac14\left(s+\sum_i\sin g_i\right).
}
\tag{FVA.5}
$$

The boundary of `F_infty` consists of the retained circle subset plus the two chords spanning every projective gap. The retained full-circle angular measure is `2s`, contributing arc length `s` at radius `1/2`. Each projective gap pair contributes total chord length

$$
2\sin(g_i/2).
$$

Hence

$$
\boxed{
p:=\operatorname{per}(F_\infty)
=s+2\sum_i\sin(g_i/2).
}
\tag{FVA.6}
$$

Perimeter is continuous under planar convex Hausdorff convergence, so this `p` is also the limit of `P_F/D`.

---

## 4. Joint area-perimeter lower bound

Every gap obeys

$$
0\le g_i\le\sum_jg_j=\pi-s.
$$

Thus

$$
\cos(g_i/2)
\ge
\cos((\pi-s)/2)
=
\sin(s/2).
$$

Therefore

$$
\sin g_i
=2\sin(g_i/2)\cos(g_i/2)
\ge
2\sin(s/2)\sin(g_i/2).
$$

Summing and using FVA.6,

$$
\sum_i\sin g_i
\ge
\sin(s/2)(p-s).
$$

Insert this in FVA.5:

$$
\boxed{
A_\infty
\ge
\frac14\left[s+(p-s)\sin(s/2)\right].
}
\tag{FVA.7}

For fixed `p`, the function

\[
\phi_p(s):=s+(p-s)\sin(s/2)
$$

is nondecreasing on `0<=s<=p`, because

$$
\phi_p'(s)
=1-\sin(s/2)+\frac{p-s}{2}\cos(s/2)
\ge0.
$$

DDM/C67 gives

$$
s\ge y:=\lim h/D.
$$

Hence

$$
\boxed{
\liminf\frac{\operatorname{area}(F)}{D^2}
\ge
J(y,p)
:=
\frac14\left[y+(p-y)\sin(y/2)\right].
}
\tag{FVA.8}

This improves ADA whenever the actual perimeter is larger than the minimum antipodal-hull perimeter at density `y`.

---

## 5. Full visibility also gives the exact feasible perimeter interval

From FVA.6 and the projective gaps,

\[
\sum_i\sin(g_i/2)
\ge
\sin\left(\frac12\sum_i g_i\right)
=
\cos(s/2),
$$

using repeated `sin a+sin b>=sin(a+b)` on total half-gap angle at most `pi/2`.

Thus

$$
p\ge s+2\cos(s/2).
$$

The right side is increasing on `[0,pi]` because its derivative is `1-sin(s/2)>=0`. Since `s>=y`,

$$
\boxed{
p\ge y+2\cos(y/2).}
\tag{FVA.9}

On the other hand the exact post-ZF outer-walk identity is

\[
b=2h-Q-2s_Z\le2h,
$$

and `P_F<=b`, so

$$
\boxed{p\le2y.}
\tag{FVA.10}
$$

Cauchy's perimeter-diameter inequality also gives `p<=pi`.

Writing

$$
u:=p-y,
$$

we therefore have

$$
\boxed{
2\cos(y/2)
\le u
\le M(y):=\min\{y,\pi-y\}.
}
\tag{FVA.11}

The lower and upper endpoints first meet exactly at

\[
y_0:=2\rho,
\qquad
\rho=\cos\rho,
$$

because

$$
2\cos(y_0/2)=2\rho=y_0.
\tag{FVA.12}

---

## 6. Insert the exact joint geometry into ZK and JC

Let

\[
\lambda:=\lim\frac{e_{BB}+2s_C}{D}.
$$

The generic ZK/C40 attachment-cell capacity gives

$$
\limsup\frac1{D^2}
\sum_r\operatorname{area}(\operatorname{conv}A_r)
\le\frac\pi4\lambda^2.
\tag{6.1}
$$

Hence FVA.8 gives the attachment-gap lower bound

$$
\boxed{
\liminf\frac G{D^2}
\ge
\frac14\left[y+u\sin(y/2)\right]
-\frac\pi4\lambda^2.
}
\tag{FVA.13}

Because FVA.10 gives `p-y=u<=y`, the actual-perimeter JC minimum is exactly `u`. Since `e_BB/D<=lambda`, JC gives

\[
\boxed{
\limsup\frac G{D^2}
\le\frac{(\lambda+u)^2}{4\pi}.
}
\tag{FVA.14}

Therefore every survivor satisfies

\[
\boxed{
\pi\left[y+u\sin(y/2)\right]
-(\lambda+u)^2
-\pi^2\lambda^2
\le0.
}
\tag{FVA.15}

with `(y,u)` in the feasible region FVA.11.

---

## 7. Exact minimization over the feasible region

Define

\[
y_0:=2\rho
$$

and define `lambda_FVA` as the positive root of equality in FVA.15 at

$$
(y,u)=(y_0,y_0).
$$

Since

$$
\sin(y_0/2)=\sin\rho,
$$

this is

$$
\frac{\rho}{2}(1+\sin\rho)
-\frac\pi4\lambda^2
=
\frac{(\lambda+2\rho)^2}{4\pi}.
\tag{7.1}

Equivalently,

\[
\boxed{
(\pi^2+1)\lambda^2
+4\rho\lambda
+4\rho^2
-2\pi\rho(1+\sin\rho)
=0.
}
\tag{FVA.16}

Its positive root is

\[
\boxed{
\lambda_{FVA}
=0.5937285472681860970190\ldots .
}
\tag{FVA.17}

We prove that this is the global minimum required by FVA.15.

For fixed `y`, the left side of FVA.15 at `lambda=lambda_FVA` is a concave quadratic in `u`, with second derivative `-2`. Therefore its minimum on the interval FVA.11 occurs at one of the two endpoints.

### Lower endpoint: `u=2cos(y/2)`

Put

\[
F_L(y)
:=
\pi(y+\sin y)
-(\lambda_{FVA}+2\cos(y/2))^2
-\pi^2\lambda_{FVA}^2.
$$

At `y=y_0`, FVA.12 and FVA.16 give

$$
F_L(y_0)=0.
$$

Differentiate:

$$
F_L'(y)
=
\pi(1+\cos y)
+2(\lambda_{FVA}+2\cos(y/2))\sin(y/2)
>0
$$

for `y in[y_0,pi]`. Hence

$$
\boxed{F_L(y)\ge0.}
\tag{7.2}
$$

### Upper endpoint below `pi/2`: `u=y`

For `y in[y_0,pi/2]`, put

$$
F_{U,1}(y)
:=
\pi y(1+\sin(y/2))
-(\lambda_{FVA}+y)^2
-\pi^2\lambda_{FVA}^2.
$$

Again `F_{U,1}(y_0)=0`. Its derivative is

$$
F_{U,1}'(y)
=
\pi\left(1+\sin(y/2)+\frac y2\cos(y/2)\right)
-2(\lambda_{FVA}+y).
\tag{7.3}
$$

This is strictly positive on the interval. A deliberately coarse verification is enough: `lambda_FVA<0.6`, `y<=pi/2<1.6`, and `y/2>=rho>pi/6`, so `sin(y/2)>1/2`. Dropping the nonnegative last term in the parentheses,

$$
F_{U,1}'(y)
>
\frac{3\pi}{2}-2(0.6+1.6)
>4.71-4.4>0.
$$

Thus

$$
\boxed{F_{U,1}(y)\ge0.}
\tag{7.4}
$$

### Upper endpoint above `pi/2`: `u=pi-y`

For `y in[pi/2,pi]`, put

$$
F_{U,2}(y)
:=
\pi\left[y+(\pi-y)\sin(y/2)\right]
-(\lambda_{FVA}+\pi-y)^2
-\pi^2\lambda_{FVA}^2.
$$

It joins continuously to `F_{U,1}` at `pi/2`. Moreover

$$
F_{U,2}'(y)
=
\pi\left[
1-\sin(y/2)
+\frac{\pi-y}{2}\cos(y/2)
\right]
+2(\lambda_{FVA}+\pi-y)
>0.
\tag{7.5}
$$

Hence `F_{U,2}>0` throughout this interval.

Since the concave-in-`u` function is nonnegative at both feasible endpoints, it is nonnegative for every feasible `u`. Therefore FVA.15 cannot hold with `lambda<lambda_FVA`, because the left side decreases strictly with `lambda`.

This proves FVA.1.

---

## 8. Near-equality normal form

Equality in the scalar proof can occur only at

$$
\boxed{
y\to2\rho,\qquad u\to2\rho,\qquad p\to4\rho.}
\tag{FVA.18}

Thus any sequence approaching the new generic floor must simultaneously satisfy

\[
\frac hD\to2\rho,
\qquad
\frac{P_F}{D}\to4\rho
=2.9563405328\ldots .
\tag{FVA.19}

The limiting projective support must have measure exactly `2rho`, and equality in the gap inequalities forces its complement to be one projective interval. Therefore the limiting force hull is the convex hull of two antipodal circular arcs, separated by one antipodal pair of missing gaps.

The endpoint geometry is now very different from AAS's artificial `p->pi` optimizer. In particular the force hull has two macroscopic straight chord sides spanning the two missing arcs. This gives a concrete outer-walk target: post-ZF has `P_F<=b<=2h`, and FVA equality has `P_F/D -> 2h/D`, so

\[
\boxed{(b-P_F)/D\to0,\qquad (Q+2s_Z)/D\to0.}
\tag{FVA.20}

At the same time, almost the entire `O(D)` outer contact-walk budget required to replace the two macroscopic force-hull chord sides must be carried with asymptotically zero total chain-chord detour. This is the next geometric obstruction to attack.

---

## 9. Regression audit

- The key strengthening over ADA uses full C-II visibility: every force-hull vertex is an actual source-diameter endpoint with a partner in `B_+`. Without `H=H_*` the exact antipodal limiting hull need not follow.
- FVA does not assume finite central symmetry. It proves central symmetry only for the normalized Hausdorff limit.
- Arbitrary closed/fractal antipodal vertex limits are allowed; formulas FVA.5-FVA.6 use complementary gaps and remain valid.
- The scalar optimization uses only the generic ZK attachment-cell bound, not any near-zero/SCC assumption.
- The concavity in `u` is used in the correct direction: a concave function attains its minimum on a compact interval at an endpoint.
- `lambda_FVA<0.6` in (7.3) follows directly by substituting `0.6` into the strictly increasing quadratic FVA.16; the displayed decimal is not a logical dependency.
- Level I remains open. The theorem raises a necessary linear currency but does not yet convert it to the forbidden face inequality.

---

## 10. Next target

FVA has reduced generic near equality to a two-arc antipodal force hull with

\[
h/D\to2\rho,
\qquad
P_F/D\to4\rho,
\qquad
b-P_F=o(D).
$$

The most direct next theorem should quantify the outer contact-walk cost of the two macroscopic missing-arc chord sides.

Each missing projective gap has angle `pi-2rho`; its force-hull chord has normalized length

$$
\sin\frac{\pi-2\rho}{2}=\cos\rho=\rho.
$$

There are two antipodal chord sides, each of Euclidean length `rho D+o(D)`.

If those sides are not unit contacts, the outer contact walk must replace them by unit-edge paths between the same endpoints. FVA.20 says the **total** excess of those paths over their straight chord lengths is `o(D)`. Thus both replacement paths are asymptotic geodesics of length `rho D+o(D)`.

A closing route is to combine their two-strip geometry with the positive-contact barycenter/no-neutral-vertex theorem and the QSG/NSE series-rank restrictions. If every near-geodesic path must spend a fixed linear amount of transverse/face defect in the fully visible C-II core, FVA equality is impossible and the generic `0.593728...` floor gains a uniform gap.

## 11. Compact handoff

```text
FVA:
Because H=H_* and C34/C65 identify F=conv(B_+), every force-hull vertex has an actual
diameter partner. The complete source hull tends to the radius-1/2 disk. Therefore
all force-hull vertices tend uniformly to the circle; after Hausdorff convergence their
vertex set U is closed and antipodal, and F_inf=conv(U).

Let projective support S have measure s and complementary gaps g_i, sum g_i=pi-s.
Exact radius-1/2 formulas:
    A=(1/4)[s+sum sin g_i],
    p=s+2 sum sin(g_i/2).
Thus
    A >= (1/4)[s+(p-s)sin(s/2)]
      >= (1/4)[y+(p-y)sin(y/2)],
where y=lim h/D and DDM gives s>=y.
Also
    p >= s+2cos(s/2) >= y+2cos(y/2).
Outer walk gives p<=2y and Cauchy p<=pi. With u=p-y:
    2cos(y/2)<=u<=min(y,pi-y).

Generic ZK cells + JC give
    pi[y+u sin(y/2)]-(lambda+u)^2-pi^2 lambda^2 <=0,
    lambda=lim(e_BB+2s_C)/D.
At fixed y this is concave in u, so check endpoints. For lambda=lambda_FVA defined by
equality at y=u=2rho:
    lower endpoint derivative = pi(1+cos y)+2(lambda+2cos(y/2))sin(y/2)>0;
    upper endpoint derivatives are also strictly positive below and above pi/2.
Hence the global minimum is y=u=2rho and
    (pi^2+1)lambda^2+4rho lambda+4rho^2
      -2pi rho(1+sin rho)=0.
Positive root:
    lambda_FVA=0.5937285472681860970....
Near equality forces y->2rho, p->4rho, and a two-arc antipodal circle hull with two
macroscopic chord sides of length rho D each; simultaneously b-P_F=o(D).
```

> Generated reading edition · [exact source](../../../docs/reports/target_c_rsr_dirichlet_detour_joint_gap_2026-09-10.md) · source SHA-256 `02d03f7eb44c7f079969965c76345c252331f00e7779c6d683604c96811f6b0e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B80C6EC70D3F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — RSR plus Dirichlet detour gives a strictly stronger generic post-ZF floor

**Date:** 2026-09-10  
**Repository base:** `ff31de4783ff49173d9f4bfdf61364735ff5a590`  
**Run type:** exact cavity refinement / compact variational strengthening  
**Target:** Target C, C-II after ZF  
**Depends on:** DB, DD, JC/ZG/GU, FSDB, RSJ  
**External input:** none beyond the already imported Rogalski–Saint Raymond theorem  
**Computation:** none in the theorem

## LEVEL I STATUS

`STILL OPEN`.

RSJ proves the generic post-ZF surplus floor

$$
\lambda_R=0.5921405436062881570\ldots
$$

and excludes its equality endpoint.  This report converts that qualitative endpoint
exclusion into a new explicit variational inequality by combining the RSR force-hull
area floor with the already proved Dirichlet-dual outer-pocket detour theorem DD.

Let

$$
\lambda_D:=\frac{e_{BB}+2s_C}{D},
\qquad
 y_D:=\frac hD,
\qquad
 p_D:=\frac{\operatorname{per}F}{D}.
$$

For any convergent post-ZF subsequence write the limits as `lambda,y,p`.  Define

$$
\Phi(y):=\frac{y+\sin y}{4},
\qquad
\Psi(p):=\frac\pi{(\pi-2)^2}\left(\frac p2-1\right)^2,
\tag{RD.1}
$$

$$
A(y,p):=\max\{\Phi(y),\Psi(p)\},
\tag{RD.2}
$$

and

$$
\boxed{
\Delta(y,p):=
\frac{2}{\sqrt3}\,y^{3/2}\sqrt{2y-p}.
}
\tag{RD.3}
$$

Then every post-ZF survivor limit satisfies the new necessary inequality

$$
\boxed{
A(y,p)-\frac\pi4\lambda^2
\le \Delta(y,p).
}
\tag{RD.4}
$$

Together with the retained actual-perimeter JC inequality,

$$
\boxed{
A(y,p)-\frac\pi4\lambda^2
\le \frac{(\lambda+p-y)^2}{4\pi},
}
\tag{RD.5}
$$

this defines a compact variational threshold `lambda_RD` satisfying

$$
\boxed{
\liminf_{D\to\infty}\lambda_D
\ge\lambda_{RD}>\lambda_R.
}
\tag{RD.6}
$$

The strict improvement is proved without numerical optimization.  A later report will
solve the reduced optimizer and certify a decimal value.

---

## 1. Full normalized geometric domain

Put

$$
z_D:=\frac{Q+2s_Z}{D}.
$$

Along a convergent subsequence write `z_D->z`.  DB gives

$$
0\le z\le y-2\cos(y/2)\le y.
\tag{1.1}
$$

The exact outer-walk identity is

$$
b=2h-Q-2s_Z,
$$

so

$$
\frac bD\to 2y-z.
\tag{1.2}
$$

Because the convex force hull is the convex hull of that closed contact walk,

$$
p\le2y-z\le2y.
\tag{1.3}
$$

On the other side, the force-hull vertices are unit separated, hence

$$
\operatorname{per}F\ge q\ge h,
$$

so

$$
p\ge y.
\tag{1.4}
$$

DB actually gives the stronger lower perimeter bound

$$
\boxed{
p\ge g(y):=y+2\cos(y/2).}
\tag{1.5}
$$

Finally Cauchy's diameter-perimeter bound gives `p<=pi`, and `h<=q<=per(F)` gives
`y<=pi`.  Thus every limit lies in the compact region

$$
\boxed{
\mathcal R=
\left\{(y,p):
2\rho\le y\le\pi,
\quad
g(y)\le p\le\min\{2y,\pi\}
\right\}.
}
\tag{1.6}
$$

Because `p<=2y`, the actual-perimeter JC branch simplifies everywhere on this domain:

$$
\min\{y,p-y\}=p-y.
\tag{1.7}
$$

---

## 2. DD plus exceptional faces gives a detour-sensitive total cavity bound

DD proves

$$
H_{out}
\le
\frac1{\sqrt6}(x_B+a)^{3/2}
\sqrt{b-\operatorname{per}F},
\tag{2.1}
$$

where `a` is the number of missing force-hull side contacts.  Trivially `a<=q`, while
`x_B=b-q`.  Therefore

$$
\boxed{x_B+a\le b.}
\tag{2.2}
$$

Hence

$$
H_{out}
\le
\frac1{\sqrt6}b^{3/2}
\sqrt{b-\operatorname{per}F}.
\tag{2.3}
$$

JC proves for the bounded exceptional contact faces

$$
A_{exc}
\le\frac{Q^2+O(D)}{4\pi}.
\tag{2.4}
$$

Since `0<=Q<=Q+2s_Z`, division by `D^2` gives

$$
\limsup\frac{A_{exc}}{D^2}
\le\frac{z^2}{4\pi}.
\tag{2.5}
$$

Combining (1.2), (2.3), and (2.5),

$$
\limsup\frac{H_{out}+A_{exc}}{D^2}
\le
C(2y-z)^{3/2}\sqrt{2y-z-p}
+\frac{z^2}{4\pi},
\tag{2.6}
$$

where

$$
C:=\frac1{\sqrt6}.
\tag{2.7}
$$

The square root is real by (1.3).

---

## 3. The worst cavity capacity occurs at zero face/mixed defect

For fixed feasible `(y,p)`, define

$$
F(z):=
C(2y-z)^{3/2}\sqrt{2y-z-p}
+\frac{z^2}{4\pi}.
\tag{3.1}
$$

Put

$$
B=2y-z,
\qquad
U=B-p\ge0.
$$

For `U>0`, direct differentiation gives

$$
F'(z)
=-\frac C2\sqrt{\frac BU}\,(3U+B)
+\frac{z}{2\pi}.
\tag{3.2}
$$

Now `0<=U<=B`, so

$$
\sqrt{B/U}\ge1,
\qquad
3U+B\ge B.
$$

Also DB gives `z<=y`, hence

$$
z\le 2y-z=B.
$$

Therefore

$$
F'(z)
\le
-\frac{CB}{2}+\frac{B}{2\pi}
=
\frac B2\left(\frac1\pi-\frac1{\sqrt6}\right)<0,
\tag{3.3}
$$

because `pi>3>sqrt(6)`.  The conclusion extends to the `U=0` endpoint by
continuity.  Hence

$$
\boxed{F(z)\le F(0).}
\tag{3.4}
$$

This monotonicity is the key simplification: giving perimeter budget to exceptional
faces or extra mixed dependence decreases the total quadratic cavity capacity more
than the exceptional-face isoperimetric term can recover.

At `z=0`,

$$
F(0)
=\frac1{\sqrt6}(2y)^{3/2}\sqrt{2y-p}
=\boxed{\frac{2}{\sqrt3}y^{3/2}\sqrt{2y-p}}.
\tag{3.5}
$$

Thus

$$
\boxed{
\limsup\frac{H_{out}+A_{exc}}{D^2}
\le\Delta(y,p).
}
\tag{3.6}
$$

---

## 4. Convert cavity capacity into a second surplus obstruction

ZG gives

$$
G
\le H_{out}+A_{exc}+O(D),
\tag{4.1}
$$

where

$$
G=\operatorname{area}F-
\sum_r\operatorname{area}(P_r).
$$

GU gives

$$
\limsup\frac{\sum_r\operatorname{area}(P_r)}{D^2}
\le\frac\pi4\lambda^2.
\tag{4.2}
$$

FSDB plus RSJ give

$$
\liminf\frac{\operatorname{area}F}{D^2}
\ge A(y,p).
\tag{4.3}
$$

Combining (3.6), (4.1), (4.2), and (4.3) proves RD.4:

$$
A(y,p)-\frac\pi4\lambda^2
\le\Delta(y,p).
$$

Equivalently, define

$$
D_{RD}(y,p):=
\sqrt{
\max\left\{
0,
\frac4\pi\bigl(A(y,p)-\Delta(y,p)\bigr)
\right\}
}.
\tag{4.4}
$$

Then every survivor satisfies

$$
\boxed{\lambda\ge D_{RD}(y,p).}
\tag{4.5}
$$

Independently, RSJ/JC gives RD.5.  Let

$$
R(A,m):=
\frac{\sqrt{4\pi(\pi^2+1)A-\pi^2m^2}-m}{\pi^2+1}.
\tag{4.6}
$$

Since `m=p-y`, RD.5 is equivalent to

$$
\boxed{
\lambda\ge
J_{RD}(y,p):=R(A(y,p),p-y).
}
\tag{4.7}
$$

Thus every survivor limit obeys

$$
\boxed{
\lambda\ge
M_{RD}(y,p):=
\max\{J_{RD}(y,p),D_{RD}(y,p)\}.
}
\tag{4.8}
$$

---

## 5. A new exact variational constant

Define

$$
\boxed{
\lambda_{RD}:=
\min_{(y,p)\in\mathcal R}M_{RD}(y,p).
}
\tag{5.1}
$$

All functions are continuous on `mathcal R` (with the displayed `max{0,...}` at the
square-root threshold), so the minimum exists.  Equation (4.8) proves

$$
\liminf\lambda_D\ge\lambda_{RD}.
\tag{5.2}
$$

This is already constructive: `lambda_RD` is the minimum of an explicit elementary
function on an explicit compact two-dimensional region.

---

## 6. Strict improvement over the current generic RSJ floor

RSJ proves that

$$
J_{RD}(y,p)
\ge\lambda_R
$$

on a domain at least as large as `mathcal R`, and that equality occurs at the unique
point

$$
(y,p)=(y_R,2y_R).
\tag{6.1}
$$

At that point the detour vanishes:

$$
\Delta(y_R,2y_R)=0.
$$

Also

$$
A(y_R,2y_R)=\Phi(y_R)=\Psi(2y_R)>0.
$$

Therefore

$$
D_{RD}(y_R,2y_R)
=\sqrt{\frac{4A(y_R,2y_R)}\pi}.
\tag{6.2}
$$

The defining RSJ equality is

$$
A(y_R,2y_R)-\frac\pi4\lambda_R^2
=
\frac{(\lambda_R+y_R)^2}{4\pi}>0.
\tag{6.3}
$$

Hence

$$
\boxed{
D_{RD}(y_R,2y_R)>\lambda_R.
}
\tag{6.4}
$$

Suppose `lambda_RD=lambda_R`.  Let `(y_0,p_0)` attain the minimum in (5.1).  Since

$$
M_{RD}\ge J_{RD}\ge\lambda_R,
$$

equality would force

$$
J_{RD}(y_0,p_0)=\lambda_R.
$$

By RSJ uniqueness, `(y_0,p_0)=(y_R,2y_R)`.  But (6.4) gives

$$
M_{RD}(y_R,2y_R)>\lambda_R,
$$

a contradiction.  Therefore

$$
\boxed{\lambda_{RD}>\lambda_R.}
\tag{6.5}
$$

This proves RD.6.

The argument is stronger than the earlier qualitative RSJ endpoint exclusion: the
same detour mechanism has now been inserted into the full compact feasible region, so
the positive gap is represented by an explicit variational constant rather than an
unspecified compactness epsilon.

---

## 7. Endpoint topology recovered automatically

The old RSJ scalar endpoint had

$$
p=2y.
$$

The exact outer-walk identity then forces

$$
\frac{Q+2s_Z}{D}\to0,
$$

because `p<=2y-z`.  DD then forces `H_out=o(D^2)`, while `Q=o(D)` forces
`A_exc=o(D^2)`.  Thus RD also gives a C-II-native explanation of why the RSJ endpoint
cannot carry its required positive quadratic cavity gap, without using the equality
classification in the external RSR theorem.

The new variational inequality is the quantitative form of this observation.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| compact domain `mathcal R` | proved | DB lower perimeter + outer-walk and Cauchy upper bounds |
| `x_B+a<=b` | proved | `x_B=b-q`, `a<=q` |
| total cavity bound (2.6) | proved asymptotically | DD + JC exceptional-face isoperimetry |
| cavity capacity decreases with `z` | proved | derivative estimate (3.2)--(3.3) |
| RD.4 | proved asymptotically | ZG/GU + FSDB/RSR area lower bound |
| variational floor `lambda_RD` | proved | compact minimization |
| `lambda_RD>lambda_R` | proved exactly | RSJ unique optimizer + positive DD obstruction there |
| explicit decimal for `lambda_RD` | not claimed here | deferred to analytic optimizer/certification |
| Level I | still open | no upper contradiction for all high-surplus survivors |

---

## 9. Next run

Solve the compact optimizer in (5.1).  For fixed `y`, the JC threshold decreases with
`p` until the FSDB/RSR area crossover while the DD threshold increases with `p`.
Numerical reconnaissance indicates the global minimum occurs when three equalities
meet:

$$
\Phi(y)=\Psi(p),
$$

$$
A-\frac\pi4\lambda^2
=\frac{(\lambda+p-y)^2}{4\pi},
$$

$$
A-\frac\pi4\lambda^2
=\frac{2}{\sqrt3}y^{3/2}\sqrt{2y-p}.
$$

The next theorem should prove that localization analytically and then certify the
resulting one-dimensional root.

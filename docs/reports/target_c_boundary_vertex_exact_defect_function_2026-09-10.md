<!-- theorem-state: {"artifact_id":"ART-17F57974DF75","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact boundary-vertex isodiametric defect function

**Date:** 2026-09-10  
**Branch base:** `5f36ed98f217cd9bb2c8f9a70423592cac980147`  
**Depends on:** BV on this branch  
**External input:** the same Bonnesen concentric-annulus theorem used in BV  
**Run type:** exact quantitative convex geometry / feedback coefficient  
**Target:** Target C, C-II after ZF

## LEVEL I STATUS

`STILL OPEN`.

BV used the simple rational implication `d<=3/5 => x>=1/20` in its Bonnesen/support-net
argument.  The same proof has an exact one-parameter form.

For `0<c<1`, let `kappa(c)` be the unique root in

\[
0<x<3-2\sqrt2
\]

of

\[
\boxed{
c(1+x)^3=1-6x+x^2.}
\tag{BVE.1}
\]

Define

\[
\boxed{
C(c):=\frac\pi4-\frac{\kappa(c)^2}{4}.}
\tag{BVE.2}
\]

### Theorem BVE — exact boundary-sharing defect

Let `F` be a compact convex planar set of diameter `D`, and let `K subset F` be a
nondegenerate convex polygon whose vertices all lie on `partial F`.  If

\[
\operatorname{diam}K\le cD,
\qquad 0<c<1,
\]

then

\[
\boxed{
\operatorname{area}K
\le C(c)\operatorname{diam}(K)^2.
}
\tag{BVE.3}

The function `kappa(c)` is strictly decreasing, so `C(c)` is strictly increasing.
Thus a smaller allowed attachment-cell diameter gives a larger uniform area defect.

---

## 1. Existence and monotonicity of `kappa`

Put

\[
H_c(x)=c(1+x)^3-(1-6x+x^2).
\tag{1.1}
\]

Then

\[
H_c(0)=c-1<0.
\]

At

\[
x_0=3-2\sqrt2,
\]

we have `1-6x_0+x_0^2=0`, so

\[
H_c(x_0)=c(1+x_0)^3>0.
\]

Moreover on `[0,x_0]`,

\[
\frac{\partial H_c}{\partial x}
=3c(1+x)^2+6-2x>0.
\tag{1.2}
\]

Hence BVE.1 has exactly one root `kappa(c)` in `(0,x_0)`.

Implicit differentiation gives

\[
\kappa'(c)
=-\frac{(1+\kappa)^3}
{3c(1+\kappa)^2+6-2\kappa}<0.
\tag{1.3}
\]

Therefore `C(c)` is strictly increasing.

At `c=3/5`, BVE.1 becomes

\[
3x^3+4x^2+39x-2=0,
\tag{1.4}
\]

whose positive root is

\[
\kappa(3/5)=0.0510050225668455\ldots .
\]

In particular `kappa(3/5)>51/1000`, since substitution into the strictly increasing
left side of (1.4) gives a negative value at `51/1000`.  Thus BVE strictly strengthens
the rational BV coefficient `1/1600`.

---

## 2. Exact radius bound from the BV support-normal argument

Normalize `D=1`.  Write

\[
d=\operatorname{diam}K\le c,
\qquad
A=\operatorname{area}K,
\]

and define the isodiametric deficit

\[
\varepsilon=\pi d^2-4A.
\tag{2.1}
\]

Bonnesen plus `per(K)<=pi d`, exactly as in BV, gives concentric disks

\[
\overline B(o,d/2-w)
\subseteq K
\subseteq
\overline B(o,d/2+w)
\tag{2.2}
\]

with

\[
0\le w\le\frac{\sqrt\varepsilon}{2}.
\tag{2.3}
\]

Set

\[
x=\frac{2w}{d}.
\tag{2.4}
\]

Suppose `x<3-2sqrt(2)`, so the normal-net angle below is less than `pi/2`.  BV's
argument gives, with

\[
\cos\alpha=\frac{1-x}{1+x},
\]

a `2alpha`-net of force-hull support normals through vertices of `K`.  Every such
support line is at distance at most

\[
R=\frac d2(1+x)
\]

from `o`.  Therefore

\[
\operatorname{diam}F
\le\frac{2R}{\cos(2\alpha)}.
\tag{2.5}
\]

Now

\[
\cos(2\alpha)
=2\left(\frac{1-x}{1+x}\right)^2-1
=\frac{1-6x+x^2}{(1+x)^2}.
\tag{2.6}
\]

Substitution into (2.5) yields the exact bound

\[
\boxed{
\operatorname{diam}F
\le
 d\,\frac{(1+x)^3}{1-6x+x^2}.
}
\tag{2.7}

This is the quantitative core hidden behind BV's rational evaluation.

---

## 3. Proof of BVE

Suppose contrary to BVE.3 that

\[
A>C(c)d^2
=\left(\frac\pi4-\frac{\kappa(c)^2}{4}\right)d^2.
\]

Then

\[
\varepsilon
=\pi d^2-4A
<\kappa(c)^2d^2.
\]

By (2.3)--(2.4),

\[
x\le\frac{\sqrt\varepsilon}{d}<\kappa(c)<3-2\sqrt2.
\tag{3.1}
\]

The function

\[
x\mapsto\frac{(1+x)^3}{1-6x+x^2}
\]

is strictly increasing on this interval.  Since `d<=c`, (2.7) and (3.1) give

\[
\operatorname{diam}F
<
 c\frac{(1+\kappa(c))^3}{1-6\kappa(c)+\kappa(c)^2}
=1
\]

by the defining equation BVE.1.  This contradicts the normalization
`diam(F)=1`.  Therefore BVE.3 holds.

---

## 4. Surplus-dependent attachment coefficient

Return to Target C.  Let

\[
\lambda
=\limsup\frac{e_{BB}+2s_C}{D}<1.
\tag{4.1}
\]

ZK gives

\[
\sum_r\delta_r
\le6+e_{BB}+2s_C,
\]

and C44 gives

\[
\operatorname{diam}(\operatorname{conv}A_r)
\le\delta_r+2.
\]

Fix `eta>0` with `lambda+eta<1`.  For all sufficiently large `D`, every attachment
cell therefore has diameter at most `(lambda+eta)D`.  Apply BVE with
`c=lambda+eta` to every cell:

\[
\operatorname{area}(\operatorname{conv}A_r)
\le C(\lambda+\eta)(\delta_r+2)^2.
\]

Summing and using `c_I=O(D)`,

\[
\sum_r(\delta_r+2)^2
\le\left(\sum_r\delta_r\right)^2+O(D).
\]

Divide by `D^2`, pass to the limit, and then let `eta downarrow0`.  Continuity of
`kappa`, hence of `C`, gives

\[
\boxed{
\limsup\frac1{D^2}
\sum_r\operatorname{area}(\operatorname{conv}A_r)
\le
G(\lambda):=C(\lambda)\lambda^2.
}
\tag{BVE.4}

Since `C(lambda)>0` and is strictly increasing, `G(lambda)` is strictly increasing on
`(0,1)`.

This is stronger than both GU and the constant-coefficient BV refinement.  The
attachment capacity now feeds the candidate surplus back into its own geometric defect.

---

## 5. Strengthened RSR/DD inequalities

Every post-ZF survivor limit with `lambda<1` must now satisfy

\[
\boxed{
A(y,p)-G(\lambda)
\le\frac{(\lambda+p-y)^2}{4\pi},
}
\tag{5.1}
\]

and

\[
\boxed{
A(y,p)-G(\lambda)
\le\frac2{\sqrt3}y^{3/2}\sqrt{2y-p}.
}
\tag{5.2}

The fixed-`y` optimizer geometry of RX is unchanged because `G` depends only on
`lambda`, not on `y` or `p`, and is strictly increasing.  The next report solves this
feedback system and certifies the next explicit generic floor.

---

## 6. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| unique `kappa(c)` | proved | monotone cubic on `(0,3-2sqrt2)` |
| exact force-hull diameter bound (2.7) | proved | BV support-normal net with algebra retained |
| BVE cellwise defect | proved | Bonnesen width + monotonicity + defining root |
| surplus-dependent capacity `G(lambda)` | proved asymptotically | ZK/C44 + cellwise BVE + `eta->0` |
| `G` strictly increasing | proved | `C` and `lambda^2` both increase |
| feedback RSR/DD system | proved | replace attachment capacity in RD |
| new optimized decimal | not claimed here | next report |
| Level I | still open | high-surplus branch remains |

---

## 7. Next run

Solve (5.1)--(5.2) exactly as in RX.  On the area crossover `p=p_e(y)`, define the
JC root and DD root using `G(lambda)` rather than a quadratic coefficient.  The DD root
strictly decreases because its right-side target `E(y)` decreases and `G` increases;
the JC root strictly increases by implicit differentiation.  Their unique intersection
is the new global optimizer.
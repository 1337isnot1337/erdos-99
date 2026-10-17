> Generated reading edition · [exact source](../../../docs/reports/target_c_fs_perimeter_area_diameter_hull_2026-09-10.md) · source SHA-256 `122b141d8ca23b1ab2148015eb26916841a437c09f0c2366dc1bc8c7465f1351`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-9913C4BF17AD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fs_perimeter_area_diameter_hull_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=a96a87733b66c814523fbed0a486eff848bf3a83; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — diameter-pair strengthening of the FS perimeter/area tradeoff

**Date:** 2026-09-10  
**Branch base:** `f977f2d0d25f5022c2a587e59cab38375d85caee`  
**Depends on:** FD and QPA on this branch  
**Run type:** exact convex-geometric refinement  
**Target:** Target C, C-II after ZF  
**External input:** none

## LEVEL I STATUS

`STILL OPEN`.

The QPA theorem lower-bounds the area of the central symmetral from a centered inball.
That leaves unused the exact fact that the symmetral has diameter `D`.  A centrally
symmetric diameter-`D` body contains an antipodal pair at radius `D/2`; adjoining that
pair to the centered inball gives a strictly larger explicit area lower bound.

Retain

```math
f(a)=2\left(\arcsin a+\sqrt{1-a^2}\right),
\qquad
\alpha=f^{-1}:[2,\pi]\to[0,1]
\tag{QPD.1}
```

from QPA.  Define

```math
\boxed{
\Theta(a):=
\frac14\left[
\pi a^2
+2a\sqrt{1-a^2}
-2a^2\arccos a
\right],
\qquad 0\le a\le1,
}
\tag{QPD.2}
```

and

```math
\boxed{
\Omega(p):=\Theta(\alpha(p)),
\qquad 2\le p\le\pi.
}
\tag{QPD.3}
```

Then every post-ZF force hull `F` with `P=per(F)` satisfies

```math
\boxed{
\operatorname{area}F
\ge
D^2\Omega(P/D)-L_DP-\pi L_D^2,
}
\tag{QPD.4}
```

where `L_D` is the FS.4 error used in FD and QPA.  Hence if `P/D->p`,

```math
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}\ge\Omega(p).
}
\tag{QPD.5}
```

For every `2<p<pi`,

```math
\boxed{
\Omega(p)>\Psi(p),
}
\tag{QPD.6}
```

so QPD strictly strengthens QPA away from the disk endpoint.

---

## 1. Exact diameter endpoints in a centrally symmetric body

Let `K` be centrally symmetric about `0` and have diameter `D`.  As in QPA,

```math
K\subseteq \overline B(0,R),
\qquad R=D/2.
\tag{1.1}
```

Because the diameter is attained, choose `x,y in K` with `|x-y|=D`.  Both satisfy
`|x|,|y|<=R`, so

```math
D=|x-y|\le |x|+|y|\le2R=D.
```

Equality throughout the triangle inequality forces

```math
y=-x,
\qquad
|x|=|y|=R.
\tag{1.2}
```

Thus every centrally symmetric diameter-`D` body contains an antipodal diameter pair
at the boundary of its radius-`R` containing disk.

Let

```math
r=\min_{|u|=1}h_K(u),
\qquad
a=r/R.
\tag{1.3}
```

QPA proves

```math
\overline B(0,r)\subseteq K
\tag{1.4}
```

and, if `p=per(K)/D`,

```math
a\ge\alpha(p).
\tag{1.5}
```

After rotation, (1.2) and (1.4) imply

```math
\boxed{
\operatorname{conv}
\left(\overline B(0,r)\cup\{(-R,0),(R,0)\}\right)
\subseteq K.
}
\tag{1.6}
```

---

## 2. Area of the inball-plus-diameter hull

Normalize temporarily to `R=1`, so the disk radius is `a`.  Consider the right
external point `P=(1,0)`.  Its two tangent points on the radius-`a` disk are

```math
T_\pm=\left(a^2,\ \pm a\sqrt{1-a^2}\right).
\tag{2.1}
```

The triangle `PT_+T_-` has area

```math
a(1-a^2)^{3/2}.
\tag{2.2}
```

The circular segment of the radius-`a` disk cut off by the chord `T_+T_-` has area

```math
a^2\left(
\arccos a-a\sqrt{1-a^2}
\right).
\tag{2.3}
```

Therefore adjoining `P` to the disk adds exactly

```math
\begin{aligned}
\Delta(a)
&=a(1-a^2)^{3/2}
-a^2\arccos a
+a^3\sqrt{1-a^2}\\
&=\boxed{
a\sqrt{1-a^2}-a^2\arccos a.
}
\end{aligned}
\tag{2.4}
```

The left antipodal point contributes the same disjoint exterior region.  Hence

```math
\operatorname{area}
\operatorname{conv}
\left(\overline B(0,a)\cup\{(-1,0),(1,0)\}\right)
=\pi a^2+2\Delta(a).
\tag{2.5}
```

Restoring `R=D/2` multiplies area by `R^2=D^2/4`, so (1.6) yields

```math
\boxed{
\frac{\operatorname{area}K}{D^2}
\ge\Theta(a).
}
\tag{2.6}
```

The function `Theta` is strictly increasing.  Differentiating QPD.2 gives

```math
\boxed{
\Theta'(a)
=\frac12\sqrt{1-a^2}+a\arcsin a>0
\qquad(0\le a\le1).
}
\tag{2.7}
```

Combining (1.5), (2.6), and (2.7),

```math
\boxed{
\frac{\operatorname{area}K}{D^2}
\ge\Theta(\alpha(p))=\Omega(p).
}
\tag{2.8}
```

This is the centrally symmetric QPD inequality.

---

## 3. Strict improvement over QPA

QPA used only the centered disk and obtained

```math
\Psi(p)=\frac\pi4\alpha(p)^2.
```

For `a in (0,1)`, QPD adds

```math
\Theta(a)-\frac\pi4a^2
=\frac12\left(
 a\sqrt{1-a^2}-a^2\arccos a
\right).
\tag{3.1}
```

Put `a=cos theta`, with `0<theta<pi/2`.  The bracket becomes

```math
\cos\theta\left(\sin\theta-\theta\cos\theta\right).
\tag{3.2}
```

The function

```math
q(\theta)=\sin\theta-\theta\cos\theta
```

satisfies

```math
q(0)=0,
\qquad
q'(\theta)=\theta\sin\theta>0.
```

Thus the bracket is strictly positive for `0<a<1`, proving QPD.6.

At `p=pi`, `alpha(p)=1` and

```math
\Omega(\pi)=\Theta(1)=\frac\pi4,
\tag{3.3}
```

so the bound still lands exactly on the FD disk endpoint.

---

## 4. Transfer to the force hull

For the force hull, use the central symmetral

```math
S=\frac12((F-o)-(F-o)).
```

FD gives

```math
\operatorname{diam}S=D,
\qquad
\operatorname{per}S=P,
\tag{4.1}
```

and

```math
0\le\operatorname{area}S-\operatorname{area}F
\le L_DP+\pi L_D^2.
\tag{4.2}
```

Apply (2.8) to `S` and subtract (4.2):

```math
\operatorname{area}F
\ge D^2\Omega(P/D)-L_DP-\pi L_D^2.
```

This proves QPD.4.  Since `P<=pi D` and `L_D=O(D^{3/4})`, the error is `o(D^2)`,
which proves QPD.5.

---

## 5. Exact interaction with the DB lower perimeter curve

DB gives the asymptotic constraint

```math
p\ge g(y):=y+2\cos(y/2),
\qquad
2\rho\le y\le\pi.
\tag{5.1}
```

There is an exact simplification on this lower-perimeter curve.  Since

```math
f(\sin(y/2))
=2\left(
\frac y2+\cos(y/2)
\right)
=g(y),
\tag{5.2}
```

we have

```math
\alpha(g(y))=\sin(y/2).
\tag{5.3}
```

Substitute this into QPD.2.  Because

```math
\arccos(\sin(y/2))=\frac{\pi-y}{2},
```

one obtains

```math
\boxed{
\Omega(g(y))
=\frac14\left[
y\sin^2(y/2)+\sin y\right].
}
\tag{5.4}
```

FSDB gives

```math
\Phi(y)=\frac{y+\sin y}{4}.
\tag{5.5}
```

Therefore

```math
\boxed{
\Phi(y)-\Omega(g(y))
=\frac y4\cos^2(y/2)>0
\qquad(0<y<\pi).
}
\tag{5.6}
```

So FSDB is strictly stronger on the minimum-perimeter DB boundary, while QPD becomes
stronger as `p` approaches `pi`.  The unique crossing between those two area currencies
is therefore an interior perimeter point for every `y<pi`.

This identity is the main reason the full `(y,p)` optimization can be solved cleanly.

---

## 6. Derivative needed for the optimization

For completeness, write `a=alpha(p)`.  Since

```math
f'(a)=2\frac{1-a}{\sqrt{1-a^2}},
```

QPD.2 and the inverse-function theorem give

```math
\boxed{
\Omega'(p)
=
\frac{1+a}{4}
+
\frac{a\sqrt{1-a^2}\arcsin a}{2(1-a)}.
}
\tag{6.1}
```

Post-ZF DB implies

```math
p\ge g(2\rho)=4\rho.
\tag{6.2}
```

Also `rho>7/10`, because `cos(7/10)>1-(7/10)^2/2>7/10` and `cos x-x`
is strictly decreasing on the positive root interval.  Hence

```math
4\rho>\frac{14}{5}.
\tag{6.3}
```

On the other hand

```math
f(1/2)=\frac\pi3+\sqrt3
<\frac{22}{21}+\frac74
=\frac{235}{84}
<\frac{14}{5}.
\tag{6.4}
```

Thus every feasible post-ZF `p` has

```math
a=\alpha(p)>1/2.
\tag{6.5}
```

Using (6.1), `a>=1/2`, and monotonicity of each positive factor in the second term,

```math
\Omega'(p)
\ge
\frac38+\frac{\pi\sqrt3}{24}
>\frac{7}{12}
>\frac12.
\tag{6.6}
```

The rough rational lower bound uses `pi>3` and `sqrt(3)>5/3`.

This derivative gap is enough to show that the FSDB/QPD crossover perimeter moves
more slowly than `y`, which will make the global JC optimization one-dimensional.

---

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| central symmetral contains an antipodal radius-`D/2` pair | proved | equality in the triangle inequality for an attained diameter |
| inball-plus-antipodes area formula | proved | tangent triangle minus circular segment |
| `Theta` strictly increasing | proved | explicit positive derivative |
| QPD finite force-hull area bound | proved | QPA inradius bound + diameter hull + FD area transfer |
| strict improvement over QPA for `2<p<pi` | proved | `sin(theta)-theta cos(theta)>0` |
| DB-boundary identity QPD.5.4 | proved | exact substitution `alpha(g(y))=sin(y/2)` |
| global optimized pinned/contact constant | not claimed here | separated into the next theorem/commit |
| Level I | still open | no C-II contradiction yet |

---

## 8. Next run

Replace `Psi` by the stronger `Omega` in the QPA/JC feasible-region inequality and
solve the compact optimization exactly.  The candidate transition is the unique
`y_c in (2rho,pi/2)` satisfying

```math
\Omega(2y_c)=\Phi(y_c).
```

The required proof is monotonic: below `y_c`, the best perimeter can reach `2y` before
QPD dominates; above `y_c`, the best perimeter is the unique FSDB/QPD crossover.

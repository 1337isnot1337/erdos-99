> Generated reading edition · [exact source](../../../docs/reports/integrator_joint_cavity_exclusion_2026-09-09.md) · source SHA-256 `fe9ab7658ee75b0f3a10e96ebdc02c8975703e67cbc8d6b84de4012e17ebaa90`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C3B36082BFC5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Erdős Problem #99 — ambient-force geometry strengthens the joint cavity exclusion

**Date:** 2026-09-09
**Run type:** cross-target conditional branch-exclusion theorem
**Targets:** A ambient hull geometry; B finite packing; C post-ZF cavity ledger
**Status:** report-level conditional theorem; no automatic promotion of post-ZF inputs
**Computation:** decimal evaluation only; the proof uses exact equations below

## LEVEL I STATUS

`STILL OPEN`

The new ambient-force geometry raises the explicit asymptotic pinned/contact
surplus floor to

$$
\boxed{\liminf\frac{e_{BB}+2s_C}{D}\ge
\lambda_{\rm int}=0.5932351999\ldots,}
\tag{IC.1}
$$

conditional on the post-ZF inputs stated in Section 1. There is also a positive
uniform gap above this particular constant, by the equality audit in Section 6.
This improves the latest report-level explicit GS bound `0.4647922503...`.
It is not a contradiction for all possible survivors.

The geometric part does not use Groemer, Blaschke--Lebesgue, or the PI literature
import. It uses the canonical A source-hull bound and the exact circular model
proved in the [ambient-force integrator report](integrator_ambient_force_geometry_2026-09-09.md).

## 1. Exact conditional input signature

Work on an unbounded sequence of triangle-free global sources in the C-II
lexicographic normalization. Let `F` be their full force hull. Use

- `h`: actual diameter-edge count; `q`: actual diameter-endpoint count;
- `b`: outer contact-face walk length;
- `Q>=0`: total bounded exceptional-face degree excess over four;
- `s_Z>=0`: mixed-row surplus;
- `e_BB>=0`: loaded-loaded unit contacts;
- `s_C>=0`: extra pinned-contact stress nullity;
- `L=e_BB+2s_C`;
- `G=area(F)-sum_r area(conv A_r)`: attachment-cell area gap;
- `E_out>=0`: sum of outer-pocket perimeters minus three per pocket;
- `P_F=per(F)`.

The needed additional inputs, and no stronger versions, are:

1. **ZE/ZT:** `b=2h-Q-2s_Z`, `q>=h`, and `P_F<=b`.
2. **DB:** `liminf h/D>=2rho`, where `rho=cos rho` in `(0,1)`.
3. **GU/ZK:** if `L/D->lambda<infinity`, then
   `limsup sum_r area(conv A_r)/D^2 <= pi lambda^2/4`.
4. **OP/PC and the JC derivation:**
   `E_out+Q <= P_F-h+e_BB-3(q-h)-2s_Z`.
5. **JC/ZG area charging:**
   `G <= (E_out+Q)^2/(4pi)+o(D^2)` uniformly when `L/D` is bounded.

These are the precise interface supplied by
[DB](target_c_post_zf_difference_body_perimeter_2026-09-09.md),
[GU](target_c_db_upgraded_component_gap_2026-09-09.md), and
[JC](target_c_post_pi_joint_cavity_budget_2026-09-09.md).
They are not all currently promoted. The conclusion here is a proved implication
from this signature; it does not independently certify the full ZR/ZF ancestry.

For input 4, JC.5 gives `E_out<=x_B+P_F-2q+e_BB`, while
`x_B=2h-q-Q-2s_Z`. Substitution gives exactly the displayed inequality.
For input 5, subtracting the fixed three-edge/four-edge baselines before
isoperimetry gives the two squared excess budgets; adding them is bounded by
the square of their sum. All discarded terms are `O(D)` for bounded `L/D`.

## 2. The new feasible-region inequality

Pass to a subsequence with finite limits

$$
\frac LD\to\lambda,\quad\frac{e_{BB}}D\to t,\quad
\frac hD\to y,\quad\frac{P_F}D\to p,\quad
\frac{\operatorname{area}(F)}{D^2}\to a.
\tag{IC.2}
$$

This suffices to rule out a finite lower accumulation point of `L/D`.
The bounds `0<=t<=lambda`, `h<=q<=P_F<=pi D`, and input 1 imply

$$
0\le t\le\lambda,\qquad
2\rho\le y\le p\le\min\{2y,\pi\}.
\tag{IC.3}
$$

The ambient-force report gives, writing

$$
f(y)=\frac{y+\sin y}{4},\qquad c=3\pi/4,
$$

$$
\boxed{a\ge\max\{f(y),p-c\}.}
\tag{IC.4}
$$

The first term uses all diameter directions in the centered cyclic model; the
second term is its area-perimeter inequality. Neither treats `F` as the whole
source hull.

Input 4, with nonnegative remainders dropped, gives
`E_out+Q<=P_F-h+e_BB`. Inputs 3 and 5 therefore give

$$
a\le\frac\pi4\lambda^2+
\frac{(t+p-y)^2}{4\pi}
\le\frac\pi4\lambda^2+
\frac{(\lambda+p-y)^2}{4\pi}.
\tag{IC.5}
$$

Thus every survivor must satisfy the explicit necessary condition

$$
\boxed{\max\{f(y),p-c\}\le
\frac\pi4\lambda^2+
\frac{(\lambda+p-y)^2}{4\pi},\qquad
2\rho\le y\le p\le\min\{2y,\pi\}.}
\tag{IC.6}
$$

This is stronger than independently inserting one area constant and `p<=pi`.

## 3. Exact constants

Let `y_*` be the unique root in `(0,pi)` of

$$
\boxed{7y_*-\sin y_*=3\pi.}
\tag{IC.7}
$$

Uniqueness follows because the derivative is `7-cos y>=6`. Equivalently,
`f(y_*)+c=2y_*`. Let `lambda_*` be the positive root of

$$
\boxed{f(y_*)=\frac\pi4\lambda_*^2+
\frac{(\lambda_*+y_*)^2}{4\pi}.}
\tag{IC.8}
$$

Equivalently,

$$
(\pi^2+1)\lambda_*^2+2y_*\lambda_*+
y_*^2-4\pi f(y_*)=0.
\tag{IC.9}
$$

The exact equations, not decimal approximations, define the constants:

$$
y_*=1.4887737130\ldots,\quad
f(y_*)=0.6213529360\ldots,\quad
\lambda_*=0.5932351999\ldots .
$$

Useful coarse bounds are `1.48<y_*<1.5` and `1/2<lambda_*<1`.
The former follow by evaluating IC.7 using
`sin x>=x-x^3/6`, `sin x<=1`, and `3.141<pi<22/7`.
For the latter, at `lambda=1/2` the right side of IC.8 is less than `0.515`,
while `f(y_*)=2y_*-3pi/4>0.602`; at `lambda=1` the right side exceeds `pi/4`,
whereas `f(y_*)<pi/4`. Monotonicity in positive `lambda` finishes the check.

Also `2rho<y_*`. One exact way to see this is to put
`p_min(y)=y+2cos(y/2)` and use

$$
4(f(y)+c-p_{\min}(y))
=3(\pi-y)+\sin(\pi-y)-8\sin((\pi-y)/2)>0
$$

for `y<pi`, by the strict derivative calculation in AP.4. At `y=2rho`,
`p_min(y)=2y`. Since `f(y)+c-2y` is strictly decreasing, its zero `y_*` lies
strictly above `2rho`.

## 4. Analytic optimization of IC.6

For a fixed `lambda`, define the available slack

$$
\Psi_\lambda(y,p)=\frac\pi4\lambda^2+
\frac{(\lambda+p-y)^2}{4\pi}-\max\{f(y),p-c\}.
$$

We show `Psi_(lambda_*)<=0` everywhere in IC.3, with equality only at
`y=y_*`, `p=2y_*`. Since `p-y>=0`, this expression increases strictly with
`lambda>=0` in the range relevant here. It will follow that IC.6 is impossible
for `lambda<lambda_*`.

### Optimize the actual perimeter first

Below `p_0(y)=f(y)+c`, the derivative in `p` is
`(lambda_*+p-y)/(2pi)>0`. Above `p_0`, it is that quantity minus one, which
is negative because `lambda_*<1`, `p<=pi`, and `y>=2rho>1.4`.
Also `y<=p_0(y)<=pi`. Hence, on `y<=p<=min(2y,pi)`, the maximum is at

$$
p=\min\{2y,p_0(y)\}.
\tag{IC.10}
$$

The switch is exactly at `y=y_*`.

### The range `2rho<=y<=y_*`

Here IC.10 is `p=2y`, and the maximum becomes

$$
\frac\pi4\lambda_*^2+
\frac{(\lambda_*+y)^2}{4\pi}-f(y).
\tag{IC.11}
$$

Its derivative is

$$
\frac{\lambda_*+y}{2\pi}-\frac{1+\cos y}{4}>0.
$$

For a fully explicit sign check, `rho>0.7` follows from
`cos(0.7)>=1-0.7^2/2>0.7`. Thus `y>1.4`, `lambda_*>1/2`, and
`cos y<=cos(1.4)<=1-1.4^2/2+1.4^4/24<0.181`. The first term is greater
than `1.9/(2pi)>0.302`, while the second is less than `0.296`.
Therefore IC.11 increases to zero at `y_*`, by IC.8.

### The range `y_*<=y<=pi`

Here IC.10 is `p=f(y)+c`. Put `r(y)=f(y)+c-y>=0`. The maximum is

$$
\frac\pi4\lambda_*^2+
\frac{(\lambda_*+r(y))^2}{4\pi}-f(y).
\tag{IC.12}
$$

Since `f'(y)>=0`, `r'(y)=f'(y)-1<0`, and `lambda_*+r(y)>0`, its derivative
is strictly negative. It decreases from zero at `y_*`.

This proves the claimed global maximum, and hence IC.1. The proof is analytic;
no sampled optimization is used to certify the minimum.

## 5. What the theorem eliminates

Conditional on Section 1, no unbounded survivor sequence can have

$$
\liminf\frac{e_{BB}+2s_C}{D}<0.5932351999\ldots .
$$

The increase over GS's explicit constant is about `0.12844D`, or 27.6 percent
of the old coefficient. This is a fixed linear improvement; all geometric
`o(D^2)` errors are safely lower-order for any fixed margin below the new root.

The result does not say that loaded-loaded contacts alone have this lower bound:
extra pinned-contact stress nullity can pay some or all of `L`.
It also does not control individual conductances or convert the bound into
the exact face contradiction `b+Q>2h`.

## 6. Equality audit: there is a uniform positive gap above this root

The root is exact for the relaxed inequalities IC.6, but it cannot be approached
by the actual ambient-force hulls.

Suppose a sequence had `L/D -> lambda_*`. The strict monotonicity in Section 4
forces, after taking subsequences,

$$
y\to y_*,\qquad p\to2y_*,\qquad
a\to f(y_*)=2y_*-3\pi/4.
\tag{IC.13}
$$

The ambient-force theorem makes the normalized force-hull limit the convex hull
of a closed antipodal subset of the radius-`1/2` circle. For any proper such
subset, one complementary open arc has positive length `g`. The proof of AP.4
is then strict on that gap. The same area/perimeter sums extend to a closed
subset by summing over its disjoint complementary arcs, or by polygonal
approximation. Thus

$$
\operatorname{area}(F_\infty)>
\operatorname{per}(F_\infty)-3\pi/4
$$

unless the subset is the whole circle. In the whole-circle case the perimeter
is `pi`, whereas IC.13 has perimeter `2y_*<pi`. Both alternatives contradict
IC.13. A degenerating segment also has a positive gap and strict inequality.

Therefore there is an absolute `epsilon>0` such that every sufficiently large
source satisfying Section 1 has

$$
\boxed{(e_{BB}+2s_C)/D\ge\lambda_*+\epsilon.}
\tag{IC.14}
$$

Indeed, failure would provide a sequence with increasing diameters and
`L/D<lambda_*+1/j`; IC.1 would force convergence to `lambda_*`, which was
just excluded. No numerical value for this further gap is claimed.

## 7. Regression and dependency audit

| Check | Result |
| --- | --- |
| Isolated source points | Retained in the global ambient-hull input; none is added to the contact-core rank count. |
| Distinct A and C hulls | Inclusion and the explicit midpoint error provide the bridge. No coordinate identification with a scaffold occurs. |
| General constant-width bodies | Insufficient alone; the new limiting hull is centrally symmetric and cyclic because it comes from global diameter endpoints. |
| Nearly equilateral rhombi | Allowed. No uniform local angle or area defect is assumed. |
| Linear diameter branching with `P_*/D -> 2` | Allowed: vanishing angular separation makes these facts compatible. |
| Individual weights | No lower bound is used. |
| Unpromoted ZF ancestry | Remains conditional. IC.1/IC.14 cannot promote it indirectly. |
| Numerical optimization | Not used in the proof; Section 4 verifies the entire relaxed feasible region. |

## 8. Promotion recommendation and remaining target

Hold as a conditional report. The unconditional geometric bridge is separately
auditable in the ambient-force report; Section 1 must pass the normal promotion
process before the numerical C-II theorem can be promoted unconditionally.

The remaining closing obligation is to show that the high-surplus regime
`e_BB+2s_C >= (lambda_*+epsilon)D` cannot coexist with the exact post-ZF ledgers
and the ambient cyclic force-hull model, or to build a strict sub-`D` competitor.
The new floor by itself is not incompatible with those ledgers.

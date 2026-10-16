<!-- theorem-state: {"artifact_id":"ART-AE053AB3C31C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — geometry-audited sparse full-core exclusion through `sigma=0.0105`

**Date:** 2026-09-12  
**Lifecycle:** proof-only candidate; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The audited sparse/directional signed-return split already excludes the full-core
Section-118 window `sigma<=0.0088`. A later scalar-only note verifies the same
correlated inequality at `sigma=0.0100`, conditional on extending the inherited
geometric hypotheses.

This note checks those geometric hypotheses directly and pushes the safe endpoint to

\[
\boxed{\sigma\le s_0:=0.0105.}
\tag{0.1}
\]

The extension is still proof-only because it inherits the proof-only sparse/directional
and signed-return stack. It does not touch the Type-I inactive-container branch.

Use

\[
\sigma(\theta)
=3\theta-2\pi-\sin(\theta/2)-2\sin\theta,
\quad
\lambda(\theta)=\sin(\theta/2),
\quad
U(\theta)=3\theta-2\pi.
\tag{0.2}
\]

Let `theta_8` be the canonical Section-101 zero-slack root and put

\[
\phi_8:=2\pi-2\theta_8.
\]

At `s_0=0.0105`, the unique solution of `sigma(theta_0)=s_0` is

\[
\boxed{
\begin{aligned}
\theta_0&=2.705140624515636\ldots,\\
U_0&=1.832236566367321\ldots,\\
\lambda_0&=0.976283049720324\ldots,\\
\phi_0&=2\pi-2\theta_0
=0.872904058148315\ldots .
\end{aligned}}
\tag{0.3}
\]

The exact correlated scalar residual at the endpoint is still

\[
0.00479749\ldots>0,
\]

and the conservative rounded proof below retains margin above `0.0044`.

---

## 1. The Section-118 gap geometry remains valid through `0.0105`

Use the exact Section-118 slack decomposition

\[
x+y+z+w=\sigma,
\qquad x,y,z,w\ge0.
\tag{1.1}
\]

Write the largest complement gap as

\[
g_1=\theta-\delta,
\]

and put

\[
\phi=2\pi-2\theta.
\]

The transfer function used in the hostile-audited Sections 113, 117, and 118 is

\[
h_\theta(t)
=f(\theta-t)+f(\phi+t)-f(\theta)-f(\phi),
\qquad f(u)=\sin(u/2).
\tag{1.2}
\]

The hostile Section-117 audit checks that on

\[
\theta\ge\theta_8,
\qquad 0\le t\le0.1,
\]

its `t` derivative is increasing in `theta` and decreasing in `t`, with global lower
bound

\[
\partial_t h_\theta(t)>0.30.
\tag{1.3}
\]

The same audit records that the coarse branch `delta>=0.1` costs more than `0.0326`.
Those two statements are not tied to the old `sigma=0.0029` endpoint. Since now

\[
w\le\sigma\le0.0105<0.0326,
\]

the coarse branch is still impossible. Integrating (1.3) therefore gives

\[
\boxed{\delta\le {10\over3}w.}
\tag{1.4}
\]

Write

\[
g_2=\phi+x_2,
\qquad
g_3=\phi+x_3,
\qquad
\tau=\sum_{j\ge4}g_j.
\]

The exact complement-measure identity in Section 118 is

\[
x_2+x_3+\tau=\delta+x.
\tag{1.5}
\]

Thus

\[
\boxed{
0\le x_2,x_3,\tau
\le x+{10\over3}w
\le {10\over3}\sigma
\le0.035.
}
\tag{1.6}
\]

At the endpoint the principal residual gap is still

\[
\phi_0=0.872904\ldots,
\]

so the perturbation in (1.6) is smaller by a factor above twenty-four. In particular
the Section-104 fourth-gap/adjacent-span argument remains in the same strict branch;
the two support spans adjacent to the largest principal gap are bounded by `delta`.

The oriented tangent lift is also unambiguous. The main support-region angular extent
is at most

\[
|S|+\tau
\le U(\theta)+{10\over3}\sigma
\le U_0+0.035
=1.8672365663\ldots<\pi.
\tag{1.7}
\]

Therefore the fixed-projective-window tangent counting used for the regular tooth
family remains valid.

For comparison, even the coarser Section-113 corridor-separation lower bound remains
strictly positive:

\[
{\theta_8\over2}-{\pi\over3}-{73\over6}s_0
=0.17650646\ldots>0.
\tag{1.8}
\]

Thus there is no hidden phase/corridor collision at the new endpoint.

---

## 2. The conservative carrier area floor remains valid

Let

\[
G(t)={t-\sin t\over8}.
\]

The exact Section-107 wrapping-support area identity is scale-independent. Equations
(1.4)--(1.6), monotonicity of `G`, and its superadditivity give the same sharp-Section-118
lower bound

\[
A_*(x,w)
\ge
A_0(s_0)
:={\pi\over4}
-G(\theta_0)
-2G\left(\phi_8+{10s_0\over3}\right)
-G\left({10s_0\over3}\right).
\tag{2.1}
\]

Direct evaluation gives

\[
\boxed{A_0(s_0)=0.469742134546628\ldots>0.4697.}
\tag{2.2}
\]

All gap arguments in (2.1) remain below `pi`; for example

\[
\phi_8+{10s_0\over3}
=0.9123692478\ldots<\pi.
\]

Hence local rhombic saturation transfers (2.2) to the same finite carrier area floor
used by the sparse/directional signed-return theorem.

---

## 3. The regular-tooth inverse remains in its monotone branch

Let

\[
F(q)=\sin q+\sqrt3(1-\cos q)-q
\]

and let `Q(y)` be the unique nonnegative solution of

\[
F(Q(y))={y\over2}.
\tag{3.1}
\]

At the endpoint,

\[
\boxed{Q(s_0)=0.0784749319620981\ldots<0.0785.}
\tag{3.2}
\]

This is far below `pi/3`. Thus the tangent/bathtub formula remains on the same unique
monotone inverse branch. Moreover, on `0<y<=s_0`,

\[
Q'(y)={1\over2F'(Q(y))}.
\tag{3.3}
\]

Since

\[
F'(q)=\cos q+\sqrt3\sin q-1\le\sqrt3 q,
\]

(3.2) gives the uniform bound

\[
\boxed{
Q'(y)>{1\over2\sqrt3(0.0785)}>3.677.
}
\tag{3.4}

---

## 4. Exact correlated product maximum on the enlarged simplex

The audited sparse split gives the necessary condition

\[
\lambda z\ge(2-\sqrt3)[J]_+,
\tag{4.1}
\]

where the directional product in `J` is

\[
2\bigl(U-x-y+2z\bigr)
\left(Q(y)+y+x+{10w\over3}\right).
\tag{4.2}
\]

To dominate every `sigma<=s_0` survivor, relax to

\[
x+y+z+w\le s_0,
\]

increase `U` to `U_0`, and fill unused slack with `w`. Put

\[
C:=U_0-x-y+2z,
\]

\[
B:=Q(y)+{10s_0\over3}
-{7x\over3}-{7y\over3}-{10z\over3}.
\tag{4.3}
\]

The actual product in (4.2) is at most `2CB`.

Throughout the simplex,

\[
B<0.0785+0.035=0.1135,
\]

while

\[
C\ge U_0-s_0>1.8217.
\]

Therefore

\[
{\partial(CB)\over\partial x}
=-B-{7C\over3}<0,
\]

and

\[
{\partial(CB)\over\partial z}
=2B-{10C\over3}<0.
\tag{4.4}
\]

Any maximizer has `x=z=0`. On that edge,

\[
P(y)
=(U_0-y)
\left(Q(y)+{10s_0\over3}-{7y\over3}\right).
\tag{4.5}
\]

Using (3.4), the derivative of the second factor exceeds

\[
3.677-{7\over3}>1.343.
\]

Its value is below `0.1135`, while `U_0-y>1.8217`; hence

\[
P'(y)>-0.1135+1.8217(1.343)>0.
\tag{4.6}
\]

Thus the product maximum occurs at `y=s_0`, and

\[
\boxed{
CB
\le P(s_0)
=(U_0-s_0)(Q(s_0)+s_0)
=0.1620888870\ldots<0.1622.
}
\tag{4.7}

This is an analytic simplex maximum, not a sampled optimization.

---

## 5. Strict endpoint contradiction

As in the audited `sigma=0.0088` proof, subtract

\[
{\lambda z\over2-\sqrt3}
\]

from the return bracket. The sparse penalty becomes

\[
\lambda\left(
10z+{x\over2}+{25w\over3}+{z\over2-\sqrt3}
\right).
\tag{5.1}
\]

The largest coefficient in the parenthesis is

\[
10+{1\over2-\sqrt3}
=13.7320508\ldots<13.733.
\tag{5.2}
\]

Use the conservative bounds

\[
\lambda<0.977,
\qquad
A_*(x,w)>0.4697,
\qquad
CB<0.1622,
\qquad
x+y+z+w\le0.0105.
\]

Then uniformly on the whole enlarged simplex,

\[
\begin{aligned}
J-{\lambda z\over2-\sqrt3}
&>0.4697
-0.977(13.733)(0.0105)
-2(0.1622)\\
&=0.0044200\ldots>0.
\end{aligned}
\tag{5.3}

Hence

\[
J>{\lambda z\over2-\sqrt3}\ge0.
\]

The necessary condition (4.1) would therefore imply

\[
\lambda z
\ge(2-\sqrt3)J
>\lambda z,
\]

a contradiction.

### Theorem — proof-only full-core exclusion through `sigma=0.0105`

Under the hostile-audited Section-117 signed-return theorem and the audited
sparse/directional decomposition, no full-core Type-II survivor exists in the entire
window

\[
\boxed{0\le\sigma\le0.0105.}
\tag{5.4}
\]

The proof checks the inherited gap, fourth-gap, tangent-lift, tooth-inverse, area, and
correlated-product hypotheses at the enlarged endpoint rather than assuming them.

---

## 6. Scalar envelope and exact surviving full-core obstruction

If one ignores outward rounding and solves the same correlated endpoint residual
exactly, its first zero occurs near

\[
\boxed{
\sigma_{sparse,env}
=0.01065455286\ldots,
}
\tag{6.1}
\]

with

\[
\theta=2.70517347816\ldots,
\qquad
\lambda=0.97628660596\ldots .
\]

This number is **not** claimed as a theorem endpoint here. The safe geometry-audited
endpoint is `0.0105`.

The remaining proof-only full-core problem has therefore moved to

\[
\boxed{\sigma>0.0105,}
\]

which equivalently means the selected wrapping carrier lies beyond the corresponding
angular/diameter scale

\[
\lambda>0.9762830497\ldots .
\]

Further optimization of the same scalar inequality can gain at most about
`1.55e-4` in `sigma`; a substantive continuation should instead exploit the geometry
of a carrier this close to the global diameter or improve the signed-return transport
mechanism.

The Type-I inactive-container branch remains independent and open.

---

## 7. Scope

- No source point is deleted.
- No contact-isolated source coordinate enters a core affine-kernel theorem.
- The proof uses physical endpoint occurrences and inherits the audited signed-return
  injectivity convention.
- The extension is proof-only; theorem-state authority is unchanged.
- The finite-diagonal atomic-gap theorem is not needed for this `0.0105` exclusion.
- C-II and Level I remain open.

**Disposition:** proof-only strengthened full-core exclusion.
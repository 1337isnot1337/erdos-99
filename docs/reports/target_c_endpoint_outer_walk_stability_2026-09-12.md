<!-- theorem-state: {"artifact_id":"ART-8B58666B37D5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II endpoint outer-walk stability — corrected audit

**Date:** 2026-09-12  
**Audit status:** **PARTIALLY INVALID AS ORIGINALLY PROVED; CORRIDOR CONCLUSION REPAIRED.**  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

## 1. Audit verdict

The original version of this report contained a false perimeter-squeeze step.  It
claimed that a wrapping Type-II harmonic cell at the canonical Section-96 endpoint

\[
\mu_4=0.936215741409583\ldots
\]

must satisfy

\[
\operatorname{per}(P_D)/D\to4\alpha_4,
\qquad
L_D-\operatorname{per}(P_D)=o(D),
\]

where

\[
\theta_4=2\arcsin\mu_4,
\qquad
\alpha_4=3\theta_4-2\pi={3\over2}\sin\theta_4.
\]

Those two assertions do **not** follow from the cited perimeter bounds.  However, the
main geometric conclusion about the three distinguished Section-96 routes is still
true, for a different reason: the exact outer-walk route budget itself is saturated at
the endpoint.

This file records the corrected proof and explicitly withdraws the unsupported global
perimeter claims.

## 2. The failed argument

Canonical Section 94 gives only

\[
\liminf {\operatorname{per}(P_D)\over D}
\ge \alpha_4+3\sin\theta_4
={9\over2}\sin\theta_4,
\tag{2.1}
\]

while the Section-82 attachment-perimeter capacity gives

\[
\limsup {\operatorname{per}(P_D)\over D}
\le4\alpha_4
=6\sin\theta_4.
\tag{2.2}
\]

The gap between (2.1) and (2.2) is

\[
{3\over2}\sin\theta_4=\alpha_4>0.
\]

Therefore these bounds do not squeeze `per(P_D)/D` to `4 alpha_4`, and they do not
imply

\[
L_D-\operatorname{per}(P_D)=o(D).
\]

Any downstream argument that needs the **entire** outer walk to be an asymptotically
shortest polygonal realization of `partial P_D` is unsupported.

## 3. What canonical Section 96 really gives at equality

Let `a_D` be the number of loaded attachments, `L_D` the outer-face walk length,
`Q_D` the bounded-face degree excess, `s_D` the pinned surplus, `c_D` the number of
loaded-loaded contacts in the cell, and `c_D^partial<=c_D` the number of those contacts
that are sides of the attachment polygon.

At a wrapping endpoint sequence with

\[
\operatorname{diam}(P_D)/D\to\mu_4,
\]

canonical Section 96 proves

\[
{a_D\over D}\to\alpha_4,
\qquad
Q_D/D\to0,
\qquad
s_D/D\to0,
\qquad
c_D/D\to0.
\tag{3.1}
\]

The exact Section-82 identity is

\[
L_D+Q_D=4a_D-6-2s_D-2c_D.
\tag{3.2}
\]

Hence, using `alpha_4=(3/2)sin(theta_4)`,

\[
\boxed{
L_D=6\sin\theta_4\,D+o(D).
}
\tag{3.3}

Section 96 also supplies three pairwise distinct special attachment intervals.  Let
`W_{1,D},W_{2,D},W_{3,D}` be their outer-face contact routes, with path lengths
`ell_{j,D}` and endpoint chord lengths `d_{j,D}`.  The three forbidden angular gaps
and Type-II annular convergence give

\[
\boxed{
d_{j,D}\ge \sin\theta_4\,D-o(D)
\qquad(j=1,2,3).
}
\tag{3.4}

Every remaining consecutive attachment interval has route length one only when it is
a direct loaded-loaded polygon-side contact; otherwise its route length is at least
two.  Therefore

\[
L_D
\ge
\sum_{j=1}^3\ell_{j,D}
+2(a_D-3)-c_D^\partial.
\tag{3.5}
\]

Using (3.1), (3.3), and `c_D^partial=o(D)` in (3.5),

\[
\sum_{j=1}^3\ell_{j,D}
\le
6\sin\theta_4 D
-2\alpha_4D
+o(D)
=
3\sin\theta_4D+o(D).
\tag{3.6}

On the other hand, path length dominates chord length, so (3.4) gives

\[
\sum_{j=1}^3\ell_{j,D}
\ge
\sum_{j=1}^3d_{j,D}
\ge
3\sin\theta_4D-o(D).
\tag{3.7}

Equations (3.6)--(3.7), together with the individual lower bounds (3.4), force for
each `j=1,2,3`

\[
\boxed{
\ell_{j,D}=\sin\theta_4D+o(D),
\qquad
d_{j,D}=\sin\theta_4D+o(D),
\qquad
\ell_{j,D}-d_{j,D}=o(D).
}
\tag{3.8}

Thus the original report's **three-corridor near-geodesic conclusion is valid**, but
its published proof was wrong.  The valid proof is the route-budget saturation above,
not a squeeze of `per(P_D)`.

Numerically,

\[
\sin\theta_4=0.658020712164235\ldots,
\]

so each special route has macroscopic length about `0.658020712 D`.

## 4. Finite metric stability lemma

The final path-stability lemma from the original report is valid independently.

Let a polygonal path from `u` to `v` have unit edge vectors
`z_1,...,z_m`, total length `ell=m`, chord length `d=|u-v|>0`, and excess

\[
e:=\ell-d.
\]

Let `q=(v-u)/d`, and let `psi_k in [-pi,pi]` be the signed angle from `q` to `z_k`.
Projection onto `q` gives

\[
\sum_{k=1}^m\cos\psi_k=d,
\]

hence

\[
\boxed{
\sum_{k=1}^m(1-\cos\psi_k)=e.
}
\tag{4.1}
\]

Since

\[
1-\cos x\ge {2x^2\over\pi^2}
\qquad(|x|\le\pi),
\]

we obtain

\[
\boxed{
\sum_{k=1}^m\psi_k^2\le {\pi^2\over2}e.
}
\tag{4.2}
\]

Every path point lies in the ellipse with foci `u,v` and major-axis length `ell`.
Consequently its perpendicular distance from the chord line is at most

\[
\boxed{
{1\over2}\sqrt{\ell^2-d^2}
=
\sqrt{{de\over2}+{e^2\over4}},
}
\tag{4.3}
\]

and its longitudinal overshoot beyond the chord segment is at most `e/2`.

Applying (4.1)--(4.3) to (3.8) gives, for each of the three special Section-96 routes,

\[
\boxed{
\operatorname{dist}_{H}(W_{j,D},[u_{j,D},v_{j,D}])=o(D),
\qquad
\sum_{e\in W_{j,D}}\psi_e^2=o(D).
}
\tag{4.4}

In particular, for every fixed `eta>0`, only `o(D)` edges of a special route make
angle at least `eta` with its chord direction.

## 5. Correct frontier

The repaired conclusion is strong but narrower than the original report claimed:
three specific macroscopic boundary routes collapse to three thin almost-straight
contact corridors.  The **whole** outer walk need not be close to `partial P_D` in
length.

The remaining Type-II endpoint problem is therefore to couple these three valid thin
corridors to the locally rhombus-saturated interior and the canonical ordered train
grid.  A useful next theorem would show that one corridor forces either

- linear phase/interface defect incompatible with the global angular-defect budget;
- an exact unit equilateral contact triangle; or
- a source-preserving deformation that strictly lowers the actual global diameter.

No such implication is proved here.

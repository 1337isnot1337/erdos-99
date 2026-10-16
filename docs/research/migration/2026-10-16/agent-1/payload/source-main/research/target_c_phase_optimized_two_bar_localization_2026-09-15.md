# Target C-II — phase-only adjacent selection localizes every minimal two-bar strip blocker to bounded endpoint clusters

**Date:** 2026-09-15  
**Status:** proof-only source-level structural strengthening  
**Scope:** full-core Type-II branch with `t=(q-k)/D<=1.844`  
**Dependencies:** audited `0.7404D` smallest-leaf weighted center fan; triple-small real-phase argument; adjacent-strip opening reduction; one/two-bar tangent certificate; two-bar geometry/localization theorem  
**Certificate:** `research/verify_target_c_phase_opening_cone_18782.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

Once the adjacent-strip translation obstruction has been reduced to one or two load-bearing tangent bars, minimizing the **total switching-edge count** is no longer the right adjacent-pair objective. For the two-bar branch, the useful quantity is the physical opening-cone width, because that width directly controls the projective angle and endpoint separation of the two load-bearing diameter chords.

Re-optimize the common-center path only for this phase width. A simple rational choice gives an adjacent physical strip whose contact-opening cone has angular width

\[
\boxed{
\varepsilon<{18782\over D}+o(D^{-1}).
}
\tag{PO.1}
\]

For any **minimal two-bar** tangent certificate on that strip, the two actual diameter edges therefore have projective angle

\[
\boxed{
\eta<{18782\over D}+o(D^{-1})
}
\tag{PO.2}
\]

and, after orienting the two unordered diameter segments to realize that projective angle, their corresponding endpoint pairs satisfy

\[
\boxed{
|x_2-x_1|<18782+o(1),
\qquad
|y_2-y_1|<18782+o(1).
}
\tag{PO.3}
\]

Thus the TB2 obstruction is no longer merely finite-dimensional. It is spatially localized at `O(1)` scale inside a source whose diameter tends to infinity.

The one-bar branch remains separate and is not claimed to satisfy this two-chord clustering conclusion.

---

## 1. Re-optimize only the phase-opening objective

Use the audited fan inputs

\[
{\sum_\tau w_\tau d_\tau\over\sum_\tau w_\tau}
>0.7404-o(1),
\tag{PO.4}
\]

\[
{1\over D}\sum_\tau w_\tau>0.0848-o(1),
\tag{PO.5}
\]

and

\[
N_C<1.063D+o(D).
\tag{PO.6}
\]

Fix the rational good-leaf threshold and upper-center quantile

\[
\boxed{
\lambda={6794\over10000}=0.6794,
\qquad
r={4803\over10000}=0.4803.
}
\tag{PO.7}
\]

The usual weighted thresholding gives distinct good-leaf density

\[
\begin{aligned}
g
&={ (0.7404-\lambda)(0.0848)\over1.063-\lambda}\\
&={3233\over239750}\\
&=0.01348488008\ldots .
\end{aligned}
\tag{PO.8}
\]

Every good leaf has at least

\[
\begin{aligned}
d_{top}
&=\lambda-(1-r)(1.063)\\
&={1269589\over10000000}\\
&=0.1269589
\end{aligned}
\tag{PO.9}
\]

neighbors in the top center block, and at least

\[
\begin{aligned}
d_{low}
&=\lambda-r(1.063)\\
&={1688411\over10000000}\\
&=0.1688411
\end{aligned}
\tag{PO.10}
\]

neighbors below the selected top-block center phase.

Double counting exactly as in the triple-small theorem gives one center train `gamma` crossing a simple complement-dual path

\[
P=(\tau_1,\ldots,\tau_m)
\]

with

\[
\boxed{
m>pD-o(D),}
\tag{PO.11}
\]

where

\[
\begin{aligned}
p
&={d_{top}g\over r(1.063)}\\
&={4104581237\over1224064962750}\\
&=0.003353238073\ldots .
\end{aligned}
\tag{PO.12}
\]

No switch-count budget is spent in this selection.

---

## 2. The total real-phase offset on the path is bounded

Use the same real phase representatives as in the audited triple-small proof. Let

\[
\alpha_\gamma
\]

be the chosen center phase and

\[
\beta_j
\]

be the real phase of leaf train `tau_j`, coherently oriented with the Section-157 rooted shore vector `u_j`. Put

\[
q_j:=\beta_j-\alpha_\gamma-{\pi\over3}>0.
\tag{PO.13}
\]

Each path leaf has at least `d_low D-o(D)` center neighbors with phase at most `alpha_gamma`. Every corresponding strict-rhombus angular excess is at least `q_j`. The global strict-rhombus angular-defect budget therefore gives

\[
\boxed{
\sum_{j=1}^m q_j
\le {C_{phase}\over d_{low}}+o(1),
}
\tag{PO.14}
\]

where

\[
C_{phase}={\pi^2\sqrt3(2+\sqrt3)\over12}.
\]

For adjacent path leaves,

\[
|\beta_{j+1}-\beta_j|
=|q_{j+1}-q_j|
\le q_j+q_{j+1}.
\tag{PO.15}
\]

Summing over internal boundaries gives

\[
\sum_{j=1}^{m-1}(q_j+q_{j+1})
\le2\sum_{j=1}^{m}q_j.
\tag{PO.16}
\]

Hence some adjacent pair obeys

\[
q_j+q_{j+1}
\le {2C_{phase}\over d_{low}pD}+o(D^{-1}).
\tag{PO.17}
\]

The exact certificate uses the standard outward enclosure

\[
C_{phase}
<{3258689123681\over612912000000}
\]

and proves

\[
\boxed{
{2C_{phase}\over d_{low}p}<18782.
}
\tag{PO.18}
\]

Therefore the selected adjacent pair has

\[
\boxed{
|\beta_{j+1}-\beta_j|
<{18782\over D}+o(D^{-1}).
}
\tag{PO.19}
\]

---

## 3. The physical strip opening cone is the narrow sign branch

This is the sign point that must be stated explicitly.

The real phases `beta_j` in Section 2 are not arbitrary projective representatives. They are the **same coherently oriented rooted-shore contact vectors** used in the Section-157 resultants:

\[
u_j=(\cos\beta_j,\sin\beta_j).
\tag{PO.20}
\]

For the physical layer between consecutive nested shores, the adjacent-strip opening theorem orients both boundary contact vectors from the fixed exterior into the middle layer. With the rooted shore convention this gives

\[
\boxed{
a=u_j,
\qquad
b=-u_{j+1}.
}
\tag{PO.21}
\]

For sufficiently large `D`, (PO.19) is smaller than `pi`, so

\[
\angle(a,b)
=\pi-|\beta_{j+1}-\beta_j|.
\tag{PO.22}
\]

The unit tangent directions satisfying

\[
a\cdot w\ge0,
\qquad
b\cdot w\ge0
\]

therefore form a closed arc of width

\[
\varepsilon
=\pi-\angle(a,b)
=|\beta_{j+1}-\beta_j|.
\tag{PO.23}
\]

Combining (PO.19) and (PO.23) proves (PO.1).

Thus the current adjacent real-phase theorem does resolve the physical sign ambiguity: the strip uses the narrow near-antipodal opening cone.

---

## 4. A minimal two-bar certificate is projectively `O(D^-1)`

Apply the one/two-bar tangent theorem to this selected physical strip. If the tangent obstruction has a one-bar certificate, retain that as the separate TB1 branch.

Otherwise choose a minimal two-bar certificate with inward diameter vectors `n_1,n_2`. The two-bar geometry theorem gives

\[
 d_{\mathbb{RP}^1}(n_1,n_2)
\le\varepsilon.
\tag{PO.24}
\]

Use (PO.1):

\[
\boxed{
 d_{\mathbb{RP}^1}(n_1,n_2)
<{18782\over D}+o(D^{-1}).
}
\]

This is (PO.2).

---

## 5. Quantitative diameter uniqueness gives bounded endpoint clusters

Write the two unordered diameter segments, after the orientation choice realizing their projective angle `eta`, as

\[
y_k-x_k=D u_k,
\qquad k=1,2,
\qquad
\angle(u_1,u_2)=\eta.
\]

The quantitative parallel-diameter lemma gives

\[
|x_2-x_1|,\ |y_2-y_1|
\le2D\sin(\eta/2)
\le D\eta.
\tag{PO.25}
\]

By (PO.2),

\[
D\eta<18782+o(1).
\]

This proves (PO.3).

The conclusion is source-level Euclidean localization: along an unbounded survivor sequence, the two load-bearing TB2 diameter bars have one pair of corresponding endpoints in a uniformly bounded region and their other corresponding endpoints in another uniformly bounded region a distance approximately `D` away.

---

## 6. Updated local normal form

For the phase-optimized adjacent strip, exactly one of the following holds.

### PO1 — one-bar tangent obstruction

One switching diameter bar alone blocks every tangent direction in the narrow contact-opening cone. Its inward diameter vector lies in the dual cone generated by `a,b`.

### PO2 — two-bar tangent obstruction

Two actual switching diameter bars are sufficient and minimal. Then

```text
opening-cone width < 18782/D + o(1/D)
+ two blocker chords have projective gap < 18782/D + o(1/D)
+ after aligned orientation, one endpoint pair is <18782+o(1) apart
+ the other endpoint pair is <18782+o(1) apart
+ the two bars still lie in the audited ordered one-arc switching interface.
```

This replaces a diffuse finite blocker classification by a bounded two-cluster diameter pattern.

The natural next theorem is now local: combine the `O(1)` endpoint clusters with unit separation, positive-core contact paths, and the one-arc prefix/hub/suffix order to force either a forbidden local diameter configuration, an exact unit equilateral triangle, or a finite endpoint exchange.

---

## 7. Scope audit

- The adjacent pair here is chosen for phase width, not for minimal total switching-edge count. No bound such as `542` is asserted for its full switching graph.
- The one/two-bar theorem applies regardless of the full switching count, so no count estimate is needed for PO1/PO2.
- The use of the narrow physical sign branch is justified by the real-phase/rooted-shore identity (PO.20)--(PO.23), not by projective closeness alone.
- The endpoint-cluster conclusion applies only to a **minimal two-bar** certificate. It does not apply to the one-bar branch.
- The constant `18782` is deliberately safe; the continuous optimum of this two-parameter phase-only architecture is about `18780.79`.
- Bounded endpoint clusters do not yet imply a bounded number of source vertices in those regions; unit separation gives only an area-dependent bound after an appropriate enclosing region is proved.
- No C-II closure is claimed.

**Disposition:** proved proof-only phase-optimized bounded-cluster normal form for the TB2 adjacent-strip obstruction. C-II and Level I remain open.

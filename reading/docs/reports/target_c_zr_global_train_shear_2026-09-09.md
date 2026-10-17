> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_global_train_shear_2026-09-09.md) · source SHA-256 `24d86752d6ed1d889f3041c45effb774defa0f475b1c7473b4f308e2a6ff4eff`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-20EFC75416C2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZGS: an outer-to-outer global train is an exact contact shear with negative weighted diameter curvature

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-weak-transverse-train`  
**Base:** stacked on PR #111 / ZK from PR #108  
**Run type:** exact finite train shear and diameter-cut identity  
**Target:** outer-to-outer stopped trains in the post-ZF source  
**Depends on:** DT, relative-interior KKT equilibrium, ZK strict terminal-cut response  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

A stopped train whose two endpoints lie on the **actual outer face of the full contact graph** has a stronger property than an outer-to-outer train of one rhombic component. Its midpoint pseudoline can be closed through the outer face to a Jordan curve that crosses the contact graph exactly in the parallel contact edges of that train.

Hence those train edges are a genuine global contact cut. Rotating the common cut-edge vector is realized by translating one complete shore of the source. Every actual contact length remains exactly one.

For this finite shear, let

$$
A_\tau=\sum_{e\in\tau}\alpha_e
$$

be total contact stress on the train cut and

$$
w_\tau=\sum_{h\pitchfork\tau}\beta_h
$$

be the total diameter KKT weight crossing the same shore split. Then

$$
\boxed{A_\tau>w_\tau}
$$

by ZK strict terminal-cut response and a cutset Dirichlet test. More strongly, the exact `beta`-weighted crossing-diameter squared-length sum along the shear is

$$
\boxed{
\sum_{h\pitchfork\tau}\beta_h|r_h(\theta)|^2
=
w_\tau D^2
-2(A_\tau-w_\tau)(1-\cos\theta).
}
$$

Thus every nonzero shear strictly decreases the weighted diameter square sum. Local diameter minimality can survive only through a nonsmooth maximum cusp: the active crossing diameter edges must have first shear derivatives of both signs. The all-parallel/one-sided derivative case is impossible.

---

## 1. A global outer train is a contact cut

Let `tau` be a nontrivial stopped train in the full contact graph, and assume both endpoint contact edges are incident to the global outer face.

DT gives a simple midpoint curve `gamma_tau` through the interiors of its rhombi. It meets the contact graph exactly at the midpoints of the train contact edges:

- inside each rhombus, the train segment joins midpoints of opposite train edges and misses the other two sides;
- consecutive segments meet at the midpoint of their shared train edge;
- DT excludes train self-intersection.

Join the two endpoint midpoints by a simple arc contained in the outer face, chosen far enough outside the embedded graph to avoid every contact edge except at its endpoints. The union is a Jordan curve `Gamma_tau`.

No source vertex lies on `Gamma_tau`. Let

$$
S_\tau,T_\tau
$$

be the two vertex shores.

Any contact edge joining the shores must cross `Gamma_tau`. By construction the only contact-graph intersections with `Gamma_tau` are train-edge midpoints. Therefore

$$
\boxed{
\delta_C(S_\tau)=E(\tau).
}
\tag{ZGS1}

The train contact edges are all parallel. Orient the train midpoint curve consistently with the DT positive normal direction. Its tangent always has positive projection on one fixed normal `Ju_tau`, so the fixed vector `u_tau` points consistently from one Jordan shore to the other. After swapping shore labels if necessary, every cut contact edge oriented from `T_tau` to `S_tau` has vector

\[
\boxed{p_s-p_t=u_\tau.}
\tag{ZGS2}

---

## 2. Exact finite contact shear

For real `theta`, put

\[
\Delta_\theta:=R_\theta u_\tau-u_\tau.
\tag{2.1}
$$

Define

$$
p_v(\theta)=
\begin{cases}
 p_v+\Delta_\theta,&v\in S_\tau,\\
 p_v,&v\in T_\tau.
\end{cases}
\tag{2.2}
$$

Every contact internal to a shore is unchanged by translation. For a cut contact `ts`, ZGS2 gives

$$
p_s(\theta)-p_t(\theta)
=u_\tau+\Delta_\theta
=R_\theta u_\tau,
$$

which still has length one.

Thus:

### Theorem ZGS.1 — global exact train shear

For every sufficiently small `theta`, the deformation (2.2) preserves **every actual contact length exactly**.

Since the source is finite and every noncontact pair has strict lower-distance slack, sufficiently small `theta` also preserves unit separation for all noncontact pairs.

Only cross-shore distances can change.

---

## 3. Both shores contain actual diameter terminals

Let

$$
A_\tau:=\sum_{e\in E(\tau)}\alpha_e>0.
\tag{3.1}

Sum the relative-interior KKT equilibrium equations over all vertices in `S_tau`. Internal contact and diameter forces cancel. Using ZGS2, the contact resultant across the cut is

\[
A_\tau u_\tau.
$$

Hence

$$
\boxed{
A_\tau u_\tau
=
\sum_{\substack{h=st\in H\\s\in S_\tau,t\in T_\tau}}
\beta_h(p_s-p_t).
}
\tag{ZGS3}

The right side is nonzero. Therefore at least one actual diameter pair crosses the cut, and both shores contain loaded diameter terminals.

So the terminal partition

\[
B_S=B\cap S_\tau,
\qquad
B_T=B\cap T_\tau
$$

is nonempty and proper.

Put

$$
w_\tau
:=
\sum_{h\pitchfork\tau}\beta_h.
\tag{3.2}
$$

Taking norms in ZGS3 gives the familiar coarse bound

$$
A_\tau\le Dw_\tau.
\tag{3.3}
$$

---

## 4. ZK makes the train cut strictly response-dominated

Let

$$
C_\tau
:=
\sum_{b\in B_S,k\in B_T}c_{bk}
\tag{4.1}
$$

be the total contact-network response conductance across the induced terminal cut.

ZK all-cut strictness gives

$$
\boxed{C_\tau>w_\tau.}
\tag{4.2}
$$

For the upper bound, prescribe terminal voltage one on `B_S` and zero on `B_T`. The harmonic extension has energy `C_tau`.

As a competitor, put voltage one on every contact vertex of `S_tau` and zero on every vertex of `T_tau`. Every internal contact has zero voltage drop, while each train cut contact has drop one. Its energy is exactly `A_tau`.

Dirichlet minimality gives

$$
C_\tau\le A_\tau.
\tag{4.3}
$$

Therefore:

### Theorem ZGS.2 — strict train-cut sandwich

$$
\boxed{
 w_\tau<C_\tau\le A_\tau\le Dw_\tau.
}
\tag{ZGS4}

In particular

\[
\boxed{A_\tau-w_\tau>0.}
\tag{4.4}

---

## 5. Exact weighted diameter identity under the shear

For a crossing diameter edge `h=st`, orient it from `T_tau` to `S_tau` and write

\[
r_h:=p_s-p_t,
\qquad |r_h|=D.
$$

Under ZGS1,

$$
r_h(\theta)=r_h+\Delta_\theta.
$$

Therefore

$$
|r_h(\theta)|^2
=D^2+2r_h\cdot\Delta_\theta+|\Delta_\theta|^2.
\tag{5.1}
$$

Sum with `beta_h`. ZGS3 gives

$$
\sum_{h\pitchfork\tau}\beta_hr_h
=A_\tau u_\tau.
\tag{5.2}
$$

Also

$$
\Delta_\theta\cdot u_\tau=\cos\theta-1
$$

and

$$
|\Delta_\theta|^2=2(1-\cos\theta).
$$

Thus

$$
\begin{aligned}
\sum_{h\pitchfork\tau}\beta_h|r_h(\theta)|^2
&=w_\tau D^2
 +2A_\tau(\cos\theta-1)
 +2w_\tau(1-\cos\theta)\\
&=w_\tau D^2
 -2(A_\tau-w_\tau)(1-\cos\theta).
\end{aligned}
$$

Hence:

### Theorem ZGS.3 — exact negative weighted curvature

$$
\boxed{
\sum_{h\pitchfork\tau}\beta_h
\bigl(D^2-|r_h(\theta)|^2\bigr)
=
2(A_\tau-w_\tau)(1-\cos\theta)>0
}
\tag{ZGS5}

for every sufficiently small nonzero `theta`.

Differentiating at zero,

\[
\boxed{
\sum_h\beta_h\frac d{d\theta}|r_h(\theta)|^2\Big|_0=0,
}
\tag{ZGS6}

and

\[
\boxed{
\sum_h\beta_h\frac {d^2}{d\theta^2}|r_h(\theta)|^2\Big|_0
=2(w_\tau-A_\tau)<0.
}
\tag{ZGS7}

---

## 6. Exact cusp necessity

For one crossing diameter vector, write

\[
r_h=D(\cos\phi_h\,u_\tau+\sin\phi_h\,Ju_\tau).
$$

Its first squared-length derivative is

$$
\frac d{d\theta}|r_h(\theta)|^2\Big|_0
=2D\sin\phi_h.
\tag{6.1}
$$

Suppose all crossing diameter derivatives were nonpositive for one shear sign. Then the positive weighted sum in ZGS6 would force every derivative to vanish. Thus every crossing diameter vector would be parallel to `u_tau`.

With the shore orientation fixed by ZGS2 and the resultant ZGS3 positive in direction `u_tau`, all positive-weight crossing diameters must then have vector

$$
r_h=Du_\tau.
$$

For such an edge, (5.1) gives

$$
|r_h(\theta)|^2-D^2
=2(D-1)(\cos\theta-1)<0
$$

for every small nonzero `theta`.

All crossing active diameter pairs would become strict while all contacts remain exactly unit and same-shore diameter pairs remain exactly `D`. Inactive pairwise upper-distance constraints have strict slack and remain below `D` for small `theta`.

This would produce a global minimizer with a strict subset of the original diameter pairs, contradicting the secondary diameter-pair normalization.

Therefore:

### Corollary ZGS.4 — two-sided diameter bracing

Every global outer-to-outer train cut in the lexicographically normalized post-ZF source has crossing actual diameter edges with **both signs** of first shear derivative:

$$
\boxed{
\exists h_+,h_-\pitchfork\tau:
\quad
r_{h_+}\cdot Ju_\tau>0,
\qquad
r_{h_-}\cdot Ju_\tau<0.
}
\tag{ZGS8}

The train shear is therefore blocked by a genuine max-function cusp, not by one-sided first-order geometry.

This is the exact two-edge regression that any multi-shear closing theorem must overcome.

---

## 7. Multi-train split matrix

For a family of global outer-to-outer trains `tau_1,...,tau_m`, each train cut defines a circular shore split of the outer boundary terminals.

The exact contact shears can be superposed at first order. Let `theta_j` be the angular coordinate for train `tau_j`. For an active diameter pair `h=bk`, its first squared-length derivative has the form

\[
\boxed{
D_h'(0)[\theta]
=
2\sum_{j:\,h\pitchfork\tau_j}
\epsilon_{hj}
(r_h\cdot Ju_j)\theta_j,
}
\tag{ZGS9}

where the sign `epsilon_hj` records which endpoint lies on the translated shore.

Let `A` be this `h times m` derivative matrix. Restricting KKT stationarity to the exact contact-shear tangent space gives

\[
\boxed{
A^T\beta=0,
\qquad\beta_h>0.
}
\tag{ZGS10}

Mixed infinitesimal rigidity implies that `A` has trivial kernel on non-Euclidean shear coordinates: a nonzero `theta` with `A theta=0` would be a nontrivial mixed infinitesimal flex.

Thus the outer-train branch produces an injective circular-split derivative matrix with a strictly positive left-kernel vector.

This is the precise object to compare against the report-level Theorem Z all-gap split machinery.

---

## 8. Binding regression

One shear coordinate can be locally pinned by two active diameter functions of the schematic form

\[
f_+(\theta)=a\theta-c\theta^2+O(\theta^3),
\qquad
f_-(\theta)=-b\theta-c'\theta^2+O(\theta^3),
$$

with `a,b>0`. Their maximum has a cusp minimum at zero even though a positive weighted average has negative second derivative.

Therefore ZGS5 alone does not prove a feasible diameter-decreasing shear.

The next theorem must exploit **several circular train splits simultaneously**. The two-edge crossing-square regression must remain explicit; it cannot be discarded by averaging.

---

## 9. Classification

**Status:** proved report-level exact global train-shear theorem.  
**Level I:** still open.  
**External literature:** none newly imported.  
**Computation:** none.

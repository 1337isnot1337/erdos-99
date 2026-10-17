> Generated reading edition · [exact source](../../../docs/reports/target_c_ens_saturation_disk_nesting_2026-09-09.md) · source SHA-256 `9bc430bb6382b50877601f65bfdaedd62fe6e1176d68e28d40c3d2c7bfa8e857`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-38651031BE0E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ESN: ENS saturation forces one attachment disk, then boundary nesting excludes it

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-e43-scalar-stability`  
**Run type:** equality-case classification / compactness exclusion  
**Target:** Target C C-II after ENS  
**Depends on:** ENS (PR #133), E43/EFAQ (PR #132), JC, ZK, ZT/ZU, C49, C26/C42, planar isodiametry  
**New external literature:** none  
**Computation:** none

## LEVEL I STATUS

**STILL OPEN.**

ENS proves the explicit scalar lower bound

```math
\lambda:=\frac{e_{BB}+2s_C}{D}
\ge
\lambda_E-o(1),
\qquad
\lambda_E=0.4807235804783056468\ldots .
```

This report proves that the ENS threshold itself cannot be approached.

A sequence with `lambda -> lambda_E` would force all scalar relaxations in ENS/JC/ZK to saturate simultaneously. The resulting structure is much sharper than the scalar inequality:

```math
\frac{P_F}{D}\to p_E,
\qquad
\frac hD\to\frac{p_E}{2},
\qquad
\frac{e_{BB}}D\to\lambda_E,
```

while

```math
s_C=o(D),\quad d_H=o(D),\quad Q=o(D),\quad s_Z=o(D).
```

The unloaded contact graph then has

```math
\frac{c_I}{D}
\to
\frac{p_E}{2}-\lambda_E
=1.036933119571389\ldots .
```

Nevertheless, essentially the entire linear component-diameter budget concentrates in one component `I_*`:

```math
\delta_*=(\lambda_E+o(1))D,
\qquad
\sum_{r\ne *}\delta_r=o(D).
```

All but `o(D)` of the other unloaded components are singletons with exactly three loaded contacts. The giant attachment hull `P_*=conv A_*` asymptotically saturates the isodiametric inequality:

```math
\operatorname{diam}(P_*)=(\lambda_E+o(1))D,
\qquad
\operatorname{area}(P_*)
=\left(\frac\pi4\lambda_E^2+o(1)\right)D^2.
```

After scaling by `D`, every Hausdorff limit of `P_*` is therefore a Euclidean disk of diameter `lambda_E`.

But every attachment vertex belongs to `B_+=Vert(F)`. A nested sequence of polygons whose vertices remain vertices of the containing force hull cannot converge to a proper interior disk while the containing hull keeps diameter one. A support-normal argument forces the entire force-hull limit to equal that disk, contradicting `diam(F/D)=1`.

Hence:

### Theorem ESN — uniform strict improvement beyond ENS

There exists an absolute constant

```math
\boxed{\eta_E>0}
```

such that every sufficiently large audited post-ZF survivor satisfies

```math
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_E+\eta_E.
}
\tag{ESN.1}
```

The gap is currently nonconstructive. The explicit floor `0.48072358047` remains valid; ESN proves that it is not the true asymptotic frontier.

---

## 1. Equality variables forced by ENS

Assume for contradiction that an unbounded survivor sequence satisfies

```math
\lambda_j:=\frac{e_{BB,j}+2s_{C,j}}{D_j}
\to\lambda_E.
\tag{1.1}
```

Pass to subsequences whenever necessary.

ENS has a unique global scalar minimizer. Its perimeter split and fixed-perimeter diameter-density minimization therefore force

```math
\boxed{
\frac{P_{F,j}}{D_j}\to p_E,
\qquad
\frac{h_j}{D_j}\to y_E:=\frac{p_E}{2},
}
\tag{ESN.2}
```

where

```math
p_E=3.035313400099390755\ldots,
\qquad
y_E=1.517656700049695377\ldots .
```

Write

```math
t_j:=\frac{e_{BB,j}}{D_j}.
```

Before the relaxation `t<=lambda`, the JC inequality used by ENS is

```math
A-\frac\pi4\lambda^2
\le
\frac{(t+\min\{y,p-y\})^2}{4\pi},
\tag{1.2}
```

with the enhanced PI/Hemmi area lower bound `A`. At the ENS optimizer, replacing `t` by `lambda` makes (1.2) an equality. The right side is strictly increasing in `t`. Hence (1.1)--(ESN.2) force

```math
\boxed{t_j\to\lambda_E.}
\tag{ESN.3}
```

Since

```math
\lambda_j-t_j=\frac{2s_{C,j}}{D_j},
```

we obtain

```math
\boxed{s_C=o(D).}
\tag{ESN.4}
```

---

## 2. Restore the exact JC remainder

JC derives two upper bounds on

```math
E_{out}+Q.
```

Keeping every nonnegative term that JC later dropped gives the exact pair

```math
E_{out}+Q
\le
 e_{BB}+h-3d_H-Q-4s_Z,
\tag{2.1}
```

and

```math
E_{out}+Q
\le
 e_{BB}+P_F-h-3d_H-2s_Z.
\tag{2.2}
```

Indeed (2.1) is the unsimplified form of JC.10 after substituting
`z=Q+2s_Z`, and (2.2) is the actual-perimeter version of JC.12.

Therefore

```math
\boxed{
\frac{E_{out}+Q}{D}
\le
 t-3\frac{d_H}{D}
 +\min\left\{
 y-\frac QD-4\frac{s_Z}{D},
 p-y-2\frac{s_Z}{D}
 \right\}.
}
\tag{ESN.5}
```

ENS ultimately upper-bounds the joint cavity area by the square of the relaxed quantity `lambda+p/2`. At the threshold this relaxed cavity capacity is attained by the scalar equality. Hence the normalized right side of ESN.5 must tend to

```math
\lambda_E+\frac{p_E}{2}.
```

Using ESN.2--ESN.3, every correction in ESN.5 is nonpositive. Equality of the limit therefore forces

```math
\boxed{
 d_H=o(D),
 \qquad Q=o(D),
 \qquad s_Z=o(D).
}
\tag{ESN.6}
```

This is stronger than the published ENS scalar statement.

Since

```math
q=h+d_H,
\qquad
z=Q+2s_Z,
\qquad
x_B=(2h-q)-z,
\qquad
b=2h-z,
```

we also get

```math
\boxed{
\frac qD\to y_E,
\qquad
\frac{x_B}{D}\to y_E,
\qquad
\frac bD\to p_E.
}
\tag{ESN.7}
```

Because `P_F/D->p_E` and `P_F<=b`,

```math
\boxed{b-P_F=o(D).}
\tag{ESN.8}
```

Thus the outer unit-contact boundary walk is asymptotically metric-tight with its convex hull.

Also `f<=Q` and `g_F=Q-f`, so

```math
\boxed{f=o(D),\qquad g_F=o(D).}
\tag{ESN.9}
```

Finally the canonical diameter-graph classification gives

```math
d_H=q-h=
\text{number of tree components of }H,
```

so the full diameter thrackle has only `o(D)` tree components and asymptotically saturates `h<=q`.

---

## 3. The number of unloaded components is forced

ZU gives the exact identity

```math
c_I+e_{BB}+s_C=q-2+d_H+s_Z.
\tag{3.1}
```

Divide by `D` and use ESN.3--ESN.7:

```math
\boxed{
\frac{c_I}{D}
\to
c_E:=y_E-\lambda_E
=1.036933119571389730\ldots .
}
\tag{ESN.10}
```

So the equality regime has linearly many unloaded components even though, as shown next, only one can carry macroscopic graph diameter.

---

## 4. Attachment-area saturation forces one giant component

Let

```math
S_j:=\sum_r\operatorname{area}(\operatorname{conv}A_r).
```

ZK gives

```math
L_2
=6-3(d_H+s_Z)+e_{BB}+2s_C,
\qquad
\sum_r\delta_r\le L_2.
\tag{4.1}
```

The exact pre-relaxation attachment-area estimate is

```math
S_j
\le
\frac\pi4
\left(
\sum_r\delta_r^2
+4\sum_r\delta_r
+4c_I
\right).
\tag{4.2}
```

The last two terms are `O(D)` by ESN.10 and (4.1).

The scalar ENS equality compares

```math
G=\operatorname{area}(F)-S
```

with the JC cavity upper capacity. If `S/D^2` stayed below `pi lambda_E^2/4` by a fixed amount, the lower bound on `G` would exceed the threshold cavity capacity by the same fixed amount. Therefore

```math
\boxed{
\frac{S_j}{D_j^2}
\to
\frac\pi4\lambda_E^2.
}
\tag{ESN.11}
```

ESN.6 and (4.1) give

```math
\limsup\frac1D\sum_r\delta_r\le\lambda_E.
\tag{4.3}
```

Combining (4.2), ESN.11, and (4.3) yields

```math
\boxed{
\frac1{D^2}\sum_r\delta_r^2
\to\lambda_E^2,
\qquad
\frac1D\sum_r\delta_r
\to\lambda_E.
}
\tag{ESN.12}
```

Let

```math
\delta_*:=\max_r\delta_r.
```

Since

```math
\sum_r\delta_r^2
\le
\delta_*\sum_r\delta_r,
```

ESN.12 forces

```math
\boxed{
\frac{\delta_*}{D}\to\lambda_E,
\qquad
\frac1D\sum_{r\ne *}\delta_r\to0.
}
\tag{ESN.13}
```

Thus exactly one unloaded component carries all macroscopic component graph diameter.

---

## 5. ZK removes the remaining component slack

ZK gives the exact identity

```math
\sum_r\delta_r+R_I+s_B+3(d_H+s_Z)
=6+e_{BB}+2s_C,
\tag{5.1}
```

where `R_I>=0` is the total Eppstein edge slack and `s_B>=0` is unused loaded contact-degree capacity.

Using ESN.3--ESN.6 and ESN.12 in (5.1) gives

```math
\boxed{R_I=o(D),\qquad s_B=o(D).}
\tag{ESN.14}
```

For each component, ZK also gives

```math
\tau_r-\delta_r-3=s_r+r_r,
\tag{5.2}
```

where `tau_r=|E(I_r,B_+)|`, `s_r>=0`, `r_r>=0`, and

```math
\sum_rs_r=s_C,
\qquad
\sum_rr_r=R_I.
```

For the giant component `I_*`, ESN.4, ESN.13, and ESN.14 imply

```math
\boxed{
\frac{\tau_*}{D}\to\lambda_E.
}
\tag{ESN.15}
```

---

## 6. Almost every other component is a three-contact singleton

Every non-singleton connected graph has graph diameter at least one. Therefore ESN.13 implies that among the components other than `I_*`, only `o(D)` are non-singletons.

Together with ESN.10, the number `N_1` of singleton unloaded components satisfies

```math
\boxed{
\frac{N_1}{D}\to c_E
=1.036933119571389\ldots .
}
\tag{ESN.16}
```

For a singleton component,

```math
n_r=1,
\quad e_r=0,
\quad\delta_r=0,
\quad r_r=0.
```

Hence (5.2) becomes

```math
\tau_r=3+s_r.
```

Since `sum s_r=s_C=o(D)`, all but `o(D)` singleton components satisfy `s_r=0`. Consequently:

```math
\boxed{
\text{all but }o(D)\text{ of the }c_ED+o(D)\text{ singleton components have exactly three loaded unit-contact neighbors.}
}
\tag{ESN.17}
```

Moreover `s_B=o(D)` and

```math
s_B=3q-e_{BI}-2e_{BB}
```

show that the loaded contact-degree budget is asymptotically saturated:

```math
\boxed{
\frac{e_{BI}}D
\to
3y_E-2\lambda_E
=3.591522939192475\ldots .
}
\tag{ESN.18}
```

This is exactly consistent with one giant component contributing `lambda_E D+o(D)` attachment contacts and `c_E D+o(D)` three-contact singletons contributing `3c_E D+o(D)`.

---

## 7. The giant attachment hull is asymptotically a disk

Put

```math
P_*:=\operatorname{conv}A_*.
```

Every other attachment hull has total area `o(D^2)`. Indeed, by isodiametry and ESN.13,

```math
\sum_{r\ne *}\operatorname{area}(\operatorname{conv}A_r)
\le
\frac\pi4
\left[
\left(\sum_{r\ne *}\delta_r\right)^2
+4\sum_{r\ne *}\delta_r
+4c_I
\right]
=o(D^2).
\tag{7.1}
```

Therefore ESN.11 gives

```math
\boxed{
\frac{\operatorname{area}(P_*)}{D^2}
\to
\frac\pi4\lambda_E^2.
}
\tag{ESN.19}
```

C44's contact-path estimate gives

```math
\operatorname{diam}(P_*)
=\operatorname{diam}(A_*)
\le\delta_*+2.
```

Thus ESN.13 implies

```math
\limsup\frac{\operatorname{diam}(P_*)}{D}
\le\lambda_E.
```

On the other hand the planar isodiametric inequality and ESN.19 force the opposite lower limit. Hence

```math
\boxed{
\frac{\operatorname{diam}(P_*)}{D}
\to\lambda_E,
\qquad
\frac{\operatorname{area}(P_*)}{\operatorname{diam}(P_*)^2}
\to\frac\pi4.
}
\tag{ESN.20}
```

Normalize by `D` and pass to a Hausdorff-convergent subsequence. Isodiametric equality then implies that the limit of `P_*/D` is a Euclidean disk `B` of diameter `lambda_E`.

---

## 8. Boundary-vertex disk nesting lemma

The final contradiction uses only elementary convex support geometry.

### Lemma ESN.1 — a nested vertex polygon cannot converge to a proper disk

Let `P_j subset K_j` be planar compact convex sets such that:

1. `P_j` is a polygon;
2. every vertex of `P_j` is a vertex of `K_j`;
3. `P_j -> B` in Hausdorff distance, where `B` is a nondegenerate Euclidean disk;
4. `K_j -> K` in Hausdorff distance.

Then

```math
\boxed{K=B.}
\tag{ESN.21}
```

#### Proof

Fix a unit direction `u`. The disk `B` has a unique support point `x(u)` in direction `u`.

Choose a vertex `v_j` of the support face of `P_j` in direction `u`. Hausdorff convergence gives convergence of support functions. Every limit point of `v_j` lies in the support face of `B` in direction `u`, which is the singleton `{x(u)}`. Therefore

```math
v_j\to x(u).
\tag{8.1}
```

By hypothesis `v_j` is also a vertex of `K_j`. Choose a unit vector `n_j` in the interior of its normal cone in `K_j`, so

```math
h_{K_j}(n_j)=n_j\cdot v_j.
```

Pass to a subsequence with `n_j->n`. Support-function continuity and (8.1) give

```math
h_K(n)=n\cdot x(u).
\tag{8.2}
```

Because `B subset K`, equation (8.2) says the same line through `x(u)` supports both `K` and `B`. A Euclidean disk has a unique supporting normal at `x(u)`, namely `u`. Hence

```math
n=u.
```

Thus

```math
h_K(u)=u\cdot x(u)=h_B(u).
```

Since `u` was arbitrary, `h_K=h_B` on the unit circle. Therefore `K=B`. `square`

---

## 9. Apply the nesting lemma to the force hull

C26/C42 give

```math
B_+=\operatorname{Vert}(F).
```

Every attachment vertex lies in `B_+`. Since a point extreme in `F` cannot be a convex combination of other attachment points, every member of `A_*` is also a vertex of `P_*`. Hence

```math
\operatorname{Vert}(P_*)\subseteq\operatorname{Vert}(F).
\tag{9.1}
```

Normalize

```math
K_j:=F_j/D_j,
\qquad
P_j:=P_{*,j}/D_j.
```

After translations, pass to a joint Hausdorff-convergent subsequence

```math
K_j\to K,
\qquad
P_j\to B.
```

By construction

```math
\operatorname{diam}(K)=1,
```

while ESN.20 and isodiametric equality give

```math
\operatorname{diam}(B)=\lambda_E<1.
```

But (9.1) lets us apply Lemma ESN.1, which forces `K=B`. This would imply simultaneously

```math
1=\operatorname{diam}(K)
=\operatorname{diam}(B)
=\lambda_E,
```

contradiction.

Therefore no unbounded survivor sequence can satisfy (1.1).

---

## 10. Nonattainment gives a uniform gap

ENS already proves the universal asymptotic lower bound

```math
\liminf\lambda\ge\lambda_E.
```

If no absolute `eta_E>0` existed in ESN.1, then for every integer `m` one could choose a sufficiently large survivor with

```math
\lambda<\lambda_E+1/m.
```

Choosing the diameters increasingly large gives a diagonal sequence with

```math
\lambda_j\to\lambda_E,
```

contradicting Sections 1--9.

Hence some universal `eta_E>0` exists.

No explicit value is claimed. Producing one requires a quantitative version of Lemma ESN.1 or a finite area penalty for an attachment polygon whose vertices all remain extreme in a diameter-one containing hull.

---

## 11. New near-extremal normal form

Although the exact threshold is impossible, any sequence attempting to make the pinned/contact currency small must now approach a very rigid intermediate regime. At the forbidden ENS endpoint:

```math
q/D\to1.51765670005\ldots,
\qquad
h/q\to1,
```

```math
e_{BB}/D\to0.48072358048\ldots,
\qquad
c_I/D\to1.03693311957\ldots,
```

with:

- only `o(D)` diameter-graph tree components;
- `Q,s_Z,s_C=o(D)`;
- outer contact walk excess `b-P_F=o(D)`;
- one unloaded component of graph diameter `(lambda_E+o(1))D` and attachment count `(lambda_E+o(1))D`;
- `c_E D+o(D)` singleton unloaded components, almost all with exactly three loaded contacts;
- asymptotically saturated loaded contact-degree capacity;
- an attachment hull that would have to become an isodiametric disk while all of its vertices stay force-hull vertices.

The last item is the contradiction.

This is a substantially stronger endpoint description than the scalar ENS inequality alone.

---

## 12. Audit / regressions

- The proof does **not** claim the many singleton components lie on the outer contact walk.
- The proof does **not** turn `o(D)` defect into exact zero defect at finite `D`.
- The giant component need not contain most unloaded vertices; it contains essentially all **graph-diameter budget**.
- The disk conclusion is only a Hausdorff limit statement from asymptotic isodiametric equality.
- Lemma ESN.1 uses the fact that every attachment point is a force-hull vertex. It would be false for arbitrary nested polygons whose inner vertices are allowed to become nonextreme in the outer body.
- ESN proves a nonconstructive improvement beyond the explicit ENS constant, not Level I.

## 13. Next target

Quantify the disk-nesting obstruction.

A sufficient finite theorem is:

> **boundary-vertex isodiametric penalty.** For each `0<r<1` there exists explicit `c(r)>0` such that if `P subset K`, `diam(K)=1`, `diam(P)<=r`, and every vertex of the polygon `P` is a vertex of `K`, then
> 

```math
> area(P)\le\frac\pi4r^2-c(r).
> 
```

At `r=lambda_E`, any explicit positive `c(r)` can be fed back into the JC scalar optimization. A reasonably sized penalty would move the numerical floor substantially more than further EFAQ tuning.

A second route is to use the combinatorial part of the normal form directly: one giant component plus `1.0369D` three-contact singleton components, with `b-P_F=o(D)` and only `o(D)` exceptional faces/tree components.

## 14. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Assume lambda=(e_BB+2s_C)/D -> lambda_E (ENS threshold).
Unique scalar equality forces
    P_F/D -> p_E,
    h/D -> p_E/2,
    e_BB/D -> lambda_E,
    s_C=o(D).
Restoring exact JC remainders forces
    d_H=o(D), Q=o(D), s_Z=o(D).
Hence
    q/D -> p_E/2,
    x_B/D -> p_E/2,
    b-P_F=o(D),
    c_I/D -> p_E/2-lambda_E =1.03693311957....

Attachment-area saturation plus ZK forces
    sum delta_r/D -> lambda_E,
    sum delta_r^2/D^2 -> lambda_E^2.
Thus one component has
    delta_*/D -> lambda_E,
    sum_{r!=*} delta_r=o(D).
Also R_I=s_B=o(D). Therefore all but o(D) of the other
~1.0369D components are singletons with exactly three loaded contacts.

The giant attachment hull P_* satisfies
    diam(P_*)/D -> lambda_E,
    area(P_*)/D^2 -> pi lambda_E^2/4,
so P_*/D -> a disk B of diameter lambda_E.
Every vertex of P_* lies in B_+=Vert(F).

Boundary-disk nesting lemma:
If P_j subset K_j, Vert(P_j) subset Vert(K_j), P_j -> a disk B,
and K_j -> K, then K=B. For each disk support direction u, choose a
support vertex v_j of P_j. It tends to the unique disk support point x(u).
Since v_j is also a K_j vertex, take a supporting normal n_j there; any
limit normal must equal the disk's unique normal u. Hence h_K(u)=h_B(u)
for every u, so K=B.

But diam(F/D)=1 while diam(B)=lambda_E<1. Contradiction.
Therefore the ENS threshold is uniformly unattainable: there exists eta_E>0 with
    (e_BB+2s_C)/D >= lambda_E+eta_E
for all sufficiently large survivors.

Next: quantify the boundary-vertex isodiametric penalty, or exploit the
one-giant-plus-1.0369D-three-contact-singletons shell directly.
```

> Generated reading edition · [exact source](../../../docs/reports/target_c_slope_one_outerwalk_singleton_cloud_2026-09-09.md) · source SHA-256 `ab454d30946ba28500f7f8da5d5a6921892fe8d27146b46dd8826f99e3d6d6eb`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-595E906DDC2E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — SOC: slope-one outer-walk floor and forced singleton harmonic cloud

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-nearzero-physical-carrier`  
**Run type:** exact post-ZF ledger synthesis / slope-one population reduction  
**Target:** Target C C-II, S1E/SCC endpoint  
**Depends on:** S1E, SCC, DB, ZU/ZK, HB/PC exact boundary ledger  
**New external literature:** none  
**Computation:** none

## LEVEL I STATUS

**STILL OPEN.**

SCC reduces the RCC slope-one endpoint to an `o(D^2)` force-visible contact core plus a quadratic source population invisible to that core. This note derives two further constraints on that endpoint.

Let

$$
L:=e_{BB}+2s_C,
\qquad
k:=d_H+s_Z.
$$

The finite post-ZF identities give

$$
q=x_B+Q+2k,
\tag{SOC.1}
$$

and the hull-side contact theorem gives

$$
x_B+e_{BB}\ge q.
\tag{SOC.2}
$$

Therefore, without any asymptotic assumption,

$$
\boxed{e_{BB}\ge Q+2k,}
\tag{SOC.3}
$$

and

$$
\boxed{x_B\ge q-L+2s_C\ge q-L.}
\tag{SOC.4}
$$

Now assume the S1E slope-one endpoint

$$
D\varepsilon\to0,
\qquad
L=D+o(D).
\tag{SOC.5}
$$

S1E gives

$$
k=o(D),
\qquad
h=q-o(D).
\tag{SOC.6}
$$

DB gives

$$
\liminf \frac hD\ge2\rho,
\qquad
\rho=\cos\rho=0.7390851332\ldots .
\tag{SOC.7}
$$

Hence

$$
\boxed{
\liminf\frac{x_B}{D}
\ge2\rho-1
=0.4781702664\ldots .
}
\tag{SOC.8}
$$

So the RCC slope-one survivor is forced into the **linear outer-walk phase**. It cannot enter the `x_B=o(D)` near-circle phase of the separate outer-shell route.

There is a second, more structural consequence. ZU gives the exact component-count identity

$$
\boxed{
c_I+e_{BB}+s_C=q-2+k.}
\tag{SOC.9}
$$

Combining this with `L=e_{BB}+2s_C` gives

$$
\boxed{
c_I=q-L+s_C-2+k.}
\tag{SOC.10}
$$

At slope one,

$$
\boxed{
\frac{c_I}{D}
=
\frac qD-1+rac{s_C}{D}+o(1).
}
\tag{SOC.11}
$$

Using DB again,

$$
\boxed{
c_I\ge(2\rho-1)D+s_C-o(D).}
\tag{SOC.12}
$$

S1E and SCC give one unique giant harmonic component `I_*` and

$$
\sum_{r\ne *}\delta_r=o(D).
\tag{SOC.13}
$$

Every connected harmonic component with at least two internal vertices has graph diameter at least one. Therefore the number of nonsingleton components other than `I_*` is at most the left side of SOC.13 and is `o(D)`. Consequently the number `N_1` of singleton unloaded harmonic components satisfies

$$
\boxed{
N_1=c_I-o(D)
\ge(2\rho-1)D+s_C-o(D).
}
\tag{SOC.14}
$$

Each singleton component is one unpinned source point with no internal contact edge. C40/ZK gives for every component

$$
t_r-\delta_r-3=s_r+r_r.
$$

For a singleton, `n_r=1`, `e_r=0`, `delta_r=0`, hence its Eppstein slack is

$$
r_r=2n_r-\delta_r-2-e_r=0.
$$

Thus every singleton satisfies the exact relation

$$
\boxed{t_r=3+s_r\ge3.}
\tag{SOC.15}
$$

In particular SOC.14 forces a linear cloud of positive-contact singleton components, each attached directly to at least three loaded terminals. The total pinned-stress surplus on these singleton stars is exactly

$$
\sum_{r\ singleton}(t_r-3)
\le s_C.
\tag{SOC.16}
$$

Therefore, if a later argument forces `s_C=o(D)`, then all but `o(D)` of the singleton cloud are exact three-contact tripods.

---

## 1. Finite boundary inequality

Starting from SOC.1,

$$
q-x_B=Q+2k.
$$

SOC.2 therefore gives

$$
e_{BB}\ge q-x_B=Q+2k,
$$

which is SOC.3.

Also

$$
x_B\ge q-e_{BB}.
$$

Since `e_BB=L-2s_C`,

$$
x_B\ge q-L+2s_C,
$$

which proves SOC.4.

This form is useful because it records the pinned-stress dependence rather than discarding it. Linear `s_C` makes the required outer-walk excess larger, not smaller.

---

## 2. Slope-one outer-walk floor

Under SOC.5, SOC.4 gives

$$
\frac{x_B}{D}
\ge
\frac qD-1+\frac{2s_C}{D}-o(1).
\tag{2.1}
$$

S1E gives `q-h=o(D)`. Hence DB's post-ZF diameter-edge lower bound SOC.7 implies

$$
\liminf q/D\ge2\rho.
$$

Dropping the nonnegative `2s_C/D` term proves SOC.8.

The stronger parameterized form is

$$
\boxed{
\liminf\frac{x_B-2s_C}{D}
\ge2\rho-1.
}
\tag{SOC.17}
$$

Thus any slope-one subsequence with

$$
\frac{s_C}{D}\to\sigma
$$

obeys

$$
\boxed{
\liminf\frac{x_B}{D}
\ge2\rho-1+2\sigma.
}
\tag{SOC.18}
$$

Since `x_B<=q<=pi D`, this is compatible with all presently known global bounds; it is not by itself a contradiction.

---

## 3. Component-count identity at slope one

ZU gives SOC.9. Substitute

$$
e_{BB}=L-2s_C
$$

to obtain

$$
\begin{aligned}
c_I
&=q-2+k-e_{BB}-s_C\\
&=q-2+k-(L-2s_C)-s_C\\
&=q-L+s_C-2+k,
\end{aligned}
$$

which proves SOC.10.

At S1E, `L=D+o(D)` and `k=o(D)`, yielding SOC.11.

Since `q/D>=2rho-o(1)`, SOC.12 follows.

This is a useful correction to the informal picture of the slope-one endpoint. The endpoint is not merely “one giant harmonic component plus some negligible debris.” It contains **linearly many harmonic components**, while only one of them has macroscopic graph diameter. The remaining component count is forced into graph-diameter-zero pieces.

---

## 4. Almost all non-giant components are singletons

Let `N_{>=2}` be the number of components other than `I_*` with at least two internal vertices. Every such connected graph has

$$
\delta_r\ge1.
$$

Therefore

$$
N_{>=2}
\le
\sum_{r\ne *}\delta_r
=o(D)
$$

by S1E. Hence

$$
N_1
=c_I-1-N_{>=2}
=c_I-o(D).
$$

Insert SOC.12 to prove SOC.14.

The conclusion is independent of the SCC `o(D^2)` population estimate; it uses only the stronger S1E statement that all non-giant **graph diameter** is sublinear.

---

## 5. Singleton components are direct loaded stars

For a singleton `I_r={x}`, there are no internal contact edges. Its attachment contacts are exactly all positive contact rows incident to `x`. The component identities are

$$
s_r=e_r+t_r-2n_r-1=t_r-3,
$$

and

$$
r_r=2n_r-\delta_r-2-e_r=0.
$$

Thus `t_r=3+s_r`, proving SOC.15.

Because the source is triangle-free, no two loaded neighbors of the same singleton can themselves be joined by a unit contact: that would form a unit triangle with the singleton. The attachment set therefore consists of at least three pairwise non-contact loaded terminals on the unit circle around the singleton.

Positive equilibrium at the unpinned singleton also gives

$$
\sum_{b\in A_r}\alpha_{xb}(b-x)=0,
\qquad
\alpha_{xb}>0.
$$

Hence `x` lies in the relative interior of `conv(A_r)`; since at least three distinct contact directions positively span the plane, it lies in the interior of the attachment polygon. This is the geometric “tripod cloud” interpretation.

Summing `s_r=t_r-3` over singleton components gives SOC.16 because `s_C=sum_r s_r`.

---

## 6. Interaction with SCC and the invisible population

SCC proves

$$
|V(C)|=o(D^2),
\qquad
n-|V(C)|=\Theta(D^2).
$$

SOC refines the sparse visible core itself:

1. one component `I_*` has graph diameter `D+o(D)` but only `o(D^2)` vertices and lies in an `o(D)` strip;
2. at least `(2rho-1)D+s_C-o(D)` additional visible components are singleton loaded stars;
3. only `o(D)` further visible components can be nonsingletons;
4. the outer contact walk has unavoidable excess at least `(2rho-1)D-o(D)`.

Thus the remaining quadratic source population is invisible **around a visible skeleton that already spends linear order simultaneously on outer-walk detours and singleton harmonic cells**.

This makes the next global-capacity question more specific than SCC alone.

---

## 7. Regression audit

- SOC does not claim `s_C=o(D)`. A slope-one survivor may still allocate a positive fraction of `D` to pinned-contact surplus.
- Accordingly, SOC does not claim almost every singleton has exactly three attachments unless `s_C=o(D)` is proved separately.
- Linear many singleton cells use only `O(D)` area; their existence alone does not contradict the quadratic source capacity.
- The attachment polygons are noncrossing by C36-C49, but SOC does not assume each attachment set is one cyclic interval. That stronger statement is not part of the current hypotheses.
- The forced outer-walk floor is compatible with the separate PR #119 linear-outer-walk branch; it merely proves that the S1E/SCC endpoint lies there.
- No claim is made that contact-invisible points lie outside the force hull. SCC's global remainder still splits between invisible points inside `F` and points outside `F`.

---

## 8. Next target

There are now two coupled linear resources in the slope-one endpoint:

$$
x_B\ge(2\rho-1)D+2s_C-o(D),
$$

and

$$
N_1\ge(2\rho-1)D+s_C-o(D).
$$

The next useful theorem should exploit the **noncrossing attachment incidence** of the singleton cloud together with the thin giant attachment hull from SCC.

A concrete target is:

> prove that if one attachment cell contains an actual diameter pair and lies in an `o(D)` strip, while `Theta(D)` other harmonic cells are singleton positive stars with pairwise interior-disjoint attachment polygons, then either (i) the outer-walk excess is strictly larger than the SOC lower bound by `Omega(D)`, or (ii) a positive fraction of the singleton surplus is forced, giving `s_C=Omega(D)` with an explicit coefficient.

Either alternative feeds back into SOC.18 and RCC and may raise the slope-one endpoint above one.

## 9. Compact handoff

```text
SOC at the RCC slope-one endpoint.
Exact post-ZF:
    q = x_B + Q + 2(d_H+s_Z),
    x_B + e_BB >= q,
    L=e_BB+2s_C.
Hence exactly
    e_BB >= Q+2(d_H+s_Z),
    x_B >= q-L+2s_C >= q-L.

S1E has L=D+o(D), d_H+s_Z=o(D), h=q-o(D).
DB gives h/D>=2rho-o(1), rho=cos rho.
Therefore
    x_B >= (2rho-1)D+2s_C-o(D)
        >= 0.4781702664... D-o(D).
So slope one is necessarily in the linear outer-walk phase.

ZU:
    c_I+e_BB+s_C=q-2+d_H+s_Z,
so
    c_I=q-L+s_C-2+(d_H+s_Z)
       >=(2rho-1)D+s_C-o(D).
S1E has one giant component and sum_{r!=*}delta_r=o(D).
Every nonsingleton has delta_r>=1, so all but o(D) non-giant components are singletons:
    N_singleton >=(2rho-1)D+s_C-o(D).
For a singleton, r_r=0 and exact component slack gives
    t_r=3+s_r.
Thus the sparse visible core contains a forced linear cloud of direct loaded stars around the thin giant carrier.
```

> Generated reading edition · [exact source](../../../docs/reports/target_c_radial_cut_transport_2026-08-31.md) · source SHA-256 `a4fa3153be5ed32552caeee59fcc3b0b67b22ba1dac4baf71b952baa74a50331`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-3323D6E9BD0C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C72: radial coarea and graph-layer stress transport

**Date:** 2026-08-31  
**Repository base:** `6d5fe9d6` (main after C71 / PR #75)  
**Run type:** exact transport theorem  
**Target:** Target C Gate C-II, especially C71-B single-port spine  
**Depends on:** C11 total contact-stress mass, C14 local diameter-reaction cone, C66 stress-star concentration, C68 radialization, C71 star-branch leakage  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

C71 reduces the near-zero response-defect phase to a return/cycle branch or one physical contact port carrying essentially all mechanical star load. C72 quantifies what happens after that port.

Fix a loaded diameter vertex `z` and write

$$
r_i:=|p_i-z|,
\qquad
S_z:=\sum_{zk\in H}\beta_{zk},
\qquad
\delta_z:=1-S_z.
$$

C68 defines the quadratic radial defect

$$
Q_z:=\sum_{ij\in C}\alpha_{ij}[1-(r_i-r_j)^2]
$$

and proves

$$
Q_z\le D^2\delta_z.
$$

Define the first-order radial transport

$$
T_z:=\sum_{ij\in C}\alpha_{ij}|r_i-r_j|.
$$

Then

$$
\boxed{
\frac12Q_z\le D^2-T_z\le Q_z,
}
\tag{C72.1}
$$

so in particular

$$
\boxed{T_z\ge D^2(1-\delta_z).}
\tag{C72.2}
$$

At the C66 center, where `delta_z<=C_0D epsilon` and `C_0=2pi/kappa_0`,

$$
\boxed{
T_z\ge D^2-C_0D^3\varepsilon.
}
\tag{C72.3}
$$

Thus `D epsilon->0` forces the alpha-weighted contact network to asymptotically saturate its absolute maximum possible radial transport `D^2`.

There are two exact coarea forms.

1. If `A_z(t)` is the total contact stress crossing the Euclidean radial cut `{r<t}`, then
   $$
   \boxed{T_z=\int_0^D A_z(t)\,dt.}
   \tag{C72.4}
   $$
2. If `ell(v)=d_C(z,v)`, `L=ceil(D)`, and `A_j` is the contact stress crossing the graph-distance ball `{ell<=j}`, then for every `0<=j<L`,
   $$
   \boxed{A_j\ge |g_z|-2D\delta_z.}
   \tag{C72.5}
   $$
   Hence the stress on contacts that advance one graph level before level `L` obeys
   $$
   \boxed{
   A_\uparrow\ge L[|g_z|-2D\delta_z]_+.
   }
   \tag{C72.6}
   $$

Using C14,

$$
|g_z|\ge\frac{\sqrt3}{2}D(1-\delta_z),
$$

so `D epsilon->0` implies

$$
\boxed{
\liminf \frac{A_\uparrow}{D^2}\ge\frac{\sqrt3}{2}.
}
\tag{C72.7}
$$

Combined with C71-B, the single-port survivor is therefore not merely one `Omega(D)` port edge. It is followed by a depth-`D` contact transport system whose alpha measure is almost maximally radially efficient, with at least `sqrt(3)/2-o(1)` of the entire stress budget on graph-outward edges before the diameter scale.

This still does not rule out a high-aspect-ratio rhombic carrier with extremely light transverse tracks. It does show that any closing theorem can focus entirely on charging those transverse tracks; the high-stress part is now quantitatively one-way.

---

## 1. First-order radial transport is equivalent to C68's quadratic defect

Every contact has unit length, so the reverse triangle inequality gives

$$
0\le |r_i-r_j|\le1.
$$

For `x in [0,1]`,

$$
1-x\le1-x^2\le2(1-x).
$$

Multiply by `alpha_ij` and sum over contacts. C11 gives

$$
\sum_{ij\in C}\alpha_{ij}=D^2.
$$

Therefore

$$
D^2-T_z
\le Q_z
\le2(D^2-T_z),
$$

which is C72.1.

C68 gives `Q_z<=D^2 delta_z`, proving C72.2. C66 gives

$$
\delta_z\le C_0D\varepsilon,
$$

which proves C72.3.

### Corollary C72.1 — stress on radially inefficient contacts

For fixed `eta in (0,1]`, let

$$
E_{z,\eta}:=
\{ij\in C:|r_i-r_j|\le1-\eta\}.
$$

Then

$$
\boxed{
\sum_{ij\in E_{z,\eta}}\alpha_{ij}
\le\frac{D^2-T_z}{\eta}
\le\frac{Q_z}{\eta}.
}
\tag{C72.8}
$$

At the C66 center, this is `O(D^3 epsilon/eta)`. Thus when `D epsilon->0`, every fixed positive fraction of radial inefficiency carries `o(D^2)` stress.

---

## 2. Continuous radial coarea

For `t in (0,D)`, put

$$
V_t:=\{i:r_i<t\}
$$

and

$$
A_z(t):=
\sum_{\substack{ij\in C\\i\in V_t,\ j\notin V_t}}\alpha_{ij}.
$$

A contact edge crosses exactly the thresholds between its two endpoint radii, an interval of length `|r_i-r_j|`. Fubini gives

$$
\int_0^D A_z(t)dt
=\sum_{ij\in C}\alpha_{ij}|r_i-r_j|
=T_z.
$$

This proves C72.4.

At the C66 center,

$$
\boxed{
\frac1D\int_0^D A_z(t)dt
\ge D-C_0D^2\varepsilon.
}
\tag{C72.9}
$$

No pointwise upper bound `A_z(t)<=D` is asserted. The statement is exact integrated transport.

---

## 3. Every pre-diameter graph layer transmits the center load

Let

$$
\ell(v):=d_C(z,v),
\qquad
L:=\lceil D\rceil.
$$

If `k` is a diameter partner of `z`, every contact path from `z` to `k` has at least `D` unit edges, hence

$$
\ell(k)\ge L.
\tag{C72.10}
$$

For `0<=j<L`, put

$$
U_j:=\{v:\ell(v)\le j\}.
$$

Let

$$
g_v:=\sum_{vk\in H}\beta_{vk}(p_v-p_k)
$$

at loaded vertices and `g_v=0` elsewhere. KKT equilibrium says

$$
\sum_{vw\in C}\alpha_{vw}(p_v-p_w)=g_v.
\tag{C72.11}
$$

Sum over `v in U_j`. Internal contact forces cancel:

$$
\sum_{\substack{vw\in C\\v\in U_j,w\notin U_j}}
\alpha_{vw}(p_v-p_w)
=\sum_{v\in U_j}g_v.
\tag{C72.12}
$$

The right side contains the complete star-center reaction `g_z`, because `z in U_j`, but no opposite endpoint of a `z`-star diameter edge, by C72.10. All other terms come from diameter edges not incident to `z`. Their total beta weight is `delta_z`; counting both possible endpoints gives

$$
\left|\sum_{v\in U_j}g_v-g_z\right|
\le2D\delta_z.
\tag{C72.13}
$$

Let

$$
A_j:=
\sum_{\substack{vw\in C\\v\in U_j,w\notin U_j}}\alpha_{vw}.
$$

Each crossing force vector has norm `alpha_vw`. By C72.12-C72.13,

$$
A_j
\ge\left|\sum_{v\in U_j}g_v\right|
\ge|g_z|-2D\delta_z,
$$

proving C72.5.

---

## 4. The first `ceil(D)` graph layers use disjoint edge stress

For every contact edge `uv`,

$$
|\ell(u)-\ell(v)|\le1.
$$

Hence an edge crosses at most one of the cuts `U_0,...,U_{L-1}`. Define

$$
E_\uparrow^{<L}:=
\{uv\in C:|\ell(u)-\ell(v)|=1,\min(\ell(u),\ell(v))<L\}
$$

and

$$
A_\uparrow:=\sum_{uv\in E_\uparrow^{<L}}\alpha_{uv}.
$$

Then

$$
A_\uparrow=\sum_{j=0}^{L-1}A_j.
$$

Using C72.5,

$$
A_\uparrow
\ge L[|g_z|-2D\delta_z]_+,
$$

which proves C72.6.

Because `A_up<=sum_C alpha=D^2`, C72.6 also gives the finite-scale consistency inequality

$$
\boxed{
\frac{|g_z|}{D}
\le\frac{D}{\lceil D\rceil}+2\delta_z.
}
\tag{C72.14}
$$

This can be strict when `D` is bounded away from the next lower integer, but no arithmetic gap for `D(n)` is assumed.

---

## 5. Universal graph-outward stress fraction

C14 gives

$$
|g_z|
\ge\frac{\sqrt3}{2}DS_z
=\frac{\sqrt3}{2}D(1-\delta_z).
\tag{C72.15}
$$

Substitute into C72.6:

$$
\boxed{
A_\uparrow
\ge
LD\left[
\frac{\sqrt3}{2}
-\left(2+\frac{\sqrt3}{2}\right)\delta_z
\right]_+.
}
\tag{C72.16}
$$

At the C66 center, `delta_z<=C_0D epsilon`; if `D epsilon->0`, then `L/D->1`, so

$$
\liminf A_\uparrow/D^2\ge\sqrt3/2.
$$

This proves C72.7.

The continuous theorem C72.3 is stronger in Euclidean radial efficiency: it says the alpha-weighted sum of actual radial increments is `D^2-o(D^2)`. C72.7 is complementary because it is purely graph-topological and locates a fixed fraction of stress on edges advancing away from the center in the contact metric.

---

## 6. Interaction with C71 single-port concentration

In C71-B, one component `R` of `C-z` carries `w_R->1` star mass through one contact edge `zx_R`, with

$$
\alpha_{zx_R}\ge(c_\infty-o(1))D,
\qquad
c_\infty=0.90348\ldots .
$$

C72 shows that this is not an isolated heavy edge followed by diffuse stress. Before graph distance `ceil(D)`, every level cut carries a vector resultant of order `D`, and at least `sqrt3/2-o(1)` of the entire alpha mass lies on edges that advance one graph level.

Together with C68, all but `o(D^2)` stress is also concentrated on contacts with near-unit Euclidean radial progress. Thus the high-stress carrier in C71-B has the following rigorous aggregate normal form:

```text
one Omega(D) port from z
+ depth at least ceil(D) before any z-star diameter leaf
+ every pre-leaf graph cut carries Omega(D) stress
+ >=sqrt(3)/2-o(1) total alpha on graph-outward edges
+ D^2-o(D^2) alpha-weighted Euclidean radial progress
+ force hull area >=0.1237019... D^2 by C67.
```

The only remaining way to reconcile these facts is to place the two-dimensional geometry in contacts carrying asymptotically negligible stress compared with the radial carrier.

---

## 7. What C72 does not prove

C72 does **not** imply a literal single path. A cut of resultant `Omega(D)` may contain several contact edges whose force vectors nearly align. Nor does it lower-bound the stress on transverse contacts. A high-aspect-ratio rhombic strip/grid can carry almost all stress along one direction while arbitrarily small positive transverse stresses preserve a two-dimensional embedding.

Therefore the next step cannot be another estimate using only the same alpha mass. It must introduce a second resource:

1. vary the normalized KKT certificate and show geometrically essential transverse contacts cannot stay light in every stress;
2. use the Maxwell/Tutte reciprocal dual, where a transverse contact of stress `alpha_e` is a dual edge of the same length `alpha_e`, and derive a global dual-width/area obstruction;
3. use contact-minimality/global source capacity to charge low-stress side branches independently of their alpha weights; or
4. close C71-A first by quantitative separator stability, then show the single-port phase cannot coexist with the full diameter support C65.

## Compact handoff

**C72.1:** with `T_z=sum alpha|Delta r|`,

`Q_z/2 <= D^2-T_z <= Q_z`.

**C72.2:** exact radial coarea:

`T_z=integral_0^D A_z(t)dt`.

**C72.3:** at the C66 center,

`T_z>=D^2-C_0D^3 epsilon`.

**C72.4:** every contact graph-distance cut before `ceil(D)` satisfies

`A_j>=|g_z|-2D delta_z`.

Thus

`A_up>=ceil(D)[|g_z|-2D delta_z]_+`,

and C14 gives

`liminf A_up/D^2>=sqrt(3)/2`

whenever `D epsilon->0`.

**Status:** open. With C71, the single-port branch is now an almost maximally radial depth-`D` stress transport system. The unresolved object is the geometrically essential but arbitrarily low-stress transverse structure.
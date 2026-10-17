> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_robust_sparse_error_path_2026-09-09.md) · source SHA-256 `55b3212a32b59d12d7148b07c9b0df041aadf34c3763a5ce85ebe85125ad10bd`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 14 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-9017E4F32871","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZSP: the sparse-error trunk contains a D+o(D) diameter path

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-deep-harmonic-capture`  
**Run type:** geometric reduction after ZEG Branch A  
**Target:** Target C bridge-dominant near-zero phase  
**Depends on:** ZDC, ZEG, ZRP, C68  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

ZEG Branch A says the exceptional trunk blocks have total graph diameter `o(D)`. ZDC gives directed high-force radial corridors through all but `o(D)` remaining blocks. The first version of this report stopped one step too early and treated the sum of the small radial losses on the selected corridor edges as uncontrolled.

C68 controls that sum directly. Every selected good edge has stress at least `widetilde gamma_D D`, with `delta_D/widetilde gamma_D->0`, while the total weighted radial defect is `Q_z<=C_0D^2 delta_D`. Therefore the **unweighted total radial progress loss along the selected route is o(D)**.

The resulting actual contact path between the captured diameter endpoints has length

```math
\boxed{D+o(D)}.
```

This is a genuine almost-geodesic diameter path. The remaining escape is not route length but weak off-route geometry/loaded attachments.

---

## 1. Complete z--y route path

Use the ZHT/ZHH captured harmonic cell and choose an actual star diameter pair

```math
z,y\in A_*,
\qquad |z-y|=D,
\tag{1.1}
```

whose bridge-tree route contains the complete ZHT trunk. Assume ZEG Branch A:

```math
R_D:=\sum_{X\in\mathcal E_D}\delta_X=o(D).
\tag{1.2}
```

For every ZDC-good nonsingleton internal trunk block choose its directed radial corridor. For every exceptional block, including an endpoint block if necessary, choose a shortest contact path between the appropriate route ports. Add the endpoint attachment contacts needed to start at `z` and finish at `y`, and concatenate with the physical trunk bridges.

This gives an actual contact walk from `z` to `y`. Erase loops to obtain a simple contact path `P_D`. Loop erasure can only shorten it and cannot increase the exceptional-edge count.

Let `P_exc` consist of path edges lying in exceptional block paths, the finitely many endpoint attachment pieces, or trunk positions excluded by ZDC/ZHT radialization. Since every exceptional block shortest path has length at most its graph diameter and (1.2) holds,

```math
\boxed{|P_{exc}|=o(D).}
\tag{ZSP1}
```

All remaining path edges form `P_good`.

---

## 2. Uniform stress scale and radial progress on good edges

Let

```math
\delta_D:=D\varepsilon\to0.
```

ZDC supplies a moving stress coefficient `widetilde gamma_D>0` such that

```math
\boxed{
\frac{\delta_D}{\widetilde\gamma_D}\to0
}
\tag{2.1}
```

and every selected internal good edge satisfies

```math
\alpha_e\ge\widetilde\gamma_DD.
\tag{2.2}
```

The ZHT trunk bridges have the stronger fixed bound `alpha_e>=c_BD`; after decreasing `widetilde gamma_D` if needed, (2.2) therefore holds for every edge of `P_good`.

ZDC also gives one fixed star coordinate `u_0` such that every good edge, oriented from `z` toward `y`, satisfies

```math
 u_0\cdot d_e>0.
\tag{2.3}
```

C68 defines

```math
Q_z
=
\sum_{uv\in C}\alpha_{uv}
\left[1-(r_u-r_v)^2\right]
\le C_0D^2\delta_D,
\qquad r_v=|v-z|.
\tag{2.4}
```

---

## 3. C68 gives an o(D) total radial-loss bound

For a good route edge `e=uv`, put

```math
d_e:=|r_u-r_v|\in[0,1]
```

and

```math
\eta_e:=1-d_e\ge0.
\tag{3.1}
```

Since `0<=d_e<=1`,

```math
1-d_e
\le
1-d_e^2.
\tag{3.2}
```

Using the uniform selected-edge stress floor (2.2),

```math
\begin{aligned}
\sum_{e\in P_{good}}\eta_e
&\le
\sum_{e\in P_{good}}[1-d_e^2]\\
&\le
\frac1{\widetilde\gamma_DD}
\sum_{e\in P_{good}}\alpha_e[1-d_e^2]\\
&\le
\frac{Q_z}{\widetilde\gamma_DD}\\
&\le
C_0D\frac{\delta_D}{\widetilde\gamma_D}.
\end{aligned}
```

By (2.1),

```math
\boxed{
\sum_{e\in P_{good}}(1-|\Delta r_e|)=o(D).
}
\tag{ZSP2}
```

This is stronger than the moving pointwise radial threshold in ZDC: it controls the total route loss.

---

## 4. Radius is monotone between sparse exceptional pieces

For sufficiently large members, every good edge is strongly radial in the ZRP sense. The strongly-radial contact graph is a path forest, and every vertex other than `z` has at most one smaller-radius and one larger-radius strongly-radial neighbor.

Therefore every maximal consecutive good segment of `P_D` has strictly monotone radius. ZDC simultaneously makes its `u_0` coordinate strictly increasing.

Let the good segments be `S_1,...,S_m`. Between them lie the exceptional path pieces. Every exceptional contact edge changes radius by at most one, so the total radial reset available across all exceptional pieces is at most

```math
|P_{exc}|=o(D).
\tag{4.1}
```

Because the path begins at radius zero and ends at radius `D`, summing the telescoping radial increments over the monotone good segments gives

```math
\sum_{e\in P_{good}}|\Delta r_e|
\le D+2|P_{exc}|
=D+o(D).
\tag{4.2}
```

The factor two allows an exceptional piece to reverse radial direction before the next monotone good segment.

---

## 5. The complete contact path has length D+o(D)

By definition,

```math
|P_{good}|
=
\sum_{e\in P_{good}}|\Delta r_e|
+
\sum_{e\in P_{good}}(1-|\Delta r_e|).
```

Use (4.2) and ZSP2:

```math
|P_{good}|\le D+o(D).
\tag{5.1}
```

Together with ZSP1,

```math
|P_D|\le D+o(D).
\tag{5.2}
```

But `P_D` is a unit-edge path from `z` to `y`, and `|z-y|=D`. Triangle inequality gives

```math
|P_D|\ge D.
```

Hence:

### Theorem ZSP.1 — almost-geodesic captured diameter path

Under bridge dominance, `D epsilon->0`, and ZEG Branch A,

```math
\boxed{|P_D|=D+o(D).}
\tag{ZSP3}
```

Moreover only `o(D)` of its edges are exceptional; every other edge is directed forward in the common ZDC star coordinate and lies in the strongly-radial path forest.

---

## 6. Directional concentration around the diameter chord

Orient every unit edge vector of `P_D` from `z` toward `y` and write them as

```math
v_1,\ldots,v_N,
\qquad N=|P_D|.
```

Let

```math
u:=\frac{y-z}{D}.
```

Since

```math
\sum_{i=1}^Nv_i=y-z=Du,
```

we have the exact identity

```math
\sum_{i=1}^N(1-u\cdot v_i)
=N-D.
\tag{6.1}
```

By ZSP3,

```math
\boxed{
\sum_{i=1}^N(1-u\cdot v_i)=o(D).
}
\tag{ZSP4}
```

Consequently, for every fixed angle `theta>0`, the number of path edges making angle at least `theta` with the diameter direction `u` is

```math
\boxed{o(D).}
\tag{ZSP5}
```

Indeed each such edge contributes at least `1-cos theta` to ZSP4.

Thus Theorem P's `15 degree` directional condition fails, if at all, on only `o(D)` path edges.

---

## 7. The entire path lies in an o(D) tube around the diameter segment

For any path vertex `p`, let `L_1,L_2` be the numbers of path edges before and after it. Then

```math
|p-z|+|p-y|
\le L_1+L_2
=N
=D+o(D).
\tag{7.1}
```

Thus every path vertex lies in the ellipse with foci `z,y` and major-axis length `D+o(D)`.

The maximum perpendicular distance of this ellipse from the segment `zy` is

```math
\frac12\sqrt{N^2-D^2}
=
\frac12\sqrt{(N-D)(N+D)}
=o(D).
```

Therefore

```math
\boxed{
\max_{p\in P_D}\operatorname{dist}(p,[z,y])=o(D).
}
\tag{ZSP6}
```

This is a global tube theorem, not merely a local angular statement.

---

## 8. Central path vertices are uniformly subdiametral

Fix `kappa in (0,1/2)`. Put coordinates `z=(0,0)`, `y=(D,0)`. For any path vertex

```math
p=(t,h)
```

with

```math
\kappa D\le t\le(1-\kappa)D,
```

ZSP6 gives `|h|=o(D)`. Let

```math
m=\min(t,D-t)\ge\kappa D.
```

The exact estimate used in Theorem P gives, for every source point `w`,

```math
|p-w|^2
\le
D^2-t(D-t)+\sqrt3D|h|+h^2.
\tag{8.1}
```

Here

```math
t(D-t)\ge\kappa(1-\kappa)D^2,
```

while the final two terms are `o(D^2)`. Therefore for all sufficiently large members,

```math
\boxed{
\max_{w\in A}|p-w|
\le
(1-c_\kappa)D
}
\tag{ZSP7}
```

for some fixed `c_kappa>0` depending only on `kappa`.

In particular no central path vertex can be an actual diameter endpoint.

This is consistent with the unloaded-cell route but becomes useful when a selected ZDC corridor tries to pass through a loaded route block: the path itself must avoid every loaded terminal in the macroscopic central portion.

---

## 9. Exact remaining obstruction

ZEG Branch A is now much narrower than a generic sparse-error path problem. It contains an actual contact path between diameter endpoints satisfying

```text
length = D+o(D),
all vertices lie in an o(D) tube around the diameter segment,
all but o(D) edges lie in any prescribed fixed angular cone around that segment,
all but o(D) edges are strongly radial / ZDC-forward,
central path vertices are uniformly subdiametral from the complete source.
```

A straight or gently perturbed unit chain can satisfy these properties, so this is not itself a contradiction.

The remaining geometry is off the path: ZHA forces `Omega(D)` distinct loaded extreme attachments to the same harmonic cell, while the route path itself is asymptotically one-dimensional and cannot contain loaded terminals throughout its central macroscopic portion.

The next high-value theorem is therefore an **off-path attachment theorem**:

> A globally diameter-minimal triangle-free source cannot attach `Omega(D)` distinct convex-hull diameter terminals to a `D+o(D)` contact path inside one harmonic component while maintaining the ZHT macroscopic bridge forces and the ZHA `o(1/D)` short-response matching.

This is more specific than the previous generic robust-path target.

---

## 10. Classification

**Status:** proved report-level strengthening of ZSP/ZEG Branch A.  
**Level I:** still open.  
**External literature:** none.  
**Computation:** none.

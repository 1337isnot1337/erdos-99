# Target C-II — a CENTER-CORRIDOR has `D/2-O(sqrt D)` edges and linear inverse-diameter near-unit matchings

**Date:** 2026-09-17  
**Status:** proved candidate awaiting promotion; proof-only composition of two current FREE-module reductions  
**Scope:** the `CENTER-CORRIDOR` branch of the central-plane / tangent-gate dichotomy  
**Dependencies:** central-plane / upper-gate dichotomy; FREE outer-corridor total-slack theorem  
**Certificate:** `research/verify_target_c_tooth_reflection_central_plane_corridor_slack_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

Two current results combine more strongly than either statement records separately.

The central-plane dichotomy says that, unless a FREE repair creates an exact anchor or a first upper gate, one parent ancestry chain of old fully inactive vertices crosses the actual support hyperplane through the full-source circumcenter. The concurrent total-slack theorem says that the activation times along any one such ancestry chain telescope.

Consequently a surviving `CENTER-CORRIDOR`

\[
z_0,z_1,\ldots,z_\ell
\]

satisfies all of the following simultaneously:

\[
\boxed{
\sum_{j=0}^{\ell-1}\bigl(|z_{j+1}-z_j|-1\bigr)
\le t_D<h_*+D^{-1/3},
}
\tag{CS.1}
\]

\[
\boxed{
\ell\ge {D\over2}-O(\sqrt D),
}
\tag{CS.2}
\]

and its first central-plane crossing vertex satisfies

\[
\boxed{
-(1+t_D)\le N\cdot(z_\ell-o)<0.
}
\tag{CS.3}
\]

Here

\[
h_*={\sqrt{303}\over52}=0.334747984337100\ldots .
\]

Thus the old `0.3746...D` edge-count lower bound from the edgewise clearing estimate is not the correct leading scale for this branch. The ancestry chain has at least half-diameter many edges up to a `O(sqrt D)` loss, while its **total** excess over unit length stays bounded by an absolute constant.

This also pushes the inverse-`D` matching statement all the way to the actual circumcenter support plane. For every fixed `K>2h_*`, the same corridor contains a vertex-disjoint matching of original fully inactive pairs with

\[
1<|x-y|\le1+{K\over D}
\]

and size

\[
\boxed{
\left({1\over4}-{h_*\over2K}-o(1)\right)D.
}
\tag{CS.4}
\]

For `K=1`, this is

\[
\boxed{(0.0826260078314499\ldots-o(1))D.}
\tag{CS.5}
\]

For `K=2`, it is

\[
\boxed{(0.166313003915725\ldots-o(1))D.}
\tag{CS.6}
\]

More generally, if `K_D -> infinity` while `K_D=o(D)`, parity thinning gives

\[
\boxed{
(1/4-o(1))D
}
\tag{CS.7}

vertex-disjoint corridor pairs of length at most

\[
1+{K_D\over D}=1+o(1).
\]

The point of (CS.7) is cardinality: almost the full quarter-diameter matching ceiling of a path survives at an arbitrarily slowly relaxed inverse-diameter scale.

---

## 1. Activation times still telescope up to the central-plane event

Let

\[
0=s_0<s_1<\cdots<s_\ell\le t_D
\]

be the absorption times along the ancestry chain, with `z_0` an original blocker root. Put

\[
\tau_j=s_{j+1}-s_j>0.
\]

At the absorption of `z_{j+1}` the parent has moved for exactly `tau_j`, so

\[
\left|z_j-\tau_jN-z_{j+1}\right|=1.
\tag{CS.8}
\]

The central-plane theorem stops the process when `z_ell` is absorbed. Nothing in the activation-time telescope requires the later clearing time to be reached. Therefore

\[
\boxed{
\sum_{j=0}^{\ell-1}\tau_j=s_\ell\le t_D.
}
\tag{CS.9}
\]

Every chain vertex is fully inactive in the original source, so consecutive vertices were strict old noncontacts. From (CS.8),

\[
1<|z_j-z_{j+1}|\le1+\tau_j.
\]

Writing

\[
\sigma_j:=|z_j-z_{j+1}|-1>0,
\]

we have `sigma_j<=tau_j`. Summation with (CS.9) proves (CS.1).

---

## 2. The edge count reaches the half-diameter scale

The support-depth coordinate is

\[
a_v=H-N\cdot v.
\]

Strict support monotonicity gives

\[
a_{z_\ell}-a_{z_0}
=\sum_{j=0}^{\ell-1}N\cdot(z_j-z_{j+1}).
\]

For every edge,

\[
N\cdot(z_j-z_{j+1})
\le |z_j-z_{j+1}|
=1+\sigma_j.
\]

Hence

\[
a_{z_\ell}-a_{z_0}
\le\ell+\sum_j\sigma_j
\le\ell+t_D,
\]

so

\[
\boxed{
\ell\ge a_{z_\ell}-a_{z_0}-t_D.
}
\tag{CS.10}
\]

The central-plane event has

\[
a_{z_\ell}>C_D:=H-N\cdot o,
\]

while the blocker root has

\[
a_{z_0}=O(\sqrt D).
\]

The same-center support estimate gives

\[
C_D>{D\over2}-3^{1/4}\sqrt D-h_*.
\]

Since `t_D=O(1)`, substitution into (CS.10) yields

\[
\boxed{
\ell\ge {D\over2}-O(\sqrt D),
}
\]

which is (CS.2).

This is a genuine improvement over applying the edgewise bound `|z_{j+1}-z_j|<=1+t_D` separately, which loses the factor `1+h_*` in the leading coefficient.

---

## 3. Fixed inverse-`D` thresholds give linear matchings

Fix `K>0`. Call an edge bad when

\[
\sigma_j>{K\over D}.
\]

If `B_K` is the number of bad edges, then (CS.1) gives

\[
B_K{K\over D}
<\sum_j\sigma_j
\le t_D,
\]

and therefore

\[
B_K
\le {t_DD\over K}
=\left({h_*\over K}+o(1)\right)D.
\tag{CS.11}
\]

Using (CS.2), the number of good corridor edges is at least

\[
\left({1\over2}-{h_*\over K}-o(1)\right)D.
\tag{CS.12}
\]

The even and odd edge classes of a path are each vertex-disjoint. Keeping the larger parity class proves (CS.4).

For `K=1`,

\[
{1\over4}-{h_*\over2}
=0.0826260078314499\ldots .
\]

For `K=2`,

\[
{1\over4}-{h_*\over4}
=0.166313003915725\ldots .
\]

The fixed-`K` coefficient is positive exactly for `K>2h_*`.

If instead `K=K_D->infinity`, (CS.11) says only `o(D)` edges are bad. Equation (CS.2) then leaves `(1/2-o(1))D` good edges, and parity thinning gives (CS.7). The additional condition `K_D=o(D)` merely ensures the retained distance threshold tends to one.

---

## 4. The matching persists to a moving terminal slab ending at the circumcenter plane

The older slab theorem was stated for fixed

\[
0\le\alpha<\beta<{1\over2}.
\]

The central-plane crossing permits a terminal slab whose deep endpoint is the actual module-dependent value `C_D`.

Fix `0<=alpha<1/2`. Let `i_alpha` be the first index with support depth above `alpha D`, and let `z_ell` be the first central-plane crossing. The support-depth span of this terminal subchain is

\[
C_D-\alpha D-O(1)
=\left({1\over2}-\alpha\right)D-O(\sqrt D).
\tag{CS.13}
\]

Applying the same total-slack and parity argument only to this terminal subchain gives, for every fixed

\[
K>{h_*\over 1/2-\alpha},
\]

a vertex-disjoint matching of size

\[
\boxed{
\left(
{1/2-\alpha-h_*/K\over2}-o(1)
\right)D
}
\tag{CS.14}
\]

whose pair lengths lie in `(1,1+K/D]` and whose vertices are all old fully inactive source points on the same simple outer-face corridor.

For example, with `alpha=1/4` and `K=2`, the last quarter-depth portion of the path, ending at the actual circumcenter support plane, contains

\[
\boxed{
(0.0413130039157249\ldots-o(1))D
}
\tag{CS.15}

vertex-disjoint old-inactive pairs of length at most `1+2/D`.

---

## 5. What this does not prove

The result does not make different module corridors vertex-disjoint. They may merge after their initially separated prefixes.

It also does not show that the polygonal corridor is a near-geodesic in Euclidean length. Equation (CS.2) is a lower bound on the number of edges, not an upper bound. A corridor may still make many additional nearly tangent steps while remaining strictly monotone in support depth.

Finally, the inverse-`D` pairs are not automatically the LOWER exact-swap blockers from the Horn branch. Additional local support/force information would be required before importing the four-row LOWER machinery.

What is now forced in the `CENTER-CORRIDOR` branch is narrower and exact:

```text
simple old-inactive outer-face ancestry path
crosses the actual circumcenter support hyperplane
>= D/2-O(sqrt D) edges
O(1) total edge-length excess above one
linear 1+K/D matching for every fixed K>2h_*
(1/4-o(1))D matching at every slowly relaxed K_D/D scale
```

The remaining closure problem is source-preserving. One must exploit the ordered outer-face placement and bounded total slack to close many of these gaps simultaneously, or derive a force-hull/outer-walk obstruction from a corridor that passes through the circumcenter support plane.

**Disposition:** composed the central-plane stopping theorem with the activation-time telescope, raising the CENTER-CORRIDOR edge count to `D/2-O(sqrt D)` and carrying the linear inverse-diameter matching all the way to the actual circumcenter support plane. C-II remains open.

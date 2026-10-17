> Generated reading edition · [exact source](../../../docs/reports/target_c_radial_flux_divergence_2026-08-31.md) · source SHA-256 `d6481ed890ac516ecd60a12cf57be5373ffb72adef3bade6adb9165534d2afa3`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-474B7A1E95FD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C74: pointwise radial-flux transport

**Date:** 2026-08-31  
**Repository base:** `41b7c431` (main after C73 / PR #77)  
**Run type:** exact local equilibrium / Euclidean radial-cut theorem  
**Target:** Target C Gate C-II, C66-C73 near-zero stress-star phase  
**Depends on:** C18 diameter-star angle gap, C66 stress-star concentration, C68 radial defect, C72 radial transport  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

C72 proves an averaged Euclidean radial coarea identity and an `Omega(D)` lower bound
on every pre-diameter graph-distance cut. C74 strengthens the Euclidean side.

There are two levels of statement.

1. The local radial-divergence identity and radial-cut balance below are exact for every
   diameter vertex `z`, with no large-`D` assumption.
2. The explicit pointwise lower bound using the stronger C18 reaction cone is invoked
   only for `D>=20`, when the C18 angular width `Theta_D` is strictly below `pi/3` and
   the diameter-star directions lie in one interval of that width.

In that large-`D` regime, every Euclidean circle of radius `t<D` carries
`Omega(D)` signed outward radial contact stress. At the C66 center with
`D epsilon->0`, the uniform constant tends to `0.90348...`.

---

## 1. Exact local radial identity

Fix a diameter vertex `z`. For every source vertex `v`, put

```math
r_v:=|p_v-p_z|.
```

For a contact `vj` incident to `v\ne z`, define

```math
d_{vj}:=r_j-r_v\in[-1,1]
\tag{C74.1}
```

and

```math
q_{vj}:=1-d_{vj}^2\ge0.
\tag{C74.2}
```

Let

```math
n_v:=\frac{p_v-p_z}{r_v}.
```

Since `|p_j-p_v|=1`,

```math
r_j^2-r_v^2
=2(p_v-p_z)\cdot(p_j-p_v)+1.
```

Using `r_j=r_v+d_{vj}` gives

```math
\boxed{
 n_v\cdot(p_j-p_v)
=d_{vj}-\frac{q_{vj}}{2r_v}.
}
\tag{C74.3}
```

This is exact.

Use the reaction convention

```math
g_v:=\sum_{vk\in H}\beta_{vk}(p_v-p_k),
```

with `g_v=0` at unloaded vertices. KKT equilibrium is

```math
\sum_{vj\in C}\alpha_{vj}(p_v-p_j)=g_v.
\tag{C74.4}
```

Equivalently,

```math
\sum_{vj\in C}\alpha_{vj}(p_j-p_v)=-g_v.
```

Dot with `n_v` and use C74.3.

### Lemma C74.1 — local radial divergence

For every contact-core vertex `v\ne z`,

```math
\boxed{
\sum_{vj\in C}\alpha_{vj}(r_j-r_v)
=
\frac1{2r_v}
\sum_{vj\in C}\alpha_{vj}[1-(r_j-r_v)^2]
-g_v\cdot n_v.
}
\tag{C74.5}
```

At every unloaded vertex,

```math
\boxed{
\sum_{vj\in C}\alpha_{vj}(r_j-r_v)\ge0.
}
\tag{C74.6}
```

Thus unloaded equilibrium cannot destroy signed outward radial stress flux. Its radial
divergence is exactly the local C68 defect divided by `2r_v`.

If

```math
q_v:=\sum_{vj\in C}\alpha_{vj}[1-(r_j-r_v)^2],
```

then

```math
\sum_v q_v=2Q_z,
```

where C68 defines

```math
Q_z:=\sum_{ij\in C}\alpha_{ij}[1-(r_i-r_j)^2].
```

---

## 2. Exact Euclidean radial-cut balance

Choose `t in (0,D)` different from every source radius and put

```math
V_t:=\{v:r_v<t\}.
```

For a contact crossing this cut, orient it from its inside endpoint `i` to its outside
endpoint `j`. Define

```math
F_z(t):=
\sum_{\substack{ij\in C\\r_i<t<r_j}}
\alpha_{ij}(r_j-r_i).
\tag{C74.7}
```

Every summand is nonnegative.

At the center, every contact neighbor has radius exactly one. Define

```math
J_z:=\sum_{zj\in C}\alpha_{zj}.
\tag{C74.8}
```

Sum C74.5 over `V_t\setminus\{z\}` and add the center contribution `J_z`.
Every internal contact cancels because its signed radial increments at the two
endpoints are opposite. The boundary terms are exactly C74.7.

### Lemma C74.2 — exact radial-cut balance

```math
\boxed{
F_z(t)
=J_z
+
\sum_{\substack{v\in V_t\\v\ne z}}
\frac{q_v}{2r_v}
-
\sum_{\substack{v\in V_t\\v\ne z}}
g_v\cdot n_v.
}
\tag{C74.9}
```

This is an exact scalar divergence theorem for the KKT contact stress.

---

## 3. Reaction drain below the diameter sphere

Put

```math
S_z:=\sum_{zk\in H}\beta_{zk},
\qquad
\delta_z:=1-S_z.
\tag{C74.10}
```

Every endpoint `k` of a `z`-star diameter edge has

```math
r_k=D.
```

Hence no such endpoint lies in `V_t` for `t<D`.

For a loaded vertex put

```math
s_v:=\sum_{vk\in H}\beta_{vk}.
```

Every loaded vertex in `V_t\setminus\{z\}` is charged only through non-star diameter
edges. Summing endpoint degrees of those non-star edges gives

```math
\sum_{\substack{v\in V_t\\v\ne z}}s_v\le2\delta_z.
\tag{C74.11}
```

Since each diameter reaction vector has length `D`,

```math
|g_v|\le Ds_v,
```

and therefore

```math
\sum_{\substack{v\in V_t\\v\ne z}}g_v\cdot n_v
\le2D\delta_z.
\tag{C74.12}
```

The defect term in C74.9 is nonnegative, so

### Corollary C74.3 — universal cut lower bound from the center source

For every regular `t in (0,D)`,

```math
\boxed{
F_z(t)\ge J_z-2D\delta_z.
}
\tag{C74.13}
```

No angular hypothesis has been used yet.

---

## 4. Large-D center reaction from C18

KKT equilibrium at `z` gives

```math
\sum_{zj\in C}\alpha_{zj}(p_z-p_j)=g_z.
```

By the triangle inequality,

```math
J_z\ge|g_z|.
\tag{C74.14}
```

For `D>=20`, C18 gives a common angular interval of width at most

```math
\Theta_D:=
\frac{
D\left(\frac{5\pi}{6}-\sqrt3\right)
+\frac{4\pi}{3}
+\frac{\pi}{2D}
}{D+1}
<\frac\pi3
\tag{C74.15}
```

containing all `z`-star diameter directions. Put

```math
c_D:=\cos(\Theta_D/2)>0.
\tag{C74.16}
```

Project the star reaction at `z` onto the interval bisector. This gives

```math
|g_z|\ge Dc_DS_z.
\tag{C74.17}
```

Combine C74.13-C74.17.

### Theorem C74 — pointwise Euclidean radial-flux transport

For `D>=20`, every diameter vertex `z` and every regular `t in (0,D)` satisfy

```math
\boxed{
F_z(t)
\ge
D[c_DS_z-2\delta_z]
=
D[c_D-(c_D+2)\delta_z].
}
\tag{C74.18}
```

At the C66 star center,

```math
\delta_z\le C_0D\varepsilon,
\qquad
C_0:=2\pi/\kappa_0.
\tag{C74.19}
```

Also

```math
c_D\to
c_\infty
:=
\cos\left(\frac{5\pi}{12}-\frac{\sqrt3}{2}\right)
=0.90348\ldots .
```

Hence:

### Corollary C74.4 — uniform near-zero radial flux

Along any hypothetical C-II sequence with `D epsilon->0`, at the C66 center,

```math
\boxed{
\inf_{0<t<D}\frac{F_z(t)}D
\ge c_\infty-o(1).
}
\tag{C74.20}
```

The infimum can be read over regular radii; one-sided limits give the same bound at
vertex radii.

---

## 5. Squared-radial coarea

A contact with endpoint radii `a<b` crosses the thresholds `t in (a,b)`. Its value in
`F_z(t)` is `alpha(b-a)` throughout that interval. Thus

```math
\int_0^D F_z(t)\,dt
=
\sum_{ij\in C}\alpha_{ij}(r_i-r_j)^2.
\tag{C74.21}
```

Since C11 gives

```math
\sum_{ij\in C}\alpha_{ij}=D^2,
```

we obtain:

### Corollary C74.5 — exact radial-flux energy

```math
\boxed{
\int_0^D F_z(t)\,dt=D^2-Q_z.
}
\tag{C74.22}
```

This complements C72's first-order identity

```math
T_z=\int_0^D A_z(t)\,dt,
```

where `A_z(t)` is unweighted cut stress and the edge contribution uses one power of
`|Delta r|`. C74.22 uses the signed outward radial flux and two powers of
`|Delta r|`.

---

## 6. Interaction with C71-C73

When `D epsilon->0`, the current single-port/return stack now forces:

- C71: a returning component at `z`, or one physical port carrying essentially all
  star mass with stress `Omega(D)`;
- C72: every pre-leaf graph-distance cut transmits `Omega(D)` total stress and almost
  all alpha mass has near-maximal radial progress;
- C73: all but `O(D)` core vertices lie in clean degree-four strict-rhombus
  neighborhoods;
- C74: every Euclidean radial cut below `D` transmits at least
  `(0.90348-o(1))D` signed outward radial stress.

The heavy carrier can therefore neither disappear into local circulation nor vanish
between graph layers. The only remaining escape is to support the required
quadratic-area geometry on contacts carrying asymptotically negligible alpha weight.

---

## 7. What remains

C74 is still a one-certificate theorem. It cannot by itself charge a transverse edge
whose chosen alpha weight is arbitrarily small. That limitation is real and agrees
with C72's audit.

The next useful input must be independent of the fixed alpha mass. The leading options
are:

1. use the Maxwell reciprocal: every radial cut has a dual transverse displacement of
   order `D`, and try to force reciprocal width/area beyond the mixed-area/perimeter
   bounds;
2. vary the normalized KKT certificate so geometrically essential C73 transverse
   contacts cannot remain light in every stress; or
3. prove quantitative stability of the C71 return/separator branch and eliminate that
   branch using C70 response starization.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Exact, all D:
  sum_j alpha_vj(r_j-r_v)
    = [1/(2r_v)] sum_j alpha_vj[1-(r_j-r_v)^2] - g_v dot n_v.
Thus unloaded vertices have nonnegative radial-stress divergence.

For every Euclidean cut V_t={r<t}, t<D:
  F_z(t)=J_z + sum_inside q_v/(2r_v) - sum_inside g_v dot n_v,
so
  F_z(t)>=J_z-2D delta_z.

For D>=20, C18 gives
  J_z>=|g_z|>=D c_D S_z,
therefore
  F_z(t)>=D[c_D S_z-2delta_z]
for every t<D.
At the C66 center and D epsilon->0,
  inf_t F_z(t)/D >=0.90348...-o(1).

Also
  integral_0^D F_z(t)dt=D^2-Q_z.
```

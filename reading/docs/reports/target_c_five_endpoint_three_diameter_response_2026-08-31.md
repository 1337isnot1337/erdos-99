> Generated reading edition · [exact source](../../../docs/reports/target_c_five_endpoint_three_diameter_response_2026-08-31.md) · source SHA-256 `8a1f1ba249ce8bb6523223df203228f4f78e66b2c2f7bace25a9a3dd49f0802d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-5FB5FCCB3CCA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: the five-endpoint three-diameter reduction

**Date:** 2026-08-31
**Repository state:** 43bae6e (`research/target-c-next-2026-08-31`)
**Run type:** exact affine-stress sign reduction
**Target:** Target C Gate C-I
**External web search:** not used
**Computation:** exploratory sanity checks only; not used in the proof

## LEVEL I STATUS

**STILL OPEN.**

The response-inertia theorem C30 reduces a three-edge diameter forest to one possible
non-affine negative mode. C31 removes the four-endpoint forest. This addendum removes
the five-endpoint forest as well; the only remaining three-edge forest topology is a
matching on six endpoints.

## Theorem C32

Let (A) be a diametrally saturated source with (D>1), and let
(s=(\alpha,\beta)) be a normalized KKT stress. Let (G_s=(V_s,C_s)) be its
connected positive unit-contact graph, let (H_s) be its positive diameter support,
and put (B=V(H_s)). Assume that (H_s) is a three-edge forest,

```math
|B|=5,\qquad \operatorname{aff}B\text{ is two-dimensional}.
```

Then, for the signed stress matrix

```math
\Omega_s=L_{C_s}(\alpha)-L_{H_s}(\beta),
```

```math
\boxed{\Omega_s\succeq0.}
\tag{C32.1}
```

Consequently the C30 scalar response parameter satisfies

```math
\boxed{\rho_s\le1.}
\tag{C32.2}
```

### Proof

A three-edge forest on five non-isolated endpoints is a two-edge path together with
one disjoint edge. Since every positive diameter endpoint is a convex-hull vertex,
two disjoint diameter edges cannot be opposite boundary sides of the convex
polygon: if (AB) and (CD) were such sides, the crossing diagonals would give

```math
|AB|+|CD|<|AC|+|BD|\le2D,
```

contradicting (|AB|=|CD|=D). Thus all three support edges are diagonals. A cyclic
order check gives, after relabeling the convex pentagon,

```math
H_s=\{02,13,24\}.
\tag{C32.3}
```

In particular the boundary pairs

```math
01,\quad12,\quad23,\quad34,\quad40
\tag{C32.4}
```

are not diameter-support edges.

Let (I=V_s\setminus B), let $`\Lambda`$ be the positive contact Dirichlet
response on (B), and put (M=\Lambda-L_{H_s}). By C11,

```math
M\mathbf1=0,\qquad MP_B=0.
\tag{C32.5}
```

For each omitted vertex (r=0,1,2), choose the alternating affine circuit of the
remaining four convex-hull vertices. With positive entries (a,b,c,d,e,f,g,h,i,j,k,\ell),
write

```math
\begin{aligned}
a^{(0)}&=(0,a,-b,c,-d),\\
a^{(1)}&=(-e,0,f,-g,h),\\
a^{(2)}&=(i,-j,0,k,-\ell).
\end{aligned}
\tag{C32.6}
```

These vectors span the two-dimensional affine-dependence space. Their unique
relation has positive coefficients; rescale it as

```math
u a^{(0)}+a^{(1)}+v a^{(2)}=0,qquad u,v>0.
\tag{C32.7}
```

Coordinate comparison gives

```math
e=vi,\qquad f=ub,\qquad g=uc+vk,\qquad h=ud+v\ell,
\tag{C32.8}
```

with also (ua=vj), which is not needed below.

Every symmetric matrix annihilating (\mathbf1,x,y) is a symmetric form on this
two-dimensional dependence space. The three rank-one matrices in (C32.6) are
linearly independent (entries (12,01,02) isolate them), so

```math
M=c_0a^{(0)}a^{(0)\mathsf T}
 +c_1a^{(1)}a^{(1)\mathsf T}
 +c_2a^{(2)}a^{(2)\mathsf T}
\tag{C32.9}
```

for real (c_0,c_1,c_2). The response has nonpositive off-diagonal entries. The
non-support signs at (01) and (12) therefore give

```math
c_2\ge0,\qquad c_0\ge0.
\tag{C32.10}
```

If (c_1\ge0), (C32.9) is positive semidefinite. Otherwise set (c_1=-t),
(t>0). The remaining signs at (23,40,34) give

```math
\begin{aligned}
t&\le U_2:=\frac{bc}{fg}c_0
 =\frac{c}{u(uc+vk)}c_0,\\
t&\le U_1:=\frac{i\ell}{eh}c_2
 =\frac{\ell}{v(ud+v\ell)}c_2,\\
t&\le U_3:=\frac{cd\,c_0+k\ell\,c_2}{gh}.
\end{aligned}
\tag{C32.11}
```

On the dependence coordinates (X=a^{(0)\mathsf T}q) and
(Z=a^{(2)\mathsf T}q), relation (C32.7) makes the quadratic form equal to

```math
c_0X^2-t(uX+vZ)^2+c_2Z^2.
\tag{C32.12}
```

It is positive semidefinite exactly when

```math
t\le T:=\frac{c_0c_2}{c_0v^2+c_2u^2}.
\tag{C32.13}
```

Assume (c_0,c_2>0) and put (x=c_0/c_2). Direct comparison gives

```math
U_2\le T\quad\text{if }x\le x_0:=\frac{uk}{cv},
\qquad
U_1\le T\quad\text{if }x\ge x_1:=\frac{u\ell}{dv}.
\tag{C32.14}
```

For the intermediate range, the comparison with (U_3) is governed by the exact
factorization

```math
\begin{aligned}
&x(uc+vk)(ud+v\ell)
 -(cdx+k\ell)(xv^2+u^2)\\
&\qquad=-(cvx-ku)(dvx-\ell u).
\end{aligned}
\tag{C32.15}
```

Thus (U_3\le T) whenever (x) lies between (x_0) and (x_1). If
(x_0\le x_1), (C32.14) and the intermediate case cover all (x>0). If
(x_1<x_0), the first two inequalities already cover all (x>0). Hence
(t\le T). If (c_2=0), the (40) inequality forces (t=0); if (c_0=0),
the (23) inequality forces (t=0). Therefore (M\succeq0).

The positive interior block (L_{C_s}[I,I]) is positive definite. Schur
congruence gives

```math
\Omega_s\sim_{\mathrm{cong}}
M\oplus L_{C_s}[I,I],
\tag{C32.16}
```

which proves (C32.1). C30 identifies the only possible non-affine eigenvalue for a
three-edge forest as (\rho_s), so (C32.1) gives (C32.2). $`\square`$

## Exact effect on Target C

C30 bounds the negative inertia of a three-edge forest by one. C31 and C32 show that
the four- and five-endpoint forest regimes cannot realize that negative mode. Hence
the only unresolved three-edge forest support is the six-endpoint matching

```math
H_s=\{03,14,25\}
```

up to cyclic relabeling. This is a genuine C-I narrowing, not a closure: C30--C32
still do not prove that a direction-dependent second-order stress has maximal
diameter support, nor do they eliminate the six-endpoint matching.

## Audit classification and regressions

- **Proved:** (C32.1), (C32.2), and the five-endpoint sign-factorization.
- **Not proved:** strict (\rho_s<1) in the five-endpoint case; equality is allowed.
- **Open:** the six-endpoint matching and C13 support selection.
- **Rejected:** any extension of this pentagon factorization to arbitrary endpoint
  sets or a universal PSD claim for (\Lambda-L_H).

The proof uses the actual positive contact-network response, not an independently
chosen scaffold. It does not use triangle-freeness, global asymptotic packing bounds,
uniform stress lower bounds, or a generic Loewner comparison.

## Exploratory computation

One-off floating-point samples of convex five-point affine-dependence data found no
indefinite form satisfying the five non-support sign inequalities. Those samples
omitted exact diameter realization and global optimality, prove nothing, and are not
used in the proof.

## Compact handoff

```math
\begin{array}{c|c}
\text{three-edge forest endpoints}&\text{response conclusion}\\\hline
4&\Omega_s\succeq0,\text{ strict }\rho_s<1\text{ if triangle-free}\\
5&\Omega_s\succeq0,\ \rho_s\le1\\
6&\text{matching; open}
\end{array}
```

The next exact response target is the six-point matching, with three-dimensional
affine-dependence space. Do not assume its response defect is PSD without a new
sign-cone proof.

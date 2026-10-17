> Generated reading edition · [exact source](../../../docs/reports/target_c_six_endpoint_sign_cone_regression_2026-08-31.md) · source SHA-256 `e3ed66a15dbef79ab46ad8d294c4315f86c60ba19d6f3d1ff9ebea0df183740a`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-52222279AB14","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: six-endpoint sign-cone regression

**Date:** 2026-08-31
**Repository state:** c4311de (`research/target-c-promote-c30-c32-2026-08-31`)
**Run type:** exact finite regression
**Target:** Target C Gate C-I, six-endpoint three-diameter matching
**External web search:** used only to record the circular-minor diagnostic
**Arithmetic:** exact integer matrices

## LEVEL I STATUS

**STILL OPEN.**

This note rejects a tempting but insufficient extension of C31-C32. For a convex
hexagon with matching diameter support, the facts

```math
M\mathbf1=0,\qquad MP_B=0,\qquad M_{ij}\le0
\quad(ij\notin H)
```

do **not** force (M=\Lambda-L_H) to be positive semidefinite. The missing
information must include genuine circular-planar response constraints, unit-contact
geometry, or another Target C hypothesis.

## Exact regression

Take the regular hexagon in cyclic order

```math
p_r=(\cos(r\pi/3),\sin(r\pi/3)),\qquad 0\le r<6,
```

and the matching

```math
H=\{03,14,25\}.
```

The three matching pairs have the common diameter (D=2). The affine kernel is
unchanged if the two coordinate columns are rescaled, so use the integer-scaled
coordinate columns

```math
x=(2,1,-1,-2,-1,1),\qquad y=(0,1,1,0,-1,-1).
```

The columns of

```math
Z=\begin{pmatrix}
-1&-2&-2\\
2&3&2\\
-2&-2&-1\\
1&0&0\\
0&1&0\\
0&0&1
\end{pmatrix}
```

span ({\mathbf1,x,y\}^{\perp}). Define

```math
M_{\rm ind}=
\begin{pmatrix}
2&-2&0&2&-2&0\\
-2&5&-4&0&3&-2\\
0&-4&5&-2&-2&3\\
2&0&-2&2&0&-2\\
-2&3&-2&0&1&0\\
0&-2&3&-2&0&1
\end{pmatrix}.
\tag{C33.1}
```

Direct multiplication gives

```math
M_{\rm ind}\mathbf1=M_{\rm ind}x=M_{\rm ind}y=0.
\tag{C33.2}
```

For every nonmatching pair (ij\notin H), the upper-triangular entries are

```math
\begin{array}{c|rrrrrrrrrrrr}
ij&01&02&04&05&12&13&15&23&24&34&35&45\\\hline
(M_{\rm ind})_{ij}&-2&0&-2&0&-4&0&-2&-2&-2&0&-2&0.
\end{array}
\tag{C33.3}
```

Thus all required nonmatching response signs hold. Nevertheless

```math
M_{\rm ind}=ZQ_{\rm ind}Z^{\mathsf T},qquad
Q_{\rm ind}=
\begin{pmatrix}2&0&-2\\0&1&0\\-2&0&1\end{pmatrix},
\tag{C33.4}
```

and

```math
\det Q_{\rm ind}=-2<0.
\tag{C33.5}
```

Since (Z) has full column rank, (M_{\rm ind}) has a negative direction. This
already disproves the sign-cone PSD claim, but some entries in (C33.3) vanish.

## Strict-sign and abstract-response version

Let (M_0) be the circulant matrix with diagonal (11), cyclic-neighbor entries
(-7), cyclic-distance-two entries (-1), and opposite entries (5). Explicitly,

```math
M_0=ZQ_0Z^{\mathsf T},qquad
Q_0=\begin{pmatrix}11&-7&-1\\-7&11&-7\\-1&-7&11\end{pmatrix}.
\tag{C33.6}
```

It annihilates (mathbf1,x,y), is positive semidefinite, and has strictly negative
entries on every nonmatching off-diagonal pair. Put

```math
M=M_{\rm ind}+\frac1{100}M_0.
\tag{C33.7}
```

Then (M_{ij}<0) for every (ij\notin H), while

```math
M=Z\left(Q_{\rm ind}+\frac1{100}Q_0\right)Z^{\mathsf T}
```

and

```math
\det\left(100Q_{\rm ind}+Q_0\right)
=-1920256<0.
\tag{C33.8}
```

So the strict-sign version remains indefinite.

To show that this is not merely a boundary artifact of the sign cone, let
(L_H) be the matching Laplacian with weight (1/3) on each edge and set

```math
\Lambda=L_H+\frac1{100}M.
\tag{C33.9}
```

Every off-diagonal entry of (Lambda) is strictly negative: on nonmatching pairs
this follows from (C33.7), and on matching pairs the corrections are smaller than
the base value (1/3). Also (Lambda\mathbf1=0), so (Lambda) is a connected
weighted graph Laplacian, and

```math
\Lambda P_B=L_HP_B
\tag{C33.10}
```

because (MP_B=0). But

```math
\Lambda-L_H=\frac1{100}M
```

is indefinite by (C33.8). This supplies an exact abstract response/Laplacian
regression with the affine identity and strict off-matching signs.

## The missing planar constraint is genuinely violated

The matrix in (C33.9) is not circular-planar either. In the standard positive
Laplacian convention used here, a circular-planar response must satisfy

```math
(-1)^k\det \Lambda[P;Q]\ge 0
\tag{C33.11}
```

for every circular pair `(P;Q)` of size `k`. This is the
Curtis--Ingerman--Morrow circular-minor characterization; an exact statement with
their opposite (negative-Laplacian) sign convention is recorded on p. 15 of the
[Alman--Lian--Tran response-matrix notes](https://web.mit.edu/clian/www/alman_electricalslides.pdf).
For the regular-hexagon cyclic order, `P=(0,1)` and `Q=(4,3)` form a circular pair,
because `0,1,3,4` occur in that order. Direct exact evaluation gives

```math
\det \Lambda[(0,1);(4,3)]
 =-\frac{21315229}{225000000}<0.
\tag{C33.12}
```

Here `k=2`, so the sign in (C33.11) is positive. Thus the regression is deliberately
outside the circular-planar response cone. This does not weaken (C33.8); it identifies
the precise extra hypothesis that a six-endpoint proof must exploit.

## Classification and precise limitation

**Regression, not a Target C counterexample.** The matrix (Lambda) in (C33.9) is
an abstract connected response Laplacian; the construction does not prove that it is
the Dirichlet response of a circular-planar positive unit-contact network with the
regular-hexagon geometry. It therefore does not disprove Erdős Problem #99 or the
six-endpoint matching response claim under all of Target C's hypotheses.

It does prove that C31-C32 cannot be extended to six endpoints using only:

1. the affine response kernel;
2. nonpositive off-diagonal entries away from the diameter matching; and
3. positivity of the matching weights.

Any successful six-endpoint theorem must explicitly use the circular-planar response
constraints, the actual unit-contact graph, stronger diameter geometry, or a new
global-minimality input.

## Compact handoff

```math
\boxed{
\text{six-endpoint matching: sign cone plus affine kernel }\not\Rightarrow
\text{ PSD response defect}.}
```

C30-C32 remain valid. The live six-endpoint problem is strictly narrower than this
regression: determine whether the additional circular-planar/unit-contact structure
rules out the exact algebraic negative mode, or exploit that mode directly in the
C-I separator argument.

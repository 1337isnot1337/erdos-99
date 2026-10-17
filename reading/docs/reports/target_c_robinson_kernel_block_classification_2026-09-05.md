> Generated reading edition · [exact source](../../../docs/reports/target_c_robinson_kernel_block_classification_2026-09-05.md) · source SHA-256 `d0bd74ce164a98029a18dc2a3a599b6ac778a9f492e467500c9d810a8ae8e9ac`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-53D803DA09B6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: C53 Robinson-kernel block classification

**Date:** 2026-09-05  
**Branch:** `research/target-c-c97-adjacent-cut-transition-2026-09-05`  
**Status:** LEVEL I STILL OPEN

## 1. Purpose

C53 proves that the selected-stress defect matrix is positive semidefinite by reducing it to the weighted Robinson equilibrium lemma C52.R. The live C54 question is the equality kernel. This note classifies that kernel at the level of the Robinson reduction.

The main point is exact:

> modulo constants, every kernel vector is piecewise affine in the strict edge-slope coordinate `t`; slope changes can occur only between disconnected blocks of an explicit first-difference Robinson matrix.

In particular, strict Robinson order gives no non-affine kernel at all.

## 2. Abstract setup

Let `L` be the C52.R matrix:

- `L=L^T`;
- `L 1=0`;
- for `i!=j`,

  `L_ij=-gamma_i gamma_j s_ij`,

  with every `gamma_i>0`;
- the similarities satisfy the Robinson inequalities

  `s_ik <= min(s_ij,s_jk)` for `i<j<k`;
- there is a strictly increasing vector

  `t_0<t_1<...<t_(q-1)`

  with `L t=0`.

C52.R proves `L>=0`.

Let `Gamma=diag(gamma_i)` and `G=sum_i gamma_i`. Let `D_1` be the `(q-1) x q` first-difference matrix

`(D_1 x)_i=x_(i+1)-x_i`,

and let `T_1` be the cumulative right inverse

`(T_1 y)_0=0`,

`(T_1 y)_r=sum_(h<r)y_h`.

Thus `D_1 T_1=I` and `T_1 D_1 x=x-x_0 1`.

## 3. Shift to a positive Robinson Laplacian

Choose `c>0` so that

`s'_ij=s_ij+c>0`

for every `i!=j`. Let

`L' = L + c(G Gamma-gamma gamma^T)`,

where `gamma=(gamma_i)`.

This is the positive complete weighted Laplacian associated with similarities `s'_ij`. On the weighted-mean-zero space

`gamma^T x=0`,

the generalized eigenvalues of `(L',Gamma)` are exactly those of `(L,Gamma)` shifted by `cG`.

Center `t` by

`t^0=t-(gamma^T t/G)1`.

Since `L t=0` and `gamma^T t^0=0`,

`L' t^0 = cG Gamma t^0`.                     (3.1)

Because `L>=0`, the smallest nonconstant generalized eigenvalue of `L'` is `cG`.

Define

`H=D_1 Gamma^(-1) L' T_1`.

Adding the constant `c` does not change the off-diagonal entries of `H`; exactly as in C52.R, for `k<i`,

`H_ik = - sum_(r<=k) gamma_r (s_(i r)-s_(i+1,r)) <=0`,     (3.2)

and for `k>i`,

`H_ik = sum_(r>k) gamma_r (s_(i r)-s_(i+1,r)) <=0`.       (3.3)

The nonconstant generalized spectrum of `(L',Gamma)` is exactly the spectrum of `H`.

Put

`delta=D_1 t`,

so every `delta_i>0`. From (3.1),

`H delta=cG delta`.                              (3.4)

There is also a strictly positive *left* eigenvector. Define

`eta_k = sum_(i>k) gamma_i t_i^0 = -sum_(i<=k) gamma_i t_i^0`.

Strict increase of `t^0` and weighted mean zero imply `eta_k>0` for every `k`. Moreover

`D_1^T eta=Gamma t^0`,

so

`eta^T H`
`=(D_1^T eta)^T Gamma^(-1)L'T_1`
`=(t^0)^T L'T_1`
`=cG (t^0)^T Gamma T_1`
`=cG eta^T`.                                    (3.5)

Thus the eigenvalue `cG` has positive right and left eigenvectors.

## 4. The Robinson gap graph

Define the graph `G_R` on the `q-1` gap indices `0,...,q-2` by joining `i` and `k` whenever

`H_ik<0` or `H_ki<0`.

The zero pattern does not depend on the shift `c`.

Choose `alpha` large enough that

`P=alpha I-H`

is entrywise nonnegative. Equations (3.4)-(3.5) give positive right and left Perron eigenvectors of `P` for the eigenvalue

`rho=alpha-cG`.

Scale by the positive right Perron vector `delta`:

`Q = rho^(-1) diag(delta)^(-1) P diag(delta)`.

Then `Q` is a finite row-stochastic matrix. Equation (3.5) gives a stationary distribution with strictly positive mass at every state. Therefore `Q` has no transient state. Its communicating classes are all closed, so after a simultaneous permutation `Q`, hence `P` and `H`, is block diagonal by the connected components of `G_R`.

Each irreducible block has Perron root `rho`, because the positive Perron eigenvector has nonzero restriction to every block.

Consequently the `cG` eigenspace of `H` has dimension exactly

`b=# components(G_R)`.                          (4.1)

Since `D_1` identifies vectors modulo constants with gap vectors, this gives the kernel dimension of `L`:

### Theorem RK1 — exact kernel dimension

`dim ker L = 1 + b`,                             (4.2)

where `b` is the number of connected components of the Robinson gap graph `G_R`.

## 5. Components are contiguous

The Robinson formulas (3.2)-(3.3) make the gap graph interval-convex.

For fixed `i`, if `k<i` and `H_ik<0`, then every `k'` with `k<=k'<i` also has `H_i,k'<0`, because (3.2) only adds further nonnegative Robinson differences as `k'` moves toward `i`.

Likewise, if `k>i` and `H_ik<0`, then every `k'` with `i<k'<=k` also has `H_i,k'<0`, because (3.3) only adds further nonpositive terms as `k'` moves toward `i`.

Therefore a connected component cannot skip over a gap index belonging to another component. The components of `G_R` are consecutive intervals

`I_1, I_2, ..., I_b`

in the natural gap order.

## 6. Piecewise-affine kernel classification

Let `x in ker L`. Center it by subtracting a constant. Then `y=D_1 x` lies in the `cG` eigenspace of `H`.

On each irreducible block `I_a`, Perron simplicity says that the `cG` eigenspace is one-dimensional and is spanned by the restriction of the positive vector `delta=D_1 t`. Hence there is a scalar `lambda_a` such that

`x_(i+1)-x_i = lambda_a (t_(i+1)-t_i)`

for every gap `i in I_a`.                       (6.1)

Integrating over each consecutive block proves:

### Theorem RK2 — piecewise-affine equality kernel

Every `x in ker L` is a continuous piecewise-affine function of the slope coordinate `t`, with one affine slope `lambda_a` on each component interval `I_a` of `G_R`.

Conversely, the kernel has one independent slope parameter per component, plus the global additive constant, exactly as (4.2) states.

Hence

`ker L = span{1,t}`

if and only if `G_R` is connected.              (6.2)

A non-affine kernel vector is possible **only** if the Robinson gap graph disconnects, and every non-affine degree of freedom is an exact slope break at one of those disconnections.

## 7. Strict Robinson corollary

Assume the stronger inequalities

`s_ik < min(s_ij,s_jk)`

for every `i<j<k`.

Then every summand in (3.2) and (3.3) is strict, so every off-diagonal entry of `H` is negative. Thus `G_R` is connected (indeed complete), and RK2 gives

### Corollary RK3 — strict Robinson rigidity

`ker L = span{1,t}`.                             (7.1)

So C53 can have a genuinely non-affine equality mode only through exact saturation of the circular-planar Robinson inequalities.

## 8. What a block boundary forces in K

This is already more than a spectral statement. Suppose a block boundary separates gap indices `h` and `h+1`.

Because there is no `H` coupling across components, every cross-block entry vanishes. For example

`H_(h,h+1)=sum_(r>h+1) gamma_r (s_(h r)-s_(h+1,r))=0`.

Each summand is nonpositive by Robinson order, so

`s_(h r)=s_(h+1,r)` for every `r>=h+2`.          (8.1)

Similarly

`s_(r,h+1)=s_(r,h+2)` for every `r<=h`.          (8.2)

Iterating across all gap indices in the two adjacent components propagates rectangular plateaux in the Robinson similarity matrix.

In the C53 application `s_ij=K_ij`, and each Robinson difference is itself a nonnegative Kalmanson-split sum with a fixed sign. Therefore equality in (8.1)-(8.2) is termwise: every positive interval-split coefficient must have zero signed contribution to the corresponding difference.

This is the exact circular-planar degeneracy that the remaining C54 separator step has to interpret.

## 9. C53 consequence

Apply RK1-RK3 to the C53 edge-space matrix `M`, ordered by projective diameter direction.

- If its Robinson gap graph is connected, the only edge-space equality modes are the two affine modes `1,t` already forced by the coordinate columns.
- Every extra C53 kernel mode forces one or more exact projective-direction cuts where the Kalmanson response matrix develops the plateau identities (8.1)-(8.2).
- The number of extra kernel dimensions is exactly the number of Robinson slope blocks minus one.

Thus the C54 problem is reduced from an arbitrary PSD-kernel classification to an exact equality-to-separator problem for these response plateaux.

The next step is to translate one plateau boundary into vanishing circular minors / a terminal separator in the positive contact network. This note does **not** claim that translation yet.

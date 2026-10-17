> Generated reading edition · [exact source](../../../docs/reports/target_c_general_matching_contraction_audit_2026-08-31.md) · source SHA-256 `bc7eef599ea2243754ab3fdf546b157e8e1a178464155de9b661dbed319cb8a6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-60AE6CBF3358","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C general matching contraction audit

**Date:** 2026-08-31  
**Repository state:** post-C51 mainline, research branch `research/target-c-general-matching-audit-2026-08-31`  
**Run type:** falsification / exact regression / computational theorem search  
**Target:** Target C selected-stress response, beyond C51  
**Computation:** exact rational regression plus optional floating-point linear programming  

## LEVEL I STATUS

`STILL OPEN`.

This report does **not** promote a new response theorem.  It identifies a plausible
all-support extension of C51, stress-tests it through seven opposite pairs, and kills
a tempting but false proof simplification with an exact rational witness.

## 1. Candidate theorem suggested by C51

For `m>=3`, take `2m` strictly convex cyclic terminals and the opposite matching

$$
H=\{\,i(i+m):0\le i<m\,\}.
$$

Let `Q` be the matching incidence matrix, `B=diag(beta_i)>0`, `Lambda` a connected
circular-planar response, `R=Lambda^+`, and

$$
K=Q^T RQ.
$$

Write the directed opposite chords as

$$
u_i=a_i(1,t_i),\qquad a_i>0,\qquad t_0<t_1<\cdots<t_{m-1},
$$

after the same affine normalization used in C51.  The C11 affine identity is

$$
KBU=U.
$$

Forcey's Kalmanson split representation implies

$$
K=\sum_I \lambda_I z_Iz_I^T,\qquad \lambda_I\ge0,
$$

where

$$
(z_I)_i=1_I(i)-1_I(i+m)
$$

for cyclic intervals `I` of the `2m` boundary order.

C51 proves, for `m=4`,

$$
B^{-1}-K\succeq0.
$$

The natural scalable candidate is:

> **GM conjecture.** Under the displayed split-cone, ordered-chord, and affine
> identity hypotheses, `B^{-1}-K` is positive semidefinite for every `m>=3`.

If true, this would remove the support-size obstruction for every selected positive
diameter stress whose support is a convex crossing matching.  It would still require a
kernel/strictness analysis and would not by itself solve direction-dependent KKT
support selection.

## 2. Computational search

The accompanying script

`research/target_c_matching_contraction_audit.py`

constructs every unique interval-difference vector `z_I` for the paired `2m` order.
For randomized positive ordered chord scales and positive `beta`, it solves the exact
linear affine constraints in floating point as a nonnegative LP in the split weights.
For sampled vectors `x` orthogonal to the two affine columns of `B^(1/2)U`, it then
solves the LP

$$
\max\;x^T B^{1/2}KB^{1/2}x
$$

subject to those same affine constraints.

Runs for `m=4,5,6,7`, including arbitrary unequal scale factors, repeatedly reached
the threshold `1` but produced no sampled value above `1` (up to numerical tolerance).
The identity split solution shows why equality at `1` is not itself suspicious.

This is **computational evidence only**.  The objective with the top eigenvalue is not
a linear program, and finitely many sampled directions do not prove the GM conjecture.
A single certified value above `1` would falsify it.

## 3. Exact regression against the naive slope-Laplacian proof

A tempting route is to pass to the ordered slopes `t_i`, use the affine kernel, and try
to show that the contraction defect is a one-dimensional Laplacian with every
long-range cross-cut coupling nonpositive.  That claim is false even inside the exact
abstract C51 hypotheses.

Take `m=5` with

$$
t=(0,1,4,7,8),\qquad
a=(4,1,2,1,2),\qquad
\beta=(1,2,4,2,4).
$$

Put `gamma_i=a_i beta_i`.  Use the following positive interval-difference split
weights:

| `z` | `lambda_z` |
| --- | ---: |
| `(1,0,0,0,0)` | `43/55` |
| `(1,1,0,0,0)` | `483/48880` |
| `(1,1,1,0,0)` | `3/47` |
| `(0,0,1,1,1)` | `24489/537680` |
| `(0,0,0,0,1)` | `11/80` |
| `(1,0,-1,-1,-1)` | `1/110` |
| `(1,1,-1,-1,-1)` | `457/97760` |
| `(1,1,1,-1,-1)` | `5/376` |
| `(1,1,1,1,-1)` | `1/160` |

Define

$$
K=\sum_z\lambda_z zz^T.
$$

Direct exact arithmetic gives

$$
KBU=U.
$$

However the rectangular transformed coupling across the two separated slope cuts
`k=2`, `l=3` is

$$
\sum_{i\le2,\ j\ge4}\gamma_i\gamma_j K_{ij}
=\frac{36672}{33605}>0.
$$

So the desired proof cannot consist of showing every such rectangular coupling is
nonpositive and then interpreting the slope energy as an ordinary graph Laplacian.

Crucially, the contraction still holds in this witness.  Let

$$
N=B-BKB,
\qquad E=diag(a_i),
$$

and use the local affine-annihilator matrix

$$
C=
\begin{pmatrix}
3&0&0\\
-4&3&0\\
1&-6&1\\
0&3&-4\\
0&0&3
\end{pmatrix}.
$$

Exact calculation gives

$$
ENE=CGC^T
$$

with

$$
G=
\begin{pmatrix}
59767/302445&64033/362934&35824/302445\\
64033/362934&3243199/10888020&182368/907335\\
35824/302445&182368/907335&72352/302445
\end{pmatrix}.
$$

The leading principal minors are

$$
\frac{59767}{302445},\qquad
\frac{29036}{1046925},\qquad
\frac{64}{22275},
$$

all strictly positive.  Hence `G` is positive definite and `N` is positive semidefinite
with exactly the two affine kernel directions.  This is an exact regression: the
simple cross-cut sign route fails while the stronger contraction survives.

## 4. What the regression says about the proof shape

The local three-point affine annihilators used above are the natural generalization of
the two columns in C51.  For general `m`, let `C_0` have column `r` supported on
`r,r+1,r+2` with coefficients

$$
(t_{r+2}-t_{r+1}),\quad
-(t_{r+2}-t_r),\quad
(t_{r+1}-t_r).
$$

For the scaled defect

$$
M=E(B-BKB)E,
$$

the affine identity gives `M 1=M t=0`, hence uniquely

$$
M=C_0 G C_0^T
$$

for a symmetric `(m-2)x(m-2)` Gale matrix `G`.

C51 is exactly the `2x2` instance of proving `G>=0`.  The audit above shows that for
`m=5` the `3x3` matrix can remain positive despite positive long-range slope
couplings.  The scalable problem is therefore not entrywise sign control.  It is to
find a **matrix-valued Kalmanson/planar-dual certificate for `G>=0`**.

The most promising next mechanisms are:

1. express `G` directly as a Gram/covariance matrix of the circular split weights;
2. use the planar dual network underlying the Kalmanson split system to identify the
   contraction defect as a genuine dual Dirichlet energy; or
3. prove an oscillation/total-positivity theorem for the generalized eigenproblem
   `KBx=lambda x`, where the two ordered affine chord fields already occupy the
   threshold eigenvalue `1`.

The first two are preferable because they could preserve exact electrical hypotheses
and make strictness/kernel analysis accessible.

## 5. Scope and claim classification

| Claim | Classification | Reason |
| --- | --- | --- |
| `m=4` contraction | proved previously | C51. |
| GM contraction for arbitrary `m` | conjectural route | no proof in this report. |
| no sampled violation through `m=7` | computational evidence | floating LP plus sampled directions. |
| all cross-cut slope couplings are nonpositive | rejected | exact rational `m=5` witness above. |
| exact witness still has PSD defect | proved regression | explicit `C G C^T` factorization with `G>0`. |
| Target C / Level I closed | not proved | C-I support selection and C-II remain open. |

## 6. Reproduction

```sh
python3 research/target_c_matching_contraction_audit.py
python3 research/target_c_matching_contraction_audit.py --scan
```

The first command is standard-library exact arithmetic.  The optional scan requires
NumPy and SciPy.

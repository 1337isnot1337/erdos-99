<!-- theorem-state: {"artifact_id":"ART-8333BC47C6A1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: arbitrary matching response contraction

**Date:** 2026-08-31  
**Repository base:** `b1b646c` (main after C51)  
**Run type:** exact response inequality / selected-stress closure  
**Target:** C-I selected positive-diameter matching supports  
**Depends on:** C11 affine response, C30 Schur reduction, C50 Kalmanson split cone, C51 opposite-chord setup

## LEVEL I STATUS

**STILL OPEN.**

This report removes the finite-size restriction in C51. Every selected positive
diameter support that is a matching, of arbitrary cardinality, has nonnegative
Schur defect. The proof does not assume equal chord lengths, equal KKT weights,
a regular polygon, or a bounded number of terminals.

The new ingredient is a weighted Robinson/Fiedler lemma. The circular Kalmanson
split cone orders the opposite-pair resistance block as a Robinson similarity.
The affine response identity supplies two exact zero modes, the constant mode and
the strictly ordered opposite-chord slope mode. A Robinson weighted Laplacian
cannot have a negative mode while those two modes are present.

This is still a selected-support theorem. It does not prove that the
velocity-dependent second-order KKT multiplier has matching support, and it does
not close the C-I diameter-shear separator or the fully force-visible C-II branch.

## 1. Theorem C52

### Theorem C52 (arbitrary opposite-matching response contraction)

Let `q>=2`, and let

\[
p_0,p_1,\ldots,p_{2q-1}
\]

be distinct vertices in strict convex cyclic order. Pair them by

\[
H=\{\,i(i+q):0\le i<q\,\}.
\]

Put

\[
q_i=e_i-e_{i+q},\qquad
Q=(q_0\ \cdots\ q_{q-1}),\qquad
B=\operatorname{diag}(\beta_0,\ldots,\beta_{q-1}),
\]

with every `beta_i>0`, and define

\[
L_H=QBQ^{\mathsf T}.
\]

Translate the coordinate matrix `P` so that
`1^T P=0`, and put

\[
U=Q^{\mathsf T}P.
\]

Thus row `i` of `U` is the directed opposite chord

\[
u_i=p_i-p_{i+q}.
\]

Let `Lambda` be the Dirichlet response of a connected circular-planar
positive-conductance network on these `2q` terminals, let

\[
R=\Lambda^+,
\qquad
W_{ab}=R_{aa}+R_{bb}-2R_{ab},
\]

and assume the C11 affine response identity

\[
\Lambda P=L_HP.
\tag{C52.1}
\]

Assume, equivalently to the circular-planar input already used in C50-C51,
that `W` lies in the Kalmanson cone for this cyclic terminal order. Set

\[
K=Q^{\mathsf T}RQ.
\]

Then

\[
\boxed{B^{-1}-K\succeq0.}
\tag{C52.2}
\]

Consequently

\[
\boxed{\Lambda-L_H\succeq0\quad\text{on }\mathbf1^\perp.}
\tag{C52.3}
\]

In the selected-stress C30 setting, if `L_C(alpha)` is the positive-contact
Laplacian whose Kron response is `Lambda`, then

\[
\boxed{L_C(\alpha)-L_H(\beta)\succeq0.}
\tag{C52.4}
\]

Because distinct diameter edges in the plane intersect, every selected positive
diameter support with maximum degree one is, after cyclic relabeling of its
strictly convex endpoints, exactly the opposite matching above. Hence C52 closes
**every selected positive-diameter matching support, with no bound on its size**.

## 2. Ordered opposite-chord coordinates

For `0<=i<j<q`, the four vertices

\[
p_i,p_j,p_{i+q},p_{j+q}
\]

occur in this cyclic order and form a strict convex quadrilateral. The directed
diagonals `u_i=p_i-p_{i+q}` and `u_j=p_j-p_{j+q}` therefore have a common strict
orientation. After choosing the orientation once,

\[
\det(u_i,u_j)>0\qquad(i<j).
\tag{C52.5}
\]

Thus all `u_i` lie in one open half-plane and occur there in strict angular order.
Choose covectors `ell,m` with `ell(u_i)>0` for every `i`, orient `(ell,m)`
consistently with (C52.5), and write

\[
a_i=\ell(u_i)>0,
\qquad
t_i=\frac{m(u_i)}{\ell(u_i)}.
\]

Then

\[
t_0<t_1<\cdots<t_{q-1},
\qquad
u_i=a_i(1,t_i)
\tag{C52.6}
\]

in these affine coordinates. With

\[
E=\operatorname{diag}(a_0,\ldots,a_{q-1}),
\qquad
V=\begin{pmatrix}1&t_0\\\vdots&\vdots\\1&t_{q-1}\end{pmatrix},
\]

we have `U=EV`.

The centered affine response identity gives, exactly as in C50-C51,

\[
KBU=U.
\tag{C52.7}
\]

Indeed `R Lambda P=P` on centered coordinate columns, so
`RQB U=P`, and premultiplication by `Q^T` gives (C52.7).

Define

\[
N=B-BKB,
\qquad
M=ENE,
\qquad
\gamma_i=a_i\beta_i>0,
\qquad
\Gamma=\operatorname{diag}(\gamma_i).
\tag{C52.8}
\]

Equation (C52.7) gives `NU=0`, hence

\[
M\mathbf1=0,
\qquad
Mt=0,
\qquad
t=(t_0,\ldots,t_{q-1})^{\mathsf T}.
\tag{C52.9}
\]

For `i!=j`,

\[
M_{ij}=a_ia_jN_{ij}
       =-a_i\beta_i\,a_j\beta_jK_{ij}
       =-\gamma_i\gamma_jK_{ij}.
\tag{C52.10}
\]

Thus the response problem has become a weighted Laplacian problem. It remains to
use circular planarity to control the order structure of the similarities `K_ij`.

## 3. Kalmanson splits force a Robinson similarity

Use the promoted C50 Kalmanson-cone decomposition. Modulo a sum matrix, which is
annihilated by `Q^T(\cdot)Q`, the effective-resistance matrix is a nonnegative
combination of circular interval cut metrics. For one circular interval `A`, put

\[
z_i=\mathbf1_A(i)-\mathbf1_A(i+q).
\tag{C52.11}
\]

Its contribution to `K=Q^T RQ` is `z z^T`.

Fix `i<j<k`. The six points

\[
i,j,k,i+q,j+q,k+q
\]

occur in this cyclic order. Restricting a circular interval indicator to these six
points still gives a circular consecutive-ones pattern. Up to complement, hence up
to the harmless global sign `z -> -z`, the possible triples
`(z_i,z_j,z_k)` are

\[
000,\ 001,\ 010,\ 011,\ 100,\ 110,\ 111,\
1\bar1\bar1,\ 10\bar1,\ 11\bar1,
\tag{C52.12}
\]

where `bar1=-1`. Directly in this ten-case list,

\[
z_k(z_i-z_j)\le0,
\qquad
z_i(z_k-z_j)\le0.
\tag{C52.13}
\]

Summing (C52.13) over the nonnegative interval-split coefficients gives

\[
K_{ik}-K_{jk}\le0,
\qquad
K_{ik}-K_{ij}\le0.
\]

Therefore

\[
\boxed{K_{ik}\le\min(K_{ij},K_{jk})
       \qquad(i<j<k).}
\tag{C52.14}
\]

So the off-diagonal matrix `K_ij` is a Robinson similarity in the strict slope
order (C52.6).

## 4. Weighted Robinson equilibrium lemma

The remaining statement is purely linear algebra.

### Lemma C52.R (weighted Robinson equilibrium is PSD)

Let `s_ij=s_ji` for `i!=j` satisfy

\[
s_{ik}\le\min(s_{ij},s_{jk})\qquad(i<j<k).
\tag{C52.R1}
\]

Let `gamma_i>0`, and let `L` be the symmetric matrix with

\[
L_{ij}=-\gamma_i\gamma_js_{ij}\quad(i\ne j),
\qquad
L\mathbf1=0.
\tag{C52.R2}
\]

If there is a strictly increasing vector

\[
t_0<t_1<\cdots<t_{q-1}
\]

such that

\[
Lt=0,
\tag{C52.R3}
\]

then

\[
\boxed{L\succeq0.}
\tag{C52.R4}
\]

#### Proof

We first prove the weighted Fiedler fact needed below.

Suppose temporarily that every `s_ij>0`. Then `L` is the Laplacian of a complete
positive weighted graph with edge weights `gamma_i gamma_j s_ij`. Put

\[
A=\Gamma^{-1}L.
\]

The generalized eigenvalues of `(L,Gamma)` are the eigenvalues of `A`; they are
real because `A` is similar to the symmetric matrix
`Gamma^{-1/2} L Gamma^{-1/2}`. Write them as

\[
0=\lambda_1<\lambda_2\le\cdots\le\lambda_q.
\]

Let `D` be the `(q-1) x q` first-difference matrix,

\[
(Dx)_i=x_{i+1}-x_i,
\]

and let `T` be the `q x (q-1)` cumulative matrix

\[
(Ty)_0=0,
\qquad
(Ty)_r=\sum_{h<r}y_h.
\]

Then

\[
DT=I,
\qquad
TDx=x-x_0\mathbf1.
\tag{C52.R5}
\]

Set

\[
H=DAT.
\tag{C52.R6}
\]

Because `A1=0`, the spectrum of `H` is exactly
`lambda_2,...,lambda_q`. For completeness: if `Ax=lambda x` with
`lambda!=0`, then `y=Dx!=0` and `Hy=lambda y`; conversely, if
`Hy=lambda y`, then `x=Ty` satisfies
`D(Ax-lambda x)=0`, so adding a constant to `x` gives an eigenvector of `A`
with eigenvalue `lambda`.

The Robinson inequalities make every off-diagonal entry of `H` nonpositive.
Indeed, for `k<i`, use the zero row sums of `A` to obtain

\[
H_{ik}
=-\sum_{r\le k}\gamma_r(s_{ir}-s_{i+1,r})\le0,
\tag{C52.R7}
\]

because `r<i<i+1` implies `s_{r,i+1}<=s_{r,i}`. For `k>i`,

\[
H_{ik}
=\sum_{r>k}\gamma_r(s_{ir}-s_{i+1,r})\le0,
\tag{C52.R8}
\]

because `i<i+1<r` implies `s_{i,r}<=s_{i+1,r}`.

Choose `alpha` so large that `alpha I-H` is entrywise nonnegative and
`alpha>=lambda_q`. Its eigenvalues are
`alpha-lambda_2,...,alpha-lambda_q`, all nonnegative, so its spectral radius is
`alpha-lambda_2`. Perron-Frobenius gives an eigenvector `y>=0` for that
spectral radius. Hence `Hy=lambda_2 y`. Reconstructing the corresponding
`A`-eigenvector `x` as above gives

\[
Dx=y\ge0.
\]

Thus the smallest positive generalized eigenvalue has a nonconstant
**nondecreasing** eigenvector `x`.

Now return to possibly signed Robinson similarities and suppose, for contradiction,
that `L` is not positive semidefinite. Since `L1=0`, the generalized Rayleigh
quotient on the weighted-mean-zero space

\[
\gamma^{\mathsf T}x=0
\]

has a negative minimum `lambda_*<0`.

Let

\[
G=\sum_i\gamma_i.
\]

Choose `c>0` large enough that

\[
s'_{ij}=s_{ij}+c>0\quad(i\ne j)
\]

and `cG+lambda_*>0`. Adding the same constant preserves the Robinson
inequalities. The corresponding weighted Laplacian is

\[
L'=L+c(G\Gamma-\gamma\gamma^{\mathsf T}).
\tag{C52.R9}
\]

On `gamma^T x=0`, all generalized eigenvalues are shifted by exactly `cG`.
Therefore the smallest positive generalized eigenvalue of `(L',Gamma)` is

\[
\lambda_2'=cG+\lambda_*<cG.
\tag{C52.R10}
\]

The weighted Fiedler argument above supplies a nonconstant nondecreasing eigenvector
`x` for `lambda_2'`. Since `lambda_2'>0`, it is weighted-orthogonal to the
constant kernel:

\[
\sum_i\gamma_i x_i=0.
\tag{C52.R11}
\]

Center the strictly increasing vector `t` by

\[
t^0=t-\frac{\sum_i\gamma_i t_i}{G}\mathbf1.
\]

Equations (C52.R3) and (C52.R9) give

\[
L't^0=cG\,\Gamma t^0.
\tag{C52.R12}
\]

The generalized eigenvalues in (C52.R10) and (C52.R12) are distinct. Symmetry of
`L'` therefore gives generalized orthogonality,

\[
\sum_i\gamma_i x_i t_i=0.
\tag{C52.R13}
\]

But the weighted covariance identity and (C52.R11) give

\[
\sum_i\gamma_i x_i t_i
=\frac1{2G}\sum_{i,j}\gamma_i\gamma_j
 (x_i-x_j)(t_i-t_j).
\tag{C52.R14}
\]

Every term on the right is nonnegative because both sequences are nondecreasing,
and at least one is strictly positive because `x` is nonconstant and `t` is strictly
increasing. Hence the right side of (C52.R14) is positive, contradicting
(C52.R13). Therefore `L` has no negative generalized eigenvalue and
`L>=0`. This proves C52.R. `square`

## 5. Completion of C52

Apply C52.R to `L=M`, `s_ij=K_ij`, and the positive weights `gamma_i` from
(C52.8). Equations (C52.9), (C52.10), and the Robinson inequalities (C52.14)
verify every hypothesis. Hence

\[
M\succeq0.
\]

Because `E` is positive diagonal,

\[
N=E^{-1}ME^{-1}\succeq0.
\]

Finally

\[
B^{-1}-K
=B^{-1}NB^{-1}\succeq0,
\]

which is (C52.2).

Let `Y=R^{1/2}QB^{1/2}` on `1^perp`. Then

\[
Y^{\mathsf T}Y=B^{1/2}KB^{1/2}\preceq I.
\]

Hence `YY^T<=I`, i.e.

\[
R^{1/2}L_HR^{1/2}\preceq I.
\]

On `1^perp`, `R=Lambda^{-1}`, so congruence gives
`L_H<=Lambda`, proving (C52.3). The positive interior contact block in the
usual C30 Kron/Schur decomposition is positive definite, and its Schur complement
is `Lambda-L_H`; therefore (C52.4) follows. `square`

## 6. Exact effect on Target C

Before C52, the selected response audit was finite:

- all three-edge forests were closed by C31-C32/C50;
- the four-edge eight-terminal opposite matching was closed by C51.

C52 removes the cardinality parameter completely:

\[
\boxed{
\text{selected positive diameter support is a matching}
\Longrightarrow
L_C(\alpha)-L_H(\beta)\succeq0.}
\tag{C52.15}
\]

Thus an arbitrarily large matching cannot furnish the negative response/Schur mode
needed to evade the affine contact response.

The obstruction left after C52 is no longer “larger matching support.” Any surviving
selected support must use a positive-diameter vertex of degree at least two, or the
C-I failure must come from the support-selection/finite-integration issue itself.
That is a materially smaller combinatorial target because shared-endpoint diameter
edges are simultaneously constrained by the global shared-endpoint angle bound.

## 7. Shortest remaining lemma

A direct next target is:

> **C53 shared-endpoint reduction.** For a selected positive diameter thrackle on
> the force-hull boundary satisfying the same C11 affine response identity, either
> its Schur defect is positive semidefinite, or a vertex incident to at least two
> positive diameter edges carries a negative mode that can be converted into the C9
> common-angular-rate release or contradicted by the global shared-endpoint angle
> bound.

Equivalently, after C52 the only response topology that still needs a genuinely new
matrix argument is one with shared diameter endpoints. Decomposing such a support
into matching color classes is not enough, because the affine identity
`Lambda P=L_H P` belongs to the total support and does not hold separately on the
color classes.

## 8. Regressions and no-go statements

C52 does **not** justify any of the following:

- a general Loewner comparison for arbitrary positive diameter graphs;
- decomposition of an arbitrary support into independently affine matching blocks;
- maximality of the velocity-dependent second-order KKT support;
- a finite same-diameter release from semidefiniteness alone;
- a uniform positive response gap;
- any claim that contact-isolated source points are negligible.

The near-star strict-minor regression remains binding in C-II. The C52 proof escapes
it only because the matching affine identity supplies the exact increasing zero mode;
it does not produce quantitative minor mass.

## 9. Verification

The proof was audited in three independent ways before promotion:

1. the six-point interval restriction was enumerated exactly, yielding the ten
   sign patterns in (C52.12);
2. the weighted Fiedler transform was checked symbolically at the formula level:
   the off-diagonal entries are exactly (C52.R7)-(C52.R8), so no unweighted
   assumption is hidden in the argument;
3. random linear-program falsification tests for `q=5,6,7`, unequal chord scales,
   unequal positive weights, and random increasing slopes found the sharp maximum
   contraction eigenvalue `1` to numerical precision. These tests are evidence only;
   the proof above is exact and does not depend on them.

## 10. Compact handoff

**LEVEL I STATUS:** still open.

**New theorem:** C52 proves full response contraction for every selected positive
diameter matching, with arbitrary size, weights, and strict convex geometry.

**Mechanism:** Kalmanson interval splits -> Robinson similarity; affine opposite-chord
coordinates -> constant plus strictly increasing zero modes; weighted Fiedler theorem
-> no negative defect mode.

**Next obstruction:** shared-endpoint positive diameter supports and the independent
C-I support-selection/finite-integration gap.

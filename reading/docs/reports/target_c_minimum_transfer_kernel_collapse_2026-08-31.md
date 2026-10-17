> Generated reading edition · [exact source](../../../docs/reports/target_c_minimum_transfer_kernel_collapse_2026-08-31.md) · source SHA-256 `72c20bc7ad6e2c602cc9b185907e16f46f4c906529d75bb3cc496ab2f45b2a89`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-9B296BE6BAF7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: minimum-transfer kernel collapse

**Date:** 2026-08-31  
**Repository base:** `466badfd` (main after C55 / PR #57)  
**Run type:** exact equality-kernel sharpening  
**Target:** Target C Gate C-I  
**Depends on:** C53 arbitrary-thrackle contraction, C54 universal PSD/null-face selection, C55 Robinson-kernel localization

## LEVEL I STATUS

**STILL OPEN.**

C55 allows the C53 difference-space kernel to decompose into several contiguous
Robinson blocks and localizes angular shear to singleton gap blocks. The decomposition
is in fact much more rigid.

For any two-dimensional selected KKT stress, let

```math
K=Q^{\mathsf T}\Lambda^+Q
```

be the C53 diameter-edge transfer kernel in strict projective direction order and put

```math
c=\min_{i\ne j}K_{ij}.
```

Then `c<=0`, and there are only two possibilities:

1. **generic phase `c<0`:** the entire C53 scalar edge kernel is exactly
   `span{1,t}`. Equivalently the C55 gap transform has one irreducible block. Any
   tangential diameter velocity in the full stress kernel has one common angular rate;
2. **zero-transfer phase `c=0`:** every off-diagonal transfer vanishes,
   `K=B^{-1}`, the C53 edge defect is identically zero, and the positive diameter
   graph is a forest. Every C55 gap is isolated simultaneously.

Thus the mixed C55 picture — a multi-gap block next to an isolated hinge — cannot
occur. A genuine selected-support shear forces the **global zero-transfer forest
phase**.

## 1. C53/C55 edge-space notation

Fix a normalized KKT stress `s=(alpha,beta)` whose positive diameter endpoints span
two dimensions. Orient its `m>=2` positive diameter edges by the C53 projective order

```math
e_0<e_1<\cdots<e_{m-1}
```

and write their directed chord vectors as

```math
u_i=a_i(1,t_i),
\qquad a_i>0,
\qquad t_0<t_1<\cdots<t_{m-1}.
\tag{C56.1}
```

Put

```math
B=\operatorname{diag}(\beta_i),
\qquad
\gamma_i=a_i\beta_i,
\qquad
\Gamma=\operatorname{diag}(\gamma_i),
\qquad
G=\sum_i\gamma_i.
\tag{C56.2}
```

C53 gives the Robinson inequalities

```math
K_{ik}\le\min(K_{ij},K_{jk})
\qquad(i<j<k)
\tag{C56.3}
```

and the scaled edge defect

```math
M=\Gamma(B^{-1}-K)\Gamma\succeq0,
\qquad
M\mathbf1=0,
\qquad
Mt=0.
\tag{C56.4}
```

For `i!=j`,

```math
M_{ij}=-\gamma_i\gamma_jK_{ij}.
\tag{C56.5}
```

C55 studies this kernel after first differences. C56 instead first subtracts the
minimum off-diagonal transfer.

## 2. Weighted Robinson Fiedler simplicity

The only new linear-algebra input is a weighted form of the classical simplicity
mechanism for an irreducible Robinson similarity. The proof is included because the
KKT weights `gamma_i` are arbitrary positive reals.

For a symmetric nonnegative similarity `A=(A_ij)` and positive `gamma`, define its
weighted Laplacian by

```math
(L_A)_{ij}=-\gamma_i\gamma_jA_{ij}\quad(i\ne j),
\qquad L_A\mathbf1=0.
\tag{C56.6}
```

Its generalized Fiedler value is

```math
\lambda_2(A,\gamma)
=
\min_{\gamma^{\mathsf T}x=0,\ x\ne0}
\frac{x^{\mathsf T}L_Ax}{x^{\mathsf T}\Gamma x}.
\tag{C56.7}
```

### Lemma C56.1 (weighted plateau propagation)

Let `A` be a nonnegative Robinson similarity and `x` a nondecreasing generalized
Fiedler vector. If `J=[r,s]` is a maximal constant interval of `x`, then

```math
A_{r,k}=A_{r+1,k}=\cdots=A_{s,k}
\qquad(k\notin J).
\tag{C56.8}
```

#### Proof

The generalized eigen-equation is

```math
\sum_j\gamma_jA_{ij}(x_i-x_j)=\lambda_2x_i.
\tag{C56.9}
```

Subtract the equations at `r` and `s`. Since `x_r=x_s`, the right side is zero and
all terms with indices in `J` vanish. Multiplying the resulting identity by `-1`
gives

```math
0=
\sum_{k<r}\gamma_k(A_{r,k}-A_{s,k})(x_r-x_k)
+
\sum_{k>s}\gamma_k(A_{s,k}-A_{r,k})(x_k-x_r).
\tag{C56.10}
```

Every term is nonnegative by Robinson monotonicity and monotonicity of `x`; maximality
of `J` makes every value difference in (C56.10) strict. Hence all similarity
differences vanish. Robinson monotonicity then fills in the intermediate rows.
$`\square`$

### Lemma C56.2 (weighted converse plateau lemma)

Let `A` be an irreducible nonnegative Robinson similarity whose minimum off-diagonal
entry is zero. Let `J=[r,s]` be a proper interval such that

```math
A_{r,k}=A_{s,k}
\qquad(k\notin J).
\tag{C56.11}
```

Then every generalized Fiedler vector is constant on `J`.

#### Proof

For every outside `k`, Robinson monotonicity makes `A_{i,k}` independent of `i in J`;
write the common value `a_k`. Put

```math
\alpha=A_{r,s}.
```

Irreducibility forces `alpha>0`: if `alpha=0`, Robinson monotonicity and (C56.11)
make every similarity from `J` to its complement zero.

Every off-diagonal similarity inside `J` is at least `alpha`. Define `B<=A` by setting
all off-diagonal entries inside `J` equal to `alpha`, leaving all other entries
unchanged. Put

```math
G_J=\sum_{i\in J}\gamma_i,
\qquad
C=\sum_{k\notin J}\gamma_k a_k,
\qquad
\mu=\alpha G_J+C.
\tag{C56.12}
```

The weighted space decomposes orthogonally into

```math
U=\{x:x_i\text{ is constant on }J\}
```

and

```math
W=\{x:\operatorname{supp}x\subseteq J,
\ \sum_{i\in J}\gamma_ix_i=0\}.
```

Both are invariant for the generalized `B`-Laplacian. For every `w in W`,

```math
L_Bw=\mu\Gamma w,
\tag{C56.13}
```

because

```math
\sum_{i<j\in J}\gamma_i\gamma_j(w_i-w_j)^2
=G_J\sum_{i\in J}\gamma_iw_i^2.
```

We show `lambda_2(B,gamma)<mu`.

Every outside value satisfies `a_k<=alpha`. If

```math
C<\alpha(G-G_J),
```

take the weighted-mean-zero vector which is `1` at any fixed `i in J` and constant
on its complement. Its Rayleigh quotient is

```math
R_i=
\frac{G[\alpha(G_J-\gamma_i)+C]}{G-\gamma_i}.
\tag{C56.14}
```

A direct calculation gives

```math
\mu-R_i
=
\frac{\gamma_i[\alpha(G-G_J)-C]}{G-\gamma_i}>0.
\tag{C56.15}
```

If instead `C=alpha(G-G_J)`, positivity of every `gamma_k` implies
`a_k=alpha` for every outside index. The zero minimum of a Robinson similarity occurs
at the extreme pair, so `A_{0,m-1}=0`. Hence the complement of `J` has nonempty
left and right parts; otherwise the extreme zero would be one of the `a_k`,
contradicting `alpha>0`.

Let their total weights be `G_L,G_R>0` and set

```math
x_i=
\begin{cases}
-G_R,&i<r,\\
0,&r\le i\le s,\\
G_L,&i>s.
\end{cases}
\tag{C56.16}
```

This vector has weighted mean zero. Pairs inside each of the three constant blocks
contribute no energy. All cross-block similarities are at most `alpha`, and the
extreme left-right pair has similarity `0<alpha`. Therefore its quotient is strictly
below that of the complete constant-`alpha` similarity, namely `alpha G=mu`.

Thus in both cases `lambda_2(B,gamma)<mu`. By (C56.13), every Fiedler vector of `B`
lies in `U` and is constant on `J`.

Finally `A>=B` and the matrices differ only inside `J`. A Fiedler vector of `B` is
constant there, so its energy is unchanged by restoring `A`. Hence
`lambda_2(A,gamma)=lambda_2(B,gamma)`. Any Fiedler vector of `A` has `B`-energy no
larger than that common minimum, so it is also a Fiedler vector of `B` and is constant
on `J`. $`\square`$

### Lemma C56.3 (strict weighted Robinson Fiedler vector is simple)

Let `A` be irreducible, nonnegative, Robinson, and have minimum off-diagonal value
zero. If `A` has a strictly increasing generalized Fiedler vector `t`, then its
Fiedler value is simple.

#### Proof

Assume there is another independent Fiedler vector `y`. Every

```math
z(\theta)=\cos\theta\,t+\sin\theta\,y
```

is a Fiedler vector. At `theta=0` all consecutive differences are positive, while at
`theta=pi` all are negative. At the first positive parameter where one consecutive
difference vanishes, `z(theta)` is nondecreasing and has a proper constant interval
`J`. Lemma C56.1 gives equal endpoint similarities outside `J`, and Lemma C56.2 says
every Fiedler vector, including the strictly increasing `t`, is constant on `J`.
Contradiction. $`\square`$

This is the arbitrary-positive-vertex-weight version of the simplicity mechanism in
Atkins, Boman, and Hendrickson, *A Spectral Algorithm for Seriation and the
Consecutive Ones Problem*, SIAM J. Comput. 28(1), 297–310 (1998), Theorem 4.6,
DOI `10.1137/S0097539795285771`. The weighted proof above is self-contained.

## 3. Minimum-transfer dichotomy

### Theorem C56 (minimum-transfer kernel collapse)

Let `K,M,t,gamma` satisfy the C53 identities (C56.1)-(C56.5), and define

```math
c=\min_{i\ne j}K_{ij}.
\tag{C56.17}
```

Then `c<=0`. Exactly one of the following holds.

#### C56-G: `c<0`

```math
\boxed{
\ker M=\operatorname{span}\{\mathbf1,t\}.
}
\tag{C56.18}
```

In particular the C55 difference-space transform has a one-dimensional kernel and
therefore exactly one irreducible gap block.

#### C56-Z: `c=0`

```math
\boxed{
K_{ij}=0\quad(i\ne j),
\qquad
K=B^{-1},
\qquad
M=0.
}
\tag{C56.19}
```

Every C55 gap is isolated simultaneously.

#### Proof

Shift the off-diagonal similarity by its minimum:

```math
A_{ij}=K_{ij}-c
\qquad(i\ne j).
\tag{C56.20}
```

Then `A` is a nonnegative Robinson similarity with minimum off-diagonal value zero.
Let `L_A` be its weighted Laplacian in weights `gamma`. Adding a constant similarity
to all off-diagonal entries gives the exact identity

```math
L_A=M-c(G\Gamma-\gamma\gamma^{\mathsf T}).
\tag{C56.21}
```

Center the strict slope vector in weighted mean,

```math
t^0=t-\frac{\gamma^{\mathsf T}t}{G}\mathbf1.
```

Using `Mt=0`,

```math
L_A t^0=-cG\Gamma t^0.
\tag{C56.22}
```

Because `A` is nonnegative, `L_A` is PSD. Since `t^0` is nonzero, (C56.22) implies
`c<=0`.

If `c=0`, then `A=K` off the diagonal and

```math
0=(t^0)^{\mathsf T}L_A t^0
=
\sum_{i<j}\gamma_i\gamma_jK_{ij}(t_i-t_j)^2.
\tag{C56.23}
```

All summands are nonnegative and every slope difference is nonzero. Thus every
off-diagonal `K_ij=0`. Equation (C56.5) plus zero row sums gives `M=0`. Since

```math
M=\Gamma(B^{-1}-K)\Gamma
```

and `Gamma` is invertible, `K=B^{-1}`. This is C56-Z.

Now suppose `c<0`. On the weighted-mean-zero subspace, C53 positivity gives

```math
x^{\mathsf T}L_Ax
=x^{\mathsf T}Mx-cGx^{\mathsf T}\Gamma x
\ge -cGx^{\mathsf T}\Gamma x.
\tag{C56.24}
```

The vector `t^0` attains equality by (C56.22), so

```math
\lambda_2(A,\gamma)=-cG>0.
\tag{C56.25}
```

Therefore `A` is irreducible. Its Fiedler vector `t^0` is strictly increasing, so
Lemma C56.3 makes the eigenspace at (C56.25) one-dimensional.

For `x in ker M`, subtract its weighted mean to obtain `x^0`. Equation (C56.21) gives

```math
L_Ax^0=-cG\Gamma x^0,
```

so `x^0` is a multiple of `t^0`. Hence (C56.18). $`\square`$

### Corollary C56.4 (mixed C55 blocks are impossible)

The C55 gap transform has either

1. one irreducible block containing every gap (`c<0`), or
2. no off-diagonal coupling at all, so every gap is a singleton (`c=0`).

There is no decomposition with both a nontrivial block and an isolated gap.

This follows because C55.1 identifies the number of gap blocks with the dimension of
`ker M` modulo constants. In C56-G that quotient kernel is one-dimensional; in
C56-Z, `M=0`.

## 4. Angular consequence

### Corollary C56.5 (nonzero minimum transfer kills selected-support shear)

Let a fixed-diameter critical velocity lie in the full selected stress kernel as in
C55. Then

```math
\omega\in\ker M,
\qquad
t\odot\omega\in\ker M.
\tag{C56.26}
```

If `c<0`, Theorem C56 gives

```math
\omega=a+bt,
\qquad
t\omega=a'+b't.
```

The second identity says

```math
b t_i^2+(a-b')t_i-a'=0
```

at every selected diameter slope. The branch `c<0` cannot occur for only two edges:
then the shifted similarity `A` would have its sole off-diagonal entry zero and could
not have positive Fiedler value (C56.25). Hence there are at least three distinct
`t_i`, forcing `b=0`. Therefore

```math
\boxed{
\omega_0=\omega_1=\cdots=\omega_{m-1}.
}
\tag{C56.27}
```

So a selected null-face stress can carry genuine diameter shear only in C56-Z.

## 5. Structure of the zero-transfer phase

### Corollary C56.6 (zero-transfer diameter graph is a forest)

In C56-Z,

```math
K=Q^{\mathsf T}\Lambda^+Q=B^{-1}\succ0.
```

Hence `Q` has independent columns. Incidence-matrix columns are independent exactly
for a forest, so

```math
\boxed{H_s\text{ is a forest}.}
\tag{C56.28}
```

Since `H_s` is also a geometric convex thrackle, each component has the usual
caterpillar form.

### Corollary C56.7 (all positive Kalmanson splits are direction-local)

In C56-Z every C55 gap is isolated. Apply C55.3 at every adjacent pair. If a positive
Kalmanson interval split vector `z` changes between coordinates `i,i+1`, then

```math
\operatorname{supp}z\subseteq\{i,i+1\}.
\tag{C56.29}
```

For `m>=3`, a nonzero split vector constant in all edge coordinates would contribute
a positive amount to `K_{0,m-1}`. No split supported on an adjacent pair can affect
that nonadjacent entry, while C56-Z has `K_{0,m-1}=0`. Hence no such constant split
occurs with positive coefficient. Therefore every positive split vector satisfies

```math
\boxed{
|\operatorname{supp}z|\le2,
\quad\text{and if }|\operatorname{supp}z|=2,
\text{ the two coordinates are adjacent in projective edge order}.}
\tag{C56.30}
```

For `m=2` the same conclusion is tautological.

Thus the remaining electrical equality is not an arbitrary star-like response. Its
entire Kalmanson split measure is local to one diameter edge or one adjacent pair of
diameter directions.

## 6. Exact effect on Gate C-I

C54 supplies an exposed null face of the normalized KKT polytope annihilating the
entire strong-framework flex space. C55 localizes a possible shear to isolated gaps.
C56 collapses that localization to a global alternative:

```text
null-face selected stress s
    -> two-dimensional support ?
       yes -> C53 PSD and C56
              c<0 -> selected angular rate is common
              c=0 -> M=0, K=B^{-1}, diameter support is a forest,
                     every positive Kalmanson split is one-edge/two-adjacent-edge local
       no  -> C54.1 straight-chain selected support
```

Therefore a weak-contact diameter-shear obstruction can survive only if the relevant
null-face stresses are trapped in the **zero-transfer forest face** or in the already
classified one-dimensional straight-chain phase.

The next closing target is no longer a generic electrical hinge:

> **C57 zero-transfer null-face exclusion.** Prove that the exposed C54 null face
> cannot annihilate the whole strong flex space while all of its two-dimensional
> stresses satisfy `K=B^{-1}` (and its one-dimensional stresses are straight chains),
> unless the strong diameter angular rates already have one common value.

Two concrete routes remain:

1. convert the direction-local split structure (C56.30) into a source-preserving
   one-/two-vertex contact separator and use the strong-support connectivity/bridge
   stack; or
2. use convexity of the null face: show that mixing two zero-transfer stresses with
   different diameter supports necessarily creates a stress with a negative
   off-diagonal transfer `c<0`, after which C56.5 gives common angular rate.

The second route is especially short if the zero-transfer property is not preserved by
nontrivial support mixing.

## 7. Verification

The minimum-shift dichotomy was additionally falsification-tested on random extreme
points of the abstract Robinson/harmonic linear system for `m=3,...,8`, with unequal
positive `gamma` and random strict slopes. Among 3000 PSD extreme points tested:

- every case with `c<0` had nullity exactly two;
- every case with `c=0` had all off-diagonal transfers zero;
- no mixed C55 block pattern occurred.

These computations are regression checks only. The proof is the exact weighted
Fiedler argument above.

## 8. Binding cautions

- C56 classifies one selected two-dimensional stress. It does not by itself make that
  support maximal in the C54 null face.
- The zero-transfer phase is electrically realizable by star/tree-like responses; it
  cannot be rejected by linear algebra alone.
- C56.30 is a statement about the positive Kalmanson split representation in edge
  coordinates, not yet a literal decomposition of the physical unit-contact network.
- A one-dimensional null-face extreme stress remains the exact straight-chain phase
  of C54.1.
- C-II is still separate until Gate C-I eliminates weak contacts.

## 9. Compact handoff

**LEVEL I STATUS:** still open.

**C56:** with `c=min_{i!=j}K_ij`, either

- `c<0`, in which case `ker M=span{1,t}` and every tangential selected-kernel velocity
  has one common diameter angular rate; or
- `c=0`, in which case `M=0`, `K=B^{-1}`, the positive diameter graph is a forest,
  every C55 gap is isolated, and every positive Kalmanson split is supported on one
  edge or two adjacent diameter directions.

**Consequently:** the mixed isolated-hinge configurations allowed by C55 do not occur.
Any surviving C-I shear is trapped in a global zero-transfer forest/null-face phase.

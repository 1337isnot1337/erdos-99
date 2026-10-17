> Generated reading edition · [exact source](../../../docs/reports/target_c_four_pair_response_contraction_2026-08-31.md) · source SHA-256 `4821f00059780c8dd4951d24e7190aaa53dc44d794e3a76556b2c137e06835e4`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-1C0BBD127DA4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_four_pair_response_contraction_2026-08-31.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=c59d797999d35d414bcae0a84ddcf80d4aae73d5; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — Target C: four-pair response contraction

**Date:** 2026-08-31<br>
**Repository state:** `research/target-c-current-frontier-2026-08-31` at `bc6ea85` before this addendum<br>
**Run type:** closing proof / response inequality<br>
**Target:** C / C-I selected-stress subcase<br>
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`<br>
**External web search:** used for the inherited Kalmanson source audit
**Computation:** used only for exact symbolic expansion; no script added

## LEVEL I STATUS

`STILL OPEN`.

This report closes a new finite response subcase. It does not prove the global
support-selection statement needed for C-I, and it does not close the fully
force-visible C-II branch.

## 1. Starting endpoint

C30 gives a response-inertia budget for a selected normalized stress. C31, C32,
and C50 settle the three-edge forest cases on four, five, and six force-hull
endpoints. They do not give a general PSD comparison when the selected positive
diameter support has four edges: two affine response modes are forced, but two
non-affine modes remain.

The exact subcase attacked here is the four-edge opposite matching

```math
H=\{04,15,26,37\}
```

on eight strictly convex cyclic boundary vertices. The desired implication is

```text
four-pair response contraction -> Lambda-L_H >= 0 -> selected Schur defect Omega >= 0.
```

## 2. Strongest genuinely new audited theorem

### Theorem C51 (four-pair opposite-matching contraction)

Let $`p_0,\ldots,p_7`$ be distinct vertices in strict convex cyclic order, and
let $`P`$ be their $`8\times2`$ coordinate matrix, translated so that
$`\mathbf 1^{\mathsf T}P=0`$. Put

```math
q_i=e_i-e_{i+4},\qquad Q=(q_0\ q_1\ q_2\ q_3),
```

and let $`B=\operatorname{diag}(\beta_0,\ldots,\beta_3)`$ with every
$`\beta_i>0`$. Define

```math
L_H=QBQ^{\mathsf T},\qquad U=Q^{\mathsf T}P,
```

so the $`i`$-th row of $`U`$ is $`u_i=p_i-p_{i+4}`$.

Assume that $`\Lambda`$ is the connected positive-contact Dirichlet response
on these eight boundary vertices, $`R=\Lambda^+`$, and the affine force-hull
identity holds:

```math
\Lambda\mathbf 1=0,\qquad \Lambda P=L_HP.
```

Assume also that the effective-resistance matrix

```math
W_{ij}=R_{ii}+R_{jj}-2R_{ij}
```

has the circular-planar Kalmanson property. Then, with

```math
K=Q^{\mathsf T}RQ,
```

one has the full contraction

```math
\boxed{B^{-1}-K\succeq0.}
\tag{C51.1}
```

Equivalently, $`T=B^{1/2}KB^{1/2}`$ satisfies $`T\preceq I`$. Consequently the
boundary response defect $`\Lambda-L_H`$ is positive semidefinite on
$`\mathbf1^\perp`$, and the C30 Schur reduction gives

```math
\boxed{\Omega=L_C(\alpha)-L_H(\beta)\succeq0}
\tag{C51.2}
```

for the selected positive contact support.

### Scope

This is a finite selected-support theorem. It applies to arbitrary positive
weights and arbitrary strictly convex eight-point geometry satisfying the stated
response identity; it does not assume a regular octagon, equal chord lengths,
equal conductances, a tree contact graph, or global optimality by itself. It is
not a theorem for an arbitrary four-edge diameter graph, for degenerate hulls, or
for a direction-dependent maximal-support selection without the displayed
matching topology.

### Proof

#### 1. Convex chord directions

For $`i<j`$ in $`\{0,1,2,3\}`$, the four vertices

```math
p_i,p_j,p_{i+4},p_{j+4}
```

occur in this cyclic order and form a strictly convex quadrilateral. Its two
directed diagonals are $`u_i=p_i-p_{i+4}`$ and $`u_j=p_j-p_{j+4}`$. The diagonal
intersection, or an affine normalization of this quadrilateral, gives

```math
\det(u_i,u_j)>0.
\tag{C51.3}
```

Thus the four directions lie in an open half-plane. Choose covectors $`\ell,m`$
with $`\ell(u_i)>0`$ and put

```math
a_i=\ell(u_i)>0,\qquad t_i=\frac{m(u_i)}{\ell(u_i)}.
```

Choosing the orientation of $`(\ell,m)`$, (C51.3) says
$`t_0<t_1<t_2<t_3`$. Replacing $`m`$ by a positive affine combination of
$`m`$ and $`\ell`$, we may normalize

```math
t_0=0,\qquad t_1=1,qquad t_2=1+r,qquad t_3=1+r+s,
\tag{C51.4}
```

with $`r,s>0`$. The chord lengths are not normalized away: the exact relation is

```math
u_i=a_i(1,t_i).
\tag{C51.5}
```

#### 2. The affine kernel and a two-by-two defect

Since the columns of $`P`$ are centered, $`R\Lambda P=P`$. The affine identity
therefore gives

```math
R QB U=P,
\qquad KBU=U.
\tag{C51.6}
```

Let $`D=B^{1/2}`$, $`T=DKD`$, and $`A=DU`$. Equation (C51.6) becomes

```math
TA=A.
\tag{C51.7}
```

The matrix $`U`$, and hence $`A`$, has rank two by (C51.3). Define
$`\widehat S=I-T`$. Then $`\widehat S A=0`$. Let

```math
V=\begin{pmatrix}
1&0\\
1&1\\
1&1+r\\
1&1+r+s
\end{pmatrix},
\qquad
E=\operatorname{diag}(a_0,a_1,a_2,a_3),
```

so $`U=EV`$. The following four-by-two matrix has columns spanning
$`\ker U^{\mathsf T}`$:

```math
C_0=
\begin{pmatrix}
r&0\\
-(r+1)&s\\
1&-(r+s)\\
0&r
\end{pmatrix}.
\tag{C51.8}
```

Indeed, direct substitution into (C51.4) gives $`C_0^{\mathsf T}V=0`$, and
the first and last rows show that $`C_0`$ has rank two. Put

```math
C=E^{-1}C_0,
\qquad N=D\widehat S D.
```

Then $`NU=0`$, and symmetry implies that the range of $`N`$ is contained in
$`\ker U^{\mathsf T}=\operatorname{col}(C)`$. Hence there is a unique symmetric
two-by-two matrix $`G`$ such that

```math
N=CGC^{\mathsf T},
\qquad
\widehat S=D^{-1}CGC^{\mathsf T}D^{-1}.
\tag{C51.9}
```

Write $`G=\begin{pmatrix}x&y\\y&z\end{pmatrix}`$, and set

```math
M=C_0GC_0^{\mathsf T},qquad \gamma_i=a_i\beta_i>0.
\tag{C51.10}
```

For $`i\ne j`$, (C51.9) gives

```math
N_{ij}=\frac{M_{ij}}{a_i a_j}=-\beta_i\beta_jK_{ij}.
\tag{C51.11}
```

#### 3. The Kalmanson monotonicity inequalities

The Kalmanson split-cone representation used in C50 says that, modulo a sum
matrix, $`W`$ is a nonnegative combination of interval cut matrices. For an
interval $`I`$ on the eight-cycle, put

```math
z_i=\mathbf1_I(i)-\mathbf1_I(i+4).
```

The interval cut contributes $`zz^{\mathsf T}`$ to $`K=Q^{\mathsf T}RQ`$, while
the sum matrix contributes zero. Up to a global sign (replace an interval by its
complement), the possible nonzero $`z`$-vectors are

```math
\begin{gathered}
0001,0010,0011,0100,0110,0111,\\
1\bar1\bar1\bar1,10\bar1\bar1,100\bar1,1000,
11\bar1\bar1,110\bar1,1100,111\bar1,1110,1111,
\end{gathered}
\tag{C51.12}
```

where $`\bar1=-1`$; the zero vector comes from the empty/full interval cases.
For every one of these vectors and every $`i<j<k`$ in $`\{0,1,2,3\}`$,

```math
z_k(z_i-z_j)\le0.
```

Therefore the nonnegative split representation gives the exact monotonicity

```math
\boxed{K_{ik}\le K_{jk}\qquad(0\le i<j<k\le3).}
\tag{C51.13}
```

Combining (C51.11) and (C51.13), and cancelling the positive common factor,
gives

```math
\frac{M_{ik}}{\gamma_i}\ge\frac{M_{jk}}{\gamma_j}
\qquad(0\le i<j<k\le3).
\tag{C51.14}
```

Only three instances are needed. Define

```math
A_1=\gamma_0(r+1)+\gamma_1r,
```

```math
A_y=\gamma_0(r^2+rs+r+2s)+\gamma_1(r^2+rs),
```

```math
C_1=\gamma_1(r+s)+\gamma_2s,
\qquad
C_2=\gamma_1+\gamma_2(r+1).
```

Expanding the three inequalities in (C51.14) for
$`(i,j,k)=(0,1,2),(0,1,3),(1,2,3)`$, respectively, yields

```math
A_1x-A_yy+\gamma_0s(r+s)z\ge0,
\tag{C51.15}
```

```math
A_1y-\gamma_0sz\ge0,
\tag{C51.16}
```

```math
C_1z-C_2y\ge0.
\tag{C51.17}
```

#### 4. The scalar sign argument

Put

```math
L=\frac{\gamma_0s}{A_1},qquad U=\frac{C_1}{C_2}.
```

All denominators are positive, and direct subtraction gives

```math
U-L
=\frac{\gamma_1r\bigl(\gamma_0(r+s+1)+\gamma_1(r+s)+\gamma_2s\bigr)}
        {C_2A_1}>0,
\tag{C51.18}
```

while

```math
r+s-U=\frac{\gamma_2r(r+s+1)}{C_2}>0.
\tag{C51.19}
```

If $`z<0`$, (C51.16)--(C51.17), after division by the negative number $`z`$,
would require $`U\le y/z\le L`$, contradicting (C51.18). If $`z=0`$, the
same two inequalities force $`y=0`$, and (C51.15) gives $`x\ge0`$. Thus $`G`$
is positive semidefinite in this case.

It remains to consider $`z>0`$. Set $`t=y/z`$. Equations (C51.16)--(C51.17)
give

```math
L\le t\le U<r+s.
\tag{C51.20}
```

The left side of (C51.15), divided by $`z`$, is nonnegative, so

```math
\frac{x}{z}\ge
\frac{A_yt-\gamma_0s(r+s)}{A_1}.
```

The exact factorization

```math
A_1t^2-A_yt+\gamma_0s(r+s)
=-(r+s-t)(A_1t-\gamma_0s)
\tag{C51.21}
```

and (C51.20) imply that the left side of (C51.21) is nonpositive. Consequently

```math
\frac{x}{z}\ge t^2,
\qquad xz-y^2\ge0.
```

Together with $`z>0`$, this proves $`G\succeq0`$. Equation (C51.9) now gives
$`\widehat S\succeq0`$, hence $`T\preceq I`$ and (C51.1).

Finally, the nonzero eigenvalues of

```math
B^{1/2}Q^{\mathsf T}\Lambda^+QB^{1/2}
\quad\text{and}\quad
\Lambda^{-1/2}L_H\Lambda^{-1/2}
```

are the same. Therefore (C51.1) implies
$`\Lambda-L_H\succeq0`$ on $`\mathbf1^\perp`$. The positive interior block in
the C30 Schur congruence is positive definite, proving (C51.2). $`\square`$

## 3. Exact target implication

Before C51, a selected four-edge matching had two uncontrolled non-affine
response modes. C51 removes both at once:

```math
H=\{04,15,26,37\},\quad
\text{strict convex endpoints},\quad
\text{circular-planar response}
\Longrightarrow
\Lambda-L_H\succeq0.
```

Thus this matching cannot supply a negative Schur mode to the C-I shear
separator. It also removes this topology from the fully force-visible C-II
response obstruction when the selected positive stress has exactly this support.

The remaining global implication is not a matrix inequality. One must still prove
that the relevant direction-dependent KKT multiplier can be selected with a
support covered by the already closed finite topologies, or else close the
general support-selection/diameter-shear alternative directly.

## 4. Exact remaining lemma

The shortest missing statement after C51 is:

> **Maximal-support transport lemma.** Every two-dimensional positive KKT
> diameter support that survives the C-I separator has a finite decomposition,
> compatible with the same circular-planar response and affine identity, into
> selected response blocks whose signed Schur defects are positive semidefinite;
> equivalently, the direction-dependent critical-cone multiplier admits a
> relative-interior common-angular-rate velocity.

This is not proved here. In particular, C51 does not imply that an arbitrary
support has matching topology, nor that semidefinite selected defects integrate
to a finite same-diameter release.

## 5. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| Opposite-chord orientation (C51.3) | proved | Each pair is the directed-diagonal pair of a strict convex quadrilateral. |
| Kalmanson monotonicity (C51.13) | proved | Exact interval-cut split check; the same decomposition is audited in C50. |
| Four-pair contraction (C51.1) | proved | The three exact inequalities force the two-by-two defect matrix (G) to be PSD. |
| Selected Schur positivity (C51.2) | proved | Singular-value equivalence plus the C30 Schur congruence. |
| Strict positivity in the four-pair case | not proved | The scalar argument allows equality; no triangle-free source classification is claimed. |
| Arbitrary four-edge diameter support | not proved | The opposite matching and strict convexity are essential hypotheses. |
| C-I globally closed | not proved | Support selection and the shear-separator alternative remain. |

## 6. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| C33 abstract six-endpoint sign cone | yes | It is not circular-planar: it violates an exact circular minor/Kalmanson constraint. |
| Unequal opposite-chord lengths | yes | The proof keeps $`a_i>0`$ and uses $`\gamma_i=a_i\beta_i`$; no unit-length normalization is used. |
| Unequal positive conductances | yes | The proof uses arbitrary positive $`\gamma_0,\gamma_1,\gamma_2`$; $`\beta_3`$ is unrestricted except for positivity. |
| Regular-octagon/star equality response | yes | The theorem is semidefinite, not strict; equality is not incorrectly discarded. |
| Non-circular or disconnected response | outside scope | The circular-planar Kalmanson property and connected response are explicit hypotheses. |
| One-dimensional force hull | outside scope | That canonical phase is already excluded separately. |

## 7. Failed routes and no-go results

The first draft incorrectly set all four vectors (u_i) to $`(1,t_i)`$ by a
single linear coordinate change. A linear map preserves individual scale factors,
so that normalization is invalid in general. The corrected proof writes
$`u_i=a_i(1,t_i)`$ and carries the factors into
$`\gamma_i=a_i\beta_i`$. This correction is binding: any future use of the
four-pair lemma must retain these factors or state an additional equal-scale
hypothesis.

The proof also does not promote the tempting general claim that every opposite
matching with any number of pairs has $`B^{-1}-K\succeq0`$. Small exact LP
experiments suggest such a direction, but no proof for five or more pairs is
included here.

## 8. Literature imported

The only external input is the already audited circular-planar Kalmanson structure:

### Forcey, *Circular planar electrical networks, Split systems, and Phylogenetic networks*

- Link: <https://arxiv.org/abs/2108.00550>
- Exact use: effective-resistance matrices of circular-planar positive networks
  satisfy the Kalmanson inequalities.
- Hypotheses used here: connected positive planar network with the eight boundary
  terminals in cyclic order.
- Conclusion used here: the interval-cut/sum-matrix Kalmanson cone, after applying
  zero-sum vectors (q_i), gives (C51.13).

The split-cone form and its exact interval-cut decomposition are also recorded in
C50 from Proposition 3.1 of Polyakovskiy--Spieksma--Woeginger,
<https://digital.library.adelaide.edu.au/server/api/core/bitstreams/9cc0da56-2dfb-4a98-bf0a-40f81869cbd2/content>.
No source is being used to claim a global Erdős result.

## 9. Computation and reproducibility

A transient SymPy calculation expanded the three entries of
$`C_0GC_0^{\mathsf T}`$ and verified the factorization (C51.21) over the exact
polynomial ring. It used symbolic arithmetic only and was not logically required:
all displayed identities can be checked by direct multiplication. No research
script or numerical certificate was added.

## 10. Canonical promotion recommendation

**Promote now** — the proof is exact, its hypotheses are explicit, and it removes
the first four-edge matching response obstruction beyond the three-edge forest
ledger.

Promotion files:

- `docs/reports/target_c_four_pair_response_contraction_2026-08-31.md`;
- `docs/targets/target-c/01-force-hull-and-shear.md`;
- `docs/targets/target-c/README.md`;
- `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`.

## 11. Next run

Attack the support-selection gap: determine whether a maximal positive KKT
diameter support can be reduced, without changing the affine response identity,
to matching blocks of size at most four. If not, the next highest-value branch is
the C44-C45 macroscopic harmonic-cell exclusion, because C51 only addresses a
finite support topology and leaves the global force-visible response mass
uncontrolled.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Strongest new theorem:
  For eight strictly convex cyclic terminals and the opposite matching
  H={04,15,26,37}, every connected circular-planar response satisfying
  Lambda P=L_H P obeys B^{-1}-Q^T Lambda^+ Q >= 0. The selected Schur defect
  is therefore PSD. Unequal chord scales are retained through gamma_i=a_i beta_i.

Exact endpoint now:
  The four-edge opposite matching is removed from the selected response
  obstruction. The global maximal-support transport / C-I shear-separator
  lemma remains open; C-II remains open.

Binding regressions/no-go results:
  Do not normalize all chord vectors to (1,t_i) without scale factors; do not
  promote the numerical q>=5 LP suggestion; equality is not automatically strict.

Highest-value next lemma:
  A support-selection/transport theorem covering arbitrary two-dimensional
  positive diameter supports, or a direct C44-C45 macroscopic-cell exclusion.

Authoritative files:
  docs/targets/target-c/README.md
  docs/targets/target-c/01-force-hull-and-shear.md
  docs/reports/target_c_four_pair_response_contraction_2026-08-31.md
```

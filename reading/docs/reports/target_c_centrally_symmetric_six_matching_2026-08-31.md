> Generated reading edition · [exact source](../../../docs/reports/target_c_centrally_symmetric_six_matching_2026-08-31.md) · source SHA-256 `a191efc9b63ced53956940aa62fe56ab92112c3ef7c5214804a97c54d170f11b`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-DB65390AEF16","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: centrally symmetric six-endpoint Kalmanson lemma

**Date:** 2026-08-31  
**Repository state:** 4bd6f42 (origin/main before this promotion)  
**Run type:** exact response inequality / C-I subcase  
**Target:** Target C Gate C-I, six-endpoint three-diameter matching  
**Active prompt:** docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md  
**External web search:** used to verify the circular-planar resistance input  
**Computation:** not used in the proof

## LEVEL I STATUS

**STILL OPEN.**

This addendum removes the regularity assumption from the selected-stress
Kalmanson argument. It proves the response inequality for every nondegenerate
centrally symmetric convex six-terminal matching, but it does not remove the
maximal-support requirement, the equality mode, or the non-centrally-symmetric
six-terminal case.

## 1. Starting endpoint

C30-C32 reduce the three-edge response-inertia question to the six-endpoint
matching

```math
H_s=\{03,14,25\}.
```

The previous Kalmanson certificate handled only a regular hexagon. The exact
implication sought here is

```math
\text{central symmetry of the six-terminal geometry}
\ \Longrightarrow\
\rho_s\le 1
\ \Longrightarrow\
\Omega_s\succeq0.
```

The last implication is the C30 response-inertia alternative. It remains a
selected-stress statement and is not, by itself, a C-I closure.

## 2. Strongest genuinely new audited theorem

### Theorem CS6 (centrally symmetric six-endpoint response positivity)

Let

```math
B=(p_0,p_1,p_2,p_3,p_4,p_5)
```

be the vertices of a nondegenerate centrally symmetric convex hexagon in cyclic
order. Translate its center to the origin, so that

```math
p_{i+3}=-p_i\qquad (i=0,1,2).
```

Let the positive diameter support be the opposite matching

```math
H_s=\{03,14,25\},
```

with positive normalized weights

```math
\beta_{03}=a,\qquad \beta_{14}=u,\qquad \beta_{25}=v,
\qquad a+u+v=1.
```

Let $`\Lambda`$ be the Dirichlet response on these six boundary terminals of a
connected circular-planar positive-conductance contact network, and let

```math
R=\Lambda^+,\qquad
W_{ij}=R_{ii}+R_{jj}-2R_{ij}.
```

Assume the C11 affine response identity

```math
\Lambda P_B=L_{H_s}P_B.
```

Then

```math
\boxed{aW_{03}+uW_{14}+vW_{25}\le 3.}
```

Consequently, in the C30 three-edge notation,

```math
\rho_s\le1
\qquad\text{and}\qquad
\boxed{\Omega_s\succeq0.}
```

### Scope

This theorem concerns one actual connected positive contact response and one
selected normalized stress. The six boundary terminals themselves form the
centrally symmetric convex hexagon; no independently chosen scaffold or
smaller optimum is introduced. The theorem does not assert that every
six-endpoint stress in a global minimizer has this geometry.

### Proof

Let $`U`$ be the $`6\times3`$ matrix whose columns are

```math
u_0=e_0-e_3,\qquad
u_1=e_1-e_4,\qquad
u_2=e_2-e_5.
```

Put

```math
A=\operatorname{diag}(a,u,v),\qquad
D=U^{\mathsf T}P_B.
```

The rows of $`D`$ are the vectors

```math
d_i^{\mathsf T},\qquad d_i=p_i-p_{i+3}=2p_i.
```

Because $`P_B=\frac12UD`$ and $`L_{H_s}=UAU^{\mathsf T}`$, the C11 identity,
after multiplication by $`R`$ and restriction to the centered coordinate
columns, gives

```math
R L_{H_s}P_B=P_B.
```

Premultiplying by $`U^{\mathsf T}`$ yields

```math
GAD=D,\qquad G:=U^{\mathsf T}RU.
\tag{CS6.1}
```

The three vectors $`d_0,d_1,d_2`$ span the plane. Since their directions occur
in this order inside an open half-plane, $`d_1`$ is a strictly positive linear
combination of $`d_0`$ and $`d_2`$. Thus there is a nonzero vector

```math
c=(c_0,c_1,c_2)^{\mathsf T},
\qquad c^{\mathsf T}D=0,
\qquad c_0>0,\quad c_1<0,\quad c_2>0.
\tag{CS6.2}
```

For example, if $`d_1=\lambda_0d_0+\lambda_2d_2`$ with
$`\lambda_0,\lambda_2>0`$, take
$`c=(\lambda_0,-1,\lambda_2)^{\mathsf T}`$.

Set $`K=G-A^{-1}`$. Equation (CS6.1) says that $`K`$ annihilates
$`\operatorname{col}(AD)`$. The normal vector to this two-dimensional subspace
is $`A^{-1}c`$, because

```math
(A^{-1}c)^{\mathsf T}(ADz)=c^{\mathsf T}Dz=0.
```

Since $`K`$ is symmetric, its range is contained in the same one-dimensional
normal space. Therefore, for a scalar $`\kappa`$,

```math
G=A^{-1}+\kappa A^{-1}cc^{\mathsf T}A^{-1}.
\tag{CS6.3}
```

The target weighted resistance is the trace

```math
\begin{aligned}
aW_{03}+uW_{14}+vW_{25}
&=\operatorname{tr}(R L_{H_s})\\
&=\operatorname{tr}(GA)\\
&=3+\kappa\,c^{\mathsf T}A^{-1}c.
\end{aligned}
\tag{CS6.4}
```

It remains to determine the sign of $`\kappa`$.

Let $`T`$ be the half-turn permutation $`i\mapsto i+3`$ modulo six and define

```math
\overline R=\frac12(R+T^{\mathsf T}RT).
```

The Kalmanson inequalities are linear in $`W`$ and invariant under cyclic
relabeling, so $`\overline R`$ has the same Kalmanson inequalities. Also
$`T U=-U`$, hence

```math
U^{\mathsf T}\overline R U=U^{\mathsf T}RU=G.
\tag{CS6.5}
```

In the top/bottom pair ordering, write the half-turn-invariant matrix as

```math
\overline R=
\begin{pmatrix}E&F\\F&E\end{pmatrix}.
```

Then $`G=2(E-F)`$. Direct expansion of the cyclic Kalmanson expression gives

```math
\begin{aligned}
\mathcal K_1(0,1,2,3)
&=W_{02}+W_{13}-W_{01}-W_{23}\\
&=G_{01}-G_{02}.
\end{aligned}
\tag{CS6.6}
```

Using (CS6.3), the diagonal part of $`A^{-1}`$ cancels from these off-diagonal
entries, and (CS6.6) becomes

```math
\mathcal K_1(0,1,2,3)
=\kappa\,\frac{c_0}{a}
\left(\frac{c_1}{u}-\frac{c_2}{v}\right).
\tag{CS6.7}
```

The Kalmanson inequality says that the left side is nonnegative. By (CS6.2)
and positivity of $`a,u,v`$, the factor multiplying $`\kappa`$ on the right is
strictly negative. Hence $`\kappa\le0`$. Since
$`c^{\mathsf T}A^{-1}c>0`$, (CS6.4) proves

```math
aW_{03}+uW_{14}+vW_{25}\le3.
```

Finally, C30 identifies the three nonzero eigenvalues of the conjugated
response comparison as $`1,1,\rho_s`$, where

```math
\rho_s=aW_{03}+uW_{14}+vW_{25}-2.
```

Thus $`\rho_s\le1`$, and the C30 inertia alternative gives
$`\Omega_s\succeq0`$. $`\square`$

## 3. Exact target implication

The selected-stress six-endpoint PSD subcase is now

```math
\text{centrally symmetric convex matching}
\quad\Longrightarrow\quad
\rho_s\le1.
```

This strictly contains the earlier regular-hexagon certificate. The remaining
selected-stress response classes are:

1. non-centrally-symmetric convex six-endpoint matchings; and
2. the equality case $`\rho_s=1`$, including the possibility of an additional
   scalar kernel mode.

The global C-I route also still needs to show that the direction-dependent
second-order stress has the required support. Therefore the exact remaining
implication is not a global theorem but

```math
\boxed{
\text{support selection}
\ +\
\text{strictness or equality classification}
\ \Longrightarrow\
\text{finite same-diameter release}.
}
```

## 4. Dependencies

- docs/reports/target_c_force_polygon_2026-08-30.md, Theorem C11:
  the actual positive contact Dirichlet response and
  $`\Lambda P_B=L_{H_s}P_B`$.
- docs/reports/target_c_three_edge_response_inertia_2026-08-31.md, Theorem C30:
  the two affine eigenvalues and the scalar three-edge response alternative.
- Stefan Forcey, *Circular planar electrical networks, Split systems, and
  Phylogenetic networks*, Theorem 4.2,
  [arXiv:2108.00550](https://arxiv.org/abs/2108.00550):
  the effective-resistance matrix of a connected circular-planar network obeys
  the cyclic Kalmanson inequalities. The theorem is used only as a necessary
  response property.

No generic PSD or Loewner comparison is used.

## 5. Why it is new

The earlier promoted certificate used a regular-hexagon coordinate elimination
and a five-term Kalmanson identity. The proof above uses only the half-turn
symmetry and the alternating sign pattern of the unique linear dependence among
the three opposite-pair vectors. It therefore applies to every centrally
symmetric convex six-terminal geometry, including nonregular cyclic geometries.

## 6. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| CS6 response inequality | proved | The half-turn average, affine response identity, and one Kalmanson inequality give the exact sign of $`\kappa`$. |
| CS6 semidefinite response conclusion | proved conditional on C30 | C30 converts $`\rho_s\le1`$ into the stated response-inertia conclusion. |
| Strict inequality for triangle-free sources | not proved | Kalmanson only gives $`\kappa\le0`$; equality is not excluded. |
| All six-endpoint matchings are PSD | not proved | The argument needs half-turn symmetry. |
| C-I is closed | not proved | The direction-dependent support-selection and equality-mode obligations remain. |
| General PSD/Loewner comparison | rejected | C33 gives an exact sign-cone regression, and no such general comparison is used here. |

## 7. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| Regular hexagon with opposite matching | yes | It is the special case $`p_{i+3}=-p_i`$ covered by CS6. |
| Unequal positive matching weights | yes | Only $`a,u,v>0`$ and $`a+u+v=1`$ enter the sign argument. |
| Circular-planar star response | yes | It realizes $`\kappa=0`$ and equality, so the proof correctly does not claim strictness. |
| C33 abstract sign-cone matrix | yes | It lacks the circular-planar Kalmanson property used in (CS6.7). |
| Collinear or nonconvex six-terminal sets | outside scope | The alternating sign pattern (CS6.2) need not hold. |

The star equality mode is a binding regression against any attempt to infer
strict positivity from connectedness and circular planarity alone.

## 8. Failed routes and no-go results

### Automatic strictness from Kalmanson

The proof has a single sign conclusion, $`\kappa\le0`$. Equality makes the
Kalmanson witness in (CS6.7) vanish, and the star response shows that this
boundary case is compatible with connected circular-planar response data.
An actual unit-contact or global-minimality argument is still required for
$`\kappa<0`$.

### Extension to arbitrary convex matchings by half-turn averaging

Without $`p_{i+3}=-p_i`$, the half-turn is not a symmetry of the terminal
geometry or of the matching response identity. The proof cannot be applied to
an arbitrary convex six-endpoint matching.

### Support-selection shortcut

CS6 applies to one selected normalized stress satisfying the stated six-terminal
hypotheses. It does not imply that the direction-dependent second-order
multiplier has maximal diameter support.

## 9. Literature imported

### Stefan Forcey, Theorem 4.2

- Link: [arXiv:2108.00550](https://arxiv.org/abs/2108.00550)
- Exact input: the resistance matrix associated to a connected circular-planar
  network satisfies the cyclic Kalmanson inequalities.
- Hypotheses used here: finite connected positive-conductance network with the
  displayed cyclic boundary order.
- Conclusion used here: $`\mathcal K_1(0,1,2,3)\ge0`$ after half-turn averaging.
- Normalization: none; the resistance matrix is the Moore--Penrose inverse of
  the response Laplacian.
- Applicability: yes, as a necessary condition on the C11 positive contact
  network response.

## 10. Computation and reproducibility

No computation is logically required. The only algebraic checks are the direct
matrix identities (CS6.1), (CS6.3), (CS6.4), and (CS6.6)-(CS6.7), all of which
are symbolic expansions in the displayed variables.

## 11. Canonical promotion recommendation

**Promote now — proof audited and frontier changes.**

Promote the theorem and its limitation into:

- docs/targets/target-c/01-force-hull-and-shear.md;
- docs/targets/target-c/README.md; and
- docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md.

The earlier regular-hexagon report remains useful provenance but is subsumed by
CS6.

## 12. Next run

The highest-value next lemma is:

```math
\boxed{
\text{A triangle-free actual unit-contact realization of CS6 cannot have }
\rho_s=1,
}
```

under the full-support hypothesis. A second route is to extend the response
inequality to non-centrally-symmetric convex six-endpoint matchings using the
full circular-planar split cone rather than half-turn symmetry.

## 13. Compact handoff

~~~text
LEVEL I STATUS: STILL OPEN.

Strongest new theorem:
For a connected circular-planar response on a centrally symmetric convex
six-terminal hexagon with opposite matching H={03,14,25}, positive normalized
weights satisfy
  a W_03 + u W_14 + v W_25 <= 3.
The proof uses C11, half-turn averaging, the alternating null vector
  c_0>0>c_1, c_2>0
and Kalmanson K_1(0,1,2,3)>=0. C30 then gives a PSD response defect.

Exact endpoint now:
Non-centrally-symmetric six-endpoint matchings, the rho=1 equality mode, and
the direction-dependent support-selection step remain.

Binding regressions/no-go results:
The circular-planar star has rho=1, so Kalmanson alone cannot give strictness.
C33 blocks a proof from affine kernel plus off-matching signs alone.

Highest-value next lemma:
Exclude rho=1 for a triangle-free actual unit-contact realization, or extend
the inequality to arbitrary convex six-endpoint matchings.

Authoritative files:
docs/targets/target-c/README.md
docs/targets/target-c/01-force-hull-and-shear.md
docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md
~~~

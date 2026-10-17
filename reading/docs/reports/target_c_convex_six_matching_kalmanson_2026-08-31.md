> Generated reading edition · [exact source](../../../docs/reports/target_c_convex_six_matching_kalmanson_2026-08-31.md) · source SHA-256 `a08c23258df8119a064af168b169500f138a7d50cd8fb32401165e1b6996852c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-36AD4C83DA73","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: convex six-endpoint Kalmanson closure

**Date:** 2026-08-31  
**Repository state:** 025fe3d (origin/main before this promotion)  
**Run type:** exact response inequality / C-I subcase  
**Target:** Target C Gate C-I, six-endpoint three-diameter matching  
**Active prompt:** docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md  
**External web search:** used to verify the circular-planar resistance input  
**Computation:** not used in the proof

## LEVEL I STATUS

**STILL OPEN.**

This addendum corrects and strengthens the preceding centrally symmetric
certificate. The half-turn is an index symmetry of the matching and may be
applied to the response matrix even when the terminal geometry is not
centrally symmetric. Convexity supplies the required sign pattern for the
three matching-chord vectors.

Consequently, the response inequality is proved for every nondegenerate
convex six-terminal geometry in the matching topology
$H_s=\{03,14,25\}$. This removes the entire three-edge six-endpoint response
obstruction, but it does not remove the direction-dependent support-selection
problem or the equality mode.

## 1. Starting endpoint

C30-C32 leave one response question in the three-edge forest case: the
six-endpoint matching. The previous promoted Kalmanson result treated a
regular hexagon and was then generalized to a centrally symmetric convex
hexagon.

The exact implication sought here is

$$
\text{convex six-terminal matching}
\ \Longrightarrow\
\rho_s\le1
\ \Longrightarrow\
\Omega_s\succeq0.
$$

The first implication is the new theorem. The second is C30's exact
three-edge response alternative.

## 2. Strongest genuinely new audited theorem

### Theorem K6 (convex six-endpoint response positivity)

Let

$$
B=(p_0,p_1,p_2,p_3,p_4,p_5)
$$

be the vertices of a nondegenerate strictly convex hexagon in counterclockwise
cyclic order. Let

$$
H_s=\{03,14,25\}
$$

be the matching with positive normalized weights

$$
\beta_{03}=a,\qquad \beta_{14}=u,\qquad \beta_{25}=v,
\qquad a+u+v=1,
\qquad a,u,v>0.
$$

Let $\Lambda$ be the Dirichlet response on these six terminals of a
connected circular-planar positive-conductance contact network. Put

$$
R=\Lambda^+,\qquad
W_{ij}=R_{ii}+R_{jj}-2R_{ij}.
$$

Assume the C11 affine response identity

$$
\Lambda P_B=L_{H_s}P_B.
$$

Then

$$
\boxed{aW_{03}+uW_{14}+vW_{25}\le3.}
\tag{K6.1}
$$

If this is the three-edge positive diameter support of a selected stress in
the C30 setting, then

$$
\boxed{\rho_s\le1,\qquad \Omega_s\succeq0.}
\tag{K6.2}
$$

No central symmetry of $B$ and no equality of the three chord lengths are
needed for (K6.1).

### Scope

The theorem is about one actual connected positive contact response and one
selected normalized matching support. The terminal points are the source
boundary vertices in cyclic order; no independent scaffold or smaller
optimum is introduced. It is not a theorem about a direction-dependent
second-order multiplier having maximal support.

### Proof

Translate the coordinate columns of $P_B$ by constants so that they are
centered. This does not change the C11 identity. Let $U$ be the $6\times3$
matrix with columns

$$
u_0=e_0-e_3,\qquad
u_1=e_1-e_4,\qquad
u_2=e_2-e_5,
$$

and set

$$
A=\operatorname{diag}(a,u,v),\qquad
D=U^{\mathsf T}P_B,\qquad
G=U^{\mathsf T}RU.
$$

The rows of $D$ are the directed matching chords

$$
d_i^{\mathsf T},\qquad d_i=p_i-p_{i+3}.
$$

Since $L_{H_s}=UAU^{\mathsf T}$, the C11 identity and
$R\Lambda P_B=P_B$ on centered columns give

$$
RUA D=P_B.
$$

Premultiplication by $U^{\mathsf T}$ gives the only response equation needed
below:

$$
GAD=D.
\tag{K6.3}
$$

#### Convex-chord sign lemma

For $0\le i<j\le2$, the four vertices
$p_i,p_j,p_{i+3},p_{j+3}$ occur in this cyclic order. Their two diagonals
cross, and the standard oriented-diagonal identity for a counterclockwise
convex quadrilateral gives

$$
\det(p_{i+3}-p_i,\ p_{j+3}-p_j)>0.
$$

Both $d_i$ and $d_j$ reverse these two diagonal orientations, so

$$
\det(d_i,d_j)>0
\qquad (0\le i<j\le2).
\tag{K6.4}
$$

Thus $d_0,d_1,d_2$ have directions in this order inside an open half-plane.
In particular, there are $\lambda_0,\lambda_2>0$ such that

$$
d_1=\lambda_0d_0+\lambda_2d_2.
$$

Therefore the one-dimensional nullspace of $D^{\mathsf T}$ is spanned by

$$
c=(c_0,c_1,c_2)^{\mathsf T}
=(\lambda_0,-1,\lambda_2)^{\mathsf T},
\qquad
c^{\mathsf T}D=0,
\qquad
c_0>0,\quad c_1<0,\quad c_2>0.
\tag{K6.5}
$$

#### The response block has one scalar freedom

Set $K=G-A^{-1}$. Equation (K6.3) says

$$
K(AD)=0.
$$

The normal vector to $\operatorname{col}(AD)$ is $A^{-1}c$, since

$$
(A^{-1}c)^{\mathsf T}(ADz)=c^{\mathsf T}Dz=0.
$$

The matrix $K$ is symmetric, so its range is contained in this
one-dimensional normal space. Hence, for a scalar $\kappa$,

$$
G=A^{-1}+\kappa A^{-1}cc^{\mathsf T}A^{-1}.
\tag{K6.6}
$$

The weighted effective-resistance sum is

$$
\begin{aligned}
aW_{03}+uW_{14}+vW_{25}
&=\operatorname{tr}(R L_{H_s})\\
&=\operatorname{tr}(GA)\\
&=3+\kappa\,c^{\mathsf T}A^{-1}c.
\end{aligned}
\tag{K6.7}
$$

#### Half-turn Kalmanson sign

Let $\tau$ be the index half-turn $i\mapsto i+3$ modulo six and define

$$
\overline R
=\frac12\left(R+\tau^{\mathsf T}R\tau\right).
$$

This is only an index symmetrization; it does not assert that the terminal
geometry is centrally symmetric. The effective-resistance Kalmanson
inequalities are linear and invariant under cyclic relabeling. Therefore
$\overline R$ satisfies the same Kalmanson inequalities. Also
$\tau U=-U$, so

$$
U^{\mathsf T}\overline R U=U^{\mathsf T}RU=G.
\tag{K6.8}
$$

In the top/bottom pair ordering, write

$$
\overline R=
\begin{pmatrix}E&F\\F&E\end{pmatrix}.
$$

Then $G=2(E-F)$. Direct expansion of one cyclic Kalmanson expression gives

$$
\begin{aligned}
\mathcal K_1(0,1,2,3)
&:=W_{02}+W_{13}-W_{01}-W_{23}\\
&=G_{01}-G_{02}.
\end{aligned}
\tag{K6.9}
$$

Using (K6.6), the diagonal part of $A^{-1}$ cancels from the off-diagonal
entries, and therefore

$$
\mathcal K_1(0,1,2,3)
=\kappa\,\frac{c_0}{a}
\left(\frac{c_1}{u}-\frac{c_2}{v}\right).
\tag{K6.10}
$$

The Kalmanson inequality makes the left side nonnegative. The factor
multiplying $\kappa$ on the right is strictly negative by (K6.5) and
$a,u,v>0$. Consequently $\kappa\le0$. Since
$c^{\mathsf T}A^{-1}c>0$, (K6.7) proves (K6.1).

Finally, C30 identifies the three nonzero conjugated response eigenvalues as

$$
1,\quad1,\quad
\rho_s=aW_{03}+uW_{14}+vW_{25}-2.
$$

Thus (K6.1) gives $\rho_s\le1$, and C30 gives (K6.2). $\square$

## 3. Exact target implication

The three-edge response alternatives are now all nonnegative:

- C31 handles four force-hull endpoints;
- C32 handles five endpoints; and
- K6 handles the six-endpoint matching for every convex terminal geometry.

Thus a selected three-edge forest cannot supply the negative response mode
allowed by the general C30 inertia count.

This is not a C-I closure. The remaining C-I obligations include:

1. proving that the direction-dependent second-order multiplier has the
   needed three-edge support, or controlling supports with more than three
   diameter edges; and
2. treating the equality case $\rho_s=1$, where an additional scalar kernel
   mode can remain.

## 4. Dependencies

- docs/reports/target_c_force_polygon_2026-08-30.md, Theorem C11:
  the actual positive contact response and
  $\Lambda P_B=L_{H_s}P_B$.
- docs/reports/target_c_three_edge_response_inertia_2026-08-31.md, Theorem C30:
  the two affine response eigenvalues and the three-edge scalar alternative.
- Stefan Forcey, *Circular planar electrical networks, Split systems, and
  Phylogenetic networks*, Theorem 4.2,
  [arXiv:2108.00550](https://arxiv.org/abs/2108.00550):
  effective resistance of a connected circular-planar network satisfies the
  cyclic Kalmanson inequalities.

No generic PSD or Loewner comparison is used.

## 5. Why it is new

The proof uses the index half-turn only after deriving the response block
equation. It therefore does not require a half-turn symmetry of $P_B$.
The only geometric input is the oriented crossing of the three pairs of
opposite cyclic chords, which forces the alternating sign pattern (K6.5).
This removes the central-symmetry restriction from the preceding addendum.

## 6. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| K6 response inequality | proved | Equations (K6.3)-(K6.10) are exact linear-algebra and Kalmanson identities. |
| K6 semidefinite response conclusion | proved conditional on C30 | C30 converts $\rho_s\le1$ into $\Omega_s\succeq0$. |
| All three-edge forest supports have no negative response mode | proved | C31, C32, and K6 cover four, five, and six endpoints. |
| Strict inequality in the triangle-free case | not proved | The Kalmanson sign gives only $\kappa\le0$. |
| C-I is closed | not proved | Support selection and equality-mode obligations remain. |
| General PSD/Loewner comparison | rejected | C33 shows the affine/sign data alone are insufficient, and K6 uses only the stated matching case. |

## 7. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| Regular hexagon | yes | It is a special convex six-gon and recovers the earlier certificate. |
| Nonregular centrally symmetric hexagon | yes | No regularity or metric symmetry is used. |
| Non-centrally-symmetric convex hexagon | yes | The chord determinant argument supplies (K6.5); the response is symmetrized only in index space. |
| Unequal positive matching weights | yes | The sign argument uses only positivity of $a,u,v$. |
| Circular-planar star response | yes | It realizes the boundary case $\kappa=0$, so no strict inequality is claimed. |
| C33 abstract sign-cone matrix | yes | It does not satisfy the circular-planar Kalmanson hypothesis used in (K6.10). |

## 8. Failed routes and no-go results

### Central symmetry as a necessary response hypothesis

It is not necessary. The proof does not average the terminal coordinates or
the response identity; it averages the response matrix after extracting the
matching block $G$, which is invariant under the index half-turn.

### Automatic strictness

The theorem gives $\kappa\le0$, not $\kappa<0$. The circular-planar star
equality mode remains compatible with the response hypotheses.

### Support-selection shortcut

K6 applies to a selected matching support. It does not imply that the
direction-dependent second-order multiplier has exactly this support.

## 9. Literature imported

### Stefan Forcey, Theorem 4.2

- Link: [arXiv:2108.00550](https://arxiv.org/abs/2108.00550)
- Exact input: the resistance matrix of a connected circular-planar network
  obeys the cyclic Kalmanson inequalities.
- Hypotheses used here: finite connected positive-conductance network with
  the displayed cyclic boundary order.
- Conclusion used here: $\mathcal K_1(0,1,2,3)\ge0$ after the index half-turn
  average.
- Applicability: yes, as a necessary property of the C11 response.

## 10. Computation and reproducibility

No computation is logically required. The proof is a finite symbolic
calculation from the displayed response equations and the oriented convex
quadrilateral identity.

## 11. Canonical promotion recommendation

**Promote now — proof audited and frontier changes.**

Promote this theorem and the corrected endpoint into:

- docs/targets/target-c/01-force-hull-and-shear.md;
- docs/targets/target-c/README.md; and
- docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md.

The centrally symmetric addendum is superseded for mathematical scope by K6,
while remaining useful provenance.

## 12. Next run

Attack the equality boundary of K6. Prove that $\rho_s=1$ forces an
additive effective-resistance metric (a star-equivalent response), then use
the actual unit-contact geometry or full-support hypothesis to exclude that
response in a triangle-free global minimizer. In parallel, address the
support-selection step for the direction-dependent second-order multiplier.

## 13. Compact handoff

~~~text
LEVEL I STATUS: STILL OPEN.

Strongest new theorem:
For any nondegenerate convex six-terminal geometry in cyclic order, a
connected circular-planar response satisfying C11 for
H={03,14,25} and positive normalized weights obeys
  a W_03 + u W_14 + v W_25 <= 3.
The proof extracts G=U^T R U, obtains
  G=A^{-1}+kappa A^{-1} c c^T A^{-1}
with c_0>0>c_1 and c_2>0 from crossing convex chords, then applies one
Kalmanson inequality to the index-half-turn average of R. C30 gives
Omega_s >= 0 for the three-edge six-endpoint matching.

Exact endpoint now:
All three-edge forest topologies have no negative response mode. The
direction-dependent support-selection step, supports with more than three
diameter edges, and the rho=1 equality mode remain.

Binding regressions/no-go results:
The circular-planar star realizes rho=1, so Kalmanson does not imply
strictness. C33 blocks any proof using only affine kernel and off-matching
signs.

Highest-value next lemma:
Show rho=1 forces a star-equivalent response and rule that out using actual
unit-contact/global geometry, or control the support-selection step.

Authoritative files:
docs/targets/target-c/README.md
docs/targets/target-c/01-force-hull-and-shear.md
docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md
~~~

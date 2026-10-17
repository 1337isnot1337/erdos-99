> Generated reading edition · [exact source](../../../docs/reports/target_c_six_matching_equality_star_2026-08-31.md) · source SHA-256 `75c80904ffc5539f44b49955e5e19267932183dcaa7d08fd25bb4d2bb349f529`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-35DAB5E36077","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: equality rigidity for the six-endpoint Kalmanson bound

**Date:** 2026-08-31  
**Repository state:** c9edbd6 (origin/main before this promotion)  
**Run type:** exact equality classification / C-I subcase  
**Target:** Target C Gate C-I, three-edge six-endpoint matching  
**Active prompt:** docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md  
**External web search:** not used beyond the already audited Kalmanson input  
**Computation:** not used in the proof

## LEVEL I STATUS

**STILL OPEN.**

This addendum classifies the equality case in the convex six-endpoint Kalmanson
closure. If the scalar response threshold satisfies $`\rho_s=1`$, the terminal
effective-resistance metric is additive, hence star-shaped as a resistance
metric. This is an exact reduction, not yet a geometric contradiction for the
actual unit-contact graph.

## 1. Starting endpoint

The K6 convex six-endpoint lemma proves

```math
aW_{03}+uW_{14}+vW_{25}\le3,
```

and therefore $`\rho_s\le1`$. Equality is the only remaining response mode in
which C30 can leave an additional non-affine kernel direction.

The exact implication sought here is

```math
\rho_s=1
\ \Longrightarrow\
\text{all cyclic Kalmanson inequalities vanish}
\ \Longrightarrow\
W_{ij}=r_i+r_j\quad(i\ne j).
```

## 2. Strongest genuinely new audited theorem

### Theorem EQ6 (equality forces an additive resistance metric)

Assume the hypotheses of K6. If

```math
aW_{03}+uW_{14}+vW_{25}=3,
\tag{EQ6.1}
```

then there are nonnegative pendant parameters $`r_0,\ldots,r_5`$ such that

```math
\boxed{W_{ij}=r_i+r_j\qquad(i\ne j).}
\tag{EQ6.2}
```

Moreover,

```math
\boxed{r_i+r_{i+3}=\frac1{\beta_i}
\qquad(i=0,1,2),}
\tag{EQ6.3}
```

where $`\beta_0=a,\beta_1=u,\beta_2=v`$. Thus the boundary response is
star-equivalent in the electrical resistance metric, with the opposite-pair
pendant sums fixed by the matching weights.

If the response matrix is itself half-turn invariant, then
$`r_{i+3}=r_i=1/(2\beta_i)`$.

### Scope

The theorem concerns the response matrix of the actual connected
circular-planar positive contact network in the selected three-edge matching
subcase. It does not claim that the physical contact graph is literally a
one-vertex star, because electrical equivalence can be preserved by network
reductions and does not preserve unit-edge geometry.

### Proof

Use the notation of K6. Equality in (K6.1) and (K6.7) gives $`\kappa=0`$ in

```math
G=A^{-1}+\kappa A^{-1}cc^{\mathsf T}A^{-1}.
\tag{EQ6.4}
```

Let $`\tau`$ be the index half-turn and put

```math
\overline R=\frac12(R+\tau^{\mathsf T}R\tau)
=\begin{pmatrix}E&F\\F&E\end{pmatrix}.
```

Set

```math
X=E-F=\frac12G
=\operatorname{diag}(x_0,x_1,x_2),
\qquad
x_0=\frac1{2a},\quad
x_1=\frac1{2u},\quad
x_2=\frac1{2v},
\tag{EQ6.5}
```

and write $`Y=E+F`$. Since $`\overline R\mathbf1=0`$, the symmetric matrix $`Y`$
has zero row sums. Denote its three off-diagonal entries by

```math
z_{01}=Y_{01},\qquad z_{02}=Y_{02},\qquad z_{12}=Y_{12}.
```

With $`X`$ diagonal, direct expansion of the Kalmanson expressions gives the
following opposite pairs:

```math
\begin{aligned}
\mathcal K_2(0,1,2,3)&=-\mathcal K_1(0,1,3,5),\\
\mathcal K_1(0,1,2,4)&=-\mathcal K_2(0,1,4,5),\\
\mathcal K_1(0,1,2,5)&=-\mathcal K_2(0,2,4,5).
\end{aligned}
\tag{EQ6.6}
```

Every term in (EQ6.6) is nonnegative by Kalmanson. Hence all six terms
vanish. Equivalently,

```math
\begin{aligned}
x_0+2z_{01}+2z_{02}-z_{12}&=0,\\
x_1+2z_{01}-z_{02}+2z_{12}&=0,\\
x_2-z_{01}+2z_{02}+2z_{12}&=0.
\end{aligned}
\tag{EQ6.7}
```

Solving gives

```math
\begin{aligned}
z_{01}&=\frac{-2x_0-2x_1+x_2}{9},\\
z_{02}&=\frac{-2x_0+x_1-2x_2}{9},\\
z_{12}&=\frac{x_0-2x_1-2x_2}{9}.
\end{aligned}
\tag{EQ6.8}
```

Substitution into the definition of $`W`$ gives, for every distinct terminal
pair,

```math
\overline W_{ij}=x_i+x_j,
\qquad
x_{i+3}=x_i.
\tag{EQ6.9}
```

In particular every Kalmanson expression of $`\overline W`$ vanishes.

For any cyclic quadruple and either Kalmanson type,

```math
\mathcal K(\overline W)
=\frac12\bigl(\mathcal K(W)+\mathcal K(\tau W)\bigr).
\tag{EQ6.10}
```

Both terms on the right are nonnegative, while the left side is zero.
Therefore every cyclic Kalmanson expression of the original $`W`$ also
vanishes.

It remains to solve the resulting linear equalities. For
$`2\le i<j\le5`$, the two zero Kalmanson identities on
$`(0,1,i,j)`$ give

```math
W_{0i}+W_{1j}=W_{01}+W_{ij},
\qquad
W_{0i}+W_{1j}=W_{0j}+W_{1i}.
\tag{EQ6.11}
```

Define

```math
r_0=\frac{W_{01}+W_{0i}-W_{1i}}2,\qquad
r_1=W_{01}-r_0,\qquad
r_i=W_{0i}-r_0\quad(i=2,3,4,5).
\tag{EQ6.12}
```

The second identity in (EQ6.11) makes $`r_0`$ independent of the chosen
$`i`$. The first identity then gives $`W_{ij}=r_i+r_j`$ for all distinct
$`i,j`$, proving (EQ6.2). Since $`W`$ is an effective-resistance metric, the
$`r_i`$ are nonnegative: the resistance triangle inequality gives
$`2r_i=W_{ij}+W_{ik}-W_{jk}\ge0`$ for any two distinct $`j,k\ne i`$.
Thus they are the (possibly limiting) pendant lengths of its star metric.

Finally,

```math
W_{i,i+3}=u_i^{\mathsf T}Ru_i=G_{ii}=\frac1{\beta_i},
```

and (EQ6.2) gives (EQ6.3). If $`R`$ is half-turn invariant, then
$`r_i=r_{i+3}`$, giving the last assertion. $`\square`$

## 3. Exact target implication

The response equality mode is no longer an arbitrary point of the
Kalmanson cone. It must be a star-equivalent resistance metric:

```math
\rho_s=1
\quad\Longrightarrow\quad
W\text{ is additive}
\quad\Longrightarrow\quad
\text{all circular Kalmanson defects vanish}.
```

This supplies a concrete target for the remaining geometry. To close the
selected full-support C-I subcase, it would suffice to prove that an actual
triangle-free unit-contact network with the C11 coordinate identity cannot
have this additive response, or that its additive response forces a
same-diameter finite release.

The theorem does not itself prove either implication. Electrical star
equivalence does not automatically identify the physical contact graph with
a one-hub unit framework.

## 4. Dependencies

- docs/reports/target_c_convex_six_matching_kalmanson_2026-08-31.md, Theorem K6:
  the convex six-endpoint bound and the half-turn response-block reduction.
- docs/reports/target_c_force_polygon_2026-08-30.md, Theorem C11:
  the actual positive contact response and affine response identity.
- docs/reports/target_c_three_edge_response_inertia_2026-08-31.md, Theorem C30:
  the scalar equality mode $`\rho_s=1`$ and its extra-kernel interpretation.
- The circular-planar Kalmanson inequalities imported in K6.

No assertion that the physical graph is a literal star is used.

## 5. Why it is new

K6 established only the inequality $`\rho_s\le1`$. EQ6 determines the full
boundary resistance metric at equality and propagates the vanishing of one
half-turn-averaged Kalmanson certificate to every cyclic Kalmanson equality.
This turns the residual scalar mode into a sharply specified electrical
normal form.

## 6. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| Equality implies $`\kappa=0`$ | proved | Equation (EQ6.4) and the positive quadratic factor in K6. |
| Equality implies additive $`W`$ | proved | Paired Kalmanson inequalities force the half-turn average to be additive, then nonnegativity propagates all Kalmanson equalities to $`W`$. |
| Additive $`W`$ is star-equivalent | proved as a resistance-metric statement | It is exactly a star tree metric, with possible zero-pendant limiting cases. |
| Physical contact graph is a one-hub star | not proved | Electrical equivalence does not preserve the embedded unit-contact graph. |
| Equality is impossible in a triangle-free source | not proved | A new unit-contact/geometric argument is required. |
| C-I is closed | not proved | Support selection and finite integration remain. |

## 7. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| Circular-planar star response | yes | It is the additive equality model and satisfies (EQ6.3). |
| Half-turn-invariant regular hexagon | yes | It gives $`r_i=r_{i+3}=1/(2\beta_i)`$. |
| Non-half-turn-invariant response | yes | EQ6 allows unequal opposite pendant lengths with fixed pair sums. |
| C33 abstract sign-cone matrix | yes | It lacks the Kalmanson property needed for (EQ6.10). |
| Literal one-hub geometric realization | not asserted | It is a possible electrical representative, not a consequence about the source embedding. |

## 8. Failed routes and no-go results

### Star response as an immediate geometric contradiction

The theorem identifies star equivalence only at the boundary response level.
Replacing the actual network by a star would lose the unit-contact geometry and
is not a valid source-preserving operation.

### Strictness from equality classification alone

EQ6 does not show $`\rho_s<1`$. The circular-planar star remains an exact
equality model, so strictness must come from the actual unit-contact,
triangle-free, or global-minimality hypotheses.

## 9. Literature imported

No new literature is imported in this addendum. The only external input is the
Kalmanson theorem already audited in K6.

## 10. Computation and reproducibility

No computation is logically required. Equations (EQ6.6)-(EQ6.9) are finite
symbolic expansions, and (EQ6.10)-(EQ6.12) are elementary linear identities.

## 11. Canonical promotion recommendation

**Promote now — proof audited and frontier changes.**

Promote the equality classification into:

- docs/targets/target-c/01-force-hull-and-shear.md;
- docs/targets/target-c/README.md; and
- docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md.

## 12. Next run

Prove a source-preserving obstruction to the EQ6 star-equivalent response:
either a circular-planar network lemma that gives a common cut structure
in the actual contact graph, or a unit-contact geometric argument showing
that the resulting harmonic embedding forces a unit equilateral triangle.

In parallel, keep the support-selection issue separate; EQ6 is conditional on
the selected three-edge matching support.

## 13. Compact handoff

~~~text
LEVEL I STATUS: STILL OPEN.

Strongest new theorem:
In the convex six-endpoint three-edge matching, rho=1 forces every cyclic
Kalmanson defect to vanish and the effective-resistance metric to be additive:
  W_ij = r_i + r_j.
The opposite-pair sums satisfy
  r_i + r_{i+3} = 1/beta_i.
This is star equivalence at the boundary response level.

Exact endpoint now:
Rule out this additive response using the actual unit-contact geometry or
derive a same-diameter release; also solve direction-dependent support selection.

Binding regressions/no-go results:
A circular-planar star is an exact equality model. Electrical star equivalence
does not imply that the physical contact graph is literally a one-hub unit star.
C33 remains a sign-only regression outside the Kalmanson cone.

Highest-value next lemma:
Convert EQ6 star-equivalent response into a source-preserving common-cut or
unit-contact geometric contradiction.

Authoritative files:
docs/targets/target-c/README.md
docs/targets/target-c/01-force-hull-and-shear.md
docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md
~~~

<!-- theorem-state: {"artifact_id":"ART-E41D50702D72","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: equality forces concurrent diameter chords

**Date:** 2026-08-31  
**Repository state:** efceb54 (origin/main before this promotion)  
**Run type:** exact source-geometry consequence / C-I equality subcase  
**Target:** Target C Gate C-I, three-edge six-endpoint matching  
**Active prompt:** docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md  
**External web search:** not used beyond the already audited Kalmanson input  
**Computation:** not used in the proof

## LEVEL I STATUS

**STILL OPEN.**

EQ6 classifies the $\rho_s=1$ boundary response as an additive effective-resistance
metric. This addendum converts that response normal form into a source-preserving
geometric statement: the three selected matching chords must meet at one point
inside all three chords.

## 1. Starting endpoint

The K6 convex six-endpoint response closure gives $\rho_s\le1$. EQ6 gives, in
the equality case,

$$
W_{ij}=r_i+r_j,\qquad
r_i+r_{i+3}=\frac1{\beta_i}.
$$

The exact next implication is

$$
\rho_s=1
\ \Longrightarrow\
\text{the matching chords }p_ip_{i+3}\text{ are concurrent}.
$$

## 2. Strongest genuinely new audited theorem

### Theorem CONC6 (equality forces a common chord point)

Assume the hypotheses of K6 and EQ6. In particular, $B=(p_0,\ldots,p_5)$
is a strictly convex hexagon in cyclic order, the response is connected and
circular-planar, and

$$
H_s=\{03,14,25\}.
$$

If $\rho_s=1$, then all six additive parameters in EQ6 are strictly positive.
With

$$
g_i=\frac1{r_i},
\qquad
q=\frac{\sum_{i=0}^5 g_i p_i}{\sum_{i=0}^5 g_i},
$$

one has

$$
\boxed{
q\in\operatorname{relint}[p_i,p_{i+3}]
\qquad(i=0,1,2).
}
\tag{CONC6.1}
$$

Thus the three selected matching chords are concurrent at the weighted
boundary barycenter $q$.

### Scope

This is a statement about the actual C11 terminal coordinates and the actual
positive contact response. It does not replace the contact network by a
geometrically embedded star. It applies only to the selected three-edge
matching equality mode.

### Proof

EQ6 gives the additive resistance representation and

$$
r_i+r_{i+3}=\frac1{\beta_i}>0.
\tag{CONC6.2}
$$

Let $J=I-\mathbf1\mathbf1^{\mathsf T}/6$. For an additive resistance matrix
with zero diagonal,

$$
W_{ij}=r_i+r_j\quad(i\ne j),
$$

the centered resistance matrix is

$$
R=J\operatorname{diag}(r_0,\ldots,r_5)J.
\tag{CONC6.3}
$$

Since $\Lambda$ is the response of a connected network, $R=\Lambda^+$ is
positive definite on $\mathbf1^\perp$. If two of the $r_i$ were zero, then
$e_i-e_j\in\mathbf1^\perp$ would have zero quadratic form in (CONC6.3).
Therefore at most one $r_i$ can vanish.

We first exclude one zero. Suppose $r_z=0$. By (CONC6.2), $r_{z+3}>0$,
and all parameters in the other two matching pairs are positive. For positive
parameters, the response whose resistance metric is additive is the star
response

$$
\Lambda=\operatorname{diag}(g)
-\frac{gg^{\mathsf T}}{\sum_k g_k},
\qquad g_i=\frac1{r_i}.
\tag{CONC6.4}
$$

When $r_z\downarrow0$, this formula has a finite limit on the centered
subspace, with its weighted barycenter tending to $p_z$. Hence the C11
identity in the limit gives, for each $i\notin\{z,z+3\}$,

$$
g_i(p_i-p_z)=\beta_i(p_i-p_{i+3}).
\tag{CONC6.5}
$$

Equivalently,

$$
p_z=(1-\beta_i r_i)p_i+\beta_i r_i\,p_{i+3}.
\tag{CONC6.6}
$$

Both $r_i$ and $r_{i+3}$ are positive, and (CONC6.2) gives

$$
0<\beta_i r_i<1.
$$

Thus $p_z$ lies in the relative interior of the segment joining the two
other vertices $p_i$ and $p_{i+3}$. This contradicts strict convexity of the
hexagon, because $p_z$ is an extreme vertex distinct from both endpoints of
that segment. Therefore every $r_i>0$.

For positive $r_i$, the star response (CONC6.4) is the Moore--Penrose inverse
of (CONC6.3). Its action on the coordinate matrix is

$$
(\Lambda P_B)_i=g_i(p_i-q).
\tag{CONC6.7}
$$

The C11 identity gives, for $i=0,1,2$,

$$
g_i(p_i-q)=\beta_i(p_i-p_{i+3}).
\tag{CONC6.8}
$$

Therefore

$$
q=(1-\beta_i r_i)p_i+\beta_i r_i\,p_{i+3}.
\tag{CONC6.9}
$$

By (CONC6.2), both coefficients in (CONC6.9) are strictly between zero and
one. The same equation for $i+3$ is consistent because

$$
\beta_i r_i+\beta_i r_{i+3}=1.
$$

Hence (CONC6.1) holds for all three matching pairs. $\square$

## 3. Exact target implication

The equality mode is now source-geometrically restricted:

$$
\rho_s=1
\quad\Longrightarrow\quad
\text{three pairwise crossing diameter chords concur at an interior point}.
$$

Consequently, any independent geometric theorem excluding concurrent selected
diameter matchings in the relevant global-minimizer class would make the K6
response inequality strict in that class. The theorem also supplies the exact
point $q$ and its stress-dependent barycentric representation.

This still does not close C-I. Concurrent diameter matchings are not excluded
by the current canonical stack; the support-selection problem also remains.

## 4. Dependencies

- docs/reports/target_c_six_matching_equality_star_2026-08-31.md, Theorem EQ6:
  additive resistance metric and opposite-pair parameter sums.
- docs/reports/target_c_convex_six_matching_kalmanson_2026-08-31.md, Theorem K6:
  the six-endpoint response inequality and C11 response-block setting.
- docs/reports/target_c_force_polygon_2026-08-30.md, Theorem C11:
  $\Lambda P_B=L_{H_s}P_B$ for the actual positive contact response.

No physical one-hub replacement of the contact graph is used; (CONC6.4) is
only the exact boundary response associated with the additive resistance
metric.

## 5. Why it is new

EQ6 stopped at an electrical normal form. CONC6 pushes that form through the
actual coordinate identity and obtains a concrete concurrency condition in the
source geometry, including strict interiority and a stress-dependent division
ratio on each chord.

## 6. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| All additive parameters are positive | proved | Connectedness rules out two zeros; one zero contradicts strict convexity through the limiting C11 identity. |
| Additive response has star form | proved | It is the inverse of the centered diagonal form (CONC6.3), first for positive parameters and then by a centered limit. |
| C11 forces chord concurrency | proved | Equation (CONC6.8) places the same barycenter $q$ in every matching segment. |
| Concurrent matching is impossible globally | not proved | The current Target C stack does not exclude it. |
| Physical contact graph is a literal star | not proved and not used | Electrical response equivalence does not preserve the embedded unit-contact graph. |
| C-I is closed | not proved | Support selection and the remaining global equality geometry remain. |

## 7. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| Regular centrally symmetric matching | yes | $q$ is the center and lies in all three opposite chords. |
| Unequal positive matching weights | yes | The ratios $\beta_i r_i$ may differ, but remain in $(0,1)$. |
| A single zero pendant parameter | excluded | It would put an extreme terminal vertex in the interior of a segment joining two other hull vertices. |
| Two zero pendant parameters | excluded | It creates a nonzero zero mode of $R$ on $\mathbf1^\perp$. |
| Nonconcurrent convex matching | equality excluded | It cannot satisfy (CONC6.1), though it may still have $\rho_s<1$. |

## 8. Failed routes and no-go results

### Replacing the source by a star graph

The star formula is used only to identify the boundary response matrix forced by
the additive resistance metric. It does not alter the source graph or preserve
unit-edge geometry under arbitrary electrical reductions.

### Declaring strict K6 inequality

CONC6 gives a necessary concurrency condition for equality, not an exclusion.
The regular hexagon is a compatible response geometry, so a new
triangle-free/unit-contact or global-minimality argument is required.

## 9. Literature imported

No new literature is imported. The electrical inversion used in (CONC6.4) is
an elementary calculation from the additive resistance matrix; the
circular-planar Kalmanson theorem was already audited in K6.

## 10. Computation and reproducibility

No computation is logically required. The identities (CONC6.3)-(CONC6.9) are
direct matrix calculations and the only geometric input is strict convexity.

## 11. Canonical promotion recommendation

**Promote now — proof audited and frontier changes.**

Promote the theorem into:

- docs/targets/target-c/01-force-hull-and-shear.md;
- docs/targets/target-c/README.md; and
- docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md.

## 12. Next run

Use the common point $q$ as the next geometric variable. The highest-value
lemma is an exact obstruction to three concurrent diameter chords in a
triangle-free global minimizer, or an argument that CONC6 equality forces a
unit equilateral triangle in the actual contact embedding.

## 13. Compact handoff

~~~text
LEVEL I STATUS: STILL OPEN.

Strongest new theorem:
In the convex six-endpoint equality mode rho=1, EQ6 plus C11 forces every
additive pendant parameter positive and places the weighted barycenter
  q = (sum_i p_i/r_i)/(sum_i 1/r_i)
strictly inside all three matching chords [p_i,p_(i+3)].
The three selected diameter chords are concurrent.

Exact endpoint now:
Exclude this concurrent equality geometry using the actual unit-contact or
global-minimality hypotheses, and separately solve direction-dependent support
selection.

Binding regressions/no-go results:
Electrical star equivalence is not a literal one-hub unit framework. The regular
concurrent matching is a compatible response geometry, so strictness is not
automatic.

Highest-value next lemma:
Turn concurrent equal-diameter chords into a unit-equilateral or other
source-preserving contradiction.

Authoritative files:
docs/targets/target-c/README.md
docs/targets/target-c/01-force-hull-and-shear.md
docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md
~~~

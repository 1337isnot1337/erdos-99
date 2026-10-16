# Target C: generic H6 ground-coupled affine reduction

Date: 2026-09-19

Scope: the degree-pure support-seven generic `H6` branch, with reciprocal vertices `0,1,...,5` forming a strict convex hexagon, reciprocal ground vertex `0`, reciprocal vertices `6,7` strict interior, and no collinear reciprocal triple.

This note continues the exact generic-H6 census after the interior force/chirotope reduction.  The input is

\[
14{,}174=10{,}670\ C_7+3{,}504\ (C_3\sqcup C_4)
\]

labelled cells.  The new affine layer excludes 7,866 of them and leaves

\[
\boxed{6{,}308=4{,}936\ C_7+1{,}372\ (C_3\sqcup C_4).}
\]

The verifier is

`research/verify_target_c_support7_h6_ground_coupled_affine_reduction_2026_09_19.py`.

It rebuilds the 14,174 input cells, reconstructs the complete signed force cyclic order at every non-ground physical pentagon, constructs the affine systems below, asks a numerical LP solver only for candidate dual supports, then verifies every accepted dual identity exactly over `fractions.Fraction`.  No cell is excluded from a floating-point inequality alone.

## 1. Non-ground pentagon variables

For each non-ground reciprocal vertex \(v\in\{1,\ldots,7\}\), write

\[
x_{v,0},\ldots,x_{v,4}
\]

for the five consecutive force-direction gaps divided by \(\pi\), in the unique force cyclic order recovered from the signed reciprocal chirotope.  The previously proved physical pentagon theorem gives

\[
\sum_{k=0}^4 x_{v,k}=2
\]

and the five strict simplex inequalities

\[
q_{v,k}:=x_{v,k}+x_{v,k+1}-x_{v,k+3}>\frac13,
\qquad k\pmod 5.
\]

Thus the seven non-ground pentagons contribute 35 strict affine facets.

For two present reciprocal rays \(va,vb\), the reciprocal interior angle at \(v\), divided by \(\pi\), is an integer-affine function of the five \(x_{v,k}\).  The formula depends only on the force arc from \(a\) to \(b\), the two edge signs, and \(\chi(v,a,b)\).  Explicitly, if \(A\) is the normalized CCW force arc, then the raw reciprocal angle is one of

\[
A,\qquad 2-A,\qquad A-1,\qquad 1-A,
\]

with the case fixed by those exact signs.  This is the same audited conversion used in the preceding `H7b` and generic-`H6` triangle/simplex reductions.

Every present reciprocal triangle among vertices \(1,\ldots,7\) therefore gives one exact affine equation saying that its three normalized interior angles sum to 1.  There are seven such triangles for a `C7` missing graph and six for a `C3+C4` missing graph.

The non-ground-only version of this relaxation already gives an exact intermediate reduction

\[
14{,}174\longrightarrow10{,}490
\]

by 2,072 distinct exact Farkas certificates, excluding 3,684 labelled cells.  Of those, 2,952 cells already fail a single-triangle lower-bound test over the closed local pentagon simplices.

## 2. Put the reciprocal ground geometry back in

The earlier `H6` ground theorem gives more structure that the non-ground-only relaxation does not use.

Let the seven raw reciprocal rays from ground vertex 0 occur in the strict certified order

\[
r_1,r_2,\ldots,r_7.
\]

Introduce six normalized consecutive ground gaps

\[
g_p=\frac{\angle(r_p,r_{p+1})}{\pi},
\qquad p=1,\ldots,6.
\]

The generic order and the `H6` cone-width theorem give the strict inequalities

\[
g_p>0
\]

and

\[
\sum_{p=1}^6 g_p<\frac23.
\]

Because the entire ground cone has width less than \(2\pi/3<\pi\), the ordinary interior angle at 0 between any two ground rays is simply the sum of the consecutive \(g_p\)'s between their positions in this linear order.  No wraparound ambiguity is possible.

Now let \(ab\) be a present non-ground relation edge.  Both reciprocal rays \(a0,ab\) occur among the five force-support rays at \(a\), and similarly at \(b\).  Hence the two non-ground interior angles of Euclidean triangle \(0ab\) are exact affine functions of the pentagon turn variables.  If

\[
G_{ab}
\]

denotes the corresponding ground-gap sum, then triangle \(0ab\) gives the exact equation

\[
\boxed{
G_{ab}+A_{a;0b}+A_{b;0a}=1.
}
\]

The non-ground relation graph has 14 present edges, so this supplies 14 additional affine equations in every cell.

The complete strict-facet family used in the new reduction is therefore

\[
q_{v,k}-\frac13>0
\]

for the 35 pentagon facets,

\[
g_p>0
\]

for the six ground-order gaps, and

\[
\frac23-\sum_{p=1}^6 g_p>0
\]

for the `H6` cone width.

## 3. Exact Farkas certificate form

Write all equality constraints as

\[
E_r(z)=b_r
\]

and every strict facet as

\[
f_j(z)=c_j+a_j\cdot z>0,
\]

where \(z\) consists of the 35 non-ground pentagon turns and the six ground gaps.

A certificate consists of coefficients

\[
\lambda_j\ge0,
\qquad
\sum_j\lambda_j=1,
\]

and arbitrary equality multipliers \(\mu_r\) satisfying the exact coefficient identity

\[
\sum_j\lambda_j a_j+
\sum_r\mu_r E_r=0.
\]

On the equality space, this forces

\[
\sum_j\lambda_j f_j(z)
=
\sum_j\lambda_jc_j-
\sum_r\mu_rb_r
=:\kappa.
\]

If \(\kappa\le0\), the cell is impossible because every \(f_j(z)\) is strictly positive while a nonnegative convex combination of them is forced to be nonpositive.

The committed verifier uses HiGHS dual simplex only to propose a support and approximate dual coefficients.  It converts every proposed coefficient to a rational number, then checks all 41 variable coefficients, nonnegativity, the normalization \(\sum\lambda_j=1\), and \(\kappa\le0\) exactly.  Failure of any exact check means no exclusion is recorded.

## 4. Census

Among the 14,174 input cells there are 9,038 distinct extended affine systems.

Exact certificates are found and verified for 5,854 of those systems.  At the labelled-cell level this excludes

\[
\boxed{7{,}866=5{,}734\ C_7+2{,}132\ (C_3\sqcup C_4).}
\]

The exact certificate constants split as follows:

- 5,256 labelled cells have boundary certificates with \(\kappa=0\);
- 2,610 labelled cells have strict certificates with \(\kappa<0\).

At the distinct-system level the split is 3,576 boundary certificates and 2,278 strict negative certificates.  The exact rational dual coefficients found in this run have denominator at most 231.

The ground-coupled system contains every one of the 3,684 exclusions from the non-ground-only affine layer and adds exactly

\[
\boxed{4{,}182}
\]

new labelled-cell exclusions.

The final generic-H6 census after this layer is

\[
\boxed{6{,}308=4{,}936\ C_7+1{,}372\ (C_3\sqcup C_4).}
\]

There are 3,184 distinct surviving extended affine systems: 2,276 of type `C7` and 908 of type `C3+C4`.

The surviving labelled cells by normalized ground sign pattern are

| pattern | survivors |
|---|---:|
| `145` | 12 |
| `156` | 16 |
| `235` | 830 |
| `236` | 1,726 |
| `237` | 16 |
| `245` | 558 |
| `256` | 1,726 |
| `345` | 24 |
| `346` | 558 |
| `347` | 12 |
| `356` | 830 |

Patterns `234` and `456` had already been eliminated by the preceding interior-force/chirotope layer.

## 5. What this does and does not prove

This is a necessary-condition reduction.  It does not prove that any of the remaining 6,308 cells is geometrically realizable.

Conversely, any further obstruction that is only a linear consequence of the equations and strict facets included above is already visible to this affine feasibility problem.  The remaining cells have positive numerical margin in this relaxation; that numerical observation is not promoted to a theorem, but it identifies the next useful layer.

The natural next constraints are nonlinear and metric.  For every present relation edge \(ij\), triangle \(0ij\) gives the radius ratio

\[
\frac{\rho_j}{\rho_i}
=
\frac{\sin A_{i;0j}}{\sin A_{j;0i}},
\]

so the logarithmic sine ratios must sum to zero around each relation-graph cycle.  The support-seven relation graph has cycle rank 8.  Those eight sine-cycle identities couple different pentagons in a way the affine relaxation cannot express.  They should be combined with the actual nonlinear equilateral-pentagon vector-closure equations on the 3,184 surviving affine systems.

Reciprocal-collinearity walls remain outside this generic calculation and still require a separate branch.

# Target C-II — complete metric integrability for generic support-seven `H6`

**Date:** 2026-09-19  
**Status:** exact structural reduction; theorem-state authority unchanged  
**Scope:** the degree-pure support-seven generic `H6` branch, with reciprocal hull `0,1,...,5`, reciprocal interior vertices `6,7`, and no collinear reciprocal triple  
**Certificate:** `research/verify_target_c_support7_h6_complete_metric_integrability_2026_09_19.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current generic-`H6` affine endpoint has 6,308 labelled cells after the ground-coupled angle/simplex reduction. The next nonlinear metric layer was previously phrased using the eight sine-cycle conditions of the 14-edge present relation graph. That is not the full metric information available in a generic reciprocal configuration.

The reciprocal contains eight geometric points whether or not a pair is a relation edge. Once the complete angular data of those eight points is introduced, metric consistency is governed by the complete graph on the seven non-ground reciprocal vertices. Its cycle rank is fifteen. Thus generic `H6` has seven additional independent sine-law consistency conditions beyond the relation-only eight.

The fifteen conditions are also sufficient, together with the complete angular equations, to reconstruct one common reciprocal coordinate configuration up to Euclidean similarity.

## 1. Exact complete-angle affine lift

Fix one generic `H6` oriented-matroid cell. Its chirotope determines the circular order of the seven rays from every reciprocal vertex.

At each hull vertex `v=0,...,5`, all seven other points lie in the strict interior wedge at `v`. Introduce six positive normalized consecutive ray gaps

\[
h_{v,1},\ldots,h_{v,6}>0.
\]

For the ground vertex `0`, the already proved `H6` cone bound gives

\[
\sum_{p=1}^6 h_{0,p}<\frac23.
\tag{1.1}
\]

For the other five hull vertices, strict convexity gives

\[
\sum_{p=1}^6 h_{v,p}<1.
\tag{1.2}
\]

At each interior reciprocal vertex `v=6,7`, introduce seven positive cyclic gaps

\[
h_{v,1},\ldots,h_{v,7}>0,
\qquad
\sum_{p=1}^7 h_{v,p}=2.
\tag{1.3}
\]

The chirotope selects, for every ordered pair of rays from an interior vertex, which cyclic arc is the ordinary angle. Genericity requires that selected arc to lie strictly between `0` and `1`.

Therefore every ordinary reciprocal angle

\[
A_{v;ab}:=\frac1\pi\angle avb
\qquad(a,b\ne v)
\]

is an exact integer-affine function of the `h` variables, with

\[
0<A_{v;ab}<1.
\]

For every reciprocal triple `{a,b,c}` the Euclidean triangle identity gives

\[
\boxed{
A_{a;bc}+A_{b;ac}+A_{c;ab}=1.
}
\tag{1.4}
\]

There are `C(8,3)=56` such exact affine equations.

Now include the seven non-ground physical force pentagons. Let

\[
x_{v,0},\ldots,x_{v,4}
\]

be their normalized consecutive signed-force gaps. The existing local theorem gives

\[
\sum_{k=0}^4 x_{v,k}=2,
\qquad
x_{v,k}+x_{v,k+1}-x_{v,k+3}>\frac13.
\tag{1.5}
\]

For each non-ground vertex `v`, exactly five reciprocal rays correspond to present support edges. Their complete edge-sign assignment and reciprocal chirotope determine the signed force cyclic order. Hence for every pair of those five present rays, the raw reciprocal angle is an exact integer-affine function of the five `x_{v,k}`: it is an appropriate force arc, its complement, or that arc shifted by one half-turn according to the two edge signs. Equating that expression to the corresponding `A_{v;ab}` ties the force variables to the complete reciprocal angular variables.

Thus every generic `H6` realization lies in an explicit rational affine strict polyhedron with

- 35 force-turn variables;
- 36 hull-ray gap variables;
- 14 interior-ray gap variables;
- 85 variables in total;
- seven force turn-sum equations;
- two interior full-circle equations;
- 70 present-ray angle-tie equations;
- 56 complete reciprocal triangle equations;
- the existing strict force-turn facets, ray-order positivity, hull-span bounds, and interior chirotope angle bounds.

This is a necessary affine lift. It is stronger than the current ground-coupled system because (1.4) includes triangles and ray angles involving missing relation edges. It is not by itself a metric realization theorem: triangle angle sums do not enforce globally consistent radial lengths.

## 2. Complete sine-law cochain

For distinct non-ground vertices `i,j in {1,...,7}`, define

\[
A_{ij}:=\angle 0ij.
\]

All these angles lie strictly in `(0,pi)` in a generic cell. If

\[
\rho_i=|y_i-y_0|>0
\]

are the reciprocal radii, then the law of sines in triangle `0ij` gives

\[
\boxed{
\frac{\rho_j}{\rho_i}
=
\frac{\sin A_{ij}}{\sin A_{ji}}.
}
\tag{2.1}
\]

Define the antisymmetric edge cochain

\[
g_{ij}
=
\log\sin A_{ij}-\log\sin A_{ji}.
\tag{2.2}
\]

A common reciprocal metric exists only if

\[
g_{ij}=\log\rho_j-\log\rho_i,
\]

so `g` must be exact on the complete graph `K_7`.

Choose the star spanning tree rooted at vertex `1`. The fifteen non-tree edges are the pairs

\[
2\le i<j\le7.
\]

Their fundamental cycles are the root-fan triangles `1-i-j-1`. Exactness is therefore equivalent to

\[
\boxed{
g_{1i}+g_{ij}+g_{j1}=0}
\qquad(2\le i<j\le7),
\tag{2.3}
\]

or, without logarithms,

\[
\boxed{
\sin A_{1i}\,\sin A_{ij}\,\sin A_{j1}
=
\sin A_{i1}\,\sin A_{ji}\,\sin A_{1j}
}
\qquad(2\le i<j\le7).
\tag{2.4}
\]

There are exactly fifteen independent equations.

The exact graph certificate checks all 465 labelled support-seven missing graphs: 360 Hamiltonian `C7` graphs and 105 `C3+C4` graphs. In every case the present non-ground relation graph has 14 edges, is connected, and has cycle rank

\[
14-7+1=8.
\]

Completing its seven missing edges gives `K_7`, whose cycle rank is

\[
21-7+1=15.
\]

Hence

\[
\boxed{15=8+7.}
\tag{2.5}
\]

The seven missing reciprocal pairs contribute seven independent metric conditions that are invisible to a relation-edge-only sine-cycle calculation.

## 3. Sufficiency for common reciprocal-coordinate reconstruction

Assume the complete affine angular equations from Section 1 and all fifteen identities (2.4).

The positive ground ray gaps determine the seven ray directions from `0` up to a common rotation. Write these directions as

\[
\phi_1,\ldots,\phi_7.
\]

Set

\[
\rho_1=1,
\qquad
\rho_i=\frac{\sin A_{1i}}{\sin A_{i1}}
\quad(i=2,\ldots,7).
\tag{3.1}
\]

Every factor is positive. Equation (2.3) then gives, for every pair `i,j`,

\[
\boxed{
\frac{\rho_j}{\rho_i}
=
\frac{\sin A_{ij}}{\sin A_{ji}}.
}
\tag{3.2}
\]

Define coordinates

\[
y_0=0,
\qquad
y_i=\rho_i(\cos\phi_i,\sin\phi_i).
\tag{3.3}
\]

For triangle `0ij`, let the prescribed angle at `0` be `G_{ij}`. The complete triangle equations give

\[
A_{ij}+A_{ji}=\pi-G_{ij}=:S_{ij},
\qquad 0<S_{ij}<\pi.
\tag{3.4}
\]

For fixed `S in (0,pi)`, the function

\[
f(a)=\frac{\sin a}{\sin(S-a)}
\qquad(0<a<S)
\]

is strictly increasing because

\[
\frac{d}{da}\log f(a)
=
\cot a+\cot(S-a)
=
\frac{\sin S}{\sin a\sin(S-a)}>0.
\tag{3.5}
\]

The coordinate triangle from (3.3) has included angle `G_ij` at `0` and radial ratio `rho_j/rho_i`. By (3.2), that ratio is exactly the prescribed sine ratio. Strict monotonicity in (3.5) therefore forces its other two angles to be precisely `A_ij` and `A_ji`.

This holds for every pair `i,j`. Consequently (3.3) realizes all prescribed complete triangle angles and all ray orders. Therefore:

\[
\boxed{
\text{complete angular feasibility + the fifteen equations (2.4)}
\iff
\text{one common generic reciprocal metric, up to similarity}.
}
\tag{3.6}
\]

The reverse implication is just the law of sines in the realized triangles.

## 4. Consequence for the current `H6` endpoint

The 6,308-cell generic `H6` endpoint should no longer be attacked with only the eight relation-graph sine cycles. A stronger exact route is now available:

1. lift each surviving oriented-matroid cell to the complete 85-variable affine angular system of Section 1;
2. eliminate any cell whose complete affine lift is already empty by exact Farkas certificates;
3. on the affine survivors, impose the fifteen root-fan equations (2.4), not only the eight present-edge cycle equations;
4. intersect those metric equations with the seven exact equilateral-pentagon closure conditions.

Step 2 is entirely rational linear algebra. Steps 3-4 are the remaining nonlinear core. The fifteen-equation theorem means that a zero of that nonlinear system is already sufficient for common reciprocal-coordinate reconstruction; there is no additional hidden metric-gluing condition afterward.

Reciprocal-collinearity walls remain outside this generic argument and require a separate branch. No theorem-state file is changed. C-II remains open.

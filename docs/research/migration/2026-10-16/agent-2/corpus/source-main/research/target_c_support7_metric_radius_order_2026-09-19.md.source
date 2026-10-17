# Target C support-seven: metric radius-order obstruction

Date: 2026-09-19

Status: exact structural necessary condition for every generic support-seven reciprocal realization. The theorem-state authority is unchanged. C-II remains open.

## Result

Let `0` be the ground reciprocal point and let `1,...,7` be the seven non-ground reciprocal points. For distinct `i,j` define

\[
A_{ij}=\angle 0ij,
\qquad
\rho_i=|y_i-y_0|>0,
\]

and the antisymmetric angle difference

\[
D_{ij}=A_{ij}-A_{ji}.
\]

Then every genuine reciprocal metric satisfies the exact sign identity

\[
\boxed{
\operatorname{sgn}D_{ij}=\operatorname{sgn}(\rho_j-\rho_i).
}
\tag{1}
\]

Thus the signs of the 21 affine quantities `D_ij` cannot be an arbitrary tournament or signed complete graph. They must be the comparison signs of seven positive scalars. Equivalently, they form a total preorder on the seven reciprocal radii.

In particular:

- no strict directed triangle can occur;
- if `D_ij=0`, then `rho_i=rho_j`, so `i` and `j` must have identical comparisons with every third vertex;
- when all seven radii are distinct, the 21 signs come from one of only `7! = 5040` total orders;
- allowing equal radii gives exactly `47293` weak orders on seven labelled elements;
- every weak order is contained in at least one of the 5040 closed total-order cones, so the nonlinear metric system admits a finite 5040-way linear outer disjunction before any sine magnitudes are used.

This gives a new exact affine obstruction that sits strictly before the fifteen nonlinear sine-law cycle identities.

## Proof of the pairwise sign identity

In triangle `0ij`, the law of sines gives

\[
\frac{\rho_j}{\rho_i}
=
\frac{\sin A_{ij}}{\sin A_{ji}}.
\tag{2}
\]

Let

\[
G_{ij}=\angle i0j.
\]

Genericity gives `0<G_ij<pi`, and the triangle angle sum gives

\[
A_{ij}+A_{ji}=\pi-G_{ij}<\pi.
\tag{3}
\]

Both `A_ij` and `A_ji` lie in `(0,pi)`. Therefore

\[
\sin A_{ij}-\sin A_{ji}
=
2\cos\!\left(\frac{A_{ij}+A_{ji}}2\right)
 \sin\!\left(\frac{A_{ij}-A_{ji}}2\right).
\tag{4}
\]

By (3), the cosine factor in (4) is strictly positive. Since

\[
-\pi<A_{ij}-A_{ji}<\pi,
\]

the sine factor has the same sign as `A_ij-A_ji`. Hence

\[
\operatorname{sgn}(\sin A_{ij}-\sin A_{ji})
=
\operatorname{sgn}(A_{ij}-A_{ji}).
\tag{5}
\]

The denominator `sin A_ji` in (2) is positive, so

\[
\operatorname{sgn}\!\left(\frac{\rho_j}{\rho_i}-1\right)
=
\operatorname{sgn}(\sin A_{ij}-\sin A_{ji}).
\tag{6}
\]

Finally `rho_i>0`, so the left side of (6) has the same sign as `rho_j-rho_i`. Combining (5) and (6) proves (1).

No approximation, convexity estimate, or numerical trigonometry enters this argument.

## Total-preorder consequence

Define

\[
i\preceq j\quad\Longleftrightarrow\quad D_{ij}\ge0.
\]

By (1), this is exactly

\[
\rho_i\le\rho_j.
\]

Therefore `preceq` is a total preorder. Its strict part is transitive, and equality of radii is an equivalence relation.

For any three distinct labels `i,j,k`, the cyclic sign configuration

\[
D_{ij}>0,
\qquad
D_{jk}>0,
\qquad
D_{ki}>0
\tag{7}
\]

would imply

\[
\rho_i<\rho_j<\rho_k<\rho_i,
\]

which is impossible. The reversed strict cycle is equally impossible.

Ties also propagate. For example,

\[
D_{ij}=0
\]

forces `rho_i=rho_j`, and therefore for every `k`

\[
\operatorname{sgn}D_{ik}
=
\operatorname{sgn}D_{jk}.
\tag{8}
\]

So checking only absence of strict directed triangles is sufficient in the no-tie case, but tie-consistency must also be enforced on boundary cells.

## Linear order cones

On a fixed generic `H6` complete-angle cell, every `A_ij` is an integer-affine function of the 85 angle variables. Therefore every

\[
D_{ij}=A_{ij}-A_{ji}
\]

is affine as well.

For a permutation

\[
\pi=(\pi_1,\ldots,\pi_7),
\]

define its closed radius-order cone by the 21 inequalities

\[
D_{\pi_a\pi_b}\ge0
\qquad(1\le a<b\le7).
\tag{9}
\]

If a metric realization has

\[
\rho_{\pi_1}\le\rho_{\pi_2}\le\cdots\le\rho_{\pi_7},
\]

then (1) places its angle vector in this cone. Every weak radius order has at least one linear extension, so all metric realizations lie in the union of the 5040 cones (9).

Consequently, for any affine/physical branch:

\[
\boxed{
\text{if all 5040 closed radius-order cones are impossible, then the branch is metrically impossible.}
}
\tag{10}
\]

The important point is that (10) is still a rational linear-disjunctive problem. It can be attacked with the same exact Farkas machinery already used for pentagon branch cones. The nonlinear sine products are not needed to obtain this first metric cut.

A cheaper first pass is to certify signs of selected `D_ij`. If exact affine certificates force a strict directed triangle as in (7), the cell is immediately excluded without enumerating radius orders.

## Finite combinatorics

There are `7! = 5040` strict total orders. Allowing ties gives the ordered Bell number

\[
\boxed{47293}
\]

weak orders on seven labelled elements. A weak order is an ordered partition into nonempty equal-radius blocks.

The companion verifier enumerates all canonical rank vectors on seven labels, confirms the count `47293`, confirms that exactly `5040` have seven distinct levels, checks that every weak order has a total-order linear extension, and checks the induced pair-sign convention.

Certificate: `research/verify_target_c_support7_metric_radius_order_2026_09_19.py`.

## Next computational target

For the current generic-H6 survivors, use the complete-angle affine system to test the closed halfspaces `D_ij<=0` and `D_ij>=0` with exact rational Farkas certificates. Any three forced comparisons forming a directed cycle eliminate the cell immediately. For the remaining cells, branch over radius orders with partial-order pruning rather than solving 5040 independent LPs from scratch.

This obstruction is only necessary. A transitive radius order does not imply the fifteen sine-law identities; it retains only their pairwise sign content. Cells surviving the order layer still require the full metric equations and the seven equilateral-pentagon closures.

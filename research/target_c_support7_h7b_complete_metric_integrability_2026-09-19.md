<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "ba5d0c4ad4f51306b549cac058ea2b0058bbf16c", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_h7b_complete_metric_integrability_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "3f591e73ac35c4ecbe5e6b86f4163b89b26aa2e58b3b06c1c307db4472f3b846"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — complete metric integrability for the 27 generic H7b survivors

**Date:** 2026-09-19  
**Claim class:** exact nonlinear reduction inside generic interior-ground `H7b`  
**Input endpoint:** 27 affine `C7` cells from the repaired full-angle reduction  
**Certificate:** `research/verify_target_c_support7_h7b_complete_metric_integrability_2026_09_19.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The full-angle reduction leaves 27 necessary affine cells. Its endpoint description still listed three nonlinear tasks separately: relation-edge law-of-sines integrability, common reciprocal-coordinate reconstruction, and ground force closure. Two of those tasks can be removed, and the metric layer must be strengthened from 8 relation-cycle equations to 15 complete-graph cycle equations.

## 1. Every hull pair gives a radial ratio, including missing relation edges

Work in one generic `H7b` cell. The reciprocal ground is

\[
y_0=0,
\]

and `y_1,...,y_7` form a strict convex heptagon containing the origin. For every ordered pair of distinct hull vertices `i,j`, let

\[
A_{ij}\in(0,\pi)
\]

be the ordinary interior angle at `y_i` of triangle `0ij`, between rays `i0` and `ij`. The full-angle affine system already determines each `A_ij` as an affine function of its raw angular gaps, even when `ij` is a missing relation edge.

Put

\[
\rho_i=|y_i|>0.
\]

The sine law in triangle `0ij` gives

\[
\boxed{
\frac{\rho_j}{\rho_i}
=
\frac{\sin A_{ij}}{\sin A_{ji}}.
}
\tag{1.1}
\]

Define the antisymmetric edge cochain on the complete graph `K7`

\[
g_{ij}
:=
\log\sin A_{ij}-\log\sin A_{ji}.
\tag{1.2}
\]

For an actual reciprocal,

\[
g_{ij}=\log\rho_j-\log\rho_i,
\tag{1.3}
\]

so `g` must be exact on all 21 hull-pair edges, not merely on the 14 present relation edges.

## 2. The complete metric layer has 15 independent cycle equations

The cycle rank of `K7` is

\[
21-7+1=15.
\]

A convenient basis is given by the fifteen root-fan triangles

\[
(1,i,j),
\qquad 2\le i<j\le7.
\]

Thus complete radial integrability is equivalent to

\[
\boxed{
g_{1i}+g_{ij}+g_{j1}=0}
\qquad(2\le i<j\le7),
\tag{2.1}
\]

or, without logarithms,

\[
\boxed{
\sin A_{1i}\,\sin A_{ij}\,\sin A_{j1}
=
\sin A_{i1}\,\sin A_{ji}\,\sin A_{1j}.
}
\tag{2.2}
\]

There are exactly fifteen independent equations of this form.

For every surviving generic `H7b` state, the missing relation graph is a Hamiltonian `C7`. Hence the present non-ground relation graph has 14 edges. It is connected, so its cycle rank is

\[
14-7+1=8.
\]

The previously identified relation-only sine layer therefore checks only eight independent cycle conditions.

Fix any spanning tree `T` of the 14-edge present graph. The eight present non-tree edges give eight fundamental cycles. Add the seven missing `C7` edges one at a time to `T`. Each produces another fundamental cycle containing a missing-edge coordinate that appears in none of the relation cycles and in none of the other six missing-edge fundamental cycles. Therefore these seven cycles are independent modulo the relation-cycle space.

Consequently

\[
\boxed{15=8+7.}
\tag{2.3}
\]

The exact certificate checks this rank statement for all 360 undirected Hamiltonian `C7` missing graphs and independently verifies rank 15 for the root-fan triangle basis.

## 3. The fifteen equations are sufficient for common reciprocal-coordinate reconstruction

The complete sine-cycle system is stronger than a list of necessary radius identities. Under the already-imposed generic full-angle equations, it is sufficient to reconstruct one common reciprocal metric, up to Euclidean similarity.

Let the positive ground angular gaps determine the cyclic ray directions

\[
\phi_1,\ldots,\phi_7
\]

up to a common rotation. Set `phi_1=0`. The ground chirotope inequalities in the affine cell ensure that, for each pair `i,j`, the smaller included angle between rays `0i` and `0j` is exactly the prescribed triangle angle

\[
G_{ij}\in(0,\pi).
\]

Assume the fifteen root-fan equations (2.1). Set

\[
\rho_1=1,
\qquad
\rho_i=\frac{\sin A_{1i}}{\sin A_{i1}}
\quad(i=2,\ldots,7).
\tag{3.1}
\]

Equation (2.1) then gives, for every pair `i,j`,

\[
\frac{\rho_j}{\rho_i}
=
\frac{\sin A_{ij}}{\sin A_{ji}}.
\tag{3.2}
\]

Define

\[
y_i=\rho_i(\cos\phi_i,\sin\phi_i).
\tag{3.3}
\]

It remains to check that these coordinates realize the prescribed non-ground triangle angles, rather than merely their sine ratios. The full affine triangle equations already give

\[
A_{ij}+A_{ji}=\pi-G_{ij}=:S_{ij},
\qquad 0<S_{ij}<\pi.
\tag{3.4}
\]

For fixed `S` in `(0,pi)`, define

\[
f(a)=\frac{\sin a}{\sin(S-a)},
\qquad 0<a<S.
\]

Then

\[
\frac{d}{da}\log f(a)
=
\cot a+\cot(S-a)
=
\frac{\sin S}{\sin a\,\sin(S-a)}>0.
\tag{3.5}
\]

Thus `f` is strictly increasing. For a fixed included ground angle `G_ij` and fixed positive radial ratio `rho_j/rho_i`, there is at most one pair of positive triangle angles summing to `S_ij=pi-G_ij` with the required sine ratio. The coordinate triangle from (3.3) has the same included angle and the same radial ratio, so its two remaining angles must equal `A_ij,A_ji`.

Therefore the coordinates (3.3) realize every prescribed triangle angle and hence every full raw-ray direction. No additional common-coordinate reconstruction constraint remains after the fifteen complete sine-cycle equations.

## 4. Ground force closure is redundant after the seven pentagon closures

For every present reciprocal edge `ij`, let `s_ij` be its common edge sign and define its signed unit contribution at `i` by

\[
f_{ij}
=
s_{ij}\frac{y_j-y_i}{|y_j-y_i|}.
\]

Then

\[
f_{ji}=-f_{ij}.
\]

Let

\[
F_i=\sum_{j:ij\text{ present}} f_{ij}.
\]

Summing over all eight reciprocal vertices cancels every edge contribution pairwise:

\[
\sum_{i=0}^{7}F_i=0.
\tag{4.1}
\]

At each non-ground hull vertex there are five present edges, so `F_i=0` is exactly its equilateral force-pentagon vector-closure condition. Hence

\[
F_1=\cdots=F_7=0
\quad\Longrightarrow\quad
F_0=0.
\tag{4.2}
\]

The seven-force ground closure is therefore automatic once a common reciprocal metric exists and all seven non-ground pentagons close. It should not be treated as an additional independent nonlinear target.

## 5. Sharpened finite endpoint

For each of the 27 surviving generic `H7b` cells, the affine equality space has exact dimension 27. The remaining metric/force problem can now be posed without auxiliary radius variables or reciprocal coordinates:

1. impose the fifteen complete-`K7` sine-cycle equations (2.2);
2. impose the seven non-ground equilateral-pentagon vector closures, i.e. fourteen scalar real equations.

The raw angles entering both systems are already affine functions of the 27-dimensional equality cell variables. The strict inequalities from the full-angle reduction remain in force.

This is a system of 29 scalar nonlinear equations on a 27-dimensional affine space, but **the equation count is not a proof of emptiness**. Independence or transversality has not been established, and hidden algebraic dependencies are possible. No dimension-count exclusion is claimed.

The practical gain is exact: the old eight-cycle relation-only metric layer was incomplete by seven independent conditions, common coordinate reconstruction is now absorbed into the complete fifteen-cycle system, and the ground force equation is redundant.

The next high-value target is a rigorous emptiness certificate for these 27 cells, preferably by eliminating the fifteen sine-cycle constraints against the pentagon closures or by validated interval subdivision on the resulting reduced variables.

No theorem-state file is changed. C-II remains open.

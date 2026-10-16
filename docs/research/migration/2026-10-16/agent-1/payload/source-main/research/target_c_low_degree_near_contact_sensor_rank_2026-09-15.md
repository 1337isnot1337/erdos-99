# Target C-II — the degree-5/6 residual branch carries a linear-rank near-contact train sensor

**Date:** 2026-09-15
**Status:** proof-only source-level differential strengthening
**Scope:** the `R_F=o(D)` branch of the degree-5/6 residual theorem, at every fixed `t<=T<X_6`
**Dependencies:** degree-5/6 residual near-contact extension; Wegner/Groemer equality for 5/6 faces; audited train-rate parametrization; no-bounded-return train theorem; contact-degree bound `deg_C<=5`
**Certificate:** `research/verify_target_c_low_degree_near_contact_sensor_rank.py`
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The existing hidden-diagonal train-sensor theorem is written for pentagons. The degree-5/6 residual extension gives almost-active hidden pairs in hexagons too, but an arbitrary hidden unit pair in a hexagon may span three boundary edges and therefore does not automatically produce the same two-train derivative row.

Wegner equality contains more structure than the arbitrary-pair statement: a zero-slack 5/6-face is a Groemer packing whose boundary point set admits a unit equilateral triangulation. Every triangulated polygon has an ear. Hence every zero-slack limit has a **two-edge** boundary diagonal of length one. Compactness propagates that fact to near equality.

Consequently, throughout the sublinear-residual branch, one may choose linearly many vertex-disjoint degree-5/6 faces with a two-edge hidden diagonal of length `1+o(1)`. Each such diagonal measures one difference of adjacent stopped-train angular rates with coefficient tending to `sqrt(3)`. The resulting sensor operator has linear rank.

Let

\[
F_{56}:=f_5+f_6,
\qquad
L_6(T):={3C_{707}/2+\pi-11T/4\over2}.
\]

### Theorem LS — low-degree sensor rank

If `R_F=o(D)` along an unbounded survivor sequence with fixed `t<=T<X_6`, then there is a vertex-disjoint family `G_D` of degree-5/6 bounded faces and one two-edge hidden diagonal `d_P` in each face such that

\[
\boxed{
 |G_D|\ge\left({L_6(T)\over25}-o(1)\right)D,
 \qquad
 \max_{P\in G_D}(|d_P|-1)\to0.
}
\tag{LS.1}

If `D_hid` is the derivative operator sending stopped-train angular rates to the squared-length derivatives of these selected hidden diagonals, then

\[
\boxed{
 \operatorname{rank}D_{hid}
 \ge {|G_D|\over2}
 \ge\left({L_6(T)\over50}-o(1)\right)D.
}
\tag{LS.2}

Every nonzero row coefficient converges uniformly to `sqrt(3)`.

## 1. Equality forces a unit two-edge diagonal

Fix `m in {5,6}` and a zero-Oler-slack limit of strict convex equilateral unit-separated `m`-faces. The audited scaled Wegner equality theorem says the limiting point set is a Groemer/Wegner packing and admits a straight-line triangulation by unit equilateral triangles.

All `m` limiting source points remain on the boundary of the weakly convex limiting polygon in their original cyclic order. There are no additional source points in this face. Hence the Groemer triangulation is a triangulation of a polygonal disk with this `m`-cycle as its boundary, allowing collinear boundary subdivisions in the weak limit.

The abstract triangulation of a polygonal disk with no interior vertices has an ear: some boundary vertex `v_{i+1}` belongs to a triangular face whose other two vertices are its boundary neighbors `v_i,v_{i+2}`. Equivalently, the triangulation contains the diagonal

\[
v_iv_{i+2}.
\]

Every edge of the Groemer triangulation has unit length, so

\[
\boxed{|v_i-v_{i+2}|=1}
\tag{LS.3}

for at least one `i` in every zero-slack 5/6 limit.

This is stronger than merely asserting that *some* nonboundary unit pair exists.

## 2. Compactness gives a two-edge stability modulus

For a strict convex equilateral `m`-face `P=(v_1,...,v_m)`, define

\[
h_2(P):=\min_i\bigl(|v_i-v_{i+2}|-1\bigr).
\]

Unit separation and canonical face visibility give `h_2(P)>0` at finite `D`.

Fix `eta>0`. Suppose no positive Oler gap existed among 5- or 6-faces satisfying `h_2(P)>=eta`. A zero-slack convergent subsequence would then contradict (LS.3). Therefore there are positive constants

\[
\widetilde\sigma_5(\eta),\widetilde\sigma_6(\eta)>0
\]

such that

\[
h_2(P)\ge\eta
\quad\Longrightarrow\quad
A_P-A_{min}(\deg P)\ge\widetilde\sigma_{\deg P}(\eta).
\tag{LS.4}
\]

Using the exact residual identity

\[
r_P={A_P-A_{min}(\deg P)\over a_0},
\]

and residual conservation, the same diagonal argument as in the degree-5/6 residual theorem shows that if `R_F=o(D)`, there is a family `H_D` with

\[
|H_D|\ge(L_6(T)-o(1))D,
\qquad
\max_{P\in H_D}h_2(P)\to0.
\tag{LS.5}

Choose one minimizing two-edge diagonal in each face.

## 3. Extract vertex-disjoint faces with factor 25

The train-sensor incidence argument needs face-terminal occurrences not to be reused, so here we deliberately extract vertex-disjoint **faces**, rather than only endpoint-disjoint hidden pairs.

A degree-5/6 face has at most six vertices. Every source vertex lies on at most five bounded face boundaries. Therefore one selected face intersects at most

\[
6(5-1)=24
\]

other selected faces. The face-intersection graph has maximum degree at most 24, so a greedy independent-set extraction gives a vertex-disjoint subfamily `G_D` with

\[
|G_D|\ge {|H_D|\over25}.
\tag{LS.6}

Together with (LS.5), this proves (LS.1).

## 4. Every selected two-edge diagonal is a two-train sensor

Fix a selected face and write its chosen two-edge boundary path as

\[
x\;--\;z\;--\;y.
\]

Orient the two unit side vectors along the face:

\[
a=z-x,
\qquad
b=y-z.
\]

Let `tau_a,tau_b` be the complete stopped trains containing these two boundary side occurrences. They are distinct. If one non-singleton train terminated on both sides of the same bounded face it would violate the audited no-bounded-return theorem; two distinct singleton sides are distinct singleton trains.

For a contact infinitesimal flex with train angular rates `omega_tau`, the audited train parametrization gives

\[
\dot a=\omega_{\tau_a}Ja,
\qquad
\dot b=\omega_{\tau_b}Jb.
\]

For the hidden diagonal `d=a+b`,

\[
\boxed{
{d\over dt}|d|^2
=2\det(a,b)\bigl(\omega_{\tau_a}-\omega_{\tau_b}\bigr).
}
\tag{LS.7}

Since `|d|->1` uniformly on `G_D`,

\[
a\cdot b={|d|^2-2\over2}\to-{1\over2}
\]

and strict convexity fixes the positive determinant orientation. Hence

\[
\boxed{2\det(a,b)\to\sqrt3}
\tag{LS.8}

uniformly over the selected sensor rows.

## 5. The sensor graph still has maximum degree two

Build the sensor multigraph `H_sens` whose vertices are complete stopped trains and whose edge for each selected face joins `tau_a` to `tau_b`.

The selected faces are vertex-disjoint, so a terminal side occurrence cannot be used by two sensor faces. A complete stopped train has exactly two terminal occurrences. Therefore

\[
\boxed{\Delta(H_{sens})\le2.}
\tag{LS.9}

There are no loops by no-bounded-return. Thus every nontrivial component is a path or a cycle, including the possible two-edge parallel cycle.

The hidden-diagonal derivative matrix is a positive diagonal row scaling of the oriented incidence matrix of `H_sens`. A path with `e` edges has incidence rank `e`; a cycle with `e>=2` edges has rank `e-1>=e/2`. Summing components gives

\[
\operatorname{rank}D_{hid}\ge {|G_D|\over2},
\]

which proves (LS.2).

## 6. Certified rank densities

The exact companion verifier gives the safe rows

\[
\begin{array}{c|c|c}
T & |G_D|/D\text{ lower} & \operatorname{rank}D_{hid}/D\text{ lower}\\ \hline
2.00 & 0.0102 & 0.00510\\
2.05 & 0.0074 & 0.0037\\
2.10 & 0.0047 & 0.00235\\
2.15 & 0.0019 & 0.00097\\
2.18 & 0.00030 & 0.00015\\
2.1854 & 0.0000048 & 0.0000024
\end{array}
\tag{LS.10}

All rows are rounded down from exact-rational enclosures.

## 7. Updated algebraic obstruction

The sublinear-residual high-`t` branch now contains two simultaneous low-degree objects:

```text
strong activation population:
  endpoint-disjoint hidden near-contact matching of density L_6(T)/9;

strong differential population:
  vertex-disjoint 5/6-face sensor family of density L_6(T)/25,
  with hidden-contact derivative rank at least L_6(T)/50.
```

The latter extends the pentagon-only sensor architecture beyond the `2.0215` pentagon cutoff to the degree-5/6 cutoff `2.1854`.

The remaining issue is not local first-order sensitivity: every selected row has a coefficient tending to `sqrt(3)`. The open problem is how this sensor operator intersects the global face-closure kernel and the actual-diameter derivative map. A closure would follow from proving that the diameter graph cannot block a linear-dimensional low-degree sensor subspace without forcing either linear `R_F` or an actual unit hidden chord.

No such rank-intersection theorem is claimed here.

**Disposition:** proved proof-only degree-5/6 near-contact train-sensor rank extension through the certified `t<=2.1854` residual frontier. C-II and Level I remain open.

# Target C-II — exact gap-order classification for physical equilateral force pentagons

**Date:** 2026-09-19  
**Status:** exact local nonlinear structural theorem; theorem-state authority unchanged  
**Scope:** every strict closed equilateral force pentagon used by the Target C reciprocal reductions  
**Depends on:** the audited physical one-turn/two-turn bounds; the force-closure cosine identities and full-range monotonicity developed for the generic `H7b` orbit-129 exclusion  
**Certificate:** `research/verify_target_c_pentagon_gap_order_2026_09_19.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

Let

\[
x_0,x_1,x_2,x_3,x_4>0,
\qquad
\sum_i x_i=2,
\]

be the consecutive force-direction gaps of a strict closed equilateral pentagon, normalized by `pi`. The pentagon closure equations impose substantially more order information than the previously used affine turn simplex.

The main result is

\[
\boxed{
\operatorname{sgn}(x_{k+1}-x_{k-1})
=
\operatorname{sgn}(x_{k+3}-x_{k+2})
\quad\text{for every }k\pmod 5.
}
\tag{1}
\]

Equality is included: one difference vanishes if and only if the other does.

Consequently, if all five gaps are distinct, their cyclic ranks are, up to a dihedral relabeling,

\[
\boxed{1,5,2,3,4.}
\tag{2}
\]

Equivalently, among the `5!=120` possible strict gap orders, only ten can occur, and those ten form one `D_5` orbit. In particular the smallest and largest gaps are always cyclically adjacent.

The equality walls are rigid as well. A physical gap vector can have only

\[
\boxed{1,3,\text{ or }5\text{ distinct gap values}.}
\tag{3}
\]

If it has three distinct values, the multiplicities are `1+2+2`; after cyclic/reflection relabeling its turn sequence has exactly one of

\[
\boxed{T<B=D<A=E}
\tag{4a}
\]

or

\[
\boxed{A=E<B=D<T.}
\tag{4b}
\]

If all gaps are equal, then

\[
x_0=\cdots=x_4=\frac25.
\tag{5}
\]

Thus the full physical turn set, including equality cases, lies in the union of the closures of only ten permutation cones. This replaces a naive `120`-order local branching by ten exact local order chambers.

---

## 1. Two closure identities

Use unnormalized angular gaps

\[
T,A,B,D,E>0,
\qquad
T+A+B+D+E=2\pi.
\]

Let the five unit force directions in cyclic order be `u_0,...,u_4`, with successive gaps `T,A,B,D,E`. Pentagon closure gives

\[
u_4+u_0+u_1=-(u_2+u_3),
\qquad
u_0+u_1+u_2=-(u_3+u_4).
\]

Taking squared norms gives the exact identities already used in the orbit-129 analysis:

\[
\cos B
=
\frac12+\cos E+\cos T+\cos(E+T),
\tag{6}
\]

\[
\cos D
=
\frac12+\cos T+\cos A+\cos(T+A).
\tag{7}
\]

For fixed `T`, define

\[
f_T(z)
=
\arccos\!\left(
\frac12+\cos T+\cos z+\cos(T+z)
\right).
\tag{8}
\]

Then

\[
B=f_T(E),
\qquad
D=f_T(A).
\tag{9}
\]

The physical turn bounds give

\[
0<T<\frac{2\pi}{3},
\qquad
0<A+T<\pi,
\qquad
0<E+T<\pi.
\tag{10}
\]

If

\[
R_T(z)=\frac12+\cos T+\cos z+\cos(T+z),
\]

then throughout the interval between `A` and `E`,

\[
R_T'(z)
=-2\cos(T/2)\sin(z+T/2)<0.
\tag{11}
\]

The endpoint values are `cos B` and `cos D`, with physical `0<B,D<2pi/3`; hence the arccos branch stays real and nonsingular throughout the interval. Therefore

\[
f_T'(z)>0.
\tag{12}
\]

It follows from (9) that

\[
\boxed{
\operatorname{sgn}(A-E)=\operatorname{sgn}(D-B).
}
\tag{13}
\]

Rotating the choice of `T` through the five gaps gives (1).

---

## 2. Strict order classification

Assume first that all five gaps are distinct. Give each `x_i` its rank in increasing order. Relation (1) is then a sign constraint on each of the five cyclic quadruples.

There are only `120` strict rank permutations. The exact companion verifier checks all of them. Exactly ten satisfy all five instances of (1):

```text
(0,2,3,4,1)
(0,3,2,1,4)
(1,3,4,0,2)
(1,4,3,2,0)
(2,0,4,3,1)
(2,4,0,1,3)
(3,0,1,2,4)
(3,1,0,4,2)
(4,1,2,3,0)
(4,2,1,0,3)
```

Each tuple lists the gap indices from smallest to largest. These ten orders are exactly the dihedral orbit of the first one. The corresponding cyclic rank vector for that representative is `(1,5,2,3,4)`, proving (2). The adjacency of the minimum and maximum follows immediately and is checked independently for all ten orders by the verifier.

---

## 3. Equality propagation

Now allow equal gaps. Encode a weak order by integer ranks, with equal ranks exactly when the corresponding gaps are equal. Replace ordinary signs in (1) by the three-valued sign in `{-1,0,+1}`.

There are `541` ordered set partitions on five labelled entries. The exact exhaustive check finds only `21` satisfying all five relations:

\[
10\text{ strict five-level orders}
+10\text{ three-level orders}
+1\text{ one-level order}.
\tag{14}
\]

There are no admissible two-level or four-level weak orders. Every three-level order has multiplicities `1+2+2`, and the singleton is always the minimum or always the maximum. The ten such weak orders split into two five-element dihedral orbits. Canonical rank patterns in cyclic coordinates `(T,A,B,D,E)` are

\[
(0,2,1,1,2)
\quad\text{and}\quad
(2,0,1,1,0),
\tag{15}
\]

which are exactly (4a) and (4b).

The verifier also checks that every one of the 21 admissible weak orders is a coarsening of at least one of the ten strict orders. Therefore no extra equality chamber has to be added: the closures of the ten strict permutation cones already cover all physical equality cases.

---

## 4. The three-level wall is a one-parameter exact family

Suppose one equality occurs. After cyclic relabeling take

\[
A=E.
\]

Strict monotonicity in (9) gives

\[
B=D.
\]

Put

\[
\gamma=A+\frac T2.
\]

The turn sum gives

\[
B=\pi-\gamma.
\tag{16}
\]

Substituting `A=E` into (6), setting `c=cos(T/2)`, and using `cos B=-cos gamma` gives

\[
-(1+2c)\cos\gamma
=2c^2-\frac12,
\]

hence

\[
\boxed{
\cos\gamma=\frac12-\cos(T/2).
}
\tag{17}
\]

Thus the equality wall has the explicit parameterization

\[
\boxed{
\gamma=\arccos\!\left(\frac12-\cos(T/2)\right),
\quad
A=E=\gamma-\frac T2,
\quad
B=D=\pi-\gamma.
}
\tag{18}
\]

The regular point occurs exactly at

\[
T=A=B=D=E=\frac{2\pi}{5}.
\tag{19}
\]

If `T<2pi/5`, `T` cannot be the maximum in (15), since then the total turn would be strictly less than `5T<2pi`; hence

\[
T<B=D<A=E.
\tag{20}
\]

If `T>2pi/5`, the symmetric argument excludes `T` as the minimum, so

\[
A=E<B=D<T.
\tag{21}
\]

This describes the entire nonregular equality wall up to cyclic relabeling.

---

## 5. Use at the current support-seven endpoint

This theorem is local and does not by itself exclude one of the currently surviving support-seven reciprocal branches. Its value is that it supplies exact nonconvex information absent from the pentagon turn simplex.

For each physical pentagon, a rigorous branch-and-bound or interval proof now needs only the ten closed cones from (2), not all `120` arbitrary gap orders. Equality cases require no additional branch because they lie on those cone boundaries. The three-level boundaries themselves have the explicit one-variable parameterization (18).

The next use is in the remaining generic `H7b` cells and the twelve convex `H8` reflection orbits: intersect the existing exact affine/triangle systems and law-of-sines constraints with these ten order cones before applying validated nonlinear force-closure bounds. A failure in one cone can then be certified independently without assuming generic distinctness.

No theorem-state file is changed. C-II remains open.

# Target C-II - generic H6 oriented-matroid/sign reduction

**Date:** 2026-09-19  
**Status:** exact finite necessary-condition reduction; theorem-state authority unchanged  
**Scope:** degree-pure support-seven `H6` reciprocal branch with no collinear triple of reciprocal points  
**Depends on:** audited support-seven endpoint reduction; exact H6 ground sign classification; local non-ground hull `2+3` sign/positions theorem  
**Certificate:** `research/verify_target_c_support7_h6_oriented_matroid_sign_reduction_2026_09_19.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The preceding H6 work classified the seven signed unit rays at the ground exactly but left all thirteen feasible ground sign patterns alive. This note adds the first cross-face combinatorial layer for H6. It couples the ground order to the two interior reciprocal points, the support-seven missing graph, and the exact local sign positions at the five non-ground hull vertices.

The result is an exact outer reduction

\[
\boxed{11,171,160\longrightarrow264,944}
\]

labelled generic H6 cells. The survivors split as

\[
\boxed{208,588\ C_7+56,356\ (C_3\sqcup C_4).}
\]

More cleanly, twelve of the 360 labelled `C7` missing-graph embeddings are impossible for every generic H6 reciprocal order type and every one of the thirteen ground-feasible sign patterns. Under reflection of the hexagon fixing the ground and exchange of the two interior labels, these twelve form three classes.

This is a necessary-condition reduction only. The 264,944 surviving cells are not claimed geometrically realizable.

## 1. Generic H6 setup

Label the strict convex reciprocal hexagon in counterclockwise order

\[
0,1,2,3,4,5,
\]

where `0` is the ground point. The two non-ground reciprocal points in the interior are `6,7`. Thus the seven non-ground vertices are `1,...,7`.

At the degree-pure support-seven endpoint, the missing graph among `1,...,7` is two-regular, hence

\[
\overline R=C_7\quad\text{or}\quad C_3\sqcup C_4.
\]

The present reciprocal graph is `K8` minus those seven missing non-ground edges.

The branch treated here is generic: no three of the eight reciprocal points are collinear. The collinearity walls remain a separate branch.

## 2. One interior point gives 26 exact slot vectors

Fix one strict interior point `p`. At a hull vertex `i`, the rays to the other five hull vertices occur in the order

\[
i+1,i+2,\ldots,i+5\pmod 6.
\]

Because `p` is strictly inside the hexagon, its ray lies strictly between the two boundary-neighbor rays. It therefore occupies one of four slots. Let

\[
k_i\in\{1,2,3,4\}
\]

be the number of hull rays preceding the ray to `p`.

For distinct hull vertices `i,j`, define

\[
\chi_p(i,j)=
\begin{cases}
+1,&j\text{ precedes }p\text{ in the raw ray order at }i,\\
-1,&p\text{ precedes }j.
\end{cases}
\]

This is the orientation sign `chi(i,j,p)`. Alternation of the determinant gives the exact compatibility condition

\[
\chi_p(i,j)=-\chi_p(j,i).
\tag{2.1}
\]

Enumerating the `4^6` slot vectors and imposing (2.1) leaves exactly

\[
\boxed{26}
\]

single-interior slot vectors.

This count is only a necessary order condition. No realizability assumption is made.

## 3. Coupling the two interior points by the rank-three chirotope axiom

Take one of the 26 slot vectors for point `6` and one for point `7`. At a hull vertex `i`, if their slots differ then the sign

\[
\chi(i,6,7)
\]

is forced by which ray occurs first. If their slots coincide, that sign has two possible values.

Together with the fixed convex-hexagon orientations, these signs specify all `56` unordered triple orientations on the eight labels. Any actual generic point configuration must define a uniform rank-three chirotope. Hence for every distinct `x,a,b,c,d`, the three nonzero signs

\[
\chi(x,a,b)\chi(x,c,d),
\quad
-\chi(x,a,c)\chi(x,b,d),
\quad
\chi(x,a,d)\chi(x,b,c)
\tag{3.1}
\]

must contain both `+1` and `-1`.

The verifier tests all compatible choices exactly:

```text
single-interior slot vectors:       26
paired sign extensions tested:    4678
uniform chirotope survivors:      1848
unique six-hull raw-order types:  1848
ground raw orders:                  20
```

Thus every actual generic H6 configuration induces one of these 1,848 outer raw-order types. Some of the 1,848 may themselves be nonrealizable oriented matroids; that can only make this reduction conservative.

## 4. Insert the exact H6 ground classification

For a fixed raw order at the ground, number the seven non-ground rays from `1` through `7` in that order. The exact ground-only H6 theorem says the size-three sign class must occupy one of exactly thirteen position patterns:

```text
145 156 234 235 236 237 245 256
345 346 347 356 456
```

Fix this size-three class as positive. Global sign reversal then adds no new state.

There are `360` labelled `C7` missing graphs and `105` labelled `C3+C4` missing graphs. Therefore before using any non-ground hull sign constraint, the finite outer state count is

\[
1848\cdot(360+105)\cdot13
=\boxed{11,171,160}.
\tag{4.1}
\]

## 5. Exact local sign compatibility at the five non-ground hull vertices

Fix a hull vertex `i in {1,...,5}`. Its full raw order contains the other seven reciprocal vertices. Delete the two missing non-neighbors of `i`. Exactly five present reciprocal rays remain.

The audited local pentagon theorem says that, up to exchanging the two force-sign colors, one sign class occupies raw positions `2` and `4` among these five present rays.

Normalize that local pattern so that the ground edge `0i` has sign `+1`, and let

\[
b_i(j)\in\{\pm1\}
\]

be the resulting normalized sign assigned to a present hull-hull edge `ij`.

Let

\[
g_i\in\{\pm1\}
\]

be the actual sign of the ground edge `0i`, fixed by the chosen ground sign pattern. Then the actual sign prescribed at endpoint `i` for a present relation edge `ij` is

\[
g_i b_i(j).
\]

A reciprocal edge has one sign, so the prescriptions from its two endpoints must agree. Hence every present hull-hull relation edge satisfies the exact condition

\[
\boxed{g_i g_j=b_i(j)b_j(i).}
\tag{5.1}
\]

No metric approximation enters (5.1). The verifier applies it to every one of the states in (4.1).

## 6. Exact census

The result is

\[
\boxed{11,171,160\longrightarrow264,944},
\tag{6.1}
\]

with

\[
\boxed{208,588\ C_7+56,356\ (C_3\sqcup C_4)}.
\tag{6.2}
\]

Equivalently, the local cross-face sign layer rejects `97.6283...%` of this labelled outer census. The exact surviving fraction is

\[
\frac{264944}{11171160}=\frac{33118}{1396395}.
\]

All 1,848 outer raw-order types still have at least one survivor. At the missing-graph level:

```text
C7 embeddings with at least one survivor:       348 / 360
C3+C4 embeddings with at least one survivor:    105 / 105
```

The survivor counts by ground position pattern are:

```text
145   3694
156  19678
234  10924
235  18556
236  67914
237  19678
245  10256
256  67914
345   2900
346  10256
347   3694
356  18556
456  10924
```

## 7. Twelve `C7` embeddings are excluded outright in generic H6

The following twelve labelled missing `C7` edge sets have no survivor at all. Each row lists the seven missing edges:

```text
12 14 26 35 37 47 56
12 14 27 35 36 46 57
13 15 24 26 37 47 56
13 15 24 27 36 46 57
13 16 25 27 34 47 56
13 16 25 27 37 45 46
13 17 25 26 34 46 57
13 17 25 26 36 45 47
14 16 23 27 35 47 56
14 17 23 26 35 46 57
15 16 24 27 35 37 46
15 17 24 26 35 36 47
```

This exclusion is uniform over all 1,848 chirotope outer orders and all thirteen H6 ground patterns. Therefore none of these twelve missing-graph placements can occur in an actual generic H6 support-seven reciprocal.

The obvious relabeling group generated by

- reflection of the hull fixing `0`, sending `(1,2,3,4,5)` to `(5,4,3,2,1)`, and
- exchange of the two interior labels `6,7`

partitions these twelve embeddings into three classes of four. Representatives are

```text
12 14 26 35 37 47 56
13 15 24 26 37 47 56
13 16 25 27 34 47 56
```

## 8. What remains

This does not exclude H6. It closes the purely local ground-only stage and starts the required cross-face coupling, but 264,944 labelled outer cells remain.

The next exact layer should use the actual angular geometry rather than more ground projection inequalities. For each surviving cell, the raw radial order is fixed strongly enough to write affine angle-sum equations for reciprocal triangles, while each of the five non-ground hull force pentagons obeys the audited turn-simplex inequalities and exact force-angle conversion. This is the H6 analogue of the successful generic-H7b affine/Farkas reduction and is now a finite certificate problem.

The generic restriction is essential here. Collinear reciprocal triples are not represented by a uniform chirotope and must remain in the separate collinearity-wall analysis.

No theorem-state file is changed. C-II remains open.

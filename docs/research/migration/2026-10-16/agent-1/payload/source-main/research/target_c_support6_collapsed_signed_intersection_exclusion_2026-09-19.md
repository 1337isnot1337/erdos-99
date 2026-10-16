# Target C-II — signed cycle intersection excludes collapsed support six

**Date:** 2026-09-19  
**Claim class:** exact global train-topology exclusion; theorem-state authority unchanged  
**Scope:** degree-pure collapsed support-six one-anchor components after maximal two-anchor activation  
**Depends on:** audited one-anchor relation-component theorem; completed noncollapsed support-six exclusion; audited collapsed rotation-cell reduction; stopped-train at-most-one-crossing theorem; strict-rhombus crossing-angle theorem; complete-train crossing graph triangle-freeness  
**Certificate:** `research/verify_target_c_support6_collapsed_signed_intersection_exclusion_2026_09_19.cpp`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The last degree-pure support-six one-anchor mechanism is impossible.

The previous support-six work had reduced every surviving degree-pure block to the collapsed form

\[
y_1=\cdots=y_6\ne0,
\qquad
R[K]=K_6\setminus M,
\]

with six projectively parallel outside anchors in a `3+3` orientation split. Exact local closure roots show that this mechanism is locally real: the six equilateral-pentagon closure equations and all current strict turn inequalities do not remove it. The later global finite search forced at least ten internal train crossings but had not excluded all higher crossing counts.

The missing constraint is the **signed integer** version of the mod-2 cycle-intersection equation. Once the algebraic sign of every train crossing and every exceptional-face chord crossing is retained, every one of the 42 exact collapsed rotation-cell symmetry orbits is impossible.

Hence

\[
\boxed{\text{no globally realizable degree-pure collapsed support-six block exists}.}
\tag{SI.0}
\]

Together with the completed noncollapsed support-six exclusion,

\[
\boxed{\text{no nonzero degree-pure one-anchor dual component has support }\le6.}
\tag{SI.0'}
\]

The support-five and support-six equality mechanisms are therefore both gone.

---

## 1. Oriented relation cycles

Use one of the exact collapsed rotation cells. For every internal relation train `e`, choose the upper-half-plane representative

\[
u_e=(\cos\alpha_e,\sin\alpha_e),
\qquad 0<\alpha_e<\pi,
\]

and orient the complete train from the exceptional face carrying the side occurrence `+u_e` to the face carrying `-u_e`. This is the coherent orientation already used in the audited rotation-cell and forced-crossing-rotation theorems.

Let `C` be a simple cycle of the relation graph `K_6\setminus M`, with an arbitrary orientation. For an edge `e` of `C`, define

\[
\epsilon_C(e)=
\begin{cases}
+1,&C\text{ traverses }e\text{ in the canonical train orientation},\\
-1,&C\text{ traverses }e\text{ against it}.
\end{cases}
\tag{1.1}
\]

Construct an oriented immersed closed curve `gamma_C` in the physical plane as follows.

1. Follow the canonical midpoint centerline of each relation train in the direction prescribed by `C`.
2. At every exceptional face, join the incoming train-end midpoint to the outgoing train-end midpoint by a straight chord inside that strict convex face.

For two edge-disjoint relation cycles `C,D`, the curves `gamma_C,gamma_D` share no complete train. At a common exceptional face their four train-end midpoints are distinct because the cycles are edge-disjoint.

---

## 2. Algebraic intersection in the plane is zero

For two compact oriented closed curves in `R^2`, after an arbitrarily small generic perturbation, the algebraic intersection number is zero. Equivalently, `H_1(R^2)=0`, so either oriented 1-cycle is null-homologous and has zero algebraic intersection with every closed 1-cycle.

Apply this to `gamma_C` and `gamma_D`.

All intersections occur in one of two places already identified in the audited mod-2 argument:

- a strict rhombus where one complete train of `C` crosses one complete train of `D`; or
- the interior of a common exceptional face, where the two joining chords may cross.

The stopped-train theorem gives at most one strict-rhombus crossing for a fixed train pair.

---

## 3. Signed contribution of a strict-rhombus train crossing

Suppose internal trains `e,f` cross in a strict rhombus. Write `t_e,t_f` for their canonical oriented midpoint-path tangents through that rhombus. The already-audited local rhombus calculation gives

\[
\boxed{
\operatorname{sign}\det(t_e,t_f)
=
\operatorname{sign}\det(u_e,u_f).
}
\tag{3.1}
\]

If the cycle curve `gamma_C` traverses train `e`, its tangent is `epsilon_C(e)t_e`; similarly for `D` and `f`. Therefore the oriented intersection contribution is

\[
\boxed{
\epsilon_C(e)\epsilon_D(f)
\operatorname{sign}\det(u_e,u_f).
}
\tag{3.2}
\]

Let `z_{e,f}` be `1` when the two complete trains cross and `0` otherwise. The total train-crossing contribution is therefore

\[
\sum_{e\in E(C),\,f\in E(D)}
\epsilon_C(e)\epsilon_D(f)
\operatorname{sign}\det(u_e,u_f)\,z_{e,f}.
\tag{3.3}
\]

The sign of the determinant is exact inside a selected crossing window. With

\[
x_e={3\alpha_e\over\pi},
\]

a strict unit-rhombus crossing requires one of

\[
1<x_e-x_f<2,
\qquad
1<x_f-x_e<2.
\tag{3.4}
\]

In the first window `alpha_e>alpha_f`, hence

\[
\operatorname{sign}\det(u_e,u_f)
=
\operatorname{sign}\sin(\alpha_f-\alpha_e)
=-1,
\]

and in the second it is `+1`.

---

## 4. Signed contribution inside a common exceptional face

At a common exceptional face `v`, orient the `C` chord from its incoming side midpoint to its outgoing side midpoint, and do the same for `D`.

Let

\[
\iota_v(C,D)\in\{-1,0,+1\}
\]

be the oriented intersection sign of those two chords. Because the face is strictly convex,

- `iota_v=0` exactly when the two endpoint pairs do not alternate in the cyclic side order;
- `|iota_v|=1` exactly when they alternate.

The sign is determined purely by the counterclockwise side order. If the `C` chord is `a -> b` and the incoming endpoint `c` of the `D` chord lies strictly on the counterclockwise boundary arc from `a` to `b` while the outgoing endpoint `d` does not, then

\[
\iota_v(C,D)=+1;
\]

if `d` lies on that arc and `c` does not, then `iota_v=-1`.

The exact rotation-cell tuple `(A_1,A_2,B_1,B_2)` is the physical counterclockwise relation-side order after deleting the unique anchor side. Thus `iota_v` is read exactly from the stored cell data; no metric realization of the pentagon is needed.

Modulo two,

\[
\iota_v(C,D)\equiv\eta_v(C,D)\pmod2,
\tag{4.1}
\]

where `eta_v` is the alternation bit from the earlier MI.1 theorem.

---

## 5. Signed cycle-intersection equation

The total algebraic intersection of `gamma_C` and `gamma_D` is zero. Combining Sections 3 and 4 gives, for every pair of edge-disjoint oriented simple relation cycles,

\[
\boxed{
\sum_{e\in E(C),\,f\in E(D)}
\epsilon_C(e)\epsilon_D(f)
\operatorname{sign}\det(u_e,u_f)\,z_{e,f}
+
\sum_{v\in V(C)\cap V(D)}\iota_v(C,D)
=0.
}
\tag{SI.1}
\]

This is an integer equation, not a parity equation.

Reducing (SI.1) modulo two recovers the audited MI.1 equation. Every nonzero crossing coefficient is `+1` modulo two and (4.1) identifies the face terms. Thus (SI.1) is a strict lift of the previous obstruction rather than a different topological assumption.

The verifier checks the local parity reduction for every edge-disjoint cycle pair in all 42 tested representatives.

---

## 6. Complete exact finite exclusion

Every actual collapsed support-six block lies in one of the audited 388 labelled open rational rotation cells. The conservative symmetry quotient has

\[
15+27=42
\]

representatives: 15 for the all-cross missing matching and 27 for the mixed missing matching.

For each representative the certificate performs the following exact search.

1. Generate the full MI.1 affine crossing space over `F_2`. This is necessary because every actual drawing satisfies MI.1, equivalently the mod-2 reduction of (SI.1).
2. Retain only triangle-free train-crossing graphs. The complete-train crossing graph is triangle-free.
3. For every selected crossing set, impose all strict crossing windows (3.4) **simultaneously** in the same exact difference-constraint system. Enumerate every jointly feasible determinant-sign choice.
4. Evaluate (SI.1) for every pair of edge-disjoint simple relation cycles.

The search ranges over the entire MI.1 affine space, not only the low crossing weights used in the earlier `X_K>=7` and `X_K>=10` regressions.

The exact totals are:

\[
\begin{array}{c|r|r|r|r}
|S|&\text{MI.1}&\text{triangle-free}&\text{joint angle}&\text{SI.1 survivors}\\\hline
2&17&17&15&0\\
3&34&34&32&0\\
4&191&189&134&0\\
5&407&395&279&0\\
6&1,916&1,740&1,140&0\\
7&4,909&3,965&2,544&0\\
8&11,944&9,340&5,801&0\\
9&27,650&19,455&10,453&0\\
10&58,377&40,324&20,349&0\\
11&115,221&68,769&29,112&0\\
12&210,197&111,761&43,138&0\\
13&345,201&147,900&49,043&0\\
14&520,106&182,236&58,456&0\\
15&677,710&176,890&49,474&0\\
16&790,014&150,897&41,475&0\\
17&818,048&99,956&24,221&0\\
18&743,201&60,563&15,022&0\\
19&621,404&26,851&5,522&0\\
20&451,767&11,870&2,922&0\\
21&297,653&3,563&609&0\\
22&176,014&1,255&302&0\\
23&87,969&196&38&0\\
24&43,426&52&6&0\\
25&16,318&3&1&0\\
26&6,765&3&0&0\\
27&1,997&0&0&0\\
28&685&0&0&0\\
29&131&0&0&0\\
30&36&0&0&0\\
31&4&0&0&0
\end{array}
\tag{6.1}
\]

There are no MI.1 states of weights zero or one. Across all 42 representatives there are

\[
\boxed{6,029,312}
\]

MI.1 affine states in total and

\[
\boxed{360,088}
\]

triangle-free, jointly angle-feasible crossing states. Every one has exactly one feasible determinant-sign assignment in this census, and

\[
\boxed{0}
\]

satisfy all signed equations (SI.1).

All arithmetic in the cell, parity, triangle, and signed-intersection layers is integer or bitset arithmetic. Joint strict-angle feasibility uses the already-audited integer difference-constraint transformation. No floating-point geometry, nonlinear optimization, or tolerance enters the exclusion.

---

## 7. Why the 42-representative quotient is safe for SI.1

The 42-orbit quotient uses sign-preserving face relabelings preserving the missing matching, together with reflection in the common anchor line.

A sign-preserving relabeling merely permutes relation edges, cycles, train-pair variables, and equations (SI.1).

A reflection reverses the orientation of the physical plane. Every oriented train-crossing sign and every oriented face-chord intersection sign therefore changes sign. Each complete equation (SI.1) is multiplied by `-1`, so the condition that it equal zero is unchanged.

Thus a signed-intersection survivor in any of the 388 labelled cells would map to a survivor in its tested representative. Since no representative survives, no labelled cell survives.

---

## 8. Support accounting after eliminating collapsed support six

The completed reciprocal analysis already excluded every **noncollapsed** degree-pure support-six component. Equation (SI.0) now excludes the collapsed case too. Therefore the earlier population `c_6` of degree-pure support-six components is exactly zero.

Support-six components with degree excess are a different class. As before, each such component consumes at least one unit of

\[
x_U=\sum_{F\in U}(\deg F-5),
\]

so their number is at most `x_U`.

Let `c_*` be the number of active one-anchor relation components carrying nonzero projection of the transpose-kernel fiber. Support five and degree-pure support six are impossible. Hence the existing component count simplifies to

\[
\boxed{
c_*\le {n_1+x_U\over7}.
}
\tag{8.1}
\]

With the existing zero-/two-anchor projection bound,

\[
\boxed{
\sigma_C
\le
2n_0+n_2+{n_1\over7}+{x_U\over7}.
}
\tag{8.2}
\]

Using

\[
E_U=a_F+{x_A\over2}+{n_0+n_2\over2},
\qquad
x_A+x_U=Q-f,
\]

the already-checked coefficient comparison becomes

\[
\boxed{
\sigma_C\le {Q\over7}+{26\over7}E_U.
}
\tag{8.3}
\]

The tangent-payment and rhombus-payment correction terms attached to `c_6` are no longer needed: `c_6=0` outright.

At the degree-pure endpoint `x_U=0`, every nonzero one-anchor relation component uses at least seven one-anchor faces, so the one-anchor fiber density is at most `1/7`.

---

## 9. What remains

This closes the support-six classification, not C-II.

The one-anchor transpose-kernel can still use:

1. support-six components containing positive degree excess, charged by `x_U`; or
2. components of support at least seven.

Thus the next support-theoretic equality target is support seven, while the global C-II route must still connect the improved closure-corank bound to diameter locking or a source-preserving finite deformation.

The local collapsed closure certificates remain valid and useful: they now demonstrate a real local/global separation. Their regular two-dimensional six-pentagon closure manifolds exist, but none can be embedded into a globally valid stopped-train/rhombus source because the signed plane-intersection equations fail.

No theorem-state file is changed.

**Disposition:** signed algebraic cycle intersection lifts MI.1 to the integer equation (SI.1); an exact exhaustive search over all 42 collapsed rotation-cell symmetry representatives finds 360,088 triangle-free jointly angle-feasible crossing states and zero SI.1 survivors. The collapsed degree-pure support-six branch is globally impossible. Combined with the prior noncollapsed exclusion, every degree-pure nonzero one-anchor dual component has support at least seven, yielding (8.2)--(8.3). C-II remains open.

> Generated reading edition · [exact source](../../research/target_c_support6_collapsed_rotation_cell_reduction_2026-09-19.md) · source SHA-256 `18fe0f26dd69f5b24785447f75220f6a43a16a4b82ada7d12beffdc1b120c0dc`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "af26559b59e6dec526a42601f497a4d78a5888fa", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support6_collapsed_rotation_cell_reduction_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f4c04fb66216d3ffc82a713e8eb40d22efe4310a1d4a9296e0e0bd9660eb8b07"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — collapsed support-six reduces to 42 exact rotation cells and every cell needs train crossings

**Date:** 2026-09-19  
**Claim class:** proved candidate awaiting promotion; theorem-state authority unchanged  
**Scope:** degree-pure collapsed support-six one-anchor components after maximal two-anchor activation  
**Depends on:** the audited one-anchor relation-component theorem; support-five and noncollapsed-support-six exclusions; the bounded-pentagon no-parallel-side theorem; the strict one-turn bound; the closed-equilateral-pentagon adjacent-turn bounds; the stopped-train crossing/rotation primitive  
**Certificate:** `research/verify_target_c_support6_collapsed_rotation_cells_2026_09_19.cpp`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The remaining degree-pure support-six mechanism is collapsed:

```math
y_1=\cdots=y_6\ne0,
\qquad R=K_6\setminus M,
```

where `M` is a perfect matching and the six oriented outside anchors are projectively parallel with a `3+3` sign split. The existing exact local witness shows that the six pentagon closure equations alone do not eliminate this mechanism. The later Jordan argument eliminates the rigorous box around that witness, but it does not classify the other collapsed angle/order cells.

This note makes that classification finite before imposing the nonlinear vector-closure equations.

For every internal relation train choose its projective direction

```math
0<\alpha_e<\pi
```

and the upper-half-plane representative `v_e=(cos alpha_e,sin alpha_e)`. At one endpoint the oriented side is `+v_e` and at the other it is `-v_e`; orient `e` from the `+` endpoint to the `-` endpoint.

The physical pentagon inequalities force exactly two outgoing and two incoming relation edges at every face. More strongly, after rotating the anchor side to angle zero, the two first-block and two second-block projective directions satisfy one fixed interlacing order. Scaling

```math
x_e={3\alpha_e\over\pi}
```

turns every current local angle inequality into an integer strict difference constraint.

An exact enumeration then gives:

```math
\boxed{
\begin{array}{c|c|c|c}
\text{missing matching type}&\text{feasible labelled cells}&\text{conservative symmetry orbits}&\text{ribbon genus counts}\\ \hline
3\text{ cross-sign edges}&180&15&36g_1+60g_2+84g_3\\
1\text{ cross}+1(++ )+1(-- )&208&27&32g_1+72g_2+104g_3
\end{array}}
```

Thus every collapsed support-six solution satisfying the current pentagon inequalities belongs to one of

```math
\boxed{388}
```

labelled open rational difference cells, or only

```math
\boxed{42}
```

orbits under sign-preserving relabelings of the six faces and reflection in the common anchor line.

There is no genus-zero cell. Consequently the relation-train arcs cannot realize any surviving local rotation system without internal train crossings. If `X_K` is the number of strict-rhombus crossings between the twelve internal relation trains of the block and `g_K` is its ribbon genus, then

```math
\boxed{X_K\ge g_K\ge1.}
```

The current certified local root lies in a genus-two cell. The previous Jordan certificate proves that its entire rigorous root box is nevertheless globally impossible.

This does not eliminate the collapsed branch. It changes the remaining task from an unconstrained two-dimensional nonlinear family to a finite rotation-cell problem. The next exact subdivision is by the crossing thresholds

```math
{\pi\over3}<|\alpha_e-\alpha_f|< {2\pi\over3},
```

because only such pairs can cross in a strict unit rhombus. The existing Jordan separator can then be applied cell-by-cell, with the vector-closure equations available to remove crossing subcells that survive topology alone.

---

## 1. Every collapsed face has a `2+2` projective sign split

Normalize one face so its anchor side is `+e_1`. For each of its four internal relation sides write the oriented side as either `+v_e` or `-v_e`, with `0<alpha_e<pi`.

All four signs cannot be equal: the `y`-components of the four relation sides would then have one strict sign, while the anchor has zero `y`-component, contradicting face closure.

Suppose there is exactly one `+` side, at projective angle `alpha`, and three `-` sides with

```math
0<\beta_1<\beta_2<\beta_3<\pi.
```

The physical oriented-side order after the anchor begins

```math
0,
\alpha,
\pi+\beta_1,
\pi+\beta_2,
\pi+\beta_3.
```

The first two exterior turns therefore sum to

```math
\alpha+(\pi+\beta_1-\alpha)=\pi+\beta_1>\pi,
```

contradicting the proved strict two-turn upper bound.

If instead there are three `+` sides with largest projective angle `alpha_3` and one `-` side at `beta`, the last two exterior turns sum to

```math
(\pi+\beta-\alpha_3)+(\pi-\beta)=2\pi-\alpha_3>\pi,
```

again impossible.

Hence there are exactly two `+` and two `-` relation occurrences. At the other endpoint of an internal train the oriented side is negated, so `+` and `-` are respectively tail and head of one coherent edge orientation. Therefore

```math
\boxed{\deg^+_R(F)=\deg^-_R(F)=2}
```

at all six faces: every collapsed block carries an Eulerian `2`-in/`2`-out orientation of the octahedral graph `K_6\setminus M`.

A `-e_1` anchor gives the same conclusion after rotating the face by `pi`, which flips all four relation signs and preserves the `2+2` count.

---

## 2. The projective order is forced

Again use a `+e_1` anchor. Let the two `+` projective directions be

```math
a_1<a_2
```

and the two `-` directions be

```math
b_1<b_2.
```

The physical side order is

```math
0,
 a_1,
 a_2,
 \pi+b_1,
 \pi+b_2.
```

The strict two-turn upper inequalities give

```math
\begin{aligned}
(a_2-a_1)+(\pi+b_1-a_2)&<\pi &&\Longrightarrow b_1<a_1,\\
(\pi+b_1-a_2)+(b_2-b_1)&<\pi &&\Longrightarrow b_2<a_2,\\
(\pi-b_2)+a_1&<\pi &&\Longrightarrow a_1<b_2.
\end{aligned}
```

Thus

```math
\boxed{b_1<a_1<b_2<a_2.}
```

For a positive-anchor face, `+` means outgoing and `-` incoming. For a negative-anchor face, rotating its anchor to `+e_1` flips the relation signs, so the first physical block is incoming and the second outgoing.

It is therefore convenient to define

```math
A=(A_1,A_2)=
\begin{cases}
\text{outgoing directions},&F\text{ has positive anchor},\\
\text{incoming directions},&F\text{ has negative anchor},
\end{cases}
```

and `B` as the other two directions. In every case the physical order after the normalized anchor is

```math
0,\alpha_{A_1},\alpha_{A_2},\pi+\alpha_{B_1},\pi+\alpha_{B_2}.
```

---

## 3. All local geometry is an integer strict-difference system

Set

```math
x_e={3\alpha_e\over\pi}\in(0,3).
```

For one face with ordered tuple `(A1,A2,B1,B2)`, its five scaled exterior turns are

```math
\begin{aligned}
G_0&=x_{A_1},\\
G_1&=x_{A_2}-x_{A_1},\\
G_2&=3+x_{B_1}-x_{A_2},\\
G_3&=x_{B_2}-x_{B_1},\\
G_4&=3-x_{B_2}.
\end{aligned}
```

The current physical-pentagon theorems give exactly the strict inequalities

```math
\boxed{
0<G_i<2,
\qquad
2<G_i+G_{i+1}<3
}
```

for all indices cyclically.

The upper adjacent inequality is the earlier two-turn lemma. The lower adjacent inequality is the exact equilateral-pentagon result proved in the support-six H5 work: under the already established one-turn bound `delta_i<2pi/3`, every adjacent pair satisfies

```math
\delta_i+\delta_{i+1}>2\pi/3.
```

Its proof uses only equilateral pentagon closure and the one-turn bound; no noncollapsed reciprocal hypothesis is used in the lemma itself, so it applies to the collapsed physical pentagons here.

Every displayed inequality is of the form

```math
x_v-x_u<c
```

with integer `c`. Hence each fixed edge orientation and local order choice defines one open rational difference polyhedron. There is no numerical root search in the finite classification below.

---

## 4. Only two missing-matching types occur

Let the positive-anchor faces be `P={0,1,2}` and the negative-anchor faces be `N={3,4,5}`. A perfect matching on the six faces has an odd number of `P--N` edges. Hence, up to relabeling within `P` and within `N`, there are only two types:

1. all three matching edges are cross-sign, represented by
   ```math
   M_X=\{03,14,25\};
   
   ```
2. exactly one matching edge is cross-sign, with one `P--P` and one `N--N` edge, represented by
   ```math
   M_M=\{01,23,45\}.
   
   ```

For either type there are exactly 38 Eulerian `2`-in/`2`-out orientations of `K_6\setminus M`.

For a fixed orientation, each face has two possible orders of its `A` pair and two possible orders of its `B` pair, hence four local choices. The finite search therefore starts from only

```math
38\cdot4^6
```

combinatorial order assignments per matching type.

---

## 5. Exact strict-difference certificate

The certificate uses only integer arithmetic for logical decisions.

For a system of strict differences

```math
x_v-x_u<c,
\qquad c\in\mathbb Z,
```

with 12 angle variables plus one constant node, feasibility is equivalent to every directed cycle having strictly positive total weight. Every simple cycle has at most 13 edges.

The verifier replaces every integer edge weight `c` by

```math
14c-1.
```

For a cycle of length `k<=13` and original integer total `C`, the transformed total is

```math
14C-k.
```

This is negative exactly when `C<=0`. Therefore ordinary integer Bellman--Ford negative-cycle detection on the transformed graph is an exact decision procedure for the original strict system.

Running that test over all order assignments gives

```math
\boxed{180\text{ cells for }M_X,\qquad208\text{ cells for }M_M.}
```

The per-Eulerian-orientation counts are an additional regression:

- `M_X`: 24 orientations support 2 cells, 6 support 6 cells, and 8 support 12 cells;
- `M_M`: 4 orientations support 4 cells, 24 support 5 cells, 8 support 7 cells, and 2 support 8 cells.

Every one of the 38 Eulerian orientations occurs, but the metric order choices are sharply restricted.

---

## 6. Conservative symmetry quotient: 42 cells

The verifier quotients only by symmetries whose action is immediate from the normalized model:

- vertex relabelings preserving `P`, `N`, and the chosen matching;
- reflection across the common anchor line.

Reflection sends `alpha` to `pi-alpha`, reverses every coherent edge orientation, and sends

```math
(A_1,A_2,B_1,B_2)
\mapsto
(B_2,B_1,A_2,A_1).
```

No sign-swapping relabeling is used in the quotient, so the count is deliberately conservative.

The exact orbit counts are

```math
\boxed{15\text{ for }M_X,
\qquad27\text{ for }M_M.}
```

Thus 42 representative local rotation cells suffice for any subsequent crossing-threshold or nonlinear-closure classification.

---

## 7. Every feasible rotation cell is nonplanar

For each accepted cell, delete the anchor half-edge from each exceptional-face disk and retain the cyclic order

```math
A_1,A_2,B_1,B_2
```

of the four relation-train endpoints. This is an orientable rotation system for `R=K_6\setminus M`.

The exact dart permutation gives the following genera:

```math
\begin{array}{c|ccc}
&g=1&g=2&g=3\\ \hline
M_X&36&60&84\\
M_M&32&72&104.
\end{array}
```

There are no genus-zero cells.

Consequently a global stopped-train realization cannot draw all twelve internal relation trains without crossings. More quantitatively, suppose the train drawing has `X_K` transverse strict-rhombus crossings among those twelve trains. Resolve each crossing by adding one handle. This produces an embedding with the same vertex rotation system on an orientable surface of genus at most `X_K`. Since the rotation system itself has genus `g_K`,

```math
\boxed{X_K\ge g_K.}
```

Thus every live collapsed block must contain at least one internal relation-train crossing; cells of genus two or three require at least two or three such crossings respectively.

Across the 388 labelled cells, the lower-bound distribution is

```math
68\text{ cells with }g=1,
\quad132\text{ with }g=2,
\quad188\text{ with }g=3.
```

This is a global train-integrability restriction absent from the isolated six-pentagon closure system.

---

## 8. Relation to the certified root and the next target

The existing certified collapsed local root has relation rotation genus two. The later Jordan certificate proves something stronger for its rigorous parameter box: the crossing pattern required by its rotation system cannot be supplied by the permitted train directions, so that whole box is globally nonintegrable.

The present theorem does not make that conclusion for the other 41 symmetry orbits. It supplies the finite framework needed to do so.

For two projective directions, a strict unit-rhombus crossing requires

```math
{\pi\over3}<\angle_{\rm proj}(e,f)\le {\pi\over2},
```

which in the representatives `alpha in (0,pi)` is equivalent to

```math
\boxed{
{\pi\over3}<|\alpha_e-\alpha_f|<{2\pi\over3}.
}
```

In scaled coordinates this is simply

```math
1<|x_e-x_f|<2.
```

Those are again rational strict difference inequalities. Therefore the next classification can subdivide the 42 cells exactly along the two threshold hyperplanes for each relevant train pair, apply the Jordan-separator criterion to each resulting crossing cell, and use the six nonlinear vector-closure equations only on crossing cells that survive topology.

**Disposition:** the collapsed support-six endpoint is now a finite 42-orbit rational rotation-cell problem before nonlinear closure. Every surviving local cell has positive ribbon genus and therefore requires actual internal train crossings in any global source. This is a proved candidate, not a promotion and not a C-II closure.

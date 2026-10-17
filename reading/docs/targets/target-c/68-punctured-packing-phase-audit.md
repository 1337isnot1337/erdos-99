> Generated reading edition · [exact source](../../../../docs/targets/target-c/68-punctured-packing-phase-audit.md) · source SHA-256 `b43bc3fbdab2918315721fa0c3c7057527fc86057a0c994ac33e8eb493aaccdd`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target C — punctured packing / global phase audit

This module replaces the annular external-population route by a direct finite-packing
argument on the **full source hull with the strict-rhombus interiors punctured out**.
It is valid for every post-ZF C-II survivor, with arbitrary Woodall topology,
`d_H`, `s_Z`, exceptional contact faces, outer pockets, and contact-isolated source
points.  No force-bulk theorem and no annular Voronoi estimate is used.

**LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.**

---

# 68. Boundary-order global rhombus defect from a punctured finite packing

Retain the canonical Section 67 notation.  Let

- `A` be the full `n`-point source and `K=conv(A)` its full source hull;
- `D=diam(A)`;
- `R_4` be the number of bounded quadrilateral faces of the positive contact core;
- for every such face `R`,
  
  ```math
  \epsilon_R:=\operatorname{area}(R)-a_0>0,
  \qquad a_0={\sqrt3\over2};
  ```

- `E_4=sum_R epsilon_R`; and
- `c_0=sqrt(3)/4=a_0/2`.

Section 67 proves two facts needed below:

1. every bounded quadrilateral contact face is a convex unit rhombus; and
2. its interior contains no additional source point.

Put

```math
\delta_K:={\pi D^2\over4}-\operatorname{area}(K)\ge0.
\tag{68.1}
```

The main theorem is

```math
\boxed{
E_4+\delta_K<c_0\operatorname{per}(K)
\le {\pi\sqrt3\over4}D.
}
\tag{68.2}
```

Thus every post-ZF survivor has only boundary-order **total** strict-rhombus area
excess, even if a quadratic population lies outside the force hull.  In particular,
external rattlers are not a leading-order escape for rhombus/phase transport.

The proof uses one classical finite-packing theorem at its exact Euclidean scale:
R. L. Graham, H. S. Witsenhausen and H. J. Zassenhaus,
*On tightest packings in the Minkowski plane*, Pacific J. Math. 41 (1972),
699–715, Theorem 4.  Its Euclidean specialization is independently restated and
scoped in Section 68.1.

## 68.1 External finite-packing theorem at the exact normalization

For a finite plane simplicial complex `S`, let

- `alpha_0(S)` be its number of vertices;
- `A(S)` be the area invariant;
- `P(S)` be the Graham–Witsenhausen–Zassenhaus perimeter invariant; and
- `chi(S)` be its Euler characteristic.

Their Theorem 4 states, for a finite packing in a Minkowski plane,

```math
\alpha_0(S)
\le {A(S)\over2\Delta_*}+{P(S)\over2}+\chi(S),
\tag{68.3}
```

where `Delta_*` is the minimum area of a unit equilateral triangle in the norm.
For Euclidean distance,

```math
\Delta_*={\sqrt3\over4},
```

so (68.3) becomes

```math
\boxed{
a_0\alpha_0(S)
\le A(S)+c_0P(S)+a_0\chi(S).
}
\tag{68.4}
```

The paper defines a finite packing by requiring distance at least one for the
relevant vertex pairs in the support.  Every vertex used below is an original source
point, and the source is globally unit-separated, so this hypothesis is automatic.

A scope point matters for the proof below.  `P(S)` is not merely the geometric
perimeter of the two-dimensional part.  A one-dimensional nonbounding edge is paid
twice by the invariant.  This is exactly what is needed when two deleted rhombus
faces share an edge, or when a deleted face meets the outer hull along an edge.
The audit below tracks those multiplicities explicitly rather than treating shared
boundary pieces as if they disappeared.

## 68.2 Build the punctured full-source complex

Start with a straight triangulation of `K` whose vertex set contains every point of
`A`, and refine it so that every unit-contact edge bounding a quadrilateral contact
face is an edge of the triangulation.  This can be done without Steiner vertices:
all constrained edges come from the planar contact graph, their interiors do not
cross, every convex-hull vertex is a source point, and any remaining source point can
be inserted by edge subdivision or stellar subdivision.

For each bounded quadrilateral contact face, choose one diagonal and triangulate the
rhombus by that diagonal.  Its endpoints are source points, hence the diagonal has
length at least one.  Distinct bounded contact-face interiors are disjoint, so all of
these local choices are compatible.

Now delete, for every quadrilateral face, the interiors of its two triangular
2-faces and delete the chosen diagonal.  Retain the four unit sides and all vertices.
Call the resulting finite plane simplicial complex `S^o`.

Section 67's no-hidden-source-point theorem is essential here: no source point is
lost when a rhombus interior is punctured.  Therefore

```math
\boxed{\alpha_0(S^o)=n.}
\tag{68.5}
```

Its support is exactly

```math
|S^o|=K\setminus\bigcup_R\operatorname{int}(R).
```

## 68.3 Exact area, perimeter, and Euler bookkeeping

The deleted rhombi have pairwise disjoint interiors and total area

```math
\sum_R\operatorname{area}(R)=a_0R_4+E_4.
```

Hence

```math
\boxed{
A(S^o)=\operatorname{area}(K)-a_0R_4-E_4.
}
\tag{68.6}
```

Before puncturing, a triangulated convex disk has Euler characteristic one.  For each
rhombus puncture we remove two 2-faces and its one chosen diagonal 1-face, while all
four boundary edges and all vertices remain.  Thus `alpha_1` drops by one and
`alpha_2` drops by two, decreasing Euler characteristic by exactly one.  Therefore

```math
\boxed{\chi(S^o)=1-R_4.}
\tag{68.7}
```

For the perimeter invariant, the unpunctured triangulated disk contributes exactly
`per(K)`.  Each deleted rhombus contributes one additional unit of perimeter for each
of its four side occurrences.  This remains true in every incidence case:

- if the opposite side of a rhombus edge remains two-dimensional, that edge changes
  from interior to boundary and is counted once;
- if two deleted rhombi share the edge, both side occurrences are retained and the
  final edge is nonbounding, so the GWZ perimeter invariant counts it twice; and
- if a deleted rhombus side lies on `partial K`, it changes from an outer boundary
  edge to a nonbounding edge, increasing its multiplicity from one to two.

Consequently

```math
\boxed{P(S^o)=\operatorname{per}(K)+4R_4.}
\tag{68.8}
```

This multiplicity audit is the point that the older annular report left implicit in
its touching-boundary discussion.

## 68.4 The rhombus count cancels identically

Apply (68.4) to `S^o` and substitute (68.5)–(68.8):

```math
\begin{aligned}
a_0n
&\le
\operatorname{area}(K)-a_0R_4-E_4
+c_0\bigl(\operatorname{per}(K)+4R_4\bigr)
+a_0(1-R_4)\\
&=
\operatorname{area}(K)+c_0\operatorname{per}(K)+a_0-E_4,
\end{aligned}
\tag{68.9}
```

because `4c_0=2a_0`.  Thus every occurrence of `R_4` cancels **exactly**.

The canonical strict translated-triangular-lattice comparison for a global
minimum-diameter source is

```math
\boxed{a_0(n-1)>{\pi D^2\over4}.}
\tag{68.10}
```

Equivalently,

```math
a_0n>{\pi D^2\over4}+a_0.
```

Compare this with (68.9), cancel `a_0`, and use the definition of `delta_K`:

```math
E_4+\delta_K<c_0\operatorname{per}(K).
```

Finally Cauchy's convex perimeter–diameter inequality gives
`per(K)<=pi D`, proving (68.2).  `square`

## 68.5 Immediate consequences

Both terms on the left of (68.2) are nonnegative.  Hence

```math
\boxed{E_4=O(D),\qquad \delta_K=O(D).}
\tag{68.11}
```

The second statement was already available from the full-source geometry stack; the
first is new at this level of generality.  It is independent of `Z_ext`, `d_H`,
`s_Z`, `q`, the Woodall branch, and the force-hull area deficit.

In particular, Section 67's conditional implication

```text
Z_ext=o(D^2)  ->  E_4=o(D^2)
```

is superseded for the rhombus term by the unconditional stronger statement

```text
all post-ZF survivors  ->  E_4=O(D).
```

Section 67 remains independently useful for its exact inside-force-hull population
ledger and its low-`h` external-population floor.

## 68.6 Global boundary-order phase cut

For each strict unit rhombus choose its acute angle

```math
\theta_R={\pi\over3}+\delta_R,
\qquad 0<\delta_R\le{\pi\over6}.
\tag{68.12}
```

Its area excess is

```math
\epsilon_R=\sin\left({\pi\over3}+\delta_R\right)-a_0.
```

Concavity of `sin` on `[pi/3,pi/2]` puts the graph above its endpoint chord, so

```math
\epsilon_R
\ge {6(1-a_0)\over\pi}\,\delta_R.
\tag{68.13}
```

Let

```math
\Delta_{train}:=\sum_R\delta_R.
```

Summing (68.13) gives

```math
\boxed{
{3\Delta_{train}\over\pi}
\le(2+\sqrt3)E_4
< (2+\sqrt3)c_0\operatorname{per}(K).
}
\tag{68.14}
```

Now form the train-crossing multigraph of the strict rhombus faces.  A train has a
projective direction `phi_v in R/pi Z`; at a rhombus crossing, orient the crossing so
that

```math
\phi_v-\phi_u\equiv{\pi\over3}+\delta_e\pmod\pi.
```

At a right-angle crossing choose either orientation once and retain that choice.
Reduce every train direction modulo `L=pi/3`.  Each oriented crossing then marks on
the circle `R/LZ` a positive arc of length `delta_e`.  For a cut point `s`, delete the
crossings whose marked arc contains `s`.  Averaging over `s` gives

```math
{1\over L}\int_0^L|F_s|\,ds
={\Delta_{train}\over L}={3\Delta_{train}\over\pi}.
```

Hence some cut deletes at most

```math
\boxed{
|F_s|
\le\left\lfloor{3\Delta_{train}\over\pi}\right\rfloor
\le\lfloor(2+\sqrt3)E_4\rfloor
=O(D).
}
\tag{68.15}
```

Lift every reduced direction to `x_v in (s,s+L)`.  Every retained oriented crossing
satisfies

```math
x_v-x_u=\delta_e>0.
\tag{68.16}
```

Thus the retained oriented train graph is acyclic and carries an exact real phase
potential.  This is the phase-cut mechanism re-proved here at the full post-ZF scope;
it does not assume a pure rhombic disk, one coherent grain, or `s_Z=0`.

## 68.7 What the theorem changes

The old all-topology picture after Section 67 still allowed the possibility that a
quadratic external population paid for a quadratic total rhombus defect.  Equation
(68.2) removes that possibility completely.  External population may remain
quadratic, but the entire strict-rhombus angular/area defect is boundary-order.

The live obstruction is therefore no longer annular capacity.  After deleting only
`O(D)` rhombus-crossing relations, every remaining train component has an exact phase
potential.  What is **not** yet proved is a multi-grain globalization theorem:
several linearly sized phase-coherent components can still share the quadratic
rhombus mass, and an `O(D)` interface set is large enough to separate such grains.
The canonical Target B dominant-component theorem does not by itself exclude this.

A useful next theorem must do one of the following:

1. charge every macroscopic phase interface to canonical Target C currencies
   (`e_BB`, `x_B`, `Q`, `s_C`, `d_H+s_Z`) strongly enough to leave one dominant
   coherent grain;
2. aggregate the existing Target B grid/penetration inequalities over all retained
   phase components without losing the boundary-order budget; or
3. turn the global real phase potential into a diameter-decreasing finite competitor
   while respecting all active diameter constraints.

## 68.8 Regression and dependency audit

- **External rattlers:** all retained as vertices of `S^o`; no force-bulk assumption.
- **Exceptional bounded faces:** retained in the support and triangulated normally.
- **Outer pockets / force-hull deficit:** irrelevant to the punctured-complex proof.
- **Shared rhombus edges:** safe because the GWZ perimeter invariant counts a final
  nonbounding edge twice; (68.8) keeps both face-side occurrences.
- **Rhombus touching `partial K`:** safe for the same reason; the side's perimeter
  multiplicity increases from one to two after puncturing.
- **Positive `s_Z` and both Woodall branches:** unused by the proof and therefore fully
  retained.
- **Near-equilateral shears:** genuine regression.  A triangle-free oblique rhombic
  grid can make each `epsilon_R` arbitrarily small, so `E_4=O(D)` is not itself a
  contradiction and no uniform positive per-face gap is asserted.
- **GWZ equality classification:** not used.  The proof imports only Theorem 4's exact
  packing inequality.

## 68.9 Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Puncture every bounded quadrilateral contact face out of the full source hull K.
Section 67 guarantees each is a unit rhombus and hides no source point.
For the resulting finite plane simplicial packing S^o:
    alpha_0 = n,
    A(S^o) = area(K)-a0 R_4-E_4,
    P(S^o) = per(K)+4R_4,
    chi(S^o) = 1-R_4.
GWZ Theorem 4 in Euclidean normalization says
    a0 alpha_0 <= A+c0 P+a0 chi.
Since 4c0=2a0, every R_4 term cancels:
    a0 n <= area(K)+c0 per(K)+a0-E_4.
Strict global lattice comparison then gives
    E_4+delta_K < c0 per(K) <= (pi sqrt(3)/4)D.
Hence E_4=O(D) in every post-ZF branch, regardless of Z_ext.

The phase-circle cut is re-proved directly:
    |F_cut| <= floor((2+sqrt(3)) E_4) = O(D),
and the retained train-crossing graph has an exact acyclic real phase potential.

Next obstruction: multi-grain globalization / interface charging, not external
population capacity.
```

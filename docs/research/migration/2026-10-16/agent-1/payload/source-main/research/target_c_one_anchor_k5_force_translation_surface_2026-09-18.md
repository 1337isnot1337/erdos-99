# Target C-II — the minimal reciprocal `K_6` glues to an orientable six-pentagon translation surface

**Date:** 2026-09-18  
**Status:** proved candidate; theorem-state authority unchanged  
**Scope:** the unit-force reciprocal `K_6` forced by a degree-pure minimal one-anchor `K_5` dual block  
**Depends on:** `target_c_one_anchor_k5_reciprocal_unit_force_2026-09-18.md`; `target_c_one_anchor_k5_reciprocal_turn_gap_2026-09-18.md`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The unit-force reciprocal equilibrium has a useful global encoding.  At each reciprocal
vertex, its five incident unit force vectors form a closed equilateral pentagon.  The
force on edge `ij` at the other endpoint is the exact negative vector.  Therefore the
six force pentagons glue pairwise by translations along all fifteen sides.

The result is a compact orientable translation surface with six equilateral pentagonal
2-cells and dual adjacency graph exactly `K_6`.  Consequently its genus is an integer
between one and five and the number of vertex classes is restricted to

\[
\boxed{9,7,5,3,\text{ or }1.}
\]

This removes the nonorientable/projective-plane combinatorial embedding of `K_6` from
the minimal dual endpoint and converts the remaining block into a finite list of
orientable rotation-system genera, with the source-derived `<120`-degree corner data on
five of the six pentagons.

---

## 1. Six closed force pentagons

For reciprocal points `y_0,...,y_5`, put

\[
f_{ij}:={y_i-y_j\over\lambda_{ij}}.
\]

The reciprocal theorem gives

\[
|f_{ij}|=1,
\qquad
f_{ji}=-f_{ij},
\qquad
\sum_{j\ne i}f_{ij}=0
\tag{1.1}
\]

for every `i=0,...,5`.

No two force vectors at one reciprocal vertex are projectively parallel.  Indeed a
parallel pair would make the corresponding three reciprocal points collinear, already
excluded by the reciprocal theorem.

Sort the five vectors `f_ij` by their arguments.  Because their sum is zero they cannot
lie in a closed semicircle: a supporting linear functional nonnegative on such a
semicircle would have nonnegative sum, and equality would force all five vectors onto
one line, contradicting the no-parallel property.  Hence every cyclic angular gap is
strictly below `pi`.

The sorted vectors therefore form, head to tail, the boundary of a strict convex
unit-sided pentagon `P_i`.  For `i=1,...,5`, this force pentagon has exactly the same
oriented side-vector set and cyclic order as the corresponding physical contact
pentagon.  For `i=0`, it is an auxiliary reciprocal force pentagon.

---

## 2. Edge pairings are translations

Label the side of `P_i` with vector `f_ij` by the unordered edge `{i,j}`.  In `P_j` the
side with the same label has vector

\[
f_{ji}=-f_{ij}.
\]

Thus the two equal-length sides are parallel with opposite boundary orientations.  They
can be identified pointwise by a translation, reversing the boundary parameter as
required for an orientation-preserving surface gluing.

Do this for every one of the fifteen unordered pairs `{i,j}`.  Every pentagon side is
paired exactly once.  The quotient therefore has no boundary and has

\[
F=6,
\qquad
E=15.
\tag{2.1}
\]

All transition maps away from the identified vertices are translations.  Hence the
quotient is an orientable translation surface, possibly with cone singularities at the
vertex classes.

The six pentagonal cells are pairwise adjacent along exactly one side, so the dual
adjacency graph of this cell structure is `K_6`.

---

## 3. Genus and vertex-class count

Let `V_s` be the number of vertex classes after the side identifications and let `g` be
the genus of the orientable quotient.  Euler's formula gives

\[
V_s-15+6=2-2g,
\]

so

\[
\boxed{V_s=11-2g.}
\tag{3.1}
\]

The dual graph `K_6` cannot be embedded on the sphere, so `g>=1`.  Also `V_s>=1`, so
`g<=5`.  Consequently

\[
\boxed{
g\in\{1,2,3,4,5\},
\qquad
V_s\in\{9,7,5,3,1\}.
}
\tag{3.2}
\]

In particular the six-pentagon block cannot realize a nonorientable projective-plane
cellulation: the force-vector edge pairings carry a canonical orientation and
translation structure.

---

## 4. Cone-angle accounting

Let a surface vertex class `v` have cone angle `Theta_v`.  Translation holonomy implies

\[
\Theta_v=2\pi m_v,
\qquad
m_v\in\mathbb Z_{>=1}.
\tag{4.1}
\]

Every equilateral pentagon has interior-angle sum `3pi`, so the six cells have total
corner angle

\[
18\pi.
\]

Therefore

\[
\boxed{
\sum_v m_v=9.
}
\tag{4.2}
\]

Together with (3.1),

\[
\sum_v(m_v-1)=2g-2,
\tag{4.3}
\]

which is the expected translation-surface curvature identity.

For the five non-ground cells `P_1,...,P_5`, the source-separation theorem proved in the
reciprocal turn-gap note gives exterior turns below `2pi/3`, hence physical interior
angles strictly above `pi/3`.  Thus any surface vertex class containing six or more
corners from the five physical pentagons cannot be a regular `2pi` point; it must have
`m_v>=2`.

No corresponding `>pi/3` lower bound is asserted for corners contributed by the
auxiliary ground force pentagon `P_0`.

---

## 5. Frontier effect

The minimal five-face dual block is now constrained at three levels simultaneously:

1. reciprocal metric equilibrium: a six-point straight-line `K_6` with unit force on
   every edge and signed inverse-distance stress rank at most three;
2. local source geometry: the five non-ground force pentagons have every exterior turn
   below 120 degrees; and
3. global force topology: the six force pentagons must assemble into an orientable
   translation surface of genus `1,...,5`, with exactly `11-2g` vertex classes and cone
   orders summing to nine.

This does not exclude the block.  It makes the remaining classification finite on the
combinatorial side: one may enumerate orientable rotation systems of `K_6` in the five
possible genera and test them against the reciprocal straight-line order type, the
unit-force equations, and the strict source corner inequalities.  A contradiction for
all such systems would remove the sharp `K_5` equality case from the one-anchor corank
bound.

No theorem-state file is changed.

**Disposition:** encoded the minimal reciprocal obstruction as an orientable
six-equilateral-pentagon translation surface, forcing genus `1<=g<=5`, vertex-class
count `V_s in {9,7,5,3,1}`, and integer cone-angle data `sum m_v=9`.  C-II remains
open.
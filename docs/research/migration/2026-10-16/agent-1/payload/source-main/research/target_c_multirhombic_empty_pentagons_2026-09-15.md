# Target C-II — Branch R forces a linear population of multi-rhombic empty pentagons

**Date:** 2026-09-15  
**Status:** proof-only exact incidence strengthening  
**Scope:** modern high-`t` Branch R in the canonical full-core/no-macroscopic-container Type-II branch  
**Dependencies:** modern singleton/rhombic train-slack dichotomy; modern all-train pentagon sea; isolate-host face degree-`>=7` theorem  
**Certificate:** `research/verify_target_c_multirhombic_empty_pentagons_t18623.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The modern Branch R theorem gives a large number `I_5` of strict-rhombus/pentagon boundary incidences, but its published conversion uses only the crude capacities

\[
I_5/2
\]

for distinct rhombic trains and

\[
I_5/5
\]

for distinct pentagons touched at least once.

There is another useful consequence.  The total number of pentagons is itself bounded above by the exceptional defect budget `Q`, because every pentagon contributes one unit to

\[
Q=\sum_P(\deg P-4).
\]

Therefore a large `I_5` cannot be spread over arbitrarily many singly touched pentagons.  A linear population must have several rhombic sides.

At the widest modern endpoint `t<=1.8623`, Branch R forces more than

\[
\boxed{0.1652D-o(D)}
\]

pentagons with at least two strict-rhombus neighbors and more than

\[
\boxed{0.0260D-o(D)}
\]

pentagons with at least three strict-rhombus neighbors.  Every one of these faces is source-empty by the degree-`>=7` isolate-host theorem.

A pentagon with at least three marked sides has two adjacent marked sides, so the latter population gives linearly many **empty double-rhombic pentagon corners**.

---

## 1. Incidence notation

For each bounded pentagonal contact face `P`, let

\[
d_R(P)\in\{0,1,2,3,4,5\}
\]

be the number of its boundary sides whose opposite face is a strict unit rhombus.

Then the strict-rhombus/pentagon incidence count is exactly

\[
\boxed{I_5=\sum_{P\in\mathcal P_5} d_R(P).}
\tag{MR.1}
\]

Put

\[
X_2:=\#\{P:d_R(P)\ge2\},
\qquad
X_3:=\#\{P:d_R(P)\ge3\}.
\tag{MR.2}
\]

Let `P_5=|\mathcal P_5|`.

---

## 2. Two elementary incidence inequalities

Pentagons outside `X_2` contribute at most one incidence, while a pentagon in `X_2` contributes at most five.  Hence

\[
I_5
\le (P_5-X_2)+5X_2
=P_5+4X_2.
\]

Therefore

\[
\boxed{X_2\ge {I_5-P_5\over4}.}
\tag{MR.3}
\]

Likewise, pentagons outside `X_3` contribute at most two incidences, while members of `X_3` contribute at most five.  Thus

\[
I_5
\le2(P_5-X_3)+5X_3
=2P_5+3X_3,
\]

so

\[
\boxed{X_3\ge {I_5-2P_5\over3}.}
\tag{MR.4}
\]

Every pentagon contributes one unit to `Q`, hence

\[
\boxed{P_5\le Q.}
\tag{MR.5}
\]

Combining (MR.3)--(MR.5),

\[
\boxed{X_2\ge {I_5-Q\over4},}
\tag{MR.6}
\]

\[
\boxed{X_3\ge {I_5-2Q\over3}.}
\tag{MR.7}
\]

No geometric independence assumption is used here.

---

## 3. Insert the modern Branch R envelopes

Use the exact modern constants

\[
C_{707}=2\sqrt{\Delta_2}+0.007707,
\qquad
\Delta_2={\pi\over2\sqrt3},
\]

and

\[
\tau_0=0.7467921.
\]

At an endpoint `t<=T`, the current all-train pentagon theorem gives

\[
{f\over D}
\ge {C_{707}\over2}-{T\over4}-o(1),
\tag{MR.8}
\]

\[
{Q\over D}
\le2T-\pi+o(1),
\tag{MR.9}
\]

and therefore

\[
{P_5\over D}
\ge2{f\over D}-{Q\over D}
-o(1).
\tag{MR.10}
\]

In Branch R, the modern train-slack theorem gives

\[
{I_5\over D}
\ge5\left(2{f\over D}-{Q\over D}\right)-\tau_0-o(1).
\tag{MR.11}
\]

Insert the same outward `f` lower and `Q` upper bounds in (MR.11), then use (MR.6)--(MR.7).  The exact companion certificate gives:

\[
\begin{array}{c|c|c}
T & X_2/D\text{ lower} & X_3/D\text{ lower}\\ \hline
1.850  & 0.2098 & 0.0936\\
1.855  & 0.1917 & 0.0661\\
1.860  & 0.1736 & 0.0386\\
1.8623 & 0.1652 & 0.0260.
\end{array}
\tag{MR.12}
\]

All four rows have positive exact outward-rational margin.  In particular, throughout the widest certified modern Branch R range,

\[
\boxed{X_2>0.1652D-o(D),}
\tag{MR.13}
\]

\[
\boxed{X_3>0.0260D-o(D).}
\tag{MR.14}
\]

---

## 4. These are genuinely empty geometric holes

The isolate-host face theorem proves that a bounded contact face containing any source point in its interior must have degree at least seven.  Hence every pentagon in `X_2` or `X_3` satisfies

\[
\boxed{A\cap\operatorname{int}P=\varnothing.}
\tag{MR.15}
\]

Thus (MR.13) is a linear population of empty unit-edge pentagonal holes with at least two rhombic sides, and (MR.14) is a linear population with at least three rhombic sides.

---

## 5. Three rhombic sides force a double-rhombic corner

The five sides of a pentagon form a 5-cycle under side adjacency.  An independent set in that cycle has size at most two.  Therefore any set of at least three rhombus-adjacent sides contains two consecutive sides.

Consequently every pentagon counted by `X_3` has a vertex at which **both incident pentagon sides border strict rhombi**.

Call such a face-corner pair a double-rhombic pentagon corner.  Different pentagons give different face-corner pairs, so (MR.14) yields

\[
\boxed{
\text{Branch R contains }>0.0260D-o(D)
\text{ empty pentagons with a double-rhombic corner}
}
\tag{MR.16}
\]

through `t<=1.8623`.

At the complete currently valid O--O path endpoint `t<=1.860`, the stronger row of (MR.12) gives

\[
\boxed{>0.0386D-o(D)}
\tag{MR.17}
\]

such pentagons.

This is a face count, not necessarily a count of distinct source vertices: several pentagons may share one contact vertex.

---

## 6. Frontier effect

The modern train-slack dichotomy can now be written more geometrically as

```text
Branch S:
    >0.373D singleton stopped trains;

Branch R through t<=1.8623:
    >0.390D^2 Mantel deficit;
    >0.622D rhombic stopped trains ending at pentagons;
    >0.1652D source-empty pentagons with >=2 rhombic sides;
    >0.0260D source-empty pentagons with >=3 rhombic sides;
    hence >0.0260D explicit empty double-rhombic pentagon corners.
```

The last object is local and finite: two strict rhombi meet the boundary of one empty convex unit pentagon at a common pentagon vertex.  This is a more specific target for a deformation or angular-defect argument than an arbitrary rhombus/pentagon incidence.

No claim is made yet that a double-rhombic corner forces a unit triangle, a uniform angular defect, or a strict same-cardinality competitor.  Near-degenerate pentagons remain a genuine regression.

**Disposition:** proved a linear multi-rhombic empty-pentagon population in modern Branch R. C-II and Level I remain open.

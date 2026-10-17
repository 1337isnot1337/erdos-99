> Generated reading edition · [exact source](../../../docs/reports/target_c_isolate_adjusted_local_return_2026-09-25.md) · source SHA-256 `01582ceebc960a5de1933897d6642589daec71d39cf7af31364f875d03498cea`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-75881EF22FF9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_isolate_adjusted_local_return_2026-09-25.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=45871b068edd2c5dc694372924aa41bb1486e6ed; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — isolate-adjusted harmonic return and global paid-area budget

**Date:** 2026-09-25  
**Repository commit:** `15cd5d8a8346b42101b355afebd6da28ccd58886`  
**State version:** `2026-09-14.audit.51`  
**Run type:** closing proof / source-level synthesis  
**Target:** C-II  
**Starting status:** canonical Sections 77, 83, 120--123; full-core and macroscopic-container branches open  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`  
**External literature search:** no theorem imported  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

## 1. Starting canonical endpoint and implication chain

In the full-core branch, canonical Section 122 requires

$$
\liminf_{D\to\infty}D^{-1}\sum_r(L_r+P_{{\rm exc},r}-2d_r)
\ge \frac{\pi}{2}(2-\sqrt3).
\tag{1}
$$

The exact source-preserving closure still needs an incompatible upper bound, an
exact unit triangle, or a same-cardinality strict sub-`D` competitor. The
candidate chain tested here was

```text
Oler with the actual isolates inside each harmonic cell
    -> isolate-adjusted local return currency
    -> full-source boundary-order budget for that same currency
    -> a sharp enough aggregate/moment constraint
    -> contradiction or source-preserving strict competitor.
```

The first two arrows are proved below. The last two do not follow from the
available constants. This is a finite source-level candidate, not Level I
closure.

## 2. Isolate-adjusted local theorem

**Classification:** proved candidate awaiting independent audit; noncanonical.

Fix a canonical unloaded positive-contact component `I_r`, its loaded
attachment polygon `P_r`, and the induced harmonic graph of Section 121. Keep
that section's `L_r`, `p_r`, `d_r`, `f_r`, `Q_r`, `P_exc,r=4f_r+Q_r`, and strict
rhombus area `A_{4,r}`. Put `G_r=area(P_r)-A_{4,r}`. Choose one global
assignment of each contact-isolated source point of `F` to a containing cell
or complement region. An isolate strictly inside a cell is assigned to that
cell; for a point on a shared boundary choose one containing region. Within
each cell, assign its selected isolates to one local bounded face or
added-side outer pocket whose closure contains them. Let `Z_r` be the number
assigned to the cell. Then

$$
\boxed{
T_r:=G_r-a_0Z_r
\ge c_0[(L_r-p_r)+(2f_r+Q_r)]
\ge\frac{3c_0}{5}(L_r+P_{{\rm exc},r}-p_r)\ge0,
}
\tag{2}
$$

where `a_0=sqrt(3)/2` and `c_0=sqrt(3)/4`. In particular, actual isolates do
not appear as an additive error in the local return inequality.

For the Section-120 pair of specified outer-walk occurrences, with chord
length `r`, direction `q`, and signed projection moment `M_r(q)`, (2) gives

$$
\boxed{
M_r(q)\ge 2A_{4,r}-{d_r\over2}
\left[p_r-2r+{5T_r\over3c_0}\right].
}
\tag{3}
$$

This is the corrected finite Section-121 moment inequality with its area error
replaced by the **paid** gap `T_r`. It makes no assertion that `T_r=o(d_r)`.

### Proof of (2)

Canonical Section 121 convexifies the local outer face by adding the missing
sides of `P_r`. It partitions `P_r` into strict unit rhombi, old bounded
nonquadrilateral faces, and convex outer pockets. A strict unit rhombus contains
no additional source point: either diagonal cuts it into two triangles, each
with one rhombus vertex joined by unit sides to the other two. By strict
convexity of the unit disk centered at that first vertex, every point of that
triangle other than its vertices is at distance less than one from it.
Equivalently, this is the empty-rhombus part of the canonical Section-67
source classification. Thus every isolate counted by
`Z_r` lies in a nonquadrilateral face or an outer pocket. An isolate on an
added polygon side can be assigned to either adjacent closed region and is
included in Oler's point set there; it is never counted twice.

For an old bounded nonquadrilateral face of degree `m=4+t`, its boundary has
`m` distinct unit-contact vertices, perimeter `m`, and contains `z` assigned
isolates. Oler's finite inequality applied to all `m+z` actual source points
in its closure gives

$$
\operatorname{area}(C)-a_0z
\ge a_0(m-1)-c_0m=c_0(m-2)=c_0(2+t).
\tag{4}
$$

For an added-side outer pocket `C`, let `k_C` count its old boundary source
vertices, `P_C` its Euclidean perimeter, and `z_C` its assigned isolates.
The same Oler inequality gives

$$
\operatorname{area}(C)-a_0z_C
\ge a_0(k_C-1)-c_0P_C.
\tag{5}
$$

If `h` polygon sides were added, Section 121's exact occurrence identities are
`sum_C k_C=L_r+2h-a_r`, `sum_C P_C=L_r+2L_add-p_r`, and
`p_r=c_partial+L_add` with `h=a_r-c_partial`. Summing (5) and using
`a_0=2c_0` yields

$$
\sum_C[\operatorname{area}(C)-a_0z_C]\ge c_0(L_r-p_r).
\tag{6}
$$

The face and pocket areas sum to `G_r`, while their assigned isolate counts
sum to `Z_r`. Summing (4) and (6) proves the first inequality in (2). The
second is Section 121's exact algebra:

$$
5[(L_r-p_r)+(2f_r+Q_r)]
-3[(L_r-p_r)+(4f_r+Q_r)]
=2[(L_r-p_r)+(Q_r-f_r)]\ge0.
$$

Here `L_r>=p_r` and `Q_r>=f_r`. Finally Section 120 gives
`d_r(L_r+P_exc,r-2r)>=4A_{4,r}-2M_r(q)`; combine this with
`L_r+P_exc,r-p_r<=5T_r/(3c_0)` to obtain (3). Every step uses the
occurrence-counted local walk; no global boundary injectivity is assumed.

## 3. Finite full-source budget for the paid gaps

**Classification:** proved candidate awaiting independent audit; noncanonical.

Use global canonical notation: `F` is the loaded force hull, `N_F` is the
number of all source points in `F`, `m` the nonisolated positive-contact core
population, `A_4` all strict-rhombus area, `A_4^0` unloaded-only strict-rhombus
area, `E_4=A_4-a_0R_4>=0`, `f` the number of global bounded
nonquadrilateral contact faces, `q=|B|`, `k=d_H+s_Z`, and
`P_F=per(F)`. Set `Z_cell=sum_r Z_r`. Then every canonical post-ZF C-II source
satisfies the finite bound

$$
\boxed{
0\le\sum_rT_r
<a_0(\pi D+f+q-k)-E_4
 +(A_4-A_4^0)+c_0\left(P_F+\sum_rp_r\right)
 -a_0d_{\rm tile},
}
\tag{7}
$$

The right side is `O(D)` by canonical Sections 62, 68, 77, 83, and 122.
In particular `sum_r T_r=O(D)` with **no** assumption on `Z_cell`.

### Proof of (7)

Canonical Section 77.12 gives `A_F-a_0N_F<a_0 pi D-a_0`, and Sections
77.20--77.25 give

$$
A_4=a_0R_4+E_4,
\quad m=R_4+f+q-k+1,
\quad Z_{ch}=N_F-m.
$$

Consequently, with `A_ch=A_F-A_4`,

$$
A_{ch}-a_0Z_{ch}
<a_0(\pi D+f+q-k)-E_4.
\tag{8}
$$

The convex attachment cells have pairwise disjoint interiors and all their
vertices are among the strictly convex-position loaded vertices of `F`
(canonical Section 83). Their sides therefore form a noncrossing chord
subdivision of `F`. Besides the cells themselves, its positive-area faces are
convex complement polygons `C_j`. Write `A_out` for their total area and
`Z_out` for the isolates assigned to their closures, so that

$$
A_F=\sum_r\operatorname{area}(P_r)+A_{out},
\qquad Z_{ch}=Z_{cell}+Z_{out}.
\tag{9}
$$

Each complement polygon has loaded source vertices on its boundary. Apply
Oler to those vertices together with its assigned isolates, ignoring any
other source points. If its perimeter is `p_j`, the resulting weak bound is
`area(C_j)-a_0z_j>=a_0(b_j-1)-c_0p_j`, where `b_j` is its number of
loaded boundary vertices. The polygon-dissection identity of canonical
Section 123 gives

$$
\sum_j(b_j-2)=q-2-\sum_r(a_r-2)=d_{\rm tile}.
$$

Thus `sum_j(b_j-1)=d_tile+t`, with `t` the number of complement polygons.
Every complement-side occurrence is either a side of `F` or a side of one
attachment cell, so

$$
A_{out}-a_0Z_{out}
\ge a_0(d_{\rm tile}+t)-c_0\sum_jp_j
\ge a_0d_{\rm tile}-c_0\left(P_F+\sum_rp_r\right).
\tag{10}
$$

Canonical Section 122 assigns every unloaded-only strict rhombus to exactly
one induced harmonic graph, whence `sum_r A_{4,r}>=A_4^0`. The exact area and
population decomposition (9) now gives

$$
\begin{aligned}
\sum_rT_r
&=\sum_r\operatorname{area}(P_r)-\sum_rA_{4,r}-a_0Z_{cell}\\
&=(A_{ch}-a_0Z_{ch})
 +(A_4-\sum_rA_{4,r})-(A_{out}-a_0Z_{out})\\
&\le (A_{ch}-a_0Z_{ch})+(A_4-A_4^0)
 +c_0(P_F+\sum_rp_r)-a_0d_{\rm tile}.
\end{aligned}
\tag{11}
$$

Insert (8) to prove (7). The lower bound is (2) summed. Canonical Section
122 gives `A_4-A_4^0=O(D)` because only `O(D)` rhombi touch loaded
vertices. Section 62 gives `sum_r p_r=O(D)`; Section 77 gives
`f+q-k=O(D)` and `P_F<=pi D`; Section 68 gives `E_4=O(D)`. Thus the
finite right side is boundary order. The proof is valid even if `Z_cell` is
larger than linear.

### Aggregate consequence

Define the explicit right side of (7) as `U_D`. Equations (2) and (7) give

$$
\boxed{
\sum_r(L_r+P_{{\rm exc},r}-2d_r)
< {5U_D\over3c_0}+\sum_r(p_r-2d_r)=O(D).
}
\tag{12}
$$

The `O(D)` scale of the aggregate detour also follows from existing Euler
ledgers. The new content of (7)--(12) is the **paid-area and moment** control:
the local Section-121 error can be charged to boundary-order full-source
currency even when a cell contains many isolates. The coefficients in (12)
are not low enough to contradict (1).

## 4. Scope, dependencies, and hostile checks

This proof uses the actual canonical source, its loaded hull, and its actual
attachment cells. It does not turn a scaffold into a source, alter any point,
or infer global optimality from a local configuration. Contact-isolated points
are retained and assigned exactly once. The finite statements rely on the
canonical post-ZF representative; (1) additionally requires the full-core
Type-II branch.

Canonical dependencies are `C-ATTACH-CURRENCY` (Section 62), the full-source
chamber saturation (Section 77), `C-HARMONIC-CELL-TILING` (Section 83),
`C-ANISOTROPIC-TWO-ARC-RETURN` (Section 120),
`C-LOCAL-RETURN-OLER-BRIDGE` (corrected finite Section 121), and
`C-AGGREGATE-TWO-ARC-DETOUR` (Section 122), with the polygon-dissection
identity from `C-AUGMENTED-CELL-DEFECT-BUDGET` (Section 123). Oler's inequality is used in the
same finite normalization as Sections 77 and 121. No external equality or
uniqueness theorem is imported.

The previous unpromoted isolate-payment report
`docs/reports/target_c_isolate_paid_aggregate_detour_2026-09-14.md` bounded
`sum G_r` by `a_0 Z_cell+O(D)` and then retained a `Z_cell` term in its
detour bound. Equation (2) pays those same isolates on the **lower** side of
the local Oler inequality, so (7) cancels the population term. This corrects
that report's stated isolate obstruction for the aggregate upper-bound route;
its finite inequalities are not thereby rejected. The remaining obstacle is
the sharp coefficient/source deformation, not proving `Z_cell=o(D)` merely
to obtain an `O(D)` aggregate bound.

Checks against binding regressions:

| Regression | Treatment |
| --- | --- |
| Contact-isolated source points | Included in `Z_r` or `Z_out`; never deleted or put in the ZR/ZF kernel. |
| Repeated outer-walk vertices and bridges | Only the canonical occurrence identities are used. |
| Loaded-touching rhombus double counts | Only unloaded-only area `A_4^0` is claimed injective. |
| Withdrawn Section-121 normalization | (3) retains `T_r/d_r`; (7) gives `O(1)` for a macroscopic `d_r`, not `o(1)`. |
| Source versus scaffold and global optimality | All geometry comes from the actual source; no competitor is claimed. |
| Boundary isolates on added chords | Assigned once to one closed Oler region; no extra source point is created. |

## 5. Failed closure attempts and exact remaining lemma

The direct scalar substitution of (7) into (12) fails: `U_D/D` has positive
allowance from the force-hull perimeter, loaded-touching rhombi, and
complement-cell boundary, while `sum_r(p_r-2d_r)` may itself be linear for a
round cell. In particular, a disk-like cell has `p_r-2d_r\sim(\pi-2)d_r`,
already larger than the Section-122 coefficient
`pi(2-sqrt(3))/2`. The finite paid-gap theorem also does not integrate a
KKT-flat direction into a strict feasible diameter decrease.

A precise next bridge is:

> For every full-core canonical Type-II survivor with the Section-122 return
> floor, prove a *sharp source-level coupling* of the paid gaps `T_r`, the
> convexity excess `sum_r(p_r-2d_r)`, and the actual loaded
> diameter/contact graph that makes the right side of (12) smaller than
> `pi(2-sqrt(3))D/2`, **or** uses a positive term in that right side to build
> a same-cardinality feasible source of diameter strictly below `D`.

For the Section-120 anisotropic moment route, the narrower missing lemma is
`T_r=o(d_r)` on a macroscopic cell, or an explicit coefficient on `T_r/d_r`
small enough to cross its moment threshold. Requiring `G_r=o(d_r)` without
paying isolates is unnecessarily strong and may be false.

## 6. Claim audit table

| Claim | Classification | Dependency and limit |
| --- | --- | --- |
| Local paid return (2) and moment (3) | proved candidate awaiting independent audit | Section 121 convexification and Section 120; finite actual cell. |
| Global paid budget (7) | proved candidate awaiting independent audit | Sections 62, 77, 83, 122; all post-ZF C-II sources. |
| Full-core Level I closure | not proved | Bound (12) has no contradictory coefficient or finite competitor. |
| `Z_cell=o(D)` is needed for boundary-order aggregate detour | rejected as a necessary step | (2), (7), and existing Euler ledgers give `O(D)` without it. |

## 7. Literature and computation

No external theorem beyond the repository's already imported finite Oler
inequality is used. No computation or numerical certificate is used.

## 8. Promotion recommendation and handoff

**Unreviewed.** Seek independent audit of boundary-isolate assignment, the
convex complement partition in (9)--(10), and the exact local Oler sum (4)--(6).
Do not change `docs/STATE.md`, the manifest, or the active prompt before such
an audit and a demonstrated frontier effect.

The strongest new result is the finite local isolate-adjusted return and its
global paid budget, (2)--(7). The canonical chain is Sections
62 + 77 + 83 + 120--123. The exact remaining obligations are the sharp
paid-gap/convexity/loaded-graph coupling or a source-preserving strict
sub-`D` construction, plus the separate macroscopic-container branch.

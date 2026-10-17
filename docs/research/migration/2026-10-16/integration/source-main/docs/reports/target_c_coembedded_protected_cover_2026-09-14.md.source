<!-- theorem-state: {"artifact_id":"ART-1C7B62A041B3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Co-embedded protected-erosion regression

**Date:** 2026-09-14
**Repository commit:** ef941ab2b44aa393bdc461926769247b45754202
**State version:** 2026-09-14.audit.47
**Run type:** audit / computation / regression
**Target:** C-II
**Starting status:** canonical Sections 122–123 frontier
**Active prompt:** docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md
**External literature search:** used in the surrounding run; no theorem imported here
**Computation:** used (research/verify_target_c_coembedded_protected_cover.py)

## LEVEL I STATUS

STILL OPEN

## 1. Starting canonical endpoint

The current canonical C-II route starts with the macroscopic-container/full-core dichotomy of
C-INACTIVE-DICHOTOMY and C-FULLCORE-NEAR-DISK. In the full-core branch, the promoted
Sections 122–123 statements are

\[
\liminf_{D\to\infty}\frac1D\sum_r
 (L_r+P_{{\rm exc},r}-2d_r)\ge\frac{\pi}{2}(2-\sqrt3)
\]

and

\[
\sum_rP_{{\rm exc},r}\le 10(e_{BB}-k).
\]

Their uncancelled source-level quantity is the aggregate outer-walk detour
\(\sum_r(L_r-2d_r)\). In the macroscopic-container branch, the canonical near-matching
and deep-matching results provide many close isolate pairs, but do not provide a finite
source-preserving exchange or a strict smaller-diameter competitor.

The checkout now also contains the canonical full-core diameter-budget floor
C-FULLCORE-DIAMETER-BUDGET-FLOOR: with
\(\mu_D=(e_{BB}+2s_C-3(d_H+s_Z))/D\), every full-core sequence satisfies
\(\liminf\mu_D\ge1\). This removes the subunit-\(\mu_D\) subbranch, but it does
not bound the remaining \(\mu_D\ge1\) regime and does not apply to Type I.

This regression tests whether even a genuine unit-contact shell with a dense strict
interior and full inner-window coverage can be ruled out by a one-point protected
exchange. The chain is:

co-embedded shell plus strict interior
    -> exact feasibility, linear chamber capacity slack, and quadratic near-unit matching
    -> one-point erosion-cover exchange still has no forced strict descent
    -> the one-point protected-exchange closure is insufficient; a collective exchange,
       an exact triangle, or a global source-preserving diameter decrease remains needed.

## 2. Strongest genuinely new result

**Classification:** regression

### Statement

Let \(\Lambda=\mathbb Z u+\mathbb Z v\), where
\(u=(1,0)\) and \(v=(1/2,\sqrt3/2)\). For \(t\ge0\), let \(H_t\) be the regular
hexagon whose axial-coordinate description is

\[
H_t=\{iu+jv:(i,j)\in\mathbb R^2,\ \max(|i|,|j|,|i+j|)\le t\}.
\]

For an integer \(R\ge10\), define

\[
B_R=\{iu+jv\in\Lambda:\max(|i|,|j|,|i+j|)=R\},
\]

\[
h_R=1+\frac1{2R},\qquad
Z_R=h_R\bigl(\Lambda\cap H_{R-2}\bigr),\qquad
A_R=B_R\cup Z_R.
\]

Then:

1. \(|B_R|=6R\), \(|Z_R|=1+3(R-2)(R-1)\), and
   \[
   |A_R|=3R^2-3R+7.
   \]

2. \(A_R\) is unit-separated and triangle-free. Its shell \(B_R\) has a
   \(6R\)-edge unit-contact cycle.

3. \(\operatorname{diam}(A_R)=2R\), with the diameter attained by opposite shell
   vertices.

4. If \(C_R=H_R\), then the one-unit inner parallel body is exactly
   \[
   (C_R)_{-1}=H_{R-2/\sqrt3},
   \]
   and every point of the larger hexagon \(H_{R-1}\) is within distance strictly
   less than one of a point of \(Z_R\). In particular, every point of the eroded
   chamber is covered:
   \[
   H_{R-1}\subseteq\bigcup_{z\in Z_R}B(z,1)
   \quad\text{and}\quad
   (C_R)_{-1}\subseteq\bigcup_{z\in Z_R}\overline B(z,1).
   \]

5. The unscaled triangular-lattice capacity exceeds the strict interior population by
   only
   \[
   \bigl|\Lambda\cap H_R\bigr|-\bigl|\Lambda\cap H_{R-2}\bigr|=12R-6,
   \]
   while \(Z_R\) contains an explicit matching of
   \(m(2m+1)\) pairs at distance \(h_R=1+1/(2R)\), where
   \(m=\lfloor(R-3)/2\rfloor\). This matching is quadratic in \(R\).

   The full source is inclusion-maximal in \(C_R\), because the shell covers
   \(H_R\setminus H_{R-1}\). Its total deficit from the unscaled window capacity is
   \[
   \bigl|\Lambda\cap H_R\bigr|-|A_R|=6R-6.
   \]

This is a fixed-container feasible regression. It is not a global minimum-diameter
certificate and does not assert that \(A_R\) is a minimizer for its cardinality.

### Scope

The source is the full finite set \(A_R\), including every shell point and every
strict-interior point. The shell is an actual unit-contact core; the interior points
are contact-isolated from the shell and from one another. The container is the fixed
convex hexagon \(C_R\). All claims are finite and uniform for every integer \(R\ge10\).
The cover claim concerns the full continuous chamber, not merely sampled points, and
the inclusion-maximality claim concerns the entire container.

The configuration is deliberately not presented as a candidate global minimizer. It has
no global optimality certificate; related shell/interior families have smaller
same-cardinality competitors.

### Proof

The axial window \(H_t\) is a regular hexagon of circumradius \(t\) and inradius
\(\sqrt3\,t/2\). The six boundary chains of the integer window \(H_R\cap\Lambda\)
contain \(R\) unit edges each, so \(|B_R|=6R\). The standard axial count gives

\[
|\Lambda\cap H_s|=1+3s(s+1)
\]

for integer \(s\), hence the displayed formula for \(|Z_R|\) and then for \(|A_R|\).

Every nonzero difference of two points of \(\Lambda\) has squared length
\(i^2+ij+j^2\), an integer at least one. Distances inside \(Z_R\) are therefore
at least \(h_R>1\). Put

\[
b=h_R(R-2)=R-\frac32-\frac1R.
\]

Every point of \(Z_R\) lies in \(H_b\). A shell point lies on a side of \(H_R\), and
the distance between the corresponding parallel side lines of \(H_R\) and \(H_b\) is

\[
\frac{\sqrt3}{2}(R-b)
=\frac{\sqrt3}{2}\left(\frac32+\frac1R\right)>1
\]

for \(R\ge10\). Thus every shell/interior pair is strictly farther than one. The
unit edges within the shell are exactly the two boundary-neighbor edges at each
shell vertex, forming one cycle. There are no unit edges inside \(Z_R\), so the
whole source is triangle-free.

Both sets lie in \(H_R\). Opposite shell vertices \((R,0)\) and \((-R,0)\) are in
\(B_R\) and are \(2R\) apart. Since the diameter of \(H_R\) is \(2R\), this proves
\(\operatorname{diam}(A_R)=2R\).

For erosion, each side of \(H_R\) is at inradius \(\sqrt3 R/2\). Moving every side
inward by one changes the inradius to \(\sqrt3 R/2-1\), which is the inradius of
\(H_a\), where

\[
a=R-\frac2{\sqrt3}.
\]

Thus \((H_R)_{-1}=H_a\). The convex hull of \(Z_R\) is \(P=H_b\). Put

\[
\delta=a-b=\frac32-\frac2{\sqrt3}+\frac1R,\qquad
s=\frac{\sqrt3}{2}\delta.
\]

For \(R\ge10\), \(\delta>0\) and

\[
\delta\le\frac85-\frac2{\sqrt3}<\frac9{20}.
\]

The last strict inequality is exact because \(2/\sqrt3>23/20\), as
\(4/3>529/400\). Also \(h_R\le21/20\).

If \(x\in P\), the scaled elementary triangular-lattice triangles tile \(P\),
including its boundary. Every such equilateral triangle has side \(h_R\) and
circumradius \(h_R/\sqrt3<1\), so every point of \(P\) is within one of one of
its three vertices in \(Z_R\).

Now let \(x\in H_a\setminus P\), and let \(y\) be its Euclidean projection onto
the convex polygon \(P\).

If \(y\) lies in the relative interior of a side, then \(x-y\) is normal to that
side and its length is at most the distance \(s\) between the corresponding
supporting lines of \(H_a\) and \(P\). The source points on that side of \(P\) form
an arithmetic progression with spacing \(h_R\), including both endpoints. Choose
the nearest one, say \(z\); its tangential distance from \(y\) is at most \(h_R/2\).
The two components are orthogonal, hence

\[
|x-z|^2\le s^2+\frac{h_R^2}{4}
=\frac34\delta^2+\frac14h_R^2
<\frac34\left(\frac9{20}\right)^2
 +\frac14\left(\frac{21}{20}\right)^2
=\frac{171}{400}<1.
\]

If \(y\) is a vertex, let \(n_1,n_2\) be the two outward unit normals of its
incident sides. They make an angle of \(60\) degrees. Since \(x-y\) lies in the
normal cone, write

\[
x-y=\alpha n_1+\beta n_2,\qquad \alpha,\beta\ge0.
\]

The two supporting inequalities for \(H_a\) give

\[
\alpha+\frac{\beta}{2}\le s,\qquad
\frac{\alpha}{2}+\beta\le s.
\]

The squared norm is \(\alpha^2+\beta^2+\alpha\beta\). On the resulting polygon
in the \((\alpha,\beta)\)-plane, its maximum occurs at an extreme point: it is
\(s^2\) at \((s,0)\) and \((0,s)\), and \(4s^2/3=\delta^2\) at
\((2s/3,2s/3)\). Therefore \(|x-y|\le\delta<1\). The vertex \(y\) is itself a
source point of \(Z_R\), so \(x\) is covered.

This proves the full continuous erosion inclusion.

The same projection proof gives a stronger inclusion. Replace \(a\) by \(R-1\) and
put

\[
\delta_1=(R-1)-b=\frac12+\frac1R\le\frac35.
\]

The inner-hull vertex case is then bounded by \(\delta_1<1\). In the side case the
source point on the corresponding boundary row has distance squared at most

\[
\frac34\delta_1^2+\frac14h_R^2
\le\frac34\left(\frac35\right)^2
+\frac14\left(\frac{21}{20}\right)^2
=\frac{873}{1600}<1.
\]

Therefore \(H_{R-1}\) is covered strictly by the disks centered at \(Z_R\). It remains
to cover the outer band. The hexagon \(H_{R-1}\) is the inner parallel body of \(H_R\)
at Euclidean depth \(\sqrt3/2\). Hence every \(x\in H_R\setminus H_{R-1}\) has
\(\operatorname{dist}(x,\partial H_R)<\sqrt3/2\). Let \(y\) be a nearest boundary
point. If \(y\) is in the relative interior of a side, the shell points on that side
have spacing one, so a nearest shell point has tangential distance at most \(1/2\),
and its squared distance from \(x\) is strictly less than

\[
\left(\frac{\sqrt3}{2}\right)^2+\left(\frac12\right)^2=1.
\]

If \(y\) is a vertex, it is itself in \(B_R\), and its distance from \(x\) is less than
\(\sqrt3/2<1\). Thus the shell covers the outer band by open unit disks. Together
with the strict \(Z_R\)-cover of \(H_{R-1}\), this proves that \(A_R\) is
inclusion-maximal in \(H_R\).

For the matching, let \(m=\lfloor(R-3)/2\rfloor\). For each
\(j=-m,\ldots,m\), pair

\[
(-m+2k,j)\quad\text{with}\quad(-m+2k+1,j),
\qquad k=0,\ldots,m-1.
\]

All these points lie in \(H_{R-2}\), the pairs are mutually vertex-disjoint, and
each pair has lattice difference \(u\). After scaling, each pair has distance
\(h_R=1+1/(2R)\). Their number is \(m(2m+1)=\Theta(R^2)\). The capacity difference
is the direct count

\[
(1+3R(R+1))-(1+3(R-2)(R-1))=12R-6.
\]

The proof is complete.

### Dependencies

- C-INACTIVE-DICHOTOMY, canonical, docs/targets/target-c/79-inactive-chamber-rhombic-saturation-dichotomy-audit.md. It supplies the canonical global branch split; it is not used as a premise for the finite construction.
- C-FULLCORE-NEAR-DISK, canonical, docs/targets/target-c/80-global-isolate-concentration-fullcore-disk-audit.md. It supplies the canonical exterior-cap/full-core orientation; it is not used to claim global optimality here.
- C-AGGREGATE-TWO-ARC-DETOUR, canonical, docs/targets/target-c/122-aggregate-two-arc-detour-audit.md. Its scope is the canonical full-core representative; no part is silently applied to this regression.
- C-AUGMENTED-CELL-DEFECT-BUDGET, canonical, docs/targets/target-c/123-augmented-cell-defect-budget-audit.md. Its payment is for the canonical loaded harmonic-cell source and is not asserted for this shell/interior source.
- C-FULLCORE-DIAMETER-BUDGET-FLOOR, canonical, docs/reports/target_c_fullcore_diameter_budget_floor_2026-09-14.md, independently audited in docs/audits/target_c_fullcore_diameter_budget_floor_independent_audit_2026-09-14.md. It removes only the full-core subunit-\(\mu_D\) regime and is not used to assert anything about this Type-I-style fixed-container regression.
- research/verify_target_c_coembedded_protected_cover.py uses exact integer and Fraction arithmetic for all displayed finite checks. The continuous cover is supplied by the geometric proof above, not by floating-point sampling.

## 3. Exact frontier effect

No canonical theorem-state entry is advanced. This is a stronger regression against a
specific one-point closure mechanism:

- the contact boundary is genuine and triangle-free;
- the quadratic strict interior is co-embedded in the same container;
- the full \(H_{R-1}\) inner window is covered by strict interior unit disks, and the
  shell covers the remaining outer band;
- the chamber capacity slack is only linear;
- the entire source is inclusion-maximal in the fixed chamber despite a linear
  population deficit from the lattice-window capacity;
- there are quadratically many near-unit interior pairs.

Thus “linear slack plus protected one-point inner-window cover” does not itself force an
exact equilateral triangle or a strict diameter decrease. The regression does not show
that the canonical global minimizer can realize this exact geometry.

## 4. Exact remaining lemma

A valid C-II closure still needs a source-level statement of the following form:

For every sufficiently large triangle-free global minimizer in either the macroscopic
container branch or the full-core branch, the canonical source, with contact-isolated
points retained, admits either an exact unit equilateral triangle or a finite deformation
or replacement with exactly the same cardinality, all pairwise distances at least one
throughout, and final diameter strictly below the minimizer's \(D(n)\).

For the macroscopic branch, the missing implication is collective: convert the many
deep near-unit pairs and macroscopic container geometry into a jointly compatible
source-preserving motion or a globally smaller competitor.

For the full-core branch, the missing implication remains an upper bound on
\(\sum_r(L_r-2d_r)\), an exact triangle forced by carrier or loaded-diameter geometry,
or a source-preserving strict descent from the forced non-rhombic area. The newly
canonical floor \(\liminf\mu_D\ge1\) removes only the subunit-\(\mu_D\) regime; it
does not supply this remaining implication.

## 5. Claim audit table

| Claim | Status | Reason |
| --- | --- | --- |
| Finite shell/interior source is unit-separated and triangle-free | regression | exact lattice geometry and exhaustive finite checks |
| Source has diameter \(2R\) | regression | opposite shell vertices attain the chamber diameter |
| Full \(H_{R-1}\) inner window is covered by \(Z_R\) | regression | side and vertex projection proof |
| Outer band is covered by \(B_R\) | regression | inner parallel depth \(\sqrt3/2\), side spacing one |
| Full source is inclusion-maximal in \(H_R\) | regression | the two preceding covers partition the container |
| Linear capacity slack coexists with quadratic strict interior and near-unit matching | regression | exact formulas |
| One-point protected exchange closes Type I | rejected mechanism | no strict descent or exact triangle follows |
| The finite source is a global minimizer for \(|A_R|\) | unproved/rejected as a claim | no global optimality certificate |
| Regression realizes every canonical C-II survivor | unproved | no realization theorem |
| C-II is solved | false | aggregate detour and collective exchange remain open |

## 6. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
| --- | --- | --- |
| Shell contact graph | pass | exactly \(6R\) edges and degree two at every shell vertex |
| Inner strict separation | pass | triangular-lattice quadratic form and \(h_R>1\) |
| Shell/interior separation | pass | support gap \((\sqrt3/2)(3/2+1/R)>1\) |
| Full \(H_{R-1}\) inner-window cover | pass | side bound \(873/1600\), vertex bound below \(3/5\) |
| Outer band cover | pass | inner parallel depth \(\sqrt3/2\), side spacing one |
| Full-source inclusion maximality | pass | the two preceding covers partition \(H_R\) |
| Quadratic matching | pass | \(m(2m+1)\) disjoint pairs at distance \(1+1/(2R)\) |
| Prior coarse homothety-cover draft | rejected and repaired | wrong sign in the \(1/R\) term; no downstream theorem used it |
| Global-minimality bridge | unresolved | fixed-container feasibility does not imply minimum diameter |
| Exact source-cardinality descent | unresolved | no jointly compatible multi-point exchange |

## 7. Literature imports

No external theorem is load-bearing in this report. The surrounding search checked the
official Erdős Problem #99 status page, which still lists the problem as open, and
best-packing diameter bounds of Bondarenko–Hardin–Saff. Those bounds concern arbitrary
best-packing constants and do not establish that every minimum-diameter planar minimizer
contains a unit equilateral triangle. No external result is used in the proof above.

## 8. Computation

The command

    python3 -m py_compile research/verify_target_c_coembedded_protected_cover.py
    python3 research/verify_target_c_coembedded_protected_cover.py

uses exact integer arithmetic for axial norms, quadratic lattice distances, shell edge
enumeration, and cardinalities, with Fraction arithmetic for \(h_R\), support
separation, and the rational covering margin. It reports:

    R=10:  core=60,  isolates=217,   n=277,   sigma=114,  matching=21,    inner_window_bound_squared=873/1600 total_capacity_slack=54
    R=20:  core=120, isolates=1027,  n=1147,  sigma=234,  matching=136,  inner_window_bound_squared=873/1600 total_capacity_slack=114
    R=40:  core=240, isolates=4447,  n=4687,  sigma=474, matching=666,  inner_window_bound_squared=873/1600 total_capacity_slack=234
    R=80:  core=480, isolates=18487, n=18967, sigma=954, matching=2926, inner_window_bound_squared=873/1600 total_capacity_slack=474
    R=160: core=960, isolates=75367, n=76327, sigma=1914, matching=12246, inner_window_bound_squared=873/1600 total_capacity_slack=954

The exact common rational bound printed by the certificate is
inner_window_bound_squared=873/1600, and the full-source capacity deficit is
total_capacity_slack=6R-6. The script does not test global optimality,
response realizability, KKT equilibrium, or a finite multi-point exchange.

## 9. Corrections / supersessions

The first proposed version of the erosion-cover certificate used the expression
\(h_R^2-3(1/2+1/R)^2\). Direct expansion shows that the homothety displacement has
a \(+1/(2\sqrt3 R)\) contribution, not the claimed negative contribution. That
coarse bound was invalid and is withdrawn. The present report replaces it with the
side-projection and vertex-projection argument; the new argument has the certified
uniform bound \(873/1600\) for the strengthened \(H_{R-1}\) cover.

No canonical theorem or prior report depended on the withdrawn expression.

## 10. Promotion recommendation

**regression/rejection only** — preserve this artifact as a finite fixed-container
regression. Do not promote it into the canonical theorem state. The script may be
listed in research/README.md and in the generated artifact index. No state-version,
route-map, prompt, or canonical dependency edits are required.

## 11. Handoff

1. Strongest new theorem: a unit-contact triangle-free shell can co-embed with a
   quadratic strict interior whose disks cover \(H_{R-1}\), while the shell covers
   the outer band, making the full source inclusion-maximal in \(H_R\). The interior
   capacity slack is \(12R-6\), the full-source deficit is \(6R-6\), and there is a
   quadratic near-unit matching.
2. Canonical chain: C-INACTIVE-DICHOTOMY / C-FULLCORE-NEAR-DISK -> C-AGGREGATE-TWO-ARC-DETOUR and C-AUGMENTED-CELL-DEFECT-BUDGET; the present artifact is a noncanonical stress test against one-point macroscopic-container closure.
3. Exact remaining lemma: a collective source-preserving finite descent or exact
   triangle for every actual global minimizer, plus the full-core aggregate-detour bridge.
4. Binding dead routes: one-anchor retraction, density-only/vanishing-shear bounds,
   square-grid local detour bounds, scalar ledger compatibility, and one-point protected exchange.
5. Files to read next: docs/targets/target-c/CURRENT.md,
   docs/targets/target-c/87-deep-near-unit-isolate-matching-audit-2026-09-12.md,
   docs/targets/target-c/122-aggregate-two-arc-detour-audit.md,
   docs/targets/target-c/123-augmented-cell-defect-budget-audit.md, and the
   concurrent report docs/reports/target_c_exterior_cap_hull_and_cover_2026-09-14.md.

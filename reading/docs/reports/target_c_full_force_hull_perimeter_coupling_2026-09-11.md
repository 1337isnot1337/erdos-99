> Generated reading edition · [exact source](../../../docs/reports/target_c_full_force_hull_perimeter_coupling_2026-09-11.md) · source SHA-256 `9acce34c10141f4f3458dc67cd9524a79836497397304e2b8b2aae1ccc8a2b78`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-66EB67AF9A45","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_full_force_hull_perimeter_coupling_2026-09-11.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=08ac8044d66c9426eeea026e973fb823536de0fc; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — full-hull/force-hull perimeter coupling at the near-π endpoint

**Date:** 2026-09-11
**Repository state at run start:** `c0e36d39b0b49b98515692d13493942fd3a47c9b`
**Run type:** closing proof / full-source convex-capacity audit
**Target:** Target C C-II, forest near-π endpoint
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`
**External web search:** not used
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`.

This report proves a source/force-hull coupling that was not stated in the merged
Target C reports at the start of this run. It uses the global perimeter saturation of the *actual full source
hull*, rather than imposing hull saturation on the C-II lexicographic representative.
It closes one geometric ambiguity at the forest near-π endpoint, but it does not
close the surplus or triangle-free population obstruction.

## 1. Starting endpoint

For a C-II source (A_j) in the C65 full-diameter-visible normalization, write

$$
D_j=\operatorname {diam}A_j,
\qquad K_j=\operatorname {conv}A_j,
\qquad F_j=\operatorname {conv}B_j,
\qquad q_j=|B_j|,
$$

where (B_j) is the loaded terminal set of the actual relative-interior KKT
stress. C65 ensures that every actual diameter endpoint belongs to (B_j), so
(F_j) has the full source diameter. Let (P_{K,j}) and (P_{F,j}) be the two perimeters. The exact endpoint
under examination is the post-ZF forest branch with (s_Z=0), (d_H>0), and

$$
\frac{q_j}{D_j}\longrightarrow \pi.
\tag{1.1}
$$

The desired closing implication was

```text
q/D -> pi
  -> full source is disk-like and force-visible
  -> all quadratic source population is controlled by the contact core
  -> contradiction with the forest surplus or a strict smaller-diameter competitor.
```

The first two arrows are proved below. The third is not: Oler saturation permits a
quadratic population of contact-isolated points, and no global operation currently
turns those points into positive contact vertices.

## 2. Strongest new theorem

### Theorem — perimeter and population coupling

Let (A_j) be any unbounded sequence of C-II sources satisfying (1.1), with all
source points retained. Then

$$
\boxed{
0\le P_{K,j}-P_{F,j}
\le \pi D_j-q_j=o(D_j).
}
\tag{2.1}
$$

Moreover,

$$
\boxed{
\frac{\operatorname {area}K_j-\operatorname {area}F_j}{D_j^2}
\longrightarrow0,
\qquad
\frac{|A_j\setminus F_j|}{D_j^2}\longrightarrow0.
}
\tag{2.2}
$$

Consequently the full source population in the force hull has the global triangular
density:

$$
\boxed{
\frac{|A_j\cap F_j|}{D_j^2}
\longrightarrow \frac{\pi}{2\sqrt3},
\qquad
\frac{\operatorname {area}F_j}{D_j^2}
\longrightarrow\frac\pi4.
}
\tag{2.3}
$$

Every normalized Hausdorff limit of (F_j) and (K_j) is the unit-diameter disk.
No conclusion is made that the positive contact core has quadratic size.

### Scope

This is a theorem about the actual C-II full source and its actual force hull. It
retains contact-isolated points in both (A_j\cap F_j) and (A_j\setminus F_j).
It does not select a hull-saturated representative, change the contact/diameter
lexicographic order, or use an independently chosen smaller optimum. The hypothesis
is the near-π loaded-terminal endpoint; it is not asserted in the cyclic branch or
for arbitrary (s_Z>0) sources.

## 3. Proof

### 3.1 The full source hull has a bounded perimeter deficit

Put

$$
a_0=\frac{\sqrt3}{2},
\qquad c_0=\frac{\sqrt3}{4}.
$$

The strict translated-triangular-lattice comparison for a global (n)-point
minimum-diameter source is

$$
D_j^2<\frac{2\sqrt3}{\pi}(n_j-1).
\tag{3.1}
$$

Finite Oler and isoperimetry give

$$
a_0(n_j-1)
\le \operatorname {area}K_j+c_0P_{K,j}
\le \frac{P_{K,j}^2}{4\pi}+c_0P_{K,j}.
\tag{3.2}
$$

Since (a_0\cdot \pi/(2\sqrt3)=\pi/4), (3.1)--(3.2) imply

$$
P_{K,j}^2+\pi\sqrt3 P_{K,j}>\pi^2D_j^2.
$$

Taking the positive root gives the finite bound

$$
P_{K,j}>\frac\pi2\left(\sqrt{4D_j^2+3}-\sqrt3\right).
\tag{3.3}
$$

In particular,

$$
0\le \pi D_j-P_{K,j}<\frac{\pi\sqrt3}{2}.
\tag{3.4}
$$

This is the global perimeter theorem already available in the Target B theorem
stack; (3.1)--(3.4) are included to make the present C-II use auditable.

### 3.2 Perimeter transfer from loaded terminals to the full hull

All loaded terminals lie on the boundary of (F_j) and occur in cyclic order.
Consecutive terminals are distinct source points, so each consecutive chord has
length at least one. Therefore

$$
q_j\le P_{F,j}.
\tag{3.5}
$$

Since (F_j\subseteq K_j), monotonicity of convex perimeter and the diameter
perimeter inequality give

$$
q_j\le P_{F,j}\le P_{K,j}\le \pi D_j.
\tag{3.6}
$$

Subtracting the middle terms proves the exact finite transfer inequality

$$
0\le P_{K,j}-P_{F,j}\le \pi D_j-q_j.
\tag{3.7}
$$

The hypothesis (1.1) proves (2.1), and also (P_{F,j}/D_j\to\pi).

### 3.3 Hausdorff limits force the two hulls to coincide

Translate and scale by (D_j), choosing one point of (F_j) as the origin. Both
normalized convex bodies lie in a fixed bounded disk. Pass to a subsequence with

$$
\widetilde F_j:=D_j^{-1}F_j\longrightarrow F_\infty,
\qquad
\widetilde K_j:=D_j^{-1}K_j\longrightarrow K_\infty
$$

in the Hausdorff metric. Convex perimeter is continuous under this convergence, so

$$
\operatorname {diam}F_\infty\le1,
\quad
\operatorname {diam}K_\infty\le1,
\quad
F_\infty\subseteq K_\infty,
\quad
\operatorname {per}F_\infty=\pi.
\tag{3.8}
$$

The width formula gives

$$
\operatorname {per}F_\infty
 =\int_0^\pi w_{F_\infty}(u)\,du.
$$

Every width is at most the diameter, hence at most one. Equation (3.8) forces

$$
w_{F_\infty}(u)=1\quad\text{for every direction }u.
\tag{3.9}
$$

Thus (F_\infty) has constant width one. It is maximal among convex bodies of
diameter at most one. To see this directly, if (x\in K_\infty\setminus F_\infty),
strict separation supplies a unit vector (u) with

$$
u\cdot x>h_{F_\infty}(u).
$$

Choose (y\in F_\infty) with

$$
u\cdot y=-h_{F_\infty}(-u).
$$

By (3.9), (h_{F_\infty}(u)+h_{F_\infty}(-u)=1). Therefore

$$
u\cdot(x-y)>1,
$$

contradicting $\operatorname {diam}K_\infty\le1$. Hence

$$
K_\infty=F_\infty.
\tag{3.10}
$$

Every subsequential pair of normalized hulls has the same limit. Continuity of
convex area therefore proves the first assertion in (2.2):

$$
\operatorname {area}K_j-\operatorname {area}F_j=o(D_j^2).
\tag{3.11}
$$

### 3.4 The external source population is subquadratic

We use the following finite annular capacity estimate. If (F\subseteq K) are
convex and (X\subseteq K\setminus F) is unit-separated, then

$$
|X|\frac\pi4
\le \operatorname {area}K-\operatorname {area}F
 +\frac12(\operatorname {per}K+\operatorname {per}F)+\frac\pi4.
\tag{3.12}
$$

For completeness, put (r=1/2). The open disks (x+rB), (x\in X), have
disjoint interiors and lie in (K+rB\setminus F_{-r}), where (F_{-r}) is the
inner parallel body. Steiner's formula and

$$
\operatorname {area}F-\operatorname {area}F_{-r}
\le r\operatorname {per}F
$$

give

$$
|X|\pi r^2
\le \operatorname {area}K-\operatorname {area}F
 +r(P_K+P_F)+\pi r^2.
$$

Substituting (r=1/2) proves (3.12).

Apply (3.12) to (X=A_j\setminus F_j). The area term is (o(D_j^2)) by
(3.11), and both perimeter terms are (O(D_j)). Hence

$$
|A_j\setminus F_j|=o(D_j^2),
$$

which proves the second assertion in (2.2). Notice that no contact-isolated point
was omitted: every point outside (F_j) is in (X), regardless of whether it has
unit contacts.

### 3.5 The force hull has disk area and global source density

The standard global asymptotic for minimum-diameter unit-separated sources is

$$
\frac{n_j}{D_j^2}\longrightarrow \Delta_2:=\frac\pi{2\sqrt3}.
\tag{3.13}
$$

By the preceding step,

$$
\frac{|A_j\cap F_j|}{D_j^2}
=\frac{n_j}{D_j^2}-o(1)
\longrightarrow\Delta_2.
\tag{3.14}
$$

Apply Oler inside (F_j) to all source points (A_j\cap F_j), including
contact-isolated points:

$$
a_0|A_j\cap F_j|
\le \operatorname {area}F_j+c_0P_{F,j}+a_0.
\tag{3.15}
$$

Divide by (D_j^2), use (3.14), (P_{F,j}=O(D_j)), and

$$
a_0\Delta_2=\frac\pi4.
$$

This yields

$$
\liminf\frac{\operatorname {area}F_j}{D_j^2}\ge\frac\pi4.
\tag{3.16}
$$

The isodiametric inequality gives the reverse inequality, so

$$
\frac{\operatorname {area}F_j}{D_j^2}\longrightarrow\frac\pi4.
\tag{3.17}
$$

Together with (3.11), the full hull has the same normalized area. Equality in the
normalized isodiametric inequality forces every Hausdorff limit in (3.10) to be the
unit-diameter disk. This proves (2.3) and the final assertion of the theorem.
$\square$

## 4. Exact target implication

The theorem removes the following geometric ambiguity from the forest near-π
endpoint:

```text
the loaded force hull could be disk-like while a quadratic source population lived
in a macroscopically different part of the full diameter hull.
```

That cannot happen at quadratic scale. The entire source hull and force hull have
the same normalized area, and all but (o(D^2)) source points lie in the force
hull. The force-hull source population is asymptotically Oler-saturated.

The theorem changes no surplus inequality. In particular it does not improve

$$
\frac{e_{BB}+2s_C-3d_H}{D}\ge0.597+\varepsilon_{597}
$$

or the cyclic lower endpoint (lambda_A+\varepsilon_A), and it gives no bound on
the positive contact-core population. The exact remaining implication would be one
of:

1. a theorem converting Oler saturation of (A_j\cap F_j) plus the actual
   triangle-free KKT contact geometry into a unit equilateral triangle;
2. a source-preserving strict competitor for an (o(D^2)) but potentially
   superlinear contact-isolated population; or
3. a common-hub/forest inequality coupling the (3d_H) charge to the now disk-like
   full source.

None is proved here.

## 5. Why the obvious closing implications fail

### 5.1 Perimeter coupling is not an exact hull identity

Equation (2.1) is only (o(D)). It does not imply (K_j=F_j) for any finite
source. A width defect can be concentrated in a small set of directions, and the
compactness argument supplies no rate that crosses the linear surplus ledger.

### 5.2 A generic area-versus-perimeter-difference inequality is false

A tempting strengthening would be

$$
\operatorname {area}(K)-\operatorname {area}(F)
\le \frac{D}{2}\bigl(\operatorname {per}K-\operatorname {per}F\bigr)
\tag{5.1}
$$

for all nested diameter-(D) convex bodies. It is false. Let (K) be the unit
disk, (D=2), and let (F_\epsilon) be the ellipse with semiaxes (1) and
(\epsilon), contained in (K). As (\epsilon\downarrow0),

$$
\operatorname {area}K-\operatorname {area}F_\epsilon\to\pi,
\qquad
\operatorname {per}K-\operatorname {per}F_\epsilon\to2\pi-4.
$$

The right side of (5.1) tends to (2\pi-4<\pi). The counterexample is not in the
near-π endpoint because (P_F/D\to2); it shows that (2.1) alone cannot be
converted into a quantitative area rate without using the near-π geometry.

### 5.3 Unit boundary edges do not force a triangle

For (m\ge2), let

$$
\theta_m=\frac\pi3+m^{-2},
\qquad
u=(1,0),
\qquad
v=(\cos\theta_m,\sin\theta_m),
$$

and

$$
A_m=\{iu+jv:0\le i,j\le m,\ i,j\in\mathbb Z\}.
$$

Every nonzero difference (au+bv) has norm at least one. If (ab<0), writing
(x=|a|,y=|b|) gives

$$
|au+bv|^2=(x-y)^2+2xy(1-\cos\theta_m)>1;
$$

the same-sign case is larger, and the unit vectors are only (pm u,pm v).
Thus (A_m) is unit-separated, its only unit differences are the grid edges, and
it has no unit equilateral triangle. Its convex hull is a parallelogram with

$$
|A_m|=(m+1)^2,
\quad
\operatorname {per}(\operatorname {conv}A_m)=4m,
\quad
\operatorname {area}(\operatorname {conv}A_m)=m^2\sin\theta_m.
$$

Since (sin(\pi/3+m^{-2})=\sqrt3/2+\frac12m^{-2}+O(m^{-4})),

$$
a_0|A_m|-\operatorname {area}(\operatorname {conv}A_m)
=\sqrt3\,m+O(1).
\tag{5.2}
$$

Therefore a linear Oler boundary term cannot be removed merely from unit boundary
edges, triangle-freeness, and a positive contact graph. This example has

$$
\frac{\operatorname {per}(\operatorname {conv}A_m)}{\operatorname {diam}A_m}
\longrightarrow\frac4{\sqrt3}<\pi,
$$

so it does not refute the near-π theorem. It is a regression against the stronger
local boundary claim that would be needed to turn (2.3) into a contact-transport
theorem.

## 6. Branch and regression audit

| Branch or regression | Result | Exact reason |
|---|---|---|
| forest, (s_Z=0), (q/D\to\pi) | theorem applies | only this endpoint is assumed |
| cyclic, (s_Z=0) | not covered | cyclic near-π perimeter report has (q/D\to\pi/2) at its equality endpoint |
| (s_Z>0) | not covered | no near-π loaded-terminal hypothesis is available |
| strict-negative transfer | retained | proof uses no transfer sign |
| zero transfer | retained | proof uses no response-kernel classification |
| contact-isolated points | retained | they are included in both Oler and annular counts |
| repeated outer-walk edges | irrelevant to proof | only convex hulls and loaded boundary points are used |
| shared diameter endpoints | irrelevant to proof | the only contact fact is pairwise source separation |
| regular odd shells | not excluded | they have (s_Z=2) and no global-optimality certificate |
| exceptional faces and whole-circuit exceptions | not excluded | no facewise surplus identity is invoked |
| sheared rhombic grid | regression survives | it has linear Oler slack despite triangle-free unit edges |

## 7. Failed routes and exact obstruction

The attempted route was

```text
full-source/force-hull perimeter equality
 -> quadratic population must be contact-visible
 -> the forest surplus contradicts global optimality.
```

The failure is the middle implication. Equations (2.2)--(2.3) control the location
and density of the full population, not its unit-contact graph. A triangular-lattice
cloud can be Oler-saturated up to (O(D)) boundary slack while all its pairwise
distances are strictly greater than one. The existing regular-shell-plus-cloud
competitor report shows that one such family is not globally optimal, but its
competitor proof uses a specific two-unit radial buffer and does not apply to an
arbitrary C-II source.

The exact remaining lemma is therefore:

> **Near-disk source-to-contact transport lemma.** In a C-II source satisfying
> (2.1)--(2.3), prove either that the (o(D^2)) contact-isolated population can be
> replaced by a strictly smaller-diameter source-preserving packing, or that the
> actual unit-contact/KKT geometry forces a unit equilateral triangle.

This must retain the forest (3d_H) charge and all source points. A density gap for
triangle-free feasible sets alone is false.

## 8. Dependencies and provenance

The proof uses:

- the promoted/shared finite Oler inequality and the strict translated-lattice
  comparison, with their hypotheses as stated in `docs/theory/03-oler-shell.md` and
  `docs/targets/target-b/01-jammed-rhombic-branch.md`;
- the elementary perimeter monotonicity, Cauchy perimeter-diameter inequality,
  width formula, Hausdorff compactness, and isodiametric inequality;
- the annular capacity estimate proved in Section 3.4, so no unpromoted report is
  needed for that step;
- the standard global asymptotic (n/D^2\to\pi/(2\sqrt3)).

No later cyclic detour estimate, pure-disk train transport, response sign claim, or
hull-saturation selection is used.

## 9. Canonical promotion recommendation

**Hold as report.** The theorem is complete and its hypotheses are explicit, but the
near-π endpoint is already represented by a specialized forest report. The present
report adds the exact finite perimeter transfer (2.1), a self-contained Oler route to
the disk-area conclusion, and the boundary-capacity regression (5.2). It should not
change the authoritative route map until independently audited against the current
forest module.

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New theorem:
  For any C-II sequence with q/D -> pi, where q is the loaded force-hull vertex count,
      0 <= per(K)-per(F) <= pi D-q = o(D).
  Convex compactness then gives area(K)-area(F)=o(D^2). The annular disk-capacity
  inequality gives |A\F|=o(D^2), and Oler inside F gives
      |A cap F|/D^2 -> pi/(2sqrt(3)), area(F)/D^2 -> pi/4.
  The normalized full and force hulls are both the unit disk.

Exact obstruction:
  Oler saturation does not imply positive contact visibility. A near-unit triangular
  cloud can be triangle-free and contact-isolated; the known competitor removes only
  buffered shell families, not arbitrary C-II sources. A sheared rhombic grid proves
  that unit boundary edges and triangle-freeness do not remove the linear Oler term.

Highest-value missing lemma:
  near-disk source-to-contact transport retaining the forest 3d_H charge and all
  contact-isolated points.

Authoritative files:
  docs/targets/target-c/56-ci-restored-frontier.md
  docs/reports/target_c_forest_near_pi_external_rattler_2026-09-11.md
  docs/reports/target_c_external_annulus_capacity_2026-09-11.md
  docs/reports/target_c_inactive_cloud_global_competitor_2026-09-11.md
```

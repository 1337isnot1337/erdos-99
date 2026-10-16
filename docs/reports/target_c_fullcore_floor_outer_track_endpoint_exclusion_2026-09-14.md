<!-- theorem-state: {"artifact_id":"ART-2D17F89212AF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fullcore_floor_outer_track_endpoint_exclusion_2026-09-14.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=2e15b9c8adff32adcc5e0831218ff22be2bdbd76; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — outer-track exclusion of the full-core train-floor endpoint

**Date:** 2026-09-14
**Repository commit:** `ef941ab2b44aa393bdc461926769247b45754202`
**State version:** `2026-09-14.audit.49`
**Run type:** closing proof / endpoint exclusion / adversarial audit
**Target:** Target C-II / Level I
**Starting status:** canonical full-core near-disk Type-II branch and the promoted
full-core train-surplus floor
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** not used
**Computation:** used only for decimal evaluation of exact constants; no logical
dependency

## LEVEL I STATUS

`STILL OPEN`

This report excludes one asymptotic endpoint of the full-core branch. It does not
exclude larger full-core surplus, the macroscopic-container branch, or all possible
global minimizers. The result is therefore not a Level-I solution.

## 1. Starting canonical endpoint

Use the canonical full-core, no-macroscopic-container, near-disk Type-II setting and
assume for contradiction that a sequence reaches the promoted train-coupled floor

\[
 \mu_D\longrightarrow \mu_{\rm TC},
 \qquad
 \Delta_2=\frac{\pi}{2\sqrt3},
 \qquad
 \mu_{\rm TC}=\frac{2\pi+2\sqrt{\Delta_2}}5.
\tag{1.1}
\]

The canonical endpoint equalities are

\[
 \frac{R_D}{D^2}\to\Delta_2,
 \quad
 \frac{b_D}{D}\to\pi,
 \quad
 \frac{f_D}{D}\to f_{\rm TC}:=\frac{4\sqrt{\Delta_2}-\pi}{5},
 \quad
 \frac{Q_D-f_D}{D}\to0.
\tag{1.2}
\]

Here `R_D` is the number of bounded strict unit-rhombus faces, `b_D` is the
occurrence-counted outer contact-face walk length, `f_D` is the number of bounded
nonquadrilateral contact faces, and `Q_D` is the sum of their degree excesses.
Let `B_D` be the occurrence-counted boundary size of the strict-rhombus complex and
`T_D=B_D/2` its train count. The canonical train-floor squeeze gives

\[
 \frac{B_D}{D}\to4\sqrt{\Delta_2},
 \qquad
 \frac{T_D}{D}\to2\sqrt{\Delta_2}.
\tag{1.3}
\]

The candidate chain is

```text
floor equality
  -> outer/nonquadrilateral boundary incidences separately saturate
  -> all but O(D) trains have both ends on the outer face
  -> endpoint phase support supplies a large outer-ended/distinct-label pair
  -> outer-ended crosscuts give an interval extraction despite holes
  -> angular-defect clustering gives one fixed phase orientation
  -> Section 76 diameter inequality contradicts the global D scale.
```

The first, second, and last arrows are proved below. The exact topological
outer-crosscut assertion is stated with its regular-neighborhood construction so that
bridges and repeated outer-face vertices are not silently discarded.

## 2. Boundary saturation leaves many outer-ended tracks

Let `H_D` be the number of strict-rhombus boundary-edge occurrences whose other side
is the old unbounded contact face, and let `I_D` be the number whose other side is a
bounded nonquadrilateral face. Every strict-rhombus boundary occurrence has exactly
one of these two recipients, so

\[
 B_D=H_D+I_D,
 \qquad
 H_D\le b_D,
 \qquad
 I_D\le4f_D+Q_D.
\tag{2.1}
\]

The upper train-boundary inequality is `B_D\le b_D+4f_D+Q_D`. Equations (1.2)--(1.3)
and

\[
 \pi+5f_{\rm TC}=4\sqrt{\Delta_2}
\tag{2.2}
\]

show that the difference between the right side of that inequality and `B_D` is
`o(D)`. Since both deficits in

\[
 (b_D-H_D)+(4f_D+Q_D-I_D)
 =b_D+4f_D+Q_D-B_D
\tag{2.3}
\]

are nonnegative, each is `o(D)`. Consequently

\[
 \frac{H_D}{D}\to\pi,
 \qquad
 \frac{I_D}{D}\to4\sqrt{\Delta_2}-\pi.
\tag{2.4}
\]

Every train has exactly two boundary-edge occurrences, including occurrences on
holes and at bridges. A train with at least one endpoint in the nonquadrilateral
recipient set consumes at least one of the `I_D` occurrences. Thus the number `G_D`
of trains whose two endpoints both face the unbounded contact face satisfies the
finite bound

\[
 G_D\ge T_D-I_D.
\tag{2.5}
\]

Using (1.3)--(2.4),

\[
 \boxed{
 \frac{G_D}{D}\ge
 \pi-2\sqrt{\Delta_2}-o(1).
 }
\tag{2.6}
\]

Set

\[
 \tau:=2\sqrt{\Delta_2},
 \qquad
 g:=\pi-2\sqrt{\Delta_2}.
\tag{2.7}
\]

Numerically, `\tau=1.9046256137...` and `g=1.2369670398...`. The estimate is only
an endpoint estimate; away from (1.1), the same outer-ended count is not asserted.

## 3. A finite phase-support calculation

The canonical phase-circle cut removes `O(D)` crossing edges and assigns every train
one of three labels. Same-label pairs are nonedges of the retained crossing graph.
At the endpoint, the Mantel stability theorem from the preceding endpoint report
gives a partition

\[
 \mathcal T_D=X_D\sqcup Y_D,
 \qquad
 |X_D|/T_D\to1/2,
 \quad |Y_D|/T_D\to1/2,
\tag{3.1}
\]

with `o(T_D^2)` missing cross edges. If `x_i=|X_D\cap\ell^{-1}(i)|` and
`y_i=|Y_D\cap\ell^{-1}(i)|`, then

\[
 \sum_i x_i y_i=o(T_D^2).
\tag{3.2}
\]

Let `g_i` be the number of outer-ended trains in `X_D` with label `i`, and `h_i`
the corresponding number in `Y_D`. By (2.6),

\[
 \sum_i(g_i+h_i)\ge(g-o(1))D.
\tag{3.3}
\]

The following elementary limiting lemma is the exact support calculation used here.

### Lemma 3.1 — outer-ended distinct-label pair

Suppose `T_D/D\to\tau`, `|X_D|/T_D,|Y_D|/T_D\to1/2`, (3.2) holds, and
`\sum_i(g_i+h_i)/D\ge g-o(1)`, with `g_i\le x_i` and `h_i\le y_i`. Then, along every
subsequence, there are distinct labels `i\ne j` and a choice of orientation of the
two Mantel sides such that one of

\[
 g_i+y_j,
 \qquad h_i+x_j
\tag{3.4}
\]

is at least

\[
 \boxed{
 \left(\frac\pi3+\frac{\sqrt{\Delta_2}}6-o(1)\right)D.
 }
\tag{3.5}
\]

In particular both selected families have cardinality bounded below by a fixed
positive multiple of `D`.

#### Proof

Pass to a further subsequence and divide all populations by `T_D`. Equation (3.2)
implies that the limiting supports of the labels on `X_D` and `Y_D` are disjoint.
Both sides have positive limiting mass, so after interchanging them if necessary
there is either one label on one side and two labels on the other, or one positive
label on each side.

In the one-plus-two case, write the one-label side's limiting mass as `1/2`, the two
labels on the other side as `y_1,y_2` with `y_1+y_2=1/2`, and its outer-ended counts
as `g,h_1,h_2`. Let `G_*=g+h_1+h_2`. Then

\[
 \max(y_1,y_2)\ge\frac14,
 \qquad
 \max(h_1,h_2)\ge\frac{G_*-g}{2}.
\tag{3.6}
\]

Therefore the largest distinct-label pair in (3.4) is at least

\[
 \max\left(g+\frac14,\frac12+\frac{G_*-g}{2}\right).
\tag{3.7}
\]

The minimum over `g` is attained when the two terms agree, and equals

\[
 \frac5{12}+\frac{G_*}{3}.
\tag{3.8}
\]

The one-plus-one case gives the larger lower bound `1/2+G_*/2`. Substituting

\[
 \frac{g}{\tau}=\frac{\pi-2\sqrt{\Delta_2}}{2\sqrt{\Delta_2}}
\tag{3.9}
\]

into (3.8), then multiplying by `\tau D`, gives

\[
 \tau\left(\frac5{12}+\frac{g/\tau}{3}\right)
 =\frac{5\sqrt{\Delta_2}}6+\frac{\pi-2\sqrt{\Delta_2}}3
 =\frac\pi3+\frac{\sqrt{\Delta_2}}6.
\]

This proves (3.5). Since each total side population is at most
`T_D/2+o(D)`, (3.5) also gives a uniform positive lower bound for each selected
family. `\square`

The label-support conclusion is used only asymptotically. No finite exact
three-color partition is inferred from (3.2).

## 4. Outer-ended interval extraction with holes

We now state and prove the topological fact needed to turn the pair from Lemma 3.1
into a complete grid. It is deliberately one-sided: only the first family must have
both endpoints on the old unbounded face.

### Lemma 4.1 — one-sided outer-crosscut interval lemma

Let `\mathcal A` be a finite family of pairwise disjoint train centerlines in a
finite planar contact complex. Assume every member of `\mathcal A` has both terminal
edge midpoints on the unbounded face of the complex. Let `\mathcal B` be a family of
pairwise disjoint train centerlines, with arbitrary terminal faces. Assume every
`A`--`B` pair crosses at most once. Then there is an ordering of `\mathcal A` such
that, for every `B\in\mathcal B`, the set of members of `\mathcal A` crossed by `B` is
a consecutive interval. This remains true with holes, bridges, and repeated
occurrences in the unbounded-face walk.

#### Proof

Take a closed topological disk `U` containing the finite contact complex in its
interior. The unbounded face is connected. For each terminal midpoint of an
`A`-centerline, choose a narrow arc in the unbounded face from that midpoint to a
small outer collar of `\partial U`. Choose the arcs in the collar and in the face
successively, perturbing them at repeated vertices, so that all such terminal arcs
are pairwise disjoint and avoid all train-centerline interiors. This is the standard
regular-neighborhood construction for a finite planar embedding: a boundary edge
occurrence is represented by a distinct small side of the face, so a bridge or a
repeated vertex creates parallel collar sides rather than a crossing.

Append the two chosen terminal arcs to each member of `\mathcal A`, and, if needed,
continue them a short distance in the collar to `\partial U`. The resulting arcs
`\widehat A` are pairwise disjoint proper crosscuts of `U`. The appended pieces lie
in the unbounded face and therefore do not meet any train-centerline in the finite
complex. The crosscuts divide `U` into a linear chain of regions

\[
 U\setminus\bigcup\widehat A=R_0\cup\cdots\cup R_a,
\tag{4.1}
\]

where consecutive regions share exactly one crosscut. As a `B` centerline is
traversed, its region index changes by `+1` or `-1` whenever it crosses a
`\widehat A`. Any walk on the line of regions in (4.1) visits a connected interval
of the line: if it visits regions on both sides of `R_i`, it must cross the boundary
crosscut between them. Hence the set of crosscuts met by `B` is an interval. The
pairwise-at-most-once hypothesis identifies this with the set of members of
`\mathcal A` crossed by `B`; no common crossing sign is needed here. The construction
also never assumes that the other endpoint of `B` lies on the outer face. `\square`

The common phase orientation is not used in Lemmas 4.1--4.2. It is imposed only
after the complete product is extracted, in Section 5, where angular-defect
clustering provides a fresh short phase arc without deleting all trains incident to
the original phase cut.

### Lemma 4.2 — near-complete one-sided extraction

Under the hypotheses of Lemma 4.1, suppose `|\mathcal A|=a`, `|\mathcal B|=b` and the
number `q_D` of missing actual crossings satisfies `q_D=o(ab)`, with
`a,b=\Theta(D)`. Then there are subfamilies

\[
 \mathcal A_0\subset\mathcal A,
 \qquad
 \mathcal B_0\subset\mathcal B,
\tag{4.2}
\]

such that every `A\in\mathcal A_0` crosses every `B\in\mathcal B_0` and

\[
 |\mathcal A_0|=a-o(D),
 \qquad
 |\mathcal B_0|=b-o(D).
\tag{4.3}
\]

#### Proof

By Lemma 4.1, the neighbors of each `B` form an interval in the ordered `A`
family. If `m_B` is its missing count, then the interval omits `m_B` members from
the two ends, and

\[
 \sum_Bm_B=q_D.
\tag{4.4}
\]

Choose `\eta_D\downarrow0` with `q_D/(\eta_D a b)\to0`. Delete the `o(b)` members of
`\mathcal B` with `m_B>\eta_Da`. The interval of every remaining member contains the
central block obtained by deleting `\lceil\eta_Da\rceil` members at each end of
`\mathcal A`. This gives (4.3) and the complete product. `\square`

## 5. Angular-defect clustering and fixed orientation

Apply Lemma 3.1, choosing the orientation so that the outer-ended family is called
`\mathcal A_D` and the other family `\mathcal B_D`. The near-Mantel partition has
`o(T_D^2)=o(D^2)` missing cross edges, so

\[
 |\mathcal A_D||\mathcal B_D|
 -e(\mathcal A_D,\mathcal B_D)=o(D^2).
\tag{5.1}
\]

Lemma 4.2 gives a complete actual crossing product `\mathcal A_{0,D}\times
\mathcal B_{0,D}` after losing `o(D)` trains. All selected train directions lie on the
reduced phase circle. For every complete-product pair, the circular distance between
the two reduced directions is exactly the rhombus angular excess `\delta_{AB}` in
`(0,\pi/6]`. The global canonical angular-defect budget gives

\[
 S_D:=\sum_{A\in\mathcal A_{0,D}}
       \sum_{B\in\mathcal B_{0,D}}\delta_{AB}=O(D).
\tag{5.2}
\]

We use the following finite clustering observation. If two finite subsets of a circle
have complete cross-product and the sum of their pairwise circular distances is
`O(D)`, while both cardinalities are `\Theta(D)`, then deleting `o(D)` points from
each leaves both subsets in an arc of length `o(1)`. Indeed, choose a point of the
first set with average distance `O(D^{-1})` to the second set, delete the
`O(1/\eta_D)` second points farther than `\eta_D`, then choose a remaining second
point with average distance `O(D^{-1})` to the first set and delete the analogous
first points, where `\eta_D\downarrow0` and `D\eta_D\to\infty`.

After this `o(D)` loss, choose a new phase-circle cut outside the resulting short
arc. Every remaining actual crossing is then uncut, and all crossings between the two
fixed labels have one orientation. The two selected direction sets have diameter
`o(1)<\pi/6` in the reduced phase coordinate for all sufficiently large `D`.

This step does not assert that all trains in the original global source share the
new cut. It uses only the two selected complete families. Contact-isolated source
points are untouched.

## 6. Diameter contradiction at the floor endpoint

The final complete product is phase-pure, internally pairwise noncrossing, and has
one common crossing sign. Its first family is a subfamily of outer-ended tracks; the
second may have arbitrary holes, which Section 76 explicitly permits after common
order is established. Apply the hole-stable complete-grid inequality (canonical
`C-HOLE-GRID-DIAMETER`, Section 76): if the final shore sizes are `a_D,b_D`, then

\[
 D\ge
 \frac{\sqrt3}{2}(a_D+b_D)
 -\frac{S_D'}{\min(a_D,b_D)}-2,
\tag{6.1}
\]

where `S_D'=O(D)` is the angular-defect sum on the final complete product. Since both
shore sizes remain linear, the defect term is `O(1)`. The pair-size bound (3.5), the
`o(D)` extraction losses, and

\[
 \frac\pi3+\frac{\sqrt{\Delta_2}}6
 =1.2059163523\ldots
 >
 \frac2{\sqrt3}=1.1547005383\ldots
\tag{6.2}
\]

The comparison in (6.2) is an exact strict inequality, not a floating-point
assumption. With `s=\sqrt{\Delta_2}`, it is equivalent to
`2\pi+s>4\sqrt3`; for example the classical rational bounds
`\pi>31/10`, `\sqrt3<7/4`, and
`s^2=\pi/(2\sqrt3)>31/35>16/25` give
`2\pi+s>31/5+4/5=7>4\sqrt3`.

give a fixed `c>0` such that

\[
 a_D+b_D\ge\left(\frac2{\sqrt3}+c\right)D
\tag{6.3}
\]

for all sufficiently large members of the sequence. Equation (6.1) then gives
`D\ge(1+c\sqrt3/2)D-O(1)`, a contradiction.

Therefore:

\[
\boxed{
\text{No canonical full-core Type-II sequence can satisfy }
\mu_D\to\mu_{\rm TC}.
}
\tag{6.4}
\]

This is not an explicit numerical gap, but it does give an existence-only uniform gap
within the stated canonical branch. Indeed, if no `\varepsilon_C>0` and `D_C` existed
with `\mu_D\ge\mu_{\rm TC}+\varepsilon_C` for every sufficiently large member of
the branch, one could choose a sequence with `\mu_D-\mu_{\rm TC}\to0`; the endpoint
contradiction above would apply. The argument supplies no effective value of
`\varepsilon_C` or finite threshold, and it does not extend that gap to the
macroscopic-container branch.

## 7. Exact frontier effect

The previous live full-core statement was

\[
 \liminf\mu_D\ge\mu_{\rm TC}.
\]

The new result removes equality at the endpoint and, by the sequential argument just
given, yields a nonexplicit branch-uniform positive gap:

\[
\boxed{
 \exists\,\varepsilon_C>0,\ D_C<\infty:\quad
 \mu_D\ge\mu_{\rm TC}+\varepsilon_C
 \text{ for every sufficiently large canonical full-core Type-II minimizer.}
 }
\tag{7.1}
\]

The gap is existential and non-effective, not a displayed decimal or a supplied
threshold. The higher-surplus full-core branch above this gap, the macroscopic-container
branch, and the source-preserving global-minimality bridge remain live.

## 8. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| Endpoint equalities (1.2)--(1.3) | canonical input | `C-FULLCORE-TRAIN-SURPLUS-FLOOR`, `C-FULLCORE-NEAR-DISK`, `C-TRAIN-INTERFACE-CURRENCY` | promoted full-core floor and its equality ledger |
| Separate outer/nonquadrilateral saturation | proved here, report-level | finite occurrence inequalities (2.1) and endpoint squeeze | both nonnegative recipient deficits sum to `o(D)` |
| Outer-ended train count (2.6) | proved here, report-level | Theorem 10.6 train-end identity | each nonouter train consumes an interface endpoint occurrence |
| Lemma 3.1 | proved here, report-level | Mantel endpoint stability and elementary optimization | three labels have disjoint limiting side supports |
| Lemma 4.1 | candidate; topological audit required | planar regular-neighborhood completion | bridges/repeated face occurrences are addressed, but this is the binding new topology |
| Lemma 4.2 | conditional on Lemma 4.1 | interval neighborhoods plus Markov | exact complete product after `o(D)` loss |
| Angular clustering (5.2) | conditional | canonical angular-defect budget plus complete product | removes phase-cut orientation exceptions |
| Endpoint contradiction (6.4) | conditional on Lemmas 4.1--4.2 and clustering | canonical Section 76 | size margin exceeds `2/\sqrt3` |
| Level I closure | unresolved | higher-surplus, container, and source-cardinality branches | one endpoint exclusion is not uniform all-branch coverage |

## 9. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
| --- | --- | --- |
| contact-isolated source points | pass | none are deleted; only train endpoints and rhombus centers are used |
| holes and repeated outer-face walks | pass at the stated lemma scope | Lemma 4.1 uses a regular-neighborhood collar and counts boundary occurrences; it does not replace the walk by a simple polygon |
| bridges | pass at the stated lemma scope | distinct face-side collar occurrences are perturbed separately; bridge excursions only add boundary occurrences |
| anisotropic two-direction lattice | pass | it has no global-minimizer certificate and is not used as a closure counterexample |
| five-rhombus cross | pass | the endpoint count permits a finite exceptional cross; the argument is asymptotic and uses the near-Mantel endpoint mass |
| arbitrary near-Mantel graph with no linear biclique | pass | Lemma 4.2 uses interval geometry from outer-ended crosscuts, not abstract graph stability |
| phase-cut deletion edges | unresolved until clustering | they are not deleted incident trains; complete-product angular clustering is used to choose a fresh local cut |
| source/scaffold distinction | pass | the source is the original full configuration; the train complex supplies only selected source rhombi and endpoint hull bounds |
| local versus global optimality | pass | global optimality enters only through the canonical endpoint ledger and Section-76 comparison; no local jammed example is called global |

The binding hostile audit is Lemma 4.1. If its collar-completion assertion fails for a
contact complex with repeated outer-face incidences, the endpoint exclusion must be
downgraded to a conditional result. In particular, the proof does not use the false
claim that every arbitrary family of arcs in a holed domain has a single boundary
order; it first requires both endpoints of the one selected family to lie on the
unbounded face and explicitly adds collar tails.

## 10. Literature imports

No external theorem is load-bearing in this report. All imported inputs are canonical
repository results with the exact scopes listed in the claim table, especially
`C-FULLCORE-TRAIN-SURPLUS-FLOOR`, the endpoint Mantel stability report, and
`C-HOLE-GRID-DIAMETER` / Section 76.

## 11. Computation

The decimal values in (2.7) and (6.2) were evaluated from the exact expressions
`\Delta_2=\pi/(2\sqrt3)`, `g=\pi-2\sqrt{\Delta_2}`, and
`\rho=\pi/3+\sqrt{\Delta_2}/6`. No floating-point inequality is used: the symbolic
margin `\rho>2/\sqrt3` is an elementary exact inequality, and the decimals are only
orientation values.

## 12. Promotion recommendation

**unreviewed**. The outer-crosscut collar construction and the angular-clustering
transition require an independent hostile audit before any theorem-state promotion.
The report should not be used as a canonical Level-I closure.

## 13. Handoff

1. Strongest new result: conditional/report-level exclusion of the exact full-core
   train-floor endpoint, with a concrete margin from outer-ended train mass.
2. Exact dependency chain: endpoint train-floor equality → separate outer/interface
   saturation → `G_D/D\ge\pi-2\sqrt{\Delta_2}` → Lemma 3.1 → one-sided interval
   extraction → Section 76 contradiction.
3. Exact remaining lemma: independently audit whether arbitrary outer-ended train
   centerlines can be completed to disjoint crosscuts in one disk while preserving
   all `B` crossing data in the presence of bridges and repeated face incidences.
4. Binding dead routes: abstract Mantel stability without interval geometry, deleting
   all phase-cut incident trains, and any appeal to a finite global modulus from an
   asymptotic endpoint exclusion.
5. Files to read next: `docs/targets/target-c/122-aggregate-two-arc-detour-audit.md`,
   `docs/targets/target-c/123-augmented-cell-defect-budget-audit.md`,
   `docs/targets/target-c/85-train-boundary-interface-currency-audit.md`, and
   `docs/reports/target_c_fullcore_train_mantel_phase_star_endpoint_2026-09-14.md`.

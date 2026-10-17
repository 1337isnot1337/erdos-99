> Generated reading edition · [exact source](../../../docs/reports/target_c_fullcore_mantel_phase_star_refinement_2026-09-14.md) · source SHA-256 `45001ccf588572965f64e7a254b36e8205888212cc0e8be39eab7311611d6a93`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-63FDED205605","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fullcore_mantel_phase_star_refinement_2026-09-14.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=4721d5fd930342e69848db4b75ac2fe027018387; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — exact phase-star refinement at the full-core Mantel endpoint

**Date:** 2026-09-14
**Repository commit:** `ef941ab2b44aa393bdc461926769247b45754202`
**State version:** `2026-09-14.audit.49`
**Run type:** closing proof / exact asymptotic endpoint reduction
**Target:** Target C-II / Level I
**Starting status:** report-level full-core Mantel endpoint stability
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** used only for a scope check; no external theorem imported
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

This report does not solve Erdős Problem #99. It sharpens the report-level
full-core floor endpoint. The phase labels do not merely give two arbitrary
linear subfamilies: at the Mantel endpoint they force one phase class of size
(T_D/2+o(T_D)) on one Mantel shore and the other two phase classes on the
other shore. Each center-to-leaf pair is individually almost complete. After
deleting (o(T_D)) low cross-degree tracks, both shores are exactly internally
noncrossing.

The candidate chain is

```text
full-core train-floor endpoint
    -> Mantel edit partition
    -> one-versus-two phase-star concentration
    -> delete o(T) low cross-degree tracks
    -> exact internally noncrossing near-complete phase star
    -> ? holed/interface diagonal or source-preserving contradiction
```

The last arrow remains unproved.

## 1. Canonical endpoint input and scope

Work along a subsequence of canonical contact-minimal, then diameter-pair-minimal
triangle-free global-minimizer representatives in the full-core, no-macroscopic-
container Type-II branch. Let (D	oinfty). Let (mathcal R_D) be the full
strict-rhombus complex after the canonical phase-circle cut, let (T_D) be its
global train count, and let (G_D) be the simple train-crossing graph. The graph
vertices are the actual train segments; source contact-isolates are not graph
vertices and are not deleted from the source.

Assume the report-level train-floor endpoint

$$
\frac{R_D}{D^2}\to\Delta_2:=\frac{\pi}{2\sqrt3},
\qquad
\frac{T_D}{D}\to2\sqrt{\Delta_2},
\qquad
R_D=\frac{T_D^2}{4}-o(T_D^2).
\tag{1.1}
$$

The last relation is the report-level consequence of the canonical train-boundary
squeeze at (mu_D	omu_{\rm TC}); it is not being promoted here.

The canonical phase-circle cut deletes only (O(D)=o(T_D^2)) rhombus crossings
and gives every train a label in (mathbb Z/3\mathbb Z). Same-label trains
cannot cross. Thus (G_D) is triangle-free and its phase-label partition is a
proper three-partition for the retained crossing graph.

## 2. Mantel partition and exact one-versus-two phase star

The elementary Mantel stability argument gives a partition

$$
V(G_D)=X_D\sqcup Y_D
\tag{2.1}
$$

with

$$
|X_D|,|Y_D|=\frac{T_D}{2}+o(T_D),
\tag{2.2}
$$

$$
e(G_D[X_D])+e(G_D[Y_D])=o(T_D^2),
\qquad
|X_D||Y_D|-e(X_D,Y_D)=o(T_D^2).
\tag{2.3}
$$

For (iinmathbb Z/3\mathbb Z), write

$$
x_i=|X_D\cap\ell^{-1}(i)|,
\qquad
y_i=|Y_D\cap\ell^{-1}(i)|.
\tag{2.4}
$$

Since same-label cross pairs are nonedges,

$$
\sum_i x_i y_i=o(T_D^2).
\tag{2.5}
$$

Consequently

$$
\sum_i\min\{x_i,y_i\}=o(T_D).
\tag{2.6}
$$

Indeed, (min(x_i,y_i)lesqrt{x_i y_i}), and Cauchy--Schwarz over three
labels gives the claim.

Let the total phase-class sizes be

$$
M_D\ge U_D\ge V_D,
\qquad M_D+U_D+V_D=T_D.
\tag{2.7}

We use the following elementary three-partite consequence of triangle-freeness.

### Lemma 2.1 — three-partite edge bound

If a triangle-free graph has phase classes of sizes (M\ge U\ge V), then

\[
e\le M(U+V)=M(T-M).
\tag{2.8}
$$

#### Proof

Let (x=MU-e(M,U)) and (y=MV-e(M,V)) be the missing edges incident with
the largest class. For every (UV)-edge, the two endpoint neighborhoods in the
(M)-class are disjoint, so summing their degrees gives

$$
M e(U,V)\le Vx+Uy\le M(x+y).
$$

Thus (e(U,V)le x+y), and

$$
e=e(M,U)+e(M,V)+e(U,V)
\le M(U+V).
$$
$square$

By (1.1) and Lemma 2.1,

$$
\frac{T_D^2}{4}-o(T_D^2)
\le M_D(T_D-M_D)
\le\frac{T_D^2}{4}.
$$

The strict concavity of (z(1-z)) therefore gives

$$
\boxed{
\frac{M_D}{T_D}\to\frac12,
\qquad
\frac{U_D+V_D}{T_D}\to\frac12.}
\tag{2.9}
$$

Now (2.6) says every phase class is concentrated on one Mantel shore up to
(o(T_D)) tracks. Since the (M_D)-class itself has size (T_D/2+o(T_D)),
it occupies one shore, say (X_D), up to (o(T_D)). Equation (2.2) then forces
the (U_D)- and (V_D)-classes to occupy the other shore (Y_D), up to
(o(T_D)). Thus, after changing (o(T_D)) tracks,

$$
X_D=\mathcal M_D,
\qquad
Y_D=\mathcal U_D\sqcup\mathcal V_D,
\tag{2.10}
$$

where (|\mathcal M_D|=T_D/2+o(T_D)) and

$$
|\mathcal U_D|+|\mathcal V_D|=T_D/2+o(T_D).
$$

The internal (Y_D)-edges are (o(T_D^2)) by (2.3), so the center-to-leaf
crossing count obeys

$$
e(\mathcal M_D,\mathcal U_D)+e(\mathcal M_D,\mathcal V_D)
=\frac{T_D^2}{4}-o(T_D^2).
\tag{2.11}
$$

Since the two missing counts in (2.11) are nonnegative, each individual pair
satisfies

$$
\boxed{
|\mathcal M_D||\mathcal U_D|-e(\mathcal M_D,\mathcal U_D)=o(T_D^2),
\qquad
|\mathcal M_D||\mathcal V_D|-e(\mathcal M_D,\mathcal V_D)=o(T_D^2).}
\tag{2.12}
$$

The second statement is vacuous if (V_D=o(T_D)), but no assumption that both
leaf classes are linear is needed.

This is stronger than the earlier (T_D/6) pigeonhole bound. The correct
endpoint combinatorics is one class versus the union of the other two; using a
single largest class on each shore loses an avoidable factor when one shore
contains two labels.

## 3. Exact internally noncrossing clean shores

The edit-distance partition can be made exactly independent after deleting only
(o(T_D)) tracks. This uses the triangle-free graph hypothesis and is not a
generic assertion about sparse graphs.

Let

$$
\mathfrak m_D:=|X_D||Y_D|-e(X_D,Y_D)=o(T_D^2).
\tag{3.1}
$$

Call (xin X_D) (X)-dirty if its (Y_D)-degree is at most
(|Y_D|/2). Every dirty (x) is incident with at least (|Y_D|/2) missing
cross edges, hence

$$
|X_D^{\rm dirty}|\le\frac{2\mathfrak m_D}{|Y_D|}=o(T_D).
\tag{3.2}
$$

Define (Y_D^{\rm dirty}) symmetrically. Delete all dirty vertices and put

$$
X_D^*=X_D\setminus X_D^{\rm dirty},
\qquad
Y_D^*=Y_D\setminus Y_D^{\rm dirty}.
\tag{3.3}
$$

Then

$$
|X_D^*|,|Y_D^*|=\frac{T_D}{2}-o(T_D),
\tag{3.4}
$$

and both induced graphs (G_D[X_D^*]) and (G_D[Y_D^*]) are empty. To
see this for (X_D^*), if (x,x'\in X_D^*) were adjacent, triangle-freeness
would imply

$$
N_Y(x)\cap N_Y(x')=\varnothing,
$$

so

$$
d_Y(x)+d_Y(x')\le|Y_D|,
$$

contradicting (d_Y(x),d_Y(x')>|Y_D|/2). The proof for (Y_D^*) is the
same.

Thus the cleaned graph is an actual bipartite train-crossing graph with balanced
shores, and the total number of missing cross edges remains (o(T_D^2)). The
phase-star conclusion survives after deleting only (o(T_D)) tracks.

## 4. Exact endpoint theorem

Combining Sections 2--3 gives the following report-level theorem.

> **Mantel phase-star refinement.** Assume the full-core train-floor endpoint
> (1.1). Then, after the canonical (O(D)) phase-circle cut, there are cleaned
> train families
> (mathcal M_D\subset X_D^*) and
> (mathcal U_D\sqcupmathcal V_D\subset Y_D^*) such that
>
> 

$$

> |\mathcal M_D|=\frac{T_D}{2}-o(T_D),
> \qquad
> |\mathcal U_D|+|\mathcal V_D|=\frac{T_D}{2}-o(T_D),
> 
$$


>
> the two shores are internally pairwise noncrossing, and each center-to-leaf
> pair has (o(T_D^2)) missing actual crossings relative to its complete
> product. The center has one phase label and the two leaf classes have the
> other two labels, up to (o(T_D)) discarded tracks.

The exact size scale is

$$
|\mathcal M_D|,\ |\mathcal U_D|+|\mathcal V_D|
 =\sqrt{\Delta_2}\,D-o(D),
\tag{4.1}
$$

and the two shore sizes sum to

$$
2\sqrt{\Delta_2}\,D-o(D).
\tag{4.2}
$$

This theorem concerns the actual train curves and occurrence-counted rhombus
crossings after deletion of (O(D)) crossing relations. It does not replace the
full source by the train graph and does not delete contact-isolated source points.

## 5. Exact frontier effect and remaining implication

The refinement upgrades the current floor endpoint from a merely dense
distinct-label pair to a cleaned, balanced, internally noncrossing
one-versus-two phase star. In the two-leaf case, both center-to-leaf crossing
graphs are individually near-complete, not merely jointly dense.

The resulting exact remaining implication is

$$
\boxed{
\begin{aligned}
&\text{balanced internally noncrossing actual train shores,}\
&\text{one center label versus two leaf labels,}\
&\text{each center-to-leaf pair missing }o(T_D^2)
\end{aligned}
\Longrightarrow
\text{a source-level diameter penalty or an exact unit triangle.}}
\tag{5.1}
$$

The abstract graph conclusion is not enough. The graph-level random bipartite
regression remains relevant: subquadratic missing crossings can have no linear
complete biclique. The new geometric hypotheses are the actual train embedding,
one-crossing pseudosegments, phase directions, and (O(D)) boundary/interface
occurrences. No theorem converting them into a complete star in the canonical
holed/interface complex has been proved here.

The simply connected proper-train disk conditional report can use (2.12) in its
dual-tree extraction. It does not follow that the canonical complex is a disk;
holes and interfaces remain the live obstruction.

## 6. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| Mantel edit partition | report-level proved | elementary triangle-free Mantel stability | Degree-square variance argument |
| One-versus-two phase-class sizes | report-level proved | Lemma 2.1 and endpoint density | (M(T-M)) reaches (T^2/4) only at (M=T/2) |
| Each center-to-leaf pair is near-complete | report-level proved | phase concentration, internal-edge (o(T^2)) bound | Nonnegative pairwise missing counts sum to (o(T^2)) |
| Dirty-track count is (o(T)) | report-level proved | cross missing count (o(T^2)) | Each dirty track contributes at least (T/4-o(T)) misses |
| Clean shores are exactly internally noncrossing | report-level proved | triangle-freeness | Two (> |Y|/2)-degree adjacent vertices would form a triangle |
| Complete geometric star in a holed complex | unresolved | missing completion theorem | Endpoint/interface boundaries can absorb order information |
| Level I | open | original quantifiers | Type-I branch, higher-surplus branch, and holed endpoint remain |

## 7. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
| --- | --- | --- |
| Abstract random near-complete bipartite graph | pass | It has no train embedding and is not used as a counterexample to the theorem |
| Five-sector (C_5)-blowup | pass | Its train density is (1/5), not the (1/4) endpoint |
| Same-label crossing attempt | pass | Same-label pairs are forbidden by the strict (>\pi/3) angle gap |
| Internal-edge removal by density alone | not used | Exact cleaning uses triangle-free common-neighborhood disjointness |
| Contact-isolated source points | pass | They remain in the source and never enter the affine-kernel claim |
| Holes, bridges, and repeated boundary occurrences | pass | No boundary simplification is made; these are precisely the remaining geometric obstruction |
| Global optimality | pass | The statement is a necessary endpoint structure for canonical global-minimizer representatives, not a competitor theorem |

## 8. Literature and computation

No external theorem is imported into the proof and no computation is required.
The web scope check confirmed that general (x)-monotone or pseudosegment density
theorems do not automatically give a near-full complete star; this report relies
only on the elementary finite graph arguments displayed above.

## 9. Corrections / supersessions

This report corrects only the strength of the phase-star handoff. The earlier
(T_D/6) distinct-label pair bound remains true but is nonsharp at the
one-versus-two endpoint. No canonical theorem is superseded, and no theorem-state
entry is changed.

## 10. Promotion recommendation

**unreviewed** — preserve as a report-level proved endpoint refinement. It is not
canonical and does not close C-II or Level I.

## 11. Handoff

1. Strongest new theorem: the Mantel-floor train graph has a cleaned balanced
   near-complete one-versus-two phase star, with both shores exactly internally
   noncrossing after deleting (o(T_D)) trains.
2. Canonical dependency chain: `C-FULLCORE-TRAIN-SURPLUS-FLOOR` → Sections 85 and
   90 / canonical train theorem → report-level Mantel stability.
3. Exact remaining lemma: complete-star or direct diagonal completion for this
   actual holed/interface train complex, retaining all holes, bridges, repeated
   boundary occurrences, and source isolates.
4. Binding dead route: ordinary graph stability or density alone cannot provide
   the required complete geometric star.
5. Files to read next: `target_c_fullcore_mantel_endpoint_stability_2026-09-14.md`,
   `target_c_pure_disk_mantel_floor_closure_2026-09-14.md`, and
   `target_c/76-hole-stable-complete-grid-order-diameter-audit.md`.

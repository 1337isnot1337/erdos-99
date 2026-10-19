> Generated reading edition · [exact source](../../../docs/audits/target_c_pr952_component_anchor_stress_gain_destination_audit_2026-10-19.md) · source SHA-256 `863f6ec863db8285e3813118a7fc06f62d41d6b0dbf0aeee47d237a66d3ef390`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-718A099744A6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: destination audit of PR #952 component anchoring and stress gain

Date: 2026-10-19. Refined scope key: `e419c7fa59fd31af62050ae0`. Audit base: `7d0a450fe66991036541023f95c44c064a04b6a8`; theorem state `2026-10-15.publication.2`; priority `public-frontier.3`; catalogue `public-frontier.9`.

## Verdict and lifecycle

**Conditional proof audit: pass under the report's complete hypotheses.** I reconstructed the cut-resultant identity, the acute-owner stress identity, and the mixed-component upper-safety argument. I found no algebraic defect in those implications. Their use still requires the supplied owner family, its fixed isolate dispatch and bounded-face assignments, every stated singleton/unary check, and a nonzero selection passing the remaining strict lower clauses.

This is the missing destination review of `TARGET-C-PR952-COMPONENT-ANCHOR-STRESS-GAIN`, not a theorem promotion. The candidate remains `unreviewed` in the destination registry and artifact index; no manifest, theorem state, priority allocation, or Level I/C-II status is changed. Level I, Target A, Target B and C-II remain open; C-I remains closed.

## Exact source and scope

Destination main and this audit's source head are `7d0a450fe66991036541023f95c44c064a04b6a8`. The destination candidate is [the Slot 01 report](../reports/target_c_owner_component_anchoring_and_source_realized_sink_2026-10-10.md), blob `54a97e49d1d303641ab20f771a69239f45998afc`, SHA-256 `a8e3e9a42129eef055bbc6b494322fefaa749b2f373ea76631fe5d3fb7620eff`. Its source PR #952 head is `3536c0b6f6c2a929d9c96fffbdcfc480735fea3`; a live raw-content hash check matched the destination report, verifier, and saved JSONL fixture byte-for-byte. The verifier SHA-256 is `df2cd04d208b0370cb85b3c15a2cef308b11be2a942058c724473456ad85da25`; the saved fixture SHA-256 is `c14bcafb77c02e6ac64d0cbd76d1ed095ee041f186344273307b4b72848f3198`.

The source PR #952 is open and has no submitted GitHub reviews at audit time. Destination PR #25 is the merged migration/reconciliation record; it explicitly retains these five mathematical candidates as unreviewed. Neither that import nor the source's historical status supplies this exact destination audit. No exact-scope audit was present in the live Discussion #83 handoffs, predecessor handoffs, or open destination PR search.

The audited statements are conditional finite-source claims for the canonical contact-minimal, then actual-diameter-pair-minimal C-II source. They do not produce a moving owner family. The mixed refinement conclusion is used only after its report-specific hypotheses are supplied.

The cited [`C-OO-TERMINAL-OWNER-CAPACITY`](target_c_owner_order_and_terminal_capacity_promotion_audit_2026-10-06.md), [`C-OO-OVERLAP-AWARE-ROOT-RUN-CAPACITY`](target_c_overlap_aware_owner_capacity_independent_audit_2026-10-08.md), and Audit.184/185 sink bounds constrain counts or witnesses; they supply neither an extracted stable owner family nor a source move or full-source upper feasibility. I treat them as context and obstruction bounds, not as discharged extraction hypotheses.

## Reconstruction of component anchoring (CA)

Let $`C`$ be the connected contact graph on the nonisolated core $`V`$, $`H_+`$ the positive-multiplier diameter support on that core, and $`H_{all}`$ the full actual diameter graph. At each core vertex use the stated equilibrium

```math
\sum_{j:ij\in C}\alpha_{ij}(p_i-p_j)
=\sum_{j:ij\in H_+}\beta_{ij}(p_i-p_j),
\qquad \alpha_{ij}>0,\quad \beta_{ij}\ge0.
```

For a nonempty proper $`G ⊂ V`$ translated by nonzero $`d`$, take a component $`W`$ of the induced contact graph on $`G`$. Connectivity of $`C`$ gives a crossing contact. Every crossing contact of $`W`$ leaves $`G`$, since $`W`$ is a component of $`C[G]`$. If its oriented vector is $`r=p_i-p_j`$, exact contact preservation gives

```math
|r+d|^2=|r|^2=1,
\qquad r\cdot d=-|d|^2/2.
```

Summing equilibrium over $`W`$ cancels internal rows. Dotting with $`d`$ yields

```math
\sum_{ij\in\delta_{H_+}(W)}\beta_{ij}(p_i-p_j)\cdot d
=-\frac{|d|^2}{2}\sum_{ij\in\delta_C(W)}\alpha_{ij}<0.
```

Thus a crossing $`H_+`$-row has positive multiplier. For a contact component $`W ⊂ V\setminus G`$, move $`W`$ alone by $`-d`$; its only crossing contacts go to $`G`$, and their vectors change exactly as under the original $`G`$-move. The same sum proves a positive-multiplier diameter port for $`W`$. This does not claim upper feasibility or control a component consisting only of contact isolates.

The acute split corollary also checks: if distinct owners $`G_i,G_j`$ share an old contact, the four binary placements make all four squared lengths one. Their mixed second difference is $`2d_i·d_j ≠ 0`$, a contradiction. Therefore no contact joins two moving owners, and splitting a parent into contact components keeps each old contact together. This argument needs preservation in all four binary states and strict positive dot product.

## Reconstruction of strict stress gain (SG)

Use the canonical core stress $`\Omega=L_C(\alpha)-L_{H_+}(\beta)\succeq0`$, with $`\ker\Omega=\operatorname{span}\{\mathbf1,P_x,P_y\}`$, $`\sum_{H_+}\beta_h=1`$, and $`\sum_C\alpha_e=D^2`$. This is the restored relative-interior KKT stress and the core-only [`C-ZRF`](../targets/target-c/57-zr-zf-rigidity-audit.md) normalization. C-ZRF places every supported diameter endpoint in $`V`$; the count $`h_+\ge\lceil D\rceil\ge9`$ uses canonical [`C-WOODALL`](../reports/target_c_woodall_diameter_topology_2026-09-10.md) with ZRF. The candidate also lists the full-source force-hull input and [`C-FS-GEOM`](../targets/target-c/58-full-source-geometry-audit.md) for loaded-endpoint location. [`C-MIXED-CORE-FINITE-RIGIDITY`](target_c_finite_mixed_core_rigidity_independent_audit_2026-10-07.md) supplies compatible finite-equality context, but is not needed in the strict-gain calculation. Contact isolates remain outside the stress matrix.

For disjoint owners, the mixed contact argument makes the contact part of $`\mathbf1_{G_i}^T\Omega\mathbf1_{G_j}`$ vanish. The diameter Laplacian contributes

```math
\mathbf1_{G_i}^T\Omega\mathbf1_{G_j}
=\sum_{h\in H_+[G_i,G_j]}\beta_h=:b_{ij}\ge0.
```

For $`\kappa_i=\mathbf1_{G_i}^T\Omega\mathbf1_{G_i}`$, PSD gives $`\kappa_i\ge0`$. If it were zero, PSD would put $`\mathbf1_{G_i}`$ in the affine kernel. A nonconstant affine function taking only values 0 and 1 on $`V`$ puts all core points on two parallel lines, whose convex hull has at most four vertices. Every $`H_+`$ endpoint is an extreme point of the full source and lies in $`V`$ by C-ZRF, so at most six supported diameter pairs could then exist. This contradicts $`h_+\ge\lceil D\rceil\ge9`$. Hence every $`\kappa_i>0`$.

For binary selection $`x`$, put $`U=Q-P=\sum_i x_i\mathbf1_{G_i}d_i`$. Since $`\Omega P=0`$, and every old contact remains unit,

```math
\begin{aligned}
\sum_{h\in H_+}\beta_h(D^2-|Q_h|^2)
&=\operatorname{tr}(Q^T\Omega Q)
=\operatorname{tr}(U^T\Omega U)\\
&=\sum_i x_i\kappa_i|d_i|^2
+2\sum_{i<j}x_ix_jb_{ij}(d_i\cdot d_j).
\end{aligned}
```

Every mixed term is nonnegative, and a selected diagonal term is positive. Thus every nonzero selection has positive weighted old-diameter deficit; because the nonnegative weights sum to one, some supported actual diameter shortens by at least the displayed total deficit. Other old diameters may lengthen: this identity alone is not an upper-feasibility result.

This agrees with canonical [`C-FINITE-CONTACT-ISOMETRY-DIAMETER-GAIN`](target_c_contact_isometry_energy_independent_audit_2026-10-08.md): both use the same normalized core stress and exact contact preservation. SG adds strict positivity for this special owner family by proving its diagonal terms are nonzero. Neither result handles the full-source lower/upper ledger. [`C-DISJOINT-SWAP-2SAT`](../reports/target_c_simultaneous_disjoint_swaps_exact_2sat_2026-10-01.md) supplies only the downstream minimality consequence after every inactive lower and upper pair has the required strict status.

For the later *full* diameter ledger, weak active rows must not be silently dropped just because their KKT coefficient is zero. In the stress formulas, $`H_+`$ denotes only positive-multiplier rows; the mixed graph below uses $`H_{all}`$. In the canonical lexicographic source, no contact-isolated point $`z`$ can be an endpoint of an actual diameter pair. A diameter endpoint is extreme: if $`z`$ were a nontrivial convex combination of other source labels, the variance identity would make its squared distance to every partner strictly less than $`D^2`$. Thus choose a linear functional strictly exposing $`z`$ and move it a sufficiently small distance inward. Every distance from $`z`$ strictly decreases to first order; because $`z`$ has no contacts and the source is finite, choose the move small enough that every formerly inactive lower pair stays strictly above one. If another diameter pair remains, the same contact graph has fewer actual diameter pairs; if none remains, the diameter is strictly below $`D`$. Both contradict the canonical choice. Thus all actual diameter endpoints, including endpoints of zero-multiplier rows, lie in $`V`$. The stress sum uses only supported rows; the mixed graph and upper ledger still include every actual diameter row.

## Reconstruction and adversarial checks of mixed refinement (RM)

The report's RM statement is sound with its supplied, subfamily-stable O–O parent system, pairwise acute translations, exact contact preservation in all binary states, cloud bound

```math
s=\operatorname{diam}\{0,d_1,\ldots,d_r\}<\min\{D-\sqrt{D^2-1},\sqrt2-1\},
```

parent singleton weak shortening of every actual diameter, fixed long-pair/isolate-anchor dispatch with $`|E|\le d_H`$, compatible bounded-face transport, and every parent unary strict-rhombus test.

The dependency scopes fit this argument: [`C-ZRF`](../targets/target-c/57-zr-zf-rigidity-audit.md) supplies the core stress/rigidity normalization; [`C-LONG-PAIR-ISOLATE-DISPATCH`](../reports/target_c_forest_isolate_dispatch_2026-10-01.md) provides one source-fixed anchor/exception partition, uniform across moves; [`C-OO-LOWER-BLOCKER-LOCALIZATION`](../reports/target_c_near_unit_faces_and_pure_conflict_paths_2026-10-01.md) supplies the small-cloud bounded-face transport and reduces remaining lower blockers; [`C-NEAR-UNIT-CONFLICT-GEOMETRY`](../reports/target_c_near_unit_faces_and_pure_conflict_paths_2026-10-01.md) supplies the cofaciality used for near-unit pairs. These are conditional on the supplied actual O–O system and cloud bound. They do not imply owner-family extraction, and acuteness alone does not substitute for the fixed isolate map or bounded-face compatibility.

* **Deletion and source labels.** Mark the parent owner of each core endpoint of a pair in $`E`$, and the owner of each anchor of an isolate endpoint. At most $`2|E|\le2d_H`$ parents are removed. An unanchored isolate is fixed. This removes proposals only; it does not delete labels. Bounded-face isolates cannot be endpoints of a pair longer than $`L=\sqrt{D^2-1}`$, by the variance bound.
* **Contacts.** No contact crosses distinct moving parents by the mixed-difference argument. A parent-internal contact is an edge of its induced $`C\cup H_{all}`$ graph and stays inside one refined component. Parent-to-fixed contacts have their original singleton state. The supplied O–O face transport keeps each moved bounded face in one translation; its assigned isolates follow that translation. Hence all old contacts remain exactly unit.
* **Actual diameter pairs.** If an old $`H_{all}`$-edge is internal to one parent, inclusion in the mixed graph keeps its endpoints in one refined component, so its length is unchanged. If exactly one parent moves, its parent singleton test gives change $`g_i=2r\cdot d_i+|d_i|^2\le0`$. If distinct parents move its endpoints, the simultaneous change is $`g_{ij}=g_i+g_j-2d_i\cdot d_j<0`$. Thus all old actual diameter pairs weakly shorten, regardless of which contact components were split.
* **Inactive upper pairs.** For a nonexceptional inactive pair longer than $`L`$, the fixed dispatch gives equal endpoint displacements (common anchor, or both unanchored), so its length is unchanged. Every other nonexceptional inactive pair starts at most $`L`$ and its relative displacement is at most $`s`$; hence its final length is at most $`L+s<D`$. The marked $`E`$-pairs have both endpoint displacements fixed after owner deletion, so they remain below $`D`$. This uses the report's full anchor/exception assignment; pairwise acuteness alone would not prove it.
* **Unary and lower ledger.** Each active strict rhombus remains in its single supplied owner state because its moving contact edge is retained by the mixed-component refinement; its stipulated unary test handles its diagonals. Bounded nonquadrilateral faces are transported rigidly with their assigned isolates. Near-unit cofaciality leaves only the outer-face near-unit pairs as remaining lower clauses. A contradiction follows only if a nonzero state passes those clauses **strictly**, so no new unit contact appears. SG then supplies strict loss of an old diameter, while the full upper proof prevents any new diameter pair; global minimality or secondary diameter-pair minimality is contradicted.

These checks preserve the separation between conditional lemma and source-wide theorem. The report does not prove that a canonical survivor supplies more than $`2d_H`$ usable parent owners, a nonzero strictly lower-admissible refined state, or the analogous macroscopic-container endpoint. The separate near-unit/outer-face lower formula remains a real feasibility obligation.

## Finite regression controls

The source report's SR construction is intentionally a regression to the implication “connected geometric O–O realization plus unary and upper safety implies a nonzero lower-feasible Horn state.” Its positive-contact KKT hypothesis fails: each gadget moving contact component has a nonzero cut-contact resultant and no incident diameter row, so strictly positive weights on all its contacts cannot satisfy equilibrium. The family is also explicitly nonglobal, and the verifier constructs a smaller square-lattice packing. It is not a counterexample to CA, SG, or a canonical endpoint theorem.

At the eleven zero-limit noncontacts, the leading lower-slack coefficients in state order $`00,10,01,11`$ give $`Am0/Bm0:(20,-4,28,4)`$, $`Cm0/Dm0:(4,28,-4,20)`$, and each of the three $`Emj/Fmj:(56,8,136,-8)`$. Thus A-only, B-only, and both-owner states each fail strict lower feasibility at their stated physical witnesses; the zero state has positive slack. The remaining six zero-limit pairs have positive leading coefficients in all four states. The exact verifier also requires all other noncontacts to remain strictly above one.

For the all-large family argument, the limit cluster has only finitely many pairs: the 5,751 strictly positive limiting slacks persist on one common interval, and each of the eleven rational critical slacks has its displayed nonzero leading sign for all sufficiently small positive $`t`$. The high chain lies on $`x=0`$ at integer heights starting at 22; its lower checks against the cluster reduce to levels 22 and 23. The upper bounds use the cluster box $`[-6,6]\times[0,23]`$: cluster pairs have squared distance at most 673; points of height at least one are within squared distance $`(H-1)^2+36<D^2`$ of the chain; points below height one have $`|x|\le5`$ and are at most $`D^2=H^2+25`$ from the top, with equality only at the two stated diameter pairs. The remaining family step is the report's stable connector-count interval; the finite runs at $`H=30,31,100`$ are controls, not a substitute for the small-$`t`$ argument.

## Verification and limits

The source verifier replay and required corpus checks are recorded in the PR body. No full theorem-certificate replay is claimed; that is deferred to the merging agent. No external literature is imported. Original candidate credit remains with Slot 01 and source PR #952. Review authored by OpenAI Codex, GPT-6 Luna xhigh, as an independent AI agent; the report is an Apache-2.0-compatible original audit. No human mathematical review is claimed.

## Remaining exact lemma

Extract, in every sufficiently large canonical full-core C-II survivor, a subfamily-stable disjoint O–O parent family with the stated acute translations, small cloud, fixed isolate/exception dispatch, bounded-face transport, singleton actual-diameter safety and unary tests, retaining more than $`2d_H`$ owners; then prove its refined outer-face lower system has a nonzero strictly admissible state. Either outcome changes the full-source lower/upper endpoint ledger. If extraction fails, identify a source-compatible replacement that retains every contact isolate and still gives a strict lexicographic endpoint.

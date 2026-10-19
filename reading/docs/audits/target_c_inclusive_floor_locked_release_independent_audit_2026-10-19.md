> Generated reading edition · [exact source](../../../docs/audits/target_c_inclusive_floor_locked_release_independent_audit_2026-10-19.md) · source SHA-256 `36fee0256d57b6e14a75b62d6515b14a198c3cd5d81a53045f16bf362ce3b1f9`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-1535587A6849","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Independent audit: inclusive floor closure and locked contact release

**Date:** 2026-10-19  
**Verdict:** **CONDITIONAL** — the supplied-family source conclusions follow under the stated geometric hypotheses and canonical dependencies. The abstract IFC theorem should explicitly require nonnegative upper-bound costs; without that condition its construction is false. In the report's geometric use, the bound is (U_i=2D>0), so this wording defect does not affect the claimed finite endpoint results.  
**Audit base:** destination `main` at `7d0a450fe66991036541023f95c44c064a04b6a8`, tree `db766e0e25b562054df26aeec7e627d5a579dd6d`. State `2026-10-15.publication.2`; priority `public-frontier.3`; catalogue `public-frontier.9`.  
**Reviewed candidate:** `TARGET-C-PR952-INCLUSIVE-FLOOR-LOCKED-RELEASE`, destination status `unreviewed`; no lifecycle or theorem-state change is requested.

## Scope and exact inputs

This is the destination-side audit of the imported candidate, not an audit of the historical source PR itself. The source PR is #952 in `1337isnot1337/e-99` at `3536c0b6f6c2a929d9c96fffbdcfc480735fea3`; it is not PR #952 in the destination repository. Its report, verifier, and finite output are byte-identical at destination `main` to the assigned SHA-256 pins:

| Destination path | SHA-256 |
| --- | --- |
| [`target_c_inclusive_floor_closure_and_locked_contact_release_2026-10-10.md`](../reports/target_c_inclusive_floor_closure_and_locked_contact_release_2026-10-10.md) | `25dcc76277cc3382b7334d2c2d748850dcd04a3ddbdc694d4f6729c6fd2ca218` |
| [`verify_target_c_inclusive_floor_release_2026_10_10.py`](../../../research/verify_target_c_inclusive_floor_release_2026_10_10.py) | `9cfd38a998de0b6fc420674943b98c05ef0a371fa21ee9f9352b4ea02c3608fc` |
| [`target_c_inclusive_floor_release_2026_10_10.jsonl`](../../../research/certificates/target_c_inclusive_floor_release_2026_10_10.jsonl) | `6a18eeaf4616c86e15dd6811103481637cc7a470f9fdc83cfda66fae391e0c18` |

I reconstructed the arguments before reading earlier audit conclusions. I then checked the current manifest/catalogue lifecycle, the supplied dependency statements, the candidate registry and live destination coordination. The private refreshed overlap cache at 2026-10-19 09:33 UTC had complete pagination for 47 open PRs, 97 closed PRs, 8 Discussions (including comments/replies), and 0 Issues; no record matched the candidate ID, report path, verifier path, or this investigation ID. The candidate remains `unreviewed`; the live destination contains no audit of this exact candidate or scope. The source report's historical label and source PR number do not constitute destination review.

## Exact question and decision boundary

**Candidate lemma.** Given a supplied full-source partition into a fixed group and disjoint translating groups in one direction, with every source label assigned, actual lower/upper pair constraints, no old contact between moving groups, and the report's floor rules, lexicographic shortest paths plus finite zero closure construct the unique inclusion-largest feasible active support. Under weak upper constraints, this construction detects every contact-loss endpoint in the stated class. Under canonical C-II KKT hypotheses and strict inactive core-core upper constraints, a surviving proper core group yields a finite full-source competitor contradicting the canonical contact/diameter-pair lexicographic choice, including when its height equals a positive contact floor.

**Canonical quantity affected.** A contact-opening endpoint lowers the unit-contact count at diameter (D). If contacts stay fixed, the locked-contact branch lowers the actual diameter-pair count at (D), or gives a same-cardinality strict-sub-(D) competitor. Every source pair, including pairs incident to contact isolates and previously inactive upper pairs, must remain feasible.

**Falsification and stop condition.** The finite falsifiers are a feasible support outside the computed maximal support; a failed simultaneous endpoint; a weak equal-positive-floor path incorrectly eliminated; a strict inactive upper cap incorrectly retained; or any omitted/newly active source pair in a geometric fixture. I ran the pinned finite verifier and checked its exact inequalities. I stop at the supplied-family theorem: no family extraction or universal survival claim is proved here. The decisive remaining question is whether every sufficiently large canonical triangle-free C-II minimizer supplies such an owner family with a surviving core group, or a weak-policy contact loss.

## Independent reconstruction

### Full-source encoding

Let (s_0=0) for the fixed labels and translate each moving group (G_i) by (s_i v). Every label is assigned to exactly one group, including each contact isolate. Pairs within one group are unchanged. For an intergroup pair write its axial/transverse coordinates as ((a,z)) and put (u=(D^2-z^2)^{1/2}). Its two diameter constraints are exactly

```math
s_i-s_j\le u-a,\qquad s_j-s_i\le u+a.
```

Both costs are nonnegative because the original pair length is at most (D); both are positive for a pair that was strictly below (D). Policy B marks the two constraints strict for every previously inactive core-core pair. It leaves actual diameter constraints weak and isolate-involving upper constraints weak. Thus every pair that can change receives both upper tests. For an old noncontact with (|z|\le1), preserving its original projected side gives one strict lower difference bound with positive cost (|a|-(1-z^2)^{1/2}); if (|z|>1), the transverse coordinate alone keeps the pair strictly above one. Old contacts to the fixed group give (1+s_i(s_i-\tau)), where (\tau=-2(p-q)\cdot v); hence a positive group height must be at least (F_i=\max(0,\max\tau)). A zero-floor active height must still be positive.

This encoding checks contacts, all noncontacts, all actual diameter pairs and all inactive upper pairs. Contacts within a moving group and fixed labels are unchanged. No isolate is deleted or identified with a core point during the endpoint construction.

### Inclusive floor closure (IFC)

On the directed difference graph, use edge cost \hat c=(c,-k), where (k=1) marks a strict inequality. With (c\ge0) on every edge and (c>0) for every strict edge, all edge costs are lexicographically nonnegative. A shortest path from (i) to the already forced-zero set (Z) has cost ((a_i,-m_i)). Summing its inequalities gives (s_i\le a_i), strictly if (m_i>0). Therefore a vertex is forced to zero when (a_i<F_i), when (a_i=F_i>0) and (m_i>0), or when (a_i=F_i=0). Repeating this at most (r) times proves every feasible active support is contained in the final complement (I).

For sufficiency, shortest-path optimality gives (w_e=c_e-a_i+a_j\ge0) and, when (w_e=0), (m_i\ge m_j+k_e). Choose 
```math
\eta=\min\bigl(1,\{w_e:w_e>0\},\{c_e:k_e=1\},\{a_i-F_i:i\in I,\ a_i>F_i\}\bigr)>0,
\qquad \epsilon=\eta/(2(r+1)),
```
omitting empty sets, and set (s_i=a_i-m_i\epsilon). If (w_e=0), the strict-count inequality preserves that edge, including strictness when (k_e=1). If (w_e>0), the loss from the strict-count term is at most ((r+1)\epsilon=\eta/2<w_e). Thus every edge inequality holds. The choice of ε keeps every strict edge strict and every surviving height above a positive floor; an equal positive floor survives only with (m_i=0), so it is attained exactly. A zero floor is never retained at zero height. The constructed endpoint therefore has support exactly (I), proving that (I) is the unique largest feasible support, not merely a maximal support found by a heuristic.

This proof needs nonnegative costs for the bound edges as well as the pair edges. The generic theorem says bounds are finite but does not explicitly say (U_i\ge0). Counterexample: one variable, (F_1=0), and only the weak bound (s_1\le U_1=-1). The feasible class is empty, while the stated zero construction violates its own bound. Add (U_i\ge0) to the abstract statement. In the geometric application (U_i=2D) is available from a fixed reference label, so the application satisfies the condition.

### Contact loss (CLR)

Under weak upper policy A, the construction is feasible and only old contacts can remain or open. If an arbitrary feasible endpoint opens a cut contact at (s_i>F_i), its path cap satisfies (a_i\ge s_i>F_i), so the constructed height also exceeds the floor. If the opening occurs at (s_i=F_i>0), the opened cut has (\tau<F_i), and the constructed height is at least (F_i). If (F_i=0), every active height is positive and likewise opens any cut with (\tau\le0). Thus the closure detects every contact loss in the stated class. The full-source lower tests forbid new contacts. At diameter (D), the endpoint remains triangle-free and has fewer contacts; below (D), global optimality is contradicted. Signed motions reduce to the same class by choosing the direction of a contact-loss witness and clipping negative group heights to zero; positive-part clipping preserves all weak/strict difference inequalities, and clipped groups return their contacts to their original lengths.

### Locked contact release (LCR)

Under policy B, suppose a core group survives and no contact opens. Then all old contacts remain exactly unit: a cut contact stays unit only at its floor equality. The full contact graph is unchanged and the strict lower bounds forbid new contacts. For disjoint core indicators (g_i), the canonical core stress satisfies (\Omega\succeq0), (\Omega P=0), and (\ker\Omega=\operatorname{span}\{1,P_x,P_y\}). There is no cross-contact between moving groups, so
```math
\kappa_i=g_i^T\Omega g_i>0,
\qquad b_{ij}=g_i^T\Omega g_j\ge0.
```
Indeed, zero κ would put the nonconstant 0/1 indicator in the affine kernel. Its two level sets would put the core on two parallel lines and leave at most four core-hull vertices. But C-ZRF and Woodall give (q\ge h\ge\lceil D\rceil\ge9) distinct loaded diameter endpoints; these are core-hull vertices. Thus zero κ is impossible. The cross terms (b_{ij}) are sums of positive diameter weights because the contact cross terms vanish.

With (U=\sum_i s_i g_i v^T), exact contact preservation and the normalized KKT identity give
```math
\sum_{h\in H}\beta_h(D^2-|Q_h|^2)
=\operatorname{tr}(U^T\Omega U)
=\sum_i\kappa_i s_i^2+2\sum_{i<j}b_{ij}s_is_j>0.
```
All old diameter pairs obey their weak upper bounds, so at least one old core diameter pair strictly shortens. The strict inactive core-core upper constraints prevent any previously inactive core pair from becoming a diameter pair; within-group pairs are unchanged. The canonical isolate normalization then moves every isolate toward the core centroid, preserves all lower constraints and the contact graph, and makes every isolate-involving pair strictly shorter than (D). Hence no new full-source diameter pair can replace the shortened old one. The resulting same-cardinality endpoint has diameter below (D), or diameter (D) and fewer actual diameter pairs. Both alternatives contradict the selected canonical source.

This uses only the stated canonical core stress/loaded-hull facts and the exact full-source isolate-normalization theorem. It does not assume a stress or affine relation on isolates. The dependency chain checked is `C-ZRF`, `C-WOODALL`, `C-LOADED-HULL`, `C-FINITE-CONTACT-ISOMETRY-DIAMETER-GAIN` (transitively `C-MIXED-CORE-FINITE-RIGIDITY`), and `C-FULL-SOURCE-ISOLATE-NORMALIZATION`. The `C-FINITE...GAIN` report's contact-preserving stress identity applies here; its stronger noncongruent/no-lengthening conclusion cannot be invoked merely from the contact graph, since the mixed-rigidity theorem requires equality on every old diameter edge. The argument above independently establishes strict stress energy from the nonconstant core indicator and nonnegative old-diameter slacks. No dependence on that stronger conclusion is needed. The energy identity is derived explicitly rather than inferred from a finite calculation.

### Collapse certificate and the unproved bridge

If every core group is eliminated, its shortest path reaches an earlier forced-zero group with cost below its contact floor, or equal to a positive floor with at least one strict edge, or zero at a zero floor. A weak path of cost equal to a positive floor leaves the group at that floor and cannot force it to zero. This is exactly the distinction the report preserves. Lower-edge witnesses have original length at most (1+c); upper-edge witnesses have length at least (D-c). These are owner-variable paths, not physical source paths or train returns. Nothing here extracts a suitable owner family or shows its closure survives for every canonical minimizer.

## Finite controls and adversarial checks

I reran the exact pinned command:

```text
flock -x /home/cinna/.local/state/erdos99-host-compute.lock \
  /home/cinna/.local/state/erdos99-pass/paired-20261019T091333Z/venv/bin/python \
  research/verify_target_c_inclusive_floor_release_2026_10_10.py \
  --graphs 80 --seed 1001001 --diameters 20 30 50
```

It exited successfully. The independent exact Fourier–Motzkin enumerator checked all 620 supports from 80 rational graphs (one to four variables); the separate shortest-path implementation's union support was feasible in each graph. The critical controls include an all-weak path that retains a positive equal-floor variable, a strict edge on the equal-cost path that eliminates it, and a two-round zero cascade. Six nonglobal triangle-free geometric fixtures checked all 15 label pairs at both endpoints for each of (D=20,30,50), totaling 180 pair-state checks. The exact weak-lock fixtures remove one diameter while retaining another; the strict-inactive fixtures replace the shortened old diameter with a formerly inactive pair, correctly defeating policy A and triggering policy B. The rerun's stdout was byte-identical to the pinned JSONL certificate (SHA-256 `6a18eeaf4616c86e15dd6811103481637cc7a470f9fdc83cfda66fae391e0c18`). The verifier uses exact identities and directed rational enclosures for the algebraic coordinates. These runs verify finite implementation and regressions only; they do not certify the analytic theorem by enumeration.

The verifier and its imported enclosure helper were inspected. The helper uses exact rational intervals with monotone square-root bounds for the expressions used here. The checked fixtures remain nonglobal (the report itself exhibits small-diameter competitors), so they test endpoint bookkeeping and the strict/weak distinction, not canonical minimizer extraction or KKT validity.

## Disposition and remaining lemma

The conditional analytic results pass for the supplied-family geometric class, after making (U_i\ge0) explicit in generic IFC. The weak equal-floor and strict-inactive controls support the separate endpoint policies. No source-wide owner extraction, support survival, asymptotic onset, or universal statement about every global minimizer follows. Keep C-II, A, B and Level I open, with C-I closed.

**Next lemma:** prove that every sufficiently large canonical triangle-free C-II source admits a direction and a partition of every source label into disjoint moving groups plus a fixed group with a nonempty proper core moving part, no inter-group old contact, and at least one fixed core label, such that policy B's inclusive closure retains a core group; alternatively, make policy A's constructed endpoint open an old contact. The exact downstream quantities are the contact count or actual diameter-pair count at (D), after checking every lower and actual/inactive upper pair. A source-specific collapse of every such owner family would falsify this route and force a different endpoint mechanism.

**Attribution and AI disclosure:** The audited candidate report and finite verifier are retained byte-for-byte from the frozen source PR #952 in `1337isnot1337/e-99`; this audit preserves that provenance and does not claim their authorship. This independent audit was produced by OpenAI Codex, GPT-6 Luna xhigh, in the assigned reviewer role. No external paper text or third-party code is imported here. The contribution is offered under Apache-2.0 as permitted by the repository contribution policy.

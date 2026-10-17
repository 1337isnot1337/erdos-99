> Generated reading edition · [exact source](../../../docs/audits/target_c_monotone_route_debit_independent_audit_2026-10-08.md) · source SHA-256 `f72859b832fdc9826bfda30d4c4262ababddc51c380711667d6024ef686e1e5e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C93C5BF5C633","canonical":true,"claim_ids":["C-ATTACHMENT-TRIANGLE-DEBIT-REGRESSION","C-MONOTONE-POSITIVE-CONTACT-ROUTE-DEBIT","C-RHOMBIC-PATH-ROUTE-EXCESS-SHARP-REGRESSION"],"claim_statuses":{"C-ATTACHMENT-TRIANGLE-DEBIT-REGRESSION":"regression","C-MONOTONE-POSITIVE-CONTACT-ROUTE-DEBIT":"canonical","C-RHOMBIC-PATH-ROUTE-EXCESS-SHARP-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Independent audit: monotone contact routes and their exact defect currency

Date: 2026-10-08. Audit base: `origin/main=9d98bdecd288cfdb486a0189d28d9928d0bdae22`, state `2026-10-08.audit.123`. Target C C-II remains open.

Frozen source: PR #662 branch `research/c2-deep-port-grid-audit-20261004` at `e275fc53d92d543c78421e76dacc245832d79b86`. Source report `docs/reports/target_c_monotone_cap_routes_and_global_payment_2026-10-04.md`, SHA-256 `b70ddf1f7b6cb3b3cf7a0eb23f6acc555ff0e80b9aeb69c35030b53b68bb3147`. Exact source verifier `research/verify_target_c_monotone_cap_routes_2026_10_04.py`, SHA-256 `ff6c3beba4fd18ebb811b14b82be0cefa1e6deaab91ae174a75aac4318738a3b`.

## Verdicts

- **PASS — promote `C-MONOTONE-POSITIVE-CONTACT-ROUTE-DEBIT`.** The strict-successor forest and global route-excess bank follow from positive equilibrium, canonical mixed rigidity, face geometry, and the exact Section-123 dissection identity. The bank is one-use for pairwise disjoint unloaded route tails, including routes in different cells or with different projection directions. For overlapping routes the report correctly retains visit multiplicity; it does not infer bounded overlap.
- **REGRESSION VALID — promote `C-RHOMBIC-PATH-ROUTE-EXCESS-SHARP-REGRESSION`.** Exact oblique rhombic grids have paths of length asymptotic to twice their projection gain, with zero slow-vertex debit and no exceptional face. This refutes charging raw linear route length to face defect under the stated local pinned hypotheses. The coefficient two in the route inequality is sharp as a limiting local ratio.
- **REGRESSION VALID — promote `C-ATTACHMENT-TRIANGLE-DEBIT-REGRESSION`.** A positive pinned equilibrium with three triangular augmented faces and zero degree-above-four defect has a one-edge uphill route with debit `61/101`; attachment-triangle currency cannot be dropped from the local bank.
- **NOT PROMOTED — source report Section 5 attachment-gap statement.** The original leaf-attachment objection in this audit is withdrawn: the outer walk traverses a leaf's bridge twice but visits the leaf itself once. A noncut attachment that is an extreme hull vertex has one outer occurrence, including the leaf case. The [2026-10-15 preservation correction](../reports/monotone_route_attachment_gap_correction_2026-10-15.md) supplies the block proof and reconstructs the resulting gap and clipped-height inequalities. Those candidates remain outside canonical theorem state pending independent human review; Section 5 is not used by the three promoted claims.
- **CONDITIONAL ONLY — source report Sections 6 and 8 high-cap application.** The route conclusion from a high grid in a co-located host cap is valid under the stated geometric antecedent, but the source report cites that cap co-location as proof-only input. This audit does not promote the application or eliminate a C-II regime.

## Exact global theorem

Take a canonical contact-minimal, then diameter-pair-minimal C-II representative with `D>=9`. Let `V` be its nonisolated positive-contact core, `B` the actual loaded diameter endpoints, and `C` the full actual unit-contact graph on `V`. Canonical relative-interior stress gives every edge of `C` a strictly positive coefficient. Let `I_r` be the connected components of `C[V\setminus B]`, and let `A_r` be the distinct loaded attachments of `I_r`, `a_r=|A_r|`, and `a=sum_r a_r`. Contact-isolated source points remain in the full configuration but are not vertices of these route graphs.

For a unit vector `n`, and each `x in I_r`, define

```text
t_n(x) = max { n dot (y-x) : xy is an edge of C }.
```

Choose any maximizing edge of `C` as the successor of `x`. Every successor step is an actual unit contact with positive stress and strictly increases `n dot x`, so finiteness gives a directed forest rooted at actual attachments in `A_r`. The exact per-cell bank below is independent of `n` at the level of its charged vertex set.

Let `J_r^+` be the Section-123 augmentation: internal and attachment contacts plus the sides of `P_r=conv(A_r)`, with no other loaded-loaded chords. Let `Q_r^+` be its bounded face degree-above-four defect, `T_r` its bounded triangular-face count, `c_r^partial` the actual unit-contact polygon sides, and `M_r=a_r-c_r^partial`. Set

```text
U_A = sum_r (a_r-T_r),
C_partial = sum_r c_r^partial,
k = d_H+s_Z.
```

Define `E_r` as the unloaded core vertices incident with any bounded augmented face that either has degree at least five or has degree three or four and is not a strict unit rhombus. If `t_n(x)<1/2`, the sector containing `n` at `x` has angle greater than `2pi/3`, so its face is in this direction-independent set. A bounded quadrilateral all of whose sides are actual unit contacts is a unit rhombus; triangle-freeness excludes the limiting `pi/3` and `2pi/3` angles. A low-degree charged face contains a nonunit polygon-side occurrence. Each such side is adjacent to at most one bounded face; triangles use distinct such side occurrences and contain at most one unloaded vertex, while quadrilaterals contain at most two. A degree-`j>=5` face has at most `j<=5(j-4)` unloaded vertex occurrences. Therefore

$$
|E_r|\le 2M_r-T_r+5Q_r^+.
$$

Write `w_n(x)=(1-2t_n(x))_+`. Then

$$
\sum_r\sum_{x\in I_r}w_n(x)
\le \mathcal B
:=\sum_r(2M_r-T_r+5Q_r^+)
=a+10(e_{BB}-k-d_{tile})-4U_A-2C_{partial}
\le a+10(e_{BB}-k).
$$

The equality uses the canonical Section-123 identity
$$
\sum_r((a_r-T_r)+Q_r^+)=2(e_{BB}-k-d_{tile}),
$$
and `d_tile,U_A,C_partial>=0`. The last bound is the same global augmented-cell currency as Section 123, not a new face bank for each route.

For a successor route `gamma` from `z` to its first loaded attachment `b`, with `ell` unit edges and `Delta h=n dot(b-z)>0`, every edge is charged to its unloaded tail. Hence

$$
\ell-2\Delta h=\sum_{x\in\gamma\setminus\{b\}}(1-2t_n(x))
\le \sum_{x\in\gamma\setminus\{b\}}w_n(x).
$$

Thus `ell<=2 Delta h+2M_r-T_r+5Q_r^+` for one route. For a family with different projection directions, use the same charged sets `E_r`: a positive term `w_n(x)` can occur only at a slow vertex in `E_r`, and pairwise disjoint tails count each such vertex at most once; each weight is less than one. Therefore for any family of routes with pairwise disjoint unloaded tails, even if cells or directions differ,

$$
\sum_\gamma(\ell_\gamma-2\Delta h_\gamma)_+\le\mathcal B\le a+10(e_{BB}-k).
$$

For overlapping routes in one fixed successor forest, the valid bound is instead `sum_x m(x) w_n(x)`, where `m(x)` is the number of selected routes visiting `x`. No bound on `m` follows from this audit. Since `Delta h<=D`, the one-route estimate also gives `ell<=2D+2M_r-T_r+5Q_r^+`.

### Proof dependency audit

Canonical `C-MIXED-CORE-ONE-ROW-REDUNDANCY` ensures a relative-interior stress is strictly positive on every actual contact row. If all contact-neighbor projections at `x` were nonpositive, their positive weighted sum could vanish only when they all vanished; that would put all contact directions on one line and create a nonzero mixed flex supported at `x`, contrary to canonical `C-ZRF`. The contact neighbors span the plane, so `t_n(x)>0` for every direction. Harmonic measure on the connected unloaded component gives positive mass to each attachment. Since the canonical attachment set is in strictly convex position with at least three vertices, every unloaded vertex lies strictly inside `P_r`; hence its face sectors in `J_r^+` are bounded. These checks retain the core/source distinction and do not extend stress-kernel claims to contact isolates.

The shared bank algebra uses only the canonical finite Section-123 defect identity and its nonnegative dissection deficit. It does not use Section 5's outer-walk assertion, the proof-only host-cap localization, a first-order source motion, a source replacement, or a global-optimality inference from the local examples.

## Exact local regressions

### Rhombic paths with no defect debit

For positive integers `p,q` with `q^2-3p^2=-2`, starting at `(3,5)` and iterating `(p,q)->(2p+q,3p+2q)`, define

$$
c=\frac{p^2-1}{2p^2-1},\qquad s=\frac{pq}{2p^2-1},\qquad
u=(1,0),\quad v=(c,s),\quad N=p^2.
$$

Then `c^2+s^2=1` and `0<c<1/2`. Every lattice displacement has squared length `i^2+j^2+2cij`; its minimum over nonzero integer pairs is one, attained only on the two axes. Indeed, if `i^2+j^2>=3`, the quadratic form is at least `(1-c)(i^2+j^2)>1`; the only remaining non-axis case has `|i|=|j|=1` and length squared `2-2c>1` for opposite signs or `2+2c>1` for equal signs. The unit-contact graph is therefore the rhombic grid, whose bounded faces are strict rhombi and whose interior vertices have positive equilibrium with the four unit neighbors.

From `(N-1)u+v`, take `N-2` steps of `-u` and then `N-1` steps of `v`; this ends at the boundary pin `u+Nv`, so the full successor route has `ell=2N-3` edges. With `n=(v-u)/|v-u|`, both step projections equal `g=sqrt((1-c)/2)>1/2`; every route tail is an interior grid vertex and every debit vanishes. Direct calculation gives

$$
D_N=N\sqrt{2+2c},\qquad
\Delta h=(2N-3)g,\qquad
\left(\frac{\ell}{\Delta h}\right)^2=\frac1{g^2}=4-\frac2{p^2}\longrightarrow4.
$$

The family is an exact local pinned regression. Its pins are not asserted to be the canonical loaded set, and no global minimum-diameter optimality is claimed. The frozen verifier checks all pairs in its finite rational grids and the listed Pell identities; the all-`p` pair-distance claim above is established by the displacement calculation, not by enumeration.

### Attachment triangles carry a nonzero local debit

Pin the unit neighbors `(99/101,20/101)`, `(-99/101,20/101)`, and `(0,-1)` to the origin. Their pairwise distances exceed one, and positive weights `101/40,101/40,1` balance the origin. Add the three polygon sides between pins as the augmented boundary. Its three bounded faces are triangles, hence `Q^+=0`; upward projection has `t=20/101`, so the one-edge route debit is `1-2t=61/101`. This exact four-point local framework proves that the attachment-triangle term cannot be replaced by `Q^+` alone. It is not a canonical source or global-minimizer regression.

## Hostile checks and scope

- The selected-successor edge is an actual positive-contact edge, not an actual diameter edge, a geometric grid direction, or an artificial polygon side.
- Strict increase, not an Euler-path assertion, yields the forest and ensures each route terminates at a loaded attachment.
- The common bank bounds excess, not path length; the Pell family is an exact regression against raw-length charging.
- Routes sharing unloaded vertices reuse the debit; this audit makes no simultaneous-disjointness claim for arbitrary starts.
- A positive local stress, a pinned grid, or a local regression is not promoted to a canonical source or global minimizer.
- No claim closes the strong Type-II host-cap branch, C-II, or Level I.

## Certificate and canonical disposition

The frozen verifier was inspected and rerun from the exact source commit. It passed 6,966 exact source-pair checks, 100 greedy routes, overlap multiplicity 8, the exact `61/101` attachment-triangle debit, ten Pell arithmetic identities, and 56 attachment-pocket face walks/clipped-height ledgers. This is finite regression evidence only; it does not verify the analytic global bank, all members of the Pell grid family, the proof-only cap co-location hypothesis, global optimality, or a source competitor.

The audit promotes only the three claims listed above. The Section 5 attachment-gap argument and the Section 6 high-cap application remain outside canonical theorem state at the stated dispositions. C-II and Level I remain open; this promotion reduces a route-payment obligation but supplies no contradiction or finite source replacement.

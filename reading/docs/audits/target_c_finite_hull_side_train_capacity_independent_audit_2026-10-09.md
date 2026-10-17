> Generated reading edition · [exact source](../../../docs/audits/target_c_finite_hull_side_train_capacity_independent_audit_2026-10-09.md) · source SHA-256 `3a87a95abc5d50e42d409afab9b5d998a6d6557cd127f32eed25d2918e9b2ae3`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-0763D4D142C4","canonical":true,"claim_ids":["C-FINITE-HULL-SIDE-TRAIN-CAPACITY"],"claim_statuses":{"C-FINITE-HULL-SIDE-TRAIN-CAPACITY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.232 — exact finite hull-side train capacity

**Date:** 2026-10-09
**Canonical base:** `origin/main=08da5beefeb0cebeeabc532c83e814dba95b6241`, state `2026-10-09.audit.225`
**Frozen source:** `origin/research/sol/c2-high-t-capacity-audit-20261004` at `fdc40cc7844aaa8b5f949f59a8c1607edf43d65a`
**Candidate report:** `docs/reports/target_c_hull_side_exact_train_capacity_audit_2026-10-04.md`, SHA-256 `d0169556e724ed33adedcc55beaae354b6d31e296c6f6d0a278fcad34391273b`; last report commit `1651ff128bb7b2f287aa917074ffd8b621622ef8`
**Verifier:** `research/verify_target_c_hull_side_train_capacity_2026_10_04.py`, SHA-256 `1c11a1a886c0a06eae0dca7e68fd9e67270f2598b4329558bdbcce3d94b82fba`
**Verdict:** **PASS WITH NARROWED SCOPE — promote `C-FINITE-HULL-SIDE-TRAIN-CAPACITY`.**

## 1. Exact statement audited

For a finite canonical contact-minimal, then diameter-pair-minimal triangle-free global minimizer in the post-ZF C-II normal form, with `C=C_*`, `H=H_*`, all source labels retained, and positive-area actual loaded force hull `F`, let `q,b,x_B,m_B,f,Q,k,P_F` have the meanings stated in the promoted report. At most two complete trains have both terminal incidences on direct unit loaded-hull sides. The occurrence intervals satisfy

$$
\ell_i=1\iff |b_i-b_{i+1}|=1,
\qquad \sum_{\ell_i>1}\ell_i=x_B+m_B,
$$

and the source satisfies

$$
\boxed{5(q-k)+x_B+m_B\ge3P_F-2.}
$$

This is finite source geometry. It does not assert a finite move, a capacity surplus, or a branch elimination.

## 2. Independent reconstruction

The canonical outer-walk split has `q` intervals with `ell_i >= 1`, `sum_i ell_i=b`, and `P_F <= b`. `C-ATTACH-CURRENCY` gives harmonic trapping: each connected unloaded contact component lies in the convex hull of its loaded attachments, which are in `B`; loaded core vertices are themselves in `B`. Hence `V subset F`. For a consecutive loaded side of length one, the endpoints are in `C_*`; unit separation prevents a third source label in the open segment. The core containment puts every other contact neighbor on the inward side, so the exterior facial occurrence at that side is its direct contact edge. If `ell_i=1`, the unit-edge route has endpoint distance one. This establishes the exact good-interval classification, including a bridge edge's distinct inward facial occurrence. Consequently exactly the `m_B` nonunit loaded sides are bad intervals, and their total occurrence count is `x_B+m_B`.

For each actual rhombus, the train-link graph joins opposite contact edges. The canonical finite train theorem gives a path forest and the exact incidence count `T=(b+Q)/2+2f=(q-k)+2f`, with singleton contact-edge trains included. A train with two good ends has terminal sides parallel to its fixed projective direction and with opposite orientations. The directed edge angles of the strictly convex polygon `F` make one strictly ordered turn. A double-good train uses one side in each of two opposite directions. A strictly convex polygon has at most one side in each oriented direction, and each physical contact edge belongs to one train, so distinct double-good trains have distinct projective directions. For directions `0 <= theta_i < theta_j < pi`, their four directed sides occur in the order `theta_i, theta_j, theta_i+pi, theta_j+pi`. Their terminal pairs alternate on the boundary of `F`, so their embedded train arcs must cross. The canonical simple triangle-free crossing graph allows at most two such trains.

Each remaining train has a terminal occurrence either among the `x_B+m_B` bad outer occurrences or among the
$\sum_{G\text{ nonquadrilateral}}\deg G=4f+Q$ bounded exceptional-face incidences. Incidence counting gives

$$
T-2\le x_B+m_B+4f+Q.
$$

Substitute `T=(q-k)+2f`, then `f <= Q`, to get `q-k-2 <= x_B+m_B+3Q`. The canonical identity `Q=2(q-k)-b` yields `3b <= 5(q-k)+x_B+m_B+2`; `P_F <= b` gives the stated inequality. No asymptotic premise enters this derivation.

The source's separate small-excess Type-II application is superseded by the stronger canonical full-core floor `C-FULLCORE-HULL-DEPLETION-FLOOR` and by the Type-II separate-face floor. The promoted theorem extracts only the exact finite inequality at its broader finite-source scope.

## 3. Hostile scope checks

- The five-hull-end pentagon regression does not contradict the result: it rules out a local per-face bound, while this theorem bounds globally the number of trains with two good ends.
- The rational three-edge articulation star in the verifier tests repeated loaded-vertex outer occurrences; it is nonglobal and is not treated as a canonical counterexample.
- The exact unit-square fixture saturates the displayed inequality: `q=b=P_F=4`, `m_B=x_B=Q=f=0`, `k=2`, and `q-k=2`, so both sides equal `10`. It is a constant check only; no global-minimizer sharpness claim is needed.
- The report's scalar regression after dropping its small-excess premise is not a source configuration. It remains outside this promotion; no geometric realization or canonical-source conclusion is claimed.
- Contact-isolated points remain in the full source and in the global separation hypothesis. The proof uses no affine-kernel coordinates for them.

## 4. Verifier boundary and reproduction

Inspected the exact verifier and reran it from the frozen theorem stack. It uses rational `Fraction` arithmetic for pair distances, face walks, hull intervals, train components, and the finite slack identities. It checks 383 exact unit-separated triangle-free sources, including 354 with repeated outer walks and 225 with repeated loaded-vertex occurrences, plus 183,212 integer depletion ledgers. It confirms finite examples, the square sharpness, and the scalar arithmetic checks. It does not prove the universal occurrence lemma, the topological alternating-end argument, canonical global optimality, or any asymptotic statement; those are supplied only by the analytic reconstruction above and its canonical premises.

The current-main verifier blob equals the frozen source verifier blob. The source report itself has other claims; its artifact lifecycle is therefore left separate from this exact promoted claim.

## 5. Dependencies and disposition

- `C-LINEAR-NONMATCH`: canonical train path/crossing structure and triangle-free crossing graph.
- `C-LOADED-HULL`: canonical loaded-hull walk partition and `b+Q=2(q-k)`.
- `C-ATTACH-CURRENCY`: harmonic trapping places every unloaded contact component in the convex hull of its loaded attachments; together with the loaded core vertices this gives `V subset F`. The cap-budget theorem assumes this inclusion and is not its source.

**Claim classification:** proved candidate awaiting promotion → audited canonical finite theorem.
**Frontier effect:** none. This makes an exact finite accounting lemma reusable outside the near-disk branch. The current C-II finite-move/payment obligation and the macroscopic-container branch are unchanged.
**Discovery-worker protection:** audited the immutable `fdc40cc7844aaa8b5f949f59a8c1607edf43d65a` snapshot. No discovery branch or worktree was changed.

**Promotion transaction:** PR #942 head `87ea99e8a440d2577fa529b4379bb37fb0900166` merged as `ad88c61a77927891fa68c481369f7947bfd3f1fd`. Protected `state-consistency` run `38020546184` passed in 6m57s; merge tree `bb8c4e596f7f5157b200aa678fe0347da2a58d9d` exactly matched the reviewed head tree.

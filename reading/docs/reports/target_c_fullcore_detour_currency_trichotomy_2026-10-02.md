> Generated reading edition · [exact source](../../../docs/reports/target_c_fullcore_detour_currency_trichotomy_2026-10-02.md) · source SHA-256 `64db3e80b3552aa5deacf234bb65512d4990f4c15687524b3519964f5e15f985`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-0B69AA45750E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fullcore_detour_currency_trichotomy_2026-10-02.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=648f9249797f7b50ae0efe5f662aca3cb4ca8090; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Target C-II — full-core detour currency trichotomy

Date: 2026-10-02
Base main: fbeae9b3fa18a63e07573676b4e2e512a91ca4d5
Status: proof-only current-main composition; theorem-state unchanged.
LEVEL I STATUS: STILL OPEN. C-II remains open.

## Theorem

In every sufficiently large canonical full-core near-disk Type-II survivor, let
$`k=d_H+s_Z`$. Use the canonical Section 63 currencies $`Q`$, the global bounded
nonquadrilateral degree excess; $`m`$, the number of nonunit loaded-hull sides;
$`u_B=x_B-m`$, the outer-walk excess after paying one mandatory occurrence for each
nonunit hull side; $`s_C`$, total pinned-component surplus; and $`c_I`$, the number
of unloaded positive-contact components. Then

```math
\boxed{q-k=Q+u_B+s_C+c_I+2.}\tag{1}
```

The current-main near-disk chord-dissection theorem proves at proof-only scope
```math
q-k-\sum_r d_r\ge(\pi/2-1-o(1))D.\tag{2}
```
Canonical harmonic-cell area saturation and isodiametry give
```math
\sum_r d_r\ge D-o(D).\tag{3}
```
Canonical component deatomization gives $`c_I=O(D^{2/3})=o(D)`$. Therefore

```math
\boxed{Q+u_B+s_C\ge(\pi/2-o(1))D,}\tag{4}
```
and hence
```math
\boxed{\max\{Q,u_B,s_C\}\ge(\pi/6-o(1))D.}\tag{5}
```

Thus the disk-scale cell-shape detour forces a linear obstruction in at least one
of three concrete structures: global nonquadrilateral face defect, genuine excess
outer routing, or pinned component self-stress.

## Proof

Canonical Section 63 gives
```math
q-x_B=Q+2k,\qquad u_B=x_B-m.
```
Hence
```math
q-k=Q+k+m+u_B.\tag{6}
```
Canonical C-FULLCORE-LOADED-CHORD gives $`c_B=0`$ in the sufficiently large
full-core Type-II branch. Section 63 also gives
```math
c_I+s_C+c_B=m+k-2.
```
Thus
```math
m+k=c_I+s_C+2.
```
Substitution into (6) proves (1). The topology defect $`k`$ and the mandatory first
excess occurrence for each nonunit side $`m`$ cancel exactly.

For (3), write $`A_r=\operatorname{area}(P_r)`$. Canonical area saturation gives
```math
\sum_r A_r=\pi D^2/4-o(D^2).
```
Isodiametry gives $`A_r\le\pi d_r^2/4`$, so
```math
\sum_r d_r^2\ge D^2-o(D^2).
```
Since all $`d_r\ge0`$,
```math
\sum_r d_r\ge\sqrt{\sum_r d_r^2}\ge D-o(D).
```
Adding this to (2) yields
```math
q-k\ge(\pi/2-o(1))D.
```
Now apply (1) and $`c_I=o(D)`$ to obtain (4), and pigeonhole gives (5).

## Conditional sharpenings

If $`Q=o(D)`$, then
```math
u_B+s_C\ge(\pi/2-o(1))D,
```
so $`\max\{u_B,s_C\}\ge(\pi/4-o(1))D`$.

If $`Q=o(D)`$ and $`u_B=o(D)`$, then
```math
s_C\ge(\pi/2-o(1))D.
```
Together with $`c_I=O(D^{2/3})`$, at least one unloaded component has
```math
s_r=\Omega(D^{1/3}).
```

If $`Q=o(D)`$ and $`s_C=o(D)`$, then
```math
u_B\ge(\pi/2-o(1))D.
```

If $`u_B=o(D)`$ and $`s_C=o(D)`$, then
```math
Q\ge(\pi/2-o(1))D.
```

## Remaining bottleneck

This is a structural narrowing, not closure. A closing argument must eliminate one
of the forced branches:

- large $`Q`$: combine global face fidelity or inactive-corridor geometry with the
  actual diameter graph;
- large $`u_B`$: use convex Section-63 pocket geometry and stopped-train occupancy
  to rule out linear excess routing;
- large $`s_C`$: combine component deatomization and the resulting large local pinned
  surplus with a response/diameter obstruction.

The separate macroscopic-container branch remains open.

## Scope

Identity (1) uses only canonical Section 63 and C-FULLCORE-LOADED-CHORD. The linear
floor (4) also uses the proof-only current-main chord-dissection theorem in
docs/reports/target_c_neardisk_chord_dissection_shape_detour_2026-09-29.md, so
(4)-(5) remain proof-only and do not change theorem authority. Contact-isolated
source points remain retained. No full-source ZR/ZF extension, KKT coefficient floor,
rejected Euler-path/FB4/Reuleaux-cap route, or discarded Section-121 scaling
inference is used.

No computation, verifier execution, numerical search, CI result, or unexecuted
verifier code is used.

## Slot 2 recovery provenance — 2026-10-05

Recovered from `research/fullcore-detour-currency-trichotomy-2026-10-02` at exact source tip `24dc9accecd85eb2cfd50832bc7b810d68f53e80`. No original PR is associated with the source branch. This is an unreviewed proof-only full-core Target C-II composition; it does not change theorem status or close C-II/Level I. No standalone verifier or computational certificate was present on the source branch.

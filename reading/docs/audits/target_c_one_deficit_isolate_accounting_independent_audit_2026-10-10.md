> Generated reading edition · [exact source](../../../docs/audits/target_c_one_deficit_isolate_accounting_independent_audit_2026-10-10.md) · source SHA-256 `0af6c8478f5cf5e0446ed2f4bd51693e4728a88772f9e9f857e7771d6343af6d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-F28469852DC2","canonical":true,"claim_ids":["C-ONE-DEFICIT-ALL-M-SOURCE-EXCLUSION"],"claim_statuses":{"C-ONE-DEFICIT-ALL-M-SOURCE-EXCLUSION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit — one-deficit wall isolate accounting

**Date:** 2026-10-10
**Canonical base:** `origin/main=496abf9d1d0d080f5f992f1c74619f166de0d011`, state `2026-10-10.audit.231`
**Frozen source:** `origin/research/sol/target-c-overnight-closure-20261007` at `c6a75bd708e553c4feb3a540e0b17f3b65e22a82`
**Target status:** C-I closed; C-II open; Level I open.

## Verdict

**PASS WITH NARROWED SCOPE — already subsumed by canonical Audits.77, .80, and .107; no new theorem or frontier change.** The fixed-wall source-exclusion argument remains valid when the strict-interior population contains contact-isolated labels. It deletes and replaces those labels as part of the whole interior cloud. It retains every source label outside the wall, including exterior contact isolates. It makes no label-retention claim for interior isolates.

The new second-referee note is correct on this point. Its statement that current summaries had been clarified was premature at the refreshed main snapshot: Target C `CURRENT.md` and the active continuation prompt still used the ambiguous phrase “retaining ... contact isolates.” This change makes their scope match the proof. The independently audited theorem and dependencies were already canonical; theorem state remains `.231`.

## Exact claim and dependencies

For each fixed `M>=4` and fixed symmetric strictly decreasing rate profile, at every sufficiently small positive curvature allowed to depend on `M` and the profile, a contact-minimal then diameter-pair-minimal triangle-free global minimizer containing all `6M` vertices of the specified wall cannot have `z<=N-1` points in the strict wall interior, where `N=3M^2-3M+1` and `z` counts **all** strict-interior source labels, including contact isolates.

This is the existing fixed-wall claim, not an arbitrary-wall theorem. The exchange uses these canonical inputs:

- `C-ONE-DEFICIT-ALL-M-STRICT-PACKET`;
- `C-ONE-VERTEX-CONVEX-WALL-SHIELD`;
- `C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT`.

## Independent exchange reconstruction

Let `A` be the source, `W` the specified convex wall, `I=A intersect int(W)`, and `z=|I|`. No source point can lie in the relative interior of a unit wall side: its distance to a side endpoint would be strictly less than one. Thus all nonvertex labels in `W` are exactly the strict-interior cloud `I`.

When `z<=N-1`, choose `z+1` sites from the canonical strict packet. Delete every label in `I`, with no exception for contact isolates, and delete the one wall vertex `v_0` cleared by the packet construction. Insert the `z+1` selected sites. This preserves cardinality exactly. Every old label outside `W` remains, including exterior isolates.

The strict packet separation and the one-vertex wall shield make each inserted site strictly farther than one from every retained source label. Hence there are no new unit contacts, so the retained contact graph is an induced subgraph of the old triangle-free graph and stays triangle-free. Deleting `v_0` removes its two incident unit wall edges, so at least two old contacts are lost.

For the upper bound, `W` lies in `conv(A)` because all its vertices belong to `A`, and each inserted site lies in `int(W)`. For any retained old point `y`, the strictly convex function `x -> |x-y|^2` is strictly below its maximum at an interior point of `conv(A)`; the maximum is attained at an old source point and is at most `D^2`. Thus every inserted-to-retained distance is `<D`. Distances between inserted sites are `<diam(W)<=D`, and retained old pairs are unchanged. The competitor therefore has diameter at most `D`.

If its diameter is below `D`, this contradicts global minimum-diameter optimality for the same cardinality. If it equals `D`, it has at least two fewer unit contacts and no new ones, contradicting contact minimality. This proves the exclusion for `z<=N-1`, including interior-isolate populations, without preserving those labels' identities.

## Hostile scope checks

- The exchanged object is the full source, not just the positive-contact core; interior isolates are counted and removed, and exterior isolates are retained.
- The wall is the specified fixed wall already contained in the source hull. No extraction from an arbitrary canonical source follows.
- The result concerns global minimizers with the canonical lexicographic contact and diameter-pair choice. It does not infer global optimality from a local move.
- For Audit.107 the `z=N` case is separately classified as a sorting packet containing a unit triangle. The one-deficit exchange covers only `z<=N-1`.
- No claim is made that interior contact-isolated labels persist through the exchange.

## Verifier audit

At the frozen source commit, the report and verifier have SHA-256 hashes `7febb3769caec4221c83375c9c752168910c0370e5572c8296973a8574bba17a` and `c66a97dec048c4704e0629bcc56ac3432be634cdeaa489fd923f35ca50ba2081`, respectively. The verifier was rerun and exited 0. It uses exact rational and `Q(sqrt(3))` arithmetic. Its output reports eight base cases (`M=3,...,10`), three explicit window cases (`M=4,6,10`), 206,058 lower-pair checks, 304 constructive opening rows, and ten complete exact half-plane eliminations. `M=3` is explicitly only a local peeling regression.

This is finite certificate evidence only. It does not prove the analytic all-`M` packet theorem, the fixed-profile onset, the growing-`M` theorem, or any global-minimizer conclusion. Those conclusions rely on the separately audited proof and canonical dependencies listed above.

## Canonical disposition

The corrected wording now appears in Target C `CURRENT.md` and the active continuation prompt. The Target C `README.md` and `docs/STATE.md` already state that interior isolates are counted and replaced in the exchange, or otherwise scope isolate retention to exterior labels. The state version, canonical theorem IDs, route obligation, and C-II status do not change. No discovery branch or open PR was modified.

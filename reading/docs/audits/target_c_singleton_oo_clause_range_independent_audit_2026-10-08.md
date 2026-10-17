> Generated reading edition · [exact source](../../../docs/audits/target_c_singleton_oo_clause_range_independent_audit_2026-10-08.md) · source SHA-256 `1eb13b8220ad93f4c4750a4398d15c53cbb91ce7b6be4d25d465adcad57d291b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-0BC5F7E1874E","canonical":true,"claim_ids":["C-OO-SINGLETON-BAD-TERMINAL-CAPACITY"],"claim_statuses":{"C-OO-SINGLETON-BAD-TERMINAL-CAPACITY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: singleton O--O charge and clause-range claim

**Date:** 2026-10-08
**Audit base:** `origin/main=941700545e62cacdfaa02ab59be741c6df4f55b4`, state `2026-10-08.audit.150`
**Frozen source:** `research/sol/target-c-owner-order-closure-20261006` at `bf288c82e8a62466d5580025c94e750a177e63e2`
**Source artifact:** `research/target_c_singleton_oo_dual_tree_bandwidth_2026-10-06.md`, SHA-256 `ea684c81fd95bc1d73eaec46cc812f8cef7012aaa491c9fb3a1025f7b40c7941`

## Verdict

**PASS — promote `C-OO-SINGLETON-BAD-TERMINAL-CAPACITY`.** Every selected singleton O--O train consumes a distinct bad outer terminal occurrence. Since the canonical bad bank has size `x_B+m_B`, the singleton count is at most `x_B+m_B`.

**FAIL — proof gap for the claimed clause-range bound.** The source's `14 + x_B + m_B` dual-tree range conclusion depends on a bound of fourteen non-singleton O--O cuts per witness path. That estimate was explicitly withheld by Audit.138 because the frozen source did not give an exact inequality, a cut-to-rhombus injection, or the tube calculation. The arithmetic after that premise is valid, but the premise remains unproved.

The Audit.153 marked-interval theorem bounds loaded-cycle sides crossing one rooted branch; it does not bound the number of non-singleton cuts along a clause path inside a branch. The C-II frontier is unchanged.

## Exact surviving theorem

Use the canonical contact-minimal then diameter-pair-minimal C-II source with its full loaded-hull outer-walk decomposition. Let `q>=3` be the number of loaded hull vertices, `x_B=b-q` the outer-walk excess, and `m_B` the number of nonunit loaded-hull sides. Let `B_bad` be the canonical set of bad outer terminal occurrences, counted with facial multiplicity, so `|B_bad|=x_B+m_B` by the promoted terminal-capacity ledger. For any finite selected family `S` of actual singleton O--O trains in the canonical stopped-train system,

`|S| <= x_B + m_B`.

## Independent proof

A singleton O--O train is one outer-face contact bridge. Its edge has two distinct terminal occurrences in the outer facial walk, counted with facial multiplicity. The loaded-hull decomposition selects one distinguished exterior occurrence for each loaded hull vertex in cyclic hull order. A direct unit loaded-hull side has one distinguished one-edge interval occurrence; the reverse traversal of the same bridge is a separate outer-walk occurrence and cannot be a second distinguished occurrence of that physical side. If the bridge is not a loaded-hull side, neither traversal supplies that distinguished side occurrence. Thus no singleton bridge has two good terminal occurrences, so each selected singleton train has at least one bad terminal occurrence.

Terminal occurrences belong to unique complete stopped trains. Choosing one bad occurrence per selected singleton is therefore an injection from `S` into `B_bad`. The established bank size gives `|S|<=|B_bad|=x_B+m_B`. This argument permits bad--bad singleton bridges and does not require a direction window.

The result is already consistent with the global terminal allocation in [Audit.63](target_c_owner_order_and_terminal_capacity_promotion_audit_2026-10-06.md): non-singleton trains can consume the one fully-good exception, while singleton bridges cannot.

## Audit of the proposed dual-tree range

The source report decomposes a witness path into singleton and non-singleton dual edges. Its statement that each witness crosses at most fourteen selected non-singleton cuts is the only step that turns the valid singleton count into a uniform path-range bound. Audit.138 examined the corresponding frozen worker claim and withheld it: the report gave no exact fourteen-cut inequality, no definitions for the segment and midpoint-cut intersection sufficient to verify it, no injective assignment from cuts to distinct strict rhombi, and no tube-area estimate.

If that missing premise were proved, the remaining implication would be immediate: any simple dual-tree path uses at most `|S|` singleton edges, so its length would be at most `14+|S|<=14+x_B+m_B<=14+2x_B`; hence it would be `o(D)` when `x_B=o(D)`. The first inequality is conditional only. Audit.148/149's six-/five-row bounds require a supplied crosscut path with explicit distinct rhombus crossings; they do not extract such a path for every lower witness and do not repair the missing fourteen-cut premise.

No source verifier encodes the fourteen-cut geometry. The exact owner-system verifier checks finite tree, Horn, and binary-owner regressions only and is not used as proof evidence here.

## Canonical disposition

- Promote `C-OO-SINGLETON-BAD-TERMINAL-CAPACITY` at the exact occurrence-counting scope above.
- Do not promote the bound `dist_D(R_x,R_y)<=14+x_B+m_B` or the resulting `o(D)` range claim. Record them as **FAIL — proof gap** until the fourteen-cut geometry is independently completed.
- No source motion, strict-`D` competitor, or C-II / Level I consequence follows.

> Generated reading edition · [exact source](../../../docs/audits/target_c_overlap_aware_owner_capacity_independent_audit_2026-10-08.md) · source SHA-256 `5ef20be7acb2d2e657cbfc12f22f415d4505094b5ce3578da5a07a1c7f629c2a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B248C3CED18A","canonical":true,"claim_ids":["C-OO-OVERLAP-AWARE-ROOT-RUN-CAPACITY"],"claim_statuses":{"C-OO-OVERLAP-AWARE-ROOT-RUN-CAPACITY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: overlap-aware owner root/run capacity

**Date:** 2026-10-08  
**Audit base:** origin/main 68fd5283948795061c5e40c9c6192da1d960fadd, state 2026-10-08.audit.126  
**Source branch and immutable snapshot:** research/sol/target-c-owner-order-closure-20261006 at bf288c82e8a62466d5580025c94e750a177e63e2  
**Source artifacts:** docs/reports/target_c_hub_owner_terminal_capacity_audit_2026-10-06.md (SHA-256 61e16a888f99858fc6af890c05f4ac1ba27efd0394ea6e65434b29412dbf3468); research/verify_target_c_hub_owner_systems_2026_10_06.py (SHA-256 0618e67333980c32b867b64272a099a6edbc30c2d47d6913e8ea7ccf38c9414b)  
**Verdict:** PASS WITH NARROWED SCOPE — promote the exact owner-bank inequality below.  
**Frontier:** C-II and Level I remain open.

## 1. Exact audited statement

Use the finite actual O–O system in the canonical localization theorem on the connected nonisolated positive-contact core. Assume:

1. the selected stopped O–O trains are actual pairwise disjoint proper crosscuts, and the owner translation is constant on each region after deleting the selected cut edges;
2. every old unit contact remains exactly unit under every independent binary owner selection;
3. each nonzero owner translation has norm below one, distinct nonzero owner translations are mutually acute, and every retained selected-cut increment is nonzero;
4. the loaded force-hull vertices have their canonical cyclic order among distinguished occurrences on the outer contact-face walk.

Pairwise disjointness is an explicit hypothesis. The promoted acute-binary laminarity result excludes crossing in its stated actual binary model, and C-OWNER-REGION-TREE-RECURRENCE supplies the dual-tree statement for disjoint proper crosscuts. This audit does not infer disjointness for a generic crossing multishear model. Let T_OO be the number of selected complete stopped O–O trains. For each owner i, let T_i count the selected trains whose two adjacent region labels are zero and i. Let r_i be the number of cyclic runs of owner i on the loaded-hull word. Let I be any set of owners whose outer-walk word has a nonempty complement, and let J be a set of owners for which an active unary strict-rhombus root is specified. Here a root for i is a bounded strict unit rhombus with two adjacent vertices of owner i, the other two fixed, and the resulting opposite moving/fixed contact edges in the selected train system.

Then
```math
\boxed{\sum_{i\in I} r_i + |J\setminus I| \le T_{\rm OO}.}
```

In particular, if each i in I occurs on the loaded hull, then
```math
|I\cup J| \le T_{\rm OO}.
```
With the canonical acute-binary terminal bound, the right side is at most x_B+m_B+1. This is a finite capacity statement. It does not establish a beneficial pin, a simultaneous feasible motion, or a full-source competitor.

The statement does not apply to arbitrary crossing multishears, to a post-hoc contraction that identifies distinct source vertices as owners, or to owners charged only through unloaded endpoints. Contact-isolated source points remain in the full configuration and are outside this core train count.

## 2. Independent reconstruction

### One selected train has one owner bank

Suppose an old contact joins distinct moving owners i and j, with contact vector v and translations Delta_i, Delta_j. Exact unit-contact preservation in the four independent binary states gives
```math
|v+\Delta_i-\Delta_j|^2-|v+\Delta_i|^2-|v-\Delta_j|^2+|v|^2
=-2\Delta_i\cdot\Delta_j=0.
```
This contradicts the acute hypothesis. Thus an old contact cannot join two distinct moving owners.

Across a selected cut, equal region translations would give zero increment, excluded by hypothesis. Its adjacent regions therefore cannot both have label zero or the same owner. They also cannot have distinct nonzero owner labels, by the identity above. Every selected cut consequently separates label zero from one unique owner i. Since each stopped train is one of these actual cuts, assigning that train to i partitions the selected train set into disjoint banks T_i, with sum_i T_i=T_OO.

This is the missing step that the earlier Audit.63 properly withheld: the general terminal-occurrence bound alone did not provide an owner-specific allocation. The acute-binary cut conditions do.

### Loaded runs spend terminals from their own bank

Let r_out(i) be the number of maximal cyclic outer-walk runs carrying owner i. A change of owner across an outer contact occurrence must lie on a selected cut edge: otherwise its endpoints remain in one component after the selected cut edges are deleted and have the same translation label. The cut-bank argument assigns each such boundary occurrence to the unique bank T_i.

Every outer run of i with nonempty complement has two distinct boundary occurrences. They are terminal occurrences of complete stopped trains. A selected train has exactly two terminal occurrences, counted with facial multiplicity for a singleton bridge. Distinct run boundaries are distinct outer-walk occurrences, so
```math
r_{\rm out}(i)\le T_i.
```
Restricting the outer walk to the distinguished loaded-hull occurrences cannot split one outer run into two, and distinct loaded runs remain separated by a retained loaded vertex of another owner. Hence r_i<=r_out(i)<=T_i.

### A unary rhombus root spends a train from its owner's bank

For a root owned by j, the two moving/fixed contacts are opposite sides of the same bounded strict rhombus. The canonical stopped-train decomposition links opposite rhombus sides, so these contacts lie in one complete train. The train has nonzero increment across the root's owner boundary and therefore belongs to T_j. Thus T_j>=1 for each j in J.

For i in I use r_i<=T_i. For j in J\I use one unit from T_j. The banks for different owner labels are disjoint, so summing these charges proves the boxed inequality. Owners in I intersect J are charged only by r_i; no second train is assumed for them.

## 3. Adversarial scope and certificate review

- The direct mixed-norm identity rules out a train cut between two distinct moving labels. A repeated owner label on disconnected regions causes no collision: each zero/i cut remains uniquely assigned to i.
- Singleton bridges retain two distinct facial terminal occurrences. The proof counts occurrences, not physical edges.
- The loaded-run charge requires an outer-walk complement. The theorem does not silently extend to unloaded owner tails.
- The rhombus charge is for an active root with the stated two-moving/two-fixed pattern. It does not charge every bounded rhombus or every abstract unary clause.
- The source verifier was inspected and rerun at its exact main-tree input. It reported 14,182 tree-bank checks, 110,887 Horn/pinning checks, and 72 binary packets. Its recurrence routine allocates abstract tree edges to their unique nonzero endpoint; it does not encode outer-run geometry, rhombus-root support, source coordinates, equilibrium, or global optimality. It is a finite accounting regression, not the analytic proof.
- The verifier's one-train unary packet is explicitly marked as having no source realization. It is not a counterexample to the audited theorem or a Target C source configuration.

The audit does not promote the source report's other section-4 applications, unloaded-tail bounds, or any claim that this capacity creates a useful pin.

## 4. Canonical disposition and remaining limit

Promote C-OO-OVERLAP-AWARE-ROOT-RUN-CAPACITY with dependencies on C-OO-LOWER-BLOCKER-LOCALIZATION, C-ACUTE-BINARY-OO-LAMINARITY, C-OWNER-REGION-TREE-RECURRENCE, C-NEAR-UNIT-CONFLICT-GEOMETRY, and C-LINEAR-NONMATCH. This closes the specific owner-to-train allocation gap noted in Audit.63 for the stated acute binary cut system. It does not alter the canonical Target C obligation: an owner-capacity bound still supplies no source-level compatible shortening, no strict-D competitor, and no Level I consequence.

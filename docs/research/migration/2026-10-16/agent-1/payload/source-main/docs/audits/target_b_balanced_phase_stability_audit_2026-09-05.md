<!-- theorem-state: {"artifact_id":"ART-F154D751D898","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Audit — Target B balanced phase stability exclusion

**Date:** 2026-09-05  
**Candidate:** `docs/reports/target_b_balanced_phase_stability_exclusion_2026-09-05.md`  
**Verdict:** PASS for the equal-size balanced model under the stated coherent dense-core hypotheses.  
**LEVEL I status:** STILL OPEN.

## 1. Triple-defect identity

For equal classes of size `m`, each phase edge belongs to exactly `m` transversal triples. Triangle-freeness makes every triple contain at most two edges, so

`D_3=sum d=2m^3-mE`.

If `E>=(2-epsilon)m^2`, then `D_3<=epsilon m^3`.

PASS.

## 2. Slice-good anchor

At most `sqrt(epsilon)m` vertices of either `A` or `B` can have slice defect above `sqrt(epsilon)m^2`. If the `A`–`B` pair has more than `4sqrt(epsilon)m^2` nonedges, more than `2sqrt(epsilon)m^2` of them have two slice-good endpoints.

Averaging `d(ab)` over those nonedges gives one with

`d(a_0b_0)<=sqrt(epsilon)m/2`.

Because `a_0b_0` is absent, every `c` not adjacent to both endpoints contributes at least one to this defect. Thus

`|C_*|>=(1-sqrt(epsilon)/2)m`.

PASS.

## 3. Approximate two-colouring

For `A_1=N(b_0) cap A`, every `A_1`–`C_*` edge is forbidden by a transversal triangle. Missing `A_0`–`C_*` edges each cost one defect in the slice through `b_0`, so there are at most `sqrt(epsilon)m^2` of them. The symmetric statement holds for `B`.

For `a in A_1`, `b in B_1`, `c in C_*`, both phase edges to `c` are absent, hence `d(a,b,c)>=1`. Therefore

`|A_1||B_1||C_*|<=epsilon m^3`.

Since `|C_*|>=m/2`, one of `A_1,B_1` has size at most `sqrt(2epsilon)m`. The corresponding opposite phase pair has only `O(sqrt(epsilon))m^2` missing edges.

PASS.

## 4. Ordered extraction

Within one coherent train class, tracks are pairwise noncrossing, so every train of a second class has a consecutive crossing interval. The already audited dense interval-bigraph lemma therefore turns `o(m^2)` missing crossings into a complete `(m-o(m)) x (m-o(m))` rectangle.

PASS.

## 5. Diameter comparison

The audited trimmed-grid theorem allows the third phase to contribute arbitrary coherent cancellation of magnitude at most its size. At balanced scale `t=1`, its constrained diagonal minimum is exactly `3`, independent of the third-phase scalar within the admissible range.

Hence

`D^2>=(3-o(1))m^2`.

Near-extremal crossing count gives `n=(2-o(1))m^2`, while the strict translated-lattice comparison gives

`D^2<(4sqrt(3)/pi+o(1))m^2`.

Since `4sqrt(3)/pi<3`, contradiction follows.

PASS.

## Scope

The proof as written assumes equal class sizes. It does not by itself justify the asymptotically balanced `M,M,(1-o(1))M` case, which needs an explicit trimming-to-equal-size reduction. That reduction is handled separately.

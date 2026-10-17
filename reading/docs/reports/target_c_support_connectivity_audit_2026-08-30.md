> Generated reading edition · [exact source](../../../docs/reports/target_c_support_connectivity_audit_2026-08-30.md) · source SHA-256 `98739f29fab60877a6b6873e4e1509db8b445934aa3d681d5100fe002107c71b`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-F9E3D66A0BF7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — audit note for Target C support connectivity

**Date:** 2026-08-30  
**Repository state:** `research/target-c-force-hull-v2-2026-08-30`  
**Audits:** `docs/reports/target_c_support_connectivity_2026-08-30.md`  
**LEVEL I STATUS:** `STILL OPEN`

This note replaces only the proof of Lemma C12.4 in the support-connectivity report.
The original conclusion is correct, but its nesting-forest wording was more informal
than necessary.  The induction below is self-contained and removes that avoidable
topological gap.

## Audited Lemma C12.4

> **Lemma C12.4 (two interval blocks).**  If a noncrossing partition of a finite
> cyclically ordered set has at least two blocks, then at least two blocks consist of
> cyclically consecutive elements.

### Proof

Induct on the number of blocks.  The statement is immediate for two blocks: if one
block were not a cyclic interval, two of its elements would separate elements of the
other block into two nonempty cyclic gaps, giving an alternating quadruple and hence a
crossing.

Now let the partition have at least three blocks and choose any block `B`.  List the
elements of `B` in cyclic order.  The open cyclic gaps between consecutive elements of
`B` have the following property:

```math
\boxed{\text{every other block is contained entirely in one such gap.}}
\tag{A12.1}
```

Indeed, if another block `L` met two distinct gaps, choose two elements of `L` in
those gaps and two suitable consecutive elements of `B` separating the gaps.  Around
the circle the four chosen points alternate between `B` and `L`, contradicting
noncrossing.

Hence each nonempty gap inherits a noncrossing partition by whole blocks.

There are now two cases.

1. **At least two gaps are nonempty.**  In each such gap, choose an interval block of
   the induced linear/cyclic subpartition.  Such a block exists by induction if the
   gap contains at least two blocks, and is the unique block if the gap contains one.
   Because no block crosses the endpoints of the gap by (A12.1), that block is also a
   cyclic interval block of the original partition.  Two different nonempty gaps give
   two distinct interval blocks.

2. **Exactly one gap is nonempty.**  Then all elements outside `B` lie in that one gap,
   so `B` itself is a cyclic interval block.  The induced partition inside the unique
   nonempty gap has at least one block; choose an interval block there, again using
   induction if necessary.  It is a second interval block of the original partition.

No gap can be nonempty zero times because the original partition has at least two
blocks.  Thus at least two cyclic interval blocks always exist. `\square`

## Effect on Theorem C12

No other line of the proof changes.  Lemma C12.3 still shows that the sets
`B_K=B_+\cap V(K)` form a noncrossing partition of the cyclic force-hull vertices.
The audited lemma supplies two disjoint interval blocks.  Since positive diameter
reaction directions lie strictly inside the corresponding vertex normal cones, the
two interval angular spans have total strictly less than `2\pi`; one span is strictly
less than `\pi`.  The reaction vectors of that component therefore lie in an open
half-plane and cannot have zero sum, contradicting the component reaction balance.

Thus Theorem C12 remains:

```math
\boxed{C_+\text{ has exactly one nontrivial connected component}}
```

for every normalized KKT stress.

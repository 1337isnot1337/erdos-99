# Hostile audit — collapsed support-six ten-crossing floor

**Audited source:** `target_c_support6_collapsed_ten_crossing_floor_2026-09-19.md`  
**Certificate:** `verify_target_c_support6_collapsed_ten_crossing_floor_2026_09_19.cpp`

The new certificate uses the same exact affine MI.1 reduction and forced crossing
rotations as the audited seven-crossing certificate. It canonicalizes all 388
labelled rotation cells to 42 conservative symmetry representatives, then checks
weights 7, 8, and 9. For each candidate it applies, in order:

1. the full affine MI.1 equations;
2. triangle-freeness of the complete-train crossing graph;
3. simultaneous strict angle-window feasibility;
4. every permutation of multiple crossing vertices along each train; and
5. exact Euler-genus planarization.

The reproduced aggregate counts are:

```text
k=7: parity=4909, triangle-free=3965, metric=2544, planar=0
k=8: parity=11944, triangle-free=9340, metric=5801, planar=0
k=9: parity=27650, triangle-free=19455, metric=10453, planar=0
```

The certificate asserts these totals and asserts zero planar candidates. A planar
global stopped-train drawing with fewer than ten internal crossings would appear in
one of these cases, because the actual crossing order on each train is among the
enumerated permutations. External trains cannot repair a nonplanarization after
they are deleted from the retained internal subdrawing.

The resource inequality `R_4>=10c_6` does not double-count: distinct relation
components have disjoint internal train sets, and each strict rhombus contains
exactly two complete trains. The displayed sigma bound is only algebraic
substitution into the already audited tangent/support count; it is not presented
as a new canonical terminal contradiction.

**Audit disposition:** PASS for the stated exact ten-crossing floor and its scoped
resource consequence. C-II remains open.

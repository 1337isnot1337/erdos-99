<!-- theorem-state: {"artifact_id":"ART-CE5429891F64","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-a"} -->
# Audit — Target A boundary-terminal common-source V-paths

**Date:** 2026-09-05  
**Candidate:** `docs/reports/target_a_boundary_terminal_common_source_vpaths_2026-09-05.md`  
**Verdict:** PASS.  
**Global LEVEL I status:** STILL OPEN.

## 1. Two-sided boundary-band count

For a convex body `K` of perimeter `P`, let `T_w(partial K)` be the Euclidean width-`w` two-sided boundary band. Radius-`1/2` disks around unit-separated points in this band are disjoint and lie in the width-`r=w+1/2` two-sided tube.

The outer tube has area `rP+pi r^2` by Steiner. For the inner tube, the coarea identity for inner parallel sets gives

`area(K)-area(K_r)=integral_0^r per(K_t)dt<=rP`,

with the integrand taken as zero after the inner parallel body disappears. Thus the full tube area is at most

`2rP+pi r^2`.

Dividing by `pi/4` gives

`# <= 8rP/pi+4r^2`.

For `w=2`, `r=5/2`, this is

`20P/pi+25`.

Cauchy gives `P<=pi d`, hence the candidate's `20d+25` bound.

PASS.

## 2. Both source images lie in the width-two band

Every `c in C^partial` lies in `X^partial`, so Section 99.25 gives

`dist(c,partial K^*)<=1`.

The zero-slack matching has `|c-a_c|<1`, hence

`dist(a_c,partial K^*)<2`.

Every `o in O` lies in `Y_in\Z`, where `Y_in subset int(K^*+B)`. Thus `dist(o,K^*)<1`; because `o` is not an interior point of `K^*`, its distance to the boundary is below one (zero if it lies on the boundary). Its matched source point `b_o` therefore also lies within distance below two of `partial K^*`.

PASS.

## 3. Inclusion-exclusion overlap

The two zero-slack matchings are independent but each is injective into `A^0`. Their source-image sets have cardinalities exactly

`|S_C|=|C^partial|`, `|S_O|=|O|`.

Both lie in a unit-separated source subset of size at most `20d+25`. Therefore

`|S_C cap S_O|>=|C^partial|+|O|-(20d+25)`.

No identification of the matchings is used.

PASS.

## 4. One common mediator gives one actual V-path

A common source point `a` has one unique `C^partial` partner in the first matching and one unique `O` partner in the second matching. Both arms have length strictly below one.

Distinct common mediators give distinct `C^partial`, `O`, and source vertices because both matchings are injective.

PASS.

## 5. Interference degree

Within each matching, the straight segments are pairwise disjoint by Theorem 163.1. Therefore intersections between two different V-paths can only occur between a `C`-arm from one matching and an `O`-arm from the other matching.

Theorem 163.2 and its exact cell-degree consequence state that one `X`-to-source matching segment crosses at most four lattice-to-source matching segments, while one lattice-to-source segment crosses at most five `X`-to-source segments. The present shores are restrictions of exactly those two types: `C^partial subset X^*` and `O subset Y_in`.

Hence a V-path can interfere with at most `4+5=9` other V-paths. Shared mediator endpoints between distinct paths are impossible by construction; shared `C` or `O` endpoints are impossible by matching injectivity.

Thus the interference graph has maximum degree at most nine and contains an independent set of size at least `L/10`.

PASS.

## 6. Scope

The selected V-paths are pairwise disjoint as polygonal arcs and connect actual Schur-source vertices to actual exterior lattice sinks through distinct genuine source points. This does not imply a direct `C^partial-O` conflict edge, an alternating Schur linkage, or Schur nullity.

The candidate correctly stops at the geometric gate family.

## 7. Conclusion

The lower bound

`G_CO >= (1/10) max(0, |C^partial|+|O|-20d-25)`

for pairwise disjoint zero-slack source-mediated `C^partial-A^0-O` V-paths is valid.

The next legitimate use is geometric: classify these gates relative to a contact shield and charge shield-crossing gates before attempting any sectorwise rank conclusion.

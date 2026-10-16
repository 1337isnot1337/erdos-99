# Joint diameter-cover exchange and whole-source regressions

**Source:** open draft PR #957, frozen at `a11e16998094ab3d7afd9fd07eff8b55909ec406` (tree `77ce8dd135c2b4233f121bd448621d362841da06`), with source-PR merge base `d6f953100d62a84de72e991642041fdd026e82ba`. The source branch is older than frozen source main and its comparison includes stale main-side deletions. The actual source-PR branch delta is the seven paths in the [frozen branch-change manifest](../migration/2026-10-16/baseline/pr-files/957.branch-changes.txt), not every difference between source main and the old branch tree. **Lifecycle:** the matching identity is a proved noncanonical candidate; all packet-existence claims remain unproved. See the [per-file ledger](../migration/2026-10-16/ledger/source-pr-files.jsonl), [scientific reconciliation](../migration/2026-10-16/scientific-reconciliation.md), and [source audit](../../audits/pr957_autonomous_proof_audit_2026-10-15.md).

## 1. Exact joint cost for a supplied packet

Let `A=(a_1,...,a_n)` be any unit-separated planar source of actual diameter `D>0`. Let `B=(b_1,...,b_m)` be a separately labelled unit-separated packet with `diam(B)<D`. Build the complete actual-diameter graph `H` on `A`, and the bipartite cross-conflict graph `G` by joining `a_i` to `b_j` exactly when

`|a_i-b_j| < 1` or `|a_i-b_j| >= D`.

The upper inequality is inclusive: a mixed set must have diameter *strictly* below `D`. Coincident labels are lower conflicts. For each vertex cover `T` of `H`, let `nu_T` be the maximum matching size in the cross-conflict graph restricted to `(A\T) union B`, and put

`K(A,B) = min_{T covers H} (|T| + nu_T)`.

The report proves the exact identity

`maximum size of a unit-separated strict-D subset of A union B = n + m - K(A,B)`.

For a fixed `T`, deleting `T` pays for every actual source diameter pair; the maximum independent set of the remaining bipartite conflict graph has size `n-|T|+m-nu_T`, by the matching/minimum-vertex-cover theorem proved in the report. Conversely, every feasible mixed subset omits a cover of `H`, so optimizing over all covers is exact. No independently feasible exchanges are combined by assumption.

A supplied packet gives an `n`-point strict-`D` competitor iff some cover satisfies `m-|T|-nu_T >= 0`. Therefore a global diameter minimizer must satisfy `|T|+nu_T >= m+1` for *every* unit-separated `B` with diameter below `D` and every cover `T`. Every source label, including every contact isolate, participates in `G` and in the cardinality count.

**The exact missing Level I theorem** is existence of such a successful packet: prove that for every sufficiently large triangle-free global minimizer `A` there is a finite unit-separated `B` with `diam(B)<D` and a cover `T` of the actual diameter graph such that `nu_T <= |B|-|T|`. The report proves the consequence once `B,T` are supplied; it does not prove they exist.

## 2. Regressions that constrain the search

The full report has four exact small controls: (a) a three-label star where the unique minimum-cardinality diameter cover fails but a larger inclusion-minimal cover gives a nonglobal strict competitor; (b) a source of four labels augmented by a smaller three-label packet; (c) the unit square, a global four-label source for which a supplied packet does not improve the maximum mixed population; and (d) a translated packet whose upper cross-conflicts form `K_(4,3)`. The lower-conflict graph alone is planar and has degree at most five, but the complete lower-and-upper graph need not be planar. Thus neither minimum-cardinality covers nor lower blockers alone determine the correct objective.

The all-`k` rational construction is an unbounded regression. For every `k>=4`, `D=k^2`, `|A_k|=pi D^2/(2 sqrt(3))+O(D)`, `|B_k|=|A_k|-1`, the source has exactly one unit contact and `|A_k|-2` contact isolates, and the cross-conflict graph is exactly a matching. The unique one-label diameter cover has exchange profit `-1`, while the cover deleting all `k` diameter leaves has profit `0`; retaining the old origin and using the packet yields the same cardinality at diameter exactly `D-1/8`. Every source in this construction is explicitly **nonglobal**. The regression invalidates a minimum-cover-first algorithm and refutes no global-minimizer conjecture.

**Finite checks:** [`verify_global_joint_exchange_2026_10_12.py`](../../../research/verify_global_joint_exchange_2026_10_12.py) checks the rational graph identity against exhaustive mixed-subset enumeration and controls for invalid edges, duplicate matching edges, incomplete covers, and missing right labels. [`verify_global_exchange_star_family_2026_10_12.py`](../../../research/verify_global_exchange_star_family_2026_10_12.py) checks the complete pair ledgers at `k=4,5` (57 and 256 source labels; 55 and 254 isolates). The all-`k` proof is analytic; the finite runs do not establish a successful packet for arbitrary minimizers.

## 3. Free-region propagation: a separate local cage regression

The accompanying research-run note explores replacing the full source inside a free region, based on Schurmann's 2006 theorem for a smooth fixed container and packing families with two uniform-geometry controls. It records why those hypotheses cannot be inferred from triangle-freeness alone. A rational four-label cage has center `0` and three unit neighbors

`u=(1,0)`, `v=(-(1-t^2)/(1+t^2), 2t/(1+t^2))`, `w=(0,-1)`.

The neighbors have pairwise distance greater than one, while positive coefficients satisfy `a*u + v + b*w = 0` for positive `a,b`; the line through `u,v` misses the center by `t/sqrt(1+t^2)`, tending to zero. Given any `R>0`, choose `t<1/(4R)` and center a radius-`R` ball at `(Rt,R)`. All four labels lie outside the ball, but the origin is only `R*(sqrt(1+t^2)-1)` beyond its boundary. This is an exact local obstruction to a uniform free-region propagation lemma based only on triangle-freeness and an adjacent free ball. The four-label source is nonglobal and no global-source or free-ball-in-hull statement is claimed.

A destination report already preserves a different Schurmann-near-miss family: [two-copy similarity obstruction](../../reports/global_two_copy_similarity_obstruction_2026-10-12.md). The new four-label cage is a distinct bounded local configuration and explicit arbitrary-radius placement; it complements the dense-ring failure of uniform affine-span controls rather than replacing it. Schurmann's paper remains a legitimate citation/link only; no third-party text or PDF is copied or used as a load-bearing premise.

## 4. Current frontier and use order

1. Use the joint cost formula to evaluate a *supplied* whole-source packet without dropping actual diameter pairs, upper conflicts, coincident labels, or isolates.
2. Do not optimize minimum diameter-cover size before checking the matching cost. The all-`k` regression shows this loses a valid simultaneous strict competitor even at asymptotically optimal leading density.
3. Do not planarize the complete cross-conflict graph. Only the lower-conflict graph has the stated planar embedding.
4. Do not reuse the free-region route by assuming a uniform contact affine-span gap from triangle-freeness. The bounded cage regression blocks that implication.
5. Read the source AI audit for proof reconstruction and finite controls. It is provenance, not the independent destination exact-head AI review required before consequential promotion.

The two Python programs verify finite/formal propositions only. The theorem-state manifest remains unchanged; the packet-existence bridge and Level I closure are still open.

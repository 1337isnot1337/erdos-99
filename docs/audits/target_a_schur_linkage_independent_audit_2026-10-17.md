<!-- theorem-state: {"artifact_id":"ART-358694DA4F4B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-a"} -->
# Independent audit: finite Target A Schur/linkage verifier

Date: 2026-10-17. **Verdict: PASS within the declared finite and abstract scope.**
Target A and Level I remain open.

## Source and scope

I reviewed the checker, saved output, and report at PR #78 head
`9f230b2f900bf050a27ce7430ae7b3fed8ef8eda`, against fetched `origin/main`
`e396ea07887dd0528b817ce4e656ff0e6b01f8fb`. The reviewed source files are
[`verify_target_a_schur_linkage_2026_10_17.py`](../../research/verify_target_a_schur_linkage_2026_10_17.py),
its [saved JSON](../../research/target_a_schur_linkage_2026_10_17.json), and the
[author report](../reports/target_a_independent_schur_linkage_2026-10-17.md).
Their bytes at the reviewed head match the fetched main versions.

At selection, the authoritative state was `2026-10-15.publication.2`,
priority revision `public-frontier.3`, and catalogue revision
`public-frontier.7`. This audit changes neither theorem state nor priority;
the task catalogue is updated to revision `public-frontier.8` to record the
new exact-SHA review and the refreshed open-PR snapshot.

This audit reconstructs the generic Schur/linkage correspondence from Sections
102 and 113, then the tube/shield and sector bookkeeping in Sections 173--175.
It checks the exact finite enumeration and the verifier's adversarial controls.
It does not reprove the geometric construction of an actual response shield or
audit the upstream stress, source, and global-optimality chain.

## Proof reconstruction

Let `B` and `Z` have equal size and let the support contain a fixed matching
`mu:B->Z`. Give each support edge its own algebraically independent variable.
The matching supplies a nonzero monomial in `det A[Z,B]`, so this block is
invertible over the rational-function field. For equal-size `I subset O` and
`J subset C`, block elimination gives

```text
det S[I,J] = det A[Z union I, B union J] / det A[Z,B].
```

Every determinant monomial is the edge set of a matching. Distinct permutations
use distinct edge sets, so a bordered determinant is nonzero exactly when its
support has a matching saturating `B union J` and `Z union I`. The column-support
matroid is transversal, and `B` is independent because of `mu`. Matroid
augmentation therefore lets a maximum independent subset of `B union J` be
chosen to contain `B`. It follows that `rank(S[:,J])` is
`max{|K|: K subset J and B union K is matchable}`. For any such `K`, choose a
matching saturating `B union K`. Its symmetric difference with `mu` decomposes
into alternating paths and cycles. The components beginning at vertices of
`K` end at distinct right vertices unmatched by `mu`, hence in `O`: every
`B` is covered by both matchings, so these paths cannot end at `Z`. Retaining just those
components and `mu` elsewhere gives the required bordered matching.
Conversely, flipping `mu` along vertex-disjoint `K`-to-`O` paths gives such a
matching. This proves the claimed rank/linkage equality without an acyclicity
assumption.

Splitting each graph vertex into an in/out pair with a unit-capacity internal
arc enforces vertex-disjoint paths, including capacity one at sources and
sinks. Directed vertex Menger then identifies the maximum flow with the minimum
vertex separator, where terminal vertices may be deleted. A matched `Z-B` pair
can be contracted only with capacity one: its `Z` endpoint has no outgoing arc
except the matched arc, and its `B` endpoint has no incoming arc except that
arc. Thus every path using either endpoint uses the pair as one indivisible
unit. The verifier's contraction preserves that capacity.

For the shield calculation, write
`W = T union C_sh union mu^{-1}(T intersect Z)`, with every neighbor of each
`c in C_sh` lying in `T`. A directed path meeting `T` is charged to one of its
vertices. A path starting in `C_sh` must next enter `T`; a path visiting a
shielded basis vertex must have entered it from its matched `Z` vertex in `T`.
Since the paths are vertex-disjoint, at most `|T|` paths meet `W`. Every other
path stays in one connected component of the surviving internal support until
its final sink. The terminal and sink endpoints of these paths form a matching
in the coarse graph joining each sector's terminals to every surviving sink
adjacent to that sector. Consequently

```text
rank(S) <= |T| + nu(coarse sector-sink graph).
```

This bound remains valid when a sink is shared by several sectors; the matching
capacity records that sharing. Since `O` splits into tube sinks, surviving
sinks, and then isolated sinks plus sector sinks,

```text
|O| - rank(S) >= |O_surviving| - |T intersect Z| - nu(coarse graph).
```

When the sector sink sets are pairwise disjoint, the coarse matching number is
`sum_i min(|C_i|,|O_i|)`. Substitution gives both checked forms:

```text
|C| - rank(S) >= |C_sh| + sum_i max(0, |C_i|-|O_i|) - |T|
|O| - rank(S) >= |O_iso| + sum_i max(0, |O_i|-|C_i|) - |T intersect Z|.
```

The second formula depends on sink disjointness. The overlap-safe formula above
uses `nu(coarse graph)` instead. The verifier keeps these cases separate.

## Finite domain and replay

The checker enumerates all supports with `B=C=Z=O=2` labelled vertices per
shore, a fixed diagonal `B-Z` matching, and every optional edge among the 14
remaining left-right pairs. Each terminal must have a direct exterior-sink
neighbor, matching the definition of a boundary terminal. Hence the domain has
`4 * 16 * 16 * 9 = 9,216` supports. For each support it checks all four
terminal subsets against symbolic bordered determinants, unit-capacity flow,
and exhaustive injections; it also enumerates all vertex separators and checks
unit-capacity matching contraction. Across all supports and admissible tube /
shield-terminal choices, the exact results are:

| Check | Cases |
| --- | ---: |
| Terminal-subset rank/flow/injection comparisons | 36,864 |
| Full-set separator comparisons | 9,216 |
| Full-set matching-contraction comparisons | 9,216 |
| Tube/shield cases | 234,176 |
| Disjoint-sink cases using the separate-sector formulas | 176,984 |
| Shared-sink cases using the coarse matching formula | 57,192 |
| Strict improvements over the older full-shield charge | 150,408 |

The rank-one total `704` also has a direct count. Rank two holds whenever the
direct `C-O` support has a size-two matching. Otherwise both terminals share
one singleton sink. For the four possible directed off-diagonal `B-Z` edge
sets, the counts of `C-Z` choices times choices of `B` edges to the other sink
that avoid an alternate path are `25, 22, 22, 19`. The other sink has two
possible identities and the two `B` edges to the common sink are arbitrary, so
the rank-one count is `2 * 4 * (25+22+22+19) = 704`; the remaining `8,512`
supports have rank two.

Five controls reject tempting weakened rules:

- Without terminal interception, true rank `2` exceeds the proposed cut upper
  bound `1`.
- With two sectors sharing both sinks, the separate-surplus expression gives
  the false lower bound `2` while true right deficiency is `0`; the coarse
  matching formula gives `0`.
- Contracting a matched pair without vertex capacity raises flow from `2` to
  `3`; unit-capacity contraction retains `2`.
- Reversing the matched-edge orientation changes a support's flow from the
  correct rank `2` to `1`.
- Setting four independent `C-O` variables equal to one changes a rank-two
  generic Schur block to rank one; the checker correctly tests generic support
  rank, not arbitrary specializations.

Reproduction from repository root (Python 3.14.8):

```sh
python research/verify_target_a_schur_linkage_2026_10_17.py \
  --check research/target_a_schur_linkage_2026_10_17.json
python -O research/verify_target_a_schur_linkage_2026_10_17.py \
  --check research/target_a_schur_linkage_2026_10_17.json
python research/tube_shield_cut_audit.py
python tools/check_public.py
```

All passed. Both optimized and ordinary runs returned the same saved counts and
controls. The predecessor one-sink audit returned `PASS: 17104 exact
graph/tube/shield cases; 15056 strictly improved lower bounds`. Public
integrity returned `passed` with zero errors. No theorem-state file or claim
lifecycle was changed.

## Exact remaining gap

The finite graph argument does not establish that a canonical geometric source
produces a shield satisfying the abstract inputs, nor that its sector surplus
closes Target A. The locked-branch endpoint still needs, for an actual
plateau-terminalized response and stress-generated fan,

```text
|O_iso| + sum_i max(0, |O_i|-|C_i|) >= j_* + |T_Z|,
```

or a same-cardinality strict-diameter competitor retaining every source label.
The zero-slack branch and the universal quantifiers over all sufficiently
large cardinalities and all global minimizers also remain open. The checker
does not solve Erdős Problem #99.

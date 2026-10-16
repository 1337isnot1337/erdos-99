<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "e407548de3570f86857f4d60faedd411deba4a12", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/global_discrete_isometry_blocker_closure_2026-10-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f6cad41fcd649de78fedb1ec01e68351b2ca6b81ddf1a9ba7777d08e3313dc64"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Global discrete isometries: exact endpoint decisions and blocker closure

**Date:** 2026-10-12.
**Baseline:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`.
**State:** `2026-10-10.audit.234`.
**Target:** Level I, independent full-source competitor route.
**Classification:** proved candidate awaiting promotion; artifact unreviewed.
**Active prompt:** `../prompts/erdos_problem_99_GPT6_ASTRA_FULL_SOLUTION_PROMPT.md`.
**LEVEL I STATUS: STILL OPEN.**

## 1. Global obligation and mechanism selection

The objective is the full quantifier in
[`statement.md`](../problem/statement.md). This run considered independent
population replacement, a second-order motion of the whole source, and
discrete relocation by isometries. Population replacement needs a
source-specific upper capacity estimate; density alone does not supply it.
Weighted stress improvement does not certify the inactive upper pairs of
a finite motion. The discrete route checks the complete endpoint and permits
infeasible intermediate positions.

```text
common-isometry dictionary + compatible state assignment
  -> every actual source label placed with every pair in [1,D)
  -> same-cardinality strict-sub-D competitor
  -> contradiction to global optimality.
```

The endpoint decision is proved for two states. A universal dictionary and
assignment theorem is not proved. A binary dictionary has an intrinsic
odd-cycle obstruction. The blocker-closure theorem below is a global
necessary condition without Target C stress hypotheses and without
discarding contact isolates.

## 2. Exact two-state endpoint theorem

Let `P=(p_1,...,p_n)` be a finite unit-separated source with `n>=2` and
diameter `D`. The cardinality condition excludes the vacuous singleton case,
whose diameter zero cannot be strictly decreased.
Let `T` be any Euclidean isometry. Each label chooses

\[
q_i=T^{x_i}p_i,\qquad x_i\in\{0,1\},
\]

where `T^0` means identity, not an assumption that `T` is involutive.
For each `i<j` and state pair `(a,b)`, forbid the pair exactly when

\[
|T^a p_i-T^b p_j|<1\quad\text{or}\quad
|T^a p_i-T^b p_j|\ge D. \tag{1}
\]

There is a full-source unit-separated endpoint of diameter strictly below
`D` if and only if the clauses

\[
(x_i\ne a)\lor(x_j\ne b) \tag{2}
\]

for these forbidden pairs are satisfiable.

**Proof.** Each clause excludes precisely one violating choice of two
actual positions. Satisfying all clauses checks every one of the
`n(n-1)/2` actual source pairs against both bounds. Thus no label is lost,
no coincidence is possible, and the finite maximum of the upper distances
is strictly below `D`. Conversely any such endpoint satisfies the clauses.
The implication-graph SCC criterion decides (2), with `O(n^2)` graph
operations after exact comparisons are available. Algebraic bit complexity
is not included in that graph bound.

New contacts and triangles are allowed: a strict smaller-diameter source
contradicts globality regardless of its contact graph. No feasible
interpolation or stress claim is required.

## 3. Exact exhaustion of a translation parameter

For rational source coordinates, rational nonzero `v`, and
`T_t(p)=p+t v`, the unequal-state distances have squares

\[
|p_i-p_j|^2\pm2t\,v\cdot(p_i-p_j)+t^2|v|^2. \tag{3}
\]

All coefficients and `D^2` are rational. Forbidden pairs change only at
the real roots of (3) equal to `1` or `D^2`. There are `O(n^2)` roots.
Compare and sort them exactly; test each root and one rational point in
each intervening open interval. Every forbidden pair is constant on an
open interval, so these tests decide the entire continuous parameter
family. Roots themselves matter because a new unit contact is allowed,
including when feasibility exists at only one parameter. A new diameter
pair is forbidden for strict improvement.

It suffices to test `t>=0`: complement the moved set and translate the
whole endpoint by `-t v` to identify its distances with the opposite-sign
parameter. For `t|v|>2D`, every unequal-state distance exceeds `D`, so only
constant states remain and neither strictly improves the diameter.
The sweep uses at most `O(n^4)` graph operations, in addition to exact
algebraic root and sign costs. Failure excludes this direction/dictionary,
not arbitrary competitors.

## 4. Full-source global blocker closure

If triangle-free global minimizers exist for a fixed `n`, choose one with
minimum contact count and then minimum actual diameter-pair count in that
class. Both integer minima exist in the nonempty class; compactness of the
open triangle-free class is unnecessary.

Call `T` generic if every unequal-state pair distance is different from
`1` and `D`. Generic translations exist because finitely many circles in
the translation plane are excluded.

On **all** source labels put an arc `i -> j` exactly when

\[
|T p_i-p_j|<1\quad\text{or}\quad |T p_i-p_j|>D. \tag{4}
\]

It forbids `(x_i,x_j)=(1,0)`, equivalently `x_i<=x_j`. Feasible moved sets
for the non-strict interval `[1,D]` are exactly forward-closed sets of this
directed blocker graph `B_T`.

**Theorem.** Every actual contact edge and every actual diameter edge has
its endpoints in the same SCC of `B_T`, for every generic `T`.

**Proof.** Distinct SCCs can be separated by a forward-closed union: in
the condensation DAG choose the forward closure of a component that does
not reach the other. Applying `T` to this union satisfies every source
lower and upper bound. Same-state pairs retain their old distances;
genericity prevents any unequal-state pair from creating a new contact
or diameter pair. Hence triangle-freeness persists.

Separating a contact strictly opens it, contradicting the first integer
minimum. Separating a diameter strictly shortens it. Either contacts also
decrease, already a contradiction, or their count stays fixed and the
diameter-pair count decreases, contradicting the second minimum. A strict
decrease in the actual diameter would contradict globality immediately.
Isolates remain vertices and can mediate blocker paths.

For reflections and half-turns the unequal-state distances agree, so SCCs
reduce to undirected components. For general translations direction
matters. This theorem concerns the chosen normalized counterexample;
it does not assert the integer minima for every original minimizer or
transfer an original source's lattice geometry to a different source.

## 5. Two global obstructions to binary or axis-only closure

**Odd actual diameter cycles.** A same-state old diameter pair keeps
length `D` under any common two-isometry dictionary. Strict improvement
therefore requires a proper two-coloring of the complete original
diameter graph. An odd cycle makes that impossible, independently of all
lower constraints and of the chosen isometry. One binary cut cannot be a
universal closing theorem for this topology. Several successive cuts or
at least three states are not ruled out.

**Arbitrarily large Cartesian grids.** Horizontal relocation by any
number of translations leaves `m` labels on each row of an `m by k` unit
grid. Unit separation forces each row's span to be at least `m-1`.
For bottom extremes `a,b` and top extremes `c,d`,

\[
\max\{|d-a|,|b-c|\}\ge m-1,
\qquad (d-a)+(b-c)=(b-a)+(d-c)\ge2(m-1).
\]

Those cross-row pairs have vertical separation `k-1`, so some endpoint
distance squared is at least `(m-1)^2+(k-1)^2`, the original diameter.
Thus even independently chosen horizontal shifts cannot improve it.
The vertical statement is analogous. Large grid nonglobality is compatible
with this infinite-family obstruction: a different rearrangement is needed.
An exact unsuccessful sweep is not a global-optimality certificate.

## 6. Exact computation and hostile pairs

Run `python3 research/verify_global_discrete_isometry_2026_10_12.py`.
The checker uses SymPy rational and exact real-algebraic signs. It tests
all translation-offset cells, compares 2-SAT against exhaustive assignments
for small sources, and independently checks every pair of each successful
endpoint. Its fixtures include two separated unit chains, four direction
sweeps of a unit square, and a horizontal sweep of the `3 by 3` grid.
The preservation repair of 2026-10-15 refuses optimized Python, validates
that endpoint state vectors retain every source label and are binary, and
rejects truncated and nonbinary states. It does not convert these fixtures
into a universal source theorem.

The hostile source

\[
(0,0),(10,0),(9,1),(1,1),(1,2)
\]

has diameter `10`, a single diameter pair `0,1`, and a single unit contact
`3,4`. Translate only labels `0,2` by `(21/10,0)`. Every lower constraint
holds and the old diameter strictly shortens, but old inactive pair `2,3`
becomes `101/10>D`. The offending moved label is a contact isolate.
The full pair solver rejects the purported competitor exactly.

## 7. Dependencies, classification, and remaining bridge

The proofs use the canonical problem definition, elementary Euclidean
arithmetic, and the finite Boolean/SCC equivalences proved here. No
unpromoted report, stress weight, or source/co-embedding is a premise.
External reconnaissance checked the [problem page](https://www.erdosproblems.com/99);
it supplied no new theorem used in the argument.

The new claims are **proved candidates awaiting promotion**, in an
**unreviewed** artifact. The odd-cycle and grid statements are also
regressions for universal binary or axis-only claims. No canonical state
or current route prompt changes.

The exact remaining bridge is to supply, for every sufficiently large
triangle-free global minimizer, a finite dictionary with at least three
states and a simultaneous full-source assignment with all distances in
`[1,D)`. Coloring the old diameter graph is insufficient: every inactive
pair and every isolate must enter the conflict instance. That extraction
theorem and Level I remain unproved.

The [preservation audit](global_discrete_replacement_preservation_2026-10-15.md)
records the exact original source and complete proof/history comparison.

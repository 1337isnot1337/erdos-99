<!-- theorem-state: {"artifact_id":"ART-E1196A93C7AE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "ffb27942a58c68d4c22b5c2d82778a96b4ed49ff", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/erdos_problem_99_2026-08-30_phase-cover-stability.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "6fe37d39bf85846c4c2807e1704d577bab0bc9298a4d2576ecec41cc4ec50867"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — phase-cover stability checkpoint

## A weighted cover lemma for a three-phase core

Consider a tripartite crossing graph \(G\) with phase classes
\(A,B,C\), of sizes \(a,b,c\). Assume that no triple with one vertex in each
class is a triangle. Write \(X_{AB},X_{BC},X_{CA}\) for the sets of nonedges
between the corresponding classes. Then every \(A\times B\times C\) triple is
covered by at least one of these three nonedge sets.

Suppose, after relabelling, that

\[
a\le b\le c.
\]

Put

\[
R=c(a+b)-|E(G)|.
\]

The extremal bound is

\[
\boxed{|E(G)|\le c(a+b).}
\tag{1}
\]

More importantly, the deficit \(R\) controls the nonedges of the two links
incident with the largest class:

\[
\boxed{
(c-a)|X_{BC}|+(c-b)|X_{CA}|
\le cR.
}
\tag{2}
\]

### Proof

Give every triple in \(A\times B\times C\) weight \(1/c\). A nonedge in
\(X_{AB}\) covers \(c\) triples and therefore has weighted cover cost \(1\); a
nonedge in \(X_{BC}\) covers \(a\) triples and has cost \(a/c\); and a nonedge
in \(X_{CA}\) has cost \(b/c\). Since the nonedges cover every triple,

\[
ab
\le |X_{AB}|+\frac ac|X_{BC}|+\frac bc|X_{CA}|.
\tag{3}
\]

On the other hand, the total number of nonedges is

\[
|X_{AB}|+|X_{BC}|+|X_{CA}|
=ab+R,
\tag{4}
\]

because the total number of possible cross-class pairs is
\(ab+bc+ca\). Subtracting the weighted expression in (3) from (4) gives (2).
It also gives \(R\ge0\), which is (1). \(\square\)

## Equality and quantitative stability

If \(c>b\), equality in (1) is rigid:

\[
R=0
\quad\Longrightarrow\quad
X_{BC}=X_{CA}=\varnothing,
\qquad X_{AB}=A\times B.
\tag{5}
\]

Thus the crossing graph is exactly the complete bipartite graph with parts
\(C\) and \(A\sqcup B\). Indeed, (2) forces the two displayed link sets to be
empty, while (4) then forces every \(AB\) pair to be a nonedge.

The same calculation is quantitative. If

\[
\Delta=c-b>0,
\]

then \(c-a\ge\Delta\), and (2) implies

\[
|X_{BC}|+|X_{CA}|\le \frac{c}{\Delta}R.
\tag{6}
\]

The number of \(AB\)-edges is

\[
|E_{AB}|=ab-|X_{AB}|
=|X_{BC}|+|X_{CA}|-R,
\tag{7}
\]

so the whole graph differs from the complete bipartite cut
\(C\mid(A\sqcup B)\) in at most

\[
2\bigl(|X_{BC}|+|X_{CA}|\bigr)
\le \frac{2c}{\Delta}R
\tag{8}
\]

edge edits. In particular, if \(c\ge(1+\rho)b\), the edit distance is at most
\(2(1+\rho)R/\rho\).

## Consequence for the jammed phase route

The phase-order theorem in the Target B module supplies exactly the hypothesis
used above: an oriented phase-core edge cannot complete a directed transversal
triangle, so the nonedges cover every one-from-each-phase triple. The lemma
therefore adds a clean dichotomy to the current endpoint:

* if the three phase classes have a fixed positive imbalance, a near-extremal
  crossing core is close to a single complete bipartite cut, with an explicit
  error proportional to its edge deficit;
* the unresolved two-colour splitting can persist only in the balanced or
  near-balanced regime, where \(c-b=o(c)\) and the factor in (8) becomes large.

This does not yet solve the geometric biclique-to-additive-block problem. It does
remove an entire unbalanced branch from that problem and gives the exact parameter
that a future geometric argument must charge: the phase imbalance \(\Delta\) or the
crossing deficit \(R\).

## Sanity checks

For \(a=b=c=m\), (1) becomes \(|E(G)|\le2m^2\), the balanced phase bound. The
weights in (3) are all equal, so no link is forced to be sparse; this is exactly
the equality-splitting obstruction already isolated in the Target B module.

For \(a=b<m<c\), equality forces all \(AB\) pairs to be nonedges and all \(AC\),
\(BC\) pairs to be edges. This is the unique extremal pattern up to relabelling
of the phase classes.

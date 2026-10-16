# Target C-II: loaded sink obstructions force cyclic owner recurrence

**Date:** 2026-10-05
**Authority checked:** current main `583203ac1dc1d7bc49f0ca0574d75e85f9de2ee1`, state `2026-10-05.audit.62`.
**Status:** proof-only Target C reduction; theorem state unchanged. C-II and Level I remain open.

## 1. Purpose

Audit.61 reduces a sufficiently small actual O--O finite-motion failure, after
the stated upper checks and unary-rhombus tests, to outer-face near-unit lower
clauses. Audit.62 adds the finite loaded-hull theorem that every loaded pair of
length at most (13/12) is a side of the cyclic loaded hull for (D\ge6).

The stable worker's preceding acute-clause note proves that, after prime
reduction, one physical two-owner lower pair has only one binary role, and a
binary-only sink implication SCC (S), (|S|=m\ge2), needs at least (m+1)
distinct physical lower-pair witnesses: (m) implication witnesses plus one
internal incompatibility.

This note converts that witness debt into an exact loaded-hull occurrence debt.

## 2. Every loaded lower witness is a loaded-hull side

Let (s) be the diameter of the translation cloud in the audit.61 O--O
motion. Canonically
\[
s<\gamma_D:=D-\sqrt{D^2-1}
=\frac{1}{D+\sqrt{D^2-1}}.
\]

If an old noncontact pair (pq) becomes a lower blocker in any binary state,
its relative displacement changes by a vector of norm at most (s). Therefore
\[
1<|pq|\le1+s.
\tag{1}
\]

For (D\ge7),
\[
\gamma_D<\frac1{2D-1}\le\frac1{13}<\frac1{12},
\]
so
\[
|pq|<\frac{13}{12}.
\tag{2}
\]

If both endpoints of (pq) are loaded diameter endpoints, canonical
`C-LOADED-NEAR-UNIT-ADJACENCY` now forces (pq) to be an actual side of
the loaded hull.

This step is finite. It uses the exact audit.61 cloud bound and the exact
audit.62 loaded-hull threshold, not an asymptotic near-unit approximation.

## 3. Cyclic run bound

Fix a set (S) of moving owners. For each owner (i\in S), let (r_i)
be the number of maximal cyclic runs of loaded-hull vertices carrying owner
(i); put (r_i=0) if (i) has no loaded hull vertex. Define
\[
R(S)=\sum_{i\in S}r_i.
\]

Let (E_S) be the number of loaded-hull sides whose endpoints carry two
distinct owners in (S). Then
\[
\boxed{E_S\le R(S).}
\tag{3}
\]

Proof. Mark the cyclic loaded-hull vertices whose owners lie in (S).
Each maximal marked component is a path unless every hull vertex is marked.
Within a path component, compress each maximal same-owner run. With (r)
runs there are at most (r-1) original hull sides joining distinct
(S)-owners. If every hull vertex is marked, the compressed object is a
cycle and has at most one such side per run. Summing over components gives
(3). \(\square\)

## 4. Sink-obstruction payment

Let S be a binary-only sink SCC of the reduced implication graph, with
m=|S|>=2. Its simple implication digraph has at least m distinct arcs.
Choose m of them so that every owner in S is incident with a chosen arc:
take a directed spanning out-arborescence with m-1 arcs and add any further
distinct implication arc. Choose one physical pair witnessing each selected
implication arc, and one further physical pair witnessing the internal
incompatibility. Acute prime reduction makes these m+1 physical pairs
distinct.

Let (u(S)) be the number of these chosen witnesses having at least one
endpoint that is not loaded. The other
\[
m+1-u(S)
\]
witnesses are loaded-loaded. By Section 2 each is a distinct loaded-hull side
joining two distinct owners in (S). Hence
\[
m+1-u(S)\le E_S\le R(S).
\]
Therefore
\[
\boxed{u(S)+R(S)-|S|\ge1.}
\tag{4}
\]

This is the new finite Target C reduction.

### Loaded-only corollary

If every chosen witness is loaded-loaded, (u(S)=0). Every owner in (S)
then occurs on the loaded hull, so (r_i\ge1), and
\[
\boxed{\sum_{i\in S}(r_i-1)\ge1.}
\tag{5}
\]

Thus every loaded-only binary sink obstruction forces at least one owner to
occur in two disjoint cyclic loaded-hull runs.

For the smallest possible binary sink,
\[
A\to B,\qquad B\to A,\qquad A\not\sim B,
\]
the three required physical witnesses cannot fit into one loaded-hull run of
(A) and one of (B). One owner must return in a second run.

### Simultaneous sinks

For pairwise disjoint sink SCCs (S_1,\ldots,S_t), choose the irreducible
witness packet above in each sink and write (u_a=u(S_a)). The owner sets,
hence the chosen physical witness packets, are disjoint. Summing (4) gives
\[
\boxed{
\sum_{a=1}^t u_a+
\sum_{a=1}^t\bigl(R(S_a)-|S_a|\bigr)\ge t.
}
\tag{6}
\]

Every sink obstruction therefore spends at least one unit of either:

1. an outer-face witness with an unloaded endpoint; or
2. cyclic loaded-owner run excess beyond one loaded-hull run per owner.

## 5. What this does and does not close

This removes the possibility that a loaded-only contradiction is supported
by owners that each occupy one cyclic loaded-hull interval. It is stronger
than source-level path-forest control because it survives owner contraction.

It does not prove that repeated loaded-owner runs are impossible. A repeated
owner run is not automatically one of audit.53's canonical loaded return
paths. Audit.62's cap theorem does not bound every unloaded outer-face witness
inside the loaded hull.

The next exact Target C theorem should therefore prove one of two payments:
either every extra loaded-owner run consumes actual stopped-train/loaded-return
capacity, or every remaining unloaded-endpoint witness consumes a separately
bounded outer-face currency. That is now the residual owner-order bottleneck.

The macroscopic-container branch remains separate.

All statements above are analytic finite proofs. No computation, verifier,
CI result, or numerical experiment is a proof premise.

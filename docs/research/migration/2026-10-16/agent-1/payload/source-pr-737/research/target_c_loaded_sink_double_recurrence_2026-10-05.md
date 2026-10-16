# Target C-II: a loaded binary sink needs two repeated owners

**Date:** 2026-10-05
**Authority checked:** current main `583203ac1dc1d7bc49f0ca0574d75e85f9de2ee1`, state `2026-10-05.audit.62`.
**Status:** proof-only Target C reduction; theorem state unchanged. C-II and Level I remain open.

## 1. Target

The current outer-face Horn obstruction has two already-proved payments on the
stable worker branch:

1. a binary-only sink SCC \(S\) needs an internal incompatibility in addition
   to its implication structure; and
2. every sufficiently short loaded-loaded lower witness is an actual side of
   the cyclic loaded hull.

The preceding run-count theorem only concluded that a loaded-only sink forces
at least one repeated loaded owner. This note strengthens that conclusion to
two distinct repeated owners and gives the corresponding simultaneous-sink
bound.

## 2. Physical-pair irreducibility

Work in the audit.61 finite O--O translation scope after prime reduction.
For distinct moving owners \(i,j\), one physical old noncontact pair can have
only one irreducible binary role:

- one implication \(i\to j\);
- one implication \(j\to i\); or
- one incompatibility \(\neg x_i\lor\neg x_j\).

The mixed-difference identity
\[
f_{11}-f_{10}-f_{01}+f_{00}
=-2\Delta_i\cdot\Delta_j<0
\]
rules out the only apparent two-implication escape after unary reductions.
In particular, reciprocal implications require two distinct physical pairs,
and an incompatibility witness is distinct from every implication witness.

This is the acute-prime lemma already proved in
`target_c_acute_horn_sink_obstruction_2026-10-05.md`.

## 3. Three incident loaded witnesses force owner recurrence

Let \(S\) be a binary-only sink SCC of the reduced implication digraph, with
\(|S|\ge2\). Let \(ab\) be any internal incompatibility edge of \(S\).

Strong connectivity gives owner \(a\) at least one incoming and at least one
outgoing implication inside \(S\). They are distinct directed arcs. By
Section 2, choose distinct physical pairs witnessing those two arcs; the
physical pair witnessing the incompatibility \(ab\) is a third distinct pair.
Thus owner \(a\) is incident with three distinct physical binary witnesses.
The same statement holds for owner \(b\).

Suppose all three witnesses incident with \(a\) are loaded-loaded. In the
audit.61 displacement range,
\[
1<|pq|\le1+s,\qquad
s<D-\sqrt{D^2-1}.
\]
For \(D\ge7\), \(1+s<13/12\). Canonical
`C-LOADED-NEAR-UNIT-ADJACENCY` therefore makes every one of these three
physical pairs a distinct side of the loaded hull.

Let \(r_a\) be the number of maximal cyclic loaded-hull runs carrying owner
\(a\). Because every selected witness joins two distinct owners, it is an
owner-transition side. A cyclic owner run has only two boundary sides, so
owner \(a\) is incident with at most \(2r_a\) loaded-hull transition sides.
Hence
\[
3\le2r_a,
\qquad\text{so}\qquad
\boxed{r_a\ge2}.
\tag{1}
\]
Likewise, if the three selected witnesses at \(b\) are loaded-loaded, then
\[
\boxed{r_b\ge2}.
\tag{2}
\]

Therefore every internal incompatibility edge has the following exact
alternative:
\[
\boxed{
\begin{array}{c}
\text{one of the selected incident implication/incompatibility witnesses}\\
\text{has an unloaded endpoint}
\end{array}
\quad\text{or}\quad
r_a\ge2\ \text{and}\ r_b\ge2.
}
\tag{3}
\]

In particular,
\[
\boxed{\text{a loaded-only binary sink SCC contains at least two distinct
repeated loaded owners.}}
\tag{4}
\]

This is strictly stronger than the earlier conclusion
\(\sum_{i\in S}(r_i-1)\ge1\).

For the minimal two-owner obstruction
\[
A\to B,\qquad B\to A,\qquad A\not\sim B,
\]
all three physical pairs are incident with both owners. A loaded-only
realization therefore forces
\[
\boxed{r_A\ge2,\qquad r_B\ge2.}
\tag{5}
\]

## 4. Simultaneous sink payment

Let \(S_1,\dots,S_t\) be pairwise disjoint binary-only sink SCCs. For each
\(S_c\), choose one internal incompatibility edge \(a_cb_c\), and at each of
its endpoints choose one incoming and one outgoing implication in \(S_c\).
Choose one physical witness for each selected clause.

Let \(u^\sharp(S_c)\) be the number of distinct selected physical witnesses
having an unloaded endpoint, and let
\[
N_{\rm rep}
=
\#\{i\in\cup_cS_c:r_i\ge2\}.
\]

If \(u^\sharp(S_c)=0\), (3) gives two distinct repeated owners in \(S_c\).
If \(u^\sharp(S_c)>0\), that sink already spends at least one unloaded
witness. Thus
\[
1\le
u^\sharp(S_c)
+\frac12\#\{i\in S_c:r_i\ge2\}.
\tag{6}
\]

The sink owner sets are disjoint, so selected physical witness packets from
different sinks are disjoint. Summing gives
\[
\boxed{
t\le
\sum_{c=1}^t u^\sharp(S_c)
+\frac12N_{\rm rep}.
}
\tag{7}
\]

The companion note
`target_c_unloaded_sink_outer_occurrence_payment_2026-10-05.md` proves that
every family of distinct surviving lower witnesses with an unloaded endpoint
has cardinality at most
\[
6(b-q+Z_{\rm out}).
\]
Therefore
\[
\boxed{
t\le
6(b-q+Z_{\rm out})
+\frac12N_{\rm rep}.
}
\tag{8}
\]

Compared with the preceding aggregate estimate
\[
t\le
6(b-q+Z_{\rm out})
+\sum_c(R(S_c)-|S_c|),
\]
(8) identifies the residual loaded obstruction more sharply: once the
outer unloaded budget is exhausted, every additional sink consumes two
distinct owners which each occur in at least two loaded-hull runs.

## 5. Remaining Target C obligation

The remaining geometric payment is now narrower. It is not enough for a
loaded-only sink to have one owner return somewhere else on the loaded hull.
It must have an incompatibility edge whose two endpoint owners both recur in
disjoint loaded-hull runs.

The next useful theorem should charge such paired recurrence to the actual
ordered O--O cut geometry or to audit.53 loaded-return capacity. No claim is
made here that a repeated owner is itself a stopped train or a canonical
loaded return.

Unary rhombus blockers and the at-most-\(d_H\) upper exceptions remain
separate. The macroscopic inactive-container branch remains separate.

Everything above is an analytic finite proof. No computation, verifier,
CI result, or numerical experiment is a premise.

# Target C-II: train terminals bound complete Horn implication basins

Date: 2026-10-05.
Authority: main 583203ac1dc1d7bc49f0ca0574d75e85f9de2ee1, state 2026-10-05.audit.62.
Status: proof-only Target C reduction; theorem state unchanged. C-II and Level I remain open.

## Scope

Work in the audit.61 acute binary O--O owner system after the bounded inactive
upper exceptions, relevant old-diameter requirements, unary rhombus tests, and
bounded-face isolate reassignment have been handled. Thus every remaining
inter-owner lower clause is an actual outer-face near-unit source pair.

Let \(Q\) be the reduced lower implication digraph and put
\[
X=b-q+Z_{\rm out}.
\]
Here \(b\) is the occurrence-counted outer contact-walk length, \(q\) is the
number of actual loaded vertices, and \(Z_{\rm out}\) is the number of
outer-face contact isolates. Let \(T_{\rm OO}\) be the number of selected
global stopped O--O trains inducing this owner system. It is a selected-family
count, not the canonical total-train variable used elsewhere.

## 1. Unloaded witnesses cost at most \(6X\)

The audit.61 displacement bound gives
\[
s<D-\sqrt{D^2-1}<1/11\qquad(D\ge6),
\]
so every surviving lower witness has old length \(<12/11\).

The source graph of pairs of length \(<12/11\) has maximum degree six. If one
source point had seven such neighbors, two consecutive neighbor rays would
make angle \(\theta\le2\pi/7\). With radii
\(r_1,r_2\in[1,12/11)\),
\[
|p_1-p_2|^2
=(r_1-r_2)^2+4r_1r_2\sin^2(\theta/2)
<
\frac1{121}
+4\left(\frac{12}{11}\right)^2\left(\frac{22}{49}\right)^2
=\frac{281185}{290521}<1,
\]
using \(\sin(\pi/7)<\pi/7<22/49\). This contradicts unit separation.

There are at most \(b-q\) distinct unloaded nonisolated outer-face vertices:
choose one outer occurrence for each of them together with the \(q\)
distinguished loaded occurrences. Bounded-face isolates have already been
reassigned. Hence every family \(\mathcal W\) of distinct surviving lower
witnesses satisfies
\[
\boxed{
\#\{e\in\mathcal W:e\text{ has an unloaded endpoint}\}\le6X.
}
\tag{1}
\]

## 2. Loaded owner runs cost O--O terminals

For a moving owner \(i\), let \(r_i\) be its number of maximal cyclic runs on
the distinguished loaded-hull occurrences.

Every owner change on the outer contact walk occurs on a selected train cut.
An old unit contact cannot join two distinct moving owners: preservation in all
four binary states would give the mixed difference
\[
-2\Delta_i\cdot\Delta_j=0,
\]
contradicting the acute condition. Thus a train-terminal occurrence can bound a
run of at most one moving owner.

The \(T_{\rm OO}\) selected trains supply exactly \(2T_{\rm OO}\) terminal
outer-walk occurrences, while every moving-owner outer run with nonempty
complement has two boundary occurrences. Restricting to the distinguished
loaded occurrences cannot increase run count. Therefore, for any family \(I\)
of moving owners having nonempty outer-walk complement,
\[
\boxed{\sum_{i\in I}r_i\le T_{\rm OO}.}
\tag{2}
\]

## 3. Outgoing-implication packet lemma

Let \(A\) be any set of distinct moving owners and choose one outgoing reduced
lower implication
\[
i\to j(i),\qquad j(i)\ne i,
\]
for every \(i\in A\).

By the acute truth-table identity proved in
research/target_c_acute_horn_sink_obstruction_2026-10-05.md, one physical
two-owner lower pair has at most one irreducible role after unary
simplification. Thus distinct selected directed arcs have distinct physical
witnesses.

Partition the selected arcs by witness type. Let \(A_X\) contain tails whose
selected witness has an unloaded endpoint, and let \(A_B=A\setminus A_X\).
Equation (1) gives
\[
|A_X|\le6X.
\tag{3}
\]

For \(i\in A_B\), both endpoints of the selected witness are loaded. The target
belongs to a distinct owner and supplies a distinguished loaded outer
occurrence outside owner \(i\). Hence \(r_i\ge1\) and owner \(i\) has nonempty
outer-walk complement. Equation (2) gives
\[
|A_B|\le\sum_{i\in A_B}r_i\le T_{\rm OO}.
\tag{4}
\]
Therefore
\[
\boxed{|A|\le T_{\rm OO}+6X.}
\tag{5}
\]

The witness partition matters: the terminal charge is used only when both
witness endpoints are loaded. Every other selected arc is paid by (1).

## 4. Complete implication basins are paid

Let \(S\) be a nontrivial sink SCC of \(Q\). Let \(B(S)\) be the full set of
owners having a directed path into \(S\), including \(S\).

For every owner outside \(S\), choose one outgoing implication along a shortest
path toward \(S\). For every owner in \(S\), choose one internal outgoing
implication; strong connectivity and \(|S|\ge2\) guarantee one. Applying (5)
to all owners of \(B(S)\) gives
\[
\boxed{|B(S)|\le T_{\rm OO}+6X.}
\tag{6}
\]

This removes the previous loophole in which a small obstructed sink could have
an arbitrarily large uncharged incoming basin.

There is also a zero-only corollary. Suppose the residual lower formula has no
unary forced-zero owner and its only model is the all-zero assignment. Because
the original zero state is valid, its reduced clauses are directed
implications and binary incompatibilities. Every owner must have positive
outdegree in \(Q\): if owner \(i\) had outdegree zero, setting only \(x_i=1\)
would satisfy every implication and every incompatibility. Hence (5) applied
to all owners gives
\[
\boxed{k_{\rm bin}\le T_{\rm OO}+6X.}
\tag{7}
\]

## 5. Residual pinned path and fork certificates

Canonical C-DISJOINT-SWAP-2SAT and all-zero validity imply that the residual
lower formula is made of directed implications, incompatibilities, and unary
forced-zero clauses. For pinned true owners, take forward implication closure.
If the closure avoids every forced-zero or pinned-false owner and does not
contain both endpoints of an incompatibility, its indicator is a model.
Otherwise failure contains either a directed path to a forbidden owner or two
directed paths reaching an incompatibility pair.

For a simple residual lower path
\[
v_0\to v_1\to\cdots\to v_\ell,
\]
choose its outgoing arc at each nonterminal owner. Equation (5) gives
\[
\boxed{\ell\le T_{\rm OO}+6X.}
\tag{8}
\]
Thus its support has at most \(T_{\rm OO}+6X+1\) owners.

For the union of two simple residual lower paths ending at the distinct
endpoints of one incompatibility, every owner except the two endpoints has a
selected outgoing arc in the union. Hence
\[
\boxed{|V(\text{fork})|\le T_{\rm OO}+6X+2.}
\tag{9}
\]

These bounds apply only after the upper/active-diameter and unary-rhombus
obligations named in the scope have been handled.

## 6. Composition with loaded sink recurrence

Let \(t_L\) count binary sink SCCs for which the selected covering implication
packet and one internal incompatibility packet are all loaded-loaded, as in
research/target_c_loaded_sink_double_recurrence_2026-10-05.md.

Choose one outgoing implication for every owner of a zero-only binary system.
For each owner in one of these \(t_L\) sinks, use an arc from that sink's
loaded-loaded covering packet. Choose any outgoing implication for every other
owner. Partition the selected tails into \(A_X,A_B\) as in Section 3.

Equation (3) gives \(|A_X|\le6X\). Every owner in \(A_B\) spends at least one
loaded-hull run. Each of the \(t_L\) sinks lies entirely in \(A_B\), and the
double-recurrence theorem forces two additional runs at two distinct owners of
that sink. Sink owner sets are disjoint. Therefore
\[
|A_B|+2t_L
\le\sum_{i\in A_B}r_i
\le T_{\rm OO}.
\]
Since \(k_{\rm bin}=|A_X|+|A_B|\),
\[
\boxed{k_{\rm bin}+2t_L\le T_{\rm OO}+6X.}
\tag{10}
\]

If every selected outgoing witness is loaded-loaded and every sink packet is
loaded-only, then \(A_X=\varnothing\) and \(t_L=t\), so
\[
\boxed{k_{\rm bin}+2t\le T_{\rm OO}.}
\tag{11}
\]

This strictly extends the preceding sink-only terminal budget to the complete
incoming implication population.

## 7. Remaining Target C obligation

In this acute O--O scope, the binary implication population is now paid by the
two physical currencies
\[
T_{\rm OO}\quad\text{and}\quad b-q+Z_{\rm out}.
\]
A closing theorem must compare the beneficial owner population supplied by the
extraction with these currencies, or reduce them using the canonical audit.53
return/depletion identities. A large implication basin can survive only with a
comparably large selected O--O terminal bank or outer unloaded/isolate bank.

This note does not prove either bank sublinear in every full-core source.
Unary rhombus failures, the at-most-\(d_H\) inactive upper exceptions, and the
macroscopic inactive-container branch remain separate.

Everything above is an analytic finite proof. No computation, verifier, CI
output, or numerical experiment is a proof premise.

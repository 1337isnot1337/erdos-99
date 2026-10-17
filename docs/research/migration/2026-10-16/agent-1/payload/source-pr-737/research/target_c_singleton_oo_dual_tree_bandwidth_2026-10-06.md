# Target C-II: singleton O--O bridges bound full dual-tree clause range

Date: 2026-10-06.
Authority: main \`583203ac1dc1d7bc49f0ca0574d75e85f9de2ee1\`, state \`2026-10-05.audit.62\`.
Status: proof-only Target C reduction; C-II and Level I remain open.

Work in the audit.61 narrow-window O--O multishear scope used by
\`research/target_c_noncrossing_owner_region_budget_2026-10-06.md\`.
Write
\[
x_B=b-q,\qquad
m_B=\#\{\text{nonunit loaded-hull sides}\}.
\]
Canonical \`C-GOOD-HULL-SINGLETON-CHARGE\` includes the exact bad outer
terminal-occurrence capacity
\[
B_{\rm bad}=x_B+m_B,
\qquad m_B\le x_B.
\]

Let \(S_{\rm OO}^{(1)}\) be the number of selected singleton O--O trains.
A singleton O--O train is an outer-face contact bridge, so its two terminal
incidences are the two outer occurrences of that bridge. For \(q\ge3\), both
cannot be good distinguished loaded-hull occurrences: one physical hull side
has only one distinguished one-edge loaded-hull occurrence. Hence every
singleton O--O train has at least one bad outer occurrence.

Terminal occurrences belong to unique complete stopped trains. Choosing one
bad occurrence per selected singleton therefore injects the singleton O--O
family into the canonical bad-occurrence bank:
\[
\boxed{
S_{\rm OO}^{(1)}\le x_B+m_B\le2x_B.
}
\tag{1}
\]
This includes bad--bad singleton bridges, not only the good-hull singleton
subfamily.

The existing worker-branch dual-tree theorem proves that for \(D\ge20\) every
surviving lower-clause physical witness crosses at most fourteen selected
non-singleton O--O cuts. If \(s_0(x,y)\) is the number of singleton dual edges
on its ordinary complement-dual-tree path, then
\[
s_0(x,y)\le S_{\rm OO}^{(1)}.
\]
Therefore every surviving implication, incompatibility, or previously strict
unary lower witness satisfies
\[
\boxed{
\operatorname{dist}_{\mathscr D}(R_x,R_y)
\le14+x_B+m_B
\le14+2x_B.
}
\tag{2}
\]

Thus the zero-weight singleton-chain escape in the previous weighted
dual-tree bound is fully paid by canonical outer-occurrence excess. Along any
full-core subsequence with \(x_B=o(D)\), every individual remaining lower
clause has dual-tree range \(o(D)\).

This does not make the owner implication graph acyclic. A macroscopic forcing
certificate may concatenate many short clauses, and one owner may recur in
distant regions. The remaining narrow-window obstruction is therefore
concatenation/owner recurrence, to be combined with audit.62 loaded-hull
degree at most two and audit.53 loaded-return/depletion currency.

Unary rhombus tests, the at-most-\(d_H\) inactive upper exceptions, the
crossing-multishear branch, and the macroscopic inactive-container branch
remain separate.

Everything above is analytic. No computation, verifier, CI output, or
unexecuted verifier is a proof premise.

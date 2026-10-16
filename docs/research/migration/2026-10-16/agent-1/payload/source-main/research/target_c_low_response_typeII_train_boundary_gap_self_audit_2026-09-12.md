# Hostile self-audit — LRII-T local train-boundary gap

**Date:** 2026-09-12  
**Audited commit:** `782f3dd74d92aa7c91cd265dec4aef16ace19482`  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## Verdict

The LRII-T argument survives the local-face audit. The only point needing a sharper
justification is Lemma 3.1: after retaining the whole internal graph `C[I_*]` and only
two loaded attachments as leaves, deleting the other loaded vertices cannot create a
new bounded face. The correct reason is an outer-face argument, not merely the fact
that omitted loaded vertices lie outside the convex hull.

No change to the constant

\[
M_{tr}={2\pi+\sqrt{2\pi/\sqrt3}\over5}
\]

is required.

## 1. Retained graph and omitted loaded vertices

Let

\[
G'=C[I_*]\cup\{s,t\}
\]

with exactly one actual attachment edge from `s` and one from `t` into `I_*`, as in
LRII-T. Put

\[
K_*=\operatorname{conv}V(G').
\]

Every attachment vertex of `A_*` is an extreme vertex of

\[
P_*:=\operatorname{conv}(A_*).
\]

Harmonic trapping gives `I_* subset P_*`, while `s,t in A_*`. Hence

\[
K_*\subset P_*.
\]

If `a in A_*\setminus\{s,t\}`, then

\[
a\notin K_*.
\tag{1.1}
\]

Indeed `K_*` is the convex hull of points of `P_*` not including `a`; if `a` belonged
to that hull, it would cease to be an extreme point of `P_*`.

## 2. Omitted loaded-contact edges lie in the outer face of `G'`

Consider any contact segment `e=[a,u]` of the full induced harmonic graph with at
least one omitted loaded endpoint `a in A_*\setminus\{s,t\}`. The other endpoint may
be internal or loaded.

The straight-line contact graph is planar, so the relative interior of `e` is disjoint
from every edge of `G'` and from every vertex of `G'`. Since `a` lies outside `K_*`,
the segment starts in the unbounded component of the complement of `G'`.

Suppose some interior point of `e` entered a bounded face `F` of `G'`. To pass from the
unbounded face to `F`, the connected open segment would have to cross the boundary
walk of `F`, which consists entirely of edges and vertices of `G'`. Such a crossing is
forbidden by planarity. The only possible contact with `G'` is at a retained endpoint
of `e`; that does not place any relative-interior point of `e` inside a bounded face.
Therefore

\[
\boxed{
\operatorname{relint}(e)\subset\text{outer face of }G'.
}
\tag{2.1}
\]

The same argument applies to loaded-loaded contact segments whose endpoints are both
omitted, or one omitted and one of `s,t`.

Consequently, restoring all omitted loaded vertices and all omitted contact edges
subdivides only the outer face of `G'`. Equivalently, deleting them from the full
induced harmonic graph can merge faces only into the outer face. It cannot merge two
old bounded faces into a new bounded face.

## 3. Bounded faces of `G'` are original all-unloaded bounded faces

Every bounded face of `G'` is therefore already a bounded face of the full induced
harmonic graph on `I_* union A_*`. The two retained loaded vertices `s,t` have degree
one in `G'`, so their bridge edges occur only on the outer-face walk. Thus every
bounded face of `G'` has all boundary vertices in `I_*`.

Canonical Section 82 proves that every bounded face of the full induced harmonic graph
is convex and that every bounded degree-four face is a strict unit rhombus.
Therefore

\[
\boxed{
\text{bounded degree-four faces of }G'
=
\text{unloaded-only strict rhombi assigned to }I_*.
}
\tag{3.1}
\]

The reverse inclusion is immediate: an unloaded-only rhombus assigned to `I_*` uses
only internal vertices and internal contact edges, all of which are retained in `G'`;
its original empty interior remains empty.

This establishes the exact face identification required by LRII-T.

## 4. Recipient count is then valid

Let `R_*` be this collection of rhombi and `B_*` its train-boundary occurrence count.
The finite train theorem gives

\[
B_*\ge4\sqrt{R_*}.
\]

A boundary edge occurrence of `R_*` has on its other side either

1. the outer face of `G'`; or
2. a bounded face of `G'` that is not degree four.

By (3.1), the second possibility has degree at least five. If `f'` is the number of
such faces and

\[
Q'=\sum_F(\deg F-4),
\]

then `f'<=Q'` and

\[
B_*\le b'+4f'+Q'\le b'+5Q'.
\]

Thus the central LRII-T inequality

\[
4\sqrt{a/a_0}\le10\gamma-4p
\]

is unchanged.

## 5. Remaining audit points

The other potentially dangerous steps were rechecked against the canonical stack.

- `area(P_*)-A_{4,*}=o(D^2)` follows componentwise from canonical Section 83 because
  all local deficits are nonnegative and their total is `o(D^2)`.
- `A_{4,*}-a_0R_*=o(D^2)` follows from the canonical global Type-II rhombus excess
  and nonnegativity of each individual rhombus excess.
- The remaining-cell estimate retains the C40 `+2` term; summing its square produces
  only `O(D)` because `c_I=O(D)`.
- `gamma>=1` uses only `delta_*/D->1` and `r_*>=0`.
- The final optimization does not double-spend the ZK budget: `gamma+t<=mu`, with all
  other Eppstein slacks and `s_B` discarded only in the favorable direction.

## 6. Status

LRII-T remains a proof-only candidate with the audited conclusion

\[
\liminf\mu_D
\ge
{2\pi+\sqrt{2\pi/\sqrt3}\over5}
=1.6375621841\ldots
\]

under canonical Type II and `epsilon_D->0`.

The next useful task is not another lower-bound decimal. It is to search the canonical
loaded-hull, difference-body, diameter-graph, and aggregate-detour ledgers for an upper
tradeoff on this same renormalized currency. Any valid Type-II upper bound below the
constant above would close the low-response Type-II branch.

# Hostile audit — inactive diameter-vertex-cover repacking

**Date:** 2026-09-12  
**Reviewed:** `research/target_c_inactive_diameter_vertex_cover_repacking_2026-09-12.md`  
**Disposition:** **PASS with two binding wording/proof corrections below.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The main structural theorem is valid: if one protected inactive chamber can absorb its
assigned isolates plus a vertex cover of the complete actual diameter graph, deleting
that cover and repacking in the chamber gives a same-cardinality unit-separated source
of strict diameter below `D`.

Two local corrections are binding.

## 1. Bare odd-cycle edge case in the Woodall cover proof

The source writes

\[
{k\over 2k+1}L<L/2
\]

for the total number `L` of pendant leaves. This strict inequality is valid only for
`L>0`.

If `L=0`, the diameter graph is the bare odd cycle `C_{2k+1}` and its minimum vertex
cover has size exactly

\[
\tau(C_{2k+1})=k+1
=\left\lceil{2k+1\over2}\right\rceil.
\]

If `L>0`, the averaging proof in the source applies exactly as written. Among the
`2k+1` maximum cycle-independent sets of size `k`, the average pendant-leaf weight is

\[
{k\over2k+1}L<L/2.
\]

Hence one has integer weight at most `floor((L-1)/2)` when `L` is even and at most
`floor(L/2)` when `L` is odd, which gives a cover of size at most `ceil(q/2)`.

Thus the theorem

\[
\boxed{\tau(H)\le\lceil q/2\rceil}
\]

survives unchanged.

## 2. Final handoff must say a lower spare-capacity bound

The source's final sentence says that it suffices to prove a spare-capacity bound “of
at most `pi D/2+O(1)` slots.” The inequality direction in that prose is wrong.

The actual sufficient condition is the lower bound

\[
\operatorname{spare}(C)
=M_1(C)-z_C
\ge\tau(H),
\]

and the topology-free version is

\[
\boxed{
\operatorname{spare}(C)
\ge\left\lceil{q\over2}\right\rceil.
}
\]

Since `q<=pi D`, the number of extra protected slots one ever needs to prove is **at
most** `pi D/2+O(1)`; equivalently, a universal lower bound of `pi D/2+O(1)` spare
slots is more than sufficient. The source theorem statements (4.1)--(4.4) already have
the correct inequality directions; only the final prose sentence is reversed.

## 3. Other hostile checks

### Cardinality

`Z_C` and the diameter-cover set `U subset B` are disjoint because `Z_C` consists of
contact-isolated inactive source points while `B` is the loaded force-visible terminal
set. Exactly `z_C+|U|` old points are deleted and the same number are inserted.

### Complete removal of old diameter pairs

C65 identifies `H` with the complete actual diameter graph. Therefore every retained
old-old pair has distance strictly below `D` after deleting a vertex cover of `H`.
This would fail if `U` covered only one selected KKT diameter support; the source
correctly requires the complete C65 graph.

### New diameter pairs

`C_{-1} subset int C subset int F subset int K` for a genuine two-dimensional internal
inactive chamber. The strict interior lemma therefore makes every new-old and new-new
distance strictly below `D`.

### Unit separation across the chamber boundary

Every retained old source point lies outside `int C`. For `y in C_{-1}`, the segment
from `y` to any such retained point meets `partial C` after length greater than one, so
cross-boundary separation is strict.

### Triangle-freeness

No triangle-free condition on the competitor is needed because the conclusion is
`diam(A')<D(n)`, a direct contradiction to global diameter minimality. This is an
important advantage over the existing lexicographic one-extra-point exchange.

### Lattice averaging

For the unit triangular lattice of covolume `a_0`, averaging the indicator count of
`C_{-1}` over one translation fundamental domain gives mean
`area(C_{-1})/a_0`. Hence some translate contains at least the ceiling of that mean
when the mean is nonintegral, and at least the mean when it is integral. The displayed
bound

\[
M_1(C)\ge\left\lceil area(C_{-1})/a_0\right\rceil
\]

is valid.

## 4. Correct handoff

The internal macroscopic inactive-chamber branch is now reduced to the finite packing
statement

\[
\boxed{
M_1(C_*)-z_*
\ge\tau(H).
}
\]

Woodall guarantees

\[
\tau(H)\le\lceil q/2\rceil\le \pi D/2+O(1).
\]

Therefore one does **not** need a protected `k -> k+1` move that preserves the
triangle-free comparison class. It is enough to prove that collective repacking of the
macroscopic chamber creates linearly many spare protected slots, with coefficient
large enough for the diameter-graph vertex cover. Once that happens, all actual
diameter pairs can be deleted simultaneously and strict global diameter descent is
automatic.

**Verdict:** theorem valid with the two binding corrections above; proof-only, no
theorem-state promotion.
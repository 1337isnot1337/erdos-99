# Hostile audit — AG47 chain-cover atomic train gap

**Date:** 2026-09-14
**Target:** `research/target_c_atomic_gap_chain_cover_00047_2026-09-14.md`
**Base:** `d03ba81c`
**Disposition:** PASS at proof-only scope
**Theorem-state authority:** unchanged

## 1. Claim under audit

The target note replaces the phase-inversion Markov deletion in audited-working §168
by a minimum vertex cover of the inversion chain graph.  It claims that this changes
the total phase-pruning loss from `2p_0D` to at most `sqrt(2)p_0D`, and consequently
certifies

\[
x\sigma\ge2\sqrt{\Delta_2}+0.00047.
\]

The audit checks the chain-graph assertion, the cover size, worst-case shore imbalance,
the common-neighbor threshold, and the final opposite-corner loss.

## 2. Inversions really form a chain graph — PASS

For the two selected atom windows, choose lifts

\[
x_u=\alpha_u,
\qquad y_v=\beta_v-\pi/3.
\]

An actual strict-rhombus crossing has `y_v>x_u`.  Thus every pair with
`x_u>=y_v` is missing.  For fixed `u`, its inversion neighborhood is

\[
N_H(u)=\{v:y_v\le x_u\}.
\]

Ordering the `u` by increasing `x_u` makes these neighborhoods nested.  This is exactly
a bipartite chain graph, including ties.  Deleting a vertex cover eliminates every
inversion and therefore leaves strict phase order `x_u<y_v` for every remaining pair,
not merely for actual crossing pairs.

## 3. Sparse-chain cover constant — PASS

Let the inversion graph have `m` edges and maximum matching size `nu`.  Choose the
matched vertices on one shore in increasing nested-neighborhood order

\[
N(a_1)\subseteq\cdots\subseteq N(a_\nu).
\]

Their matched opposite vertices are distinct.  For every `i`, the first `i` matched
opposite vertices all belong to `N(a_i)`, so `deg(a_i)>=i`.  Hence

\[
m\ge1+2+\cdots+\nu={\nu(\nu+1)\over2}.
\]

König gives a vertex cover of size `nu`, and therefore

\[
\tau(H)=\nu<\sqrt{2m}.
\]

Audited §168 supplies at most `(2d_0+o(1))D^2` missing cross-shore pairs after the
majority assignment.  Since every inversion is missing,

\[
m\le(2d_0+o(1))D^2.
\]

Thus a phase cover deletes in total at most

\[
(2\sqrt{d_0}+o(1))D
=(\sqrt2\,p_0+o(1))D,
\qquad p_0=\sqrt{2d_0}.
\]

This is the claimed constant.  No assumption about how the cover splits between the
two shores is used.

## 4. Worst-case shore loss and common neighbors — PASS

Before phase deletion, the selected opposite-shore atom families have normalized sizes
at least

\[
S_0,\qquad S_0/2.
\]

The entire chain cover could lie on the smaller shore.  After the cover and the later
Markov degree pruning, the smaller shore is therefore still at least

\[
{S_0\over2}-(\sqrt2+1)p_0-o(1).
\]

Every retained vertex misses at most `p_0D+o(D)` vertices of the opposite shore.  Thus
any three vertices on the large shore have a common neighbor on the small shore if

\[
{S_0\over2}-(\sqrt2+1)p_0-3p_0>0,
\]

i.e.

\[
{S_0\over2}>(4+\sqrt2)p_0.
\]

The exact interval certificate proves the stronger margin

\[
{S_0\over2}-(4+\sqrt2)p_0>0.27749.
\]

The reverse common-neighbor requirement is easier because the other shore begins with
mass `S_0`.  Hence the §163 pair/triple common-neighbor globalization remains valid.

## 5. Final path loss — PASS

The initial selected total mass is at least `3S_0/2`.  The losses are:

1. chain-cover phase deletion: at most `sqrt(2)p_0` total;
2. degree-pruning deletion: at most `p_0` from each shore, hence `2p_0` total;
3. at the chosen opposite corner, the two endpoint trains each miss at most `p_0D`
   retained opposite trains, hence another `2p_0` in the degree sum.

Therefore the corner degree sum is bounded below by

\[
{3S_0\over2}-(4+\sqrt2)p_0-o(1),
\]

exactly as claimed.  There is no omitted second phase-pruning loss; the vertex cover is
one joint deletion across both shores.

The inherited §163/§168 positive-projection argument then gives

\[
1\ge{\sqrt3\over2}
\left[{3S_0\over2}-(4+\sqrt2)p_0\right]-o(1).
\]

For `eta=0.00047`, the exact interval script proves the right side is greater than
`1.00162`, contradiction.

## 6. Scope and failure modes checked

- **Ties:** inversion uses `x_u>=y_v`; deleting a vertex cover leaves strict `<`.
- **Cover imbalance:** all cover vertices may lie on one shore; the threshold check
  explicitly pays that worst case.
- **Non-inversion missing pairs:** they remain in the degree-pruning missing budget;
  the proof never assumes the chain cover removes all missing pairs.
- **Repeated/bridge trains:** §168's selected atom train graph already uses the complete
  stopped-train conventions; the chain argument sees only train vertices and does not
  change occurrence accounting.
- **Common-neighbor globalization:** the small-shore triple margin remains positive by
  more than `0.277D`, far above rounding or `o(D)` losses.
- **Numerical ceiling:** the same architecture loses its path contradiction near
  `eta=0.0004764914`; `0.00047` is safely below that root.

## 7. Disposition

PASS at proof-only scope.  AG47 is a genuine strengthening of the current atomic train
gap using a combinatorial property already present in the endpoint proof.  It does not
close C-II.

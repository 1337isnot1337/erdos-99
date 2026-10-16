# Target C-II: outer-train terminal occurrences pay loaded sink recurrence

Date: 2026-10-05.
Authority checked: current main 583203ac1dc1d7bc49f0ca0574d75e85f9de2ee1, state 2026-10-05.audit.62.
Status: proof-only Target C reduction; theorem state unchanged. C-II and Level I remain open.

## 1. Target and scope

The preceding sink analysis leaves one geometric currency unpaid: a loaded-only
binary sink SCC needs two distinct owners that each recur in separate cyclic
loaded-hull runs.

This note pays that recurrence directly by actual terminal occurrences of the
selected global stopped outer-to-outer trains.

Work in the explicit audit.61 acute binary O-O owner scope. The positive
contact core is connected. Let tau_1,...,tau_T be the actual selected global
stopped O-O trains. Each tau_j is an actual contact cut and has exactly two
terminal contact-edge occurrences on the occurrence-counted outer contact-face
walk. The selected cuts induce the layer/slab owner partition on the core, so
ownership is constant on each component after the selected train cut edges are
deleted. Every binary owner selection preserves every old unit contact, and
distinct nonzero owner translations are mutually acute.

The conclusion is only for this actual binary cut-induced owner system. It is
not asserted for an arbitrary later contraction of source vertices to labels.

## 2. Moving-owner outer runs consume train-terminal occurrences

Let W be the cyclic occurrence-counted outer contact-face boundary walk. For a
moving owner i, let r_out(i) be the number of maximal cyclic runs of outer-walk
vertex occurrences carrying owner i.

Every boundary between a moving-owner run and its complement is an occurrence
of a selected train edge. If an outer contact edge is not in any selected train
cut, its endpoints lie in the same component after the selected cut edges are
deleted, hence have the same layer/slab owner. Therefore an owner change across
an outer contact edge can occur only on a selected cut edge.

The acute binary hypotheses sharpen this. An old unit contact cannot join two
distinct moving owners. If its old vector is r and the owner translations are
Delta_i and Delta_j, preservation of that contact in all four binary states
gives the exact mixed squared-norm identity

    |r + Delta_i - Delta_j|^2 - |r + Delta_i|^2
      - |r - Delta_j|^2 + |r|^2
    = -2 Delta_i dot Delta_j
    = 0.

This contradicts Delta_i dot Delta_j > 0. Thus an outer owner-boundary
occurrence has exactly one moving-owner side. In particular one train-terminal
occurrence cannot simultaneously bound runs of two distinct moving owners.

Now let I be any family of moving owners such that each i in I has a nonempty
complement on W. Every cyclic run of such an owner has two boundary
occurrences. A singleton bridge causes no exception: its physical edge occurs
twice on the outer facial walk.

Each selected global O-O train has exactly two terminal outer-face edge
occurrences. Its interior train edges have strict rhombi on both sides and do
not occur on the outer face. Therefore the T selected trains supply exactly 2T
available train-terminal occurrences. The run-boundary incidences for owners
in I inject into these occurrences, so

    2 sum_{i in I} r_out(i) <= 2T,

hence

    sum_{i in I} r_out(i) <= T.                      (1)

This is an occurrence statement. It does not identify one train with one
owner, and it permits a singleton physical bridge to contribute its two
oriented outer-walk occurrences.

## 3. Loaded-hull runs inherit the same budget

Let B be the actual loaded force-hull vertex set. Loaded vertices are extreme
source vertices, hence appear on the outer contact face in their cyclic
convex-hull order. Choose one distinguished outer occurrence of each loaded
vertex in that order.

For a moving owner i, let r(i) be the number of maximal cyclic runs of
loaded-hull vertices carrying i, as in the preceding sink notes.

Restricting the outer walk to the distinguished loaded occurrences cannot
create two loaded runs of i from one outer run of i. Inside one outer run every
retained loaded occurrence has the same owner. Conversely, two different
loaded runs of i are separated in loaded-hull order by a loaded vertex of
another owner, and therefore come from distinct outer runs. Thus

    r(i) <= r_out(i).

For every family I covered by Section 2,

    sum_{i in I} r(i) <= T.                          (2)

## 4. Loaded-only sink SCCs consume more runs than owners

Let S be a binary-only sink SCC in the acute prime lower system.

Choose an irreducible implication packet covering every owner of S, plus one
internal incompatibility witness. At the two endpoints of that
incompatibility also choose one incoming and one outgoing implication witness,
as in the preceding double-recurrence note. Call S loaded-only when every
physical witness in this combined selected packet is loaded-loaded. If any
selected witness has an unloaded endpoint, call the sink unloaded-paid.

For a loaded-only sink, the covering implication packet gives every owner at
least one loaded-hull occurrence:

    r(i) >= 1 for every i in S.

The double-recurrence theorem gives two distinct owners a,b in S, namely the
endpoints of the internal incompatibility, with

    r(a) >= 2 and r(b) >= 2.

Therefore, writing R(S) = sum_{i in S} r(i),

    R(S) >= |S| + 2.                                 (3)

Now let S_1,...,S_t be pairwise disjoint loaded-only sink SCCs and put

    M = sum_c |S_c|.

Every owner in their union has a loaded vertex, and every sink has at least two
owners. Hence each such owner has a nonempty complement on W, so Section 2
applies to the union of their owner sets. Equations (2) and (3) give

    M + 2t <= T.                                     (4)

Since every binary-only sink has at least two owners,

    t <= floor(T/4).                                 (5)

For one loaded-only sink of size s,

    T >= s + 2.                                      (6)

In particular the minimal two-owner obstruction

    A -> B,  B -> A,  and incompatibility(A,B)

cannot occur in this loaded-only O-O system unless at least four selected
global O-O trains are present.

## 5. Combined sink count including unloaded witnesses

The companion unloaded-witness note proves that every family of distinct
surviving lower witnesses with an unloaded endpoint has size at most

    6 (b - q + Z_out),

where b is the occurrence-counted outer contact-walk length, q = |B|, and
Z_out is the number of contact isolates in the outer face.

For pairwise disjoint binary sink SCCs, every unloaded-paid sink contributes
at least one such selected physical witness. Selected internal witness packets
from different sink SCCs are physically distinct. Hence the number of
unloaded-paid sinks is at most 6(b-q+Z_out). Equation (5) bounds the
loaded-only sinks. Thus

    t_all <= 6 (b - q + Z_out) + floor(T/4).         (7)

More strongly, the loaded-only part satisfies the owner-sensitive budget (4),
not just the scalar count (5).

## 6. What remains open

This removes the previously uncharged repeated-loaded-owner quantity from the
binary-sink ledger in the actual acute O-O cut-induced scope. Repeated loaded
owners now spend an explicit source resource: terminal occurrences of selected
global O-O trains.

It does not prove satisfiability. A zero-only Horn system may concentrate the
obstruction in one sink SCC and attach many upstream owners to that sink.
Equation (6) controls the sink's own size but does not charge the full
implication basin feeding it.

The next Target C owner-order theorem should extend terminal-occurrence
accounting from the sink SCC to its incoming implication arborescence, or show
that enough upstream owners force additional unloaded-endpoint witnesses.
Unary rhombus blockers and the at-most-d_H inactive upper exceptions remain
separate. The macroscopic-container branch is untouched.

Everything above is an analytic finite proof. No computation, verifier,
numerical experiment, CI output, or unexecuted verifier is a proof premise.

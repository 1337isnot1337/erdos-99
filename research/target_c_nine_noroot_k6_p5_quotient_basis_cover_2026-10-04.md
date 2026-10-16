<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "4aecbbac2eb71c36fc5eaa72d5bda50197fa85ae", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_nine_noroot_k6_p5_quotient_basis_cover_2026-10-04.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "9a753ffe1d8aac7890bc5210f0053ab27b86315f1cac117f85621e36bf0b2347"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: k=6 p=5 quotient-basis cover

Date: 2026-10-04
Base dependency: `research/target_c_nine_noroot_k6_p5_triple_sync_2026-10-04.md`
Status: proof-only structural reduction for the nine-no-root `k=6,D=-1,d_root=1,p=5` branch. No computation is used. C-II and Level I remain open.

## Setup

Let `B` be a surviving nine-no-root state with

```
k=6, D=-1, d_root=1, p=5,
rank(P)=3,
(d1,d2,d3)(P)>=(2,4,5).
```

The preceding deletion work gives, for every deleted coordinate set `S`,

`D(B-S)=-1+2|S|-3q_S`,

where `q_S` is the rank loss of the coefficient space under puncturing. All nine no-root rows are M-independent modulo the selected root rows.

Choose six coordinate classes
`e_i+P`, `i in U`,
forming a basis of `Q^9/P`, and let

`V=[9]\U`.

Thus `|U|=6` and `|V|=3`.

For every `S subset U`, the quotient-basis property implies

`P cap Q^S = 0`,

so puncturing `S` preserves `rank(P)=3`, i.e. `q_S=0`.

For such an `S`, the punctured state has
`t_S=9-|S|` and `k_S=6-|S|`. Writing `p_S,d_S`
for its stripped incomplete-root cost and root deficiency, the exact root formula gives

`D(B-S)=t_S+p_S+3d_S-3k_S`.

Comparing with `D(B-S)=-1+2|S|` yields

`p_S+3d_S=8`.                                               (1)

Since puncturing cannot increase incomplete-root cost, `0<=p_S<=5`.
Hence every rank-preserving puncture inside `U` has

`p_S in {5,2}`.                                               (2)

## The quotient-basis cover theorem

> Every selected incomplete root block is touched by at least one of the three
> no-root cycles indexed by `V`.

Assume otherwise. Among selected incomplete blocks whose complete no-root touch
support lies in `U`, choose one with inclusion-minimal touch support `S`.

Deleting `S` makes this block untouched, so `p_S<5`. By (2),

`p_S=2`,

and therefore exactly three units of selected incomplete-root cost disappear.

Every selected block lost by this deletion has touch support contained in `S`.
By minimality of `S`, every such lost block has exact touch support `S`.
Since one incomplete block contributes cost one or two, a lost cost of three
contains at least two distinct root blocks and at least one singleton block.

The one-coordinate synchronization already proves that every selected incomplete
block is touched by at least two no-root cycles, so `|S|>=2`.

Take two distinct lost root blocks. They are two distinct triangular faces.
Every no-root cycle in `S` touches both. The local four-cycle geometry used in
the depth-two synchronization then forces every cycle in `S` to be an
orientation of the same tetrahedral four-set, namely the union of those two
triangles. There are only three no-root four-cycle orientations on that
four-set, so `|S|<=3`.

At the lost singleton block, any two of those distinct orientations have
different local projective directions. Therefore the singleton local
coefficient constraint is nonzero and is supported inside `S`.
That nonzero constraint lies in `P`.

But `S subset U`, while the coordinate classes indexed by `U` are
independent modulo `P). Equivalently, `P` contains no nonzero vector
supported inside `U`. Contradiction.

Therefore every selected incomplete root block meets `V`.

## Pair-block activation

The cover theorem has a useful linear-algebra reformulation.

Because `U` is a quotient basis, restriction

`P -> Q^V`

is injective. Both spaces have dimension three, so it is an isomorphism.
Equivalently, the three columns indexed by `V` form a column basis of any
rank-three generator matrix for `P`.

Let `b` be any selected incomplete root block and let `T_b` be its full
nine-coordinate touch support. The cover theorem holds for every quotient basis
`U`, not only the one fixed above. Therefore `T_b` meets the complement of
every quotient basis.

If the columns of `P` outside `T_b` had rank three, they would contain a
three-column basis `V'`; its complement `U'` would be a quotient basis
disjoint from `T_b`, contradicting the theorem. Hence

`rank(P|_[9]\T_b) <= 2`.

Thus there exists a nonzero word

`w_b in P`

whose support is contained in `T_b`.

This is automatic for singleton blocks from their local coefficient line, but
it is new for selected pair blocks, which contribute no local coefficient
constraint themselves:

> every selected pair block nevertheless has touch support containing the
> support of a nonzero global coefficient word.

In particular every selected incomplete block contains a coefficient support
of size at least `d1(P)>=2`.

## Singleton-basis transversal

The existing generator reduction leaves only the two p=5 root profiles

```
(3 singleton blocks, 1 pair block),
(5 singleton blocks, 0 pair blocks).
```

In either profile choose three singleton coefficient lines
`ell_1,ell_2,ell_3` forming a basis of `P`.

Since restriction `P -> Q^V` is an isomorphism, the three restricted rows
`ell_i|_V` are linearly independent. Therefore the 3 by 3 coefficient matrix
on these singleton lines and the three coordinates in `V` has nonzero
determinant.

Consequently its nonzero-entry bipartite graph has a perfect matching.
After relabeling the three cycles in `V`, there are distinct
`v_1,v_2,v_3 in V` such that

`ell_i(v_i) != 0`

for `i=1,2,3`.

A nonzero singleton coefficient at coordinate `v_i` requires that cycle
`v_i` touch the corresponding singleton root block. Hence every quotient-basis
complement contains three distinct no-root cycles that can be matched to the
three singleton basis blocks. In the `(3,1)` profile the pair block is also
touched by at least one of those three cycles.

## Consequence for the finite target

The previous triple-shadow theorem required at least nineteen six-no-root
`(k,D,d_root,p)=(3,5,1,5)` shadows. The present theorem gives a stronger
nine-row structural filter before any six-row classification:

1. choose any six-coordinate quotient basis `U`;
2. the complementary three no-root cycles `V` must cover every selected
   incomplete root block;
3. every selected pair block touch support must contain a nonzero word of
   the global rank-three coefficient space;
4. for every singleton basis of `P`, the three singleton blocks admit a
   distinct representative matching into the three cycles of `V`.

Thus a future exact search need not consider arbitrary placements of the p=5
incomplete blocks. It may first enumerate rank-three coefficient spaces and
three-coordinate column bases `V`, then require all selected incomplete blocks
to lie in the union of the twelve triangle incidences of those three cycles and
apply the singleton-basis matching test before relation-rank work.

This note does not claim closure of the p=5 branch, the nine-no-root k=6 layer,
C-II, or Level I.

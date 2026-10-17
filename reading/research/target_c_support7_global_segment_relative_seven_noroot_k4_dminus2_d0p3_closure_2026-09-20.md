> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_seven_noroot_k4_dminus2_d0p3_closure_2026-09-20.md) · source SHA-256 `7d61b8a22edeb21d6b08a550e048695608067c392acc2a9c0646bc9636ab2651`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "d4f5366ecbecc5664414283bdd941f6333797d7c", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_seven_noroot_k4_dminus2_d0p3_closure_2026-09-20.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "fb493f5be0160e51bec8033edc4d49fdbd66ccaf46de36f82a95a80b7c9f0290"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: close the seven-no-root `D=-2,k=4,d=0,p=3` branch

Date: 2026-09-20

Status: exact closure of the remaining `D=-2,k=4` seven-no-root branch. Together with the previously closed `D=-2,k=4,d=1,p=0` branch, this closes all `D=-2,k=4` arithmetic cases. It does not close the full seven-no-root layer or C-II.

Companion exact verifier:

`research/verify_target_c_support7_global_segment_relative_seven_noroot_k4_dminus2_d0p3_closure_2026_09_20.py`

## 1. Inputs already proved

Suppose a seven-no-root counterexample existed with

`D=-2, k=4, d=0, p=3`.

The preceding deletion and sharp-shadow results give all of the following.

1. The global coefficient-constraint space `P <= Q^7` has rank three.
2. Its generalized Hamming weights satisfy

   `(d_1,d_2,d_3) >= (3,4,6)`.
3. The root state contains exactly three incomplete singleton blocks and no pair block.
4. Every one of those singleton blocks is touched by at least three of the seven no-root cycles.
5. For a singleton block `b`, if `L_b <= E_b <= Q^7` are its singleton and empty local coefficient spaces, then

   `L_b subset P`,

   `E_b not subset P`,

   and `(E_b+P)/P` is one-dimensional.
6. More strongly, the nonzero quotient coset `(E_b+P)/P` has Hamming distance at least three from `P`, because every two-coordinate puncture is a sharp five-row `D=2,k=2,p=3` shadow.

The goal is to show that no three singleton blocks can coexist with a rank-three `P` satisfying these conditions.

## 2. Local three-direction geometry

Fix a root block `b`, corresponding to a three-subset of `{1,...,7}`. Exactly twelve no-root four-cycles touch `b`. Their nonzero local quotient components lie on exactly the three projective directions

`(1,0), (0,1), (1,-1)`,

with exactly four cycles on each direction.

For two distinct root blocks `a,b`, a no-root cycle touches both exactly when the two three-subsets share two vertices. In that case their union is a four-set `U`; exactly the three no-root four-cycle orientations on `U` touch both blocks. At either block those three orientations give the three different projective local directions, one each.

The companion verifier checks these statements directly from the exact quotient coordinates for all 35 blocks and all block pairs.

## 3. A sharp singleton is either aligned rank one or has at least five touches

Let `b` be one of the three singleton blocks. Let `S_b` be its set of touching no-root rows and put

`t=|S_b|`.

For the three local projective directions, write their multiplicities among `S_b` as

`m_0,m_1,m_2`,

so `m_0+m_1+m_2=t` and each `m_i<=4`.

### Rank-one local empty space

If `rank E_b=1`, then `E_b` is one projective local direction. Since

`L_b subset P`

but

`E_b not subset P`,

we must have

`L_b=0`.

For a singleton row, `L_b=0` exactly when every touching local component is parallel to the selected root-row direction. Thus all cycles in `S_b` lie on one local projective direction. There are only four such cycles globally, while the sharp-shadow theorem already gives `t>=3`. Therefore

`t in {3,4}`.

Call such a singleton **aligned**.

### Rank-two local empty space

Now suppose `rank E_b=2`. Then `L_b` is a nonzero line in `P` and `E_b intersect P=L_b`.

Let `s` be the selected singleton direction. The coefficient row spanning `L_b` vanishes exactly on touching cycles whose local component is parallel to `s`. Hence

`wt(L_b)=t-m_s`.

The bound `d_1(P)>=3` gives

`t-m_s >= 3`.

For either of the other two projective directions `j`, choose the linear functional on the local two-space that vanishes on direction `j`. Its coefficient row `w_j` belongs to `E_b` but is not in `L_b`, so it represents the nonzero quotient line `(E_b+P)/P`. Its support has size

`t-m_j`.

The established quotient-coset distance at least three implies, in particular by taking the zero vector of `P`,

`t-m_j >= 3`.

Thus every direction multiplicity satisfies

`m_i <= t-3`.

Consequently a rank-two singleton has

`t>=5`.

At the extremal value `t=5`, its direction profile is necessarily a permutation of

`(2,2,1)`.

The companion verifier checks this finite multiplicity arithmetic.

## 4. Two rank-two singleton blocks are impossible

Suppose two singleton blocks `b_1,b_2` had rank-two local empty spaces. Their touch sets both have size at least five inside the same seven-cycle set, so

`|S_1 intersect S_2| >= |S_1|+|S_2|-7 >= 3`.

Distinct root blocks have at most three common touching no-root cycles. Hence equality holds throughout:

`|S_1|=|S_2|=5`,

`|S_1 intersect S_2|=3`,

`S_1 union S_2=E`,

where `E` is the full seven-cycle set. In particular the two root triples share two vertices, and `S_1 intersect S_2` is the complete three-orientation family on their common four-set.

Consider the third singleton block `c`.

If `c` is aligned rank one, it cannot obtain three aligned touches from only one of `S_1,S_2`: among the three cycles that can touch `c` together with one fixed block, the local directions at `c` are all different. Therefore `c` must share two vertices with both `b_1` and `b_2`.

There are only two geometries for three distinct triples pairwise sharing two vertices.

1. They are three faces of one four-set. Then the three cycles in `S_1 intersect S_2` touch `c` in all three local directions, contradicting alignment.
2. They share one common two-set and have three different third vertices. The three cycles in `S_1 intersect S_2` do not touch `c`. The only possible touches of `c` are the two `S_1`-exclusive cycles and the two `S_2`-exclusive cycles. Within either exclusive pair, at most one cycle can use the fixed aligned direction at `c`. Thus `c` has at most two aligned touches, contradicting `|S_c|>=3`.

If instead `c` is rank two, then `|S_c|>=5`, so again it must share two vertices with both `b_1,b_2`. In the three-faces-of-one-four-set geometry, the four cycles outside `S_1 intersect S_2` cannot touch `c`, because any cycle touching `c` and either `b_i` is one of the same three orientations of that four-set. Hence `|S_c|=3`, impossible. In the common-two-set geometry, `c` is touched only by the four cycles exclusive to `S_1` or `S_2`, so `|S_c|<=4`, again impossible.

Therefore at most one singleton block can have rank-two local empty space.

## 5. Exactly one rank-two singleton block is impossible

Assume `b` is rank two and the other two singleton blocks `a,c` are aligned rank one.

For an aligned block `a`, the intersection `S_a intersect S_b` has size at most one. If the root triples fail to share two vertices the intersection is empty; if they share two vertices, the three common orientations have three distinct local directions at `a`, while `S_a` uses only one direction.

Since `|S_a|>=3` and the full external set has seven cycles,

`3 <= |S_a intersect S_b| + |E \ S_b| <= 1 + (7-|S_b|)`.

The rank-two bound gives `|S_b|>=5`, so equality is forced:

`|S_b|=5`,

`|S_a|=3`,

`|S_a intersect S_b|=1`,

and both cycles in `E\S_b` belong to `S_a`.

The same argument applies to `c`. Hence the same two cycles outside `S_b` touch both aligned singleton blocks `a` and `c`.

Two distinct no-root cycles can touch two distinct root blocks simultaneously only when those blocks share two vertices; then the cycles are two of the three orientations on their common four-set. At either block those orientations have different local projective directions. But both cycles belong to the aligned touch set `S_a`, contradiction.

Thus no singleton block can be rank two.

## 6. All three singleton blocks are aligned rank one

Every singleton block is therefore aligned, with exactly three or four touching no-root cycles, all in one local projective direction. In particular

`L_b=0`

for all three singleton blocks.

The singleton blocks contribute no nonzero coefficient constraints. Every other incomplete root block has cost zero and is therefore empty; complete blocks also contribute no coefficient constraint. It follows that the global rank-three space `P` is generated entirely by empty-block constraint spaces from touched blocks other than the three singleton blocks.

This converts the rest of the proof into a small exact finite search.

## 7. Only three block-triple geometries remain

Two aligned singleton touch sets intersect in at most one cycle. Three touch sets of size at least three contribute at least nine touch incidences among only seven external cycles, so at least two pairs of singleton blocks must have nonempty touch-set intersection. Such an intersection requires the corresponding root triples to share two vertices.

There are exactly ten `S_7`-orbits of unordered triples of the 35 root blocks. Only three have at least two block pairs with two-vertex intersection. Canonical representatives are

```text
(123,124,125)   pair intersections (2,2,2)
(123,124,134)   pair intersections (2,2,2)
(123,124,135)   pair intersections (2,2,1)
```

The verifier derives all ten orbits directly from the `S_7` action; these three are not supplied as an assumed classification.

For each of these representatives it enumerates every aligned singleton touch set of size three or four, takes unions of size at most seven, and fills any unused external coordinates only with cycles touching none of the singleton blocks. It then checks that the induced touch set at each singleton is exactly the selected aligned set.

The resulting exact seven-cycle configuration counts are

```text
singleton-block orbit      configurations
(123,124,125)                    654
(123,124,134)                     81
(123,124,135)                     54
------------------------------------
total                            789
```

This is already a reduction from `C(105,7)=22,760,723,700` raw seven-cycle sets.

## 8. Exact coefficient-space exhaustion

Fix one of the 789 configurations. For every touched non-singleton root block `b`, compute its exact local empty constraint space `E_b <= Q^7`.

An actual root state may make such a block empty or complete. Therefore every possible global coefficient space is obtained by selecting some of these local empty spaces and taking their span. The verifier performs that subset-span dynamic program, retaining only spans of dimension at most three and finally only rank-three spaces.

The exact counts are

```text
singleton-block orbit      rank-3 coefficient candidates
(123,124,125)                         34,986
(123,124,134)                          3,996
(123,124,135)                          2,406
---------------------------------------------
total                                 41,388
```

For every rank-three candidate `P`, the verifier tests the already-proved generalized-weight conditions by exact rational puncturing:

- deleting any two coordinates must leave rank 3 (`d_1>=3`);
- deleting any three coordinates must leave rank at least 2 (`d_2>=4`);
- deleting any five coordinates must leave rank at least 1 (`d_3>=6`).

The number of survivors is

`0`.

All row reduction in this stage uses `fractions.Fraction`. No modular-rank assumption or probabilistic computation enters this final certificate.

Therefore no seven-no-root state with

`D=-2, k=4, d=0, p=3`

exists.

## 9. Consequence

The other arithmetic case with `D=-2,k=4`, namely

`d=1,p=0`,

was closed previously. Hence

> there is no seven-no-root counterexample with `D=-2,k=4`.

This does not close all seven-no-root boundary tuples. The next small open branch remains the synchronized

`D=-1, k=3, d=0, p=1`

case, whose every pair-deletion shadow has `D=3,k=1,d=0,p=1`. The higher-`k` seven-no-root arithmetic cases also remain unless eliminated by a separate committed argument.

The direct C-II endpoint remains unchanged:

`3874 = 3076 C7 + 798 (C3 disjoint-union C4)`.

No theorem-state authority file is changed by this note.

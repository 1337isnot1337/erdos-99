> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_seven_noroot_k5_small_branches_2026-09-20.md) · source SHA-256 `a1163172d329f8e685d3910e528d9e7172a1196d80ae49cf05fac9dddf3e71c0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "6a1e75dc80c4f0fd4f6f15463d4cdd771686a7d1", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_seven_noroot_k5_small_branches_2026-09-20.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "60414ab5e4c90b7a018d632d8f1bcc06a8d20439e58c74f8a5bb099ab2c615bb"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: seven-no-root `k=5` small-branch closures

Date: 2026-09-20

Status: exact closure of three seven-no-root `k=5` arithmetic branches:

- `D=-2, d=2, p=0`;
- `D=-2, d=1, p=3`;
- `D=-1, d=2, p=1`.

After this result, the open `k=5` boundary cases are only

- `D=-2, d=0, p=6`;
- `D=-1, d=1, p=4`;
- `D=-1, d=0, p=7`.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_seven_noroot_k5_small_branches_2026_09_20.py`

## Inputs

Let `B` be a hypothetical seven-no-root counterexample. The previously proved seven-row deletion theorem gives `D(B) in {-2,-1}` and makes every no-root row an `M`-coloop and a `Q`-noncoloop. The exact boundary identity is

`D = 7 + p + 3d - 3k`.

If `D=-2`, every two-row deletion is synchronized: deleting any pair of no-root rows keeps the same external quotient rank and produces a five-no-root shadow with

`D=2`, `k_shadow=k-2`.

The all-depth theorem also gives the generalized Hamming weights of the seven-coordinate coefficient space `P`. For `k=5`, `rank(P)=2`; in the `D=-2` case,

`(d_1(P),d_2(P)) >= (3,4)`,

while in the `D=-1` case `d_1(P)>=2`.

The other input is the coverage-correct five-no-root `k=3,p<=3` containment theorem. For a five-row state with rank-two coefficient space `P`, let `C` be its virtual canonical complete-block set, let

`d_v = |C| - rank H(C)`,

and let `q` be the number of virtual-canonical complete blocks replaced by incomplete blocks in the actual state. The theorem proves

`d_v>=1`, `q<=p`,

and

`D >= 5 + p + 3d_v - 3q`.

## 1. Close `D=-2,k=5,d=2,p=0`

Delete any two no-root rows. Depth-two synchronization produces a five-row state with

`D=2, k=3, p=0`.

But the five-row containment theorem has `q=0` when `p=0`, so

`D >= 5 + 0 + 3*1 = 8`.

This contradicts `D=2`. Therefore no seven-no-root `D=-2,k=5,d=2,p=0` state exists.

## 2. Equality structure in `D=-2,k=5,d=1,p=3`

Suppose

`D=-2, k=5, d=1, p=3`.

Every pair deletion is a five-row `D=2,k=3,p=3` state. Apply the five-row containment bound:

`2 >= 5+3+3d_v-3q`,

with `d_v>=1` and `q<=3`. The only possible equality case is

`d_v=1, q=3`.

Therefore this equality holds in every one of the 21 pair-deletion shadows.

Since total incomplete-root cost is only `p=3`, replacing three virtual-canonical complete blocks forces exactly three incomplete blocks, each containing one selected root row. Thus the seven-row root state has exactly three singleton incomplete blocks and no pair block.

Moreover each singleton block is virtual-canonical-complete after every pair deletion. If `E_b` is its empty local coefficient space and `P_J` is the projected coefficient space after deleting coordinate pair `J`, then

`E_b^J not subset P_J`

for every pair `J`. In particular the singleton remains touched after every pair deletion, so it is touched by at least three of the seven no-root cycles.

Let `L_b` be its singleton local constraint. The actual singleton state gives `L_b subset P`, while pair-puncture exclusion gives `E_b not subset P`. If `rank E_b=2`, then `E_b intersect P=L_b`, so `(E_b+P)/P` is a nonzero quotient line. The condition for all pair punctures says this quotient coset has Hamming distance at least three from `P`.

## 3. The three singleton blocks are aligned

The local argument proved in the preceding `D=-2,k=4,d=0,p=3` closure uses only `d_1(P)>=3`, the distance-three quotient-coset condition, and the root-block touch geometry, so it applies unchanged to this rank-two `P`.

At one root block, the twelve no-root cycles that touch it split into three projective local directions with multiplicities `4+4+4`. Two distinct root blocks are co-touched only when their root triples share two vertices; then exactly three no-root cycles touch both, one in each local direction.

If `rank E_b=1`, `E_b not subset P` and `L_b subset P` force `L_b=0`; all touches are parallel to the selected singleton direction. Such a singleton is aligned and has three or four touches.

If `rank E_b=2`, write the three direction multiplicities as `m_0,m_1,m_2` and the total touches as `t`. The nonzero line `L_b<=P` and `d_1(P)>=3`, together with the distance-three quotient coset, give

`m_i <= t-3`

for all three directions. Hence a rank-two singleton has `t>=5`.

The overlap proof from the committed `k=4,p=3` closure now applies verbatim. Two rank-two singleton blocks would each have at least five touches among seven cycles and force a three-cycle common touch set; neither possible root-block geometry leaves a valid third singleton. With exactly one rank-two singleton, each aligned singleton is forced to contain the same two cycles outside the five-touch set, but two such cycles cannot both use one aligned direction at either block. Thus rank-two singleton blocks are impossible.

All three singleton blocks are therefore aligned rank-one blocks and have `L_b=0`. The global rank-two coefficient space `P` is generated entirely by empty constraints on the other touched root blocks.

## 4. Exact rank-two exhaustion

The same exact `S_7` block-triple classification from the `k=4,p=3` closure leaves only

```text
(123,124,125)
(123,124,134)
(123,124,135)
```

as possible singleton-block triples. Their exact seven-cycle configuration counts are

```text
singleton-block orbit      configurations
(123,124,125)                    654
(123,124,134)                     81
(123,124,135)                     54
------------------------------------
total                            789
```

For each configuration, the verifier exhausts every rank-two coefficient space generated by choosing empty states on the remaining touched non-singleton blocks. Exact rational row-space deduplication gives

```text
singleton-block orbit      rank-2 coefficient candidates
(123,124,125)                         19,128
(123,124,134)                          2,268
(123,124,135)                          1,386
---------------------------------------------
total                                 22,782
```

Each candidate is tested against `(d_1,d_2)>=(3,4)` by exact rational puncturing. Deleting any two coordinates must leave rank two, and deleting any three coordinates cannot kill the whole plane. The number of survivors is exactly zero.

Therefore no seven-no-root `D=-2,k=5,d=1,p=3` state exists.

## 5. Close `D=-1,k=5,d=2,p=1`

For a pair deletion in a `D=-1` seven-row counterexample, the second deleted row either lowers the external quotient rank or does not. If it does not, the five-row shadow has

`D=3, k=3, p=1`.

The five-row containment theorem gives, even at its weakest parameters `d_v=1,q=1`,

`D >= 5+1+3-3 = 6`.

Thus the no-drop alternative is impossible for every pair. Every pair deletion would have to lower the external quotient rank once.

Translate this to the rank-two coefficient code `P<=Q^7`. Projection after deleting any coordinate pair must lower `rank(P)` by one, so every coordinate pair supports a nonzero vector of `P`. The `D=-1` all-depth theorem gives `d_1(P)>=2`, so such a vector uses both coordinates.

Take the words supported on disjoint pairs `{1,2}` and `{3,4}`. They are independent and span the two-dimensional `P`. Hence every vector of `P` is supported inside `{1,2,3,4}`. But the pair `{5,6}` must also support a nonzero vector of `P`, impossible.

Therefore no seven-no-root `D=-1,k=5,d=2,p=1` state exists.

## 6. Remaining `k=5` boundary

The full `k=5` boundary was

```text
D=-2: (d,p)=(0,6),(1,3),(2,0)
D=-1: (d,p)=(0,7),(1,4),(2,1)
```

The remaining cases are exactly

```text
D=-2: (d,p)=(0,6)
D=-1: (d,p)=(0,7),(1,4)
```

The `D=-1,d=1,p=4` branch is the smallest next target. A pair with no second quotient-rank drop would give a five-row `D=3,k=3,p=4` shadow, immediately adjacent to the current coverage-correct `k=3,p<=3` theorem. Extending that theorem through the sharp `p=4,D=3` boundary would either force every pair-rank drop or close the seven-row branch directly.

The direct C-II endpoint remains unchanged at

`3874 = 3076 C7 + 798 (C3 disjoint-union C4)`.

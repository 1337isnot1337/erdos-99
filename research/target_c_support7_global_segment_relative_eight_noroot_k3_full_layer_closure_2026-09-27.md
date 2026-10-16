<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "ceb5ac96287301d68657135c12f25954c8dd5d02", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k3_full_layer_closure_2026-09-27.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "6e719298dc81b9157a7ff86c2de73f007bf3c207471560ecfe8b4f0dd81398b3"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: close the eight-no-root k=3 layer and complete the t<=8 rank-density barrier

Date: 2026-09-27

Status: proof-level reduction plus exact finite support certificate. The new theorem closes the final `k=3` eight-no-root rank-density branch. On the branch containing the independently audited `k=4,r=2` closure, this completes the entire eight-no-root factor-three rank-density layer. It does not close Target C-II or Erdős Problem #99.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k3_closure_2026_09_27.py`

Branch dependencies beyond current `main`:

- `107e552cd2afbc98677801bf78479a97d0e0de83` closes the final `k=4,p=3,r=2` subcase;
- `ce1694b1cbf6d05522b5828a3c96c352dc0d2afe` independently audits that closure and its six-shard exact certificate.

The present `k=3` argument itself does not use either commit.

## 1. Arithmetic leaves one k=3 branch

Let `B=R union E`, `|E|=8`, be a hypothetical eight-no-root counterexample and write

`D(B)=|B|-3 delta(B)`.

The committed seven-no-root theorem gives `D(B\S)>=0` for every nonempty proper deletion `S subset E`. As in the committed eight-no-root reductions, every external row of a counterexample is therefore an `M`-coloop and a `Q`-noncoloop, so

`D(B) in {-2,-1}`.

The exact root-block formula is

`D(B)=8+p+3 d_root-3k`.

If `k<=2`, its right side is at least `2`, so no counterexample exists. For `k=3`,

`D(B)=p+3 d_root-1`.

Thus `D=-2` is impossible, while `D=-1` forces

`p=0, d_root=0`.

Consequently the only eight-no-root layer below `k=4` that needs any work is

`k=3, D=-1, d_root=0, p=0`.

## 2. Rank-five generalized-weight floors

For `k=3` the external coefficient-constraint space is

`P <= Q^8, rank(P)=8-k=5`.

For a deletion set `S` of size `s`, let `q_S` be the rank loss of `P` under puncturing on `S`. The all-depth identity gives

`D(B\S)=-1+2s-3q_S>=0`.

Hence the generalized Hamming weights of `P` satisfy

`d_j(P)>=ceil((3j+1)/2)`,

so

`(d1,d2,d3,d4,d5)(P)>=(2,4,5,7,8)`.

Because `p=0`, every touched incomplete root block is actual-empty. Complete and pair states contribute no coefficient constraint, while a singleton would consume one unit of `p`; therefore the local empty-block spaces generate all of `P`.

For a touched block `b`, let `I_b` be its set of external occurrences. The committed local-block rule gives `dim(E_b)=1` or `2`. Since the actual coordinate support of `E_b` is contained in `I_b`, every actual-empty block satisfies

- `dim(E_b)=1 => |I_b|>=2`;
- `dim(E_b)=2 => |I_b|>=4`.

Two actual-empty local spaces also obey the following necessary weak support tests.

- line-line: `|I intersect J|>=2` or `|I union J|>=4`;
- line-plane: `|I intersect J|>=2` or `|I union J|>=5`;
- plane-plane: `|I intersect J|>=4`, or both `|I intersect J|>=2` and `|I union J|>=5`, or `|I union J|>=7`.

These are obtained by splitting according to the intersection dimension of the two local spaces and applying `d1,d2,d3,d4` to their intersection or sum. They deliberately use the larger occurrence sets rather than the unknown exact supports, so they only enlarge the search.

Since the empty local spaces generate rank five,

`sum_b dim(E_b)>=5`.

The floor `d5(P)=8` says `support(P)` is all eight coordinates. Therefore the union of the empty-block occurrence sets must cover all eight external coordinates.

## 3. Touched-block bound

Let `h` be the number of touched root blocks, `e` the number of touched empty blocks, and `c=h-e` the number of touched complete blocks.

Because `d_root=0`, all complete-root triangle rows are independent. The ground-root triangle-row space has rank 15, so

`c<=15`,

and therefore

`e>=h-15`.

Every empty block has at least two external incidences by `d1(P)>=2`; every complete touched block has at least one. The eight no-root four-cycles contribute exactly 32 cycle-block incidences. Hence

`32>=2e+c=h+e>=2h-15`,

so

`h<=23`.

This bound uses only complete-row independence, not the external relation-capacity condition used below.

## 4. Face-local capacity

Let `T` be the touched triangle-block set and `C subset T` the touched complete blocks.

The committed face-local four-cycle identity puts every external relation lift in `H(T)`, the triangle-row span of `T`. For `k=3` there are three independent external relation directions modulo the full complete-root span. Passing to the smaller touched-complete span `H(C)` cannot destroy their independence. Therefore every actual state must satisfy

`rank H(T)-rank H(C)>=3`.

Since `d_root=0`, `H(C)` also has rank exactly `|C|`.

## 5. Exact finite certificate

The verifier imports the already committed support-orbit and exact triangle-rank layer from

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d1p0_support_closure_2026_09_26.py`.

It regenerates all `S_7`-orbits of multisets of eight tetrahedral four-supports, with multiplicity at most three, and reproduces the established orbit counts

`1,1,4,14,61,268,1283,6032,27763`.

For every size-eight support orbit it computes the touched blocks and exhaustively enumerates every pairwise-compatible set of individually eligible virtual empty blocks. The virtual search imposes only necessary conditions:

1. `h<=23` and at least `h-15` empty blocks;
2. the pairwise generalized-weight tests in Section 2;
3. nominal empty-space dimension at least five;
4. occurrence support covering all eight coordinates;
5. independence of the complementary touched-complete rows;
6. face-local capacity at least three.

It does not require the nominal local spaces to glue into a common rank-five `P`, so every actual state is included in the search.

The exact census is

```text
support_multiset_orbits_size_8       27763
touch_at_most_23                     24720
cardinality_compatible_empty_sets    22686
dimension_at_least_5                 16385
full_support_empty_sets               7203
complete_independent                    59
capacity 0                              38
capacity 1                              19
capacity 2                               2
capacity >=3                             0
```

Thus every candidate surviving the coefficient-support and complete-row tests has face-local capacity at most two. An actual `k=3` state requires capacity at least three. Contradiction.

Therefore

> **Theorem 1.** There is no eight-no-root counterexample with `k=3`.

## 6. Exactness

Support canonicalization, incidence, and generalized-weight tests use exact integer/set arithmetic.

Triangle-row ranks are computed modulo `2^31-1` by the imported verifier. That verifier checks primality by Lucas-Lehmer. Triangle rows have squared Euclidean norm three and rank at most 15, and it checks

`(2^31-1)^2 > 3^15`.

Hadamard's inequality therefore makes every modular triangle-row rank used here equal to the rational rank.

The exact verifier source persisted in this commit was executed end-to-end locally before upload. Its imported helper functions were supplied by a source-equivalent local copy of the already audited current-main helper blob `acce53eedc2ab64147588a21a4e8e693cb6bfbc6`. The run reproduced every census value above and `capacity_survivors=0`. The post-persistence repository import was not rerun byte-for-byte in this run.

## 7. Composition: the t<=8 rank-density barrier

Current `main` already closes the eight-no-root `k=8`, `k=7`, `k=6`, and `k=5` layers and all `k=4` branches except the audited `r=2` subcase. The branch containing commits `107e552...` and `ce1694b...` closes that final `k=4` subcase. The present theorem closes `k=3`, and Section 1 excludes `k<=2` arithmetically.

Hence, on this branch, every eight-no-root counterexample is excluded. Combined with the committed seven-no-root theorem:

> **Theorem 2.** Every four-cycle family containing at most eight no-root four-cycles satisfies
>
> `3 delta(A) <= |A|`.

Under the established 44-cycle sufficient-family reduction, sufficiency requires `delta(A)=15`. A 44-row family has `44-3*15=-1`, so Theorem 2 implies:

> every hypothetical sufficient 44-cycle family contains at least nine no-root four-cycles.

This advances the metric-basis route by one full no-root layer. It does not prove that the existing 45-cycle test is globally minimal: the next unresolved density layer is nine no-root cycles. It also does not alter the canonical C-II macroscopic-container/full-core frontier.

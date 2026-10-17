> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_five_noroot_k3_p5_sharp_2026-09-21.md) · source SHA-256 `71b5bf0f1e1fe97f57eb8729116ad3bdd5e7c16b32b158772add59720985de82`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "a9ac013d4d22bfd3aaf8f8734095717b8d307f5e", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_five_noroot_k3_p5_sharp_2026-09-21.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "a3b98fded2be0f1560431e0737d4fdd5612011f80ca7a61f963f3fe4dd47f9c2"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: five-no-root `k=3,p=5` sharp boundary

Date: 2026-09-21

Status: exact quantitative closure of the five-no-root `k=3,p=5` slice:

`D>=1`.

There are exactly 6,445 canonical minimal `D=1` cores. Every one has virtual canonical deficiency two and consists of five singleton replacements of five canonical-complete blocks.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_five_noroot_k3_p5_sharp_2026_09_21.py`

## Reduction

The repaired five-row containment theorem gives

`D >= 5+p+3d-3q`.

At `p=5`,

`D >= 10+3d-3q`,

with `d>=1` and `q<=5`. Since `D=|A|-3 delta(A)` is congruent to one modulo three in this slice, a negative state would have `D<=-2`.

The only containment class that can reach below one is

`d=1,q=5`.

That class would require five singleton replacements of canonical-complete blocks. The exact deficiency-one virtual census has only 86 states, and their unfiltered number of canonical-complete blocks admitting a compatible singleton is

```text
capacity   d=1 virtual states
0                 71
2                  3
3                 12
```

The maximum is three, so `d=1,q=5` is impossible. This proves `D>=1` once the sharp boundary classes are audited.

## Exact `D=1` boundary

The containment equality `D=1` can occur only at

- `d=1,q=4`, or
- `d=2,q=5`.

For `d=1,q=4`, a five-row cost of five can be realized either by one pair plus three singleton replacements on four canonical-complete blocks, or by five singleton blocks with only four replacing canonical-complete blocks. The latter requires singleton capacity at least four and is already impossible. The exact audit of the pair-plus-three-singleton class finds 144 realizations, all with

`D=7`.

For `d=2,q=5`, all five incomplete rows must be singleton replacements of canonical-complete blocks. The exact local-generation and relation-rank audit gives

```text
result                         states
fail to realize target P          268
exact realizations             67,515
```

Their defect census is

```text
D        states
1         6,445
4        35,573
7        17,156
10        8,175
13          166
```

Hence the minimum is exactly one.

The 6,445 sharp cores have remaining complete-block count `c'` and exact relation rank `delta`:

```text
c'   delta   D=1 cores
3      6           41
4      7          340
5      8        2,992
6      9        3,072
----------------------
total             6,445
```

As in the `p=4` audit, later completion of a canonical-empty block can preserve defect when it raises relation rank by one. Thus 6,445 counts canonical minimal cores rather than all actual sharp states. The incomplete part of every sharp core is nevertheless five singleton blocks.

## Exactness

The scan uses the full 535,040-state coverage-correct rank-two coefficient-space census. Coefficient-space operations are exact over the rationals. Relation ranks use the established `2^127-1` prime. The maximum squared norm of any relation row in the audit is 44, and the existing Hadamard certificate applies.

Together with the new `p=4` result, the repaired five-row `k=3` containment route now has exact quantitative bounds through `p=5`:

- `p=4`: `D>=3`, with 19,392 canonical `D=3` cores;
- `p=5`: `D>=1`, with 6,445 canonical `D=1` cores.

These sharp structures can be used as deletion targets in the two remaining seven-no-root `k=5` branches.

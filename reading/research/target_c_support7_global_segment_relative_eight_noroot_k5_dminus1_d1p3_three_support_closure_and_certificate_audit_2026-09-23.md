> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_three_support_closure_and_certificate_audit_2026-09-23.md) · source SHA-256 `429ecb3d10da992e1d6db8aa9af19dd6802d4ed2e04a5e4be98d8b68632a374c`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "8c5b4e125cb4677b33c3b462c5f44288391f76a6", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_three_support_closure_and_certificate_audit_2026-09-23.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "7d53712e07b212530fc728e67ffe2ac575a3993e2ea8edd4b6045befabf9d68d"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: close the three-support branch in the eight-no-root `k=5,D=-1,d_root=1,p=3` state

Date: 2026-09-23

Status: exact finite closure of the `m=3` subbranch, plus a certificate audit of the already-closed `m=5` subbranch. This does **not** close `m=4`, the full `k=5` layer, Target C-II, or Erdos Problem #99.

Inputs:

- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_three_singleton_basis_reduction_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_tetrahedral_support_compression_2026-09-23.md`;
- the exact K8 normal form in `research/verify_target_c_support7_global_segment_relative_four_noroot_k2_2026_09_20.py`.

## 1. Certificate audit: the old eight-cycle wrapper used a four-cycle nullspace helper

The base verifier function

```python
relation_rows_int(ext, touched, states, constraint_key)
```

calls

```python
nullspace_int(constraint_key, 4)
```

because that base module was written for four selected no-root cycles. The first `m=5` eight-cycle wrapper imported that helper unchanged. Therefore that wrapper is not a valid executable certificate for an eight-element `ext`: the external coefficient nullspace has dimension `8-rank(P)=5`, not `4-rank(P)`.

This is a verifier bug, not a mathematical counterexample to the five-support closure. The new file

`verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_five_support_closure_corrected_2026_09_23.py`

repeats the five-support census with the nullspace dimension set to `len(ext)=8`. An independent local reconstruction of the exact K8 normal form was run in two bounded shards covering all 43 `S_5` cycle-set orbits. The corrected relation rank is still exactly six for every one of the 36,106 generalized-weight-admissible states. Thus the five-support closure survives the audit. The older wrapper should not be used as the certificate.

## 2. What `D=-1` requires in the three-support branch

The support-compression theorem leaves, for `m=3`, only support multiplicity

```text
(3,3,2).
```

The three-singleton-basis reduction gives exactly three touched singleton root blocks. Every other touched block is complete, and the touched-complete root nullity is at most one. The singleton rows span a rank-three coefficient code

```text
P <= Q^8
```

with

```text
(d_1,d_2,d_3) >= (2,4,5).
```

Let `C_touch` be the touched complete blocks and let

```text
r_touch = rank H(C_touch).
```

The branch has `d_root=1`. In any full completion with `c` complete root blocks, the root relation span therefore has rank `c-1`. Since `rank(P)=3`, there are five external nullspace relations. From

```text
D = 8 + 3c + 3 - 3 delta = -1
```

we obtain

```text
delta = c+4.
```

Hence all five external relations must be independent modulo the full complete-root span.

This gives a completion-independent necessary test. If `E` is the span of the five external relation rows for the touched state, then any addition of untouched complete root rows only enlarges the root span. Therefore

```text
dim((H(C_full)+E)/H(C_full))
<= dim((H(C_touch)+E)/H(C_touch)).
```

So a state is impossible whenever the external rank increment over the touched complete-root span is less than five.

## 3. Exact `m=3` census

There are `C(35,3)` choices of three four-vertex supports. For each support triple, one support has multiplicity two and the other two have multiplicity three, and the multiplicity-two support omits one of its three cycle orientations. Hence there are exactly

```text
C(35,3) * 3 * 3 = 58,905
```

raw eight-cycle sets.

Reduction by the full `S_7` action gives

```text
32
```

cycle-set orbits.

For each orbit representative the verifier enumerates every triple of touched singleton blocks and rejects it unless the remaining touched complete rows have nullity at most one. Across the 32 representatives this leaves

```text
5,124
```

singleton triples.

There are three local singleton directions at each of the three singleton blocks, so the reduced direction census contains

```text
5,124 * 3^3 = 138,348
```

states. Of these,

```text
125,117
```

have rank-three singleton coefficient space, and

```text
22,634
```

also satisfy

```text
(d_1,d_2,d_3) >= (2,4,5).
```

For each of those 22,634 states, form the complete-root relation rows and all five external nullspace relation rows using an eight-coordinate nullspace basis. The exact external rank increment over the touched complete-root span has census

```text
0 : 20,215
1 :  2,419
```

and never exceeds one. In particular it is never the required value five.

Therefore:

> **Theorem.** The `m=3` subbranch of the eight-no-root `k=5,D=-1,d_root=1,p=3` branch is empty.

Untouched complete blocks cannot repair a state: enlarging the root span can only decrease the number of independent external directions modulo that span.

## 4. Exactness of the rank decisions

The relation rows are integral and are reduced modulo

```text
P = 2^127 - 1.
```

The base verifier certifies this Mersenne prime with Lucas-Lehmer. In the complete `m=3` census the maximum squared Euclidean norm of any relation row is

```text
70.
```

The verifier checks

```text
P^2 > 70^15.
```

Hadamard's inequality therefore bounds every nonzero minor of order at most 15 strictly below `P` in absolute value. Modular rank is consequently equal to rational rank for every rank decision used above.

## 5. Remaining finite target

The branch `D=-1,k=5,d_root=1,p=3` now has only the four-support case:

```text
m=4:
(3,3,1,1),
(3,2,2,1),
(2,2,2,2),
```

with singleton-incidence rank three and touched-complete root nullity at most one.

The next target is the same completion-independent external-rank-increment test for these four-support profiles. If every generalized-weight-admissible state has increment less than five, the entire `p=3` branch closes.

The other open `k=5` arithmetic branches remain

```text
D=-2, (d_root,p)=(0,5),
D=-1, (d_root,p)=(0,6).
```

No theorem-state authority file is changed by this note.

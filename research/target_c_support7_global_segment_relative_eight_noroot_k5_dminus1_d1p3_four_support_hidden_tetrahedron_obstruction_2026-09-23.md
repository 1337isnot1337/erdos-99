<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "ead49d2b4ab701a635c236b5a1ae1d7385dd642f", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_hidden_tetrahedron_obstruction_2026-09-23.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f785bc25c51c63797591852c91be283bbb7ecd634e9c011057666d79b9904e12"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: a support-nullity obstruction in the remaining four-support `p=3` branch

Date: 2026-09-23

Status: proof-level elimination of one previously open `S_7` support-set orbit in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4` branch. The elimination applies simultaneously to the remaining multiplicity profiles `(3,2,2,1)` and `(2,2,2,2)`. It does not close either full profile, the full `p=3` branch, the full `k=5` layer, Target C-II, or Erdos Problem #99.

Inputs:

- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_three_singleton_basis_reduction_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_tetrahedral_support_compression_2026-09-23.md`;
- the complete-root triangle-boundary identification and the five-tetrahedron independence lemma proved there.

## 1. General support-nullity obstruction

In every surviving `m=4` state of this branch there are exactly three singleton root blocks `S`, every other touched root block is complete, and the touched-complete relation nullity satisfies

```text
nullity H(T \ S) <= 1,
```

where `T` is the set of touched root blocks.

For any finite row set `T`, deleting one row can lower row-nullity by at most one. Therefore deleting three rows gives

```text
nullity H(T \ S) >= nullity H(T) - 3.
```

Consequently:

> **Lemma.** Any four-support state with `nullity H(T) >= 5` is impossible in the `p=3,m=4` branch.

Indeed, every choice of three singleton rows would leave touched-complete nullity at least two.

This obstruction depends only on the four underlying tetrahedral supports. It is independent of four-cycle orientations, singleton directions, and the multiplicity profile on those supports.

## 2. A previously open order-4 support orbit

Consider the support representative

```text
F1 = 1234,
F2 = 1235,
F3 = 1456,
F4 = 2457.
```

Its touched triangle set is

```text
T = {
  123,124,125,134,135,
  145,146,156,
  234,235,245,247,257,
  456,457
}.
```

Besides the four tetrahedron boundaries supplied by the used supports, `T` contains all four faces of the additional tetrahedron

```text
G = 1245,
```

because

```text
{124,125,145,245} subset T.
```

Hence `H(T)` has the five tetrahedron-boundary dependencies

```text
z_1234,
z_1235,
z_1456,
z_2457,
z_1245.
```

These five dependencies are linearly independent. The repository's small-rank tetrahedron-boundary lemma says that five distinct tetrahedron boundaries are dependent only when they are exactly the five 4-faces of one common 5-vertex set. The five supports above use all seven vertices, so they are not such a 4-simplex boundary.

Therefore

```text
nullity H(T) >= 5.
```

The support-nullity lemma now gives

```text
nullity H(T \ S) >= 2
```

for every three-element singleton set `S`, contradicting the necessary touched-complete nullity bound.

Thus:

> **Theorem.** No state in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4` branch can have a four-support set in the `S_7` orbit of
>
> ```text
> {1234,1235,1456,2457}.
> ```

This theorem applies to every multiplicity profile on those four supports. The `(3,3,1,1)` profile was already closed globally, so the new reduction removes this orbit from both still-open profiles `(3,2,2,1)` and `(2,2,2,2)`.

## 3. Exact support-level certificate

The companion verifier

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_hidden_tetrahedron_obstruction_2026_09_23.py`

uses only the ordinary triangle-boundary matrix over `Q`. It independently checks:

```text
touched triangles: 15
rank H(T): 10
nullity H(T): 5
```

and exhausts all `C(15,3)=455` possible singleton triples. The resulting touched-complete nullity census is

```text
2 : 350
3 : 103
4 :   2
```

so no singleton triple leaves nullity at most one.

The same script checks that the support-set stabilizer has order four. Therefore this support orbit contains

```text
5040 / 4 = 1260
```

labeled support sets.

For the two still-open multiplicity profiles, the support-stabilizer quotient gives:

```text
(2,2,2,2): 24 S_7 cycle-set orbits, 102060 labeled cycle sets;
(3,2,2,1): 84 S_7 cycle-set orbits, 408240 labeled cycle sets.
```

Hence this proof removes 108 cycle-set orbit representatives, or 510300 labeled cycle sets, from the remaining finite `m=4` search before any singleton-direction arithmetic.

The verifier was executed locally exactly over `Fraction`; its output matched all asserted counts. No modular-rank heuristic is involved.

## 4. Remaining target

The `D=-1,k=5,d_root=1,p=3` branch still consists of:

```text
(3,2,2,1)
```

on the other four-support orbits, and

```text
(2,2,2,2)
```

on the still-unclosed low-symmetry support orbits after removing the orbit above. The completion-independent external-rank-increment test remains the direct finite target for those states.

The other unresolved `k=5` arithmetic branches remain

```text
D=-2, (d_root,p)=(0,5),
D=-1, (d_root,p)=(0,6).
```

No theorem-state authority file is changed by this note.

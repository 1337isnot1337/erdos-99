> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_order1_shard_a_closure_2026-09-24.md) · source SHA-256 `0aa3f1ce0b39080e052ef54a32bf3da3a814ff81cd02d36315b3b74d13ea2e88`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "a92f4245e6e5a8f06e9345a11030ed06bee1780d", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_order1_shard_a_closure_2026-09-24.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "21a69eeea21494ad94282e2446379318c455520d8d6cdd4cea6acc14ff944391"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: close the first order-1 `(3,2,2,1)` support orbit in the `p=3,m=4` branch

Date: 2026-09-24

Status: exact finite closure of the stabilizer-order-1 support orbit represented by `{1234,1235,1246,1367}` in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(3,2,2,1)` branch, conditional on the structural reductions already proved in the repository. This does not close the full `(3,2,2,1)` profile, the full `p=3` branch, the `k=5` layer, Target C-II, or Erdos Problem #99.

## Support orbit

The support stabilizer is trivial. Therefore all 324 `(3,2,2,1)` external cycle choices over this support are distinct cycle-set orbits over the fixed support representative. The support orbit contains `7! = 5040` labeled support sets, so this certificate covers

```text
5040 * 324 = 1632960
```

labeled eight-cycle sets.

Every representative touches the same 14 root blocks. The complete touched-root family has exact rank 10 and nullity 4. Exactly 208 choices of three touched root blocks leave the remaining complete-root family with nullity one.

The existing branch reduction requires three singleton blocks, singleton coefficient rank three, generalized weights at least `(2,4,5)`, and external relation-rank increment five.

## Exact finite census

The 324 cycle-set representatives were split into three disjoint shards.

```text
[0,108):
  admissible singleton triples    22464
  singleton-direction states     606528
  coefficient-rank-three states  471140
  generalized-weight states       32822
  external increment census   {0:32822}
  max relation-row norm^2             70

[108,216):
  admissible singleton triples    22464
  singleton-direction states     606528
  coefficient-rank-three states  480072
  generalized-weight states       33422
  external increment census   {0:33422}
  max relation-row norm^2             70

[216,324):
  admissible singleton triples    22464
  singleton-direction states     606528
  coefficient-rank-three states  487076
  generalized-weight states       34860
  external increment census   {0:34860}
  max relation-row norm^2             70
```

Aggregate totals are

```text
admissible singleton triples      67392
singleton-direction states      1819584
coefficient-rank-three states   1438288
generalized-weight states        101104
external increment census     {0:101104}
```

Every generalized-weight-admissible state has external relation-rank increment zero, whereas a survivor requires increment five. Therefore this support orbit is empty.

> **Theorem.** No `(3,2,2,1)` state in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4` branch can have support set in the `S_7` orbit of `{1234,1235,1246,1367}`.

## Exactness and validation

The finite census above was executed with a standalone exact reconstruction of the current repository K8 coordinate normal form and the verifier logic. Before running the new `(3,2,2,1)` enumeration, the same reconstruction was run on the repository's already-closed `(2,2,2,2)` order-1 class with this same support. It reproduced the committed class-I census exactly:

```text
S7 cycle-set orbits                  81
admissible singleton triples     16848
singleton-direction states      454896
coefficient-rank-three states   454896
generalized-weight states        23808
external increment census    {0:23808}
max relation-row norm^2              70
```

Ranks of the final relation rows are computed modulo `P=2^127-1`. Lucas-Lehmer passes. The maximum squared Euclidean norm of any relation row in the new certificate is 70, and

```text
P^2 > 70^15.
```

The repository's Hadamard argument therefore certifies the modular ranks as the corresponding rational ranks. The zero-only increment census is an exact finite certificate, not probabilistic finite-field evidence.

The companion repository verifier re-enumerates the 324 candidates, checks that the support stabilizer is trivial, checks the touched-root rank/nullity and the 208 admissible singleton triples, asserts all three shard censuses, asserts the zero-only increment census, and checks the same Hadamard bound. It was syntax-checked before upload. The committed wrapper itself was not executed from a repository checkout in this run; the proof evidence is the executed standalone reconstruction described above.

## Remaining target

After this closure, only the second stabilizer-order-1 `(3,2,2,1)` support class remains in the touched-nullity-four support catalog:

```text
{1234,1235,1456,2467}
```

The final stabilizer-order-2 class `{1234,1235,1267,1467}` has an exact certificate on branch `target-c-3221-order2-final-20260924`, but that commit is not yet on `main` at the time of this note.

The other unresolved `k=5` arithmetic branches remain

```text
D=-2, (d_root,p)=(0,5),
D=-1, (d_root,p)=(0,6).
```

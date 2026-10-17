> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_order2_shard_g_closure_2026-09-24.md) · source SHA-256 `fbed0fff7873e79718bc97ef7c1d6e70ac2e97e5826c84fd8013b4474d52c9a9`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "73ec32818ce4136551938fa951665dfe6c51e253", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_order2_shard_g_closure_2026-09-24.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "1e36a26dabf39f04e70688dabd1042ad83ea819a62357a2b7e5e8804856ef1e3"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: close the seventh order-2 `(3,2,2,1)` support orbit in the `p=3,m=4` branch

Date: 2026-09-24

Status: exact finite closure of the stabilizer-order-2 support orbit represented by `{1234,1235,1267,1456}` in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(3,2,2,1)` branch, conditional on the structural reductions already proved in the repository. This does not close the full profile, the full `p=3` branch, the `k=5` layer, Target C-II, or Erdos Problem #99.

## Support orbit

The support stabilizer has order two. The exact orbit catalog gives 168 `S_7` cycle-set representatives and `(7!/2)*324 = 816480` labeled eight-cycle sets. Every representative touches the same 15 root blocks. The complete touched-root family has exact rank 11 and nullity 4. Exactly 232 choices of three touched root blocks leave the remaining complete-root family with nullity one.

The existing reduction requires three singleton blocks, singleton coefficient rank three, generalized weights at least `(2,4,5)`, and external relation-rank increment five.

## Exact finite census

```text
[0,56):
  admissible singleton triples    12992
  singleton-direction states     350784
  coefficient-rank-three states  266148
  generalized-weight states       13308
  external increment census   {0:13308}
  max relation-row norm^2             36

[56,112):
  admissible singleton triples    12992
  singleton-direction states     350784
  coefficient-rank-three states  270816
  generalized-weight states       13296
  external increment census   {0:13296}
  max relation-row norm^2             36

[112,168):
  admissible singleton triples    12992
  singleton-direction states     350784
  coefficient-rank-three states  272064
  generalized-weight states       13248
  external increment census   {0:13248}
  max relation-row norm^2             34
```

Aggregate totals are 38,976 admissible singleton triples, 1,052,352 singleton-direction states, 809,028 coefficient-rank-three states, and 39,852 generalized-weight-admissible states. Every final state has external relation-rank increment zero, whereas survival requires increment five. Therefore this support orbit is empty.

## Exactness and validation

The verifier used for this certificate was syntax-compiled and executed locally on all three disjoint shards. The same reconstruction reproduced the already-committed fifth order-2 certificate on `[0,59)` exactly: 12,272 singleton triples, 331,344 direction states, 257,478 rank-three states, 18,116 generalized-weight states, increment census `{0:18116}`, and maximum squared relation-row norm 70.

Ranks of the final relation rows are computed modulo `P=2^127-1`. Lucas-Lehmer passes. The maximum squared relation-row norm in this new class is 36, and `P^2 > 36^15`, so the repository's Hadamard argument certifies the modular ranks over `Q`.

The committed companion wrapper specializes the already-committed shard-E engine by exact text substitutions guarded by uniqueness assertions. It changes only the target support, expected orbit metadata, expected shard census, admissible-singleton count, and status label; the enumeration and exact-rank machinery remain the shard-E implementation.

## Remaining target

After this closure, one stabilizer-order-2 and two stabilizer-order-1 touched-nullity-four `(3,2,2,1)` support classes remain.

The final order-2 representative is `{1234,1235,1267,1467}`, with 198 `S_7` cycle-set representatives, 14 touched root blocks, touched-root rank 10/nullity 4, and 210 admissible singleton triples per representative.

The two remaining stabilizer-order-1 representatives are `{1234,1235,1246,1367}` and `{1234,1235,1456,2467}`.

The other unresolved `k=5` arithmetic branches remain `D=-2,(d_root,p)=(0,5)` and `D=-1,(d_root,p)=(0,6)`.

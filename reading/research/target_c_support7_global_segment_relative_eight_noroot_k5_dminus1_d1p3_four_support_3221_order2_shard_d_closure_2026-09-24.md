> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_order2_shard_d_closure_2026-09-24.md) · source SHA-256 `271f7954e0ab1051d9d5dce26b8d5d7a3c14292c0aa19b7962a2bd441aa8fadd`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "bed35d97902785b42cd57505f735aaf1f0bfec83", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_order2_shard_d_closure_2026-09-24.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "47a954570aa238d68f955e88f3c8c78956d7e3e3bbe3ace65d656e9a477e0579"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: close the fourth order-2 `(3,2,2,1)` support orbit in the `p=3,m=4` branch

Date: 2026-09-24

Status: exact finite closure of the stabilizer-order-2 support orbit represented by `{1234,1235,1246,1567}` in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(3,2,2,1)` branch, conditional on the structural reductions already proved in the repository. This does not close the full profile, the full `p=3` branch, the `k=5` layer, Target C-II, or Erdos Problem #99.

## Support orbit

The support stabilizer has order two. The exact orbit catalog gives 165 `S_7` cycle-set representatives and `(7!/2)*324 = 816480` labeled eight-cycle sets. Every representative touches the same 14 root blocks. The complete touched-root family has exact rank 10 and nullity 4. Exactly 208 choices of three touched root blocks leave the remaining complete-root family with nullity one.

The existing reduction requires three singleton blocks, singleton coefficient rank three, generalized weights at least `(2,4,5)`, and external relation-rank increment five.

## Exact finite census

The 165 representatives were split into three disjoint intervals.

```text
[0,55):
  admissible singleton triples    11440
  singleton-direction states     308880
  coefficient-rank-three states  239408
  generalized-weight states       16534
  external increment census   {0:16534}
  max relation-row norm^2             70

[55,110):
  admissible singleton triples    11440
  singleton-direction states     308880
  coefficient-rank-three states  239902
  generalized-weight states       16036
  external increment census   {0:16036}
  max relation-row norm^2             70

[110,165):
  admissible singleton triples    11440
  singleton-direction states     308880
  coefficient-rank-three states  253166
  generalized-weight states       18872
  external increment census   {0:18872}
  max relation-row norm^2             70
```

Aggregate totals are 34,320 admissible singleton triples, 926,640 singleton-direction states, 732,476 coefficient-rank-three states, and 51,442 generalized-weight-admissible states. Every final state has external relation-rank increment zero, whereas survival requires increment five. Therefore this support orbit is empty.

## Exactness and validation

The finite census above was executed in a standalone exact reconstruction of the current-main coordinate model. As an implementation control, that reconstruction reproduced the previously committed third order-2 certificate on interval `[0,54)` exactly: 10,044 singleton triples, 271,188 direction states, 216,260 rank-three states, 20,506 generalized-weight states, increment census `{0:20506}`, and maximum squared relation-row norm 70.

Ranks of the final relation rows were computed modulo `P=2^127-1`. Lucas-Lehmer passed, the maximum squared relation-row norm was 70, and `P^2 > 70^15`, so the repository's Hadamard argument certifies the modular ranks over `Q`.

The companion repository verifier records the exact three-shard census and hard assertions. That wrapper was derived from the current-main third order-2 verifier but was not itself executed end-to-end in a repository checkout during this run; the executed evidence is the standalone reconstruction described above.

## Remaining target

After this closure, four stabilizer-order-2 and two stabilizer-order-1 touched-nullity-four `(3,2,2,1)` support classes remain. The next order-2 representative is `{1234,1235,1246,3457}`, with 177 `S_7` cycle-set representatives, 14 touched root blocks, touched-root rank 10/nullity 4, and 208 admissible singleton triples per representative.

The other unresolved `k=5` arithmetic branches remain `D=-2,(d_root,p)=(0,5)` and `D=-1,(d_root,p)=(0,6)`.

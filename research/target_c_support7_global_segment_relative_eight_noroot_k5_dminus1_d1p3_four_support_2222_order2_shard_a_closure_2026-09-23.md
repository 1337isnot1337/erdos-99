<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "dfb102695b581a72fb6b1c4fe35054469f2bddfe", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_2222_order2_shard_a_closure_2026-09-23.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "e80b72b7645015cf776ee182d40a938e7e280d342e8d21a7ffd6560906f339f0"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: close two order-2 `(2,2,2,2)` support orbits in the `p=3,m=4` branch

Date: 2026-09-23

Status: exact finite closure of two of the eight previously open stabilizer-order-2 support-set `S_7` orbits in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(2,2,2,2)` branch. This does not close the full `(2,2,2,2)` profile, the full `p=3` branch, the `k=5` layer, Target C-II, or Erdos Problem #99.

## 1. Support shard

The two support representatives are

```text
A = {1234,1235,1245,1346},
B = {1234,1235,1246,1356}.
```

The exact four-support orbit enumeration has eight stabilizer-order-2 support classes. The companion verifier selects exactly `A,B` from that list and checks their stabilizers have order two.

For `(2,2,2,2)`, each support set has `3^4=81` cycle choices. The two support orbits therefore contain

```text
2 * (7!/2) * 3^4 = 408240
```

labeled eight-cycle sets. Quotienting the cycle choices by the support stabilizers gives 42 cycle-set orbits for `A` and 45 for `B`, hence 87 `S_7` cycle-set representatives in this shard.

## 2. Necessary survivor conditions

The existing `p=3,m=4` reduction forces exactly three singleton touched root blocks, all remaining touched root blocks complete, touched-complete root nullity one, singleton coefficient rank three, and generalized weights

```text
(d1,d2,d3) >= (2,4,5).
```

For `D=-1,d_root=1`, the rank-three singleton coefficient system on eight external cycles has a five-dimensional coefficient nullspace. All five external relations would have to survive independently modulo the touched complete-root relation span. Equivalently, a survivor requires external relation-rank increment five. Untouched complete blocks cannot increase this quotient increment.

## 3. Exact finite census

A standalone exact reconstruction of the repository K8 coordinate normal form was run separately on both support classes. The results were

```text
A:
  S7 cycle-set orbits              42
  admissible singleton triples   6720
  singleton-direction states   181440
  coefficient-rank-three       181440
  generalized-weight states     21428
  external increment census {0:21428}
  max relation-row norm^2          70

B:
  S7 cycle-set orbits              45
  admissible singleton triples   8370
  singleton-direction states   225990
  coefficient-rank-three       225990
  generalized-weight states     19154
  external increment census {0:19154}
  max relation-row norm^2          70
```

Thus the aggregate shard census is

```text
S7 cycle-set orbits               87
admissible singleton triples   15090
singleton-direction states    407430
coefficient-rank-three        407430
generalized-weight states      40582
external increment census {0:40582}
```

Every generalized-weight-admissible state has external relation-rank increment zero, not five. Therefore neither support orbit contains a survivor.

> **Theorem.** In the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(2,2,2,2)` branch, no state exists whose support set is in the `S_7` orbit of `A` or `B` above.

## 4. Exactness and validation

All coefficient and generalized-weight tests use exact integer arithmetic. Relation rows are integral and ranked modulo

```text
P = 2^127 - 1.
```

The maximum squared Euclidean relation-row norm encountered is 70. An independent Lucas-Lehmer calculation verifies `P` is prime, and

```text
P^2 > 70^15.
```

The existing Hadamard argument therefore rules out modular rank loss in the relevant minors, so the recorded relation ranks are exact over `Q`.

The companion repository wrapper was syntax-checked before upload. It was not executed from a checked-out repository during this run. The executed calculation was a standalone reconstruction using the same coordinate construction, support/cycle orbit enumeration, singleton filters, relation-row construction, and exact-rank criterion. The two support classes were executed separately and produced the counts above.

## 5. Remaining target

Before this run the open `(2,2,2,2)` support layer consisted of

```text
2 stabilizer-order-1 classes,
8 stabilizer-order-2 classes.
```

This theorem removes two order-two classes. The exact remaining `(2,2,2,2)` support bottleneck is therefore

```text
2 stabilizer-order-1 classes,
6 stabilizer-order-2 classes,
```

for eight support-set orbits total.

The `(3,2,2,1)` profile remains open on the 35 touched-nullity-four support classes. The other unresolved `k=5` arithmetic branches remain

```text
D=-2, (d_root,p)=(0,5),
D=-1, (d_root,p)=(0,6).
```

The next direct finite target is another bounded external-rank-increment shard among the six remaining order-two `(2,2,2,2)` support classes.

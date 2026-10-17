> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_2222_order2_shard_d_closure_2026-09-23.md) · source SHA-256 `9491e48bf247b8444c16620ccb2cb24f925752b3bae808be46e85a2306773df7`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "82694a065563bc4a10033c391d133a37003a24e7", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_2222_order2_shard_d_closure_2026-09-23.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "24bb240dd1214fd03963bc29f82e5921e3bb742571e0f817db4960b71dc56b80"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: close the final two order-2 `(2,2,2,2)` support orbits in the `p=3,m=4` branch

Date: 2026-09-23

Status: exact finite closure of the last two stabilizer-order-2 support-set `S_7` orbits in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(2,2,2,2)` branch. This closes the entire stabilizer-order-2 layer of that profile. It does not close the two remaining stabilizer-order-1 support classes, the full `(2,2,2,2)` profile, the full `p=3` branch, the `k=5` layer, Target C-II, or Erdos Problem #99.

## 1. Support shard

The final two order-two support representatives are

```text
G = {1234,1235,1267,1456},
H = {1234,1235,1267,1467}.
```

The companion verifier enumerates all 38 four-support-set `S_7` orbits, selects the eight classes with setwise stabilizer order two, and then selects exactly `G,H`. Each `(2,2,2,2)` support set has `3^4=81` external cycle choices. Hence these two support orbits cover

```text
2 * (7!/2) * 3^4 = 408240
```

labeled eight-cycle sets. Quotienting the 81 cycle choices by the order-two support stabilizer gives 45 cycle-set orbits for each support class, 90 `S_7` cycle-set representatives in total.

## 2. Necessary survivor conditions

The existing `p=3,m=4` reduction forces exactly three singleton touched root blocks, every other touched root block complete, touched-complete root nullity one, singleton coefficient rank three, and generalized weights

```text
(d1,d2,d3) >= (2,4,5).
```

For `D=-1,d_root=1`, a rank-three singleton coefficient system on eight external cycles has a five-dimensional coefficient nullspace. A survivor therefore requires external relation-rank increment five over the touched complete-root relation span. Untouched complete blocks cannot increase this quotient increment.

## 3. Exact finite census

An independent standalone reconstruction of the current repository's K8 coordinate normal form and the shard verifier logic was executed locally. It gave the following exact counts.

```text
G:
  S7 cycle-set orbits              45
  admissible singleton triples  10440
  singleton-direction states   281880
  coefficient-rank-three       281880
  generalized-weight states     11880
  external increment census {0:11880}
  max relation-row norm^2          34

H:
  S7 cycle-set orbits              45
  admissible singleton triples   9450
  singleton-direction states   255150
  coefficient-rank-three       255150
  generalized-weight states     12150
  external increment census {0:12150}
  max relation-row norm^2          34
```

Aggregate:

```text
S7 cycle-set orbits               90
admissible singleton triples   19890
singleton-direction states    537030
coefficient-rank-three        537030
generalized-weight states      24030
external increment census {0:24030}
```

Every generalized-weight-admissible state has external relation-rank increment zero, whereas a survivor requires increment five. Therefore neither support orbit contains a survivor.

> **Theorem.** In the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(2,2,2,2)` branch, no state exists whose support set lies in the `S_7` orbit of `G` or `H` above.

## 4. Exactness and validation

The support/cycle orbit enumeration, coefficient-rank tests, generalized-weight tests, and coordinate construction in the standalone reconstruction use exact integer/rational arithmetic except for the final relation-rank elimination, which uses the repository prime modulus

```text
P = 2^127 - 1.
```

The maximum squared Euclidean norm of any relation row encountered in this shard is 34. The reconstruction independently checks the Lucas-Lehmer certificate for `P` and

```text
P^2 > 34^15.
```

The existing Hadamard argument therefore certifies that the modular relation ranks equal the corresponding rational ranks; the census is not probabilistic finite-field evidence.

The companion repository wrapper contains assertions for the exact aggregate counts above and the zero-only rank-increment census. It was syntax-checked before upload. The exact wrapper itself was not executed from a checked-out repository during this run; the executed calculation was the independent standalone reconstruction described above.

## 5. Remaining target

Before this run the open `(2,2,2,2)` support layer consisted of

```text
2 stabilizer-order-1 classes,
2 stabilizer-order-2 classes.
```

This theorem removes both remaining order-two classes. The exact remaining `(2,2,2,2)` support bottleneck is therefore

```text
2 stabilizer-order-1 classes.
```

The next bounded finite target is those final two order-one classes. The `(3,2,2,1)` profile remains open on the touched-nullity-four support classes recorded by the current repository. The other unresolved `k=5` arithmetic branches remain

```text
D=-2, (d_root,p)=(0,5),
D=-1, (d_root,p)=(0,6).
```

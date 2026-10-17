> Generated reading edition · [exact source](../../research/target_c_k6_nine_no_root_profile_packet_2026-10-05.md) · source SHA-256 `50aac14d91ad230cbaf879cbfc6380a10d0fcb5a70ffec6c46bb354bfa8b14f6`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "bcd5d227a508cd12b3c50115c2c9df8e7261cd87", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_k6_nine_no_root_profile_packet_2026-10-05.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "d807ce17146eb24534237cdb2dd93ed5700e918db0c53b95c32fc295ff77a1f3"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: nine-no-root k=6 support-profile packet

Date: 2026-10-05
Status: unreviewed finite support reductions; theorem-state authority unchanged.
C-II and Level I remain open.

This packet consolidates the worker-b k=6, nine-no-root support-profile lineage.
The common reductions are conditional on the stated coefficient-space/root-block
hypotheses. The exact m=4 and m=6 slice verifiers were rerun on this salvage branch
and passed. The m=3 slice has a direct incidence proof. Two broader finite censuses
are not reproducible from the source branches: the support-compression census that
claims `3 <= m <= 6`, and the m=5 census. Therefore this packet does not claim the
full p=4 branch is exhausted.

## p=4 profile

Under the branch hypotheses `k=6, D=-2, d_root=1, p=4`, the retained reductions
state that `rank(P)=3`, the generalized weights are at least `(3,4,6)`, exactly
four touched singleton root blocks remain, and there are no touched empty or pair
blocks. The support-compression note reports a finite census restricting the number `m`
of distinct four-vertex supports to `3 <= m <= 6`, but does not include its verifier
source. The range is therefore a candidate reduction, not a reproduced result here.

- **m=3:** each support occurs three times. Each of the four required singleton
  triangles must lie in at least two of the three tetrahedra. Three support pairs
  can account for at most three such triangles, so this slice is impossible.
- **m=4:** the exact verifier exhausts profiles `(3,3,2,1)` and `(3,2,2,2)`.
  It reports external relation-rank increment one for each generalized-weight
  survivor, against the required increment six. The verifier passed here.
- **m=5:** the written audit reports all 824 generalized-weight-admissible states
  have increment zero or one, against the required six. The audit says its exact
  verifier source could not be committed. This census was not reproducible from
  the repository during this salvage, so m=5 remains open in this packet.
- **m=6:** conditional on the cited reduction to two overlap types, the exact
  verifier exhausts the overlap-two and overlap-three types; no
  generalized-weight-admissible overlap-two state survives, and all 432
  overlap-three survivors have increment zero. The verifier passed here.

The durable conclusion is limited to the displayed m=3 incidence argument and
the conditional m=4 and m=6 exact slice censuses. The full p=4 branch remains open
until the support-compression census, the m=5 census, and the common reductions are
reproduced and jointly audited.

## p=5 structural reductions

For `k=6, D=-1, d_root=1, p=5`, the quotient-basis and triple-deletion notes give
proof-level restrictions. They reduce the incomplete root profiles to three
singletons plus one pair, or five singletons; bound the support families by
triangle-boundary nullity; and show at least 19 of 84 triple deletions retain the
specified six-row profile (at least 20 in the exceptional-pair case). The stated
next finite target is the six-row class and its simultaneous extension
multiplicity.

The accompanying support-orbit census reports exact counts through `m=8`, but
its verifier source was also not retained. Those numerical counts are recorded as
unreproduced research evidence, not as a certified premise. The p=5 branch remains
open.

## Exact checks

```text
python3 research/verify_target_c_nine_noroot_k6_dminus2_d1p4_m4_closure_2026_10_04.py
python3 research/verify_target_c_nine_noroot_k6_dminus2_d1p4_m6_closure_2026_10_03.py
```

Both passed on this branch. They certify their encoded finite support/root
censuses and exact relation-rank checks under the stated inputs. They do not prove
the common structural reductions, the m=5 audit, the p=5 uncommitted census, C-II,
or Level I.

## Source branches audited in this consolidation

| Branch | Audited tip SHA |
|---|---|
| `worker-b/nine-noroot-k6-d0-e3-m3-m5-closure-2026-10-03` | `5e7766f70781c655d201416efd54e5c310b06c0a` |
| `worker-b/nine-noroot-k6-d0-e3-m4-closure-2026-10-03` | `5e7766f70781c655d201416efd54e5c310b06c0a` |
| `worker-b/nine-noroot-k6-d0-minimal-empty-closure-2026-10-03` | `5e7766f70781c655d201416efd54e5c310b06c0a` |
| `worker-b/nine-noroot-k6-deletion-reduction-2026-10-03-v2` | `dd4cadc446f1503efe0c103ef48a669b61a149b3` |
| `worker-b/nine-noroot-k6-depth2-sync-2026-10-03` | `54d4bbfc8a29417c61979fa2d01239b6b80d4d04` |
| `worker-b/nine-noroot-k6-depth3-sync-2026-10-03` | `900ccf4eee8477281673a78396c876ad20afdfce` |
| `worker-b/nine-noroot-k6-p4-m3-touch-count-closure-2026-10-04` | `faa48e03c649b259f4e1daf6a0e03d445102b510` |
| `worker-b/nine-noroot-k6-p4-m4-closure-2026-10-03` | `b1b83ac3c382e9b8d79815cf520f001a046fc6ad` |
| `worker-b/nine-noroot-k6-p4-m4-reproducible-closure-2026-10-04` | `f7addda0b924915ab62b9158fef1ea5cdf2c1b36` |
| `worker-b/nine-noroot-k6-p4-m45-reproducible-closure-2026-10-04` | `f7addda0b924915ab62b9158fef1ea5cdf2c1b36` |
| `worker-b/nine-noroot-k6-p4-m5-33111-weight-closure-2026-10-03` | `cb28457ca3bb239289449440bfeab76d42917b76` |
| `worker-b/nine-noroot-k6-p4-m5-exact-audit-2026-10-04` | `5d474b9e7133d07c28976334f66ccd0e6105b70f` |
| `worker-b/nine-noroot-k6-p4-m5-full-closure-repair-2026-10-03` | `0fa5337ccd85bd80549444af614ff31a1dd18d0f` |
| `worker-b/nine-noroot-k6-p4-m5-reproducible-closure-2026-10-04` | `5d474b9e7133d07c28976334f66ccd0e6105b70f` |
| `worker-b/nine-noroot-k6-p4-m5-reproducible-v2-2026-10-04` | `01b58b11d0600a24ce13d776ec266d0f340f74df` |
| `worker-b/nine-noroot-k6-p4-m6-closure-2026-10-03` | `cb47d562f3e36cf2c6eb03a24188426ef87979ee` |
| `worker-b/nine-noroot-k6-p4-m6-exact-closure-2026-10-03` | `8a5edc378d5802759da544f052a0125cd2f4f3f1` |
| `worker-b/nine-noroot-k6-p4-m6-exact-closure-2026-10-03-v2` | `8b6774a1de70277c88bbebf48772a49a32b5dba5` |
| `worker-b/nine-noroot-k6-p4-support-compression-2026-10-03-v2` | `cb47d562f3e36cf2c6eb03a24188426ef87979ee` |
| `worker-b/nine-noroot-k6-p5-quotient-basis-cover-2026-10-04` | `8203da01948d9a0bba7675d2c1b20c17dbd53909` |
| `worker-b/nine-noroot-k6-p5-triple-sync-2026-10-04` | `31b8d18e0f06ba5620801c75613b2db41b787e8b` |
| `worker-b/nine-noroot-k6-singleton-generator-reduction-2026-10-03` | `5e7766f70781c655d201416efd54e5c310b06c0a` |

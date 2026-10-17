# Target C: close the sixth order-2 `(3,2,2,1)` support orbit in the `p=3,m=4` branch

Date: 2026-09-24

Status: exact finite closure of the stabilizer-order-2 support orbit represented by `{1234,1235,1246,3567}` in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(3,2,2,1)` branch, conditional on the structural reductions already proved in the repository. This does not close the full profile, the full `p=3` branch, the `k=5` layer, Target C-II, or Erdos Problem #99.

## Support orbit

The support stabilizer has order two. The exact orbit catalog gives 177 `S_7` cycle-set representatives and `(7!/2)*324 = 816480` labeled eight-cycle sets. Every representative touches the same 14 root blocks. The complete touched-root family has exact rank 10 and nullity 4. Exactly 208 choices of three touched root blocks leave the remaining complete-root family with nullity one.

The existing reduction requires three singleton blocks, singleton coefficient rank three, generalized weights at least `(2,4,5)`, and external relation-rank increment five.

## Exact finite census

The 177 representatives were split into three disjoint intervals.

```text
[0,59):
  admissible singleton triples    12272
  singleton-direction states     331344
  coefficient-rank-three states  257478
  generalized-weight states       18116
  external increment census   {0:18116}
  max relation-row norm^2             70

[59,118):
  admissible singleton triples    12272
  singleton-direction states     331344
  coefficient-rank-three states  256917
  generalized-weight states       17084
  external increment census   {0:17084}
  max relation-row norm^2             70

[118,177):
  admissible singleton triples    12272
  singleton-direction states     331344
  coefficient-rank-three states  271507
  generalized-weight states       20396
  external increment census   {0:20396}
  max relation-row norm^2             70
```

Aggregate totals are 36,816 admissible singleton triples, 994,032 singleton-direction states, 785,902 coefficient-rank-three states, and 55,596 generalized-weight-admissible states. Every final state has external relation-rank increment zero, whereas survival requires increment five. Therefore this support orbit is empty.

## Exactness and validation

The finite census above was executed in a standalone reconstruction of the current repository coordinate model using the exact integer/rational formulas from the current-main base and `(3,3,1,1)` parent verifiers. As an implementation control, the same reconstruction reproduced the current-main fourth order-2 certificate on interval `[0,55)` exactly: 11,440 singleton triples, 308,880 direction states, 239,408 rank-three states, 16,534 generalized-weight states, increment census `{0:16534}`, and maximum squared relation-row norm 70.

Ranks of the final relation rows were computed modulo `P=2^127-1`. Lucas-Lehmer passed, the maximum squared relation-row norm was 70, and `P^2 > 70^15`, so the repository's Hadamard argument certifies the modular ranks over `Q`.

The companion verifier is a small wrapper around the exact shard-E engine. It changes only `TARGET`; the parent engine still reconstructs the selected support orbit and independently checks stabilizer order, orbit count, touched-root nullity, admissible singleton count, the full three-shard census, zero-only external rank increments, Lucas-Lehmer, and the Hadamard bound. The wrapper itself was not executed from a repository checkout during this run; the executed evidence is the standalone reconstruction described above.

## Remaining target

After this closure, two stabilizer-order-2 and two stabilizer-order-1 touched-nullity-four `(3,2,2,1)` support classes remain.

The next order-2 representative is `{1234,1235,1267,1456}`, with 168 `S_7` cycle-set representatives, 15 touched root blocks, touched-root rank 11/nullity 4, and 232 admissible singleton triples per representative. The final order-2 representative is `{1234,1235,1267,1467}`, with 198 representatives, 14 touched blocks, rank 10/nullity 4, and 210 admissible singleton triples per representative.

The two remaining stabilizer-order-1 representatives are `{1234,1235,1246,1367}` and `{1234,1235,1456,2467}`.

The other unresolved `k=5` arithmetic branches remain `D=-2,(d_root,p)=(0,5)` and `D=-1,(d_root,p)=(0,6)`.

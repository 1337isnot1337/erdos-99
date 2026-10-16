# Target C: middle-third certificate for the final order-1 `(3,2,2,1)` support class

Date: 2026-09-25

Status: exact finite partial closure of representatives `108..215` of the 324 fixed-support cycle-set representatives for

```text
{1234,1235,1456,2467}
```

in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(3,2,2,1)` branch, conditional on the structural reductions already proved in the repository. Combined with the parent first-third certificate, representatives `0..215` are excluded. This does not close representatives `216..323`, the full `p=3` branch, Target C-II, or Erdos Problem #99.

## Global support data

The support stabilizer is trivial. Hence the class has 324 fixed-support cycle-set representatives and `5040*324 = 1632960` labeled cycle sets.

Every representative touches 15 root blocks. The complete touched-root family has exact rank 11 and nullity 4. Exactly 232 choices of three singleton blocks leave the remaining complete-root family with nullity one.

## Executed finite census

The middle 108 representatives were split into six disjoint 18-representative subshards:

```text
[108,126):  4176  112752   86508  3780  {0:3780}  maxnorm^2=36
[126,144):  4176  112752   86796  4500  {0:4500}  maxnorm^2=36
[144,162):  4176  112752   84888  3672  {0:3672}  maxnorm^2=36
[162,180):  4176  112752   86652  3924  {0:3924}  maxnorm^2=36
[180,198):  4176  112752   88704  4896  {0:4896}  maxnorm^2=36
[198,216):  4176  112752   88416  4608  {0:4608}  maxnorm^2=36
```

The numeric columns are admissible singleton triples, singleton-direction states, coefficient-rank-three states, generalized-weight-admissible states, and the external relation-rank increment census.

Aggregate over representatives `108..215`:

```text
admissible singleton triples       25056
singleton-direction states        676512
coefficient-rank-three states     521964
generalized-weight states          25380
external increment census      {0:25380}
```

All 25,380 generalized-weight-admissible states have external relation-rank increment zero. The established branch reduction requires increment five. Therefore no survivor occurs among representatives `108..215`.

Ranks were computed modulo `P=2^127-1`. Lucas-Lehmer passed. The maximum squared relation-row norm in these subshards is 36, and `P^2 > 36^15`, so the repository's Hadamard argument certifies the modular rank decisions over `Q`.

The computation used a self-contained exact reconstruction of the current-main coordinate formulas. As a control, the same reconstruction re-ran `[0,18)` and reproduced the parent certificate exactly:

```text
[0,18): 4176 112752 84888 4104 {0:4104} maxnorm^2=36
```

No sampling or heuristic pruning is used in this certificate.

## Remaining bottleneck

For this support class, only representatives `216..323` remain unchecked after combining this certificate with its parent first-third certificate.

Across existing certificate branches, the other order-1 support class `{1234,1235,1246,1367}` is already closed, and the final order-2 class `{1234,1235,1267,1467}` has an exact certificate. Those branch results are not assumed to be on authoritative `main`.

The other unresolved `k=5` arithmetic branches remain `D=-2,(d_root,p)=(0,5)` and `D=-1,(d_root,p)=(0,6)`.

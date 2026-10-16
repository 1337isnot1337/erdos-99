# Target C: close the third order-2 `(3,2,2,1)` support orbit in the `p=3,m=4` branch

Date: 2026-09-24

Status: exact finite closure of one of the eight touched-nullity-four stabilizer-order-2 support-set `S_7` orbits in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(3,2,2,1)` branch. This does not close the full `(3,2,2,1)` profile, the full `p=3` branch, the `k=5` layer, Target C-II, or Erdos Problem #99.

## 1. Support orbit

The support representative is

```text
C = {1234,1235,1246,1357}.
```

Its support stabilizer has order two. For `(3,2,2,1)` there are 324 cycle choices on a fixed four-support set, so this support orbit contains

```text
(7!/2) * 324 = 816480
```

labeled eight-cycle sets. Quotienting the 324 choices by the order-two support stabilizer gives 162 `S_7` cycle-set representatives.

Every representative touches the same 13 root blocks. The complete touched-root row family has exact rank 9, hence nullity 4. Exactly 186 choices of three touched root blocks leave the remaining complete-root family with nullity one.

The support orbit is distinct from the previously closed order-two representatives `{1234,1235,1245,1346}` and `{1234,1235,1246,1356}`; all three occur as different representatives in the exact four-support `S_7` orbit catalog.

## 2. Necessary survivor conditions

The existing `p=3,m=4` reduction forces exactly three singleton touched root blocks, all remaining touched root blocks complete, singleton coefficient rank three, and generalized weights

```text
(d1,d2,d3) >= (2,4,5).
```

For `D=-1,d_root=1`, the coefficient constraint space has rank three on eight external cycles, hence a five-dimensional coefficient nullspace. All five external relations must survive independently modulo the complete-root relation span. Thus any survivor requires external relation-rank increment five.

## 3. Exact finite census

The 162 cycle-set representatives were split into three disjoint intervals:

```text
[0,54):
  admissible singleton triples    10044
  singleton-direction states     271188
  coefficient-rank-three states  216260
  generalized-weight states       20506
  external increment census   {0:20506}
  max relation-row norm^2             70

[54,108):
  admissible singleton triples    10044
  singleton-direction states     271188
  coefficient-rank-three states  220572
  generalized-weight states       21062
  external increment census   {0:21062}
  max relation-row norm^2             70

[108,162):
  admissible singleton triples    10044
  singleton-direction states     271188
  coefficient-rank-three states  222975
  generalized-weight states       22018
  external increment census   {0:22018}
  max relation-row norm^2             70
```

The aggregate census is

```text
S7 cycle-set representatives       162
admissible singleton triples     30132
singleton-direction states      813564
coefficient-rank-three states   659807
generalized-weight states        63586
external increment census    {0:63586}
```

Every generalized-weight-admissible state has external relation-rank increment zero, not five. Therefore this entire support orbit is empty.

> **Theorem.** In the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(3,2,2,1)` branch, no state exists whose four-support set lies in the `S_7` orbit of `{1234,1235,1246,1357}`.

## 4. Exactness and validation

All coefficient and generalized-weight calculations are exact integer/rational arithmetic. Relation rows are integral and ranked modulo

```text
P = 2^127 - 1.
```

Lucas-Lehmer verifies that `P` is prime. The largest squared Euclidean norm of any relation row in this census is 70, and

```text
P^2 > 70^15.
```

The repository's existing Hadamard argument therefore rules out modular rank loss in the relevant minors, so the recorded ranks equal their ranks over `Q`.

The companion verifier was executed end-to-end for all three disjoint shards in a local runtime using the exact current-main coordinate definitions needed by this verifier, fetched through the GitHub connector. Each shard passed its hard-coded census, zero-increment assertion, Lucas-Lehmer check, and Hadamard bound. The verifier source has local SHA-256

```text
2e318f367045a9cfd36fca1f1aeb553419f1e6849512471fbf331f2d7273fdcb
```

and Git blob SHA `f03eeb2304517356c705f358a80cd575ee9cf377`.

## 5. Remaining target

With the first two order-two support closures already on `main`, this theorem removes a third order-two class. The exact remaining touched-nullity-four `(3,2,2,1)` support bottleneck is therefore

```text
2 stabilizer-order-1 classes,
5 stabilizer-order-2 classes,
```

for seven support-set orbits total.

The next bounded order-two target in the exact orbit catalog is

```text
{1234,1235,1246,1567},
```

which has 165 `S_7` cycle-set representatives, 14 touched root blocks, touched-root rank 10/nullity 4, and 208 admissible singleton triples per representative before direction filtering.

The other unresolved `k=5` arithmetic branches remain

```text
D=-2, (d_root,p)=(0,5),
D=-1, (d_root,p)=(0,6).
```

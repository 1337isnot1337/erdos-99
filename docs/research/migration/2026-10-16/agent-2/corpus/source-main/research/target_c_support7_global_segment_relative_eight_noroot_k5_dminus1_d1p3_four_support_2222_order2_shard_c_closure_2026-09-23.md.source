# Target C: close two more order-2 `(2,2,2,2)` support orbits in the `p=3,m=4` branch

Date: 2026-09-23

Status: exact finite closure of two further stabilizer-order-2 support-set `S_7` orbits in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(2,2,2,2)` branch. This does not close the full `(2,2,2,2)` profile, the full `p=3` branch, the `k=5` layer, Target C-II, or Erdos Problem #99.

## 1. Support shard

The two support representatives are

```text
E = {1234,1235,1246,3457},
F = {1234,1235,1246,3567}.
```

The companion verifier enumerates all 38 four-support-set `S_7` orbits, selects the eight classes with setwise stabilizer order two, and then selects exactly `E,F`. Each `(2,2,2,2)` support set has `3^4=81` external cycle choices. Hence these two support orbits cover

```text
2 * (7!/2) * 3^4 = 408240
```

labeled eight-cycle sets. Quotienting the 81 cycle choices by the order-two support stabilizer gives 42 cycle-set orbits for each support class, 84 `S_7` cycle-set representatives in total.

## 2. Necessary survivor conditions

The existing `p=3,m=4` reduction forces exactly three singleton touched root blocks, every other touched root block complete, touched-complete root nullity one, singleton coefficient rank three, and generalized weights

```text
(d1,d2,d3) >= (2,4,5).
```

For `D=-1,d_root=1`, a rank-three singleton coefficient system on eight external cycles has a five-dimensional coefficient nullspace. A survivor therefore requires external relation-rank increment five over the touched complete-root relation span. Untouched complete blocks cannot increase this quotient increment.

## 3. Exact finite census

The verifier gives the following exact counts for each support class:

```text
E:
  S7 cycle-set orbits              42
  admissible singleton triples   8736
  singleton-direction states   235872
  coefficient-rank-three       235872
  generalized-weight states     12336
  external increment census {0:12336}
  max relation-row norm^2          70

F:
  S7 cycle-set orbits              42
  admissible singleton triples   8736
  singleton-direction states   235872
  coefficient-rank-three       235872
  generalized-weight states     12336
  external increment census {0:12336}
  max relation-row norm^2          70
```

Aggregate:

```text
S7 cycle-set orbits               84
admissible singleton triples   17472
singleton-direction states    471744
coefficient-rank-three        471744
generalized-weight states      24672
external increment census {0:24672}
```

Every generalized-weight-admissible state has external relation-rank increment zero, whereas a survivor requires increment five. Therefore neither support orbit contains a survivor.

> **Theorem.** In the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(2,2,2,2)` branch, no state exists whose support set lies in the `S_7` orbit of `E` or `F` above.

## 4. Exactness and validation

The support/cycle orbit enumeration, coefficient-rank tests, generalized-weight tests, and relation-rank census were executed with exact integer/rational arithmetic except for the final relation-rank elimination, which uses the repository's prime modulus

```text
P = 2^127 - 1.
```

The maximum squared Euclidean norm of any relation row encountered is 70. The verifier checks the repository Lucas-Lehmer certificate for `P` and

```text
P^2 > 70^15.
```

The existing Hadamard argument therefore certifies that the modular relation ranks equal the corresponding rational ranks; the census is not probabilistic finite-field evidence.

For local validation, the current repository coordinate construction and the functions used by this shard were reconstructed directly from current `main`. That reconstruction first reproduced the preceding shard-B certificate exactly:

```text
17106 admissible singleton triples,
461862 direction states,
27078 generalized-weight states,
external increment census {0:27078},
max relation-row norm^2 70.
```

The shard-C verifier was then executed end-to-end locally and produced the aggregate counts above, including `external increment census {0:24672}`. The exact source subsequently written to `main` was fetched back and inspected.

## 5. Remaining target

Before this run the open `(2,2,2,2)` support layer consisted of

```text
2 stabilizer-order-1 classes,
4 stabilizer-order-2 classes.
```

This theorem removes two of the four order-two classes. The exact remaining `(2,2,2,2)` support bottleneck is therefore

```text
2 stabilizer-order-1 classes,
2 stabilizer-order-2 classes,
```

for four support-set orbits total.

The two remaining order-two representatives are

```text
{1234,1235,1267,1456},
{1234,1235,1267,1467}.
```

The `(3,2,2,1)` profile remains open on the 35 touched-nullity-four support classes. The other unresolved `k=5` arithmetic branches remain

```text
D=-2, (d_root,p)=(0,5),
D=-1, (d_root,p)=(0,6).
```

The next bounded finite target is the final two stabilizer-order-2 `(2,2,2,2)` support classes.
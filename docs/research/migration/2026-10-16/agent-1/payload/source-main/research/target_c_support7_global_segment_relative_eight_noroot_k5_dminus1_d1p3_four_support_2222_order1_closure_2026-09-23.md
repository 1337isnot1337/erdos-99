# Target C: close the final two order-1 `(2,2,2,2)` support orbits in the `p=3,m=4` branch

Date: 2026-09-23

Status: exact finite closure of the final two support-set `S_7` orbits in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(2,2,2,2)` branch. Together with the existing stabilizer-layer certificates, this closes the full `(2,2,2,2)` profile. It does not close the `(3,2,2,1)` profile, the full `p=3` branch, the `k=5` layer, Target C-II, or Erdos Problem #99.

## 1. Final support classes

The two remaining support-set orbits have trivial setwise stabilizer and representatives

```text
I = {1234,1235,1246,1367},
J = {1234,1235,1456,2467}.
```

The complete four-support catalog has exactly two stabilizer-order-1 classes. The companion verifier re-enumerates all 38 support-set `S_7` orbits, selects exactly these two classes, and checks that their stabilizers are trivial.

Each support has `3^4=81` `(2,2,2,2)` external cycle choices. Because the support stabilizer is trivial, all 81 choices are distinct cycle-set orbits over that fixed support representative. Hence this shard contains

```text
162 S_7 cycle-set representatives
```

and covers

```text
2 * 7! * 3^4 = 816480
```

labeled eight-cycle sets.

## 2. Necessary survivor conditions

The existing `p=3,m=4` reduction forces exactly three singleton touched root blocks, every other touched root block complete, touched-complete root nullity one, singleton coefficient rank three, and generalized weights

```text
(d1,d2,d3) >= (2,4,5).
```

For `D=-1,d_root=1`, a rank-three singleton coefficient system on eight external cycles has a five-dimensional coefficient nullspace. A surviving state must therefore contribute external relation-rank increment five over the touched complete-root relation span. Untouched complete blocks cannot increase this quotient increment.

## 3. Exact finite census

A standalone reconstruction of the current repository K8 coordinate normal form and the verifier logic was executed locally for each support class separately.

For `I`:

```text
S_7 cycle-set orbits               81
admissible singleton triples    16848
singleton-direction states     454896
coefficient-rank-three         454896
generalized-weight states       23808
external increment census   {0:23808}
max relation-row norm^2             70
```

For `J`:

```text
S_7 cycle-set orbits               81
admissible singleton triples    18792
singleton-direction states     507384
coefficient-rank-three         507384
generalized-weight states       21384
external increment census   {0:21384}
max relation-row norm^2             36
```

Aggregate:

```text
S_7 cycle-set orbits              162
admissible singleton triples    35640
singleton-direction states     962280
coefficient-rank-three         962280
generalized-weight states       45192
external increment census   {0:45192}
max relation-row norm^2             70
```

Every generalized-weight-admissible state has external relation-rank increment zero, whereas a survivor requires increment five. Therefore neither final support class contains a survivor.

> **Theorem.** In the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4` branch, the `(2,2,2,2)` multiplicity profile is empty.

## 4. Exactness

The support enumeration, coefficient-rank tests, generalized-weight tests, and coordinate construction use exact integer/rational arithmetic except for the final relation-rank elimination, which uses

```text
P = 2^127 - 1.
```

The standalone reconstruction independently checks the Lucas-Lehmer certificate for `P`. The maximum squared Euclidean norm of any relation row in this shard is 70, and

```text
P^2 > 70^15.
```

The existing Hadamard argument therefore certifies the modular relation ranks as the corresponding rational ranks. The zero-only increment census is an exact finite certificate, not probabilistic finite-field evidence.

The committed repository wrapper asserts the support representatives, the two 81-orbit counts, all aggregate census values, the zero-only increment census, and the Hadamard bound. It was syntax-checked before upload. That exact wrapper was not executed from a checked-out repository during this run; the executed calculation was the independent standalone reconstruction described above.

## 5. Why this closes the whole `(2,2,2,2)` profile

The exact support catalog partitions the 38 four-support-set orbits by stabilizer order as

```text
1^2, 2^8, 4^12, 6^2, 8^5, 12^2, 16^2, 24^2, 36^1, 48^1, 144^1.
```

The repository now has exact certificates closing:

```text
orders >=16: 7 classes,
orders 8,12: 7 classes,
order 6:      2 classes,
order 4:     12 classes,
order 2:      8 classes,
order 1:      2 classes.
```

These counts sum to all 38 support classes. Thus no `(2,2,2,2)` support geometry remains.

## 6. Remaining target

The immediate `p=3,m=4` bottleneck is now the `(3,2,2,1)` profile on the 35 touched-nullity-four support classes recorded by the current support catalog. The `(3,3,1,1)` profile is already closed elsewhere in the repository.

The other unresolved `k=5` arithmetic branches remain

```text
D=-2, (d_root,p)=(0,5),
D=-1, (d_root,p)=(0,6).
```

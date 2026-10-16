# Target C: close four order-4 `(2,2,2,2)` support orbits in the `p=3,m=4` branch

Date: 2026-09-23

Status: exact finite closure of four explicitly listed support-set `S_7` orbits in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(2,2,2,2)` branch. This is a shard closure only. It does not close the full `(2,2,2,2)` profile, the full `p=3` branch, the `k=5` layer, Target C-II, or Erdos Problem #99.

Inputs:

- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_three_singleton_basis_reduction_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_tetrahedral_support_compression_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_nullity_catalog_2026-09-23.md`;
- the preceding exact `(2,2,2,2)` high/intermediate/order-6 shard verifiers;
- the companion verifier committed with this note.

## 1. Shard definition

The support-nullity catalog gives 12 support-set orbits of stabilizer order four. One is the already-closed nullity-five hidden-tetrahedron class. This run attacks the following four nullity-four classes:

```text
A1 = {1234,1235,1236,1245},
A2 = {1234,1235,1236,1247},
A3 = {1234,1235,1236,1457},
A4 = {1234,1235,1245,1367}.
```

Each support set has `S_7` stabilizer order four. In the `(2,2,2,2)` profile, every support contributes exactly two of its three no-root four-cycle orientations, so there are `3^4=81` cycle choices per labeled support set.

Each support orbit therefore contains

```text
(7!/4) * 3^4 = 102060
```

labeled eight-cycle sets. The four classes together cover

```text
408240
```

labeled eight-cycle sets. Exact quotienting by the support stabilizers leaves

```text
107
```

`S_7` cycle-set orbit representatives.

## 2. Structural filters reused

For every surviving state in this arithmetic branch, the previous proof-level reductions force:

- exactly three singleton touched root blocks;
- every other touched root block complete;
- touched-complete root nullity exactly one in the `m=4` case;
- singleton coefficient rank three;
- generalized weights

```text
(d1,d2,d3) >= (2,4,5).
```

The arithmetic identity for `D=-1,d_root=1,p=3` then requires all five dimensions of the coefficient nullspace to survive independently modulo the complete-root relation span. Equivalently, the external relation-rank increment over the touched complete-root span must equal five.

Thus a state is impossible if its exact external increment is smaller than five. Untouched complete blocks cannot increase this quotient increment, so the test is completion-independent.

## 3. Exact census

Across the 107 cycle-set orbit representatives, the verifier enumerates every three-element singleton subset of the touched root blocks and keeps only those for which the remaining touched complete-root rows have nullity exactly one.

The exact counts are:

```text
admissible singleton triples: 18990
singleton-direction states:   512730
coefficient-rank-three states: 512730
generalized-weight states:     36286
```

For every one of the 36286 states satisfying all structural filters, the external relation-rank increment is

```text
0.
```

The complete increment census is therefore

```text
{0: 36286}.
```

But a survivor requires increment five. Hence no state in any of `A1,A2,A3,A4` survives.

> **Theorem.** In the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(2,2,2,2)` branch, no state whose four support set lies in the `S_7` orbit of `A1`, `A2`, `A3`, or `A4` exists.

## 4. Exactness of the rank certificate

The verifier uses integer relation rows and computes their ranks modulo

```text
P = 2^127 - 1.
```

The largest squared Euclidean norm of any relation row encountered is

```text
70.
```

The verifier checks both the Lucas-Lehmer primality certificate for `P` and the Hadamard inequality

```text
P^2 > 70^15.
```

Therefore any nonzero rational minor relevant to the rank computation has absolute determinant strictly below `P^2`; modular rank loss at the prime `P` is impossible for the rank range used here. The reported relation ranks are exact over `Q`, not probabilistic finite-field evidence.

The coefficient-rank-three test uses exact integer `3 x 3` minors, and the generalized-weight computation is exact integer arithmetic.

## 5. Validation performed in this run

A standalone reconstruction of the repository K8 coordinate normal form and the same shard enumeration was executed locally. It reproduced:

```text
support-set orbits:             4
labeled cycle sets:             408240
S_7 cycle-set orbits:           107
admissible singleton triples:   18990
singleton-direction states:     512730
coefficient-rank-three states:  512730
generalized-weight states:      36286
external increment census:      {0: 36286}
maximum relation-row norm^2:    70
```

The local run also independently checked the Lucas-Lehmer residue `0` for `2^127-1` and `P^2 > 70^15`.

The committed companion wrapper was syntax-checked before upload. It was not itself executed from a checked-out repository during this run; the executed computation was the standalone reconstruction described above.

## 6. Remaining target

Before this run, the still-open low-symmetry `(2,2,2,2)` support classes consisted of

```text
2 stabilizer-order-1 classes,
8 stabilizer-order-2 classes,
11 stabilizer-order-4 classes.
```

This theorem removes four of the order-four classes. The remaining `(2,2,2,2)` support-level bottleneck is therefore

```text
2 order-1 classes,
8 order-2 classes,
7 order-4 classes,
```

for 17 support-set orbits total.

The `(3,2,2,1)` profile remains open on the 35 support classes with touched nullity four. The other unresolved `k=5` arithmetic branches remain

```text
D=-2, (d_root,p)=(0,5),
D=-1, (d_root,p)=(0,6).
```

The direct next target is another bounded external-rank-increment shard among the 17 remaining `(2,2,2,2)` support classes, preferably an order-four group large enough to amortize the exact verifier cost.

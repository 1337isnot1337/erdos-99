# Target C: complete four-support nullity classification in the `p=3,m=4` branch

Date: 2026-09-23

Status: exact finite classification of the support-level nullity obstruction in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4` branch. It eliminates two additional support-set `S_7` orbits from the still-open `(3,2,2,1)` profile. It also proves that this particular support-nullity argument cannot eliminate any of the other 35 four-support orbits. It does not close `(3,2,2,1)`, `(2,2,2,2)`, the full `p=3` branch, the `k=5` layer, Target C-II, or Erdos Problem #99.

Inputs:

- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_three_singleton_basis_reduction_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_tetrahedral_support_compression_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_hidden_tetrahedron_obstruction_2026-09-23.md`;
- the exact finite verifier committed with this note.

## 1. Necessary support-nullity condition

Every surviving `m=4` state has exactly three singleton touched root blocks. If `T` is the touched root-block set and `S subset T` is the three-element singleton set, the prior reduction requires

```text
nullity H(T \ S) <= 1.
```

Deleting three rows lowers row nullity by at most three, so

```text
nullity H(T \ S) >= nullity H(T) - 3.
```

Therefore every support set with

```text
nullity H(T) >= 5
```

is impossible, independently of four-cycle orientations and independently of whether the multiplicity profile is `(3,2,2,1)` or `(2,2,2,2)`.

The previous hidden-tetrahedron note applied this criterion to one order-4 support orbit. The missing question was whether that orbit was exceptional or represented a larger support class.

## 2. Complete `S_7` support census

There are

```text
C(35,4) = 52360
```

labeled four-element sets of tetrahedral supports on seven vertices. Exact quotienting by `S_7` gives 38 support-set orbits, with stabilizer-order distribution

```text
1^2, 2^8, 4^12, 6^2, 8^5, 12^2, 16^2, 24^2, 36^1, 48^1, 144^1.
```

For every orbit representative the verifier forms the union `T` of the touched triangles and computes the rank of the ordinary triangle-to-edge boundary matrix over `Q`. The complete nullity distribution is

```text
nullity 4 : 35 support orbits
nullity 5 :  3 support orbits.
```

The three nullity-5 representatives are

```text
A = {1234,1235,1456,2457},  |Stab(A)| = 4,
B = {1234,1235,1456,2456},  |Stab(B)| = 8,
C = {1234,1235,1245,3456},  |Stab(C)| = 12.
```

For every triple of deleted touched rows, the exact minimum complement nullity is

```text
2
```

for `A`, `B`, and `C`. Their complete complement-nullity censuses are

```text
A: {2: 350, 3: 103, 4: 2},
B: {2: 306, 3: 58},
C: {2: 248, 3: 37, 4: 1}.
```

Thus all three support orbits are impossible in the `p=3,m=4` branch.

For each of the other 35 support orbits, full touched nullity is exactly four and there exists at least one three-row deletion for which

```text
nullity H(T \ S) = 1.
```

Hence the row-deletion inequality alone is sharp there and gives no contradiction. This exhausts the pure support-nullity route: further closure of those 35 support orbits must use additional structure such as the singleton coefficient code or the external-rank-increment obstruction.

## 3. New consequence for `(3,2,2,1)`

Orbit `A` is exactly the order-4 hidden-tetrahedron class already eliminated by the previous theorem. The classification adds the order-8 class `B` and order-12 class `C` without any cycle-direction computation.

For `(3,2,2,1)`, quotienting the 324 cycle choices on each support set by the corresponding support stabilizer gives

```text
A: 84 S_7 cycle-set orbits, 408240 labeled cycle sets,
B: 42 S_7 cycle-set orbits, 204120 labeled cycle sets,
C: 34 S_7 cycle-set orbits, 136080 labeled cycle sets.
```

Therefore the complete nullity-5 classification removes

```text
160 S_7 cycle-set orbits
748440 labeled cycle sets
```

from `(3,2,2,1)`. Relative to the already-committed order-4 hidden-tetrahedron theorem, this run newly removes

```text
76 S_7 cycle-set orbits
340200 labeled cycle sets.
```

> **Theorem.** No surviving `(3,2,2,1)` state can have support set in the `S_7` orbit of `B` or `C` above.

The proof is support-level: both classes have touched nullity five, so every possible choice of three singleton blocks leaves complete-root nullity at least two, contradicting the necessary `m=4` nullity-one condition.

## 4. Relation to the `(2,2,2,2)` certificates

The same support-nullity theorem applies to `(2,2,2,2)`. The three exceptional support classes contain

```text
49 S_7 cycle-set orbits
187110 labeled cycle sets
```

in that profile. The order-8 and order-12 classes were already included in the broader exact intermediate-symmetry `(2,2,2,2)` certificate, so this classification is not a new closure claim for those states. Its value there is explanatory: two pieces of the intermediate-symmetry computation admit a shorter support-level proof.

## 5. Exact certificate

The companion verifier is

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_nullity_catalog_2026_09_23.py`.

It uses exact `Fraction` Gaussian elimination throughout. It independently checks:

```text
support-set orbits: 38,
stabilizer distribution: {1:2,2:8,4:12,6:2,8:5,12:2,16:2,24:2,36:1,48:1,144:1},
touched-nullity distribution: {4:35,5:3},
minimum three-deletion complement-nullity distribution: {1:35,2:3},
nullity-5 support stabilizers: {4,8,12},
(3,2,2,1) nullity-5 cycle-set orbits: 160,
(3,2,2,1) nullity-5 labeled cycle sets: 748440,
new beyond the prior order-4 theorem: 76 orbits / 340200 labeled cycle sets.
```

The committed source was syntax-checked and the full certificate was executed locally. All assertions passed.

## 6. Remaining target

The support-nullity obstruction is now exhausted for four-support states. The remaining `(3,2,2,1)` work lies on support orbits with touched nullity four; the remaining `(2,2,2,2)` work lies among its still-unclosed low-symmetry support orbits after the existing high/intermediate symmetry and hidden-tetrahedron closures.

The next direct finite target remains the completion-independent external-rank-increment test on those nullity-four states. The other unresolved `k=5` arithmetic branches remain

```text
D=-2, (d_root,p)=(0,5),
D=-1, (d_root,p)=(0,6).
```

No theorem-state authority file is changed by this note.

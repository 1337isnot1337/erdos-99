# Target C: close the five-support branch in the eight-no-root `k=5,D=-1,d_root=1,p=3` state

Date: 2026-09-23

Status: exact finite closure of the `m=5` subbranch of the remaining three-singleton-basis state. This does **not** close the `m=3` or `m=4` subbranches, the full `k=5` layer, Target C-II, or Erdos Problem #99.

Inputs:

- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_three_singleton_basis_reduction_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_tetrahedral_support_compression_2026-09-23.md`;
- the exact K8 normal form in `research/verify_target_c_support7_global_segment_relative_four_noroot_k2_2026_09_20.py`.

The preceding support-compression note proves that if five distinct four-vertex supports occur, then they are exactly the five tetrahedral faces of one five-vertex set `W`. It also proves that the three singleton root blocks are three triangles of `W` which do not all contain a common edge.

## 1. The root deficiency is already saturated on the touched five-vertex complex

In the `m=5` case, every triangle of `W` is touched. Thus the touched root blocks are

```text
T = binom(W,3),
|T|=10.
```

There are exactly three singleton blocks `S`, and every block in

```text
C_touch = T \ S
```

is complete. The preceding five-support classification proves that the seven triangle-boundary rows in `C_touch` have rank six whenever the three singleton triangles do not share a common edge. Therefore

```text
|C_touch| - rank H(C_touch) = 7-6 = 1.
```

So the branch parameter `d_root=1` is already attained by the touched complete blocks alone.

Any additional untouched complete block can only enlarge the root relation span. It cannot create new external relation directions, because every no-root cycle has zero local quotient component at an untouched block.

## 2. What `D=-1` would require

Let `c` be the number of complete root blocks in the full state and let `delta` be the dimension of the full relation space in the standard 15-dimensional `T` quotient.

Here

```text
t=8,
p=3,
```

so

```text
D = 8 + 3c + 3 - 3 delta.
```

The branch value `D=-1` is equivalent to

```text
delta = c+4.
```

Since `d_root=1`, the complete-root relation rows have rank `c-1`. The coefficient space `P<=Q^8` has rank three, so its nullspace has dimension five. Hence the absolute maximum possible total relation rank is

```text
(c-1)+5 = c+4.
```

Thus `D=-1` requires **all five external nullspace relation rows to be independent modulo the complete-root relation span**.

Consequently, in the touched-only five-vertex state, where the complete-root span has rank six, a necessary condition is

```text
rank(root relations + five external relations) = 11.
```

If those five external relations already lie in the rank-six touched-root span, adding untouched complete blocks cannot repair the failure.

## 3. Exact finite census

Fix `W={1,2,3,4,5}` by the `S_7` action. There are 15 no-root four-cycles supported inside `W`, three on each of the five tetrahedra.

The only allowed support multiplicity profiles are

```text
(3,2,1,1,1),
(2,2,2,1,1).
```

They produce exactly

```text
4050
```

distinct eight-cycle sets. Reducing by the `S_5` action on `W` gives

```text
43
```

cycle-set orbits.

For each orbit representative, enumerate all three-singleton triples among the ten triangles of `W` which do not share a common edge. There are

```text
120 - 10 = 110
```

such triples. At each singleton there are three root-row directions. Therefore the reduced direction census has

```text
43 * 110 * 3^3 = 127710
```

candidate states.

For each state the verifier forms the three exact singleton coefficient rows `ell_1,ell_2,ell_3`. It requires rank three and computes the generalized weights of their span from the eight projective columns. The already-proved branch floors are

```text
(d_1,d_2,d_3) >= (2,4,5).
```

Exactly

```text
36106
```

orbit-representative direction states pass these generalized-weight tests.

For every one of these 36,106 states, form the seven complete-root relation rows and the five external nullspace relation rows using the exact K8 normal form. The resulting relation rank is always

```text
6.
```

The complete-root rows already have rank six. Hence **all five external relation rows lie in the touched complete-root relation span** for every generalized-weight-admissible five-support state.

This is incompatible with the required rank eleven.

Therefore:

> **Theorem.** The `m=5` subbranch of the eight-no-root `k=5,D=-1,d_root=1,p=3` branch is empty.

No optional untouched complete blocks can restore the branch: their quotient components against the eight no-root cycles are zero, so they add only root relation rows and cannot recover the missing five external directions.

## 4. Exactness of the finite rank computation

The verifier uses integer relation rows and reduces them modulo

```text
P = 2^127 - 1.
```

The base verifier certifies this Mersenne prime with Lucas-Lehmer. In the present census the maximum squared Euclidean norm of any integer relation row is

```text
B = 84.
```

The verifier checks

```text
P^2 > B^15.
```

By Hadamard, every nonzero minor of order at most 15 has absolute value strictly less than `P`. Therefore reduction modulo `P` preserves the exact rational rank. The rank-six census is a rational certificate, not a probabilistic finite-field heuristic.

## 5. Remaining finite target

The `D=-1,k=5,d_root=1,p=3` branch now has only:

```text
m=3: multiplicity (3,3,2), singleton-incidence rank at least 2;

m=4: multiplicity (3,3,1,1), (3,2,2,1), or (2,2,2,2),
     singleton-incidence rank exactly 3.
```

The five-support case is closed and should not be revisited unless an earlier structural input is changed.

The other open `k=5` arithmetic branches remain

```text
D=-2, (d_root,p)=(0,5),
D=-1, (d_root,p)=(0,6).
```

No theorem-state authority file is changed by this note.
